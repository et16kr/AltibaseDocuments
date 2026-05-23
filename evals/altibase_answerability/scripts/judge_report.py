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
import functools
import hashlib
import json
import os
import re
import shlex
import subprocess
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
# Subordinating conjunctions. A negation inside a clause they introduce ("if no
# rule matches, ...", "... when expr1 is not NULL") states a *condition*, not
# the claim's own polarity, so claim_is_negative() ignores such negations and
# judges polarity from the main clause alone.
SUBORDINATOR_KEYWORDS = {
    "if",
    "when",
    "whenever",
    "unless",
    "while",
    "until",
    "where",
    "wherever",
    "because",
    "since",
    "although",
    "though",
}
# Negation words that make a prohibited *claim* intrinsically negative in
# polarity when they sit in the claim's main clause ("system tablespaces cannot
# be dropped", "anonymous blocks cannot use OUTPUT bind variables"). This covers
# the "cannot / can not / may not / must not / does not / is not" phrasings:
# every two-word form contains the bare "not" token, and "cannot"/"cant" are
# listed directly. When the claim itself is negative, an answer that echoes that
# negation is *asserting* the claim; an answer that affirms the affirmative is
# safe -- see answer_asserts_negative_claim().
#
# "without" is deliberately excluded. A "may do X without Y" claim is positive
# in polarity -- "without Y" names the *prohibited behavior* (skipping the
# safeguard Y), not the claim's polarity. A protective answer that forbids that
# behavior ("do not do X until Y is confirmed") genuinely contradicts the
# claim, so the protective-negation guard must stay enabled. Disabling it for
# "without"-phrased claims flagged every careful preflight/checklist answer as
# a false positive (job-10 gate regression, 2026-05-20).
MAIN_CLAUSE_NEGATION_TOKENS = {"not", "never", "no", "cannot", "cant", "unsupported"}
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
# Single-token negation markers, used for proximity and sentence-level checks.
# Multi-word negation forms ("do not", "does not", "must not") are already
# covered by the bare "not" token after normalization.
NEGATION_TOKENS = {
    "not",
    "never",
    "no",
    "cannot",
    "cant",
    "without",
    "unsupported",
}
# Ordering keywords. A *_BEFORE keyword between term X and term Y asserts
# "X then Y"; a *_AFTER keyword between Y and X asserts the same ordering.
ORDER_BEFORE_KEYWORDS = {"before", "then", "precede", "precedes", "preceding"}
ORDER_AFTER_KEYWORDS = {"after", "following", "follows"}
# Asymmetric relation keywords. A claim "A <relation> B" asserts a direction (A
# acts on, or precedes, B); the same words with A and B swapped are a
# different -- often correct -- statement that bag-of-words cannot tell apart.
# Such a claim is flagged only when the answer asserts the *same* relation in
# the *same* direction. ("takes precedence over" is collapsed to "supersedes"
# by collapse_relation_phrases() so it parses as a single relation token.)
DIRECTION_RELATION_FAMILIES = (
    frozenset({"overrides", "override", "overriding", "overrode", "overridden"}),
    frozenset({"precedes", "precede", "preceding", "preceded"}),
    frozenset({"replaces", "replace", "replacing", "replaced"}),
    frozenset({"supersedes", "supersede", "superseding", "superseded"}),
)
DIRECTION_RELATION_KEYWORDS = frozenset().union(*DIRECTION_RELATION_FAMILIES)

# --- C2-02: optional LLM-assisted fact judge (T7-B) --------------------------
# The deterministic rule judge stays the DEFAULT and the FALLBACK. When opted in
# (--llm-fact-judge or JUDGE_LLM_FACT=1) the LLM judge adjudicates only the
# paraphrase-suspect band -- facts whose rule-judge term_score lands between
# LLM_FACT_JUDGE_BAND_LOW and LLM_FACT_JUDGE_BAND_HIGH. The band brackets the
# rule judge's 0.62 coverage threshold (see fact_match()): cycle 1 sampled the
# judge gold set around the 0.40-0.62 term_score band, and confirming that
# against the gold-set distribution (reports/full_rerun_analysis_20260520.md
# section 4) shows the rule judge's residual over-credits run from term_score
# 0.56 all the way to a full 1.00 bag-of-words overlap -- the SQL-101 / SQL-129
# paraphrase-suspect facts score 1.00 yet are wrong, because bag-of-words cannot
# tell a correct paraphrase from a near-miss even at total overlap. The band low
# bound therefore sits at 0.40 (below it the rule judge has clearly missed the
# fact) and the high bound at 1.00 so those documented over-credits are
# adjudicated. A fact matched by exact normalized fact-text containment is
# genuinely, literally covered and is never sent to the LLM.
LLM_FACT_JUDGE_BAND_LOW = 0.40
LLM_FACT_JUDGE_BAND_HIGH = 1.00
# fact_match() emits this exact note for a literal fact-text containment hit.
EXACT_FACT_MATCH_NOTE = "exact normalized fact text found"
# Provider plumbing reused from answer generation: the same command provider
# answer_runner.py shells out to (Codex CLI via codex_exec_provider.sh).
DEFAULT_LLM_FACT_JUDGE_COMMAND = str(BENCHMARK_ROOT / "scripts" / "codex_exec_provider.sh")
DEFAULT_LLM_FACT_JUDGE_CACHE = (
    BENCHMARK_ROOT / "improvement2" / "cache" / "llm_fact_judge_cache.json"
)
DEFAULT_LLM_FACT_JUDGE_TIMEOUT_SECONDS = 180
# After this many consecutive provider failures the judge stops shelling out for
# the rest of the run and falls back to the rule verdict directly, so a missing
# or broken provider never spawns a doomed subprocess for every in-band fact.
LLM_FACT_JUDGE_MAX_CONSECUTIVE_FAILURES = 3
# The LLM provider is non-deterministic, so each in-band fact is graded by a
# majority vote over this many independent provider calls (env
# JUDGE_LLM_FACT_VOTES). Voting removes the per-fact verdict flakiness that made
# the C2-04 gate spread ~3.8 pp across fresh runs (OPS-126 F01/F02 flipped on
# identical input). The majority verdict is what gets cached, so re-runs against
# a warm cache are free and stable.
DEFAULT_LLM_FACT_JUDGE_VOTES = 3
# The verdict cache is keyed by (prompt version, fact, answer). Bump this token
# whenever build_llm_fact_judge_prompt() changes so stale verdicts graded under
# an older prompt are never reused.
LLM_FACT_JUDGE_PROMPT_VERSION = "c2-04-balanced-2"


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


def answer_sample_index(record: dict[str, Any]) -> int:
    """Return an answer record's 0-based sample index (0 when absent) (C3-04).

    A legacy single-sample ``answers.jsonl`` carries no ``sample_index``; each
    such record is sample 0 of a one-sample run and is judged exactly as before.
    A multi-sample run (``ANSWER_SAMPLES`` > 1) tags every record with a 0-based
    ``sample_index``.
    """
    value = record.get("sample_index")
    if value is None:
        return 0
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise JudgeError(
            f"answer record for {record.get('question_id', '<unknown>')} has an "
            f"invalid sample_index: {value!r}"
        )
    return value


