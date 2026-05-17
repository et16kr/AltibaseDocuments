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
