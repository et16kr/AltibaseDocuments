# Common Stage 2 Context

Use this file as shared context for every Stage 2 job.

## Source And Scope Contract

- Do not browse the web.
- Use only repository-local sources and the adjacent `~/AID` corpus.
- Korean Altibase manuals are authoritative for version-sensitive Altibase behavior.
- English manuals and AID English materials may be used according to their recorded
  authority, tier, auxiliary, source-limitation, and coverage classifications.
- Preserve exact product tokens: SQL syntax, DDL/DCL clauses, command options,
  property names, view and column names, error codes, API names, file paths, output
  tokens, patch identifiers, `BUG-*`, and `TASK-*`.
- Do not infer Altibase behavior from Oracle, MySQL, PostgreSQL, ANSI SQL, generic
  JDBC, generic ODBC, Kubernetes, or third-party assumptions.
- If a claim depends on exact customer environment, patch level, runtime output,
  object definitions, logs, installed tools, or live validation, ask for that missing
  input and provide the safest source-backed next check.

## Stage Boundary

Stage 2 creates the agent playbook layer from the validated Stage 1 source pack and
Korean-aligned English baseline.

Allowed outputs:

- `GPTs/agent_playbooks/*.md`
- `GPTs/agent_playbooks/playbook_manifest.tsv`
- `GPTs/agent_playbooks/playbook_validation.md`
- `GPTs/agent_playbooks/test_scenarios.md`
- `GPTs/agent_playbooks/scenario_judge_rubric.md`
- `GPTs/agent_playbooks/coding_agent_instruction_note.md`
- `GPTs/agent_playbooks/gpt_service_development_instruction_note.md`
- `GPTs/agent_playbooks/scripts/`
- `GPTs/reports/source_pack_to_playbook_crosswalk.tsv`
- `GPTs/reports/korean_aligned_english_to_playbook_crosswalk.tsv`
- `GPTs/reports/agent_playbook_gap_register.md`
- `GPTs/reports/customer_agent_enablement_stage_02_readiness.md`
- `GPTs/reports/stage_02_agent_playbooks_plan.md`
- `GPTs/reports/stage_02_preflight_status.md`

Do not edit original source files. Do not edit `GPTs/attachments/` or create
`GPTs/upload_package/` content in Stage 2. If a source, baseline, or authority problem
is found, record a blocker or gap instead of silently rewriting Stage 1 evidence.

## Required Files To Inspect

Read the relevant subset before editing:

- `AGENTS.md`
- `GPTs/reports/customer_agent_enablement_requirements.md`
- `GPTs/reports/customer_agent_enablement_stage_01_readiness.md`
- `GPTs/source_pack/source_manifest.tsv`
- `GPTs/source_pack/source_to_shard_manifest.tsv`
- `GPTs/source_pack/source_pack_validation.md`
- `GPTs/reports/aid_tier_manifest.tsv`
- `GPTs/korean_aligned_english/baseline_manifest.tsv`
- `GPTs/korean_aligned_english/alignment_validation.md`
- `GPTs/reports/source_pack_to_korean_aligned_english_crosswalk.tsv`
- `GPTs/reports/source_conflict_register.md`
- `GPTs/reports/agent_playbook_gap_register.md`

## Guardrails To Preserve

- `CONF-000004` through `CONF-000007` remain open guardrails for exhaustive tables,
  production operations, patch-specific behavior, AID upload composition, and live
  environment claims.
- `CONF-000008` is resolved only as a Stage 1 routing blocker; Stage 2 still must use
  exact source IDs, baseline block IDs, missing-input prompts, and recheck guardrails.
- `CONF-000009` remains a nonblocking exclusion: do not use `SRC-000109` or
  `SRC-000169` as authoritative customer-facing playbook content unless a later
  source-authority decision records a permitted use.
- Rows with `candidate_with_open_recheck_guardrail` may support guarded drafts only.
  They do not prove exhaustive or production-ready coverage.

## Playbook Shape

Each playbook should include, where source-backed and relevant:

- task purpose;
- supported versions;
- required customer inputs;
- source-backed assumptions;
- prerequisites;
- generated artifacts;
- commands, SQL, configuration, code, scripts, or test templates;
- step-by-step procedure;
- validation checks;
- expected result tokens;
- common errors and first checks;
- stop conditions;
- cleanup, rollback, or non-production test guidance;
- source IDs, source-pack block IDs, and Korean-aligned baseline block IDs.

Generated implementation artifacts must separate runnable SQL, commands,
configuration, code, and tests in fenced code blocks and must include validation checks
and safety warnings for destructive, privilege-changing, storage-changing,
replication-changing, or security-sensitive effects.

## Required Job Discipline

- Work only on the current job.
- Before editing, confirm project files outside `.codex-jobs/` are clean or stop.
- Keep Stage 2 changes source-backed and bounded.
- Add or update validation whenever the job creates a new machine-checkable contract.
- Run targeted checks and `git diff --check` on changed Stage 2 paths.
- Review the final diff.
- Commit the completed job with a focused commit message.
