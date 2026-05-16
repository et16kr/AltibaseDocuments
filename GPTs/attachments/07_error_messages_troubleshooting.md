# 07. Error Messages and Troubleshooting

## Applicable Versions

- 7.1: Based on Altibase 7.1 Error Message Reference.
- 7.3: Based on Altibase 7.3 Error Message Reference.
- 8.1: Based on Altibase 8.1 verified source Error Message Reference.

## Questions This File Can Answer

- What are the cause and action for covered/common Altibase error codes?
- How should a GPT answer when the user provides only `ERR-xxxxx`, an error message, or a trace log excerpt?
- Which log files, SQL checks, and commands should be requested for startup, SQL execution, connection, replication, SSL, LOB, JSON, regular expression, tablespace, and lock errors?
- Which errors are version-sensitive in 7.1, 7.3, and 8.1?
- How should an error response be formatted so the answer is consistent in any user language?

## Source Documents

- 7.1: Altibase 7.1 Error Message Reference.
- 7.3: Altibase 7.3 Error Message Reference.
- 8.1: Altibase 8.1 verified source Error Message Reference.

## Error Reference Inventory Baseline

The selected Error Message References are organized by module chapters. Use the module
family to choose a diagnostic lane, but do not infer cause, action, `SQLSTATE`, exact
version support, or severity from the prefix alone. The exact error entry and the
customer's runtime context decide the answer.

Inventory summary:

- 7.1 Error Message Reference: `2927` exact `0x...` entries across `ID`, `SM`, `MT`, `RP`, `QP`, `SD`, `ST`, `MM`, `ODBC`, `APRE`, `Utilities`, `CM`, `Database Link`, and `Log Analyzer` chapters. The Regular Expression chapter explains PCRE2 error text and routes exact-code handling back to `MT`.
- 7.3 Error Message Reference: `2899` exact `0x...` entries across `ID`, `SM`, `MT`, `RP`, `QP`, `ST`, `MM`, `ODBC`, `APRE`, `Utilities`, `CM`, `Database Link`, and `Log Analyzer` chapters. `SD Error Code` is not listed in the checked 7.3 Error Message Reference.
- Altibase 8.1 verified source: `2916` exact `0x...` entries across `ID`, `SM`, `MT`, `RP`, `QP`, `ST`, `MM`, `ODBC`, `APRE`, `Utilities`, `CM`, `Database Link`, and `Log Analyzer` chapters. `SD Error Code` is not listed in the checked Altibase 8.1 verified source.

Expanded block routing:

- Storage, backup, recovery, datafile, log, lock, and tablespace errors: use storage/recovery error blocks when present.
- SQL, DDL, data type, constraint, JSON, Temporary LOB, LOB, and regular expression errors: use SQL/data-type error blocks when present.
- Client, network, SSL/TLS, replication, utility, DB Link, Log Analyzer, APRE, and CLI/ODBC errors: use client/tool/replication error blocks when present.
- Unresolved exact-code gaps and source-drift cases: preserve the supplied code and ask for exact version and evidence before a definitive answer.

## Response Rules

- Answer explanations in the user's language.
- Keep SQL object names, function names, error codes, reference symbols, property names, commands, file paths, and environment variables literal.
- Preserve the exact error code and message the user provided. Do not translate or rewrite `ERR-31363`, `0x31363`, `qpERR_ABORT_QDB_TEMPORARY_TABLE_DDL_DISABLE`, `TEMPORARY_LOB_ENABLE`, `REGEXP_MODE`, `ALTIBASE_SSL_PORT_NO`, or similar tokens.
- If the user gives only an error code, ask for the full error line, Altibase version, SQL or command, and relevant trace log excerpt before making a final diagnosis.
- If the user gives a specific Altibase error code that does not match one of the consolidated error blocks, preserve the supplied code and message. Do not answer only that the code is absent from the attachments. Set cause/action beyond the user's evidence to `Unknown from the supplied message`, and ask for the Altibase version, full error line, SQL or command, and relevant trace log excerpt. Do not infer cause, action, `SQLSTATE`, module, or severity from the prefix or code family alone.
- Runtime messages often appear as `[ERR-31363 : Cannot execute DDL when a temporary table is in use.]`. The Error Message Reference may list the same code as `0x31363 (201571)` with a reference symbol. Keep both forms when known.
- Treat placeholders such as `<0%s>`, `<1%d>`, and `<0%lu>` as values that Altibase substitutes at runtime. Do not ask users to type placeholders literally.
- If the reference action says to contact support, first collect version, exact command, SQL text, timestamp, trace log excerpts, OS error number if present, and reproduction steps.
- Do not expose internal source labels. Use `Altibase 8.1 verified source` for 8.1 material.

## Standard Error Response Format

Use this format for every customer-facing error explanation:

```text
Error Code:
Reference Symbol:
Module / Severity:
Message:
Applies To:
Symptom:
Primary Causes:
Immediate Action:
Check SQL or Command:
Version Cautions:
Escalation:
Related Document:
```

If one field is unknown, say `Unknown from the supplied message` instead of inventing it.

Short answers may compress the fields, but preserve the same order:

```text
Symptom -> Cause -> Action -> Check SQL or Command -> Version Cautions -> Escalation
```

## Error Code Normalization

When a runtime message uses `ERR-xxxxx`, normalize it without changing the user's literal code:

```text
Runtime form:   ERR-31363
Reference form: 0x31363 (201571)
Symbol:         qpERR_ABORT_QDB_TEMPORARY_TABLE_DDL_DISABLE
Message:        Cannot execute DDL when a temporary table is in use.
```

Rules:

- `ERR-31363` usually corresponds to reference code `0x31363`.
- Keep leading zeroes in runtime codes such as `ERR-00000`.
- Do not convert a decimal value unless the reference entry explicitly provides it.
- Search by message text when a utility wraps the original server error.
- If the user supplies `SQLSTATE`, keep it in the answer, but do not infer `SQLSTATE` from an Altibase error code unless the driver reported it.

## Module and Severity Map

| Reference area | Typical prefix | Use this diagnosis lane |
| --- | --- | --- |
| ID Error Code | `idERR_*` | Infrastructure, OS calls, shared memory, semaphores, sockets, files, properties |
| SM Error Code | `smERR_*` | Storage manager, transactions, locks, log files, data files, tablespaces, backup, recovery |
| MT Error Code | `mtERR_*` | Data types, conversion, literals, date format, time zone, regular expression, JSON type support |
| RP Error Code | `rpERR_*` | Replication definition, sender, receiver, socket, handshake, sync, replication metadata |
| QP Error Code | `qpERR_*` | SQL parser, DDL, DML, metadata, objects, privileges, PSM, query execution |
| SD Error Code | `sdERR_*` | Sharding metadata, shard nodes, shard keys, shard SQL restrictions |
| ST Error Code | `stERR_*` | Spatial SQL and geometry operations |
| MM Error Code | `mmERR_*` | Main module, sessions, startup, shutdown, access mode, protocol checks |
| ODBC / CLI Error Code | `ulERR_*` | CLI, ODBC, client connection, fetch, bind, LOB, SSL client settings |
| APRE Error Code | `ulpERR_*` | Precompiler and embedded SQL |
| Utilities Error Code | `utERR_*` | `isql`, `iloader`, utilities, display, file, communication, LOB utility behavior |
| CM Error Code | `cmERR_*` | Communication module, SSL/TLS context, certificates, socket I/O |
| Database Link Error Code | `dkERR_*` | DB Link, AltiLinker, remote transaction, `dblink.conf` |
| Log Analyzer Error Code | `ulaERR_*` | Log Analyzer network and CDC-related processing |

Version note: `SD Error Code` / `sdERR_*` is confirmed in the 7.1 Error Message
Reference, but is not listed in the checked 7.3 or Altibase 8.1 verified source. If a
customer reports an `sdERR_*` or sharding error on 7.3 or 8.1, ask for the exact
product version, patch level, full error line, and installed manual/runtime evidence
before making a definitive version claim. Sharding-related errors can also appear
under other modules, so use the exact code first.

Severity handling:

| Severity | Meaning for answer |
| --- | --- |
| `FATAL` | Treat as high risk. Collect trace logs, OS error numbers, startup phase, and version. Restart or recovery guidance must be careful and state impact. |
| `ABORT` | The current operation failed. Explain the cause, corrective action, and retry conditions. |
| `RETRY` | The reference expects retry after a condition clears. Explain what condition to verify before retrying. |
| `IGNORE` | Usually informational or non-fatal. Explain when it can be ignored and when to collect logs. |

Inherited escalation default for every error block:

- Every block under `Searchable Error Blocks` inherits this `Escalation:` policy unless the block provides a narrower escalation line.
- Collect evidence before escalation: exact error code and message, Altibase version, failed SQL or command, module context, relevant dictionary query output, trace log excerpt around the timestamp, and recent corrective actions already attempted.
- Stop corrective actions and escalate when evidence conflicts with the documented cause, the same failure remains after the listed verification checks, a restart, data movement, tablespace drop, replication rebuild, certificate change, or property change would be needed, or the source action says to contact Altibase Support.

## Triage Workflow

```mermaid
flowchart TD
  A[Capture exact error line] --> B[Identify Altibase version and client or server context]
  B --> C[Normalize runtime code to reference code if possible]
  C --> D{Which module?}
  D --> E[SQL or object metadata]
  D --> F[Storage, tablespace, lock, backup, recovery]
  D --> G[Connection, utility, SSL, network]
  D --> H[Replication, DB Link, shard]
  E --> I[Run object and privilege checks]
  F --> J[Run tablespace, lock, log, and phase checks]
  G --> K[Check client settings, server phase, ports, trace logs]
  H --> L[Check replication, link, or shard metadata and runtime views]
  I --> M[Return standardized error response]
  J --> M
  K --> M
  L --> M
```

## Evidence to Request

Ask for this information when the error cannot be answered directly:

- Altibase version: `altibase -v` output, or `V$VERSION`.
- Exact command or SQL statement that failed.
- Exact error line and any preceding error lines.
- Whether the error came from server startup, `isql`, CLI/ODBC/JDBC, replication, DB Link, utility, or application code.
- Startup phase: `PROCESS`, `CONTROL`, `META`, or `SERVICE`, if the error is operational.
- Relevant trace logs around the timestamp, especially `altibase_boot.log`, `altibase_rp.log`, utility output, and the module trace log named in the error context.

Useful OS commands:

```bash
altibase -v
ls -ltr "$ALTIBASE_HOME/trc"
tail -200 "$ALTIBASE_HOME/trc/altibase_boot.log"
tail -200 "$ALTIBASE_HOME/trc/altibase_rp.log"
```

Use `altibase_rp.log` when the error prefix is `rpERR_*` or the message mentions replication sender, receiver, handshake, sync, or replication socket.

## Common Check SQL

Check version:

```sql
SELECT product_version,
       meta_version,
       protocol_version,
       repl_protocol_version
FROM V$VERSION;
```

Check properties used by troubleshooting answers:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name IN (
  'PORT_NO',
  'REPLICATION_PORT_NO',
  'REPLICATION_RECEIVE_TIMEOUT',
  'DDL_LOCK_TIMEOUT',
  'USER_LOCK_REQUEST_TIMEOUT',
  'REPLICATION_LOCK_TIMEOUT',
  'REPLICATION_SYNC_LOCK_TIMEOUT',
  'QUERY_TIMEOUT',
  'REGEXP_MODE',
  'TEMPORARY_LOB_ENABLE',
  'MEMORY_TEMPLOB_MAX_ALLOC_SIZE',
  'MEMORY_TEMPLOB_PIECE_SIZE',
  'MEM_MAX_DB_SIZE',
  'VOLATILE_MAX_DB_SIZE',
  'TABLESPACE_LOCK_ENABLE'
)
ORDER BY name;
```

Check object existence:

```sql
SELECT u.user_name,
       t.table_id,
       t.table_name,
       t.table_type,
       t.tbs_name,
       t.is_partitioned,
       t.temporary,
       t.access
FROM SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_USERS_ u
WHERE t.user_id = u.user_id
  AND u.user_name = '<OWNER_NAME>'
  AND t.table_name = '<OBJECT_NAME>';
```

Check columns:

```sql
SELECT c.column_order,
       c.column_name,
       c.data_type,
       c.precision,
       c.scale,
       c.is_nullable,
       c.store_type
FROM SYSTEM_.SYS_COLUMNS_ c,
     SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_USERS_ u
WHERE c.user_id = t.user_id
  AND c.table_id = t.table_id
  AND t.user_id = u.user_id
  AND u.user_name = '<OWNER_NAME>'
  AND t.table_name = '<TABLE_NAME>'
ORDER BY c.column_order;
```

Check constraints:

```sql
SELECT cs.constraint_name,
       cs.constraint_type,
       cs.index_id,
       cs.column_cnt,
       cs.referenced_table_id,
       cs.delete_rule,
       cs.check_condition,
       cs.validated
FROM SYSTEM_.SYS_CONSTRAINTS_ cs,
     SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_USERS_ u
WHERE cs.user_id = t.user_id
  AND cs.table_id = t.table_id
  AND t.user_id = u.user_id
  AND u.user_name = '<OWNER_NAME>'
  AND t.table_name = '<TABLE_NAME>'
ORDER BY cs.constraint_name;
```

Check tablespaces and data files:

```sql
SELECT id,
       name,
       type,
       state,
       datafile_count,
       total_page_count,
       allocated_page_count,
       page_size
FROM V$TABLESPACES
ORDER BY id;

SELECT id,
       name,
       spaceid,
       currsize,
       autoextend,
       opened,
       modified,
       state
FROM V$DATAFILES
ORDER BY spaceid, id;
```

Check locks and long-running statements:

```sql
SELECT *
FROM V$LOCK_WAIT;

SELECT session_id,
       id,
       execute_flag,
       query_start_time,
       query
FROM V$STATEMENT
WHERE execute_flag = 1
ORDER BY query_start_time;
```

Check replication:

```sql
SELECT rep_name,
       status,
       sender_ip,
       sender_port,
       peer_ip,
       peer_port,
       net_error_flag
FROM V$REPSENDER
ORDER BY rep_name;

SELECT rep_name,
       my_ip,
       my_port,
       peer_ip,
       peer_port,
       apply_xsn,
       insert_failure_count,
       update_failure_count,
       delete_failure_count
FROM V$REPRECEIVER
ORDER BY rep_name;

SELECT rep_name,
       rep_gap,
       rep_gap_size
FROM V$REPGAP
ORDER BY rep_name;
```

Check whether version-sensitive views exist before using them:

```sql
SELECT name, columncount
FROM V$TABLE
WHERE name IN ('V$TEMPORARY_LOBS', 'V$MEM_STABLE', 'V$LOCK_TABLE_STATS')
ORDER BY name;
```

## Searchable Error Blocks

### Error Block: Startup Connected to Idle Instance

Error Code: `0x910FB (594171)`; runtime messages can also show `[ERR-00000 : Connected to idle instance]`.

Reference Symbol: `utERR_ABORT_Connected_Idle_Instance_Error`.

Module / Severity: Utilities / `ABORT` in the reference, but the message itself is a notification.

Message: `Connected to idle instance`.

Applies To: `isql -sysdba` connections before the server reaches service phase.

Symptom: The user connects as `SYSDBA` and sees that the instance is idle.

Primary Causes: No error occurred. The utility connected to an idle Altibase instance.

Immediate Action: Start the database to the required phase, or continue with startup, recovery, or creation work if idle state is expected.

Check SQL or Command:

```sql
STARTUP PROCESS;
STARTUP CONTROL;
STARTUP META;
STARTUP SERVICE;
```

Version Cautions: Applies across 7.1, 7.3, and 8.1.

Related Document: Administration and Operations.

### Error Block: Communication Failure

Error Code: `ERR-91015` / `0x91015 (593941)`.

Reference Symbol: `utERR_ABORT_Comm_Failure_Error`.

Module / Severity: Utilities / `ABORT`.

Message: `Communication failure.`

Applies To: `isql`, utilities, client/server communication.

Symptom: The client loses communication with the DBMS server.

Primary Causes: The network connection was closed, the server is not running, the server is in the wrong phase, a port is wrong, or the client was disconnected.

Immediate Action: Check server status and startup phase. Verify host, port, listener availability, and `altibase_boot.log`.

Check SQL or Command:

```bash
ps -ef | grep altibase
tail -200 "$ALTIBASE_HOME/trc/altibase_boot.log"
```

```sql
SELECT product_version FROM V$VERSION;
```

Version Cautions: Applies across 7.1, 7.3, and 8.1. For SSL connections, also check the SSL-specific blocks below.

Related Document: Getting Started and Installation; Administration and Operations.

### Error Block: INET Socket Bind Failure

Error Code: `0x0001F (31)`.

Reference Symbol: `idERR_FATAL_idc_SVC_INET_BIND_ERROR`.

Module / Severity: ID / `FATAL`.

Message: `Unable to bind the INET socket.(<0%d>)`.

Applies To: Server startup and listener binding.

Symptom: Altibase cannot bind the configured TCP listener port.

Primary Causes: The port is already in use by another process, not yet released, or the configured port is wrong.

Immediate Action: Find the process using the port, stop it if appropriate, or change the Altibase port property.

Check SQL or Command:

```bash
netstat -an | grep '<PORT_NO>'
lsof -i :<PORT_NO>
tail -200 "$ALTIBASE_HOME/trc/altibase_boot.log"
```

Version Cautions: Applies across 7.1, 7.3, and 8.1. On systems without `lsof`, use the OS-native socket inspection command.

Related Document: Getting Started and Installation; Administration and Operations.

### Error Block: Insufficient Memory for Query Processor

Error Code: `0x311D6 (201174)`.

Reference Symbol: `qpERR_ABORT_MEMORY_ALLOCATION`.

Module / Severity: QP / `ABORT`.

Message: `Insufficient memory for Query Processor`.

Applies To: SQL parsing, optimization, execution, PSM, and memory-heavy statements.

Symptom: A SQL statement fails because the query processor cannot allocate enough memory.

Primary Causes: System memory pressure, too many concurrent memory-heavy statements, or memory-related properties that are too small for the workload.

Immediate Action: Check system memory, reduce concurrent workload, simplify the query if possible, and review memory properties.

Check SQL or Command:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name LIKE '%MEMORY%'
   OR name LIKE '%MEM%';
```

