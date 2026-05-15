# R09 System Properties and Data Type Property Blocks

Date: 2026-05-16
Reviewer: Codex
Verdict: Pass

## Scope

- Attachments:
  - `GPTs/attachments/05_data_types_properties.md`
- Supporting reports:
  - `GPTs/reports/eng_kor_parity.md`
- Source manuals sampled:
  - `Manuals/Altibase_7.1/kor/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_7.3/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`
  - `ReleaseNotes/kor/Altibase_7_1_0_1_2_Release_Notes.md`
  - `ReleaseNotes/kor/Altibase_7_3_0_0_1_Release_Notes.md`
  - `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`

## Commands Run

```bash
bash review/scripts/run_review_remediation_cycle.sh status
rg -n $'\t(Reviewing|Remediating|ReReviewing|Fail)$' review/review_remediation_cycle_status.tsv
git status --short
git diff -- GPTs/attachments/05_data_types_properties.md
git diff -- GPTs/reports/eng_kor_parity.md
nl -ba GPTs/attachments/05_data_types_properties.md | sed -n '1,2066p'
rg -n "^### (Type|Property) Item:" GPTs/attachments/05_data_types_properties.md
rg -n -C 3 "JSON|Temporary LOB|TEMPORARY_LOB_ENABLE|MEMORY_TEMPLOB|REPLICATION_SSL_PORT_NO" Manuals/Altibase_trunk/kor/General_Reference-1.Data\ Types\ \&\ Altibase\ Properties.md ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md
rg -n -C 2 "MEMORY_VARIABLE_COLUMN_IN_ROW_SIZE|EXECUTE_STMT_MEMORY_MAXIMUM|PREPARE_STMT_MEMORY_MAXIMUM|ISOLATION_LEVEL|SSL_PORT_NO|PSM_CASE_SENSITIVE_MODE|LISTAGG_PRECISION|FLOAT" Manuals/Altibase_7.1/kor/General\ Reference-1.Data\ Types\ \&\ Altibase\ Properties.md Manuals/Altibase_7.3/kor/General_Reference-1.Data\ Types\ \&\ Altibase\ Properties.md Manuals/Altibase_trunk/kor/General_Reference-1.Data\ Types\ \&\ Altibase\ Properties.md GPTs/reports/eng_kor_parity.md
rg -n -C 2 "LOG_FILE_SIZE|CHECKPOINT_INTERVAL_IN_LOG|FAST_START_LOGFILE_TARGET|LOG_CREATE_METHOD|CHECKPOINT_SCALE_SINGLE_DW_BUFFER_SIZE|OPTIMIZER_FEATURE_ENABLE|INSPECTION_LARGE_HEAP_THRESHOLD|REPLICATION_SSL_PORT_NO|TRCLOG_EXPLAIN_TYPE|TRCLOG_JSON_PLAN_INDENT_DEPTH" Manuals/Altibase_trunk/kor/General_Reference-1.Data\ Types\ \&\ Altibase\ Properties.md ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md
rg -n "JSON|Temporary LOB|TEMPORARY_LOB|MEMORY_TEMPLOB|REPLICATION_SSL_PORT_NO|PSM_CASE_SENSITIVE_MODE|REGEXP_MODE|LISTAGG_PRECISION|EXECUTE_STMT_MEMORY_MAXIMUM|PREPARE_STMT_MEMORY_MAXIMUM|SSL_PORT_NO|LOG_FILE_SIZE" ReleaseNotes/kor/Altibase_7_1_0_1_2_Release_Notes.md ReleaseNotes/kor/Altibase_7_3_0_0_1_Release_Notes.md ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md
rg -n -A 1 "<td>(DB_NAME|DEFAULT_DISK_DB_DIR|MEM_DB_DIR|LOG_DIR|LOGANCHOR_DIR|LOG_FILE_SIZE|MEM_MAX_DB_SIZE|DISK_MAX_DB_SIZE|VOLATILE_MAX_DB_SIZE|DISK_LOB_COLUMN_IN_ROW_SIZE|MEMORY_LOB_COLUMN_IN_ROW_SIZE|MEMORY_VARIABLE_COLUMN_IN_ROW_SIZE|LOB_OBJECT_BUFFER_SIZE|TEMPORARY_LOB_ENABLE|MEMORY_TEMPLOB_MAX_ALLOC_SIZE|MEMORY_TEMPLOB_PIECE_SIZE|PCTFREE|PCTUSED|HASH_AREA_SIZE|SORT_AREA_SIZE|EXECUTE_STMT_MEMORY_MAXIMUM|PREPARE_STMT_MEMORY_MAXIMUM|SQL_PLAN_CACHE_SIZE|OPTIMIZER_FEATURE_ENABLE|CHECKPOINT_INTERVAL_IN_LOG|FAST_START_LOGFILE_TARGET|LOG_CREATE_METHOD|CHECKPOINT_SCALE_SINGLE_DW_BUFFER_SIZE|AUTO_COMMIT|ISOLATION_LEVEL|DEFAULT_DATE_FORMAT|TIME_ZONE|NLS_NUMERIC_CHARACTERS|QUERY_TIMEOUT|FETCH_TIMEOUT|IDLE_TIMEOUT|LOGIN_TIMEOUT|DDL_LOCK_TIMEOUT|DDL_TIMEOUT|UTRANS_TIMEOUT|PORT_NO|MAX_CLIENT|REPLICATION_PORT_NO|REPLICATION_SSL_PORT_NO|SSL_ENABLE|SSL_PORT_NO|SSL_CA|SSL_CERT|SSL_KEY|PSM_CASE_SENSITIVE_MODE|LISTAGG_PRECISION|REGEXP_MODE|VARRAY_MEMORY_MAXIMUM)</td>" Manuals/Altibase_trunk/kor/General_Reference-1.Data\ Types\ \&\ Altibase\ Properties.md
rg -n "V\$PROPERTY|VALUE1|STOREDCOUNT|ATTR" Manuals/Altibase_trunk/kor/General_Reference-2.The\ Data\ Dictionary.md
rg -n "V\$TEMPORARY_LOBS|ALLOCED_SIZE|OPEN_COUNT" Manuals/Altibase_trunk/kor/General_Reference-2.The\ Data\ Dictionary.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name README.md | wc -l
rg -n "trunk|file://|C:/|Manuals/|ReleaseNotes/|Altibase_trunk" GPTs/attachments/05_data_types_properties.md
git diff --check
bash review/scripts/run_review_stage.sh validate
```

