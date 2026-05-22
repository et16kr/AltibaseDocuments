# Job 03 — IMG-03 Convert C/D/E images

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Spec: `GPTs/reports/image_content_recovery_spec_20260522.md` — Phase 2,
  decision D4 (verification depth).
- Inputs: `GPTs/image_recovery/image_inventory.tsv` and
  `GPTs/image_recovery/image_classification.tsv` (IMG-01 / IMG-02).

## Task

Produce a **text rendition** of every image classified **C, D, or E** (skip A
and B entirely).

1. For each C/D/E reference, read the rendered raster image (located via
   `image_path_resolved` in `image_inventory.tsv`, joined by `ref_id`) and
   transcribe its content in the per-class format:
   - **C** (railroad/syntax diagram) → a BNF/EBNF grammar in a fenced code
     block.
   - **D** (tabular image) → a Markdown table.
   - **E** (flowchart) → a Mermaid `flowchart` block.
   Many C-class diagrams are `.gif`. If the image-reading tool cannot open a
   `.gif` (or any) raster, convert it to PNG into a scratch temp directory with
   ImageMagick (`convert`) and read that — never modify the original.
2. **Verification — D4: full per-image cross-check.** Every conversion must be
   verified against its rendered raster. Where the raster is too low-resolution
   to transcribe reliably, fall back to the manual's PDF rendition (the
   `Manuals/.../PDF/` folders — note these exist for the 7.1 / 7.3 trees but not
   necessarily for `Altibase_trunk`). If the content is still unreadable,
   **flag it — do not guess.**
3. Write `GPTs/image_recovery/image_conversions.jsonl`, one JSON record per
   C/D/E reference, with fields: `ref_id`, `class`, `source_md`, `line_no`
   (both carried from `image_inventory.tsv`, joined by `ref_id`),
   `image_path_raw`, `format` (`bnf`/`table`/`mermaid`), `converted_text`,
   `verified` (`true` only after the raster/PDF cross-check), `source_used`
   (`raster`/`pdf`), `notes` (empty, or the reason it could not be verified).
   `converted_text` must have no trailing whitespace on any line — IMG-04
   inserts it verbatim into shards that are checked with `git diff --check`.
4. **Write resumably.** This job may be large. Append records as you go and, on
   a re-run, skip references whose `ref_id` is already present in
   `image_conversions.jsonl` so an interrupted run resumes instead of redoing
   every conversion.

## Constraints (non-negotiable)

- Convert **only** C/D/E references. Do not touch A/B.
- Never invent diagram content — an unreadable image is flagged
  (`verified:false` with a `notes` reason), not guessed.
- Do NOT modify originals, `GPTs/source_pack/`, `GPTs/upload_package/`, or build
  scripts — this job only produces the conversion sidecar.
- Do not run `run-all.sh` or other jobs' files.

## Acceptance checks

```bash
test -s GPTs/image_recovery/image_conversions.jsonl
# One conversion record per C/D/E classification row:
cde=$(awk -F'\t' 'NR>1 && ($2=="C"||$2=="D"||$2=="E")' GPTs/image_recovery/image_classification.tsv | wc -l)
conv=$(grep -c . GPTs/image_recovery/image_conversions.jsonl)
echo "cde=$cde conversions=$conv"   # must match
python3 -c "import json,sys; [json.loads(l) for l in open('GPTs/image_recovery/image_conversions.jsonl')]; print('jsonl OK')"
git diff --check
```

For PASS: every C/D/E reference has a conversion record; each record is either
`verified:true` after a raster/PDF cross-check or explicitly flagged with a
reason; the JSONL is well-formed.

## Completion protocol

As your final action:

- Ensure `GPTs/image_recovery/state/` exists.
- If the acceptance checks passed, write `GPTs/image_recovery/state/03.result`
  with first line `PASS` and a short summary (conversions by class, count
  verified vs flagged, count that needed the PDF fallback).
- Otherwise write the same file with first line `FAIL: <one-line reason>`.
