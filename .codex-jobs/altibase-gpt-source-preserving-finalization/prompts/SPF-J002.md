# Job SPF-J002: Source-preserving package validator

## Goal

Create and document a validator dedicated to
`GPTs/upload_package_source_preserving/` before any shard-wrapper wording edits.

## Scope

- Work only on this job.
- Read `.codex-jobs/altibase-gpt-source-preserving-finalization/prompts/common-source-preserving-finalization.md` first.
- Prefer adding `GPTs/reports/scripts/validate_source_preserving_upload_package.py`.
- Write validation results to
  `GPTs/reports/source_preserving_upload_package_validation.md`.
- Do not normalize package wording in this job.

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
     blocks when strict-final mode is requested;
   - manifest wrapper readability and parseability.
3. Add a command-line interface with clear PASS/FAIL output. It may support a
   pre-final mode for the current package and a strict-final mode for later jobs.
4. Document the current result:
   - source-body/package-structure checks must pass;
   - strict-final wording blockers may be recorded as expected until `SPF-J003`.
5. Self-review for false positives caused by source body text, path handling, and
   line-ending assumptions.
6. Run targeted checks:
   - `python3 GPTs/reports/scripts/validate_source_preserving_upload_package.py`
     or the documented pre-final equivalent;
   - strict-final mode if implemented, recording expected wording blockers;
   - existing relevant package/source-pack validators if applicable;
   - `git diff --check -- GPTs/reports/scripts/validate_source_preserving_upload_package.py GPTs/reports/source_preserving_upload_package_validation.md`.
7. Review the final diff.
8. Commit with a focused message such as:

```text
source-preserving: add final package validator
```

## Acceptance Criteria

- The new validator passes source-body and package-structure checks on the
  current source-preserving package.
- The validator can enforce final wrapper wording for later jobs.
- The validator enforces source-body integrity, not obsolete whole-file equality
  after wrapper normalization.
- The validation report records command, result, strict-final wording status, and
  any known limitations.
- The job creates a focused commit and leaves project files clean.