## Findings

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Note | `GPTs/attachments/05_data_types_properties.md` | - | No actionable `Blocker`, `High`, `Medium`, or `Low` findings remain for this stage. The prior R09 property/default/range findings were re-checked against Korean 7.1, 7.3, and 8.1 sources and are remediated in the current worktree. | No R09 attachment remediation is required. Keep using installed-version `V$PROPERTY` checks for properties not represented in this compact attachment. |

## Source Checks

- Claims checked:
  - JSON type existence, size, standards, functions, path elements, path-expression restrictions, and `SELECT FOR UPDATE` restriction.
  - Temporary LOB lifecycle, cleanup SQL, `TEMPORARY_LOB_ENABLE`, `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`, and `MEMORY_TEMPLOB_PIECE_SIZE`.
  - Property change model, alter levels, defaults, ranges, and version-sensitive changes for the listed property blocks.
  - 7.3 and 8.1 release-note property additions and changed defaults.
  - `V$PROPERTY` and `V$TEMPORARY_LOBS` column names used by the check SQL.
- Source coverage:
  - Korean 8.1 General Reference supports the JSON and Temporary LOB blocks, including `V$TEMPORARY_LOBS` and `ALTER SESSION SET FREE TEMPORARY LOB`.
  - Korean 8.1 release notes support native JSON, Temporary LOB, `REPLICATION_SSL_PORT_NO`, JSON plan property names, and the 8.1 changed-property list.
  - Korean 7.3 release notes support `LISTAGG_PRECISION`, `REGEXP_MODE`, and the `EXECUTE_STMT_MEMORY_MAXIMUM` default change from `1073741824` to `2147483648`.
  - Korean 7.1/7.3/8.1 manuals support the remediated `MEMORY_VARIABLE_COLUMN_IN_ROW_SIZE`, `EXECUTE_STMT_MEMORY_MAXIMUM`, `PREPARE_STMT_MEMORY_MAXIMUM`, `ISOLATION_LEVEL`, `SSL_PORT_NO`, `PSM_CASE_SENSITIVE_MODE`, `LISTAGG_PRECISION`, and `FLOAT` blocks.
  - Korean 8.1 data dictionary supports `V$PROPERTY.NAME`, `STOREDCOUNT`, `ATTR`, `MIN`, `MAX`, `VALUE1` through `VALUE8`, and `V$TEMPORARY_LOBS.TYPE`, `ID`, `ALLOCED_SIZE`, and `OPEN_COUNT`.
