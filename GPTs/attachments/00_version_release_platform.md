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

## Retrieval Alias Index

Use this compact index before scanning the long release and platform sections. It is intentionally redundant with later headings so lexical retrieval can land on the exact version, patch, platform, or upgrade block.

- Aliases and customer wording: version comparison, release notes, supported platforms, OS and CPU matrix, server support, client support, Windows client-only, database binary version, metadata version, communication protocol, replication protocol, upgrade risk, migration risk, patch caveat.
- Exact-token anchors: `V$VERSION`, `product_version`, `meta_version`, `protocol_version`, `repl_protocol_version`, `JSON`, `Temporary LOB`, `KADA`, `Kafka`, `ABM`, `abm`, `OpenSSL 3.0.8`, `TLS 1.3`, `JDBC 4.2`, `AKU`, `REPLICATION_SSL_PORT_NO`.
- Focused routing anchors: release identity and feature-introduction answers route to `Quick Version Difference Summary`; platform and OS questions route to `Platform Support Blocks`; binary, metadata, client-protocol, and replication-protocol questions route to `Upgrade Risk Blocks`; patch-specific support boundaries route to `Minor Patch & Release Notes Caveats` and `Patch Note Compact Change Blocks`.
- Answer route: start here for release identity, supported platform, protocol, and feature-introduction questions, then route implementation details to the attachment that owns the feature.
- Cross-file routing: installation and patch rollback use `01_getting_started_installation.md`; property defaults and ranges use `05_data_types_properties.md`; replication compatibility uses `09_replication_ha_cdc.md`; TLS details use `18_security_ssl_tls.md`; connector and tool procedures use `11_java_jdbc_spring.md` through `19_spatial_nifi_tableau_misc.md`.

## Source Documents

- Altibase 7.1 Release Notes.
- Altibase 7.3 Release Notes.
- Altibase 8.1 Release Notes.
- Altibase Supported Platforms by Version.
- Altibase 8.1 verified source.

## Response Rules

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
- Performance: checkpoint scale single mode, memory index build improvements during startup, shutdown and memory index removal improvements, log file prepare thread improvements, `LOG_FILE_SIZE` default changed from `10485760` (10 MB) to `104857600` (100 MB) and maximum changed from `18446744073709551615` to `4294967295`, `LOG_CREATE_METHOD` default changed from `0` to `1` while the 8.1 verified source remains OS-specific (`0` on HP-UX/AIX, `1` on Linux), bulk LOB insert improvement, and page cache handling during memory database startup.
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

## Patch Note Compact Change Blocks

These blocks preserve exact patch versions and patch-note tokens for source-backed retrieval. They do not replace customer environment analysis: before attributing an incident to a patch item, ask for the installed Altibase patch, platform, topology, SQL or object definition, logs, and runtime output. Route implementation procedures to the owner attachment named for each token.

Owner routes used below: `01_getting_started_installation.md` for install/start/stop/license; `02_administration_operations.md` for server operations, backup/recovery, storage, and transaction operations; `03_sql_ddl_generation.md` for DDL and partition SQL; `04_sql_dml_oracle_compatibility.md` for DML, functions, predicates, and query behavior; `05_data_types_properties.md` for properties, data types, LOB, and numeric behavior; `06_data_dictionary_performance_views.md` for dictionary and performance views; `07_error_messages_troubleshooting.md` for error/log symptoms; `08_performance_tuning_monitoring.md` for optimizer, plan, statistics, monitoring API, and performance; `09_replication_ha_cdc.md` for replication, HBT, protocol, and HA; `10_psm_stored_external_procedures.md` for PSM, packages, procedures, and triggers; `11_java_jdbc_spring.md` for JDBC and JDBC Adapter; `12_c_cli_odbc_precompiler.md` for CLI, ODBC, IPCDA, and APRE/precompiler; `13_isql_iloader_basic_tools.md` for iSQL and iLoader; `14_utilities_operation_tools.md` for `aexport`, `altiComp`, `awrite`, `dumptrc`, `dumpStack`, and altiMon; `15_migration_oracle_compatibility.md` for oraAdapter and Oracle skip policy; `16_dblink_external_connectors.md` for DB Link and AltiLinker; `18_security_ssl_tls.md` for OpenSSL/TLS and encryption.

### Altibase 7.1.0.1.3 Patch Notes

Source row: `SRC-PATCH-PATCH-000001`.
Source file: `PatchNotes/Altibase_7.1/kor/Altibase_7_1_0_1_3_Patch_Notes.md`.
Version Info: database binary `6.5.1`, meta `8.5.1`, cm protocol version `7.1.6`, replication protocol `7.4.2`.

New features:

- `BUG-45145` - adds iSQL command history through `ISQL_HIST_FILE`; the patch note warns that interactive input, including sensitive values, can be written to the history file. Route: `13_isql_iloader_basic_tools.md`.
- `BUG-45802` - supports fetch across rollback. Route: `04_sql_dml_oracle_compatibility.md`.
- `BUG-45830` - adds the `awrite` utility. Route: `14_utilities_operation_tools.md`.
- `BUG-45858` - supports Hierarchy Query joins. Route: `04_sql_dml_oracle_compatibility.md`.
- `BUG-45921` - supports DDL for Queue Sequence initialization. Route: `03_sql_ddl_generation.md`.
- `BUG-45924` - adds `sql_cache_text_id` to Monitoring API `ABISqlText`. Route: `08_performance_tuning_monitoring.md`.
- `BUG-45934` - records LOB restrictions for Hierarchy Query joins. Route: `04_sql_dml_oracle_compatibility.md` and `05_data_types_properties.md`.
- `BUG-45978` - adds RDMA/InfiniBand communication support and `IB_*` properties. Route: `05_data_types_properties.md`, `06_data_dictionary_performance_views.md`, and `09_replication_ha_cdc.md`.
- `BUG-45936` - adds package support for online table partition swap. Route: `10_psm_stored_external_procedures.md` and `03_sql_ddl_generation.md`.
- `BUG-45953` - allows replication create/add IP fields to use hostnames. Route: `09_replication_ha_cdc.md`.

Fixed bugs:

- `BUG-45344` - fixes A5 client communication with a higher-version server accessing freed memory. Route: `12_c_cli_odbc_precompiler.md`.
- `BUG-45618` - checks thread-termination state in replication send and receive functions. Route: `09_replication_ha_cdc.md`.
- `BUG-45722` - changes `TERM ON` behavior so commands are not printed. Route: `13_isql_iloader_basic_tools.md`.
- `BUG-45813` - reduces inefficient CPU use while a replication Parallel Applier waits for transactions. Route: `09_replication_ha_cdc.md`.
- `BUG-45825` - fixes an unexpected error when an `UPDATE` statement uses a window function. Route: `04_sql_dml_oracle_compatibility.md`.
- `BUG-45838` - allows `null` as the value for JDBC `PreparedStatement.setObject(Index, Value, Sqltype, Scale)`. Route: `11_java_jdbc_spring.md`.
- `BUG-45856` - fixes a case where the job scheduler could stop while operating. Route: `02_administration_operations.md` and `10_psm_stored_external_procedures.md`.
- `BUG-45857` - avoids writing a call stack to `altibase_error.log` for normal disk temporary table exceptions. Route: `07_error_messages_troubleshooting.md`.
- `BUG-45864` - revises the Action text for DB Link errors when `altilinker.jar` is missing or has unsuitable permissions. Route: `16_dblink_external_connectors.md` and `07_error_messages_troubleshooting.md`.
- `BUG-45872` - fixes `altiComp` Diff `Invalid Lob range` errors when LOB length exceeds `4096`. Route: `14_utilities_operation_tools.md`.
- `BUG-45883` - fixes wrong `altiComp` diff/sync output for LOB columns in differently named master and slave tables. Route: `14_utilities_operation_tools.md`.
- `BUG-45893` - prevents user sessions from using cached plans for queries against `system_.dba_users_`. Route: `06_data_dictionary_performance_views.md` and `08_performance_tuning_monitoring.md`.
- `BUG-45904` - cleans BCB state from the page hash when page-header initialization fails during page creation. Route: `02_administration_operations.md` and `07_error_messages_troubleshooting.md`.
- `BUG-45909` - improves `altiComp` LOB-column diff/sync handling. Route: `14_utilities_operation_tools.md`.
- `BUG-45925` - aligns server and client `Numeric` to `double` conversion error behavior. Route: `05_data_types_properties.md` and `12_c_cli_odbc_precompiler.md`.
- `BUG-45935` - fixes abnormal termination when a `KEEP` clause uses a parallel hint. Route: `04_sql_dml_oracle_compatibility.md` and `08_performance_tuning_monitoring.md`.
- `BUG-45958` - fixes `altiComp` `DIFF` and `SYNC` handling for `BIT` type data. Route: `14_utilities_operation_tools.md` and `05_data_types_properties.md`.
- `BUG-45976` - checks for deleted semaphores in IPCDA mode. Route: `12_c_cli_odbc_precompiler.md`.
- `BUG-45979` - prevents invalid page-information access after index-cache creation fails. Route: `08_performance_tuning_monitoring.md` and `02_administration_operations.md`.
- `BUG-45981` - fixes continuous HBT checking when `REPLICATION_HBT_DETECT_TIME` is set to `1`. Route: `09_replication_ha_cdc.md` and `05_data_types_properties.md`.
- `BUG-45989` - fixes a segmentation fault when `aexport` runs in a directory without write permission. Route: `14_utilities_operation_tools.md`.
- `BUG-45990` - fixes abnormal server termination when PSM with `PRAGMA AUTONOMOUS_TRANSACTION` is executed concurrently through a query. Route: `10_psm_stored_external_procedures.md`.

