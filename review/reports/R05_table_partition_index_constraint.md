# R05 DDL generation: tables, partitions, indexes, and constraints

Date: 2026-05-16
Reviewer: Codex
Verdict: Pass

## Scope

- Attachments:
  - `GPTs/attachments/03_sql_ddl_generation.md`
  - `GPTs/attachments/08_performance_tuning_monitoring.md`
- Supporting reports:
  - `GPTs/reports/sql_generation_test_results.md`
- Source manuals sampled:
  - `Manuals/Altibase_7.1/kor/SQL Reference.md`
  - `Manuals/Altibase_7.3/kor/SQL Reference.md`
  - `Manuals/Altibase_trunk/kor/SQL Reference.md`
  - `Manuals/Altibase_7.1/kor/Performance Tuning Guide.md`
  - `Manuals/Altibase_7.3/kor/Performance Tuning Guide.md`
  - `Manuals/Altibase_trunk/kor/Performance Tuning Guide.md`
  - `Manuals/Altibase_7.1/kor/Administrator's Manual.md`
  - `Manuals/Altibase_7.3/kor/Administrator's Manual.md`
  - `Manuals/Altibase_trunk/kor/Administrator's Manual.md`
  - `Manuals/Altibase_7.1/kor/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`

## Commands Run

```bash
bash review/scripts/run_review_remediation_cycle.sh status
rg -n $'\t(Reviewing|Remediating|ReReviewing|Fail)$' review/review_remediation_cycle_status.tsv
git status --short
git diff -- GPTs/attachments/03_sql_ddl_generation.md
git diff -- GPTs/attachments/08_performance_tuning_monitoring.md
git diff -- GPTs/reports/sql_generation_test_results.md
git diff -- review/review_remediation_cycle_status.tsv review/review_stage_status.tsv
sed -n '1,240p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,220p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,260p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
rg -n "^(#|##|###)|CREATE TABLE|ALTER TABLE|DROP TABLE|PARTITION|CREATE INDEX|INDEX|DIRECT KEY|DIRECTKEY|CONSTRAINT|PRIMARY KEY|FOREIGN KEY|CHECK|UNIQUE|Verification|SYS_TABLES|SYS_INDICES|SYS_CONSTRAINT|SYS_INDEX|LOCALUNIQUE|ROW MOVEMENT|IF NOT EXISTS|IF EXISTS|MAXROWS|CTAS" GPTs/attachments/03_sql_ddl_generation.md
rg -n "^(#|##|###)|CREATE INDEX|INDEX|DIRECT KEY|DIRECTKEY|PARTITION|constraint|PRIMARY KEY|UNIQUE|FOREIGN KEY|CHECK|EXPLAIN|plan|optimizer|verification|SYS_|LOCALUNIQUE|function-based" GPTs/attachments/08_performance_tuning_monitoring.md
nl -ba GPTs/attachments/03_sql_ddl_generation.md | sed -n '223,370p'
nl -ba GPTs/attachments/03_sql_ddl_generation.md | sed -n '424,481p'
nl -ba GPTs/attachments/03_sql_ddl_generation.md | sed -n '1235,1488p'
nl -ba GPTs/attachments/03_sql_ddl_generation.md | sed -n '1497,1800p'
nl -ba GPTs/attachments/08_performance_tuning_monitoring.md | sed -n '931,1148p'
sed -n '1,260p' GPTs/reports/sql_generation_test_results.md
rg -n "ADD PARTITION|COALESCE PARTITION|SPLIT PARTITION|DEFAULT.*파티션|VALUES DEFAULT|파티션드 테이블|PARTITION BY RANGE|RANGE_USING_HASH|LOCALUNIQUE|DIRECTKEY|INDEXTYPE|CREATE INDEX|FOREIGN KEY|CHECK 제약|CTAS|AS SELECT|MAXROWS|IF NOT EXISTS|IF EXISTS" Manuals/Altibase_7.1/kor/SQL\ Reference.md Manuals/Altibase_7.3/kor/SQL\ Reference.md Manuals/Altibase_trunk/kor/SQL\ Reference.md
rg -n "로컬 인덱스|글로벌.*인덱스|논파티션드 인덱스|파티션드 메모리|메모리 파티션드|LOCALUNIQUE|DIRECTKEY|함수 기반|QUERY_REWRITE_ENABLE|인덱스" Manuals/Altibase_7.1/kor/Administrator\'s\ Manual.md Manuals/Altibase_7.3/kor/Administrator\'s\ Manual.md Manuals/Altibase_trunk/kor/Administrator\'s\ Manual.md Manuals/Altibase_7.1/kor/Performance\ Tuning\ Guide.md Manuals/Altibase_7.3/kor/Performance\ Tuning\ Guide.md Manuals/Altibase_trunk/kor/Performance\ Tuning\ Guide.md
rg -n "SYS_CONSTRAINTS_|SYS_CONSTRAINT_COLUMNS_|REFERENCED_INDEX|REFERENCED_TABLE|DELETE_RULE|SYS_INDICES_|SYS_INDEX_COLUMNS_|SYS_PART_INDICES_|SYS_INDEX_PARTITIONS_|SYS_TABLE_PARTITIONS_|V\$DISK_BTREE_HEADER" Manuals/Altibase_7.1/kor/General*Reference-2* Manuals/Altibase_7.3/kor/General*Reference-2* Manuals/Altibase_trunk/kor/General*Reference-2*
rg -n "IF NOT EXISTS|IF EXISTS" Manuals/Altibase_7.1/kor/SQL\ Reference.md Manuals/Altibase_7.3/kor/SQL\ Reference.md Manuals/Altibase_trunk/kor/SQL\ Reference.md
rg -n "GLOBAL TEMPORARY|임시 테이블|temporary_attributes_clause|ON COMMIT DELETE ROWS|ON COMMIT PRESERVE ROWS|분산 트랜잭션|파티션.*임시|임시.*파티션" Manuals/Altibase_7.1/kor/SQL\ Reference.md Manuals/Altibase_7.3/kor/SQL\ Reference.md Manuals/Altibase_trunk/kor/SQL\ Reference.md
rg -n "ALTER TABLESPACE|LOB \(|ALTER TABLE .*LOB|partition_lob|LOB.*TABLESPACE|테이블스페이스.*LOB|LOB 칼럼" Manuals/Altibase_7.1/kor/SQL\ Reference.md Manuals/Altibase_7.3/kor/SQL\ Reference.md Manuals/Altibase_trunk/kor/SQL\ Reference.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' | wc -l
rg -n "trunk|C:/|file://" GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/08_performance_tuning_monitoring.md
git diff --check
bash review/scripts/run_review_stage.sh validate
git status --short
```

