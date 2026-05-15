# R05 DML and Oracle Compatibility Compression

Date: 2026-05-14
Reviewer: Codex
Verdict: Review Required

## Scope
- Attachments:
  - `GPTs/attachments/04_sql_dml_oracle_compatibility.md`
  - `GPTs/attachments/15_migration_oracle_compatibility.md`
  - `GPTs/attachments/03_sql_ddl_generation.md`
- Supporting reports:
  - None used for final findings.
- Source manuals sampled:
  - `Manuals/Altibase_7.1/eng/SQL Reference.md`
  - `Manuals/Altibase_7.3/eng/SQL Reference.md`
  - `Manuals/Altibase_trunk/eng/SQL Reference.md`
  - `Manuals/Altibase_7.1/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_7.3/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_trunk/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_trunk/kor/SQL Reference.md`
  - `ReleaseNotes/eng/Altibase_7_3_0_0_1_Release_Notes.md`
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`
  - `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`
  - `ReleaseNotes/eng/Altibase_Migration_Center_7_15_Release_Notes.md`
  - `ReleaseNotes/eng/Altibase_Migration_Center_7_16_Release_Notes.md`
  - `ReleaseNotes/eng/Altibase_Migration_Center_7_18_Release_Notes.md`
  - `ReleaseNotes/kor/Altibase_Migration_Center_7_19_Release_Notes.md`

## Commands Run
```bash
sed -n '1,240p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,220p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,260p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
wc -l GPTs/attachments/04_sql_dml_oracle_compatibility.md GPTs/attachments/15_migration_oracle_compatibility.md GPTs/attachments/03_sql_ddl_generation.md
rg -n "^(#|##|###) " GPTs/attachments/04_sql_dml_oracle_compatibility.md
rg -n "^(#|##|###) " GPTs/attachments/15_migration_oracle_compatibility.md
rg -n "^(#|##|###) " GPTs/attachments/03_sql_ddl_generation.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' | sort | wc -l
rg -n "REGEXP_MODE|PCRE2|Perl Compatible|lookahead|backreference|JSON|SELECT FOR UPDATE|TEMPORARY_LOB_ENABLE" GPTs/attachments/04_sql_dml_oracle_compatibility.md GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/05_data_types_properties.md GPTs/attachments/15_migration_oracle_compatibility.md
rg -n "REGEXP_MODE|PCRE2|Perl Compatible Regular Expressions|backreferences|lookaheads" Manuals/Altibase_7.1/eng/SQL\ Reference.md Manuals/Altibase_7.1/eng/General\ Reference-1.Data\ Types\ \&\ Altibase\ Properties.md Manuals/Altibase_7.3/eng/General\ Reference-1.Data\ Types\ \&\ Altibase\ Properties.md Manuals/Altibase_trunk/eng/General\ Reference-1.Data\ Types\ \&\ Altibase\ Properties.md ReleaseNotes/eng/Altibase_7_3_0_0_1_Release_Notes.md
rg -n "JSON_ARRAY|JSON_OBJECT|JSON_EXISTS|JSON_QUERY|JSON_VALUE|JSON_VALID|IS JSON|TEMPORARY_LOB_ENABLE" GPTs/attachments/04_sql_dml_oracle_compatibility.md GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/05_data_types_properties.md ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md
rg -n "Convert Oversized String VARCHAR To CLOB|BINARY_DOUBLE|NaN|INF|JSON data type|Altibase 8.1|Oracle Database 10gR2|21c|6.5.1" GPTs/attachments/15_migration_oracle_compatibility.md ReleaseNotes/eng/Altibase_Migration_Center_7_15_Release_Notes.md ReleaseNotes/eng/Altibase_Migration_Center_7_16_Release_Notes.md ReleaseNotes/eng/Altibase_Migration_Center_7_18_Release_Notes.md ReleaseNotes/kor/Altibase_Migration_Center_7_19_Release_Notes.md
nl -ba GPTs/attachments/04_sql_dml_oracle_compatibility.md | sed -n '724,746p'
nl -ba GPTs/attachments/04_sql_dml_oracle_compatibility.md | sed -n '858,866p'
nl -ba GPTs/attachments/03_sql_ddl_generation.md | sed -n '348,363p'
nl -ba GPTs/attachments/05_data_types_properties.md | sed -n '565,590p'
nl -ba Manuals/Altibase_7.1/eng/SQL\ Reference.md | sed -n '23300,23580p'
nl -ba GPTs/attachments/15_migration_oracle_compatibility.md | sed -n '445,557p'
```

## Findings
No Blocker issues were found.

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| High | `GPTs/attachments/04_sql_dml_oracle_compatibility.md` | 740 | The `REGEXP_LIKE` note says Altibase regular expression support is partial POSIX BRE/ERE and that multibyte characters, backreferences, lookaheads, lookbehinds, and conditional regular expressions are unsupported. That describes only the default Altibase regular expression library. The 7.1 SQL Reference documents a selectable PCRE2 library from Altibase 7.1.0.7.7, and 7.3/trunk property manuals plus 7.3 release notes document `REGEXP_MODE`/PCRE2 compatibility mode. As written, the attachment can make the GPT incorrectly reject valid PCRE2-mode regex answers. | Split the note into default Altibase regex mode versus PCRE2-compatible mode. Mention `REGEXP_MODE=1`, `ALTER SYSTEM SET REGEXP_MODE=1`, `ALTER SESSION SET REGEXP_MODE=1`, the `US7ASCII` or `UTF-8` server character set requirement, and that syntax differs between the two libraries. Keep it compact and cross-reference `05_data_types_properties.md` and `07_error_messages_troubleshooting.md` rather than adding a full regex manual. |
| Medium | `GPTs/attachments/04_sql_dml_oracle_compatibility.md` | 858 | The 8.1 JSON function section preserves `JSON_ARRAY`, `JSON_OBJECT`, `JSON_EXISTS`, `JSON_QUERY`, `JSON_VALUE`, `JSON_VALID`, and `IS JSON`, but it does not carry the DML-side native `JSON` column cautions that are important for generated SQL: `JSON` processing uses Temporary LOB, `TEMPORARY_LOB_ENABLE` must be `1`, and `JSON` cannot be used with `SELECT FOR UPDATE`. Those cautions are present in `03_sql_ddl_generation.md` and `05_data_types_properties.md`, but a DML/JSON retrieval may land on this attachment alone. | Add a short "JSON column DML cautions" block to `04_sql_dml_oracle_compatibility.md`: native `JSON` is 8.1 only, check `TEMPORARY_LOB_ENABLE`, treat JSON columns as LOB-like for restrictions, and do not generate `SELECT FOR UPDATE` against `JSON` columns. Cross-reference `05_data_types_properties.md` for details. |

## Source Checks
- Claims checked:
  - Ordinary `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `MOVE`, `MERGE`, multi-table insert/delete, `RETURN`/`RETURNING`, `LIMIT`, `TOP`, `ROWNUM`, `FOR UPDATE`, recursive `WITH`, `LATERAL`, `APPLY`, hierarchical query, grouping extension, `PIVOT`, and `UNPIVOT` behavior against 7.1, 7.3, and trunk SQL Reference samples.
  - 8.1 JSON function names and `TEMPORARY_LOB_ENABLE` against 8.1 release notes and existing JSON type coverage.
  - Oracle migration type and option coverage against Migration Center 7.15, 7.16, 7.18, and 7.19 release notes.
  - `REGEXP_MODE` and PCRE2 behavior against 7.1 SQL Reference, 7.1/7.3/trunk property manuals, and 7.3 release notes.
