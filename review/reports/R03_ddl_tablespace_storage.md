# R03 DDL Generation: Tablespaces, Storage, Users, Privileges, Replication SQL

Date: 2026-05-14
Reviewer: Codex
Verdict: Review Required

## Scope

- Stage ID: R03
- Group: G2_CoreSQL
- Attachments reviewed:
  - `GPTs/attachments/03_sql_ddl_generation.md`
  - `GPTs/attachments/02_administration_operations.md`
  - `GPTs/attachments/09_replication_ha_cdc.md`
- Supporting documents read:
  - `review/Altibase_GPT_Detailed_Review_Design.md`
  - `GPTs/Altibase_GPT_Document_Selection.md`
  - `GPTs/Altibase_GPT_Attachment_Build_Workplan.md`
  - `GPTs/attachments/README.md`
  - `GPTs/reports/sql_generation_test_results.md`
- Source manuals sampled:
  - `Manuals/Altibase_7.1/eng/SQL Reference.md`
  - `Manuals/Altibase_7.3/eng/SQL Reference.md`
  - `Manuals/Altibase_trunk/eng/SQL Reference.md`
  - `Manuals/Altibase_trunk/eng/General Reference-2.Data Dictionary.md`
  - `Manuals/Altibase_trunk/eng/Administrator's Manual.md`
  - `Manuals/Altibase_trunk/eng/Replication Manual.md`
  - `Manuals/Altibase_trunk/eng/Log Analyzer User's Manual.md`
  - `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`

## Commands Run

```bash
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' | wc -l
rg -n "trunk|C:/|file://" GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/02_administration_operations.md GPTs/attachments/09_replication_ha_cdc.md
rg -n "CREATE \[LAZY \| EAGER\] REPLICATION|START \[RETRY\]|QUICKSTART \[RETRY\]|FOR ANALYSIS|sub-millisecond|guarantees" GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/09_replication_ha_cdc.md
rg -n "IF NOT EXISTS|IF EXISTS|USING SSL|REPLICATION_SSL_PORT_NO|VOLATILE_MAX_DB_SIZE|MEM_MAX_DB_SIZE" GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/02_administration_operations.md GPTs/attachments/09_replication_ha_cdc.md
rg -n "cannot guarantee data consistency|same row|conflict|REPLICATION_EAGER_PARALLEL_FACTOR|EAGER" "Manuals/Altibase_trunk/eng/Replication Manual.md"
rg -n "EAGER mode cannot be specified|XLog Sender is created|LAZY mode|FOR ANALYSIS|QUICKSTART|START \[AT SN" "Manuals/Altibase_trunk/eng/Log Analyzer User's Manual.md"
rg -n "RETRY option is not supported in EAGER|START RETRY|QUICKSTART RETRY|ALTER REPLICATION.*START" "Manuals/Altibase_trunk/eng/SQL Reference.md"
rg -n "USING SSL|REPLICATION_SSL_PORT_NO|SSL/TLS" ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md
```

## Findings

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| High | `GPTs/attachments/09_replication_ha_cdc.md` | 20 | The opening Active-Active description says replication "guarantees sub-millisecond latency and built-in conflict resolution." This overstates Altibase behavior. The Replication Manual says replication cannot guarantee data consistency against conflicts, conflict resolution is not perfect, and EAGER mode has data-consistency constraints during network failure and other cases. | Rewrite the overview to say Altibase supports XLog-based LAZY/EAGER replication and Active-Active topologies, but conflict ownership, conflict policy, replication gap monitoring, and failover/failback design are required. Remove the latency guarantee and avoid saying conflict resolution is guaranteed. |
| High | `GPTs/attachments/03_sql_ddl_generation.md` | 577 | The compact grammar combines `CREATE [LAZY \| EAGER] REPLICATION` with `[FOR ANALYSIS ...]`, which can lead the GPT to generate invalid `CREATE EAGER REPLICATION ... FOR ANALYSIS` SQL. The Log Analyzer manual states the XLog Sender is automatically created in LAZY mode and EAGER cannot be specified for XLog Sender creation. | Split ordinary replication syntax from Log Analyzer syntax. Use `CREATE [LAZY \| EAGER] REPLICATION ... WITH ... FROM ... TO ...` only for table-to-table replication, and a separate `CREATE REPLICATION replication_name FOR ANALYSIS [PROPAGATION] ...` pattern for Log Analyzer CDC. Add a local note that `EAGER` is invalid with `FOR ANALYSIS`. |
| High | `GPTs/attachments/09_replication_ha_cdc.md` | 303 | The same compact grammar permits the invalid combination of `EAGER` and `FOR ANALYSIS`, even though nearby notes only cover SSL/InfiniBand exclusions. This is likely to affect replication SQL answers because this attachment is the main HA/CDC source. | Mirror the split syntax in `03_sql_ddl_generation.md` and place the LAZY-only Log Analyzer rule next to the grammar, not only in later CDC prose. |
| Medium | `GPTs/attachments/03_sql_ddl_generation.md` | 602 | `ALTER REPLICATION replication_name START [RETRY]` and `QUICKSTART [RETRY]` are listed without the EAGER-mode restriction. The SQL Reference states that `RETRY` is not supported in EAGER mode. | Add a generation rule: do not include `RETRY` when the replication object is EAGER. If the mode is unknown, tell the user to verify the replication mode first, for example from replication catalog/runtime views, before generating `START RETRY` or `QUICKSTART RETRY`. |
| Medium | `GPTs/attachments/09_replication_ha_cdc.md` | 477 | The operations syntax also lists `START [RETRY]` and `QUICKSTART [RETRY]` without the EAGER restriction, so troubleshooting or runbook answers could recommend unsupported SQL. | Add the same EAGER-mode caveat near the operations syntax and in the start/restart troubleshooting guidance. |

