# 06. Data Dictionary and Performance Views

## Applicable Versions

- 7.1: Based on Altibase 7.1 General Reference 2.
- 7.3: Based on Altibase 7.3 General Reference 2.
- 8.1: Based on Altibase 8.1 verified source General Reference 2 and Altibase 8.1 Release Notes.

## Questions This File Can Answer

- Which meta table or performance view should be queried for a table, index, column, user, privilege, session, lock, transaction, replication, tablespace, property, or plan cache question?
- How do I generate check SQL for a specific object name?
- How do I check running sessions, statements, waits, locks, and replication gap?
- How do I inspect tablespaces, datafiles, archive log mode, backup metadata, checkpoint image state, and file I/O hotspots?
- Which dictionary and performance view checks are version-sensitive in 8.1?
- How should a GPT answer data dictionary questions in the user's language while preserving SQL names and object names literally?

## Source Documents

- 7.1: Altibase 7.1 General Reference 2.
- 7.3: Altibase 7.3 General Reference 2.
- 8.1: Altibase 8.1 verified source General Reference 2; Altibase 8.1 Release Notes.

## Response Rules

- Answer explanatory text in the user's language.
- Keep SQL object names, column names, function names, property names, error codes, commands, and file paths literal.
- Use `SYSTEM_.SYS_*` for meta tables when showing fully qualified dictionary SQL.
- Query meta tables with `SELECT`. Do not suggest direct DML against meta tables except to explain that it is unsafe and should be avoided.
- If the user supplies an object name, include owner-qualified check SQL when possible. Use `'<OWNER_NAME>'`, `'<TABLE_NAME>'`, `'<INDEX_NAME>'`, `'<USER_NAME>'`, `'<REPLICATION_NAME>'`, and similar placeholders when the exact value is not known.
- For quoted mixed-case object names, tell the user to use the exact stored value in the meta table predicates.
- For cross-version answers, first check performance-view availability with `V$TABLE` and `V$ALLCOLUMN`, and check meta-table column availability with `SYSTEM_.SYS_TABLES_` and `SYSTEM_.SYS_COLUMNS_` when a column may vary by version.

## Version Notes

- 7.1 and 7.3: Use the General Reference 2 meta table and performance view definitions for the target version.
- 8.1: The release notes state that no meta tables were added, deleted, or changed.
- 8.1: `V$LOG.CHECKPOINT_SCALE` and `V$MEM_STABLE` are documented in the Altibase 8.1 verified source data dictionary and are used with `V$MEM_TABLESPACES.CURRENT_DB` for memory checkpoint image checks. For 7.1/7.3-compatible SQL, check `V$ALLCOLUMN` before selecting `CHECKPOINT_SCALE`.
- 8.1: Temporary LOB support is documented in the Altibase 8.1 release notes. Check Temporary LOB usage with `V$TEMPORARY_LOBS` when that view exists.
- Version-sensitive view check: the 8.1 release notes list `V$LOCK_TABLE_STATS`, `V$MEM_STABLE`, and `V$TEMPORARY_LOBS`; 7.1 and 7.3 General Reference 2 also document `V$LOCK_TABLE_STATS`. For portable answers, check `V$TABLE` before relying on these views.
- Version-sensitive meta-table column check: `SYSTEM_.SYS_REPL_ITEMS_.IS_CONDITION_SYNCED` is documented for 7.3 and 8.1, but not for the 7.1 `SYSTEM_.SYS_REPL_ITEMS_` layout. For 7.1-compatible SQL, omit that column unless the target database exposes it.

```sql
SELECT name, columncount
FROM V$TABLE
WHERE name IN ('V$LOCK_TABLE_STATS', 'V$MEM_STABLE', 'V$TEMPORARY_LOBS')
ORDER BY name;

SELECT tablename, colname
FROM V$ALLCOLUMN
WHERE tablename IN ('V$SESSION', 'V$STATEMENT', 'V$TEMPORARY_LOBS')
ORDER BY tablename, colname;
```

## Dictionary and Performance View Inventory Baseline

Use this baseline to choose the right object family before moving to the cookbook SQL
or detailed object blocks below. It is a name, version, and grouping baseline, not a
promise that every column is identical across every patch. When a final answer depends
on an uncommon column, exact patch level, or installed metadata layout, check the
target database first with `V$TABLE`, `V$ALLCOLUMN`, `SYSTEM_.SYS_TABLES_`, and
`SYSTEM_.SYS_COLUMNS_`.

Inventory summary:

- Meta tables: 71 names are common to 7.1, 7.3, and the Altibase 8.1 verified source.
  `SYS_REPL_TABLE_OID_IN_USE_` is listed in 7.1 and 7.3 General Reference 2; verify
  installed 8.1 metadata before relying on it because the checked 8.1 General Reference
  2 table does not list it even though the 8.1 release notes state that no meta tables
  were added, deleted, or changed.
- Performance views: 125 names are common to 7.1, 7.3, and the Altibase 8.1 verified
  source. `V$MEM_STABLE` and `V$TEMPORARY_LOBS` are Altibase 8.1 verified source views.
  `V$ST_ANGULAR_UNIT`, `V$ST_AREA_UNIT`, and `V$ST_LINEAR_UNIT` are listed in Altibase
  7.1 General Reference 2 as reserved spatial unit views; check `V$TABLE` before using
  them on later versions.
- `V$LOCK_TABLE_STATS` is documented in 7.1 and 7.3 General Reference 2 and is also
  listed in the 8.1 release notes. For portable SQL, still check `V$TABLE` before
  assuming the view exists.

### Meta Table Inventory Groups

Unless an exception is called out, these groups are available in 7.1, 7.3, and the
Altibase 8.1 verified source.

| Group | Names |
| --- | --- |
| Audit and security | `SYS_AUDIT_`, `SYS_AUDIT_OPTS_`, `SYS_SECURITY_`, `SYS_ENCRYPTED_COLUMNS_` |
| Core database and internal support | `SYS_DATABASE_`, `SYS_DN_USERS_`, `SYS_DUMMY_` |
| Objects, columns, comments, LOBs, and size | `SYS_TABLES_`, `SYS_COLUMNS_`, `SYS_COMMENTS_`, `SYS_COMPRESSION_TABLES_`, `SYS_LOBS_`, `SYS_TABLE_SIZE_`, `SYS_RECYCLEBIN_` |
| Constraints, indexes, and partitions | `SYS_CONSTRAINTS_`, `SYS_CONSTRAINT_COLUMNS_`, `SYS_CONSTRAINT_RELATED_`, `SYS_INDICES_`, `SYS_INDEX_COLUMNS_`, `SYS_INDEX_PARTITIONS_`, `SYS_INDEX_RELATED_`, `SYS_PART_INDICES_`, `SYS_PART_KEY_COLUMNS_`, `SYS_PART_LOBS_`, `SYS_PART_TABLES_`, `SYS_TABLE_PARTITIONS_` |
| Users, roles, privileges, passwords, and tablespace access | `SYS_USERS_`, `DBA_USERS_`, `SYS_USER_ROLES_`, `SYS_PRIVILEGES_`, `SYS_GRANT_SYSTEM_`, `SYS_GRANT_OBJECT_`, `SYS_TBS_USERS_`, `SYS_PASSWORD_HISTORY_`, `SYS_PASSWORD_LIMITS_` |
| Procedures, packages, views, triggers, jobs, and schema helpers | `SYS_PROCEDURES_`, `SYS_PROC_PARAS_`, `SYS_PROC_PARSE_`, `SYS_PROC_RELATED_`, `SYS_PACKAGES_`, `SYS_PACKAGE_PARAS_`, `SYS_PACKAGE_PARSE_`, `SYS_PACKAGE_RELATED_`, `SYS_DIRECTORIES_`, `SYS_LIBRARIES_`, `SYS_MATERIALIZED_VIEWS_`, `SYS_SYNONYMS_`, `SYS_VIEWS_`, `SYS_VIEW_PARSE_`, `SYS_VIEW_RELATED_`, `SYS_JOBS_`, `SYS_TRIGGERS_`, `SYS_TRIGGER_DML_TABLES_`, `SYS_TRIGGER_STRINGS_`, `SYS_TRIGGER_UPDATE_COLUMNS_` |
| Replication metadata | `SYS_REPLICATIONS_`, `SYS_REPL_HOSTS_`, `SYS_REPL_ITEMS_`, `SYS_REPL_OFFLINE_DIR_`, `SYS_REPL_OLD_CHECKS_`, `SYS_REPL_OLD_CHECK_COLUMNS_`, `SYS_REPL_OLD_COLUMNS_`, `SYS_REPL_OLD_INDEX_COLUMNS_`, `SYS_REPL_OLD_INDICES_`, `SYS_REPL_OLD_ITEMS_`, `SYS_REPL_RECOVERY_INFOS_`; `SYS_REPL_TABLE_OID_IN_USE_` is listed in 7.1 and 7.3 and should be verified on 8.1 before use. |
| Database link and distributed transaction metadata | `SYS_DATABASE_LINKS_`, `SYS_XA_HEURISTIC_TRANS_` |
| Spatial metadata | `SYS_GEOMETRIES_`, `SYS_GEOMETRY_COLUMNS_`, `USER_SRS_` |

### Performance View Inventory Groups

Unless an exception is called out, these groups are available in 7.1, 7.3, and the
Altibase 8.1 verified source.

| Group | Names |
| --- | --- |
| Inventory, catalog, properties, NLS, and object metadata | `V$TABLE`, `V$ALLCOLUMN`, `V$CATALOG`, `V$DATATYPE`, `V$PROPERTY`, `V$VERSION`, `V$TIME_ZONE_NAMES`, `V$NLS_PARAMETERS`, `V$NLS_TERRITORY`, `V$QUEUE_DELETE_OFF`, `V$SEQ`, `V$EXTPROC_AGENT` |
| Server access, sessions, statements, text, and service threads | `V$ACCESS_LIST`, `V$DB_PROTOCOL`, `V$INSTANCE`, `V$SESSION`, `V$INTERNAL_SESSION`, `V$SESSIONMGR`, `V$STATEMENT`, `V$SQLTEXT`, `V$PLANTEXT`, `V$PROCTEXT`, `V$PKGTEXT`, `V$SERVICE_THREAD`, `V$SERVICE_THREAD_MGR` |
| Wait events, locks, transactions, and distributed transaction state | `V$EVENT_NAME`, `V$WAIT_CLASS_NAME`, `V$SESSION_EVENT`, `V$SESSION_WAIT`, `V$SESSION_WAIT_CLASS`, `V$SYSTEM_EVENT`, `V$SYSTEM_WAIT_CLASS`, `V$SYSTEM_CONFLICT_PAGE`, `V$LATCH`, `V$MUTEX`, `V$LOCK`, `V$LOCK_WAIT`, `V$LOCK_STATEMENT`, `V$LOCK_TABLE_STATS`, `V$TRANSACTION`, `V$TRANSACTION_MGR`, `V$DBA_2PC_PENDING`, `V$XID` |
| System/session statistics, memory, and process counters | `V$STATNAME`, `V$SYSSTAT`, `V$SESSTAT`, `V$MEMSTAT`, `V$MEMGC` |
| Tablespaces, files, logs, backup, archive, and checkpoint state | `V$DATABASE`, `V$TABLESPACES`, `V$MEM_TABLESPACES`, `V$VOL_TABLESPACES`, `V$DATAFILES`, `V$STABLE_MEM_DATAFILES`, `V$MEM_TABLESPACE_CHECKPOINT_PATHS`, `V$MEM_TABLESPACE_STATUS_DESC`, `V$ARCHIVE`, `V$BACKUP_INFO`, `V$OBSOLETE_BACKUP_INFO`, `V$LOG`, `V$LFG`, `V$FILESTAT`, `V$TRACELOG`, `V$SNAPSHOT`; `V$MEM_STABLE` and `V$TEMPORARY_LOBS` are Altibase 8.1 verified source views. |
| Table, index, segment, space, and temporary storage internals | `V$MEMTBL_INFO`, `V$DISKTBL_INFO`, `V$INDEX`, `V$MEM_BTREE_HEADER`, `V$MEM_BTREE_NODEPOOL`, `V$DISK_BTREE_HEADER`, `V$DISK_RTREE_HEADER`, `V$MEM_RTREE_HEADER`, `V$MEM_RTREE_NODEPOOL`, `V$SEGMENT`, `V$USAGE`, `V$DB_FREEPAGELISTS`, `V$TSSEGS`, `V$TXSEGS`, `V$UDSEGS`, `V$DISK_UNDO_USAGE`, `V$DISK_TEMP_INFO`, `V$DISK_TEMP_STAT`, `V$DIRECT_PATH_INSERT` |
| Buffer pool, secondary buffer, and flush statistics | `V$BUFFPAGEINFO`, `V$BUFFPOOL_STAT`, `V$UNDO_BUFF_STAT`, `V$SBUFFER_STAT`, `V$FLUSHER`, `V$FLUSHINFO`, `V$SFLUSHER`, `V$SFLUSHINFO` |
| Optimizer statistics and SQL plan cache | `V$DBMS_STATS`, `V$SQL_PLAN_CACHE`, `V$SQL_PLAN_CACHE_PCO`, `V$SQL_PLAN_CACHE_SQLTEXT` |
| Replication runtime and recovery | `V$REPEXEC`, `V$REPGAP`, `V$REPGAP_PARALLEL`, `V$REPLOGBUFFER`, `V$REPOFFLINE_STATUS`, `V$REPRECEIVER`, `V$REPRECEIVER_COLUMN`, `V$REPRECEIVER_PARALLEL`, `V$REPRECEIVER_PARALLEL_APPLY`, `V$REPRECEIVER_STATISTICS`, `V$REPRECEIVER_TRANSTBL`, `V$REPRECEIVER_TRANSTBL_PARALLEL`, `V$REPRECOVERY`, `V$REPSENDER`, `V$REPSENDER_PARALLEL`, `V$REPSENDER_SENT_LOG_COUNT`, `V$REPSENDER_SENT_LOG_COUNT_PARALLEL`, `V$REPSENDER_STATISTICS`, `V$REPSENDER_TRANSTBL`, `V$REPSENDER_TRANSTBL_PARALLEL`, `V$REPSYNC` |
| Database link runtime | `V$DBLINK_ALTILINKER_STATUS`, `V$DBLINK_DATABASE_LINK_INFO`, `V$DBLINK_GLOBAL_TRANSACTION_INFO`, `V$DBLINK_LINKER_CONTROL_SESSION_INFO`, `V$DBLINK_LINKER_DATA_SESSION_INFO`, `V$DBLINK_LINKER_SESSION_INFO`, `V$DBLINK_NOTIFIER_TRANSACTION_INFO`, `V$DBLINK_REMOTE_STATEMENT_INFO`, `V$DBLINK_REMOTE_TRANSACTION_INFO` |
| Spatial unit catalog | `V$ST_ANGULAR_UNIT`, `V$ST_AREA_UNIT`, `V$ST_LINEAR_UNIT` are listed in Altibase 7.1 General Reference 2 as reserved spatial unit views. Check `V$TABLE` before using them on 7.3 or 8.1. |

### Inventory Verification SQL

```sql
SELECT name, slotsize, columncount
FROM V$TABLE
WHERE name IN (
  'V$LOCK_TABLE_STATS',
  'V$MEM_STABLE',
  'V$TEMPORARY_LOBS',
  'V$ST_ANGULAR_UNIT',
  'V$ST_AREA_UNIT',
  'V$ST_LINEAR_UNIT',
  'V$QUEUE_DELETE_OFF'
)
ORDER BY name;

SELECT tablename, colname
FROM V$ALLCOLUMN
WHERE tablename IN (
  'V$LOCK_TABLE_STATS',
  'V$MEM_STABLE',
  'V$TEMPORARY_LOBS',
  'V$QUEUE_DELETE_OFF'
)
ORDER BY tablename, colname;

SELECT t.table_name
FROM SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_USERS_ u
WHERE t.user_id = u.user_id
  AND u.user_name = 'SYSTEM_'
  AND t.table_name IN (
    'SYS_REPL_TABLE_OID_IN_USE_',
    'SYS_REPL_ITEMS_',
    'SYS_REPLICATIONS_'
  )
ORDER BY t.table_name;
```

## Fast Object Map

Use these first when selecting the right source:

| Task | Primary objects |
| --- | --- |
| Product and meta version | `V$VERSION` |
| Properties | `V$PROPERTY` |
| Property effect checks | `V$PROPERTY` plus the related performance view, such as `V$SQL_PLAN_CACHE`, `V$TIME_ZONE_NAMES`, `V$TEMPORARY_LOBS`, or replication views |
| Performance view inventory | `V$TABLE`, `V$ALLCOLUMN` |
| Tables, views, sequences, queues | `SYSTEM_.SYS_TABLES_` |
| Synonyms | `SYSTEM_.SYS_SYNONYMS_` |
| Materialized views | `SYSTEM_.SYS_MATERIALIZED_VIEWS_`, `SYSTEM_.SYS_TABLES_`, `SYSTEM_.SYS_VIEWS_` |
| Directories and jobs | `SYSTEM_.SYS_DIRECTORIES_`, `SYSTEM_.SYS_JOBS_` |
| Columns | `SYSTEM_.SYS_COLUMNS_` |
| Data type lookup | `V$DATATYPE` |
| Comments | `SYSTEM_.SYS_COMMENTS_` |
| Table size | `SYSTEM_.SYS_TABLE_SIZE_`, `V$USAGE` |
| Partitions | `SYSTEM_.SYS_TABLE_PARTITIONS_`, `SYSTEM_.SYS_PART_TABLES_`, `SYSTEM_.SYS_PART_KEY_COLUMNS_` |
| Indexes | `SYSTEM_.SYS_INDICES_`, `SYSTEM_.SYS_INDEX_COLUMNS_`, `V$INDEX` |
| Constraints | `SYSTEM_.SYS_CONSTRAINTS_`, `SYSTEM_.SYS_CONSTRAINT_COLUMNS_` |
| Users and roles | `SYSTEM_.SYS_USERS_`, `SYSTEM_.DBA_USERS_`, `SYSTEM_.SYS_USER_ROLES_` |
| Privileges | `SYSTEM_.SYS_PRIVILEGES_`, `SYSTEM_.SYS_GRANT_SYSTEM_`, `SYSTEM_.SYS_GRANT_OBJECT_` |
| Trigger metadata | `SYSTEM_.SYS_TRIGGERS_`, `SYSTEM_.SYS_TRIGGER_STRINGS_`, `SYSTEM_.SYS_TRIGGER_DML_TABLES_`, `SYSTEM_.SYS_TRIGGER_UPDATE_COLUMNS_` |
| Memory database identity and size | `V$DATABASE` |
| Tablespaces and datafiles | `V$TABLESPACES`, `V$DATAFILES`, `V$MEM_TABLESPACES`, `V$VOL_TABLESPACES`, `V$MEM_TABLESPACE_STATUS_DESC` |
| Memory checkpoint files and paths | `V$MEM_TABLESPACE_CHECKPOINT_PATHS`, `V$STABLE_MEM_DATAFILES`, `V$MEM_STABLE` for Altibase 8.1 verified source |
| Sessions | `V$SESSION`, `V$INTERNAL_SESSION`, `V$SESSIONMGR` |
| SQL text and statements | `V$STATEMENT`, `V$SQLTEXT` |
| Waits and locks | `V$SESSION_WAIT`, `V$SESSION_WAIT_CLASS`, `V$LOCK`, `V$LOCK_WAIT`, `V$LOCK_STATEMENT` |
| Transactions | `V$TRANSACTION`, `V$TRANSACTION_MGR`, `V$DBA_2PC_PENDING` |
| Plan cache | `V$SQL_PLAN_CACHE`, `V$SQL_PLAN_CACHE_PCO`, `V$SQL_PLAN_CACHE_SQLTEXT` |
| System and session counters | `V$STATNAME`, `V$SYSSTAT`, `V$SESSTAT` |
| Memory module usage | `V$MEMSTAT` |
| Buffer pool statistics | `V$BUFFPOOL_STAT` |
| Statistics | `V$DBMS_STATS`, `V$LOCK_TABLE_STATS`, `V$USAGE` |
| Replication definition | `SYSTEM_.SYS_REPLICATIONS_`, `SYSTEM_.SYS_REPL_HOSTS_`, `SYSTEM_.SYS_REPL_ITEMS_` |
| Replication runtime | `V$REPEXEC`, `V$REPGAP`, `V$REPGAP_PARALLEL`, `V$REPSENDER`, `V$REPRECEIVER` |
| Database links | `SYSTEM_.SYS_DATABASE_LINKS_`, `V$DBLINK_*` |
| Backup, archive, log, recovery | `V$LOG`, `V$LFG`, `V$ARCHIVE`, `V$BACKUP_INFO`, `V$OBSOLETE_BACKUP_INFO`, `V$DATAFILES` |
| Disk file I/O hotspots | `V$FILESTAT`, `V$DATAFILES`, `V$TABLESPACES` |
| Snapshot and trace log state | `V$SNAPSHOT`, `V$TRACELOG` |
| Temporary LOB in 8.1 | `V$TEMPORARY_LOBS`, `V$PROPERTY` |

