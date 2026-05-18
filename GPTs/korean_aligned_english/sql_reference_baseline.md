# Korean-Aligned English Baseline: SQL Reference Batch

- Job: `S1-J008`
- Scope: SQL Reference DDL, DCL, DML, administrative SQL, replication SQL,
  check SQL, data types, JSON, LOB, Temporary LOB, functions, expressions,
  Oracle-difference SQL, General Reference properties, dictionary and
  performance views, error codes, and troubleshooting response structure.
- Source-pack gate: `GPTs/source_pack/source_pack_validation.md` records
  `Status: pass`, `Verdict: Pass`, no blockers, and the explicit gate for
  continuing to the Korean-aligned English baseline.
- Authority rule: Korean product manuals are authoritative. English product
  manuals are extraction aids. For 8.1 material, preserve the established
  `Altibase 8.1 verified source` boundary.
- Downstream boundary: this file is a working baseline, not a final GPT upload
  package. It does not replace exact source-pack extraction, item-level SQL
  grammar conversion, property-by-property normalization, view-column
  extraction, or exact error-code maps.

## Batch Source Coverage

| Source family | Version scope | Korean source IDs | English source IDs | Baseline manifest rows |
| --- | --- | --- | --- | --- |
| `sql_reference` | 7.1, 7.3, `Altibase 8.1 verified source` | `SRC-000072`, `SRC-000134`, `SRC-000194` | `SRC-000040`, `SRC-000103`, `SRC-000163` | `KAE-BLOCK-000035`, `KAE-BLOCK-000166`, `KAE-BLOCK-000223` |
| `general_reference_1_datatypes_properties` | 7.1, 7.3, `Altibase 8.1 verified source` | `SRC-000056`, `SRC-000120`, `SRC-000180` | `SRC-000025`, `SRC-000089`, `SRC-000150` | `KAE-BLOCK-000010`, `KAE-BLOCK-000145`, `KAE-BLOCK-000201` |
| `general_reference_2_dictionary_views` | 7.1, 7.3, `Altibase 8.1 verified source` | `SRC-000057`, `SRC-000121`, `SRC-000181` | `SRC-000026`, `SRC-000090`, `SRC-000151` | `KAE-BLOCK-000011`, `KAE-BLOCK-000146`, `KAE-BLOCK-000202` |
| `error_message_reference` | 7.1, 7.3, `Altibase 8.1 verified source` | `SRC-000054`, `SRC-000118`, `SRC-000178` | `SRC-000023`, `SRC-000087`, `SRC-000148` | `KAE-BLOCK-000009`, `KAE-BLOCK-000144`, `KAE-BLOCK-000200` |
| `administrator_operations` and `replication_manual` support | 7.1, 7.3, `Altibase 8.1 verified source` | `SRC-000049`, `SRC-000113`, `SRC-000173`, `SRC-000070`, `SRC-000132`, `SRC-000192` | `SRC-000018`, `SRC-000082`, `SRC-000143`, `SRC-000038`, `SRC-000101`, `SRC-000161` | `KAE-BLOCK-000001`, `KAE-BLOCK-000136`, `KAE-BLOCK-000191`, `KAE-BLOCK-000029`, `KAE-BLOCK-000162`, `KAE-BLOCK-000217` |

## KAE-SQLREF-BLOCK-001: SQL Statement Family Boundary

- Source IDs: `SRC-000072`, `SRC-000040`, `SRC-000134`, `SRC-000103`,
  `SRC-000194`, `SRC-000163`.
- Version scope: 7.1, 7.3, and `Altibase 8.1 verified source`.
- Source block refs: `SRC-000072/BLOCK-000884`, `SRC-000040/BLOCK-000883`,
  `SRC-000134/BLOCK-000886`, `SRC-000103/BLOCK-000885`,
  `SRC-000194/BLOCK-000888`, `SRC-000163/BLOCK-000887`.
- Alignment status: baseline generated from paired Korean authority and English
  extraction aids. Full BNF conversion for every statement remains not-ready.

Baseline:

1. Treat Altibase SQL as source-classified into DDL, DML, and DCL before
   generating customer SQL. Preserve the SQL Reference classification even
   when it differs from generic database assumptions; for example, `GRANT` and
   `REVOKE` appear in the SQL Reference statement inventory rather than being
   inferred from another database.
2. SQL generation must preserve exact Altibase statement tokens such as
   `ALTER DATABASE`, `CREATE DATABASE`, `DROP DATABASE`, `CREATE DISK
   TABLESPACE`, `CREATE MEMORY TABLESPACE`, `CREATE VOLATILE TABLESPACE`,
   `CREATE TEMPORARY TABLESPACE`, `ALTER TABLESPACE`, `DROP TABLESPACE`,
   `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`, `TRUNCATE TABLE`, `CREATE
   INDEX`, `ALTER INDEX`, `DROP INDEX`, `CREATE USER`, `ALTER USER`, `DROP
   USER`, `CREATE ROLE`, `DROP ROLE`, `GRANT`, `REVOKE`, `CREATE
   REPLICATION`, `ALTER REPLICATION`, `DROP REPLICATION`, `ALTER SYSTEM`,
   `ALTER SESSION`, `AUDIT`, `NOAUDIT`, `DELAUDIT`, `COMMIT`, `ROLLBACK`,
   `SAVEPOINT`, and `SET TRANSACTION`.
3. Do not broaden 8.1-only idempotent syntax. The checked 7.1 and 7.3 Korean
   SQL Reference sources did not expose the `IF EXISTS` or `IF NOT EXISTS`
   matches found in the `Altibase 8.1 verified source` SQL Reference. Generate
   `IF EXISTS` or `IF NOT EXISTS` only for 8.1-verified scope or after exact
   installed-version evidence.
