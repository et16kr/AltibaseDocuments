# R07 Installation, Startup/Shutdown, Administration, Backup, Recovery, Tablespace Operations

Date: 2026-05-14
Reviewer: Codex
Verdict: Review Required

## Scope

- Attachments:
  - `GPTs/attachments/00_version_release_platform.md`
  - `GPTs/attachments/01_getting_started_installation.md`
  - `GPTs/attachments/02_administration_operations.md`
- Supporting reports:
  - `GPTs/reports/version_coverage_validation.md`
- Source manuals sampled:
  - `Manuals/Altibase_7.1/eng/Getting Started Guide.md`
  - `Manuals/Altibase_7.1/eng/Installation Guide.md`
  - `Manuals/Altibase_7.1/eng/Administrator's Manual.md`
  - `Manuals/Altibase_7.1/eng/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_7.1/eng/SQL Reference.md`
  - `Manuals/Altibase_trunk/eng/Installation Guide.md`
  - `Manuals/Altibase_trunk/eng/Administrator's Manual` equivalent path with typographic apostrophe
  - `Manuals/Altibase_trunk/eng/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_trunk/eng/SQL Reference.md`
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`

## Commands Run

```bash
wc -l GPTs/attachments/00_version_release_platform.md GPTs/attachments/01_getting_started_installation.md GPTs/attachments/02_administration_operations.md Manuals/Altibase_7.1/eng/Getting\ Started\ Guide.md Manuals/Altibase_7.1/eng/Installation\ Guide.md Manuals/Altibase_7.1/eng/Administrator\'s\ Manual.md GPTs/reports/version_coverage_validation.md
nl -ba GPTs/attachments/01_getting_started_installation.md | sed -n '1,430p'
nl -ba GPTs/attachments/02_administration_operations.md | sed -n '1,1780p'
nl -ba GPTs/attachments/00_version_release_platform.md | sed -n '1,470p'
sed -n '1,240p' GPTs/reports/version_coverage_validation.md
rg -n 'startup|shutdown|server start|server stop|dbcreate|post_install|pre_install|license|ulimit|transparent|THP|archivelog|noarchivelog|catproc|ALTIBASE_NLS|ALTIBASE_HOME' Manuals/Altibase_7.1/eng/Getting\ Started\ Guide.md Manuals/Altibase_7.1/eng/Installation\ Guide.md
rg -n 'Startup Phase|STARTUP|SHUTDOWN|ARCHIVELOG|NOARCHIVELOG|BACKUP|RECOVER|RESETLOGS|DISCARD|TABLESPACE|V\$TABLESPACES|V\$DATAFILES|V\$MEM_TABLESPACES|V\$ARCHIVE|V\$LOG|altipasswd|syspassword' Manuals/Altibase_7.1/eng/Administrator\'s\ Manual.md
rg -n 'V\$LOG|SERVER_STATUS|ARCHIVELOG_MODE|CHECKPOINT_SCALE|BEGIN_CHKPT_FILE_NO|V\$ARCHIVE|V\$DATAFILES|V\$MEM_TABLESPACES|V\$VOL_TABLESPACES|V\$MEM_STABLE|V\$BACKUP_INFO|V\$OBSOLETE_BACKUP_INFO|V\$TABLE\b' Manuals/Altibase_7.1/eng Manuals/Altibase_7.3/eng Manuals/Altibase_trunk/eng
rg -n 'AIX 7\.2|Red Hat Enterprise Linux 9|Windows 2008|Windows 10|Altibase 8\.1|Supported Platform|Platform' ReleaseNotes Manuals/Altibase_trunk GPTs/attachments/00_version_release_platform.md GPTs/attachments/01_getting_started_installation.md
rg -n 'TODO|FIXME|trunk|/home/|file://|media/|\.jpg|\.png|ReleaseNotes|Altibase_trunk|Technical Documents' GPTs/attachments/00_version_release_platform.md GPTs/attachments/01_getting_started_installation.md GPTs/attachments/02_administration_operations.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name README.md | sort | wc -l
```

## Findings

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| High | `GPTs/attachments/01_getting_started_installation.md` | 60 | The 8.1 platform baseline says 8.1.0.0.1 supports Linux x86-64 on RHEL 7, 8, and 9 for server/client and Windows client-only, but omits AIX 7.2. This conflicts with `00_version_release_platform.md` line 322 and the 8.1 release notes, which list AIX 7.2 as server and client supported. | Add AIX 7.2 to the 8.1 pre-installation platform item and keep the wording aligned with `00_version_release_platform.md`. If this file intentionally gives only the Linux quick path, say that explicitly and point platform decisions to file 00. |
| High | `GPTs/attachments/01_getting_started_installation.md` | 380 | The 8.1 version-difference block repeats the same incomplete platform list and can cause GPT answers to state an incomplete 8.1 install target set. | Update this block to include AIX 7.2 server/client support, RHEL 7/8/9 Linux x86-64 support, Windows 2008/10 client-only support, 64-bit-only packages, and JDK 1.8+ for Java components. |
| High | `GPTs/attachments/02_administration_operations.md` | 162 | The common DBA check query selects `checkpoint_scale` from `V$LOG`. `CHECKPOINT_SCALE` is documented in the 8.1 verified source data dictionary, but it is not present in the sampled 7.1 or 7.3 data dictionaries. A generated 7.1/7.3 operational query would fail. | Remove `checkpoint_scale` from the common `V$LOG` query. Add a separate 8.1-only checkpoint-scale query, guarded by a column check through `V$ALLCOLUMN` or explicit wording that it applies only to Altibase 8.1 verified source. |
| Medium | `GPTs/attachments/02_administration_operations.md` | 130 | Shutdown phase guidance says all shutdown options are available in `SERVICE`, but does not preserve the source distinction that `SHUTDOWN NORMAL` and `SHUTDOWN IMMEDIATE` are service-phase-only while `SHUTDOWN ABORT` can be executed in any phase. | Add a short rule under shutdown choices: `SHUTDOWN NORMAL` and `SHUTDOWN IMMEDIATE` require `SERVICE`; `SHUTDOWN ABORT` is available in any startup phase and should be emergency-only because restart recovery is expected. |
| Medium | `GPTs/attachments/02_administration_operations.md` | 842 | The memory checkpoint path runbook is not fully actionable. It starts at `STARTUP PROCESS`/`STARTUP CONTROL` and lists `ADD`, `RENAME`, and `DROP CHECKPOINT PATH`, but omits the service shutdown/window, directory creation and permissions before the change, OS-level move/copy commands before returning to service, and verification queries. | Split this into separate add, rename, and drop runbooks. Include planned shutdown, `STARTUP CONTROL`, pre-created destination paths owned by the Altibase OS account, the exact `ALTER TABLESPACE` operation, required movement of checkpoint image files, verification with `V$TABLESPACES` in control or `V$MEM_TABLESPACE_CHECKPOINT_PATHS` after meta/service, then `STARTUP SERVICE`. |
| Medium | `GPTs/attachments/02_administration_operations.md` | 1053 | The offline physical backup block correctly says to copy all memory checkpoint directories, log anchors, needed log files, and disk data files, but the command example only copies default-looking `$ALTIBASE_HOME/dbs0`, `$ALTIBASE_HOME/dbs1`, `$ALTIBASE_HOME/logs`, and `$ALTIBASE_HOME/dbs/*.dbf`. Sites with non-default `MEM_DB_DIR`, `LOGANCHOR_DIR`, `LOG_DIR`, or data files outside `$ALTIBASE_HOME/dbs` could take an incomplete backup if they follow the sample literally. | Add a preflight discovery step: read `MEM_DB_DIR`, `LOGANCHOR_DIR`, and `LOG_DIR` from properties, query `V$DATAFILES` for all disk data files, and state that the sample `cp` commands are placeholders to be expanded to every site-specific path. Include a post-copy file-count or manifest verification step. |
| Medium | `GPTs/attachments/02_administration_operations.md` | 1213 | Incremental backup prerequisites mention that `backupInfo` loss makes prior incremental backups unusable, but the recovery runbooks do not capture the source procedure for missing `changeTracking` or `backupInfo` files: if those files are lost, the server may not start in `CONTROL`; it must start in `PROCESS` so change tracking can be disabled and `backupInfo` restored from the most recent incremental backup path. | Add an incremental recovery preflight block before `ALTER DATABASE RESTORE DATABASE`: check whether `$ALTIBASE_HOME/dbs/changeTracking` and `backupInfo` exist, start `PROCESS` if `CONTROL` fails because of these files, run `ALTER DATABASE DISABLE INCREMENTAL CHUNK CHANGE TRACKING` when needed, restore `backupInfo` from the backup tag directory, then proceed to `CONTROL`. |
| Low | `GPTs/attachments/02_administration_operations.md` | 18 | The "Altibase Hybrid Architecture" section uses marketing-style claims such as "extreme high-performance (microsecond latency)" and "requires no external caching layer." This is not tied to the operational source checks and may encourage overclaiming in administration answers. | Remove the latency and no-cache claims from this operations attachment, or reword as a sourced architecture summary without performance guarantees. Keep performance positioning in the performance attachment. |

## Source Checks

- Claims checked:
  - Installation order, `post_install.sh dbcreate`, `server create`, `server start`, iSQL verification, shutdown modes, PSM `catproc.sql`, license handling, user limits, kernel parameters, and THP guidance.
  - 8.1 platform support from release notes and 8.1 installation source.
  - Startup phase semantics, shutdown phase restrictions, archive/noarchive behavior, online/offline backup, media recovery, incomplete recovery with `RESETLOGS`, incremental backup files, and tablespace state/DDL behavior.
  - Data dictionary columns for `V$LOG`, `V$ARCHIVE`, `V$DATAFILES`, `V$TABLESPACES`, `V$MEM_TABLESPACES`, `V$VOL_TABLESPACES`, and 8.1 `V$MEM_STABLE`.
- Source coverage:
  - Strong for 7.1 installation and administration because the sampled manuals contain detailed procedures.
  - Strong for 8.1 platform support and checkpoint-scale behavior from 8.1 release notes and verified-source manuals.
  - `version_coverage_validation.md` confirms marker coverage for 7.1, 7.3, and 8.1 across the attachment set.
- Source gaps:
  - I did not execute SQL against a live Altibase instance, so query syntax was checked against manuals and attachment cross-references only.
  - I did not exhaustively verify every user/role privilege query in `02_administration_operations.md`; the stage review focused on installation, startup/shutdown, backup, recovery, and tablespace operation risk.

## Oracle-Overlap Decision

- Correctly compressed:
  - Ordinary account, role, grant/revoke, and generic SQL mechanics are kept brief compared with Altibase-specific operation, storage, backup, and recovery guidance.
- Too much generic Oracle material:
  - No major Oracle-overlap bloat was found in this stage.
- Missing Altibase-specific difference:
  - The 8.1-only `V$LOG.CHECKPOINT_SCALE` column must be separated from common 7.1/7.3 operational queries.
  - The 8.1 AIX 7.2 platform support difference must be included in the installation attachment, not only in the platform attachment.

## Version Checks

- 7.1:
  - Startup/shutdown, backup/recovery, archive/noarchive, tablespace states, and tablespace DDL broadly match the sampled 7.1 manuals.
  - The common `V$LOG` query currently includes an 8.1-only column and is not safe for 7.1.
- 7.3:
  - The stage file includes 7.3 coverage markers and the operational model appears mostly aligned with 7.1 for the reviewed procedures.
  - The common `V$LOG` query currently includes an 8.1-only column and is not safe for 7.3.
- 8.1:
  - File 00 correctly lists AIX 7.2, RHEL 7/8/9, and Windows client-only platform support for 8.1.
  - File 01 omits AIX 7.2 in two 8.1 installation/platform locations.
  - 8.1 checkpoint-scale handling is present, but the common `V$LOG` query needs version scoping.

## Retrieval And GPT Answer Quality

- Strengths:
  - File 02 has strong runbook coverage for DBA operations and uses the right operational pattern: identify state, check views, confirm backup, execute, verify, and state rollback/recovery limits.
  - Backup and recovery sections include important Altibase-specific cautions: `ARCHIVELOG`, current log anchors, stable memory checkpoint images, `RESETLOGS`, and follow-up full backup.
  - File 00 is a useful platform and upgrade anchor with concise version matrices and answer rules.
- Risks:
  - Conflicting 8.1 platform statements between files 00 and 01 can cause inconsistent installation answers.
  - A GPT may retrieve the common `V$LOG` query without the later 8.1 context and generate failing 7.1/7.3 SQL.
  - Some high-risk runbooks still read like summaries rather than exact procedures, especially memory checkpoint path changes and offline physical backups.

## Required Follow-Up

- Fix the two High platform issues in `01_getting_started_installation.md`.
- Split `V$LOG.CHECKPOINT_SCALE` into an 8.1-only check and keep 7.1/7.3 common log checks portable.
- Add the missing shutdown phase distinction for `SHUTDOWN ABORT`.
- Harden the memory checkpoint path and offline backup runbooks with complete command order, path discovery, OS file steps, and verification.
- Add an incremental recovery preflight for missing `changeTracking` and `backupInfo`.
