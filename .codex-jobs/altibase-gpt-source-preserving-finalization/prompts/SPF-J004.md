# Job SPF-J004: GPT Codex retrieval instructions

## Goal

Add final GPT/Codex/LLM usage instructions that define
`GPTs/upload_package_source_preserving/` as the primary source corpus and enforce
source-grounded answer behavior.

## Scope

- Work only on this job.
- Read `.codex-jobs/altibase-gpt-source-preserving-finalization/prompts/common-source-preserving-finalization.md` first.
- Update package README/instructions and add a report or instruction document if
  useful.

## Required Steps

1. Inspect the package README, manifests, source-pack conventions, and existing
   answer contracts.
2. Add concise instructions for:
   - GPT Knowledge upload order and package role;
   - Codex/code-agent source lookup workflow;
   - `02_source_manifest.md` and `03_source_to_shard_manifest.md` usage;
   - source ID, source path, version, language, and block citation behavior;
   - version-sensitive SQL/iSQL/configuration safety;
   - unsupported-claim refusal or missing-input behavior;
   - relationship between the source-preserving package and compact topic
     package.
3. Keep instructions practical and upload-friendly.
4. Self-review for internal contradictions, obsolete Stage 1 wording, and
   over-claims about live benchmark readiness.
5. Run targeted checks:
   - source-preserving validator from `SPF-J003`;
   - grep checks for contradictory package role wording;
   - `git diff --check -- GPTs/upload_package_source_preserving GPTs/reports`.
6. Review the final diff.
7. Commit with a focused message such as:

```text
source-preserving: add GPT Codex usage instructions
```

## Acceptance Criteria

- The upload package contains clear primary-corpus usage instructions.
- The instructions distinguish primary source corpus from secondary topic routes.
- Version-sensitive and safety-sensitive answer rules are explicit.
- The job creates a focused commit and leaves project files clean.
