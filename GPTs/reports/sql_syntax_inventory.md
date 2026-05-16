# Altibase GPT SQL Syntax Inventory

Job: `J010`
Status: Active support artifact
Last updated: 2026-05-17

## Reconfirmed Requirement And Boundary

`J010` inventories Altibase SQL statement families and defines the BNF-like conversion
rules that later SQL jobs must use when converting syntax diagrams into customer-facing
attachment text.

This is a documentation-scope baseline. It does not attempt to complete every SQL
statement, clause, function, hint, or operator block in the customer-facing attachments.
Those item-level expansions are split across J011-J016, with J011 and J012 now
source-audited and the remaining SQL families continuing in J013-J016. PSM, Spatial,
tool, and
connector-specific syntax are handled by their later source-family jobs. No attachment
filename, upload boundary, or customer-facing 8.1 source label change was found.

The target customer attachments affected by this baseline are:

- `02_administration_operations.md`
- `03_sql_ddl_generation.md`
- `04_sql_dml_oracle_compatibility.md`
- `05_data_types_properties.md`
- `08_performance_tuning_monitoring.md`
- `09_replication_ha_cdc.md`
- `10_psm_stored_external_procedures.md`
- `15_migration_oracle_compatibility.md`
- `16_dblink_external_connectors.md`
- `18_security_ssl_tls.md`
- `19_spatial_nifi_tableau_misc.md`

Direct attachment remediation is deferred because the current job's accepted output is
the inventory, BNF conversion contract, and follow-on queue. Later jobs should use this
report together with `GPTs/reports/coverage_matrix.md`,
`GPTs/reports/gap_register.md`, and
`GPTs/reports/catalog_schema_extraction_rules.md`.

## Design Note

J010 adds this support report as the SQL counterpart to the property baseline created
by J004. The report groups syntax work by source family and later-job ownership so that
J011-J016 can add compact, searchable BNF blocks without duplicating source discovery or
mixing unrelated SQL areas.

The design choice is to treat source syntax diagrams as clause trees, not screenshots.
Later jobs should convert each statement into a small root production plus named clause
productions, then put prerequisites, destructive-operation cautions, examples, and
verification SQL in prose or SQL blocks outside the grammar. This keeps grammar
answerable while preventing giant opaque BNF blocks.

## Scoped Sources

Korean sources are authoritative when paired Korean and English sources differ. English
manuals are extraction aids for terminology and examples only when consistent with the
Korean source.

| Source family | Authoritative sources for this inventory | Extraction aids | Primary later jobs |
| --- | --- | --- | --- |
| `sql_reference` | `Manuals/Altibase_7.1/kor/SQL Reference.md`; `Manuals/Altibase_7.3/kor/SQL Reference.md`; `Manuals/Altibase_trunk/kor/SQL Reference.md` | Matching English SQL Reference manuals | J011-J016 |
| `administrator_operations` | Korean Administrator manuals plus Korean SQL Reference administrative SQL | Matching English manuals | J011, J016 |
| `replication_manual` | Korean Replication manuals plus Korean SQL Reference replication SQL | Matching English manuals | J016, J031-J033 |
| `log_analyzer` | Korean Log Analyzer User's Manuals | Matching English manuals | J016, J032 |
| `general_reference_1_datatypes_properties` | Korean General Reference 1 manuals for type/property syntax | Matching English manuals | J015, property follow-ups |
| `performance_tuning` | Korean Performance Tuning Guides and Korean SQL Reference hint sections | Matching English manuals | J013 |
| `migration_oracle` | Korean Migration Center and Adapter for Oracle manuals | Matching English manuals | J015, J039 |
| `dblink_hadoop_external_connectors` | Korean DB Link and connector manuals plus Korean SQL Reference DB Link SQL | Matching English manuals | J016, J038 |
| `spatial_nifi_tableau` | Korean Spatial SQL Reference manuals | Matching English manuals | J015, J039 |
| `stored_external_procedures` | Korean Stored Procedures and External Procedures manuals | Matching English manuals | J034 |

