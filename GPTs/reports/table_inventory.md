# Altibase GPTs Table Inventory

Job: `JOB-014`
Phase: P1 Inventory
Status: Complete

Objective: list large source tables that require decomposition into searchable item blocks during attachment build jobs.

## Scope and Method

- Source list: `GPTs/reports/source_inventory.md`
- Selected Markdown source documents scanned: 114
- Missing selected source documents: 0
- Markdown pipe-table blocks found: 3662
- Large table candidates found: 438
- Candidates requiring decomposition: 339
- Repeated documentation-convention tables to omit or summarize once: 86
- Korean supplemental fallback-only candidates: 13

Candidate thresholds:

| Priority | Rule | Build expectation |
| --- | --- | --- |
| P0 | 60 or more rows, 12 or more columns, or 300 or more cells | Decompose first. These tables are too large for direct attachment use. |
| P1 | 30 or more rows, 8 or more columns, or 160 or more cells | Decompose when retained in the target attachment. |
| P2 | 15 or more rows, or 75 or more cells | Decompose or compact into grouped item blocks based on attachment scope. |

Counts include repeated 7.1, 7.3, and Altibase 8.1 verified source copies when the same logical table appears in multiple versions. Attachment jobs should use the Altibase 8.1 verified source as the base when the table is equivalent, then record only material 7.1 and 7.3 differences.

## Top Priority Tables

These are the highest-impact table groups. They should be converted before lower-priority tables because they are likely to answer direct customer questions and are difficult to search in wide or long Markdown form.

| Priority | Target attachment | Table group | Representative source trace | Decomposition action |
| --- | --- | --- | --- | --- |
| P0 | `06_data_dictionary_performance_views.md` | Performance view catalog, including `V$Views` list, `V$STATNAME` statistic identifiers, `V$MEMSTAT` module names, and the `V$SESSION` column table. | `General Reference-2.The Data Dictionary.md`: `V$Views` 129x2, `V$STATNAME` 133x3, `V$MEMSTAT` 119x2, `V$SESSION` 60x3 | Create one block per view, statistic, module, or column. Include fields such as `Object`, `Column`, `Type`, `Meaning`, and `When to query`. |
| P0 | `06_data_dictionary_performance_views.md` | Meta table catalog and large view column tables such as `V$STATEMENT`, `V$TRANSACTION`, `V$BUFFPOOL_STAT`, and `V$INTERNAL_SESSION`. | `General Reference-2.The Data Dictionary.md`: meta table types 72x2; large P1/P2 column tables across the same source | Use one block per meta table or performance view, followed by one searchable column block for large schemas. |
| P0 | `03_sql_ddl_generation.md`, `04_sql_dml_oracle_compatibility.md` | System privilege reference and object privilege matrix. | `SQL Reference.md`: system privileges 69x4; object privileges 11x8 | Create privilege blocks keyed by privilege name. Preserve `PrivID`, privilege category, purpose, and grant notes. |
| P0 | `03_sql_ddl_generation.md`, `04_sql_dml_oracle_compatibility.md`, `05_data_types_properties.md` | Data type conversion and column modification matrices. | `SQL Reference.md`: `ALTER TABLE` modification matrix 21x21; `General Reference-1.Data Types & Altibase Properties.md`: data type conversion 23x23 | Replace wide matrices with source-type item blocks listing allowed target types and data-loss requirements. Preserve the `O` and `△` legend. |
| P0 | `11_java_jdbc_spring.md` | JDBC SQL state table and JDBC type conversion matrices. | `JDBC User's Manual.md`: `SQL States` 100x4; Java-to-database 24x18; database-to-Java 22x18 | Create searchable blocks by SQL state class/subclass and by Java or Altibase data type. |
| P1 | `11_java_jdbc_spring.md` | JDBC API support tables, especially `java.sql.ResultSet`, `java.sql.CallableStatement`, and JDBC data type mapping. | `JDBC User's Manual.md`: `ResultSet` 49x5; `CallableStatement` 43x5; data type mapping 31x3 | Create method-level support blocks with `Supported`, `Exception`, and notes fields. |
| P0 | `12_c_cli_odbc_precompiler.md` | CLI SQL/C data type conversion matrices. | `CLI User's Manual.md`: SQL-to-C 24x20; C-to-SQL 20x19 | Convert each SQL or C type into a block listing compatible target types and limitations. |
| P1 | `12_c_cli_odbc_precompiler.md` | ODBC conformance table. | `ODBC User's Manual.md`: ODBC conformance 59x5 | Create one block per ODBC function with level, support status, future support, and remarks. |
| P0 | `15_migration_oracle_compatibility.md` | Migration Center character set and heterogeneous type mapping tables. | `Migration Center User's Manual.md`: Oracle character sets 166x2; PostgreSQL type mapping 39x4; MySQL type mapping 34x4; PostgreSQL character sets 43x2; Tibero character sets 34x2 | Create item blocks by source DB and source type or character set. Keep source and destination data types literal. |
| P0 | `09_replication_ha_cdc.md` | Log Analyzer ODBC C value conversion matrix. | `Log Analyzer User's Manual.md`: `ALA_GetODBCCValue` 17x12 | Decompose by Altibase data type, listing valid ODBC C target values. |
| P1 | `09_replication_ha_cdc.md` | Log Analyzer error code table. | `Log Analyzer User's Manual.md`: `INFO Error` 34x3 | Convert to error-code blocks with description and API-return context. |
| P0 | `08_performance_tuning_monitoring.md` | Optimizer index/data type matrix. | `Performance Tuning Guide.md`: `Indexes and Data Types` 15x15 | Convert to data type blocks listing index compatibility. |
| P1 | `08_performance_tuning_monitoring.md` | Monitoring API data structures mapped to performance views. | `Monitoring API Developer's Guide.md`: `ABIVSession` 41x3 | Create structure-member blocks and cross-reference corresponding `V$SESSION` columns. |
| P1 | `16_dblink_external_connectors.md` | Database Link supported data types. | `DB Link User's Manual.md`: supported data types 38x5 | Create one block per JDBC data type with Altibase SQL type, standard SQL type, support status, and comments. |
| P1 | `13_isql_iloader_basic_tools.md`, `14_utilities_operation_tools.md` | Tool option and output field tables. | `iLoader User's Manual.md`: general options 32-34x6; `Utilities Manual.md`: `altiAudit` output and statement fields 30-38 rows | Create command-option blocks and output-field blocks by tool and command section. |
| P1 | `00_version_release_platform.md` | Supported platform matrices. | `Technical Documents/eng/Supported Platforms.md`: server/client and library/tool tables up to 28x5 and 24x7 | Convert into version/OS support blocks. Use English source as canonical; Korean table is fallback only. |

