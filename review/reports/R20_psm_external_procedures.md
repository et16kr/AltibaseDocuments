# R20 PSM, Stored Procedures, and External Procedures

Date: 2026-05-16
Reviewer: Codex
Verdict: Pass

## Scope

- Attachments:
  - `GPTs/attachments/10_psm_stored_external_procedures.md`
  - `GPTs/attachments/04_sql_dml_oracle_compatibility.md`
- Supporting reports:
  - `GPTs/reports/source_inventory.md`
  - `GPTs/reports/eng_kor_parity.md`
  - `GPTs/reports/8_1_verification.md`
- Source manuals sampled:
  - `Manuals/Altibase_7.1/kor/Stored Procedures Manual.md`
  - `Manuals/Altibase_7.3/kor/Stored Procedures Manual.md`
  - `Manuals/Altibase_trunk/kor/Stored Procedures Manual.md`
  - `Manuals/Altibase_7.1/kor/External Procedures Manual.md`
  - `Manuals/Altibase_7.3/kor/External Procedures Manual.md`
  - `Manuals/Altibase_trunk/kor/External Procedures Manual.md`
  - `Manuals/Altibase_7.1/kor/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_7.3/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `ReleaseNotes/kor/Altibase_7_3_0_0_1_Release_Notes.md`
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
git diff -- GPTs/attachments/10_psm_stored_external_procedures.md GPTs/reports/source_inventory.md review/review_remediation_cycle_status.tsv review/review_stage_status.tsv review/reports/R20_psm_external_procedures.md
wc -l GPTs/attachments/10_psm_stored_external_procedures.md GPTs/attachments/04_sql_dml_oracle_compatibility.md
nl -ba GPTs/attachments/10_psm_stored_external_procedures.md | sed -n '1,220p'
nl -ba GPTs/attachments/10_psm_stored_external_procedures.md | sed -n '221,520p'
nl -ba GPTs/attachments/10_psm_stored_external_procedures.md | sed -n '521,980p'
nl -ba GPTs/attachments/10_psm_stored_external_procedures.md | sed -n '981,1070p'
nl -ba GPTs/attachments/04_sql_dml_oracle_compatibility.md | sed -n '1,260p'
nl -ba GPTs/attachments/04_sql_dml_oracle_compatibility.md | sed -n '261,620p'
nl -ba GPTs/attachments/04_sql_dml_oracle_compatibility.md | sed -n '621,1125p'
rg -n "trunk|file://|/home/|C:/|TODO|Conversion TODO|IF EXISTS|IF NOT EXISTS|BODY IF EXISTS|IF EXISTS BODY|BYTE|VARBYTE|PSM_CASE_SENSITIVE_MODE|VARRAY_MEMORY_MAXIMUM|TEMPORARY_LOB|V\\$TEMPORARY_LOBS|V\\$EXTPROC_AGENT|V\\$LIBRARY|V\\$PROCINFO|SYS_LIBRARIES_" GPTs/attachments/10_psm_stored_external_procedures.md GPTs/attachments/04_sql_dml_oracle_compatibility.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' | sort | wc -l
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' | sort
rg -n "PSM_CASE_SENSITIVE_MODE|VARRAY_MEMORY_MAXIMUM|VARRAY|IF NOT EXISTS|IF EXISTS|DROP PACKAGE|CREATE PACKAGE|Anonymous|익명|COMMIT|ROLLBACK|커서|cursor|NOCOPY|AUTHID|DETERMINISTIC|RAISE_APPLICATION_ERROR|SQLCODE|SQLERRM|REF CURSOR|TYPESET|EXECUTE IMMEDIATE" "Manuals/Altibase_7.1/kor/Stored Procedures Manual.md" "Manuals/Altibase_7.3/kor/Stored Procedures Manual.md" "Manuals/Altibase_trunk/kor/Stored Procedures Manual.md" "ReleaseNotes/kor/Altibase_7_3_0_0_1_Release_Notes.md" "ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md"
rg -n "V\\$LIBRARY|V\\$PROCINFO|SYS_LIBRARIES_|V\\$EXTPROC_AGENT|EXTPROC_AGENT|LANGUAGE|EXTERNAL|INTERNAL|entryfunction|SQL_TIMESTAMP_STRUCT|ALTIBASE_EXTPROC_IND|CREATE LIBRARY|DROP LIBRARY|ALTER LIBRARY|BYTE|VARBYTE|PARAMETERS|INDICATOR|MAXLEN|LENGTH" "Manuals/Altibase_7.1/kor/External Procedures Manual.md" "Manuals/Altibase_7.3/kor/External Procedures Manual.md" "Manuals/Altibase_trunk/kor/External Procedures Manual.md"
rg -n "Temporary LOB|임시 LOB|TEMPORARY_LOB|TEMPLOB|TO_CLOB|TO_BLOB|V\\$TEMPORARY_LOBS|FREE TEMPORARY LOB|MEMORY_TEMPLOB|LOB_OBJECT_BUFFER_SIZE" "Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md" "Manuals/Altibase_trunk/kor/Stored Procedures Manual.md" "ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md"
rg -n "PSM_CHAR_DEFAULT_PRECISION|PSM_VARCHAR_DEFAULT_PRECISION|LOB_OBJECT_BUFFER_SIZE|PSM_CASE_SENSITIVE_MODE|VARRAY_MEMORY_MAXIMUM" "Manuals/Altibase_7.1/kor/General Reference-1.Data Types & Altibase Properties.md" "Manuals/Altibase_7.3/kor/General_Reference-1.Data Types & Altibase Properties.md" "Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md"
rg -n "RETURNING|RETURN|AUTOCOMMIT|COMMIT|ROLLBACK|Temporary LOB|JSON|PSM|procedure|function|host variables|BULK COLLECT" GPTs/attachments/04_sql_dml_oracle_compatibility.md
find Manuals -path '*media/StoredProcedure*' -type f \( -name 'drop_package.*' -o -name 'create_package.*' -o -name 'create_package_body.*' -o -name 'create_procedure.*' -o -name 'create_function.*' -o -name 'callSpec.*' -o -name 'create_library.*' -o -name 'drop_library.*' \) -printf '%p\n' | sort
file Manuals/Altibase_trunk/kor/media/StoredProcedure/drop_package.png Manuals/Altibase_7.3/kor/media/StoredProcedure/drop_package.gif Manuals/Altibase_7.1/kor/media/StoredProcedure/drop_package.gif Manuals/Altibase_trunk/kor/media/ExternalProcedure/create_library.png
sed -n '340,365p' "Manuals/Altibase_7.1/kor/External Procedures Manual.md"
sed -n '398,422p' "Manuals/Altibase_7.3/kor/External Procedures Manual.md"
sed -n '397,421p' "Manuals/Altibase_trunk/kor/External Procedures Manual.md"
sed -n '8568,8582p' "Manuals/Altibase_7.3/kor/Stored Procedures Manual.md"
sed -n '15820,15842p' "Manuals/Altibase_7.3/kor/General_Reference-1.Data Types & Altibase Properties.md"
sed -n '16130,16149p' "Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md"
sed -n '15317,15336p' "Manuals/Altibase_7.1/kor/General Reference-1.Data Types & Altibase Properties.md"
sed -n '80,91p' ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md
sed -n '2617,2640p' "Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md"
```

