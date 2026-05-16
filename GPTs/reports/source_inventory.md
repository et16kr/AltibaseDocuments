# Altibase GPTs Source Inventory

Job: `JOB-010`
Phase: P1 Inventory
Status: Complete

This report inventories source availability for the 20 GPT attachment files. Korean Altibase manuals are the authoritative latest manual source. English manuals can be used for convenient extraction and English wording, but when English and Korean manuals differ, the Korean manual is the source of truth and English-facing artifacts should be updated or normalized from the Korean source.

For Altibase 8.1, the internally verified source set is the current 8.1 verified manual tree plus the 8.1 release notes. Customer-facing attachments must label this as "Altibase 8.1 verified source" or equivalent wording, not by the internal directory name.

## J001 Rebuild Source Scope Addendum

J001 confirms that this source inventory remains the support report for source roots and
attachment-to-source mapping until the J002 coverage matrix and gap register are created.
The current job does not change the 20 attachment filenames and does not require direct
customer-facing attachment edits; it records the source-backed reason here because J001
only finalizes requirements, source corpus scope, and success criteria.

The scoped source corpus for the encyclopedia rebuild is:

- Altibase 7.1 manuals: Korean manuals are authoritative; English manuals are extraction
  aids when consistent.
- Altibase 7.3 manuals: Korean manuals are authoritative; English manuals are extraction
  aids when consistent.
- Altibase 8.1 verified source manuals: Korean manuals are authoritative for detailed
  manual behavior, checked against the 8.1 release notes before customer-facing use.
- Release notes: Korean release notes are authoritative when release-note content differs;
  English release notes are extraction aids.
- Patch notes: supported 7.1 and 7.3 patch notes are allowed for patch-level behavior;
  older 6.x patch notes are outside default answer scope unless a later job records a
  source-backed migration or historical reason.
- Tool manuals, technical documents, and third-party guides: Korean sources are
  authoritative when paired, Korean-only, or more specific; English sources are extraction
  aids.
- Supporting reports under `GPTs/reports/`: internal traceability and validation sources
  only, not customer-facing source labels.

No new manual/source-backed coverage gap was discovered during J001. Known prior source
detail risks, such as Korean-source-only 8.1 JSON, Temporary LOB, replication SSL,
JSON-related errors, and `SQLFreeLob2` detail, remain governed by the existing
English/Korean parity report and must be tracked in the J002 coverage matrix or later
job-specific gap register entries.

## J002 Coverage Matrix And Gap Register Addendum

J002 creates the coverage matrix and primary post-J002 gap register promised by J001:

- `GPTs/reports/coverage_matrix.md` maps selected source families to the 20 upload
  attachments, records the required coverage shape for each family, and assigns later
  job handoff areas.
- `GPTs/reports/gap_register.md` records item-level gaps, residual source limitations,
  and verification limits discovered from the selected source reports and review-cycle
  reports.

This source inventory remains the source-root and attachment-to-source path inventory.
After J002, use `GPTs/reports/gap_register.md` as the primary tracking artifact when a
later job discovers, splits, closes, or accepts an item-level source-backed gap.

J002 did not change the 20 customer-facing attachment filenames and did not require
direct attachment edits. The source-backed reason is that the existing attachment
boundary still maps all selected source families to an upload unit, while the newly
created matrix/register provide the missing concrete work queue for item-level coverage
expansion.

## J003 Catalog Schema And Extraction Rules Addendum

J003 adds `GPTs/reports/catalog_schema_extraction_rules.md` as the reusable schema and
Korean-first extraction contract for later rebuild jobs. Use it with the source
inventory, coverage matrix, and gap register when converting source-backed material into
customer-facing item blocks, BNF-like syntax, runbook steps, examples, cross-references,
and validation notes.

J003 does not change the 20 customer-facing attachment filenames and does not require
direct attachment edits. The source-backed reason is that the existing attachment
boundary still maps every selected source family to an upload unit; the missing piece
for this job is a shared extraction and item-block structure for later item-level work.

No new manual/source-backed coverage gap was discovered during J003. Existing post-J002
gaps remain tracked in `GPTs/reports/gap_register.md`.

## J004 Property Inventory Addendum

J004 creates `GPTs/reports/property_inventory.md` as the canonical property-name and
version-availability baseline for the `general_reference_1_datatypes_properties` source
family. The inventory is generated from Korean General Reference 1 detailed property
headings for Altibase 7.1, Altibase 7.3, and the Altibase 8.1 verified source, with the
matching English manuals used only as extraction aids.

J004 updates `GPTs/attachments/05_data_types_properties.md` with a compact
customer-facing property-name availability index. The index records source-backed name
presence by version family, but it does not claim complete per-property defaults,
ranges, units, dynamic-change support, or restart behavior. Those details remain split
work for J005-J009 and are tracked in `GPTs/reports/gap_register.md` as
`GAP-J004-001`.

## J010 SQL Syntax Inventory Addendum

J010 creates `GPTs/reports/sql_syntax_inventory.md` as the SQL statement-family and
BNF-like syntax conversion baseline for the `sql_reference` source family and adjacent
administrator, replication, Log Analyzer, DB Link, migration, Spatial, and PSM syntax
families. The inventory is generated from the Korean SQL Reference statement
classification and statement chapters for Altibase 7.1, Altibase 7.3, and the Altibase
8.1 verified source, with matching English manuals used only as extraction aids when
consistent.

J010 does not change the 20 customer-facing attachment filenames and does not directly
rewrite the SQL attachments. The source-backed reason is that this job defines the
shared SQL conversion queue and BNF rules. J011 has since completed the database,
tablespace, datafile, archive, backup, restore, and recovery SQL family; J012 has
since completed the table, column, constraint, partition, LOB storage, and queue SQL
family. Remaining item-level SQL expansion continues across J013-J016 and later
specialized jobs. The
remaining SQL syntax conversion queue is tracked in `GPTs/reports/gap_register.md` as
`GAP-J010-001`.

## J011 Database, Tablespace, Datafile, Backup, Restore, And Recovery SQL Addendum

J011 uses the `sql_reference` and `administrator_operations` source families for
Altibase 7.1, Altibase 7.3, and the Altibase 8.1 verified source. Korean SQL Reference
and Administrator manuals remain authoritative; matching English manuals were used only
for English extraction when consistent. The Altibase 8.1 `CHECKPOINT SCALE` syntax was
checked against the Altibase 8.1 verified SQL Reference, Korean Administrator manual
checkpoint-scale section, and Korean 8.1 release note support statement.

