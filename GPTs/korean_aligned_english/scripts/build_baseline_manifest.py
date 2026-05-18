#!/usr/bin/env python3
"""Build the Stage 1 Korean-aligned English baseline inventory manifest."""

from __future__ import annotations

import argparse
import csv
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass
from io import StringIO
from pathlib import Path, PurePosixPath


JOB_ID = "S1-J006"

ROOT = Path(__file__).resolve().parents[3]
BASELINE_DIR = Path("GPTs/korean_aligned_english")
MANIFEST_PATH = BASELINE_DIR / "baseline_manifest.tsv"
SOURCE_MANIFEST_PATH = Path("GPTs/source_pack/source_manifest.tsv")
SOURCE_TO_SHARD_PATH = Path("GPTs/source_pack/source_to_shard_manifest.tsv")
SOURCE_PACK_VALIDATION_PATH = Path("GPTs/source_pack/source_pack_validation.md")

LANGUAGE_SEGMENTS = {"kor": "ko", "eng": "en"}
READY_MARKERS = [
    "- Status: `pass`",
    "Verdict: Pass",
    "No source-pack validation blockers were found.",
    "Do not proceed to the",
    "Korean-aligned English baseline",
]

BASELINE_COLUMNS = [
    "baseline_block_id",
    "korean_source_id",
    "korean_source_path",
    "english_source_id",
    "english_source_path",
    "other_source_id",
    "other_source_path",
    "source_family",
    "version_scope",
    "authority_label",
    "baseline_source_type",
    "planned_downstream_use",
    "alignment_status",
    "source_block_refs",
    "evidence_or_limitation_note",
    "last_verified_job",
]

SOURCE_REQUIRED_COLUMNS = {
    "source_id",
    "source_origin",
    "source_path",
    "source_role",
    "source_family",
    "version_scope",
    "language",
    "authority_label",
    "selection_decision",
    "extraction_mode",
    "line_count",
}

SHARD_REQUIRED_COLUMNS = {
    "source_id",
    "block_id",
    "source_start_line",
    "source_end_line",
}

ALLOWED_ALIGNMENT_STATUSES = {
    "pending",
    "aligned",
    "conflict",
    "recheck",
    "excluded",
    "aid_reuse",
    "not_ready",
}

VERSION_ORDER = {
    "7.1": 10,
    "7.3": 20,
    "8.1_verified": 30,
    "multi": 40,
    "aid": 50,
    "unknown": 90,
}


@dataclass(frozen=True)
class SourceGroup:
    group_key: tuple[str, ...]
    korean_rows: tuple[dict[str, str], ...]
    english_rows: tuple[dict[str, str], ...]
    other_rows: tuple[dict[str, str], ...]


def clean(value: object) -> str:
    text = "" if value is None else str(value)
    return re.sub(r"[\t\r\n]+", " ", text).strip()


def normalize_part(part: str) -> str:
    text = unicodedata.normalize("NFKC", part)
    text = text.replace("’", "'").replace("‘", "'").replace("`", "'")
    text = re.sub(r"[_\s]+", " ", text.casefold())
    return text.strip()


def read_tsv(path: Path, required_columns: set[str]) -> list[dict[str, str]]:
    full_path = ROOT / path
    with full_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        fieldnames = set(reader.fieldnames or [])
        missing = sorted(required_columns.difference(fieldnames))
        if missing:
            raise ValueError(f"{path}: missing columns {missing}")
        return [
            {column: clean(row.get(column, "")) for column in reader.fieldnames or []}
            for row in reader
        ]


def source_pack_validation_ready() -> tuple[bool, str]:
    full_path = ROOT / SOURCE_PACK_VALIDATION_PATH
    if not full_path.exists():
        return False, f"{SOURCE_PACK_VALIDATION_PATH} is missing."

    text = full_path.read_text(encoding="utf-8")
    missing = [marker for marker in READY_MARKERS if marker not in text]
    if missing:
        return (
            False,
            f"{SOURCE_PACK_VALIDATION_PATH} does not contain ready markers: "
            + "; ".join(missing),
        )

    return (
        True,
        "source_pack_validation.md records Status pass, Verdict Pass, no blockers, "
        "and the Korean-aligned English continuation gate.",
    )


def language_segment(path_text: str) -> tuple[str, int] | tuple[None, None]:
    parts = PurePosixPath(path_text).parts
    for index, part in enumerate(parts):
        if part in LANGUAGE_SEGMENTS:
            return part, index
    return None, None


