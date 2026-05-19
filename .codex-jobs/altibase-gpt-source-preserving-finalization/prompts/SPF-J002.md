# Job SPF-J002: Final-upload wording normalization

## Goal

Normalize final-upload wrapper/header wording in
`GPTs/upload_package_source_preserving/` while preserving every source body inside
`SOURCE_BLOCK_BEGIN` / `SOURCE_BLOCK_END`.

## Scope

- Work only on this job.
- Read `.codex-jobs/altibase-gpt-source-preserving-finalization/prompts/common-source-preserving-finalization.md` first.
- Edit only wrapper/header/guidance text outside source blocks.
- Do not change source body bytes inside source block boundaries.

## Required Steps

1. Inspect the preflight report from `SPF-J001`.
2. Locate final-disqualifying wrapper phrases such as `Upload intended: no`,
   `not a final GPT Knowledge upload manifest`, or equivalent Stage 1 language.
3. Replace those phrases with final-upload wording that says the package is the
   primary source-preserving upload candidate.
4. Preserve source bodies exactly. Use a mechanical guard or script if helpful,
   but keep the source-body before/after comparison in the report.
5. Update or create
   `GPTs/reports/source_preserving_upload_package_wording_normalization.md`.
6. Self-review all changed package files for accidental source-body edits.
7. Run targeted checks:
   - grep scan for disallowed wrapper phrases;
   - source-block body preservation check or documented equivalent;
   - `git diff --check -- GPTs/upload_package_source_preserving GPTs/reports/source_preserving_upload_package_wording_normalization.md`.
8. Review the final diff.
9. Commit with a focused message such as:

```text
source-preserving: normalize final upload wording
```

## Acceptance Criteria

- Final-upload wrapper wording no longer contradicts upload use.
- Source block bodies are documented as preserved.
- The package still has 20 files and 16 shard files.
- The job creates a focused commit and leaves project files clean.
