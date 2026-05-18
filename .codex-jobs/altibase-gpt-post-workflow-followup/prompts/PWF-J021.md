# Job PWF-J021: Protected Remediation Destructive SQL

## Goal

Fix or justify `destructive_sql` protected blockers.

## Steps

1. Run the required first checks from `AGENTS.md`.
2. Use `protected_blocker_classification_20260518.md` as the primary scope owner and
   `GPTs/reports/full_coverage_audit/replacement_grade_gap_register_20260518.md` as the cross-document policy scope.
3. Remediate source-backed destructive SQL gaps in SQL, operations, or error attachments.
4. Include object confirmation, stop conditions, privilege/scope caveats, and validation SQL.
5. Run structural checks and targeted validation for the scoped question IDs. If live
   targeted validation cannot run, create an explicit blocker report.
6. Run repository validation, review the diff, and commit.

## Acceptance Criteria

- Scoped destructive SQL blockers are fixed or safely justified.
- Assigned replacement-grade destructive-SQL gaps are fixed, blocked with evidence, or
  explicitly deferred with owner rationale.
- Targeted validation ran, or a blocker report explains why it could not.
- Project files are clean after the focused commit.
