# Replication And CDC Playbook

- Playbook ID: `APB-000007`
- Owning job: `S2-J006`
- Validation status: `pass`
- Supported versions: Altibase 7.1, Altibase 7.3, and `Altibase 8.1 verified source`
- Protected topic: yes

## Source Routes

| Route | Source IDs | Source-pack block refs | Baseline blocks |
| --- | --- | --- | --- |
| Replication topology, `CREATE REPLICATION`, `ALTER REPLICATION`, `DROP REPLICATION`, LAZY/EAGER mode, conflict handling, `SYNC`, `SYNC ONLY`, `QUICKSTART`, DDL synchronization, Fail-Over, sequence replication, metadata, and runtime checks | `SRC-000070`, `SRC-000038`, `SRC-000132`, `SRC-000101`, `SRC-000192`, `SRC-000161` | `SRC-000070/BLOCK-000845`, `SRC-000038/BLOCK-000844`, `SRC-000132/BLOCK-000847`, `SRC-000101/BLOCK-000846`, `SRC-000192/BLOCK-000849`, `SRC-000161/BLOCK-000848` | `KAE-BLOCK-000272`, `KAE-BLOCK-000273` |
| Log Analyzer and CDC-style XLog Sender routing, `FOR ANALYSIS`, XLog Collector workflow, ALA API, metadata, and XLog conversion guardrails | `SRC-000062`, `SRC-000031`, `SRC-000126`, `SRC-000095`, `SRC-000186`, `SRC-000156` | `SRC-000062/BLOCK-000564`, `SRC-000031/BLOCK-000563`, `SRC-000126/BLOCK-000566`, `SRC-000095/BLOCK-000565`, `SRC-000186/BLOCK-000568`, `SRC-000156/BLOCK-000567` | `KAE-BLOCK-000280` |
| Replication Manager GUI route, manual workflow, release-note route, tool version, package, Java/JRE, JDBC driver, full-mesh, pair, sync, and drop guardrails | `SRC-000211`, `SRC-000204`, `SRC-000225`, `SRC-000218`, `SRC-000464`, `SRC-000443`, `SRC-000465`, `SRC-000444`, `SRC-000466`, `SRC-000445` | `SRC-000211/BLOCK-000843`, `SRC-000204/BLOCK-000842`, `SRC-000225/BLOCK-000835`, `SRC-000218/BLOCK-000834`, `SRC-000464/BLOCK-000837`, `SRC-000443/BLOCK-000836`, `SRC-000465/BLOCK-000839`, `SRC-000444/BLOCK-000838`, `SRC-000466/BLOCK-000841`, `SRC-000445/BLOCK-000840` | `KAE-BLOCK-000286`, `KAE-BLOCK-000287` |
| Altibase 8.1 verified source replication SSL separation, release-note evidence, property and SQL source routing, and ordinary SSL/TLS handoff | `SRC-000452`, `SRC-000429`, `SRC-000477`, `SRC-000180`, `SRC-000150`, `SRC-000194`, `SRC-000163`, `SRC-000175`, `SRC-000145` | `SRC-000452/BLOCK-000826`, `SRC-000429/BLOCK-000825`, `SRC-000477/BLOCK-000829`, `SRC-000180/BLOCK-000519`, `SRC-000150/BLOCK-000518`, `SRC-000194/BLOCK-000888`, `SRC-000163/BLOCK-000887`, `SRC-000175/BLOCK-000855`, `SRC-000145/BLOCK-000854` | `KAE-BLOCK-000253`, `KAE-BLOCK-000272`, `KAE-BLOCK-000273`, `KAE-BLOCK-000275` |

Guardrails: `CONF-000004`, `CONF-000005`, `CONF-000006`, `CONF-000007`, and
`CONF-000008` remain active. This playbook drafts guarded first checks,
topology plans, SQL templates, and validation bundles only. Do not present
state-changing replication commands as production-ready unless the exact
target-version source block, customer topology, object definitions, current
runtime state, logs, validation plan, and rollback or recovery plan are all
available.

Forbidden assumption note: do not infer Altibase replication behavior from
Oracle, generic CDC, generic HA, or generic GUI-tool assumptions. Replication
is a protected, data-moving operation.

## Required Customer Inputs

Missing input prompts to collect before generating replication, CDC, HA, or
Replication Manager artifacts:

- Target Altibase version and patch level for every node, plus whether any
  node uses `Altibase 8.1 verified source` features.
- Topology: Active-Standby, Active-Active, pair, full-mesh, Log Analyzer
  XLog Sender to XLog Collector, propagation, sequence replication, or
  client Fail-Over route.
- Local and remote host names or IP addresses, ordinary `REPLICATION_PORT_NO`,
  Altibase 8.1 `REPLICATION_SSL_PORT_NO` if SSL replication is requested,
  and whether the request is TCP, InfiniBand, UNIX domain, ordinary SSL/TLS,
  or replication SSL.
- Replication object name, mode (`LAZY` or `EAGER`), role (`AS MASTER` or
  `AS SLAVE` if used), options, source and target table or partition names,
  primary keys, partitioning, constraints, unique indexes, and whether primary
  key updates are planned.
- Connected user and privilege path. Replication-related statements require
  the `SYS` user route in the checked Replication Manual sources.
- Character-set evidence from `NLS_CHARACTERSET` and
  `NLS_NCHAR_CHARACTERSET`, plus object DDL from both nodes.
- Current runtime evidence from `V$VERSION`, `SYSTEM_.SYS_REPLICATIONS_`,
  `SYSTEM_.SYS_REPL_HOSTS_`, `SYSTEM_.SYS_REPL_ITEMS_`, `V$REPSENDER`,
  `V$REPRECEIVER`, `V$REPGAP`, `V$REPSYNC`, and relevant trace logs such as
  `altibase_rp.log`.
- Current operation target: create, start, `SYNC`, `SYNC ONLY`, stop,
  `QUICKSTART`, `RESET`, `DROP TABLE`, `ADD TABLE`, `DROP REPLICATION`, host
  change, `FLUSH`, DDL synchronization, SQL Apply Mode, failback, conflict
  handling, Log Analyzer CDC, Replication Manager GUI route, or client
  Fail-Over.
- For Log Analyzer: XLog Sender name, XLog Collector host and port or
  `UNIX_DOMAIN`, `$ALTIBASE_HOME`, archivelog mode, `REPLICATION_LOG_BUFFER_SIZE`,
  analyzed tables, installed `alaAPI.h`, `alaTypes.h`, `libala_sl.x`,
  `libala.x`, ACK policy, XLog pool size, and whether ODBC C conversion is
  required.
- For Replication Manager: tool version, package filename, OS, Java/JRE,
  imported JDBC driver file, `Connection Name`, `DB Address`, `DB Port`,
  `DB Name`, `IP Address Type`, `NLS for Client`, `Extra Host IP`, DB
  Connection list, and intended GUI action.
- Customer-approved maintenance window, data-consistency objective, expected
  validation output, rollback plan, recovery plan, and explicit approval for
  any data-loss, data-movement, service-migration, destructive, or
  replication-changing effect.

## Generated Artifacts

This playbook may draft:

- Replication topology evidence requests and decision records.
- Guarded `CREATE REPLICATION`, `ALTER REPLICATION`, and `DROP REPLICATION`
  first-draft SQL templates with placeholders and stop points.
- Non-destructive metadata, state, gap, sender, receiver, and property checks.
- `SYNC`, `SYNC ONLY`, failback, SQL Apply Mode, and conflict-handling
  validation bundles.
- DDL synchronization checklists that preserve property setup and restore
  steps.
- Log Analyzer CDC setup and XLog Collector workflow outlines.
- Replication Manager GUI route checklists and generated-SQL verification
  prompts.
- Client Fail-Over routing notes for JDBC, ODBC/CLI, Embedded SQL, or PDO,
  with handoff to the client playbooks for full code.
- Replication SSL separation notes for Altibase 8.1 verified source.

## Procedure

1. Classify the request before drafting SQL or commands. Separate ordinary
   table replication, Log Analyzer CDC, Replication Manager GUI workflows,
   client Fail-Over, DDL synchronization, SQL Apply Mode, and Altibase 8.1
   replication SSL.
2. Confirm source and version route. Use 7.1 source blocks for 7.1, 7.3 source
   blocks for 7.3, and `Altibase 8.1 verified source` blocks for 8.1-only
   features such as `USING SSL` and `REPLICATION_SSL_PORT_NO`.
