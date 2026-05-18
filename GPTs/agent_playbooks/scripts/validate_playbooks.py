#!/usr/bin/env python3
"""Validate the Stage 2 agent playbook manifest scaffold."""

from __future__ import annotations

import csv
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PLAYBOOK_DIR = ROOT / "GPTs/agent_playbooks"
MANIFEST_PATH = PLAYBOOK_DIR / "playbook_manifest.tsv"
README_PATH = PLAYBOOK_DIR / "README.md"
SOURCE_MANIFEST = ROOT / "GPTs/source_pack/source_manifest.tsv"
SOURCE_TO_SHARD = ROOT / "GPTs/source_pack/source_to_shard_manifest.tsv"
BASELINE_MANIFEST = ROOT / "GPTs/korean_aligned_english/baseline_manifest.tsv"
AID_TIER_MANIFEST = ROOT / "GPTs/reports/aid_tier_manifest.tsv"
CONFLICT_REGISTER = ROOT / "GPTs/reports/source_conflict_register.md"

MANIFEST_COLUMNS = [
    "playbook_id",
    "path",
    "title",
    "domain",
    "supported_versions",
    "source_ids",
    "source_pack_block_ids",
    "korean_aligned_baseline_block_ids",
    "aid_route_or_tier",
    "guardrail_ids",
    "generated_artifact_types",
    "protected_topic",
    "required_missing_input_prompts",
    "validation_status",
    "owning_stage2_job",
    "notes",
]

REQUIRED_DOMAINS = [
    "Installation and startup",
    "DDL generation",
    "SQL and data types",
    "Properties",
    "Dictionary and views",
    "Backup and recovery",
    "Replication and CDC",
    "Security and TLS",
    "ODBC and C clients",
    "Java and JDBC",
    "Tools",
    "Migration and integrations",
    "Errors and troubleshooting",
    "Test generation",
]

ALLOWED_STATUSES = {"planned", "draft", "pass", "fail", "blocked"}
ALLOWED_PROTECTED = {"yes", "no"}
ALLOWED_AID_ROUTES = {
    "not_used_yet",
    "aid_route_when_used",
    "upload_content_candidate_when_used",
    "upload_content_candidate",
    "primary_working_source",
    "auxiliary_labeled_only",
    "evidence_only_authority",
    "authority_check_only",
    "support_evidence_only",
}

REQUIRED_PLAYBOOK_SECTIONS = [
    "## Source Routes",
    "## Required Customer Inputs",
    "## Generated Artifacts",
    "## Guardrails",
    "## Validation Checks",
    "## Stop Conditions",
]

CODE_ARTIFACT_TYPES = {
    "DDL",
    "DCL",
    "DML",
    "SQL",
    "commands",
    "configuration",
    "diagnostics",
    "tests",
    "validation_sql",
    "validation_checks",
}

DOMAIN_REQUIRED_TOKENS = {
    "Installation and startup": [
        "ALTIBASE_HOME",
        "CREATE DATABASE",
        "STARTUP PROCESS",
        "SHUTDOWN NORMAL",
        "SHUTDOWN IMMEDIATE",
        "SHUTDOWN ABORT",
    ],
    "Properties": [
        "V$PROPERTY",
        "ALTER SYSTEM",
        "ALTER SESSION",
        "ADMIN_MODE",
        "LOGANCHOR_DIR",
        "ARCHIVE_DIR",
        "INCREMENTAL_BACKUP_CHUNK_SIZE",
        "altibase.properties",
    ],
    "Backup and recovery": [
        "ARCHIVELOG",
        "NOARCHIVELOG",
        "ALTER DATABASE BACKUP DATABASE",
        "ALTER TABLESPACE",
        "STARTUP CONTROL",
        "RESETLOGS",
        "backupInfo",
    ],
    "Security and TLS": [
        "SSL_ENABLE",
        "SSL_PORT_NO",
        "SSL_CERT",
        "SSL_KEY",
        "SSL_CA",
        "SSL_VERIFY",
        "openssl version",
    ],
    "Java and JDBC": [
        "JDBC",
        "Altibase.jdbc.driver.AltibaseDriver",
        "jdbc:Altibase://",
        "Altibase.jar",
        "Altibase42.jar",
        "Spring",
        "Hibernate",
        "Adapter for JDBC",
    ],
    "ODBC and C clients": [
        "ODBC",
        "CLI",
        "ACI",
        "Precompiler",
        "APRE",
        "SQLAllocHandle",
        "SQLDriverConnect",
        "SQLGetDiagRec",
        "$ALTIBASE_HOME/include/sqlcli.h",
        "libodbccli.a",
        "libapre.a",
    ],
    "Protected administration operations": [
        "DROP DATABASE",
        "DROP TABLESPACE",
        "ALTER DATABASE",
        "ALTER TABLESPACE",
        "ALTER SYSTEM",
        "LOGANCHOR_DIR",
        "ARCHIVE_DIR",
        "ADMIN_MODE",
    ],
}

