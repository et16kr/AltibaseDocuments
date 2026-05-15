# R06 DDL generation: LOB, JSON, and data type restrictions

Date: 2026-05-16
Reviewer: Codex
Verdict: Pass

## Scope

- Attachments:
  - `GPTs/attachments/03_sql_ddl_generation.md`
  - `GPTs/attachments/05_data_types_properties.md`
- Supporting reports:
  - `GPTs/reports/8_1_verification.md`
  - `GPTs/reports/eng_kor_parity.md`
- Source manuals sampled:
  - `Manuals/Altibase_7.1/kor/SQL Reference.md`
  - `Manuals/Altibase_7.1/kor/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_7.3/kor/SQL Reference.md`
  - `Manuals/Altibase_7.3/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_trunk/kor/SQL Reference.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`
  - `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`

## Commands Run

```bash
bash review/scripts/run_review_remediation_cycle.sh status
rg -n $'\t(Reviewing|Remediating|ReReviewing|Fail)$' review/review_remediation_cycle_status.tsv
git status --short
git diff -- GPTs/attachments/05_data_types_properties.md
git diff -- review/review_remediation_cycle_status.tsv review/review_stage_status.tsv
sed -n '1,260p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,260p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,300p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,240p' GPTs/attachments/README.md
rg -n "LOB|CLOB|BLOB|JSON|Temporary|temporary|TEMPORARY_LOB|MEMORY_TEMPLOB|V\$TEMPORARY_LOBS|data type|datatype|GEOMETRY|BYTE|CHAR|NCHAR|NVARCHAR|BOOLEAN|INTERVAL|TABLESPACE|IS JSON|CHECK|DEFAULT|partition|PRIMARY KEY|INDEX" GPTs/attachments/03_sql_ddl_generation.md
rg -n "LOB|CLOB|BLOB|JSON|Temporary|temporary|TEMPORARY_LOB|MEMORY_TEMPLOB|V\$TEMPORARY_LOBS|data type|datatype|GEOMETRY|BYTE|CHAR|NCHAR|NVARCHAR|BOOLEAN|INTERVAL|TABLESPACE|IS JSON|CHECK|DEFAULT|partition|PRIMARY KEY|INDEX|MAX" GPTs/attachments/05_data_types_properties.md
nl -ba GPTs/attachments/03_sql_ddl_generation.md | sed -n '300,390p'
nl -ba GPTs/attachments/03_sql_ddl_generation.md | sed -n '1220,1515p'
nl -ba GPTs/attachments/05_data_types_properties.md | sed -n '1,155p'
nl -ba GPTs/attachments/05_data_types_properties.md | sed -n '450,620p'
nl -ba GPTs/attachments/05_data_types_properties.md | sed -n '675,760p'
nl -ba GPTs/attachments/05_data_types_properties.md | sed -n '920,1265p'
rg -n "JSON|Temporary LOB|TEMPORARY_LOB|V\$TEMPORARY_LOBS|MEMORY_TEMPLOB|JSON_ARRAY|JSON_OBJECT|JSON_EXISTS|JSON_QUERY|JSON_VALUE|JSON_VALID|IS JSON|TRCLOG_JSON" Manuals/Altibase_7.1/kor/SQL\ Reference.md Manuals/Altibase_7.1/kor/General\ Reference-1.Data\ Types\ \&\ Altibase\ Properties.md Manuals/Altibase_7.3/kor/SQL\ Reference.md Manuals/Altibase_7.3/kor/General_Reference-1.Data\ Types\ \&\ Altibase\ Properties.md
rg -n "JSON|Temporary LOB|TEMPORARY_LOB|V\$TEMPORARY_LOBS|MEMORY_TEMPLOB|JSON_ARRAY|JSON_OBJECT|JSON_EXISTS|JSON_QUERY|JSON_VALUE|JSON_VALID|IS JSON|TRCLOG_JSON|SELECT FOR UPDATE|path expression" Manuals/Altibase_trunk/kor/SQL\ Reference.md Manuals/Altibase_trunk/kor/General_Reference-1.Data\ Types\ \&\ Altibase\ Properties.md Manuals/Altibase_trunk/kor/General_Reference-2.The\ Data\ Dictionary.md ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md
rg -n "BLOB|CLOB|IN ROW|VARIABLE|LOB|volatile|temporary|partition key|index|cursor" Manuals/Altibase_7.1/kor/General\ Reference-1.Data\ Types\ \&\ Altibase\ Properties.md Manuals/Altibase_7.3/kor/General_Reference-1.Data\ Types\ \&\ Altibase\ Properties.md Manuals/Altibase_trunk/kor/General_Reference-1.Data\ Types\ \&\ Altibase\ Properties.md
rg -n "JSON|Temporary LOB|TEMPORARY_LOB|V\$TEMPORARY_LOBS|MEMORY_TEMPLOB|TRCLOG_JSON|CLOB|BLOB|IN ROW|LOB_OBJECT_BUFFER_SIZE|DISK_LOB_COLUMN_IN_ROW_SIZE|MEMORY_LOB_COLUMN_IN_ROW_SIZE|Altibase 8.1 verified source" GPTs/reports/8_1_verification.md GPTs/reports/eng_kor_parity.md
rg -n 'Temporary LOB|TEMPORARY_LOB_ENABLE|MEMORY_TEMPLOB|V\$TEMPORARY_LOBS|native `JSON`|`JSON`|JSON columns are|JSON column|JSON processing|JSON workload' GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/05_data_types_properties.md
rg -n 'trunk|C:/|file://|Manuals/Altibase_trunk|local build|branch' GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/05_data_types_properties.md
rg -n 'BLOB \[VARIABLE|CLOB \[VARIABLE|BLOB.*VARIABLE|CLOB.*VARIABLE|Supported types: .*BLOB|Supported types: .*CLOB' GPTs/attachments/05_data_types_properties.md GPTs/attachments/03_sql_ddl_generation.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' | wc -l
```

