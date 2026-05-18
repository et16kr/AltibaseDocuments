# Service Development And Artifact Generation Playbook

- Playbook ID: `APB-000015`
- Owning job: `S2-J003`
- Validation status: `pass`
- Supported versions: Altibase 7.1, Altibase 7.3, and `Altibase 8.1 verified source`
- Protected topic: yes

## Source Routes

Use this playbook as the service-development and copy/paste artifact hub for
Altibase-backed implementation work. It makes SQL, DDL, DCL, and DML generation
one artifact class inside the broader service objective.

| Route | Source IDs | Source-pack block refs | Baseline blocks |
| --- | --- | --- | --- |
| Administration, storage, startup, privileges, protected operations | `SRC-000049`, `SRC-000018`, `SRC-000113`, `SRC-000082`, `SRC-000173`, `SRC-000143` | `SRC-000049/BLOCK-000002`, `SRC-000018/BLOCK-000001`, `SRC-000113/BLOCK-000004`, `SRC-000082/BLOCK-000003`, `SRC-000173/BLOCK-000006`, `SRC-000143/BLOCK-000005` | `KAE-BLOCK-000272` |
| Data types, properties, SQL syntax, dictionary and performance views | `SRC-000056`, `SRC-000025`, `SRC-000057`, `SRC-000026`, `SRC-000072`, `SRC-000040`, `SRC-000120`, `SRC-000089`, `SRC-000121`, `SRC-000090`, `SRC-000134`, `SRC-000103`, `SRC-000180`, `SRC-000150`, `SRC-000181`, `SRC-000151`, `SRC-000194`, `SRC-000163` | `SRC-000056/BLOCK-000515`, `SRC-000025/BLOCK-000514`, `SRC-000057/BLOCK-000521`, `SRC-000026/BLOCK-000520`, `SRC-000072/BLOCK-000884`, `SRC-000040/BLOCK-000883`, `SRC-000120/BLOCK-000517`, `SRC-000089/BLOCK-000516`, `SRC-000121/BLOCK-000523`, `SRC-000090/BLOCK-000522`, `SRC-000134/BLOCK-000886`, `SRC-000103/BLOCK-000885`, `SRC-000180/BLOCK-000519`, `SRC-000150/BLOCK-000518`, `SRC-000181/BLOCK-000525`, `SRC-000151/BLOCK-000524`, `SRC-000194/BLOCK-000888`, `SRC-000163/BLOCK-000887` | `KAE-BLOCK-000273` |

Guardrails: `CONF-000004` and `CONF-000005` remain open. The playbook can
produce guarded first drafts, not exhaustive or production-ready coverage of
every property, SQL grammar branch, view column, error entry, patch behavior, or
live environment outcome.

Forbidden assumption note: do not infer behavior from Oracle, MySQL,
PostgreSQL, or ANSI SQL. Use only the Altibase routes above, the exact
target-version source block, and supplied customer evidence.

## Required Customer Inputs

Collect these inputs before drafting a customer-usable artifact package:

- Target Altibase version and patch level, including whether the request is for
  7.1, 7.3, or `Altibase 8.1 verified source` behavior.
- Service goal, workload shape, transaction expectations, data growth estimate,
  availability target, and whether replication or backup/recovery integration
  is part of the first draft.
- Platform, `ALTIBASE_HOME`, database name, startup phase, connected user,
  credentials policy, and whether the customer has SYSDBA or delegated
  privileges.
- Schema names, object names, existing object definitions, table type,
  tablespace plan, partitioning requirement, index requirement, LOB or JSON
  requirement, and expected row counts.
- Required users, roles, object privileges, system privileges, tablespace
  access, and least-privilege constraints.
- Property requirements, current `V$PROPERTY` evidence, restart window,
  maintenance window, and rollback plan.
- Validation plan, expected result tokens, non-production test target, backup
  point, and cleanup or rollback acceptance.

If any input is absent, ask for it and provide the safest source-backed next
check instead of inventing a final artifact.

## Generated Artifacts

The service package may draft these artifact classes when source-backed:

- Architecture note: target-version assumptions, source routes, service
  boundary, storage and privilege decisions, risk notes, and omitted areas.
- SQL package: precheck SQL, schema DDL, data seed DML, privilege DCL,
  property inspection SQL, dictionary or performance-view validation SQL, and
  cleanup SQL.
- Configuration package: `altibase.properties` change plan or `ALTER SYSTEM`
  / `ALTER SESSION` plan when exact property mutability is confirmed.
- Test package: non-production setup, positive cases, negative cases, expected
  tokens, cleanup, and stop conditions.
- Handoff note: source IDs, source-pack block refs, Korean-aligned baseline
  block IDs, missing inputs, and live-validation requirements.

Do not use this playbook to finalize JDBC, ODBC, CLI, C Interface,
Precompiler, backup/recovery, replication/CDC, tool, migration, integration,
or production troubleshooting artifacts. Route those to the later focused
playbooks unless the artifact is only a SQL-side prerequisite covered here.

## Procedure

1. Classify the request as service planning, SQL/DDL/DCL/DML generation,
   property change, dictionary/view validation, or test generation. Use a
   focused playbook for the detailed artifact class after this hub identifies
   the route.
2. Confirm target version and patch. Do not use `IF EXISTS`, `IF NOT EXISTS`,
   native `JSON`, `TEMPORARY_LOB_ENABLE`, `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`,
   `MEMORY_TEMPLOB_PIECE_SIZE`, or `V$TEMPORARY_LOBS` for 7.1 or 7.3 unless
   the customer supplies exact installed-version proof.
