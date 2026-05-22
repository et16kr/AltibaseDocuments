# Altibase Answerability Test Harness — Improvement Plan, Cycle 3

- Date: 2026-05-22
- Repository: `/home/et16/AltibaseDocuments`
- Scope: `evals/altibase_answerability/` test harness only — including its
  question sets under `evals/altibase_answerability/questions/`. No changes to
  `GPTs/upload_package/` source bodies.
- Cycle-2 plan: `GPTs/reports/answerability_improvement_cycle2_plan_20260520.md`
- Cycle-2 outcome: `evals/altibase_answerability/reports/full_rerun_analysis_cycle2_20260520.md`
- Baseline runs (cycle-3 "before"):
  - `altibase_source_preserving_20260521_220915_job09` — full, 41/270 (15.2%)
  - `altibase_coding_agent_20260521_220915_job09` — coding-agent, 2/10 (20%)

## Why this cycle exists

Cycle 2 met its acceptance: judge-vs-gold agreement 75.0% → 96.15% (the ≥90%
gate held), precision 0.711 → 0.966, prohibited-claim false positives 6 → 1,
required-token-in-context +8.5 pp, full pass rate 13.7% → 15.2%.

The headline pass rate moved far less than cycle 2's projected 35–45%. The
cycle-2 regression analysis (`full_rerun_analysis_cycle2_20260520.md` §6)
explains why and leaves five remediation targets. Two of them are *measurement*
problems that mask genuine coverage gains, not coverage problems:

- The cycle-2 retrieval/answer track gained **+10** questions against a
  deliberately stricter judge, but **11 losses were pure live answer-generation
  variance** — net movement was small because the noise floor is as large as
  the signal.
- The LLM judge correctly withdrew rule-judge over-credits, so pass-rate growth
  must now come from *genuine* coverage; the instrument no longer inflates it.

Cycle 3 therefore sequences **measurement validity first** (tighten the judge's
last false positive, expand the gold set, and damp answer-generation variance so
real gains are visible), **then retrieval/coverage** on the two domains that are
now worst.

### The five carried-over targets

1. Residual prohibited-claim false positive (ERR-101) — a `cannot`-phrased
   claim still mis-fires when an unrelated literal negation sits inside a quoted
   code/example span.
2. `views_performance_monitoring` and `replication_cdc_security_network` are now
   the worst domains (10.0% pass each). Replication had no dedicated cycle-2
   builder; VPM coverage rose under C2-07 but few questions cross the threshold.
3. Live answer-generation variance dominates the small movements.
4. The 52-entry judge gold set is small; both residual disagreements are
   borderline labels on it.
5. The 10-question coding-agent suite is too coarse to register coverage gains
   (critical-fact coverage +16.7 pp showed no pass-rate movement).

## Decisions for this cycle

- **Sequencing:** measurement validity first, then retrieval/coverage, then live
  validation. (Same discipline as cycles 1–2.)
- **Variance handling — both levers (confirmed).** Multi-sample answer
  generation stabilises the live runs, *and* the scorecard reports an explicit
  variance band so retrieval/answer gains are never masked by noise.
- **Gold set expands 52 → ~150 (confirmed).** Domain-balanced and audited; the
  ≥90% agreement gate is re-verified on the larger set.
- **Targets:** judge agreement ≥ 90% on the expanded gold set (gated). Pass rate
  is expected to reach an intermediate **~25–35%** — the judge is now calibrated,
  so growth is genuine coverage only, and the headline is capped by live
  variance until C3-04 lands. 85% readiness remains a later-cycle goal.

## Phase 1 — Measurement validity (gate: agreement ≥ 90% on the expanded gold set)

- **C3-01 — ERR-101 residual prohibited-claim false-positive fix.** Generalise
  the C2-01 polarity guard so negation tokens inside quoted code/example spans
  (e.g. `altierr -w "does not"`) do not flip a `cannot`-phrased claim's verdict.
  Add ERR-101 as a self-test fixture; keep all six C2-01 fixtures green.