## Extraction Method

1. Use the Korean SQL Reference statement classification and statement chapters as the
   canonical SQL family list for Altibase 7.1, 7.3, and the Altibase 8.1 verified
   source.
2. Use matching English manuals for customer-facing English names only where they agree
   with the Korean source.
3. Use `GPTs/reports/image_inventory.md` to identify syntax-diagram density and target
   attachments, then audit the original source section before converting any diagram.
4. Preserve source classifications even when they differ from generic database
   expectations. For example, the selected SQL Reference tables list `GRANT` and
   `REVOKE` under the DDL list.
5. Treat 8.1-only syntax as 8.1-only unless the 7.1 or 7.3 Korean manuals prove the same
   clause. The `IF EXISTS` and `IF NOT EXISTS` clauses found in the Altibase 8.1
   verified SQL Reference are not broad 7.x claims.
6. Treat Korean-source-only 8.1 detail as usable after English normalization. The 8.1
   Korean SQL Reference has a `JSON` function section with `JSON_ARRAY`, `JSON_OBJECT`,
   `JSON_EXISTS`, `JSON_QUERY`, `JSON_VALUE`, and `JSON_VALID`; do not depend on the
   English extraction aid alone for that topic.

## Source Inventory Observations

- The 7.1, 7.3, and 8.1 SQL Reference manuals use the same high-level statement
  families: DDL, DML, and DCL, followed by functions, operators, conditions, and
  regular-expression material.
- `GPTs/reports/image_inventory.md` records SQL Reference syntax-diagram conversion
  demand as `425` diagrams for the 7.1 English SQL Reference, `425` for the 7.3 English
  SQL Reference, and `426` for the 8.1 verified English SQL Reference.
- The same inventory maps most SQL Reference syntax diagrams to
  `03_sql_ddl_generation.md` and `04_sql_dml_oracle_compatibility.md`; specialized
  syntax also routes to `05_data_types_properties.md`,
  `08_performance_tuning_monitoring.md`, `09_replication_ha_cdc.md`,
  `16_dblink_external_connectors.md`, and `19_spatial_nifi_tableau_misc.md`.
- The SQL Reference classification says DDL statements implicitly commit prior
  uncommitted DML in the session because DDL is executed as its own transaction. DML
  statements do not receive the same implicit-commit treatment when autocommit is off.
  Later SQL generation blocks must carry that operational caution where it affects
  rollback expectations.
- Existing attachments already contain some compact BNF blocks for database lifecycle,
  backup/recovery, directory/synonym/view/materialized-view DDL, replication SQL,
  property SQL, PSM, DML return clauses, and selected query features. J010 does not
  certify those as exhaustive; later jobs must source-audit and expand them by family.

## Statement Family Inventory

### J011 Baseline: Database And Recovery SQL

- Statement family: Database, tablespace, datafile, archive, backup, restore, and
  recovery.
- Source-backed statement or clause groups: `ALTER DATABASE`, `CREATE DATABASE`,
  `DROP DATABASE`, `ALTER TABLESPACE`, `CREATE DISK TABLESPACE`,
  `CREATE MEMORY TABLESPACE`, `CREATE VOLATILE TABLESPACE`,
  `CREATE TEMPORARY TABLESPACE`, `DROP TABLESPACE`, archive-log, backup,
  incremental backup, recover, restore, change-tracking, checkpoint, and datafile
  clauses.
- Primary attachment targets: `02_administration_operations.md`,
  `03_sql_ddl_generation.md`.
- Required conversion shape: Per-version BNF root plus clause blocks,
  operation mode/prerequisite notes, example SQL or command sequence, and validation
  SQL.
