# R02 High-Risk Source Traceability Audit

Date: 2026-05-14
Reviewer: Codex
Verdict: Pass

## Scope

- Attachments:
  - `GPTs/attachments/00_version_release_platform.md`
  - `GPTs/attachments/03_sql_ddl_generation.md`
  - `GPTs/attachments/05_data_types_properties.md`
  - `GPTs/attachments/06_data_dictionary_performance_views.md`
  - `GPTs/attachments/09_replication_ha_cdc.md`
  - `GPTs/attachments/18_security_ssl_tls.md`
- Supporting reports:
  - `GPTs/reports/source_inventory.md`
  - `GPTs/reports/8_1_verification.md`
  - `GPTs/reports/eng_kor_parity.md`
- Source manuals sampled:
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`
  - `Technical Documents/eng/Supported Platforms.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_trunk/kor/SQL Reference.md`
  - `Manuals/Altibase_trunk/kor/Replication Manual.md`
  - `Manuals/Altibase_trunk/eng/Altibase SSL TLS User's Guide.md`

## Commands Run

```bash
wc -l GPTs/attachments/00_version_release_platform.md GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/05_data_types_properties.md GPTs/attachments/06_data_dictionary_performance_views.md GPTs/attachments/09_replication_ha_cdc.md GPTs/attachments/18_security_ssl_tls.md GPTs/reports/source_inventory.md GPTs/reports/8_1_verification.md GPTs/reports/eng_kor_parity.md
rg -n "JSON|LOB|Temporary LOB|SSL|TLS|replication SSL|REPLICATION|REPL|S\$|V\$|property|properties|platform|8\.1|7\.3|7\.1|Altibase 8\.1 verified source|trunk|Manuals/|/home|file://" GPTs/attachments/00_version_release_platform.md GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/05_data_types_properties.md GPTs/attachments/06_data_dictionary_performance_views.md GPTs/attachments/09_replication_ha_cdc.md GPTs/attachments/18_security_ssl_tls.md
rg -n "JSON|LOB|Temporary LOB|SSL|TLS|replication|REPLICATION|XLog|platform|8\.1|supported|property|view|performance view|V\$|S\$|Altibase 8\.1" GPTs/reports/source_inventory.md GPTs/reports/8_1_verification.md GPTs/reports/eng_kor_parity.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' | sort
rg -n "trunk|Manuals/|ReleaseNotes/|Technical Documents|/home/|file://|C:/|ALTIBASE/Documents|github.com/ALTIBASE/Documents" GPTs/attachments/00_version_release_platform.md GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/05_data_types_properties.md GPTs/attachments/06_data_dictionary_performance_views.md GPTs/attachments/09_replication_ha_cdc.md GPTs/attachments/18_security_ssl_tls.md || true
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name README.md | wc -l
rg -n "V\$LOCK_TABLE_STATS|V\$MEM_STABLE|V\$TEMPORARY_LOBS|DBMS_STATS\.LOCK_TABLE_STATS|LOCK_TABLE_STATS" "Manuals/Altibase_7.1/eng/General Reference-2.The Data Dictionary.md" "Manuals/Altibase_7.3/eng/General Reference-2.The Data Dictionary.md" "Manuals/Altibase_trunk/eng/General Reference-2.The Data Dictionary.md" "Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md"
rg -n "TEMPORARY_LOB_ENABLE|MEMORY_TEMPLOB_MAX_ALLOC_SIZE|MEMORY_TEMPLOB_PIECE_SIZE|REPLICATION_SSL_PORT_NO|TRCLOG_EXPLAIN_TYPE|TRCLOG_JSON_PLAN_INDENT_DEPTH|CHECKPOINT_SCALE_SINGLE_DW_BUFFER_SIZE" "Manuals/Altibase_trunk/eng/General Reference-1.Data Types & Altibase Properties.md" "Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md"
```

## Findings

No Blocker or High findings were found in this stage.

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Note | Stage scope | n/a | The sampled high-risk 8.1 claims are supported by the source reports and sampled manuals, or are explicitly bounded as release-note-only / verify-on-installed-build material. | No attachment change is required for this stage. Keep the existing source-boundary warnings when later edits touch these sections. |

## Source Checks

