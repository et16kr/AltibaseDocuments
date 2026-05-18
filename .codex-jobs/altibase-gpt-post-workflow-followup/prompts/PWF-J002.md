# Job PWF-J002: Patch-Note Closure Design

## Goal

Design how to close active patch-note `Missing` rows before attachment edits.

## Steps

1. Run the required first checks from `AGENTS.md`.
2. Confirm `SRC-PATCH-PATCH-000001` through `SRC-PATCH-PATCH-000115` are still the
   active patch-note `Missing` rows.
3. Inspect representative early 7.1, late 7.1, and 7.3 patch-note files.
4. Create `GPTs/reports/full_coverage_audit/patch_note_closure_design_20260518.md`.
5. Define the closure shape for compact blocks, owner routing, possible row splitting,
   `Guardrail`, and `Out-of-scope`.
6. Run `python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers`,
   `git diff --check`, and `bash review/scripts/run_review_stage.sh validate`.
7. Review the diff and create a focused commit.

## Acceptance Criteria

- The design assigns the 115 rows to the small batches used by this workflow.
- It preserves exact patch versions and customer-answerable `BUG-*` / `TASK-*` tokens.
- It does not perform the broad remediation itself.
- Project files are clean after the focused commit.
