# Source Audit QA Report

Job: `JOB-086`
Phase: P8 QA
Date: 2026-05-14
Result: Pass

## Objective

Verify that major, high-risk customer-facing claims in `GPTs/attachments/` trace to source manuals, release notes, or approved source reports.

Acceptance criterion: high-risk claims are sourced.

## Scope

- Customer-facing attachments: `GPTs/attachments/*.md`, excluding `README.md`
- Source reports:
  - `GPTs/reports/source_inventory.md`
  - `GPTs/reports/8_1_verification.md`
  - `GPTs/reports/eng_kor_parity.md`
  - `GPTs/reports/version_coverage_validation.md`
  - `GPTs/reports/english_consistency_validation.md`
- Source roots audited by targeted spot checks:
  - `Manuals/Altibase_7.1/eng`
  - `Manuals/Altibase_7.3/eng`
  - `Manuals/Altibase_trunk/eng`
  - `Manuals/Altibase_trunk/kor` for documented 8.1 fallback gaps
  - `Manuals/Tools/Altibase_release/eng`
  - `Manuals/Tools/Altibase_trunk/eng`
  - `ReleaseNotes/eng`
  - `Technical Documents/eng`
  - `Technical Documents/kor` where listed as supplemental in the inventory
  - `3rd Party Guide for Altibase/eng`

This is a work report. Internal source paths are intentionally preserved here. Customer-facing attachment files must continue to use safe labels such as `Altibase 8.1 verified source`.

## Summary

| Area | Audit result | Notes |
| --- | --- | --- |
| Source inventory coverage | Pass | `source_inventory.md` lists a source family for all 20 attachments across 7.1, 7.3, and Altibase 8.1 verified source. |
| English canonical source policy | Pass | `eng_kor_parity.md` documents English as canonical, with controlled Korean fallback only for specific 8.1 gaps. |
| 8.1 feature claims | Pass with caveats | JSON, Temporary LOB, replication SSL, and JSON plan claims trace to 8.1 release notes; detailed JSON, Temporary LOB, replication SSL, JSON errors, and `SQLFreeLob2` use documented Korean fallback where English manuals are incomplete. |
| Version-specific attachment claims | Pass | `version_coverage_validation.md` confirms every attachment covers 7.1, 7.3, and 8.1. |
| Customer-facing source labels | Pass | `english_consistency_validation.md` confirms all attachments use `Altibase 8.1 verified source` and have no `trunk`, `C:/`, or `file://` leakage. |
| Blocking unsourced high-risk claims | None found | No attachment changes were required. |

## High-Risk Claim Audit Matrix

