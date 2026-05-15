# R15 Monitoring Views, Monitoring API, and SNMP

Date: 2026-05-16
Reviewer: Codex
Verdict: Pass

## Scope

- Attachments:
  - `GPTs/attachments/08_performance_tuning_monitoring.md`
  - `GPTs/attachments/06_data_dictionary_performance_views.md`
- Supporting reports:
  - `GPTs/reports/source_inventory.md`
- Source manuals sampled:
  - `Manuals/Altibase_7.1/kor/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_7.1/kor/Monitoring API Developer's Guide.md`
  - `Manuals/Altibase_7.3/kor/Monitoring API Developer's Guide.md`
  - `Manuals/Altibase_trunk/kor/Monitoring API Developer's Guide.md`
  - `Manuals/Altibase_7.1/kor/SNMP Agent Guide.md`
  - `Manuals/Altibase_7.3/kor/SNMP Agent Guide.md`
  - `Manuals/Altibase_trunk/kor/SNMP Agent Guide.md`
  - `Manuals/Altibase_7.1/kor/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_7.3/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`

## Commands Run

```bash
bash review/scripts/run_review_remediation_cycle.sh status
rg -n $'\t(Reviewing|Remediating|ReReviewing|Fail)$' review/review_remediation_cycle_status.tsv
git status --short
sed -n '1,240p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,220p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,260p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
nl -ba review/reports/R15_monitoring_snmp_api.md
nl -ba GPTs/attachments/08_performance_tuning_monitoring.md
nl -ba GPTs/attachments/06_data_dictionary_performance_views.md
sed -n '1,220p' GPTs/reports/source_inventory.md
rg -n "Find Active Statements|Active Statements|current SQL|V\$STATEMENT|execute_flag|current_stmt_id|V\$SERVICE_THREAD|SOCKET|ABIGetSqlText|ABIGetDBInfo|ABIGetReadCount|ABIGetSessionCount|ABIGetMaxClientCount|ABIGetLockWaitSessionCount|10000002|10000004|Continuous session failure|altiTrapLevel|SNMP|ALTIBASE-MIB|altisnmpd|AgentX|altiProperty|altiStatus" GPTs/attachments/08_performance_tuning_monitoring.md GPTs/attachments/06_data_dictionary_performance_views.md
rg -n "Unix|유닉스|domain|도메인|socket|소켓|thread|스레드|mutex|뮤텍스|ABIInitialize|ABIFinalize|ABISetProperty|ABIGetSqlText|ABIGetSessionCount|ABIGetMaxClientCount|ABIGetLockWaitSessionCount|ABIGetDBInfo|ABIGetReadCount|ABIGetVSession|ABIGetVSystemEvent|ABIGetEventName|ABIGetRepGap|ABIGetRepSentLogCount|altibaseMonitor|libaltibaseMonitor|odbccli|return|반환|성공|개수" "Manuals/Altibase_7.1/kor/Monitoring API Developer's Guide.md" "Manuals/Altibase_7.3/kor/Monitoring API Developer's Guide.md" "Manuals/Altibase_trunk/kor/Monitoring API Developer's Guide.md"
rg -n "ALTIBASE-MIB|altiTrap|altiProperty|altiStatus|17180|SNMP_ENABLE|SNMP_PORT_NO|SNMP_TRAP_PORT_NO|SNMP_ALARM|altisnmpd|snmpd|snmptrapd|trap2sink|master agentx|10000001|10000002|10000003|10000004|10000101|10000102|10000103|10000201|AgentX|UDP|TCP|altibase_trap|altibase " "Manuals/Altibase_7.1/kor/SNMP Agent Guide.md" "Manuals/Altibase_7.3/kor/SNMP Agent Guide.md" "Manuals/Altibase_trunk/kor/SNMP Agent Guide.md"
rg -n "V\$SESSION|V\$STATEMENT|V\$SQLTEXT|V\$SESSION_WAIT|V\$SYSTEM_EVENT|V\$SESSION_EVENT|V\$LOCK_WAIT|V\$LOCK_STATEMENT|V\$MEMGC|V\$SERVICE_THREAD|V\$BUFFPOOL_STAT|V\$REPGAP|V\$REPSENDER_SENT_LOG_COUNT|V\$TABLE|V\$ALLCOLUMN|V\$PROPERTY|V\$VERSION|V\$MEM_STABLE|V\$TEMPORARY_LOBS|V\$LOCK_TABLE_STATS|EXECUTE_FLAG|SESSION_WAIT|SYSTEM_EVENT|LOCK_WAIT|STATEMENT|REPGAP|MEMGC|BUFFPOOL_STAT|SOCKET\(|SOCKET \(" "Manuals/Altibase_7.1/kor/General Reference-2.The Data Dictionary.md" "Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md" "Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md"
nl -ba GPTs/attachments/06_data_dictionary_performance_views.md | sed -n '1000,1065p'
nl -ba GPTs/attachments/08_performance_tuning_monitoring.md | sed -n '1860,1950p'
nl -ba GPTs/attachments/08_performance_tuning_monitoring.md | sed -n '1970,2090p'
nl -ba GPTs/attachments/08_performance_tuning_monitoring.md | sed -n '2085,2225p'
nl -ba "Manuals/Altibase_7.3/kor/Monitoring API Developer's Guide.md" | sed -n '300,375p'
nl -ba "Manuals/Altibase_7.3/kor/Monitoring API Developer's Guide.md" | sed -n '640,670p'
nl -ba "Manuals/Altibase_7.3/kor/Monitoring API Developer's Guide.md" | sed -n '1270,1565p'
nl -ba "Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md" | sed -n '10200,10270p'
nl -ba "Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md" | sed -n '10870,11045p'
nl -ba "Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md" | sed -n '11395,11455p'
nl -ba "Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md" | sed -n '6940,7055p'
nl -ba "Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md" | sed -n '9580,9820p'
rg -n "V\$LFG|LF_PREPARE_WAIT_COUNT|PREPARE_LOG_FILE_COUNT" "Manuals/Altibase_7.1/kor/General Reference-2.The Data Dictionary.md" "Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md" "Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md" "Manuals/Altibase_7.1/kor/General Reference-1.Data Types & Altibase Properties.md" "Manuals/Altibase_7.3/kor/General_Reference-1.Data Types & Altibase Properties.md" "Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md"
rg -n -F -e 'V$LOCK_TABLE_STATS' -e 'V$MEM_STABLE' -e 'V$TEMPORARY_LOBS' -e 'TRCLOG_EXPLAIN_TYPE' -e 'TRCLOG_JSON_PLAN_INDENT_DEPTH' ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md "Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md"
rg -n "trunk|Altibase_trunk|file://|C:|/home/|\.png|\.jpg|\.jpeg|\.gif|!\[" GPTs/attachments/08_performance_tuning_monitoring.md GPTs/attachments/06_data_dictionary_performance_views.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' | sort | wc -l
git diff --check
bash review/scripts/run_review_stage.sh validate
rg -n "^Verdict:|^\| (Blocker|High|Medium|Low) \|" review/reports/R15_monitoring_snmp_api.md
git status --short
```

