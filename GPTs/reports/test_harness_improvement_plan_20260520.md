# Altibase Answerability Test Harness — Improvement Plan

- Date: 2026-05-20
- Repository: `/home/et16/AltibaseDocuments`
- Scope: `evals/altibase_answerability/` test harness only. No changes to
  `GPTs/upload_package/` source bodies.
- Baseline runs: `altibase_source_preserving_20260520_090243` (full, 14/270),
  `altibase_coding_agent_20260520_104452` (coding-agent, 0/10)
- Companion analysis: `GPTs/reports/source_preserving_test_analysis_and_plan_review_20260520.md`

## Why This Plan Exists

The current 5.2% pass rate measures defects in the test harness, not the quality
of the upload package. Two independent failure engines, both inside
`evals/altibase_answerability/`, must be fixed before the benchmark can produce a
valid measurement:

- **Engine A — Retrieval.** `answer_runner.py` builds context with flat 8 KB
  lexical chunks and never executes the package's manifest-routing contract.
  ~69% of missed critical facts and all coding-agent provenance failures trace
  here.
- **Engine B — Judge.** `judge_report.py` is a bag-of-words lexical scorer that
  under-credits paraphrased-correct answers (~31% of missed facts are false
  negatives) and produces false-positive prohibited-claim findings.

The Codex improvement plan addresses Engine A only. This plan covers both, and
fixes the Engine B work the Codex plan misframes as "safety" work.

## Track 1 — Retrieval (`answer_runner.py`)

### T1 — Retrieval audit instrumentation

- **Target:** `answer_runner.py` `main()`; new `write_retrieval_audit()`.
- **Change:** write a sidecar `retrieval_audit.jsonl` next to `answers.jsonl`,
  one record per question:
  - `question_id`, `query_tokens`, `budget`, `selected_chunks`
    (each: `rel_path`, `heading`, `char_count`, `score`),
  - flags: `included_02_manifest`, `included_03_manifest`, `included_readme`,
    `distinct_shards`.
- **Post-judge recall report:** a new `judge_report.py` diagnostic pass that,
  *after* judging, compares each question's selected context against judge-only
  `source_refs` and `required_tokens`. This is permitted because it runs after
  the provider call and is diagnostic output, not answer-generation input.
- **Risk:** none — additive sidecar, no answer-record schema change.
- **Acceptance:**
  ```bash
  MODE=dry_run LIMIT=5 RUN_ROOT=/tmp/altibase-audit ./run-test.sh source-preserving
  test -s /tmp/altibase-audit/answers/retrieval_audit.jsonl
  git diff --check
  ```
- **Do first.** Every later item is measured against this output.

### T2 — Source-block metadata propagation in chunking

- **Target:** `split_markdown_chunks()` (line 340), `ContextChunk` (line 92),
  `make_context_chunk()` (line 328).
- **Problem:** the `<!-- SOURCE_BLOCK_BEGIN source_id=... block_id=... -->`
  wrapper is an HTML comment, not a Markdown heading, so chunk splitting ignores
  it and block provenance is lost.
- **Change:**
  - Parse `SOURCE_BLOCK_BEGIN` / `SOURCE_BLOCK_END` comments; track
    `current_block_meta` (`source_id`, `block_id`, `source_path`,
    `source_family`, `version_scope`, `language`, `authority_label`).
  - Add a `block_meta` field to `ContextChunk`.
  - When emitting the chunk context header, prefix provenance, e.g.
    `===== source_id=SRC-000018 block_id=BLOCK-000001 version=7.1 :: <heading> =====`.
- **Effect:** `SRC-*` / `BLOCK-*` / shard-path tokens become literally present
  in context — the structural fix for coding-agent provenance failures.
- **Acceptance:** dry-run a coding-agent question; T1 audit shows `SRC-*` and
  `BLOCK-*` strings inside selected context for `AGENT-001`.

### T3 — Query tokenization fix

- **Target:** `tokenize_query()` (line 319), `score_chunk()` (line 375).
- **Problem:** the query string concatenates `id`, `question`, `version_scope`,
  `user_level`, `answer_type`. `user_level` / `answer_type` are generic strings
  (`advanced_operator`, `reference`) that occur in thousands of chunks and
  dilute the technical signal.
- **Change:**
  - Build the lexical signal from `question` only; drop `user_level` and
    `answer_type` as ranking tokens.
  - Extract technical tokens from the question (uppercase identifiers, `V$...`,
    tokens with `_`/`$`/`.`, error-code patterns) and weight them ~4× in
    `score_chunk`.
  - Use `version_scope` as a separate per-chunk bonus: chunk
    `block_meta.version_scope == query version` → score boost.
- **Acceptance:** T1 audit shows tighter, more topical chunk selection on a
  10-question sample; output deterministic across two runs.

### T4 — Manifest-aware routing stage

- **Target:** new functions in `answer_runner.py`; integrated into
  `build_context()` (line 388).
