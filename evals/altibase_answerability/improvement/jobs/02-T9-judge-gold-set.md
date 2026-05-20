# Job 02 — T9 Judge calibration gold set

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Master plan: `GPTs/reports/test_harness_improvement_plan_20260520.md` — read
  section **T9** before starting.
- Purpose: the benchmark judge is a lexical rule judge. Before changing it
  (jobs 03–05) we need a trusted yardstick: a labelled gold set and a
  calibration script that measures judge-vs-label agreement.

## Task

### Part A — build the gold set

Create `evals/altibase_answerability/fixtures/judge_gold_set.jsonl`.

Source data (a completed run already in the repo):
- judgments: `evals/altibase_answerability/reports/full_benchmark/runs/altibase_source_preserving_20260520_090243/judge/judgments.jsonl`
- answers: `evals/altibase_answerability/reports/full_benchmark/runs/altibase_source_preserving_20260520_090243/answers/answers.jsonl`
- expected facts live in the question records under
  `evals/altibase_answerability/questions/*.jsonl` (field `expected_facts`).

Select **at least 40 (question_id, fact_id) pairs**, deliberately weighted:
- ~60% from facts whose judge `term_score` is in the 0.40–0.62 band (the
  paraphrase-suspect zone — read `notes` in `fact_results`);
- ~40% spread across clear covered and clearly-missed facts as anchors.

For each pair, read the expected fact text and the model answer, and assign a
**careful human-equivalent label**. Write one JSON object per line with fields:

- `question_id`, `fact_id`, `importance`
- `fact_text` (the expected fact)
- `answer` (the full model answer text for that question)
- `required_tokens` (the question's `required_tokens` list)
- `label`: `covered` or `not_covered` — your judgement of whether the answer
  substantively conveys the fact, regardless of exact wording
- `notes`: one short sentence justifying the label

Label by meaning, not by lexical overlap. A correct paraphrase counts as
`covered`. A confident but wrong or absent statement is `not_covered`.

### Part B — build the calibration script

Create `evals/altibase_answerability/scripts/calibrate_judge.py`.

It must:
- Be runnable from the repository root. It imports `judge_report` from
  `evals/altibase_answerability/scripts/`, so add that directory to `sys.path`
  explicitly — do not assume the current directory.
- Take `--gold <path>` (default the gold set above).
- For each gold entry, call `judge_report.py`'s
  `fact_match(fact_text, answer, required_tokens)` and read only its `.covered`
  attribute. Treat `fact_match(fact_text, answer, required_tokens) -> object
  with a .covered attribute` as a STABLE interface and depend on nothing else
  inside the judge — later jobs change the judge's internals.
- Compare `covered` against the gold `label`; print and write a short report:
  counts, precision, recall, and overall agreement (% of entries where judge
  `covered` == gold `label`).
- Exit 0 whenever it runs successfully (it is a measurement tool; it does not
  fail on low agreement — later jobs improve agreement).

## Constraints (non-negotiable)

- Create only the two new files above. Do not modify `judge_report.py` or
  `answer_runner.py` in this job. Do not touch `GPTs/upload_package/`.
- The gold set is calibration data used after the provider call. It is not
  answer-generation input, so reading judge-only `expected_facts` here is
  allowed and expected.

## Acceptance checks

```bash
test "$(wc -l < evals/altibase_answerability/fixtures/judge_gold_set.jsonl)" -ge 40
python3 -c "import json; [json.loads(l) for l in open('evals/altibase_answerability/fixtures/judge_gold_set.jsonl')]; print('gold json ok')"
python3 evals/altibase_answerability/scripts/calibrate_judge.py \
  --gold evals/altibase_answerability/fixtures/judge_gold_set.jsonl
git diff --check
```

## Completion protocol

As your final action:

- Ensure `evals/altibase_answerability/improvement/state/` exists.
- If every acceptance check passed, write
  `evals/altibase_answerability/improvement/state/02.result` with first line
  `PASS` and a short summary, including the baseline judge-vs-gold agreement %.
- Otherwise write the same file with first line `FAIL: <one-line reason>`.