Compatibility and catalog caveat: database binary, meta, communication protocol, and replication protocol are unchanged for this patch. Added properties are `IB_ENABLE`, `IB_PORT_NO`, `IB_MAX_LISTEN`, `IB_LISTENER_DISABLE`, `IB_LATENCY`, and `IB_CONCHKSPIN`; changed performance view: `V$STATNAME`. Ask for exact installed patch, platform, object definitions, replication topology, and logs before asserting production applicability.

### Altibase 7.1.0.1.4 Patch Notes

Source row: `SRC-PATCH-PATCH-000002`.
Source file: `PatchNotes/Altibase_7.1/kor/Altibase_7_1_0_1_4_Patch_Notes.md`.
Version Info: database binary `6.5.1`, meta `8.6.1`, cm protocol version `7.1.6`, replication protocol table value `7.4.3`.

New features:

- `BUG-45779` - supports APRE PSM array-type arguments. Route: `12_c_cli_odbc_precompiler.md` and `10_psm_stored_external_procedures.md`.
- `BUG-45701` - supports PSM associative array parameter binding. Route: `10_psm_stored_external_procedures.md`.
- `BUG-46032` - supports two-level associative array variables in `BULK COLLECT INTO`. Route: `10_psm_stored_external_procedures.md`.
- `BUG-45946` - allows DDL Synchronization through replication and requires aligned `REPLICATION_DDL_SYNC`, `REPLICATION_DDL_ENABLE`, and `REPLICATION_DDL_ENABLE_LEVEL` settings on participating nodes. Route: `09_replication_ha_cdc.md` and `05_data_types_properties.md`.
- `BUG-46308` - supports replication for Partition Merge/Split DDL. Route: `09_replication_ha_cdc.md` and `03_sql_ddl_generation.md`.
- `BUG-45972` - handles DDL syntax that is valid only in standalone mode. Route: `03_sql_ddl_generation.md`.
- `BUG-45984` - supports InfiniBand communication for replication and introduces `REPLICATION_IB_*` property use. Route: `09_replication_ha_cdc.md` and `05_data_types_properties.md`.
- `BUG-46209` - adds APRE and AEXPORT syntax support for replication InfiniBand communication. Route: `12_c_cli_odbc_precompiler.md`, `14_utilities_operation_tools.md`, and `09_replication_ha_cdc.md`.
- `BUG-46011` - removes CLI Deferred Prepare restrictions. Route: `12_c_cli_odbc_precompiler.md`.
- `BUG-46016` - removes the LOB restriction for Hierarchy Query joins. Route: `04_sql_dml_oracle_compatibility.md` and `05_data_types_properties.md`.
- `BUG-46065` - supports `RANGE PARTITION` with `HASH`. Route: `03_sql_ddl_generation.md`.
- `BUG-46074` - supports multiple trigger events and adds `DBMS_STANDARD`. Route: `10_psm_stored_external_procedures.md`.
- `BUG-46095` - adds Adapter Propagation functionality. Route: `11_java_jdbc_spring.md` and `09_replication_ha_cdc.md`.
- `BUG-46151` - changes failover behavior by adding `LoadBalance`. Route: `11_java_jdbc_spring.md`.
- `BUG-46154` - adds `print_enable` and `print_disable` procedures to `DBMS_OUTPUT`. Route: `10_psm_stored_external_procedures.md`.
- `BUG-46158` - provides a way to keep plans in the plan cache. Route: `08_performance_tuning_monitoring.md`.
- `BUG-46163` - supports Queue over IPCDA. Route: `12_c_cli_odbc_precompiler.md` and `03_sql_ddl_generation.md`.
- `BUG-46229` - improves memory reuse for `MERGE` statements. Route: `04_sql_dml_oracle_compatibility.md`.
- `BUG-46245` - lets `jdbcAdapter` execute SQL scripts at runtime like `oraAdapter`. Route: `11_java_jdbc_spring.md` and `15_migration_oracle_compatibility.md`.
- `BUG-46273` - adds `LOCK TABLE` support for locking a specific partition. Route: `03_sql_ddl_generation.md`.
- `BUG-46067` - improves replication sync lock-acquisition failure messages by including the table name. Route: `09_replication_ha_cdc.md` and `07_error_messages_troubleshooting.md`.

Fixed bugs:

- `BUG-45053` - returns threads correctly when a replication Parallel Applier thread-start function fails. Route: `09_replication_ha_cdc.md`.
- `BUG-45060` - prevents `replication drop` while an offline replication start has not completed. Route: `09_replication_ha_cdc.md`.
- `BUG-45264` - automatically creates a missing temp file at server startup. Route: `02_administration_operations.md`.
- `BUG-45643` - fixes replication handshake failure for DDL on encrypted columns. Route: `09_replication_ha_cdc.md` and `18_security_ssl_tls.md`.
- `BUG-45652` - fixes handshake success when Active and Standby List Partition tables have different range conditions. Route: `09_replication_ha_cdc.md` and `03_sql_ddl_generation.md`.
- `BUG-45898` - prevents fetch exceptions from causing hangs or protocol misinterpretation. Route: `12_c_cli_odbc_precompiler.md` and `04_sql_dml_oracle_compatibility.md`.
- `BUG-45948` - fixes abnormal termination when DDL sync is performed to the server after client startup. Route: `09_replication_ha_cdc.md`.
- `BUG-45961` - improves cursor reuse-condition checks for fetch across rollback. Route: `04_sql_dml_oracle_compatibility.md`.
- `BUG-46010` - does not treat HBT connection-progress events as errors. Route: `09_replication_ha_cdc.md`.
- `BUG-46023` - fixes abnormal termination when creating a forced view with `SELECT UNION ALL` against a table without a referenced column. Route: `03_sql_ddl_generation.md` and `04_sql_dml_oracle_compatibility.md`.
- `BUG-46051` - fixes a DB Link select-result issue after savepoint rollback failure. Route: `16_dblink_external_connectors.md`.
- `BUG-46068` - fixes rare abnormal termination when a disk unique index accesses reused data. Route: `03_sql_ddl_generation.md` and `08_performance_tuning_monitoring.md`.
- `BUG-46113` - fixes segmentation fault from `SQLSetDescField()` with `NCHAR` or `NVARCHAR` schema. Route: `12_c_cli_odbc_precompiler.md`.
- `BUG-46123` - fixes JDBC `DatabaseMetaData.getTypeInfo()` result type-conversion errors. Route: `11_java_jdbc_spring.md`.
- `BUG-46130` - fixes `dumptrc` operation on PowerPC Linux. Route: `14_utilities_operation_tools.md`.
- `BUG-46157` - adds propagation-related create-replication syntax to APRE and AEXPORT. Route: `09_replication_ha_cdc.md`, `12_c_cli_odbc_precompiler.md`, and `14_utilities_operation_tools.md`.
- `BUG-46161` - fixes segmentation fault in RDMA library `rshutdown()`. Route: `09_replication_ha_cdc.md`.
- `BUG-46184` - fixes abnormal termination in Hierarchy Query `ORDER SIBLINGS BY` when normal and meaningless columns are used together. Route: `04_sql_dml_oracle_compatibility.md`.
- `BUG-46197` - fixes unwanted AltiLinker reconnect behavior when disconnect is performed while AltiLinker is not running. Route: `16_dblink_external_connectors.md`.
- `BUG-46202` - removes duplicate entries in `V$EVENT_NAME`. Route: `06_data_dictionary_performance_views.md`.
- `BUG-46230` - refines error messages for `iduMemory.getStatus()` and `iduMemory.setStatus()`. Route: `07_error_messages_troubleshooting.md`.
- `BUG-46239` - fixes DDL Synchronization failure when a `SELECT` during DDL sync fails to acquire a lock. Route: `09_replication_ha_cdc.md`.
- `BUG-46242` - requires DDL Synchronization to fail when the Propagation option is enabled. Route: `09_replication_ha_cdc.md`.
- `BUG-46249` - fixes wrong results when no set operation references a column in a `GROUP BY` expression. Route: `04_sql_dml_oracle_compatibility.md`.
- `BUG-46264` - fixes a hang on disk tables when duplicate columns appear in a window sort `ORDER BY` clause. Route: `04_sql_dml_oracle_compatibility.md` and `08_performance_tuning_monitoring.md`.
- `BUG-46265` - validates whether a `Create Disk Temp Table` key column list can cycle. Route: `04_sql_dml_oracle_compatibility.md` and `08_performance_tuning_monitoring.md`.
- `BUG-46274` - fixes `column not found` after partition swap followed by update. Route: `03_sql_ddl_generation.md` and `04_sql_dml_oracle_compatibility.md`.
- `BUG-46279` - fixes wrong results when disk-temp grouping data sort references a subquery. Route: `04_sql_dml_oracle_compatibility.md` and `08_performance_tuning_monitoring.md`.
- `BUG-46286` - fixes an error when an `insert ~ select` statement uses a parallel hint without a table name. Route: `04_sql_dml_oracle_compatibility.md` and `08_performance_tuning_monitoring.md`.

