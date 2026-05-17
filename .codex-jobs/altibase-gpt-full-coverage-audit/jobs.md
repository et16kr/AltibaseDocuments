# Altibase GPT Full Coverage Audit

- Kind: `docs`
- Status values: `ToDo`, `Progress`, `Done`, `Fail`
- Workflow name: `altibase-gpt-full-coverage-audit`
- Current artifact status: executable workflow prepared; user-run only
- Intended repository: `/home/et16/AltibaseDocuments`
- Plan source: `/home/et16/work/altibase_gpt_full_coverage_audit_plan_20260517.md`

This workflow is prepared for manual execution. It includes `run-all.sh`,
`requirements.md`, and per-job prompts, but the generated workflow must not be run
automatically by Codex. The user starts or resumes it manually.

## Baseline Evidence

The current review/remediation cycle is complete:

- `review/scripts/run_review_remediation_cycle.sh status` reports `R00` through `R27`
  as `Done`.
- No review stage is `Reviewing`, `Remediating`, `ReReviewing`, or `Fail`.
- `git status --short` was clean before this workflow was created.
- `bash review/scripts/run_review_stage.sh validate` passed.
- Review reports contain `Verdict: Pass` lines and no actionable `Blocker`, `High`,
  `Medium`, or `Low` finding rows.

The latest full benchmark run to use as failure evidence is:

- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_205641/`
- Result: `101/270` passed, `169` failed, pass rate `37.4%`.
- Critical fact coverage: `85.1%`.
- Required token preservation: `90.1%`.
- Unsupported-claim rate: `1.1%`.
- Protected-topic blockers: `32`.
- Readiness decision: `blocking_gaps`.

This benchmark is not the audit scope. It is evidence for priority, targeted
validation, retrieval weakness analysis, and protected-topic triage. The audit scope is
the selected repository-local source corpus.

## Job Count Decision

The original plan proposed 34 jobs as a first cut. This reviewed workflow uses 51 jobs
because several source families are too large for one reliable Codex execution:

- properties already have `484` inventoried names and need four catalog jobs;
- Administrator operations are split between protected backup/recovery/storage and
  account/tablespace/privilege administration;
- SQL Reference coverage is split across DDL storage objects, DCL/admin/replication
  SQL, DML/functions, and JSON/LOB/Oracle-difference syntax;
- error coverage previously required multiple exact-code and grouped-code slices;
- dictionary/performance view coverage spans meta tables, operational views, and
  patch-sensitive column guardrails;
- remediation is bounded by attachment groups instead of broad all-domain waves;
- catalog consolidation happens before source-to-attachment matrix mapping.

Prefer more bounded jobs over broad manual spot checks. If a catalog job is still too
large, split it by source family or attachment owner while preserving the same catalog
schema and stable ID rules.

## Disposition Contract

Every source item must end with exactly one traceable disposition:

- `Covered`: represented in `GPTs/attachments/` as an answer-ready block.
- `Covered-by-routing`: represented through a linked section plus retrieval alias,
  index, or routing entry.
- `Guardrail`: selected sources do not support a definitive customer answer, or the
  answer depends on exact patch, environment, object definition, log excerpt, runtime
  output, installed tool behavior, or live integration state.
- `Out-of-scope`: not part of the selected upload source corpus, with the reason
  recorded.
- `Missing`: source-backed and in scope but not answerable from the attachments.
- `Retrieval-weak`: present but unlikely to be found by GPT retrieval.

The final state must have no unresolved `Missing` or unresolved `Retrieval-weak` rows.

## Required Durable Artifacts

The workflow should create or update:

- `GPTs/reports/full_coverage_audit/source_corpus_lock.md`
- `GPTs/reports/full_coverage_audit/source_item_catalog.tsv`
- `GPTs/reports/full_coverage_audit/source_to_attachment_matrix.tsv`
- `GPTs/reports/full_coverage_audit/missing_item_register.md`
- `GPTs/reports/full_coverage_audit/guardrail_register.md`
- `GPTs/reports/full_coverage_audit/retrieval_weakness_register.md`
- `GPTs/reports/full_coverage_audit/remediation_log.md`
- `GPTs/reports/full_coverage_audit/final_full_coverage_audit.md`

Customer-facing remediation should remain in:

- `GPTs/attachments/*.md`
- `GPTs/GPT_Instructions_Draft.md`

## Source Policy

- Use repository-local selected sources only.
- Korean manuals, release notes, patch notes, tool manuals, technical documents, and
  third-party guides are authoritative when Korean and English sources differ.
- English manuals are extraction aids when consistent with Korean sources.
- Keep customer-facing attachments in English.
- Preserve the established `Altibase 8.1 verified source` wording for 8.1-only
  material where the attachment set uses it.
- Do not edit original manuals or source documents.
- Do not replace Altibase-specific behavior with generic Oracle or database behavior.

## Priority Signals From Latest Benchmark

The latest run has `169` failed questions. Domain failure counts:

| Domain | Failed |
| --- | ---: |
| `properties` | 32 |
| `sql_ddl_dml_datatypes` | 30 |
| `views_performance_monitoring` | 24 |
| `tools_apis_connectors_migration` | 24 |
| `replication_cdc_security_network` | 21 |
| `errors_troubleshooting` | 20 |
| `operations_admin` | 18 |

High retrieval risk dominates: `113` of `169` failed questions have
`retrieval_risk=high`. FCA-J040, FCA-J046, FCA-J047, and FCA-J050 must explicitly use
this evidence when building the matrix, fixing routing, and selecting targeted checks.

Protected-topic blocker themes:

| Topic | Count |
| --- | ---: |
| `version_sensitive_property_changes` | 12 |
| `replication_state_changes` | 8 |
| `backup_recovery` | 6 |
| `destructive_sql` | 3 |
| `security_tls` | 3 |

Any post-remediation protected-topic blocker remains release-blocking until triaged.

## Partitioning Model

- FCA-J001-FCA-J003: preflight, corpus lock, and reusable catalog/check machinery.
- FCA-J004-FCA-J012: release/platform, installation, administrator, SQL, and data type catalog extraction.
- FCA-J013-FCA-J016: property catalog extraction split by property family.
- FCA-J017-FCA-J019: dictionary, performance view, and view-column guardrail catalog extraction.
- FCA-J020-FCA-J023: error catalog extraction split by error family.
- FCA-J024-FCA-J038: remaining catalog extraction for performance, monitoring, replication, security, tools, APIs, connectors, integrations, and technical support documents.
- FCA-J039-FCA-J040: catalog QA and source-to-attachment matrix mapping.
- FCA-J041-FCA-J045: content remediation split by attachment group.
- FCA-J046-FCA-J047: retrieval remediation split by attachment group.
- FCA-J048-FCA-J051: guardrail audit, answer contract alignment, validation, and final sign-off.

## Job Scope Matrix

| ID | Primary target areas | Expected durable output |
| --- | --- | --- |
| `FCA-J001` | Current workflow status, latest benchmark, existing reports | Preflight evidence section and locked latest-run baseline. |
| `FCA-J002` | `source_inventory.md`, `coverage_matrix.md`, selected source roots | `source_corpus_lock.md`. |
| `FCA-J003` | Catalog schema, controlled vocabularies, extraction/check scripts | Catalog schema, stable ID rules, and reusable script/check plan. |
| `FCA-J004` | Release notes, patch notes, supported platforms | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J005` | Getting Started and Installation manuals | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J006` | Administrator manuals: backup, recovery, archive, storage, server mode | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J007` | Administrator manuals: tablespaces, datafiles, accounts, users, privileges | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J008` | SQL Reference: storage/table/index/constraint/queue DDL | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J009` | SQL Reference: DCL/admin/replication/destructive SQL | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J010` | SQL Reference: DML, predicates, expressions, functions | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J011` | SQL Reference: JSON, LOB, Oracle differences, syntax restrictions | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J012` | General Reference 1 data types | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J013` | Core/path/storage property families | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J014` | Memory/log/cache/capacity property families | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J015` | Optimizer/session/locale/timeout property families | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J016` | Security/replication/network/DB Link property families | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J017` | Dictionary tables and meta tables | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J018` | Performance views | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J019` | View columns and installed-metadata guardrails | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J020` | Storage/backup/recovery/tablespace errors | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J021` | SQL/datatype/JSON/LOB/regex errors | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J022` | Client/network/replication/tool errors | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J023` | Spatial and remaining grouped-code errors | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J024` | Performance Tuning Guides | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J025` | Monitoring API and SNMP manuals | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J026` | Replication manuals and related SQL | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J027` | CDC, Log Analyzer, RepMgr | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J028` | SSL/TLS, replication SSL, network docs | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J029` | Stored Procedures and External Procedures manuals | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J030` | JDBC, Adapter, Spring, Hibernate, Java compatibility | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J031` | CLI, ODBC, C Interface, Precompiler | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J032` | iSQL and iLoader manuals | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J033` | Utilities and dataCompJ manuals | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J034` | Migration Center and Adapter for Oracle | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J035` | DB Link, Hadoop, third-party connector guides | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J036` | Kubernetes, AKU, container/cloud guides | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J037` | Spatial, altiShapeLoader, NiFi, Tableau | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J038` | Technical documents and cross-family support files | Catalog rows for the scoped source family with source evidence, literal tokens, expected attachment owner, and initial disposition. |
| `FCA-J039` | Whole catalog | Validated `source_item_catalog.tsv`, duplicate/ID report, vocabulary checks, and source-family completeness notes. |
| `FCA-J040` | Catalog, coverage matrix, attachments | Initial `source_to_attachment_matrix.tsv` with dispositions and evidence. |
| `FCA-J041` | Attachments `03`, `04`, `05` and related reports | Remediated scoped attachment gaps with updated matrix/register dispositions and remediation log evidence. |
| `FCA-J042` | Attachments `01`, `02`, `07` and related reports | Remediated scoped attachment gaps with updated matrix/register dispositions and remediation log evidence. |
| `FCA-J043` | Attachments `06`, `08`, `09`, `18` and related reports | Remediated scoped attachment gaps with updated matrix/register dispositions and remediation log evidence. |
| `FCA-J044` | Attachments `10`, `11`, `12`, `13`, `14`, `16` and related reports | Remediated scoped attachment gaps with updated matrix/register dispositions and remediation log evidence. |
| `FCA-J045` | Attachments `15`, `17`, `19` and related reports | Remediated scoped attachment gaps with updated matrix/register dispositions and remediation log evidence. |
| `FCA-J046` | Attachments `00` through `09` | Remediated scoped attachment gaps with updated matrix/register dispositions and remediation log evidence. |
| `FCA-J047` | Attachments `10` through `19` | Remediated scoped attachment gaps with updated matrix/register dispositions and remediation log evidence. |
| `FCA-J048` | Guardrail and out-of-scope rows | Audited guardrail register with required missing-input and safest-next-check patterns. |
| `FCA-J049` | GPT instructions and answer contract | Updated instruction/prompt alignment if needed. |
| `FCA-J050` | Validation scripts and answerability checks | Validation output and targeted answerability results for remediated/high-risk rows. |
| `FCA-J051` | Final audit reports | `final_full_coverage_audit.md` and final readiness decision. |

## Jobs

| ID | Status | Title | Goal |
| --- | --- | --- | --- |
| `FCA-J001` | `ToDo` | Preflight and benchmark evidence lock | Confirm the current review/remediation cycle is complete, the worktree is clean, previous jobs are committed, and the latest full benchmark run is locked as audit evidence. |
| `FCA-J002` | `ToDo` | Source corpus lock | Freeze the exact selected source roots, source families, authoritative Korean sources, extraction aids, exclusions, and customer-facing scope boundaries. |
| `FCA-J003` | `ToDo` | Catalog schema and extraction scripts | Define the source item catalog schema, controlled vocabularies, stable ID rules, and reusable extraction and coverage-check scripts where practical. |
| `FCA-J004` | `ToDo` | Release notes patch notes and platform catalog | Extract release, patch, feature, platform, upgrade, and exact version-boundary items into the source item catalog. |
| `FCA-J005` | `ToDo` | Installation and getting-started catalog | Extract installation, environment setup, database creation, startup, shutdown, licensing, and first-check items. |
| `FCA-J006` | `ToDo` | Administrator backup recovery archive and storage catalog | Extract backup, recovery, archive log, storage, server-mode, media-failure, and protected-operation items. |
| `FCA-J007` | `ToDo` | Administrator tablespace account privilege catalog | Extract tablespace, datafile, user, role, privilege, account, schema administration, and validation-check items. |
| `FCA-J008` | `ToDo` | SQL Reference DDL storage table index catalog | Extract tablespace, datafile, table, partition, index, constraint, LOB storage, queue, and related DDL grammar items. |
| `FCA-J009` | `ToDo` | SQL Reference DCL admin replication destructive catalog | Extract DCL, user/privilege SQL, administrative SQL, replication SQL, Log Analyzer SQL, destructive SQL, privileges, and safety-boundary items. |
| `FCA-J010` | `ToDo` | SQL Reference DML expression and function catalog | Extract DML, predicates, expressions, built-in functions, regular expression, object-name, and syntax restriction items. |
| `FCA-J011` | `ToDo` | SQL Reference JSON LOB and Oracle-difference catalog | Extract JSON SQL, LOB SQL, data-type syntax restrictions, Oracle-difference, migration-risk, and compatibility items. |
| `FCA-J012` | `ToDo` | General Reference data type catalog | Extract data type, LOB, JSON, Temporary LOB, direct-key, conversion, and data-type compatibility items. |
| `FCA-J013` | `ToDo` | Property catalog core path and storage | Extract core identity, path, database-file, memory-directory, storage, log-anchor, and startup/restart property items. |
| `FCA-J014` | `ToDo` | Property catalog memory log cache and capacity | Extract memory, disk, volatile, log-size, checkpoint, cache, result-cache, plan-cache, and capacity-limit property items. |
| `FCA-J015` | `ToDo` | Property catalog optimizer session locale and timeout | Extract optimizer, normalization, lock, timeout, autocommit, session, locale, and performance property items. |
| `FCA-J016` | `ToDo` | Property catalog security replication network and DB Link | Extract account, access-list, SSL/TLS, replication, network, port, SQL-apply, and DB Link property items. |
| `FCA-J017` | `ToDo` | Dictionary and meta table catalog | Extract dictionary table, meta table, object metadata, privilege, PSM, trigger, job, and schema lookup items. |
| `FCA-J018` | `ToDo` | Performance view operational catalog | Extract performance view names, purposes, version availability, operational grouping, query timing, and safe check SQL items. |
| `FCA-J019` | `ToDo` | View column and metadata guardrail catalog | Extract key column coverage, patch-sensitive column limits, installed-metadata checks, and view-column guardrail rows. |
| `FCA-J020` | `ToDo` | Error catalog storage backup recovery and tablespace | Extract storage, backup, recovery, datafile, log, log-anchor, archive, lock, and tablespace error items. |
| `FCA-J021` | `ToDo` | Error catalog SQL datatype JSON LOB and regular expression | Extract SQL parser, DDL, constraint, datatype, conversion, JSON, Temporary LOB, LOB, and regular-expression error items. |
| `FCA-J022` | `ToDo` | Error catalog client network replication and tools | Extract client, network, SSL/TLS, replication, DB Link, iSQL, iLoader, utility, APRE, CLI/ODBC, and Log Analyzer error items. |
| `FCA-J023` | `ToDo` | Error catalog Spatial and remaining grouped-code guardrails | Extract Spatial and remaining low-frequency grouped-code error items, including exact-code guardrails where sources are incomplete. |
| `FCA-J024` | `ToDo` | Performance tuning and optimizer catalog | Extract execution plan, hint, statistics, index, optimizer, wait, lock, session, monitoring, and tuning workflow items. |
| `FCA-J025` | `ToDo` | Monitoring API and SNMP catalog | Extract Monitoring API, SNMP object, metric, port, counter, mapping, output, and runtime-check items. |
| `FCA-J026` | `ToDo` | Replication and HA catalog | Extract topology, state, mode, DDL, compatibility, gap, conflict, protected state-change, and unsafe-operation items. |
| `FCA-J027` | `ToDo` | CDC Log Analyzer and RepMgr catalog | Extract CDC API, XLog, ACK/restart, Log Analyzer, Replication Manager, GUI-replacement, release, and diagnostic items. |
| `FCA-J028` | `ToDo` | Security SSL TLS and network catalog | Extract certificate, TLS, replication SSL, client/server, network property, port, access-list, and diagnostic items. |
| `FCA-J029` | `ToDo` | PSM and external procedure catalog | Extract PSM, package, trigger, library, external procedure, type mapping, deployment, compile, and runtime-evidence items. |
| `FCA-J030` | `ToDo` | JDBC Java Spring and Hibernate catalog | Extract JDBC URLs, driver classes, Java compatibility, Adapter for JDBC, Spring, Hibernate, failover, property, and API items. |
| `FCA-J031` | `ToDo` | C CLI ODBC and Precompiler catalog | Extract CLI, ODBC, Altibase C Interface, Precompiler, DSN, diagnostics, LOB, JSON LOB, compile, and runtime items. |
| `FCA-J032` | `ToDo` | iSQL and iLoader catalog | Extract iSQL session commands, host variables, load/export workflows, iLoader options, files, examples, and diagnostics. |
| `FCA-J033` | `ToDo` | Utilities and operation tools catalog | Extract utility commands, options, outputs, diagnostics, dataCompJ, dump tools, AKU-related utility, and installed-tool guardrail items. |
| `FCA-J034` | `ToDo` | Migration and Oracle compatibility catalog | Extract Migration Center, Adapter for Oracle, conversion, unsupported objects, report, PSM review, validation, and Oracle-difference items. |
| `FCA-J035` | `ToDo` | DB Link and external connectors catalog | Extract DB Link, Hadoop, linker, connector setup, DB Link views/properties, third-party procedure, and validation items. |
| `FCA-J036` | `ToDo` | Kubernetes AKU and cloud catalog | Extract container, Kubernetes, AKU, image, environment, lifecycle, replication/TLS caution, and operational caveat items. |
| `FCA-J037` | `ToDo` | Spatial NiFi Tableau and miscellaneous integration catalog | Extract Spatial SQL, GEOMETRY, altiShapeLoader, NiFi, Tableau, JDBC setting, third-party guide, and validation items. |
| `FCA-J038` | `ToDo` | Technical documents and cross-family support catalog | Extract source-backed items from selected technical documents and cross-family support files that are not fully owned by earlier catalog jobs. |
| `FCA-J039` | `ToDo` | Catalog consolidation and QA | Validate source item catalog schema, stable IDs, duplicate rows, controlled vocabulary values, source-family completeness, and evidence fields before matrix mapping. |
| `FCA-J040` | `ToDo` | Source-to-attachment matrix build | Map every catalog row to an attachment owner, initial coverage disposition, attachment anchor, guardrail reason, and evidence command. |
| `FCA-J041` | `ToDo` | Content remediation SQL data types and properties | Fix missing source-backed items in SQL, data type, property, JSON, LOB, and Oracle-difference attachment areas. |
| `FCA-J042` | `ToDo` | Content remediation operations backup recovery and errors | Fix missing source-backed items in installation, administration, backup/recovery, destructive-operation, and error/troubleshooting attachment areas. |
| `FCA-J043` | `ToDo` | Content remediation views performance replication and security | Fix missing source-backed items in dictionary/performance views, tuning, monitoring, replication, CDC, SSL/TLS, and network attachment areas. |
| `FCA-J044` | `ToDo` | Content remediation tools APIs clients and connectors | Fix missing source-backed items in PSM, Java/JDBC, C/CLI/ODBC, iSQL, iLoader, utilities, DB Link, and external connector attachment areas. |
| `FCA-J045` | `ToDo` | Content remediation migration cloud spatial and integrations | Fix missing source-backed items in migration, Oracle compatibility, Kubernetes, AKU, Spatial, NiFi, Tableau, and miscellaneous integration attachment areas. |
| `FCA-J046` | `ToDo` | Retrieval remediation core reference attachments | Convert retrieval-weak rows for core reference attachments 00 through 09 into covered-by-routing rows with headings, aliases, indexes, and cross-links. |
| `FCA-J047` | `ToDo` | Retrieval remediation developer tools and integrations | Convert retrieval-weak rows for attachments 10 through 19 into covered-by-routing rows with headings, aliases, indexes, and cross-links. |
| `FCA-J048` | `ToDo` | Guardrail and out-of-scope audit | Verify every guardrail and out-of-scope row is truly source-limited, patch-specific, environment-limited, or customer-evidence-dependent. |
| `FCA-J049` | `ToDo` | Answer contract and prompt alignment | Update GPT instructions only where needed so exact tokens, item-block shapes, missing-input rules, and guardrails are used in answers. |
| `FCA-J050` | `ToDo` | Validation and targeted answerability | Run repository validation, source-to-attachment checks, targeted answerability for failed/protected/exact-token rows, and a selected full rerun if feasible. |
| `FCA-J051` | `ToDo` | Final full coverage audit report | Produce final sign-off with source scope, method, coverage totals, remaining guardrails, validation output, and no unresolved Missing or Retrieval-weak rows. |

## Execution Notes

This workflow has been converted into an executable `job-orchestrator` workflow:

- `requirements.md`, `prompts/FCA-J*.md`, `run-all.sh`, `logs/`, and `rollbacks/`
  are present.
- `run-all.sh` invokes `codex exec --cd` from the repository root by default.
- `run-all.sh` stops on dirty project files before each job.
- Each successful job must run scoped verification, review the final diff, create
  a focused project-file commit, commit workflow status, and leave project files clean.
- Do not run `run-all.sh` automatically; the user starts or resumes it manually.

## Acceptance Checklist For This Workflow

- `jobs.tsv` and `jobs.md` stay aligned.
- Every job has a matching prompt file.
- Every prompt has source review, catalog or remediation steps, validation, final diff
  review, focused commit, and clean handoff requirements.
- `bash -n .codex-jobs/altibase-gpt-full-coverage-audit/run-all.sh` passes.
- The final audit has no unresolved `Missing` or unresolved `Retrieval-weak` catalog
  rows.
