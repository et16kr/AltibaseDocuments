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
- `git status --short` was clean before this job list was created.
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

The original plan proposed 34 jobs as a first cut. This reviewed job list uses 48 jobs
because several source families are too large for one reliable Codex execution:

- properties already have `484` inventoried names and need four catalog jobs;
- error coverage previously required multiple exact-code and grouped-code slices;
- dictionary/performance view coverage spans meta tables, operational views, and
  patch-sensitive column guardrails;
- remediation must be bounded by attachment groups instead of broad all-domain waves;
- catalog consolidation must happen before source-to-attachment matrix mapping.

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

The future workflow should create or update:

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
`retrieval_risk=high`. FCA-J037, FCA-J043, FCA-J044, and FCA-J047 must explicitly use
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
- FCA-J004-FCA-J009: broad source-family catalog extraction.
- FCA-J010-FCA-J013: property catalog extraction split by property family.
- FCA-J014-FCA-J016: dictionary, performance view, and view-column guardrail catalog extraction.
- FCA-J017-FCA-J020: error catalog extraction split by error family.
- FCA-J021-FCA-J035: remaining catalog extraction for operations, tools, APIs,
  connectors, integrations, and technical support documents.
- FCA-J036-FCA-J037: catalog QA and source-to-attachment matrix mapping.
- FCA-J038-FCA-J042: content remediation split by attachment group.
- FCA-J043-FCA-J044: retrieval remediation split by attachment group.
- FCA-J045-FCA-J048: guardrail audit, answer contract alignment, validation, and final sign-off.

## Job Scope Matrix

