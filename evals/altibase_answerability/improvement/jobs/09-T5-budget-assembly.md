# Job 09 — T5 Budgeted context assembly

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Master plan: `GPTs/reports/test_harness_improvement_plan_20260520.md` — read
  section **T5**.
- The upload package is ~59.7 MB; `max_context_chars` is 180000. Selection must
  be partitioned so routed source blocks are not crowded out by secondary
  lexical chunks.

## Task

In `build_context()` in
`evals/altibase_answerability/scripts/answer_runner.py`:

1. Partition the `max_context_chars` budget deterministically into sections, in
   priority order:
   1. compact routing metadata (manifest rows for the routed sources from
      job 08);
   2. routed-source chunks, each with the provenance prefix from job 06;
   3. nearby heading / wrapper context;
   4. secondary lexical chunks, only with leftover budget.
2. Apply deterministic truncation rules at section boundaries. Never exceed
   `max_context_chars`. Preserve the existing behaviour when the package easily
   fits.
3. Do not include a whole manual-sized source block just because it is the best
   match — only include it if it already fits the remaining budget. Otherwise
   include the best-ranked source-internal chunks.
4. Preserve determinism, leakage checks, `--self-test`, and the retrieval audit
   sidecar including every field added by earlier jobs (job-01 base fields,
   job-06 `block_meta`, job-08 `routed_source_ids`).

## Constraints (non-negotiable)

- Modify only `evals/altibase_answerability/scripts/answer_runner.py`.
- Use only allowlisted question input and in-package context — no judge-only
  fields.
- Do not touch `GPTs/upload_package/` source bodies. Keep behaviour
  deterministic.
- Do not run `run-all.sh` or other jobs' files.

## Acceptance checks

```bash
python3 evals/altibase_answerability/scripts/answer_runner.py --self-test
MODE=dry_run LIMIT=10 RUN_ROOT=/tmp/altibase-job09-sp ./run-test.sh source-preserving
MODE=dry_run RUN_ROOT=/tmp/altibase-job09-agent ./run-test.sh coding-agent
# No selected context may exceed the 180000-char budget.
python3 -c "
import json
for path in ['/tmp/altibase-job09-sp/answers/retrieval_audit.jsonl',
             '/tmp/altibase-job09-agent/answers/retrieval_audit.jsonl']:
    for l in open(path):
        r=json.loads(l)
        total=sum(c['char_count'] for c in r.get('selected_chunks',[]))
        assert total<=180000, (r['question_id'], total)
print('all selected contexts within budget')
"
python3 evals/altibase_answerability/scripts/validate_benchmark.py \
  --manifest evals/altibase_answerability/manifests/coding_agent_source_preserving_package.json \
  --profile coding_agent
git diff --check
```

## Completion protocol

As your final action:

- Ensure `evals/altibase_answerability/improvement/state/` exists.
- If every acceptance check passed, write
  `evals/altibase_answerability/improvement/state/09.result` with first line
  `PASS` and a short summary.
- Otherwise write the same file with first line `FAIL: <one-line reason>`.