| Claim group | Attachment coverage | Primary source trace | Audit result |
| --- | --- | --- | --- |
| Supported versions and platform boundaries, including Windows x64 client-only guidance | `00_version_release_platform.md`, `01_getting_started_installation.md` | `ReleaseNotes/eng/Altibase_7_1_0_1_2_Release_Notes.md`; `ReleaseNotes/eng/Altibase_7_3_0_0_1_Release_Notes.md`; `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`; `Technical Documents/eng/Supported Platforms.md:37`, `:70`, `:104`, `:134` | Sourced. Supported-platform claims should stay patch-aware. |
| 8.1 JSON data type, maximum size, standards, `JSON [ IN ROW size ]`, JSON functions, `IS JSON`, and `TEMPORARY_LOB_ENABLE` dependency | `00`, `03`, `04`, `05`, `07`, `10`, `12`, `15` | Release-note feature claim: `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md:68`-`:81`; Korean fallback details: `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md:2741`-`:2796`; `Manuals/Altibase_trunk/kor/SQL Reference.md:23604`-`:24025`, `:26496`; parity decision: `eng_kor_parity.md` | Sourced. English manual gap is documented; attachments correctly use English canonical wording. |
| 8.1 Temporary LOB categories, creation cases, cleanup, properties, and `V$TEMPORARY_LOBS` | `03`, `05`, `06`, `07`, `10`, `11`, `12` | Release-note claim: `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md:83`-`:96`, `:324`-`:328`, `:374`; Korean fallback: `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md:2617`-`:2638`, `:16014`, `:16038`, `:16549`; `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md:11665`-`:11684`; `Manuals/Altibase_trunk/kor/SQL Reference.md:16174`-`:16206` | Sourced. Keep the feature scoped to 8.1 unless the user proves another version supports it. |
| 8.1 replication SSL using `USING SSL` and `REPLICATION_SSL_PORT_NO` | `00`, `03`, `07`, `09`, `18` | Release-note claim: `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md:133`-`:138`, `:326`; Korean fallback syntax/property detail: `Manuals/Altibase_trunk/kor/Replication Manual.md:1110`, `:1188`, `:1198`; `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md:12373`; `Manuals/Altibase_trunk/kor/SQL Reference.md:6877` | Sourced. Attachments correctly separate replication SSL from ordinary client/server SSL. |
| 8.1 JSON-format execution plan and `TRCLOG_EXPLAIN_TYPE`, `TRCLOG_JSON_PLAN_INDENT_DEPTH` | `08_performance_tuning_monitoring.md` | `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md:231`-`:233`, `:329`-`:330`; `8_1_verification.md` documents no English or Korean manual schema detail | Sourced with narrow scope. Attachment correctly says not to invent JSON plan field names, property values, or examples. |
| 8.1 checkpoint scale single and `V$MEM_STABLE` | `00`, `02`, `06` | `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md:155`-`:157`, `:323`, `:373`; `Manuals/Altibase_trunk/eng/Administrator’s Manual.md:6757`-`:6786`; `Manuals/Altibase_trunk/eng/General Reference-2.The Data Dictionary.md:7321`-`:7441` | Sourced. |
| Idempotent DDL clauses `IF NOT EXISTS` and `IF EXISTS` in 8.1 SQL generation | `03`, `09`, `10`, `16` | `Manuals/Altibase_trunk/eng/SQL Reference.md:5244`-`:9459`; DB Link-specific clauses in `Manuals/Altibase_trunk/eng/DB Link User's Manual.md:1025`-`:1085`; external library clauses in `Manuals/Altibase_trunk/eng/External Procedures Manual.md:747`-`:800`; package/typeset clauses in `Manuals/Altibase_trunk/eng/Stored Procedures Manual.md:6077`, `:7277`, `:7501` | Sourced. Attachments correctly omit these clauses for 7.1/7.3 unless explicitly version-confirmed. |
| Data dictionary, property, and performance-view check SQL patterns | `03`, `05`, `06`, `08`, `09` | `Manuals/Altibase_7.1/eng/General Reference-2.The Data Dictionary.md`; `Manuals/Altibase_7.3/eng/General Reference-2.The Data Dictionary.md`; `Manuals/Altibase_trunk/eng/General Reference-2.The Data Dictionary.md`; 8.1 release notes for new properties/views | Sourced by manual family and release-note deltas. Use `V$TABLE` and `V$ALLCOLUMN` checks where view/column availability varies. |
| Error response format and JSON/SSL/LOB/tablespace/replication error blocks | `07_error_messages_troubleshooting.md` | English error references for 7.1/7.3/8.1; JSON fallback symbols in `Manuals/Altibase_trunk/kor/Error Message Reference.md:14893`-`:14981`; SSL sources in SSL/TLS guides and release notes | Sourced. JSON error blocks are correctly 8.1-sensitive. |
| Replication modes, compatibility, DDL sync restrictions, protocol caveats, Log Analyzer CDC, and network checks | `09_replication_ha_cdc.md` | `Manuals/Altibase_7.1/eng/Replication Manual.md`; `Manuals/Altibase_7.3/eng/Replication Manual.md`; `Manuals/Altibase_trunk/eng/Replication Manual.md`; `ReleaseNotes/eng/Altibase_7_3_0_0_1_Release_Notes.md:186`-`:205`, `:475`-`:588`; `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md:282`-`:296`; supplemental `Technical Documents/kor/ReplicationCompatibility.md` and `Replication network check.md` | Sourced. Compatibility wording should remain conservative and version-specific. |
| SSL/TLS setup, OpenSSL 3.0.8, TLS 1.3, FIPS, ordinary SSL ports, and client connection properties | `07`, `11`, `12`, `13`, `14`, `18` | `ReleaseNotes/eng/Altibase_7_3_0_0_1_Release_Notes.md:105`-`:109`, `:634`-`:635`; `Manuals/Altibase_7.3/eng/Altibase SSL TLS User's Guide.md:245`-`:343`, `:507`-`:532`, `:613`-`:635`; `Manuals/Altibase_trunk/eng/Altibase SSL TLS User's Guide.md:243`-`:343`, `:507`-`:532`, `:607`-`:626` | Sourced. Attachment 18 correctly separates ordinary SSL from replication SSL. |
| JDBC 4.2, Maven Central availability, Hibernate 6.4 `AltibaseDialect`, `lob_null_select`, statement cache, and Java compatibility | `11_java_jdbc_spring.md`, `16_dblink_external_connectors.md`, `19_spatial_nifi_tableau_misc.md` | `ReleaseNotes/eng/Altibase_7_3_0_0_1_Release_Notes.md:101`-`:103`, `:499`-`:564`; `Manuals/Altibase_7.3/eng/JDBC User's Manual.md:3363`-`:3398`, `:3558`-`:3807`; `3rd Party Guide for Altibase/eng/Spring Data JPA With Hibernate 6.4 User's Guide for Altibase.md:43`-`:63`, `:103`-`:112`; Java compatibility fallback in `Technical Documents/kor/JavaCompatibility.md` | Sourced. Keep Java compatibility as source-backed supplemental guidance. |
| CLI/ODBC LOB locator cleanup, including 8.1 `SQLFreeLob2` after `SQLPutLob()` on JSON data | `12_c_cli_odbc_precompiler.md` | English CLI/ODBC/C Interface/Precompiler manuals for general interface behavior; Korean fallback for `SQLFreeLob2`: `Manuals/Altibase_trunk/kor/CLI User's Manual.md:8169`-`:8202` | Sourced. Attachment correctly limits `SQLFreeLob2` to 8.1 JSON LOB locator cleanup. |
| PSM, user-defined types, packages, pragmas, external procedures, external library behavior, and external mode risk | `10_psm_stored_external_procedures.md` | `Manuals/Altibase_trunk/eng/Stored Procedures Manual.md:5198`-`:5297`, `:6925`-`:7192`, `:7277`-`:7503`; `Manuals/Altibase_trunk/eng/External Procedures Manual.md:245`-`:301`, `:340`-`:350`, `:737`-`:800` | Sourced. 8.1 Temporary LOB-in-PSM statements trace through the 8.1 Temporary LOB sources above. |
| iSQL, iLoader command usage, form/data files, load modes, delimiters, LOB handling, bad files, and option caveats | `13_isql_iloader_basic_tools.md` | `Manuals/Altibase_trunk/eng/iSQL User's Manual.md:319`-`:843`; `Manuals/Altibase_trunk/eng/iLoader User's Manual.md:2385`-`:2486`, `:2511`-`:2734`; 7.1/7.3 equivalents listed in `source_inventory.md` | Sourced. |
| Utility roles: `aexport`, `altiComp`, `dataCompJ`, `aku`, diagnostic tools, and destructive-operation cautions | `14_utilities_operation_tools.md`, `17_kubernetes_aku_cloud.md` | `Manuals/Altibase_trunk/eng/Utilities Manual.md:257`-`:684`, `:1068`-`:1128`, `:1796`-`:1849`; `Manuals/Tools/Altibase_trunk/eng/dataCompJ User's Manual.md:331`-`:365`, `:419`-`:447`, `:560`-`:1130`; `ReleaseNotes/eng/Altibase_dataCompJ_7_2_Release_Notes.md:126`-`:162` | Sourced. |
| Migration Center process, CLI/GUI model, data validation, JSON mapping, LOB/`NOT NULL`, empty strings, partition/external-table conversion, and PSM converter TODO review | `15_migration_oracle_compatibility.md` | `Manuals/Tools/Altibase_trunk/eng/Migration Center User's Manual.md:420`-`:448`, `:887`-`:952`, `:1065`-`:1068`, `:1193`-`:1219`, `:2170`-`:2262`, `:7837`-`:7839`; `ReleaseNotes/eng/Altibase_Migration_Center_7_19_Release_Notes.md:122`-`:179`; `Manuals/Altibase_trunk/eng/Adapter for Oracle User's Manual.md:862`, `:945`-`:965` | Sourced. |
| DB Link syntax, `REMOTE_TABLE`, `REMOTE_EXECUTE_*`, global transaction levels, Hadoop Connector, DBeaver, Hibernate, and OpenLDAP `back-sql` | `16_dblink_external_connectors.md` | `Manuals/Altibase_trunk/eng/DB Link User's Manual.md:458`-`:464`, `:545`-`:560`, `:654`-`:657`, `:1005`-`:1085`, `:1191`-`:1236`, `:1383`-`:1415`; `Manuals/Altibase_trunk/eng/Hadoop Connector User's Manual.md`; `Manuals/Tools/Altibase_trunk/eng/Altibase 3rd Party Connector Guide.md:226`-`:641` | Sourced. |
| AKU replica limits, Kubernetes pod/service/StatefulSet workflows, dynamic Pod IP replication, scale-up/down, and multiple replication configuration | `17_kubernetes_aku_cloud.md` | `Manuals/Altibase_7.1/eng/Utilities Manual.md:1796`-`:1823`; `Manuals/Altibase_7.3/eng/Utilities Manual.md:1823`-`:1849`; `Manuals/Altibase_trunk/eng/Utilities Manual.md:1819`-`:1845`; `3rd Party Guide for Altibase/eng/Altibase aku Sample Guide for Kubernetes.md:258`-`:272`, `:516`-`:565`; `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md:211`-`:216` | Sourced. |
| Spatial `GEOMETRY`, SRID, R-Tree restrictions, `SPATIAL_REF_SYS`, altiShapeLoader, NiFi, and Tableau procedures | `19_spatial_nifi_tableau_misc.md` | `Manuals/Altibase_trunk/eng/Spatial SQL Reference.md:6835`-`:7068`; `Manuals/Tools/Altibase_trunk/eng/altiShapeLoader User's Manual.md:232`-`:337`; `3rd Party Guide for Altibase/eng/NiFi User's Guide for Altibase.md:42`-`:185`; `3rd Party Guide for Altibase/eng/Tableau User's Guide for Altibase/Tableau User's Guide for Altibase.md:27`-`:80` | Sourced. |

