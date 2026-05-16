#!/usr/bin/env python3
"""Validate Altibase answerability benchmark artifacts.

The full profile enforces production benchmark count gates. The fixture profile
validates schemas and record hygiene without requiring the full 200-question set.
"""

from __future__ import annotations

import argparse
import glob
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

try:
    from jsonschema import Draft202012Validator, FormatChecker
    from jsonschema.exceptions import SchemaError
except ImportError as exc:  # pragma: no cover - exercised only on missing dependency
    print(
        "ERROR: validate_benchmark.py requires the Python package 'jsonschema'.",
        file=sys.stderr,
    )
    raise SystemExit(2) from exc


BENCHMARK_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_DIR = BENCHMARK_ROOT / "schemas"
HANGUL_RE = re.compile(r"[\u1100-\u11ff\u3130-\u318f\uac00-\ud7af]")


@dataclass
class ValidationState:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    schema_count: int = 0
    question_file_count: int = 0
    question_count: int = 0
    domain_counts: Counter[str] = field(default_factory=Counter)

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def repo_rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def json_path(error_path: Any) -> str:
    parts = ["$"]
    for part in error_path:
        if isinstance(part, int):
            parts.append(f"[{part}]")
        else:
            parts.append(f".{part}")
    return "".join(parts)


def load_json(path: Path, state: ValidationState) -> Any | None:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError:
        state.error(f"Missing JSON file: {repo_rel(path)}")
    except json.JSONDecodeError as exc:
        state.error(f"Invalid JSON in {repo_rel(path)}:{exc.lineno}:{exc.colno}: {exc.msg}")
    return None


def schema_validator(schema_path: Path, state: ValidationState) -> Draft202012Validator | None:
    schema = load_json(schema_path, state)
    if schema is None:
        return None
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        state.error(f"Invalid JSON schema {repo_rel(schema_path)}: {exc.message}")
        return None
    state.schema_count += 1
    return Draft202012Validator(schema, format_checker=FormatChecker())


def validate_instance(
    data: Any,
    validator: Draft202012Validator,
    label: str,
    state: ValidationState,
) -> None:
    for error in sorted(validator.iter_errors(data), key=lambda item: list(item.path)):
        state.error(f"{label} {json_path(error.path)}: {error.message}")


def validate_all_schemas(state: ValidationState) -> None:
    for schema_path in sorted(SCHEMA_DIR.glob("*.schema.json")):
        schema_validator(schema_path, state)


def resolve_repo_path(path_text: str, state: ValidationState, label: str) -> Path | None:
    path = Path(path_text)
    if path.is_absolute():
        state.error(f"{label} must be repository-relative, got absolute path: {path_text}")
        return None
    resolved = (REPO_ROOT / path).resolve()
    try:
        resolved.relative_to(REPO_ROOT)
    except ValueError:
        state.error(f"{label} escapes the repository root: {path_text}")
        return None
    return resolved


def validate_policy(policy_path: Path, state: ValidationState) -> dict[str, Any] | None:
    validator = schema_validator(SCHEMA_DIR / "policy.schema.json", state)
    policy = load_json(policy_path, state)
    if validator is None or policy is None:
        return None
    validate_instance(policy, validator, repo_rel(policy_path), state)

    allowlist = set(policy.get("answer_input_allowlist", []))
    judge_only = set(policy.get("judge_only_question_fields", []))
    overlap = sorted(allowlist & judge_only)
    if overlap:
        state.error(f"Policy answer allowlist overlaps judge-only fields: {', '.join(overlap)}")

    required_sum = sum(domain.get("required_minimum", 0) for domain in policy.get("domains", []))
    if required_sum != policy.get("question_total_minimum"):
        state.error(
            "Policy domain required minimums must sum to question_total_minimum "
            f"({required_sum} != {policy.get('question_total_minimum')})"
        )

    source_inventory = policy.get("source_boundary", {}).get("source_inventory")
    if source_inventory:
        source_inventory_path = resolve_repo_path(source_inventory, state, "source_inventory")
        if source_inventory_path and not source_inventory_path.exists():
            state.error(f"Policy source_inventory does not exist: {source_inventory}")

    return policy


def validate_taxonomy(taxonomy_path: Path, state: ValidationState) -> dict[str, Any] | None:
    validator = schema_validator(SCHEMA_DIR / "source_taxonomy.schema.json", state)
    taxonomy = load_json(taxonomy_path, state)
    if validator is None or taxonomy is None:
        return None
    validate_instance(taxonomy, validator, repo_rel(taxonomy_path), state)

    for coverage in taxonomy.get("domain_coverage", []):
        question_file = coverage.get("question_file")
        if question_file and not question_file.startswith("evals/altibase_answerability/questions/"):
            state.error(f"Taxonomy question_file is outside durable questions path: {question_file}")
        for attachment in coverage.get("attachment_files", []):
            attachment_path = resolve_repo_path(attachment, state, "taxonomy attachment_files")
            if attachment_path and not attachment_path.exists():
                state.error(f"Taxonomy attachment file does not exist: {attachment}")

    return taxonomy


