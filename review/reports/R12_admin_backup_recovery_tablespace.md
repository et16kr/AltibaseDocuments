# R12 Administration, Backup/Recovery, and Tablespace Operations

Date: 2026-05-16
Reviewer: Codex
Verdict: Pass

## Scope

- Attachments:
  - `GPTs/attachments/02_administration_operations.md`
  - `GPTs/attachments/03_sql_ddl_generation.md`
  - `GPTs/attachments/06_data_dictionary_performance_views.md`
- Supporting reports:
  - `GPTs/reports/source_inventory.md`
  - `GPTs/reports/eng_kor_parity.md`
- Source manuals sampled:
  - `Manuals/Altibase_7.1/kor/Administrator's Manual.md`
  - `Manuals/Altibase_7.3/kor/Administrator's Manual.md`
  - `Manuals/Altibase_trunk/kor/Administrator's Manual.md`
  - `Manuals/Altibase_7.1/kor/SQL Reference.md`
  - `Manuals/Altibase_7.3/kor/SQL Reference.md`
  - `Manuals/Altibase_trunk/kor/SQL Reference.md`
  - `Manuals/Altibase_7.1/kor/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`
  - `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`

## Commands Run

```bash
bash review/scripts/run_review_remediation_cycle.sh status
rg -n $'\t(Reviewing|Remediating|ReReviewing|Fail)$' review/review_remediation_cycle_status.tsv
git status --short
sed -n '1,220p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,220p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,260p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
git diff -- GPTs/attachments/02_administration_operations.md
git diff -- GPTs/attachments/03_sql_ddl_generation.md
git diff -- GPTs/attachments/06_data_dictionary_performance_views.md
wc -l GPTs/attachments/02_administration_operations.md GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/06_data_dictionary_performance_views.md
nl -ba GPTs/attachments/02_administration_operations.md | sed -n '1,2117p'
nl -ba GPTs/attachments/03_sql_ddl_generation.md | sed -n '1,240p'
nl -ba GPTs/attachments/03_sql_ddl_generation.md | sed -n '700,1120p'
nl -ba GPTs/attachments/06_data_dictionary_performance_views.md | sed -n '620,700p'
nl -ba GPTs/attachments/06_data_dictionary_performance_views.md | sed -n '1500,1565p'
rg -n "BACKUP INCREMENTAL|CUMULATIVE|RESTORE DATABASE|RECOVER DATABASE|UNTIL CANCEL|ENABLE INCREMENTAL|CHANGE BACKUP|backupInfo|changeTracking" Manuals/Altibase_7.1/kor/Administrator\'s\ Manual.md Manuals/Altibase_7.3/kor/Administrator\'s\ Manual.md Manuals/Altibase_trunk/kor/Administrator\'s\ Manual.md
rg -n "TEMPORARY|temporary|임시|temp\\.dbf|CREATE DATAFILE|SYS_TBS_DISK_TEMP|온라인.*백업|백업.*임시" Manuals/Altibase_7.1/kor/Administrator\'s\ Manual.md Manuals/Altibase_7.3/kor/Administrator\'s\ Manual.md Manuals/Altibase_trunk/kor/Administrator\'s\ Manual.md
rg -n "CREATE TABLESPACE|DROP TABLESPACE|ALTER TABLESPACE|RENAME DATAFILE|BEGIN BACKUP|END BACKUP|IF NOT EXISTS|IF EXISTS|MANAGE TABLESPACE|LIMIT \\(|DISABLE TCP|ACCOUNT LOCK|BACKUP INCREMENTAL|RESTORE DATABASE|RECOVER DATABASE" Manuals/Altibase_7.1/kor/SQL\ Reference.md Manuals/Altibase_7.3/kor/SQL\ Reference.md Manuals/Altibase_trunk/kor/SQL\ Reference.md
rg -n "RESTORE TABLESPACE|restore_tablespace_clause|TABLESPACE .*RESTORE|RESTORE .*TABLESPACE|복원.*테이블스페이스|테이블스페이스.*복원" Manuals/Altibase_7.1/kor/Administrator\'s\ Manual.md Manuals/Altibase_7.3/kor/Administrator\'s\ Manual.md Manuals/Altibase_trunk/kor/Administrator\'s\ Manual.md Manuals/Altibase_7.1/kor/SQL\ Reference.md Manuals/Altibase_7.3/kor/SQL\ Reference.md Manuals/Altibase_trunk/kor/SQL\ Reference.md GPTs/attachments/02_administration_operations.md GPTs/attachments/03_sql_ddl_generation.md
rg -n "### V\\\\\\$DATAFILES|INITSIZE|CURRSIZE|NEXTSIZE|MAXSIZE|PAGE_SIZE|### V\\\\\\$TABLESPACES|### V\\\\\\$MEM_STABLE|CHECKPOINT_SCALE|### V\\\\\\$BACKUP_INFO|### V\\\\\\$ARCHIVE|### V\\\\\\$LOG" Manuals/Altibase_7.1/kor/General\ Reference-2.The\ Data\ Dictionary.md Manuals/Altibase_7.3/kor/General_Reference-2.The\ Data\ Dictionary.md Manuals/Altibase_trunk/kor/General_Reference-2.The\ Data\ Dictionary.md
sed -n '2590,2725p' Manuals/Altibase_trunk/kor/SQL\ Reference.md
sed -n '5040,5265p' Manuals/Altibase_trunk/kor/SQL\ Reference.md
sed -n '8860,9385p' Manuals/Altibase_trunk/kor/SQL\ Reference.md
sed -n '10724,10820p' Manuals/Altibase_trunk/kor/SQL\ Reference.md
sed -n '5180,5265p' Manuals/Altibase_trunk/kor/General_Reference-2.The\ Data\ Dictionary.md
sed -n '11540,11670p' Manuals/Altibase_trunk/kor/General_Reference-2.The\ Data\ Dictionary.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name README.md | sort | wc -l
rg -n "trunk|file://|C:/|/home/|media/|!\[|Altibase_trunk" GPTs/attachments/02_administration_operations.md GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/06_data_dictionary_performance_views.md
rg -n 'INCREMENTAL BACKUP|RECOVER TABLESPACE|RESTORE DATABASE UNTIL CANCEL|Temporary tablespaces are not backed up|They cannot be backed up\.|d\.currsize,$|d\.maxsize,$|d\.initsize,$|d\.nextsize,|MANAGE TABLESPACE' GPTs/attachments/02_administration_operations.md GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/06_data_dictionary_performance_views.md
git diff --check
bash review/scripts/run_review_stage.sh validate
```

