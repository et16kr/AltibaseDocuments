#!/usr/bin/env python3
"""Validate the Stage 3 customer-facing attachment scaffold."""

from __future__ import annotations

import csv
import argparse
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
ATTACHMENT_DIR = ROOT / "GPTs/attachments"
SCOPE_PATH = ROOT / "GPTs/reports/stage_03_attachment_followup_scope.tsv"
SOURCE_ATTACHMENT_CROSSWALK = ROOT / "GPTs/reports/source_pack_to_attachment_crosswalk.tsv"
BASELINE_ATTACHMENT_CROSSWALK = (
    ROOT / "GPTs/reports/korean_aligned_english_to_attachment_crosswalk.tsv"
)
PLAYBOOK_ATTACHMENT_CROSSWALK = ROOT / "GPTs/reports/playbook_to_attachment_crosswalk.tsv"
PLAYBOOK_MANIFEST = ROOT / "GPTs/agent_playbooks/playbook_manifest.tsv"
SOURCE_MANIFEST = ROOT / "GPTs/source_pack/source_manifest.tsv"
SOURCE_TO_SHARD = ROOT / "GPTs/source_pack/source_to_shard_manifest.tsv"
BASELINE_MANIFEST = ROOT / "GPTs/korean_aligned_english/baseline_manifest.tsv"
STAGE3_BASE_COMMIT = "5538c9a8"

EXPECTED_ATTACHMENT_COUNT = 20

REQUIRED_ATTACHMENT_SECTIONS = [
    "Applicable Versions",
    "Questions This File Can Answer",
    "Retrieval Alias Index",
    "Source Documents",
    "Response Rules",
    "Attachment Cross-References",
    "Residual Scope",
]

SCOPE_COLUMNS = [
    "scope_row_id",
    "source_inventory_job_group",
    "owning_stage3_job",
    "priority",
    "question_ids",
    "exact_tokens",
    "critical_fact_ids_or_notes",
    "target_attachments",
    "source_ids_or_route_requirement",
    "source_pack_block_ids_where_known",
    "korean_aligned_baseline_block_ids_where_known",
    "stage2_playbook_ids",
    "protected_topic_flag",
    "expected_disposition",
    "current_status",
    "validation_notes",
]

SOURCE_ATTACHMENT_CROSSWALK_COLUMNS = [
    "scope_row_id",
    "source_inventory_job_group",
    "owning_stage3_job",
    "attachment_path",
    "attachment_title",
    "source_id",
    "source_origin",
    "source_role",
    "source_family",
    "source_title",
    "version_scope",
    "authority_label",
    "source_pack_shard_id",
    "source_pack_block_id",
    "source_pack_block_ref",
    "source_pack_validation_status",
    "question_ids",
    "exact_tokens",
    "stage2_playbook_ids",
    "protected_topic_flag",
    "stage3_disposition",
    "stage3_status",
    "notes",
]

BASELINE_ATTACHMENT_CROSSWALK_COLUMNS = [
    "scope_row_id",
    "source_inventory_job_group",
    "owning_stage3_job",
    "attachment_path",
    "attachment_title",
    "baseline_block_id",
    "baseline_source_type",
    "planned_downstream_use",
    "alignment_status",
    "source_family",
    "version_scope",
    "authority_label",
    "source_ids",
    "source_pack_block_ids",
    "question_ids",
    "stage2_playbook_ids",
    "protected_topic_flag",
    "stage3_disposition",
    "stage3_status",
    "notes",
]

PLAYBOOK_ATTACHMENT_CROSSWALK_COLUMNS = [
    "scope_row_id",
    "source_inventory_job_group",
    "owning_stage3_job",
    "attachment_path",
    "attachment_title",
    "playbook_id",
    "playbook_path",
    "playbook_title",
    "domain",
    "validation_status",
    "supported_versions",
    "source_ids",
    "source_pack_block_ids",
    "korean_aligned_baseline_block_ids",
    "generated_artifact_types",
    "protected_topic",
    "guardrail_ids",
    "question_ids",
    "protected_topic_flag",
    "stage3_disposition",
    "stage3_status",
    "notes",
]

EXPECTED_STAGE3_BY_SOURCE_GROUP = {
    "J004": "S3-J003",
    "J005": "S3-J004",
    "J006": "S3-J005",
    "J007": "S3-J006",
    "J008": "S3-J007",
    "J009": "S3-J008",
    "J010": "S3-J009",
    "J011": "S3-J010",
    "J012": "S3-J011",
    "J013": "S3-J012",
    "J014": "S3-J013",
    "J015": "S3-J014",
    "J016": "S3-J015",
    "J017": "S3-J016",
}

