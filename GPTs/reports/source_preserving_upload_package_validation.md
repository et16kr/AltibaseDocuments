# Source-Preserving Upload Package Validation

- Job: `SPF-J002`
- Date: 2026-05-19
- Package: `GPTs/upload_package/`
- Validator: `GPTs/reports/scripts/validate_source_preserving_upload_package.py`

## Verdict

Verdict: Pass

The current pre-final source-preserving package passes package-structure,
manifest-wrapper, selected-source representation, source-block pairing,
file limit, and source-body SHA-256 integrity checks.

Strict-final wrapper wording is enforceable by the validator, but the
current package is expected to fail that mode until `SPF-J003` removes
reverse-routing wording outside source blocks.

## Commands

| Command | Result | Notes |
| --- | --- | --- |
| `python3 GPTs/reports/scripts/validate_source_preserving_upload_package.py` | Pass | Pre-final mode; source-body and package-structure checks must pass. |
| `python3 GPTs/reports/scripts/validate_source_preserving_upload_package.py --strict-final` | Expected Fail | Strict wording blockers are expected until `SPF-J003`. |

## Check Matrix

| Check | Result | Evidence |
| --- | --- | --- |
| Exact file count | Pass | 20 package files found. |
| Required wrappers and shards | Pass | README, upload-order, two manifest wrappers, and 16 shard files are required. |
| File-size safety | Pass | 90% of 512 MiB safety limit checked for every file. |
| Estimated-token safety | Pass | 90% of 2,000,000 estimated-token safety limit checked for every file. |
| Manifest wrapper parseability | Pass | `02_source_manifest.md` and `03_source_to_shard_manifest.md` parse as TSV and match `GPTs/source_pack/` TSV rows. |
| Selected source representation | Pass | 941 selected sources represented by 941 source-to-shard rows. |
| Source-block pairs | Pass | 941 parsed `SOURCE_BLOCK_BEGIN` / `SOURCE_BLOCK_END` pairs. |
| Source-body SHA-256 integrity | Pass | Parsed source-block bodies are hashed and compared to recorded `source_sha256` metadata; whole-shard equality is not required. |
| Strict-final wrapper wording | Expected blocker | 18 reverse-routing phrase matches outside source blocks. |

## Package Metrics

| Metric | Value |
| --- | ---: |
| Package files | 20 |
| Package bytes | 59,719,357 |
| Selected source rows | 941 |
| Source-to-shard rows | 941 |
| Parsed source blocks | 941 |
| Shard files | 16 |
| Largest file by size | `GPTs/upload_package/source_pack_shard_001.md` (4.30 MiB) |
| Largest file by estimated tokens | `GPTs/upload_package/source_pack_shard_011.md` (945,108) |

## Strict-Final Wording Status

The following matches are outside source blocks and are expected until
`SPF-J003` normalizes wrapper/header wording:

- GPTs/upload_package/01_upload_order.md:5: not-final upload manifest wording: 'not a final GPT Knowledge upload manifest'
- GPTs/upload_package/01_upload_order.md:10: not-final upload wording: 'not final upload'
- GPTs/upload_package/source_pack_shard_001.md:4: upload-intended=no shard header: 'Upload intended: `no`'
- GPTs/upload_package/source_pack_shard_002.md:4: upload-intended=no shard header: 'Upload intended: `no`'
- GPTs/upload_package/source_pack_shard_003.md:4: upload-intended=no shard header: 'Upload intended: `no`'
- GPTs/upload_package/source_pack_shard_004.md:4: upload-intended=no shard header: 'Upload intended: `no`'
- GPTs/upload_package/source_pack_shard_005.md:4: upload-intended=no shard header: 'Upload intended: `no`'
- GPTs/upload_package/source_pack_shard_006.md:4: upload-intended=no shard header: 'Upload intended: `no`'
- GPTs/upload_package/source_pack_shard_007.md:4: upload-intended=no shard header: 'Upload intended: `no`'
- GPTs/upload_package/source_pack_shard_008.md:4: upload-intended=no shard header: 'Upload intended: `no`'
- GPTs/upload_package/source_pack_shard_009.md:4: upload-intended=no shard header: 'Upload intended: `no`'
- GPTs/upload_package/source_pack_shard_010.md:4: upload-intended=no shard header: 'Upload intended: `no`'
- GPTs/upload_package/source_pack_shard_011.md:4: upload-intended=no shard header: 'Upload intended: `no`'
- GPTs/upload_package/source_pack_shard_012.md:4: upload-intended=no shard header: 'Upload intended: `no`'
- GPTs/upload_package/source_pack_shard_013.md:4: upload-intended=no shard header: 'Upload intended: `no`'
- GPTs/upload_package/source_pack_shard_014.md:4: upload-intended=no shard header: 'Upload intended: `no`'
- GPTs/upload_package/source_pack_shard_015.md:4: upload-intended=no shard header: 'Upload intended: `no`'
- GPTs/upload_package/source_pack_shard_016.md:4: upload-intended=no shard header: 'Upload intended: `no`'

## Supporting Check Log

| Command | Result | Notes |
| --- | --- | --- |
| `python3 -m py_compile GPTs/reports/scripts/validate_source_preserving_upload_package.py` | Pass | Validator syntax check passed. |
| `python3 GPTs/reports/scripts/validate_upload_package.py --assembled` | Pass | Existing compact Stage 4 package validator still passes. |
| `python3 GPTs/source_pack/scripts/validate_source_pack.py --check` | Not passed in this workspace | The command requires the adjacent `/home/et16/AID` corpus; that directory is absent here, so the source-pack builder reported missing AID evidence paths. This does not change the new package validator result because it checks the already packaged source-block bodies against recorded metadata. |

## Known Limitations

- Token counts use the same conservative estimator as the source-pack
  validator: UTF-8 decoded character count divided by four and rounded up.
- Strict-final wording scans remove parsed source-block spans first, so
  phrases inside preserved source bodies do not trigger wrapper blockers.
- Shard source-body integrity is checked from recorded source metadata and
  parsed block bodies. Whole shard-file SHA-256 equality with
  `GPTs/source_pack/` is intentionally not required after wrapper
  normalization.
- `source_to_shard_manifest.tsv` paths are mapped from
  `GPTs/source_pack/source_pack_shard_*.md` to the same shard filenames in
  `GPTs/upload_package/`.
