# Stage 3 Attachments Follow-Up Plan

- Job: `S3-J001`
- Updated by: `S3-J002`
- Date: 2026-05-19
- Scope: planning evidence for Stage 3 attachment follow-up
- Status: Ready for guarded domain attachment follow-up after scope and validation
  scaffolding

## Requirement And Boundary

Stage 3 replans and performs the still-needed answer-ready attachment follow-up
work using the validated Stage 1 source pack, Korean-aligned English baseline,
durable benchmark inventories, and Stage 2 playbooks. This plan records how
downstream Stage 3 jobs should proceed after the preflight gate. It does not edit
attachment content.

Allowed Stage 3 outputs remain limited to the paths listed in
`.codex-jobs/altibase-gpt-stage-03-attachments-followup/prompts/common-stage-03.md`.
Stage 3 may edit existing `GPTs/attachments/*.md`, attachment scripts, Stage 3
crosswalks, Stage 3 validation reports, and Stage 3 readiness reports. Stage 3
must not edit original source files and must not create `GPTs/upload_package/`
content.

The attachment set must remain exactly `20` customer-facing Markdown files under
`GPTs/attachments/`, excluding `README.md`.

## Design Note

This plan changes documentation structure by adding Stage 3 planning evidence under
`GPTs/reports/`.

`S3-J002` adds the first executable Stage 3 attachment validation scaffold and the
machine-checkable attachment follow-up scope TSV. It does not add Altibase behavior,
broaden source claims, edit customer-facing attachment text, or create
`GPTs/upload_package/` content. Later domain jobs must still open the exact source
routes before changing answer-ready product behavior.

## Starting Evidence

| Evidence area | Starting source |
| --- | --- |
| Product objective | `GPTs/reports/customer_agent_enablement_requirements.md` |
| Stage 1 readiness | `GPTs/reports/customer_agent_enablement_stage_01_readiness.md` |
| Source-preserving pack | `GPTs/source_pack/source_manifest.tsv`, `GPTs/source_pack/source_to_shard_manifest.tsv`, `GPTs/source_pack/source_pack_shard_*.md`, `GPTs/source_pack/source_pack_validation.md` |
| Korean-aligned English baseline | `GPTs/korean_aligned_english/baseline_manifest.tsv`, `GPTs/korean_aligned_english/alignment_validation.md`, `GPTs/korean_aligned_english/*.md` |
| Stage 1 source-to-baseline routing | `GPTs/reports/source_pack_to_korean_aligned_english_crosswalk.tsv` |
| Stage 2 readiness | `GPTs/reports/customer_agent_enablement_stage_02_readiness.md` |
| Stage 2 playbook routes | `GPTs/agent_playbooks/playbook_manifest.tsv`, `GPTs/agent_playbooks/*.md` |
| Stage 2 playbook crosswalks | `GPTs/reports/source_pack_to_playbook_crosswalk.tsv`, `GPTs/reports/korean_aligned_english_to_playbook_crosswalk.tsv` |
| Stage 2 scenarios and rubric | `GPTs/agent_playbooks/test_scenarios.md`, `GPTs/agent_playbooks/scenario_judge_rubric.md` |
| Stage 2 validation and gaps | `GPTs/agent_playbooks/playbook_validation.md`, `GPTs/reports/agent_playbook_gap_register.md` |
| Conflict and limitation guardrails | `GPTs/reports/source_conflict_register.md` |
| Durable answerability evidence | `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_095919/` |
| Attachment remediation inventory | `GPTs/reports/answerability_failure_remediation_inventory_20260517.md` |
| Exact-token gap inventory | `GPTs/reports/exact_token_gap_inventory_20260517.md` |

## Attachment Boundary

The current customer-facing attachment package is exactly the required `20`
Markdown files, excluding `README.md`:

