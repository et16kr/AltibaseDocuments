# Job PWF-J019: Protected Remediation Security TLS

## Goal

Fix or justify `security_tls` protected blockers.

## Steps

1. Run the required first checks from `AGENTS.md`.
2. Use `protected_blocker_classification_20260518.md` as the primary scope owner and
   `GPTs/reports/full_coverage_audit/replacement_grade_gap_register_20260518.md` as the cross-document policy scope.
3. Remediate source-backed TLS gaps in `18_security_ssl_tls.md` and related routes.
4. Preserve exact SSL/TLS properties, certificate terms, port separation, version
   boundaries, and missing-input prompts.
5. Run structural checks and targeted validation for the scoped question IDs. If live
   targeted validation cannot run, create an explicit blocker report.
6. Run repository validation, review the diff, and commit.

## Acceptance Criteria

- Scoped security/TLS blockers are fixed or safely justified.
- Assigned replacement-grade security/TLS gaps are fixed, blocked with evidence, or
  explicitly deferred with owner rationale.
- Targeted validation ran, or a blocker report explains why it could not.
- Project files are clean after the focused commit.
