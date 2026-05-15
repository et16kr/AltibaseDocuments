# Remediation Failure Log

This file records why remediation tasks enter `Fail` or why a finish gate fails.

## 2026-05-15T14:59:24+09:00 - H02

- Source: finish Fail
- State at failure: Progress
- Reason: Codex CLI review gate blocked by network-disabled sandbox
- Plan: `review/remediation_plan.md:57`
- Severity: High
- Source reports: R03, R10
- Target files: `GPTs/attachments/09_replication_ha_cdc.md`
- Validation: `rg -n "REPLICATION_DDL_ENABLE|REPLICATION_DDL_ENABLE_LEVEL|REPLICATION_DDL_SYNC|REPLICATION_SQL_APPLY_ENABLE|ALTER SESSION SET REPLICATION = DEFAULT|flush" GPTs/attachments/09_replication_ha_cdc.md`
- Resolution: H02 validation and local review passed; the task was marked `Done` after changing worker prompts to avoid nested Codex CLI review. The run-all parent process now performs the separate automatic Codex post-review after each worker exits.

## 2026-05-15T16:36:43+09:00 - H14

- Source: run-all post-review
- State at failure: Done
- Reason: run-all post-review returned RETRY; task marked Fail. Review output: REMEDIATION_REVIEW_RESULT: RETRY The H14 structure and validation coverage are present, but one new customer-facing claim is version-wrong: `GPTs/attachments/11_java_jdbc_spring.md:630` says ordinary `BLOB`/`CLOB` can be up to 2 GB generally. Local source evidence shows 7.1 says `4GB-1byte` (`Manuals/Altibase_7.1/eng/JDBC User's Manual.md:2406`), while 7.3/trunk say `2Gbytes` (`...7.3...:2410`, `...trunk...:2521`). Version-scope that size note or remove it. OpenAI Codex v0.130.0 -------- workdir: /home/et16/AltibaseDocuments model: gpt-5.5 provider: openai approval: never sandbox: danger-full-access reasoning effort: xhigh reasoning summaries: none session id: 019e2a8f-715c-7691-90ac-94268b7dc3b7 -------- user You are Codex acting as an independent reviewer for one remediation task. Workspace: /home/et16/AltibaseDocuments Plan file: review/remediation_plan.md Do not edit files. Do not change task state. Review only. Task: ID: H14 State: Done Severity: High Section: P1 High Severity Fixes Source reports: R14 Target files: `GPTs/attachments/11_java_jdbc_spring.md` Required change: Expand JDBC matrix material into searchable blocks by important Java/JDBC type mapping and method fam...
- Plan: `review/remediation_plan.md:69`
- Severity: High
- Source reports: R14
- Target files: `GPTs/attachments/11_java_jdbc_spring.md`
- Validation: `rg -n "ResultSet|CallableStatement|PreparedStatement|LOB|type mapping|SQLSTATE|JDBC 4\.2" GPTs/attachments/11_java_jdbc_spring.md`
- Resolution: H14 validation and local review passed after aligning ordinary LOB size and `createBlob()`/`createClob()` support with the Korean JDBC manuals; the task was marked `Done`.

## 2026-05-15T16:54:27+09:00 - H15

- Source: run-all
- State at failure: ToDo
- Reason: Codex command failed during run-all with exit code 3
- Plan: `review/remediation_plan.md:70`
- Severity: High
- Source reports: R14
- Target files: `GPTs/attachments/11_java_jdbc_spring.md`
- Validation: `rg -n "SQLSTATE|SQL state|080|220|HY|class|subclass" GPTs/attachments/11_java_jdbc_spring.md`
