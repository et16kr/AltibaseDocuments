# Full Coverage Audit Remediation Log

- Workflow: `altibase-gpt-full-coverage-audit`
- Initialized by: `FCA-J003`
- Status: Active log for later FCA remediation jobs

## Log Contract

Every later job that changes attachments, GPT instructions, support reports, catalog
rows, matrix rows, or registers should add a concise entry here.

Each entry should include:

- job ID;
- changed files;
- affected `source_item_id` values or register entries;
- source evidence;
- coverage status changes;
- validation commands and results;
- skipped checks or residual risk.

## Entries

### FCA-J003

- Changed files: initialized full coverage audit schema, TSV headers, registers, final
  report placeholder, and reusable script tooling under
  `GPTs/reports/full_coverage_audit/`.
- Product coverage changes: none. This job does not catalog source items or remediate
  customer-facing attachments.
- Evidence: `AGENTS.md`, `source_corpus_lock.md`, `coverage_matrix.md`,
  `source_inventory.md`, `gap_register.md`, `catalog_schema_extraction_rules.md`, and
  latest locked benchmark artifacts under
  `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_205641/`.
- Validation: `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers`
  passed with 0 catalog rows and 0 matrix rows; `git diff --check` passed;
  `bash review/scripts/run_review_stage.sh validate` passed with 20 upload attachments;
  `rg -n "^Verdict:|^\| (Blocker|High|Medium|Low) \|" review/reports/R*.md` showed
  `Verdict: Pass` for R00-R27 and no actionable severity rows.
- Residual risk: item-level catalog rows, matrix rows, and final dispositions remain
  assigned to later FCA jobs.

### FCA-J004

- Changed files: `source_item_catalog.tsv`, `missing_item_register.md`, `guardrail_register.md`, `retrieval_weakness_register.md`, and this remediation log.
- Product coverage changes: cataloged release/platform/patch source rows only; no customer-facing attachment text was changed and no original source documents were edited.
- Catalog totals added by this job: 165 rows total; 16 `Covered`, 15 `Covered-by-routing`, 128 `Missing`, 5 `Guardrail`, 1 `Out-of-scope`, and 0 `Retrieval-weak`.
- Source evidence: Korean Altibase 7.1/7.3/8.1 release notes, Korean `Technical Documents/kor/Supported Platforms.md`, and selected Korean 7.1/7.3 patch notes under `PatchNotes/Altibase_7.1/kor` and `PatchNotes/Altibase_7.3/kor`.
- Coverage status changes: exact release/platform rows already represented in `00_version_release_platform.md` were marked `Covered` or `Covered-by-routing`; exact patch-note change-set rows and older tool-release boundaries absent from answer-ready attachments were registered as `Missing`; unlisted platform support, release-note-only procedure scope, Shard/Windows2026 release notes without a selected owner, and 6.5.1 platform rows were registered as guardrail or out-of-scope rows.
- Validation: `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers` passed with 165 catalog rows and 0 matrix rows; ASCII hygiene scan passed; `git diff --check` passed; `bash review/scripts/run_review_stage.sh validate` passed with 20 upload attachments; review-report severity scan showed `Verdict: Pass` for R00-R27 and no actionable severity rows.
- Residual risk: patch notes are cataloged at patch-file change-set granularity with all `BUG-*` tokens preserved in `literal_tokens`; later matrix/remediation work may split high-priority patch files into per-BUG rows before closing exact patch answerability gaps.

### FCA-J005

- Changed files: `source_item_catalog.tsv`, `missing_item_register.md`,
  `guardrail_register.md`, and this remediation log.
- Product coverage changes: cataloged Getting Started and Installation manual rows only;
  no customer-facing attachment text was changed and no original source documents were
  edited.
- Catalog totals added by this job: 40 rows total; 27 `Covered`, 7
  `Covered-by-routing`, 4 `Missing`, 2 `Guardrail`, 0 `Out-of-scope`, and 0
  `Retrieval-weak`.
- Source evidence: Korean Altibase 7.1/7.3/8.1 Getting Started Guides and Installation
  Guides, with matching English manuals used as extraction aids where consistent.
- Coverage status changes: installation, environment setup, database creation, startup,
  shutdown, client install, patch rollback, meta downgrade, first-run checks, and
  broad getting-started overview topics were mapped to answer-ready attachment anchors
  or routing targets. Missing rows were registered for the exact `70KB` client stack
  size, APatch file inventory, full-versus-patch step matrix, and full-uninstall/profile
  cleanup runbook. Guardrails were registered for live package download availability
  and license acquisition/entitlement.
- Validation: `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers`
  passed with 205 catalog rows and 0 matrix rows; `git diff --check` passed;
  `bash review/scripts/run_review_stage.sh validate` passed with 20 upload
  attachments; review-report severity scan showed `Verdict: Pass` for R00-R27 and no
  actionable severity rows.
- Residual risk: later remediation jobs must close or route the four new `Missing`
  rows before final full-coverage readiness can have no unresolved `Missing`
  dispositions.

### FCA-J006

- Changed files: `source_item_catalog.tsv`, `missing_item_register.md`, and this
  remediation log.
- Product coverage changes: cataloged Administrator manual backup, recovery, archive
  log, storage, server-mode, media-failure, and protected-operation rows only; no
  customer-facing attachment text was changed and no original source documents were
  edited.
- Catalog totals added by this job: 34 rows total; 29 `Covered`, 3
  `Covered-by-routing`, 2 `Missing`, 0 `Guardrail`, 0 `Out-of-scope`, and 0
  `Retrieval-weak`.
- Source evidence: Korean Altibase 7.1/7.3 Administrator manuals and the Altibase 8.1
  verified-source Korean Administrator manual, with existing attachment anchors in
  `02_administration_operations.md`, `03_sql_ddl_generation.md`,
  `06_data_dictionary_performance_views.md`, `13_isql_iloader_basic_tools.md`, and
  `01_getting_started_installation.md`.
- Coverage status changes: startup/server phases, shutdown, log-anchor and physical
  file evidence, backup-policy choices, archive-log mode, online/offline backup,
  media-recovery variants, incomplete recovery and `RESETLOGS`, replication recovery
  cautions, snapshot backup, incremental backup/restore, backup-file management, disk
  usage/archive-full handling, and 8.1 checkpoint-scale handling were mapped to
  answer-ready attachment anchors or routing targets. Missing rows were registered for
  detailed disk tablespace physical/logical structure and detailed memory/volatile
  tablespace structure.
- Validation: `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers`
  passed with 239 catalog rows and 0 matrix rows; `git diff --check` passed;
  `bash review/scripts/run_review_stage.sh validate` passed with 20 upload
  attachments; review-report severity scan showed `Verdict: Pass` for R00-R27 and no
  actionable severity rows.
- Residual risk: later remediation jobs must close or route the two new Administrator
  storage-structure `Missing` rows before final full-coverage readiness can have no
  unresolved `Missing` dispositions.

### FCA-J007

- Changed files: `source_item_catalog.tsv`, `missing_item_register.md`, and this
  remediation log.
- Product coverage changes: cataloged Administrator and SQL Reference rows for
  tablespaces, datafiles, users, roles, privileges, accounts, schema administration,
  and validation checks only; no customer-facing attachment text was changed and no
  original source documents were edited.
- Catalog totals added by this job: 29 rows total; 27 `Covered`, 0
  `Covered-by-routing`, 2 `Missing`, 0 `Guardrail`, 0 `Out-of-scope`, and 0
  `Retrieval-weak`.
- Source evidence: Korean Altibase 7.3 Administrator manual, Korean Altibase 7.3 SQL
  Reference, and Altibase 8.1 verified-source Korean SQL Reference for idempotent
  user and tablespace syntax, checked against existing anchors in
  `02_administration_operations.md`, `03_sql_ddl_generation.md`, and
  `06_data_dictionary_performance_views.md`.
- Coverage status changes: system-created accounts, user DDL workflow, role and
  grant/revoke syntax, object privilege support, tablespace classification, disk and
  undo space management, planned tablespace state changes, checkpoint-path
  operations, volatile tablespace lifecycle, tablespace monitoring views, tablespace
  DDL, file-size cautions, and 8.1-only `IF EXISTS`/`IF NOT EXISTS` boundaries were
  mapped to answer-ready attachment anchors. Missing rows were registered for the
  complete schema versus non-schema object taxonomy and the complete system privilege
  catalog.
- Validation: `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers`
  passed with 268 catalog rows and 0 matrix rows; `git diff --check` passed;
  `bash review/scripts/run_review_stage.sh validate` passed with 20 upload
  attachments; review-report severity scan showed `Verdict: Pass` for R00-R27 and no
  actionable severity rows.
