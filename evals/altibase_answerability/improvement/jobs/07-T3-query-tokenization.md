# Job 07 — T3 Query tokenization fix

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Master plan: `GPTs/reports/test_harness_improvement_plan_20260520.md` — read
  section **T3**.
- Problem: in `evals/altibase_answerability/scripts/answer_runner.py`,
  `tokenize_query()` builds the ranking query from
  `id + question + version_scope + user_level + answer_type`. `user_level`
  (`advanced_operator`, ...) and `answer_type` (`reference`, ...) are generic
  strings that occur in thousands of chunks and dilute the technical signal in
  `score_chunk()`.

## Task

In `evals/altibase_answerability/scripts/answer_runner.py`:

1. Change `tokenize_query()` so the lexical ranking signal is built from the
   `question` text only. Drop `user_level` and `answer_type` as ranking tokens.
2. Add a helper that extracts technical tokens from the question — uppercase
   identifiers, `V$...` names, tokens containing `_` / `$` / `.`, error-code
   patterns, and SQL-keyword-like tokens — and weight those higher (about 4x) in
   `score_chunk()`.
3. Use `version_scope` as a separate ranking bonus, not as a flat token: when a
   chunk's propagated `block_meta.version_scope` (added in job 06) equals the
   question's `version_scope`, give that chunk a score bonus.
4. Keep `id` available if you still want it, but it must not dominate ranking
   (question text is the primary signal).
5. Preserve determinism, `max_context_chars` behaviour, leakage checks, the
   `--self-test`, and the retrieval audit sidecar including every field added by
   earlier jobs (job-01 base fields and the job-06 per-chunk `block_meta`).

## Constraints (non-negotiable)

- Modify only `evals/altibase_answerability/scripts/answer_runner.py`.
- Use only allowlisted question input — no judge-only fields.
- Do not touch `GPTs/upload_package/`. Keep behaviour deterministic.
- Do not run `run-all.sh` or other jobs' files.

## Acceptance checks

```bash
python3 evals/altibase_answerability/scripts/answer_runner.py --self-test
# Determinism: two identical dry runs must produce identical audit output.
MODE=dry_run LIMIT=10 RUN_ROOT=/tmp/altibase-job07-a ./run-test.sh source-preserving
MODE=dry_run LIMIT=10 RUN_ROOT=/tmp/altibase-job07-b ./run-test.sh source-preserving
diff <(sort /tmp/altibase-job07-a/answers/retrieval_audit.jsonl) \
     <(sort /tmp/altibase-job07-b/answers/retrieval_audit.jsonl) \
  && echo "deterministic ok"
python3 evals/altibase_answerability/scripts/validate_benchmark.py \
  --manifest evals/altibase_answerability/manifests/full_benchmark_source_preserving_package.json \
  --profile full
git diff --check
```

## Completion protocol

As your final action:

- Ensure `evals/altibase_answerability/improvement/state/` exists.
- If every acceptance check passed, write
  `evals/altibase_answerability/improvement/state/07.result` with first line
  `PASS` and a short summary.
- Otherwise write the same file with first line `FAIL: <one-line reason>`.
