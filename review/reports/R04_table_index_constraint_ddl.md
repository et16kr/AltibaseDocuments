# R04 Table, Index, Constraint DDL Review

Date: 2026-05-14
Reviewer: Codex
Verdict: Review Required

## Scope

- Attachments: `GPTs/attachments/03_sql_ddl_generation.md`; `GPTs/attachments/05_data_types_properties.md`; `GPTs/attachments/08_performance_tuning_monitoring.md`
- Supporting reports: `GPTs/reports/8_1_verification.md`
- Source manuals sampled: `Manuals/Altibase_7.1/eng/SQL Reference.md`; `Manuals/Altibase_7.3/eng/SQL Reference.md`; `Manuals/Altibase_trunk/eng/SQL Reference.md`; `Manuals/Altibase_trunk/eng/General Reference-1.Data Types & Altibase Properties.md`; `Manuals/Altibase_trunk/eng/General Reference-2.The Data Dictionary.md`; Korean 8.1 fallback sections for JSON and Temporary LOB

## Commands Run

```bash
sed -n '1,240p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,220p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,260p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
nl -ba GPTs/attachments/03_sql_ddl_generation.md | sed -n '223,365p'
nl -ba GPTs/attachments/03_sql_ddl_generation.md | sed -n '1175,1335p'
nl -ba GPTs/attachments/03_sql_ddl_generation.md | sed -n '1437,1735p'
nl -ba GPTs/attachments/05_data_types_properties.md | sed -n '455,610p'
nl -ba GPTs/attachments/08_performance_tuning_monitoring.md | sed -n '931,1148p'
rg -n "CREATE TABLE|PARTITION BY|LOCALUNIQUE|DIRECTKEY|LOB \\(|JSON|IF NOT EXISTS|IF EXISTS" Manuals/Altibase_7.1/eng/SQL\ Reference.md Manuals/Altibase_7.3/eng/SQL\ Reference.md Manuals/Altibase_trunk/eng/SQL\ Reference.md
rg -n "SYS_CONSTRAINTS_|SYS_INDEX_COLUMNS_|SYS_INDICES_|SYS_PART_INDICES_|SYS_INDEX_PARTITIONS_" Manuals/Altibase_trunk/eng/General\ Reference-2.The\ Data\ Dictionary.md
rg -n "trunk|Altibase_trunk|file://|/home/|C:\\\\|IF NOT EXISTS|IF EXISTS|JSON|Temporary LOB|DIRECTKEY|RANGE PARTITIONING USING HASH|TO_DATE\\(" GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/05_data_types_properties.md GPTs/attachments/08_performance_tuning_monitoring.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name README.md | sort | wc -l
rg -n '!\\[|media/|\\.png|\\.gif|\\.jpg|\\.jpeg' GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/05_data_types_properties.md GPTs/attachments/08_performance_tuning_monitoring.md
```

