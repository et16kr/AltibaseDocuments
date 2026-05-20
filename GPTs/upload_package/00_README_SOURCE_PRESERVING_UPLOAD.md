# Altibase Source-Preserving Upload Package

## Purpose

This directory is the upload package to use when the goal is an Altibase
encyclopedia for Codex, GPTs, or other LLM/RAG systems that must contain the
original selected source content.

The package is source-preserving. It includes `source_pack_shard_001.md`
through `source_pack_shard_016.md` in this directory, plus upload order and
lookup manifests.

For package-only upload and benchmark runs, use only the Markdown files in this
directory. Do not route to answer-ready attachment files, source-pack baselines,
reports, original manuals, or any other repository paths outside this package.

## Upload Set

Upload all 20 Markdown files in this directory as one GPT Knowledge source
corpus. When the upload tool allows ordering, upload this README, the upload
order file, and the two manifest files before the 16 shard files so the lookup
contract is available before retrieval reaches the large source bodies.

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

`01_upload_order.md` records the deterministic shard order and shard-family
span. The order is guidance for upload, validation, and retrieval; all 20 files
are part of one package and count against the same 20-file GPT Knowledge limit.

## Retrieval Contract

- Use `02_source_manifest.md` to identify selected source documents, source IDs,
  versions, language, authority labels, byte counts, line counts, and extraction
  mode.
- Use `03_source_to_shard_manifest.md` to map a `SRC-*` and `BLOCK-*` reference
  to the shard that contains the exact source body.
- Use the shard files for exact source text. Each shard contains
  `SOURCE_BLOCK_BEGIN` / `SOURCE_BLOCK_END` wrappers and the copied source body.
- For concise answer synthesis during package-only runs, use this README,
  `01_upload_order.md`, `02_source_manifest.md`, and
  `03_source_to_shard_manifest.md` only as in-package routing aids, and use the
  shard source blocks for exact behavior.

## GPT, Codex, And LLM Usage Instructions

Treat this directory as the primary source corpus for Altibase GPT Knowledge,
Codex, and RAG-style LLM use. The shard files are the authority for exact
Altibase behavior, syntax, commands, examples, properties, errors, and version
boundaries within the selected corpus.

Use this lookup workflow:

1. Start with `02_source_manifest.md` to find candidate sources by `source_id`,
   `source_path`, title, `source_family`, `version_scope`, `language`,
   `authority_label`, and AID classification.
2. Use `03_source_to_shard_manifest.md` to map the selected `source_id` and
   `BLOCK-*` record to the exact shard file and block.
3. Read the matching source block in `source_pack_shard_*.md`, using the
   `SOURCE_BLOCK_BEGIN` metadata to confirm `source_id`, `source_path`,
   `version_scope`, `language`, `authority_label`, `sha256`, and `block_id`.
4. Answer or generate artifacts from the source block text. During package-only
   runs, do not consult files outside this directory.

When citing or preserving provenance, include the practical metadata available
for the answer: `source_id`, `block_id`, `source_path`, `version_scope`,
`language`, and `authority_label`. Customer-facing answers may use a concise
manual/version citation, but internal Codex or RAG traces should retain the
machine-readable IDs whenever possible.

For repository-local Korean and English source conflicts, apply the active
source policy: Korean Altibase manuals are authoritative; English manuals are
extraction aids unless the source metadata records a stronger label. Preserve
AID labels such as Korean-source-verified, link-validated, English-only
auxiliary, evidence-only, and accepted source-limitation classifications.

## Source-Grounded Answer Safety

- Ask for the exact Altibase version and patch level before giving
  version-sensitive SQL, iSQL commands, configuration, replication, backup,
  recovery, security, TLS, driver, utility, or migration guidance.
- Ask for missing platform, topology, installed tool output, object DDL, log
  excerpt, runtime state, backup state, replication state, certificate paths,
  credentials policy, or rollback constraints when those inputs affect safe
  execution.
- For destructive SQL, recovery, replication state changes, TLS/security
  changes, and property changes, provide guarded first checks and stop
  conditions before copy-ready commands.
- Do not infer Altibase behavior from Oracle, generic SQL, generic JDBC/ODBC,
  Kubernetes, or third-party assumptions when the source block does not support
  the claim.
- If the selected source blocks do not establish a claim, say that the package
  does not support the definitive claim, ask for the missing evidence, and give
  the safest source-backed next check instead of inventing behavior.
- Do not claim a live benchmark readiness pass from this package alone. Current
  finalization evidence is structural validation and dry-run routing evidence
  unless a later package-aware live benchmark report records otherwise.

## Current Coverage

The source pack validation baseline records `941` selected sources, `16` shards,
and `8,767` exclusions. Exclusions are intentional source-selection exclusions,
not missing text from the selected source-pack shards.
