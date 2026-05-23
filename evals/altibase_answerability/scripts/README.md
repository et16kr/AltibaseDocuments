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
  deterministically into priority sections: routing metadata; the named-definition
  section (below); routed-source chunks (with provenance prefixes); nearby
  heading/wrapper context; then secondary lexical chunks from leftover budget. A
  lexical reserve keeps a routing miss degrading gracefully to baseline lexical
  retrieval. Whole-chunk greedy packing and deterministic section-boundary
  truncation guarantee the assembled context never exceeds the budget.
- **Named-definition admission.** Every per-version manual row in the source
  manifest carries the same generic title, so `route_sources()` cannot single out
  the manual that documents a specific property, error code, view, or
  replication clause, and a generic-titled mis-route can flood the saturated
  budget with the wrong manual. To stay resilient, `build_context()` admits the
  chunks the question's own named identifier points at into a dedicated
  highest-priority section, regardless of the routing decision:
  - a **property-definition section** (`build_definition_section`) for
    `properties` questions — the General Reference-1 block whose heading is a
    property identifier from the question text, plus the `V$PROPERTY`
    data-dictionary companion;
  - an **error-reference / dictionary-view section** for `errors_troubleshooting`
    and `views_performance_monitoring` questions — the Error Message Reference
    entry for a named error symbol, hex code, or `ERR-<hex>` runtime code
    (`build_error_reference_section`), and the full General Reference-2 section of
    a named `V$`/`X$`/`SYS_..._` identifier (`build_dict_view_section`);
  - a **replication clause / option section** for
    `replication_cdc_security_network` questions
    (`build_replication_section`) — the Replication Manual section that the
    named DDL clause, replication command, or option block points at
    (`CREATE/ALTER/DROP REPLICATION`, `START`/`STOP`/`RESET`/`FLUSH`,
    `ADD`/`DROP HOST`, Gapless / Parallel Applier / Meta Logging / Offline /
    `REPLICATION MODE` …), version-filtered, plus the replication monitoring
    views (`V$REPSENDER` / `V$REPRECEIVER` / `V$REPSYNC` / …) from the General
    Reference-2 data-dictionary manual as the documented companion (the
    analogue of the `V$PROPERTY` companion for properties).
  Each builder is anchored on identifiers in the question text and confined to the
  relevant `source_family`, so it returns nothing — and `build_context()` is
  byte-identical to before — for a question that names no such identifier or
  replication clause. `route_sources()` itself is unchanged; the fix makes
  assembly resilient to the unavoidable routing miss.
- **Prose → identifier resolution.** A residual band of questions names the
  object only descriptively rather than by its identifier ("session time zone"
  vs `TIME_ZONE`, "conversion not applicable" vs
  `mtERR_ABORT_CONVERSION_NOT_APPLICABLE`, "wait-event investigation" vs
  `V$SESSION_WAIT`). The identifier-anchored builders above then never fire and
  the question falls back to plain lexical retrieval, which is insufficient
  under the saturated 180k budget against a generic-titled mis-route.
  `resolve_prose_identifiers()` closes that gap with a deterministic,
  conservative, high-precision phrase → identifier map: each lower-cased anchor
  phrase was verified to occur in exactly one residual question (and in no
  other benchmark question), and to point at a property / error / view with a
  documented section in `GPTs/upload_package/`. The resolved identifiers are
  unioned into the sets `build_definition_section`,
  `build_error_reference_section`, and `build_dict_view_section` already
  extract literally, so a resolved phrase reaches exactly the same admission
  path — and the resolver returns three empty sets, leaving `build_context()`
  byte-identical, for every question whose object is named by its identifier or
  whose prose is too ambiguous to resolve safely. Only the question text is
  read; no judge-only field is consulted.
- **Exact-block deduplication.** After the budgeted fill passes, `build_context()`
  drops any chunk whose body byte-identically repeats an already-selected chunk
  and reinvests the freed budget — duplicate-aware and add-only — in unique
  content. The source-preserving package re-serialises many blocks verbatim across
  the 7.1/7.3/8.1 version trees and shared shard boilerplate, so on a saturated
  budget this recovers context space without losing any token. The pass removes
  only proven duplicates and only adds, so the assembled context is a
  token-superset of the pre-dedup context.

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
It reconstructs each question's context manifest-aware — parsing the in-package
`02_source_manifest.md` and `03_source_to_shard_manifest.md` exactly as
`answer_runner.main()` does — so the rebuild matches a routed run's recorded audit
instead of a pre-routing lexical context; when those manifests are absent it warns
and degrades to a plain pre-routing lexical rebuild. It writes
`retrieval_recall.json` reporting required-token and source-ref recall.

