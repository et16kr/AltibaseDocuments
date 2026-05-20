# Job 08 — T4 Manifest-aware routing stage

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Master plan: `GPTs/reports/test_harness_improvement_plan_20260520.md` — read
  section **T4**.
- Problem: `02_source_manifest.md` (a source manifest TSV) and
  `03_source_to_shard_manifest.md` (a source-to-shard map TSV) define the
  package's intended retrieval contract, but `answer_runner.py` never uses them.
  In the latest run `03_source_to_shard_manifest.md` was selected for 0 of 270
  questions. The retrieval ranks flat lexical chunks only.
- Jobs 01, 06, 07 already added: the retrieval audit, per-chunk `block_meta`,
  and improved query tokenization.

## Task

In `evals/altibase_answerability/scripts/answer_runner.py`:

1. Add `parse_source_manifest()` — parse the TSV inside
   `GPTs/upload_package/02_source_manifest.md` into rows keyed by `source_id`
   (columns include `source_id`, `source_path`, `source_family`, `title`,
   `version_scope`, `language`, `authority_label`).
2. Add `parse_shard_manifest()` — parse the TSV inside
   `GPTs/upload_package/03_source_to_shard_manifest.md` into a
   `(source_id, block_id) -> shard_path` mapping. Normalize the preserved
   `GPTs/source_pack/source_pack_shard_NNN.md` paths to the matching
   `GPTs/upload_package/source_pack_shard_NNN.md` context file by basename.
3. Add `route_sources(query, manifest_rows)` — score manifest rows against the
   question/technical tokens by overlap with `title`, `source_family`,
   `source_path`, `version_scope`, `language`; return the top-K `source_id`s.
4. Integrate into `build_context()`: chunks whose propagated
   `block_meta.source_id` (from job 06) is in the routed set get a large score
   bonus, so routed-source chunks win ranking. Use only the question text and
   the in-package manifest files — never judge-only question fields.
5. **Extend the retrieval audit**: add a `routed_source_ids` field to each
   question's audit record listing the source ids `route_sources()` selected.
   This is the meaningful observable for jobs 10 and 11 — note that "routing
   used the manifest" is not the same as "the manifest file appeared in selected
   context", so do not rely only on the existing `included_03_manifest` flag.
6. Preserve determinism, `max_context_chars`, leakage checks, `--self-test`, and
   every existing retrieval-audit field (job-01 base fields and job-06
   `block_meta`).

## Constraints (non-negotiable)

- Modify only `evals/altibase_answerability/scripts/answer_runner.py`.
- Use only allowlisted question input and the in-package manifest files. Never
  use judge-only question fields (`source_refs`, `required_tokens`,
  `expected_facts`, etc.) to route.
- Do not touch `GPTs/upload_package/` source bodies. Keep behaviour
  deterministic.
- Do not run `run-all.sh` or other jobs' files.

## Acceptance checks

```bash
python3 evals/altibase_answerability/scripts/answer_runner.py --self-test
MODE=dry_run LIMIT=20 RUN_ROOT=/tmp/altibase-job08 ./run-test.sh source-preserving
python3 -c "
import json
rows=[json.loads(l) for l in open('/tmp/altibase-job08/answers/retrieval_audit.jsonl')]
assert len(rows)==20, len(rows)
with_routes=sum(1 for r in rows if r.get('routed_source_ids'))
print('questions with routed_source_ids:', with_routes, '/', len(rows))
assert with_routes>=1, 'routing produced no routed_source_ids for any question'
"
python3 evals/altibase_answerability/scripts/validate_benchmark.py \
  --manifest evals/altibase_answerability/manifests/full_benchmark_source_preserving_package.json \
  --profile full
git diff --check
```

In your result summary, report how the routed-source signal changed selection
(e.g. for how many of the 20 questions a routed source's chunk reached the
selected context), using the retrieval audit output.

## Completion protocol

As your final action:

- Ensure `evals/altibase_answerability/improvement/state/` exists.
- If every acceptance check passed, write
  `evals/altibase_answerability/improvement/state/08.result` with first line
  `PASS` and a short summary.
- Otherwise write the same file with first line `FAIL: <one-line reason>`.
