# Common Stage 4 Context

Use this shared context for every Stage 4 job.

## Source And Scope Contract

- Do not browse the web.
- Use only repository-local sources and the adjacent `~/AID` corpus.
- Korean Altibase manuals are authoritative for version-sensitive Altibase behavior.
- English manuals, AID English materials, Stage 1 source pack, Korean-aligned English
  baseline, Stage 2 playbooks, and Stage 3 attachments may be used only according to
  their recorded authority, tier, source-limitation, auxiliary, and guardrail
  classifications.
- Preserve exact product tokens: SQL syntax, DDL/DCL clauses, commands, command
  options, property names, view and column names, error codes, API names, file paths,
  output tokens, patch identifiers, `BUG-*`, and `TASK-*`.
- Do not infer Altibase behavior from Oracle, MySQL, PostgreSQL, ANSI SQL, generic
  JDBC, generic ODBC, Kubernetes, or third-party assumptions.
- If an upload-package answer depends on exact customer environment, patch level,
  runtime output, object definitions, logs, installed tools, or live validation, the
  package must preserve a missing-input prompt and the safest source-backed next
  check.

## Stage Boundary

Stage 4 assembles the final GPT Knowledge upload package from the validated layers:

- `GPTs/source_pack/`: source-preserving routes and authority labels;
- `GPTs/korean_aligned_english/`: Korean-aligned English baseline and AID
  classifications;
- `GPTs/agent_playbooks/`: task and coding-agent playbook routes;
- `GPTs/attachments/`: concise answer-ready customer references.

Stage 4 may create or update:

- `GPTs/upload_package/*.md`;
- `GPTs/reports/stage_04_upload_package_plan.md`;
- `GPTs/reports/stage_04_upload_package_manifest.tsv`;
- `GPTs/reports/stage_04_upload_package_validation.md`;
- `GPTs/reports/source_pack_to_upload_package_crosswalk.tsv`;
- `GPTs/reports/korean_aligned_english_to_upload_package_crosswalk.tsv`;
- `GPTs/reports/playbook_to_upload_package_crosswalk.tsv`;
- `GPTs/reports/attachment_to_upload_package_crosswalk.tsv`;
- `GPTs/reports/customer_agent_enablement_stage_04_readiness.md`;
- a validation helper under `GPTs/reports/scripts/` if a reusable validator is needed;
- limited updates to `GPTs/reports/agent_playbook_gap_register.md`,
  `GPTs/reports/source_conflict_register.md`, or
  `GPTs/reports/final_upload_readiness.md` when required by the job.

Do not edit original manuals, release notes, technical documents, AID source files, or
benchmark expected-answer files. Do not treat files outside `GPTs/upload_package/` as
final upload files unless they are intentionally copied or transformed into that
directory and listed in the Stage 4 upload manifest.

## Required Files To Inspect

Read the relevant subset before editing:

- `AGENTS.md`
- `GPTs/reports/customer_agent_enablement_requirements.md`
- `GPTs/reports/customer_agent_enablement_stage_01_readiness.md`
- `GPTs/reports/customer_agent_enablement_stage_02_readiness.md`
- `GPTs/reports/customer_agent_enablement_stage_03_readiness.md`
- `.codex-jobs/altibase-gpt-stage-03-attachments-followup/jobs.tsv`
- `GPTs/source_pack/source_manifest.tsv`
- `GPTs/source_pack/source_pack_validation.md`
- `GPTs/korean_aligned_english/baseline_manifest.tsv`
- `GPTs/korean_aligned_english/alignment_validation.md`
- `GPTs/agent_playbooks/playbook_manifest.tsv`
- `GPTs/agent_playbooks/playbook_validation.md`
- `GPTs/reports/stage_03_attachment_followup_scope.tsv`
- `GPTs/reports/source_pack_to_attachment_crosswalk.tsv`
- `GPTs/reports/korean_aligned_english_to_attachment_crosswalk.tsv`
- `GPTs/reports/playbook_to_attachment_crosswalk.tsv`
- `GPTs/reports/source_conflict_register.md`
- `GPTs/reports/agent_playbook_gap_register.md`
- `GPTs/reports/final_upload_readiness.md`
- 2nd answerability benchmark run:
  `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_095919/`

## Guardrails To Preserve

- The final GPT Knowledge upload package must be 20 Markdown files or fewer,
  including any AID-derived content.
- Auxiliary manifests, reports, scripts, and validation artifacts must remain outside
  `GPTs/upload_package/` unless they are intentionally counted as upload Markdown.
- `APB-000014` test generation remains `planned` and blocked/deferred unless a later
  scoped job creates and validates a source-ID-backed test-generation playbook. Stage 4
  may record final exclusion or deferral, but must not silently mark it complete.
- Scenario files remain validation scenarios with `Not run` placeholders unless a job
  actually runs and records scenario results.
- `CONF-000004` through `CONF-000007` remain open guardrails for exhaustive tables,
  production operations, patch-specific behavior, AID upload composition, and live
  environment claims.
- `CONF-000008` is closed only as a Stage 1 routing blocker; item-level upload-package
  claims still require exact source IDs, source-pack blocks, and recheck handling.
- `CONF-000009` remains a nonblocking exclusion: do not use `SRC-000109` or
  `SRC-000169` as authoritative upload-package content unless a later source-authority
  decision records a permitted use.
- Do not claim final upload readiness, live benchmark readiness, or production
  operational certainty unless the corresponding validation evidence exists.

## Upload Package Shape

The default target is a maximum of 20 Markdown files under `GPTs/upload_package/`.
Use the existing 20 attachment filenames only if the Stage 4 composition plan confirms
that source-preserving, playbook, and AID routing can be integrated without adding
extra upload Markdown. If the package uses fewer files or merged files, record the
mapping in `stage_04_upload_package_manifest.tsv`.

Each upload Markdown file should preserve or improve:

- applicable versions and authority labels;
- source-boundary or source-route notes where needed for source-backed synthesis;
- task/playbook routing for coding agents and customer-owned LLMs;
- answer-ready reference content from Stage 3 attachments;
- missing-input prompts, stop conditions, validation checks, and rollback or cleanup
  notes for protected operations;
- cross-references to related upload-package files;
- residual scope and known limitations.

Do not expose local workspace paths, local branch names, temporary run directories, or
internal workflow implementation details in upload Markdown. Source IDs and block IDs
may appear only if the Stage 4 package format explicitly uses them as source-boundary
metadata; otherwise keep internal IDs in manifests and crosswalks outside the package.

## Required Job Discipline

- Work only on the current job.
- Before editing, confirm project files outside `.codex-jobs/` are clean or stop.
- Open the selected source routes before adding or broadening customer-facing product
  behavior.
- Use Stage 2 playbooks and Stage 3 crosswalks as routing and guardrail evidence, not
  as replacements for exact source checks.
- If source support is weak, record a gap, exclusion, or limitation instead of adding
  the claim.
- Keep `GPTs/upload_package/` deterministic: generated files must be reproducible from
  the recorded plan, manifest, and selected source layers.
- Run targeted checks and `git diff --check` on changed Stage 4 paths.
- Review the final diff.
- Commit the completed job with a focused commit message.

