# R07 Installation, Startup/Shutdown, Administration, Backup, Recovery, and Tablespace Operations

Date: 2026-05-15
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
  - `Manuals/Altibase_7.1/eng/SQL Reference.md`
  - `Manuals/Altibase_7.1/eng/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_7.3/eng/Administrator’s Manual.md`
  - `Manuals/Altibase_trunk/eng/Administrator’s Manual.md`
  - `Manuals/Altibase_trunk/eng/SQL Reference.md`
  - `Manuals/Altibase_trunk/eng/General Reference-2.The Data Dictionary.md`
  - `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`

## Commands Run

```bash
sed -n '1,240p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,220p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,260p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
wc -l GPTs/attachments/00_version_release_platform.md GPTs/attachments/01_getting_started_installation.md GPTs/attachments/02_administration_operations.md GPTs/reports/version_coverage_validation.md
rg -n "^## |^### |^Item:|^Phase block:|^Command block:|^Operation block:|^Backup|^Recovery|^Tablespace|^Version|^Caution|^Checklist|^Risk" GPTs/attachments/02_administration_operations.md
rg -n "STARTUP|SHUTDOWN|ARCHIVELOG|NOARCHIVELOG|BEGIN BACKUP|END BACKUP|RECOVER DATABASE|RESTORE DATABASE|RESETLOGS|CREATE DATAFILE|CREATE CHECKPOINT IMAGE|DISCARD|CHECKPOINT PATH|INCREMENTAL|CHANGE BACKUP DIRECTORY" "Manuals/Altibase_7.1/eng/Administrator's Manual.md"
rg -n "post_install|pre_install|server create|server start|server stop|startup|shutdown|license|Transparent Huge|THP|ulimit|kernel|catproc|Patch Installation|APatch|server downgrade" "Manuals/Altibase_7.1/eng/Getting Started Guide.md" "Manuals/Altibase_7.1/eng/Installation Guide.md"
rg -n "IF NOT EXISTS|CREATE.*TABLESPACE|DROP TABLESPACE|ALTER TABLESPACE" Manuals/Altibase_trunk/eng/SQL\ Reference.md Manuals/Altibase_trunk/eng/Administrator*Manual.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name README.md | sort | wc -l
rg -n "BEGIN BACKUP|END BACKUP|RECOVER DATABASE|RESTORE DATABASE|RESETLOGS|DISCARD|ARCHIVELOG|NOARCHIVELOG|RENAME DATAFILE|CREATE DATAFILE|CREATE CHECKPOINT IMAGE|CHECKPOINT SCALE|server stop|server kill|post_install|pre_install" GPTs/attachments/00_version_release_platform.md GPTs/attachments/01_getting_started_installation.md GPTs/attachments/02_administration_operations.md
rg -n 'trunk|file://|/home/et16|media/|\.gif|\.png|\.jpg|C:\\' GPTs/attachments/00_version_release_platform.md GPTs/attachments/01_getting_started_installation.md GPTs/attachments/02_administration_operations.md
```

## Findings

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| High | `GPTs/attachments/02_administration_operations.md` | 805 | The disk datafile move runbook shows `OFFLINE`, `RENAME DATAFILE`, and `ONLINE`, but it does not include the required OS-level move/copy before the rename/online step. The note about moving the physical file appears after the SQL block and after `ONLINE`, so a GPT may produce an unsafe or failing command order. Source wording also needs reconciliation: the Administrator's Manual allows service-phase rename for offline tablespaces, while the SQL Reference says `ALTER TABLESPACE ... RENAME DATAFILE` is only during `CONTROL`. | Split this into explicit runbooks: planned service/offline move if accepted by source policy, and recovery/`CONTROL` move. In both, include precheck, stop/offline or `STARTUP CONTROL`, OS copy/move to the target path, ownership/permission check, `ALTER ... RENAME DATAFILE`, `V$DATAFILES` verification, then `ONLINE` or `SERVICE`. Add a source-audit note for the Admin Manual vs SQL Reference phase difference. |
| High | `GPTs/attachments/02_administration_operations.md` | 1354 | Incremental restore/recovery coverage lists the basic `RESTORE DATABASE` and `RECOVER DATABASE` commands but omits the source-required handling for incomplete incremental recovery: restoring historical `loganchor*` and `backupInfo`, disabling invalid change tracking in `PROCESS`, then using `RESETLOGS`. This can produce an incomplete recovery answer that fails or leaves backup metadata inconsistent. | Add separate incremental recovery runbooks for complete recovery, incomplete recovery by tag, and incomplete recovery by `UNTIL TIME` or `UNTIL CANCEL`. Include when to restore old `loganchor*` and `backupInfo`, when to run `ALTER DATABASE DISABLE INCREMENTAL CHUNK CHANGE TRACKING` in `PROCESS`, tag matching rules, temporary-file recreation, `META RESETLOGS`, and the required full backup afterward. |
| Medium | `GPTs/attachments/02_administration_operations.md` | 1073 | Offline physical backup says to copy memory checkpoint directories, log anchors, needed logs, and disk data files, but it does not say to preserve the exact `$ALTIBASE_HOME/conf/altibase.properties` used at backup time. The source recovery section states that the properties file used when the database was backed up must be used during recovery. | Add `$ALTIBASE_HOME/conf/altibase.properties` to the offline backup manifest, or explicitly state that it must be retained and restored with the backup set. Also add a post-`server stop` verification step before copying files so the backup is not taken while logs are still changing. |
| Medium | `GPTs/attachments/02_administration_operations.md` | 1176 | The archive log mode change block starts at `STARTUP CONTROL` and runs `ALTER DATABASE ARCHIVELOG` or `ALTER DATABASE NOARCHIVELOG`, but it does not show the full service-impact sequence or verification. Since phases only move forward and mode changes require `CONTROL`, a production answer needs shutdown planning, archive destination capacity checks, transition back to service, and mode verification. | Convert this block into a runbook: confirm current `V$LOG.ARCHIVELOG_MODE` and `V$ARCHIVE`, plan downtime, cleanly stop service, connect `SYSDBA`, `STARTUP CONTROL`, alter mode, verify, `STARTUP SERVICE`, and confirm archive destination behavior. Add backup follow-up guidance after changing mode if local policy requires a new baseline. |
| Medium | `GPTs/attachments/01_getting_started_installation.md` | 331 | Patch rollback notes correctly warn that installer rollback does not cover data or logs, but the meta downgrade section only says to stop the server first. The Installation Guide also says that after `server downgrade`, the user must delete the patch; otherwise running the server can trigger meta upgrade again. | Add the missing post-downgrade rollback/delete-patch step and make the order explicit: backup product/data/logs, `server stop`, run `server downgrade` when needed, run the APatch patch uninstaller/delete step, then verify binary and meta versions. |
| Low | `GPTs/attachments/02_administration_operations.md` | 89 | The administration attachment uses `isql -u sys -p manager -sysdba` for high-risk operations but does not repeat the production-safety note found in the installation attachment that `manager` is only a manual example and must be replaced if changed. | Add one short note near the SYSDBA command block: examples use `sys` and `manager`; use the site-specific `SYS` password and avoid embedding production passwords in reusable scripts. |
| Low | `GPTs/attachments/02_administration_operations.md` | 18 | The architecture block uses promotional wording such as "extreme high-performance (microsecond latency)" and "requires no external caching layer". This is not an operational safety bug, but it is less source-neutral than the rest of the attachment and could lead to overconfident GPT answers. | Reword as source-backed architecture guidance: Altibase supports memory, disk, and volatile tablespaces in one engine; choose storage by persistence, size, and performance requirements. Avoid latency claims unless tied to a precise source and workload. |