Version Cautions: Applies across 7.1, 7.3, and 8.1. Do not recommend a property change without the exact version and workload context.

Related Document: Performance Tuning and Monitoring; Data Types and Properties.

### Error Block: Deadlock Detected

Error Code: `0x11041 (69697)`.

Reference Symbol: `smERR_ABORT_Aborted`.

Module / Severity: SM / `ABORT`.

Message: `A deadlock situation has been detected.`

Applies To: Concurrent transactions.

Symptom: One transaction is selected as the deadlock victim and rolled back.

Primary Causes: Two or more transactions lock resources in conflicting order.

Immediate Action: Re-execute the rolled-back transaction. For recurring cases, standardize update order and reduce transaction duration.

Check SQL or Command:

```sql
SELECT *
FROM V$LOCK_WAIT;

SELECT session_id,
       id AS stmt_id,
       tx_id,
       state,
       lock_item_type,
       table_oid,
       lock_desc,
       lock_cnt,
       is_grant,
       query
FROM V$LOCK_STATEMENT
ORDER BY is_grant, session_id, id;
```

Version Cautions: Applies across 7.1, 7.3, and 8.1.

Related Document: Administration and Operations; Performance Tuning and Monitoring.

### Error Block: Lock Timeout

Error Code: `0x11075 (69749)`.

Reference Symbol: `smERR_ABORT_smcExceedLockTimeWait`.

Module / Severity: SM / `ABORT`.

Message: `The transaction has exceeded the lock timeout specified by the user.`

Applies To: SQL waiting for row, table, or tablespace locks.

Symptom: A transaction cannot acquire a lock before timeout.

Primary Causes: A long-running transaction holds the required lock. For DDL, `DDL_LOCK_TIMEOUT` may be too short; for user-lock requests, check `USER_LOCK_REQUEST_TIMEOUT`; for replication flows, check `REPLICATION_LOCK_TIMEOUT` or `REPLICATION_SYNC_LOCK_TIMEOUT`. For statement-level row or table locking, the relevant SQL may use `WAIT n` or `NOWAIT` with `LOCK TABLE` or `SELECT ... FOR UPDATE`.

Immediate Action: Identify the blocking transaction. Increase the context-specific timeout property or adjust statement-level `WAIT n`/`NOWAIT` behavior only when it is operationally acceptable.

Check SQL or Command:

```sql
SELECT *
FROM V$LOCK_WAIT;

SELECT name, value1
FROM V$PROPERTY
WHERE name IN (
  'DDL_LOCK_TIMEOUT',
  'USER_LOCK_REQUEST_TIMEOUT',
  'REPLICATION_LOCK_TIMEOUT',
  'REPLICATION_SYNC_LOCK_TIMEOUT'
)
ORDER BY name;
```

Version Cautions: Applies across 7.1, 7.3, and 8.1.

Related Document: Administration and Operations; Data Dictionary and Performance Views.

### Error Block: Tablespace Does Not Have Enough Free Space

Error Code: `0x11123 (69923)`.

Reference Symbol: `smERR_ABORT_NOT_ENOUGH_SPACE`.

Module / Severity: SM / `ABORT`.

Message: `The tablespace does not have enough free space ( TBS Name :<0%s> ).`

Applies To: DML, index creation, DDL, and allocation in disk or memory tablespaces.

Symptom: A statement cannot allocate space in the target tablespace.

Primary Causes: The tablespace is full, no data file can extend, `AUTOEXTEND` is off, `MAXSIZE` is reached, or memory tablespace limits are reached.

Immediate Action: Add a data file, enable or adjust autoextend where appropriate, free space, or increase the relevant maximum size property after impact review.

Check SQL or Command:

```sql
SELECT id, name, type, state, total_page_count, allocated_page_count, page_size
FROM V$TABLESPACES
ORDER BY id;

SELECT name, spaceid, currsize, autoextend, state
FROM V$DATAFILES
ORDER BY spaceid, name;
```

Version Cautions: Memory, volatile, disk, undo, and temporary tablespaces have different remedies. Ask for tablespace type before giving DDL.

Related Document: Administration and Operations; SQL DDL Generation.

### Error Block: Tablespace Autoextend Is Off

Error Code: `0x110EF (69871)`.

Reference Symbol: `smERR_ABORT_UNABLE_TO_EXTEND_CHUNK_WHEN_AUTO_EXTEND_OFF`.

Module / Severity: SM / `ABORT`.

Message: `Unable to extend the tablespace(<0%s>) when AUTOEXTEND mode is OFF`.

Applies To: Tablespace allocation.

Symptom: The tablespace reaches its allocated size and cannot extend.

Primary Causes: `AUTOEXTEND` is disabled for the relevant data file or tablespace.

Immediate Action: Use documented `ALTER TABLESPACE ... AUTOEXTEND ON` syntax for the tablespace type, add a data file, or free space.

Check SQL or Command:

```sql
SELECT name, spaceid, currsize, autoextend, state
FROM V$DATAFILES
ORDER BY spaceid, name;
```

Version Cautions: Confirm disk versus memory or volatile tablespace before generating the exact DDL.

Related Document: Administration and Operations; SQL DDL Generation.

### Error Block: Datafile and File-System Storage Errors

Error Codes: listed individually in the exact code map below.

Module / Severity: `ID` or `SM` / mostly `ABORT`; treat `smERR_FATAL_*` rows as high-risk storage failures.

Exact code map:

| Reference code | Reference symbol | Source message or action focus |
| --- | --- | --- |
| `0x01058 (4184)` | `idERR_ABORT_DISK_SPACE_EXHAUSTED` | Failed to create, extend, or sync a file; increase disk space or quota for the log file, memory DB file, or disk tablespace datafile. |
| `0x01059 (4185)` | `idERR_ABORT_EXCEED_FILE_SIZE_LIMIT` | Failed to increase file size; check the operating-system file size limit. |
| `0x0105A (4186)` | `idERR_ABORT_EXCEED_OPEN_FILE_LIMIT` | Failed to create a file because open-file limits were exceeded; close unused files or change system limits. |
| `0x0108B (4235)` | `idERR_ABORT_CannotShrinkFile` | Data file size cannot be shrunk; choose a valid datafile size. |
| `0x010EB (4331)` | `idERR_ABORT_NOT_SUPPORT_FALLOCATE` | Filesystem or kernel does not support the operation; source action is to set `LOG_CREATE_METHOD` to `0` and restart. |
| `0x010EC (4332)` | `idERR_ABORT_Sysfallocate` | `fallocate()` failed on the file; source action is to set `LOG_CREATE_METHOD` to `0` and restart. |
| `0x1101F (69663)` | `smERR_ABORT_InvalidAutoExtFileSize` | Datafile `MAXSIZE` is less than current size; set `MAXSIZE` correctly. |
| `0x11020 (69664)` | `smERR_ABORT_InitExceedMaxFileSize` | Datafile `INITSIZE` exceeds maximum file size; set `INITSIZE` correctly. |
| `0x11022 (69666)` | `smERR_ABORT_MaxExceedMaxFileSize` | Datafile `MAXSIZE` exceeds maximum file size; set `MAXSIZE` correctly. |
| `0x11023 (69667)` | `smERR_ABORT_InvalidFilePathABS` | Datafile path is not absolute; check `ALTIBASE_HOME` and use an absolute path. |
| `0x11024 (69668)` | `smERR_ABORT_InvalidFilePathKeyWord` | Datafile path contains reserved keywords; choose a supported path. |
| `0x11025 (69669)` | `smERR_ABORT_AlreadyExistFile` | Datafile already exists; use documented `REUSE` only when safe, or remove/choose another file. |
| `0x11027 (69671)` | `smERR_ABORT_NotExistFile` | Datafile does not exist; verify the path and file. |
| `0x11028 (69672)` | `smERR_ABORT_NoReadPermFile` | Path lacks read permission; fix filesystem permissions for the Altibase OS account. |
| `0x11029 (69673)` | `smERR_ABORT_NoWritePermFile` | Path lacks write permission; fix filesystem permissions for the Altibase OS account. |
| `0x11030 (69680)` | `smERR_ABORT_InvalidExtendFileSize` | Requested extension is larger than maximum file size; resize within the file maximum. |
| `0x11034 (69684)` | `smERR_ABORT_NotFoundDataFileNode` | Datafile node was not found; verify the datafile exists in metadata and on disk. |
| `0x1108E (69774)` | `smERR_ABORT_NotFoundDataFileNodeByID` | Datafile node ID was not found; check the datafile and tablespace metadata. |
| `0x11099 (69785)` | `smERR_ABORT_UseFileInOtherTBS` | Destination file is already in use by another tablespace; choose another destination. |
| `0x110AF (69807)` | `smERR_ABORT_OSFileSizeLimit_ERROR` | OS maximum file size is smaller than the requested database file size; increase the OS limit. |
| `0x11105 (69893)` | `smERR_ABORT_InvalidExtendFileSizeOSLimit` | Requested datafile extension exceeds the OS file limit; choose a smaller size or raise the OS limit. |
| `0x11121 (69921)` | `smERR_ABORT_CANNOT_ADD_DataFile` | Datafile count limit was reached; do not keep adding files without redesigning the tablespace. |
| `0x11122 (69922)` | `smERR_ABORT_CANT_SHRINK_BELOW_HWM` | Requested shrink size is below the used file size or HWM; choose a larger target or move/free data first. |
| `0x11124 (69924)` | `smERR_ABORT_FILE_IS_TOO_SMALL` | Initial file size cannot hold one extent; retry with a larger size. |
| `0x11128 (69928)` | `smERR_ABORT_SHRINK_SIZE_IS_TOO_SMALL` | Requested datafile size is below the minimum file size; increase the target size. |
| `0x11129 (69929)` | `smERR_ABORT_TOO_MANY_DATA_FILE` | Tablespace has too many datafiles; reduce the number to the source limit before creation. |
| `0x11137 (69943)` | `smERR_ABORT_UseFileInTheTBS` | File name is already in use by the named tablespace; choose another destination. |
| `0x1113B (69947)` | `smERR_ABORT_Datafile_Header_Read_Failure` | Datafile header could not be read; check the DB file, path, permission, and media. |
| `0x1113C (69948)` | `smERR_ABORT_Datafile_Header_Write_Failure` | Datafile header could not be written; check the DB file, filesystem, and permission. |
| `0x1113D (69949)` | `smERR_ABORT_NotFoundDataFileByPath` | Datafile was not found by path; check the file location. |
| `0x11150 (69968)` | `smERR_ABORT_InitSizeExceedMaxSize` | `INITSIZE` exceeds `MAXSIZE`; correct the datafile size clauses. |
| `0x11151 (69969)` | `smERR_ABORT_InitSizePropExceedMaxSizeProp` | Initial-size property exceeds max-size property; correct the related datafile size properties. |
| `0x11152 (69970)` | `smERR_ABORT_MaxSizePropExceedOSLimit` | Max-size property exceeds the OS file size limit; lower the property or raise OS limit. |
| `0x11153 (69971)` | `smERR_ABORT_InitSizeExceedOSLimit` | `INITSIZE` exceeds the OS file size limit; lower initial size or raise OS limit. |
| `0x11154 (69972)` | `smERR_ABORT_MaxSizeExceedOSLimit` | `MAXSIZE` exceeds the OS file size limit; lower max size or raise OS limit. |
| `0x11155 (69973)` | `smERR_ABORT_InvalidFileSizeOnLogAnchor` | Log anchor stores invalid datafile size information; collect trace logs before repair. |
| `0x11156 (69974)` | `smERR_ABORT_InvalidExtendFileSizeMaxSize` | Requested extension exceeds datafile `MAXSIZE`; choose a valid size. |
| `0x11163 (69987)` | `smERR_ABORT_TooLongFilePath` | Full file path and name are too long; choose a shorter path or file name. |
| `0x11164 (69988)` | `smERR_ABORT_AlreadyExistDBFiles` | Database files already exist; confirm `destroydb` history before recreating a database. |
| `0x111AD (70061)` | `smERR_ABORT_InvalidDatafileHeader` | Datafile header metadata does not match control/log-anchor expectations; verify the datafile and backup source. |
| `0x111AE (70062)` | `smERR_ABORT_InvalidDataFileCreateLSN` | Datafile create LSN is newer than restart redo LSN; verify that the datafile was backed up correctly. |

Applies To: datafile creation, resize, shrink, rename, backup restore, `CREATE DATABASE`, online file extension, and filesystem-backed log/datafile operations.

Symptom: Altibase cannot create, open, extend, shrink, read, write, or validate a datafile or required storage file.

Primary Causes: full filesystem, OS quota or `ulimit`, open-file limit, unsupported `fallocate`, invalid datafile size clause, invalid file path, missing file, permission error, duplicate file, file already mapped to another tablespace, invalid file header, or backup/datafile mismatch.

Immediate Action: Do not overwrite files blindly. Identify the exact file path, tablespace, operation, and startup phase; check OS free space, permissions, file limits, and `V$DATAFILES`; then apply the narrow source action for the exact code.

Check SQL or Command:

```bash
df -h '<FILESYSTEM>'
ulimit -a
ls -l '<DATAFILE_OR_DIRECTORY>'
tail -200 "$ALTIBASE_HOME/trc/altibase_boot.log"
```

```sql
SELECT d.id,
       d.name,
       d.spaceid,
       t.name AS tablespace_name,
       d.currsize,
       d.autoextend,
       d.opened,
       d.modified,
       d.state
FROM V$DATAFILES d,
     V$TABLESPACES t
WHERE d.spaceid = t.id
ORDER BY d.spaceid, d.id;
```

Required Customer Input: exact Altibase version and patch level, full error line, failed SQL or command, datafile path, tablespace name, OS error number when present, `V$DATAFILES` output, and trace log excerpt.

Version Cautions: The listed reference codes are present in the checked Korean 7.1, 7.3, and Altibase 8.1 verified source Error Message References. Exact file-size limits still depend on OS, filesystem, direct I/O, and configured properties.

Escalation: Escalate before replacing, deleting, or reusing datafiles when header, LSN, log-anchor, or backup compatibility errors appear, or when the source action says to contact Altibase Support.

Related Document: Administration and Operations; SQL DDL Generation; Data Dictionary and Performance Views.

### Error Block: Backup, Recovery, Log, and Resetlogs Errors

Error Codes: listed individually in the exact code map below.

Module / Severity: `SM` / `FATAL`, `ABORT`, or recovery-stop condition depending on the exact entry. Treat restart-recovery, media-recovery, log-consistency, and page-corruption entries as production-risk events.

Exact code map:

