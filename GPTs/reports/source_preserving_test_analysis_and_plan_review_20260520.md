# Source-Preserving Benchmark — Test Result Analysis and Plan Review

- Date: 2026-05-20
- Repository: `/home/et16/AltibaseDocuments`
- Scope: `evals/altibase_answerability` package-only runs over `GPTs/upload_package/*.md`
- Runs analyzed:
  - full benchmark: `altibase_source_preserving_20260520_090243` (270 questions)
  - coding-agent: `altibase_coding_agent_20260520_104452` (10 questions)
- Document under review: `GPTs/reports/source_preserving_answerability_improvement_plan_20260520.md`
  (the "Codex plan")

## 1. Verdict

The Codex plan transcribes the run metrics correctly and its core retrieval
diagnosis is **substantially right but incomplete**. There is a real, severe
retrieval problem. But the plan attributes 100% of the failure to "retrieval and
synthesis quality" and therefore misses two findings that this analysis
establishes from the run artifacts:

1. **A second, independent failure engine exists: the lexical rule judge.** The
   benchmark is scored entirely by a bag-of-words rule judge that requires
   ~62% exact word overlap per expected fact and 100% literal token
   preservation, and that turns any single missed fact or token into an
   auto-fail finding. A semantically correct, well-grounded answer fails this
   judge routinely. Roughly **30% of "missed" critical facts are paraphrase
   false negatives**, not content gaps. No amount of retrieval work removes this
   ceiling.

2. **Codex job J005 ("Protected-Topic Safety Fixes") is misdiagnosed.** The 104
   "protected-topic blockers" are not safety violations — 187 of 188
   blocker-severity findings are ordinary coverage/token misses on
   protected-topic-tagged questions and will clear when coverage improves. The
   only two prohibited-claim findings (OPS-111, TOOL-038) are **both false
   positives** produced by a broken negation check in the judge. There is no
   real prohibited-claim problem to fix with prompt scaffolding; the defect is
   in the judge.

Net: keep the Codex retrieval jobs (J001–J004), drop/replace J005, and add a
judge-validity job. Reset the success criteria — retrieval work will move the
coverage and token metrics, but the 85% pass-rate target is gated by judge
design, not by retrieval alone.

## 2. Metric Verification

Every number in the Codex plan's evidence tables was checked against
`judge/aggregate_report.json` and `summary.txt`. All transcriptions are
accurate:

| Suite | Pass rate | Critical fact coverage | Required token preservation | Unsupported-claim rate | Protected-topic blockers |
| --- | ---: | ---: | ---: | ---: | ---: |
| full (`...090243`) | 5.2% (14/270) | 49.8% | 56.4% | 0.7% | 104 |
| coding-agent (`...104452`) | 0.0% (0/10) | 55.0% | 65.4% | 0.0% | 5 |

The Codex claim that this is not a runner failure is also correct:
`run.json` reports `errors=0` for both runs and all 270 + 10 answer records have
`status=answered`.

**Added context the Codex plan omits — the metrics have plateaued.** The last
three full source-preserving runs:

| Run | Pass | Critical fact coverage | Token preservation |
| --- | ---: | ---: | ---: |
| `...20260519_224759` | 0/270 | 7.2% | 10.0% |
| `...20260520_015047` | 18/270 (6.7%) | 50.6% | 55.5% |
| `...20260520_090243` | 14/270 (5.2%) | 49.8% | 56.4% |

The first run was a broken context build. The two healthy runs are flat within
noise (and the "latest" run is in fact slightly *worse* than its predecessor).
A flat plateau across runs is itself evidence that the benchmark is bounded by a
structural ceiling, not by tunable answer quality.

## 3. Failure Engine A — Retrieval and Synthesis (Codex diagnosis: confirmed)

The Codex plan's retrieval diagnosis holds up and the evidence is stronger than
the plan states.

### 3.1 The selection ratio is extreme

`GPTs/upload_package/` is **59.7 MB** of Markdown (20 files; 16 shards of
1–4.5 MB each). The runner budget is `--max-context-chars 180000`. The lexical
builder must therefore select **~0.3%** of the corpus per question.