3. Start with non-destructive evidence checks. Do not generate a runnable
   `CREATE REPLICATION`, `ALTER REPLICATION`, `DROP REPLICATION`, or
   Replication Manager operation until node versions, topology, object
   definitions, endpoints, state, gap, logs, and validation goals are known.
4. For ordinary replication DDL, preserve the paired-object requirement. The
   same replication object name is created on both nodes, and each node points
   to the peer host and peer replication port. Table or partition mappings are
   one-to-one. Confirm the `SYS` execution route before drafting runnable
   replication DDL.
5. For `SYNC`, `SYNC ONLY`, and failback, check current transactions, locks,
   `REPLICATION_SYNC_LOCK_TIMEOUT`, `V$REPGAP`, `V$REPSENDER`,
   `V$REPRECEIVER`, and `V$REPSYNC` first. Stopping an active `SYNC` task can
   require deleting all records from all replication target tables before
   performing `SYNC` again.
6. Treat `QUICKSTART`, `RESET`, `DROP TABLE`, `DROP HOST ALL`,
   `DROP REPLICATION`, offline replication, and receive-only conversion as
   protected operations. `QUICKSTART` starts from the current log position and
   can skip undelivered replication data. `RESET` changes restart information
   and is allowed only while replication is stopped.
7. For conflicts, identify INSERT, UPDATE, or DELETE conflict class, conflict
   policy, active topology, `REPLICATION_INSERT_REPLACE`,
   `REPLICATION_UPDATE_REPLACE`, `AS MASTER`, `AS SLAVE`, timestamp-based
   configuration, and `altibase_rp.log` evidence. Do not promise perfect data
   consistency for conflicting Active-Active updates.
8. For replication-changing DDL, choose either the standard DDL execution
   procedure or DDL synchronization route based on the exact source and
   topology. Preserve `REPLICATION_DDL_ENABLE`,
   `REPLICATION_DDL_ENABLE_LEVEL`, `REPLICATION_DDL_SYNC`,
   `REPLICATION_SQL_APPLY_ENABLE`, `ALTER SESSION SET REPLICATION = DEFAULT`,
   `ALTER REPLICATION ... FLUSH`, service migration, property restore, and
   SQL Apply Mode validation.
9. For Log Analyzer, route `FOR ANALYSIS` and `FOR ANALYSIS PROPAGATION` to
   the Log Analyzer source, not to ordinary replication. The XLog Collector
   must be online and waiting before starting the XLog Sender. Do not combine
   Log Analyzer `FOR ANALYSIS` with `USING SSL` or `USING IB`; use TCP or
   `UNIX_DOMAIN` only when the source and environment support it.
10. For Replication Manager, treat GUI actions as convenience routes that must
    be verified against the Replication Manual and live state. `Start`, `Stop`,
    `Quick Start`, `Sync`, `Sync Only`, `Drop`, `Edit Table List`, `Show DDL`,
    `Compare DDL`, `Create Full-mesh Replications`, and `Create Replication
    Pair` still require exact tool version, JDBC driver, topology, runtime
    state, and post-action validation.
11. For Fail-Over, distinguish connection success from data consistency.
    Preserve `AlternateServers`, `ConnectionRetryCount`,
    `ConnectionRetryDelay`, `SessionFailOver`, callback validation, and
    interface-specific success tokens such as `ES_08FO01`,
    `ALTIBASE_FAILOVER_SUCCESS`, and `PDO::ALTIBASE_FAILOVER_SUCCESS`. Route
    full JDBC, ODBC/CLI, Embedded SQL, or PDO code to the relevant client
    playbook.
12. For replication SSL, keep ordinary client/server SSL/TLS separate from
    replication SSL. Ordinary clients use `SSL_PORT_NO` or client SSL
    connection properties. Altibase 8.1 verified source replication SSL uses
    `CREATE REPLICATION ... USING SSL` and the peer node's
    `REPLICATION_SSL_PORT_NO`; both replication target servers need SSL setup
    before SSL replication is drafted.

## Artifact Templates

