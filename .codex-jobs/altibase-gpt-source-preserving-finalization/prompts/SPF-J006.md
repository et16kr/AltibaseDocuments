# Job SPF-J006: Package-aware benchmark harness

## Goal

Retarget benchmark tooling or manifests so the existing 270-question benchmark
can dry-run against `GPTs/upload_package_source_preserving/` without changing
existing questions, expected answers, or judge policy.

## Scope

- Work only on this job.
- Read `.codex-jobs/altibase-gpt-source-preserving-finalization/prompts/common-source-preserving-finalization.md` first.
- Do not change files under `evals/altibase_answerability/questions/` for the
  existing 270-question benchmark.
- Do not run a live benchmark.

## Required Steps

1. Inspect `full_benchmark.json`, benchmark schemas, `answer_runner.py`, and the
   S4-J010 rerun note.
2. Add a package-aware manifest or manifest option for
   `GPTs/upload_package_source_preserving/*.md`.
3. Update benchmark tooling only as needed to allow a safe package-rooted dry run
   while preserving:
   - unchanged 270 questions;
   - unchanged expected answers and judge policy;
   - answer-input allowlisting;
   - judge-only leakage protection;
   - explicit context-root allowlisting.
4. Write or update a package-context rerun note under
   `evals/altibase_answerability/reports/full_benchmark/`.
5. Self-review for leakage regressions and accidental baseline mutation.
6. Run targeted checks:
   - source-preserving validator from `SPF-J003`;
   - `python3 evals/altibase_answerability/scripts/validate_benchmark.py --manifest <new-package-aware-manifest>`;
   - `python3 evals/altibase_answerability/scripts/answer_runner.py --self-test`;
   - `python3 evals/altibase_answerability/scripts/judge_report.py --self-test`;
   - package-aware dry run with `--mode dry_run --context-mode lexical --validate-output`;
   - `git diff --check -- evals/altibase_answerability GPTs/reports`.
7. Review the final diff.
8. Commit with a focused message such as:

```text
evals: add source-preserving package dry-run route
```

## Acceptance Criteria

- Existing 270 benchmark records are unchanged.
- A package-aware manifest or option targets
  `GPTs/upload_package_source_preserving/*.md`.
- A dry run against the source-preserving package succeeds.
- No live benchmark pass is claimed.
- The job creates a focused commit and leaves project files clean.
