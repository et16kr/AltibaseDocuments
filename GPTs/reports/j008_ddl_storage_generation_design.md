# J008 DDL and Storage SQL Generation Design Note

## Scope

J008 strengthens `GPTs/attachments/03_sql_ddl_generation.md` for generated SQL answers covering tablespaces, datafiles, tables, partitions, indexes, constraints, LOB storage, and destructive DDL. Related files `02_administration_operations.md` and `05_data_types_properties.md` already contain deeper operational and property runbooks, so this job keeps the main edits in the DDL-generation attachment and uses cross-references rather than duplicating long procedures.

## Evidence Used

- `evals/altibase_answerability/reports/full_benchmark/failure_root_cause_analysis_20260517.md`
- `GPTs/reports/answerability_failure_remediation_inventory_20260517.md`
- `GPTs/reports/exact_token_gap_inventory_20260517.md`
- `evals/altibase_answerability/questions/sql_ddl_dml_datatypes.jsonl`
- Altibase 8.1 Korean SQL Reference and General Reference source sections cited by the failed SQL questions.

## Documentation Structure Decision

The main failure pattern was not a missing long-form manual rewrite. The attachment already had broad syntax, but exact grammar tokens were split across optional syntax or examples, and answers sometimes compressed away safety caveats. The remediation therefore adds compact exact-token anchors near `Compact Syntax Patterns`, then reinforces the relevant local syntax blocks:

- tablespace/datafile generation blocks for `CREATE DISK TABLESPACE`, `CREATE VOLATILE TABLESPACE`, `AUTOEXTEND ON`, `MAXSIZE UNLIMITED`, `REUSE`, `CHECKPOINT PATH`, and `SPLIT EACH`;
- table and partition blocks for `GLOBAL TEMPORARY`, `ON COMMIT` behavior, `ALTER TABLE ADD PARTITION`, default-less range partition metadata, `TIMESTAMP`, `CREATE TABLE AS SELECT`, `table_compression_clause`, and `LOB(column_name)`;
- index blocks for `PARALLEL`, `INDEX_BUILD_THREAD_COUNT`, `NOLOGGING`, `FORCE`, `NOFORCE`, `V$DISK_BTREE_HEADER`, and LOB/index restrictions;
- destructive DDL guardrails for `DROP TABLESPACE`, `INCLUDING CONTENTS`, `AND DATAFILES`, `CASCADE CONSTRAINTS`, and system tablespaces.

## Source-Safety Notes

The volatile tablespace block preserves both source-backed limits: the SQL Reference explains `MAXSIZE UNLIMITED` growth against the combined memory and volatile total reaching `MEM_MAX_DB_SIZE`, while the General Reference separately defines `VOLATILE_MAX_DB_SIZE` as the maximum total volatile tablespace size. Generated answers should check both before sizing volatile storage.

The table/index numeric limit note preserves a source nuance: the `ALTER TABLE` caution lists `64` for table indexes and primary/unique constraints, while the `CREATE TABLE` caution also lists a combined `1024` count. Answers whose main point is the numeric limit should quote the target SQL Reference section and installed version.
