# Altibase GPTs Source Inventory

Job: `JOB-010`
Phase: P1 Inventory
Status: Complete

This report inventories source availability for the 20 GPT attachment files. Korean Altibase manuals are the authoritative latest manual source. English manuals can be used for convenient extraction and English wording, but when English and Korean manuals differ, the Korean manual is the source of truth and English-facing artifacts should be updated or normalized from the Korean source.

For Altibase 8.1, the internally verified source set is the current 8.1 verified manual tree plus the 8.1 release notes. Customer-facing attachments must label this as "Altibase 8.1 verified source" or equivalent wording, not by the internal directory name.

## Source Roots

- Altibase 7.1 manuals: `Manuals/Altibase_7.1/kor` authoritative, `Manuals/Altibase_7.1/eng` English extraction/reference
- Altibase 7.3 manuals: `Manuals/Altibase_7.3/kor` authoritative, `Manuals/Altibase_7.3/eng` English extraction/reference
- Altibase 8.1 verified source manuals: `Manuals/Altibase_trunk/kor` authoritative, `Manuals/Altibase_trunk/eng` English extraction/reference
- Release notes, English: `ReleaseNotes/eng`
- Release notes, Korean: `ReleaseNotes/kor` authoritative if release-note content differs from English
- Patch notes: `PatchNotes/*/kor` authoritative for patch-level behavior; `PatchNotes/*/eng` English extraction/reference when present
- Tool manuals, release source: `Manuals/Tools/Altibase_release/kor` authoritative, `Manuals/Tools/Altibase_release/eng` English extraction/reference
- Tool manuals, Altibase 8.1 verified source: `Manuals/Tools/Altibase_trunk/kor` authoritative, `Manuals/Tools/Altibase_trunk/eng` English extraction/reference
- Technical documents: `Technical Documents/kor` authoritative when paired or Korean-only, `Technical Documents/eng` English extraction/reference
- Third-party guides: `3rd Party Guide for Altibase/eng`

## Inventory Summary

- Attachment files inventoried: 20
- Attachments with 7.1 source paths: 20
- Attachments with 7.3 source paths: 20
- Attachments with Altibase 8.1 verified source paths: 20
- Missing blocking source paths: none
- Korean supplemental technical documents: `Technical Documents/kor/JavaCompatibility.md`, `Technical Documents/kor/ReplicationCompatibility.md`, `Technical Documents/kor/Replication network check.md`

## Attachment Source Inventory

### 00_version_release_platform.md

Source purpose: release history, version differences, supported platforms, upgrade cautions.

- 7.1:
  - `ReleaseNotes/eng/Altibase_7_1_0_1_2_Release_Notes.md`
  - `Technical Documents/eng/Supported Platforms.md`
- 7.3:
  - `ReleaseNotes/eng/Altibase_7_3_0_0_1_Release_Notes.md`
  - `Technical Documents/eng/Supported Platforms.md`
- Altibase 8.1 verified source:
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`
  - `Technical Documents/eng/Supported Platforms.md`
- Korean source authority/check:
  - `ReleaseNotes/kor/Altibase_7_1_0_1_2_Release_Notes.md`
  - `ReleaseNotes/kor/Altibase_7_3_0_0_1_Release_Notes.md`
  - `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`
  - `Technical Documents/kor/Supported Platforms.md`

### 01_getting_started_installation.md

Source purpose: installation, database creation, startup, shutdown, first-run checks.

- 7.1:
  - `Manuals/Altibase_7.1/eng/Getting Started Guide.md`
  - `Manuals/Altibase_7.1/eng/Installation Guide.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/Getting Started Guide.md`
  - `Manuals/Altibase_7.3/eng/Installation Guide.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/Getting Started Guide.md`
  - `Manuals/Altibase_trunk/eng/Installation Guide.md`
- Korean source authority/check:
  - `Manuals/Altibase_7.1/kor/Getting Started Guide.md`
  - `Manuals/Altibase_7.1/kor/Installation Guide.md`
  - `Manuals/Altibase_7.3/kor/Getting Started Guide.md`
  - `Manuals/Altibase_7.3/kor/Installation Guide.md`
  - `Manuals/Altibase_trunk/kor/Getting Started Guide.md`
  - `Manuals/Altibase_trunk/kor/Installation Guide.md`

### 02_administration_operations.md

Source purpose: administration, accounts, backup/recovery, tablespaces, server operations.

- 7.1:
  - `Manuals/Altibase_7.1/eng/Administrator's Manual.md`
  - `Manuals/Altibase_7.1/eng/SQL Reference.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/Administrator’s Manual.md`
  - `Manuals/Altibase_7.3/eng/SQL Reference.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/Administrator’s Manual.md`
  - `Manuals/Altibase_trunk/eng/SQL Reference.md`
