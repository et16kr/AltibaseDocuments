# Dictionary And Views Playbook

- Playbook ID: `APB-000005`
- Owning job: `S2-J003`
- Validation status: `pass`
- Supported versions: Altibase 7.1, Altibase 7.3, and `Altibase 8.1 verified source`
- Protected topic: no

## Source Routes

| Route | Source IDs | Source-pack block refs | Baseline blocks |
| --- | --- | --- | --- |
| Data dictionary, metadata tables, performance views, and validation checks | `SRC-000057`, `SRC-000026`, `SRC-000121`, `SRC-000090`, `SRC-000181`, `SRC-000151`, `SRC-000072`, `SRC-000134`, `SRC-000194` | `SRC-000057/BLOCK-000521`, `SRC-000026/BLOCK-000520`, `SRC-000121/BLOCK-000523`, `SRC-000090/BLOCK-000522`, `SRC-000181/BLOCK-000525`, `SRC-000151/BLOCK-000524`, `SRC-000072/BLOCK-000884`, `SRC-000134/BLOCK-000886`, `SRC-000194/BLOCK-000888` | `KAE-BLOCK-000273` |
| Performance tuning view route | `SRC-000067`, `SRC-000035`, `SRC-000129`, `SRC-000098`, `SRC-000189`, `SRC-000159` | `SRC-000067/BLOCK-000812`, `SRC-000035/BLOCK-000811`, `SRC-000129/BLOCK-000814`, `SRC-000098/BLOCK-000813`, `SRC-000189/BLOCK-000816`, `SRC-000159/BLOCK-000815` | `KAE-BLOCK-000283` |

Guardrail: `CONF-000005` remains open. This playbook can draft lookup and
validation SQL, but full per-view column lists and exact performance
diagnostic interpretations require the target-version source block and live
environment evidence.

Forbidden assumption note: do not infer Altibase dictionary or performance-view
columns from Oracle, MySQL, PostgreSQL, or ANSI SQL catalog names.

## Required Customer Inputs

Before generating dictionary or performance-view SQL, collect:

- Target Altibase version and patch level.
- The object, schema, table, index, user, role, privilege, property,
  replication, session, lock, SQL, or performance symptom to inspect.
- Candidate view or meta-table names and exact columns needed.
- Runtime state, error message, SQL text, execution plan output, object
  definitions, and expected validation result when the query is diagnostic.
- Whether the query must be portable across 7.1, 7.3, and
  `Altibase 8.1 verified source` or exact to one installed environment.

## Generated Artifacts

This playbook may draft:

- View availability checks with `V$TABLE`.
- Column availability checks with `V$ALLCOLUMN`.
- Object, privilege, user, role, property, replication, and session lookup SQL.
- Performance and troubleshooting validation SQL when exact view and column
  availability is confirmed.
- A "missing input" request when a requested column, view, or diagnostic
  interpretation depends on live environment evidence.

## Procedure

1. Treat General Reference 2 as the source for data dictionary and performance
   view names, descriptions, and columns. Do not write DML against performance
   views; use `SELECT`.
2. Verify the view or meta table before writing a column-level query. Use
   `V$TABLE` for object/view presence and `V$ALLCOLUMN` for column names.
3. Preserve meta-table group tokens such as `SYS_TABLES_`, `SYS_COLUMNS_`,
   `SYS_INDICES_`, `SYS_INDEX_COLUMNS_`, `SYS_TABLE_PARTITIONS_`,
   `SYS_CONSTRAINTS_`, `SYS_GRANT_SYSTEM_`, `SYS_GRANT_OBJECT_`,
   `SYS_USERS_`, `DBA_USERS_`, `SYS_USER_ROLES_`, `SYS_DIRECTORIES_`,
   `SYS_SYNONYMS_`, `SYS_MATERIALIZED_VIEWS_`, `SYS_TRIGGERS_`,
   `SYS_JOBS_`, `SYS_REPLICATIONS_`, `SYS_REPL_HOSTS_`,
   `SYS_REPL_ITEMS_`, `SYS_REPL_RECOVERY_INFOS_`, `SYS_DATABASE_LINKS_`,
   and `SYS_XA_HEURISTIC_TRANS_`.