Compatibility and catalog caveat: database binary and communication protocol are unchanged. Meta changes from `8.5.1` to `8.6.1`, and patching from `7.1.0.1.3` or earlier to `7.1.0.1.4` performs an automatic meta upgrade; `SYS_REPL_HOSTS_` adds `CONN_TYPE` and `IB_LATENCY`. The version table lists replication protocol `7.4.3`, while the compatibility prose says the replication protocol changed from `7.4.3` to `7.4.4` with backward compatibility; ask for `V$VERSION` output before making mixed-replication claims. Added properties are `REPLICATION_IB_PORT_NO`, `REPLICATION_IB_LATENCY`, `REPLICATION_DDL_SYNC`, and `REPLICATION_DDL_SYNC_TIMEOUT`; changed performance views are `V$SQL_PLAN_CACHE_SQLTEXT`, `V$SQL_PLAN_CACHE_PCO`, and `V$SESSION`.

### Altibase 7.1.0.1.5 Patch Notes

Source row: `SRC-PATCH-PATCH-000003`.
Source file: `PatchNotes/Altibase_7.1/kor/Altibase_7_1_0_1_5_Patch_Notes.md`.
Version Info: database binary `6.5.1`, meta `8.6.1`, cm protocol version `7.1.6`, replication protocol `7.4.3`.

New features:

- `BUG-46475` - supports JDBC Adapter for HP-UX and AIX. Route: `11_java_jdbc_spring.md`.
- `BUG-46216` - adds key-preserved checking for updatable join views. Route: `04_sql_dml_oracle_compatibility.md` and `03_sql_ddl_generation.md`.
- `BUG-46352` - prints the OpenSSL version while loading OpenSSL. Route: `18_security_ssl_tls.md`.
- `BUG-46411` - changes the maximum value of `LOB_CACHE_THRESHOLD` for LOB fetch performance. Route: `05_data_types_properties.md`.
- `BUG-46443` - applies list protocol to normal bind-parameter transmission for JDBC performance. Route: `11_java_jdbc_spring.md`.
- `BUG-46465` - refactors `CmBufferWriter.encodeString` for JDBC performance. Route: `11_java_jdbc_spring.md`.

Fixed bugs:

- `BUG-46309` - fixes server abnormal termination when PSM calls `DEQUEUE` without an `INTO` clause. Route: `10_psm_stored_external_procedures.md` and `03_sql_ddl_generation.md`.
- `BUG-46392` - fixes abnormal termination when an `ORDER BY` expression is referenced redundantly in the target clause. Route: `04_sql_dml_oracle_compatibility.md`.
- `BUG-46416` - fixes infinite wait when a view is referenced by both a function and a view. Route: `03_sql_ddl_generation.md` and `04_sql_dml_oracle_compatibility.md`.
- `BUG-46424` - fixes a disk temporary table creation case where an upper plan node does not store a required value. Route: `08_performance_tuning_monitoring.md`.
- `BUG-46183` - fixes `DEQUEUE` `WAIT TIME` below one second not waiting for the configured time. Route: `03_sql_ddl_generation.md` and `04_sql_dml_oracle_compatibility.md`.
- `BUG-46217` - makes `V$TABLE` show only performance views rather than also showing `X$` and `D$` views. Route: `06_data_dictionary_performance_views.md`.
- `BUG-46266` - fixes wrong `V$LFG` values for `FIRST_DELETED_LOGFILE` and `LAST_DELETED_LOGFILE`. Route: `06_data_dictionary_performance_views.md`.
- `BUG-46383` - fixes a disk sort temp table hang caused by reading the wrong page. Route: `08_performance_tuning_monitoring.md`.
- `BUG-46384` - fixes disk sort temp table misbehavior or hang when an unfinished page is changed to another page. Route: `08_performance_tuning_monitoring.md`.
- `BUG-46322` - fixes an incorrect error in a specific merge join during disk sort temp table processing. Route: `08_performance_tuning_monitoring.md`.
- `BUG-46410` - fixes possible wrong row pointer setup in `sdcTempRow::filteringAndFetch()`. Route: `08_performance_tuning_monitoring.md` and `07_error_messages_troubleshooting.md`.
- `BUG-46442` - fixes a case where an error message is not set when a column value read from a file is invalid. Route: `07_error_messages_troubleshooting.md` and `14_utilities_operation_tools.md`.
- `BUG-46292` - fixes `aexport` binding a `BIGINT` Object Id as integer and raising `Numeric value out of range`. Route: `14_utilities_operation_tools.md`.
- `BUG-46295` - fixes generated SQL files failing when a view creation statement's final line contains a single-line comment. Route: `14_utilities_operation_tools.md` and `03_sql_ddl_generation.md`.
- `BUG-46310` - fixes invalid memory access when querying `V$REPRECEIVER_TRANSTBL` while the receiver is stopping. Route: `09_replication_ha_cdc.md` and `06_data_dictionary_performance_views.md`.
- `BUG-46314` - fixes replication update failure when column order differs between replication target tables on each server. Route: `09_replication_ha_cdc.md`.
- `BUG-46354` - prints an error message when HBT socket open fails. Route: `09_replication_ha_cdc.md` and `07_error_messages_troubleshooting.md`.
- `BUG-46369` - fixes repeated SenderApply restart attempts when tablespace full occurs during replication. Route: `09_replication_ha_cdc.md` and `02_administration_operations.md`.
- `BUG-46385` - fixes eager replication hang when replications are not started in create order. Route: `09_replication_ha_cdc.md`.
- `BUG-46276` - fixes hang when a transaction exists before eager replication failback flush state. Route: `09_replication_ha_cdc.md`.
- `BUG-46393` - fixes commit waits when only lazy-replication tables have transactions but eager replication is in `FLUSH FAILBACK` state. Route: `09_replication_ha_cdc.md`.
- `BUG-46400` - initializes all client communication module callback function lists. Route: `12_c_cli_odbc_precompiler.md`.
- `BUG-46277` - fixes repeated oraAdapter connection errors after Oracle server shutdown by no longer skipping the connection error. Route: `15_migration_oracle_compatibility.md`.
- `BUG-46403` - adds oraAdapter support for Oracle `TIMESTAMP`. Route: `15_migration_oracle_compatibility.md`.
- `BUG-46448` - fixes reversed microsecond values when `jdbcAdapter` inserts into a date column. Route: `11_java_jdbc_spring.md`.
- `BUG-46455` - fixes split partition on `RANGE_USING_HASH` partition tables not moving data. Route: `03_sql_ddl_generation.md`.
- `BUG-46469` - fixes missing `XA_PREPARE_REQ` log-name dump output. Route: `02_administration_operations.md` and `07_error_messages_troubleshooting.md`.

Compatibility and catalog caveat: database binary, meta, communication protocol, and replication protocol are unchanged for this patch. Changed property: `LOB_CACHE_THRESHOLD`; changed performance view: `V$TABLE`. Ask for exact patch, LOB settings, adapter version, object definitions, and replication state before claiming runtime root cause.

### Altibase 7.1.0.1.6 Patch Notes

Source row: `SRC-PATCH-PATCH-000004`.
Source file: `PatchNotes/Altibase_7.1/kor/Altibase_7_1_0_1_6_Patch_Notes.md`.
Version Info: database binary `6.5.1`, meta `8.6.1`, cm protocol version `7.1.6`, replication protocol `7.4.3`.

New features:

- `BUG-46406` - extends `MERGE` syntax. Route: `04_sql_dml_oracle_compatibility.md`.
- `BUG-46481` - adds system stored procedure `sleep2` for microsecond sleep. Route: `10_psm_stored_external_procedures.md`.
- `BUG-46402` - changes memory-index allocation handling for memory returned to mempool. Route: `08_performance_tuning_monitoring.md`.
- `BUG-46436` - adds a `time` item to Monitoring API `ABISqlText`. Route: `08_performance_tuning_monitoring.md`.
- `BUG-46480` - refactors internal functions for JDBC insert performance. Route: `11_java_jdbc_spring.md`.
- `BUG-46485` - changes iLoader double-data binding from `SQL_C_DOUBLE` to `SQL_C_CHAR` for performance. Route: `13_isql_iloader_basic_tools.md`.
- `BUG-46486` - improves iLoader performance by acquiring locks per array, not per record, when reading from buffers. Route: `13_isql_iloader_basic_tools.md`.

