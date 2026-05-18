# DDL And DCL Generation Playbook

- Playbook ID: `APB-000002`
- Owning job: `S2-J003`
- Validation status: `pass`
- Supported versions: Altibase 7.1, Altibase 7.3, and `Altibase 8.1 verified source`
- Protected topic: yes

## Source Routes

| Route | Source IDs | Source-pack block refs | Baseline blocks |
| --- | --- | --- | --- |
| DDL, DCL, administrative SQL, and replication SQL | `SRC-000049`, `SRC-000018`, `SRC-000056`, `SRC-000025`, `SRC-000057`, `SRC-000026`, `SRC-000070`, `SRC-000038`, `SRC-000072`, `SRC-000040`, `SRC-000113`, `SRC-000082`, `SRC-000120`, `SRC-000089`, `SRC-000121`, `SRC-000090`, `SRC-000132`, `SRC-000101`, `SRC-000134`, `SRC-000103`, `SRC-000173`, `SRC-000143`, `SRC-000180`, `SRC-000150`, `SRC-000181`, `SRC-000151`, `SRC-000192`, `SRC-000161`, `SRC-000194`, `SRC-000163` | `SRC-000049/BLOCK-000002`, `SRC-000018/BLOCK-000001`, `SRC-000056/BLOCK-000515`, `SRC-000025/BLOCK-000514`, `SRC-000057/BLOCK-000521`, `SRC-000026/BLOCK-000520`, `SRC-000070/BLOCK-000845`, `SRC-000038/BLOCK-000844`, `SRC-000072/BLOCK-000884`, `SRC-000040/BLOCK-000883`, `SRC-000113/BLOCK-000004`, `SRC-000082/BLOCK-000003`, `SRC-000120/BLOCK-000517`, `SRC-000089/BLOCK-000516`, `SRC-000121/BLOCK-000523`, `SRC-000090/BLOCK-000522`, `SRC-000132/BLOCK-000847`, `SRC-000101/BLOCK-000846`, `SRC-000134/BLOCK-000886`, `SRC-000103/BLOCK-000885`, `SRC-000173/BLOCK-000006`, `SRC-000143/BLOCK-000005`, `SRC-000180/BLOCK-000519`, `SRC-000150/BLOCK-000518`, `SRC-000181/BLOCK-000525`, `SRC-000151/BLOCK-000524`, `SRC-000192/BLOCK-000849`, `SRC-000161/BLOCK-000848`, `SRC-000194/BLOCK-000888`, `SRC-000163/BLOCK-000887` | `KAE-BLOCK-000272`, `KAE-BLOCK-000273` |

Guardrails: `CONF-000004` and `CONF-000005` remain open. Use this playbook for
guarded first drafts and route exact syntax, exhaustive clause coverage,
complete privilege lists, property ranges, view columns, and patch behavior to
the exact target-version source block.

Forbidden assumption note: DDL and DCL must be Altibase-source-backed. Do not
fill missing grammar from Oracle, MySQL, PostgreSQL, or ANSI SQL.

## Required Customer Inputs

Before generating DDL or DCL, collect:

- Target Altibase version and patch level.
- Connected user, privilege level, startup phase, and whether SYSDBA or `SYS`
  authority is required.
- Object owner, object names, schema names, tablespace names, object
  dependencies, existing DDL, table type, partitioning, indexes, constraints,
  LOB columns, and replication membership.
- Requested action class: create, alter, drop, truncate, grant, revoke, role
  change, user change, tablespace change, database operation, or replication
  operation.
- Maintenance window, current sessions, backup point, rollback expectation,
  restore plan, and customer approval for destructive or privilege-changing
  effects.
- Validation plan and expected result tokens.

## Generated Artifacts

This playbook may draft:

- Schema DDL: `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`, `TRUNCATE TABLE`,
  `CREATE INDEX`, `ALTER INDEX`, `DROP INDEX`, view, sequence, synonym,
  trigger, queue, job, and materialized-view routes when exact source syntax is
  checked.
- Storage DDL: `CREATE DISK TABLESPACE`, `CREATE MEMORY TABLESPACE`,
  `CREATE VOLATILE TABLESPACE`, `CREATE TEMPORARY TABLESPACE`,
  `ALTER TABLESPACE`, and `DROP TABLESPACE`.
- User, role, and privilege DCL: `CREATE USER`, `ALTER USER`, `DROP USER`,
  `CREATE ROLE`, `DROP ROLE`, `GRANT`, and `REVOKE`.
- Administrative SQL: `CREATE DATABASE`, `DROP DATABASE`, startup phase SQL,
  `ALTER DATABASE`, `ALTER SYSTEM`, `ALTER SESSION`, backup/recovery SQL, and
  replication SQL when the protected-operation inputs are supplied.
- Validation SQL and rollback or cleanup notes.

## Procedure

1. Confirm the source route for the target version. Use Korean manuals as
   authority and English manuals as extraction aids. Preserve the
   `Altibase 8.1 verified source` boundary for 8.1-only syntax.
2. Classify the requested statement as DDL, DCL, administrative SQL, or
   replication SQL before drafting. Preserve source tokens such as
   `ALTER DATABASE`, `CREATE DATABASE`, `CREATE TABLE`, `ALTER TABLE`,
   `DROP TABLE`, `TRUNCATE TABLE`, `CREATE USER`, `ALTER USER`, `DROP USER`,
   `GRANT`, `REVOKE`, `CREATE REPLICATION`, `ALTER REPLICATION`,
   `DROP REPLICATION`, `ALTER SYSTEM`, and `ALTER SESSION`.
