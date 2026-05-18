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
