# R04 Table, Index, And Constraint DDL Review

Date: 2026-05-14
Reviewer: Codex
Verdict: Pass

## Scope

- Attachments:
  - `GPTs/attachments/03_sql_ddl_generation.md`
  - `GPTs/attachments/05_data_types_properties.md`
  - `GPTs/attachments/08_performance_tuning_monitoring.md`
- Supporting reports:
  - `GPTs/reports/8_1_verification.md`
- Source manuals sampled:
  - `Manuals/Altibase_7.1/eng/SQL Reference.md`
  - `Manuals/Altibase_7.3/eng/SQL Reference.md`
  - `Manuals/Altibase_trunk/eng/SQL Reference.md`
  - `Manuals/Altibase_7.1/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_7.3/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_trunk/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_trunk/eng/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`

## Commands Run

```bash
sed -n '1,240p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,220p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,260p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
rg -n "^(#|##|###) " GPTs/attachments/03_sql_ddl_generation.md
rg -n "^(#|##|###) " GPTs/attachments/05_data_types_properties.md
rg -n "^(#|##|###) " GPTs/attachments/08_performance_tuning_monitoring.md
nl -ba GPTs/attachments/03_sql_ddl_generation.md | sed -n '223,369p'
nl -ba GPTs/attachments/03_sql_ddl_generation.md | sed -n '421,481p'
nl -ba GPTs/attachments/03_sql_ddl_generation.md | sed -n '1192,1772p'
nl -ba GPTs/attachments/05_data_types_properties.md | sed -n '460,620p'
nl -ba GPTs/attachments/08_performance_tuning_monitoring.md | sed -n '856,1147p'
rg -n 'IF NOT EXISTS|IF EXISTS|JSON|Temporary LOB|TEMPORARY_LOB|DIRECTKEY|LOCALUNIQUE|RANGE_USING_HASH|SYS_CONSTRAINTS_|SYS_INDEX_PARTITIONS_|SYS_PART_INDICES_|V\$TEMPORARY_LOBS' "Manuals/Altibase_7.1/eng/SQL Reference.md" "Manuals/Altibase_7.3/eng/SQL Reference.md" "Manuals/Altibase_trunk/eng/SQL Reference.md" GPTs/reports/8_1_verification.md
rg -n 'LOB columns|LOB.*volatile|volatile.*LOB|temporary.*LOB|disk temporary|BLOB|CLOB|IN ROW|VARIABLE \(IN ROW|JSON \[|SELECT FOR UPDATE' "Manuals/Altibase_7.1/eng/General Reference-1.Data Types & Altibase Properties.md" "Manuals/Altibase_7.3/eng/General Reference-1.Data Types & Altibase Properties.md" "Manuals/Altibase_trunk/eng/General Reference-1.Data Types & Altibase Properties.md"
rg -n 'LOB|JSON|TEMPORARY_LOB|V\$TEMPORARY_LOBS|SELECT FOR UPDATE|IN ROW' "Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md" "Manuals/Altibase_trunk/kor/SQL Reference.md"
rg -n 'SYS_CONSTRAINTS_|SYS_CONSTRAINT_COLUMNS_|SYS_INDICES_|SYS_INDEX_COLUMNS_|SYS_PART_INDICES_|SYS_INDEX_PARTITIONS_|SYS_TABLE_PARTITIONS_|V\$DISK_BTREE_HEADER|V\$TEMPORARY_LOBS' "Manuals/Altibase_trunk/eng/General Reference-2.The Data Dictionary.md" "Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md"
find review -maxdepth 2 -type f -path 'review/reports/*' | sort
```

## Findings

No Blocker, High, Medium, or Low issues were found in the scoped review.

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Note | `GPTs/attachments/03_sql_ddl_generation.md`; `GPTs/attachments/05_data_types_properties.md`; `GPTs/attachments/08_performance_tuning_monitoring.md` | - | The reviewed DDL guidance keeps 8.1-only syntax and features scoped to 8.1, and the Altibase-specific restrictions for partitions, LOB, JSON, indexes, direct key indexes, and constraint metadata are visible. | No attachment change required for R04. |

## Source Checks