def load_answer_records(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    seen_keys: set[tuple[str, int]] = set()
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
            # A run is keyed by (question_id, sample_index) so a multi-sample
            # run's N records per question are all accepted, while a duplicate
            # of the same (question, sample) -- and any duplicate in a legacy
            # single-sample file, where every sample_index is 0 -- still errors.
            sample_index = answer_sample_index(record)
            key = (question_id, sample_index)
            if key in seen_keys:
                raise JudgeError(
                    f"Duplicate answer for question id {question_id} sample {sample_index}"
                )
            seen_keys.add(key)
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


# --- T7-A: deterministic word-form tolerance for fact-term coverage ----------
# Fact coverage used exact-word overlap, so a paraphrased-but-correct answer
# failed purely on inflection (`restarting` vs `restarted`, `changed` vs
# `change`) or on a synonymous Altibase phrasing (`reflected` vs `take effect`).
# The helpers below add a small deterministic stemmer plus a curated equivalence
# map. They make fact-TERM coverage form-tolerant only; literal required-token
# preservation (`literal_token_present`) deliberately stays exact.

# Curated equivalence classes for recurring Altibase phrasings. The rule judge
# is bag-of-words, so without these a fact and a substantively identical answer
# miss each other purely on word choice. Kept deliberately small and
# conservative -- every group below is genuinely interchangeable in Altibase
# operations docs, so tolerance never credits an answer that is actually wrong.
# Members are compared stem-first, so inflected forms need not be listed.
FACT_TERM_EQUIVALENCES: tuple[tuple[str, ...], ...] = (
    # A static / read-only property change is visible only after a server bounce.
    ("restart", "reboot"),
    # "the new value is reflected" == "the change takes effect" == "is applied".
    ("reflect", "apply", "take effect"),
    # An operator "verifies" a state by checking / validating / confirming it.
    ("verify", "check", "validate", "validation", "confirm"),
)


def lemma(word: str) -> str:
    """Reduce an English word to a coarse stem for form-tolerant fact matching.

    Deterministic and dependency-free: it strips one inflectional suffix
    (plural -s/-es/-ies, past -ed/-ied, gerund -ing) and de-doubles a trailing
    consonant left by -ed/-ing stripping (`dropped` -> `drop`). Conservative
    length guards leave very short words (`used`, `set`) intact, so tolerance
    does not bridge a fact term to an unrelated filler word.
    """
    word = word.strip()
    if len(word) > 4 and word.endswith(("ies", "ied")):
        return word[:-3] + "y"
    if len(word) > 5 and word.endswith("ing"):
        word = word[:-3]
    elif len(word) > 4 and word.endswith("ed"):
        word = word[:-2]
    else:
        if len(word) > 4 and word.endswith(("ses", "xes", "zes", "ches", "shes")):
            return word[:-2]
        if len(word) > 4 and word.endswith("es"):
            return word[:-1]
        if len(word) > 3 and word.endswith("s") and not word.endswith("ss"):
            return word[:-1]
        return word
    # Reached only after stripping -ing / -ed: de-double a trailing consonant.
    if len(word) > 3 and word[-1] == word[-2] and word[-1] not in "lsz":
        word = word[:-1]
    return word


@functools.lru_cache(maxsize=256)
def answer_word_stems(answer_norm: str) -> frozenset[str]:
    """Coarse stems of an answer's content words, for form-tolerant matching.

    Stopwords and single non-digit characters are dropped, so word-form
    tolerance can never bridge a fact term to a filler word in the answer.
    """
    stems: set[str] = set()
    for token in re.findall(r"[a-z0-9_$#./:+*^<>=-]+", answer_norm):
        cleaned = token.strip(".:")
        if not cleaned or cleaned in STOPWORDS:
            continue
        if len(cleaned) == 1 and not cleaned.isdigit():
            continue
        stems.add(lemma(cleaned))
    return frozenset(stems)


def phrase_present(answer_norm: str, answer_stems: frozenset[str], phrase: str) -> bool:
    """True when every word of an equivalence-map phrase appears in the answer.

    Each word is matched exactly or via its coarse stem. Multi-word members
    such as ``take effect`` require *every* word, so an answer that only has the
    common word (``effect``) does not spuriously trigger the equivalence.
    """
    for word in phrase.split():
        if re.search(rf"(?<![a-z0-9_]){re.escape(word)}(?![a-z0-9_])", answer_norm):
            continue
        if any(stems_match(lemma(word), candidate) for candidate in answer_stems):
            continue
        return False
    return True


def equivalent_term_present(
    answer_norm: str, answer_stems: frozenset[str], word_stem: str
) -> bool:
    """True when an equivalence-class peer of ``word_stem`` appears in the answer."""
    for group in FACT_TERM_EQUIVALENCES:
        single_stems = {lemma(member) for member in group if " " not in member}
        if word_stem not in single_stems:
            continue
        for member in group:
            if " " not in member and lemma(member) == word_stem:
                continue  # the fact term itself; its exact form was already tried
            if phrase_present(answer_norm, answer_stems, member):
                return True
    return False


def word_term_tolerant(answer_norm: str, word: str) -> bool:
    """Form-tolerant fallback for a plain-word fact term.

    The exact word-boundary check has already failed. This compares coarse
    stems so inflected variants match (``restarting`` ~ ``restarted``), then
    consults the curated equivalence map for recurring Altibase phrasings.
    """
    answer_stems = answer_word_stems(answer_norm)
    word_stem = lemma(word)
    if any(stems_match(word_stem, candidate) for candidate in answer_stems):
        return True
    return equivalent_term_present(answer_norm, answer_stems, word_stem)


def term_present(answer_norm: str, term: str) -> bool:
    term_norm = normalize_text(term)
    if not term_norm:
        return False
    # Tokenization keeps a sentence-final '.'/':' as part of a fact term
    # ("recovery.", "num."); strip it so word-form matching is not defeated by
    # punctuation. A leading '.' (".bad", ".dat") is meaningful and is kept.
    core = term_norm.rstrip(".:") or term_norm
    if re.fullmatch(r"[a-z0-9_]+", core):
        if re.search(rf"(?<![a-z0-9_]){re.escape(core)}(?![a-z0-9_])", answer_norm):
            return True
        # Word-form tolerance: coarse-stem comparison plus the equivalence map.
        return word_term_tolerant(answer_norm, core)
    if core in answer_norm:
        return True
    # A hyphenated compound ("lazy-mode") and its spaced form ("lazy mode") are
    # the same term; accept the spaced form when it appears verbatim.
    if "-" in core and core.replace("-", " ") in answer_norm:
        return True
    compact_answer = answer_norm.replace(" ", "")
    compact_term = core.replace(" ", "")
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


def env_flag(name: str) -> bool:
    """True when an environment toggle is set to an affirmative value."""
    return os.environ.get(name, "").strip().lower() in {"1", "true", "yes", "on"}


def build_llm_fact_judge_prompt(fact_text: str, answer: str) -> str:
    """Build the single, tightly scoped grading question for the LLM fact judge.

    The LLM is asked one thing only -- does the ANSWER convey the core assertion
    of the EXPECTED FACT, judged by meaning -- and to reply with a single bare
    verdict word so parse_llm_fact_verdict() can read it reliably.

    The decision rule is deliberately balanced. It must keep rejecting answers
    that state a different or opposite fact (so the rule judge's bag-of-words
    over-credits stay rejected -- this is what lifted precision to 1.00), while
    crediting a correct paraphrase that omits secondary or incidental detail (a
    strict-grader framing under-credited those genuine partial paraphrases and
    sank recall to ~0.79 in the C2-04 gate). If this prompt changes, bump
    LLM_FACT_JUDGE_PROMPT_VERSION so the verdict cache is invalidated.
    """
    return (
        "You grade one fact for an Altibase database documentation "
        "answerability benchmark. Decide ONE thing only: does the ANSWER "
        "convey the core assertion of the EXPECTED FACT?\n\n"
        "Decision rule:\n"
        "- Reply 'covered' if the ANSWER states the main point of the fact, "
        "judged by meaning. A correct paraphrase counts. Different wording, a "
        "different sentence structure, or omission of secondary or incidental "
        "detail does not matter, as long as the core assertion is present and "
        "correct. Do not require every clause or qualifier of the expected "
        "fact to appear.\n"
        "- When the fact states a rule together with an exception or "
        "qualifier, an ANSWER that correctly states the rule is covered even "
        "if it omits the exception or qualifier.\n"
        "- When the fact lists several items (for example several things that "
        "are restricted, disallowed, or returned), the ANSWER is covered if it "
        "conveys the restriction and most of the listed items; it need not "
        "name every item. But an ANSWER that names none of the listed items, "
        "or omits the restriction itself, is not covered.\n"
        "- Reply 'not_covered' only if the ANSWER omits the core assertion, "
        "contradicts it, or states a materially different or opposite claim. "
        "Wrong or opposite information is not coverage, and mere keyword "
        "overlap with no real assertion of the fact is not coverage.\n\n"
        "When the ANSWER clearly conveys the substance of the fact, prefer "
        "'covered'.\n\n"
        f"EXPECTED FACT:\n{fact_text}\n\n"
        f"ANSWER:\n{answer}\n\n"
        "Respond with exactly one word, lower-case, on its own final line: "
        "covered or not_covered."
    )


def parse_llm_fact_verdict(reply: str) -> bool | None:
    """Read a covered / not_covered verdict from a provider reply.

    Returns True for ``covered``, False for ``not_covered``, or ``None`` when no
    verdict can be read -- the caller then falls back to the rule verdict. Lines
    are scanned bottom-up because the judge asks the model to end with the
    verdict, and ``not_covered`` is tested before ``covered`` because the former
    contains the latter as a substring.
    """
    if not reply:
        return None
    for line in reversed(reply.splitlines()):
        cleaned = re.sub(r"[^a-z_ ]+", " ", line.lower())
        cleaned = re.sub(r"\s+", " ", cleaned).strip()
        if not cleaned:
            continue
        if "not_covered" in cleaned or "not covered" in cleaned:
            return False
        if "covered" in cleaned:
            return True
    return None


def majority_verdict(verdicts: list[bool]) -> bool | None:
    """Majority vote over independent LLM verdicts.

    Returns ``True`` / ``False`` for a clear majority, or ``None`` for an empty
    list or an exact tie -- on a tie the caller keeps the deterministic rule
    verdict. The LLM provider is non-deterministic per call, so voting over an
    odd number of calls is what makes a fact's verdict stable across runs.
    """
    if not verdicts:
        return None
    covered = sum(1 for verdict in verdicts if verdict)
    not_covered = len(verdicts) - covered
    if covered > not_covered:
        return True
    if not_covered > covered:
        return False
    return None


def llm_fact_judge_helper_failures() -> list[str]:
    """Deterministic self-test for the LLM fact judge's pure helpers.

    Exercises only verdict parsing and majority voting -- no provider call --
    so the judge self-test stays hermetic with the LLM judge OFF.
    """
    failures: list[str] = []
    parse_cases: list[tuple[str, bool | None]] = [
        ("the verdict is below\ncovered", True),
        ("not_covered", False),
        ("final: not covered", False),
        ("COVERED", True),
        ("maybe", None),
        ("", None),
    ]
    for reply, expected in parse_cases:
        got = parse_llm_fact_verdict(reply)
        if got is not expected:
            failures.append(
                f"parse_llm_fact_verdict({reply!r}) -> {got!r}, expected {expected!r}"
            )
    vote_cases: list[tuple[list[bool], bool | None]] = [
        ([True, True, False], True),
        ([False, False, True], False),
        ([True, False], None),
        ([True], True),
        ([], None),
    ]
    for verdicts, expected in vote_cases:
        got = majority_verdict(verdicts)
        if got is not expected:
            failures.append(
                f"majority_verdict({verdicts!r}) -> {got!r}, expected {expected!r}"
            )
    return failures


class LLMFactJudge:
    """Optional LLM-assisted adjudicator for paraphrase-suspect fact coverage.

    Opt-in (``--llm-fact-judge`` / ``JUDGE_LLM_FACT=1``); OFF by default. The
    deterministic rule judge stays the default and the fallback. This judge is
    consulted only for facts whose rule-judge ``term_score`` lands in the
    paraphrase-suspect band (see ``in_band``); a clearly covered or clearly
    missed fact keeps the rule verdict untouched.

    Verdicts are cached, keyed by a hash of ``(fact_text, answer)``, so re-runs
    are stable and cheap. On any provider error, timeout, missing provider, or
    unparseable reply the judge falls back to the rule verdict and records the
    fallback; it never raises and never hangs -- every provider call is bounded
    by ``timeout_seconds`` and a run of failures trips a circuit breaker.

    Only ``FactMatch.covered`` may be overridden; ``term_score`` /
    ``technical_score`` / literal-token preservation stay the rule judge's
    deterministic values.
    """

    def __init__(
        self,
        command: str,
        timeout_seconds: int = DEFAULT_LLM_FACT_JUDGE_TIMEOUT_SECONDS,
        cache_path: Path | None = None,
        votes: int = DEFAULT_LLM_FACT_JUDGE_VOTES,
    ) -> None:
        self.command = command
        self.timeout_seconds = max(1, int(timeout_seconds))
        self.cache_path = cache_path
        self.votes = max(1, int(votes))
        self._cache: dict[str, str] = {}
        self._cache_loaded = False
        self._consecutive_failures = 0
        self._provider_disabled = False
        self.stats: dict[str, int] = {
            "in_band": 0,
            "rule_covered_in_band": 0,
            "cache_hits": 0,
            "provider_calls": 0,
            "llm_covered": 0,
            "llm_not_covered": 0,
            "overrides": 0,
            "fallbacks": 0,
        }

    def in_band(self, rule_match: FactMatch) -> bool:
        """True when a fact is paraphrase-suspect and should be adjudicated."""
        if rule_match.notes.startswith(EXACT_FACT_MATCH_NOTE):
            return False  # literal fact-text containment -- genuinely covered
        return (
            LLM_FACT_JUDGE_BAND_LOW
            <= rule_match.term_score
            <= LLM_FACT_JUDGE_BAND_HIGH
        )

    def adjudicate(self, fact_text: str, answer: str, rule_match: FactMatch) -> FactMatch:
        """Return a FactMatch whose .covered reflects the LLM verdict in-band.

        Out-of-band facts are returned untouched. In-band, the LLM verdict
        overrides ``.covered``; on any failure the rule verdict is kept and the
        fallback is recorded in the notes and stats. ``term_score`` and
        ``technical_score`` are always the rule judge's values -- only
        ``.covered`` may change.
        """
        if not self.in_band(rule_match):
            return rule_match
        self.stats["in_band"] += 1
        if rule_match.covered:
            self.stats["rule_covered_in_band"] += 1

        verdict, origin = self._verdict(fact_text, answer)
        if verdict is None:
            self.stats["fallbacks"] += 1
            return FactMatch(
                rule_match.covered,
                rule_match.term_score,
                rule_match.technical_score,
                f"{rule_match.notes}; llm_fact_judge=fallback->rule ({origin})",
            )

        if verdict:
            self.stats["llm_covered"] += 1
        else:
            self.stats["llm_not_covered"] += 1
        if verdict != rule_match.covered:
            self.stats["overrides"] += 1
        return FactMatch(
            verdict,
            rule_match.term_score,
            rule_match.technical_score,
            f"{rule_match.notes}; llm_fact_judge="
            f"{'covered' if verdict else 'not_covered'} ({origin})",
        )

    def _verdict(self, fact_text: str, answer: str) -> tuple[bool | None, str]:
        """Return ``(verdict, origin)``; verdict None means fall back to rule.

        A fresh verdict is a majority vote over ``self.votes`` independent
        provider calls -- the LLM provider is non-deterministic per call, and
        voting removes the per-fact flakiness. The majority verdict is cached
        (keyed by prompt version + fact + answer), so a warm cache returns it
        directly. A tie, or no usable reply at all, yields ``None`` and the
        caller keeps the deterministic rule verdict.
        """
        key = digest_text(
            f"{LLM_FACT_JUDGE_PROMPT_VERSION}\x00{fact_text}\x00{answer}"
        )
        cached = self._cache_get(key)
        if cached is not None:
            self.stats["cache_hits"] += 1
            return cached == "covered", "cache"
        verdicts: list[bool] = []
        for _ in range(self.votes):
            if self._provider_disabled:
                break
            reply = self._call_provider(fact_text, answer)
            if reply is None:
                continue
            parsed = parse_llm_fact_verdict(reply)
            if parsed is not None:
                verdicts.append(parsed)
        if not verdicts:
            return None, "provider-unavailable"
        tally = f"{sum(1 for v in verdicts if v)}/{len(verdicts)} covered"
        verdict = majority_verdict(verdicts)
        if verdict is None:
            return None, f"llm-tie ({tally})"
        self._cache_put(key, "covered" if verdict else "not_covered")
        return verdict, f"llm {tally}"

    def _call_provider(self, fact_text: str, answer: str) -> str | None:
        """Shell out to the command provider; return stdout or None on failure.

        Never raises and never hangs: the call is bounded by ``timeout_seconds``
        and, once the circuit breaker has tripped, no further subprocess is
        spawned for the rest of the run.
        """
        if self._provider_disabled or not self.command:
            return None
        try:
            argv = shlex.split(self.command)
        except ValueError:
            self._record_failure()
            return None
        if not argv:
            self._record_failure()
            return None
        self.stats["provider_calls"] += 1
        prompt = build_llm_fact_judge_prompt(fact_text, answer)
        try:
            completed = subprocess.run(
                argv,
                input=prompt,
                text=True,
                capture_output=True,
                timeout=self.timeout_seconds,
                check=False,
            )
        except (OSError, subprocess.SubprocessError):
            self._record_failure()
            return None
        if completed.returncode != 0 or not completed.stdout.strip():
            self._record_failure()
            return None
        self._consecutive_failures = 0
        return completed.stdout

    def _record_failure(self) -> None:
        self._consecutive_failures += 1
        if self._consecutive_failures >= LLM_FACT_JUDGE_MAX_CONSECUTIVE_FAILURES:
            self._provider_disabled = True

    def _cache_get(self, key: str) -> str | None:
        if not self._cache_loaded:
            self._load_cache()
        return self._cache.get(key)

    def _cache_put(self, key: str, value: str) -> None:
        if not self._cache_loaded:
            self._load_cache()
        self._cache[key] = value
        self._persist_cache()

    def _load_cache(self) -> None:
        self._cache_loaded = True
        if self.cache_path is None or not self.cache_path.is_file():
            return
        try:
            raw = json.loads(self.cache_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return
        if isinstance(raw, dict):
            for key, value in raw.items():
                if value in ("covered", "not_covered"):
                    self._cache[str(key)] = value

    def _persist_cache(self) -> None:
        """Write the verdict cache atomically; a cache failure never fails a run."""
        if self.cache_path is None:
            return
        try:
            self.cache_path.parent.mkdir(parents=True, exist_ok=True)
            payload = json.dumps(
                self._cache, ensure_ascii=False, indent=2, sort_keys=True
            )
            tmp = self.cache_path.with_suffix(self.cache_path.suffix + ".tmp")
            tmp.write_text(payload + "\n", encoding="utf-8")
            tmp.replace(self.cache_path)
        except OSError:
            pass  # the cache is an optimization, never a correctness dependency


def judge_fact(
    fact_text: str,
    answer: str,
    required_tokens: list[str],
    llm_fact_judge: LLMFactJudge | None = None,
) -> FactMatch:
    """Rule-judge a fact, then let the optional LLM judge adjudicate it in-band.

    With ``llm_fact_judge`` None (the default) this is exactly ``fact_match`` --
    the deterministic rule judge, byte-for-byte. With an LLM judge supplied, a
    paraphrase-suspect fact's ``.covered`` may be overridden by the LLM verdict;
    ``term_score``, ``technical_score``, and literal required-token preservation
    are unchanged. ``fact_match`` itself stays stable for ``calibrate_judge.py``.
    """
    rule_match = fact_match(fact_text, answer, required_tokens)
    if llm_fact_judge is None:
        return rule_match
    return llm_fact_judge.adjudicate(fact_text, answer, rule_match)


def make_llm_fact_judge(
    *,
    flag: bool = False,
    command: str | None = None,
    cache_path: Path | None = None,
    timeout_seconds: int | None = None,
) -> LLMFactJudge | None:
    """Build an LLMFactJudge when opted in, else None (rule judge only).

    Enabled by the ``--llm-fact-judge`` CLI flag OR the ``JUDGE_LLM_FACT=1``
    environment toggle. The env toggle is mandatory plumbing: run-test.sh
    invokes judge_report.py with a fixed argument list and passes no judge flag,
    so the live benchmark runs reach the LLM judge only through the env toggle.
    When neither is set this returns None and judging behaves byte-for-byte like
    the deterministic rule judge. The provider command, cache path, and per-call
    timeout each fall back: explicit argument, then environment variable, then a
    built-in default (the Codex command provider, as answer_runner.py uses).
    """
    if not (flag or env_flag("JUDGE_LLM_FACT")):
        return None
    resolved_command = (
        command
        or os.environ.get("JUDGE_LLM_FACT_COMMAND", "").strip()
        or DEFAULT_LLM_FACT_JUDGE_COMMAND
    )
    if cache_path is None:
        env_cache = os.environ.get("JUDGE_LLM_FACT_CACHE", "").strip()
        cache_path = Path(env_cache) if env_cache else DEFAULT_LLM_FACT_JUDGE_CACHE
    if timeout_seconds is None:
        env_timeout = os.environ.get("JUDGE_LLM_FACT_TIMEOUT", "").strip()
        timeout_seconds = (
            int(env_timeout)
            if env_timeout.isdigit() and int(env_timeout) > 0
            else DEFAULT_LLM_FACT_JUDGE_TIMEOUT_SECONDS
        )
    env_votes = os.environ.get("JUDGE_LLM_FACT_VOTES", "").strip()
    votes = (
        int(env_votes)
        if env_votes.isdigit() and int(env_votes) > 0
        else DEFAULT_LLM_FACT_JUDGE_VOTES
    )
    return LLMFactJudge(
        command=resolved_command,
        timeout_seconds=timeout_seconds,
        cache_path=cache_path,
        votes=votes,
    )


def llm_fact_judge_summary(judge: LLMFactJudge) -> str:
    """One-line human-readable summary of an LLM fact judge's run statistics."""
    stats = judge.stats
    detail = (
        "llm fact judge: "
        f"votes={judge.votes} "
        f"in_band={stats['in_band']} "
        f"provider_calls={stats['provider_calls']} "
        f"cache_hits={stats['cache_hits']} "
        f"covered={stats['llm_covered']} not_covered={stats['llm_not_covered']} "
        f"overrides={stats['overrides']} fallbacks={stats['fallbacks']}"
    )
    if stats["in_band"] and stats["fallbacks"] == stats["in_band"]:
        detail += (
            " (provider unavailable -- every in-band fact fell back "
            "to the rule judge)"
        )
    return detail


def suffix_stem(term: str) -> str:
    """Reduce a word to a rough stem so -s/-es/-ed/-ing variants compare equal.

    This is a deliberately small, deterministic stemmer (no external data): it
    strips one inflectional suffix and de-doubles a consonant left behind by
    -ed/-ing stripping (``dropped`` -> ``drop``). It exists so the negation and
    ordering checks treat ``tablespaces`` and ``tablespace`` as the same word.
    """
    word = term
    if len(word) > 4 and word.endswith("ies"):
        return word[:-3] + "y"
    if len(word) > 5 and word.endswith("ing"):
        word = word[:-3]
    elif len(word) > 4 and word.endswith("ed"):
        word = word[:-2]
    else:
        if len(word) > 4 and word.endswith(("ses", "xes", "zes", "ches", "shes")):
            return word[:-2]
        if len(word) > 4 and word.endswith("es"):
            return word[:-1]
        if len(word) > 3 and word.endswith("s") and not word.endswith("ss"):
            return word[:-1]
        return word
    # Reached only after stripping -ing / -ed: de-double a trailing consonant.
    if len(word) > 3 and word[-1] == word[-2] and word[-1] not in "lsz":
        word = word[:-1]
    return word


def stems_match(left: str, right: str) -> bool:
    """Return True when two already-computed stems denote the same word.

    Equal stems match; otherwise a short stem that is a prefix of a slightly
    longer one is treated as a match, which forgives stemmer imperfections such
    as ``delet`` (from ``deleted``) vs ``delete``.
    """
    if left == right:
        return True
    short, long = (left, right) if len(left) <= len(right) else (right, left)
    return len(short) >= 4 and long.startswith(short) and len(long) - len(short) <= 2


def stem_in_set(stem: str, stem_set: set[str]) -> bool:
    return any(stems_match(stem, candidate) for candidate in stem_set)


def split_sentences(text: str) -> list[str]:
    """Split text into clause-level sentences for sentence-scoped checks.

    Splits on sentence-ending punctuation followed by whitespace and on line
    breaks. It does not split on a period with no following whitespace, so
    version numbers (``8.1``) and dotted paths (``altibase.properties``) stay
    intact.
    """
    parts = re.split(r"(?<=[.!?;:])\s+|[\n\r]+", text)
    return [part for part in parts if part.strip()]


def answer_has_negation_near(
    answer_norm: str, claim_terms: list[str], window: int = 8
) -> bool:
    """Return True when a high-value claim term is negated in the answer.

    Claim terms are suffix-normalized so plural/singular and verb-form variants
    match (``tablespaces`` in the claim vs ``tablespace`` in the answer's
    negation). Every high-value term is considered -- not just the longest few
    -- and the proximity window is wide enough to span a short clause.
    """
    claim_stems = {
        suffix_stem(term)
        for term in claim_terms
        if term not in STOPWORDS and len(term) > 3
    }
    if not claim_stems:
        return False
    tokens = answer_norm.split()
    negation_positions = [
        index for index, token in enumerate(tokens) if token in NEGATION_TOKENS
    ]
    if not negation_positions:
        return False
    for index, token in enumerate(tokens):
        if not stem_in_set(suffix_stem(token), claim_stems):
            continue
        if any(abs(index - negation) <= window for negation in negation_positions):
            return True
    return False


def order_side_terms(tokens: list[str]) -> list[str]:
    return [token for token in tokens if token not in STOPWORDS and len(token) > 2]


def collapse_relation_phrases(text: str) -> str:
    """Collapse the multi-word relation "takes precedence over" to one token.

    Order/direction parsing is token-based; collapsing the phrase lets
    "A takes precedence over B" be handled exactly like "A supersedes B".
    """
    return re.sub(r"\btakes?\s+precedence\s+over\b", "supersedes", text)


def direction_relation_family(token: str) -> set[str]:
    """Return the inflected forms of the asymmetric relation ``token`` belongs to."""
    for family in DIRECTION_RELATION_FAMILIES:
        if token in family:
            return set(family)
    return {token}


def parse_order_claim(
    claim_norm: str,
) -> tuple[list[str], list[str], set[str], set[str]] | None:
    """Detect an order- or direction-sensitive claim.

    Returns ``(first_terms, second_terms, forward_keywords, reverse_keywords)``
    or ``None`` for a plain claim that keeps the bag-of-words path. The claim is
    asserted by the answer when a ``forward`` keyword sits between a first-side
    term and a second-side term, or a ``reverse`` keyword sits between a
    second-side term and a first-side term, inside one un-negated sentence.

    Two claim shapes are recognised:

    * Ordering -- "X before Y" / "X after Y". For "before" the claim asserts X
      precedes Y; "after" swaps the sides. Either ordering keyword can assert it
      in the answer, so both keyword sets are returned.
    * Asymmetric relation -- "A overrides B", "A replaces B", "A precedes B",
      "A takes precedence over B". Only the same relation in the same direction
      asserts the claim, so the reverse set is empty.
    """
    tokens = collapse_relation_phrases(claim_norm).split()
    for index, token in enumerate(tokens):
        if token in ("before", "after", "then"):
            left = order_side_terms(tokens[:index])
            right = order_side_terms(tokens[index + 1 :])
            if not left or not right:
                continue
            if token == "after":
                return right, left, ORDER_BEFORE_KEYWORDS, ORDER_AFTER_KEYWORDS
            return left, right, ORDER_BEFORE_KEYWORDS, ORDER_AFTER_KEYWORDS
        if token in DIRECTION_RELATION_KEYWORDS:
            left = order_side_terms(tokens[:index])
            right = order_side_terms(tokens[index + 1 :])
            if not left or not right:
                continue
            return left, right, direction_relation_family(token), set()
    return None


def order_claim_asserted(
    first_terms: list[str],
    second_terms: list[str],
    forward_keywords: set[str],
    reverse_keywords: set[str],
    answer: str,
) -> bool:
    """Return True when the answer asserts the claim's first->second direction.

    Bag-of-words overlap cannot distinguish the prohibited "X before Y" from the
    correct "Y before X", nor "A overrides B" from "B overrides A" -- the words
    are identical. This requires a forward keyword to sit between a first-side
    term and a second-side term (or a reverse keyword between a second-side term
    and a first-side term), within a single un-negated sentence.
    """
    first_stems = {suffix_stem(term) for term in first_terms}
    second_stems = {suffix_stem(term) for term in second_terms}
    for sentence in split_sentences(answer):
        tokens = normalize_text(collapse_relation_phrases(sentence)).split()
        if not tokens or any(token in NEGATION_TOKENS for token in tokens):
            continue
        stems = [suffix_stem(token) for token in tokens]
        first_pos = [i for i, stem in enumerate(stems) if stem_in_set(stem, first_stems)]
        second_pos = [i for i, stem in enumerate(stems) if stem_in_set(stem, second_stems)]
        if not first_pos or not second_pos:
            continue
        for index, token in enumerate(tokens):
            if (
                token in forward_keywords
                and any(p < index for p in first_pos)
                and any(p > index for p in second_pos)
            ):
                return True
            if (
                reverse_keywords
                and token in reverse_keywords
                and any(p < index for p in second_pos)
                and any(p > index for p in first_pos)
            ):
                return True
    return False


def strip_markdown_emphasis(text: str) -> str:
    """Remove Markdown emphasis markers so an emphasised word tokenises plainly.

    ``**not**`` / ``*not*`` / ``_not_`` / `` `not` `` all collapse to ``not``,
    so an emphasised negation word is still recognised by the negation and
    ordering checks. Asterisks and backticks are removed outright; underscores
    are removed only at word boundaries, so identifier underscores
    (``SSL_PORT_NO``) survive.
    """
    text = text.replace("*", "").replace("`", "")
    text = re.sub(r"(?<![A-Za-z0-9])_+", "", text)
    text = re.sub(r"_+(?![A-Za-z0-9])", "", text)
    return text


# Negation words the polarity guards recognise as single tokens. A negation
# that sits inside a quoted code/example span is part of a command or verbatim
# example, not the answer's own prose -- mask_quoted_span_negations() blanks it.
QUOTED_SPAN_NEGATION_RE = re.compile(
    r"(?<![A-Za-z])(?:cannot|cant|never|not|no|without|unsupported)(?![A-Za-z])",
    re.IGNORECASE,
)
# The spans that hold commands, code, and verbatim examples rather than the
# answer's prose: fenced triple-backtick code blocks, inline backtick spans,
# and single- or double-quoted string literals. Both straight and curly quotes
# are covered, because live answers use either. The single-quote pattern is
# boundary-guarded (no surrounding letter/digit) so an apostrophe inside a word
# such as "doesn't" or "user's" does not open a spurious span.
QUOTED_SPAN_RES = (
    re.compile(r"```.*?```", re.DOTALL),
    re.compile(r"`[^`]*`"),
    re.compile("[\"“”][^\"“”]*[\"“”]"),
    re.compile(
        r"(?<![A-Za-z0-9])['‘’][^'‘’\n]*['‘’]"
        r"(?![A-Za-z0-9])"
    ),
)


def mask_quoted_span_negations(text: str) -> str:
    """Blank negation words that sit inside quoted code/example spans.

    Inline backtick spans, fenced triple-backtick code blocks, and quoted
    string literals hold commands, code, and verbatim examples rather than the
    answer's own prose. A negation token there -- for example the ``does not``
    in the CLI example ``altierr -w "does not"`` -- belongs to that example,
    not to the answer asserting a negative, so the cannot-claim polarity guard
    must not read it. Only the negation words inside such spans are blanked
    (replaced by equal-length runs of spaces); every other character -- the
    backticks and quotes themselves, technical/claim terms, and all the
    surrounding prose -- is left byte-for-byte intact, so a span-resident claim
    term still counts toward sentence coverage and only the answer's own prose
    contributes its polarity.
    """

    def blank(match: "re.Match[str]") -> str:
        return QUOTED_SPAN_NEGATION_RE.sub(
            lambda hit: " " * len(hit.group(0)), match.group(0)
        )

    for span_re in QUOTED_SPAN_RES:
        text = span_re.sub(blank, text)
    return text


def claim_is_negative(claim: str) -> bool:
    """True when a prohibited claim's own *main* clause is negative in polarity.

    A negation inside a subordinate clause ("if no rule matches, ...", "... when
    expr1 is not NULL") states a *condition*, not the claim's polarity: the
    claim "Altibase denies access by default" is positive even though its
    "if no ..." condition contains "no". Only a negation in the main clause
    ("X cannot be dropped", "anonymous blocks cannot use OUTPUT bind variables")
    makes the claim intrinsically negative. "without" is excluded -- see
    MAIN_CLAUSE_NEGATION_TOKENS.
    """
    for segment in claim.lower().replace("'", "").split(","):
        words = re.findall(r"[a-z0-9_]+", segment)
        if not words or words[0] in SUBORDINATOR_KEYWORDS:
            continue  # an empty segment or a fronted subordinate clause
        main_words: list[str] = []
        for word in words:
            if word in SUBORDINATOR_KEYWORDS:
                break  # a trailing subordinate clause starts here
            main_words.append(word)
        if any(word in MAIN_CLAUSE_NEGATION_TOKENS for word in main_words):
            return True
    return False


def answer_asserts_negative_claim(answer: str, claim_terms: list[str]) -> bool:
    """Decide whether an answer asserts an intrinsically-negative prohibited claim.

    An intrinsically-negative claim ("X cannot do Y") is asserted only when the
    answer *also* negates X near Y. Whole-answer proximity is too coarse: an
    answer can affirm the claim's point ("Unlike stored procedures, it can use
    BIND variables for ... OUTPUT") while carrying unrelated negations elsewhere
    ("It does not create or store a PSM object"). So the decision is
    sentence-scoped -- the answer sentence covering the most claim terms decides
    the polarity. If that sentence negates, the answer asserts the negative
    claim; otherwise it affirms the opposite and is safe.

    The negation read is kept on the answer's *own prose* by two C3-01
    refinements:

    * Negation tokens inside quoted code/example spans are blanked first
      (mask_quoted_span_negations), so a ``does not`` inside a CLI example such
      as ``altierr -w "does not"`` -- which is example text, not the answer's
      polarity -- cannot flip the verdict.
    * Only MAIN_CLAUSE_NEGATION_TOKENS count as a polarity-flipping negation --
      the same impossibility-negations claim_is_negative() reads on the claim
      side. "without" is excluded for the identical reason it is excluded there:
      "search ... with or without the minus sign" affirms that the search *is*
      possible; it does not assert an impossibility, so it must not be read as
      the answer echoing a ``cannot`` claim.

    raw markdown emphasis is then stripped so an emphasised negation word still
    tokenises plainly. ``answer`` is therefore the raw answer text.
    """
    answer = strip_markdown_emphasis(mask_quoted_span_negations(answer))
    claim_stems = {
        suffix_stem(term)
        for term in claim_terms
        if term not in STOPWORDS and len(term) > 3
    }
    if not claim_stems:
        return False
    best_cover = 0
    best_has_negation = False
    for sentence in split_sentences(answer):
        tokens = normalize_text(sentence).split()
        if not tokens:
            continue
        stems = {suffix_stem(token) for token in tokens}
        cover = sum(1 for stem in stems if stem_in_set(stem, claim_stems))
        if cover > best_cover:
            best_cover = cover
            best_has_negation = any(
                token in MAIN_CLAUSE_NEGATION_TOKENS for token in tokens
            )
    return best_cover > 0 and best_has_negation


def claim_has_incidental_literal_only(claim_terms: list[str], answer: str) -> bool:
    """True when a purely-numeric claim token matches only unrelated answer text.

    A claim like "SSL_PORT_NO defaults to 20300" must not be flagged when the
    answer's only "20300" sits in an unrelated TCP-listener log line. A numeric
    token is incidental unless it shares an answer sentence with another claim
    term; an incidental match means the claim's subject and predicate never
    co-occur, so the claim is not actually asserted.
    """
    numeric_terms = [
        term
        for term in claim_terms
        if any(char.isdigit() for char in term)
        and not any(char.isalpha() for char in term)
    ]
    if not numeric_terms:
        return False
    other_stems = {
        suffix_stem(term) for term in claim_terms if term not in numeric_terms
    }
    if not other_stems:
        return False
    for numeric in numeric_terms:
        co_occurs = False
        for sentence in split_sentences(answer):
            sentence_norm = normalize_text(sentence)
            if not term_present(sentence_norm, numeric):
                continue
            sentence_stems = {suffix_stem(token) for token in sentence_norm.split()}
            if any(stem_in_set(stem, other_stems) for stem in sentence_stems):
                co_occurs = True
                break
        if not co_occurs:
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

    # Markdown emphasis around a negation word ("does **not** commit") would
    # otherwise leave the negation un-tokenised. Strip emphasis markers before
    # any negation/ordering analysis; the bag-of-words overlap above keeps using
    # the untouched answer, so SQL tokens such as `*` are unaffected.
    answer_for_analysis = strip_markdown_emphasis(answer)
    answer_norm_for_analysis = normalize_text(answer_for_analysis)

    # A claim counts as intrinsically negative only when its *main* clause is
    # negative ("X cannot be dropped"). A negation confined to a subordinate
    # clause ("if no rule matches", "when expr1 is not NULL") is a condition,
    # not the claim's polarity -- see claim_is_negative().
    claim_negative = claim_is_negative(claim)

    # Order- and direction-sensitive claims ("X before Y", "A overrides B")
    # cannot be judged by bag-of-words: the same words in the other direction
    # are an allowed answer. Require both high overlap and the directed relation
    # to be asserted un-negated.
    order_relation = parse_order_claim(claim_norm)
    if order_relation is not None:
        first_terms, second_terms, forward_kw, reverse_kw = order_relation
        if score >= 0.90 and order_claim_asserted(
            first_terms, second_terms, forward_kw, reverse_kw, answer_for_analysis
        ):
            return True, f"high overlap ({score:.2f}) and answer asserts the prohibited direction"
        return False, f"order/direction-sensitive claim not asserted in the answer (overlap {score:.2f})"

    if score >= 0.90:
        # Incidental-token guard: a purely-numeric claim token ("20300") that
        # surfaces only in unrelated answer text does not assert the claim.
        if claim_has_incidental_literal_only(claim_terms, answer_for_analysis):
            return False, (
                f"high overlap ({score:.2f}) but a numeric claim token appears "
                "only in unrelated answer text"
            )
        # Bag-of-words overlap alone cannot tell an answer that asserts the
        # claim from one that asserts its opposite: "X can be searched" and
        # "X cannot be searched" share every term but "can"/"cannot". So at high
        # overlap, compare polarity -- an answer asserts the claim only when its
        # negation state matches the claim's own polarity:
        #   - positive claim ("X can be dropped"): asserted by an un-negated
        #     answer; an answer that negates near the terms contradicts it.
        #   - intrinsically-negative claim ("X cannot use OUTPUT bind
        #     variables"): asserted only by an answer whose best-covering
        #     sentence also negates; an answer that affirms the affirmative
        #     ("it can use ... OUTPUT") is safe even if it negates elsewhere.
        if claim_negative:
            # answer_asserts_negative_claim() does its own quoted-span negation
            # masking and markdown-emphasis stripping, so it takes the raw
            # answer (not answer_for_analysis, whose backticks are already
            # gone -- the quoted spans could no longer be located).
            if answer_asserts_negative_claim(answer, claim_terms):
                return True, f"high lexical overlap ({score:.2f}); answer asserts the negative claim"
            return False, f"high lexical overlap ({score:.2f}) but answer affirms the opposite"
        if answer_has_negation_near(answer_norm_for_analysis, claim_terms):
            return False, f"high lexical overlap ({score:.2f}) but answer negates the claim"
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
    thresholds: dict[str, Any],
    llm_fact_judge: LLMFactJudge | None = None,
) -> dict[str, Any]:
    answer = answer_record.get("answer", "")
    required_tokens = list(question.get("required_tokens", []))
    protected_topics = detect_protected_topics(question)
    findings: list[dict[str, Any]] = []

    fact_results: list[dict[str, Any]] = []
    for fact in question.get("expected_facts", []):
        match = judge_fact(fact.get("fact", ""), answer, required_tokens, llm_fact_judge)
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

    # --- T8: pass decision reconciled with policy.json thresholds ------------
    # The pass test used to require `severity in {"none", "low"}`. Because any
    # missed critical fact emits a `high` finding and any missed required token
    # emits a `medium` finding -- and no code path ever emits a `low` finding --
    # that clause collapsed to "zero findings", which silently overrode the
    # numeric policy thresholds: a single near-miss auto-failed a question even
    # when its critical_fact_coverage / required_token_preservation were inside
    # the bars policy.json calls acceptable. It also left every other clause as
    # dead code -- once `severity == "none"` the answer already has full
    # critical coverage, full token preservation and no prohibited claim, so the
    # hardcoded `>= 0.80` bars (which did not even match policy's 0.90 / 0.95)
    # could never bind.
    #
    # The decision is now made directly against `readiness_thresholds` in
    # policy.json. A question passes when:
    #   * no `blocker` finding is present -- an unjudgeable answer (bad status or
    #     a failed leakage check) or a protected-topic blocker
    #     (policy `protected_topic_blockers_allowed == 0`); and
    #   * critical_fact_coverage >= policy `critical_fact_coverage_minimum`; and
    #   * required_token_preservation >= policy
    #     `required_token_preservation_minimum`; and
    #   * no prohibited claim is present (per-question form of policy
    #     `unsupported_claim_rate_maximum`).
    # `high`/`medium` near-miss findings remain in the findings list as
    # remediation signal but no longer override an in-policy numeric score.
    # Each clause below is independently load-bearing: clause 1 alone catches
    # status/leakage blockers, and clauses 2-4 each fail a non-protected-topic
    # answer the others would pass.
    has_blocker_finding = any(item["severity"] == "blocker" for item in findings)
    passed = (
        not has_blocker_finding
        and critical_fact_coverage >= thresholds["critical_fact_coverage_minimum"]
        and required_token_preservation >= thresholds["required_token_preservation_minimum"]
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


# --- C3-04: multi-sample variance band --------------------------------------
# A multi-sample live run (ANSWER_SAMPLES>1) answers every question N times.
# The scorecard then reports each metric as the mean across the N samples
# together with the min-max band, so a genuine retrieval/answer gain is never
# hidden inside live answer-generation variance -- the cycle-2 rerun
# (reports/full_rerun_analysis_cycle2_20260520.md section 6, target 3) found
# the answer-generation noise floor as large as the cycle-2 signal. All eight
# group_metrics() fields vary per sample, so all eight are banded.
VARIANCE_BAND_METRICS = (
    "pass_rate",
    "fact_coverage",
    "critical_fact_coverage",
    "required_token_preservation",
    "unsupported_claim_rate",
    "version_handling",
    "altibase_specific_correctness",
    "missing_input_handling",
)


def metric_band(values: list[float]) -> dict[str, Any]:
    """Mean and min-max band for one metric across the per-sample values."""
    return {
        "mean": mean(values, default=0.0),
        "min": rate(min(values)) if values else 0.0,
        "max": rate(max(values)) if values else 0.0,
        "per_sample": [rate(value) for value in values],
    }


def compute_variance_band(
    judgments: list[dict[str, Any]],
    sample_of_judgment: list[int],
    sample_indices: list[int],
    questions_per_sample: int,
) -> dict[str, Any]:
    """Summarise per-sample metric spread for a multi-sample run (C3-04).

    ``judgments`` is the flat list of every per-(question, sample) judgment and
    ``sample_of_judgment`` carries each judgment's sample index in the same
    order. Each scorecard metric is reduced to a mean plus a min-max band across
    the per-sample group_metrics(). Single-sample runs do not call this -- the
    band would be degenerate and every artifact must read exactly as today.
    """
    per_sample: dict[int, list[dict[str, Any]]] = {index: [] for index in sample_indices}
    for judgment, sample in zip(judgments, sample_of_judgment):
        per_sample[sample].append(judgment)
    sample_metrics = [group_metrics(per_sample[index]) for index in sample_indices]
    passed_per_sample = [
        sum(1 for judgment in per_sample[index] if judgment["passed"])
        for index in sample_indices
    ]
    return {
        "samples": len(sample_indices),
        "questions_per_sample": questions_per_sample,
        "metrics": {
            metric: metric_band([metrics[metric] for metrics in sample_metrics])
            for metric in VARIANCE_BAND_METRICS
        },
        "passed_per_sample": passed_per_sample,
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
    variance_band: dict[str, Any] | None = None,
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

    report: dict[str, Any] = {
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
    # C3-04: the variance band is an additive field, present only for a
    # multi-sample run. A single-sample run leaves it off, so aggregate_report
    # .json is byte-for-byte identical to a pre-C3-04 run and still validates
    # against the unmodified aggregate-report schema. Every existing top-level
    # key and metric is preserved either way.
    if variance_band is not None:
        report["variance_band"] = variance_band
    return report


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


def variance_band_markdown(band: dict[str, Any] | None) -> list[str]:
    """Markdown lines for the C3-04 multi-sample variance band.

    Returns an empty list for a single-sample run, so report.md is byte-for-byte
    identical to a pre-C3-04 run.
    """
    if not band:
        return []
    metrics = band["metrics"]
    rows = [
        [
            metric.replace("_", " ").capitalize(),
            metric_percent(metrics[metric]["mean"]),
            metric_percent(metrics[metric]["min"]),
            metric_percent(metrics[metric]["max"]),
        ]
        for metric in VARIANCE_BAND_METRICS
    ]
    return [
        "## Sample Variance Band",
        "",
        (
            f"Live answer generation was sampled {band['samples']} times per "
            f"question ({band['questions_per_sample']} questions per sample). "
            "The Overall Metrics above are the mean across samples; the band "
            "below is the min-max spread across samples, so a retrieval or "
            "answer gain can be read against the live answer-generation noise "
            "floor."
        ),
        "",
        markdown_table(["Metric", "Mean", "Min", "Max"], rows),
        "",
        "Passing questions per sample: "
        + ", ".join(str(count) for count in band["passed_per_sample"])
        + ".",
        "",
    ]


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
        *variance_band_markdown(report.get("variance_band")),
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


def run_retrieval_recall(
    manifest: dict[str, Any],
    policy: dict[str, Any],
    questions_by_id: dict[str, dict[str, Any]],
    answers_path: Path,
    destination: Path,
) -> Path | None:
    """Post-judge diagnostic: compare selected context to judge-only fields.

    This runs only after judging is complete. It reads the answer runner's
    retrieval audit sidecar, reconstructs each question's selected context, and
    reports how many judge-only ``required_tokens`` and ``source_refs`` are
    present in that context. It is diagnostic output only and never feeds answer
    generation, so judge-only fields are permitted here.
    """
    audit_path = answers_path.parent / "retrieval_audit.jsonl"
    if not audit_path.exists():
        print(
            f"WARNING: --retrieval-recall: no retrieval audit sidecar at "
            f"{repo_rel(audit_path)}; skipping diagnostic",
            file=sys.stderr,
        )
        return None

    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import answer_runner
    except ImportError as exc:
        print(
            f"WARNING: --retrieval-recall: cannot import answer_runner ({exc}); "
            "skipping diagnostic",
            file=sys.stderr,
        )
        return None

    audit_by_id: dict[str, dict[str, Any]] = {}
    for line in audit_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped:
            record = json.loads(stripped)
            audit_by_id[record["question_id"]] = record
    if not audit_by_id:
        print("WARNING: --retrieval-recall: retrieval audit sidecar is empty; skipping", file=sys.stderr)
        return None

    selected_chunks = [
        chunk for record in audit_by_id.values() for chunk in record.get("selected_chunks", [])
    ]
    context_mode = "lexical" if any(c.get("score") is not None for c in selected_chunks) else "full"
    int_budgets = [record.get("budget") for record in audit_by_id.values() if isinstance(record.get("budget"), int)]
    budget = max(int_budgets) if int_budgets else 0
    chunk_chars = 8_000  # answer_runner.py --chunk-chars default

    try:
        context_root = answer_runner.validate_runner_policy(manifest, policy)
        attachment_glob = manifest["answer_generation"]["attachment_glob"]
        documents = answer_runner.load_attachment_documents(attachment_glob, context_root)
        context_chunks = answer_runner.collect_markdown_chunks(documents, chunk_chars)
    except answer_runner.RunnerError as exc:
        print(
            f"WARNING: --retrieval-recall: cannot rebuild context ({exc}); skipping diagnostic",
            file=sys.stderr,
        )
        return None

    # Manifest-aware routing inputs (cycle-1 jobs 08-09): parse the in-package
    # source/shard manifests exactly as answer_runner.main() does, so the
    # reconstructed context matches a routed run's recorded audit instead of the
    # pre-routing lexical context. Each parser returns an empty mapping when its
    # manifest is absent; build_context() then degrades to plain pre-routing
    # lexical ranking -- the same un-routed reconstruction produced before this
    # fix -- so the diagnostic stays resilient rather than crashing.
    manifest_rows = answer_runner.parse_source_manifest()
    shard_map = answer_runner.parse_shard_manifest()
    if not manifest_rows or not shard_map:
        missing = []
        if not manifest_rows:
            missing.append(repo_rel(answer_runner.REPO_ROOT / answer_runner.SOURCE_MANIFEST_REL))
        if not shard_map:
            missing.append(repo_rel(answer_runner.REPO_ROOT / answer_runner.SHARD_MANIFEST_REL))
        print(
            "WARNING: --retrieval-recall: source/shard manifest(s) absent or empty "
            f"({', '.join(missing)}); reconstructing pre-routing lexical context -- "
            "faithful_reconstruction will be approximate for manifest-routed runs",
            file=sys.stderr,
        )

    per_question: list[dict[str, Any]] = []
    faithful_count = 0
    token_total = token_present = 0
    ref_total = ref_present = 0
    for question_id in sorted(audit_by_id):
        question = questions_by_id.get(question_id)
        if question is None:
            continue
        recorded_audit = audit_by_id[question_id]
        try:
            projection = answer_runner.project_question(question, manifest, policy)
            bundle, rebuilt_audit = answer_runner.build_context(
                documents,
                context_chunks,
                projection,
                context_mode,
                recorded_audit.get("budget") if isinstance(recorded_audit.get("budget"), int) else budget,
                attachment_glob,
                context_root,
                manifest_rows,
                shard_map,
            )
        except answer_runner.RunnerError as exc:
            per_question.append({"question_id": question_id, "error": str(exc)})
            continue

        context_text = bundle.text
        faithful = rebuilt_audit["selected_chunks"] == recorded_audit.get("selected_chunks")
        if faithful:
            faithful_count += 1

        required_tokens = [str(token) for token in question.get("required_tokens", [])]
        missing_tokens = [token for token in required_tokens if not literal_token_present(context_text, token)]
        present_tokens = len(required_tokens) - len(missing_tokens)

        source_refs = [ref for ref in question.get("source_refs", []) if isinstance(ref, dict)]
        missing_refs: list[str] = []
        present_refs = 0
        for ref in source_refs:
            source_path = str(ref.get("source_path", "")).strip()
            candidates = [source_path] if source_path else []
            if source_path:
                candidates.append(source_path.replace("&", "&amp;").replace("'", "&#x27;"))
            if any(candidate and candidate in context_text for candidate in candidates):
                present_refs += 1
            else:
                missing_refs.append(str(ref.get("id") or source_path or "<source_ref>"))

        token_total += len(required_tokens)
        token_present += present_tokens
        ref_total += len(source_refs)
        ref_present += present_refs
        per_question.append(
            {
                "question_id": question_id,
                "faithful_reconstruction": faithful,
                "required_tokens_total": len(required_tokens),
                "required_tokens_present": present_tokens,
                "required_tokens_missing": missing_tokens,
                "source_refs_total": len(source_refs),
                "source_refs_present": present_refs,
                "source_refs_missing": missing_refs,
            }
        )

    evaluated = [item for item in per_question if "error" not in item]
    report = {
        "diagnostic": "retrieval_recall",
        "generated_at": utc_now(),
        "audit_path": repo_rel(audit_path),
        "context_mode": context_mode,
        "context_budget": budget,
        "chunk_chars": chunk_chars,
        "questions_evaluated": len(evaluated),
        "faithful_reconstructions": faithful_count,
        "required_token_recall": {
            "total": token_total,
            "present": token_present,
            "recall": rate(token_present / token_total) if token_total else 1.0,
        },
        "source_ref_recall": {
            "total": ref_total,
            "present": ref_present,
            "recall": rate(ref_present / ref_total) if ref_total else 1.0,
        },
        "per_question": per_question,
    }
    recall_path = destination / "retrieval_recall.json"
    write_json(recall_path, report)
    print(
        "OK: retrieval-recall diagnostic - "
        f"required-token recall {metric_percent(report['required_token_recall']['recall'])}, "
        f"source-ref recall {metric_percent(report['source_ref_recall']['recall'])}; "
        f"report={repo_rel(recall_path)}"
    )
    if faithful_count != len(evaluated):
        print(
            f"WARNING: --retrieval-recall: {len(evaluated) - faithful_count} question(s) did not "
            "reconstruct identically (chunk_chars may differ from the original run); "
            "recall numbers are approximate for those questions",
            file=sys.stderr,
        )
    return recall_path


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
    retrieval_recall: bool = False,
    llm_fact_judge: LLMFactJudge | None = None,
) -> JudgeRunResult:
    manifest = load_json(manifest_path)
    manifest["_path"] = repo_rel(manifest_path)
    policy = load_json(policy_path)
    if judge_mode != "rule":
        raise JudgeError("Only judge mode 'rule' is implemented for offline J012 tooling")

    selected_questions = filter_questions(load_questions(manifest), question_ids, limit)
    questions_by_id = {record["id"]: record for record in selected_questions}
    answer_records = load_answer_records(answers_path)
    # C3-04: a multi-sample run carries N records per question, each tagged with
    # a 0-based sample_index; a legacy single-sample file carries none, so every
    # record is sample 0. `sample_of_record` is index-aligned with both
    # `answer_records` and the `judgments` built from them below.
    sample_of_record = [answer_sample_index(record) for record in answer_records]
    sample_indices = sorted(set(sample_of_record))
    answer_validator = load_schema_validator("answer_record.schema.json") if validate_output else None
    if answer_validator:
        answer_errors: list[str] = []
        for record in answer_records:
            # sample_index is C3-04 bookkeeping, not part of the answer-record
            # schema; validate the canonical record without it.
            instance = {
                key: value for key, value in record.items() if key != "sample_index"
            }
            answer_errors.extend(
                validate_instance(instance, answer_validator, f"answer {record['question_id']}")
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
    # Every sample must answer every selected question, so the per-sample
    # metrics in the variance band are computed over the same question set.
    for sample in sample_indices:
        sample_ids = {
            record["question_id"]
            for record, record_sample in zip(answer_records, sample_of_record)
            if record_sample == sample
        }
        sample_missing = sorted(set(questions_by_id) - sample_ids)
        if sample_missing:
            raise JudgeError(
                f"Answer sample {sample} is missing selected question id(s): "
                + ", ".join(sample_missing[:20])
            )

    run_ids = {str(record.get("run_id", "")) for record in answer_records if record.get("run_id")}
    run_id = sorted(run_ids)[0] if len(run_ids) == 1 else f"mixed_{digest_text(repo_rel(answers_path))[-12:]}"
    destination = output_dir or default_output_dir(manifest, run_id)
    if not destination.is_absolute():
        destination = (REPO_ROOT / destination).resolve()
    destination.mkdir(parents=True, exist_ok=True)

    thresholds = policy["readiness_thresholds"]
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
                thresholds=thresholds,
                llm_fact_judge=llm_fact_judge,
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
    # The variance band is emitted only for a multi-sample run; a single-sample
    # run passes None and aggregate_report.json reads exactly as before C3-04.
    variance_band = (
        compute_variance_band(
            judgments, sample_of_record, sample_indices, len(selected_questions)
        )
        if len(sample_indices) > 1
        else None
    )
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
        variance_band=variance_band,
    )
    if aggregate_validator:
        # variance_band is the C3-04 additive field; validate the canonical
        # report without it against the unmodified aggregate-report schema.
        aggregate_instance = {
            key: value for key, value in aggregate.items() if key != "variance_band"
        }
        aggregate_errors = validate_instance(
            aggregate_instance, aggregate_validator, "aggregate report"
        )
        if aggregate_errors:
            raise JudgeError("Aggregate report schema validation failed: " + "; ".join(aggregate_errors[:10]))
    write_json(aggregate_path, aggregate)
    write_markdown_report(aggregate, markdown_path)

    if retrieval_recall:
        run_retrieval_recall(
            manifest=manifest,
            policy=policy,
            questions_by_id=questions_by_id,
            answers_path=answers_path,
            destination=destination,
        )

    return JudgeRunResult(
        judgments_path=judgments_path,
        aggregate_report_path=aggregate_path,
        markdown_report_path=markdown_path,
        judgment_count=len(judgments),
        readiness_decision=aggregate["readiness_decision"],
    )


# T6 regression fixtures: the verbatim OPS-111 and TOOL-038 answers from run
# altibase_source_preserving_20260520_090243
# (reports/full_benchmark/runs/.../answers/answers.jsonl). Both were FALSE
# POSITIVES of the prohibited-claim judge -- OPS-111 explicitly says the
# tablespace is *not* a system one, and TOOL-038 runs DIFF before FILESYNC (the
# safe order), the opposite of the flagged claim.
OPS_111_REGRESSION_ANSWER = 'Before generating `DROP TABLESPACE` for Altibase 8.1, include these caveats:\n\n- `DROP TABLESPACE` is destructive. Confirm the exact `{Tablespace Name}` and that it is not a system tablespace being deleted by a general user.\n- The executor must be `SYS` or have the `DROP TABLESPACE` privilege.\n- If the tablespace contains objects, `INCLUDING CONTENTS` is required; otherwise `DROP TABLESPACE` fails.\n- `INCLUDING CONTENTS` deletes the objects in the tablespace, but does not remove disk data files or memory checkpoint image files from the file system.\n- `INCLUDING CONTENTS AND DATAFILES` physically deletes all data files for a disk tablespace, and all checkpoint image files for a memory tablespace.\n- `CASCADE CONSTRAINTS` removes referential constraints in other tablespaces that reference objects in the dropped tablespace.\n- If the tablespace was discarded with `ALTER TABLESPACE ... DISCARD`, its objects are inaccessible and the only later action allowed on that tablespace is `DROP`; `DISCARD` should be used only with caution, typically after media recovery is impossible.\n\nDo not generate the final SQL until the operator confirms whether to include `INCLUDING CONTENTS`, `AND DATAFILES`, and `CASCADE CONSTRAINTS`.'
TOOL_038_REGRESSION_ANSWER = '**Runbook**\n\nThe included context only provides two exact CLI commands, so do not invent additional CLI syntax for Build, Reconcile, Data Validation, or FILESYNC.\n\n1. In the Migration Center installation directory, prepare `register.xml` with:\n   - unique project name\n   - source database connection information\n   - destination database connection information\n\n2. Register the project and database connections:\n\n```sh\n./migcenter.sh register register.xml\n```\n\n3. After registration, check the generated project folder. Migration Center automatically creates `options.xml` in that project folder.\n\n4. Edit `options.xml` as needed:\n   - set normal migration options\n   - for full validation, set `Data Sampling` to `No`\n   - set Data Validation `Operation` to `DIFF` for comparison\n\n5. Complete Build and Reconcile before running. The provided context recommends doing Build and Reconcile in GUI mode, especially for mapping datatype, tablespace, partition, `SELECT`, and DDL handling.\n\n6. Run the migration from Linux CLI:\n\n```sh\n./migcenter.sh run [project_path]\n```\n\n`[project_path]` must be an absolute path.\n\n7. Run Data Validation with `Operation` = `DIFF`. The context says validation checks migrated tables with primary keys and may write CSV diff output.\n\n8. If differences are found, change Data Validation `Operation` to `FILESYNC`.\n\n9. Because changing Migration Options requires restarting from Reconcile, rerun Reconcile. For FILESYNC, use `Table Mode` and select the tables to synchronize.\n\n10. Run Data Validation again with `Operation` = `FILESYNC`, then check the Data Validation report to confirm the differences were resolved.\n\nThe missing item in the benchmark context is the exact CLI command syntax for Data Validation and FILESYNC. The safest next check is to provide the Migration Center version and the `migcenter.sh` CLI help output for validation/FILESYNC commands before writing an executable CLI-only script.'


# T6 negation-phrased regression (job-10 gate, 2026-05-20). A prohibited claim
# of the form "may do X without Y" is positive in polarity; the "without" must
# not disable the protective-negation guard. The safe answers are protective
# preflight runbooks -- they discuss exactly the prohibited topic in order to
# forbid it, so they carry near-total vocabulary overlap with the claim, but
# they explicitly negate the prohibited behavior and must read as NOT present.
# The unsafe answer performs the prohibited behavior with no protective
# negation and must still be detected.
WITHOUT_CLAIM_BACKUP = (
    "The answer may provide RESETLOGS, restore, or recovery commands without "
    "confirming backup state and archive-log state."
)
WITHOUT_CLAIM_BACKUP_SAFE_ANSWER = (
    "Backup and recovery preflight runbook. Do not provide RESETLOGS, restore, "
    "or recovery commands until the preflight is complete. First confirm the "
    "backup state and the archive-log state. This answer must never provide a "
    "recovery command without confirming backup state and archive-log state."
)
WITHOUT_CLAIM_BACKUP_UNSAFE_ANSWER = (
    "This answer may provide RESETLOGS, restore, and recovery commands "
    "directly. Just run the recovery commands to bring the database back. "
    "Confirming backup state and archive-log state is optional, so provide the "
    "commands and execute them immediately."
)
WITHOUT_CLAIM_PROPERTY = (
    "The answer may change a system property without version, patch, current "
    "value, and rollback plan."
)
WITHOUT_CLAIM_PROPERTY_SAFE_ANSWER = (
    "This answer must never change a system property without first capturing "
    "the version, patch level, current value, and a rollback plan. The answer "
    "may not proceed until every item is collected."
)

# T6 intrinsically-negative regression (job-10 gate, 2026-05-20). The verbatim
# ERR-101 answer from run job10_err101: it correctly explains that a negative
# SQLCODE *can* be searched with altierr (absolute value -> hex -> lookup), the
# OPPOSITE of the intrinsically-negative prohibited claim. Bag-of-words overlap
# is 1.00 because every term but "can"/"cannot" is shared, so polarity must be
# compared -- the answer does not negate near the claim terms and must read as
# NOT present. The unsafe answer echoes the negative claim and must still be
# detected.
NEGATIVE_CLAIM_ERR101 = "A negative SQLCODE cannot be searched with altierr."
NEGATIVE_CLAIM_ERR101_SAFE_ANSWER = 'Use `altierr` as the first lookup step, but normalize the input carefully.\n\n1. If the user gives an Altibase error code such as `ERR-11075`, run/use:\n\n```sh\naltierr 0x11075\n```\n\nExample context output:\n\n```text\n0x11075 ( 69749) smERR_ABORT_smcExceedLockTimeWait The transaction has exceeded the lock timeout specified by the user.\n```\n\n2. If the user gives a negative `SQLCODE`, treat values other than `0`, `1`, `100`, `-1`, and `-2` as an actual error code. Use the absolute numeric code, convert it to hexadecimal, then query `altierr`. For example, `SQLCODE=-69749` corresponds to `69749`, which is `0x11075`, so use:\n\n```sh\naltierr 0x11075\n```\n\n3. If the user gives an ODBC/SQLCLI diagnostic, first collect the diagnostic fields using `SQLError(env,dbc,stmt,state,err,msg,msgMax,msgLength)` or `SQLGetDiagRec`/`SQLGetDiagField`. Use the `err`/native error number, convert it to hexadecimal if needed, and query `altierr`.\n\n4. If the user only has an error-message keyword, ask for the exact full error line or diagnostic fields: `ERR-xxxxx`, `SQLCODE`, `SQLSTATE`, ODBC `err`, and `msg`. The safest next check is to search the installed error text with `altierr` only after obtaining a real code; keyword-only matching can be ambiguous.'
NEGATIVE_CLAIM_ERR101_UNSAFE_ANSWER = (
    "A negative SQLCODE cannot be searched with altierr. altierr never "
    "resolves a negative SQLCODE, so no altierr lookup is possible for it."
)


# C2-01 prohibited-claim false-positive regression fixtures. The verbatim
# answers for PROP-140, PROP-142, SQL-137, TOOL-003, TOOL-019, and TOOL-033 are
# from the cycle-1 job-11 run altibase_source_preserving_20260520_195639_job11
# (reports/full_benchmark/runs/.../answers/answers.jsonl). The cycle-1 full run
# flagged all six as prohibited claims; section 5.2 of
# reports/full_rerun_analysis_20260520.md confirms every one is a FALSE
# POSITIVE -- each answer asserts the correct or opposite statement. They cover
# four distinct failure modes: claim-condition polarity (PROP-142, SQL-137),
# Markdown-emphasised negation (TOOL-019), a `cannot`-phrased claim the answer
# affirms (TOOL-003), a reversed-direction relation (TOOL-033), and an
# incidental numeric token (PROP-140). All six must read as NOT present.
PROP_140_C2_CLAIM = "SSL_PORT_NO defaults to 20300."
PROP_142_C2_CLAIM = "If no ACCESS_LIST rule matches, Altibase denies access by default."
SQL_137_C2_CLAIM = "NVL2 returns expr3 when expr1 is not NULL."
TOOL_003_C2_CLAIM = "Anonymous blocks cannot use OUTPUT bind variables in iSQL."
TOOL_019_C2_CLAIM = "SQLFreeLob2 commits the JSON LOB update."
TOOL_033_C2_CLAIM = (
    "ALTIBASE_UT_FILE_PERMISSION overrides AEXPORT_FILE_PERMISSION when both are set."
)
PROP_140_C2_ANSWER = 'In Altibase 7.3, `SSL_PORT_NO` is the server property for the ordinary SSL/TLS database listener. Its default is `20443`, range is `[1024, 65535]`, and it specifies the listening port number for SSL connections. The SSL/TLS guide shows it starting beside the normal TCP listener, for example:\n\n```text\n[CM] Listener started : TCP on port 20300 [IPV4]\n[CM] Listener started : SSL on port 20443 [IPV4]\n```\n\nIt must not be treated as the replication SSL port because the 7.3 replication context identifies the replication endpoint port as `REPLICATION_PORT_NO`: `remote_host_port_no` is the port where the remote server Receiver thread listens, specifically the port specified in `REPLICATION_PORT_NO`.\n\nSo for 7.3, keep the roles separate:\n\n- `SSL_PORT_NO`: ordinary client/server SSL/TLS listener, used by SSL clients such as JDBC/ODBC/ADO.NET/iSQL.\n- `REPLICATION_PORT_NO`: replication Receiver listener port in the 7.3 replication manual.\n\nThe provided 7.3 context does not provide a source-backed `REPLICATION_SSL_PORT_NO` property for 7.3. If you need to validate replication-over-SSL specifically, the safe next check is the exact Altibase 7.3 patch level and the actual replication DDL/properties/log excerpt showing whether a supported `USING SSL` or replication SSL port mechanism exists in that build.'
PROP_142_C2_ANSWER = '**ACCESS_LIST Runbook For Altibase 7.3**\n\n`ACCESS_LIST` rules are evaluated in the order they are written. For each incoming IP packet, Altibase checks the rule’s `address` and `mask`; if it matches, the rule’s `operation` is applied: `PERMIT` allows access, `DENY` blocks access. If it does not match, Altibase skips that entry and checks the next `ACCESS_LIST` entry.\n\nIf no `ACCESS_LIST` entry matches, access is allowed. Therefore, for a default-deny policy, add an explicit final catch-all `DENY` rule after the intended `PERMIT` rules, for example:\n\n```bash\nACCESS_LIST = permit, 192.168.3.0, 255.255.255.0\nACCESS_LIST = permit, 219.211.253.0, 255.255.255.0\nACCESS_LIST = deny ,0.0.0.0, 0.0.0.0\n```\n\n`limit` is optional:\n\n```bash\nACCESS_LIST = operation, address, mask, [limit]\n```\n\nWhen `limit` is specified, Altibase checks the maximum number of sessions allowed from the accessible IP address range in that `ACCESS_LIST` entry. If an allowed IP exceeds `limit`, the new connection is rejected. If `limit` is omitted, the limit condition is not checked. A limit rejection can appear as `0x410FD` / `mmERR_ABORT_IP_ACL_CONNECT_OVER`.\n\n`RELOAD ACCESS LIST` scope is only new connections. When `ACCESS_LIST` is updated with `ALTER SYSTEM RELOAD ACCESS LIST` while the server is running, existing connected sessions are not affected. The changed `ACCESS_LIST` applies only to new connection requests after the reload. Because of that, `V$ACCESS_LIST.CONNECTED` can be greater than `V$ACCESS_LIST.LIMIT`.\n\nOperational checks:\n\n```sql\nSELECT ID, ADDRESS, OPERATION, MASK, LIMIT, CONNECTED\nFROM V$ACCESS_LIST;\n```\n\n`RELOAD ACCESS LIST` rebuilds the list from the file configured by `ACCESS_LIST_FILE`; if `ACCESS_LIST_FILE` is omitted or disabled, `0x410F0` / `mmERR_ABORT_RELOAD_ACL_NOT_PERMITTED` applies.'
SQL_137_C2_ANSWER = 'An Altibase answer should say:\n\n- `DECODE` is similar to `CASE WHEN` when `CASE WHEN` uses `simple_case_expr`. `expr` is compared sequentially with each `comparison_expr` using `=`, and the matching `ret_expr` is returned. If nothing matches, `default` is returned; if `default` is omitted, `NULL` is returned.\n- `CASE WHEN` has two forms:\n  - With `simple_case_expr`, `expr` is compared with each `comparison_expr` using `=`.\n  - With `searched_case_expr`, it behaves like `CASE2`: it returns `return_expr` for the first condition that evaluates to `TRUE`; if no condition is `TRUE`, it returns `else_expr` if specified, otherwise `NULL`.\n- `NVL2 (expr1, expr2, expr3)` returns `expr2` when `expr1` is not `NULL`; it returns `expr3` when `expr1` is `NULL`.\n\nFor cross-version scope, the included `7.1`, `7.3`, and `8.1_verified` references show the same descriptions for these behaviors. Sources: `SRC-000040`, `SRC-000103`, `SRC-000163`, and `AID-SRC-000328`.'
TOOL_003_C2_ANSWER = 'In Altibase 7.3, an anonymous block is a stored procedure block used independently without a header.\n\nMain differences from a stored procedure:\n\n- It does not create or store a PSM object in the database.\n- It does not return the value of a RETURN clause.\n- Unlike stored procedures, it can use BIND variables for INPUT, OUTPUT, and INOUTPUT.\n\nStored procedures are created as database objects with `CREATE [OR REPLACE] PROCEDURE`, have a header and body, and are managed with statements such as `ALTER PROCEDURE`, `DROP PROCEDURE`, and `EXECUTE`.\n\nExample of BIND variables in an anonymous block:\n\n```sql\niSQL> VAR OUT1 OUTPUT INTEGER;\niSQL> VAR INOUT1 INOUTPUT INTEGER;\niSQL> EXEC :INOUT1 := 1;\n\niSQL> DECLARE\n    VAR1 INTEGER;\nBEGIN\n    VAR1 := :INOUT1;\n    :OUT1 := VAR1;\n    :INOUT1 := VAR1 + 1;\nEND;\n/\nExecute success.\n\niSQL> PRINT VAR;\n[ HOST VARIABLE ]\n-------------------------------------------------------\nNAME                 TYPE                 VALUE\n-------------------------------------------------------\nOUT1                 INTEGER              1\nINOUT1               INTEGER              2\n```\n\nHere, `:INOUT1` is read and then updated, and `:OUT1` receives the output value.'
TOOL_019_C2_ANSWER = 'In 8.1, after using `SQLPutLob` to update `JSON` data through an Altibase CLI LOB locator, you must call `SQLFreeLob2`.\n\n`SQLFreeLob2` releases resources related to the `LOB Locator` for the `JSON` data type.\n\nIt does **not** `commit` or `rollback` the changes to the LOB pointed to by the locator. Transaction completion still has to be handled separately with an explicit `commit` or `rollback`.'
TOOL_033_C2_ANSWER = '**Runbook**\n\nFor aexport-generated files, permission is selected in this order:\n\n1. `AEXPORT_FILE_PERMISSION`\n2. `ALTIBASE_UT_FILE_PERMISSION`\n3. Default `666` (`user:rw, group:rw, other: rw`)\n\n`ALTIBASE_UT_FILE_PERMISSION` is the common environment variable for files created by `aexport`, `iLoader`, and `iSQL`.\n\n```bash\nexport ALTIBASE_UT_FILE_PERMISSION=600\n```\n\nWith only this set, files created by `aexport` use `600` (`user:rw, group:--, other:--`).\n\n`AEXPORT_FILE_PERMISSION` is specific to files created by `aexport`. If it is set, it overrides `ALTIBASE_UT_FILE_PERMISSION` for `aexport` output.\n\n```bash\nexport ALTIBASE_UT_FILE_PERMISSION=660\nexport AEXPORT_FILE_PERMISSION=600\n```\n\nIn this case, `aexport`-generated files use `AEXPORT_FILE_PERMISSION=600`, not `ALTIBASE_UT_FILE_PERMISSION=660`.\n\nIf neither variable is set, `aexport`-generated files default to `666` (`user:rw, group:rw, other: rw`).\n\nIf an invalid permission value is used, the documented error is:\n\n```text\n326, HY000, utERR_ABORT_FilePerm_OutOfRange_Error = File permission value is out of range (<0%s>=<1%s>)\n# *Cause: File permission value is out of range.\n# *Action: Use valid file permission value.\n```'


# C3-01 prohibited-claim false-positive regression fixtures.
#
# ERR_101_C3_ANSWER is the verbatim ERR-101 answer from the cycle-2 job-09 run
# altibase_source_preserving_20260521_220915_job09
# (reports/full_benchmark/runs/.../answers/answers.jsonl). It was the single
# surviving prohibited-claim false positive after cycle 2
# (reports/full_rerun_analysis_cycle2_20260520.md section 4): the `cannot`-
# phrased claim "A negative SQLCODE cannot be searched with altierr" mis-fired
# even though the answer states the OPPOSITE -- a negative SQLCODE *can* be
# searched, with worked examples. Its best-covering sentence carries an
# incidental "without" ("search ... with or without the minus sign"), which is
# positive polarity, not an impossibility; and the answer also contains a
# `does not` inside the CLI example `altierr -w "does not"`, a negation that
# belongs to example text, not the answer's prose. Neither is the answer
# asserting the negative claim, so ERR-101 must read as NOT present.
ERR_101_C3_ANSWER = 'Use `altierr` as the first lookup step, matching the evidence the user has.\n\n- If the user has an `ERR-` code, search by hexadecimal or decimal code. Example for `ERR-00015`:\n```sh\naltierr 0x00015\naltierr –w 00015\naltierr 21\n```\n\n- If the user has a negative `SQLCODE` from C/C++ precompiler or an ODBC error code returned by the ODBC function, search either with or without the minus sign, or by the equivalent hex code:\n```sh\naltierr -266286\naltierr 266286\naltierr 0x4102E\n```\n\n- If the user only has an error-message keyword, search message text with `–w`. This can return multiple records, so ask the user to share the exact error code/message if the result is ambiguous:\n```sh\naltierr –w connect\naltierr –w “does not”\n```\n\nIn an Altibase answer, explain that `altierr` returns the error code number, error code string, description, cause, and action. For ODBC cases, also ask the user to collect the diagnostic error number/message from `SQLError` or supported diagnostic APIs such as `SQLGetDiagRec` if they only provided a generic failure.'

# C3-01 quoted-span isolation case. This synthetic answer affirms the opposite
# of a `cannot`-phrased claim in plain prose ("can use OUTPUT bind variables")
# and carries NO prose negation; its only negation token is the `does not`
# inside the backtick example span `flag does not apply`. It must read as NOT
# present, and -- unlike ERR-101, which is also cleared by the "without"
# refinement -- it isolates the quoted-span masking: without
# mask_quoted_span_negations() the span's `not` would flip the verdict.
QUOTED_SPAN_SAFE_CLAIM = "Anonymous blocks cannot use OUTPUT bind variables."
QUOTED_SPAN_SAFE_ANSWER = (
    "Anonymous blocks can use OUTPUT bind variables, even in an example like "
    "`flag does not apply`."
)


def prohibited_claim_regression_failures() -> list[str]:
    """Check prohibited-claim regression cases.

    The two real run answers (OPS-111, TOOL-038) are false positives and must
    read as "not present". The negation-phrased "may do X without Y" cases
    (job-10 gate) cover the protective preflight/checklist answers that the
    "without"-disables-the-guard bug wrongly flagged. The six C2-01 fixtures are
    the cycle-1 job-11 prohibited-claim false positives -- polarity-, emphasis-,
    `cannot`-, and direction-blind misfires -- and must all read as "not
    present". Four clearly prohibited answers -- one plain, one order-sensitive,
    one direction-sensitive, one negation-phrased -- must still be detected, so
    the false-positive fixes do not silently disable prohibited-claim detection.
    """
    failures: list[str] = []

    ops111_present, ops111_notes = prohibited_claim_present(
        "System tablespaces can be dropped with CASCADE CONSTRAINTS.",
        OPS_111_REGRESSION_ANSWER,
    )
    if ops111_present:
        failures.append(
            f"OPS-111 answer wrongly flagged as a prohibited claim ({ops111_notes})"
        )

    tool038_present, tool038_notes = prohibited_claim_present(
        "FILESYNC should be run before diff.",
        TOOL_038_REGRESSION_ANSWER,
    )
    if tool038_present:
        failures.append(
            f"TOOL-038 answer wrongly flagged as a prohibited claim ({tool038_notes})"
        )

    genuine_plain_present, _ = prohibited_claim_present(
        "System tablespaces can be dropped with CASCADE CONSTRAINTS.",
        "With CASCADE CONSTRAINTS, system tablespaces can simply be dropped. "
        "Dropping such system tablespaces is fully allowed with CASCADE CONSTRAINTS.",
    )
    if not genuine_plain_present:
        failures.append("a clearly prohibited (non-ordered) claim was not detected")

    genuine_order_present, _ = prohibited_claim_present(
        "FILESYNC should be run before diff.",
        "For Altibase Migration Center you should always run FILESYNC before the diff.",
    )
    if not genuine_order_present:
        failures.append("a clearly prohibited ordered claim was not detected")

    # Negation-phrased "may do X without Y" claims: protective preflight answers
    # must not be flagged, reckless answers must still be detected.
    backup_safe_present, backup_safe_notes = prohibited_claim_present(
        WITHOUT_CLAIM_BACKUP, WITHOUT_CLAIM_BACKUP_SAFE_ANSWER
    )
    if backup_safe_present:
        failures.append(
            "a protective backup/recovery preflight answer was wrongly flagged "
            f"against a negation-phrased claim ({backup_safe_notes})"
        )

    property_safe_present, property_safe_notes = prohibited_claim_present(
        WITHOUT_CLAIM_PROPERTY, WITHOUT_CLAIM_PROPERTY_SAFE_ANSWER
    )
    if property_safe_present:
        failures.append(
            "a protective property-change preflight answer was wrongly flagged "
            f"against a negation-phrased claim ({property_safe_notes})"
        )

    backup_unsafe_present, _ = prohibited_claim_present(
        WITHOUT_CLAIM_BACKUP, WITHOUT_CLAIM_BACKUP_UNSAFE_ANSWER
    )
    if not backup_unsafe_present:
        failures.append(
            "a reckless negation-phrased prohibited claim was not detected"
        )

    # Intrinsically-negative claims: an answer that affirms the OPPOSITE of
    # "X cannot be done" must not be flagged on bag-of-words overlap alone; an
    # answer that echoes the negative claim must still be detected.
    err101_safe_present, err101_safe_notes = prohibited_claim_present(
        NEGATIVE_CLAIM_ERR101, NEGATIVE_CLAIM_ERR101_SAFE_ANSWER
    )
    if err101_safe_present:
        failures.append(
            "an answer affirming the opposite of an intrinsically-negative "
            f"claim was wrongly flagged ({err101_safe_notes})"
        )

    err101_unsafe_present, _ = prohibited_claim_present(
        NEGATIVE_CLAIM_ERR101, NEGATIVE_CLAIM_ERR101_UNSAFE_ANSWER
    )
    if not err101_unsafe_present:
        failures.append(
            "an answer asserting an intrinsically-negative prohibited claim "
            "was not detected"
        )

    # C2-01: the six cycle-1 job-11 prohibited-claim false positives. Each
    # answer asserts the correct or opposite statement and must read as NOT
    # present (see reports/full_rerun_analysis_20260520.md section 5.2).
    c2_cases = [
        ("PROP-140", PROP_140_C2_CLAIM, PROP_140_C2_ANSWER, "incidental numeric token"),
        ("PROP-142", PROP_142_C2_CLAIM, PROP_142_C2_ANSWER, "claim-condition polarity"),
        ("SQL-137", SQL_137_C2_CLAIM, SQL_137_C2_ANSWER, "claim-condition polarity"),
        ("TOOL-003", TOOL_003_C2_CLAIM, TOOL_003_C2_ANSWER, "affirmed cannot-phrased claim"),
        ("TOOL-019", TOOL_019_C2_CLAIM, TOOL_019_C2_ANSWER, "markdown-emphasised negation"),
        ("TOOL-033", TOOL_033_C2_CLAIM, TOOL_033_C2_ANSWER, "reversed-direction relation"),
    ]
    for question_id, claim, answer, mode in c2_cases:
        present, notes = prohibited_claim_present(claim, answer)
        if present:
            failures.append(
                f"{question_id} answer wrongly flagged as a prohibited claim "
                f"[{mode}] ({notes})"
            )

    # A genuine reversed-direction ("A overrides B") claim that the answer
    # asserts in the same direction must still be detected, so the
    # direction-sensitivity fix does not disable prohibited-claim detection.
    genuine_direction_present, _ = prohibited_claim_present(
        "ALTIBASE_UT_FILE_PERMISSION overrides AEXPORT_FILE_PERMISSION.",
        "In Altibase, ALTIBASE_UT_FILE_PERMISSION overrides AEXPORT_FILE_PERMISSION "
        "for every utility.",
    )
    if not genuine_direction_present:
        failures.append("a clearly prohibited direction-sensitive claim was not detected")

    # C3-01: the verbatim cycle-2 job-09 ERR-101 answer -- the single
    # prohibited-claim false positive that survived cycle 2. The answer states
    # the OPPOSITE of the `cannot`-phrased claim (a negative SQLCODE *can* be
    # searched), so it must read as NOT present.
    err101_c3_present, err101_c3_notes = prohibited_claim_present(
        NEGATIVE_CLAIM_ERR101, ERR_101_C3_ANSWER
    )
    if err101_c3_present:
        failures.append(
            "the cycle-2 job-09 ERR-101 answer was wrongly flagged as a "
            f"prohibited claim [quoted-span / incidental negation] ({err101_c3_notes})"
        )

    # C3-01: isolate the quoted-span masking. The answer affirms the opposite
    # of a `cannot` claim with no prose negation; its only negation is `does
    # not` inside a backtick example span and must not flip the verdict.
    quoted_span_safe_present, quoted_span_safe_notes = prohibited_claim_present(
        QUOTED_SPAN_SAFE_CLAIM, QUOTED_SPAN_SAFE_ANSWER
    )
    if quoted_span_safe_present:
        failures.append(
            "an answer whose only negation sits inside a quoted example span "
            f"was wrongly flagged as a prohibited claim ({quoted_span_safe_notes})"
        )

    return failures


def variance_band_self_test_failures() -> list[str]:
    """Deterministic self-test for the C3-04 multi-sample variance band.

    Exercises the pure band helpers on synthetic per-sample judgments -- no
    provider, no fixture file -- so the judge self-test stays hermetic. It
    confirms a one-sample band is degenerate (mean == min == max), so the band
    behaves as N=1, and that a three-sample band reports the mean and spread.
    """
    failures: list[str] = []

    def judgment(passed: bool) -> dict[str, Any]:
        score = 1.0 if passed else 0.0
        return {
            "passed": passed,
            "scores": {
                "fact_coverage": score,
                "critical_fact_coverage": score,
                "required_token_preservation": score,
                "version_handling": 1.0,
                "altibase_specific_correctness": score,
                "missing_input_handling": 1.0,
            },
            "prohibited_claim_results": [],
        }

    # One sample -> degenerate band: mean == min == max.
    band1 = compute_variance_band(
        [judgment(True), judgment(False)], [0, 0], [0], 2
    )
    pass1 = band1["metrics"]["pass_rate"]
    if not (pass1["mean"] == pass1["min"] == pass1["max"] == 0.5):
        failures.append(f"single-sample band is not degenerate: {pass1}")
    if band1["passed_per_sample"] != [1]:
        failures.append(f"single-sample passed_per_sample wrong: {band1['passed_per_sample']}")

    # Three samples with pass rates 1.0 / 0.5 / 0.0 -> mean 0.5, band 0.0-1.0.
    judgments = [
        judgment(True), judgment(True),    # sample 0: 2/2 passed
        judgment(True), judgment(False),   # sample 1: 1/2 passed
        judgment(False), judgment(False),  # sample 2: 0/2 passed
    ]
    band3 = compute_variance_band(judgments, [0, 0, 1, 1, 2, 2], [0, 1, 2], 2)
    pass3 = band3["metrics"]["pass_rate"]
    if not (pass3["mean"] == 0.5 and pass3["min"] == 0.0 and pass3["max"] == 1.0):
        failures.append(f"three-sample pass-rate band wrong: {pass3}")
    if pass3["per_sample"] != [1.0, 0.5, 0.0]:
        failures.append(f"three-sample per-sample pass rates wrong: {pass3['per_sample']}")
    if band3["passed_per_sample"] != [2, 1, 0]:
        failures.append(f"three-sample passed_per_sample wrong: {band3['passed_per_sample']}")
    if band3["samples"] != 3 or band3["questions_per_sample"] != 2:
        failures.append(f"three-sample band header wrong: {band3}")

    return failures


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
        aggregate = load_json(result.aggregate_report_path)
    by_id = {record["question_id"]: record for record in judgments}
    if "variance_band" in aggregate:
        print(
            "SELF-TEST FAILED: single-sample run emitted a variance band",
            file=sys.stderr,
        )
        return 1
    if not by_id["PROP-001"]["passed"]:
        print("SELF-TEST FAILED: PROP-001 calibration answer should pass", file=sys.stderr)
        return 1
    if by_id["OPS-001"]["passed"]:
        print("SELF-TEST FAILED: OPS-001 unsafe calibration answer should fail", file=sys.stderr)
        return 1
    if "backup_recovery" not in by_id["OPS-001"].get("protected_topic_blockers", []):
        print("SELF-TEST FAILED: OPS-001 should produce a backup_recovery blocker", file=sys.stderr)
        return 1
    regression_failures = prohibited_claim_regression_failures()
    if regression_failures:
        for message in regression_failures:
            print(f"SELF-TEST FAILED: {message}", file=sys.stderr)
        return 1
    llm_helper_failures = llm_fact_judge_helper_failures()
    if llm_helper_failures:
        for message in llm_helper_failures:
            print(f"SELF-TEST FAILED: {message}", file=sys.stderr)
        return 1
    variance_failures = variance_band_self_test_failures()
    if variance_failures:
        for message in variance_failures:
            print(f"SELF-TEST FAILED: {message}", file=sys.stderr)
        return 1
    print(
        "OK: judge/report self-test passed (incl. OPS-111 / TOOL-038, "
        "C2-01 PROP-140 / PROP-142 / SQL-137 / TOOL-003 / TOOL-019 / TOOL-033, "
        "C3-01 ERR-101 quoted-span regression, LLM-fact-judge verdict/vote "
        "helpers, C3-04 variance band)"
    )
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
    parser.add_argument(
        "--retrieval-recall",
        action="store_true",
        help=(
            "After judging, run a post-judge diagnostic that compares each "
            "question's selected context against judge-only source_refs and "
            "required_tokens. Off by default; diagnostic output only."
        ),
    )
    parser.add_argument(
        "--llm-fact-judge",
        action="store_true",
        help=(
            "Enable the optional LLM-assisted fact-coverage judge for "
            "paraphrase-suspect facts. Also enabled by the JUDGE_LLM_FACT=1 "
            "environment toggle. Off by default; the deterministic rule judge "
            "stays the default and the fallback. Ignored by --self-test."
        ),
    )
    parser.add_argument(
        "--llm-fact-judge-command",
        help=(
            "Provider command for the LLM fact judge (default: the Codex "
            "command provider; env JUDGE_LLM_FACT_COMMAND)."
        ),
    )
    parser.add_argument(
        "--llm-fact-judge-cache",
        type=Path,
        help="Cache file for LLM fact-judge verdicts (env JUDGE_LLM_FACT_CACHE).",
    )
    parser.add_argument(
        "--llm-fact-judge-timeout",
        type=int,
        help=(
            "Per-call timeout in seconds for the LLM fact judge "
            "(env JUDGE_LLM_FACT_TIMEOUT)."
        ),
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
        # Opt-in LLM fact judge. The self-test path returned above, so the
        # self-test (and the run-all.sh preflight) is always hermetic and never
        # builds this, even with JUDGE_LLM_FACT=1 set in the environment.
        llm_fact_judge = make_llm_fact_judge(
            flag=args.llm_fact_judge,
            command=args.llm_fact_judge_command,
            cache_path=args.llm_fact_judge_cache,
            timeout_seconds=args.llm_fact_judge_timeout,
        )
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
            retrieval_recall=args.retrieval_recall,
            llm_fact_judge=llm_fact_judge,
        )
    except JudgeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(
        "OK: wrote "
        f"{result.judgment_count} judgment(s) to {repo_rel(result.judgments_path)}; "
        f"readiness={result.readiness_decision}; report={repo_rel(result.markdown_report_path)}"
    )
    if llm_fact_judge is not None:
        print("OK: " + llm_fact_judge_summary(llm_fact_judge))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