def validate_manifest(
    manifest_path: Path,
    policy: dict[str, Any],
    state: ValidationState,
) -> dict[str, Any] | None:
    validator = schema_validator(SCHEMA_DIR / "manifest.schema.json", state)
    manifest = load_json(manifest_path, state)
    if validator is None or manifest is None:
        return None
    validate_instance(manifest, validator, repo_rel(manifest_path), state)

    answer_generation = manifest.get("answer_generation", {})
    manifest_allowlist = set(answer_generation.get("allowlisted_question_fields", []))
    policy_allowlist = set(policy.get("answer_input_allowlist", []))
    if manifest_allowlist != policy_allowlist:
        state.error(
            f"{repo_rel(manifest_path)} answer_generation.allowlisted_question_fields "
            "must match policy answer_input_allowlist"
        )

    judge_only = set(policy.get("judge_only_question_fields", []))
    leakage_keys = sorted(manifest_allowlist & judge_only)
    if leakage_keys:
        state.error(
            f"{repo_rel(manifest_path)} allowlists judge-only keys: {', '.join(leakage_keys)}"
        )

    if answer_generation.get("attachment_glob") not in policy.get("source_boundary", {}).get(
        "answer_generation_sources", []
    ):
        state.error(
            f"{repo_rel(manifest_path)} attachment_glob is outside policy answer-generation sources"
        )

    if answer_generation.get("default_answer_language") != "en":
        state.error(f"{repo_rel(manifest_path)} must default answer generation to English")

    include_draft = answer_generation.get("include_gpt_instruction_draft")
    draft_path = answer_generation.get("gpt_instruction_draft_path")
    if include_draft and not draft_path:
        state.error(f"{repo_rel(manifest_path)} includes GPT instruction draft but has no path")
    if draft_path:
        resolved = resolve_repo_path(draft_path, state, "gpt_instruction_draft_path")
        if resolved and not resolved.exists():
            state.error(f"Manifest GPT instruction draft path does not exist: {draft_path}")

    output_dir = manifest.get("reporting", {}).get("output_dir")
    if output_dir:
        resolved = resolve_repo_path(output_dir, state, "reporting.output_dir")
        if resolved:
            try:
                resolved.relative_to(BENCHMARK_ROOT)
            except ValueError:
                state.error(f"reporting.output_dir must stay under {repo_rel(BENCHMARK_ROOT)}")

    return manifest


def expand_question_files(manifest: dict[str, Any], state: ValidationState) -> list[Path]:
    resolved_files: list[Path] = []
    for pattern in manifest.get("question_files", []):
        if any(char in pattern for char in "*?[]"):
            matches = sorted(Path(match).resolve() for match in glob.glob(str(REPO_ROOT / pattern)))
            if not matches:
                state.error(f"Question file glob matched no files: {pattern}")
                continue
            resolved_files.extend(matches)
        else:
            resolved = resolve_repo_path(pattern, state, "question_files")
            if resolved is not None:
                resolved_files.append(resolved)

    seen: set[Path] = set()
    unique_files: list[Path] = []
    for path in resolved_files:
        if path in seen:
            state.error(f"Duplicate resolved question file: {repo_rel(path)}")
            continue
        seen.add(path)
        unique_files.append(path)

    for path in unique_files:
        try:
            path.relative_to(BENCHMARK_ROOT)
        except ValueError:
            state.error(f"Question file must stay under {repo_rel(BENCHMARK_ROOT)}: {repo_rel(path)}")
        if path.suffix != ".jsonl":
            state.error(f"Question file must be JSONL: {repo_rel(path)}")
        if not path.exists():
            state.error(f"Question file does not exist: {repo_rel(path)}")

    return unique_files


def has_hangul(value: str) -> bool:
    return bool(HANGUL_RE.search(value))


def validate_english_field(value: str, label: str, state: ValidationState) -> None:
    if has_hangul(value):
        state.error(f"{label} contains Korean text; canonical benchmark fields must be English")


