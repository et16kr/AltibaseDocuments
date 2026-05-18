# Job PWF-J028: Domain Remediation Replication Security Network

## Goal

Remediate classified replication/CDC/security/network failures.

## Steps

1. Run the required first checks from `AGENTS.md`.
2. Use `residual_failure_classification_20260518.md` as the primary scope owner and
   `GPTs/reports/full_coverage_audit/replacement_grade_gap_register_20260518.md` as the cross-document policy scope.
3. Preserve exact replication modes, states, DDL, properties, views, ports, TLS
   separation, missing-input triggers, and stop conditions.
4. Run targeted validation for scoped question IDs, or create an explicit not-ready report.
5. Run repository validation, review the diff, and commit.

## Acceptance Criteria

- Scoped replication/security/network failures are improved, fixed, or blocked with evidence.
- Assigned replacement-grade replication/security/network gaps are fixed, blocked with
  evidence, or explicitly deferred with owner rationale.
- Targeted validation evidence exists.
- Project files are clean after the focused commit.