## Findings

No actionable `Blocker`, `High`, `Medium`, or `Low` findings were found in this re-review.

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |

## Source Checks

- Claims checked:
  - LOB syntax, LOB storage placement, `IN ROW` behavior, explicit `VARIABLE` support, LOB cursor/volatile/disk-temporary/partition-key/index restrictions, `NOT NULL` caution, JSON syntax, JSON maximum size/depth/standards, JSON path-expression restrictions, Temporary LOB lifecycle, Temporary LOB creation cases, `ALTER SESSION SET FREE TEMPORARY LOB`, `TEMPORARY_LOB_ENABLE`, `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`, `MEMORY_TEMPLOB_PIECE_SIZE`, and `V$TEMPORARY_LOBS`.
- Source coverage:
  - Korean 7.1, 7.3, and 8.1 General References all support `BLOB [ IN ROW size ]` and `CLOB [ IN ROW size ]`; they describe LOB data as variable by storage behavior, but the explicit `VARIABLE` supported-type list excludes `BLOB` and `CLOB`.
  - Korean 7.1, 7.3, and 8.1 General References support `4GB - 1 byte` LOB size, separate disk LOB tablespace placement for disk tables, no separate memory LOB tablespace placement, cursor restriction, volatile/disk-temporary restriction, partition-key restriction, and index restriction.
  - Korean 8.1 General Reference and Korean 8.1 release notes support native `JSON`, `JSON [ IN ROW size ]`, maximum JSON size `2GB`, maximum depth `256`, RFC 8259 and ISO/IEC 19075-6:2021 references, Temporary LOB dependency, `TEMPORARY_LOB_ENABLE=1`, `SELECT FOR UPDATE` exclusion, JSON function families, and string-only path-expression operands.
  - Korean 8.1 General Reference, SQL Reference, Data Dictionary, and release notes support Temporary LOB lifecycle, transaction/session Temporary LOB categories, common creation cases, `ALTER SESSION SET FREE TEMPORARY LOB`, `TEMPORARY_LOB_ENABLE`, `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`, `MEMORY_TEMPLOB_PIECE_SIZE`, and `V$TEMPORARY_LOBS`.
  - Targeted searches over Korean 7.1 and 7.3 SQL Reference and General Reference 1 found no `JSON`, JSON function, `IS JSON`, Temporary LOB, `TEMPORARY_LOB_ENABLE`, `MEMORY_TEMPLOB_*`, or `V$TEMPORARY_LOBS` coverage, supporting the attachments' 8.1-only boundary.
