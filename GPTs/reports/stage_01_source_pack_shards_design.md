# Stage 1 Source Pack Shards Design Note

Job: `S1-J004`
Status: source-pack generation design
Created: 2026-05-18
Scope: deterministic source-pack scripts, shard files, and source-to-shard mapping

## Reconfirmed Requirement And Boundary

`S1-J004` implements deterministic source-pack generation for selected Stage 1
sources. This job may update source-pack scripts, source manifests required for exact
file-level AID extraction, source-pack shards, and the source-to-shard manifest. It
does not edit customer-facing attachments, generate the Korean-aligned English
baseline, or assemble `GPTs/upload_package/`.

## Design

`GPTs/source_pack/scripts/build_source_manifest.py` remains the deterministic source
selection builder. For this job it also materializes file-level AID upload-content
candidate rows that were deferred by `S1-J003`, using `~/AID/llm-reference/coverage/source-inventory.tsv`
and the selected top-level `~/AID/llm-reference/` and GPT upload-candidate Markdown
files. AID exact-source rows use stable `AID-SRC-*` source IDs so they do not collide
with AID tier-group IDs such as `AID-000001`.

`GPTs/source_pack/scripts/build_source_pack.py` reads `GPTs/source_pack/source_manifest.tsv`
and writes source-pack shard files plus `source_to_shard_manifest.tsv`. Each selected
`include_exact` or `include_support_evidence` row is written to exactly one shard.
The original file bytes are copied between stable `SOURCE_BLOCK_BEGIN` and
`SOURCE_BLOCK_END` markers. The begin marker records the source ID, path, family,
version scope, language, authority label, source checksum, byte count, line count,
and token estimate.

Shard assignment is deterministic: rows are ordered by source family, version scope,
origin, path, and source ID, then packed into numbered shards with a fixed token
target. Shards are Stage 1 evidence artifacts and are marked `upload_intended=no`
until a later upload-package job intentionally transforms or copies selected content
into `GPTs/upload_package/`.

## Validation Contract

The builder must verify that:

- every selected manifest row appears in exactly one source-to-shard row;
- source body SHA-256, byte count, line count, and token estimate match the selected
  source file;
- every generated shard contains source block boundary markers;
- `--check` mode fails when generated shards or `source_to_shard_manifest.tsv` are
  stale.
