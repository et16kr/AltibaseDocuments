# Altibase Source-Preserving Upload Package

## Purpose

This directory is the upload package to use when the goal is an Altibase
encyclopedia for Codex, GPTs, or other LLM/RAG systems that must contain the
original selected source content.

The package is source-preserving. It includes the exact source-pack shard bodies
from `GPTs/source_pack/source_pack_shard_001.md` through
`GPTs/source_pack/source_pack_shard_016.md`, plus upload order and lookup
manifests.

Do not confuse this package with `GPTs/upload_package/`. The topical files in
`GPTs/upload_package/` are answer-ready routing and synthesis documents. They are
useful as a compact guide, but they are not the full source-preserving
encyclopedia by themselves.

## Upload Set

Upload all files in this directory:

1. `00_README_SOURCE_PRESERVING_UPLOAD.md`
2. `01_upload_order.md`
3. `02_source_manifest.md`
4. `03_source_to_shard_manifest.md`
5. `source_pack_shard_001.md`
6. `source_pack_shard_002.md`
7. `source_pack_shard_003.md`
8. `source_pack_shard_004.md`
9. `source_pack_shard_005.md`
10. `source_pack_shard_006.md`
11. `source_pack_shard_007.md`
12. `source_pack_shard_008.md`
13. `source_pack_shard_009.md`
14. `source_pack_shard_010.md`
15. `source_pack_shard_011.md`
16. `source_pack_shard_012.md`
17. `source_pack_shard_013.md`
18. `source_pack_shard_014.md`
19. `source_pack_shard_015.md`
20. `source_pack_shard_016.md`

## Retrieval Contract

- Use `02_source_manifest.md` to identify selected source documents, source IDs,
  versions, language, authority labels, byte counts, line counts, and extraction
  mode.
- Use `03_source_to_shard_manifest.md` to map a `SRC-*` and `BLOCK-*` reference
  to the shard that contains the exact source body.
- Use the shard files for exact source text. Each shard contains
  `SOURCE_BLOCK_BEGIN` / `SOURCE_BLOCK_END` wrappers and the copied source body.
- For concise answer synthesis, `GPTs/upload_package/` can still be used as a
  secondary routing layer, but it must not replace the source-preserving upload
  set when exact original content is required.

## Current Coverage

The source pack validation baseline records `941` selected sources, `16` shards,
and `8,767` exclusions. Exclusions are intentional source-selection exclusions,
not missing text from the selected source-pack shards.

