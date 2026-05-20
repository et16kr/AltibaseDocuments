# Source-Preserving Upload Order

- Job: `SPF-J003`
- Last verified: 2026-05-19
- Status: primary source-preserving GPT Knowledge upload candidate

## Boundary

`GPTs/upload_package/` is the primary source-preserving upload
candidate for Altibase GPT Knowledge, Codex, and LLM/RAG usage. Upload all 20
Markdown files in this directory together when the objective is selected-source
retrieval with preserved source bodies.

For package-only upload and benchmark runs, treat the files below as the complete
allowed context. Do not route to source-pack baselines, answer-ready attachment
files, reports, original manuals, or any other repository paths outside this
package.

## Current Package Order

Use this order when uploading or validating the source-preserving package. It
follows the deterministic shard IDs written in
`source_to_shard_manifest.tsv`.

| Order | Shard | Sources | Size | Estimated tokens | Upload role | Source-family span |
| ---: | --- | ---: | ---: | ---: | --- | --- |
| 1 | `GPTs/upload_package/source_pack_shard_001.md` | 125 | 4.30 MiB | 929,328 | primary source shard | administrator_operations to aid_06_monitoring_diagnostics |
| 2 | `GPTs/upload_package/source_pack_shard_002.md` | 307 | 2.91 MiB | 762,011 | primary source shard | aid_06_monitoring_diagnostics to aid_coverage_ledger |
| 3 | `GPTs/upload_package/source_pack_shard_003.md` | 19 | 2.56 MiB | 671,448 | primary source shard | aid_coverage_ledger to aid_llm_reference |
| 4 | `GPTs/upload_package/source_pack_shard_004.md` | 19 | 3.54 MiB | 865,693 | primary source shard | aid_llm_reference to c_cli_odbc_precompiler |
| 5 | `GPTs/upload_package/source_pack_shard_005.md` | 17 | 3.89 MiB | 899,447 | primary source shard | c_cli_odbc_precompiler |
| 6 | `GPTs/upload_package/source_pack_shard_006.md` | 22 | 3.55 MiB | 815,431 | primary source shard | c_cli_odbc_precompiler to error_message_reference |
| 7 | `GPTs/upload_package/source_pack_shard_007.md` | 5 | 3.27 MiB | 854,729 | primary source shard | error_message_reference to general_reference_1_datatypes_properties |
| 8 | `GPTs/upload_package/source_pack_shard_008.md` | 9 | 4.14 MiB | 882,724 | primary source shard | general_reference_1_datatypes_properties to general_reference_2_dictionary_views |
| 9 | `GPTs/upload_package/source_pack_shard_009.md` | 31 | 4.04 MiB | 899,094 | primary source shard | general_reference_2_dictionary_views to jdbc_java |
| 10 | `GPTs/upload_package/source_pack_shard_010.md` | 50 | 3.90 MiB | 902,825 | primary source shard | jdbc_java to monitoring_api_snmp |
| 11 | `GPTs/upload_package/source_pack_shard_011.md` | 188 | 4.07 MiB | 945,108 | primary source shard | monitoring_api_snmp to patch_notes |
| 12 | `GPTs/upload_package/source_pack_shard_012.md` | 76 | 4.21 MiB | 912,959 | primary source shard | patch_notes to source_inventory_support |
| 13 | `GPTs/upload_package/source_pack_shard_013.md` | 16 | 3.35 MiB | 763,236 | primary source shard | source_inventory_support to sql_reference |
| 14 | `GPTs/upload_package/source_pack_shard_014.md` | 12 | 3.69 MiB | 838,744 | primary source shard | sql_reference to stored_external_procedures |
| 15 | `GPTs/upload_package/source_pack_shard_015.md` | 32 | 3.75 MiB | 860,990 | primary source shard | stored_external_procedures to utilities_datacompj |
| 16 | `GPTs/upload_package/source_pack_shard_016.md` | 13 | 1.06 MiB | 224,573 | primary source shard | utilities_datacompj |

## Upload Guidance

- Upload the README, this order file, both manifest wrappers, and all 16 shard
  files as one package.
- Treat the shard files as the source authority for exact Altibase behavior.
- Preserve bytes inside every `SOURCE_BLOCK_BEGIN` / `SOURCE_BLOCK_END` body.
- Re-run the source-preserving package validator after any wrapper/header,
  manifest, or shard change.
