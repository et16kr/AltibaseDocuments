# SQL Generation Test Results

Job: `JOB-084`
Phase: P8 QA
Date: 2026-05-14
Result: Pass

## Objective

Run 20 representative SQL generation prompt checks against the Altibase GPT attachment set, with primary focus on `GPTs/attachments/03_sql_ddl_generation.md`.

Acceptance criterion: every prompt has an acceptable answer.

## Sources Reviewed

- `GPTs/attachments/03_sql_ddl_generation.md`
- `GPTs/attachments/04_sql_dml_oracle_compatibility.md`
- `GPTs/attachments/05_data_types_properties.md`
- `GPTs/attachments/06_data_dictionary_performance_views.md`
- `GPTs/attachments/09_replication_ha_cdc.md`
- `GPTs/attachments/15_migration_oracle_compatibility.md`
- `GPTs/attachments/18_security_ssl_tls.md`

## Method

The checks were run as manual Codex prompt simulations. For each prompt, the generated-answer requirements were compared with the attachment content and the GPT instruction draft.

No SQL was executed against a live Altibase server. This QA pass validates whether the attachment set supports acceptable generated SQL answers, including version boundaries, runnable syntax patterns, prerequisites, cautions, and verification SQL.

Pass criteria used for every check:

- The answer states the assumed Altibase version or asks for it when required.
- SQL object names, properties, commands, file paths, and view names remain literal.
- Generated SQL is ordered and executable after replacing environment placeholders.
- Version-specific syntax such as `IF NOT EXISTS`, `IF EXISTS`, `JSON`, Temporary LOB, and `USING SSL` is limited to the supported version guidance.
- A relevant verification query is included when the attachment provides one.
- The answer does not expose internal source labels or local source paths.

## Summary

| Metric | Count |
| --- | ---: |
| Prompt checks run | 20 |
| Passed | 20 |
| Failed | 0 |
| Review needed | 0 |

## Prompt Checks

### SQL-GEN-01: 8.1 idempotent tablespace DDL

Prompt: Generate Altibase 8.1 DDL to create disk, memory, volatile, and temporary tablespaces for schema `app`, using idempotent syntax where supported.

Accepted answer:

- States Altibase 8.1 verified source as the target.
- Uses `CREATE DISK DATA TABLESPACE IF NOT EXISTS`, `CREATE MEMORY DATA TABLESPACE IF NOT EXISTS`, `CREATE VOLATILE DATA TABLESPACE IF NOT EXISTS`, and `CREATE TEMPORARY TABLESPACE IF NOT EXISTS`.
- Uses absolute placeholder paths such as `/data/altibase/dbs/app_disk01.dbf` and `/data/altibase/dbs/app_temp01.tmp`.
- Mentions `CREATE TABLESPACE` privilege or `SYS`, checkpoint directory requirements, and memory or volatile allocation-unit cautions.
- Includes verification with `V$TABLESPACES`, `V$DATAFILES`, `V$MEM_TABLESPACES`, `V$VOL_TABLESPACES`, and `V$PROPERTY`.

Result: Pass

### SQL-GEN-02: 7.3 compatible tablespace DDL

Prompt: Generate Altibase 7.3 DDL for one disk tablespace and one memory tablespace, with verification SQL.

Accepted answer:

- States Altibase 7.3 as the target.
- Omits `IF NOT EXISTS`.
- Uses `CREATE DISK DATA TABLESPACE` with `DATAFILE`, `AUTOEXTEND`, `EXTENTSIZE`, and `SEGMENT MANAGEMENT`.
- Uses `CREATE MEMORY DATA TABLESPACE` with `SIZE`, `AUTOEXTEND`, `CHECKPOINT PATH`, and `SPLIT EACH`.
- Includes verification against `V$TABLESPACES`, `V$DATAFILES`, `V$MEM_TABLESPACES`, and related property checks.

Result: Pass

### SQL-GEN-03: Application schema and least-privilege DDL role

Prompt: Create schema `app` with default memory tablespace `app_mem_tbs`, temporary tablespace `app_temp_tbs`, access to `app_disk_tbs`, and only the DDL privileges required to create tables, sequences, and views.

Accepted answer:

- Uses `CREATE USER app IDENTIFIED BY ... DEFAULT TABLESPACE ... TEMPORARY TABLESPACE ... ACCESS ... ON`.
- Uses a role such as `app_schema_ddl_role`.
- Grants `CREATE SESSION`, `CREATE TABLE`, `CREATE SEQUENCE`, and `CREATE VIEW`, without broad `ALL PRIVILEGES`.
- Adds `ALTER USER app ACCESS app_mem_tbs ON` when needed.
- Includes verification with `SYSTEM_.SYS_USERS_`, `SYSTEM_.SYS_GRANT_SYSTEM_`, and `SYSTEM_.SYS_USER_ROLES_`.