4. DDL is protected for rollback expectations. Before producing copy/paste
   DDL, confirm the target version, startup phase where applicable, connected
   user, privileges, object names, object dependencies, replication
   participation, backup point, maintenance window, and rollback plan.

Safe first checks:

- Use the exact SQL Reference source for the target version before producing a
  final BNF-like statement.
- Use `V$VERSION` for version inspection when available in the customer's
  environment.
- Use `V$TABLE` and `V$ALLCOLUMN` to verify version-sensitive dictionary or
  performance views before hard-coding check SQL.

Stop conditions:

- Stop if the request asks for an exhaustive list of SQL statements, clauses,
  hints, functions, or restrictions from this baseline alone.
- Stop if the target version is 7.1 or 7.3 and the requested syntax depends on
  `IF EXISTS`, `IF NOT EXISTS`, native `JSON`, Temporary LOB, replication SSL,
  or another `Altibase 8.1 verified source` feature.

## KAE-SQLREF-BLOCK-002: DDL, DCL, Administrative SQL, And Replication SQL

- Source IDs: `SRC-000072`, `SRC-000040`, `SRC-000134`, `SRC-000103`,
  `SRC-000194`, `SRC-000163`, with administration support from `SRC-000049`,
  `SRC-000018`, `SRC-000113`, `SRC-000082`, `SRC-000173`, `SRC-000143`,
  and replication support from `SRC-000070`, `SRC-000038`, `SRC-000132`,
  `SRC-000101`, `SRC-000192`, `SRC-000161`.
- Version scope: 7.1, 7.3, and `Altibase 8.1 verified source`.
- Source block refs: `SRC-000072/BLOCK-000884`, `SRC-000040/BLOCK-000883`,
  `SRC-000134/BLOCK-000886`, `SRC-000103/BLOCK-000885`,
  `SRC-000194/BLOCK-000888`, `SRC-000163/BLOCK-000887`,
  `SRC-000049/BLOCK-000002`, `SRC-000018/BLOCK-000001`,
  `SRC-000113/BLOCK-000004`, `SRC-000082/BLOCK-000003`,
  `SRC-000173/BLOCK-000006`, `SRC-000143/BLOCK-000005`,
  `SRC-000070/BLOCK-000845`, `SRC-000038/BLOCK-000844`,
  `SRC-000132/BLOCK-000847`, `SRC-000101/BLOCK-000846`,
  `SRC-000192/BLOCK-000849`, `SRC-000161/BLOCK-000848`.
- Alignment status: baseline generated for safe first-draft DDL/DCL routing.
  Exhaustive statement grammar remains not-ready.

Baseline:

1. Database and recovery SQL must preserve phase and mode boundaries. Source-
   backed tokens include `STARTUP PROCESS`, `STARTUP CONTROL`, `STARTUP META`,
   `STARTUP SERVICE`, `CREATE DATABASE`, `DROP DATABASE`, `ARCHIVELOG`,
   `NOARCHIVELOG`, `ALTER DATABASE BACKUP DATABASE TO`, `ALTER DATABASE
   BACKUP TABLESPACE`, `RESTORE`, `RECOVER`, `RESETLOGS`, and backup-file
   management clauses. Do not generate recovery SQL without backup files,
   archive logs, online logs, log anchor state, and target recovery point.
2. Tablespace and file SQL must preserve storage-medium tokens:
   `CREATE DISK TABLESPACE`, `CREATE MEMORY TABLESPACE`, `CREATE VOLATILE
   TABLESPACE`, `CREATE TEMPORARY TABLESPACE`, `DATAFILE`, `AUTOEXTEND ON`,
   `NEXT`, `MAXSIZE`, `UNLIMITED`, `REUSE`, `CHECKPOINT PATH`, `SPLIT EACH`,
   `ALTER TABLESPACE`, `DROP TABLESPACE`, `INCLUDING CONTENTS`, and
   `AND DATAFILES`.
3. Table, partition, index, and LOB DDL must preserve exact tokens such as
   `GLOBAL TEMPORARY`, `ON COMMIT`, `ALTER TABLE ADD PARTITION`, `CREATE
   TABLE AS SELECT`, `table_compression_clause`, `LOB(column_name)`, `STORE AS
   (TABLESPACE ...)`, `PARALLEL`, `NOLOGGING`, `FORCE`, `NOFORCE`, and
   `INDEX_BUILD_THREAD_COUNT`. Disk-table LOB data can be placed in a separate
   disk tablespace; memory-table LOB data cannot be stored separately from the
   table tablespace.
4. User and privilege SQL must preserve Altibase account and privilege tokens:
   `CREATE USER`, `ALTER USER`, `DROP USER`, `IDENTIFIED BY`, `DEFAULT
   TABLESPACE`, `TEMPORARY TABLESPACE`, `ACCESS`, `CREATE ROLE`, `DROP ROLE`,
   `GRANT`, and `REVOKE`. Do not generate `DROP USER ... CASCADE`, broad
   system privileges, or SYSDBA actions without dependency and approval
   evidence.
5. Replication SQL must preserve `CREATE REPLICATION`, `ALTER REPLICATION`,
   `DROP REPLICATION`, `SYNC`, `SYNC ONLY`, `START`, `QUICKSTART`, `STOP`,
   `RESET`, `ADD TABLE`, `DROP TABLE`, `FLUSH`, `replication_host_ip`, and
   `replication_host_port_no`. Only `SYS` can execute replication-related
   statements. Verify `V$REPSENDER`, `V$REPRECEIVER`, `V$REPGAP`, trace logs,
   and topology evidence before using protected replication SQL.

