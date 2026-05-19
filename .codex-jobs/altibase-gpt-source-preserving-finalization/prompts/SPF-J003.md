# Job SPF-J003: Source-preserving package validator

## Goal

Create and document a validator dedicated to
`GPTs/upload_package_source_preserving/`.

## Scope

- Work only on this job.
- Read `.codex-jobs/altibase-gpt-source-preserving-finalization/prompts/common-source-preserving-finalization.md` first.
- Prefer adding `GPTs/reports/scripts/validate_source_preserving_upload_package.py`.
- Write validation results to
  `GPTs/reports/source_preserving_upload_package_validation.md`.

## Required Steps

1. Inspect the existing Stage 4 validator and source-pack manifests.
2. Implement a validator for the source-preserving package that checks:
   - exactly 20 files;
   - required README, upload-order, manifest wrappers, and 16 shard files;
   - file-size and estimated-token safety limits;
   - selected source representation;
   - matching `SOURCE_BLOCK_BEGIN` / `SOURCE_BLOCK_END` pairs;
   - source body SHA-256 matches recorded `source_sha256` metadata;
   - final wrapper text does not contain reverse-routing phrases outside source
     blocks;
   - manifest wrapper readability and parseability.
3. Add a command-line interface with clear PASS/FAIL output.
4. Document the validator command and current result.
5. Self-review for false positives caused by source body text, path handling, and
   line-ending assumptions.
6. Run targeted checks:
   - `python3 GPTs/reports/scripts/validate_source_preserving_upload_package.py`;
   - existing relevant package/source-pack validators if applicable;
   - `git diff --check -- GPTs/reports/scripts/validate_source_preserving_upload_package.py GPTs/reports/source_preserving_upload_package_validation.md`.
7. Review the final diff.
8. Commit with a focused message such as:

```text
source-preserving: add final package validator
```

## Acceptance Criteria

- The new validator passes on the current source-preserving package.
- The validator enforces source-body integrity, not obsolete whole-file equality
  after wrapper normalization.
- The validation report records command, result, and any known limitations.
- The job creates a focused commit and leaves project files clean.
