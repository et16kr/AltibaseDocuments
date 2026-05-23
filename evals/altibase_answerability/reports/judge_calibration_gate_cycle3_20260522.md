# Judge Re-calibration Gate — Cycle 3, Phase 1 (C3-05)

- Job: C3-05 — Judge re-calibration gate (Phase 1 gate)
- Master plan: `GPTs/reports/answerability_improvement_cycle3_plan_20260522.md`
  (item C3-05, "Acceptance — three separate scorecards")
- Gold set: `evals/altibase_answerability/fixtures/judge_gold_set.jsonl`
  — the **expanded** set produced by job C3-02: **147 entries**
  (111 `covered`, 36 `not_covered`), up from the cycle-2 52-entry set.
- Cycle-2 judge-validity steady state (`full_rerun_analysis_cycle2_20260520.md`
  §6, on the old 52-entry set): agreement 96.15 %, precision 0.966,
  recall ≈ 0.93, prohibited-claim false positives 1 → 0.
- Measured: 2026-05-22.

## Gate verdict: **PASS**

The LLM-assisted fact judge clears the Phase-1 gate on the expanded 147-entry
gold set. All gate criteria hold (§5). Jobs C3-01…C3-04 stand; Phase 2
(retrieval / coverage — jobs C3-06…C3-08) may proceed.

One-line result: LLM-judge agreement mean **97.96 %** (lowest 97.28 %, spread
1.36 pp), precision mean **0.9880** (lowest 0.9821), recall mean **0.9850**
(lowest 0.9730), 0 provider fallbacks in all three runs; the job-09 re-judge
produces **0** prohibited-claim findings on all seven gate IDs (and 0 across the
whole 270-question run).

## 1. Rule-only calibration (reference)

```
python3 evals/altibase_answerability/scripts/calibrate_judge.py \
  --gold evals/altibase_answerability/fixtures/judge_gold_set.jsonl
```

| Metric | Value |
| --- | ---: |
| Agreement | 82.31 % (121/147) |
| Precision (positive class = `covered`) | 0.8346 |
| Recall | 0.9550 |
| F1 | 0.8908 |
| Confusion (TP / FP / FN / TN) | 106 / 21 / 5 / 15 |

The deterministic rule judge's error profile on the expanded set is **21 false
positives** (over-credits) and **5 false negatives** (under-credits) — 26
disagreements in all. The 95 new entries (job C3-02) are all paraphrase-suspect
by construction (`term_score` in `[0.40, 1.00]`), so the rule judge's raw
agreement is necessarily lower than on the old set; closing that gap is exactly
the LLM judge's job.

Rule-only disagreements (26):

- **FP (21)**: OPS-110 F01, OPS-110 F04, OPS-115 F04, PROP-147 F01,
  REPL-106 F03, REPL-106 F04, REPL-116 F01, SQL-101 F01, SQL-102 F03,
  SQL-102 F05, SQL-104 F02, SQL-105 F02, SQL-129 F01, SQL-129 F02,
  SQL-129 F03, TOOL-001 F04, TOOL-002 F04, TOOL-032 F03, TOOL-038 F03,
  VPM-127 F02, VPM-128 F01.
- **FN (5)**: PROP-147 F03, REPL-109 F01, TOOL-001 F03, TOOL-041 F01,
  VPM-123 F01.

## 2. LLM-assisted fact judge — three runs, fresh cache each

Three independent runs, each with a **fresh empty verdict cache**, default
`JUDGE_LLM_FACT_VOTES=3`. The live Codex CLI command provider
(`codex_exec_provider.sh`) was confirmed usable before the runs and was healthy
throughout: **141 in-band facts, 423 provider calls, 0 cache hits, 0 fallbacks**
per run — every in-band verdict is a genuine LLM majority vote, none fell back
to the rule judge.

```
for i in 1 2 3; do
  python3 evals/altibase_answerability/scripts/calibrate_judge.py \
    --gold evals/altibase_answerability/fixtures/judge_gold_set.jsonl \
    --llm-fact-judge \
    --llm-fact-judge-cache /tmp/altibase-c3-05-cache-$i.json
done
```

| Run | Agreement | Precision | Recall | F1 | TP / FP / FN / TN | overrides |
| --- | ---: | ---: | ---: | ---: | :---: | ---: |
| 1 | 98.64 % (145/147) | 0.9910 | 0.9910 | 0.9910 | 110 / 1 / 1 / 35 | 26 |
| 2 | 97.28 % (143/147) | 0.9908 | 0.9730 | 0.9818 | 108 / 1 / 3 / 35 | 28 |
| 3 | 97.96 % (144/147) | 0.9821 | 0.9910 | 0.9865 | 110 / 2 / 1 / 34 | 27 |
| **mean** | **97.96 %** | **0.9880** | **0.9850** | **0.9864** | — | — |
| **lowest** | **97.28 %** | **0.9821** | **0.9730** | — | — | — |

Three-run spread: agreement **1.36 pp** (97.28 %–98.64 %) — well inside the
"too flaky to gate on" threshold (lowest must be ≥ 88 %; it is 97.28 %).

Raw JSON: `evals/altibase_answerability/improvement3/logs/c3-05/run-{1,2,3}.report.json`
(git-ignored runtime output); per-run stdout alongside as `run-{1,2,3}.stdout.txt`.

The LLM judge lifts agreement 82.31 % → 97.96 % mean and precision
0.8346 → 0.9880: it corrects 25 of the rule judge's 26 disagreements every run
(all but REPL-106 F04) and, in voting, occasionally re-grades a borderline
compound fact — the residual disagreements below.

## 3. Per-disagreement breakdown

### 3a. Steady-state disagreements (present in all three runs)

