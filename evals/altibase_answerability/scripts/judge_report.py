#!/usr/bin/env python3
"""Judge Altibase answerability answers and write readiness reports.

This script consumes attachments-only answer records from answer_runner.py and compares
them with the judge-only, source-backed question records. The default rule judge is
deterministic and offline: it uses canonical-English expected facts, required technical
tokens, prohibited claims, source-language metadata, and readiness thresholds without
calling a live model.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import sys
import tempfile
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any


BENCHMARK_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_DIR = BENCHMARK_ROOT / "schemas"
SEVERITY_RANK = {"none": 0, "low": 1, "medium": 2, "high": 3, "blocker": 4}
PROTECTED_TOPICS = {
    "backup_recovery",
    "destructive_sql",
    "security_tls",
    "replication_state_changes",
    "version_sensitive_property_changes",
}
AGGREGATE_DIMENSIONS = [
    "domain",
    "subdomain",
    "user_level",
    "version_scope",
    "answer_type",
    "retrieval_risk",
]
STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "before",
    "both",
    "by",
    "can",
    "cannot",
    "do",
    "does",
    "for",
    "from",
    "has",
    "have",
    "if",
    "in",
    "into",
    "is",
    "it",
    "its",
    "not",
    "of",
    "on",
    "only",
    "or",
    "should",
    "so",
    "that",
    "the",
    "then",
    "this",
    "to",
    "until",
    "use",
    "uses",
    "using",
    "when",
    "while",
    "with",
}
NEGATION_TERMS = {
    "not",
    "never",
    "no",
    "cannot",
    "can't",
    "do not",
    "does not",
    "must not",
    "without",
    "unsupported",
}
REQUEST_TERMS = {
    "ask",
    "check",
    "collect",
    "confirm",
    "exact",
    "need",
    "needs",
    "provide",
    "request",
    "share",
    "verify",
}
DETAIL_TERMS = {
    "command",
    "definition",
    "environment",
    "file",
    "log",
    "object",
    "patch",
    "path",
    "server",
    "sql",
    "trace",
    "version",
}


class JudgeError(Exception):
    """Raised for invalid judge inputs or configuration."""


@dataclass(frozen=True)
class FactMatch:
    covered: bool
    term_score: float
    technical_score: float
    notes: str


@dataclass(frozen=True)
class JudgeRunResult:
    judgments_path: Path
    aggregate_report_path: Path
    markdown_report_path: Path
    judgment_count: int
    readiness_decision: str


def repo_rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def utc_now() -> str:
    return (
        dt.datetime.now(dt.timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def canonical_json(data: Any) -> str:
    return json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def digest_text(text: str) -> str:
    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()


def rate(value: float) -> float:
    if value < 0:
        return 0.0
    if value > 1:
        return 1.0
    return round(value, 4)


def mean(values: list[float], default: float = 1.0) -> float:
    if not values:
        return default
    return rate(sum(values) / len(values))


def max_severity(severities: list[str]) -> str:
    if not severities:
        return "none"
    return max(severities, key=lambda item: SEVERITY_RANK[item])


def load_json(path: Path) -> dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except FileNotFoundError as exc:
        raise JudgeError(f"Missing JSON file: {repo_rel(path)}") from exc
    except json.JSONDecodeError as exc:
        raise JudgeError(f"Invalid JSON in {repo_rel(path)}:{exc.lineno}:{exc.colno}: {exc.msg}") from exc
    if not isinstance(data, dict):
        raise JudgeError(f"Expected JSON object: {repo_rel(path)}")
    return data


def resolve_repo_path(path_text: str, label: str) -> Path:
    path = Path(path_text)
    if path.is_absolute():
        return path.resolve()
    resolved = (REPO_ROOT / path).resolve()
    try:
        resolved.relative_to(REPO_ROOT)
    except ValueError as exc:
        raise JudgeError(f"{label} escapes repository root: {path_text}") from exc
    return resolved


def expand_question_files(manifest: dict[str, Any]) -> list[Path]:
    resolved_files: list[Path] = []
    for pattern in manifest.get("question_files", []):
        if any(char in pattern for char in "*?[]"):
            matches = sorted((REPO_ROOT / path).resolve() for path in REPO_ROOT.glob(pattern))
            if not matches:
                raise JudgeError(f"Question file glob matched no files: {pattern}")
            resolved_files.extend(matches)
        else:
            resolved_files.append(resolve_repo_path(pattern, "question_files"))

    seen: set[Path] = set()
    unique_files: list[Path] = []
    for path in resolved_files:
        if path in seen:
            raise JudgeError(f"Duplicate resolved question file: {repo_rel(path)}")
        seen.add(path)
        if path.suffix != ".jsonl":
            raise JudgeError(f"Question file must be JSONL: {repo_rel(path)}")
        if not path.exists():
            raise JudgeError(f"Question file does not exist: {repo_rel(path)}")
        unique_files.append(path)
    return unique_files


def load_questions(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    for question_file in expand_question_files(manifest):
        with question_file.open("r", encoding="utf-8") as handle:
            for line_no, line in enumerate(handle, start=1):
                stripped = line.strip()
                if not stripped:
                    continue
                try:
                    record = json.loads(stripped)
                except json.JSONDecodeError as exc:
                    raise JudgeError(
                        f"Invalid JSONL in {repo_rel(question_file)}:{line_no}:{exc.colno}: {exc.msg}"
                    ) from exc
                if not isinstance(record, dict):
                    raise JudgeError(f"{repo_rel(question_file)}:{line_no} must be a JSON object")
                question_id = record.get("id")
                if not isinstance(question_id, str) or not question_id:
                    raise JudgeError(f"{repo_rel(question_file)}:{line_no} has no question id")
                if question_id in seen_ids:
                    raise JudgeError(f"Duplicate question id selected by manifest: {question_id}")
                seen_ids.add(question_id)
                records.append(record)
    return records


def load_answer_records(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    try:
        handle = path.open("r", encoding="utf-8")
    except FileNotFoundError as exc:
        raise JudgeError(f"Missing answer JSONL file: {repo_rel(path)}") from exc
    with handle:
        for line_no, line in enumerate(handle, start=1):
            stripped = line.strip()
            if not stripped:
                continue
            try:
                record = json.loads(stripped)
            except json.JSONDecodeError as exc:
                raise JudgeError(
                    f"Invalid answer JSONL in {repo_rel(path)}:{line_no}:{exc.colno}: {exc.msg}"
                ) from exc
            if not isinstance(record, dict):
                raise JudgeError(f"{repo_rel(path)}:{line_no} must be a JSON object")
            question_id = record.get("question_id")
            if not isinstance(question_id, str) or not question_id:
                raise JudgeError(f"{repo_rel(path)}:{line_no} has no question_id")
            if question_id in seen_ids:
                raise JudgeError(f"Duplicate answer for question id: {question_id}")
            seen_ids.add(question_id)
            records.append(record)
    if not records:
        raise JudgeError(f"No answer records found in {repo_rel(path)}")
    return records


def filter_questions(
    questions: list[dict[str, Any]],
    question_ids: list[str] | None,
    limit: int | None,
) -> list[dict[str, Any]]:
    selected = questions
    if question_ids:
        wanted = set(question_ids)
        selected = [record for record in selected if record.get("id") in wanted]
        missing = sorted(wanted - {record.get("id") for record in selected})
        if missing:
            raise JudgeError(f"Requested question id(s) not found: {', '.join(missing)}")
    if limit is not None:
        selected = selected[:limit]
    if not selected:
        raise JudgeError("No questions selected")
    return selected


def load_schema_validator(schema_name: str) -> Any:
    try:
        from jsonschema import Draft202012Validator, FormatChecker
    except ImportError as exc:
        raise JudgeError("validate-output requires the Python package 'jsonschema'") from exc
    schema = load_json(SCHEMA_DIR / schema_name)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def validate_instance(data: dict[str, Any], validator: Any, label: str) -> list[str]:
    return [
        f"{label} {list(error.path)}: {error.message}"
        for error in sorted(validator.iter_errors(data), key=lambda item: list(item.path))
    ]


def normalize_text(value: str) -> str:
    lowered = value.lower()
    lowered = lowered.replace("'", "")
    lowered = lowered.replace('"', "")
    lowered = lowered.replace("`", "")
    lowered = re.sub(r"[^a-z0-9_$#./:+*^<>=-]+", " ", lowered)
    return re.sub(r"\s+", " ", lowered).strip()


def text_terms(value: str) -> list[str]:
    tokens = re.findall(r"[a-z0-9_$#./:+*^<>=-]+", normalize_text(value))
    terms: list[str] = []
    for token in tokens:
        if token in STOPWORDS:
            continue
        if len(token) == 1 and not token.isdigit():
            continue
        terms.append(token)
    return terms


def term_present(answer_norm: str, term: str) -> bool:
    term_norm = normalize_text(term)
    if not term_norm:
        return False
    if re.fullmatch(r"[a-z0-9_]+", term_norm):
        return bool(re.search(rf"(?<![a-z0-9_]){re.escape(term_norm)}(?![a-z0-9_])", answer_norm))
    if term_norm in answer_norm:
        return True
    compact_answer = answer_norm.replace(" ", "")
    compact_term = term_norm.replace(" ", "")
    return bool(compact_term and compact_term in compact_answer)


def literal_token_present(answer: str, token: str) -> bool:
    if re.fullmatch(r"[A-Za-z0-9_]+", token):
        return bool(re.search(rf"(?<![A-Za-z0-9_]){re.escape(token)}(?![A-Za-z0-9_])", answer))
    if token in answer:
        return True
    escaped = re.escape(token).replace(r"\ ", r"\s+")
    return bool(re.search(escaped, answer))


def technical_terms(value: str) -> set[str]:
    terms: set[str] = set()
    for quoted in re.findall(r"`([^`]+)`", value):
        if quoted.strip():
            terms.add(quoted.strip())
    for token in re.findall(r"[$A-Za-z0-9_./:+*^#<>=-]+", value):
        stripped = token.strip(".,;:()[]{}")
        if not stripped:
            continue
        has_marker = any(char in stripped for char in "$_./:+*^#<>=-")
        has_digit = any(char.isdigit() for char in stripped)
        mostly_upper = stripped.upper() == stripped and any(char.isalpha() for char in stripped)
        if has_marker or has_digit or mostly_upper:
            terms.add(stripped)
    return terms


def fact_match(fact_text: str, answer: str, required_tokens: list[str]) -> FactMatch:
    answer_norm = normalize_text(answer)
    fact_norm = normalize_text(fact_text)
    if fact_norm and fact_norm in answer_norm:
        return FactMatch(True, 1.0, 1.0, "exact normalized fact text found")

    fact_terms = sorted(set(text_terms(fact_text)))
    matched_terms = [term for term in fact_terms if term_present(answer_norm, term)]
    term_score = len(matched_terms) / len(fact_terms) if fact_terms else 1.0

    fact_technical_terms = technical_terms(fact_text)
    for token in required_tokens:
        if term_present(fact_norm, token):
            fact_technical_terms.add(token)
    matched_technical = [
        term
        for term in sorted(fact_technical_terms)
        if term_present(answer_norm, term) or literal_token_present(answer, term)
    ]
    technical_score = (
        len(matched_technical) / len(fact_technical_terms) if fact_technical_terms else 1.0
    )

    covered = (
        term_score >= 0.62
        or (technical_score >= 0.75 and term_score >= 0.45)
        or (technical_score >= 0.80 and term_score >= 0.35)
        or (technical_score == 1.0 and len(fact_technical_terms) >= 2 and term_score >= 0.25)
    )
    notes = (
        f"term_score={term_score:.2f} ({len(matched_terms)}/{len(fact_terms)}), "
        f"technical_score={technical_score:.2f} "
        f"({len(matched_technical)}/{len(fact_technical_terms)})"
    )
    return FactMatch(covered, rate(term_score), rate(technical_score), notes)


def answer_has_negation_near(answer_norm: str, claim_terms: list[str]) -> bool:
    high_value_terms = sorted(
        {term for term in claim_terms if term not in STOPWORDS and len(term) > 3},
        key=len,
        reverse=True,
    )[:4]
    for term in high_value_terms:
        pattern_before = rf"\b(?:{'|'.join(re.escape(item) for item in NEGATION_TERMS)})\b(?:\s+\S+){{0,6}}\s+{re.escape(term)}\b"
        pattern_after = rf"\b{re.escape(term)}\b(?:\s+\S+){{0,6}}\s+\b(?:{'|'.join(re.escape(item) for item in NEGATION_TERMS)})\b"
        if re.search(pattern_before, answer_norm) or re.search(pattern_after, answer_norm):
            return True
    return False


def prohibited_claim_present(claim: str, answer: str) -> tuple[bool, str]:
    answer_norm = normalize_text(answer)
    claim_norm = normalize_text(claim)
    if claim_norm and claim_norm in answer_norm:
        return True, "exact normalized prohibited claim found"

    claim_terms = sorted(set(text_terms(claim)))
    if not claim_terms:
        return False, "no claim terms"
    matched = [term for term in claim_terms if term_present(answer_norm, term)]
    score = len(matched) / len(claim_terms)
    claim_has_negation = any(term in claim_norm.split() for term in NEGATION_TERMS)
    if score >= 0.90 and not claim_has_negation and answer_has_negation_near(answer_norm, claim_terms):
        return False, f"high lexical overlap ({score:.2f}) but answer negates the claim"
    if score >= 0.90:
        return True, f"high lexical overlap with prohibited claim ({score:.2f})"
    return False, f"lexical overlap={score:.2f}"


def required_missing_input(question: dict[str, Any]) -> bool:
    combined = " ".join(
        [
            question.get("question", ""),
            question.get("scoring_notes", ""),
            " ".join(fact.get("fact", "") for fact in question.get("expected_facts", [])),
        ]
    ).lower()
    triggers = [
        "ask for",
        "before changing",
        "before destructive",
        "before proposing",
        "before recommending",
        "before changing",
        "environment",
        "exact command",
        "exact sql",
        "log excerpt",
        "object definition",
        "patch level",
        "should request",
    ]
    if any(trigger in combined for trigger in triggers):
        return True
    return question.get("answer_type") == "troubleshooting" and question.get("retrieval_risk") == "high"


def score_missing_input_handling(question: dict[str, Any], answer: str, fact_coverage: float) -> float:
    answer_terms = set(text_terms(answer))
    has_request = bool(answer_terms & REQUEST_TERMS)
    has_detail = bool(answer_terms & DETAIL_TERMS)
    required = required_missing_input(question)
    if required:
        if has_request and has_detail:
            return 1.0
        if has_request or has_detail:
            return 0.5
        return 0.0
    if fact_coverage < 0.5 and has_request and "cannot" in answer_terms:
        return 0.6
    return 1.0


def score_version_handling(question: dict[str, Any], answer: str) -> float:
    answer_norm = normalize_text(answer)
    scope = question.get("version_scope")
    if scope in {"7.1", "7.3", "8.1"}:
        if scope in answer_norm:
            return 1.0
        if "altibase" in answer_norm:
            return 0.75
        return 0.5
    if scope == "cross-version":
        version_hits = sum(1 for version in ("7.1", "7.3", "8.1") if version in answer_norm)
        if version_hits >= 2 or "cross-version" in answer_norm or "all supported" in answer_norm:
            return 1.0
        if "version" in answer_norm or "altibase" in answer_norm:
            return 0.75
        return 0.5
    if scope == "patch-specific":
        source_versions = [
            str(ref.get("version", ""))
            for ref in question.get("source_refs", [])
            if isinstance(ref, dict) and ref.get("version")
        ]
        if any(version and normalize_text(version) in answer_norm for version in source_versions):
            return 1.0
        if "patch" in answer_norm or "release note" in answer_norm or "build" in answer_norm:
            return 0.8
        return 0.4
    return 0.75


def detect_protected_topics(question: dict[str, Any]) -> set[str]:
    combined = normalize_text(
        " ".join(
            [
                question.get("domain", ""),
                question.get("subdomain", ""),
                question.get("question", ""),
                question.get("answer_type", ""),
                " ".join(question.get("required_tokens", [])),
                " ".join(fact.get("fact", "") for fact in question.get("expected_facts", [])),
                " ".join(question.get("prohibited_claims", [])),
            ]
        )
    )
    topics: set[str] = set()
    if any(term in combined for term in ["backup", "recovery", "restore", "archivelog", "resetlogs"]):
        topics.add("backup_recovery")
    if any(
        term in combined
        for term in [
            "drop tablespace",
            "discard",
            "resetlogs",
            "truncate",
            "delete all",
            "drop replication",
            "drop database",
            "drop table",
        ]
    ):
        topics.add("destructive_sql")
    if any(
        term in combined
        for term in [
            "ssl",
            "tls",
            "certificate",
            "openssl",
            "ciphersuite",
            "altibase_ssl_port_no",
            "replication_ssl_port_no",
            "security",
        ]
    ):
        topics.add("security_tls")
    if "replication" in combined and any(
        term in combined
        for term in [
            "alter replication",
            "create replication",
            "drop replication",
            "replication start",
            "replication stop",
            "rebuild",
            "reset",
            "sender",
            "receiver",
            "gap",
        ]
    ):
        topics.add("replication_state_changes")
    if question.get("domain") == "properties" and any(
        term in combined
        for term in [
            "alter system",
            "changed default",
            "default",
            "dynamic",
            "patch-specific",
            "range",
            "read-only",
            "recreating",
            "restart",
        ]
    ):
        topics.add("version_sensitive_property_changes")
    return topics & PROTECTED_TOPICS


def finding(
    severity: str,
    category: str,
    message: str,
    recommendation: str,
    source_ref_ids: list[str] | None = None,
    protected_topic: str | None = None,
) -> dict[str, Any]:
    record: dict[str, Any] = {
        "severity": severity,
        "category": category,
        "message": message,
        "recommendation": recommendation,
    }
    if source_ref_ids:
        record["source_ref_ids"] = sorted(set(source_ref_ids))
    if protected_topic:
        record["protected_topic"] = protected_topic
    return record


def judge_answer(
    run_id: str,
    manifest_id: str,
    question: dict[str, Any],
    answer_record: dict[str, Any],
    judged_at: str,
    judge_mode: str,
    judge_model: str | None,
) -> dict[str, Any]:
    answer = answer_record.get("answer", "")
    required_tokens = list(question.get("required_tokens", []))
    protected_topics = detect_protected_topics(question)
    findings: list[dict[str, Any]] = []

    fact_results: list[dict[str, Any]] = []
    for fact in question.get("expected_facts", []):
        match = fact_match(fact.get("fact", ""), answer, required_tokens)
        result = {
            "fact_id": fact["id"],
            "covered": match.covered,
            "importance": fact["importance"],
            "notes": match.notes,
        }
        fact_results.append(result)

    critical_results = [item for item in fact_results if item["importance"] == "critical"]
    fact_coverage = mean([1.0 if item["covered"] else 0.0 for item in fact_results], default=1.0)
    critical_fact_coverage = mean(
        [1.0 if item["covered"] else 0.0 for item in critical_results],
        default=1.0,
    )

    token_results: list[dict[str, Any]] = []
    for token in required_tokens:
        preserved = literal_token_present(answer, token)
        notes = "literal token found" if preserved else "literal token not found"
        token_results.append({"token": token, "preserved": preserved, "notes": notes})
    required_token_preservation = mean(
        [1.0 if item["preserved"] else 0.0 for item in token_results],
        default=1.0,
    )

    prohibited_claim_results: list[dict[str, Any]] = []
    for claim in question.get("prohibited_claims", []):
        present, notes = prohibited_claim_present(claim, answer)
        prohibited_claim_results.append({"claim": claim, "present": present, "notes": notes})
    prohibited_hits = [item for item in prohibited_claim_results if item["present"]]
    unsupported_claim_control = rate(1.0 - (len(prohibited_hits) / len(prohibited_claim_results))) if prohibited_claim_results else 1.0

    version_handling = score_version_handling(question, answer)
    altibase_specific_correctness = rate((fact_coverage * 0.6) + (required_token_preservation * 0.4))
    if "altibase" not in normalize_text(answer) and required_token_preservation < 0.5:
        altibase_specific_correctness = rate(altibase_specific_correctness * 0.7)
    missing_input_handling = score_missing_input_handling(question, answer, fact_coverage)

    status = answer_record.get("status")
    leakage_check = answer_record.get("leakage_check", {})
    if status != "answered":
        findings.append(
            finding(
                "blocker",
                "answer_status",
                f"Answer record status is {status!r}, so no reliable answer can be judged.",
                "Regenerate this answer successfully from the attachments-only runner before using readiness metrics.",
            )
        )
    if leakage_check and not leakage_check.get("passed", False):
        findings.append(
            finding(
                "blocker",
                "metadata_leakage",
                "The answer record reports a failed judge-only metadata leakage check.",
                "Fix the answer-generation projection or prompt construction and rerun the answer runner.",
            )
        )

    missed_critical = [
        fact
        for fact, result in zip(question.get("expected_facts", []), fact_results, strict=False)
        if fact.get("importance") == "critical" and not result["covered"]
    ]
    missed_supporting = [
        fact
        for fact, result in zip(question.get("expected_facts", []), fact_results, strict=False)
        if fact.get("importance") == "supporting" and not result["covered"]
    ]
    if missed_critical:
        severity = "blocker" if protected_topics and critical_fact_coverage < 0.75 else "high"
        source_ref_ids = sorted(
            {
                source_ref_id
                for fact in missed_critical
                for source_ref_id in fact.get("source_ref_ids", [])
            }
        )
        protected_topic = sorted(protected_topics)[0] if severity == "blocker" and protected_topics else None
        findings.append(
            finding(
                severity,
                "missing_critical_facts",
                f"Missed {len(missed_critical)} critical expected fact(s).",
                "Remediate the relevant attachment blocks or improve answer retrieval so all critical expected facts are covered.",
                source_ref_ids=source_ref_ids,
                protected_topic=protected_topic,
            )
        )
    if missed_supporting and fact_coverage < 0.80:
        findings.append(
            finding(
                "medium",
                "missing_supporting_facts",
                f"Missed {len(missed_supporting)} supporting expected fact(s).",
                "Review whether the attachment answer path should include these supporting details.",
            )
        )

    missing_tokens = [item["token"] for item in token_results if not item["preserved"]]
    if missing_tokens:
        severity = "blocker" if protected_topics and required_token_preservation < 0.75 else "medium"
        protected_topic = sorted(protected_topics)[0] if severity == "blocker" and protected_topics else None
        findings.append(
            finding(
                severity,
                "missing_required_tokens",
                f"Required technical token(s) were not preserved literally: {', '.join(missing_tokens[:12])}.",
                "Ensure the attachment context and answer preserve SQL, property, command, view, error, API, and version tokens exactly.",
                protected_topic=protected_topic,
            )
        )

    for hit in prohibited_hits:
        severity = "blocker" if protected_topics else "high"
        protected_topic = sorted(protected_topics)[0] if protected_topics else None
        findings.append(
            finding(
                severity,
                "prohibited_claim",
                f"Answer appears to contain prohibited claim: {hit['claim']}",
                "Remove unsupported or unsafe guidance and align the answer with the source-backed expected facts.",
                protected_topic=protected_topic,
            )
        )

    if version_handling < 0.6:
        findings.append(
            finding(
                "medium",
                "version_handling",
                "The answer does not handle the question's version scope clearly enough.",
                "State the applicable Altibase version, patch, or cross-version boundary and avoid unsupported broadening.",
            )
        )
    if missing_input_handling < 0.5:
        severity = "high" if protected_topics or question.get("answer_type") == "troubleshooting" else "medium"
        findings.append(
            finding(
                severity,
                "missing_input_handling",
                "The answer does not request required environment, log, patch, object, or SQL details before risky guidance.",
                "Ask only for the missing details needed for a safe source-backed next check.",
            )
        )

    protected_topic_blockers = sorted(
        {
            item.get("protected_topic")
            for item in findings
            if item.get("severity") == "blocker" and item.get("protected_topic")
        }
    )
    severity = max_severity([item["severity"] for item in findings])
    overall = rate(
        (fact_coverage * 0.30)
        + (critical_fact_coverage * 0.22)
        + (required_token_preservation * 0.14)
        + (version_handling * 0.10)
        + (altibase_specific_correctness * 0.10)
        + (unsupported_claim_control * 0.08)
        + (missing_input_handling * 0.06)
    )
    if status != "answered" or (leakage_check and not leakage_check.get("passed", False)):
        overall = 0.0

    passed = (
        severity in {"none", "low"}
        and overall >= 0.80
        and critical_fact_coverage >= 0.80
        and required_token_preservation >= 0.80
        and unsupported_claim_control == 1.0
    )

    record: dict[str, Any] = {
        "$schema": "../schemas/judgment.schema.json",
        "judgment_id": f"{run_id}:{question['id']}:rule:{digest_text(answer)[:18]}",
        "run_id": run_id,
        "manifest_id": manifest_id,
        "question_id": question["id"],
        "answer_record_id": f"{answer_record.get('run_id', run_id)}:{question['id']}",
        "judged_at": judged_at,
        "judge_mode": judge_mode,
        "scores": {
            "fact_coverage": fact_coverage,
            "critical_fact_coverage": critical_fact_coverage,
            "required_token_preservation": required_token_preservation,
            "version_handling": rate(version_handling),
            "altibase_specific_correctness": altibase_specific_correctness,
            "unsupported_claim_control": unsupported_claim_control,
            "missing_input_handling": rate(missing_input_handling),
            "overall": overall,
        },
        "passed": passed,
        "max_severity": severity,
        "fact_results": fact_results,
        "token_results": token_results,
        "prohibited_claim_results": prohibited_claim_results,
        "findings": findings,
        "protected_topic_blockers": protected_topic_blockers,
    }
    if judge_model:
        record["judge_model"] = judge_model
    return record


def group_metrics(judgments: list[dict[str, Any]]) -> dict[str, float]:
    if not judgments:
        return {
            "pass_rate": 0.0,
            "fact_coverage": 0.0,
            "critical_fact_coverage": 0.0,
            "required_token_preservation": 0.0,
            "unsupported_claim_rate": 0.0,
            "version_handling": 0.0,
            "altibase_specific_correctness": 0.0,
            "missing_input_handling": 0.0,
        }
    count = len(judgments)
    unsupported_hits = sum(
        1
        for judgment in judgments
        if any(item["present"] for item in judgment.get("prohibited_claim_results", []))
    )
    return {
        "pass_rate": rate(sum(1 for item in judgments if item["passed"]) / count),
        "fact_coverage": mean([item["scores"]["fact_coverage"] for item in judgments]),
        "critical_fact_coverage": mean(
            [item["scores"]["critical_fact_coverage"] for item in judgments]
        ),
        "required_token_preservation": mean(
            [item["scores"]["required_token_preservation"] for item in judgments]
        ),
        "unsupported_claim_rate": rate(unsupported_hits / count),
        "version_handling": mean([item["scores"]["version_handling"] for item in judgments]),
        "altibase_specific_correctness": mean(
            [item["scores"]["altibase_specific_correctness"] for item in judgments]
        ),
        "missing_input_handling": mean(
            [item["scores"]["missing_input_handling"] for item in judgments]
        ),
    }


def aggregate_by_dimension(
    questions_by_id: dict[str, dict[str, Any]],
    judgments: list[dict[str, Any]],
    dimension: str,
) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for judgment in judgments:
        question = questions_by_id[judgment["question_id"]]
        key = str(question.get(dimension, "<missing>"))
        grouped[key].append(judgment)

    summaries: list[dict[str, Any]] = []
    for key, items in sorted(grouped.items()):
        summaries.append(
            {
                "key": key,
                "questions": len(items),
                "passed": sum(1 for item in items if item["passed"]),
                "failed": sum(1 for item in items if not item["passed"]),
                "metrics": group_metrics(items),
                "max_severity": max_severity([item["max_severity"] for item in items]),
            }
        )
    return summaries


def readiness_decision(
    metrics: dict[str, float],
    aggregates: dict[str, list[dict[str, Any]]],
    protected_topic_blockers: list[dict[str, Any]],
    thresholds: dict[str, Any],
    invalid_run: bool,
) -> tuple[str, list[str]]:
    if invalid_run:
        return "invalid_run", ["The run has missing answers, validation errors, or no judgments."]

    failures: list[str] = []
    if metrics["pass_rate"] < thresholds["overall_pass_rate_minimum"]:
        failures.append("overall pass rate below threshold")
    domain_pass_rates = [item["metrics"]["pass_rate"] for item in aggregates["domain"]]
    if domain_pass_rates and min(domain_pass_rates) < thresholds["domain_pass_rate_minimum"]:
        failures.append("one or more domains below pass-rate threshold")
    if metrics["critical_fact_coverage"] < thresholds["critical_fact_coverage_minimum"]:
        failures.append("critical fact coverage below threshold")
    if metrics["required_token_preservation"] < thresholds["required_token_preservation_minimum"]:
        failures.append("required token preservation below threshold")
    if metrics["unsupported_claim_rate"] > thresholds["unsupported_claim_rate_maximum"]:
        failures.append("unsupported-claim rate above threshold")
    blocker_count = sum(item["count"] for item in protected_topic_blockers)
    if blocker_count > thresholds["protected_topic_blockers_allowed"]:
        failures.append("protected-topic blocker findings present")

    if not failures:
        return "ready_for_upload", []
    if blocker_count > thresholds["protected_topic_blockers_allowed"]:
        return "blocking_gaps", failures
    if metrics["pass_rate"] < thresholds["overall_pass_rate_minimum"] * 0.85:
        return "blocking_gaps", failures
    if metrics["critical_fact_coverage"] < thresholds["critical_fact_coverage_minimum"] * 0.85:
        return "blocking_gaps", failures
    return "targeted_remediation", failures


def top_remediation_targets(
    questions_by_id: dict[str, dict[str, Any]],
    judgments: list[dict[str, Any]],
    limit: int = 10,
) -> list[dict[str, Any]]:
    buckets: dict[tuple[str, str], dict[str, Any]] = {}
    for judgment in judgments:
        if judgment["passed"]:
            continue
        question = questions_by_id[judgment["question_id"]]
        domain = question["domain"]
        for item in judgment.get("findings", []):
            if item["severity"] == "low":
                continue
            key = (domain, item["category"])
            bucket = buckets.setdefault(
                key,
                {
                    "domain": domain,
                    "issue": item["category"],
                    "recommendation": item["recommendation"],
                    "question_ids": set(),
                    "severity_rank": SEVERITY_RANK[item["severity"]],
                },
            )
            bucket["question_ids"].add(judgment["question_id"])
            bucket["severity_rank"] = max(bucket["severity_rank"], SEVERITY_RANK[item["severity"]])

    ordered = sorted(
        buckets.values(),
        key=lambda item: (-item["severity_rank"], -len(item["question_ids"]), item["domain"], item["issue"]),
    )
    targets: list[dict[str, Any]] = []
    for item in ordered[:limit]:
        targets.append(
            {
                "domain": item["domain"],
                "issue": item["issue"],
                "recommendation": item["recommendation"],
                "question_ids": sorted(item["question_ids"]),
            }
        )
    return targets


def build_aggregate_report(
    manifest: dict[str, Any],
    policy: dict[str, Any],
    questions_by_id: dict[str, dict[str, Any]],
    selected_question_count: int,
    answer_count: int,
    judgments: list[dict[str, Any]],
    answers_path: Path,
    judgments_path: Path,
    markdown_report_path: Path,
    invalid_run: bool,
    generated_at: str,
) -> dict[str, Any]:
    metrics = group_metrics(judgments)
    aggregates = {
        dimension: aggregate_by_dimension(questions_by_id, judgments, dimension)
        for dimension in AGGREGATE_DIMENSIONS
    }
    protected_counter: dict[str, set[str]] = defaultdict(set)
    for judgment in judgments:
        for topic in judgment.get("protected_topic_blockers", []):
            protected_counter[topic].add(judgment["question_id"])
    protected_topic_blockers = [
        {
            "topic": topic,
            "count": len(question_ids),
            "question_ids": sorted(question_ids),
        }
        for topic, question_ids in sorted(protected_counter.items())
    ]
    thresholds = policy["readiness_thresholds"]
    decision, decision_reasons = readiness_decision(
        metrics,
        aggregates,
        protected_topic_blockers,
        thresholds,
        invalid_run,
    )
    if decision == "ready_for_upload":
        summary = "Readiness thresholds are met with no protected-topic blockers."
    else:
        summary = "Readiness decision: " + decision + ". " + "; ".join(decision_reasons)

    return {
        "$schema": "../schemas/aggregate_report.schema.json",
        "report_id": f"{manifest['manifest_id']}_{judgments[0]['run_id'] if judgments else 'empty'}_aggregate",
        "manifest_id": manifest["manifest_id"],
        "run_id": judgments[0]["run_id"] if judgments else "empty",
        "generated_at": generated_at,
        "readiness_decision": decision,
        "thresholds": thresholds,
        "totals": {
            "questions": selected_question_count,
            "answers": answer_count,
            "judgments": len(judgments),
            "passed": sum(1 for item in judgments if item["passed"]),
            "failed": sum(1 for item in judgments if not item["passed"]),
        },
        "overall_metrics": metrics,
        "aggregates": aggregates,
        "protected_topic_blockers": protected_topic_blockers,
        "top_remediation_targets": top_remediation_targets(questions_by_id, judgments),
        "artifacts": {
            "manifest_path": repo_rel(resolve_repo_path(manifest.get("_path", ""), "manifest_path"))
            if manifest.get("_path")
            else "",
            "answers_path": repo_rel(answers_path),
            "judgments_path": repo_rel(judgments_path),
            "markdown_report_path": repo_rel(markdown_report_path),
        },
        "summary": summary,
    }


def metric_percent(value: float) -> str:
    return f"{value * 100:.1f}%"


def markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def write_markdown_report(report: dict[str, Any], output_path: Path) -> None:
    metrics = report["overall_metrics"]
    lines = [
        "# Altibase Answerability Readiness Report",
        "",
        f"- Manifest: `{report['manifest_id']}`",
        f"- Run: `{report['run_id']}`",
        f"- Generated: `{report['generated_at']}`",
        f"- Readiness decision: `{report['readiness_decision']}`",
        "",
        "## Summary",
        "",
        report["summary"],
        "",
        "## Overall Metrics",
        "",
        markdown_table(
            ["Metric", "Value", "Threshold"],
            [
                [
                    "Pass rate",
                    metric_percent(metrics["pass_rate"]),
                    metric_percent(report["thresholds"]["overall_pass_rate_minimum"]),
                ],
                [
                    "Critical fact coverage",
                    metric_percent(metrics["critical_fact_coverage"]),
                    metric_percent(report["thresholds"]["critical_fact_coverage_minimum"]),
                ],
                [
                    "Required token preservation",
                    metric_percent(metrics["required_token_preservation"]),
                    metric_percent(report["thresholds"]["required_token_preservation_minimum"]),
                ],
                [
                    "Unsupported-claim rate",
                    metric_percent(metrics["unsupported_claim_rate"]),
                    "<= " + metric_percent(report["thresholds"]["unsupported_claim_rate_maximum"]),
                ],
                [
                    "Version handling",
                    metric_percent(metrics["version_handling"]),
                    "Tracked",
                ],
                [
                    "Altibase-specific correctness",
                    metric_percent(metrics["altibase_specific_correctness"]),
                    "Tracked",
                ],
                [
                    "Missing-input handling",
                    metric_percent(metrics["missing_input_handling"]),
                    "Tracked",
                ],
            ],
        ),
        "",
        "## Domain Results",
        "",
        markdown_table(
            ["Domain", "Questions", "Passed", "Failed", "Pass Rate", "Max Severity"],
            [
                [
                    item["key"],
                    str(item["questions"]),
                    str(item["passed"]),
                    str(item["failed"]),
                    metric_percent(item["metrics"]["pass_rate"]),
                    item["max_severity"],
                ]
                for item in report["aggregates"]["domain"]
            ],
        ),
        "",
        "## Protected Topic Blockers",
        "",
    ]
    if report["protected_topic_blockers"]:
        lines.append(
            markdown_table(
                ["Topic", "Count", "Question IDs"],
                [
                    [item["topic"], str(item["count"]), ", ".join(item.get("question_ids", []))]
                    for item in report["protected_topic_blockers"]
                ],
            )
        )
    else:
        lines.append("No protected-topic blockers.")
    lines.extend(["", "## Top Remediation Targets", ""])
    if report.get("top_remediation_targets"):
        lines.append(
            markdown_table(
                ["Domain", "Issue", "Questions", "Recommendation"],
                [
                    [
                        item["domain"],
                        item["issue"],
                        ", ".join(item.get("question_ids", [])),
                        item["recommendation"],
                    ]
                    for item in report["top_remediation_targets"]
                ],
            )
        )
    else:
        lines.append("No remediation targets.")
    lines.extend(
        [
            "",
            "## Artifacts",
            "",
            f"- Answers: `{report['artifacts']['answers_path']}`",
            f"- Judgments: `{report['artifacts']['judgments_path']}`",
            f"- Aggregate JSON: `{repo_rel(output_path.parent / 'aggregate_report.json')}`",
        ]
    )
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def default_output_dir(manifest: dict[str, Any], run_id: str) -> Path:
    base = manifest.get("reporting", {}).get("output_dir", "evals/altibase_answerability/reports")
    return resolve_repo_path(f"{base}/runs/{run_id}/judge", "output_dir")


def run_judge(
    manifest_path: Path,
    answers_path: Path,
    policy_path: Path,
    output_dir: Path | None,
    question_ids: list[str] | None,
    limit: int | None,
    judge_mode: str,
    judge_model: str | None,
    validate_output: bool,
) -> JudgeRunResult:
    manifest = load_json(manifest_path)
    manifest["_path"] = repo_rel(manifest_path)
    policy = load_json(policy_path)
    if judge_mode != "rule":
        raise JudgeError("Only judge mode 'rule' is implemented for offline J012 tooling")

    selected_questions = filter_questions(load_questions(manifest), question_ids, limit)
    questions_by_id = {record["id"]: record for record in selected_questions}
    answer_records = load_answer_records(answers_path)
    answer_validator = load_schema_validator("answer_record.schema.json") if validate_output else None
    if answer_validator:
        answer_errors: list[str] = []
        for record in answer_records:
            answer_errors.extend(
                validate_instance(record, answer_validator, f"answer {record['question_id']}")
            )
        if answer_errors:
            raise JudgeError("Answer record schema validation failed: " + "; ".join(answer_errors[:10]))
    answer_ids = {record["question_id"] for record in answer_records}
    missing_answers = sorted(set(questions_by_id) - answer_ids)
    extra_answers = sorted(answer_ids - set(questions_by_id))
    if missing_answers:
        raise JudgeError(
            "Answer file is missing selected question id(s): " + ", ".join(missing_answers[:20])
        )
    if extra_answers:
        raise JudgeError(
            "Answer file contains question id(s) outside the selected manifest/filter: "
            + ", ".join(extra_answers[:20])
        )

    run_ids = {str(record.get("run_id", "")) for record in answer_records if record.get("run_id")}
    run_id = sorted(run_ids)[0] if len(run_ids) == 1 else f"mixed_{digest_text(repo_rel(answers_path))[-12:]}"
    destination = output_dir or default_output_dir(manifest, run_id)
    if not destination.is_absolute():
        destination = (REPO_ROOT / destination).resolve()
    destination.mkdir(parents=True, exist_ok=True)

    judged_at = utc_now()
    judgments: list[dict[str, Any]] = []
    for answer_record in answer_records:
        question = questions_by_id[answer_record["question_id"]]
        judgments.append(
            judge_answer(
                run_id=run_id,
                manifest_id=manifest["manifest_id"],
                question=question,
                answer_record=answer_record,
                judged_at=judged_at,
                judge_mode=judge_mode,
                judge_model=judge_model,
            )
        )

    judgment_validator = load_schema_validator("judgment.schema.json") if validate_output else None
    aggregate_validator = load_schema_validator("aggregate_report.schema.json") if validate_output else None
    validation_errors: list[str] = []
    if judgment_validator:
        for judgment in judgments:
            validation_errors.extend(
                validate_instance(judgment, judgment_validator, f"judgment {judgment['question_id']}")
            )
    if validation_errors:
        raise JudgeError("Judgment schema validation failed: " + "; ".join(validation_errors[:10]))

    judgments_path = destination / "judgments.jsonl"
    with judgments_path.open("w", encoding="utf-8") as handle:
        for judgment in judgments:
            handle.write(canonical_json(judgment) + "\n")

    markdown_path = destination / "report.md"
    aggregate_path = destination / "aggregate_report.json"
    aggregate = build_aggregate_report(
        manifest=manifest,
        policy=policy,
        questions_by_id=questions_by_id,
        selected_question_count=len(selected_questions),
        answer_count=len(answer_records),
        judgments=judgments,
        answers_path=answers_path,
        judgments_path=judgments_path,
        markdown_report_path=markdown_path,
        invalid_run=False,
        generated_at=judged_at,
    )
    if aggregate_validator:
        aggregate_errors = validate_instance(aggregate, aggregate_validator, "aggregate report")
        if aggregate_errors:
            raise JudgeError("Aggregate report schema validation failed: " + "; ".join(aggregate_errors[:10]))
    write_json(aggregate_path, aggregate)
    write_markdown_report(aggregate, markdown_path)

    return JudgeRunResult(
        judgments_path=judgments_path,
        aggregate_report_path=aggregate_path,
        markdown_report_path=markdown_path,
        judgment_count=len(judgments),
        readiness_decision=aggregate["readiness_decision"],
    )


def run_self_test(policy_path: Path) -> int:
    manifest_path = BENCHMARK_ROOT / "manifests" / "fixture_seed.json"
    answers_path = BENCHMARK_ROOT / "fixtures" / "judge_answers.jsonl"
    with tempfile.TemporaryDirectory(prefix="altibase-judge-self-test-") as tmp:
        result = run_judge(
            manifest_path=manifest_path,
            answers_path=answers_path,
            policy_path=policy_path,
            output_dir=Path(tmp),
            question_ids=["PROP-001", "OPS-001"],
            limit=None,
            judge_mode="rule",
            judge_model=None,
            validate_output=True,
        )
        judgments = load_answer_like_jsonl(result.judgments_path)
    by_id = {record["question_id"]: record for record in judgments}
    if not by_id["PROP-001"]["passed"]:
        print("SELF-TEST FAILED: PROP-001 calibration answer should pass", file=sys.stderr)
        return 1
    if by_id["OPS-001"]["passed"]:
        print("SELF-TEST FAILED: OPS-001 unsafe calibration answer should fail", file=sys.stderr)
        return 1
    if "backup_recovery" not in by_id["OPS-001"].get("protected_topic_blockers", []):
        print("SELF-TEST FAILED: OPS-001 should produce a backup_recovery blocker", file=sys.stderr)
        return 1
    print("OK: judge/report self-test passed")
    return 0


def load_answer_like_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            stripped = line.strip()
            if stripped:
                records.append(json.loads(stripped))
    return records


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, help="Benchmark manifest JSON path.")
    parser.add_argument("--answers", type=Path, help="Answer JSONL path from answer_runner.py.")
    parser.add_argument(
        "--policy",
        type=Path,
        default=BENCHMARK_ROOT / "policy.json",
        help="Benchmark policy JSON path.",
    )
    parser.add_argument("--output-dir", type=Path, help="Directory for judgments and reports.")
    parser.add_argument("--question-id", action="append", help="Judge one question id. May be repeated.")
    parser.add_argument("--limit", type=int, help="Limit selected questions after filtering.")
    parser.add_argument("--judge-mode", choices=["rule"], default="rule")
    parser.add_argument("--judge-model", help="Optional model label for hybrid/human provenance.")
    parser.add_argument(
        "--validate-output",
        action="store_true",
        help="Validate answer, judgment, and aggregate report schemas.",
    )
    parser.add_argument("--self-test", action="store_true", help="Run offline fixture self-test and exit.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    policy_path = args.policy if args.policy.is_absolute() else (REPO_ROOT / args.policy)
    try:
        if args.self_test:
            return run_self_test(policy_path.resolve())
        if not args.manifest:
            raise JudgeError("--manifest is required unless --self-test is used")
        if not args.answers:
            raise JudgeError("--answers is required unless --self-test is used")
        if args.limit is not None and args.limit < 1:
            raise JudgeError("--limit must be a positive integer")
        manifest_path = args.manifest if args.manifest.is_absolute() else (REPO_ROOT / args.manifest)
        answers_path = args.answers if args.answers.is_absolute() else (REPO_ROOT / args.answers)
        output_dir = args.output_dir
        if output_dir is not None and not output_dir.is_absolute():
            output_dir = (REPO_ROOT / output_dir).resolve()
        result = run_judge(
            manifest_path=manifest_path.resolve(),
            answers_path=answers_path.resolve(),
            policy_path=policy_path.resolve(),
            output_dir=output_dir,
            question_ids=args.question_id,
            limit=args.limit,
            judge_mode=args.judge_mode,
            judge_model=args.judge_model,
            validate_output=args.validate_output,
        )
    except JudgeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(
        "OK: wrote "
        f"{result.judgment_count} judgment(s) to {repo_rel(result.judgments_path)}; "
        f"readiness={result.readiness_decision}; report={repo_rel(result.markdown_report_path)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
