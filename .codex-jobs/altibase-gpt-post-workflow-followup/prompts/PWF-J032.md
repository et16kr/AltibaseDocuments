# Job PWF-J032: Final Readiness Gate And Rerun

## Goal

Run final validation and the full live benchmark only when closure, replacement-grade,
protected-topic, domain-remediation, and developer/test-readiness gates are clean.

## Steps

1. Run the required first checks from `AGENTS.md`.
2. Verify active `Missing=0`, active `Retrieval-weak=0`, replacement-grade gaps
   assigned and closed or explicitly guarded, protected blockers clean or safe-stop
   justified, domain validation complete, developer/test readiness complete,
   repository validation passing, and worktree clean.
3. Run full coverage structural checks and repository validation.
4. If preconditions are met, run the full live benchmark using
   `evals/altibase_answerability/reports/full_benchmark/rerun_plan_j022_20260517.md`.
5. If preconditions are not met, do not force a benchmark; write a not-ready gate report.
6. Update final readiness reporting, review the diff, and commit.

## Acceptance Criteria

- Full rerun is executed only when prerequisites are clean.
- Replacement-grade and developer/test-readiness gates are clean or explicitly
  not-ready; unresolved gates block the rerun.
- Thresholds and benchmark questions are not weakened.
- Final report states pass/fail/blocking status and artifact paths.
- Project files are clean after the focused commit.