Fixed bugs:

- `BUG-46085` - frees `Query_Prepare` memory allocated while checking cached plans. Route: `08_performance_tuning_monitoring.md`.
- `BUG-46389` - adds the missing `silent` option to APRE usage. Route: `12_c_cli_odbc_precompiler.md`.
- `BUG-46390` - adds a missing check for whether the client session ended when an IPCDA session ends. Route: `12_c_cli_odbc_precompiler.md`.
- `BUG-46483` - fixes HP `jdbcAdapter` startup behavior when `LD_LIBRARY_PATH` is not set. Route: `11_java_jdbc_spring.md`.
- `BUG-46508` - fixes min/max statistics setup changing table meta-cache column information. Route: `08_performance_tuning_monitoring.md`.
- `BUG-46516` - fixes APRE PSM Array not working for newly created users. Route: `12_c_cli_odbc_precompiler.md` and `10_psm_stored_external_procedures.md`.

Compatibility and catalog caveat: database binary, meta, communication protocol, and replication protocol are unchanged; no added, changed, or deleted properties or performance views are listed. Ask for exact APRE/JDBC/iLoader build and runtime evidence before asserting applicability.

### Altibase 7.1.0.1.7 Patch Notes

Source row: `SRC-PATCH-PATCH-000005`.
Source file: `PatchNotes/Altibase_7.1/kor/Altibase_7_1_0_1_7_Patch_Notes.md`.
Version Info: database binary `6.5.1`, meta `8.6.1`, cm protocol version `7.1.6`, replication protocol `7.4.3`.

New features:

- `BUG-46418` - supports APRE host-variable data type `APRE_BINARY2`. Route: `12_c_cli_odbc_precompiler.md`.

Fixed bugs:

- `BUG-46519` - fixes abnormal termination when memory-allocation failure handling frees memory that was not allocated. Route: `02_administration_operations.md` and `07_error_messages_troubleshooting.md`.
- `BUG-46526` - fixes AIX iSQL connection output of `"grep: Not a recognized flag: m"`. Route: `13_isql_iloader_basic_tools.md`.

Compatibility and catalog caveat: database binary, meta, communication protocol, and replication protocol are unchanged; no added, changed, or deleted properties are listed, and no performance-view changes are intended. Ask for exact AIX/iSQL/APRE package evidence before asserting applicability.

### Altibase 7.1.0.1.8 Patch Notes

Source row: `SRC-PATCH-PATCH-000006`.
Source file: `PatchNotes/Altibase_7.1/kor/Altibase_7_1_0_1_8_Patch_Notes.md`.
Version Info: database binary `6.5.1`, meta `8.7.1`, cm protocol version `7.1.6`, replication protocol `7.4.4`.

New features:

- `BUG-46174` - extends stored procedures so `INSERT` and `UPDATE` can use record-type variables. Route: `10_psm_stored_external_procedures.md`.

Fixed bugs:

- `BUG-46120` - requires replication to fail when Active and Standby hash-partitioned tables have different partition counts. Route: `09_replication_ha_cdc.md` and `03_sql_ddl_generation.md`.
- `BUG-46396` - fixes an iSQL syntax error caused by a newline appended to the last line of DDL generated by `aexport`. Route: `14_utilities_operation_tools.md` and `13_isql_iloader_basic_tools.md`.
- `BUG-46515` - fixes omitted call stacks in `altibase_error.log` when `dumptrc` prints call stacks. Route: `14_utilities_operation_tools.md` and `07_error_messages_troubleshooting.md`.
- `BUG-46539` - fixes parser conflicts for `MERGE`. Route: `04_sql_dml_oracle_compatibility.md`.
- `BUG-46550` - fixes JDBC driver memory growth when `directByteBuffer` is used with `addBatch`. Route: `11_java_jdbc_spring.md`.
- `BUG-46551` - fixes `ArrayIndexOutOfBoundsException` when `jdbcAdapter` transfers data to Altibase `5.5.1`. Route: `11_java_jdbc_spring.md`.
- `BUG-46552` - changes iSQL so it does not use `/dev/null`. Route: `13_isql_iloader_basic_tools.md`.
- `BUG-46567` - fixes `dumpStack` concurrency issues. Route: `14_utilities_operation_tools.md` and `07_error_messages_troubleshooting.md`.
- `BUG-46572` - fixes APRE failure to recognize PSM arrays when packages are used. Route: `12_c_cli_odbc_precompiler.md` and `10_psm_stored_external_procedures.md`.
- `BUG-46574` - fixes restart failure after abnormal server termination during checkpoint image creation. Route: `02_administration_operations.md`.
- `BUG-46586` - fixes repeated error output during Service Time Failover (`STF`) retries. Route: `11_java_jdbc_spring.md`.
- `BUG-46598` - changes `V$REPGAP.REP_GAP` to a size unit. Route: `06_data_dictionary_performance_views.md` and `09_replication_ha_cdc.md`.

Compatibility and catalog caveat: database binary and communication protocol are unchanged. Meta changes from `8.6.1` to `8.7.1`, and patching from `7.1.0.1.7` or earlier to `7.1.0.1.8` performs an automatic meta upgrade. Replication protocol changes from `7.4.3` to `7.4.4` with backward compatibility. Added property: `REPLICATION_GAP_UNIT`; changed performance views: `V$REPGAP`, `V$REPGAP_PARALLEL`. Ask for exact replication mode and `V$VERSION` output before mixed-patch replication claims.

### Altibase 7.1.0.1.9 Patch Notes

Source row: `SRC-PATCH-PATCH-000007`.
Source file: `PatchNotes/Altibase_7.1/kor/Altibase_7_1_0_1_9_Patch_Notes.md`.
Version Info: database binary `6.5.1`, meta `8.7.1`, cm protocol version `7.1.6`, replication protocol `7.4.4`.

Fixed bugs:

- `BUG-45623` - fixes HP-UX HBT errors caused by using more sockets than allowed during connection checks. Route: `09_replication_ha_cdc.md`.
- `BUG-46296` - changes behavior so connection errors are not skipped when `OTHER_DATABASE_SKIP_ERROR` is `1`. Route: `15_migration_oracle_compatibility.md`.
- `BUG-46453` - fixes Service Time Failover (`STF`) `ASSERT` errors when `AlternateServers` is not set. Route: `11_java_jdbc_spring.md`.
- `BUG-46593` - adds logic to check host-variable array-size equality when PSM is called. Route: `12_c_cli_odbc_precompiler.md` and `10_psm_stored_external_procedures.md`.
- `BUG-46596` - adds defensive handling for data-file open failure. Route: `02_administration_operations.md`.
- `BUG-46607` - improves altiMon behavior on unsupported OS environments where `PICL` library files are missing. Route: `14_utilities_operation_tools.md` and `07_error_messages_troubleshooting.md`.
- `BUG-46608` - fixes receiver-side `Invalid protocol sequence` errors after replication HBT errors. Route: `09_replication_ha_cdc.md`.
- `BUG-46620` - supports altiMon on AIX 7. Route: `14_utilities_operation_tools.md`.
- `BUG-46625` - fixes IPCDA abnormal termination when no column matches a host variable. Route: `12_c_cli_odbc_precompiler.md`.

Compatibility and catalog caveat: database binary, meta, communication protocol, and replication protocol are unchanged; no added, changed, or deleted properties or performance views are listed. Ask for exact HP-UX/AIX, altiMon, HBT, IPCDA, and STF evidence before making root-cause claims.

### Altibase 7.1.0.2.0 Patch Notes

Source row: `SRC-PATCH-PATCH-000008`.
Source file: `PatchNotes/Altibase_7.1/kor/Altibase_7_1_0_2_0_Patch_Notes.md`.
Version Info: database binary `6.5.1`, meta `8.7.1`, cm protocol version `7.1.6`, replication protocol `7.4.4`.

Fixed bugs:

- `BUG-46502` - improves IPCDA stability on PowerPC. Route: `12_c_cli_odbc_precompiler.md`.
- `BUG-46594` - removes unnecessary locks during replication handshake. Route: `09_replication_ha_cdc.md`.
- `BUG-46644` - fixes a possible XA memory leak. Route: `02_administration_operations.md` and `12_c_cli_odbc_precompiler.md`.
- `BUG-46666` - fixes memory table size continuing to grow during LOB updates. Route: `05_data_types_properties.md` and `02_administration_operations.md`.
- `BUG-46678` - fixes return-buffer size calculation for functions whose return precision is not specified. Route: `10_psm_stored_external_procedures.md`.
- `BUG-46679` - fixes disk-table Hierarchy Query cases that raised `[ERR-311A4 : Loop in hierarchical query detected.]`. Route: `04_sql_dml_oracle_compatibility.md` and `07_error_messages_troubleshooting.md`.
- `BUG-46709` - fixes abnormal termination during `server stop` on AIX. Route: `01_getting_started_installation.md` and `02_administration_operations.md`.