```sql
-- 00_replication_evidence_precheck.sql
-- Keep only the property names that exist in the exact target-version source.
SELECT * FROM V$VERSION;

SELECT NAME, VALUE1, VALUE2
FROM V$PROPERTY
WHERE NAME IN ('REPLICATION_PORT_NO',
               'REPLICATION_SSL_PORT_NO',
               'REPLICATION_MAX_COUNT',
               'REPLICATION_SYNC_LOCK_TIMEOUT',
               'REPLICATION_DDL_ENABLE',
               'REPLICATION_DDL_ENABLE_LEVEL',
               'REPLICATION_DDL_SYNC',
               'REPLICATION_SQL_APPLY_ENABLE',
               'REPLICATION_LOG_BUFFER_SIZE',
               'SSL_ENABLE',
               'SSL_PORT_NO')
ORDER BY NAME;

SELECT NAME, VALUE1
FROM V$NLS_PARAMETERS
WHERE NAME IN ('NLS_CHARACTERSET', 'NLS_NCHAR_CHARACTERSET')
ORDER BY NAME;

SELECT *
FROM SYSTEM_.SYS_REPLICATIONS_
WHERE REPLICATION_NAME = '<REPLICATION_NAME>';

SELECT *
FROM SYSTEM_.SYS_REPL_HOSTS_
WHERE REPLICATION_NAME = '<REPLICATION_NAME>';

SELECT *
FROM SYSTEM_.SYS_REPL_ITEMS_
WHERE REPLICATION_NAME = '<REPLICATION_NAME>';

SELECT REP_NAME, STATUS, NET_ERROR_FLAG, SENDER_IP, SENDER_PORT, PEER_IP, PEER_PORT
FROM V$REPSENDER
WHERE REP_NAME = '<REPLICATION_NAME>';

SELECT REP_NAME, MY_IP, MY_PORT, PEER_IP, PEER_PORT, SQL_APPLY_TABLE_COUNT
FROM V$REPRECEIVER
WHERE REP_NAME = '<REPLICATION_NAME>';

SELECT REP_NAME, REP_GAP
FROM V$REPGAP
WHERE REP_NAME = '<REPLICATION_NAME>';
```

```sql
-- 10_replication_create_template.sql
-- Guarded first draft only. Replace every placeholder from customer evidence.
-- Run corresponding reversed peer definitions on both nodes after source check.

CREATE [LAZY|EAGER] REPLICATION <replication_name>
WITH '<peer_host>', <peer_replication_port> [USING TCP|IB]
FROM <local_user>.<local_table> [PARTITION <local_partition>]
TO <remote_user>.<remote_table> [PARTITION <remote_partition>];

ALTER REPLICATION <replication_name> SYNC;
-- or:
ALTER REPLICATION <replication_name> SYNC ONLY;
-- or:
ALTER REPLICATION <replication_name> START;
```

```sql
-- 11_replication_ssl_8_1_template.sql
-- Altibase 8.1 verified source route only.
-- Use the peer node's REPLICATION_SSL_PORT_NO, not SSL_PORT_NO.
-- Do not use this for Log Analyzer FOR ANALYSIS.

CREATE REPLICATION <replication_name>
WITH '<peer_host>', <peer_replication_ssl_port> USING SSL
FROM <local_user>.<local_table>
TO <remote_user>.<remote_table>;
```

```sql
-- 20_state_change_hold_points.sql
-- Fill these only after the precheck output and approval are available.

ALTER REPLICATION <replication_name> FLUSH [ALL] [WAIT <timeout_sec>];
ALTER REPLICATION <replication_name> STOP;
ALTER REPLICATION <replication_name> RESET;
ALTER REPLICATION <replication_name> DROP TABLE
FROM <local_user>.<local_table> TO <remote_user>.<remote_table>;
ALTER REPLICATION <replication_name> ADD TABLE
FROM <local_user>.<local_table> TO <remote_user>.<remote_table>;
ALTER REPLICATION <replication_name> START;
DROP REPLICATION <replication_name>;
```

```sql
-- 30_ddl_synchronization_guarded_route.sql
-- Use only after checking exact source restrictions and current topology.

-- Local server where the DDL is executed:
ALTER SYSTEM SET REPLICATION_DDL_ENABLE = 1;
ALTER SYSTEM SET REPLICATION_DDL_ENABLE_LEVEL = 1;
ALTER SESSION SET REPLICATION_DDL_SYNC = 1;
ALTER SESSION SET REPLICATION = DEFAULT;
ALTER REPLICATION <replication_name> FLUSH;

-- Execute the approved DDL here.

ALTER SYSTEM SET REPLICATION_DDL_ENABLE = 0;
ALTER SYSTEM SET REPLICATION_DDL_ENABLE_LEVEL = 0;
ALTER SESSION SET REPLICATION_DDL_SYNC = 0;

-- Remote server route also requires REPLICATION_SQL_APPLY_ENABLE handling
-- when the exact source route and topology require SQL Apply Mode.
```

