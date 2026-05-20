# Job 03 — C2-03 `--retrieval-recall` manifest fix

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Master plan: `GPTs/reports/answerability_improvement_cycle2_plan_20260520.md` —
  item C2-03.
- Evidence: `evals/altibase_answerability/reports/full_rerun_analysis_20260520.md`
  section **6, "Tooling note"** — `judge_report.py --retrieval-recall` calls
  `build_context()` **without** the `manifest_rows` / `shard_map` arguments that
  cycle-1 jobs 08–09 added, so it reconstructs the *pre-routing* lexical context
  and under-reports recall for routed runs (reconstruction was unfaithful for
  every sampled question).

## Problem

In `evals/altibase_answerability/scripts/judge_report.py`, `run_retrieval_recall()`
(around line 1585) rebuilds context with:

```python
bundle, rebuilt_audit = answer_runner.build_context(
    documents, context_chunks, projection, context_mode, budget,
    attachment_glob, context_root,
)
```

`answer_runner.build_context()` now also accepts the manifest-aware routing
inputs (the parsed `02_source_manifest.md` rows and the
`03_source_to_shard_manifest.md` shard map) that jobs 08–09 introduced. Because
`run_retrieval_recall()` omits them, `rebuilt_audit["selected_chunks"]` never
matches the recorded audit and `faithful_reconstruction` is false for routed
runs.

## Task

Make the `--retrieval-recall` diagnostic reconstruct the routed context
faithfully.

1. Read the current `answer_runner.py` to confirm the exact signature
   `build_context()` now expects and the names of the manifest-parsing helpers
   (`parse_source_manifest`, `parse_shard_manifest`, `route_sources`, or
   whatever the current code calls them).
2. In `run_retrieval_recall()`, parse the in-package manifests from the
   answer-generation context root the same way `answer_runner.main()` does, and
   pass them into `build_context()` so the reconstruction is manifest-aware.
3. Recompute `faithful_reconstruction` against the manifest-aware rebuild.
4. Keep the diagnostic resilient: if the manifests are absent, degrade to the
   current lexical reconstruction with a clear warning rather than crashing —
   match the existing warn-and-skip style in that function.
5. Do not change any answer-generation or judging behaviour; this is a
   measurement-tool fix only.

## Constraints (non-negotiable)

- Modify only `evals/altibase_answerability/scripts/judge_report.py`.
- Do not touch `GPTs/upload_package/` or `answer_runner.py`. Keep the judge
  deterministic.
- Do not run `run-all.sh` or other jobs' files.

## Acceptance checks

```bash
python3 evals/altibase_answerability/scripts/judge_report.py --self-test
# Run the diagnostic over the cycle-1 job-11 routed run and confirm the
# reconstruction is now faithful for the questions sampled:
python3 evals/altibase_answerability/scripts/judge_report.py \
  --manifest evals/altibase_answerability/manifests/full_benchmark_source_preserving_package.json \
  --policy evals/altibase_answerability/policy.json \
  --answers evals/altibase_answerability/reports/full_benchmark/runs/altibase_source_preserving_20260520_195639_job11/answers/answers.jsonl \
  --retrieval-recall \
  --output-dir /tmp/altibase-c2-03-judge
python3 -c "import json; d=json.load(open('/tmp/altibase-c2-03-judge/retrieval_recall.json')); pq=d.get('per_question',[]); faithful=sum(1 for q in pq if q.get('faithful_reconstruction')); print(f'faithful reconstruction: {faithful}/{len(pq)}'); assert pq and faithful >= 0.9*len(pq), (faithful, len(pq))"
git diff --check
```

## Completion protocol

As your final action:

- Ensure `evals/altibase_answerability/improvement2/state/` exists.
- If every acceptance check passed, write
  `evals/altibase_answerability/improvement2/state/03.result` with first line
  `PASS` and a short summary (faithful-reconstruction rate before and after).
- Otherwise write the same file with first line `FAIL: <one-line reason>`.