The Korean source syntax diagrams for 8.1-source `drop_package.png` and 7.3 `drop_package.gif` were also visually inspected.

## Findings

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Note | `GPTs/attachments/10_psm_stored_external_procedures.md` | - | No actionable `Blocker`, `High`, `Medium`, or `Low` findings remain in the current R20 scope. The prior package `DROP PACKAGE BODY IF EXISTS` ordering issue and external `BYTE` / `VARBYTE` mapping gap are remediated. | No R20 remediation required. Preserve the current version-scoped wording for `IF EXISTS` / `IF NOT EXISTS`, external procedure mode, PSM case sensitivity, VARRAY, and Temporary LOB guidance. |

## Source Checks

- Claims checked:
  - Stored procedure, function, anonymous block, package, package body, typeset, cursor, dynamic SQL, exception, pragma, and transaction-control guidance.
  - Version-scoped `IF NOT EXISTS` and `IF EXISTS` support for PSM objects in the 8.1 verified source, including the corrected `DROP PACKAGE [BODY] [IF EXISTS] [user_name.]package_name` order.
  - External procedure setup, `CREATE LIBRARY`, `DROP LIBRARY`, `LANGUAGE [EXTERNAL | INTERNAL] C`, default external mode, `entryfunction`, `PARAMETERS`, `INDICATOR`, `LENGTH`, `MAXLEN`, and agent troubleshooting properties/views.
  - Korean-source external procedure data type mapping, including `BYTE` and `VARBYTE` in the same `char *` mapping family as character/binary buffer types.
  - `PSM_CASE_SENSITIVE_MODE` defaults: `0` in 7.1 and `1` in 7.3 and 8.1 verified source.
  - VARRAY support from 7.3 release notes and 7.3/8.1-source manuals, including `VARRAY_MEMORY_MAXIMUM`.
  - 8.1 Temporary LOB behavior from Korean release notes and General Reference, including transaction/session Temporary LOB cases, `V$TEMPORARY_LOBS`, `TEMPORARY_LOB_ENABLE`, `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`, `MEMORY_TEMPLOB_PIECE_SIZE`, and `ALTER SESSION SET FREE TEMPORARY LOB`.
  - R20-relevant DML overlap in `04_sql_dml_oracle_compatibility.md`, especially transaction syntax, DML `RETURN`/`RETURNING`, PSM host-variable mentions, JSON/Temporary LOB boundaries, and Oracle feature-parity cautions.
