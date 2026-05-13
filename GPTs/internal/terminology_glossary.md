# Altibase Terminology Glossary for Multilingual Answers

Job: `JOB-021`
Status: work output
Purpose: define Altibase terms and token patterns that must stay literal when the GPT
answers in Korean, English, Japanese, Chinese, Vietnamese, Turkish, Persian, Hindi,
German, French, or any other user language.

This is an internal work document. Customer-facing attachment files should copy the
language policy, not the internal source paths.

## Source Basis

- Language policy: `GPTs/GPT_Instructions_Draft.md`, `GPTs/attachments/README.md`
- Source inventory: `GPTs/reports/source_inventory.md`
- English canonical decision: `GPTs/reports/eng_kor_parity.md`
- Core source manuals sampled:
  - `Manuals/Altibase_7.1/eng`
  - `Manuals/Altibase_7.3/eng`
  - `Manuals/Altibase_trunk/eng`
  - `Manuals/Tools/Altibase_trunk/eng`
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`
- Korean fallback terms checked for 8.1 gaps:
  - JSON functions and `IS JSON`
  - Temporary LOB, `TEMPORARY_LOB_ENABLE`, `V$TEMPORARY_LOBS`
  - replication SSL, `USING SSL`, `REPLICATION_SSL_PORT_NO`

## Global Rule

Answer explanations in the user's language, but never translate, transliterate,
inflect, pluralize, or localize literal technical tokens. Preserve spelling, casing,
underscores, dollar signs, punctuation, and version numbers exactly.

Use local-language explanations around the literal token:

- Good: "Set `REPLICATION_SSL_PORT_NO` before creating replication with `USING SSL`."
- Bad: translating `REPLICATION_SSL_PORT_NO`, changing it to lower case, or adding a
  local-language suffix directly to the token.

When in doubt, keep the technical token in backticks and explain it in the user's
language.

## Do Not Translate Token Patterns

Always preserve any token that matches one of these patterns when it appears in source
manuals, code, SQL, configuration, commands, paths, logs, or user-provided input.

| Pattern | Examples | Handling |
| --- | --- | --- |
| SQL identifiers | `T_CUSTOMER`, `customer_order`, `SYS`, `SYSTEM_`, `MEM_TBS`, `REP1` | Preserve exactly as supplied unless the user asks to rename it. |
| SQL keywords and syntax fragments | `CREATE TABLE`, `ALTER SYSTEM`, `USING SSL`, `PARTITION BY RANGE` | Preserve literal when shown as SQL or syntax. |
| Data dictionary and performance views | `V$SESSION`, `V$PROPERTY`, `SYS_TABLES_`, `SYSTEM_.SYS_USERS_` | Preserve prefix, `$`, `_`, schema, and case. |
| Properties and configuration keys | `LOG_FILE_SIZE`, `QUERY_TIMEOUT`, `REPLICATION_SSL_PORT_NO` | Preserve exactly; do not translate component words. |
| Environment variables | `ALTIBASE_HOME`, `ALTIBASE_PORT_NO`, `PATH`, `LD_LIBRARY_PATH` | Preserve exactly. |
| Commands, tools, and options | `isql`, `iloader`, `server`, `aexport -s`, `aku -p start` | Preserve command spelling and option names. |
| File names and paths | `altibase.properties`, `$ALTIBASE_HOME/conf`, `/altibase_home/trc` | Preserve exact path text; do not localize separators. |
| Function/API names | `JSON_VALUE`, `SQLConnect`, `ALA_GetXLog`, `PreparedStatement` | Preserve exact spelling and parentheses style if present. |
| Error identifiers | `0x2106D`, `mtERR_ABORT_JSON_WITHOUT_TEMPLOB`, `RULE-11001`, `SQLSTATE` | Preserve exact code and identifier. |
| Product, tool, and connector names | `Altibase`, `iSQL`, `iLoader`, `Migration Center`, `DBeaver` | Preserve brand/tool spelling. |
| Version labels | `Altibase 7.1`, `Altibase 7.3`, `Altibase 8.1`, `Altibase 8.1 verified source` | Preserve version numbers and canonical label. |

## Customer-Safe Source Labels

Use these labels in customer-facing attachment text and GPT answers.

| Canonical label | Usage |
| --- | --- |
| `Altibase 7.1` | Customer version label for 7.1 manuals and release notes. |
| `Altibase 7.3` | Customer version label for 7.3 manuals and release notes. |
| `Altibase 8.1` | Customer version label for 8.1 answers. |
| `Altibase 8.1 verified source` | Customer-safe label for 8.1 source material. |

Do not expose internal source labels, branch names, local workstation paths, or repository
directory names in customer-facing attachments.

## Product, Tool, and Feature Names

Preserve these names as literal terms. It is acceptable to explain their meaning in the
user's language after the preserved term.

### Product and Version Terms

- `Altibase`
- `Altibase 7.1`
- `Altibase 7.3`
- `Altibase 8.1`
- `Altibase 8.1 verified source`
- `Altibase HDB`
- `Altibase server`
- `Altibase client`
- `SYS`
- `SYSTEM_`

### Server Utilities and Operational Tools

- `altibase`
- `server`
- `isql`
- `iSQL`
- `iloader`
- `iLoader`
- `aexport`
- `altiComp`
- `aku`
- `aku.conf`
- `altiAudit`
- `altiMon`
- `altimon.sh`
- `altierr`
- `altipasswd`
- `checkServer`
- `dumpbi`
- `dumpct`
- `dumpdb`
- `dumpddf`
- `dumpla`
- `dumplf`
- `dumptrc`
- `dataCompJ`
- `altiShapeLoader`
- `Migration Center`
- `Replication Manager`
- `Altibase Heartbeat`
- `aheartbeat`

### Connectors, APIs, and External Integrations

- `Adapter for JDBC`
- `Adapter for Oracle`
- `Altibase Hadoop Connector`
- `DB Link`
- `DBeaver`
- `GoldenGate`
- `NiFi`
- `Tableau`
- `Kubernetes`
- `StatefulSet`
- `Pod`
- `Service`
- `PersistentVolume`
- `PersistentVolumeClaim`
- `Spring Data JPA`
- `Spring Boot`
- `Hibernate`
- `JPA`
- `JDBC`
- `ODBC`
- `CLI`
- `C Interface`
- `APRE`
- `Precompiler`
- `SSL`
- `TLS`
- `OpenSSL`
- `JDK`
- `JRE`

### Replication and CDC Terms

- `Replication`
- `CREATE REPLICATION`
- `ALTER REPLICATION`
- `DROP REPLICATION`
- `SYNC`
- `SYNC ONLY`
- `LAZY`
- `EAGER`
- `XLog`
- `XLog Sender`
- `XLog Collector`
- `XLog Queue`
- `XLog Pool`
- `Log Analyzer`
- `Log Analysis API`
- `ALA_CreateXLogCollector`
- `ALA_Handshake`
- `ALA_ReceiveXLog`
- `ALA_GetXLog`
- `ALA_FreeXLog`
- `ALA_DestroyXLogCollector`
- `ALA_GetXLogCollectorStatus`
- `ALA_GetXLogHeader`
- `ALA_GetXLogPrimaryKey`
- `ALA_GetXLogColumn`
- `ALA_GetXLogSavepoint`
- `ALA_GetXLogLOB`

## SQL Statements and Syntax Tokens

Preserve SQL statement names and clauses exactly when they appear as syntax, examples,
or requested generated SQL.

### DDL and Database Object Statements

- `ALTER DATABASE`
- `ALTER DATABASE LINKER`
- `ALTER INDEX`
- `ALTER JOB`
- `ALTER QUEUE`
- `ALTER REPLICATION`
- `ALTER SEQUENCE`
- `ALTER TABLE`
- `ALTER TABLESPACE`
- `ALTER TRIGGER`
- `ALTER USER`
- `ALTER VIEW`
- `ALTER MATERIALIZED VIEW`
- `COMMENT`
- `CONJOIN TABLE`
- `CREATE DATABASE`
- `CREATE DATABASE LINK`
- `CREATE DIRECTORY`
- `CREATE INDEX`
- `CREATE JOB`
- `CREATE QUEUE`
- `CREATE REPLICATION`
- `CREATE ROLE`
- `CREATE SEQUENCE`
- `CREATE SYNONYM`
- `CREATE TABLE`
- `CREATE DISK TABLESPACE`
- `CREATE MEMORY TABLESPACE`
- `CREATE VOLATILE TABLESPACE`
- `CREATE TEMPORARY TABLESPACE`
- `CREATE TRIGGER`
- `CREATE USER`
- `CREATE VIEW`
- `CREATE MATERIALIZED VIEW`
- `DISJOIN TABLE`
- `DROP DATABASE`
- `DROP DATABASE LINK`
- `DROP DIRECTORY`
- `DROP INDEX`
- `DROP JOB`
- `DROP QUEUE`
- `DROP REPLICATION`
- `DROP ROLE`
- `DROP SEQUENCE`
- `DROP SYNONYM`
- `DROP TABLE`
- `DROP TABLESPACE`
- `DROP TRIGGER`
- `DROP USER`
- `DROP VIEW`
- `DROP MATERIALIZED VIEW`
- `FLASHBACK TABLE`
- `PURGE TABLE`
- `RENAME TABLE`
- `TRUNCATE TABLE`

### DML, Query, Transaction, and Security Statements

- `SELECT`
- `INSERT`
- `UPDATE`
- `DELETE`
- `MERGE`
- `MOVE`
- `LOCK TABLE`
- `ENQUEUE`
- `DEQUEUE`
- `GRANT`
- `REVOKE`
- `ALTER SESSION`
- `ALTER SYSTEM`
- `AUDIT`
- `DELAUDIT`
- `NOAUDIT`
- `COMMIT`
- `ROLLBACK`
- `SAVEPOINT`
- `SET TRANSACTION`
- `UNION`
- `UNION ALL`
- `INTERSECT`
- `MINUS`

### Storage, Tablespace, and Partitioning Clauses

- `MEMORY`
- `DISK`
- `VOLATILE`
- `TEMPORARY`
- `TABLESPACE`
- `DATAFILE`
- `TEMPFILE`
- `ADD DATAFILE`
- `ADD TEMPFILE`
- `RENAME DATAFILE`
- `DROP DATAFILE`
- `CHECKPOINT PATH`
- `AUTOEXTEND`
- `NEXT`
- `MAXSIZE`
- `SIZE`
- `MAXROWS`
- `LOB`
- `IN ROW`
- `OUT ROW`
- `PARTITION`
- `PARTITION BY RANGE`
- `PARTITION BY LIST`
- `PARTITION BY HASH`
- `VALUES LESS THAN`
- `VALUES DEFAULT`
- `LOCAL`
- `LOCALUNIQUE`
- `DIRECTKEY`
- `UNCOMPRESSED LOGGING`
- `USING INDEX TABLESPACE`
- `USING SSL`

## Data Types

Preserve data type tokens in SQL, schema descriptions, mappings, and compatibility
tables. The concept can be explained in the user's language, but the type name stays
literal.

- `CHAR`
- `VARCHAR`
- `NCHAR`
- `NVARCHAR`
- `BIGINT`
- `DECIMAL`
- `DOUBLE`
- `FLOAT`
- `INTEGER`
- `NUMBER`
- `NUMERIC`
- `REAL`
- `SMALLINT`
- `DATE`
- `BYTE`
- `VARBYTE`
- `NIBBLE`
- `BIT`
- `VARBIT`
- `BLOB`
- `CLOB`
- `LOB`
- `JSON`
- `Temporary LOB`
- `GEOMETRY`
- `POINT`
- `MULTIPOINT`
- `LINESTRING`
- `MULTILINESTRING`
- `POLYGON`
- `MULTIPOLYGON`
- `GEOMETRYCOLLECTION`
- `WKB`
- `WKT`
- `EWKB`
- `EWKT`

## SQL Functions and Operators

Preserve function and operator names. Add parentheses when writing a callable function,
for example `JSON_VALUE()`, unless quoting a source heading without parentheses.

### 8.1 JSON Tokens

- `JSON`
- `JSON_ARRAY`
- `JSON_OBJECT`
- `JSON_EXISTS`
- `JSON_QUERY`
- `JSON_VALUE`
- `JSON_VALID`
- `IS JSON`
- `JSON Path Expression`
- `NULL ON ERROR`
- `ERROR ON ERROR`
- `FALSE ON ERROR`
- `TRUE ON ERROR`
- `NULL ON EMPTY`
- `ERROR ON EMPTY`
- `DEFAULT ... ON ERROR`
- `DEFAULT ... ON EMPTY`
- `ABSENT ON NULL`
- `NULL ON NULL`
- `RETURNING JSON`
- `RETURNING CLOB`
- `WITH WRAPPER`
- `WITHOUT WRAPPER`
- `WITH CONDITIONAL WRAPPER`

### Aggregate and Analytic Functions

- `AVG`
- `COUNT`
- `MAX`
- `MIN`
- `SUM`
- `GROUP_CONCAT`
- `LISTAGG`
- `STDDEV`
- `STDDEV_POP`
- `STDDEV_SAMP`
- `VARIANCE`
- `VAR_POP`
- `VAR_SAMP`
- `DENSE_RANK`
- `RANK`
- `ROW_NUMBER`
- `NTILE`
- `LAG`
- `LEAD`
- `FIRST_VALUE`
- `LAST_VALUE`
- `NTH_VALUE`
- `RATIO_TO_REPORT`
- `PERCENT_RANK`
- `PERCENTILE_CONT`
- `PERCENTILE_DISC`

### Scalar and String Functions

- `ABS`
- `CEIL`
- `FLOOR`
- `ROUND`
- `TRUNC`
- `MOD`
- `POWER`
- `RAND`
- `RANDOM`
- `SIGN`
- `ASCII`
- `CHR`
- `NCHR`
- `CONCAT`
- `LOWER`
- `UPPER`
- `INITCAP`
- `INSTR`
- `INSTRB`
- `POSITION`
- `LPAD`
- `RPAD`
- `LTRIM`
- `RTRIM`
- `TRIM`
- `SUBSTR`
- `SUBSTRB`
- `SUBSTRING`
- `TRANSLATE`
- `REGEXP_COUNT`
- `REGEXP_INSTR`
- `REGEXP_REPLACE`
- `REGEXP_SUBSTR`
- `CHAR_LENGTH`
- `CHARACTER_LENGTH`
- `OCTET_LENGTH`
- `LENGTH`
- `LENGTHB`
- `SIZEOF`

### Spatial Functions and Metadata

- `DIMENSION`
- `GEOMETRYTYPE`
- `ENVELOPE`
- `ASTEXT`
- `ASBINARY`
- `ASEWKT`
- `ASEWKB`
- `ISEMPTY`
- `ISSIMPLE`
- `ISVALID`
- `ISVALIDHEADER`
- `BOUNDARY`
- `GEOMETRYLENGTH`
- `STARTPOINT`
- `ENDPOINT`
- `ISCLOSED`
- `ISRING`
- `ST_ISCOLLECTION`
- `NUMPOINTS`
- `POINTN`
- `AREA`
- `CENTROID`
- `POINTONSURFACE`
- `EXTERIORRING`
- `NUMINTERIORRING`
- `INTERIORRINGN`
- `NUMGEOMETRIES`
- `DISTANCE`
- `BUFFER`
- `CONVEXHULL`
- `INTERSECTION`
- `UNION`
- `DIFFERENCE`
- `SYMDIFFERENCE`
- `SRID`
- `SETSRID`
- `GEOMFROMTEXT`
- `POINTFROMTEXT`
- `POLYFROMTEXT`
- `ST_POLYGONFROMTEXT`
- `GEOMFROMWKB`
- `POINTFROMWKB`
- `ST_LINESTRINGFROMWKB`
- `ST_MAKEPOINT`
- `ST_POINT`
- `ST_MAKELINE`
- `ST_MAKEPOLYGON`
- `ST_POLYGON`
- `ST_COLLECT`
- `ST_MAKEENVELOPE`
- `ST_REVERSE`
- `ST_TRANSFORM`
- `EQUALS`
- `NOTEQUALS`
- `DISJOINT`
- `INTERSECTS`
- `TOUCHES`
- `NOTTOUCHES`
- `CROSSES`
- `NOTCROSSES`
- `WITHIN`
- `NOTWITHIN`
- `CONTAINS`
- `NOTCONTAINS`
- `OVERLAPS`
- `NOTOVERLAPS`
- `RELATE`
- `NOTRELATE`
- `ISMBRINTERSECTS`
- `ISMBRWITHIN`
- `ISMBRCONTAINS`
- `GEOMETRY_COLUMNS`
- `SPATIAL_REF_SYS`
- `ADD_SPATIAL_REF_SYS`
- `DELETE_SPATIAL_REF_SYS`

## Optimizer Hints

Preserve hint names exactly, including underscores and space-separated forms.

- `APPEND`
- `CNF`
- `COST`
- `DELAY`
- `DISTINCT_HASH`
- `DISTINCT_SORT`
- `DNF`
- `EXEC_FAST`
- `FIRST_ROWS`
- `FULL SCAN`
- `GROUP_HASH`
- `GROUP_SORT`
- `HASH_AJ`
- `HASH_SJ`
- `INDEX`
- `INDEX ASC`
- `INDEX DESC`
- `INDEX_ASC`
- `INDEX_DESC`
- `INVERSE_JOIN`
- `KEEP_PLAN`
- `LEADING`
- `MERGE_AJ`
- `MERGE_SJ`
- `NL_AJ`
- `NL_SJ`
- `NO DELAY`
- `NO_EXEC_FAST`
- `NO_EXPAND`
- `NO INDEX`
- `NO_INDEX`
- `NO_INVERSE_JOIN`
- `NO_MERGE`
- `NO_PARALLEL`
- `NO_PLAN_CACHE`
- `NO_PUSH_SELECT_VIEW`
- `NO_SERIAL_FILTER`
- `NO_TRANSITIVE_PRED`
- `NO_UNNEST`
- `NO_USE_HASH`
- `NO_USE_MERGE`
- `NO_USE_NL`
- `NO_USE_SORT`
- `PARALLEL`
- `PLAN_CACHE_KEEP`
- `ORDERED`
- `PUSH_PRED`
- `PUSH_SELECT_VIEW`
- `RESULT_CACHE`
- `RULE`
- `SERIAL_FILTER`
- `SORT_AJ`
- `SORT_SJ`
- `TEMP_TBS_DISK`
- `TEMP_TBS_MEMORY`
- `TOP_RESULT_CACHE`
- `UNNEST`
- `USE_ANTI`
- `USE_CONCAT`
- `USE_FULL_NL`
- `USE_FULL_STORE_NL`
- `USE_HASH`
- `USE_INDEX_NL`
- `USE_INVERSE_HASH`
- `USE_MERGE`
- `USE_NL`
- `USE_ONE_PASS_HASH`
- `USE_ONE_PASS_SORT`
- `USE_SORT`
- `USE_TWO_PASS_HASH`
- `USE_TWO_PASS_SORT`

## Properties and Configuration Keys

Preserve every property name from `altibase.properties`, `aexport.properties`,
`aku.conf`, and source manual property tables. Treat all-uppercase underscore tokens as
literal unless the context clearly shows ordinary prose.

### High-Priority Server Properties

- `ACCESS_LIST`
- `ADMIN_MODE`
- `ARCHIVE_DIR`
- `ARCHIVE_FULL_ACTION`
- `ARCHIVE_MULTIPLEX_COUNT`
- `ARCHIVE_MULTIPLEX_DIR`
- `AUDIT_FILE_SIZE`
- `AUDIT_LOG_DIR`
- `AUDIT_OUTPUT_METHOD`
- `AUTO_COMMIT`
- `BUFFER_AREA_SIZE`
- `BUFFER_FLUSHER_CNT`
- `CHECKPOINT_ENABLED`
- `CHECKPOINT_INTERVAL_IN_LOG`
- `CHECKPOINT_INTERVAL_IN_SEC`
- `COMMIT_WRITE_WAIT_MODE`
- `DB_NAME`
- `DEFAULT_DATE_FORMAT`
- `DEFAULT_DISK_DB_DIR`
- `DEFAULT_MEM_DB_FILE_SIZE`
- `DIRECT_IO_ENABLED`
- `DISK_LOB_COLUMN_IN_ROW_SIZE`
- `DISK_MAX_DB_SIZE`
- `DOUBLE_WRITE_DIRECTORY`
- `ERROR_MSGLOG_FILE`
- `EXEC_DDL_DISABLE`
- `FAILED_LOGIN_ATTEMPTS`
- `FETCH_TIMEOUT`
- `GROUP_CONCAT_PRECISION`
- `HASH_AREA_SIZE`
- `IDLE_TIMEOUT`
- `INDEX_BUILD_THREAD_COUNT`
- `ISOLATION_LEVEL`
- `JOB_SCHEDULER_ENABLE`
- `LOB_CACHE_THRESHOLD`
- `LOB_OBJECT_BUFFER_SIZE`
- `LOCK_ESCALATION_MEMORY_SIZE`
- `LOGANCHOR_DIR`
- `LOG_BUFFER_TYPE`
- `LOG_CREATE_METHOD`
- `LOG_DIR`
- `LOG_FILE_SIZE`
- `LOG_IO_TYPE`
- `LOG_MULTIPLEX_COUNT`
- `LOG_MULTIPLEX_DIR`
- `LOGIN_TIMEOUT`
- `MAX_CLIENT`
- `MAX_STATEMENTS_PER_SESSION`
- `MEM_DB_DIR`
- `MEM_MAX_DB_SIZE`
- `NLS_COMP`
- `NLS_CURRENCY`
- `NLS_NCHAR_LITERAL_REPLACE`
- `NLS_NUMERIC_CHARACTERS`
- `NLS_TERRITORY`
- `OPTIMIZER_AUTO_STATS`
- `OPTIMIZER_DELAYED_EXECUTION`
- `OPTIMIZER_FEATURE_ENABLE`
- `OPTIMIZER_MODE`
- `OPTIMIZER_PERFORMANCE_VIEW`
- `PORT_NO`
- `PSM_CASE_SENSITIVE_MODE`
- `QUERY_PROF_FLAG`
- `QUERY_PROF_LOG_DIR`
- `QUERY_REWRITE_ENABLE`
- `QUERY_STACK_SIZE`
- `QUERY_TIMEOUT`
- `RECYCLEBIN_ENABLE`
- `REMOTE_SYSDBA_ENABLE`
- `RESULT_CACHE_ENABLE`
- `SERVER_MSGLOG_FILE`
- `SHUTDOWN_IMMEDIATE_TIMEOUT`
- `SNMP_ENABLE`
- `SNMP_PORT_NO`
- `SNMP_TRAP_PORT_NO`
- `SORT_AREA_SIZE`
- `SQL_PLAN_CACHE_BUCKET_CNT`
- `SQL_PLAN_CACHE_SIZE`
- `TABLESPACE_LOCK_ENABLE`
- `TABLE_LOCK_ENABLE`
- `TEMP_HASH_BUCKET_DENSITY`
- `TIME_ZONE`
- `TRANSACTION_TABLE_SIZE`
- `UNIXDOMAIN_FILEPATH`
- `UTRANS_TIMEOUT`
- `VOLATILE_MAX_DB_SIZE`

### Replication Properties

- `REPLICATION_ACK_XLOG_COUNT`
- `REPLICATION_ALLOW_DUPLICATE_HOSTS`
- `REPLICATION_BEFORE_IMAGE_LOG_ENABLE`
- `REPLICATION_COMMIT_WRITE_WAIT_MODE`
- `REPLICATION_CONNECT_RECEIVE_TIMEOUT`
- `REPLICATION_CONNECT_TIMEOUT`
- `REPLICATION_DDL_ENABLE`
- `REPLICATION_DDL_ENABLE_LEVEL`
- `REPLICATION_DDL_SYNC`
- `REPLICATION_DDL_SYNC_TIMEOUT`
- `REPLICATION_EAGER_PARALLEL_FACTOR`
- `REPLICATION_EAGER_RECEIVER_MAX_ERROR_COUNT`
- `REPLICATION_FAILBACK_INCREMENTAL_SYNC`
- `REPLICATION_GAP_UNIT`
- `REPLICATION_GAPLESS_ALLOW_TIME`
- `REPLICATION_GAPLESS_MAX_WAIT_TIME`
- `REPLICATION_GROUPING_AHEAD_READ_NEXT_LOG_FILE`
- `REPLICATION_GROUPING_TRANSACTION_MAX_COUNT`
- `REPLICATION_HBT_DETECT_HIGHWATER_MARK`
- `REPLICATION_HBT_DETECT_TIME`
- `REPLICATION_IB_LATENCY`
- `REPLICATION_IB_PORT_NO`
- `REPLICATION_INSERT_REPLACE`
- `REPLICATION_KEEP_ALIVE_CNT`
- `REPLICATION_LOCK_TIMEOUT`
- `REPLICATION_LOG_BUFFER_SIZE`
- `REPLICATION_MAX_COUNT`
- `REPLICATION_MAX_LISTEN`
- `REPLICATION_MAX_LOGFILE`
- `REPLICATION_POOL_ELEMENT_COUNT`
- `REPLICATION_POOL_ELEMENT_SIZE`
- `REPLICATION_PORT_NO`
- `REPLICATION_PREFETCH_LOGFILE_COUNT`
- `REPLICATION_RECEIVE_TIMEOUT`
- `REPLICATION_RECEIVER_APPLIER_ASSIGN_MODE`
- `REPLICATION_RECEIVER_APPLIER_QUEUE_SIZE`
- `REPLICATION_RECOVERY_MAX_LOGFILE`
- `REPLICATION_RECOVERY_MAX_TIME`
- `REPLICATION_SENDER_AUTO_START`
- `REPLICATION_SENDER_COMPRESS_XLOG`
- `REPLICATION_SENDER_ENCRYPT_XLOG`
- `REPLICATION_SENDER_SEND_TIMEOUT`
- `REPLICATION_SENDER_SLEEP_TIME`
- `REPLICATION_SENDER_SLEEP_TIMEOUT`
- `REPLICATION_SENDER_START_AFTER_GIVING_UP`
- `REPLICATION_SERVER_FAILBACK_MAX_TIME`
- `REPLICATION_SQL_APPLY_ENABLE`
- `REPLICATION_SSL_PORT_NO`
- `REPLICATION_SYNC_APPLY_METHOD`
- `REPLICATION_SYNC_LOCK_TIMEOUT`
- `REPLICATION_SYNC_LOG`
- `REPLICATION_SYNC_TUPLE_COUNT`
- `REPLICATION_TIMESTAMP_RESOLUTION`
- `REPLICATION_TRANSACTION_POOL_SIZE`
- `REPLICATION_UPDATE_REPLACE`

### SSL/TLS Properties

- `SSL_CA`
- `SSL_CAPATH`
- `SSL_CERT`
- `SSL_CIPHER_LIST`
- `SSL_CIPHER_SUITES`
- `SSL_CLIENT_AUTHENTICATION`
- `SSL_ENABLE`
- `SSL_KEY`
- `SSL_LOAD_CONFIG`
- `SSL_MAX_LISTEN`
- `SSL_PORT_NO`

### 8.1 JSON and Temporary LOB Properties

- `TEMPORARY_LOB_ENABLE`
- `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`
- `MEMORY_TEMPLOB_PIECE_SIZE`
- `REPLICATION_SSL_PORT_NO`

### Environment Variables

- `ALTIBASE_HOME`
- `ALTIBASE_PORT_NO`
- `ALTIBASE_SSL_PORT_NO`
- `ALTIBASE_NLS_USE`
- `ALTIBASE_NLS_NCHAR_LITERAL_REPLACE`
- `ALTIBASE_DATE_FORMAT`
- `ALTIBASE_IPC_FILEPATH`
- `ALTIBASE_TIME_ZONE`
- `ALTIBASE_UT_FILE_PERMISSION`
- `ALTIBASE_ENV`
- `ISQL_CONNECTION`
- `ISQL_BUFFER_SIZE`
- `ISQL_EDITOR`
- `ISQL_FILE_PERMISSION`
- `ISQL_SECURE_LOGIN_MSG`
- `IPCDA_FILEPATH`
- `ALTI_HBP_HOME`
- `PATH`
- `LD_LIBRARY_PATH`

### Tool Configuration Keys and Files

- `altibase.properties`
- `aexport.properties`
- `aexport.properties.sample`
- `aku.conf`
- `aku.conf.sample`
- `glogin.sql`
- `login.sql`
- `aheartbeat.settings`
- `sample.cfg`
- `OPERATION`
- `OBJECT`
- `EXECUTE`
- `TWO_PHASE_SCRIPT`
- `NLS_USE`
- `ILOADER_ARRAY`
- `AKU_ALTIBASE_HOME`
- `AKU_QUERY_TIMEOUT`
- `AKU_QUERY_RETRY_COUNT`
- `AKU_QUERY_RETRY_DELAY_MSEC`
- `AKU_REPLICATION_RESET_AT_END`

## Data Dictionary, Meta Tables, and Performance Views

Preserve dictionary object names exactly. Do not translate `SYS_`, `V$`, `X$`, `SYSTEM_`,
or trailing underscores.

### Common Meta Tables

- `SYSTEM_.SYS_USERS_`
- `SYSTEM_.SYS_TABLES_`
- `SYSTEM_.SYS_COLUMNS_`
- `SYSTEM_.SYS_INDICES_`
- `SYSTEM_.SYS_INDEX_COLUMNS_`
- `SYSTEM_.SYS_CONSTRAINTS_`
- `SYSTEM_.SYS_CONSTRAINT_COLUMNS_`
- `SYSTEM_.SYS_TABLESPACES_`
- `SYS_AUDIT_`
- `SYS_AUDIT_OPTS_`
- `SYS_COMMENTS_`
- `SYS_COMPRESSION_TABLES_`
- `SYS_DATABASE_`
- `SYS_DATABASE_LINKS_`
- `SYS_DIRECTORIES_`
- `SYS_ENCRYPTED_COLUMNS_`
- `SYS_GEOMETRIES_`
- `SYS_GEOMETRY_COLUMNS_`
- `SYS_GRANT_OBJECT_`
- `SYS_GRANT_SYSTEM_`
- `SYS_JOBS_`
- `SYS_LIBRARIES_`
- `SYS_LOBS_`
- `SYS_MATERIALIZED_VIEWS_`
- `SYS_PACKAGES_`
- `SYS_PROCEDURES_`
- `SYS_PRIVILEGES_`
- `SYS_RECYCLEBIN_`
- `SYS_REPLICATIONS_`
- `SYS_REPL_HOSTS_`
- `SYS_REPL_ITEMS_`
- `SYS_SECURITY_`
- `SYS_SYNONYMS_`
- `SYS_TRIGGERS_`
- `SYS_USERS_`
- `SYS_USER_ROLES_`
- `SYS_VIEWS_`
- `SYS_XA_HEURISTIC_TRANS_`

### Common Performance Views

- `V$ACCESS_LIST`
- `V$ARCHIVE`
- `V$BACKUP_INFO`
- `V$BUFFPAGEINFO`
- `V$BUFFPOOL_STAT`
- `V$CATALOG`
- `V$DATABASE`
- `V$DATAFILES`
- `V$DATATYPE`
- `V$DBA_2PC_PENDING`
- `V$DBLINK_ALTILINKER_STATUS`
- `V$DBLINK_DATABASE_LINK_INFO`
- `V$DBLINK_GLOBAL_TRANSACTION_INFO`
- `V$DBMS_STATS`
- `V$DB_FREEPAGELISTS`
- `V$DB_PROTOCOL`
- `V$DIRECT_PATH_INSERT`
- `V$DISKTBL_INFO`
- `V$DISK_TEMP_INFO`
- `V$DISK_TEMP_STAT`
- `V$DISK_UNDO_USAGE`
- `V$EVENT_NAME`
- `V$EXTPROC_AGENT`
- `V$FILESTAT`
- `V$FLUSHER`
- `V$FLUSHINFO`
- `V$INDEX`
- `V$INSTANCE`
- `V$INTERNAL_SESSION`
- `V$LATCH`
- `V$LFG`
- `V$LIBRARY`
- `V$LOCK`
- `V$LOCK_STATEMENT`
- `V$LOCK_TABLE_STATS`
- `V$LOCK_WAIT`
- `V$LOG`
- `V$MEMGC`
- `V$MEMSTAT`
- `V$MEMTBL_INFO`
- `V$MEM_TABLESPACES`
- `V$MEM_TABLESPACE_CHECKPOINT_PATHS`
- `V$MUTEX`
- `V$NLS_PARAMETERS`
- `V$NLS_TERRITORY`
- `V$OBSOLETE_BACKUP_INFO`
- `V$PKGTEXT`
- `V$PLANTEXT`
- `V$PROCINFO`
- `V$PROPERTY`
- `V$REPGAP`
- `V$REPLOGBUFFER`
- `V$REPOFFLINE_STATUS`
- `V$REPRECEIVER`
- `V$REPRECEIVER_STATISTICS`
- `V$REPRECOVERY`
- `V$REPSENDER`
- `V$REPSENDER_STATISTICS`
- `V$REPSYNC`
- `V$RESERVED_WORDS`
- `V$SBUFFER_STAT`
- `V$SEQ`
- `V$SERVICE_THREAD`
- `V$SESSION`
- `V$SESSIONMGR`
- `V$SESSION_EVENT`
- `V$SESSION_WAIT`
- `V$SESSION_WAIT_CLASS`
- `V$SQLTEXT`
- `V$SQL_PLAN_CACHE`
- `V$STATEMENT`
- `V$STATNAME`
- `V$SYSTEM_EVENT`
- `V$SYSTEM_WAIT_CLASS`
- `V$TABLE`
- `V$TABLESPACES`
- `V$TEMPORARY_LOBS`
- `V$TIME_ZONE_NAMES`
- `V$TRACELOG`
- `V$TRANSACTION`
- `V$TRANSACTION_MGR`
- `V$USAGE`
- `V$VERSION`
- `V$VOL_TABLESPACES`
- `V$WAIT_CLASS_NAME`
- `V$XID`

## Client API and Programming Tokens

Preserve class, package, function, macro, structure, enum, and constant names exactly.

### JDBC and Java

- `Altibase.jdbc.driver.AltibaseDriver`
- `DriverManager`
- `DataSource`
- `Statement`
- `PreparedStatement`
- `CallableStatement`
- `ResultSet`
- `java.sql.PreparedStatement`
- `java.sql.ResultSet`
- `java.sql.SQLTypes`
- `SQLException`
- `jdbc:Altibase://`
- `hibernate.dialect`
- `AltibaseDialect`