## Cookbook: Version, Properties, and View Availability

### Check Server Version and Metadata Version

```sql
SELECT product_version,
       meta_version,
       protocol_version,
       repl_protocol_version
FROM V$VERSION;
```

Use `META_VERSION` when an upgrade, migration, or metadata compatibility question is involved.

### Check Properties

```sql
SELECT name,
       storedcount,
       attr,
       min,
       max,
       value1,
       value2,
       value3,
       value4,
       value5,
       value6,
       value7,
       value8
FROM V$PROPERTY
WHERE name IN (
  '<PROPERTY_NAME_1>',
  '<PROPERTY_NAME_2>'
)
ORDER BY name;
```

`STOREDCOUNT` is the number of configured values for the property. Multi-value properties can use `VALUE1` through `VALUE8`.

For multi-value path properties:

```sql
SELECT name,
       storedcount,
       value1,
       value2,
       value3,
       value4,
       value5,
       value6,
       value7,
       value8
FROM V$PROPERTY
WHERE name IN ('MEM_DB_DIR', 'LOGANCHOR_DIR')
ORDER BY name;
```

For dynamic property change checks, always query before and after the change in the same session or maintenance window:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name = 'QUERY_TIMEOUT';

ALTER SESSION SET QUERY_TIMEOUT = 120;

SELECT name, value1
FROM V$PROPERTY
WHERE name = 'QUERY_TIMEOUT';

SELECT query_time_limit
FROM V$SESSION
WHERE id = SESSION_ID();
```

For 8.1 Temporary LOB checks:

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

### Verify Property Effects with System Views

Use this when the user asks whether a property change is active or whether the running system reflects the configured value.

SQL plan cache:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name = 'SQL_PLAN_CACHE_SIZE';

SELECT max_cache_size,
       current_cache_size,
       current_cache_obj_count,
       cache_hit_count,
       cache_miss_count
FROM V$SQL_PLAN_CACHE;
```

Time zone:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'TIME_ZONE';

SELECT name, utc_offset
FROM V$TIME_ZONE_NAMES
WHERE name = 'Asia/Seoul';

SELECT time_zone
FROM V$SESSION
WHERE id = SESSION_ID();
```

Replication ports:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name IN ('REPLICATION_PORT_NO', 'REPLICATION_SSL_PORT_NO')
ORDER BY name;

SELECT port, max_sender_count, max_receiver_count
FROM V$REPEXEC;
```

Storage defaults used by generated DDL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name IN (
  'USER_DATA_FILE_INIT_SIZE',
  'USER_DATA_FILE_NEXT_SIZE',
  'USER_DATA_FILE_MAX_SIZE',
  'USER_TEMP_FILE_INIT_SIZE',
  'USER_TEMP_FILE_NEXT_SIZE',
  'USER_TEMP_FILE_MAX_SIZE',
  'MEM_MAX_DB_SIZE',
  'VOLATILE_MAX_DB_SIZE'
)
ORDER BY name;

SELECT id, name, type, state, datafile_count, total_page_count, page_size
FROM V$TABLESPACES
ORDER BY id;
```

Property and system-view matrix:

| Question | Property check | Related view check |
| --- | --- | --- |
| What value is configured? | `V$PROPERTY` | Usually none |
| Is a performance-view query portable? | `V$TABLE` | `V$ALLCOLUMN` |
| Did `SQL_PLAN_CACHE_SIZE` take effect? | `V$PROPERTY` | `V$SQL_PLAN_CACHE` |
| Is `TIME_ZONE` value valid? | `V$PROPERTY` | `V$TIME_ZONE_NAMES` |
| Is Temporary LOB enabled and used in 8.1? | `V$PROPERTY` | `V$TEMPORARY_LOBS` |
| Which replication port is configured? | `V$PROPERTY` | `V$REPEXEC`, `V$REPGAP`, `V$REPSENDER`, `V$REPRECEIVER` |
| Which storage default affects DDL? | `V$PROPERTY` | `V$TABLESPACES`, `V$DATAFILES`, `V$MEM_TABLESPACES`, `V$VOL_TABLESPACES` |

### Check Whether a Performance View or Column Exists

```sql
SELECT name, columncount
FROM V$TABLE
WHERE name = '<VIEW_NAME>';

SELECT tablename, colname
FROM V$ALLCOLUMN
WHERE tablename = '<VIEW_NAME>'
ORDER BY colname;
```

## Cookbook: Objects, Columns, Comments, and Sequences

### List Objects Owned by a User

```sql
SELECT u.user_name,
       t.table_name,
       t.table_type,
       t.tbs_name,
       t.column_count,
       t.is_partitioned,
       t.temporary,
       t.access,
       t.created,
       t.last_ddl_time
FROM SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_USERS_ u
WHERE t.user_id = u.user_id
  AND u.user_name = '<OWNER_NAME>'
ORDER BY t.table_type, t.table_name;
```

`TABLE_TYPE` common values: `T` table, `S` sequence, `V` view, `Q` queue, `M` materialized-view maintenance table, `A` materialized-view maintenance view, `G` global-index internal table, `D` compressed-column dictionary table.

### Check One Table, View, Sequence, or Queue

```sql
SELECT u.user_name,
       t.table_id,
       t.table_oid,
       t.table_name,
       t.table_type,
       t.tbs_name,
       t.column_count,
       t.maxrow,
       t.is_partitioned,
       t.temporary,
       t.hidden,
       t.access,
       t.created,
       t.last_ddl_time
FROM SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_USERS_ u
WHERE t.user_id = u.user_id
  AND u.user_name = '<OWNER_NAME>'
  AND t.table_name = '<TABLE_NAME>';
```

### List Columns for a Table or View

```sql
SELECT c.column_order,
       c.column_name,
       c.data_type,
       c.precision,
       c.scale,
       c.is_nullable,
       c.default_val,
       c.store_type,
       c.in_row_size,
       c.is_hidden,
       c.is_key_preserved
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

`STORE_TYPE` common values: `V` variable, `F` fixed, `L` LOB column. `IS_NULLABLE`, `IS_HIDDEN`, and `IS_KEY_PRESERVED` use true/false style flags in the dictionary.

### Look Up Data Type Codes

```sql
SELECT type_name,
       data_type,
       column_size,
       create_param,
       nullable,
       searchable
FROM V$DATATYPE
ORDER BY type_name;
```

Use this to interpret `SYSTEM_.SYS_COLUMNS_.DATA_TYPE`. If duplicate `DATA_TYPE` values appear for aliases, present both aliases rather than hiding one.

### Check Comments

```sql
SELECT user_name,
       table_name,
       column_name,
       comments
FROM SYSTEM_.SYS_COMMENTS_
WHERE user_name = '<OWNER_NAME>'
  AND table_name = '<TABLE_NAME>'
ORDER BY column_name;
```

`COLUMN_NAME` is `NULL` for a table-level or view-level comment.

### Check a Sequence

```sql
SELECT u.user_name,
       t.table_name AS sequence_name,
       s.current_seq,
       s.start_seq,
       s.increment_seq,
       s.cache_size,
       s.min_seq,
       s.max_seq,
       s.is_cycle
FROM SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_USERS_ u,
     V$SEQ s
WHERE t.user_id = u.user_id
  AND t.table_oid = s.seq_oid
  AND t.table_type = 'S'
  AND u.user_name = '<OWNER_NAME>'
  AND t.table_name = '<SEQUENCE_NAME>';
```

### Check Synonyms

```sql
SELECT owner.user_name AS synonym_owner,
       s.synonym_name,
       s.object_owner_name,
       s.object_name,
       s.created,
       s.last_ddl_time
FROM SYSTEM_.SYS_SYNONYMS_ s,
     SYSTEM_.SYS_USERS_ owner
WHERE s.synonym_owner_id = owner.user_id
  AND owner.user_name = '<OWNER_NAME>'
ORDER BY owner.user_name, s.synonym_name;
```

`SYSTEM_.SYS_SYNONYMS_` stores the alias owner, alias name, target owner, and target object name. Privileges are checked against the target object, not the synonym row.

### Check Directory Objects

```sql
SELECT directory_id,
       user_id,
       directory_name,
       directory_path,
       created,
       last_ddl_time
FROM SYSTEM_.SYS_DIRECTORIES_
WHERE directory_name = '<DIRECTORY_NAME>';
```

Directory objects are database metadata for PSM file access. The corresponding operating-system directory must still exist on disk, and directory object privileges are visible through `SYSTEM_.SYS_GRANT_OBJECT_` with `OBJ_TYPE = 'D'`.

```sql
SELECT grantee.user_name AS grantee_name,
       p.priv_name,
       d.directory_name,
       g.with_grant_option
FROM SYSTEM_.SYS_GRANT_OBJECT_ g,
     SYSTEM_.SYS_USERS_ grantee,
     SYSTEM_.SYS_PRIVILEGES_ p,
     SYSTEM_.SYS_DIRECTORIES_ d
WHERE g.grantee_id = grantee.user_id
  AND g.priv_id = p.priv_id
  AND g.obj_id = d.directory_id
  AND g.obj_type = 'D'
  AND d.directory_name = '<DIRECTORY_NAME>'
ORDER BY grantee.user_name, p.priv_name;
```

For directory grants to `PUBLIC`, `GRANTEE_ID` is `0` and does not join to `SYSTEM_.SYS_USERS_`.

### Check Scheduler Jobs

```sql
SELECT job_id,
       job_name,
       exec_query,
       start_time,
       end_time,
       interval,
       interval_type,
       state,
       last_exec_time,
       exec_count,
       error_code,
       is_enable,
       comment
FROM SYSTEM_.SYS_JOBS_
WHERE job_name = '<JOB_NAME>';
```

`STATE` shows whether a job is running, `IS_ENABLE` shows whether the scheduler may execute it, and `ERROR_CODE` records the last execution error when one exists.

## Cookbook: Indexes and Constraints

### List Indexes on a Table

```sql
SELECT u.user_name,
       t.table_name,
       i.index_name,
       i.index_id,
       i.index_type,
       i.is_unique,
       i.column_cnt,
       i.is_range,
       i.is_pers,
       i.is_directkey,
       i.tbs_id,
       i.is_partitioned,
       i.created,
       i.last_ddl_time
FROM SYSTEM_.SYS_INDICES_ i,
     SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_USERS_ u
WHERE i.user_id = t.user_id
  AND i.table_id = t.table_id
  AND t.user_id = u.user_id
  AND u.user_name = '<OWNER_NAME>'
  AND t.table_name = '<TABLE_NAME>'
ORDER BY i.index_name;
```

`INDEX_TYPE` values include `1` for B-tree and `2` for R-tree. `IS_UNIQUE`, `IS_RANGE`, `IS_DIRECTKEY`, and `IS_PARTITIONED` are flags.

### List Index Columns

```sql
SELECT i.index_name,
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
ORDER BY i.index_name, ic.index_col_order;
```

`SORT_ORDER` values are `A` ascending and `D` descending.

### List Constraints on a Table

```sql
SELECT u.user_name,
       t.table_name,
       cs.constraint_name,
       cs.constraint_type,
       cs.index_id,
       cs.column_cnt,
       cs.referenced_table_id,
       cs.referenced_index_id,
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

`CONSTRAINT_TYPE` values: `0` foreign key, `1` not null, `2` unique, `3` primary key, `5` timestamp, `6` local unique, `7` check.

### List Constraint Columns

```sql
SELECT cs.constraint_name,
       cs.constraint_type,
       cc.constraint_col_order,
       c.column_name
FROM SYSTEM_.SYS_CONSTRAINTS_ cs,
     SYSTEM_.SYS_CONSTRAINT_COLUMNS_ cc,
     SYSTEM_.SYS_COLUMNS_ c,
     SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_USERS_ u
WHERE cs.user_id = cc.user_id
  AND cs.table_id = cc.table_id
  AND cs.constraint_id = cc.constraint_id
  AND cc.user_id = c.user_id
  AND cc.table_id = c.table_id
  AND cc.column_id = c.column_id
  AND cs.user_id = t.user_id
  AND cs.table_id = t.table_id
  AND t.user_id = u.user_id
  AND u.user_name = '<OWNER_NAME>'
  AND t.table_name = '<TABLE_NAME>'
ORDER BY cs.constraint_name, cc.constraint_col_order;
```

### List Foreign Key Targets

```sql
SELECT cs.constraint_name,
       u.user_name AS local_owner,
       t.table_name AS local_table,
       ru.user_name AS referenced_owner,
       rt.table_name AS referenced_table,
       cs.delete_rule,
       cs.validated
FROM SYSTEM_.SYS_CONSTRAINTS_ cs,
     SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_USERS_ u,
     SYSTEM_.SYS_TABLES_ rt,
     SYSTEM_.SYS_USERS_ ru
WHERE cs.user_id = t.user_id
  AND cs.table_id = t.table_id
  AND t.user_id = u.user_id
  AND cs.referenced_table_id = rt.table_id
  AND rt.user_id = ru.user_id
  AND cs.constraint_type = 0
  AND u.user_name = '<OWNER_NAME>'
  AND t.table_name = '<TABLE_NAME>'
ORDER BY cs.constraint_name;
```

`DELETE_RULE` values include `0` no cascade, `1` cascade delete, and `2` set null.

## Cookbook: Partitions, Tablespaces, and Space Usage

### List Table Partitions

```sql
SELECT p.partition_name,
       p.partition_min_value,
       p.partition_max_value,
       p.partition_order,
       p.tbs_id,
       p.partition_access,
       p.replication_count,
       p.replication_recovery_count,
       p.created,
       p.last_ddl_time
FROM SYSTEM_.SYS_TABLE_PARTITIONS_ p,
     SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_USERS_ u
WHERE p.user_id = t.user_id
  AND p.table_id = t.table_id
  AND t.user_id = u.user_id
  AND u.user_name = '<OWNER_NAME>'
  AND t.table_name = '<TABLE_NAME>'
ORDER BY p.partition_order, p.partition_name;
```

`PARTITION_ACCESS` values: `R` read-only, `W` read/write, `A` read/append.

### List Partition Keys

```sql
SELECT pk.object_type,
       pk.part_col_order,
       c.column_name
FROM SYSTEM_.SYS_PART_KEY_COLUMNS_ pk,
     SYSTEM_.SYS_PART_TABLES_ pt,
     SYSTEM_.SYS_COLUMNS_ c,
     SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_USERS_ u
WHERE pk.user_id = pt.user_id
  AND pk.partition_obj_id = pt.table_id
  AND pk.object_type = 0
  AND pt.user_id = t.user_id
  AND pt.table_id = t.table_id
  AND pk.user_id = c.user_id
  AND pt.table_id = c.table_id
  AND pk.column_id = c.column_id
  AND t.user_id = u.user_id
  AND u.user_name = '<OWNER_NAME>'
  AND t.table_name = '<TABLE_NAME>'
ORDER BY pk.part_col_order;
```

### Check Table Size from the Dictionary

```sql
SELECT user_name,
       table_name,
       tbs_name,
       memory_size,
       disk_size
FROM SYSTEM_.SYS_TABLE_SIZE_
WHERE user_name = '<OWNER_NAME>'
  AND table_name = '<TABLE_NAME>';
```

### Check Object Space Usage from Statistics

`V$USAGE` depends on DBMS statistics collection. If results look stale, gather the relevant statistics first.

```sql
SELECT u.user_name,
       t.table_name,
       v.meta_space,
       v.used_space,
       v.ageable_space,
       v.free_space
FROM V$USAGE v,
     SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_USERS_ u
WHERE v.type = 'T'
  AND v.target_id = t.table_oid
  AND t.user_id = u.user_id
  AND u.user_name = '<OWNER_NAME>'
  AND t.table_name = '<TABLE_NAME>';
```

### List Tablespaces

```sql
SELECT id,
       name,
       type,
       state,
       extent_management,
       segment_management,
       datafile_count,
       total_page_count,
       allocated_page_count,
       page_size,
       total_page_count * page_size AS total_bytes,
       allocated_page_count * page_size AS allocated_bytes,
       attr_log_compress
FROM V$TABLESPACES
ORDER BY id;
```

`TYPE` values include memory system dictionary, memory system data, memory user data, disk system data, disk user data, disk temporary, disk undo, and volatile user data. `STATE` values include online, offline, backup, dropped, and discarded states.

Use these source-backed code meanings when explaining `V$TABLESPACES` output:

- `TYPE`: `0` memory system dictionary, `1` memory system data, `2` memory user data, `3` disk system data, `4` disk user data, `5` disk system temporary, `6` disk user temporary, `7` disk system undo, `8` volatile user data.
- `STATE`: `1` offline, `2` online, `5` offline tablespace being backed up, `6` online tablespace being backed up, `128` dropped, `1024` discarded, `1028` discarded tablespace being backed up.
- `ATTR_LOG_COMPRESS`: `0` means DML on tables in the tablespace is not log-compressed; `1` means it is log-compressed.

### List Datafiles

```sql
SELECT d.id,
       d.name,
       d.spaceid,
       t.name AS tablespace_name,
       t.page_size,
       d.initsize AS initsize_pages,
       d.initsize * t.page_size AS initsize_bytes,
       d.initsize * t.page_size / 1048576 AS initsize_mb,
       d.currsize AS currsize_pages,
       d.currsize * t.page_size AS currsize_bytes,
       d.currsize * t.page_size / 1048576 AS currsize_mb,
       d.nextsize AS nextsize_pages,
       d.nextsize * t.page_size AS nextsize_bytes,
       d.nextsize * t.page_size / 1048576 AS nextsize_mb,
       d.maxsize AS maxsize_pages,
       d.maxsize * t.page_size AS maxsize_bytes,
       d.maxsize * t.page_size / 1048576 AS maxsize_mb,
       d.autoextend,
       d.opened,
       d.modified,
       d.state,
       d.max_open_fd_count,
       d.cur_open_fd_count
FROM V$DATAFILES d,
     V$TABLESPACES t
