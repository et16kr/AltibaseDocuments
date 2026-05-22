# Altibase Answerability Benchmark

This directory contains the durable benchmark used to decide whether
`GPTs/attachments/` is sufficient as an encyclopedia-grade Altibase reference for GPT
upload.

The benchmark is not a replacement for the selected source corpus. It is an evaluation
layer: questions and expected facts are derived from the selected manuals, release
notes, patch notes, technical documents, tool manuals, third-party guides, and approved
supporting sources already present in this repository. Answer generation is then
restricted to the rebuilt attachment files so the benchmark can expose remaining
answerability gaps.

The separate coding-agent source-preserving benchmark uses the same runner and judge
contracts but targets `GPTs/upload_package/` and practical agent
artifacts. It is not part of the locked 270-question full answerability baseline.

## Scope

- Supported Altibase versions: `7.1`, `7.3`, and `8.1`.
- Source boundary: repository-local selected sources only, as inventoried in
  `GPTs/reports/source_inventory.md`.
- Answer source boundary: `GPTs/attachments/*.md`, an allowlisted projection of each
  question record, and optional GPT instruction draft material only when a manifest
  explicitly selects it.
- Comparison language: canonical English.
- Default answering language: English, with technical tokens preserved literally.

Korean Altibase manuals are authoritative when paired Korean and English manuals differ.
Question expected facts, canonical reference answers, scoring notes, and reports must be
written in English by translating and normalizing Korean-source facts, not by storing
Korean prose as the expected answer. Korean section titles may appear in source
locators when needed for review.

## Durable Layout

```text
evals/altibase_answerability/
  README.md
  SCORING.md
  policy.json
  SOURCE_COVERAGE_MAP.md
  source_taxonomy.json
  schemas/
  questions/
  manifests/
  scripts/
  reports/
  fixtures/
```

- `schemas/`: JSON schemas for benchmark policy, question records, manifest records,
  answer records, judgments, aggregate reports, and the source taxonomy.
- `source_taxonomy.json`: machine-readable source-family, domain, user-level, version,
  and target-count map for question-generation jobs.
- `SOURCE_COVERAGE_MAP.md`: human-readable summary of the source taxonomy and domain
  coverage plan.
- `questions/`: source-backed JSONL question sets. Later jobs should create one file per
  required domain.
- `manifests/`: run manifests that select question files, configure run metadata, and
  optionally enable multilingual or GPT-instruction tests.
- `scripts/`: validation, answer-runner, judge, and report scripts. Scripts must support
  offline or dry-run checks where practical.
- `reports/`: generated aggregate reports and reviewable run summaries. Large transient
  run payloads should stay out of version control.
- `fixtures/`: small calibration samples that can run without the full benchmark or live
  model calls.

The coding-agent extension adds
`questions/coding_agent_source_preserving.jsonl`,
`manifests/coding_agent_source_preserving_package.json`, and
`reports/coding_agent_source_preserving_rubric.md`. Validate it with
`--profile coding_agent` so the small agent-task set stays distinct from the full
readiness count gates.

The `.codex-jobs/altibase-gpt-answerability-benchmark/` directory is only orchestration
state. Durable benchmark implementation belongs here.

## Domain Requirements

The validator must fail if the benchmark has fewer than 200 total questions or if any
domain is below its required minimum.

| Domain ID | Required minimum | Target | Owned by |
| --- | ---: | ---: | --- |
| `properties` | 40 | 50 | J004 |
| `sql_ddl_dml_datatypes` | 35 | 45 | J005 |
| `operations_admin` | 25 | 35 | J006 |
| `views_performance_monitoring` | 20 | 30 | J007 |
| `replication_cdc_security_network` | 20 | 30 | J008 |
| `errors_troubleshooting` | 20 | 30 | J009 |
| `tools_apis_connectors_migration` | 40 | 50 | J010 |

Question generation should target about 270 questions so later pruning still leaves more
than 200 usable items.

J004-J010 should use `source_taxonomy.json` and `SOURCE_COVERAGE_MAP.md` as the planning
map for source families, subdomain targets, user-level mix, version-scope mix, answer
type mix, retrieval-risk mix, and exclusions. The taxonomy is planning and judge-side
material; it must not be provided to the answering model.

## Question Records

