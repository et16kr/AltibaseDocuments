# Altibase GPTs Knowledge Document Selection

## Objective

Build the attachment knowledge set so an Altibase GPT can answer customer questions
according to the customer's Altibase version: 7.1, 7.3, or 8.1.

Customer questions are expected to focus on SQL generation, DDL authoring, server
configuration, operational check SQL, replication, and error handling. Keep generic
Oracle-overlapping SQL content brief, and give more depth to Altibase-specific DDL,
configuration, operation, and troubleshooting behavior.

## Version Policy

| Customer version | Internal source | Customer-facing label |
| --- | --- | --- |
| 7.1 | `Manuals/Altibase_7.1` | Altibase 7.1 |
| 7.3 | `Manuals/Altibase_7.3` | Altibase 7.3 |
| 8.1 | `Manuals/Altibase_trunk` + `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md` | Altibase 8.1 verified source |

Rules:

- Do not leave internal source labels such as `trunk` in customer-facing attachment files.
- Use the 8.1 source set internally only after checking it against the 8.1 release notes
  for JSON, Temporary LOB, replication SSL, JSON plan, new properties, and performance
  views.
- Exclude `7.8` from the default target versions because it is not one of the current
  local product manual baseline versions. If a tool release note, such as Migration
  Center, mentions that version, treat it only as supplemental context for that tool.

## Selection Criteria

1. High-frequency customer question areas.
2. Altibase-specific information that ChatGPT could otherwise infer incorrectly from
   general database knowledge.
3. Differences across Altibase 7.1, 7.3, and 8.1.
4. Operational troubleshooting information needed for real support cases.
5. Content that can be reorganized into Markdown for GPTs knowledge retrieval.

## Final Recommendation: 20 Attachment Files

These 20 files are the final upload units for GPTs. Do not upload original manuals
directly. Combine source material by customer question topic.

| No. | Attachment file | Customer question scope | Main source family |
| --- | --- | --- | --- |
| 00 | `00_version_release_platform.md` | 7.1/7.3/8.1 releases, supported platforms, upgrade cautions | Release Notes, Supported Platforms |
| 01 | `01_getting_started_installation.md` | Installation, database creation, startup/shutdown, basic environment | Getting Started, Installation |
| 02 | `02_administration_operations.md` | Administration, accounts, backup/recovery, tablespaces | Administrator's Manual |
| 03 | `03_sql_ddl_generation.md` | DDL, DCL, and configuration SQL for GPT SQL generation | SQL Reference, General Reference |
| 04 | `04_sql_dml_oracle_compatibility.md` | Oracle-compatible SQL, DML, function differences | SQL Reference |
| 05 | `05_data_types_properties.md` | Data types, properties, JSON, Temporary LOB | General Reference 1 |
| 06 | `06_data_dictionary_performance_views.md` | Meta tables, performance views, check SQL | General Reference 2 |
| 07 | `07_error_messages_troubleshooting.md` | Error codes, causes, actions, check commands | Error Message Reference |
| 08 | `08_performance_tuning_monitoring.md` | Execution plans, indexes, joins, monitoring | Performance Tuning, Monitoring API, SNMP |
| 09 | `09_replication_ha_cdc.md` | Replication, HA, XLog/Log Analyzer, compatibility | Replication, Log Analyzer, ReplicationCompatibility |
| 10 | `10_psm_stored_external_procedures.md` | PSM, functions, procedures, external procedures | Stored Procedures, External Procedures |
| 11 | `11_java_jdbc_spring.md` | JDBC, Java compatibility, Spring/Hibernate | JDBC, Adapter for JDBC, JavaCompatibility, Spring guides |
| 12 | `12_c_cli_odbc_precompiler.md` | CLI, ODBC, C Interface, Precompiler | CLI, ODBC, C Interface, Precompiler |
| 13 | `13_isql_iloader_basic_tools.md` | iSQL, iLoader, data load/extract | iSQL, iLoader |
| 14 | `14_utilities_operation_tools.md` | aexport, altiComp, aku, altiMon, dataCompJ | Utilities, dataCompJ |
| 15 | `15_migration_oracle_compatibility.md` | Migration Center, Oracle Adapter, conversion guidance | Migration Center, Adapter for Oracle |
| 16 | `16_dblink_external_connectors.md` | DB Link, Hadoop, DBeaver, GoldenGate, and related connectors | DB Link, Hadoop, 3rd Party Connector |
| 17 | `17_kubernetes_aku_cloud.md` | Kubernetes, AKU, container operation | Kubernetes guides, AKU sample, 7.3 release AKU notes |
| 18 | `18_security_ssl_tls.md` | SSL/TLS, certificates, encrypted connections | SSL/TLS User's Guide |
| 19 | `19_spatial_nifi_tableau_misc.md` | Spatial SQL, altiShapeLoader, NiFi, Tableau | Spatial SQL, altiShapeLoader, NiFi, Tableau |