### Judge behaviour

- **Semantic-tolerant fact matching.** Fact-term coverage (`term_present()` /
  `fact_match()`) is not exact-form only. A deterministic, dependency-free suffix
  stemmer plus stopword-aware stem comparison make word-form variants match
  (`restarting` ~ `restarted` ~ `restart`), a hyphenated compound matches its spaced
  form, and a small curated equivalence map covers recurring Altibase phrasings
  (`restart`/`reboot`; `reflect`/`apply`/`take effect`;
  `verify`/`check`/`validate`/`confirm`). Literal **required-token** preservation
  (`literal_token_present()`) stays exact — only fact-term coverage is form-tolerant.
- **Prohibited-claim detection (round 2).** `prohibited_claim_present()` is
  polarity-, direction-, markdown-emphasis-, and quoted-span-aware. Before any
  negation or ordering analysis the answer passes through
  `strip_markdown_emphasis()`, so an emphasised negation (`does **not** commit`)
  still tokenises as `not` while identifier underscores (`SSL_PORT_NO`) survive.
  The negation read for an intrinsically-negative ("cannot") claim is then
  taken on the answer's own prose: `mask_quoted_span_negations()` blanks
  negation tokens (`cannot` / `cant` / `never` / `not` / `no` / `without` /
  `unsupported`) that sit inside fenced triple-backtick code blocks, inline
  backtick spans, or single- / double- / curly-quoted string literals, so a
  `does not` inside a CLI example like `` `altierr -w "does not"` `` — which is
  example text, not the answer's polarity — cannot flip the verdict. Only the
  negation tokens inside such spans are blanked (replaced by equal-length
  spaces); the surrounding prose and every claim / technical term, including
  ones that sit inside the same span, is left byte-for-byte intact so it still
  counts toward sentence coverage. `parse_order_claim()` separates ordering
  claims ("X before Y") from asymmetric-relation claims ("A overrides B",
  "A replaces / supersedes / precedes B", "A takes precedence over B"): the same
  words in the other direction are an allowed answer, so such a claim flags only
  when high bag-of-words overlap is paired with the answer actually asserting the
  prohibited direction un-negated. For a plain claim it compares polarity near the
  claim terms, so an answer that negates a positive claim — or affirms the opposite
  of an intrinsically-negative one — is no longer a false positive.
- **Pass logic.** A judgment's `passed` decision is made directly against the
  `readiness_thresholds` in `policy.json`. A question passes when it has no
  `blocker` finding, `critical_fact_coverage` is at or above
  `critical_fact_coverage_minimum`, `required_token_preservation` is at or above
  `required_token_preservation_minimum`, and no prohibited claim is present. The old
  test collapsed to "zero findings", which let a single near-miss override an
  in-policy numeric score; `high`/`medium` near-miss findings now remain as
  remediation signal without auto-failing the question.

### Multi-sample answer mode

`answer_runner.py` can generate N answer records per question to expose live
answer-generation variance. The count is resolved by `resolve_answer_samples()`
with the precedence: an explicit `--samples` CLI flag, then the
`ANSWER_SAMPLES` environment variable, then the default of 1. Because
`run-test.sh` invokes the runner with a fixed argument list and never passes
`--samples`, `ANSWER_SAMPLES` is the only path a live benchmark run can enable
multi-sampling — exactly like `JUDGE_LLM_FACT` for the judge. The value must be
a positive integer.

For each question, retrieval, `build_context()` assembly, prompt construction,
and the leakage check are computed once and shared across that question's N
samples; only answer generation repeats. The runner writes N answer records per
question to `answers.jsonl`, each tagged with a 0-based `sample_index`, and
keeps the `retrieval_audit.jsonl` sidecar one record per question regardless of
N. `sample_index` is multi-sample bookkeeping rather than part of the canonical
answer-record schema, so the validator drops it before schema-checking the
record structure.

`ANSWER_SAMPLES=1` (the default) keeps every artifact byte-for-byte identical
to a pre-multi-sample run: the loop runs once, `sample_index` is omitted from
the record, and `answers.jsonl` / `aggregate_report.json` / `report.md` read
exactly as before. `answer_runner.py --self-test` exercises both paths — the
flag/env resolution and `sample_index` tagging — so the N=1 byte-identity and
the N>1 plumbing are both verified hermetically without a provider.

