#!/usr/bin/env python3
"""Build deterministic Stage 1 source-pack shards and source-to-shard mapping."""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import math
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SOURCE_PACK_DIR = Path("GPTs/source_pack")
MANIFEST_PATH = SOURCE_PACK_DIR / "source_manifest.tsv"
SHARD_MANIFEST_PATH = SOURCE_PACK_DIR / "source_to_shard_manifest.tsv"
SHARD_NAME_TEMPLATE = "source_pack_shard_{index:03d}.md"
SHARD_TOKEN_TARGET = 900_000

SOURCE_MANIFEST_REQUIRED_COLUMNS = [
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


@dataclass(frozen=True)
class Source:
    row: dict[str, str]
    body: bytes

    @property
    def source_id(self) -> str:
        return self.row["source_id"]

    @property
    def estimated_tokens(self) -> int:
        return int(self.row["estimated_tokens"])


def clean(value: object) -> str:
    text = "" if value is None else str(value)
    return re.sub(r"[\t\r\n]+", " ", text).strip()


def full_path_for(source_path: str) -> Path:
    if source_path.startswith("~/"):
        return Path.home() / source_path[2:]
    return ROOT / source_path


def line_count(data: bytes) -> int:
    if not data:
        return 0
    return data.count(b"\n") + (0 if data.endswith(b"\n") else 1)


def estimated_tokens(data: bytes) -> int:
    text = data.decode("utf-8")
    return max(1, math.ceil(len(text) / 4)) if text else 0


def source_sort_key(source: Source) -> tuple[str, str, str, str, str]:
    row = source.row
    return (
        row["source_family"],
        row["version_scope"],
        row["source_origin"],
        row["source_path"],
        row["source_id"],
    )


def attr(value: str) -> str:
    return html.escape(clean(value), quote=True)


def markdown_cell(value: str) -> str:
    return clean(value).replace("\\", "\\\\").replace("|", "\\|")


def read_manifest() -> list[dict[str, str]]:
    path = ROOT / MANIFEST_PATH
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames != SOURCE_MANIFEST_REQUIRED_COLUMNS:
            raise ValueError(f"{MANIFEST_PATH}: unexpected columns {reader.fieldnames!r}")
        return [{key: clean(value) for key, value in row.items()} for row in reader]


def load_sources() -> list[Source]:
    errors: list[str] = []
    sources: list[Source] = []
    seen_ids: set[str] = set()

    for row in read_manifest():
        source_id = row["source_id"]
        if source_id in seen_ids:
            errors.append(f"duplicate source_id in source manifest: {source_id}")
            continue
        seen_ids.add(source_id)

        if row["selection_decision"] not in SELECTED_DECISIONS:
            continue

        path = full_path_for(row["source_path"])
        if not path.exists():
            errors.append(f"{source_id}: source path does not exist: {row['source_path']}")
            continue

        data = path.read_bytes()
        try:
            data.decode("utf-8")
        except UnicodeDecodeError as exc:
            errors.append(f"{source_id}: source is not UTF-8 decodable: {row['source_path']} ({exc})")
            continue

        sha256 = hashlib.sha256(data).hexdigest()
        checks = {
            "source_sha256": sha256,
            "byte_count": str(len(data)),
            "line_count": str(line_count(data)),
            "estimated_tokens": str(estimated_tokens(data)),
        }
        for field, actual in checks.items():
            if row[field] != actual:
                errors.append(f"{source_id}: {field} mismatch: manifest={row[field]} actual={actual}")

        sources.append(Source(row=row, body=data))

    if errors:
        raise SystemExit("\n".join(f"ERROR: {error}" for error in errors))
    return sorted(sources, key=source_sort_key)


def pack_sources(sources: list[Source]) -> list[list[Source]]:
    shards: list[list[Source]] = []
    current: list[Source] = []
    current_tokens = 0

    for source in sources:
        tokens = source.estimated_tokens
        if current and current_tokens + tokens > SHARD_TOKEN_TARGET:
            shards.append(current)
            current = []
            current_tokens = 0
        current.append(source)
        current_tokens += tokens

    if current:
        shards.append(current)
    return shards


def render_source_block(source: Source, block_id: str) -> bytes:
    row = source.row
    metadata_rows = [
        ("source_id", row["source_id"]),
        ("source_path", row["source_path"]),
        ("source_family", row["source_family"]),
        ("version_scope", row["version_scope"]),
        ("language", row["language"]),
        ("authority_label", row["authority_label"]),
        ("source_sha256", row["source_sha256"]),
        ("byte_count", row["byte_count"]),
        ("line_count", row["line_count"]),
        ("estimated_tokens", row["estimated_tokens"]),
    ]
    table = ["| Field | Value |", "| --- | --- |"]
    table.extend(f"| `{field}` | {markdown_cell(value)} |" for field, value in metadata_rows)
    begin = (
        "<!-- SOURCE_BLOCK_BEGIN "
        f"source_id=\"{attr(row['source_id'])}\" "
        f"source_path=\"{attr(row['source_path'])}\" "
        f"source_family=\"{attr(row['source_family'])}\" "
        f"version_scope=\"{attr(row['version_scope'])}\" "
        f"language=\"{attr(row['language'])}\" "
        f"authority_label=\"{attr(row['authority_label'])}\" "
        f"sha256=\"{attr(row['source_sha256'])}\" "
        f"byte_count=\"{attr(row['byte_count'])}\" "
        f"line_count=\"{attr(row['line_count'])}\" "
        f"estimated_tokens=\"{attr(row['estimated_tokens'])}\" "
        f"block_id=\"{attr(block_id)}\" -->\n"
    )
    end = f"<!-- SOURCE_BLOCK_END source_id=\"{attr(row['source_id'])}\" block_id=\"{attr(block_id)}\" -->\n\n"
    prefix = (
        f"## {row['source_id']} - {row['title']}\n\n"
        + "\n".join(table)
        + "\n\n"
        + begin
    )
    return prefix.encode("utf-8") + source.body + end.encode("utf-8")


def render_outputs(sources: list[Source]) -> tuple[dict[Path, bytes], str]:
    shard_files: dict[Path, bytes] = {}
    manifest_rows: list[dict[str, str]] = []
    block_number = 0

    for shard_index, shard_sources in enumerate(pack_sources(sources), start=1):
        shard_id = f"SHARD-{shard_index:03d}"
        shard_path = SOURCE_PACK_DIR / SHARD_NAME_TEMPLATE.format(index=shard_index)
        shard_header = (
            f"# Altibase Source Pack Shard {shard_index:03d}\n\n"
            f"- Shard ID: `{shard_id}`\n"
            "- Upload intended: `no`\n"
            "- Purpose: Stage 1 source-preserving evidence artifact.\n\n"
        ).encode("utf-8")
        shard_body = bytearray(shard_header)
        shard_rows: list[dict[str, str]] = []

        for order, source in enumerate(shard_sources, start=1):
            block_number += 1
            block_id = f"BLOCK-{block_number:06d}"
            shard_body.extend(render_source_block(source, block_id))
            row = source.row
            shard_rows.append(
                {
                    "source_id": row["source_id"],
                    "shard_id": shard_id,
                    "shard_path": shard_path.as_posix(),
                    "block_id": block_id,
                    "order_in_shard": str(order),
                    "source_start_line": "1",
                    "source_end_line": row["line_count"],
                    "source_sha256": row["source_sha256"],
                    "extracted_body_sha256": hashlib.sha256(source.body).hexdigest(),
                    "block_byte_count": str(len(source.body)),
                    "block_line_count": str(line_count(source.body)),
                    "block_estimated_tokens": row["estimated_tokens"],
                    "shard_estimated_tokens": "",
                    "upload_intended": "no",
                    "validation_status": "pass",
                    "notes": "Exact source bytes copied into the source-pack shard body.",
                }
            )

        shard_bytes = bytes(shard_body)
        shard_token_count = str(estimated_tokens(shard_bytes))
        for row in shard_rows:
            row["shard_estimated_tokens"] = shard_token_count
        manifest_rows.extend(shard_rows)
        shard_files[shard_path] = shard_bytes

    validate_generated_outputs(sources, shard_files, manifest_rows)
    return shard_files, render_tsv(manifest_rows, SHARD_MANIFEST_COLUMNS)


def render_tsv(rows: list[dict[str, str]], columns: list[str]) -> str:
    output = ["\t".join(columns)]
    for row in rows:
        output.append("\t".join(clean(row.get(column, "")) for column in columns))
    return "\n".join(output) + "\n"


def validate_generated_outputs(
    sources: list[Source],
    shard_files: dict[Path, bytes],
    manifest_rows: list[dict[str, str]],
) -> None:
    errors: list[str] = []
    expected_ids = [source.source_id for source in sources]
    mapped_ids = [row["source_id"] for row in manifest_rows]
    if sorted(expected_ids) != sorted(mapped_ids):
        errors.append("source_to_shard_manifest does not cover exactly the selected source IDs")
    if len(mapped_ids) != len(set(mapped_ids)):
        errors.append("duplicate source IDs in source_to_shard_manifest")
    for row in manifest_rows:
        if row["source_sha256"] != row["extracted_body_sha256"]:
            errors.append(f"{row['source_id']}: extracted body checksum does not match source checksum")
        if row["block_byte_count"] == "0":
            errors.append(f"{row['source_id']}: empty source block")
    for path, content in shard_files.items():
        if b"<!-- SOURCE_BLOCK_BEGIN " not in content or b"<!-- SOURCE_BLOCK_END " not in content:
            errors.append(f"{path}: missing source boundary markers")
    if errors:
        raise SystemExit("\n".join(f"ERROR: {error}" for error in errors))


def generated_shard_paths() -> set[Path]:
    return {path.relative_to(ROOT) for path in (ROOT / SOURCE_PACK_DIR).glob("source_pack_shard_*.md")}


def write_outputs(shard_files: dict[Path, bytes], shard_manifest: str) -> None:
    target_dir = ROOT / SOURCE_PACK_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    expected_paths = set(shard_files)
    for path in sorted(generated_shard_paths()):
        if path not in expected_paths:
            (ROOT / path).unlink()
    for path, content in shard_files.items():
        full_path = ROOT / path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        full_path.write_bytes(content)
    (ROOT / SHARD_MANIFEST_PATH).write_text(shard_manifest, encoding="utf-8", newline="")


def check_outputs(shard_files: dict[Path, bytes], shard_manifest: str) -> bool:
    ok = True
    expected_paths = set(shard_files)
    for path, content in sorted(shard_files.items()):
        full_path = ROOT / path
        if not full_path.exists():
            print(f"missing generated shard: {path}", file=sys.stderr)
            ok = False
        elif full_path.read_bytes() != content:
            print(f"generated shard is stale: {path}", file=sys.stderr)
            ok = False
    for path in sorted(generated_shard_paths() - expected_paths):
        print(f"unexpected generated shard: {path}", file=sys.stderr)
        ok = False
    manifest_path = ROOT / SHARD_MANIFEST_PATH
    if not manifest_path.exists():
        print(f"missing generated file: {SHARD_MANIFEST_PATH}", file=sys.stderr)
        ok = False
    elif manifest_path.read_text(encoding="utf-8") != shard_manifest:
        print(f"generated file is stale: {SHARD_MANIFEST_PATH}", file=sys.stderr)
        ok = False
    return ok


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write generated shards and mapping")
    parser.add_argument("--check", action="store_true", help="verify generated shards and mapping are current")
    args = parser.parse_args()

    if args.write and args.check:
        parser.error("--write and --check are mutually exclusive")
    if not args.write and not args.check:
        args.check = True

    sources = load_sources()
    shard_files, shard_manifest = render_outputs(sources)

    if args.write:
        write_outputs(shard_files, shard_manifest)
    elif not check_outputs(shard_files, shard_manifest):
        return 1

    print(f"source_pack selected sources: {len(sources)}")
    print(f"source_pack shards: {len(shard_files)}")
    print(f"source_to_shard_manifest rows: {len(sources)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