- Claims checked:
  - 8.1 `JSON` type, size, syntax, restrictions, functions, path expressions, and `IS JSON`: attachment claims at `00_version_release_platform.md:97`-`100`, `03_sql_ddl_generation.md:1298`-`1315`, and `05_data_types_properties.md:565`-`589` match release-note lines `68`-`79` plus Korean fallback lines `2741`-`2778`, `2798`-`2814`, `23604`-`23616`, and `26496`-`26506`.
  - 8.1 Temporary LOB categories, cleanup, properties, and `V$TEMPORARY_LOBS`: attachment claims at `00_version_release_platform.md:101`-`103`, `05_data_types_properties.md:506`-`541`, `05_data_types_properties.md:1201`-`1262`, and `06_data_dictionary_performance_views.md:1494`-`1516` match release-note lines `83`-`96`, `321`-`330`, `370`-`374`, and Korean fallback lines `2617`-`2638`, `16014`-`16058`, `16549`-`16569`, `11665`-`11674`, and `16174`-`16206`.
  - 8.1 replication SSL: attachment claims at `09_replication_ha_cdc.md:392`-`460` and `18_security_ssl_tls.md:397`-`470` match release-note lines `133`-`138` and Korean fallback lines `1106`-`1123`, `1180`-`1202`, `12373`-`12393`, and `6874`-`6884`.
  - 8.1 new properties and performance views: attachment claims at `05_data_types_properties.md:39`, `05_data_types_properties.md:1502`-`1532`, and `06_data_dictionary_performance_views.md:35`-`39` match release-note lines `321`-`330` and `360`-`374`. The JSON plan properties remain correctly marked as release-note-only / verify-on-installed-server.
  - Platform and version boundaries: attachment claims at `00_version_release_platform.md:120`-`127` and `00_version_release_platform.md:317`-`341` match release-note lines `42`-`60` and `256`-`296`; 7.1/7.3 platform claims are consistent with the supported-platform source.
- Source coverage:
  - The source inventory maps every reviewed attachment to 7.1, 7.3, and 8.1 sources and lists no blocking source-path gaps.
  - The 8.1 verification and English/Korean parity reports explicitly authorize Korean fallback for JSON, Temporary LOB, `V$TEMPORARY_LOBS`, and replication SSL.
  - The reviewed attachments use customer-safe `Altibase 8.1 verified source` labeling and the scoped validation found no internal path, branch, `file://`, or local filesystem leakage in the six stage files.
- Source gaps:
  - JSON-formatted execution plan details remain release-note-only. The reviewed files avoid schema/value examples and instruct verification against `V$PROPERTY`, which is acceptable residual risk.
  - `V$LOCK_TABLE_STATS` is listed as an 8.1 release-note new performance view, while sampled 7.1 and 7.3 English data dictionaries also document it. `06_data_dictionary_performance_views.md:39` handles this safely by requiring `V$TABLE` availability checks for portable answers.

## Oracle-Overlap Decision

- Correctly compressed:
  - Ordinary DML remains outside this stage's high-risk content and is not expanded in the reviewed files.
  - `03_sql_ddl_generation.md` focuses DDL generation on Altibase-specific storage, tablespaces, JSON, Temporary LOB, properties, and replication.
- Too much generic Oracle material:
  - None found in the sampled high-risk sections.
- Missing Altibase-specific difference:
  - None found in the sampled high-risk sections. JSON/LOB restrictions and replication SSL port separation are explicitly called out.

## Version Checks

- 7.1:
  - Reviewed files avoid presenting native `JSON`, Temporary LOB, `USING SSL` replication, `REPLICATION_SSL_PORT_NO`, `SSL_CIPHER_SUITES`, or `SSL_LOAD_CONFIG` as 7.1 features.
  - Platform support is bounded to the 7.1 supported-platform source and distinguishes Windows client-only support.
- 7.3:
  - Reviewed files distinguish 7.3 OpenSSL 3.0.8 / TLS 1.3 / FIPS-related SSL properties from 8.1 replication SSL.
  - 7.3 replication compatibility is limited to documented LAZY/protocol guidance.
- 8.1:
  - Native `JSON`, Temporary LOB, `V$TEMPORARY_LOBS`, `USING SSL`, `REPLICATION_SSL_PORT_NO`, and JSON plan properties are version-scoped to Altibase 8.1 verified source.
  - 8.1 platform support is bounded to AIX 7.2, RHEL 7/8/9 x86-64, and Windows client-only entries as listed in the release notes.

## Retrieval And GPT Answer Quality

- Strengths:
  - High-risk tokens are literal and searchable: `JSON`, `TEMPORARY_LOB_ENABLE`, `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`, `MEMORY_TEMPLOB_PIECE_SIZE`, `V$TEMPORARY_LOBS`, `USING SSL`, `REPLICATION_SSL_PORT_NO`, `TRCLOG_EXPLAIN_TYPE`, and `TRCLOG_JSON_PLAN_INDENT_DEPTH`.
  - Replication SSL is repeated consistently in both replication and SSL/TLS attachments, with clear separation from ordinary `SSL_PORT_NO`.
  - The attachments include operational verification SQL rather than only prose descriptions.
- Risks:
  - Some 8.1 JSON and Temporary LOB details depend on translated Korean fallback; future edits should keep those source line references in work reports, not in customer-facing attachment text.
  - Release-note-only feature summaries in `00_version_release_platform.md` are safe as routing material, but should not be expanded into procedures without dedicated source support.

## Required Follow-Up

- No required follow-up for this stage.
- Keep JSON plan output limited to release-note-level statements unless a later source documents property values, output schema, or examples.
- If later jobs add more JSON function syntax or KADA/Kafka/ABM procedures, run a separate source audit before adding executable examples.
