# Source-Preserving Upload Package Readiness Review

- Job: `SPF-J008`
- Date: 2026-05-19
- Package: `GPTs/upload_package/`
- Verdict: `Conditional-ready`

## Verdict

The source-preserving upload package is conditionally ready as the primary
source-preserving Altibase corpus for GPT Knowledge, Codex, and LLM/RAG use.
The condition is explicit: this review proves deterministic package integrity,
schema validity, answer-runner and judge self-tests, and package-aware dry-run
routing. It does not claim live answer-quality readiness, because no live
benchmark was approved or run for this job.

No structural blocker was found for uploading the 20 Markdown package files as
the source-preserving corpus. A future live answerability claim still requires
operator approval and a pre-recorded output path before running the package-aware
live benchmark.

## Evidence Reviewed

This review inspected the SPF finalization plan, remediation note, current
source-preserving upload README, Stage 4 retrieval dry-run note, S4-J010
package-context rerun note, SPF reports from `SPF-J001` through `SPF-J006`, the
coding-agent manifest/rubric/question set from `SPF-J007`, current package
files, validator scripts, package-aware benchmark manifests, and recent SPF
commits through `993933bb evals: add source-preserving coding agent benchmark`.

Relevant prior evidence:

- `SPF-J001` recorded the clean preflight boundary and no live benchmark approval.
- `SPF-J002` added source-body integrity validation for the package.
- `SPF-J003` normalized final-upload wording outside source blocks.
- `SPF-J004` added GPT/Codex/LLM retrieval and safety instructions.
- `SPF-J005` added shard retrieval metadata outside source blocks.
- `SPF-J006` added the source-preserving package dry-run route for the unchanged
  270-question benchmark.
- `SPF-J007` added the separate coding-agent benchmark profile and 10-question
  AGENT question set.

## Package Summary

| Metric | Result |
| --- | ---: |
| Markdown files in `GPTs/upload_package/` | 20 |
| Total package bytes | 59,738,374 |
| Approximate total size | 56.97 MiB |
| Source shard files | 16 |
| Manifest/wrapper files | 4 |
| Selected sources represented | 941 |
| Source-to-shard rows | 941 |
| Parsed source blocks | 941 |
| Largest file by size | `source_pack_shard_001.md` at 4.30 MiB |
| Largest estimated-token file | `source_pack_shard_011.md` at 945,291 tokens |

## Final Validation Commands

| Gate | Command | Result |
| --- | --- | --- |
| Source-preserving package validator | `python3 GPTs/reports/scripts/validate_source_preserving_upload_package.py --strict-final` | Pass: 20 package files, 941 selected sources, 941 source-to-shard rows, 941 parsed source blocks. |
| Package-aware 270 benchmark schema | `python3 evals/altibase_answerability/scripts/validate_benchmark.py --manifest evals/altibase_answerability/manifests/full_benchmark_source_preserving_package.json` | Pass: 11 schemas, 7 question files, 270 questions, full profile domain counts validated. |
| Coding-agent benchmark schema | `python3 evals/altibase_answerability/scripts/validate_benchmark.py --manifest evals/altibase_answerability/manifests/coding_agent_source_preserving_package.json --profile coding_agent` | Pass: 11 schemas, 1 question file, 10 questions, coding-agent profile validated. |
| Answer-runner self-test | `python3 evals/altibase_answerability/scripts/answer_runner.py --self-test` | Pass. |
| Judge/report self-test | `python3 evals/altibase_answerability/scripts/judge_report.py --self-test` | Pass. |
| Package-aware 270 dry run | `python3 evals/altibase_answerability/scripts/answer_runner.py --manifest evals/altibase_answerability/manifests/full_benchmark_source_preserving_package.json --run-id spf_j008_full_source_preserving_dry_run_20260519 --mode dry_run --context-mode lexical --validate-output --output-dir /tmp/spf_j008_full_source_preserving_dry_run` | Pass: 270 answer records, `errors=0`. |
| Coding-agent dry run | `python3 evals/altibase_answerability/scripts/answer_runner.py --manifest evals/altibase_answerability/manifests/coding_agent_source_preserving_package.json --run-id spf_j008_coding_agent_source_preserving_dry_run_20260519 --mode dry_run --context-mode lexical --validate-output --output-dir /tmp/spf_j008_coding_agent_source_preserving_dry_run` | Pass: 10 answer records, `errors=0`. |

## Source-Body Integrity

The strict-final package validator passed. It parsed all 941
`SOURCE_BLOCK_BEGIN` / `SOURCE_BLOCK_END` bodies and compared each body SHA-256
against the recorded `source_sha256` metadata. This is the required integrity
rule for the finalized package because wrapper wording and retrieval metadata
may differ from `GPTs/source_pack/`, while source body bytes must remain
unchanged.