- Claims checked:
  - Table DDL, temporary table restrictions, `MAXROWS`, range/list/hash partition notes, `RANGE_USING_HASH`, row movement, and LOB tablespace placement.
  - LOB storage syntax, 7.x `BLOB [VARIABLE (IN ROW size)]` / `CLOB [VARIABLE (IN ROW size)]`, 8.1 `BLOB [IN ROW size]` / `CLOB [IN ROW size]`, volatile/disk-temporary LOB restrictions, partition-key and index restrictions.
  - 8.1 native `JSON`, Temporary LOB prerequisites, `V$TEMPORARY_LOBS`, JSON depth, `SELECT FOR UPDATE` restriction, and JSON function family.
  - `CREATE INDEX`, `LOCALUNIQUE`, `BTREE`/`RTREE`, local index limits, direct key restrictions, `MAXSIZE`, function-based index restrictions, and `QUERY_REWRITE_ENABLE`.
  - Constraint and index verification SQL column names for `SYSTEM_.SYS_CONSTRAINTS_`, `SYSTEM_.SYS_CONSTRAINT_COLUMNS_`, `SYSTEM_.SYS_INDICES_`, `SYSTEM_.SYS_INDEX_COLUMNS_`, `SYSTEM_.SYS_PART_INDICES_`, `SYSTEM_.SYS_INDEX_PARTITIONS_`, `SYSTEM_.SYS_TABLE_PARTITIONS_`, and `V$DISK_BTREE_HEADER`.
- Source coverage:
  - 7.1/7.3 SQL Reference sources support the shared table, partition, LOB, local index, direct key, and constraint guidance.
  - 8.1 English SQL Reference supports `IF NOT EXISTS` / `IF EXISTS` on the sampled DDL objects, including table, index, queue, tablespace, replication, user, view, synonym, trigger, directory, sequence, and materialized view forms.
  - `GPTs/reports/8_1_verification.md` confirms that JSON and Temporary LOB require the 8.1 verified source path because English 8.1 manual coverage is incomplete and Korean source/manual fallback supplies the detailed feature text.
- Source gaps:
  - This was a source review only. No live Altibase instance was available, so example SQL was not executed.
  - JSON and Temporary LOB details remain partly Korean-source-backed through the existing 8.1 verification report rather than fully covered by the English 8.1 manuals.

## Oracle-Overlap Decision

- Correctly compressed:
  - Generic Oracle-like DDL is not expanded unnecessarily. The reviewed sections focus on Altibase storage, partitioning, LOB, index, direct key, JSON, and metadata behavior.
- Too much generic Oracle material:
  - None found in this stage.
- Missing Altibase-specific difference:
  - None found in this stage. Oracle conversion warnings correctly call out Altibase differences for storage target, temporary tables, LOB storage, JSON, partitioning, queues, and index design.

## Version Checks

- 7.1:
  - Attachments instruct the GPT to omit `IF NOT EXISTS`, `IF EXISTS`, native `JSON`, Temporary LOB checks, and 8.1 replication SSL forms unless the customer proves support in the exact build.
  - Table, partition, LOB, `LOCALUNIQUE`, direct key, and metadata guidance is consistent with sampled 7.1 sources.
- 7.3:
  - Attachments treat 7.3 as close to 7.1 for this DDL surface and avoid applying 8.1-only syntax by default.
  - Sampled 7.3 sources support the same LOB, partition, local index, direct key, and constraint metadata guidance.
- 8.1:
  - Attachments allow `IF NOT EXISTS` / `IF EXISTS` only as Altibase 8.1 verified source syntax.
  - Native `JSON`, Temporary LOB, `TEMPORARY_LOB_ENABLE`, `V$TEMPORARY_LOBS`, and JSON-plan property names are labeled as 8.1 material with appropriate cautions.

## Retrieval And GPT Answer Quality

- Strengths:
  - The high-risk DDL areas are easy to retrieve by heading: `Table Syntax`, `Index Syntax`, `Table Examples`, `Constraint Examples`, `Index Examples`, `Type Item: BLOB`, `Type Item: CLOB`, `Type Item: Temporary LOB`, `Type Item: JSON`, and `Index and Constraint Tuning`.
  - Literal object names, SQL keywords, properties, performance views, and meta table names are preserved.
  - Verification SQL is included close to the DDL examples, which should improve generated answer quality for operational checks.
- Risks:
  - Without a live Altibase smoke test, there is residual risk that an example has a minor execution-order or environment dependency, such as prerequisite schema/tablespace creation or object existence.
  - 8.1 JSON and Temporary LOB retrieval depends on source-normalized Korean/manual fallback summarized by the verification report.

## Required Follow-Up

- No required R04 follow-up.
- Optional later validation: run a live iSQL smoke test for representative 7.1/7.3/8.1 DDL examples if test servers become available.
