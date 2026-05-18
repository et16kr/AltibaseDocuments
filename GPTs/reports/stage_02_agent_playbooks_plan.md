# Stage 2 Agent Playbooks Plan

- Job: `S2-J001`
- Date: 2026-05-19
- Scope: planning evidence for Stage 2 agent playbooks
- Status: Ready to start guarded Stage 2 playbook work after preflight pass

## Requirement And Boundary

Stage 2 creates task-oriented agent playbooks from the validated Stage 1 source
pack and Korean-aligned English baseline. This plan records how downstream Stage 2
jobs should proceed after the preflight gate; it does not create playbook content.

Allowed Stage 2 outputs remain limited to the paths listed in
`.codex-jobs/altibase-gpt-stage-02-agent-playbooks/prompts/common-stage-02.md`,
including `GPTs/agent_playbooks/`, Stage 2 crosswalks, the playbook gap register,
and Stage 2 readiness reports. Stage 2 must not edit original source files,
`GPTs/attachments/`, or `GPTs/upload_package/`.

## Starting Evidence

| Evidence area | Starting source |
| --- | --- |
| Product objective | `GPTs/reports/customer_agent_enablement_requirements.md` |
| Stage 1 readiness | `GPTs/reports/customer_agent_enablement_stage_01_readiness.md` |
| Source-preserving pack | `GPTs/source_pack/source_manifest.tsv`, `GPTs/source_pack/source_to_shard_manifest.tsv`, `GPTs/source_pack/source_pack_shard_*.md` |
| AID classifications | `GPTs/reports/aid_tier_manifest.tsv` |
| Korean-aligned English baseline | `GPTs/korean_aligned_english/baseline_manifest.tsv`, `GPTs/korean_aligned_english/*.md` |
| Stage 1 routing crosswalk | `GPTs/reports/source_pack_to_korean_aligned_english_crosswalk.tsv` |
| Conflict and limitation guardrails | `GPTs/reports/source_conflict_register.md` |
| Stage 2 gap seed | `GPTs/reports/agent_playbook_gap_register.md` |

## Stage 2 Work Plan

| Job | Planned outcome | Required routing discipline |
| --- | --- | --- |
| `S2-J002` | Create playbook schema, manifest schema, validation script, and source-routing plan. | Validate source IDs, source-pack block IDs, baseline block IDs, guardrail IDs, and forbidden unsupported assumptions before any domain playbook is considered ready. |
| `S2-J003` | Create service-development and SQL generation playbooks. | Use SQL/reference baselines only for guarded first drafts; exact SQL grammar, DDL/DCL/DML clauses, property values, view columns, and error handling must route to exact source blocks when item-level precision is needed. |
| `S2-J004` | Create application connectivity playbooks. | Require target Altibase version, client/tool package, OS/compiler/JDK/runtime evidence, exact API or driver source blocks, and validation commands before compile-ready or production-use artifacts. |
| `S2-J005` | Create administration and protected-operations playbooks. | Treat startup/shutdown, tablespace, backup/recovery, security, TLS, and property changes as protected operations with prerequisites, stop conditions, rollback/cleanup notes, and live-evidence prompts. |
| `S2-J006` | Create replication, CDC, HA, Log Analyzer, and Replication Manager playbooks. | Preserve topology, state, compatibility, tool-release, and runtime-output gates; route `CONF-000008` remediation rows through `KAE-BLOCK-000277` through `KAE-BLOCK-000287` only with exact source checks. |
| `S2-J007` | Create tools, utilities, migration, and integration playbooks. | Preserve installed-tool help, version, file, platform, third-party product, and live validation requirements; avoid unsupported third-party compatibility claims. |
| `S2-J008` | Create troubleshooting and performance playbooks. | Separate source-backed first checks from definitive diagnosis; require logs, object definitions, runtime state, plans, statistics, and patch evidence where needed. |
| `S2-J009` | Create AID, version, release, and patch routing playbooks. | Preserve AID source labels, English-only auxiliary labels, source limitations, 8.1-only wording, patch-token boundaries, and the global 20-file upload-package constraint for later stages. |
| `S2-J010` | Create coding-agent and GPT instruction notes. | Require generated artifacts to include missing-input prompts, assumptions, source IDs, validation checks, destructive-action warnings, and stop conditions. |
| `S2-J011` | Create scenario tests and judge rubric. | Test for required source routes, exact tokens, missing-input behavior, generated artifacts, validation checks, rollback/cleanup, and forbidden generic database assumptions. |
| `S2-J012` | Create playbook crosswalks and validation report. | Validate playbook coverage against the source-pack, Korean-aligned baseline, guardrails, and accepted exclusions; update the gap register without weakening prior limitations. |
| `S2-J013` | Write Stage 2 readiness report. | Declare ready/pass only if playbook outputs, manifests, crosswalks, scenario tests, and validation reports pass with no unresolved blocker/high/medium/low start-blocking findings. |