| ID | Primary target areas | Expected durable output |
| --- | --- | --- |
| `FCA-J001` | Current workflow status, latest benchmark, existing reports | Preflight evidence section and locked latest-run baseline. |
| `FCA-J002` | `source_inventory.md`, `coverage_matrix.md`, selected source roots | `source_corpus_lock.md`. |
| `FCA-J003` | Catalog schema, controlled vocabularies, extraction/check scripts | Catalog schema, stable ID rules, and reusable script/check plan. |
| `FCA-J004` | Release notes, patch notes, supported platforms | Catalog rows for release, platform, patch, upgrade, and feature-boundary items. |
| `FCA-J005` | Getting Started and Installation manuals | Catalog rows for install, database creation, startup/shutdown, and first checks. |
| `FCA-J006` | Administrator manuals and administrative SQL | Catalog rows for backup, recovery, tablespace, privilege, storage, and protected operations. |
| `FCA-J007` | SQL Reference DDL/DCL/admin SQL | Catalog rows for DDL, DCL, replication SQL, destructive SQL, and grammar. |
| `FCA-J008` | SQL Reference DML/functions/JSON/LOB | Catalog rows for DML, expressions, functions, data type syntax, and Oracle differences. |
| `FCA-J009` | General Reference 1 data types | Catalog rows for data types, LOB, JSON, Temporary LOB, direct key, and conversion. |
| `FCA-J010` | Core/path/storage property families | Catalog rows for core identity, paths, files, storage, log anchors, and startup/restart properties. |
| `FCA-J011` | Memory/log/cache/capacity property families | Catalog rows for memory, disk, volatile, log, checkpoint, cache, and capacity properties. |
| `FCA-J012` | Optimizer/session/locale/timeout property families | Catalog rows for optimizer, session, locale, lock, timeout, autocommit, and performance properties. |
| `FCA-J013` | Security/replication/network/DB Link property families | Catalog rows for account, access, TLS, replication, network, port, SQL-apply, and DB Link properties. |
| `FCA-J014` | Dictionary tables and meta tables | Catalog rows for schema, object, privilege, PSM, trigger, job, and metadata lookup items. |
| `FCA-J015` | Performance views | Catalog rows for performance view names, purposes, version availability, grouping, timing, and check SQL. |
| `FCA-J016` | View columns and installed-metadata guardrails | Catalog rows for key columns, patch-sensitive column limits, and installed metadata checks. |
| `FCA-J017` | Storage/backup/recovery/tablespace errors | Catalog rows for exact and grouped storage, backup, recovery, log, archive, and tablespace errors. |
| `FCA-J018` | SQL/datatype/JSON/LOB/regex errors | Catalog rows for parser, DDL, constraint, datatype, conversion, JSON, Temporary LOB, LOB, and regex errors. |
| `FCA-J019` | Client/network/replication/tool errors | Catalog rows for client, network, SSL/TLS, replication, DB Link, iSQL, iLoader, utility, APRE, CLI/ODBC, and Log Analyzer errors. |
| `FCA-J020` | Spatial and remaining grouped-code errors | Catalog rows for Spatial and low-frequency grouped-code handling with explicit guardrails. |
| `FCA-J021` | Performance Tuning Guides | Catalog rows for optimizer, plans, hints, statistics, waits, locks, and tuning workflows. |
| `FCA-J022` | Monitoring API and SNMP manuals | Catalog rows for API/SNMP metrics, counters, ports, and runtime checks. |
| `FCA-J023` | Replication manuals and related SQL | Catalog rows for replication topology, states, DDL, compatibility, gaps, and conflicts. |
| `FCA-J024` | CDC, Log Analyzer, RepMgr | Catalog rows for CDC/XLog/API, ACK/restart, RepMgr, release, and diagnostic items. |
| `FCA-J025` | SSL/TLS, replication SSL, network docs | Catalog rows for TLS, certificates, replication SSL separation, ports, and diagnostics. |
| `FCA-J026` | Stored Procedures and External Procedures manuals | Catalog rows for PSM, packages, triggers, external procedures, type mapping, and deployment. |
| `FCA-J027` | JDBC, Adapter, Spring, Hibernate, Java compatibility | Catalog rows for Java/JDBC/Spring/Hibernate and Adapter behavior. |
| `FCA-J028` | CLI, ODBC, C Interface, Precompiler | Catalog rows for C-facing APIs, diagnostics, DSN, LOB, JSON LOB, and compile cautions. |
| `FCA-J029` | iSQL and iLoader manuals | Catalog rows for session commands, load/export workflows, options, and diagnostics. |
| `FCA-J030` | Utilities and dataCompJ manuals | Catalog rows for utility commands, output fields, diagnostics, dump tools, and AKU utility items. |
| `FCA-J031` | Migration Center and Adapter for Oracle | Catalog rows for conversion, unsupported objects, reports, PSM review, and validation. |
| `FCA-J032` | DB Link, Hadoop, third-party connector guides | Catalog rows for DB Link, linker, Hadoop, connector setup, views, properties, and checks. |
| `FCA-J033` | Kubernetes, AKU, container/cloud guides | Catalog rows for Kubernetes, AKU, image/env/lifecycle, and operational caveats. |
| `FCA-J034` | Spatial, altiShapeLoader, NiFi, Tableau | Catalog rows for spatial SQL/functions, loaders, NiFi/Tableau settings, and validation. |
| `FCA-J035` | Technical documents and cross-family support files | Catalog rows for unique technical-document facts not fully owned by earlier jobs. |
| `FCA-J036` | Whole catalog | Validated `source_item_catalog.tsv`, duplicate/ID report, vocabulary checks, and source-family completeness notes. |
| `FCA-J037` | Catalog, coverage matrix, attachments | Initial `source_to_attachment_matrix.tsv` with dispositions and evidence. |
| `FCA-J038` | Attachments `03`, `04`, `05` and related reports | Remediated SQL, data type, property, JSON, LOB, and Oracle-difference gaps. |
| `FCA-J039` | Attachments `01`, `02`, `07` and related reports | Remediated installation, administration, backup/recovery, destructive-operation, and error gaps. |
| `FCA-J040` | Attachments `06`, `08`, `09`, `18` and related reports | Remediated view, performance, monitoring, replication, CDC, TLS, and network gaps. |
| `FCA-J041` | Attachments `10`, `11`, `12`, `13`, `14`, `16` and related reports | Remediated PSM, Java/JDBC, C/CLI/ODBC, iSQL, iLoader, utility, DB Link, and connector gaps. |
| `FCA-J042` | Attachments `15`, `17`, `19` and related reports | Remediated migration, cloud, Kubernetes, AKU, Spatial, NiFi, Tableau, and misc integration gaps. |
| `FCA-J043` | Attachments `00` through `09` | Remediated retrieval-weak core reference rows and updated retrieval weakness register. |
| `FCA-J044` | Attachments `10` through `19` | Remediated retrieval-weak developer/tool/integration rows and updated retrieval weakness register. |
| `FCA-J045` | Guardrail and out-of-scope rows | Audited guardrail register with required missing-input and safest-next-check patterns. |
| `FCA-J046` | GPT instructions and answer contract | Updated instruction/prompt alignment if needed. |
| `FCA-J047` | Validation scripts and answerability checks | Validation output and targeted answerability results for remediated/high-risk rows. |
| `FCA-J048` | Final audit reports | `final_full_coverage_audit.md` and final readiness decision. |