- Residual risk: later remediation jobs must close or route the two new Administrator
  privilege and schema-taxonomy `Missing` rows before final full-coverage readiness
  can have no unresolved `Missing` dispositions.

### FCA-J008

- Changed files: `source_item_catalog.tsv`, `missing_item_register.md`, and this
  remediation log.
- Product coverage changes: cataloged Korean SQL Reference DDL rows for table,
  partition, constraint, LOB storage, queue, index, and table-maintenance grammar; no
  customer-facing attachment text was changed and no original source documents were
  edited. Existing `FCA-J007` rows already cover the overlapping tablespace/datafile
  DDL rows `SRC-SQL-XVER-000009` through `SRC-SQL-XVER-000012` and
  `SRC-SQL-8.1-000001`.
- Catalog totals added by this job: 27 rows total; 23 `Covered`, 4 `Missing`, 0
  `Covered-by-routing`, 0 `Guardrail`, 0 `Out-of-scope`, and 0 `Retrieval-weak`.
- Source evidence: Korean Altibase 7.1, 7.3, and Altibase 8.1 verified-source SQL
  Reference manuals, checked against existing answer-ready anchors in
  `GPTs/attachments/03_sql_ddl_generation.md` and related dictionary routing where
  applicable.
- Coverage status changes: core `CREATE TABLE`, `ALTER TABLE`, partition, LOB storage,
  queue, `ENQUEUE`/`DEQUEUE`, `CREATE INDEX`, `ALTER INDEX`, `DROP INDEX`, table
  maintenance, conjoin/disjoin, and 8.1-only idempotent table/index/queue clauses were
  mapped to covered attachment anchors. Missing rows were registered for the exact
  `table_compression_clause` type/minimum-size matrix, the `ALTER TABLE MODIFY COLUMN`
  conversion matrix, full `COMMENT ON` limit/delete behavior, and the direct-key
  supported type/`MAXSIZE` matrix.
- Validation: `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers`
  passed with 295 catalog rows and 0 matrix rows; scoped ASCII hygiene scan passed;
  `git diff --check` passed; `bash review/scripts/run_review_stage.sh validate`
  passed with 20 upload attachments; review-report severity scan showed
  `Verdict: Pass` for R00-R27 and no actionable severity rows.
- Residual risk: later remediation jobs must close or route the four new SQL DDL
  `Missing` rows before final full-coverage readiness can have no unresolved
  `Missing` dispositions.

### FCA-J009

- Changed files: `source_item_catalog.tsv`, `missing_item_register.md`, and this
  remediation log.
- Product coverage changes: cataloged SQL Reference DCL/admin/destructive SQL,
  replication SQL, Log Analyzer SQL, and privilege safety-boundary rows only; no
  customer-facing attachment text was changed and no original source documents were
  edited. Existing `FCA-J007` rows remain the owner for base `CREATE USER`,
  `ALTER USER`, `DROP USER`, `CREATE ROLE`, `DROP ROLE`, `GRANT`, `REVOKE`, and
  complete system-privilege catalog coverage.
- Catalog totals added by this job: 21 rows total; 18 `Covered`, 2
  `Covered-by-routing`, 1 `Missing`, 0 `Guardrail`, 0 `Out-of-scope`, and 0
  `Retrieval-weak`.
- Source evidence: Korean Altibase 7.3 SQL Reference DDL/DCL statement
  classification, `ALTER SYSTEM`, `ALTER SESSION`, transaction control, audit
  control, `CREATE/ALTER/DROP REPLICATION`, destructive SQL, and privilege sections;
  Korean Altibase 7.3 Replication Manual lifecycle, receive-only, DDL replication, and
  SQL Apply Mode sections; Korean Altibase 7.3 Log Analyzer manual XLog Sender SQL;
  and Altibase 8.1 verified-source Korean SQL Reference syntax for replication
  idempotency, SSL replication, and `ALTER SESSION SET FREE TEMPORARY LOB`.
- Coverage status changes: DCL classification, system/session/transaction controls,
  audit-control syntax, destructive operation routing, replication create/alter/drop
  syntax, DDL replication and SQL Apply Mode runbook items, receive-only and host
  maintenance boundaries, Log Analyzer XLog Sender SQL, and 8.1-only replication and
  Temporary LOB session syntax were mapped to existing answer-ready attachment
  anchors. One new `Missing` row was registered for the exact audit operation and
  object-audit support matrix, because the attachment has generic audit placeholders
  and examples but not the complete source-backed matrix.
- Validation: `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers`
  passed with 316 catalog rows and 0 matrix rows; `git diff --check` passed;
  `bash review/scripts/run_review_stage.sh validate` passed with 20 upload
  attachments; review-report severity scan showed `Verdict: Pass` for R00-R27 and no
  actionable severity rows.
- Residual risk: later remediation jobs must close or route
  `SRC-SQL-XVER-000043` before final full-coverage readiness can have no unresolved
  `Missing` dispositions.

### FCA-J010

- Changed files: `source_item_catalog.tsv` and this remediation log.
- Product coverage changes: cataloged SQL Reference DML, predicate, expression,
  operator, regular-expression, object-name, and non-JSON built-in-function rows
  only; no customer-facing attachment text was changed and no original source
  documents were edited. JSON, LOB, and broader Oracle-difference rows remain scoped
  to FCA-J011.
- Catalog totals added by this job: 37 rows total; 26 `Covered`, 11
  `Covered-by-routing`, 0 `Missing`, 0 `Guardrail`, 0 `Out-of-scope`, and 0
  `Retrieval-weak`.
- Source evidence: Korean Altibase 7.3 SQL Reference statement, object-name, DML,
  condition, expression/operator, regular-expression, and SQL-function sections;
  Korean Altibase 7.1 SQL Reference for the 7.1.0.7.7 PCRE2 boundary; and Altibase
  8.1 verified-source Korean SQL Reference checks for version-sensitive function
  evidence, checked against existing answer-ready anchors in
  `GPTs/attachments/04_sql_dml_oracle_compatibility.md`.
- Coverage status changes: DML classification, object-name rules,
  SELECT/INSERT/UPDATE/DELETE/MOVE/MERGE/RETURNING, set operators,
  expression/operator rules, logical/comparison/membership/pattern conditions,
  REGEXP_MODE and PCRE2 routing, non-JSON function family inventories, exact syntax
  blocks for ordered-set/statistical/window/conditional/regex functions,
  ROWNUM/sequence notes, queue DML, and DML hint routing were mapped to existing
  attachment anchors.
- Validation: `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers`
  passed with 353 catalog rows and 0 matrix rows; scoped TSV required-cell,
  duplicate-ID, status, version-scope, and guardrail-reason checks passed;
  `git diff --check` passed; `bash review/scripts/run_review_stage.sh validate`
  passed with 20 upload attachments; review-report severity scan showed
  `Verdict: Pass` for R00-R27 and no actionable severity rows.
- Residual risk: this job intentionally did not catalog JSON, LOB, or broader
  Oracle-difference rows because FCA-J011 owns those. No new `Missing` or
  `Retrieval-weak` rows were added by FCA-J010.

### FCA-J011

- Changed files: `source_item_catalog.tsv`, `missing_item_register.md`, and this
  remediation log.
- Product coverage changes: cataloged SQL Reference JSON functions and `IS JSON`,
  General Reference 1 JSON data type, Temporary LOB, LOB storage modifier rules,
  Oracle outer-join and semi/anti-join compatibility, and LOB helper functions only;
  no customer-facing attachment text was changed and no original source documents
  were edited.
- Catalog totals added by this job: 15 rows total; 12 `Covered`, 1
  `Covered-by-routing`, 2 `Missing`, 0 `Guardrail`, 0 `Out-of-scope`, and 0
  `Retrieval-weak`.
- Source evidence: Korean Altibase 8.1 verified-source SQL Reference JSON function
  and `IS JSON` sections; Korean Altibase 8.1 verified-source General Reference 1
  JSON type and Temporary LOB sections; Korean Altibase 7.3 General Reference 1
  `FIXED`, `VARIABLE`, `IN ROW`, `BLOB`, and `CLOB` sections; Korean Altibase 7.1,
  7.3, and 8.1 verified-source SQL Reference `EMPTY_BLOB` and `EMPTY_CLOB`
  sections; and Korean Altibase 7.3 SQL Reference join sections.
- Coverage status changes: JSON type and path-expression restrictions, Temporary
  LOB lifecycle and checks, storage modifier rules, individual JSON function syntax
  and defaults, `IS JSON`, SQL/JSON migration routing, and Oracle-style outer join
  routing were mapped to existing answer-ready anchors. Two new `Missing` rows were
  registered because `TO_CLOB`/`TO_BLOB` and `EMPTY_BLOB`/`EMPTY_CLOB` are only
  indexed or mentioned in lifecycle lists, not represented as answer-ready function
  blocks.
