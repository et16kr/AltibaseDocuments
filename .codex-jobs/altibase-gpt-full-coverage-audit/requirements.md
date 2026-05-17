# Workflow Requirements

## Purpose

Build a source-to-attachment proof that `GPTs/attachments/` is a source-exhaustive,
customer-usable Altibase GPT encyclopedia for the selected repository-local source
corpus.

This workflow is stricter than benchmark remediation. Benchmark results are evidence
for priority and validation, but completion requires item-level source coverage proof.

## Baseline Evidence

Use the latest full benchmark run as failure evidence:

- Run directory:
  `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_205641/`
- Summary: `101/270` passed, `169` failed, pass rate `37.4%`.
- Critical fact coverage: `85.1%`.
- Required token preservation: `90.1%`.
- Unsupported-claim rate: `1.1%`.
- Protected-topic blockers: `32`.
- Readiness decision: `blocking_gaps`.

Also use these earlier comparison runs when trend context matters:

- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260516_145452/`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_095919/`

Do not treat benchmark questions as the full audit scope. They are priority, targeted
answerability, retrieval-risk, exact-token, and protected-topic evidence.

## Non-Negotiable Objective

For every item in the selected source corpus, the audit must end with exactly one
traceable disposition:

- `Covered`: represented in `GPTs/attachments/` as an answer-ready block.
- `Covered-by-routing`: represented through a clearly linked attachment section and
  retrieval alias/index/routing entry.
- `Guardrail`: selected sources do not support a definitive customer answer, or the
  answer depends on exact version, patch level, environment, object definition, log
  excerpt, runtime output, installed tool behavior, or live integration state.
- `Out-of-scope`: outside the selected upload source corpus, with a reason recorded.
- `Missing`: source-backed and in scope but not answerable from the attachments.
- `Retrieval-weak`: present but unlikely to be found by GPT retrieval.

The final state must have no unresolved `Missing` or unresolved `Retrieval-weak` rows.

## Source Policy

- Use repository-local selected sources only. Do not browse the web.
- Do not invent Altibase behavior from generic Oracle or generic database knowledge.
- Korean Altibase manuals, release notes, patch notes, tool manuals, technical
  documents, and third-party guides are authoritative when Korean and English sources
  differ.
- English sources are extraction aids when consistent with Korean sources.
- Keep customer-facing attachments in clear English.
- Preserve established `Altibase 8.1 verified source` wording for 8.1-only material
  where the attachment set uses it.
- 7.1 and 7.3 claims require corresponding selected sources before broadening.
- Do not edit original manuals or source documents.

## Core Input Artifacts

Before editing or cataloging, inspect the job-relevant parts of:

- `AGENTS.md`
- `GPTs/attachments/README.md`
- `GPTs/GPT_Instructions_Draft.md`
- `GPTs/reports/source_inventory.md`
- `GPTs/reports/coverage_matrix.md`
- `GPTs/reports/gap_register.md`
- `GPTs/reports/final_upload_readiness.md`
- `GPTs/reports/answerability_failure_remediation_inventory_20260517.md`
- `evals/altibase_answerability/reports/full_benchmark/failure_root_cause_analysis_20260517.md`
- latest benchmark artifacts under
  `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_205641/`

Use selected source roots recorded in `GPTs/reports/source_inventory.md` and source
family ownership recorded in `GPTs/reports/coverage_matrix.md`.

## Required Output Artifacts

The workflow should create or update:

- `GPTs/reports/full_coverage_audit/source_corpus_lock.md`
- `GPTs/reports/full_coverage_audit/source_item_catalog.tsv`
- `GPTs/reports/full_coverage_audit/source_to_attachment_matrix.tsv`
- `GPTs/reports/full_coverage_audit/missing_item_register.md`
- `GPTs/reports/full_coverage_audit/guardrail_register.md`
- `GPTs/reports/full_coverage_audit/retrieval_weakness_register.md`
- `GPTs/reports/full_coverage_audit/remediation_log.md`
- `GPTs/reports/full_coverage_audit/final_full_coverage_audit.md`

The workflow may also update existing support reports when needed:

- `GPTs/reports/source_inventory.md`
- `GPTs/reports/coverage_matrix.md`
- `GPTs/reports/gap_register.md`
- `GPTs/reports/final_upload_readiness.md`

Customer-facing remediation should remain in:

- `GPTs/attachments/*.md`
- `GPTs/GPT_Instructions_Draft.md`

## Catalog Schema

`source_item_catalog.tsv` must be machine-checkable. Each row should contain at least:

- `source_item_id`: stable ID such as `SRC-PROP-7.3-000123`.
- `source_family`: source family from `GPTs/reports/coverage_matrix.md`.
- `version_scope`: `7.1`, `7.3`, `8.1`, `cross-version`, or `patch-specific`.
- `source_path`: repository-relative source file path.
- `source_heading`: heading path or nearest stable anchor.
- `item_type`: controlled category such as property, SQL syntax, command option, view,
  column, error code, API, runbook step, compatibility rule, version note, warning,
  example, or other documented category.
- `literal_tokens`: exact tokens that must survive into answers.
- `source_summary`: short normalized English summary.
- `attachment_target`: expected `GPTs/attachments/*.md` owner.
- `coverage_status`: one of the disposition values above.
- `attachment_anchor`: heading or line reference where represented.
- `guardrail_reason`: required for `Guardrail` or `Out-of-scope`.
- `audit_job`: job ID that created or last reviewed the row.
- `evidence`: command, grep, script, source locator, or review evidence.

Catalog jobs must preserve existing rows from earlier jobs and append or update only
their scoped rows. Do not overwrite unrelated catalog work.

## Answer-Ready Coverage Standard

An item is not covered merely because a related topic is mentioned. It is covered only
when the attachment contains enough structured context for a safe customer answer.

Minimum expectations by item type:

- Property: name, purpose, versions, default, allowed values/range, unit, mutability,
  dynamic-change support, restart/recreate requirement, change method, check SQL,
  related views, and cautions when source-backed.
- SQL syntax: exact syntax or BNF-like grammar, version availability, required
  privileges, object restrictions, destructive or transactional effects, examples, and
  validation SQL.
- View or dictionary item: exact view name, purpose, version availability, key columns,
  safe query timing, example check SQL, and patch-sensitive column warning when needed.
- Error code: exact code forms, symbol, message, cause, action, related
  properties/views, first checks, and required customer inputs.
- Tool or API: exact command/function/class/method/option names, file paths,
  environment prerequisites, call order, minimal example, expected output, and
  diagnostics.
- Runbook: prerequisites, current-state checks, exact commands or SQL, stop
  conditions, expected state transitions, rollback or escalation inputs, and validation
  checks.
- Compatibility or version rule: source version, affected feature, exact boundary,
  allowed/unsupported behavior, and required customer evidence when patch-specific.

## Workflow Method

Each job must complete only its scoped work and must not dilute the proof standard.

Required job pattern:

1. Reconfirm the job boundary from `jobs.tsv` and `jobs.md`.
2. Run or inspect the repository first checks from `AGENTS.md` when starting a review
   or remediation-cycle job.
3. Inspect relevant support reports, source roots, attachments, and benchmark evidence.
4. Catalog or remediate only the scoped source family or attachment group.
5. Update the relevant full coverage audit artifact.
6. Self-review for source backing, Korean-source precedence, exact tokens, guardrails,
   customer-facing English, and attachment routing.
7. Run scoped validation.
8. Review the final diff.
9. Create a focused git commit and leave project files clean.

Do not pause for step-by-step confirmation unless the job is unsafe, ambiguous enough
to risk wrong source claims, or blocked by missing information.

## Standard Verification

At minimum, each successful job should run:

```bash
git diff --check
bash review/scripts/run_review_stage.sh validate
rg -n "^Verdict:|^\\| (Blocker|High|Medium|Low) \\|" review/reports/R*.md
```

Catalog or matrix jobs should also run scoped TSV checks for:

- required columns;
- duplicate `source_item_id`;
- valid `coverage_status`;
- valid `version_scope`;
- non-empty `source_path`, `source_summary`, `audit_job`, and `evidence`;
- required `guardrail_reason` for `Guardrail` and `Out-of-scope`.

Answerability jobs should use the latest benchmark artifacts and run targeted checks
where feasible. Do not launch a full 270-question live benchmark unless the job prompt
explicitly decides that the runtime budget is suitable.

## Handoff

Each successful job must:

- update only its scoped files;
- preserve unrelated user changes;
- commit a focused result;
- commit scoped project files outside `.codex-jobs` unless
  `REQUIRE_PROJECT_COMMIT_AFTER_JOB=0` is explicitly set;
- let `run-all.sh` commit the `jobs.tsv` status transition unless
  `COMMIT_STATUS_AFTER_JOB=0` is explicitly set;
- leave project files clean after the commit;
- record skipped checks or residual risk explicitly in the relevant report.

If the worktree is dirty before a job starts outside `.codex-jobs/`, stop and report
the blocking files instead of continuing.
