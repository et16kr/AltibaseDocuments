#!/usr/bin/env python3
"""Utilities for the Altibase GPT full coverage audit catalog.

The tools are intentionally conservative. They validate the machine-checkable
TSV contract, provide extraction aids, and can initialize the source-to-attachment
matrix from already reviewed catalog rows. Catalog jobs remain responsible for
source-backed judgment.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[4]
AUDIT_DIR = REPO_ROOT / "GPTs" / "reports" / "full_coverage_audit"
DEFAULT_CATALOG = AUDIT_DIR / "source_item_catalog.tsv"
DEFAULT_MATRIX = AUDIT_DIR / "source_to_attachment_matrix.tsv"

SOURCE_FAMILIES = {
    "release_notes_platform",
    "patch_notes",
    "getting_started_installation",
    "administrator_operations",
    "sql_reference",
    "general_reference_1_datatypes_properties",
    "general_reference_2_dictionary_views",
    "error_message_reference",
    "performance_tuning",
    "monitoring_api_snmp",
    "replication_manual",
    "log_analyzer",
    "replication_manager",
    "security_ssl_tls",
    "stored_external_procedures",
    "jdbc_java",
    "c_cli_odbc_precompiler",
    "isql_iloader",
    "utilities_datacompj",
    "migration_oracle",
    "dblink_hadoop_external_connectors",
    "kubernetes_aku",
    "spatial_nifi_tableau",
    "technical_documents_support",
    "third_party_guides",
}

VERSION_SCOPES = {"7.1", "7.3", "8.1", "cross-version", "patch-specific"}

COVERAGE_STATUSES = {
    "Covered",
    "Covered-by-routing",
    "Guardrail",
    "Out-of-scope",
    "Missing",
    "Retrieval-weak",
}

ITEM_TYPES = {
    "property",
    "SQL syntax",
    "command option",
    "view",
    "column",
    "error code",
    "API",
    "runbook step",
    "compatibility rule",
    "version note",
    "warning",
    "example",
    "data type",
    "function",
    "tool command",
    "connector setting",
    "release note",
    "platform rule",
    "other documented category",
}

CATALOG_REQUIRED_COLUMNS = [
    "source_item_id",
    "source_family",
    "version_scope",
    "source_path",
    "source_heading",
    "item_type",
    "literal_tokens",
    "source_summary",
    "attachment_target",
    "coverage_status",
    "attachment_anchor",
    "guardrail_reason",
    "audit_job",
    "evidence",
]

MATRIX_REQUIRED_COLUMNS = [
    "source_item_id",
    "source_family",
    "version_scope",
    "source_path",
    "source_heading",
    "item_type",
    "attachment_target",
    "coverage_status",
    "attachment_anchor",
    "routing_aliases",
    "matrix_notes",
    "guardrail_reason",
    "audit_job",
    "evidence",
]

REGISTER_FILES = [
    "missing_item_register.md",
    "guardrail_register.md",
    "retrieval_weakness_register.md",
    "remediation_log.md",
    "final_full_coverage_audit.md",
]

ATTACHMENTS = {
    str(path.relative_to(REPO_ROOT))
    for path in (REPO_ROOT / "GPTs" / "attachments").glob("*.md")
    if path.name != "README.md"
}

ATTACHMENT_ALIAS_TERMS = {
    "GPTs/attachments/00_version_release_platform.md": [
        "release notes",
        "patch notes",
        "supported platforms",
        "upgrade risk",
        "Altibase 8.1 verified source",
    ],
    "GPTs/attachments/01_getting_started_installation.md": [
        "install",
        "startup",
        "shutdown",
        "database creation",
        "first checks",
    ],
    "GPTs/attachments/02_administration_operations.md": [
        "backup",
        "recovery",
        "tablespaces",
        "accounts",
        "privileges",
    ],
    "GPTs/attachments/03_sql_ddl_generation.md": [
        "DDL",
        "DCL",
        "tablespace SQL",
        "replication SQL",
        "destructive SQL",
    ],
    "GPTs/attachments/04_sql_dml_oracle_compatibility.md": [
        "DML",
        "functions",
        "predicates",
        "Oracle compatibility",
        "JSON SQL",
    ],
    "GPTs/attachments/05_data_types_properties.md": [
        "data types",
        "properties",
        "property defaults",
        "ALTER SYSTEM",
        "V$PROPERTY",
    ],
    "GPTs/attachments/06_data_dictionary_performance_views.md": [
        "dictionary",
        "performance views",
        "view columns",
        "metadata checks",
        "V$",
    ],
    "GPTs/attachments/07_error_messages_troubleshooting.md": [
        "error codes",
        "altierr",
        "SQLCODE",
        "cause action",
        "troubleshooting",
    ],
    "GPTs/attachments/08_performance_tuning_monitoring.md": [
        "performance tuning",
        "execution plan",
        "hints",
        "statistics",
        "Monitoring API",
    ],
    "GPTs/attachments/09_replication_ha_cdc.md": [
        "replication",
        "CDC",
        "Log Analyzer",
        "RepMgr",
        "replication state",
    ],
    "GPTs/attachments/10_psm_stored_external_procedures.md": [
        "PSM",
        "stored procedures",
        "packages",
        "triggers",
        "external procedures",
    ],
    "GPTs/attachments/11_java_jdbc_spring.md": [
        "JDBC",
        "Java compatibility",
        "Spring",
        "Hibernate",
        "Adapter for JDBC",
    ],
    "GPTs/attachments/12_c_cli_odbc_precompiler.md": [
        "CLI",
        "ODBC",
        "Altibase C Interface",
        "APRE",
        "diagnostics",
    ],
    "GPTs/attachments/13_isql_iloader_basic_tools.md": [
        "iSQL",
        "iLoader",
        "host variables",
        "FORM files",
        "load export",
    ],
    "GPTs/attachments/14_utilities_operation_tools.md": [
        "utilities",
        "dataCompJ",
        "aexport",
        "altiComp",
        "dump tools",
    ],
    "GPTs/attachments/15_migration_oracle_compatibility.md": [
        "Migration Center",
        "Adapter for Oracle",
        "Oracle conversion",
        "migration validation",
        "oraAdapter",
    ],
    "GPTs/attachments/16_dblink_external_connectors.md": [
        "DB Link",
        "AltiLinker",
        "Hadoop Connector",
        "DBeaver",
        "external connectors",
    ],
    "GPTs/attachments/17_kubernetes_aku_cloud.md": [
        "Kubernetes",
        "AKU",
        "container",
        "Pod",
        "StatefulSet",
    ],
    "GPTs/attachments/18_security_ssl_tls.md": [
        "SSL",
        "TLS",
        "certificates",
        "FIPS",
        "replication SSL",
    ],
    "GPTs/attachments/19_spatial_nifi_tableau_misc.md": [
        "Spatial",
        "GEOMETRY",
        "altiShapeLoader",
        "NiFi",
        "Tableau",
    ],
    "N/A": ["out-of-scope", "source boundary", "selected corpus"],
}

ITEM_TYPE_ALIAS_TERMS = {
    "property": ["default", "range", "dynamic change", "restart", "check SQL"],
    "SQL syntax": ["syntax", "BNF", "privileges", "examples", "validation SQL"],
    "command option": ["command option", "tool option", "help output"],
    "view": ["view purpose", "key columns", "query timing", "check SQL"],
    "column": ["column name", "installed metadata", "patch-sensitive columns"],
    "error code": ["error code", "symbol", "message", "cause", "action"],
    "API": ["API", "call order", "arguments", "return code", "diagnostics"],
    "runbook step": ["prerequisites", "commands", "stop conditions", "validation"],
    "compatibility rule": ["compatibility", "version boundary", "unsupported behavior"],
    "version note": ["version note", "patch boundary", "release note"],
    "warning": ["caution", "missing input", "safest next check"],
    "example": ["example", "expected output", "validation"],
    "data type": ["data type", "limits", "conversion", "LOB", "JSON"],
    "function": ["function", "arguments", "return value", "examples"],
    "tool command": ["tool command", "options", "output", "diagnostics"],
    "connector setting": ["connector", "driver", "configuration", "runtime checks"],
    "release note": ["release note", "BUG token", "changed behavior"],
    "platform rule": ["platform", "OS", "hardware", "JDK", "support boundary"],
    "other documented category": ["documented item", "source-backed", "answer block"],
}

SOURCE_ID_RE = re.compile(
    r"^SRC-[A-Z0-9]+-(?:7\.1|7\.3|8\.1|XVER|PATCH)-[0-9]{6}$"
)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
BACKTICK_RE = re.compile(r"`([^`]+)`")
TOKEN_RE = re.compile(r"\b(?:[A-Z][A-Z0-9_$#]{2,}|V\$[A-Z0-9_]+|X\$[A-Z0-9_]+)\b")


class CheckError(Exception):
    pass


def repo_relative(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def read_tsv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    if not path.exists():
        raise CheckError(f"missing TSV: {repo_relative(path)}")
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames is None:
            raise CheckError(f"empty TSV with no header: {repo_relative(path)}")
        rows = [dict(row) for row in reader]
    return list(reader.fieldnames), rows


def require_columns(path: Path, fieldnames: list[str], required: list[str]) -> None:
    missing = [column for column in required if column not in fieldnames]
    if missing:
        raise CheckError(
            f"{repo_relative(path)} missing required columns: {', '.join(missing)}"
        )


def require_exact_columns(path: Path, fieldnames: list[str], required: list[str]) -> None:
    if fieldnames != required:
        raise CheckError(
            f"{repo_relative(path)} has non-canonical column order: "
            f"{', '.join(fieldnames)}"
        )


def validate_repo_path(value: str, field: str, path: Path, row_number: int) -> None:
    if not value:
        return
    if value.startswith("/") or "\\" in value or value.startswith("../"):
        raise CheckError(
            f"{repo_relative(path)} row {row_number}: {field} must be repository-relative"
        )


def validate_attachment(value: str, status: str, path: Path, row_number: int) -> None:
    if status == "Out-of-scope" and value in {"", "N/A"}:
        return
    if value not in ATTACHMENTS:
        raise CheckError(
            f"{repo_relative(path)} row {row_number}: attachment_target must be one "
            f"of GPTs/attachments/*.md or N/A for Out-of-scope"
        )


def validate_catalog(path: Path) -> list[dict[str, str]]:
    fieldnames, rows = read_tsv(path)
    require_columns(path, fieldnames, CATALOG_REQUIRED_COLUMNS)
    seen: set[str] = set()
    for index, row in enumerate(rows, start=2):
        source_item_id = row["source_item_id"]
        if not SOURCE_ID_RE.match(source_item_id):
            raise CheckError(
                f"{repo_relative(path)} row {index}: invalid source_item_id {source_item_id!r}"
            )
        if source_item_id in seen:
            raise CheckError(
                f"{repo_relative(path)} row {index}: duplicate source_item_id {source_item_id}"
            )
        seen.add(source_item_id)

        if row["source_family"] not in SOURCE_FAMILIES:
            raise CheckError(
                f"{repo_relative(path)} row {index}: invalid source_family "
                f"{row['source_family']!r}"
            )
        if row["version_scope"] not in VERSION_SCOPES:
            raise CheckError(
                f"{repo_relative(path)} row {index}: invalid version_scope "
                f"{row['version_scope']!r}"
            )
        if row["item_type"] not in ITEM_TYPES:
            raise CheckError(
                f"{repo_relative(path)} row {index}: invalid item_type {row['item_type']!r}"
            )
        status = row["coverage_status"]
        if status not in COVERAGE_STATUSES:
            raise CheckError(
                f"{repo_relative(path)} row {index}: invalid coverage_status {status!r}"
            )
        for field in ("source_path", "source_summary", "audit_job", "evidence"):
            if not row[field].strip():
                raise CheckError(
                    f"{repo_relative(path)} row {index}: {field} is required"
                )
        validate_repo_path(row["source_path"], "source_path", path, index)
        validate_attachment(row["attachment_target"], status, path, index)
        if status in {"Guardrail", "Out-of-scope"} and not row["guardrail_reason"].strip():
            raise CheckError(
                f"{repo_relative(path)} row {index}: guardrail_reason is required "
                f"for {status}"
            )
    return rows


def validate_matrix(path: Path, catalog_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    fieldnames, rows = read_tsv(path)
    require_columns(path, fieldnames, MATRIX_REQUIRED_COLUMNS)
    catalog_ids = {row["source_item_id"] for row in catalog_rows}
    seen_pairs: set[tuple[str, str]] = set()
    for index, row in enumerate(rows, start=2):
        source_item_id = row["source_item_id"]
        if not SOURCE_ID_RE.match(source_item_id):
            raise CheckError(
                f"{repo_relative(path)} row {index}: invalid source_item_id {source_item_id!r}"
            )
        if catalog_ids and source_item_id not in catalog_ids:
            raise CheckError(
                f"{repo_relative(path)} row {index}: source_item_id {source_item_id} "
                f"is not in source_item_catalog.tsv"
            )
        pair = (source_item_id, row["attachment_target"])
        if pair in seen_pairs:
            raise CheckError(
                f"{repo_relative(path)} row {index}: duplicate source_item_id/"
                f"attachment_target pair {pair}"
            )
        seen_pairs.add(pair)
        if row["source_family"] not in SOURCE_FAMILIES:
            raise CheckError(
                f"{repo_relative(path)} row {index}: invalid source_family "
                f"{row['source_family']!r}"
            )
        if row["version_scope"] not in VERSION_SCOPES:
            raise CheckError(
                f"{repo_relative(path)} row {index}: invalid version_scope "
                f"{row['version_scope']!r}"
            )
        if row["item_type"] not in ITEM_TYPES:
            raise CheckError(
                f"{repo_relative(path)} row {index}: invalid item_type {row['item_type']!r}"
            )
        status = row["coverage_status"]
        if status not in COVERAGE_STATUSES:
            raise CheckError(
                f"{repo_relative(path)} row {index}: invalid coverage_status {status!r}"
            )
        for field in ("source_path", "audit_job", "evidence"):
            if not row[field].strip():
                raise CheckError(
                    f"{repo_relative(path)} row {index}: {field} is required"
                )
        validate_repo_path(row["source_path"], "source_path", path, index)
        validate_attachment(row["attachment_target"], status, path, index)
        if status in {"Guardrail", "Out-of-scope"} and not row["guardrail_reason"].strip():
            raise CheckError(
                f"{repo_relative(path)} row {index}: guardrail_reason is required "
                f"for {status}"
            )
    return rows


def cmd_check(args: argparse.Namespace) -> int:
    catalog_path = Path(args.catalog)
    matrix_path = Path(args.matrix)
    catalog_rows = validate_catalog(catalog_path)
    matrix_rows = validate_matrix(matrix_path, catalog_rows)
    if args.require_registers:
        for name in REGISTER_FILES:
            path = AUDIT_DIR / name
            if not path.exists():
                raise CheckError(f"missing audit register/report: {repo_relative(path)}")
    print(
        "OK: validated "
        f"{repo_relative(catalog_path)} ({len(catalog_rows)} rows) and "
        f"{repo_relative(matrix_path)} ({len(matrix_rows)} rows)"
    )
    return 0


def version_scope_from_id(source_item_id: str) -> str:
    version_code = source_item_id.split("-")[2]
    if version_code == "XVER":
        return "cross-version"
    if version_code == "PATCH":
        return "patch-specific"
    return version_code


def count_by(rows: list[dict[str, str]], field: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in rows:
        value = row[field]
        counts[value] = counts.get(value, 0) + 1
    return dict(sorted(counts.items()))


def clean_cell(value: str) -> str:
    return " ".join((value or "").replace("\t", " ").split())


def split_literal_tokens(value: str, limit: int = 12) -> list[str]:
    tokens = []
    for raw in (value or "").split(";"):
        token = clean_cell(raw)
        if token and token not in tokens:
            tokens.append(token)
        if len(tokens) >= limit:
            break
    return tokens


def append_unique(values: list[str], additions: list[str]) -> None:
    seen = {value.lower(): value for value in values}
    for value in additions:
        value = clean_cell(value)
        if not value:
            continue
        key = value.lower()
        if key not in seen:
            seen[key] = value
            values.append(value)


def matrix_routing_aliases(row: dict[str, str]) -> str:
    aliases: list[str] = []
    append_unique(aliases, [row["source_family"].replace("_", " "), row["item_type"]])
    append_unique(aliases, ATTACHMENT_ALIAS_TERMS.get(row["attachment_target"], []))
    append_unique(aliases, ITEM_TYPE_ALIAS_TERMS.get(row["item_type"], []))
    append_unique(aliases, split_literal_tokens(row.get("literal_tokens", "")))
    return "; ".join(aliases)


def matrix_status_note(row: dict[str, str]) -> str:
    status = row["coverage_status"]
    status_notes = {
        "Covered": (
            "Catalog maps this item to an answer-ready attachment block; preserve exact "
            "literal tokens and version scope during later edits."
        ),
        "Covered-by-routing": (
            "Catalog maps this item through attachment routing, cross-reference, alias, "
            "or index coverage; strengthen routing if later lexical checks miss it."
        ),
        "Guardrail": (
            "Guardrail row; a definitive customer answer requires the recorded missing "
            "input or safest next check."
        ),
        "Out-of-scope": (
            "Outside the locked selected upload corpus; do not add customer-facing "
            "coverage unless the corpus boundary changes."
        ),
        "Missing": (
            "Unresolved source-backed attachment gap; target attachment needs an "
            "answer-ready block before final audit closure."
        ),
        "Retrieval-weak": (
            "Represented but retrieval-weak; add or strengthen aliases, headings, "
            "indexes, or cross-links before final audit closure."
        ),
    }
    summary = clean_cell(row.get("source_summary", ""))
    if len(summary) > 220:
        summary = summary[:217].rstrip() + "..."
    return f"{status_notes[status]} Source summary: {summary}"


def matrix_evidence(row: dict[str, str], audit_job: str) -> str:
    command = (
        "python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py "
        f"build-matrix --audit-job {audit_job}"
    )
    return clean_cell(f"matrix build: {command}; catalog evidence: {row['evidence']}")


def build_matrix_rows(
    catalog_rows: list[dict[str, str]], audit_job: str
) -> list[dict[str, str]]:
    matrix_rows: list[dict[str, str]] = []
    for row in catalog_rows:
        matrix_row = {
            "source_item_id": row["source_item_id"],
            "source_family": row["source_family"],
            "version_scope": row["version_scope"],
            "source_path": row["source_path"],
            "source_heading": row["source_heading"],
            "item_type": row["item_type"],
            "attachment_target": row["attachment_target"],
            "coverage_status": row["coverage_status"],
            "attachment_anchor": row["attachment_anchor"],
            "routing_aliases": matrix_routing_aliases(row),
            "matrix_notes": matrix_status_note(row),
            "guardrail_reason": row["guardrail_reason"],
            "audit_job": audit_job,
            "evidence": matrix_evidence(row, audit_job),
        }
        matrix_rows.append(
            {field: clean_cell(matrix_row[field]) for field in MATRIX_REQUIRED_COLUMNS}
        )
    return matrix_rows


def write_tsv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            delimiter="\t",
            fieldnames=fieldnames,
            lineterminator="\n",
            extrasaction="raise",
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def cmd_build_matrix(args: argparse.Namespace) -> int:
    catalog_path = Path(args.catalog)
    matrix_path = Path(args.matrix)
    catalog_rows = validate_catalog(catalog_path)
    _, existing_rows = read_tsv(matrix_path)
    if existing_rows and not args.force:
        raise CheckError(
            f"{repo_relative(matrix_path)} already has {len(existing_rows)} rows; "
            "rerun with --force only when intentionally rebuilding the whole matrix"
        )
    matrix_rows = build_matrix_rows(catalog_rows, args.audit_job)
    write_tsv(matrix_path, MATRIX_REQUIRED_COLUMNS, matrix_rows)
    print(
        f"OK: wrote {len(matrix_rows)} matrix rows to {repo_relative(matrix_path)} "
        f"from {len(catalog_rows)} catalog rows"
    )
    return 0


def check_matrix_qa(
    catalog_path: Path, matrix_path: Path
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    catalog_fieldnames, catalog_rows = read_tsv(catalog_path)
    matrix_fieldnames, matrix_rows = read_tsv(matrix_path)
    require_exact_columns(catalog_path, catalog_fieldnames, CATALOG_REQUIRED_COLUMNS)
    require_exact_columns(matrix_path, matrix_fieldnames, MATRIX_REQUIRED_COLUMNS)

    catalog_rows = validate_catalog(catalog_path)
    matrix_rows = validate_matrix(matrix_path, catalog_rows)
    if not matrix_rows:
        raise CheckError(f"{repo_relative(matrix_path)} has no matrix rows")

    catalog_by_id = {row["source_item_id"]: row for row in catalog_rows}
    matrix_by_pair = {
        (row["source_item_id"], row["attachment_target"]): row for row in matrix_rows
    }
    missing_ids = sorted(
        source_item_id
        for source_item_id in catalog_by_id
        if not any(row["source_item_id"] == source_item_id for row in matrix_rows)
    )
    if missing_ids:
        raise CheckError(
            "matrix is missing catalog source_item_id rows: "
            + ", ".join(missing_ids[:20])
            + (" ..." if len(missing_ids) > 20 else "")
        )

    for catalog_row in catalog_rows:
        key = (catalog_row["source_item_id"], catalog_row["attachment_target"])
        matrix_row = matrix_by_pair.get(key)
        if not matrix_row:
            raise CheckError(
                "matrix is missing the catalog attachment mapping for "
                f"{catalog_row['source_item_id']} -> {catalog_row['attachment_target']}"
            )
        for field in (
            "source_family",
            "version_scope",
            "source_path",
            "source_heading",
            "item_type",
            "coverage_status",
            "attachment_anchor",
            "guardrail_reason",
        ):
            if clean_cell(matrix_row[field]) != clean_cell(catalog_row[field]):
                raise CheckError(
                    f"matrix field mismatch for {catalog_row['source_item_id']} "
                    f"field {field}: {matrix_row[field]!r} != {catalog_row[field]!r}"
                )
        for field in ("routing_aliases", "matrix_notes", "audit_job", "evidence"):
            if not matrix_row[field].strip():
                raise CheckError(
                    f"matrix row {catalog_row['source_item_id']} has empty {field}"
                )
        if (
            matrix_row["coverage_status"] in {"Covered-by-routing", "Retrieval-weak"}
            and "alias" not in matrix_row["matrix_notes"].lower()
            and "routing" not in matrix_row["matrix_notes"].lower()
        ):
            raise CheckError(
                f"matrix row {catalog_row['source_item_id']} lacks retrieval/routing note"
            )

    return catalog_rows, matrix_rows


def cmd_matrix_qa(args: argparse.Namespace) -> int:
    catalog_rows, matrix_rows = check_matrix_qa(Path(args.catalog), Path(args.matrix))
    print("OK: matrix QA passed")
    print(f"Catalog rows: {len(catalog_rows)}")
    print(f"Matrix rows: {len(matrix_rows)}")
    print("Coverage statuses:")
    for status, count in count_by(matrix_rows, "coverage_status").items():
        print(f"  {status}: {count}")
    print("Attachment targets:")
    for attachment, count in count_by(matrix_rows, "attachment_target").items():
        print(f"  {attachment}: {count}")
    return 0


def namespace_sequence_gap_count(rows: list[dict[str, str]]) -> int:
    seen_by_namespace: dict[str, set[int]] = {}
    for row in rows:
        parts = row["source_item_id"].split("-")
        namespace = "-".join(parts[:3])
        sequence = int(parts[3])
        seen_by_namespace.setdefault(namespace, set()).add(sequence)

    gap_count = 0
    for sequences in seen_by_namespace.values():
        expected = set(range(1, max(sequences) + 1))
        gap_count += len(expected - sequences)
    return gap_count


def register_text(name: str) -> str:
    path = AUDIT_DIR / name
    if not path.exists():
        raise CheckError(f"missing audit register/report: {repo_relative(path)}")
    return path.read_text(encoding="utf-8")


def check_catalog_qa(catalog_path: Path, matrix_path: Path) -> tuple[
    list[dict[str, str]], list[dict[str, str]]
]:
    catalog_fieldnames, catalog_rows = read_tsv(catalog_path)
    matrix_fieldnames, matrix_rows = read_tsv(matrix_path)
    require_exact_columns(catalog_path, catalog_fieldnames, CATALOG_REQUIRED_COLUMNS)
    require_exact_columns(matrix_path, matrix_fieldnames, MATRIX_REQUIRED_COLUMNS)

    catalog_rows = validate_catalog(catalog_path)
    matrix_rows = validate_matrix(matrix_path, catalog_rows)

    missing_register = register_text("missing_item_register.md")
    guardrail_register = register_text("guardrail_register.md")
    retrieval_register = register_text("retrieval_weakness_register.md")

    for index, row in enumerate(catalog_rows, start=2):
        source_item_id = row["source_item_id"]
        expected_scope = version_scope_from_id(source_item_id)
        if row["version_scope"] != expected_scope:
            raise CheckError(
                f"{repo_relative(catalog_path)} row {index}: ID version code does not "
                f"match version_scope for {source_item_id}"
            )
        for field in ("source_heading", "literal_tokens", "source_summary"):
            if not row[field].strip():
                raise CheckError(
                    f"{repo_relative(catalog_path)} row {index}: {field} is required "
                    "for catalog QA"
                )
        source_path = REPO_ROOT / row["source_path"]
        if not source_path.exists():
            raise CheckError(
                f"{repo_relative(catalog_path)} row {index}: source_path does not exist: "
                f"{row['source_path']}"
            )
        status = row["coverage_status"]
        if status in {"Covered", "Covered-by-routing", "Guardrail", "Retrieval-weak"}:
            if not row["attachment_anchor"].strip():
                raise CheckError(
                    f"{repo_relative(catalog_path)} row {index}: attachment_anchor is "
                    f"required for {status}"
                )
        if status == "Missing" and source_item_id not in missing_register:
            raise CheckError(
                f"{source_item_id} is Missing in catalog but absent from "
                "missing_item_register.md"
            )
        if (
            status in {"Guardrail", "Out-of-scope"}
            and source_item_id not in guardrail_register
        ):
            raise CheckError(
                f"{source_item_id} is {status} in catalog but absent from "
                "guardrail_register.md"
            )
        if status == "Retrieval-weak" and source_item_id not in retrieval_register:
            raise CheckError(
                f"{source_item_id} is Retrieval-weak in catalog but absent from "
                "retrieval_weakness_register.md"
            )

    missing_families = sorted(
        SOURCE_FAMILIES - {row["source_family"] for row in catalog_rows}
    )
    if missing_families:
        raise CheckError(
            "catalog has no rows for source families: " + ", ".join(missing_families)
        )

    return catalog_rows, matrix_rows


def cmd_catalog_qa(args: argparse.Namespace) -> int:
    catalog_path = Path(args.catalog)
    matrix_path = Path(args.matrix)
    catalog_rows, matrix_rows = check_catalog_qa(catalog_path, matrix_path)
    print("OK: catalog QA passed")
    print(f"Catalog rows: {len(catalog_rows)}")
    print(f"Matrix rows: {len(matrix_rows)}")
    print(f"ID namespace sequence gaps: {namespace_sequence_gap_count(catalog_rows)}")
    print("Coverage statuses:")
    for status, count in count_by(catalog_rows, "coverage_status").items():
        print(f"  {status}: {count}")
    print("Version scopes:")
    for scope, count in count_by(catalog_rows, "version_scope").items():
        print(f"  {scope}: {count}")
    print("Source families:")
    for family, count in count_by(catalog_rows, "source_family").items():
        print(f"  {family}: {count}")
    print("Audit jobs:")
    for job, count in count_by(catalog_rows, "audit_job").items():
        print(f"  {job}: {count}")
    return 0


def split_markdown_row(line: str) -> list[str]:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return []
    return [cell.strip() for cell in stripped[1:-1].split(" | ")]


def guardrail_register_rows() -> dict[str, dict[str, str]]:
    text = register_text("guardrail_register.md")
    rows: dict[str, dict[str, str]] = {}
    for line_number, line in enumerate(text.splitlines(), start=1):
        if not line.startswith("| SRC-"):
            continue
        cells = split_markdown_row(line)
        if len(cells) != 11:
            raise CheckError(
                "guardrail_register.md row could not be parsed at line "
                f"{line_number}: expected 11 cells, found {len(cells)}"
            )
        source_item_id = cells[0]
        if source_item_id in rows:
            raise CheckError(
                f"guardrail_register.md has duplicate row for {source_item_id}"
            )
        rows[source_item_id] = {
            "source_item_id": cells[0],
            "coverage_status": cells[1],
            "source_family": cells[2],
            "version_scope": cells[3],
            "source_path": cells[4],
            "source_heading": cells[5],
            "guardrail_reason": cells[6],
            "safest_next_check": cells[7],
            "attachment_target": cells[8],
            "audit_job": cells[9],
            "evidence": cells[10],
        }
    return rows


def contains_any(value: str, needles: tuple[str, ...]) -> bool:
    lowered = value.lower()
    return any(needle in lowered for needle in needles)


def check_guardrail_text(source_item_id: str, status: str, reason: str, check: str) -> None:
    for field_name, value in (
        ("guardrail_reason", reason),
        ("safest_next_check", check),
    ):
        if not value.strip():
            raise CheckError(f"{source_item_id}: {field_name} is empty")
        if "..." in value:
            raise CheckError(f"{source_item_id}: {field_name} contains ellipsis")

    if status == "Out-of-scope":
        if not contains_any(reason, ("outside", "out-of-scope")) or "scope" not in reason.lower():
            raise CheckError(
                f"{source_item_id}: Out-of-scope reason must explicitly name scope"
            )
        if not contains_any(check, ("ask", "do not", "route", "otherwise")):
            raise CheckError(
                f"{source_item_id}: Out-of-scope safest_next_check lacks action pattern"
            )
        return

    boundary_terms = (
        "exact",
        "patch",
        "version",
        "installed",
        "runtime",
        "live",
        "source",
        "selected",
        "depends",
        "requires",
        "does not",
        "cannot",
        "conflict",
        "boundary",
        "package",
        "environment",
        "topology",
        "output",
        "logs",
        "diagnostics",
    )
    action_terms = (
        "ask",
        "query",
        "run ",
        "validate",
        "consult",
        "state only",
        "answer only",
        "preserve only",
        "route",
        "direct",
    )
    if not contains_any(reason, boundary_terms):
        raise CheckError(
            f"{source_item_id}: Guardrail reason lacks a source/customer boundary term"
        )
    if not contains_any(check, action_terms):
        raise CheckError(
            f"{source_item_id}: safest_next_check lacks missing-input or next-check action"
        )


def check_guardrail_audit(
    catalog_path: Path, matrix_path: Path
) -> tuple[list[dict[str, str]], list[dict[str, str]], dict[str, dict[str, str]]]:
    catalog_rows, matrix_rows = check_matrix_qa(catalog_path, matrix_path)
    register_rows = guardrail_register_rows()

    guarded_catalog = {
        row["source_item_id"]: row
        for row in catalog_rows
        if row["coverage_status"] in {"Guardrail", "Out-of-scope"}
    }
    guarded_matrix = {
        row["source_item_id"]: row
        for row in matrix_rows
        if row["coverage_status"] in {"Guardrail", "Out-of-scope"}
    }
    if set(guarded_catalog) != set(guarded_matrix):
        missing_in_matrix = sorted(set(guarded_catalog) - set(guarded_matrix))
        extra_in_matrix = sorted(set(guarded_matrix) - set(guarded_catalog))
        raise CheckError(
            "guardrail matrix/catalog ID mismatch; missing in matrix: "
            f"{missing_in_matrix}; extra in matrix: {extra_in_matrix}"
        )
    if set(guarded_catalog) != set(register_rows):
        missing_in_register = sorted(set(guarded_catalog) - set(register_rows))
        extra_in_register = sorted(set(register_rows) - set(guarded_catalog))
        raise CheckError(
            "guardrail register/catalog ID mismatch; missing in register: "
            f"{missing_in_register}; extra in register: {extra_in_register}"
        )

    for source_item_id, catalog_row in guarded_catalog.items():
        matrix_row = guarded_matrix[source_item_id]
        register_row = register_rows[source_item_id]
        for field in (
            "coverage_status",
            "source_family",
            "version_scope",
            "source_path",
            "source_heading",
            "attachment_target",
        ):
            if clean_cell(register_row[field]) != clean_cell(catalog_row[field]):
                raise CheckError(
                    f"guardrail register mismatch for {source_item_id} field {field}: "
                    f"{register_row[field]!r} != {catalog_row[field]!r}"
                )
            if clean_cell(matrix_row[field]) != clean_cell(catalog_row[field]):
                raise CheckError(
                    f"guardrail matrix mismatch for {source_item_id} field {field}: "
                    f"{matrix_row[field]!r} != {catalog_row[field]!r}"
                )
        check_guardrail_text(
            source_item_id,
            catalog_row["coverage_status"],
            catalog_row["guardrail_reason"],
            register_row["safest_next_check"],
        )
        if clean_cell(register_row["guardrail_reason"]) != clean_cell(
            catalog_row["guardrail_reason"]
        ):
            check_guardrail_text(
                source_item_id,
                catalog_row["coverage_status"],
                register_row["guardrail_reason"],
                register_row["safest_next_check"],
            )

    return catalog_rows, matrix_rows, register_rows


def cmd_guardrail_audit(args: argparse.Namespace) -> int:
    catalog_rows, matrix_rows, register_rows = check_guardrail_audit(
        Path(args.catalog), Path(args.matrix)
    )
    guarded_catalog = [
        row
        for row in catalog_rows
        if row["coverage_status"] in {"Guardrail", "Out-of-scope"}
    ]
    print("OK: guardrail audit passed")
    print(f"Catalog rows: {len(catalog_rows)}")
    print(f"Matrix rows: {len(matrix_rows)}")
    print(f"Guardrail register rows: {len(register_rows)}")
    print("Guardrail dispositions:")
    for status, count in count_by(guarded_catalog, "coverage_status").items():
        print(f"  {status}: {count}")
    print("Guardrail source families:")
    for family, count in count_by(guarded_catalog, "source_family").items():
        print(f"  {family}: {count}")
    return 0


def infer_version_scope(path: Path) -> str:
    value = str(path)
    if "Altibase_7.1" in value or "PatchNotes/Altibase_7.1" in value:
        return "7.1"
    if "Altibase_7.3" in value or "PatchNotes/Altibase_7.3" in value:
        return "7.3"
    if "Altibase_trunk" in value:
        return "8.1"
    if "ReleaseNotes" in value:
        return "patch-specific"
    return "cross-version"


def infer_item_type(heading: str) -> str:
    text = heading.lower()
    if "error" in text or "err-" in text or "0x" in text:
        return "error code"
    if "view" in text or "v$" in text:
        return "view"
    if "syntax" in text or "create " in text or "alter " in text or "drop " in text:
        return "SQL syntax"
    if "property" in text or re.search(r"\b[A-Z][A-Z0-9]*_[A-Z0-9_]+\b", heading):
        return "property"
    if "install" in text or "backup" in text or "restore" in text or "recover" in text:
        return "runbook step"
    if "jdbc" in text or "api" in text:
        return "API"
    if "option" in text or "command" in text or "utility" in text:
        return "tool command"
    if "release" in text or "fixed" in text or "added" in text:
        return "version note"
    return "other documented category"


def literal_tokens_from_heading(heading: str) -> str:
    tokens = [match.group(1).strip() for match in BACKTICK_RE.finditer(heading)]
    tokens.extend(match.group(0) for match in TOKEN_RE.finditer(heading))
    deduped = []
    seen = set()
    for token in tokens:
        if token and token not in seen:
            seen.add(token)
            deduped.append(token)
    return "; ".join(deduped)


def iter_markdown_headings(paths: list[Path]):
    for path in paths:
        with path.open("r", encoding="utf-8", errors="replace") as handle:
            stack: list[str] = []
            for line_number, line in enumerate(handle, start=1):
                match = HEADING_RE.match(line)
                if not match:
                    continue
                level = len(match.group(1))
                heading = match.group(2).strip()
                stack = stack[: level - 1]
                stack.append(heading)
                yield path, line_number, level, " > ".join(stack), heading


def cmd_outline(args: argparse.Namespace) -> int:
    paths = [Path(value) for value in args.paths]
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(
        [
            "source_family",
            "version_scope",
            "source_path",
            "line",
            "heading_level",
            "source_heading",
            "item_type_hint",
            "literal_token_hints",
        ]
    )
    for path, line_number, level, heading_path, heading in iter_markdown_headings(paths):
        version_scope = args.version_scope or infer_version_scope(path)
        writer.writerow(
            [
                args.source_family,
                version_scope,
                repo_relative(path),
                line_number,
                level,
                heading_path,
                infer_item_type(heading),
                literal_tokens_from_heading(heading),
            ]
        )
    return 0


def cmd_next_id(args: argparse.Namespace) -> int:
    catalog_path = Path(args.catalog)
    _, rows = read_tsv(catalog_path)
    prefix = f"SRC-{args.kind_code}-{args.version_code}-"
    max_seen = 0
    for row in rows:
        source_item_id = row.get("source_item_id", "")
        if source_item_id.startswith(prefix):
            try:
                max_seen = max(max_seen, int(source_item_id.rsplit("-", 1)[1]))
            except ValueError:
                continue
    print(f"{prefix}{max_seen + 1:06d}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    check = subparsers.add_parser("check", help="validate catalog and matrix TSVs")
    check.add_argument("--catalog", default=str(DEFAULT_CATALOG))
    check.add_argument("--matrix", default=str(DEFAULT_MATRIX))
    check.add_argument("--require-registers", action="store_true")
    check.set_defaults(func=cmd_check)

    build_matrix = subparsers.add_parser(
        "build-matrix", help="initialize source_to_attachment_matrix.tsv from catalog rows"
    )
    build_matrix.add_argument("--catalog", default=str(DEFAULT_CATALOG))
    build_matrix.add_argument("--matrix", default=str(DEFAULT_MATRIX))
    build_matrix.add_argument("--audit-job", default="FCA-J040")
    build_matrix.add_argument(
        "--force",
        action="store_true",
        help="overwrite an already populated matrix intentionally",
    )
    build_matrix.set_defaults(func=cmd_build_matrix)

    matrix_qa = subparsers.add_parser(
        "matrix-qa", help="verify matrix coverage of every catalog row"
    )
    matrix_qa.add_argument("--catalog", default=str(DEFAULT_CATALOG))
    matrix_qa.add_argument("--matrix", default=str(DEFAULT_MATRIX))
    matrix_qa.set_defaults(func=cmd_matrix_qa)

    catalog_qa = subparsers.add_parser(
        "catalog-qa", help="run stricter catalog consolidation QA checks"
    )
    catalog_qa.add_argument("--catalog", default=str(DEFAULT_CATALOG))
    catalog_qa.add_argument("--matrix", default=str(DEFAULT_MATRIX))
    catalog_qa.set_defaults(func=cmd_catalog_qa)

    guardrail_audit = subparsers.add_parser(
        "guardrail-audit",
        help="verify Guardrail and Out-of-scope rows have actionable next-check patterns",
    )
    guardrail_audit.add_argument("--catalog", default=str(DEFAULT_CATALOG))
    guardrail_audit.add_argument("--matrix", default=str(DEFAULT_MATRIX))
    guardrail_audit.set_defaults(func=cmd_guardrail_audit)

    outline = subparsers.add_parser(
        "outline", help="emit a heading outline TSV for source extraction"
    )
    outline.add_argument("--source-family", required=True, choices=sorted(SOURCE_FAMILIES))
    outline.add_argument("--version-scope", choices=sorted(VERSION_SCOPES))
    outline.add_argument("paths", nargs="+")
    outline.set_defaults(func=cmd_outline)

    next_id = subparsers.add_parser("next-id", help="print the next source item ID")
    next_id.add_argument("--catalog", default=str(DEFAULT_CATALOG))
    next_id.add_argument("--kind-code", required=True)
    next_id.add_argument(
        "--version-code", required=True, choices=["7.1", "7.3", "8.1", "XVER", "PATCH"]
    )
    next_id.set_defaults(func=cmd_next_id)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except CheckError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