- Validation: `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers`
  passed with 368 catalog rows and 0 matrix rows; `git diff --check` passed;
  `bash review/scripts/run_review_stage.sh validate` passed with 20 upload
  attachments; review-report severity scan showed `Verdict: Pass` for R00-R27 and no
  actionable severity rows.
- Residual risk: later remediation jobs must close or route `SRC-SQL-8.1-000015`
  and `SRC-SQL-XVER-000089` before final full-coverage readiness can have no
  unresolved `Missing` dispositions.

### FCA-J012

- Changed files: `source_item_catalog.tsv`, `missing_item_register.md`, and this
  remediation log.
- Product coverage changes: cataloged General Reference 1 data-type overview,
  storage-size formulas, NULL semantics, implicit and explicit conversion rules,
  string-literal notation, scalar type items, numeric and date format model elements,
  binary types, LOB overview and restrictions, GEOMETRY routing, 8.1 Temporary LOB
  examples, 8.1 JSON path examples, and the 7.1 LOB `NOT NULL` caution only; no
  customer-facing attachment text was changed and no original source documents were
  edited.
- Catalog totals added by this job: 34 rows total; 22 `Covered`, 3
  `Covered-by-routing`, 9 `Missing`, 0 `Guardrail`, 0 `Out-of-scope`, and 0
  `Retrieval-weak`.
- Source evidence: Korean Altibase 7.1, 7.3, and 8.1 verified-source General
  Reference 1 data type chapters were sufficient for this catalog scope. SQL
  Reference-owned direct-key indexing remains under `SRC-SQL-XVER-000035` from
  `FCA-J008`; no duplicate General Reference row was created because the scoped
  General Reference source does not contain the direct-key matrix.
- Coverage status changes: core scalar data types, binary types, BLOB/CLOB,
  LOB restrictions, GEOMETRY routing, LOB API routing, and the 7.1 LOB `NOT NULL`
  caution were mapped to existing attachment anchors or routing anchors. Nine new
  `Missing` rows were registered because the attachments do not yet preserve
  answer-ready storage-size formulas, NULL semantics, implicit/explicit conversion
  rules, string literal quoting, numeric/date format element tables, 8.1 Temporary
  LOB examples, or 8.1 JSON path example/result tables.
- Validation: `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers`
  passed with 402 catalog rows and 0 matrix rows; scoped TSV required-cell,
  duplicate-ID, status, version-scope, and guardrail-reason checks passed;
  `git diff --check` passed; `bash review/scripts/run_review_stage.sh validate`
  passed with 20 upload attachments; review-report severity scan showed
  `Verdict: Pass` for R00-R27 and no actionable severity rows.
- Residual risk: later remediation jobs must close or route the nine new FCA-J012
  `Missing` rows before final full-coverage readiness can have no unresolved
  `Missing` dispositions.

### FCA-J015

- Changed files: `source_item_catalog.tsv`, `missing_item_register.md`, and this
  remediation log.
- Product coverage changes: cataloged General Reference 1 optimizer, normalization,
  lock, timeout, autocommit, session, locale, and performance property rows only; no
  customer-facing attachment text was changed and no original source documents were
  edited. Network, SSL/TLS, replication, and DB Link properties remain scoped to
  `FCA-J016`.
- Catalog totals added by this job: 94 rows total; 54 `Covered`, 40 `Missing`, 0
  `Covered-by-routing`, 0 `Guardrail`, 0 `Out-of-scope`, and 0 `Retrieval-weak`.
- Source evidence: Korean General Reference 1 detailed property sections for Altibase
  7.1, Altibase 7.3, and the Altibase 8.1 verified source, using
  `GPTs/reports/property_inventory.md` as the line-locator baseline and existing
  answer-ready anchors in `GPTs/attachments/05_data_types_properties.md`.
- Coverage status changes: optimizer behavior, `NORMALFORM_MAXIMUM`, result/LOB cache
  routing where scoped, parallel query worker limits, lock escalation, timeouts,
  `AUTO_COMMIT`, `ISOLATION_LEVEL`, `DEFAULT_DATE_FORMAT`, `TIME_ZONE`, NLS locale
  settings, user-lock settings, PSM session resource limits, and XA heuristic settings
  were mapped to existing answer-ready attachment anchors. Forty performance and lock
  properties were registered as `Missing` because the attachment currently preserves
  only inventory-level name/version coverage for those properties.
- Validation: `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers`
  passed with 624 catalog rows and 0 matrix rows; `git diff --check` passed;
  `bash review/scripts/run_review_stage.sh validate` passed with 20 upload
  attachments; review-report severity scan showed `Verdict: Pass` for R00-R27 and no
  actionable severity rows.
- Residual risk: later remediation jobs must close or route the forty new FCA-J015
  `Missing` rows before final full-coverage readiness can have no unresolved
  `Missing` dispositions.

### FCA-J016

- Changed files: `source_item_catalog.tsv`,
  `GPTs/attachments/05_data_types_properties.md`, and this remediation log.
- Product coverage changes: cataloged General Reference 1 account/password,
  administrator access, `ACCESS_LIST`, network/listener/IPC, SSL/TLS, SNMP,
  InfiniBand, replication transport/apply/conflict/recovery, SQL Apply, and DB Link
  property rows only; no original source documents were edited.
- Catalog totals added by this job: 121 rows total; 121 `Covered`, 0 `Missing`,
  0 `Covered-by-routing`, 0 `Guardrail`, 0 `Out-of-scope`, and 0
  `Retrieval-weak`.
- Source evidence: Korean General Reference 1 detailed property sections for
  Altibase 7.1, Altibase 7.3, and the Altibase 8.1 verified source, using
  `GPTs/reports/property_inventory.md` as the line-locator baseline and existing
  answer-ready anchors in `GPTs/attachments/05_data_types_properties.md` plus
  `GPTs/attachments/16_dblink_external_connectors.md`.
- Coverage status changes: `MAX_CLIENT`, listener/IPC ports, all scoped
  `REPLICATION_*` properties including Altibase 8.1-only `REPLICATION_SSL_PORT_NO`,
  `SSL_*`, `SNMP_*`, `IB_*`, `TCP_ENABLE`, `DBLINK_*`, password-aging properties,
  `REMOTE_SYSDBA_ENABLE`, `ADMIN_MODE`, `ACCESS_LIST`, and `ACCESS_LIST_FILE` were
  mapped to existing answer-ready attachment anchors. The account/access attachment
  version-scope note was normalized from 7.3/8.1-only wording to 7.1/7.3/8.1 after
  checking the Korean 7.1, 7.3, and 8.1 source sections.
- Validation: `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers`
  passed with 745 catalog rows and 0 matrix rows; scoped TSV required-cell,
  duplicate-ID, status, version-scope, and guardrail-reason checks passed;
  `git diff --check` passed; `bash review/scripts/run_review_stage.sh validate`
  passed with 20 upload attachments; review-report severity scan showed
  `Verdict: Pass` for R00-R27 and no actionable severity rows.
- Residual risk: no new `Missing`, `Guardrail`, `Out-of-scope`, or
  `Retrieval-weak` rows were added by FCA-J016. Exact production changes for
  replication, SSL/TLS, DB Link, and access-control properties still require the
  customer inputs and installed-server checks recorded in the attachment cautions.

### FCA-J017

- Changed files: `source_item_catalog.tsv`, `guardrail_register.md`, and this remediation log.
- Product coverage changes: cataloged General Reference 2 dictionary/meta-table rows only; no customer-facing attachment text was changed and no original source documents were edited.
- Catalog totals added by this job: 73 rows total; 45 `Covered`, 27 `Covered-by-routing`, 0 `Missing`, 1 `Guardrail`, 0 `Out-of-scope`, and 0 `Retrieval-weak`.
- Source evidence: Korean Altibase 7.1, 7.3, and Altibase 8.1 verified-source General Reference 2 meta-table lists, with the matching English 7.3 General Reference 2 list used only to normalize English summaries.
- Coverage status changes: meta-table access/change/schema safety rules and answer-ready object/cookbook blocks were mapped to `06_data_dictionary_performance_views.md`; inventory-only table-purpose rows were marked `Covered-by-routing`; `SYS_REPL_TABLE_OID_IN_USE_` was registered as a guardrail because of the 7.1/7.3 versus 8.1 source-list conflict.
- Validation: `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers` passed with 818 catalog rows and 0 matrix rows; `git diff --check` passed; `bash review/scripts/run_review_stage.sh validate` passed with 20 upload attachments; the review-report severity scan showed `Verdict: Pass` for R00-R27 and no actionable severity rows.
- Residual risk: this job catalogs meta-table name/purpose coverage. Exhaustive per-column and patch-sensitive dictionary layout proof remains governed by `GAP-J002-006` and installed metadata checks using `SYSTEM_.SYS_TABLES_`, `SYSTEM_.SYS_COLUMNS_`, `V$TABLE`, and `V$ALLCOLUMN`.

