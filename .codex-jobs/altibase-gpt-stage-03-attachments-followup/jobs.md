# Altibase GPT Stage 3: Attachments Follow-up

- Kind: `mixed`
- Status values: `ToDo`, `Progress`, `Done`, `Fail`
- User-run command: `./run-all.sh` from this directory
- Codex workdir: repository root by default, override with `CODEX_WORKDIR=/path`
- Default behavior: continue through all jobs until completion or failure
- Optional single-job mode: `RUN_ONE=1 ./run-all.sh`
- Handoff gate: uncommitted project files stop the workflow before the next job starts
- Commit gate: each successful job must pass review and create a focused commit
- Purpose: re-plan and perform only the still-needed answer-ready attachment
  follow-up work using Stage 1 source evidence, Korean-aligned English baseline,
  durable benchmark evidence, and Stage 2 playbooks as guarded routing evidence.
- Scope boundary: this workflow may edit existing `GPTs/attachments/*.md`,
  attachment validation helpers, and Stage 3 reports/crosswalks under `GPTs/reports/`;
  it must not edit original source files or assemble `GPTs/upload_package/`.
- Mandatory first gate: `S3-J001` must refuse downstream work if Stage 2 is not
  explicitly ready/pass for guarded Stage 3 routing, if Stage 2 validation artifacts
  are missing, if the Stage 2 workflow is incomplete, or if a prior-stage
  operator-only decision is unresolved.
- Attachment boundary: keep exactly 20 customer-facing attachment Markdown files under
  `GPTs/attachments/`, excluding `README.md`; do not add new final upload files in
  Stage 3.
- Guardrails: preserve `APB-000014` as blocked/deferred test-generation coverage,
  scenario tests as not-run validation scenarios, `CONF-000004` through `CONF-000007`
  open recheck gates, and `CONF-000009` English-only exclusions.
- Completion target: `customer_agent_enablement_stage_03_readiness.md` must be
  updated by `S3-J018` with an explicit `ready/pass` or not-ready/blocker verdict.

## Jobs

| ID | Status | Title | Goal |
| --- | --- | --- | --- |
| `S3-J001` | `ToDo` | Stage 3 preflight readiness gate | Verify Stage 2 ready/pass status, Stage 2 workflow completion, playbook validation, APB-000014 guardrail handling, and unresolved operator-only decisions before any attachment work starts. |
| `S3-J002` | `ToDo` | Attachment follow-up scope and validation scaffolding | Create the Stage 3 attachment follow-up scope, validation scaffolding, and source/playbook routing plan from durable benchmark evidence and Stage 2 playbooks. |
| `S3-J003` | `ToDo` | Core identity path storage property follow-up | Remediate core identity, path, database-file, log-anchor, storage, and foundational property attachment gaps using source-backed item blocks. |
| `S3-J004` | `ToDo` | Capacity and memory property follow-up | Remediate memory, disk, volatile, log-size, cache, result-cache, and capacity-limit property attachment gaps. |
| `S3-J005` | `ToDo` | Session optimizer locale lock property follow-up | Remediate optimizer, session, locale, lock, timeout, autocommit, transaction, and performance property attachment gaps. |
| `S3-J006` | `ToDo` | Security replication network property follow-up | Remediate account, access-list, SSL/TLS, replication, network, port, and SQL-apply property attachment gaps. |
| `S3-J007` | `ToDo` | DDL and destructive SQL generation follow-up | Remediate tablespace, datafile, table, partition, index, constraint, LOB storage, queue, and destructive DDL generation attachment gaps. |
| `S3-J008` | `ToDo` | DML functions datatypes Oracle-difference follow-up | Remediate DML, functions, data type, JSON, LOB, object-name, regular-expression, and Oracle-difference attachment gaps. |
| `S3-J009` | `ToDo` | Error and troubleshooting follow-up | Remediate exact error-code, SQL/property error, tool/driver error, symptom, log, and troubleshooting attachment gaps. |
| `S3-J010` | `ToDo` | Install startup privilege runbook follow-up | Remediate installation, startup, account, privilege, tablespace, datafile, loganchor, and beginner-to-veteran runbook attachment gaps. |
| `S3-J011` | `ToDo` | Backup recovery protected operations follow-up | Remediate backup, recovery, archive log, RESETLOGS, DROP/DISCARD/REUSE, and destructive protected-operation attachment gaps. |
| `S3-J012` | `ToDo` | Replication topology state SQL follow-up | Remediate replication topology, state, DDL, control SQL, gap, compatibility, and replication guardrail attachment gaps. |
| `S3-J013` | `ToDo` | CDC Log Analyzer RepMgr TLS network follow-up | Remediate CDC, Log Analyzer, Replication Manager, replication SSL, ordinary TLS, certificate, port, and network diagnostic attachment gaps. |
| `S3-J014` | `ToDo` | Dictionary performance monitoring follow-up | Remediate dictionary and performance view, optimizer, execution plan, wait, lock, session, Monitoring API, and SNMP attachment gaps. |
| `S3-J015` | `ToDo` | PSM client tools utilities follow-up | Remediate PSM, external procedure, CLI, ODBC, ACI, Precompiler, iSQL, iLoader, utility, and LOB/API attachment gaps. |
| `S3-J016` | `ToDo` | Java connectors migration integration follow-up | Remediate Java, JDBC, connector, migration, Kubernetes, Spatial, NiFi, Tableau, and miscellaneous integration attachment gaps. |
| `S3-J017` | `ToDo` | Retrieval aliases crosswalks and attachment validation | Update retrieval aliases, cross-links, source/playbook-to-attachment crosswalks, gap registers, and attachment validation reports after domain remediation. |
| `S3-J018` | `ToDo` | Stage 3 readiness review | Review all Stage 3 attachment outputs, rerun validation, preserve guardrails, and write a ready/pass or not-ready Stage 3 readiness report. |

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
- `S3-J001` is the first job and performs the prior-stage readiness gate.
- Stage 3 jobs use source IDs, source-pack block IDs, Korean-aligned baseline routes,
  and Stage 2 playbook routes before broadening attachment content.
- Preflight validates Stage 1 source-pack/alignment health and Stage 2 playbook health
  before starting attachment edits.
- Required exact-token, protected-topic, retrieval-alias, source-route, and
  cross-reference checks pass or are recorded as explicit gaps.
- `source_pack_to_attachment_crosswalk.tsv` and
  `korean_aligned_english_to_attachment_crosswalk.tsv` are current before readiness is
  claimed.
- `GPTs/upload_package/` is untouched by Stage 3.
