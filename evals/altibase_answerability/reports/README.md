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

## Current Comparison Baselines

For the saved comparison between the 1st test before GPTs update and the 2nd test
after GPTs upgrade, use these run directories directly:

- 1st test, before GPTs update:
  `full_benchmark/runs/altibase_answerability_20260516_145452/`
- 2nd test, after GPTs upgrade:
  `full_benchmark/runs/altibase_answerability_20260517_095919/`

Open `summary.txt` first, then `judge/aggregate_report.json` and
`judge/judgments.jsonl` for structured comparison.

The root-cause analysis for these two runs is saved at
`full_benchmark/failure_root_cause_analysis_20260517.md`.

The final remediation-workflow rerun plan is saved at
`full_benchmark/rerun_plan_j022_20260517.md`. Use it for the next full live
270-question run after J004-J022 validation.
