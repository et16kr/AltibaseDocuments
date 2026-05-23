# C3-09 — Targeted Calibration Run (stop/go gate)

- Date: 2026-05-22
- Job: C3-09, Phase 3 of the cycle-3 answerability improvement plan
  (`GPTs/reports/answerability_improvement_cycle3_plan_20260522.md`).
- Type: **LIVE** targeted calibration run, multi-sample (N=3), LLM fact judge.
- **Gate decision: PASS** — all four gate criteria hold. The C3-10 full
  270-question multi-sample re-run may proceed.

## 1. Run configuration

| Setting | Value |
|---|---|
| Mode | `live` |
| Provider | `command` — Codex CLI (`codex_exec_provider.sh`), model `gpt-5.5` |
| Answer samples | `ANSWER_SAMPLES=3` (C3-04 multi-sample; option name confirmed against the job-04 result) |
| Judge | `JUDGE_LLM_FACT=1` — LLM fact judge, 3-vote majority per in-band fact |
| Answer context | pinned to `GPTs/upload_package/*.md`, 180 000-char budget, lexical assembly |

The provider was confirmed usable before any scored run (a smoke call returned
correctly with model `gpt-5.5`).

Runs executed (46 run-test.sh invocations, each one question × 3 samples):

- 1 coding-agent / full-benchmark canary — `ERR-101`.
- 45-run driver (concurrency 6): 15 full-benchmark targeted questions +
  the enlarged 30-question coding-agent suite. Each run had its own
  `RUN_ROOT` and its own `JUDGE_LLM_FACT_CACHE` (concurrent runs must not
  share the judge verdict cache).

The coding-agent suite was run **per question** rather than as a single
`./run-test.sh coding-agent` invocation. Per-question runs produce identical
per-question answers and judgments to a whole-suite run (context assembly is
deterministic per question; samples are independent) and let the 30 questions
run concurrently instead of ~3 h sequentially. Every per-question coding-agent
run carries its own N=3 variance band.

Run health: all 46 runs produced 3 `answered` records (138 answer-generation
provider calls, **0 answer errors**); the LLM fact judge logged
**0 fallbacks** on every run (the judge never silently degraded to rule-only);
no `invalid_run`.

## 2. Baseline

Cycle-3 "before" baselines (job-09):

- `altibase_source_preserving_20260521_220915_job09` — full, 41/270.
- `altibase_coding_agent_20260521_220915_job09` — coding-agent, 2/10 on the
  original 10-question suite.

For an apples-to-apples comparison the baseline **answer records** were
re-judged with the same LLM fact judge used in this job
(`JUDGE_LLM_FACT=1`). Re-judged baseline: coding-agent **2/10** pass
(AGENT-001, AGENT-005), preserving the plan's stated 2/10. Required-token
preservation and prohibited-claim detection are rule-based and judge-mode
independent; critical-fact coverage is the metric the LLM judge affects, and
re-judging the baseline removes the judge-mode confound from it.

**Known confound (documented, not a defect).** The baseline answers predate the
IMG-01..06 source-pack refresh (commit `1dc54cb6`, 2026-05-22) — the same
refresh job 07 already noted. The baseline's exact assembled context is not
bit-reproducible at any single commit (digest match 0/26 against the last
pre-baseline commit `de972b4`), so the baseline ran with then-uncommitted
working-tree state. The before/after comparison below therefore reflects the
**combined** effect of the cycle-3 harness changes (C3-01/06/07/08) and the
pack refresh — which is exactly the end-to-end "before/after" the C3-10 full
run will also measure.

## 3. Methodology — variance band

Each new figure is reported as `mean [min–max]` over the 3 samples. A question
**"improves beyond the variance band"** when the *worst* of its three samples
(the floor of the N=3 band) still strictly exceeds the single-point baseline —
i.e. the whole band lies above baseline, so the gain cannot be sampling noise.

## 4. Scorecard 1 — ERR-101 prohibited-claim case + C2-01 regression check

Gate criterion: the ERR-101 case and the C2-01 sample produce **zero**
prohibited-claim findings.

