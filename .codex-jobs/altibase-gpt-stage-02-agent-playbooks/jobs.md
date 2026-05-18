# Altibase GPT Stage 2: Agent Playbooks

- Kind: `mixed`
- Status values: `ToDo`, `Progress`, `Done`, `Fail`
- User-run command: `./run-all.sh` from this directory
- Codex workdir: repository root by default, override with `CODEX_WORKDIR=/path`
- Default behavior: continue through all jobs until completion or failure
- Optional single-job mode: `RUN_ONE=1 ./run-all.sh`
- Handoff gate: uncommitted project files stop the workflow before the next job starts
- Commit gate: each successful job must pass review and create a focused commit
- Purpose: create the Stage 2 agent playbook layer from the validated Stage 1 source
  pack and Korean-aligned English baseline.
- Scope boundary: this workflow may create or update `GPTs/agent_playbooks/` and
  Stage 2 integration reports under `GPTs/reports/`; it must not edit
  `GPTs/attachments/` or assemble `GPTs/upload_package/`.
- Mandatory first gate: `S2-J001` must refuse downstream work if Stage 1 is not
  explicitly ready/pass, if required Stage 1 validation artifacts are missing, if
  blocked routing rows remain, or if a prior-stage operator-only decision is
  unresolved. It must also inspect prior not-ready, conflict, recheck, and
  accepted-limitation records before treating Stage 2 as started.
- Completion target: `customer_agent_enablement_stage_02_readiness.md` must be
  updated by `S2-J013` with an explicit `ready/pass` or not-ready/blocker verdict.
- Source guardrails: preserve Korean-authoritative source routing, AID tier labels,
  `CONF-000004` through `CONF-000007` recheck guardrails, and the `CONF-000009`
  nonblocking exclusion.

## Jobs

| ID | Status | Title | Goal |
| --- | --- | --- | --- |
| `S2-J001` | `ToDo` | Stage 2 preflight readiness gate | Verify Stage 1 ready/pass status, prior workflow completion, validation artifacts, blocked routing scans, and operator-only decisions before any playbook work starts. |
| `S2-J002` | `ToDo` | Playbook schema and validation scaffolding | Create the agent playbook directory, manifest schema, validation script, and Stage 2 source-routing plan. |
| `S2-J003` | `ToDo` | Service development and SQL generation playbooks | Create playbooks for Altibase-backed service planning plus SQL, DDL, DCL, DML, schema, privilege, object, data type, property, view, and validation artifact generation. |
| `S2-J004` | `ToDo` | Application connectivity playbooks | Create source-backed playbooks for JDBC, ODBC, CLI, ACI, Precompiler, Java/Spring/Hibernate, connection configuration, compile/link/runtime checks, and diagnostics. |
| `S2-J005` | `ToDo` | Administration and protected operations playbooks | Create guarded playbooks for installation, startup/shutdown, properties, tablespaces, backup/recovery, archive logs, security-sensitive administration, and protected operations. |
| `S2-J006` | `ToDo` | Replication, CDC, and HA playbooks | Create guarded playbooks for replication topology, DDL, state checks, sync/conflict handling, CDC, Log Analyzer, and Replication Manager. |
| `S2-J007` | `ToDo` | Tools, utilities, migration, and integration playbooks | Create playbooks for iSQL, iLoader, utilities, dataCompJ, dump tools, altiComp, aexport, Migration Center, Adapter for Oracle, DB Link, Hadoop, Kubernetes/AKU, Spatial, NiFi, and Tableau. |
| `S2-J008` | `ToDo` | Troubleshooting and performance playbooks | Create playbooks for exact error handling, log/symptom triage, monitoring, dictionary/performance views, tuning checks, escalation points, and safe next checks. |
| `S2-J009` | `ToDo` | AID, version, release, and patch routing playbooks | Create playbook routing guidance for AID-derived content, 7.1/7.3/8.1 boundaries, release-note tokens, patch-specific claims, accepted limitations, and source recheck guardrails. |
| `S2-J010` | `ToDo` | Coding-agent and GPT instruction notes | Create coding-agent and GPT service-development instruction notes that define source routing, missing-input prompts, generated-artifact structure, and forbidden generic assumptions. |
| `S2-J011` | `ToDo` | Scenario tests and judge rubric | Create representative GPT and coding-agent scenario tests plus the judge rubric for required source IDs, exact tokens, forbidden assumptions, missing inputs, artifacts, validations, stop conditions, and pass thresholds. |
| `S2-J012` | `ToDo` | Playbook crosswalks and validation report | Validate playbook source-ID and baseline coverage, generate source-to-playbook crosswalks, update the playbook gap register, and write the playbook validation report. |
| `S2-J013` | `ToDo` | Stage 2 readiness review | Review all Stage 2 outputs, rerun validation, preserve guardrails, and write a ready/pass or not-ready Stage 2 readiness report. |

## Resume Rules

- `Fail`: stop before starting later jobs.
- Dirty project files: stop before starting or advancing to another job.
- `Progress`: preserve interruption evidence, set the job back to `ToDo`, then rerun only when project files are clean.
- `Done`: skip.
- Nonzero `codex exec` exits leave the job as `Progress` by default; the next manual run stops if project files are dirty, or resets runtime state and retries when clean.

## Acceptance Checklist

- Each job has a matching prompt in `prompts/`.
- Each job has concrete acceptance criteria.
- Each successful job leaves project files clean and advances HEAD with a commit.
- `bash -n run-all.sh` passes.
- `S2-J001` is the first job and performs the prior-stage readiness gate.
- Required playbook domains from the requirements document are represented or listed
  as explicit gaps/blockers.
- Every playbook route includes source IDs and, where applicable, source-pack and
  Korean-aligned baseline block IDs.
- `playbook_manifest.tsv`, source-to-playbook crosswalks, `playbook_validation.md`,
  `test_scenarios.md`, and `scenario_judge_rubric.md` are complete or the readiness
  report is not-ready.
- Stage 2 does not modify original source files, `GPTs/attachments/`, or
  `GPTs/upload_package/`.
