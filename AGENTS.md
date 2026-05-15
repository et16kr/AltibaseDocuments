# Repository Agent Notes

## Current Workflow

This repository is in an iterative Altibase GPT attachment review and remediation workflow.

The recurring loop is:

1. Fill or update staged review reports under `review/reports/`.
2. Use those findings to update customer-facing knowledge files under `GPTs/attachments/`.
3. Update supporting evidence such as `GPTs/reports/source_inventory.md` when source traceability changes.
4. Track remediation task state in `review/remediation_plan.md`.
5. Run the task-specific validation command before marking a task `Done`.

When the user mentions IDs such as `H01`, `M03`, `L08`, or `V02`, treat them as remediation task IDs from `review/remediation_plan.md`.

## First Checks

At the start of a review/remediation request, run or inspect:

```bash
bash GPTs/scripts/remediation_plan.sh status
rg -n "\| Progress \||\| Fail \||\| ToDo \|" review/remediation_plan.md
```

If any task is `Progress`, continue that task first unless the user explicitly redirects. If any task is `Fail`, inspect the task, the target files, and `review/remediation_failure_log.md` before deciding whether to retry, mark `Done`, or leave it failed.

## Review Report Phase

Review reports live in `review/reports/R*.md`.

When asked to review or fill review documents:

- Do not edit `GPTs/attachments/` directly during the pure review phase.
- Write findings with severity, file, line, finding, and recommendation.
- Prefer source-backed findings over broad style comments.
- Keep report conclusions actionable enough to become remediation tasks.
- R15 is a final readiness gate and should remain unresolved until underlying review-required reports or residual risks are handled.

## Remediation Phase

Remediation is driven by `review/remediation_plan.md`.

When asked to fix a task:

- Start from the plan row and related `review/reports/R*.md` findings.
- Mark the task `Progress` before editing when appropriate.
- Keep edits scoped to listed target files and directly required support files.
- Preserve customer-facing wording in `GPTs/attachments/`; do not expose local paths, internal job labels, or source inventory mechanics there.
- If source traceability changes, update `GPTs/reports/source_inventory.md`.
- Run the validation command in the plan row.
- Mark `Done` only when the required change is applied and validation evidence is acceptable.
- Mark `Fail` only when blocked or validation/review shows the task is incomplete.

Use the runner where practical:

```bash
bash GPTs/scripts/remediation_plan.sh show H01
bash GPTs/scripts/remediation_plan.sh start H01
bash GPTs/scripts/remediation_plan.sh validate H01
bash GPTs/scripts/remediation_plan.sh finish H01 Done
bash GPTs/scripts/remediation_plan.sh finish H01 Fail --force --reason "short failure reason"
```

## Failure Recording

Failure reasons must be preserved in `review/remediation_failure_log.md`.

The remediation runner records failures for `mark`, `finish`, and `run-all` paths. When manually marking a task `Fail`, always pass `--reason` with a concise cause. If a failure happened outside the runner, add a short entry to the failure log before moving on.

## Source Policy

Altibase version-sensitive claims must be source-backed.

- Use the selected manuals, release notes, technical documents, and source inventory already present in the repository.
- For 8.1-only material, preserve the established `Altibase 8.1 verified source` wording where the attachment set uses it.
- For 7.1 and 7.3 claims, check the corresponding manuals or approved supporting documents before broadening a statement.
- Do not replace an Altibase-specific rule with generic Oracle/database assumptions.

## Validation And Hygiene

Before finishing a task, check the relevant diff and validation output.

Useful commands:

```bash
git status --short
git diff --check
bash GPTs/scripts/remediation_plan.sh status
rg -n "^Verdict:|^\| (Blocker|High|Medium|Low) \|" review/reports/R*.md
```

Do not revert unrelated local changes. If unrelated modified files are present, leave them alone and mention them separately if they affect the requested work.
