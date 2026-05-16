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

## J019 Session Statement Wait Lock Transaction View Addendum

J019 uses the `general_reference_2_dictionary_views` source family for Altibase 7.1,
Altibase 7.3, and the Altibase 8.1 verified source. Korean General Reference 2 manuals
remain authoritative for session, statement, SQL text, wait, lock, transaction,
latch/mutex, and service-thread performance-view behavior; matching English manuals
were used only for customer-facing terminology when consistent.

Design note: J019 keeps the 20-file attachment boundary unchanged and expands
`GPTs/attachments/06_data_dictionary_performance_views.md` in place. The documentation
structure now treats `06_data_dictionary_performance_views.md` as the evidence
collection and view-reference surface for active sessions, SQL text, waits, lock
chains, transactions, and service threads. Operational tuning actions and root-cause
interpretation remain cross-referenced to `08_performance_tuning_monitoring.md`.

J019 updates `GPTs/attachments/06_data_dictionary_performance_views.md` with richer
cookbook checks and searchable object blocks for `V$SESSION`, `V$SESSIONMGR`,
`V$SERVICE_THREAD`, `V$SERVICE_THREAD_MGR`, `V$STATEMENT`, `V$SQLTEXT`,
`V$EVENT_NAME`, `V$WAIT_CLASS_NAME`, `V$SESSION_WAIT`, `V$SESSION_EVENT`,
`V$SESSION_WAIT_CLASS`, `V$SYSTEM_EVENT`, `V$SYSTEM_WAIT_CLASS`, `V$LATCH`,
`V$MUTEX`, `V$TRANSACTION`, `V$TRANSACTION_MGR`, `V$LOCK_WAIT`, `V$LOCK`, and
`V$LOCK_STATEMENT`.

Scoped source paths checked for J019:

- `Manuals/Altibase_7.1/kor/General Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_7.1/eng/General Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_7.3/eng/General Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_trunk/eng/General Reference-2.The Data Dictionary.md`

No new manual/source-backed gap was discovered during J019. `GAP-J002-006` remains
open for later J020-J021 slices and for exhaustive per-view, patch-sensitive column
coverage outside the J019 session/statement/wait/lock/transaction/service-thread
scope.

## J020 Optimizer Plan Cache Statistics Buffer View Addendum

J020 uses the `general_reference_2_dictionary_views`, `performance_tuning`,
`general_reference_1_datatypes_properties`, and `sql_reference` source families for
Altibase 7.1, Altibase 7.3, and the Altibase 8.1 verified source. Korean General
Reference 2 manuals remain authoritative for optimizer statistics, SQL plan cache,
system/session statistics, memory, buffer, flusher, table/index internals, segment,
undo, disk temporary-table, and direct-path insert performance-view columns. Korean
Performance Tuning Guides remain authoritative for buffer, memory-GC, statistics, SQL
plan cache, checkpoint/flusher, disk temporary-table, and direct-path insert
interpretation. Matching English manuals were used only for customer-facing wording
when consistent.

Design note: J020 keeps the 20-file attachment boundary unchanged. It expands
`GPTs/attachments/06_data_dictionary_performance_views.md` as the evidence collection
and view-reference surface for plan cache, optimizer statistics, buffer, memory,
flusher, table/index, segment, undo, temp, and direct-path counters. It expands
`GPTs/attachments/08_performance_tuning_monitoring.md` only where the same views need
operational tuning interpretation. Property defaults and change methods remain routed
to `05_data_types_properties.md`; SQL generation and administrative statements remain
routed to `03_sql_ddl_generation.md`.

J020 updates `GPTs/attachments/06_data_dictionary_performance_views.md` with richer
cookbook checks and searchable object blocks for `V$SQL_PLAN_CACHE`,
`V$SQL_PLAN_CACHE_PCO`, `V$SQL_PLAN_CACHE_SQLTEXT`, `V$DBMS_STATS`,
`V$LOCK_TABLE_STATS`, `V$STATNAME`, `V$SYSSTAT`, `V$SESSTAT`, `V$MEMSTAT`,
`V$MEMGC`, `V$BUFFPAGEINFO`, `V$BUFFPOOL_STAT`, `V$UNDO_BUFF_STAT`,
`V$SBUFFER_STAT`, `V$FLUSHER`, `V$FLUSHINFO`, `V$SFLUSHER`, `V$SFLUSHINFO`,
`V$MEMTBL_INFO`, `V$DISKTBL_INFO`, `V$INDEX`, BTREE/RTREE header and node-pool view
families, `V$SEGMENT`, `V$USAGE`, `V$DB_FREEPAGELISTS`, `V$TSSEGS`, `V$TXSEGS`,
`V$UDSEGS`, `V$DISK_UNDO_USAGE`, `V$DISK_TEMP_INFO`, `V$DISK_TEMP_STAT`, and
`V$DIRECT_PATH_INSERT`. It updates `GPTs/attachments/08_performance_tuning_monitoring.md`
with view-backed checkpoint/flusher, disk temporary-table spill, and direct-path insert
diagnostic blocks.

Scoped source paths checked for J020:

- `Manuals/Altibase_7.1/kor/General Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_7.1/eng/General Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_7.3/eng/General Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_trunk/eng/General Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_7.1/kor/Performance Tuning Guide.md`
- `Manuals/Altibase_7.3/kor/Performance Tuning Guide.md`
- `Manuals/Altibase_trunk/kor/Performance Tuning Guide.md`
- `Manuals/Altibase_7.1/eng/Performance Tuning Guide.md`
- `Manuals/Altibase_7.3/eng/Performance Tuning Guide.md`
- `Manuals/Altibase_trunk/eng/Performance Tuning Guide.md`
- `Manuals/Altibase_7.1/kor/SQL Reference.md`
- `Manuals/Altibase_7.3/kor/SQL Reference.md`
- `Manuals/Altibase_trunk/kor/SQL Reference.md`

