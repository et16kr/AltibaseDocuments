# 00. Versions, Releases, and Supported Platforms

## Applicable Versions

- 7.1: Altibase 7.1 release notes and supported-platform guidance.
- 7.3: Altibase 7.3 release notes and supported-platform guidance.
- 8.1: Altibase 8.1 release notes and Altibase 8.1 verified source.

## Questions This File Can Answer

- What changed between Altibase 7.1, 7.3, and 8.1?
- Which release added `JSON`, Temporary LOB, KADA, Kafka connectors, ABM, replication SSL, JDBC 4.2, AKU, or OpenSSL 3.0.8?
- Is a server, client, library, or tool supported on a specific OS and CPU platform?
- What upgrade risks apply to database binary versions, metadata, client protocol, and replication protocol?
- What quick SQL should be used to check the running product version, meta version, protocols, and 8.1 feature properties?

## Source Documents

- Altibase 7.1 Release Notes.
- Altibase 7.3 Release Notes.
- Altibase 8.1 Release Notes.
- Altibase Supported Platforms by Version.
- Altibase 8.1 verified source.

## Core Guidance

- Always identify the customer's exact target version and patch level before answering a platform or upgrade question.
- If the customer does not specify a version, answer from the 8.1 baseline and explicitly say that 7.1 and 7.3 can differ.
- Keep SQL object names, function names, property names, commands, file names, error codes, and view names literal.
- Do not translate `JSON`, `V$TEMPORARY_LOBS`, `REPLICATION_SSL_PORT_NO`, `DBMS_METADATA`, `USING SSL`, or other database terms.
- For supported-platform answers, distinguish server support from client support. Windows x64 is client-only for the 7.1, 7.3, and 8.1 guidance in this attachment.
- For 7.1 and 7.3, the supported-platform document includes patch-level platform additions beyond the initial release notes. Mention the patch condition when one is listed.
- For 8.1, use the 8.1 release notes and Altibase 8.1 verified source. Do not infer support for platforms not listed there.
- For upgrade answers, use the compatibility section first, then list feature changes. A feature list alone is not enough for a migration answer.

## Quick Version Difference Summary

### Altibase 7.1

Release identity: Altibase 7.1.0.1.2 release notes state that 7.1.0.1.2 is the final 7.1 release line version and that maintenance starts from 7.1.0.1.2.

Main role in answers: established 7.x baseline with major SQL, replication, DBLink, PSM, tooling, and performance improvements over 6.5.1.

Major additions:

- SQL and table features: partition `CONJOIN` and `DISJOIN`, moving table tablespaces, hybrid partitioned tables, partition-level `COMPACT` and `AGING`, `NOWAIT` and `WAIT`, user-defined queue columns, table functions, additional aggregate and window functions, user lock functions, `SYS_CONTEXT`, encoding functions, pipe functions, `LOCK TABLE ... UNTIL NEXT DDL`, trigger `ENABLE` and `DISABLE`, `KEEP (DENSE_RANK FIRST|LAST ORDER BY)`, additional date format tokens, spatial `REVERSE` and `MAKEENVELOPE`, and numeric bit functions.
- Replication: relaxed replication table constraint matching, SQL apply mode with `REPLICATION_SQL_APPLY_ENABLE`, and DDL execution controls for replicated tables through `REPLICATION_DDL_ENABLE_LEVEL`.
- DBLink: two-phase commit level through `DBLINK_GLOBAL_TRANSACTION_LEVEL`, DBLink recovery and distributed-transaction views, and batch-oriented `REMOTE_*` functions for stored procedures.
- Development interfaces: PDO driver support and embedded SQL host array `FETCH` in a `FOR` clause.
- PSM and packages: `AUTHID`, `STANDARD`, `UTL_COPYSWAP`, `UTL_SMTP`, several `DBMS_*` and `UTL_*` packages, static SQL in cursor `OPEN FOR`, `BULK COLLECTION INTO`, `NOCOPY`, package subprogram overloading, PSM character precision properties, `PRAGMA AUTONOMOUS_TRANSACTION`, and `PRAGMA EXCEPTION_INIT`.
- Tools: JDBC Adapter, SQuirreL SQL integration, `altimon.sh` improvements, iSQL formatting commands, iLoader `-prefetch_rows`, partition information in `DESC`, `dataCompJ`, asynchronous prefetch, and aexport property additions.
- Performance and resources: disk buffer manager improvements, memory fetch improvements, result cache, automatic statistics, optimizer hints, delayed execution plan support, IPCDA on Linux for CLI/ODBC, access-list management, memory allocation improvements, thread reuse, startup index rebuild improvements, and memory index reorganization.

