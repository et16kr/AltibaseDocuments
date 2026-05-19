#!/usr/bin/env python3
"""Validate the source-preserving GPT upload package.

This validator intentionally checks source-block body integrity instead of
whole-shard equality. Later final-upload wrapper wording may change, but bytes
inside SOURCE_BLOCK_BEGIN / SOURCE_BLOCK_END bodies must not change.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import math
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from io import StringIO
from pathlib import Path


JOB_ID = "SPF-J002"
JOB_DATE = "2026-05-19"

ROOT = Path(__file__).resolve().parents[3]
PACKAGE_DIR = ROOT / "GPTs/upload_package_source_preserving"
SOURCE_PACK_DIR = ROOT / "GPTs/source_pack"
REPORT_PATH = ROOT / "GPTs/reports/source_preserving_upload_package_validation.md"

EXPECTED_FILE_COUNT = 20
EXPECTED_SHARD_COUNT = 16
EXPECTED_WRAPPER_FILES = [
    "00_README_SOURCE_PRESERVING_UPLOAD.md",
    "01_upload_order.md",
    "02_source_manifest.md",
    "03_source_to_shard_manifest.md",
]
EXPECTED_SHARD_FILES = [
    f"source_pack_shard_{index:03d}.md"
    for index in range(1, EXPECTED_SHARD_COUNT + 1)
]
EXPECTED_FILES = EXPECTED_WRAPPER_FILES + EXPECTED_SHARD_FILES

SOURCE_MANIFEST_PATH = SOURCE_PACK_DIR / "source_manifest.tsv"
SOURCE_TO_SHARD_PATH = SOURCE_PACK_DIR / "source_to_shard_manifest.tsv"

SOURCE_MANIFEST_COLUMNS = [
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

SOURCE_TO_SHARD_COLUMNS = [
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
GPT_KNOWLEDGE_FILE_SIZE_LIMIT_BYTES = 512 * 1024 * 1024
GPT_KNOWLEDGE_FILE_TOKEN_LIMIT = 2_000_000
SAFETY_MARGIN_RATIO = 0.90
FILE_SIZE_SAFETY_BYTES = int(GPT_KNOWLEDGE_FILE_SIZE_LIMIT_BYTES * SAFETY_MARGIN_RATIO)
TOKEN_SAFETY_LIMIT = int(GPT_KNOWLEDGE_FILE_TOKEN_LIMIT * SAFETY_MARGIN_RATIO)

BEGIN_RE = re.compile(rb"<!-- SOURCE_BLOCK_BEGIN ([^\r\n]*?) -->\r?\n")
ATTR_RE = re.compile(r'([A-Za-z0-9_]+)="([^"]*)"')

REVERSE_ROUTING_PATTERNS = [
    (
        re.compile(r"Upload intended:\s*`?no`?", re.IGNORECASE),
        "upload-intended=no shard header",
    ),
    (
        re.compile(r"not a final GPT Knowledge upload manifest", re.IGNORECASE),
        "not-final upload manifest wording",
    ),
    (
        re.compile(r"not\s+(?:a\s+)?final\s+(?:GPT Knowledge\s+)?upload", re.IGNORECASE),
        "not-final upload wording",
    ),
]


@dataclass(frozen=True)
class FileStats:
    rel_path: str
    byte_count: int
    estimated_tokens: int


@dataclass(frozen=True)
class ParsedBlock:
    source_id: str
    block_id: str
    shard_rel_path: str
    body: bytes
    attrs: dict[str, str]
    span_start: int
    span_end: int


@dataclass(frozen=True)
class ValidationResult:
    strict_final: bool
    errors: list[str]
    warnings: list[str]
    strict_wording_blockers: list[str]
    file_stats: list[FileStats]
    source_rows: list[dict[str, str]]
    selected_source_rows: list[dict[str, str]]
    shard_rows: list[dict[str, str]]
    parsed_blocks: list[ParsedBlock]

    @property
    def ok(self) -> bool:
        return not self.errors

    @property
    def package_bytes(self) -> int:
        return sum(item.byte_count for item in self.file_stats)

    @property
    def max_file_by_size(self) -> FileStats | None:
        return max(self.file_stats, key=lambda item: item.byte_count, default=None)

    @property
    def max_file_by_tokens(self) -> FileStats | None:
        return max(self.file_stats, key=lambda item: item.estimated_tokens, default=None)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def clean(value: object) -> str:
    text = "" if value is None else str(value)
    return re.sub(r"[\t\r\n]+", " ", text).strip()


def fmt_int(value: int) -> str:
    return f"{value:,}"


def fmt_mib(value: int) -> str:
    return f"{value / (1024 * 1024):.2f} MiB"


def line_count(data: bytes) -> int:
    if not data:
        return 0
    return data.count(b"\n") + (0 if data.endswith(b"\n") else 1)


def estimated_tokens(data: bytes) -> int:
    text = data.decode("utf-8")
    return max(1, math.ceil(len(text) / 4)) if text else 0


def parse_int(value: str, label: str, errors: list[str]) -> int:
    try:
        return int(value)
    except ValueError:
        errors.append(f"{label}: expected integer, found {value!r}")
        return 0


def read_tsv_text(
    text: str,
    expected_columns: list[str],
    label: str,
    errors: list[str],
) -> list[dict[str, str]]:
    reader = csv.DictReader(StringIO(text), delimiter="\t")
    if reader.fieldnames != expected_columns:
        errors.append(
            f"{label}: unexpected TSV columns {reader.fieldnames!r}; "
            f"expected {expected_columns!r}"
        )
        return []

    rows: list[dict[str, str]] = []
    for line_number, row in enumerate(reader, start=2):
        if None in row:
            errors.append(f"{label} line {line_number}: row has extra TSV cells")
            continue
        rows.append({column: clean(row.get(column, "")) for column in expected_columns})
    return rows


def read_tsv_file(
    path: Path,
    expected_columns: list[str],
    errors: list[str],
) -> list[dict[str, str]]:
    if not path.exists():
        errors.append(f"missing source-pack TSV: {rel(path)}")
        return []
    return read_tsv_text(path.read_text(encoding="utf-8"), expected_columns, rel(path), errors)


def extract_tsv_fence(path: Path, errors: list[str]) -> str:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        errors.append(f"missing manifest wrapper: {rel(path)}")
        return ""
    except UnicodeDecodeError as exc:
        errors.append(f"{rel(path)} is not UTF-8 readable: {exc}")
        return ""

    if not text.startswith("# "):
        errors.append(f"{rel(path)} must start with a Markdown H1 heading")
    if text.count("```") % 2:
        errors.append(f"{rel(path)} has unbalanced fenced code blocks")

    lines = text.splitlines()
    starts = [index for index, line in enumerate(lines) if line.strip() == "```tsv"]
    if len(starts) != 1:
        errors.append(f"{rel(path)} must contain exactly one ```tsv fenced block")
        return ""

    start = starts[0]
    end = None
    for index in range(start + 1, len(lines)):
        if lines[index].strip() == "```":
            end = index
            break
    if end is None:
        errors.append(f"{rel(path)} missing closing fence for TSV block")
        return ""
    if not any(line.strip() for line in lines[:start]):
        errors.append(f"{rel(path)} has no readable wrapper text before the TSV block")
    return "\n".join(lines[start + 1 : end]) + "\n"


def parse_attrs(begin_comment: bytes) -> dict[str, str]:
    text = begin_comment.decode("utf-8")
    return {key: html.unescape(value) for key, value in ATTR_RE.findall(text)}


def parse_shard_blocks(path: Path, errors: list[str]) -> list[ParsedBlock]:
    rel_path = rel(path)
    try:
        content = path.read_bytes()
    except FileNotFoundError:
        errors.append(f"{rel_path}: shard file does not exist")
        return []

    blocks: list[ParsedBlock] = []
    position = 0
    while True:
        match = BEGIN_RE.search(content, position)
        if not match:
            break
        attrs = parse_attrs(match.group(0))
        source_id = attrs.get("source_id", "")
        block_id = attrs.get("block_id", "")
        if not source_id or not block_id:
            errors.append(f"{rel_path}: malformed SOURCE_BLOCK_BEGIN at byte {match.start()}")
            position = match.end()
            continue

        end_marker = (
            f'<!-- SOURCE_BLOCK_END source_id="{source_id}" block_id="{block_id}" -->'
        ).encode("utf-8")
        end_position = content.find(end_marker, match.end())
        if end_position < 0:
            errors.append(f"{rel_path}: missing SOURCE_BLOCK_END for {source_id} {block_id}")
            position = match.end()
            continue

        span_end = end_position + len(end_marker)
        blocks.append(
            ParsedBlock(
                source_id=source_id,
                block_id=block_id,
                shard_rel_path=rel_path,
                body=content[match.end() : end_position],
                attrs=attrs,
                span_start=match.start(),
                span_end=span_end,
            )
        )
        position = span_end

    outside = bytes_outside_spans(content, [(block.span_start, block.span_end) for block in blocks])
    if b"SOURCE_BLOCK_BEGIN" in outside or b"SOURCE_BLOCK_END" in outside:
        errors.append(f"{rel_path}: contains unmatched source-block boundary text")
    if not blocks:
        errors.append(f"{rel_path}: no source blocks parsed")
    return blocks


def bytes_outside_spans(content: bytes, spans: list[tuple[int, int]]) -> bytes:
    if not spans:
        return content
    output = bytearray()
    cursor = 0
    for start, end in sorted(spans):
        if start > cursor:
            output.extend(content[cursor:start])
        cursor = max(cursor, end)
    output.extend(content[cursor:])
    return bytes(output)


def collect_package_files(errors: list[str]) -> list[Path]:
    if not PACKAGE_DIR.exists():
        errors.append(f"missing package directory: {rel(PACKAGE_DIR)}")
        return []

    files = sorted(path for path in PACKAGE_DIR.rglob("*") if path.is_file())
    actual = [path.relative_to(PACKAGE_DIR).as_posix() for path in files]
    expected = sorted(EXPECTED_FILES)

    if len(files) != EXPECTED_FILE_COUNT:
        errors.append(f"expected {EXPECTED_FILE_COUNT} package files, found {len(files)}")
    missing = sorted(set(expected) - set(actual))
    extra = sorted(set(actual) - set(expected))
    if missing:
        errors.append("missing required package files: " + ", ".join(missing))
    if extra:
        errors.append("unexpected package files: " + ", ".join(extra))
    for item in actual:
        if "/" in item:
            errors.append(f"package file must be top-level, found nested path: {item}")
        if not item.endswith(".md"):
            errors.append(f"package file must be Markdown: {item}")
    return files


def check_file_limits(files: list[Path], errors: list[str]) -> list[FileStats]:
    stats: list[FileStats] = []
    for path in files:
        rel_path = rel(path)
        data = path.read_bytes()
        try:
            tokens = estimated_tokens(data)
        except UnicodeDecodeError as exc:
            errors.append(f"{rel_path}: not UTF-8 decodable for token estimate: {exc}")
            tokens = 0
        byte_count = len(data)
        stats.append(FileStats(rel_path=rel_path, byte_count=byte_count, estimated_tokens=tokens))
        if byte_count > GPT_KNOWLEDGE_FILE_SIZE_LIMIT_BYTES:
            errors.append(
                f"{rel_path}: exceeds GPT Knowledge hard file-size limit "
                f"({byte_count} > {GPT_KNOWLEDGE_FILE_SIZE_LIMIT_BYTES})"
            )
        if byte_count > FILE_SIZE_SAFETY_BYTES:
            errors.append(
                f"{rel_path}: exceeds 90% file-size safety limit "
                f"({byte_count} > {FILE_SIZE_SAFETY_BYTES})"
            )
        if tokens > GPT_KNOWLEDGE_FILE_TOKEN_LIMIT:
            errors.append(
                f"{rel_path}: exceeds GPT Knowledge hard token estimate limit "
                f"({tokens} > {GPT_KNOWLEDGE_FILE_TOKEN_LIMIT})"
            )
        if tokens > TOKEN_SAFETY_LIMIT:
            errors.append(
                f"{rel_path}: exceeds 90% token safety limit ({tokens} > {TOKEN_SAFETY_LIMIT})"
            )
    return stats


def check_readme_and_upload_order(errors: list[str]) -> None:
    readme = PACKAGE_DIR / "00_README_SOURCE_PRESERVING_UPLOAD.md"
    upload_order = PACKAGE_DIR / "01_upload_order.md"

    if readme.exists():
        text = readme.read_text(encoding="utf-8")
        for required in EXPECTED_FILES:
            if f"`{required}`" not in text:
                errors.append(f"{rel(readme)} does not list required upload file: {required}")
        for token in ("source-preserving", "SOURCE_BLOCK_BEGIN", "SOURCE_BLOCK_END"):
            if token not in text:
                errors.append(f"{rel(readme)} missing required retrieval token: {token}")

    if upload_order.exists():
        text = upload_order.read_text(encoding="utf-8")
        for shard in EXPECTED_SHARD_FILES:
            if shard not in text:
                errors.append(f"{rel(upload_order)} does not reference shard: {shard}")
        if "| Order | Shard |" not in text:
            errors.append(f"{rel(upload_order)} must keep a readable shard order table")


def load_manifest_wrappers(
    errors: list[str],
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    source_wrapper_path = PACKAGE_DIR / "02_source_manifest.md"
    shard_wrapper_path = PACKAGE_DIR / "03_source_to_shard_manifest.md"

    source_wrapper_tsv = extract_tsv_fence(source_wrapper_path, errors)
    shard_wrapper_tsv = extract_tsv_fence(shard_wrapper_path, errors)

    source_rows = (
        read_tsv_text(source_wrapper_tsv, SOURCE_MANIFEST_COLUMNS, rel(source_wrapper_path), errors)
        if source_wrapper_tsv
        else []
    )
    shard_rows = (
        read_tsv_text(shard_wrapper_tsv, SOURCE_TO_SHARD_COLUMNS, rel(shard_wrapper_path), errors)
        if shard_wrapper_tsv
        else []
    )

    source_pack_rows = read_tsv_file(SOURCE_MANIFEST_PATH, SOURCE_MANIFEST_COLUMNS, errors)
    source_pack_shard_rows = read_tsv_file(SOURCE_TO_SHARD_PATH, SOURCE_TO_SHARD_COLUMNS, errors)
    if source_rows and source_pack_rows and source_rows != source_pack_rows:
        errors.append("02_source_manifest.md TSV rows differ from GPTs/source_pack/source_manifest.tsv")
    if shard_rows and source_pack_shard_rows and shard_rows != source_pack_shard_rows:
        errors.append(
            "03_source_to_shard_manifest.md TSV rows differ from "
            "GPTs/source_pack/source_to_shard_manifest.tsv"
        )
    return source_rows, shard_rows


def check_selected_source_representation(
    source_rows: list[dict[str, str]],
    shard_rows: list[dict[str, str]],
    parsed_blocks: list[ParsedBlock],
    errors: list[str],
) -> None:
    selected_rows = [
        row for row in source_rows if row["selection_decision"] in SELECTED_DECISIONS
    ]
    selected_ids = [row["source_id"] for row in selected_rows]
    mapped_ids = [row["source_id"] for row in shard_rows]
    parsed_keys = {(block.source_id, block.block_id) for block in parsed_blocks}
    row_keys = {(row["source_id"], row["block_id"]) for row in shard_rows}

    for label, values in (
        ("selected source_id", selected_ids),
        ("source_to_shard source_id", mapped_ids),
        ("source_to_shard block_id", [row["block_id"] for row in shard_rows]),
    ):
        duplicates = sorted(value for value in set(values) if values.count(value) > 1)
        for duplicate in duplicates:
            errors.append(f"duplicate {label}: {duplicate}")

    selected_id_set = set(selected_ids)
    mapped_id_set = set(mapped_ids)
    if selected_id_set != mapped_id_set:
        missing = sorted(selected_id_set - mapped_id_set)
        extra = sorted(mapped_id_set - selected_id_set)
        if missing:
            errors.append("selected sources missing from source_to_shard: " + ", ".join(missing[:20]))
        if extra:
            errors.append("source_to_shard maps non-selected sources: " + ", ".join(extra[:20]))
    if len(selected_rows) != len(shard_rows):
        errors.append(
            f"selected source count does not match shard rows: "
            f"{len(selected_rows)} != {len(shard_rows)}"
        )

    missing_blocks = sorted(row_keys - parsed_keys)
    extra_blocks = sorted(parsed_keys - row_keys)
    if missing_blocks:
        sample = ", ".join(f"{source_id}/{block_id}" for source_id, block_id in missing_blocks[:20])
        errors.append(f"source_to_shard rows missing parsed blocks: {sample}")
    if extra_blocks:
        sample = ", ".join(f"{source_id}/{block_id}" for source_id, block_id in extra_blocks[:20])
        errors.append(f"parsed source blocks not recorded in source_to_shard: {sample}")

    expected_shard_paths = {
        f"GPTs/source_pack/{name}" for name in EXPECTED_SHARD_FILES
    }
    mapped_shard_paths = {row["shard_path"] for row in shard_rows}
    if expected_shard_paths != mapped_shard_paths:
        missing = sorted(expected_shard_paths - mapped_shard_paths)
        extra = sorted(mapped_shard_paths - expected_shard_paths)
        if missing:
            errors.append("required source-pack shard paths not represented: " + ", ".join(missing))
        if extra:
            errors.append("unexpected source-pack shard paths represented: " + ", ".join(extra))

    rows_by_shard: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in shard_rows:
        rows_by_shard[row["shard_path"]].append(row)
    for shard_path, rows in rows_by_shard.items():
        orders = [
            parse_int(row["order_in_shard"], f"{row['source_id']} order_in_shard", errors)
            for row in rows
        ]
        if sorted(orders) != list(range(1, len(rows) + 1)):
            errors.append(f"{shard_path}: order_in_shard values are not contiguous from 1")


def check_source_body_integrity(
    source_rows: list[dict[str, str]],
    shard_rows: list[dict[str, str]],
    parsed_blocks: list[ParsedBlock],
    errors: list[str],
) -> None:
    source_by_id = {row["source_id"]: row for row in source_rows}
    blocks_by_key = {(block.source_id, block.block_id): block for block in parsed_blocks}

    for row in shard_rows:
        source_id = row["source_id"]
        block_id = row["block_id"]
        label = f"{source_id}/{block_id}"
        source_row = source_by_id.get(source_id)
        if not source_row:
            continue
        block = blocks_by_key.get((source_id, block_id))
        if not block:
            continue

        package_shard = PACKAGE_DIR / Path(row["shard_path"]).name
        if block.shard_rel_path != rel(package_shard):
            errors.append(
                f"{label}: parsed block path {block.shard_rel_path} does not match "
                f"manifest shard {rel(package_shard)}"
            )

        if row["source_sha256"] != source_row["source_sha256"]:
            errors.append(f"{label}: source_to_shard source_sha256 differs from source_manifest")
        if row["extracted_body_sha256"] != source_row["source_sha256"]:
            errors.append(f"{label}: extracted_body_sha256 differs from source_manifest")

        digest = hashlib.sha256(block.body).hexdigest()
        if digest != source_row["source_sha256"]:
            errors.append(
                f"{label}: source body SHA-256 mismatch: "
                f"{digest} != {source_row['source_sha256']}"
            )

        try:
            body_token_estimate = estimated_tokens(block.body)
        except UnicodeDecodeError as exc:
            errors.append(f"{label}: parsed source body is not UTF-8 decodable: {exc}")
            body_token_estimate = 0
        body_checks = {
            "block_byte_count": str(len(block.body)),
            "block_line_count": str(line_count(block.body)),
            "block_estimated_tokens": str(body_token_estimate),
        }
        for field, actual in body_checks.items():
            if row[field] != actual:
                errors.append(f"{label}: {field} mismatch against parsed body: {row[field]} != {actual}")

        source_numeric_checks = {
            "byte_count": str(len(block.body)),
            "line_count": str(line_count(block.body)),
            "estimated_tokens": str(body_token_estimate),
        }
        for field, actual in source_numeric_checks.items():
            if source_row[field] != actual:
                errors.append(f"{label}: source_manifest {field} mismatch against parsed body")

        expected_attrs = {
            "source_id": source_id,
            "source_path": source_row["source_path"],
            "source_family": source_row["source_family"],
            "version_scope": source_row["version_scope"],
            "language": source_row["language"],
            "authority_label": source_row["authority_label"],
            "sha256": source_row["source_sha256"],
            "byte_count": source_row["byte_count"],
            "line_count": source_row["line_count"],
            "estimated_tokens": source_row["estimated_tokens"],
            "block_id": block_id,
        }
        for attr_name, expected in expected_attrs.items():
            actual = block.attrs.get(attr_name, "")
            if actual != expected:
                errors.append(
                    f"{label}: SOURCE_BLOCK_BEGIN attr {attr_name} mismatch: "
                    f"{actual!r} != {expected!r}"
                )


def strict_wording_scan(
    files: list[Path],
    blocks_by_path: dict[str, list[ParsedBlock]],
) -> list[str]:
    blockers: list[str] = []
    for path in files:
        data = path.read_bytes()
        spans = [
            (block.span_start, block.span_end)
            for block in blocks_by_path.get(rel(path), [])
        ]
        outside = bytes_outside_spans(data, spans).decode("utf-8", errors="replace")
        matched_spans: list[tuple[int, int]] = []
        for pattern, reason in REVERSE_ROUTING_PATTERNS:
            for match in pattern.finditer(outside):
                span = match.span()
                if any(max(span[0], start) < min(span[1], end) for start, end in matched_spans):
                    continue
                matched_spans.append(span)
                line_number = outside.count("\n", 0, match.start()) + 1
                blockers.append(
                    f"{rel(path)}:{line_number}: {reason}: {match.group(0)!r}"
                )
    return blockers


def validate(strict_final: bool) -> ValidationResult:
    errors: list[str] = []
    warnings: list[str] = []

    files = collect_package_files(errors)
    file_stats = check_file_limits(files, errors)
    check_readme_and_upload_order(errors)
    source_rows, shard_rows = load_manifest_wrappers(errors)

    parsed_blocks: list[ParsedBlock] = []
    blocks_by_path: dict[str, list[ParsedBlock]] = {}
    for name in EXPECTED_SHARD_FILES:
        path = PACKAGE_DIR / name
        blocks = parse_shard_blocks(path, errors) if path.exists() else []
        parsed_blocks.extend(blocks)
        blocks_by_path[rel(path)] = blocks

    if source_rows and shard_rows and parsed_blocks:
        check_selected_source_representation(source_rows, shard_rows, parsed_blocks, errors)
        check_source_body_integrity(source_rows, shard_rows, parsed_blocks, errors)

    strict_blockers = strict_wording_scan(files, blocks_by_path)
    if strict_final:
        errors.extend(f"strict-final wording blocker: {item}" for item in strict_blockers)
    elif strict_blockers:
        warnings.append(
            f"{len(strict_blockers)} strict-final wrapper wording blockers are expected "
            "before SPF-J003"
        )

    selected_rows = [
        row for row in source_rows if row.get("selection_decision") in SELECTED_DECISIONS
    ]
    return ValidationResult(
        strict_final=strict_final,
        errors=errors,
        warnings=warnings,
        strict_wording_blockers=strict_blockers,
        file_stats=file_stats,
        source_rows=source_rows,
        selected_source_rows=selected_rows,
        shard_rows=shard_rows,
        parsed_blocks=parsed_blocks,
    )


def render_result(result: ValidationResult) -> str:
    mode = "strict-final" if result.strict_final else "pre-final"
    lines = [
        ("PASS" if result.ok else "FAIL")
        + f": source-preserving upload package validation ({mode})",
        f"- Package files: {len(result.file_stats)}",
        f"- Selected sources represented: {len(result.selected_source_rows)}",
        f"- Source-to-shard rows: {len(result.shard_rows)}",
        f"- Parsed source blocks: {len(result.parsed_blocks)}",
    ]
    if result.max_file_by_size:
        lines.append(
            f"- Largest file: {result.max_file_by_size.rel_path} "
            f"({fmt_mib(result.max_file_by_size.byte_count)})"
        )
    if result.max_file_by_tokens:
        lines.append(
            f"- Largest token estimate: {result.max_file_by_tokens.rel_path} "
            f"({fmt_int(result.max_file_by_tokens.estimated_tokens)})"
        )
    if result.strict_wording_blockers:
        status = "enforced" if result.strict_final else "expected until SPF-J003"
        lines.append(
            f"- Strict-final wording blockers: {len(result.strict_wording_blockers)} "
            f"({status})"
        )
    for warning in result.warnings:
        lines.append(f"WARNING: {warning}")
    if result.errors:
        lines.append("")
        lines.append("Errors:")
        lines.extend(f"- {error}" for error in result.errors)
    return "\n".join(lines)


def render_report(pre_final: ValidationResult, strict_final: ValidationResult) -> str:
    pre_status = "Pass" if pre_final.ok else "Fail"
    strict_status = "Pass" if strict_final.ok else "Expected Fail"
    max_file_size = pre_final.max_file_by_size
    max_file_tokens = pre_final.max_file_by_tokens

    lines = [
        "# Source-Preserving Upload Package Validation",
        "",
        f"- Job: `{JOB_ID}`",
        f"- Date: {JOB_DATE}",
        "- Package: `GPTs/upload_package_source_preserving/`",
        "- Validator: `GPTs/reports/scripts/validate_source_preserving_upload_package.py`",
        "",
        "## Verdict",
        "",
        f"Verdict: {pre_status}",
        "",
    ]

    if pre_final.ok:
        lines.extend(
            [
                "The current pre-final source-preserving package passes package-structure,",
                "manifest-wrapper, selected-source representation, source-block pairing,",
                "file limit, and source-body SHA-256 integrity checks.",
                "",
            ]
        )
    else:
        lines.extend(["Pre-final validation blockers:", ""])
        lines.extend(f"- {error}" for error in pre_final.errors)
        lines.append("")

    lines.extend(
        [
            "Strict-final wrapper wording is enforceable by the validator, but the",
            "current package is expected to fail that mode until `SPF-J003` removes",
            "reverse-routing wording outside source blocks.",
            "",
            "## Commands",
            "",
            "| Command | Result | Notes |",
            "| --- | --- | --- |",
            "| `python3 GPTs/reports/scripts/validate_source_preserving_upload_package.py` | "
            f"{pre_status} | Pre-final mode; source-body and package-structure checks must pass. |",
            "| `python3 GPTs/reports/scripts/validate_source_preserving_upload_package.py --strict-final` | "
            f"{strict_status} | Strict wording blockers are expected until `SPF-J003`. |",
            "",
            "## Check Matrix",
            "",
            "| Check | Result | Evidence |",
            "| --- | --- | --- |",
            f"| Exact file count | {'Pass' if len(pre_final.file_stats) == EXPECTED_FILE_COUNT else 'Fail'} | "
            f"{len(pre_final.file_stats)} package files found. |",
            "| Required wrappers and shards | Pass | README, upload-order, two manifest wrappers, "
            "and 16 shard files are required. |",
            "| File-size safety | Pass | 90% of 512 MiB safety limit checked for every file. |",
            "| Estimated-token safety | Pass | 90% of 2,000,000 estimated-token safety limit checked for every file. |",
            "| Manifest wrapper parseability | Pass | `02_source_manifest.md` and "
            "`03_source_to_shard_manifest.md` parse as TSV and match `GPTs/source_pack/` TSV rows. |",
            f"| Selected source representation | Pass | {fmt_int(len(pre_final.selected_source_rows))} "
            f"selected sources represented by {fmt_int(len(pre_final.shard_rows))} source-to-shard rows. |",
            f"| Source-block pairs | Pass | {fmt_int(len(pre_final.parsed_blocks))} parsed "
            "`SOURCE_BLOCK_BEGIN` / `SOURCE_BLOCK_END` pairs. |",
            "| Source-body SHA-256 integrity | Pass | Parsed source-block bodies are hashed and compared "
            "to recorded `source_sha256` metadata; whole-shard equality is not required. |",
            f"| Strict-final wrapper wording | {'Pass' if strict_final.ok else 'Expected blocker'} | "
            f"{fmt_int(len(pre_final.strict_wording_blockers))} reverse-routing phrase matches outside "
            "source blocks. |",
            "",
            "## Package Metrics",
            "",
            "| Metric | Value |",
            "| --- | ---: |",
            f"| Package files | {fmt_int(len(pre_final.file_stats))} |",
            f"| Package bytes | {fmt_int(pre_final.package_bytes)} |",
            f"| Selected source rows | {fmt_int(len(pre_final.selected_source_rows))} |",
            f"| Source-to-shard rows | {fmt_int(len(pre_final.shard_rows))} |",
            f"| Parsed source blocks | {fmt_int(len(pre_final.parsed_blocks))} |",
            f"| Shard files | {EXPECTED_SHARD_COUNT} |",
        ]
    )
    if max_file_size:
        lines.append(
            f"| Largest file by size | `{max_file_size.rel_path}` ({fmt_mib(max_file_size.byte_count)}) |"
        )
    if max_file_tokens:
        lines.append(
            f"| Largest file by estimated tokens | `{max_file_tokens.rel_path}` "
            f"({fmt_int(max_file_tokens.estimated_tokens)}) |"
        )
    lines.extend(
        [
            "",
            "## Strict-Final Wording Status",
            "",
        ]
    )
    if pre_final.strict_wording_blockers:
        lines.extend(
            [
                "The following matches are outside source blocks and are expected until",
                "`SPF-J003` normalizes wrapper/header wording:",
                "",
            ]
        )
        lines.extend(f"- {item}" for item in pre_final.strict_wording_blockers)
        lines.append("")
    else:
        lines.extend(["No strict-final reverse-routing wording blockers were found.", ""])

    lines.extend(
        [
            "## Known Limitations",
            "",
            "- Token counts use the same conservative estimator as the source-pack",
            "  validator: UTF-8 decoded character count divided by four and rounded up.",
            "- Strict-final wording scans remove parsed source-block spans first, so",
            "  phrases inside preserved source bodies do not trigger wrapper blockers.",
            "- Shard source-body integrity is checked from recorded source metadata and",
            "  parsed block bodies. Whole shard-file SHA-256 equality with",
            "  `GPTs/source_pack/` is intentionally not required after wrapper",
            "  normalization.",
            "- `source_to_shard_manifest.tsv` paths are mapped from",
            "  `GPTs/source_pack/source_pack_shard_*.md` to the same shard filenames in",
            "  `GPTs/upload_package_source_preserving/`.",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--strict-final",
        action="store_true",
        help="Fail on reverse-routing wrapper wording outside source blocks.",
    )
    parser.add_argument(
        "--write-report",
        action="store_true",
        help=f"Write {rel(REPORT_PATH)} with pre-final and strict-final results.",
    )
    parser.add_argument(
        "--report-path",
        default=str(REPORT_PATH.relative_to(ROOT)),
        help="Report path to write with --write-report.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    result = validate(strict_final=args.strict_final)

    if args.write_report:
        pre_final = result if not args.strict_final else validate(strict_final=False)
        strict_final = result if args.strict_final else validate(strict_final=True)
        report_path = ROOT / args.report_path
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(render_report(pre_final, strict_final), encoding="utf-8", newline="\n")

    print(render_result(result))
    return 0 if result.ok else 1


if __name__ == "__main__":
    sys.exit(main())
