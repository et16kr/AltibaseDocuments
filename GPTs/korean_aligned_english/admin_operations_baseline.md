# Korean-Aligned English Baseline: Admin Operations Batch

- Job: `S1-J007`
- Scope: installation, environment setup, database creation, startup, shutdown,
  first checks, administrator storage, tablespaces, datafiles, log anchors,
  archive log, backup, recovery, user administration, privileges, roles,
  replication state changes, protected DDL, destructive SQL, TLS/security, and
  version-sensitive property-change guardrails.
- Source-pack gate: `GPTs/source_pack/source_pack_validation.md` records
  `Status: pass`, `Verdict: Pass`, no blockers, and explicit permission to
  continue to the Korean-aligned English baseline.
- Authority rule: Korean product manuals are authoritative. English product
  manuals are extraction aids. For 8.1 material, preserve the established
  `Altibase 8.1 verified source` boundary.
- Downstream boundary: this file is a working baseline, not a final GPT upload
  package. It does not replace exact source-pack extraction.

## Batch Source Coverage

| Version scope | Korean source IDs | English source IDs | Baseline manifest rows |
| --- | --- | --- | --- |
| 7.1 | `SRC-000049`, `SRC-000056`, `SRC-000058`, `SRC-000060`, `SRC-000070`, `SRC-000051`, `SRC-000072` | `SRC-000018`, `SRC-000025`, `SRC-000027`, `SRC-000029`, `SRC-000038`, `SRC-000020`, `SRC-000040` | `KAE-BLOCK-000001`, `KAE-BLOCK-000010`, `KAE-BLOCK-000012`, `KAE-BLOCK-000013`, `KAE-BLOCK-000029`, `KAE-BLOCK-000030`, `KAE-BLOCK-000035` |
| 7.3 | `SRC-000113`, `SRC-000120`, `SRC-000122`, `SRC-000124`, `SRC-000132`, `SRC-000115`, `SRC-000134` | `SRC-000082`, `SRC-000089`, `SRC-000091`, `SRC-000093`, `SRC-000101`, `SRC-000084`, `SRC-000103` | `KAE-BLOCK-000136`, `KAE-BLOCK-000145`, `KAE-BLOCK-000147`, `KAE-BLOCK-000148`, `KAE-BLOCK-000162`, `KAE-BLOCK-000163`, `KAE-BLOCK-000166` |
| 8.1 verified | `SRC-000173`, `SRC-000180`, `SRC-000182`, `SRC-000184`, `SRC-000192`, `SRC-000175`, `SRC-000194` | `SRC-000143`, `SRC-000150`, `SRC-000152`, `SRC-000154`, `SRC-000161`, `SRC-000145`, `SRC-000163` | `KAE-BLOCK-000191`, `KAE-BLOCK-000201`, `KAE-BLOCK-000203`, `KAE-BLOCK-000204`, `KAE-BLOCK-000217`, `KAE-BLOCK-000218`, `KAE-BLOCK-000223` |

## KAE-ADMINOPS-BLOCK-001: Installation And Environment Setup

- Source IDs: `SRC-000060`, `SRC-000029`, `SRC-000124`, `SRC-000093`,
  `SRC-000184`, `SRC-000154`, with supporting first-run context from
  `SRC-000058`, `SRC-000027`, `SRC-000122`, `SRC-000091`, `SRC-000182`,
  `SRC-000152`.
- Version scope: 7.1, 7.3, and `Altibase 8.1 verified source`.
- Source block refs: `SRC-000060/BLOCK-000529`, `SRC-000029/BLOCK-000527`,
  `SRC-000124/BLOCK-000533`, `SRC-000093/BLOCK-000531`,
  `SRC-000184/BLOCK-000537`, `SRC-000154/BLOCK-000535`,
  `SRC-000058/BLOCK-000528`, `SRC-000027/BLOCK-000526`,
  `SRC-000122/BLOCK-000532`, `SRC-000091/BLOCK-000530`,
  `SRC-000182/BLOCK-000536`, `SRC-000152/BLOCK-000534`.
- Alignment status: baseline generated from paired Korean authority and English
  extraction aids. Platform tables and installer examples contain version-
  sensitive details; check the exact source row before producing a customer
  platform-support statement.

Baseline:

1. Collect required inputs before installation: target Altibase version or
   patch level, server versus client package, operating system, CPU
   architecture, available memory, disk layout, replication requirement,
   desired `ALTIBASE_HOME`, license file status, database name, service port,
   memory database limit, buffer size, archive-log choice, database character
   set, national character set, and directories for disk database files, memory
   database files, archive logs, transaction logs, and log anchor files.
2. Use the package installer that matches the operating system and CPU. The
   manuals state that both server and client packages are 64-bit, Microsoft
   Windows is client-only, and server/client support differs by version and
   patch. Do not generalize platform support beyond the exact version source.
3. Before installation, check system requirements and kernel/resource settings.
   The manuals give a general baseline of at least 1 GB memory, 2 GB
   recommended, one CPU minimum, two CPUs recommended, at least 1 GB each for
   software and transaction logs, and at least 12 GB free disk for smooth
   operation. Special-purpose deployments require customer-specific sizing.