Important removals or discontinuations:

- The 7.1 release notes discontinue Windows server/client support and 32-bit clients. The current supported-platform guidance later lists Windows x64 client support with patch conditions. Do not claim Windows server support for 7.1.
- DataPort and disaster recovery functions are removed.
- Shared memory mode and related utilities and properties are not supported.
- JDK/JRE 1.4 is no longer supported; use JDK/JRE 1.5 or later for 7.1.

### Altibase 7.3

Release identity: Altibase 7.3.0.0.1 release notes are dated 2023.08.

Main role in answers: 7.x modernization release with Kubernetes tooling, JDBC 4.2, OpenSSL 3.0.8, TLS 1.3, SQL and Spatial SQL improvements, replication DDL synchronization, and major performance work.

Major additions:

- Platform and operations: AKU, altiShapeLoader 1.0, DBeaver package for Windows, and altiMon support expansion.
- Security and SSL: OpenSSL 3.0.8 support, no OpenSSL 1.0.x support, TLS 1.3 support in addition to TLS 1.0 and TLS 1.2, `SSL_CIPHER_SUITES`, `SSL_LOAD_CONFIG`, and FIPS module support when `SSL_LOAD_CONFIG` is set to `1`.
- JDBC: partial JDBC API Specification 4.2 support, automatic driver loading, wrapper pattern support, national character set support, `Connection.abort()`, `Connection.setNetworkTimeout()`, `Connection.isValid()`, large update counts, `Connection.setClientInfo()`, `AltibaseJDBCType`, try-with-resources, and enhanced exception iteration.
- SQL and PSM: `VARRAY`, anonymous blocks, internal mode for C/C++ external procedures, multiple delete and update, PCRE2-compatible regular expression mode for Korean search, fetch across rollback, queue delete controls, `ALTER SEQUENCE` restart clause, `DBMS_STANDARD`, `DBMS_METADATA`, `DBMS_SQL_PLAN_CACHE`, `DBMS_OUTPUT` print controls, `DBMS_LOCK.sleep2`, and `SYS_SPATIAL`.
- Spatial SQL: SRID support, EWKT, EWKB, spatial SRID metadata, and functions including `ASEWKT`, `ASEWKB`, `GEOMFROMEWKT`, `GEOMFROMEWKB`, `SETSRID`, `SRID`, `ST_Collect`, `ST_IsCollection`, `ST_MakeEnvelope`, and related constructors.
- Replication: DDL synchronization with `REPLICATION_DDL_SYNC`, `REPLICATION_DDL_ENABLE`, and matching `REPLICATION_DDL_ENABLE_LEVEL`; `RECEIVE_ONLY`; replication sender performance improvements; and new remote metadata check views.
- Communication: InfiniBand support and related `IB_*` and `REPLICATION_IB_*` properties.
- Performance: lighter table lock mode, tablespace manager mutex improvements, disk temporary table performance, LZ4 log compression, OLTP scalability improvements, index build improvements, startup improvements, parallel `DEQUEUE`, CSE prepare-time reductions, simple query optimization on memory partitioned tables, `SERIAL_FILTER` and `SERIAL_EXECUTE_MODE`, scalar subquery optimization, PSM loop improvements, migration `-lightmode`, and JDBC `reuse_resultset`.
- Adapter features: `ADAPTER_LOB_TYPE_SUPPORT` and offline option for JDBC Adapter and oraAdapter.

Important compatibility changes:

- 7.3 changes database binary version to `7.3.0`; migration is required from lower versions because the log-file logging structure changed.
- Metadata must be reconfigured when upgrading from an earlier version to 7.3.
- Client backward compatibility is guaranteed only when major and minor communication protocol versions are identical.
- For replication, LAZY mode has backward compatibility; EAGER mode, DDL synchronization, and offline replication require the same replication protocol version.
- DDL synchronization and offline replication are not supported between Altibase 7.1 and Altibase 7.3.
- 7.3 aexport requires the `DBMS_METADATA` package. Without it, aexport can fail with `[ERR-91144 : DBMS_METADATA package does not exist.]`.
- JDBC behavior changes include `SQLFeatureNotSupportedException`, `SPECIFIC_NAME` metadata, `reuse_resultset`, `lob_null_select`, `getprocedures_return_functions`, and `CLIENT_TYPE = NEW_JDBC42`.

