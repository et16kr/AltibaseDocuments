#!/usr/bin/env python3
"""Build deterministic Stage 1 repository-local source manifests."""

from __future__ import annotations

import argparse
import csv
import hashlib
import math
import re
import sys
from dataclasses import dataclass
from pathlib import Path


JOB_ID = "S1-J002"

ROOT = Path(__file__).resolve().parents[3]
SOURCE_PACK_DIR = Path("GPTs/source_pack")
SOURCE_ROOTS = [
    Path("Manuals"),
    Path("ReleaseNotes"),
    Path("PatchNotes"),
    Path("Technical Documents"),
    Path("3rd Party Guide for Altibase"),
]

MANIFEST_PATH = SOURCE_PACK_DIR / "source_manifest.tsv"
EXCLUSION_PATH = SOURCE_PACK_DIR / "source_exclusion_register.tsv"

MANIFEST_COLUMNS = [
    "source_id",
    "source_origin",
    "source_path",
    "source_role",
    "source_family",
    "title",
    "version_scope",
    "language",
    "authority_label",
    "aid_classification",
    "classification_evidence",
    "selection_decision",
    "extraction_mode",
    "source_sha256",
    "byte_count",
    "line_count",
    "estimated_tokens",
    "selected_by_job",
    "last_verified_job",
    "notes",
]

EXCLUSION_COLUMNS = [
    "exclusion_id",
    "candidate_origin",
    "candidate_path",
    "source_family",
    "version_scope",
    "language",
    "exclusion_type",
    "exclusion_reason",
    "evidence_ref",
    "replacement_source_id",
    "aid_tier",
    "risk_label",
    "selected_by_job",
    "review_status",
    "notes",
]

APPROVED_SUPPORT_REPORTS = [
    {
        "path": "GPTs/reports/stage_01_source_pack_baseline_plan.md",
        "family": "stage1_source_selection",
        "title": "Stage 1 Source Pack And Korean-Aligned English Baseline Plan",
        "evidence": "AGENTS.md;GPTs/reports/customer_agent_enablement_requirements.md",
        "notes": "Approved support evidence: defines the Stage 1 manifest schemas, selection contract, and validation gates.",
    },
    {
        "path": "GPTs/reports/source_inventory.md",
        "family": "source_inventory_support",
        "title": "Altibase GPTs Source Inventory",
        "evidence": "GPTs/reports/stage_01_source_pack_baseline_plan.md",
        "notes": "Approved support evidence: canonical source-root and attachment-to-source mapping support artifact.",
    },
    {
        "path": "GPTs/reports/coverage_matrix.md",
        "family": "source_inventory_support",
        "title": "Altibase GPTs Coverage Matrix",
        "evidence": "GPTs/reports/source_inventory.md",
        "notes": "Approved support evidence: maps source families, authority basis, and attachment coverage boundaries.",
    },
    {
        "path": "GPTs/reports/8_1_verification.md",
        "family": "release_notes_platform",
        "title": "Altibase 8.1 Verification Evidence",
        "evidence": "GPTs/reports/source_inventory.md",
        "notes": "Approved support evidence: records the 8.1 verified-source basis and customer-safe wording.",
    },
    {
        "path": "GPTs/reports/eng_kor_parity.md",
        "family": "source_inventory_support",
        "title": "English/Korean Parity Evidence",
        "evidence": "GPTs/reports/source_inventory.md",
        "notes": "Approved support evidence: records Korean-authority parity and source-drift evidence for paired sources.",
    },
    {
        "path": "GPTs/reports/gap_register.md",
        "family": "source_inventory_support",
        "title": "Altibase GPTs Gap Register",
        "evidence": "GPTs/reports/coverage_matrix.md;GPTs/reports/source_inventory.md",
        "notes": "Approved support evidence: records source-backed gaps, accepted limitations, and downstream guardrails.",
    },
]


@dataclass(frozen=True)
class FileStats:
    sha256: str
    byte_count: int
    line_count: int
    estimated_tokens: int
    text: str


def rel(path: Path) -> str:
    return path.as_posix()


def clean(value: object) -> str:
    text = "" if value is None else str(value)
    return re.sub(r"[\t\r\n]+", " ", text).strip()