Safe first checks:

```sql
SELECT REP_NAME, REP_GAP FROM V$REPGAP;
SELECT COUNT(*) FROM V$SESSION WHERE ID <> SESSION_ID();
SELECT NAME, VALUE1 FROM V$PROPERTY
WHERE NAME IN ('ADMIN_MODE', 'REPLICATION_DDL_ENABLE',
               'REPLICATION_DDL_ENABLE_LEVEL',
               'REPLICATION_SQL_APPLY_ENABLE');
```

Stop conditions:

- Stop before destructive SQL such as `DROP DATABASE`, `DROP TABLESPACE ...
  INCLUDING CONTENTS`, `DROP TABLESPACE ... AND DATAFILES`, `DROP USER ...
  CASCADE`, `DROP TABLE`, and `TRUNCATE TABLE` without backup, dependency,
  replication, and maintenance-window evidence.
- Stop before replication DDL if `REP_GAP` is not `0`, if service cannot be
  stopped or migrated, or if the requested DDL is not in the source-backed
  allowed list for the selected replication mode and version.

## KAE-SQLREF-BLOCK-003: DML, Query, Set Operators, And Transaction SQL

- Source IDs: `SRC-000072`, `SRC-000040`, `SRC-000134`, `SRC-000103`,
  `SRC-000194`, `SRC-000163`.
- Version scope: 7.1, 7.3, and `Altibase 8.1 verified source`.
- Source block refs: `SRC-000072/BLOCK-000884`, `SRC-000040/BLOCK-000883`,
  `SRC-000134/BLOCK-000886`, `SRC-000103/BLOCK-000885`,
  `SRC-000194/BLOCK-000888`, `SRC-000163/BLOCK-000887`.
- Alignment status: baseline generated for DML and query safeguards. Full
  clause conversion remains not-ready.

Baseline:

1. DML generation must preserve `SELECT`, `INSERT`, `UPDATE`, `DELETE`,
   `MOVE`, `MERGE`, `ENQUEUE`, and `DEQUEUE` as separate Altibase statement
   families. Required privilege checks differ by target object and statement:
   for example, `DELETE`, `INSERT`, and `UPDATE` require the matching object
   privilege or system privilege such as `DELETE ANY TABLE`, `INSERT ANY
   TABLE`, or `UPDATE ANY TABLE`.
2. The DML `returning_clause` retrieves records affected by DML. Preserve the
   token shape `return ... into` in examples and keep the source restrictions:
   no aggregate functions in `expr` for `UPDATE`, `DELETE`, or `INSERT`; table
   only; no LOB type return; no aliases or subqueries in `expr`; no sequences
   in `expr`; host or PSM variable counts and types must match.
3. `multiple_delete` and `multiple_update` are Altibase-specific DML anchors.
   Preserve the exact tokens `multiple_delete`, `multiple_update`, `tbl_ref`,
   `one_table`, and `join_table`. For both multiple forms, do not combine with
   `limit_clause` or `returning_clause`, do not use dictionary tables, and do
   not use `full outer join`.
4. Query generation must preserve join and lateral-view tokens exactly where
   used: `LEFT OUTER JOIN`, `RIGHT OUTER JOIN`, `FULL OUTER JOIN`, `(+)`,
   `LATERAL`, `APPLY`, `CROSS APPLY`, and `OUTER APPLY`. The `APPLY` keyword
   defines a lateral view and has source restrictions; do not mix `APPLY` with
   unsupported `ON`-clause usage.
5. Transaction SQL is version-sensitive but source-backed tokens include
   `COMMIT`, `ROLLBACK`, `SAVEPOINT`, and `SET TRANSACTION`. Do not promise
   rollback of DDL or truncation outcomes without checking the exact statement
   consideration section and current autocommit or transaction context.

Safe first checks:

- Ask for target table owner, table DDL, constraints, triggers, indexes,
  partitioning, replication membership, autocommit state, expected row count,
  and rollback need before generating write DML.
- For `MERGE`, ask for the `ON` condition, source rows, target uniqueness
  expectation, and whether the update clause changes columns used by `ON`.

Stop conditions:

- Stop if the user asks to generate DML against dictionary tables or
  performance views without a source-backed writable object.
- Stop if the DML would affect all rows and the customer has not confirmed the
  intended predicate, backup point, transaction plan, and expected row count.

## KAE-SQLREF-BLOCK-004: Data Types, LOB, Temporary LOB, And JSON

- Source IDs: `SRC-000056`, `SRC-000025`, `SRC-000120`, `SRC-000089`,
  `SRC-000180`, `SRC-000150`, with SQL function support from `SRC-000194`
  and `SRC-000163`.
- Version scope: 7.1, 7.3, and `Altibase 8.1 verified source`, with native
  `JSON` and Temporary LOB scoped to `Altibase 8.1 verified source` unless
  customer evidence proves otherwise.
- Source block refs: `SRC-000056/BLOCK-000515`, `SRC-000025/BLOCK-000514`,
  `SRC-000120/BLOCK-000517`, `SRC-000089/BLOCK-000516`,
  `SRC-000180/BLOCK-000519`, `SRC-000150/BLOCK-000518`,
  `SRC-000194/BLOCK-000888`, `SRC-000163/BLOCK-000887`.
- Alignment status: baseline generated for type boundaries and 8.1-only JSON
  guardrails. Exhaustive type-conversion matrices remain not-ready.

Baseline:

1. Preserve data type tokens exactly: `CHAR`, `VARCHAR`, `NCHAR`, `NVARCHAR`,
   `BIGINT`, `DECIMAL`, `DOUBLE`, `FLOAT`, `INTEGER`, `NUMBER`, `NUMERIC`,
   `REAL`, `SMALLINT`, `DATE`, `BYTE`, `VARBYTE`, `NIBBLE`, `BIT`, `VARBIT`,
   `BLOB`, `CLOB`, and `JSON`.
2. Preserve numeric and range boundaries where this batch surfaces them:
   `BIGINT` ranges from `-2^63 + 1 (-9223372036854775807)` to
   `2^63 - 1 (9223372036854775807)`. `FLOAT` precision ranges from `1` to
   `38` and rounds at the 39th digit; omitted precision defaults to `38`.
   `NUMBER` and `NUMERIC` omit precision as `38` and omit scale as `0`.
3. LOB source tokens and limits: `BLOB`, `CLOB`, `IN ROW size`,
   `DISK_LOB_COLUMN_IN_ROW_SIZE`, `MEMORY_LOB_COLUMN_IN_ROW_SIZE`,
   `MEMORY_VARIABLE_COLUMN_IN_ROW_SIZE`, `LOB_OBJECT_BUFFER_SIZE`, and
   `LOB_CACHE_THRESHOLD`. One LOB column can store up to `4GB-1byte`. A LOB
   column cannot be an index key, cannot be used as a partition key, cannot be
   used in cursor columns according to the data type restriction, and cannot be
   used in volatile tablespaces or disk temporary tablespaces.
4. Temporary LOB is an `Altibase 8.1 verified source` feature in this baseline.
   Preserve `TEMPORARY_LOB_ENABLE`, `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`,
   `MEMORY_TEMPLOB_PIECE_SIZE`, `V$TEMPORARY_LOBS`, and
   `ALTER SESSION SET FREE TEMPORARY LOB`. Temporary LOB memory is separate
   from `MEM_MAX_DB_SIZE`, so memory sizing cannot be inferred from memory
   database size alone.
5. Native `JSON` is an `Altibase 8.1 verified source` data type in this
   baseline. Preserve `2GB (2,147,483,648 bytes)`, `RFC 8259`,
   `ISO/IEC 19075-6(2021)`, maximum JSON depth `256`, `IN ROW size`,
   `TEMPORARY_LOB_ENABLE=1`, and the restriction that `JSON` cannot be used in
   `SELECT FOR UPDATE`.
6. JSON SQL must preserve `JSON_ARRAY`, `JSON_OBJECT`, `JSON_EXISTS`,
   `JSON_QUERY`, `JSON_VALUE`, `JSON_VALID`, `IS JSON`, `IS NOT JSON`,
   `NULL ON NULL`, `ABSENT ON NULL`, `RETURNING JSON`, `RETURNING CLOB`,
   `NULL ON ERROR`, `ERROR ON ERROR`, `DEFAULT expr ON ERROR`,
   `NULL ON EMPTY`, and `ERROR ON EMPTY`.

Safe first checks:

- For 7.1 or 7.3, do not generate native `JSON`, `TEMPORARY_LOB_ENABLE`,
  `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`, `MEMORY_TEMPLOB_PIECE_SIZE`, or
  `V$TEMPORARY_LOBS` unless the customer supplies exact installed-version
  proof.
- For LOB and JSON SQL, ask for table type, tablespace type, in-row size,
  expected document or LOB size, client API, autocommit mode, and memory limit.

Stop conditions:

- Stop if JSON or Temporary LOB output is requested for 7.1 or 7.3 without
  target-version evidence.
- Stop if a generated artifact would put LOB columns in a prohibited context
  such as an index key, partition key, volatile tablespace, or disk temporary
  tablespace.

## KAE-SQLREF-BLOCK-005: Functions, Expressions, Conditions, And Oracle Differences

- Source IDs: `SRC-000072`, `SRC-000040`, `SRC-000134`, `SRC-000103`,
  `SRC-000194`, `SRC-000163`, with data-type support from `SRC-000056`,
  `SRC-000120`, and `SRC-000180`.
- Version scope: 7.1, 7.3, and `Altibase 8.1 verified source`, with JSON
  functions scoped to `Altibase 8.1 verified source`.
- Source block refs: `SRC-000072/BLOCK-000884`, `SRC-000040/BLOCK-000883`,
  `SRC-000134/BLOCK-000886`, `SRC-000103/BLOCK-000885`,
  `SRC-000194/BLOCK-000888`, `SRC-000163/BLOCK-000887`,
  `SRC-000056/BLOCK-000515`, `SRC-000120/BLOCK-000517`,
  `SRC-000180/BLOCK-000519`.
- Alignment status: baseline generated for retrieval and safe first drafts.
  Exhaustive function-by-function examples remain not-ready.

Baseline:

1. Preserve function-family tokens before synthesizing SQL: aggregate
   functions, window functions, numeric functions, character functions,
   datetime functions, conversion functions, encryption functions, JSON
   functions, and other functions.
2. High-risk exact function forms in this batch include
   `GROUP_CONCAT (expr1 [, arg1])`, `LISTAGG`, `DECODE (expr,
   comparison_expr1, ret_expr1[, comparison_expr2, ret_expr2,..][, default])`,
   `NVL2 (expr1, expr2, expr3)`, `REGEXP_REPLACE (expr, pattern_expr [,
   replace_string [, start [,occurrence]]])`, `REGEXP_SUBSTR (expr,
   pattern_expr [, start [, occurrence]])`, `REGEXP_LIKE`, `CURRVAL`,
   `NEXTVAL`, and `ROWNUM`.