4. Run or review the installer flow in this order: environment check, package
   download, installer start, installation directory and installation type,
   system parameter checks, Altibase property settings, property confirmation,
   product installation, license key registration or later license-file copy,
   quick setting guide, and post-installation tasks.
5. The installer can create `altibase_user.env` under
   `$ALTIBASE_HOME/conf/` and add sourcing of that file to the account profile.
   The baseline environment variables are `ALTIBASE_HOME`, `PATH`,
   `LD_LIBRARY_PATH`, and `CLASSPATH`. If the installer did not apply them,
   source the environment file before running server, iSQL, or utility checks.
6. License handling is a startup blocker. If license registration was postponed,
   copy the license file to `$ALTIBASE_HOME/conf/license` before attempting to
   start Altibase service.

Safe first checks:

- `uname -a` to confirm the package matches the host.
- Review `$ALTIBASE_HOME/install/pre_install.sh` before changing kernel
  parameters as root.
- Review `$ALTIBASE_HOME/install/post_install.sh` before using generated
  database-creation SQL.
- Confirm `$ALTIBASE_HOME/conf/altibase.properties` after installer property
  entry and before database creation or startup.

Stop conditions:

- Stop if the operating system, CPU architecture, glibc/library level, or patch
  requirement is not confirmed against the exact version source.
- Stop if the license file is missing or expired.
- Stop if kernel/resource settings cannot be applied before running Altibase.
- Stop if storage directories for data, logs, archive logs, or log anchors are
  missing, temporary, or not backed by the intended filesystem.

## KAE-ADMINOPS-BLOCK-002: Database Creation, Startup, Shutdown, And First Checks

- Source IDs: `SRC-000049`, `SRC-000018`, `SRC-000113`, `SRC-000082`,
  `SRC-000173`, `SRC-000143`, with first-start context from `SRC-000058`,
  `SRC-000027`, `SRC-000122`, `SRC-000091`, `SRC-000182`, `SRC-000152`.
- Version scope: 7.1, 7.3, and `Altibase 8.1 verified source`.
- Source block refs: `SRC-000049/BLOCK-000002`, `SRC-000018/BLOCK-000001`,
  `SRC-000113/BLOCK-000004`, `SRC-000082/BLOCK-000003`,
  `SRC-000173/BLOCK-000006`, `SRC-000143/BLOCK-000005`,
  `SRC-000058/BLOCK-000528`, `SRC-000027/BLOCK-000526`,
  `SRC-000122/BLOCK-000532`, `SRC-000091/BLOCK-000530`,
  `SRC-000182/BLOCK-000536`, `SRC-000152/BLOCK-000534`.
- Alignment status: baseline generated for standard manual flow. Exact
  `CREATE DATABASE` syntax and character-set lists remain delegated to the SQL
  Reference source IDs listed in the protected SQL block.

Baseline:

1. Create a database only after installation, environment variables, license,
   directory properties, and initialization properties are confirmed. Altibase
   requires a manually created database before the database server can be used
   for normal service.
2. Use iSQL with SYSDBA mode to establish an administration session, then
   advance to the `PROCESS` phase before `CREATE DATABASE`.

```sql
-- Administration session shell command:
-- isql -u sys -p manager -sysdba

STARTUP PROCESS;
CREATE DATABASE mydb INITSIZE=50M NOARCHIVELOG
CHARACTER SET ksc5601 NATIONAL CHARACTER SET utf16;
```

3. Startup phases proceed forward only: `PRE_PROCESS`, `PROCESS`, `CONTROL`,
   `META`, and `SERVICE`. Users other than `SYS` can connect only in the
   `SERVICE` phase. `PROCESS` supports database creation and selected property
   inspection/change. `CONTROL` is used for media recovery. `META` supports
   metadata upgrade and resetlogs after incomplete recovery. `SERVICE` is the
   normal operational phase.
4. After database creation, either shut down the server process or advance to
   service. `SHUTDOWN ABORT` can be used outside service phases, but it is a
   forceful shutdown and the next startup can require automatic restart
   recovery. `SHUTDOWN NORMAL` and `SHUTDOWN IMMEDIATE` are service-phase
   operations.
5. Normal startup can be performed through iSQL SYSDBA or the `server` script.
   Startup must be executed using the operating-system account that installed
   Altibase.

Safe first checks:

- Confirm the administration session is SYSDBA before `STARTUP`, `SHUTDOWN`,
  `CREATE DATABASE`, recovery, or resetlogs.
- Confirm the current phase before issuing phase-specific commands.
- Confirm the database name, character set, national character set, archive-log
  mode, and storage-directory properties before `CREATE DATABASE`.
- After startup, verify service transition messages and connection behavior
  before opening customer traffic.

Stop conditions:

- Stop if the current startup phase is not the required phase for the command.
- Stop if the OS user is not the Altibase installation account.
- Stop if `SHUTDOWN ABORT`, `DROP DATABASE`, incomplete recovery, or resetlogs
  is requested without a maintenance window and backup/recovery plan.
- Stop if requested character-set choices are not explicitly confirmed for the
  customer application and data.