### CLI, ODBC, and C Interface

- `SQLAllocConnect`
- `SQLAllocEnv`
- `SQLAllocHandle`
- `SQLAllocStmt`
- `SQLBindCol`
- `SQLBindParameter`
- `SQLBulkOperations`
- `SQLCancel`
- `SQLCloseCursor`
- `SQLColAttribute`
- `SQLColumns`
- `SQLConnect`
- `SQLDescribeCol`
- `SQLDescribeParam`
- `SQLDisconnect`
- `SQLDriverConnect`
- `SQLEndTran`
- `SQLError`
- `SQLExecDirect`
- `SQLExecute`
- `SQLFetch`
- `SQLFetchScroll`
- `SQLFreeConnect`
- `SQLFreeEnv`
- `SQLFreeHandle`
- `SQLFreeStmt`
- `SQLGetConnectAttr`
- `SQLGetData`
- `SQLGetDiagField`
- `SQLGetDiagRec`
- `SQLGetEnvAttr`
- `SQLGetFunctions`
- `SQLGetInfo`
- `SQLGetPlan`
- `SQLGetStmtAttr`
- `SQLMoreResults`
- `SQLNativeSql`
- `SQLNumParams`
- `SQLNumResultCols`
- `SQLParamData`
- `SQLPrepare`
- `SQLPrimaryKeys`
- `SQLPutData`
- `SQLRowCount`
- `SQLSetConnectAttr`
- `SQLSetEnvAttr`
- `SQLSetStmtAttr`
- `SQLTables`
- `SQLTransact`
- `SQLBindFileToCol`
- `SQLBindFileToParam`
- `SQLGetLobLength`
- `SQLGetLob`
- `SQLPutLob`
- `SQLTrimLob`
- `SQLFreeLob`
- `SQLSTATE`
- `SQLCODE`
- `SQLCA`
- `SQLDA`
- `ALTIBASE_APRE`
- `ALTIBASE_BIND`