J021 design/source note: J021 used `general_reference_2_dictionary_views`,
`replication_manual`, `log_analyzer`, `monitoring_api_snmp`, and `security_ssl_tls`
source families for Altibase 7.1, Altibase 7.3, and the Altibase 8.1 verified source.
Korean manuals were preferred where paired sources existed; English extraction was used
for 7.3 and 8.1 General Reference 2 data-dictionary details where the corresponding
Korean Markdown source was not present in this repository. The main customer-facing
update is in `GPTs/attachments/06_data_dictionary_performance_views.md`, with
cross-reference updates in `GPTs/attachments/08_performance_tuning_monitoring.md`,
`GPTs/attachments/09_replication_ha_cdc.md`, and
`GPTs/attachments/18_security_ssl_tls.md`. The job expanded audit/security metadata,
replication and Log Analyzer CDC evidence mapping, Monitoring API-to-view mapping, and
SNMP MIB-to-SQL cross-check guidance. No new manual/source-backed gap was discovered
during J021. `GAP-J002-006` remains open only for exhaustive per-view,
patch-sensitive column proof beyond the J021 slice, and `GAP-J002-009` remains open
for live Monitoring API/SNMP validation against target environments.

## J022 Error Reference Inventory Addendum

J022 uses the `error_message_reference` source family for Altibase 7.1, Altibase 7.3,
and the Altibase 8.1 verified source. Korean Error Message Reference manuals remain
authoritative for error-family inventory, exact code, decimal code, symbol, severity
heading, message, cause, and action; matching English manuals were used only as
extraction aids when consistent.

J022 adds `GPTs/reports/error_reference_inventory.md` as the source-backed error-family
inventory and troubleshooting response-schema handoff for J023-J026. It updates
`GPTs/attachments/07_error_messages_troubleshooting.md` with a compact customer-facing
inventory baseline and tightens the `sdERR_*` sharding version caution. The attachment
boundary remains unchanged.

Scoped source paths checked for J022:

- `Manuals/Altibase_7.1/kor/Error Message Reference.md`
- `Manuals/Altibase_7.3/kor/Error Message Reference.md`
- `Manuals/Altibase_trunk/kor/Error Message Reference.md`
- `Manuals/Altibase_7.1/eng/Error Message Reference.md`
- `Manuals/Altibase_7.3/eng/Error Message Reference.md`
- `Manuals/Altibase_trunk/eng/Error Message Reference.md`

J022 records `GAP-J022-001` for source drift around `SD Error Code`: it is present in
the 7.1 Korean source and the checked 8.1 English extraction aid, but absent from the
checked 7.3 and Altibase 8.1 verified Korean Error Message Reference files. Later
answers must require exact installed-version evidence before making definitive 7.3 or
8.1 `sdERR_*` claims.

## J023 Storage Backup Recovery And Tablespace Error Addendum

J023 uses the `error_message_reference` source family for Altibase 7.1, Altibase 7.3,
and the Altibase 8.1 verified source. Korean Error Message Reference manuals remain
authoritative for exact code, decimal code, symbol, severity heading, message, cause,
and action; matching English manuals were used only as extraction aids when consistent.
Supporting source families for checks and response guardrails are
`administrator_operations`, `sql_reference`,
`general_reference_1_datatypes_properties`, and
`general_reference_2_dictionary_views`.

Design note: J023 keeps the 20-file attachment boundary unchanged and expands
`GPTs/attachments/07_error_messages_troubleshooting.md` in place with grouped
exact-code maps. Corrective runbooks remain in `02_administration_operations.md`,
copy-ready administrative SQL remains in `03_sql_ddl_generation.md`, property context
remains in `05_data_types_properties.md`, and storage/backup validation views remain in
`06_data_dictionary_performance_views.md`.

Scoped source paths checked for J023:

- `Manuals/Altibase_7.1/kor/Error Message Reference.md`
- `Manuals/Altibase_7.3/kor/Error Message Reference.md`
- `Manuals/Altibase_trunk/kor/Error Message Reference.md`
- `Manuals/Altibase_7.1/eng/Error Message Reference.md`
- `Manuals/Altibase_7.3/eng/Error Message Reference.md`
- `Manuals/Altibase_trunk/eng/Error Message Reference.md`

J023 updated `GPTs/attachments/07_error_messages_troubleshooting.md` with storage,
datafile, backup, recovery, log, checkpoint, incremental backup, and tablespace grouped
blocks. The grouped blocks include exact reference codes and symbols, source-backed
message/action focus, `V$LOG`, `V$ARCHIVE`, `V$TABLESPACES`, `V$DATAFILES`,
`V$BACKUP_INFO`, and checkpoint-path check SQL, required customer-input prompts, and
stop conditions before destructive recovery actions. No new manual/source-backed gap
was discovered during J023; `GAP-J002-008` remains open for the later J024-J026 error
slices and for exhaustive exact-code coverage outside the J023 grouped blocks.

## J024 SQL DDL Data Type JSON And LOB Error Addendum

J024 uses the `error_message_reference` source family for Altibase 7.1, Altibase 7.3,
and the Altibase 8.1 verified source. Korean Error Message Reference manuals remain
authoritative for exact code, decimal code, symbol, severity heading, message, cause,
and action; matching English manuals were used only as extraction aids when consistent.
Supporting source families for checks and response guardrails are `sql_reference`,
`general_reference_1_datatypes_properties`, `general_reference_2_dictionary_views`,
`c_cli_odbc_precompiler`, `isql_iloader`, and `utilities_datacompj`.