## KAE-ADMINOPS-BLOCK-003: Storage, Tablespaces, Datafiles, Log Anchors, And Archive Logs

- Source IDs: `SRC-000049`, `SRC-000018`, `SRC-000113`, `SRC-000082`,
  `SRC-000173`, `SRC-000143`, plus property detail from `SRC-000056`,
  `SRC-000025`, `SRC-000120`, `SRC-000089`, `SRC-000180`, `SRC-000150`.
- Version scope: 7.1, 7.3, and `Altibase 8.1 verified source`.
- Source block refs: `SRC-000049/BLOCK-000002`, `SRC-000018/BLOCK-000001`,
  `SRC-000113/BLOCK-000004`, `SRC-000082/BLOCK-000003`,
  `SRC-000173/BLOCK-000006`, `SRC-000143/BLOCK-000005`,
  `SRC-000056/BLOCK-000515`, `SRC-000025/BLOCK-000514`,
  `SRC-000120/BLOCK-000517`, `SRC-000089/BLOCK-000516`,
  `SRC-000180/BLOCK-000519`, `SRC-000150/BLOCK-000518`.
- Alignment status: baseline generated for storage concepts and protected
  state changes. Exact property defaults and complete property tables remain
  not-ready for item-level downstream use until rechecked from the General
  Reference.

Baseline:

1. Altibase stores data logically in tablespaces and physically in data files,
   checkpoint image files, and log-related files depending on tablespace type.
   Disk tablespaces use data files. Memory tablespaces reside in memory and are
   backed by checkpoint image files. Volatile tablespaces reside in memory and
   do not have checkpoint image files; their data disappears when the database
   shuts down.
2. Database creation automatically creates the system dictionary, memory data,
   disk data, undo, and temporary tablespaces. System tablespaces cannot be
   deleted or renamed by users.
3. Log files store transaction log records used for complete system recovery.
   Log anchor files store database-execution metadata such as tablespace
   information, data-file locations, and checkpoint information. Altibase
   maintains three log anchor files. The manuals recommend maintaining the
   three log anchor files on different file systems; `LOGANCHOR_DIR` controls
   their locations.
4. `ARCHIVELOG` versus `NOARCHIVELOG` is chosen at database creation and can be
   changed during `STARTUP CONTROL`. In archivelog mode, filled online log
   files are copied to the archive directory set by `ARCHIVE_DIR`. Online backup
   and media recovery depend on archive-log availability.
5. Tablespace state changes are protected operations. User-defined disk and
   memory tablespaces can move between online and offline. Volatile and
   temporary tablespace states cannot be changed. Tablespaces containing
   replicated tables cannot have their state changed. Discard is a control-phase
   recovery measure for a broken tablespace and only `DROP TABLESPACE` can be
   executed on a discarded tablespace.
6. Undo tablespace is a system tablespace, only one exists, it is automatically
   managed, and it cannot be taken offline or discarded. User operations are
   limited to adding or dropping data files, resizing data files, and beginning
   or ending online data-file backup.

Safe first checks:

- Confirm `LOGANCHOR_DIR`, `ARCHIVE_DIR`, database file directories, and
  filesystem redundancy before creating or moving storage.
- Confirm target tablespace type, current state, and whether it contains
  replication targets before `ALTER TABLESPACE`.
- Confirm whether the operation must run in `CONTROL`, `META`, or `SERVICE`.
- For undo-space pressure, check source-backed undo tablespace and transaction
  segment guidance before changing `TRANSACTION_SEGMENT_COUNT` or data files.

Stop conditions:

- Stop if a log anchor file is missing, stale, or being restored without a
  media-recovery reason recorded in the backup/recovery block.
- Stop if a requested tablespace operation targets a system, temporary,
  volatile, replicated, or discarded tablespace in a way the manuals disallow.
- Stop if archive-log destination space is not confirmed before enabling
  archivelog mode or online backup.

## KAE-ADMINOPS-BLOCK-004: User, Privilege, And Role Administration

- Source IDs: `SRC-000049`, `SRC-000018`, `SRC-000113`, `SRC-000082`,
  `SRC-000173`, `SRC-000143`, with SQL statement support from `SRC-000072`,
  `SRC-000040`, `SRC-000134`, `SRC-000103`, `SRC-000194`, `SRC-000163`.
- Version scope: 7.1, 7.3, and `Altibase 8.1 verified source`.
- Source block refs: `SRC-000049/BLOCK-000002`, `SRC-000018/BLOCK-000001`,
  `SRC-000113/BLOCK-000004`, `SRC-000082/BLOCK-000003`,
  `SRC-000173/BLOCK-000006`, `SRC-000143/BLOCK-000005`,
  `SRC-000072/BLOCK-000884`, `SRC-000040/BLOCK-000883`,
  `SRC-000134/BLOCK-000886`, `SRC-000103/BLOCK-000885`,
  `SRC-000194/BLOCK-000888`, `SRC-000163/BLOCK-000887`.
- Alignment status: baseline generated for administration flow and protected
  user-drop guardrails. Exhaustive privilege enumeration remains delegated to
  the SQL Reference and source pack.

