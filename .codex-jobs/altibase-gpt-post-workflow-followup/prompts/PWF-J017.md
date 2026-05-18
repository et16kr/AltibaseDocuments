# Job PWF-J017: Protected-Topic Blocker Classification

## Goal

Classify every protected-topic blocker from `altibase_answerability_20260518_091947`
by primary cause.

## Steps

1. Run the required first checks from `AGENTS.md`.
2. Inspect `judgments.jsonl`, `answers.jsonl`, selected attachment context, and source
   or attachment evidence for all 36 protected blockers.
3. Create `GPTs/reports/full_coverage_audit/protected_blocker_classification_20260518.md`.
4. Classify each blocker as content, retrieval, synthesis, guardrail, or judge
   calibration.
5. Assign blocker rows to `PWF-J018` through `PWF-J022`.
6. Run `git diff --check` and review-stage validate.
7. Review the diff and create a focused commit.

## Acceptance Criteria

- All 36 protected blockers have primary cause, evidence, and owner job.
- Judge-only classifications include context, answer, source, token, and expected-fact evidence.
- Project files are clean after the focused commit.
