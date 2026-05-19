# Scripts

This directory is reserved for benchmark tooling:

- question and manifest validation;
- attachments-only answer generation with leakage checks;
- source-backed judging;
- aggregate report generation;
- offline fixture checks.

Script jobs must keep model and provider settings configurable and include dry-run or
offline paths that do not require live model calls.

## Current Tooling

`validate_benchmark.py` validates the durable schemas, `policy.json`,
`source_taxonomy.json`, a manifest, and all selected JSONL question records.

`answer_runner.py` generates answer records from an explicitly allowlisted Markdown
context root. It projects each question to the policy allowlist, builds retrieval
context only from the manifest-selected context glob, checks that judge-only metadata
keys do not enter the projected input, prompt scaffold, or request payload, and writes
JSONL records that validate against
`schemas/answer_record.schema.json`.

`judge_report.py` judges answer records against the full source-backed question record
and writes `judgments.jsonl`, `aggregate_report.json`, and `report.md`. With
`--validate-output`, it also validates the input answer records before writing judge
outputs. The rule judge
scores fact coverage, critical fact coverage, required-token preservation, version
handling, Altibase-specific correctness, prohibited claims, and missing-input handling,
then applies readiness thresholds from `policy.json`.

Fixture validation:

```bash
python3 evals/altibase_answerability/scripts/validate_benchmark.py \
  --manifest evals/altibase_answerability/manifests/fixture_seed.json \
  --profile fixture
```

Full benchmark validation:

```bash
python3 evals/altibase_answerability/scripts/validate_benchmark.py \
  --manifest evals/altibase_answerability/manifests/<full-manifest>.json
```

The full profile fails when the manifest selects fewer than 200 questions or any domain
is below the required minimum in `policy.json`. The fixture profile keeps schema,
source-path, source-language, canonical-English, and answer-projection leakage checks
enabled, but skips production count gates so small offline samples can pass.

Answer-runner self-test:

```bash
python3 evals/altibase_answerability/scripts/answer_runner.py --self-test
```

Offline fixture answer generation:

```bash
python3 evals/altibase_answerability/scripts/answer_runner.py \
  --manifest evals/altibase_answerability/manifests/fixture_seed.json \
  --mode offline_fixture \
  --limit 2 \
  --validate-output \
  --output-dir /tmp/altibase-answer-runner-fixture
```

Dry-run projection and leakage audit:

```bash
python3 evals/altibase_answerability/scripts/answer_runner.py \
  --manifest evals/altibase_answerability/manifests/fixture_seed.json \
  --mode dry_run \
  --limit 2 \
  --validate-output \
  --output-dir /tmp/altibase-answer-runner-dry-run
```

Source-preserving package dry-run:

```bash
python3 evals/altibase_answerability/scripts/answer_runner.py \
  --manifest evals/altibase_answerability/manifests/full_benchmark_source_preserving_package.json \
  --mode dry_run \
  --context-mode lexical \
  --validate-output \
  --output-dir /tmp/altibase-source-preserving-package-dry-run
```

Coding-agent source-preserving validation and dry-run:

```bash
python3 evals/altibase_answerability/scripts/validate_benchmark.py \
  --manifest evals/altibase_answerability/manifests/coding_agent_source_preserving_package.json \
  --profile coding_agent

python3 evals/altibase_answerability/scripts/answer_runner.py \
  --manifest evals/altibase_answerability/manifests/coding_agent_source_preserving_package.json \
  --mode dry_run \
  --context-mode lexical \
  --validate-output \
  --output-dir /tmp/altibase-coding-agent-source-preserving-dry-run
```

Judge/report self-test:

```bash
python3 evals/altibase_answerability/scripts/judge_report.py --self-test
```

Offline fixture judging:

```bash
python3 evals/altibase_answerability/scripts/judge_report.py \
  --manifest evals/altibase_answerability/manifests/fixture_seed.json \
  --answers evals/altibase_answerability/fixtures/judge_answers.jsonl \
  --question-id PROP-001 \
  --question-id OPS-001 \
  --validate-output \
  --output-dir /tmp/altibase-judge-report-fixture
```

Live answer generation is provider-configurable. `provider=command` reads the rendered
prompt on stdin and writes the model answer on stdout:

```bash
python3 evals/altibase_answerability/scripts/answer_runner.py \
  --manifest evals/altibase_answerability/manifests/<manifest>.json \
  --mode live \
  --provider command \
  --model local-model-name \
  --provider-command "your-model-cli --arg value"
```

`provider=openai` is also supported when the optional `openai` Python package and
`OPENAI_API_KEY` are available. Large run payloads should be written under ignored
`reports/**/runs/` directories or outside the repository.
