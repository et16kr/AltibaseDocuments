# Job PWF-J001: Benchmark Evidence Lock

## Goal

Record `altibase_answerability_20260518_091947` as the official post-workflow full
benchmark evidence baseline. Do not remediate attachment content in this job.

## Steps

1. Run the required first checks from `AGENTS.md`.
2. Inspect the latest run artifacts under
   `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260518_091947/`.
3. Create `GPTs/reports/full_coverage_audit/post_workflow_benchmark_lock_20260518.md`.
4. Record run configuration, artifact paths, overall metrics, domain rates, protected
   blockers, and the `blocking_gaps` decision.
5. Run `git diff --check` and `bash review/scripts/run_review_stage.sh validate`.
6. Review the diff and create a focused commit.

## Acceptance Criteria

- Benchmark evidence is locked in a self-contained repo document.
- No `GPTs/attachments/` remediation is mixed into this job.
- Validation passes or skipped checks are explained.
- Project files are clean after the focused commit.
