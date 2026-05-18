# Backup And Recovery Playbook

- Playbook ID: `APB-000006`
- Owning job: `S2-J005`
- Validation status: `pass`
- Supported versions: Altibase 7.1, Altibase 7.3, and `Altibase 8.1 verified source`
- Protected topic: yes

## Source Routes

| Route | Source IDs | Source-pack block refs | Baseline blocks |
| --- | --- | --- | --- |
| Backup planning, logical/offline/online backup, archive-log mode, media recovery, log anchors, tablespace recovery, and incremental backup | `SRC-000049`, `SRC-000018`, `SRC-000056`, `SRC-000025`, `SRC-000072`, `SRC-000040`, `SRC-000113`, `SRC-000082`, `SRC-000120`, `SRC-000089`, `SRC-000134`, `SRC-000103`, `SRC-000173`, `SRC-000143`, `SRC-000180`, `SRC-000150`, `SRC-000194`, `SRC-000163`, `AID-SRC-000429` | `SRC-000049/BLOCK-000002`, `SRC-000018/BLOCK-000001`, `SRC-000056/BLOCK-000515`, `SRC-000025/BLOCK-000514`, `SRC-000072/BLOCK-000884`, `SRC-000040/BLOCK-000883`, `SRC-000113/BLOCK-000004`, `SRC-000082/BLOCK-000003`, `SRC-000120/BLOCK-000517`, `SRC-000089/BLOCK-000516`, `SRC-000134/BLOCK-000886`, `SRC-000103/BLOCK-000885`, `SRC-000173/BLOCK-000006`, `SRC-000143/BLOCK-000005`, `SRC-000180/BLOCK-000519`, `SRC-000150/BLOCK-000518`, `SRC-000194/BLOCK-000888`, `SRC-000163/BLOCK-000887`, `BLOCK-000439` | `KAE-BLOCK-000272`, `KAE-BLOCK-000273`, `KAE-BLOCK-000276` |

Guardrails: `CONF-000004`, `CONF-000005`, and `CONF-000007` remain open. This
playbook can draft guarded backup and recovery plans, but exact recovery
commands, complete backup-tag combinations, temporary datafile recreation,
patch-specific behavior, and production-ready restore decisions require exact
source recheck plus customer backup files and live state evidence.

Forbidden assumption note: do not infer Altibase recovery behavior from Oracle,
generic ARIES recovery, or filesystem snapshot conventions.

## Required Customer Inputs

Missing input prompts to collect before generating a backup or recovery
artifact:

- Target Altibase version and patch level.
- Backup goal: logical backup, offline physical backup, online database backup,
  online tablespace backup, archive-log operation, media recovery, incomplete
  recovery, or incremental backup.
- Current startup phase, service state, archive-log state, replication state,
  and whether a maintenance window is available.
- Backup directory, archive-log directory, online log paths, log anchor paths,
  datafile paths, checkpoint image paths, and free-space evidence.
- Failure scope, damaged or missing files, current log anchor state, available
  backup set, available online logs, available archive logs, and intended
  recovery point.
- Tablespace names and types, stable checkpoint image evidence for memory
  tablespaces, and whether any involved tablespace was added, deleted, renamed,
  discarded, or replicated.
- Incremental backup level, change-tracking state, `backupInfo` availability,
  and level 0 evidence when incremental backup or recovery is requested.
- Customer acceptance of data-loss boundary, post-reset backup requirement, and
  rollback or recovery plan.

## Generated Artifacts

This playbook may draft:

- Backup-policy evidence requests.
- Logical, offline, and online backup plans.
- Archive-log mode and archive-log handling checks.
- Media-failure triage and recovery plans.
- Incremental backup and recovery prerequisites.
- Validation SQL and operating-system file checks.
- Rollback or recovery notes for failed backup, incomplete recovery, resetlogs,
  or restored file mistakes.

## Procedure

1. Classify the request as backup planning, backup execution, archive-log
   operation, recovery planning, media recovery, incomplete recovery, or
   incremental backup.
2. Confirm archive-log state before online backup or recovery paths that depend
   on archive logs. `ARCHIVELOG` versus `NOARCHIVELOG` is a protected recovery
   boundary, and online backup is not a substitute for archive-log evidence.
3. For offline backup, require normal shutdown and a file inventory that covers
   all tablespace files, log anchor files, and log files.
