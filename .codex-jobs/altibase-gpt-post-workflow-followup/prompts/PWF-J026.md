# Job PWF-J026: Domain Remediation SQL Data Types

## Goal

Remediate classified SQL/DDL/DML/data type failures.

## Steps

1. Run the required first checks from `AGENTS.md`.
2. Use `residual_failure_classification_20260518.md` as the primary scope owner and
   `GPTs/reports/full_coverage_audit/replacement_grade_gap_register_20260518.md` as the cross-document policy scope.
3. Preserve exact grammar tokens, examples, privileges, destructive effects, data type
   restrictions, version boundaries, and validation SQL.
4. Run targeted validation for scoped question IDs, or create an explicit not-ready report.
5. Run repository validation, review the diff, and commit.

## Acceptance Criteria

- Scoped SQL/data type failures are improved, fixed, or explicitly documented as blocked.
- Assigned replacement-grade SQL/data-type gaps are fixed, blocked with evidence, or
  explicitly deferred with owner rationale.
- Targeted validation evidence exists.
- Project files are clean after the focused commit.