def pairing_key(path_text: str) -> tuple[str, ...] | None:
    parts = list(PurePosixPath(path_text).parts)
    segment, index = language_segment(path_text)
    if segment is None or index is None:
        return None
    parts[index] = "{lang}"
    return tuple(normalize_part(part) for part in parts)


def row_language_class(row: dict[str, str]) -> str:
    segment, _ = language_segment(row["source_path"])
    if segment == "kor":
        return "ko"
    if segment == "eng":
        return "en"
    return "other"


def selected_repo_exact_rows(source_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    return [
        row
        for row in source_rows
        if row["source_origin"] == "repo"
        and row["selection_decision"] == "include_exact"
        and row["extraction_mode"] == "exact_markdown"
    ]


def group_rows(source_rows: list[dict[str, str]]) -> list[SourceGroup]:
    grouped: dict[tuple[str, ...], list[dict[str, str]]] = defaultdict(list)
    no_language_rows: list[dict[str, str]] = []

    for row in selected_repo_exact_rows(source_rows):
        key = pairing_key(row["source_path"])
        if key is None:
            no_language_rows.append(row)
        else:
            grouped[key].append(row)

    groups: list[SourceGroup] = []
    for key, rows in grouped.items():
        korean = tuple(sorted((row for row in rows if row_language_class(row) == "ko"), key=source_sort_key))
        english = tuple(sorted((row for row in rows if row_language_class(row) == "en"), key=source_sort_key))
        other = tuple(sorted((row for row in rows if row_language_class(row) == "other"), key=source_sort_key))
        groups.append(SourceGroup(key, korean, english, other))

    for row in sorted(no_language_rows, key=source_sort_key):
        key = tuple(normalize_part(part) for part in PurePosixPath(row["source_path"]).parts)
        groups.append(SourceGroup(key, tuple(), tuple(), (row,)))

    return sorted(groups, key=group_sort_key)


def version_sort_value(version_scope: str) -> tuple[int, str]:
    if version_scope in VERSION_ORDER:
        return (VERSION_ORDER[version_scope], version_scope)
    if re.fullmatch(r"\d+(?:\.\d+)+", version_scope):
        family = version_scope.split(".")[:2]
        base = ".".join(family)
        return (VERSION_ORDER.get(base, 80), version_scope)
    return (80, version_scope)


def source_sort_key(row: dict[str, str]) -> tuple[tuple[int, str], str, str, str]:
    return (
        version_sort_value(row["version_scope"]),
        row["source_family"],
        row["source_path"],
        row["source_id"],
    )


def group_sort_key(group: SourceGroup) -> tuple[tuple[int, str], str, str]:
    rows = list(group.korean_rows + group.english_rows + group.other_rows)
    version = joined_unique(row["version_scope"] for row in rows)
    family = joined_unique(row["source_family"] for row in rows)
    first_path = min((row["source_path"] for row in rows), default="")
    return (version_sort_value(version), family, first_path)


def joined_unique(values: object) -> str:
    cleaned = sorted({clean(value) for value in values if clean(value)})
    return ";".join(cleaned)


def joined_source_ids(rows: tuple[dict[str, str], ...]) -> str:
    return ";".join(row["source_id"] for row in rows)


def joined_source_paths(rows: tuple[dict[str, str], ...]) -> str:
    return ";".join(row["source_path"] for row in rows)


def joined_authority(rows: tuple[dict[str, str], ...]) -> str:
    labels: list[str] = []
    for row in rows:
        for label in row["authority_label"].split(";"):
            label = clean(label)
            if label and label not in labels:
                labels.append(label)
    return "; ".join(labels)


def source_block_ref(row: dict[str, str], shard_refs: dict[str, str]) -> str:
    source_id = row["source_id"]
    if source_id not in shard_refs:
        raise ValueError(f"{source_id}: missing source-to-shard block reference")
    return shard_refs[source_id]


def joined_block_refs(rows: tuple[dict[str, str], ...], shard_refs: dict[str, str]) -> str:
    return ";".join(source_block_ref(row, shard_refs) for row in rows)


def load_shard_refs(shard_rows: list[dict[str, str]]) -> dict[str, str]:
    refs: dict[str, str] = {}
    for row in shard_rows:
        source_id = row["source_id"]
        refs[source_id] = (
            f"{source_id}/{row['block_id']}:lines="
            f"{row['source_start_line']}-{row['source_end_line']}"
        )
    return refs


def expected_manifest_rows() -> tuple[list[dict[str, str]], Counter[str], str]:
    ready, validation_note = source_pack_validation_ready()
    if not ready:
        return [not_ready_row(validation_note)], Counter({"not_ready": 1}), validation_note

    source_rows = read_tsv(SOURCE_MANIFEST_PATH, SOURCE_REQUIRED_COLUMNS)
    shard_rows = read_tsv(SOURCE_TO_SHARD_PATH, SHARD_REQUIRED_COLUMNS)
    shard_refs = load_shard_refs(shard_rows)

    rows: list[dict[str, str]] = []
    stats: Counter[str] = Counter()

    for index, group in enumerate(group_rows(source_rows), start=1):
        manifest_row, source_type = manifest_row_for_group(index, group, shard_refs)
        rows.append(manifest_row)
        stats[source_type] += 1

    validate_inventory(rows, source_rows, stats)
    return rows, stats, validation_note


def not_ready_row(note: str) -> dict[str, str]:
    return {
        "baseline_block_id": "KAE-BLOCK-NOT-READY",
        "korean_source_id": "",
        "korean_source_path": "",
        "english_source_id": "",
        "english_source_path": "",
        "other_source_id": "",
        "other_source_path": "",
        "source_family": "stage1_source_pack_validation",
        "version_scope": "multi",
        "authority_label": "Source pack validation gate not ready",
        "baseline_source_type": "not_ready",
        "planned_downstream_use": "blocked_until_source_pack_validation_passes",
        "alignment_status": "not_ready",
        "source_block_refs": SOURCE_PACK_VALIDATION_PATH.as_posix(),
        "evidence_or_limitation_note": note,
        "last_verified_job": JOB_ID,
    }


def manifest_row_for_group(
    index: int, group: SourceGroup, shard_refs: dict[str, str]
) -> tuple[dict[str, str], str]:
    korean = group.korean_rows
    english = group.english_rows
    other = group.other_rows
    all_rows = korean + english + other

    source_family = joined_unique(row["source_family"] for row in all_rows)
    version_scope = joined_unique(row["version_scope"] for row in all_rows)
    authority_label = joined_authority(all_rows)

    if korean and english:
        source_type = "repo_paired_ko_en"
        alignment_status = "pending"
        planned_use = "primary_working_source_after_alignment"
        note = (
            "Detected matched kor/eng source paths under selected roots; derived "
            "English baseline text is pending Korean-authority alignment."
        )
    elif korean:
        source_type = "repo_ko_only"
        alignment_status = "pending"
        planned_use = "translation_candidate_after_alignment"
        note = (
            "No paired English source was selected; preserve Korean authority for "
            "later English baseline translation."
        )
    elif english:
        source_type = "repo_en_only"
        alignment_status = "excluded"
        planned_use = "blocked_until_korean_authority_or_auxiliary_label"
        note = (
            "No paired Korean authority source was selected; excluded from the "
            "Korean-aligned baseline until Korean authority or approved auxiliary "
            "use is recorded."
        )
    else:
        source_type = "repo_no_language_tree"
        alignment_status = "excluded"
        planned_use = "source_pack_only_not_korean_aligned"
        note = (
            "Selected repository source has no kor/eng path segment; retained in "
            "the exact source pack and excluded from this Korean-English pairing "
            "inventory."
        )

    if len(korean) > 1 or len(english) > 1:
        alignment_status = "recheck"
        planned_use = "blocked_until_pairing_recheck"
        note = (
            "Multiple Korean or English rows share the same normalized pairing key; "
            "manual recheck is required before baseline derivation."
        )

    if len({row["source_family"] for row in all_rows}) > 1 or len({row["version_scope"] for row in all_rows}) > 1:
        alignment_status = "recheck"
        planned_use = "blocked_until_family_or_version_recheck"
        note = (
            "Matched rows do not share one source_family and version_scope; manual "
            "recheck is required before baseline derivation."
        )

    block_ref_rows = all_rows
    source_block_refs = joined_block_refs(block_ref_rows, shard_refs)

    return (
        {
            "baseline_block_id": f"KAE-BLOCK-{index:06d}",
            "korean_source_id": joined_source_ids(korean),
            "korean_source_path": joined_source_paths(korean),
            "english_source_id": joined_source_ids(english),
            "english_source_path": joined_source_paths(english),
            "other_source_id": joined_source_ids(other),
            "other_source_path": joined_source_paths(other),
            "source_family": source_family,
            "version_scope": version_scope,
            "authority_label": authority_label,
            "baseline_source_type": source_type,
            "planned_downstream_use": planned_use,
            "alignment_status": alignment_status,
            "source_block_refs": source_block_refs,
            "evidence_or_limitation_note": note,
            "last_verified_job": JOB_ID,
        },
        source_type,
    )


def validate_inventory(
    rows: list[dict[str, str]],
    source_rows: list[dict[str, str]],
    stats: Counter[str],
) -> None:
    errors: list[str] = []

    ids = [row["baseline_block_id"] for row in rows]
    duplicate_ids = sorted(item for item, count in Counter(ids).items() if count > 1)
    if duplicate_ids:
        errors.append(f"duplicate baseline_block_id values: {duplicate_ids}")

    bad_statuses = sorted({row["alignment_status"] for row in rows} - ALLOWED_ALIGNMENT_STATUSES)
    if bad_statuses:
        errors.append(f"unsupported alignment_status values: {bad_statuses}")

    if not any(row["alignment_status"] == "not_ready" for row in rows):
        selected_source_ids = {row["source_id"] for row in selected_repo_exact_rows(source_rows)}
        recorded_source_ids = source_ids_from_manifest_rows(rows)
        missing_source_ids = sorted(selected_source_ids - recorded_source_ids)
        extra_source_ids = sorted(recorded_source_ids - selected_source_ids)
        if missing_source_ids:
            errors.append(f"selected repo source IDs missing from baseline manifest: {missing_source_ids}")
        if extra_source_ids:
            errors.append(f"baseline manifest records unknown source IDs: {extra_source_ids}")

        for required in ("7.1", "7.3", "8.1_verified"):
            if required not in {row["version_scope"] for row in rows}:
                errors.append(f"missing distinguishable version_scope row: {required}")

        if stats["repo_paired_ko_en"] == 0:
            errors.append("no paired Korean/English source groups detected")

        expected_unpaired = source_unpaired_counts(source_rows)
        if stats["repo_ko_only"] != expected_unpaired["repo_ko_only"]:
            errors.append(
                "Korean-only source group count mismatch: "
                f"expected {expected_unpaired['repo_ko_only']} got {stats['repo_ko_only']}"
            )
        if stats["repo_en_only"] != expected_unpaired["repo_en_only"]:
            errors.append(
                "English-only source group count mismatch: "
                f"expected {expected_unpaired['repo_en_only']} got {stats['repo_en_only']}"
            )

    if errors:
        raise ValueError("\n".join(errors))


def source_ids_from_manifest_rows(rows: list[dict[str, str]]) -> set[str]:
    result: set[str] = set()
    for row in rows:
        for field in ("korean_source_id", "english_source_id", "other_source_id"):
            for source_id in row[field].split(";"):
                source_id = clean(source_id)
                if source_id:
                    result.add(source_id)
    return result


def source_unpaired_counts(source_rows: list[dict[str, str]]) -> Counter[str]:
    counts: Counter[str] = Counter()
    for group in group_rows(source_rows):
        if group.korean_rows and not group.english_rows:
            counts["repo_ko_only"] += 1
        if group.english_rows and not group.korean_rows:
            counts["repo_en_only"] += 1
    return counts


def render_tsv(rows: list[dict[str, str]]) -> str:
    output = StringIO()
    writer = csv.DictWriter(
        output,
        fieldnames=BASELINE_COLUMNS,
        delimiter="\t",
        lineterminator="\n",
        extrasaction="raise",
    )
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue()


def write_manifest(path: Path, content: str) -> None:
    full_path = ROOT / path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    full_path.write_text(content, encoding="utf-8", newline="")


def summary(stats: Counter[str], validation_note: str) -> str:
    ordered = [
        "repo_paired_ko_en",
        "repo_ko_only",
        "repo_en_only",
        "repo_no_language_tree",
        "not_ready",
    ]
    parts = [f"{key}={stats[key]}" for key in ordered if stats[key]]
    return f"{'; '.join(parts)}; gate={validation_note}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="exit non-zero if the committed baseline manifest is not current",
    )
    parser.add_argument(
        "--output",
        default=MANIFEST_PATH.as_posix(),
        help="repository-relative output path",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output_path = Path(args.output)

    rows, stats, validation_note = expected_manifest_rows()
    expected = render_tsv(rows)
    full_output_path = ROOT / output_path

    if args.check:
        if not full_output_path.exists():
            print(f"{output_path}: missing", file=sys.stderr)
            return 1
        actual = full_output_path.read_text(encoding="utf-8")
        if actual != expected:
            print(f"{output_path}: not current; rerun build_baseline_manifest.py", file=sys.stderr)
            return 1
        print(f"{output_path}: current ({len(rows)} rows; {summary(stats, validation_note)})")
        return 0

    write_manifest(output_path, expected)
    print(f"{output_path}: wrote {len(rows)} rows ({summary(stats, validation_note)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