3. Add an effect block before SQL. State whether the artifact is destructive,
   privilege-changing, storage-changing, replication-changing,
   phase-restricted, or version-sensitive.
4. Check implicit commit risk. Altibase DDL changes meta information and
   commits prior uncommitted DML when DDL executes. Do not generate an
   execution sequence that assumes prior DML can be rolled back after DDL.
5. Check version-only syntax. Generate `IF EXISTS` or `IF NOT EXISTS` only for
   `Altibase 8.1 verified source` scope or after exact installed-version
   evidence.
6. For replication-related SQL, require `SYS`, topology evidence, current gap,
   current sessions, service migration or stop plan, trace-log validation, and
   rollback or rebuild plan.
7. Draft validation SQL with every generated DDL/DCL artifact. Do not present
   DDL/DCL as ready to execute without validation and cleanup notes.

## Artifact Templates

Use placeholders until exact target-version syntax and customer inputs are
confirmed.

```sql
-- 00_ddl_precheck.sql
SELECT * FROM V$VERSION;

SELECT NAME, VALUE1, VALUE2
FROM V$PROPERTY
WHERE NAME IN ('ADMIN_MODE',
               'REPLICATION_DDL_ENABLE',
               'REPLICATION_DDL_ENABLE_LEVEL',
               'REPLICATION_SQL_APPLY_ENABLE')
ORDER BY NAME;

SELECT REP_NAME, REP_GAP
FROM V$REPGAP;

SELECT COUNT(*) AS non_admin_sessions
FROM V$SESSION
WHERE ID <> SESSION_ID();
```

```sql
-- 10_schema_first_draft.sql
-- Replace every placeholder after checking the exact target-version SQL Reference.
CREATE TABLE <schema_name>.<table_name> (
    <primary_key_column> <ALTIBASE_DATA_TYPE> NOT NULL,
    <business_column> <ALTIBASE_DATA_TYPE>,
    <created_at_column> DATE
) TABLESPACE <tablespace_name>;

CREATE INDEX <index_name>
ON <schema_name>.<table_name> (<business_column>);
```

```sql
-- 20_privileges_first_draft.sql
-- Use least privilege. Do not grant broad system privileges without approval.
CREATE ROLE <service_role>;

GRANT <object_privilege>
ON <schema_name>.<object_name>
TO <service_role>;

GRANT <service_role>
TO <service_user>;
```

```sql
-- 90_ddl_validation.sql
SELECT NAME, SLOTSIZE, COLUMNCOUNT
FROM V$TABLE
WHERE NAME IN ('<TABLE_OR_VIEW_NAME>', 'V$PROPERTY', 'V$REPGAP')
ORDER BY NAME;

SELECT TABLENAME, COLNAME
FROM V$ALLCOLUMN
WHERE TABLENAME = '<TABLE_OR_VIEW_NAME>'
ORDER BY COLNAME;
```

## Guardrails

- Destructive DDL: stop before `DROP DATABASE`, `DROP TABLESPACE ...
  INCLUDING CONTENTS`, `DROP TABLESPACE ... AND DATAFILES`, `DROP USER ...
  CASCADE`, `DROP TABLE`, or `TRUNCATE TABLE` without explicit approval,
  dependency inventory, backup point, replication check, and cleanup or restore
  plan.
- Privilege DCL: confirm the exact privilege exists for the target version.
  The source route states that `ALL` does not grant `ALTER DATABASE`,
  `DROP DATABASE`, or `MANAGE TABLESPACE`, and `DROP DATABASE` cannot be
  granted to users other than `SYS`.
- User DDL: do not modify or drop `SYS` or `SYSTEM_`. Stop before
  `DROP USER ... CASCADE` unless owned objects and referential-integrity
  effects are confirmed.
- Tablespaces: confirm tablespace type, current state, data files,
  checkpoint paths, archive-log state, replication membership, and whether the
  target is a system, temporary, volatile, replicated, or discarded tablespace.
- LOB storage: disk-table LOB data can be placed in a separate disk
  tablespace; memory-table LOB data cannot be stored separately from the table
  tablespace.
- Replication DDL: only `SYS` can execute replication-related statements. Do
  not generate protected replication DDL unless `REP_GAP=0`, service state,
  topology, and source-backed allowed statement list are confirmed.

## Validation Checks

Every generated DDL/DCL answer must include:

- Version check: `V$VERSION` or supplied installed-version evidence.
- Object check: `V$TABLE`, `V$ALLCOLUMN`, and exact dictionary routes for the
  target object type.
- Property check: `V$PROPERTY` for `ADMIN_MODE`, replication DDL properties,
  and any storage or behavior property used by the artifact.
- Privilege check: exact system/object privilege route from the SQL Reference
  and dictionary route such as `SYS_GRANT_SYSTEM_` or `SYS_GRANT_OBJECT_` when
  the target version exposes it.
- Replication check when relevant: `V$REPGAP`, `V$REPSENDER`,
  `V$REPRECEIVER`, and customer trace logs.
- Cleanup or rollback note explaining what can and cannot be rolled back after
  DDL executes.

## Stop Conditions

Stop and ask for missing evidence if:

- The target version, patch, object definition, privilege model, or rollback
  plan is missing.
- The request asks for exact BNF-like syntax from this playbook alone.
- The DDL depends on 8.1-only `IF EXISTS`, `IF NOT EXISTS`, native `JSON`,
  Temporary LOB, or `V$TEMPORARY_LOBS` while the target is 7.1 or 7.3.
- The artifact would run after uncommitted DML and the customer expects that
  DML to remain rollback-safe.
- A storage, replication, user, privilege, database, or system-property action
  is requested without explicit customer approval and validation output.
