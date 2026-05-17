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
