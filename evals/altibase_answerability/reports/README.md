# Reports

Generated aggregate reports and compact run summaries belong here. Large transient
payloads, raw prompts, raw model responses, and provider logs should be stored outside
version control or under ignored subdirectories.

Reports must be written in English and aggregate results by domain, subdomain, user
level, version scope, answer type, and retrieval risk.

`../scripts/judge_report.py` writes:

- `judgments.jsonl`: one source-backed judgment per answer record;
- `aggregate_report.json`: schema-validated readiness summary;
- `report.md`: human-readable readiness report with thresholds, domain results,
  protected-topic blockers, and top remediation targets.

Large per-run outputs should stay under ignored `runs/` directories or outside the
repository, for example `/tmp/altibase-judge-report-fixture`.