## SQL Generation Compression Strategy

`03_sql_ddl_generation.md` is the central file for customer SQL generation requests.
Do not merely summarize the full SQL Reference. Rewrite it according to these rules.

| Area | Treatment |
| --- | --- |
| `SELECT`, `INSERT`, `UPDATE`, `DELETE`, basic `JOIN`, basic predicates | Treat as Oracle-compatible territory and keep only key Altibase differences or limits. Mark the detailed syntax as similar to Oracle SQL. |
| `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`, constraints, partitioning, LOB, QUEUE | Keep detail because Altibase DDL differences matter. Include SQL examples. |
| `CREATE INDEX`, index attributes, hints, execution plan SQL | Keep detail because this connects to tuning questions. |
| `CREATE/ALTER/DROP TABLESPACE`, datafiles, memory/disk storage structure | Keep detail because these are core Altibase operational DDL areas. |
| `CREATE USER`, privileges, role, synonym, view, sequence | Summarize Oracle-like parts and prioritize Altibase syntax differences and examples. |
| Replication SQL | Treat as Altibase-specific and cross-reference `09_replication_ha_cdc.md`. |
| Property and system-configuration SQL | Provide representative query/change SQL and cross-reference `05` and `06`. |
| Built-in functions, analytic functions, general expressions | Compress Oracle-equivalent material and keep Altibase-specific functions, restrictions, and data type differences. |

Use this structure for each DDL item.

```text
Example customer questions:
- Create DDL for a memory table.

Applicable versions:
- Common:
- 7.1:
- 7.3:
- 8.1:

Oracle compatibility:
- Similar to Oracle:
- Different in Altibase:

Altibase syntax essentials:
- Required clauses:
- Optional clauses:
- Important restrictions:

Examples:
- Minimal example
- Operational example
- Verification SQL
```

## Conversion Priority

1. `03_sql_ddl_generation.md`
2. `05_data_types_properties.md`
3. `06_data_dictionary_performance_views.md`
4. `02_administration_operations.md`
5. `09_replication_ha_cdc.md`
6. `08_performance_tuning_monitoring.md`
7. `07_error_messages_troubleshooting.md`
8. `01_getting_started_installation.md`

## Recommended Working Method

- Preserve original source manuals. Create upload-ready Markdown under `GPTs/attachments/`.
- Do not leave internal source labels such as `trunk` in customer-facing attachment files.
- Use the verified 8.1 source set internally, but label it in customer-facing attachments as
  `Altibase 8.1 verified source`.
- Convert image-based SQL syntax diagrams to compact BNF-like text or simple Mermaid.
- Convert graph, flow, state, architecture, topology, and sequence images to Mermaid when
  the diagram adds useful structure.
- Replace UI screenshots with procedural text and input/value descriptions.
- Decompose large tables into searchable item blocks instead of preserving them as large
  Markdown tables.
- Place a `Questions This File Can Answer` section near the beginning of each attachment.
- Write attachment files in canonical English so the GPT can answer in any user language
  while preserving literal SQL object names, function names, error codes, property names,
  commands, and file paths.
