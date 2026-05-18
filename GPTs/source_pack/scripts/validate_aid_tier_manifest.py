#!/usr/bin/env python3
"""Validate the Stage 1 AID tier manifest."""

from __future__ import annotations

import csv
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
AID_MANIFEST = ROOT / "GPTs/reports/aid_tier_manifest.tsv"
SOURCE_MANIFEST = ROOT / "GPTs/source_pack/source_manifest.tsv"
CONFLICT_REGISTER = ROOT / "GPTs/reports/source_conflict_register.md"
DESIGN_NOTE = ROOT / "GPTs/reports/stage_01_aid_tier_manifest_design.md"

REQUIRED_COLUMNS = [
    "aid_source_id",
    "aid_path",
    "aid_tier",
    "source_class",
    "coverage_status",
    "classification_evidence",
    "allowed_downstream_use",
    "required_label",
    "source_manifest_action",
    "source_id",
    "exclusion_id",
    "conflict_id",
    "last_verified_job",
    "notes",
]

ALLOWED_TIERS = {
    "upload_content_candidate",
    "evidence_only_authority",
    "accepted_limitation",
    "conflict",
    "recheck",
}

ALLOWED_ACTIONS = {
    "include_exact",
    "include_support_evidence",
    "exclude_register",
    "conflict_register",
    "recheck_register",
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        if reader.fieldnames != REQUIRED_COLUMNS:
            raise ValueError(f"{path}: unexpected columns {reader.fieldnames!r}")
        return list(reader)


def read_source_ids() -> set[str]:
    with SOURCE_MANIFEST.open(newline="", encoding="utf-8") as f:
        return {row["source_id"] for row in csv.DictReader(f, delimiter="\t")}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> int:
    errors: list[str] = []
    rows = read_tsv(AID_MANIFEST)
    source_ids = read_source_ids()
    conflict_text = CONFLICT_REGISTER.read_text(encoding="utf-8")
    design_text = DESIGN_NOTE.read_text(encoding="utf-8")

    if "No blanket Korean-to-English rewrite is scheduled for AID." not in design_text:
        fail(errors, "design note does not verify the no-blanket-rewrite boundary")

    seen_ids: set[str] = set()
    upload_candidates = 0
    for row in rows:
        aid_id = row["aid_source_id"]
        if not aid_id:
            fail(errors, "blank aid_source_id")
        if aid_id in seen_ids:
            fail(errors, f"duplicate aid_source_id {aid_id}")
        seen_ids.add(aid_id)

        if row["aid_tier"] not in ALLOWED_TIERS:
            fail(errors, f"{aid_id}: invalid aid_tier {row['aid_tier']!r}")
        if row["source_manifest_action"] not in ALLOWED_ACTIONS:
            fail(errors, f"{aid_id}: invalid source_manifest_action {row['source_manifest_action']!r}")

        for col in (
            "aid_path",
            "source_class",
            "coverage_status",
            "classification_evidence",
            "allowed_downstream_use",
            "required_label",
            "last_verified_job",
        ):
            if not row[col].strip():
                fail(errors, f"{aid_id}: required field {col} is blank")

        if row["aid_tier"] == "upload_content_candidate":
            upload_candidates += 1
            if row["source_manifest_action"] != "include_exact":
                fail(errors, f"{aid_id}: upload candidate must plan include_exact")
            if not row["classification_evidence"].startswith("~/AID/"):
                fail(errors, f"{aid_id}: upload candidate lacks AID evidence path")
            if "English-only" in row["source_class"] and "English-only" not in row["required_label"]:
                fail(errors, f"{aid_id}: English-only candidate does not preserve required label")

        if row["aid_tier"] in {"conflict", "recheck"}:
            if not row["conflict_id"]:
                fail(errors, f"{aid_id}: conflict/recheck row lacks conflict_id")
            if row["conflict_id"] not in conflict_text:
                fail(errors, f"{aid_id}: conflict_id not found in conflict register")

        if row["conflict_id"] and row["conflict_id"] not in conflict_text:
            fail(errors, f"{aid_id}: conflict_id {row['conflict_id']} not found in conflict register")

        if row["source_id"] and row["source_id"] not in source_ids:
            fail(errors, f"{aid_id}: source_id {row['source_id']} missing from source_manifest.tsv")

    if upload_candidates == 0:
        fail(errors, "no AID upload-content candidates found")

    if "no open AID" not in conflict_text:
        fail(errors, "conflict register does not record no open AID conflict/recheck rows")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"validated {len(rows)} AID tier rows; upload candidates={upload_candidates}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
