# Source-Preserving GPT Codex Usage Instructions

- Job: `SPF-J004`
- Date: 2026-05-19
- Package: `GPTs/upload_package/`
- Verdict: Pass

## Scope

This job adds final upload-friendly GPT, Codex, and LLM/RAG usage instructions
for the source-preserving package. It does not change benchmark questions,
expected answers, shard source bodies, or source-pack TSV rows.

## Changes

- `00_README_SOURCE_PRESERVING_UPLOAD.md` now states that all 20 Markdown files
  form one primary GPT Knowledge source corpus and gives the upload-order role.
- The README now defines the Codex/LLM lookup workflow from
  `02_source_manifest.md` to `03_source_to_shard_manifest.md` to the matching
  `SOURCE_BLOCK_BEGIN` / `SOURCE_BLOCK_END` body in the shard files.
- The README now records provenance expectations for `source_id`, `block_id`,
  `source_path`, `version_scope`, `language`, and `authority_label`.
- The README now makes version-sensitive, destructive, replication,
  backup/recovery, TLS/security, configuration, driver, utility, and unsupported
  claim guardrails explicit.
- `02_source_manifest.md` now explains how to use source metadata for source
  selection and version-sensitive answer routing.
- `03_source_to_shard_manifest.md` now explains how to map source IDs and block
  IDs to the package shards, and clarifies that the preserved `upload_intended`
  TSV column is baseline metadata that does not override this package's final
  primary-corpus role.

## Verification

| Check | Result |
| --- | --- |
| `python3 GPTs/reports/scripts/validate_source_preserving_upload_package.py --strict-final` | Pass: 20 package files, 941 selected sources, 941 source-to-shard rows, and 941 parsed source blocks. |
| Disallowed package-role wording scan outside shard files | Pass: no matches for `Upload intended: no`, `not a final GPT Knowledge upload manifest`, `not final upload`, or equivalent non-final wording. |
| Positive package-role wording scan | Pass: README and manifest wrapper wording confirms primary source corpus, secondary topic routing, and no live benchmark readiness claim. |
| `git diff --check -- GPTs/upload_package GPTs/reports` | Pass. |

## Self-Review

- No source body inside a `SOURCE_BLOCK_BEGIN` / `SOURCE_BLOCK_END` boundary was
  edited.
- The new instructions distinguish the primary source-preserving corpus from
  the secondary compact topic package.
- The instructions avoid obsolete Stage 1 reverse-routing language while
  preserving source-pack baseline metadata in the TSV fences.
- The package does not claim live answer-quality or package-context benchmark
  readiness; it points to structural validation and future package-aware live
  benchmark evidence instead.