## Findings

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| High | `GPTs/attachments/03_sql_ddl_generation.md` | 31 | The core rule says to omit `IF NOT EXISTS` and `IF EXISTS` for 7.1/7.3 unless the customer targets 8.1 "or explicitly requests idempotent DDL." That second exception can make GPT generate 8.1-only syntax for 7.1 or 7.3 when the user asks for idempotent DDL. Later lines correctly say to omit these clauses for 7.1/7.3, but retrieval could surface only the broader rule. | Make the idempotent exception explicitly 8.1-only. For 7.1/7.3, recommend metadata pre-check SQL plus application or script-side conditional execution instead of SQL-level `IF EXISTS` / `IF NOT EXISTS`. |
| High | `GPTs/attachments/05_data_types_properties.md` | 97 | LOB `IN ROW` syntax is not version-differentiated. The 7.1/7.3 English manuals show `BLOB [ VARIABLE ( IN ROW size ) ]` and `CLOB [ VARIABLE ( IN ROW size ) ]`, while the 8.1 Korean fallback shows `BLOB [ IN ROW size ]` and `CLOB [ IN ROW size ]`. The attachment presents the 7.x-style form as common syntax, which risks wrong 8.1 DDL if `VARIABLE` is not accepted for 8.1 LOB declarations. | Split LOB syntax by source/version, or add a source-audit note. Prefer `BLOB [IN ROW size]` / `CLOB [IN ROW size]` for 8.1 verified-source answers unless compatibility with `VARIABLE (IN ROW size)` is confirmed. |
| Medium | `GPTs/attachments/03_sql_ddl_generation.md` | 291 | Compact partition syntax covers only `RANGE`, `LIST`, and `HASH`. The SQL Reference also documents `RANGE PARTITIONING USING HASH`, with a single partition key and ranges based on the hash value modulo `1000`. This is an Altibase-specific partitioning form and is currently omitted from the generation guidance. | Add a compact `range_partitioning_using_hash` pattern, version scope, restrictions, and one small example. Cross-reference the same restriction in the partitioning notes and DDL checklist. |
| Medium | `GPTs/attachments/03_sql_ddl_generation.md` | 1241 | Range partition examples use bare string values such as `'01-JAN-2026'` and the split example uses `AT ('01-JAN-2027')` for a `DATE` partition key. Source examples use `TO_DATE(...)`, and bare strings depend on date format/session assumptions. | Use explicit conversion in partition boundary examples, such as `TO_DATE('2026-01-01', 'YYYY-MM-DD')`, or another documented unambiguous Altibase date form. Add the "full date literal" caution to partition bounds, not only `CHECK` constraints. |
| Medium | `GPTs/attachments/03_sql_ddl_generation.md` | 456 | Direct-key notes include the major storage restrictions, but omit the supported data-type and `MAXSIZE` behavior from the SQL Reference. The source says unsupported non-partial-key sizes fail, partial-key types store a prefix, default `MAXSIZE` is `8`, and only listed types support direct key indexes. | Add a compact direct-key eligibility block covering default `MAXSIZE`, full-key versus partial-key behavior, supported type families, and failure behavior for unsupported types. Mirror the short version in `08_performance_tuning_monitoring.md`. |
| Low | `GPTs/attachments/03_sql_ddl_generation.md` | 419 | The index syntax block omits 8.1 `IF NOT EXISTS` for `CREATE INDEX` and `IF EXISTS` for `DROP INDEX`, even though the 8.1 SQL Reference documents both and the file otherwise emphasizes idempotent DDL. | Add the optional clauses to the index syntax with the same 8.1-only warning used for tables and tablespaces. |
| Low | `GPTs/attachments/03_sql_ddl_generation.md` | 1683 | The index-column verification query joins `SYS_INDEX_COLUMNS_` and `SYS_COLUMNS_` by `TABLE_ID`/`COLUMN_ID` but not `USER_ID`, even though both meta tables include `USER_ID`. The current scoped example is likely to work, but the join is weaker than the constraint queries and can be copied into broader answers. | Include `i.user_id = ic.user_id`, `ic.user_id = c.user_id`, and the matching `USER_ID` predicates in both `03` and the similar metadata query in `08`. |

## Source Checks

- Claims checked: 8.1-only `IF EXISTS` / `IF NOT EXISTS`; temporary-table restrictions; LOB storage and LOB restrictions; JSON 8.1 restrictions; range/list/hash partition behavior; `RANGE PARTITIONING USING HASH`; `LOCALUNIQUE`; direct-key restrictions; dictionary columns for constraint and index verification.
- Source coverage: Core table, partition, LOB, constraint, and index claims are mostly source-backed. JSON and Temporary LOB claims align with the 8.1 release notes and Korean fallback documented by `GPTs/reports/8_1_verification.md`.
- Source gaps: 8.1 LOB syntax needs an explicit compatibility decision because English trunk retains the 7.x-style LOB syntax while Korean 8.1 fallback shows simplified `BLOB [ IN ROW size ]` / `CLOB [ IN ROW size ]`.

## Oracle-Overlap Decision

- Correctly compressed: Ordinary table, constraint, and index concepts are kept brief where they overlap with Oracle.
- Too much generic Oracle material: None found in this stage.
- Missing Altibase-specific difference: `RANGE PARTITIONING USING HASH` and direct-key supported type / `MAXSIZE` behavior should be made visible because GPTs are likely to miss those from general database knowledge.

## Version Checks

- 7.1: Native `JSON`, Temporary LOB, `IF EXISTS`, and `IF NOT EXISTS` are generally kept out of 7.1 guidance, except for the ambiguous idempotent-DDL exception at line 31.
- 7.3: Same as 7.1. Core table, partition, LOB, direct-key, and dictionary metadata claims sampled against 7.3 match the common 7.x source pattern.
- 8.1: JSON and Temporary LOB restrictions are visible and properly narrow. LOB `IN ROW` syntax needs version-specific resolution against the Korean 8.1 fallback.

## Retrieval And GPT Answer Quality

- Strengths: The three attachments are well structured for retrieval and contain explicit post-DDL verification SQL for constraints, indexes, partitions, JSON/Temporary LOB, and performance checks. JSON and JSON-plan wording is conservative and avoids inventing unsupported JSON plan fields.
- Risks: A GPT may retrieve the compact syntax blocks without the later cautions. The highest-risk examples are idempotent DDL for 7.1/7.3, 8.1 LOB `IN ROW` syntax, and ambiguous date strings in partition DDL.

## Required Follow-Up

- Resolve the two High findings before treating this stage as passable.
- Add the omitted Altibase-specific partition and direct-key details.
- Tighten date boundary examples and dictionary joins in copied verification SQL.