Design note: J024 keeps the 20-file attachment boundary unchanged and expands
`GPTs/attachments/07_error_messages_troubleshooting.md` in place with grouped
exact-code maps. Corrected SQL remains in `03_sql_ddl_generation.md` and
`04_sql_dml_oracle_compatibility.md`, data type and property semantics remain in
`05_data_types_properties.md`, dictionary checks remain in
`06_data_dictionary_performance_views.md`, and LOB client/tool workflows remain in
`12_c_cli_odbc_precompiler.md`, `13_isql_iloader_basic_tools.md`, and
`14_utilities_operation_tools.md`.

Scoped source paths checked for J024:

- `Manuals/Altibase_7.1/kor/Error Message Reference.md`
- `Manuals/Altibase_7.3/kor/Error Message Reference.md`
- `Manuals/Altibase_trunk/kor/Error Message Reference.md`
- `Manuals/Altibase_7.1/eng/Error Message Reference.md`
- `Manuals/Altibase_7.3/eng/Error Message Reference.md`
- `Manuals/Altibase_trunk/eng/Error Message Reference.md`
- `Manuals/Altibase_7.1/kor/SQL Reference.md`
- `Manuals/Altibase_7.3/kor/SQL Reference.md`
- `Manuals/Altibase_trunk/kor/SQL Reference.md`
- `Manuals/Altibase_7.1/kor/General Reference-1.Data Types & Altibase Properties.md`
- `Manuals/Altibase_7.3/kor/General_Reference-1.Data Types & Altibase Properties.md`
- `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`

J024 updated `GPTs/attachments/07_error_messages_troubleshooting.md` with SQL parser,
DDL clause, table/column/data type, constraint, conversion, date, regular-expression,
ordinary LOB, client/utility LOB, JSON, and Temporary LOB grouped blocks. The grouped
blocks include exact reference codes and symbols, source-backed message/action focus,
object/column/constraint/property check SQL, required customer-input prompts, and
version cautions. No new manual/source-backed gap was discovered during J024;
`GAP-J002-008` remains open for the later J025-J026 error slices and for exhaustive
exact-code coverage outside the J023-J024 grouped blocks.

## J025 Client Network Security Replication And Tool Error Addendum

J025 uses the `error_message_reference` source family for Altibase 7.1, Altibase 7.3,
and the Altibase 8.1 verified source. Korean Error Message Reference manuals remain
authoritative for exact code, decimal code, symbol, severity heading, message, cause,
and action; matching English manuals were used only as extraction aids when consistent.
Supporting source families for diagnostics and guardrails are `replication_manual`,
`security_ssl_tls`, `general_reference_2_dictionary_views`, `isql_iloader`,
`utilities_datacompj`, `c_cli_odbc_precompiler`, `dblink_hadoop_external_connectors`,
and `log_analyzer`.

Design note: J025 keeps the 20-file attachment boundary unchanged and expands
`GPTs/attachments/07_error_messages_troubleshooting.md` in place with grouped
exact-code maps. Runtime remediation remains routed to owner attachments:
replication and Log Analyzer workflows to `09_replication_ha_cdc.md`, CLI/ODBC/APRE
details to `12_c_cli_odbc_precompiler.md`, iSQL/iLoader and utility command syntax to
`13_isql_iloader_basic_tools.md` and `14_utilities_operation_tools.md`, DB Link and
`AltiLinker` procedures to `16_dblink_external_connectors.md`, and SSL/TLS setup to
`18_security_ssl_tls.md`.

Scoped source paths checked for J025:

- `Manuals/Altibase_7.1/kor/Error Message Reference.md`
- `Manuals/Altibase_7.3/kor/Error Message Reference.md`
- `Manuals/Altibase_trunk/kor/Error Message Reference.md`
- `Manuals/Altibase_7.1/eng/Error Message Reference.md`
- `Manuals/Altibase_7.3/eng/Error Message Reference.md`
- `Manuals/Altibase_trunk/eng/Error Message Reference.md`
- `Manuals/Altibase_7.1/kor/General Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`
- `GPTs/attachments/09_replication_ha_cdc.md`
- `GPTs/attachments/12_c_cli_odbc_precompiler.md`
- `GPTs/attachments/13_isql_iloader_basic_tools.md`
- `GPTs/attachments/14_utilities_operation_tools.md`
- `GPTs/attachments/16_dblink_external_connectors.md`
- `GPTs/attachments/18_security_ssl_tls.md`

J025 updated `GPTs/attachments/07_error_messages_troubleshooting.md` with grouped
blocks for client session/protocol and alternate-server connection errors, replication
startup/object-eligibility and metadata/conflict/log-buffer errors, DB Link/`AltiLinker`
network and transaction errors, iSQL/iLoader/utility option and file errors, APRE
source/connection/cursor errors, and Log Analyzer network/protocol/metadata/XLog-pool
errors. It also expanded SSL/TLS evidence prompts and property checks around the
existing client and server SSL error blocks. No new manual/source-backed gap was
discovered during J025; `GAP-J002-008` remains open for J026 QA and for exhaustive
exact-code coverage outside the J023-J025 grouped blocks.

## J026 Troubleshooting QA And Unresolved Error Gap Addendum

J026 uses the `error_message_reference` source family for Altibase 7.1, Altibase 7.3,
and the Altibase 8.1 verified source. Korean Error Message Reference manuals remain
authoritative for exact code, decimal code, symbol, severity heading, message, cause,
and action; matching English manuals are extraction aids only when consistent.
Supporting source families for unresolved-gap routing are `spatial_nifi_tableau`,
`general_reference_2_dictionary_views`, `replication_manual`, and the existing owner
attachments.