Question records are judge-owned data. Each record must be source-backed and include:

- stable `id`;
- `domain`, `subdomain`, `user_level`, `version_scope`, `question`, and
  `answer_language`;
- `source_language_basis`, preferring `ko` or `ko+en` where Korean manuals exist for the
  same product area and version;
- `source_refs` with enough manual/source, version, section, and locator detail for a
  reviewer to verify the fact;
- `expected_facts` in English;
- `required_tokens` that must remain literal;
- `prohibited_claims` for common unsupported or unsafe assumptions;
- `answer_type`, `difficulty`, and `retrieval_risk`;
- optional `canonical_reference_answer`, used only by the judge and human calibration.

Do not create questions whose expected answer is absent from the selected source corpus.
It is acceptable for the current attachments to miss the answer before remediation.

## Answer Runner Contract

The answer runner evaluates the attachments, not the original manuals. It may send only
these question fields to the answering model:

- `id`
- `question`
- `version_scope`
- `user_level`
- `answer_type`
- `answer_language`, defaulting to `en`
- `requested_language`, only when a manifest explicitly enables multilingual testing

All other question fields are judge-only. Runner code must record the exact projected
answering input for audit and must fail a leakage check if judge-only keys appear in the
prompt text or request payload.

The durable runner is `scripts/answer_runner.py`. It supports:

- `dry_run` mode for projection, context construction, output-schema validation, and
  leakage checks without answer generation;
- `offline_fixture` mode for deterministic fixture answers without live model calls;
- `live` mode through a configurable provider, including stdin/stdout command providers
  and optional OpenAI client support.

By default the runner requests English answers, preserves literal technical tokens, and
uses bounded lexical chunk selection from the manifest-selected context root. Lexical
selection is manifest-aware and source-block-aware: it parses the package source
manifests (`02_source_manifest.md`, `03_source_to_shard_manifest.md`) to route each
question to the documented source blocks, propagates per-chunk source-block metadata
(`source_id`, `block_id`, version, language) into the context headers, and partitions
`max_context_chars` into priority sections so routed-source content leads the context
without crowding out secondary lexical chunks. When a question names a specific
property, error code, or `V$`/`X$`/`SYS_` view, the runner also admits that
identifier's own documented definition block into a dedicated highest-priority
section, so a generic-titled routing miss cannot starve it, and a final exact-block
deduplication pass reinvests budget otherwise spent on byte-identical chunks. Use
`--context-mode full` only when the selected model can safely accept the whole
attachment set. See `scripts/README.md` for the context-selection details.

Each run also writes a `retrieval_audit.jsonl` sidecar next to `answers.jsonl`. The
audit records, per question, the ranking tokens, the routed source ids, and the
selected chunks with their source-block provenance. It is observability only — derived
from the allowlisted projection and in-package context, never from judge-only fields —
and does not affect answer generation. See `scripts/README.md` for the field list.

## Judge Contract

The judge may use the complete question record, expected facts, required tokens,
prohibited claims, source references, optional canonical reference answer, and scoring
notes. It compares attachments-only answers against the canonical-English expected facts
derived from Korean-first sources.

The durable rule judge and report generator is `scripts/judge_report.py`. It consumes
answer records produced by the attachments-only runner, uses only judge-side question
metadata for evaluation, writes per-question judgments, and emits JSON plus Markdown
aggregate reports. It supports an offline self-test and fixture calibration answers, so
judge/report validation does not require live model calls.

Fact coverage is semantic-tolerant: a deterministic suffix stemmer and a small curated
equivalence map let correct paraphrases and word-form variants count as covered, while
literal required-token preservation stays exact. Prohibited-claim detection is
polarity-, direction-, and markdown-emphasis-aware, so a correct, safe answer is not
flagged merely for sharing vocabulary with a prohibited claim. A question's `passed`
decision is made directly against the `readiness_thresholds` in `policy.json` — no
`blocker` finding, critical fact coverage and required-token preservation at or above
their policy minimums, and no prohibited claim — and near-miss `high`/`medium`
findings remain as remediation signal without auto-failing an otherwise in-policy
answer.

