# Job 03 — T6 Prohibited-claim false-positive fix

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Master plan: `GPTs/reports/test_harness_improvement_plan_20260520.md` — read
  section **T6**.
- Evidence: `GPTs/reports/source_preserving_test_analysis_and_plan_review_20260520.md`
  section 5 — both prohibited-claim findings in the latest run (OPS-111 and
  TOOL-038) are FALSE POSITIVES. The answers are correct and safe; the judge's
  negation/order detection is broken.

## Problem

In `evals/altibase_answerability/scripts/judge_report.py`:
- `answer_has_negation_near()` inspects only the 4 longest claim terms within a
  6-token window and fails on plural/singular mismatch
  (`tablespaces` in the claim vs `tablespace` in the answer's negation).
- `prohibited_claim_present()` flags any claim with >=0.90 bag-of-words overlap;
  it cannot represent statement order, so TOOL-038's correct
  DIFF-then-FILESYNC sequence reads as the prohibited "FILESYNC before diff".

## Task

Fix `judge_report.py` so OPS-111 and TOOL-038 are no longer flagged, without
weakening detection of genuine prohibited claims.

1. In `answer_has_negation_near()`: suffix-normalize terms (`-s`, `-es`, `-ed`,
   `-ing`) before matching; consider all high-value claim terms, not just the
   longest 4; widen the proximity window or use sentence-level negation.
2. In `prohibited_claim_present()`: for order-sensitive claims ("X before Y"),
   do not flag on bag-of-words overlap alone — require the claim's subject +
   verb + polarity to appear un-negated and in the asserted relation.
3. Add a regression test to the judge self-test (`run_self_test` /
   `--self-test`): include the real OPS-111 and TOOL-038 answer text (read them
   from
   `evals/altibase_answerability/reports/full_benchmark/runs/altibase_source_preserving_20260520_090243/answers/answers.jsonl`)
   and assert `prohibited_claim_present` returns "not present" for the claims
   `"System tablespaces can be dropped with CASCADE CONSTRAINTS."` and
   `"FILESYNC should be run before diff."`.
4. Keep a genuine-positive guard in the self-test: a clearly prohibited answer
   must still be detected, so the fix does not silently disable detection.

## Constraints (non-negotiable)

- Modify only `evals/altibase_answerability/scripts/judge_report.py`.
- Do not touch `GPTs/upload_package/`. Keep the judge deterministic.
- Do not run `run-all.sh` or other jobs' files.

## Acceptance checks

```bash
python3 evals/altibase_answerability/scripts/judge_report.py --self-test
# Re-judge the existing run and confirm zero prohibited-claim findings on the two questions:
python3 evals/altibase_answerability/scripts/judge_report.py \
  --manifest evals/altibase_answerability/manifests/full_benchmark_source_preserving_package.json \
  --policy evals/altibase_answerability/policy.json \
  --answers evals/altibase_answerability/reports/full_benchmark/runs/altibase_source_preserving_20260520_090243/answers/answers.jsonl \
  --output-dir /tmp/altibase-job03-judge
python3 -c "import json; js=[json.loads(l) for l in open('/tmp/altibase-job03-judge/judgments.jsonl')]; bad=[j['question_id'] for j in js for f in j.get('findings',[]) if f['category']=='prohibited_claim']; print('prohibited_claim findings:', bad); assert 'OPS-111' not in bad and 'TOOL-038' not in bad, bad"
git diff --check
```

## Completion protocol

As your final action:

- Ensure `evals/altibase_answerability/improvement/state/` exists.
- If every acceptance check passed, write
  `evals/altibase_answerability/improvement/state/03.result` with first line
  `PASS` and a short summary.
- Otherwise write the same file with first line `FAIL: <one-line reason>`.