- **Change:**
  - `parse_source_manifest()` — parse the `02_source_manifest.md` TSV into rows
    keyed by `source_id`.
  - `parse_shard_manifest()` — parse `03_source_to_shard_manifest.md` into a
    `(source_id, block_id) → shard_path` map; normalize preserved
    `GPTs/source_pack/...` paths to the matching
    `GPTs/upload_package/source_pack_shard_*.md` by basename.
  - `route_sources(query, rows)` — score manifest rows by query/technical-token
    overlap against `title`, `source_family`, `source_path`, `version_scope`,
    `language`; return top-K `source_id`s.
  - In `build_context`, give a large score bonus to chunks whose
    `block_meta.source_id` is in the routed set, so routed blocks win ranking.
  - Uses only the question text and in-package manifests — no judge-only fields.
- **Effect:** implements the README's documented retrieval contract;
  `03_source_to_shard_manifest.md` data stops being unused (currently 0/270).
- **Acceptance:** T1 audit shows routed-source chunks present in selected
  context for a clear majority of a 20-question sample.

### T5 — Budgeted context assembly

- **Target:** `build_context()` (line 388).
- **Change:** partition `max_context_chars` (180 KB) deterministically:
  routing metadata for routed sources → routed-block chunks with provenance
  prefixes → secondary lexical chunks. Keep `max_context_chars` semantics and
  deterministic ordering/truncation.
- **Acceptance:** `LIMIT=1` live smoke for both suites; context never exceeds
  budget; `git diff --check` clean.

## Track 2 — Judge (`judge_report.py`)

### T6 — Fix prohibited-claim false positives

- **Target:** `answer_has_negation_near()` (line 437),
  `prohibited_claim_present()` (line 451).
- **Problem:** OPS-111 and TOOL-038 are flagged as prohibited claims although
  both answers are correct and safe. Causes: the negation check inspects only
  the 4 longest claim terms within a 6-token window and fails on plural/singular
  mismatch (`tablespaces` vs `tablespace`); and bag-of-words cannot represent
  statement order (TOOL-038 correctly runs DIFF before FILESYNC).
- **Change:**
  - Suffix-normalize terms (`-s`, `-es`, `-ed`, `-ing`) before negation
    matching; check all high-value terms, not the top 4; widen the window or
    use sentence-level negation detection.
  - For ordered claims, do not flag on bag-of-words overlap alone; require the
    claim's subject + verb + polarity to appear un-negated.
- **Regression test:** add OPS-111 and TOOL-038 answer fixtures to
  `judge_report.py --self-test`; both must score "not present".
- **Acceptance:** `python3 evals/altibase_answerability/scripts/judge_report.py --self-test`
  passes the two new cases.

### T7 — Semantic-tolerant fact matching

- **Target:** `fact_match()` (line 400), `term_present()` (line 361).
- **Problem:** fact coverage is exact-word overlap with a `term_score >= 0.62`
  bar. Word-form variants fail (`restarting` ≠ `restarted`,
  `reflected` ≠ `take effect`). PROP-101 gives a substantively correct answer
  scored `term_score=0.50`. Because all 270 questions are Korean-sourced and the
  expected facts are English paraphrases authored by the benchmark, retrieval
  cannot close this lexical gap.
- **Change — phase A (deterministic, do now):**
  - Add light stemming/lemmatization in `term_present` so word-form variants
    match.
  - Add a small curated equivalence map for recurring Altibase phrasings
    (e.g. `restart` ↔ `reboot`; `reflected` ↔ `applied` / `take effect`).
- **Change — phase B (follow-up):**
  - Add an optional LLM-assisted fact-coverage judge. `judge_report.py`
    currently hard-stops non-rule modes (line 1244); extend
    `--judge-mode {rule,hybrid}`. `hybrid` uses a model (same command-provider
    plumbing as `answer_runner.py`, pinned model, low temperature) for fact
    coverage only, and keeps the deterministic rule judge for literal token
    preservation. `rule` stays the default and fallback.
- **Acceptance:** re-judging the existing `...090243` answers with phase A,
  PROP-101 F01 becomes covered; agreement with the T9 gold set improves without
  loss of precision.

### T8 — Pass-logic and threshold consistency

- **Target:** pass computation (`judge_report.py` line 827); `policy.json`.
- **Problem:** any missed critical fact emits a `high` finding and any missed
  required token emits a `medium` finding, and `passed` requires
  `severity in {none, low}` — so passing needs zero misses, and the
  `critical_fact_coverage >= 0.80` clause is dead code. Degenerate required
  tokens exist (single-character `'0'`).
- **Change:** reconcile the pass test with the stated policy thresholds
  (`critical_fact_coverage_minimum = 0.90`, etc.) so the bar is intentional and
  consistent; fix or remove degenerate required tokens in the question records.
- **Note:** this is a policy decision — present options to the benchmark owner;
  do not change thresholds silently.

### T9 — Judge calibration gold set