Design note: J026 keeps the 20-file attachment boundary unchanged. It does not attempt
to convert every remaining Error Message Reference entry into `07_error_messages_troubleshooting.md`.
Instead, it validates the J022-J025 troubleshooting structure, adds a customer-facing
QA gate for exact-code answers, aligns the response format with `Required Customer
Input`, tightens uncovered-code and prefix-safety wording, and records remaining
manual-backed work in the gap register.

Scoped source paths checked for J026:

- `Manuals/Altibase_7.1/kor/Error Message Reference.md`
- `Manuals/Altibase_7.3/kor/Error Message Reference.md`
- `Manuals/Altibase_trunk/kor/Error Message Reference.md`
- `Manuals/Altibase_7.1/kor/Spatial SQL Reference.md`
- `Manuals/Altibase_7.3/kor/Spatial SQL Reference.md`
- `Manuals/Altibase_trunk/kor/Spatial SQL Reference.md`
- `GPTs/attachments/19_spatial_nifi_tableau_misc.md`
- `GPTs/reports/error_reference_inventory.md`
- `GPTs/reports/gap_register.md`

J026 updated `GPTs/attachments/07_error_messages_troubleshooting.md` to require
explicit `Required Customer Input` handling, preserve user-supplied exact codes and
messages, avoid module/severity/`SQLSTATE` inference from prefixes alone, and stop
before destructive or environment-changing remedies when evidence is incomplete. No
new Korean/English source-drift case was found beyond the existing `SD Error Code`
drift tracked as `GAP-J022-001`. J026 records `GAP-J026-001` for the remaining
Spatial `ST Error Code` exact-code itemization gap across the selected Korean 7.1,
7.3, and Altibase 8.1 verified source Error Message Reference and Spatial SQL
Reference sources.

## J027 Installation Platform Startup And Shutdown Runbook Addendum

J027 uses the `getting_started_installation`, `release_notes_platform`, and
`technical_documents_support` source families for Altibase 7.1, Altibase 7.3, and the
Altibase 8.1 verified source. Korean Getting Started Guides, Installation Guides,
release notes, and supported-platform technical documents remain authoritative for
installation flow, platform/package boundaries, database creation, startup, shutdown,
first-run checks, and patch rollback cautions; matching English manuals are extraction
aids only when consistent.

Design note: J027 keeps the 20-file attachment boundary unchanged and does not create a
new attachment. It expands `GPTs/attachments/01_getting_started_installation.md` with
runbook-schema blocks for required inputs, stop conditions, server package
installation, database creation, startup and first-run verification, shutdown mode
selection, and client-only installation. The existing platform matrix remains in
`GPTs/attachments/00_version_release_platform.md`; `01_getting_started_installation.md`
now routes platform decisions there and preserves exact-version guardrails.

Scoped source paths checked for J027:

- `Manuals/Altibase_7.1/kor/Getting Started Guide.md`
- `Manuals/Altibase_7.1/kor/Installation Guide.md`
- `Manuals/Altibase_7.3/kor/Getting Started Guide.md`
- `Manuals/Altibase_7.3/kor/Installation Guide.md`
- `Manuals/Altibase_trunk/kor/Getting Started Guide.md`
- `Manuals/Altibase_trunk/kor/Installation Guide.md`
- `Manuals/Altibase_7.1/eng/Getting Started Guide.md`
- `Manuals/Altibase_7.1/eng/Installation Guide.md`
- `Manuals/Altibase_7.3/eng/Getting Started Guide.md`
- `Manuals/Altibase_7.3/eng/Installation Guide.md`
- `Manuals/Altibase_trunk/eng/Getting Started Guide.md`
- `Manuals/Altibase_trunk/eng/Installation Guide.md`
- `ReleaseNotes/kor/Altibase_7_1_0_1_2_Release_Notes.md`
- `ReleaseNotes/kor/Altibase_7_3_0_0_1_Release_Notes.md`
- `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`
- `Technical Documents/kor/Supported Platforms.md`
- `GPTs/reports/gap_register.md`
- `GPTs/reports/coverage_matrix.md`
- `GPTs/reports/catalog_schema_extraction_rules.md`

J027 adds no new attachment filename, source family, or Korean/English source-drift
case. It narrows `GAP-J002-018` for the installation/startup/shutdown slice by
representing the high-risk installer and first-run procedure as procedural text,
copy-ready command blocks, expected output markers, and stop conditions. `GAP-J002-007`
remains a guardrail for exhaustive 7.1 and 7.3 minor patch platform review.

## J028 Backup Archive And Incremental Backup Runbook Addendum

J028 uses the `administrator_operations`, `sql_reference`,
`general_reference_1_datatypes_properties`, `general_reference_2_dictionary_views`, and
`isql_iloader` source families for Altibase 7.1, Altibase 7.3, and the Altibase 8.1
verified source. Korean Administrator, SQL Reference, General Reference, and iLoader
manuals remain authoritative for backup method boundaries, archive-log behavior,
log-anchor handling, snapshot export, incremental backup metadata, and recovery
preconditions; matching English manuals remain extraction aids only when consistent.