| Reference code | Reference symbol | Source message or action focus |
| --- | --- | --- |
| `0x1001C (65564)` | `smERR_FATAL_PageCorrupted` | Page is corrupt; recover the tablespace that contains the corrupt page using backup and recovery utilities. |
| `0x10043 (65603)` | `smERR_FATAL_WrongLogFileSize` | Log file size is wrong; check the filesystem. |
| `0x1008D (65677)` | `smERR_FATAL_NotFoundDataFile` | Datafile containing a page does not exist; collect trace logs and support evidence. |
| `0x100BA (65722)` | `smERR_FATAL_MISMATCHED_FILENO_IN_LOGFILE` | Log file number does not match its name; check whether the logfile was renamed and restore the original name. |
| `0x1013A (65850)` | `smERR_FATAL_ErrNeedMoreLog` | Insufficient or invalid logfiles at the specified path; check required logfiles. |
| `0x11018 (69656)` | `smERR_ABORT_BACKUP_DISK_INVALID` | Backup datafile version is incompatible with the storage manager; use compatible storage manager or import/export. |
| `0x11033 (69683)` | `smERR_ABORT_forbiddenOpWhileBackup` | Operation cannot run while a tablespace backup is in progress; wait for backup completion. |
| `0x11039 (69689)` | `smERR_ABORT_InvalidLogAnchorFile` | Log anchor file is missing or invalid; check `LOGANCHOR_DIR`. |
| `0x1103E (69694)` | `smERR_ABORT_MediaRecoDataFile` | Media-recovery datafile action is allowed only in `CONTROL`; restart to `CONTROL`. |
| `0x11074 (69748)` | `smERR_ABORT_InvalidBackupFile` | Invalid table backup file; check database version and backup file. |
| `0x11079 (69753)` | `smERR_ABORT_BackupWrite` | Backup write failed because disk is full; provide additional disk space. |
| `0x1108F (69775)` | `smERR_ABORT_CanStartARCH` | Archive thread cannot start in `NOARCHIVE` mode; switch to `ARCHIVELOG` in `CONTROL`. |
| `0x11090 (69776)` | `smERR_ABORT_BackupDatafile` | Failed to back up a memory region or disk tablespace datafile; check disk and backup destination. |
| `0x11091 (69777)` | `smERR_ABORT_DontNeedBackupTempTBS` | Temporary tablespace backup is not required; do not back up `TEMP` tablespace online. |
| `0x11094 (69780)` | `smERR_ABORT_ErrArchiveLogMode` | Operation impossible in `NOARCHIVE` mode; media/restart recovery that needs logs requires `ARCHIVELOG`. |
| `0x11095 (69781)` | `smERR_ABORT_NeedMediaRecovery` | Start in `CONTROL` and execute complete media recovery. |
| `0x11098 (69784)` | `smERR_ABORT_BackupLogMode` | Operation cannot execute in `NOARCHIVELOG`; switch to `ARCHIVELOG` when source-backed and planned. |
| `0x110A1 (69793)` | `smERR_ABORT_InvalidFileHdr` | Invalid datafile header; copy a valid datafile to `MEM_DB_DIR`. |
| `0x110A2 (69794)` | `smERR_ABORT_NeedResetLogs` | Incomplete media recovery requires `RESETLOGS`; start `META RESETLOGS`. |
| `0x110A4 (69796)` | `smERR_ABORT_BACKUP_GOING` | Backup is in progress; wait for current backup before switching logfiles. |
| `0x110A5 (69797)` | `smERR_ABORT_NotBeginBackup` | Tablespace backup is not in progress; run `ALTER TABLESPACE tablespace_name BEGIN BACKUP` before manual backup steps. |
| `0x110A6 (69798)` | `smERR_ABORT_NoActiveBeginBackup` | No active backup process; begin backup before the matching backup operation. |
| `0x110A9 (69801)` | `smERR_ABORT_AlreadyBeginBackup` | Tablespace is already in `BEGIN BACKUP`; complete or end the previous backup. |
| `0x110B7 (69815)` | `smERR_ABORT_InvalidUseResetLog` | `RESETLOGS` is not needed; do not run it unnecessarily. |
| `0x110BC (69820)` | `smERR_ABORT_WaitLogFileOpen` | Unable to open log file; collect trace error number and log path. |
| `0x110C1 (69825)` | `smERR_ABORT_NotFoundDataFile` | Datafile containing a page does not exist; verify the file and restore/recover if needed. |
| `0x110D7 (69847)` | `smERR_ABORT_INVALID_STARTUP_PHASE_NOT_CONTROL` | Operation is allowed only in `CONTROL`; restart to `CONTROL` and retry. |
| `0x110ED (69869)` | `smERR_ABORT_ERROR_MEDIA_RECOVERY_TYPE` | Incomplete media recovery must run in `CONTROL`, or restart recovery is appropriate; restart normally if recovery is complete or unnecessary. |
| `0x110F9 (69881)` | `smERR_ABORT_MEDIA_RECOVERY_IS_NOT_SUPPORT_SHARED_MEMORY` | Media recovery is not supported for shared memory version; verify `SHM_DB_KEY=0`. |
| `0x11101 (69889)` | `smERR_ABORT_UNABLE_TO_BACKUP_FOR_VOLATILE_TABLESPACE` | Volatile tablespace cannot be backed up; backup is unnecessary for volatile data. |
| `0x11108 (69896)` | `smERR_ABORT_LogFileSizeNotAlignedToDirectIOPageSize` | Logfile size is not aligned to `DIRECT_IO_PAGE_SIZE`; correct logfile sizing. |
| `0x1111A (69914)` | `smERR_ABORT_Invalid_DataFile_Create_LSN` | Datafile create LSN is newer than restart redo LSN; verify the backup was taken correctly. |
| `0x1111F (69919)` | `smERR_ABORT_PageCorrupted` | Page is corrupt; recover the containing tablespace with backup and recovery utilities. |
| `0x11135 (69941)` | `smERR_ABORT_AlreadyExistLogFile` | Log file already exists; confirm `destroydb` history before database recreation. |
| `0x11136 (69942)` | `smERR_ABORT_AlreadyExistLogAnchorFile` | Log anchor file already exists; confirm `destroydb` history before database recreation. |
| `0x11140 (69952)` | `smERR_ABORT_LogSizeExceedLogFileSize` | Log record exceeds logfile size; change property to a suitable value and recreate the database. |
| `0x11147 (69959)` | `smERR_ABORT_INVALID_LOGFILE` | Invalid logfile; check the logfile. |
| `0x1114E (69966)` | `smERR_ABORT_NOT_FOUND_LOGFILE` | No logfiles found in the specified directory; check the directory. |
| `0x1114F (69967)` | `smERR_ABORT_EXIST_ACTIVE_TRANS_IN_RECOV` | Recovery failed because active transactions exist; end active transactions during `CONTROL`. |
| `0x11168 (69992)` | `smERR_ABORT_LOG_FILE_MISSING` | Non-continuous log file numbers; collect trace logs before attempting recovery. |
| `0x11169 (69993)` | `smERR_ABORT_FAILURE_DURABILITY_AT_STARTUP` | Restart recovery aborted to protect durability; collect trace logs and required logfiles. |
| `0x1116A (69994)` | `smERR_ABORT_FAILURE_DRDB_WAL_AT_STARTUP` | Restart recovery aborted due to WAL failure for disk objects; collect missing-log evidence. |
| `0x1116B (69995)` | `smERR_ABORT_FAILURE_MRDB_WAL_AT_STARTUP` | Restart recovery aborted due to WAL failure for memory objects; collect missing-log evidence. |
| `0x1116C (69996)` | `smERR_ABORT_INCONSISTENT_DB` | Access blocked to avoid worsening inconsistency; stop DML and collect trace evidence. |
| `0x1116D (69997)` | `smERR_ABORT_INCONSISTENT_PAGE` | Page is inconsistent; collect trace evidence and plan recovery/escalation. |
| `0x1116E (69998)` | `smERR_ABORT_ERR_INCONSISTENT_DB_AND_LOG_BUFFER_TYPE` | Emergency startup blocked by `LOG_BUFFER_TYPE`; source action is `LOG_BUFFER_TYPE=1`. |
| `0x1116F (69999)` | `smERR_ABORT_LOGFILE_TOO_BIG_WITH_DIRECT_IO` | Logfile exceeds direct I/O limitation; reduce logfile size or set `LOG_IO_TYPE=0`. |
| `0x11173 (70003)` | `smERR_ABORT_ErrUntilTag` | Cannot recover at the specified backup tag; restore using the correct tag. |
| `0x11174 (70004)` | `smERR_ABORT_InvalidBackupInfoFile` | `backupInfo` file is invalid; restore it from a recent backup. |
| `0x11175 (70005)` | `smERR_ABORT_InvalidRestoreTime` | No backup predates the requested restore time; restore to a more recent point. |
| `0x1119B (70043)` | `smERR_ABORT_TablespaceDoesNotExist` | Tablespace ID in create-datafile redo does not exist; restore with a valid backup file. |
| `0x111AC (70060)` | `smERR_ABORT_LogFileSizeIsZero` | OS returned log file size zero; check and remove zero-sized log file only under a validated recovery plan. |
| `0x111B0 (70064)` | `smERR_ABORT_NotFoundLog` | Cannot find the log record needed in the logfile; check required logfiles. |
| `0x111B1 (70065)` | `smERR_ABORT_InvalidLog` | Invalid log at file/offset; check the logfile. |
| `0x111B5 (70069)` | `smERR_ABORT_ERR_LOG_CONSISTENCY` | Incomplete media recovery aborted due to log consistency failure; copy valid logs or move unneeded logs out of recovery path. |
| `0x111C1 (70081)` | `smERR_ABORT_WrongLogFileSize` | Log file size changed abnormally; restore a backed-up logfile if available, otherwise escalate. |

Applies To: online backup, manual `BEGIN BACKUP`/`END BACKUP`, archive-log operation, restart recovery, media recovery, incomplete recovery, `RESETLOGS`, log anchor validation, and recovery after missing or corrupt data/log files.

Symptom: Startup, backup, restore, or recovery stops because required datafiles, logfiles, log anchors, backup files, archive mode, backup state, or recovery target do not match the requested operation.

Primary Causes: `NOARCHIVELOG` mode for an online backup or media-recovery operation, backup already active, missing `BEGIN BACKUP`, invalid backup file, incompatible datafile version, missing or renamed logfile, missing log record, invalid log anchor, corrupt/inconsistent page, active transaction during recovery, invalid `RESETLOGS` timing, or inconsistent recovery target.

Immediate Action: Preserve files before changing anything. Identify complete versus incomplete recovery, confirm `ARCHIVELOG` mode, required logs, backup source, startup phase, and affected tablespace/datafile. Run recovery commands only from the documented startup phase and do not run `RESETLOGS` unless incomplete recovery requires it.

Check SQL or Command:

```bash
tail -200 "$ALTIBASE_HOME/trc/altibase_boot.log"
ls -l "$ALTIBASE_HOME/logs"
ls -l '<BACKUP_DIRECTORY>'
```

```sql
SELECT server_status,
       archivelog_mode,
       begin_chkpt_file_no,
       begin_chkpt_file_offset,
       end_chkpt_file_no,
       end_chkpt_file_offset,
       oldest_logfile_no,
       oldest_logfile_offset
FROM V$LOG;

SELECT lfg_id,
       archive_mode,
       archive_dest,
       nextlogfile_to_arch,
       oldest_active_logfile,
       current_logfile
FROM V$ARCHIVE
ORDER BY lfg_id;

SELECT backup_type,
       backup_tag,
       begin_backup_time,
       end_backup_time,
       backup_file
FROM V$BACKUP_INFO
ORDER BY begin_backup_time, backup_file;
```

Required Customer Input: exact version and patch level, startup phase, database mode, recovery target, full error line, backup manifest, affected datafile/logfile/log anchor paths, archive destination contents, and trace log excerpt.

Version Cautions: The listed reference codes are present in the checked Korean 7.1, 7.3, and Altibase 8.1 verified source Error Message References. Recovery details still depend on exact patch, backup type, log availability, and whether the operation is complete or incomplete recovery.

Escalation: Stop and escalate before deleting logfiles, replacing log anchors, forcing `RESETLOGS`, discarding a tablespace, or continuing after durability/WAL/inconsistent-page errors without a validated recovery plan.

Related Document: Administration and Operations; SQL DDL Generation; Data Dictionary and Performance Views.

### Error Block: Checkpoint Path, Incremental Backup, and Multiplex Directory Errors

Error Codes: listed individually in the exact code map below.

Module / Severity: `SM` / `ABORT`.

Exact code map:

| Reference code | Reference symbol | Source message or action focus |
| --- | --- | --- |
| `0x110D8 (69848)` | `smERR_ABORT_CPATH_NOT_EXIST` | Checkpoint path does not exist; verify path existence. |
| `0x110D9 (69849)` | `smERR_ABORT_CPATH_NO_READ_PERMISSION` | Checkpoint path lacks read permission; fix path permission. |
| `0x110DA (69850)` | `smERR_ABORT_CPATH_NO_WRITE_PERMISSION` | Checkpoint path lacks write permission; fix path permission. |
| `0x110DB (69851)` | `smERR_ABORT_CPATH_NO_EXEC_PERMISSION` | Checkpoint path lacks execute permission; fix path permission. |
| `0x110DC (69852)` | `smERR_ABORT_CPATH_NOT_A_DIRECTORY` | Checkpoint path is not a directory; choose a directory. |
| `0x110DD (69853)` | `smERR_ABORT_CPATH_NODE_NOT_EXIST` | Checkpoint path node does not exist; verify path metadata. |
| `0x110DE (69854)` | `smERR_ABORT_UNABLE_TO_DROP_LAST_CPATH` | A tablespace needs at least one checkpoint path; rename instead of dropping the last path. |
| `0x110DF (69855)` | `smERR_ABORT_CPATH_ALREADY_EXISTS` | Checkpoint path node already exists; do not add the same path again. |
| `0x110E5 (69861)` | `smERR_ABORT_INVALID_CIMAGE_HEADER` | Invalid checkpoint image header; copy a valid checkpoint image to `MEM_DB_DIR`. |
| `0x110E6 (69862)` | `smERR_ABORT_DefaultDBFileSizeNotAlignedToChunkSize` | `DEFAULT_MEM_DB_FILE_SIZE` must align to `EXPAND_CHUNK_PAGE_COUNT * PAGE_SIZE`. |
| `0x110EA (69866)` | `smERR_ABORT_SplitSizeNotAlignedToChunkSize` | Memory checkpoint image split size must align to expand chunk size. |
| `0x110EB (69867)` | `smERR_ABORT_INVALID_CIMAGE_FILESPEC_FORMAT` | Invalid checkpoint image filespec; check filespec format. |
| `0x110EC (69868)` | `smERR_ABORT_INPUT_UNSTABLE_CIMAGE` | Checkpoint image is not stable; check log anchor and use a stable checkpoint image. |
| `0x1114C (69964)` | `smERR_ABORT_DROP_CPATH_NOT_YET_MOVED_CIMG_IN_CPATH` | Checkpoint image remains in a checkpoint path being dropped; move it first. |
| `0x1115F (69983)` | `smERR_ABORT_CheckpointPathIsNullString` | Checkpoint path is empty; provide a valid path. |
| `0x11160 (69984)` | `smERR_ABORT_InvalidCheckpointPathABS` | Checkpoint path is not absolute; check `ALTIBASE_HOME` and use an absolute path. |
| `0x11161 (69985)` | `smERR_ABORT_InvalidCheckpointPathKeyWord` | Checkpoint path contains reserved keywords; set a supported path. |
| `0x11162 (69986)` | `smERR_ABORT_TooLongCheckpointPath` | Checkpoint path is too long; choose a path within the source limit. |
| `0x11171 (70001)` | `smERR_ABORT_InvalidChangeTrackingFile` | Change-tracking file is invalid; disable and re-enable change tracking. |
| `0x11172 (70002)` | `smERR_ABORT_ChangeTrackingState` | Unexpected change-tracking state; check change-tracking manager state. |
| `0x11176 (70006)` | `smERR_ABORT_NotDefinedIncrementalBackupPath` | No incremental backup path is defined; specify an incremental backup directory. |
| `0x11177 (70007)` | `smERR_ABORT_AlreadyExistIncrementalBackupPath` | Incremental backup path already exists; change directory or wait/retry. |
| `0x11178 (70008)` | `smERR_ABORT_BackupInfoState` | Unexpected Backup Information Manager state; check backup-info manager state. |
| `0x11179 (70009)` | `smERR_ABORT_AlreadyExistPath` | Directory already exists; delete, rename, or choose another directory. |
| `0x1117A (70010)` | `smERR_ABORT_ThereIsNoDatabaseIncrementalBackup` | No incremental database backup exists; perform one before restore. |
| `0x1117B (70011)` | `smERR_ABORT_ThereIsNoIncrementalBackup` | No incremental backup exists; perform one before restore. |
| `0x1117C (70012)` | `smERR_ABORT_FailToCreateDirectory` | Failed to create directory; check directory path and permission. |
| `0x11180 (70016)` | `smERR_ABORT_DuplicateMultiplexDirPath` | Duplicate `LOG_MULTIPLEX_DIR` or `ARCHIVE_MULTIPLEX_DIR` path; remove duplicate. |
| `0x11181 (70017)` | `smERR_ABORT_WrongLogMultiplexDirCount` | `LOG_MULTIPLEX_DIR` count differs from `LOG_MULTIPLEX_COUNT`; align values. |
| `0x11182 (70018)` | `smERR_ABORT_WrongArchMultiplexDirCount` | `ARCH_MULTIPLEX_DIR` count differs from `ARCH_MULTIPLEX_COUNT`; align values. |
| `0x11199 (70041)` | `smERR_ABORT_Cannot_Perform_Level1_Backup` | Cannot perform level 1 backup because level 0 backup does not exist; run level 0 first. |

Applies To: memory tablespace checkpoint image paths, checkpoint image files, incremental backup metadata, change tracking, `backupInfo`, and log/archive multiplex directory configuration.

Symptom: A memory checkpoint-path change, incremental backup/restore, or multiplexed log/archive configuration fails before or during backup/recovery.

Primary Causes: missing or inaccessible checkpoint path, attempt to drop the last checkpoint path, checkpoint image still present in the path, unstable checkpoint image, invalid or missing change-tracking/backup-info metadata, missing level 0 backup, duplicate or count-mismatched multiplex directories, or filesystem permission problem.

Immediate Action: Verify path existence and permission as the Altibase OS user. For incremental backup recovery, protect current `changeTracking`, `backupInfo`, log anchors, and logs before replacing metadata. Rebuild the incremental chain with a new level 0 backup after change tracking is disabled or lost.

Check SQL or Command:

```bash
ls -ld '<CHECKPOINT_OR_BACKUP_DIRECTORY>'
ls -l "$ALTIBASE_HOME/dbs/changeTracking" "$ALTIBASE_HOME/dbs/backupInfo"
tail -200 "$ALTIBASE_HOME/trc/altibase_boot.log"
```

```sql
SELECT m.space_id,
       m.space_name,
       p.checkpoint_path
FROM V$MEM_TABLESPACES m,
     V$MEM_TABLESPACE_CHECKPOINT_PATHS p
WHERE m.space_id = p.space_id
ORDER BY m.space_id, p.checkpoint_path;

SELECT backup_type,
       backup_tag,
       backup_file,
       begin_backup_time,
       end_backup_time
FROM V$BACKUP_INFO
ORDER BY begin_backup_time, backup_file;
```

Required Customer Input: exact version, failed backup/recovery/checkpoint command, checkpoint path, backup directory, whether incremental level 0 exists, `backupInfo` and `changeTracking` status, log anchor source, and trace log excerpt.

Version Cautions: The listed reference codes are present in the checked Korean 7.1, 7.3, and Altibase 8.1 verified source Error Message References. For 8.1 memory backup/recovery answers, also check any available `V$LOG.CHECKPOINT_SCALE` evidence before explaining checkpoint-image selection.

Escalation: Escalate before substituting checkpoint images, log anchors, or `backupInfo` files when file history is uncertain, when the incremental chain is inconsistent, or when trace logs show unexpected manager state after the documented corrective action.

Related Document: Administration and Operations; Data Dictionary and Performance Views; Data Types and Properties.

### Error Block: Tablespace State, Type, and DDL Errors

Error Codes: listed individually in the exact code map below.

Module / Severity: `SM` or `QP` / `ABORT`, plus `SM / RETRY` for retryable tablespace-structure change.

Exact code map:

| Reference code | Reference symbol | Source message or action focus |
| --- | --- | --- |
| `0x1102A (69674)` | `smERR_ABORT_NotFoundTableSpaceNodeByName` | Tablespace node not found by name; verify the tablespace exists. |
| `0x1102B (69675)` | `smERR_ABORT_NotFoundTableSpaceNode` | Tablespace node not found by ID; verify the tablespace exists. |
| `0x1102C (69676)` | `smERR_ABORT_MustBeDataFileOnlineMode` | Datafile node must be online; change datafile/tablespace state appropriately. |
| `0x11031 (69681)` | `smERR_ABORT_NotEnoughTableSpaceID` | Maximum tablespace ID reached; use existing tablespace or rebuild the database. |
| `0x11032 (69682)` | `smERR_ABORT_AlreadySetAutoExtendMode` | Datafile `AUTOEXTEND` mode is already set; no action is needed. |
| `0x11035 (69685)` | `smERR_ABORT_NotEnoughFreeSpace` | Tablespace has insufficient free space; add a datafile. |
| `0x11036 (69686)` | `smERR_ABORT_CannotRemoveDataFileNode` | Datafile is in use; do not remove it while allocated. |
| `0x11037 (69687)` | `smERR_ABORT_CannotDropTableSpace` | System-related tablespaces cannot be dropped. |
| `0x110AA (69802)` | `smERR_ABORT_AlreadyExistTableSpaceName` | Duplicate tablespace name; choose/check the name. |
| `0x110E0 (69856)` | `smERR_ABORT_ALTER_TBS_AUTOEXTEND_ALREADY_SET` | Tablespace `AUTOEXTEND` is already set; no action needed. |
| `0x110E1 (69857)` | `smERR_ABORT_ALTER_TBS_NEXTSIZE_NOT_ALIGNED_TO_CHUNK_SIZE` | `NEXT` must align to `EXPAND_CHUNK_PAGE_COUNT * PAGE_SIZE`. |
| `0x110E2 (69858)` | `smERR_ABORT_ALTER_TBS_MAXSIZE_LESSTHAN_CURRENT_SIZE` | `MAXSIZE` must be greater than or equal to current tablespace size. |
| `0x110E3 (69859)` | `smERR_ABORT_ALTER_TBS_AT_DROPPED_TBS` | Cannot alter a dropped tablespace; verify it exists. |
| `0x110E4 (69860)` | `smERR_ABORT_ALTER_TBS_AT_OFFLINE_TBS` | Cannot alter an offline tablespace; bring it online if appropriate. |
| `0x110E7 (69863)` | `smERR_ABORT_CANNOT_ALTER_STATUS_OF_SYSTEM_TABLESPACE` | Cannot change system, undo, or system temp tablespace status. |
| `0x110E8 (69864)` | `smERR_ABORT_CANNOT_ALTER_AUTOEXTEND_DICTIONARY_TABLESPACE` | Cannot alter dictionary tablespace `AUTOEXTEND`. |
| `0x110E9 (69865)` | `smERR_ABORT_ALTER_TBS_ONOFF_ALLOWED_ONLY_AT_META_SERVICE_PHASE` | `ALTER TABLESPACE ONLINE/OFFLINE` is allowed only in `META` or `SERVICE`. |
| `0x110EE (69870)` | `smERR_ABORT_TBSInitSizeNotAlignedToChunkSize` | Initial memory tablespace size must align to expand chunk size. |
| `0x110EF (69871)` | `smERR_ABORT_UNABLE_TO_EXTEND_CHUNK_WHEN_AUTO_EXTEND_OFF` | Cannot extend when `AUTOEXTEND` is off; use documented `AUTOEXTEND ON`. |
| `0x110F0 (69872)` | `smERR_ABORT_UNABLE_TO_EXTEND_CHUNK_MORE_THAN_MEM_MAX_DB_SIZE` | Memory tablespace extension would exceed `MEM_MAX_DB_SIZE`; adjust capacity or remove other tablespace. |
| `0x110F1 (69873)` | `smERR_ABORT_UNABLE_TO_EXTEND_CHUNK_MORE_THAN_TBS_MAXSIZE` | Extension would exceed tablespace `MAXSIZE`; adjust `MAXSIZE` if safe. |
| `0x110F4 (69876)` | `smERR_ABORT_TABLESPACE_IS_ALREADY_ONLINE` | Tablespace is already `ONLINE`; do not repeat `ONLINE`. |
| `0x110F5 (69877)` | `smERR_ABORT_TABLESPACE_IS_ALREADY_OFFLINE` | Tablespace is already `OFFLINE`; do not repeat `OFFLINE`. |
| `0x110F8 (69880)` | `smERR_ABORT_CannotDiscardTableSpace` | Cannot discard system, undo, or system temp tablespace. |
| `0x110FB (69883)` | `smERR_ABORT_UNABLE_TO_USE_OFFLINE_TBS` | Cannot use offline tablespace; execute `ALTER TABLESPACE ... ONLINE` only after impact review. |
| `0x110FC (69884)` | `smERR_ABORT_UNABLE_TO_USE_DISCARDED_TBS` | Cannot use discarded tablespace; drop and recreate it. |
| `0x110FD (69885)` | `smERR_ABORT_TBS_ALREADY_DISCARDED` | Tablespace is already discarded; drop and recreate it. |
| `0x110FE (69886)` | `smERR_ABORT_AUTOEXT_ON_UNALLOWED_FOR_USED_UP_FILE` | Cannot switch `AUTOEXTEND` on for a used-up datafile; use current or unused file. |
| `0x11100 (69888)` | `smERR_ABORT_UNABLE_TO_EXTEND_CHUNK_MORE_THAN_VOLATILE_MAX_DB_SIZE` | Volatile extension would exceed `VOLATILE_MAX_DB_SIZE`; increase property or drop another volatile tablespace. |
| `0x11102 (69890)` | `smERR_ABORT_UNABLE_TO_ALTER_ONLINE_CUZ_MEM_MAX_DB_SIZE` | Bringing tablespace online would exceed `MEM_MAX_DB_SIZE`; increase property or offline another tablespace. |
| `0x11103 (69891)` | `smERR_ABORT_UNABLE_TO_CREATE_CUZ_MEM_MAX_DB_SIZE` | Creating tablespace would exceed `MEM_MAX_DB_SIZE`; increase property or offline/drop another tablespace. |
| `0x11115 (69909)` | `smERR_ABORT_TBS_ATTR_FLAG_ALREADY_SET` | Tablespace attribute already has the requested value; no action needed. |
| `0x11117 (69911)` | `smERR_ABORT_UNABLE_TO_COMPRESS_VOLATILE_TBS_LOG` | Log compression is not supported for volatile tablespaces. |
| `0x11123 (69923)` | `smERR_ABORT_NOT_ENOUGH_SPACE` | Tablespace does not have enough free space; add a new datafile. |
| `0x11139 (69945)` | `smERR_ABORT_CannotCreateSegInUndoTBS` | Cannot create segments in undo tablespace; use another tablespace. |
| `0x1118A (70026)` | `smERR_ABORT_TablespaceLockUse` | Tablespace locks are disabled by `TABLESPACE_LOCK_ENABLE=0`; change property only after impact review. |
| `0x13111 (78097)` | `smERR_REBUILD_smiTBSModified` | Tablespace structure was modified; rebuild the query and retry. |
| `0x311D7 (201175)` | `qpERR_ABORT_QDT_DUPLICATE_TBS_NAME` | Duplicate tablespace name; check specified name. |
| `0x311D8 (201176)` | `qpERR_ABORT_QDT_NOT_EXIST_TBS` | Specified tablespace name was not found; verify spelling and existence. |
| `0x311DA (201178)` | `qpERR_ABORT_QDT_MISMATCH_TBS_TYPE` | Tablespace type and file type differ; match the file clause to tablespace type. |
| `0x311DB (201179)` | `qpERR_ABORT_QDT_NO_DROP_SYSTEM_TBS` | `SYSTEM` tablespace cannot be dropped. |
| `0x311DD (201181)` | `qpERR_ABORT_QDT_OBJECT_EXIST` | Tablespace has objects; drop/move objects or use documented destructive form after impact review. |
| `0x311DE (201182)` | `qpERR_ABORT_QDT_NO_CREATE_IN_SYSTEM_TBS` | Cannot create objects in dictionary, undo, or temp tablespace. |
| `0x311DF (201183)` | `qpERR_ABORT_QDT_NO_ACCESS_TBS` | User cannot access the tablespace; grant/access needs review. |
| `0x311E3 (201187)` | `qpERR_ABORT_QDT_ERR_INVALID_DATA_TBS` | Specified tablespace is not a valid data tablespace. |
| `0x311E4 (201188)` | `qpERR_ABORT_QDT_ERR_INVALID_TEMP_TBS` | Specified tablespace is not a valid temporary tablespace. |
| `0x311E7 (201191)` | `qpERR_ABORT_QDT_CANNOT_ONOFFLINE` | Cannot bring specified tablespace online/offline; check tablespace type/state. |
| `0x3124F (201295)` | `qpERR_ABORT_QDT_DUPLICATE_CHECKPOINT_PATH` | Duplicate checkpoint path; check specified path. |
| `0x31250 (201296)` | `qpERR_ABORT_QDT_NO_MEM_TBS_SPLIT_FILE_SIZE` | Memory tablespace syntax lacks `SPLIT EACH`; specify it when required. |
| `0x31251 (201297)` | `qpERR_ABORT_QDT_INVALID_ALTER_ON_DISK_TBS` | `ALTER DISK TABLESPACE` used on non-disk tablespace; match statement and type. |
| `0x31252 (201298)` | `qpERR_ABORT_QDT_INVALID_ALTER_ON_MEM_TBS` | `ALTER MEMORY TABLESPACE` used on non-memory tablespace; match statement and type. |
| `0x31253 (201299)` | `qpERR_ABORT_QDT_INVALID_ALTER_ON_VOLATILE_TBS` | `ALTER VOLATILE TABLESPACE` used on non-volatile tablespace; match statement and type. |
| `0x31254 (201300)` | `qpERR_ABORT_QDT_INVALID_ALTER_ON_MEM_OR_VOL_TBS` | `ALTER TABLESPACE` clause requires memory or volatile tablespace; verify type. |
| `0x31255 (201301)` | `qpERR_ABORT_QDT_CANNOT_DISCARD` | Cannot discard specified tablespace; check type/state. |
| `0x31256 (201302)` | `qpERR_ABORT_QDT_CANNOT_ALTER_SYSTEM_TABLESPACE` | Cannot alter system tablespace; check specified tablespace. |
| `0x3128B (201355)` | `qpERR_ABORT_QDT_PART_TABLE_IN_DIFFERENT_TBS` | Partitioned table has partitions in different tablespaces; drop table before the requested statement when source action applies. |
| `0x3128C (201356)` | `qpERR_ABORT_QDT_PART_INDEX_IN_DIFFERENT_TBS` | Partitioned index has partitions in different tablespaces; drop index before the requested statement when source action applies. |
| `0x31295 (201365)` | `qpERR_ABORT_QDT_ERR_INVALID_USER_DEFAULT_TEMP_TBS` | User default temporary tablespace is invalid; check the user's temporary tablespace. |
| `0x312A0 (201376)` | `qpERR_ABORT_QDT_DUPLICATE_TBS_ATTRIBUTE` | Duplicate tablespace attribute; check attribute list. |
| `0x312A9 (201385)` | `qpERR_ABORT_QDT_UNABLE_TO_COMPRESS_VOLATILE_TBS_LOG` | Log compression is not supported for volatile tablespaces. |
| `0x312E1 (201441)` | `qpERR_ABORT_QDT_NON_ASCII_TBS_NAME` | Tablespace name contains invalid character set; use ASCII characters. |
| `0x312E6 (201446)` | `qpERR_ABORT_QDT_CANNOT_RENAME_SYS_TBS` | System tablespace cannot be renamed. |
| `0x31365 (201573)` | `qpERR_ABORT_QDT_DROP_TBS_DISABLE_BECAUSE_TEMP_TABLE` | Volatile tablespace cannot be dropped while temporary tables exist; truncate temporary tables and retry. |
| `0x31458 (201816)` | `qpERR_ABORT_QDB_CANNOT_ALTER_TABLESPACE_TEMPORARY_TABLE` | Temporary table cannot modify tablespace; do not run `ALTER TABLESPACE` syntax on a temporary table. |

Applies To: `CREATE TABLESPACE`, `ALTER TABLESPACE`, `DROP TABLESPACE`, datafile clauses, checkpoint path clauses, user default/temporary tablespace checks, tablespace locks, memory/volatile limits, and object placement.

Symptom: DDL or DML fails because the named tablespace is missing, the type is wrong, the state is offline/discarded/dropped/system, capacity limits block the operation, or the requested DDL is not valid for that tablespace family.

Primary Causes: wrong tablespace name, duplicate name, wrong disk/memory/volatile/temp type, system/dictionary/undo/temp tablespace restriction, user lacks tablespace access, existing objects block drop, replicated or temporary objects block state changes, `AUTOEXTEND`/`MAXSIZE`/`NEXT` mismatch, `MEM_MAX_DB_SIZE` or `VOLATILE_MAX_DB_SIZE` limit, or invalid checkpoint path.

Immediate Action: Query the tablespace, datafile, object, user-access, and property state before generating DDL. State destructive impact before `DROP TABLESPACE`, `INCLUDING CONTENTS`, `AND DATAFILES`, `DISCARD`, or online/offline operations.

Check SQL or Command:

```sql
SELECT id,
       name,
       type,
       state,
       datafile_count,
       total_page_count,
       allocated_page_count,
       page_size
FROM V$TABLESPACES
ORDER BY id;

SELECT d.id,
       d.name,
       d.spaceid,
       t.name AS tablespace_name,
       d.currsize,
       d.autoextend,
       d.state
FROM V$DATAFILES d,
     V$TABLESPACES t
WHERE d.spaceid = t.id
ORDER BY d.spaceid, d.id;

SELECT name, value1
FROM V$PROPERTY
WHERE name IN (
  'MEM_MAX_DB_SIZE',
  'VOLATILE_MAX_DB_SIZE',
  'EXPAND_CHUNK_PAGE_COUNT',
  'TABLESPACE_LOCK_ENABLE',
  'USER_DATA_FILE_INIT_SIZE',
  'USER_DATA_FILE_MAX_SIZE'
)
ORDER BY name;

SELECT u.user_name,
       t.table_name,
       t.table_type,
       t.tbs_name
FROM SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_USERS_ u
WHERE t.user_id = u.user_id
  AND t.tbs_name = '<TABLESPACE_NAME>'
ORDER BY u.user_name, t.table_name;
```

Required Customer Input: exact version, full error line, SQL text, tablespace name, intended tablespace family, datafile/checkpoint path clauses, object owner/name, and whether the operation is planned maintenance or recovery.

Version Cautions: The listed reference codes are present in the checked Korean 7.1, 7.3, and Altibase 8.1 verified source Error Message References. The exact corrective DDL differs for disk, memory, volatile, undo, and temporary tablespaces; ask for type and phase before returning copy-ready SQL.

Escalation: Escalate or require DBA confirmation before dropping objects, dropping/discarding a tablespace, deleting datafiles, or changing memory/volatile maximum properties in production.

Related Document: Administration and Operations; SQL DDL Generation; Data Dictionary and Performance Views; Data Types and Properties.

### Error Block: Tablespace Not Found

Error Code: `0x311D8 (201176)`.

Reference Symbol: `qpERR_ABORT_QDT_NOT_EXIST_TBS`.

Module / Severity: QP / `ABORT`.

Message: `Tablespace not found. The name of the specified tablespace was not found in the database.`

Applies To: DDL that names a tablespace.

Symptom: A DDL statement fails because the named tablespace cannot be resolved.

Primary Causes: Misspelled tablespace name, wrong owner assumptions, dropped tablespace, or version-specific DDL copied from another environment.

Immediate Action: Verify the tablespace exists and use the exact stored name.

Check SQL or Command:

```sql
SELECT id, name, type, state
FROM V$TABLESPACES
WHERE name = '<TABLESPACE_NAME>';
```

Version Cautions: Applies across 7.1, 7.3, and 8.1.

Related Document: Administration and Operations; Data Dictionary and Performance Views.

### Error Block: Tablespace Has Objects

Error Code: `0x311DD (201181)`.

Reference Symbol: `qpERR_ABORT_QDT_OBJECT_EXIST`.

Module / Severity: QP / `ABORT`.

Message: `The tablespace has objects.`

Applies To: `DROP TABLESPACE`.

Symptom: A tablespace cannot be dropped because objects still exist in it.

Primary Causes: Tables, indexes, LOB segments, or dependent objects remain in the tablespace.

Immediate Action: Identify and drop or move objects explicitly, or use the documented `DROP TABLESPACE ... INCLUDING CONTENTS` form only after confirming impact and backup status.

Check SQL or Command:

```sql
SELECT u.user_name,
       t.table_name,
       t.table_type,
       t.tbs_name
FROM SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_USERS_ u
WHERE t.user_id = u.user_id
  AND t.tbs_name = '<TABLESPACE_NAME>'
ORDER BY u.user_name, t.table_name;
```

Version Cautions: Do not drop system, undo, or temporary tablespaces. State destructive impact before providing `DROP TABLESPACE`.

Related Document: Administration and Operations.

### Error Block: SQL Parser, Clause, and Statement-Shape Errors

Error Codes: listed individually in the exact code map below.

Module / Severity: QP / `ABORT`.

Exact code map:

| Runtime / reference code | Reference symbol | Source message or action focus |
| --- | --- | --- |
| `ERR-31001` / `0x31001 (200705)` | `qpERR_ABORT_QCP_SYNTAX` | SQL syntax error; check reserved words, delimiters, and target-version SQL grammar. |
| `ERR-31003` / `0x31003 (200707)` | `qpERR_ABORT_QCP_NOT_SUPPORTED_SYNTAX` | Unsupported syntax; rewrite using a supported Altibase form. |
| `ERR-31004` / `0x31004 (200708)` | `qpERR_ABORT_QCP_CONFLICT_NULL_CONSTRAINT` | Duplicate or conflicting `NULL` / `NOT NULL` constraints; remove the duplicate or conflict. |
| `ERR-31005` / `0x31005 (200709)` | `qpERR_ABORT_QCP_NO_HAVE_DATATYPE_IN_CRT_TBL` | `CREATE TABLE` or `ALTER TABLE ADD COLUMN` column lacks a data type; specify one. |
| `ERR-31006` / `0x31006 (200710)` | `qpERR_ABORT_QCP_HAVE_DATATYPE_IN_CRT_TBL_AS_SELECT` | `CREATE TABLE AS SELECT` column definition has a data type; remove data types from the column list. |
| `ERR-31007` / `0x31007 (200711)` | `qpERR_ABORT_QCP_DUPLICATE_COLUMN_NAME` | Duplicate column name in statement text; make column names unique. |
| `ERR-31234` / `0x31234 (201268)` | `qpERR_ABORT_QCP_DUPLICATE_CONSTRAINT_NAME` | Duplicate constraint name in statement text; make constraint names unique. |
| `ERR-31008` / `0x31008 (200712)` | `qpERR_ABORT_QCP_HAVE_NO_COLUMN` | `CREATE TABLE` or `ALTER TABLE ADD COLUMN` has no column; specify at least one column. |
| `ERR-3118B` / `0x3118B (201099)` | `qpERR_ABORT_QCP_MAX_NAME_LENGTH_OVERFLOW` | Object name length exceeds the limit; shorten the name. |
| `ERR-3121C` / `0x3121C (201244)` | `qpERR_ABORT_QCP_INVALID_LOGGING_OPTION` | Duplicate `LOGGING` / `NOLOGGING` option; keep one option. |
| `ERR-3121D` / `0x3121D (201245)` | `qpERR_ABORT_QCP_INVALID_PARALLEL_OPTION` | Duplicate `PARALLEL` / `NOPARALLEL` option; keep one option. |
| `ERR-3121E` / `0x3121E (201246)` | `qpERR_ABORT_QCP_INVALID_TABLESPACE_OPTION` | Duplicate tablespace-name clause; remove the duplicate. |
| `ERR-31242` / `0x31242 (201282)` | `qpERR_ABORT_QCP_INVALID_BUFFER_OPTION` | Duplicate `BUFFER` / `NOBUFFER` option; keep one option. |
| `ERR-312DD` / `0x312DD (201437)` | `qpERR_ABORT_QCP_INVALID_DATABASE_CHARSET` | Database character set is missing; specify `CHARACTER SET`. |
| `ERR-312DE` / `0x312DE (201438)` | `qpERR_ABORT_QCP_INVALID_NATIONAL_CHARSET` | National character set is missing; specify `NATIONAL CHARACTER SET`. |
| `ERR-31388` / `0x31388 (201608)` | `qpERR_ABORT_QCP_COLUMN_CHECK_CONSTRAINT_REFERENCE_OTHER_COLUMN` | Column-level `CHECK` references another column; revise as a table constraint or rewrite. |
| `ERR-31389` / `0x31389 (201609)` | `qpERR_ABORT_QCP_SET_USER_NAME_OR_TABLE_NAME_TO_CONSTRAINT_COLUMN` | Column constraint specified user or table name; remove owner/table qualification. |
| `ERR-3139A` / `0x3139A (201626)` | `qpERR_ABORT_QCP_CANNOT_SPECIFY_USER_NAME_OR_TABLE_NAME` | Function-based index column specified user or table name; remove the qualification. |
| `ERR-3139F` / `0x3139F (201631)` | `qpERR_ABORT_QCP_REQUIRE_OWNER_NAME_IN_DEFAULT_EXPR` | Stored function owner is required in a function-based index definition; qualify the function. |
| `ERR-313A0` / `0x313A0 (201632)` | `qpERR_ABORT_QCP_REQUIRE_OWNER_NAME_IN_CHECK_EXPR` | Stored function owner is required in a check-constraint expression; qualify the function. |

Applies To: parser and validator checks for `CREATE TABLE`, `ALTER TABLE`, `CREATE TABLE AS SELECT`, tablespace clauses, storage options, check constraints, function-based indexes, and database character-set clauses.

Symptom: Altibase rejects the statement before it can execute object changes or DML.

Primary Causes: unsupported dialect syntax, a statement shape that violates Altibase SQL Reference grammar, duplicated clauses, missing column data types, wrong `CREATE TABLE AS SELECT` column-list form, duplicate names, missing character-set clauses, or invalid check/function expression qualification.

Immediate Action: Confirm target version first, then isolate the failing clause. Rewrite from the Altibase SQL Reference for that version instead of translating Oracle or another DBMS grammar mechanically.

Check SQL or Command:

```sql
SELECT product_version,
       meta_version,
       protocol_version
FROM V$VERSION;

-- Check object and column names separately before treating every parser error as grammar.
SELECT u.user_name,
       t.table_name,
       t.table_type
FROM SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_USERS_ u
WHERE t.user_id = u.user_id
  AND u.user_name = '<OWNER_NAME>'
  AND t.table_name = '<TABLE_NAME>';
```

Required Customer Input: exact version and patch level, full SQL text, object owner/name, whether the SQL was generated from another DBMS, and the full error line including the substituted parser detail.

Version Cautions: The listed parser/DDL-shape codes are present in the checked Korean 7.1, 7.3, and Altibase 8.1 verified source Error Message References. Do not apply 8.1-only syntax such as native `JSON`, `IF EXISTS`, or `IF NOT EXISTS` to 7.1 or 7.3 without exact target-source proof.

Related Document: SQL DDL Generation; SQL DML and Oracle Compatibility.

### Error Block: Object Name Already Exists

Error Code: `ERR-31022` / `0x31022 (200738)`.

Reference Symbol: `qpERR_ABORT_QDB_EXIST_OBJECT_NAME`.

Module / Severity: QP / `ABORT`.

Message: `The name is already used by an existing object.`

Applies To: `CREATE TABLE`, `CREATE VIEW`, `CREATE SEQUENCE`, and other object creation statements.

Symptom: A DDL statement tries to create an object with a name already used by that user.

Primary Causes: Existing table, view, sequence, queue, or synonym-like object with the same name.

Immediate Action: Use a unique name, drop or rename the existing object after impact review, or generate idempotent deployment logic outside Altibase if needed.

Check SQL or Command:

```sql
SELECT u.user_name,
       t.table_name,
       t.table_type,
       t.created,
       t.last_ddl_time
FROM SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_USERS_ u
WHERE t.user_id = u.user_id
  AND u.user_name = '<OWNER_NAME>'
  AND t.table_name = '<OBJECT_NAME>';
```

Version Cautions: Use exact stored case for quoted identifiers.

Related Document: SQL DDL Generation; Data Dictionary and Performance Views.

### Error Block: Table, Column, Data Type, Temporary Table, and LOB DDL Errors

Error Codes: listed individually in the exact code map below.

Module / Severity: QP / `ABORT`.

Exact code map:

| Runtime / reference code | Reference symbol | Source message or action focus |
| --- | --- | --- |
| `ERR-31022` / `0x31022 (200738)` | `qpERR_ABORT_QDB_EXIST_OBJECT_NAME` | Object name is already used; choose a unique object name or handle the existing object. |
| `ERR-31023` / `0x31023 (200739)` | `qpERR_ABORT_QDB_DUPLICATE_COLUMN` | Duplicate column name in a table; rename one column. |
| `ERR-31025` / `0x31025 (200741)` | `qpERR_ABORT_QDB_MISMATCH_COL_COUNT` | `CREATE TABLE AS SELECT` column count differs from target-list expression count. |
| `ERR-31026` / `0x31026 (200742)` | `qpERR_ABORT_QDB_INVALID_COLUMN_COUNT` | Table has too many, too few, or zero columns after add/drop; review column count. |
| `ERR-31028` / `0x31028 (200744)` | `qpERR_ABORT_QDB_CREATE_DISABLE_DATA_TYPE` | Column cannot be created with the specified data type; verify allowed data types. |
| `ERR-31233` / `0x31233 (201267)` | `qpERR_ABORT_QDB_FIXED_PAGE_SIZE_ERROR` | Fixed record size exceeds page size; reduce fixed-length columns. |
| `ERR-31236` / `0x31236 (201270)` | `qpERR_ABORT_QDB_IN_ROW_SIZE_ERROR` | `IN ROW` size exceeds maximum; reduce the `IN ROW` size. |
| `ERR-31243` / `0x31243 (201283)` | `qpERR_ABORT_QDB_MISMATCHED_LOB_TYPE_COLUMN` | LOB type column mismatch; check `BLOB`/`CLOB` column specification. |
| `ERR-31244` / `0x31244 (201284)` | `qpERR_ABORT_QDB_NOT_FOUND_LOB_TYPE_COLUMN` | LOB type column not found; verify the target LOB column name. |
| `ERR-31257` / `0x31257 (201303)` | `qpERR_ABORT_QDB_LOB_VIOLATION_ON_VOLATILE_TABLE` | Volatile table cannot have a LOB column; remove the LOB column or change storage design. |
| `ERR-312ED` / `0x312ED (201453)` | `qpERR_ABORT_QDB_INVALID_MODIFICATION` | Invalid column modification; data-type change is restricted for types such as `CHAR`, `BLOB`, `CLOB`, `NIBBLE`, `BYTE`, `TIMESTAMP`, and `GEOMETRY`, and cannot change into `BLOB`, `CLOB`, `TIMESTAMP`, or `GEOMETRY`. |
| `ERR-312EE` / `0x312EE (201454)` | `qpERR_ABORT_QDB_INVALID_LENGTH` | Invalid length for the specified data type; check type length. |
| `ERR-3135F` / `0x3135F (201567)` | `qpERR_ABORT_QDB_CANNOT_CREATE_TEMPORARY_TABLE_IN_NONVOLATILE_TBS` | Temporary tables cannot be created in non-volatile tablespaces; use a volatile tablespace. |
| `ERR-31360` / `0x31360 (201568)` | `qpERR_ABORT_QDB_NOT_SUPPORTED_TEMPORARY_TABLE_FEATURE` | Unsupported temporary-table feature; remove unsupported table options. |
| `ERR-31363` / `0x31363 (201571)` | `qpERR_ABORT_QDB_TEMPORARY_TABLE_DDL_DISABLE` | DDL cannot execute while a related temporary table is in use; truncate related temporary tables before retry. |
| `ERR-313B6` / `0x313B6 (201654)` | `qpERR_ABORT_QDB_COMPRESSION_NOT_SUPPORTED_DATATYPE` | Unsupported data type for compression column; check column type. |
| `ERR-313B7` / `0x313B7 (201655)` | `qpERR_ABORT_QDB_COMPRESSION_NOT_SUPPORTED_TABLESPACE` | Compression column supports only memory tablespaces; check tablespace type. |
| `ERR-31458` / `0x31458 (201816)` | `qpERR_ABORT_QDB_CANNOT_ALTER_TABLESPACE_TEMPORARY_TABLE` | Temporary table cannot modify tablespace; do not use `ALTER TABLESPACE` syntax on the temporary table. |

Applies To: table creation, `ALTER TABLE`, column add/drop/modify, `IN ROW` sizing, LOB column clauses, compression columns, volatile/temporary table placement, and DDL against active temporary tables.

Symptom: DDL fails because a column shape, storage target, type change, LOB clause, temporary-table rule, or compression/storage combination is not valid for Altibase.

Primary Causes: generated DDL used an unsupported data type, a row or `IN ROW` size exceeded limits, a LOB column was placed in volatile storage, a LOB clause named a non-LOB column, a column type change crossed an unsupported boundary, a temporary table was created outside volatile storage, or a temporary table was active when DDL was attempted.

Immediate Action: Query current object, column, tablespace, and constraint metadata before rewriting DDL. For active temporary-table cases, use the source action of truncating related temporary tables; do not invent a session-kill procedure unless the target-version source provides one.

Check SQL or Command:

```sql
SELECT u.user_name,
       t.table_name,
       t.table_type,
       t.tbs_name,
       t.temporary,
       t.is_partitioned,
       t.access
FROM SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_USERS_ u
WHERE t.user_id = u.user_id
  AND u.user_name = '<OWNER_NAME>'
  AND t.table_name = '<TABLE_NAME>';

SELECT c.column_order,
       c.column_name,
       c.data_type,
       c.precision,
       c.scale,
       c.is_nullable,
       c.store_type
FROM SYSTEM_.SYS_COLUMNS_ c,
     SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_USERS_ u
WHERE c.user_id = t.user_id
  AND c.table_id = t.table_id
  AND t.user_id = u.user_id
  AND u.user_name = '<OWNER_NAME>'
  AND t.table_name = '<TABLE_NAME>'
ORDER BY c.column_order;

SELECT id, name, type, state
FROM V$TABLESPACES
ORDER BY id;
```

Required Customer Input: target version, full DDL, owner/table/column names, current table definition, target tablespace type, whether the object is replicated, and whether temporary tables are active.

Version Cautions: The listed non-JSON DDL codes are present in the checked Korean 7.1, 7.3, and Altibase 8.1 verified source Error Message References. Native `JSON` and Temporary LOB behavior are 8.1-specific in this attachment set; use the JSON blocks for 8.1 JSON errors.

Escalation: Escalate before dropping or rebuilding objects when metadata checks show replicated tables, hidden/compressed/encrypted columns, active temporary tables, or storage limits that cannot be resolved by a documented DDL rewrite.

Related Document: SQL DDL Generation; Data Types and Properties; Data Dictionary and Performance Views.

### Error Block: User, Table, Column, Sequence, Index, or Replication Not Found

Error Code: `ERR-31010`, `ERR-31011`, `ERR-31012`, `ERR-31013`, `ERR-31014`, `ERR-31017`.

Reference Symbol: `qpERR_ABORT_QCM_NOT_EXIST_USER`, `qpERR_ABORT_QCM_NOT_EXIST_TABLE`, `qpERR_ABORT_QCM_NOT_EXIST_COLUMN`, `qpERR_ABORT_QCM_NOT_EXIST_SEQUENCE`, `qpERR_ABORT_QCM_NOT_EXISTS_INDEX`, `qpERR_ABORT_QCM_REPL_NOT_FOUND`.

Module / Severity: QP / `ABORT`.

Message: `User not found`, `Table not found`, `Column not found`, `Sequence not found`, `Index not found`, or `Replication not found`.

Applies To: DDL, DML, replication DDL, and dictionary-dependent SQL.

Symptom: Altibase cannot resolve an object referenced by the SQL statement.

Primary Causes: Wrong owner, typo, missing object, quoted identifier case mismatch, or running against the wrong database.

Immediate Action: Verify the owner-qualified object name and the current connection user.

Check SQL or Command:

```sql
-- User check.
SELECT user_name
FROM SYSTEM_.SYS_USERS_
WHERE user_name = '<OWNER_NAME>';

-- Table, view, queue, or sequence-style object check.
SELECT u.user_name, t.table_name, t.table_type
FROM SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_USERS_ u
WHERE t.user_id = u.user_id
  AND u.user_name = '<OWNER_NAME>'
  AND t.table_name = '<OBJECT_NAME>';

-- Column check.
SELECT u.user_name, t.table_name, c.column_name
FROM SYSTEM_.SYS_USERS_ u,
     SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_COLUMNS_ c
WHERE u.user_id = t.user_id
  AND t.user_id = c.user_id
  AND t.table_id = c.table_id
  AND u.user_name = '<OWNER_NAME>'
  AND t.table_name = '<TABLE_NAME>'
  AND c.column_name = '<COLUMN_NAME>';

-- Index check.
SELECT u.user_name, t.table_name, i.index_name
FROM SYSTEM_.SYS_USERS_ u,
     SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_INDICES_ i
WHERE u.user_id = t.user_id
  AND t.table_id = i.table_id
  AND u.user_name = '<OWNER_NAME>'
  AND t.table_name = '<TABLE_NAME>'
  AND i.index_name = '<INDEX_NAME>';

-- Replication definition and host checks.
SELECT replication_name, is_started, repl_mode, role
FROM SYSTEM_.SYS_REPLICATIONS_
WHERE replication_name = '<REPLICATION_NAME>';

SELECT replication_name, host_ip, port_no, conn_type
FROM SYSTEM_.SYS_REPL_HOSTS_
WHERE replication_name = '<REPLICATION_NAME>';
```

Version Cautions: Applies across 7.1, 7.3, and 8.1.

Related Document: Data Dictionary and Performance Views.

### Error Block: Insufficient Privileges

Error Code: `0x311B1 (201137)`, `0x31293 (201363)`, `0x4107C (266364)`.

Reference Symbol: `qpERR_ABORT_QDP_INSUFFICIENT_PRIVILEGES`, `qpERR_ABORT_QCI_NotPermittedUser`, `mmERR_ABORT_INSUFFICIENT_PRIV`.

Module / Severity: QP or MM / `ABORT`.

Message: `The user must have <0%s> privilege(s) to execute this statement.`, `Unauthorized user.`, or `Insufficient privileges. The user has to connect as SYSDBA.`

Applies To: DDL, DBA operations, startup, shutdown, backup, recovery, and administrative SQL.

Symptom: The statement is rejected because the connected user lacks the required system, object, or `SYSDBA` privilege.

Primary Causes: Wrong user, missing grant, attempting `SYSDBA` work without `-sysdba`, or operation restricted to `SYS` or `SYSTEM_`.

Immediate Action: Connect with the correct user or ask a DBA to grant the required privilege. Do not suggest direct DML on meta tables.

Check SQL or Command:

```bash
isql -u sys -p '<password>' -sysdba
```

```sql
SELECT user_name
FROM SYSTEM_.SYS_USERS_
WHERE user_name = '<USER_NAME>';
```

Version Cautions: Applies across 7.1, 7.3, and 8.1. Explain least-privilege alternatives for application users.

Related Document: Administration and Operations; SQL DDL Generation.

### Error Block: Constraint Definition, Unique Index, and Referential Errors

Error Codes: listed individually in the exact code map below.

Module / Severity: SM or QP / `ABORT`.

Exact code map:

