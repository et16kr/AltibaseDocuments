# Job SPF-J007: Coding-agent benchmark extension

## Goal

Add a separate coding-agent benchmark question set, manifest, and rubric that
tests practical Codex/LLM agent use of the source-preserving package.

## Scope

- Work only on this job.
- Read `.codex-jobs/altibase-gpt-source-preserving-finalization/prompts/common-source-preserving-finalization.md` first.
- Keep the coding-agent benchmark distinct from the existing 270 answerability
  baseline.
- Do not mutate existing 270-question files or expected answers.

## Required Steps

1. Inspect existing benchmark question schemas, manifests, policies, and reports.
2. Add a coding-agent question set that covers:
   - source-grounded repository/code navigation;
   - Altibase SQL/iSQL script generation with manual-path citation;
   - JDBC/CLI/ODBC/API usage;
   - error diagnosis from exact messages or codes;
   - property and version checks;
   - replication, backup/recovery, destructive-operation, and security safety
     gates;
   - required citation of `source_id`, `source_path`, `version_scope`, and
     relevant block or manual evidence.
3. Add a manifest for the coding-agent benchmark that uses the source-preserving
   package context.
4. Add or update a judge rubric/report documenting expected artifacts and pass
   criteria for coding-agent tasks.
5. Extend schemas or runner support only if necessary, keeping backward
   compatibility with existing manifests.
6. Self-review for overlap with the original 270 benchmark and for unsafe
   prompts that would encourage destructive actions.
7. Run targeted checks:
   - source-preserving validator from `SPF-J002`;
   - benchmark schema validation for the new coding-agent manifest;
   - answer-runner and judge self-tests;
   - dry run for the coding-agent manifest;
   - `git diff --check -- evals/altibase_answerability GPTs/reports`.
8. Review the final diff.
9. Commit with a focused message such as:

```text
evals: add source-preserving coding agent benchmark
```

## Acceptance Criteria

- A separate coding-agent question set and manifest exist.
- The existing 270-question benchmark remains comparable and unchanged.
- Coding-agent tasks require source-grounded artifacts and citation behavior.
- Dry-run validation passes.
- The job creates a focused commit and leaves project files clean.