- J011 completion note: `GPTs/attachments/03_sql_ddl_generation.md` now contains
  source-audited BNF-like blocks for `CREATE DATABASE`, `DROP DATABASE`,
  `ALTER DATABASE`, database/datafile/checkpoint-image lifecycle clauses,
  archive-log mode, online backup, incremental backup, restore, recovery, backup-file
  management, change tracking, snapshot, 8.1 checkpoint scale, `CREATE`/`ALTER`/`DROP`
  tablespace, file and checkpoint-path clauses, and tablespace backup state clauses.
  `GPTs/attachments/02_administration_operations.md` now records the guarded
  `ALTER DATABASE RESTORE TABLESPACE tablespace_name [, ...]` operational note. The
  7.1, 7.3, and 8.1 SQL Reference restore/datafile/backup/recovery clause diagrams were
  checked against the original image files; the shared `restore_tablespace_clause`
  converts only to `TABLESPACE tablespace_name [, tablespace_name ...]`, and no
  `RECOVER TABLESPACE` syntax was introduced.

### J012 Baseline: Table And Queue SQL

- Statement family: Table, column, constraint, partition, LOB storage, and queue SQL.
- Source-backed statement or clause groups: `CREATE TABLE`, `ALTER TABLE`,
  `DROP TABLE`, `TRUNCATE TABLE`, `COMMENT`, `CONJOIN TABLE`, `DISJOIN TABLE`,
  `FLASHBACK TABLE`, `PURGE TABLE`, `LOCK TABLE`, `CREATE QUEUE`, `ALTER QUEUE`,
  `DROP QUEUE`, `ENQUEUE`, `DEQUEUE`, table property clauses, partition clauses,
  direct-key table clauses, and LOB storage clauses.
- Primary attachment targets: `03_sql_ddl_generation.md`,
  `04_sql_dml_oracle_compatibility.md`, `05_data_types_properties.md`.
- Required conversion shape: Searchable item blocks for object creation, change, and
  destruction, BNF for complex clauses, examples, rollback/destructive cautions, and
  dictionary validation SQL.
- J012 completion note: `GPTs/attachments/03_sql_ddl_generation.md` now contains
  source-audited BNF-like blocks and examples for `CREATE TABLE`, `DROP TABLE`,
  `ALTER TABLE`, column default/type/nullability changes, constraint add/modify/rename
  and drop forms, partition maintenance, LOB storage movement, table maintenance,
  recycle-bin table operations, `LOCK TABLE`, queue creation/alter/drop, and
  `ENQUEUE`/`DEQUEUE`. The update preserves 8.1-only idempotent table/queue clauses,
  7.1 range-default partition requirements, 7.3/8.1 default-less range add-partition
  behavior, queue `DELETE ON|OFF`, `NOWAIT` and wait-unit semantics, and
  `V$QUEUE_DELETE_OFF` validation. `GPTs/attachments/04_sql_dml_oracle_compatibility.md`
  carries the queue DML wait semantics, and `GPTs/attachments/05_data_types_properties.md`
  cross-references disk-table LOB storage DDL.

### J013 Baseline: Index, Hint, And Plan SQL

- Statement family: Index, statistics, hints, optimizer-facing SQL, and plan syntax.
- Source-backed statement or clause groups: `CREATE INDEX`, `ALTER INDEX`,
  `DROP INDEX`, direct-key index clauses, index partition clauses, hint syntax, hint
  list, table access hints, join-order hints, join-method hints, bucket-count hints,
  optimizer-mode hints, normal-form hints, push-predicate hints, and execution-plan
  related syntax.
- Primary attachment targets: `03_sql_ddl_generation.md`,
  `04_sql_dml_oracle_compatibility.md`, `08_performance_tuning_monitoring.md`.
- Required conversion shape: Hint family blocks with exact token spelling, argument
  BNF, risk/when-to-use notes, example SQL, and plan/check SQL cross-references.