```sql
-- 40_log_analyzer_xlog_sender_template.sql
-- Guarded Log Analyzer CDC route. The XLog Collector must already be waiting.
-- Do not combine FOR ANALYSIS with USING SSL or USING IB.

CREATE REPLICATION <xlog_sender_name> FOR ANALYSIS
WITH '<xlog_collector_host>', <xlog_collector_port>
FROM <source_user>.<source_table>
TO <source_user>.<source_table>;

ALTER REPLICATION <xlog_sender_name> START;
-- Log Analyzer-only alternative when source conditions are met:
-- ALTER REPLICATION <xlog_sender_name> START AT SN (<xlog_sender_start_sn>);

ALTER REPLICATION <xlog_sender_name> FLUSH [ALL] [WAIT <timeout_sec>];
ALTER REPLICATION <xlog_sender_name> STOP;
DROP REPLICATION <xlog_sender_name>;
```

```text
# 50_log_analyzer_collector_workflow.txt
Initialize: ALA_InitializeAPI
Create: ALA_CreateXLogCollector
Optional auth/timeouts/pool: ALA_AddAuthInfo, ALA_SetHandshakeTimeout,
ALA_SetReceiveXLogTimeout, ALA_SetXLogPoolSize
Handshake: ALA_Handshake
Loop: ALA_ReceiveXLog, ALA_GetXLog, inspect XLog, ALA_SendACK, ALA_FreeXLog
Status: ALA_GetXLogCollectorStatus
Metadata: ALA_GetProtocolVersion, ALA_GetReplicationInfo, ALA_GetTableInfo
Conversion: ALA_GetAltibaseText, ALA_GetAltibaseSQL, ALA_GetODBCCValue
Errors: ALA_ClearErrorMgr, ALA_GetErrorCode, ALA_GetErrorLevel, ALA_GetErrorMessage
Cleanup: ALA_DestroyXLogCollector, ALA_DestroyAPI
```

```text
# 60_replication_manager_route.txt
Tool version:
Package filename:
OS and Java/JRE:
Imported JDBC driver:
Connection Name:
DB Address / DB Port / DB Name:
IP Address Type:
NLS for Client:
Extra Host IP:
GUI action:
Generated SQL or DDL shown by tool:
Replication Manual source route:
Runtime state evidence:
Post-action validation:
Rollback or recovery:
```

```text
# 70_failover_route.txt
Connection Time Fail-Over or Service Time Fail-Over:
AlternateServers:
ConnectionRetryCount:
ConnectionRetryDelay:
SessionFailOver:
Callback route: JDBC ABFailOverCallback, ODBC/CLI ALTIBASE_FAILOVER_CALLBACK,
Embedded SQL REGISTER FAIL_OVER_CALLBACK, or PDO setFailoverCallback
Data consistency validation query:
Retry boundary:
Success token: ES_08FO01, ALTIBASE_FAILOVER_SUCCESS, or PDO::ALTIBASE_FAILOVER_SUCCESS
```

## Guardrails

- Stop before any replication-changing command when the exact target version,
  patch, topology, peer endpoints, object DDL, primary keys, current state,
  replication gap, logs, validation plan, and rollback or recovery plan are
  missing.
- Stop before `QUICKSTART` unless the customer explicitly accepts the risk of
  starting from the current log position and possibly skipping undelivered
  replication data.
- Stop before `RESET`, `DROP TABLE`, `DROP HOST ALL`, `DROP REPLICATION`, or
  offline replication unless replication is stopped where required and the
  consistency impact is documented.
- Stop before DDL synchronization or SQL Apply Mode if the source restrictions,
  service migration plan, property restore plan, lock impact, and
  `V$REPRECEIVER.SQL_APPLY_TABLE_COUNT` validation are not available.
- Stop before EAGER mode or failback guidance if both-node EAGER status,
  time synchronization, network-failure history, recovery options, and
  commit-related property evidence are missing.