Compatibility and catalog caveat: database binary, meta, communication protocol, and replication protocol are unchanged. The CM protocol section specifically warns that when IPCDA connection attributes are used, compatibility with `7.1.0.2.0` or lower is not guaranteed; patch both server and client to `7.1.0.2.0` or later for IPCDA. No added, changed, or deleted properties or performance views are listed. Ask for exact server/client patch and IPCDA use before compatibility claims.

### Altibase 7.1.0.2.1 Patch Notes

Source row: `SRC-PATCH-PATCH-000009`.
Source file: `PatchNotes/Altibase_7.1/kor/Altibase_7_1_0_2_1_Patch_Notes.md`.
Version Info: database binary `6.5.1`, meta `8.7.1`, cm protocol version `7.1.6`, replication protocol `7.4.4`.

New features:

- `BUG-46702` - supports `WITH ROLLUP`. Route: `04_sql_dml_oracle_compatibility.md`.
- `BUG-46806` - supports aliases in `INSERT` statements. Route: `04_sql_dml_oracle_compatibility.md`.
- `BUG-46703` - supports simple expressions in `LIMIT` clauses. Route: `04_sql_dml_oracle_compatibility.md`.
- `BUG-46719` - supports `SYSDATETIME`. Route: `04_sql_dml_oracle_compatibility.md`.
- `BUG-46727` - supports ISO standard-year `IYYY` format. Route: `04_sql_dml_oracle_compatibility.md`.
- `BUG-46755` - applies licenses issued by host name. Route: `01_getting_started_installation.md`.
- `BUG-46826` - improves DDL PVO stability. Route: `03_sql_ddl_generation.md` and `08_performance_tuning_monitoring.md`.
- `BUG-46781` - improves replication DDL safety. Route: `09_replication_ha_cdc.md`.
- `BUG-46825` - changes `OTHER_DATABASE_SKIP_ERROR` and `ORACLE_SKIP_ERROR` policy. Route: `15_migration_oracle_compatibility.md`.
- `BUG-46832` - optimizes simple queries on memory partition tables. Route: `08_performance_tuning_monitoring.md` and `04_sql_dml_oracle_compatibility.md`.

Fixed bugs:

- `BUG-46208` - fixes server startup failure when `REPLICATION_SENDER_AUTO_START` is set. Route: `09_replication_ha_cdc.md`, `02_administration_operations.md`, and `05_data_types_properties.md`.
- `BUG-46670` - fixes temp flusher access to an already freed temp table header. Route: `08_performance_tuning_monitoring.md`.
- `BUG-46680` - fixes lock timeout when replication sync is run twice on a CLOB-containing table while `INSERT_REPLACE` is `1`. Route: `09_replication_ha_cdc.md` and `05_data_types_properties.md`.
- `BUG-46697` - fixes hash-partition replication restart failing handshake because the partition count cannot be found. Route: `09_replication_ha_cdc.md` and `03_sql_ddl_generation.md`.
- `BUG-46700` - fixes memory table size continuing to grow when LOB columns are updated in memory tables. Route: `05_data_types_properties.md` and `02_administration_operations.md`.
- `BUG-46708` - changes Windows AltiLinker startup to find `java.exe`, not `java`. Route: `16_dblink_external_connectors.md`.
- `BUG-46728` - sets an `ORDER BY` host variable to the same `VARCHAR` type as the target. Route: `12_c_cli_odbc_precompiler.md` and `04_sql_dml_oracle_compatibility.md`.
- `BUG-46731` - handles `NOWAIT` for `INSERT` statements that use simple query. Route: `04_sql_dml_oracle_compatibility.md` and `08_performance_tuning_monitoring.md`.
- `BUG-46754` - fixes server restart failure when `logfile0` is missing. Route: `02_administration_operations.md`.
- `BUG-46757` - fixes abnormal characters in `V$DB_PROTOCOL` output. Route: `06_data_dictionary_performance_views.md`.
- `BUG-46782` - adds Begin Transaction debugging information. Route: `02_administration_operations.md` and `07_error_messages_troubleshooting.md`.
- `BUG-46800` - handles constant filters when an `ANTI JOIN` creates an `INVERSE HASH` plan. Route: `08_performance_tuning_monitoring.md` and `04_sql_dml_oracle_compatibility.md`.
- `BUG-46805` - fixes wrong results when two indexed subqueries in the target are identical except for the `WHERE` clause. Route: `04_sql_dml_oracle_compatibility.md`.
- `BUG-46816` - fixes memory overwrite when table names and user names are at least `128` characters. Route: `03_sql_ddl_generation.md` and `07_error_messages_troubleshooting.md`.
- `BUG-46836` - fixes `NOWAIT` option not being applied for `SELECT FOR UPDATE` when simple query optimization is used. Route: `04_sql_dml_oracle_compatibility.md` and `08_performance_tuning_monitoring.md`.

Compatibility and catalog caveat: database binary, meta, communication protocol, and replication protocol are unchanged. Changed property: `EXECUTOR_FAST_SIMPLE_QUERY`; no added, changed, or deleted performance views are listed. Ask for exact simple-query settings, SQL text, object definitions, replication state, and installed patch before asserting behavior.

### Altibase 7.1.0.2.2 Patch Notes

Source row: `SRC-PATCH-PATCH-000010`.
Source file: `PatchNotes/Altibase_7.1/kor/Altibase_7_1_0_2_2_Patch_Notes.md`.
Version Info: database binary `6.5.1`, meta `8.7.1`, cm protocol version `7.1.6`, replication protocol `7.4.4`.

Fixed bugs:

- `BUG-46602` - fixes inaccurate `V$REPGAP.REP_GAP` values when Replication GAP is at least `4G` (`unsigned int max`). Route: `06_data_dictionary_performance_views.md` and `09_replication_ha_cdc.md`.

Compatibility and catalog caveat: database binary, meta, communication protocol, and replication protocol are unchanged; no added, changed, or deleted properties or performance views are listed. Ask for exact replication topology, `V$REPGAP` output, and installed patch before attributing a gap-value issue to this fix.

### Altibase 7.1.0.2.3 Patch Notes

Source row: `SRC-PATCH-PATCH-000011`.
Source file: `PatchNotes/Altibase_7.1/kor/Altibase_7_1_0_2_3_Patch_Notes.md`.
Version Info: database binary `6.5.1`, meta `8.7.1`, cm protocol version `7.1.6`, replication protocol `7.4.4`.

New features:

- `BUG-46837` - improves the error message printed when a replication Sender tries to connect to a dropped Receiver. Route: `09_replication_ha_cdc.md` and `07_error_messages_troubleshooting.md`.
- `BUG-46866` - adds the `SERIAL_FILTER` hint and `SERIAL_EXECUTE_MODE` property for serial filter execution; the plan can show `[ FILTER SERIAL EXECUTE ]`. Route: `04_sql_dml_oracle_compatibility.md`, `05_data_types_properties.md`, and `08_performance_tuning_monitoring.md`.
- `BUG-46882` - allows a tablespace clause when creating a `QUEUE`. Route: `03_sql_ddl_generation.md`.
- `BUG-46883` - adds anonymous block support. Route: `10_psm_stored_external_procedures.md`.

Fixed bugs:

- `BUG-46529` - corrects `REPLICATION_DDL_ENABLE_LEVEL` error text under `REPLICATION_DDL_ENABLE` options, including `ERR-6117F` cases. Route: `09_replication_ha_cdc.md`, `05_data_types_properties.md`, and `07_error_messages_troubleshooting.md`.
- `BUG-46661` - fixes intermittent Receiver data conflict during Online DDL on a replicated table. Route: `09_replication_ha_cdc.md` and `03_sql_ddl_generation.md`.
- `BUG-46803` - fixes intermittent server startup failure when the license was issued by host name. Route: `01_getting_started_installation.md` and `07_error_messages_troubleshooting.md`.
- `BUG-46804` - counts execute-success statistics when an IPCDA fast simple query runs. Route: `12_c_cli_odbc_precompiler.md` and `08_performance_tuning_monitoring.md`.
- `BUG-46885` - prevents segmentation faults when a NULL handle is passed to CLI functions, including `SQLProcedureColumns`, `SQLProcedures`, `SQLSpecialColumns`, `SQLStatistics`, `SQLTablePrivileges`, `SQLBulkOperations`, `SQLCancel`, and `SQLSetPos`. Route: `12_c_cli_odbc_precompiler.md` and `07_error_messages_troubleshooting.md`.
- `BUG-46889` - fixes a segmentation fault when `SQLGetLob()` or `SQLGetLobLength()` is called before `SQLFetch()` after `SQLExecute()`. Route: `12_c_cli_odbc_precompiler.md` and `05_data_types_properties.md`.
- `BUG-46890` - records additional diagnostics when an assert occurs because legacy statement creation fails. Route: `07_error_messages_troubleshooting.md` and `08_performance_tuning_monitoring.md`.
- `BUG-46891` - fixes replication sync success/fail reporting when a conflict leaves data inconsistent. Route: `09_replication_ha_cdc.md`.
- `BUG-46893` - fixes AIX altiMon PICL `SWAP_FREE` reporting to use KB units. Route: `14_utilities_operation_tools.md`.
- `BUG-46903` - corrects the Administrator manual "media recovery case 4" recovery flow so an invalid `UNTIL TIME` recovery fails when required log files are missing; related token: `smERR_ABORT_ERR_LOG_CONSISTENCY`. Route: `02_administration_operations.md` and `07_error_messages_troubleshooting.md`.
- `BUG-46910` - fixes replication Sync incorrectly failing when data is added or deleted during sync even though sync actually succeeded. Route: `09_replication_ha_cdc.md`.

