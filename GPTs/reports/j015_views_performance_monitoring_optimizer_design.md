# J015 Views, Monitoring, And Optimizer Design Note

- Job: `J015`
- Scope: `GPTs/attachments/06_data_dictionary_performance_views.md` and `GPTs/attachments/08_performance_tuning_monitoring.md`
- Evidence: `GPTs/reports/answerability_failure_remediation_inventory_20260517.md`, `GPTs/reports/exact_token_gap_inventory_20260517.md`, and `evals/altibase_answerability/questions/views_performance_monitoring.jsonl`

## Boundary

This job is a retrieval and answer-synthesis remediation pass for dictionary views,
performance views, Monitoring API, SNMP, optimizer, execution-plan, wait, lock,
session, and check-SQL content. It does not rename attachments, change the 20-file
upload boundary, or edit original manuals.

## Source Basis

- Korean Altibase 7.3 General Reference 2 for `SYSTEM_.SYS_TABLES_`,
  `SYSTEM_.SYS_INDICES_`, `SYSTEM_.SYS_INDEX_COLUMNS_`,
  `SYSTEM_.SYS_TABLE_PARTITIONS_`, `V$SESSION_WAIT`, `V$LOCK_WAIT`,
  `V$LOCK_STATEMENT`, `V$LFG`, and `V$LOG` column and value definitions.
- Korean Altibase 7.3 and Altibase 8.1 verified source Performance Tuning Guides for
  optimizer components, memory/disk access costs, `EXPLAIN PLAN`,
  `TRCLOG_DETAIL_PREDICATE`, hint syntax, hint conflict handling, statistics, plan
  cache, and server bottleneck checks.
- Korean Altibase 7.1 and 7.3 Monitoring API Developer's Guides for local `Unix Domain
  Socket` use, `Altibase 5.5.1` support wording, build artifacts, result-memory rules,
  mutex cautions, and function-to-view mappings.
- Korean Altibase 7.3 SNMP Agent Guide for `ALTIBASE-MIB`, `altibase(17180)`,
  `altiPropertyTable`, `altiStatus`, `altiTrap`, AgentX topology, SNMP properties,
  and trap-code blocks.
- Korean Altibase 7.1.0.7.9 Patch Notes for `BUG-49796`, the old `Altibase 6.5.1`
  `JDBC` performance-view error, `That had return update result`, and the
  `OPTIMIZER_PERFORMANCE_VIEW` workaround caveat.

## Documentation Shape

- `06_data_dictionary_performance_views.md`: keep the existing cookbook/object-block
  structure and add exact-token interpretation notes near the relevant check SQL.
- `08_performance_tuning_monitoring.md`: keep tuning workflows intact and add
  literal optimizer, hint, predicate-detail, Monitoring API, SNMP, and log-wait tokens
  in compact blocks.

## Safety Rules

- Verify target-version view and column availability with `V$TABLE` and `V$ALLCOLUMN`
  before hard-coding version-sensitive performance-view SQL.
- Do not recommend DML against `V$` performance views; they are read with `SELECT`.
- Do not recommend hints, indexes, statistics changes, or properties without current
  SQL text, plan, table/index metadata, statistics, and bottleneck evidence.
- For the `OPTIMIZER_PERFORMANCE_VIEW` patch workaround, ask for exact server patch
  level and client driver version first, and warn that performance-view query
  performance can degrade.
