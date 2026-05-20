# Job 10 — Targeted calibration run (stop/go gate)

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

This job runs LIVE provider calls and can take a long time. It is a stop/go
gate: if the targeted calibration does not improve, this job must FAIL on
purpose so the retrieval jobs can be revised before a full 270-question run.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Master plan: `GPTs/reports/test_harness_improvement_plan_20260520.md` —
  read "Sequencing / Phase 3" and "Acceptance — Three Separate Scorecards".
- Jobs 01–09 have already changed the retrieval and judge code.
- Live runs use `./run-test.sh`, provider `command` (Codex CLI), model `gpt-5.5`.

## Task

1. Confirm the live provider is usable. If it is not configured/available, do
   NOT hang — write a FAIL result explaining what is missing.
2. Run the targeted coding-agent suite (all 10 `AGENT-*` questions):
   ```bash
   RUN_ID=job10_coding_agent RUN_ROOT=/tmp/altibase-job10-agent ./run-test.sh coding-agent
   ```
3. Run the targeted full-benchmark questions one at a time:
   `PROP-101`, `SQL-101`, `ERR-101`, `TOOL-002`, `OPS-111`, `TOOL-038` — e.g.
   ```bash
   RUN_ID=job10_prop101 RUN_ROOT=/tmp/altibase-job10-prop101 QUESTION_ID=PROP-101 ./run-test.sh source-preserving
   ```
   Long runs: start each with the background option and poll for the run's
   `summary.txt` rather than blocking a single foreground call.
4. Compare every result against the baseline run
   `altibase_source_preserving_20260520_090243` /
   `altibase_coding_agent_20260520_104452` (critical fact coverage, required
   token preservation, severity, prohibited-claim findings).
5. Write a calibration report to
   `evals/altibase_answerability/reports/targeted_calibration_20260520.md` with
   the per-question deltas and the gate decision.

## Gate criteria (all must hold for PASS)

- At least one coding-agent question passes, OR the job-01 retrieval audit shows
  that the expected `SRC-*` / `BLOCK-*` provenance tokens are now present in the
  selected context for every failing coding-agent question.
- `OPS-111` and `TOOL-038` produce no prohibited-claim findings.
- At least three of the six targeted full-benchmark questions improve in
  critical fact coverage, required token preservation, or severity versus the
  baseline.

If the gate criteria are not met, that is a real stop signal: write a FAIL
result. Do not proceed to the full run.

## Constraints (non-negotiable)

- Do not edit retrieval/judge source files in this job — this is a measurement
  and gate job. If you find a bug, record it in the report and FAIL the gate.
- Do not touch `GPTs/upload_package/` source bodies.
- Do not run `run-all.sh` or other jobs' files.

## Acceptance checks

- The targeted runs completed and produced `summary.txt` / `judgments.jsonl`.
- The calibration report exists.
- The gate criteria above are evaluated explicitly in the report.

```bash
test -f evals/altibase_answerability/reports/targeted_calibration_20260520.md
git diff --check
```

## Completion protocol

As your final action:

- Ensure `evals/altibase_answerability/improvement/state/` exists.
- If the runs completed AND every gate criterion holds, write
  `evals/altibase_answerability/improvement/state/10.result` with first line
  `PASS` and a short summary of the deltas.
- If the gate is not met, or the live provider is unavailable, write the same
  file with first line `FAIL: <one-line reason>` (this is an expected,
  legitimate outcome — the runner will stop so the plan can be revised).