3. Preserve expression and condition tokens such as arithmetic operators,
   concatenation, `CAST`, logical and comparison conditions, `LIKE`,
   `BETWEEN`, `IN`, `EXISTS`, `IS NULL`, `IS JSON`, regular expression
   conditions, set operators `UNION`, `UNION ALL`, `INTERSECT`, and `MINUS`,
   and pseudo column `ROWNUM`.
4. Oracle-overlap syntax must be treated as Altibase-source-backed only when
   the SQL Reference or migration sources show it. For outer joins, preserve
   both ANSI and Oracle-style tokens where source-backed: `LEFT OUTER JOIN`,
   `RIGHT OUTER JOIN`, `FULL OUTER JOIN`, and `(+)`. Do not assume wider
   Oracle behavior for PL/SQL packages, hints, data types, SQL/JSON, or object
   semantics.
5. Regular-expression answers must preserve `REGEXP_MODE` and source mode
   boundaries. The SQL Reference states `REGEXP_LIKE` is similar to `LIKE` but
   performs regular-expression matching, and references POSIX Basic Regular
   Expression support; PCRE2-related error handling is represented separately
   in the Error Message Reference appendix and exact `MT` entries.

Safe first checks:

- Ask for the exact SQL text, expected return type, input data types, target
  version, collation or NLS setting, `REGEXP_MODE`, and output precision before
  generating function-heavy SQL.
- For Oracle conversion, ask for the original Oracle SQL and the intended
  Altibase version, then map only source-backed syntax.

Stop conditions:

- Stop if a requested function or Oracle behavior is not named in the selected
  Altibase SQL or migration sources.
- Stop if JSON functions are requested outside `Altibase 8.1 verified source`
  without exact installed-version proof.

## KAE-SQLREF-BLOCK-006: Properties, Defaults, Ranges, Dynamic Behavior, And Cautions

- Source IDs: `SRC-000056`, `SRC-000025`, `SRC-000120`, `SRC-000089`,
  `SRC-000180`, `SRC-000150`, with change-SQL support from `SRC-000072`,
  `SRC-000040`, `SRC-000134`, `SRC-000103`, `SRC-000194`, `SRC-000163`.
- Version scope: 7.1, 7.3, and `Altibase 8.1 verified source`.
- Source block refs: `SRC-000056/BLOCK-000515`, `SRC-000025/BLOCK-000514`,
  `SRC-000120/BLOCK-000517`, `SRC-000089/BLOCK-000516`,
  `SRC-000180/BLOCK-000519`, `SRC-000150/BLOCK-000518`,
  `SRC-000072/BLOCK-000884`, `SRC-000040/BLOCK-000883`,
  `SRC-000134/BLOCK-000886`, `SRC-000103/BLOCK-000885`,
  `SRC-000194/BLOCK-000888`, `SRC-000163/BLOCK-000887`.
- Alignment status: baseline generated for property response structure and
  high-risk token preservation. Exhaustive per-property default/range/change
  blocks remain not-ready.

Baseline:

1. Every property answer must preserve these source fields when present:
   property name, default value, attribute, value range, unit, dynamic-change
   level, related views, cautions, and version scope. Do not infer default,
   range, or online-change support from the property name.
2. Preserve the General Reference dynamic-change vocabulary:
   `SESSION`, `SYSTEM`, `BOTH`, and `NONE`. `SESSION` maps to `ALTER SESSION`;
   `SYSTEM` maps to `ALTER SYSTEM`; `BOTH` can use either path; `NONE` is not
   dynamically changeable. Static file and environment-variable changes require
   restart or the source-specific activation path.
3. Preserve key property tokens for this SQL/reference batch:
   `DB_NAME`, `DEFAULT_DISK_DB_DIR`, `MEM_DB_DIR`, `LOGANCHOR_DIR`, `LOG_DIR`,
   `LOG_FILE_SIZE`, `MEM_MAX_DB_SIZE`, `VOLATILE_MAX_DB_SIZE`,
   `DISK_LOB_COLUMN_IN_ROW_SIZE`, `MEMORY_LOB_COLUMN_IN_ROW_SIZE`,
   `LOB_OBJECT_BUFFER_SIZE`, `LOB_CACHE_THRESHOLD`, `ARCHIVE_DIR`,
   `INCREMENTAL_BACKUP_CHUNK_SIZE`, `TRANSACTION_SEGMENT_COUNT`,
   `AUTO_COMMIT`, `ISOLATION_LEVEL`, `REPLICATION_DDL_ENABLE`,
   `REPLICATION_DDL_ENABLE_LEVEL`, `REPLICATION_SQL_APPLY_ENABLE`,
   `REPLICATION_SSL_PORT_NO`, `SSL_ENABLE`, `SSL_PORT_NO`,
   `SSL_CIPHER_LIST`, `SSL_CIPHER_SUITES`, `SSL_LOAD_CONFIG`,
   `SNMP_ENABLE`, `ADMIN_MODE`, `REGEXP_MODE`, `TEMPORARY_LOB_ENABLE`,
   `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`, and `MEMORY_TEMPLOB_PIECE_SIZE`.
4. Preserve source-drift cautions already identified in support evidence:
   `REPLICATION_UPDATE_REPLACE` and
   `REPLICATION_META_ITEM_COUNT_DIFF_ENABLE` require installed-version checks
   for 8.1 because the selected 8.1 General Reference detailed property blocks
   are absent or incomplete while related replication evidence exists.