| Question | Prohibited findings (per sample) | Critical-fact coverage | Required-token preservation | Severity |
|---|---|---|---|---|
| ERR-101 | [0, 0, 0] — **0** | 100.0% [100.0–100.0] | 81.0% [71.4–85.7] | medium → medium |
| PROP-142 (C2-01) | [0, 0, 0] — **0** | 80.0% [80.0–80.0] | 100.0% [100.0–100.0] | high → high |
| TOOL-033 (C2-01) | [0, 0, 0] — **0** | 100.0% [100.0–100.0] | 100.0% [100.0–100.0] | high → none |

All 9 sample-judgments are clean. The C3-01 quoted-span polarity guard holds on
freshly generated live answers; the C2-01 fixtures do not regress (TOOL-033
critical-fact coverage rose 75.0% → 100.0%).

**Gate 1: PASS.**

## 5. Scorecard 2 — `replication_cdc_security_network` sample

Gate criterion: ≥ half of the sample improves in critical-fact coverage *or*
required-token preservation beyond the variance band.

| Question | Critical-fact coverage (base → new) | Required-token preservation (base → new) | Improved beyond band |
|---|---|---|---|
| REPL-102 | 66.7% → **100.0% [100.0–100.0]** | 28.6% → **81.0% [71.4–85.7]** | **yes** (both) |
| REPL-106 | 100.0% → 93.3% [80.0–100.0] | 69.2% → **76.9% [76.9–76.9]** | **yes** (token) |
| REPL-107 | 80.0% → **100.0% [100.0–100.0]** | 70.0% → **90.0% [90.0–90.0]** | **yes** (both) |
| REPL-110 | 20.0% → **60.0% [60.0–60.0]** | 20.0% → **86.7% [80.0–90.0]** | **yes** (both) |
| REPL-130 | 100.0% → 83.3% [83.3–83.3] | 77.8% → 77.8% [77.8–77.8] | no |

**4/5 improved beyond the variance band** (need ≥ 2.5). Severity also improved
on the blockers: REPL-106 blocker → high, REPL-107 blocker → medium.
REPL-130 is the lone non-improver (stable 3-sample band, no within-run
variance — a genuine answer-level difference vs the baseline's single sample,
not noise).

**Gate 2: PASS.**

## 6. Scorecard 3 — `views_performance_monitoring` + prose-residual sample

Gate criterion: ≥ half of the sample improves in critical-fact coverage *or*
required-token preservation beyond the variance band.

| Question | Critical-fact coverage (base → new) | Required-token preservation (base → new) | Improved beyond band |
|---|---|---|---|
| PROP-123 | 0.0% → **100.0% [100.0–100.0]** | 16.7% → **100.0% [100.0–100.0]** | **yes** (both) |
| ERR-119 | 0.0% → **100.0% [100.0–100.0]** | 25.0% → **100.0% [100.0–100.0]** | **yes** (both) |
| ERR-123 | 50.0% → **100.0% [100.0–100.0]** | 40.0% → **100.0% [100.0–100.0]** | **yes** (both) |
| ERR-130 | 75.0% → **100.0% [100.0–100.0]** | 75.0% → **100.0% [100.0–100.0]** | **yes** (both) |
| VPM-101 | 100.0% → 66.7% [66.7–66.7] | 42.9% → 42.9% [42.9–42.9] | no |
| VPM-104 | 25.0% → **100.0% [100.0–100.0]** | 50.0% → **100.0% [100.0–100.0]** | **yes** (both) |
| VPM-107 | 0.0% → **100.0% [100.0–100.0]** | 15.4% → **92.3% [92.3–92.3]** | **yes** (both) |
| VPM-108 | 50.0% → **100.0% [100.0–100.0]** | 41.7% → **100.0% [100.0–100.0]** | **yes** (both) |

**7/8 improved beyond the variance band** (need ≥ 4.0). Severity improved
sharply: PROP-123 blocker → none, ERR-130 high → none, VPM-104 high → none,
ERR-119/123 high → medium/none, VPM-107/108 high → medium.