- J013 completion note: `GPTs/attachments/08_performance_tuning_monitoring.md` now
  contains source-audited statistics procedure signatures, statistics verification SQL,
  full hint-family token coverage from the SQL Reference hint table, argument patterns,
  `ALTI_` hint alias rules, and plan/statistics invalidation guidance. J013 also adds
  `V$DBMS_STATS` and `V$LOCK_TABLE_STATS` object blocks in
  `GPTs/attachments/06_data_dictionary_performance_views.md` and sharpens index notes
  in `GPTs/attachments/03_sql_ddl_generation.md`. No direct J013 change was needed in
  `GPTs/attachments/04_sql_dml_oracle_compatibility.md`; DML hint placement is covered
  through the tuning attachment's `SELECT`/`INSERT`/`UPDATE`/`DELETE` hint syntax and
  cross-references.

### J014 Baseline: Privilege And Schema Object SQL

- Statement family: Users, privileges, roles, schema objects, jobs, and reusable
  object SQL.
- Source-backed statement or clause groups: `CREATE USER`, `ALTER USER`, `DROP USER`,
  `CREATE ROLE`, `DROP ROLE`, `GRANT`, `REVOKE`, `CREATE SEQUENCE`,
  `ALTER SEQUENCE`, `DROP SEQUENCE`, `CREATE SYNONYM`, `DROP SYNONYM`,
  `CREATE VIEW`, `ALTER VIEW`, `DROP VIEW`, `CREATE MATERIALIZED VIEW`,
  `ALTER MATERIALIZED VIEW`, `DROP MATERIALIZED VIEW`, `CREATE DIRECTORY`,
  `DROP DIRECTORY`, `CREATE JOB`, `ALTER JOB`, `DROP JOB`, `CREATE TRIGGER`,
  `ALTER TRIGGER`, and `DROP TRIGGER`.
- Primary attachment targets: `03_sql_ddl_generation.md`,
  `10_psm_stored_external_procedures.md`, `18_security_ssl_tls.md`.
- Required conversion shape: Object-type blocks with privileges, 8.1 idempotent
  clauses where source-backed, examples, cleanup syntax, and metadata validation SQL.
- J014 completion note: `GPTs/attachments/03_sql_ddl_generation.md` now contains
  source-audited BNF-like syntax, generation notes, examples, and verification SQL for
  user accounts, password policy clauses, roles, `GRANT`, `REVOKE`, full sequence
  lifecycle, directories, synonyms, views, materialized views, triggers, and scheduler
  jobs. `GPTs/attachments/06_data_dictionary_performance_views.md` now includes
  metadata cookbook queries and object blocks for `SYSTEM_.SYS_GRANT_SYSTEM_`,
  `SYSTEM_.SYS_GRANT_OBJECT_`, `SYSTEM_.SYS_USER_ROLES_`, `SYSTEM_.SYS_SYNONYMS_`,
  `SYSTEM_.SYS_DIRECTORIES_`, `SYSTEM_.SYS_MATERIALIZED_VIEWS_`,
  `SYSTEM_.SYS_TRIGGERS_`, trigger source/dependency tables, and `SYSTEM_.SYS_JOBS_`.
  The update preserves Korean-source precedence for 8.1-only idempotent clauses,
  directory file-system boundaries, synonym privilege/name-resolution behavior, view
  and materialized-view validation limits, trigger restrictions, replication-trigger
  separation, and job scheduler prerequisites.

### J015 Baseline: DML, Functions, And JSON SQL

- Statement family: DML, query expressions, functions, operators, JSON, conditions, and
  Oracle-difference SQL.
- Source-backed statement or clause groups: `SELECT`, `INSERT`, `UPDATE`, `DELETE`,
  `MERGE`, `MOVE`, set operators, `RETURN` or `RETURNING` clauses, aggregate
  functions, window functions, numeric functions, character functions, datetime
  functions, conversion functions, encryption functions, other functions, arithmetic
  operators, unary/binary operators, concatenation, `CAST`, logical and comparison
  conditions, regular expressions, and 8.1 Korean-source JSON functions.
