# R02 High-Risk Source Traceability Audit

Date: 2026-05-14
Reviewer: Codex
Verdict: Review Required

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
  - `ReleaseNotes/eng/Altibase_7_3_0_0_1_Release_Notes.md`
  - `ReleaseNotes/eng/Altibase_7_1_0_1_2_Release_Notes.md`
  - `Technical Documents/eng/Supported Platforms.md`
  - `Manuals/Altibase_trunk/eng/Replication Manual.md`
  - `Manuals/Altibase_trunk/kor/Replication Manual.md`
  - `Manuals/Altibase_trunk/kor/SQL Reference.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`

## Commands Run

```bash
sed -n '1,220p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,220p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,220p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
cat review/review_stages.tsv
rg -n -i "JSON|TEMPORARY LOB|TEMPORARY_LOB|TEMPLOB|V\$TEMPORARY_LOBS|MEMORY_TEMPLOB|REPLICATION_SSL_PORT_NO|USING SSL|SSL|TLS|TRCLOG_EXPLAIN_TYPE|TRCLOG_JSON_PLAN_INDENT_DEPTH|platform|supported|8\.1|7\.3|7\.1" GPTs/attachments/00_version_release_platform.md GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/05_data_types_properties.md GPTs/attachments/06_data_dictionary_performance_views.md GPTs/attachments/09_replication_ha_cdc.md GPTs/attachments/18_security_ssl_tls.md
rg -n "trunk|Manuals/|ReleaseNotes/|C:/|file://|Altibase_" GPTs/attachments/00_version_release_platform.md GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/05_data_types_properties.md GPTs/attachments/06_data_dictionary_performance_views.md GPTs/attachments/09_replication_ha_cdc.md GPTs/attachments/18_security_ssl_tls.md
find GPTs/attachments -maxdepth 1 -name '*.md' ! -name README.md | sort | wc -l
nl -ba ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md | sed -n '38,62p'
nl -ba ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md | sed -n '60,140p'
nl -ba ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md | sed -n '220,240p'
nl -ba ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md | sed -n '316,332p'
nl -ba ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md | sed -n '358,378p'
nl -ba "Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md" | sed -n '2614,2642p'
nl -ba "Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md" | sed -n '2738,2784p'
nl -ba "Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md" | sed -n '16010,16046p'
nl -ba "Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md" | sed -n '16545,16575p'
nl -ba "Manuals/Altibase_trunk/kor/Replication Manual.md" | sed -n '1106,1114p'
nl -ba "Manuals/Altibase_trunk/kor/Replication Manual.md" | sed -n '1184,1202p'
nl -ba "Manuals/Altibase_trunk/eng/Replication Manual.md" | sed -n '630,700p'
rg -n -i "sub-?millisecond|built-in conflict resolution|ShardManager" "Manuals/Altibase_7.1/eng/Replication Manual.md" "Manuals/Altibase_7.3/eng/Replication Manual.md" "Manuals/Altibase_trunk/eng/Replication Manual.md" GPTs/reports/source_inventory.md GPTs/reports/8_1_verification.md GPTs/reports/eng_kor_parity.md
```

## Findings

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| High | `GPTs/attachments/09_replication_ha_cdc.md` | 20 | Unsupported and contradicted HA wording: the Active-Active overview says Altibase replication "guarantees sub-millisecond latency and built-in conflict resolution." The sampled replication manual does not support a latency guarantee, and it explicitly says replication cannot guarantee data consistency against conflicts and that deferred replication has no perfect conflict solution (`Manuals/Altibase_trunk/eng/Replication Manual.md:657`, `:661`-`:675`). The same attachment later gives safer conflict guidance at lines 181-187, so this overview can cause the GPT to answer incorrectly. | Replace the sentence with source-bounded wording: Altibase replication replays XLogs and supports LAZY/EAGER modes plus documented conflict-resolution schemes, but latency depends on workload/network and conflict handling requires routing, ownership, and validation. Remove "guarantees sub-millisecond latency" and avoid implying automatic conflict safety. |
| High | `GPTs/attachments/09_replication_ha_cdc.md` | 21 | Sharding/scale-out guidance is not traceable to the selected source set for this attachment. `source_inventory.md` scopes `09_replication_ha_cdc.md` to replication, Log Analyzer, Replication Manager, replication compatibility, network checks, and replication SSL (`GPTs/reports/source_inventory.md:162`-`:180`), while `eng_kor_parity.md` says Korean-only `Sharding(deprecated).md` is not in the current attachment source inventory (`GPTs/reports/eng_kor_parity.md:33`). The line tells the GPT to refer users to ShardManager scale-out without source-backed procedures or version boundaries. | Remove the sharding overview from `09_replication_ha_cdc.md`, or mark it as requiring a separate selected sharding source before the GPT answers ShardManager/scale-out setup questions. Keep replication/HA separate from data scale-out. |
| Medium | `GPTs/attachments/05_data_types_properties.md` | 576 | The JSON path expression restriction is not traceable in the sampled text sources or source reports. The line says JSON function path expressions must be string literals and cannot be bind variables, `NULL`, table columns, SQL functions, or user-defined functions. The reports verify JSON feature existence and fallback sections (`GPTs/reports/8_1_verification.md:31`-`:44`, `GPTs/reports/eng_kor_parity.md:63`-`:64`), but do not document this operand restriction. The Korean SQL Reference sections sampled around JSON functions describe function categories and examples, but the restriction appears to need syntax-diagram verification. | Either add a follow-up marker to verify the JSON function grammar image/converted BNF, or soften the line to "verify the JSON path operand form in the 8.1 SQL Reference before generating dynamic path-expression SQL." Do not rely on this detailed restriction as source-confirmed until the grammar is converted or a textual source is found. |

