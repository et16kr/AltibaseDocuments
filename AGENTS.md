# Repository Agent Notes

## Current Workflow

This repository is in a staged Altibase GPT attachment review/remediation cycle.

The active loop is:

1. Run review stages from `review/review_stages.tsv`.
2. Write one report per stage under `review/reports/R*.md`.
3. If a report has actionable findings, update the scoped files under `GPTs/attachments/`
   and directly required support files such as `GPTs/reports/source_inventory.md`.
4. Re-run validation and the same review stage.
5. Commit the stage when the report reaches `Verdict: Pass` with no actionable
   `Blocker`, `High`, `Medium`, or `Low` findings.

## First Checks

At the start of a review/remediation-cycle request, run or inspect:

```bash
bash review/scripts/run_review_remediation_cycle.sh status
rg -n $'\t(Reviewing|Remediating|ReReviewing|Fail)$' review/review_remediation_cycle_status.tsv
git status --short
```

If any stage is `Reviewing`, `Remediating`, or `ReReviewing`, inspect the relevant
report, target files, and worktree before continuing. If any stage is `Fail`, inspect
the failure context before resetting or rerunning it.

## Review Report Phase

Review reports live in `review/reports/R*.md`.

When asked to review or fill review documents:

- Do not edit `GPTs/attachments/` directly during a pure review phase.
- Write findings with severity, file, line, finding, and recommendation.
- Prefer source-backed findings over broad style comments.
- Keep report conclusions actionable enough for scoped remediation.
- The final readiness stage is the last `G5_Retrieval` stage in
  `review/review_stages.tsv` and should remain unresolved until upstream review-required
  findings or accepted residual risks are handled.

Use the review stage runner for staged report generation:

```bash
bash review/scripts/run_review_stage.sh list
bash review/scripts/run_review_stage.sh clear
bash review/scripts/run_review_stage.sh run-all
```

Stage status is tracked in `review/review_stage_status.tsv`, not inferred from whether
a report file exists. A report file may be partial if a run ended while writing.

## Review/Remediation Cycle

Use the cycle runner for the current end-to-end process:

```bash
bash review/scripts/run_review_remediation_cycle.sh status
DRY_RUN=1 bash review/scripts/run_review_remediation_cycle.sh run-all
bash review/scripts/run_review_remediation_cycle.sh run-all
bash review/scripts/run_review_remediation_cycle.sh run R00
bash review/scripts/run_review_remediation_cycle.sh reset R00
```

Bare `run-all` means run all remaining non-`Done` review stages in
`review/review_stages.tsv` order. It should not be treated as a one-stage command.

The cycle runner:

- Refuses to start a stage when uncommitted project files are present.
- Runs the read-only review stage first.
- Remediates only when the report verdict or severity table indicates actionable work.
- Runs common validation before re-reviewing.
- Commits each completed stage before moving to the next stage.

## Source Policy

Altibase version-sensitive claims must be source-backed.

- Korean Altibase manuals are the authoritative latest manual source. If Korean and
  English manuals differ, treat the Korean manual as the source of truth and update or
  normalize English-facing artifacts from the Korean source.
- Keep customer-facing attachments in clear English unless the file explicitly requires
  otherwise; do not copy Korean prose directly into `GPTs/attachments/` without
  translating and normalizing it.
- Use the selected manuals, release notes, technical documents, and source inventory
  already present in the repository.
- For 8.1-only material, preserve the established `Altibase 8.1 verified source`
  wording where the attachment set uses it.
- For 7.1 and 7.3 claims, check the corresponding manuals or approved supporting
  documents before broadening a statement.
- Do not replace an Altibase-specific rule with generic Oracle/database assumptions.

## Validation And Hygiene

Before finishing a task, check the relevant diff and validation output.

Useful commands:

```bash
git status --short
git diff --check
bash review/scripts/run_review_stage.sh validate
rg -n "^Verdict:|^\| (Blocker|High|Medium|Low) \|" review/reports/R*.md
```

Do not revert unrelated local changes. If unrelated modified files are present, leave
them alone and mention them separately if they affect the requested work.