## Findings

No actionable `Blocker`, `High`, `Medium`, or `Low` findings remain in the R05 scope.

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Note | `GPTs/attachments/03_sql_ddl_generation.md`; `GPTs/attachments/08_performance_tuning_monitoring.md` | - | The previously reported R05 issues were rechecked: range partition default handling is now version-split, range `ADD PARTITION` is limited to 7.3/8.1 default-less range tables, foreign-key count/type matching is visible, and column-level `CHECK` plus CTAS `CHECK` restrictions are visible. | No further R05 remediation is required. Keep the current version-scoped wording during later broad cleanup. |

## Source Checks

- Claims checked:
  - `CREATE TABLE`, `CREATE TABLE IF NOT EXISTS`, `DROP TABLE IF EXISTS`, memory/disk/volatile/temporary table storage, `MAXROWS`, temporary table restrictions, range/list/hash/range-using-hash partitioning, `ENABLE ROW MOVEMENT`, partition maintenance, table movement, CTAS restrictions, primary/unique/local unique/foreign key/check constraints, direct key constraints and indexes, `CREATE INDEX`, `CREATE INDEX IF NOT EXISTS`, `DROP INDEX IF EXISTS`, local/global index boundaries, local B+tree restriction, function-based indexes, direct key indexes, `ALTER INDEX`, `NOLOGGING`, and verification SQL.