- Korean/English source conflicts:
  - `GPTs/reports/8_1_verification.md` and `GPTs/reports/eng_kor_parity.md` document that English 8.1 manuals lack substantive JSON and Temporary LOB coverage while Korean 8.1 manuals contain it. This review used Korean manuals and Korean release notes as the technical basis.
- Source gaps:
  - No live Altibase server was available, so SQL was reviewed against manuals and release notes rather than executed.
  - Full JSON function option grammar was sampled only enough to verify the function family and path-expression restriction; deeper JSON DML behavior remains better covered in the DML/Oracle-compatibility stages.

## Oracle-Overlap Decision

- Correctly compressed:
  - The scoped attachments keep ordinary Oracle-overlapping data type and DDL content brief and focus on Altibase-specific storage target choices, LOB storage, JSON version gating, Temporary LOB properties, and verification views.
  - Oracle JSON and LOB conversion guidance is framed as non-portable to Altibase without version and storage checks.
- Too much generic Oracle material:
  - None found in the R06 scope.
- Missing Altibase-specific difference:
  - None found after the current remediation. The prior LOB syntax/modifier issue and missing LOB cursor restriction are resolved in `GPTs/attachments/05_data_types_properties.md`.

## Version Checks

- 7.1:
  - Native `JSON`, Temporary LOB, `TEMPORARY_LOB_ENABLE`, `MEMORY_TEMPLOB_*`, and `V$TEMPORARY_LOBS` are excluded from the 7.1 baseline in the scoped attachments.
  - LOB syntax now matches the Korean 7.1 General Reference: `BLOB [IN ROW size]` and `CLOB [IN ROW size]`, without explicit `VARIABLE`.
- 7.3:
  - Native `JSON`, Temporary LOB, `TEMPORARY_LOB_ENABLE`, `MEMORY_TEMPLOB_*`, and `V$TEMPORARY_LOBS` are excluded from the 7.3 baseline in the scoped attachments.
  - LOB syntax now matches the Korean 7.3 General Reference: `BLOB [IN ROW size]` and `CLOB [IN ROW size]`, without explicit `VARIABLE`.
- 8.1:
  - JSON and Temporary LOB guidance is tied to the customer-safe `Altibase 8.1 verified source` source family in the scoped attachments.
  - JSON guidance includes `JSON [IN ROW size]`, `2GB` maximum size, depth `256`, Temporary LOB dependency, `TEMPORARY_LOB_ENABLE=1`, `SELECT FOR UPDATE` exclusion, LOB-like restrictions, function-family names, and path-expression operand caution.
  - Temporary LOB guidance includes transaction/session lifecycle, common creation cases, `ALTER SESSION SET FREE TEMPORARY LOB`, `V$TEMPORARY_LOBS`, and related memory properties.

## Retrieval And GPT Answer Quality

- Strengths:
  - `03_sql_ddl_generation.md` gives retrievable DDL guidance for disk LOB tablespace placement, memory LOB placement, temporary table storage, 8.1 JSON columns, `TEMPORARY_LOB_ENABLE`, and `V$TEMPORARY_LOBS`.
  - `05_data_types_properties.md` has compact item blocks for LOB, Temporary LOB, JSON, and related properties, with clear version boundaries for 7.1, 7.3, and 8.1.
  - Searches found no unsupported `BLOB [VARIABLE ...]` / `CLOB [VARIABLE ...]` syntax and no customer-facing internal source labels in the scoped attachments.
- Risks:
  - `V$TEMPORARY_LOBS` appears in broad verification SQL lists as an as-applicable view. This is acceptable because the surrounding version sections explicitly restrict Temporary LOB and `V$TEMPORARY_LOBS` to Altibase 8.1 verified source, but generated answers should still state the target version before emitting the query.
  - JSON function examples are intentionally compact; uncommon JSON function options should still be verified against the target 8.1 SQL Reference.

## Required Follow-Up

- None for R06. The stage meets the acceptance condition: JSON and Temporary LOB guidance is tied to Altibase 8.1 verified source, and unsupported 7.1/7.3 leakage was not found in the scoped attachments.