WHERE d.spaceid = t.id
ORDER BY d.spaceid, d.id;
```

`V$DATAFILES.INITSIZE`, `CURRSIZE`, `NEXTSIZE`, and `MAXSIZE` are page counts. Use the `PAGE_SIZE`-derived byte or MB aliases for capacity and autoextend decisions.

### Check Memory Tablespaces

```sql
SELECT m.space_id,
       m.space_name,
       m.space_status,
       s.status_desc,
       m.autoextend_mode,
       m.autoextend_nextsize,
       m.maxsize,
       m.current_size,
       m.alloc_page_count,
       m.free_page_count,
       m.current_db,
       m.high_limit_page,
       m.page_count_per_file,
       m.page_count_in_disk
FROM V$MEM_TABLESPACES m,
     V$MEM_TABLESPACE_STATUS_DESC s
WHERE m.space_status = s.status
ORDER BY m.space_id;
```

`AUTOEXTEND_MODE = 1` means memory tablespace autoextend is enabled. `CURRENT_DB` is the ping-pong checkpoint file group for pair checkpoint scale; in 8.1 single checkpoint scale it can be `-1`, and `V$MEM_STABLE` holds the stable image ping-pong value per file.

### Check Memory Tablespace Checkpoint Paths

```sql
SELECT m.space_id,
       m.space_name,
       p.checkpoint_path
FROM V$MEM_TABLESPACES m,
     V$MEM_TABLESPACE_CHECKPOINT_PATHS p
WHERE m.space_id = p.space_id
ORDER BY m.space_id, p.checkpoint_path;
```

Use this before changing checkpoint-path DDL or diagnosing missing memory database image files.

### Check Volatile Tablespaces

```sql
SELECT v.space_id,
       v.space_name,
       v.space_status,
       s.status_desc,
       v.init_size,
       v.autoextend_mode,
       v.next_size,
       v.max_size,
       v.current_size,
       v.alloc_page_count,
       v.free_page_count
FROM V$VOL_TABLESPACES v,
     V$MEM_TABLESPACE_STATUS_DESC s
WHERE v.space_status = s.status
ORDER BY v.space_id;
```

Volatile tablespaces exist in memory and use the same status-description view as memory tablespaces.

### Check Stable Memory Datafile Paths

```sql
SELECT mem_data_file
FROM V$STABLE_MEM_DATAFILES
ORDER BY mem_data_file;
```

This view lists the full paths of stable memory data files known to the database.

### Check 8.1 Stable Checkpoint Image Files

Use this when `V$LOG.CHECKPOINT_SCALE` is `SINGLE`, or when investigating memory checkpoint image file state in 8.1.

```sql
SELECT tablename, colname
FROM V$ALLCOLUMN
WHERE tablename IN ('V$LOG', 'V$MEM_STABLE')
  AND colname IN ('CHECKPOINT_SCALE', 'SPACE_ID', 'FILE_NUM', 'CURRENT_DB')
ORDER BY tablename, colname;

SELECT checkpoint_scale
FROM V$LOG;

SELECT space_id,
       space_name,
       file_num,
       current_db
FROM V$MEM_STABLE
ORDER BY space_id, file_num;
```

## Cookbook: Users, Roles, and Privileges

### List Users and Roles

```sql
SELECT user_id,
       user_name,
       default_tbs_id,
       temp_tbs_id,
       account_lock,
       password_limit_flag,
       failed_login_count,
       password_expiry_date,
       user_type,
       disable_tcp,
       created,
       last_ddl_time
FROM SYSTEM_.SYS_USERS_
ORDER BY user_type, user_name;
```

`USER_TYPE` values are `U` user and `R` role. `ACCOUNT_LOCK` values include `N` unlocked and `L` locked. `DISABLE_TCP` shows whether TCP is disabled for the account.

`SYSTEM_.DBA_USERS_` contains user information visible only to `SYS`.

### Check System Privileges for a User

```sql
SELECT grantee.user_name AS grantee_name,
       p.priv_name,
       grantor.user_name AS grantor_name
FROM SYSTEM_.SYS_GRANT_SYSTEM_ g,
     SYSTEM_.SYS_USERS_ grantee,
     SYSTEM_.SYS_USERS_ grantor,
     SYSTEM_.SYS_PRIVILEGES_ p
WHERE g.grantee_id = grantee.user_id
  AND g.grantor_id = grantor.user_id
  AND g.priv_id = p.priv_id
  AND grantee.user_name = '<USER_NAME>'
ORDER BY p.priv_name;
```

### Check Object Privileges on Tables, Views, or Sequences

```sql
SELECT grantee.user_name AS grantee_name,
       p.priv_name,
       owner.user_name AS object_owner,
       t.table_name AS object_name,
       g.obj_type,
       g.with_grant_option
FROM SYSTEM_.SYS_GRANT_OBJECT_ g,
     SYSTEM_.SYS_USERS_ grantee,
     SYSTEM_.SYS_USERS_ owner,
     SYSTEM_.SYS_PRIVILEGES_ p,
     SYSTEM_.SYS_TABLES_ t
WHERE g.grantee_id = grantee.user_id
  AND g.user_id = owner.user_id
  AND g.priv_id = p.priv_id
  AND g.user_id = t.user_id
  AND g.obj_id = t.table_id
  AND owner.user_name = '<OWNER_NAME>'
  AND t.table_name = '<OBJECT_NAME>'
ORDER BY grantee.user_name, p.priv_name;
```

For grants to `PUBLIC`, `GRANTEE_ID` is `0` and does not join to `SYSTEM_.SYS_USERS_`:

```sql
SELECT p.priv_name,
       owner.user_name AS object_owner,
       t.table_name AS object_name,
       g.obj_type,
       g.with_grant_option
FROM SYSTEM_.SYS_GRANT_OBJECT_ g,
     SYSTEM_.SYS_USERS_ owner,
     SYSTEM_.SYS_PRIVILEGES_ p,
     SYSTEM_.SYS_TABLES_ t
WHERE g.grantee_id = 0
  AND g.user_id = owner.user_id
  AND g.priv_id = p.priv_id
  AND g.user_id = t.user_id
  AND g.obj_id = t.table_id
ORDER BY owner.user_name, t.table_name, p.priv_name;
```

`OBJ_TYPE` common values: `T` table or view, `S` sequence, `P` stored procedure or function, `A` package, `D` directory, `Y` library.

### Check Role Grants

```sql
SELECT grantee.user_name AS grantee_name,
       role_user.user_name AS role_name
FROM SYSTEM_.SYS_USER_ROLES_ r,
     SYSTEM_.SYS_USERS_ grantee,
     SYSTEM_.SYS_USERS_ role_user
WHERE r.grantee_id = grantee.user_id
  AND r.role_id = role_user.user_id
ORDER BY grantee.user_name, role_user.user_name;
```

### Check Tablespace Access by User

```sql
SELECT u.user_name,
       tu.tbs_id,
       tu.is_access
FROM SYSTEM_.SYS_TBS_USERS_ tu,
     SYSTEM_.SYS_USERS_ u
WHERE tu.user_id = u.user_id
  AND u.user_name = '<USER_NAME>'
ORDER BY tu.tbs_id;
```

`IS_ACCESS` values are `0` access not permitted and `1` access permitted.

## Cookbook: Views, Procedures, Packages, and Triggers

### Check View Status

```sql
SELECT u.user_name,
       t.table_name AS view_name,
       v.status,
       v.read_only
FROM SYSTEM_.SYS_VIEWS_ v,
     SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_USERS_ u
WHERE v.user_id = t.user_id
  AND v.view_id = t.table_id
  AND t.user_id = u.user_id
  AND u.user_name = '<OWNER_NAME>'
ORDER BY t.table_name;
```

`STATUS` values are `0` valid and `1` invalid.

### Retrieve View Source Fragments

```sql
SELECT vp.seq_no,
       vp.parse
FROM SYSTEM_.SYS_VIEW_PARSE_ vp,
     SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_USERS_ u
WHERE vp.user_id = t.user_id
  AND vp.view_id = t.table_id
  AND t.user_id = u.user_id
  AND u.user_name = '<OWNER_NAME>'
  AND t.table_name = '<VIEW_NAME>'
ORDER BY vp.seq_no;
```

Concatenate `PARSE` values in `SEQ_NO` order in the client if a complete source string is needed.

### Check Materialized Views

```sql
SELECT u.user_name,
       m.mview_name,
       m.table_id,
       m.view_id,
       m.refresh_type,
       m.refresh_time,
       m.created,
       m.last_ddl_time,
       m.last_refresh_time
FROM SYSTEM_.SYS_MATERIALIZED_VIEWS_ m,
     SYSTEM_.SYS_USERS_ u
WHERE m.user_id = u.user_id
  AND u.user_name = '<OWNER_NAME>'
ORDER BY m.mview_name;
```

`REFRESH_TYPE` values include `C` complete, `F` fast, and `R` force. `REFRESH_TIME` values include `D` on demand and `C` on commit. Source SQL Reference notes that Altibase currently does not support fast refresh, on-commit refresh, or never-refresh materialized views; check the DDL before assuming those codes can be produced for a new materialized view.

To inspect the internal maintenance objects for one materialized view:

```sql
SELECT m.mview_name,
       mt.table_name AS maintenance_table,
       mv.table_name AS maintenance_view
FROM SYSTEM_.SYS_MATERIALIZED_VIEWS_ m,
     SYSTEM_.SYS_TABLES_ mt,
     SYSTEM_.SYS_TABLES_ mv,
     SYSTEM_.SYS_USERS_ u
WHERE m.user_id = u.user_id
  AND m.user_id = mt.user_id
  AND m.table_id = mt.table_id
  AND m.user_id = mv.user_id
  AND m.view_id = mv.table_id
  AND u.user_name = '<OWNER_NAME>'
  AND m.mview_name = '<MVIEW_NAME>';
```

### Check Invalid Stored Procedures and Functions

```sql
SELECT u.user_name,
       p.proc_name,
       p.object_type,
       p.status,
       p.authid,
       p.para_num,
       p.created,
       p.last_ddl_time
FROM SYSTEM_.SYS_PROCEDURES_ p,
     SYSTEM_.SYS_USERS_ u
WHERE p.user_id = u.user_id
  AND p.status = 1
ORDER BY u.user_name, p.proc_name;
```

`OBJECT_TYPE` values include `0` procedure, `1` function, and `3` type set. `STATUS` values are `0` valid and `1` invalid.

### Check Procedure Parameters

```sql
SELECT u.user_name,
       p.proc_name,
       pp.para_order,
       pp.para_name,
       pp.inout_type,
       pp.data_type,
       pp.size,
       pp.precision,
       pp.scale,
       pp.default_val
FROM SYSTEM_.SYS_PROC_PARAS_ pp,
     SYSTEM_.SYS_PROCEDURES_ p,
     SYSTEM_.SYS_USERS_ u
WHERE pp.user_id = p.user_id
  AND pp.proc_oid = p.proc_oid
  AND p.user_id = u.user_id
  AND u.user_name = '<OWNER_NAME>'
  AND p.proc_name = '<PROC_NAME>'
ORDER BY pp.para_order;
```

`INOUT_TYPE` values are `0` IN, `1` OUT, and `2` IN OUT.

### Retrieve Procedure Source Fragments

```sql
SELECT pp.seq_no,
       pp.parse
FROM SYSTEM_.SYS_PROC_PARSE_ pp,
     SYSTEM_.SYS_PROCEDURES_ p,
     SYSTEM_.SYS_USERS_ u
WHERE pp.user_id = p.user_id
  AND pp.proc_oid = p.proc_oid
  AND p.user_id = u.user_id
  AND u.user_name = '<OWNER_NAME>'
  AND p.proc_name = '<PROC_NAME>'
ORDER BY pp.seq_no;
```

### Check Dependencies of a Procedure, Package, or View

```sql
SELECT u.user_name,
       p.proc_name,
       dep.related_object_name,
       dep.related_object_type
FROM SYSTEM_.SYS_PROC_RELATED_ dep,
     SYSTEM_.SYS_PROCEDURES_ p,
     SYSTEM_.SYS_USERS_ u
WHERE dep.user_id = p.user_id
  AND dep.proc_oid = p.proc_oid
  AND p.user_id = u.user_id
  AND u.user_name = '<OWNER_NAME>'
  AND p.proc_name = '<PROC_NAME>'
ORDER BY dep.related_object_type, dep.related_object_name;

SELECT u.user_name,
       pkg.package_name,
       dep.related_object_name,
       dep.related_object_type
FROM SYSTEM_.SYS_PACKAGE_RELATED_ dep,
     SYSTEM_.SYS_PACKAGES_ pkg,
     SYSTEM_.SYS_USERS_ u
WHERE dep.user_id = pkg.user_id
  AND dep.package_oid = pkg.package_oid
  AND pkg.user_id = u.user_id
  AND u.user_name = '<OWNER_NAME>'
  AND pkg.package_name = '<PACKAGE_NAME>'
ORDER BY dep.related_object_type, dep.related_object_name;

SELECT u.user_name,
       t.table_name AS view_name,
       dep.related_object_name,
       dep.related_object_type
FROM SYSTEM_.SYS_VIEW_RELATED_ dep,
     SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_USERS_ u
WHERE dep.user_id = t.user_id
  AND dep.view_id = t.table_id
  AND t.user_id = u.user_id
  AND u.user_name = '<OWNER_NAME>'
  AND t.table_name = '<VIEW_NAME>'
ORDER BY dep.related_object_type, dep.related_object_name;
```

### Check Triggers on a Table

```sql
SELECT tr.user_name,
       t.table_name,
       tr.trigger_name,
       tr.is_enable,
       tr.event_time,
       tr.event_type,
       tr.granularity,
       tr.update_column_cnt,
       tr.created,
       tr.last_ddl_time
FROM SYSTEM_.SYS_TRIGGERS_ tr,
     SYSTEM_.SYS_TABLES_ t
WHERE tr.table_id = t.table_id
  AND tr.user_name = '<OWNER_NAME>'
  AND t.table_name = '<TABLE_NAME>'
ORDER BY tr.trigger_name;
```

`IS_ENABLE` values are `0` disabled and `1` enabled. `EVENT_TIME` values include `1` before, `2` after, `3` instead of. `EVENT_TYPE` values include `1` insert, `2` delete, `4` update. `GRANULARITY` values include `1` for each row and `2` for each statement.

### Retrieve Trigger Source and Dependencies

```sql
SELECT ts.seqno,
       ts.substring
FROM SYSTEM_.SYS_TRIGGER_STRINGS_ ts,
     SYSTEM_.SYS_TRIGGERS_ tr
WHERE ts.table_id = tr.table_id
  AND ts.trigger_oid = tr.trigger_oid
  AND tr.user_name = '<OWNER_NAME>'
  AND tr.trigger_name = '<TRIGGER_NAME>'
ORDER BY ts.seqno;
```

Concatenate `SUBSTRING` values in `SEQNO` order in the client to reconstruct the trigger text.

```sql
SELECT base.table_name AS trigger_table,
       dml.table_name AS referenced_table,
       td.stmt_type
FROM SYSTEM_.SYS_TRIGGER_DML_TABLES_ td,
     SYSTEM_.SYS_TRIGGERS_ tr,
     SYSTEM_.SYS_TABLES_ base,
     SYSTEM_.SYS_TABLES_ dml
WHERE td.table_id = tr.table_id
  AND td.trigger_oid = tr.trigger_oid
  AND tr.table_id = base.table_id
  AND td.dml_table_id = dml.table_id
  AND tr.user_name = '<OWNER_NAME>'
  AND tr.trigger_name = '<TRIGGER_NAME>'
ORDER BY referenced_table, td.stmt_type;
```

`STMT_TYPE` values include `8` delete, `19` insert, and `33` update.

```sql
SELECT c.column_name
FROM SYSTEM_.SYS_TRIGGER_UPDATE_COLUMNS_ tuc,
     SYSTEM_.SYS_TRIGGERS_ tr,
     SYSTEM_.SYS_COLUMNS_ c
WHERE tuc.table_id = tr.table_id
  AND tuc.trigger_oid = tr.trigger_oid
  AND tuc.table_id = c.table_id
  AND tuc.column_id = c.column_id
  AND tr.user_name = '<OWNER_NAME>'
  AND tr.trigger_name = '<TRIGGER_NAME>'
ORDER BY c.column_name;
```

## Cookbook: Sessions, Statements, Waits, Locks, and Transactions

### List Current Sessions

```sql
SELECT id,
       trans_id,
       db_username,
       task_state,
       session_state,
       active_flag,
       opened_stmt_count,
       current_stmt_id,
       autocommit_flag,
       comm_name,
       client_app_info,
       module,
       action,
       login_time
FROM V$SESSION
ORDER BY id;
```

`TASK_STATE` values include `WAITING`, `READY`, `EXECUTING`, `QUEUE WAIT`, `QUEUE READY`, and `UNKNOWN`. `SESSION_STATE` values include `INIT`, `AUTH`, `SERVICE READY`, `SERVICE`, `END`, `ROLLBACK`, and `UNKNOWN`.

Use this triage join when a user asks "which session is running which SQL now":

```sql
SELECT s.id AS session_id,
       s.db_username,
       s.task_state,
       s.session_state,
       s.active_flag,
       s.trans_id,
       s.current_stmt_id,
       st.id AS stmt_id,
       st.execute_flag,
       st.execute_state,
       st.event,
       st.wait_time,
       st.total_time,
       st.query
FROM V$SESSION s,
     V$STATEMENT st
WHERE s.id = st.session_id
  AND s.current_stmt_id = st.id
ORDER BY s.active_flag DESC, st.total_time DESC, s.id;
```

If `V$SESSION.TRANS_ID = -1`, no transaction is currently underway for that session. If `ACTIVE_FLAG = 1`, the session is executing a statement; if it is `0`, the session is connected or has completed commit/rollback work.

### Find Active Statements and SQL Text

```sql
SELECT s.id AS session_id,
       s.db_username,
       s.task_state,
       st.id AS stmt_id,
       st.execute_state,
       st.fetch_state,
       st.execute_flag,
       st.total_time,
       st.execute_time,
       st.fetch_time,
       st.process_row,
       st.query
FROM V$SESSION s,
     V$STATEMENT st
WHERE s.id = st.session_id
  AND st.execute_flag = 1
ORDER BY st.total_time DESC;
```

`V$STATEMENT.EXECUTE_FLAG = 1` means the statement is currently executing. `V$STATEMENT.TOTAL_TIME`, `PARSE_TIME`, `VALIDATE_TIME`, `OPTIMIZE_TIME`, `EXECUTE_TIME`, and `FETCH_TIME` are in microseconds.

For SQL text fragments:

```sql
SELECT sid,
       stmt_id,
       piece,
       text
FROM V$SQLTEXT
WHERE sid = <SESSION_ID>
  AND stmt_id = <STMT_ID>
ORDER BY piece;
```

`V$SQLTEXT.TEXT` is stored in 64-byte fragments. Preserve `PIECE` order when presenting the full SQL text, and use `V$STATEMENT.QUERY` as the faster first check when the 16 KB statement text is sufficient.

To retrieve the current statement's fragments for one session:

```sql
SELECT x.sid,
       x.stmt_id,
       x.piece,
       x.text
FROM V$SESSION s,
     V$SQLTEXT x
WHERE s.id = x.sid
  AND s.current_stmt_id = x.stmt_id
  AND s.id = <SESSION_ID>
ORDER BY x.piece;
```

### Check Session Waits

```sql
SELECT sid,
       seqnum,
       event,
       wait_class,
       wait_time,
       second_in_wait,
       p1,
       p2,
       p3
FROM V$SESSION_WAIT
ORDER BY second_in_wait DESC, wait_time DESC;
```

Join current waits to session and statement context:

```sql
SELECT sw.sid AS session_id,
       s.db_username,
       s.task_state,
       s.current_stmt_id,
       sw.event,
       sw.wait_class,
       sw.wait_time,
       sw.second_in_wait,
       st.query
