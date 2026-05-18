# Job PWF-J024: Residual Failure Classification And Domain Plan

## Goal

Classify remaining non-protected failures and define bounded domain remediation waves.

## Steps

1. Run the required first checks from `AGENTS.md`.
2. Inspect latest benchmark artifacts, `GPTs/reports/full_coverage_audit/replacement_grade_gap_register_20260518.md`,
   and any targeted validation results.
3. Create `GPTs/reports/full_coverage_audit/residual_failure_classification_20260518.md`.
4. Classify remaining failures by content, retrieval, synthesis, guardrail, or judge
   calibration.
5. Include the second Korean source sample audit from
   `GPTs/reports/full_coverage_audit/post_workflow_followup_plan_20260518.md` in the
   tools/APIs/connectors classification unless the exact iSQL tokens are already
   proven answer-ready.
6. Assign failures to `PWF-J025` through `PWF-J030`.
7. Run repository validation, review the diff, and commit.

## Acceptance Criteria

- Remaining non-protected failures have evidence-backed primary classes and owner jobs.
- Remaining replacement-grade gaps are assigned to the domain owner jobs, not only
  benchmark failures.
- The iSQL replacement-sample gaps are assigned to `PWF-J030` or explicitly proven
  already covered with evidence.
- Domain waves are narrow enough for targeted validation.
- Project files are clean after the focused commit.