- Korean source authority/check:
  - `Manuals/Altibase_7.1/kor/Administrator's Manual.md`
  - `Manuals/Altibase_7.1/kor/SQL Reference.md`
  - `Manuals/Altibase_7.3/kor/Administrator's Manual.md`
  - `Manuals/Altibase_7.3/kor/SQL Reference.md`
  - `Manuals/Altibase_trunk/kor/Administrator's Manual.md`
  - `Manuals/Altibase_trunk/kor/SQL Reference.md`

### 03_sql_ddl_generation.md

Source purpose: DDL/DCL generation, tablespaces, tables, indexes, users, replication SQL, Log Analyzer CDC syntax, property checks.

- 7.1:
  - `Manuals/Altibase_7.1/eng/SQL Reference.md`
  - `Manuals/Altibase_7.1/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_7.1/eng/Replication Manual.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/SQL Reference.md`
  - `Manuals/Altibase_7.3/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_7.3/eng/Replication Manual.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/SQL Reference.md`
  - `Manuals/Altibase_trunk/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_trunk/eng/Replication Manual.md`
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`
- Korean source authority/check:
  - `Manuals/Altibase_7.1/kor/SQL Reference.md`
  - `Manuals/Altibase_7.1/kor/Replication Manual.md`
  - `Manuals/Altibase_7.1/kor/Log Analyzer User's Manual.md`
  - `Manuals/Altibase_7.1/kor/Administrator's Manual.md`
  - `Manuals/Altibase_7.3/kor/SQL Reference.md`
  - `Manuals/Altibase_7.3/kor/Replication Manual.md`
  - `Manuals/Altibase_7.3/kor/Log Analyzer User's Manual.md`
  - `Manuals/Altibase_7.3/kor/Administrator's Manual.md`
  - `Manuals/Altibase_trunk/kor/SQL Reference.md`
  - `Manuals/Altibase_trunk/kor/Replication Manual.md`
  - `Manuals/Altibase_trunk/kor/Log Analyzer User's Manual.md`
  - `Manuals/Altibase_trunk/kor/Administrator's Manual.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
- R03 source-drift note: Korean SQL Reference and General Reference differ on omitted user disk datafile `SIZE` defaults; the attachment now directs generated DDL to emit explicit disk datafile `SIZE`, `NEXT`, and `MAXSIZE` values instead of relying on omitted defaults.

### 04_sql_dml_oracle_compatibility.md

Source purpose: DML, expressions, functions, Oracle compatibility boundaries, SQL differences.

- 7.1:
  - `Manuals/Altibase_7.1/eng/SQL Reference.md`
  - `Manuals/Altibase_7.1/eng/General Reference-1.Data Types & Altibase Properties.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/SQL Reference.md`
  - `Manuals/Altibase_7.3/eng/General Reference-1.Data Types & Altibase Properties.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/SQL Reference.md`
  - `Manuals/Altibase_trunk/eng/General Reference-1.Data Types & Altibase Properties.md`
- Korean source authority/check:
  - `Manuals/Altibase_7.1/kor/SQL Reference.md`
  - `Manuals/Altibase_7.1/kor/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_7.3/kor/SQL Reference.md`
  - `Manuals/Altibase_7.3/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_trunk/kor/SQL Reference.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
