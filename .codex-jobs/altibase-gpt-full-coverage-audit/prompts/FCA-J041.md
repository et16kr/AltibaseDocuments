# Job FCA-J041: Content remediation SQL data types and properties

## Goal

Fix missing source-backed items in SQL, data type, property, JSON, LOB, and Oracle-difference attachment areas.

## Job Focus

Content remediation SQL data types and properties

## Primary Inputs

- `GPTs/reports/full_coverage_audit/source_to_attachment_matrix.tsv`
- `GPTs/reports/full_coverage_audit/missing_item_register.md`
- `GPTs/reports/full_coverage_audit/retrieval_weakness_register.md`
- scoped GPTs/attachments files from jobs.md

## Expected Durable Output

- Remediated scoped attachment gaps with updated matrix/register dispositions and remediation log evidence.

## Remediation Guidance

- Start from `source_to_attachment_matrix.tsv` and the relevant register, not from broad manual spot checks.
- Keep edits bounded to the scoped attachment group and directly required support reports.
- Update matrix/register dispositions after remediation and record evidence in `remediation_log.md`.

## Scope

- Work only on this job.
- Use repository-relative paths; `run-all.sh` invokes Codex from the repository root by default.
- Preserve unrelated user changes and do not edit original manuals or source documents.
- Do not browse the web or use non-repository Altibase facts.
- Keep customer-facing attachment text in English and source-backed.
- Before editing, stop if uncommitted project files exist outside `.codex-jobs` workflow runtime/status files.

## Required Steps

1. Reconfirm the job requirement, source family or attachment boundary, and expected durable output.
2. Inspect `AGENTS.md`, the shared workflow requirements prepended by the orchestrator, and the relevant support reports/source files.
3. Run or inspect the first-check commands when starting a review/remediation-cycle job:
   ```bash
   bash review/scripts/run_review_remediation_cycle.sh status
   rg -n $'\t(Reviewing|Remediating|ReReviewing|Fail)$' review/review_remediation_cycle_status.tsv
   git status --short
   ```
4. Perform only the scoped catalog, matrix, remediation, validation, or final-report work.
5. Update the relevant full coverage audit artifact under `GPTs/reports/full_coverage_audit/` and any scoped attachments/support reports.
6. Self-review for source backing, Korean-source precedence, exact literal tokens, guardrails, customer-facing English, and retrieval routing.
7. Run scoped checks plus the standard verification commands:
   ```bash
   git diff --check
   bash review/scripts/run_review_stage.sh validate
   rg -n "^Verdict:|^\| (Blocker|High|Medium|Low) \|" review/reports/R*.md
   ```
8. Fix failures and rerun the relevant checks.
9. Review the final diff after checks pass.
10. Create a focused git commit for this job. Do not report success without a commit.

## Acceptance Criteria

- The job goal is complete for the scoped source family or attachment group.
- If this job updates catalog, matrix, register, or report rows, the rows are added or updated without overwriting unrelated rows.
- Any `Guardrail` or `Out-of-scope` row touched by this job has a specific reason and customer-facing missing-input or safest-next-check pattern.
- Relevant checks pass, or skipped checks are explicitly justified in the job output/report.
- The final diff is reviewed.
- The result is committed, and project files are clean after the commit.