5. Use `V$PROPERTY` for runtime inspection when available, but do not treat the
   current runtime value as proof of a default, range, or dynamic-change level.

Safe first checks:

```sql
SELECT NAME, VALUE1, VALUE2
FROM V$PROPERTY
WHERE NAME IN ('ADMIN_MODE',
               'TEMPORARY_LOB_ENABLE',
               'MEMORY_TEMPLOB_MAX_ALLOC_SIZE',
               'MEMORY_TEMPLOB_PIECE_SIZE',
               'REPLICATION_DDL_ENABLE',
               'REPLICATION_DDL_ENABLE_LEVEL',
               'REPLICATION_SQL_APPLY_ENABLE',
               'SSL_ENABLE',
               'SNMP_ENABLE')
ORDER BY NAME;
```

Stop conditions:

- Stop if a property is read-only, startup-only, `NONE`, or phase-restricted
  and the requested change path does not match the source.
- Stop if the requested value is outside the source-defined range, if the unit
  is unknown, or if the property's detailed source block is absent for the
  target version.

## KAE-SQLREF-BLOCK-007: Dictionary, Metadata, Performance Views, And Key Columns

- Source IDs: `SRC-000057`, `SRC-000026`, `SRC-000121`, `SRC-000090`,
  `SRC-000181`, `SRC-000151`, with check-SQL support from `SRC-000072`,
  `SRC-000134`, and `SRC-000194`.
- Version scope: 7.1, 7.3, and `Altibase 8.1 verified source`.
- Source block refs: `SRC-000057/BLOCK-000521`, `SRC-000026/BLOCK-000520`,
  `SRC-000121/BLOCK-000523`, `SRC-000090/BLOCK-000522`,
  `SRC-000181/BLOCK-000525`, `SRC-000151/BLOCK-000524`,
  `SRC-000072/BLOCK-000884`, `SRC-000134/BLOCK-000886`,
  `SRC-000194/BLOCK-000888`.
- Alignment status: baseline generated for name groups and portable checks.
  Exhaustive per-view and per-column blocks remain not-ready.

Baseline:

1. Treat General Reference 2 as the source of data dictionary and performance
   view names, descriptions, and columns. Do not generate DML against
   performance views; use `SELECT`.
2. Preserve meta-table group tokens: `SYS_TABLES_`, `SYS_COLUMNS_`,
   `SYS_INDICES_`, `SYS_INDEX_COLUMNS_`, `SYS_TABLE_PARTITIONS_`,
   `SYS_CONSTRAINTS_`, `SYS_GRANT_SYSTEM_`, `SYS_GRANT_OBJECT_`,
   `SYS_USERS_`, `DBA_USERS_`, `SYS_USER_ROLES_`, `SYS_DIRECTORIES_`,
   `SYS_SYNONYMS_`, `SYS_MATERIALIZED_VIEWS_`, `SYS_TRIGGERS_`,
   `SYS_JOBS_`, `SYS_REPLICATIONS_`, `SYS_REPL_HOSTS_`, `SYS_REPL_ITEMS_`,
   `SYS_REPL_RECOVERY_INFOS_`, `SYS_DATABASE_LINKS_`, and
   `SYS_XA_HEURISTIC_TRANS_`.
3. Preserve performance-view group tokens: `V$TABLE`, `V$ALLCOLUMN`,
   `V$CATALOG`, `V$DATATYPE`, `V$PROPERTY`, `V$VERSION`, `V$SESSION`,
   `V$STATEMENT`, `V$SQLTEXT`, `V$PLANTEXT`, `V$SESSION_WAIT`,
   `V$LOCK_WAIT`, `V$LOCK_STATEMENT`, `V$LOCK_TABLE_STATS`, `V$TRANSACTION`,
   `V$DATABASE`, `V$TABLESPACES`, `V$DATAFILES`, `V$ARCHIVE`,
   `V$BACKUP_INFO`, `V$LOG`, `V$LFG`, `V$DISK_BTREE_HEADER`,
   `V$SQL_PLAN_CACHE`, `V$DBMS_STATS`, `V$REPGAP`, `V$REPSENDER`,
   `V$REPRECEIVER`, `V$TEMPORARY_LOBS`, and `V$QUEUE_DELETE_OFF`.
4. Key-column generation remains source-check required. Use exact view sections
   before asserting column availability. Representative check tokens include
   `NAME`, `SLOTSIZE`, `COLUMNCOUNT` in `V$TABLE` and `TABLENAME`,
   `COLNAME` in `V$ALLCOLUMN`; do not infer other column names by analogy.
5. Preserve version-drift cautions: `SYS_REPL_TABLE_OID_IN_USE_` is listed in
   7.1 and 7.3 Korean sources but not in the checked 8.1 Korean table list;
   `V$TEMPORARY_LOBS` and `V$MEM_STABLE` are `Altibase 8.1 verified source`
   views; `V$QUEUE_DELETE_OFF` is present in Korean General Reference 2 while
   English extraction-aid lists can omit it.

Safe first checks:

```sql
SELECT NAME, SLOTSIZE, COLUMNCOUNT
FROM V$TABLE
WHERE NAME IN ('V$PROPERTY', 'V$TEMPORARY_LOBS', 'V$QUEUE_DELETE_OFF',
               'V$LOCK_TABLE_STATS', 'V$REPGAP')
ORDER BY NAME;

SELECT TABLENAME, COLNAME
FROM V$ALLCOLUMN
WHERE TABLENAME IN ('V$PROPERTY', 'V$TEMPORARY_LOBS', 'V$QUEUE_DELETE_OFF',
                    'V$REPGAP')
ORDER BY TABLENAME, COLNAME;
```

