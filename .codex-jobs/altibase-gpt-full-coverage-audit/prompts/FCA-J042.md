# Job FCA-J042: Content remediation migration cloud spatial and integrations

## Goal

Fix missing source-backed items in migration, Oracle compatibility, Kubernetes, AKU, Spatial, NiFi, Tableau, and miscellaneous integration attachment areas.

## Job Focus

Content remediation: migration/cloud/spatial/integrations

## Primary Inputs

- `GPTs/reports/full_coverage_audit/source_to_attachment_matrix.tsv`
- `GPTs/attachments/15_migration_oracle_compatibility.md`
- `GPTs/attachments/17_kubernetes_aku_cloud.md`
- `GPTs/attachments/19_spatial_nifi_tableau_misc.md`

## Expected Durable Output

- Fix missing source-backed rows in migration, Oracle compatibility, Kubernetes, AKU, Spatial, NiFi, Tableau, and miscellaneous integration areas.
- Update remediation_log.md and matrix dispositions.

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
- Before editing, stop if uncommitted project files exist outside `.codex-jobs/` workflow directories.

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