FROM V$SESSION_WAIT sw,
     V$SESSION s,
     V$STATEMENT st
WHERE sw.sid = s.id
  AND s.id = st.session_id
  AND s.current_stmt_id = st.id
ORDER BY sw.second_in_wait DESC, sw.wait_time DESC;
```

Use cumulative wait views to avoid overreacting to one instant:

```sql
SELECT sid,
       event,
       wait_class,
       total_waits,
       total_timeouts,
       time_waited,
       average_wait,
       max_wait
FROM V$SESSION_EVENT
WHERE sid = <SESSION_ID>
ORDER BY time_waited DESC, total_waits DESC;

SELECT wait_class,
       total_waits,
       time_waited
FROM V$SYSTEM_WAIT_CLASS
WHERE wait_class <> 'Idle'
ORDER BY time_waited DESC, total_waits DESC;
```

`V$WAIT_CLASS_NAME` maps wait class IDs to class names. Documented classes are `Other`, `Administrative`, `Configuration`, `Concurrency`, `Commit`, `Idle`, `User I/O`, `System I/O`, and `Replication`.

### Check Lock Wait Chains

```sql
SELECT trans_id,
       wait_for_trans_id
FROM V$LOCK_WAIT
ORDER BY wait_for_trans_id, trans_id;
```

Join lock holders or waiters to statements:

```sql
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

Join table locks to dictionary names:

```sql
SELECT l.lock_item_type,
       u.user_name,
       t.table_name,
       l.table_oid,
       l.trans_id,
       l.lock_desc,
       l.lock_cnt,
       l.is_grant
FROM V$LOCK l,
     SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_USERS_ u
WHERE l.table_oid = t.table_oid
  AND t.user_id = u.user_id
ORDER BY l.is_grant, u.user_name, t.table_name;
```

`IS_GRANT` indicates whether the lock is granted or waiting.

Map waiting and holder transactions back to sessions:

```sql
SELECT lw.trans_id AS waiting_trans_id,
       tw.session_id AS waiting_session_id,
       sw.db_username AS waiting_user,
       lw.wait_for_trans_id AS holder_trans_id,
       th.session_id AS holder_session_id,
       sh.db_username AS holder_user
FROM V$LOCK_WAIT lw,
     V$TRANSACTION tw,
     V$TRANSACTION th,
     V$SESSION sw,
     V$SESSION sh
WHERE lw.trans_id = tw.id
  AND lw.wait_for_trans_id = th.id
  AND tw.session_id = sw.id
  AND th.session_id = sh.id
ORDER BY holder_session_id, waiting_session_id;
```

Use `V$LOCK_STATEMENT` when the question is "which SQL is holding or waiting for a lock"; use `V$LOCK` when the question is "which object is locked." `V$LOCK.LOCK_ITEM_TYPE` values include `TBS`, `TBL`, `DBF`, and `UNKNOWN`.

### Check Transactions

```sql
SELECT id,
       session_id,
       status,
       update_status,
       log_type,
       xa_commit_status,
       ddl_flag,
       update_size,
       first_update_time,
       isolation_level
FROM V$TRANSACTION
ORDER BY id;
```

`STATUS` values include `0` begin, `1` precommit, `2` commit in memory, `3` commit, `4` abort, `5` blocked, and `6` end. `UPDATE_STATUS` values are `0` read-only and `1` updating. `DDL_FLAG` values are `0` non-DDL and `1` DDL.

Use the transaction-manager view for capacity and admission state:

```sql
SELECT total_count,
       free_list_count,
       begin_enable,
       active_count,
       sys_min_disk_viewscn
FROM V$TRANSACTION_MGR;
```

`BEGIN_ENABLE = 1` means new transactions can begin; `0` means transaction begin is disabled.

### Check Service Threads

```sql
SELECT id,
       type,
       state,
       run_mode,
       session_id,
       statement_id,
       execute_time,
       task_count,
       ready_task_count,
       thread_id
FROM V$SERVICE_THREAD
ORDER BY ready_task_count DESC, execute_time DESC, id;
```

Summarize service-thread pressure:

```sql
SELECT type,
       run_mode,
       state,
       COUNT(*) AS thread_count,
       SUM(task_count) AS task_count,
       SUM(ready_task_count) AS ready_task_count
FROM V$SERVICE_THREAD
GROUP BY type, run_mode, state
ORDER BY ready_task_count DESC, thread_count DESC;

SELECT add_thr_count,
       remove_thr_count
FROM V$SERVICE_THREAD_MGR;
```

`V$SERVICE_THREAD.READY_TASK_COUNT` is the number of sessions waiting for that service thread to process their requests. `V$SERVICE_THREAD_MGR` counts service-thread additions and removals since startup.

## Cookbook: Plan Cache and Optimizer Statistics

### Check SQL Plan Cache Summary

```sql
SELECT max_cache_size,
       current_hot_lru_size,
       current_cold_lru_size,
       current_cache_size,
       current_cache_obj_count,
       cache_hit_count,
       cache_miss_count,
       cache_in_fail_count,
       cache_out_count,
       cache_inserted_count,
       none_cache_sql_try_count
FROM V$SQL_PLAN_CACHE;
```

### Find Plan Cache SQL Text

```sql
SELECT sql_text_id,
       child_pco_count,
       child_pco_create_count,
       plan_cache_keep,
       sql_text
FROM V$SQL_PLAN_CACHE_SQLTEXT
WHERE sql_text LIKE '%<SQL_TEXT_FRAGMENT>%'
ORDER BY sql_text_id;
```

### Check Plan Cache Objects

```sql
SELECT sql_text_id,
       pco_id,
       create_reason,
       hit_count,
       rebuild_count,
       plan_state,
       lru_region,
       plan_size,
       fix_count,
       plan_cache_keep
FROM V$SQL_PLAN_CACHE_PCO
ORDER BY hit_count DESC, rebuild_count DESC;
```

### Check Collected Statistics

```sql
SELECT type,
       target_id,
       column_id,
       date,
       sample_size,
       num_row_change,
       num_row,
       num_page,
       num_dist,
       num_null,
       avg_len,
       used_space,
       free_space
FROM V$DBMS_STATS
ORDER BY type, target_id, column_id;
```

`TYPE` values: `S` system, `T` table, `I` index, `C` column.

### Check Table Statistics Lock Status

```sql
SELECT u.user_name,
       t.table_name,
       l.stat_locked
FROM V$LOCK_TABLE_STATS l,
     SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_USERS_ u
WHERE l.table_oid = t.table_oid
  AND t.user_id = u.user_id
ORDER BY u.user_name, t.table_name;
```

`STAT_LOCKED` values include `NONE` and `LOCKED`.

## Cookbook: Replication

### Check Replication Definitions

```sql
SELECT replication_name,
       is_started,
       xsn,
       item_count,
       conflict_resolution,
       repl_mode,
       role,
       options,
       invalid_recovery,
       parallel_applier_count,
       remote_xsn,
       remote_fault_detect_time,
       give_up_time,
       give_up_xsn
FROM SYSTEM_.SYS_REPLICATIONS_
ORDER BY replication_name;
```

`IS_STARTED` values are `0` suspended and `1` active. `REPL_MODE` values include `0` lazy and `2` eager. `OPTIONS` is a bit-style decimal flag: `1` recovery, `2` offline, `4` gapless, `8` parallel applier, `16` transaction grouping, `256` meta logging, and, on versions that expose it, `512` receive-only. On 7.1 systems, treat receive-only as 7.1.0.8.5 patch-level material and verify the exact patch/meta version plus observed metadata before decoding `512`, because earlier 7.1 dictionary layouts may not list the receive-only flag.

### Check Replication Hosts

```sql
SELECT replication_name,
       host_no,
       host_ip,
       port_no,
       conn_type,
       ib_latency
FROM SYSTEM_.SYS_REPL_HOSTS_
WHERE replication_name = '<REPLICATION_NAME>'
ORDER BY host_no;
```

### Check Replication Items

```sql
SELECT replication_name,
       local_user_name,
       local_table_name,
       local_partition_name,
       remote_user_name,
       remote_table_name,
       remote_partition_name,
       is_partition,
       replication_unit,
       invalid_max_sn
FROM SYSTEM_.SYS_REPL_ITEMS_
WHERE replication_name = '<REPLICATION_NAME>'
ORDER BY local_user_name, local_table_name, local_partition_name;
```

Use `IS_CONDITION_SYNCED` only after confirming the target version exposes that column. It is documented for 7.3 and 8.1, but not for the 7.1 `SYSTEM_.SYS_REPL_ITEMS_` layout.

```sql
SELECT c.column_name
FROM SYSTEM_.SYS_COLUMNS_ c,
     SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_USERS_ u
WHERE c.user_id = t.user_id
  AND c.table_id = t.table_id
  AND t.user_id = u.user_id
  AND u.user_name = 'SYSTEM_'
  AND t.table_name = 'SYS_REPL_ITEMS_'
  AND c.column_name = 'IS_CONDITION_SYNCED';
```

If the column exists on the target system:

```sql
SELECT replication_name,
       local_user_name,
       local_table_name,
       local_partition_name,
       remote_user_name,
       remote_table_name,
       remote_partition_name,
       is_partition,
       replication_unit,
       invalid_max_sn,
       is_condition_synced
FROM SYSTEM_.SYS_REPL_ITEMS_
WHERE replication_name = '<REPLICATION_NAME>'
ORDER BY local_user_name, local_table_name, local_partition_name;
```

### Check Replication Manager

```sql
SELECT port,
       max_sender_count,
       max_receiver_count
FROM V$REPEXEC;
```

### Check Replication Gap

```sql
SELECT rep_name,
       start_flag,
       rep_last_sn,
       rep_sn,
       rep_gap,
       rep_gap_size,
       read_file_no,
       read_offset
FROM V$REPGAP
ORDER BY rep_name;
```

For parallel replication:

```sql
SELECT rep_name,
       current_type,
       parallel_id,
       rep_last_sn,
       rep_sn,
       rep_gap,
       rep_gap_size,
       read_file_no,
       read_offset
FROM V$REPGAP_PARALLEL
ORDER BY rep_name, parallel_id;
```

### Check Replication Sender Status

```sql
SELECT rep_name,
       start_flag,
       net_error_flag,
       xsn,
       commit_xsn,
       status,
       sender_ip,
       sender_port,
       peer_ip,
       peer_port,
       read_log_count,
       send_log_count,
       repl_mode,
       act_repl_mode
FROM V$REPSENDER
ORDER BY rep_name;
```

`STATUS` values include `0` stop, `1` run, `2` retry, `6` sync, and `9` idle. `NET_ERROR_FLAG` value `1` indicates a network error.

### Check Replication Synchronization Progress

```sql
SELECT rep_name,
       sync_table,
       sync_partition,
       sync_record_count
FROM V$REPSYNC
ORDER BY rep_name, sync_table, sync_partition;
```

Use `V$REPSYNC` while `SYNC` or `SYNC ONLY` is running. `SYNC_RECORD_COUNT` shows synchronized records during synchronization and `-1` after synchronization completes.

### Check Replication Receiver Status

```sql
SELECT rep_name,
       my_ip,
       my_port,
       peer_ip,
       peer_port,
       apply_xsn,
       insert_success_count,
       insert_failure_count,
       update_success_count,
       update_failure_count,
       delete_success_count,
       delete_failure_count,
       sql_apply_table_count,
       applier_init_buffer_usage
FROM V$REPRECEIVER
ORDER BY rep_name;
```

Failure counts include conflicts and are not reduced when a statement rolls back.

### Check Replication Target Columns

```sql
SELECT rep_name,
       user_name,
       table_name,
       partition_name,
       column_name,
       apply_mode
FROM V$REPRECEIVER_COLUMN
WHERE rep_name = '<REPLICATION_NAME>'
ORDER BY user_name, table_name, partition_name, column_name;
```

`APPLY_MODE` values are `0` binary mode and `1` SQL mode.

## Cookbook: Database Links

### Check Database Link Definitions

```sql
SELECT u.user_name,
       d.link_name,
       d.link_id,
       d.link_oid,
       d.user_mode,
       d.remote_user_id,
       d.link_type,
       d.target_name,
       d.created,
       d.last_ddl_time
FROM SYSTEM_.SYS_DATABASE_LINKS_ d,
     SYSTEM_.SYS_USERS_ u
WHERE d.user_id = u.user_id
ORDER BY u.user_name, d.link_name;
```

Do not display `REMOTE_USER_PWD` in customer-facing answers.

### Check AltiLinker and Linker Sessions

```sql
SELECT status,
       session_count,
       remote_session_count,
       jvm_memory_pool_max_size,
       jvm_memory_usage,
       start_time
FROM V$DBLINK_ALTILINKER_STATUS;

SELECT session_id,
       status,
       session_type
FROM V$DBLINK_LINKER_SESSION_INFO
ORDER BY session_type, session_id;
```

### Check Database Link Transactions and Remote SQL

```sql
SELECT transaction_id,
       status,
       session_id,
       remote_transaction_count,
       transaction_level,
       global_transaction_id
FROM V$DBLINK_GLOBAL_TRANSACTION_INFO
ORDER BY transaction_id;

SELECT transaction_id,
       remote_transaction_id,
       statement_id,
       global_transaction_id,
       query
FROM V$DBLINK_REMOTE_STATEMENT_INFO
ORDER BY transaction_id, statement_id;
```

## Cookbook: Backup, Archive, Log, and File State

### Check Server Log and Archive Mode

```sql
SELECT server_status,
       archivelog_mode,
       begin_chkpt_file_no,
       begin_chkpt_file_offset,
       end_chkpt_file_no,
       end_chkpt_file_offset,
       oldest_logfile_no,
       oldest_logfile_offset,
       transaction_segment_count
FROM V$LOG;
```

`SERVER_STATUS` values include server shutdown and server started. `ARCHIVELOG_MODE` values include `ARCHIVE` and `NOARCHIVE`. For `CHECKPOINT_SCALE`, use the 8.1-only stable checkpoint check instead of adding it to this common query.

### Check Log File Group and Group Commit State

```sql
SELECT lfg_id,
       cur_write_lf_no,
       cur_write_lf_offset,
       lf_open_count,
       lf_prepare_count,
       lf_prepare_wait_count,
       lst_prepare_lf_no,
       end_lsn_file_no,
       end_lsn_offset,
       first_deleted_logfile,
       last_deleted_logfile,
       reset_lsn_file_no,
       reset_lsn_offset,
       update_tx_count,
       gc_wait_count,
       gc_already_sync_count,
       gc_real_sync_count
FROM V$LFG
ORDER BY lfg_id;
```

Use `LF_PREPARE_WAIT_COUNT` when checking whether log-file preparation is falling behind, and use `GC_WAIT_COUNT` with the group-commit counters only as cumulative evidence since server start.

### Check Archive Progress

```sql
SELECT lfg_id,
       archive_mode,
       archive_thr_running,
       archive_dest,
       nextlogfile_to_arch,
       oldest_active_logfile,
       current_logfile
FROM V$ARCHIVE
ORDER BY lfg_id;
```

`ARCHIVE_MODE` values are `0` no archive log mode and `1` archive log mode.

### Check Backup Metadata

```sql
SELECT begin_backup_time,
       end_backup_time,
       incremental_backup_chunk_count,
       backup_target,
       backup_level,
       backup_type,
       tablespace_id,
       file_id,
       backup_tag,
       backup_file
FROM V$BACKUP_INFO
ORDER BY begin_backup_time, backup_file;
```

`BACKUP_TARGET` values are `1` database and `2` tablespace. `BACKUP_LEVEL` values are `1` level 0 and `2` level 1. `BACKUP_TYPE` values are `1` full backup, `2` differential incremental backup, and `4` cumulative incremental backup.

### Check Obsolete Backup Metadata

```sql
SELECT begin_backup_time,
       end_backup_time,
       backup_target,
       backup_level,
       backup_type,
       tablespace_id,
       file_id,
       backup_tag,
       backup_file
FROM V$OBSOLETE_BACKUP_INFO
ORDER BY begin_backup_time, backup_file;
```

Use this as evidence for backup-retention cleanup questions. Do not recommend deleting backup files until the requested recovery target, retention rule, and current backup catalog are known.

### Check File I/O Hotspots

```sql
SELECT f.spaceid,
       t.name AS tablespace_name,
       f.fileid,
       d.name AS datafile_name,
       f.phyrds,
       f.phywrts,
       f.phyblkrd,
       f.phyblkwrt,
       f.singleblkrds,
       f.readtim,
       f.writetim,
       f.avgiotim,
       f.lstiotim,
       f.miniotim,
       f.maxiortm,
       f.maxiowtm
FROM V$FILESTAT f,
     V$DATAFILES d,
     V$TABLESPACES t
WHERE f.spaceid = d.spaceid
  AND f.fileid = d.id
  AND d.spaceid = t.id
ORDER BY f.avgiotim DESC, f.spaceid, f.fileid;
```

`V$FILESTAT` counters are cumulative since server start. Use them for relative hot-spot evidence and pair them with OS storage metrics before concluding that a device is faulty.

### Check File I/O Status

```sql
SELECT d.id,
       d.name,
       d.spaceid,
       t.name AS tablespace_name,
       t.page_size,
       d.currsize AS currsize_pages,
       d.currsize * t.page_size AS currsize_bytes,
       d.currsize * t.page_size / 1048576 AS currsize_mb,
       d.autoextend,
       d.iocount,
       d.opened,
       d.modified,
       d.state,
       d.cur_open_fd_count,
       d.max_open_fd_count
FROM V$DATAFILES d,
     V$TABLESPACES t
WHERE d.spaceid = t.id
ORDER BY d.spaceid, d.id;
```

`OPENED` values are `0` closed and `1` opened. `MODIFIED` value `1` means pages were flushed without subsequent synchronization. `STATE` values include offline, online, backup in progress, and dropped.

### Check Snapshot Usage

```sql
SELECT scn,
       begin_time,
       begin_mem_usage,
       begin_disk_undo_usage,
       current_time,
       current_mem_usage,
       current_disk_undo_usage
FROM V$SNAPSHOT;
```

Use `V$SNAPSHOT` when `BEGIN SNAPSHOT` is in use, especially before advising long-running export or undo-space actions.

### Check Trace Logging Flags

```sql
SELECT module_name,
       trclevel,
       flag,
       powlevel,
       description
FROM V$TRACELOG
WHERE module_name IN ('SM', 'SERVER', 'RP')
ORDER BY module_name, trclevel;
```

`FLAG` values include `O` output enabled, `X` output disabled, and `SUM` for the module's combined `POWLEVEL` value. Change message-log properties only after confirming the target module and support purpose.

## Cookbook: Temporary LOB in 8.1

### Check Temporary LOB Enablement and Usage

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name IN (
  'TEMPORARY_LOB_ENABLE',
  'MEMORY_TEMPLOB_MAX_ALLOC_SIZE',
  'MEMORY_TEMPLOB_PIECE_SIZE'
)
ORDER BY name;

SELECT type,
       id,
       alloced_size,
       open_count
