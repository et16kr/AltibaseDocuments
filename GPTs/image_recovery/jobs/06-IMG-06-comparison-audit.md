# Job 06 — IMG-06 Conversion comparison audit

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Spec: `GPTs/reports/image_content_recovery_spec_20260522.md` — Phase 5.
- Inputs: `GPTs/image_recovery/image_conversions.jsonl` (IMG-03),
  `GPTs/image_recovery/image_classification.tsv` (IMG-02), the rendered rasters
  under `Manuals/.../media/`, and the manuals' `PDF/` folders.

## Task

Independently verify that each converted graph **faithfully represents its
source image**, by visual comparison of the original image against the
conversion. This is the conversion-fidelity check; it is read-only.

1. **Audit scope.**
   - Class **D** (tables) and class **E** (flowcharts): audit **100%** of
     conversions.
   - Class **C** (syntax/railroad diagrams): audit a **stratified sample** —
     at least 25% of C conversions and at least 40 images, spread across the
     source manuals; if C has fewer than 40 conversions, audit all of them.
   - Always audit **every** conversion that IMG-03 marked `verified:false`,
     regardless of class.
   - Class **A/B** (classified redundant, never converted): audit a
     **stratified sample** — at least 10% and at least 30 images across the
     manuals. A C/D/E diagram mislabelled A/B is never converted, so its
     information is lost silently and no conversion exists to compare; this
     sample is the only check against that failure mode. Treat a misclassified
     A/B (the image genuinely carries unique non-redundant content) as a
     `material` finding.
2. **Compare.** For each audited reference: open the original raster with the
   image-reading tool, read the conversion's `converted_text`, and compare:
   - **E** — every node, edge, label, and branch direction.
   - **D** — every header and cell.
   - **C** — every grammar path, token, and optional/mandatory marker.
   - **A/B** — there is no `converted_text`; instead open the image and its
     inventory `context` and confirm the image content is genuinely redundant
     with the adjacent syntax block (A) or prose (B). If the image carries
     unique content, the classification is wrong.
   If a `.gif` raster cannot be opened, convert it to PNG into a scratch temp
   directory with ImageMagick (`convert`) and read that — never modify the
   original. If the raster is unreadable, fall back to the manual's PDF. For
   class E you may additionally render `converted_text` with `mmdc`
   (mermaid-cli) into the scratch dir for a side-by-side visual compare if the
   tool is available; otherwise do a structural compare.
3. **Verdict per audited image:** `match` | `minor` (cosmetic or ordering
   difference, no information lost) | `material` (a missing or wrong node,
   edge, cell, token, or a reversed direction) | `uncertain` (raster and PDF
   both unreadable).
4. Write ledger rows resumably — append as you go and, on a re-run, skip
   `ref_id`s already audited so an interrupted run resumes rather than
   re-auditing every image. Write the audit ledger
   `GPTs/image_recovery/image_comparison_audit.tsv`
   (header + `ref_id`, `class`, `verdict`, `detail`) and the report
   `GPTs/reports/image_content_recovery_comparison_audit_20260522.md`:
   per-verdict counts, audit coverage per class, and **every** `material` and
   `uncertain` case listed with its specific discrepancy.

## Constraints (non-negotiable)

- Read-only audit: do NOT modify `image_conversions.jsonl`, the originals,
  `GPTs/source_pack/`, `GPTs/upload_package/`, or build scripts.
- `gif`→`png` scratch conversions go to a temp directory only.
- Do not run `run-all.sh` or other jobs' files.

## Acceptance checks

```bash
test -f GPTs/reports/image_content_recovery_comparison_audit_20260522.md
test -s GPTs/image_recovery/image_comparison_audit.tsv
git diff --check
```

For PASS: D and E are audited 100%, the C sample meets the ratio above, and the
audit finds **zero `material` mismatches**. If any `material` mismatch is found,
write `FAIL` — the conversions must be corrected (re-run IMG-03 / fix the
sidecar) and jobs IMG-04 → IMG-06 re-run. `minor` verdicts are logged but do not
fail; `uncertain` cases are listed for follow-up and do not fail on their own.

## Completion protocol

As your final action:

- Ensure `GPTs/image_recovery/state/` exists.
- If the acceptance checks passed and there are zero `material` mismatches,
  write `GPTs/image_recovery/state/06.result` with first line `PASS` and a
  short summary (per-verdict counts, audit coverage per class).
- Otherwise write the same file with first line `FAIL: <one-line reason>` and
  list the `material` mismatches in the result.
