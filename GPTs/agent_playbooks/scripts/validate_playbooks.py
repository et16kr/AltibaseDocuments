#!/usr/bin/env python3
"""Validate the Stage 2 agent playbook and scenario-test scaffold."""

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
SCENARIO_PATH = PLAYBOOK_DIR / "test_scenarios.md"
RUBRIC_PATH = PLAYBOOK_DIR / "scenario_judge_rubric.md"
VALIDATION_REPORT_PATH = PLAYBOOK_DIR / "playbook_validation.md"
SOURCE_MANIFEST = ROOT / "GPTs/source_pack/source_manifest.tsv"
SOURCE_TO_SHARD = ROOT / "GPTs/source_pack/source_to_shard_manifest.tsv"
BASELINE_MANIFEST = ROOT / "GPTs/korean_aligned_english/baseline_manifest.tsv"
AID_TIER_MANIFEST = ROOT / "GPTs/reports/aid_tier_manifest.tsv"
CONFLICT_REGISTER = ROOT / "GPTs/reports/source_conflict_register.md"
GAP_REGISTER = ROOT / "GPTs/reports/agent_playbook_gap_register.md"
SOURCE_PLAYBOOK_CROSSWALK = ROOT / "GPTs/reports/source_pack_to_playbook_crosswalk.tsv"
BASELINE_PLAYBOOK_CROSSWALK = (
    ROOT / "GPTs/reports/korean_aligned_english_to_playbook_crosswalk.tsv"
)
INSTRUCTION_NOTE_PATHS = [
    PLAYBOOK_DIR / "coding_agent_instruction_note.md",
    PLAYBOOK_DIR / "gpt_service_development_instruction_note.md",
]

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

SOURCE_PLAYBOOK_CROSSWALK_COLUMNS = [
    "playbook_id",
    "playbook_path",
    "playbook_title",
    "domain",
    "validation_status",
    "source_id",
    "source_origin",
    "source_path",
    "source_role",
    "source_family",
    "version_scope",
    "authority_label",
    "source_pack_shard_id",
    "source_pack_block_id",
    "source_pack_block_ref",
    "source_pack_validation_status",
    "aid_route_or_tier",
    "aid_tier_ids",
    "korean_aligned_baseline_block_ids",
    "generated_artifact_types",
    "protected_topic",
    "guardrail_ids",
    "remaining_gap_ids",
    "remaining_gap_class",
    "notes",
]

BASELINE_PLAYBOOK_CROSSWALK_COLUMNS = [
    "playbook_id",
    "playbook_path",
    "playbook_title",
    "domain",
    "validation_status",
    "baseline_block_id",
    "baseline_source_type",
    "planned_downstream_use",
    "alignment_status",
    "source_block_refs",
    "source_family",
    "version_scope",
    "authority_label",
    "source_ids",
    "source_pack_block_ids",
    "aid_route_or_tier",
    "aid_tier_ids",
    "generated_artifact_types",
    "protected_topic",
    "guardrail_ids",
    "remaining_gap_ids",
    "remaining_gap_class",
    "notes",
]

NON_PLAYBOOK_MARKDOWN = {
    "README.md",
    "coding_agent_instruction_note.md",
    "gpt_service_development_instruction_note.md",
    "playbook_validation.md",
    "scenario_judge_rubric.md",
    "test_scenarios.md",
}

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

INSTRUCTION_NOTE_REQUIRED_TOKENS = [
    "## Source Routing",
    "## Missing Input Prompts",
    "## Validation",
    "## Stop Conditions",
    "## Forbidden Generic Assumptions",
    "source ID",
    "source-pack block",
    "Korean-aligned",
    "playbook_manifest.tsv",
    "missing input",
    "validation",
    "stop condition",
    "SQL",
    "DDL",
    "DCL",
    "code",
    "commands",
    "configuration",
    "scripts",
    "validation SQL",
    "test",
    "generic database assumptions",
]