| Attachment | Primary Stage 3 use |
| --- | --- |
| `GPTs/attachments/00_version_release_platform.md` | Version, release, platform, package, and patch-sensitive routing support. |
| `GPTs/attachments/01_getting_started_installation.md` | Installation, startup, shutdown, privilege, path, and first-run runbooks. |
| `GPTs/attachments/02_administration_operations.md` | Administration, backup/recovery, tablespaces, datafiles, log anchors, and protected operations. |
| `GPTs/attachments/03_sql_ddl_generation.md` | DDL, DCL, destructive SQL, tablespaces, storage, partitions, constraints, and validation SQL. |
| `GPTs/attachments/04_sql_dml_oracle_compatibility.md` | DML, expressions, functions, Oracle differences, regular expressions, and SQL examples. |
| `GPTs/attachments/05_data_types_properties.md` | Data types, properties, capacity, session, optimizer, network, replication, and security property blocks. |
| `GPTs/attachments/06_data_dictionary_performance_views.md` | Dictionary and performance views, columns, metadata checks, and validation SQL. |
| `GPTs/attachments/07_error_messages_troubleshooting.md` | Error codes, symptoms, root-cause prompts, log checks, and escalation packets. |
| `GPTs/attachments/08_performance_tuning_monitoring.md` | Performance tuning, optimizer, execution plans, waits, locks, Monitoring API, and SNMP routing. |
| `GPTs/attachments/09_replication_ha_cdc.md` | Replication topology, state, control SQL, CDC, Log Analyzer, Replication Manager, and replication SSL. |
| `GPTs/attachments/10_psm_stored_external_procedures.md` | PSM, stored procedures, external procedures, and related errors or examples. |
| `GPTs/attachments/11_java_jdbc_spring.md` | Java, JDBC, Spring, Hibernate, driver, URL, and connection diagnostics. |
| `GPTs/attachments/12_c_cli_odbc_precompiler.md` | CLI, ODBC, C Interface, Precompiler/APRE, compile/link/runtime checks, and diagnostics. |
| `GPTs/attachments/13_isql_iloader_basic_tools.md` | iSQL, iLoader, spool/log handling, load/export, and tool verification. |
| `GPTs/attachments/14_utilities_operation_tools.md` | Utilities, dataCompJ, dump tools, altiComp, aexport, and operation tool details. |
| `GPTs/attachments/15_migration_oracle_compatibility.md` | Migration Center, Adapter for Oracle, Oracle compatibility, and conversion risks. |
| `GPTs/attachments/16_dblink_external_connectors.md` | DB Link, external connectors, Hadoop, and connector routing. |
| `GPTs/attachments/17_kubernetes_aku_cloud.md` | Kubernetes, AKU, cloud/platform caveats, and YAML or deployment checks. |
| `GPTs/attachments/18_security_ssl_tls.md` | Security, TLS, certificate, access-control, network, and replication SSL boundaries. |
| `GPTs/attachments/19_spatial_nifi_tableau_misc.md` | Spatial, NiFi, Tableau, and miscellaneous integration topics. |

Do not add new customer-facing attachment package files. If a later job needs a new
topic shape, it must refactor within the existing `00` through `19` files.

## Stage 3 Work Plan

