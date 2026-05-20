# Job 04 — C2-04 Judge re-calibration gate

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

This job is the **Phase 1 gate**. Phase 2 (retrieval/coverage) must not start
until judge-vs-gold agreement reaches the target. If the target is not met, this
job must FAIL on purpose so the judge work (jobs 01–02) can be revised.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Master plan: `GPTs/reports/answerability_improvement_cycle2_plan_20260520.md` —
  item C2-04 and "Acceptance — three separate scorecards".
- Jobs 01–03 have already changed the judge: the round-2 prohibited-claim fix,
  the optional LLM-assisted fact judge, and the `--retrieval-recall` fix.
- Cycle-1 judge-validity baseline (from `full_rerun_analysis_20260520.md` §4):
  agreement 75.0%, precision 0.711, recall 0.931, against the 52-entry gold set
  `evals/altibase_answerability/fixtures/judge_gold_set.jsonl`.

## Task

1. Run the rule-only calibration as a reference:
   ```bash
   python3 evals/altibase_answerability/scripts/calibrate_judge.py \
     --gold evals/altibase_answerability/fixtures/judge_gold_set.jsonl
   ```
2. Run the calibration with the LLM-assisted fact judge enabled:
   ```bash
   python3 evals/altibase_answerability/scripts/calibrate_judge.py \
     --gold evals/altibase_answerability/fixtures/judge_gold_set.jsonl --llm-fact-judge
   ```
   The LLM judge requires the live command provider (Codex CLI). Confirm it is
   usable first; if it is not, do NOT hang — this job FAILs with a clear reason
   (the gate cannot be evaluated without it).
3. Re-judge the cycle-1 job-11 run and confirm the round-2 prohibited-claim fix
   still holds end to end (0 of the six C2-01 false positives fire).
4. Write the gate decision record to
   `evals/altibase_answerability/reports/judge_calibration_gate_cycle2_20260520.md`:
   rule-only vs LLM-judge agreement / precision / recall, the per-disagreement
   breakdown of any residual gold-set misses, the prohibited-claim
   false-positive count, and an explicit PASS/FAIL gate verdict.

## Gate criteria (all must hold for PASS)

- Judge-vs-gold agreement with the LLM judge enabled is **>= 90.0%**.
- Precision is **>= 0.711** (no regression versus the cycle-1 baseline).
- Recall does not drop below the cycle-1 baseline by more than a small margin
  (>= 0.90).
- Re-judging the job-11 run produces **zero** prohibited-claim findings on
  PROP-140, PROP-142, SQL-137, TOOL-003, TOOL-019, TOOL-033.

If any criterion fails, that is a real stop signal: write a FAIL result so jobs
01–02 can be revised before any retrieval work or live run.

## Constraints (non-negotiable)

- Do not edit judge or retrieval source files in this job — it is a measurement
  and gate job. If you find a bug, record it in the report and FAIL the gate.
- Do not touch `GPTs/upload_package/`.
- Do not run `run-all.sh` or other jobs' files.

## Acceptance checks

```bash
test -f evals/altibase_answerability/reports/judge_calibration_gate_cycle2_20260520.md
python3 evals/altibase_answerability/scripts/judge_report.py --self-test
git diff --check
```

## Completion protocol

As your final action:

- Ensure `evals/altibase_answerability/improvement2/state/` exists.
- If every gate criterion holds, write
  `evals/altibase_answerability/improvement2/state/04.result` with first line
  `PASS` and a short summary (rule-only vs LLM agreement, precision, recall).
- If the gate is not met, or the live provider is unavailable, write the same
  file with first line `FAIL: <one-line reason>` (an expected, legitimate
  outcome — the runner stops so the judge work can be revised).