def read_stats(path: Path, *, require_utf8: bool) -> FileStats:
    data = (ROOT / path).read_bytes()
    sha256 = hashlib.sha256(data).hexdigest()
    line_count = data.count(b"\n")
    if data and not data.endswith(b"\n"):
        line_count += 1
    if require_utf8:
        text = data.decode("utf-8")
        estimated_tokens = max(1, math.ceil(len(text) / 4)) if text else 0
    else:
        try:
            text = data.decode("utf-8")
            estimated_tokens = max(1, math.ceil(len(text) / 4)) if text else 0
        except UnicodeDecodeError:
            text = ""
            estimated_tokens = max(1, math.ceil(len(data) / 4)) if data else 0
    return FileStats(
        sha256=sha256,
        byte_count=len(data),
        line_count=line_count,
        estimated_tokens=estimated_tokens,
        text=text,
    )


def title_from_markdown(path: Path, stats: FileStats) -> str:
    for line in stats.text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return clean(stripped.lstrip("#").strip()) or path.stem
    return clean(path.stem.replace("_", " "))


def infer_language(path: Path) -> str:
    parts = path.parts
    if "kor" in parts:
        return "ko"
    if "eng" in parts:
        return "en"
    if path.suffix.lower() not in {".md", ".sql", ".txt"}:
        return "n/a"
    return "mixed"


def infer_version_scope(path: Path) -> str:
    p = rel(path)
    name = path.name
    if "Altibase_trunk" in p:
        return "8.1_verified"
    if "Altibase 8.1" in p:
        return "8.1_verified"
    if "Altibase_8_1_0_0_1" in name:
        return "8.1.0.0.1"
    match = re.search(r"Altibase_((?:[0-9]+_)*[0-9]+)", name)
    if match:
        return ".".join(match.group(1).split("_"))
    if "Altibase_7.1" in p or "Altibase 7.1" in p:
        return "7.1"
    if "Altibase_7.3" in p or "Altibase 7.3" in p:
        return "7.3"
    if "Altibase_6.1.1" in p:
        return "6.1.1"
    if "Altibase_6.3.1" in p:
        return "6.3.1"
    if "Altibase_6.5.1" in p:
        return "6.5.1"
    tool_match = re.search(r"(Migration_Center|Replication_Manager|dataCompJ|ShardManager).*?([0-9]+)_([0-9]+)", name)
    if tool_match:
        return f"{tool_match.group(1).replace('_', ' ')} {tool_match.group(2)}.{tool_match.group(3)}"
    if path.parts[:2] == ("Manuals", "Tools"):
        return "multi"
    if path.parts and path.parts[0] in {"Technical Documents", "3rd Party Guide for Altibase"}:
        return "multi"
    return "multi"


def is_readme_or_index(path: Path) -> bool:
    lower = path.name.lower()
    return lower in {"readme.md", "readme_sample.md"} or lower.endswith("version_histories.md")


def infer_source_role(path: Path) -> str:
    top = path.parts[0]
    if top == "Manuals":
        return "tool_manual" if len(path.parts) > 1 and path.parts[1] == "Tools" else "product_source"
    if top == "ReleaseNotes":
        return "release_note"
    if top == "PatchNotes":
        return "patch_note"
    if top == "Technical Documents":
        return "technical_document"
    if top == "3rd Party Guide for Altibase":
        return "third_party_guide"
    if top == "GPTs":
        return "support_evidence"
    return "product_source"


def infer_source_family(path: Path) -> str:
    p = rel(path).lower()
    name = path.name.lower()
    if path.parts[0] == "GPTs":
        for item in APPROVED_SUPPORT_REPORTS:
            if item["path"] == rel(path):
                return item["family"]
        return "source_inventory_support"
    if is_readme_or_index(path):
        if path.parts[0] == "ReleaseNotes":
            return "release_notes_platform"
        if path.parts[0] == "PatchNotes":
            return "patch_notes"
        if path.parts[0] == "3rd Party Guide for Altibase":
            return "third_party_guides"
        return "source_index"
    if path.parts[0] == "ReleaseNotes":
        if "migration_center" in name:
            return "migration_oracle"
        if "replication_manager" in name:
            return "replication_manager"
        if "datacompj" in name:
            return "utilities_datacompj"
        if "altishapeloader" in name:
            return "spatial_nifi_tableau"
        return "release_notes_platform"
    if path.parts[0] == "PatchNotes":
        return "patch_notes"
    if path.parts[0] == "Technical Documents":
        if "javacompatibility" in name:
            return "jdbc_java"
        return "technical_documents_support"
    if path.parts[0] == "3rd Party Guide for Altibase":
        return "third_party_guides"
    if "getting started" in name or "installation guide" in name:
        return "getting_started_installation"
    if "administrator" in name:
        return "administrator_operations"
    if "sql reference" in name and "spatial" not in name:
        return "sql_reference"
    if "general reference-1" in name or "general_reference-1" in name:
        return "general_reference_1_datatypes_properties"
    if "general reference-2" in name or "general_reference-2" in name:
        return "general_reference_2_dictionary_views"
    if "error message" in name:
        return "error_message_reference"
    if "performance tuning" in name:
        return "performance_tuning"
    if "monitoring api" in name or "snmp" in name:
        return "monitoring_api_snmp"
    if "replication manual" in name:
        return "replication_manual"
    if "log analyzer" in name:
        return "log_analyzer"
    if "replication manager" in name:
        return "replication_manager"
    if "ssl tls" in name:
        return "security_ssl_tls"
    if "stored procedures" in name or "external procedures" in name:
        return "stored_external_procedures"
    if "jdbc" in name:
        return "jdbc_java"
    if any(token in name for token in ["cli user", "odbc", "c interface", "precompiler", "api user"]):
        return "c_cli_odbc_precompiler"
    if "isql" in name or "iloader" in name:
        return "isql_iloader"
    if any(token in name for token in ["utilities", "datacompj", "heartbeat"]):
        return "utilities_datacompj"
    if "migration center" in name or "adapter for oracle" in name:
        return "migration_oracle"
    if "db link" in name or "hadoop connector" in name or "3rd party connector" in name:
        return "dblink_hadoop_external_connectors"
    if "spatial" in name or "altishapeloader" in name:
        return "spatial_nifi_tableau"
    if "new features" in name:
        return "release_notes_platform"
    if "storedprocedure" in p:
        return "stored_external_procedures"
    return "source_index"