Baseline:

1. After database creation, the system administrator accounts are `SYSTEM_` and
   `SYS`. `SYSTEM_` owns meta tables and can execute DDL/DML on meta tables.
   `SYS` is the DBA account with normal-table and system-level rights. These
   users cannot be modified or removed with DDL.
2. Create general users with `CREATE USER`; the creator needs `CREATE USER`
   system privilege. A password is required. Default and temporary tablespaces
   can be specified, and tablespace access can be granted.

```sql
CREATE USER DLR IDENTIFIED BY DLR123
DEFAULT TABLESPACE user_data
TEMPORARY TABLESPACE temp_data
ACCESS sys_tbs_memory ON;
```

3. Use `ALTER USER` for password changes, default tablespace changes,
   temporary tablespace changes, and tablespace access changes. Use `DROP USER`
   to remove users. `DROP USER ... CASCADE` also drops the user's schema
   objects and referential-integrity constraints that refer to them; without
   `CASCADE`, remaining schema objects make the statement fail.
4. Altibase supports system privileges, object privileges, and roles. Use
   `GRANT` and `REVOKE` according to the SQL Reference. The SQL Reference
   states that `ALL` does not grant `ALTER DATABASE`, `DROP DATABASE`, or
   `MANAGE TABLESPACE`, and `DROP DATABASE` cannot be granted to users other
   than `SYS`.

Safe first checks:

- Confirm target user, ownership of schema objects, default and temporary
  tablespaces, and required access to tablespaces before generating DCL.
- Confirm the requested privilege exists in the exact SQL Reference for the
  target version.
- Confirm whether a role or direct privilege is required by customer policy.

Stop conditions:

- Stop before `DROP USER ... CASCADE` unless object ownership, dependency
  impact, backup, and rollback expectations are confirmed.
- Stop before granting broad system privileges unless least-privilege
  justification is recorded.
- Stop if asked to modify or drop `SYS` or `SYSTEM_`.

## KAE-ADMINOPS-BLOCK-005: Backup, Recovery, Incremental Backup, And Log Anchors

- Source IDs: `SRC-000049`, `SRC-000018`, `SRC-000113`, `SRC-000082`,
  `SRC-000173`, `SRC-000143`, with property support from `SRC-000056`,
  `SRC-000025`, `SRC-000120`, `SRC-000089`, `SRC-000180`, `SRC-000150`.
- Version scope: 7.1, 7.3, and `Altibase 8.1 verified source`.
- Source block refs: `SRC-000049/BLOCK-000002`, `SRC-000018/BLOCK-000001`,
  `SRC-000113/BLOCK-000004`, `SRC-000082/BLOCK-000003`,
  `SRC-000173/BLOCK-000006`, `SRC-000143/BLOCK-000005`,
  `SRC-000056/BLOCK-000515`, `SRC-000025/BLOCK-000514`,
  `SRC-000120/BLOCK-000517`, `SRC-000089/BLOCK-000516`,
  `SRC-000180/BLOCK-000519`, `SRC-000150/BLOCK-000518`.
- Alignment status: protected baseline generated. Exact recovery command
  variants must still be checked against the SQL Reference and the customer's
  backup files before use.

Baseline:

1. Altibase supports logical backup through utilities and physical backup
   through offline and online backup. Offline backup requires normal shutdown
   and copying all tablespace files, log anchor files, and log files. Online
   backup is service-preserving but requires archivelog mode because recovery
   needs log files to undo uncommitted work and redo committed work.
2. Full online backup can target the entire database or individual tablespaces.
   Representative statements:

```sql
ALTER DATABASE BACKUP DATABASE TO '/backup_dir';
ALTER DATABASE BACKUP TABLESPACE SYS_TBS_DISK_DATA TO '/backup_dir';
ALTER TABLESPACE SYS_TBS_DISK_DATA BEGIN BACKUP;
-- copy the data files with operating-system tools
ALTER TABLESPACE SYS_TBS_DISK_DATA END BACKUP;
```

3. Database-level backup guarantees that backup-related log files are archived.
   Tablespace-level backup does not guarantee this; archive the required logs
   separately using the source-backed DCL flow.
4. Restart recovery runs automatically after abnormal process termination.
   Media recovery is for lost or corrupted data files, is performed in
   `STARTUP CONTROL`, and is offline media recovery. Complete recovery restores
   to current time when required logs are available. Incomplete recovery
   restores to a time or valid-log boundary and requires `META RESETLOGS`
   before proceeding.
5. For media recovery, use current log anchor files whenever possible. Restore
   only data files from backups except for special cases such as accidental
   `DROP TABLESPACE`, where backup log anchors may be needed because the
   current log anchors no longer contain the dropped tablespace metadata.
6. Stable checkpoint image files are required for media recovery of memory
   tablespaces. If checkpoint scale is Pair, identify the stable ping-pong
   checkpoint image with `dumpla` and the log anchor attribute before backup.
7. If a tablespace is added, deleted, or renamed, back up `SYS_TBS_MEM_DIC` and
   the changed tablespace, or back up the entire database. Back up log anchors
   with the dictionary tablespace because log anchors contain tablespace
   structure information.
