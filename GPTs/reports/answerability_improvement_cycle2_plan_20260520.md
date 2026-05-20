# Altibase Answerability Test Harness — Improvement Plan, Cycle 2

- Date: 2026-05-20
- Repository: `/home/et16/AltibaseDocuments`
- Scope: `evals/altibase_answerability/` test harness only. No changes to
  `GPTs/upload_package/` source bodies.
- Cycle-1 plan: `GPTs/reports/test_harness_improvement_plan_20260520.md`
- Cycle-1 outcome: `evals/altibase_answerability/reports/full_rerun_analysis_20260520.md`
- Baseline runs (cycle-2 "before"):
  - `altibase_source_preserving_20260520_195639_job11` — full, 37/270 (13.7%)
  - `altibase_coding_agent_20260520_195650_job11` — coding-agent, 2/10 (20%)

## Why this cycle exists

Cycle 1 made the measuring instrument trustworthy and turned on manifest-aware
retrieval: pass rate 5.2% → 13.7% (full) and 0% → 20% (coding-agent),
judge-vs-gold agreement 61.5% → 75.0%, routed-source-in-context 0% → 100%. It
did not reach the 85% readiness threshold, and was not expected to.

The cycle-1 regression analysis (`full_rerun_analysis_20260520.md` §6) left five
remediation targets. Cycle 2 addresses them in the same order cycle 1 used —
**judge validity first** (a measurement you cannot trust cannot guide retrieval
work), **then retrieval/coverage**.

### The five carried-over targets

1. Judge prohibited-claim false positives — count rose 2 → 6, each one blocks an
   otherwise-passing question. Polarity-, direction-, and markdown-emphasis
   blind spots remain.
2. Judge-vs-gold agreement 75% < 90% target — 11 over-credits concentrated in
   SQL paraphrase-suspect facts that bag-of-words cannot adjudicate.
3. `properties` domain — 2.0% pass, 32 version-sensitive-property blockers,
   required-token preservation ≈ 50%.
4. Self-reported context gaps still 30%; required-token-in-context 72.6%.
5. `errors_troubleshooting` and `views_performance_monitoring` — lowest
   critical-fact coverage and token preservation after `properties`.

Plus one tooling defect: `judge_report.py --retrieval-recall` rebuilds context
without the job-08/09 manifest arguments and under-reports recall for routed
runs.

## Decisions for this cycle

- **Sequencing:** judge first, then retrieval/coverage. (Confirmed.)
- **The LLM-assisted fact judge (T7-B) is IN scope.** The deterministic rule
  judge stays the default and the fallback; the LLM judge adjudicates only the
  paraphrase-suspect band. 90% judge-vs-gold agreement is a **hard Phase-1
  gate** — Phase 2 does not start until it is met.
- **Targets:** judge agreement ≥ 90% (gated). Pass rate is expected to reach an
  intermediate **~35–45%**, not 85%. 85% readiness remains a later-cycle goal.

## Phase 1 — Judge validity (gate: gold-set agreement ≥ 90%)

- **C2-01 — Prohibited-claim false-positive fix, round 2.** Make
  `prohibited_claim_present()` polarity- and direction-aware; strip markdown
  emphasis before negation tokenisation; generalise the `cannot`-phrased
  intrinsically-negative guard. Add PROP-140, PROP-142, SQL-137, TOOL-003,
  TOOL-019, TOOL-033 as self-test fixtures.
- **C2-02 — LLM-assisted fact judge (T7-B).** Add an optional LLM fact-judge
  mode to `judge_report.py` that adjudicates only paraphrase-suspect facts; rule
  judge stays default and fallback. `fact_match(...).covered` interface stays
  stable; `calibrate_judge.py` gains an opt-in flag to exercise it.
- **C2-03 — `--retrieval-recall` manifest fix.** Pass the job-08/09
  manifest/shard arguments into `build_context()` so the diagnostic reconstructs
  the routed context faithfully.
- **C2-04 — Judge re-calibration gate.** Run `calibrate_judge.py` with the LLM
  judge enabled against the 52-entry gold set, three times with a fresh cache.
  Gate: mean agreement ≥ 90% and lowest ≥ 88%, precision ≥ 0.711 (no
  regression). Writes the gate decision record.

The LLM fact judge is reached by benchmark runs through the `JUDGE_LLM_FACT=1`
environment toggle (`run-test.sh` passes `judge_report.py` a fixed argument
list and takes no judge flag). The live command provider is therefore needed
from C2-02/C2-04 onward, not only in Phase 3. The 52-entry gold set is small;
expanding it is noted as cycle-3 work.

## Phase 2 — Retrieval / coverage

- **C2-05 — Router scoring tuning for under-specified questions.** Tighten
  `route_sources()` scoring so vaguely worded questions still route correctly;
  raise required-token-in-context above 72.6%.
- **C2-06 — `properties` domain deep-dive.** Determine whether the routed
  property sources actually carry the version-specific facts the questions need;
  fix routing/coverage where the facts exist, and document any genuine
  source-content gap (out of harness scope) plainly.
- **C2-07 — `errors_troubleshooting` / `views_performance_monitoring`
  coverage.** Raise critical-fact coverage and token preservation for the two
  weakest remaining domains.

## Phase 3 — Validation (LIVE)

- **C2-08 — Targeted calibration run (stop/go gate).** Live targeted run over
  the six prohibited-claim questions, a sample of `properties` /
  `errors_troubleshooting` / `views_performance_monitoring` questions, and the
  coding-agent suite. Fails on purpose if the targeted set does not improve.
- **C2-09 — Full re-run and regression analysis.** Live 270 + 10 run; three
  separate scorecards versus the job-11 baseline.

## Phase 4 — Documentation

- **C2-10 — Harness documentation update.** Bring the harness docs in line with
  the LLM fact judge, the round-2 prohibited-claim logic, and the
  `--retrieval-recall` fix.

## Acceptance — three separate scorecards

As in cycle 1, the run is judged on three scorecards reported separately, never
collapsed into one number:

- **Retrieval** — routed-source-in-context, required-token-in-context, share of
  answers self-reporting missing context.
- **Judge validity** — judge-vs-gold agreement (must be ≥ 90% this cycle),
  precision/recall, prohibited-claim false-positive count.
- **Pass rate** — pass rate, gained/lost question IDs, critical-fact coverage,
  required-token preservation, protected-topic blockers, genuine prohibited
  claims.

Cycle 2 passes when the judge-validity gate (≥ 90% agreement) is met, the
retrieval scorecard improves, the pass rate improves, and no genuine prohibited
claim is added.