## S2-J002 Scaffold Update

### Design Note

`S2-J002` changes the Stage 2 documentation structure by creating the
`GPTs/agent_playbooks/` scaffold, a strict playbook manifest schema, an executable
validator, and required-domain placeholders before domain playbooks are drafted. The
placeholders are not customer-facing playbooks and do not claim source completeness.
They exist to make later Stage 2 jobs fill exact source IDs, source-pack block IDs,
Korean-aligned baseline block IDs, AID routes, generated artifact types,
missing-input prompts, validation status, and owning job metadata in a deterministic
contract.

Rows with `validation_status=planned` may carry high-level baseline and guardrail
routes, but exact `source_ids` and `source_pack_block_ids` remain blank until the
owning domain job itemizes the target source sections. Any row promoted beyond
`planned` must point to an existing Markdown playbook and carry source-backed routes.

### Manifest Contract

`GPTs/agent_playbooks/playbook_manifest.tsv` now has strict columns for:

- playbook ID, path, title, and domain;
- supported versions;
- source IDs;
- source-pack block IDs;
- Korean-aligned baseline block IDs;
- AID route or tier;
- conflict or recheck guardrail IDs;
- generated artifact types;
- protected-topic flag;
- required missing-input prompts;
- validation status;
- owning Stage 2 job;
- notes.

`GPTs/agent_playbooks/scripts/validate_playbooks.py` validates schema, file
existence for non-planned playbook rows, duplicate IDs, source-ID format, known
source-pack and baseline reference formats when populated, required domain
placeholders, and forbidden `GPTs/attachments/` or `GPTs/upload_package/` edits.

### Stage 2 Source-Routing Plan

The initial manifest covers every required domain from
`customer_agent_enablement_requirements.md`. These routes are planning routes only;
domain jobs must replace placeholders with exact source-pack block routes before
declaring playbook rows `pass`.

| Required domain | Placeholder | Owner job | Initial baseline or AID route | Source-pack itemization required before | Guardrails |
| --- | --- | --- | --- | --- | --- |
| Installation and startup | `APB-000001` | `S2-J005` | `KAE-BLOCK-000272` | exact install, environment, create-database, startup, shutdown, and first-check blocks | `CONF-000004` |
| DDL generation | `APB-000002` | `S2-J003` | `KAE-BLOCK-000272`; `KAE-BLOCK-000273` | exact DDL/DCL grammar, object, privilege, storage, replication, and validation SQL blocks | `CONF-000004`; `CONF-000005` |
| SQL and data types | `APB-000003` | `S2-J003` | `KAE-BLOCK-000273` | exact DML, function, predicate, data type, JSON, LOB, Temporary LOB, and Oracle-difference blocks | `CONF-000005` |
| Properties | `APB-000004` | `S2-J005` | `KAE-BLOCK-000272`; `KAE-BLOCK-000273` | exact property default, range, unit, dynamic/static, restart, dependency, and check-SQL blocks | `CONF-000004`; `CONF-000005` |
| Dictionary and views | `APB-000005` | `S2-J008` | `KAE-BLOCK-000273` | exact dictionary and performance-view rows, columns, object lookup, and metadata check blocks | `CONF-000005` |
| Backup and recovery | `APB-000006` | `S2-J005` | `KAE-BLOCK-000272` | exact backup, archive-log, recovery, media-failure, incremental backup, validation, and rollback blocks | `CONF-000004` |
| Replication and CDC | `APB-000007` | `S2-J006` | `KAE-BLOCK-000272`; `KAE-BLOCK-000273`; `KAE-BLOCK-000280`; `KAE-BLOCK-000286`; `KAE-BLOCK-000287` | exact topology, DDL, state, sync, conflict, CDC, Log Analyzer, RepMgr, and runtime-output blocks | `CONF-000004`; `CONF-000005`; `CONF-000008` |
| Security and TLS | `APB-000008` | `S2-J005` | `KAE-BLOCK-000272`; `KAE-BLOCK-000274` | exact certificate, TLS, access-control, client, replication SSL, and validation blocks | `CONF-000004`; `CONF-000006` |
| ODBC and C clients | `APB-000009` | `S2-J004` | `KAE-BLOCK-000274` | exact ODBC, CLI, ACI, Precompiler, diagnostic, compile, link, and runtime blocks | `CONF-000006` |
| Java and JDBC | `APB-000010` | `S2-J004` | `KAE-BLOCK-000274` | exact JDBC URL, driver, property, LOB, Java compatibility, Spring, Hibernate, and Adapter blocks | `CONF-000006` |
| Tools | `APB-000011` | `S2-J007` | `KAE-BLOCK-000274`; `KAE-BLOCK-000275` | exact iSQL, iLoader, utilities, dataCompJ, dump, altiComp, aexport, option, file, and output blocks | `CONF-000006`; `CONF-000007` |
| Migration and integrations | `APB-000012` | `S2-J007` | `KAE-BLOCK-000274`; `KAE-BLOCK-000275`; `KAE-BLOCK-000276` | exact Migration Center, Adapter for Oracle, DB Link, Hadoop, Kubernetes/AKU, Spatial, NiFi, Tableau, AID-label, and third-party validation blocks | `CONF-000006`; `CONF-000007`; `CONF-000009` |
| Errors and troubleshooting | `APB-000013` | `S2-J008` | `KAE-BLOCK-000273`; `KAE-BLOCK-000280`; `KAE-BLOCK-000281`; `KAE-BLOCK-000282`; `KAE-BLOCK-000283` | exact error, symptom, log, command, view, runtime-state, and escalation blocks | `CONF-000005`; `CONF-000008` |
| Test generation | `APB-000014` | `S2-J011` | `KAE-BLOCK-000272`; `KAE-BLOCK-000273`; `KAE-BLOCK-000274`; `KAE-BLOCK-000275`; `KAE-BLOCK-000276` | exact positive, negative, boundary, setup, teardown, expected-output, and cleanup blocks | `CONF-000004`; `CONF-000005`; `CONF-000006`; `CONF-000007`; `CONF-000008` |

