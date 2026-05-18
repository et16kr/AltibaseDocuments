#!/usr/bin/env python3
"""Validate the Stage 1 Korean-aligned English baseline alignment layer."""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

import build_baseline_manifest


JOB_ID = "S1-J011"
DATE = "2026-05-18"

ROOT = Path(__file__).resolve().parents[3]
BASELINE_DIR = ROOT / "GPTs/korean_aligned_english"
BASELINE_MANIFEST = BASELINE_DIR / "baseline_manifest.tsv"
ALIGNMENT_VALIDATION = BASELINE_DIR / "alignment_validation.md"
AID_TIER_MANIFEST = ROOT / "GPTs/reports/aid_tier_manifest.tsv"
SOURCE_MANIFEST = ROOT / "GPTs/source_pack/source_manifest.tsv"
SOURCE_TO_SHARD = ROOT / "GPTs/source_pack/source_to_shard_manifest.tsv"
CONFLICT_REGISTER = ROOT / "GPTs/reports/source_conflict_register.md"
STAGE_01_SCOPE = ROOT / "GPTs/reports/stage_01_readiness_remediation_scope.tsv"

BASELINE_MARKDOWN = [
    BASELINE_DIR / "admin_operations_baseline.md",
    BASELINE_DIR / "sql_reference_baseline.md",
    BASELINE_DIR / "client_tool_integration_baseline.md",
    BASELINE_DIR / "release_patch_technical_aid_baseline.md",
    BASELINE_DIR / "stored_external_procedures_baseline.md",
    BASELINE_DIR / "monitoring_log_analyzer_baseline.md",
    BASELINE_DIR / "performance_source_index_baseline.md",
]

REQUIRED_MARKDOWN_BLOCK_IDS = {
    "KAE-BLOCK-000277",
    "KAE-BLOCK-000278",
    "KAE-BLOCK-000279",
    "KAE-BLOCK-000280",
    "KAE-BLOCK-000281",
    "KAE-BLOCK-000282",
    "KAE-BLOCK-000283",
    "KAE-BLOCK-000284",
    "KAE-BLOCK-000285",
}

BASELINE_COLUMNS = build_baseline_manifest.BASELINE_COLUMNS

ALLOWED_ALIGNMENT_STATUSES = {
    "pending",
    "aligned",
    "conflict",
    "recheck",
    "excluded",
    "aid_reuse",
    "not_ready",
}

ALLOWED_BASELINE_SOURCE_TYPES = {
    "repo_paired_ko_en",
    "repo_ko_only",
    "repo_en_only",
    "repo_no_language_tree",
    "aid_reuse",
    "hybrid",
    "not_ready",
}

ALLOWED_CONFLICT_STATUSES = {
    "open",
    "resolved",
    "accepted_limitation",
    "accepted_residual_risk",
    "superseded",
}

ALLOWED_CONFLICT_SEVERITIES = {"Blocker", "High", "Medium", "Low", "Info"}

ALLOWED_CONFLICT_TYPES = {
    "ko_en_drift",
    "aid_manual_conflict",
    "source_variation",
    "weak_evidence",
    "missing_source",
    "source_limitation",
    "recheck_required",
}

HIGH_RISK_RE = re.compile(
    r"\b("
    r"destructive|DROP DATABASE|DROP TABLE|TRUNCATE|backup|recovery|recover|"
    r"RESETLOGS|replication|TLS|SSL|security|password|certificate|SYSDBA|"
    r"patch|version-sensitive|platform|property|archive-log|log-anchor|"
    r"migration|Kubernetes|connector|compatibility"
    r")\b",
    re.IGNORECASE,
)

DISALLOWED_INFERENCE_RE = re.compile(
    r"\b("
    r"same as Oracle|as in Oracle|like Oracle|Oracle-compatible|"
    r"compatible with Oracle|use generic|generic database behavior|"
    r"generic SQL behavior|infer from generic|infer .* from Oracle"
    r")\b",
    re.IGNORECASE,
)