- Source coverage:
  - `04_sql_dml_oracle_compatibility.md` is generally well compressed for ordinary DML and preserves many Altibase-specific DML restrictions.
  - `15_migration_oracle_compatibility.md` has strong migration-focused coverage for JSON mapping, oversized strings, `BINARY_DOUBLE`, `NaN`/`INF`, `NCLOB`, `ROWID`, empty strings, defaults, PSM conversion, and tool scope.
  - `03_sql_ddl_generation.md` preserves the DDL-side JSON, LOB, temporary table, partition, storage, and Oracle conversion cautions needed by this stage.
- Source gaps:
  - The regex issue is an attachment synthesis gap, not a source gap. The PCRE2/`REGEXP_MODE` source signal is present and cross-version.
  - The JSON DML caution is covered elsewhere, but `04_sql_dml_oracle_compatibility.md` should carry a compact copy or pointer because it is the primary DML retrieval target.

## Oracle-Overlap Decision
- Correctly compressed:
  - Ordinary Oracle-overlapping `SELECT`, `INSERT`, `UPDATE`, and `DELETE` syntax is kept brief in `04_sql_dml_oracle_compatibility.md`.
  - `15_migration_oracle_compatibility.md` focuses on migration tool behavior, object support, data type mappings, default/empty string conversion, LOB validation, Adapter for Oracle, and version/tool scope instead of restating generic Oracle SQL.
  - `03_sql_ddl_generation.md` keeps Oracle DDL conversion advice scoped to Altibase storage, partitioning, temporary tables, LOB/JSON, identifiers, and unsupported Oracle clauses.