- **C3-02 — Expand and audit the judge gold set (52 → ~150).** Add gold entries
  to `fixtures/judge_gold_set.jsonl`, domain-balanced across all seven domains,
  with priority on the paraphrase-suspect band and the borderline labels
  (REPL-106 F04, REPL-108 F04 re-audited). Document the labelling rationale.
- **C3-03 — Enlarge the coding-agent question suite.** Grow the 10-question
  coding-agent set so coverage gains register as pass-rate movement; new
  questions must be answerable from `GPTs/upload_package/` and follow the
  existing schema. No source bodies are edited.
- **C3-04 — Multi-sample answer generation + scorecard variance band.** Add an
  optional N-sample answer mode to `answer_runner.py` (default N=1; cycle-3
  runs use N=3) and report a variance band in the scorecard so retrieval/answer
  gains are separated from the noise floor. Deterministic single-sample
  behaviour stays the default and the self-test path.
- **C3-05 — Judge re-calibration gate (LIVE).** Run `calibrate_judge.py` with
  the LLM judge against the expanded gold set, three times with a fresh cache.
  Gate: mean agreement ≥ 90% and lowest ≥ 88%, precision/recall ≥ cycle-2
  steady-state (no regression). Writes the gate decision record. Phase 2 does
  not start until this gate is met.

## Phase 2 — Retrieval / coverage

- **C3-06 — `replication_cdc_security_network` identifier-anchored assembly.**
  Apply the C2-06/07 named-definition admission pattern to replication objects
  (replication clauses, `REPLICATION_*` properties, security/network meta-tables
  and views). `build_context()` only; byte-identical for non-replication
  questions.
- **C3-07 — `views_performance_monitoring` residual coverage.** Resolve the
  C2-07 VPM residuals: out-of-mechanism-scope manuals (Performance Tuning Guide,
  Monitoring API Guide) and the question-phrasing residuals C2-07 listed.
- **C3-08 — Prose-named identifier resolution.** Many residuals (PROP-123,
  ERR-117/119/120/123/130, VPM-101/103/104/106/107/108) name the
  property/error/view in prose, not as the identifier the C2-06/07 builders
  anchor on. Add a prose→identifier resolution step so the named-definition
  sections can still fire.

## Phase 3 — Validation (LIVE)

- **C3-09 — Targeted calibration run (stop/go gate).** Live targeted run over
  the ERR-101 prohibited-claim case, a sample of `replication_cdc` /
  `views_performance_monitoring` questions, and the enlarged coding-agent suite.
  Multi-sample (N=3). Fails on purpose if the targeted set does not improve.
- **C3-10 — Full re-run and regression analysis.** Live 270 + enlarged
  coding-agent run, multi-sample (N=3); three separate scorecards versus the
  job-09 baseline, each with its variance band.

## Phase 4 — Documentation

- **C3-11 — Harness documentation update.** Bring the harness docs in line with
  the quoted-span polarity guard, the expanded gold set, multi-sample answer
  generation and the scorecard variance band, and the replication /
  prose-identifier assembly additions.

## Acceptance — three separate scorecards

As in cycles 1–2, the run is judged on three scorecards reported separately,
never collapsed into one number, and each retrieval/pass-rate figure now carries
its variance band:

- **Retrieval** — routed-source-in-context, required-token-in-context, share of
  answers self-reporting missing context.
- **Judge validity** — judge-vs-gold agreement (≥ 90% on the expanded gold set),
  precision/recall, prohibited-claim false-positive count.
- **Pass rate** — pass rate with variance band, gained/lost question IDs,
  critical-fact coverage, required-token preservation, protected-topic blockers,
  genuine prohibited claims.

Cycle 3 passes when the judge-validity gate (≥ 90% agreement on the expanded
gold set) is met, the retrieval scorecard improves, the pass rate improves
beyond its variance band, and no genuine prohibited claim is added.
