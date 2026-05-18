# Source Pack Upload Order Guidance

- Job: `S1-J005`
- Last verified: 2026-05-18
- Status: guidance only; not a final GPT Knowledge upload manifest

## Boundary

`GPTs/source_pack/` is a source-preserving evidence layer. The shard files below
are not final upload files, and they must not be uploaded beside the current
attachments as an additional package. Anything later copied or transformed into
`GPTs/upload_package/` must count against the same global 20 Markdown file
limit, including AID-derived content.

## Current Source-Pack Order

Use this order when a reviewer or downstream packaging job needs to inspect the
source-pack shards. It follows the deterministic shard IDs written in
`source_to_shard_manifest.tsv`.

| Order | Shard | Sources | Size | Estimated tokens | Upload state | Source-family span |
| ---: | --- | ---: | ---: | ---: | --- | --- |
| 1 | `GPTs/source_pack/source_pack_shard_001.md` | 125 | 4.30 MiB | 929,328 | `no` | administrator_operations to aid_06_monitoring_diagnostics |
| 2 | `GPTs/source_pack/source_pack_shard_002.md` | 307 | 2.91 MiB | 762,011 | `no` | aid_06_monitoring_diagnostics to aid_coverage_ledger |
| 3 | `GPTs/source_pack/source_pack_shard_003.md` | 19 | 2.56 MiB | 671,448 | `no` | aid_coverage_ledger to aid_llm_reference |
| 4 | `GPTs/source_pack/source_pack_shard_004.md` | 19 | 3.54 MiB | 865,693 | `no` | aid_llm_reference to c_cli_odbc_precompiler |
| 5 | `GPTs/source_pack/source_pack_shard_005.md` | 17 | 3.89 MiB | 899,447 | `no` | c_cli_odbc_precompiler |
| 6 | `GPTs/source_pack/source_pack_shard_006.md` | 22 | 3.55 MiB | 815,431 | `no` | c_cli_odbc_precompiler to error_message_reference |
| 7 | `GPTs/source_pack/source_pack_shard_007.md` | 5 | 3.27 MiB | 854,729 | `no` | error_message_reference to general_reference_1_datatypes_properties |
| 8 | `GPTs/source_pack/source_pack_shard_008.md` | 9 | 4.14 MiB | 882,724 | `no` | general_reference_1_datatypes_properties to general_reference_2_dictionary_views |
| 9 | `GPTs/source_pack/source_pack_shard_009.md` | 31 | 4.04 MiB | 899,094 | `no` | general_reference_2_dictionary_views to jdbc_java |
| 10 | `GPTs/source_pack/source_pack_shard_010.md` | 50 | 3.90 MiB | 902,825 | `no` | jdbc_java to monitoring_api_snmp |
| 11 | `GPTs/source_pack/source_pack_shard_011.md` | 188 | 4.07 MiB | 945,108 | `no` | monitoring_api_snmp to patch_notes |
| 12 | `GPTs/source_pack/source_pack_shard_012.md` | 76 | 4.21 MiB | 912,959 | `no` | patch_notes to source_inventory_support |
| 13 | `GPTs/source_pack/source_pack_shard_013.md` | 16 | 3.35 MiB | 763,236 | `no` | source_inventory_support to sql_reference |
| 14 | `GPTs/source_pack/source_pack_shard_014.md` | 12 | 3.67 MiB | 834,345 | `no` | sql_reference to stored_external_procedures |
| 15 | `GPTs/source_pack/source_pack_shard_015.md` | 32 | 3.75 MiB | 860,990 | `no` | stored_external_procedures to utilities_datacompj |
| 16 | `GPTs/source_pack/source_pack_shard_016.md` | 13 | 1.06 MiB | 224,573 | `no` | utilities_datacompj |

## Upload Guidance

- Stage 1 source-pack shards are direct-upload not-ready because they are
  evidence artifacts marked `upload_intended=no`.
- A later upload-package job may transform or copy selected evidence into
  `GPTs/upload_package/`; that job must rerun size, token, and 20-file count
  validation on the final package.
- If a shard is ever changed to `upload_intended=yes` or `candidate`, it must
  stay below the validation margin of 90% of 512 MiB and 90% of 2,000,000
  estimated tokens, or its shard manifest notes must mark it `not-ready`.