### Altibase 8.1

Release identity: Altibase 8.1.0.0.1 release notes are dated 2026.02.

Main role in answers: current baseline in this attachment set, adding JSON-native storage, document access, Temporary LOB, Kafka connectors, backup management, replication SSL, security utilities, JSON plans, and newer application interfaces.

Major additions:

- JSON data type: native `JSON` data type, up to 2 GB, based on RFC 8259. JSON path expressions and JSON functions follow ISO/IEC 19075-6:2021. Key functions include `JSON_ARRAY`, `JSON_OBJECT`, `JSON_EXISTS`, `JSON_QUERY`, `JSON_VALUE`, and `JSON_VALID`.
- 8.1 verified JSON syntax: `JSON [ IN ROW size ]`.
- 8.1 verified JSON cautions: JSON follows LOB-column restrictions, JSON document depth is limited to 256, JSON processing uses Temporary LOB, `TEMPORARY_LOB_ENABLE` must be set to `1` to use JSON, and JSON cannot be used with `SELECT FOR UPDATE`.
- JSON condition: the 8.1 verified source documents `IS JSON`.
- Temporary LOB: Temporary LOBs are transient LOBs created in memory at execution time and scoped to a session or transaction. Current usage can be checked with `V$TEMPORARY_LOBS`.
- Temporary LOB categories: Session Temporary LOB is used for LOB data types in PSM `ASSOCIATIVE ARRAY`, `VARRAY`, or package variables. Transaction Temporary LOB is used for cases such as `TO_CLOB`, `TO_BLOB`, CLOB-argument `SUBSTR`, CLOB-argument `CONCAT`, and LOB variables in PSM execution except session-scope cases.
- Temporary LOB controls: `TEMPORARY_LOB_ENABLE`, `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`, `MEMORY_TEMPLOB_PIECE_SIZE`, and `ALTER SESSION SET FREE TEMPORARY LOB`.
- KADA: Key-optimized Altibase Document Access for JSON document data, with Java API and REST API. KADA supports key-based CRUD, MongoDB-like query operators and syntax, manual transaction control, `AutoCloseable`, JWT-based REST authentication, multi-tenant isolation, and ACL-based collection sharing.
- Kafka connectors: Altibase Source Connector publishes Altibase change data to Kafka topics; Altibase Sink Connector consumes Kafka messages and applies them to Altibase tables.
- ABM: `abm` supports physical backup, backup file compression, encryption, and decryption.
- Replication SSL: replication communication can use SSL/TLS. Create replication with `USING SSL`, and configure the SSL replication port with `REPLICATION_SSL_PORT_NO`.
- Security utilities: `altiEncrypt` encrypts passwords for AKU, dblink, and adapters. Encrypted password files can be used by iSQL, iLoader, aexport, and abm through the `-pf` option.
- Performance: checkpoint scale single mode, memory index build improvements during startup, shutdown and memory index removal improvements, log file prepare thread improvements, `LOG_FILE_SIZE` default changed from 10 MB to 100 MB, `LOG_CREATE_METHOD` default changed, bulk LOB insert improvement, and page cache handling during memory database startup.
- External integration: Altibase Handler for MindsDB, .NET 8 support for Altibase ADO.NET and Altibase EF Core, and `node-odbc-altibase` for Node.js.
- Release-note-only feature scope: `KADA`, Kafka connectors, `abm`, MindsDB, `.NET 8`/EF Core, and `node-odbc-altibase` are summarized here for routing and version awareness. Do not generate implementation procedures for these feature families unless a dedicated attachment or source-backed block provides the procedure.
- Empty LOB handling: CLI adds `SQLEmptyLob()` and `SQLGetLobLength2()`, iLoader supports empty LOB with `-lob -use_lob_file=yes`, JDBC improves empty LOB handling, and JDBC Adapter and OraAdapter support empty LOB processing.
- ODBC: updatable dynaset support and improved read performance for `SQL_CURSOR_KEYSET_DRIVEN`.
- AKU: scale-up to six nodes, multiple replication definitions in `REPLICATIONS`, multithreaded parallel processing, and increased replication target table/user name length from 40 to 128 characters.
- Locale: Thai character set and Thai collation in UTF-8 environments; set `NLS_COMP` to `1` for Thai collation.
- Other: `DBMS_STATS.LOCK_TABLE_STATS`, `DBMS_STATS.UNLOCK_TABLE_STATS`, JSON-formatted execution plans, JDBC statement caching through `stmt_cache_enable`, and META LOGGING support in general replication environments.