Design note: J028 keeps the 20-file attachment boundary unchanged and expands
`GPTs/attachments/02_administration_operations.md` with backup strategy blocks and
runbooks for logical `iLoader` backup/restore, offline physical backup/restore, online
database and tablespace backup, archive-log retention, log-anchor backup/restore
decisions, incremental backup initialization, recurring level 0/level 1 backup, backup
file movement/deletion, and invalid `backupInfo` removal with a 7.3/8.1 source-backed
caution. It updates
`GPTs/attachments/03_sql_ddl_generation.md` only to expose the source-backed
Altibase 7.3/8.1 `ALTER DATABASE REMOVE BACKUP INFO FILE` repair clause and its
generation guardrail.

Scoped source paths checked for J028:

- `Manuals/Altibase_7.1/kor/Administrator's Manual.md`
- `Manuals/Altibase_7.3/kor/Administrator's Manual.md`
- `Manuals/Altibase_trunk/kor/Administrator's Manual.md`
- `Manuals/Altibase_7.1/kor/SQL Reference.md`
- `Manuals/Altibase_7.3/kor/SQL Reference.md`
- `Manuals/Altibase_trunk/kor/SQL Reference.md`
- `Manuals/Altibase_7.1/kor/General Reference-1.Data Types & Altibase Properties.md`
- `Manuals/Altibase_7.3/kor/General_Reference-1.Data Types & Altibase Properties.md`
- `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
- `Manuals/Altibase_7.1/kor/General Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_7.1/kor/iLoader User's Manual.md`
- `Manuals/Altibase_7.3/kor/iLoader User's Manual.md`
- `Manuals/Altibase_trunk/kor/iLoader User's Manual.md`
- `GPTs/attachments/02_administration_operations.md`
- `GPTs/attachments/03_sql_ddl_generation.md`
- `GPTs/attachments/06_data_dictionary_performance_views.md`
- `GPTs/attachments/13_isql_iloader_basic_tools.md`
- `GPTs/reports/gap_register.md`
- `GPTs/reports/coverage_matrix.md`

J028 adds no new attachment filename, source family, or Korean/English source-drift
case. It narrows `GAP-J002-018` for the backup/recovery workflow slice by replacing
high-risk source workflow tables and examples with searchable English runbook steps,
copy-ready SQL/command examples, archive/log-anchor stop conditions, and view-backed
validation hooks. No new manual/source-backed gap was discovered during the scoped
backup, archive, log-anchor, and incremental-backup review.

## J029 Restore Recovery And Media Failure Runbook Addendum

J029 uses the `administrator_operations`, `sql_reference`, and
`general_reference_2_dictionary_views` source families for Altibase 7.1, Altibase 7.3,
and the Altibase 8.1 verified source. Korean Administrator and SQL Reference manuals
remain authoritative for complete and incomplete media recovery, incremental restore
and recovery, selected tablespace restore grammar, disk datafile recreation, temporary
file recreation, memory checkpoint image recovery, `META RESETLOGS`, and log-anchor
handling; matching English manuals remain extraction aids only when consistent.

Design note: J029 keeps the 20-file attachment boundary unchanged and expands
`GPTs/attachments/02_administration_operations.md` rather than creating a separate
recovery file. The recovery section now uses a triage-and-runbook structure: recovery
planning inputs, stop conditions, complete/incomplete/incremental decision blocks,
SQL-driven selected-tablespace restore, complete recovery from online backup,
DBA-copied tablespace restore, lost disk datafile recovery with or without a backup
copy, temporary file recreation, memory checkpoint image recovery, past-time recovery,
and `UNTIL CANCEL` recovery. `GPTs/attachments/03_sql_ddl_generation.md` already
contains the source-audited recovery and restore grammar, so J029 did not change it.

Scoped source paths checked for J029:

- `Manuals/Altibase_7.1/kor/Administrator's Manual.md`
- `Manuals/Altibase_7.3/kor/Administrator's Manual.md`
- `Manuals/Altibase_trunk/kor/Administrator's Manual.md`
- `Manuals/Altibase_7.1/kor/SQL Reference.md`
- `Manuals/Altibase_7.3/kor/SQL Reference.md`
- `Manuals/Altibase_trunk/kor/SQL Reference.md`
- `Manuals/Altibase_trunk/eng/Administrator’s Manual.md`
- `Manuals/Altibase_trunk/eng/SQL Reference.md`
- `GPTs/attachments/02_administration_operations.md`
- `GPTs/attachments/03_sql_ddl_generation.md`
- `GPTs/attachments/06_data_dictionary_performance_views.md`
- `GPTs/reports/gap_register.md`
- `GPTs/reports/coverage_matrix.md`

J029 adds no new attachment filename, source family, or Korean/English source-drift
case. It narrows `GAP-J002-018` for the restore/media-failure workflow slice by
replacing high-risk manual examples with searchable English recovery inputs, stop
conditions, copy-ready SQL and command examples, and cross-references to SQL generation
and dictionary-view validation. No new manual/source-backed gap was discovered during
the scoped restore, media recovery, incremental restore, tablespace, datafile, or
temporary-file review.

## J030 Administration Tablespace User And Privilege Runbook Addendum

J030 uses the `administrator_operations`, `sql_reference`,
`general_reference_2_dictionary_views`, and `general_reference_1_datatypes_properties`
source families for Altibase 7.1, Altibase 7.3, and the Altibase 8.1 verified source.
Korean Administrator, SQL Reference, and General Reference manuals remain authoritative
for built-in DBA accounts, user creation and alteration, password policy clauses,
tablespace `ACCESS`, role and privilege behavior, tablespace state transitions, undo
tablespace limits, and tablespace metadata backup follow-up; matching English manuals
remain extraction aids only when consistent.

