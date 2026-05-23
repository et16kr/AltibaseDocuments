# Job 09 — C3-09 Targeted calibration run (stop/go gate)

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

This job runs LIVE provider calls and can take a long time. It is a stop/go
gate: if the targeted calibration does not improve, this job must FAIL on
purpose so the cycle-3 jobs can be revised before a full 270-question
multi-sample run.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Master plan: `GPTs/reports/answerability_improvement_cycle3_plan_20260522.md` —
  read "Phase 3" and "Acceptance — three separate scorecards".
- Jobs 01–08 have already changed the harness; job 05 passed the judge-validity
  gate on the expanded gold set.
- Live runs use `./run-test.sh`, provider `command` (Codex CLI).
- Baselines (cycle-3 "before"): `altibase_source_preserving_20260521_220915_job09`
  (full, 41/270) and `altibase_coding_agent_20260521_220915_job09`
  (coding-agent, 2/10 on the original 10-question suite).

## Task

1. Confirm the live provider is usable. If it is not configured/available, do
   NOT hang — write a FAIL result explaining what is missing.
2. **Enable the LLM fact judge for all judging in this job.** Export
   `JUDGE_LLM_FACT=1` in the environment for every run below — `run-test.sh`
   invokes `judge_report.py` with a fixed argument list, so without the env
   toggle the judging falls back to the rule judge.
3. **Use multi-sample answer generation (N=3).** Set the C3-04 sample option
   (`ANSWER_SAMPLES=3`) for every run so the targeted deltas carry the variance
   band. Confirm the option name against the job-04 result.
4. Run the targeted coding-agent suite (all `AGENT-*` questions, the enlarged
   C3-03 set):
   ```bash
   JUDGE_LLM_FACT=1 ANSWER_SAMPLES=3 RUN_ID=c3_09_coding_agent \
     RUN_ROOT=/tmp/altibase-c3-09-agent ./run-test.sh coding-agent
   ```
5. Run the targeted full-benchmark questions. Cover the three cycle-3 work areas:
   - the ERR-101 prohibited-claim case (and a couple of the C2-01 questions as
     a regression check);
   - a `replication_cdc_security_network` sample: at least three previously
     failing `REPL-*` questions identified by job 06;
   - a `views_performance_monitoring` sample: at least three previously failing
     `VPM-*` questions identified by job 07;
   - the prose-identifier residuals fixed by job 08 (a sample of PROP-123,
     ERR-117/119/120/123/130, VPM-101/103/104/106/107/108).
   ```bash
   JUDGE_LLM_FACT=1 ANSWER_SAMPLES=3 RUN_ID=c3_09_err101 \
     RUN_ROOT=/tmp/altibase-c3-09-err101 QUESTION_ID=ERR-101 ./run-test.sh source-preserving
   ```
   Long runs: start each in the background and poll for the run's `summary.txt`
   rather than blocking a single foreground call.
6. Compare every result against the job-09 baseline (critical-fact coverage,
   required-token preservation, severity, prohibited-claim findings), reporting
   each figure with its multi-sample variance band.
7. Write a calibration report to
   `evals/altibase_answerability/reports/targeted_calibration_cycle3_20260522.md`
   with the per-question deltas, the variance bands, and the explicit gate
   decision.

## Gate criteria (all must hold for PASS)

- The ERR-101 case (and the C2-01 sample) produce **zero** prohibited-claim
  findings.
- At least half of the targeted `replication_cdc_security_network` sample
  improves in critical-fact coverage or required-token preservation versus the
  job-09 baseline, beyond the variance band.
- At least half of the targeted `views_performance_monitoring` + prose-residual
  sample improves in critical-fact coverage or required-token preservation,
  beyond the variance band.
- The coding-agent suite does not regress: on the questions shared with the
  original 10-question baseline, pass count and `SRC-*`/`BLOCK-*` provenance
  in-context are ≥ the job-09 baseline (2/10).

If the gate criteria are not met, that is a real stop signal: write a FAIL
result. Do not proceed to the full run.

## Constraints (non-negotiable)

- Do not edit retrieval/judge source files in this job — it is a measurement and
  gate job. If you find a bug, record it in the report and FAIL the gate.
- Do not touch `GPTs/upload_package/` source bodies.
- Keep answer-generation context pinned to `GPTs/upload_package/*.md`.
- Do not run `run-all.sh` or other jobs' files.

## Acceptance checks

```bash
test -f evals/altibase_answerability/reports/targeted_calibration_cycle3_20260522.md
git diff --check
```

## Completion protocol

As your final action:

- Ensure `evals/altibase_answerability/improvement3/state/` exists.
- If the runs completed AND every gate criterion holds, write
  `evals/altibase_answerability/improvement3/state/09.result` with first line
  `PASS` and a short summary of the deltas and their variance bands.
- If the gate is not met, or the live provider is unavailable, write the same
  file with first line `FAIL: <one-line reason>` (an expected, legitimate
  outcome — the runner stops so the plan can be revised).
