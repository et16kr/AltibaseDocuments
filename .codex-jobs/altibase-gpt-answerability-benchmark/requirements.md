# Altibase GPT Answerability Benchmark Requirements

## Purpose

Create and maintain an answerability benchmark that determines whether `GPTs/attachments/`
is sufficient as an encyclopedia-grade Altibase reference after the attachment rebuild
workflow finishes.

The benchmark must be source-backed by the selected Altibase manuals, release notes,
technical documents, tool manuals, third-party guides, and approved supporting sources
already present in this repository. It should intentionally include questions that are
hard for the current attachment set, as long as the expected answer is present in the
selected source corpus.

## Source Authority And Answer Language

Korean Altibase manuals are the authoritative source when paired Korean and English
manuals differ. Benchmark questions and expected answers must therefore be derived from
Korean manuals first where Korean manuals exist for the same product area and version.

The benchmark's comparison language is canonical English:

- Write question records in English unless a specific multilingual test explicitly
  requires otherwise.
- Write `expected_facts`, any canonical reference answer, scoring notes, and report
  summaries in English.
- Translate and normalize Korean-source facts into concise English; do not store Korean
  prose as the expected answer. Korean section titles may appear in `source_refs` only
  when needed to locate the source.
- Keep SQL object names, SQL keywords, function names, property names, error codes,
  commands, paths, package/class/method/API names, connector names, and version labels
  literal in every language.
- The default attachments-only answer language is English. Optional multilingual tests
  must still judge semantic equivalence against the canonical-English expected facts.

## Persistent Artifact Location

Long-term benchmark artifacts belong under:

```text
evals/altibase_answerability/
```

Expected durable artifacts include:

- `README.md`: how to maintain and run the benchmark.
- `schemas/`: JSON schemas for questions, answer records, judgments, and aggregate reports.
- `questions/`: source-backed question sets, preferably one JSONL file per domain.
- `manifests/`: benchmark manifests that select question files and define run metadata.
- `scripts/`: validation, answer-runner, judge, and report scripts.
- `reports/`: generated reports, with large or transient outputs excluded if needed.
- `fixtures/`: small calibration samples that can run without the full benchmark.

The `.codex-jobs/altibase-gpt-answerability-benchmark/` directory is only the job
orchestration workflow. Do not store the long-term benchmark implementation only inside
the workflow directory.

## Benchmark Design

The benchmark must contain at least 200 source-backed questions. Target about 270
questions so later pruning still leaves more than 200 usable items. The benchmark
validator must fail if the total question count is below 200 or if any domain is below
its required minimum.

Required minimums and targets:

| Domain | Required minimum | Target |
| --- | ---: | ---: |
| Properties | 40 | 50 |
| SQL, DDL, DML, data types, JSON, LOB, functions, and Oracle differences | 35 | 45 |
| Installation, startup, shutdown, backup, restore, recovery, tablespace, and admin runbooks | 25 | 35 |
| Dictionary views, performance views, optimizer, plan, monitoring, SNMP, and tuning | 20 | 30 |
| Replication, CDC, Log Analyzer, RepMgr, security, TLS, and network diagnostics | 20 | 30 |
| Error codes, symptoms, cause/action, log collection, and troubleshooting | 20 | 30 |
| PSM, external procedures, JDBC, CLI, ODBC, Precompiler, iSQL, iLoader, utilities, connectors, Kubernetes, migration, Spatial, NiFi, and Tableau | 40 | 50 |

Job ownership for question counts:

- J004 must create at least 40 property questions and should target 50.
- J005 must create at least 35 SQL/DDL/DML/compatibility questions and should target 45.
- J006 must create at least 25 operations/admin questions and should target 35.
- J007 must create at least 20 view/performance/monitoring questions and should target 30.
- J008 must create at least 20 replication/CDC/security/network questions and should target 30.
- J009 must create at least 20 error/troubleshooting questions and should target 30.
- J010 must create at least 40 tools/API/connectors/migration questions and should
  target 50.

Include a mix of user levels: beginner, intermediate, advanced operator, developer, and
expert. Prefer questions that require Altibase-specific facts, syntax, properties,
commands, or views over generic database questions.

