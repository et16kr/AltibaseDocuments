# Scripts

This directory is reserved for benchmark tooling:

- question and manifest validation;
- attachments-only answer generation with leakage checks;
- source-backed judging;
- aggregate report generation;
- offline fixture checks.

Script jobs must keep model and provider settings configurable and include dry-run or
offline paths that do not require live model calls.

## Current Tooling

For normal operation, prefer the repository-root wrapper:

```bash
./run-test.sh                  # attachment full benchmark
./run-test.sh source-preserving
./run-test.sh coding-agent
```

Live command-provider runs default to `gpt-5.5`. Use
`ALTIBASE_TEST_MODEL` or `CODEX_EXEC_MODEL` only for an intentional model override.

The lower-level commands below remain useful for targeted validation and debugging.

`validate_benchmark.py` validates the durable schemas, `policy.json`,
`source_taxonomy.json`, a manifest, and all selected JSONL question records.

`answer_runner.py` generates answer records from an explicitly allowlisted Markdown
context root. It projects each question to the policy allowlist, builds retrieval
context only from the manifest-selected context glob, checks that judge-only metadata
keys do not enter the projected input, prompt scaffold, or request payload, and writes
JSONL records that validate against `schemas/answer_record.schema.json`. Alongside
`answers.jsonl` it also writes a `retrieval_audit.jsonl` sidecar (see below).

### Context selection

In `lexical` mode `answer_runner.py` does not simply rank flat Markdown chunks.
Context selection is manifest-aware and source-block-aware:

- **Source-block metadata.** Shard files wrap each copied source body in
  `<!-- SOURCE_BLOCK_BEGIN ... -->` / `<!-- SOURCE_BLOCK_END -->` comments.
  `split_markdown_chunks()` parses those comments and attaches a `BlockMeta`
  (`source_id`, `block_id`, `source_path`, `source_family`, `version_scope`,
  `language`, `authority_label`, and the shard file path) to every chunk carved from
  inside a block. The context section header for such a chunk is prefixed with
  compact provenance (`source_id=SRC-... block_id=BLOCK-... version=... lang=...`)
  so `SRC-*` / `BLOCK-*` / version tokens are literally present in the model
  context. Chunks outside any block carry no metadata and keep a plain header.
- **Query tokenization.** The lexical ranking signal is built from the `question`
  text only; `user_level`, `answer_type`, and `id` are not ranking tokens.
  Technical tokens (uppercase identifiers, `V$...` names, tokens with `_`/`$`/`.`,
  error-code patterns) are weighted higher in `score_chunk()`. A chunk whose
  `block_meta.version_scope` matches the question's `version_scope` gets a separate
  score bonus.
- **Manifest-aware routing.** `parse_source_manifest()` reads
  `GPTs/upload_package/02_source_manifest.md` and `parse_shard_manifest()` reads
  `03_source_to_shard_manifest.md`. `route_sources()` scores manifest rows against
  the question tokens and returns the top-ranked `source_id`s. Chunks whose
  propagated `block_meta.source_id` is in the routed set receive a large score bonus
  so routed-source content wins ranking. When the manifests are missing, routing
  degrades cleanly to plain lexical ranking.
- **Budgeted assembly.** `build_context()` partitions `max_context_chars`
  deterministically into priority sections: routing metadata, routed-source chunks
  (with provenance prefixes), nearby heading/wrapper context, then secondary lexical
  chunks from leftover budget. A lexical reserve keeps a routing miss degrading
  gracefully to baseline lexical retrieval. Whole-chunk greedy packing and
  deterministic section-boundary truncation guarantee the assembled context never
  exceeds the budget.

### Retrieval audit sidecar

Every run writes `retrieval_audit.jsonl` next to `answers.jsonl`, one JSON object per
question. It is observability only — derived solely from the allowlisted question
projection and the in-package manifests/context, never from judge-only fields, and it
does not influence answer generation. `run.json` records its path as
`retrieval_audit_path`. Each record contains:

- `question_id`;
- `query_tokens` — the tokens used for lexical ranking;
- `budget` — the `max_context_chars` limit;
- `routed_source_ids` — the `source_id`s `route_sources()` selected;
- `selected_chunks` — per chunk: `rel_path`, `heading`, `char_count`, `score`, and
  `block_meta` (the source-block provenance above, or `null` outside any block);
- `included_02_manifest`, `included_03_manifest`, `included_readme` — booleans for
  whether those files reached the selected context;
- `distinct_shards` — count of distinct `source_pack_shard_*.md` files used.

A non-empty `routed_source_ids` means routing used the manifest; that is not the same
as the manifest file appearing in the selected context (`included_03_manifest`), so
do not rely on the flag alone.

`judge_report.py` judges answer records against the full source-backed question record
and writes `judgments.jsonl`, `aggregate_report.json`, and `report.md`. With
`--validate-output`, it also validates the input answer records before writing judge
outputs. The rule judge scores fact coverage, critical fact coverage, required-token
preservation, version handling, Altibase-specific correctness, prohibited claims, and
missing-input handling, then applies readiness thresholds from `policy.json`.
`--retrieval-recall` adds an off-by-default post-judge diagnostic that compares each
question's selected context against judge-only `source_refs` and `required_tokens`.

### Judge behaviour

- **Semantic-tolerant fact matching.** Fact-term coverage (`term_present()` /
  `fact_match()`) is not exact-form only. A deterministic, dependency-free suffix
  stemmer plus stopword-aware stem comparison make word-form variants match
  (`restarting` ~ `restarted` ~ `restart`), a hyphenated compound matches its spaced
  form, and a small curated equivalence map covers recurring Altibase phrasings
  (`restart`/`reboot`; `reflect`/`apply`/`take effect`;
  `verify`/`check`/`validate`/`confirm`). Literal **required-token** preservation
  (`literal_token_present()`) stays exact — only fact-term coverage is form-tolerant.
