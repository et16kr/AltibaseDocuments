# Altibase GPT Answerability Benchmark

- Kind: `mixed`
- Status values: `ToDo`, `Progress`, `Done`, `Fail`
- User-run command: `./run-all.sh` from this directory
- Default behavior: continue through all jobs until completion or failure
- Optional single-job mode: `RUN_ONE=1 ./run-all.sh`
- Handoff gate: uncommitted project files stop the workflow before the next job starts
- Commit gate: each successful job must pass review and create a focused commit

## Workflow Requirements

`run-all.sh` prepends `requirements.md` to every job prompt at runtime. Treat that file
as the shared contract for the benchmark purpose, durable artifact layout, source-backed
question policy, attachments-only answer runner, judge/report behavior, and readiness
thresholds.

## Persistent Output

This workflow must create and maintain the long-term benchmark under:

```text
evals/altibase_answerability/
```

The `.codex-jobs/altibase-gpt-answerability-benchmark/` directory is only the
orchestration layer. The actual benchmark questions, schemas, scripts, fixtures, and
reports must be durable repository artifacts outside the workflow directory.

## Partitioning Model

The workflow is split into 12 jobs:

- J001-J003: benchmark requirements, durable layout, schemas, manifests, and validation
  rules.
- J004-J010: at least 200 total source-backed benchmark questions across required
  domain minimums, with a target of about 270 questions.
- J011: attachments-only answer generation runner with strict question-field projection
  and leakage checks.
- J012: source-backed judge comparison, reports, calibration, and readiness thresholds.

## Jobs

| ID | Status | Title | Goal |
| --- | --- | --- | --- |
| `J001` | `ToDo` | Benchmark requirements and durable layout | Define benchmark purpose, persistent eval directory layout, schemas, scoring policy, and success thresholds. |
| `J002` | `ToDo` | Source taxonomy and coverage map | Map selected manual/source families to benchmark domains, user levels, and target question counts. |
| `J003` | `ToDo` | Question schema and manifest tooling | Create the machine-readable question schema, manifest format, validation rules, and seed examples. |
| `J004` | `ToDo` | Property benchmark questions | Generate hard source-backed property questions covering defaults, ranges, dynamic changes, check SQL, and cautions. |
| `J005` | `ToDo` | SQL DDL DML and compatibility questions | Generate hard source-backed SQL, DDL, DML, data type, JSON, LOB, function, and Oracle-difference questions. |
| `J006` | `ToDo` | Operations backup recovery questions | Generate hard source-backed installation, startup, shutdown, backup, restore, recovery, tablespace, and admin runbook questions. |
| `J007` | `ToDo` | Views performance and monitoring questions | Generate hard source-backed dictionary, performance view, optimizer, plan, monitoring, SNMP, and tuning questions. |
| `J008` | `ToDo` | Replication CDC security network questions | Generate hard source-backed replication, CDC, Log Analyzer, RepMgr, security, TLS, and network diagnostic questions. |
| `J009` | `ToDo` | Error and troubleshooting questions | Generate hard source-backed error-code, symptom, cause/action, log collection, and troubleshooting questions. |
| `J010` | `ToDo` | Tools APIs connectors migration questions | Generate hard source-backed PSM, external procedure, JDBC, CLI, ODBC, Precompiler, iSQL, iLoader, utilities, connectors, Kubernetes, migration, Spatial, NiFi, and Tableau questions. |
| `J011` | `ToDo` | Attachments-only answer generation runner | Implement the durable script that projects question records to the allowed answering input, runs answer generation using only GPTs/attachments as retrieval context, checks for judge-only metadata leakage, and records model responses. |
| `J012` | `ToDo` | Source-backed judge and readiness reports | Implement source-backed judge/report tooling that compares attachments-only answers against expected facts, required tokens, prohibited claims, and readiness thresholds, with calibration samples and validation commands. |

## Resume Rules

- `Fail`: stop before starting later jobs.
- Dirty project files: stop before starting or advancing to another job.
- `Progress`: preserve interruption evidence first, stop if project files are dirty, or set the job back to `ToDo` and rerun only when project files are clean.
- `Done`: skip.
- Nonzero `codex exec` exits leave the job as `Progress` by default; the next manual run preserves status/diff evidence, then stops if project files are dirty or resets runtime state and retries when clean.

## Acceptance Checklist

- Each job has a matching prompt in `prompts/`.
- Each job has concrete acceptance criteria.
- Each successful job leaves project files clean and advances HEAD with a commit.
- `bash -n run-all.sh` passes.
