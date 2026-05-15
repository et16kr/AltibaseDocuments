# R07 Installation, Startup/Shutdown, Administration, Backup, Recovery, and Tablespace Operations

Date: 2026-05-15
Reviewer: Codex
Verdict: Pass

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
| Resolved High | `GPTs/attachments/02_administration_operations.md` | 805 | The disk datafile move runbook shows `OFFLINE`, `RENAME DATAFILE`, and `ONLINE`, but it does not include the required OS-level move/copy before the rename/online step. The note about moving the physical file appears after the SQL block and after `ONLINE`, so a GPT may produce an unsafe or failing command order. Source wording also needs reconciliation: the Administrator's Manual allows service-phase rename for offline tablespaces, while the SQL Reference says `ALTER TABLESPACE ... RENAME DATAFILE` is only during `CONTROL`. | Resolved by H04. The datafile move runbook is no longer an open High gate item. |
| Resolved High | `GPTs/attachments/02_administration_operations.md` | 1354 | Incremental restore/recovery coverage lists the basic `RESTORE DATABASE` and `RECOVER DATABASE` commands but omits the source-required handling for incomplete incremental recovery: restoring historical `loganchor*` and `backupInfo`, disabling invalid change tracking in `PROCESS`, then using `RESETLOGS`. This can produce an incomplete recovery answer that fails or leaves backup metadata inconsistent. | Resolved by H05. The incremental recovery runbook gap is no longer an open High gate item. |
| Resolved Medium | `GPTs/attachments/02_administration_operations.md` | 1073 | Offline physical backup said to copy memory checkpoint directories, log anchors, needed logs, and disk data files, but did not say to preserve the exact `$ALTIBASE_HOME/conf/altibase.properties` used at backup time. | Resolved by M08. The offline backup manifest now retains `altibase.properties` and includes a post-`server stop` verification before copying backup files. |
| Resolved Medium | `GPTs/attachments/02_administration_operations.md` | 1176 | The archive log mode change block started at `STARTUP CONTROL` and did not show the full service-impact sequence or verification. | Resolved by M09. The archive log mode material is now a service-impact runbook with mode checks, downtime planning, archive destination checks, clean stop, `STARTUP CONTROL`, verification, `STARTUP SERVICE`, and follow-up backup guidance. |
| Resolved Medium | `GPTs/attachments/01_getting_started_installation.md` | 331 | Patch rollback notes warned that installer rollback does not cover data or logs, but the meta downgrade section only said to stop the server first. | Resolved by M10. The rollback flow now includes backup, `server stop`, `server downgrade` when needed, APatch delete/uninstall, and binary/meta-version verification. |
| Resolved Low | `GPTs/attachments/02_administration_operations.md` | 89 | The administration attachment used `isql -u sys -p manager -sysdba` for high-risk operations but did not repeat the production-safety note that `manager` is only a manual example. | Resolved by L04. The SYSDBA example block now tells users to use the site-specific `SYS` password and avoid embedding production passwords. |
| Resolved Low | `GPTs/attachments/02_administration_operations.md` | 18 | The architecture block used promotional wording such as "extreme high-performance (microsecond latency)" and "requires no external caching layer". | Resolved by M03. The architecture block now uses source-neutral hybrid storage guidance without latency or cache-layer guarantees. |

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
- Closed by H04: disk datafile rename phase behavior is now split into explicit service/offline and `CONTROL` runbooks with source-policy cautioning.

## Oracle-Overlap Decision

- Correctly compressed:
  - The reviewed attachments avoid generic Oracle DML and focus on Altibase installation, phases, properties, tablespaces, backup, recovery, and operational views.
- Too much generic Oracle material:
  - None found in this stage.
- Missing Altibase-specific difference:
  - Prior incremental incomplete recovery and datafile/checkpoint-image flow gaps are closed by H04 and H05.

## Version Checks

- 7.1:
  - Installation, startup/shutdown, online/offline backup, archive log mode, media recovery, and incremental backup material is broadly source-backed.
  - Offline backup property-file retention, patch rollback, datafile move ordering, and incomplete incremental recovery follow-ups are closed by H04, H05, M08, M09, and M10.
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
  - The original High datafile move and recovery command-block risks are closed by H04 and H05.
  - The Medium/Low operational follow-ups are closed by M08, M09, M10, L04, and M03.

## V02 Closure

- Closed by H04 and H05: the two original High findings in `02_administration_operations.md`.
- Closed by M08, M09, and M10: offline backup, archive log mode, and patch rollback operational-safety improvements.
- Closed by L04 and M03: SYSDBA password safety and source-neutral architecture wording.
- No open R07 finding remains after V02 re-review of the changed sections.