def authority_label(path: Path, language: str, version_scope: str, source_role: str) -> str:
    if source_role == "support_evidence":
        return "Approved support evidence"
    verified = version_scope == "8.1_verified" or version_scope.startswith("8.1")
    if language == "ko":
        return "Korean authoritative; Altibase 8.1 verified source" if verified else "Korean authoritative"
    if language == "en":
        return "English extraction aid; Altibase 8.1 verified source" if verified else "English extraction aid"
    if verified:
        return "Altibase 8.1 verified source index"
    return "Repository source evidence"


def include_markdown(path: Path, stats: FileStats) -> bool:
    p = rel(path)
    if p.startswith("PatchNotes/Altibase_6."):
        return False
    if stats.byte_count <= 1:
        return False
    return True


def exclusion_for(path: Path, stats: FileStats | None) -> dict[str, str]:
    p = rel(path)
    language = infer_language(path)
    version_scope = infer_version_scope(path)
    source_family = infer_source_family(path)
    suffix = path.suffix.lower()

    if suffix == ".md" and p.startswith("PatchNotes/Altibase_6."):
        return {
            "candidate_origin": "repo",
            "candidate_path": p,
            "source_family": "patch_notes",
            "version_scope": version_scope,
            "language": language,
            "exclusion_type": "out_of_scope",
            "exclusion_reason": "Altibase 6.x patch notes are outside the active Altibase 7.1, 7.3, and 8.1 answer scope unless a later migration or historical job explicitly selects them.",
            "evidence_ref": "GPTs/reports/source_inventory.md",
            "replacement_source_id": "",
            "aid_tier": "",
            "risk_label": "low",
            "selected_by_job": JOB_ID,
            "review_status": "accepted",
            "notes": "Older patch-level source retained in repository but not selected for this source-pack baseline.",
        }

    if suffix == ".md" and stats is not None and stats.byte_count <= 1:
        return {
            "candidate_origin": "repo",
            "candidate_path": p,
            "source_family": source_family,
            "version_scope": version_scope,
            "language": language,
            "exclusion_type": "low_information",
            "exclusion_reason": "Markdown file contains no substantive source text beyond a newline.",
            "evidence_ref": "file_byte_count<=1",
            "replacement_source_id": "",
            "aid_tier": "",
            "risk_label": "none",
            "selected_by_job": JOB_ID,
            "review_status": "accepted",
            "notes": "Placeholder Markdown file.",
        }

    if suffix == ".sql":
        return {
            "candidate_origin": "repo",
            "candidate_path": p,
            "source_family": source_family,
            "version_scope": version_scope,
            "language": language,
            "exclusion_type": "non_markdown",
            "exclusion_reason": "SQL sidecar is useful operational evidence but is not eligible for the Stage 1 exact Markdown extraction mode.",
            "evidence_ref": "3rd Party Guide for Altibase/eng/Tableau User's Guide for Altibase/Tableau User's Guide for Altibase.md",
            "replacement_source_id": "",
            "aid_tier": "",
            "risk_label": "medium",
            "selected_by_job": JOB_ID,
            "review_status": "accepted",
            "notes": "Later text-sidecar extraction should promote this file if source-pack SQL sidecars become in scope.",
        }

    non_markdown_reason = "Binary, media, PDF, or helper sidecar is outside the Stage 1 exact Markdown source-pack extraction mode."
    if suffix == ".pdf":
        non_markdown_reason = "PDF sidecar is outside the Stage 1 exact Markdown extraction mode; Markdown counterparts are selected where available."
    elif suffix in {".png", ".gif", ".jpg", ".jpeg", ".emf", ".vsd"}:
        non_markdown_reason = "Media asset is outside the Stage 1 exact Markdown extraction mode; referenced Markdown sources are selected separately."
    elif suffix == ".bat":
        non_markdown_reason = "Helper script is outside the selected Markdown source-pack extraction mode."

    return {
        "candidate_origin": "repo",
        "candidate_path": p,
        "source_family": source_family,
        "version_scope": version_scope,
        "language": language,
        "exclusion_type": "non_markdown",
        "exclusion_reason": non_markdown_reason,
        "evidence_ref": "GPTs/reports/stage_01_source_pack_baseline_plan.md",
        "replacement_source_id": "",
        "aid_tier": "",
        "risk_label": "low",
        "selected_by_job": JOB_ID,
        "review_status": "accepted",
        "notes": "Candidate remains available in the repository for later media/PDF/script-specific source handling.",
    }