| Job | Planned outcome | Primary evidence | Attachment targets |
| --- | --- | --- | --- |
| `S3-J002` | Create Stage 3 scope TSV, validation scaffolding, and source/playbook routing plan. Completed by `GPTs/reports/stage_03_attachment_followup_scope.tsv` and `GPTs/attachments/scripts/validate_attachments.py`. | Preflight report, this plan, benchmark inventories, Stage 2 playbook crosswalks. | Reports and scripts only. |
| `S3-J003` | Remediate core identity, path, database-file, log-anchor, storage, and foundational property gaps. | `J004` remediation matrix, property/source routes, `APB-000004`, `APB-000016`. | `05`, `00`, `01`, `02`, `06`. |
| `S3-J004` | Remediate memory, disk, volatile, log-size, cache, result-cache, and capacity-limit property gaps. | `J005`, exact-token inventory, `APB-000004`, `APB-000016`. | `05`, `00`, `02`, `08`. |
| `S3-J005` | Remediate optimizer, session, locale, lock, timeout, autocommit, transaction, and performance property gaps. | `J006`, exact-token inventory, `APB-000004`, `APB-000005`, `APB-000015`. | `05`, `08`, `06`. |
| `S3-J006` | Remediate account, access-list, SSL/TLS, replication, network, port, and SQL-apply property gaps. | `J007`, security/replication routes, `APB-000004`, `APB-000007`, `APB-000008`. | `05`, `09`, `18`. |
| `S3-J007` | Remediate tablespace, datafile, table, partition, index, constraint, LOB storage, queue, and destructive DDL gaps. | `J008`, SQL/token inventory, `APB-000002`, `APB-000016`. | `03`, `02`, `05`. |
| `S3-J008` | Remediate DML, functions, data type, JSON, LOB, object-name, regular-expression, and Oracle-difference gaps. | `J009`, SQL/token inventory, `APB-000003`, `APB-000015`. | `04`, `05`, `15`. |
| `S3-J009` | Remediate exact error-code, SQL/property error, tool/driver error, symptom, log, and troubleshooting gaps. | `J010`, error routes, `APB-000013`. | `07`, `13`, `14`. |
| `S3-J010` | Remediate installation, startup, account, privilege, tablespace, datafile, loganchor, and beginner-to-veteran runbook gaps. | `J011`, runbook routes, `APB-000001`, `APB-000016`. | `01`, `02`, `13`. |
| `S3-J011` | Remediate backup, recovery, archive log, RESETLOGS, DROP/DISCARD/REUSE, and protected-operation gaps. | `J012`, protected-topic blockers, `APB-000006`, `APB-000016`. | `02`, `03`, `07`. |
| `S3-J012` | Remediate replication topology, state, DDL, control SQL, gap, compatibility, and guardrail gaps. | `J013`, replication routes, `APB-000007`, `APB-000002`. | `09`, `03`, `06`. |
| `S3-J013` | Remediate CDC, Log Analyzer, Replication Manager, replication SSL, ordinary TLS, certificate, port, and network diagnostics. | `J014`, `CONF-000008`, `APB-000007`, `APB-000008`, `APB-000012`. | `09`, `16`, `18`. |
| `S3-J014` | Remediate dictionary/performance view, optimizer, execution plan, wait, lock, session, Monitoring API, and SNMP gaps. | `J015`, view/performance routes, `APB-000005`, `APB-000013`. | `06`, `08`. |
| `S3-J015` | Remediate PSM, external procedure, CLI, ODBC, ACI, Precompiler, iSQL, iLoader, utilities, and LOB/API gaps. | `J016`, client/tool routes, `APB-000009`, `APB-000011`. | `10`, `12`, `13`, `14`. |
| `S3-J016` | Remediate Java, JDBC, connectors, migration, Kubernetes, Spatial, NiFi, Tableau, and miscellaneous integration gaps. | `J017`, integration routes, `APB-000010`, `APB-000012`. | `11`, `15`, `16`, `17`, `19`. |
| `S3-J017` | Update retrieval aliases, cross-links, source/playbook-to-attachment crosswalks, gap registers, and attachment validation reports. | All prior Stage 3 scope rows, benchmark inventories, playbook/source routes. | Reports, scripts, and affected attachments. |
| `S3-J018` | Review all Stage 3 outputs, rerun validation, preserve guardrails, and write Stage 3 readiness. | Stage 3 validation, final diff, gap/register state, attachment count. | `customer_agent_enablement_stage_03_readiness.md` and validation reports. |

Design note for `S3-J010`: this job does not change attachment architecture or upload-package structure. It adds compact answer-route anchors inside the existing installation, administration, and iSQL attachments so long runbooks retrieve as beginner-to-veteran sequences with prerequisites, commands, expected states, validation SQL, and missing-input stop points.

Design note for `S3-J011`: this job does not change attachment architecture or upload-package structure. It closes the J012 backup/recovery protected-operation row inside the existing administration, SQL-generation, and troubleshooting attachments by using compact answer anchors for archive-log mode, online backup, media recovery, `RESETLOGS`, current-versus-historical log anchors, temporary datafile recovery, `DROP`/`DISCARD`/`REUSE`, and escalation inputs. The completed scope row now makes the attachment validator enforce the J012 exact-token anchors.