## Findings

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Note | `GPTs/attachments/08_performance_tuning_monitoring.md` | 1991 | Korean Monitoring API source text says `altibaseMonitor.h` and Monitoring API libraries are under `$ALTIBASE_HDB_HOME`, while the same Korean source compile examples use `$ALTIBASE_HOME`. The attachment follows the compile-example form. | No remediation required for upload. If this becomes a developer build-support hot path, mention the source inconsistency or tell users to verify the installed environment variable layout. |
| Note | `GPTs/attachments/08_performance_tuning_monitoring.md` | 2042 | Korean Monitoring API text says `ABIGetSqlText` with `aStmtID = 0` returns active statement information, while the documented return code is success/failure rather than a row count and the sample prints a single `ABISqlText`. The attachment avoids row-count handling for this API and does not overstate array semantics. | No remediation required. Keep the current success-code guidance and avoid adding row-count iteration for `ABIGetSqlText` unless an executable sample or later source confirms it. |

No actionable `Blocker`, `High`, `Medium`, or `Low` issues were found in this re-review.

## Source Checks

- Claims checked:
  - Active-statement SQL now filters `V$STATEMENT.EXECUTE_FLAG = 1`, matching the Korean General Reference definition that `1` means currently executing.
  - `V$SESSION`, `V$STATEMENT`, `V$SQLTEXT`, `V$SESSION_WAIT`, `V$SYSTEM_EVENT`, `V$LOCK_WAIT`, `V$LOCK_STATEMENT`, `V$MEMGC`, `V$SERVICE_THREAD`, `V$BUFFPOOL_STAT`, `V$LFG`, `V$TABLE`, `V$ALLCOLUMN`, `V$PROPERTY`, `V$VERSION`, `V$MEM_STABLE`, `V$TEMPORARY_LOBS`, and `V$LOCK_TABLE_STATS` object names and sampled columns.
  - Monitoring API locality, Unix Domain Socket requirement, thread-safety warning, mutex guidance, no manual result memory allocation/freeing, header/library references, function names, and mixed return styles.
  - SNMP `ALTIBASE-MIB` hierarchy, `altiTrap`, `altiPropertyTable`, `altiStatus`, `altisnmpd`, `snmpd`, `snmptrapd`, AgentX, Altibase SNMP properties, MIB objects, and trap-code notes.
