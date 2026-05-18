#!/usr/bin/env python3
"""Validate Stage 1 source-pack manifests, shards, and upload notes."""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import math
import re
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


JOB_ID = "S1-J005"
JOB_DATE = "2026-05-18"

ROOT = Path(__file__).resolve().parents[3]
AID_ROOT = Path.home() / "AID"
SOURCE_PACK_DIR = Path("GPTs/source_pack")

MANIFEST_PATH = SOURCE_PACK_DIR / "source_manifest.tsv"
EXCLUSION_PATH = SOURCE_PACK_DIR / "source_exclusion_register.tsv"
SHARD_MANIFEST_PATH = SOURCE_PACK_DIR / "source_to_shard_manifest.tsv"
VALIDATION_NOTE_PATH = SOURCE_PACK_DIR / "source_pack_validation.md"
UPLOAD_ORDER_PATH = SOURCE_PACK_DIR / "upload_order.md"
GPT_INSTRUCTION_NOTE_PATH = SOURCE_PACK_DIR / "source_pack_gpt_instruction_note.md"

SOURCE_ROOTS = [
    Path("Manuals"),
    Path("ReleaseNotes"),
    Path("PatchNotes"),
    Path("Technical Documents"),
    Path("3rd Party Guide for Altibase"),
]

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

SHARD_MANIFEST_COLUMNS = [
    "source_id",
    "shard_id",
    "shard_path",
    "block_id",
    "order_in_shard",
    "source_start_line",
    "source_end_line",
    "source_sha256",
    "extracted_body_sha256",
    "block_byte_count",
    "block_line_count",
    "block_estimated_tokens",
    "shard_estimated_tokens",
    "upload_intended",
    "validation_status",
    "notes",
]

SELECTED_DECISIONS = {"include_exact", "include_support_evidence"}
ALLOWED_ORIGINS = {"repo", "aid"}
ALLOWED_UPLOAD_STATES = {"yes", "no", "candidate"}
ALLOWED_VALIDATION_STATUSES = {"pending", "pass", "fail"}
ALLOWED_EXCLUSION_STATUSES = {"draft", "accepted", "superseded", "recheck_required"}

GPT_KNOWLEDGE_FILE_COUNT_LIMIT = 20
GPT_KNOWLEDGE_FILE_SIZE_LIMIT_BYTES = 512 * 1024 * 1024
GPT_KNOWLEDGE_FILE_TOKEN_LIMIT = 2_000_000
UPLOAD_MARGIN_RATIO = 0.90
UPLOAD_MARGIN_BYTES = int(GPT_KNOWLEDGE_FILE_SIZE_LIMIT_BYTES * UPLOAD_MARGIN_RATIO)
UPLOAD_MARGIN_TOKENS = int(GPT_KNOWLEDGE_FILE_TOKEN_LIMIT * UPLOAD_MARGIN_RATIO)

BEGIN_RE = re.compile(rb"<!-- SOURCE_BLOCK_BEGIN ([^\n]*?) -->\n")
ATTR_RE = re.compile(r'([A-Za-z0-9_]+)="([^"]*)"')


@dataclass(frozen=True)
class FileStats:
    sha256: str
    byte_count: int
    line_count: int
    estimated_tokens: int


@dataclass(frozen=True)
class ShardBlock:
    source_id: str
    block_id: str
    shard_path: str
    start_offset: int
    body: bytes
    attrs: dict[str, str]


@dataclass(frozen=True)
class ShardSummary:
    shard_id: str
    shard_path: str
    source_count: int
    byte_count: int
    estimated_tokens: int
    upload_intended: str
    first_source_id: str
    last_source_id: str
    first_family: str
    last_family: str
    validation_status: str


@dataclass
class ValidationResult:
    errors: list[str]
    warnings: list[str]
    command_summaries: list[str]
    manifest_rows: list[dict[str, str]]
    selected_rows: list[dict[str, str]]
    exact_rows: list[dict[str, str]]
    support_rows: list[dict[str, str]]
    exclusion_rows: list[dict[str, str]]
    shard_rows: list[dict[str, str]]
    shard_summaries: list[ShardSummary]
    upload_candidate_paths: set[str]
    upload_not_ready: list[str]


def clean(value: object) -> str:
    text = "" if value is None else str(value)
    return re.sub(r"[\t\r\n]+", " ", text).strip()


def full_path_for(path_text: str) -> Path:
    if path_text.startswith("~/"):
        return Path.home() / path_text[2:]
    if path_text.startswith("AID:"):
        return AID_ROOT / path_text[4:].lstrip("/")
    return ROOT / path_text


def line_count(data: bytes) -> int:
    if not data:
        return 0
    return data.count(b"\n") + (0 if data.endswith(b"\n") else 1)


