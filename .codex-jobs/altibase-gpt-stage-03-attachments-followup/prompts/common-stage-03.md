# Common Stage 3 Context

Use this shared context for every Stage 3 job.

## Source And Scope Contract

- Do not browse the web.
- Use only repository-local sources and the adjacent `~/AID` corpus.
- Korean Altibase manuals are authoritative for version-sensitive Altibase behavior.
- English manuals, AID English materials, Stage 1 source pack, Korean-aligned English
  baseline, and Stage 2 playbooks may be used only according to their recorded
  authority, tier, source-limitation, auxiliary, and guardrail classifications.
- Preserve exact product tokens: SQL syntax, DDL/DCL clauses, commands, command
  options, property names, view and column names, error codes, API names, file paths,
  output tokens, patch identifiers, `BUG-*`, and `TASK-*`.
- Do not infer Altibase behavior from Oracle, MySQL, PostgreSQL, ANSI SQL, generic
  JDBC, generic ODBC, Kubernetes, or third-party assumptions.
- If an attachment answer depends on exact customer environment, patch level, runtime
  output, object definitions, logs, installed tools, or live validation, ask for that
  missing input and provide the safest source-backed next check.

## Stage Boundary

Stage 3 replans and performs only the still-needed answer-ready attachment follow-up
work using:

- validated Stage 1 source pack;
- Korean-aligned English baseline;
- durable benchmark evidence and gap inventories;
- Stage 2 playbooks, manifests, crosswalks, scenario files, and guardrails.

Stage 3 preparation starts from commit `5538c9a8`.

Allowed outputs:

- edits to existing `GPTs/attachments/*.md`;
- `GPTs/attachments/scripts/`;
- `GPTs/reports/stage_03_preflight_status.md`;
- `GPTs/reports/stage_03_attachments_followup_plan.md`;
- `GPTs/reports/stage_03_attachment_followup_scope.tsv`;
- `GPTs/reports/source_pack_to_attachment_crosswalk.tsv`;
- `GPTs/reports/korean_aligned_english_to_attachment_crosswalk.tsv`;
- `GPTs/reports/playbook_to_attachment_crosswalk.tsv`;
- `GPTs/reports/stage_03_attachment_validation.md`;
- updates to `GPTs/reports/agent_playbook_gap_register.md`;
- `GPTs/reports/customer_agent_enablement_stage_03_readiness.md`.

Do not edit original source files. Do not create `GPTs/upload_package/` content in
Stage 3. Keep the attachment set at exactly 20 customer-facing Markdown files under
`GPTs/attachments/`, excluding `README.md`; do not add new attachment package files.

## Required Files To Inspect

Read the relevant subset before editing:

- `AGENTS.md`
- `GPTs/reports/customer_agent_enablement_requirements.md`
- `GPTs/reports/customer_agent_enablement_stage_01_readiness.md`
- `GPTs/reports/customer_agent_enablement_stage_02_readiness.md`
- `GPTs/source_pack/source_manifest.tsv`
- `GPTs/source_pack/source_to_shard_manifest.tsv`
- `GPTs/source_pack/source_pack_validation.md`
- `GPTs/reports/source_pack_to_korean_aligned_english_crosswalk.tsv`
- `GPTs/korean_aligned_english/baseline_manifest.tsv`
- `GPTs/korean_aligned_english/alignment_validation.md`
- `GPTs/agent_playbooks/playbook_manifest.tsv`
- `GPTs/agent_playbooks/playbook_validation.md`
- `GPTs/reports/source_pack_to_playbook_crosswalk.tsv`
- `GPTs/reports/korean_aligned_english_to_playbook_crosswalk.tsv`
- `GPTs/reports/answerability_failure_remediation_inventory_20260517.md`
- `GPTs/reports/exact_token_gap_inventory_20260517.md`
- `GPTs/reports/source_conflict_register.md`
- `GPTs/reports/agent_playbook_gap_register.md`
- 2nd answerability benchmark run:
  `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_095919/`

## Guardrails To Preserve

- `APB-000014` test generation remains `planned` and blocked/deferred. Stage 3 must
  not present it as a complete customer-facing source-backed test-generation playbook.
- Scenario files are validation scenarios with `Not run` placeholders, not evidence
  that generated answers passed live judging.
- `CONF-000004` through `CONF-000007` remain open guardrails for exhaustive tables,
  production operations, patch-specific behavior, AID upload composition, and live
  environment claims.
- `CONF-000008` is closed only as a Stage 1 routing blocker; item-level attachment
  claims still require exact source IDs, source-pack blocks, and recheck handling.
- `CONF-000009` remains a nonblocking exclusion: do not use `SRC-000109` or
  `SRC-000169` as authoritative customer-facing attachment content unless a later
  source-authority decision records a permitted use.
- Files under `GPTs/upload_package/` are Stage 4 outputs, not Stage 3 outputs.

## Attachment Shape

Customer-facing attachment edits should keep or improve:

- `Applicable Versions`;
- `Questions This File Can Answer`;
- `Retrieval Alias Index`;
- `Source Documents`;
- `Response Rules`;
- `Attachment Cross-References`;
- `Residual Scope`;
- source-backed answer blocks with exact tokens, practical examples, validation
  checks, missing-input prompts, stop conditions, and cleanup or rollback notes where
  relevant.

Use concise customer-safe source labels, not local paths. For Altibase 8.1-only
material, preserve `Altibase 8.1 verified source` wording where the attachment set
uses it.

## Required Job Discipline

- Work only on the current job.
- Before editing, confirm project files outside `.codex-jobs/` are clean or stop.
- Open the selected source routes before adding or broadening customer-facing product
  behavior.
- Use Stage 2 playbooks as routing and guardrail evidence, not as replacement for
  exact source checks.
- If source support is weak, record a gap or limitation instead of adding the claim.
- Run targeted checks and `git diff --check` on changed Stage 3 paths.
- Review the final diff.
- Commit the completed job with a focused commit message.
