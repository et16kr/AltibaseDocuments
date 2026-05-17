# Altibase GPT Final Validation Readiness

- Job: `J022` (`altibase-gpt-customer-llm-remediation`)
- Status: repository validation pass; final live full-benchmark rerun pending
- Date: 2026-05-17
- Scope: validation reports, `evals/altibase_answerability/reports/`,
  `GPTs/reports/final_upload_readiness.md`

## Reconfirmed Requirement And Boundary

J022 finalizes the repository-side readiness handoff after the customer LLM
remediation workflow. The job is bounded to validation evidence, readiness reporting,
the full-benchmark rerun plan, and residual-risk summary.

This job does not add, remove, rename, or rewrite customer-facing attachment content.
It does not edit original manuals, benchmark thresholds, durable question expectations,
judge rules, or source documents.

## Design Note

J022 replaces the older final-readiness handoff with the current remediation-workflow
handoff and adds a durable rerun plan:

- `GPTs/reports/final_upload_readiness.md`: current repository validation and readiness
  decision.
- `evals/altibase_answerability/reports/full_benchmark/rerun_plan_j022_20260517.md`:
  exact full-benchmark rerun instructions, gating thresholds, and triage order.
- `evals/altibase_answerability/reports/README.md`: pointer to the J022 rerun plan.

This is a documentation-structure change only. Product behavior, customer-facing
Altibase facts, source boundaries, and benchmark acceptance thresholds are unchanged.

## Evidence Reviewed

Primary benchmark evidence:

- `evals/altibase_answerability/reports/full_benchmark/failure_root_cause_analysis_20260517.md`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_095919/summary.txt`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_095919/judge/aggregate_report.json`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_095919/judge/judgments.jsonl`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_095919/answers/answers.jsonl`
- `evals/altibase_answerability/questions/*.jsonl`

Remediation and final-review evidence:

- `GPTs/reports/customer_answer_contract.md`
- `GPTs/reports/answerability_failure_remediation_inventory_20260517.md`
- `GPTs/reports/exact_token_gap_inventory_20260517.md`
- `evals/altibase_answerability/reports/targeted_calibration_j019_20260517.md`
- `GPTs/reports/j020_residual_gap_remediation_design.md`
- `GPTs/reports/j021_customer_llm_editorial_qa.md`

The stored 2026-05-17 full run remains the comparison baseline, not the current final
readiness result. It used `full_benchmark`, 270 questions, `mode=live`,
`provider=command`, `model=codex-exec`, `context_mode=lexical`, and did not include
`GPTs/GPT_Instructions_Draft.md` in the answer prompt.

Baseline result before the final remediation jobs:

| Metric | Stored 2026-05-17 run |
| --- | ---: |
| Passed / total | 27 / 270 |
| Pass rate | 10.0% |
| Critical fact coverage | 68.7% |
| Required token preservation | 74.6% |
| Unsupported-claim rate | 0.4% |
| Protected-topic blockers | 77 |

J019 and J020 narrowed the dominant risk: in the representative calibration sample, 11
of 12 old failures had all missed items in current lexical context and were classed as
answer synthesis gaps; the remaining sampled `PROP-117` retrieval gap was remediated
with a `RESULT_CACHE_MEMORY_MAXIMUM` retrieval anchor and deterministic dry-run checks.

## Upload Package Boundary

The upload package remains exactly these 20 Markdown files:

1. `00_version_release_platform.md`
2. `01_getting_started_installation.md`
3. `02_administration_operations.md`
4. `03_sql_ddl_generation.md`
5. `04_sql_dml_oracle_compatibility.md`
6. `05_data_types_properties.md`
7. `06_data_dictionary_performance_views.md`
8. `07_error_messages_troubleshooting.md`
9. `08_performance_tuning_monitoring.md`
10. `09_replication_ha_cdc.md`
11. `10_psm_stored_external_procedures.md`
12. `11_java_jdbc_spring.md`
13. `12_c_cli_odbc_precompiler.md`
14. `13_isql_iloader_basic_tools.md`
15. `14_utilities_operation_tools.md`
16. `15_migration_oracle_compatibility.md`
17. `16_dblink_external_connectors.md`
18. `17_kubernetes_aku_cloud.md`
19. `18_security_ssl_tls.md`
20. `19_spatial_nifi_tableau_misc.md`

`GPTs/attachments/README.md` is the attachment-set policy/readme file and is not
counted as an upload attachment.

## Repository Validation Readiness

Repository-side validation passed for the current package:

- exactly 20 upload Markdown files under `GPTs/attachments/`, excluding `README.md`;
- every upload file has `Applicable Versions`, `Questions This File Can Answer`,
  `Retrieval Alias Index`, `Source Documents`, `Response Rules`,
  `Attachment Cross-References`, and `Residual Scope`;
- every upload file preserves `Altibase 8.1 verified source` wording for 8.1 coverage;
- no image references, local source paths, `file://` links, Windows drive paths, or
  local workstation paths appear in customer-facing attachments or GPT instructions;
- no Korean, Chinese, Japanese, or other CJK prose appears in canonical English
  attachment files;