`judge_report.py` also carries an optional LLM-assisted fact judge
(`--llm-fact-judge`, or the `JUDGE_LLM_FACT=1` environment toggle), off by default.
When enabled it adjudicates only paraphrase-suspect facts — those whose rule-judge
term score cannot distinguish a correct paraphrase from a near-miss — by majority vote
over a configurable provider, caches verdicts, and falls back to the deterministic
rule verdict on any provider failure or tie. With it off, judging is byte-for-byte the
rule judge. See `scripts/README.md` for the band, caching, and fallback details.

`scripts/calibrate_judge.py` measures judge-vs-human agreement against the labelled
gold set `fixtures/judge_gold_set.jsonl`, reporting a confusion matrix with precision,
recall, and overall agreement. It is a measurement tool and never fails a run, and it
accepts the same `--llm-fact-judge` flag to measure agreement with the LLM-assisted
judge enabled.

Judgments must score at least:

- required fact coverage;
- required token preservation;
- version handling and assumptions;
- Altibase-specific correctness;
- unsupported or hallucinated claims;
- whether missing environment, log, patch-level, or object-definition details were
  requested only when needed.

## Readiness Thresholds

Initial upload readiness thresholds are defined in `policy.json` and explained in
`SCORING.md`:

- overall pass rate at least 85%;
- no domain below 80%;
- critical fact coverage at least 90%;
- required technical token preservation at least 95%;
- unsupported-claim rate no more than 2%;
- no blocker findings for backup/recovery, destructive SQL, security/TLS, replication
  state changes, or version-sensitive property changes.

## Maintenance Rules

- Keep question records, expected facts, canonical reference answers, scoring notes, and
  reports in English.
- Keep SQL keywords, object names, property names, error codes, command options, view
  names, API names, connector names, paths, and version labels literal.
- Treat version-sensitive Altibase behavior as source-backed. Do not replace Altibase
  rules with generic Oracle or generic database assumptions.
- If a question depends on an exact patch level, customer environment, log excerpt, or
  object definition, expected facts should require the answer to ask for that missing
  input and provide the safest source-backed next check.
- Do not let original manuals, source inventory files, source references, expected facts,
  required tokens, prohibited claims, canonical reference answers, source-language basis,
  difficulty, or retrieval-risk metadata enter answer-generation prompts.

## Validation

Use `run-test.sh` from the repository root for the common test routes:

```bash
# Original attachment-based 270-question benchmark.
./run-test.sh

# Source-preserving package 270-question benchmark.
./run-test.sh source-preserving

# Source-preserving coding-agent benchmark.
./run-test.sh coding-agent
```

For mechanical smoke checks without live model calls, set `MODE=dry_run`. Live
Codex command-provider runs default to `gpt-5.5`; override
`ALTIBASE_TEST_MODEL` or `CODEX_EXEC_MODEL` only when intentionally comparing another
model:

```bash
MODE=dry_run ./run-test.sh coding-agent

./run-test.sh source-preserving

ALTIBASE_TEST_MODEL=gpt-5.5 \
./run-test.sh source-preserving
```

Use the validator before committing benchmark artifact changes:

```bash
python3 evals/altibase_answerability/scripts/validate_benchmark.py \
  --manifest evals/altibase_answerability/manifests/fixture_seed.json \
  --profile fixture
```

For production manifests, omit `--profile fixture`. The default full profile fails when
the selected question set has fewer than 200 total records or any domain is below its
required minimum in `policy.json`.

Use the runner fixture checks after editing answer-generation code:

```bash
python3 evals/altibase_answerability/scripts/answer_runner.py --self-test

python3 evals/altibase_answerability/scripts/answer_runner.py \
  --manifest evals/altibase_answerability/manifests/fixture_seed.json \
  --mode offline_fixture \
  --limit 2 \
  --validate-output \
  --output-dir /tmp/altibase-answer-runner-fixture
```

Use the judge/report fixture checks after editing scoring or reporting code:

```bash
python3 evals/altibase_answerability/scripts/judge_report.py --self-test

python3 evals/altibase_answerability/scripts/judge_report.py \
  --manifest evals/altibase_answerability/manifests/fixture_seed.json \
  --answers evals/altibase_answerability/fixtures/judge_answers.jsonl \
  --question-id PROP-001 \
  --question-id OPS-001 \
  --validate-output \
  --output-dir /tmp/altibase-judge-report-fixture
```
