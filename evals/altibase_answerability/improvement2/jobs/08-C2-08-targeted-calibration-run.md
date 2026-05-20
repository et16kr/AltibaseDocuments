# Job 08 — C2-08 Targeted calibration run (stop/go gate)

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

This job runs LIVE provider calls and can take a long time. It is a stop/go
gate: if the targeted calibration does not improve, this job must FAIL on
purpose so the cycle-2 jobs can be revised before a full 270-question run.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Master plan: `GPTs/reports/answerability_improvement_cycle2_plan_20260520.md` —
  read "Phase 3" and "Acceptance — three separate scorecards".
- Jobs 01–07 have already changed the judge and retrieval code; job 04 passed
  the judge-validity gate.
- Live runs use `./run-test.sh`, provider `command` (Codex CLI), model `gpt-5.5`.
- Baselines: `altibase_source_preserving_20260520_195639_job11` (full) and
  `altibase_coding_agent_20260520_195650_job11` (coding-agent).

## Task

1. Confirm the live provider is usable. If it is not configured/available, do
   NOT hang — write a FAIL result explaining what is missing.
2. **Enable the LLM fact judge for all judging in this job.** `run-test.sh`
   invokes `judge_report.py` with a fixed argument list, so export
   `JUDGE_LLM_FACT=1` in the environment for every run below — otherwise the
   judging falls back to the rule judge and the deltas do not reflect the
   cycle-2 judge. Confirm `JUDGE_LLM_FACT` is the toggle C2-02 implemented.
3. Run the targeted coding-agent suite (all 10 `AGENT-*` questions):
   ```bash
   JUDGE_LLM_FACT=1 RUN_ID=c2_08_coding_agent RUN_ROOT=/tmp/altibase-c2-08-agent ./run-test.sh coding-agent
   ```
4. Run the targeted full-benchmark questions one at a time. Cover the three
   cycle-2 work areas:
   - the six prohibited-claim questions: `PROP-140`, `PROP-142`, `SQL-137`,
     `TOOL-003`, `TOOL-019`, `TOOL-033`;
   - a `properties` sample: `PROP-101` plus at least three previously-failing
     `PROP-*` questions identified by job 06;
   - an `errors_troubleshooting` and a `views_performance_monitoring` sample:
     at least three previously-failing `ERR-*` and three `VPM-*` questions
     identified by job 07.
   ```bash
   JUDGE_LLM_FACT=1 RUN_ID=c2_08_prop101 RUN_ROOT=/tmp/altibase-c2-08-prop101 QUESTION_ID=PROP-101 ./run-test.sh source-preserving
   ```
   Long runs: start each in the background and poll for the run's `summary.txt`
   rather than blocking a single foreground call.
5. Compare every result against the job-11 baseline (critical fact coverage,
   required token preservation, severity, prohibited-claim findings).
6. Write a calibration report to
   `evals/altibase_answerability/reports/targeted_calibration_cycle2_20260520.md`
   with the per-question deltas and the explicit gate decision.

## Gate criteria (all must hold for PASS)

- The six prohibited-claim questions produce **zero** prohibited-claim findings
  in this run.
- At least half of the targeted `properties` sample improves in critical fact
  coverage or required token preservation versus the job-11 baseline.
- At least half of the targeted `errors_troubleshooting` + `VPM` sample improves
  in critical fact coverage or required token preservation.
- The coding-agent suite does not regress (pass count and provenance
  in-context >= the job-11 baseline of 2/10).

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
test -f evals/altibase_answerability/reports/targeted_calibration_cycle2_20260520.md
git diff --check
```

## Completion protocol

As your final action:

- Ensure `evals/altibase_answerability/improvement2/state/` exists.
- If the runs completed AND every gate criterion holds, write
  `evals/altibase_answerability/improvement2/state/08.result` with first line
  `PASS` and a short summary of the deltas.
- If the gate is not met, or the live provider is unavailable, write the same
  file with first line `FAIL: <one-line reason>` (an expected, legitimate
  outcome — the runner stops so the plan can be revised).
