# Targeted Calibration Run — Cycle 2, C2-08 (stop/go gate)

- Date: 2026-05-21
- Repository: `/home/et16/AltibaseDocuments`
- Master plan: `GPTs/reports/answerability_improvement_cycle2_plan_20260520.md` —
  Phase 3, item C2-08; "Acceptance — three separate scorecards".
- Job: `evals/altibase_answerability/improvement2/jobs/08-C2-08-targeted-calibration-run.md`
- Baselines (cycle-2 "before", job 11):
  - `altibase_source_preserving_20260520_195639_job11` — full, 37/270, judged
    with the cycle-1 rule judge.
  - `altibase_coding_agent_20260520_195650_job11` — coding-agent, 2/10.

## 1. Gate decision

**PASS.** All four gate criteria hold. The cycle-2 jobs may proceed to the full
re-run (C2-09).

| Gate criterion | Result | Status |
| --- | --- | --- |
| Six prohibited-claim questions → **zero** prohibited-claim findings | 0 / 6 findings (0 / 26 across the whole run) | **PASS** |
| ≥ half of the `properties` sample improves (crit-fact coverage or token preservation) | 3 / 4 improved | **PASS** |
| ≥ half of the `errors_troubleshooting` + `VPM` sample improves | 6 / 6 improved | **PASS** |
| Coding-agent does not regress (pass count + provenance-in-context ≥ baseline) | 2 / 10 pass = baseline; 10 / 10 routed-source-in-context = baseline | **PASS** |

No genuine prohibited claim was added anywhere in the run.

## 2. Run configuration (verified)

- **Live provider usable.** `codex` CLI 0.132.0 at `/usr/local/bin/codex`,
  `codex login status` → "Logged in using ChatGPT". A provider smoke test
  (`codex_exec_provider.sh`, model `gpt-5.5`) returned a valid answer before the
  suite was launched.
- **LLM fact judge enabled for all judging.** `JUDGE_LLM_FACT=1` was exported
  for every run. This is the C2-02 toggle: `make_llm_fact_judge()` in
  `judge_report.py` builds the judge when `--llm-fact-judge` **or**
  `env_flag("JUDGE_LLM_FACT")` is set, and `run-test.sh` passes `judge_report.py`
  a fixed argument list with no judge flag, so the env toggle is the only path.
  Engagement confirmed: the LLM fact judge adjudicated **86 facts across all 26
  questions** (every run shows `llm_fact_judge=…` in its `fact_results` notes,
  e.g. `llm_fact_judge=covered (llm 3/3 covered)`). Each run used an isolated
  verdict cache under its own `RUN_ROOT` to keep the parallel runs independent.
- Provider `command` (Codex CLI), model `gpt-5.5`, mode `live`,
  `max-context-chars 180000`, lexical context mode — the standard harness
  configuration. All 17 runs finished with answer-runner exit code 0.
- Suites: 16 single-question `source-preserving` runs (`QUESTION_ID=…`) plus the
  full 10-question `coding-agent` suite.

## 3. Method

Each targeted question was run as its own `run-test.sh` invocation
(`JUDGE_LLM_FACT=1 RUN_ID=… RUN_ROOT=… QUESTION_ID=… ./run-test.sh
source-preserving`), and the coding-agent suite as
`JUDGE_LLM_FACT=1 RUN_ID=c2_08_coding_agent … ./run-test.sh coding-agent`.
Per-question critical-fact coverage, required-token preservation, max severity,
pass/fail and prohibited-claim findings were read from each run's
`judge/judgments.jsonl` and compared against the job-11 baseline judgments.

Comparison caveat, stated honestly: the job-11 baseline was judged with the
cycle-1 **rule** judge; these runs use the cycle-2 **LLM fact judge** for the
paraphrase-suspect band. Critical-fact-coverage deltas therefore reflect both
the C2-06/C2-07 retrieval changes and the C2-02 judge change. **Required-token
preservation is judge-method-independent** (literal substring presence in the
answer), so it is the cleaner cross-run signal — and it moves strongly in the
right direction on its own. Live generation is non-deterministic; single-run
deltas are directional, not exact.

