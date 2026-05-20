# Job 05 — T8 Pass-logic and threshold consistency

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Master plan: `GPTs/reports/test_harness_improvement_plan_20260520.md` — read
  section **T8**.
- Evidence: `GPTs/reports/source_preserving_test_analysis_and_plan_review_20260520.md`
  section 4.3 — any missed critical fact emits a `high` finding and any missed
  required token emits a `medium` finding, and `passed` requires
  `severity in {none, low}`. So the `critical_fact_coverage >= 0.80` clause in
  the pass test is dead code, and the real bar is "zero misses". There are also
  degenerate required tokens (a single-character `'0'`).

## Task

Make the pass logic intentional and internally consistent.

1. Read the pass computation in
   `evals/altibase_answerability/scripts/judge_report.py` (around the `passed =`
   expression) and the thresholds in `evals/altibase_answerability/policy.json`.
2. Reconcile them. Recommended option (implement this unless you find a concrete
   blocker, in which case document the alternative you chose and why):
   - Make the `passed` decision consistent with the policy thresholds
     (`critical_fact_coverage_minimum`, `required_token_preservation_minimum`,
     `overall_pass_rate_minimum`, etc.) so a near-miss finding does not silently
     override a numeric threshold the policy says is acceptable, and so no clause
     in the pass expression is dead code.
3. Identify and fix degenerate required tokens in
   `evals/altibase_answerability/questions/*.jsonl` — required tokens that are a
   single character or otherwise cannot be meaningfully matched literally (for
   example a bare `"0"`). Either remove them or replace them with the meaningful
   token they were meant to represent, based on the question and its
   `expected_facts`. Keep changes minimal and source-justified.
4. Write a short decision note to
   `evals/altibase_answerability/reports/judge_pass_logic_decision_20260520.md`
   recording: what the pass logic was, what it is now, why, and the list of
   degenerate tokens changed.

## Constraints (non-negotiable)

- Modify only: `judge_report.py`, `policy.json` (if a threshold value genuinely
  must change — prefer not to), the affected `questions/*.jsonl` files, and the
  new decision note. Do not touch `GPTs/upload_package/` source bodies.
- Do not change question `expected_facts` semantics; only fix degenerate
  `required_tokens`.
- Keep the judge deterministic.
- Do not run `run-all.sh` or other jobs' files.

## Acceptance checks

```bash
python3 evals/altibase_answerability/scripts/judge_report.py --self-test
python3 evals/altibase_answerability/scripts/validate_benchmark.py \
  --manifest evals/altibase_answerability/manifests/full_benchmark_source_preserving_package.json \
  --profile full
python3 evals/altibase_answerability/scripts/validate_benchmark.py \
  --manifest evals/altibase_answerability/manifests/coding_agent_source_preserving_package.json \
  --profile coding_agent
test -f evals/altibase_answerability/reports/judge_pass_logic_decision_20260520.md
git diff --check
```

## Completion protocol

As your final action:

- Ensure `evals/altibase_answerability/improvement/state/` exists.
- If every acceptance check passed, write
  `evals/altibase_answerability/improvement/state/05.result` with first line
  `PASS` and a short summary of the pass-logic decision and the degenerate
  tokens fixed.
- Otherwise write the same file with first line `FAIL: <one-line reason>`.