### 3.2 The lexical builder treats the package as flat chunks

Confirmed in `evals/altibase_answerability/scripts/answer_runner.py`:

- `split_markdown_chunks` splits each file into ~8 KB chunks on Markdown
  headings. The shard provenance wrappers (`SOURCE_BLOCK_BEGIN` HTML comments,
  `source_id`, `block_id`) are not headings, so block metadata is not a chunk
  boundary and is scattered into body chunks.
- `score_chunk` ranks chunks purely by query-token frequency. Query tokens
  include `version_scope`, `user_level`, and `answer_type` (e.g. `7.3`,
  `advanced_operator`, `reference`) — generic strings that occur in thousands of
  chunks and dilute the technical signal.
- There is no manifest lookup. The README's stated retrieval contract
  (`02_source_manifest` → `03_source_to_shard_manifest` → exact shard block) is
  never executed.

### 3.3 The routing manifests are effectively never retrieved

Across the 270 full-benchmark answers, context-file selection frequency:

| File | Questions that used it |
| --- | ---: |
| `00_README_SOURCE_PRESERVING_UPLOAD.md` | 1 / 270 |
| `01_upload_order.md` | 1 / 270 |
| `02_source_manifest.md` | 21 / 270 |
| `03_source_to_shard_manifest.md` | **0 / 270** |
| `source_pack_shard_*.md` | the rest |

The source-to-shard map — the file that makes `SRC-*`/`BLOCK-*` routing
possible — is never selected. This directly confirms Codex jobs J002 and J003.

### 3.4 The model self-reports missing context in a third of cases

