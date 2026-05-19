# Job SPF-J008: Final validation and readiness review

## Goal

Run final deterministic validation, benchmark dry-runs, and write the readiness
report for the source-preserving upload package.

## Scope

- Work only on this job.
- Read `.codex-jobs/altibase-gpt-source-preserving-finalization/prompts/common-source-preserving-finalization.md` first.
- Do not run a live benchmark unless explicit operator approval and output path
  have already been recorded.
- Write `GPTs/reports/source_preserving_upload_package_readiness.md`.

## Required Steps

1. Review all prior SPF reports, commits, package files, validators, benchmark
   manifests, and dry-run notes.
2. Run final deterministic validation:
   - source-preserving package validator;
   - benchmark schema validation for the existing 270 package-aware manifest;
   - benchmark schema validation for the coding-agent manifest;
   - answer-runner self-test;
   - judge/report self-test;
   - dry run for the package-aware 270 benchmark;
   - dry run for the coding-agent benchmark.
3. Inspect outputs and record failures or residual risks without reinterpreting
   them as passes.
4. Write the readiness report with:
   - package file count and size summary;
   - source-body integrity result;
   - validator result;
   - benchmark dry-run results;
   - coding-agent benchmark coverage summary;
   - live-benchmark routing decision;
   - explicit ready/pass, conditional-ready, or blocker verdict.
5. Self-review for unsupported readiness claims.
6. Run `git diff --check -- GPTs/reports evals/altibase_answerability`.
7. Review the final diff.
8. Commit with a focused message such as:

```text
source-preserving: record final readiness review
```

## Acceptance Criteria

- Final readiness report exists and cites actual commands/results.
- No live benchmark pass is claimed unless a live run actually occurred with
  prior approval.
- Source-preserving package validation passes or blockers are explicit.
- Existing 270 and coding-agent dry-run status is recorded.
- The job creates a focused commit and leaves project files clean.
