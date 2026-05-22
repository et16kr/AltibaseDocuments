# Job 05 — IMG-05 Validation and documentation

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Spec: `GPTs/reports/image_content_recovery_spec_20260522.md` — Phase 4.
- Prior jobs produced the inventory, classification, conversion sidecar, and the
  rebuilt `GPTs/upload_package/` shards (IMG-01 … IMG-04).

## Task

Validate the rebuilt package and document the image-recovery mechanism.

1. **Spot-check converted sites.** For a representative sample of C/D/E
   references across the affected manuals, confirm in the rebuilt
   `GPTs/upload_package/` shards that the site carries both the original
   `![]()` / `<img>` reference and the recovered text, and that the recovered
   text matches the `image_conversions.jsonl` record.
2. **Regression check.** `git diff` the rebuilt `GPTs/source_pack/` and
   `GPTs/upload_package/` shards against the repository state from before IMG-04
   ran — current `HEAD` if IMG-04 committed nothing, otherwise the commit before
   IMG-04's checkpoint — and confirm **every** changed hunk sits at a C/D/E
   reference site that gained recovered text: no non-C/D/E reference site, and
   no non-image content, changed.
3. **Update docs.** Update `GPTs/source_pack/README.md` and
   `GPTs/upload_package/00_README_SOURCE_PRESERVING_UPLOAD.md` to describe the
   image-recovery sidecar: what classes are recovered, that originals are
   unmodified, and where the sidecar (`GPTs/image_recovery/`) and spec live.
4. **Write the validation report**
   `GPTs/reports/image_content_recovery_validation_20260522.md`: spot-check
   results, the regression check, counts of recovered references by class, and
   any residual flagged (unverified) conversions carried over from IMG-03.

## Constraints (non-negotiable)

- `Manuals/` originals MUST stay byte-unchanged.
- Do not re-run the IMG-04 build here; this job validates and documents.
- Do not run `run-all.sh` or other jobs' files.

## Acceptance checks

```bash
test -f GPTs/reports/image_content_recovery_validation_20260522.md
git diff --name-only -- Manuals/ | (! grep .) && echo "Manuals untouched OK"
git diff --check
```

For PASS: the spot-checks confirm converted sites carry the link plus recovered
text, the regression check shows no unintended change, the two READMEs are
updated, and the validation report is present.

## Completion protocol

As your final action:

- Ensure `GPTs/image_recovery/state/` exists.
- If the acceptance checks passed, write `GPTs/image_recovery/state/05.result`
  with first line `PASS` and a short summary (spot-check outcome, recovered
  references by class, residual flagged conversions).
- Otherwise write the same file with first line `FAIL: <one-line reason>`.
