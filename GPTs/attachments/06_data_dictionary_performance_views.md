# 06. Data Dictionary and Performance Views

## Applicable Versions

- 7.1: Based on Altibase 7.1 General Reference 2.
- 7.3: Based on Altibase 7.3 General Reference 2.
- 8.1: Based on Altibase 8.1 verified source General Reference 2 and Altibase 8.1 Release Notes.

## Questions This File Can Answer

- Which meta table or performance view should be queried for a table, index, column, user, privilege, session, lock, transaction, replication, tablespace, property, or plan cache question?
- How do I generate check SQL for a specific object name?
- How do I check running sessions, statements, waits, locks, and replication gap?
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
- 8.1: `V$MEM_STABLE` is documented in the Altibase 8.1 verified source data dictionary and is used with `V$LOG.CHECKPOINT_SCALE` and `V$MEM_TABLESPACES.CURRENT_DB` for memory checkpoint image checks.
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

## Fast Object Map

Use these first when selecting the right source:

| Task | Primary objects |
| --- | --- |
| Product and meta version | `V$VERSION` |
| Properties | `V$PROPERTY` |
| Property effect checks | `V$PROPERTY` plus the related performance view, such as `V$SQL_PLAN_CACHE`, `V$TIME_ZONE_NAMES`, `V$TEMPORARY_LOBS`, or replication views |
| Performance view inventory | `V$TABLE`, `V$ALLCOLUMN` |
| Tables, views, sequences, queues | `SYSTEM_.SYS_TABLES_` |
| Columns | `SYSTEM_.SYS_COLUMNS_` |
| Data type lookup | `V$DATATYPE` |
| Comments | `SYSTEM_.SYS_COMMENTS_` |
| Table size | `SYSTEM_.SYS_TABLE_SIZE_`, `V$USAGE` |
| Partitions | `SYSTEM_.SYS_TABLE_PARTITIONS_`, `SYSTEM_.SYS_PART_TABLES_`, `SYSTEM_.SYS_PART_KEY_COLUMNS_` |
| Indexes | `SYSTEM_.SYS_INDICES_`, `SYSTEM_.SYS_INDEX_COLUMNS_`, `V$INDEX` |
| Constraints | `SYSTEM_.SYS_CONSTRAINTS_`, `SYSTEM_.SYS_CONSTRAINT_COLUMNS_` |
| Users and roles | `SYSTEM_.SYS_USERS_`, `SYSTEM_.DBA_USERS_`, `SYSTEM_.SYS_USER_ROLES_` |
| Privileges | `SYSTEM_.SYS_PRIVILEGES_`, `SYSTEM_.SYS_GRANT_SYSTEM_`, `SYSTEM_.SYS_GRANT_OBJECT_` |
| Tablespaces and datafiles | `V$TABLESPACES`, `V$DATAFILES`, `V$MEM_TABLESPACES`, `V$VOL_TABLESPACES` |
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
| Backup, archive, log, recovery | `V$LOG`, `V$ARCHIVE`, `V$BACKUP_INFO`, `V$DATAFILES` |
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
SELECT space_id,
       space_name,
       space_status,
       autoextend_mode,
       autoextend_nextsize,
       maxsize,
       current_size,
       alloc_page_count,
       free_page_count,
       current_db,
       high_limit_page,
       page_count_per_file,
       page_count_in_disk
FROM V$MEM_TABLESPACES
ORDER BY space_id;
```

### Check 8.1 Stable Checkpoint Image Files

Use this when `V$LOG.CHECKPOINT_SCALE` is `SINGLE`, or when investigating memory checkpoint image file state in 8.1.

```sql
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

### Object Block: `V$SESSION`

Purpose: shows current client sessions.

Key columns: `ID`, `TRANS_ID`, `TASK_STATE`, `SESSION_STATE`, `ACTIVE_FLAG`, `OPENED_STMT_COUNT`, `CURRENT_STMT_ID`, `DB_USERNAME`, `COMM_NAME`, `CLIENT_APP_INFO`, `MODULE`, `ACTION`.

Representative SQL:

```sql
SELECT id, db_username, task_state, session_state, active_flag, current_stmt_id
FROM V$SESSION
ORDER BY id;
```

### Object Block: `V$STATEMENT`

Purpose: shows the most recently executed query information for connected sessions.

Key columns: `ID`, `SESSION_ID`, `TX_ID`, `QUERY`, `EXECUTE_STATE`, `FETCH_STATE`, `TOTAL_TIME`, `PARSE_TIME`, `OPTIMIZE_TIME`, `EXECUTE_TIME`, `FETCH_TIME`, `PROCESS_ROW`, `EVENT`, `WAIT_TIME`.

Representative SQL:

