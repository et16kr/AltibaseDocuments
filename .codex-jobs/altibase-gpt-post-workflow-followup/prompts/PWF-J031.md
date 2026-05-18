# Job PWF-J031: Answer Contract And Instruction Check

## Goal

Use instruction-aware targeted checks to separate answer synthesis gaps from attachment
or retrieval gaps.

## Steps

1. Run the required first checks from `AGENTS.md`.
2. Select representative synthesis-gap examples from residual/domain validation
   reports and replacement-grade gap evidence.
3. Run dry-run validation for `targeted_calibration_j019_instruction.json`.
4. Run bounded live targeted checks for the selected examples, or write an explicit
   blocker section explaining why live checks cannot be executed.
5. Update `GPTs/GPT_Instructions_Draft.md` only for narrow, evidence-backed synthesis gaps.
6. Create `GPTs/reports/full_coverage_audit/instruction_aware_check_20260518.md`.
7. Run repository validation, review the diff, and commit.

## Acceptance Criteria

- The report separates attachment/retrieval gaps from answer synthesis gaps.
- The report does not use instruction edits to hide replacement-grade content gaps.
- Live targeted-check evidence is recorded, or an explicit execution blocker is
  documented.
- Instruction edits do not authorize unsupported claims.
- Project files are clean after the focused commit.
