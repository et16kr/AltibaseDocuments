# Job 01 — C3-01 ERR-101 quoted-span prohibited-claim false-positive fix

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Master plan: `GPTs/reports/answerability_improvement_cycle3_plan_20260522.md` —
  read the "C3-01" item and "Phase 1".
- Evidence: `evals/altibase_answerability/reports/full_rerun_analysis_cycle2_20260520.md`
  section **6, target 1** — cycle 2 cut prohibited-claim false positives 6 → 1,
  and the surviving one is **ERR-101**: a `cannot`-phrased prohibited claim still
  mis-fires because the answer contains an *unrelated* literal negation
  (`does not`) that sits inside a quoted code/example span — the example text
  `altierr -w "does not"`. The negation belongs to a CLI example, not to the
  factual assertion, but the polarity guard reads it as the answer asserting the
  negative.
- Cycle 2's C2-01 job made `judge_report.py` polarity-, direction-, and
  markdown-emphasis-aware and added six self-test regression fixtures
  (PROP-140, PROP-142, SQL-137, TOOL-003, TOOL-019, TOOL-033). Do not regress
  those, nor the cycle-1 OPS-111 / TOOL-038 cases, nor the genuine-positive
  guard.

## Problem

In `evals/altibase_answerability/scripts/judge_report.py`, the C2-01 polarity
guard for `cannot`-phrased intrinsically-negative claims scans the whole answer
for negation tokens. When a negation word appears inside a quoted code span,
fenced code block, or a CLI example string, the guard treats it as part of the
answer's prose polarity and flips the verdict — producing the ERR-101 false
positive.

## Task

Make the prohibited-claim polarity guard ignore negation tokens that occur
inside quoted code/example spans.

1. **Identify the quoted/example spans** of the answer before polarity
   tokenisation: inline backtick spans, fenced triple-backtick code blocks, and
   quoted string literals (single- and double-quoted) — i.e. the spans that hold
   commands, code, and verbatim examples rather than the answer's own prose.
2. **Generalise the C2-01 polarity guard** so negation tokens (`not`, `cannot`,
   `can not`, `no`, `never`, `does not`, etc.) that fall *inside* those spans do
   not contribute to the polarity decision for a `cannot`-phrased claim. The
   answer's own prose polarity must still be read normally.
3. Do not weaken genuine detection: a prohibited claim genuinely asserted in the
   answer's prose must still be flagged. Keep the markdown-emphasis stripping and
   the direction-/incidental-token logic C2-01 added intact.
4. **Self-test fixture:** add ERR-101 as a regression case to the judge
   self-test (`run_self_test` / `--self-test`). Read the real answer text from
   the cycle-2 job-09 run
   `evals/altibase_answerability/reports/full_benchmark/runs/altibase_source_preserving_20260521_220915_job09/answers/answers.jsonl`
   and assert `prohibited_claim_present` returns "not present" for ERR-101.
5. Keep all six C2-01 fixtures green, keep the cycle-1 OPS-111 / TOOL-038
   regression cases green, and keep the genuine-positive guard case green.

## Constraints (non-negotiable)

- Modify only `evals/altibase_answerability/scripts/judge_report.py`.
- Do not touch `GPTs/upload_package/`. Keep the judge deterministic; the
  `--self-test` path must not call the LLM judge.
- Do not run `run-all.sh` or other jobs' files.

## Acceptance checks

```bash
python3 evals/altibase_answerability/scripts/judge_report.py --self-test
# Re-judge the cycle-2 job-09 run; confirm zero prohibited-claim false positives,
# including ERR-101 and the six C2-01 questions:
python3 evals/altibase_answerability/scripts/judge_report.py \
  --manifest evals/altibase_answerability/manifests/full_benchmark_source_preserving_package.json \
  --policy evals/altibase_answerability/policy.json \
  --answers evals/altibase_answerability/reports/full_benchmark/runs/altibase_source_preserving_20260521_220915_job09/answers/answers.jsonl \
  --output-dir /tmp/altibase-c3-01-judge
python3 -c "import json; js=[json.loads(l) for l in open('/tmp/altibase-c3-01-judge/judgments.jsonl')]; bad=sorted({j['question_id'] for j in js for f in j.get('findings',[]) if f['category']=='prohibited_claim'}); print('prohibited_claim findings:', bad); want={'ERR-101','PROP-140','PROP-142','SQL-137','TOOL-003','TOOL-019','TOOL-033'}; assert not (want & set(bad)), sorted(want & set(bad))"
git diff --check
```

## Completion protocol

As your final action:

- Ensure `evals/altibase_answerability/improvement3/state/` exists.
- If every acceptance check passed, write
  `evals/altibase_answerability/improvement3/state/01.result` with first line
  `PASS` and a short summary (ERR-101 cleared, total prohibited-claim findings
  before and after on the job-09 run).
- Otherwise write the same file with first line `FAIL: <one-line reason>`.
