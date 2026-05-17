#!/usr/bin/env python3
"""Utilities for the Altibase GPT full coverage audit catalog.

The tools are intentionally conservative. They validate the machine-checkable
TSV contract and provide extraction aids, but they do not write canonical audit
rows. Catalog jobs remain responsible for source-backed judgment.
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

    catalog_qa = subparsers.add_parser(
        "catalog-qa", help="run stricter catalog consolidation QA checks"
    )
    catalog_qa.add_argument("--catalog", default=str(DEFAULT_CATALOG))
    catalog_qa.add_argument("--matrix", default=str(DEFAULT_MATRIX))
    catalog_qa.set_defaults(func=cmd_catalog_qa)

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