Design note: J030 keeps the 20-file attachment boundary unchanged and expands
`GPTs/attachments/02_administration_operations.md` rather than moving account or
tablespace runbooks into the SQL generation attachment. The administration section now
distinguishes operational workflows from syntax: application schema/runtime account
provisioning, account lock/password/TCP changes, least-privilege grant and revoke
review, user and role retirement, storage model selection, planned tablespace state
changes, undo tablespace capacity expansion, post-tablespace-DDL backup follow-up, and
tablespace access mismatch triage. `GPTs/attachments/03_sql_ddl_generation.md` already
contains the source-audited compact BNF for users, roles, grants, revoke, and
tablespace SQL, so J030 did not change it.

Scoped source paths checked for J030:

- `Manuals/Altibase_7.1/kor/Administrator's Manual.md`
- `Manuals/Altibase_7.3/kor/Administrator's Manual.md`
- `Manuals/Altibase_trunk/kor/Administrator's Manual.md`
- `Manuals/Altibase_7.1/kor/SQL Reference.md`
- `Manuals/Altibase_7.3/kor/SQL Reference.md`
- `Manuals/Altibase_trunk/kor/SQL Reference.md`
- `Manuals/Altibase_7.1/kor/General Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_7.1/kor/General Reference-1.Data Types & Altibase Properties.md`
- `Manuals/Altibase_7.3/kor/General_Reference-1.Data Types & Altibase Properties.md`
- `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
- `GPTs/attachments/02_administration_operations.md`
- `GPTs/attachments/03_sql_ddl_generation.md`
- `GPTs/attachments/06_data_dictionary_performance_views.md`
- `GPTs/reports/gap_register.md`
- `GPTs/reports/coverage_matrix.md`

J030 adds no new attachment filename, source family, or Korean/English source-drift
case. It narrows `GAP-J002-018` for the administration/tablespace lifecycle slice by
representing account, privilege, storage, and tablespace operational workflows as
searchable English runbooks with copy-ready SQL, source-backed safety notes, and
view-backed validation hooks. No new manual/source-backed gap was discovered during the
scoped administration, user, privilege, storage, or tablespace lifecycle review.

## J031 Replication Topology State And Compatibility Addendum

J031 uses the `replication_manual`, `release_notes_platform`,
`technical_documents_support`, `general_reference_2_dictionary_views`, and
`patch_notes` source families for Altibase 7.1, Altibase 7.3, and the Altibase 8.1
verified source. Korean Replication Manuals, Korean 8.1 release notes, Korean
Replication Compatibility technical notes, and Korean 7.1 patch notes remain
authoritative for target eligibility, conflict behavior, mode restrictions,
receive-only patch evidence, and replication backward-compatibility wording; matching
English manuals remain extraction aids only when consistent.

Design note: J031 keeps the 20-file attachment boundary unchanged and expands
`GPTs/attachments/09_replication_ha_cdc.md` rather than moving replication behavior into
the SQL generation or dictionary attachments. The replication attachment now has
searchable blocks for Active-Active conflict handling, target object and column
eligibility, partition/storage/platform compatibility, mode and optional-feature
compatibility, receive-only patch/meta-version checks, and 8.1 LAZY backward
compatibility direction. `GPTs/attachments/06_data_dictionary_performance_views.md`
only received a retrieval polish update that adds `V$REPSYNC` to the fast replication
runtime row; detailed view coverage was already present.

Scoped source paths checked for J031:

- `Manuals/Altibase_7.1/kor/Replication Manual.md`
- `Manuals/Altibase_7.3/kor/Replication Manual.md`
- `Manuals/Altibase_trunk/kor/Replication Manual.md`
- `Manuals/Altibase_7.1/eng/Replication Manual.md`
- `Manuals/Altibase_7.3/eng/Replication Manual.md`
- `Manuals/Altibase_trunk/eng/Replication Manual.md`
- `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`
- `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`
- `PatchNotes/Altibase_7.1/kor/Altibase_7_1_0_8_5_Patch_Notes.md`
- `Technical Documents/kor/ReplicationCompatibility.md`
- `Technical Documents/kor/Replication network check.md`
- `GPTs/attachments/09_replication_ha_cdc.md`
- `GPTs/attachments/06_data_dictionary_performance_views.md`
- `GPTs/reports/gap_register.md`
- `GPTs/reports/coverage_matrix.md`

J031 adds no new attachment filename, source family, or Korean/English source-drift
case. It closes the receive-only patch/meta-version documentation gap for the scoped
7.1/7.3/8.1 replication slice and narrows the 8.1 compatibility guardrail: the
attachment can now answer lower-version Sender to higher-version Receiver LAZY
compatibility from source-backed protocol checks, while still refusing unsupported
8.1 Sender to older Receiver, 8.1 SSL cross-version, EAGER, offline, and optional-feature
compatibility claims without exact source confirmation.

## J032 Replication Operations CDC Log Analyzer And RepMgr Addendum

J032 uses the `replication_manual`, `log_analyzer`, `replication_manager`,
`general_reference_1_datatypes_properties`, and
`general_reference_2_dictionary_views` source families for Altibase 7.1, Altibase 7.3,
and the Altibase 8.1 verified source. Korean Replication Manuals remain authoritative
for `SYNC`, `SYNC ONLY`, `START`, `QUICKSTART`, `STOP`, `RESET`, `FLUSH`, EAGER
failback, and offline-operational wording. Korean Log Analyzer manuals remain
authoritative for XLog Collector API order, ACK/Restart SN behavior, control XLog
handling, collector status fields, and unsupported CDC transport. Korean Replication
Manager manuals and Korean Replication Manager release notes remain authoritative for
GUI workflow boundaries, pane/object actions, JDBC driver import, extra host IP,
full-mesh impact, and high-risk `Quick Start` warnings.

Design note: J032 keeps the 20-file attachment boundary unchanged and expands
`GPTs/attachments/09_replication_ha_cdc.md` because replication operations, CDC, Log
Analyzer, and Replication Manager are already owned by attachment 09. The update adds
searchable workflow blocks for synchronization retries, `REPLICATION_SYNC_TUPLE_COUNT`
conflict handling, EAGER failback incremental/normal sync behavior, Replication Manager
inspection/create/edit/drop flows, and Log Analyzer ACK/restart/status/control-XLog
handling. `GPTs/attachments/14_utilities_operation_tools.md` remains a cross-reference
target for `altiComp` mismatch comparison and generic tool routing, not the main home
for Replication Manager runbooks.

Scoped source paths checked for J032:

- `Manuals/Altibase_7.1/kor/Replication Manual.md`
- `Manuals/Altibase_7.3/kor/Replication Manual.md`
- `Manuals/Altibase_trunk/kor/Replication Manual.md`
- `Manuals/Altibase_7.1/kor/Log Analyzer User's Manual.md`
- `Manuals/Altibase_7.3/kor/Log Analyzer User's Manual.md`
- `Manuals/Altibase_trunk/kor/Log Analyzer User's Manual.md`
- `Manuals/Tools/Altibase_release/kor/Replication Manager User's Manual.md`
- `Manuals/Tools/Altibase_trunk/kor/Replication Manager User's Manual.md`
- `ReleaseNotes/kor/Altibase_Replication_Manager_1_2_Release_Notes.md`
- `ReleaseNotes/kor/Altibase_Replication_Manager_1_3_Release_Notes.md`
- `ReleaseNotes/kor/Altibase_Replication_Manager_1_4_Release_Notes.md`
- `Manuals/Altibase_7.1/kor/General Reference-1.Data Types & Altibase Properties.md`
- `Manuals/Altibase_7.3/kor/General_Reference-1.Data Types & Altibase Properties.md`
- `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
- `Manuals/Altibase_7.1/kor/General Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`
- `GPTs/attachments/09_replication_ha_cdc.md`
- `GPTs/attachments/14_utilities_operation_tools.md`
- `GPTs/reports/gap_register.md`
- `GPTs/reports/coverage_matrix.md`

J032 adds no new attachment filename, source family, or Korean/English source-drift
case. No new item-level manual/source-backed gap was discovered. The existing
`GAP-J002-011` Replication Manager package-manifest guardrail remains because the
selected source set supports package/runtime prerequisites and release-note caveats but
does not provide a stable manifest for every distribution.

## J033 Network Checks SSL TLS And Replication SSL Addendum

J033 uses the `replication_manual`, `security_ssl_tls`,
`general_reference_1_datatypes_properties`, `general_reference_2_dictionary_views`,
`release_notes_platform`, and `technical_documents_support` source families for
Altibase 7.1, Altibase 7.3, and the Altibase 8.1 verified source. Korean SSL/TLS
guides remain authoritative for ordinary server/client SSL/TLS setup, certificate
properties, client trust/verification keys, OpenSSL/JRE requirements, session
monitoring, and TCP access restrictions. Korean Replication Manual, Korean SQL
Reference, Korean General Reference property material, Korean 8.1 release notes, and
the Korean replication network-check note remain authoritative for replication
transport ports, `USING SSL`, `REPLICATION_SSL_PORT_NO`, Log Analyzer SSL/IB
exclusion, Sender/Receiver endpoint checks, and packet-capture troubleshooting.

Design note: J033 keeps the 20-file attachment boundary unchanged. Replication network
and transport diagnostics stay in `GPTs/attachments/09_replication_ha_cdc.md`; ordinary
client/server TLS, certificate handling, port separation, and replication SSL security
guardrails stay in `GPTs/attachments/18_security_ssl_tls.md`. The update does not move
property catalog ownership out of `GPTs/attachments/05_data_types_properties.md` or
error-code ownership out of `GPTs/attachments/07_error_messages_troubleshooting.md`;
those files remain cross-reference targets.

Scoped source paths checked for J033:

- `Manuals/Altibase_7.1/kor/Altibase SSL TLS User's Guide.md`
- `Manuals/Altibase_7.3/kor/Altibase SSL TLS User's Guide.md`
- `Manuals/Altibase_trunk/kor/Altibase SSL TLS User's Guide.md`
- `Manuals/Altibase_trunk/kor/Replication Manual.md`
- `Manuals/Altibase_trunk/kor/SQL Reference.md`
- `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
- `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`
- `Technical Documents/kor/Replication network check.md`
- `GPTs/attachments/09_replication_ha_cdc.md`
- `GPTs/attachments/18_security_ssl_tls.md`
- `GPTs/reports/gap_register.md`
- `GPTs/reports/coverage_matrix.md`

J033 adds no new attachment filename, source family, or Korean/English source-drift
case. No new item-level manual/source-backed gap was discovered. The existing
mixed-version 8.1 replication SSL compatibility guardrail remains because no selected
source provides an 8.1-to-older replication SSL compatibility matrix. The live TLS and
connector integration guardrail also remains because this job expanded source-backed
certificate and port diagnostics, but did not perform live handshakes against customer
environments.

## J034 PSM Stored And External Procedures Addendum

J034 uses the `stored_external_procedures`, `sql_reference`,
`general_reference_1_datatypes_properties`, and
`general_reference_2_dictionary_views` source families for Altibase 7.1, Altibase 7.3,
and the Altibase 8.1 verified source. Korean Stored Procedures Manuals remain
authoritative for PSM blocks, packages, VARRAY, user-defined types, pragmas, package
initialization, and built-in package boundaries. Korean External Procedures Manuals
remain authoritative for external C/C++ library deployment, `entryfunction`, mode
selection, `PARAMETERS`, type mapping, and external-agent diagnostics. Korean SQL
Reference manuals remain authoritative for trigger DDL, trigger PSM body restrictions,
`IF EXISTS` and `IF NOT EXISTS` version boundaries, and LOB/replication trigger
cautions. Korean General Reference manuals remain authoritative for PSM, package,
trigger, external library, property, and performance-view validation SQL.

Design note: J034 keeps the 20-file attachment boundary unchanged. PSM object syntax,
trigger PSM body rules, package usage, VARRAY behavior, and external procedure
deployment stay in `GPTs/attachments/10_psm_stored_external_procedures.md`. Broader
schema-object DDL generation remains owned by `GPTs/attachments/03_sql_ddl_generation.md`;
property catalog details remain owned by `GPTs/attachments/05_data_types_properties.md`;
dictionary/performance-view detail remains owned by
`GPTs/attachments/06_data_dictionary_performance_views.md`.

Scoped source paths checked for J034:

- `Manuals/Altibase_7.1/kor/Stored Procedures Manual.md`
- `Manuals/Altibase_7.3/kor/Stored Procedures Manual.md`
- `Manuals/Altibase_trunk/kor/Stored Procedures Manual.md`
- `Manuals/Altibase_7.1/kor/External Procedures Manual.md`
- `Manuals/Altibase_7.3/kor/External Procedures Manual.md`
- `Manuals/Altibase_trunk/kor/External Procedures Manual.md`
- `Manuals/Altibase_7.1/kor/SQL Reference.md`
- `Manuals/Altibase_7.3/kor/SQL Reference.md`
- `Manuals/Altibase_trunk/kor/SQL Reference.md`
- `Manuals/Altibase_7.1/kor/General Reference-1.Data Types & Altibase Properties.md`
- `Manuals/Altibase_7.3/kor/General_Reference-1.Data Types & Altibase Properties.md`
- `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
- `Manuals/Altibase_7.1/kor/General Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md`
- `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`
- `ReleaseNotes/kor/Altibase_7_3_0_0_1_Release_Notes.md`
- `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`
- `GPTs/attachments/10_psm_stored_external_procedures.md`
- `GPTs/attachments/03_sql_ddl_generation.md`
- `GPTs/attachments/05_data_types_properties.md`
- `GPTs/attachments/06_data_dictionary_performance_views.md`
- `GPTs/reports/gap_register.md`
- `GPTs/reports/coverage_matrix.md`