### FCA-J018

- Changed files: `source_item_catalog.tsv`, `GPTs/attachments/06_data_dictionary_performance_views.md`, and this remediation log.
- Product coverage changes: cataloged General Reference 2 performance-view operational rows only; original source documents were not edited.
- Catalog totals added by this job: 132 rows total; 2 `Covered`, 130 `Covered-by-routing`, 0 `Missing`, 0 `Guardrail`, 0 `Out-of-scope`, and 0 `Retrieval-weak`.
- Source evidence: Korean Altibase 7.1, 7.3, and Altibase 8.1 verified-source General Reference 2 performance-view lists and operational semantics, with matching English General Reference 2 text used only to normalize customer-facing English summaries where consistent. `dictionary_view_inventory.md` supplied the source-backed grouping and version-availability baseline.
- Coverage status changes: performance-view read-only/query-time semantics and the `SELECT * FROM V$TAB` / `DESC` source query method were mapped to answer-ready attachment text; all per-view name, purpose, version, operational group, query-timing, and safe `V$TABLE` / `V$ALLCOLUMN` check rows were mapped to existing inventory routing and verification SQL. The 7.1-only reserved spatial unit views and 8.1-only `V$MEM_STABLE` / `V$TEMPORARY_LOBS` rows were cataloged as version-specific `Covered-by-routing` entries with installed-metadata checks.
- Validation: `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers` passed with 950 catalog rows and 0 matrix rows; scoped TSV counts confirmed 132 FCA-J018 rows with valid statuses, version scopes, and item types; `git diff --check` passed; `bash review/scripts/run_review_stage.sh validate` passed with 20 upload attachments; the review-report severity scan showed `Verdict: Pass` for R00-R27 and no actionable severity rows.
- Residual risk: this job catalogs view-level operational coverage. Exhaustive per-column and patch-sensitive layout proof remains scoped to later view-column and consolidation jobs, using `V$TABLE`, `V$ALLCOLUMN`, `SYSTEM_.SYS_TABLES_`, and `SYSTEM_.SYS_COLUMNS_` before generating version-sensitive SQL.

### FCA-J019

- Changed files: `source_item_catalog.tsv`, `guardrail_register.md`, and this remediation log.
- Product coverage changes: cataloged General Reference 2 view-column and installed-metadata guardrail rows only; no customer-facing attachment text or original source documents were edited.
- Catalog totals added by this job: 21 rows total; 14 `Covered`, 0 `Covered-by-routing`, 0 `Missing`, 7 `Guardrail`, 0 `Out-of-scope`, and 0 `Retrieval-weak`.
- Source evidence: Korean Altibase 7.1, 7.3, and Altibase 8.1 verified-source General Reference 2 dictionary/performance-view sections for `V$TABLE`, `V$ALLCOLUMN`, `SYS_TABLES_`, `SYS_COLUMNS_`, `V$DATATYPE`, key session/statement/wait/lock/transaction/statistics/storage/replication view columns, and 8.1 `V$LOG.CHECKPOINT_SCALE` / `V$MEM_STABLE`. `dictionary_view_inventory.md` and `gap_register.md` supplied the existing drift and exhaustive-column guardrail context.
- Coverage status changes: key column groups were mapped to existing answer-ready anchors in `06_data_dictionary_performance_views.md`; guardrails were registered for exact performance-view layout, exact `SYS_*` layout, `SYS_REPL_ITEMS_.IS_CONDITION_SYNCED`, 8.1 checkpoint-scale columns, 7.1-only reserved spatial-unit views, replication runtime object-ID resolution, and `V$USAGE` statistics prerequisites.
- Validation: `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers` passed with 971 catalog rows and 0 matrix rows; scoped TSV counts confirmed 21 FCA-J019 rows with 14 `Covered` and 7 `Guardrail` statuses; `git diff --check` passed; `bash review/scripts/run_review_stage.sh validate` passed with 20 upload attachments; the review-report severity scan showed `Verdict: Pass` for R00-R27 and no actionable severity rows.
- Residual risk: exhaustive per-view, per-column proof for every supported patch remains an installed-metadata guardrail, not an unresolved `Missing` or `Retrieval-weak` row from this job.

### FCA-J020

- Changed files: `source_item_catalog.tsv` and this remediation log.
- Product coverage changes: cataloged the `error_message_reference` storage, backup,
  recovery, datafile, log, log-anchor, archive, lock, checkpoint, incremental-backup,
  multiplex-directory, and tablespace exact-code slice only. No customer-facing
  attachment text or original source documents were edited.
- Catalog totals added by this job: 194 rows total; 6 `Covered`, 188
  `Covered-by-routing`, 0 `Missing`, 0 `Guardrail`, 0 `Out-of-scope`, and 0
  `Retrieval-weak`.
- Source evidence: selected Korean Altibase 7.1, Altibase 7.3, and Altibase 8.1
  verified-source Error Message Reference entries were matched by exact reference code
  and symbol. The 7.3 Korean manual is the representative `source_path`; each row's
  evidence records matching 7.1, 7.3, and 8.1 line locators plus the existing
  `07_error_messages_troubleshooting.md` exact-code map or dedicated block line.
- Coverage status changes: dedicated rows were mapped to answer-ready blocks for
  deadlock, lock timeout, tablespace free space, `AUTOEXTEND` off, tablespace not
  found, and tablespace has objects. The remaining scoped entries were mapped to
  existing grouped exact-code blocks for datafile/file-system storage, backup/recovery
  log and `RESETLOGS`, checkpoint/incremental backup/multiplex paths, and tablespace
  state/type/DDL errors.
- Validation: `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers`
  passed with 1165 catalog rows and 0 matrix rows; scoped TSV counts confirmed 194
  FCA-J020 rows with 6 `Covered` and 188 `Covered-by-routing` statuses. Standard
  repository verification passed: `git diff --check`, `bash review/scripts/run_review_stage.sh validate`,
  and the review-report severity scan showed `Verdict: Pass` for R00-R27 and no
  actionable severity rows.
- Residual risk: no new `Missing`, `Guardrail`, `Out-of-scope`, or `Retrieval-weak`
  rows were added by FCA-J020. Exact production recovery or destructive tablespace
  actions still require the customer inputs and stop conditions already recorded in
  `07_error_messages_troubleshooting.md`.

### FCA-J021

- Changed files: `source_item_catalog.tsv` and this remediation log.
- Product coverage changes: cataloged SQL parser, DDL/table/column/data type,
  object-resolution, privilege, constraint, conversion/literal/date, regular-expression,
  LOB, JSON, and Temporary LOB exact-code rows from the selected Error Message
  Reference family only; no customer-facing attachment text or original source
  documents were edited.
- Catalog rows touched by this job: 155 rows total; 154 added and 1 updated. Status split: 3 `Covered`, 152 `Covered-by-routing`, 0 `Missing`, 0 `Guardrail`, 0 `Out-of-scope`, and 0 `Retrieval-weak`.
- Version scope: 139 cross-version rows and 16 Altibase 8.1 verified source rows. The `0x314B4` SQL LOB autocommit row is recorded as cross-version with source summary noting its 7.3 and 8.1 evidence.
- Source evidence: selected Korean Altibase 7.1, Altibase 7.3, and Altibase 8.1
  verified-source Error Message Reference entries were matched by exact reference code
  and symbol. The representative `source_path` is the 7.3 Korean manual for
  cross-version rows and the trunk Korean manual for 8.1-only JSON/Temporary LOB rows;
  each row records line locators and the `07_error_messages_troubleshooting.md` block
  line used for attachment evidence.
- Coverage status changes: single-code answer-ready blocks for object-name collision,
  DDL blocked by active temporary table use, and JSON blocked by disabled
  `TEMPORARY_LOB_ENABLE` were marked `Covered`; grouped exact-code maps for parser,
  DDL, object lookup, privilege, constraint, conversion, regex, LOB/client utility, and
  JSON function/path errors were marked `Covered-by-routing`. Existing row
  `SRC-ERR-XVER-000192` for `0x31458` was updated from the broader tablespace route to
  the scoped temporary-table/LOB DDL route.
