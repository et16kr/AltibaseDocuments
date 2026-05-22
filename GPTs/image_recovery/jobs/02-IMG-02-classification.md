# Job 02 — IMG-02 Image classification and audit

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Spec: `GPTs/reports/image_content_recovery_spec_20260522.md` — Phase 1 and the
  class taxonomy in §4.
- Input: `GPTs/image_recovery/image_inventory.tsv` (produced by IMG-01).

## Task

Classify every inventoried image reference, **in its document context**, into
one of five classes (spec §4):

- **A** — syntax diagram redundant with an adjacent text `Syntax` code block.
- **B** — conceptual diagram redundant with the surrounding prose.
- **C** — railroad/syntax diagram that is the **only** source of the grammar.
- **D** — tabular data rendered as an image.
- **E** — true process/decision flowchart with branching logic not in prose.

Only C/D/E will later be converted; A/B are skipped.

1. **Rule pass.** Apply cheap deterministic rules over the inventory `context`
   column first — e.g. an image immediately followed by a fenced code block
   under a `Syntax` heading is class A. Record which rule decided each row.
2. **Sampled validation.** Manually review a representative sample (open the
   actual raster with the image-reading tool) to confirm the rules; tighten any
   rule that misfires. Err toward **C/D/E** when a call is uncertain — a wrong
   A/B silently drops unique information.
3. **Residual pass.** Classify rows the rules cannot decide by reading the
   raster image and its context. If the image-reading tool cannot open a `.gif`
   (or any) raster, convert it to PNG into a scratch temp directory with
   ImageMagick (`convert`) and read that — never modify the original. Write
   classification rows resumably so an interrupted run can resume rather than
   reclassify every row.
4. Write `GPTs/image_recovery/image_classification.tsv`, one row per inventory
   `ref_id`, header + tab-separated columns: `ref_id`, `class` (A–E),
   `decided_by` (rule id or `vision`), `rationale` (one line),
   `raster_readable` (`yes`/`low_res`/`missing`).
5. Write the audit report `GPTs/reports/image_content_audit_20260522.md`:
   per-class counts, a recoverable-information estimate (how much C/D/E content
   is currently lost), two or three worked examples per class, and the count of
   rasters flagged `low_res`/`missing`.

## Stop/go note

If C + D + E together are negligible, this job still **PASSes** — but the result
line and the audit report must state plainly that IMG-03/04 would recover
little, so the user can decide whether to continue the runner.

## Constraints (non-negotiable)

- Do NOT convert images, modify originals, `GPTs/source_pack/`,
  `GPTs/upload_package/`, or build scripts.
- Do not run `run-all.sh` or other jobs' files.

## Acceptance checks

```bash
test -s GPTs/image_recovery/image_classification.tsv
test -f GPTs/reports/image_content_audit_20260522.md
# Every inventory row must be classified exactly once:
inv=$(( $(grep -c . GPTs/image_recovery/image_inventory.tsv) - 1 ))
cls=$(( $(grep -c . GPTs/image_recovery/image_classification.tsv) - 1 ))
echo "inventory=$inv classified=$cls"   # must match
git diff --check
```

For PASS: classification covers 100% of inventory rows into A–E, the audit
report is present with per-class counts and the recoverable-information
estimate.

## Completion protocol

As your final action:

- Ensure `GPTs/image_recovery/state/` exists.
- If the acceptance checks passed, write `GPTs/image_recovery/state/02.result`
  with first line `PASS` and a short summary (per-class counts, the C/D/E total,
  and the stop/go assessment).
- Otherwise write the same file with first line `FAIL: <one-line reason>`.
