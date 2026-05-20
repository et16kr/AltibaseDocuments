# Source-Preserving Answerability Improvement Plan

- Date: 2026-05-20
- Repository: `/home/et16/AltibaseDocuments`
- Scope: `GPTs/upload_package/` package-only answer generation
- Latest full run: `altibase_source_preserving_20260520_090243`
- Latest coding-agent run: `altibase_coding_agent_20260520_104452`

## Objective

Improve the package-only source-preserving benchmark without relaxing the source
boundary. Answer generation must use only Markdown files matched by
`GPTs/upload_package/*.md`. External reports, attachments, source-pack baselines,
manual trees, release notes, and technical document trees must not be added to
the answer-generation prompt.

The judge may still use benchmark questions, policy metadata, expected facts,
and scoring rules because those are evaluation inputs, not answer context.

## Current Evidence

The latest package-only runs executed successfully:

| Suite | Run | Model | Context | Runner | Result |
| --- | --- | --- | --- | --- | --- |
| full benchmark | `altibase_source_preserving_20260520_090243` | `gpt-5.5` | `GPTs/upload_package/*.md` | ok | 14/270 passed |
| coding-agent | `altibase_coding_agent_20260520_104452` | `gpt-5.5` | `GPTs/upload_package/*.md` | ok | 0/10 passed |

Full benchmark metrics:

| Metric | Latest Value | Threshold |
| --- | ---: | ---: |
| Pass rate | 5.2% | 85.0% |
| Critical fact coverage | 49.8% | 90.0% |
| Required token preservation | 56.4% | 95.0% |
| Unsupported-claim rate | 0.7% | <= 2.0% |
| Protected-topic blockers | 104 | 0 target |

Coding-agent metrics:

| Metric | Latest Value | Threshold |
| --- | ---: | ---: |
| Pass rate | 0.0% | 85.0% |
| Critical fact coverage | 55.0% | 90.0% |
| Required token preservation | 65.4% | 95.0% |
| Unsupported-claim rate | 0.0% | <= 2.0% |
| Protected-topic blockers | 5 | 0 target |

The failure pattern is not a runner failure. The answer runner wrote all answer
records with `errors=0`. The failure is retrieval and synthesis quality under a
large source-shard package.

## Diagnosis

The current lexical context builder treats the 20-file upload package as flat
Markdown chunks. This works poorly for source-preserving shards because exact
answers often require a lookup sequence:

1. Find candidate source metadata in `02_source_manifest.md`.
2. Map candidate `source_id` and `block_id` values through
   `03_source_to_shard_manifest.md`.
3. Retrieve relevant source-internal chunks from the mapped shard while
   preserving the enclosing `SOURCE_BLOCK_BEGIN` metadata.

The current runner does not perform that sequence. It ranks chunks by question
tokens only, so large shards can crowd out exact source evidence and required
tokens.

Coding-agent failures show the same issue more directly: answers often miss
literal provenance tokens such as `SRC-*`, `BLOCK-*`, and shard paths.

Two important limits shape the remediation:

- `source_refs`, `required_tokens`, expected facts, and canonical answers are
  judge-only metadata. Answer generation must not use those fields to select
  context, even though they identify the ideal source after judging.
- A `SOURCE_BLOCK_BEGIN` / `SOURCE_BLOCK_END` body is usually a whole manual or
  large support source, not a small section. Including entire source blocks is
  often impossible within `max_context_chars`. The retrieval fix must propagate
  source metadata to smaller chunks and rank source-internal sections, not
  blindly include whole source blocks.

## Non-Negotiable Constraints

- Keep answer-generation context restricted to `GPTs/upload_package/*.md`.
- Do not re-enable `gpt_instruction_draft_path` from `GPTs/reports/`.
- Do not use `GPTs/attachments/` as an answer-generation fallback for these
  package-only benchmarks.
- Do not use judge-only fields such as `source_refs`, `required_tokens`,
  `expected_facts`, `canonical_reference_answer`, or prohibited-claim metadata
  for answer-generation retrieval or prompt construction.
- Do not edit source bodies inside `SOURCE_BLOCK_BEGIN` /
  `SOURCE_BLOCK_END` blocks unless a separate source-preservation validation
  plan explicitly authorizes and verifies the byte change.
- Keep live runs comparable: `provider=command`, `model=gpt-5.5`,
  `context=lexical` unless a run is explicitly labeled as an experiment.

