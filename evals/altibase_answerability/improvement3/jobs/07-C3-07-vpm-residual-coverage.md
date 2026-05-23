# Job 07 — C3-07 `views_performance_monitoring` residual coverage

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Master plan: `GPTs/reports/answerability_improvement_cycle3_plan_20260522.md` —
  item C3-07.
- Evidence: `evals/altibase_answerability/reports/full_rerun_analysis_cycle2_20260520.md`
  section **6, target 2** — `views_performance_monitoring` (VPM) is tied for the
  worst domain at 10.0% pass. Cycle-2 job C2-07 raised VPM critical-fact coverage
  and token preservation, but few questions cross the pass threshold. The C2-07
  deep-dive report
  `evals/altibase_answerability/reports/errors_views_deep_dive_cycle2_20260521.md`
  lists the surviving VPM residuals, including out-of-mechanism-scope manuals
  (Performance Tuning Guide, Monitoring API Guide) and question-phrasing
  residuals.
- The 30 VPM questions are in
  `evals/altibase_answerability/questions/views_performance_monitoring.jsonl`.

## Task

Resolve the C2-07 VPM residuals.

1. **Start from the C2-07 residual list.** Read the VPM residual section of
   `errors_views_deep_dive_cycle2_20260521.md` and enumerate every residual VPM
   question it names.
2. **Classify each residual** using the cycle-2 job-09 run
   (`altibase_source_preserving_20260521_220915_job09`), the retrieval-audit
   sidecar, and `judge_report.py --retrieval-recall`:
   - **(a) retrieval/assembly defect** — the facts are in a routed source but
     not selected into context. Fixable here.
   - **(b) out-of-mechanism-scope source gap** — the facts live in a manual the
     pack does not carry in the depth the question needs (e.g. Performance
     Tuning Guide, Monitoring API Guide). Out of harness scope; report it.
   - **(c) question-phrasing residual** — the question is answerable but its
     wording does not route/anchor cleanly; note whether C3-08
     (prose→identifier resolution) is the proper fix and defer it there rather
     than duplicating the work.
3. **Fix category (a)** in `answer_runner.py`, conservatively and
   deterministically — `V$`/`SYS_*`/`D$` dictionary-view and performance-view
   definition blocks must survive chunking and budgeted assembly intact and be
   admitted whole.
4. **Report (b) and (c) honestly** in a residual report
   `evals/altibase_answerability/reports/vpm_residual_cycle3_20260522.md`: the
   (a)/(b)/(c) split, what was fixed, the out-of-scope source gaps, and which
   residuals are handed to C3-08. Do NOT edit `GPTs/upload_package/` and do NOT
   weaken the question records.
5. **Do not regress** the other six domains or the gains from cycle-2 jobs
   C2-06/07 and from job 06. Preserve determinism, leakage checks, `--self-test`,
   and all retrieval-audit fields.

## Constraints (non-negotiable)

- You MAY modify `evals/altibase_answerability/scripts/answer_runner.py`.
- Do NOT touch `GPTs/upload_package/` source bodies. Do NOT modify question
  records in `evals/altibase_answerability/questions/`.
- Do not run `run-all.sh` or other jobs' files.

## Acceptance checks

```bash
python3 evals/altibase_answerability/scripts/answer_runner.py --self-test
test -f evals/altibase_answerability/reports/vpm_residual_cycle3_20260522.md
MODE=dry_run LIMIT=20 RUN_ID=c3_07_vpm RUN_ROOT=/tmp/altibase-c3-07 \
  ./run-test.sh source-preserving
test -s /tmp/altibase-c3-07/answers/retrieval_audit.jsonl
git diff --check
```

For PASS: required-token-in-context for the `views_performance_monitoring`
questions, reconstructed the same way before and after, must **increase** for
the category-(a) questions versus the cycle-2 baseline, with no regression in
the other six domains, and the report must cleanly separate (a) fixes from (b)
out-of-scope gaps and (c) phrasing residuals deferred to C3-08. If the residuals
are overwhelmingly (b)/(c), that is still a PASS provided the report documents it
precisely — state that plainly in the result.

## Completion protocol

As your final action:

- Ensure `evals/altibase_answerability/improvement3/state/` exists.
- If the acceptance checks passed and the residual report is complete, write
  `evals/altibase_answerability/improvement3/state/07.result` with first line
  `PASS` and a short summary (the (a)/(b)/(c) split, before/after
  token-in-context for category (a)).
- Otherwise write the same file with first line `FAIL: <one-line reason>`.