- **Target:** new `evals/altibase_answerability/fixtures/judge_gold_set.jsonl`;
  new `evals/altibase_answerability/scripts/calibrate_judge.py`.
- **Change:**
  - Hand-label ~40 (question, answer, per-fact covered/not-covered, overall
    correct/incorrect) records sampled from the latest run — weighted toward the
    172 facts in the `term_score` 0.40–0.62 band plus clear pass/fail anchors.
  - `calibrate_judge.py` runs the judge against the gold set and reports
    precision, recall, and judge-vs-human agreement.
  - Tune T6/T7/T8 until agreement reaches a target (recommend ≥ 90%).
- **Acceptance:** calibration report meets the agreement target; precision does
  not regress (semantic tolerance must not over-credit wrong answers).

## Sequencing

| Phase | Items | Notes |
| --- | --- | --- |
| 0 | T1 | Additive instrumentation; do first |
| 1 (judge validity) | T9, T6, T7-A, T8 | Makes the measuring instrument trustworthy |
| 2 (retrieval) | T2, T3, T4, T5 | Touches `answer_runner.py`; runnable in parallel with Phase 1 |
| 3 | Targeted calibration run, then full re-run | Needs both tracks |
| Follow-up | T7-B (LLM judge) | After phase-A calibration is stable |

Phase 1 (`judge_report.py`) and Phase 2 (`answer_runner.py`) touch different
files and can proceed in parallel with separate owners. Phase 1 should not lag,
because until the judge is trustworthy, retrieval gains cannot be read as
pass-rate movement.

Phase 3 — run the Codex plan's targeted set first (AGENT-001…010 plus PROP-101,
SQL-101, ERR-101, TOOL-002, OPS-111, TOOL-038) as a stop/go gate, then the full
270-question + 10-agent run.

## Acceptance — Three Separate Scorecards

Do not collapse these into a single pass-rate number. Each moves with a
different track.

| Scorecard | Metric | Source | Moves with |
| --- | --- | --- | --- |
| Retrieval | routed source family present in selected context (%) | T1 audit | Phase 2 |
| Retrieval | required tokens present in context (%) | T1 post-judge recall | Phase 2 |
| Retrieval | answers self-reporting missing context (33% baseline → < 10% target) | answer scan | Phase 2 |
| Retrieval | coding-agent `SRC-*`/`BLOCK-*` in-context rate | T1 audit | Phase 2 |
| Judge validity | judge-vs-human agreement on gold set (≥ 90%) | T9 | Phase 1 |
| Judge validity | OPS-111 / TOOL-038 prohibited-claim findings = 0 | self-test | Phase 1 |
| Pass rate | pass rate; gained/lost question IDs | full re-run | Phases 1 + 2 |

First-cycle expectation: the retrieval and judge-validity scorecards should move
clearly. The pass rate will move only after both tracks land, and is not
expected to reach the 85% readiness threshold in one cycle.

## Risks

| Risk | Mitigation |
| --- | --- |
| Semantic tolerance over-credits wrong answers | Calibrate against the T9 gold set; track precision, not only recall |
| LLM judge nondeterminism | Keep rule judge as default and fallback; pin model, low temperature; report judge mode per run |
| Judge calibration leaks expected facts into the answer prompt | Keep the projection allowlist and leakage self-tests active; judge work touches `judge_report.py` only |
| Retrieval router misses the true source for vaguely worded questions | T1 audit surfaces the miss; iterate router scoring before tuning prompts |
| Answer-record schema churn | Keep T1 audit as a sidecar file, not a schema change |
| Threshold change masks real regressions | T8 is an explicit owner decision, documented, not silent |

## Validation Checklist

Before any live run:

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
python3 evals/altibase_answerability/scripts/answer_runner.py --self-test
python3 evals/altibase_answerability/scripts/judge_report.py --self-test   # must include OPS-111 / TOOL-038
MODE=dry_run LIMIT=3 RUN_ROOT=/tmp/altibase-sp-dry ./run-test.sh source-preserving
MODE=dry_run RUN_ROOT=/tmp/altibase-agent-dry ./run-test.sh coding-agent
```

Then `LIMIT=1` live smoke for each suite, then the targeted calibration gate,
then the full re-run.

## Relationship to the Codex Plan

| This plan | Codex plan equivalent | Status |
| --- | --- | --- |
| T1 | J001 | Same intent; keep |
| T2, T4, T5 | J002, J003 | Same intent; keep |
| T3 | partial J003 | Adds explicit query-token de-weighting |
| T2 (provenance prefix) | J004 | Retrieval-side fix for coding-agent provenance |
| T6, T7, T8, T9 | — (Codex J005 instead) | New. Codex J005 misframes this as safety-prompt work; the real defect is in the judge |

The non-negotiable constraints from the Codex plan (context pinned to
`GPTs/upload_package/*.md`; no `GPTs/reports`/`GPTs/attachments` leakage; no
source-body edits; no judge-only fields in retrieval; pinned
`provider=command`, `model=gpt-5.5`) carry over unchanged.
