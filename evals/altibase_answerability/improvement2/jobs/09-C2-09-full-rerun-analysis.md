# Job 09 — C2-09 Full re-run and regression analysis

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

This job runs the LIVE full benchmark and can take a long time (270 + 10
provider calls). It is the final measurement job of cycle 2.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Master plan: `GPTs/reports/answerability_improvement_cycle2_plan_20260520.md` —
  read "Acceptance — three separate scorecards".
- Jobs 01–07 changed the harness; job 08 passed the targeted gate.
- Baselines (cycle-2 "before"): `altibase_source_preserving_20260520_195639_job11`
  (full, 37/270) and `altibase_coding_agent_20260520_195650_job11`
  (coding-agent, 2/10). The cycle-1 final analysis is
  `evals/altibase_answerability/reports/full_rerun_analysis_20260520.md`.

## Task

1. Confirm the live provider is usable. If not, do NOT hang — write a FAIL
   result explaining what is missing.
2. Before spending the run, check whether a complete post-job-07 full run
   already exists under
   `evals/altibase_answerability/reports/full_benchmark/runs/` and
   `.../coding_agent_source_preserving/runs/` (a run newer than job 08 with a
   valid `summary.txt`). If so, reuse it instead of re-running.
3. Otherwise run both suites. Long runs: start each in the background and poll
   for `summary.txt` rather than blocking one foreground call.
   ```bash
   ./run-test.sh source-preserving
   ./run-test.sh coding-agent
   ```
4. Produce a regression analysis report at
   `evals/altibase_answerability/reports/full_rerun_analysis_cycle2_20260520.md`
   with **three separate scorecards** (do not collapse them into one number):
   - **Retrieval scorecard:** routed-source-in-context rate,
     required-token-in-context rate, share of answers self-reporting missing
     context, coding-agent `SRC-*`/`BLOCK-*` in-context rate — all versus the
     job-11 baseline.
   - **Judge-validity scorecard:** judge-vs-gold agreement (`calibrate_judge.py`
     with `--llm-fact-judge`), precision/recall, prohibited-claim
     false-positive count (must stay near zero — the six C2-01 questions cleared).
   - **Pass-rate scorecard:** pass rate, gained/lost question IDs, critical fact
     coverage delta, required token preservation delta, protected-topic blocker
     delta, prohibited-claim count (genuine vs false-positive).
5. Decompose the pass-rate movement into the judge track and the
   retrieval/answer track, as the cycle-1 report did.
6. State plainly whether each scorecard improved versus the job-11 baseline, and
   list the top remaining remediation targets for cycle 3.

## Acceptance criteria for PASS

- Both suites completed (or a valid recent run was reused) and the analysis
  report exists.
- The judge-validity scorecard shows judge-vs-gold agreement **>= 90%** (the
  cycle-2 gate, already met at job 04 — confirm it holds on the full run).
- The retrieval scorecard improved versus the job-11 baseline.
- The pass rate improved versus the job-11 baseline (13.7% full / 20%
  coding-agent). Reaching the 85% readiness threshold is NOT required.
- No increase in genuine prohibited claims.

If the retrieval or judge-validity scorecard did not improve, write a FAIL
result so the cycle-2 changes can be inspected.

## Constraints (non-negotiable)

- Do not edit retrieval/judge source files in this job — it is measurement only.
- Do not touch `GPTs/upload_package/` source bodies.
- Keep answer-generation context pinned to `GPTs/upload_package/*.md`.
- Do not run `run-all.sh` or other jobs' files.

## Acceptance checks

```bash
test -f evals/altibase_answerability/reports/full_rerun_analysis_cycle2_20260520.md
git diff --check
```

## Completion protocol

As your final action:

- Ensure `evals/altibase_answerability/improvement2/state/` exists.
- If the runs completed and the acceptance criteria hold, write
  `evals/altibase_answerability/improvement2/state/09.result` with first line
  `PASS` and a short summary of all three scorecards.
- Otherwise write the same file with first line `FAIL: <one-line reason>`.