J011 updates `GPTs/attachments/03_sql_ddl_generation.md` with source-audited compact
BNF and examples for database creation/drop, `ALTER DATABASE`, tablespace creation,
alter/drop, datafile/tempfile clauses, archive-log mode, online backup, incremental
backup, restore, recovery, backup-file management, change tracking, snapshot, and 8.1
checkpoint scale. J011 also updates `GPTs/attachments/02_administration_operations.md`
with the guarded `RESTORE TABLESPACE` operational note and closes
`GAP-J002-003` as a trace entry in `GPTs/reports/gap_register.md`.

## J012 Table, Column, Constraint, Partition, LOB Storage, And Queue SQL Addendum

J012 uses the `sql_reference`, `general_reference_1_datatypes_properties`, and
`general_reference_2_dictionary_views` source families for Altibase 7.1, Altibase 7.3,
and the Altibase 8.1 verified source. Korean SQL Reference manuals remain authoritative
for table, column, constraint, partition, LOB storage, queue, and table-maintenance
syntax; matching English manuals were used only for English extraction when consistent.
Korean General Reference 2 manuals were used for `V$QUEUE_DELETE_OFF` verification
because the queue `DELETE OFF` state is exposed through that performance view.

J012 updates `GPTs/attachments/03_sql_ddl_generation.md` with source-audited compact
BNF and examples for `CREATE TABLE`, `DROP TABLE`, `ALTER TABLE` column/default/type
changes, constraint add/modify/rename/drop forms, partition maintenance, LOB storage
movement, table maintenance, `LOCK TABLE`, `CREATE QUEUE`, `ALTER QUEUE`, `DROP QUEUE`,
`ENQUEUE`, and `DEQUEUE`. It preserves the 7.1 default-range-partition boundary, the
7.3/8.1 default-less range `ADD PARTITION` boundary, and the 8.1-only
`IF NOT EXISTS`/`IF EXISTS` table and queue clauses. It also updates
`GPTs/attachments/04_sql_dml_oracle_compatibility.md` for queue DML wait semantics and
`GPTs/attachments/05_data_types_properties.md` for LOB DDL cross-reference coverage.

## J013 Index, Statistics, Hint, And Plan SQL Addendum

J013 uses the `sql_reference`, `performance_tuning`,
`stored_external_procedures`, and `general_reference_2_dictionary_views` source
families for Altibase 7.1, Altibase 7.3, and the Altibase 8.1 verified source. Korean
manuals remain authoritative for index syntax, optimizer statistics, hints, execution
plans, and dictionary/performance view columns; matching English manuals were used only
for English extraction when consistent.

J013 updates `GPTs/attachments/08_performance_tuning_monitoring.md` with exact
statistics procedure signatures, `DBMS_STATS` package-specific index-stat helpers,
statistics verification SQL, full hint-family token coverage, hint argument patterns,
the `ALTI_` hint alias rule, and plan/statistics invalidation guidance. It updates
`GPTs/attachments/06_data_dictionary_performance_views.md` with object blocks for
`V$DBMS_STATS` and `V$LOCK_TABLE_STATS`, and
`GPTs/attachments/03_sql_ddl_generation.md` with sharper index-generation notes for
function-based index restrictions, `ALTER INDEX` storage caveats, and prefixed versus
non-prefixed partitioned indexes. No direct change was required in
`GPTs/attachments/04_sql_dml_oracle_compatibility.md`; J013 DML hint placement is
covered by the tuning attachment's `SELECT`/`INSERT`/`UPDATE`/`DELETE` hint syntax.

Scoped source paths checked for J013:

- `Manuals/Altibase_7.1/kor/SQL Reference.md`
- `Manuals/Altibase_7.3/kor/SQL Reference.md`
- `Manuals/Altibase_trunk/kor/SQL Reference.md`
- `Manuals/Altibase_7.1/kor/Performance Tuning Guide.md`
- `Manuals/Altibase_7.3/kor/Performance Tuning Guide.md`
- `Manuals/Altibase_trunk/kor/Performance Tuning Guide.md`
- `Manuals/Altibase_7.1/kor/Stored Procedures Manual.md`
- `Manuals/Altibase_7.3/kor/Stored Procedures Manual.md`
- `Manuals/Altibase_trunk/kor/Stored Procedures Manual.md`
- `Manuals/Altibase_7.1/kor/General Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`

No new source family was added. The shared SQL syntax conversion queue remains open for
J014-J016 and later specialized SQL families.

## J014 Users, Privileges, Roles, And Schema Object SQL Addendum

J014 uses the `sql_reference`, `administrator_operations`,
`general_reference_2_dictionary_views`, `stored_external_procedures`, and
`security_ssl_tls` source families for Altibase 7.1, Altibase 7.3, and the Altibase
8.1 verified source. Korean SQL Reference and General Reference 2 manuals remain
authoritative for user, privilege, role, sequence, synonym, view, materialized view,
directory, trigger, and job SQL plus metadata validation; matching English manuals were
used only for customer-facing terminology when consistent.

J014 updates `GPTs/attachments/03_sql_ddl_generation.md` with source-audited compact
syntax and examples for user/role/grant/revoke policy, full sequence lifecycle,
directory, synonym, view, materialized view, trigger, and job SQL. It adds source-backed
cautions for 8.1-only idempotent clauses, directory file-system boundaries, synonym
privilege/name-resolution behavior, view `FORCE` validation, materialized-view refresh
limits, trigger body restrictions, replication-trigger separation, LOB-trigger cautions,
and scheduler-job prerequisites. J014 also updates
`GPTs/attachments/06_data_dictionary_performance_views.md` with metadata checks and
object blocks for schema-object validation, and narrows `GAP-J010-001` to the remaining
J015-J016 SQL families plus later specialized SQL work.

Scoped source paths checked for J014:

- `Manuals/Altibase_7.1/kor/SQL Reference.md`
- `Manuals/Altibase_7.3/kor/SQL Reference.md`
- `Manuals/Altibase_trunk/kor/SQL Reference.md`
- `Manuals/Altibase_7.1/eng/SQL Reference.md`
- `Manuals/Altibase_7.3/eng/SQL Reference.md`
- `Manuals/Altibase_trunk/eng/SQL Reference.md`
- `Manuals/Altibase_7.1/kor/General Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_7.1/eng/General Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_7.3/eng/General Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_trunk/eng/General Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_7.1/kor/Stored Procedures Manual.md`
- `Manuals/Altibase_7.3/kor/Stored Procedures Manual.md`
- `Manuals/Altibase_trunk/kor/Stored Procedures Manual.md`

No new manual/source-backed gap was discovered during J014. The shared SQL syntax
conversion queue remains open for J015-J016 and later specialized SQL families.

## J015 DML, Functions, Expressions, And JSON SQL Addendum

J015 uses the `sql_reference`, `general_reference_1_datatypes_properties`, and
`migration_oracle` source families for Altibase 7.1, Altibase 7.3, and the Altibase
8.1 verified source. Korean SQL Reference and General Reference 1 manuals remain
authoritative for DML, conditions, expression operators, function families, native
`JSON`, JSON path, Temporary LOB prerequisites, and 8.1 JSON SQL grammar. Matching
English manuals were used only for customer-facing terminology when consistent.
Migration Center release notes and manuals were used for Oracle JSON migration mapping.

J015 updates `GPTs/attachments/04_sql_dml_oracle_compatibility.md` with expanded
expression/operator guidance, condition semantics, function family indexes, function
placement cautions, 8.1 JSON path and function option grammar, JSON DML examples, and
Oracle SQL/JSON difference checks. It updates
`GPTs/attachments/05_data_types_properties.md` with a JSON SQL cross-reference and
`GPTs/attachments/15_migration_oracle_compatibility.md` with JSON SQL rewrite and
Temporary LOB migration cautions. No attachment boundary or customer-facing source-label
change was needed.

Scoped source paths checked for J015:

- `Manuals/Altibase_7.1/kor/SQL Reference.md`
- `Manuals/Altibase_7.3/kor/SQL Reference.md`
- `Manuals/Altibase_trunk/kor/SQL Reference.md`
- `Manuals/Altibase_7.1/eng/SQL Reference.md`
- `Manuals/Altibase_7.3/eng/SQL Reference.md`
- `Manuals/Altibase_trunk/eng/SQL Reference.md`
- `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
- `Manuals/Altibase_trunk/eng/General Reference-1.Data Types & Altibase Properties.md`
- `Manuals/Tools/Altibase_release/kor/Migration Center User's Manual.md`
- `Manuals/Tools/Altibase_release/eng/Migration Center User's Manual.md`
- `Manuals/Tools/Altibase_trunk/kor/Migration Center User's Manual.md`
- `Manuals/Tools/Altibase_trunk/eng/Migration Center User's Manual.md`
- `ReleaseNotes/kor/Altibase_Migration_Center_7_16_Release_Notes.md`
- `ReleaseNotes/eng/Altibase_Migration_Center_7_16_Release_Notes.md`

No new manual/source-backed gap was discovered during J015. The shared SQL syntax
conversion queue remains open for J016 and later specialized SQL families.

## J017 Dictionary View Inventory Baseline Addendum

J017 uses the `general_reference_2_dictionary_views`, `performance_tuning`,
`replication_manual`, and release-note source families for Altibase 7.1, Altibase 7.3,
and the Altibase 8.1 verified source. Korean General Reference 2 manuals remain
authoritative for meta table and performance view names, grouping, version availability,
and view descriptions; matching English manuals were used only for customer-facing
terminology when consistent.

J017 adds `GPTs/reports/dictionary_view_inventory.md` as the source-backed name,
version, and group baseline for later J018-J021 view expansion. It updates
`GPTs/attachments/06_data_dictionary_performance_views.md` with compact customer-facing
inventory groups and portable existence checks using `V$TABLE`, `V$ALLCOLUMN`,
`SYSTEM_.SYS_TABLES_`, and `SYSTEM_.SYS_USERS_`. It does not close the remaining
per-view column coverage gap.

Scoped source paths checked for J017:

- `Manuals/Altibase_7.1/kor/General Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_7.1/eng/General Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_7.3/eng/General Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_trunk/eng/General Reference-2.The Data Dictionary.md`
- `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`
- `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`

J017 records `GAP-J017-001` for source drift around
`SYS_REPL_TABLE_OID_IN_USE_`, `V$QUEUE_DELETE_OFF`, `V$TEMPORARY_LOBS`, and the
reserved `V$ST_*` spatial unit views. Later jobs should keep Korean-source precedence
and require installed-version metadata checks when these names affect final customer
SQL.

## J018 Storage Log Archive Backup And Tablespace View Addendum

J018 uses the `general_reference_2_dictionary_views`, `administrator_operations`, and
release-note source families for Altibase 7.1, Altibase 7.3, and the Altibase 8.1
verified source. Korean General Reference 2 manuals remain authoritative for storage,
tablespace, datafile, log, archive, backup, checkpoint, snapshot, trace log, and
Temporary LOB performance-view behavior; matching English manuals were used only for
customer-facing terminology when consistent.

Design note: J018 keeps the 20-file attachment boundary unchanged and expands
`GPTs/attachments/06_data_dictionary_performance_views.md` in place. The documentation
structure now separates evidence-gathering view blocks from operational runbooks:
storage and backup corrective actions continue to live in
`02_administration_operations.md`, and generated DDL/administrative SQL continues to
live in `03_sql_ddl_generation.md`.

J018 updates `GPTs/attachments/06_data_dictionary_performance_views.md` with richer
cookbook checks and searchable object blocks for `V$DATABASE`, `V$TABLESPACES`,
`V$DATAFILES`, `V$MEM_TABLESPACES`, `V$MEM_TABLESPACE_CHECKPOINT_PATHS`,
`V$MEM_TABLESPACE_STATUS_DESC`, `V$VOL_TABLESPACES`, `V$STABLE_MEM_DATAFILES`,
`V$MEM_STABLE`, `V$LOG`, `V$LFG`, `V$ARCHIVE`, `V$BACKUP_INFO`,
`V$OBSOLETE_BACKUP_INFO`, `V$FILESTAT`, `V$SNAPSHOT`, `V$TRACELOG`, and
`V$TEMPORARY_LOBS`. `V$MEM_STABLE`, `V$LOG.CHECKPOINT_SCALE`, and
`V$TEMPORARY_LOBS` remain scoped to Altibase 8.1 verified source with portable
`V$TABLE`/`V$ALLCOLUMN` checks.

