# R07 DML, Expressions, Functions, and Oracle-Overlap Compression

Date: 2026-05-16
Reviewer: Codex
Verdict: Pass

## Scope

- Attachments:
  - `GPTs/attachments/04_sql_dml_oracle_compatibility.md`
  - `GPTs/attachments/03_sql_ddl_generation.md`
- Supporting reports:
  - `GPTs/reports/eng_kor_parity.md`
  - `GPTs/reports/8_1_verification.md`
  - `GPTs/reports/source_inventory.md`
- Source manuals sampled:
  - `Manuals/Altibase_7.1/kor/SQL Reference.md`
  - `Manuals/Altibase_7.3/kor/SQL Reference.md`
  - `Manuals/Altibase_trunk/kor/SQL Reference.md`
  - `Manuals/Altibase_7.1/kor/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_7.3/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`

## Commands Run

```bash
bash review/scripts/run_review_remediation_cycle.sh status
rg -n $'\t(Reviewing|Remediating|ReReviewing|Fail)$' review/review_remediation_cycle_status.tsv
git status --short
sed -n '1,240p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,240p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,240p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
sed -n '1,260p' review/reports/R07_dml_functions_oracle_overlap.md
git diff -- GPTs/attachments/04_sql_dml_oracle_compatibility.md
git diff -- GPTs/reports/source_inventory.md
git diff -- review/review_remediation_cycle_status.tsv
git diff -- review/review_stage_status.tsv
wc -l GPTs/attachments/04_sql_dml_oracle_compatibility.md GPTs/attachments/03_sql_ddl_generation.md
rg -n '^#{1,4} ' GPTs/attachments/04_sql_dml_oracle_compatibility.md
rg -n '^#{1,4} ' GPTs/attachments/03_sql_ddl_generation.md
rg -n 'Oracle|SELECT|INSERT|UPDATE|DELETE|MERGE|RETURNING|RETURN |JSON|REGEXP|NVL|DECODE|ROWNUM|TOP|LIMIT|LATERAL|APPLY|PIVOT|UNPIVOT|WITH|FOR UPDATE|APPEND|Direct|DIRECT' GPTs/attachments/04_sql_dml_oracle_compatibility.md
rg -n 'SELECT|INSERT|UPDATE|DELETE|MERGE|DML|Oracle|JSON|REGEXP|NVL|DECODE|ROWNUM|TOP|LIMIT|LATERAL|APPLY|PIVOT|UNPIVOT|WITH|FOR UPDATE|APPEND' GPTs/attachments/03_sql_ddl_generation.md
nl -ba GPTs/attachments/04_sql_dml_oracle_compatibility.md | sed -n '1,260p'
nl -ba GPTs/attachments/04_sql_dml_oracle_compatibility.md | sed -n '260,620p'
nl -ba GPTs/attachments/04_sql_dml_oracle_compatibility.md | sed -n '620,1125p'
nl -ba GPTs/attachments/03_sql_ddl_generation.md | sed -n '1960,2015p'
rg -n 'JSON_ARRAY|JSON_OBJECT|JSON_EXISTS|JSON_QUERY|JSON_VALUE|JSON_VALID|IS JSON|TEMPORARY_LOB_ENABLE|SELECT FOR UPDATE|json_path|JSON path|패스|경로' Manuals/Altibase_trunk/kor/SQL\ Reference.md Manuals/Altibase_trunk/kor/General_Reference-1.Data\ Types\ \&\ Altibase\ Properties.md ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md
rg -n 'REGEXP_MODE|PCRE2|REGEXP_LIKE|7\.1\.0\.7\.7|US7ASCII|UTF-8' Manuals/Altibase_7.1/kor/SQL\ Reference.md Manuals/Altibase_7.1/kor/General\ Reference-1.Data\ Types\ \&\ Altibase\ Properties.md Manuals/Altibase_7.3/kor/SQL\ Reference.md Manuals/Altibase_7.3/kor/General_Reference-1.Data\ Types\ \&\ Altibase\ Properties.md Manuals/Altibase_trunk/kor/SQL\ Reference.md Manuals/Altibase_trunk/kor/General_Reference-1.Data\ Types\ \&\ Altibase\ Properties.md
rg -n 'RETURNING|RETURN |MERGE|WHEN NO ROWS|LATERAL|APPLY|PIVOT|UNPIVOT|WITH|RECURSION_LEVEL_MAXIMUM|FOR UPDATE|LIMIT|TOP|ROWNUM|APPEND|다이렉트|Direct' Manuals/Altibase_7.1/kor/SQL\ Reference.md Manuals/Altibase_7.3/kor/SQL\ Reference.md Manuals/Altibase_trunk/kor/SQL\ Reference.md
rg -n 'JSON|Temporary LOB|TEMPORARY_LOB|IS JSON|JSON_VALUE|JSON_QUERY|JSON_EXISTS|Korean|English|영문|한글' GPTs/reports/eng_kor_parity.md GPTs/reports/8_1_verification.md GPTs/reports/source_inventory.md GPTs/attachments/05_data_types_properties.md
nl -ba Manuals/Altibase_7.1/kor/SQL\ Reference.md | sed -n '15530,15610p'
nl -ba Manuals/Altibase_trunk/kor/SQL\ Reference.md | sed -n '13270,13390p'
nl -ba Manuals/Altibase_trunk/kor/General_Reference-1.Data\ Types\ \&\ Altibase\ Properties.md | sed -n '2770,2860p'
nl -ba Manuals/Altibase_7.1/kor/SQL\ Reference.md | sed -n '26010,26024p'
nl -ba Manuals/Altibase_trunk/kor/SQL\ Reference.md | sed -n '12540,12572p'
nl -ba Manuals/Altibase_trunk/kor/SQL\ Reference.md | sed -n '13752,13788p'
nl -ba Manuals/Altibase_trunk/kor/SQL\ Reference.md | sed -n '24940,25040p'
nl -ba Manuals/Altibase_trunk/kor/SQL\ Reference.md | sed -n '23618,24090p'
mkdir -p review/reports
git diff --check
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' | wc -l
rg -n 'trunk|Altibase_trunk|Manuals/|file://|C:\\|/home/' GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/04_sql_dml_oracle_compatibility.md
rg -n '!\[|media/|\.gif|\.png|\.jpg|\.jpeg' GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/04_sql_dml_oracle_compatibility.md
rg -n '^Verdict:|^\| (Blocker|High|Medium|Low) \|' review/reports/R07_dml_functions_oracle_overlap.md
git status --short
```