4. For online backup, confirm `ARCHIVELOG` mode, backup directory, available
   space, and whether the scope is the whole database, a tablespace, or a data
   file.
5. For database-level backup, record that backup-related logs are archived by
   the database-level backup path. For tablespace-level backup, require a
   separate source-backed plan to archive the required logs.
6. For media recovery, prefer current log anchor files. Restore backup log
   anchors only for a source-backed special case, such as recovering an
   accidentally dropped tablespace whose metadata is no longer present in the
   current log anchors.
7. For memory tablespace media recovery, require stable checkpoint image
   evidence. When checkpoint scale is Pair, identify the stable ping-pong
   checkpoint image with source-backed tooling before drafting restore steps.
8. For incomplete recovery and resetlogs, record the accepted data-loss
   boundary and the requirement for a full backup after resetlogs.
9. For incremental backup, confirm level 0 exists before level 1, page change
   tracking is enabled, and `backupInfo` is present.

## Artifact Templates

```sql
-- 00_backup_precheck.sql
SELECT * FROM V$VERSION;

SELECT NAME, VALUE1, VALUE2
FROM V$PROPERTY
WHERE NAME IN ('ARCHIVE_DIR',
               'LOGANCHOR_DIR',
               'INCREMENTAL_BACKUP_CHUNK_SIZE',
               'REPLICATION_SENDER_AUTO_START')
ORDER BY NAME;

SELECT * FROM V$LOG;
SELECT * FROM V$ARCHIVE;
```

```sql
-- 10_online_backup_guarded_template.sql
-- Use only when ARCHIVELOG state, backup path, free space, and source syntax
-- are confirmed for the target version.
ALTER DATABASE BACKUP DATABASE TO '<backup_dir>';
ALTER DATABASE BACKUP TABLESPACE <tablespace_name> TO '<backup_dir>';

ALTER TABLESPACE <tablespace_name> BEGIN BACKUP;
-- Copy the target data files with customer-approved operating-system tooling.
ALTER TABLESPACE <tablespace_name> END BACKUP;
```

```sh
# 20_file_inventory_template.sh
# Non-destructive inventory only; do not move or overwrite files from this step.
find "<backup_dir>" -maxdepth 2 -type f -ls
find "<archive_log_dir>" -maxdepth 1 -type f -ls
find "<loganchor_dir>" -maxdepth 1 -type f -ls
```

```sql
-- 30_recovery_phase_guarded_template.sql
-- Use only after source recheck and customer restore evidence.
STARTUP CONTROL;
-- RECOVER commands must be filled from the exact target-version source and
-- the customer's available backup, online log, archive log, and recovery point.
-- STARTUP META;
-- ALTER DATABASE RESETLOGS;
-- STARTUP SERVICE;
```

## Guardrails

- Stop before online backup if archive-log state, backup path, or free space is
  unknown.
- Stop before media recovery if failure scope, current log anchors, backup set,
  online logs, archive logs, or target recovery point is missing.
- Stop before restoring backup log anchor files unless the source-backed special
  case is recorded.
- Stop before incomplete recovery or resetlogs unless the customer accepts the
  data-loss boundary and full post-reset backup requirement.
- Stop before incremental backup or recovery if level 0, page change tracking,
  or `backupInfo` evidence is missing.
- Stop if replication state is unknown during backup or recovery.

## Validation Checks

Every generated backup or recovery artifact must include:

- Exact source route and target-version scope.
- Non-destructive state checks for startup phase, `V$LOG`, `V$ARCHIVE`,
  archive-log directory, backup directory, and relevant properties.
- File inventory for datafiles, checkpoint images, log anchors, online logs,
  archive logs, and backup files.
- Tablespace type and state validation before tablespace-level backup or
  recovery.
- Replication state validation when any replicated table or database is
  involved.
- A recovery note explaining what can be retried, what must not be overwritten,
  and what full backup is required after resetlogs or major file relocation.

## Stop Conditions

Stop and ask for missing input if:

- The target version, backup mode, archive-log state, backup path, datafile
  paths, failure scope, restore target, or rollback plan is missing.
- The requested command depends on exact source syntax not present in the
  playbook.
- The customer wants a definitive recovery answer without providing logs,
  backup inventory, log anchor state, archive logs, online logs, or failure
  details.
- The artifact would overwrite current files or restore backup files without a
  verified recovery plan and customer approval.
