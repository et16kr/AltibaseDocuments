# FCA-J050 Validation And Targeted Answerability Results

- Workflow: `altibase-gpt-full-coverage-audit`
- Audit job: `FCA-J050`
- Date: 2026-05-18
- Status: Validation completed; full coverage closure remains blocked by active
  patch-note `Missing` rows and targeted answerability `blocking_gaps`

## Job Boundary

`FCA-J050` runs repository validation, source-to-attachment checks, targeted
answerability checks for failed/protected/exact-token rows, and decides whether a
selected full live rerun is feasible. This job does not edit original manuals or source
documents and does not add customer-facing product behavior.

Durable output for this job is this validation report plus the `FCA-J050` entry in
`remediation_log.md`.

## Inputs Inspected

- `AGENTS.md`
- `.codex-jobs/altibase-gpt-full-coverage-audit/jobs.tsv`
- `.codex-jobs/altibase-gpt-full-coverage-audit/jobs.md`
- `.codex-jobs/altibase-gpt-full-coverage-audit/prompts/FCA-J050.md`
- `GPTs/attachments/README.md`
- `GPTs/GPT_Instructions_Draft.md`
- `GPTs/reports/source_inventory.md`
- `GPTs/reports/coverage_matrix.md`
- `GPTs/reports/gap_register.md`
- `GPTs/reports/final_upload_readiness.md`
- `GPTs/reports/answerability_failure_remediation_inventory_20260517.md`
- `GPTs/reports/full_coverage_audit/`
- `evals/altibase_answerability/reports/full_benchmark/failure_root_cause_analysis_20260517.md`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_205641/summary.txt`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_205641/judge/report.md`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_205641/judge/aggregate_report.json`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_205641/judge/judgments.jsonl`

## First-Check Evidence

Required first checks from `AGENTS.md` were run before project edits:

| Check | Evidence | Result |
| --- | --- | --- |
| Review/remediation cycle status | `bash review/scripts/run_review_remediation_cycle.sh status` | `R00` through `R27` were all `Done` for both cycle and review status. |
| Active or failed cycle stages | `rg -n $'\t(Reviewing\|Remediating\|ReReviewing\|Fail)$' review/review_remediation_cycle_status.tsv` | No matches; exit code `1` means no active or failed cycle rows were present. |
| Worktree status before edits | `git status --short` | Only `.codex-jobs/altibase-gpt-full-coverage-audit/jobs.tsv` was modified. No project files outside workflow status/runtime files were dirty. |

## Source-To-Attachment Validation

Commands:

```bash
python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers
python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py catalog-qa
python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py matrix-qa
python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py guardrail-audit
```

Result: all four commands passed structurally.

| Check area | Result |
| --- | --- |
| Catalog rows | `2153` |
| Matrix rows | `2153` |
| Duplicate `source_item_id` values | `0` |
| Invalid controlled vocabulary values | `0` |
| ID namespace sequence gaps | `0` |
| Guardrail register reconciliation | Passed with `36` guarded rows |
| Active `Retrieval-weak` rows | `0` |
| Active `Missing` rows | `115` |

Coverage status totals in both catalog and matrix:

| coverage_status | Rows |
| --- | ---: |
| `Covered` | 1162 |
| `Covered-by-routing` | 840 |
| `Guardrail` | 33 |
| `Missing` | 115 |
| `Out-of-scope` | 3 |
| `Retrieval-weak` | 0 |

The active `Missing` rows are all `patch_notes` rows owned by
`GPTs/attachments/00_version_release_platform.md`. They are the remaining
`SRC-PATCH-PATCH-000001` through `SRC-PATCH-PATCH-000115` patch-note change-set rows
after later jobs resolved the non-patch-note `Missing` rows.

Full coverage closure is therefore not ready: the non-negotiable final-state rule still
requires these `115` rows to become `Covered`, `Covered-by-routing`, `Guardrail`, or
`Out-of-scope` before final sign-off. This job records the blocker but does not broaden
or remediate patch-note behavior outside the validation scope.

## Benchmark Harness Validation

Commands:

```bash
python3 evals/altibase_answerability/scripts/validate_benchmark.py \
  --manifest evals/altibase_answerability/manifests/full_benchmark.json
python3 evals/altibase_answerability/scripts/validate_benchmark.py \
  --manifest evals/altibase_answerability/manifests/targeted_calibration_j019_instruction.json \
  --profile fixture
python3 evals/altibase_answerability/scripts/answer_runner.py --self-test
python3 evals/altibase_answerability/scripts/judge_report.py --self-test
python3 evals/altibase_answerability/scripts/answer_runner.py \
  --manifest evals/altibase_answerability/manifests/full_benchmark.json \
  --mode dry_run \
  --context-mode lexical \
  --validate-output \
  --output-dir /tmp/altibase-fca-j050-full-lexical-dry-run
python3 evals/altibase_answerability/scripts/answer_runner.py \
  --manifest evals/altibase_answerability/manifests/targeted_calibration_j019_instruction.json \
  --mode dry_run \
  --context-mode lexical \
  --question-id PROP-101 --question-id PROP-105 --question-id PROP-112 \
  --question-id SQL-103 --question-id SQL-108 --question-id SQL-129 \
  --question-id OPS-116 --question-id REPL-121 --question-id ERR-116 \
  --question-id ERR-120 --question-id VPM-112 --question-id VPM-125 \
  --question-id TOOL-010 --question-id TOOL-036 \
  --validate-output \
  --output-dir /tmp/altibase-fca-j050-targeted-instruction-dry-run
```