Stop conditions:

- Stop before giving a final column-level query if the customer version does
  not expose the view or column in `V$TABLE` and `V$ALLCOLUMN`.
- Stop if a view is known to be 8.1-only or source-drifted and the target
  environment is not verified.

## KAE-SQLREF-BLOCK-008: Error Codes And Troubleshooting Response Baseline

- Source IDs: `SRC-000054`, `SRC-000023`, `SRC-000118`, `SRC-000087`,
  `SRC-000178`, `SRC-000148`, with diagnostic support from `SRC-000057`,
  `SRC-000121`, `SRC-000181`, `SRC-000070`, `SRC-000132`, `SRC-000192`,
  `SRC-000051`, `SRC-000115`, and `SRC-000175`.
- Version scope: 7.1, 7.3, and `Altibase 8.1 verified source`.
- Source block refs: `SRC-000054/BLOCK-000509`, `SRC-000023/BLOCK-000508`,
  `SRC-000118/BLOCK-000511`, `SRC-000087/BLOCK-000510`,
  `SRC-000178/BLOCK-000513`, `SRC-000148/BLOCK-000512`,
  `SRC-000057/BLOCK-000521`, `SRC-000121/BLOCK-000523`,
  `SRC-000181/BLOCK-000525`, `SRC-000070/BLOCK-000845`,
  `SRC-000132/BLOCK-000847`, `SRC-000192/BLOCK-000849`,
  `SRC-000051/BLOCK-000851`, `SRC-000115/BLOCK-000853`,
  `SRC-000175/BLOCK-000855`.
- Alignment status: baseline generated for response structure and high-risk
  exact tokens. Exhaustive exact-code conversion remains not-ready.

Baseline:

1. Preserve error-family tokens and do not infer from prefix alone:
   `ID Error Code`, `SM Error Code`, `MT Error Code`, `RP Error Code`,
   `QP Error Code`, `SD Error Code`, `ST Error Code`, `MM Error Code`,
   `ODBC Error Code`, `APRE Error Code`, `Utilities Error Code`,
   `CM Error Code`, `Database Link Error Code`, `Log Analyzer Error Code`,
   and `Regular Expression Error Code`.
2. Preserve source severity headings as source headings, not as complete
   operational severity: `FATAL`, `ABORT`, `IGNORE`, and `RETRY`.
3. Exact-code answers must preserve runtime form when supplied, reference
   `0x... (decimal)` form when source-backed, reference symbol, message,
   module, source severity heading, version scope, source-backed cause/action,
   check SQL or command, required customer evidence, and stop conditions.
4. High-risk literal tokens for this batch include `0x0001F (31)
   idERR_FATAL_idc_SVC_INET_BIND_ERROR`, `0x2106D (135277)
   mtERR_ABORT_JSON_WITHOUT_TEMPLOB`, `0x31010 (200720)
   qpERR_ABORT_QCM_NOT_EXIST_USER`, `0x31363 (201571)
   qpERR_ABORT_QDB_TEMPORARY_TABLE_DDL_DISABLE`, `0x314BC (201916)
   qpERR_ABORT_JSON_INVALID_TYPE`, `0x6100D (397325)
   rpERR_ABORT_RP_SENDER_HANDSHAKE`, `0x61010 (397328)
   rpERR_ABORT_RP_SENDER_START`, `0x6102D (397357)
   rpERR_ABORT_LISTEN`, `0x710A0 (463008)
   cmERR_ABORT_INVALID_CERTIFICATE`, `0x710A3 (463011)
   cmERR_ABORT_SSL_HANDSHAKE`, and `ERR-2106C`.
5. Source-backed first-check examples must remain evidence-limited:
   `mtERR_ABORT_JSON_WITHOUT_TEMPLOB` points to checking
   `TEMPORARY_LOB_ENABLE`; `qpERR_ABORT_QCM_NOT_EXIST_USER` points to
   verifying the requested user; replication sender/receiver errors point to
   topology, `V$REPSENDER`, `V$REPRECEIVER`, `V$REPGAP`, ports, and trace logs;
   SSL certificate and handshake errors point to certificate paths, CA files,
   OpenSSL version, SSL properties, and trace logs. Do not turn these first
   checks into a definitive root cause without customer evidence.
6. Preserve source drift: `SD Error Code` is listed in the 7.1 Korean Error
   Message Reference, but not in the checked 7.3 or 8.1 Korean Error Message
   Reference. Do not treat `sdERR_*` as 7.3 or 8.1 verified without exact
   installed-version evidence.

Safe first checks:

- Ask for Altibase version, patch level, exact runtime error line, complete
  message text, SQL or command, object definition, trace log excerpt, client
  or tool version, OS error text, and topology before recommending restart,
  recovery, object rebuild, replication rebuild, certificate replacement, or
  property changes.
- For an uncovered exact code, preserve the supplied code and message and say
  which fields are unknown rather than inferring severity, module, cause,
  action, or `SQLSTATE`.

Stop conditions:

- Stop before destructive recovery, object drop/rebuild, replication reset,
  certificate replacement, or server restart unless the exact source entry,
  customer evidence, and rollback plan support the action.
- Stop if only an error prefix such as `qpERR_`, `rpERR_`, or `cmERR_` is
  supplied without the exact code and message.

## KAE-SQLREF-BLOCK-009: Check SQL And Customer Evidence Contract

- Source IDs: `SRC-000072`, `SRC-000134`, `SRC-000194`, `SRC-000057`,
  `SRC-000121`, `SRC-000181`, `SRC-000056`, `SRC-000120`, `SRC-000180`,
  `SRC-000070`, `SRC-000132`, `SRC-000192`.
