# Protected Administration Operations Playbook

- Playbook ID: `APB-000016`
- Owning job: `S2-J005`
- Validation status: `pass`
- Supported versions: Altibase 7.1, Altibase 7.3, and `Altibase 8.1 verified source`
- Protected topic: yes

## Source Routes

| Route | Source IDs | Source-pack block refs | Baseline blocks |
| --- | --- | --- | --- |
| Cross-cutting protected administration gates for destructive SQL, database operations, tablespaces, log anchors, archive logs, properties, security, and recovery-sensitive work | `SRC-000049`, `SRC-000018`, `SRC-000056`, `SRC-000025`, `SRC-000072`, `SRC-000040`, `SRC-000113`, `SRC-000082`, `SRC-000120`, `SRC-000089`, `SRC-000134`, `SRC-000103`, `SRC-000173`, `SRC-000143`, `SRC-000180`, `SRC-000150`, `SRC-000194`, `SRC-000163`, `AID-SRC-000428`, `AID-SRC-000429` | `SRC-000049/BLOCK-000002`, `SRC-000018/BLOCK-000001`, `SRC-000056/BLOCK-000515`, `SRC-000025/BLOCK-000514`, `SRC-000072/BLOCK-000884`, `SRC-000040/BLOCK-000883`, `SRC-000113/BLOCK-000004`, `SRC-000082/BLOCK-000003`, `SRC-000120/BLOCK-000517`, `SRC-000089/BLOCK-000516`, `SRC-000134/BLOCK-000886`, `SRC-000103/BLOCK-000885`, `SRC-000173/BLOCK-000006`, `SRC-000143/BLOCK-000005`, `SRC-000180/BLOCK-000519`, `SRC-000150/BLOCK-000518`, `SRC-000194/BLOCK-000888`, `SRC-000163/BLOCK-000887`, `BLOCK-000438`, `BLOCK-000439` | `KAE-BLOCK-000272`, `KAE-BLOCK-000273`, `KAE-BLOCK-000276` |

Guardrails: `CONF-000004`, `CONF-000005`, and `CONF-000007` remain open. This
playbook is the cross-cutting safety gate for administration answers that could
destroy data, change privileges, alter storage, change startup phase, affect
replication, weaken security, or depend on backup/recovery state.

Forbidden assumption note: do not replace Altibase-specific stop conditions with
generic database best practices. If the exact source route or customer runtime
state is missing, ask for the missing input and provide the safest
source-backed next check.

## Required Customer Inputs

Missing input prompts to collect before any protected operation:

- Target Altibase version and patch level.
- Requested operation and exact object names: database, tablespace, datafile,
  log anchor, archive-log directory, user, role, privilege, property,
  replication object, certificate path, or backup set.
- Connected user, SYSDBA path, startup phase, service state, current sessions,
  replication state, and whether a maintenance window is approved.
- Exact source section for the command or property, including version scope,
  phase requirement, privilege requirement, dynamic/static behavior, and known
  cautions.
- Dependency inventory, object definitions, tablespace type, datafile paths,
  log anchor paths, archive-log paths, and backup timestamp where relevant.
- Non-destructive first checks, expected validation output, rollback plan, and
  recovery plan.
- Customer approval for destructive, privilege-changing, storage-changing,
  replication-changing, phase-changing, or security-weakening effects.

## Generated Artifacts

This playbook may draft:

- Protected-operation decision records.
- Preconditions and missing-evidence requests.
- Non-destructive SQL and file checks.
- Execution hold points for a human DBA.
- Validation bundles for post-change checks.
- Rollback or recovery notes, including when rollback is not possible after DDL
  or restore work.

## Procedure

1. Classify the operation. Protected classes include `DROP DATABASE`, `DROP
   TABLESPACE`, `DROP TABLESPACE ... INCLUDING CONTENTS`, `DROP TABLESPACE ...
   AND DATAFILES`, `DROP USER ... CASCADE`, `DROP TABLE`, `TRUNCATE TABLE`,
   `ALTER DATABASE`, `ALTER TABLESPACE`, `ALTER SYSTEM`, archive-log mode
   changes, log-anchor relocation, datafile relocation, recovery, resetlogs,
   TLS property changes, broad `GRANT`, and replication-affecting changes.