## Expected Impact And Confidence

This work is likely to improve the benchmark, but it is not expected to make the
package readiness pass in one cycle.

The Claude plan review was checked against the run artifacts and judge code.
Its central correction is accepted: the current benchmark has two failure
engines, not one. Retrieval is the largest practical lever, but the rule judge
is also a structural pass-rate gate because it scores expected facts by lexical
word overlap and turns any missed critical fact or required token into a
failing severity.

High-confidence improvements:

- Coding-agent provenance token preservation should improve once selected
  context includes `source_id`, `block_id`, shard path, `source_path`,
  `version_scope`, and `authority_label` prefixes.
- Required-token preservation should improve for questions whose allowed prompt
  text contains distinctive technical tokens such as SQL keywords, property
  names, error codes, view names, command names, driver classes, URLs, or API
  calls.
- Retrieval audit output should make remaining failures actionable instead of
  opaque.

Medium-confidence improvements:

- Critical fact coverage should improve when the question text can route to the
  correct source family, manual title, version, language, heading, or technical
  token.
- Protected-topic blocker counts should improve as a derived result of better
  coverage and token preservation. They should not be treated as an independent
  safety-defect count unless the finding category is an actual prohibited claim
  or unsafe missing-input failure.

Low-confidence or longer-term improvements:

- Questions with broad conceptual wording and few distinctive source terms may
  still route poorly without additional package-local indexes or curated
  aliases.
- The full benchmark is unlikely to approach the 85% readiness threshold until
  both retrieval recall and judge validity are proven. Retrieval work alone can
  raise token preservation and fact coverage but may not unlock pass rate.
- Model synthesis can still omit facts even when retrieval succeeds, and the
  rule judge can still miss semantically correct paraphrases. These must be
  diagnosed separately from retrieval failure.
- The 172 missed critical facts with `term_score` in the 0.40-0.62 band are
  paraphrase candidates, not automatically proven judge false negatives. They
  need sampled calibration before changing scoring thresholds broadly.

## Job Distribution Review

Verdict: the job split is appropriate after keeping targeted calibration
separate from the full re-run. The work should be divided by dependency and
failure mode, not by equal-sized effort.

Appropriate boundaries:

- J001 is a prerequisite diagnostic job. It should land first because it makes
  later failures attributable to retrieval, prompt synthesis, or judging.
- J002 and J003 are tightly coupled but still useful as separate work units:
  J002 owns package parsing and metadata propagation, while J003 owns scoring
  and context assembly. They should share a small explicit interface.
- J004 depends on J002/J003. It should not be treated as a standalone prompt
  fix because provenance tokens cannot be preserved if retrieval never selects
  them.
- J005 should be a judge-validity and protected-topic calibration job, not a
  prompt-safety job. The latest `OPS-111` and `TOOL-038` prohibited-claim
  findings are better explained as judge false positives after checking the
  answer text and `prohibited_claim_present` logic.
- J006 is a targeted calibration gate, not a full benchmark. It should block
  J007 unless it shows measurable retrieval improvement, judge-validity
  regressions are controlled, or audit evidence proves the next failure is no
  longer retrieval.
- J007 is only the final measurement job. It should not be used for iterative
  tuning.

Distribution risks:

- Splitting J002 and J003 across disconnected implementations would be risky.
  The parser output contract must be agreed before context-scoring changes.
- Running J004 before J003 would likely create prompt-only churn with little
  benchmark effect.
- Running J005 as prompt scaffolding would spend effort changing already safe
  answers to satisfy false-positive prohibited-claim findings.
- Running the full benchmark before J006 would spend a live 270-question run
  without evidence that retrieval and judge validity have improved.

Improvement judgment: this plan should improve retrieval observability and is
likely to improve token preservation. It is not guaranteed to improve pass rate
substantially unless J002/J003 raise source-block recall and J005 removes or
calibrates known judge false positives. The plan therefore includes J006 as a
stop/go gate before the full run.

## Improvement Jobs

### J001 - Retrieval Audit Instrumentation

Goal: make each answer record explain which package chunks were selected and why.

Implementation targets:

- `evals/altibase_answerability/scripts/answer_runner.py`
- Answer record usage or audit metadata fields, if schema permits; otherwise a
  separate per-run retrieval audit JSONL under the run answers directory.

