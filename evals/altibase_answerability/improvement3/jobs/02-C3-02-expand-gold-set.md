# Job 02 — C3-02 Expand and audit the judge gold set (52 → ~150)

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Master plan: `GPTs/reports/answerability_improvement_cycle3_plan_20260522.md` —
  item C3-02 and "Decisions for this cycle".
- Evidence: `evals/altibase_answerability/reports/full_rerun_analysis_cycle2_20260520.md`
  section **6, target 4** — the 52-entry gold set
  `evals/altibase_answerability/fixtures/judge_gold_set.jsonl` is small (one
  entry ≈ 1.9%), and both residual cycle-2 judge disagreements (**REPL-106 F04**
  and **REPL-108 F04**) are borderline labels on it. The agreement estimate is
  fragile because the set is small.
- The expanded gold set is what the C3-05 calibration gate is measured against,
  so it must be domain-balanced and accurately labelled.

## Task

Expand the gold set from 52 to **~150 entries (≥ 140)**, domain-balanced and
audited.

1. **Survey the existing set.** Read `fixtures/judge_gold_set.jsonl` and record
   its current per-domain count and the `term_score` / label distribution.
   Confirm the exact record schema (`question_id`, `fact_id`, `importance`,
   `fact_text`, `answer`, `required_tokens`, `label`, `notes`) and reuse it
   unchanged.
2. **Add ~100 new gold entries** drawn from real benchmark answers in
   `evals/altibase_answerability/reports/full_benchmark/runs/` (the cycle-2
   job-09 run `altibase_source_preserving_20260521_220915_job09` and earlier
   runs are the source of `answer` text — copy answers verbatim, do not
   synthesise them). Balance them across all **seven** domains
   (`errors_troubleshooting`, `operations_admin`, `properties`,
   `replication_cdc_security_network`, `sql_ddl_dml_datatypes`,
   `tools_apis_connectors_migration`, `views_performance_monitoring`) so the
   final set is roughly even per domain.
3. **Prioritise the hard band.** Weight the new entries toward the
   paraphrase-suspect `term_score` band that the rule judge cannot resolve
   confidently (the band the LLM fact judge adjudicates — confirm it against the
   rule judge's current threshold), and toward facts where a correct paraphrase
   and a near-miss look similar.
4. **Re-audit the borderline labels.** Re-examine `REPL-106 F04` and
   `REPL-108 F04` against their source material and either confirm or correct
   their `label`, recording the rationale.
5. **Label every new entry by meaning**, not wording: `covered` if the answer
   substantively conveys the fact, `not_covered` otherwise. Fill `notes` with a
   one-line justification for each.
6. **Write the labelling-rationale report** to
   `evals/altibase_answerability/reports/judge_gold_set_expansion_cycle3_20260522.md`:
   the before/after per-domain counts, the term_score-band coverage, the
   REPL-106/REPL-108 re-audit outcome, and the labelling policy used.

## Constraints (non-negotiable)

- Modify only `evals/altibase_answerability/fixtures/judge_gold_set.jsonl`
  (and write the report). Do not change judge or retrieval code in this job.
- Do not touch `GPTs/upload_package/` and do not modify question records under
  `evals/altibase_answerability/questions/`.
- Every new entry must be valid JSONL matching the existing schema; `answer`
  text must be copied from a real run, never invented.
- Do not run `run-all.sh` or other jobs' files.

## Acceptance checks

```bash
# >= 140 entries, all valid JSONL with the required fields:
python3 -c "import json; rows=[json.loads(l) for l in open('evals/altibase_answerability/fixtures/judge_gold_set.jsonl') if l.strip()]; print('entries:', len(rows)); req={'question_id','fact_id','fact_text','answer','label'}; assert len(rows)>=140, len(rows); assert all(req<=set(r) for r in rows); assert all(r['label'] in ('covered','not_covered') for r in rows)"
# The judge self-test stays green and the rule-only calibration runs on the new set:
python3 evals/altibase_answerability/scripts/judge_report.py --self-test
python3 evals/altibase_answerability/scripts/calibrate_judge.py \
  --gold evals/altibase_answerability/fixtures/judge_gold_set.jsonl
test -f evals/altibase_answerability/reports/judge_gold_set_expansion_cycle3_20260522.md
git diff --check
```

## Completion protocol

As your final action:

- Ensure `evals/altibase_answerability/improvement3/state/` exists.
- If every acceptance check passed, write
  `evals/altibase_answerability/improvement3/state/02.result` with first line
  `PASS` and a short summary (entry count before/after, per-domain balance,
  REPL-106/REPL-108 re-audit outcome).
- Otherwise write the same file with first line `FAIL: <one-line reason>`.
