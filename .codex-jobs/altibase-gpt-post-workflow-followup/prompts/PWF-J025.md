# Job PWF-J025: Domain Remediation Views Performance

## Goal

Remediate classified views/performance/monitoring failures.

## Steps

1. Run the required first checks from `AGENTS.md`.
2. Use `residual_failure_classification_20260518.md` as the primary scope owner and
   `GPTs/reports/full_coverage_audit/replacement_grade_gap_register_20260518.md` as the cross-document policy scope.
3. Update only the scoped attachment/support files.
4. Preserve exact view names, column names, check SQL, version boundaries, and runbook cautions.
5. Run targeted validation for scoped question IDs, or create an explicit not-ready report.
6. Run repository validation, review the diff, and commit.

## Acceptance Criteria

- Scoped failures are improved, fixed, or explicitly documented as blocked.
- Assigned replacement-grade view/performance gaps are fixed, blocked with evidence,
  or explicitly deferred with owner rationale.
- Targeted validation evidence exists.
- Project files are clean after the focused commit.
