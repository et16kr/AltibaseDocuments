# Job PWF-J018: Protected Remediation Version-Sensitive Properties

## Goal

Fix or justify protected blockers for version-sensitive property changes.

## Steps

1. Run the required first checks from `AGENTS.md`.
2. Use `protected_blocker_classification_20260518.md` as the primary scope owner and
   `GPTs/reports/full_coverage_audit/replacement_grade_gap_register_20260518.md` as the cross-document policy scope.
3. Remediate only source-backed property gaps in `05_data_types_properties.md` and
   required support files.
4. Preserve exact property names, defaults, ranges, units, mutability, restart/recreate
   requirements, check SQL, and version boundaries.
5. Run structural checks and targeted validation for the scoped question IDs. If live
   targeted validation cannot run, create an explicit blocker report with the exact reason.
6. Run repository validation, review the diff, and commit.

## Acceptance Criteria

- Scoped property blockers are fixed or have safe-stop guardrail justification.
- Assigned replacement-grade property gaps are fixed, blocked with evidence, or
  explicitly deferred with owner rationale.
- Targeted validation ran, or a blocker report explains why it could not.
- Project files are clean after the focused commit.