- Source coverage:
  - The current `10_psm_stored_external_procedures.md` content is source-grounded for the sampled high-risk PSM and external procedure areas.
  - `04_sql_dml_oracle_compatibility.md` remains appropriately compressed for R20 and does not conflict with PSM/external-procedure guidance.
  - The scoped attachment set still has exactly 20 upload Markdown files excluding `README.md`.
- Korean/English source conflicts:
  - The Korean External Procedures manuals include `BYTE` and `VARBYTE` in the data type mapping where English-source extraction can appear incomplete; the attachment now follows the Korean source.
  - The current attachment follows Korean-source behavior for cursor `COMMIT`/`ROLLBACK` guidance instead of older English drift.
- Source gaps:
  - No live Altibase compile/execution test was performed.
  - External C/C++ examples were not compiled, loaded into `$ALTIBASE_HOME/lib`, or executed through an Altibase server.
  - Syntax diagrams were sampled for the high-risk package/library areas, not exhaustively re-rendered for every PSM grammar image.

## Oracle-Overlap Decision

- Correctly compressed:
  - `04_sql_dml_oracle_compatibility.md` keeps ordinary Oracle-overlapping DML brief and focuses on Altibase row limiting, DML `RETURN`/`RETURNING`, transaction behavior, JSON version boundaries, hints, and function differences.
  - `10_psm_stored_external_procedures.md` frames Altibase PSM as PL/SQL-like but not fully Oracle PL/SQL compatible.
- Too much generic Oracle material:
  - None found in the scoped files.
- Missing Altibase-specific difference:
  - None requiring remediation in this R20 pass. The attachment now calls out Altibase-specific `?` dynamic SQL bind markers, `RAISE_APPLICATION_ERROR` code range, SQL-callable function restrictions, package availability limits, collection conversion choices, `PSM_CASE_SENSITIVE_MODE`, native external procedure requirements, and 8.1 Temporary LOB behavior.

## Version Checks

- 7.1:
  - PSM syntax, non-VARRAY baseline, external procedure `LANGUAGE [EXTERNAL | INTERNAL] C` mode behavior, external data type mapping, `PSM_CASE_SENSITIVE_MODE` default `0`, and cursor transaction-control guidance are source-aligned in the sampled areas.
  - Attachment guidance correctly avoids broad 7.1 generation of PSM `IF EXISTS` / `IF NOT EXISTS`.
- 7.3:
  - VARRAY and `VARRAY_MEMORY_MAXIMUM` are included; `PSM_CASE_SENSITIVE_MODE` default `1` is explicit; external procedure mode and mapping are source-aligned in the sampled areas.
  - Attachment guidance correctly avoids broad 7.3 generation of PSM `IF EXISTS` / `IF NOT EXISTS`.
- 8.1:
  - 8.1 verified-source guidance covers PSM idempotent DDL, corrected package drop syntax order, VARRAY, Temporary LOB, external library DDL, external procedure mode, and relevant troubleshooting views/properties.

## Retrieval And GPT Answer Quality

- Strengths:
  - The PSM attachment has strong question-oriented headings, syntax blocks, generation notes, minimal examples, Oracle compatibility warnings, external procedure flow, and troubleshooting cues.
  - Literal tokens are preserved, including `RAISE_APPLICATION_ERROR`, `EXECUTE IMMEDIATE`, `REF CURSOR`, `TYPESET`, `PSM_CASE_SENSITIVE_MODE`, `entryfunction`, `TEMPORARY_LOB_ENABLE`, `V$TEMPORARY_LOBS`, `V$EXTPROC_AGENT`, and `SYS_LIBRARIES_`.
  - The corrected package and external type mapping content appears in the main retrieval paths for SQL generation and external procedure parameter mapping.
- Risks:
  - External procedure advice remains inherently operationally risky because native code behavior was not compiled or exercised in a live Altibase environment.
  - Some compact grammar blocks include 8.1-only optional clauses; the surrounding version table and core guidance mitigate this, but answer generation should continue to check the requested target version before emitting `IF EXISTS` or `IF NOT EXISTS`.

## Required Follow-Up

- No R20 remediation is required for `GPTs/attachments/10_psm_stored_external_procedures.md`.
- No R20 remediation is required for `GPTs/attachments/04_sql_dml_oracle_compatibility.md`.
- Continue to the next review stage only after the cycle runner's normal validation/commit step for the current R20 worktree state.