## Mandatory Playbook Content Rules

Every downstream playbook should include the following where the source evidence
supports it:

- task purpose and supported versions;
- required customer inputs and source-backed assumptions;
- prerequisites and environment or patch-level requirements;
- generated artifacts such as SQL, commands, configuration, code, scripts, or tests;
- step-by-step procedure with validation checks;
- expected result tokens or observable checks where source-backed;
- common errors and first checks;
- stop conditions and escalation prompts;
- cleanup, rollback, or non-production test guidance;
- source IDs, source-pack block IDs, Korean-aligned baseline block IDs, and guardrail
  IDs.

Generated artifacts must distinguish guarded draft generation from production
execution. For destructive, privilege-changing, storage-changing,
replication-changing, security-sensitive, or environment-dependent work, the
playbook must ask for missing customer evidence and provide the safest source-backed
next check instead of inventing a definitive answer.

## Carry-Forward Guardrails

| Guardrail | Stage 2 handling |
| --- | --- |
| `CONF-000001` | Preserve source-limitation labels for missing AID URLs, diagrams, non-document artifacts, source variations, and accepted auxiliary rows. |
| `CONF-000002` | Preserve English-only auxiliary labeling when source confidence matters. |
| `CONF-000003` | Do not copy untranslated Korean extraction-aid snippets into customer-facing playbooks unless intentionally source-labeled. |
| `CONF-000004` | Recheck exact source blocks before exhaustive admin operations, platform, backup/recovery, property, or protected-operation claims. |
| `CONF-000005` | Recheck exact source blocks before exhaustive SQL/reference grammar, property, view, data type, or error-code claims. |
| `CONF-000006` | Recheck exact source blocks, installed client/tool evidence, and third-party versions before item-level API/tool/integration artifacts. |
| `CONF-000007` | Preserve AID classification labels and patch-token/version boundaries; do not decide final AID upload-package composition in Stage 2 unless a later scoped job requires it. |
| `CONF-000008` | Treat as closed for Stage 1 routing only; exact procedures, APIs, command options, tuning, source-index behavior, and Replication Manager workflows still require source-section and customer-evidence checks. |
| `CONF-000009` | Keep `SRC-000109` and `SRC-000169` excluded from authoritative customer-facing playbook, attachment, and upload-package content unless a later source-authority decision permits use. |

## Validation Plan

`S2-J002` should make the validation contract executable. The validation should
check at least:

- every playbook appears in `GPTs/agent_playbooks/playbook_manifest.tsv`;
- every cited `SRC-*`, `BLOCK-*`, and `KAE-BLOCK-*` resolves to Stage 1 artifacts;
- guarded rows with `CONF-*` IDs preserve the required warning or missing-input
  behavior;
- no playbook cites `SRC-000109` or `SRC-000169` as authoritative content;
- no customer-facing playbook contains Korean prose leakage except intentional
  source labels or source-labeled examples;
- generated artifact sections include validation checks and stop conditions;
- protected operations include prerequisites, risk notes, rollback or cleanup, and
  live-evidence prompts;
- unsupported generic Oracle, MySQL, PostgreSQL, ANSI SQL, JDBC, ODBC, Kubernetes, or
  third-party assumptions are rejected unless the selected source corpus supports
  the exact claim.

## Preflight Decision

The Stage 2 preflight gate passed. Downstream playbook work may begin with the
guarded routing and validation constraints above.
