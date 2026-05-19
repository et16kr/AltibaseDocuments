# Stage 4 Retrieval And Answerability Dry-Run Gate

- Job: `S4-J010`
- Date: 2026-05-19
- Scope: deterministic upload-package, retrieval-context, schema, leakage, and
  benchmark dry-run validation against the assembled Stage 4 package boundary
- Verdict: Pass for deterministic package checks and the existing lexical dry-run
  gate; no package-context benchmark pass or live benchmark pass is claimed

## Requirement And Boundary

`S4-J010` reconfirms the assembled upload package and runs the safest benchmark
dry-run validation available without changing benchmark questions, expected answers,
or runner behavior. The job does not edit upload Markdown, benchmark expected-answer
records, durable questions, judge rules, or live-run thresholds.

The final upload package remains the 20 Markdown files under `GPTs/upload_package/`.
Reports, manifests, crosswalks, benchmark artifacts, and source evidence remain
outside the upload package unless intentionally transformed into one of those 20 files
and listed in the Stage 4 upload manifest.

## Design Note

This job changes documentation state only. It records the dry-run gate, the current
benchmark runner limitation, and the live-benchmark routing decision. It does not
change package architecture, answer-generation code, benchmark expectations, or
customer-facing Altibase behavior.

Because the current benchmark runner is explicitly attachment-bound, a true
`GPTs/upload_package/` benchmark requires a later scoped tooling change or a documented
operator-approved harness. Until that exists, the dry-run gate uses the existing
lexical attachment-context validation and separately validates the upload package with
the Stage 4 package validator.

## Package File Count And Manifest

| Check | Result |
| --- | --- |
| Upload Markdown count | Pass: `GPTs/upload_package/` contains exactly 20 Markdown files. |
| Manifest confirmation | Pass: `stage_04_upload_package_manifest.tsv` has 20 rows; all rows are assembled and count against the global 20-file limit. |
| Package validator | Pass: `validate_upload_package.py --assembled` confirmed required sections, package boundary scans, source/baseline/playbook/attachment crosswalk routes, excluded-source handling, AID limitation labels, stale-placeholder scan, and CJK scan. |

## Commands And Results

| Gate | Command | Result |
| --- | --- | --- |
| Package validator | `python3 GPTs/reports/scripts/validate_upload_package.py --assembled` | Pass: 20 manifest rows and 20 upload Markdown files validated. |
| Benchmark schema validation | `python3 evals/altibase_answerability/scripts/validate_benchmark.py --manifest evals/altibase_answerability/manifests/full_benchmark.json` | Pass: 11 schemas, 7 question files, 270 questions, and full-profile domain counts validated. |
| Answer-runner self-test | `python3 evals/altibase_answerability/scripts/answer_runner.py --self-test` | Pass. |
| Judge/report self-test | `python3 evals/altibase_answerability/scripts/judge_report.py --self-test` | Pass. |
| Existing lexical dry-run | `python3 evals/altibase_answerability/scripts/answer_runner.py --manifest evals/altibase_answerability/manifests/full_benchmark.json --run-id s4_j010_full_lexical_dry_run_20260519 --mode dry_run --context-mode lexical --validate-output --output-dir /tmp/s4_j010_full_lexical_dry_run` | Pass: wrote 270 answer records with `errors=0`. |

## Package-Context Benchmark Decision

The current benchmark scripts cannot run directly against `GPTs/upload_package/`
without a code or manifest-policy change:

- `full_benchmark.json` sets `answer_generation.attachment_glob` to
  `GPTs/attachments/*.md`;
- `answer_runner.py` validates that the manifest attachment glob is exactly
  `GPTs/attachments/*.md`;
- `answer_runner.py` also rejects context paths outside `GPTs/attachments/`.

Therefore no package-context benchmark result is claimed here. The package itself is
covered by `validate_upload_package.py --assembled`; the benchmark dry-run evidence is
the existing lexical attachment-context dry-run, which is the safest supported runner
path that preserves the locked benchmark questions and expected answers.

## Dry-Run Retrieval Context

The lexical dry-run used `context_mode=lexical`, `mode=dry_run`, `provider=offline`,
and `model=fixture`. Dry-run records intentionally have status `skipped`; they prove
projection, context construction, schema validation, and leakage checks, not answer
quality.

Summary from `/tmp/s4_j010_full_lexical_dry_run/run.json` and `answers.jsonl`:

| Metric | Result |
| --- | ---: |
| Answer records | 270 |
| Runner errors | 0 |
| Leakage-check failures | 0 |
| Dry-run statuses | 270 `skipped` |
| Unique context files selected | 21 attachment Markdown files, including `GPTs/attachments/README.md` |
| Selected attachment files per question | min 4, max 19, average 11.6 |
| Selected context characters per question | min 179,852, max 179,997, average 179,959 |
| Selected context chunks per question | min 26, max 71, average 37.8 |

The 21-file attachment-context source set differs from the 20-file upload package
because `GPTs/attachments/README.md` is part of the attachment glob but is not an
upload-package file. This is a benchmark-routing limitation, not an upload-package file
count issue.

## Schema And Leakage Results

| Area | Result |
| --- | --- |
| Benchmark manifest and question schemas | Pass via `validate_benchmark.py` full profile. |
| Answer record schema | Pass via `answer_runner.py --validate-output` during the 270-question dry-run. |
| Runner leakage self-test | Pass via `answer_runner.py --self-test`. |
| Dry-run leakage checks | Pass: 0 of 270 answer records reported leakage-check failure. |
| Judge/report schema self-test | Pass via `judge_report.py --self-test`. |
| Upload-package leakage and boundary scans | Pass via `validate_upload_package.py --assembled`. |

## Residual Gaps And Risks

- No live 270-question benchmark was run for this job, so no live benchmark pass,
  readiness pass, or answer-quality improvement is claimed.
- No package-context benchmark was run because the current runner is intentionally
  attachment-bound. A later scoped tool change must preserve the same leakage boundary
  before package-context live results can be compared.
- The latest recorded full live comparison run remains
  `altibase_answerability_20260517_095919`, with `blocking_gaps`, 27/270 passed,
  10.0% pass rate, 68.7% critical fact coverage, 74.6% required token preservation,
  0.4% unsupported-claim rate, and 77 protected-topic blockers.
- The existing root-cause analysis still applies as residual risk until a new judged
  live run proves otherwise: answer synthesis/extraction gaps dominate critical-fact
  misses, while token misses include both omitted selected-context tokens and tokens
  absent from the full attachment set.
- Protected-topic risk remains open for backup/recovery, destructive SQL,
  replication state changes, security/TLS, and version-sensitive property changes
  until a live judged run reaches the configured policy gates.

## Live Benchmark Routing Decision

No live benchmark was performed and no live benchmark pass is claimed.

A future package-specific live benchmark requires explicit operator approval before
starting, an output path recorded before generation, unchanged benchmark questions and
expected answers, and either a package-aware runner or a documented package-context
harness that preserves answer-input allowlisting and judge-only leakage protection.

## Self-Review

- The report distinguishes deterministic dry-run evidence from live answer-quality
  evidence.
- No benchmark expected-answer files were changed.
- The upload package remains exactly 20 Markdown files.
- The package-targeting limitation is recorded instead of being worked around by
  changing benchmark expectations.
- The residual-gap section cites only existing recorded benchmark evidence and does
  not claim a new live result.
