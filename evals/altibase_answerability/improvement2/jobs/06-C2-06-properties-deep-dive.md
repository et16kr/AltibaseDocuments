# Job 06 — C2-06 `properties` domain deep-dive

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Master plan: `GPTs/reports/answerability_improvement_cycle2_plan_20260520.md` —
  item C2-06.
- Evidence: `evals/altibase_answerability/reports/full_rerun_analysis_20260520.md`
  sections **5.3** and **6, target 3** — `properties` is the worst domain: pass
  rate 2.0%, 32 version-sensitive-property protected-topic blockers, and
  required-token preservation stuck at ≈ 50%. Routing now executes, but coverage
  there is still low.
- Job 05 already tuned the general router scoring; this job is the
  domain-specific investigation `properties` needs.

## Task

Determine **why** `properties` questions fail and fix what is fixable inside the
test harness.

1. **Investigate.** For the 50 `properties` questions
   (`evals/altibase_answerability/questions/properties.jsonl`), use the cycle-1
   job-11 run, the retrieval audit sidecar, and the `--retrieval-recall`
   diagnostic to determine, per question, whether each required token / critical
   fact is:
   - **(a) present in the routed source but not selected into context** — a
     retrieval/scoring defect this job must fix; or
   - **(b) genuinely absent from the source pack** — a source-content gap that
     is OUT of harness scope and must be reported, not papered over.
2. **Fix category (a).** Where the version-specific property facts exist in the
   routed sources but are not reaching context, fix the routing/assembly in
   `answer_runner.py` — e.g. property-name token weighting, version-scope
   matching for `7.1` / `7.3` / `trunk`, or block-granularity selection so the
   right property table/row block is admitted.
3. **Report category (b) honestly.** List every `properties` question whose
   required facts are genuinely missing from the source pack in the deep-dive
   report. Do NOT edit `GPTs/upload_package/` to manufacture coverage, and do
   NOT weaken the question records to make them pass.
4. **Write the deep-dive report** to
   `evals/altibase_answerability/reports/properties_deep_dive_cycle2_20260520.md`:
   the (a)/(b) split, what was fixed, and the residual source-content gaps.
5. Preserve determinism, leakage checks, `--self-test`, and all retrieval-audit
   fields. Use only the question text and in-package manifests for routing.

## Constraints (non-negotiable)

- You MAY modify `evals/altibase_answerability/scripts/answer_runner.py`.
- Do NOT touch `GPTs/upload_package/` source bodies. Do NOT modify question
  records in `evals/altibase_answerability/questions/` — if a question looks
  wrong, record it in the report instead.
- Do not run `run-all.sh` or other jobs' files.

## Acceptance checks

```bash
python3 evals/altibase_answerability/scripts/answer_runner.py --self-test
test -f evals/altibase_answerability/reports/properties_deep_dive_cycle2_20260520.md
# Dry-run retrieval; the audit sidecar must still be produced. Filter to
# individual properties questions with QUESTION_ID if a domain subset is needed.
MODE=dry_run LIMIT=20 RUN_ID=c2_06_props RUN_ROOT=/tmp/altibase-c2-06 \
  ./run-test.sh source-preserving
test -s /tmp/altibase-c2-06/answers/retrieval_audit.jsonl
git diff --check
```

For PASS: required-token-in-context for the `properties` questions, reconstructed
the same way before and after, must **increase** versus the cycle-1 baseline for
the category-(a) questions, and the report must clearly separate the (a) fixes
from the (b) source-content gaps. If the investigation shows the failure is
overwhelmingly category (b), that is still a PASS provided the report documents
it precisely — but state that plainly in the result.

## Completion protocol

As your final action:

- Ensure `evals/altibase_answerability/improvement2/state/` exists.
- If the acceptance checks passed and the deep-dive report is complete, write
  `evals/altibase_answerability/improvement2/state/06.result` with first line
  `PASS` and a short summary (the (a)/(b) split, before/after token-in-context
  for category (a)).
- Otherwise write the same file with first line `FAIL: <one-line reason>`.
