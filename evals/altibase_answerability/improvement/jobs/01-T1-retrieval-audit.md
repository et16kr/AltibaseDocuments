# Job 01 — T1 Retrieval audit instrumentation

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Master plan: `GPTs/reports/test_harness_improvement_plan_20260520.md` — read
  section **T1** before starting.
- Evidence basis: `GPTs/reports/source_preserving_test_analysis_and_plan_review_20260520.md`.
- This job adds retrieval observability. It must not change retrieval behaviour
  or answer content.

## Task

Add a retrieval audit sidecar to the answer runner.

Target file: `evals/altibase_answerability/scripts/answer_runner.py`.

1. While building context for each question, collect an audit record. Add a new
   function `write_retrieval_audit()` and call it from `main()`.
2. Write the audit to `retrieval_audit.jsonl` in the same output directory as
   `answers.jsonl`, one JSON object per question, each containing at least:
   - `question_id`
   - `query_tokens` (the tokens used for ranking)
   - `budget` (`max_context_chars`)
   - `selected_chunks`: list of objects with `rel_path`, `heading`,
     `char_count`, `score`
   - `included_02_manifest`, `included_03_manifest`, `included_readme` (booleans)
   - `distinct_shards` (count of distinct `source_pack_shard_*.md` files used)
3. Do NOT change the answer-record schema. The audit is a separate sidecar file.
4. Keep the audit derived only from allowlisted question input and the selected
   package context — no judge-only question fields.
5. Optional but preferred: add a `--retrieval-recall` post-judge diagnostic to
   `evals/altibase_answerability/scripts/judge_report.py` that, after judging,
   compares each question's selected context against judge-only `source_refs`
   and `required_tokens` and reports presence counts. This is permitted because
   it runs after the provider call and is diagnostic output only. If you add it,
   keep it off by default and guarded behind the flag.

## Constraints (non-negotiable)

- Modify only `answer_runner.py` (and optionally `judge_report.py` for the
  post-judge diagnostic). Do not touch `GPTs/upload_package/` source bodies.
- Keep all behaviour deterministic.
- Do not run `run-all.sh` or any other job's files.

## Acceptance checks

Run these from the repository root; all must pass:

```bash
python3 evals/altibase_answerability/scripts/answer_runner.py --self-test
MODE=dry_run LIMIT=5 RUN_ROOT=/tmp/altibase-job01-audit ./run-test.sh source-preserving
test "$(wc -l < /tmp/altibase-job01-audit/answers/retrieval_audit.jsonl)" -ge 5
python3 -c "import json,sys; [json.loads(l) for l in open('/tmp/altibase-job01-audit/answers/retrieval_audit.jsonl')]; print('audit json ok')"
python3 evals/altibase_answerability/scripts/validate_benchmark.py \
  --manifest evals/altibase_answerability/manifests/full_benchmark_source_preserving_package.json \
  --profile full
git diff --check
```

## Completion protocol

As your final action:

- Ensure the directory `evals/altibase_answerability/improvement/state/` exists.
- If every acceptance check passed, write
  `evals/altibase_answerability/improvement/state/01.result` with the first line
  exactly `PASS` followed by a short summary of what changed.
- If any check failed and you could not fix it within this job, write the same
  file with the first line `FAIL: <one-line reason>`.