## Error Codes and Rule IDs

Preserve the complete code or identifier exactly. Translate the surrounding explanation
only.

### Error Code Forms

- Hexadecimal error codes: `0x00012`, `0x01044`, `0x2106D`, `0x314C3`
- Decimal numbers shown with error codes: `( 18)`, `( 4176)`, `( 135277)`
- Error identifiers: `idERR_FATAL_idc_SHM_ATTACH`, `idERR_ABORT_Query_Timeout`,
  `mtERR_ABORT_JSON_WITHOUT_TEMPLOB`, `qpERR_ABORT_JSON_OBJECT_INCOMPLETE`
- SQL diagnostics: `SQLSTATE`, `SQLCODE`, `SQLERRM`
- Migration rule IDs: `RULE-11001`, `RULE-12002`, `RULE-13001`, `RULE-14001`,
  `RULE-16001`, `RULE-17001`, `RULE-20001`

### Error Answering Rule

If the user asks in another language, keep the literal code and identifier first, then
explain the cause and action in the user's language. Do not translate the identifier
segments such as `ERR`, `FATAL`, `ABORT`, `JSON`, `TEMPLOB`, or `Query_Timeout`.

## Command and Path Tokens

Preserve commands, options, file names, path variables, and path separators exactly.

### Common Commands and Options

