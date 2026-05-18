# Job PWF-J027: Domain Remediation Properties

## Goal

Remediate classified non-protected property failures.

## Steps

1. Run the required first checks from `AGENTS.md`.
2. Use `residual_failure_classification_20260518.md` as the primary scope owner and
   `GPTs/reports/full_coverage_audit/replacement_grade_gap_register_20260518.md` as the cross-document policy scope.
3. Preserve exact property names, defaults, ranges, units, mutability, change method,
   restart/recreate rules, and check SQL.
4. Run targeted validation for scoped question IDs, or create an explicit not-ready report.
5. Run repository validation, review the diff, and commit.

## Acceptance Criteria

- Scoped property failures are improved, fixed, or explicitly documented as blocked.
- Assigned replacement-grade property gaps are fixed, blocked with evidence, or
  explicitly deferred with owner rationale.
- Targeted validation evidence exists.
- Project files are clean after the focused commit.
