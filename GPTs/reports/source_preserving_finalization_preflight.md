# Source-Preserving Finalization Preflight

- Job: `SPF-J001`
- Date: 2026-05-19
- Scope: preflight and package-boundary gate for
  `GPTs/upload_package_source_preserving/`
- Verdict: `ready_for_spf_j002`

## Boundary

The primary source-preserving package for this finalization cycle is:

`GPTs/upload_package_source_preserving/`

The existing compact topic package remains:

`GPTs/upload_package/`

The source evidence baseline for this preflight is:

`GPTs/source_pack/`

This job did not edit source package shard content. The next jobs may normalize
wrapper/header text or add retrieval metadata outside source bodies, but they must
not change bytes inside any `SOURCE_BLOCK_BEGIN` / `SOURCE_BLOCK_END` source body.
After wrapper normalization, validation must compare source-block body integrity
against recorded source metadata rather than requiring whole-shard byte equality.

## Committed Baseline

The finalization plan records the initial source-preserving package baseline as
`5af19e71 Add source-preserving GPT upload package`.

The current committed repository baseline before this preflight report was:

`4e3401ac Improve finalization workflow resume handling`

The required worktree stop gate was checked before editing. No uncommitted project
files outside `.codex-jobs/` workflow files were present. The pre-existing
`.codex-jobs/altibase-gpt-source-preserving-finalization/jobs.tsv` modification was
left untouched.

## Package Facts

| Fact | Result |
| --- | --- |
| Source-preserving package file count | Pass: `20` files under `GPTs/upload_package_source_preserving/`. |
| Source shard presence | Pass: `source_pack_shard_001.md` through `source_pack_shard_016.md` are present. |
| Pre-normalization shard equality | Pass: all `16` package shard files byte-match the corresponding files in `GPTs/source_pack/`. No wrapper differences are present yet. |
| Package bytes | `59,719,357` bytes across the 20 package files. |
| Selected source count | `941` rows in `02_source_manifest.md`; this matches `GPTs/source_pack/source_pack_validation.md`. |
| Source-to-shard rows | `941` rows in `03_source_to_shard_manifest.md`. |
| Source-block markers | `941` `SOURCE_BLOCK_BEGIN` markers and `941` `SOURCE_BLOCK_END` markers with `BLOCK-*` IDs across the 16 shard files. |
| Shard manifest coverage | `941` unique sources across `16` unique shard IDs; all rows have `validation_status=pass`. |
| Current shard upload-intended values | `upload_intended=no` in the copied source-pack manifest rows. This is expected pre-normalization evidence-layer wording for `SPF-J001`; `SPF-J002` must replace or normalize upload-facing wrapper language without changing source bodies. |

## Live Benchmark Gate

No live 270-question benchmark approval has been recorded for this source-preserving
package finalization cycle.

The checked references only record the approval requirement and the absence of a
package-context live run:

- `.codex-jobs/altibase-gpt-source-preserving-finalization/prompts/common-source-preserving-finalization.md`
  requires explicit operator approval and an output path before any live 270-question
  benchmark.
- `GPTs/reports/stage_04_retrieval_dry_run.md` records no live benchmark pass and
  says future package-specific live benchmarking requires explicit approval before
  starting.
- `evals/altibase_answerability/reports/full_benchmark/package_context_rerun_note_s4_j010_20260519.md`
  records that no package-context live benchmark was started.

Therefore this job preserves the live-benchmark boundary: do not run a live
270-question benchmark until operator approval and the intended output path are
recorded before execution.

## Source-Pack Validator Note

The committed `GPTs/source_pack/source_pack_validation.md` records a previous
`Verdict: Pass` for `941` selected sources, `16` shards, and `8,767` exclusions.

An extra local attempt to run `python3 GPTs/source_pack/scripts/validate_source_pack.py`
in this workspace did not complete because `/home/et16/AID` is not present in the
current execution environment while the source manifest references `~/AID/...`
inputs. This is not treated as a package-boundary blocker for `SPF-J001`, because
the required preflight checks compare the committed source-preserving package to the
committed `GPTs/source_pack/` baseline. Any future source-pack rebuild or
external-source revalidation must mount or restore the `~/AID` corpus first.

## Targeted Checks

| Check | Command | Result |
| --- | --- | --- |
| File-count check | `find GPTs/upload_package_source_preserving -maxdepth 1 -type f` | Pass: 20 files. |
| Shard presence and byte-match check | SHA-256 comparison of package shards against `GPTs/source_pack/source_pack_shard_*.md` | Pass: 16 present, 16 byte-identical, 0 differences. |
| Source/block count check | Parse `02_source_manifest.md`, `03_source_to_shard_manifest.md`, and shard block markers | Pass: 941 selected sources, 941 source-to-shard rows, 941 begin markers, 941 end markers. |
| Live benchmark approval search | `rg` over job prompts, finalization reports, and full-benchmark package-context notes | Pass: only approval requirements and no-live-run statements found; no approval record found. |
| Whitespace check | `git diff --check -- GPTs/reports/source_preserving_finalization_preflight.md` | Pass. |

## Self-Review

- Paths are repository-relative and point to the active source-preserving package,
  compact topic package, source-pack baseline, and benchmark notes.
- The report distinguishes the plan's initial package commit from the current
  committed repository baseline.
- The source-integrity rule is stated as a source-body byte-preservation rule, not as
  a permanent whole-shard SHA requirement after wrapper normalization.
- The live benchmark approval boundary is explicit, and no live benchmark result is
  claimed.
- `SPF-J002` is ready to proceed with wrapper/header normalization and a dedicated
  source-body integrity validator, subject to preserving source-block body bytes.
