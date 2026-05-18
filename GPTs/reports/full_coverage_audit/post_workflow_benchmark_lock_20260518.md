# Post-Workflow Benchmark Evidence Lock

- Job ID: `PWF-J001`
- Date: 2026-05-18
- Repository: `/home/et16/AltibaseDocuments`
- Evidence baseline: `altibase_answerability_20260518_091947`
- Status: Locked as the official post-workflow full benchmark evidence baseline.
- Scope: evidence recording only. This job does not remediate `GPTs/attachments/`
  content or change benchmark judgments.

## Lock Decision

`altibase_answerability_20260518_091947` is the official post-workflow full
benchmark evidence baseline.

The locked readiness decision is `blocking_gaps`. This means the attachment set is
not upload-ready by the benchmark policy. The decision is evidence-only in this
document; remediation is deferred to later scoped jobs.

Decision reasons recorded by the judge:

- overall pass rate below threshold;
- one or more domains below pass-rate threshold;
- critical fact coverage below threshold;
- required token preservation below threshold;
- protected-topic blocker findings present.

## First-Check Evidence

Required first checks from `AGENTS.md` were run before project edits:

| Check | Result |
| --- | --- |
| `bash review/scripts/run_review_remediation_cycle.sh status` | `R00` through `R27` were all `Done` for both cycle and review status. |
| `rg -n $'\t(Reviewing\|Remediating\|ReReviewing\|Fail)$' review/review_remediation_cycle_status.tsv` | No active or failed cycle rows; exit code `1` with no matches. |
| `git status --short` | Only `.codex-jobs/altibase-gpt-post-workflow-followup/jobs.tsv` was dirty before project edits. No project files outside workflow state were dirty. |

## Run Configuration

| Field | Value |
| --- | --- |
| Manifest | `full_benchmark` |
| Run ID | `altibase_answerability_20260518_091947` |
| Mode | `live` |
| Provider | `command` |
| Model | `codex-exec` |
| Provider command | `evals/altibase_answerability/scripts/codex_exec_provider.sh` |
| Context mode | `lexical` |
| Attachment glob | `GPTs/attachments/*.md` |
| Questions | `270` |
| Answer records | `270` |
| Answer runner errors | `0` |
| Answer run generated at | `2026-05-18T02:10:57Z` |
| Judge report generated at | `2026-05-18T02:10:58Z` |

The run log records successful benchmark schema validation, answer runner self-test,
judge/report self-test, answer generation for all `270` questions, and judge output
validation.

## Artifact Paths

| Artifact | Path |
| --- | --- |
| Run directory | `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260518_091947/` |
| Summary | `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260518_091947/summary.txt` |
| Human-readable judge report | `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260518_091947/judge/report.md` |
| Aggregate JSON | `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260518_091947/judge/aggregate_report.json` |
| Per-question judgments | `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260518_091947/judge/judgments.jsonl` |
| Generated answers | `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260518_091947/answers/answers.jsonl` |
| Answer runner metadata | `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260518_091947/answers/run.json` |
| Run log | `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260518_091947/run-test.log` |

## Overall Metrics

| Metric | Value | Threshold |
| --- | ---: | ---: |
| Passed / total | `98 / 270` | n/a |
| Failed | `172` | n/a |
| Pass rate | `36.3%` | `85.0%` minimum |
| Critical fact coverage | `82.5%` | `90.0%` minimum |
| Required token preservation | `89.2%` | `95.0%` minimum |
| Unsupported-claim rate | `1.1%` | `2.0%` maximum |
| Version handling | `92.8%` | tracked |
| Altibase-specific correctness | `84.0%` | tracked |
| Missing-input handling | `96.3%` | tracked |

## Domain Results

| Domain | Questions | Passed | Failed | Pass rate | Max severity |
| --- | ---: | ---: | ---: | ---: | --- |
| `errors_troubleshooting` | 30 | 12 | 18 | `40.0%` | `blocker` |
| `operations_admin` | 35 | 18 | 17 | `51.4%` | `blocker` |
| `properties` | 50 | 16 | 34 | `32.0%` | `blocker` |
| `replication_cdc_security_network` | 30 | 11 | 19 | `36.7%` | `blocker` |
| `sql_ddl_dml_datatypes` | 45 | 12 | 33 | `26.7%` | `blocker` |
| `tools_apis_connectors_migration` | 50 | 26 | 24 | `52.0%` | `high` |
| `views_performance_monitoring` | 30 | 3 | 27 | `10.0%` | `blocker` |

Worst domain by pass rate: `views_performance_monitoring` at `10.0%`.

## Protected-Topic Blockers

Total protected-topic blockers: `36`.

| Topic | Count | Question IDs |
| --- | ---: | --- |
| `backup_recovery` | 7 | `ERR-110`, `OPS-103`, `OPS-114`, `OPS-118`, `OPS-133`, `PROP-130`, `VPM-114` |
| `destructive_sql` | 3 | `ERR-120`, `ERR-128`, `SQL-105` |
| `replication_state_changes` | 8 | `ERR-127`, `PROP-136`, `REPL-113`, `REPL-116`, `REPL-118`, `SQL-114`, `SQL-141`, `VPM-125` |
| `security_tls` | 2 | `PROP-140`, `PROP-141` |
| `version_sensitive_property_changes` | 16 | `PROP-109`, `PROP-110`, `PROP-112`, `PROP-115`, `PROP-117`, `PROP-121`, `PROP-122`, `PROP-124`, `PROP-127`, `PROP-128`, `PROP-131`, `PROP-144`, `PROP-146`, `PROP-147`, `PROP-148`, `PROP-149` |

## Non-Remediation Boundary

This lock records the benchmark evidence exactly as generated. It intentionally does
not:

- edit any file under `GPTs/attachments/`;
- reinterpret failed judgments as passes;
- add new Altibase product behavior;
- start remediation for protected-topic blockers or domain failures.

Follow-up remediation should use this document and the locked artifacts above as the
baseline evidence.

## Job Verification

Post-edit checks for this evidence-lock job:

| Command | Result |
| --- | --- |
| `git diff --check` | Passed with no whitespace errors. |
| `bash review/scripts/run_review_stage.sh validate` | Passed with exit code `0`; validation listed all review stages as `Done`, counted `20` attachment files excluding `README`, and reported no residual image references or forbidden customer-facing strings in attachments. |

No validation checks were skipped.