## Findings

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Note | `GPTs/attachments/04_sql_dml_oracle_compatibility.md` | 741 | Re-review confirmed the previous `REGEXP_MODE=1` finding is remediated: the attachment now states that Altibase 7.1 requires 7.1.0.7.7 or later for PCRE2-compatible mode, and retains the `US7ASCII`/`UTF-8` and syntax-difference cautions. | No further action for R07. |
| Note | `GPTs/attachments/04_sql_dml_oracle_compatibility.md` | 884 | Re-review confirmed the previous JSON path operand finding is remediated: the 8.1 JSON function section now says path operands for `JSON_EXISTS`, `JSON_QUERY`, and `JSON_VALUE` must be string-form path expressions and should not be bind variables, `NULL`, table columns, SQL functions, or user-defined functions unless a later exact source confirms support. | No further action for R07. |

No actionable `Blocker`, `High`, `Medium`, or `Low` findings remain for this stage.

## Source Checks

- Claims checked:
  - Ordinary DML compression and Altibase-specific DML syntax: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `MOVE`, `MERGE`, `RETURN`/`RETURNING`, row limiting, `FOR UPDATE`, multi-table DML, direct-path `INSERT /*+ APPEND */`, `LATERAL`/`APPLY`, `PIVOT`/`UNPIVOT`, recursive `WITH`, hierarchical query, set operators, and DML privileges.
  - Function behavior: `NVL`, `DECODE`, `ROWNUM`, sequence `NEXTVAL`/`CURRVAL`, analytic/window placement, ordered-set functions, `REGEXP_LIKE`, and `REGEXP_MODE`.
  - 8.1 JSON function and JSON column cautions: native `JSON`, `TEMPORARY_LOB_ENABLE`, `SELECT FOR UPDATE` restriction, `JSON_ARRAY`, `JSON_OBJECT`, `JSON_EXISTS`, `JSON_QUERY`, `JSON_VALUE`, `JSON_VALID`, and `IS JSON`.
