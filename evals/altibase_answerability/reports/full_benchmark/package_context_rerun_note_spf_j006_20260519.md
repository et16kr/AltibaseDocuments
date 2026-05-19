# SPF-J006 Source-Preserving Package Context Rerun Note

- Date: 2026-05-19
- Job: `SPF-J006`
- Scope: package-aware dry-run route for the existing 270-question full benchmark
- Decision: source-preserving package dry-run routing now exists; no live benchmark
  was started, and no live benchmark pass is claimed

## Package-Aware Route

`evals/altibase_answerability/manifests/full_benchmark_source_preserving_package.json`
selects the same seven durable question files as
`evals/altibase_answerability/manifests/full_benchmark.json`. The benchmark questions,
expected facts, canonical answers, required tokens, prohibited claims, and judge
threshold policy remain unchanged.

The package-aware manifest changes only answer-generation context routing:

- `answer_generation.attachment_glob`:
  `GPTs/upload_package_source_preserving/*.md`
- `answer_generation.context_root`:
  `GPTs/upload_package_source_preserving`
- `answer_generation.gpt_instruction_draft_path`:
  `GPTs/reports/source_preserving_upload_package_finalization_plan.md`

The runner and validator now allow context only through an explicit glob-to-root
allowlist. The added source-preserving package route is separate from the legacy
`GPTs/attachments/*.md` route and still uses the same answer-input allowlist from
`policy.json`.

## Dry-Run Evidence

The package-aware dry run used `mode=dry_run`, `provider=offline`, `model=fixture`,
and `context_mode=lexical`. It did not call a live model.

```bash
python3 evals/altibase_answerability/scripts/answer_runner.py \
  --manifest evals/altibase_answerability/manifests/full_benchmark_source_preserving_package.json \
  --run-id spf_j006_source_preserving_package_dry_run_20260519 \
  --mode dry_run \
  --context-mode lexical \
  --validate-output \
  --output-dir /tmp/spf_j006_source_preserving_package_dry_run
```

Result: pass for dry-run mechanics; 270 answer records were written with
`errors=0`.

`/tmp/spf_j006_source_preserving_package_dry_run/run.json` records:

| Field | Value |
| --- | --- |
| `manifest_id` | `full_benchmark_source_preserving_package` |
| `answer_records` | `270` |
| `errors` | `0` |
| `attachment_glob` | `GPTs/upload_package_source_preserving/*.md` |
| `context_source_glob` | `GPTs/upload_package_source_preserving/*.md` |
| `context_root` | `GPTs/upload_package_source_preserving` |
| `mode` | `dry_run` |
| `provider` | `offline` |
| `model` | `fixture` |

## Validation Commands

| Gate | Command | Result |
| --- | --- | --- |
| Source-preserving package validator | `python3 GPTs/reports/scripts/validate_source_preserving_upload_package.py --strict-final` | Pass: 20 files, 941 selected sources, 941 source-to-shard rows, and 941 parsed source blocks. |
| Package-aware benchmark schema validation | `python3 evals/altibase_answerability/scripts/validate_benchmark.py --manifest evals/altibase_answerability/manifests/full_benchmark_source_preserving_package.json` | Pass: 11 schemas, 7 question files, 270 questions, full profile domain counts validated. |
| Answer-runner self-test | `python3 evals/altibase_answerability/scripts/answer_runner.py --self-test` | Pass. |
| Judge/report self-test | `python3 evals/altibase_answerability/scripts/judge_report.py --self-test` | Pass. |
| Package-aware dry run | Command shown above | Pass: 270 records, `errors=0`. |

## Leakage And Boundary Review

- Answer input is still projected only from the policy allowlist: `id`, `question`,
  `version_scope`, `user_level`, `answer_type`, `answer_language`, and
  `requested_language`.
- Judge-only question fields remain excluded from projected input, prompt scaffold,
  and request payload keys before any provider call.
- Source-context files must match the manifest glob and remain under the explicit
  context root paired with that glob.
- The source-preserving package route does not allow `evals/altibase_answerability/`
  question or expected-answer files into answer-generation context.

## Residual Limits

This note proves package-aware dry-run routing, schema validation, output validation,
and leakage-boundary mechanics. It does not prove answer quality. A future live
package-context benchmark still requires explicit operator approval and a recorded
durable output path before starting.
