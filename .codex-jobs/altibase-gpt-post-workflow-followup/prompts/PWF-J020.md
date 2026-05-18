# Job PWF-J020: Protected Remediation Backup Recovery

## Goal

Fix or justify `backup_recovery` protected blockers.

## Steps

1. Run the required first checks from `AGENTS.md`.
2. Use `protected_blocker_classification_20260518.md` as the primary scope owner and
   `GPTs/reports/full_coverage_audit/replacement_grade_gap_register_20260518.md` as the cross-document policy scope.
3. Remediate source-backed backup/recovery gaps in operations, errors, views, or
   properties attachments as classified.
4. Require exact version, archive mode, backup type, current state, log/datafile
   evidence, and recovery objective before risky guidance.
5. Run structural checks and targeted validation for the scoped question IDs. If live
   targeted validation cannot run, create an explicit blocker report.
6. Run repository validation, review the diff, and commit.

## Acceptance Criteria

- Scoped backup/recovery blockers are fixed or safely justified.
- Assigned replacement-grade backup/recovery gaps are fixed, blocked with evidence, or
  explicitly deferred with owner rationale.
- Targeted validation ran, or a blocker report explains why it could not.
- Project files are clean after the focused commit.