REQUIRED_SCENARIOS = {
    "SCN-001": "Minimal Altibase-Backed Service Plan",
    "SCN-002": "Application Connection Code And Configuration",
    "SCN-003": "Disk Tablespace DDL With Validation SQL",
    "SCN-004": "User And Privilege Setup",
    "SCN-005": "GPT Copy/Paste Implementation Artifacts",
    "SCN-006": "ODBC DSN Configuration And Verification",
    "SCN-007": "JDBC Example With Version Caveats",
    "SCN-008": "iSQL Script With Spool And Log Handling",
    "SCN-009": "iLoader Load And Export Workflow",
    "SCN-010": "Safe Property Change",
    "SCN-011": "Exact Error Diagnosis",
    "SCN-012": "Backup And Recovery Check",
    "SCN-013": "Replication Setup Draft",
    "SCN-014": "TLS Client/Server Basics",
    "SCN-015": "Utility Or Migration Workflow",
    "SCN-016": "Positive And Negative SQL Tests",
}

SCENARIO_REQUIRED_FIELDS = [
    "Input Prompt:",
    "Expected Source IDs:",
    "Expected Artifacts:",
    "Applicability:",
    "Required Exact Tokens:",
    "Forbidden Generic Assumptions:",
    "Missing Inputs:",
    "Expected Files/Code/SQL/Commands/Configuration/Tests:",
    "Validation Checks:",
    "Stop Conditions:",
    "Scenario Scoring Rubric:",
    "Pass Threshold:",
    "Pass/Fail Result Placeholder:",
]

RUBRIC_REQUIRED_TOKENS = [
    "Required Source IDs",
    "Required Exact Tokens",
    "Forbidden Generic Assumptions",
    "Missing-Input Prompts",
    "Generated Artifacts",
    "Validation Steps",
    "Stop Conditions",
    "Pass Threshold",
    "Blocker Failures",
    "85/100",
    "source IDs",
    "exact tokens",
    "forbidden generic assumption",
    "missing-input prompts",
    "generated artifacts",
    "validation steps",
    "stop conditions",
    "Oracle",
    "generic JDBC",
    "generic ODBC",
]

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
    "Tools": [
        "iSQL",
        "iLoader",
        "SPOOL",
        "SET QUERYLOGGING",
        "VAR p1 INTEGER",
        "iloader formout",
        "-bad",
        "-log",
        "aexport",
        "run_il_out.sh",
        "run_is.sh",
        "dataCompJ",
        "dataCompJCli.sh",
        "altiComp",
        "dumpdb",
        "dumpla",
        "ALTIBASE_UT_FILE_PERMISSION",
    ],
    "Migration and integrations": [
        "Migration Center",
        "migcenter.sh",
        "register.xml",
        "RunReport4Summary.html",
        "oraAdapter",
        "oaUtility",
        "CREATE REPLICATION",
        "CREATE DATABASE LINK",
        "REMOTE_TABLE",
        "sqoop",
        "com.altibase.sqoop.manager.AltibaseManager",
        "aku -p start",
        "StatefulSet",
        "GEOMETRY",
        "NiFi",
        "force_clob_bind=true",
        "Tableau",
    ],
    "Errors and troubleshooting": [
        "ERR-",
        "altierr",
        "SQLSTATE",
        "exact_error_code",
        "error_symbol",
        "error_message",
        "log_excerpt",
        "altibase_boot.log",
        "altibase_qp.log",
        "altibase_rp.log",
        "altibase_error.log",
        "V$SESSION",
        "V$STATEMENT",
        "V$SQLTEXT",
        "V$SESSION_WAIT",
        "V$LOCK_WAIT",
        "Monitoring API",
        "ABIGetVSession",
        "SNMP",
        "altisnmpd",
        "altiProfile",
        "TIMED_STATISTICS",
        "QUERY_PROF_FLAG",
        "Escalation Stop Points",
    ],
    "Replication and CDC": [
        "CREATE REPLICATION",
        "ALTER REPLICATION",
        "DROP REPLICATION",
        "V$REPSENDER",
        "V$REPRECEIVER",
        "V$REPGAP",
        "Log Analyzer",
        "FOR ANALYSIS",
        "ALA_Handshake",
        "Replication Manager",
        "QUICKSTART",
        "SYNC ONLY",
        "REPLICATION_DDL_SYNC",
        "USING SSL",
        "REPLICATION_SSL_PORT_NO",
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
    "AID, version, release, and patch routing": [
        "AID-000001",
        "AID-000005",
        "AID-000006",
        "AID-000015",
        "AID-000022",
        "AID-SRC-000423",
        "AID-SRC-000438",
        "upload_content_candidate",
        "evidence_only_authority",
        "accepted_limitation",
        "Korean-source-verified",
        "Link-validated Korean-source-verified",
        "English-only source",
        "source_limitation",
        "llm-reference/",
        "Altibase 8.1 verified source",
        "BUG-*",
        "TASK-*",
        "database binary version",
        "meta version",
        "CM protocol version",
        "replication protocol version",
        "global 20 Markdown file",
        "CONF-000004",
        "CONF-000005",
        "CONF-000006",
        "CONF-000007",
        "CONF-000009",
    ],
}

