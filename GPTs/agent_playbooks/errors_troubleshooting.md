# Errors And Troubleshooting Playbook

- Playbook ID: `APB-000013`
- Owning job: `S2-J008`
- Validation status: `pass`
- Supported versions: Altibase 7.1, Altibase 7.3, and `Altibase 8.1 verified source`, plus classified AID monitoring and troubleshooting routes
- Protected topic: yes

## Source Routes

Use this playbook for exact error handling, log and symptom triage, monitoring routes, dictionary and performance-view checks, first-pass performance tuning evidence, and escalation packets. It produces guarded first drafts and evidence bundles, not definitive diagnosis when customer evidence is missing.

| Route | Source IDs | Source-pack block refs | Baseline blocks |
| --- | --- | --- | --- |
| Error Message Reference and exact error response structure | `SRC-000054`, `SRC-000023`, `SRC-000118`, `SRC-000087`, `SRC-000178`, `SRC-000148` | `SRC-000054/BLOCK-000509`, `SRC-000023/BLOCK-000508`, `SRC-000118/BLOCK-000511`, `SRC-000087/BLOCK-000510`, `SRC-000178/BLOCK-000513`, `SRC-000148/BLOCK-000512` | `KAE-BLOCK-000273` |
| Properties, dictionary views, performance views, and safe check SQL | `SRC-000057`, `SRC-000026`, `SRC-000121`, `SRC-000090`, `SRC-000181`, `SRC-000151`, `SRC-000056`, `SRC-000025`, `SRC-000120`, `SRC-000089`, `SRC-000180`, `SRC-000150` | `SRC-000057/BLOCK-000521`, `SRC-000026/BLOCK-000520`, `SRC-000121/BLOCK-000523`, `SRC-000090/BLOCK-000522`, `SRC-000181/BLOCK-000525`, `SRC-000151/BLOCK-000524`, `SRC-000056/BLOCK-000515`, `SRC-000025/BLOCK-000514`, `SRC-000120/BLOCK-000517`, `SRC-000089/BLOCK-000516`, `SRC-000180/BLOCK-000519`, `SRC-000150/BLOCK-000518` | `KAE-BLOCK-000273` |
| Performance tuning first checks | `SRC-000067`, `SRC-000035`, `SRC-000129`, `SRC-000098`, `SRC-000189`, `SRC-000159` | `SRC-000067/BLOCK-000812`, `SRC-000035/BLOCK-000811`, `SRC-000129/BLOCK-000814`, `SRC-000098/BLOCK-000813`, `SRC-000189/BLOCK-000816`, `SRC-000159/BLOCK-000815` | `KAE-BLOCK-000283` |
| Log Analyzer and XLog diagnostics | `SRC-000062`, `SRC-000031`, `SRC-000126`, `SRC-000095`, `SRC-000186`, `SRC-000156` | `SRC-000062/BLOCK-000564`, `SRC-000031/BLOCK-000563`, `SRC-000126/BLOCK-000566`, `SRC-000095/BLOCK-000565`, `SRC-000186/BLOCK-000568`, `SRC-000156/BLOCK-000567` | `KAE-BLOCK-000280` |
| Monitoring API route | `SRC-000063`, `SRC-000032`, `SRC-000127`, `SRC-000096`, `SRC-000187`, `SRC-000157` | `SRC-000063/BLOCK-000605`, `SRC-000032/BLOCK-000603`, `SRC-000127/BLOCK-000609`, `SRC-000096/BLOCK-000607`, `SRC-000187/BLOCK-000613`, `SRC-000157/BLOCK-000611` | `KAE-BLOCK-000281` |
| SNMP Agent route | `SRC-000071`, `SRC-000039`, `SRC-000133`, `SRC-000102`, `SRC-000193`, `SRC-000162` | `SRC-000071/BLOCK-000606`, `SRC-000039/BLOCK-000604`, `SRC-000133/BLOCK-000610`, `SRC-000102/BLOCK-000608`, `SRC-000193/BLOCK-000614`, `SRC-000162/BLOCK-000612` | `KAE-BLOCK-000282` |
| Utility diagnostic route for `altierr`, dump tools, and trace evidence | `SRC-000076`, `SRC-000043`, `SRC-000137`, `SRC-000106`, `SRC-000197`, `SRC-000166` | `SRC-000076/BLOCK-000927`, `SRC-000043/BLOCK-000926`, `SRC-000137/BLOCK-000929`, `SRC-000106/BLOCK-000928`, `SRC-000197/BLOCK-000931`, `SRC-000166/BLOCK-000930` | `KAE-BLOCK-000274` |
| AID monitoring and troubleshooting working references | `AID-SRC-000431`, `AID-SRC-000432` | `BLOCK-000441`, `BLOCK-000442` | `KAE-BLOCK-000276` |