- Validation: `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers`
  passed with 1319 catalog rows and 0 matrix rows; scoped TSV counts confirmed 155
  FCA-J021 rows with 3 `Covered` and 152 `Covered-by-routing` statuses. Standard
  repository verification passed: `git diff --check`, `bash review/scripts/run_review_stage.sh validate`,
  and the review-report severity scan showed `Verdict: Pass` for R00-R27 and no
  actionable severity rows.
- Residual risk: no new `Missing`, `Guardrail`, `Out-of-scope`, or `Retrieval-weak`
  rows were added by FCA-J021. Customer answers for exact SQL, JSON, Temporary LOB,
  LOB, and regex errors still require the version, full error line, SQL/API/tool
  command, object definition, property values, and log/client evidence requested by
  `07_error_messages_troubleshooting.md`.

### FCA-J022

- Changed files: `source_item_catalog.tsv` and this remediation log.
- Product coverage changes: cataloged the selected `error_message_reference` client,
  network, replication, SSL/TLS, DB Link, iSQL/iLoader utility, APRE, CLI/ODBC, and
  Log Analyzer exact-code slice only; no customer-facing attachment text or original
  source documents were edited.
- Catalog rows added by this job: 148 rows total; 5 `Covered`, 143
  `Covered-by-routing`, 0 `Missing`, 0 `Guardrail`, 0 `Out-of-scope`, and 0
  `Retrieval-weak`.
- Version scope: all rows are `cross-version` rows with the 7.3 Korean Error Message
  Reference as the representative `source_path`. `cmERR_ABORT_UNSUPPORTED_OPENSSL_VERSION`
  records 7.3 and Altibase 8.1 verified-source evidence and notes that the checked 7.1
  Korean source has no matching symbol.
- Source evidence: selected Korean Altibase 7.1, Altibase 7.3, and Altibase 8.1
  verified-source Error Message Reference entries were matched by exact reference code
  and symbol. Each row records line locators plus the existing
  `07_error_messages_troubleshooting.md` block or exact-code map line used for
  attachment evidence.
- Coverage status changes: dedicated single-code blocks for idle-instance utility
  connection, communication failure, INET socket bind failure, duplicate replication
  name, and unsupported OpenSSL were marked `Covered`. Grouped maps for client
  session/protocol, replication startup and metadata mismatch, client/server SSL, DB
  Link, utility, APRE, and Log Analyzer errors were marked `Covered-by-routing`.
- Validation: `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers`
  passed with 1467 catalog rows and 0 matrix rows; scoped TSV counts confirmed 148
  FCA-J022 rows with 5 `Covered` and 143 `Covered-by-routing` statuses. Standard
  repository verification passed: `git diff --check`, `bash review/scripts/run_review_stage.sh validate`,
  and the review-report severity scan showed `Verdict: Pass` for R00-R27 and no
  actionable severity rows.
- Residual risk: no new `Missing`, `Guardrail`, `Out-of-scope`, or `Retrieval-weak`
  rows were added by FCA-J022. Customer answers for replication, SSL/TLS, DB Link,
  utility, APRE, CLI/ODBC, and Log Analyzer errors still require exact version, full
  error line, command/API call, topology or connection string, relevant properties, and
  log/client evidence as requested by `07_error_messages_troubleshooting.md`.

### FCA-J023

- Changed files: `source_item_catalog.tsv`, `guardrail_register.md`,
  `remediation_log.md`, `GPTs/attachments/07_error_messages_troubleshooting.md`, and
  `GPTs/reports/gap_register.md`.
- Product coverage changes: cataloged the remaining scoped `error_message_reference`
  proof for Spatial `ST Error Code`, 7.1 `SD Error Code` sharding entries, the QP
  memory exact-code block, and the cross-version `sdERR_*` source-drift guardrail. No
  original manuals or source documents were edited.
- Catalog rows added by this job: 148 rows total; 1 `Covered`, 146
  `Covered-by-routing`, 0 `Missing`, 1 `Guardrail`, 0 `Out-of-scope`, and 0
  `Retrieval-weak`.
- Version scope: 81 `cross-version` rows and 67 `7.1` rows. The Spatial rows are
  checked against 7.1, 7.3, and Altibase 8.1 verified source Korean Error Message
  References; `stERR_ABORT_GEOS_UNEXPECTED_ERROR` is recorded as 7.3 and Altibase 8.1
  verified source only because the checked 7.1 source has no matching symbol. The
  sharding `sdERR_*` rows are 7.1-scoped because checked 7.3 and 8.1 Korean sources do
  not list `SD Error Code`.
- Source evidence: selected Korean Error Message Reference entries were matched by
  exact reference code and symbol. Each row records source line locators plus the
  `07_error_messages_troubleshooting.md` exact-code map or block used for attachment
  evidence.
- Coverage status changes: the dedicated `qpERR_ABORT_MEMORY_ALLOCATION` block was
  marked `Covered`; Spatial and 7.1 sharding exact-code maps were marked
  `Covered-by-routing`; the 7.3/8.1 `sdERR_*` source-drift boundary was registered as a
  `Guardrail`.
- Validation: `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers`
  passed with 1615 catalog rows and 0 matrix rows; scoped TSV assertions confirmed 148
  FCA-J023 rows with 1 `Covered`, 146 `Covered-by-routing`, and 1 `Guardrail` status.
  Standard repository verification passed: `git diff --check`,
  `bash review/scripts/run_review_stage.sh validate`, and the review-report severity
  scan showed `Verdict: Pass` for R00-R27 and no actionable severity rows.
- Residual risk: no new `Missing`, `Out-of-scope`, or `Retrieval-weak` rows were added.
  `sdERR_*` answers outside confirmed 7.1 remain guarded by installed-version evidence;
  Spatial answers still require the exact code, failed Spatial SQL/function/operator,
  geometry metadata, SRID, sanitized geometry input when shareable, and trace or loader
  output before state-changing advice.

### FCA-J024

- Changed files: `source_item_catalog.tsv`, `missing_item_register.md`,
  `retrieval_weakness_register.md`, and this remediation log.
- Product coverage changes: cataloged the `performance_tuning` source family for
  Korean Performance Tuning Guide execution plans, access methods, indexes, optimizer
  flow, query transformations, join methods, plan nodes, statistics, hints, SQL Plan
  Cache, Result Cache, waits, locks, sessions, and server-tuning workflows. No original
  manuals or customer-facing attachments were edited.
- Catalog rows added by this job: 81 rows total; 73 `Covered`, 3
  `Covered-by-routing`, 2 `Missing`, 0 `Guardrail`, 0 `Out-of-scope`, and 3
  `Retrieval-weak`.
- Version scope: all rows are `cross-version`, based on checked Korean Altibase 7.1,
  7.3, and Altibase 8.1 verified-source Performance Tuning Guide headings. The 7.3
  Korean manual is the representative `source_path`, and matching English manuals were
  used only to normalize English summaries where consistent with Korean source.
- Source evidence: each row records a Korean Performance Tuning Guide source locator
  and an attachment or grep check. The job used `08_performance_tuning_monitoring.md`
  as the primary owner and routed wait/lock/session evidence to the existing
  `06_data_dictionary_performance_views.md` cross-reference where exact view columns
  are owned by earlier catalog jobs.
- Coverage status changes: existing attachment sections were mapped to answer-ready
  plan, access-method, join, statistics, hint, plan-cache, result-cache, and server
  tuning blocks. Query transformation detail and the full comparison-operator/index
  availability matrix were registered as `Missing`. `GROUP-CUBE`, `GROUP-ROLLUP`, and
  `WINDOW  SORT`/`WINDOW-SORT` were registered as `Retrieval-weak` because current
  attachment coverage preserves only token-level/result-cache routing rather than
  dedicated plan-node answer blocks.
- Validation: `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers`
  passed with 1696 catalog rows and 0 matrix rows; scoped TSV assertions confirmed 81
  FCA-J024 rows with 73 `Covered`, 3 `Covered-by-routing`, 2 `Missing`, and 3
  `Retrieval-weak` statuses. Standard repository verification passed: `git diff --check`,
  `bash review/scripts/run_review_stage.sh validate`, and the review-report severity
  scan showed `Verdict: Pass` for R00-R27 and no actionable severity rows.
- Residual risk: this job did not remediate customer-facing text. Later performance
  remediation should close the two missing rows and three retrieval-weak plan-node
  rows before the final audit can claim no unresolved performance tuning gaps.

### FCA-J026

- Changed files: `source_item_catalog.tsv`, `guardrail_register.md`, and this
  remediation log.
- Product coverage changes: cataloged the selected `replication_manual` source-family
  slice for topology terms, replication state, LAZY/EAGER modes, target eligibility,
  gap and failure handling, conflicts, replication DDL, options, offline recovery,
  host routing, HA failover, sequence replication, propagation roles, compatibility
  boundaries, and unsafe state-change stop conditions. No original manuals or
  customer-facing attachments were edited.