PLAYBOOK_ID_RE = re.compile(r"APB-\d{6}\Z")
SOURCE_ID_RE = re.compile(r"(?:SRC|AID|AID-SRC)-\d{6}\Z")
SOURCE_BLOCK_RE = re.compile(r"BLOCK-\d{6}\Z")
SOURCE_BLOCK_PAIR_RE = re.compile(r"(?:SRC|AID-SRC)-\d{6}/BLOCK-\d{6}\Z")
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
    return source_manifest_ids() | aid_tier_ids()


def source_manifest_ids() -> set[str]:
    return first_column_ids(SOURCE_MANIFEST)


def aid_tier_ids() -> set[str]:
    return first_column_ids(AID_TIER_MANIFEST)


def source_block_refs() -> tuple[set[str], set[str]]:
    rows = read_tsv(SOURCE_TO_SHARD)
    blocks = {row["block_id"] for row in rows if row.get("block_id")}
    pairs = {
        f"{row['source_id']}/{row['block_id']}"
        for row in rows
        if row.get("source_id") and row.get("block_id")
    }
    return blocks, pairs


def source_shard_rows_by_source() -> dict[str, dict[str, str]]:
    return {row["source_id"]: row for row in read_tsv(SOURCE_TO_SHARD)}


def source_manifest_rows_by_id() -> dict[str, dict[str, str]]:
    return {row["source_id"]: row for row in read_tsv(SOURCE_MANIFEST)}


def baseline_rows_by_id() -> dict[str, dict[str, str]]:
    return {row["baseline_block_id"]: row for row in read_tsv(BASELINE_MANIFEST)}


def baseline_block_ids() -> set[str]:
    return first_column_ids(BASELINE_MANIFEST)


def guardrail_ids() -> set[str]:
    text = CONFLICT_REGISTER.read_text(encoding="utf-8")
    return set(re.findall(r"\bCONF-\d{6}\b", text))


def aid_tier_rows_by_id() -> dict[str, dict[str, str]]:
    return {row["aid_source_id"]: row for row in read_tsv(AID_TIER_MANIFEST)}


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


def check_instruction_notes(errors: list[str]) -> None:
    for path in INSTRUCTION_NOTE_PATHS:
        label = rel(path)
        if not path.exists():
            errors.append(f"Required instruction note missing: {label}")
            continue

        text = path.read_text(encoding="utf-8")
        for token in INSTRUCTION_NOTE_REQUIRED_TOKENS:
            if token not in text:
                errors.append(f"{label}: instruction note is missing required token: {token}")

        if "```" not in text:
            errors.append(f"{label}: instruction note must include a fenced structure template")


def check_validation_report(errors: list[str]) -> None:
    label = rel(VALIDATION_REPORT_PATH)
    if not VALIDATION_REPORT_PATH.exists():
        errors.append(f"Required playbook validation report missing: {label}")
        return

    text = VALIDATION_REPORT_PATH.read_text(encoding="utf-8")
    for token in (
        "S2-J012",
        "Verdict:",
        "Source-To-Playbook Crosswalk",
        "Korean-Aligned English-To-Playbook Crosswalk",
        "Required Domains",
        "Gap Register",
        "Self-Review",
    ):
        if token not in text:
            errors.append(f"{label}: validation report missing required token: {token}")