## Question Record Requirements

Each question record must include at least:

- Stable `id`.
- `domain` and `subdomain`.
- `user_level`.
- `version_scope` such as `7.1`, `7.3`, `8.1`, or `cross-version`.
- `question`.
- `answer_language`, defaulting to `en`.
- `source_language_basis`, such as `ko`, `en`, or `ko+en`, with `ko` or `ko+en` expected
  when Korean manuals are the authoritative basis.
- `source_refs` with manual/source name, version, section or heading, and enough locator
  detail for review.
- `expected_facts`: source-backed facts the answer must contain.
- Optional `canonical_reference_answer`: an English source-backed model answer for
  calibration and human review. This field is judge-only and must not be sent to the
  answering model.
- `required_tokens`: SQL keywords, property names, error codes, command options, view
  names, API names, or literal values that must remain unchanged.
- `prohibited_claims`: unsupported claims or common wrong assumptions the answer must not
  make.
- `answer_type`: reference, SQL generation, runbook, troubleshooting, compatibility,
  tool/API, or mixed.
- `difficulty` and `retrieval_risk`.

Do not create questions whose expected answer is not present in the selected source
corpus. The answer may be missing from the current attachments before the rebuild; that
is acceptable and useful.

## Answer Runner Requirements

The answer runner must evaluate whether the attachments are sufficient, so answer
generation may use only:

- `GPTs/attachments/*.md`
- an allowlisted projection of the question record
- optional GPT instruction draft material if explicitly selected by the manifest

The answering model input allowlist is:

- `id`
- `question`
- `version_scope`
- `user_level`
- `answer_type`
- `answer_language`, defaulting to `en`
- optional `requested_language` when a manifest explicitly asks for multilingual testing

All other question fields are judge-only unless a later reviewed schema change explicitly
moves them into the allowlist. The answer runner must not provide original manuals,
source inventory files, source references, expected facts, required tokens, prohibited
claims, canonical reference answers, source-language basis, retrieval risk, difficulty
labels, or any source excerpts to the answering model. It must record the exact projected
answering input for audit and include a leakage check that fails if judge-only keys
appear in answer-generation prompts or request payloads.

The answer runner must request English answers by default. If `requested_language` is
absent, it must set `answer_language` to `en` and instruct the answering model to answer
in English while preserving technical tokens literally.

The scripts must keep model/provider settings configurable and must support dry-run or
offline validation paths that do not require live model calls.

## Judge And Report Requirements

The judge may use the question record, expected facts, optional canonical reference
answer, required tokens, prohibited claims, source-language basis, and source references.
It must compare attachments-only answers against canonical-English expected facts derived
from Korean-first sources. It should score at least:

- Required fact coverage.
- Required token preservation.
- Version handling and assumptions.
- Altibase-specific correctness.
- Unsupported or hallucinated claims.
- Whether the answer asks for missing environment/log/object details only when needed.

Reports must aggregate results by domain, subdomain, user level, version scope,
answer type, and retrieval risk. The final report must make it clear whether the
attachment set is ready for GPT upload, needs targeted remediation, or has blocking gaps.

## Suggested Readiness Thresholds

Use these as initial thresholds, then calibrate them in the final job:

- Overall pass rate at least 85%.
- No domain below 80%.
- Critical fact coverage at least 90%.
- Required technical token preservation at least 95%.
- Unsupported-claim rate no more than 2%.
- No blocker findings for backup/recovery, destructive SQL, security/TLS, replication
  state changes, or version-sensitive property changes.

## Common Verification

Every job must run checks proportional to its scope. At minimum, use:

```bash
git diff --check
bash review/scripts/run_review_stage.sh validate
```

Question-generation jobs must run the benchmark validator once it exists. Script jobs
must include targeted unit or fixture checks that can run without external model calls.

Each successful job must review the final diff, create a focused commit, and leave
project files clean.

## Current Dirty Worktree Note

Before this workflow can run, current project changes outside
`.codex-jobs/altibase-gpt-answerability-benchmark/` must be committed, stashed, or
otherwise resolved. The workflow intentionally stops when project files are dirty so one
job's output cannot leak into the next job.
