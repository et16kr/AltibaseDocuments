# Job 05 — C3-05 Judge re-calibration gate

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

This job is the **Phase 1 gate**. Phase 2 (retrieval/coverage) must not start
until judge-vs-gold agreement reaches the target on the **expanded** gold set.
If the target is not met, this job must FAIL on purpose so the Phase 1 judge
work (jobs 01–04) can be revised.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Master plan: `GPTs/reports/answerability_improvement_cycle3_plan_20260522.md` —
  item C3-05 and "Acceptance — three separate scorecards".
- Jobs 01–04 have already changed the harness: the ERR-101 quoted-span
  prohibited-claim fix, the expanded ~150-entry gold set, the enlarged
  coding-agent suite, and multi-sample answer generation + the scorecard
  variance band.
- Cycle-2 judge-validity steady state (from
  `full_rerun_analysis_cycle2_20260520.md` §6): gold-set agreement 96.15%,
  precision 0.966, recall ≈ 0.93, prohibited-claim false positives 1, on the
  old 52-entry gold set.
- The gate is now measured against the **expanded** gold set
  `evals/altibase_answerability/fixtures/judge_gold_set.jsonl` produced by job 02.

## Task

1. Run the rule-only calibration as a reference:
   ```bash
   python3 evals/altibase_answerability/scripts/calibrate_judge.py \
     --gold evals/altibase_answerability/fixtures/judge_gold_set.jsonl
   ```
2. Run the calibration with the LLM-assisted fact judge enabled. Because the LLM
   judge is non-deterministic at first computation, run it **three times with a
   fresh verdict cache each time** so the gate measures a stable result, not one
   lucky draw. Use the `--llm-fact-judge-cache` option to point each run at a
   distinct, empty cache file:
   ```bash
   for i in 1 2 3; do
     python3 evals/altibase_answerability/scripts/calibrate_judge.py \
       --gold evals/altibase_answerability/fixtures/judge_gold_set.jsonl \
       --llm-fact-judge \
       --llm-fact-judge-cache /tmp/altibase-c3-05-cache-$i.json
   done
   ```
   The LLM judge requires the live command provider (Codex CLI). Confirm it is
   usable first; if it is not, do NOT hang — this job FAILs with a clear reason
   (the gate cannot be evaluated without it). Record all three agreement /
   precision / recall numbers and their spread.
3. Re-judge the cycle-2 job-09 run and confirm the ERR-101 quoted-span fix still
   holds end to end (0 prohibited-claim false positives across ERR-101 and the
   six C2-01 questions).
4. Write the gate decision record to
   `evals/altibase_answerability/reports/judge_calibration_gate_cycle3_20260522.md`:
   rule-only vs LLM-judge agreement / precision / recall on the expanded gold
   set, the per-disagreement breakdown of any residual gold-set misses, the
   prohibited-claim false-positive count, and an explicit PASS/FAIL gate verdict.

## Gate criteria (all must hold for PASS)

- Judge-vs-gold agreement with the LLM judge enabled, on the expanded gold set:
  the **mean of the three runs is ≥ 90.0%** and the **lowest of the three is
  ≥ 88.0%**. A wide spread (lowest well under 88%) is itself a stop signal — the
  LLM judge is too flaky to gate on; FAIL and record it.
- Precision and recall must not regress materially versus the cycle-2 steady
  state (precision ≈ 0.97, recall ≈ 0.93). A small movement caused by the larger
  gold set is acceptable; a real drop (precision < 0.90 or recall < 0.90 in any
  run) is a stop signal — FAIL and record it.
- Re-judging the job-09 run produces **zero** prohibited-claim findings on
  ERR-101, PROP-140, PROP-142, SQL-137, TOOL-003, TOOL-019, TOOL-033.

If any criterion fails, that is a real stop signal: write a FAIL result so jobs
01–04 can be revised before any retrieval work or live run.

## Constraints (non-negotiable)

- Do not edit judge or retrieval source files in this job — it is a measurement
  and gate job. If you find a bug, record it in the report and FAIL the gate.
- Do not touch `GPTs/upload_package/` and do not modify the gold set or question
  records.
- Do not run `run-all.sh` or other jobs' files.

## Acceptance checks

```bash
test -f evals/altibase_answerability/reports/judge_calibration_gate_cycle3_20260522.md
python3 evals/altibase_answerability/scripts/judge_report.py --self-test
git diff --check
```

## Completion protocol

As your final action:

- Ensure `evals/altibase_answerability/improvement3/state/` exists.
- If every gate criterion holds, write
  `evals/altibase_answerability/improvement3/state/05.result` with first line
  `PASS` and a short summary (rule-only vs LLM agreement on the expanded set,
  precision, recall, the three-run spread).
- If the gate is not met, or the live provider is unavailable, write the same
  file with first line `FAIL: <one-line reason>` (an expected, legitimate
  outcome — the runner stops so the judge work can be revised).
