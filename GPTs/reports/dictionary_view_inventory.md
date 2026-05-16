# Altibase Dictionary And Performance View Inventory Baseline

Job: `J017`
Status: Active support artifact
Last updated: 2026-05-17

## Reconfirmed Requirement And Boundary

`J017` inventories dictionary and performance view names, version availability, and
grouping for the supported Altibase 7.1, 7.3, and 8.1 scope. This is a
documentation-scope baseline for later J018-J021 view expansion work. It does not
rename attachments or change the 20-file upload boundary.

Target attachment affected by this job:

- `GPTs/attachments/06_data_dictionary_performance_views.md`

Support artifacts affected by this job:

- `GPTs/reports/dictionary_view_inventory.md`
- `GPTs/reports/source_inventory.md`
- `GPTs/reports/coverage_matrix.md`
- `GPTs/reports/gap_register.md`

## Design Note

This report is the item-name baseline for the `general_reference_2_dictionary_views`
source family. It records grouped names and version availability, but it does not close
the remaining per-column coverage gap. Later jobs should use this report as the first
filter when choosing which view or meta table blocks to expand, then use Korean General
Reference 2 manuals as the authoritative column source and English manuals only for
customer-facing wording when consistent.

Customer-facing attachments should keep compact inventory groups plus portable layout
checks. Support reports may keep internal source paths and source-drift notes.

## Scoped Source Families

- `general_reference_2_dictionary_views`: primary source family for meta tables,
  performance views, descriptions, and column layouts.
- `performance_tuning`: supporting source family for optimizer, plan cache,
  statistics, buffer, wait, and monitoring interpretation.
- `replication_manual`: supporting source family for replication runtime and metadata
  view interpretation.
- `patch_notes` and release notes: supporting source families for patch-level or
  version-introduction cautions.

Korean source paths checked first:

- `Manuals/Altibase_7.1/kor/General Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`
- `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`

English extraction paths checked second:

- `Manuals/Altibase_7.1/eng/General Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_7.3/eng/General Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_trunk/eng/General Reference-2.The Data Dictionary.md`
- `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`

## Extraction Summary

- Korean General Reference 2 manuals were used as the authoritative list source.
- English General Reference 2 manuals were used only to normalize descriptions when the
  English list agreed with the Korean list.
- Meta-table inventory:
  - 7.1 Korean source lists 72 meta tables.
  - 7.3 Korean source lists 72 meta tables.
  - Altibase 8.1 verified Korean source lists 71 meta tables.
  - `SYS_REPL_TABLE_OID_IN_USE_` is listed in 7.1 and 7.3 Korean sources, but not in
    the Altibase 8.1 verified Korean source table. The 8.1 release notes state that no
    meta tables were added, deleted, or changed, so customer-facing answers should
    verify installed 8.1 metadata before relying on this table.
- Performance-view inventory:
  - 7.1 Korean source lists 128 performance views.
  - 7.3 Korean source lists 125 performance views.
  - Altibase 8.1 verified Korean source lists 127 performance views.
  - 125 performance views are common to 7.1, 7.3, and the Altibase 8.1 verified
    source.
  - `V$MEM_STABLE` and `V$TEMPORARY_LOBS` are Altibase 8.1 verified source views.
  - `V$ST_ANGULAR_UNIT`, `V$ST_AREA_UNIT`, and `V$ST_LINEAR_UNIT` are listed in the
    7.1 Korean source as reserved spatial unit views and are not listed in the 7.3 or
    8.1 Korean source tables.
  - `V$LOCK_TABLE_STATS` is documented in 7.1 and 7.3 Korean General Reference 2 and
    is also listed in the 8.1 release notes. The attachment should continue to advise a
    `V$TABLE` existence check before relying on version-sensitive views.

## Source Drift Notes

- `V$QUEUE_DELETE_OFF` is listed in Korean General Reference 2 for 7.1, 7.3, and the
  Altibase 8.1 verified source, but it is absent from the corresponding English
  performance-view list. Use the Korean source and keep the name in customer-facing
  inventory.
- `V$TEMPORARY_LOBS` is listed in the Altibase 8.1 verified Korean source and 8.1
  release notes, but not in the checked English General Reference 2 list. Use the
  Korean source and release note.
- `V$ST_ANGULAR_UNIT`, `V$ST_AREA_UNIT`, and `V$ST_LINEAR_UNIT` appear in checked
  English 7.3/8.1 lists but not in the corresponding Korean 7.3/8.1 lists. Treat them
  as 7.1 Korean-source-only reserved views unless a later selected source proves wider
  availability.
