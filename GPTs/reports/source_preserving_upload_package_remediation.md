# Source-Preserving Upload Package Remediation

- Date: 2026-05-19
- Remediation target: `GPTs/upload_package_source_preserving/`
- Reason: the previously assembled topical `GPTs/upload_package/` files are
  answer-ready routing and synthesis documents, not a source-preserving Altibase
  encyclopedia by themselves.

## Decision

For the original goal of an Altibase encyclopedia usable by Codex, GPTs, and
LLM/RAG systems with original selected source content included, the correct upload
candidate is the source-preserving package:

`GPTs/upload_package_source_preserving/`

This package contains 20 files:

- 16 byte-identical source-pack shard files copied from `GPTs/source_pack/`
- 1 README that states the package purpose and retrieval contract
- 1 upload order file
- 2 manifest wrappers for source lookup and source-to-shard lookup

The topical package under `GPTs/upload_package/` remains useful as a compact
answer-ready guide, but it must not be represented as the full source-preserving
encyclopedia.

## Verification

The source-pack validator passed:

```text
validated source pack: 941 selected sources, 16 shards, 8767 exclusions
```

The new upload package contains 20 files and 59,719,357 bytes. All 16 copied shard
files are byte-identical to the corresponding `GPTs/source_pack/source_pack_shard_*.md`
files by SHA-256 comparison.

## Operator Guidance

Upload all files in `GPTs/upload_package_source_preserving/` when the objective is
full selected-source retrieval. Use `GPTs/upload_package/` only as an optional
secondary answer-routing layer, not as the sole knowledge corpus.

