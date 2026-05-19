# Job SPF-J003: Final-upload wording normalization

## Goal

Normalize final-upload wrapper/header wording in
`GPTs/upload_package_source_preserving/` while preserving every source body inside
`SOURCE_BLOCK_BEGIN` / `SOURCE_BLOCK_END`.

## Scope

- Work only on this job.
- Read `.codex-jobs/altibase-gpt-source-preserving-finalization/prompts/common-source-preserving-finalization.md` first.
- Use the validator created by `SPF-J002` before and after package edits.
- Edit only wrapper/header/guidance text outside source blocks.
- Do not change source body bytes inside source block boundaries.

## Required Steps

1. Inspect the preflight report from `SPF-J001` and validator/report from
   `SPF-J002`.
2. Run the `SPF-J002` validator before editing and record the baseline result.
3. Locate final-disqualifying wrapper phrases such as `Upload intended: no`,
   `not a final GPT Knowledge upload manifest`, or equivalent Stage 1 language.
4. Replace those phrases with final-upload wording that says the package is the
   primary source-preserving upload candidate.
5. Preserve source bodies exactly. Use the source-preserving validator for the
   before/after source-body comparison.
6. Update or create
   `GPTs/reports/source_preserving_upload_package_wording_normalization.md`.
7. Self-review all changed package files for accidental source-body edits.
8. Run targeted checks:
   - source-preserving validator strict-final mode;
   - grep scan for disallowed wrapper phrases outside source blocks;
   - source-block body preservation check;
   - `git diff --check -- GPTs/upload_package_source_preserving GPTs/reports/source_preserving_upload_package_wording_normalization.md`.
9. Review the final diff.
10. Commit with a focused message such as:

```text
source-preserving: normalize final upload wording
```

## Acceptance Criteria

- Final-upload wrapper wording no longer contradicts upload use.
- Source block bodies are validated as preserved by the `SPF-J002` validator.
- The package still has 20 files and 16 shard files.
- The job creates a focused commit and leaves project files clean.