Result: Pass

### SQL-GEN-04: Runtime user object grants

Prompt: Create a runtime user for `app` that can only read and write `app.app_user`, read `app.app_document`, and read sequence `app.seq_app_user`.

Accepted answer:

- Creates `app_runtime` with `CREATE SESSION`.
- Grants table and sequence privileges through a role such as `app_runtime_dml_role`.
- Uses object grants: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, and `SELECT ON app.seq_app_user`.
- Notes that the runtime user should reconnect after a role grant.
- Includes broad-grant audit SQL using `SYSTEM_.SYS_GRANT_SYSTEM_`, `SYSTEM_.SYS_GRANT_OBJECT_`, `SYSTEM_.SYS_PRIVILEGES_`, and `SYSTEM_.SYS_USERS_`.

Result: Pass

### SQL-GEN-05: Memory table with constraints

Prompt: Generate DDL for a hot OLTP memory table `app.app_user` with `user_id`, `user_name`, `status`, `created_at`, primary key, unique key, and check constraint.

Accepted answer:

- Uses `CREATE TABLE app.app_user`.
- Places the table in `TABLESPACE app_mem_tbs`.
- Includes `MAXROWS` as appropriate for a non-partitioned memory table.
- Defines named constraints such as `pk_app_user`, `uk_app_user_name`, and a `CHECK` on `status`.
- Includes verification with `SYSTEM_.SYS_TABLES_`, `SYSTEM_.SYS_COLUMNS_`, `SYSTEM_.SYS_CONSTRAINTS_`, and `V$MEMTBL_INFO`.

Result: Pass

### SQL-GEN-06: Disk table with LOB storage and foreign key

Prompt: Generate DDL for disk table `app.app_document` with a `CLOB` body, primary key, foreign key to `app.app_user`, and separated LOB storage.

Accepted answer:

- Uses `CREATE TABLE app.app_document`.
- Places the base table in `TABLESPACE app_disk_tbs`.
- Uses `LOB (body) STORE AS (TABLESPACE app_disk_tbs)`.
- Adds a named primary key and named foreign key, with an explicit delete rule such as `ON DELETE CASCADE`.
- Includes table, column, and constraint verification SQL.

Result: Pass

### SQL-GEN-07: Global temporary tables in volatile storage

Prompt: Generate Altibase DDL for transaction-scoped and session-scoped temporary staging tables.

Accepted answer:

- Uses `CREATE GLOBAL TEMPORARY TABLE`.
- Uses `ON COMMIT DELETE ROWS` for transaction-scoped data and `ON COMMIT PRESERVE ROWS` for session-scoped data.
- Places the tables in a volatile tablespace such as `app_vol_tbs`.
- Warns not to put ordinary `BLOB` or `CLOB` columns in volatile temporary-table storage.
- Includes verification using `SYSTEM_.SYS_TABLES_` and table type or temporary table metadata.

Result: Pass

### SQL-GEN-08: Partitioned disk table DDL

Prompt: Generate examples for range, list, and hash partitioned disk tables and explain the key restrictions.

Accepted answer:

- Generates `PARTITION BY RANGE`, `PARTITION BY LIST`, and `PARTITION BY HASH` examples.
- Includes a `DEFAULT` partition for range and list examples.
- Uses `TABLESPACE app_disk_tbs` at the table and partition level.
- Notes that list partitioning uses one key column, `MAXROWS` is not used with partitioned tables, and LOB columns should not be partition keys.
- Includes verification with `SYSTEM_.SYS_TABLE_PARTITIONS_` and related dictionary tables.

Result: Pass

### SQL-GEN-09: 8.1 JSON table

Prompt: Generate Altibase 8.1 DDL for `app.app_event` with a native `JSON` payload column and the required checks.

Accepted answer:

- States that `JSON` is an 8.1 baseline feature from the Altibase 8.1 verified source.
- Uses `payload JSON IN ROW 2048` or equivalent supported `JSON` syntax.
- Does not use `JSON` for 7.1 or 7.3 unless the user explicitly confirms support.
- Notes that JSON processing uses Temporary LOB and checks `TEMPORARY_LOB_ENABLE`.
- Includes verification with `SYSTEM_.SYS_COLUMNS_`, `V$PROPERTY`, and `V$TEMPORARY_LOBS`.

Result: Pass

### SQL-GEN-10: ALTER TABLE maintenance DDL

Prompt: Generate SQL to add a column, move a disk table or LOB to another tablespace, split a range partition, and add or coalesce a hash partition.