Guardrails: `CONF-000004`, `CONF-000005`, `CONF-000006`, `CONF-000007`, and `CONF-000008`. Exact cause/action text, full error tables, complete view columns, full API signatures, production monitoring policy, patch-specific behavior, and live-environment diagnosis still require target-version source blocks and customer evidence.

## Required Customer Inputs

Collect these exact error/evidence fields before giving a diagnosis or drafting remediation steps:

- `target_version`, `patch_level`, platform, server role, and whether the question targets Altibase 7.1, Altibase 7.3, or `Altibase 8.1 verified source`.
- `exact_error_code`, runtime code form such as `ERR-2106C`, `0x6100D`, decimal code, `SQLCODE`, `SQLSTATE`, or errno.
- `error_symbol` when available, such as `rpERR_ABORT_RP_SENDER_HANDSHAKE`, `cmERR_ABORT_SSL_HANDSHAKE`, or `idERR_FATAL_idc_SVC_INET_BIND_ERROR`.
- `error_message`, complete message text, source component, timestamp, process ID, session ID, transaction ID, statement ID, and client or tool output.
- `log_excerpt` with file name and timestamp, especially `$ALTIBASE_HOME/trc/altibase_boot.log`, `altibase_error.log`, `altibase_dump.log`, `altibase_qp.log`, `altibase_rp.log`, `altibase_rp_conflict.log`, `altibase_sm.log`, `altibase_snmp.log`, `altibase_mm.log`, client logs, and utility logs.
- `SQL_or_command`, bind values when supplied, query text, DDL/DCL/DML, tool command, connection string, DSN, JDBC URL, SNMP command, Monitoring API function, or Log Analyzer call.
- `object_definitions`: table, index, constraint, tablespace, datafile, replication, certificate, user, privilege, package, or procedure definitions related to the symptom.
- `runtime_state`: startup phase, session state, current locks, transaction state, replication state, archivelog state, tablespace state, property values, OS resource state, and current `V$` or `SYSTEM_` rows.
- `monitoring_route`: SQL query, Monitoring API, SNMP, Log Analyzer, iSQL, `altiProfile`, `altimon`, OS command, or support-escalation evidence path.
- `symptom_timeline`, impact, recurrence pattern, recent changes, expected result, validation window, `rollback_plan`, cleanup plan, and `escalation_goal`.

If any required field is missing, ask for it and provide the safest source-backed next check. Do not infer a definitive root cause from an error prefix, one log line, or a generic database pattern.

## Generated Artifacts

This playbook may draft diagnostics packets, read-only SQL, command checklists, monitoring route choices, performance evidence plans, and escalation packets. State-changing fixes remain protected and require source recheck, approval, validation, and rollback evidence.

### Exact error triage packet

```text
error_packet:
  target_version: <7.1|7.3|8.1_verified>
  patch_level: <exact patch or unknown>
  exact_error_code: <ERR-/hex/decimal/SQLCODE/SQLSTATE/errno>
  error_symbol: <source symbol or unknown>
  error_message: <complete runtime message>
  component: <server|client|iSQL|iLoader|JDBC|ODBC|replication|Log Analyzer|SNMP|Monitoring API|utility>
  source_route: <SRC ids, BLOCK ids, KAE-BLOCK ids>
  log_excerpt: <file name, timestamp range, exact lines>
  SQL_or_command: <exact statement or command>
  object_definitions: <table/index/tablespace/replication/certificate/user definitions>
  runtime_state: <startup/session/lock/transaction/replication/property/OS evidence>
  safe_next_check: <read-only SQL, altierr lookup, log collection, installed help, or source block recheck>
  escalation_stop_point: <why the answer must stop or can proceed>
```