### Scorecard variance band

When the judge consumes a multi-sample `answers.jsonl`, `compute_variance_band()`
summarises each scorecard metric (`pass_rate`, `fact_coverage`,
`critical_fact_coverage`, `required_token_preservation`,
`unsupported_claim_rate`, `version_handling`, `altibase_specific_correctness`,
`missing_input_handling`) as the mean across the N samples together with the
per-sample min and max, so a genuine retrieval / answer gain can be read
against the live answer-generation noise floor. Every sample must answer every
selected question; the judge errors out otherwise so per-sample metrics share
the same question set.

The result is added as an optional `variance_band` field to
`aggregate_report.json` and as a "Sample Variance Band" Markdown section in
`report.md`. A single-sample run leaves `variance_band` off and emits no
Markdown section, so `aggregate_report.json` still validates against the
unmodified `aggregate_report.schema.json` and `report.md` is byte-for-byte the
pre-band layout. The `Overall Metrics` table continues to show the
single-number metrics (the per-sample mean for a multi-sample run); the band
is purely additive.

### Optional LLM-assisted fact judge

`judge_report.py` carries an optional LLM-assisted fact judge, **off by default**.
`--llm-fact-judge` (or the `JUDGE_LLM_FACT=1` environment toggle) enables it; with
neither set, judging is byte-for-byte the deterministic rule judge, which stays the
default and the fallback.

- **Paraphrase-suspect band only.** The LLM is consulted only for facts whose
  rule-judge `term_score` lands in the paraphrase-suspect band (`0.40`–`1.00`) —
  the band where bag-of-words coverage cannot tell a correct paraphrase from a
  near-miss. A fact matched by exact normalized fact-text containment, or one the
  rule judge clearly missed, keeps the rule verdict untouched. Only
  `FactMatch.covered` may be overridden; `term_score`, `technical_score`, and
  literal required-token preservation stay the rule judge's deterministic values.
- **Majority vote.** Each in-band fact is graded by a majority vote over several
  independent provider calls (`JUDGE_LLM_FACT_VOTES`, default 3), since the
  provider is non-deterministic per call; a tie keeps the rule verdict.
- **Cached verdicts.** Majority verdicts are cached, keyed by prompt version, fact,
  and answer, so warm-cache re-runs are free and stable. The default cache is
  `improvement2/cache/llm_fact_judge_cache.json`.
- **Rule-judge fallback.** On any provider error, timeout, missing provider,
  unparseable reply, or vote tie the judge falls back to the deterministic rule
  verdict and records the fallback. Consecutive provider failures trip a circuit
  breaker that stops shelling out for the rest of the run, so a broken or missing
  provider never hangs or fails a run.
- **Configuration.** `--llm-fact-judge-command`, `--llm-fact-judge-cache`, and
  `--llm-fact-judge-timeout` (env `JUDGE_LLM_FACT_COMMAND`, `JUDGE_LLM_FACT_CACHE`,
  `JUDGE_LLM_FACT_TIMEOUT`) override the provider command, cache path, and per-call
  timeout; each falls back to a built-in default (the same Codex command provider
  `answer_runner.py` uses). `--self-test` never builds the LLM judge, so the
  self-test stays hermetic even with `JUDGE_LLM_FACT=1` set.

### Judge calibration

`calibrate_judge.py` measures how well the rule judge agrees with hand-labelled
ground truth. It runs the judge's `fact_match(fact_text, answer, required_tokens)`
over each entry of the gold set `fixtures/judge_gold_set.jsonl` — labelled
`(question_id, fact_id)` pairs each marked `covered` or `not_covered`, expanded in
cycle 3 to roughly 150 entries balanced across the benchmark's seven domains so
agreement is measured on a representative slice — compares the judge's
`.covered` verdict against the human label, and prints and writes a confusion
matrix with precision, recall, F1, and overall agreement. It is a measurement tool:
it always exits 0 and never fails on low agreement. With `--llm-fact-judge` (or
`JUDGE_LLM_FACT=1`) it routes each gold entry through `judge_fact(...)` instead, so
agreement can be measured with the LLM-assisted judge enabled; with the flag off it
uses `fact_match` exactly as before.

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