8. Incremental backup requires a level 0 backup before level 1. Page change
   tracking must be enabled, and tracking starts after level 0 backup. The
   `backupInfo` file is required for incremental recovery; if it is lost,
   incremental backup files created before the loss can no longer be used.

Safe first checks:

- Required inputs: exact Altibase version and patch, database mode, backup type,
  backup path, archive-log path, current log anchor state, target data files,
  tablespaces, stable checkpoint image information, replication status, failure
  symptom, available online logs, available archive logs, and the intended
  recovery point.
- Confirm database mode with source-backed checks such as `V$LOG` or
  `V$ARCHIVE` before online backup or archive-log commands.
- Confirm backup directory, free space, archive-log availability, log anchor
  currentness, and stable checkpoint image files.
- Confirm whether replication is active. If recovering a replicated database,
  handle `REPLICATION_SENDER_AUTO_START`, replication reset, or replication
  recreation according to source-backed recovery guidance.
- For incremental backup, confirm changeTracking and `backupInfo` files before
  restore/recovery commands.

Stop conditions:

- Stop if archive logs or online logs needed for complete recovery are missing.
- Stop before restoring backup log anchor files unless the source-backed special
  case applies and the reason is recorded.
- Stop before incomplete recovery or resetlogs unless the target recovery point,
  data-loss boundary, and full post-reset backup requirement are accepted.
- Stop if replication state is unknown during backup or recovery.

## KAE-ADMINOPS-BLOCK-006: Replication State Changes And Protected Replication DDL

- Source IDs: `SRC-000070`, `SRC-000038`, `SRC-000132`, `SRC-000101`,
  `SRC-000192`, `SRC-000161`, with property support from `SRC-000056`,
  `SRC-000025`, `SRC-000120`, `SRC-000089`, `SRC-000180`, `SRC-000150`.
- Version scope: 7.1, 7.3, and `Altibase 8.1 verified source`.
- Source block refs: `SRC-000070/BLOCK-000845`, `SRC-000038/BLOCK-000844`,
  `SRC-000132/BLOCK-000847`, `SRC-000101/BLOCK-000846`,
  `SRC-000192/BLOCK-000849`, `SRC-000161/BLOCK-000848`,
  `SRC-000056/BLOCK-000515`, `SRC-000025/BLOCK-000514`,
  `SRC-000120/BLOCK-000517`, `SRC-000089/BLOCK-000516`,
  `SRC-000180/BLOCK-000519`, `SRC-000150/BLOCK-000518`.
- Alignment status: protected baseline generated. See `CONF-000003` for
  untranslated Korean snippets in English extraction-aid sources; this baseline
  normalizes them in English.

Baseline:

1. Only `SYS` can execute replication-related statements. State changes include
   `SYNC`, `SYNC ONLY`, `START`, `QUICKSTART`, `STOP`, `RESET`, `DROP TABLE`,
   `ADD TABLE`, and `FLUSH`.
2. `START` resumes from the most recent replication point. `QUICKSTART` starts
   from the current log position. `START ... RETRY` or `QUICKSTART ... RETRY`
   can create the sender thread even if first handshaking fails; iSQL can show
   success even when initial handshaking failed, so verify trace logs or
   `V$REPSENDER`.
3. `STOP` stops replication. If a `SYNC` task is stopped, transmission of all
   rows is not guaranteed; to run `SYNC` again, delete all records from all
   replication target tables and perform `SYNC` again.
4. `RESET` resets replication restart information and can be used only while
   replication is stopped. `ADD TABLE` can be executed only while replication is
   stopped. `DROP TABLE` can skip a replication gap if target primary
   transaction logs or metadata logs are inside the gap, which can cause data
   inconsistency.
5. DDL generated by ordinary DDL operations is not transmitted by replication
   because DDL changes metadata on replication targets and can create data
   inconsistency. The standard procedure is to remove the target object from
   replication, execute DDL independently on each replication node, and add the
   target back.
6. The replication DDL properties are protected:
   `REPLICATION_DDL_ENABLE`, `REPLICATION_DDL_ENABLE_LEVEL`, and
   `REPLICATION_SQL_APPLY_ENABLE`. `REPLICATION_DDL_ENABLE_LEVEL` can be 0 or 1.
   Level 1 requires SQL apply mode. The exact allowed DDL statement list must
   be rechecked from the General Reference and Replication Manual before use.
7. Standard DDL procedure when service can stop: stop service, verify sessions,
   set `ADMIN_MODE=1`, flush replication, verify `REP_GAP=0`, stop replication,
   drop target from replication, execute DDL on all replication servers, add the
   target back, start replication, set `ADMIN_MODE=0`, and restart service.
8. Standard DDL procedure when service cannot stop: migrate service, flush and
   verify gap, set admin mode, stop replication, remove target, execute DDL on
   the isolated server, add target, enable SQL apply mode, restart replication,
   remove admin mode, repeat on the other active server, verify
   `SQL_APPLY_TABLE_COUNT=0`, disable SQL apply mode, and redistribute service.

Safe first checks:

