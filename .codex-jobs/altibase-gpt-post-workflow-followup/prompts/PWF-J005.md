# Job PWF-J005: Patch-Note Closure 7.1 021-030

## Goal

Close or justify `SRC-PATCH-PATCH-000021` through `SRC-PATCH-PATCH-000030`.

## Steps

1. Run the required first checks from `AGENTS.md`.
2. Read `GPTs/reports/full_coverage_audit/replacement_grade_reference_policy_20260518.md`, then inspect the scoped
   catalog/matrix rows and corresponding patch-note source files.
3. Update `GPTs/attachments/00_version_release_platform.md`, catalog, matrix,
   `missing_item_register.md`, and `remediation_log.md` as required.
4. Preserve exact patch versions, `BUG-*` / `TASK-*` tokens, affected area, caveat,
   and owner-attachment routing.
5. Run:
   - `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers`
   - `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py catalog-qa`
   - `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py matrix-qa`
   - `git diff --check`
   - `bash review/scripts/run_review_stage.sh validate`
6. Review the diff and create a focused commit.

## Acceptance Criteria

- Rows `000021` through `000030` are no longer active `Missing` rows.
- Exact patch versions and customer-answerable tokens are preserved.
- Structural checks, repository validation, final diff review, and a focused commit are complete.
