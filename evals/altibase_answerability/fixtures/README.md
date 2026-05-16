# Fixtures

Fixtures are small calibration inputs for validator, answer-runner, judge, and report
tests. They should be small enough to run without the full benchmark or live model
calls.

Fixture question records must still be source-backed if they are real benchmark
questions. Synthetic fixtures used only for schema error handling should be clearly
named and kept out of production manifests.

## Current Fixtures

- `seed_questions.jsonl`: seven source-backed seed records, one per required benchmark
  domain. They are real benchmark examples but are intended for offline calibration, not
  for satisfying production count gates.

Run the seed fixture with:

```bash
python3 evals/altibase_answerability/scripts/validate_benchmark.py \
  --manifest evals/altibase_answerability/manifests/fixture_seed.json \
  --profile fixture
```

Run the answer runner against a small fixture slice without live model calls:

```bash
python3 evals/altibase_answerability/scripts/answer_runner.py \
  --manifest evals/altibase_answerability/manifests/fixture_seed.json \
  --mode offline_fixture \
  --limit 2 \
  --validate-output \
  --output-dir /tmp/altibase-answer-runner-fixture
```
