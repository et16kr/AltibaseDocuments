# Job 10 — C3-10 Full re-run and regression analysis

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

This job runs the LIVE full benchmark, multi-sample (N=3), and can take a long
time (270 + the enlarged coding-agent suite, each ×3 samples). It is the final
measurement job of cycle 3.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Master plan: `GPTs/reports/answerability_improvement_cycle3_plan_20260522.md` —
  read "Acceptance — three separate scorecards" and the "Targets".
- Jobs 01–08 changed the harness; job 09 passed the targeted stop/go gate.
- Baselines (cycle-3 "before"): `altibase_source_preserving_20260521_220915_job09`
  (full, 41/270 = 15.2%) and `altibase_coding_agent_20260521_220915_job09`
  (coding-agent, 2/10 = 20% on the **original 10-question** suite). The cycle-2
  final analysis is
  `evals/altibase_answerability/reports/full_rerun_analysis_cycle2_20260520.md`.

## Task

1. Confirm the live provider is usable. If not, do NOT hang — write a FAIL
   result explaining what is missing.
2. **Enable the LLM fact judge** (`JUDGE_LLM_FACT=1`) and **multi-sample
   answer generation N=3** (`ANSWER_SAMPLES=3`) for both `run-test.sh`
   invocations. Confirm both toggles against the job-02/04/05 results.
3. Before spending the run, check whether a complete post-job-08 full
   multi-sample run already exists under
   `evals/altibase_answerability/reports/full_benchmark/runs/` and
   `.../coding_agent_source_preserving/runs/` (newer than job 09, N=3, valid
   `summary.txt`). If so, reuse it; otherwise run both suites. Long runs: start
   each in the background and poll for `summary.txt`.
   ```bash
   JUDGE_LLM_FACT=1 ANSWER_SAMPLES=3 ./run-test.sh source-preserving
   JUDGE_LLM_FACT=1 ANSWER_SAMPLES=3 ./run-test.sh coding-agent
   ```
4. Produce a regression analysis report at
   `evals/altibase_answerability/reports/full_rerun_analysis_cycle3_20260522.md`
   with **three separate scorecards** (never collapsed into one number), each
   retrieval/pass-rate figure carrying its **multi-sample variance band**:
   - **Retrieval scorecard:** routed-source-in-context rate,
     required-token-in-context rate, share of answers self-reporting missing
     context, coding-agent `SRC-*`/`BLOCK-*` in-context rate — versus the job-09
     baseline.
   - **Judge-validity scorecard:** judge-vs-gold agreement on the **expanded**
     gold set (`calibrate_judge.py --llm-fact-judge`), precision/recall,
     prohibited-claim false-positive count (must stay near zero — ERR-101 and
     the six C2-01 questions cleared).
   - **Pass-rate scorecard:** pass rate with variance band, gained/lost question
     IDs, critical-fact-coverage delta, required-token-preservation delta,
     protected-topic blocker delta, prohibited-claim count (genuine vs false
     positive).
5. **Coding-agent comparability.** The job-09 coding-agent baseline (2/10) is on
   the original 10 questions; C3-03 enlarged the suite. Report the enlarged-suite
   pass rate AND, for a like-for-like comparison, the pass rate restricted to the
   original 10 `AGENT-*` IDs.
6. Decompose the pass-rate movement into the judge track and the
   retrieval/answer track, and use the variance band to state which gains are
   real and which sit inside the noise floor (the cycle-2 report found 11 losses
   were pure answer-generation variance — the N=3 band exists to settle this).
7. State plainly whether each scorecard improved versus the job-09 baseline, and
   list the top remaining remediation targets for a possible cycle 4.

## Acceptance criteria for PASS

- Both suites completed (or a valid recent N=3 run was reused) and the analysis
  report exists with all three scorecards and variance bands.
- The judge-validity scorecard shows judge-vs-gold agreement **≥ 90%** on the
  expanded gold set (the cycle-3 gate, already met at job 05 — confirm it holds).
- The retrieval scorecard improved versus the job-09 baseline.
- The full pass rate improved **beyond its variance band** versus the job-09
  baseline (15.2% full). Reaching the 85% readiness threshold is NOT required;
  the plan's intermediate expectation is ~25–35%.
- No increase in genuine prohibited claims.

If the retrieval or judge-validity scorecard did not improve, or the pass-rate
gain does not clear its variance band, write a FAIL result so the cycle-3
changes can be inspected.

## Constraints (non-negotiable)

- Do not edit retrieval/judge source files in this job — it is measurement only.
- Do not touch `GPTs/upload_package/` source bodies.
- Keep answer-generation context pinned to `GPTs/upload_package/*.md`.
- Do not run `run-all.sh` or other jobs' files.

## Acceptance checks

```bash
test -f evals/altibase_answerability/reports/full_rerun_analysis_cycle3_20260522.md
git diff --check
```

## Completion protocol

As your final action:

- Ensure `evals/altibase_answerability/improvement3/state/` exists.
- If the runs completed and the acceptance criteria hold, write
  `evals/altibase_answerability/improvement3/state/10.result` with first line
  `PASS` and a short summary of all three scorecards with their variance bands.
- Otherwise write the same file with first line `FAIL: <one-line reason>`.