J034 adds no new attachment filename, source family, or Korean/English source-drift
case. No new item-level manual/source-backed gap was discovered. The existing PSM and
external procedure compile/runtime verification limit remains because this job expanded
source-backed BNF, examples, and diagnostics but did not compile PSM objects, build
C/C++ shared libraries, load `$ALTIBASE_HOME/lib` files, or execute an Altibase server
test.

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

Source purpose: PSM, stored procedures/functions, triggers, external procedures, PL/SQL compatibility notes.

- 7.1:
  - `Manuals/Altibase_7.1/eng/Stored Procedures Manual.md`
  - `Manuals/Altibase_7.1/eng/External Procedures Manual.md`
  - `Manuals/Altibase_7.1/eng/SQL Reference.md`
  - `Manuals/Altibase_7.1/eng/General Reference-1.Data Types & Altibase Properties.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/Stored Procedures Manual.md`
  - `Manuals/Altibase_7.3/eng/External Procedures Manual.md`
  - `Manuals/Altibase_7.3/eng/SQL Reference.md`
  - `Manuals/Altibase_7.3/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `ReleaseNotes/eng/Altibase_7_3_0_0_1_Release_Notes.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/Stored Procedures Manual.md`
  - `Manuals/Altibase_trunk/eng/External Procedures Manual.md`
  - `Manuals/Altibase_trunk/eng/SQL Reference.md`
  - `Manuals/Altibase_trunk/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`
- Korean source authority/check:
  - `Manuals/Altibase_7.1/kor/Stored Procedures Manual.md`
  - `Manuals/Altibase_7.1/kor/External Procedures Manual.md`
  - `Manuals/Altibase_7.1/kor/SQL Reference.md`
  - `Manuals/Altibase_7.1/kor/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_7.3/kor/Stored Procedures Manual.md`
  - `Manuals/Altibase_7.3/kor/External Procedures Manual.md`
  - `Manuals/Altibase_7.3/kor/SQL Reference.md`
  - `Manuals/Altibase_7.3/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `ReleaseNotes/kor/Altibase_7_3_0_0_1_Release_Notes.md`
  - `Manuals/Altibase_trunk/kor/Stored Procedures Manual.md`
  - `Manuals/Altibase_trunk/kor/External Procedures Manual.md`
  - `Manuals/Altibase_trunk/kor/SQL Reference.md`
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
- J035 design note: `11_java_jdbc_spring.md` remains the Java/JDBC/Spring/Adapter
  packaging file; no attachment boundary or file-name change was required. J035
  expanded item-block coverage from Korean JDBC and Adapter manuals, Korean
  Spring/Hibernate guides, and `Technical Documents/kor/JavaCompatibility.md` with
  driver jar selection, patch-sensitive Java compatibility cautions, additional
  connection attributes, failover grammar and retry handling, validation-query rules,
  Spring/Hibernate examples, Altibase-specific Java APIs, and Adapter platform/version
  boundaries. J035 did not perform live JDBC, Spring, Hibernate, or `jdbcAdapter`
  execution tests, so runtime examples remain source-backed documentation examples.

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