4. Preserve performance-view group tokens such as `V$TABLE`, `V$ALLCOLUMN`,
   `V$CATALOG`, `V$DATATYPE`, `V$PROPERTY`, `V$VERSION`, `V$SESSION`,
   `V$STATEMENT`, `V$SQLTEXT`, `V$PLANTEXT`, `V$SESSION_WAIT`,
   `V$LOCK_WAIT`, `V$LOCK_STATEMENT`, `V$LOCK_TABLE_STATS`,
   `V$TRANSACTION`, `V$DATABASE`, `V$TABLESPACES`, `V$DATAFILES`,
   `V$ARCHIVE`, `V$BACKUP_INFO`, `V$LOG`, `V$LFG`,
   `V$SQL_PLAN_CACHE`, `V$DBMS_STATS`, `V$REPGAP`, `V$REPSENDER`,
   `V$REPRECEIVER`, `V$TEMPORARY_LOBS`, and `V$QUEUE_DELETE_OFF`.
5. Preserve version-drift cautions: `SYS_REPL_TABLE_OID_IN_USE_` is listed in
   7.1 and 7.3 Korean sources but not in the checked 8.1 Korean table list;
   `V$TEMPORARY_LOBS` and `V$MEM_STABLE` are `Altibase 8.1 verified source`
   views; `V$QUEUE_DELETE_OFF` is present in Korean General Reference 2 while
   English extraction-aid lists can omit it.
6. For performance views, route interpretation through the performance tuning
   source before producing recommendations. View SQL alone does not prove a
   tuning action.

## Artifact Templates

```sql
-- 00_view_availability.sql
SELECT NAME, SLOTSIZE, COLUMNCOUNT
FROM V$TABLE
WHERE NAME IN ('V$PROPERTY',
               'V$TEMPORARY_LOBS',
               'V$QUEUE_DELETE_OFF',
               'V$LOCK_TABLE_STATS',
               'V$REPGAP',
               '<TARGET_VIEW_OR_TABLE>')
ORDER BY NAME;
```

```sql
-- 10_column_availability.sql
SELECT TABLENAME, COLNAME
FROM V$ALLCOLUMN
WHERE TABLENAME IN ('V$PROPERTY',
                    'V$TEMPORARY_LOBS',
                    'V$QUEUE_DELETE_OFF',
                    'V$REPGAP',
                    '<TARGET_VIEW_OR_TABLE>')
ORDER BY TABLENAME, COLNAME;
```

```sql
-- 20_property_lookup.sql
SELECT NAME, VALUE1, VALUE2
FROM V$PROPERTY
WHERE NAME IN ('<PROPERTY_NAME>')
ORDER BY NAME;
```

```sql
-- 30_replication_lookup.sql
SELECT REP_NAME, REP_GAP
FROM V$REPGAP;
```

```sql
-- 40_object_column_lookup.sql
SELECT TABLENAME, COLNAME
FROM V$ALLCOLUMN
WHERE TABLENAME = '<OBJECT_OR_VIEW_NAME>'
ORDER BY COLNAME;
```

## Guardrails

- Do not assert a column exists until `V$ALLCOLUMN` or the exact
  target-version General Reference section confirms it.
- Do not use 8.1-only or drifted views for 7.1 or 7.3 without installed-version
  proof.
- Do not generate write DML against dictionary tables or performance views.
- Do not infer privilege, dependency, replication, lock, session, or plan
  state from a single view when the source route requires supporting views,
  trace logs, object definitions, or customer runtime output.
- Do not interpret performance symptoms as production tuning actions without
  workload evidence, SQL text, execution plan, table/index definitions,
  statistics state, and rollback plan.

## Validation Checks

Every generated dictionary/view artifact must include:

- Target version and source route.
- View existence check with `V$TABLE`.
- Column existence check with `V$ALLCOLUMN`.
- Exact query using only confirmed columns.
- Expected result shape, such as one row per object, one row per column, or a
  named runtime token.
- A note identifying which missing columns or runtime values require exact
  source or customer evidence.

## Stop Conditions

Stop and ask for more evidence if:

- The requested view or column is not confirmed in the target version.
- The query depends on `V$TEMPORARY_LOBS`, `V$MEM_STABLE`, or other
  `Altibase 8.1 verified source` views while the target is 7.1 or 7.3.
- The request asks for a complete dictionary or performance-view column list
  from this playbook alone.
- The answer depends on current locks, sessions, plans, replication state,
  logs, object definitions, or performance samples that the customer has not
  supplied.
