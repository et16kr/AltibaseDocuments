# Job PWF-J016: Coverage Closure Validation

## Goal

Prove the source-to-attachment audit closure gate is clean before benchmark remediation.

## Steps

1. Run the required first checks from `AGENTS.md`.
2. Run:
   - `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers`
   - `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py catalog-qa`
   - `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py matrix-qa`
   - `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py guardrail-audit`
3. Confirm active `Missing` rows are `0` and active `Retrieval-weak` rows are `0`.
4. Update `final_full_coverage_audit.md` only if the evidence supports a changed
   readiness decision.
5. Do not claim replacement-grade readiness here; `PWF-J016A` applies that broader
   policy after structural closure.
6. Run `git diff --check`, review-stage validate, and the review report severity scan.
7. Review the diff and create a focused commit.

## Acceptance Criteria

- Catalog and matrix row counts match.
- Active `Missing` and `Retrieval-weak` counts are `0`.
- The final audit report matches current evidence.
- The report distinguishes structural source closure from replacement-grade readiness.
- Project files are clean after the focused commit.