The validator also confirmed strict-final wrapper wording: no reverse-routing
wrapper blockers such as `Upload intended: no` or not-final upload language were
found outside source blocks.

## Benchmark Dry-Run Results

The 270-question package-aware dry run used:

- Manifest: `full_benchmark_source_preserving_package`
- Context glob: `GPTs/upload_package/*.md`
- Context root: `GPTs/upload_package`
- Mode/provider/model: `dry_run` / `offline` / `fixture`
- Output: `/tmp/spf_j008_full_source_preserving_dry_run`

Summary from `run.json` and `answers.jsonl`:

| Metric | Result |
| --- | ---: |
| Answer records | 270 |
| Runner errors | 0 |
| Dry-run statuses | 270 `skipped` |
| Leakage-check failures | 0 |
| Unique selected context files | 18 |
| Selected context files per question | min 2, max 16, avg 9.5 |
| Selected context characters per question | min 179,897, max 179,997, avg 179,966.2 |
| Selected context chunks per question | min 24, max 149, avg 59.7 |

The coding-agent dry run used:

- Manifest: `coding_agent_source_preserving_package`
- Context glob: `GPTs/upload_package/*.md`
- Context root: `GPTs/upload_package`
- Mode/provider/model: `dry_run` / `offline` / `fixture`
- Output: `/tmp/spf_j008_coding_agent_source_preserving_dry_run`

Summary from `run.json` and `answers.jsonl`:

| Metric | Result |
| --- | ---: |
| Answer records | 10 |
| Runner errors | 0 |
| Dry-run statuses | 10 `skipped` |
| Leakage-check failures | 0 |
| Unique selected context files | 17 |
| Selected context files per question | min 7, max 10, avg 8.8 |
| Selected context characters per question | min 179,916, max 179,990, avg 179,960.9 |
| Selected context chunks per question | min 28, max 51, avg 39.1 |

These dry runs validate projection, allowlisted package context construction,
answer-record schema, output writing, and leakage checks. They do not validate
live answer quality.

## Coding-Agent Coverage

The coding-agent benchmark is separate from the locked 270-question full
benchmark. It contains 10 `AGENT-*` questions and uses the dedicated
`coding_agent` validation profile.

Task-type coverage:

| Task type | Questions |
| --- | ---: |
| `backup_recovery_safety` | 1 |
| `destructive_operation_safety` | 1 |
| `driver_api_usage` | 2 |
| `error_diagnosis` | 1 |
| `property_version_check` | 1 |
| `replication_safety` | 1 |
| `security_safety` | 1 |
| `source_navigation` | 1 |
| `sql_isql_generation` | 1 |

Domain coverage:

| Domain | Questions |
| --- | ---: |
| `errors_troubleshooting` | 1 |
| `operations_admin` | 1 |
| `properties` | 1 |
| `replication_cdc_security_network` | 2 |
| `sql_ddl_dml_datatypes` | 2 |
| `tools_apis_connectors_migration` | 3 |

Answer artifact types covered: `tool_api` 3, `runbook` 3,
`sql_generation` 2, `troubleshooting` 1, and `mixed` 1.

## Live-Benchmark Routing Decision

No live benchmark was run for `SPF-J008`, and this report does not claim a live
benchmark pass.

The source-preserving package-aware route now exists through
`evals/altibase_answerability/manifests/full_benchmark_source_preserving_package.json`.
A future live 270-question benchmark must be started only after explicit
operator approval and a durable output path are recorded before generation. The
run must preserve the locked 270 question records, expected answers, answer-input
allowlist, judge-only leakage protections, and package context rooted at
`GPTs/upload_package/`.

Until that run exists and is judged, the latest live answerability evidence
remains the earlier recorded full-benchmark evidence, not a source-preserving
package live-readiness pass.

## Residual Risks

- Live answer quality is unproven for the source-preserving package in this job.
- Dry-run lexical context selection proves routing mechanics, not factual answer
  synthesis.
- The source-preserving package is large; retrieval quality depends on the GPT,
  Codex, or RAG system respecting the README lookup workflow and source-block
  citation contract.
- Protected topics such as backup/recovery, destructive SQL, replication state
  changes, TLS/security, and version-sensitive property changes still require
  live judged evidence before any answer-quality readiness claim.

## Self-Review

- The report cites only commands that were run during this job or already
  recorded in prior SPF evidence.
- The report treats dry-run results as deterministic routing and schema evidence,
  not live model answer-quality evidence.
- The report preserves the source integrity rule as source-body SHA-256 checking,
  not whole-shard equality after wrapper normalization.
- The locked 270 benchmark questions and expected answers were not changed.
- No live benchmark pass is claimed.