FROM V$TEMPORARY_LOBS
ORDER BY type, id;
```

`TYPE` values are `0` transaction Temporary LOB and `1` session Temporary LOB. `ID` is the transaction ID or session ID according to `TYPE`. `ALLOCED_SIZE` is the Temporary LOB size. `OPEN_COUNT` is the number of created Temporary LOBs.

### Free Session Temporary LOBs

```sql
ALTER SESSION SET FREE TEMPORARY LOB;
```

Use this only when session Temporary LOB cleanup is intended.

## Searchable Object Blocks

### Object Block: `V$PROPERTY`

Purpose: shows internally set Altibase property values, min/max metadata, attributes, and multi-value entries.

Key columns: `NAME`, `STOREDCOUNT`, `ATTR`, `MIN`, `MAX`, `VALUE1`, `VALUE2`, `VALUE3`, `VALUE4`, `VALUE5`, `VALUE6`, `VALUE7`, `VALUE8`.

Representative SQL:

```sql
SELECT name, storedcount, attr, min, max, value1, value2, value3
FROM V$PROPERTY
WHERE name IN ('QUERY_TIMEOUT', 'SQL_PLAN_CACHE_SIZE', 'TIME_ZONE')
ORDER BY name;
```

### Object Block: `V$TABLE` and `V$ALLCOLUMN`

Purpose: list available performance views and the columns exposed by those views.

Key columns: `V$TABLE.NAME`, `V$TABLE.SLOTSIZE`, `V$TABLE.COLUMNCOUNT`, `V$ALLCOLUMN.TABLENAME`, `V$ALLCOLUMN.COLNAME`.

Representative SQL:

```sql
SELECT name, slotsize, columncount
FROM V$TABLE
WHERE name IN ('V$PROPERTY', 'V$SQL_PLAN_CACHE', 'V$TEMPORARY_LOBS')
ORDER BY name;

SELECT tablename, colname
FROM V$ALLCOLUMN
WHERE tablename IN ('V$PROPERTY', 'V$SQL_PLAN_CACHE', 'V$TEMPORARY_LOBS')
ORDER BY tablename, colname;
```

### Object Block: `V$VERSION`

Purpose: shows product, package, storage-manager, metadata, communication protocol, and replication protocol versions.

Key columns: `PRODUCT_VERSION`, `PKG_BUILD_PLATFORM_INFO`, `PRODUCT_TIME`, `SM_VERSION`, `META_VERSION`, `PROTOCOL_VERSION`, `REPL_PROTOCOL_VERSION`.

Representative SQL:

```sql
SELECT product_version,
       meta_version,
       protocol_version,
       repl_protocol_version
FROM V$VERSION;
```

### Object Block: `V$TIME_ZONE_NAMES`

Purpose: lists region names, abbreviations, and UTC offset values that can be used for `TIME_ZONE`.

Key columns: `NAME`, `UTC_OFFSET`.

Representative SQL:

```sql
SELECT name, utc_offset
FROM V$TIME_ZONE_NAMES
WHERE name IN ('Asia/Seoul', 'UTC')
ORDER BY name;
```

### Object Block: `SYSTEM_.SYS_TABLES_`

Purpose: stores meta tables, user tables, sequences, views, queues, and internal table-like objects.

Key columns: `USER_ID`, `TABLE_ID`, `TABLE_OID`, `TABLE_NAME`, `TABLE_TYPE`, `TBS_ID`, `TBS_NAME`, `IS_PARTITIONED`, `TEMPORARY`, `ACCESS`, `CREATED`, `LAST_DDL_TIME`.

Representative SQL:

```sql
SELECT u.user_name, t.table_name, t.table_type, t.table_oid, t.tbs_name
FROM SYSTEM_.SYS_TABLES_ t, SYSTEM_.SYS_USERS_ u
WHERE t.user_id = u.user_id
ORDER BY u.user_name, t.table_name;
```

### Object Block: `SYSTEM_.SYS_COLUMNS_`

Purpose: stores columns for tables, views, and sequences.

Key columns: `USER_ID`, `TABLE_ID`, `COLUMN_ID`, `COLUMN_ORDER`, `COLUMN_NAME`, `DATA_TYPE`, `PRECISION`, `SCALE`, `IS_NULLABLE`, `DEFAULT_VAL`, `STORE_TYPE`, `IS_HIDDEN`.

Representative SQL:

```sql
SELECT column_order, column_name, data_type, precision, scale, is_nullable
FROM SYSTEM_.SYS_COLUMNS_
WHERE user_id = <USER_ID>
  AND table_id = <TABLE_ID>
ORDER BY column_order;
```

### Object Block: `SYSTEM_.SYS_INDICES_` and `SYSTEM_.SYS_INDEX_COLUMNS_`

Purpose: store index definitions and index column order.

Key columns: `INDEX_ID`, `INDEX_NAME`, `INDEX_TYPE`, `IS_UNIQUE`, `COLUMN_CNT`, `IS_RANGE`, `IS_DIRECTKEY`, `IS_PARTITIONED`, `INDEX_COL_ORDER`, `SORT_ORDER`.

Representative SQL:

```sql
SELECT i.index_name, ic.index_col_order, ic.column_id, ic.sort_order
FROM SYSTEM_.SYS_INDICES_ i, SYSTEM_.SYS_INDEX_COLUMNS_ ic
WHERE i.user_id = ic.user_id
  AND i.table_id = ic.table_id
  AND i.index_id = ic.index_id
ORDER BY i.index_name, ic.index_col_order;
```

### Object Block: `SYSTEM_.SYS_CONSTRAINTS_` and `SYSTEM_.SYS_CONSTRAINT_COLUMNS_`

Purpose: store constraint definitions and participating columns.

Key columns: `CONSTRAINT_ID`, `CONSTRAINT_NAME`, `CONSTRAINT_TYPE`, `INDEX_ID`, `REFERENCED_TABLE_ID`, `DELETE_RULE`, `CHECK_CONDITION`, `VALIDATED`, `CONSTRAINT_COL_ORDER`.

Representative SQL:

```sql
SELECT cs.constraint_name, cs.constraint_type, cc.constraint_col_order, cc.column_id
FROM SYSTEM_.SYS_CONSTRAINTS_ cs, SYSTEM_.SYS_CONSTRAINT_COLUMNS_ cc
WHERE cs.user_id = cc.user_id
  AND cs.table_id = cc.table_id
  AND cs.constraint_id = cc.constraint_id
ORDER BY cs.constraint_name, cc.constraint_col_order;
```

### Object Block: `SYSTEM_.SYS_USERS_`

Purpose: stores users and roles.

Key columns: `USER_ID`, `USER_NAME`, `DEFAULT_TBS_ID`, `TEMP_TBS_ID`, `ACCOUNT_LOCK`, `PASSWORD_LIMIT_FLAG`, `FAILED_LOGIN_COUNT`, `USER_TYPE`, `DISABLE_TCP`, `CREATED`, `LAST_DDL_TIME`.

Representative SQL:

```sql
SELECT user_id, user_name, user_type, account_lock, disable_tcp, created
FROM SYSTEM_.SYS_USERS_
ORDER BY user_type, user_name;
```

### Object Block: `SYSTEM_.SYS_GRANT_SYSTEM_`, `SYSTEM_.SYS_GRANT_OBJECT_`, and `SYSTEM_.SYS_USER_ROLES_`

Purpose: stores system privilege grants, object privilege grants, and role grants.

Key columns: system grants use `GRANTOR_ID`, `GRANTEE_ID`, `PRIV_ID`; object grants add `USER_ID`, `OBJ_ID`, `OBJ_TYPE`, `WITH_GRANT_OPTION`; role grants use `GRANTEE_ID` and `ROLE_ID`.

Representative SQL:

```sql
SELECT grantee.user_name AS grantee_name, p.priv_name
FROM SYSTEM_.SYS_GRANT_SYSTEM_ g,
     SYSTEM_.SYS_USERS_ grantee,
     SYSTEM_.SYS_PRIVILEGES_ p
WHERE g.grantee_id = grantee.user_id
  AND g.priv_id = p.priv_id
ORDER BY grantee.user_name, p.priv_name;
```

`SYSTEM_.SYS_GRANT_OBJECT_.OBJ_TYPE` common values are `T` table or view, `S` sequence, `P` stored procedure or function, `A` stored package, `D` directory, and `Y` library.

### Object Block: `SYSTEM_.SYS_SYNONYMS_`

Purpose: stores private and public synonym metadata.

Key columns: `SYNONYM_OWNER_ID`, `SYNONYM_NAME`, `OBJECT_OWNER_NAME`, `OBJECT_NAME`, `CREATED`, `LAST_DDL_TIME`.

Representative SQL:

```sql
SELECT owner.user_name AS synonym_owner,
       s.synonym_name,
       s.object_owner_name,
       s.object_name
FROM SYSTEM_.SYS_SYNONYMS_ s,
     SYSTEM_.SYS_USERS_ owner
WHERE s.synonym_owner_id = owner.user_id
ORDER BY owner.user_name, s.synonym_name;
```

### Object Block: `SYSTEM_.SYS_DIRECTORIES_`

Purpose: stores directory objects used by stored procedures for file access.

Key columns: `DIRECTORY_ID`, `USER_ID`, `DIRECTORY_NAME`, `DIRECTORY_PATH`, `CREATED`, `LAST_DDL_TIME`.

Representative SQL:

```sql
SELECT directory_name, directory_path, created, last_ddl_time
FROM SYSTEM_.SYS_DIRECTORIES_
ORDER BY directory_name;
```

### Object Block: `SYSTEM_.SYS_MATERIALIZED_VIEWS_`

Purpose: stores materialized view metadata and the internal maintenance table/view identifiers.

Key columns: `USER_ID`, `MVIEW_ID`, `MVIEW_NAME`, `TABLE_ID`, `VIEW_ID`, `REFRESH_TYPE`, `REFRESH_TIME`, `CREATED`, `LAST_DDL_TIME`, `LAST_REFRESH_TIME`.

Representative SQL:

```sql
SELECT u.user_name, m.mview_name, m.refresh_type, m.refresh_time,
       m.last_refresh_time
FROM SYSTEM_.SYS_MATERIALIZED_VIEWS_ m,
     SYSTEM_.SYS_USERS_ u
WHERE m.user_id = u.user_id
ORDER BY u.user_name, m.mview_name;
```

### Object Block: `SYSTEM_.SYS_TRIGGERS_`

Purpose: stores default trigger metadata; related trigger text and referenced-table metadata live in `SYSTEM_.SYS_TRIGGER_STRINGS_`, `SYSTEM_.SYS_TRIGGER_DML_TABLES_`, and `SYSTEM_.SYS_TRIGGER_UPDATE_COLUMNS_`.

Key columns: `USER_ID`, `USER_NAME`, `TRIGGER_OID`, `TRIGGER_NAME`, `TABLE_ID`, `IS_ENABLE`, `EVENT_TIME`, `EVENT_TYPE`, `UPDATE_COLUMN_CNT`, `GRANULARITY`, `REF_ROW_CNT`, `SUBSTRING_CNT`, `STRING_LENGTH`, `CREATED`, `LAST_DDL_TIME`.

Representative SQL:

```sql
SELECT user_name, trigger_name, table_id, is_enable, event_time,
       event_type, granularity, created, last_ddl_time
FROM SYSTEM_.SYS_TRIGGERS_
ORDER BY user_name, trigger_name;
```

### Object Block: `SYSTEM_.SYS_JOBS_`

Purpose: stores scheduler job definitions and last execution state.

Key columns: `JOB_ID`, `JOB_NAME`, `EXEC_QUERY`, `START_TIME`, `END_TIME`, `INTERVAL`, `INTERVAL_TYPE`, `STATE`, `LAST_EXEC_TIME`, `EXEC_COUNT`, `ERROR_CODE`, `IS_ENABLE`, `COMMENT`.

Representative SQL:

```sql
SELECT job_name, exec_query, start_time, interval, interval_type,
       state, is_enable, error_code, last_exec_time
FROM SYSTEM_.SYS_JOBS_
ORDER BY job_name;
```

### Object Block: `V$SESSION`

Purpose: shows current client sessions. This view is the first stop for session ownership, current transaction ID, current statement ID, timeout settings, client identity, session state, autocommit mode, replication mode, transaction mode, failover source, TLS client certificate fields, and application/module/action text.

Key columns: `ID`, `TRANS_ID`, `TASK_STATE`, `SESSION_STATE`, `ACTIVE_FLAG`, `OPENED_STMT_COUNT`, `CURRENT_STMT_ID`, `DB_USERNAME`, `DB_USERID`, `COMM_NAME`, `CLIENT_PACKAGE_VERSION`, `CLIENT_PROTOCOL_VERSION`, `CLIENT_PID`, `CLIENT_TYPE`, `CLIENT_APP_INFO`, `CLIENT_INFO`, `MODULE`, `ACTION`, `AUTOCOMMIT_FLAG`, `ISOLATION_LEVEL`, `REPLICATION_MODE`, `TRANSACTION_MODE`, `COMMIT_WRITE_WAIT_MODE`, `QUERY_TIME_LIMIT`, `DDL_TIME_LIMIT`, `FETCH_TIME_LIMIT`, `UTRANS_TIME_LIMIT`, `IDLE_TIME_LIMIT`, `IDLE_START_TIME`, `LOGIN_TIME`, `FAILOVER_SOURCE`, `TIME_ZONE`, `LOB_CACHE_THRESHOLD`, `QUERY_REWRITE_ENABLE`, `SSL_CIPHER`, `SSL_CERTIFICATE_SUBJECT`, `SSL_CERTIFICATE_ISSUER`, `REPLICATION_DDL_SYNC`, `REPLICATION_DDL_TIMELIMIT`, `MESSAGE_CALLBACK`.

Value notes: `TRANS_ID = -1` means no transaction is currently underway. `ACTIVE_FLAG = 1` means the session is executing a statement. `AUTOCOMMIT_FLAG` values are `0` non-autocommit and `1` autocommit. `TRANSACTION_MODE` values include `0` read/write and `4` read only. `COMMIT_WRITE_WAIT_MODE` values are `0` do not wait for commit logs to be written to disk and `1` wait for commit logs to be written. `REPLICATION_MODE` values include `0` default and `16` none. `QUERY_REWRITE_ENABLE` values include `FALSE` and `TRUE`. `MESSAGE_CALLBACK` values include `REG`, `UNREG`, and `UNKNOWN`.

When to query: use `V$SESSION` before `V$STATEMENT`, `V$SQLTEXT`, `V$SESSION_WAIT`, `V$LOCK_WAIT`, or `V$TRANSACTION` when the user gives a session ID, user name, client process, application name, failover symptom, TLS client-authentication symptom, timeout symptom, or "who is running this" question.

Representative SQL:

```sql
SELECT id,
       db_username,
       task_state,
       session_state,
       active_flag,
       trans_id,
       current_stmt_id,
       opened_stmt_count,
       autocommit_flag,
       transaction_mode,
       client_app_info,
       client_info,
       module,
       action
FROM V$SESSION
ORDER BY id;
```

### Object Block: `V$SESSIONMGR`

Purpose: shows cumulative session-manager counters since Altibase startup.

Key columns: `TASK_COUNT`, `BASE_TIME`, `LOGIN_TIMEOUT_COUNT`, `IDLE_TIMEOUT_COUNT`, `QUERY_TIMEOUT_COUNT`, `DDL_TIMEOUT_COUNT`, `FETCH_TIMEOUT_COUNT`, `UTRANS_TIMEOUT_COUNT`, `SESSION_TERMINATE_COUNT`.

When to query: use `V$SESSIONMGR` when the user asks whether timeout or forced-termination events are accumulating across the server, or wants the current connected-session count without per-session details.

Representative SQL:

```sql
SELECT task_count,
       login_timeout_count,
       idle_timeout_count,
       query_timeout_count,
       ddl_timeout_count,
       fetch_timeout_count,
       utrans_timeout_count,
       session_terminate_count
FROM V$SESSIONMGR;
```

### Object Block: `V$SERVICE_THREAD` and `V$SERVICE_THREAD_MGR`

Purpose: `V$SERVICE_THREAD` shows service threads that receive and execute client requests; `V$SERVICE_THREAD_MGR` shows cumulative counts of dynamically added and removed service threads.

Key columns: service-thread identity and state use `ID`, `TYPE`, `STATE`, `RUN_MODE`, `THREAD_ID`; active work uses `SESSION_ID`, `STATEMENT_ID`, `EXECUTE_TIME`; queue and fan-in use `TASK_COUNT`, `READY_TASK_COUNT`; manager counters use `ADD_THR_COUNT`, `REMOVE_THR_COUNT`.

Value notes: `TYPE` values include `SOCKET(MULTIPLEXING)`, `SOCKET(DEDICATED)`, `IPC`, and `IPCDA`. `STATE` values include `NONE`, `POLL`, `QUEUE-WAIT`, `EXECUTE`, and `UNKNOWN`. `RUN_MODE` values are `SHARED` and `DEDICATED`. `START_TIME` is in seconds. `EXECUTE_TIME` is in microseconds. `READY_TASK_COUNT` is the number of sessions waiting for their requests to be processed by the service thread.

When to query: use this pair for service-thread overload, multiplexing/dedicated mode checks, queueing evidence, OS-thread correlation through `THREAD_ID`, or service-thread churn since startup. Use `SESSION_ID` and `STATEMENT_ID` to join back to `V$SESSION` and `V$STATEMENT`.

Representative SQL:

```sql
SELECT t.id,
       t.type,
       t.state,
       t.run_mode,
       t.session_id,
       t.statement_id,
       t.execute_time,
       t.task_count,
       t.ready_task_count,
       t.thread_id,
       s.db_username,
       st.query
FROM V$SERVICE_THREAD t,
     V$SESSION s,
     V$STATEMENT st
WHERE t.session_id = s.id
  AND t.session_id = st.session_id
  AND t.statement_id = st.id
ORDER BY t.ready_task_count DESC, t.execute_time DESC;
```

For a grouped snapshot:

```sql
SELECT type,
       run_mode,
       state,
       COUNT(*) AS thread_count,
       SUM(task_count) AS task_count,
       SUM(ready_task_count) AS ready_task_count
FROM V$SERVICE_THREAD
GROUP BY type, run_mode, state
ORDER BY ready_task_count DESC, thread_count DESC;

SELECT add_thr_count, remove_thr_count
FROM V$SERVICE_THREAD_MGR;
```

### Object Block: `V$STATEMENT`

Purpose: shows the most recently executed query information for connected sessions, including current statement state, statement text, elapsed-time breakdown, plan-cache linkage, page and scan counters, execution/fetch result counters, processed rows, and the current wait event.

Key columns: `ID`, `PARENT_ID`, `CURSOR_TYPE`, `SESSION_ID`, `TX_ID`, `QUERY`, `LAST_QUERY_START_TIME`, `QUERY_START_TIME`, `FETCH_START_TIME`, `EXECUTE_STATE`, `FETCH_STATE`, `ARRAY_FLAG`, `ROW_NUMBER`, `EXECUTE_FLAG`, `BEGIN_FLAG`, `TOTAL_TIME`, `PARSE_TIME`, `VALIDATE_TIME`, `OPTIMIZE_TIME`, `EXECUTE_TIME`, `FETCH_TIME`, `SOFT_PREPARE_TIME`, `SQL_CACHE_TEXT_ID`, `SQL_CACHE_PCO_ID`, `OPTIMIZER`, `COST`, `READ_PAGE`, `WRITE_PAGE`, `GET_PAGE`, `CREATE_PAGE`, `UNDO_READ_PAGE`, `UNDO_WRITE_PAGE`, `UNDO_GET_PAGE`, `UNDO_CREATE_PAGE`, `MEM_CURSOR_FULL_SCAN`, `MEM_CURSOR_INDEX_SCAN`, `DISK_CURSOR_FULL_SCAN`, `DISK_CURSOR_INDEX_SCAN`, `EXECUTE_SUCCESS`, `EXECUTE_FAILURE`, `FETCH_SUCCESS`, `FETCH_FAILURE`, `PROCESS_ROW`, `MEMORY_TABLE_ACCESS_COUNT`, `SEQNUM`, `EVENT`, `P1`, `P2`, `P3`, `WAIT_TIME`, `SECOND_IN_TIME`.

Value notes: `EXECUTE_FLAG = 1` means currently executing and `0` means not currently executing. `BEGIN_FLAG` uses the same `0`/`1` current-execution meaning. `EXECUTE_STATE` values include `ALLOC`, `PREPARED`, `EXECUTED`, and `UNKNOWN`. `FETCH_STATE` values include `PROCEED`, `CLOSE`, `NO_RESULTSET`, `INVALIDATED`, and `UNKNOWN`. `CURSOR_TYPE` hex value `0x02` indicates a memory cursor and `0x04` indicates a disk cursor. `SQL_CACHE_TEXT_ID = 'NO_SQL_CACHE_STMT'` indicates a statement not registered in SQL Plan Cache, such as DDL, DCL, or SQL using the `NO_PLAN_CACHE` hint.

Representative SQL:

```sql
SELECT session_id,
       id,
       execute_flag,
       execute_state,
       fetch_state,
       total_time,
       execute_time,
       fetch_time,
       read_page,
       get_page,
       process_row,
       event,
       wait_time,
       query