Compatibility and catalog caveat: database binary, meta, communication protocol, and replication protocol are unchanged. PSM/package caveat: when upgrading or patching from 6.3.1 through `7.1.0.2.2` to `7.1.0.2.3` or later, PSM that uses host variables with `:` must be revised, for example `:var` to `var`. Added property: `SERIAL_EXECUTE_MODE`; no added, changed, or deleted performance views are listed. Ask for exact patch, PSM source, replication topology, IPCDA/CLI usage, and recovery logs before asserting applicability.

### Altibase 7.1.0.2.4 Patch Notes

Source row: `SRC-PATCH-PATCH-000012`.
Source file: `PatchNotes/Altibase_7.1/kor/Altibase_7_1_0_2_4_Patch_Notes.md`.
Version Info: database binary `6.5.1`, meta `8.7.1`, cm protocol version `7.1.7`, replication protocol `7.4.5`.

New features:

- `BUG-46892` - adds Mathematics memory limiting and Mathematics Temp monitoring, including `V$STATEMENT.MATHEMATICS_TEMP_MEMORY` and the `MATHEMATICS_TEMP_MEMORY_MAXIMUM` property. Route: `04_sql_dml_oracle_compatibility.md`, `05_data_types_properties.md`, `06_data_dictionary_performance_views.md`, and `08_performance_tuning_monitoring.md`.

Fixed bugs:

- `BUG-46940` - fixes a replication start case where XLOG is not sent to the Receiver after drop/recreate and restartXSN metadata drift. Route: `09_replication_ha_cdc.md`.
- `BUG-46942` - fixes abnormal termination when a target expression such as `NVL` is aliased, a join exists, and `ORDER BY` calculates that alias. Route: `04_sql_dml_oracle_compatibility.md`, `08_performance_tuning_monitoring.md`, and `07_error_messages_troubleshooting.md`.
- `BUG-46955` - improves memory index POINTER BASE BOTTOM-UP build speed. Route: `08_performance_tuning_monitoring.md`.
- `BUG-46977` - allows `?` bind markers in anonymous block `SELECT ... INTO ?` syntax, including JDBC `prepareCall` cases. Route: `10_psm_stored_external_procedures.md` and `11_java_jdbc_spring.md`.

Compatibility and catalog caveat: database binary and meta are unchanged. Communication protocol changes from `7.1.6` to `7.1.7` with backward compatibility, and replication protocol changes from `7.4.4` to `7.4.5` with backward compatibility. Added property: `MATHEMATICS_TEMP_MEMORY_MAXIMUM`; changed performance view: `V$STATEMENT`. Ask for exact `V$VERSION`, SQL text, plan, and replication state before mixed-patch or root-cause claims.

### Altibase 7.1.0.2.5 Patch Notes

Source row: `SRC-PATCH-PATCH-000013`.
Source file: `PatchNotes/Altibase_7.1/kor/Altibase_7_1_0_2_5_Patch_Notes.md`.
Version Info: database binary `6.5.1`, meta `8.7.1`, cm protocol version `7.1.7`, replication protocol `7.4.5`.

New features:

- `BUG-46878` - fixes DBLink startup failure with Java version 9 or later; the note explains that an error can be logged because the Java `-d64` option was removed in Java 9 or later. Route: `16_dblink_external_connectors.md` and `11_java_jdbc_spring.md`.

Fixed bugs:

- `BUG-46938` - fixes a performance issue after adding `getStatus` and `setStatus` to reuse all Mathematics function data. Route: `04_sql_dml_oracle_compatibility.md` and `08_performance_tuning_monitoring.md`.
- `BUG-46957` - improves customer-facing Cause and Action text for `cmERR_ABORT_INVALID_OPERATION = Invalid operation`. Route: `07_error_messages_troubleshooting.md`.
- `BUG-46977` - allows `?` bind markers in anonymous block `SELECT ... INTO ?` syntax. Route: `10_psm_stored_external_procedures.md` and `11_java_jdbc_spring.md`.
- `BUG-47043` - fixes server startup failure after the server is killed during checkpoint. Route: `02_administration_operations.md` and `07_error_messages_troubleshooting.md`.
- `BUG-47048` - fixes `aexport` generated scripts omitting the QUEUE tablespace clause, including queues created in `DISK_SYSTEM_DATA`. Route: `14_utilities_operation_tools.md` and `03_sql_ddl_generation.md`.
- `BUG-47051` - fixes `Function sequence error` or `[ERR-4103A : Invalid statement processing request]` when a procedure returning a ResultSet is executed after `set explainplan on/only`. Route: `13_isql_iloader_basic_tools.md`, `10_psm_stored_external_procedures.md`, and `07_error_messages_troubleshooting.md`.

Compatibility and catalog caveat: database binary, meta, communication protocol, and replication protocol are unchanged; no added, changed, or deleted properties or performance views are listed. Ask for exact Java/JDBC/DBLink versions, `aexport` output, iSQL settings, and server logs before asserting applicability.

### Altibase 7.1.0.2.6 Patch Notes

Source row: `SRC-PATCH-PATCH-000014`.
Source file: `PatchNotes/Altibase_7.1/kor/Altibase_7_1_0_2_6_Patch_Notes.md`.
Version Info: database binary `6.5.1`, meta `8.7.1`, cm protocol version `7.1.7`, replication protocol `7.4.5`.

New features:

- `BUG-46824` - adds APRE support for anonymous blocks. Route: `12_c_cli_odbc_precompiler.md` and `10_psm_stored_external_procedures.md`.
- `BUG-46887` - supports the `DBMS_METADATA` package and provides `$ALTIBASE_HOME/packages/dbms_metadata.sql` and `$ALTIBASE_HOME/packages/dbms_metadata.plb` for querying DDL for database objects. Route: `10_psm_stored_external_procedures.md` and `14_utilities_operation_tools.md`.
- `BUG-46922` - improves memory reuse for `Percentile_Cont` and `Percentile_Disc`. Route: `04_sql_dml_oracle_compatibility.md` and `08_performance_tuning_monitoring.md`.
- `BUG-47082` - improves VALUE BASE BOTTOM-UP memory index build speed, improves startup index build speed for VALUE BASE indexes, reduces extra build memory by half, and changes `MEMORY_INDEX_BUILD_RUN_SIZE`. Route: `08_performance_tuning_monitoring.md` and `05_data_types_properties.md`.

Fixed bugs:

