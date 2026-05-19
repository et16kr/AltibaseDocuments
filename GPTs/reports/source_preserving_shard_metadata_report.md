# Source-Preserving Shard Retrieval Metadata Report

- Job: `SPF-J005`
- Date: 2026-05-19
- Package: `GPTs/upload_package_source_preserving/`
- Scope: non-source-body retrieval metadata added to all 16 source shard files

## Summary

All 16 shard files now include a compact `Shard Retrieval Metadata` section above
the first per-source entry and before any `SOURCE_BLOCK_BEGIN` marker. The added
metadata is wrapper text only. It summarizes shard topics, major source families,
version/language spans, representative `SRC-*` / `AID-*` and `BLOCK-*` ranges, and
keyword aliases useful for GPT/Codex semantic retrieval.

No source body text inside `SOURCE_BLOCK_BEGIN` / `SOURCE_BLOCK_END` boundaries was
edited.

## Metadata Inventory

| Shard | Source/block span | Retrieval focus |
| --- | --- | --- |
| `source_pack_shard_001.md` | `SRC-000018` to `AID-SRC-000069`; `BLOCK-000001` to `BLOCK-000125` | administrator operations, installation, operation, backup/recovery, replication, monitoring |
| `source_pack_shard_002.md` | `AID-SRC-000070` to `AID-000025`; `BLOCK-000126` to `BLOCK-000432` | AID troubleshooting, error messages, monitoring, framework integration, migration, coverage ledgers |
| `source_pack_shard_003.md` | `AID-000022` to `AID-SRC-000423`; `BLOCK-000433` to `BLOCK-000451` | AID LLM reference package and coverage evidence |
| `source_pack_shard_004.md` | `AID-SRC-000438` to `SRC-000065`; `BLOCK-000452` to `BLOCK-000470` | AID GPT encyclopedia, AID evidence, Altibase 7.1 client API/CLI/C/ODBC/precompiler |
| `source_pack_shard_005.md` | `SRC-000068` to `SRC-000170`; `BLOCK-000471` to `BLOCK-000487` | CLI, C Interface, ODBC, Precompiler/APRE manuals |
| `source_pack_shard_006.md` | `SRC-000174` to `SRC-000054`; `BLOCK-000488` to `BLOCK-000509` | client interfaces, DB Link, Hadoop/external connectors, 7.1 error reference |
| `source_pack_shard_007.md` | `SRC-000087` to `SRC-000025`; `BLOCK-000510` to `BLOCK-000514` | error message references and General Reference data types/properties |
| `source_pack_shard_008.md` | `SRC-000056` to `SRC-000121`; `BLOCK-000515` to `BLOCK-000523` | General Reference data types, properties, dictionary, and performance views |
| `source_pack_shard_009.md` | `SRC-000151` to `SRC-000080`; `BLOCK-000524` to `BLOCK-000554` | data dictionary, installation/getting started, JDBC, iSQL, iLoader |
| `source_pack_shard_010.md` | `SRC-000094` to `SRC-000039`; `BLOCK-000555` to `BLOCK-000604` | JDBC, Log Analyzer, Migration Center, Oracle migration, SNMP/monitoring |
| `source_pack_shard_011.md` | `SRC-000063` to `SRC-000410`; `BLOCK-000605` to `BLOCK-000792` | Monitoring API, SNMP, Altibase 7.1/7.3 patch notes |
| `source_pack_shard_012.md` | `SRC-000411` to `SRC-000479`; `BLOCK-000793` to `BLOCK-000868` | patch/release notes, performance tuning, replication, Replication Manager, SSL/TLS |
| `source_pack_shard_013.md` | `SRC-000480` to `SRC-000072`; `BLOCK-000869` to `BLOCK-000884` | support inventory evidence, SQL Reference 7.1, Spatial SQL and integrations |
| `source_pack_shard_014.md` | `SRC-000103` to `SRC-000055`; `BLOCK-000885` to `BLOCK-000896` | SQL Reference 7.3/8.1, stored/external procedures, source-pack support evidence |
| `source_pack_shard_015.md` | `SRC-000075` to `SRC-000106`; `BLOCK-000897` to `BLOCK-000928` | stored procedures, utilities, technical support, third-party guides |
| `source_pack_shard_016.md` | `SRC-000137` to `SRC-000213`; `BLOCK-000929` to `BLOCK-000941` | utilities, dataCompJ, Altibase Heartbeat, command/tool references |

## Self-Review

- Metadata was inserted before the first source block in each shard.
- Metadata avoids live benchmark readiness claims.
- Keyword aliases are retrieval hints tied to represented source families and
  manuals; they do not replace exact source-block evidence.
- Source body preservation passed the `SPF-J002` validator and an independent
  source-block hash check.

## Verification Results

| Check | Result |
| --- | --- |
| `python3 GPTs/reports/scripts/validate_source_preserving_upload_package.py --strict-final` | Pass: 20 files, 941 selected sources, 941 source-to-shard rows, and 941 parsed source blocks validated. |
| Independent inline Python source-block body preservation check | Pass: 941 source-block bodies hashed against recorded `source_sha256` and `extracted_body_sha256` values. |
| `git diff --check -- GPTs/upload_package_source_preserving GPTs/reports/source_preserving_shard_metadata_report.md` | Pass. |

No live benchmark was run or claimed for this metadata-only job.