ALLOWED_PRIORITIES = {"P0", "P1", "P2", "P3"}
ALLOWED_PROTECTED_FLAGS = {"yes", "no"}
ALLOWED_DISPOSITIONS = {
    "attachment_update",
    "retrieval_alias_update",
    "crosslink_update",
    "recorded_gap",
    "already_covered",
    "blocked",
}
ALLOWED_STATUSES = {
    "planned",
    "in_progress",
    "done",
    "blocked",
    "recorded_gap",
    "already_covered",
}

FORBIDDEN_ATTACHMENT_PATTERNS = [
    (re.compile(r"/home/et16"), "local workstation path"),
    (re.compile(r"~/AID"), "local AID workspace path"),
    (re.compile(r"\.codex-jobs"), "workflow runtime path"),
    (re.compile(r"\bGPTs/"), "repository-internal GPT path"),
    (re.compile(r"\bManuals/Altibase"), "repository source-tree path"),
    (re.compile(r"\bsource_pack\b"), "internal source-pack label"),
    (re.compile(r"\bkorean_aligned_english\b"), "internal baseline path label"),
    (re.compile(r"\bplaybook_manifest\.tsv\b"), "internal playbook manifest name"),
    (re.compile(r"\bsource_manifest\.tsv\b"), "internal source manifest name"),
    (re.compile(r"\bsource_to_shard_manifest\.tsv\b"), "internal shard manifest name"),
    (re.compile(r"\bKAE-BLOCK-\d{6}\b"), "internal Korean-aligned block ID"),
    (re.compile(r"\bAID-SRC-\d{6}\b"), "internal AID source ID"),
    (re.compile(r"\bSRC-\d{6}\b"), "internal source ID"),
    (re.compile(r"\bBLOCK-\d{6}\b"), "internal source-pack block ID"),
    (re.compile(r"\bSHARD-\d{3}\b"), "internal source-pack shard ID"),
    (re.compile(r"\bcandidate_with_open_recheck_guardrail\b"), "internal routing status"),
    (re.compile(r"\bprimary_working_source\b"), "internal routing label"),
    (re.compile(r"\bupload_content_candidate\b"), "internal AID upload label"),
    (re.compile(r"\benglish_only_auxiliary\b"), "internal AID confidence label"),
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def split_values(value: str) -> list[str]:
    return [item.strip() for item in value.split(";") if item.strip()]


def load_id_set(path: Path, column: str) -> set[str]:
    return {row[column] for row in read_tsv(path)}


def attachment_files() -> list[Path]:
    return sorted(
        path
        for path in ATTACHMENT_DIR.glob("*.md")
        if path.name != "README.md"
    )


def git_diff_name_only(base: str, pathspec: str, failures: list[str]) -> list[str]:
    result = subprocess.run(
        ["git", "diff", "--name-only", base, "--", pathspec],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        failures.append(
            f"could not inspect git diff from {base} for {pathspec}: "
            f"{result.stderr.strip() or result.stdout.strip()}"
        )
        return []
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def check_attachment_shape(failures: list[str]) -> None:
    files = attachment_files()
    if len(files) != EXPECTED_ATTACHMENT_COUNT:
        failures.append(
            "expected exactly "
            f"{EXPECTED_ATTACHMENT_COUNT} customer-facing attachment Markdown files "
            f"excluding README.md, found {len(files)}"
        )

    for path in files:
        text = path.read_text(encoding="utf-8")
        for section in REQUIRED_ATTACHMENT_SECTIONS:
            pattern = rf"^## {re.escape(section)}$"
            if not re.search(pattern, text, re.MULTILINE):
                failures.append(f"{path.relative_to(ROOT)} missing top-level section: {section}")

        if "8.1" in text and "Altibase 8.1 verified source" not in text:
            failures.append(
                f"{path.relative_to(ROOT)} mentions 8.1 but does not preserve "
                "`Altibase 8.1 verified source` wording"
            )


def check_forbidden_attachment_text(failures: list[str]) -> None:
    for path in attachment_files():
        text = path.read_text(encoding="utf-8")
        for pattern, label in FORBIDDEN_ATTACHMENT_PATTERNS:
            match = pattern.search(text)
            if match:
                failures.append(
                    f"{path.relative_to(ROOT)} contains forbidden {label}: {match.group(0)}"
                )


def check_upload_package_clean(failures: list[str]) -> None:
    changed_paths = git_diff_name_only(STAGE3_BASE_COMMIT, "GPTs/upload_package", failures)
    if changed_paths:
        failures.append(
            "Stage 3 attachment work must not change GPTs/upload_package; "
            "changed upload-package paths found:\n"
            + "\n".join(changed_paths)
        )

    result = subprocess.run(
        ["git", "status", "--porcelain", "--", "GPTs/upload_package"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        failures.append(
            "could not inspect GPTs/upload_package git status: "
            f"{result.stderr.strip() or result.stdout.strip()}"
        )
        return
    if result.stdout.strip():
        failures.append(
            "Stage 3 attachment validation does not require GPTs/upload_package edits; "
            "uncommitted upload-package paths found:\n"
            f"{result.stdout.rstrip()}"
        )


def read_required_tsv(path: Path, columns: list[str], failures: list[str]) -> list[dict[str, str]]:
    if not path.exists():
        failures.append(f"missing Stage 3 crosswalk TSV: {path.relative_to(ROOT)}")
        return []

    with path.open(newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        actual_columns = reader.fieldnames or []
        missing_columns = [column for column in columns if column not in actual_columns]
        if missing_columns:
            failures.append(
                f"{path.relative_to(ROOT)} missing required columns: "
                + ", ".join(missing_columns)
            )
            return []
        rows = list(reader)

    if not rows:
        failures.append(f"{path.relative_to(ROOT)} has no data rows")
    return rows


def check_scope_tsv(failures: list[str]) -> None:
    if not SCOPE_PATH.exists():
        failures.append(f"missing Stage 3 scope TSV: {SCOPE_PATH.relative_to(ROOT)}")
        return

    with SCOPE_PATH.open(newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        columns = reader.fieldnames or []
        missing_columns = [column for column in SCOPE_COLUMNS if column not in columns]
        if missing_columns:
            failures.append(
                f"{SCOPE_PATH.relative_to(ROOT)} missing required columns: "
                + ", ".join(missing_columns)
            )
            return
        rows = list(reader)

    if not rows:
        failures.append(f"{SCOPE_PATH.relative_to(ROOT)} has no data rows")
        return

    playbook_ids = load_id_set(PLAYBOOK_MANIFEST, "playbook_id")
    source_ids = load_id_set(SOURCE_MANIFEST, "source_id")
    source_block_pairs = {
        f"{row['source_id']}/{row['block_id']}"
        for row in read_tsv(SOURCE_TO_SHARD)
    }
    baseline_ids = load_id_set(BASELINE_MANIFEST, "baseline_block_id")
    attachment_path_set = {str(path.relative_to(ROOT)) for path in attachment_files()}

    seen_row_ids: set[str] = set()
    covered_groups: set[str] = set()

    for number, row in enumerate(rows, start=2):
        row_id = row["scope_row_id"]
        if not re.fullmatch(r"S3-SCOPE-\d{3}", row_id):
            failures.append(f"scope row {number} has invalid scope_row_id: {row_id}")
        if row_id in seen_row_ids:
            failures.append(f"duplicate scope_row_id: {row_id}")
        seen_row_ids.add(row_id)

        group = row["source_inventory_job_group"]
        if group not in EXPECTED_STAGE3_BY_SOURCE_GROUP:
            failures.append(f"{row_id} has invalid source inventory job group: {group}")
        else:
            covered_groups.add(group)
            expected_stage3 = EXPECTED_STAGE3_BY_SOURCE_GROUP[group]
            if row["owning_stage3_job"] != expected_stage3:
                failures.append(
                    f"{row_id} maps {group} to {row['owning_stage3_job']}, "
                    f"expected {expected_stage3}"
                )

        if row["priority"] not in ALLOWED_PRIORITIES:
            failures.append(f"{row_id} has invalid priority: {row['priority']}")

        question_ids = split_values(row["question_ids"])
        if not question_ids:
            failures.append(f"{row_id} has no question_ids")
        for question_id in question_ids:
            if not re.fullmatch(r"(PROP|SQL|ERR|OPS|REPL|VPM|TOOL)-\d{3}", question_id):
                failures.append(f"{row_id} has invalid question ID: {question_id}")

        if not row["exact_tokens"].strip():
            failures.append(f"{row_id} has no exact token anchors")
        if not row["critical_fact_ids_or_notes"].strip():
            failures.append(f"{row_id} has no critical fact IDs or notes")

        for target in split_values(row["target_attachments"]):
            if target not in attachment_path_set:
                failures.append(f"{row_id} has invalid attachment target: {target}")

        source_route = row["source_ids_or_route_requirement"].strip()
        if not source_route:
            failures.append(f"{row_id} has no source ID or route requirement")
        for source_id in re.findall(r"\b(?:AID-SRC|SRC)-\d{6}\b", source_route):
            if source_id not in source_ids:
                failures.append(f"{row_id} references unknown source ID: {source_id}")

        for source_block_pair in split_values(row["source_pack_block_ids_where_known"]):
            if source_block_pair not in source_block_pairs:
                failures.append(
                    f"{row_id} references unknown source-pack block pair: "
                    f"{source_block_pair}"
                )

        for baseline_id in split_values(row["korean_aligned_baseline_block_ids_where_known"]):
            if baseline_id not in baseline_ids:
                failures.append(f"{row_id} references unknown baseline block: {baseline_id}")

        for playbook_id in split_values(row["stage2_playbook_ids"]):
            if playbook_id not in playbook_ids:
                failures.append(f"{row_id} references unknown playbook ID: {playbook_id}")

        if row["protected_topic_flag"] not in ALLOWED_PROTECTED_FLAGS:
            failures.append(
                f"{row_id} has invalid protected_topic_flag: {row['protected_topic_flag']}"
            )
        if row["expected_disposition"] not in ALLOWED_DISPOSITIONS:
            failures.append(
                f"{row_id} has invalid expected_disposition: {row['expected_disposition']}"
            )
        if row["current_status"] not in ALLOWED_STATUSES:
            failures.append(f"{row_id} has invalid current_status: {row['current_status']}")
        if not row["validation_notes"].strip():
            failures.append(f"{row_id} has no validation_notes")

    missing_groups = sorted(set(EXPECTED_STAGE3_BY_SOURCE_GROUP) - covered_groups)
    if missing_groups:
        failures.append(
            "Stage 3 scope TSV does not cover source inventory job groups: "
            + ", ".join(missing_groups)
        )


def check_completed_scope_exact_tokens(failures: list[str]) -> None:
    """For completed scope rows, require exact tokens in the row's target files."""
    if not SCOPE_PATH.exists():
        return

    for row in read_tsv(SCOPE_PATH):
        if row.get("current_status") not in {"done", "already_covered"}:
            continue

        targets = split_values(row.get("target_attachments", ""))
        combined = ""
        for target in targets:
            path = ROOT / target
            if path.exists():
                combined += "\n" + path.read_text(encoding="utf-8")

        missing_tokens = [
            token
            for token in split_values(row.get("exact_tokens", ""))
            if token not in combined
        ]
        if missing_tokens:
            failures.append(
                f"{row['scope_row_id']} is {row['current_status']} but target "
                "attachments are missing exact token(s): " + ", ".join(missing_tokens)
            )


def check_attachment_crosswalks(failures: list[str]) -> None:
    source_rows = read_required_tsv(
        SOURCE_ATTACHMENT_CROSSWALK,
        SOURCE_ATTACHMENT_CROSSWALK_COLUMNS,
        failures,
    )
    baseline_rows = read_required_tsv(
        BASELINE_ATTACHMENT_CROSSWALK,
        BASELINE_ATTACHMENT_CROSSWALK_COLUMNS,
        failures,
    )
    playbook_rows = read_required_tsv(
        PLAYBOOK_ATTACHMENT_CROSSWALK,
        PLAYBOOK_ATTACHMENT_CROSSWALK_COLUMNS,
        failures,
    )
    if failures:
        return

    attachment_path_set = {str(path.relative_to(ROOT)) for path in attachment_files()}
    source_ids = load_id_set(SOURCE_MANIFEST, "source_id")
    source_block_pairs = {
        f"{row['source_id']}/{row['block_id']}"
        for row in read_tsv(SOURCE_TO_SHARD)
    }
    baseline_ids = load_id_set(BASELINE_MANIFEST, "baseline_block_id")
    playbook_ids = load_id_set(PLAYBOOK_MANIFEST, "playbook_id")

    scope_rows = read_tsv(SCOPE_PATH) if SCOPE_PATH.exists() else []
    scope_row_ids = {row["scope_row_id"] for row in scope_rows}
    completed_target_attachments: set[str] = set()
    for row in scope_rows:
        if row.get("current_status") in {"done", "already_covered"}:
            completed_target_attachments.update(split_values(row["target_attachments"]))

    edited_attachments = {
        path
        for path in git_diff_name_only(STAGE3_BASE_COMMIT, "GPTs/attachments", failures)
        if path in attachment_path_set
    }

    source_attachment_paths = {row["attachment_path"] for row in source_rows}
    baseline_attachment_paths = {row["attachment_path"] for row in baseline_rows}
    playbook_attachment_paths = {row["attachment_path"] for row in playbook_rows}

    for path in sorted(completed_target_attachments | edited_attachments):
        if path not in source_attachment_paths:
            failures.append(f"{path} has no source-pack-to-attachment crosswalk route")
        if path not in baseline_attachment_paths:
            failures.append(
                f"{path} has no Korean-aligned-English-to-attachment crosswalk route"
            )
        if path not in playbook_attachment_paths:
            failures.append(f"{path} has no playbook-to-attachment crosswalk route")

    for path, rows, row_label in [
        (SOURCE_ATTACHMENT_CROSSWALK, source_rows, "source crosswalk"),
        (BASELINE_ATTACHMENT_CROSSWALK, baseline_rows, "baseline crosswalk"),
        (PLAYBOOK_ATTACHMENT_CROSSWALK, playbook_rows, "playbook crosswalk"),
    ]:
        seen_keys: set[tuple[str, ...]] = set()
        for number, row in enumerate(rows, start=2):
            row_id = row["scope_row_id"]
            if row_id not in scope_row_ids:
                failures.append(
                    f"{path.relative_to(ROOT)} row {number} references unknown "
                    f"scope_row_id: {row_id}"
                )
            if row["attachment_path"] not in attachment_path_set:
                failures.append(
                    f"{path.relative_to(ROOT)} row {number} has invalid attachment_path: "
                    f"{row['attachment_path']}"
                )
            if row["stage3_status"] not in ALLOWED_STATUSES:
                failures.append(
                    f"{path.relative_to(ROOT)} row {number} has invalid stage3_status: "
                    f"{row['stage3_status']}"
                )
            if row["stage3_disposition"] not in ALLOWED_DISPOSITIONS:
                failures.append(
                    f"{path.relative_to(ROOT)} row {number} has invalid "
                    f"stage3_disposition: {row['stage3_disposition']}"
                )

            if row_label == "source crosswalk":
                if row["source_id"] not in source_ids:
                    failures.append(
                        f"{path.relative_to(ROOT)} row {number} references unknown "
                        f"source_id: {row['source_id']}"
                    )
                block_ref = row["source_pack_block_ref"]
                if block_ref not in source_block_pairs:
                    failures.append(
                        f"{path.relative_to(ROOT)} row {number} references unknown "
                        f"source_pack_block_ref: {block_ref}"
                    )
                key = (row_id, row["attachment_path"], row["source_pack_block_ref"])
            elif row_label == "baseline crosswalk":
                if row["baseline_block_id"] not in baseline_ids:
                    failures.append(
                        f"{path.relative_to(ROOT)} row {number} references unknown "
                        f"baseline_block_id: {row['baseline_block_id']}"
                    )
                key = (row_id, row["attachment_path"], row["baseline_block_id"])
            else:
                if row["playbook_id"] not in playbook_ids:
                    failures.append(
                        f"{path.relative_to(ROOT)} row {number} references unknown "
                        f"playbook_id: {row['playbook_id']}"
                    )
                key = (row_id, row["attachment_path"], row["playbook_id"])

            if key in seen_keys:
                failures.append(
                    f"{path.relative_to(ROOT)} row {number} duplicates {row_label} key: "
                    + " / ".join(key)
                )
            seen_keys.add(key)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate the Stage 3 customer-facing attachment scaffold."
    )
    parser.add_argument(
        "--skip-upload-package-gate",
        action="store_true",
        help=(
            "Skip the Stage 3 GPTs/upload_package cleanliness gate. Use only from "
            "Stage 4+ workflows that intentionally assemble GPTs/upload_package."
        ),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    failures: list[str] = []
    check_attachment_shape(failures)
    check_forbidden_attachment_text(failures)
    if not args.skip_upload_package_gate:
        check_upload_package_clean(failures)
    check_scope_tsv(failures)
    check_completed_scope_exact_tokens(failures)
    check_attachment_crosswalks(failures)

    if failures:
        print("Attachment validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Attachment validation passed.")
    print(f"- Customer-facing attachment files: {len(attachment_files())}")
    print("- Required top-level attachment sections: present")
    print("- Customer-facing path/internal-label scan: passed")
    print("- Altibase 8.1 verified source wording: preserved")
    if args.skip_upload_package_gate:
        print("- GPTs/upload_package Stage 3 and uncommitted-change gate: skipped")
    else:
        print("- GPTs/upload_package Stage 3 and uncommitted-change gate: clean")
    print("- Stage 3 scope TSV routing: valid")
    print("- Completed Stage 3 scope exact-token checks: passed")
    print("- Stage 3 attachment crosswalk routes: valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