Scoped source paths checked for J018:

- `Manuals/Altibase_7.1/kor/General Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_7.1/eng/General Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_7.3/eng/General Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_trunk/eng/General Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_trunk/kor/Administrator's Manual.md`
- `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`
- `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`

No new manual/source-backed gap was discovered during J018. `GAP-J002-006` remains
open for later J019-J021 slices and for exhaustive per-view, patch-sensitive column
coverage outside the J018 storage/log/archive/backup/checkpoint scope.

## Source Roots

- Altibase 7.1 manuals: `Manuals/Altibase_7.1/kor` authoritative, `Manuals/Altibase_7.1/eng` English extraction/reference
- Altibase 7.3 manuals: `Manuals/Altibase_7.3/kor` authoritative, `Manuals/Altibase_7.3/eng` English extraction/reference
- Altibase 8.1 verified source manuals: `Manuals/Altibase_trunk/kor` authoritative, `Manuals/Altibase_trunk/eng` English extraction/reference
- Release notes, English: `ReleaseNotes/eng`
- Release notes, Korean: `ReleaseNotes/kor` authoritative if release-note content differs from English
- Patch notes: `PatchNotes/*/kor` authoritative for patch-level behavior; `PatchNotes/*/eng` English extraction/reference when present
- Tool manuals, release source: `Manuals/Tools/Altibase_release/kor` authoritative, `Manuals/Tools/Altibase_release/eng` English extraction/reference
- Tool manuals, Altibase 8.1 verified source: `Manuals/Tools/Altibase_trunk/kor` authoritative, `Manuals/Tools/Altibase_trunk/eng` English extraction/reference
- Technical documents: `Technical Documents/kor` authoritative when paired or Korean-only, `Technical Documents/eng` English extraction/reference
- Third-party guides: `3rd Party Guide for Altibase/kor` authoritative when present, `3rd Party Guide for Altibase/eng` English extraction/reference

## Inventory Summary

- Attachment files inventoried: 20
- Attachments with 7.1 source paths: 20
- Attachments with 7.3 source paths: 20
- Attachments with Altibase 8.1 verified source paths: 20
- Missing blocking source paths: none
- Korean supplemental technical documents: `Technical Documents/kor/JavaCompatibility.md`, `Technical Documents/kor/ReplicationCompatibility.md`, `Technical Documents/kor/Replication network check.md`

## Attachment Source Inventory

### 00_version_release_platform.md

Source purpose: release history, version differences, supported platforms, upgrade cautions.

- 7.1:
  - `ReleaseNotes/eng/Altibase_7_1_0_1_2_Release_Notes.md`
  - `Technical Documents/eng/Supported Platforms.md`
- 7.3:
  - `ReleaseNotes/eng/Altibase_7_3_0_0_1_Release_Notes.md`
  - `Technical Documents/eng/Supported Platforms.md`
- Altibase 8.1 verified source:
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`
  - `Technical Documents/eng/Supported Platforms.md`
- Korean source authority/check:
  - `ReleaseNotes/kor/Altibase_7_1_0_1_2_Release_Notes.md`
  - `ReleaseNotes/kor/Altibase_7_3_0_0_1_Release_Notes.md`
  - `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`
  - `Technical Documents/kor/Supported Platforms.md`

### 01_getting_started_installation.md

Source purpose: installation, database creation, startup, shutdown, first-run checks.

- 7.1:
  - `Manuals/Altibase_7.1/eng/Getting Started Guide.md`
  - `Manuals/Altibase_7.1/eng/Installation Guide.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/Getting Started Guide.md`
  - `Manuals/Altibase_7.3/eng/Installation Guide.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/Getting Started Guide.md`
  - `Manuals/Altibase_trunk/eng/Installation Guide.md`
- Korean source authority/check:
  - `Manuals/Altibase_7.1/kor/Getting Started Guide.md`
  - `Manuals/Altibase_7.1/kor/Installation Guide.md`
  - `Manuals/Altibase_7.3/kor/Getting Started Guide.md`
  - `Manuals/Altibase_7.3/kor/Installation Guide.md`
  - `Manuals/Altibase_trunk/kor/Getting Started Guide.md`
  - `Manuals/Altibase_trunk/kor/Installation Guide.md`

### 02_administration_operations.md

Source purpose: administration, accounts, backup/recovery, tablespaces, server operations.

- 7.1:
  - `Manuals/Altibase_7.1/eng/Administrator's Manual.md`
  - `Manuals/Altibase_7.1/eng/SQL Reference.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/Administrator’s Manual.md`
  - `Manuals/Altibase_7.3/eng/SQL Reference.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/Administrator’s Manual.md`
  - `Manuals/Altibase_trunk/eng/SQL Reference.md`
- Korean source authority/check:
  - `Manuals/Altibase_7.1/kor/Administrator's Manual.md`
  - `Manuals/Altibase_7.1/kor/SQL Reference.md`
  - `Manuals/Altibase_7.3/kor/Administrator's Manual.md`
  - `Manuals/Altibase_7.3/kor/SQL Reference.md`
  - `Manuals/Altibase_trunk/kor/Administrator's Manual.md`
  - `Manuals/Altibase_trunk/kor/SQL Reference.md`

### 03_sql_ddl_generation.md

Source purpose: DDL/DCL generation, tablespaces, tables, indexes, users, replication SQL, Log Analyzer CDC syntax, property checks.