- Catalog rows added by this job: 30 rows total; 28 `Covered`, 1
  `Covered-by-routing`, 0 `Missing`, 1 `Guardrail`, 0 `Out-of-scope`, and 0
  `Retrieval-weak`.
- Version scope: all rows are `cross-version`, using the 7.3 Korean Replication Manual
  as the representative `source_path` and checking the 7.1 and Altibase 8.1 verified
  source replication-manual outlines for corresponding source-family coverage.
- Source evidence: each row records a Korean Replication Manual source locator and an
  attachment or routing check. `09_replication_ha_cdc.md` is the primary attachment
  owner; `SRC-REPL-XVER-000028` routes `REPLICATION_SENDER_IP` property details to
  `05_data_types_properties.md`.
- Coverage status changes: topology, mode, prerequisites, conflicts, EAGER failback,
  replication options, DDL, HA failover, sequence replication, propagation, and unsafe
  operation stop conditions were marked `Covered`; `REPLICATION_SENDER_IP` was marked
  `Covered-by-routing`; exact cross-version compatibility was registered as a
  `Guardrail`.
- Validation: `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers`
  passed with 1779 catalog rows and 0 matrix rows; scoped TSV assertions confirmed 30
  FCA-J026 rows with 28 `Covered`, 1 `Covered-by-routing`, and 1 `Guardrail` status.
  Standard repository verification passed: `git diff --check`,
  `bash review/scripts/run_review_stage.sh validate`, and the review-report severity
  scan showed `Verdict: Pass` for R00-R27 and no actionable severity rows.
- Residual risk: no new `Missing`, `Out-of-scope`, or `Retrieval-weak` rows were
  added. Cross-version replication compatibility remains guarded by exact
  Sender/Receiver direction, installed `V$VERSION` output, replication mode, option
  list, and feature-use evidence before giving a definitive customer answer.

### FCA-J027

- Changed files: `source_item_catalog.tsv`, `missing_item_register.md`,
  `guardrail_register.md`, and this remediation log.
- Product coverage changes: cataloged the `log_analyzer` and `replication_manager`
  source-family slices for CDC concepts, Log Analysis API files/call order/collector
  setup/ACK-restart behavior/status diagnostics/XLog handling/conversion/error APIs,
  Replication Manager connection workflows, pane/object action mapping, full-mesh and
  join workflows, package-boundary guardrails, and 1.2 through 1.4 release-note items.
  No original manuals or customer-facing attachments were edited.
- Catalog rows added by this job: 25 rows total; 18 `Covered`, 0
  `Covered-by-routing`, 6 `Missing`, 1 `Guardrail`, 0 `Out-of-scope`, and 0
  `Retrieval-weak`.
- Version scope: Log Analyzer rows are `cross-version`, using the 7.3 Korean Log
  Analyzer manual as representative source and checking 7.1 and Altibase 8.1
  verified-source outlines for corresponding sections. Replication Manager manual rows
  use the release Korean manual and trunk Korean manual as checked sources. Replication
  Manager release-note rows are `patch-specific` for 1.2, 1.3, and 1.4.
- Source evidence: each row records a Korean source locator and attachment or register
  evidence. Attachment owner is `09_replication_ha_cdc.md`; `14_utilities_operation_tools.md`
  remains a cross-route only for generic tool routing.
- Coverage status changes: core CDC concepts, limitations, required files, call order,
  collector setup, ACK/restart behavior, collector status, XLog types, inspection,
  metadata, conversion, error handling, and Replication Manager workflows were marked
  `Covered`; Replication Manager package-manifest claims were marked `Guardrail`.
  Exact environment/logging API details, XLog structure tables, `ALA_IsNullValue`,
  sample program path, and detailed Replication Manager 1.2/1.3 BUG-token release
  rows were registered as `Missing`.
- Validation: `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers`
  passed with 1804 catalog rows and 0 matrix rows; scoped TSV assertions confirmed 25
  FCA-J027 rows with 18 `Covered`, 6 `Missing`, and 1 `Guardrail` status. Standard
  repository verification passed: `git diff --check`,
  `bash review/scripts/run_review_stage.sh validate`, and the review-report severity
  scan showed `Verdict: Pass` for R00-R27 and no actionable severity rows.
- Residual risk: this job did not remediate customer-facing text. Later CDC/RepMgr
  remediation should close the six missing rows before the final audit can claim no
  unresolved CDC or Replication Manager source-item gaps.

### FCA-J028

- Changed files: `source_item_catalog.tsv` and this remediation log.
- Product coverage changes: cataloged the `security_ssl_tls` source-family slice for
  SSL/TLS handshake behavior, server certificate and listener setup, JDBC, ODBC/CLI,
  ADO.NET, FIPS, TCP-access restriction, session monitoring, sample locations, 7.1
  Heartbleed/OpenSSL requirements, 7.3/8.1 TLS 1.3 requirements, Altibase 8.1
  replication SSL, and the selected replication network-check technical document.
  No original manuals or customer-facing attachments were edited.
- Catalog rows added by this job: 21 rows total; 20 `Covered`, 1
  `Covered-by-routing`, 0 `Missing`, 0 `Guardrail`, 0 `Out-of-scope`, and 0
  `Retrieval-weak`.
- Version scope: ordinary SSL/TLS rows use the Korean 7.3 SSL/TLS guide as the
  representative source with 7.1 and Altibase 8.1 verified-source checks where
  corresponding material exists; 7.1-specific and 8.1-specific rows use explicit
  version scopes. Replication network diagnostics use
  `Technical Documents/kor/Replication network check.md` under
  `technical_documents_support`.
- Source evidence: each row records a Korean source locator plus attachment evidence
  in `18_security_ssl_tls.md` or `09_replication_ha_cdc.md`. Overlapping
  `ACCESS_LIST`, `ACCESS_LIST_FILE`, `SSL_*`, and `REPLICATION_*` property details
  already cataloged by `FCA-J016` were preserved rather than duplicated.
- Coverage status changes: the scoped SSL/TLS and network-diagnostic rows were mapped
  to existing answer-ready attachment anchors; the SSL sample location row is
  `Covered-by-routing` because the source is represented through the client setup and
  troubleshooting routing rather than a standalone sample-code block.
- Validation: `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers`
  passed with 1825 catalog rows and 0 matrix rows; scoped TSV assertions confirmed 21
  FCA-J028 rows with 20 `Covered` and 1 `Covered-by-routing` status. Standard
  repository verification passed: `git diff --check`,
  `bash review/scripts/run_review_stage.sh validate`, and the review-report severity
  scan showed `Verdict: Pass` for R00-R27 and no actionable severity rows.
- Residual risk: this job did not remediate customer-facing text and added no new
  unresolved `Missing`, `Guardrail`, `Out-of-scope`, or `Retrieval-weak` rows.

### FCA-J030

- Changed files: `source_item_catalog.tsv`, `guardrail_register.md`, and this
  remediation log.
- Product coverage changes: cataloged the `jdbc_java` source-family slice for JDBC
  driver packaging, JDBC URLs, connection properties, failover, DataSource and pool
  validation, JDBC API behavior, Java compatibility, Spring Boot, Hibernate, and
  Adapter for JDBC setup, properties, utilities, constraints, and runbooks. No
  original manuals or customer-facing attachments were edited.
- Catalog rows added by this job: 38 rows total; 37 `Covered`, 0
  `Covered-by-routing`, 0 `Missing`, 1 `Guardrail`, 0 `Out-of-scope`, and 0
  `Retrieval-weak`.
- Version scope: 7.1-specific driver packaging uses the Korean Altibase 7.1 JDBC
  manual; 7.3-specific driver packaging uses the Korean Altibase 7.3 JDBC manual; the
  statement-cache properties use the Korean trunk JDBC manual with established
  `Altibase 8.1 verified source` wording; cross-version Java compatibility uses
  `Technical Documents/kor/JavaCompatibility.md`; Adapter rows use Korean Adapter for
  JDBC manuals; Spring and Hibernate rows use the approved Korean third-party guides.
- Source evidence: each row records a repository-local source locator plus attachment
  evidence in `11_java_jdbc_spring.md`. The guardrail row is registered as
  `SRC-OTHER-XVER-000225` and captures live JDBC/Spring/Hibernate/Adapter runtime
  validation inputs required before asserting production compatibility or failover
  behavior.
- Coverage status changes: the scoped source items were mapped to existing
  answer-ready anchors in `11_java_jdbc_spring.md`. No new `Missing`,
  `Out-of-scope`, or `Retrieval-weak` rows were added.