- `BUG-46409` - fixes uninitialized metadata in an `ALTER REPLICATION SET` syntax path. Route: `09_replication_ha_cdc.md`.
- `BUG-46783` - fixes copying an already-freed replication name when the Receiver exits during DDL under replication. Route: `09_replication_ha_cdc.md` and `07_error_messages_troubleshooting.md`.
- `BUG-46879` - fixes jdbcAdapter startup under OpenJDK11 and records JVM stderr in `$ALTIBASE_HOME/trc/stderr.log`. Route: `11_java_jdbc_spring.md`, `15_migration_oracle_compatibility.md`, and `07_error_messages_troubleshooting.md`.
- `BUG-47090` - fixes the function that blocks remote SYSDBA connection on AIX and HP systems. Route: `01_getting_started_installation.md`, `02_administration_operations.md`, and `18_security_ssl_tls.md`.
- `BUG-47095` - fixes missing memory initialization during partition simple query execution. Route: `04_sql_dml_oracle_compatibility.md` and `08_performance_tuning_monitoring.md`.
- `BUG-47105` - checks whether CPUs are online or offline so server boot does not fail on Linux platforms with only some CPUs active. Route: `01_getting_started_installation.md` and `02_administration_operations.md`.
- `BUG-47115` - fixes `StackOverflowError` during jdbcAdapter tests in an OpenJDK11 environment. Route: `11_java_jdbc_spring.md`.
- `BUG-47119` - fixes memory access caused by wrong packet calculation when sending `sendHandshakeAck` during replication connection. Route: `09_replication_ha_cdc.md` and `07_error_messages_troubleshooting.md`.
- `BUG-47121` - fixes jdbcAdapter configuration so `OTHER_DATABASE_JDBC_MAX_HEAP_SIZE` is used consistently instead of the mismatched `OTHER_DATABASE_JDBC_JVM_MAX_HEAP_SIZE`. Route: `11_java_jdbc_spring.md` and `15_migration_oracle_compatibility.md`.
- `BUG-47126` - fixes iSQL segmentation fault when a long value is assigned to a host variable because the string buffer was fixed at length `256`. Route: `13_isql_iloader_basic_tools.md` and `12_c_cli_odbc_precompiler.md`.
- `BUG-47128` - fixes `query_binding` memory growth when a prepared statement with binds is repeatedly executed and query rebuild occurs. Route: `04_sql_dml_oracle_compatibility.md` and `08_performance_tuning_monitoring.md`.
- `BUG-47135` - fixes OpenJDK altiMon JVM creation failure, including `altimon_stderr.log` output such as `Could not create the Java Virtual Machine`. Route: `14_utilities_operation_tools.md` and `11_java_jdbc_spring.md`.
- `BUG-47136` - fixes tablespace usage calculation during tablespace swap/table movement that could raise `[ERR-3144E : Need more free space of tablespace.]`. Route: `02_administration_operations.md` and `03_sql_ddl_generation.md`.
- `BUG-47140` - fixes replication start failure with lower-version peers when hash-partitioned table partition counts are actually the same. Route: `09_replication_ha_cdc.md` and `03_sql_ddl_generation.md`.
- `BUG-47142` - fixes excessive memory/error handling for HASH joins on tables with `BLOB` and `DECIMAL` columns, including the expected `LOB and GEOMETRY type data cannot be displayed` behavior. Route: `04_sql_dml_oracle_compatibility.md`, `05_data_types_properties.md`, and `08_performance_tuning_monitoring.md`.
- `BUG-47173` - improves fast simple query handling when host variable precision is larger than a `CHAR` or `VARCHAR` column size; source workaround uses `NO_EXEC_FAST`. Route: `04_sql_dml_oracle_compatibility.md`, `12_c_cli_odbc_precompiler.md`, and `08_performance_tuning_monitoring.md`.
- `BUG-47195` - fixes server restart failure after abnormal termination following `PARTITION SWAP`. Route: `02_administration_operations.md` and `03_sql_ddl_generation.md`.

Compatibility and catalog caveat: database binary, meta, communication protocol, and replication protocol are unchanged. Changed property: `MEMORY_INDEX_BUILD_RUN_SIZE`; no added, changed, or deleted performance views are listed. Ask for exact OpenJDK version, adapter configuration, replication peer patch, SQL, tablespace layout, and startup logs before asserting production safety.

### Altibase 7.1.0.2.7 Patch Notes

Source row: `SRC-PATCH-PATCH-000015`.
Source file: `PatchNotes/Altibase_7.1/kor/Altibase_7_1_0_2_7_Patch_Notes.md`.
Version Info: database binary `6.5.1`, meta `8.7.1`, cm protocol version `7.1.7`, replication protocol `7.4.5`.

New features:

- `BUG-47159` - applies the `DBMS_METADATA` package to `aexport`. Route: `14_utilities_operation_tools.md` and `10_psm_stored_external_procedures.md`.

Fixed bugs:

- `BUG-45933` - fixes decimal-value truncation when APRE uses `APRE_NUMERIC`. Route: `12_c_cli_odbc_precompiler.md` and `05_data_types_properties.md`.
- `BUG-46019` - removes unnecessary data transmission when `PRINT` is used in a procedure. Route: `10_psm_stored_external_procedures.md`, `06_data_dictionary_performance_views.md`, and `08_performance_tuning_monitoring.md`.

Compatibility and catalog caveat: database binary, meta, communication protocol, and replication protocol are unchanged. No added, changed, or deleted properties are listed; changed performance view: `V$SESSION`. Ask for exact APRE numeric definition, PSM output path, `aexport` command, and `V$SESSION` query before claiming behavior.

### Altibase 7.1.0.2.8 Patch Notes

Source row: `SRC-PATCH-PATCH-000016`.
Source file: `PatchNotes/Altibase_7.1/kor/Altibase_7_1_0_2_8_Patch_Notes.md`.
Version Info: database binary `6.5.1`, meta `8.7.1`, cm protocol version `7.1.7`, replication protocol `7.4.5`.

Fixed bugs:

- `BUG-47149` - fixes a standby-server crash when `V$REPRECEIVER_TRANSTBL` is queried during a transaction abort that includes conflict; the source notes `LOCAL_TID`. Route: `09_replication_ha_cdc.md` and `06_data_dictionary_performance_views.md`.
- `BUG-47155` - fixes active-active replication where only one direction starts because `updateXSN()` updates with an SN greater than the Sender's `mXSN`. Route: `09_replication_ha_cdc.md`.
- `BUG-47306` - fixes Online DDL failure when multiple replications are configured. Route: `09_replication_ha_cdc.md` and `03_sql_ddl_generation.md`.
- `BUG-47325` - fixes iSQL result wrapping at the wrong position when output contains newline characters. Route: `13_isql_iloader_basic_tools.md`.
- `BUG-47334` - fixes the inability to set `SORT_AREA_SIZE` and `HASH_AREA_SIZE` above `32GB`; the source workaround mentions values at or below `34331426816`. Route: `05_data_types_properties.md` and `08_performance_tuning_monitoring.md`.
- `BUG-47359` - adds missing `SQL_NUMERIC_STRUCT` to APRE `-keyword` output. Route: `12_c_cli_odbc_precompiler.md`.
- `BUG-47361` - makes `IS NOT NULL` eligible for `SERIAL EXECUTE` with `serial_execute_mode=1`; the plan can show `[ FILTER SERIAL EXECUTE ]`. Route: `04_sql_dml_oracle_compatibility.md`, `05_data_types_properties.md`, and `08_performance_tuning_monitoring.md`.
- `BUG-47364` - adds missing exception handling in File Resize Recovery. Route: `02_administration_operations.md` and `07_error_messages_troubleshooting.md`.

Compatibility and catalog caveat: database binary, meta, communication protocol, and replication protocol are unchanged; no added, changed, or deleted properties or performance views are listed. Ask for exact replication topology, `V$REPRECEIVER_TRANSTBL` query, iSQL output, property values, and recovery logs before asserting applicability.

### Altibase 7.1.0.2.9 Patch Notes

Source row: `SRC-PATCH-PATCH-000017`.
Source file: `PatchNotes/Altibase_7.1/kor/Altibase_7_1_0_2_9_Patch_Notes.md`.
Version Info: database binary `6.5.1`, meta `8.7.1`, cm protocol version `7.1.7`, replication protocol `7.4.5`.

Fixed bugs:

- `BUG-47020` - fixes replication packet transmission so compression failure is not treated as success and an error log is recorded. Route: `09_replication_ha_cdc.md` and `07_error_messages_troubleshooting.md`.
- `BUG-47385` - adds protection against memory index `fetchNext` hangs when leaf-node links become abnormal. Route: `08_performance_tuning_monitoring.md` and `02_administration_operations.md`.
- `BUG-47387` - fixes FAC (`Fetch Across Commit`) memory growth when statement close is not followed by commit by updating the min view SCN when the statement ends. Route: `04_sql_dml_oracle_compatibility.md` and `08_performance_tuning_monitoring.md`.
- `BUG-47393` - fixes abnormal termination during meta upgrade from `8.0.1` through `8.3.1` to `8.4.1` or later. Route: `01_getting_started_installation.md` and `02_administration_operations.md`.

Compatibility and catalog caveat: database binary, meta, communication protocol, and replication protocol are unchanged; no added, changed, or deleted properties or performance views are listed. Ask for exact meta version, upgrade path, replication compression setting, FAC workload, and memory-index evidence before root-cause claims.

### Altibase 7.1.0.3.0 Patch Notes

Source row: `SRC-PATCH-PATCH-000018`.
Source file: `PatchNotes/Altibase_7.1/kor/Altibase_7_1_0_3_0_Patch_Notes.md`.
Version Info: database binary `6.5.1`, meta `8.7.1`, cm protocol version `7.1.7`, replication protocol `7.4.5`.

New features:

- `BUG-47347` - allows Partition Split while DML-related locks exist. Route: `03_sql_ddl_generation.md` and `02_administration_operations.md`.
- `BUG-47416` - removes the `2GB - 1byte` limit for CLI LOB file binding with `SQLBindFileToParam`; the maximum becomes `4,294,967,295 bytes (4GB-1byte)`. Route: `12_c_cli_odbc_precompiler.md` and `05_data_types_properties.md`.
- `BUG-47456` - adds support for updating 4 GB data through `updateBinaryStream()` by supporting a long-length interface. Route: `11_java_jdbc_spring.md` and `05_data_types_properties.md`.
- `BUG-47431` - improves the query used by APRE to check PSM Array information. Route: `12_c_cli_odbc_precompiler.md`, `10_psm_stored_external_procedures.md`, and `08_performance_tuning_monitoring.md`.
- `BUG-47436` - allows altiMon Altibase connection settings to include additional connection properties through `<ConnectionProperties>`, such as `login_timeout=3;fetch_timeout=60`. Route: `14_utilities_operation_tools.md`.
- `BUG-47437` - passes metric name, level, threshold value, and measured value as arguments when altiMon runs an action script. Route: `14_utilities_operation_tools.md`.
- `BUG-47434` - includes error codes when printing errors returned from SQLCLI, including altiComp/audit utility paths. Route: `14_utilities_operation_tools.md`, `12_c_cli_odbc_precompiler.md`, and `07_error_messages_troubleshooting.md`.