## Jobs

| ID | Status | Title | Goal |
| --- | --- | --- | --- |
| `FCA-J001` | `ToDo` | Preflight and benchmark evidence lock | Confirm the current review/remediation cycle is complete, the worktree is clean, previous jobs are committed, and the latest full benchmark run is locked as audit evidence. |
| `FCA-J002` | `ToDo` | Source corpus lock | Freeze the exact selected source roots, source families, authoritative Korean sources, extraction aids, exclusions, and customer-facing scope boundaries. |
| `FCA-J003` | `ToDo` | Catalog schema and extraction scripts | Define the source item catalog schema, controlled vocabularies, stable ID rules, and reusable extraction and coverage-check scripts where practical. |
| `FCA-J004` | `ToDo` | Release notes patch notes and platform catalog | Extract release, patch, feature, platform, upgrade, and exact version-boundary items into the source item catalog. |
| `FCA-J005` | `ToDo` | Installation and getting-started catalog | Extract installation, environment setup, database creation, startup, shutdown, licensing, and first-check items. |
| `FCA-J006` | `ToDo` | Administrator operations catalog | Extract backup, recovery, archive log, tablespace, user, privilege, storage, server-mode, and protected-operation items. |
| `FCA-J007` | `ToDo` | SQL Reference DDL catalog | Extract DDL, DCL, administrative SQL, replication SQL, Log Analyzer SQL, destructive SQL, privileges, and grammar items. |
| `FCA-J008` | `ToDo` | SQL Reference DML function and catalog syntax | Extract DML, expressions, functions, JSON, LOB, object-name, syntax restriction, and Oracle-difference items. |
| `FCA-J009` | `ToDo` | General Reference data type catalog | Extract data type, LOB, JSON, Temporary LOB, direct-key, conversion, and data-type compatibility items. |
| `FCA-J010` | `ToDo` | Property catalog core path and storage | Extract core identity, path, database-file, memory-directory, storage, log-anchor, and startup/restart property items. |
| `FCA-J011` | `ToDo` | Property catalog memory log cache and capacity | Extract memory, disk, volatile, log-size, checkpoint, cache, result-cache, plan-cache, and capacity-limit property items. |
| `FCA-J012` | `ToDo` | Property catalog optimizer session locale and timeout | Extract optimizer, normalization, lock, timeout, autocommit, session, locale, and performance property items. |
| `FCA-J013` | `ToDo` | Property catalog security replication network and DB Link | Extract account, access-list, SSL/TLS, replication, network, port, SQL-apply, and DB Link property items. |
| `FCA-J014` | `ToDo` | Dictionary and meta table catalog | Extract dictionary table, meta table, object metadata, privilege, PSM, trigger, job, and schema lookup items. |
| `FCA-J015` | `ToDo` | Performance view operational catalog | Extract performance view names, purposes, version availability, operational grouping, query timing, and safe check SQL items. |
| `FCA-J016` | `ToDo` | View column and metadata guardrail catalog | Extract key column coverage, patch-sensitive column limits, installed-metadata checks, and view-column guardrail rows. |
| `FCA-J017` | `ToDo` | Error catalog storage backup recovery and tablespace | Extract storage, backup, recovery, datafile, log, log-anchor, archive, lock, and tablespace error items. |
| `FCA-J018` | `ToDo` | Error catalog SQL datatype JSON LOB and regular expression | Extract SQL parser, DDL, constraint, datatype, conversion, JSON, Temporary LOB, LOB, and regular-expression error items. |
| `FCA-J019` | `ToDo` | Error catalog client network replication and tools | Extract client, network, SSL/TLS, replication, DB Link, iSQL, iLoader, utility, APRE, CLI/ODBC, and Log Analyzer error items. |
| `FCA-J020` | `ToDo` | Error catalog Spatial and remaining grouped-code guardrails | Extract Spatial and remaining low-frequency grouped-code error items, including exact-code guardrails where sources are incomplete. |
| `FCA-J021` | `ToDo` | Performance tuning and optimizer catalog | Extract execution plan, hint, statistics, index, optimizer, wait, lock, session, monitoring, and tuning workflow items. |
| `FCA-J022` | `ToDo` | Monitoring API and SNMP catalog | Extract Monitoring API, SNMP object, metric, port, counter, mapping, output, and runtime-check items. |
| `FCA-J023` | `ToDo` | Replication and HA catalog | Extract topology, state, mode, DDL, compatibility, gap, conflict, protected state-change, and unsafe-operation items. |
| `FCA-J024` | `ToDo` | CDC Log Analyzer and RepMgr catalog | Extract CDC API, XLog, ACK/restart, Log Analyzer, Replication Manager, GUI-replacement, release, and diagnostic items. |
| `FCA-J025` | `ToDo` | Security SSL TLS and network catalog | Extract certificate, TLS, replication SSL, client/server, network property, port, access-list, and diagnostic items. |
| `FCA-J026` | `ToDo` | PSM and external procedure catalog | Extract PSM, package, trigger, library, external procedure, type mapping, deployment, compile, and runtime-evidence items. |
| `FCA-J027` | `ToDo` | JDBC Java Spring and Hibernate catalog | Extract JDBC URLs, driver classes, Java compatibility, Adapter for JDBC, Spring, Hibernate, failover, property, and API items. |
| `FCA-J028` | `ToDo` | C CLI ODBC and Precompiler catalog | Extract CLI, ODBC, Altibase C Interface, Precompiler, DSN, diagnostics, LOB, JSON LOB, compile, and runtime items. |
| `FCA-J029` | `ToDo` | iSQL and iLoader catalog | Extract iSQL session commands, host variables, load/export workflows, iLoader options, files, examples, and diagnostics. |
| `FCA-J030` | `ToDo` | Utilities and operation tools catalog | Extract utility commands, options, outputs, diagnostics, dataCompJ, dump tools, AKU-related utility, and installed-tool guardrail items. |
| `FCA-J031` | `ToDo` | Migration and Oracle compatibility catalog | Extract Migration Center, Adapter for Oracle, conversion, unsupported objects, report, PSM review, validation, and Oracle-difference items. |
| `FCA-J032` | `ToDo` | DB Link and external connectors catalog | Extract DB Link, Hadoop, linker, connector setup, DB Link views/properties, third-party procedure, and validation items. |
| `FCA-J033` | `ToDo` | Kubernetes AKU and cloud catalog | Extract container, Kubernetes, AKU, image, environment, lifecycle, replication/TLS caution, and operational caveat items. |
| `FCA-J034` | `ToDo` | Spatial NiFi Tableau and miscellaneous integration catalog | Extract Spatial SQL, GEOMETRY, altiShapeLoader, NiFi, Tableau, JDBC setting, third-party guide, and validation items. |
| `FCA-J035` | `ToDo` | Technical documents and cross-family support catalog | Extract source-backed items from selected technical documents and cross-family support files that are not fully owned by earlier catalog jobs. |
| `FCA-J036` | `ToDo` | Catalog consolidation and QA | Validate source item catalog schema, stable IDs, duplicate rows, controlled vocabulary values, source-family completeness, and evidence fields before matrix mapping. |
| `FCA-J037` | `ToDo` | Source-to-attachment matrix build | Map every catalog row to an attachment owner, initial coverage disposition, attachment anchor, guardrail reason, and evidence command. |
| `FCA-J038` | `ToDo` | Content remediation SQL data types and properties | Fix missing source-backed items in SQL, data type, property, JSON, LOB, and Oracle-difference attachment areas. |
| `FCA-J039` | `ToDo` | Content remediation operations backup recovery and errors | Fix missing source-backed items in installation, administration, backup/recovery, destructive-operation, and error/troubleshooting attachment areas. |
| `FCA-J040` | `ToDo` | Content remediation views performance replication and security | Fix missing source-backed items in dictionary/performance views, tuning, monitoring, replication, CDC, SSL/TLS, and network attachment areas. |
| `FCA-J041` | `ToDo` | Content remediation tools APIs clients and connectors | Fix missing source-backed items in PSM, Java/JDBC, C/CLI/ODBC, iSQL, iLoader, utilities, DB Link, and external connector attachment areas. |
| `FCA-J042` | `ToDo` | Content remediation migration cloud spatial and integrations | Fix missing source-backed items in migration, Oracle compatibility, Kubernetes, AKU, Spatial, NiFi, Tableau, and miscellaneous integration attachment areas. |
| `FCA-J043` | `ToDo` | Retrieval remediation core reference attachments | Convert retrieval-weak rows for core reference attachments 00 through 09 into covered-by-routing rows with headings, aliases, indexes, and cross-links. |
| `FCA-J044` | `ToDo` | Retrieval remediation developer tools and integrations | Convert retrieval-weak rows for attachments 10 through 19 into covered-by-routing rows with headings, aliases, indexes, and cross-links. |
| `FCA-J045` | `ToDo` | Guardrail and out-of-scope audit | Verify every guardrail and out-of-scope row is truly source-limited, patch-specific, environment-limited, or customer-evidence-dependent. |
| `FCA-J046` | `ToDo` | Answer contract and prompt alignment | Update GPT instructions only where needed so exact tokens, item-block shapes, missing-input rules, and guardrails are used in answers. |
| `FCA-J047` | `ToDo` | Validation and targeted answerability | Run repository validation, source-to-attachment checks, targeted answerability for failed/protected/exact-token rows, and a selected full rerun if feasible. |
| `FCA-J048` | `ToDo` | Final full coverage audit report | Produce final sign-off with source scope, method, coverage totals, remaining guardrails, validation output, and no unresolved Missing or Retrieval-weak rows. |

## Execution Notes

This workflow has been converted into an executable `job-orchestrator` workflow:

- `requirements.md`, `prompts/FCA-J*.md`, `run-all.sh`, `logs/`, and `rollbacks/`
  are present.
- `run-all.sh` invokes `codex exec --cd` from the repository root by default.
- `run-all.sh` stops on dirty project files before each job.
- Each successful job must run scoped verification, review the final diff, create
  a focused git commit, and leave project files clean.
- Do not run `run-all.sh` automatically; the user starts or resumes it manually.

## Acceptance Checklist For This Workflow

- `jobs.tsv` and `jobs.md` stay aligned.
- Every job has a matching prompt file.
- Every prompt has source review, catalog or remediation steps, validation, final diff
  review, focused commit, and clean handoff requirements.
- `bash -n .codex-jobs/altibase-gpt-full-coverage-audit/run-all.sh` passes.
- The final audit has no unresolved `Missing` or unresolved `Retrieval-weak` catalog
  rows.