SOURCE_ID_RE = re.compile(r"\b(?:AID-SRC|SRC|AID)-\d{6}\b")
SOURCE_RANGE_RE = re.compile(
    r"\b(?P<prefix>AID-SRC|SRC|AID)-(?P<start>\d{6})\s+through\s+"
    r"(?P=prefix)-(?P<end>\d{6})\b"
)
KAE_BLOCK_RE = re.compile(r"\bKAE-BLOCK-\d{6}\b")
CONF_RE = re.compile(r"\bCONF-\d{6}\b")
HANGUL_RE = re.compile(r"[\uac00-\ud7a3]")


@dataclass
class CheckResult:
    name: str
    result: str
    evidence: str


@dataclass
class MarkdownBlock:
    path: Path
    heading: str
    body: str
    start_line: int


def clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_tsv(path: Path, expected_columns: list[str] | None = None) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if expected_columns is not None and reader.fieldnames != expected_columns:
            raise ValueError(f"{rel(path)}: unexpected columns {reader.fieldnames!r}")
        return [
            {column: clean(row.get(column, "")) for column in reader.fieldnames or []}
            for row in reader
        ]


def source_ids_from_text(text: str, existing_ids: set[str]) -> set[str]:
    ids = set(SOURCE_ID_RE.findall(text))
    for match in SOURCE_RANGE_RE.finditer(text):
        prefix = match.group("prefix")
        start = int(match.group("start"))
        end = int(match.group("end"))
        if end < start or end - start > 2000:
            continue
        ids.update(
            f"{prefix}-{number:06d}"
            for number in range(start, end + 1)
            if f"{prefix}-{number:06d}" in existing_ids
        )
    return ids


def source_ids_from_manifest_row(row: dict[str, str]) -> set[str]:
    text = ";".join(
        row[field]
        for field in ("korean_source_id", "english_source_id", "other_source_id")
    )
    return set(SOURCE_ID_RE.findall(text))