Design note for `S3-J014`: this job does not change attachment architecture or upload-package structure. It closes the J015 dictionary/performance-view, optimizer, execution-plan, wait, lock, session, Monitoring API, and SNMP row inside the existing dictionary/views and performance/monitoring attachments by adding compact answer bridges for exact partition/index columns, wait and lock check SQL, log-group counters, Monitoring API and SNMP mappings, optimizer predicate-detail first checks, and the `7.1.0.7.9` `OPTIMIZER_PERFORMANCE_VIEW` guardrail. The completed scope row now makes the attachment validator enforce the J015 exact-token anchors.

Design note for `S3-J015`: this job does not change attachment architecture or upload-package structure. It closes the J016 PSM, external-procedure, C/CLI/ODBC/ACI/APRE, iSQL/iLoader, utility, and LOB/API row inside the existing client-tool attachments by adding compact answer bridges for exact commands, options, methods, handles, file paths, call order, verification output, and common error-handling packets. The completed scope row now makes the attachment validator enforce the J016 exact-token anchors.

Design note for `S3-J017`: this job does not change attachment architecture or upload-package structure. It consolidates Stage 3 retrieval routing by adding targeted cross-reference anchors, generating source-pack-to-attachment, Korean-aligned-English-to-attachment, and playbook-to-attachment crosswalks from the completed scope ledger, and extending attachment validation so completed scope targets must have source, baseline, and playbook routes. `APB-000014` remains deferred; scenario files remain `Not run` scenario definitions.

## Required Attachment Edit Pattern

Each domain remediation job should keep attachment edits answer-ready and
source-backed:

- Open the exact source-pack rows, Korean-aligned baseline blocks, and playbook
  routes before adding or broadening any customer-facing product behavior.
- Add or improve compact answer blocks, not broad prose rewrites.
- Preserve exact product tokens: SQL, DDL/DCL clauses, command options, property
  names, view and column names, error codes, API names, file paths, output tokens,
  patch identifiers, `BUG-*`, and `TASK-*`.
- Include required customer inputs, version or patch assumptions, validation checks,
  expected output tokens, stop conditions, and cleanup or rollback notes where the
  source supports them.
- Use retrieval aliases, headings, and cross-links when the inventory identifies a
  retrieval gap rather than a content gap.
- For answer-synthesis gaps, strengthen answer-ready item structure so exact facts
  and tokens are hard to omit.
- Record unsupported, weakly sourced, environment-dependent, or customer-specific
  items as gaps or limitations instead of inventing a definitive answer.

## Carry-Forward Guardrails

| Guardrail | Stage 3 handling |
| --- | --- |
| `APB-000014` | Keep blocked/deferred. Do not present a completed customer-facing test-generation playbook or source-backed generated-test coverage unless a later job creates it. |
| Scenario files | Treat `test_scenarios.md` as scenario definitions only. `Not run` placeholders are not pass evidence. |
| `CONF-000001` | Preserve AID source-limitation labels for missing URLs, diagrams, non-document artifacts, source variations, and accepted auxiliary rows. |
| `CONF-000002` | Preserve English-only auxiliary labeling where source confidence matters. |
| `CONF-000003` | Do not copy untranslated Korean extraction-aid snippets into customer-facing attachments unless intentionally source-labeled and translated or normalized. |
| `CONF-000004` | Recheck exact source blocks before exhaustive admin operations, platform, backup/recovery, property, or protected-operation claims. |
| `CONF-000005` | Recheck exact source blocks before exhaustive SQL/reference grammar, property, view, data type, or error-code claims. |
| `CONF-000006` | Recheck exact source blocks, installed client/tool evidence, and third-party versions before item-level API/tool/integration artifacts. |
| `CONF-000007` | Preserve AID classification labels and patch-token/version boundaries; do not decide final AID upload-package composition in Stage 3 attachment jobs unless a later scoped job requires a recorded decision. |
| `CONF-000008` | Treat as closed for Stage 1 routing only; exact procedures, APIs, command options, tuning, source-index behavior, and Replication Manager workflows still require source-section and customer-evidence checks. |
| `CONF-000009` | Keep `SRC-000109` and `SRC-000169` excluded from authoritative customer-facing attachment and upload-package content unless a later source-authority decision permits use. |

## S3-J002 Scope And Routing Outputs

`S3-J002` creates `GPTs/reports/stage_03_attachment_followup_scope.tsv` as the
durable routing contract for domain remediation jobs. The TSV maps durable inventory
groups `J004` through `J017` to owning Stage 3 jobs `S3-J003` through `S3-J016`.
Each row records:

- source inventory job group, owning Stage 3 job, priority, benchmark question IDs,
  exact-token anchors, and critical fact notes;
- target attachment paths;
- source IDs and source-pack block pairs derived from the benchmark question
  `source_refs` and `GPTs/source_pack/source_to_shard_manifest.tsv`;
- Korean-aligned baseline block IDs derived from
  `GPTs/reports/source_pack_to_korean_aligned_english_crosswalk.tsv`;
- Stage 2 playbook routes, protected-topic flags, expected disposition, current
  status, and validation notes.

Current scope policy:

- Initial rows use `current_status=planned`.
- Initial expected disposition is `attachment_update` because every row needs a
  source-checked answer-ready block, token-preserving item block, retrieval alias, or
  downstream gap decision inside the owning domain job.
- Later jobs may update `current_status` and, if source checks prove the better final
  handling, may change `expected_disposition` or add follow-up notes using one of
  `attachment_update`, `retrieval_alias_update`, `crosslink_update`, `recorded_gap`,
  `already_covered`, or `blocked`.
- A row may not be treated as completed unless its tokens, fact notes, source route,
  target attachment, protected-topic handling, and validation notes are still
  accurate after the edit.

## Validation Plan

`S3-J002` makes the first Stage 3 validation contract executable with:

```bash
python3 GPTs/attachments/scripts/validate_attachments.py
```

The validation currently checks:

- the attachment count remains exactly `20` Markdown files excluding `README.md`;
- every customer-facing attachment has the required top-level sections:
  `Applicable Versions`, `Questions This File Can Answer`, `Retrieval Alias Index`,
  `Source Documents`, `Response Rules`, `Attachment Cross-References`, and
  `Residual Scope`;
- Stage 3 validation does not require `GPTs/upload_package/` content and fails if
  there are uncommitted upload-package paths;
- customer-facing attachments do not expose repository-local paths, local workspace
  paths, source-pack IDs, Korean-aligned block IDs, source IDs, shard IDs, or stale
  internal routing labels;
- any customer-facing attachment that mentions `8.1` preserves
  `Altibase 8.1 verified source` wording;
- `GPTs/reports/stage_03_attachment_followup_scope.tsv` has required columns, valid
  `J004` through `J017` job groups, valid owning `S3-J003` through `S3-J016` job
  IDs, valid priorities, valid question IDs, valid attachment paths, valid Stage 2
  playbook IDs, valid source IDs, valid source-pack block pairs, valid
  Korean-aligned baseline block IDs, valid protected-topic flags, valid expected
  dispositions, and valid current statuses.

`S3-J003` extends the validation scaffold for completed scope rows: when a row is
marked `current_status=done` or `current_status=already_covered`, the validator now
requires every exact token in that row to appear literally in one of the row's target
attachments. Planned, blocked, and recorded-gap rows are not forced through this exact
token check.

Later validation expansion should add checks that:

- every Stage 3 scope row has a completed final disposition such as
  `attachment_update`, `retrieval_alias_update`, `crosslink_update`,
  `recorded_gap`, `already_covered`, or `blocked`;
- every new customer-facing claim cites a valid source-pack source ID, source-pack
  block route, Korean-aligned baseline block, playbook route, or accepted limitation;
- no attachment cites `SRC-000109` or `SRC-000169` as authoritative content;
- `APB-000014` remains blocked/deferred unless a later job explicitly creates a
  source-ID-backed test-generation route;
- protected topics preserve missing-input prompts, validation checks, stop
  conditions, and rollback or cleanup notes;
- exact tokens from the benchmark inventories remain literal in attachment text or
  are recorded as source-normalization candidates;
- unsupported generic Oracle, MySQL, PostgreSQL, ANSI SQL, JDBC, ODBC, Kubernetes,
  TLS, or third-party assumptions are rejected unless selected sources support the
  exact claim;
- Stage 1 and Stage 2 validators still pass before Stage 3 readiness is claimed.

## Preflight Decision

The Stage 3 preflight gate passed. Downstream attachment follow-up work may begin
with the guarded routing, attachment boundary, and validation constraints above.
