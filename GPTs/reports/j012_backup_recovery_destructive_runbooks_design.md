# J012 Backup Recovery And Destructive Operation Runbook Design Note

Date: 2026-05-17

## Scope

J012 strengthens protected operation content in:

- `GPTs/attachments/02_administration_operations.md`
- `GPTs/attachments/03_sql_ddl_generation.md`
- `GPTs/attachments/07_error_messages_troubleshooting.md`

The job does not change original manuals, benchmark thresholds, benchmark questions,
or unsupported Altibase behavior.

## Design

The main structure change is a dedicated `Protected Backup And Recovery Answer Anchors`
section in `02_administration_operations.md`. The section is intentionally
answer-ready: it groups backup family selection, archive-log mode, online backup
completion, complete versus incomplete recovery, `RESETLOGS`, log-anchor choice,
datafile and checkpoint-image recovery, incremental restore metadata, destructive
`DROP`/`DISCARD`/`REUSE`, replication restore safety, and hard stop inputs.

`03_sql_ddl_generation.md` now has a compact SQL-generation guardrail block so
generated backup, recovery, datafile, `DROP TABLESPACE`, `DISCARD`, and `REUSE`
answers preserve exact command tokens and do not skip preconditions.

`07_error_messages_troubleshooting.md` now has an error-led triage anchor for
backup/recovery/destructive-operation symptoms. It keeps troubleshooting answers
from jumping from an error code directly to datafile replacement, `RESETLOGS`,
discard, drop, or overwrite actions without required evidence.

## Evidence Classification

The J012 benchmark evidence is mostly synthesis and retrieval weakness around exact
protected-operation tokens rather than broad absence of all recovery content. The
edits therefore add compact anchors and generation hooks instead of replacing the
longer runbooks.

- Content gaps addressed: `ALTER DATABASE db_name META RESETLOGS`,
  `ALTER DATABASE dbname SERVICE`, `Database-Level Backup Completed [SUCCESS]`,
  `t1.fmt`, `t1.dat`, and `backup-time metadata`.
- Retrieval and synthesis gaps addressed: `ARCHIVELOG`, `NOARCHIVELOG`,
  `ARCHIVE_DIR`, `V$LOG`, `V$ARCHIVE`, `current loganchor`,
  `ALTER DATABASE BACKUP LOGANCHOR`, `SYS_TBS_MEM_DIC`, `CREATE_LSN_FILENO`,
  `dumpla`, `LOG_DIR`, `PAIR`, `SINGLE`, `V$LOG.CHECKPOINT_SCALE`,
  `V$MEM_STABLE`, `CURRENT_DB`, `BEGIN BACKUP`, `END BACKUP`,
  `ALTER SYSTEM SWITCH LOGFILE`, `DROP TABLESPACE`, `INCLUDING CONTENTS`,
  `AND DATAFILES`, `DISCARD`, and `REUSE`.

## Source Basis

The edited facts were checked against repository-local selected sources, especially:

- Altibase 7.3 and Altibase 8.1 verified source Administrator's Manuals for backup
  types, `ARCHIVELOG` and `NOARCHIVELOG`, online backup, `ALTER SYSTEM SWITCH
  LOGFILE`, `altibase_sm.log`, complete and incomplete media recovery, `ALTER
  DATABASE db_name META RESETLOGS`, current-versus-historical log-anchor recovery,
  replicated database restore cautions, incremental `changeTracking` and
  `backupInfo`, and `DISCARD` behavior.
- Altibase 8.1 verified source General Reference for `V$LOG.CHECKPOINT_SCALE`,
  `V$MEM_STABLE`, `V$MEM_TABLESPACES`, `V$DATAFILES.CREATE_LSN_FILENO`,
  `V$ARCHIVE`, and archive destination columns.
- Altibase 7.3 and Altibase 8.1 verified source SQL References for
  `DROP TABLESPACE`, `INCLUDING CONTENTS`, `AND DATAFILES`, `CASCADE CONSTRAINTS`,
  `BEGIN BACKUP`, `END BACKUP`, `DISCARD`, and `REUSE`.
- iLoader source material already consolidated in the attachment set for logical
  table-level backup using `formout`, `out`, `in`, `t1.fmt`, and `t1.dat`.

## Safety Rules Preserved

- Ask for exact version, patch, startup phase, database mode, file paths, object
  inventory, backup manifest, log availability, log-anchor source, replication
  topology, and explicit data-loss approval before protected operations.
- Prefer complete media recovery when required logs and backups exist.
- Use `current loganchor` files for ordinary complete recovery; use historical
  `loganchor*` only for source-backed recovery plans that need historical metadata.
- Do not run `META RESETLOGS` after complete recovery.
- Do not recommend `DISCARD`, `DROP TABLESPACE ... INCLUDING CONTENTS`, `AND
  DATAFILES`, or `REUSE` without explicit destructive-operation confirmation.
