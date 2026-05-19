# Source Pack Validation

- Job: `S1-J005`
- Last verified: 2026-05-18
- Status: `pass`
- Validation command: `python3 GPTs/source_pack/scripts/validate_source_pack.py --check`

## Reconfirmed Requirement And Boundary

`S1-J005` validates the Stage 1 source-pack evidence layer only. It checks
`GPTs/source_pack/source_manifest.tsv`, `source_exclusion_register.tsv`,
`source_to_shard_manifest.tsv`, and the committed `source_pack_shard_*.md`
files. It does not generate the Korean-aligned English baseline, edit
`GPTs/attachments/`, or assemble `GPTs/upload_package/`.

## Design Note

The validator treats the committed source pack as the evidence artifact under
test. It first runs the deterministic manifest and shard builders in `--check`
mode, then independently parses every committed source block and hashes the
body between `SOURCE_BLOCK_BEGIN` and `SOURCE_BLOCK_END`. This keeps exact
source preservation separate from later baseline, playbook, attachment, and
upload-package generation.

## Verdict

Verdict: Pass

No source-pack validation blockers were found. Do not proceed to the
Korean-aligned English baseline from an unvalidated or locally modified
source pack; rerun the command above after any source, manifest, or shard
change.

## Validation Checks

| Check | Result | Evidence |
| --- | --- | --- |
| Source manifest currentness | Pass | `python3 GPTs/source_pack/scripts/build_source_manifest.py --check` -> exit 0 |
| Shard generator currentness | Pass | `python3 GPTs/source_pack/scripts/build_source_pack.py --check` -> exit 0 |
| Selected source coverage | Pass | 941 selected sources mapped |
| Exclusion reasons | Pass | 8,767 excluded candidates checked |
| Exact extraction checksums | Pass | 941 source blocks parsed and hashed |
| Upload margin gate | Pass | 0 upload-intended shard candidates |

## Corpus Summary

| Metric | Value |
| --- | ---: |
| Source manifest rows | 941 |
| Selected rows | 941 |
| Exact source rows | 914 |
| Support-evidence rows | 27 |
| Exclusion rows | 8,767 |
| Source-to-shard rows | 941 |
| Source-pack shards | 16 |
| Selected source bytes | 57,981,744 |
| Selected source estimated tokens | 12,785,127 |
| Shard bytes including wrappers | 58,958,626 |
| Largest shard by tokens | `GPTs/source_pack/source_pack_shard_011.md` (945,108) |
| Largest shard by bytes | `GPTs/source_pack/source_pack_shard_001.md` (4.30 MiB) |

## Upload-Intended Shard Gate

Current Stage 1 planning constants for GPT Knowledge upload validation are:

| Limit | Value | Margin used here |
| --- | ---: | ---: |
| Markdown file count | 20 | 20 |
| File size | 512.00 MiB | 460.80 MiB |
| Estimated tokens per file | 2,000,000 | 1,800,000 |

No source-pack shard is currently upload-intended. Every committed shard is
marked `upload_intended=no`, so direct GPT Knowledge upload of the source
pack is not-ready by policy until a later upload-package job intentionally
copies or transforms selected content into `GPTs/upload_package/` and counts
it against the global 20 Markdown file limit.

## Required Verification Commands

```bash
python3 GPTs/source_pack/scripts/validate_source_pack.py --check
git diff --check -- GPTs/source_pack
```