def estimated_tokens(data: bytes) -> int:
    text = data.decode("utf-8")
    return max(1, math.ceil(len(text) / 4)) if text else 0


def file_stats(path_text: str) -> FileStats:
    data = full_path_for(path_text).read_bytes()
    return FileStats(
        sha256=hashlib.sha256(data).hexdigest(),
        byte_count=len(data),
        line_count=line_count(data),
        estimated_tokens=estimated_tokens(data),
    )


def read_tsv(path: Path, expected_columns: list[str]) -> list[dict[str, str]]:
    full_path = ROOT / path
    with full_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames != expected_columns:
            raise ValueError(f"{path}: unexpected columns {reader.fieldnames!r}")
        return [{column: clean(row.get(column, "")) for column in expected_columns} for row in reader]


def int_field(row: dict[str, str], field: str, errors: list[str], label: str) -> int:
    value = row.get(field, "")
    try:
        return int(value)
    except ValueError:
        errors.append(f"{label}: {field} is not an integer: {value!r}")
        return 0


def source_sort_key(row: dict[str, str]) -> tuple[str, str, str, str, str]:
    return (
        row["source_family"],
        row["version_scope"],
        row["source_origin"],
        row["source_path"],
        row["source_id"],
    )


def shard_sort_key(row: dict[str, str]) -> tuple[int, int, str]:
    shard_match = re.search(r"(\d+)$", row["shard_id"])
    shard_number = int(shard_match.group(1)) if shard_match else 0
    try:
        order = int(row["order_in_shard"])
    except ValueError:
        order = 0
    return shard_number, order, row["source_id"]


def parse_attrs(begin_comment: bytes) -> dict[str, str]:
    text = begin_comment.decode("utf-8")
    return {key: html.unescape(value) for key, value in ATTR_RE.findall(text)}


def parse_shard_blocks(shard_path: str, errors: list[str]) -> list[ShardBlock]:
    full_path = ROOT / shard_path
    try:
        content = full_path.read_bytes()
    except FileNotFoundError:
        errors.append(f"{shard_path}: shard file does not exist")
        return []

    blocks: list[ShardBlock] = []
    position = 0
    while True:
        match = BEGIN_RE.search(content, position)
        if not match:
            break
        attrs = parse_attrs(match.group(0))
        source_id = attrs.get("source_id", "")
        block_id = attrs.get("block_id", "")
        if not source_id or not block_id:
            errors.append(f"{shard_path}: malformed SOURCE_BLOCK_BEGIN at byte {match.start()}")
            position = match.end()
            continue
        end_marker = f'<!-- SOURCE_BLOCK_END source_id="{source_id}" block_id="{block_id}" -->'.encode("utf-8")
        end_position = content.find(end_marker, match.end())
        if end_position < 0:
            errors.append(f"{shard_path}: missing SOURCE_BLOCK_END for {source_id} {block_id}")
            position = match.end()
            continue
        blocks.append(
            ShardBlock(
                source_id=source_id,
                block_id=block_id,
                shard_path=shard_path,
                start_offset=match.start(),
                body=content[match.end() : end_position],
                attrs=attrs,
            )
        )
        position = end_position + len(end_marker)
    return blocks


def read_shard_upload_header(shard_path: str) -> str:
    content = (ROOT / shard_path).read_bytes()[:1024].decode("utf-8", errors="replace")
    match = re.search(r"- Upload intended: `([^`]+)`", content)
    return match.group(1) if match else ""