PLAYBOOK_ID_RE = re.compile(r"APB-\d{6}\Z")
SOURCE_ID_RE = re.compile(r"(?:SRC|AID|AID-SRC)-\d{6}\Z")
SOURCE_BLOCK_RE = re.compile(r"BLOCK-\d{6}\Z")
SOURCE_BLOCK_PAIR_RE = re.compile(r"SRC-\d{6}/BLOCK-\d{6}\Z")
BASELINE_BLOCK_RE = re.compile(r"KAE-BLOCK-\d{6}\Z")
GUARDRAIL_RE = re.compile(r"CONF-\d{6}\Z")
JOB_RE = re.compile(r"S2-J\d{3}\Z")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def split_semicolon(value: str) -> list[str]:
    return [item.strip() for item in value.split(";") if item.strip()]


def read_tsv(path: Path, expected_columns: list[str] | None = None) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if expected_columns is not None and reader.fieldnames != expected_columns:
            raise ValueError(
                f"{rel(path)}: unexpected columns {reader.fieldnames!r}; "
                f"expected {expected_columns!r}"
            )
        return [
            {column: clean(row.get(column, "")) for column in reader.fieldnames or []}
            for row in reader
        ]


def first_column_ids(path: Path) -> set[str]:
    rows = read_tsv(path)
    if not rows:
        return set()
    first = next(iter(rows[0]))
    return {row[first] for row in rows if row.get(first)}


def source_ids() -> set[str]:
    ids = first_column_ids(SOURCE_MANIFEST)
    ids.update(first_column_ids(AID_TIER_MANIFEST))
    return ids


def source_block_refs() -> tuple[set[str], set[str]]:
    rows = read_tsv(SOURCE_TO_SHARD)
    blocks = {row["block_id"] for row in rows if row.get("block_id")}
    pairs = {
        f"{row['source_id']}/{row['block_id']}"
        for row in rows
        if row.get("source_id") and row.get("block_id")
    }
    return blocks, pairs


def baseline_block_ids() -> set[str]:
    return first_column_ids(BASELINE_MANIFEST)


def guardrail_ids() -> set[str]:
    text = CONFLICT_REGISTER.read_text(encoding="utf-8")
    return set(re.findall(r"\bCONF-\d{6}\b", text))