def validate_question_custom(
    record: dict[str, Any],
    source_file: Path,
    line_no: int,
    state: ValidationState,
) -> None:
    label = f"{repo_rel(source_file)}:{line_no} {record.get('id', '<missing id>')}"

    source_refs = record.get("source_refs", [])
    source_ref_ids = [ref.get("id") for ref in source_refs if isinstance(ref, dict)]
    duplicate_source_refs = [ref_id for ref_id, count in Counter(source_ref_ids).items() if count > 1]
    if duplicate_source_refs:
        state.error(f"{label} has duplicate source_ref ids: {', '.join(duplicate_source_refs)}")

    source_ref_id_set = set(source_ref_ids)
    for ref in source_refs:
        if not isinstance(ref, dict):
            continue
        source_path = ref.get("source_path")
        if source_path:
            resolved = resolve_repo_path(source_path, state, f"{label} source_path")
            if resolved and not resolved.exists():
                state.error(f"{label} source_path does not exist: {source_path}")

    fact_ids = [fact.get("id") for fact in record.get("expected_facts", []) if isinstance(fact, dict)]
    duplicate_fact_ids = [fact_id for fact_id, count in Counter(fact_ids).items() if count > 1]
    if duplicate_fact_ids:
        state.error(f"{label} has duplicate expected_fact ids: {', '.join(duplicate_fact_ids)}")

    critical_facts = 0
    for fact in record.get("expected_facts", []):
        if not isinstance(fact, dict):
            continue
        if fact.get("importance") == "critical":
            critical_facts += 1
        validate_english_field(fact.get("fact", ""), f"{label} expected_facts.{fact.get('id')}", state)
        for source_ref_id in fact.get("source_ref_ids", []):
            if source_ref_id not in source_ref_id_set:
                state.error(f"{label} expected_fact {fact.get('id')} references unknown {source_ref_id}")
    if record.get("expected_facts") and critical_facts == 0:
        state.error(f"{label} must mark at least one expected_fact as critical")

    if record.get("answer_language") == "en":
        validate_english_field(record.get("question", ""), f"{label} question", state)
    if "canonical_reference_answer" in record:
        validate_english_field(
            record.get("canonical_reference_answer", ""),
            f"{label} canonical_reference_answer",
            state,
        )
    if "scoring_notes" in record:
        validate_english_field(record.get("scoring_notes", ""), f"{label} scoring_notes", state)
    for index, claim in enumerate(record.get("prohibited_claims", []), start=1):
        validate_english_field(claim, f"{label} prohibited_claims[{index}]", state)

    source_languages = {ref.get("language") for ref in source_refs if isinstance(ref, dict)}
    basis = record.get("source_language_basis")
    has_ko = bool(source_languages & {"ko", "ko+en"})
    has_en = bool(source_languages & {"en", "ko+en"})
    if basis == "ko" and not has_ko:
        state.error(f"{label} source_language_basis=ko requires a Korean source_ref")
    elif basis == "ko+en" and not (has_ko and has_en):
        state.error(f"{label} source_language_basis=ko+en requires Korean and English source_refs")
    elif basis == "en" and has_ko:
        state.error(f"{label} uses Korean source_refs but source_language_basis is en")

    if not record.get("required_tokens"):
        state.warn(f"{label} has no required_tokens; add literal technical tokens if possible")
    if not record.get("prohibited_claims"):
        state.warn(f"{label} has no prohibited_claims; add common unsafe assumptions if possible")


def validate_answer_projection(
    record: dict[str, Any],
    manifest: dict[str, Any],
    policy: dict[str, Any],
    source_file: Path,
    line_no: int,
    state: ValidationState,
) -> None:
    answer_generation = manifest.get("answer_generation", {})
    allowlist = set(answer_generation.get("allowlisted_question_fields", []))
    judge_only = set(policy.get("judge_only_question_fields", []))
    projection: dict[str, Any] = {}

    for key in allowlist:
        if key == "requested_language":
            if "requested_language" in answer_generation:
                projection[key] = answer_generation["requested_language"]
        elif key == "answer_language":
            projection[key] = record.get("answer_language") or answer_generation.get(
                "default_answer_language", "en"
            )
        elif key in record:
            projection[key] = record[key]

    leaked_keys = sorted(set(projection) & judge_only)
    if leaked_keys:
        state.error(
            f"{repo_rel(source_file)}:{line_no} projected answering input leaks judge-only keys: "
            f"{', '.join(leaked_keys)}"
        )

    disallowed = sorted(set(projection) - set(policy.get("answer_input_allowlist", [])))
    if disallowed:
        state.error(
            f"{repo_rel(source_file)}:{line_no} projected answering input has non-policy keys: "
            f"{', '.join(disallowed)}"
        )

    required_projection_keys = {"id", "question", "version_scope", "user_level", "answer_type", "answer_language"}
    missing = sorted(required_projection_keys - set(projection))
    if missing:
        state.error(
            f"{repo_rel(source_file)}:{line_no} projected answering input missing keys: "
            f"{', '.join(missing)}"
        )