### Error-code lookup commands

```bash
altierr 0x00015
altierr -w 00015
altierr 21
altierr -266286
altierr 266286
altierr 0x4102E
altierr -w connect
```

Preserve both runtime and source forms. Examples that require exact source and evidence include `0x0001F (31) idERR_FATAL_idc_SVC_INET_BIND_ERROR`, `0x2106D (135277) mtERR_ABORT_JSON_WITHOUT_TEMPLOB`, `0x6100D (397325) rpERR_ABORT_RP_SENDER_HANDSHAKE`, `0x61010 (397328) rpERR_ABORT_RP_SENDER_START`, `0x710A0 (463008) cmERR_ABORT_INVALID_CERTIFICATE`, `0x710A3 (463011) cmERR_ABORT_SSL_HANDSHAKE`, and `ERR-2106C`.

### Log and evidence collection draft

```bash
test -n "$ALTIBASE_HOME" && ls -ld "$ALTIBASE_HOME" "$ALTIBASE_HOME/trc"
ls -l "$ALTIBASE_HOME/trc"
tail -200 "$ALTIBASE_HOME/trc/altibase_boot.log"
tail -200 "$ALTIBASE_HOME/trc/altibase_qp.log"
tail -200 "$ALTIBASE_HOME/trc/altibase_rp.log"
tail -200 "$ALTIBASE_HOME/trc/altibase_error.log"
tail -200 "$ALTIBASE_HOME/trc/altibase_snmp.log"
grep -n "ERR-" "$ALTIBASE_HOME/trc/altibase_boot.log"
```

For crash or abnormal termination, collect the complete `$ALTIBASE_HOME/trc` directory before restart when service constraints allow it. For suspected hang/no response, collect OS stack snapshots, system logs, and all trace logs before restarting when possible.

### Read-only SQL first checks

```sql
-- 00_property_and_version_check.sql
SELECT NAME, VALUE1, VALUE2
FROM V$PROPERTY
WHERE NAME IN ('DB_NAME', 'ADMIN_MODE', 'ARCHIVE_DIR',
               'TEMPORARY_LOB_ENABLE', 'REPLICATION_DDL_ENABLE',
               'REPLICATION_DDL_ENABLE_LEVEL', 'SSL_ENABLE',
               'TIMED_STATISTICS', 'QUERY_PROF_FLAG',
               'QUERY_PROF_LOG_DIR', 'TRX_UPDATE_MAX_LOGSIZE',
               'TOTAL_WA_SIZE', 'TEMP_MAX_PAGE_COUNT')
ORDER BY NAME;

-- 10_view_availability_check.sql
SELECT NAME, SLOTSIZE, COLUMNCOUNT
FROM V$TABLE
WHERE NAME IN ('V$VERSION', 'V$PROPERTY', 'V$ALLCOLUMN',
               'V$SESSION', 'V$STATEMENT', 'V$SQLTEXT',
               'V$PLANTEXT', 'V$SESSION_WAIT', 'V$LOCK_WAIT',
               'V$TRANSACTION', 'V$REPGAP', 'V$REPSENDER',
               'V$REPRECEIVER', 'V$LFG')
ORDER BY NAME;

-- 20_column_availability_check.sql
SELECT TABLENAME, COLNAME
FROM V$ALLCOLUMN
WHERE TABLENAME IN ('V$SESSION', 'V$STATEMENT', 'V$SQLTEXT',
                    'V$PLANTEXT', 'V$SESSION_WAIT', 'V$LOCK_WAIT',
                    'V$TRANSACTION', 'V$REPGAP', 'V$REPSENDER',
                    'V$REPRECEIVER', 'V$LFG')
ORDER BY TABLENAME, COLNAME;

-- 30_replication_gap_check.sql
SELECT REP_NAME, REP_GAP
FROM V$REPGAP;
```

Use `V$TABLE` and `V$ALLCOLUMN` before adding column-specific SQL. Do not infer view columns from another Altibase version or from another DBMS.

### Performance tuning evidence plan