## Attachment-Level Decomposition Load

The following counts exclude repeated documentation-convention tables and Korean supplemental fallback-only tables. Version-duplicate source blocks are still counted because later attachment jobs must check version drift.

| Attachment | P0 | P1 | P2 | Primary table families |
| --- | ---: | ---: | ---: | --- |
| `00_version_release_platform.md` | 0 | 1 | 5 | Supported platform matrices |
| `01_getting_started_installation.md` | 0 | 0 | 1 | Startup and first-use reference tables |
| `02_administration_operations.md` | 0 | 0 | 6 | Administration state and backup/recovery reference tables |
| `03_sql_ddl_generation.md` | 9 | 6 | 9 | Privileges, DDL statement lists, table/data type matrices |
| `04_sql_dml_oracle_compatibility.md` | 6 | 6 | 9 | SQL reference lists and compatibility matrices |
| `05_data_types_properties.md` | 3 | 0 | 0 | Data type conversion matrix |
| `06_data_dictionary_performance_views.md` | 15 | 15 | 90 | Data dictionary catalogs and performance view schemas |
| `07_error_messages_troubleshooting.md` | 0 | 0 | 0 | No large decomposition target found in selected source |
| `08_performance_tuning_monitoring.md` | 3 | 3 | 3 | Optimizer matrices, monitoring structures |
| `09_replication_ha_cdc.md` | 3 | 3 | 0 | Log Analyzer conversion and error code tables |
| `10_psm_stored_external_procedures.md` | 0 | 0 | 12 | PSM package and procedure/function lists |
| `11_java_jdbc_spring.md` | 9 | 9 | 9 | SQL states, JDBC API support, Java/database type matrices |
| `12_c_cli_odbc_precompiler.md` | 6 | 3 | 39 | CLI/ODBC/Precompiler conversion and descriptor tables |
| `13_isql_iloader_basic_tools.md` | 0 | 3 | 0 | `iLoader` option tables |
| `14_utilities_operation_tools.md` | 0 | 6 | 27 | Utility output and audit field tables |
| `15_migration_oracle_compatibility.md` | 2 | 8 | 25 | Migration type mappings and character set mappings |
| `16_dblink_external_connectors.md` | 0 | 3 | 3 | DB Link data type support |
| `17_kubernetes_aku_cloud.md` | 0 | 0 | 3 | Small operational reference tables |
| `18_security_ssl_tls.md` | 0 | 0 | 0 | Only repeated convention tables matched the large-table threshold |
| `19_spatial_nifi_tableau_misc.md` | 0 | 3 | 0 | Spatial subtype and tool reference tables |

## Decomposition Rules For Later Jobs

- Do not keep P0/P1 matrices as wide Markdown tables in final attachments. Convert them to item blocks keyed by the item users will search for, such as data type, privilege, view, column, function, character set, or error code.
- For data dictionary and performance view schemas, use a parent object block followed by column blocks. Example fields: `Object`, `Column`, `Type`, `Description`, `Version notes`, `Useful query`.
- For compatibility matrices, invert the matrix. Use one block per source type and list compatible target types. Keep legends such as `O`, `△`, `Supported`, and `Unsupported` explicit.
- For API support tables, create one block per method or function. Include support status and exception or limitation notes.
- For migration mappings, group by source database first, then by source type or source character set.
- Repeated `Documentation Conventions` and `Sample Code Conventions` tables should be omitted from customer-facing attachments or summarized once in shared attachment policy, not decomposed in every attachment.
- Korean-only supplemental tables should not override English canonical content. Use them only as fallback when no English source contains the same information.

## Highest-Risk Attachment Order

1. `06_data_dictionary_performance_views.md`
2. `11_java_jdbc_spring.md`
3. `12_c_cli_odbc_precompiler.md`
4. `03_sql_ddl_generation.md`
5. `04_sql_dml_oracle_compatibility.md`
6. `15_migration_oracle_compatibility.md`
7. `08_performance_tuning_monitoring.md`
8. `09_replication_ha_cdc.md`

These attachments contain the largest concentration of P0/P1 tables and should receive explicit decomposition checks during their build jobs.
