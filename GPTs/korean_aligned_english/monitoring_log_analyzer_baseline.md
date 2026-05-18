# Korean-Aligned English Baseline: Monitoring API, SNMP Agent, And Log Analyzer

- Job: `S1R-J003`
- Scope: Monitoring API Developer's Guide, SNMP Agent Guide, and Log
  Analyzer User's Manual rows across 7.1, 7.3, and `Altibase 8.1 verified
  source` scope.
- Source-pack gate: `GPTs/source_pack/source_pack_validation.md` records
  `Status: pass`, `Verdict: Pass`, no blockers, and exact source-pack block
  preservation for the selected Monitoring API, SNMP Agent, and Log Analyzer
  manuals.
- Authority rule: Korean manuals are authoritative. English manuals are
  extraction aids. For 8.1 material, preserve the established `Altibase 8.1
  verified source` boundary.
- Downstream boundary: this file is a working route for guarded first drafts.
  It does not replace exact source-pack extraction, complete API signature
  transcription, installed-header validation, live SNMP daemon validation,
  complete error-code conversion, replication-runtime checks, or customer
  environment evidence.

## Design Note

`S1R-J003` adds a dedicated monitoring and log-analyzer baseline file instead
of rewriting generated S1-J006 inventory rows. The original per-manual
inventory rows remain immutable generated evidence, while
`KAE-BLOCK-000280` through `KAE-BLOCK-000282` provide downstream-ready working
routes for Log Analyzer, Monitoring API, and SNMP Agent drafting. The routes
preserve exact command, API, property, MIB, and XLog tokens, but keep recheck
guardrails where production-ready or exhaustive coverage is not proven.

## Batch Source Coverage

| Route | Korean source IDs | English source IDs | Baseline manifest rows | Disposition |
| --- | --- | --- | --- | --- |
| Log Analyzer User's Manual | `SRC-000062`, `SRC-000126`, `SRC-000186` | `SRC-000031`, `SRC-000095`, `SRC-000156` | `KAE-BLOCK-000018`, `KAE-BLOCK-000153`, `KAE-BLOCK-000209`, plus `KAE-BLOCK-000280` | aligned baseline route |
| Monitoring API Developer's Guide | `SRC-000063`, `SRC-000127`, `SRC-000187` | `SRC-000032`, `SRC-000096`, `SRC-000157` | `KAE-BLOCK-000020`, `KAE-BLOCK-000155`, `KAE-BLOCK-000212`, plus `KAE-BLOCK-000281` | aligned baseline route |
| SNMP Agent Guide | `SRC-000071`, `SRC-000133`, `SRC-000193` | `SRC-000039`, `SRC-000102`, `SRC-000162` | `KAE-BLOCK-000021`, `KAE-BLOCK-000156`, `KAE-BLOCK-000213`, plus `KAE-BLOCK-000282` | aligned baseline route |

## KAE-BLOCK-000280: Log Analyzer Routing

- Source IDs: `SRC-000062`, `SRC-000031`, `SRC-000126`, `SRC-000095`,
  `SRC-000186`, `SRC-000156`.
- Version scope: 7.1, 7.3, and `Altibase 8.1 verified source`.
- Source block refs: `SRC-000062/BLOCK-000564`, `SRC-000031/BLOCK-000563`,
  `SRC-000126/BLOCK-000566`, `SRC-000095/BLOCK-000565`,
  `SRC-000186/BLOCK-000568`, `SRC-000156/BLOCK-000567`.
- Alignment status: baseline generated from paired Korean authority and English
  extraction aids. Exact C prototypes, structure members, sample programs,
  complete error-code tables, and runtime behavior still require source-pack
  or installed-version recheck before production use.

Baseline:

1. Route Log Analyzer work to the target-version Korean Log Analyzer User's
   Manual first, using the paired English manual only as an extraction aid.
   Preserve terms and tokens such as `XLog`, `XLog Sender`, `XLog Collector`,
   `Log Analysis API`, `XLog Queue`, `XLog Pool`, `Transaction Table`,
   `Restart SN`, `SN`, `Handshake`, `Replication`, and `Replication SYNC`.
2. Treat the XLog Sender as an Altibase replication-managed sender for log
   analysis, not as a generic change-data-capture stream. Preserve XLog Sender
   SQL tokens including `CREATE REPLICATION ... FOR ANALYSIS [PROPAGATION]`,
   `WITH {'remote_host_ip', remote_host_port_no} | UNIX_DOMAIN`,
   `FROM user_name.table_name TO user_name.table_name`, `DROP REPLICATION`,
   `ALTER REPLICATION ... START [AT SN (xlog_sender_start_sn)] | QUICKSTART`,
   `ALTER REPLICATION ... STOP`, `ADD TABLE`, `DROP TABLE`, `ADD HOST`,
   `DROP HOST`, `SET HOST`, and `FLUSH [ALL] [WAIT timeout_sec]`.
3. Preserve the documented limits before drafting setup SQL: only `SYS` can
   run the XLog Sender; the analysis unit is a table; an analyzed table must
   have a primary key; primary-key column values cannot be updated; DDL cannot
   be executed on analyzed tables; the combined total of XLog Senders and
   Replication Senders in one database cannot exceed 32; the Log Analyzer uses
   Lazy Mode; and the Replication protocol version used by Replication and the
   Log Analysis API must match. The manuals also record that Log Analyzer can
   use tables with foreign keys.
4. For connection routing, preserve TCP and `UNIX_DOMAIN` boundaries. UNIX
   domain sockets are available only when the XLog Sender and XLog Collector
   are on the same UNIX or Linux machine, and the `$ALTIBASE_HOME` value must
   match. Starting with `AT SN` requires archivelog mode and
   `REPLICATION_LOG_BUFFER_SIZE` set to `0`.
5. For client API setup, preserve required files and library labels:
   `alaAPI.h`, `alaTypes.h`, `libala_sl.x`, and `libala.x`. Route API
   environment work through `ALA_InitializeAPI`, `ALA_DestroyAPI`,
   `ALA_EnableLogging`, and `ALA_DisableLogging`; preserve basic types such as
   `ALA_BOOL`, `ALA_TRUE`, `ALA_FALSE`, `ALA_RC`, `ALA_SUCCESS`,
   `ALA_FAILURE`, and `ALA_ErrorMgr`.
6. Use this collector workflow for guarded first drafts:
   `ALA_CreateXLogCollector`, optional `ALA_AddAuthInfo` or
   `ALA_RemoveAuthInfo`, optional `ALA_SetHandshakeTimeout`,
   optional `ALA_SetReceiveXLogTimeout`, optional `ALA_SetXLogPoolSize`,
   `ALA_Handshake`, repeated `ALA_ReceiveXLog`, `ALA_GetXLog`, XLog analysis,
   `ALA_SendACK`, `ALA_FreeXLog`, status checks with
   `ALA_GetXLogCollectorStatus`, and cleanup with
   `ALA_DestroyXLogCollector`. Do not call `ALA_ReceiveXLog`,
   `ALA_GetXLog`, or `ALA_SendACK` before a successful handshake.
7. Preserve XLog type tokens exactly: `XLOG_TYPE_COMMIT`, `XLOG_TYPE_ABORT`,
   `XLOG_TYPE_INSERT`, `XLOG_TYPE_UPDATE`, `XLOG_TYPE_DELETE`,
   `XLOG_TYPE_SP_SET`, `XLOG_TYPE_SP_ABORT`, `XLOG_TYPE_LOB_CURSOR_OPEN`,
   `XLOG_TYPE_LOB_CURSOR_CLOSE`, `XLOG_TYPE_LOB_PREPARE4WRITE`,
   `XLOG_TYPE_LOB_PARTIAL_WRITE`, `XLOG_TYPE_LOB_FINISH2WRITE`,
   `XLOG_TYPE_KEEP_ALIVE`, `XLOG_TYPE_REPL_STOP`, `XLOG_TYPE_LOB_TRIM`, and
   `XLOG_TYPE_CHANGE_META`. Transaction-related XLogs end with either
   `XLOG_TYPE_COMMIT` or `XLOG_TYPE_ABORT`; `KEEP_ALIVE` checks network
   validity; `REPL_STOP` indicates normal sender shutdown; `CHANGE_META`
   requires refreshed metadata handling.
8. Route XLog inspection and conversion through the exact API names:
   `ALA_GetXLogHeader`, `ALA_GetXLogPrimaryKey`, `ALA_GetXLogColumn`,
   `ALA_GetXLogSavepoint`, `ALA_GetXLogLOB`, `ALA_GetProtocolVersion`,
   `ALA_GetReplicationInfo`, `ALA_GetTableInfo`, `ALA_GetTableInfoByName`,
   `ALA_GetColumnInfo`, `ALA_GetIndexInfo`, `ALA_IsHiddenColumn`,
   `ALA_GetInternalNumericInfo`, `ALA_GetAltibaseText`,
   `ALA_GetAltibaseSQL`, `ALA_GetODBCCValue`, and `ALA_IsNullValue`.
   Recheck the exact source before relying on complete structure members such
   as `ALA_XLogHeader`, `ALA_XLogPrimaryKey`, `ALA_XLogColumn`,
   `ALA_XLogSavepoint`, `ALA_XLogLOB`, `ALA_XLog`, `ALA_ProtocolVersion`,
   `ALA_Replication`, `ALA_Table`, `ALA_Column`, and `ALA_Index`.
9. Preserve conversion limits. `ALA_GetAltibaseText()`,
   `ALA_GetAltibaseSQL()`, and `ALA_GetODBCCValue()` cannot be used with
   `BLOB`, `CLOB`, or `GEOMETRY` values. For `NCHAR` or `NVARCHAR`
   conversion, the manuals route to `ALTIBASE_ALA_NCHARSET` on the XLog
   Collector side. Do not generate final conversion code without source and
   environment confirmation.
10. Route error handling through `ALA_ClearErrorMgr`, `ALA_GetErrorCode`,
    `ALA_GetErrorLevel`, and `ALA_GetErrorMessage`. Preserve error-level
    actions: `ALA_ERROR_FATAL` requires destroying the XLog Collector;
    `ALA_ERROR_ABORT` requires a new `ALA_Handshake`; `ALA_ERROR_INFO` requires
    error-code-specific handling. Use the Error Manager instead of interpreting
    internal `mErrorCode` values directly.
11. Route metadata and status checks to the source-backed paths:
    `SYSTEM_.SYS_REPLICATIONS_`, `SYSTEM_.SYS_REPL_HOSTS_`,
    `SYSTEM_.SYS_REPL_ITEMS_`, `V$REPEXEC`, `V$REPSENDER`,
    `V$REPSENDER_TRANSTBL`, and `V$REPGAP`. Recheck the General Reference
    before generating complete column lists or production monitoring SQL.

Safe first checks:

- Ask for target Altibase version and patch, whether the XLog Sender uses TCP
  or `UNIX_DOMAIN`, source and collector host details, `$ALTIBASE_HOME`,
  archivelog mode, `REPLICATION_LOG_BUFFER_SIZE`, XLog Sender name, analyzed
  table owner/name list, primary keys, foreign keys, expected DML volume,
  transaction ordering requirements, ACK policy, XLog Pool sizing, and whether
  ODBC conversion is required.
- Confirm the XLog Collector is waiting before starting the XLog Sender.
- Confirm analyzed tables have primary keys and no unsupported DDL or primary
  key updates are planned while analysis is active.
- Check sender status through the replication metadata and performance-view
  route before starting, stopping, flushing, or changing hosts.

Stop conditions:

- Stop if the request depends on live active logs, restart SN, runtime sender
  state, network errors, protocol version, object definitions, installed header
  files, exact compiler/linker flags, or logs that the customer has not
  supplied.
- Stop if the request asks for exhaustive C API signatures, every sample
  program, complete error-code tables, complete internal data structures, or
  production-ready replication-to-DBMS code from this baseline alone. Route to
  the exact source-pack block.
- Stop if a request asks to infer unsupported behavior from generic database
  assumptions, generic replication concepts, or Oracle-only CDC patterns.

## KAE-BLOCK-000281: Monitoring API Routing

- Source IDs: `SRC-000063`, `SRC-000032`, `SRC-000127`, `SRC-000096`,
  `SRC-000187`, `SRC-000157`.
- Version scope: 7.1, 7.3, and `Altibase 8.1 verified source`.
- Source block refs: `SRC-000063/BLOCK-000605`, `SRC-000032/BLOCK-000603`,
  `SRC-000127/BLOCK-000609`, `SRC-000096/BLOCK-000607`,
  `SRC-000187/BLOCK-000613`, `SRC-000157/BLOCK-000611`.
- Alignment status: baseline generated from paired Korean authority and English
  extraction aids. Exact function prototypes, structure members, sample
  programs, library filenames, and runtime behavior still require source-pack,
  installed-header, or installed-library recheck before production use.

Baseline:

1. Route Monitoring API work to the target-version Korean Monitoring API
   Developer's Guide first, using the paired English manual only as an
   extraction aid. The Monitoring API is for local application monitoring of
   Altibase; it connects to the Altibase server through a Unix domain socket,
   so the Monitoring API application and Altibase must run on the same server.
   It is not a substitute for generic JDBC, ODBC, or CLI database access.
2. Preserve build inputs and library names: `altibaseMonitor.h`,
   `-I$ALTIBASE_HOME/include`, `libaltibaseMonitor.a`,
   `libaltibaseMonitor_sl.so`, `libodbccli.a`, `libpthread.a`, and `libdl.a`.
   The sample build route uses `$(ALTIBASE_HOME)/install/altibase_env.mk`,
   `-L$ALTIBASE_HOME/lib`, `-laltibaseMonitor`, `-lodbccli`, `-ldl`,
   `-lpthread`, `-lcrypt`, and `-lrt`; recheck the exact source and installed
   platform before generating final build commands.
3. Preserve initialization and connection-control functions:
   `ABIInitialize`, `ABIFinalize`, `ABISetProperty`, and
   `ABICheckConnection`. Preserve `ABIPropType` values `ABI_USER`,
   `ABI_PASSWD`, and `ABI_LOGFILE`; do not rename them or silently substitute
   ordinary connection-string options.
4. Route performance-view result retrieval through the documented structures:
   `ABIVSession`, `ABIVSysstat`, `ABIVSesstat`, `ABIStatName`,
   `ABIVSystemEvent`, `ABIVSessionEvent`, `ABIEventName`,
   `ABIVSessionWait`, `ABISqlText`, `ABILockPair`, `ABIDBInfo`,
   `ABIReadCount`, `ABIRepGap`, and `ABIRepSentLogCount`. Recheck the exact
   source before using complete member lists or data widths.
5. Preserve function routes for performance views and session details:
   `ABIGetVSession`, `ABIGetVSessionBySID`, `ABIGetVSysstat`,
   `ABIGetVSesstat`, `ABIGetVSesstatBySID`, `ABIGetStatName`,
   `ABIGetVSystemEvent`, `ABIGetVSessionEvent`,
   `ABIGetVSessionEventBySID`, `ABIGetEventName`, `ABIGetVSessionWait`,
   `ABIGetVSessionWaitBySID`, `ABIGetSqlText`,
   `ABIGetLockPairBetweenSessions`, `ABIGetDBInfo`, `ABIGetReadCount`,
   `ABIGetSessionCount`, `ABIGetMaxClientCount`,
   `ABIGetLockWaitSessionCount`, `ABIGetRepGap`,
   `ABIGetRepSentLogCount`, and `ABIGetErrorMessage`.
6. Preserve memory-management boundaries. The API allocates memory for result
   structures and returns pointers through double-pointer output arguments.
   The application should declare the structure pointer, pass its address, and
   access only the returned row count. Do not directly allocate or deallocate
   the memory returned by Monitoring API functions.
7. Preserve thread-safety guardrails. The manuals state that memory internally
   allocated by Monitoring API functions or libraries is shared by Monitoring
   API functions and is not thread-safe. If multiple threads use the API,
   synchronize access with mutexes or another explicit serialization method.
8. Route detailed column semantics to the paired General Reference performance
   view rows. Examples include `V$SESSION`, `V$SYSSTAT`, `V$SESSTAT`,
   `V$SYSTEM_EVENT`, `V$SESSION_EVENT`, and `V$SESSION_WAIT`. Do not invent
   view columns or Monitoring API structure members from generic database
   assumptions.

Safe first checks:

- Ask for target Altibase version and patch, operating system, compiler,
  installed `ALTIBASE_HOME`, installed header/library paths, whether the
  monitor process runs on the same server as Altibase, required user/password
  handling, desired log file path, thread model, and the exact performance view
  or function target.
- Confirm the Altibase server is running locally and the Unix domain socket
  path is usable before interpreting connection failures.
- Confirm whether returned row counts, active-session filters, session IDs,
  and statement IDs are known before generating result-processing code.

Stop conditions:

- Stop if the request depends on installed header signatures, platform linker
  behavior, live socket state, exact performance-view columns, session state,
  SQL text visibility, replication runtime state, or logs that have not been
  supplied.
- Stop if a request asks for complete sample programs, complete structure
  member tables, production-ready monitoring code, or cross-platform build
  commands from this baseline alone. Route to the exact source-pack block and
  installed files.
- Stop if a request asks to infer JDBC, ODBC, CLI, or external monitoring
  behavior from the Monitoring API route.

## KAE-BLOCK-000282: SNMP Agent Routing

- Source IDs: `SRC-000071`, `SRC-000039`, `SRC-000133`, `SRC-000102`,
  `SRC-000193`, `SRC-000162`.
- Version scope: 7.1, 7.3, and `Altibase 8.1 verified source`.
- Source block refs: `SRC-000071/BLOCK-000606`, `SRC-000039/BLOCK-000604`,
  `SRC-000133/BLOCK-000610`, `SRC-000102/BLOCK-000608`,
  `SRC-000193/BLOCK-000614`, `SRC-000162/BLOCK-000612`.
- Alignment status: baseline generated from paired Korean authority and English
  extraction aids. Exact daemon options, full MIB definitions, security policy,
  network ACL behavior, and live SNMP output still require source-pack,
  installed-package, and environment recheck before production use.

Baseline:

1. Route SNMP work to the target-version Korean SNMP Agent Guide first, using
   the paired English manual only as an extraction aid. Preserve `ALTIBASE-MIB`
   and the IANA route `altibase(17180)` under `enterprises(1)`.
2. Preserve the Altibase SNMP model. `snmpd` is the SNMP master agent daemon;
   `altisnmpd` is the Altibase SNMP subagent daemon; `snmptrapd` is the trap
   daemon. The manuals describe synchronous request flow through SNMP manager
   to `snmpd`, `altisnmpd`, and Altibase, and asynchronous trap flow from
   Altibase through `altisnmpd`, `snmpd`, and `snmptrapd`. Preserve AgentX
   communication between `altisnmpd` and `snmpd`.
3. Preserve package and file names: `altibase-snmp-xxx.tar.gz`, `snmpget`,
   `snmpset`, `snmpwak`, `snmpwalk`, `snmpd`, `snmptrapd`, `altisnmpd`,
   `ALTIBASE-MIB.txt`, `snmpd.conf`, `altisnmpd.conf`, and `altisnmp.env`.
   Preserve environment variables `ALTISNMP`, `ALTISNMPCONF`,
   `ALTISNMPBIN`, `ALTISNMPSBIN`, `SNMP_PERSISTENT_FILE`,
   `SNMP_PERSISTENT_DIR`, `MIBDIRS`, and `MIBS=ALL`.
4. Preserve Altibase SNMP properties exactly: `SNMP_ENABLE`, `SNMP_PORT_NO`,
   `SNMP_TRAP_PORT_NO`, `SNMP_RECV_TIMEOUT`, `SNMP_SEND_TIMEOUT`,
   `SNMP_MSGLOG_FLAG`, `SNMP_ALARM_QUERY_TIMEOUT`,
   `SNMP_ALARM_FETCH_TIMEOUT`, `SNMP_ALARM_UTRANS_TIMEOUT`, and
   `SNMP_ALARM_SESSION_FAILURE_COUNT`. Recheck the General Reference before
   stating defaults, ranges, dynamic-change rules, or production values.
5. Preserve daemon command routing and option names. The packaged example uses
   `snmpd -f -L -c $ALTISNMPCONF/snmpd.conf -C -x localhost:1705
   udp:localhost:1161`, background `snmpd` with `-l`, `-s`, and `-P`,
   `snmptrapd -f -P udp:localhost:1162`, background `snmptrapd` with `-s`,
   `-o`, and `-u`, and `altisnmpd -f -L -c $ALTISNMPCONF/altisnmpd.conf -x
   localhost:1705`. Do not reuse these ports without confirming the customer's
   existing SNMP services.
6. Preserve `altisnmpd.conf` routing tokens: `altibase PORT_NO SNMP_PORT_NO`
   and `altibase_trap SNMP_TRAP_PORT_NO`. For multiple Altibase servers,
   preserve multiple `altibase` lines. For an already installed NET-SNMP
   environment, preserve `mibs +ALTIBASE-MIB` in `snmp.conf` and the default
   AgentX route `localhost:705` unless the local administrator provides a
   different route.
7. Route MIB work through the documented groups:
   `altiPropertyTable`, `altiStatus`, and `altiTrap`. Preserve object names
   such as `altiPropertyIndex`, `altiPropertyAlarmQueryTimeout`,
   `altiPropertyAlarmFetchTimeout`, `altiPropertyAlarmUtransTimeout`,
   `altiPropertyAlarmUTransTimeout`, `altiPropertyAlarmSessionFailureCount`,
   `altiStatusIndex`, `altiStatusDBName`, `altiStatusDBVersion`,
   `altiStatusRunningTime`, `altiStatusProcessID`,
   `altiStatusSessionCount`, `altiNotification`, `altiTrapAddress`,
   `altiTrapLevel`, `altiTrapCode`, `altiTrapMessage`, and
   `altiTrapMoreInfo`. Recheck the target source before finalizing object
   case, OIDs, and read/write status.
8. Preserve trap code and level routing for first-draft troubleshooting:
   `10000001` Altibase Running Status, `10000002` Altibase UnRunning Status,
   `10000003` Altibase Subagent Running Status, `10000004` Altibase Subagent
   UnRunning Status, `10000101` Session Query Timeout, `10000102` Session
   Fetch Timeout, `10000103` Session Utrans Timeout, and `10000201` Too Many
   Continuous Query Failure. Recheck the exact source before producing a full
   trap table or customer alert policy.
9. Route common SNMP failures through source-backed checks: if `altisnmpd`
   reports `Error: Failed to connect to the agentx master agent: Unknown host
   (Connection refused)`, verify that `snmpd` is running and check the
   `altisnmpd -x` address and port. For `No Such Object available on this
   agent at this OID`, check `altisnmpd` and restart it after `snmpd` restarts.
   For `notWritable`, verify read-only versus read-write objects and the
   network path. For `No Such Instance currently exists at this OID`, check the
   OID/object name and use `snmpwalk`. For `Unknown Object Identifier`, verify
   `ALTIBASE-MIB.txt`, `$MIBDIRS`, and `$MIBS`.

Safe first checks:

- Ask for target Altibase version and patch, SNMP package source, existing
  NET-SNMP version, operating system, desired SNMP manager host, community
  string policy, daemon ports, AgentX port, Altibase `PORT_NO`,
  `SNMP_PORT_NO`, `SNMP_TRAP_PORT_NO`, firewall rules, ACL rules, process
  account, log paths, pid paths, and whether packaged or preinstalled NET-SNMP
  is being used.
- Confirm `SNMP_ENABLE`, `SNMP_PORT_NO`, and `SNMP_TRAP_PORT_NO` in
  `$ALTIBASE_HOME/conf/altibase.properties` before starting the daemons.
- Confirm `snmpd`, `snmptrapd`, `altisnmpd`, and Altibase are running before
  interpreting `snmpwalk`, `snmpget`, `snmpset`, or trap output.
- Confirm `ALTIBASE-MIB.txt` is discoverable through `$MIBDIRS` and `$MIBS`
  before troubleshooting object names.

Stop conditions:

- Stop if the request depends on live daemon output, network reachability,
  firewall policy, community-string authorization, installed NET-SNMP behavior,
  exact OID case, property defaults, or alert thresholds that the customer has
  not supplied.
- Stop if a request asks for complete `ALTIBASE-MIB.txt`, full OID tables,
  production SNMP security hardening, or final monitoring policy from this
  baseline alone. Route to the exact source-pack block and installed
  environment checks.
- Stop if a request would silently expose insecure community strings, change
  read-write MIB objects, or infer behavior from generic SNMP assumptions
  without target-version Altibase source and environment evidence.
