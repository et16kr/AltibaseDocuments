# Job 05 — C2-05 Router scoring tuning for under-specified questions

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Master plan: `GPTs/reports/answerability_improvement_cycle2_plan_20260520.md` —
  item C2-05.
- Evidence: `evals/altibase_answerability/reports/full_rerun_analysis_20260520.md`
  sections **3** and **6, target 4** — manifest routing now executes for every
  question, but required-token-in-context is only 72.6% (full) and 30% of
  answers still self-report missing context. Over a quarter of required tokens
  never reach the model. The cycle-1 lexical reserve keeps mis-routes from
  scoring 0.0, but the router still mis-ranks vaguely worded questions.
- Cycle 1 added `route_sources()` and budgeted assembly to `answer_runner.py`
  (jobs T3/T4/T5). This job tunes that scoring; it does not rebuild it.

## Task

Improve `route_sources()` and the context-assembly scoring in
`evals/altibase_answerability/scripts/answer_runner.py` so under-specified
questions still retrieve the right source blocks.

1. **Baseline first.** Reconstruct required-token-in-context for the full suite
   against the cycle-1 job-11 run and record the number. Use the
   `judge_report.py --retrieval-recall` diagnostic (fixed in job C2-03) over
   `altibase_source_preserving_20260520_195639_job11`, or an equivalent
   manifest-aware rebuild. This is your "before" number.
2. **Diagnose the mis-routes.** Identify questions whose required tokens are
   absent from selected context and whose `routed_source_ids` (retrieval audit)
   miss the source that carries those tokens. Characterise *why* — short
   questions, generic vocabulary, version scope not used, technical tokens
   under-weighted.
3. **Tune the scoring**, conservatively and deterministically:
   - strengthen the version-scope and technical-token signals in
     `route_sources()` so they still discriminate when the question text is
     short;
   - consider widening the routed top-K, or routing a small secondary set when
     the top score is weak/ambiguous, so a near-miss still admits the right
     block;
   - keep the cycle-1 lexical reserve so a mis-route still degrades gracefully.
4. **Do not regress** questions that already retrieve correctly. Verify the
   "after" required-token-in-context against the same baseline question set.
5. Preserve determinism, `max_context_chars`, leakage checks, `--self-test`,
   and every existing retrieval-audit field.

## Constraints (non-negotiable)

- Modify only `evals/altibase_answerability/scripts/answer_runner.py`.
- Use only the question text and the in-package manifest files for routing —
  never judge-only question fields (`expected_facts`, `required_tokens`,
  `source_refs`, `prohibited_claims`).
- Do not touch `GPTs/upload_package/` source bodies. Do not run `run-all.sh`.

## Acceptance checks

```bash
python3 evals/altibase_answerability/scripts/answer_runner.py --self-test
# Dry-run retrieval over a sample; the audit sidecar must still be produced:
MODE=dry_run LIMIT=20 RUN_ID=c2_05_dryrun RUN_ROOT=/tmp/altibase-c2-05 \
  ./run-test.sh source-preserving
test -s /tmp/altibase-c2-05/answers/retrieval_audit.jsonl
git diff --check
```

Required-token-in-context for the full suite, reconstructed the same way for
"before" and "after", must **increase** versus the 72.6% cycle-1 baseline, with
no question that previously had all required tokens in context losing them.
Record both numbers in the result.

## Completion protocol

As your final action:

- Ensure `evals/altibase_answerability/improvement2/state/` exists.
- If every acceptance check passed AND required-token-in-context improved with
  no regression, write
  `evals/altibase_answerability/improvement2/state/05.result` with first line
  `PASS` and a short summary (before/after required-token-in-context).
- Otherwise write the same file with first line `FAIL: <one-line reason>`.
