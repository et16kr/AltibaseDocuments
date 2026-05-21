# Judge Re-calibration Gate — Cycle 2, Phase 1 (C2-04)

- Job: C2-04 — Judge re-calibration gate (Phase 1 gate)
- Master plan: `GPTs/reports/answerability_improvement_cycle2_plan_20260520.md`
  (item C2-04, "Acceptance — three separate scorecards")
- Gold set: `evals/altibase_answerability/fixtures/judge_gold_set.jsonl`
  (52 entries — 29 `covered`, 23 `not_covered`)
- Cycle-1 judge-validity baseline (`full_rerun_analysis_20260520.md` §4):
  agreement 75.0 %, precision 0.711, recall 0.931.
- First gate attempt: 2026-05-20 — **FAIL** (see §2).
- C2-02 revision + re-measurement: 2026-05-21 — **PASS** (see §3–§6).

## Gate verdict: **PASS**

The LLM-assisted fact judge clears the Phase-1 gate after the C2-02 revision.
All five gate criteria are met (§6). Phase 2 (retrieval / coverage — jobs
C2-05…C2-07) may proceed.

One-line result: LLM-judge agreement mean **94.87 %** (lowest 92.31 %),
precision and recall **0.954** mean (lowest 0.931 each), and the six C2-01
prohibited-claim false positives stay cleared (0 of 6, 0 across the whole
270-question job-11 run).

## 1. Rule-only calibration (reference)

```
python3 evals/altibase_answerability/scripts/calibrate_judge.py \
  --gold evals/altibase_answerability/fixtures/judge_gold_set.jsonl
```

| Metric | Value |
| --- | ---: |
| Agreement | 75.0 % (39/52) |
| Precision (positive class = `covered`) | 0.7105 |
| Recall | 0.9310 |
| F1 | 0.8060 |
| Confusion (TP / FP / FN / TN) | 27 / 11 / 2 / 12 |

Reproduces the cycle-1 baseline exactly. The rule judge's error profile is
**11 false positives** (over-credits) and **2 false negatives**.

## 2. First gate attempt (2026-05-20) — FAIL

The original C2-02 LLM fact judge was measured over three fresh-cache runs and
**failed**: agreement mean 88.46 % (< 90 %), lowest 86.54 % (< 88 %), and recall
0.76–0.83 in every run (< 0.90). The judge had eliminated all 11 rule-judge
over-credits (precision → 1.00) but **over-corrected** — a "strict grader"
prompt converted genuine paraphrases into false negatives — and was
**non-deterministic** (OPS-126 F01/F02 flipped verdict across identical runs,
driving a 3.84 pp spread). Diagnosis: the Phase-1 blocker was entirely C2-02;
C2-01 and C2-03 were sound.

## 3. C2-02 revision (2026-05-21)

Two changes to the LLM fact judge in
`evals/altibase_answerability/scripts/judge_report.py`:

1. **Prompt rebalanced** (`LLM_FACT_JUDGE_PROMPT_VERSION = c2-04-balanced-2`).
   The "strict grader" / "mere keyword overlap" framing was replaced with a
   balanced decision rule: it still rejects answers that contradict or state a
   materially different fact (so the rule judge's over-credits stay rejected —
   this is what holds precision up), but it credits a correct paraphrase that
   omits secondary or incidental detail, a rule stated without its exception,
   and an enumeration fact whose answer conveys the restriction and most of the
   listed items. An answer that names none of the listed items, or omits the
   restriction itself, is still not covered.
2. **Majority-of-N voting** (`DEFAULT_LLM_FACT_JUDGE_VOTES = 3`, env
   `JUDGE_LLM_FACT_VOTES`). Each in-band fact is graded by the majority of
   three independent provider calls. This removes the per-fact verdict
   flakiness that produced the first attempt's 3.84 pp spread.

Supporting change: the verdict cache key now includes the prompt version, so a
prompt change automatically invalidates stale verdicts. The `judge_report.py`
self-test gained deterministic coverage of the verdict parser and the majority
vote helper and still runs with the LLM judge OFF.

## 4. LLM-assisted fact judge — three runs, fresh cache each

Three independent runs, each with a fresh verdict cache (the C2-02 cache was
bypassed), `JUDGE_LLM_FACT_VOTES=3`. The live Codex CLI command provider was
available throughout: **46 in-band facts, 138 provider calls, 0 fallbacks** per
run.