Required behavior:

- Record selected chunk headings, file paths, character counts, lexical scores,
  and query tokens for each question.
- Record whether selected chunks include `02_source_manifest.md`,
  `03_source_to_shard_manifest.md`, and any `source_pack_shard_*.md`.
- Write a pre-provider retrieval audit that uses only allowlisted question input
  and selected package context.
- Write an optional post-judge retrieval recall report after judging. This
  report may compare selected context against judge-only `source_refs` and
  `required_tokens` because it is diagnostic output after the provider call, not
  answer-generation input.
- Preserve the existing answer record schema or update the schema with
  validation.

Acceptance checks:

```bash
MODE=dry_run LIMIT=3 RUN_ROOT=/tmp/altibase-retrieval-audit-smoke ./run-test.sh source-preserving
python3 evals/altibase_answerability/scripts/validate_benchmark.py \
  --manifest evals/altibase_answerability/manifests/full_benchmark_source_preserving_package.json \
  --profile full
git diff --check
```

Expected outcome:

- For failed questions, reviewers can tell whether the right package source,
  shard, chunk, and required tokens were absent from selected context, present
  but ignored by the model, or present without answer-side preservation.

### J002 - Package Manifest And Shard Index Parser

Goal: add structured package parsing that can attach provenance metadata to
smaller retrieval chunks without using judge-only question metadata.

Implementation targets:

- New helper module or functions in
  `evals/altibase_answerability/scripts/answer_runner.py`
- Optional fixture tests in the benchmark scripts test path if available.

Required behavior:

- Parse `02_source_manifest.md` into source records keyed by `source_id`.
- Parse `03_source_to_shard_manifest.md` into mapping records keyed by
  `source_id` and `block_id`.
- Parse shard wrappers enough to identify each source block's metadata and the
  byte or character range of its body without modifying source bodies.
- Split source block bodies into smaller retrieval chunks while retaining the
  parent `source_id`, `block_id`, `source_path`, `source_family`,
  `version_scope`, `language`, `authority_label`, and shard path.
- Provide deterministic lookup APIs for:
  - manifest rows by source metadata;
  - shard mappings by source metadata;
  - chunk metadata by shard and source block;
  - package-only file path normalization from preserved `GPTs/source_pack/...`
    TSV paths to the matching `GPTs/upload_package/source_pack_shard_*.md`
    context file.
- Do not expose or depend on judge-only `source_refs` from question records.

Acceptance checks:

```bash
python3 evals/altibase_answerability/scripts/answer_runner.py --self-test
MODE=dry_run LIMIT=3 RUN_ROOT=/tmp/altibase-package-index-smoke ./run-test.sh source-preserving
python3 GPTs/reports/scripts/validate_source_preserving_upload_package.py --strict-final
git diff --check
```

Expected outcome:

- The runner can rank source-internal chunks while preserving machine-readable
  provenance in the selected context. It should not need to include a whole
  manual-sized source block to preserve `SRC-*`, `BLOCK-*`, shard path, version,
  and authority metadata.

### J003 - Source-Block-Aware Context Builder

Goal: improve context selection while staying inside `GPTs/upload_package` and
without using judge-only metadata.

Implementation targets:

- `build_context`, `tokenize_query`, and chunk selection logic in
  `evals/altibase_answerability/scripts/answer_runner.py`.

Required behavior:

- Build query signals only from allowlisted question input:
  `id`, `question`, `version_scope`, `user_level`, `answer_type`,
  `answer_language`, and `requested_language`.
- Add a package-router stage that scores source manifest rows using question
  text, version scope, source family, title, source path tokens, language,
  authority label, SQL/property/error/view/command/API tokens, and domain-like
  terms inferred from the question text.
- Prefer source-internal chunks whose propagated metadata and body text match
  the query. Do not select a source solely because judge-only `source_refs`
  would identify it.
- Prefix selected source-internal chunks with compact package provenance:
  `source_id`, `block_id`, shard path, `source_path`, `version_scope`,
  `language`, and `authority_label`.
- Include the in-package README and manifest guidance only when they fit the
  budget and improve lookup. They must not crowd out source-internal chunks.
- Reserve context budget for:
  1. concise routing metadata;
  2. source-internal chunks with provenance prefixes;
  3. nearby heading or wrapper metadata;
  4. secondary lexical chunks only after exact block candidates.