3. Build an assumptions block before code. Include target version, source
   routes, supplied customer evidence, unresolved inputs, destructive effects,
   privilege effects, storage effects, and validation plan.
4. Draft artifacts in execution order: environment and version checks,
   dictionary checks, schema DDL, DCL, DML, property checks or changes,
   validation SQL, and cleanup or rollback notes.
5. Preserve Altibase tokens exactly. Do not rewrite source tokens into generic
   database vocabulary when the source provides names such as `CREATE DISK
   TABLESPACE`, `ALTER SYSTEM`, `GRANT`, `REVOKE`, `V$PROPERTY`,
   `V$TABLE`, `V$ALLCOLUMN`, `SYS_GRANT_SYSTEM_`, or `SYS_GRANT_OBJECT_`.
6. Mark every artifact as a non-production first draft until the customer has
   run validation in the target environment and supplied results.

## Copy/Paste Package Template

Use this format when a direct GPT answer is expected to produce copy/paste
artifacts. Fill only source-backed values and leave unresolved placeholders
visible.

```text
# Altibase Service Artifact Package

Target version:
Patch level:
Source routes:
- Source IDs:
- Source-pack block refs:
- Korean-aligned baseline blocks:

Customer inputs used:
- Service goal:
- Schema/object names:
- Tablespaces:
- Privilege model:
- Properties:
- Validation target:
- Rollback plan:

Guarded assumptions:
- This is a non-production first draft until validated.
- DDL can implicitly commit previous DML; do not run after uncommitted work.
- Destructive, privilege-changing, storage-changing, and version-sensitive
  actions require explicit approval and a backup or rollback plan.

Artifacts in order:
1. 00_precheck.sql
2. 10_schema.sql
3. 20_privileges.sql
4. 30_seed_or_change_dml.sql
5. 40_property_checks_or_changes.sql
6. 90_validation.sql
7. 99_cleanup_or_rollback.sql
```

```sql
-- 00_precheck.sql
-- Confirm the target environment before running generated artifacts.
SELECT * FROM V$VERSION;

SELECT NAME, VALUE1, VALUE2
FROM V$PROPERTY
WHERE NAME IN ('ADMIN_MODE',
               'AUTO_COMMIT',
               'ISOLATION_LEVEL',
               'REPLICATION_DDL_ENABLE',
               'REPLICATION_DDL_ENABLE_LEVEL',
               'REPLICATION_SQL_APPLY_ENABLE')
ORDER BY NAME;

SELECT NAME, SLOTSIZE, COLUMNCOUNT
FROM V$TABLE
WHERE NAME IN ('V$PROPERTY', 'V$TABLE', 'V$ALLCOLUMN', 'V$REPGAP')
ORDER BY NAME;
```

```sql
-- 90_validation.sql
-- Replace placeholders with target object names after confirming they exist.
SELECT TABLENAME, COLNAME
FROM V$ALLCOLUMN
WHERE TABLENAME IN ('<TARGET_TABLE_OR_VIEW>')
ORDER BY TABLENAME, COLNAME;

SELECT REP_NAME, REP_GAP
FROM V$REPGAP;
```

## Guardrails

- Destructive effects: stop before `DROP DATABASE`, `DROP TABLESPACE ...
  INCLUDING CONTENTS`, `DROP TABLESPACE ... AND DATAFILES`, `DROP USER ...
  CASCADE`, `DROP TABLE`, `TRUNCATE TABLE`, or broad update/delete DML unless
  backup, dependency, row-count, replication, maintenance-window, and rollback
  evidence is supplied.
- Implicit commits: Altibase DDL changes meta information and commits prior
  DML that has not been committed when the DDL executes. Do not place DDL
  after uncommitted DML if rollback of that DML is required.
- Privilege changes: require the exact user or role, target object, required
  privilege, least-privilege justification, and confirmation that `SYS` or
  `SYSTEM_` is not being modified or dropped.
- Storage changes: require tablespace type, file paths, archive-log status,
  replication membership, free space, backup point, and phase requirement.
- Properties: require exact property default, range, unit, attribute,
  dynamic-change level, and current runtime value. `V$PROPERTY` shows current
  values, not proof of defaults or allowed ranges.
- Dictionary and performance views: verify view and column availability with
  `V$TABLE` and `V$ALLCOLUMN` before hard-coding validation SQL.

## Validation Checks

Before handing off generated artifacts, include at least one validation query
for each artifact class used:

- Version and environment: `V$VERSION`, `V$PROPERTY`.
- Object existence and columns: `V$TABLE`, `V$ALLCOLUMN`, and exact
  `SYS_*` meta tables when the target source confirms them.
- Privileges: `SYS_GRANT_SYSTEM_`, `SYS_GRANT_OBJECT_`, `SYS_USER_ROLES_`,
  or the exact target-version privilege view route.
- Replication-sensitive schema changes: `V$REPGAP`, `V$REPSENDER`,
  `V$REPRECEIVER`, and trace logs supplied by the customer.
- Test result: expected row count, expected error token for negative cases,
  and cleanup confirmation.

## Stop Conditions

Stop and ask for customer evidence if:

- The target version or patch is missing.
- The request asks for production-ready, exhaustive, or patch-specific
  behavior from this playbook alone.
- The artifact depends on object definitions, logs, runtime output, installed
  tool output, property details, view columns, platform support, or live
  validation that has not been supplied.
- A requested syntax or behavior is present only in `Altibase 8.1 verified
  source` but the target is 7.1 or 7.3.
- The generated artifact would alter privileges, storage, replication,
  startup phase, or persistent properties without explicit approval and a
  rollback or recovery plan.