- Markdown code fences are balanced in upload attachments;
- benchmark schemas, questions, manifests, answer runner, and judge/report self-tests
  passed;
- full-benchmark lexical dry-run and J019 instruction-aware targeted dry-run passed
  schema and leakage validation.

## Residual Risk Summary

| Risk | Current handling | Required next check |
| --- | --- | --- |
| The 270-question live benchmark has not been rerun after the final remediation workflow. | Treat the stored 2026-05-17 live run as baseline evidence only. | Run the full live rerun in `evals/altibase_answerability/reports/full_benchmark/rerun_plan_j022_20260517.md`. |
| The readiness manifest tests attachment-only behavior and does not include `GPTs/GPT_Instructions_Draft.md`. | Keep the attachment-only run as the comparable readiness gate; use instruction-aware targeted checks as supplemental evidence. | If synthesis gaps remain, run the instruction-aware target set before changing content. |
| Old protected-topic blockers covered backup/recovery, destructive SQL, replication state changes, security/TLS, and version-sensitive properties. | Current attachments and GPT instructions now require missing inputs, first checks, validation SQL, and stop conditions. | Any remaining protected-topic blocker after rerun is release-blocking until triaged. |
| Guardrail and verification-limited entries remain in support reports. | Attachments must ask for exact patch level, object definition, log excerpt, topology, installed metadata, or runtime evidence where required. | Do not invent unsupported compatibility, exhaustive column, error-code, tool, or integration claims. |
| Tool, compiler, Kubernetes, TLS, third-party connector, and live server execution was not performed by this documentation job. | Source-backed documentation exists, but runtime behavior remains environment-specific. | Ask for installed version, command output, log excerpt, client/tool version, and environment before definitive operational advice. |

## Full-Benchmark Rerun Gate

The next readiness decision must come from a new live run, not from this documentation
report. Use:

- primary plan: `evals/altibase_answerability/reports/full_benchmark/rerun_plan_j022_20260517.md`;
- required manifest: `evals/altibase_answerability/manifests/full_benchmark.json`;
- provider command: `evals/altibase_answerability/scripts/codex_exec_provider.sh`;
- output location: `evals/altibase_answerability/reports/full_benchmark/runs/<new-run-id>/`;
- thresholds: `evals/altibase_answerability/policy.json`.

The readiness gates remain:

- overall pass rate at least 85.0%;
- every domain pass rate at least 80.0%;
- critical fact coverage at least 90.0%;
- required token preservation at least 95.0%;
- unsupported-claim rate no more than 2.0%;
- protected-topic blockers equal to 0.

Do not lower thresholds, rewrite expected questions, or edit original manuals to pass
the benchmark. If the rerun fails, classify failures as content gap, retrieval gap,
answer synthesis gap, or judge calibration issue after inspecting the selected context,
full attachment context, answer, and source-backed expected items.

## Verification Summary

J022 verification commands:

```bash
python3 evals/altibase_answerability/scripts/validate_benchmark.py \
  --manifest evals/altibase_answerability/manifests/full_benchmark.json
python3 evals/altibase_answerability/scripts/validate_benchmark.py \
  --manifest evals/altibase_answerability/manifests/targeted_calibration_j019_instruction.json
python3 evals/altibase_answerability/scripts/answer_runner.py --self-test
python3 evals/altibase_answerability/scripts/judge_report.py --self-test
python3 evals/altibase_answerability/scripts/answer_runner.py \
  --manifest evals/altibase_answerability/manifests/full_benchmark.json \
  --mode dry_run \
  --context-mode lexical \
  --validate-output \
  --output-dir /tmp/altibase-j022-full-lexical-dry-run
python3 evals/altibase_answerability/scripts/answer_runner.py \
  --manifest evals/altibase_answerability/manifests/targeted_calibration_j019_instruction.json \
  --mode dry_run \
  --context-mode lexical \
  --question-id PROP-101 --question-id PROP-105 --question-id PROP-117 \
  --question-id SQL-103 --question-id SQL-108 --question-id SQL-142 \
  --question-id OPS-117 --question-id REPL-118 --question-id ERR-116 \
  --question-id VPM-112 --question-id TOOL-010 --question-id TOOL-036 \
  --validate-output \
  --output-dir /tmp/altibase-j022-instruction-target-dry-run
git diff --check
bash review/scripts/run_review_stage.sh validate
rg -n "^Verdict:|^\\| (Blocker|High|Medium|Low) \\|" review/reports/R*.md
```

Result: pass. The review-report scan returned only `Verdict: Pass` lines and no
actionable `Blocker`, `High`, `Medium`, or `Low` finding rows.

The full 270-question live benchmark was intentionally not run in J022 because it would
launch 270 live `codex-exec` answer generations. The repository is ready for that
final rerun under the plan above.

## Readiness Decision

The current repository package is ready for final full-benchmark rerun and controlled
upload preparation. It is not yet certified as a fresh live benchmark pass.

Proceed to the J022 rerun plan. Treat any post-rerun protected-topic blocker, severe
critical-fact miss, or required-token regression as blocking until triaged from the
repository-local selected sources and current attachment context.