- Preserve `max_context_chars` behavior and deterministic ordering.
- Do not include whole manual-sized source blocks unless the block already fits
  the budget and is the best available unit.

Acceptance checks:

```bash
MODE=dry_run LIMIT=10 RUN_ROOT=/tmp/altibase-source-block-context-smoke ./run-test.sh source-preserving
RUN_ID=source_block_context_limit1 RUN_ROOT=/tmp/altibase-source-block-context-limit1 LIMIT=1 ./run-test.sh source-preserving
git diff --check
```

Expected outcome:

- Required technical tokens and provenance tokens are present in context more
  often before model synthesis begins. The expected first-cycle improvement is
  higher token preservation and critical fact coverage, not immediate readiness.

### J004 - Coding-Agent Provenance Guardrail

Goal: make coding-agent answers preserve package provenance tokens.

Implementation targets:

- Prompt scaffold in `answer_runner.py`
- Possibly coding-agent manifest wording if prompt-scaffold changes require
  suite-specific instructions.

Required behavior:

- For `coding_agent` profile questions, instruct the model to preserve and
  return relevant `SRC-*`, `BLOCK-*`, and shard path tokens when present in
  context.
- Keep this instruction inside the runner scaffold, not an external report
  draft.
- Add answer-side checks or audit metadata showing whether required provenance
  tokens were present in selected context before judging.
- If provenance tokens are absent from selected context, record that as a
  retrieval failure rather than treating it as only a model synthesis failure.

Acceptance checks:

```bash
MODE=dry_run RUN_ROOT=/tmp/altibase-coding-agent-provenance-dry ./run-test.sh coding-agent
RUN_ID=coding_agent_provenance_limit1 RUN_ROOT=/tmp/altibase-coding-agent-provenance-limit1 LIMIT=1 ./run-test.sh coding-agent
git diff --check
```

Expected outcome:

- Coding-agent failures shift from missing provenance tokens toward only true
  missing facts, then eventually pass once exact metadata-bearing chunks and
  manifest rows are selected reliably.

### J005 - Judge Validity And Protected-Topic Calibration

Goal: separate true unsafe answers from judge artifacts before changing answer
prompts or package content.

Accepted review findings:

- `OPS-111` and `TOOL-038` are likely prohibited-claim false positives in the
  latest run. The answer text is safety-aware for `OPS-111`, and the `TOOL-038`
  answer gives `DIFF` before `FILESYNC`.
- Protected-topic blockers are mostly coverage and token findings attached to
  protected-topic questions. They are not automatically independent safety
  violations.
- The rule judge can miss semantically correct paraphrases because `fact_match`
  relies on lexical word overlap.

Implementation targets:

- `evals/altibase_answerability/scripts/judge_report.py`
- Judge self-tests and regression fixtures for `OPS-111`, `TOOL-038`, and a
  small fact-paraphrase calibration set.

Required behavior:

- Fix or tighten prohibited-claim detection so negated, caveated, or opposite
  ordered statements are not marked as claim presence solely because of high
  bag-of-words overlap.
- Add regression tests showing the latest `OPS-111` and `TOOL-038` answer
  patterns are not marked as prohibited claims.
- Keep true prohibited-claim detection active; this is not a waiver for unsafe
  answers.
- Add a judge-validity report that separates:
  - true prohibited-claim findings;
  - protected-topic coverage/token blockers;
  - missing-input safety failures;
  - possible paraphrase false negatives.
- Treat `term_score` 0.40-0.62 missed critical facts as calibration candidates.
  Sample them manually before broad threshold changes; do not assume every item
  in the band is a correct paraphrase.
- Do not use judge-only fields for answer-generation retrieval or prompt
  construction. Judge calibration may inspect judge-only fields only after the
  provider answer has already been generated.
- Do not add external source material outside `GPTs/upload_package`.

Acceptance checks:

```bash
python3 evals/altibase_answerability/scripts/judge_report.py --self-test
RUN_ID=judge_validity_ops111 RUN_ROOT=/tmp/altibase-judge-validity-ops111 QUESTION_ID=OPS-111 ./run-test.sh source-preserving
RUN_ID=judge_validity_tool038 RUN_ROOT=/tmp/altibase-judge-validity-tool038 QUESTION_ID=TOOL-038 ./run-test.sh source-preserving
git diff --check
```

