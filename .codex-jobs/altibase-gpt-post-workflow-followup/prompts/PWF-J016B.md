# Job PWF-J016B: Replacement Remediation Version Release Platform

## Goal

Remediate replacement-grade version, release-note, platform, and patch-note gaps
assigned by the cross-document gap register.

## Steps

1. Run the required first checks from `AGENTS.md`.
2. Read `GPTs/reports/full_coverage_audit/replacement_grade_reference_policy_20260518.md`,
   `GPTs/reports/full_coverage_audit/replacement_grade_gap_register_20260518.md`,
   `GPTs/reports/full_coverage_audit/final_full_coverage_audit.md`, the catalog, the
   matrix, and the missing register.
3. Identify gap-register rows whose owner area is version, release notes, platform
   support, install/upgrade/downgrade/uninstall, package boundaries, compatibility, or
   patch-note coverage.
4. Update only `GPTs/attachments/00_version_release_platform.md` and directly required
   audit support files unless the gap evidence proves another attachment is the owner.
5. Preserve exact version, patch, BUG/TASK, platform, package, install/upgrade,
   downgrade/uninstall, compatibility, generated-file, and unsupported-boundary tokens
   needed for customer Q&A, coding-agent implementation, and test-case generation.
6. If the assigned gaps are too broad for one execution, create an explicit not-ready
   report under `GPTs/reports/full_coverage_audit/` with proposed follow-up jobs and
   stop before claiming readiness.
7. Run full coverage structural checks, targeted retrieval checks for changed anchors,
   `git diff --check`, review-stage validate, review the diff, and commit.

## Acceptance Criteria

- All gap-register rows in the version/release/platform/patch-note owner area are
  fixed, guarded with source-backed rationale, or moved into an explicit not-ready
  follow-up with owner and scope.
- `00_version_release_platform.md` remains searchable reference material, not an
  unstructured dump of release notes.
- Exact version, patch, platform, and compatibility tokens needed for LLM retrieval and
  test generation are preserved.
- Project files are clean after the focused commit.