- `SYS_REPL_TABLE_OID_IN_USE_` has an 8.1 source conflict as noted above. This is
  recorded in `GAP-J017-001`.

## Meta Table Inventory Groups

Version note: every listed meta table is common to 7.1, 7.3, and the Altibase 8.1
verified source unless the row explicitly names an exception.

| Group | Names | Version availability and use |
| --- | --- | --- |
| Audit and security | `SYS_AUDIT_`, `SYS_AUDIT_OPTS_`, `SYS_SECURITY_`, `SYS_ENCRYPTED_COLUMNS_` | Common inventory group for auditing state, audit options, security module metadata, and encrypted column metadata. |
| Core database and internal support | `SYS_DATABASE_`, `SYS_DN_USERS_`, `SYS_DUMMY_` | Common inventory group for database identity/version and internal or reserved support tables. |
| Objects, columns, comments, LOBs, and size | `SYS_TABLES_`, `SYS_COLUMNS_`, `SYS_COMMENTS_`, `SYS_COMPRESSION_TABLES_`, `SYS_LOBS_`, `SYS_TABLE_SIZE_`, `SYS_RECYCLEBIN_` | Common inventory group for table-like objects, column layout, comments, compression, LOB metadata, object size, and recycle-bin metadata. |
| Constraints, indexes, and partitions | `SYS_CONSTRAINTS_`, `SYS_CONSTRAINT_COLUMNS_`, `SYS_CONSTRAINT_RELATED_`, `SYS_INDICES_`, `SYS_INDEX_COLUMNS_`, `SYS_INDEX_PARTITIONS_`, `SYS_INDEX_RELATED_`, `SYS_PART_INDICES_`, `SYS_PART_KEY_COLUMNS_`, `SYS_PART_LOBS_`, `SYS_PART_TABLES_`, `SYS_TABLE_PARTITIONS_` | Common inventory group for constraint, index, function-based-index, and partition metadata. |
| Users, roles, privileges, passwords, and tablespace access | `SYS_USERS_`, `DBA_USERS_`, `SYS_USER_ROLES_`, `SYS_PRIVILEGES_`, `SYS_GRANT_SYSTEM_`, `SYS_GRANT_OBJECT_`, `SYS_TBS_USERS_`, `SYS_PASSWORD_HISTORY_`, `SYS_PASSWORD_LIMITS_` | Common inventory group for users, roles, grants, password policy/history, and user tablespace access. |
| Procedures, packages, views, triggers, jobs, and schema helpers | `SYS_PROCEDURES_`, `SYS_PROC_PARAS_`, `SYS_PROC_PARSE_`, `SYS_PROC_RELATED_`, `SYS_PACKAGES_`, `SYS_PACKAGE_PARAS_`, `SYS_PACKAGE_PARSE_`, `SYS_PACKAGE_RELATED_`, `SYS_DIRECTORIES_`, `SYS_LIBRARIES_`, `SYS_MATERIALIZED_VIEWS_`, `SYS_SYNONYMS_`, `SYS_VIEWS_`, `SYS_VIEW_PARSE_`, `SYS_VIEW_RELATED_`, `SYS_JOBS_`, `SYS_TRIGGERS_`, `SYS_TRIGGER_DML_TABLES_`, `SYS_TRIGGER_STRINGS_`, `SYS_TRIGGER_UPDATE_COLUMNS_` | Common inventory group for PSM, packages, source text, dependencies, directory/library objects, materialized views, synonyms, views, scheduler jobs, and trigger metadata. |
| Replication metadata | `SYS_REPLICATIONS_`, `SYS_REPL_HOSTS_`, `SYS_REPL_ITEMS_`, `SYS_REPL_OFFLINE_DIR_`, `SYS_REPL_OLD_CHECKS_`, `SYS_REPL_OLD_CHECK_COLUMNS_`, `SYS_REPL_OLD_COLUMNS_`, `SYS_REPL_OLD_INDEX_COLUMNS_`, `SYS_REPL_OLD_INDICES_`, `SYS_REPL_OLD_ITEMS_`, `SYS_REPL_RECOVERY_INFOS_`, `SYS_REPL_TABLE_OID_IN_USE_` | All except `SYS_REPL_TABLE_OID_IN_USE_` are common in the checked Korean lists. `SYS_REPL_TABLE_OID_IN_USE_` is listed in 7.1 and 7.3 Korean sources; verify installed 8.1 metadata before relying on it. |
| Database link and distributed transaction metadata | `SYS_DATABASE_LINKS_`, `SYS_XA_HEURISTIC_TRANS_` | Common inventory group for database link objects and global/distributed transaction metadata. |
| Spatial metadata | `SYS_GEOMETRIES_`, `SYS_GEOMETRY_COLUMNS_`, `USER_SRS_` | Common inventory group for `GEOMETRY` column metadata and spatial reference system metadata. |