Accepted answer:

- Uses `ALTER TABLE ... ADD COLUMN`.
- Uses `ALTER TABLE ... ALTER TABLESPACE ... LOB (...)` for disk table and LOB movement.
- Uses `SPLIT PARTITION ... AT (...) INTO (...)` for a range partition.
- Uses `ADD PARTITION` and `COALESCE PARTITION` for the hash-partition example, without applying hash-only `COALESCE PARTITION` to range or list partitions.
- Notes that table-definition changes should not be generated for a table that is a replication target.

Result: Pass

### SQL-GEN-11: Constraints and verification

Prompt: Generate named primary-key, unique, check, foreign-key, local unique constraint, and drop-constraint SQL for `app.department`, `app.employee`, and `app.order_history`.

Accepted answer:

- Uses named constraints such as `pk_department`, `uk_department_code`, `ck_department_status`, and `fk_employee_department`.
- Uses `USING INDEX TABLESPACE app_disk_tbs` where index placement matters.
- Uses `LOCALUNIQUE` for the partitioned table case.
- Drops constraints explicitly using `DROP CONSTRAINT`, `DROP UNIQUE`, `DROP PRIMARY KEY`, or `DROP LOCALUNIQUE`.
- Includes verification queries using `SYSTEM_.SYS_CONSTRAINTS_` and `SYSTEM_.SYS_CONSTRAINT_COLUMNS_`, including constraint type and delete rule interpretation.

Result: Pass

### SQL-GEN-12: Index generation and maintenance

Prompt: Generate Altibase SQL for ordinary, unique, local, local unique, function-based, direct key, and maintenance operations on indexes.

Accepted answer:

- Generates `CREATE INDEX`, `CREATE UNIQUE INDEX`, local index syntax, and `CREATE LOCALUNIQUE INDEX`.
- Uses a deterministic function before a function-based index when a user-defined function is involved.
- Uses `DIRECTKEY MAXSIZE` only where appropriate.
- Includes `ALTER INDEX ... REBUILD`, partition rebuild, `DIRECTKEY OFF`, rename, and `DROP INDEX` examples.
- Includes verification with `SYSTEM_.SYS_INDICES_`, `SYSTEM_.SYS_INDEX_COLUMNS_`, `SYSTEM_.SYS_PART_INDICES_`, `SYSTEM_.SYS_INDEX_PARTITIONS_`, `V$PROPERTY`, and `V$DISK_BTREE_HEADER`.

Result: Pass

### SQL-GEN-13: Sequence DDL

Prompt: Generate SQL for `app.seq_app_user`, show how to use `NEXTVAL`, and create a sequence ready for sequence replication.

Accepted answer:

- Uses `CREATE SEQUENCE app.seq_app_user START WITH ... INCREMENT BY ... CACHE ...`.
- Shows `app.seq_app_user.NEXTVAL` in an `INSERT`.
- Uses `ENABLE SYNC TABLE` only for the sequence replication case.
- Includes verification using `V$SEQ` joined through `SYSTEM_.SYS_TABLES_` and `SYSTEM_.SYS_USERS_`.

Result: Pass

### SQL-GEN-14: Queue DDL and minimal queue usage

Prompt: Generate SQL for queue `app.app_event_q`, then enqueue, dequeue, compact, reset message IDs, and verify it.

Accepted answer:

- Uses `CREATE QUEUE`, not `CREATE TABLE`, for queue behavior.
- Avoids unsupported queue column constraints, encryption clauses, and `TIMESTAMP`.
- Generates `ENQUEUE INTO`, `DEQUEUE ... FIFO ... WAIT`, `ALTER QUEUE ... COMPACT`, and `ALTER QUEUE ... MSGID RESET`.
- Notes that `DROP QUEUE` removes the queue table, index, and sequence used for `MSGID`.
- Verifies with `SYSTEM_.SYS_TABLES_` and `table_type = 'Q'`.

Result: Pass

### SQL-GEN-15: Idempotent DDL version boundary

Prompt: Can I use `IF NOT EXISTS` and `IF EXISTS` in generated DDL for tables, queues, users, tablespaces, and replication objects across Altibase 7.3 and 8.1?

Accepted answer:

- Separates 7.3 and 8.1 guidance.
- Says to omit `IF NOT EXISTS` and `IF EXISTS` for 7.1 and 7.3 unless the customer confirms exact build support.
- Allows supported `IF NOT EXISTS` and `IF EXISTS` forms for Altibase 8.1 verified source.
- Warns that idempotent existence checks do not validate that existing objects have the intended attributes.
- Keeps object names and syntax fragments literal.

Result: Pass

### SQL-GEN-16: Dynamic and static property SQL

