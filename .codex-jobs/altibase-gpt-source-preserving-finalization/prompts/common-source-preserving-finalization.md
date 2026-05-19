# Common Context: Source-Preserving Package Finalization

Read this common context before the job-specific scope.

## Primary Objective

Finalize `GPTs/upload_package_source_preserving/` as the primary source corpus for
Altibase GPT Knowledge, Codex, and LLM/RAG usage. The package must behave as an
Altibase encyclopedia while preserving selected source content.

## Required References

Read these before editing in every job:

- `GPTs/reports/source_preserving_upload_package_finalization_plan.md`
- `GPTs/reports/source_preserving_upload_package_remediation.md`
- `GPTs/upload_package_source_preserving/00_README_SOURCE_PRESERVING_UPLOAD.md`
- `GPTs/reports/stage_04_retrieval_dry_run.md`
- `evals/altibase_answerability/reports/full_benchmark/package_context_rerun_note_s4_j010_20260519.md`

Also inspect the local files directly relevant to the job before editing.

## Boundaries

- Primary package: `GPTs/upload_package_source_preserving/`
- Existing compact topic package: `GPTs/upload_package/`
- Source evidence baseline: `GPTs/source_pack/`
- Existing 270-question benchmark: `evals/altibase_answerability/manifests/full_benchmark.json`
- Do not change existing 270 benchmark questions or expected answers.
- Do not run a live 270-question benchmark unless explicit operator approval and
  output path are recorded before starting. Dry-runs and schema/self-tests are allowed.

## Source Integrity Rule

The final upload package may normalize wrapper/header text and add retrieval
metadata outside source blocks. It must not change bytes inside any
`SOURCE_BLOCK_BEGIN` / `SOURCE_BLOCK_END` source body.

After wrapper/header normalization, whole shard-file SHA-256 values may differ
from `GPTs/source_pack/`. Validation must therefore check source-block body
integrity using recorded source metadata, not whole-file equality, unless the job
is explicitly comparing the current pre-normalization baseline.

## Required Job Behavior

- Work only on the current job.
- Preserve unrelated user changes.
- Add or update focused checks appropriate for the job.
- Run `git diff --check` on changed paths.
- Review the final diff before committing.
- Before the final commit, mark the current job `Done` in
  `.codex-jobs/altibase-gpt-source-preserving-finalization/jobs.tsv` and
  `.codex-jobs/altibase-gpt-source-preserving-finalization/jobs.md`.
- Create one focused commit for the job that includes both the scoped project output
  and the workflow status update.
- Leave project files clean after the commit.
