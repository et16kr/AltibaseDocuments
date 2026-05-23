# Job 03 — C3-03 Enlarge the coding-agent question suite

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Master plan: `GPTs/reports/answerability_improvement_cycle3_plan_20260522.md` —
  item C3-03.
- Evidence: `evals/altibase_answerability/reports/full_rerun_analysis_cycle2_20260520.md`
  section **6, target 5** — the coding-agent suite has only 10 questions, so the
  cycle-2 critical-fact-coverage gain of +16.7 pp produced **no** pass-rate
  movement (it stayed 2/10). The suite is too coarse to register coverage gains.
- The coding-agent question set is
  `evals/altibase_answerability/questions/coding_agent_source_preserving.jsonl`
  (10 records, ID field `id`, e.g. `AGENT-001`). Its manifest
  `evals/altibase_answerability/manifests/coding_agent_source_preserving_package.json`
  references that file **by path** in `question_files` and does not enumerate
  individual question IDs — so growing the `.jsonl` needs **no manifest edit**.
- `validate_benchmark.py --profile coding_agent` enforces
  `CODING_AGENT_MIN_QUESTIONS = 10` as a **minimum** (more is allowed) and
  requires every `agent_task_type` in `CODING_AGENT_TASK_TYPES` to be covered:
  `source_navigation`, `sql_isql_generation`, `driver_api_usage`,
  `error_diagnosis`, `property_version_check`, `replication_safety`,
  `backup_recovery_safety`, `destructive_operation_safety`, `security_safety`.

## Task

Grow the coding-agent question suite so coverage gains register as pass-rate
movement.

1. **Study the existing suite.** Read the 10 `AGENT-*` records and confirm the
   exact schema and field set (`id`, `agent_task_type`, `domain`, `subdomain`,
   `question`, `expected_facts`, `required_tokens`, `source_refs`,
   `prohibited_claims`, `expected_artifacts`, `citation_requirements`,
   `safety_gates`, `scoring_notes`, difficulty/level fields, etc.). New
   questions must follow that schema exactly.
2. **Add new questions to reach ≥ 30 total** (~20 new records). Continue the ID
   numbering contiguously (`AGENT-011`, `AGENT-012`, …). Spread the new
   `agent_task_type` values across all nine task types above so the suite stays
   balanced and every task type keeps coverage.
3. **Every new question must be answerable from `GPTs/upload_package/`.** For
   each new record, confirm the facts, `required_tokens`, and `source_refs`
   actually exist in the upload-package source bodies — open the referenced
   shards and verify. Do not write a question whose answer is not in the pack.
4. **Do not edit any source body or the manifest.** `GPTs/upload_package/` and
   `coding_agent_source_preserving_package.json` are read-only here. This job
   only adds question records to the `.jsonl` file.
5. Keep the new questions deterministic and self-contained, with no leakage of
   judge-only fields into the `question` prompt text.

## Constraints (non-negotiable)

- Modify only
  `evals/altibase_answerability/questions/coding_agent_source_preserving.jsonl`.
- Do NOT touch `GPTs/upload_package/` source bodies or any manifest JSON.
- Do not run `run-all.sh` or other jobs' files.

## Acceptance checks

```bash
# >= 30 questions, all valid JSONL, unique ids (question records use the `id` field):
python3 -c "import json; rows=[json.loads(l) for l in open('evals/altibase_answerability/questions/coding_agent_source_preserving.jsonl') if l.strip()]; print('coding-agent questions:', len(rows)); assert len(rows)>=30, len(rows); ids=[r['id'] for r in rows]; assert len(ids)==len(set(ids)), 'duplicate ids'; tt={r['agent_task_type'] for r in rows}; want={'source_navigation','sql_isql_generation','driver_api_usage','error_diagnosis','property_version_check','replication_safety','backup_recovery_safety','destructive_operation_safety','security_safety'}; assert want<=tt, sorted(want-tt)"
# Benchmark validation for the coding-agent profile passes:
python3 evals/altibase_answerability/scripts/validate_benchmark.py \
  --manifest evals/altibase_answerability/manifests/coding_agent_source_preserving_package.json \
  --profile coding_agent
# Harness self-tests stay green:
python3 evals/altibase_answerability/scripts/answer_runner.py --self-test
python3 evals/altibase_answerability/scripts/judge_report.py --self-test
git diff --check
```

## Completion protocol

As your final action:

- Ensure `evals/altibase_answerability/improvement3/state/` exists.
- If every acceptance check passed, write
  `evals/altibase_answerability/improvement3/state/03.result` with first line
  `PASS` and a short summary (question count before/after, task-type spread,
  how source-backing was verified).
- Otherwise write the same file with first line `FAIL: <one-line reason>`.