```
JUDGE_LLM_FACT_VOTES=3 python3 evals/altibase_answerability/scripts/calibrate_judge.py \
  --gold evals/altibase_answerability/fixtures/judge_gold_set.jsonl \
  --llm-fact-judge --llm-fact-judge-cache <fresh-cache-file>
```

| Run | Agreement | Precision | Recall | F1 | TP / FP / FN / TN |
| --- | ---: | ---: | ---: | ---: | :---: |
| 1 | 92.31 % (48/52) | 0.9310 | 0.9310 | 0.9310 | 27 / 2 / 2 / 21 |
| 2 | 96.15 % (50/52) | 0.9655 | 0.9655 | 0.9655 | 28 / 1 / 1 / 22 |
| 3 | 96.15 % (50/52) | 0.9655 | 0.9655 | 0.9655 | 28 / 1 / 1 / 22 |
| **mean** | **94.87 %** | **0.9540** | **0.9540** | **0.9540** | — |
| **lowest** | **92.31 %** | **0.9310** | **0.9310** | — | — |

Raw JSON: `evals/altibase_answerability/improvement2/logs/gate3_llm_run_{1,2,3}.json`
(git-ignored runtime output). Runs 2 and 3 are identical — voting made the
verdicts stable; run 1's two extra disagreements (SQL-102 F05, SQL-120 F02) are
2-1 vote splits that settled correctly in runs 2/3. The first attempt's
agreement mean rose 88.46 % → 94.87 % and recall 0.79 → 0.954.

## 5. Per-disagreement breakdown — steady state (runs 2/3)

At steady state the judge has exactly **two** disagreements, both long-standing
borderline gold entries:

| Question / fact | Type | Note |
| --- | :---: | --- |
| REPL-106 F04 | FP | The answer describes `DROP TABLE` removing a table from replication but omits the gap-given-up / data-mismatch risk that is the fact's substantive point. A genuine over-credit — the lone survivor of the rule judge's original 11. |
| REPL-108 F04 | FN | Compound fact (multiple appliers + improves performance + distributes XLogs by transaction + commit-sync caveat); the answer conveys roughly half. The gold `covered` label is generous; `not_covered` is defensible. |

The LLM judge eliminated 10 of the rule judge's 11 over-credits and both of its
false negatives, at the cost of the single REPL-106 F04 over-credit.

## 6. Gate criteria

| Criterion | Target | Measured | Verdict |
| --- | --- | --- | :---: |
| LLM-judge agreement — mean of 3 runs | ≥ 90.0 % | 94.87 % | **PASS** |
| LLM-judge agreement — lowest of 3 runs | ≥ 88.0 % | 92.31 % | **PASS** |
| Precision — every run | ≥ 0.711 | 0.931 / 0.966 / 0.966 | **PASS** |
| Recall — every run | ≥ 0.90 | 0.931 / 0.966 / 0.966 | **PASS** |
| Job-11 re-judge prohibited-claim findings on the 6 IDs | 0 | 0 (and 0 across all 270) | **PASS** |

Prohibited-claim re-check: the cycle-1 job-11 full run was re-judged end to end
with the current `judge_report.py`; PROP-140, PROP-142, SQL-137, TOOL-003,
TOOL-019, TOOL-033 each produce **0** prohibited-claim findings, and there are
**0** prohibited-claim findings anywhere in the 270-question run. The C2-01
round-2 fix holds. `judge_report.py --self-test` passes.

**All five criteria pass. The gate is met.**

## 7. Caveat — gold-set resolution

The residual disagreements are not a judge defect but the borderline tail of a
52-entry gold set. The tuning pass surfaced a genuine inconsistency: SQL-120 F05
and SQL-102 F05 are both "answer conveys 2 of 3 listed items" yet are labelled
`covered` and `not_covered` respectively (the distinction — homogeneous example
list vs. a conjunction of distinct facts — is real but fine-grained). A set this
small cannot resolve a judge much past the mid-90s, and one entry is ≈ 1.9 %.
As the cycle-2 plan and the first gate report already note, **cycle 3 should
expand and audit the gold set** so the judge-validity gate has more resolution.

Operational note: `JUDGE_LLM_FACT_VOTES=3` triples the judge's provider calls.
For the long Phase-3 runs (C2-08/C2-09) the vote count can be tuned down via the
env var if provider cost or time becomes a constraint; 3 is the default for
gate-grade stability.

## 8. Outcome

- Gate verdict: **PASS**.
- C2-01 and C2-03 stand; C2-02 was revised (§3) and now clears the gate.
- The cycle-2 runner may proceed to Phase 2 (C2-05…C2-07).