- Source coverage:
  - Korean SQL Reference samples support the attachment's DML restrictions, direct-path insert restrictions, sequence behavior, `NVL` type rule, `ROWNUM` type/order note, recursive `WITH` limit, `LATERAL`/`APPLY` restrictions, and 7.1/7.3 availability of sampled DML features.
  - Korean 8.1 SQL Reference and General Reference support the JSON function names, defaults sampled, native `JSON` type, Temporary LOB prerequisite, `SELECT FOR UPDATE` restriction, and JSON path-expression restrictions.
  - Korean 7.1 SQL Reference supports the 7.1.0.7.7 patch boundary for PCRE2-compatible `REGEXP_MODE=1`; Korean 7.3 and 8.1 sources support the general `REGEXP_MODE` behavior and character-set cautions.
  - Korean release notes support the 8.1 JSON feature boundary.
- Korean/English source conflicts:
  - `GPTs/reports/eng_kor_parity.md` and `GPTs/reports/8_1_verification.md` already document that English 8.1 manuals lack the detailed JSON function, `IS JSON`, and Temporary LOB sections found in Korean sources. The attachment uses customer-safe English prose and does not expose internal source labels.
- Source gaps:
  - No source gap found for the sampled DML syntax, function cautions, or 8.1 JSON behavior in this stage.

## Oracle-Overlap Decision

- Correctly compressed:
  - `04_sql_dml_oracle_compatibility.md` does not teach generic Oracle DML at length. It keeps ordinary `SELECT`, `INSERT`, `UPDATE`, and `DELETE` patterns compact and expands only Altibase-specific syntax, restrictions, function differences, JSON behavior, queue DML, and answer templates.
  - `03_sql_ddl_generation.md` remains focused on DDL/storage/object generation and does not bloat ordinary DML.
- Too much generic Oracle material:
  - None found. The DML attachment is long, but the length is driven by Altibase-specific difference blocks, SQL limitations, function categories, and JSON function behavior that materially improve generated answers.
- Missing Altibase-specific difference:
  - None found after the current remediation. The previous JSON path operand and 7.1 `REGEXP_MODE=1` patch-boundary gaps are now present in the primary DML/function attachment.

## Version Checks

- 7.1:
  - Core DML, `MERGE WHEN NO ROWS`, `LATERAL`/`APPLY`, `PIVOT`/`UNPIVOT`, `RETURN`/`RETURNING`, recursive `WITH`, and REGEXP support were sampled from the Korean 7.1 SQL Reference.
  - The attachment now preserves the 7.1.0.7.7 patch caveat for PCRE2-compatible regex mode.
- 7.3:
  - Core DML and REGEXP behavior sampled from Korean 7.3 sources matched the attachment's general 7.3 baseline. No 7.3-specific issue found.
- 8.1:
  - Native `JSON`, JSON functions, `IS JSON`, Temporary LOB dependency, `SELECT FOR UPDATE` JSON restriction, and JSON path operand restrictions are source-backed by Korean 8.1 manuals and release notes.

## Retrieval And GPT Answer Quality

- Strengths:
  - The DML decision flow, compatibility classifier, difference blocks, and answer templates should help a GPT avoid claiming full Oracle compatibility.
  - Literal SQL tokens, property names, function names, and version labels are preserved.
  - 8.1 JSON is clearly separated from 7.1/7.3, and the key JSON path restriction is now directly retrievable from the primary DML/function attachment.
  - The regex patch caveat is now close to the `REGEXP_MODE=1` guidance, reducing risk for generic Altibase 7.1 answers.
- Risks:
  - The file is not a complete SQL Reference. For uncommon DML/function clauses outside the sampled sections, the GPT should still verify the exact target-version manual before producing executable SQL.
  - JSON detail is Korean-source-backed because English 8.1 manuals lack equivalent detail; future edits should keep the current English normalization rather than copying Korean prose directly.

## Required Follow-Up

- None for R07. This stage can proceed as `Verdict: Pass` if validation stays clean and the existing remediation changes are committed by the cycle owner.
