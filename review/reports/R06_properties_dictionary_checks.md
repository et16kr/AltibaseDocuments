# R06 System Properties, Data Dictionary, and Check SQL

Date: 2026-05-14
Reviewer: Codex
Verdict: Review Required

## Scope

- Attachments:
  - `GPTs/attachments/05_data_types_properties.md`
  - `GPTs/attachments/06_data_dictionary_performance_views.md`
  - `GPTs/attachments/07_error_messages_troubleshooting.md`
- Supporting reports:
  - Not used directly; reviewed against the stage design, document selection, workplan, and attachment README.
- Source manuals sampled:
  - `Manuals/Altibase_7.1/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_7.1/eng/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_7.3/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_7.3/eng/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_7.3/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_trunk/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_trunk/eng/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_trunk/eng/Error Message Reference.md`
  - `Manuals/Altibase_trunk/kor/Error Message Reference.md`
  - `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`

## Commands Run

```bash
sed -n '1,240p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,220p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,260p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
nl -ba GPTs/attachments/05_data_types_properties.md | sed -n '1,2045p'
nl -ba GPTs/attachments/06_data_dictionary_performance_views.md | sed -n '1,1830p'
nl -ba GPTs/attachments/07_error_messages_troubleshooting.md | sed -n '1,1500p'
rg -n 'V\$TEMPORARY_LOBS|V\$MEM_STABLE|V\$LOCK_TABLE_STATS' Manuals/Altibase_trunk Manuals/Altibase_7.1 Manuals/Altibase_7.3 ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md
rg -n "PSM_CASE_SENSITIVE_MODE|REGEXP_MODE|LISTAGG_PRECISION|VARRAY_MEMORY_MAXIMUM" Manuals/Altibase_7.1 Manuals/Altibase_7.3 Manuals/Altibase_trunk
rg -n "ALTER SESSION SET QUERY_TIMEOUT|ALTER SESSION SET TIME_ZONE|QUERY_TIME_LIMIT|TIME_ZONE|SESSION_ID" GPTs/attachments/05_data_types_properties.md GPTs/attachments/06_data_dictionary_performance_views.md Manuals/Altibase_trunk/eng
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name README.md | sort | wc -l
rg -n '^### (Property Item|Type Item|Object Block|Error Block):|^## Searchable|^## Conversion TODO|trunk|file://|/home/emlee|C:' GPTs/attachments/05_data_types_properties.md GPTs/attachments/06_data_dictionary_performance_views.md GPTs/attachments/07_error_messages_troubleshooting.md
git status --short
```

## Findings

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| High | `GPTs/attachments/05_data_types_properties.md` | 39 | `PSM_CASE_SENSITIVE_MODE` is listed under 8.1 added or newly documented properties, but the 7.1 and 7.3 General Reference sources already document `PSM_CASE_SENSITIVE_MODE`. This can make the GPT incorrectly treat a valid 7.x property as 8.1-only. | Remove `PSM_CASE_SENSITIVE_MODE` from the 8.1-new property list, or explicitly label it as available in earlier baselines and only changed/verified in 8.1 if a source shows that distinction. |
| High | `GPTs/attachments/05_data_types_properties.md` | 1976 | `REGEXP_MODE` is labeled as an `8.1 verified source property`, but 7.1 English General Reference and 7.3 Korean General Reference document `REGEXP_MODE`, and 7.x error references use it for PCRE2 troubleshooting. | Reclassify `REGEXP_MODE` as a cross-version property where supported. Add a version note that 7.1/7.3 support should be checked against the installed source, rather than implying 8.1-only availability. |
| Medium | `GPTs/attachments/05_data_types_properties.md` | 1956 | `LISTAGG_PRECISION` and `VARRAY_MEMORY_MAXIMUM` are labeled as 8.1 verified-source properties, while 7.3 Korean General Reference documents both. This is a version-label source gap. | Run a focused version audit for these properties. If they are supported in 7.3, change the item labels from 8.1-only wording to version-scoped wording. |
| Medium | `GPTs/attachments/05_data_types_properties.md` | 974 | Individual check SQL for multi-value path properties such as `MEM_DB_DIR`, `LOG_DIR`, and `LOGANCHOR_DIR` selects only `VALUE1`, even though the source marks these as multiple-value properties and `V$PROPERTY` exposes `STOREDCOUNT` plus `VALUE1` through `VALUE8`. | In each affected property item block, use `SELECT name, storedcount, value1, value2, ..., value8 FROM V$PROPERTY ...` so GPT answers do not hide configured paths. |
| Medium | `GPTs/attachments/05_data_types_properties.md`; `GPTs/attachments/06_data_dictionary_performance_views.md` | 777 | Session-level examples run `ALTER SESSION SET QUERY_TIMEOUT` or `ALTER SESSION SET TIME_ZONE`, then verify only with `V$PROPERTY`. The data dictionary source exposes effective session values in `V$SESSION` columns such as `QUERY_TIME_LIMIT` and `TIME_ZONE`, and SQL Reference documents `SESSION_ID()`. | Keep `V$PROPERTY` for configured/default property checks, but add session-effect checks such as `SELECT query_time_limit, time_zone FROM V$SESSION WHERE id = SESSION_ID();` after `ALTER SESSION` examples. |

