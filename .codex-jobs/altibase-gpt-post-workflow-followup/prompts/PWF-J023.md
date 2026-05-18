# Job PWF-J023: Protected-Topic Targeted Validation

## Goal

Run or record targeted validation for all protected-topic remediation jobs.

## Steps

1. Run the required first checks from `AGENTS.md`.
2. Build a targeted question list from `protected_blocker_classification_20260518.md`.
3. Run dry-run validation and live targeted checks for every protected-topic class, or
   write an explicit blocker section explaining why a check cannot be executed.
4. Create `GPTs/reports/full_coverage_audit/protected_topic_targeted_validation_20260518.md`.
5. If any protected blockers remain, record exact blocker IDs and stop before residual
   domain remediation unless they are safe-stop justified.
6. Run repository validation, review the diff, and commit.

## Acceptance Criteria

- Protected-topic validation evidence is recorded for every protected-topic class, or
  an explicit execution blocker is documented.
- Remaining protected blockers are `0` or explicitly safe-stop justified.
- Project files are clean after the focused commit.
