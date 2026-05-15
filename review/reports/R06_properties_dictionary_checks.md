# R06 System Properties, Data Dictionary, and Check SQL Review

Date: 2026-05-14
Reviewer: Codex
Verdict: Review Required

## Scope

- Attachments:
  - `GPTs/attachments/05_data_types_properties.md`
  - `GPTs/attachments/06_data_dictionary_performance_views.md`
  - `GPTs/attachments/07_error_messages_troubleshooting.md`
- Supporting reports:
  - `review/Altibase_GPT_Detailed_Review_Design.md`
  - `GPTs/Altibase_GPT_Document_Selection.md`
  - `GPTs/Altibase_GPT_Attachment_Build_Workplan.md`
  - `GPTs/attachments/README.md`
- Source manuals sampled:
  - `Manuals/Altibase_7.1/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_7.1/eng/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_7.1/eng/Error Message Reference.md`
  - `Manuals/Altibase_7.3/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_7.3/eng/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_7.3/eng/Error Message Reference.md`
  - `Manuals/Altibase_trunk/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_trunk/eng/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_trunk/eng/Error Message Reference.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`

## Commands Run

```bash
sed -n '1,240p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,220p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,260p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
nl -ba GPTs/attachments/05_data_types_properties.md | sed -n '1,2068p'
nl -ba GPTs/attachments/06_data_dictionary_performance_views.md | sed -n '1,1824p'
nl -ba GPTs/attachments/07_error_messages_troubleshooting.md | sed -n '1,1534p'
rg -n "V\$TEMPORARY_LOBS|V\$MEM_STABLE|V\$LOCK_TABLE_STATS|TEMPORARY_LOB_ENABLE|MEMORY_TEMPLOB|REPLICATION_SSL_PORT_NO|JSON \[|ALTER SESSION SET FREE TEMPORARY LOB" GPTs/attachments/05_data_types_properties.md GPTs/attachments/06_data_dictionary_performance_views.md GPTs/attachments/07_error_messages_troubleshooting.md
rg -n "V\$LOCK_TABLE_STATS|MEM_STABLE|TEMPORARY_LOBS" Manuals/Altibase_7.1/eng/General\ Reference-2.The\ Data\ Dictionary.md Manuals/Altibase_7.3/eng/General\ Reference-2.The\ Data\ Dictionary.md Manuals/Altibase_trunk/eng/General\ Reference-2.The\ Data\ Dictionary.md Manuals/Altibase_trunk/kor/General_Reference-2.The\ Data\ Dictionary.md
rg -n "TEMPORARY_LOB_ENABLE|MEMORY_TEMPLOB_MAX_ALLOC_SIZE|MEMORY_TEMPLOB_PIECE_SIZE|REPLICATION_SSL_PORT_NO|CHECKPOINT_SCALE_SINGLE_DW_BUFFER_SIZE|TRCLOG_EXPLAIN_TYPE|TRCLOG_JSON_PLAN_INDENT_DEPTH" ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md Manuals/Altibase_trunk/kor/General_Reference-1.Data\ Types\ \&\ Altibase\ Properties.md
rg -n "314B4|5112C|91101|LOB_AUTOCOMMIT" Manuals/Altibase_7.1/eng/Error\ Message\ Reference.md Manuals/Altibase_7.3/eng/Error\ Message\ Reference.md Manuals/Altibase_trunk/eng/Error\ Message\ Reference.md
rg -n "trunk|Altibase_trunk|file://|/home/|C:\\|Manuals/|ReleaseNotes/" GPTs/attachments/05_data_types_properties.md GPTs/attachments/06_data_dictionary_performance_views.md GPTs/attachments/07_error_messages_troubleshooting.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name README.md | sort | wc -l
```

## Findings

No Blocker or High issues were found.

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Medium | `GPTs/attachments/07_error_messages_troubleshooting.md` | 1114 | The LOB autocommit version caution says LOB autocommit errors appear in 7.3 and 8.1 sources. Source sampling found `0x5112C` / `ulERR_ABORT_LOB_AUTOCOMMIT_MODE_ERR` and `0x91101` / `utERR_ABORT_LOB_AUTOCOMMIT_MODE_ERR` in the 7.1 Error Message Reference too; only the SQL-level `0x314B4` / `qpERR_ABORT_QMX_LOB_AUTOCOMMIT_MODE` was not found in 7.1 English source. This could cause a 7.1 customer answer to understate applicable client or utility LOB autocommit diagnostics. | Split the version caution by code: state that `0x5112C` and `0x91101` are present in sampled 7.1, 7.3, and 8.1 sources, while `0x314B4` should be treated as 7.3/8.1 unless confirmed in a target 7.1 build. |
| Low | `GPTs/attachments/05_data_types_properties.md` | 1989 | The property blocks for `LISTAGG_PRECISION` and `VARRAY_MEMORY_MAXIMUM` use process wording: "sampled 7.3 Korean source". The names and cautions are searchable, but this wording is not ideal for customer-facing GPT knowledge and slightly exposes the review/build method. | Reword to customer-safe source labels, for example "documented in Altibase 7.3 supplemental source and Altibase 8.1 verified source; verify exact availability in the installed build." Apply the same cleanup to the matching `VARRAY_MEMORY_MAXIMUM` line and the broader "sampled 7.x" wording near the version notes. |