## 8.1 Source Caveats

- JSON and Temporary LOB: feature existence is confirmed by English 8.1 release notes; detailed manual text is in Korean 8.1 sources. The attachment set translated and normalized those details into English canonical text. This is acceptable under `eng_kor_parity.md`.
- Replication SSL: English 8.1 release notes confirm `USING SSL` and `REPLICATION_SSL_PORT_NO`; replication-specific syntax/property detail is backed by Korean 8.1 manuals.
- JSON plan: the only verified source basis is the English 8.1 release notes. The performance attachment correctly avoids JSON plan schema, example output, and property value claims.
- `SQLFreeLob2`: English 8.1 CLI source did not contain the targeted text. Korean CLI source backs the 8.1 JSON LOB cleanup guidance.

## Attachment-Level Source Status

| Attachment | Source status |
| --- | --- |
| `00_version_release_platform.md` | Sourced by release notes, supported-platform document, and 8.1 verified source caveats. |
| `01_getting_started_installation.md` | Sourced by Getting Started, Installation, release notes, and supported-platform guidance. |
| `02_administration_operations.md` | Sourced by Administrator manuals; 8.1 checkpoint claims also trace to release notes and Data Dictionary. |
| `03_sql_ddl_generation.md` | Sourced by SQL Reference, General Reference, Data Dictionary, Replication Manual, release notes, and controlled 8.1 fallback. |
| `04_sql_dml_oracle_compatibility.md` | Sourced by SQL Reference; JSON DML/function claims use 8.1 release notes and Korean fallback. |
| `05_data_types_properties.md` | Sourced by General Reference and release notes; JSON/Temporary LOB/property details use controlled 8.1 fallback. |
| `06_data_dictionary_performance_views.md` | Sourced by Data Dictionary and release-note deltas; `V$TEMPORARY_LOBS` uses controlled 8.1 fallback. |
| `07_error_messages_troubleshooting.md` | Sourced by Error Message Reference; JSON error blocks use controlled 8.1 fallback. |
| `08_performance_tuning_monitoring.md` | Sourced by Performance Tuning, Monitoring API, SNMP, and release notes; JSON plan is correctly release-note-only. |
| `09_replication_ha_cdc.md` | Sourced by Replication Manual, Log Analyzer, Replication Manager, release notes, and Korean supplemental compatibility/network docs. |
| `10_psm_stored_external_procedures.md` | Sourced by Stored Procedures, External Procedures, and 8.1 Temporary LOB fallback. |
| `11_java_jdbc_spring.md` | Sourced by JDBC, Adapter for JDBC, Spring/Hibernate guides, release notes, and Java compatibility supplemental source. |
| `12_c_cli_odbc_precompiler.md` | Sourced by CLI, ODBC, C Interface, Precompiler manuals; `SQLFreeLob2` uses controlled 8.1 fallback. |
| `13_isql_iloader_basic_tools.md` | Sourced by iSQL and iLoader manuals. |
| `14_utilities_operation_tools.md` | Sourced by Utilities, dataCompJ manual, and dataCompJ release notes. |
| `15_migration_oracle_compatibility.md` | Sourced by Migration Center, Adapter for Oracle, and Migration Center release notes. |
| `16_dblink_external_connectors.md` | Sourced by DB Link, Hadoop Connector, and third-party connector guides. |
| `17_kubernetes_aku_cloud.md` | Sourced by Utilities, Kubernetes guide, AKU sample guide, and release notes. |
| `18_security_ssl_tls.md` | Sourced by SSL/TLS guides, General Reference where applicable, release notes, and controlled replication SSL fallback. |
| `19_spatial_nifi_tableau_misc.md` | Sourced by Spatial SQL Reference, altiShapeLoader, NiFi, and Tableau guides. |

