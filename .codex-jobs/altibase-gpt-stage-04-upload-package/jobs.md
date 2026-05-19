# Altibase GPT Stage 4: Upload Package Assembly

- Kind: `mixed`
- Status values: `ToDo`, `Progress`, `Done`, `Fail`
- User-run command: `./run-all.sh` from this directory
- Codex workdir: repository root by default, override with `CODEX_WORKDIR=/path`
- Default behavior: continue through all jobs until completion or failure
- Optional single-job mode: `RUN_ONE=1 ./run-all.sh`
- Handoff gate: uncommitted project files stop the workflow before the next job starts
- Commit gate: each successful job must pass review and create a focused commit
- Purpose: assemble the final GPT Knowledge upload package from the validated
  source-preserving, playbook, and answer-ready layers without exceeding the global
  20 Markdown file limit.
- Scope boundary: this workflow may create `GPTs/upload_package/*.md`, Stage 4
  manifests/crosswalks/reports under `GPTs/reports/`, and a validation helper under
  `GPTs/reports/scripts/` if needed. It must not edit original source documents or
  benchmark expected-answer files.
- Mandatory first gate: `S4-J001` must refuse downstream work if Stage 3 is not
  explicitly ready/pass for guarded Stage 4 routing, if required validations fail, if
  project files outside `.codex-jobs/` are dirty, or if an unresolved operator-only
  decision blocks final package composition.
- Upload boundary: final upload Markdown files live only under `GPTs/upload_package/`
  and must total 20 or fewer including any AID-derived content. Auxiliary reports,
  manifests, scripts, and validation artifacts should stay outside that directory.
- Guardrails: preserve `APB-000014` as deferred or explicitly excluded unless a later
  source-backed playbook closes it; carry forward `CONF-000004` through `CONF-000007`,
  the item-level `CONF-000008` recheck rule, and the `CONF-000009` exclusions.
- Completion target: `customer_agent_enablement_stage_04_readiness.md` must be
  written by `S4-J011` with an explicit ready/pass or not-ready/blocker verdict.

## Jobs

| ID | Status | Title | Goal |
| --- | --- | --- | --- |
| `S4-J001` | `ToDo` | Stage 4 preflight readiness gate | Verify Stage 3 ready/pass status, Stage 3 workflow completion, validation health, APB-000014 deferral, guardrails, AID candidate status, upload-package absence or cleanliness, and unresolved operator-only decisions before package assembly starts. |
| `S4-J002` | `ToDo` | Upload package composition and validation scaffold | Define the Stage 4 upload composition plan, manifest schema, package validation checks, file-count policy, AID selection decision path, and source/playbook/attachment routing requirements. |
| `S4-J003` | `ToDo` | Version installation administration package assembly | Assemble the version, release, platform, installation, startup, administration, tablespace, backup/recovery, and protected-operation upload-package files. |
| `S4-J004` | `ToDo` | SQL reference upload package assembly | Assemble SQL DDL/DCL/DML, Oracle compatibility, data type, property, dictionary, and performance-view upload-package files. |
| `S4-J005` | `ToDo` | Troubleshooting performance replication security package assembly | Assemble troubleshooting, error-response, performance tuning, monitoring, replication, CDC, HA, security, SSL, and TLS upload-package files. |
| `S4-J006` | `ToDo` | Developer client tools package assembly | Assemble PSM, stored/external procedure, Java/JDBC/Spring/Hibernate, C/CLI/ODBC/ACI/Precompiler, iSQL, iLoader, utility, and operation-tool upload-package files. |
| `S4-J007` | `ToDo` | Migration connectors cloud spatial package assembly | Assemble migration, Oracle compatibility, DB Link, external connector, Kubernetes, AKU, Spatial, NiFi, Tableau, and miscellaneous integration upload-package files. |
| `S4-J008` | `ToDo` | AID source-limitation and guardrail integration | Apply the final AID upload-content decision, preserve AID classifications and accepted limitations, carry forward CONF guardrails, and record APB-000014 as deferred or explicitly excluded without inflating the upload file count. |
| `S4-J009` | `ToDo` | Upload package crosswalks and deterministic validation | Generate upload-package manifests and crosswalks, validate file count, required sections, leakage scans, source/playbook/attachment routes, excluded-source handling, and upload boundary hygiene. |
| `S4-J010` | `ToDo` | Retrieval and answerability dry-run gate | Run deterministic retrieval/package checks and benchmark dry-run validation against the assembled package, record any residual gaps, and avoid live-benchmark claims unless a live run is explicitly performed. |
| `S4-J011` | `ToDo` | Stage 4 readiness review | Review all Stage 4 outputs, rerun validation, preserve guardrails, and write a ready/pass or not-ready Stage 4 readiness report for final upload or live benchmark rerun routing. |

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
- `S4-J001` is the first job and performs the Stage 3 readiness gate.
- `GPTs/upload_package/` contains 20 Markdown files or fewer when readiness is
  claimed, and every Markdown file is listed in
  `GPTs/reports/stage_04_upload_package_manifest.tsv`.
- Final upload files have attachment, source-pack, Korean-aligned English, and
  playbook routes or explicit recorded limitations.
- AID upload-content candidates are either integrated within the same global file
  limit or recorded as not selected/deferred with source-limitation labels preserved.
- `APB-000014`, `CONF-000004` through `CONF-000009`, scenario-test status, and live
  benchmark status are not silently closed.
- Deterministic package validation passes before Stage 4 readiness is claimed.
