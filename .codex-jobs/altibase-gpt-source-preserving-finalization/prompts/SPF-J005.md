# Job SPF-J005: Shard retrieval metadata

## Goal

Add non-source-body shard retrieval metadata that improves GPT/Codex semantic
search while preserving all source block bytes.

## Scope

- Work only on this job.
- Read `.codex-jobs/altibase-gpt-source-preserving-finalization/prompts/common-source-preserving-finalization.md` first.
- Edit shard metadata outside source blocks only.
- Do not change source body bytes inside source block boundaries.

## Required Steps

1. Inspect `03_source_to_shard_manifest.md`, `02_source_manifest.md`, and all 16
   shard headers.
2. Design a compact metadata block for each shard, such as:
   - shard topic summary;
   - major source families/manuals;
   - version/language spans;
   - representative `SRC-*` / `BLOCK-*` ranges;
   - keyword aliases useful for retrieval.
3. Add metadata above the first source block in each shard.
4. Update or create
   `GPTs/reports/source_preserving_shard_metadata_report.md`.
5. Self-review for source-body changes, excessive metadata, and misleading
   keywords.
6. Run targeted checks:
   - source-preserving validator from `SPF-J002`;
   - source-block body preservation check;
   - `git diff --check -- GPTs/upload_package_source_preserving GPTs/reports/source_preserving_shard_metadata_report.md`.
7. Review the final diff.
8. Commit with a focused message such as:

```text
source-preserving: add shard retrieval metadata
```

## Acceptance Criteria

- All 16 source shard files have useful retrieval metadata outside source blocks.
- Source body integrity validation passes.
- Metadata does not claim live benchmark readiness.
- The job creates a focused commit and leaves project files clean.