def load_existing_ids(path: Path, key_field: str, id_field: str) -> tuple[dict[str, str], int]:
    full_path = ROOT / path
    if not full_path.exists():
        return {}, 0
    result: dict[str, str] = {}
    max_id = 0
    with full_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            key = row.get(key_field, "")
            value = row.get(id_field, "")
            if key and value:
                result[key] = value
                match = re.search(r"-(\d+)$", value)
                if match:
                    max_id = max(max_id, int(match.group(1)))
    return result, max_id


def allocate_id(path: str, existing: dict[str, str], counter: list[int], prefix: str) -> str:
    if path in existing:
        return existing[path]
    counter[0] += 1
    return f"{prefix}-{counter[0]:06d}"


def iter_source_root_files() -> list[Path]:
    files: list[Path] = []
    for source_root in SOURCE_ROOTS:
        root_path = ROOT / source_root
        if not root_path.exists():
            raise FileNotFoundError(f"source root not found: {source_root}")
        files.extend(path.relative_to(ROOT) for path in root_path.rglob("*") if path.is_file())
    return sorted(files, key=rel)


def build_rows() -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    source_ids, max_source_id = load_existing_ids(MANIFEST_PATH, "source_path", "source_id")
    exclusion_ids, max_exclusion_id = load_existing_ids(EXCLUSION_PATH, "candidate_path", "exclusion_id")
    source_counter = [max_source_id]
    exclusion_counter = [max_exclusion_id]

    included_paths: list[Path] = []
    excluded: list[tuple[Path, dict[str, str]]] = []

    for path in iter_source_root_files():
        if path.suffix.lower() == ".md":
            stats = read_stats(path, require_utf8=True)
            if include_markdown(path, stats):
                included_paths.append(path)
            else:
                excluded.append((path, exclusion_for(path, stats)))
        else:
            excluded.append((path, exclusion_for(path, None)))

    for support in APPROVED_SUPPORT_REPORTS:
        path = Path(support["path"])
        if not (ROOT / path).exists():
            raise FileNotFoundError(f"approved support report not found: {path}")
        included_paths.append(path)

    included_rows: list[dict[str, str]] = []
    for path in sorted(included_paths, key=lambda p: (1 if p.parts[0] == "GPTs" else 0, rel(p))):
        stats = read_stats(path, require_utf8=True)
        source_role = infer_source_role(path)
        language = infer_language(path)
        version_scope = infer_version_scope(path)
        support = next((item for item in APPROVED_SUPPORT_REPORTS if item["path"] == rel(path)), None)
        notes = support["notes"] if support else f"Selected repository-local Markdown source from {path.parts[0]}."
        classification_evidence = support["evidence"] if support else ""
        title = support["title"] if support else title_from_markdown(path, stats)
        included_rows.append(
            {
                "source_id": allocate_id(rel(path), source_ids, source_counter, "SRC"),
                "source_origin": "repo",
                "source_path": rel(path),
                "source_role": source_role,
                "source_family": infer_source_family(path),
                "title": title,
                "version_scope": version_scope,
                "language": language,
                "authority_label": authority_label(path, language, version_scope, source_role),
                "aid_classification": "",
                "classification_evidence": classification_evidence,
                "selection_decision": "include_support_evidence" if source_role == "support_evidence" else "include_exact",
                "extraction_mode": "support_evidence_only" if source_role == "support_evidence" else "exact_markdown",
                "source_sha256": stats.sha256,
                "byte_count": str(stats.byte_count),
                "line_count": str(stats.line_count),
                "estimated_tokens": str(stats.estimated_tokens),
                "selected_by_job": JOB_ID,
                "last_verified_job": JOB_ID,
                "notes": notes,
            }
        )

    excluded_rows: list[dict[str, str]] = []
    for path, row in sorted(excluded, key=lambda item: rel(item[0])):
        row = dict(row)
        row["exclusion_id"] = allocate_id(rel(path), exclusion_ids, exclusion_counter, "EXC")
        excluded_rows.append(row)

    return included_rows, excluded_rows