- Stop before conflict resolution advice if the INSERT, UPDATE, or DELETE
  conflict class, replication role, replace properties, timestamps, and
  `altibase_rp.log` evidence are missing.
- Stop before Log Analyzer code or commands if installed headers, libraries,
  protocol version, XLog Collector state, `$ALTIBASE_HOME`, archivelog mode,
  `REPLICATION_LOG_BUFFER_SIZE`, ACK policy, or XLog Sender metadata is
  missing.
- Stop before Replication Manager `Quick Start`, `Drop`, full-mesh, sync, or
  table-list edit instructions when tool version, JDBC driver, current state,
  object definitions, generated DDL, or runtime validation is missing.
- Stop before replication SSL guidance unless both nodes are in the
  `Altibase 8.1 verified source` route or another exact source route is
  provided. Do not treat `SSL_PORT_NO` as `REPLICATION_SSL_PORT_NO`.
- Stop if the request asks for a complete production HA architecture,
  patch-specific compatibility matrix, current package availability, every
  Replication Manager screen, exhaustive ALA API signatures, or a live
  troubleshooting verdict from this playbook alone.

## Validation Checks

Every replication, CDC, HA, Log Analyzer, or Replication Manager artifact must
include:

- Exact source route: source IDs, source-pack block refs, baseline block refs,
  target version, and guardrail IDs.
- Missing-input prompt list and explicit assumptions.
- Non-destructive prechecks for version, properties, topology, metadata,
  sender/receiver state, gap, logs, and object definitions.
- Validation SQL for `SYSTEM_.SYS_REPLICATIONS_`, `SYSTEM_.SYS_REPL_HOSTS_`,
  `SYSTEM_.SYS_REPL_ITEMS_`, `V$REPSENDER`, `V$REPRECEIVER`, `V$REPGAP`, and
  `V$REPSYNC` where relevant.
- Explicit distinction among ordinary replication, Log Analyzer CDC,
  Replication Manager GUI workflow, client Fail-Over, ordinary SSL/TLS, and
  Altibase 8.1 replication SSL.
- Conflict, sync, and DDL synchronization risk notes when the task could alter
  data consistency.
- Rollback, cleanup, restore, rebuild, or resync note, including when SQL
  rollback is not sufficient.
- Human DBA approval hold point for data-moving, data-loss, topology-changing,
  DDL-changing, or replication-changing effects.

## Common Errors And First Checks

- Handshake or start failure: check peer host, peer port, `REPLICATION_PORT_NO`
  or `REPLICATION_SSL_PORT_NO`, protocol route, role compatibility, trace logs,
  and `V$REPSENDER.NET_ERROR_FLAG`.
- Sync failure or lock timeout: check current sessions, active transactions,
  `REPLICATION_SYNC_LOCK_TIMEOUT`, `V$REPSYNC`, target table locks, and
  conflict logs before retrying.
- Conflict messages in `altibase_rp.log`: classify INSERT, UPDATE, or DELETE
  conflict and ask for both-node row evidence before choosing a resolution
  route.
- DDL replication failure: check property values, DDL synchronization
  restrictions, SQL Apply Mode, service migration, table identity, object DDL,
  and `V$REPRECEIVER.SQL_APPLY_TABLE_COUNT`.
- Log Analyzer API failure: identify the exact API function, call
  `ALA_GetErrorLevel`, then apply the source route for `ALA_ERROR_FATAL`,
  `ALA_ERROR_ABORT`, or `ALA_ERROR_INFO`.
- Replication Manager display mismatch: check imported JDBC driver, connected
  DB Connections, `Extra Host IP`, replication object names, peer endpoints,
  and live metadata before treating the GUI map as health proof.

## Stop Conditions

Stop and ask for missing input if:

- The target versions, patch levels, topology, endpoints, object definitions,
  primary keys, character sets, replication state, logs, validation plan, or
  rollback plan are missing.
- The answer would generate runnable `ALTER REPLICATION`, `DROP REPLICATION`,
  DDL synchronization, failback, `QUICKSTART`, `RESET`, Replication Manager
  destructive GUI steps, Log Analyzer production code, or replication SSL setup
  without exact source blocks and customer runtime evidence.
- The request depends on exact customer environment, live network state,
  installed tool version, package availability, GUI dialog output, current
  replication gap, patch-specific behavior, mixed-version compatibility, or
  unsupported behavior that has not been supplied.