- Too much generic Oracle material:
  - No material bloat found in the sampled DML or migration sections.
- Missing Altibase-specific difference:
  - `REGEXP_MODE=1` PCRE2-compatible regex mode is missing from the `REGEXP_LIKE` compatibility note.
  - `04_sql_dml_oracle_compatibility.md` does not locally carry the 8.1 native `JSON` column DML restrictions.

## Version Checks
- 7.1:
  - Core DML coverage is consistent with sampled SQL Reference behavior.
  - Regex guidance must distinguish the default Altibase regex library from the PCRE2 library available from Altibase 7.1.0.7.7.
  - 8.1 JSON functions are correctly excluded.
- 7.3:
  - Core DML baseline is treated consistently with 7.1.
  - `REGEXP_MODE`/PCRE2 compatibility mode is documented and should not be implied absent.
  - 8.1 JSON functions are correctly excluded.
- 8.1:
  - JSON function names and `IS JSON` are preserved in `04_sql_dml_oracle_compatibility.md`.
  - The DML file should connect JSON function usage with native `JSON` column restrictions already present in `03_sql_ddl_generation.md` and `05_data_types_properties.md`.

## Retrieval And GPT Answer Quality
- Strengths:
  - The classifier in `04_sql_dml_oracle_compatibility.md` should help the GPT avoid over-answering generic Oracle-like DML.
  - The compact syntax blocks expose high-value Altibase differences without expanding into full SQL Reference duplication.
  - Migration content in `15_migration_oracle_compatibility.md` is practical and answer-oriented, especially for tool options and conversion risks.
- Risks:
  - Regex answers can be wrong for users using `REGEXP_MODE=1` or asking about Korean regex search, backreferences, lookaheads, or lookbehinds.
  - JSON DML answers generated from `04_sql_dml_oracle_compatibility.md` alone may miss `TEMPORARY_LOB_ENABLE` and `SELECT FOR UPDATE` restrictions.

## Required Follow-Up
- Update `GPTs/attachments/04_sql_dml_oracle_compatibility.md` to correct the `REGEXP_LIKE`/PCRE2 compatibility guidance.
- Add a compact native `JSON` column DML caution block to `GPTs/attachments/04_sql_dml_oracle_compatibility.md`.
- Re-run focused validation searches for `REGEXP_MODE`, `PCRE2`, `TEMPORARY_LOB_ENABLE`, `SELECT FOR UPDATE`, and JSON function names after remediation.