- Primary attachment targets: `04_sql_dml_oracle_compatibility.md`,
  `05_data_types_properties.md`, `15_migration_oracle_compatibility.md`,
  `19_spatial_nifi_tableau_misc.md`.
- Required conversion shape: Function/operator item blocks plus BNF for options,
  concise Oracle-difference notes, examples, return-type/LOB restrictions, and
  error/property cross-references.
- J015 completion note: `GPTs/attachments/04_sql_dml_oracle_compatibility.md` now
  contains source-audited compact blocks for expression placement, arithmetic and date
  arithmetic, concatenation, `CAST`, logical/operator precedence, condition semantics,
  function family indexes, analytic/window placement, regular expression mode cautions,
  8.1 JSON path essentials, JSON DML examples, JSON function option grammar,
  `JSON_VALID`, `IS JSON`, and Oracle SQL/JSON difference checks. J015 also adds a JSON
  SQL cross-reference in `GPTs/attachments/05_data_types_properties.md` and a JSON SQL
  migration rewrite caution in `GPTs/attachments/15_migration_oracle_compatibility.md`.
  No direct J015 edit was needed in `GPTs/attachments/19_spatial_nifi_tableau_misc.md`;
  specialized Spatial function/operator extraction remains owned by J039.

### J016 Baseline: Replication, DB Link, And Control SQL

- Statement family: Replication, DB Link, system/session, audit, transaction, property
  SQL, and Log Analyzer SQL.
- Source-backed statement or clause groups: `CREATE REPLICATION`, `ALTER REPLICATION`,
  `DROP REPLICATION`, replication control forms, `CREATE DATABASE LINK`,
  `DROP DATABASE LINK`, `ALTER DATABASE LINKER`, `ALTER SYSTEM`, `ALTER SESSION`,
  `AUDIT`, `DELAUDIT`, `NOAUDIT`, `COMMIT`, `ROLLBACK`, `SAVEPOINT`,
  `SET TRANSACTION`, property SQL, Log Analyzer `FOR ANALYSIS`, and Log Analyzer
  `FOR ANALYSIS PROPAGATION` XLog Sender syntax.
- Primary attachment targets: `03_sql_ddl_generation.md`,
  `05_data_types_properties.md`, `09_replication_ha_cdc.md`,
  `16_dblink_external_connectors.md`, `18_security_ssl_tls.md`.
- Required conversion shape: Version-scoped BNF, topology/transport guardrails,
  property/view validation SQL, exact missing-input prompts, and clear separation of
  ordinary replication, replication SSL, and Log Analyzer forms.

### J034/J039 Baseline: Specialized SQL

- Statement family: PSM, external procedure, Spatial, and tool-adjacent SQL.
- Source-backed statement or clause groups: PSM procedure/function/package/trigger
  grammar, external procedure SQL, Spatial DDL/functions/operators, altiShapeLoader,
  and migration-related SQL examples.
- Primary attachment targets: `10_psm_stored_external_procedures.md`,
  `15_migration_oracle_compatibility.md`, `19_spatial_nifi_tableau_misc.md`.
- Required conversion shape: Use this report's notation rules, but leave item-level
  extraction to the specialized source-family jobs.

## BNF Conversion Rules For SQL Syntax Diagrams

Use these rules in addition to the shared schema in
`GPTs/reports/catalog_schema_extraction_rules.md`.

### Source And Version Rules

- Audit the Korean source section first. Use English text for extraction only when it
  agrees with the Korean source.
- Record version scope beside the statement or clause, not only in the surrounding
  section. Use `Altibase 8.1 verified source` for customer-facing 8.1 labels.
- Do not project 8.1 syntax such as `IF EXISTS`, `IF NOT EXISTS`, or JSON function
  options onto 7.1 or 7.3 unless the corresponding Korean 7.x manual proves it.