def check_forbidden_git_edits(errors: list[str]) -> None:
    result = subprocess.run(
        ["git", "status", "--short", "--", "GPTs/attachments", "GPTs/upload_package"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        errors.append(
            "Unable to check forbidden path edits with git status: "
            f"{result.stderr.strip() or result.stdout.strip()}"
        )
        return
    dirty = [line for line in result.stdout.splitlines() if line.strip()]
    if dirty:
        errors.append(
            "Forbidden Stage 2 path has uncommitted changes: " + "; ".join(dirty)
        )


def check_path(row: dict[str, str], errors: list[str]) -> None:
    label = row["playbook_id"]
    path_text = row["path"]
    if not path_text:
        errors.append(f"{label}: path is required")
        return
    if path_text.startswith("/") or ".." in Path(path_text).parts:
        errors.append(f"{label}: path must be a repository-relative path without '..'")
    if path_text.startswith("GPTs/attachments/") or path_text.startswith("GPTs/upload_package/"):
        errors.append(f"{label}: path targets forbidden Stage 2 area {path_text}")
    if not path_text.startswith("GPTs/agent_playbooks/"):
        errors.append(f"{label}: path must stay under GPTs/agent_playbooks/")
    if not path_text.endswith(".md"):
        errors.append(f"{label}: path must be a Markdown file")

    full_path = ROOT / path_text
    if row["validation_status"] != "planned" and not full_path.exists():
        errors.append(f"{label}: non-planned playbook path does not exist: {path_text}")


def check_playbook_file(row: dict[str, str], errors: list[str]) -> None:
    """Validate source traceability and shape for completed playbook files."""
    if row["validation_status"] == "planned":
        return

    label = row["playbook_id"]
    full_path = ROOT / row["path"]
    if not full_path.exists():
        return

    text = full_path.read_text(encoding="utf-8")
    required_tokens = [row["playbook_id"], row["title"]]
    required_tokens.extend(REQUIRED_PLAYBOOK_SECTIONS)
    required_tokens.extend(split_semicolon(row["source_ids"]))
    required_tokens.extend(split_semicolon(row["source_pack_block_ids"]))
    required_tokens.extend(split_semicolon(row["korean_aligned_baseline_block_ids"]))
    required_tokens.extend(split_semicolon(row["guardrail_ids"]))

    for token in required_tokens:
        if token and token not in text:
            errors.append(f"{label}: playbook file is missing required token: {token}")

    artifact_types = set(split_semicolon(row["generated_artifact_types"]))
    if artifact_types & CODE_ARTIFACT_TYPES and "```" not in text:
        errors.append(f"{label}: generated code/configuration artifact playbook needs fenced blocks")

    if row["protected_topic"] == "yes":
        lower_text = text.lower()
        if "rollback" not in lower_text and "cleanup" not in lower_text:
            errors.append(f"{label}: protected playbook must mention rollback or cleanup")
        if "stop" not in lower_text:
            errors.append(f"{label}: protected playbook must include stop conditions")

    for token in DOMAIN_REQUIRED_TOKENS.get(row["domain"], []):
        if token not in text:
            errors.append(f"{label}: playbook file is missing domain token: {token}")


def check_known_list(
    label: str,
    field: str,
    values: list[str],
    pattern: re.Pattern[str],
    known: set[str],
    errors: list[str],
) -> None:
    for value in values:
        if not pattern.fullmatch(value):
            errors.append(f"{label}: {field} has invalid reference format: {value}")
        elif value not in known:
            errors.append(f"{label}: {field} references unknown ID: {value}")


def validate_rows(rows: list[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    known_sources = source_ids()
    known_source_blocks, known_source_pairs = source_block_refs()
    known_baseline_blocks = baseline_block_ids()
    known_guardrails = guardrail_ids()

    seen_ids: set[str] = set()
    domains_seen: dict[str, list[str]] = {domain: [] for domain in REQUIRED_DOMAINS}

    for row_number, row in enumerate(rows, start=2):
        label = row.get("playbook_id") or f"row {row_number}"
        for column in MANIFEST_COLUMNS:
            if "\t" in row[column] or "\n" in row[column] or "\r" in row[column]:
                errors.append(f"{label}: {column} contains forbidden whitespace")

        playbook_id = row["playbook_id"]
        if not PLAYBOOK_ID_RE.fullmatch(playbook_id):
            errors.append(f"{label}: playbook_id must match APB-000000")
        elif playbook_id in seen_ids:
            errors.append(f"{label}: duplicate playbook_id")
        seen_ids.add(playbook_id)

        if row["validation_status"] not in ALLOWED_STATUSES:
            errors.append(f"{label}: validation_status must be one of {sorted(ALLOWED_STATUSES)}")
        if row["protected_topic"] not in ALLOWED_PROTECTED:
            errors.append(f"{label}: protected_topic must be yes or no")
        if not JOB_RE.fullmatch(row["owning_stage2_job"]):
            errors.append(f"{label}: owning_stage2_job must match S2-J000")
        if not row["title"]:
            errors.append(f"{label}: title is required")
        if not row["domain"]:
            errors.append(f"{label}: domain is required")
        if not row["supported_versions"]:
            errors.append(f"{label}: supported_versions is required")
        if not split_semicolon(row["generated_artifact_types"]):
            errors.append(f"{label}: generated_artifact_types is required")
        if not split_semicolon(row["required_missing_input_prompts"]):
            errors.append(f"{label}: required_missing_input_prompts is required")

        check_path(row, errors)
        check_playbook_file(row, errors)

        if row["domain"] in domains_seen:
            domains_seen[row["domain"]].append(playbook_id)

        check_known_list(
            label,
            "source_ids",
            split_semicolon(row["source_ids"]),
            SOURCE_ID_RE,
            known_sources,
            errors,
        )

        for value in split_semicolon(row["source_pack_block_ids"]):
            if SOURCE_BLOCK_PAIR_RE.fullmatch(value):
                if value not in known_source_pairs:
                    errors.append(f"{label}: source_pack_block_ids references unknown pair: {value}")
            elif SOURCE_BLOCK_RE.fullmatch(value):
                if value not in known_source_blocks:
                    errors.append(f"{label}: source_pack_block_ids references unknown block: {value}")
            else:
                errors.append(f"{label}: source_pack_block_ids has invalid reference format: {value}")

        check_known_list(
            label,
            "korean_aligned_baseline_block_ids",
            split_semicolon(row["korean_aligned_baseline_block_ids"]),
            BASELINE_BLOCK_RE,
            known_baseline_blocks,
            errors,
        )
        check_known_list(
            label,
            "guardrail_ids",
            split_semicolon(row["guardrail_ids"]),
            GUARDRAIL_RE,
            known_guardrails,
            errors,
        )

        aid_route = row["aid_route_or_tier"]
        if aid_route and aid_route not in ALLOWED_AID_ROUTES:
            errors.append(f"{label}: aid_route_or_tier is not an allowed scaffold route: {aid_route}")

        if row["validation_status"] == "pass":
            if not split_semicolon(row["source_ids"]):
                errors.append(f"{label}: pass rows must cite source_ids")
            if not (
                split_semicolon(row["source_pack_block_ids"])
                or split_semicolon(row["korean_aligned_baseline_block_ids"])
            ):
                errors.append(
                    f"{label}: pass rows must cite source-pack or Korean-aligned baseline blocks"
                )

    missing_domains = [domain for domain, ids in domains_seen.items() if not ids]
    if missing_domains:
        errors.append("Missing required domain placeholders: " + "; ".join(missing_domains))

    return errors


def main() -> int:
    errors: list[str] = []

    for path in (PLAYBOOK_DIR, README_PATH, MANIFEST_PATH):
        if not path.exists():
            errors.append(f"Required scaffold path missing: {rel(path)}")

    rows: list[dict[str, str]] = []
    if MANIFEST_PATH.exists():
        try:
            rows = read_tsv(MANIFEST_PATH, MANIFEST_COLUMNS)
        except ValueError as exc:
            errors.append(str(exc))

    if rows:
        errors.extend(validate_rows(rows))

    check_forbidden_git_edits(errors)

    if errors:
        print("Stage 2 playbook validation: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    planned = sum(1 for row in rows if row["validation_status"] == "planned")
    non_planned = len(rows) - planned
    covered_domains = sorted({row["domain"] for row in rows if row["domain"] in REQUIRED_DOMAINS})
    print("Stage 2 playbook validation: PASS")
    print(f"Manifest rows: {len(rows)}")
    print(f"Required domains covered: {len(covered_domains)}/{len(REQUIRED_DOMAINS)}")
    print(f"Planned placeholders: {planned}")
    print(f"Non-planned playbooks requiring files: {non_planned}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