def normalize_rows(rows: list[dict[str, str]], columns: list[str]) -> list[dict[str, str]]:
    return [{column: clean(row.get(column, "")) for column in columns} for row in rows]


def render_tsv(rows: list[dict[str, str]], columns: list[str]) -> str:
    output = ["\t".join(columns)]
    for row in normalize_rows(rows, columns):
        output.append("\t".join(row[column] for column in columns))
    return "\n".join(output) + "\n"


def validate(manifest_rows: list[dict[str, str]], exclusion_rows: list[dict[str, str]]) -> None:
    errors: list[str] = []
    source_ids = [row["source_id"] for row in manifest_rows]
    if len(source_ids) != len(set(source_ids)):
        errors.append("duplicate source_id values found")
    exclusion_ids = [row["exclusion_id"] for row in exclusion_rows]
    if len(exclusion_ids) != len(set(exclusion_ids)):
        errors.append("duplicate exclusion_id values found")
    source_paths = [row["source_path"] for row in manifest_rows]
    if len(source_paths) != len(set(source_paths)):
        errors.append("duplicate included source_path values found")
    for row in manifest_rows:
        if not (ROOT / row["source_path"]).exists():
            errors.append(f"included source path does not exist: {row['source_path']}")
        if row["source_path"].startswith("GPTs/reports/") and row["source_role"] != "support_evidence":
            errors.append(f"GPTs/reports row is not support_evidence: {row['source_path']}")
        if row["source_role"] == "support_evidence" and not row["classification_evidence"]:
            errors.append(f"support evidence row lacks classification_evidence: {row['source_path']}")
    included_path_set = set(source_paths)
    for row in exclusion_rows:
        if not row["exclusion_reason"]:
            errors.append(f"excluded candidate lacks reason: {row['candidate_path']}")
        if row["candidate_path"] in included_path_set and row["review_status"] != "superseded":
            errors.append(f"candidate is both included and excluded: {row['candidate_path']}")
    if errors:
        raise SystemExit("\n".join(f"ERROR: {error}" for error in errors))


def write_file(path: Path, content: str) -> None:
    full_path = ROOT / path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    full_path.write_text(content, encoding="utf-8", newline="")


def check_file(path: Path, expected: str) -> bool:
    full_path = ROOT / path
    if not full_path.exists():
        print(f"missing generated file: {path}", file=sys.stderr)
        return False
    actual = full_path.read_text(encoding="utf-8")
    if actual != expected:
        print(f"generated file is stale: {path}", file=sys.stderr)
        return False
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write generated manifests")
    parser.add_argument("--check", action="store_true", help="verify generated manifests are up to date")
    args = parser.parse_args()

    if args.write and args.check:
        parser.error("--write and --check are mutually exclusive")
    if not args.write and not args.check:
        args.check = True

    manifest_rows, exclusion_rows = build_rows()
    manifest_rows = normalize_rows(manifest_rows, MANIFEST_COLUMNS)
    exclusion_rows = normalize_rows(exclusion_rows, EXCLUSION_COLUMNS)
    validate(manifest_rows, exclusion_rows)

    manifest_content = render_tsv(manifest_rows, MANIFEST_COLUMNS)
    exclusion_content = render_tsv(exclusion_rows, EXCLUSION_COLUMNS)

    if args.write:
        write_file(MANIFEST_PATH, manifest_content)
        write_file(EXCLUSION_PATH, exclusion_content)
    else:
        ok = check_file(MANIFEST_PATH, manifest_content)
        ok = check_file(EXCLUSION_PATH, exclusion_content) and ok
        if not ok:
            return 1

    print(f"source_manifest rows: {len(manifest_rows)}")
    print(f"source_exclusion_register rows: {len(exclusion_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