2. Check the exact source route and the current runtime phase before drafting a
   runnable command. Some operations are phase-restricted and some properties
   require restart, startup-control work, or database recreation.
3. Run non-destructive checks first. Prefer inventory and state queries over
   commands that change files, database phase, storage, privileges, or security.
4. State whether the artifact is destructive, privilege-changing,
   storage-changing, replication-changing, security-sensitive,
   phase-restricted, or version-sensitive.
5. Add an execution hold point before any irreversible step. A generated answer
   should not invite copy/paste execution until all missing input prompts and
   validation checks are satisfied.
6. Explain rollback honestly. DDL commits metadata changes; destructive
   operations and recovery file replacement may require restore or rebuild
   rather than SQL rollback.

## Artifact Templates

```sql
-- 00_protected_operation_precheck.sql
SELECT * FROM V$VERSION;

SELECT NAME, VALUE1, VALUE2
FROM V$PROPERTY
WHERE NAME IN ('ADMIN_MODE',
               'ARCHIVE_DIR',
               'LOGANCHOR_DIR',
               'REPLICATION_DDL_ENABLE',
               'REPLICATION_DDL_ENABLE_LEVEL',
               'REPLICATION_SQL_APPLY_ENABLE',
               'SSL_ENABLE',
               'SSL_PORT_NO')
ORDER BY NAME;

SELECT REP_NAME, REP_GAP
FROM V$REPGAP;
```

```text
# 10_protected_operation_decision_record.txt
Operation:
Target version and patch:
Exact source route:
Current phase:
Connected user and privilege:
Objects or files affected:
Destructive/storage/privilege/security/replication effect:
Missing input:
Non-destructive first checks:
Validation:
Rollback:
Recovery:
DBA approval:
```

```sql
-- 90_protected_operation_validation.sql
-- Fill exact dictionary or performance-view checks from the target source.
SELECT * FROM V$VERSION;

SELECT NAME, VALUE1, VALUE2
FROM V$PROPERTY
WHERE NAME IN ('<PROPERTY_NAME>')
ORDER BY NAME;
```

## Guardrails

- Stop before destructive DDL without explicit object inventory, dependency
  review, backup point, validation plan, and recovery plan.
- Stop before tablespace operations unless tablespace type, current state,
  datafile paths, replication membership, and system/temporary/volatile status
  are known.
- Stop before log-anchor, archive-log, datafile, or backup-file movement unless
  current file inventory, copy plan, restore plan, and source-backed phase
  requirement are recorded.
- Stop before broad privileges, protected user changes, `ADMIN_MODE`, TLS
  weakening, or certificate verification disablement without explicit customer
  approval.
- Stop before property changes where dynamic/static status, restart or recreate
  requirement, value range, and validation SQL are missing.
- Stop if asked for a complete catalog of every protected operation from this
  playbook alone.

## Validation Checks

Every protected operation artifact must include:

- Exact target-version source route and baseline block route.
- Missing input list and explicit source-backed assumptions.
- Non-destructive prechecks for version, phase, properties, affected objects,
  replication state, storage paths, logs, and certificates where relevant.
- Validation SQL or file checks for the requested operation.
- Rollback or recovery notes that distinguish SQL rollback from restore,
  rebuild, resetlogs, or post-change full backup.
- Human approval hold point for destructive, privilege-changing,
  storage-changing, replication-changing, or security-weakening steps.

## Stop Conditions

Stop and ask for missing input if:

- The target version, patch, current phase, source section, object/file
  inventory, privilege path, validation plan, rollback plan, or recovery plan is
  missing.
- The operation depends on live workload, logs, replication topology, backup
  files, certificate material, installed patch behavior, or exact object
  definitions not supplied by the customer.
- The requested answer would generate executable destructive SQL, privileged
  DCL, storage file movement, recovery commands, or TLS weakening before the
  customer has approved the impact and validation path.
