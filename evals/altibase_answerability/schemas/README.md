# Schemas

These schemas define the durable benchmark exchange formats.

- `policy.schema.json`: benchmark policy and readiness thresholds.
- `question.schema.json`: one source-backed benchmark question record.
- `manifest.schema.json`: run manifest selecting question files and run options.
- `answer_record.schema.json`: attachments-only answer runner output.
- `judgment.schema.json`: source-backed judgment for one answer.
- `aggregate_report.schema.json`: manifest-level readiness report.

Later script jobs should validate JSON and JSONL files against these schemas before
running answer generation or judging.