- 7.1:
  - `Manuals/Altibase_7.1/eng/SQL Reference.md`
  - `Manuals/Altibase_7.1/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_7.1/eng/Replication Manual.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/SQL Reference.md`
  - `Manuals/Altibase_7.3/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_7.3/eng/Replication Manual.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/SQL Reference.md`
  - `Manuals/Altibase_trunk/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_trunk/eng/Replication Manual.md`
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`
- Korean source authority/check:
  - `Manuals/Altibase_7.1/kor/SQL Reference.md`
  - `Manuals/Altibase_7.1/kor/Replication Manual.md`
  - `Manuals/Altibase_7.1/kor/Log Analyzer User's Manual.md`
  - `Manuals/Altibase_7.1/kor/Administrator's Manual.md`
  - `Manuals/Altibase_7.3/kor/SQL Reference.md`
  - `Manuals/Altibase_7.3/kor/Replication Manual.md`
  - `Manuals/Altibase_7.3/kor/Log Analyzer User's Manual.md`
  - `Manuals/Altibase_7.3/kor/Administrator's Manual.md`
  - `Manuals/Altibase_trunk/kor/SQL Reference.md`
  - `Manuals/Altibase_trunk/kor/Replication Manual.md`
  - `Manuals/Altibase_trunk/kor/Log Analyzer User's Manual.md`
  - `Manuals/Altibase_trunk/kor/Administrator's Manual.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
- R03 source-drift note: Korean SQL Reference and General Reference differ on omitted user disk datafile `SIZE` defaults; the attachment now directs generated DDL to emit explicit disk datafile `SIZE`, `NEXT`, and `MAXSIZE` values instead of relying on omitted defaults.

### 04_sql_dml_oracle_compatibility.md

Source purpose: DML, expressions, functions, Oracle compatibility boundaries, SQL differences.

- 7.1:
  - `Manuals/Altibase_7.1/eng/SQL Reference.md`
  - `Manuals/Altibase_7.1/eng/General Reference-1.Data Types & Altibase Properties.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/SQL Reference.md`
  - `Manuals/Altibase_7.3/eng/General Reference-1.Data Types & Altibase Properties.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/SQL Reference.md`
  - `Manuals/Altibase_trunk/eng/General Reference-1.Data Types & Altibase Properties.md`
- Korean source authority/check:
  - `Manuals/Altibase_7.1/kor/SQL Reference.md`
  - `Manuals/Altibase_7.1/kor/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_7.3/kor/SQL Reference.md`
  - `Manuals/Altibase_7.3/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_trunk/kor/SQL Reference.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
- R07 source-detail note: Korean SQL Reference confirms the Altibase 7.1.0.7.7 boundary for PCRE2-compatible `REGEXP_MODE=1`; Korean General Reference confirms 8.1 JSON path operands are string-form only and cannot be bind variables, `NULL`, table columns, SQL functions, or user-defined functions.

### 05_data_types_properties.md

Source purpose: data types, Altibase properties, JSON, LOB behavior, version-specific property changes.

- 7.1:
  - `Manuals/Altibase_7.1/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `ReleaseNotes/eng/Altibase_7_1_0_1_2_Release_Notes.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `ReleaseNotes/eng/Altibase_7_3_0_0_1_Release_Notes.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`
- Korean source authority/check:
  - `Manuals/Altibase_7.1/kor/General Reference-1.Data Types & Altibase Properties.md`
  - `ReleaseNotes/kor/Altibase_7_1_0_1_2_Release_Notes.md`
  - `Manuals/Altibase_7.3/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `ReleaseNotes/kor/Altibase_7_3_0_0_1_Release_Notes.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`

### 06_data_dictionary_performance_views.md

Source purpose: meta tables, data dictionary, performance views, operational check queries.

- 7.1:
  - `Manuals/Altibase_7.1/eng/General Reference-2.The Data Dictionary.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/General Reference-2.The Data Dictionary.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/General Reference-2.The Data Dictionary.md`
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`
- Korean source authority/check:
  - `Manuals/Altibase_7.1/kor/SQL Reference.md`
  - `Manuals/Altibase_7.1/kor/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`
  - `PatchNotes/Altibase_7.1/kor/Altibase_7_1_0_8_5_Patch_Notes.md`

### 07_error_messages_troubleshooting.md

Source purpose: error codes, causes, actions, troubleshooting response format.

- 7.1:
  - `Manuals/Altibase_7.1/eng/Error Message Reference.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/Error Message Reference.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/Error Message Reference.md`
- Korean source authority/check:
  - `Manuals/Altibase_7.1/kor/Error Message Reference.md`
  - `Manuals/Altibase_7.1/kor/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_7.1/kor/SQL Reference.md`
  - `Manuals/Altibase_7.3/kor/Error Message Reference.md`
  - `Manuals/Altibase_7.3/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_7.3/kor/SQL Reference.md`
  - `Manuals/Altibase_trunk/kor/Error Message Reference.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_trunk/kor/SQL Reference.md`

### 08_performance_tuning_monitoring.md

Source purpose: execution plans, optimizer behavior, indexes, joins, monitoring APIs, SNMP.

- 7.1:
  - `Manuals/Altibase_7.1/eng/Performance Tuning Guide.md`
  - `Manuals/Altibase_7.1/eng/Stored Procedures Manual.md`
  - `Manuals/Altibase_7.1/eng/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_7.1/eng/Monitoring API Developer's Guide.md`
  - `Manuals/Altibase_7.1/eng/SNMP Agent Guide.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/Performance Tuning Guide.md`
  - `Manuals/Altibase_7.3/eng/Stored Procedures Manual.md`
  - `Manuals/Altibase_7.3/eng/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_7.3/eng/Monitoring API Developer's Guide.md`
  - `Manuals/Altibase_7.3/eng/SNMP Agent Guide.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/Performance Tuning Guide.md`
  - `Manuals/Altibase_trunk/eng/Stored Procedures Manual.md`
  - `Manuals/Altibase_trunk/eng/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_trunk/eng/Monitoring API Developer's Guide.md`
  - `Manuals/Altibase_trunk/eng/SNMP Agent Guide.md`
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`
- Korean source authority/check:
  - `Manuals/Altibase_7.1/kor/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_7.1/kor/Monitoring API Developer's Guide.md`
  - `Manuals/Altibase_7.1/kor/SNMP Agent Guide.md`
  - `Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_7.3/kor/Monitoring API Developer's Guide.md`
  - `Manuals/Altibase_7.3/kor/SNMP Agent Guide.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_trunk/kor/Monitoring API Developer's Guide.md`
  - `Manuals/Altibase_trunk/kor/SNMP Agent Guide.md`

### 09_replication_ha_cdc.md

Source purpose: replication, HA, CDC/log analysis, Replication Manager, compatibility, network checks, replication SSL.