```sql
SELECT session_id, id, execute_state, total_time, process_row, query
FROM V$STATEMENT
ORDER BY total_time DESC;
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

### Column Block: `V$TRANSACTION` Large-View Columns

Purpose: use this searchable column block when a question asks which transaction view column explains transaction identity, session ownership, MVCC view SCNs, status, update size, XA state, undo-log position, DDL flag, disk update slot, or isolation level.

Key columns: identity columns are `ID`, `SESSION_ID`, `SLOT_NO`; MVCC view columns are `MEMORY_VIEW_SCN`, `MIN_MEMORY_LOB_VIEW_SCN`, `DISK_VIEW_SCN`, `MIN_DISK_LOB_VIEW_SCN`, `COMMIT_SCN`; status columns are `STATUS`, `UPDATE_STATUS`, `LOG_TYPE`, `DDL_FLAG`, `ISOLATION_LEVEL`; XA columns are `XA_COMMIT_STATUS`, `XA_PREPARED_TIME`; undo log columns are `FIRST_UNDO_NEXT_LSN_FILENO`, `FIRST_UNDO_NEXT_LSN_OFFSET`, `CURRENT_UNDO_NEXT_SN`, `CURRENT_UNDO_NEXT_LSN_FILENO`, `CURRENT_UNDO_NEXT_LSN_OFFSET`, `LAST_UNDO_NEXT_LSN_FILENO`, `LAST_UNDO_NEXT_LSN_OFFSET`, `LAST_UNDO_NEXT_SN`; update and storage columns are `UPDATE_SIZE`, `FIRST_UPDATE_TIME`, `TSS_RID`, `RESOURCE_GROUP_ID`.

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

### Object Block: `V$LOCK_WAIT`, `V$LOCK`, and `V$LOCK_STATEMENT`

Purpose: show transaction wait chains, lock objects, and statements holding or waiting for locks.

Key columns: `TRANS_ID`, `WAIT_FOR_TRANS_ID`, `LOCK_ITEM_TYPE`, `TABLE_OID`, `LOCK_DESC`, `IS_GRANT`, `SESSION_ID`, `QUERY`.

Representative SQL:

```sql
SELECT trans_id, wait_for_trans_id
FROM V$LOCK_WAIT
ORDER BY wait_for_trans_id, trans_id;
```

### Object Block: `V$SQL_PLAN_CACHE`, `V$SQL_PLAN_CACHE_PCO`, and `V$SQL_PLAN_CACHE_SQLTEXT`

Purpose: show SQL plan cache size, hit/miss counters, plan cache objects, and cached SQL text.

Key columns: `CURRENT_CACHE_SIZE`, `CURRENT_CACHE_OBJ_COUNT`, `CACHE_HIT_COUNT`, `CACHE_MISS_COUNT`, `SQL_TEXT_ID`, `PCO_ID`, `HIT_COUNT`, `REBUILD_COUNT`, `PLAN_STATE`, `PLAN_CACHE_KEEP`, `SQL_TEXT`.

Representative SQL:

```sql
SELECT current_cache_size, current_cache_obj_count, cache_hit_count, cache_miss_count
FROM V$SQL_PLAN_CACHE;
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

### Object Block: `V$TABLESPACES`, `V$DATAFILES`, and `V$MEM_TABLESPACES`

Purpose: show tablespace, datafile, and memory tablespace state.

Key columns: `ID`, `NAME`, `TYPE`, `STATE`, `PAGE_SIZE`, `TOTAL_PAGE_COUNT`, `DATAFILE_COUNT`, `SPACE_ID`, `SPACE_NAME`, `CURRENT_SIZE`, `FREE_PAGE_COUNT`, `CURRENT_DB`.

Representative SQL:

```sql
SELECT id, name, type, state, total_page_count, page_size
FROM V$TABLESPACES
ORDER BY id;
```

### Object Block: `V$TEMPORARY_LOBS`

Purpose: 8.1 Temporary LOB usage check.

Key columns: `TYPE`, `ID`, `ALLOCED_SIZE`, `OPEN_COUNT`.

Representative SQL:

```sql
SELECT type, id, alloced_size, open_count
FROM V$TEMPORARY_LOBS
ORDER BY type, id;
```

## Attachment Cross-References

- Use `02_administration_operations.md` when dictionary or performance-view evidence leads to tablespace, backup, recovery, startup, or shutdown action.
- Use `03_sql_ddl_generation.md` when metadata lookup must turn into corrected DDL for objects, privileges, indexes, partitions, sequences, or replication.
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

### Template: Version-Sensitive 8.1 Request

Use this when the user asks about 8.1 dictionary or performance view changes:

1. Query `V$VERSION`.
2. Query `V$TABLE` for `V$MEM_STABLE`, `V$TEMPORARY_LOBS`, and `V$LOCK_TABLE_STATS`.
3. Query `V$ALLCOLUMN` for the exact columns before generating version-specific SQL.
4. For Temporary LOB, also query `V$PROPERTY` for `TEMPORARY_LOB_ENABLE`, `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`, and `MEMORY_TEMPLOB_PIECE_SIZE`.

## Residual Scope

- Cookbook queries and searchable object blocks cover common dictionary and performance-view questions. They are not a full column-by-column catalog; for an exact view layout, query `V$ALLCOLUMN` or the target-version dictionary source before generating final SQL.