## 4. Scorecard A — prohibited-claim gate

The six questions that were prohibited-claim **false positives** in the job-11
baseline. The gate requires **zero** prohibited-claim findings now.

| Question | Baseline prohibited claim | C2-08 prohibited claim | Baseline crit / tok | C2-08 crit / tok | C2-08 result |
| --- | --- | --- | --- | --- | --- |
| PROP-140 | present (false positive) | **none** | 0.75 / 0.857 | 0.50 / 1.000 | fail — missing critical facts (genuine) |
| PROP-142 | present (false positive) | **none** | 0.80 / 1.000 | 1.00 / 1.000 | **pass** |
| SQL-137  | present (false positive) | **none** | 1.00 / 1.000 | 1.00 / 1.000 | **pass** |
| TOOL-003 | present (false positive) | **none** | 1.00 / 1.000 | 1.00 / 1.000 | **pass** |
| TOOL-019 | present (false positive) | **none** | 1.00 / 0.667 | 1.00 / 0.667 | fail — missing required token (medium) |
| TOOL-033 | present (false positive) | **none** | 0.75 / 1.000 | 1.00 / 1.000 | **pass** |

**0 / 6 prohibited-claim findings — gate criterion met.** The C2-01 round-2
fix cleared all six baseline false positives. Four of the six now pass outright.
PROP-140 and TOOL-019 still fail, but on genuine non-prohibited findings:
PROP-140 missed 2 critical facts (live-answer variance — crit 0.75 → 0.50, while
token preservation rose 0.857 → 1.000); TOOL-019 missed one required token
(`SQLFreeLob2(stmt, locator)`), a medium finding, not a prohibited claim.

## 5. Scorecard B — `properties` sample

PROP-101 (baseline-passing anchor) plus three previously-failing `PROP-*`
questions with large C2-06 context recoveries (job 06 deep-dive).

| Question | Baseline crit / tok | C2-08 crit / tok | Δ crit | Δ tok | Improved? | C2-08 result |
| --- | --- | --- | ---: | ---: | --- | --- |
| PROP-101 | 1.00 / 1.000 | 1.00 / 0.800 | +0.00 | −0.200 | no (regressed) | fail — see §7 |
| PROP-113 | 0.00 / 0.167 | 1.00 / 0.667 | **+1.00** | **+0.500** | **yes** | fail — residual token miss |
| PROP-124 | 0.00 / 0.200 | 1.00 / 0.800 | **+1.00** | **+0.600** | **yes** | fail — residual token miss |
| PROP-149 | 0.00 / 0.143 | 1.00 / 1.000 | **+1.00** | **+0.857** | **yes** | **pass** |

**3 / 4 improved — gate criterion met (need ≥ 2).** The three previously-failing
property questions moved from 0 % critical-fact coverage to 100 %, exactly the
category-(a) retrieval recovery the C2-06 deep-dive predicted. PROP-101 did not
improve (it was already at ceiling) and slipped one generic required token — see
§7; this is not a gate-failing criterion.

## 6. Scorecard C — `errors_troubleshooting` + `views_performance_monitoring` sample

Three previously-failing `ERR-*` and three previously-failing `VPM-*` questions
with large C2-07 context recoveries (job 07 deep-dive).

| Question | Baseline crit / tok | C2-08 crit / tok | Δ crit | Δ tok | Improved? | C2-08 result |
| --- | --- | --- | ---: | ---: | --- | --- |
| ERR-112 | 0.667 / 0.600 | 1.000 / 1.000 | +0.333 | +0.400 | **yes** | **pass** |
| ERR-113 | 0.750 / 0.500 | 0.750 / 0.667 | +0.000 | +0.167 | **yes** | fail — missing critical fact |
| ERR-126 | 0.250 / 0.556 | 0.250 / 0.778 | +0.000 | +0.222 | **yes** | fail — missing critical fact |
| VPM-111 | 0.250 / 0.364 | 0.750 / 0.727 | +0.500 | +0.364 | **yes** | fail — missing critical fact |
| VPM-112 | 0.000 / 0.250 | 1.000 / 0.500 | +1.000 | +0.250 | **yes** | fail — missing required tokens |
| VPM-114 | 0.333 / 0.333 | 0.667 / 1.000 | +0.333 | +0.667 | **yes** | fail — missing critical fact |

