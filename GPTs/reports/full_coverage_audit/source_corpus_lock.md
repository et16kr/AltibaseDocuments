# Full Coverage Audit Source Corpus Lock

- Workflow: `altibase-gpt-full-coverage-audit`
- Audit job: `FCA-J001`
- Job title: Preflight and benchmark evidence lock
- Status: Preflight locked; item-level source corpus lock remains assigned to `FCA-J002`
- Date: 2026-05-18

## FCA-J001 Scope

`FCA-J001` confirms that the staged review/remediation cycle is complete, that no
project files outside workflow runtime/status files were dirty before this job edited
the repository, and that the latest full benchmark run is locked as failure evidence
for the stricter full coverage audit.

This job does not catalog source items, remediate attachment content, broaden source
scope, edit original manuals, or change customer-facing GPT instructions. Later jobs
must still prove item-level source-to-attachment coverage from repository-local
selected sources.

## Job Boundary Evidence

The job boundary was reconfirmed from:

- `.codex-jobs/altibase-gpt-full-coverage-audit/jobs.tsv`: `FCA-J001` was the only
  `Progress` job, with goal "Confirm the current review/remediation cycle is complete,
  the worktree is clean, previous jobs are committed, and the latest full benchmark run
  is locked as audit evidence."
- `.codex-jobs/altibase-gpt-full-coverage-audit/jobs.md`: `FCA-J001` targets current
  workflow status, latest benchmark, and existing reports, with expected durable output
  "Preflight evidence section and locked latest-run baseline."
- `.codex-jobs/altibase-gpt-full-coverage-audit/requirements.md`: the latest run below
  is failure evidence only, not the full audit scope.

## Repository Preflight Evidence

Required first checks from `AGENTS.md` were run before project edits:

| Check | Evidence | Result |
| --- | --- | --- |
| Review/remediation cycle status | `bash review/scripts/run_review_remediation_cycle.sh status` | `R00` through `R27` were all `Done` for both cycle and review status. |
| Active or failed stages | `rg -n $'\t(Reviewing\|Remediating\|ReReviewing\|Fail)$' review/review_remediation_cycle_status.tsv` | No matches; command exited `1`, which means no active or failed cycle rows were present. |
| Worktree status before project edits | `git status --short` | Only `.codex-jobs/altibase-gpt-full-coverage-audit/jobs.tsv` was modified. No project files outside workflow status/runtime files were dirty. |
| Recent committed workflow base | `git log --oneline -5` | `8808d1e2 Harden full coverage audit runner cwd handling` was HEAD before this project edit; prior workflow setup commits were already present. |

Because the only pre-existing dirty path was workflow status under `.codex-jobs/`, this
job was safe to proceed under the orchestrator contract.

## Source And Support Reports Inspected

The job-relevant portions of these repository-local artifacts were inspected:

- `AGENTS.md`
- `GPTs/attachments/README.md`
- `GPTs/GPT_Instructions_Draft.md`
- `GPTs/reports/source_inventory.md`
- `GPTs/reports/coverage_matrix.md`
- `GPTs/reports/gap_register.md`
- `GPTs/reports/final_upload_readiness.md`
- `GPTs/reports/answerability_failure_remediation_inventory_20260517.md`
- `evals/altibase_answerability/reports/full_benchmark/failure_root_cause_analysis_20260517.md`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_205641/summary.txt`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_205641/judge/report.md`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_205641/judge/aggregate_report.json`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_205641/judge/judgments.jsonl`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_205641/answers/answers.jsonl`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_205641/answers/run.json`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_205641/run-test.log`

Confirmed boundary facts:

- The upload package remains exactly the 20 Markdown files listed in
  `GPTs/attachments/README.md`, excluding that README.
- `GPTs/GPT_Instructions_Draft.md` is the customer answer contract and instruction
  basis, but the locked benchmark run below used attachment lexical context and did
  not include the instruction draft in the answer prompt.
- `GPTs/reports/source_inventory.md` remains the source-root and attachment-to-source
  path inventory.
- `GPTs/reports/coverage_matrix.md` remains the source family ownership and attachment
  routing map.
- `GPTs/reports/gap_register.md` remains the active guardrail, verification-limited,
  and closed-trace register until the new full coverage audit matrix/registers replace
  or refine those rows.
- Korean source precedence, selected repository-local sources only, and the customer
  label `Altibase 8.1 verified source` remain active policy.

## Locked Latest Benchmark Baseline

The latest full benchmark run locked for this audit is:

`evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_205641/`

Run metadata:

| Field | Value |
| --- | --- |
| Run ID | `altibase_answerability_20260517_205641` |
| Generated at | `2026-05-17T13:42:05Z` |
| Manifest | `full_benchmark` |
| Mode | `live` |
| Provider | `command` |
| Model | `codex-exec` |
| Context mode | `lexical` |
| Answer runner status | `ok` |
| Answer runner exit code | `0` |
| Answer records | `270` |
| Judgment records | `270` |
| Readiness decision | `blocking_gaps` |

Overall metrics:

| Metric | Locked value | Readiness threshold |
| --- | ---: | ---: |
| Passed / total | 101 / 270 | Overall pass rate >= 85.0% |
| Failed | 169 | 0 blocking failures expected before upload readiness |
| Pass rate | 37.4% | 85.0% |
| Critical fact coverage | 85.1% | 90.0% |
| Required token preservation | 90.1% | 95.0% |
| Unsupported-claim rate | 1.1% | <= 2.0% |
| Protected-topic blockers | 32 | 0 |

Domain results from `judge/report.md`:

| Domain | Questions | Passed | Failed | Pass rate | Max severity |
| --- | ---: | ---: | ---: | ---: | --- |
| `errors_troubleshooting` | 30 | 10 | 20 | 33.3% | blocker |
| `operations_admin` | 35 | 17 | 18 | 48.6% | blocker |
| `properties` | 50 | 18 | 32 | 36.0% | blocker |
| `replication_cdc_security_network` | 30 | 9 | 21 | 30.0% | blocker |
| `sql_ddl_dml_datatypes` | 45 | 15 | 30 | 33.3% | blocker |
| `tools_apis_connectors_migration` | 50 | 26 | 24 | 52.0% | high |
| `views_performance_monitoring` | 30 | 6 | 24 | 20.0% | blocker |

Protected-topic blockers:

| Topic | Count | Question IDs |
| --- | ---: | --- |
| `backup_recovery` | 6 | `ERR-110`, `ERR-113`, `OPS-114`, `OPS-116`, `PROP-130`, `VPM-114` |
| `destructive_sql` | 3 | `ERR-120`, `ERR-122`, `SQL-129` |
| `replication_state_changes` | 8 | `ERR-127`, `PROP-136`, `PROP-137`, `REPL-113`, `REPL-116`, `SQL-114`, `SQL-141`, `VPM-125` |
| `security_tls` | 3 | `PROP-140`, `REPL-103`, `REPL-121` |
| `version_sensitive_property_changes` | 12 | `PROP-112`, `PROP-115`, `PROP-117`, `PROP-122`, `PROP-123`, `PROP-127`, `PROP-128`, `PROP-129`, `PROP-131`, `PROP-132`, `PROP-144`, `PROP-148` |

Priority signals:

- The readiness decision is `blocking_gaps`.
- `views_performance_monitoring` is the worst domain by pass rate at `20.0%`.
- `113` of the `169` failed questions are in the high retrieval-risk bucket according
  to `judge/aggregate_report.json`.
- The top remediation target categories in `judge/report.md` are missing critical
  facts and missing required tokens, led by `properties`,
  `sql_ddl_dml_datatypes`, `views_performance_monitoring`,
  `errors_troubleshooting`, `replication_cdc_security_network`, and
  `operations_admin`.

Trend context from earlier full runs:

| Run | Passed / total | Failed | Pass rate | Critical fact coverage | Required token preservation | Protected-topic blockers | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `altibase_answerability_20260516_145452` | 24 / 270 | 246 | 8.9% | 68.3% | 73.4% | 81 | `blocking_gaps` |
| `altibase_answerability_20260517_095919` | 27 / 270 | 243 | 10.0% | 68.7% | 74.6% | 77 | `blocking_gaps` |
| `altibase_answerability_20260517_205641` | 101 / 270 | 169 | 37.4% | 85.1% | 90.1% | 32 | `blocking_gaps` |

## Locked Artifact Checksums

The following SHA-256 checksums lock the latest benchmark evidence files reviewed by
`FCA-J001`:

| Artifact | SHA-256 |
| --- | --- |
| `summary.txt` | `b4d16997f67c7bd31a618fa62cf25dcd20ea6616df3eb4dbf121944af5c9ea78` |
| `judge/report.md` | `a21110b13d67508966dc9305ec724b21a03fe8596cd3a2756537d6f592bddf7d` |
| `judge/aggregate_report.json` | `79cebf2a72b0961a9661e760b329ae25553e6359dcf7a7be0f35bd3367948d7a` |
| `judge/judgments.jsonl` | `be7c5e187d4e63c1a9766705a4cb8e8093278ec77c42332eabaf73abd3a6c3d3` |
| `answers/answers.jsonl` | `2899a671158d4b9f05c17f8de273984282de22ebb16261d781b2611c0ae7cca1` |
| `answers/run.json` | `970a94ff9eb3bd8225653fad45d76587d32a69911b7ff40168eaee21dac2dff7` |
| `run-test.log` | `184a11f0e17a41d2056d47c63729708184d2a6fe8d016e9406156e768cd14630` |

## Audit Use Rules

- Treat this locked benchmark as failure evidence for priority, targeted answerability,
  retrieval weakness, exact-token preservation, and protected-topic triage.
- Do not treat the 270 benchmark questions as the full audit scope. The full coverage
  audit scope is the selected repository-local source corpus recorded through
  `GPTs/reports/source_inventory.md`, `GPTs/reports/coverage_matrix.md`, and later
  `GPTs/reports/full_coverage_audit/source_item_catalog.tsv`.
- Do not lower benchmark thresholds, edit question expectations, or use non-repository
  Altibase facts to improve scores.
- Later catalog and matrix jobs must preserve exact literal token forms from selected
  sources and questions where those tokens are used as benchmark evidence.
- Remaining `Missing` and `Retrieval-weak` dispositions in the new full coverage audit
  artifacts are unresolved until remediated, routed, or converted to a justified
  `Guardrail` or `Out-of-scope` disposition.

## FCA-J001 Verification

Verification run for this job:

| Check | Result |
| --- | --- |
| `LC_ALL=C rg -n '[^ -~\t]' GPTs/reports/full_coverage_audit/source_corpus_lock.md` | No matches; the new audit lock is ASCII-only. |
| `git diff --check` | Pass. |
| `bash review/scripts/run_review_stage.sh validate` | Pass; validation reported 20 upload attachments excluding `README.md` and completed without errors. |
| Review-report verdict/severity scan | `rg` returned `Verdict: Pass` lines for `R00` through `R27` and no actionable severity rows. |

## FCA-J001 Residual Risk And Handoff

- `FCA-J001` did not run a new 270-question live benchmark. It locked the existing
  latest run because the job scope is preflight and evidence locking.
- `FCA-J001` did not perform item-level source extraction. `FCA-J002` must freeze the
  selected source corpus in this file or a successor section before catalog jobs add
  rows.
- Existing guardrail and verification-limited entries in `GPTs/reports/gap_register.md`
  remain active until new audit registers supersede them with traceable dispositions.
- The pre-existing `.codex-jobs/altibase-gpt-full-coverage-audit/jobs.tsv` status
  modification is workflow state owned by the orchestrator; this project commit should
  include only scoped repository audit artifacts.