- Source coverage:
  - Korean SQL Reference manuals support the current 8.1-only table/index `IF NOT EXISTS` and `IF EXISTS` boundaries; no matching 7.1/7.3 Korean hits were found for those clauses.
  - Korean 7.1 SQL Reference requires range default partitions; Korean 7.3 and 8.1-source SQL References allow default-less range partitions and restrict range `ADD PARTITION` to default-less range tables. The attachment now preserves that split.
  - Korean SQL Reference manuals support list default partition requirements, hash/list/range key-count restrictions, row movement default behavior, `MAXROWS` not being usable with partitioned tables, temporary-table storage and foreign-key restrictions, and CTAS limitations.
  - Korean SQL Reference manuals support the visible constraint rules: one primary key, primary-key columns non-null, unique/primary duplicate-key restrictions, foreign keys referencing primary or unique keys, foreign-key count/type matching, `ON DELETE SET NULL` requiring nullable child columns, column-level `CHECK` scope, and `CHECK` expression restrictions.
  - Korean SQL Reference and Administrator manuals support the index-family guidance: local partitioned indexes and global non-partitioned indexes are supported; global partitioned indexes are not; partitioned memory tables cannot use global non-partitioned indexes; local indexes are B+tree only.
  - Korean SQL Reference manuals support function-based index requirements, `QUERY_REWRITE_ENABLE = 1`, direct key restrictions, direct key default `MAXSIZE`, composite direct key first-column behavior, direct key unsupported disk/compressed/encrypted boundaries, index build `PARALLEL` range, and `NOLOGGING` consistency cautions.
  - Korean General Reference data dictionary manuals support the sampled verification metadata for `SYSTEM_.SYS_TABLES_`, `SYSTEM_.SYS_COLUMNS_`, `SYSTEM_.SYS_CONSTRAINTS_`, `SYSTEM_.SYS_CONSTRAINT_COLUMNS_`, `SYSTEM_.SYS_INDICES_`, `SYSTEM_.SYS_INDEX_COLUMNS_`, `SYSTEM_.SYS_PART_INDICES_`, `SYSTEM_.SYS_INDEX_PARTITIONS_`, `SYSTEM_.SYS_TABLE_PARTITIONS_`, `V$MEMTBL_INFO`, and `V$DISK_BTREE_HEADER`.
  - Korean Performance Tuning Guides support the index access-method, composite-index, plan-node, statistics, and retest workflow guidance sampled in `08_performance_tuning_monitoring.md`.
- Korean/English source conflicts:
  - No Korean/English conflict was needed to decide this stage. Korean sources were used as the technical basis.
- Source gaps:
  - No live Altibase server was available, so SQL executability was checked against manuals and data dictionary definitions rather than runtime execution.
  - Direct key supported-type details are summarized rather than exhaustively tabulated in the attachments; this is acceptable for R05 because unsupported full-key and partial-key behavior is explicitly visible.

## Oracle-Overlap Decision

- Correctly compressed:
  - The scoped content focuses on Altibase-specific DDL, storage, partitioning, constraints, indexes, direct key behavior, metadata checks, and tuning workflow. Ordinary Oracle-overlapping SQL remains compressed.
- Too much generic Oracle material:
  - None found in the R05 scope.
- Missing Altibase-specific difference:
  - None actionable found. The important Altibase-specific restrictions sampled for R05 are visible.

## Version Checks

- 7.1:
  - Table, partition, constraint, direct key, index, and verification guidance matches the sampled 7.1 Korean sources.
  - Range partitioning keeps the 7.1 default-partition requirement.
  - `IF NOT EXISTS`, `IF EXISTS`, native `JSON`, Temporary LOB, and replication SSL are not applied as general 7.1 syntax.
- 7.3:
  - The attachment now allows default-less range partitioning and range `ADD PARTITION` only where the 7.3 Korean SQL Reference supports it.
  - List partitioning still requires a `DEFAULT` partition; hash `ADD PARTITION` and `COALESCE PARTITION` remain scoped to hash partitioning.
  - `IF NOT EXISTS` and `IF EXISTS` remain excluded unless an exact later target patch is explicitly verified.
- 8.1:
  - 8.1 table/index idempotent syntax is limited to Altibase 8.1 verified source guidance.
  - The same default-less range partition and range `ADD PARTITION` behavior found in the 8.1-source Korean SQL Reference is reflected.
  - Native `JSON` is marked as 8.1-only in this scope and kept out of 7.1/7.3 examples.

## Retrieval And GPT Answer Quality

- Strengths:
  - `03_sql_ddl_generation.md` has dense, retrievable blocks for table syntax, storage type selection, partitioning, constraints, indexes, direct key indexes, and verification SQL.
  - `08_performance_tuning_monitoring.md` connects index and constraint changes to metadata checks, execution-plan checks, statistics, and retesting, reducing the chance that the GPT recommends DDL without evidence.
  - Literal SQL keywords, object names, property names, system table names, and version labels are preserved.
- Risks:
  - Runtime validation remains unperformed; manual-backed SQL can still fail in a customer environment because of object existence, privileges, exact patch level, tablespace state, replication state, or data already violating a new constraint.
  - Direct key supported data type sizing is intentionally summarized. For precise direct key sizing, the GPT should still check the source table or ask for the target column type and width before producing final DDL.

## Required Follow-Up

- No R05 remediation is required before moving to the next stage.
- During later final-readiness stages, keep the current version-specific partition wording and avoid re-compressing it into a single cross-version rule.
