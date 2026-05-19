# Job SPF-J001: Preflight and package boundary gate

## Goal

Verify that the source-preserving package is a valid baseline for finalization,
record the package/edit boundaries, and keep the live-benchmark approval boundary
explicit before any package edits.

## Scope

- Work only on this job.
- Read `.codex-jobs/altibase-gpt-source-preserving-finalization/prompts/common-source-preserving-finalization.md` first.
- Do not edit source package shard content in this job.
- Write or update `GPTs/reports/source_preserving_finalization_preflight.md`.

## Required Steps

1. Reconfirm the finalization plan and current committed baseline.
2. Inspect `GPTs/upload_package_source_preserving/`, `GPTs/source_pack/`, source
   manifests, and the Stage 4 dry-run/rerun notes.
3. Verify current package facts:
   - exactly 20 files in `GPTs/upload_package_source_preserving/`;
   - 16 source shard files are present;
   - current pre-normalization shard files still match `GPTs/source_pack/` or
     record any wrapper differences found;
   - selected source count and source-block count are recorded;
   - no live benchmark approval has been recorded.
4. Write the preflight report with a clear `ready_for_spf_j002` or
   `blocked` verdict.
5. Self-review for inaccurate paths, outdated claims, and missing gates.
6. Run targeted checks:
   - file-count check for `GPTs/upload_package_source_preserving/`;
   - shard presence check;
   - `git diff --check -- GPTs/reports/source_preserving_finalization_preflight.md`.
7. Review the final diff.
8. Commit with a focused message such as:

```text
source-preserving: add finalization preflight gate
```

## Acceptance Criteria

- `GPTs/reports/source_preserving_finalization_preflight.md` exists.
- The report states the package boundary, source-integrity rule, live-benchmark
  approval boundary, and next job readiness.
- Checks pass or any blocker is explicitly recorded.
- The job creates a focused commit and leaves project files clean.
