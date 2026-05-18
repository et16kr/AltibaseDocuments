# Job PWF-J030: Domain Remediation Tools APIs Connectors

## Goal

Remediate classified tools/APIs/connectors/migration failures.

## Steps

1. Run the required first checks from `AGENTS.md`.
2. Use `residual_failure_classification_20260518.md` as the primary scope owner and
   `GPTs/reports/full_coverage_audit/replacement_grade_gap_register_20260518.md` as the cross-document policy scope.
3. Include the iSQL replacement-sample gaps from
   `GPTs/reports/full_coverage_audit/post_workflow_followup_plan_20260518.md` unless
   PWF-J024 proved them already answer-ready.
4. Preserve exact commands, options, file names, API/class/function names, connector
   properties, version boundaries, and live-output guardrails.
5. For iSQL, verify or remediate exact owner-route coverage for `ALTIBASE_SSL_PORT_NO`,
   `ISQL_BUFFER_SIZE`, `ALTIBASE_DATE_FORMAT`, `ALTIBASE_TIME_ZONE`,
   `ALTIBASE_IPC_FILEPATH`, `IPCDA_FILEPATH`, `-UNIXDOMAIN-FILEPATH`,
   `-IPC-FILEPATH`, `-IPCDA-FILEPATH`, `SET ECHO`, `SET SQLPROMPT`, `SET SQLP`,
   `_CONNECT_IDENTIFIER`, `_DATE`, `_PRIVILEGE`, `_USER`, `HELP INDEX`, and
   `HELP EXIT`.
6. Run targeted validation for scoped question IDs, or create an explicit not-ready report.
7. Run repository validation, review the diff, and commit.

## Acceptance Criteria

- Scoped tools/API/connectors failures are improved, fixed, or blocked with evidence.
- Assigned replacement-grade tools/API/connectors gaps are fixed, blocked with
  evidence, or explicitly deferred with owner rationale.
- The iSQL environment/session-control sample gap is remediated in
  `13_isql_iloader_basic_tools.md` or explicitly proven already answer-ready.
- Targeted validation evidence exists.
- Project files are clean after the focused commit.
