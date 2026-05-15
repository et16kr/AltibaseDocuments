# R05 DML and Oracle Compatibility Compression

Date: 2026-05-14
Reviewer: Codex
Verdict: Pass

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
No Blocker issues were found. V02 re-review confirms that all previously listed findings are closed by the remediation tasks named in the recommendation column.

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Resolved High | `GPTs/attachments/04_sql_dml_oracle_compatibility.md` | 740 | The `REGEXP_LIKE` note says Altibase regular expression support is partial POSIX BRE/ERE and that multibyte characters, backreferences, lookaheads, lookbehinds, and conditional regular expressions are unsupported. That describes only the default Altibase regular expression library. The 7.1 SQL Reference documents a selectable PCRE2 library from Altibase 7.1.0.7.7, and 7.3/trunk property manuals plus 7.3 release notes document `REGEXP_MODE`/PCRE2 compatibility mode. As written, the attachment can make the GPT incorrectly reject valid PCRE2-mode regex answers. | Resolved by H03. The regex mode split is no longer an open High gate item. |
| Resolved Medium | `GPTs/attachments/04_sql_dml_oracle_compatibility.md` | 858 | The 8.1 JSON function section preserved JSON function literals but did not carry the DML-side native `JSON` column cautions for Temporary LOB processing, `TEMPORARY_LOB_ENABLE`, and `SELECT FOR UPDATE`. | Resolved by M06. The DML attachment now includes compact native `JSON` column DML cautions and cross-references the data type attachment. |

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
  - The regex issue was an attachment synthesis gap, not a source gap; it is closed by H03.
  - The JSON DML caution is now carried in `04_sql_dml_oracle_compatibility.md` by M06.

## Oracle-Overlap Decision
- Correctly compressed:
  - Ordinary Oracle-overlapping `SELECT`, `INSERT`, `UPDATE`, and `DELETE` syntax is kept brief in `04_sql_dml_oracle_compatibility.md`.
  - `15_migration_oracle_compatibility.md` focuses on migration tool behavior, object support, data type mappings, default/empty string conversion, LOB validation, Adapter for Oracle, and version/tool scope instead of restating generic Oracle SQL.
  - `03_sql_ddl_generation.md` keeps Oracle DDL conversion advice scoped to Altibase storage, partitioning, temporary tables, LOB/JSON, identifiers, and unsupported Oracle clauses.
- Too much generic Oracle material:
  - No material bloat found in the sampled DML or migration sections.
- Missing Altibase-specific difference:
  - Closed by H03: `REGEXP_MODE=1` PCRE2-compatible regex mode has been added to the `REGEXP_LIKE` compatibility note.
  - Closed by M06: `04_sql_dml_oracle_compatibility.md` locally carries the 8.1 native `JSON` column DML restrictions.

## Version Checks
- 7.1:
  - Core DML coverage is consistent with sampled SQL Reference behavior.
  - Closed by H03: regex guidance now distinguishes the default Altibase regex library from the PCRE2 library available from Altibase 7.1.0.7.7.
  - 8.1 JSON functions are correctly excluded.
- 7.3:
  - Core DML baseline is treated consistently with 7.1.
  - `REGEXP_MODE`/PCRE2 compatibility mode is documented and should not be implied absent.
  - 8.1 JSON functions are correctly excluded.
- 8.1:
  - JSON function names and `IS JSON` are preserved in `04_sql_dml_oracle_compatibility.md`.
  - The DML file now connects JSON function usage with native `JSON` column restrictions already present in `03_sql_ddl_generation.md` and `05_data_types_properties.md`.

## Retrieval And GPT Answer Quality
- Strengths:
  - The classifier in `04_sql_dml_oracle_compatibility.md` should help the GPT avoid over-answering generic Oracle-like DML.
  - The compact syntax blocks expose high-value Altibase differences without expanding into full SQL Reference duplication.
  - Migration content in `15_migration_oracle_compatibility.md` is practical and answer-oriented, especially for tool options and conversion risks.
- Risks:
  - The regex and JSON DML retrieval risks are closed by H03 and M06.

## V02 Closure
- Closed by H03: `REGEXP_LIKE` and PCRE2 compatibility guidance.
- Closed by M06: native `JSON` column DML cautions in `GPTs/attachments/04_sql_dml_oracle_compatibility.md`.
- No open R05 finding remains after V02 re-review of the changed sections.