Results:

| Check | Result |
| --- | --- |
| Full benchmark schema validation | Passed: `270` questions across `7` domains. |
| Targeted instruction manifest validation | Passed under fixture profile. |
| Answer runner self-test | Passed. |
| Judge/report self-test | Passed. |
| Full 270-question lexical dry-run | Passed: wrote `270` answer records, `errors=0`. |
| Targeted instruction-aware lexical dry-run | Passed: wrote `14` answer records, `errors=0`. |

## Targeted Live Answerability

The targeted sample was selected from the locked latest benchmark failures
`altibase_answerability_20260517_205641`, with emphasis on protected-topic blockers,
exact-token failures, and known post-remediation smoke questions.

Run configuration:

| Field | Value |
| --- | --- |
| Manifest | `targeted_calibration_j019_instruction` |
| Run ID | `fca_j050_targeted_instruction_20260518` |
| Mode | `live` |
| Provider/model | `command` / `codex-exec` |
| Provider command | `evals/altibase_answerability/scripts/codex_exec_provider.sh` |
| Context mode | `lexical` |
| GPT instruction draft | Included by manifest |
| Output location | `/tmp/altibase-fca-j050-targeted-live/` |

Overall result:

| Metric | Latest-run baseline for same 14 IDs | FCA-J050 targeted live |
| --- | ---: | ---: |
| Passed / total | 2 / 14 | 6 / 14 |
| Pass rate | 14.3% | 42.9% |
| Critical fact coverage | 73.3% | 81.8% |
| Required token preservation | 91.6% | 93.1% |
| Unsupported-claim rate | 0.0% | 0.0% |
| Protected-topic blockers | 6 | 4 |
| Readiness decision | `blocking_gaps` | `blocking_gaps` |

Per-question result:

| Question | Result | Max severity | Finding categories | Protected blocker | Critical facts | Tokens |
| --- | --- | --- | --- | --- | ---: | ---: |
| `PROP-101` | Fail | high | `missing_critical_facts` | none | 75% | 100% |
| `PROP-105` | Pass | none | none | none | 100% | 100% |
| `PROP-112` | Fail | blocker | `missing_critical_facts`, `missing_required_tokens` | `version_sensitive_property_changes` | 0% | 60% |
| `SQL-103` | Pass | none | none | none | 100% | 100% |
| `SQL-108` | Fail | high | `missing_critical_facts` | none | 40% | 100% |
| `SQL-129` | Fail | blocker | `missing_required_tokens` | `destructive_sql` | 100% | 71% |
| `OPS-116` | Fail | blocker | `missing_required_tokens` | `backup_recovery` | 100% | 71% |
| `VPM-112` | Pass | none | none | none | 100% | 100% |
| `VPM-125` | Fail | blocker | `missing_critical_facts` | `replication_state_changes` | 50% | 100% |
| `REPL-121` | Fail | high | `missing_critical_facts` | none | 80% | 100% |
| `ERR-116` | Pass | none | none | none | 100% | 100% |
| `ERR-120` | Pass | none | none | none | 100% | 100% |
| `TOOL-010` | Fail | medium | `missing_input_handling`, `missing_supporting_facts` | none | 100% | 100% |
| `TOOL-036` | Pass | none | none | none | 100% | 100% |

Notable movement compared with `altibase_answerability_20260517_205641` for the same
IDs:

| Question | Baseline | FCA-J050 targeted live |
| --- | --- | --- |
| `SQL-103` | Fail, high | Pass |
| `REPL-121` | Fail, blocker | Fail, high |
| `ERR-116` | Fail, medium | Pass |
| `ERR-120` | Fail, blocker | Pass |
| `TOOL-036` | Fail, high | Pass |

The targeted run confirms improvement in exact SQL/error/tool answer paths, but it is
not a readiness pass. Protected blockers remain for `PROP-112`, `SQL-129`, `OPS-116`,
and `VPM-125`; these must be triaged before upload readiness.

## Full Live Rerun Decision

A fresh 270-question live full benchmark was not launched in `FCA-J050`.

Rationale:

- the source-to-attachment closure gate is already blocked by `115` active
  `patch_notes` `Missing` rows;
- the 14-question targeted live run still returns `blocking_gaps` with `4` protected
  blockers;
- the full run would launch 270 live `codex-exec` provider calls and would produce a
  non-final readiness result until the active coverage and protected-topic blockers are
  addressed;
- deterministic full lexical dry-run already proved schema, projection, attachment
  context construction, and leakage checks for all `270` questions.

Use the existing full-rerun plan in
`evals/altibase_answerability/reports/full_benchmark/rerun_plan_j022_20260517.md` after
the active patch-note `Missing` rows and targeted protected blockers are resolved or
explicitly re-dispositioned.

## Residual Risk And Handoff

- Full source-to-attachment audit closure remains blocked by `115` active patch-note
  `Missing` rows in attachment `00`.
- Retrieval closure is clean for this validation pass: active `Retrieval-weak` rows are
  `0`.
- Guardrail audit is structurally clean: `36` guarded rows have register coverage and
  missing-input or safest-next-check patterns.
- Targeted answerability remains below readiness thresholds and still has protected
  blockers in version-sensitive property changes, destructive SQL, backup/recovery, and
  replication state changes.
- No original manuals, source documents, or customer-facing attachment product facts were
  changed by this validation job.
