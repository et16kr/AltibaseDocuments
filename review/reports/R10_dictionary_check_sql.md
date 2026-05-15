# R10 Data Dictionary, Performance Views, and Check SQL

Date: 2026-05-16
Reviewer: Codex
Verdict: Pass

## Scope

- Attachments:
  - `GPTs/attachments/06_data_dictionary_performance_views.md`
  - `GPTs/attachments/05_data_types_properties.md`
  - `GPTs/attachments/07_error_messages_troubleshooting.md`
- Supporting reports:
  - Current R10 re-review state and existing worktree remediation.
  - `GPTs/reports/source_inventory.md`
- Source manuals sampled:
  - `Manuals/Altibase_7.1/kor/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_7.1/kor/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_7.3/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_7.1/kor/SQL Reference.md`
  - `Manuals/Altibase_7.3/kor/SQL Reference.md`
  - `Manuals/Altibase_trunk/kor/SQL Reference.md`
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
git diff -- GPTs/attachments/06_data_dictionary_performance_views.md GPTs/attachments/05_data_types_properties.md GPTs/attachments/07_error_messages_troubleshooting.md GPTs/reports/source_inventory.md review/review_remediation_cycle_status.tsv review/review_stage_status.tsv
wc -l GPTs/attachments/06_data_dictionary_performance_views.md GPTs/attachments/05_data_types_properties.md GPTs/attachments/07_error_messages_troubleshooting.md Manuals/Altibase_7.1/kor/General\ Reference-2.The\ Data\ Dictionary.md Manuals/Altibase_7.3/kor/General_Reference-2.The\ Data\ Dictionary.md Manuals/Altibase_trunk/kor/General_Reference-2.The\ Data\ Dictionary.md Manuals/Altibase_7.1/kor/General\ Reference-1.Data\ Types\ \&\ Altibase\ Properties.md Manuals/Altibase_7.3/kor/General_Reference-1.Data\ Types\ \&\ Altibase\ Properties.md Manuals/Altibase_trunk/kor/General_Reference-1.Data\ Types\ \&\ Altibase\ Properties.md
rg -n "^(#|##|###) " GPTs/attachments/06_data_dictionary_performance_views.md GPTs/attachments/05_data_types_properties.md GPTs/attachments/07_error_messages_troubleshooting.md
rg -n "\b(V\$|SYSTEM_\.|SYS_|IS_CONDITION_SYNCED|TEMPORARY_LOB|LOCK_TIMEOUT|DDL_LOCK_TIMEOUT|USER_LOCK_REQUEST_TIMEOUT|REPLICATION_LOCK_TIMEOUT|REPLICATION_SYNC_LOCK_TIMEOUT|WAIT n|NOWAIT)" GPTs/attachments/06_data_dictionary_performance_views.md GPTs/attachments/05_data_types_properties.md GPTs/attachments/07_error_messages_troubleshooting.md
rg -n "V\$LOCK_TABLE_STATS|V\$MEM_STABLE|V\$TEMPORARY_LOBS|SYS_REPL_ITEMS_|IS_CONDITION_SYNCED|Temporary LOB|메타 테이블|성능 뷰" ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md Manuals/Altibase_7.1/kor/General\ Reference-2.The\ Data\ Dictionary.md Manuals/Altibase_7.3/kor/General_Reference-2.The\ Data\ Dictionary.md Manuals/Altibase_trunk/kor/General_Reference-2.The\ Data\ Dictionary.md
rg -n "DDL_LOCK_TIMEOUT|USER_LOCK_REQUEST_TIMEOUT|REPLICATION_LOCK_TIMEOUT|REPLICATION_SYNC_LOCK_TIMEOUT|LOCK_TIMEOUT|TEMPORARY_LOB_ENABLE|MEMORY_TEMPLOB|REPLICATION_SSL_PORT_NO|CHECKPOINT_SCALE_SINGLE_DW_BUFFER_SIZE|TRCLOG_JSON_PLAN_INDENT_DEPTH" Manuals/Altibase_7.1/kor/General\ Reference-1.Data\ Types\ \&\ Altibase\ Properties.md Manuals/Altibase_7.3/kor/General_Reference-1.Data\ Types\ \&\ Altibase\ Properties.md Manuals/Altibase_trunk/kor/General_Reference-1.Data\ Types\ \&\ Altibase\ Properties.md ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md
rg -n "LOCK TABLE|FOR UPDATE|WAIT|NOWAIT" Manuals/Altibase_7.1/kor/SQL\ Reference.md Manuals/Altibase_7.3/kor/SQL\ Reference.md Manuals/Altibase_trunk/kor/SQL\ Reference.md
rg -n "REPLICATION_RECEIVE_TIMEOUT|TABLESPACE_LOCK_ENABLE|REGEXP_MODE|MEM_MAX_DB_SIZE|VOLATILE_MAX_DB_SIZE" Manuals/Altibase_7.1/kor/General\ Reference-1.Data\ Types\ \&\ Altibase\ Properties.md Manuals/Altibase_7.3/kor/General_Reference-1.Data\ Types\ \&\ Altibase\ Properties.md Manuals/Altibase_trunk/kor/General_Reference-1.Data\ Types\ \&\ Altibase\ Properties.md
python3 - <<'PY'
# Compared attachment V$ and SYSTEM_.SYS_* object tokens against Korean General Reference 2.
PY
python3 - <<'PY'
# Compared property-like tokens and V$PROPERTY predicates against Korean property manuals and 8.1 release notes.
PY
python3 - <<'PY'
# Parsed sampled dictionary schemas and checked representative attachment SQL column references.
PY
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name README.md | wc -l
rg -n "trunk|file://|C:/|Manuals/|ReleaseNotes/|Altibase_trunk" GPTs/attachments/06_data_dictionary_performance_views.md GPTs/attachments/05_data_types_properties.md GPTs/attachments/07_error_messages_troubleshooting.md
git diff --check
bash review/scripts/run_review_stage.sh validate
git status --short
rg -n "^Verdict:|^\| (Blocker|High|Medium|Low) \|" review/reports/R10_dictionary_check_sql.md
```

## Findings

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Note | `GPTs/attachments/06_data_dictionary_performance_views.md`; `GPTs/attachments/05_data_types_properties.md`; `GPTs/attachments/07_error_messages_troubleshooting.md` | - | No actionable `Blocker`, `High`, `Medium`, or `Low` findings remain for R10. The previously reported unsupported `LOCK_TIMEOUT` check has been replaced in the current worktree with source-backed `DDL_LOCK_TIMEOUT`, `USER_LOCK_REQUEST_TIMEOUT`, `REPLICATION_LOCK_TIMEOUT`, `REPLICATION_SYNC_LOCK_TIMEOUT`, and SQL `WAIT n`/`NOWAIT` guidance. | No R10 attachment remediation is required. Keep the existing version-availability checks before using version-sensitive views or columns. |

## Source Checks

- Claims checked:
  - `SYSTEM_.SYS_REPL_ITEMS_.IS_CONDITION_SYNCED` version scope and guarded check SQL.
  - Performance view existence and sampled columns for `V$PROPERTY`, `V$TABLE`, `V$ALLCOLUMN`, `V$VERSION`, `V$DATATYPE`, `V$SESSION`, `V$STATEMENT`, `V$SQLTEXT`, `V$LOCK`, `V$LOCK_WAIT`, `V$LOCK_STATEMENT`, `V$TRANSACTION`, `V$SQL_PLAN_CACHE`, `V$SQL_PLAN_CACHE_PCO`, `V$SQL_PLAN_CACHE_SQLTEXT`, `V$TABLESPACES`, `V$DATAFILES`, `V$MEM_TABLESPACES`, `V$MEM_STABLE`, `V$TEMPORARY_LOBS`, `V$REPEXEC`, `V$REPGAP`, `V$REPSENDER`, `V$REPRECEIVER`, and `V$REPRECEIVER_COLUMN`.
  - Meta-table names and sampled columns for object, privilege, procedure, trigger, database link, and replication lookup SQL.
  - Property-linked check SQL for `QUERY_TIMEOUT`, `TIME_ZONE`, `SQL_PLAN_CACHE_SIZE`, `TEMPORARY_LOB_ENABLE`, `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`, `MEMORY_TEMPLOB_PIECE_SIZE`, `REPLICATION_SSL_PORT_NO`, `REPLICATION_RECEIVE_TIMEOUT`, `TABLESPACE_LOCK_ENABLE`, and lock-related timeout properties.
  - SQL lock-wait wording for `LOCK TABLE`, `SELECT ... FOR UPDATE`, `WAIT n`, and `NOWAIT`.
  - 8.1 release-note claims for Temporary LOB and added performance views including `V$MEM_STABLE` and `V$TEMPORARY_LOBS`.
- Source coverage:
  - Korean 7.1, 7.3, and 8.1 General Reference 2 support the sampled common dictionary and performance-view object names.
  - `SYSTEM_.SYS_REPL_ITEMS_.IS_CONDITION_SYNCED` is documented for 7.3 and 8.1, and the attachment correctly omits it from the common 7.1-compatible query unless the target database exposes it.
  - Korean 8.1 General Reference 2 and release notes support `V$MEM_STABLE`, `V$TEMPORARY_LOBS`, and the Temporary LOB check columns `TYPE`, `ID`, `ALLOCED_SIZE`, and `OPEN_COUNT`.
  - Korean property manuals support the remediated lock-timeout property names and the common troubleshooting property list.
- Korean/English source conflicts:
  - None newly identified in this stage. The sampled checks used Korean manuals and Korean release notes as the technical basis.
- Source gaps:
  - The review sampled and mechanically checked high-risk object names and many representative column references, but did not exhaustively prove every column in every large performance view across all patch levels. The attachment's existing guidance to check exact target layouts with `V$TABLE`, `V$ALLCOLUMN`, `SYSTEM_.SYS_TABLES_`, and `SYSTEM_.SYS_COLUMNS_` remains important.

## Oracle-Overlap Decision

- Correctly compressed:
  - The scoped files stay focused on Altibase-specific dictionary objects, performance views, property checks, troubleshooting checks, and operational verification SQL.
- Too much generic Oracle material:
  - None found in this stage.
- Missing Altibase-specific difference:
  - None remaining for R10 after the lock-timeout remediation.

## Version Checks

- 7.1:
  - Common replication item SQL omits `IS_CONDITION_SYNCED`, which is not part of the sampled 7.1 `SYSTEM_.SYS_REPL_ITEMS_` layout.
  - Lock troubleshooting now uses 7.1-documented lock-related properties and SQL wait syntax rather than unsupported `LOCK_TIMEOUT`.
- 7.3:
  - `SYSTEM_.SYS_REPL_ITEMS_.IS_CONDITION_SYNCED` is documented and guarded by a meta-table column availability check.
  - Lock, replication, property, and common dictionary checks sampled in this stage are source-backed.
- 8.1:
  - Temporary LOB checks use 8.1-only `V$TEMPORARY_LOBS` and source-backed `TEMPORARY_LOB_ENABLE`, `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`, and `MEMORY_TEMPLOB_PIECE_SIZE`.
  - `V$MEM_STABLE` is framed as an 8.1 stable checkpoint image check, and availability checks are present before relying on version-sensitive views.

## Retrieval And GPT Answer Quality

- Strengths:
  - `06_data_dictionary_performance_views.md` has strong question-oriented headings, cookbook SQL, object blocks, and answer templates.
  - Literal system names, performance view names, property names, SQL keywords, error codes, and version labels are preserved.
  - Version-sensitive view and meta-table column usage is guarded by availability checks instead of assuming one layout for all versions.
  - `07_error_messages_troubleshooting.md` now surfaces source-backed lock-timeout checks in both the common SQL and the lock-timeout error block.
- Risks:
  - Large performance views are intentionally summarized. For uncommon columns or patch-specific layouts, the GPT should still verify with `V$ALLCOLUMN`, `V$TABLE`, or the installed-version manual before generating final customer SQL.
  - Some Korean manual tables contain formatting noise, so exact column validation should prefer both the column table and the per-column headings when a source row appears malformed.

## Required Follow-Up

- None for R10. Proceed to the normal cycle validation and commit step for this re-review pass.