- `server start`
- `server stop`
- `server restart`
- `server status`
- `isql -s`
- `isql -u`
- `isql -p`
- `isql -port`
- `isql -sysdba`
- `isql -silent`
- `isql -f`
- `iloader in`
- `iloader out`
- `iloader formout`
- `iloader -s`
- `iloader -port`
- `iloader -u`
- `iloader -p`
- `iloader -f`
- `iloader -d`
- `aexport -s`
- `aexport -u`
- `aexport -p`
- `aexport -port`
- `aexport -tserver`
- `aexport -tport`
- `aexport -prefer_ipv6`
- `aexport -ssl_ca`
- `aexport -ssl_capath`
- `altiComp -f`
- `aku -p start`
- `aku -p end`
- `aku -p clean`
- `aku -i`
- `altimon.sh start`
- `altimon.sh stop`
- `altiAudit -s`
- `aheartbeat start`
- `aheartbeat stop`

### Common Files and Paths

- `$ALTIBASE_HOME`
- `$ALTIBASE_HOME/bin`
- `$ALTIBASE_HOME/conf`
- `$ALTIBASE_HOME/trc`
- `$ALTIBASE_HOME/altiMon/logs/altimon.log`
- `$ALTIBASE_HOME/conf/altibase.properties`
- `$ALTIBASE_HOME/conf/aexport.properties`
- `$ALTIBASE_HOME/conf/aku.conf`
- `$ALTI_HBP_HOME`
- `$ALTI_HBP_HOME/bin`
- `$ALTI_HBP_HOME/conf`
- `/altibase_home/trc`
- `/tmp`
- `run_il_out.sh`
- `run_il_in.sh`
- `run_is.sh`
- `run_is_con.sh`
- `run_is_refresh_mview.sh`
- `run_is_index.sh`
- `run_is_fk.sh`
- `run_is_repl.sh`
- `run_is_job.sh`
- `run_is_alt_tbl.sh`

