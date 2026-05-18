# Job PWF-J015: SSL Sample Replacement Gap Remediation

## Goal

Remediate or explicitly justify the sampled SSL/TLS appendix replacement gap before
final coverage validation.

## Steps

1. Run the required first checks from `AGENTS.md`.
2. Read `GPTs/reports/full_coverage_audit/replacement_grade_reference_policy_20260518.md`, then re-check
   `Manuals/Altibase_7.1/kor/Altibase SSL TLS User's Guide.md` appendix and source
   item `SRC-SEC-XVER-000010`.
3. Add a compact SSL/TLS sample inventory to `18_security_ssl_tls.md`, or justify why
   exact sample coverage should remain guarded or residual.
4. Update `11_java_jdbc_spring.md`, catalog, matrix, and remediation log only if the
   evidence or routing changes.
5. Run full coverage structural checks, `git diff --check`, and review-stage validate.
6. Review the diff and create a focused commit.

## Acceptance Criteria

- Exact sample-path and sample-code tokens are preserved or explicitly justified.
- `SRC-SEC-XVER-000010` has accurate evidence and disposition.
- Project files are clean after the focused commit.