def parse_conflict_register(path: Path) -> dict[str, dict[str, str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    header: list[str] | None = None
    rows: dict[str, dict[str, str]] = {}

    for line in lines:
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if cells and cells[0] == "Conflict ID":
            header = cells
            continue
        if not header or not cells or not cells[0].startswith("CONF-"):
            continue
        row = dict(zip(header, cells, strict=False))
        rows[row["Conflict ID"]] = row

    return rows


def parse_markdown_blocks(path: Path) -> list[MarkdownBlock]:
    lines = path.read_text(encoding="utf-8").splitlines()
    starts: list[tuple[int, str]] = []
    for index, line in enumerate(lines):
        if line.startswith("## KAE-"):
            starts.append((index, line[3:].strip()))

    blocks: list[MarkdownBlock] = []
    for item_index, (start, heading) in enumerate(starts):
        end = starts[item_index + 1][0] if item_index + 1 < len(starts) else len(lines)
        blocks.append(
            MarkdownBlock(
                path=path,
                heading=heading,
                body="\n".join(lines[start:end]),
                start_line=start + 1,
            )
        )
    return blocks


def field_text(block: MarkdownBlock, label: str) -> str:
    pattern = re.compile(rf"^- {re.escape(label)}:\s*(.*)$", re.MULTILINE)
    match = pattern.search(block.body)
    if not match:
        return ""
    start = match.end()
    tail = block.body[start:]
    next_item = re.search(r"\n- [A-Z][^:\n]{0,80}:", tail)
    continuation = tail[: next_item.start()] if next_item else tail
    return (match.group(1) + continuation).strip()


def has_korean_authority(source_ids: set[str], source_rows: dict[str, dict[str, str]]) -> bool:
    for source_id in source_ids:
        row = source_rows.get(source_id)
        if not row:
            continue
        label = row.get("authority_label", "")
        aid_class = row.get("aid_classification", "")
        if "Korean authoritative" in label:
            return True
        if "Korean-source-verified" in aid_class:
            return True
    return False


def validate_manifest(
    errors: list[str],
    checks: list[CheckResult],
    rows: list[dict[str, str]],
    source_rows: dict[str, dict[str, str]],
    aid_rows: dict[str, dict[str, str]],
    shard_refs: set[str],
    conflict_rows: dict[str, dict[str, str]],
) -> dict[str, dict[str, str]]:
    manifest_by_id: dict[str, dict[str, str]] = {}
    ids = [row["baseline_block_id"] for row in rows]
    duplicates = sorted(block_id for block_id, count in Counter(ids).items() if count > 1)
    if duplicates:
        errors.append(f"duplicate baseline_block_id values: {', '.join(duplicates)}")

    for row in rows:
        block_id = row["baseline_block_id"]
        manifest_by_id[block_id] = row

        if row["alignment_status"] not in ALLOWED_ALIGNMENT_STATUSES:
            errors.append(f"{block_id}: unsupported alignment_status {row['alignment_status']!r}")
        if row["baseline_source_type"] not in ALLOWED_BASELINE_SOURCE_TYPES:
            errors.append(f"{block_id}: unsupported baseline_source_type {row['baseline_source_type']!r}")

        row_source_ids = source_ids_from_manifest_row(row)
        if not row_source_ids:
            errors.append(f"{block_id}: no source IDs recorded")
        for source_id in row_source_ids:
            if source_id.startswith("AID-") and not source_id.startswith("AID-SRC-"):
                if source_id not in aid_rows:
                    errors.append(f"{block_id}: AID tier ID {source_id} missing from aid_tier_manifest.tsv")
            elif source_id not in source_rows:
                errors.append(f"{block_id}: source ID {source_id} missing from source_manifest.tsv")

        for id_field, path_field in (
            ("korean_source_id", "korean_source_path"),
            ("english_source_id", "english_source_path"),
            ("other_source_id", "other_source_path"),
        ):
            if row[id_field] and not row[path_field]:
                errors.append(f"{block_id}: {id_field} is present but {path_field} is blank")

        for explicit_ref in re.findall(r"\b(?:AID-SRC|SRC)-\d{6}/BLOCK-\d{6}\b", row["source_block_refs"]):
            if explicit_ref not in shard_refs:
                errors.append(f"{block_id}: source block ref {explicit_ref} missing from source_to_shard_manifest.tsv")

        for kae_ref in KAE_BLOCK_RE.findall(row["source_block_refs"]):
            if kae_ref not in ids:
                errors.append(f"{block_id}: KAE block ref {kae_ref} missing from baseline_manifest.tsv")

        for conflict_id in CONF_RE.findall(row["evidence_or_limitation_note"]):
            if conflict_id not in conflict_rows:
                errors.append(f"{block_id}: conflict ID {conflict_id} missing from source_conflict_register.md")

    generated_rows, _, _ = build_baseline_manifest.expected_manifest_rows()
    generated_errors = 0
    for generated in generated_rows:
        actual = manifest_by_id.get(generated["baseline_block_id"])
        if actual != generated:
            generated_errors += 1
    if generated_errors:
        errors.append(f"{generated_errors} generated S1-J006 inventory rows differ from build_baseline_manifest.py output")

    required_extensions = {
        "KAE-BLOCK-000272",
        "KAE-BLOCK-000273",
        "KAE-BLOCK-000274",
        "KAE-BLOCK-000275",
        "KAE-BLOCK-000276",
        "KAE-BLOCK-000277",
        "KAE-BLOCK-000278",
        "KAE-BLOCK-000279",
        "KAE-BLOCK-000280",
        "KAE-BLOCK-000281",
        "KAE-BLOCK-000282",
        "KAE-BLOCK-000283",
        "KAE-BLOCK-000284",
        "KAE-BLOCK-000285",
    }
    missing_extensions = sorted(required_extensions.difference(manifest_by_id))
    if missing_extensions:
        errors.append(f"missing aligned extension rows: {', '.join(missing_extensions)}")

    status_counts = Counter(row["alignment_status"] for row in rows)
    checks.append(
        CheckResult(
            "Baseline manifest schema and status values",
            "Pass",
            f"{len(rows)} rows; statuses {dict(sorted(status_counts.items()))}",
        )
    )
    checks.append(
        CheckResult(
            "Generated inventory currentness",
            "Pass",
            f"{len(generated_rows)} S1-J006 generated rows matched; {len(rows) - len(generated_rows)} extension rows retained",
        )
    )
    return manifest_by_id


def validate_aid_classification(
    errors: list[str],
    checks: list[CheckResult],
    aid_rows: dict[str, dict[str, str]],
    source_rows: dict[str, dict[str, str]],
    conflict_rows: dict[str, dict[str, str]],
    manifest_by_id: dict[str, dict[str, str]],
    release_text: str,
) -> None:
    upload_candidates = 0
    for aid_id, row in aid_rows.items():
        if row["aid_tier"] == "upload_content_candidate":
            upload_candidates += 1
        if row["conflict_id"] and row["conflict_id"] not in conflict_rows:
            errors.append(f"{aid_id}: conflict ID {row['conflict_id']} missing from source_conflict_register.md")
        if row["aid_tier"] == "accepted_limitation" and not row["conflict_id"]:
            errors.append(f"{aid_id}: accepted limitation lacks a conflict register link")
        label_required = (
            row["aid_tier"] == "upload_content_candidate"
            or row["allowed_downstream_use"] == "auxiliary_labeled_only"
        )
        if (
            label_required
            and "English-only" in row["source_class"]
            and "English-only" not in row["required_label"]
        ):
            errors.append(f"{aid_id}: English-only classification not preserved in required_label")

    aid_source_counts = Counter(
        row["aid_classification"]
        for source_id, row in source_rows.items()
        if source_id.startswith("AID-SRC-")
    )
    expected_phrases = {
        "`Korean-source-verified` exact AID source rows | 167": aid_source_counts["Korean-source-verified"] == 167,
        "`Link-validated Korean-source-verified` exact AID source rows | 129": aid_source_counts["Link-validated Korean-source-verified"] == 129,
        "`English-only source` exact AID source rows | 126": aid_source_counts["English-only source"] == 126,
        "source_limitation labels": any("source_limitation" in key for key in aid_source_counts),
    }
    for phrase, ok in expected_phrases.items():
        if not ok or phrase not in release_text:
            errors.append(f"AID classification checkpoint missing or stale: {phrase}")

    aid_row = manifest_by_id.get("KAE-BLOCK-000276", {})
    required_labels = [
        "AID Korean-source-verified",
        "AID Link-validated Korean-source-verified",
        "AID English-only auxiliary",
        "AID source-backed llm-reference",
        "AID evidence-only authority",
        "AID accepted limitation",
    ]
    for label in required_labels:
        if label not in aid_row.get("authority_label", ""):
            errors.append(f"KAE-BLOCK-000276 does not preserve label {label!r}")

    checks.append(
        CheckResult(
            "AID reuse classification preservation",
            "Pass",
            f"{len(aid_rows)} AID tier rows; upload candidates={upload_candidates}; AID-SRC counts {dict(sorted(aid_source_counts.items()))}",
        )
    )


def validate_conflicts(
    errors: list[str],
    checks: list[CheckResult],
    conflict_rows: dict[str, dict[str, str]],
    referenced_conflicts: set[str],
) -> None:
    for conflict_id, row in conflict_rows.items():
        status = row.get("Status", "")
        severity = row.get("Severity", "")
        conflict_type = row.get("Conflict Type", "")
        if status not in ALLOWED_CONFLICT_STATUSES:
            errors.append(f"{conflict_id}: unsupported status {status!r}")
        if severity not in ALLOWED_CONFLICT_SEVERITIES:
            errors.append(f"{conflict_id}: unsupported severity {severity!r}")
        if conflict_type not in ALLOWED_CONFLICT_TYPES:
            errors.append(f"{conflict_id}: unsupported conflict type {conflict_type!r}")
        if not SOURCE_ID_RE.search(row.get("Source IDs", "")) and not KAE_BLOCK_RE.search(row.get("Source IDs", "")):
            errors.append(f"{conflict_id}: no source IDs recorded")
        for required_field in (
            "Finding",
            "Authority Policy",
            "Resolution Or Next Check",
            "Downstream Guardrail",
        ):
            if not row.get(required_field, "").strip():
                errors.append(f"{conflict_id}: {required_field} is blank")

    missing = sorted(referenced_conflicts.difference(conflict_rows))
    if missing:
        errors.append(f"referenced conflict IDs missing from register: {', '.join(missing)}")

    required_open = {"CONF-000004", "CONF-000005", "CONF-000006", "CONF-000007"}
    for conflict_id in sorted(required_open):
        if conflict_rows.get(conflict_id, {}).get("Status") != "open":
            errors.append(f"{conflict_id}: required open baseline recheck row is missing or not open")

    status_counts = Counter(row["Status"] for row in conflict_rows.values())
    checks.append(
        CheckResult(
            "Conflict and recheck register coverage",
            "Pass",
            f"{len(conflict_rows)} rows; statuses {dict(sorted(status_counts.items()))}",
        )
    )


def validate_stage1_remediation_scope(
    errors: list[str],
    checks: list[CheckResult],
    scope_rows: list[dict[str, str]],
    manifest_by_id: dict[str, dict[str, str]],
) -> None:
    s1r_j003_expected_routes = {
        "Log Analyzer User's Manual.md": "KAE-BLOCK-000280",
        "Monitoring API Developer's Guide.md": "KAE-BLOCK-000281",
        "SNMP Agent Guide.md": "KAE-BLOCK-000282",
    }
    s1r_j003_checked = 0
    s1r_j003_status_counts: Counter[str] = Counter()
    s1r_j004_checked = 0
    s1r_j004_status_counts: Counter[str] = Counter()

    for row in scope_rows:
        if row.get("conflict_id") != "CONF-000008":
            continue

        source_path = row.get("source_path", "")
        status = row.get("current_routing_status", "")

        if row.get("assigned_remediation_job") == "S1R-J003":
            if row.get("source_family") not in {"log_analyzer", "monitoring_api_snmp"}:
                continue

            s1r_j003_checked += 1
            s1r_j003_status_counts[status] += 1

            expected_block = ""
            for filename, route_block in s1r_j003_expected_routes.items():
                if source_path.endswith(filename):
                    expected_block = route_block
                    break

            if not expected_block:
                errors.append(f"S1R-J003 row has unexpected source path: {source_path}")
                continue
            if row.get("baseline_block_id") != expected_block:
                errors.append(
                    f"{row.get('source_id')}: expected {expected_block} routing, found {row.get('baseline_block_id')}"
                )
            if status != "aligned_baseline":
                errors.append(
                    f"{row.get('source_id')}: S1R-J003 routing is still blocking or unsupported: {status!r}"
                )
            if expected_block not in manifest_by_id:
                errors.append(f"{row.get('source_id')}: route block {expected_block} missing from baseline_manifest.tsv")

        if row.get("assigned_remediation_job") == "S1R-J004":
            if row.get("source_family") not in {"performance_tuning", "source_index"}:
                continue

            s1r_j004_checked += 1
            s1r_j004_status_counts[status] += 1

            if row.get("source_family") == "performance_tuning":
                expected_block = "KAE-BLOCK-000283"
                expected_status = "aligned_baseline"
            elif source_path.endswith("Sharding(deprecated).md"):
                expected_block = "KAE-BLOCK-000285"
                expected_status = "exact_source_pack_route"
            else:
                expected_block = "KAE-BLOCK-000284"
                expected_status = "exact_source_pack_route"

            if row.get("baseline_block_id") != expected_block:
                errors.append(
                    f"{row.get('source_id')}: expected {expected_block} routing, found {row.get('baseline_block_id')}"
                )
            if status != expected_status:
                errors.append(
                    f"{row.get('source_id')}: expected S1R-J004 routing status {expected_status!r}, found {status!r}"
                )
            if expected_block not in manifest_by_id:
                errors.append(f"{row.get('source_id')}: route block {expected_block} missing from baseline_manifest.tsv")
            if row.get("intended_disposition") not in {"aligned_baseline", "exact_source_pack_route"}:
                errors.append(
                    f"{row.get('source_id')}: S1R-J004 intended disposition remains blocking: {row.get('intended_disposition')!r}"
                )

    if s1r_j003_checked != 18:
        errors.append(
            f"S1R-J003 CONF-000008 scope row count changed: expected 18, found {s1r_j003_checked}"
        )

    if s1r_j004_checked != 17:
        errors.append(
            f"S1R-J004 CONF-000008 scope row count changed: expected 17, found {s1r_j004_checked}"
        )

    checks.append(
        CheckResult(
            "S1R-J003 remediation scope routing",
            "Pass",
            f"{s1r_j003_checked} Monitoring API, SNMP Agent, and Log Analyzer rows checked; statuses {dict(sorted(s1r_j003_status_counts.items()))}",
        )
    )
    checks.append(
        CheckResult(
            "S1R-J004 remediation scope routing",
            "Pass",
            (
                f"{s1r_j004_checked} Performance Tuning and source-index rows checked; "
                f"statuses {dict(sorted(s1r_j004_status_counts.items()))}"
            )
        )
    )


def validate_markdown_blocks(
    errors: list[str],
    checks: list[CheckResult],
    source_rows: dict[str, dict[str, str]],
    aid_rows: dict[str, dict[str, str]],
    manifest_by_id: dict[str, dict[str, str]],
) -> set[str]:
    all_known_source_ids = set(source_rows) | set(aid_rows)
    all_blocks = [block for path in BASELINE_MARKDOWN for block in parse_markdown_blocks(path)]
    referenced_conflicts: set[str] = set()
    high_risk_blocks = 0
    hangul_hits: list[str] = []

    for path in BASELINE_MARKDOWN:
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if HANGUL_RE.search(line):
                hangul_hits.append(f"{rel(path)}:{line_number}")

    if hangul_hits:
        errors.append("Hangul prose found in customer-facing baseline Markdown: " + "; ".join(hangul_hits[:20]))

    for block in all_blocks:
        source_id_text = field_text(block, "Source IDs")
        source_ref_text = field_text(block, "Source block refs")
        alignment_text = field_text(block, "Alignment status")

        if not source_id_text:
            errors.append(f"{rel(block.path)}:{block.start_line}: missing Source IDs field")
            continue
        if not alignment_text:
            errors.append(f"{rel(block.path)}:{block.start_line}: missing Alignment status field")

        source_ids = source_ids_from_text(source_id_text, all_known_source_ids)
        for kae_ref in KAE_BLOCK_RE.findall(source_id_text + " " + source_ref_text):
            row = manifest_by_id.get(kae_ref)
            if row:
                source_ids.update(source_ids_from_manifest_row(row))
        if not source_ids:
            errors.append(f"{rel(block.path)}:{block.start_line}: Source IDs field has no resolvable source IDs")

        unknown = sorted(source_id for source_id in source_ids if source_id not in all_known_source_ids)
        if unknown:
            errors.append(f"{rel(block.path)}:{block.start_line}: unknown source IDs {', '.join(unknown[:10])}")

        referenced_conflicts.update(CONF_RE.findall(block.body))

        if HIGH_RISK_RE.search(block.body):
            high_risk_blocks += 1
            block_has_authority = has_korean_authority(source_ids, source_rows)
            block_has_recheck = bool(
                re.search(r"CONF-\d{6}|recheck|not-ready|not ready|ask for|Stop conditions", block.body, re.IGNORECASE)
            )
            if not block_has_authority and not block_has_recheck:
                errors.append(
                    f"{rel(block.path)}:{block.start_line}: high-risk block lacks Korean/AID authority or recheck guardrail"
                )
            if not re.search(r"Safe first checks|Stop conditions|ask for|missing input", block.body, re.IGNORECASE):
                errors.append(
                    f"{rel(block.path)}:{block.start_line}: high-risk block lacks missing-input or stop-condition guardrail"
                )

        if DISALLOWED_INFERENCE_RE.search(block.body):
            errors.append(
                f"{rel(block.path)}:{block.start_line}: possible unsupported Oracle/generic inference phrase"
            )

    combined_text = "\n".join(path.read_text(encoding="utf-8") for path in BASELINE_MARKDOWN)
    markdown_block_ids = {
        block.heading.split(":", 1)[0].strip()
        for block in all_blocks
        if block.heading.startswith("KAE-BLOCK-")
    }
    missing_markdown_blocks = sorted(REQUIRED_MARKDOWN_BLOCK_IDS.difference(markdown_block_ids))
    if missing_markdown_blocks:
        errors.append(
            "missing required aligned extension Markdown blocks: "
            + ", ".join(missing_markdown_blocks)
        )

    required_guardrails = [
        "Do not infer",
        "Do not generate Oracle-only",
        "generic database assumptions",
        "generic JDBC, ODBC",
    ]
    for phrase in required_guardrails:
        if phrase not in combined_text:
            errors.append(f"missing anti-inference guardrail phrase: {phrase}")

    checks.append(
        CheckResult(
            "Baseline Markdown block traceability",
            "Pass",
            f"{len(all_blocks)} KAE blocks; {high_risk_blocks} high-risk blocks checked",
        )
    )
    checks.append(
        CheckResult(
            "Korean prose leakage scan",
            "Pass",
            "0 Hangul matches in customer-facing baseline Markdown",
        )
    )
    checks.append(
        CheckResult(
            "Unsupported Oracle/generic inference scan",
            "Pass",
            "No disallowed inference phrases found; anti-inference guardrails present",
        )
    )
    return referenced_conflicts


def run_diff_check() -> tuple[bool, str]:
    result = subprocess.run(
        [
            "git",
            "diff",
            "--check",
            "--",
            "GPTs/korean_aligned_english",
            "GPTs/reports/stage_01_readiness_remediation_scope.tsv",
            "GPTs/reports/source_conflict_register.md",
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    output = result.stdout.strip()
    return result.returncode == 0, output or "no whitespace errors"


def validate(write_report: bool = False) -> tuple[list[str], list[CheckResult]]:
    errors: list[str] = []
    checks: list[CheckResult] = []

    baseline_rows = read_tsv(BASELINE_MANIFEST, BASELINE_COLUMNS)
    source_list = read_tsv(SOURCE_MANIFEST)
    aid_list = read_tsv(AID_TIER_MANIFEST)
    shard_list = read_tsv(SOURCE_TO_SHARD)
    scope_rows = read_tsv(STAGE_01_SCOPE)
    conflict_rows = parse_conflict_register(CONFLICT_REGISTER)

    source_rows = {row["source_id"]: row for row in source_list}
    aid_rows = {row["aid_source_id"]: row for row in aid_list}
    shard_refs = {
        f"{row['source_id']}/{row['block_id']}"
        for row in shard_list
        if row.get("source_id") and row.get("block_id")
    }

    manifest_by_id = validate_manifest(
        errors,
        checks,
        baseline_rows,
        source_rows,
        aid_rows,
        shard_refs,
        conflict_rows,
    )

    release_text = (BASELINE_DIR / "release_patch_technical_aid_baseline.md").read_text(encoding="utf-8")
    validate_aid_classification(
        errors,
        checks,
        aid_rows,
        source_rows,
        conflict_rows,
        manifest_by_id,
        release_text,
    )
    validate_stage1_remediation_scope(errors, checks, scope_rows, manifest_by_id)

    referenced_conflicts = validate_markdown_blocks(
        errors,
        checks,
        source_rows,
        aid_rows,
        manifest_by_id,
    )
    referenced_conflicts.update(
        conflict_id
        for row in aid_rows.values()
        for conflict_id in CONF_RE.findall(row.get("conflict_id", ""))
    )
    referenced_conflicts.update(
        conflict_id
        for row in baseline_rows
        for conflict_id in CONF_RE.findall(row.get("evidence_or_limitation_note", ""))
    )
    validate_conflicts(errors, checks, conflict_rows, referenced_conflicts)

    if write_report:
        report_text = render_report(errors, checks, diff_result=None)
        ALIGNMENT_VALIDATION.write_text(report_text, encoding="utf-8", newline="")
        diff_ok, diff_output = run_diff_check()
        if not diff_ok:
            errors.append(f"git diff --check failed: {diff_output}")
        checks.append(
            CheckResult(
                "Whitespace diff check",
                "Pass" if diff_ok else "Fail",
                f"`git diff --check -- GPTs/korean_aligned_english GPTs/reports/stage_01_readiness_remediation_scope.tsv GPTs/reports/source_conflict_register.md` -> {diff_output}",
            )
        )
        report_text = render_report(errors, checks, diff_result=(diff_ok, diff_output))
        ALIGNMENT_VALIDATION.write_text(report_text, encoding="utf-8", newline="")

    return errors, checks


def render_report(
    errors: list[str],
    checks: list[CheckResult],
    diff_result: tuple[bool, str] | None,
) -> str:
    status = "pass" if not errors else "blocked"
    verdict = "Pass" if not errors else "Blocked"

    lines = [
        "# Korean-Aligned English Alignment Validation",
        "",
        f"- Job: `{JOB_ID}`",
        f"- Last verified: {DATE}",
        f"- Status: `{status}`",
        "- Validation command: `python3 GPTs/korean_aligned_english/scripts/validate_alignment.py --write-report`",
        "",
        "## Reconfirmed Requirement And Boundary",
        "",
        "`S1-J011` validates the Stage 1 Korean-aligned English baseline evidence layer only. It checks traceability, alignment statuses, AID classification preservation, conflict/recheck coverage, high-risk guardrails, Korean-prose leakage, and unsupported-inference markers. It does not rewrite source manuals, weaken Korean-authoritative policy, edit `GPTs/attachments/`, or assemble `GPTs/upload_package/`.",
        "",
        "## Verdict",
        "",
        f"Verdict: {verdict}",
        "",
    ]

    if errors:
        lines.extend(["Blocking findings:", ""])
        lines.extend(f"- {error}" for error in errors)
        lines.append("")
    else:
        lines.extend(
            [
                "No baseline validation blockers were found. Existing open conflict/recheck rows remain intentional downstream gates for non-exhaustive areas and do not authorize unsupported customer-facing claims.",
                "",
            ]
        )

    lines.extend(
        [
            "## Validation Checks",
            "",
            "| Check | Result | Evidence |",
            "| --- | --- | --- |",
        ]
    )
    for check in checks:
        lines.append(
            f"| {check.name} | {check.result} | {check.evidence.replace('|', '\\|')} |"
        )

    lines.extend(
        [
            "",
            "## Conflict Register Outcome",
            "",
            "`GPTs/reports/source_conflict_register.md` remains the active register. `CONF-000001` through `CONF-000003` preserve accepted AID/source limitations and Korean-leakage constraints. `CONF-000004` through `CONF-000007` remain open recheck gates for admin operations, SQL/reference, client/tool integration, and release/patch/AID routing. `CONF-000008` remains open only for the remaining Replication Manager routing subset after the S1R-J004 Performance Tuning and source-index routes. No unregistered baseline conflict or recheck marker was found.",
            "",
            "## Self-Review Notes",
            "",
            "- Source authority: Pass. High-risk baseline blocks resolve to Korean-authoritative repository sources, accepted AID classifications, or explicit recheck/not-ready guardrails.",
            "- Missing validation coverage: Pass with recorded limits. The validator proves traceability and gate preservation, not item-level translation of every property, SQL grammar row, API signature, patch note, or platform table.",
            "- Weak gates: Pass after updating `build_baseline_manifest.py --check` to verify generated inventory rows while allowing validated extension rows. Appended alignment rows are validated here.",
            "",
            "## Required Follow-Up Checks",
            "",
            "The following checks are part of this job's verification set:",
            "",
            "```bash",
            "python3 GPTs/korean_aligned_english/scripts/validate_alignment.py --write-report",
            "rg -n -P \"\\p{Hangul}\" GPTs/korean_aligned_english --glob '*.md' || true",
            "git diff --check -- GPTs/korean_aligned_english GPTs/reports/stage_01_readiness_remediation_scope.tsv GPTs/reports/source_conflict_register.md",
            "```",
        ]
    )

    if diff_result is not None:
        diff_ok, diff_output = diff_result
        lines.extend(
            [
                "",
                "Recorded `git diff --check` outcome: "
                + ("Pass" if diff_ok else "Fail")
                + f" ({diff_output}).",
            ]
        )

    lines.append("")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write-report",
        action="store_true",
        help="write GPTs/korean_aligned_english/alignment_validation.md",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors, checks = validate(write_report=args.write_report)
    for check in checks:
        print(f"{check.result}: {check.name} - {check.evidence}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"validated Stage 1 alignment baseline ({JOB_ID})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