```text
performance_evidence:
  symptom: <CPU|memory growth|slow SQL|lock wait|redo log prepare wait|replication delay|disk tablespace|query plan>
  workload_goal: <latency|throughput|resource limit|recovery objective>
  SQL_text: <complete SQL or unknown>
  plan_output: <EXPLAIN PLAN, V$PLANTEXT, or unknown>
  object_definitions: <tables, indexes, constraints, partitioning, statistics>
  source_checks: <Performance Tuning Guide, General Reference, SQL Reference>
  first_views: <V$SESSION_WAIT, V$SYSTEM_EVENT, V$SESSION_EVENT, V$SYSSTAT, V$SESSTAT, V$MEMSTAT, V$BUFFPOOL_STAT, V$LFG>
  property_checks: <TIMED_STATISTICS, QUERY_PROF_FLAG, SQL_PLAN_CACHE_SIZE, PREPARE_LOG_FILE_COUNT, SORT_AREA_SIZE, HASH_AREA_SIZE>
  validation_metric: <before/after metric>
  rollback_plan: <restore property, remove hint, stop profiling, revert SQL, or restore config>
```

`altiProfile` and `QUERY_PROF_FLAG` are diagnostic routes only after the customer approves the observation window and disk-impact risk. Stop profiling and preserve generated `*.prof` output with the exact command used to convert it.

### Monitoring API and SNMP routes

```text
monitoring_route:
  Monitoring API:
    prerequisites: altibaseMonitor.h, libaltibaseMonitor.a, local Unix domain socket, ABIInitialize, ABISetProperty, ABICheckConnection
    functions: ABIGetVSession, ABIGetVSessionWait, ABIGetSqlText, ABIGetLockPairBetweenSessions, ABIGetDBInfo, ABIGetReadCount, ABIGetRepGap, ABIGetRepSentLogCount, ABIGetErrorMessage
    stop_if_missing: installed header, library, same-host evidence, thread model, live socket state
  SNMP:
    daemons: snmpd, snmptrapd, altisnmpd
    files: ALTIBASE-MIB.txt, snmpd.conf, altisnmpd.conf, altisnmp.env
    properties: SNMP_ENABLE, SNMP_PORT_NO, SNMP_TRAP_PORT_NO, SNMP_RECV_TIMEOUT, SNMP_SEND_TIMEOUT
    checks: snmpwalk, snmpget, snmpset, AgentX route, MIBDIRS, MIBS=ALL
    stop_if_missing: NET-SNMP version, ports, community policy, firewall rules, live daemon output
```

## Procedure

1. Classify the request as exact error, startup/connectivity, SQL execution, lock or transaction, memory/tablespace, replication, TLS, Log Analyzer, Monitoring API, SNMP, performance tuning, crash, or hang.
2. Preserve exact runtime tokens. Keep `ERR-` code, hex code, decimal code, `SQLCODE`, `SQLSTATE`, errno, symbol, message, property name, view name, command option, path, and log filename exactly as supplied.
3. Choose the source route. Use Error Message Reference entries for cause/action, General Reference for properties and views, Performance Tuning Guide for tuning routes, Monitoring API guide for `ABI*` functions, SNMP Agent Guide for `altisnmpd` and MIB work, Log Analyzer guide for XLog and `ALA_*` routes, Utilities Manual for `altierr`, and AID `llm-reference` only with preserved classification labels.
4. Ask for missing exact error/evidence fields before diagnosing. If the user lacks the exact error, request the full log line and provide a read-only source-backed next check.
5. Run non-destructive checks first: source block recheck, `altierr`, installed help, log tail, `V$TABLE`, `V$ALLCOLUMN`, property lookup, and scoped `V$` samples.
6. For performance symptoms, collect workload, SQL text, plan, object definitions, statistics state, property values, and before/after metric before proposing any hint, property, profile, or schema change.
7. For monitoring integrations, prove the route first. Monitoring API requires same-server Unix-domain-socket evidence and installed headers/libraries; SNMP requires `snmpd`, `snmptrapd`, `altisnmpd`, `ALTIBASE-MIB`, properties, ports, and live command output.
8. If evidence points to recovery, restart, replication reset, certificate replacement, object rebuild, property change, or destructive cleanup, stop at an escalation packet unless exact source, customer approval, validation plan, and rollback plan are present.