- Validation: `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers`
  passed with 1909 catalog rows and 0 matrix rows; scoped TSV assertions confirmed 38
  FCA-J030 rows with 37 `Covered` and 1 `Guardrail` status. Standard repository
  verification passed: `git diff --check`,
  `bash review/scripts/run_review_stage.sh validate`, and the review-report severity
  scan showed `Verdict: Pass` for R00-R27 and no actionable severity rows.
- Residual risk: no customer-facing attachment text was changed. The runtime
  guardrail remains intentional and requires exact version, driver, framework,
  topology, target-driver, SSL/TLS, and live-output evidence before definitive
  customer answers about production runtime success.

### FCA-J032

- Changed files: `source_item_catalog.tsv`, `missing_item_register.md`,
  `guardrail_register.md`, and this remediation log.
- Product coverage changes: cataloged the `isql_iloader` source-family slice for iSQL
  session commands, connection and startup/shutdown workflows, file/script commands,
  host variables, output formatting, login files, iLoader command syntax, FORM files,
  batch and interactive load/export workflows, LOB handling, diagnostics,
  low-frequency options, and version-sensitive iLoader behavior. No original manuals
  or customer-facing attachments were edited.
- Catalog rows added by this job: 31 rows total; 29 `Covered`, 0
  `Covered-by-routing`, 1 `Missing`, 1 `Guardrail`, 0 `Out-of-scope`, and 0
  `Retrieval-weak`.
- Source evidence: Korean iSQL and iLoader 7.3 manuals are the representative
  cross-version sources, with Korean iLoader 7.1 for `-stmt_prefix` and the Korean
  Altibase 8.1.0.0.1 release note for iLoader Empty LOB behavior.
- Coverage status changes: existing answer-ready anchors in
  `13_isql_iloader_basic_tools.md` cover the scoped session, command, workflow, FORM,
  LOB, diagnostic, and version-sensitive rows. `SRC-ISQL-XVER-000013` was registered
  as `Missing` for the source-backed `ALTIBASE_NLS_NCHAR_LITERAL_REPLACE` NCHAR
  literal behavior that is not yet answer-ready in attachment 13. `SRC-ILOAD-XVER-000016`
  was registered as a `Guardrail` because selected sources list `-dry-run` but do not
  define exact production-precheck effects or diagnostics.
- Validation: `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers`
  passed with 1974 catalog rows and 0 matrix rows; scoped TSV assertions confirmed 31
  FCA-J032 rows with 29 `Covered`, 1 `Missing`, and 1 `Guardrail` status. Standard
  repository verification passed: `git diff --check`,
  `bash review/scripts/run_review_stage.sh validate`, and the review-report severity
  scan showed `Verdict: Pass` for R00-R27 and no actionable severity rows.
- Residual risk: no customer-facing attachment text was changed. The iSQL NCHAR
  literal `Missing` row should be remediated with a compact answer-ready block before
  final audit closure; the `-dry-run` guardrail remains intentional until installed
  client behavior is verified or fuller selected-source semantics are added.

### FCA-J033

- Changed files: `source_item_catalog.tsv`, `missing_item_register.md`,
  `guardrail_register.md`, and this remediation log.
- Product coverage changes: cataloged the `utilities_datacompj` source-family slice
  for `aexport`, `altiComp`, `aku`, `altiMon`, `altiAudit`, `altibase`, `altierr`,
  `altipasswd`, `altiProfile`, `altiwrap`, `awrite`, `checkServer`,
  `killCheckServer`, `server`, dump-family diagnostics, and `dataCompJ`. No original
  manuals or customer-facing attachments were edited.
- Catalog rows added by this job: 40 rows total; 34 `Covered`, 4
  `Covered-by-routing`, 1 `Missing`, 1 `Guardrail`, 0 `Out-of-scope`, and 0
  `Retrieval-weak`.
- Source evidence: Korean Utilities manuals for 7.1, 7.3, and Altibase trunk were
  used for utility headings and command/output boundaries; Korean dataCompJ release
  and trunk manuals were used for dataCompJ command, report, and compatibility rows;
  the Korean dataCompJ 7.2 release note was used for the exact package and BUG-token
  release-note row.
- Coverage status changes: existing answer-ready anchors in
  `14_utilities_operation_tools.md` cover the scoped utility and dataCompJ rows, with
  AKU rows routed through both attachment 14 and `17_kubernetes_aku_cloud.md`.
  `SRC-REL-PATCH-000023` was registered as `Missing` for exact dataCompJ 7.2 package
  and BUG-token preservation. `SRC-OTHER-XVER-000229` was registered as a
  `Guardrail` for installed-tool behavior, generated outputs, dump-file
  interpretation, synchronization effects, and live diagnostic conclusions.
- Validation: `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers`
  passed with 2014 catalog rows and 0 matrix rows; scoped TSV assertions confirmed 40
  FCA-J033 rows with 34 `Covered`, 4 `Covered-by-routing`, 1 `Missing`, and 1
  `Guardrail` status. Standard repository verification passed: `git diff --check`,
  `bash review/scripts/run_review_stage.sh validate`, and the review-report severity
  scan showed `Verdict: Pass` for R00-R27 and no actionable severity rows.
- Residual risk: no customer-facing attachment text was changed. The dataCompJ 7.2
  exact package/BUG-token `Missing` row should be remediated with a compact
  release-note block before final audit closure; the installed-tool guardrail remains
  intentional until exact package, configuration, input file, generated report, and
  live/non-production output evidence is provided.

### FCA-J034

- Changed files: `source_item_catalog.tsv`, `guardrail_register.md`, and this
  remediation log.
- Product coverage changes: cataloged the `migration_oracle` source-family slice for
  Migration Center 7.19 release scope, runtime/database requirements, five-stage
  workflow, CLI commands, Build/Reconcile/Run/Data Validation outputs, migration
  options, Oracle object/type/default/JSON/empty-string conversion, PSM converter
  review rules, Oracle-specific troubleshooting, Adapter for Oracle prerequisites,
  `oraAdapter.conf` properties, constraints, startup/shutdown, `oaUtility`, data type
  mapping, DDL order, and offline option. No original manuals or customer-facing
  attachments were edited.
- Catalog rows added by this job: 30 rows total; 29 `Covered`, 0
  `Covered-by-routing`, 0 `Missing`, 1 `Guardrail`, 0 `Out-of-scope`, and 0
  `Retrieval-weak`.
- Source evidence: Korean Migration Center trunk and release manuals, Korean Migration
  Center 7.19 release notes, and Korean Adapter for Oracle 7.1, 7.3, and trunk
  manuals were used as authoritative sources. Matching attachment evidence is in
  `15_migration_oracle_compatibility.md`.
- Coverage status changes: existing answer-ready anchors in
  `15_migration_oracle_compatibility.md` cover the scoped Migration Center and Adapter
  rows. `SRC-OTHER-XVER-000230` was registered as a `Guardrail` for production
  migration/adapter success because selected sources require exact versions, object
  DDL, generated reports, configuration, logs, driver/OCI state, backup/rollback plan,
  and non-production validation output before definitive customer claims.
- Validation: `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers`
  passed with 2044 catalog rows and 0 matrix rows; scoped TSV assertions confirmed 30
  FCA-J034 rows with 29 `Covered` and 1 `Guardrail` status. Standard repository
  verification passed: `git diff --check`,
  `bash review/scripts/run_review_stage.sh validate`, and the review-report severity
  scan showed `Verdict: Pass` for R00-R27 and no actionable severity rows.
- Residual risk: no customer-facing attachment text was changed. The migration and
  adapter guardrail remains intentional until the customer provides exact source/target
  versions, schemas, generated reports, configuration, logs, rollback plan, and
  non-production validation evidence.

### FCA-J035

- Changed files: `source_item_catalog.tsv`, `guardrail_register.md`, and this
  remediation log.
- Product coverage changes: cataloged the DB Link and external connector source-family
  slice for DB Link architecture, setup, SQL syntax, remote access methods, bind and
  batch functions, object support, data type support, transaction levels, metadata and
  monitoring views, AltiLinker and `TARGETS` properties, 8.1 encrypted password
  release-note boundary, Hadoop Connector/Sqoop setup and import/export behavior,
  DBeaver setup and troubleshooting, Hibernate dialect setup, OpenLDAP `back-sql`, and
  Oracle GoldenGate for Big Data JDBC Handler setup and compatibility cautions. No
  original manuals or customer-facing attachments were edited.
- Catalog rows added by this job: 42 rows total; 40 `Covered`, 1
  `Covered-by-routing`, 0 `Missing`, 1 `Guardrail`, 0 `Out-of-scope`, and 0
  `Retrieval-weak`.