def scenario_sections(text: str) -> dict[str, str]:
    matches = list(re.finditer(r"^### (SCN-\d{3}): .*$", text, re.MULTILINE))
    sections: dict[str, str] = {}
    for index, match in enumerate(matches):
        scenario_id = match.group(1)
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections[scenario_id] = text[start:end]
    return sections


def check_scenarios(errors: list[str]) -> None:
    label = rel(SCENARIO_PATH)
    if not SCENARIO_PATH.exists():
        errors.append(f"Required scenario file missing: {label}")
        return

    text = SCENARIO_PATH.read_text(encoding="utf-8")
    sections = scenario_sections(text)
    known_sources = source_ids()

    for scenario_id, title in REQUIRED_SCENARIOS.items():
        heading = f"### {scenario_id}: {title}"
        section = sections.get(scenario_id)
        if section is None or heading not in section:
            errors.append(f"{label}: missing required scenario heading: {heading}")
            continue

        for field in SCENARIO_REQUIRED_FIELDS:
            if field not in section:
                errors.append(f"{label}: {scenario_id} missing required field: {field}")

        source_refs = re.findall(r"\b(?:SRC|AID|AID-SRC)-\d{6}\b", section)
        if not source_refs:
            errors.append(f"{label}: {scenario_id} must list expected source IDs")
        for source_ref in source_refs:
            if source_ref not in known_sources:
                errors.append(f"{label}: {scenario_id} references unknown source ID: {source_ref}")

        if "85/100 and no blocker" not in section:
            errors.append(f"{label}: {scenario_id} must preserve pass threshold text")
        if "Not run" not in section:
            errors.append(f"{label}: {scenario_id} must include pass/fail placeholder")

    unexpected = sorted(set(sections) - set(REQUIRED_SCENARIOS))
    if unexpected:
        errors.append(f"{label}: unexpected scenario IDs: {'; '.join(unexpected)}")

    lower_text = text.lower()
    for token in (
        "direct GPT",
        "coding-agent",
        "forbidden generic assumptions",
        "missing-input prompts",
        "validation checks",
        "stop conditions",
    ):
        if token.lower() not in lower_text:
            errors.append(f"{label}: scenario suite missing required global token: {token}")


def check_scenario_rubric(errors: list[str]) -> None:
    label = rel(RUBRIC_PATH)
    if not RUBRIC_PATH.exists():
        errors.append(f"Required scenario judge rubric missing: {label}")
        return

    text = RUBRIC_PATH.read_text(encoding="utf-8")
    for token in RUBRIC_REQUIRED_TOKENS:
        if token not in text:
            errors.append(f"{label}: rubric missing required token: {token}")

    if "```" not in text:
        errors.append(f"{label}: rubric must include a fenced result record template")