## Source Checks

- Claims checked:
  - 8.1 native `JSON`, function list, standards, and `JSON [ IN ROW size ]` in `00`, `03`, and `05`.
  - 8.1 Temporary LOB lifecycle, properties, `V$TEMPORARY_LOBS`, and `ALTER SESSION SET FREE TEMPORARY LOB` in `00`, `05`, and `06`.
  - 8.1 replication SSL with `USING SSL` and `REPLICATION_SSL_PORT_NO` in `00`, `03`, `09`, and `18`.
  - 8.1 JSON execution-plan property names in `00` and `05`.
  - 7.1, 7.3, and 8.1 platform/version boundaries in `00`.
- Source coverage:
  - JSON feature existence is supported by 8.1 release notes (`ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md:68`-`:79`) and Korean fallback details for size, standards, syntax, Temporary LOB dependency, depth, and `SELECT FOR UPDATE` restriction (`Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md:2741`-`:2778`).
  - JSON function names and `IS JSON` are supported by Korean SQL Reference (`Manuals/Altibase_trunk/kor/SQL Reference.md:23604`-`:23616`, `:26496`).
  - Temporary LOB feature existence is supported by 8.1 release notes (`ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md:83`-`:96`) and Korean fallback details (`Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md:2617`-`:2638`, `:16014`-`:16036`, `:16038`-`:16046`, `:16549`-`:16572`; `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md:11665`-`:11674`; `Manuals/Altibase_trunk/kor/SQL Reference.md:16174`-`:16206`).
  - Replication SSL is supported by 8.1 release notes (`ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md:133`-`:138`, `:326`) and Korean replication/property fallback (`Manuals/Altibase_trunk/kor/Replication Manual.md:1106`-`:1110`, `:1187`-`:1198`; `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md:12373`-`:12389`).
  - JSON plan wording is appropriately narrow: release notes support JSON-formatted execution-plan output and the two property names (`ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md:231`-`:233`, `:329`-`:330`), and `8_1_verification.md` warns not to invent schema or examples (`GPTs/reports/8_1_verification.md:81`-`:87`).
  - 8.1 platform boundaries in `00` align with the release-note platform table (`ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md:42`-`:60`). 7.3 and 7.1 platform patch conditions align with the supported-platform document (`Technical Documents/eng/Supported Platforms.md:47`-`:71`, `:114`-`:136`).
- Source gaps:
  - No sampled source or report supports a "sub-millisecond latency" replication guarantee.
  - No selected `09` source supports customer-facing ShardManager setup guidance.
  - JSON path operand restrictions need grammar-image or textual source follow-up.

## Oracle-Overlap Decision

- Correctly compressed: The sampled files keep ordinary Oracle-overlapping DML out of scope and focus on Altibase-specific DDL, JSON, Temporary LOB, properties, data dictionary, replication, platform, and SSL/TLS.
- Too much generic Oracle material: None found in the sampled high-risk blocks.
- Missing Altibase-specific difference: The unsupported Active-Active overview obscures the actual Altibase-specific conflict caveats that are correctly documented later in the same file.

## Version Checks

- 7.1: Scoped claims correctly avoid native `JSON`, Temporary LOB, `V$TEMPORARY_LOBS`, and replication SSL. Platform guidance distinguishes Windows client-only support.
- 7.3: Scoped claims correctly avoid native `JSON`, Temporary LOB, and replication SSL; platform guidance includes 7.3 patch-conditioned platforms.
- 8.1: Core high-risk 8.1 claims for `JSON`, Temporary LOB, `V$TEMPORARY_LOBS`, `REPLICATION_SSL_PORT_NO`, `USING SSL`, and JSON plan property names are traceable. Detailed JSON path restrictions and unrelated ShardManager guidance need follow-up or removal.

## Retrieval And GPT Answer Quality

- Strengths:
  - The scoped attachments preserve literal property names, view names, function names, and syntax tokens.
  - 8.1 JSON plan content is correctly narrow and release-note-only.
  - Replication SSL is mostly well separated from ordinary client/server SSL in `09` and `18`.
  - Platform answer guidance in `00` explicitly avoids cross-version platform inference.
- Risks:
  - The unsupported Active-Active guarantee is early in `09` and likely to be retrieved before safer caveats later in the file.
  - The Sharding/ShardManager line may cause the GPT to answer scale-out setup questions from an unselected or deprecated source area.
  - The JSON path operand restriction may generate over-restrictive SQL advice unless verified.

## Required Follow-Up

- Remove or rewrite the Active-Active guarantee in `GPTs/attachments/09_replication_ha_cdc.md:20`.
- Remove the Sharding/ShardManager scale-out statement in `GPTs/attachments/09_replication_ha_cdc.md:21`, or create a separate source-backed sharding review scope before keeping it.
- Verify `GPTs/attachments/05_data_types_properties.md:576` against a converted 8.1 JSON function grammar or mark it as needing exact-version verification.
- After those scoped updates, rerun the high-risk `rg` checks for `sub-millisecond`, `ShardManager`, `JSON path expressions used by JSON functions`, `USING SSL`, `REPLICATION_SSL_PORT_NO`, and `V$TEMPORARY_LOBS`.