| Question / fact | Type | Note |
| --- | :---: | --- |
| REPL-106 F04 | FP | Fact: `DROP TABLE` removes a table from replication, but if master/meta logs for the target remain in the replication gap the gap is given up and data mismatch can occur. The answer is an `ALTER REPLICATION` runbook that mentions `DROP TABLE` but omits the gap-given-up / data-mismatch risk that is the fact's substantive point. A genuine over-credit — the lone survivor of the rule judge's 21, unchanged from the cycle-2 steady state. |
| REPL-108 F04 | FN | Compound fact: `PARALLEL` creates multiple appliers + improves performance + distributes received XLogs by transaction + commit-sync caveat. The answer conveys roughly half (it frames `GAPLESS`/`PARALLEL` as LAZY-mode features and explains `GAPLESS` in depth). The gold `covered` label is generous; `not_covered` is defensible. Unchanged from the cycle-2 steady state. |

These are exactly the same two borderline gold entries that were the cycle-2
steady-state residual — the expansion to 147 entries added no new systematic
judge error.

### 3b. Vote-split flakiness (each in exactly one run)

| Question / fact | Run | Type | Note |
| --- | :---: | :---: | --- |
| SQL-120 F02 | 2 | FN | Fact: except for a RECORD-type variable, the variable count must match the returned-expression count and types must be compatible. The answer states the count must match (`expressions after RETURNING` = `host variables after INTO`) but not the RECORD-type exception or type compatibility. Borderline; a 2-1 vote split that landed `not_covered` in run 2, `covered` in runs 1/3. |
| VPM-101 F01 | 2 | FN | Fact: use `V$TABLE` to verify a performance view exists and inspect `NAME`/`COLUMNCOUNT`. The answer queries `V$TABLE` to "check the installed layout" and "inspect its existence/columns" but does not name the `NAME`/`COLUMNCOUNT` columns. 2-1 vote split. |
| VPM-123 F02 | 3 | FP | Fact: the Monitoring API can retrieve statistics, session count, max client count, session-lock and waiting-event information. The answer describes the API generically (same status information as meta tables / performance views) without enumerating those categories. 2-1 vote split that landed `covered` in run 3. |

Each flakiness entry appears in only one of the three runs; together they
account for the entire 1.36 pp spread. Majority-of-3 voting contains, but does
not fully eliminate, the per-fact non-determinism on genuinely borderline
compound/enumeration facts — consistent with the cycle-2 observation that a
gold set cannot resolve a judge much past the high-90s.

## 4. Prohibited-claim re-check (job-09 re-judge)

The cycle-2 job-09 full run
(`reports/full_benchmark/runs/altibase_source_preserving_20260521_220915_job09`,
270 questions) was re-judged end to end with the current `judge_report.py`
(rule judge; the C3-01 ERR-101 quoted-span fix lives in the rule polarity
guard). Output: `evals/altibase_answerability/improvement3/logs/c3-05/job09-rejudge/`.

| Question | Prohibited claims checked | Findings (`present`) |
| --- | :---: | :---: |
| ERR-101 | 2 | 0 |
| PROP-140 | 2 | 0 |
| PROP-142 | 2 | 0 |
| SQL-137 | 2 | 0 |
| TOOL-003 | 2 | 0 |
| TOOL-019 | 2 | 0 |
| TOOL-033 | 2 | 0 |

**0** prohibited-claim findings on all seven gate IDs, and **0** prohibited-claim
findings anywhere in the 270-question run. The C3-01 ERR-101 quoted-span fix
holds end to end.

## 5. Gate criteria

| Criterion | Target | Measured | Verdict |
| --- | --- | --- | :---: |
| LLM-judge agreement — mean of 3 runs (expanded set) | ≥ 90.0 % | 97.96 % | **PASS** |
| LLM-judge agreement — lowest of 3 runs | ≥ 88.0 % | 97.28 % | **PASS** |
| Three-run spread not a flakiness stop signal | lowest not well under 88 % | lowest 97.28 %, spread 1.36 pp | **PASS** |
| Precision — no real drop (every run ≥ 0.90) | ≥ 0.90 | 0.9910 / 0.9908 / 0.9821 | **PASS** |
| Recall — no real drop (every run ≥ 0.90) | ≥ 0.90 | 0.9910 / 0.9730 / 0.9910 | **PASS** |
| Precision/recall vs cycle-2 steady state | no material regression | precision 0.966 → 0.988 mean, recall ≈0.93 → 0.985 mean (both up) | **PASS** |
| Job-09 re-judge prohibited-claim findings on the 7 IDs | 0 | 0 (and 0 across all 270) | **PASS** |

Precision and recall did not regress versus the cycle-2 steady state — both
improved on the larger, harder gold set. `judge_report.py --self-test` passes;
`git diff --check` is clean.

**All gate criteria pass. The Phase-1 gate is met.**

## 6. Outcome

- Gate verdict: **PASS**.
- Jobs C3-01 (ERR-101 quoted-span fix), C3-02 (expanded gold set),
  C3-03 (enlarged coding-agent suite) and C3-04 (multi-sample variance band)
  stand — none required revision.
- The judge's residual error is two long-standing borderline gold entries
  (REPL-106 F04, REPL-108 F04) plus occasional 2-1 vote flakiness on
  borderline compound facts — not a systematic defect, and unchanged in
  character from cycle 2.
- The cycle-3 runner may proceed to Phase 2 (retrieval / coverage —
  C3-06…C3-08).

Operational note: on the expanded 147-entry set the LLM judge makes 423
provider calls per run (141 in-band facts × 3 votes), ~3× the cycle-2 cost.
`JUDGE_LLM_FACT_VOTES` can be tuned down for the long Phase-3 live runs if
provider time becomes a constraint; 3 remains the default for gate-grade
stability.
