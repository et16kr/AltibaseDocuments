#!/usr/bin/env python3
"""Calibrate the benchmark fact-coverage judge against a hand-labelled gold set.

This is a measurement tool (plan item T9). It runs the rule judge's
``fact_match`` over each gold entry and reports how often the judge's
``covered`` verdict agrees with the careful human label. It never fails on low
agreement -- later jobs (T6/T7/T8) tune the judge and re-run this to check
progress.

Stable interface contract: this script depends ONLY on
``judge_report.fact_match(fact_text, answer, required_tokens)`` returning an
object with a ``.covered`` attribute. Later jobs may freely change the judge's
internals as long as that contract holds.

Run from the repository root:

    python3 evals/altibase_answerability/scripts/calibrate_judge.py
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# judge_report.py lives next to this script. Add that directory to sys.path
# explicitly so the import works regardless of the current working directory.
SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import judge_report  # noqa: E402  (import after sys.path adjustment)

DEFAULT_GOLD = SCRIPT_DIR.parent / "fixtures" / "judge_gold_set.jsonl"
DEFAULT_REPORT = SCRIPT_DIR.parent / "improvement" / "logs" / "judge_calibration_report.json"

VALID_LABELS = {"covered", "not_covered"}


def load_gold(path: Path) -> list[dict]:
    """Load and lightly validate the gold-set JSONL."""
    entries: list[dict] = []
    with path.open(encoding="utf-8") as fh:
        for lineno, raw in enumerate(fh, start=1):
            raw = raw.strip()
            if not raw:
                continue
            try:
                rec = json.loads(raw)
            except json.JSONDecodeError as exc:
                raise SystemExit(f"{path}:{lineno}: invalid JSON: {exc}")
            label = rec.get("label")
            if label not in VALID_LABELS:
                raise SystemExit(
                    f"{path}:{lineno}: label must be one of {sorted(VALID_LABELS)}, got {label!r}"
                )
            for field in ("question_id", "fact_id", "fact_text", "answer"):
                if not rec.get(field):
                    raise SystemExit(f"{path}:{lineno}: missing required field {field!r}")
            rec.setdefault("required_tokens", [])
            entries.append(rec)
    if not entries:
        raise SystemExit(f"{path}: gold set is empty")
    return entries


def evaluate(entries: list[dict]) -> dict:
    """Run the judge over every gold entry and tally the confusion matrix.

    Positive class is ``covered``: a "true positive" is the judge calling a
    fact covered when the gold label also says covered.
    """
    results = []
    tp = fp = fn = tn = 0
    for rec in entries:
        match = judge_report.fact_match(
            rec["fact_text"], rec["answer"], list(rec.get("required_tokens", []))
        )
        judge_covered = bool(match.covered)
        gold_covered = rec["label"] == "covered"
        if judge_covered and gold_covered:
            tp += 1
            outcome = "TP"
        elif judge_covered and not gold_covered:
            fp += 1
            outcome = "FP"
        elif not judge_covered and gold_covered:
            fn += 1
            outcome = "FN"
        else:
            tn += 1
            outcome = "TN"
        results.append(
            {
                "question_id": rec["question_id"],
                "fact_id": rec["fact_id"],
                "gold_label": rec["label"],
                "judge_covered": judge_covered,
                "outcome": outcome,
            }
        )

    total = len(entries)
    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = (
        2 * precision * recall / (precision + recall)
        if (precision + recall)
        else 0.0
    )
    agreement = (tp + tn) / total if total else 0.0
    return {
        "gold_entries": total,
        "gold_covered": sum(1 for r in entries if r["label"] == "covered"),
        "gold_not_covered": sum(1 for r in entries if r["label"] == "not_covered"),
        "confusion": {
            "true_positive": tp,
            "false_positive": fp,
            "false_negative": fn,
            "true_negative": tn,
        },
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1": round(f1, 4),
        "agreement": round(agreement, 4),
        "results": results,
    }


def print_report(summary: dict, gold_path: Path) -> None:
    conf = summary["confusion"]
    print("=" * 64)
    print("Judge calibration report (judge fact_match vs. gold labels)")
    print("=" * 64)
    print(f"gold set            : {gold_path}")
    print(f"gold entries        : {summary['gold_entries']}")
    print(
        f"  covered / not      : {summary['gold_covered']} / {summary['gold_not_covered']}"
    )
    print("confusion matrix (positive class = covered):")
    print(f"  true  positive    : {conf['true_positive']}")
    print(f"  false positive    : {conf['false_positive']}  (judge over-credits)")
    print(f"  false negative    : {conf['false_negative']}  (judge under-credits)")
    print(f"  true  negative    : {conf['true_negative']}")
    print(f"precision           : {summary['precision']:.4f}")
    print(f"recall              : {summary['recall']:.4f}")
    print(f"f1                  : {summary['f1']:.4f}")
    print(f"overall agreement   : {summary['agreement']:.4f}  "
          f"({summary['agreement'] * 100:.1f}%)")
    disagreements = [r for r in summary["results"] if r["outcome"] in ("FP", "FN")]
    print(f"disagreements       : {len(disagreements)} / {summary['gold_entries']}")
    for row in disagreements:
        print(
            f"  [{row['outcome']}] {row['question_id']:>10s} {row['fact_id']:>4s}  "
            f"gold={row['gold_label']:<11s} judge_covered={row['judge_covered']}"
        )
    print("=" * 64)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Measure agreement between the rule judge and the gold set."
    )
    parser.add_argument(
        "--gold",
        type=Path,
        default=DEFAULT_GOLD,
        help=f"path to the judge gold set JSONL (default: {DEFAULT_GOLD})",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=DEFAULT_REPORT,
        help=f"path to write the JSON report (default: {DEFAULT_REPORT})",
    )
    args = parser.parse_args(argv)

    gold_path = args.gold.resolve()
    if not gold_path.is_file():
        raise SystemExit(f"gold set not found: {gold_path}")

    entries = load_gold(gold_path)
    summary = evaluate(entries)
    print_report(summary, gold_path)

    report_path = args.report.resolve()
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_doc = {"gold_set": str(gold_path), **summary}
    report_path.write_text(
        json.dumps(report_doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"report written to   : {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
