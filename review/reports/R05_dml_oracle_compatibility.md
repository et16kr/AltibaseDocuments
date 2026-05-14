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
  - None. Review design, selection, workplan, and attachment README were read as stage context.
- Source manuals sampled:
  - `Manuals/Altibase_7.1/eng/SQL Reference.md`
  - `Manuals/Altibase_7.3/eng/SQL Reference.md`
  - `Manuals/Altibase_trunk/eng/SQL Reference.md`
  - `Manuals/Altibase_trunk/kor/SQL Reference.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`
  - `Manuals/Tools/Altibase_trunk/eng/Migration Center User's Manual.md`
  - `Manuals/Tools/Altibase_release/eng/Migration Center User's Manual.md`
  - `Manuals/Altibase_7.1/eng/Adapter for Oracle User's Manual.md`
  - `Manuals/Altibase_7.3/eng/Adapter for Oracle User's Manual.md`
  - `Manuals/Altibase_trunk/eng/Adapter for Oracle User's Manual.md`

## Commands Run

```bash
sed -n '1,240p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,240p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,240p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
wc -l GPTs/attachments/04_sql_dml_oracle_compatibility.md GPTs/attachments/15_migration_oracle_compatibility.md GPTs/attachments/03_sql_ddl_generation.md
rg -n "^(#|##|###) " GPTs/attachments/04_sql_dml_oracle_compatibility.md GPTs/attachments/15_migration_oracle_compatibility.md GPTs/attachments/03_sql_ddl_generation.md
rg -n "SELECT Pattern|INSERT Pattern|UPDATE Pattern|DELETE Pattern|DML RETURN Clause|8\.1 JSON Functions|Oracle-to-Altibase Data Type Mapping Blocks|Empty String Handling Blocks|Oracle DDL Conversion Rules" GPTs/attachments/04_sql_dml_oracle_compatibility.md GPTs/attachments/15_migration_oracle_compatibility.md GPTs/attachments/03_sql_ddl_generation.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name README.md | sort | wc -l
rg -n "trunk|file://|/home/|/Users/|C:\\|media/|!\[|\.png|\.gif" GPTs/attachments/04_sql_dml_oracle_compatibility.md GPTs/attachments/15_migration_oracle_compatibility.md GPTs/attachments/03_sql_ddl_generation.md
rg -n "Oracle SQL is fully compatible|fully compatible|drop-in compatible|unchanged" GPTs/attachments/04_sql_dml_oracle_compatibility.md GPTs/attachments/15_migration_oracle_compatibility.md GPTs/attachments/03_sql_ddl_generation.md
rg -n "LIMIT clause|TOP \(expr\)|LATERAL|APPLY|returning clause|multiple delete|WHEN NO ROWS|INLIST" Manuals/Altibase_7.1/eng/SQL\ Reference.md Manuals/Altibase_7.3/eng/SQL\ Reference.md Manuals/Altibase_trunk/eng/SQL\ Reference.md
rg -n "JSON_ARRAY|JSON_OBJECT|JSON_EXISTS|JSON_QUERY|JSON_VALUE|JSON_VALID|IS JSON" Manuals/Altibase_7.1/eng/SQL\ Reference.md Manuals/Altibase_7.3/eng/SQL\ Reference.md || true
rg -n "JSON_ARRAY|JSON_OBJECT|JSON_EXISTS|JSON_QUERY|JSON_VALUE|JSON_VALID|IS JSON" ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md Manuals/Altibase_trunk/kor/SQL\ Reference.md Manuals/Altibase_trunk/kor/General_Reference-1.Data\ Types\ \&\ Altibase\ Properties.md
rg -n "Convert Oversized String VARCHAR To CLOB|Default '' \(Empty String\)|volatile tablespace|IS JSON check constraint|VARCHAR2 defined|NCLOB|ROWID|JSON          \| CLOB or JSON|BINARY DOUBLE" Manuals/Tools/Altibase_trunk/eng/Migration\ Center\ User\'s\ Manual.md Manuals/Tools/Altibase_release/eng/Migration\ Center\ User\'s\ Manual.md
```

## Findings

No Blocker, High, Medium, or Low issues were found.

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Note | All scoped attachments | - | Ordinary Oracle-overlapping DML is not bloated enough to risk wrong generated answers, and Altibase-specific DML differences, JSON behavior, data type conversion behavior, and migration risks are preserved. | No attachment changes required for R05. |

## Source Checks