Fixed bugs:

- `BUG-46632` - prints memory-dump TRACE LOG output up to `2KB` when the trace log exceeds `2KB`. Route: `07_error_messages_troubleshooting.md` and `14_utilities_operation_tools.md`.
- `BUG-47371` - avoids setting the replication flag on a table partition that is not a replication target. Route: `09_replication_ha_cdc.md` and `03_sql_ddl_generation.md`.
- `BUG-47404` - fixes an incorrect WAL (`Write-Ahead Logging`) check during restart recovery. Route: `02_administration_operations.md` and `07_error_messages_troubleshooting.md`.
- `BUG-47410` - fixes abnormal termination when `cross apply (Lateral View)` is used with a Leading Hint. Route: `04_sql_dml_oracle_compatibility.md` and `08_performance_tuning_monitoring.md`.
- `BUG-47412` - reduces `EXECUTE_STMT_MEMORY` usage by revising the PSM object dependency-check query. Route: `10_psm_stored_external_procedures.md` and `08_performance_tuning_monitoring.md`.
- `BUG-47414` - fixes wrong results when `outer apply (Lateral View)` is used on disk tables. Route: `04_sql_dml_oracle_compatibility.md` and `08_performance_tuning_monitoring.md`.
- `BUG-47415` - returns `[ERR-11189 : The length of the path is zero.]` when the log-anchor backup path is empty instead of abnormal termination. Route: `02_administration_operations.md` and `07_error_messages_troubleshooting.md`.
- `BUG-47424` - fixes `StringIndexOutOfBoundsException` when escaping SQL that includes `{ ? = call }`. Route: `11_java_jdbc_spring.md` and `10_psm_stored_external_procedures.md`.
- `BUG-47461` - fixes partial parameter truncation in `isql` and `iloader` on Windows 2016. Route: `13_isql_iloader_basic_tools.md`.

Compatibility and catalog caveat: database binary, meta, communication protocol, and replication protocol are unchanged; no added, changed, or deleted properties or performance views are listed. Ask for exact CLI/JDBC/altiMon/iSQL/iLoader versions, LOB size, SQL text, partition DDL, and recovery logs before asserting applicability.

### Altibase 7.1.0.3.1 Patch Notes

Source row: `SRC-PATCH-PATCH-000019`.
Source file: `PatchNotes/Altibase_7.1/kor/Altibase_7_1_0_3_1_Patch_Notes.md`.
Version Info: database binary `6.5.1`, meta `8.7.1`, cm protocol version `7.1.7`, replication protocol `7.4.5`.

New features:

- `BUG-47458` - adds LOB type support to replication SQL Apply. Route: `09_replication_ha_cdc.md` and `05_data_types_properties.md`.
- `BUG-47489` - supports multiple update and multiple delete syntax. Route: `04_sql_dml_oracle_compatibility.md` and `03_sql_ddl_generation.md`.

Fixed bugs:

- `BUG-47219` - fixes a possible hang/deadlock when global transactions and replication are used together and the replication Sender starts while XA pending transactions and table locks contend. Route: `09_replication_ha_cdc.md` and `02_administration_operations.md`.
- `BUG-47472` - records `V$LOCK` and `V$LOCK_WAIT` information in `altibase_dump.log` when a Sender is suspended during replication auto-start at server startup. Route: `09_replication_ha_cdc.md`, `06_data_dictionary_performance_views.md`, `07_error_messages_troubleshooting.md`, and `02_administration_operations.md`.
- `BUG-47474` - fixes abnormal termination when memory-index internal-node search touches an already removed var slot before re-search. Route: `08_performance_tuning_monitoring.md` and `02_administration_operations.md`.
- `BUG-47509` - fixes wrong inner-join results when a composite index exists and an `OR` predicate in `WHERE` is merged with an `ON` predicate. Route: `04_sql_dml_oracle_compatibility.md` and `08_performance_tuning_monitoring.md`.
- `BUG-47516` - fixes invalid memory free behavior when `__PSM_STATEMENT_LIST_COUNT=0`. Route: `10_psm_stored_external_procedures.md`, `05_data_types_properties.md`, and `07_error_messages_troubleshooting.md`.

Compatibility and catalog caveat: database binary, meta, communication protocol, and replication protocol are unchanged; no added, changed, or deleted properties or performance views are listed. Ask for exact global transaction state, replication startup logs, SQL text, index definitions, and PSM property settings before asserting applicability.

### Altibase 7.1.0.3.2 Patch Notes

Source row: `SRC-PATCH-PATCH-000020`.
Source file: `PatchNotes/Altibase_7.1/kor/Altibase_7_1_0_3_2_Patch_Notes.md`.
Version Info: database binary `6.5.1`, meta `8.7.1`, cm protocol version `7.1.7`, replication protocol `7.4.5`.

New features:

- `BUG-47388` - improves the TABLE LOCK bottleneck by removing Spin Lock mode, adding Light Mutex mode, and changing `LOCK_MGR_TYPE` max value from `1` to `2`; settings for `LOCK_MGR_SPIN_COUNT`, `LOCK_MGR_MIN_SLEEP`, `LOCK_MGR_MAX_SLEEP`, and `LOCK_MGR_DETECTDEADLOCK_INTERVAL` are ignored, and startup can report `ERR-111b6(errno=9) LOCK_MGR_TYPE 1 is deprecated.` when `LOCK_MGR_TYPE=1`. Route: `02_administration_operations.md`, `05_data_types_properties.md`, and `08_performance_tuning_monitoring.md`.

Fixed bugs:

- `BUG-47344` - fixes APRE parser conflicts during compile. Route: `12_c_cli_odbc_precompiler.md`.
- `BUG-47492` - fixes `login_timeout` not being applied when the server is hung; the source workaround is `response_timeout`. Route: `11_java_jdbc_spring.md` and `12_c_cli_odbc_precompiler.md`.
- `BUG-47522` - fixes abnormal termination when a `CONNECT BY` clause has a subquery as a variable key; the source workaround mentions `__OPTIMIZER_HIERARCHY_TRANSFORMATION=1`. Route: `04_sql_dml_oracle_compatibility.md`, `05_data_types_properties.md`, and `08_performance_tuning_monitoring.md`.
- `BUG-47538` - changes the log-anchor backup failure message for insufficient space from messages such as `Disk Space was insufficient during archive log backup. Check Space!!` and `Skip archiveing logfile(...)` to `Log anchor file backup has failed!!`. Route: `02_administration_operations.md` and `07_error_messages_troubleshooting.md`.
- `BUG-47541` - fixes APRE handling of `\"` that raised `[ERR-306L : Unterminated string error.]` during precompile. Route: `12_c_cli_odbc_precompiler.md` and `07_error_messages_troubleshooting.md`.
- `BUG-47551` - fixes wrong results when `COALESCE` is used and OUTER JOIN ELIMINATION is set incorrectly; the source workaround mentions `__OPTIMIZER_OUTERJOIN_ELIMINATION=0`. Route: `04_sql_dml_oracle_compatibility.md`, `05_data_types_properties.md`, and `08_performance_tuning_monitoring.md`.

Compatibility and catalog caveat: database binary, meta, communication protocol, and replication protocol are unchanged. Changed property: `LOCK_MGR_TYPE`; no added, changed, or deleted performance views are listed. Ask for exact lock-manager properties, APRE source, client timeout properties, SQL text, optimizer-property state, and log-anchor backup logs before asserting applicability.

## Attachment Cross-References

- `01_getting_started_installation.md`: installer, package, first-run, startup, shutdown, and patch rollback procedures.
- `02_administration_operations.md`: operational upgrade prerequisites, backup, recovery, and rollback safety checks.
- `05_data_types_properties.md`: version-sensitive properties, data types, JSON, Temporary LOB, and range/default details.
- `09_replication_ha_cdc.md`: replication protocol compatibility, DDL synchronization, receive-only, and replication SSL operations.
- `11_java_jdbc_spring.md`, `12_c_cli_odbc_precompiler.md`, and `18_security_ssl_tls.md`: client protocol, driver, Java, ODBC/CLI, OpenSSL, and TLS details.
- `14_utilities_operation_tools.md`, `17_kubernetes_aku_cloud.md`, and `19_spatial_nifi_tableau_misc.md`: release-note-routed tool, AKU, KADA/Kafka/ABM, Spatial, NiFi, Tableau, and miscellaneous integration topics.

## Residual Scope

- Release-note-only feature families are kept to version awareness and routing. Do not turn those bullets into operational procedures unless a dedicated source-backed block provides the procedure.