- Required inputs: topology, active/standby or active/active role, replication
  name, target table or partition, whether service can stop, whether recovery
  options or eager mode are enabled, current replication gap, current sessions,
  desired DDL, and rollback or rebuild plan.
- Use `ALTER REPLICATION replication_name FLUSH;` and
  `SELECT REP_NAME, REP_GAP FROM V$REPGAP;` before protected DDL.
- Use `SELECT COUNT(*) FROM V$SESSION WHERE ID <> SESSION_ID();` to verify
  service stop or service migration before protected DDL.
- Use `V$REPSENDER`, `V$REPRECEIVER`, and trace logs to verify start, retry, and
  SQL apply behavior.

Stop conditions:

- Stop if `REP_GAP` is not 0 before protected DDL or target removal.
- Stop if service cannot be stopped and no SQL apply mode procedure is accepted.
- Stop if the replication object uses recovery options or eager mode and the
  source-required alternate procedure is not followed.
- Stop if the target DDL is not in the source-backed allowed list for the
  selected `REPLICATION_DDL_ENABLE_LEVEL`.

## KAE-ADMINOPS-BLOCK-007: Destructive SQL And DDL Guardrails

- Source IDs: `SRC-000072`, `SRC-000040`, `SRC-000134`, `SRC-000103`,
  `SRC-000194`, `SRC-000163`, with administrator context from `SRC-000049`,
  `SRC-000018`, `SRC-000113`, `SRC-000082`, `SRC-000173`, `SRC-000143`.
- Version scope: 7.1, 7.3, and `Altibase 8.1 verified source`.
- Source block refs: `SRC-000072/BLOCK-000884`, `SRC-000040/BLOCK-000883`,
  `SRC-000134/BLOCK-000886`, `SRC-000103/BLOCK-000885`,
  `SRC-000194/BLOCK-000888`, `SRC-000163/BLOCK-000887`,
  `SRC-000049/BLOCK-000002`, `SRC-000018/BLOCK-000001`,
  `SRC-000113/BLOCK-000004`, `SRC-000082/BLOCK-000003`,
  `SRC-000173/BLOCK-000006`, `SRC-000143/BLOCK-000005`.
- Alignment status: protected baseline generated for representative destructive
  operations. The complete SQL Reference is not exhaustively normalized in this
  batch; see `CONF-000004`.

Baseline:

1. `DROP DATABASE` can only be executed by `SYS` in SYSDBA administrator mode
   during the `PROCESS` phase. It deletes the database from the system and also
   removes the database's data, log files, and log anchor files.
2. `DROP TABLESPACE` requires `SYS` or `DROP TABLESPACE` privilege. If objects
   exist, `INCLUDING CONTENTS` is required; `AND DATAFILES` deletes associated
   files from the filesystem for disk tablespaces and checkpoint image files for
   memory tablespaces. System tablespaces cannot be removed.
3. `DROP USER ... CASCADE` drops the user, all objects in the user's schema,
   and referential-integrity constraints that refer to primary or unique keys in
   the user's schema. Without `CASCADE`, remaining schema objects make the
   operation fail.
4. `DROP TABLE` removes a table and all of its data. If `RECYCLEBIN_ENABLE=1`,
   a dropped table can move to the recycle bin instead of being immediately
   removed, subject to source-defined limits.
5. `TRUNCATE TABLE` removes all records and returns all pages in the table to
   the database as free pages. It is DDL and cannot be rolled back once it
   succeeds. If execution fails before completion or the server fails, rollback
   is possible according to the SQL Reference consideration.
6. `ALTER SYSTEM` can change system properties, checkpoint, start/stop flusher,
   start/stop archive log, switch logfile, flush buffer pool, compact or reset
   SQL plan cache, start/stop/reload audit, and reload access list. Some
   subcommands require SYSDBA or administrator mode and can affect performance,
   availability, audit behavior, or access control.

Safe first checks:

- Required inputs: exact Altibase version, current startup phase, connected
  user, privilege grant source, target object name, object owner, dependency
  list, replication participation, backup timestamp, restore plan, and
  customer-approved maintenance window.
- Confirm whether the object is a system object, system tablespace, replicated
  target, queue, or user owning schema objects before generating DDL.
- Confirm exact SQL syntax and limitations from the SQL Reference for the
  target version before producing copy/paste DDL.

Stop conditions:

- Stop before `DROP DATABASE`, `DROP TABLESPACE ... INCLUDING CONTENTS`,
  `DROP TABLESPACE ... AND DATAFILES`, `DROP USER ... CASCADE`,
  `DROP TABLE`, or `TRUNCATE TABLE` unless backup, dependency, replication, and
  maintenance-window evidence is present.
- Stop if a customer asks for "all destructive operations" or "all property
  changes" from this batch alone; use the source pack and SQL Reference for an
  exhaustive statement list.
- Stop if the request depends on current object definitions, live sessions, or
  runtime state that the user has not supplied.

## KAE-ADMINOPS-BLOCK-008: TLS And Security Operations

- Source IDs: `SRC-000051`, `SRC-000020`, `SRC-000115`, `SRC-000084`,
  `SRC-000175`, `SRC-000145`, with security administration context from
  `SRC-000049`, `SRC-000018`, `SRC-000113`, `SRC-000082`, `SRC-000173`,
  `SRC-000143`.
