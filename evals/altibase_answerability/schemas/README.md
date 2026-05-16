# Schemas

These schemas define the durable benchmark exchange formats.

- `policy.schema.json`: benchmark policy and readiness thresholds.
- `question.schema.json`: one source-backed benchmark question record.
- `manifest.schema.json`: run manifest selecting question files and run options.
- `answer_record.schema.json`: attachments-only answer runner output.
- `judgment.schema.json`: source-backed judgment for one answer.
- `aggregate_report.schema.json`: manifest-level readiness report.
- `source_taxonomy.schema.json`: source-family, domain, user-level, version, target-count,
  and retrieval-risk coverage map for question-generation jobs.

Later script jobs should validate JSON and JSONL files against these schemas before
running answer generation or judging.

`../scripts/validate_benchmark.py` checks that every schema is itself valid,
then validates policy, taxonomy, manifest, and question JSONL records. It also applies
cross-record rules that JSON Schema cannot express, including unique question IDs,
source-reference integrity, canonical-English expected facts, repository-local
`source_path` existence, and answer-projection leakage boundaries.

`../scripts/answer_runner.py --validate-output` validates generated answer records
against `answer_record.schema.json` while running dry-run, offline fixture, or live
answer-generation modes.

`../scripts/judge_report.py --validate-output` validates generated per-question
judgments against `judgment.schema.json` and aggregate readiness reports against
`aggregate_report.schema.json`.