- R07 source-detail note: Korean SQL Reference confirms the Altibase 7.1.0.7.7 boundary for PCRE2-compatible `REGEXP_MODE=1`; Korean General Reference confirms 8.1 JSON path operands are string-form only and cannot be bind variables, `NULL`, table columns, SQL functions, or user-defined functions.

### 05_data_types_properties.md

Source purpose: data types, Altibase properties, JSON, LOB behavior, version-specific property changes.

- 7.1:
  - `Manuals/Altibase_7.1/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `ReleaseNotes/eng/Altibase_7_1_0_1_2_Release_Notes.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `ReleaseNotes/eng/Altibase_7_3_0_0_1_Release_Notes.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`

### 06_data_dictionary_performance_views.md

Source purpose: meta tables, data dictionary, performance views, operational check queries.

- 7.1:
  - `Manuals/Altibase_7.1/eng/General Reference-2.The Data Dictionary.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/General Reference-2.The Data Dictionary.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/General Reference-2.The Data Dictionary.md`
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`
- Korean source authority/check:
  - `Manuals/Altibase_7.1/kor/SQL Reference.md`
  - `Manuals/Altibase_7.1/kor/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`
  - `PatchNotes/Altibase_7.1/kor/Altibase_7_1_0_8_5_Patch_Notes.md`

### 07_error_messages_troubleshooting.md

Source purpose: error codes, causes, actions, troubleshooting response format.

- 7.1:
  - `Manuals/Altibase_7.1/eng/Error Message Reference.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/Error Message Reference.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/Error Message Reference.md`
- Korean source authority/check:
  - `Manuals/Altibase_7.1/kor/Error Message Reference.md`
  - `Manuals/Altibase_7.1/kor/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_7.1/kor/SQL Reference.md`
  - `Manuals/Altibase_7.3/kor/Error Message Reference.md`
  - `Manuals/Altibase_7.3/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_7.3/kor/SQL Reference.md`
  - `Manuals/Altibase_trunk/kor/Error Message Reference.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_trunk/kor/SQL Reference.md`

### 08_performance_tuning_monitoring.md

Source purpose: execution plans, optimizer behavior, indexes, joins, monitoring APIs, SNMP.

- 7.1:
  - `Manuals/Altibase_7.1/eng/Performance Tuning Guide.md`
  - `Manuals/Altibase_7.1/eng/Stored Procedures Manual.md`
  - `Manuals/Altibase_7.1/eng/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_7.1/eng/Monitoring API Developer's Guide.md`
  - `Manuals/Altibase_7.1/eng/SNMP Agent Guide.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/Performance Tuning Guide.md`
  - `Manuals/Altibase_7.3/eng/Stored Procedures Manual.md`
  - `Manuals/Altibase_7.3/eng/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_7.3/eng/Monitoring API Developer's Guide.md`
  - `Manuals/Altibase_7.3/eng/SNMP Agent Guide.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/Performance Tuning Guide.md`
  - `Manuals/Altibase_trunk/eng/Stored Procedures Manual.md`
  - `Manuals/Altibase_trunk/eng/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_trunk/eng/Monitoring API Developer's Guide.md`
  - `Manuals/Altibase_trunk/eng/SNMP Agent Guide.md`
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`
- Korean source authority/check:
  - `Manuals/Altibase_7.1/kor/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_7.1/kor/Monitoring API Developer's Guide.md`
  - `Manuals/Altibase_7.1/kor/SNMP Agent Guide.md`
  - `Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_7.3/kor/Monitoring API Developer's Guide.md`
  - `Manuals/Altibase_7.3/kor/SNMP Agent Guide.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_trunk/kor/Monitoring API Developer's Guide.md`
  - `Manuals/Altibase_trunk/kor/SNMP Agent Guide.md`

### 09_replication_ha_cdc.md

Source purpose: replication, HA, CDC/log analysis, compatibility, network checks, replication SSL.