## Findings

No actionable `Blocker`, `High`, `Medium`, or `Low` findings remain for this stage.

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Note | All scoped attachments | 0 | R12 re-review found the prior actionable findings remediated and did not find new upload-blocking or customer-risk issues in the sampled administration, backup/recovery, tablespace, and supporting dictionary content. | No R12 remediation required. Keep the current source-grounded operational safety wording. |

## Source Checks

- Claims checked:
  - Account and administration procedures: built-in `SYSTEM_` and `SYS`, user creation and alteration, `ACCOUNT LOCK`, TCP enable/disable, password policy `LIMIT`, role and grant prerequisites, automatic baseline privileges for new ordinary users, and the `MANAGE TABLESPACE` SYS-only caveat.
  - Tablespace operations: disk, memory, volatile, temporary, and undo tablespace types; `ONLINE`, `OFFLINE`, `DISCARD`, backup state; `CREATE`, `ALTER`, `DROP`, file and checkpoint path operations; temporary file handling; system tablespace restrictions.
  - Backup and recovery: offline physical backup, online database and tablespace backup, `BEGIN BACKUP`/`END BACKUP`, archive mode changes, complete and incomplete media recovery, `META RESETLOGS`, incremental backup, `RESTORE DATABASE`, `RECOVER DATABASE`, `backupInfo`, `changeTracking`, temporary file recreation, and log anchor handling.
  - Dictionary support: `V$LOG`, `V$ARCHIVE`, `V$TABLESPACES`, `V$DATAFILES`, `V$MEM_TABLESPACES`, `V$VOL_TABLESPACES`, `V$MEM_STABLE`, and `V$BACKUP_INFO`.
