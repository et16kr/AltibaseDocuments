# Job 01 — C2-01 Prohibited-claim false-positive fix, round 2

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Master plan: `GPTs/reports/answerability_improvement_cycle2_plan_20260520.md` —
  read the "C2-01" item.
- Evidence: `evals/altibase_answerability/reports/full_rerun_analysis_20260520.md`
  section **5.2** — the cycle-1 full run produced 6 prohibited-claim findings
  (PROP-140, PROP-142, SQL-137, TOOL-003, TOOL-019, TOOL-033) and **all six are
  false positives**. Each one blocks an otherwise-passing question.
- Cycle 1 already made the judge partly polarity-aware (commits `82da7371`,
  `eabbbd68`) and fixed two earlier false positives (OPS-111, TOOL-038). This
  job finishes the work; do not regress those fixes.

## Problem

Per §5.2 of the analysis report, the six surviving false positives have four
distinct causes in `evals/altibase_answerability/scripts/judge_report.py`:

- **Polarity** — PROP-142 ("if no entry matches, access is **allowed**") and
  SQL-137 (`NVL2` returns `expr2` when not NULL) assert the opposite of the
  prohibited claim, but bag-of-words overlap fires anyway.
- **Markdown emphasis defeats negation tokenisation** — TOOL-019's answer says
  "does `**not**` commit", but the `**` around `not` stops the negation token
  from being recognised.
- **`cannot`-phrased intrinsically-negative claims** — TOOL-003's prohibited
  claim is "anonymous blocks **cannot** use OUTPUT bind variables"; the answer
  says it **can**. The cycle-1 `without`-guard did not generalise to `cannot`
  for this answer shape.
- **Reversed-direction claims** — TOOL-033's prohibited claim is "A overrides
  B"; the answer correctly says "B overrides A". Bag-of-words cannot tell the
  two directions apart. PROP-140 is an incidental-token misfire (`20300` appears
  only in an unrelated log line).

## Task

Fix `evals/altibase_answerability/scripts/judge_report.py` so all six findings
are eliminated, without weakening detection of genuine prohibited claims.

1. **Markdown emphasis:** strip Markdown emphasis markers (`**`, `*`, `_`,
   backticks) from the answer text before negation tokenisation, so an emphasised
   negation word is still recognised.
2. **`cannot`-phrased claims:** generalise the intrinsically-negative-claim
   guard so it covers `cannot`, `can not`, `may not`, `must not`, `does not`,
   `is not` — not just `without`. When the prohibited claim is itself negative,
   an answer that asserts the affirmative must NOT be flagged.
3. **Direction-sensitive claims:** for "A <relation> B" claims where the
   relation is asymmetric (`overrides`, `before`, `after`, `precedes`,
   `replaces`, `takes precedence over`), require the claim's subject and object
   to appear in the asserted order/direction before flagging — reuse or extend
   the order-sensitivity logic added in cycle 1 for "X before Y".
4. **Incidental tokens:** do not flag a claim solely because a numeric/literal
   token from the claim appears somewhere unrelated in the answer; require the
   claim's subject and predicate to co-occur.
5. **Self-test fixtures:** add all six questions as regression cases to the
   judge self-test (`run_self_test` / `--self-test`). Read the real answer text
   from the cycle-1 job-11 run
   `evals/altibase_answerability/reports/full_benchmark/runs/altibase_source_preserving_20260520_195639_job11/answers/answers.jsonl`
   and assert `prohibited_claim_present` returns "not present" for each.
6. **Genuine-positive guard:** keep (and do not weaken) a self-test case where a
   clearly prohibited answer IS still detected, so the fix does not silently
   disable detection. The existing OPS-111 / TOOL-038 regression cases must
   still pass.

## Constraints (non-negotiable)

- Modify only `evals/altibase_answerability/scripts/judge_report.py`.
- Do not touch `GPTs/upload_package/`. Keep the judge deterministic.
- Do not run `run-all.sh` or other jobs' files.

## Acceptance checks

```bash
python3 evals/altibase_answerability/scripts/judge_report.py --self-test
# Re-judge the cycle-1 job-11 run; confirm zero prohibited-claim findings on the six:
python3 evals/altibase_answerability/scripts/judge_report.py \
  --manifest evals/altibase_answerability/manifests/full_benchmark_source_preserving_package.json \
  --policy evals/altibase_answerability/policy.json \
  --answers evals/altibase_answerability/reports/full_benchmark/runs/altibase_source_preserving_20260520_195639_job11/answers/answers.jsonl \
  --output-dir /tmp/altibase-c2-01-judge
python3 -c "import json; js=[json.loads(l) for l in open('/tmp/altibase-c2-01-judge/judgments.jsonl')]; bad=sorted({j['question_id'] for j in js for f in j.get('findings',[]) if f['category']=='prohibited_claim'}); print('prohibited_claim findings:', bad); want={'PROP-140','PROP-142','SQL-137','TOOL-003','TOOL-019','TOOL-033'}; assert not (want & set(bad)), sorted(want & set(bad))"
git diff --check
```

## Completion protocol

As your final action:

- Ensure `evals/altibase_answerability/improvement2/state/` exists.
- If every acceptance check passed, write
  `evals/altibase_answerability/improvement2/state/01.result` with first line
  `PASS` and a short summary (which findings were cleared, total
  prohibited-claim findings before and after).
- Otherwise write the same file with first line `FAIL: <one-line reason>`.