## Guardrails

- Do not provide a definitive diagnosis when exact error text, logs, object definitions, runtime state, version, or patch level are missing. Ask for the missing evidence and provide the safest source-backed next check.
- Do not infer severity, module, cause, action, or `SQLSTATE` from an error prefix such as `qpERR_`, `rpERR_`, `cmERR_`, `ERR-`, or one partial message.
- Do not broaden AID English-only auxiliary material into Korean-authoritative guidance. Preserve `AID source-backed llm-reference`, Korean-source-verified, Link-validated Korean-source-verified, English-only source, and source_limitation labels when using `AID-SRC-000431` or `AID-SRC-000432`.
- Do not convert README/source-index labels into behavior claims. Route to the exact manual body or baseline block.
- Do not recommend property changes, restart, recovery, object rebuild, replication reset, certificate replacement, or SNMP read-write changes without target-version source, current runtime evidence, maintenance approval, validation checks, and rollback plan.
- Do not leave `QUERY_PROF_FLAG`, `TIMED_STATISTICS`, `altiProfile`, `altimon`, SNMP daemons, or temporary evidence scripts running beyond the approved observation window.

## Validation Checks

Every generated troubleshooting or performance response must include:

- Source route: source IDs, source-pack block refs, baseline block IDs, and guardrail IDs.
- Exact error/evidence fields received and exact fields still missing.
- Target version and patch level, or an explicit statement that the installed patch is unknown.
- A safe next check that is read-only unless the customer has approved impact.
- View existence and column existence checks before view-column SQL.
- Expected result shape, such as error symbol/cause/action from `altierr`, one row per property, one row per view, matching log timestamps, profile output file, or SNMP command output.
- Validation metric and rollback plan for any performance, property, profiling, monitoring, or state-changing suggestion.
- Escalation stop points when source, runtime, customer approval, or rollback evidence is incomplete.

## Stop Conditions

Stop and ask for more evidence if:

- Only an error prefix, symbol family, partial message, or screenshot is supplied without exact code, complete message text, and log context.
- The requested answer depends on exact Error Message Reference cause/action for a code that has not been rechecked in the target-version source block.
- The answer depends on current locks, sessions, transactions, replication state, Monitoring API return structures, SNMP OIDs, Log Analyzer protocol state, performance-view columns, or OS resource samples that are not supplied.
- The symptom is crash, abnormal termination, suspected hang, missing redo log, missing datafile, incompatible backup, corruption suspicion, or repeated out-of-memory. Collect evidence and escalate instead of inventing a fix.
- The next action would restart Altibase, run recovery, reset replication, drop or rebuild objects, change certificates, change properties, change SNMP read-write objects, or enable heavy profiling without approval and rollback.

### Escalation Stop Points

- Support escalation packet required: exact version and patch, complete `$ALTIBASE_HOME/trc` collection, customer impact, reproduction steps, last changes, OS evidence, SQL/command text, object definitions, and source route.
- Product-defect or crash escalation: include `altibase_error.log`, `altibase_dump.log`, complete trace directory, stack snapshots for hangs, and whether evidence was collected before restart.
- Performance escalation: include workload goal, slow SQL, `V$STATEMENT`/`V$SQLTEXT`/`V$PLANTEXT` evidence where available, OS CPU or memory evidence, property values, statistics state, and before/after metrics.
- Monitoring escalation: include Monitoring API headers/library evidence, `ABICheckConnection` or `ABIGetErrorMessage` output, SNMP daemon status, `snmpwalk`/`snmpget` output, `ALTIBASE-MIB.txt`, and `altisnmpd` or `altibase_snmp.log` excerpts.

## Cleanup And Rollback

Archive diagnostics with timestamps and source routes. Remove temporary scripts after review, protect credentials in collected commands, stop `tail -f`, stop approved profiling, restore any temporary `QUERY_PROF_FLAG` or `TIMED_STATISTICS` value to the recorded prior state, stop temporary `altimon` or SNMP test daemons if they were started for diagnostics, and keep rollback evidence with the final escalation packet. Do not delete trace logs, bad files, profile files, or crash evidence until the customer confirms they are preserved elsewhere.
