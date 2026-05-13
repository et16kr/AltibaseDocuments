# Altibase GPTs Attachments

This directory contains customer-facing Markdown knowledge files for Altibase GPTs.
The files are the canonical English source used by the GPT to answer customer questions
about Altibase 7.1, 7.3, and 8.1.

## Core Rules

- Keep exactly 20 attachment Markdown files, excluding this `README.md`.
- Write every attachment in canonical English.
- Treat canonical English as the source language for the knowledge files. The GPT may
  translate explanations at answer time, but the attachment text itself should stay English.
- Support Altibase 7.1, 7.3, and 8.1 answers.
- Label Altibase 8.1 material as based on the `Altibase 8.1 verified source`.
- Prioritize Altibase-specific DDL, configuration, operation, compatibility, and troubleshooting behavior.
- Keep common SQL behavior that overlaps with Oracle brief unless Altibase differs.
- Convert tables and images into searchable Markdown text whenever possible.
- Keep customer-facing source references concise and safe: use product, manual, version, and topic names only.
- Do not expose internal repository names, branch names, workstation paths, or local build labels.

## Multilingual Answer Policy

The GPT should answer in the user's language whenever possible. Keep the following items
literal and untranslated in every language:

- SQL object names
- SQL keywords when used as syntax
- Function names
- Error codes
- Property names
- Commands and command options
- File and directory paths
- Package, class, method, API, and connector names
- Altibase version numbers and edition names

When translating explanatory text, preserve the exact spelling and casing of literal
technical tokens. If a translated sentence would make a command, property, or SQL
syntax ambiguous, keep that portion in English and explain it in the user's language.

## File List

1. `00_version_release_platform.md`
2. `01_getting_started_installation.md`
3. `02_administration_operations.md`
4. `03_sql_ddl_generation.md`
5. `04_sql_dml_oracle_compatibility.md`
6. `05_data_types_properties.md`
7. `06_data_dictionary_performance_views.md`
8. `07_error_messages_troubleshooting.md`
9. `08_performance_tuning_monitoring.md`
10. `09_replication_ha_cdc.md`
11. `10_psm_stored_external_procedures.md`
12. `11_java_jdbc_spring.md`
13. `12_c_cli_odbc_precompiler.md`
14. `13_isql_iloader_basic_tools.md`
15. `14_utilities_operation_tools.md`
16. `15_migration_oracle_compatibility.md`
17. `16_dblink_external_connectors.md`
18. `17_kubernetes_aku_cloud.md`
19. `18_security_ssl_tls.md`
20. `19_spatial_nifi_tableau_misc.md`

## Attachment Structure

Until final cleanup, each attachment should keep these sections:

- `Applicable Versions`
- `Source Documents`
- `Questions This File Can Answer`
- `Core Guidance`
- `Version Differences`
- `Conversion TODO`

Use compact, searchable item blocks for large reference tables. Use BNF-like text for
SQL syntax diagrams. Use Mermaid only when it helps explain graphs, flows, states,
architecture, topology, or sequences. Replace UI screenshots with procedural text and
clear input or value descriptions.

## Source Traceability Policy

Customer-facing attachments may cite source material only with safe labels such as
Altibase version, manual family, release note, or topic. Keep internal paths and branch
names in work documents only. For Altibase 8.1, use `Altibase 8.1 verified source` or
equivalent wording instead of any internal source-set name.

## Pre-Upload Checks

- Confirm that exactly 20 Markdown attachment files exist, excluding `README.md`.
- Confirm that each attachment is English canonical and ready for multilingual answers.
- Confirm that version coverage and version differences are explicit.
- Confirm that customer-facing source references are safe and concise.
- Confirm that no internal repository labels, local paths, or non-customer source names remain.