def check_manifest_source_refs(
    label: str,
    values: list[str],
    known_source_manifest_ids: set[str],
    known_aid_tier_ids: set[str],
    errors: list[str],
) -> None:
    for value in values:
        if not SOURCE_ID_RE.fullmatch(value):
            errors.append(f"{label}: source_ids has invalid reference format: {value}")
            continue

        if value.startswith("AID-") and not value.startswith("AID-SRC-"):
            if value not in known_aid_tier_ids:
                errors.append(f"{label}: source_ids references unknown AID tier ID: {value}")
        elif value not in known_source_manifest_ids:
            errors.append(
                f"{label}: source_ids references ID missing from source_manifest.tsv: {value}"
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

    if row["domain"] == "AID, version, release, and patch routing":
        aid_rows = aid_tier_rows_by_id()
        for source_id in split_semicolon(row["source_ids"]):
            if source_id.startswith("AID-") and not source_id.startswith("AID-SRC-"):
                tier_row = aid_rows.get(source_id)
                if tier_row is None:
                    errors.append(f"{label}: AID tier source is not in aid_tier_manifest: {source_id}")
                    continue
                for field in ("aid_tier", "allowed_downstream_use", "required_label"):
                    value = tier_row[field]
                    if value and value not in text:
                        errors.append(
                            f"{label}: playbook file is missing AID {field} "
                            f"from aid_tier_manifest for {source_id}: {value}"
                        )


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


def check_playbook_files_have_manifest_rows(
    rows: list[dict[str, str]], errors: list[str]
) -> None:
    manifest_paths = {row["path"] for row in rows}
    seen_paths: set[str] = set()
    for row in rows:
        path = row["path"]
        if path in seen_paths:
            errors.append(f"{row['playbook_id']}: duplicate manifest path: {path}")
        seen_paths.add(path)

    for path in sorted(PLAYBOOK_DIR.glob("*.md")):
        if path.name in NON_PLAYBOOK_MARKDOWN:
            continue
        relative = rel(path)
        if relative not in manifest_paths:
            errors.append(f"{relative}: playbook file has no playbook_manifest.tsv row")


def check_gap_register(rows: list[dict[str, str]], errors: list[str]) -> None:
    label = rel(GAP_REGISTER)
    if not GAP_REGISTER.exists():
        errors.append(f"Required playbook gap register missing: {label}")
        return

    text = GAP_REGISTER.read_text(encoding="utf-8")
    for token in (
        "## Not-Ready Blockers",
        "## Accepted Limitations",
        "## Residual Risks",
        "## Downstream Stage 3/4 Work",
        "S2-J012",
        "APG-S2-J012",
    ):
        if token not in text:
            errors.append(f"{label}: gap register missing required token: {token}")

    for row in rows:
        if row["validation_status"] == "planned" or not split_semicolon(row["source_ids"]):
            if row["playbook_id"] not in text:
                errors.append(
                    f"{label}: planned or source-less row is not recorded as a gap: "
                    f"{row['playbook_id']}"
                )

    pass_domains = {row["domain"] for row in rows if row["validation_status"] == "pass"}
    for domain in REQUIRED_DOMAINS:
        if domain not in pass_domains and domain not in text:
            errors.append(
                f"{label}: required domain without a pass row lacks a recorded gap: {domain}"
            )


def aid_tier_refs(row: dict[str, str]) -> list[str]:
    return [
        value
        for value in split_semicolon(row["source_ids"])
        if value.startswith("AID-") and not value.startswith("AID-SRC-")
    ]


def manifest_source_refs(row: dict[str, str]) -> list[str]:
    return [
        value
        for value in split_semicolon(row["source_ids"])
        if value.startswith("SRC-") or value.startswith("AID-SRC-")
    ]


def check_source_playbook_crosswalk(
    rows: list[dict[str, str]], errors: list[str]
) -> int:
    label = rel(SOURCE_PLAYBOOK_CROSSWALK)
    if not SOURCE_PLAYBOOK_CROSSWALK.exists():
        errors.append(f"Required source-to-playbook crosswalk missing: {label}")
        return 0

    try:
        crosswalk_rows = read_tsv(
            SOURCE_PLAYBOOK_CROSSWALK, SOURCE_PLAYBOOK_CROSSWALK_COLUMNS
        )
    except ValueError as exc:
        errors.append(str(exc))
        return 0

    manifest_by_id = {row["playbook_id"]: row for row in rows}
    source_rows = source_manifest_rows_by_id()
    shard_rows = source_shard_rows_by_source()
    expected = {
        (row["playbook_id"], source_id)
        for row in rows
        for source_id in manifest_source_refs(row)
    }
    actual: set[tuple[str, str]] = set()

    for row_number, row in enumerate(crosswalk_rows, start=2):
        row_label = f"{label}:{row_number}"
        manifest_row = manifest_by_id.get(row["playbook_id"])
        if manifest_row is None:
            errors.append(f"{row_label}: unknown playbook_id {row['playbook_id']}")
            continue

        actual.add((row["playbook_id"], row["source_id"]))
        for column in SOURCE_PLAYBOOK_CROSSWALK_COLUMNS:
            if "\t" in row[column] or "\n" in row[column] or "\r" in row[column]:
                errors.append(f"{row_label}: {column} contains forbidden whitespace")

        source_row = source_rows.get(row["source_id"])
        shard_row = shard_rows.get(row["source_id"])
        if source_row is None:
            errors.append(
                f"{row_label}: source_id missing from source_manifest.tsv: {row['source_id']}"
            )
            continue
        if shard_row is None:
            errors.append(
                f"{row_label}: source_id missing from source_to_shard_manifest.tsv: "
                f"{row['source_id']}"
            )
            continue

        expected_ref = f"{row['source_id']}/{shard_row['block_id']}"
        expected_values = {
            "playbook_path": manifest_row["path"],
            "playbook_title": manifest_row["title"],
            "domain": manifest_row["domain"],
            "validation_status": manifest_row["validation_status"],
            "source_origin": source_row["source_origin"],
            "source_path": source_row["source_path"],
            "source_role": source_row["source_role"],
            "source_family": source_row["source_family"],
            "version_scope": source_row["version_scope"],
            "authority_label": source_row["authority_label"],
            "source_pack_shard_id": shard_row["shard_id"],
            "source_pack_block_id": shard_row["block_id"],
            "source_pack_block_ref": expected_ref,
            "source_pack_validation_status": shard_row["validation_status"],
            "aid_route_or_tier": manifest_row["aid_route_or_tier"],
            "aid_tier_ids": ";".join(aid_tier_refs(manifest_row)),
            "korean_aligned_baseline_block_ids": manifest_row[
                "korean_aligned_baseline_block_ids"
            ],
            "generated_artifact_types": manifest_row["generated_artifact_types"],
            "protected_topic": manifest_row["protected_topic"],
            "guardrail_ids": manifest_row["guardrail_ids"],
        }
        for field, expected_value in expected_values.items():
            if row[field] != expected_value:
                errors.append(
                    f"{row_label}: {field}={row[field]!r}, expected {expected_value!r}"
                )

    missing = sorted(expected - actual)
    extra = sorted(actual - expected)
    if missing:
        errors.append(
            f"{label}: missing manifest source routes: "
            + "; ".join(f"{playbook}/{source}" for playbook, source in missing)
        )
    if extra:
        errors.append(
            f"{label}: unexpected source routes: "
            + "; ".join(f"{playbook}/{source}" for playbook, source in extra)
        )

    return len(crosswalk_rows)


def check_baseline_playbook_crosswalk(
    rows: list[dict[str, str]], errors: list[str]
) -> int:
    label = rel(BASELINE_PLAYBOOK_CROSSWALK)
    if not BASELINE_PLAYBOOK_CROSSWALK.exists():
        errors.append(f"Required baseline-to-playbook crosswalk missing: {label}")
        return 0

    try:
        crosswalk_rows = read_tsv(
            BASELINE_PLAYBOOK_CROSSWALK, BASELINE_PLAYBOOK_CROSSWALK_COLUMNS
        )
    except ValueError as exc:
        errors.append(str(exc))
        return 0

    manifest_by_id = {row["playbook_id"]: row for row in rows}
    baseline_rows = baseline_rows_by_id()
    expected = {
        (row["playbook_id"], baseline_id)
        for row in rows
        for baseline_id in split_semicolon(row["korean_aligned_baseline_block_ids"])
    }
    actual: set[tuple[str, str]] = set()

    for row_number, row in enumerate(crosswalk_rows, start=2):
        row_label = f"{label}:{row_number}"
        manifest_row = manifest_by_id.get(row["playbook_id"])
        if manifest_row is None:
            errors.append(f"{row_label}: unknown playbook_id {row['playbook_id']}")
            continue

        actual.add((row["playbook_id"], row["baseline_block_id"]))
        for column in BASELINE_PLAYBOOK_CROSSWALK_COLUMNS:
            if "\t" in row[column] or "\n" in row[column] or "\r" in row[column]:
                errors.append(f"{row_label}: {column} contains forbidden whitespace")

        baseline_row = baseline_rows.get(row["baseline_block_id"])
        if baseline_row is None:
            errors.append(
                f"{row_label}: baseline_block_id missing from baseline_manifest.tsv: "
                f"{row['baseline_block_id']}"
            )
            continue

        expected_values = {
            "playbook_path": manifest_row["path"],
            "playbook_title": manifest_row["title"],
            "domain": manifest_row["domain"],
            "validation_status": manifest_row["validation_status"],
            "baseline_source_type": baseline_row["baseline_source_type"],
            "planned_downstream_use": baseline_row["planned_downstream_use"],
            "alignment_status": baseline_row["alignment_status"],
            "source_block_refs": baseline_row["source_block_refs"],
            "source_family": baseline_row["source_family"],
            "version_scope": baseline_row["version_scope"],
            "authority_label": baseline_row["authority_label"],
            "source_ids": manifest_row["source_ids"],
            "source_pack_block_ids": manifest_row["source_pack_block_ids"],
            "aid_route_or_tier": manifest_row["aid_route_or_tier"],
            "aid_tier_ids": ";".join(aid_tier_refs(manifest_row)),
            "generated_artifact_types": manifest_row["generated_artifact_types"],
            "protected_topic": manifest_row["protected_topic"],
            "guardrail_ids": manifest_row["guardrail_ids"],
        }
        for field, expected_value in expected_values.items():
            if row[field] != expected_value:
                errors.append(
                    f"{row_label}: {field}={row[field]!r}, expected {expected_value!r}"
                )

    missing = sorted(expected - actual)
    extra = sorted(actual - expected)
    if missing:
        errors.append(
            f"{label}: missing manifest baseline routes: "
            + "; ".join(f"{playbook}/{baseline}" for playbook, baseline in missing)
        )
    if extra:
        errors.append(
            f"{label}: unexpected baseline routes: "
            + "; ".join(f"{playbook}/{baseline}" for playbook, baseline in extra)
        )

    return len(crosswalk_rows)


def validate_rows(rows: list[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    known_source_manifest_ids = source_manifest_ids()
    known_aid_tier_ids = aid_tier_ids()
    known_source_blocks, known_source_pairs = source_block_refs()
    known_baseline_blocks = baseline_block_ids()
    known_guardrails = guardrail_ids()

    seen_ids: set[str] = set()
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

        check_manifest_source_refs(
            label,
            split_semicolon(row["source_ids"]),
            known_source_manifest_ids,
            known_aid_tier_ids,
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

    check_playbook_files_have_manifest_rows(rows, errors)

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
        check_gap_register(rows, errors)
        source_crosswalk_count = check_source_playbook_crosswalk(rows, errors)
        baseline_crosswalk_count = check_baseline_playbook_crosswalk(rows, errors)
    else:
        source_crosswalk_count = 0
        baseline_crosswalk_count = 0

    check_instruction_notes(errors)
    check_scenarios(errors)
    check_scenario_rubric(errors)
    check_validation_report(errors)
    check_forbidden_git_edits(errors)

    if errors:
        print("Stage 2 playbook validation: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    planned = sum(1 for row in rows if row["validation_status"] == "planned")
    non_planned = len(rows) - planned
    covered_domains = sorted({row["domain"] for row in rows if row["domain"] in REQUIRED_DOMAINS})
    pass_domains = sorted(
        {
            row["domain"]
            for row in rows
            if row["domain"] in REQUIRED_DOMAINS and row["validation_status"] == "pass"
        }
    )
    gap_text = GAP_REGISTER.read_text(encoding="utf-8") if GAP_REGISTER.exists() else ""
    route_or_gap_domains = sorted(
        set(covered_domains) | {domain for domain in REQUIRED_DOMAINS if domain in gap_text}
    )
    print("Stage 2 playbook validation: PASS")
    print(f"Manifest rows: {len(rows)}")
    print(f"Required domains covered: {len(covered_domains)}/{len(REQUIRED_DOMAINS)}")
    print(
        "Required domains with pass route or recorded gap: "
        f"{len(route_or_gap_domains)}/{len(REQUIRED_DOMAINS)}"
    )
    print(f"Required domains with pass rows: {len(pass_domains)}/{len(REQUIRED_DOMAINS)}")
    print(f"Planned placeholders: {planned}")
    print(f"Non-planned playbooks requiring files: {non_planned}")
    print(f"Source-to-playbook crosswalk rows: {source_crosswalk_count}")
    print(f"Baseline-to-playbook crosswalk rows: {baseline_crosswalk_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
