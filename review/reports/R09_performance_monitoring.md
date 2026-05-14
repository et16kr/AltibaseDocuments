# R09 Performance Tuning, Optimizer, Execution Plans, Monitoring, SNMP

Date: 2026-05-14
Reviewer: Codex
Verdict: Review Required

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
  - `Manuals/Altibase_7.1/eng/Monitoring API Developer's Guide.md`
  - `Manuals/Altibase_7.3/eng/Monitoring API Developer's Guide.md`
  - `Manuals/Altibase_trunk/eng/Monitoring API Developer's Guide.md`
  - `Manuals/Altibase_7.1/eng/SNMP Agent Guide.md`
  - `Manuals/Altibase_7.3/eng/SNMP Agent Guide.md`
  - `Manuals/Altibase_trunk/eng/SNMP Agent Guide.md`
  - `Manuals/Altibase_7.1/eng/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_7.3/eng/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_trunk/eng/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_7.3/eng/Stored Procedures Manual.md`
  - `Manuals/Altibase_trunk/eng/Stored Procedures Manual.md`
  - `ReleaseNotes/eng/Altibase_7_3_0_0_1_Release_Notes.md`
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`

## Commands Run

```bash
sed -n '1,240p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,220p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,260p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
nl -ba GPTs/attachments/08_performance_tuning_monitoring.md | sed -n '1,2248p'
nl -ba GPTs/attachments/06_data_dictionary_performance_views.md | sed -n '1,1817p'
sed -n '1,240p' GPTs/reports/sql_generation_test_results.md
find Manuals -path '*Performance Tuning Guide.md' -o -path '*Monitoring API Developer*' -o -path '*SNMP Agent*' | sort
rg -n "JSON|TRCLOG_EXPLAIN_TYPE|TRCLOG_JSON_PLAN_INDENT_DEPTH|Execution Plan|explain plan" ReleaseNotes Manuals/Altibase_trunk/eng/Performance\ Tuning\ Guide.md Manuals/Altibase_trunk/kor/Performance\ Tuning\ Guide.md
rg -n "ABIInitialize|ABIFinalize|ABIGet|Monitoring API|thread|socket|V\$|alti" Manuals/Altibase_7.1/eng/Monitoring\ API\ Developer\'s\ Guide.md Manuals/Altibase_7.3/eng/Monitoring\ API\ Developer\'s\ Guide.md Manuals/Altibase_trunk/eng/Monitoring\ API\ Developer\'s\ Guide.md
rg -n "ALTIBASE-MIB|altiPropertyTable|altiStatus|altiTrap|SNMP_ENABLE|SNMP_PORT_NO|SNMP_TRAP_PORT_NO|snmpwalk|altisnmpd|trap|100001" Manuals/Altibase_7.1/eng/SNMP\ Agent\ Guide.md Manuals/Altibase_7.3/eng/SNMP\ Agent\ Guide.md Manuals/Altibase_trunk/eng/SNMP\ Agent\ Guide.md
rg -n "V\$MEMGC|V\$LFG|V\$BUFFPOOL_STAT|V\$SERVICE_THREAD|victim_search|MULTIPLEXING|V\$SQL_PLAN_CACHE|CREATED_BY_CACHE_MISS|V\$DBMS_STATS|V\$LOCK_TABLE_STATS" Manuals/Altibase_7.1/eng Manuals/Altibase_7.3/eng Manuals/Altibase_trunk/eng GPTs/attachments/08_performance_tuning_monitoring.md GPTs/attachments/06_data_dictionary_performance_views.md
rg -n "10000201|10000103|Session Failure|Continuous" Manuals/Altibase_7.1/eng/SNMP\ Agent\ Guide.md Manuals/Altibase_7.3/eng/SNMP\ Agent\ Guide.md Manuals/Altibase_trunk/eng/SNMP\ Agent\ Guide.md
rg -n "DBMS_SQL_PLAN_CACHE|KEEP_PLAN|UNKEEP_PLAN|PLAN_CACHE_KEEP" GPTs/attachments Manuals/Altibase_7.3/eng/Stored\ Procedures\ Manual.md Manuals/Altibase_trunk/eng/Stored\ Procedures\ Manual.md ReleaseNotes/eng/Altibase_7_3_0_0_1_Release_Notes.md
rg -n "Conversion TODO|TODO|trunk|Manuals/Altibase|file://|/home/|media/|\.gif|\.png|\.jpg|\.jpeg|Altibase_trunk" GPTs/attachments/08_performance_tuning_monitoring.md GPTs/attachments/06_data_dictionary_performance_views.md
rg -n "JSON|TRCLOG_EXPLAIN_TYPE|TRCLOG_JSON_PLAN_INDENT_DEPTH|field|schema|example JSON|property values" GPTs/attachments/08_performance_tuning_monitoring.md
wc -l GPTs/attachments/08_performance_tuning_monitoring.md GPTs/attachments/06_data_dictionary_performance_views.md
git status --short -- GPTs/attachments review/reports/R09_performance_monitoring.md review/reports
```

## Findings

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| High | `GPTs/attachments/08_performance_tuning_monitoring.md` | 2147 | The SNMP trap block states that continuous session failure uses trap code `10000103`. All three sampled SNMP Agent Guides have conflicting source evidence: the `Too Many Continuous Query Failure` section lists code `10000201`, but its example output shows `10000103`. Presenting only `10000103` can make GPT answers produce a wrong alert rule or trap parser. | Do not assert a single continuous-session-failure trap code until the source conflict is resolved. Either correct it to the confirmed code or state the source ambiguity and require target-version validation with `snmptrapd` output before configuring alert rules. |
| Medium | `GPTs/attachments/08_performance_tuning_monitoring.md` | 1632 | The SQL Plan Cache section covers hints, views, and `ALTER SYSTEM COMPACT/RESET SQL_PLAN_CACHE`, but it omits the version-aware `DBMS_SQL_PLAN_CACHE` package. 7.3 release notes and 7.3/8.1 Stored Procedures manuals document `DBMS_SQL_PLAN_CACHE.KEEP_PLAN(sql_text_id)` and `DBMS_SQL_PLAN_CACHE.UNKEEP_PLAN(sql_text_id)` for keeping or releasing specific cached execution plans. | Add a compact 7.3/8.1 plan-cache management block under SQL Plan Cache. Include `DBMS_SQL_PLAN_CACHE.KEEP_PLAN`, `UNKEEP_PLAN`, `SQL_TEXT_ID`, and verification with `V$SQL_PLAN_CACHE_SQLTEXT.PLAN_CACHE_KEEP` and `V$SQL_PLAN_CACHE_PCO.PLAN_CACHE_KEEP`; state that this was not found in the sampled 7.1 source. |
| Medium | `GPTs/attachments/08_performance_tuning_monitoring.md` | 1937 | The Monitoring API initialization example uses `SYS` and `MANAGER` as copy-ready credential values. The Monitoring API manual documents these as defaults, but the customer-facing attachment can lead the GPT to recommend embedding default privileged credentials in monitoring code. | Replace the example values with placeholders such as `<MONITOR_USER>` and `<MONITOR_PASSWORD>`. Keep `SYS`/`MANAGER` only as a source-default caution, and tell the GPT to avoid hard-coding privileged credentials in production examples. |
| Medium | `GPTs/attachments/08_performance_tuning_monitoring.md` | 2082 | The SNMP configuration pattern uses `rocommunity public` and `rwcommunity private` without a caution. These are source-style examples, but as customer-facing GPT knowledge they can produce insecure copy-paste SNMP advice. | Use placeholders such as `<readonly-community>` and `<readwrite-community>`, and add a short caution to restrict SNMP ACLs and avoid default community strings in production. |

## Source Checks

- Claims checked:
  - Query processing sequence, memory-table versus disk-table cost priorities, executor/optimizer differences, and index-selection cautions.
  - `EXPLAIN PLAN` syntax, `ON`/`ONLY`/`OFF` behavior, `TRCLOG_DETAIL_PREDICATE`, predicate detail, `ACCESS = ??` under `ONLY`, and plan-tree reading rules.
  - Access methods, composite-index guidance, data type comparison cautions, join-order and join-method terminology, plan-node names, statistics, hints, SQL Plan Cache, Result Cache, and server bottleneck checks.
  - Monitoring API locality, Unix domain socket constraint, thread-safety warning, result pointer handling, build/link essentials, lifecycle functions, view-mapped functions, and replication API functions.
  - SNMP `ALTIBASE-MIB`, `altiPropertyTable`, `altiStatus`, `altiTrap`, ports, AgentX flow, properties, commands, and trap-code blocks.
  - 8.1 JSON execution-plan wording against release notes and new property names.
- Source coverage:
  - Strong coverage for core optimizer, plan-tree, index, join, statistics, hint, SQL plan cache, result cache, and server bottleneck guidance in all three sampled Performance Tuning Guides.
  - Strong coverage for Monitoring API constraints and function names in all three sampled Monitoring API Developer's Guides.
  - Good SNMP structure coverage, but trap-code rows contain source inconsistencies that should not be flattened into a single unqualified statement.
  - `06_data_dictionary_performance_views.md` supports the performance view checks used by `08`, including `V$SESSION`, `V$STATEMENT`, `V$SESSION_WAIT`, `V$SYSTEM_EVENT`, `V$LOCK_WAIT`, `V$SQL_PLAN_CACHE*`, `V$DBMS_STATS`, `V$MEMGC`, `V$BUFFPOOL_STAT`, and replication views.
- Source gaps:
  - The 8.1 JSON plan source found in release notes confirms JSON-format output and the properties `TRCLOG_EXPLAIN_TYPE` and `TRCLOG_JSON_PLAN_INDENT_DEPTH`, but not JSON field schema, property values, or sample JSON output. The attachment correctly avoids those details.
  - No live Altibase server was available for executing validation SQL; view and column checks were compared to manuals only.
  - SNMP continuous-session-failure trap code requires source-owner or runtime validation because all sampled SNMP manuals repeat the same contradiction.

## Oracle-Overlap Decision

- Correctly compressed:
  - Yes. The scoped attachments do not expand ordinary Oracle-overlapping DML. Performance guidance focuses on Altibase-specific plans, indexes, hints, views, properties, plan cache, Monitoring API, and SNMP.
- Too much generic Oracle material:
  - None found.
- Missing Altibase-specific difference:
  - The main missing performance-specific item is version-aware `DBMS_SQL_PLAN_CACHE` coverage for 7.3/8.1 specific plan-cache management.

## Version Checks

- 7.1:
  - Core optimizer, plan-tree, memory/disk tuning, server bottleneck, Monitoring API, and SNMP guidance is supported by sampled 7.1 manuals.
  - `DBMS_SQL_PLAN_CACHE` was not found in the sampled 7.1 sources and should not be presented as common to all versions.
  - SNMP continuous-session-failure trap code conflict appears in the 7.1 SNMP source.
- 7.3:
  - Core performance guidance is supported by sampled 7.3 manuals.
  - 7.3 release notes and Stored Procedures manual document `DBMS_SQL_PLAN_CACHE`, which is not covered in `08`.
  - SNMP continuous-session-failure trap code conflict appears in the 7.3 SNMP source.
- 8.1:
  - Core performance guidance is supported by sampled Altibase 8.1 verified source manuals.
  - 8.1 JSON-format plan handling is appropriately narrow: existence plus `TRCLOG_EXPLAIN_TYPE` and `TRCLOG_JSON_PLAN_INDENT_DEPTH` only.
  - SNMP continuous-session-failure trap code conflict appears in the 8.1 verified source SNMP manual.

## Retrieval And GPT Answer Quality

- Strengths:
  - `08` has strong response rules that prevent generic optimizer overclaims: it requires plan, data volume, storage type, indexes, statistics age, and bottleneck metrics before recommending indexes, hints, or property changes.
  - Execution-plan terminology is highly searchable and source-aligned, including `PROJECT`, `SCAN`, `JOIN`, `SORT`, `HASH`, `GROUP-AGGREGATION`, `ACCESS`, `COST`, `DISK_PAGE_COUNT`, `TID`, and subquery markers.
  - The memory-table versus disk-table distinction is preserved and should help prevent Oracle-style "always add an index" advice.
  - 8.1 JSON plan claims are intentionally narrow and do not invent schema or sample output.
  - Monitoring API and SNMP sections preserve literal function names, MIB names, property names, command names, and ports.
- Risks:
  - The SNMP trap-code conflict can produce a confidently wrong GPT answer for alert configuration.
  - Plan-cache management questions about keeping or releasing a specific plan may retrieve `08` but miss `DBMS_SQL_PLAN_CACHE` details unless another attachment is also retrieved.
  - Copy-ready default credentials and SNMP community strings could cause insecure examples in generated answers.

## Required Follow-Up

- Resolve or caveat the SNMP continuous-session-failure trap code before upload.
- Add version-aware `DBMS_SQL_PLAN_CACHE` coverage for 7.3 and 8.1, with verification queries.
- Replace Monitoring API and SNMP default credential/community examples with placeholders and production cautions.
