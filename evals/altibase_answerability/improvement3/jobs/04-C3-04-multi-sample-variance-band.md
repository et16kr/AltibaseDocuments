# Job 04 — C3-04 Multi-sample answer generation + scorecard variance band

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Master plan: `GPTs/reports/answerability_improvement_cycle3_plan_20260522.md` —
  item C3-04 and "Variance handling — both levers (confirmed)".
- Evidence: `evals/altibase_answerability/reports/full_rerun_analysis_cycle2_20260520.md`
  section **6, target 3** — 11 of the full suite's losses and the coding-agent
  AGENT-010 swing were **pure live answer-generation variance**. The noise floor
  is as large as the cycle-2 signal, so genuine retrieval/answer gains are masked.
- The two levers, both required: (a) multi-sample answer generation to stabilise
  the live runs, and (b) an explicit variance band in the scorecard so a
  retrieval/answer gain is never hidden inside the noise.
- How the harness wires together (confirm by reading the code):
  - `run-test.sh` calls `answer_runner.py` with a **fixed argument list** — it
    does NOT pass a `--samples` flag. So, exactly like the C2-02 `JUDGE_LLM_FACT`
    toggle for the judge, the only way a live benchmark run (jobs 09–10) can
    enable multi-sampling is an **environment variable** that `answer_runner.py`
    reads directly.
  - `run-test.sh` calls `judge_report.py` on `answers/answers.jsonl`, then its
    `write_summary` Python block reads `judge/aggregate_report.json` and expects
    the keys `run_id`, `totals`, `overall_metrics`, `aggregates`,
    `readiness_decision`, `protected_topic_blockers`, `artifacts`.

## Task

Add an optional N-sample answer mode to `answer_runner.py` and a variance band
to the run scorecard.

1. **N-sample answer generation — env toggle mandatory.** Add an `ANSWER_SAMPLES`
   environment variable that `answer_runner.py` reads directly (and, as a
   convenience, a matching `--samples N` CLI flag), defaulting to **N=1**. The
   env toggle is not optional: it is the only path `run-test.sh` can use. With
   N=1 the behaviour, the on-disk `answers.jsonl` format, and the
   retrieval-audit sidecar are **byte-for-byte identical** to today. With N>1,
   produce N answer records per question — retrieval/context assembly is computed
   **once** per question and shared across its samples; only answer generation
   repeats — each record tagged with a `sample_index` (0..N-1). In `dry_run`
   mode the N records are placeholder-identical (no provider is called) but the
   N-record loop still runs, so the plumbing is verifiable without a provider.
2. **Judging across samples.** Make `judge_report.py` group answer records by
   `question_id`, judge every sample, and aggregate per question. It must also
   still consume a **legacy single-sample `answers.jsonl`** (one record per
   question, no `sample_index` field) exactly as today — old runs (e.g. the
   job-09 baseline) must keep judging unchanged.
3. **Scorecard variance band.** Add an explicit variance band to
   `judge/aggregate_report.json` (the authoritative scorecard `judge_report.py`
   produces) and to the Markdown report: for a multi-sample run, report pass
   rate and the per-sample-varying retrieval/coverage metrics as a mean with a
   min–max band across samples. **Preserve every existing top-level key and
   metric** in `aggregate_report.json` so `run-test.sh`'s `write_summary` keeps
   working — add the band as new fields, do not rename or restructure existing
   ones. You MAY also extend `run-test.sh`'s `write_summary` block to print the
   band in `summary.txt`; if you do, change only that block. For N=1 the band is
   degenerate and every artifact reads exactly as today.
4. **Determinism preserved.** `answer_runner.py --self-test` and
   `judge_report.py --self-test` must stay deterministic and behave as N=1; the
   `run-all.sh` preflight must stay hermetic. The `JUDGE_LLM_FACT` toggle and all
   existing retrieval-audit fields are untouched.

## Constraints (non-negotiable)

- You MAY modify `evals/altibase_answerability/scripts/answer_runner.py`,
  `evals/altibase_answerability/scripts/judge_report.py`, and — only its
  `write_summary` block — `run-test.sh`. Do not change routing/assembly
  behaviour: this job is about sampling and reporting, not retrieval.
- Do not touch `GPTs/upload_package/` source bodies.
- N=1 must remain the default everywhere; cycle-3 live runs (jobs 09–10) pass
  `ANSWER_SAMPLES=3` explicitly.
- Do not run `run-all.sh` or other jobs' files.

## Acceptance checks

```bash
python3 evals/altibase_answerability/scripts/answer_runner.py --self-test
python3 evals/altibase_answerability/scripts/judge_report.py --self-test
# N=1 dry-run still produces the audit sidecar and one record per question:
MODE=dry_run LIMIT=10 RUN_ID=c3_04_n1 RUN_ROOT=/tmp/altibase-c3-04-n1 \
  ./run-test.sh source-preserving
test -s /tmp/altibase-c3-04-n1/answers/retrieval_audit.jsonl
python3 -c "import json,collections; rows=[json.loads(l) for l in open('/tmp/altibase-c3-04-n1/answers/answers.jsonl') if l.strip()]; c=collections.Counter(r['question_id'] for r in rows); assert rows and all(v==1 for v in c.values()), dict(c)"
# Multi-sample is wired: a 3-sample dry-run records 3 samples per question:
MODE=dry_run LIMIT=5 ANSWER_SAMPLES=3 RUN_ID=c3_04_n3 RUN_ROOT=/tmp/altibase-c3-04-n3 \
  ./run-test.sh source-preserving
python3 -c "import json,collections; rows=[json.loads(l) for l in open('/tmp/altibase-c3-04-n3/answers/answers.jsonl') if l.strip()]; c=collections.Counter(r['question_id'] for r in rows); print('samples per question:', dict(c)); assert rows and all(v==3 for v in c.values()), dict(c); assert all('sample_index' in r for r in rows)"
# The judge still consumes the cycle-2 single-sample baseline run unchanged:
python3 evals/altibase_answerability/scripts/judge_report.py \
  --manifest evals/altibase_answerability/manifests/full_benchmark_source_preserving_package.json \
  --policy evals/altibase_answerability/policy.json \
  --answers evals/altibase_answerability/reports/full_benchmark/runs/altibase_source_preserving_20260521_220915_job09/answers/answers.jsonl \
  --output-dir /tmp/altibase-c3-04-legacy
test -s /tmp/altibase-c3-04-legacy/aggregate_report.json
git diff --check
```

## Completion protocol

As your final action:

- Ensure `evals/altibase_answerability/improvement3/state/` exists.
- If every acceptance check passed, write
  `evals/altibase_answerability/improvement3/state/04.result` with first line
  `PASS` and a short summary (the `ANSWER_SAMPLES` toggle, how the variance band
  is reported, confirmation N=1 and legacy single-sample runs are unchanged).
- Otherwise write the same file with first line `FAIL: <one-line reason>`.