FROM V$STATEMENT
ORDER BY execute_flag DESC, total_time DESC;
```

### Column Block: `V$STATEMENT` Large-View Columns

Purpose: use this searchable column block when a question asks which `V$STATEMENT` column explains current SQL text, elapsed time, page access, scan counts, execution result counts, or the current wait event.

Key columns: identity and SQL text use `ID`, `PARENT_ID`, `SESSION_ID`, `TX_ID`, `QUERY`; state uses `EXECUTE_STATE`, `FETCH_STATE`, `ARRAY_FLAG`, `EXECUTE_FLAG`, `BEGIN_FLAG`; elapsed timing uses `TOTAL_TIME`, `PARSE_TIME`, `VALIDATE_TIME`, `OPTIMIZE_TIME`, `EXECUTE_TIME`, `FETCH_TIME`, `SOFT_PREPARE_TIME`; plan cache linkage uses `SQL_CACHE_TEXT_ID`, `SQL_CACHE_PCO_ID`; page counters use `READ_PAGE`, `WRITE_PAGE`, `GET_PAGE`, `CREATE_PAGE`, `UNDO_READ_PAGE`, `UNDO_WRITE_PAGE`, `UNDO_GET_PAGE`, `UNDO_CREATE_PAGE`; scan counters use `MEM_CURSOR_FULL_SCAN`, `MEM_CURSOR_INDEX_SCAN`, `DISK_CURSOR_FULL_SCAN`, `DISK_CURSOR_INDEX_SCAN`; result counters use `EXECUTE_SUCCESS`, `EXECUTE_FAILURE`, `FETCH_SUCCESS`, `FETCH_FAILURE`, `PROCESS_ROW`, `MEMORY_TABLE_ACCESS_COUNT`; wait columns use `SEQNUM`, `EVENT`, `P1`, `P2`, `P3`, `WAIT_TIME`, `SECOND_IN_TIME`.

When to query: query `V$STATEMENT` after identifying a session with `V$SESSION`, or directly when the user asks which SQL is slow, currently executing, waiting, scanning heavily, reading disk pages, or linked to SQL plan cache objects.

Representative SQL:

```sql
SELECT session_id,
       id,
       execute_state,
       fetch_state,
       total_time,
       execute_time,
       fetch_time,
       read_page,
       get_page,
       process_row,
       event,
       wait_time,
       query
FROM V$STATEMENT
ORDER BY total_time DESC;
```

### Object Block: `V$SQLTEXT`

Purpose: shows SQL text currently being executed in the server as ordered 64-byte fragments.

Key columns: `SID`, `STMT_ID`, `PIECE`, `TEXT`.

Value notes: `SID` is the session identifier. `STMT_ID` is the statement identifier. `PIECE` starts at `0` and preserves fragment order. `TEXT` is one 64-byte SQL text fragment.

When to query: use `V$SQLTEXT` when `V$STATEMENT.QUERY` is truncated, when the user asks for exact SQL text fragments, or when reconstructing the current SQL for a session and statement ID. Always order by `PIECE`.

Representative SQL:

```sql
SELECT sid,
       stmt_id,
       piece,
       text
FROM V$SQLTEXT
WHERE sid = <SESSION_ID>
  AND stmt_id = <STMT_ID>
ORDER BY piece;
```

To discover the current statement ID first:

```sql
SELECT s.id AS session_id,
       s.current_stmt_id,
       x.piece,
       x.text
FROM V$SESSION s,
     V$SQLTEXT x
WHERE s.id = x.sid
  AND s.current_stmt_id = x.stmt_id
  AND s.id = <SESSION_ID>
ORDER BY x.piece;
```

### Object Block: `V$STATNAME`, `V$SYSSTAT`, and `V$SESSTAT`

Purpose: `V$STATNAME` maps statistic identifiers to statistic names; `V$SYSSTAT` shows system-wide statistic values; `V$SESSTAT` shows statistic values for connected sessions.

Key columns: `V$STATNAME.SEQNUM`, `V$STATNAME.NAME`, `V$SYSSTAT.SEQNUM`, `V$SYSSTAT.NAME`, `V$SYSSTAT.VALUE`, `V$SESSTAT.SID`, `V$SESSTAT.SEQNUM`, `V$SESSTAT.NAME`, `V$SESSTAT.VALUE`.

When to query: use this family when the user asks what a statistic identifier means, wants system versus session counter values, or needs counters for logons, timeouts, commits, rollbacks, execution/fetch failures, page I/O, scan counts, communication bytes, plan-cache elapsed time, replication elapsed time, or task scheduling.

Representative SQL:

```sql
SELECT seqnum, name
FROM V$STATNAME
WHERE name IN (
  'query timeout',
  'execute failure count',
  'data page read',
  'elapsed time: query execute'
)
ORDER BY seqnum;

SELECT seqnum, name, value
FROM V$SYSSTAT
WHERE name IN (
  'query timeout',
  'execute failure count',
  'data page read',
  'elapsed time: query execute'
)
ORDER BY seqnum;

SELECT sid, seqnum, name, value
FROM V$SESSTAT
WHERE sid = <SESSION_ID>
ORDER BY seqnum;
```

### Column Block: `V$STATNAME` Statistic Families

Purpose: make statistic-name questions searchable without expanding the full manual table into the attachment.

Key columns: `SEQNUM` is the statistic identifier; `NAME` is the literal statistic name used by `V$SYSSTAT` and `V$SESSTAT`.

When to query: query `V$STATNAME` first when a user has a numeric `SEQNUM`, then query `V$SYSSTAT` or `V$SESSTAT` for values. Query value views directly when the user already has a statistic name.

Representative SQL:

```sql
SELECT n.seqnum,
       n.name,
       s.value AS system_value
FROM V$STATNAME n,
     V$SYSSTAT s
WHERE n.seqnum = s.seqnum
  AND n.name LIKE 'elapsed time:%'
ORDER BY n.seqnum;
```

Searchable statistic groups:

| Group | Representative `V$STATNAME.NAME` entries |
| --- | --- |
| Logon and timeout counters | `logon current`, `logon cumulative`, `query timeout`, `ddl timeout`, `idle timeout`, `fetch timeout`, `utrans timeout`, `session terminated`, `ddl sync timeout` |
| Transaction and execution counters | `session commit`, `session rollback`, `execute success count`, `execute failure count`, `prepare success count`, `prepare failure count`, `fetch success count`, `fetch failure count`, `statement rebuild count`, `rebuild count` |
| Page I/O counters | `data page read`, `data page write`, `data page gets`, `data page fix`, `data page create`, `undo page read`, `undo page write`, `undo page gets`, `undo page fix`, `undo page create` |
| Cursor and table access counters | `memory table cursor full scan count`, `memory table cursor index scan count`, `memory table cursor GRID scan count`, `disk table cursor full scan count`, `disk table cursor index scan count`, `disk table cursor GRID scan count`, `memory table access count` |
| Network counters | `read socket count`, `write socket count`, `byte received via inet`, `byte sent via inet`, `byte received via unix domain`, `byte sent via unix domain`, `read IB count`, `write IB count`, `byte received via IB`, `byte sent via IB` |
| Elapsed-time counters | `elapsed time: query parse`, `elapsed time: query validate`, `elapsed time: query optimize`, `elapsed time: query execute`, `elapsed time: query fetch`, `elapsed time: hard prepare time`, `elapsed time: sender(s) sending XLogs to receiver(s)`, `elapsed time: receiver(s) inserting rows`, `elapsed time: task schedule`, `max time: task schedule` |

Elapsed-time statistics in this table are documented in microseconds.

### Object Block: `V$MEMSTAT`

Purpose: shows memory used by Altibase process modules.

Key columns: `NAME`, `ALLOC_SIZE`, `ALLOC_COUNT`, `MAX_TOTAL_SIZE`.

When to query: use `V$MEMSTAT` when memory growth must be attributed to a module such as communication, SQL execution, PSM, replication, plan cache, disk index build, storage, temporary memory, thread stack, Database Link, external procedures, or GIS.

Representative SQL:

```sql
SELECT name,
       alloc_size,
       alloc_count,
       max_total_size
FROM V$MEMSTAT
ORDER BY alloc_size DESC;
```

### Module Block: `V$MEMSTAT.NAME` Memory Module Families

Purpose: make high-priority `V$MEMSTAT.NAME` module names searchable for memory diagnosis.

Key columns: `NAME` is the module label; `ALLOC_SIZE` is memory used by that module in bytes; `ALLOC_COUNT` is the number of memory units that make up `ALLOC_SIZE`; `MAX_TOTAL_SIZE` is the maximum memory size of the module in bytes.

When to query: filter by module names when a memory question already points to a subsystem; otherwise sort all rows by `ALLOC_SIZE` and compare repeated snapshots.

Representative SQL:

```sql
SELECT name, alloc_size, alloc_count, max_total_size
FROM V$MEMSTAT
WHERE name IN (
  'CM_Buffer',
  'Query_Execute',
  'Query_Prepare',
  'Query_Meta',
  'Query_PSM_Concurrent_Execute',
  'SQL_Plan_Cache_Control',
  'Storage_Disk_Index',
  'Storage_Disk_Buffer',
  'Storage_Memory_Manager',
  'Replication_Sender',
  'Replication_Receiver',
  'Temp_Memory'
)
ORDER BY alloc_size DESC;
```

Searchable module groups:

| Group | Representative `V$MEMSTAT.NAME` entries |
| --- | --- |
| Communication | `CM_Buffer`, `CM_DataType`, `CM_Interface`, `CM_Multiplexing`, `CM_NetworkInterface`, `Socket_Manager` |
| Query and PSM | `Query_Binding`, `Query_Common`, `Query_DML`, `Query_Execute`, `Query_Meta`, `Query_Prepare`, `Query_PSM_Concurrent_Execute`, `Query_PSM_Execute`, `Query_Result_Cache`, `Query_Sequence`, `Query_Transaction` |
| Plan cache and fixed tables | `SQL_Plan_Cache_Control`, `Fixed_Table` |
| Replication | `Replication_Control`, `Replication_Data`, `Replication_Met`, `Replication_Network`, `Replication_Receiver`, `Replication_Recovery`, `Replication_Sender`, `Replication_Storage`, `Replication_Sync` |
| Storage | `Storage_Disk_Buffer`, `Storage_Disk_Datafile`, `Storage_Disk_Index`, `Storage_Disk_Page`, `Storage_Disk_Recovery`, `Storage_Disk_SecondaryBuffer`, `Storage_Memory_Ager`, `Storage_Memory_Index`, `Storage_Memory_Manager`, `Storage_Memory_Page`, `Storage_Memory_Transaction`, `Storage_Tablespace` |
| Transaction and temporary memory | `Transaction_DiskPage_Touched_List`, `Transaction_OID_List`, `Transaction_Segment_Table`, `Transaction_Table`, `Transaction_Table_Info`, `Temp_Memory`, `Volatile_Log_Buffer`, `Volatile_Memory_Manager`, `Volatile_Memory_Page` |
| Extension and support modules | `Database_Link`, `External_Procedure`, `External_Procedure_Agent`, `GIS_DataType`, `GIS_Disk_Index`, `GIS_Function`, `Thread_Stack`, `Timer_Manager`, `SYSTEM` |

### Object Block: `V$BUFFPOOL_STAT`

Purpose: shows buffer pool size, list structure, hit ratio, page access counters, replacement-search counters, and disk read performance.

Key columns: `ID`, `POOL_SIZE`, `PAGE_SIZE`, `HASH_BUCKET_COUNT`, `HASH_CHAIN_LATCH_COUNT`, `LRU_LIST_COUNT`, `PREPARE_LIST_COUNT`, `FLUSH_LIST_COUNT`, `CHECKPOINT_LIST_COUNT`, `HASH_PAGES`, `HOT_LIST_PAGES`, `COLD_LIST_PAGES`, `PREPARE_LIST_PAGES`, `FLUSH_LIST_PAGES`, `CHECKPOINT_LIST_PAGES`, `FIX_PAGES`, `GET_PAGES`, `READ_PAGES`, `CREATE_PAGES`, `HIT_RATIO`, `VICTIM_FAILS`, `PREPARE_AGAIN_VICTIMS`, `VICTIM_SEARCH_WARP`, `LRU_SEARCHS`, `LRU_SEARCHS_AVG`, `DB_SINGLE_READ_PERF`, `DB_MULTI_READ_PERF`.

When to query: use this view for buffer pool hit ratio questions, disk page read pressure, replacement-target search pressure, high flush/checkpoint list counts, or to verify list-count properties such as LRU, prepare, flush, and checkpoint list counts.

Representative SQL:

```sql
SELECT id,
       pool_size,
       page_size,
       hit_ratio,
       get_pages,
       fix_pages,
       read_pages,
       flush_list_pages,
       checkpoint_list_pages,
       victim_fails,
       prepare_again_victims,
       victim_search_warp,
       lru_searchs_avg
FROM V$BUFFPOOL_STAT
ORDER BY id;
```

### Column Block: `V$BUFFPOOL_STAT` Buffer Pool Counters

Purpose: make exact buffer-pool column questions searchable without listing every detailed manual paragraph.

Key columns: capacity columns are `POOL_SIZE`, `PAGE_SIZE`, `HASH_BUCKET_COUNT`, `HASH_CHAIN_LATCH_COUNT`; list-count columns are `LRU_LIST_COUNT`, `PREPARE_LIST_COUNT`, `FLUSH_LIST_COUNT`, `CHECKPOINT_LIST_COUNT`; current page distribution columns are `HASH_PAGES`, `HOT_LIST_PAGES`, `COLD_LIST_PAGES`, `PREPARE_LIST_PAGES`, `FLUSH_LIST_PAGES`, `CHECKPOINT_LIST_PAGES`; I/O and hit columns are `FIX_PAGES`, `GET_PAGES`, `READ_PAGES`, `CREATE_PAGES`, `HIT_RATIO`; replacement columns are `PREPARE_VICTIMS`, `LRU_VICTIMS`, `VICTIM_FAILS`, `PREPARE_AGAIN_VICTIMS`, `VICTIM_SEARCH_WARP`; search and movement columns are `LRU_SEARCHS`, `LRU_SEARCHS_AVG`, `LRU_TO_HOTS`, `LRU_TO_COLDS`, `LRU_TO_FLUSHS`, `HOT_INSERTIONS`, `COLD_INSERTIONS`; read-performance columns are `DB_SINGLE_READ_PERF`, `DB_MULTI_READ_PERF`.

When to query: compare time-window snapshots when diagnosing buffer pool pressure. `READ_PAGES` indicates buffer misses, `HIT_RATIO` is cumulative since startup, `VICTIM_FAILS` is failures to find a replacement target, `PREPARE_AGAIN_VICTIMS` counts replacement targets found after waiting for prepare-list buffers, and `VICTIM_SEARCH_WARP` counts searches that failed after the specified time and passed to the next prepare list.

Representative SQL:

```sql
SELECT id,
       read_pages,
       hit_ratio,
       prepare_victims,
       lru_victims,
       victim_fails,
       prepare_again_victims,
       victim_search_warp,
       lru_searchs,
       lru_searchs_avg
FROM V$BUFFPOOL_STAT
ORDER BY id;
```

### Object Block: `V$INTERNAL_SESSION`

Purpose: shows sessions created by the `DBMS_CONCURRENT_EXEC` package; use `V$SESSION` for normal client sessions.

Key columns: `ID`, `TRANS_ID`, `QUERY_TIME_LIMIT`, `DDL_TIME_LIMIT`, `FETCH_TIME_LIMIT`, `UTRANS_TIME_LIMIT`, `IDLE_TIME_LIMIT`, `IDLE_START_TIME`, `ACTIVE_FLAG`, `OPENED_STMT_COUNT`, `DB_USERNAME`, `DB_USERID`, `SYSDBA_FLAG`, `AUTOCOMMIT_FLAG`, `SESSION_STATE`, `ISOLATION_LEVEL`, `CURRENT_STMT_ID`, `STACK_SIZE`, `DEFAULT_DATE_FORMAT`, `TRX_UPDATE_MAX_LOGSIZE`, `LOGIN_TIME`, `FAILOVER_SOURCE`, `TIME_ZONE`, `LOB_CACHE_THRESHOLD`, `QUERY_REWRITE_ENABLE`.

When to query: use this view when a runtime question involves `DBMS_CONCURRENT_EXEC`, internal PSM concurrent execution sessions, internal session time limits, active internal work, current statement ID, session state, user identity, or inherited session properties.

Representative SQL:

```sql
SELECT id,
       trans_id,
       db_username,
       session_state,
       active_flag,
       opened_stmt_count,
       current_stmt_id,
       query_time_limit,
       ddl_time_limit,
       fetch_time_limit,
       utrans_time_limit,
       idle_time_limit,
       time_zone
FROM V$INTERNAL_SESSION
ORDER BY id;
```

### Column Block: `V$INTERNAL_SESSION` Large-View Columns

Purpose: make exact `V$INTERNAL_SESSION` column lookup searchable for internal session troubleshooting.

Key columns: identity and transaction columns are `ID`, `TRANS_ID`, `DB_USERNAME`, `DB_USERID`, `DEFAULT_TBSID`, `DEFAULT_TEMP_TBSID`; limit columns are `QUERY_TIME_LIMIT`, `DDL_TIME_LIMIT`, `FETCH_TIME_LIMIT`, `UTRANS_TIME_LIMIT`, `IDLE_TIME_LIMIT`, `IDLE_START_TIME`; activity columns are `ACTIVE_FLAG`, `OPENED_STMT_COUNT`, `SESSION_STATE`, `CURRENT_STMT_ID`, `LOGIN_TIME`; transaction mode columns are `AUTOCOMMIT_FLAG`, `ISOLATION_LEVEL`, `REPLICATION_MODE`, `TRANSACTION_MODE`, `COMMIT_WRITE_WAIT_MODE`; execution environment columns are `OPTIMIZER_MODE`, `HEADER_DISPLAY_MODE`, `STACK_SIZE`, `DEFAULT_DATE_FORMAT`, `TRX_UPDATE_MAX_LOGSIZE`, `NLS_TERRITORY`, `NLS_ISO_CURRENCY`, `NLS_CURRENCY`, `NLS_NUMERIC_CHARACTERS`, `TIME_ZONE`, `LOB_CACHE_THRESHOLD`, `QUERY_REWRITE_ENABLE`; connection and privilege columns are `SYSDBA_FLAG`, `FAILOVER_SOURCE`.

When to query: start with `V$INTERNAL_SESSION` for package-created internal sessions, then use `CURRENT_STMT_ID` with `V$STATEMENT.ID` and `ID` with `V$STATEMENT.SESSION_ID` if SQL text or wait information is needed.

Representative SQL:

```sql
SELECT s.id,
       s.db_username,
       s.session_state,
       s.active_flag,
       s.current_stmt_id,
       st.execute_state,
       st.event,
       st.query