- Source evidence: Korean DB Link and Hadoop Connector 7.3 manuals were used for DB
  Link and Hadoop rows, Korean trunk DB Link manual and Korean 8.1 release note were
  used for 8.1-only DB Link boundaries, and Korean Tools release/trunk third-party
  connector guides were used for DBeaver, Hibernate, OpenLDAP, and GoldenGate rows.
  Matching attachment evidence is in `16_dblink_external_connectors.md`.
- Coverage status changes: existing answer-ready anchors in
  `16_dblink_external_connectors.md` cover the scoped DB Link, Hadoop, and third-party
  connector rows. `SRC-VIEW-XVER-000128` is `Covered-by-routing` through attachment 16
  plus the dictionary/view cross-reference. `SRC-OTHER-XVER-000245` was registered as
  a `Guardrail` for live connector validation, runtime success, compatibility
  conclusions, and root-cause claims.
- Validation: `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers`
  passed with 2086 catalog rows and 0 matrix rows; scoped TSV assertions confirmed 42
  FCA-J035 rows with 40 `Covered`, 1 `Covered-by-routing`, and 1 `Guardrail` status.
  Standard repository verification passed: `git diff --check`,
  `bash review/scripts/run_review_stage.sh validate`, and the review-report severity
  scan showed `Verdict: Pass` for R00-R27 and no actionable severity rows.
- Residual risk: no customer-facing attachment text was changed. The live connector
  guardrail remains intentional until the customer provides exact Altibase patch,
  DB Link and connector configuration, Java/JDBC/ODBC/runtime versions, topology,
  security settings, logs, and non-production or live output evidence.

### FCA-J037

- Changed files: `source_item_catalog.tsv`, `guardrail_register.md`, and this
  remediation log.
- Product coverage changes: cataloged the Spatial, `altiShapeLoader`, NiFi, Tableau,
  and miscellaneous integration slice for Spatial concepts, `GEOMETRY` subtypes,
  WKT/WKB/EWKT/EWKB, Spatial DDL and R-Tree syntax, SRID metadata and
  `SYS_SPATIAL` procedures, Spatial function/operator families, Spatial API function
  families, Altibase-to-Altibase WKB/EWKB migration, `altiShapeLoader` setup/options,
  shapefile import/export, shapefile constraints/type mappings, NiFi JDBC
  `DBCPConnectionPool` setup, and Tableau `Other Databases (JDBC)` setup. No original
  manuals or customer-facing attachments were edited.
- Catalog rows added by this job: 30 rows total; 29 `Covered`, 0
  `Covered-by-routing`, 0 `Missing`, 1 `Guardrail`, 0 `Out-of-scope`, and 0
  `Retrieval-weak`.
- Source evidence: Korean Spatial SQL 7.1, 7.3, and trunk manuals; Korean
  `altiShapeLoader` release and trunk manuals; Korean NiFi and Tableau third-party
  guides; and `GAP-J002-017`/`GAP-J002-018` for live validation boundaries. Matching
  attachment evidence is in `19_spatial_nifi_tableau_misc.md`.
- Coverage status changes: existing answer-ready anchors in
  `19_spatial_nifi_tableau_misc.md` cover the scoped Spatial, loader, NiFi, and
  Tableau rows. `SRC-OTHER-XVER-000267` was registered as a `Guardrail` for
  production import/export, BI/ETL connectivity, performance, and root-cause claims
  that require exact versions, source files, configuration, logs, and live output.
- Validation: `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers`
  passed with 2136 catalog rows and 0 matrix rows; scoped TSV assertions confirmed 30
  FCA-J037 rows with 29 `Covered`, 1 `Guardrail`, and no `Missing` or
  `Retrieval-weak` rows. Standard repository verification passed: `git diff --check`,
  `bash review/scripts/run_review_stage.sh validate`, and the review-report severity
  scan showed `Verdict: Pass` for R00-R27 and no actionable severity rows.
- Residual risk: no customer-facing attachment text was changed. The live Spatial,
  loader, NiFi, and Tableau guardrail remains intentional until the customer provides
  exact Altibase patch, JDBC/Java versions, host/port/database details, character set,
  SRID, geometry precision, shapefile component set and size, integration versions,
  property/config files, full logs/output, and rollback or reload plan.

### FCA-J038

- Changed files: `source_item_catalog.tsv`, `missing_item_register.md`,
  `guardrail_register.md`, and this remediation log.
- Product coverage changes: cataloged the remaining technical-document support slice
  for `ReplicationCompatibility.md` and cross-family `JavaCompatibility.md` rows not
  fully owned by earlier catalog jobs. No original manuals or customer-facing
  attachments were edited.
- Catalog rows added by this job: 17 rows total; 8 `Covered`, 0
  `Covered-by-routing`, 7 `Missing`, 0 `Guardrail`, 2 `Out-of-scope`, and 0
  `Retrieval-weak`.
- Source evidence: Korean `Technical Documents/kor/ReplicationCompatibility.md` was
  used for LAZY replication backward compatibility, 7.1/7.3 Sender/Receiver matrices,
  and 7.1/7.3 replication protocol ranges. Korean
  `Technical Documents/kor/JavaCompatibility.md` was used for the Java compatibility
  legend, DB Link runtime rows, altiMon runtime rows, and tool runtime rows for
  `altiShapeLoader`, Altibase Hadoop Connector, `dataCompJ`, Migration Center, and
  Replication Manager.
- Coverage status changes: existing answer-ready anchors in
  `09_replication_ha_cdc.md` cover the in-scope replication compatibility rows and the
  Replication Manager bundled-JRE row; existing DB Link Java runtime wording in
  `16_dblink_external_connectors.md` covers the 7.1/7.3 DB Link Java compatibility
  rows. The Java compatibility legend, altiMon, `altiShapeLoader`, Hadoop Connector,
  `dataCompJ`, and Migration Center exact runtime matrices were registered as
  `Missing`. Standalone 6.x replication and Java compatibility sections were
  registered as `Out-of-scope` for the locked 7.1/7.3/8.1 customer upload scope.
- Validation: `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers`
  passed with 2153 catalog rows and 0 matrix rows; scoped TSV assertions confirmed 17
  FCA-J038 rows with 8 `Covered`, 7 `Missing`, and 2 `Out-of-scope` status values and
  non-empty required fields/guardrail reasons. Standard repository verification passed:
  `git diff --check`, `bash review/scripts/run_review_stage.sh validate`, and the
  review-report severity scan showed `Verdict: Pass` for R00-R27 and no actionable
  severity rows.
- Residual risk: no customer-facing attachment text was changed. The seven
  Java/tool-runtime `Missing` rows should be remediated with compact compatibility
  blocks before final audit closure; the two 6.x out-of-scope rows remain intentional
  unless a later source-family update explicitly expands customer-facing historical
  scope.

### FCA-J039

- Changed files: `catalog_consolidation_qa.md`,
  `catalog_schema_and_extraction_scripts.md`,
  `scripts/fca_catalog_tools.py`, and this remediation log.
- Product coverage changes: none. This job preserved all existing catalog rows,
  catalog dispositions, registers, customer-facing attachments, GPT instructions, and
  original source documents.
- Catalog QA result: `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py catalog-qa`
  passed with 2153 catalog rows, 0 matrix rows, all 25 controlled source families
  present, 0 duplicate IDs, 0 ID/version mismatches, 0 observed ID namespace sequence
  gaps, 0 invalid controlled-vocabulary values, 0 missing source paths, and 0
  unregistered unresolved dispositions.
- Disposition totals at QA handoff: 1035 `Covered`, 840 `Covered-by-routing`, 232
  `Missing`, 33 `Guardrail`, 3 `Out-of-scope`, and 10 `Retrieval-weak`.
- Register reconciliation: every `Missing` row appears in
  `missing_item_register.md`, every `Guardrail` and `Out-of-scope` row appears in
  `guardrail_register.md`, and every `Retrieval-weak` row appears in
  `retrieval_weakness_register.md`.
- Narrative-log completeness note: the catalog contains rows for `FCA-J013`,
  `FCA-J014`, `FCA-J025`, `FCA-J029`, `FCA-J031`, and `FCA-J036`, but this log did not
  contain individual `###` sections for those jobs before `FCA-J039`. This is recorded
  as a QA note, not a catalog blocker, because their catalog rows, evidence fields, and
  required register entries passed validation.
- Validation: `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py catalog-qa`
  passed; `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers`
  passed; standard repository verification is recorded in the `FCA-J039` final job
  output.
- Residual risk: source-to-attachment matrix rows remain assigned to `FCA-J040`.
  Existing unresolved `Missing` and `Retrieval-weak` rows remain intentional handoff
  work for later remediation and routing jobs.