## Source Checks

- Tablespace DDL was checked against 7.1, 7.3, and trunk SQL Reference sections for disk, memory, volatile, and temporary tablespaces. The attachment examples correctly separate 7.1/7.3 syntax from 8.1 verified `IF NOT EXISTS` usage and include verification queries.
- Storage guidance was checked against data dictionary views including `V$TABLESPACES`, `V$DATAFILES`, `V$MEM_TABLESPACES`, `V$MEM_TABLESPACE_CHECKPOINT_PATHS`, and `V$VOL_TABLESPACES`.
- User and privilege DDL was checked against `CREATE USER`, `ALTER USER`, `DROP USER`, `GRANT`, and related dictionary views. The attachments preserve Altibase-specific items such as `ACCESS`, default/temporary tablespace selection, role/system/object privilege distinctions, and `WITH GRANT OPTION` limitations.
- Replication SQL was checked against ordinary replication, SSL replication, Log Analyzer CDC, and operation syntax. 8.1 SSL guidance for `USING SSL` and `REPLICATION_SSL_PORT_NO` is supported by the 8.1 release notes.
- The supporting SQL generation test report records passing prompt checks, but the issues above are edge cases not covered by those results.

## Oracle-Overlap Decision

- Generic Oracle-overlapping DML is appropriately compressed in this stage.
- The reviewed content emphasizes Altibase-specific DDL, storage, dictionary verification, properties, replication, and operational checks.
- The main missing Altibase-specific constraints are replication-mode caveats around Log Analyzer and `RETRY`.

## Version Checks

- 7.1: Attachment examples avoid 8.1-only `IF NOT EXISTS`, `IF EXISTS`, native `JSON`, Temporary LOB, and SSL replication unless version-specific confirmation is supplied.
- 7.3: Attachment examples follow the same conservative compatibility rule and include lower-version replication compatibility guidance.
- 8.1: Attachment examples correctly introduce verified `IF NOT EXISTS`/`IF EXISTS` patterns and SSL replication with `USING SSL` plus `REPLICATION_SSL_PORT_NO`.

## Acceptance Assessment

This stage should not pass upload review yet because High findings remain. Tablespace, storage, user, and privilege examples are generally version-aware, executable after placeholder replacement, and include useful verification SQL. Replication examples are mostly strong, but the grammar and overview issues can cause unsafe HA guidance or invalid Log Analyzer/EAGER SQL.

## Residual Risks

- No live Altibase instance was available, so executable status was assessed by source syntax and local consistency checks rather than running the SQL.
- The source set contains a wording conflict around the upper bound for volatile tablespace `UNLIMITED`: SQL Reference wording mentions `MEM_MAX_DB_SIZE`, while Administrator/Error references support `VOLATILE_MAX_DB_SIZE`. The attachments currently follow the Administrator/Error behavior. This should remain on the source-audit list if exact wording is later refined.

## Required Follow-Up

1. Fix the High replication wording and grammar issues before upload.
2. Add `RETRY` versus EAGER-mode caveats in both SQL generation and HA operations attachments.
3. Re-run targeted SQL generation prompts for Log Analyzer CDC, EAGER replication start/retry, and Active-Active overview wording after edits.
