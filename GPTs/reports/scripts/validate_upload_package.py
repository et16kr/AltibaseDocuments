#!/usr/bin/env python3
"""Validate the Stage 4 upload-package manifest and package boundary."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
REPORTS_DIR = ROOT / "GPTs/reports"
ATTACHMENTS_DIR = ROOT / "GPTs/attachments"
UPLOAD_DIR = ROOT / "GPTs/upload_package"
PLAN_PATH = REPORTS_DIR / "stage_04_upload_package_plan.md"
MANIFEST_PATH = REPORTS_DIR / "stage_04_upload_package_manifest.tsv"
VALIDATION_PATH = REPORTS_DIR / "stage_04_upload_package_validation.md"
PREFLIGHT_PATH = REPORTS_DIR / "stage_04_preflight_status.md"
SOURCE_MANIFEST = ROOT / "GPTs/source_pack/source_manifest.tsv"
SOURCE_TO_SHARD = ROOT / "GPTs/source_pack/source_to_shard_manifest.tsv"

EXPECTED_COUNT = 20
ASSEMBLY_STATUSES = {"planned_not_assembled", "assembled"}
VALIDATION_STATUSES = {"planned_scaffold", "assembled_validated"}
EXPECTED_AID_CANDIDATES = {
    "AID-000001",
    "AID-000002",
    "AID-000003",
    "AID-000004",
    "AID-000005",
}
REQUIRED_GUARDRAILS = {
    "CONF-000004",
    "CONF-000005",
    "CONF-000006",
    "CONF-000007",
    "CONF-000008",
    "CONF-000009",
}
EXCLUDED_SOURCE_IDS = {"SRC-000109", "SRC-000169"}
FINAL_AID_POLICY_TOKENS = [
    "final_aid_decision_recorded",
    "no_separate_aid_file",
    "AID-000005_separate_file_excluded",
    "accepted_limitations_evidence_only",
]
FINAL_APB_DISPOSITION_TOKEN = "final_deferred_no_customer_test_generation_playbook"

REQUIRED_SECTIONS = [
    "Package Role",
    "Applicable Versions And Authority",
    "Questions This File Can Answer",
    "Retrieval Alias Index",
    "Source Routes",
    "Task And Playbook Routing",
    "Answer-Ready Reference",
    "Required Inputs And Stop Conditions",
    "Validation And Rollback Checks",
    "Cross-References",
    "Residual Scope And Limitations",
]

MANIFEST_COLUMNS = [
    "upload_file_id",
    "upload_path",
    "source_attachment_path",
    "upload_title",
    "package_role",
    "owning_stage4_job",
    "assembly_status",
    "counts_against_20",
    "merge_policy",
    "required_sections",
    "source_route_expectation",
    "baseline_route_expectation",
    "playbook_route_expectation",
    "attachment_route_expectation",
    "aid_candidate_routes",
    "aid_integration_policy",
    "allowed_source_metadata",
    "internal_ids_excluded_from_upload",
    "guardrail_ids_carried",
    "apb_000014_disposition",
    "excluded_source_ids",
    "validation_status",
    "notes",
]

SOURCE_UPLOAD_CROSSWALK = REPORTS_DIR / "source_pack_to_upload_package_crosswalk.tsv"
BASELINE_UPLOAD_CROSSWALK = REPORTS_DIR / "korean_aligned_english_to_upload_package_crosswalk.tsv"
PLAYBOOK_UPLOAD_CROSSWALK = REPORTS_DIR / "playbook_to_upload_package_crosswalk.tsv"
ATTACHMENT_UPLOAD_CROSSWALK = REPORTS_DIR / "attachment_to_upload_package_crosswalk.tsv"

SOURCE_UPLOAD_COLUMNS = [
    "upload_file_id",
    "upload_path",
    "route_type",
    "source_id",
    "source_pack_block_id",
    "source_pack_block_ref",
    "authority_label",
    "version_scope",
    "source_family",
    "route_status",
    "notes",
]

BASELINE_UPLOAD_COLUMNS = [
    "upload_file_id",
    "upload_path",
    "baseline_route_scope",
    "baseline_block_ids",
    "source_ids",
    "source_pack_block_refs",
    "authority_label_policy",
    "upload_visibility",
    "route_status",
    "notes",
]

PLAYBOOK_UPLOAD_COLUMNS = [
    "upload_file_id",
    "upload_path",
    "playbook_id",
    "playbook_title",
    "validation_status",
    "generated_artifact_types",
    "required_missing_input_prompts",
    "protected_topic",
    "guardrail_ids",
    "upload_visibility",
    "route_status",
    "notes",
]

ATTACHMENT_UPLOAD_COLUMNS = [
    "upload_file_id",
    "upload_path",
    "source_attachment_path",
    "attachment_title",
    "included_sections",
    "transformation_policy",
    "required_sections_status",
    "route_status",
    "notes",
]

FORBIDDEN_UPLOAD_PATTERNS = [
    (re.compile(r"/home/et16"), "local workstation path"),
    (re.compile(r"~/AID"), "local AID workspace path"),
    (re.compile(r"\.codex-jobs"), "workflow runtime path"),
    (re.compile(r"\bevals/altibase_answerability/"), "internal benchmark run path"),
    (re.compile(r"\breview/scripts/"), "internal review script path"),
    (re.compile(r"\breview/reports/"), "internal review report path"),
    (re.compile(r"\brun-test\.log\b"), "internal run log name"),
    (re.compile(r"\bvalidate_upload_package\.py\b"), "validator implementation name"),
    (re.compile(r"\bstage_04_upload_package\b"), "internal Stage 4 artifact name"),
    (re.compile(r"\bGPTs/reports/"), "internal report path"),
    (re.compile(r"\bGPTs/attachments/"), "internal attachment path"),
    (re.compile(r"\bGPTs/source_pack/"), "internal source-pack path"),
    (re.compile(r"\bGPTs/agent_playbooks/"), "internal playbook path"),
    (re.compile(r"\bManuals/Altibase"), "repository source-tree path"),
    (re.compile(r"\bKAE-BLOCK-\d{6}\b"), "internal baseline block ID"),
    (re.compile(r"\bAID-\d{6}\b"), "internal AID tier ID"),
    (re.compile(r"\bAPB-\d{6}\b"), "internal playbook ID"),
    (re.compile(r"\bCONF-\d{6}\b"), "internal guardrail ID"),
    (re.compile(r"\bS3-SCOPE-\d{3}\b"), "internal Stage 3 scope ID"),
    (re.compile(r"\bS[1-4]R?-J\d{3}\b"), "internal job ID"),
]

STALE_AID_UPLOAD_PATTERNS = [
    (re.compile(r"later AID", re.IGNORECASE), "stale deferred AID wording"),
    (re.compile(r"later integration", re.IGNORECASE), "stale deferred AID wording"),
    (re.compile(r"later package pass", re.IGNORECASE), "stale deferred AID wording"),
    (re.compile(r"defer_unmatched_to_S4-J008"), "stale S4-J008 deferral token"),
]

STALE_PLACEHOLDER_PATTERNS = [
    (re.compile(r"\bTBD\b"), "stale placeholder token"),
    (re.compile(r"\bFIXME\b"), "stale placeholder token"),
    (re.compile(r"lorem ipsum", re.IGNORECASE), "stale placeholder prose"),
    (re.compile(r"to be filled", re.IGNORECASE), "stale placeholder prose"),
    (re.compile(r"to be added", re.IGNORECASE), "stale placeholder prose"),
    (re.compile(r"pending assembly", re.IGNORECASE), "stale assembly placeholder"),
    (re.compile(r"planned_not_assembled"), "stale manifest assembly status"),
    (re.compile(r"scaffold validation", re.IGNORECASE), "stale scaffold wording"),
    (re.compile(r"TODO:"), "unresolved TODO marker"),
]

CJK_RE = re.compile(r"[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uac00-\ud7af]")
LOCAL_LINK_RE = re.compile(r"\]\((?:file://|/home/et16|~/|[A-Za-z]:\\)")

SOURCE_ROUTE_STATUSES = {"pass"}
BASELINE_ROUTE_STATUSES = {"routed"}
PLAYBOOK_ROUTE_STATUSES = {"routed", "deferred_guardrail"}
ATTACHMENT_ROUTE_STATUSES = {"assembled"}


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def split_values(value: str) -> list[str]:
    return [item.strip() for item in value.split(";") if item.strip()]


def read_tsv(path: Path, errors: list[str]) -> list[dict[str, str]]:
    if not path.exists():
        errors.append(f"missing TSV: {rel(path)}")
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames != MANIFEST_COLUMNS:
            errors.append(
                f"{rel(path)} has unexpected columns: {reader.fieldnames!r}; "
                f"expected {MANIFEST_COLUMNS!r}"
            )
            return []
        return [
            {column: (row.get(column) or "").strip() for column in MANIFEST_COLUMNS}
            for row in reader
        ]


def read_any_tsv(path: Path, errors: list[str]) -> list[dict[str, str]]:
    if not path.exists():
        errors.append(f"missing TSV: {rel(path)}")
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def read_tsv_with_columns(
    path: Path, expected_columns: list[str], errors: list[str]
) -> list[dict[str, str]]:
    if not path.exists():
        errors.append(f"missing TSV: {rel(path)}")
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames != expected_columns:
            errors.append(
                f"{rel(path)} has unexpected columns: {reader.fieldnames!r}; "
                f"expected {expected_columns!r}"
            )
            return []
        return [
            {column: (row.get(column) or "").strip() for column in expected_columns}
            for row in reader
        ]


def check_required_docs(errors: list[str]) -> None:
    for path in (PLAN_PATH, MANIFEST_PATH, VALIDATION_PATH, PREFLIGHT_PATH):
        if not path.exists():
            errors.append(f"required Stage 4 file missing: {rel(path)}")

    if PLAN_PATH.exists():
        text = PLAN_PATH.read_text(encoding="utf-8")
        for token in (
            "Package Shape Decision",
            "Required Upload Markdown Sections",
            "Source Metadata Policy",
            "AID Selection Decision Path",
            "Manifest Schema",
            "Deterministic Validation Approach",
            "APB-000014",
            "CONF-000004",
            "CONF-000009",
        ):
            if token not in text:
                errors.append(f"{rel(PLAN_PATH)} missing required token: {token}")

    if VALIDATION_PATH.exists():
        text = VALIDATION_PATH.read_text(encoding="utf-8")
        for token in (
            "Scaffold Mode",
            "Assembled Mode",
            "Deterministic Check Matrix",
            "S4-J008 Final AID Decision",
            "CONF-000001",
            "CONF-000002",
            "AID-000005",
            "APB-000014",
            "SRC-000109",
            "SRC-000169",
        ):
            if token not in text:
                errors.append(f"{rel(VALIDATION_PATH)} missing required token: {token}")


def check_manifest_rows(rows: list[dict[str, str]], errors: list[str]) -> None:
    if len(rows) != EXPECTED_COUNT:
        errors.append(f"expected {EXPECTED_COUNT} manifest rows, found {len(rows)}")

    seen_ids: set[str] = set()
    seen_upload_paths: set[str] = set()
    seen_attachment_paths: set[str] = set()
    aid_seen: set[str] = set()
    guardrails_seen: set[str] = set()

    attachment_files = {
        path.name: path
        for path in ATTACHMENTS_DIR.glob("[0-9][0-9]_*.md")
        if path.is_file()
    }

    for index, row in enumerate(rows):
        row_label = row.get("upload_file_id") or f"row {index + 2}"
        expected_id = f"UPKG-{index:03d}"
        if row["upload_file_id"] != expected_id:
            errors.append(f"{row_label} expected upload_file_id {expected_id}")
        if row["upload_file_id"] in seen_ids:
            errors.append(f"duplicate upload_file_id: {row['upload_file_id']}")
        seen_ids.add(row["upload_file_id"])

        upload_path = row["upload_path"]
        if upload_path in seen_upload_paths:
            errors.append(f"{row_label} duplicates upload_path: {upload_path}")
        seen_upload_paths.add(upload_path)
        if not upload_path.startswith("GPTs/upload_package/") or not upload_path.endswith(".md"):
            errors.append(f"{row_label} upload_path must be GPTs/upload_package/*.md")

        attachment_path = row["source_attachment_path"]
        if attachment_path in seen_attachment_paths:
            errors.append(f"{row_label} duplicates source_attachment_path: {attachment_path}")
        seen_attachment_paths.add(attachment_path)
        if not attachment_path.startswith("GPTs/attachments/") or not attachment_path.endswith(".md"):
            errors.append(f"{row_label} source_attachment_path must be GPTs/attachments/*.md")
        attachment_file = ROOT / attachment_path
        if not attachment_file.exists():
            errors.append(f"{row_label} source attachment missing: {attachment_path}")
        if Path(upload_path).name != Path(attachment_path).name:
            errors.append(f"{row_label} must preserve attachment filename")
        if Path(attachment_path).name not in attachment_files:
            errors.append(f"{row_label} source attachment is not a numbered attachment")

        if row["assembly_status"] not in ASSEMBLY_STATUSES:
            errors.append(
                f"{row_label} assembly_status must be one of: "
                + ", ".join(sorted(ASSEMBLY_STATUSES))
            )
        if row["counts_against_20"] != "yes":
            errors.append(f"{row_label} counts_against_20 must be yes")
        if row["merge_policy"] != "preserve_attachment_filename":
            errors.append(f"{row_label} merge_policy must preserve attachment filename")
        if row["validation_status"] not in VALIDATION_STATUSES:
            errors.append(
                f"{row_label} validation_status must be one of: "
                + ", ".join(sorted(VALIDATION_STATUSES))
            )
        if (
            row["assembly_status"] == "planned_not_assembled"
            and row["validation_status"] != "planned_scaffold"
        ):
            errors.append(f"{row_label} planned rows must keep validation_status=planned_scaffold")
        if (
            row["assembly_status"] == "assembled"
            and row["validation_status"] != "assembled_validated"
        ):
            errors.append(f"{row_label} assembled rows must use validation_status=assembled_validated")

        sections = split_values(row["required_sections"])
        if sections != REQUIRED_SECTIONS:
            errors.append(f"{row_label} required_sections do not match Stage 4 policy")

        for field in (
            "source_route_expectation",
            "baseline_route_expectation",
            "playbook_route_expectation",
            "attachment_route_expectation",
            "aid_integration_policy",
            "allowed_source_metadata",
            "internal_ids_excluded_from_upload",
            "apb_000014_disposition",
            "notes",
        ):
            if not row[field]:
                errors.append(f"{row_label} has empty required field: {field}")

        if "no_KAE_ids_in_upload" not in row["baseline_route_expectation"]:
            errors.append(f"{row_label} must keep KAE IDs outside upload Markdown")
        if "APB-000014_deferred" not in row["playbook_route_expectation"]:
            errors.append(f"{row_label} must carry APB-000014 as deferred")
        if "SRC_AND_AID_SRC_IDS" not in row["allowed_source_metadata"]:
            errors.append(f"{row_label} must allow source IDs only as source metadata")
        if "SOURCE_PACK_BLOCK_IDS" not in row["allowed_source_metadata"]:
            errors.append(f"{row_label} must allow source-pack block metadata")
        if "defer_unmatched_to_S4-J008" in row["aid_integration_policy"]:
            errors.append(f"{row_label} still defers AID routing to S4-J008")
        for token in FINAL_AID_POLICY_TOKENS:
            if token not in row["aid_integration_policy"]:
                errors.append(f"{row_label} missing final AID policy token: {token}")
        if FINAL_APB_DISPOSITION_TOKEN not in row["apb_000014_disposition"]:
            errors.append(
                f"{row_label} must record final APB-000014 deferral disposition"
            )

        excluded_internal = set(split_values(row["internal_ids_excluded_from_upload"]))
        required_internal = {
            "KAE-BLOCK_IDS",
            "APB_IDS",
            "CONF_IDS",
            "S3_SCOPE_IDS",
            "JOB_IDS",
            "LOCAL_PATHS",
            "AID_TIER_IDS",
        }
        missing_internal = sorted(required_internal - excluded_internal)
        if missing_internal:
            errors.append(
                f"{row_label} missing internal ID exclusions: {', '.join(missing_internal)}"
            )

        guardrails = set(split_values(row["guardrail_ids_carried"]))
        unknown_guardrails = sorted(
            guardrail for guardrail in guardrails if not re.fullmatch(r"CONF-\d{6}", guardrail)
        )
        if unknown_guardrails:
            errors.append(f"{row_label} has invalid guardrail IDs: {', '.join(unknown_guardrails)}")
        guardrails_seen.update(guardrails)

        excluded = set(split_values(row["excluded_source_ids"]))
        if excluded != EXCLUDED_SOURCE_IDS:
            errors.append(f"{row_label} must record excluded source IDs SRC-000109 and SRC-000169")

        aid_routes = set(split_values(row["aid_candidate_routes"]))
        invalid_aid = sorted(aid for aid in aid_routes if not re.fullmatch(r"AID-\d{6}", aid))
        if invalid_aid:
            errors.append(f"{row_label} has invalid AID candidate IDs: {', '.join(invalid_aid)}")
        aid_seen.update(aid_routes)

    missing_aid = sorted(EXPECTED_AID_CANDIDATES - aid_seen)
    if missing_aid:
        errors.append("manifest does not cover AID candidates: " + ", ".join(missing_aid))

    missing_guardrails = sorted(REQUIRED_GUARDRAILS - guardrails_seen)
    if missing_guardrails:
        errors.append("manifest does not carry guardrails: " + ", ".join(missing_guardrails))


def upload_markdown_files() -> list[Path]:
    if not UPLOAD_DIR.exists():
        return []
    return sorted(path for path in UPLOAD_DIR.glob("*.md") if path.is_file())


def check_scaffold_boundary(errors: list[str]) -> None:
    files = upload_markdown_files()
    if files:
        errors.append(
            "scaffold mode expects no upload Markdown files, found: "
            + ", ".join(rel(path) for path in files)
        )


def check_upload_crosswalks(
    rows: list[dict[str, str]],
    files: list[Path],
    errors: list[str],
    allow_partial: bool = False,
) -> None:
    source_rows = read_tsv_with_columns(SOURCE_UPLOAD_CROSSWALK, SOURCE_UPLOAD_COLUMNS, errors)
    baseline_rows = read_tsv_with_columns(BASELINE_UPLOAD_CROSSWALK, BASELINE_UPLOAD_COLUMNS, errors)
    playbook_rows = read_tsv_with_columns(PLAYBOOK_UPLOAD_CROSSWALK, PLAYBOOK_UPLOAD_COLUMNS, errors)
    attachment_rows = read_tsv_with_columns(
        ATTACHMENT_UPLOAD_CROSSWALK, ATTACHMENT_UPLOAD_COLUMNS, errors
    )
    if errors:
        return

    manifest_by_id = {row["upload_file_id"]: row for row in rows}
    manifest_by_path = {row["upload_path"]: row for row in rows}
    known_source_ids = {
        row.get("source_id", "")
        for row in read_any_tsv(SOURCE_MANIFEST, errors)
        if row.get("source_id")
    }
    known_block_ids = {
        row.get("block_id", "")
        for row in read_any_tsv(SOURCE_TO_SHARD, errors)
        if row.get("block_id")
    }
    if errors:
        return

    def validate_common_rows(
        name: str,
        collection: list[dict[str, str]],
        allowed_statuses: set[str],
    ) -> None:
        for line_number, crosswalk_row in enumerate(collection, start=2):
            row_id = crosswalk_row.get("upload_file_id", "")
            upload_path = crosswalk_row.get("upload_path", "")
            row_label = f"{rel(REPORTS_DIR / name)} line {line_number}"

            if row_id not in manifest_by_id:
                errors.append(f"{row_label} references unknown upload_file_id: {row_id}")
            elif manifest_by_id[row_id]["upload_path"] != upload_path:
                errors.append(
                    f"{row_label} upload_path does not match manifest row {row_id}: {upload_path}"
                )

            if upload_path not in manifest_by_path:
                errors.append(f"{row_label} references upload_path outside manifest: {upload_path}")

            route_status = crosswalk_row.get("route_status", "")
            if route_status not in allowed_statuses:
                errors.append(
                    f"{row_label} has invalid route_status {route_status!r}; "
                    + "expected one of "
                    + ", ".join(sorted(allowed_statuses))
                )

    validate_common_rows(
        SOURCE_UPLOAD_CROSSWALK.name,
        source_rows,
        SOURCE_ROUTE_STATUSES,
    )
    validate_common_rows(
        BASELINE_UPLOAD_CROSSWALK.name,
        baseline_rows,
        BASELINE_ROUTE_STATUSES,
    )
    validate_common_rows(
        PLAYBOOK_UPLOAD_CROSSWALK.name,
        playbook_rows,
        PLAYBOOK_ROUTE_STATUSES,
    )
    validate_common_rows(
        ATTACHMENT_UPLOAD_CROSSWALK.name,
        attachment_rows,
        ATTACHMENT_ROUTE_STATUSES,
    )

    for line_number, source_row in enumerate(source_rows, start=2):
        row_label = f"{rel(SOURCE_UPLOAD_CROSSWALK)} line {line_number}"
        source_id = source_row["source_id"]
        block_id = source_row["source_pack_block_id"]
        if source_id in EXCLUDED_SOURCE_IDS:
            errors.append(f"{row_label} routes excluded source ID: {source_id}")
        if source_id not in known_source_ids:
            errors.append(f"{row_label} references unknown source ID: {source_id}")
        if block_id not in known_block_ids:
            errors.append(f"{row_label} references unknown source-pack block ID: {block_id}")
        expected_ref = f"{source_id}/{block_id}"
        if source_row["source_pack_block_ref"] != expected_ref:
            errors.append(
                f"{row_label} source_pack_block_ref must be {expected_ref}, "
                f"found {source_row['source_pack_block_ref']}"
            )
        for required_field in ("route_type", "authority_label", "version_scope", "source_family"):
            if not source_row[required_field]:
                errors.append(f"{row_label} has empty required field: {required_field}")

    for line_number, baseline_row in enumerate(baseline_rows, start=2):
        row_label = f"{rel(BASELINE_UPLOAD_CROSSWALK)} line {line_number}"
        if "no_baseline_ids_in_upload" not in baseline_row["upload_visibility"]:
            errors.append(f"{row_label} must keep baseline IDs outside upload Markdown")
        if not baseline_row["baseline_block_ids"]:
            errors.append(f"{row_label} must record baseline blocks or AID decision evidence")
        if not baseline_row["authority_label_policy"]:
            errors.append(f"{row_label} has empty authority_label_policy")

    for line_number, playbook_row in enumerate(playbook_rows, start=2):
        row_label = f"{rel(PLAYBOOK_UPLOAD_CROSSWALK)} line {line_number}"
        playbook_id = playbook_row["playbook_id"]
        if playbook_id == "APB-000014":
            if playbook_row["validation_status"] != "planned":
                errors.append(f"{row_label} APB-000014 must remain planned")
            if playbook_row["upload_visibility"] != "deferred_not_uploaded":
                errors.append(f"{row_label} APB-000014 must remain deferred_not_uploaded")
            if playbook_row["route_status"] != "deferred_guardrail":
                errors.append(f"{row_label} APB-000014 must remain a deferred guardrail")
        else:
            if playbook_row["validation_status"] != "pass":
                errors.append(f"{row_label} non-deferred playbook route must have pass status")
            if "no_playbook_ids_in_upload" not in playbook_row["upload_visibility"]:
                errors.append(f"{row_label} must keep playbook IDs outside upload Markdown")
            if playbook_row["route_status"] != "routed":
                errors.append(f"{row_label} non-deferred playbook route must be routed")
        if not playbook_row["required_missing_input_prompts"]:
            errors.append(f"{row_label} has empty required_missing_input_prompts")

    attachment_row_counts: dict[str, int] = {}
    for line_number, attachment_row in enumerate(attachment_rows, start=2):
        row_label = f"{rel(ATTACHMENT_UPLOAD_CROSSWALK)} line {line_number}"
        upload_path = attachment_row["upload_path"]
        attachment_row_counts[upload_path] = attachment_row_counts.get(upload_path, 0) + 1
        manifest_row = manifest_by_path.get(upload_path)
        if manifest_row:
            if attachment_row["source_attachment_path"] != manifest_row["source_attachment_path"]:
                errors.append(
                    f"{row_label} source_attachment_path does not match manifest: "
                    f"{attachment_row['source_attachment_path']}"
                )
            if split_values(attachment_row["required_sections_status"]) != REQUIRED_SECTIONS:
                errors.append(f"{row_label} required_sections_status does not match policy")
            if "preserve_answer_ready_reference" not in attachment_row["transformation_policy"]:
                errors.append(f"{row_label} must preserve answer-ready reference content")

    source_by_path: dict[str, list[dict[str, str]]] = {}
    baseline_by_path: dict[str, list[dict[str, str]]] = {}
    playbook_by_path: dict[str, list[dict[str, str]]] = {}
    attachment_by_path: dict[str, list[dict[str, str]]] = {}
    for collection, target in (
        (source_rows, source_by_path),
        (baseline_rows, baseline_by_path),
        (playbook_rows, playbook_by_path),
        (attachment_rows, attachment_by_path),
    ):
        for row in collection:
            target.setdefault(row["upload_path"], []).append(row)

    file_paths = {rel(path) for path in files}
    required_rows = (
        [row for row in rows if row["upload_path"] in file_paths]
        if allow_partial
        else rows
    )

    for manifest_row in required_rows:
        upload_path = manifest_row["upload_path"]
        row_label = manifest_row["upload_file_id"]
        for name, grouped in (
            ("source-pack", source_by_path),
            ("Korean-aligned English", baseline_by_path),
            ("playbook", playbook_by_path),
            ("attachment", attachment_by_path),
        ):
            if not grouped.get(upload_path):
                errors.append(f"{row_label} missing {name} upload-package crosswalk rows")
        if attachment_row_counts.get(upload_path, 0) != 1:
            errors.append(f"{row_label} must have exactly one attachment crosswalk row")

    for path in files:
        upload_path = rel(path)
        row_label = manifest_by_path.get(upload_path, {}).get("upload_file_id", upload_path)
        text = path.read_text(encoding="utf-8")
        upload_source_rows = source_by_path.get(upload_path, [])
        crosswalk_source_ids = {row["source_id"] for row in upload_source_rows if row["source_id"]}
        crosswalk_block_ids = {
            row["source_pack_block_id"] for row in upload_source_rows if row["source_pack_block_id"]
        }
        for source_id in sorted(set(re.findall(r"\b(?:SRC|AID-SRC)-\d{6}\b", text))):
            if source_id not in crosswalk_source_ids:
                errors.append(f"{row_label} source ID lacks source-pack crosswalk row: {source_id}")
        for block_id in sorted(set(re.findall(r"\bBLOCK-\d{6}\b", text))):
            if block_id not in crosswalk_block_ids:
                errors.append(f"{row_label} block ID lacks source-pack crosswalk row: {block_id}")


def check_assembled_package(
    rows: list[dict[str, str]], errors: list[str], allow_partial: bool = False
) -> None:
    files = upload_markdown_files()
    manifest_by_path = {row["upload_path"]: row for row in rows}
    manifest_paths = {row["upload_path"] for row in rows}
    file_paths = {rel(path) for path in files}
    known_source_ids = {
        row.get("source_id", "")
        for row in read_any_tsv(SOURCE_MANIFEST, errors)
        if row.get("source_id")
    }
    known_block_ids = {
        row.get("block_id", "")
        for row in read_any_tsv(SOURCE_TO_SHARD, errors)
        if row.get("block_id")
    }

    if not files:
        errors.append("assembled mode requires upload Markdown files")
        return
    if len(files) > EXPECTED_COUNT:
        errors.append(f"assembled upload package has {len(files)} Markdown files; limit is {EXPECTED_COUNT}")

    missing = sorted(manifest_paths - file_paths)
    extra = sorted(file_paths - manifest_paths)
    if missing and not allow_partial:
        errors.append("manifest rows missing assembled files: " + ", ".join(missing))
    if extra:
        errors.append("assembled files not listed in manifest: " + ", ".join(extra))

    for path in files:
        row = manifest_by_path.get(rel(path))
        if not row:
            continue
        if row["assembly_status"] != "assembled":
            errors.append(f"{row['upload_file_id']} has file but assembly_status is not assembled")
        if row["validation_status"] != "assembled_validated":
            errors.append(
                f"{row['upload_file_id']} has file but validation_status is not assembled_validated"
            )

    if not allow_partial:
        for row in rows:
            if row["assembly_status"] != "assembled":
                errors.append(f"{row['upload_file_id']} full assembled mode requires assembled status")

    for path in files:
        text = path.read_text(encoding="utf-8")
        label = rel(path)
        for section in REQUIRED_SECTIONS:
            if not re.search(rf"^## {re.escape(section)}$", text, re.MULTILINE):
                errors.append(f"{label} missing required section: {section}")

        for pattern, reason in FORBIDDEN_UPLOAD_PATTERNS:
            match = pattern.search(text)
            if match:
                errors.append(f"{label} contains forbidden {reason}: {match.group(0)}")
        for pattern, reason in STALE_AID_UPLOAD_PATTERNS:
            match = pattern.search(text)
            if match:
                errors.append(f"{label} contains {reason}: {match.group(0)}")
        for pattern, reason in STALE_PLACEHOLDER_PATTERNS:
            match = pattern.search(text)
            if match:
                errors.append(f"{label} contains {reason}: {match.group(0)}")

        cjk_match = CJK_RE.search(text)
        if cjk_match:
            errors.append(f"{label} contains CJK character: {cjk_match.group(0)}")

        link_match = LOCAL_LINK_RE.search(text)
        if link_match:
            errors.append(f"{label} contains local filesystem link: {link_match.group(0)}")

        for source_id in EXCLUDED_SOURCE_IDS:
            if source_id in text:
                errors.append(f"{label} contains excluded source ID: {source_id}")

        if "8.1" in text and "Altibase 8.1 verified source" not in text:
            errors.append(
                f"{label} mentions 8.1 but does not preserve "
                "`Altibase 8.1 verified source` wording"
            )

        if text.count("```") % 2:
            errors.append(f"{label} has unbalanced fenced code blocks")

        for source_id in re.findall(r"\b(?:SRC|AID-SRC)-\d{6}\b", text):
            if source_id not in known_source_ids:
                errors.append(f"{label} references unknown source ID: {source_id}")

        for block_id in re.findall(r"\bBLOCK-\d{6}\b", text):
            if block_id not in known_block_ids:
                errors.append(f"{label} references unknown source-pack block ID: {block_id}")

        for link in re.findall(r"\]\(([^)#]+\.md)(?:#[^)]+)?\)", text):
            if "://" in link:
                continue
            target = (path.parent / link).resolve()
            try:
                target.relative_to(UPLOAD_DIR.resolve())
            except ValueError:
                errors.append(f"{label} links outside upload package: {link}")
                continue
            if not target.exists():
                errors.append(f"{label} has broken upload-package link: {link}")

    check_upload_crosswalks(rows, files, errors, allow_partial=allow_partial)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--assembled",
        action="store_true",
        help="Validate assembled GPTs/upload_package Markdown files.",
    )
    parser.add_argument(
        "--allow-partial",
        action="store_true",
        help="Allow a progressive Stage 4 slice where only assembled manifest rows have files.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors: list[str] = []

    check_required_docs(errors)
    rows = read_tsv(MANIFEST_PATH, errors)
    if rows:
        check_manifest_rows(rows, errors)
        if args.assembled:
            check_assembled_package(rows, errors, allow_partial=args.allow_partial)
        else:
            check_scaffold_boundary(errors)

    if errors:
        print("Stage 4 upload package validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Stage 4 upload package validation passed.")
    print(f"- Manifest rows: {len(rows)}")
    if args.assembled:
        print(f"- Upload Markdown files: {len(upload_markdown_files())}")
        if args.allow_partial:
            print("- Mode: assembled partial")
        print("- Required sections and upload-boundary scans: passed")
        print("- Source, baseline, playbook, and attachment crosswalk routes: passed")
        print("- Excluded-source, AID limitation, stale-placeholder, and CJK scans: passed")
    else:
        print("- Mode: scaffold")
        print("- Upload Markdown files: 0")
        print("- Planned rows are not yet assembled by design")
    return 0


if __name__ == "__main__":
    sys.exit(main())