- Version scope: 7.1, 7.3, and `Altibase 8.1 verified source`.
- Source block refs: `SRC-000051/BLOCK-000851`, `SRC-000020/BLOCK-000850`,
  `SRC-000115/BLOCK-000853`, `SRC-000084/BLOCK-000852`,
  `SRC-000175/BLOCK-000855`, `SRC-000145/BLOCK-000854`,
  `SRC-000049/BLOCK-000002`, `SRC-000018/BLOCK-000001`,
  `SRC-000113/BLOCK-000004`, `SRC-000082/BLOCK-000003`,
  `SRC-000173/BLOCK-000006`, `SRC-000143/BLOCK-000005`.
- Alignment status: protected baseline generated. TLS dependency versions are
  version-sensitive and must not be generalized across 7.1, 7.3, and
  8.1-verified sources.

Baseline:

1. TLS setup requires OpenSSL on server and relevant clients. The 7.1 SSL/TLS
   source supports OpenSSL 0.9.4 through 1.0.2 and warns to verify Heartbleed
   exposure. The 7.3 and 8.1-verified SSL/TLS sources require OpenSSL toolkit
   3.0.8 and state that 7.3 no longer supports OpenSSL 1.0.x.
2. Server setup sequence: confirm OpenSSL and library, set server properties,
   specify SSL client authentication mode, set server certificate/private key
   and CA path or file, then start the server and verify that an SSL listener
   starts on the configured SSL port.
3. Server properties include `SSL_ENABLE`, `SSL_PORT_NO`, `SSL_MAX_LISTEN`,
   `SSL_CIPHER_LIST`, `SSL_CLIENT_AUTHENTICATION`, `SSL_CERT`, `SSL_KEY`,
   `SSL_CA`, and `SSL_CAPATH`. In 7.3 and 8.1-verified sources, TLS 1.3
   cipher suite and OpenSSL configuration loading are represented by
   `SSL_CIPHERS_SUITES` and `SSL_LOAD_CONFIG`.
4. JDBC SSL setup requires truststore/keystore work depending on public versus
   private certificates and server-only versus mutual authentication. For 7.3
   and 8.1-verified sources, Java 1.8.0_351 or later is recommended for TLS 1.3
   without special settings; Java 1.8.0_261 can use TLS 1.3 with an explicit
   client protocol setting.
5. ODBC/CLI SSL setup requires OpenSSL library verification, client certificate
   preparation for mutual authentication, SSL connection properties, and
   optional FIPS environment configuration. `SSL_VERIFY=0` disables server
   certificate authentication and is therefore a protected security choice.

Safe first checks:

- Required inputs: Altibase version and patch, OpenSSL version, Java/JRE
  version if JDBC is used, client type, authentication mode, certificate chain,
  private-key path, CA file or CA directory, cipher policy, FIPS requirement,
  TCP port, SSL port, and customer certificate rotation policy.
- Run `openssl version` before TLS setup.
- Check `openssl ciphers` when setting cipher lists.
- Verify startup output contains both TCP and SSL listeners when SSL is enabled.

Stop conditions:

- Stop if the OpenSSL version does not match the exact Altibase version source.
- Stop if server private keys, CA paths, truststores, or keystores are missing
  or not readable by the intended process account.
- Stop if disabling certificate verification is requested without an explicit
  customer security exception.
- Stop if TLS requirements are being mixed across 7.1 and 7.3 or 8.1-verified
  sources.

## KAE-ADMINOPS-BLOCK-009: Version-Sensitive Property Changes

- Source IDs: `SRC-000056`, `SRC-000025`, `SRC-000120`, `SRC-000089`,
  `SRC-000180`, `SRC-000150`, with SQL change mechanism from `SRC-000072`,
  `SRC-000040`, `SRC-000134`, `SRC-000103`, `SRC-000194`, `SRC-000163`.
- Version scope: 7.1, 7.3, and `Altibase 8.1 verified source`.
- Source block refs: `SRC-000056/BLOCK-000515`, `SRC-000025/BLOCK-000514`,
  `SRC-000120/BLOCK-000517`, `SRC-000089/BLOCK-000516`,
  `SRC-000180/BLOCK-000519`, `SRC-000150/BLOCK-000518`,
  `SRC-000072/BLOCK-000884`, `SRC-000040/BLOCK-000883`,
  `SRC-000134/BLOCK-000886`, `SRC-000103/BLOCK-000885`,
  `SRC-000194/BLOCK-000888`, `SRC-000163/BLOCK-000887`.
- Alignment status: protected baseline generated for the property-change
  pattern and the properties surfaced by this batch. Full property-by-property
  normalization remains not-ready; see `CONF-000004`.

Baseline:

1. Treat all property changes as version-sensitive. Before changing a property,
   check its data type, default, attributes, range, whether it is read-write or
   read-only, whether it is single-value, whether it can be changed online, and
   whether restart or phase transition is required.
2. `ALTER SYSTEM` is the SQL mechanism for changing system properties while
   Altibase is running when the property supports that mode and the user is
   `SYS` or has `ALTER SYSTEM`.