- 7.1:
  - `Manuals/Altibase_7.1/eng/Replication Manual.md`
  - `Manuals/Altibase_7.1/eng/Log Analyzer User's Manual.md`
  - `Manuals/Tools/Altibase_release/eng/Replication Manager User's Manual.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/Replication Manual.md`
  - `Manuals/Altibase_7.3/eng/Log Analyzer User's Manual.md`
  - `Manuals/Tools/Altibase_release/eng/Replication Manager User's Manual.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/Replication Manual.md`
  - `Manuals/Altibase_trunk/eng/Log Analyzer User's Manual.md`
  - `Manuals/Tools/Altibase_trunk/eng/Replication Manager User's Manual.md`
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`
- Korean source authority/check:
  - `Manuals/Altibase_7.1/kor/SQL Reference.md`
  - `Manuals/Altibase_7.1/kor/Replication Manual.md`
  - `Manuals/Altibase_7.1/kor/Log Analyzer User's Manual.md`
  - `PatchNotes/Altibase_7.1/kor/Altibase_7_1_0_8_5_Patch_Notes.md`
  - `Manuals/Altibase_7.3/kor/SQL Reference.md`
  - `Manuals/Altibase_7.3/kor/Replication Manual.md`
  - `Manuals/Altibase_7.3/kor/Log Analyzer User's Manual.md`
  - `Manuals/Altibase_trunk/kor/SQL Reference.md`
  - `Manuals/Altibase_trunk/kor/Replication Manual.md`
  - `Manuals/Altibase_trunk/kor/Log Analyzer User's Manual.md`
  - `Manuals/Tools/Altibase_release/kor/Replication Manager User's Manual.md`
  - `Manuals/Tools/Altibase_trunk/kor/Replication Manager User's Manual.md`
  - `ReleaseNotes/kor/Altibase_Replication_Manager_1_2_Release_Notes.md`
  - `ReleaseNotes/kor/Altibase_Replication_Manager_1_3_Release_Notes.md`
  - `ReleaseNotes/kor/Altibase_Replication_Manager_1_4_Release_Notes.md`
- Korean supplemental technical documents:
  - `Technical Documents/kor/ReplicationCompatibility.md`
  - `Technical Documents/kor/Replication network check.md`

### 10_psm_stored_external_procedures.md

Source purpose: PSM, stored procedures/functions, external procedures, PL/SQL compatibility notes.

- 7.1:
  - `Manuals/Altibase_7.1/eng/Stored Procedures Manual.md`
  - `Manuals/Altibase_7.1/eng/External Procedures Manual.md`
  - `Manuals/Altibase_7.1/eng/General Reference-1.Data Types & Altibase Properties.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/Stored Procedures Manual.md`
  - `Manuals/Altibase_7.3/eng/External Procedures Manual.md`
  - `Manuals/Altibase_7.3/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `ReleaseNotes/eng/Altibase_7_3_0_0_1_Release_Notes.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/Stored Procedures Manual.md`
  - `Manuals/Altibase_trunk/eng/External Procedures Manual.md`
  - `Manuals/Altibase_trunk/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`
- Korean source authority/check:
  - `Manuals/Altibase_7.1/kor/Stored Procedures Manual.md`
  - `Manuals/Altibase_7.1/kor/External Procedures Manual.md`
  - `Manuals/Altibase_7.1/kor/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_7.3/kor/Stored Procedures Manual.md`
  - `Manuals/Altibase_7.3/kor/External Procedures Manual.md`
  - `Manuals/Altibase_7.3/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `ReleaseNotes/kor/Altibase_7_3_0_0_1_Release_Notes.md`
  - `Manuals/Altibase_trunk/kor/Stored Procedures Manual.md`
  - `Manuals/Altibase_trunk/kor/External Procedures Manual.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`

### 11_java_jdbc_spring.md

Source purpose: JDBC, Adapter for JDBC, Java compatibility, Spring Data JPA, Hibernate.

- 7.1:
  - `Manuals/Altibase_7.1/eng/JDBC User's Manual.md`
  - `Manuals/Altibase_7.1/eng/Adapter for JDBC User's Manual.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/JDBC User's Manual.md`
  - `Manuals/Altibase_7.3/eng/Adapter for JDBC User's Manual.md`
  - `3rd Party Guide for Altibase/eng/Spring Data JPA User's Guide for Altibase.md`
  - `3rd Party Guide for Altibase/eng/Spring Data JPA With Hibernate 6.4 User's Guide for Altibase.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/JDBC User's Manual.md`
  - `Manuals/Altibase_trunk/eng/Adapter for JDBC User's Manual.md`
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`
  - `3rd Party Guide for Altibase/eng/Spring Data JPA User's Guide for Altibase.md`
  - `3rd Party Guide for Altibase/eng/Spring Data JPA With Hibernate 6.4 User's Guide for Altibase.md`
- Korean manual authority/check:
  - `Manuals/Altibase_7.1/kor/JDBC User's Manual.md`
  - `Manuals/Altibase_7.1/kor/Adapter for JDBC User's Manual.md`
  - `Manuals/Altibase_7.3/kor/JDBC User's Manual.md`
  - `Manuals/Altibase_7.3/kor/Adapter for JDBC User's Manual.md`
  - `Manuals/Altibase_trunk/kor/JDBC User's Manual.md`
  - `Manuals/Altibase_trunk/kor/Adapter for JDBC User's Manual.md`
  - `3rd Party Guide for Altibase/kor/Spring Data JPA User's Guide for Altibase.md`
  - `3rd Party Guide for Altibase/kor/Spring Data JPA with Hibernate 6.4 User's Guide for Altibase.md`
- Korean supplemental technical documents:
  - `Technical Documents/kor/JavaCompatibility.md`

### 12_c_cli_odbc_precompiler.md

Source purpose: C client interfaces, CLI, ODBC, C Interface, Precompiler, LOB API guidance.

- 7.1:
  - `Manuals/Altibase_7.1/kor/CLI User's Manual.md`
  - `Manuals/Altibase_7.1/eng/CLI User's Manual.md`
  - `Manuals/Altibase_7.1/eng/ODBC User's Manual.md`
  - `Manuals/Altibase_7.1/eng/Altibase C Interface Manual.md`
  - `Manuals/Altibase_7.1/eng/Precompiler User’s Manual.md`
  - `Manuals/Altibase_7.1/kor/ODBC User's Manual.md`
  - `Manuals/Altibase_7.1/kor/Altibase C Interface Manual.md`
  - `Manuals/Altibase_7.1/kor/Precompiler User's Manual.md`