- Source coverage:
  - 7.1, 7.3, and 8.1 Korean General Reference 2 manuals consistently document the sampled core monitoring views.
  - 7.1, 7.3, and 8.1 Korean Monitoring API guides consistently document local Unix Domain Socket access and non-thread-safe shared internal memory.
  - 7.1, 7.3, and 8.1 Korean SNMP Agent guides consistently document `ALTIBASE-MIB`, `altisnmpd`, `snmpd`, `snmptrapd`, AgentX communication, and sampled trap objects.
  - Korean 8.1 release notes confirm `V$LOCK_TABLE_STATS`, `V$MEM_STABLE`, `V$TEMPORARY_LOBS`, `TRCLOG_EXPLAIN_TYPE`, and `TRCLOG_JSON_PLAN_INDENT_DEPTH`.
- Korean/English source conflicts:
  - English manuals were not needed for this stage; Korean sources were sufficient.
  - Korean Monitoring API source text has the `$ALTIBASE_HDB_HOME` versus `$ALTIBASE_HOME` path inconsistency noted above.
  - Korean SNMP guides conflict internally on levels for `10000002` and `10000004`: section labels show level `3`, while sample `snmptrapd` output shows `altiTrapLevel = 1`. The attachment now warns users to validate target-version trap output before hard-coding alert severity.
  - Korean SNMP guides conflict internally on the continuous session failure trap: section label `10000201`, example output `10000103`. The attachment now records the conflict and avoids hard-coding one value.
- Source gaps:
  - No live Altibase instance was available to execute sample SQL or Monitoring API/SNMP calls. Query and API review was source-based.

## Oracle-Overlap Decision

- Correctly compressed:
  - Generic SQL syntax is not expanded in the monitored sections. The scoped content stays focused on Altibase views, Monitoring API, SNMP, execution-plan support, and operational diagnostics.
- Too much generic Oracle material:
  - None found in this stage.
- Missing Altibase-specific difference:
  - None found. The active-statement, service-thread, Monitoring API, and SNMP guidance preserve Altibase-specific object names and caveats.

## Version Checks

- 7.1:
  - Korean General Reference 2 documents the sampled monitoring views and `V$LOCK_TABLE_STATS`.
  - Korean Monitoring API and SNMP guides document the sampled API functions, local API access constraints, MIB hierarchy, and trap objects.
- 7.3:
  - Korean General Reference 2 documents the sampled monitoring views and `V$LOCK_TABLE_STATS`.
  - Korean Monitoring API and SNMP guides document the sampled API functions, local API access constraints, MIB hierarchy, and trap objects.
- 8.1:
  - Korean trunk General Reference 2 documents `V$MEM_STABLE` and `V$TEMPORARY_LOBS`; Korean 8.1 release notes list `V$LOCK_TABLE_STATS`, `V$MEM_STABLE`, and `V$TEMPORARY_LOBS`.
  - Korean 8.1 release notes confirm JSON-format plan support and the property names `TRCLOG_EXPLAIN_TYPE` and `TRCLOG_JSON_PLAN_INDENT_DEPTH`. The attachment correctly avoids inventing JSON-plan schema details.

## Retrieval And GPT Answer Quality

- Strengths:
  - The scoped files preserve literal view names, property names, API names, MIB object names, commands, trap codes, and version labels in searchable Markdown.
  - `06_data_dictionary_performance_views.md` gives portable verification checks through `V$TABLE` and `V$ALLCOLUMN`, and the active-statement query now uses `EXECUTE_FLAG = 1`.
  - `08_performance_tuning_monitoring.md` separates row-set Monitoring API functions, success-code result-pointer functions, and scalar count functions.
  - SNMP trap-code conflicts are framed as validation cautions rather than false certainty.
- Risks:
  - Live behavior was not tested against a running Altibase instance, so executable SQL/API validation remains residual risk.
  - SNMP trap level/code conflicts in the Korean guide remain source residuals; the attachment mitigates them by avoiding hard-coded alert severity for conflicted cases.

## Required Follow-Up

- None for R15. The stage is ready to be committed by the review/remediation cycle after normal validation and worktree review.