def validate_question_files(
    question_files: list[Path],
    manifest: dict[str, Any],
    policy: dict[str, Any],
    state: ValidationState,
) -> list[dict[str, Any]]:
    validator = schema_validator(SCHEMA_DIR / "question.schema.json", state)
    if validator is None:
        return []

    records: list[dict[str, Any]] = []
    seen_ids: dict[str, str] = {}

    for question_file in question_files:
        if not question_file.exists():
            continue
        state.question_file_count += 1
        with question_file.open("r", encoding="utf-8") as handle:
            for line_no, line in enumerate(handle, start=1):
                stripped = line.strip()
                if not stripped:
                    state.warn(f"{repo_rel(question_file)}:{line_no} blank JSONL line ignored")
                    continue
                try:
                    record = json.loads(stripped)
                except json.JSONDecodeError as exc:
                    state.error(
                        f"Invalid JSONL in {repo_rel(question_file)}:{line_no}:{exc.colno}: {exc.msg}"
                    )
                    continue

                validate_instance(record, validator, f"{repo_rel(question_file)}:{line_no}", state)
                if isinstance(record, dict):
                    question_id = record.get("id")
                    if question_id in seen_ids:
                        state.error(
                            f"Duplicate question id {question_id}: {seen_ids[question_id]} and "
                            f"{repo_rel(question_file)}:{line_no}"
                        )
                    elif question_id:
                        seen_ids[question_id] = f"{repo_rel(question_file)}:{line_no}"
                    validate_question_custom(record, question_file, line_no, state)
                    validate_answer_projection(record, manifest, policy, question_file, line_no, state)
                    records.append(record)
                    state.question_count += 1
                    if "domain" in record:
                        state.domain_counts[record["domain"]] += 1

    return records


def enforce_count_gates(policy: dict[str, Any], profile: str, state: ValidationState) -> None:
    if profile == "fixture":
        if state.question_count == 0:
            state.error("Fixture validation requires at least one question record")
        return

    total_minimum = policy.get("question_total_minimum", 200)
    if state.question_count < total_minimum:
        state.error(
            f"Full benchmark has {state.question_count} questions; required minimum is {total_minimum}"
        )

    for domain in policy.get("domains", []):
        domain_id = domain["id"]
        required_minimum = domain["required_minimum"]
        target = domain["target"]
        count = state.domain_counts.get(domain_id, 0)
        if count < required_minimum:
            state.error(
                f"Domain {domain_id} has {count} questions; required minimum is {required_minimum}"
            )
        elif count < target:
            state.warn(f"Domain {domain_id} has {count} questions; target is {target}")

    total_target = policy.get("question_total_target", 270)
    if state.question_count >= total_minimum and state.question_count < total_target:
        state.warn(f"Full benchmark has {state.question_count} questions; target is {total_target}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--manifest",
        type=Path,
        help="Repository-relative or absolute manifest JSON path to validate.",
    )
    parser.add_argument(
        "--profile",
        choices=["full", "fixture"],
        default="full",
        help="Use 'full' to enforce 200-question/domain gates; use 'fixture' for small offline samples.",
    )
    parser.add_argument(
        "--policy",
        type=Path,
        default=BENCHMARK_ROOT / "policy.json",
        help="Benchmark policy JSON path.",
    )
    parser.add_argument(
        "--taxonomy",
        type=Path,
        default=BENCHMARK_ROOT / "source_taxonomy.json",
        help="Source taxonomy JSON path.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    state = ValidationState()

    validate_all_schemas(state)
    policy = validate_policy(args.policy.resolve(), state)
    validate_taxonomy(args.taxonomy.resolve(), state)

    manifest = None
    question_files: list[Path] = []
    if args.manifest:
        manifest_path = args.manifest if args.manifest.is_absolute() else (REPO_ROOT / args.manifest)
        if policy is not None:
            manifest = validate_manifest(manifest_path.resolve(), policy, state)
        if manifest is not None and policy is not None:
            question_files = expand_question_files(manifest, state)
            validate_question_files(question_files, manifest, policy, state)
            enforce_count_gates(policy, args.profile, state)

    for warning in state.warnings:
        print(f"WARNING: {warning}", file=sys.stderr)
    if state.errors:
        for error in state.errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(
            f"FAILED: {len(state.errors)} error(s), {len(state.warnings)} warning(s)",
            file=sys.stderr,
        )
        return 1

    if args.manifest:
        counts = ", ".join(
            f"{domain}={count}" for domain, count in sorted(state.domain_counts.items())
        )
        print(
            "OK: "
            f"schemas={state.schema_count}, question_files={state.question_file_count}, "
            f"questions={state.question_count}, profile={args.profile}, domains=[{counts}]"
        )
    else:
        print(f"OK: schemas={state.schema_count}, policy=valid, taxonomy=valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
