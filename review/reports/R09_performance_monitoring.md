# R09 Performance Tuning, Optimizer, Execution Plans, Monitoring, SNMP

Date: 2026-05-15
Reviewer: Codex
Verdict: Pass

## Scope

- Attachments:
  - `GPTs/attachments/08_performance_tuning_monitoring.md`
  - `GPTs/attachments/06_data_dictionary_performance_views.md`
- Supporting reports:
  - `GPTs/reports/sql_generation_test_results.md`
- Source manuals sampled:
  - `Manuals/Altibase_7.1/eng/Performance Tuning Guide.md`
  - `Manuals/Altibase_7.3/eng/Performance Tuning Guide.md`
  - `Manuals/Altibase_trunk/eng/Performance Tuning Guide.md`
  - `Manuals/Altibase_7.1/eng/Stored Procedures Manual.md`
  - `Manuals/Altibase_7.3/eng/Stored Procedures Manual.md`
  - `Manuals/Altibase_trunk/eng/Stored Procedures Manual.md`
  - `Manuals/Altibase_7.1/eng/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_7.3/eng/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_trunk/eng/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_7.3/eng/Monitoring API Developer's Guide.md`
  - `Manuals/Altibase_7.3/eng/SNMP Agent Guide.md`
  - `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`

## Commands Run

```bash
sed -n '1,240p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,220p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,240p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
nl -ba GPTs/attachments/08_performance_tuning_monitoring.md | sed -n '1,2280p'
nl -ba GPTs/attachments/06_data_dictionary_performance_views.md | sed -n '1,1845p'
rg -n "EXPLAIN PLAN|ACCESS:|DISK_PAGE_COUNT|PARTITION-COORDINATOR|PARALLEL-SCAN-COORDINATOR|RESULT_CACHE|TOP_RESULT_CACHE|TRCLOG_EXPLAIN_TYPE|TRCLOG_JSON_PLAN_INDENT_DEPTH|JSON" Manuals/Altibase_7.1/eng/Performance\ Tuning\ Guide.md Manuals/Altibase_7.3/eng/Performance\ Tuning\ Guide.md Manuals/Altibase_trunk/eng/Performance\ Tuning\ Guide.md ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md
rg -n "Monitoring API|ABIInitialize|ABIFinalize|ABIGetVSession|Unix domain|thread|mutex|altibaseMonitor|ABICheckConnection|ABIGetSqlText" Manuals/Altibase_7.1/eng Manuals/Altibase_7.3/eng Manuals/Altibase_trunk/eng
rg -n "ALTIBASE-MIB|altiPropertyTable|altiStatus|altiTrap|altisnmpd|SNMP_ENABLE|SNMP_PORT_NO|17180|10000201|10000103|session failure" Manuals/Altibase_7.1/eng Manuals/Altibase_7.3/eng Manuals/Altibase_trunk/eng
rg -n "memory table|disk table|index scan|full scan|10%|selectivity" Manuals/Altibase_7.1/eng/Performance\ Tuning\ Guide.md Manuals/Altibase_7.3/eng/Performance\ Tuning\ Guide.md Manuals/Altibase_trunk/eng/Performance\ Tuning\ Guide.md
rg -n "b\.child_pco_count|DBMS_SQL_PLAN_CACHE|TRCLOG_EXPLAIN_TYPE|TRCLOG_JSON_PLAN_INDENT_DEPTH|CREATED_BY_CACHE_MISS|CREATE_BY_CACHE_MISS" GPTs/attachments/08_performance_tuning_monitoring.md GPTs/attachments/06_data_dictionary_performance_views.md Manuals/Altibase_7.1/eng/Stored\ Procedures\ Manual.md Manuals/Altibase_7.3/eng/Stored\ Procedures\ Manual.md Manuals/Altibase_7.1/eng/General\ Reference-2.The\ Data\ Dictionary.md Manuals/Altibase_7.3/eng/General\ Reference-2.The\ Data\ Dictionary.md Manuals/Altibase_trunk/eng/General\ Reference-2.The\ Data\ Dictionary.md ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md
rg -n "trunk|Manuals/|ReleaseNotes/|file://|/home/|C:\\|Altibase_trunk" GPTs/attachments/08_performance_tuning_monitoring.md GPTs/attachments/06_data_dictionary_performance_views.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name README.md | wc -l
```