## Source Checks

- Claims checked:
  - Data type syntax for character, binary, LOB, 8.1 `JSON`, and `IN ROW`.
  - Temporary LOB lifecycle, `ALTER SESSION SET FREE TEMPORARY LOB`, `V$TEMPORARY_LOBS` columns `TYPE`, `ID`, `ALLOCED_SIZE`, and `OPEN_COUNT`.
  - Property names and selected defaults/ranges for `LOG_FILE_SIZE`, `TEMPORARY_LOB_ENABLE`, `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`, `MEMORY_TEMPLOB_PIECE_SIZE`, `REPLICATION_SSL_PORT_NO`, `CHECKPOINT_SCALE_SINGLE_DW_BUFFER_SIZE`, `TRCLOG_EXPLAIN_TYPE`, and `TRCLOG_JSON_PLAN_INDENT_DEPTH`.
  - Data dictionary and performance view names/columns for `V$PROPERTY`, `V$TABLE`, `V$ALLCOLUMN`, `V$TIME_ZONE_NAMES`, `V$SQL_PLAN_CACHE`, `V$MEM_STABLE`, `V$LOCK_TABLE_STATS`, `V$TEMPORARY_LOBS`, `SYSTEM_.SYS_TABLES_`, and `SYSTEM_.SYS_COLUMNS_`.
  - Representative check SQL for properties, object metadata, sessions/statements, locks, tablespaces, replication, plan cache, and Temporary LOB.
- Source coverage:
  - 7.1 and 7.3 English General Reference sources support the common dictionary/property structures sampled.
  - 8.1 release notes support the new-property and new-performance-view lists.
  - 8.1 Korean General Reference fills the current English-source gap for `JSON`, Temporary LOB details, `V$TEMPORARY_LOBS`, and Temporary LOB properties.
- Source gaps:
  - SQL was not executed against a live Altibase instance; plausibility was checked against manual object/column definitions.
  - `TRCLOG_EXPLAIN_TYPE` and `TRCLOG_JSON_PLAN_INDENT_DEPTH` remain release-note-only in the sampled source, and the attachment correctly tells users to verify values with `V$PROPERTY`.

## Oracle-Overlap Decision

- Correctly compressed:
  - Ordinary Oracle-overlapping DML is not expanded in these files.
  - Oracle compatibility appears only where it affects data type selection and migration cautions, such as `VARCHAR2` to `VARCHAR`, Oracle `NUMBER`, `RAW`, LOB, and JSON design.
- Too much generic Oracle material:
  - None found in this stage.
- Missing Altibase-specific difference:
  - No major gap found. The attachments preserve Altibase-specific system properties, meta tables, performance views, Temporary LOB, JSON, replication port, and check SQL patterns.

## Version Checks

- 7.1:
  - Core data type, property, dictionary, and performance-view names sampled from 7.1 sources are mostly preserved.
  - The LOB autocommit troubleshooting block should be adjusted because 7.1 includes the client/utility LOB autocommit error codes.
- 7.3:
  - Common property and dictionary structures match sampled 7.3 source. `V$LOCK_TABLE_STATS` is present in sampled 7.3 General Reference 2.
  - Some property availability notes are intentionally cautious but should avoid "sampled Korean source" wording in customer-facing text.
- 8.1:
  - New 8.1 properties and performance views are represented with customer-safe `Altibase 8.1 verified source` labeling.
  - `V$MEM_STABLE`, `V$TEMPORARY_LOBS`, `JSON`, and Temporary LOB checks are version-scoped and generally plausible.

## Retrieval And GPT Answer Quality

- Strengths:
  - The attachments use searchable `Type Item`, `Property Item`, `Object Block`, and `Error Block` headings.
  - Literal property names, view names, error codes, SQL keywords, and check SQL identifiers are preserved.
  - The `V$TABLE` and `V$ALLCOLUMN` availability-check pattern is useful for version-sensitive view/column answers.
- Risks:
  - A GPT may repeat the LOB autocommit version caution too narrowly for Altibase 7.1 unless the block is corrected.
  - "sampled ... Korean source" wording can leak build/review provenance into customer answers and should be converted to product/version source labels.

## Required Follow-Up

- Update the `07_error_messages_troubleshooting.md` LOB autocommit version caution to distinguish 7.1 client/utility codes from the later SQL-level code.
- Clean the two `05_data_types_properties.md` property availability notes that mention "sampled 7.3 Korean source" and the broader "sampled 7.x" wording.
- No attachment changes were made during this review stage.