- Source coverage:
  - Korean Administrator manuals for 7.1, 7.3, and 8.1 verified source all support `ALTER DATABASE BACKUP INCREMENTAL LEVEL ...`, not the reversed `INCREMENTAL BACKUP` order. The attachment grammar now follows that order in `GPTs/attachments/03_sql_ddl_generation.md:737`.
  - Korean Administrator manuals support level 1 cumulative syntax with `CUMULATIVE`, while the ordinary level 1 form is the differential form. `GPTs/attachments/03_sql_ddl_generation.md:879` now explicitly says not to generate a `DIFFERENTIAL` keyword.
  - Korean SQL Reference text supports `RECOVER DATABASE`, `RECOVER DATABASE UNTIL TIME`, and `RECOVER DATABASE UNTIL CANCEL`; the compact generation grammar no longer emits `RECOVER TABLESPACE`.
  - Korean Administrator manuals explicitly state that `RESTORE DATABASE UNTIL CANCEL` is not supported for incremental backup restoration while `UNTIL TIME` is possible. `GPTs/attachments/02_administration_operations.md:1701` and `GPTs/attachments/03_sql_ddl_generation.md:879` now preserve that distinction.
  - Korean Administrator and SQL Reference text supports temporary tablespaces as disk work space that cannot be online tablespace-backed-up, while offline physical backup examples include discovered temporary files and media/incremental recovery may recreate missing temporary files. `GPTs/attachments/02_administration_operations.md:581`, `GPTs/attachments/02_administration_operations.md:1106`, and `GPTs/attachments/02_administration_operations.md:1769` now scope the rule by backup/recovery mode.
  - Korean General Reference 2 defines `V$DATAFILES.INITSIZE`, `CURRSIZE`, `NEXTSIZE`, and `MAXSIZE` as page counts and `V$TABLESPACES.PAGE_SIZE` as bytes. The scoped attachments now expose page aliases and byte/MB conversions in the sampled operational queries.
  - Korean SQL Reference privilege tables state that `MANAGE TABLESPACE` is not granted to users other than `SYS`. `GPTs/attachments/02_administration_operations.md:338` now says not to grant or recommend it in customer grant scripts.
- Korean/English source conflicts:
  - The known datafile rename wording drift remains safely handled: `GPTs/attachments/02_administration_operations.md:963` documents that the Administrator's Manual allows a service/offline path, while SQL Reference limits `RENAME DATAFILE` to `CONTROL`; the customer-facing default remains the stricter `CONTROL` runbook.
  - No additional Korean/English conflict was found that changes R12 recommendations.
- Source gaps:
  - Some SQL Reference grammar details remain image-only in the source manuals. The scoped attachments avoid generating unsupported or unaudited `RECOVER TABLESPACE` syntax. If future work adds tablespace-level `RESTORE TABLESPACE` generation from the `restore_tablespace_clause` image, audit the original diagram per target version before adding it.
  - This was a static document review. SQL examples were source-checked but not executed against a live Altibase instance.

## Oracle-Overlap Decision

- Correctly compressed:
  - The reviewed content stays focused on Altibase-specific administration, storage, tablespace, backup/recovery, and dictionary behavior.
- Too much generic Oracle material:
  - None found in this stage.
- Missing Altibase-specific difference:
  - No actionable missing difference remains in the sampled operational areas. The prior gaps around incremental backup order, recovery/restore boundaries, temporary tablespace backup scope, `V$DATAFILES` units, and `MANAGE TABLESPACE` were addressed.

## Version Checks

- 7.1:
  - Sampled Korean Administrator and SQL Reference content supports the current startup phase, archive mode, online backup, media recovery, incremental backup, tablespace DDL, user, privilege, and page-count handling.
  - The scoped attachments continue to omit 8.1-only `IF NOT EXISTS` and `IF EXISTS` forms for 7.1 guidance.
- 7.3:
  - Sampled Korean sources align with 7.1 for the covered backup/recovery and tablespace operations. The current attachment wording remains valid for the sampled 7.3 procedures.
  - The scoped attachments continue to omit 8.1-only `IF NOT EXISTS` and `IF EXISTS` forms for 7.3 guidance.
- 8.1:
  - 8.1 verified source supports the sampled `IF NOT EXISTS`/`IF EXISTS` syntax, `CHECKPOINT_SCALE`, `SINGLE`/`PAIR`, and `V$MEM_STABLE` coverage.
  - 8.1 sampled sources use the same `BACKUP INCREMENTAL` order and `RESTORE DATABASE UNTIL CANCEL` restriction as 7.1 and 7.3.

## Retrieval And GPT Answer Quality

- Strengths:
  - `02_administration_operations.md` now gives customer-safe runbooks with prechecks, phase requirements, backup prerequisites, verification queries, destructive-operation cautions, and post-recovery backup follow-up.
  - `03_sql_ddl_generation.md` now keeps compact backup/recovery grammar conservative and source-backed, reducing the chance that GPT-generated SQL picks an invalid administrative command.
  - `06_data_dictionary_performance_views.md` now makes datafile size units explicit enough for capacity and autoextend answers.
- Risks:
  - Exact grammar for some image-only SQL Reference diagrams was sampled through surrounding text and examples, not fully reconstructed from the diagrams. Current attachment text avoids unsupported syntax where the diagram was not audited.
  - No live database validation was run, so final production answers should still ask for target version, startup phase, archive mode, backup evidence, and file paths before issuing destructive or recovery commands.

## Required Follow-Up

- None for R12. The stage is ready for the cycle runner to mark done and commit, subject to the normal repository validation and review-cycle workflow.
