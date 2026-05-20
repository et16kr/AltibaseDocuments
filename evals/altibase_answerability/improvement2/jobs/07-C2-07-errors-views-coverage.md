# Job 07 — C2-07 `errors_troubleshooting` / `views_performance_monitoring` coverage

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Master plan: `GPTs/reports/answerability_improvement_cycle2_plan_20260520.md` —
  item C2-07.
- Evidence: `evals/altibase_answerability/reports/full_rerun_analysis_20260520.md`
  sections **5.3** and **6, target 5** — after `properties`, the two weakest
  domains are `errors_troubleshooting` (critical-fact coverage ≈ 60%, pass 13.3%)
  and `views_performance_monitoring` (critical-fact coverage ≈ 55%, pass 13.3%),
  both with required-token preservation ≈ 52–55%.
- Jobs 05 and 06 already tuned the general router scoring and the `properties`
  routing. This job applies the same retrieval-coverage treatment to these two
  domains.

## Task

Raise required-token-in-context and critical-fact retrieval for the
`errors_troubleshooting` and `views_performance_monitoring` questions.

1. **Baseline first.** For the questions in
   `evals/altibase_answerability/questions/errors_troubleshooting.jsonl` and
   `evals/altibase_answerability/questions/views_performance_monitoring.jsonl`,
   reconstruct required-token-in-context against the cycle-1 job-11 run (use the
   `--retrieval-recall` diagnostic or an equivalent manifest-aware rebuild).
   Record the per-domain "before" numbers.
2. **Diagnose.** For each question whose required tokens / critical facts are
   missing from selected context, determine whether the routed source is wrong
   (a routing defect) or the right block is routed but not selected (an
   assembly/scoring defect). These domains lean on error-message reference
   tables and `V$`/`SYS_*` dictionary-view blocks — check that those table/view
   blocks survive chunking and budgeted assembly intact.
3. **Fix** the routing/assembly defects in
   `evals/altibase_answerability/scripts/answer_runner.py`, conservatively and
   deterministically. Where the required facts are genuinely absent from the
   source pack, record it as a source-content gap (out of harness scope) — do
   not edit `GPTs/upload_package/` and do not weaken the question records.
4. **Do not regress** the other domains or the gains from jobs 05–06. Verify
   "after" numbers the same way you measured "before".
5. Preserve determinism, leakage checks, `--self-test`, and all retrieval-audit
   fields. Use only the question text and in-package manifests for routing.

## Constraints (non-negotiable)

- You MAY modify `evals/altibase_answerability/scripts/answer_runner.py`.
- Do NOT touch `GPTs/upload_package/` source bodies. Do NOT modify question
  records in `evals/altibase_answerability/questions/`.
- Do not run `run-all.sh` or other jobs' files.

## Acceptance checks

```bash
python3 evals/altibase_answerability/scripts/answer_runner.py --self-test
# Dry-run retrieval over a sample; audit sidecar must still be produced:
MODE=dry_run LIMIT=20 RUN_ID=c2_07_dryrun RUN_ROOT=/tmp/altibase-c2-07 \
  ./run-test.sh source-preserving
test -s /tmp/altibase-c2-07/answers/retrieval_audit.jsonl
git diff --check
```

For PASS: required-token-in-context for `errors_troubleshooting` and
`views_performance_monitoring`, reconstructed the same way before and after,
must **increase** versus the cycle-1 baseline, with no regression in the other
five domains. Record the per-domain before/after numbers in the result.

## Completion protocol

As your final action:

- Ensure `evals/altibase_answerability/improvement2/state/` exists.
- If every acceptance check passed AND both domains improved with no regression
  elsewhere, write
  `evals/altibase_answerability/improvement2/state/07.result` with first line
  `PASS` and a short summary (per-domain before/after token-in-context).
- Otherwise write the same file with first line `FAIL: <one-line reason>`.