- Version scope: 7.1, 7.3, and `Altibase 8.1 verified source`.
- Source block refs: `SRC-000072/BLOCK-000884`, `SRC-000134/BLOCK-000886`,
  `SRC-000194/BLOCK-000888`, `SRC-000057/BLOCK-000521`,
  `SRC-000121/BLOCK-000523`, `SRC-000181/BLOCK-000525`,
  `SRC-000056/BLOCK-000515`, `SRC-000120/BLOCK-000517`,
  `SRC-000180/BLOCK-000519`, `SRC-000070/BLOCK-000845`,
  `SRC-000132/BLOCK-000847`, `SRC-000192/BLOCK-000849`.
- Alignment status: baseline generated for portable validation patterns.

Baseline:

Use check SQL as a source-backed next step, not as a substitute for exact
source verification:

```sql
SELECT NAME, VALUE1, VALUE2
FROM V$PROPERTY
WHERE NAME IN ('DB_NAME', 'ADMIN_MODE', 'ARCHIVE_DIR',
               'TEMPORARY_LOB_ENABLE', 'REPLICATION_DDL_ENABLE',
               'REPLICATION_DDL_ENABLE_LEVEL', 'SSL_ENABLE');

SELECT NAME, SLOTSIZE, COLUMNCOUNT
FROM V$TABLE
WHERE NAME IN ('V$VERSION', 'V$PROPERTY', 'V$ALLCOLUMN',
               'V$TEMPORARY_LOBS', 'V$REPGAP');

SELECT TABLENAME, COLNAME
FROM V$ALLCOLUMN
WHERE TABLENAME IN ('V$PROPERTY', 'V$TEMPORARY_LOBS', 'V$REPGAP')
ORDER BY TABLENAME, COLNAME;

SELECT REP_NAME, REP_GAP FROM V$REPGAP;
```

Required customer evidence before final generated artifacts:

1. Exact Altibase version and patch level.
2. Target component: server, client, iSQL, iLoader, CLI/ODBC, JDBC, replication,
   DB Link, Log Analyzer, or utility.
3. Full SQL, DDL, DCL, command, property name, error line, or object
   definition.
4. Runtime state: startup phase, connected user, privileges, autocommit,
   session state, tablespace state, replication state, and relevant
   `V$`/`SYSTEM_` rows.
5. Backup, rollback, maintenance-window, and data-loss acceptance for
   destructive or recovery work.

Stop conditions:

- Stop if customer evidence is missing for version-specific syntax,
  environment-specific configuration, runtime state, object definitions, live
  logs, patch-specific behavior, unsupported behavior, or destructive action.
- Provide the safest source-backed next check instead of inventing a
  definitive answer.

## KAE-SQLREF-BLOCK-010: Scoped Not-Ready Gaps

- Source IDs: `SRC-000049`, `SRC-000018`, `SRC-000054`, `SRC-000023`,
  `SRC-000056`, `SRC-000025`, `SRC-000057`, `SRC-000026`, `SRC-000070`,
  `SRC-000038`, `SRC-000072`, `SRC-000040`, `SRC-000113`, `SRC-000082`,
  `SRC-000118`, `SRC-000087`, `SRC-000120`, `SRC-000089`, `SRC-000121`,
  `SRC-000090`, `SRC-000132`, `SRC-000101`, `SRC-000134`, `SRC-000103`,
  `SRC-000173`, `SRC-000143`, `SRC-000178`, `SRC-000148`, `SRC-000180`,
  `SRC-000150`, `SRC-000181`, `SRC-000151`, `SRC-000192`, `SRC-000161`,
  `SRC-000194`, `SRC-000163`.
- Version scope: 7.1, 7.3, and `Altibase 8.1 verified source`.
- Source block refs: see the source coverage table and each block above.
- Alignment status: not-ready gaps recorded in `CONF-000005`.

Remaining scoped gaps:

1. Full SQL Reference grammar conversion is not complete for every DDL, DML,
   DCL, function, operator, condition, hint, set-operator, and clause diagram.
2. Full data type conversion matrices, every numeric/date/binary format, and
   every implicit/explicit conversion rule remain delegated to the exact
   General Reference 1 source.
3. Full per-property normalization for all 484 inventoried property names,
   including defaults, ranges, attributes, dynamic/static behavior, units,
   related views, and cautions, is not complete in this batch.
4. Full data dictionary and performance-view column extraction is not complete.
   Use `V$TABLE` and `V$ALLCOLUMN` before generating column-specific SQL.
5. Full exact-code error conversion is not complete for all Error Message
   Reference entries. Use exact source entries before giving cause/action for
   a code outside the consolidated blocks.
6. Known source-drift or recheck items remain: `IF EXISTS` and `IF NOT EXISTS`
   are treated as 8.1 verified only in this baseline; native `JSON` and
   Temporary LOB are treated as 8.1 verified only; `SYS_REPL_TABLE_OID_IN_USE_`
   needs 8.1 installed metadata verification; `REPLICATION_UPDATE_REPLACE` and
   `REPLICATION_META_ITEM_COUNT_DIFF_ENABLE` need 8.1 property recheck; and
   `SD Error Code` is not treated as 7.3 or 8.1 Korean-verified.

Downstream rule:

Use this file for guarded first drafts and routing. When a request requires
exact syntax, full enumerations, complete property values, view columns, error
cause/action, current runtime state, patch behavior, live logs, object
definitions, or replication topology, ask for the missing input and recheck the
exact source IDs above before generating a definitive artifact.