## Commands Used

Representative audit commands:

```bash
find GPTs/attachments -maxdepth 1 -type f -name '*.md' | sort
sed -n '1,520p' GPTs/reports/source_inventory.md
sed -n '1,220p' GPTs/reports/8_1_verification.md
sed -n '1,220p' GPTs/reports/eng_kor_parity.md
rg -n "JSON|Temporary LOB|TEMPORARY_LOB|REPLICATION_SSL_PORT_NO|USING SSL|TRCLOG_EXPLAIN_TYPE|TRCLOG_JSON_PLAN_INDENT_DEPTH" ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md
rg -n -i "JSON|Temporary LOB|TEMPORARY_LOB|MEMORY_TEMPLOB|V\\$TEMPORARY_LOBS|USING SSL|REPLICATION_SSL_PORT_NO|SQLFreeLob2|qpERR_ABORT_JSON|mtERR_ABORT_JSON" Manuals/Altibase_trunk/kor
rg -n -i "IF NOT EXISTS|IF EXISTS" Manuals/Altibase_trunk/eng/SQL\ Reference.md Manuals/Altibase_trunk/eng/DB\ Link\ User\'s\ Manual.md
rg -n -i "OpenSSL 3\\.0\\.8|TLS 1\\.3|FIPS|SSL_LOAD_CONFIG|SSL_PORT_NO|ALTIBASE_SSL_PORT_NO" ReleaseNotes/eng Manuals/Altibase_7.3/eng/Altibase\ SSL\ TLS\ User\'s\ Guide.md Manuals/Altibase_trunk/eng/Altibase\ SSL\ TLS\ User\'s\ Guide.md
rg -n -i "Maven Central|Hibernate 6\\.4|lob_null_select|JDBC 4\\.2" Manuals/Altibase_7.3/eng/JDBC\ User\'s\ Manual.md "3rd Party Guide for Altibase/eng"
rg -n -i "up to .*4|up to .*6|multiple replication|REPLICATIONS" Manuals/Altibase_7.1/eng/Utilities\ Manual.md Manuals/Altibase_7.3/eng/Utilities\ Manual.md Manuals/Altibase_trunk/eng/Utilities\ Manual.md "3rd Party Guide for Altibase/eng/Altibase aku Sample Guide for Kubernetes.md" ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md
rg -n -i "JSON|IS JSON|Empty String|LOB.*NOT NULL|Data Validation|Include LOB|Batch LOB" Manuals/Tools/Altibase_trunk/eng/Migration\ Center\ User\'s\ Manual.md
```

## Conclusion

The high-risk claims in the attachment set are traceable to source manuals, release notes, or previously accepted source reports. The only narrow-source areas are already documented and constrained: 8.1 JSON detail, Temporary LOB detail, replication SSL detail, JSON error blocks, `SQLFreeLob2`, and JSON-format execution plan output.

`JOB-086` acceptance criteria are satisfied.