| Runtime / reference code | Reference symbol | Source message or action focus |
| --- | --- | --- |
| `ERR-11058` / `0x11058 (69720)` | `smERR_ABORT_smnUniqueViolation` | Row already exists in a unique index; check unique/primary key values and standalone unique indexes. |
| `ERR-31042` / `0x31042 (200770)` | `qpERR_ABORT_QDN_NOT_EXISTS_CONSTRAINT` | Constraint not found; check `SYSTEM_.SYS_CONSTRAINTS_`. |
| `ERR-31043` / `0x31043 (200771)` | `qpERR_ABORT_QDN_NOT_EXISTS_UNIQUE_KEY` | `UNIQUE KEY` constraint not found; check key metadata. |
| `ERR-31044` / `0x31044 (200772)` | `qpERR_ABORT_QDN_NOT_EXISTS_PRIMARY_KEY` | `PRIMARY KEY` constraint not found; check key metadata. |
| `ERR-31045` / `0x31045 (200773)` | `qpERR_ABORT_QDN_DUPLICATE_PRIMARY_KEY` | Primary key already exists; drop the existing key before creating a new one. |
| `ERR-31046` / `0x31046 (200774)` | `qpERR_ABORT_QDN_DUPLICATE_CONSTRAINT` | Constraint name already exists; use a different constraint name. |
| `ERR-31047` / `0x31047 (200775)` | `qpERR_ABORT_QDN_MAX_KEY_COLUMN_COUNT` | Too many key columns; reduce index/key column count. |
| `ERR-31049` / `0x31049 (200777)` | `qpERR_ABORT_QDN_REFERENCED_CONSTRAINT_NOT_FOUND` | Referenced primary/unique constraint not found; create or reference a valid key. |
| `ERR-3104A` / `0x3104A (200778)` | `qpERR_ABORT_QDN_ADD_COL_NO_DEFAULT_NOTNULL` | Cannot add `NOT NULL` column without a default value; add a default or remove `NOT NULL`. |
| `ERR-3104B` / `0x3104B (200779)` | `qpERR_ABORT_QDN_DUPLICATE_CONSTRAINT_SPEC` | Column already has the same constraint; check duplicate constraint definition. |
| `ERR-31190` / `0x31190 (201104)` | `qpERR_ABORT_QDN_NOT_COMPATIBLE_TYPE` | Incompatible data types in key/constraint definition; align referencing and referenced types. |
| `ERR-31238` / `0x31238 (201272)` | `qpERR_ABORT_QDN_MISMATCHED_REFERENCING_COLUMN_COUNT` | Referencing-column count does not match referenced key count. |
| `ERR-31291` / `0x31291 (201361)` | `qpERR_ABORT_QDN_CANNOT_CREATE_LOCAL_UNIQUE_KEY_CONSTR_ON_NON_PART_TABLE` | Local unique key cannot be created on a non-partitioned table. |
| `ERR-31321` / `0x31321 (201505)` | `qpERR_ABORT_QDB_DROP_MULTI_COLUMN_CONSTRAINT_EXIST` | Cannot drop a column with multi-column constraints; drop related constraints first. |
| `ERR-31361` / `0x31361 (201569)` | `qpERR_ABORT_QDN_CANNOT_CREATE_FOREIGN_KEY_ON_TEMPORARY_TABLE` | Cannot create a foreign key on a temporary table; remove the foreign key. |
| `ERR-3138C` / `0x3138C (201612)` | `qpERR_ABORT_QDB_USE_SEQUENCE_IN_CHECK_CONSTRAINT` | Sequence cannot be used in `CHECK`; remove sequence use. |
| `ERR-3138D` / `0x3138D (201613)` | `qpERR_ABORT_QDB_USE_VARIABLE_IN_CHECK_CONSTRAINT` | Variable cannot be used in `CHECK`; remove variable use. |
| `ERR-3138E` / `0x3138E (201614)` | `qpERR_ABORT_QDB_NOT_ALLOWED_CHECK_CONSTRAINT` | `CHECK` constraint is not allowed in this statement position; remove or relocate it. |
| `ERR-31390` / `0x31390 (201616)` | `qpERR_ABORT_QDN_NOT_SUPPORT_LOB_COLUMN_IN_CHECK_CONSTRAINT` | LOB column is not supported in a `CHECK` constraint; remove LOB columns from the expression. |
| `ERR-31391` / `0x31391 (201617)` | `qpERR_ABORT_QDN_INVALID_CHECK_CONSTRAINT_EXPRESSION` | Invalid `CHECK` expression; revise expression. |
| `ERR-31392` / `0x31392 (201618)` | `qpERR_ABORT_QDN_VIOLATE_CHECK_CONSTRAINT` | Existing or incoming rows violate `CHECK`; inspect related rows. |
| `ERR-31076` / `0x31076 (200822)` | `qpERR_ABORT_QMX_CHILD_EXIST` | Child records exist; check referential constraints before parent update/delete. |
| `ERR-31077` / `0x31077 (200823)` | `qpERR_ABORT_QMX_NOT_FOUND_PARENT_ROW` | Parent row not found; insert or correct parent key before child DML. |
| `ERR-313FB` / `0x313FB (201723)` | `qpERR_ABORT_QDN_NOT_SUPPORT_CONSTRAINT_IN_COMPRESSED_COLUMN` | Primary key, unique key, or timestamp constraint is not allowed on compressed column. |
| `ERR-31415` / `0x31415 (201749)` | `qpERR_ABORT_QDN_NOT_ALLOW_MEM_TBS_PK_UK_OF_GLOBAL_INDEX` | Primary/unique key constraint must match the non-partitioned-index and disk-partitioned-table rule. |

Applies To: primary keys, unique keys, local unique keys, foreign keys, `CHECK`, `NOT NULL`, timestamp constraints, key/index column-count limits, compressed columns, DML referential checks, and unique-index enforcement.

Symptom: DDL cannot create, alter, or drop a constraint, or DML cannot insert/update/delete rows because key or referential rules are violated.

Primary Causes: duplicate key values, duplicate constraint names, missing referenced key, incompatible referencing/referenced column types, mismatched column count, adding `NOT NULL` without default or with existing nulls, using disallowed expressions in `CHECK`, referencing LOB columns in `CHECK`, defining foreign keys on temporary tables, or DML order violating parent-child relationships.

Immediate Action: Identify whether the error is definition-time or data-time. For definition-time errors, inspect constraint and column metadata before generating `ALTER TABLE`. For data-time errors, inspect the offending key values and fix DML order or data; do not drop constraints as a first response.

Check SQL or Command:

```sql
SELECT cs.constraint_name,
       cs.constraint_type,
       cs.index_id,
       cs.column_cnt,
       cs.referenced_table_id,
       cs.delete_rule,
       cs.check_condition,
       cs.validated
FROM SYSTEM_.SYS_CONSTRAINTS_ cs,
     SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_USERS_ u
WHERE cs.user_id = t.user_id
  AND cs.table_id = t.table_id
  AND t.user_id = u.user_id
  AND u.user_name = '<OWNER_NAME>'
  AND t.table_name = '<TABLE_NAME>'
ORDER BY cs.constraint_name;

-- Standalone unique indexes can also raise unique violations.
SELECT i.index_name,
       i.index_id,
       i.is_unique,
       i.column_cnt,
       ic.index_col_order,
       c.column_name,
       ic.sort_order
FROM SYSTEM_.SYS_INDICES_ i,
     SYSTEM_.SYS_INDEX_COLUMNS_ ic,
     SYSTEM_.SYS_COLUMNS_ c,
     SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_USERS_ u
WHERE i.user_id = ic.user_id
  AND i.index_id = ic.index_id
  AND i.table_id = ic.table_id
  AND ic.user_id = c.user_id
  AND ic.table_id = c.table_id
  AND ic.column_id = c.column_id
  AND i.user_id = t.user_id
  AND i.table_id = t.table_id
  AND t.user_id = u.user_id
  AND u.user_name = '<OWNER_NAME>'
  AND t.table_name = '<TABLE_NAME>'
  AND i.is_unique = 'T'
ORDER BY i.index_name, ic.index_col_order;
```

Required Customer Input: exact version, full error line, failed DDL or DML, owner/table/constraint/index names, key column list, sample offending key value if safe to share, and whether replication is involved.

Version Cautions: The listed codes are present in the checked Korean 7.1, 7.3, and Altibase 8.1 verified source Error Message References. Replication conflicts require replication-specific checks before changing rows or constraints.

Related Document: SQL DDL Generation; SQL DML and Oracle Compatibility; Data Dictionary and Performance Views; Replication HA CDC.

### Error Block: Data Type, Conversion, Literal, Numeric, and Date Errors

Error Codes: listed individually in the exact code map below.

Module / Severity: MT / `ABORT`.

Exact code map:

| Runtime / reference code | Reference symbol | Source message or action focus |
| --- | --- | --- |
| `ERR-2100C` / `0x2100C (135180)` | `mtERR_ABORT_CONVERSION_NOT_APPLICABLE` | Conversion not applicable; check source and target data types. |
| `ERR-2100D` / `0x2100D (135181)` | `mtERR_ABORT_INVALID_LENGTH` | Invalid data type length; check declared length. |
| `ERR-2100E` / `0x2100E (135182)` | `mtERR_ABORT_INVALID_PRECISION` | Invalid precision; check precision limit. |
| `ERR-2100F` / `0x2100F (135183)` | `mtERR_ABORT_INVALID_SCALE` | Invalid scale; check scale relative to precision. |
| `ERR-21010` / `0x21010 (135184)` | `mtERR_ABORT_VALUE_OVERFLOW` | Value overflow; reduce value or widen target type when valid. |
| `ERR-21011` / `0x21011 (135185)` | `mtERR_ABORT_INVALID_LITERAL` | Invalid literal; check literal syntax and target type. |
| `ERR-21016` / `0x21016 (135190)` | `mtERR_ABORT_DIVIDE_BY_ZERO` | Division by zero; correct expression or input data. |
| `ERR-21017` / `0x21017 (135191)` | `mtERR_ABORT_ARGUMENT_NOT_APPLICABLE` | Function argument is not applicable; check function signature and argument type. |
| `ERR-21020` / `0x21020 (135200)` | `mtERR_ABORT_INVALID_LITERAL_AFTER_ESCAPE` | Missing or invalid literal after escape character; check escaped string. |
| `ERR-21021` / `0x21021 (135201)` | `mtERR_ABORT_INVALID_ESCAPE` | Invalid escape literal; check escape character usage. |
| `ERR-21022` / `0x21022 (135202)` | `mtERR_ABORT_INVALID_DATE` | Invalid date literal; check date value. |
| `ERR-21023` / `0x21023 (135203)` | `mtERR_ABORT_INVALID_YEAR` | Year is invalid or out of range. |
| `ERR-21024` / `0x21024 (135204)` | `mtERR_ABORT_INVALID_MONTH` | Month must be `1` through `12`. |
| `ERR-21025` / `0x21025 (135205)` | `mtERR_ABORT_INVALID_DAY` | Day of month is invalid. |
| `ERR-21026` / `0x21026 (135206)` | `mtERR_ABORT_INVALID_HOUR` | Hour must be in the supported range. |
| `ERR-21027` / `0x21027 (135207)` | `mtERR_ABORT_INVALID_MINUTE` | Minute must be `0` through `59`. |
| `ERR-21028` / `0x21028 (135208)` | `mtERR_ABORT_INVALID_SECOND` | Second must be `0` through `59`. |
| `ERR-21029` / `0x21029 (135209)` | `mtERR_ABORT_INVALID_MICROSECOND` | Microsecond must be `0` through `999999`. |
| `ERR-21032` / `0x21032 (135218)` | `mtERR_ABORT_DATE_NOT_ENOUGH_INPUT` | Input literal is too short for the date format. |
| `ERR-21033` / `0x21033 (135219)` | `mtERR_ABORT_DATE_NOT_ENOUGH_FORMAT` | Date format ends before the whole input is converted. |
| `ERR-21034` / `0x21034 (135220)` | `mtERR_ABORT_DATE_INVALID_HOUR24` | 24-hour value must be `0` through `23`. |
| `ERR-21038` / `0x21038 (135224)` | `mtERR_ABORT_DATE_LITERAL_MISMATCH` | Input literal characters do not match the format string. |
| `ERR-21039` / `0x21039 (135225)` | `mtERR_ABORT_DATE_NOT_RECOGNIZED_FORMAT` | Date format was not recognized; check format model. |
| `ERR-2103A` / `0x2103A (135226)` | `mtERR_ABORT_DATE_NON_NUMERIC_INPUT` | Non-numeric character appeared where numeric date input was expected. |
| `ERR-21047` / `0x21047 (135239)` | `mtERR_ABORT_NULL_VALUE` | `NULL` value is not allowed for the data type. |
| `ERR-21048` / `0x21048 (135240)` | `mtERR_ABORT_OVERFLOW` | Value is out of range for the supported type. |
| `ERR-21049` / `0x21049 (135241)` | `mtERR_ABORT_INVALID_NUMERIC` | String cannot be cast to `INTEGER`; check numeric text and bind type. |

Applies To: explicit casts, implicit conversions, literals, date/time format models, function arguments, arithmetic expressions, `INSERT`, `UPDATE`, client bind values, and SQL generated by tools.

Symptom: Altibase cannot convert a value to the target type, parse a literal, fit a value into target precision/scale/range, or parse a date/time input.

Primary Causes: incompatible source and target types, invalid literal syntax, value overflow, invalid precision/scale/length, invalid function argument, invalid date format model, date part out of range, or client bind metadata not matching the target column.

Immediate Action: Check the source value, target column type, precision, scale, nullability, function signature, and bind type. Reproduce with one literal or bind at a time before changing table definitions.

Check SQL or Command:

```sql
SELECT c.column_name,
       c.data_type,
       c.precision,
       c.scale,
       c.is_nullable
FROM SYSTEM_.SYS_COLUMNS_ c,
     SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_USERS_ u
WHERE c.user_id = t.user_id
  AND c.table_id = t.table_id
  AND t.user_id = u.user_id
  AND u.user_name = '<OWNER_NAME>'
  AND t.table_name = '<TABLE_NAME>'
ORDER BY c.column_order;

-- Reproduce date parsing with one literal at a time.
SELECT TO_DATE('<DATE_TEXT>', '<FORMAT_MODEL>')
FROM DUAL;
```

Required Customer Input: exact version, full SQL or client bind call, target table definition, literal value or sanitized sample, client/tool name, NLS/date format assumptions, and full error line.

Version Cautions: The listed non-JSON MT codes are present in the checked Korean 7.1, 7.3, and Altibase 8.1 verified source Error Message References. JSON and Temporary LOB conversion errors are 8.1-sensitive; use the JSON blocks below for JSON-specific messages.

Related Document: Data Types and Properties; SQL DML and Oracle Compatibility; C CLI ODBC Precompiler.

### Error Block: Regular Expression Pattern and PCRE2 Errors

Error Codes: listed individually in the exact code map below.

Module / Severity: MT / `ABORT`.

Exact code map:

| Runtime / reference code | Reference symbol | Source message or action focus |
| --- | --- | --- |
| `ERR-2104D` / `0x2104D (135245)` | `mtERR_ABORT_WRONG_PATTERN` | Invalid pattern string; check regular-expression syntax. |
| `ERR-21052` / `0x21052 (135250)` | `mtERR_ABORT_LONG_PATTERN` | Pattern string is too long; shorten pattern. |
| `ERR-21053` / `0x21053 (135251)` | `mtERR_ABORT_REGEXP_REQUIRED_PAREN` | Pattern requires parentheses, brackets, or braces. |
| `ERR-21054` / `0x21054 (135252)` | `mtERR_ABORT_REGEXP_CLASS_EMPTY` | Empty bracket class; fix character class. |
| `ERR-21055` / `0x21055 (135253)` | `mtERR_ABORT_REGEXP_CONST_OVERFLOW` | Pattern numeric range exceeds supported range; reduce numeric quantifier. |
| `ERR-21056` / `0x21056 (135254)` | `mtERR_ABORT_REGEXP_REQUIRED_NUMBER` | Quantifier requires numeric values; fix `{m}`, `{m,}`, or `{m,n}`. |
| `ERR-21057` / `0x21057 (135255)` | `mtERR_ABORT_REGEXP_REQUIRED_COMMA` | Braces or comma are required; fix quantifier syntax. |
| `ERR-21058` / `0x21058 (135256)` | `mtERR_ABORT_REGEXP_UNEXPECTED_CAHR` | Pattern contains an unexpected character; check syntax near that character. |
| `ERR-21059` / `0x21059 (135257)` | `mtERR_ABORT_REGEXP_UNFINISHED_RANGE` | Character range is unfinished; close the range. |
| `ERR-2105A` / `0x2105A (135258)` | `mtERR_ABORT_REGEXP_INVALID_RANGE` | Character range is invalid; check range bounds. |
| `ERR-2105B` / `0x2105B (135259)` | `mtERR_ABORT_REGEXP_CLASS_INVALID_CHAR` | Invalid predefined character class; use supported class syntax. |
| `ERR-2105C` / `0x2105C (135260)` | `mtERR_ABORT_REGEXP_LONG_PATTERN` | Pattern size exceeds `1024`; shorten pattern. |
| `ERR-2106B` / `0x2106B (135275)` | `mtERR_ABORT_PCRE2_NOT_SUPPORTED_ENCODING` | `REGEXP_MODE=1` uses PCRE2 and current server character set is not supported by PCRE2. |
| `ERR-2106C` / `0x2106C (135276)` | `mtERR_ABORT_PCRE2_UNEXPECTED_ERROR` | PCRE2 returned an unexpected detail error; collect detail text and context. |

Applies To: regular expression functions and pattern processing, especially when `REGEXP_MODE=1`.

Symptom: A regular expression statement fails during pattern parsing or PCRE2 execution.

Primary Causes: invalid pattern syntax, too-long pattern, invalid or unfinished character class/range, unsupported quantifier form, unsupported PCRE2 server character set, or PCRE2 runtime error.

Immediate Action: Test the smallest pattern that reproduces the failure. For `0x2106B`, check `REGEXP_MODE` and server character set before considering a property change or database recreation. For `0x2106C`, preserve the PCRE2 detail text and collect trace context before escalating.