FROM V$INTERNAL_SESSION s,
     V$STATEMENT st
WHERE s.id = st.session_id
ORDER BY s.id, st.id;
```

### Object Block: `V$EVENT_NAME` and `V$WAIT_CLASS_NAME`

Purpose: `V$EVENT_NAME` maps Altibase wait-event IDs to event names and wait classes; `V$WAIT_CLASS_NAME` maps wait-class IDs to class names.

Key columns: `V$EVENT_NAME.EVENT_ID`, `V$EVENT_NAME.NAME`, `V$EVENT_NAME.WAIT_CLASS_ID`, `V$EVENT_NAME.WAIT_CLASS`, `V$WAIT_CLASS_NAME.WAIT_CLASS_ID`, `V$WAIT_CLASS_NAME.WAIT_CLASS`.

Value notes: wait classes include `Other`, `Administrative`, `Configuration`, `Concurrency`, `Commit`, `Idle`, `User I/O`, `System I/O`, and `Replication`. Event names include lock waits, disk I/O waits, buffer/latch waits, plan-cache latch waits, replication waits, and `no wait event`.

When to query: use these views when the user gives `SEQNUM`, `EVENT_ID`, or `WAIT_CLASS_ID`, or when a wait event from `V$SESSION_WAIT`, `V$SESSION_EVENT`, `V$SYSTEM_EVENT`, or `V$STATEMENT.EVENT` needs explanation.

Representative SQL:

```sql
SELECT event_id,
       name,
       wait_class_id,
       wait_class
FROM V$EVENT_NAME
ORDER BY wait_class_id, event_id;

SELECT wait_class_id,
       wait_class
FROM V$WAIT_CLASS_NAME
ORDER BY wait_class_id;
```

### Object Block: `V$SESSION_WAIT`, `V$SESSION_EVENT`, and `V$SESSION_WAIT_CLASS`

Purpose: show current and cumulative session wait information. `V$SESSION_WAIT` shows current waits for currently connected sessions. `V$SESSION_EVENT` shows cumulative wait statistics per session and event. `V$SESSION_WAIT_CLASS` shows cumulative wait statistics per session and wait class.

Key columns: current wait identity uses `SID`, `SEQNUM`, `EVENT`, `P1`, `P2`, `P3`; wait class uses `WAIT_CLASS_ID`, `WAIT_CLASS`; current wait duration uses `WAIT_TIME`, `SECOND_IN_WAIT`; cumulative session-event columns use `TOTAL_WAITS`, `TOTAL_TIMEOUTS`, `TIME_WAITED`, `AVERAGE_WAIT`, `MAX_WAIT`, `TIME_WAITED_MICRO`, `EVENT_ID`; session-wait-class columns use `SID`, `SERIAL`, `WAIT_CLASS_ID`, `WAIT_CLASS`, `TOTAL_WAITS`, `TIME_WAITED`.

When to query: use `V$SESSION_WAIT` for an instant "what is this session waiting on now" answer, then use `V$SESSION_EVENT` or `V$SESSION_WAIT_CLASS` to confirm whether the wait is recurring. These views do not provide wait information for sessions that are no longer connected.

Representative SQL:

```sql
SELECT sw.sid,
       s.db_username,
       sw.seqnum,
       sw.event,
       sw.wait_class,
       sw.wait_time,
       sw.second_in_wait,
       sw.p1,
       sw.p2,
       sw.p3
FROM V$SESSION_WAIT sw,
     V$SESSION s
WHERE sw.sid = s.id
ORDER BY sw.second_in_wait DESC, sw.wait_time DESC;
```

Cumulative session wait evidence:

```sql
SELECT sid,
       event,
       wait_class,
       total_waits,
       total_timeouts,
       time_waited,
       average_wait,
       max_wait,
       time_waited_micro
FROM V$SESSION_EVENT
WHERE sid = <SESSION_ID>
ORDER BY time_waited DESC, total_waits DESC;

SELECT sid,
       wait_class_id,
       wait_class,
       total_waits,
       time_waited
FROM V$SESSION_WAIT_CLASS
WHERE sid = <SESSION_ID>
ORDER BY time_waited DESC, total_waits DESC;
```

### Object Block: `V$SYSTEM_EVENT` and `V$SYSTEM_WAIT_CLASS`

Purpose: show cumulative wait statistics from server startup to the present at system level.

Key columns: `V$SYSTEM_EVENT` uses `EVENT`, `TOTAL_WAITS`, `TOTAL_TIMEOUTS`, `TIME_WAITED`, `AVERAGE_WAIT`, `TIME_WAITED_MICRO`, `EVENT_ID`, `WAIT_CLASS_ID`, `WAIT_CLASS`. `V$SYSTEM_WAIT_CLASS` uses `WAIT_CLASS_ID`, `WAIT_CLASS`, `TOTAL_WAITS`, and `TIME_WAITED`.

When to query: use these views for server-level wait-profile questions, especially when the user does not know which session is affected. Exclude `Idle` from bottleneck summaries unless the user explicitly asks about idle/request-wait behavior.

Representative SQL:

```sql
SELECT event,
       wait_class,
       total_waits,
       total_timeouts,
       time_waited,
       average_wait,
       time_waited_micro
FROM V$SYSTEM_EVENT
WHERE wait_class <> 'Idle'
ORDER BY time_waited DESC, total_waits DESC;

SELECT wait_class,
       total_waits,
       time_waited
FROM V$SYSTEM_WAIT_CLASS
WHERE wait_class <> 'Idle'
ORDER BY time_waited DESC, total_waits DESC;
```

### Object Block: `V$LATCH` and `V$MUTEX`

Purpose: provide lower-level contention evidence. `V$LATCH` shows Buffer Control Block latch attempts and misses for buffer-pool pages. `V$MUTEX` shows mutex statistics used by Altibase process concurrency control.

Key columns: `V$LATCH` uses `SPACE_ID`, `PAGE_ID`, `TRY_READ_LATCH`, `READ_SUCCESS_IMME`, `READ_MISS`, `TRY_WRITE_LATCH`, `WRITE_SUCCESS_IMME`, `WRITE_MISS`, `SLEEPS_CNT`. `V$MUTEX` uses `NAME`, `TRY_COUNT`, `LOCK_COUNT`, `MISS_COUNT`, `SPIN_VALUE`, `TOTAL_LOCK_TIME_US`, `MAX_LOCK_TIME_US`, `THREAD_ID`.

When to query: use these views after higher-level waits point to latch, buffer, page, or mutex contention. Prefer delta snapshots under a comparable workload; do not infer a specific SQL cause from these views alone without `V$SESSION`, `V$STATEMENT`, wait views, and plan evidence.

Representative SQL:

```sql
SELECT space_id,
       page_id,
       try_read_latch,
       read_miss,
       try_write_latch,
       write_miss,
       sleeps_cnt
FROM V$LATCH
ORDER BY sleeps_cnt DESC, read_miss + write_miss DESC;

SELECT name,
       try_count,
       lock_count,
       miss_count,
       total_lock_time_us,
       max_lock_time_us,
       thread_id
FROM V$MUTEX
ORDER BY miss_count DESC, total_lock_time_us DESC;
```

### Column Block: `V$TRANSACTION` Large-View Columns

Purpose: use this searchable column block when a question asks which transaction view column explains transaction identity, session ownership, MVCC view SCNs, status, update size, XA state, undo-log position, DDL flag, disk update slot, or isolation level.

Key columns: identity columns are `ID`, `SESSION_ID`, `SLOT_NO`; MVCC view columns are `MEMORY_VIEW_SCN`, `MIN_MEMORY_LOB_VIEW_SCN`, `DISK_VIEW_SCN`, `MIN_DISK_LOB_VIEW_SCN`, `COMMIT_SCN`; status columns are `STATUS`, `UPDATE_STATUS`, `LOG_TYPE`, `DDL_FLAG`, `ISOLATION_LEVEL`; XA columns are `XA_COMMIT_STATUS`, `XA_PREPARED_TIME`; undo log columns are `FIRST_UNDO_NEXT_LSN_FILENO`, `FIRST_UNDO_NEXT_LSN_OFFSET`, `CURRENT_UNDO_NEXT_SN`, `CURRENT_UNDO_NEXT_LSN_FILENO`, `CURRENT_UNDO_NEXT_LSN_OFFSET`, `LAST_UNDO_NEXT_LSN_FILENO`, `LAST_UNDO_NEXT_LSN_OFFSET`, `LAST_UNDO_NEXT_SN`; update and storage columns are `UPDATE_SIZE`, `FIRST_UPDATE_TIME`, `TSS_RID`, `RESOURCE_GROUP_ID`.

Value notes: `STATUS` values are `0` begin, `1` precommit, `2` commit in memory, `3` commit, `4` abort, `5` blocked, and `6` end. `UPDATE_STATUS` values are `0` read-only and `1` updating. `LOG_TYPE` values are `0` general and `1` replication-related. `XA_COMMIT_STATUS` values are `0` begin, `1` prepared, and `2` complete. `DDL_FLAG` values are `0` non-DDL and `1` DDL. `ISOLATION_LEVEL` values are `0` read committed, `1` repeatable read, and `2` serializable. A `SESSION_ID` of `-1` indicates a prepared transaction branch with no associated session in an XA environment.

When to query: query this view after identifying a session or transaction ID when the user asks whether a transaction is active, blocked, read-only, updating, DDL-related, XA-prepared, holding old MVCC views, or creating a large update footprint.

Representative SQL:

```sql
SELECT id,
       session_id,
       status,
       update_status,
       log_type,
       update_size,
       ddl_flag,
       isolation_level,
       memory_view_scn,
       disk_view_scn,
       commit_scn,
       first_update_time
FROM V$TRANSACTION
WHERE session_id = <SESSION_ID>
ORDER BY id;
```

### Object Block: `V$TRANSACTION_MGR`

Purpose: shows transaction-manager capacity and state.

Key columns: `TOTAL_COUNT`, `FREE_LIST_COUNT`, `BEGIN_ENABLE`, `ACTIVE_COUNT`, `SYS_MIN_DISK_VIEWSCN`.

Value notes: `TOTAL_COUNT` is the number of transaction objects created in the transaction pool at startup. `BEGIN_ENABLE` values are `0` disabled and `1` enabled. `ACTIVE_COUNT` is the number of transaction objects assigned to tasks and currently executing.

When to query: use this view when a question asks whether the server can start new transactions, how many transaction objects are active, or which system-level minimum disk view SCN is constraining disk undo or MVCC cleanup analysis.

Representative SQL:

```sql
SELECT total_count,
       free_list_count,
       begin_enable,
       active_count,
       sys_min_disk_viewscn
FROM V$TRANSACTION_MGR;
```

### Object Block: `V$LOCK_WAIT`, `V$LOCK`, and `V$LOCK_STATEMENT`

Purpose: show transaction wait chains, lock objects, and statements holding or waiting for locks.

Key columns: wait chains use `V$LOCK_WAIT.TRANS_ID` and `WAIT_FOR_TRANS_ID`; lock objects use `V$LOCK.LOCK_ITEM_TYPE`, `TBS_ID`, `TABLE_OID`, `DBF_ID`, `TRANS_ID`, `LOCK_DESC`, `LOCK_CNT`, `IS_GRANT`; lock statements use `SESSION_ID`, `ID`, `TX_ID`, `QUERY`, `STATE`, `BEGIN_FLAG`, `LOCK_ITEM_TYPE`, `TBS_ID`, `TABLE_OID`, `DBF_ID`, `LOCK_DESC`, `LOCK_CNT`, `IS_GRANT`.

Value notes: `LOCK_ITEM_TYPE` values include `TBS`, `TBL`, `DBF`, `UNKNOWN`, and the documented non-value `NONE`. `LOCK_DESC` is a lock-mode string such as `IX`, `IS`, or `X`. `IS_GRANT` indicates whether the lock is granted or waiting. `V$LOCK_WAIT.TRANS_ID` is the waiting transaction and `WAIT_FOR_TRANS_ID` is the transaction being waited for.

When to query: use `V$LOCK_WAIT` to build the transaction wait chain, `V$LOCK` to identify locked objects, and `V$LOCK_STATEMENT` to identify the SQL text associated with lock holders or waiters. Join to `V$TRANSACTION` and `V$SESSION` when users ask for session IDs, users, or client details.

Representative SQL:

```sql
SELECT trans_id, wait_for_trans_id
FROM V$LOCK_WAIT
ORDER BY wait_for_trans_id, trans_id;
```

Expanded blocker mapping:

```sql
SELECT lw.trans_id AS waiting_trans_id,
       tw.session_id AS waiting_session_id,
       sw.db_username AS waiting_user,
       lw.wait_for_trans_id AS holder_trans_id,
       th.session_id AS holder_session_id,
       sh.db_username AS holder_user
FROM V$LOCK_WAIT lw,
     V$TRANSACTION tw,
     V$TRANSACTION th,
     V$SESSION sw,
     V$SESSION sh
WHERE lw.trans_id = tw.id
  AND lw.wait_for_trans_id = th.id
  AND tw.session_id = sw.id
  AND th.session_id = sh.id
ORDER BY holder_session_id, waiting_session_id;
```

Object and SQL detail:

```sql
SELECT ls.session_id,
       ls.id AS stmt_id,
       ls.tx_id,
       ls.lock_item_type,
       ls.table_oid,
       ls.lock_desc,
       ls.lock_cnt,
       ls.is_grant,
       ls.query
FROM V$LOCK_STATEMENT ls
ORDER BY ls.is_grant, ls.session_id, ls.id;
```

### Object Block: `V$SQL_PLAN_CACHE`, `V$SQL_PLAN_CACHE_PCO`, and `V$SQL_PLAN_CACHE_SQLTEXT`

Purpose: show SQL plan cache size, hit/miss counters, plan cache objects, and cached SQL text.

Key columns: `CURRENT_CACHE_SIZE`, `CURRENT_CACHE_OBJ_COUNT`, `CACHE_HIT_COUNT`, `CACHE_MISS_COUNT`, `SQL_TEXT_ID`, `PCO_ID`, `HIT_COUNT`, `REBUILD_COUNT`, `PLAN_STATE`, `PLAN_CACHE_KEEP`, `SQL_TEXT`.

Representative SQL:

```sql
SELECT current_cache_size, current_cache_obj_count, cache_hit_count, cache_miss_count
FROM V$SQL_PLAN_CACHE;
```

### Object Block: `V$DBMS_STATS`

Purpose: shows collected database statistics for system, table, index, and column targets.

Key columns: `TYPE`, `TARGET_ID`, `COLUMN_ID`, `DATE`, `SAMPLE_SIZE`, `NUM_ROW_CHANGE`, `NUM_ROW`, `NUM_PAGE`, `NUM_DIST`, `NUM_NULL`, `AVG_LEN`, `ONE_ROW_READ_TIME`, `AVG_SLOT_COUNT`, `INDEX_HEIGHT`, `CLUSTERING_FACTOR`, `SREAD_TIME`, `MREAD_TIME`, `MREAD_PAGE_COUNT`, `HASH_TIME`, `COMPARE_TIME`, `STORE_TIME`, `MIN`, `MAX`, `META_SPACE`, `USED_SPACE`, `AGEABLE_SPACE`, `FREE_SPACE`.

Type values: `S` = system, `T` = table, `I` = index, `C` = column.

Representative SQL:

```sql
SELECT type,
       target_id,
       column_id,
       date,
       sample_size,
       num_row_change,
       num_row,
       num_page,
       num_dist,
       avg_slot_count,
       index_height,
       clustering_factor
FROM V$DBMS_STATS
ORDER BY type, target_id, column_id;
```

### Object Block: `V$LOCK_TABLE_STATS`

Purpose: shows whether table statistics are locked.

Key columns: `TABLE_OID`, `STAT_LOCKED`.

Value notes: `STAT_LOCKED` is `NONE` when table statistics are unlocked and `LOCKED` when they are locked.

Representative SQL:

```sql
SELECT u.user_name, t.table_name, l.stat_locked
FROM V$LOCK_TABLE_STATS l,
     SYSTEM_.SYS_TABLES_ t,
     SYSTEM_.SYS_USERS_ u
WHERE l.table_oid = t.table_oid
  AND t.user_id = u.user_id
ORDER BY u.user_name, t.table_name;
```

### Object Block: `SYSTEM_.SYS_REPLICATIONS_`, `SYSTEM_.SYS_REPL_HOSTS_`, and `SYSTEM_.SYS_REPL_ITEMS_`

Purpose: store replication definitions, hosts, and replicated items.

Key columns: `REPLICATION_NAME`, `IS_STARTED`, `XSN`, `ITEM_COUNT`, `REPL_MODE`, `OPTIONS`, `HOST_IP`, `PORT_NO`, `LOCAL_USER_NAME`, `LOCAL_TABLE_NAME`, `REMOTE_USER_NAME`, `REMOTE_TABLE_NAME`.

Representative SQL:

```sql
SELECT replication_name, is_started, xsn, item_count, repl_mode, options
FROM SYSTEM_.SYS_REPLICATIONS_
ORDER BY replication_name;
```

### Object Block: `V$REPGAP`, `V$REPSYNC`, `V$REPSENDER`, and `V$REPRECEIVER`

Purpose: show replication runtime gap, synchronization progress, sender state, receiver state, network error flag, and apply counters.

Key columns: `REP_NAME`, `REP_GAP`, `REP_GAP_SIZE`, `SYNC_TABLE`, `SYNC_PARTITION`, `SYNC_RECORD_COUNT`, `STATUS`, `NET_ERROR_FLAG`, `XSN`, `COMMIT_XSN`, `APPLY_XSN`, `INSERT_FAILURE_COUNT`, `UPDATE_FAILURE_COUNT`, `DELETE_FAILURE_COUNT`.

Representative SQL:

```sql
SELECT rep_name, rep_gap, rep_gap_size, read_file_no, read_offset
FROM V$REPGAP
ORDER BY rep_name;

SELECT rep_name, sync_table, sync_partition, sync_record_count
FROM V$REPSYNC
ORDER BY rep_name, sync_table, sync_partition;
```

### Object Block: `V$DATABASE`

Purpose: shows memory database identity, product and database signatures, storage-manager version, log file size, transaction table size, memory database page counts, and maximum accessible file size.

Version scope: common to 7.1, 7.3, and the Altibase 8.1 verified source.

Key columns: `DB_NAME`, `PRODUCT_SIGNATURE`, `DB_SIGNATURE`, `VERSION_ID`, `COMPILE_BIT`, `ENDIAN`, `LOGFILE_SIZE`, `TX_TBL_SIZE`, `DURABLE_SYSTEM_SCN`, `MEM_MAX_DB_SIZE`, `MEM_ALLOC_PAGE_COUNT`, `MEM_FREE_PAGE_COUNT`, `MAX_ACCESS_FILE_SIZ`.

Representative SQL:

```sql
SELECT db_name,
       version_id,
       logfile_size,
       tx_tbl_size,
       durable_system_scn,
       mem_max_db_size,
       mem_alloc_page_count,
       mem_free_page_count