3. `ADMIN_MODE` is read-write, single value, range 0 or 1, and limits database
   connection to administrators. When set to 1, only `SYS` and `SYSTEM_` can
   connect using SYSDBA; other users cannot establish a connection.
4. `REPLICATION_DDL_ENABLE` is read-write, default 0, range 0 or 1, and enables
   DDL on replication target tables when set to 1. It can be changed by
   `ALTER SYSTEM` while Altibase is running. It must be handled with the
   replication DDL guardrails in this file.
5. `REPLICATION_DDL_ENABLE_LEVEL` requires `REPLICATION_DDL_ENABLE=1`; it
   controls which DDL can be used on replication target tables and supports
   levels 0 and 1. Level 1 requires SQL apply mode according to the Replication
   Manual baseline.
6. `REPLICATION_SQL_APPLY_ENABLE` is shown in the General Reference as
   read-only, default 0, range 0 or 1, and controls SQL apply synchronization
   behavior for metadata differences. The Replication Manual procedure uses
   `ALTER SYSTEM SET REPLICATION_SQL_APPLY_ENABLE = 1` and later resets it to
   0. Because the paired sources present this as a protected operational path,
   recheck the exact version source before generating a customer command.
7. `MEM_MAX_DB_SIZE`, `LOGANCHOR_DIR`, `ARCHIVE_DIR`,
   `TRANSACTION_SEGMENT_COUNT`, and `INCREMENTAL_BACKUP_CHUNK_SIZE` are
   surfaced by this batch because they affect database creation, storage,
   backup/recovery, log anchors, undo segments, and incremental backup. Do not
   generate exact values or online-change claims without checking the exact
   property section for the target version.

Safe first checks:

- Required inputs: exact version and patch, current phase, current property
  value, desired new value, property attribute, restart tolerance, replication
  state, backup state, archive-log state, and rollback plan.
- Check the exact property section in the version-specific General Reference.
- Confirm whether the change is intended for `altibase.properties`,
  `ALTER SYSTEM`, database creation, or startup-control operation.

Stop conditions:

- Stop if a property is read-only or phase-restricted and the requested change
  path does not match the source.
- Stop if the requested value is outside the source-defined range.
- Stop if changing a replication, archive-log, log-anchor, memory-size,
  incremental-backup, or admin-mode property without a maintenance and
  validation plan.
- Stop if source text appears inconsistent across manual sections; record a
  conflict or recheck before using the property in a generated artifact.

## KAE-ADMINOPS-BLOCK-010: Scoped Not-Ready Gaps

- Source IDs: `SRC-000049`, `SRC-000018`, `SRC-000056`, `SRC-000025`,
  `SRC-000058`, `SRC-000027`, `SRC-000060`, `SRC-000029`, `SRC-000070`,
  `SRC-000038`, `SRC-000051`, `SRC-000020`, `SRC-000072`, `SRC-000040`,
  `SRC-000113`, `SRC-000082`, `SRC-000120`, `SRC-000089`, `SRC-000122`,
  `SRC-000091`, `SRC-000124`, `SRC-000093`, `SRC-000132`, `SRC-000101`,
  `SRC-000115`, `SRC-000084`, `SRC-000134`, `SRC-000103`, `SRC-000173`,
  `SRC-000143`, `SRC-000180`, `SRC-000150`, `SRC-000182`, `SRC-000152`,
  `SRC-000184`, `SRC-000154`, `SRC-000192`, `SRC-000161`, `SRC-000175`,
  `SRC-000145`, `SRC-000194`, `SRC-000163`.
- Version scope: 7.1, 7.3, and `Altibase 8.1 verified source`.
- Source block refs: see the source coverage table and each block above.
- Alignment status: not-ready gaps recorded in `CONF-000004`.

Remaining scoped gaps:

1. Exhaustive property normalization for every storage, recovery, replication,
   TLS, and admin-mode property in the three General Reference versions is not
   complete in this batch.
2. Exhaustive destructive-SQL and DDL statement normalization from the SQL
   Reference is not complete in this batch.
3. Exact platform-support matrices and patch-specific operating-system rows
   must be checked from the target Installation Guide or supporting platform
   source before a customer-facing compatibility claim is generated.
4. Exact backup and recovery examples, including full/incremental backup tag
   combinations and temporary datafile recreation, must be checked against the
   exact source before producing a customer runbook.
5. Exact TLS sample programs and connector-specific connection strings remain
   outside this admin-operations baseline except for protected setup
   guardrails.
6. English extraction-aid sources contain untranslated Korean snippets and
   sample Korean data in several selected manuals. This baseline normalized
   operational prose into English and did not copy those snippets. Preserve
   customer-facing English unless an exact sample string is intentionally
   required and source-labeled.

Downstream rule:

Use this file for first-draft guarded admin-operation answers. When a request
requires exact syntax, full enumerations, platform support, property defaults,
property ranges, connector sample code, current runtime state, patch-specific
behavior, live logs, object definitions, or replication topology, ask for the
missing input and recheck the exact source IDs above before generating a
definitive artifact.