Expected outcome:

- `OPS-111` and `TOOL-038` no longer fail because of false-positive
  prohibited-claim findings.
- Protected-topic blocker counts remain visible, but reports identify how many
  are coverage/token blockers rather than true safety findings.
- Pass-rate reporting is no longer interpreted as a pure retrieval metric.

### J006 - Targeted Calibration And Regression Gate

Goal: run a targeted calibration before spending a full 270-question live run.

Targeted questions:

- Coding-agent: all `AGENT-001` through `AGENT-010`.
- Full benchmark high-signal failures:
  - `PROP-101`
  - `SQL-101`
  - `TOOL-002`
  - `ERR-101`
  - `OPS-111`
  - `TOOL-038`
  - `AGENT-002` equivalent safety pattern is covered by the coding-agent suite.

Commands:

```bash
MODE=dry_run RUN_ROOT=/tmp/altibase-targeted-dry-coding ./run-test.sh coding-agent
RUN_ID=targeted_agent_live RUN_ROOT=/tmp/altibase-targeted-agent-live ./run-test.sh coding-agent

RUN_ID=targeted_prop101 RUN_ROOT=/tmp/altibase-targeted-prop101 QUESTION_ID=PROP-101 ./run-test.sh source-preserving
RUN_ID=targeted_sql101 RUN_ROOT=/tmp/altibase-targeted-sql101 QUESTION_ID=SQL-101 ./run-test.sh source-preserving
RUN_ID=targeted_tool002 RUN_ROOT=/tmp/altibase-targeted-tool002 QUESTION_ID=TOOL-002 ./run-test.sh source-preserving
RUN_ID=targeted_err101 RUN_ROOT=/tmp/altibase-targeted-err101 QUESTION_ID=ERR-101 ./run-test.sh source-preserving
RUN_ID=targeted_ops111 RUN_ROOT=/tmp/altibase-targeted-ops111 QUESTION_ID=OPS-111 ./run-test.sh source-preserving
RUN_ID=targeted_tool038 RUN_ROOT=/tmp/altibase-targeted-tool038 QUESTION_ID=TOOL-038 ./run-test.sh source-preserving
```

The coding-agent live command intentionally runs all 10 coding-agent questions;
that is the targeted coding-agent set. It is not the 270-question full benchmark.

Acceptance target:

- At least one coding-agent question passes, or retrieval audit proves that the
  expected provenance tokens are present in selected context for every
  coding-agent failure.
- `OPS-111` and `TOOL-038` do not produce false-positive prohibited-claim
  findings after J005. If they still do, inspect judge validity before changing
  the answer prompt.
- At least three of the six targeted full-benchmark questions improve in
  retrieval-side metrics: selected expected source presence, required token
  preservation, critical fact term-score distribution, or missing-context
  self-report rate.
- Record pass/fail separately from retrieval metrics. A question such as
  `PROP-101` may be a judge-calibration example even when retrieval is already
  adequate.
- If targeted calibration does not improve retrieval-side metrics, do not run
  the full benchmark; inspect retrieval audit output and revise J002/J003. If
  retrieval improves but pass rate does not, inspect J005 before changing
  package wording.

### J007 - Full Re-Run And Regression Analysis

Goal: prove whether retrieval improvements materially improve benchmark
readiness.

Commands:

```bash
./run-test.sh source-preserving
./run-test.sh coding-agent
```

Post-run analysis:

- Compare against:
  - `altibase_source_preserving_20260520_090243`
  - `altibase_coding_agent_20260520_104452`
- Retrieval scorecard:
  - selected source/shard/block presence from retrieval audit;
  - required token preservation delta;
  - critical fact `term_score` distribution delta;
  - missing-context self-report delta;
  - coding-agent provenance-token context presence.
- Pass-rate and judge-validity scorecard:
  - pass-rate delta;
  - protected-topic blocker delta;
  - gained and lost pass question IDs;
  - true prohibited-claim count versus likely judge false positives;
  - top remaining remediation targets.

Acceptance target for the first improvement cycle:

- Full benchmark: meaningful increase in required token preservation and
  critical fact coverage, even if pass rate remains below readiness threshold.
- Coding-agent: at least one passing question or clear evidence that required
  provenance tokens are now present in selected context for failed questions.
- No increase in true prohibited claims, and no known `OPS-111` / `TOOL-038`
  false-positive regression.
