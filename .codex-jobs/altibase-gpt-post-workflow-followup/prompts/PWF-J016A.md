# Job PWF-J016A: Replacement-Grade Gap Register

## Goal

Apply the replacement-grade policy across source families and assign cross-document
gaps to owner jobs.

## Steps

1. Run the required first checks from `AGENTS.md`.
2. Read `GPTs/reports/full_coverage_audit/replacement_grade_reference_policy_20260518.md`, the final coverage audit,
   the catalog, the matrix, and the latest source-replacement samples.
3. Create `GPTs/reports/full_coverage_audit/replacement_grade_gap_register_20260518.md`.
4. Review every source family at the level needed to identify replacement-grade gaps,
   not only active `Missing` rows. At minimum, check whether each source family has
   owner blocks for exact commands/options, defaults/ranges, code/API contracts,
   runnable examples, diagnostics, failure modes, generated files, version boundaries,
   and test-case generation anchors.
5. Classify each gap as `content`, `retrieval`, `synthesis`, `guardrail`, or
   `accepted omission`, and assign an owner job. Use `PWF-J016B` for version,
   release-note, platform, and patch-note gaps; use `PWF-J018` through `PWF-J031A`
   for protected-topic, domain, answer-contract, developer, or test-readiness gaps.
6. For every source family with no gap, record the evidence basis and representative
   exact-token checks.
7. Run full coverage structural checks, `git diff --check`, review-stage validate,
   review the diff, and commit.

## Acceptance Criteria

- The gap register covers all source families, not only SSL/TLS and iSQL.
- Every replacement-grade gap has a type, source evidence, attachment owner, and owner
  job or explicit accepted-omission rationale.
- No final-readiness claim is made while unassigned replacement-grade gaps remain.
- Project files are clean after the focused commit.