Important compatibility changes:

- 8.1 changes database binary version to `8.1.0`; databases before 8.1 are not binary-compatible and require migration.
- 8.1 changes META major version to `10`; metadata must be rebuilt when upgrading from versions before 8.1.
- 8.1 changes only the patch part of the communication protocol; client backward compatibility is preserved.
- 8.1 does not change the replication protocol from 7.3.0.0.1 and 7.3.0.1.5, but only LAZY mode replication has backward compatibility. EAGER mode and optional replication features, including offline replication, do not guarantee backward compatibility. DDL replication requires all three digits of the replication protocol version to be identical.
- iLoader API builds that use encrypted password file login must include `libaltiutil.a`.
- 8.1 aexport delimiter defaults changed: `ILOADER_FIELD_TERM` changes from `^` to `^C_c^`; `ILOADER_ROW_TERM` changes from `%n` to `^R_r^%n`.
- The `DBMS_METADATA` package must be updated.
- JSON-formatted execution plans are release-note-backed. Do not invent JSON plan schema or output examples unless a later source provides them.

## Component Version Matrix

Use this small matrix for upgrade and compatibility answers.

| Version | Database Binary Version | Meta Version | Communication Protocol Version | Replication Protocol Version |
| --- | --- | --- | --- | --- |
| 7.1.0.1.2 | 6.5.1 | 8.5.1 | 7.1.6 | 7.4.2 |
| 7.3.0.0.1 | 7.3.0 | 9.3.1 | 7.1.8 | 7.4.9 |
| 7.3.0.1.5 | 7.3.0 | 9.4.1 | 7.1.8 | 7.4.9 |
| 8.1.0.0.1 | 8.1.0 | 10.1.1 | 7.1.9 | 7.4.9 |

## Upgrade Risk Blocks

### Risk: Database Binary Version Mismatch

Applies to: upgrades into 7.1, 7.3, and 8.1.

What changes:

- 7.1.0.1.2 uses database binary version `6.5.1`; upgrading from 6.5.1 or earlier requires migration when database image and log file formats do not match.
- 7.3.0.0.1 uses database binary version `7.3.0`; upgrading from lower versions to 7.3 requires migration because the log-file logging structure changed.
- 8.1.0.0.1 uses database binary version `8.1.0`; databases before 8.1 are not binary-compatible with 8.1 and require migration.

Required action:

- Plan a migration path, full backup, rollback plan, and application verification before replacing binaries.
- Do not treat a server binary swap as enough when database binary compatibility changes.

Check SQL:

```sql
SELECT product_version,
       meta_version,
       protocol_version,
       repl_protocol_version
FROM V$VERSION;
```

### Risk: Metadata Version Change

Applies to: 7.1, 7.3, and 8.1 upgrades.

What changes:

- 7.1 performs a meta upgrade automatically when upgrading from 6.5.1 or earlier, but rollback may require rebuilding metadata. 7.1.0.1.2 also provides `server downgrade` for patch rollback when the meta version differs.
- 7.3 changes the major metadata version and requires metadata reconfiguration when upgrading from earlier versions.
- 8.1 changes the META major version and requires metadata rebuild when upgrading from versions before 8.1.

Required action:

- Capture metadata version before and after migration.
- Do not manually update meta tables. Use documented upgrade, migration, or metadata rebuild procedures.

Check SQL:

```sql
SELECT db_name,
       meta_major_ver,
       meta_minor_ver,
       meta_patch_ver
FROM SYSTEM_.SYS_DATABASE_;
```

### Risk: Client and Communication Protocol Compatibility

Applies to: applications using CLI, ODBC, JDBC, precompiler, adapters, or tools.

What changes:

- 7.1 communication protocol changes only in the patch version compared with 6.5.1, so existing 6.5.1 client applications remain compatible with 7.1.0.1.2 without rebuild according to the 7.1 release notes.
- 7.3 client backward compatibility is guaranteed only when the major and minor communication protocol versions are identical.
- 8.1 changes only the communication protocol patch version and preserves client backward compatibility.

Required action:

- Check the server `PROTOCOL_VERSION` and client package version.
- Test connection pools, JDBC metadata calls, LOB APIs, SSL/TLS, and tool login flows after upgrade.

Check SQL:

```sql
SELECT product_version,
       protocol_version
FROM V$VERSION;
```

### Risk: Replication Compatibility

Applies to: replication, HA, CDC/log analysis, adapters, and migration projects.

What changes:

- 7.1 replication protocol remains `7.4.2` relative to 6.5.1, so replication between 6.5.1 and 7.1.0.1.2 is possible.
- 7.3 replication protocol is `7.4.9`. LAZY mode has backward compatibility, but EAGER mode, DDL synchronization, and offline replication require the same replication protocol version.
- DDL synchronization and offline replication are not supported between Altibase 7.1 and Altibase 7.3.
- 8.1 replication protocol remains `7.4.9`, but only LAZY mode has backward compatibility. EAGER mode and optional features, including offline replication, do not guarantee backward compatibility. DDL replication requires all three digits of the replication protocol version to be identical.
- 8.1 adds replication SSL with `USING SSL` and `REPLICATION_SSL_PORT_NO`.

Required action:

- Record replication mode, optional features, protocol version, table metadata, and DDL synchronization settings before upgrade.
- Keep mixed-version replication conservative. Avoid claiming compatibility for EAGER, DDL synchronization, offline replication, propagation, or analysis modes unless the exact versions and protocol rules are verified.

Check SQL:

```sql
SELECT product_version,
       repl_protocol_version
FROM V$VERSION;
```

For 8.1 replication SSL:

```sql
SELECT name,
       value1,
       min,
       max
FROM V$PROPERTY
WHERE name = 'REPLICATION_SSL_PORT_NO';
```

## Platform Support Blocks

### Common Platform Rules

- Altibase 7.1, 7.3, and 8.1 server and client packages in this attachment are 64-bit only.
- For operating systems not listed here, direct the customer to Altibase Support for compatibility test results.
- OS support can depend on Altibase patch level. Keep patch conditions in the answer.
- Do not use 6.5.1 platform support to answer a 7.1, 7.3, or 8.1 question.
- Minimum hardware stated by the release notes for 7.1, 7.3, and 8.1: 1 GB RAM, 1 CPU, and 4 GB free disk; recommended baseline is 2 GB RAM, 2 CPUs, and 12 GB free disk.

### Altibase 7.1 Server and Client Platforms

Java compatibility: JDK/JRE 1.5 or later. JDK/JRE 1.4 is not supported.

Server and client supported:

- AIX on IBM Power Systems: AIX 7.2 TL2 or later requires Altibase 7.1.0.4.7 or later; AIX 7.1 is supported; AIX 6.1 TL3 or later is supported.
- HP-UX on Itanium IA-64: HP-UX 11.31 is supported.
- Linux x86-64 Red Hat-based: Oracle Linux 9, Red Hat Enterprise Linux 9, CentOS 9, and Rocky Linux 9 require glibc 2.34 and Altibase 7.1.0.10.0 or later.
- Linux x86-64 Red Hat-based: Oracle Linux 8, Red Hat Enterprise Linux 8, CentOS 8, Rocky Linux 8, Oracle Linux 7, Red Hat Enterprise Linux 7, CentOS 7, Oracle Linux 6, Red Hat Enterprise Linux 6, and CentOS 6 are supported with glibc 2.12 to 2.33.
- Linux x86-64 Debian-based: Ubuntu 18 requires glibc 2.27 to 2.33 and Altibase 7.1.0.7.2 or later.
- Linux x86-64 Debian-based: Ubuntu 16 requires glibc 2.23 to 2.33 and Altibase 7.1.0.7.2 or later.
- Linux x86-64 Debian-based: Ubuntu 12 requires glibc 2.17 to 2.33.
- Linux on Power: POWER7 with Red Hat Enterprise Linux 6.5 is supported with glibc 2.12 to 2.33.
- Linux on Power Little Endian: POWER8(LE) with Red Hat Enterprise Linux 7.2 requires glibc 2.17 to 2.33 and Altibase 7.1.0.0.8 or later.

Client-only on Windows x64:

- Microsoft Windows 10: server is not supported; client is supported.
- Microsoft Windows 2008: server is not supported; client requires Altibase Client 7.1.0.4.5 or later.

7.1 library and tool support:

- PDO drivers are supported on Linux x86-64 Red Hat-based and Debian-based platforms and Linux on Power or Power Little Endian; they are not supported on AIX, HP-UX, or Windows.
- `altiMon` is supported on AIX, HP-UX, Linux x86-64, Linux on Power, and Linux on Power Little Endian; patch conditions apply for AIX 7.2 or 7.1, Ubuntu 18 or 16, and POWER8(LE).
- Adapter for JDBC is supported on AIX, HP-UX, Linux x86-64, Linux on Power, and Linux on Power Little Endian; it is not supported on Windows.
- Adapter for Oracle is supported on AIX and Linux x86-64; it is not supported on HP-UX, Linux on Power, Linux on Power Little Endian, or Windows.

### Altibase 7.3 Server and Client Platforms

Java compatibility: JDK/JRE 1.8 or later.

Server and client supported:

- Linux on IBM LinuxONE s390x: Red Hat Enterprise Linux 8 requires glibc 2.17 to 2.33 and Altibase 7.3.0.1.2 or later.
- Linux x86-64 Red Hat-based: Oracle Linux 9, Red Hat Enterprise Linux 9, CentOS 9, and Rocky Linux 9 require glibc 2.34 and Altibase 7.3.0.0.9 or later.
- Linux x86-64 Red Hat-based: Oracle Linux 8, Red Hat Enterprise Linux 8, CentOS 8, Rocky Linux 8, Oracle Linux 7, Red Hat Enterprise Linux 7, CentOS 7, Oracle Linux 6, Red Hat Enterprise Linux 6, and CentOS 6 are supported with glibc 2.12 to 2.33.
- Linux x86-64 Debian-based: Ubuntu 18 requires glibc 2.27 to 2.33.
- Linux x86-64 Debian-based: Ubuntu 16 requires glibc 2.23 to 2.33.
- Linux x86-64 Debian-based: Ubuntu 12 requires glibc 2.17 to 2.33.
- Linux on Power: POWER7 with Red Hat Enterprise Linux 6.5 is supported with glibc 2.12 to 2.33.
- Linux on Power Little Endian: POWER8(LE) with Red Hat Enterprise Linux 7.2 is supported with glibc 2.17 to 2.33.
- AIX on IBM Power Systems: AIX 7.2, AIX 7.1, and AIX 6.1 TL9 or later are supported.
- HP-UX on Itanium IA-64: HP-UX 11.31 is supported.

Client-only on Windows x64:

- Microsoft Windows 10: server is not supported; client is supported in the current supported-platform table.
- Microsoft Windows 2008: 7.3.0.0.1 release notes and the 7.3 Installation Guide list server not supported and client supported, but the current supported-platform table does not list Windows 2008 for 7.3. Use this only for exact patch-level or source-specific answers; do not generalize Windows 2008 support to current 7.3 platform guidance.

7.3 library and tool support:

- PDO drivers are supported on LinuxONE s390x, Linux x86-64 Red Hat-based and Debian-based platforms, Linux on Power, and Linux on Power Little Endian; they are not supported on AIX, HP-UX, or Windows.
- `altiMon` is supported on LinuxONE s390x, Linux x86-64, Linux on Power, Linux on Power Little Endian, AIX, and HP-UX; it is not supported on Windows.
- Adapter for JDBC is supported on LinuxONE s390x, Linux x86-64, Linux on Power, Linux on Power Little Endian, AIX, and HP-UX; it is not supported on Windows.
- Adapter for Oracle is supported on LinuxONE s390x, Linux x86-64, and AIX; it is not supported on Linux on Power, Linux on Power Little Endian, HP-UX, or Windows.

### Altibase 8.1 Server and Client Platforms

Java compatibility: JDK/JRE 1.8 or later.

Server and client supported:

- AIX on IBM Power Systems: AIX 7.2 is supported.
- Linux x86-64: Red Hat Enterprise Linux 9 is supported with glibc 2.34.
- Linux x86-64: Red Hat Enterprise Linux 7 and Red Hat Enterprise Linux 8 are supported with glibc 2.12 to 2.33.

Client-only on Windows x64:

- Microsoft Windows 2008: server is not supported; client is supported.
- Microsoft Windows 10: server is not supported; client is supported.

Not listed for 8.1 in the release-note platform table:

- HP-UX.
- Linux on Power.
- Linux on Power Little Endian.
- LinuxONE s390x.
- Ubuntu or other Debian-based Linux.
- Windows server.