Check SQL or Command:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'REGEXP_MODE';
```

Required Customer Input: exact version, server character set, `REGEXP_MODE`, SQL text, pattern text, input sample, and the complete error line including PCRE2 detail text.

Version Cautions: The listed regex and PCRE2 codes are present in the checked Korean 7.1, 7.3, and Altibase 8.1 verified source Error Message References. Do not recommend database recreation for character-set changes without explicit DBA approval and a migration plan.

Related Document: SQL DML and Oracle Compatibility; Data Types and Properties.

### Error Block: DDL Blocked by Temporary Table in Use

Error Code: `ERR-31363` / `0x31363 (201571)`.

Reference Symbol: `qpERR_ABORT_QDB_TEMPORARY_TABLE_DDL_DISABLE`.

Module / Severity: QP / `ABORT`.

Message: `Cannot execute DDL when a temporary table is in use.`

Applies To: DDL on an object that has active temporary table usage.

Symptom: DDL fails while one or more related temporary tables are in use.

Primary Causes: Temporary tables based on the target table are active in a session.

Immediate Action: Identify the related temporary table usage. The primary source action is to truncate all temporary tables based on the target table and retry. Ending a session or transaction is an operational fallback only after owner/session confirmation and impact review.

Check SQL or Command:

```sql
SELECT u.user_name,
       t.table_name,
       t.temporary,
       t.tbs_name
FROM SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_USERS_ u
WHERE t.user_id = u.user_id
  AND u.user_name = '<OWNER_NAME>'
  AND t.table_name = '<TABLE_NAME>';
```

Version Cautions: The same runtime code appears in 7.1, 7.3, and 8.1.

Diagnostic caution: Do not invent a session-kill query for this error unless the target version source provides a supported way to identify the temporary table and owning session.

Escalation: If the blocking session or temporary table cannot be identified from dictionary checks and trace logs, collect the exact DDL, owner and object name, active session list, and version before escalating.

Related Document: Administration and Operations; SQL DDL Generation.

### Error Block: LOB DDL, Locator, Client, and Utility Errors

Error Codes: listed individually in the exact code map below.

Module / Severity: SM, QP, CLI/ODBC, APRE, or Utilities / `ABORT`, with noted CLI fatal locator-state entries.

Exact code map:

| Runtime / reference code | Reference symbol | Source message or action focus |
| --- | --- | --- |
| `ERR-110C4` / `0x110C4 (69828)` | `smERR_ABORT_CannotSpanTransByLobLocator` | `LobLocator` cannot span transaction; reopen locator in the current transaction. |
| `ERR-110C5` / `0x110C5 (69829)` | `smERR_ABORT_LobCursorClosed` | LOB cursor is already closed; reopen cursor before use. |
| `ERR-110C6` / `0x110C6 (69830)` | `smERR_ABORT_CanNotModifyLob` | Cannot modify LOB through a read-only LOB cursor. |
| `ERR-110C8` / `0x110C8 (69832)` | `smERR_ABORT_overflowLobCursorID` | Too many LOB cursors opened; close LOB cursors. |
| `ERR-110CB` / `0x110CB (69835)` | `smERR_ABORT_RangeError` | LOB operation range is outside target range; check offset and length. |
| `ERR-110CC` / `0x110CC (69836)` | `smERR_ABORT_LobCursorTooOld` | LOB cursor became too old after another update; reopen the LOB cursor. |
| `ERR-110CD` / `0x110CD (69837)` | `smERR_ABORT_InvalidLobStartOffset` | LOB start offset is greater than current LOB length; check offset. |
| `ERR-110D0` / `0x110D0 (69840)` | `smERR_ABORT_MaxLobErrorSize` | LOB size is bigger than maximum LOB size; verify size. |
| `ERR-110D1` / `0x110D1 (69841)` | `smERR_ABORT_INVALIDE_LOB_CURSOR_MODE` | Read-only table cursor requires read-only LOB cursor. |
| `ERR-3134C` / `0x3134C (201548)` | `qpERR_ABORT_QMV_NOT_SUPPORT_LOB_COLUMN` | LOB column is not supported in `RETURNING INTO`; remove LOB columns from `RETURNING`. |
| `ERR-31382` / `0x31382 (201602)` | `qpERR_ABORT_QMV_NOT_ALLOW_PRIOR_LOB` | `PRIOR` is not supported with LOB columns; use a non-LOB column. |
| `ERR-31390` / `0x31390 (201616)` | `qpERR_ABORT_QDN_NOT_SUPPORT_LOB_COLUMN_IN_CHECK_CONSTRAINT` | LOB columns are not supported in `CHECK` constraints; remove LOB references. |
| `ERR-3139B` / `0x3139B (201627)` | `qpERR_ABORT_QDX_NOT_SUPPORT_LOB_COLUMN` | LOB column is not supported for function-based index; remove LOB expression. |
| `ERR-3145F` / `0x3145F (201823)` | `qpERR_ABORT_QMO_NOT_ALLOWED_LOB_FILTER` | LOB filter is not supported in the documented hierarchy/`SELECT FOR UPDATE` context. |
| `ERR-314B4` / `0x314B4 (201908)` | `qpERR_ABORT_QMX_LOB_AUTOCOMMIT_MODE` | SQL LOB operation cannot run in autocommit mode; turn off autocommit. |
| `ERR-50137` / `0x50137 (327991)` | `ulERR_FATAL_LOB_NOT_OPENED` | CLI LOB locator operation was attempted when locator was not open; collect client trace. |
| `ERR-50139` / `0x50139 (327993)` | `ulERR_FATAL_LOB_INVALID_STATE` | CLI LOB function called in invalid state; collect client trace. |
| `ERR-5112C` / `0x5112C (332076)` | `ulERR_ABORT_LOB_AUTOCOMMIT_MODE_ERR` | CLI/ODBC LOB operation cannot run in autocommit mode; turn off autocommit. |
| `ERR-5112D` / `0x5112D (332077)` | `ulERR_ABORT_LOB_FILE_WRITE_ERR` | Failed to write LOB data to file; check file path and write permission. |
| `ERR-5112E` / `0x5112E (332078)` | `ulERR_ABORT_LOB_FILE_READ_ERR` | Failed to read from file; check file path and read permission. |
| `ERR-5113C` / `0x5113C (332092)` | `ulERR_ABORT_INVALID_APP_BUFFER_TYPE_LOB` | Invalid application buffer type for LOB source; check bind buffer type. |
| `ERR-51140` / `0x51140 (332096)` | `ulERR_ABORT_INVALID_LOB_RANGE` | Invalid LOB range; check offset and length. |
| `ERR-51029` / `0x51029 (331817)` | `ulpERR_ABORT_COMP_Lob_Locator_Error` | Precompiler `FREE LOB` host variable must be a LOB locator. |
| `ERR-91022` / `0x91022 (593954)` | `utERR_ABORT_UNDISPLAYABLE_DATATYPE_Error` | Utility cannot display LOB or `GEOMETRY` data in console; use an appropriate client/export method. |
| `ERR-91041` / `0x91041 (593985)` | `utERR_ABORT_LOB_Opt_Str_Error` | Missing or invalid LOB option string; check utility LOB option syntax. |
| `ERR-91045` / `0x91045 (593989)` | `utERR_ABORT_LOB_File_IO_Error` | LOB file I/O error; check path, existence, space, and permissions. |
| `ERR-91101` / `0x91101 (594177)` | `utERR_ABORT_LOB_AUTOCOMMIT_MODE_ERR` | Utility LOB operation cannot run with autocommit on; turn off autocommit. |

Applies To: ordinary `BLOB`/`CLOB` table columns, SQL LOB locators/cursors, `RETURNING INTO`, `CHECK`, function-based index expressions, CLI/ODBC LOB APIs, Precompiler `FREE LOB`, iSQL/iLoader/utility LOB file handling, and LOB display limitations.

Symptom: LOB read/write, locator use, DDL, DML, index/check expression, client API, or utility file processing fails.

Primary Causes: autocommit ended the locator transaction scope, LOB cursor was closed/old/read-only, offset or length was invalid, LOB exceeded size limits, LOB was used in an unsupported SQL construct, utility file path/permission/space failed, or client buffer/locator state was invalid.

Immediate Action: For locator/API errors, turn off autocommit and keep the whole LOB operation inside one explicit transaction. For SQL-shape errors, remove LOB columns from unsupported expressions (`CHECK`, function-based index, `RETURNING INTO`, `PRIOR`, LOB filter). For utility file errors, verify path, permission, file size, and free space.

Check SQL or Command:

```sql
AUTOCOMMIT OFF;
-- Execute LOB read or write operation here.
COMMIT;

SELECT c.column_name,
       c.data_type,
       c.precision,
       c.scale,
       c.store_type
FROM SYSTEM_.SYS_COLUMNS_ c,
     SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_USERS_ u
WHERE c.user_id = t.user_id
  AND c.table_id = t.table_id
  AND t.user_id = u.user_id
  AND u.user_name = '<OWNER_NAME>'
  AND t.table_name = '<TABLE_NAME>'
ORDER BY c.column_order;
```

```bash
ls -l '<LOB_FILE_PATH>'
df -k '<LOB_FILE_DIRECTORY>'
```

Required Customer Input: exact version and client/tool version, full error line, failed SQL/API/utility command, autocommit state, transaction boundary, LOB column names and types, locator lifecycle, file path, OS error if present, and client or utility trace output.

Version Cautions: The listed non-JSON LOB codes are present in the checked Korean 7.1, 7.3, and Altibase 8.1 verified source Error Message References except `0x314B4`, which is documented in the checked Korean 7.3 and Altibase 8.1 verified source. Treat SQL-level `0x314B4` as 7.3/8.1 unless the target 7.1 runtime shows that exact code. For 8.1 JSON and Temporary LOB, also check `TEMPORARY_LOB_ENABLE`.

Escalation: Escalate CLI fatal locator-state entries such as `0x50137` or `0x50139` after collecting client version, API call sequence, locator open/free sequence, autocommit state, and trace output.

Related Document: Data Types and Properties; C CLI ODBC Precompiler; iSQL iLoader Basic Tools; Utilities Operation Tools.

### Error Block: JSON Type Cannot Be Used Because Temporary LOB Is Disabled

Error Code: `0x2106D (135277)`.

Reference Symbol: `mtERR_ABORT_JSON_WITHOUT_TEMPLOB`.

Module / Severity: MT / `ABORT`.

Message: `JSON type cannot be used when the TEMPORARY_LOB_ENABLE property is disabled.`

Applies To: Altibase 8.1 JSON usage.

Symptom: JSON SQL or JSON type handling fails immediately.

Primary Causes: `TEMPORARY_LOB_ENABLE` is disabled.

Immediate Action: Check whether `TEMPORARY_LOB_ENABLE` is enabled and apply the documented property change procedure for the target environment.

Check SQL or Command:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name IN (
  'TEMPORARY_LOB_ENABLE',
  'MEMORY_TEMPLOB_MAX_ALLOC_SIZE',
  'MEMORY_TEMPLOB_PIECE_SIZE'
)
ORDER BY name;
```

Version Cautions: Treat this as 8.1-specific unless the user proves the same feature exists in their target version.

Related Document: Data Types and Properties; SQL DML and Oracle Compatibility.

### Error Block: JSON Function Return or Path Error

Error Codes: listed individually in the exact code map below.

Module / Severity: QP / `ABORT`.

Exact code map:

| Runtime / reference code | Reference symbol | Exact message | Cause / action focus |
| --- | --- | --- | --- |
| `ERR-314BC` / `0x314BC (201916)` | `qpERR_ABORT_JSON_INVALID_TYPE` | `Unsupported data type for the returned value.` | Check the JSON function `RETURNING` type. |
| `ERR-314BD` / `0x314BD (201917)` | `qpERR_ABORT_JSON_NUMBER_OVERFLOW` | `The returned number value exceeds the minimum or maximum limits.` | Check returned numeric range and `RETURNING` type. |
| `ERR-314BE` / `0x314BE (201918)` | `qpERR_ABORT_JSON_EXCEEDED_OBJECT_MAX_DEPTH` | `The JSON object exceeds the maximum depth (<0%d>).` | Check JSON data depth. |
| `ERR-314BF` / `0x314BF (201919)` | `qpERR_ABORT_JSON_EMPTY_RESULTS` | `No results were found.` | Check the JSON path expression. |
| `ERR-314C0` / `0x314C0 (201920)` | `qpERR_ABORT_JSON_WRAPPER_IS_NEEDED` | `An array wrapper is required.` | Use the array wrapper option when multiple results are possible. |
| `ERR-314C1` / `0x314C1 (201921)` | `qpERR_ABORT_JSON_DEFAULT_VALUE_TOO_LONG` | `The default value exceeds the maximum length.` | Check the default value and `RETURNING` type. |
| `ERR-314C2` / `0x314C2 (201922)` | `qpERR_ABORT_JSON_INVALID_KEY_TYPE` | `Invalid date type for key.` | Check the JSON object key value type. |
| `ERR-314C3` / `0x314C3 (201923)` | `qpERR_ABORT_JSON_OBJECT_INCOMPLETE` | `Invalid key-value pair for the JSON_OBJECT function.` | Check `JSON_OBJECT` key-value arguments. |
| `ERR-314C4` / `0x314C4 (201924)` | `qpERR_ABORT_JSON_TEXT_OVERFLOW` | `The returned text value exceeds the maximum limits.` | Check returned text length and `RETURNING` type. |
| `ERR-314C5` / `0x314C5 (201925)` | `qpERR_ABORT_JSON_INVALID_JSON_PATH` | `JSON path syntax error. <0%s>` | Check JSON path syntax. |
| `ERR-314C6` / `0x314C6 (201926)` | `qpERR_ABORT_JSON_INVALID_JSON_DATA` | `Invalid JSON data. <0%s>` | Validate the JSON data. |
| `ERR-314C7` / `0x314C7 (201927)` | `qpERR_ABORT_JSON_INAPPROPRIATE_JSON_PATH_VALUE` | `The JSON path expression cannot be null or non-literal value.` | Use a non-null literal JSON path expression. |
| `ERR-314C8` / `0x314C8 (201928)` | `qpERR_ABORT_JSON_MULTIPLE_RESULTS` | `JSON function returns multiple results.` | Check path selectivity or wrapper options. |
| `ERR-314C9` / `0x314C9 (201929)` | `qpERR_ABORT_JSON_FAILED_TO_CONVERT_NUMERIC` | `Unable to convert the value to the numeric type.` | Check numeric format and `RETURNING` type. |
| `ERR-314CA` / `0x314CA (201930)` | `qpERR_ABORT_JSON_RETURNS_NON_SCALAR_VALUE` | `JSON function returns non-scalar values.` | Check path result shape and scalar-return expectations. |

Message Summary: JSON function returned an unsupported type, overflowed, exceeded maximum object depth, found no result, required an array wrapper, received invalid JSON data, received an invalid JSON path, returned multiple results, failed numeric conversion, or returned non-scalar values.

Applies To: Altibase 8.1 JSON functions and JSON path processing.

Symptom: JSON SQL fails during return value processing, path evaluation, or JSON data validation.

Primary Causes: Invalid JSON data, invalid JSON path expression, multiple path matches without wrapper, wrong `RETURNING` type, returned value too long, numeric overflow, non-scalar result, or invalid `JSON_OBJECT` key-value arguments.

Immediate Action: Validate the JSON data, path expression, `RETURNING` clause, wrapper option, and default value. For numeric returns, verify range and format.

Check SQL or Command:

```sql
-- Keep JSON path expressions literal and test one expression at a time.
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'TEMPORARY_LOB_ENABLE';
```

Version Cautions: These JSON error blocks are based on Altibase 8.1 verified source. Do not apply them to 7.1 or 7.3 unless the user confirms equivalent JSON support.

Related Document: SQL DML and Oracle Compatibility; Data Types and Properties.

### Error Block: Replication Socket Read or Write Failure

Error Code: `0x61003 (397315)`, `0x61004 (397316)`.

Reference Symbol: `rpERR_ABORT_RP_READ_SOCKET`, `rpERR_ABORT_RP_WRITE_SOCKET`.

Module / Severity: RP / `ABORT`.

Message: `Unable to read from a socket` or `Unable to write to a socket`.

Applies To: replication sender and receiver network I/O.

Symptom: Replication disconnects or fails to transfer data.

Primary Causes: Network error, peer server down, timeout, firewall, wrong port, or remote replication process failure.

Immediate Action: Check local and remote `altibase_rp.log`, network connectivity, peer server status, replication timeout properties, and replication gap.

Check SQL or Command:

```bash
tail -200 "$ALTIBASE_HOME/trc/altibase_rp.log"
```

```sql
SELECT rep_name,
       status,
       sender_ip,
       sender_port,
       peer_ip,
       peer_port,
       net_error_flag
FROM V$REPSENDER
ORDER BY rep_name;

SELECT rep_name,
       my_ip,
       my_port,
       peer_ip,
       peer_port,
       apply_xsn,
       insert_failure_count,
       update_failure_count,
       delete_failure_count
FROM V$REPRECEIVER
ORDER BY rep_name;
```

Version Cautions: Applies across 7.1, 7.3, and 8.1. For 8.1 replication SSL, also check SSL blocks and replication SSL settings.

Related Document: Replication HA CDC; Security SSL TLS.

### Error Block: Replication Handshake or Sender Start Failure

Error Code: `0x6100D (397325)`, `0x61010 (397328)`, `0x6102D (397357)`.

Reference Symbol: `rpERR_ABORT_RP_SENDER_HANDSHAKE`, `rpERR_ABORT_RP_SENDER_START`, `rpERR_ABORT_LISTEN`.

Module / Severity: RP / `ABORT`.

Message: `[Sender] Failed to handshake with the peer server`, `[Sender] Failed to start the sender thread`, or `[Receiver] Failed to listen to a replication socket`.

Applies To: replication startup, sender/receiver connection, and replication socket listener.

Symptom: Replication cannot start or cannot connect to the peer.

Primary Causes: Network or server error, mismatched replication definitions, peer database down, `REPLICATION_PORT_NO` occupied, or wrong IP and port.

Immediate Action: Verify both replication definitions, peer server status, `REPLICATION_PORT_NO`, and whether another process uses the port.

Check SQL or Command:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name IN ('REPLICATION_PORT_NO', 'REPLICATION_RECEIVE_TIMEOUT');

SELECT rep_name,
       status,
       sender_ip,
       sender_port,
       peer_ip,
       peer_port,
       net_error_flag
