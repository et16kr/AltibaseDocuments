# Job 04 — IMG-04 Build-sidecar integration and shard rebuild

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Spec: `GPTs/reports/image_content_recovery_spec_20260522.md` — Phase 3,
  decisions **D1** (build-stage sidecar) and **D2** (keep the link, add text
  beside it).
- Input: `GPTs/image_recovery/image_conversions.jsonl` (IMG-03).
- The source-pack build depends on `~/AID`; see `GPTs/AID_DEPENDENCY.md`.

## Task

Wire the conversion sidecar into the build so the recovered text reaches the
upload-package shards, **without modifying any original document**.

0. **Baseline precondition.** If a previous attempt of this job left local
   edits to the build scripts, discard them first
   (`git checkout -- GPTs/source_pack/scripts/`) so you start from the committed
   baseline. Then run `build_source_manifest.py --check` and
   `build_source_pack.py --check` on the unmodified build. If either fails, the
   committed baseline does not reproduce from the current `~/AID` — **STOP and
   FAIL** with that reason; do not proceed (a stale baseline would make this
   job's diff unverifiable).
1. Treat `GPTs/image_recovery/image_conversions.jsonl` as a build-stage
   **sidecar**. The `Manuals/` originals stay byte-unchanged (decision D1).
   Each sidecar record carries `ref_id`, `source_md`, and `line_no`; join to
   `image_inventory.tsv` by `ref_id` if more reference context is needed, and
   target each injection by `(source_md, line_no, image_path_raw)` so repeated
   identical references are disambiguated.
2. Modify the source-pack build
   (`GPTs/source_pack/scripts/build_source_manifest.py` and/or
   `build_source_pack.py`) so that, during extraction, at each image reference
   that has a sidecar conversion record, the original `![]()` / `<img>`
   reference is **kept** and the recovered text is inserted **immediately after
   it** (decision D2). References with no sidecar record are untouched.
3. Rebuild and verify deterministically:
   ```
   python3 GPTs/source_pack/scripts/build_source_manifest.py --write
   python3 GPTs/source_pack/scripts/build_source_pack.py --write
   python3 GPTs/source_pack/scripts/build_source_manifest.py --check
   python3 GPTs/source_pack/scripts/build_source_pack.py --check
   ```
4. Confirm the regenerated `GPTs/source_pack/` and `GPTs/upload_package/` shards
   carry, at every converted reference site, both the original link and the
   recovered text.

## Cross-effect note (record, do not act on)

Rebuilding `GPTs/upload_package/` changes the corpus the answerability harness
runs against. Re-baselining that harness is **out of scope** for this job —
note it in the result so it is not forgotten.

## Constraints (non-negotiable)

- `Manuals/` originals MUST stay byte-unchanged.
- Only the build scripts and the regenerated `GPTs/source_pack/` /
  `GPTs/upload_package/` artifacts may change. Non-converted reference sites
  must be unchanged.
- Do not run `run-all.sh` or other jobs' files.

## Acceptance checks

```bash
python3 GPTs/source_pack/scripts/build_source_manifest.py --check
python3 GPTs/source_pack/scripts/build_source_pack.py --check
# Manuals/ originals untouched:
git diff --name-only -- Manuals/ | (! grep .) && echo "Manuals untouched OK"
git diff --check
```

For PASS: both build `--check` commands pass, the converted reference sites in
the rebuilt shards carry the link plus the recovered text, the `Manuals/` tree
is byte-unchanged, and a non-converted reference site spot-check shows its text
unchanged.

## Completion protocol

As your final action:

- Ensure `GPTs/image_recovery/state/` exists.
- If the acceptance checks passed, write `GPTs/image_recovery/state/04.result`
  with first line `PASS` and a short summary (sidecar records applied, shards
  rebuilt, and the answerability re-baseline reminder).
- Otherwise write the same file with first line `FAIL: <one-line reason>`.