- Korean/English source conflicts:
  - `FLOAT` range conflicts: Korean says `-1E-120` to `1E+120`; English says `-1E+120` to `1E+120`. The attachment now follows the Korean-source decision recorded in `GPTs/reports/eng_kor_parity.md`.
  - 8.1 release notes list `PSM_CASE_SENSITIVE_MODE` as new, but Korean 7.1 and 7.3 manuals also document it. The attachment keeps the documented 7.1/7.3/8.1 availability and version-split defaults.
- Source gaps:
  - `TRCLOG_EXPLAIN_TYPE` and `TRCLOG_JSON_PLAN_INDENT_DEPTH` appear only as release-note property names in sampled sources; the attachment appropriately avoids inventing defaults or ranges.

## Oracle-Overlap Decision

- Correctly compressed:
  - Ordinary Oracle-overlapping data type mapping is brief and focused on Altibase limits, storage modifiers, LOB behavior, JSON version scope, and property checks.
- Too much generic Oracle material:
  - None found in this attachment.
- Missing Altibase-specific difference:
  - None found for this stage.

## Version Checks

- 7.1:
  - Remediated defaults and ranges were re-checked for `EXECUTE_STMT_MEMORY_MAXIMUM`, `PREPARE_STMT_MEMORY_MAXIMUM`, `PSM_CASE_SENSITIVE_MODE`, `LISTAGG_PRECISION`, `REGEXP_MODE`, and core data types.
  - Native `JSON` and Temporary LOB remain excluded from the 7.1 baseline.
- 7.3:
  - Remediated defaults and ranges were re-checked for `EXECUTE_STMT_MEMORY_MAXIMUM`, `PREPARE_STMT_MEMORY_MAXIMUM`, `PSM_CASE_SENSITIVE_MODE`, `LISTAGG_PRECISION`, `REGEXP_MODE`, and `SSL_PORT_NO`.
  - Native `JSON` and Temporary LOB remain excluded from the 7.3 baseline.
- 8.1:
  - JSON and Temporary LOB coverage is source-backed.
  - New and changed property coverage is source-backed for `TEMPORARY_LOB_ENABLE`, `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`, `MEMORY_TEMPLOB_PIECE_SIZE`, `REPLICATION_SSL_PORT_NO`, `CHECKPOINT_SCALE_SINGLE_DW_BUFFER_SIZE`, `CHECKPOINT_INTERVAL_IN_LOG`, `FAST_START_LOGFILE_TARGET`, `LOG_CREATE_METHOD`, `LOG_FILE_SIZE`, and `OPTIMIZER_FEATURE_ENABLE`.
  - The release-note-only JSON plan properties are intentionally guarded with "verify on installed server" language.

## Retrieval And GPT Answer Quality

- Strengths:
  - The attachment has strong retrieval headings and compact item blocks.
  - Literal property names, SQL object names, data type names, and `Altibase 8.1 verified source` wording are preserved.
  - JSON and Temporary LOB blocks are concise and aligned with Korean 8.1 manual structure.
  - High-risk property blocks now carry version-split defaults/ranges where Korean sources differ.
- Risks:
  - This attachment is intentionally compact. If a customer asks for an unlisted property or patch-specific behavior, the GPT should verify with the installed version and `V$PROPERTY` rather than extrapolating from adjacent properties.
  - `TRCLOG_EXPLAIN_TYPE` and `TRCLOG_JSON_PLAN_INDENT_DEPTH` are source-limited to release-note names in this stage's sampled sources, so the attachment correctly avoids detailed values.

## Required Follow-Up

- None for R09. Proceed to the next review stage after the normal cycle runner commits this pass state.