## Findings

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Resolved High | `GPTs/attachments/08_performance_tuning_monitoring.md` | 1731 | The SQL plan cache join selects `b.child_pco_count` and orders by `b.child_pco_count`, but `CHILD_PCO_COUNT` belongs to `V$SQL_PLAN_CACHE_SQLTEXT`, not `V$SQL_PLAN_CACHE_PCO`. The generated check SQL will fail or teach the GPT an invalid column ownership. | Resolved by H07. The plan-cache alias bug is no longer an open High gate item. |
| Resolved High | `GPTs/attachments/08_performance_tuning_monitoring.md` | 1648 | The attachment says only 7.3 and 8.1 sources document `DBMS_SQL_PLAN_CACHE.KEEP_PLAN` and `UNKEEP_PLAN`, then warns not to present the package as common to 7.1. The sampled 7.1 Stored Procedures Manual also documents `DBMS_SQL_PLAN_CACHE`, `KEEP_PLAN`, and `UNKEEP_PLAN`. This is wrong version guidance for 7.1 customers. | Resolved by H08. The plan-cache package version note is no longer an open High gate item. |
| Resolved Medium | `GPTs/attachments/08_performance_tuning_monitoring.md` | 1743 | `CREATE_REASON` value spelling is source-inconsistent, and the attachment hard-coded only `CREATED_BY_CACHE_MISS`. | Resolved by M15. The plan-cache interpretation now avoids brittle alert rules tied to only `CREATED_BY_*` spelling and tells users to interpret the actual target-server values. |
| Resolved Low | `GPTs/attachments/08_performance_tuning_monitoring.md` | 2110 | The SNMP run-pattern example used `-c private` even though the same section correctly warned not to use default community strings in production. | Resolved by L06. The SNMP example now uses a community placeholder while retaining the ACL/default-community warning. |

## Source Checks

- Claims checked:
  - `ALTER SESSION SET EXPLAIN PLAN = { ON | ONLY | OFF }`, `ACCESS` behavior, plan indentation, subquery markers, `DISK_PAGE_COUNT`, and `TRCLOG_DETAIL_PREDICATE`.
  - Plan node terminology for `SCAN`, `JOIN`, `SORT`, `HASH`, `GROUP-AGGREGATION`, `DISTINCT`, `LIMIT-SORT`, `MATERIALIZATION`, `PARALLEL-SCAN-COORDINATOR`, and `PARTITION-COORDINATOR`.
  - Memory-table versus disk-table optimizer priorities, index-scan guidance, data type conversion effects, join selectivity, statistics procedures, hints, SQL plan cache, and Result Cache restrictions.
  - Monitoring API same-host Unix domain socket constraint, memory/thread-safety note, result pointer pattern, and key `ABI*` function mappings.
  - SNMP `ALTIBASE-MIB`, `altiPropertyTable`, `altiStatus`, `altiTrap`, port flow, properties, and trap-code conflict note.
  - 8.1 JSON-format execution plan wording and the release-note-backed properties `TRCLOG_EXPLAIN_TYPE` and `TRCLOG_JSON_PLAN_INDENT_DEPTH`.
- Source coverage:
  - Execution-plan and optimizer guidance is strongly grounded in the Performance Tuning Guide and avoids broad generic optimizer promises.
  - `06_data_dictionary_performance_views.md` gives useful `V$TABLE` and `V$ALLCOLUMN` availability checks before version-sensitive view use.
  - The 8.1 JSON plan text is appropriately narrow and does not invent JSON schema, field names, property values, or sample JSON output.
- Source gaps:
  - No live Altibase server was available, so SQL snippets were checked against manuals, not executed.
  - The `CREATE_REASON` spelling conflict is now handled conservatively in attachment wording by M15.

## Oracle-Overlap Decision

- Correctly compressed:
  - Ordinary SQL behavior is not expanded. The reviewed files focus on Altibase-specific execution plans, storage-dependent cost behavior, performance views, Monitoring API, and SNMP.
- Too much generic Oracle material:
  - None found in this stage.
- Missing Altibase-specific difference:
  - The plan-cache package 7.1 support gap is closed by H08.

## Version Checks

- 7.1:
  - Performance tuning fundamentals, plan nodes, SQL plan cache views, Monitoring API, SNMP concepts, and `DBMS_SQL_PLAN_CACHE` support are covered.
- 7.3:
  - Source checks align well for optimizer, plan cache, Result Cache, Monitoring API, and SNMP.
- 8.1:
  - JSON-format plan claims are handled narrowly and safely.
  - `V$MEM_STABLE`, `V$TEMPORARY_LOBS`, and `TRCLOG_*` properties are treated as version-sensitive with availability checks.

## Retrieval And GPT Answer Quality

- Strengths:
  - `08_performance_tuning_monitoring.md` is highly searchable and should support good answers for slow SQL, plan reading, index selection, joins, statistics, plan cache, Result Cache, Monitoring API, and SNMP.
  - The response rules require evidence before recommending indexes, hints, or property changes, which reduces generic optimizer overclaims.
  - `06_data_dictionary_performance_views.md` complements the performance attachment with concrete runtime and metadata SQL.
- Risks:
  - Closed by H07: the `child_pco_count` alias bug is no longer an open risk.
  - Closed by H08: the 7.1 `DBMS_SQL_PLAN_CACHE` version warning is no longer an open risk.
  - Closed by M15: `CREATE_REASON` guidance is target-server oriented to avoid brittle generated monitoring rules.

## V02 Closure

- Closed by H07: the `V$SQL_PLAN_CACHE_SQLTEXT` / `V$SQL_PLAN_CACHE_PCO` alias issue in `08_performance_tuning_monitoring.md`.
- Closed by H08: the `DBMS_SQL_PLAN_CACHE` version note now includes documented 7.1 support.
- Closed by M15: `CREATE_REASON` spelling interpretation is target-server oriented.
- Closed by L06: SNMP examples use a community placeholder.
- No open R09 finding remains after V02 re-review of the changed sections.