## Object Naming Policy for Generated SQL

For generated examples, use simple ASCII identifiers and preserve them consistently
across the answer.

Recommended sample names:

- `T_CUSTOMER`
- `T_ORDER`
- `T_EVENT`
- `IDX_CUSTOMER_01`
- `PK_CUSTOMER`
- `SEQ_ORDER_ID`
- `MEM_TBS`
- `DISK_TBS`
- `TEMP_TBS`
- `REP_SALES`
- `APP_USER`

Never translate user-supplied object names. If the user provides `고객주문`, `"Order Detail"`,
`customer_order`, or `T1`, preserve the exact identifier unless they explicitly ask for a
renaming or romanization.

## Translation Guidance by Term Type

| Term type | Translate prose? | Preserve token? | Example |
| --- | --- | --- | --- |
| Product/tool names | Yes, explain in user language. | Yes. | Keep `iLoader`; explain it as a load/extract utility. |
| SQL syntax | Explain in user language. | Yes. | Keep `CREATE MEMORY TABLESPACE`. |
| SQL object identifiers | No, not unless the user asks. | Yes. | Keep `REP_SALES` or `SYSTEM_.SYS_USERS_`. |
| Concepts | Yes. | Use English canonical term when needed. | "memory table" may be translated, but `MEMORY` in SQL stays literal. |
| Properties | Explain in user language. | Yes. | Keep `LOG_FILE_SIZE`. |
| File paths | Explain in user language. | Yes. | Keep `$ALTIBASE_HOME/conf/altibase.properties`. |
| Error codes | Explain cause/action in user language. | Yes. | Keep `0x01044` and `idERR_ABORT_Query_Timeout`. |
| API names | Explain in user language. | Yes. | Keep `SQLConnect()` and `PreparedStatement`. |

## Examples for Multilingual Answers

Korean:

```text
`REPLICATION_SSL_PORT_NO`를 설정한 뒤 `CREATE REPLICATION ... USING SSL` 구문으로
SSL/TLS 기반 replication을 생성합니다.
```

Vietnamese:

```text
Kiểm tra phiên bằng `V$SESSION`, sau đó xác nhận thuộc tính `QUERY_TIMEOUT` trong
`V$PROPERTY`.
```

Turkish:

```text
`iLoader` ile veri yüklerken biçim dosyasını `iloader formout` ile oluşturun ve
yükleme için `iloader in` komutunu kullanın.
```

French:

```text
Pour une table mémoire, utilisez `CREATE TABLE ... TABLESPACE MEM_TBS` et vérifiez
le tablespace avec `V$TABLESPACES`.
```

## Maintenance Notes for Later Jobs

- When an attachment job adds a new property, command, API, view, or error identifier,
  preserve the source token exactly and add it here if it is high-frequency.
- Do not copy Korean source headings into customer-facing attachments unless the content
  is translated and normalized into English canonical text.
- For 8.1 JSON, Temporary LOB, and replication SSL content, use English release notes as
  the customer-facing source where sufficient. Use Korean fallback only as source support
  and keep the output English canonical.
