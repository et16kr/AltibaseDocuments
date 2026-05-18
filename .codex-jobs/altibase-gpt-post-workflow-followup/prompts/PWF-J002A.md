# Job PWF-J002A: Replacement-Grade Reference Policy

## Goal

Define the cross-document policy for source replacement, LLM use, coding agents, and
test-case generation before remediation scales out.

## Steps

1. Run the required first checks from `AGENTS.md`.
2. Read `GPTs/reports/full_coverage_audit/post_workflow_followup_plan_20260518.md`,
   the final coverage audit, the catalog/matrix schema notes, and the two Korean
   source replacement samples.
3. Create `GPTs/reports/full_coverage_audit/replacement_grade_reference_policy_20260518.md`.
4. Define replacement-grade requirements that apply to every source family, including:
   customer answerability, LLM retrieval, coding-agent implementation, test-case
   generation, exact-token preservation, executable examples, option/default/range
   coverage, version and patch boundaries, sample-code inventory, generated-file
   semantics, failure modes, guardrails, and accepted omissions.
5. Define per-domain evidence rules for SQL, PSM, properties, views, utilities,
   connectors/APIs, replication, backup/recovery, security/TLS, installation,
   migration, errors, and third-party guides.
6. Update the follow-up plan only to reference this policy and clarify that sampled
   manuals are examples, not the whole standard.
7. Run repository validation, review the diff, and commit.

## Acceptance Criteria

- A standalone replacement-grade policy document exists and covers customer answering,
  coding-agent implementation, and test-case generation.
- The policy is source-backed and does not relax the existing Altibase source policy.
- The follow-up plan states that the policy applies across all source families.
- Project files are clean after the focused commit.