- 7.1:
  - `Manuals/Altibase_7.1/eng/Replication Manual.md`
  - `Manuals/Altibase_7.1/eng/Log Analyzer User's Manual.md`
  - `Manuals/Tools/Altibase_release/eng/Replication Manager User's Manual.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/Replication Manual.md`
  - `Manuals/Altibase_7.3/eng/Log Analyzer User's Manual.md`
  - `Manuals/Tools/Altibase_release/eng/Replication Manager User's Manual.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/Replication Manual.md`
  - `Manuals/Altibase_trunk/eng/Log Analyzer User's Manual.md`
  - `Manuals/Tools/Altibase_trunk/eng/Replication Manager User's Manual.md`
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`
- Korean source authority/check:
  - `Manuals/Altibase_7.1/kor/SQL Reference.md`
  - `Manuals/Altibase_7.1/kor/Replication Manual.md`
  - `Manuals/Altibase_7.1/kor/Log Analyzer User's Manual.md`
  - `PatchNotes/Altibase_7.1/kor/Altibase_7_1_0_8_5_Patch_Notes.md`
  - `Manuals/Altibase_7.3/kor/SQL Reference.md`
  - `Manuals/Altibase_7.3/kor/Replication Manual.md`
  - `Manuals/Altibase_7.3/kor/Log Analyzer User's Manual.md`
  - `Manuals/Altibase_trunk/kor/SQL Reference.md`
  - `Manuals/Altibase_trunk/kor/Replication Manual.md`
  - `Manuals/Altibase_trunk/kor/Log Analyzer User's Manual.md`
- Korean supplemental technical documents:
  - `Technical Documents/kor/ReplicationCompatibility.md`
  - `Technical Documents/kor/Replication network check.md`

### 10_psm_stored_external_procedures.md

Source purpose: PSM, stored procedures/functions, external procedures, PL/SQL compatibility notes.

- 7.1:
  - `Manuals/Altibase_7.1/eng/Stored Procedures Manual.md`
  - `Manuals/Altibase_7.1/eng/External Procedures Manual.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/Stored Procedures Manual.md`
  - `Manuals/Altibase_7.3/eng/External Procedures Manual.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/Stored Procedures Manual.md`
  - `Manuals/Altibase_trunk/eng/External Procedures Manual.md`

### 11_java_jdbc_spring.md

Source purpose: JDBC, Adapter for JDBC, Java compatibility, Spring Data JPA, Hibernate.

- 7.1:
  - `Manuals/Altibase_7.1/eng/JDBC User's Manual.md`
  - `Manuals/Altibase_7.1/eng/Adapter for JDBC User's Manual.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/JDBC User's Manual.md`
  - `Manuals/Altibase_7.3/eng/Adapter for JDBC User's Manual.md`
  - `3rd Party Guide for Altibase/eng/Spring Data JPA User's Guide for Altibase.md`
  - `3rd Party Guide for Altibase/eng/Spring Data JPA With Hibernate 6.4 User's Guide for Altibase.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/JDBC User's Manual.md`
  - `Manuals/Altibase_trunk/eng/Adapter for JDBC User's Manual.md`
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`
  - `3rd Party Guide for Altibase/eng/Spring Data JPA User's Guide for Altibase.md`
  - `3rd Party Guide for Altibase/eng/Spring Data JPA With Hibernate 6.4 User's Guide for Altibase.md`
- Korean supplemental technical documents:
  - `Technical Documents/kor/JavaCompatibility.md`

### 12_c_cli_odbc_precompiler.md

Source purpose: C client interfaces, CLI, ODBC, C Interface, Precompiler, LOB API guidance.