FROM V$DATABASE;
```

Caution: `MEM_ALLOC_PAGE_COUNT` and `MEM_FREE_PAGE_COUNT` describe current memory database space, not the maximum possible size. The General Reference states that memory database page size is 32 KB when converting these counts.

### Object Block: `V$TABLESPACES`

Purpose: shows tablespace identity, type, state, extent/segment management, datafile count, page counts, page size, and log-compression attribute.

Version scope: common to 7.1, 7.3, and the Altibase 8.1 verified source.

Key columns: `ID`, `NAME`, `NEXT_FILE_ID`, `TYPE`, `STATE`, `EXTENT_MANAGEMENT`, `SEGMENT_MANAGEMENT`, `DATAFILE_COUNT`, `TOTAL_PAGE_COUNT`, `EXTENT_PAGE_COUNT`, `ALLOCATED_PAGE_COUNT`, `PAGE_SIZE`, `ATTR_LOG_COMPRESS`.

Representative SQL:

```sql
SELECT id,
       name,
       type,
       state,
       datafile_count,
       total_page_count,
       allocated_page_count,
       page_size,
       total_page_count * page_size AS total_bytes,
       attr_log_compress
FROM V$TABLESPACES
ORDER BY id;
```

Caution: Do not turn a `STATE` code into operational advice until the tablespace type, backup status, and requested action are known. For DDL generation, use `03_sql_ddl_generation.md`; for runbooks, use `02_administration_operations.md`.

### Object Block: `V$DATAFILES`

Purpose: shows disk datafile path, owning tablespace, creation and oldest checkpoint LSN pieces, autoextend sizes, current size, I/O-open state, modified state, and file status.

Version scope: common to 7.1, 7.3, and the Altibase 8.1 verified source.

Key columns: `ID`, `NAME`, `SPACEID`, `OLDEST_LSN_FILENO`, `OLDEST_LSN_OFFSET`, `CREATE_LSN_FILENO`, `CREATE_LSN_OFFSET`, `SM_VERSION`, `NEXTSIZE`, `MAXSIZE`, `INITSIZE`, `CURRSIZE`, `AUTOEXTEND`, `IOCOUNT`, `OPENED`, `MODIFIED`, `STATE`, `MAX_OPEN_FD_COUNT`, `CUR_OPEN_FD_COUNT`.

Representative SQL:

```sql
SELECT d.id,
       d.name,
       d.spaceid,
       t.name AS tablespace_name,
       d.currsize * t.page_size AS currsize_bytes,
       d.nextsize * t.page_size AS nextsize_bytes,
       d.maxsize * t.page_size AS maxsize_bytes,
       d.autoextend,
       d.opened,
       d.modified,
       d.state
FROM V$DATAFILES d,
     V$TABLESPACES t
WHERE d.spaceid = t.id
ORDER BY d.spaceid, d.id;
```

Caution: `INITSIZE`, `CURRSIZE`, `NEXTSIZE`, and `MAXSIZE` are page counts in the datafile view; multiply by `V$TABLESPACES.PAGE_SIZE` before reporting bytes.

### Object Block: `V$MEM_TABLESPACES`, `V$MEM_TABLESPACE_CHECKPOINT_PATHS`, and `V$MEM_TABLESPACE_STATUS_DESC`

Purpose: show memory tablespace size, free pages, autoextend state, restore/load mode, ping-pong checkpoint group, checkpoint image paths, and status-code descriptions.

Version scope: common to 7.1, 7.3, and the Altibase 8.1 verified source; 8.1 adds checkpoint-scale interpretation with `V$LOG.CHECKPOINT_SCALE` and `V$MEM_STABLE`.

Key columns: `SPACE_ID`, `SPACE_NAME`, `SPACE_STATUS`, `STATUS_DESC`, `AUTOEXTEND_MODE`, `AUTOEXTEND_NEXTSIZE`, `MAXSIZE`, `CURRENT_SIZE`, `DBFILE_SIZE`, `DBFILE_COUNT_0`, `DBFILE_COUNT_1`, `ALLOC_PAGE_COUNT`, `FREE_PAGE_COUNT`, `RESTORE_TYPE`, `CURRENT_DB`, `HIGH_LIMIT_PAGE`, `PAGE_COUNT_PER_FILE`, `PAGE_COUNT_IN_DISK`, `CHECKPOINT_PATH`.

Representative SQL:

```sql
SELECT m.space_id,
       m.space_name,
       s.status_desc,
       m.current_size,
       m.alloc_page_count,
       m.free_page_count,
       m.current_db,
       p.checkpoint_path
FROM V$MEM_TABLESPACES m,
     V$MEM_TABLESPACE_STATUS_DESC s,
     V$MEM_TABLESPACE_CHECKPOINT_PATHS p
WHERE m.space_status = s.status
  AND m.space_id = p.space_id
ORDER BY m.space_id, p.checkpoint_path;
```

Caution: `RESTORE_TYPE` values distinguish dynamic memory, shared-memory create, and shared-memory attach load behavior. Ask for the exact startup mode and tablespace name before interpreting it as a failure.

### Object Block: `V$VOL_TABLESPACES`

Purpose: shows volatile tablespace identity, status, initial/current/max sizes, autoextend settings, and free pages.

Version scope: common to 7.1, 7.3, and the Altibase 8.1 verified source.

Key columns: `SPACE_ID`, `SPACE_NAME`, `SPACE_STATUS`, `INIT_SIZE`, `AUTOEXTEND_MODE`, `NEXT_SIZE`, `MAX_SIZE`, `CURRENT_SIZE`, `ALLOC_PAGE_COUNT`, `FREE_PAGE_COUNT`.

Representative SQL:

```sql
SELECT v.space_id,
       v.space_name,
       s.status_desc,
       v.current_size,
       v.max_size,
       v.alloc_page_count,
       v.free_page_count
FROM V$VOL_TABLESPACES v,
     V$MEM_TABLESPACE_STATUS_DESC s
WHERE v.space_status = s.status
ORDER BY v.space_id;
```

Caution: Volatile tablespaces exist in memory and are distinct from memory tablespaces used for persistent memory database image files.

### Object Block: `V$STABLE_MEM_DATAFILES` and `V$MEM_STABLE`

Purpose: `V$STABLE_MEM_DATAFILES` lists full paths for stable memory data files. `V$MEM_STABLE` shows the stable checkpoint image file number and ping-pong value for memory tablespaces.

Version scope: `V$STABLE_MEM_DATAFILES` is common to 7.1, 7.3, and the Altibase 8.1 verified source. `V$MEM_STABLE` is an Altibase 8.1 verified source view listed in the 8.1 release notes and Korean General Reference 2.

Key columns: `MEM_DATA_FILE`, `SPACE_ID`, `SPACE_NAME`, `FILE_NUM`, `CURRENT_DB`.

Representative SQL:

```sql
SELECT mem_data_file
FROM V$STABLE_MEM_DATAFILES
ORDER BY mem_data_file;

SELECT space_id, space_name, file_num, current_db
FROM V$MEM_STABLE
ORDER BY space_id, file_num;
```

Caution: Check `V$TABLE` before querying `V$MEM_STABLE` on non-8.1 targets. In 8.1, use it with `V$LOG.CHECKPOINT_SCALE`; when checkpoint scale is `PAIR`, the stable file number can be inferred from file number `0`, and when it is `SINGLE`, all stable checkpoint image files are listed.

### Object Block: `V$LOG` and `V$LFG`

Purpose: `V$LOG` shows log-anchor checkpoint positions, server status, archive log mode, transaction segment count, oldest restart-redo log position, and 8.1 checkpoint scale. `V$LFG` shows log file group and group-commit statistics.

Version scope: common log-anchor columns are in 7.1, 7.3, and the Altibase 8.1 verified source. `V$LOG.CHECKPOINT_SCALE` is Altibase 8.1 verified source.

Key columns: `BEGIN_CHKPT_FILE_NO`, `BEGIN_CHKPT_FILE_OFFSET`, `END_CHKPT_FILE_NO`, `END_CHKPT_FILE_OFFSET`, `SERVER_STATUS`, `ARCHIVELOG_MODE`, `TRANSACTION_SEGMENT_COUNT`, `OLDEST_LOGFILE_NO`, `OLDEST_LOGFILE_OFFSET`, `CHECKPOINT_SCALE`, `CUR_WRITE_LF_NO`, `CUR_WRITE_LF_OFFSET`, `LF_PREPARE_COUNT`, `LF_PREPARE_WAIT_COUNT`, `END_LSN_FILE_NO`, `END_LSN_OFFSET`, `FIRST_DELETED_LOGFILE`, `LAST_DELETED_LOGFILE`, `GC_WAIT_COUNT`, `GC_REAL_SYNC_COUNT`.

Representative SQL:

```sql
SELECT server_status,
       archivelog_mode,
       begin_chkpt_file_no,
       end_chkpt_file_no,
       oldest_logfile_no,
       transaction_segment_count
FROM V$LOG;

SELECT lfg_id,
       cur_write_lf_no,
       cur_write_lf_offset,
       lf_prepare_wait_count,
       gc_wait_count,
       gc_real_sync_count
FROM V$LFG
ORDER BY lfg_id;
```

Caution: Do not include `CHECKPOINT_SCALE` in portable 7.1/7.3 SQL unless `V$ALLCOLUMN` proves the target exposes it.

### Object Block: `V$ARCHIVE`

Purpose: shows archive log mode and archiver progress for each log file group.

Version scope: common to 7.1, 7.3, and the Altibase 8.1 verified source.

Key columns: `LFG_ID`, `ARCHIVE_MODE`, `ARCHIVE_THR_RUNNING`, `ARCHIVE_DEST`, `NEXTLOGFILE_TO_ARCH`, `OLDEST_ACTIVE_LOGFILE`, `CURRENT_LOGFILE`.

Representative SQL:

```sql
SELECT lfg_id,
       archive_mode,
       archive_thr_running,
       archive_dest,
       nextlogfile_to_arch,
       oldest_active_logfile,
       current_logfile
FROM V$ARCHIVE
ORDER BY lfg_id;
```

Caution: `ARCHIVE_MODE` values are numeric in `V$ARCHIVE` (`0` no archive log mode, `1` archive log mode), while `V$LOG.ARCHIVELOG_MODE` exposes character values such as `ARCHIVE` and `NOARCHIVE`.

### Object Block: `V$BACKUP_INFO` and `V$OBSOLETE_BACKUP_INFO`

Purpose: show incremental-backup catalog records and backup records that are no longer required to be retained.

Version scope: common to 7.1, 7.3, and the Altibase 8.1 verified source.

Key columns: `BEGIN_BACKUP_TIME`, `END_BACKUP_TIME`, `INCREMENTAL_BACKUP_CHUNK_COUNT`, `BACKUP_TARGET`, `BACKUP_LEVEL`, `BACKUP_TYPE`, `TABLESPACE_ID`, `FILE_ID`, `BACKUP_TAG`, `BACKUP_FILE`.

Representative SQL:

```sql
SELECT begin_backup_time,
       end_backup_time,
       backup_target,
       backup_level,
       backup_type,
       tablespace_id,
       file_id,
       backup_tag,
       backup_file
FROM V$BACKUP_INFO
ORDER BY begin_backup_time, backup_file;
```

Caution: `V$OBSOLETE_BACKUP_INFO` uses the same column family as `V$BACKUP_INFO`. Treat it as retention evidence, not as permission to remove files without a recovery objective and current backup policy.

### Object Block: `V$FILESTAT`

Purpose: shows cumulative read/write I/O counters and timings for each disk datafile since server start.

Version scope: common to 7.1, 7.3, and the Altibase 8.1 verified source.

Key columns: `SPACEID`, `FILEID`, `PHYRDS`, `PHYWRTS`, `PHYBLKRD`, `PHYBLKWRT`, `SINGLEBLKRDS`, `READTIM`, `WRITETIM`, `SINGLEBLKRDTIM`, `AVGIOTIM`, `LSTIOTIM`, `MINIOTIM`, `MAXIORTM`, `MAXIOWTM`.

Representative SQL:

```sql
SELECT f.spaceid,
       f.fileid,
       f.phyrds,
       f.phywrts,
       f.readtim,
       f.writetim,
       f.avgiotim,
       d.name AS datafile_name
FROM V$FILESTAT f,
     V$DATAFILES d
WHERE f.spaceid = d.spaceid
  AND f.fileid = d.id
ORDER BY f.avgiotim DESC, f.spaceid, f.fileid;
```

Caution: These are cumulative counters. Compare intervals or use OS storage data before diagnosing a storage device bottleneck.

### Object Block: `V$SNAPSHOT`

Purpose: shows `BEGIN SNAPSHOT` SCN, begin/current times, and memory/disk undo usage ratios for snapshot-based operations such as export.

Version scope: common to 7.1, 7.3, and the Altibase 8.1 verified source.

Key columns: `SCN`, `BEGIN_TIME`, `BEGIN_MEM_USAGE`, `BEGIN_DISK_UNDO_USAGE`, `CURRENT_TIME`, `CURRENT_MEM_USAGE`, `CURRENT_DISK_UNDO_USAGE`.

Representative SQL:

```sql
SELECT scn,
       begin_time,
       begin_mem_usage,
       begin_disk_undo_usage,
       current_time,
       current_mem_usage,
       current_disk_undo_usage
FROM V$SNAPSHOT;
```

Caution: When the user asks about snapshot retention or undo pressure, ask for the export/snapshot command, elapsed time, and current undo-space evidence before recommending cleanup.

### Object Block: `V$TRACELOG`

Purpose: shows message logging modules, trace levels, enabled flags, power-of-two bit values, and descriptions.

Version scope: common to 7.1, 7.3, and the Altibase 8.1 verified source.

Key columns: `MODULE_NAME`, `TRCLEVEL`, `FLAG`, `POWLEVEL`, `DESCRIPTION`.

Representative SQL:

```sql
SELECT module_name,
       trclevel,
       flag,
       powlevel,
       description
FROM V$TRACELOG
WHERE module_name IN ('SM', 'SERVER', 'RP')
ORDER BY module_name, trclevel;
```

Caution: `FLAG = SUM` is the combined power-level row for a module. Change `*_MSGLOG_FLAG` properties only with a clear support or diagnostic purpose.

### Object Block: `V$TEMPORARY_LOBS`

Purpose: shows Temporary LOB allocation and open-count state.

Version scope: Altibase 8.1 verified source. The Korean General Reference 2 and 8.1 release notes list this view; the checked English General Reference 2 list did not.

Key columns: `TYPE`, `ID`, `ALLOCED_SIZE`, `OPEN_COUNT`.

Representative SQL:

```sql
SELECT type, id, alloced_size, open_count
FROM V$TEMPORARY_LOBS
ORDER BY type, id;
```

Caution: `TYPE = 0` is a transaction Temporary LOB and `TYPE = 1` is a session Temporary LOB. Check `TEMPORARY_LOB_ENABLE` and related properties before interpreting usage.

## Attachment Cross-References

- Use `02_administration_operations.md` when dictionary or performance-view evidence leads to tablespace, backup, recovery, startup, or shutdown action.
- Use `03_sql_ddl_generation.md` when metadata lookup must turn into corrected DDL for objects, privileges, indexes, partitions, sequences, or replication.
- Use `05_data_types_properties.md` when a storage, log, backup, checkpoint, or Temporary LOB answer depends on a property value, range, dynamic-change support, or restart rule.
- Use `07_error_messages_troubleshooting.md` when the view query is part of an error-code response or log-message triage.
- Use `08_performance_tuning_monitoring.md` for deeper interpretation of sessions, statements, waits, locks, plan cache, statistics, and server bottlenecks.
- Use `09_replication_ha_cdc.md` for replication topology, mode, failover, gap, Sender, Receiver, and CDC interpretation after view lookup.
- Use `16_dblink_external_connectors.md` when metadata or runtime checks involve database links, AltiLinker, remote statements, or global transactions.

## Answer Templates

### Template: Object Metadata Request

Use this when the user asks "show columns/indexes/constraints for table X":

1. Identify owner and object name.
2. Query `SYSTEM_.SYS_TABLES_` for object identity and `TABLE_TYPE`.
3. Query `SYSTEM_.SYS_COLUMNS_`.
4. Query `SYSTEM_.SYS_INDICES_` plus `SYSTEM_.SYS_INDEX_COLUMNS_`.
5. Query `SYSTEM_.SYS_CONSTRAINTS_` plus `SYSTEM_.SYS_CONSTRAINT_COLUMNS_`.
6. Explain code values only when they affect the answer.

### Template: Runtime Performance Request

Use this when the user asks "what is running/blocked/slow":

1. Query `V$SESSION`.
2. Query `V$STATEMENT` and `V$SQLTEXT`.
3. Query `V$SESSION_WAIT`.
4. Query `V$LOCK_WAIT` and `V$LOCK_STATEMENT` if blocking is suspected.
5. Query `V$TRANSACTION` when transaction state or update size matters.
6. Map the observed condition to the relevant response block in `07_error_messages_troubleshooting.md` or `08_performance_tuning_monitoring.md` before recommending an action.

### Template: Replication Health Request

Use this when the user asks "is replication delayed or failing":

1. Query `SYSTEM_.SYS_REPLICATIONS_`, `SYSTEM_.SYS_REPL_HOSTS_`, and `SYSTEM_.SYS_REPL_ITEMS_`.
2. Query `V$REPEXEC`.
3. Query `V$REPGAP` or `V$REPGAP_PARALLEL`.
4. If `SYNC` or `SYNC ONLY` is running, query `V$REPSYNC`.
5. Query `V$REPSENDER` and `V$REPRECEIVER`.
6. Treat `NET_ERROR_FLAG = 1`, large `REP_GAP_SIZE`, and receiver failure counts as investigation triggers.
7. Map the observed condition to the relevant response block in `07_error_messages_troubleshooting.md` or `08_performance_tuning_monitoring.md` before recommending an action.

### Template: Storage, Backup, or Archive Request

Use this when the user asks "is there enough space", "is archive log enabled", "which backup exists", or "which datafile is hot":

1. Query `V$VERSION` when version-sensitive columns or 8.1-only checkpoint/Temporary LOB views may be used.
2. Query `V$TABLESPACES`, `V$DATAFILES`, `V$MEM_TABLESPACES`, and `V$VOL_TABLESPACES` for storage layout and state.
3. Query `V$LOG`, `V$LFG`, and `V$ARCHIVE` for log-anchor, log-file-group, archive mode, and archive progress evidence.
4. Query `V$BACKUP_INFO` and `V$OBSOLETE_BACKUP_INFO` for backup catalog evidence.
5. Query `V$FILESTAT` for cumulative datafile I/O evidence and pair it with OS storage data before concluding that storage is slow or faulty.
6. For 8.1 checkpoint-scale questions, verify `V$LOG.CHECKPOINT_SCALE` and `V$MEM_STABLE` availability with `V$ALLCOLUMN` and `V$TABLE`.
7. Route any corrective action to `02_administration_operations.md` or SQL generation to `03_sql_ddl_generation.md`; keep this file as the evidence-gathering source.

### Template: Version-Sensitive 8.1 Request

Use this when the user asks about 8.1 dictionary or performance view changes:

1. Query `V$VERSION`.
2. Query `V$TABLE` for `V$MEM_STABLE`, `V$TEMPORARY_LOBS`, and `V$LOCK_TABLE_STATS`.
3. Query `V$ALLCOLUMN` for the exact columns before generating version-specific SQL.
4. For Temporary LOB, also query `V$PROPERTY` for `TEMPORARY_LOB_ENABLE`, `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`, and `MEMORY_TEMPLOB_PIECE_SIZE`.

## Residual Scope

- Cookbook queries and searchable object blocks cover common dictionary and performance-view questions. They are not a full column-by-column catalog; for an exact view layout, query `V$ALLCOLUMN` or the target-version dictionary source before generating final SQL.