FROM V$REPSENDER
ORDER BY rep_name;
```

Version Cautions: For SSL replication in 8.1, verify SSL configuration on both peers.

Related Document: Replication HA CDC; Security SSL TLS.

### Error Block: Duplicate Replication Name or Endpoint

Error Code: `0x61100 (397568)`.

Reference Symbol: `rpERR_ABORT_RPC_DUPLICATE_REPLICATION`.

Module / Severity: RP / `ABORT`.

Message: `Duplicate replication names. The replication name already exists in the database.`

Applies To: `CREATE REPLICATION`.

Symptom: A replication definition cannot be created.

Primary Causes: The replication name already exists, or the IP address and port number are not unique.

Immediate Action: Use a different replication name or remove the existing definition after impact review.

Check SQL or Command:

```sql
-- Primary check: replication definitions, including stopped or not-yet-started objects.
SELECT replication_name, is_started, repl_mode, role
FROM SYSTEM_.SYS_REPLICATIONS_
WHERE replication_name = '<REPLICATION_NAME>'
ORDER BY replication_name;

SELECT replication_name, host_ip, port_no, conn_type
FROM SYSTEM_.SYS_REPL_HOSTS_
WHERE replication_name = '<REPLICATION_NAME>'
   OR (host_ip = '<PEER_HOST>' AND port_no = <PEER_PORT>)
ORDER BY replication_name, host_ip, port_no;

-- Secondary runtime check after a definition is known to exist.
SELECT rep_name, status, sender_ip, sender_port, peer_ip, peer_port, net_error_flag
FROM V$REPSENDER
WHERE rep_name = '<REPLICATION_NAME>'
ORDER BY rep_name;

SELECT rep_name, rep_gap, rep_gap_size
FROM V$REPGAP
WHERE rep_name = '<REPLICATION_NAME>'
ORDER BY rep_name;
```

Version Cautions: Applies across 7.1, 7.3, and 8.1.

Related Document: Replication HA CDC; SQL DDL Generation.

### Error Block: Client SSL Configuration Failure

Error Code: `0x5120C (332300)`, `0x5120D (332301)`, `0x5120E (332302)`, `0x5121D (332317)`, `0x5121E (332318)`.

Module / Severity: CLI/ODBC / `ABORT`.

Exact code map:

| Runtime / reference code | Reference symbol | Exact message | Action focus |
| --- | --- | --- | --- |
| `ERR-5120C` / `0x5120C (332300)` | `ulERR_ABORT_SSL_OPERATION_FAILURE` | `SSL operation failure. <0%s>` | Check the detailed SSL error text. |
| `ERR-5120D` / `0x5120D (332301)` | `ulERR_ABORT_SSL_LIBRARY_ERROR` | `Failed to load the OpenSSL library - <0%s>` | Check whether the OpenSSL library is installed and configured. |
| `ERR-5120E` / `0x5120E (332302)` | `ulERR_ABORT_SSL_LINK_FAILURE` | `SSL link failure. <0%s>` | Check the detailed SSL link error code. |
| `ERR-5121D` / `0x5121D (332317)` | `ulERR_ABORT_INVALID_ALTIBASE_SSL_PORT_NO` | `Connection string does not have PORT_NO, and environment variable ALTIBASE_SSL_PORT_NO does not have a valid value : <0%s>.` | Set `ALTIBASE_SSL_PORT_NO` correctly or specify `PORT_NO` in the connection string. |
| `ERR-5121E` / `0x5121E (332318)` | `ulERR_ABORT_PORT_NO_ALTIBASE_SSL_PORT_NO_NOT_SET` | `Neither PORT_NO in the connection string nor the ALTIBASE_SSL_PORT_NO environment variable has been set.` | Set `PORT_NO` in the connection string or set `ALTIBASE_SSL_PORT_NO`. |

Message Summary: SSL operation failure, failed to load OpenSSL library, SSL link failure, invalid `ALTIBASE_SSL_PORT_NO`, or missing SSL port.

Applies To: CLI, ODBC, and client connection strings using SSL.

Symptom: Client cannot establish SSL connection.

Primary Causes: OpenSSL library not installed or not found, SSL operation failure, SSL port omitted, invalid `ALTIBASE_SSL_PORT_NO`, or connection string missing `PORT_NO`.

Immediate Action: Set `PORT_NO` in the connection string or set `ALTIBASE_SSL_PORT_NO`, verify OpenSSL library installation, and check detailed client error text.

Check SQL or Command:

```bash
echo "$ALTIBASE_SSL_PORT_NO"
altibase -v
```

Version Cautions: 7.1, 7.3, and 8.1 sources include SSL client errors. Confirm client library version matches server expectations.

Escalation: If the client library, OpenSSL library, `PORT_NO`, and `ALTIBASE_SSL_PORT_NO` are correct but the connection still fails, collect the client trace, detailed OpenSSL error text, server version, client version, and connection string with secrets removed.

Related Document: Security SSL TLS; C CLI ODBC Precompiler.

### Error Block: Server SSL Certificate or Handshake Failure

Error Codes: listed individually in the exact code map below.

Module / Severity: CM / `ABORT`.

Exact code map:

| Runtime / reference code | Reference symbol | Exact message | Action focus |
| --- | --- | --- | --- |
| `ERR-710A0` / `0x710A0 (463008)` | `cmERR_ABORT_INVALID_CERTIFICATE` | `Failed to load a certificate. SSL error: <0%s>` | Check the certificate file and location. |
| `ERR-710A1` / `0x710A1 (463009)` | `cmERR_ABORT_INVALID_PRIVATE_KEY` | `Failed to load a private key. SSL error: <0%s>` | Check the private key file and location. |
| `ERR-710A2` / `0x710A2 (463010)` | `cmERR_ABORT_PRIVATE_KEY_VERIFICATION` | `Failed to verify the private key. SSL error: <0%s>` | Check whether the private key matches the certificate. |
| `ERR-710A3` / `0x710A3 (463011)` | `cmERR_ABORT_SSL_HANDSHAKE` | `SSL handshake failed. SSL error: <0%s>` | Check `altibase_boot.log` for the detailed handshake failure. |
| `ERR-710A4` / `0x710A4 (463012)` | `cmERR_ABORT_SSL_READ` | `SSL read failed. SSL error: <0%s>` | Check `altibase_boot.log` for detailed SSL read failure text. |
| `ERR-710A5` / `0x710A5 (463013)` | `cmERR_ABORT_SSL_WRITE` | `SSL write failed. SSL error: <0%s>` | Check `altibase_boot.log` for detailed SSL write failure text. |
| `ERR-710A6` / `0x710A6 (463014)` | `cmERR_ABORT_SSL_SHUTDOWN` | `SSL shutdown failed. SSL error: <0%s>` | Check `altibase_boot.log` for detailed SSL shutdown failure text. |
| `ERR-710A7` / `0x710A7 (463015)` | `cmERR_ABORT_INVALID_VERIFY_LOCATION` | `Failed to load trusted certificates from the specified location(s). SSL error: <0%s>` | Check `CA` and `CAPath` property values. |
| `ERR-710A8` / `0x710A8 (463016)` | `cmERR_ABORT_INVALID_CA_LIST_FILE` | `Failed to load trusted certificates from the CA file. SSL error: <0%s>` | Check whether the CA file is valid. |
| `ERR-710A9` / `0x710A9 (463017)` | `cmERR_ABORT_SSL_CONNECT` | `SSL connect failed.` | Check `altibase_boot.log` for the detailed connect failure. |
| `ERR-710AA` / `0x710AA (463018)` | `cmERR_ABORT_VERIFY_PEER_CERITIFICATE` | `Failed to verify the peer certificate. SSL error: <0%s>` | Check whether the peer has a valid certificate. |
| `ERR-710AB` / `0x710AB (463019)` | `cmERR_ABORT_SSL_OPERATION` | `SSL operation failed. SSL error: <0%s>` | Check `altibase_boot.log` for detailed SSL operation failure text. |

Message Summary: SSL certificate, private key, CA, peer certificate, handshake, read, write, connect, shutdown, or operation failure.

Applies To: server-side SSL/TLS and communication module.

Symptom: SSL listener or SSL connection fails.

Primary Causes: Invalid certificate path, invalid private key path, private key does not match certificate, invalid CA path, peer certificate verification failure, or SSL handshake failure.

Immediate Action: Verify certificate, private key, CA file, CA path, and peer certificate. Check `altibase_boot.log` for detailed SSL error text.

Check SQL or Command:

```bash
tail -200 "$ALTIBASE_HOME/trc/altibase_boot.log"
```

Version Cautions: In 8.1 replication SSL cases, check both server SSL settings and replication SSL settings.

Related Document: Security SSL TLS; Replication HA CDC.

### Error Block: Unsupported OpenSSL Version

Error Code: `0x710CB (463051)`.

Reference Symbol: `cmERR_ABORT_UNSUPPORTED_OPENSSL_VERSION`.

Module / Severity: CM / `ABORT`.

Message: `Unsupported OpenSSL version (<0%s>)`.

Applies To: SSL/TLS startup or connection.

Symptom: SSL initialization fails because the OpenSSL version is unsupported.

Primary Causes: OpenSSL version does not match the supported library version for the Altibase build.

Immediate Action: Check whether the installed OpenSSL version is 3.x. Collect the Altibase patch level, platform, library path, and OpenSSL version before changing libraries.

Check SQL or Command:

```bash
openssl version
altibase -v
tail -200 "$ALTIBASE_HOME/trc/altibase_boot.log"
```

Version Cautions: Use this block for 7.3 and Altibase 8.1 verified source. Do not map a 7.1 SSL symptom to `0x710CB` unless the target 7.1 runtime shows that exact code.

Related Document: Security SSL TLS; Version Release Platform.

### Error Block: Shard Metadata or Shard Object Not Found

Error Code: `0xE1001 (921601)`, `0xE1003 (921603)`, `0xE1004 (921604)`, `0xE1065 (921701)`.

Reference Symbol: `sdERR_ABORT_SDM_SHARD_META_NOT_CREATED`, `sdERR_ABORT_SDM_SHARD_NODE_NOT_EXIST`, `sdERR_ABORT_SDM_SHARD_TABLE_NOT_EXIST`, `sdERR_ABORT_SDA_NOT_SUPPORTED_SQLTEXT_FOR_SHARD`.

Module / Severity: SD / `ABORT`.

Message: Shard metadata not created, shard data node not found, shard object not found, or SQL statement not supported in Altibase sharding.

Applies To: Altibase sharding metadata and shard SQL routing.

Symptom: Shard DDL or SQL fails because metadata, shard node, shard object, shard key, or supported SQL shape is missing or invalid.

Primary Causes: Shard metadata not initialized, wrong shard node name, wrong shard object name, unsupported statement for sharding, or invalid shard key condition.

Immediate Action: Verify shard metadata, shard node, object name, and whether the SQL statement is supported for sharding.

Check SQL or Command:

```bash
altibase -v
```

```sql
SELECT product_version, meta_version
FROM V$VERSION;
```

Version Cautions: `sdERR_*` coverage is confirmed in the 7.1 Error Message Reference. For 7.3 or 8.1 sharding errors, ask for the exact product version, patch level, full error line, and installed manual/runtime evidence before giving a definitive `sdERR_*` version claim. Sharding-related errors can also appear under other modules, so use the exact code first.

Related Document: SQL DDL Generation; Data Dictionary and Performance Views.

### Error Block: DB Link Configuration or Global Transaction Failure

Error Code: `0xC1005 (790533)`, `0xC1006 (790534)`, `0xC1007 (790535)`, `0xC1009 (790537)`, `0xC1030 (790576)`.

Reference Symbol: `dkERR_ABORT_DK_PARSING_DBLINK_CONF_FAILED`, `dkERR_ABORT_DK_OPEN_DBLINK_CONF_FAILED`, `dkERR_ABORT_DK_NO_HOME_DIRECTORY`, `dkERR_ABORT_DKM_GTX_PREPARE_PHASE_FAILED`, `dkERR_ABORT_DKT_GLOBAL_TX_NOT_PREPARED`.

Module / Severity: Database Link / `ABORT`.

Message: Cannot parse or open `dblink.conf`, `ALTIBASE_HOME` is not set, remote atomic transaction prepare failed, or global transaction not prepared to commit.

Applies To: DB Link and AltiLinker operations.

Symptom: DB Link setup, remote execution, or remote transaction processing fails.

Primary Causes: Invalid `dblink.conf`, missing `ALTIBASE_HOME`, network problem, protocol version inconsistency between Altibase and AltiLinker, or global transaction failure.

Immediate Action: Check `ALTIBASE_HOME`, `dblink.conf`, AltiLinker status, product versions, network, and trace log details.

Check SQL or Command:

```bash
echo "$ALTIBASE_HOME"
altibase -v
```

Version Cautions: DB Link behavior and supported remote features can vary by version and connector setup.

Related Document: DB Link and External Connectors.

## Topic Response Patterns

### Storage, Backup, Recovery, Datafile, Log, and Tablespace Errors

Use this order:

1. Identify the exact code, startup phase, database mode, affected file or tablespace, and whether the operation is normal DDL, online backup, restart recovery, complete media recovery, or incomplete media recovery.
2. Preserve current files before changing them. For recovery cases, do not delete logfiles, replace log anchors, run `RESETLOGS`, or discard a tablespace until the backup source and recovery target are known.
3. Check `V$LOG`, `V$ARCHIVE`, `V$TABLESPACES`, `V$DATAFILES`, `V$BACKUP_INFO`, checkpoint-path views, filesystem free space, permissions, and trace logs.
4. For `NOARCHIVELOG`, state that online backup and ordinary media recovery are not available; recovery is normally limited to offline backup restore or documented temporary-file recreation cases.
5. For incomplete recovery, state that `META RESETLOGS` and an immediate full backup are required after the recovery plan succeeds.
6. For tablespace DDL, choose the path for disk, memory, volatile, undo, temporary, or system tablespace rules before generating copy-ready SQL.

### Startup and Shutdown Errors

Use this order:

1. Identify exact error and startup phase.
2. Check `altibase_boot.log`.
3. Confirm `ALTIBASE_HOME`, ports, shared memory, semaphore, and file permissions.
4. For `FATAL` errors, avoid destructive recovery advice until backup and phase are known.
5. Return the standardized error block.

### SQL Execution Errors

Use this order:

1. Normalize error code.
2. Identify object names, owner, SQL type, and version.
3. Run object, column, constraint, privilege, and type checks.
4. Explain the corrected SQL or next diagnostic step.
5. Keep SQL identifiers literal in any answer language.

### Replication Errors

Use this order:

1. Identify local and remote Altibase versions.
2. Check `altibase_rp.log` on both nodes.
3. Check sender, receiver, and gap views.
4. Verify IP, port, replication name, table definitions, constraints, and SSL settings when applicable.
5. Avoid advising rebuild or reset until the replication mode and data consistency target are known.

### SSL Errors

Use this order:

1. Distinguish client SSL errors (`ulERR_*`) from server or communication module SSL errors (`cmERR_*`).
2. Check `PORT_NO`, `ALTIBASE_SSL_PORT_NO`, certificate paths, private key paths, CA file, CA path, and OpenSSL version.
3. For replication SSL, check both peer servers and the replication definition.
4. Include the detailed OpenSSL error text when present.

### JSON, Temporary LOB, and LOB Errors

Use this order:

1. Confirm version. JSON blocks in this attachment are 8.1-specific.
2. Check `TEMPORARY_LOB_ENABLE` for JSON and Temporary LOB behavior.
3. For LOB locator errors, check autocommit and transaction boundaries.
4. For JSON path errors, validate JSON data, JSON path expression, wrapper option, and `RETURNING` clause.

## Version Differences

- 7.1: Use 7.1 Error Message Reference wording when the customer reports a 7.1 system. Do not assume 8.1 JSON behavior.
- 7.3: Use 7.3 Error Message Reference wording when the customer reports a 7.3 system. SSL, regular expression, replication, and LOB errors should be checked against 7.3 wording.
- 8.1: Use Altibase 8.1 verified source for JSON, Temporary LOB, replication SSL, and current SSL/TLS behavior. JSON-specific error blocks such as `mtERR_ABORT_JSON_WITHOUT_TEMPLOB` and `qpERR_ABORT_JSON_*` are 8.1-sensitive. Do not treat `sdERR_*` as verified 8.1 coverage from this attachment alone; ask for exact installed-version evidence.

## Attachment Cross-References

- Use `02_administration_operations.md` when an error requires startup, shutdown, tablespace, backup, recovery, archive log, or media recovery action.
- Use `03_sql_ddl_generation.md` when the fix is corrected SQL syntax, object DDL, user or privilege DDL, queue DDL, or replication DDL.
- Use `06_data_dictionary_performance_views.md` for confirmation queries against objects, columns, constraints, privileges, sessions, locks, properties, and replication views.
- Use `08_performance_tuning_monitoring.md` when the reported error is coupled with slow SQL, lock waits, hangs, memory pressure, or plan instability.
- Use `09_replication_ha_cdc.md` for replication state, gap, conflict, failover, and Log Analyzer CDC troubleshooting after error normalization.
- Use `18_security_ssl_tls.md` for SSL/TLS listener, certificate, cipher, FIPS, client handshake, and replication SSL configuration checks.

## Residual Scope

- J023 expanded storage, backup, recovery, datafile, log, checkpoint, incremental backup, and tablespace exact-code maps from the selected 7.1, 7.3, and Altibase 8.1 verified source Error Message References. The maps are still grouped troubleshooting blocks, not a replacement for the complete source manuals.
- J024 expanded SQL parser, DDL, table/column/data type, constraint, regular-expression, JSON, LOB, Temporary LOB, and related client/utility LOB exact-code maps from the selected 7.1, 7.3, and Altibase 8.1 verified source Error Message References. JSON and Temporary LOB blocks remain 8.1-scoped.
- Add future error blocks only after source-backed review, and keep the standardized error format above.
- The full Error Message Reference is not yet converted into exact-code blocks. Future updates should use the inventory baseline and preserve the uncovered-code response rule for entries not yet consolidated here.