- 7.1:
  - `Manuals/Altibase_7.1/eng/CLI User's Manual.md`
  - `Manuals/Altibase_7.1/eng/ODBC User's Manual.md`
  - `Manuals/Altibase_7.1/eng/Altibase C Interface Manual.md`
  - `Manuals/Altibase_7.1/eng/Precompiler User’s Manual.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/CLI User's Manual.md`
  - `Manuals/Altibase_7.3/eng/ODBC User's Manual.md`
  - `Manuals/Altibase_7.3/eng/Altibase C Interface Manual.md`
  - `Manuals/Altibase_7.3/eng/Precompiler User's Manual.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/CLI User's Manual.md`
  - `Manuals/Altibase_trunk/eng/ODBC User's Manual.md`
  - `Manuals/Altibase_trunk/eng/Altibase C Interface Manual.md`
  - `Manuals/Altibase_trunk/eng/Precompiler User's Manual.md`
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`

### 13_isql_iloader_basic_tools.md

Source purpose: iSQL, iLoader, export/import, first-line operational tool usage.

- 7.1:
  - `Manuals/Altibase_7.1/eng/iSQL User's Manual.md`
  - `Manuals/Altibase_7.1/eng/iLoader User's Manual.md`
  - `Manuals/Altibase_7.1/kor/iLoader User's Manual.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/iSQL User's Manual.md`
  - `Manuals/Altibase_7.3/eng/iLoader User's Manual.md`
  - `Manuals/Altibase_7.3/kor/iLoader User's Manual.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/iSQL User's Manual.md`
  - `Manuals/Altibase_trunk/eng/iLoader User's Manual.md`
  - `Manuals/Altibase_trunk/kor/iLoader User's Manual.md`
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`

### 14_utilities_operation_tools.md

Source purpose: utilities, `aexport`, `altiComp`, `iloader`, `isql`, `aku`, `altiMon`, `dataCompJ`.

- 7.1:
  - `Manuals/Altibase_7.1/eng/Utilities Manual.md`
  - `Manuals/Tools/Altibase_release/eng/dataCompJ User's Manual.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/Utilities Manual.md`
  - `Manuals/Tools/Altibase_release/eng/dataCompJ User's Manual.md`
  - `ReleaseNotes/eng/Altibase_dataCompJ_7_2_Release_Notes.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/Utilities Manual.md`
  - `Manuals/Tools/Altibase_trunk/eng/dataCompJ User's Manual.md`

### 15_migration_oracle_compatibility.md

Source purpose: Migration Center, Adapter for Oracle, Oracle-to-Altibase conversion guidance.

- 7.1:
  - `Manuals/Altibase_7.1/eng/Adapter for Oracle User's Manual.md`
  - `Manuals/Tools/Altibase_release/eng/Migration Center User's Manual.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/Adapter for Oracle User's Manual.md`
  - `Manuals/Tools/Altibase_release/eng/Migration Center User's Manual.md`
  - `ReleaseNotes/eng/Altibase_Migration_Center_7_19_Release_Notes.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/Adapter for Oracle User's Manual.md`
  - `Manuals/Tools/Altibase_trunk/eng/Migration Center User's Manual.md`
  - `ReleaseNotes/eng/Altibase_Migration_Center_7_19_Release_Notes.md`
- Korean source authority/check:
  - `Manuals/Altibase_7.1/kor/Adapter for Oracle User's Manual.md`
  - `Manuals/Altibase_7.3/kor/Adapter for Oracle User's Manual.md`
  - `Manuals/Altibase_trunk/kor/Adapter for Oracle User's Manual.md`
  - `Manuals/Tools/Altibase_release/kor/Migration Center User's Manual.md`
  - `Manuals/Tools/Altibase_trunk/kor/Migration Center User's Manual.md`
  - `ReleaseNotes/kor/Altibase_Migration_Center_7_19_Release_Notes.md`

### 16_dblink_external_connectors.md

Source purpose: DB Link, Hadoop Connector, third-party connector setup and procedures.

- 7.1:
  - `Manuals/Altibase_7.1/eng/DB Link User's Manual.md`
  - `Manuals/Altibase_7.1/eng/Hadoop Connector User's Manual.md`
  - `Manuals/Tools/Altibase_release/kor/Altibase 3rd Party Connector Guide.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/DB Link User's Manual.md`
  - `Manuals/Altibase_7.3/eng/Hadoop Connector User's Manual.md`
  - `Manuals/Tools/Altibase_release/eng/Altibase 3rd Party Connector Guide.md`
  - `Manuals/Tools/Altibase_release/kor/Altibase 3rd Party Connector Guide.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/DB Link User's Manual.md`
  - `Manuals/Altibase_trunk/eng/Hadoop Connector User's Manual.md`
  - `Manuals/Tools/Altibase_trunk/eng/Altibase 3rd Party Connector Guide.md`
  - `Manuals/Tools/Altibase_trunk/kor/Altibase 3rd Party Connector Guide.md`