**89 of 270 answers (33%)** explicitly state that the supplied context is
insufficient (e.g. SQL-101: *"The included context does not expose the exact
Altibase 8.1 `CREATE DISK TABLESPACE` grammar"*). None of those 89 passed. When
the model itself reports a retrieval gap, the gap is real.

### 3.5 Genuine missed facts dominate, but not exclusively

Of **562 missed critical facts** across the run, by judge `term_score`:

| `term_score` band | Count | Interpretation |
| --- | ---: | --- |
| < 0.40 | 389 (69%) | Genuine content miss — answer did not substantively address the fact |
| 0.40–0.62 | 172 (31%) | Likely correct-but-paraphrased — see Failure Engine B |

So ~69% of missed facts are real retrieval/synthesis gaps. The Codex plan is
right that retrieval is the largest single lever. It is wrong that it is the
only one.

## 4. Failure Engine B — The Lexical Rule Judge (Codex omission)

The benchmark is judged **only** by the rule judge
(`judge_report.py` exposes `--judge-mode {rule}`; line 1244 hard-stops any other
mode). This is a pure lexical scorer, and the Codex plan never accounts for it.

### 4.1 How the judge decides "covered"

`fact_match` (judge_report.py:400) computes `term_score` = fraction of the
expected fact's content words that appear in the answer, each checked with a
word-boundary regex. A fact is `covered` only if `term_score >= 0.62` (or with
technical-token assistance, `>= 0.45`/`0.35`). Word *forms* must match:
`restarting` ≠ `restarted`, `changed` ≠ `change`, `reflected` ≠ `take effect`.

### 4.2 Worked example — PROP-101 is a correct answer that fails

PROP-101 expected fact F01: *"Static property-file changes are made in
`$ALTIBASE_HOME/conf/altibase.properties` and require restarting the Altibase
server before the changed value is reflected."*

The model's answer: *"Static file change: edit
`$ALTIBASE_HOME/conf/altibase.properties`. This is static, so Altibase must be
stopped or restarted for the new value to take effect."*

This is **factually complete and correct**. The judge scored it
`term_score=0.50` → `covered=false`, because `restarted`/`stopped`/`take effect`
are different word forms from `restarting`/`reflected`. PROP-101's answer
covers all four expected facts in substance, scored `critical_fact_coverage=0.75`,
and **failed**. This is a judge artifact, not a retrieval or synthesis defect.

### 4.3 The pass bar is near-perfect lexical reproduction

`passed` (judge_report.py:827) requires `severity in {none, low}`. But any missed
critical fact emits a `high` finding and any missed required token emits a
`medium` finding — both exceed `low`. So in practice **passing requires zero
missed critical facts and zero missed required tokens**, scored lexically. The
`critical_fact_coverage >= 0.80` clause in the pass test is effectively dead
code. Evidence: 25 questions failed *only* on `severity` while clearing every
numeric threshold; 29 questions had `critical_fact_coverage = 1.0` and still
failed on tokens/supporting facts.

Against an 85% pass-rate readiness threshold, a paraphrasing model judged this
way effectively cannot reach readiness even with perfect retrieval. 67 of 256
failed questions already score `overall >= 0.75`.

### 4.4 Required-token failures are a mix, not all retrieval

925 of 2,108 required tokens (43.9%) were not preserved. The missing-token
distribution shows two distinct classes:

- **Exact source artifacts** the model cannot invent — `0x4102E`, `-266286`,
  `65535`, `2^32 - 1`, `2097152`, `1048576`. These are genuine
  retrieval-dependent failures (Codex J002/J003 fix them).
- **Common tokens** — `V$PROPERTY` (missing 28×), `ALTER SYSTEM` (21×),
  `ALTER SESSION`, `SELECT`, `SYS`. A correctly grounded answer should emit
  these; failures here are partly retrieval, partly answer phrasing, partly
  judge brittleness (e.g. the single-character required token `'0'`, missing
  7×, is a benchmark-design weakness).

## 5. Prohibited Claims — Both Findings Are False Positives (Codex J005 error)

The Codex plan's J005 lists OPS-111 and TOOL-038 as "current prohibited claim
examples" and proposes safety-prompt scaffolding to fix them. The answer text
shows both are **judge false positives**:

- **OPS-111** — flagged claim: *"System tablespaces can be dropped with CASCADE
  CONSTRAINTS."* The actual answer says *"Confirm … that it is **not** a system
  tablespace being deleted by a general user"* and describes `CASCADE
  CONSTRAINTS` accurately. The answer never makes the prohibited claim. It is a
  careful, correct, safety-aware answer.
- **TOOL-038** — flagged claim: *"FILESYNC should be run before diff."* The
  actual answer runs Data Validation with `DIFF` first (step 7) and only then
  switches to `FILESYNC` (steps 8–10) — the **opposite** of the prohibited
  claim.

Root cause: `prohibited_claim_present` (judge_report.py:451) flags any claim
whose terms have ≥90% bag-of-words overlap with the answer. Its negation guard,
`answer_has_negation_near`, only inspects the 4 longest claim terms and only
within a 6-token window, and fails on plural/singular mismatch
(`tablespaces` in the claim vs `tablespace` in the answer's negation). It also
cannot model statement ordering, so TOOL-038's correct DIFF-then-FILESYNC
sequence reads as the prohibited claim.

Consequences for the Codex plan:

- The real unsupported-claim rate is effectively **0%**, not 0.7% — and 0.7% is
  already inside the ≤2.0% threshold. There is no prohibited-claim problem to
  remediate with prompting.
- Adding safety scaffolding (Codex J005 required behavior) would change correct
  answers in pursuit of a non-existent defect. The fix belongs in the judge's
  negation/ordering logic.

## 6. Protected-Topic Blockers Are Coverage Failures, Not Safety Failures

The Codex plan treats "104 protected-topic blockers" as a safety signal. The
artifacts show otherwise. Blocker-severity findings in the run break down as:

| Finding category | Blocker-severity count |
| --- | ---: |
| `missing_critical_facts` | 92 |
| `missing_required_tokens` | 95 |
| `prohibited_claim` | 1 |

A finding becomes a `blocker` only when the question carries a protected-topic
tag *and* coverage is low (`judge_report.py` severity rules). So **187 of 188
blocker findings are the same coverage/token misses already counted under
Failure Engines A and B** — they are protected-topic-tagged copies of ordinary
failures and will clear automatically as coverage rises. The "0 protected-topic
blockers" readiness target is therefore a *derived* consequence of fixing
coverage, not a separate workstream.

## 7. Coding-Agent Provenance (Codex J004: confirmed)

The Codex claim that coding-agent answers miss `SRC-*`/`BLOCK-*`/shard-path
tokens is correct and structural. Coding-agent questions require exact
provenance tokens — e.g. AGENT-001 `required_tokens` include `SRC-000185`,
`BLOCK-000561`, `GPTs/upload_package/source_pack_shard_010.md`. The model cannot
emit these unless the matching `02_source_manifest` and
`03_source_to_shard_manifest` rows are in context. Since the source-to-shard map
is selected for 0/270 questions (§3.3), provenance-token failure is guaranteed.
The missing-token list for the coding-agent run is dominated by `SRC-*`,
`BLOCK-*`, and shard-path strings, exactly as predicted. J004 is valid, and it
depends on J002 (manifest parsing) to be effective.

## 8. Job-by-Job Assessment of the Codex Plan

| Codex job | Verdict | Notes |
| --- | --- | --- |
| J001 — Retrieval audit instrumentation | **Keep** | Correct and high value. Make it record, per question, whether the right shard block and the manifest rows were in selected context. |
| J002 — Manifest + shard index parser | **Keep** | The single highest-value fix. Parses `02`/`03` manifests into a `source_id → block_id → shard → block text` lookup. |
| J003 — Source-block-aware context builder | **Keep** | Correct. Must also de-weight generic query tokens (`version_scope`, `user_level`, `answer_type`) that currently dilute ranking. |
| J004 — Coding-agent provenance guardrail | **Keep** | Valid; depends on J002. |
| J005 — Protected-topic safety fixes | **Replace** | Misdiagnosed. No real prohibited claims exist; the two findings are judge false positives. Protected-topic blockers are coverage failures. Replace with a judge-validity job (R4 below). |
| J006 — Full re-run and regression analysis | **Keep, re-scope** | Acceptance targets must separate retrieval metrics (will move) from pass rate (judge-gated). |

The Codex plan's "Non-Negotiable Constraints" (keep context inside
`GPTs/upload_package`, no `GPTs/reports`/`GPTs/attachments` leakage, no
source-body edits, pinned `provider=command`, `model=gpt-5.5`,
`context=lexical`) are sound and should be carried forward unchanged.

## 9. Corrected Plan

Priority order: R1 → R2 → R3 → R4 in parallel with R2 → R5.

### R1 — Retrieval audit instrumentation (= Codex J001)

Per-question audit JSONL under the run's answers directory recording: selected
chunk headings, file paths, char counts, lexical scores; whether
`02_source_manifest.md`, `03_source_to_shard_manifest.md`, and the expected
shard block were present. Keep the answer-record schema stable; emit a sidecar
file. This lets every later run separate "block absent" from "block present,
not used."

### R2 — Manifest-aware, source-block-aware retrieval (= Codex J002 + J003)

- Parse `02_source_manifest.md` and `03_source_to_shard_manifest.md` into a
  deterministic `source_id → block_id → shard path → block text` lookup.
- When a query matches a source family / title / `SRC-*` / `BLOCK-*` / SQL token
  / property / error code / view / command, pull the **exact** source block
  rather than relying on flat 8 KB lexical chunks.
- Reserve the context budget by section: routing metadata → exact mapped block →
  wrapper/heading context → secondary lexical chunks.
- De-weight `version_scope`/`user_level`/`answer_type` in `tokenize_query`/
  `score_chunk` so generic strings stop dominating ranking.
- Stay inside `GPTs/upload_package/*.md`; do not edit `SOURCE_BLOCK` bodies.

### R3 — Coding-agent provenance via manifest retrieval (= Codex J004)

Once R2 lands, ensure coding-agent questions retrieve the manifest rows for the
relevant source so `SRC-*`/`BLOCK-*`/shard-path tokens are available, and have
the prompt scaffold instruct the model to return them. This is a retrieval fix,
not a prompting fix — verify with R1 audit output that the rows were present.

### R4 — Judge validity and calibration (replaces Codex J005)

This is new and necessary. Without it, R1–R3 will raise the coverage/token
metrics but the pass rate stays pinned.

1. **Fix the prohibited-claim false positives.** Repair `answer_has_negation_near`
   (plural/singular normalization, wider window, all high-value terms) and add
   statement-order awareness, or gate prohibited-claim detection behind a
   stricter check. Regression-test against OPS-111 and TOOL-038 — both must
   score "not present."
2. **Credit paraphrased-correct facts.** Either (a) add lemmatization / stemming
   and synonym tolerance to `fact_match` so `restarted`≈`restarting`, or
   (b) introduce an optional LLM-assisted judge mode for fact coverage while
   keeping the rule judge for literal token preservation. Calibrate on a hand-
   labeled sample (start with the 172 facts in the 0.40–0.62 band).
3. **Re-scope protected-topic blockers** as a derived view of coverage findings,
   not an independent readiness gate.
4. Keep all judge-only fields out of the answer prompt — calibration must not
   leak expected facts into answer generation.

### R5 — Re-run with split acceptance criteria (= Codex J006, re-scoped)

Re-run both suites and report two separate scorecards:

- **Retrieval scorecard** (expected to move with R1–R3): required-token
  preservation, critical-fact `term_score` distribution, share of answers
  self-reporting missing context, manifest-row presence rate from R1 audit.
- **Pass-rate scorecard** (gated by R4): pass rate, gained/lost question IDs.

First-cycle acceptance: a meaningful rise in token preservation and in the
fraction of facts with `term_score >= 0.62`, a sharp drop in the 33%
"missing context" self-reports, zero prohibited-claim findings on OPS-111 /
TOOL-038, and at least one coding-agent provenance pass. Do **not** expect the
85% pass rate from retrieval work alone — that target is unlocked by R4.

## 10. Risk Register

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Treating retrieval as the only lever | Pass rate stays pinned after large retrieval effort | Land R4 (judge validity) alongside R2; report retrieval and pass-rate metrics separately |
| "Fixing" prohibited claims via prompting | Correct, safe answers get altered for a non-existent defect | Fix the judge negation/order logic; leave the answer scaffold's safety wording as-is |
| Judge calibration leaks expected facts | Benchmark invalidated | Keep projection allowlist + leakage self-tests active; calibrate judge offline only |
| Context budget overflow from exact blocks | Exact blocks crowd out other facts | Reserve budget by section; deterministic truncation |
| Source-body mutation | Package fails source-preservation validation | No edits inside `SOURCE_BLOCK` boundaries; run the strict package validator |
| Apparent gains from out-of-package context | Results invalid for the package-only objective | Keep `attachment_glob`/`context_root` pinned to `GPTs/upload_package` |

## 11. Validation Checklist

Run before any full live re-run:

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
python3 evals/altibase_answerability/scripts/judge_report.py --self-test
MODE=dry_run LIMIT=3 RUN_ROOT=/tmp/altibase-sp-dry ./run-test.sh source-preserving
MODE=dry_run RUN_ROOT=/tmp/altibase-agent-dry ./run-test.sh coding-agent
```

Then `LIMIT=1` live smoke for each suite before a full run. R4 adds one gate:
the judge self-test must include OPS-111 and TOOL-038 prohibited-claim
regression cases before a full re-run is accepted.

## 12. Summary Table — Codex Plan Accuracy

| Codex plan claim | Status |
| --- | --- |
| Run metrics (pass rate, coverage, tokens, blockers) | Accurate |
| Not a runner failure (`errors=0`, all `answered`) | Accurate |
| Lexical builder treats package as flat chunks; no manifest lookup | Accurate (manifest selected 0/270) |
| Retrieval is the largest failure lever | Accurate (~69% of missed facts are genuine) |
| Coding-agent misses `SRC-*`/`BLOCK-*` provenance tokens | Accurate and structural |
| Failure is *only* retrieval and synthesis | **Incomplete** — ignores the lexical-judge ceiling (~31% of missed facts are paraphrase false negatives) |
| J005: OPS-111 / TOOL-038 are real prohibited claims | **Wrong** — both are judge false positives; answers are correct |
| 104 protected-topic blockers are a safety problem | **Wrong** — 187/188 blocker findings are coverage misses, not safety violations |
| J006 acceptance implies pass rate can rise from retrieval work | **Overstated** — pass rate is gated by judge design |

## 13. Addendum — Assessment of the Revised Codex Plan (2026-05-20, second version)

The Codex plan was revised after this review's first 12 sections were written.
The revision is a **substantial, genuine improvement** but **two of the three
core problems remain unaddressed**, and the unaddressed ones are decisive.

### 13.1 What the revision fixed (accept these)

- **Whole-block inclusion → metadata-propagated chunking.** The first version's
  J002/J003 said to "include exact source blocks." A `SOURCE_BLOCK` body is
  usually a whole manual (BLOCK-000001 alone is 540 KB) and cannot fit the
  180 KB budget. The revision correctly pivots to splitting source bodies into
  smaller chunks that carry propagated `source_id`/`block_id`/`source_path`/
  `version_scope`/`authority_label` provenance. This corrects a real technical
  flaw — credit to the revision for catching it.
- **Judge-only metadata boundary is now explicit.** New constraint forbids using
  `source_refs`/`required_tokens`/`expected_facts`/`canonical_reference_answer`
  for retrieval. J001's split into a pre-provider audit and an optional
  post-judge recall report (which *may* compare against judge-only `source_refs`
  because it runs after the provider call) is a correct, careful distinction.
- **Expectations are tempered.** The new "Expected Impact And Confidence"
  section and J007's "not expected to reach the 85% readiness threshold" address
  this review's third critique (overstated achievability).
- **Targeted calibration gate (J006).** Splitting a 6-question + 10-agent
  calibration gate ahead of the 270-call full run is sound de-risking. Its
  targeted set (PROP-101, SQL-101, ERR-101, TOOL-002, OPS-111, TOOL-038)
  overlaps precisely with the questions analyzed in this review.

### 13.2 What the revision still gets wrong

**(1) The lexical rule judge is still not acknowledged — the decisive gap.**
The revised plan still attributes all residual failure to retrieval and to
"model synthesis [omitting] facts even when retrieval succeeds." It never
identifies that the judge is a bag-of-words scorer requiring ~62% exact English
word overlap per fact, and that any single missed fact or token forces an
auto-fail finding (§4).

New evidence makes this gap larger than first stated: **all 270 questions are
Korean-sourced** (`source_language_basis`: 242 `ko`, 28 `ko+en`; zero
English-only). The expected facts are English paraphrases authored by the
benchmark; the authoritative source bodies in the shards are Korean; the judge
does English bag-of-words matching. **Retrieving the correct Korean source block
cannot raise English lexical overlap with the author's English fact wording.**
PROP-101 — which the revised plan lists as a J006 calibration target — already
has a substantively correct answer scored `term_score=0.50` on F01. Planning to
"improve" PROP-101 through retrieval chases a phantom: the mechanism that failed
it is the judge, not retrieval. The revised plan's low-confidence note ("unlikely
to approach 85% until retrieval recall is proven") **misattributes the ceiling
to retrieval recall when it is judge design.**

**(2) J005 is unchanged and still wrong.** It still lists OPS-111 and TOOL-038
as "current prohibited claim examples" and prescribes safety-prompt scaffolding.
Both are judge false positives from a broken negation/order check in
`prohibited_claim_present` (§5); the answers are already safe and correct. This
creates a trap: J006's gate "OPS-111 and TOOL-038 do not produce prohibited-claim
findings" can be satisfied only by fixing the judge (not in the plan) or by
perturbing already-correct answers. Executing J005 as written will spend effort
on a non-existent defect and the gate will likely still fail. The real fix —
repair the judge's negation detector (plural/singular normalization, wider
window, all high-value terms, statement-order awareness) — is absent.

### 13.3 Verdict

Adopt J001–J004 and J006–J007 of the revised plan; they are technically sound.
The plan is still **incomplete**: it needs the judge-validity job from §9 R4 of
this review, and J005 must be rewritten from "safety scaffolding" to "fix the
judge's prohibited-claim negation/order logic." Without that work, the revised
plan will raise the token-preservation and fact-coverage *metrics* but the pass
rate will stay pinned near 5% — which the revised plan half-predicts but
misexplains as a retrieval-recall limit rather than a judge-design limit.