- Claims checked:
  - `04_sql_dml_oracle_compatibility.md` keeps ordinary `SELECT`, `INSERT`, `UPDATE`, and `DELETE` in compact pattern/check blocks at lines 74, 164, 197, and 218, while preserving Altibase-specific row limiting, `LATERAL`/`APPLY`, hierarchical restrictions, DML `RETURN`, multi-table insert/delete, `MERGE WHEN NO ROWS`, `INLIST`, and JSON function boundaries.
  - 7.1/7.3/trunk English SQL Reference samples support the non-JSON DML claims: `LIMIT`, `TOP (expr)`, `LATERAL`, `APPLY`, returning-clause limitations, multiple-delete limitations, `WHEN NO ROWS`, and `INLIST` were found in all three sampled English SQL References.
  - 8.1 JSON function coverage in `04_sql_dml_oracle_compatibility.md` lines 858-1022 is supported by the 8.1 release notes and verified Korean SQL Reference/General Reference source. The sampled English trunk SQL Reference did not contain JSON function sections.
  - `15_migration_oracle_compatibility.md` preserves migration-risk claims for Oracle temporary tables, external/hybrid/blockchain/immutable table conversion, `IS JSON` check constraints, `VARCHAR2` byte conversion, oversized string-to-`CLOB`, `BINARY DOUBLE` `NaN`/`INF`, `NCLOB`, `ROWID`, JSON column mapping, default conversions, empty strings, LOB `NOT NULL`, validation limits, and Adapter for Oracle DML/DDL constraints.
  - `03_sql_ddl_generation.md` lines 1904-1919 correctly keeps Oracle DDL conversion as DDL-specific cross-reference material and does not duplicate ordinary DML.
- Source coverage:
  - Good coverage for DML compression and Altibase-specific syntax in `04`.
  - Good coverage for migration/data type behavior in `15`.
  - Good cross-reference coverage for Oracle DDL conversion boundaries in `03`.
- Source gaps:
  - The English trunk SQL Reference sample has no `JSON_ARRAY`, `JSON_OBJECT`, `JSON_EXISTS`, `JSON_QUERY`, `JSON_VALUE`, `JSON_VALID`, or `IS JSON` hits. The attachment's JSON content is still source-backed through the 8.1 release notes and verified Korean source, but a future source-parity audit should confirm whether an English 8.1 SQL Reference update exists.

## Oracle-Overlap Decision

- Correctly compressed:
  - Yes. `04` uses a classifier and compact syntax/check blocks instead of expanding generic Oracle-like DML. Ordinary DML is summarized, while high-risk differences such as row limiting, `RETURN`, `MERGE WHEN NO ROWS`, multi-table DML, queue DML, function differences, and JSON version boundaries remain searchable.
  - `15` focuses on migration decisions, conversion risks, and tool behavior rather than teaching generic Oracle SQL.
  - `03` limits Oracle compatibility discussion to DDL conversion rules and refers DML questions back to `04`.
- Too much generic Oracle material:
  - None that should block upload. The condition/function syntax blocks in `04` are the largest Oracle-overlap area, but they include Altibase-specific restrictions and retrieval tokens and are not likely to produce wrong answers.
- Missing Altibase-specific difference:
  - None found in the reviewed scope that is likely to cause wrong generated answers.

## Version Checks

- 7.1:
  - `04` correctly treats core DML features as available from the 7.1 SQL Reference and blocks 8.1 JSON function generation for 7.1.
  - `15` preserves 7.1 Adapter for Oracle and migration behavior without treating Migration Center tool release numbers as Altibase server versions.
- 7.3:
  - `04` correctly uses the same core DML baseline as 7.1 and blocks 8.1 JSON function generation for 7.3.
  - `15` preserves 7.3 migration and Adapter for Oracle scope and keeps Migration Center `7.19` as a tool version.
- 8.1:
  - `04` covers native JSON functions and `IS JSON` as 8.1 verified-source features.
  - `03` and `15` preserve JSON data type, Temporary LOB, and Oracle JSON migration boundaries for 8.1.

## Retrieval And GPT Answer Quality

- Strengths:
  - `04` starts with direct answer rules and a compatibility classifier, making it likely that GPT answers will say "similar but check differences" instead of overclaiming Oracle compatibility.
  - JSON functions are grouped with defaults, return-type limits, examples, and version boundaries.
  - `15` is organized by migration workflow, option blocks, object support, data type mapping, defaults, empty strings, verification, troubleshooting, and Adapter for Oracle, which should retrieve well for migration questions.
  - `03` has a concise Oracle DDL conversion section that prevents DML/DDL compatibility guidance from being scattered.
- Risks:
  - Source traceability for 8.1 JSON depends on Korean verified source plus release notes because the sampled English trunk SQL Reference lacks JSON function sections.
  - The broad function list in `04` should not be treated as a full semantic compatibility promise; the attachment already warns to check function differences and implicit conversion edge cases.

## Required Follow-Up

- None for R05 acceptance.
- Optional later audit: confirm whether an English 8.1 SQL Reference with JSON function sections becomes available, then update source traceability notes if needed.