- 7.3:
  - `Manuals/Altibase_7.3/kor/CLI User's Manual.md`
  - `Manuals/Altibase_7.3/eng/CLI User's Manual.md`
  - `Manuals/Altibase_7.3/eng/ODBC User's Manual.md`
  - `Manuals/Altibase_7.3/eng/Altibase C Interface Manual.md`
  - `Manuals/Altibase_7.3/eng/Precompiler User's Manual.md`
  - `Manuals/Altibase_7.3/kor/ODBC User's Manual.md`
  - `Manuals/Altibase_7.3/kor/Altibase C Interface Manual.md`
  - `Manuals/Altibase_7.3/kor/Precompiler User's Manual.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/kor/CLI User's Manual.md`
  - `Manuals/Altibase_trunk/eng/CLI User's Manual.md`
  - `Manuals/Altibase_trunk/eng/ODBC User's Manual.md`
  - `Manuals/Altibase_trunk/eng/Altibase C Interface Manual.md`
  - `Manuals/Altibase_trunk/eng/Precompiler User's Manual.md`
  - `Manuals/Altibase_trunk/kor/ODBC User's Manual.md`
  - `Manuals/Altibase_trunk/kor/Altibase C Interface Manual.md`
  - `Manuals/Altibase_trunk/kor/Precompiler User's Manual.md`
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`

### 13_isql_iloader_basic_tools.md

Source purpose: iSQL, iLoader, export/import, first-line operational tool usage.

- 7.1:
  - `Manuals/Altibase_7.1/kor/iSQL User's Manual.md`
  - `Manuals/Altibase_7.1/eng/iSQL User's Manual.md`
  - `Manuals/Altibase_7.1/eng/iLoader User's Manual.md`
  - `Manuals/Altibase_7.1/kor/iLoader User's Manual.md`
- 7.3:
  - `Manuals/Altibase_7.3/kor/iSQL User's Manual.md`
  - `Manuals/Altibase_7.3/eng/iSQL User's Manual.md`
  - `Manuals/Altibase_7.3/eng/iLoader User's Manual.md`
  - `Manuals/Altibase_7.3/kor/iLoader User's Manual.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/kor/iSQL User's Manual.md`
  - `Manuals/Altibase_trunk/eng/iSQL User's Manual.md`
  - `Manuals/Altibase_trunk/eng/iLoader User's Manual.md`
  - `Manuals/Altibase_trunk/kor/iLoader User's Manual.md`
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`

### 14_utilities_operation_tools.md

Source purpose: utilities, `aexport`, `altiComp`, `iloader`, `isql`, `aku`, `altiMon`, `dataCompJ`.

- 7.1:
  - `Manuals/Altibase_7.1/kor/Utilities Manual.md`
  - `Manuals/Altibase_7.1/eng/Utilities Manual.md`
  - `Manuals/Tools/Altibase_release/kor/dataCompJ User's Manual.md`
  - `Manuals/Tools/Altibase_release/eng/dataCompJ User's Manual.md`
- 7.3:
  - `Manuals/Altibase_7.3/kor/Utilities Manual.md`
  - `Manuals/Altibase_7.3/eng/Utilities Manual.md`
  - `Manuals/Tools/Altibase_release/kor/dataCompJ User's Manual.md`
  - `Manuals/Tools/Altibase_release/eng/dataCompJ User's Manual.md`
  - `ReleaseNotes/kor/Altibase_dataCompJ_7_2_Release_Notes.md`
  - `ReleaseNotes/eng/Altibase_dataCompJ_7_2_Release_Notes.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/kor/Utilities Manual.md`
  - `Manuals/Altibase_trunk/eng/Utilities Manual.md`
  - `Manuals/Tools/Altibase_trunk/kor/dataCompJ User's Manual.md`
  - `Manuals/Tools/Altibase_trunk/eng/dataCompJ User's Manual.md`
- Source authority note: Korean manuals and Korean release notes listed above are primary; English entries are secondary extraction/parity references.

### 15_migration_oracle_compatibility.md

Source purpose: Migration Center, Adapter for Oracle, Oracle-to-Altibase conversion guidance.

- 7.1:
  - `Manuals/Altibase_7.1/eng/Adapter for Oracle User's Manual.md`
  - `Manuals/Tools/Altibase_release/eng/Migration Center User's Manual.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/Adapter for Oracle User's Manual.md`
  - `Manuals/Tools/Altibase_release/eng/Migration Center User's Manual.md`
  - `ReleaseNotes/eng/Altibase_Migration_Center_7_19_Release_Notes.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/Adapter for Oracle User's Manual.md`
  - `Manuals/Tools/Altibase_trunk/eng/Migration Center User's Manual.md`
  - `ReleaseNotes/eng/Altibase_Migration_Center_7_19_Release_Notes.md`
- Korean source authority/check:
  - `Manuals/Altibase_7.1/kor/Adapter for Oracle User's Manual.md`
  - `Manuals/Altibase_7.3/kor/Adapter for Oracle User's Manual.md`
  - `Manuals/Altibase_trunk/kor/Adapter for Oracle User's Manual.md`
  - `Manuals/Tools/Altibase_release/kor/Migration Center User's Manual.md`
  - `Manuals/Tools/Altibase_trunk/kor/Migration Center User's Manual.md`
  - `ReleaseNotes/kor/Altibase_Migration_Center_7_19_Release_Notes.md`

### 16_dblink_external_connectors.md

Source purpose: DB Link, DB Link Java compatibility, Hadoop Connector, third-party connector setup and procedures.

- 7.1:
  - `Manuals/Altibase_7.1/eng/DB Link User's Manual.md`
  - `Manuals/Altibase_7.1/eng/Hadoop Connector User's Manual.md`
  - `Manuals/Tools/Altibase_release/kor/Altibase 3rd Party Connector Guide.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/DB Link User's Manual.md`
  - `Manuals/Altibase_7.3/eng/Hadoop Connector User's Manual.md`
  - `Manuals/Tools/Altibase_release/eng/Altibase 3rd Party Connector Guide.md`
  - `Manuals/Tools/Altibase_release/kor/Altibase 3rd Party Connector Guide.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/DB Link User's Manual.md`
  - `Manuals/Altibase_trunk/eng/Hadoop Connector User's Manual.md`
  - `Manuals/Tools/Altibase_trunk/eng/Altibase 3rd Party Connector Guide.md`
  - `Manuals/Tools/Altibase_trunk/kor/Altibase 3rd Party Connector Guide.md`