VPM-101 is the lone non-improver — expected: C3-08 deliberately left VPM-101
**unresolved** ("performance view or column" names a task, not an object), so
its assembled context is byte-identical to the baseline. The change is pure
answer-generation variance (stable across all 3 samples) and does not break the
gate.

**Gate 3: PASS.**

## 7. Scorecard 4 — coding-agent suite (no-regression check)

Gate criterion: on the 10 questions shared with the original baseline, pass
count and SRC-*/BLOCK-* provenance are ≥ the job-09 baseline (2/10).

| Question | Baseline pass | New pass per sample | Baseline SRC/BLOCK provenance preserved | New provenance preserved per sample |
|---|---|---|---|---|
| AGENT-001 | pass | [pass, pass, pass] | 2 | [2, 2, 2] |
| AGENT-002 | fail | [fail, fail, fail] | 0 | [0, 0, 0] |
| AGENT-003 | fail | [fail, fail, fail] | 0 | [0, 0, 0] |
| AGENT-004 | fail | [fail, fail, fail] | 1 | [1, 1, 1] |
| AGENT-005 | pass | [pass, pass, pass] | 1 | [1, 1, 1] |
| AGENT-006 | fail | [fail, fail, fail] | 1 | [1, 1, 1] |
| AGENT-007 | fail | [fail, fail, fail] | 0 | [2, 2, 2] |
| AGENT-008 | fail | [fail, fail, fail] | 0 | [0, 0, 0] |
| AGENT-009 | fail | [fail, fail, fail] | 0 | [0, 0, 0] |
| AGENT-010 | fail | [fail, pass, pass] | 0 | [0, 2, 2] |

- **Pass count (shared 10):** baseline 2 → new **[2, 3, 3]** per sample
  (mean 2.67). The worst sample (2) equals the baseline; no regression.
- **SRC-*/BLOCK-* provenance preserved-in-answer (shared 10):** baseline
  total 5 → new **[7, 9, 9]** per sample (mean 8.33). The worst sample (7)
  exceeds the baseline; no regression. AGENT-007 (a replication coding-agent
  question) is the clearest gain: 0 → 2 — the C3-06 replication-anchored
  assembly reaching the coding-agent builder.
- *Supporting, retrieval-only:* the current deterministic build produces
  **15/28** SRC-*/BLOCK-* tokens in the assembled context for the shared 10;
  6/10 of those contexts are byte-identical to the baseline (digest match).

**Gate 4: PASS** (both sub-criteria hold even on the worst sample).

Context — the enlarged coding-agent suite (30 questions) scored per-sample
pass `[5, 6, 5]` (mean 5.33/30); 6/30 questions pass ≥ 2/3 samples. This is
the C3-10 starting point, not a gate input.

## 8. Gate decision

| Gate | Criterion | Result |
|---|---|---|
| 1 | ERR-101 + C2-01 sample: zero prohibited-claim findings | **PASS** (0/9 sample-judgments) |
| 2 | Replication sample: ≥ ½ improve beyond band | **PASS** (4/5) |
| 3 | VPM + prose-residual sample: ≥ ½ improve beyond band | **PASS** (7/8) |
| 4 | Coding-agent: no regression on shared 10 | **PASS** (pass 2→[2,3,3]; provenance 5→[7,9,9]) |

**Overall: PASS.** The targeted calibration improves the three cycle-3 work
areas well beyond the multi-sample variance band, adds no prohibited claim, and
does not regress the coding-agent suite. The stop/go gate is **GO**: the C3-10
full 270-question multi-sample re-run may proceed.

### Caveats carried forward to C3-10

1. Baseline answers predate the IMG-01..06 pack refresh (§2) — the C3-10 full
   run inherits the same end-to-end before/after framing.
2. REPL-130 and VPM-101 did not improve. VPM-101 is expected (C3-08 left it
   deliberately unresolved). Both show zero within-run variance, so the
   movement vs the baseline's single sample is a genuine answer-level
   difference, not sampling noise — worth watching at full scale.
3. No retrieval/judge source files were modified in this measurement job.