## Source Checks

- Claims checked:
  - Installation prerequisites, package flow, license handling, `pre_install.sh`, `post_install.sh dbcreate`, `catproc.sql`, startup, shutdown, and patch rollback.
  - Startup phases, `SHUTDOWN NORMAL`, `SHUTDOWN IMMEDIATE`, `SHUTDOWN ABORT`, `server stop`, and `server kill`.
  - Tablespace states, `DISCARD`, disk/memory/volatile/temporary/undo concepts, `CREATE TABLESPACE`, `ALTER TABLESPACE`, datafile/tempfile changes, checkpoint paths, and `IF NOT EXISTS` for 8.1.
  - Online backup, offline backup, archive log mode, media recovery, incomplete recovery, incremental backup/recovery, `backupInfo`, `changeTracking`, `RESETLOGS`, and 8.1 checkpoint scale.
- Source coverage:
  - 7.1 source coverage was sampled in depth because the stage hints identify 7.1 manuals.
  - 7.3 and 8.1 were checked for corresponding Administrator's Manual, SQL Reference, data dictionary, and release-note markers where version behavior differs.
  - `GPTs/reports/version_coverage_validation.md` reports pass-level marker coverage for all 20 attachments.
- Source gaps:
  - Disk datafile rename phase behavior needs source-policy resolution because the Administrator's Manual and SQL Reference wording differ. The attachment should not leave this ambiguous in a production move runbook.

## Oracle-Overlap Decision

- Correctly compressed:
  - The reviewed attachments avoid generic Oracle DML and focus on Altibase installation, phases, properties, tablespaces, backup, recovery, and operational views.
- Too much generic Oracle material:
  - None found in this stage.
- Missing Altibase-specific difference:
  - Incremental incomplete recovery needs Altibase-specific `backupInfo`, `changeTracking`, and log anchor handling.
  - Datafile and checkpoint-image move/recovery flows need stricter Altibase-specific command ordering and phase wording.

## Version Checks

- 7.1:
  - Installation, startup/shutdown, online/offline backup, archive log mode, media recovery, and incremental backup material is broadly source-backed.
  - Follow-up needed for offline backup property-file retention, patch rollback, datafile move ordering, and incomplete incremental recovery.
- 7.3:
  - The attachment states the same operational model as 7.1 for covered backup/recovery/tablespace operations. No 7.3-specific contradiction was found in sampled checks.
- 8.1:
  - 8.1 platform and feature routing in `00_version_release_platform.md` is customer-safe and avoids internal source labels.
  - 8.1 checkpoint scale, `V$LOG.CHECKPOINT_SCALE`, `V$MEM_STABLE`, and `SINGLE`/`PAIR` guidance is source-backed in sampled checks.

## Retrieval And GPT Answer Quality

- Strengths:
  - The attachments have strong question-oriented structure, literal command preservation, and useful operational check SQL.
  - `02_administration_operations.md` is rich enough for retrieval on backup, recovery, tablespaces, and operational views.
  - Upload-boundary validation found 20 attachment Markdown files, excluding `README.md`; the three stage attachments had no matches for `trunk`, `file://`, local workspace paths, or raw image references in the validation regex.
- Risks:
  - High-risk code blocks may be retrieved without nearby notes. The datafile move and recovery command blocks need to include safety steps inside the procedure, not only in surrounding prose.
  - Incremental recovery is complex enough that a compact command block can mislead unless it separates complete, incomplete, and tag-based cases.

## Required Follow-Up

- Fix the two High findings in `02_administration_operations.md` before upload.
- Add the Medium operational-safety improvements for offline backup, archive log mode changes, and patch rollback.
- Resolve or explicitly document the source-policy decision for `ALTER TABLESPACE ... RENAME DATAFILE` phase requirements.
- After edits, rerun focused validation for the same stage and re-review the changed sections only.