Prompt: Generate SQL to change `QUERY_TIMEOUT` for the current session and for the running server, and explain what to do for static properties.

Accepted answer:

- Reads `QUERY_TIMEOUT` from `V$PROPERTY` before changing it.
- Uses `ALTER SESSION SET QUERY_TIMEOUT = ...` for the session case.
- Uses `ALTER SYSTEM SET QUERY_TIMEOUT = ...` for the running server case.
- Reads `V$PROPERTY` after the change.
- For static or restart-required properties such as `LOG_FILE_SIZE`, `PORT_NO`, or `MAX_CLIENT`, does not generate dynamic `ALTER SYSTEM`; instead shows read-only checks and states that file, restart, or database recreation steps are needed.

Result: Pass

### SQL-GEN-17: SQL plan cache property SQL

Prompt: Generate SQL to inspect and change `SQL_PLAN_CACHE_SIZE`, including the related performance-view checks.

Accepted answer:

- Reads `SQL_PLAN_CACHE_SIZE` from `V$PROPERTY`.
- Queries `V$SQL_PLAN_CACHE` before the change.
- Uses `ALTER SYSTEM SET SQL_PLAN_CACHE_SIZE = ...` only as a documented dynamic-property example.
- Queries both `V$PROPERTY` and `V$SQL_PLAN_CACHE` after the change.
- States the required `SYS` or `ALTER SYSTEM` privilege.

Result: Pass

### SQL-GEN-18: Non-SSL replication DDL

Prompt: Generate two-node TCP replication SQL for `app.app_user` and `app.app_document` between `192.168.10.10` and `192.168.10.20`.

Accepted answer:

- Confirms tables and primary keys must already exist on both nodes.
- Queries the peer node's `REPLICATION_PORT_NO`.
- Creates matching `CREATE REPLICATION` objects on both nodes with reversed peer endpoints.
- Uses `ALTER REPLICATION ... SYNC` when initial data synchronization and start are intended.
- Includes verification with `SYSTEM_.SYS_REPLICATIONS_`, `SYSTEM_.SYS_REPL_HOSTS_`, `SYSTEM_.SYS_REPL_ITEMS_`, `V$REPSENDER`, and `V$REPRECEIVER`.

Result: Pass

### SQL-GEN-19: 8.1 SSL replication DDL

Prompt: Generate Altibase 8.1 SSL replication SQL for the same two nodes and explain which port to use.

Accepted answer:

- States Altibase 8.1 verified source and keeps SSL replication separate from ordinary client SSL.
- Requires completed SSL/TLS setup on both nodes and nonzero `REPLICATION_SSL_PORT_NO`.
- Uses the peer node's `REPLICATION_SSL_PORT_NO` in each `WITH 'host', port USING SSL` clause.
- Uses matching `CREATE REPLICATION` statements on both nodes and includes `ALTER REPLICATION ... SYNC`.
- Warns not to combine `FOR ANALYSIS` Log Analyzer replication with `USING SSL`.

Result: Pass

### SQL-GEN-20: Oracle DDL conversion to Altibase

Prompt: Convert an Oracle design with `VARCHAR2`, `NUMBER`, `CLOB`, an Oracle JSON check constraint, a global temporary table, a sequence, and Oracle storage clauses into Altibase DDL for an 8.1 target.

Accepted answer:

- Does not claim Oracle DDL can run unchanged.
- Maps Oracle `VARCHAR2` to Altibase `VARCHAR`, `NUMBER(p,s)` to `NUMBER(p,s)` or `NUMERIC(p,s)` depending on exactness, and `CLOB` to `CLOB`.
- Removes Oracle-only storage, `SECUREFILE`, `BASICFILE`, `RETENTION`, and similar LOB attributes.
- Uses native `JSON` only for the 8.1 target and checks `TEMPORARY_LOB_ENABLE`; for older targets, suggests `VARCHAR`, `CLOB`, application validation, or upgrade planning.
- Converts Oracle global temporary-table intent to `CREATE GLOBAL TEMPORARY TABLE ... TABLESPACE app_vol_tbs`, and converts sequences to Altibase `CREATE SEQUENCE`.
- Includes verification queries for tables, columns, constraints, sequences, and Temporary LOB or JSON checks.

Result: Pass

## Final Validation Commands

Attachment count command:

```bash
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' | wc -l
```

Expected output:

```text
20
```

Forbidden-string command:

```bash
rg -n "trunk|C:/|file://" GPTs/attachments || true
```

Expected output:

```text
No matches.
```

## Conclusion

All 20 representative SQL generation prompts have acceptable answers supported by the current attachment set. `JOB-084` acceptance criteria are satisfied.