Do not say these are supported for 8.1 unless a newer supported-platform source explicitly lists them.

## Platform Answer Checklist

When answering "Is my platform supported?", collect these fields:

- Altibase major and patch version, for example `7.1.0.10.0`, `7.3.0.0.9`, or `8.1.0.0.1`.
- Component: server, client, PDO driver, `altiMon`, Adapter for JDBC, Adapter for Oracle, AKU, ABM, or another tool.
- OS family and version, for example Red Hat Enterprise Linux 9, AIX 7.2, HP-UX 11.31, Microsoft Windows 10.
- CPU and architecture, for example x86-64, PowerPC, POWER8(LE), s390x, or IA-64.
- glibc version for Linux where the platform block lists a glibc requirement.
- JDK/JRE version when Java tools, JDBC, adapters, KADA, altiShapeLoader, or AKU are involved.
- Whether the customer needs server support, client support, or both.

Template answer:

```text
For Altibase <version>, <component> on <OS/CPU> is <supported/not listed/client-only>.
Condition: <patch requirement, glibc requirement, JDK requirement, or none>.
Server support: <yes/no/not listed>.
Client support: <yes/no/not listed>.
Do not use a different major version's platform table as proof of support.
```

## 8.1 Feature Check SQL

Use these checks when a customer asks whether an 8.1-specific property or view exists on their running server.

Check version and protocols:

```sql
SELECT product_version,
       meta_version,
       protocol_version,
       repl_protocol_version
FROM V$VERSION;
```

Check 8.1 Temporary LOB properties:

```sql
SELECT name,
       value1,
       min,
       max
FROM V$PROPERTY
WHERE name IN (
  'TEMPORARY_LOB_ENABLE',
  'MEMORY_TEMPLOB_MAX_ALLOC_SIZE',
  'MEMORY_TEMPLOB_PIECE_SIZE'
)
ORDER BY name;
```

Check currently used Temporary LOBs:

```sql
SELECT type,
       id,
       alloced_size,
       open_count
FROM V$TEMPORARY_LOBS;
```

Check 8.1 replication SSL property:

```sql
SELECT name,
       value1,
       min,
       max
FROM V$PROPERTY
WHERE name = 'REPLICATION_SSL_PORT_NO';
```

Check 8.1 JSON plan properties:

```sql
SELECT name,
       value1
FROM V$PROPERTY
WHERE name IN (
  'TRCLOG_EXPLAIN_TYPE',
  'TRCLOG_JSON_PLAN_INDENT_DEPTH'
)
ORDER BY name;
```

## Version-Specific Answer Rules

- For 7.1 answers, emphasize that it is the older stable 7.x baseline and that it removed Windows server support, 32-bit clients, DataPort, disaster recovery, and shared memory mode.
- For 7.3 answers, emphasize JDBC 4.2, OpenSSL 3.0.8, TLS 1.3, AKU, Spatial SQL/SRID, replication DDL synchronization, InfiniBand, performance, and migration-required binary/meta changes.
- For 8.1 answers, emphasize native JSON, Temporary LOB, KADA, Kafka connectors, ABM, replication SSL, encrypted password tooling, JSON plans, newer driver/interface support, and migration-required binary/meta changes.
- When comparing 7.3 and 8.1, state that 8.1 keeps replication protocol `7.4.9` but changes database binary version to `8.1.0`, meta version to `10.1.1`, and communication protocol to `7.1.9`.
- When comparing 7.1 and 7.3, state that 7.3 changes database binary version from `6.5.1` to `7.3.0`, meta version from `8.5.1` to `9.3.1`, communication protocol from `7.1.6` to `7.1.8`, and replication protocol from `7.4.2` to `7.4.9`.
- If the user asks for a generated migration plan, include a backup, target platform check, binary/meta compatibility check, replication feature check, application client test, and post-upgrade SQL verification.
- If a feature is release-note-only, say that the release notes confirm the feature but avoid operational details that are not present in the source.



## Minor Patch & Release Notes Caveats
- **Release/Patch Notes Review**: When planning an upgrade or migration, always refer to the specific Altibase release notes (e.g., 7.1.x.x, 8.1.x.x) for minor patch restrictions, deprecated functions, and critical bug fixes that may not be present in the general manual.

## Residual Scope

- Release-note-only feature families are kept to version awareness and routing. Do not turn those bullets into operational procedures unless a dedicated source-backed block provides the procedure.