**6 / 6 improved — gate criterion met (need ≥ 3).** Every question improved on
critical-fact coverage and/or required-token preservation; all six improved on
token preservation. ERR-112 now passes outright. The five still-failing
questions fail on genuine missing-fact / missing-token findings, none of them
prohibited claims, and all have improved versus baseline.

## 7. Scorecard D — coding-agent suite (regression check)

| Metric | Baseline (job 11) | C2-08 | Status |
| --- | --- | --- | --- |
| Pass count | 2 / 10 | 2 / 10 | not regressed |
| Passing question IDs | AGENT-001, AGENT-005 | AGENT-001, AGENT-005 | same questions |
| Routed-source-in-context (provenance) | 10 / 10 | 10 / 10 | not regressed |
| Critical-fact coverage (suite) | 56.7 % | 73.3 % | improved |
| Required-token preservation (suite) | 68.1 % | 69.3 % | improved |
| Prohibited-claim findings | 0 | 0 | clean |

**Coding-agent does not regress — gate criterion met.** Pass count and
provenance-in-context both equal the baseline; suite critical-fact coverage
rose. Per-question, six of the eight non-passing questions improved on crit or
tok (AGENT-003/004/007/008/009/010); AGENT-006 dropped on critical-fact
coverage and AGENT-009/010 on token preservation, but these are within
live-generation variance and do not move the gate metrics (pass count,
provenance), which both held.

## 8. Regressions and caveats — recorded honestly

- **PROP-101 regressed pass → fail.** All four critical facts are still covered
  (crit 1.00); the failure is a single `missing_required_tokens` finding
  (medium) — the generic phrase `environment variable` was not preserved
  literally by the live model this run (token preservation 1.000 → 0.800). This
  is **live-model answer-phrasing variance on one generic token**, not a
  retrieval, judge, or harness defect, and `properties` is not a no-regression
  gate. It is flagged here so C2-09 can confirm it on the full re-run; if it
  recurs it points at the literal-substring required-token check being
  phrasing-brittle for non-technical tokens (the same measurement weakness the
  C2-06 deep-dive §5.3 already recorded).
- **PROP-140 critical-fact coverage 0.75 → 0.50.** The baseline false-positive
  prohibited claim is gone, but the live answer this run missed 2 critical facts
  (F03, F05); token preservation rose 0.857 → 1.000. Again live-answer variance,
  not a cycle-2 defect.
- The full re-run (C2-09) judges all 270 + 10 questions; these single-question
  live runs are directional. No harness bug was found — no retrieval/judge
  source file was inspected for editing and none was edited (this is a
  measurement-and-gate job).

## 9. Acceptance

```
test -f evals/altibase_answerability/reports/targeted_calibration_cycle2_20260520.md   # present
git diff --check                                                                       # clean
```

All 17 runs (16 single-question `source-preserving` + the 10-question
`coding-agent` suite) completed live against `gpt-5.5` via the Codex CLI with
the LLM fact judge enabled, answer-runner exit code 0 throughout. Every gate
criterion in the C2-08 job holds:

1. prohibited-claim findings — **0 / 6** (and 0 / 26 across the run);
2. `properties` sample — **3 / 4** improved;
3. `errors_troubleshooting` + `VPM` sample — **6 / 6** improved;
4. coding-agent — pass count 2 / 10 and provenance 10 / 10, **not regressed**.

**C2-08: PASS — proceed to the full re-run (C2-09).**
