# Job 11 — Full re-run and regression analysis

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

This job runs the LIVE full benchmark and can take a long time (270 + 10
provider calls). It is the final measurement job.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Master plan: `GPTs/reports/test_harness_improvement_plan_20260520.md` — read
  "Acceptance — Three Separate Scorecards".
- Jobs 01–09 changed the harness; job 10 passed the targeted gate.
- Baselines: `altibase_source_preserving_20260520_090243` (full),
  `altibase_coding_agent_20260520_104452` (coding-agent).

## Task

1. Confirm the live provider is usable. If not, do NOT hang — write a FAIL
   result explaining what is missing.
2. Before spending the run, check whether a complete post-job-09 full run
   already exists under
   `evals/altibase_answerability/reports/full_benchmark/runs/` and
   `.../coding_agent_source_preserving/runs/` (a run newer than job 10 with a
   valid `summary.txt`). If so, reuse it instead of re-running.
3. Otherwise run both suites. Long runs: start each in the background and poll
   for `summary.txt` rather than blocking one foreground call.
   ```bash
   ./run-test.sh source-preserving
   ./run-test.sh coding-agent
   ```
4. Produce a regression analysis report at
   `evals/altibase_answerability/reports/full_rerun_analysis_20260520.md` with
   **three separate scorecards** (do not collapse them into one number):
   - Retrieval scorecard: routed-source-in-context rate, required-token-in-context
     rate, share of answers self-reporting missing context (baseline 33%),
     coding-agent `SRC-*`/`BLOCK-*` in-context rate.
   - Judge-validity scorecard: judge-vs-gold agreement
     (`calibrate_judge.py`), OPS-111 / TOOL-038 prohibited-claim findings.
   - Pass-rate scorecard: pass rate, gained/lost question IDs, critical fact
     coverage delta, required token preservation delta, protected-topic blocker
     delta, prohibited-claim count.
5. State plainly whether each scorecard improved versus baseline, and list the
   top remaining remediation targets.

## Acceptance criteria for PASS

- Both suites completed (or a valid recent run was reused) and the analysis
  report exists.
- The retrieval scorecard and the judge-validity scorecard both show measurable
  improvement versus baseline.
- No increase in genuine prohibited claims.
- Reaching the 85% readiness pass rate is NOT required for this job to pass —
  the first cycle is expected to move the retrieval and judge-validity
  scorecards, not necessarily the pass rate to readiness.

If the retrieval and judge-validity scorecards did not improve, write a FAIL
result so the harness changes can be inspected.

## Constraints (non-negotiable)

- Do not edit retrieval/judge source files in this job — it is measurement only.
- Do not touch `GPTs/upload_package/` source bodies.
- Keep the answer-generation context pinned to `GPTs/upload_package/*.md`.
- Do not run `run-all.sh` or other jobs' files.

## Acceptance checks

```bash
test -f evals/altibase_answerability/reports/full_rerun_analysis_20260520.md
git diff --check
```

## Completion protocol

As your final action:

- Ensure `evals/altibase_answerability/improvement/state/` exists.
- If the runs completed and the retrieval + judge-validity scorecards improved,
  write `evals/altibase_answerability/improvement/state/11.result` with first
  line `PASS` and a short summary of all three scorecards.
- Otherwise write the same file with first line `FAIL: <one-line reason>`.