### 17_kubernetes_aku_cloud.md

Source purpose: Kubernetes deployment, AKU samples, container operations, release-note context.

- 7.1:
  - `Manuals/Altibase_7.1/eng/Installation Guide.md`
  - `Manuals/Altibase_7.1/eng/Administrator's Manual.md`
  - `Manuals/Altibase_7.1/eng/Replication Manual.md`
  - `Manuals/Altibase_7.1/eng/Utilities Manual.md`
  - `3rd Party Guide for Altibase/eng/Altibase aku Sample Guide for Kubernetes.md`
- 7.3:
  - `3rd Party Guide for Altibase/eng/Kubernetes User's Guide for Altibase.md`
  - `3rd Party Guide for Altibase/eng/Altibase aku Sample Guide for Kubernetes.md`
  - `ReleaseNotes/eng/Altibase_7_3_0_0_1_Release_Notes.md`
- Altibase 8.1 verified source:
  - `3rd Party Guide for Altibase/eng/Kubernetes User's Guide for Altibase.md`
  - `3rd Party Guide for Altibase/eng/Altibase aku Sample Guide for Kubernetes.md`
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`

### 18_security_ssl_tls.md

Source purpose: SSL/TLS server/client setup, certificate configuration, replication SSL.

- 7.1:
  - `Manuals/Altibase_7.1/eng/Altibase SSL TLS User's Guide.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/Altibase SSL TLS User's Guide.md`
  - `ReleaseNotes/eng/Altibase_7_3_0_0_1_Release_Notes.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/Altibase SSL TLS User's Guide.md`
  - `Manuals/Altibase_trunk/eng/Replication Manual.md`
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`

### 19_spatial_nifi_tableau_misc.md

Source purpose: Spatial SQL, `GEOMETRY`, altiShapeLoader, NiFi, Tableau.

- 7.1:
  - `Manuals/Altibase_7.1/eng/Spatial SQL Reference.md`
  - `Manuals/Tools/Altibase_release/eng/altiShapeLoader User's Manual.md`
- 7.3:
  - `Manuals/Altibase_7.3/eng/Spatial SQL Reference.md`
  - `Manuals/Tools/Altibase_release/eng/altiShapeLoader User's Manual.md`
  - `3rd Party Guide for Altibase/eng/NiFi User's Guide for Altibase.md`
  - `3rd Party Guide for Altibase/eng/Tableau User's Guide for Altibase/Tableau User's Guide for Altibase.md`
  - `ReleaseNotes/eng/Altibase_altiShapeLoader_1_0_Release_Notes.md`
- Altibase 8.1 verified source:
  - `Manuals/Altibase_trunk/eng/Spatial SQL Reference.md`
  - `Manuals/Tools/Altibase_trunk/eng/altiShapeLoader User's Manual.md`
  - `3rd Party Guide for Altibase/eng/NiFi User's Guide for Altibase.md`
  - `3rd Party Guide for Altibase/eng/Tableau User's Guide for Altibase/Tableau User's Guide for Altibase.md`

## Follow-Up Notes

- JOB-011 should verify the 8.1-specific source claims against `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`, especially JSON, Temporary LOB, replication SSL, JSON plan output, new properties, and new performance views.
- JOB-012 records that Korean manuals are authoritative when English and Korean manuals differ; later jobs should check Korean manuals for version-sensitive claims and record any English-source drift.
- JOB-013 and JOB-014 should start from the manuals listed here, especially SQL Reference, Performance Tuning Guide, Replication Manual, Installation Guide, Administrator manual, and the third-party UI-heavy guides.