## Performance View Inventory Groups

Version note: every listed performance view is common to 7.1, 7.3, and the Altibase
8.1 verified source unless the row explicitly names an exception. For generated SQL,
check existence with `V$TABLE` and check columns with `V$ALLCOLUMN`.

| Group | Names | Version availability and use |
| --- | --- | --- |
| Inventory, catalog, properties, NLS, and object metadata | `V$TABLE`, `V$ALLCOLUMN`, `V$CATALOG`, `V$DATATYPE`, `V$PROPERTY`, `V$VERSION`, `V$TIME_ZONE_NAMES`, `V$NLS_PARAMETERS`, `V$NLS_TERRITORY`, `V$QUEUE_DELETE_OFF`, `V$SEQ`, `V$EXTPROC_AGENT` | Common inventory group for performance-view discovery, catalog/type/property/version lookup, NLS and time zone lookup, queue `DELETE OFF` state, sequence state, and external-procedure agent state. |
| Server access, sessions, statements, text, and service threads | `V$ACCESS_LIST`, `V$DB_PROTOCOL`, `V$INSTANCE`, `V$SESSION`, `V$INTERNAL_SESSION`, `V$SESSIONMGR`, `V$STATEMENT`, `V$SQLTEXT`, `V$PLANTEXT`, `V$PROCTEXT`, `V$PKGTEXT`, `V$SERVICE_THREAD`, `V$SERVICE_THREAD_MGR` | Common inventory group for access control, protocol flow, startup state, client/internal sessions, running statements, SQL/plan/procedure/package text, and service-thread state. |
| Wait events, locks, transactions, and distributed transaction state | `V$EVENT_NAME`, `V$WAIT_CLASS_NAME`, `V$SESSION_EVENT`, `V$SESSION_WAIT`, `V$SESSION_WAIT_CLASS`, `V$SYSTEM_EVENT`, `V$SYSTEM_WAIT_CLASS`, `V$SYSTEM_CONFLICT_PAGE`, `V$LATCH`, `V$MUTEX`, `V$LOCK`, `V$LOCK_WAIT`, `V$LOCK_STATEMENT`, `V$LOCK_TABLE_STATS`, `V$TRANSACTION`, `V$TRANSACTION_MGR`, `V$DBA_2PC_PENDING`, `V$XID` | Common inventory group for waits, wait classes, latch/page conflicts, mutexes, lock holders/waiters, table-statistic lock state, transactions, and distributed transaction branches. `V$LOCK_TABLE_STATS` is documented in 7.1/7.3 and also listed in 8.1 release notes. |
| System/session statistics, memory, and process counters | `V$STATNAME`, `V$SYSSTAT`, `V$SESSTAT`, `V$MEMSTAT`, `V$MEMGC` | Common inventory group for statistic name/value lookup, system/session counters, module memory usage, and memory garbage collection state. |
| Tablespaces, files, logs, backup, archive, and checkpoint state | `V$DATABASE`, `V$TABLESPACES`, `V$MEM_TABLESPACES`, `V$VOL_TABLESPACES`, `V$DATAFILES`, `V$STABLE_MEM_DATAFILES`, `V$MEM_TABLESPACE_CHECKPOINT_PATHS`, `V$MEM_TABLESPACE_STATUS_DESC`, `V$MEM_STABLE`, `V$ARCHIVE`, `V$BACKUP_INFO`, `V$OBSOLETE_BACKUP_INFO`, `V$LOG`, `V$LFG`, `V$FILESTAT`, `V$TRACELOG`, `V$SNAPSHOT`, `V$TEMPORARY_LOBS` | Common group for storage, tablespace, datafile, checkpoint, archive, backup, log, trace, and snapshot state, except `V$MEM_STABLE` and `V$TEMPORARY_LOBS`, which are Altibase 8.1 verified source views. |
| Table, index, segment, space, and temporary storage internals | `V$MEMTBL_INFO`, `V$DISKTBL_INFO`, `V$INDEX`, `V$MEM_BTREE_HEADER`, `V$MEM_BTREE_NODEPOOL`, `V$DISK_BTREE_HEADER`, `V$DISK_RTREE_HEADER`, `V$MEM_RTREE_HEADER`, `V$MEM_RTREE_NODEPOOL`, `V$SEGMENT`, `V$USAGE`, `V$DB_FREEPAGELISTS`, `V$TSSEGS`, `V$TXSEGS`, `V$UDSEGS`, `V$DISK_UNDO_USAGE`, `V$DISK_TEMP_INFO`, `V$DISK_TEMP_STAT`, `V$DIRECT_PATH_INSERT` | Common inventory group for table/index internals, segment and space usage, page/free-list state, undo/TSS/TX/UD segments, disk temporary tables, and direct-path insert statistics. |
| Buffer pool, secondary buffer, and flush statistics | `V$BUFFPAGEINFO`, `V$BUFFPOOL_STAT`, `V$UNDO_BUFF_STAT`, `V$SBUFFER_STAT`, `V$FLUSHER`, `V$FLUSHINFO`, `V$SFLUSHER`, `V$SFLUSHINFO` | Common inventory group for buffer pool, undo buffer, secondary buffer, flusher, and flush information. |
| Optimizer statistics and SQL plan cache | `V$DBMS_STATS`, `V$SQL_PLAN_CACHE`, `V$SQL_PLAN_CACHE_PCO`, `V$SQL_PLAN_CACHE_SQLTEXT` | Common inventory group for collected statistics and SQL plan cache size, objects, and cached SQL text. |
| Replication runtime and recovery | `V$REPEXEC`, `V$REPGAP`, `V$REPGAP_PARALLEL`, `V$REPLOGBUFFER`, `V$REPOFFLINE_STATUS`, `V$REPRECEIVER`, `V$REPRECEIVER_COLUMN`, `V$REPRECEIVER_PARALLEL`, `V$REPRECEIVER_PARALLEL_APPLY`, `V$REPRECEIVER_STATISTICS`, `V$REPRECEIVER_TRANSTBL`, `V$REPRECEIVER_TRANSTBL_PARALLEL`, `V$REPRECOVERY`, `V$REPSENDER`, `V$REPSENDER_PARALLEL`, `V$REPSENDER_SENT_LOG_COUNT`, `V$REPSENDER_SENT_LOG_COUNT_PARALLEL`, `V$REPSENDER_STATISTICS`, `V$REPSENDER_TRANSTBL`, `V$REPSENDER_TRANSTBL_PARALLEL`, `V$REPSYNC` | Common inventory group for replication manager state, gap, parallel gap, log buffer, offline status, receiver/sender state, replication columns, statistics, transaction tables, recovery, sent-log counts, and synchronization. |
| Database link runtime | `V$DBLINK_ALTILINKER_STATUS`, `V$DBLINK_DATABASE_LINK_INFO`, `V$DBLINK_GLOBAL_TRANSACTION_INFO`, `V$DBLINK_LINKER_CONTROL_SESSION_INFO`, `V$DBLINK_LINKER_DATA_SESSION_INFO`, `V$DBLINK_LINKER_SESSION_INFO`, `V$DBLINK_NOTIFIER_TRANSACTION_INFO`, `V$DBLINK_REMOTE_STATEMENT_INFO`, `V$DBLINK_REMOTE_TRANSACTION_INFO` | Common inventory group for AltiLinker status, database link objects, global transactions, linker sessions, notifier transactions, remote statements, and remote transactions. |
| Spatial unit catalog | `V$ST_ANGULAR_UNIT`, `V$ST_AREA_UNIT`, `V$ST_LINEAR_UNIT` | Listed in the 7.1 Korean source as reserved spatial unit views. Not listed in the 7.3 or 8.1 Korean performance-view tables; check `V$TABLE` before using on later versions. |

## Portable Verification SQL

Use the following pattern before generating final SQL for version-sensitive or
patch-sensitive objects:

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

## Later-Job Handoff

- J018 should use the storage, tablespace, file, log, archive, backup, checkpoint, and
  temporary LOB groups as the source-name baseline.
- J019 should use the server/session/statement, wait/lock/transaction, and statistic
  groups as the source-name baseline.
- J020 should use the optimizer statistics, SQL plan cache, buffer, memory, table/index,
  segment, and space groups as the source-name baseline.
- J021 should use the replication, database link, security/audit, Monitoring API, SNMP,
  and related runtime groups as the source-name baseline.
- `GAP-J002-006` remains open for exhaustive per-view column blocks. J017 narrows it by
  providing the source-backed name/version/group baseline.
- `GAP-J017-001` records the 8.1 `SYS_REPL_TABLE_OID_IN_USE_` source conflict and
  English/Korean list drift so later jobs do not overstate availability.