- A successful first cycle is not expected to reach the 85% readiness threshold.
  If token preservation and critical fact term-score distribution improve while
  pass rate remains flat, treat the next blocker as judge calibration, not
  retrieval.

## Priority Order

1. J001, because current reports do not explain whether selected context
   contains the needed source blocks.
2. J002 and J003, because source-preserving package quality depends on
   metadata-propagated source-internal chunk retrieval, not flat lexical chunk
   ranking or whole-block inclusion.
3. J004, because coding-agent tasks explicitly require provenance token
   preservation.
4. J005, because protected-topic and prohibited-claim reporting must distinguish
   true safety failures from judge artifacts before prompt changes.
5. J006, because targeted live calibration should prove the retrieval changes
   and judge-validity checks before a full run spends 270 provider calls.
6. J007, because only full live runs can measure readiness impact.

## Risk Register

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Context budget overflow | Exact metadata-bearing chunks may crowd out other relevant facts | Reserve budget by section and keep deterministic truncation rules |
| Schema churn | Answer record changes may break judge validation | Prefer separate retrieval audit JSONL unless schema update is necessary |
| Source-body mutation | Package may fail source-preservation validation | Do not edit inside source block boundaries; run strict package validator |
| Judge-only leakage | Expected facts could enter prompt accidentally | Keep projection allowlist checks and self-tests active |
| Apparent improvement from external context | Results become invalid for package-only objective | Keep `attachment_glob` and `context_root` pinned to `GPTs/upload_package` |
| Whole-block retrieval is too coarse | Large manuals exceed context budget and hide relevant sections | Split source bodies into metadata-prefixed chunks and rank inside the source |
| Manifest routing misses the true source | Question text may not name the exact manual or source ID | Use source family/title/path/version/token scoring and audit misses before tuning |
| Lexical judge ceiling | Pass rate may stay flat even when retrieval improves | Report retrieval metrics and pass-rate metrics separately; calibrate `fact_match` on sampled paraphrase candidates |
| Prohibited-claim false positive | Correct safety-aware answers may be altered unnecessarily | Fix judge negation/order handling and regression-test `OPS-111` and `TOOL-038` before prompt changes |

## Validation Checklist

Run these checks before any full live benchmark:

```bash
git status --short
git diff --check
python3 GPTs/reports/scripts/validate_source_preserving_upload_package.py --strict-final
python3 evals/altibase_answerability/scripts/validate_benchmark.py \
  --manifest evals/altibase_answerability/manifests/full_benchmark_source_preserving_package.json \
  --profile full
python3 evals/altibase_answerability/scripts/validate_benchmark.py \
  --manifest evals/altibase_answerability/manifests/coding_agent_source_preserving_package.json \
  --profile coding_agent
python3 evals/altibase_answerability/scripts/judge_report.py --self-test
MODE=dry_run LIMIT=3 RUN_ROOT=/tmp/altibase-source-preserving-dry-check ./run-test.sh source-preserving
MODE=dry_run RUN_ROOT=/tmp/altibase-coding-agent-dry-check ./run-test.sh coding-agent
```

Then run live smoke checks:

```bash
RUN_ID=sp_limit1_smoke RUN_ROOT=/tmp/altibase-sp-limit1-smoke LIMIT=1 ./run-test.sh source-preserving
RUN_ID=agent_limit1_smoke RUN_ROOT=/tmp/altibase-agent-limit1-smoke LIMIT=1 ./run-test.sh coding-agent
```

Only after these pass should a full live run be started.

## Deliverables

- Retrieval audit output for package-only answer generation.
- Package manifest and shard-block parser.
- Source-block-aware context selection.
- Coding-agent provenance preservation improvements.
- Judge-validity and protected-topic calibration improvements.
- Targeted calibration gate report before any full live re-run.
- Full and coding-agent re-run analysis report.

## Stop Conditions

Stop before full live re-run if any of the following occur:

- `attachment_glob` or `context_root` is no longer `GPTs/upload_package`.
- Any answer-generation prompt includes `GPTs/reports`, `GPTs/attachments`,
  `GPTs/source_pack`, manual trees, release notes, or technical document trees.
- Source-preserving strict validation fails.
- Answer-runner self-test or judge self-test fails.
- `LIMIT=1` live smoke fails for either suite.