- Korean source authority/check:
  - `Manuals/Altibase_7.1/kor/DB Link User's Manual.md`
  - `Manuals/Altibase_7.1/kor/Hadoop Connector User's Manual.md`
  - `Manuals/Altibase_7.3/kor/DB Link User's Manual.md`
  - `Manuals/Altibase_7.3/kor/Hadoop Connector User's Manual.md`
  - `Manuals/Altibase_trunk/kor/DB Link User's Manual.md`
  - `Manuals/Altibase_trunk/kor/Hadoop Connector User's Manual.md`
  - `3rd Party Guide for Altibase/kor/Spring Data JPA with Hibernate 6.4 User's Guide for Altibase.md`
  - `Technical Documents/kor/JavaCompatibility.md`
  - `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`

### 17_kubernetes_aku_cloud.md

Source purpose: Kubernetes deployment, AKU samples, container operations, release-note context.

- 7.1:
  - `Manuals/Altibase_7.1/eng/Installation Guide.md`
  - `Manuals/Altibase_7.1/eng/Administrator's Manual.md`
  - `Manuals/Altibase_7.1/eng/Replication Manual.md`
  - `Manuals/Altibase_7.1/eng/Utilities Manual.md`
  - `3rd Party Guide for Altibase/eng/Altibase aku Sample Guide for Kubernetes.md`
- 7.3:
  - `3rd Party Guide for Altibase/eng/Kubernetes User's Guide for Altibase.md`
  - `3rd Party Guide for Altibase/eng/Altibase aku Sample Guide for Kubernetes.md`
  - `ReleaseNotes/eng/Altibase_7_3_0_0_1_Release_Notes.md`
- Altibase 8.1 verified source:
  - `3rd Party Guide for Altibase/eng/Kubernetes User's Guide for Altibase.md`
  - `3rd Party Guide for Altibase/eng/Altibase aku Sample Guide for Kubernetes.md`
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`
- Korean source authority/check:
  - `Manuals/Altibase_7.1/kor/Utilities Manual.md`
  - `Manuals/Altibase_7.3/kor/Utilities Manual.md`
  - `Manuals/Altibase_trunk/kor/Utilities Manual.md`
  - `3rd Party Guide for Altibase/kor/Kubernetes User's Guide for Altibase.md`
  - `3rd Party Guide for Altibase/kor/Altibase aku Sample Guide for Kubernetes.md`
  - `ReleaseNotes/kor/Altibase_7_3_0_0_1_Release_Notes.md`
  - `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`

### 18_security_ssl_tls.md

Source purpose: SSL/TLS server/client setup, certificate configuration, replication SSL.

- 7.1:
  - `Manuals/Altibase_7.1/eng/Altibase SSL TLS User's Guide.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/Altibase SSL TLS User's Guide.md`
  - `ReleaseNotes/eng/Altibase_7_3_0_0_1_Release_Notes.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/Altibase SSL TLS User's Guide.md`
  - `Manuals/Altibase_trunk/eng/Replication Manual.md`
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`
- Korean source authority/check:
  - `Manuals/Altibase_7.1/kor/Altibase SSL TLS User's Guide.md`
  - `Manuals/Altibase_7.3/kor/Altibase SSL TLS User's Guide.md`
  - `ReleaseNotes/kor/Altibase_7_3_0_0_1_Release_Notes.md`
  - `Manuals/Altibase_trunk/kor/Altibase SSL TLS User's Guide.md`
  - `Manuals/Altibase_trunk/kor/Replication Manual.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_trunk/kor/SQL Reference.md`
  - `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`

### 19_spatial_nifi_tableau_misc.md

Source purpose: Spatial SQL, `GEOMETRY`, altiShapeLoader, NiFi, Tableau.

- 7.1:
  - `Manuals/Altibase_7.1/eng/Spatial SQL Reference.md`
  - `Manuals/Tools/Altibase_release/eng/altiShapeLoader User's Manual.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/Spatial SQL Reference.md`
  - `Manuals/Tools/Altibase_release/eng/altiShapeLoader User's Manual.md`
  - `3rd Party Guide for Altibase/eng/NiFi User's Guide for Altibase.md`
  - `3rd Party Guide for Altibase/eng/Tableau User's Guide for Altibase/Tableau User's Guide for Altibase.md`
  - `ReleaseNotes/eng/Altibase_altiShapeLoader_1_0_Release_Notes.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/Spatial SQL Reference.md`
  - `Manuals/Tools/Altibase_trunk/eng/altiShapeLoader User's Manual.md`
  - `3rd Party Guide for Altibase/eng/NiFi User's Guide for Altibase.md`
  - `3rd Party Guide for Altibase/eng/Tableau User's Guide for Altibase/Tableau User's Guide for Altibase.md`
- Korean source authority/check:
  - `Manuals/Altibase_7.1/kor/Spatial SQL Reference.md`
  - `Manuals/Altibase_7.3/kor/Spatial SQL Reference.md`
  - `Manuals/Altibase_trunk/kor/Spatial SQL Reference.md`
  - `Manuals/Tools/Altibase_release/kor/altiShapeLoader User's Manual.md`
  - `Manuals/Tools/Altibase_trunk/kor/altiShapeLoader User's Manual.md`
  - `3rd Party Guide for Altibase/kor/NiFi User's Guide for Altibase.md`
  - `3rd Party Guide for Altibase/kor/Tableau User's Guide for Altibase/Tableau User's Guide for Altibase.md`
  - `ReleaseNotes/kor/Altibase_altiShapeLoader_1_0_Release_Notes.md`

## Follow-Up Notes

- JOB-011 should verify the 8.1-specific source claims against `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`, especially JSON, Temporary LOB, replication SSL, JSON plan output, new properties, and new performance views.
- JOB-012 records that Korean manuals are authoritative when English and Korean manuals differ; later jobs should check Korean manuals for version-sensitive claims and record any English-source drift.
- JOB-013 and JOB-014 should start from the manuals listed here, especially SQL Reference, Performance Tuning Guide, Replication Manual, Installation Guide, Administrator manual, and the third-party UI-heavy guides.