- **Prohibited-claim detection.** `answer_has_negation_near()` suffix-normalizes
  terms (so a claim's `tablespaces` matches a negated `tablespace` in the answer)
  and considers every high-value claim term. `prohibited_claim_present()` handles
  order-sensitive claims ("X before Y") separately: high bag-of-words overlap flags
  only when the answer actually asserts the prohibited order un-negated. For plain
  claims it compares polarity near the claim terms, so an answer that negates a
  positive claim — or affirms the opposite of an intrinsically-negative one — is no
  longer a false positive.
- **Pass logic.** A judgment's `passed` decision is made directly against the
  `readiness_thresholds` in `policy.json`. A question passes when it has no
  `blocker` finding, `critical_fact_coverage` is at or above
  `critical_fact_coverage_minimum`, `required_token_preservation` is at or above
  `required_token_preservation_minimum`, and no prohibited claim is present. The old
  test collapsed to "zero findings", which let a single near-miss override an
  in-policy numeric score; `high`/`medium` near-miss findings now remain as
  remediation signal without auto-failing the question.

### Judge calibration

`calibrate_judge.py` measures how well the rule judge agrees with hand-labelled
ground truth. It runs the judge's `fact_match(fact_text, answer, required_tokens)`
over each entry of the gold set `fixtures/judge_gold_set.jsonl` — labelled
`(question_id, fact_id)` pairs each marked `covered` or `not_covered` — compares the
judge's `.covered` verdict against the human label, and prints and writes a confusion
matrix with precision, recall, F1, and overall agreement. It is a measurement tool:
it always exits 0 and never fails on low agreement.

```bash
python3 evals/altibase_answerability/scripts/calibrate_judge.py \
  --gold evals/altibase_answerability/fixtures/judge_gold_set.jsonl
```

It depends only on the stable `fact_match(...).covered` interface, so the judge's
internals can change without breaking calibration. The JSON report defaults to
`improvement/logs/judge_calibration_report.json`.

Fixture validation:

```bash
python3 evals/altibase_answerability/scripts/validate_benchmark.py \
  --manifest evals/altibase_answerability/manifests/fixture_seed.json \
  --profile fixture
```

Full benchmark validation:

```bash
python3 evals/altibase_answerability/scripts/validate_benchmark.py \
  --manifest evals/altibase_answerability/manifests/<full-manifest>.json
```

The full profile fails when the manifest selects fewer than 200 questions or any domain
is below the required minimum in `policy.json`. The fixture profile keeps schema,
source-path, source-language, canonical-English, and answer-projection leakage checks
enabled, but skips production count gates so small offline samples can pass.

Answer-runner self-test:

```bash
python3 evals/altibase_answerability/scripts/answer_runner.py --self-test
```

Offline fixture answer generation:

```bash
python3 evals/altibase_answerability/scripts/answer_runner.py \
  --manifest evals/altibase_answerability/manifests/fixture_seed.json \
  --mode offline_fixture \
  --limit 2 \
  --validate-output \
  --output-dir /tmp/altibase-answer-runner-fixture
```

Dry-run projection and leakage audit:

```bash
python3 evals/altibase_answerability/scripts/answer_runner.py \
  --manifest evals/altibase_answerability/manifests/fixture_seed.json \
  --mode dry_run \
  --limit 2 \
  --validate-output \
  --output-dir /tmp/altibase-answer-runner-dry-run
```

Source-preserving package dry-run:

```bash
python3 evals/altibase_answerability/scripts/answer_runner.py \
  --manifest evals/altibase_answerability/manifests/full_benchmark_source_preserving_package.json \
  --mode dry_run \
  --context-mode lexical \
  --validate-output \
  --output-dir /tmp/altibase-source-preserving-package-dry-run
```

Coding-agent source-preserving validation and dry-run:

```bash
python3 evals/altibase_answerability/scripts/validate_benchmark.py \
  --manifest evals/altibase_answerability/manifests/coding_agent_source_preserving_package.json \
  --profile coding_agent

python3 evals/altibase_answerability/scripts/answer_runner.py \
  --manifest evals/altibase_answerability/manifests/coding_agent_source_preserving_package.json \
  --mode dry_run \
  --context-mode lexical \
  --validate-output \
  --output-dir /tmp/altibase-coding-agent-source-preserving-dry-run
```

Judge/report self-test:

```bash
python3 evals/altibase_answerability/scripts/judge_report.py --self-test
```

Offline fixture judging:

```bash
python3 evals/altibase_answerability/scripts/judge_report.py \
  --manifest evals/altibase_answerability/manifests/fixture_seed.json \
  --answers evals/altibase_answerability/fixtures/judge_answers.jsonl \
  --question-id PROP-001 \
  --question-id OPS-001 \
  --validate-output \
  --output-dir /tmp/altibase-judge-report-fixture
```

Live answer generation is provider-configurable. `provider=command` reads the rendered
prompt on stdin and writes the model answer on stdout:

```bash
python3 evals/altibase_answerability/scripts/answer_runner.py \
  --manifest evals/altibase_answerability/manifests/<manifest>.json \
  --mode live \
  --provider command \
  --model local-model-name \
  --provider-command "your-model-cli --arg value"
```

`provider=openai` is also supported when the optional `openai` Python package and
`OPENAI_API_KEY` are available. Large run payloads should be written under ignored
`reports/**/runs/` directories or outside the repository.