- When release notes or patch notes introduce a syntax boundary, include the exact
  version or patch caveat; otherwise ask for the installed version before generating a
  definitive patch-sensitive answer.

### Grammar Shape Rules

```text
statement_name ::=
  LITERAL_KEYWORD required_item [optional_clause]
  { alternative_a | alternative_b }
  repeated_item [, repeated_item ...]

named_clause ::=
  LITERAL_KEYWORD clause_argument [clause_option]
```

- Use one root production per statement family and separate named productions for
  complex clauses such as storage, partition, replication item, backup, restore,
  JSON-return, or hint arguments.
- Keep SQL keywords, object names, property names, view names, function names, command
  options, and error codes literal and case-preserved.
- Use lowercase placeholders such as `table_name`, `column_name`, `expr`,
  `file_path`, `host_name`, and `port_no`.
- Use `[ ... ]` only for optional syntax that the source diagram or text proves
  optional.
- Use `{ A | B }` for one required alternative and `[A | B]` only when the complete
  alternative group is optional.
- Use `item [, item ...]` for one or more comma-separated repetitions. Do not use
  ellipses when the separator or minimum count is source-sensitive.
- Expand nested alternatives when a compact form would hide a semantic difference. This
  is especially important for backup/recovery, replication transport, partitioning,
  `RETURN` or `RETURNING`, JSON null/error handling, and destructive `DROP`/`PURGE`
  syntax.

### Prose Around Grammar

- Put prerequisites, privileges, server mode, replication topology, archive-log mode,
  file-system preparation, and operational cautions outside the BNF block.
- Put destructive-operation and implicit-commit cautions immediately after the grammar
  for `DROP`, `PURGE`, `TRUNCATE`, `ALTER DATABASE`, backup/recovery, and DDL that can
  change replicated objects.
- Add a minimal example with safe placeholder names whenever a statement is intended
  for generation.
- Add dictionary or performance-view validation SQL when a source-backed check exists.
  Prefer portable checks through `V$TABLE`, `V$ALLCOLUMN`, `SYSTEM_.SYS_TABLES_`,
  `SYSTEM_.SYS_COLUMNS_`, object-specific dictionary tables, and replication/runtime
  views where applicable.
- For exact patch level, environment, log excerpt, object definition, or unsupported
  compatibility uncertainty, add an answer pattern that requests the missing input and
  gives the safest next check instead of inventing a final answer.

## Gap And Handoff Notes

- `GAP-J002-003` was closed by J011 for the source-audited tablespace restore/recovery
  grammar. Keep the guarded wording: generate `RESTORE TABLESPACE` only from the
  audited restore clause and do not invent `RECOVER TABLESPACE`.
- `GAP-J002-004` remains the anchor for direct-key supported data type and partial-key
  behavior until J012/J013 expand table and index direct-key blocks.
- `GAP-J002-005` was closed by J015 for the selected-source JSON SQL and function
  option grammar scope. Keep the remaining guardrail that Oracle SQL/JSON constructs
  not listed in the Altibase SQL Reference require manual redesign or exact
  target-version proof.
- `GAP-J002-018` remains the high-risk visual audit anchor. This J010 inventory narrows
  the SQL syntax portion of that audit but does not close it.
- `GAP-J010-001` in `GPTs/reports/gap_register.md` tracks the remaining SQL syntax
  conversion queue created by this report.

## Validation Notes

J010 validation should confirm:

- Exactly 20 upload Markdown attachments still exist under `GPTs/attachments/`, excluding
  `README.md`.
- This support report is referenced from the source inventory, coverage matrix, and gap
  register.
- Customer-facing attachments do not expose repository-local source paths, internal
  source-family IDs, or internal branch/build labels as a result of this job.
- Later SQL jobs have a concrete statement-family queue and BNF conversion contract.