def run_subcheck(args: list[str], errors: list[str]) -> str:
    completed = subprocess.run(
        [sys.executable, *args],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    command = "python3 " + " ".join(args)
    output = "\n".join(part.strip() for part in (completed.stdout, completed.stderr) if part.strip())
    if completed.returncode != 0:
        errors.append(f"{command} failed with exit code {completed.returncode}: {output}")
    return f"`{command}` -> exit {completed.returncode}"


def validate_source_pack() -> ValidationResult:
    errors: list[str] = []
    warnings: list[str] = []
    command_summaries = [
        run_subcheck(["GPTs/source_pack/scripts/build_source_manifest.py", "--check"], errors),
        run_subcheck(["GPTs/source_pack/scripts/build_source_pack.py", "--check"], errors),
    ]

    manifest_rows = read_tsv(MANIFEST_PATH, MANIFEST_COLUMNS)
    exclusion_rows = read_tsv(EXCLUSION_PATH, EXCLUSION_COLUMNS)
    shard_rows = read_tsv(SHARD_MANIFEST_PATH, SHARD_MANIFEST_COLUMNS)

    source_ids = [row["source_id"] for row in manifest_rows]
    source_paths = [row["source_path"] for row in manifest_rows]
    exclusion_ids = [row["exclusion_id"] for row in exclusion_rows]
    exclusion_paths = [row["candidate_path"] for row in exclusion_rows]

    for label, values in (
        ("source_id", source_ids),
        ("source_path", source_paths),
        ("exclusion_id", exclusion_ids),
        ("candidate_path", exclusion_paths),
    ):
        duplicates = sorted(value for value in set(values) if values.count(value) > 1)
        for duplicate in duplicates:
            errors.append(f"duplicate {label}: {duplicate}")

    rows_by_id = {row["source_id"]: row for row in manifest_rows}
    rows_by_path = {row["source_path"]: row for row in manifest_rows}
    selected_rows = [row for row in manifest_rows if row["selection_decision"] in SELECTED_DECISIONS]
    exact_rows = [row for row in selected_rows if row["selection_decision"] == "include_exact"]
    support_rows = [row for row in selected_rows if row["selection_decision"] == "include_support_evidence"]

    source_bytes_by_id: dict[str, bytes] = {}
    for row in manifest_rows:
        label = row["source_id"]
        required_fields = [
            "source_id",
            "source_origin",
            "source_path",
            "source_role",
            "source_family",
            "title",
            "version_scope",
            "language",
            "authority_label",
            "selection_decision",
            "extraction_mode",
            "source_sha256",
            "byte_count",
            "line_count",
            "estimated_tokens",
            "selected_by_job",
            "last_verified_job",
        ]
        for field in required_fields:
            if not row[field]:
                errors.append(f"{label}: required source_manifest field {field} is blank")
        if row["source_origin"] not in ALLOWED_ORIGINS:
            errors.append(f"{label}: invalid source_origin {row['source_origin']!r}")
        if row["selection_decision"] not in SELECTED_DECISIONS:
            errors.append(f"{label}: invalid selection_decision {row['selection_decision']!r}")
        if row["source_path"].startswith("/"):
            errors.append(f"{label}: source_path must be portable, not absolute: {row['source_path']}")
        if row["source_origin"] == "aid":
            if not (row["source_path"].startswith("~/AID/") or row["source_path"].startswith("AID:")):
                errors.append(f"{label}: AID source path must use ~/AID/ or AID: {row['source_path']}")
            if not row["aid_classification"]:
                errors.append(f"{label}: AID row lacks aid_classification")
            if not row["classification_evidence"]:
                errors.append(f"{label}: AID row lacks classification_evidence")
        if row["source_path"].startswith("GPTs/reports/"):
            if row["source_role"] != "support_evidence":
                errors.append(f"{label}: GPTs/reports source is not support_evidence")
            if row["selection_decision"] != "include_support_evidence":
                errors.append(f"{label}: GPTs/reports source must use include_support_evidence")
            if not row["classification_evidence"]:
                errors.append(f"{label}: support evidence lacks classification_evidence")

        source_path = full_path_for(row["source_path"])
        if not source_path.exists():
            errors.append(f"{label}: source file does not exist: {row['source_path']}")
            continue
        data = source_path.read_bytes()
        try:
            data.decode("utf-8")
        except UnicodeDecodeError as exc:
            errors.append(f"{label}: source file is not UTF-8 decodable: {exc}")
            continue
        source_bytes_by_id[label] = data
        stats = FileStats(
            sha256=hashlib.sha256(data).hexdigest(),
            byte_count=len(data),
            line_count=line_count(data),
            estimated_tokens=estimated_tokens(data),
        )
        expected_stats = {
            "source_sha256": stats.sha256,
            "byte_count": str(stats.byte_count),
            "line_count": str(stats.line_count),
            "estimated_tokens": str(stats.estimated_tokens),
        }
        for field, actual in expected_stats.items():
            if row[field] != actual:
                errors.append(f"{label}: {field} mismatch: manifest={row[field]} actual={actual}")

    included_path_set = set(source_paths)
    exclusion_path_set = set(exclusion_paths)
    for source_root in SOURCE_ROOTS:
        root_path = ROOT / source_root
        if not root_path.exists():
            errors.append(f"candidate source root missing: {source_root}")
            continue
        for candidate in sorted(path.relative_to(ROOT).as_posix() for path in root_path.rglob("*") if path.is_file()):
            if candidate not in included_path_set and candidate not in exclusion_path_set:
                errors.append(f"source candidate is neither included nor excluded: {candidate}")

    for row in exclusion_rows:
        label = row["exclusion_id"]
        for field in (
            "exclusion_id",
            "candidate_origin",
            "candidate_path",
            "source_family",
            "version_scope",
            "language",
            "exclusion_type",
            "exclusion_reason",
            "evidence_ref",
            "risk_label",
            "selected_by_job",
            "review_status",
        ):
            if not row[field]:
                errors.append(f"{label}: required source_exclusion_register field {field} is blank")
        if row["review_status"] not in ALLOWED_EXCLUSION_STATUSES:
            errors.append(f"{label}: invalid review_status {row['review_status']!r}")
        if row["candidate_path"] in included_path_set and row["review_status"] != "superseded":
            errors.append(f"{label}: candidate is both included and excluded: {row['candidate_path']}")
        if row["exclusion_type"] == "duplicate" and not row["replacement_source_id"]:
            errors.append(f"{label}: duplicate exclusion lacks replacement_source_id")
        if not full_path_for(row["candidate_path"]).exists():
            errors.append(f"{label}: excluded candidate path does not exist: {row['candidate_path']}")

    mapped_ids = [row["source_id"] for row in shard_rows]
    mapped_duplicates = sorted(source_id for source_id in set(mapped_ids) if mapped_ids.count(source_id) > 1)
    for source_id in mapped_duplicates:
        errors.append(f"source_to_shard_manifest maps source_id more than once: {source_id}")

    selected_ids = {row["source_id"] for row in selected_rows}
    mapped_id_set = set(mapped_ids)
    for source_id in sorted(selected_ids - mapped_id_set):
        errors.append(f"selected source is missing from source_to_shard_manifest: {source_id}")
    for source_id in sorted(mapped_id_set - selected_ids):
        errors.append(f"source_to_shard_manifest includes non-selected source: {source_id}")

    expected_order = [row["source_id"] for row in sorted(selected_rows, key=source_sort_key)]
    actual_order = [row["source_id"] for row in sorted(shard_rows, key=shard_sort_key)]
    if actual_order != expected_order:
        errors.append("source_to_shard_manifest order does not match deterministic source sort order")

    block_ids = [row["block_id"] for row in shard_rows]
    block_duplicates = sorted(block_id for block_id in set(block_ids) if block_ids.count(block_id) > 1)
    for block_id in block_duplicates:
        errors.append(f"duplicate block_id in source_to_shard_manifest: {block_id}")

    shard_paths = {row["shard_path"] for row in shard_rows}
    actual_shards = {path.relative_to(ROOT).as_posix() for path in (ROOT / SOURCE_PACK_DIR).glob("source_pack_shard_*.md")}
    for shard_path in sorted(shard_paths - actual_shards):
        errors.append(f"source_to_shard_manifest references missing shard: {shard_path}")
    for shard_path in sorted(actual_shards - shard_paths):
        errors.append(f"source-pack shard is not referenced by source_to_shard_manifest: {shard_path}")

    shard_blocks: dict[tuple[str, str], ShardBlock] = {}
    source_blocks: dict[str, list[ShardBlock]] = defaultdict(list)
    for shard_path in sorted(shard_paths):
        for block in parse_shard_blocks(shard_path, errors):
            key = (block.source_id, block.block_id)
            if key in shard_blocks:
                errors.append(f"duplicate source block in shards: {block.source_id} {block.block_id}")
            shard_blocks[key] = block
            source_blocks[block.source_id].append(block)

    for source_id, blocks in sorted(source_blocks.items()):
        if len(blocks) != 1:
            errors.append(f"{source_id}: appears in {len(blocks)} parsed source blocks")

    shard_rows_by_path: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in shard_rows:
        shard_rows_by_path[row["shard_path"]].append(row)
        label = row["source_id"]
        manifest_row = rows_by_id.get(label)
        if not manifest_row:
            continue
        if row["source_sha256"] != manifest_row["source_sha256"]:
            errors.append(f"{label}: source_to_shard source_sha256 does not match source_manifest")
        if row["extracted_body_sha256"] != manifest_row["source_sha256"]:
            errors.append(f"{label}: extracted_body_sha256 does not match source_manifest source_sha256")
        if row["upload_intended"] not in ALLOWED_UPLOAD_STATES:
            errors.append(f"{label}: invalid upload_intended {row['upload_intended']!r}")
        if row["validation_status"] not in ALLOWED_VALIDATION_STATUSES:
            errors.append(f"{label}: invalid validation_status {row['validation_status']!r}")
        if row["validation_status"] != "pass" and "not-ready" not in row["notes"].lower():
            errors.append(f"{label}: validation_status is not pass and notes do not mark not-ready")
        if row["source_start_line"] != "1":
            errors.append(f"{label}: source_start_line must be 1 for whole-file extraction")
        if row["source_end_line"] != manifest_row["line_count"]:
            errors.append(f"{label}: source_end_line does not match manifest line_count")
        numeric_matches = {
            "block_byte_count": manifest_row["byte_count"],
            "block_line_count": manifest_row["line_count"],
            "block_estimated_tokens": manifest_row["estimated_tokens"],
        }
        for field, expected in numeric_matches.items():
            if row[field] != expected:
                errors.append(f"{label}: {field} mismatch: shard={row[field]} manifest={expected}")

        block = shard_blocks.get((label, row["block_id"]))
        if not block:
            errors.append(f"{label}: shard block {row['block_id']} not found in {row['shard_path']}")
            continue
        source_bytes = source_bytes_by_id.get(label)
        if source_bytes is not None and block.body != source_bytes:
            errors.append(f"{label}: extracted source block bytes differ from original source file")
        block_stats = FileStats(
            sha256=hashlib.sha256(block.body).hexdigest(),
            byte_count=len(block.body),
            line_count=line_count(block.body),
            estimated_tokens=estimated_tokens(block.body),
        )
        block_expected = {
            "extracted_body_sha256": block_stats.sha256,
            "block_byte_count": str(block_stats.byte_count),
            "block_line_count": str(block_stats.line_count),
            "block_estimated_tokens": str(block_stats.estimated_tokens),
        }
        for field, actual in block_expected.items():
            if row[field] != actual:
                errors.append(f"{label}: {field} mismatch against parsed source block: row={row[field]} actual={actual}")
        expected_attrs = {
            "source_id": label,
            "source_path": manifest_row["source_path"],
            "source_family": manifest_row["source_family"],
            "version_scope": manifest_row["version_scope"],
            "language": manifest_row["language"],
            "authority_label": manifest_row["authority_label"],
            "sha256": manifest_row["source_sha256"],
            "byte_count": manifest_row["byte_count"],
            "line_count": manifest_row["line_count"],
            "estimated_tokens": manifest_row["estimated_tokens"],
            "block_id": row["block_id"],
        }
        for attr_name, expected in expected_attrs.items():
            actual = block.attrs.get(attr_name, "")
            if actual != expected:
                errors.append(f"{label}: SOURCE_BLOCK_BEGIN attr {attr_name} mismatch: {actual!r} != {expected!r}")

    shard_summaries: list[ShardSummary] = []
    upload_candidate_paths: set[str] = set()
    upload_not_ready: list[str] = []

    for shard_path, rows in sorted(shard_rows_by_path.items()):
        sorted_rows = sorted(rows, key=lambda row: int_field(row, "order_in_shard", errors, row["source_id"]))
        expected_orders = list(range(1, len(sorted_rows) + 1))
        actual_orders = [int_field(row, "order_in_shard", errors, row["source_id"]) for row in sorted_rows]
        if actual_orders != expected_orders:
            errors.append(f"{shard_path}: order_in_shard values are not contiguous from 1")

        upload_states = {row["upload_intended"] for row in rows}
        upload_state = next(iter(upload_states)) if len(upload_states) == 1 else "mixed"
        if upload_state == "mixed":
            errors.append(f"{shard_path}: mixed upload_intended states are not allowed")
        header_upload_state = read_shard_upload_header(shard_path)
        if header_upload_state != upload_state:
            errors.append(f"{shard_path}: upload header {header_upload_state!r} does not match manifest {upload_state!r}")

        shard_content = (ROOT / shard_path).read_bytes()
        shard_tokens = estimated_tokens(shard_content)
        for row in rows:
            if row["shard_estimated_tokens"] != str(shard_tokens):
                errors.append(f"{row['source_id']}: shard_estimated_tokens mismatch: row={row['shard_estimated_tokens']} actual={shard_tokens}")

        validation_status = "pass" if all(row["validation_status"] == "pass" for row in rows) else "not-ready"
        first_row = sorted_rows[0]
        last_row = sorted_rows[-1]
        shard_summaries.append(
            ShardSummary(
                shard_id=first_row["shard_id"],
                shard_path=shard_path,
                source_count=len(rows),
                byte_count=len(shard_content),
                estimated_tokens=shard_tokens,
                upload_intended=upload_state,
                first_source_id=first_row["source_id"],
                last_source_id=last_row["source_id"],
                first_family=rows_by_id[first_row["source_id"]]["source_family"],
                last_family=rows_by_id[last_row["source_id"]]["source_family"],
                validation_status=validation_status,
            )
        )

        if upload_state in {"yes", "candidate"}:
            upload_candidate_paths.add(shard_path)
            size_ready = len(shard_content) <= UPLOAD_MARGIN_BYTES
            token_ready = shard_tokens <= UPLOAD_MARGIN_TOKENS
            marked_not_ready = any("not-ready" in row["notes"].lower() or "not ready" in row["notes"].lower() for row in rows)
            if not (size_ready and token_ready):
                message = (
                    f"{shard_path}: upload candidate exceeds margin "
                    f"({len(shard_content)} bytes, {shard_tokens} estimated tokens)"
                )
                if marked_not_ready:
                    upload_not_ready.append(message)
                else:
                    errors.append(message)

    if len(upload_candidate_paths) > GPT_KNOWLEDGE_FILE_COUNT_LIMIT:
        errors.append(
            "upload-intended source-pack shards exceed the global GPT Knowledge "
            f"file-count limit: {len(upload_candidate_paths)} > {GPT_KNOWLEDGE_FILE_COUNT_LIMIT}"
        )

    return ValidationResult(
        errors=errors,
        warnings=warnings,
        command_summaries=command_summaries,
        manifest_rows=manifest_rows,
        selected_rows=selected_rows,
        exact_rows=exact_rows,
        support_rows=support_rows,
        exclusion_rows=exclusion_rows,
        shard_rows=shard_rows,
        shard_summaries=shard_summaries,
        upload_candidate_paths=upload_candidate_paths,
        upload_not_ready=upload_not_ready,
    )


def fmt_int(value: int) -> str:
    return f"{value:,}"


def fmt_mib(value: int) -> str:
    return f"{value / (1024 * 1024):.2f} MiB"


def render_validation_note(result: ValidationResult) -> str:
    status = "not-ready" if result.errors else "pass"
    verdict = "Not Ready" if result.errors else "Pass"
    total_source_bytes = sum(int(row["byte_count"]) for row in result.selected_rows)
    total_source_tokens = sum(int(row["estimated_tokens"]) for row in result.selected_rows)
    total_shard_bytes = sum(summary.byte_count for summary in result.shard_summaries)
    max_shard = max(result.shard_summaries, key=lambda item: item.estimated_tokens, default=None)
    max_shard_by_size = max(result.shard_summaries, key=lambda item: item.byte_count, default=None)
    upload_rows = sorted(result.upload_candidate_paths)

    check_rows = [
        ("Source manifest currentness", "Pass" if not any("build_source_manifest.py" in err for err in result.errors) else "Fail", result.command_summaries[0]),
        ("Shard generator currentness", "Pass" if not any("build_source_pack.py" in err for err in result.errors) else "Fail", result.command_summaries[1]),
        ("Selected source coverage", "Pass" if not result.errors else "See blockers", f"{fmt_int(len(result.selected_rows))} selected sources mapped"),
        ("Exclusion reasons", "Pass" if not result.errors else "See blockers", f"{fmt_int(len(result.exclusion_rows))} excluded candidates checked"),
        ("Exact extraction checksums", "Pass" if not result.errors else "See blockers", f"{fmt_int(len(result.shard_rows))} source blocks parsed and hashed"),
        ("Upload margin gate", "Pass" if not result.upload_not_ready and not result.errors else "Not Ready", f"{fmt_int(len(upload_rows))} upload-intended shard candidates"),
    ]

    lines = [
        "# Source Pack Validation",
        "",
        f"- Job: `{JOB_ID}`",
        f"- Last verified: {JOB_DATE}",
        f"- Status: `{status}`",
        f"- Validation command: `python3 GPTs/source_pack/scripts/validate_source_pack.py --check`",
        "",
        "## Reconfirmed Requirement And Boundary",
        "",
        "`S1-J005` validates the Stage 1 source-pack evidence layer only. It checks",
        "`GPTs/source_pack/source_manifest.tsv`, `source_exclusion_register.tsv`,",
        "`source_to_shard_manifest.tsv`, and the committed `source_pack_shard_*.md`",
        "files. It does not generate the Korean-aligned English baseline, edit",
        "`GPTs/attachments/`, or assemble `GPTs/upload_package/`.",
        "",
        "## Design Note",
        "",
        "The validator treats the committed source pack as the evidence artifact under",
        "test. It first runs the deterministic manifest and shard builders in `--check`",
        "mode, then independently parses every committed source block and hashes the",
        "body between `SOURCE_BLOCK_BEGIN` and `SOURCE_BLOCK_END`. This keeps exact",
        "source preservation separate from later baseline, playbook, attachment, and",
        "upload-package generation.",
        "",
        "## Verdict",
        "",
        f"Verdict: {verdict}",
        "",
    ]

    if result.errors:
        lines.extend(["### Not-Ready Blockers", ""])
        lines.extend(f"- {error}" for error in result.errors)
        lines.append("")
    else:
        lines.extend(
            [
                "No source-pack validation blockers were found. Do not proceed to the",
                "Korean-aligned English baseline from an unvalidated or locally modified",
                "source pack; rerun the command above after any source, manifest, or shard",
                "change.",
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
    lines.extend(f"| {name} | {state} | {evidence} |" for name, state, evidence in check_rows)
    lines.extend(
        [
            "",
            "## Corpus Summary",
            "",
            "| Metric | Value |",
            "| --- | ---: |",
            f"| Source manifest rows | {fmt_int(len(result.manifest_rows))} |",
            f"| Selected rows | {fmt_int(len(result.selected_rows))} |",
            f"| Exact source rows | {fmt_int(len(result.exact_rows))} |",
            f"| Support-evidence rows | {fmt_int(len(result.support_rows))} |",
            f"| Exclusion rows | {fmt_int(len(result.exclusion_rows))} |",
            f"| Source-to-shard rows | {fmt_int(len(result.shard_rows))} |",
            f"| Source-pack shards | {fmt_int(len(result.shard_summaries))} |",
            f"| Selected source bytes | {fmt_int(total_source_bytes)} |",
            f"| Selected source estimated tokens | {fmt_int(total_source_tokens)} |",
            f"| Shard bytes including wrappers | {fmt_int(total_shard_bytes)} |",
            "| Largest shard by tokens | "
            + (f"`{max_shard.shard_path}` ({fmt_int(max_shard.estimated_tokens)})" if max_shard else "not available")
            + " |",
            "| Largest shard by bytes | "
            + (f"`{max_shard_by_size.shard_path}` ({fmt_mib(max_shard_by_size.byte_count)})" if max_shard_by_size else "not available")
            + " |",
            "",
            "## Upload-Intended Shard Gate",
            "",
            "Current Stage 1 planning constants for GPT Knowledge upload validation are:",
            "",
            "| Limit | Value | Margin used here |",
            "| --- | ---: | ---: |",
            f"| Markdown file count | {GPT_KNOWLEDGE_FILE_COUNT_LIMIT} | {GPT_KNOWLEDGE_FILE_COUNT_LIMIT} |",
            f"| File size | {fmt_mib(GPT_KNOWLEDGE_FILE_SIZE_LIMIT_BYTES)} | {fmt_mib(UPLOAD_MARGIN_BYTES)} |",
            f"| Estimated tokens per file | {fmt_int(GPT_KNOWLEDGE_FILE_TOKEN_LIMIT)} | {fmt_int(UPLOAD_MARGIN_TOKENS)} |",
            "",
        ]
    )

    if upload_rows:
        lines.extend(
            [
                "Upload-intended source-pack shard candidates:",
                "",
                "| Shard path | Status |",
                "| --- | --- |",
            ]
        )
        for shard_path in upload_rows:
            summary = next(item for item in result.shard_summaries if item.shard_path == shard_path)
            state = "ready-with-margin" if summary.byte_count <= UPLOAD_MARGIN_BYTES and summary.estimated_tokens <= UPLOAD_MARGIN_TOKENS else "not-ready"
            lines.append(f"| `{shard_path}` | {state} |")
        lines.append("")
    else:
        lines.extend(
            [
                "No source-pack shard is currently upload-intended. Every committed shard is",
                "marked `upload_intended=no`, so direct GPT Knowledge upload of the source",
                "pack is not-ready by policy until a later upload-package job intentionally",
                "copies or transforms selected content into `GPTs/upload_package/` and counts",
                "it against the global 20 Markdown file limit.",
                "",
            ]
        )

    if result.upload_not_ready:
        lines.extend(["Not-ready upload candidates explicitly recorded:", ""])
        lines.extend(f"- {item}" for item in result.upload_not_ready)
        lines.append("")

    lines.extend(
        [
            "## Required Verification Commands",
            "",
            "```bash",
            "python3 GPTs/source_pack/scripts/validate_source_pack.py --check",
            "git diff --check -- GPTs/source_pack",
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def render_upload_order(result: ValidationResult) -> str:
    lines = [
        "# Source Pack Upload Order Guidance",
        "",
        f"- Job: `{JOB_ID}`",
        f"- Last verified: {JOB_DATE}",
        "- Status: guidance only; not a final GPT Knowledge upload manifest",
        "",
        "## Boundary",
        "",
        "`GPTs/source_pack/` is a source-preserving evidence layer. The shard files below",
        "are not final upload files, and they must not be uploaded beside the current",
        "attachments as an additional package. Anything later copied or transformed into",
        "`GPTs/upload_package/` must count against the same global 20 Markdown file",
        "limit, including AID-derived content.",
        "",
        "## Current Source-Pack Order",
        "",
        "Use this order when a reviewer or downstream packaging job needs to inspect the",
        "source-pack shards. It follows the deterministic shard IDs written in",
        "`source_to_shard_manifest.tsv`.",
        "",
        "| Order | Shard | Sources | Size | Estimated tokens | Upload state | Source-family span |",
        "| ---: | --- | ---: | ---: | ---: | --- | --- |",
    ]
    for index, summary in enumerate(sorted(result.shard_summaries, key=lambda item: item.shard_id), start=1):
        family_span = summary.first_family if summary.first_family == summary.last_family else f"{summary.first_family} to {summary.last_family}"
        lines.append(
            f"| {index} | `{summary.shard_path}` | {fmt_int(summary.source_count)} | "
            f"{fmt_mib(summary.byte_count)} | {fmt_int(summary.estimated_tokens)} | "
            f"`{summary.upload_intended}` | {family_span} |"
        )
    lines.extend(
        [
            "",
            "## Upload Guidance",
            "",
            "- Stage 1 source-pack shards are direct-upload not-ready because they are",
            "  evidence artifacts marked `upload_intended=no`.",
            "- A later upload-package job may transform or copy selected evidence into",
            "  `GPTs/upload_package/`; that job must rerun size, token, and 20-file count",
            "  validation on the final package.",
            "- If a shard is ever changed to `upload_intended=yes` or `candidate`, it must",
            "  stay below the validation margin of 90% of 512 MiB and 90% of 2,000,000",
            "  estimated tokens, or its shard manifest notes must mark it `not-ready`.",
            "",
        ]
    )
    return "\n".join(lines)


def render_gpt_instruction_note(result: ValidationResult) -> str:
    lines = [
        "# Source Pack GPT Instruction Note",
        "",
        f"- Job: `{JOB_ID}`",
        f"- Last verified: {JOB_DATE}",
        "- Status: source-pack instruction note",
        "",
        "## Use Policy",
        "",
        "When source-pack content or source IDs are available to a GPT, LLM, or coding",
        "agent, use these rules:",
        "",
        "- Treat `GPTs/source_pack/` as exact evidence, not as the final customer-facing",
        "  upload package unless a later upload manifest explicitly selects it.",
        "- Prefer answer-ready attachments and playbooks for normal customer answers, then",
        "  use source-pack source IDs to verify exact manual text, low-frequency tokens,",
        "  examples, commands, SQL, configuration names, errors, and version boundaries.",
        "- Preserve source IDs, source paths, version scope, language, authority label, and",
        "  AID classification labels when citing or transforming source-pack evidence.",
        "- For repository-local Korean/English conflicts, apply the active source policy:",
        "  Korean Altibase manuals are authoritative, while English manuals may be",
        "  extraction aids unless a stronger source label is recorded.",
        "- For AID-derived material, preserve Korean-source-verified, link-validated,",
        "  English-only auxiliary, evidence-only, and accepted-limitation boundaries.",
        "- Do not infer Altibase behavior from Oracle, generic SQL, generic ODBC/JDBC,",
        "  Kubernetes, or third-party assumptions when source-pack evidence is absent.",
        "- If an answer depends on patch level, platform, installed output, object DDL,",
        "  logs, runtime state, unsupported behavior, or customer environment, ask for",
        "  that input and give the safest source-backed next check instead of inventing a",
        "  definitive answer.",
        "- Do not upload all source-pack shards alongside attachments. The final GPT",
        "  Knowledge upload package must remain 20 Markdown files or fewer including",
        "  AID-derived content.",
        "",
        "## Validation Reference",
        "",
        "The committed source pack currently validates "
        f"{fmt_int(len(result.selected_rows))} selected source rows across "
        f"{fmt_int(len(result.shard_summaries))} shards with exact body checksums. "
        "Rerun this command after any source-pack change:",
        "",
        "```bash",
        "python3 GPTs/source_pack/scripts/validate_source_pack.py --check",
        "```",
        "",
    ]
    return "\n".join(lines)


def write_if_requested(result: ValidationResult, *, check: bool, write: bool) -> int:
    rendered = {
        VALIDATION_NOTE_PATH: render_validation_note(result),
        UPLOAD_ORDER_PATH: render_upload_order(result),
        GPT_INSTRUCTION_NOTE_PATH: render_gpt_instruction_note(result),
    }
    if write:
        for path, content in rendered.items():
            (ROOT / path).write_text(content, encoding="utf-8", newline="\n")
        return 0

    if check:
        ok = True
        for path, expected in rendered.items():
            full_path = ROOT / path
            if not full_path.exists():
                print(f"missing generated note: {path}", file=sys.stderr)
                ok = False
                continue
            actual = full_path.read_text(encoding="utf-8")
            if actual != expected:
                print(f"generated note is stale: {path}", file=sys.stderr)
                ok = False
        return 0 if ok else 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write validation and guidance notes")
    parser.add_argument("--check", action="store_true", help="validate notes are current")
    args = parser.parse_args()

    if args.write and args.check:
        parser.error("--write and --check are mutually exclusive")
    if not args.write and not args.check:
        args.check = True

    result = validate_source_pack()
    notes_status = write_if_requested(result, check=args.check, write=args.write)

    if result.errors:
        for error in result.errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    if notes_status != 0:
        return notes_status

    print(
        "validated source pack: "
        f"{len(result.selected_rows)} selected sources, "
        f"{len(result.shard_summaries)} shards, "
        f"{len(result.exclusion_rows)} exclusions"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