## Source Checks

- Claims checked:
  - `V$PROPERTY` columns `NAME`, `STOREDCOUNT`, `ATTR`, `MIN`, `MAX`, and `VALUE1` through `VALUE8` are documented in 7.1 and 8.1-source data dictionary manuals.
  - `V$TABLE` and `V$ALLCOLUMN` are documented and are plausible for performance-view and column availability checks.
  - `V$LOCK_TABLE_STATS` is documented in 7.1, 7.3, and 8.1-source data dictionary material.
  - `V$MEM_STABLE` is documented in the 8.1-source data dictionary material.
  - `V$TEMPORARY_LOBS` is supported by the 8.1 release notes and Korean 8.1-source General Reference 2, with columns `TYPE`, `ID`, `ALLOCED_SIZE`, and `OPEN_COUNT`.
  - Temporary LOB and JSON core claims were checked against 8.1 release notes and Korean 8.1-source General Reference 1.
  - Sample error blocks for `ERR-31363`, `0x2106D`, lock timeout, tablespace space, and communication failure preserve source error codes and symbols.
- Source coverage:
  - Dictionary and performance-view query columns sampled from `V$PROPERTY`, `V$TABLE`, `V$ALLCOLUMN`, `V$SESSION`, `V$STATEMENT`, `V$LOCK_*`, `V$SQL_PLAN_CACHE*`, `SYSTEM_.SYS_TABLES_`, `SYSTEM_.SYS_COLUMNS_`, `SYSTEM_.SYS_INDICES_`, `SYSTEM_.SYS_CONSTRAINTS_`, `SYSTEM_.SYS_REPLICATIONS_`, and `V$REPGAP`/`V$REPSENDER`/`V$REPRECEIVER` were generally plausible.
  - Error-message blocks are searchable and mostly preserve literal codes, symbols, property names, and view names.
- Source gaps:
  - 8.1 `V$TEMPORARY_LOBS` and some JSON/Temporary LOB details are not present in the sampled English 8.1-source General Reference files; they rely on release notes and Korean source material.
  - Property version labels near `REGEXP_MODE`, `LISTAGG_PRECISION`, and `VARRAY_MEMORY_MAXIMUM` need a focused version audit before upload.

## Oracle-Overlap Decision

- Correctly compressed:
  - The reviewed files avoid generic Oracle DML expansion and focus on Altibase properties, dictionary objects, views, errors, JSON, Temporary LOB, replication, and operational check SQL.
- Too much generic Oracle material:
  - None found in this stage.
- Missing Altibase-specific difference:
  - The main missing distinction is not Oracle overlap; it is Altibase version availability for several properties.

## Version Checks

- 7.1:
  - `PSM_CASE_SENSITIVE_MODE`, `REGEXP_MODE`, `V$PROPERTY`, `V$LOCK_TABLE_STATS`, and core dictionary views are source-backed.
  - The attachment should not imply that `PSM_CASE_SENSITIVE_MODE` or `REGEXP_MODE` are 8.1-only.
- 7.3:
  - `PSM_CASE_SENSITIVE_MODE` is documented in English General Reference 1. Korean 7.3 sources also document `REGEXP_MODE`, `LISTAGG_PRECISION`, and `VARRAY_MEMORY_MAXIMUM`.
  - 7.3 property availability should be explicitly audited where English source coverage is incomplete.
- 8.1:
  - JSON, Temporary LOB, `TEMPORARY_LOB_ENABLE`, `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`, `MEMORY_TEMPLOB_PIECE_SIZE`, `REPLICATION_SSL_PORT_NO`, `V$MEM_STABLE`, and `V$TEMPORARY_LOBS` are represented.
  - `V$TEMPORARY_LOBS` coverage depends on release notes and Korean General Reference 2, not the sampled English General Reference 2.

## Retrieval And GPT Answer Quality

- Strengths:
  - The target files have strong retrieval structure: `Questions This File Can Answer`, `Type Item`, `Property Item`, `Object Block`, and `Error Block` headings.
  - Literal system names, property names, view names, error codes, and SQL keywords are mostly preserved.
  - Temporary LOB and JSON blocks are searchable and tied to 8.1.
- Risks:
  - Wrong version labels can cause the GPT to deny or hide valid 7.1/7.3 property guidance.
  - Multi-value path properties may be under-reported if an answer retrieves only the individual property item block.
  - Session-level property examples need `V$SESSION` verification to avoid misleading operational checks.

## Required Follow-Up

- Correct `PSM_CASE_SENSITIVE_MODE` and `REGEXP_MODE` version labels in `05_data_types_properties.md`.
- Audit and, if needed, correct `LISTAGG_PRECISION` and `VARRAY_MEMORY_MAXIMUM` version labels.
- Update multi-value property item check SQL for `MEM_DB_DIR`, `LOG_DIR`, and `LOGANCHOR_DIR` to include `STOREDCOUNT` and all `VALUE` columns.
- Add `V$SESSION`/`SESSION_ID()` verification for `ALTER SESSION` examples involving `QUERY_TIMEOUT`, `TIME_ZONE`, and similar session properties.
