# Altibase GPT Coverage Matrix

Job: `J002`
Status: Active support artifact
Last updated: 2026-05-16

## Reconfirmed Requirement And Boundary

`J002` maps the selected repository-local source families to the 20 GPT upload
attachments and creates the primary item-level gap tracking handoff for later rebuild
jobs. It is a documentation-scope job: it does not rewrite the customer-facing
attachments unless the source-scope map proves an attachment boundary or source label
must change.

No attachment boundary or customer-facing source-label change was found in this job.
Keep exactly the existing 20 upload Markdown files under `GPTs/attachments/`, excluding
`README.md`.

Use this report together with:

- `GPTs/reports/source_inventory.md`: source roots and attachment-to-source path
  inventory.
- `GPTs/reports/gap_register.md`: item-level gaps, residual source limits, and later
  remediation queue.
- `GPTs/reports/catalog_schema_extraction_rules.md`: reusable item block schemas and
  Korean-first extraction rules for later jobs.
- `GPTs/reports/property_inventory.md`: post-J004 General Reference 1 property-name
  and version-availability baseline for J005-J009 property expansion.
- `GPTs/reports/sql_syntax_inventory.md`: post-J010 SQL statement-family inventory,
  BNF-like conversion rules, and J011-J016 SQL expansion queue.
- `.codex-jobs/altibase-gpt-encyclopedia-rebuild/requirements.md`: rebuild contract,
  source policy, and success criteria.

## Design Note

`J002` adds two support reports under `GPTs/reports/`:

- `coverage_matrix.md`: source-family IDs, attachment ownership, and expected coverage
  shapes.
- `gap_register.md`: primary post-J002 register for manual/source-backed gaps and
  accepted source limitations.
- `catalog_schema_extraction_rules.md`: reusable post-J003 schema for item blocks,
  BNF-like syntax, runbooks, examples, cross-references, validation notes, and
  Korean-first extraction.

Later jobs should update `gap_register.md` when they discover, split, close, or accept a
gap. Keep concrete source paths and internal labels in support reports only. Customer
attachments must remain English-normalized and must use `Altibase 8.1 verified source`
for 8.1 customer-facing labels.

## Source Policy For This Matrix

- Default supported answer scope: Altibase 7.1, 7.3, and 8.1.
- Korean manuals, release notes, patch notes, tool manuals, technical documents, and
  third-party guides are authoritative when paired Korean and English sources differ.
- English source trees are extraction aids when they agree with Korean sources.
- 7.1 and 7.3 claims require the corresponding selected sources before broadening.
- 8.1 claims use the verified source family and release-note checks already recorded in
  `GPTs/reports/8_1_verification.md`.
- If the selected sources do not establish an exact patch-level, customer-environment,
  log, object-definition, or compatibility claim, the attachment answer pattern must ask
  for the missing input and give the safest source-backed next check.

## Source Family Matrix

| Source family ID | Authoritative basis | Extraction basis | Primary attachments | Required coverage shape |
| --- | --- | --- | --- | --- |
| `release_notes_platform` | `ReleaseNotes/kor`, `Technical Documents/kor/Supported Platforms.md` | `ReleaseNotes/eng`, `Technical Documents/eng/Supported Platforms.md` | `00` | Version/platform difference blocks, release boundaries, upgrade cautions, 8.1 feature labels, patch-level cautions. |
| `patch_notes` | `PatchNotes/Altibase_7.1/kor`, `PatchNotes/Altibase_7.3/kor` | Matching 7.x English patch notes when present | `00`, `05`, `06`, `09` | Patch-specific item notes, exact patch boundary, affected feature/property/view, and safe answer caveat. |
| `getting_started_installation` | 7.1/7.3/8.1 Korean Getting Started and Installation manuals | Matching English manuals | `01` | Installation flow, database creation, startup/shutdown, environment variables, first-run checks. |
| `administrator_operations` | Korean Administrator manuals plus SQL Reference where administrative SQL is needed | Matching English manuals | `02`, `03` | Backup/recovery runbooks, tablespaces, accounts, privileges, storage, server modes, safety checks. |
| `sql_reference` | Korean SQL Reference manuals | Matching English SQL Reference manuals | `03`, `04`, `10`, `19` | BNF-like syntax, executable examples, Oracle-difference notes, verification SQL, version restrictions. |
| `general_reference_1_datatypes_properties` | Korean General Reference 1 manuals | Matching English General Reference 1 manuals | `05`, `03`, `04` | Data type and property item blocks with version, default, range, dynamic-change support, check SQL, cautions. |
| `general_reference_2_dictionary_views` | Korean General Reference 2 manuals | Matching English General Reference 2 manuals | `06`, `08`, `09` | Dictionary/performance view item blocks with purpose, key columns, query timing, sample check SQL. |
| `error_message_reference` | Korean Error Message Reference manuals | Matching English Error Message Reference manuals | `07` | Error code blocks with symbol, message, cause, action, version caution, and troubleshooting pattern. |
| `performance_tuning` | Korean Performance Tuning Guides | Matching English Performance Tuning Guides | `08`, `06` | Optimizer, hints, plans, indexes, joins, statistics, and source-limited JSON plan wording. |
| `monitoring_api_snmp` | Korean Monitoring API Developer's Guide and SNMP Agent Guide | Matching English manuals | `08`, `06` | API/SNMP item blocks with function/object, inputs, output, counters, ports, and runtime check pattern. |
| `replication_manual` | Korean Replication Manual and SQL Reference | Matching English manuals | `09`, `03`, `06`, `18` | Topology, modes, states, DDL, properties, restrictions, compatibility checks, and protected state changes. |
| `log_analyzer` | Korean Log Analyzer User's Manual | Matching English manual | `09` | CDC/XLog workflows, API order, collector inputs, ACK/restart behavior, and unsupported transport notes. |
| `replication_manager` | Korean Replication Manager manuals and release notes | Matching English manuals and release notes | `09`, `14` | Screenshot-free GUI task blocks, release/tool boundaries, JDBC driver import, high-risk action guardrails. |
| `security_ssl_tls` | Korean SSL/TLS guide, Korean Replication Manual, 8.1 Korean release notes | Matching English SSL/TLS guide and release notes | `18`, `09`, `11`, `12`, `13`, `14`, `16` | Client/server TLS setup, certificate fields, JDBC/CLI/tool placement, replication SSL separation. |
| `stored_external_procedures` | Korean Stored Procedures and External Procedures manuals | Matching English manuals | `10`, `04` | PSM/package/trigger/library syntax, external procedure setup, type mapping, compile/deploy cautions. |
| `jdbc_java` | Korean JDBC and Adapter for JDBC manuals; `Technical Documents/kor/JavaCompatibility.md` | English manuals and approved third-party guides | `11`, `16`, `17`, `19` | JDBC URLs, drivers, Java compatibility, Adapter behavior, Spring/Hibernate/NiFi/Tableau literal tokens. |
| `c_cli_odbc_precompiler` | Korean CLI, ODBC, C Interface, and Precompiler manuals | Matching English manuals | `12`, `13` | API function blocks, DSN/driver setup, LOB/JSON LOB handling, diagnostics, compile-readiness cautions. |
| `isql_iloader` | Korean iSQL and iLoader manuals | Matching English manuals | `13`, `14`, `19` | Command syntax, session commands, load/extract workflows, option checks, example control files. |
| `utilities_datacompj` | Korean Utilities and dataCompJ manuals; Korean utility release notes | Matching English manuals and release notes | `14`, `13`, `17` | Utility command blocks, options, output fields, runbook steps, patch/client-help caveats. |
| `migration_oracle` | Korean Migration Center and Adapter for Oracle manuals; Korean release notes | Matching English manuals and release notes | `15`, `04`, `19` | Conversion item blocks, unsupported objects, generated reports, PSM review, `oraAdapter`, validation workflow. |
| `dblink_hadoop_external_connectors` | Korean DB Link and Hadoop Connector manuals; Korean third-party connector guide | Matching English manuals and connector guide | `16`, `03`, `06`, `11` | DB Link syntax/views, linker/runtime checks, Hadoop, DBeaver, GoldenGate, connector setup boundaries. |
| `kubernetes_aku` | Korean Kubernetes and AKU guides; Korean release notes where present | Matching English guides and release notes | `17`, `14`, `09`, `18` | Container/Kubernetes runbooks, AKU samples, image/env values, replication/TLS operational cautions. |
| `spatial_nifi_tableau` | Korean Spatial SQL and altiShapeLoader manuals; Korean NiFi/Tableau guides when present | Matching English manuals and guides | `19`, `13`, `14`, `15` | Spatial type/function blocks, loader workflows, NiFi/Tableau JDBC settings, expected validation results. |
| `technical_documents_support` | `Technical Documents/kor` where paired, Korean-only, or more specific | `Technical Documents/eng` | `00`, `09`, `11`, `16`, `18` | Compatibility and diagnostic notes with exact scope, evidence path, and "ask for missing input" guardrails. |
| `third_party_guides` | `3rd Party Guide for Altibase/kor` when paired or more specific | `3rd Party Guide for Altibase/eng` | `11`, `16`, `17`, `19` | UI/procedure text, field/value lists, connector-specific settings, expected checks, screenshot replacement. |

## Attachment Coverage Matrix

| Attachment | Primary source families | Supporting source families | Required item-level coverage | Gap register anchors |
| --- | --- | --- | --- | --- |
| `00_version_release_platform.md` | `release_notes_platform`, `patch_notes` | `technical_documents_support` | Version and platform matrix, feature introduction notes, upgrade cautions, customer-safe 8.1 label. | `GAP-J002-001`, `GAP-J002-007` |
| `01_getting_started_installation.md` | `getting_started_installation` | `release_notes_platform`, `technical_documents_support` | Install prerequisites, environment setup, database creation, startup/shutdown, first checks. | `GAP-J002-007`, `GAP-J002-018` |
| `02_administration_operations.md` | `administrator_operations` | `sql_reference`, `general_reference_1_datatypes_properties`, `general_reference_2_dictionary_views` | Backup/recovery, archive log mode, tablespaces, users, privileges, server modes, destructive-operation guardrails. | `GAP-J002-003`, `GAP-J002-018` |
| `03_sql_ddl_generation.md` | `sql_reference`, `administrator_operations` | `general_reference_1_datatypes_properties`, `replication_manual`, `log_analyzer` | DDL/DCL/admin SQL, compact BNF, examples, verification SQL, 8.1 idempotent syntax boundaries. | `GAP-J002-003`, `GAP-J002-004`, `GAP-J002-005`, `GAP-J002-018` |
| `04_sql_dml_oracle_compatibility.md` | `sql_reference` | `general_reference_1_datatypes_properties`, `migration_oracle` | DML, functions, predicates, expressions, JSON SQL, and Altibase/Oracle difference blocks. | `GAP-J002-005`, `GAP-J002-017` |
| `05_data_types_properties.md` | `general_reference_1_datatypes_properties` | `release_notes_platform`, `patch_notes`, `sql_reference` | Data type and property item blocks, JSON, LOB, Temporary LOB, property defaults/ranges/check SQL. | `GAP-J002-001`, `GAP-J002-004`, `GAP-J002-005` |
| `06_data_dictionary_performance_views.md` | `general_reference_2_dictionary_views` | `performance_tuning`, `replication_manual`, `patch_notes` | Dictionary/performance view blocks, key columns, object lookup SQL, version-sensitive view availability. | `GAP-J002-006`, `GAP-J002-010` |
| `07_error_messages_troubleshooting.md` | `error_message_reference` | `sql_reference`, `general_reference_1_datatypes_properties`, `replication_manual`, `security_ssl_tls` | Error code/cause/action blocks, exact-code troubleshooting, related properties/views/check SQL. | `GAP-J002-008` |
| `08_performance_tuning_monitoring.md` | `performance_tuning`, `monitoring_api_snmp` | `general_reference_2_dictionary_views`, `release_notes_platform` | Plan/tuning workflows, hints, statistics, monitoring APIs, SNMP, source-limited JSON plan guardrails. | `GAP-J002-001`, `GAP-J002-006`, `GAP-J002-009` |
| `09_replication_ha_cdc.md` | `replication_manual`, `log_analyzer`, `replication_manager` | `security_ssl_tls`, `technical_documents_support`, `general_reference_2_dictionary_views` | Replication topology, DDL, state, compatibility, CDC, RepMgr, SSL, network runbooks. | `GAP-J002-002`, `GAP-J002-010`, `GAP-J002-011`, `GAP-J002-018` |
| `10_psm_stored_external_procedures.md` | `stored_external_procedures` | `sql_reference`, `general_reference_1_datatypes_properties` | PSM, packages, triggers, external procedures, type mapping, external library deployment. | `GAP-J002-013` |
| `11_java_jdbc_spring.md` | `jdbc_java`, `third_party_guides` | `security_ssl_tls`, `technical_documents_support` | JDBC URLs, driver classes, Java compatibility, Adapter for JDBC, Spring/Hibernate examples and cautions. | `GAP-J002-012`, `GAP-J002-014` |
| `12_c_cli_odbc_precompiler.md` | `c_cli_odbc_precompiler` | `security_ssl_tls`, `general_reference_1_datatypes_properties` | CLI, ODBC, C Interface, Precompiler, LOB APIs, JSON LOB cleanup, diagnostics. | `GAP-J002-012`, `GAP-J002-015` |
| `13_isql_iloader_basic_tools.md` | `isql_iloader` | `utilities_datacompj`, `security_ssl_tls`, `spatial_nifi_tableau` | iSQL command/session usage, iLoader load/export workflows, client option checks. | `GAP-J002-016`, `GAP-J002-017` |
| `14_utilities_operation_tools.md` | `utilities_datacompj` | `isql_iloader`, `replication_manager`, `kubernetes_aku` | Utilities, `aexport`, `altiComp`, `aku`, `altiMon`, `dataCompJ`, dump/diagnostic tools. | `GAP-J002-011`, `GAP-J002-016`, `GAP-J002-017` |
| `15_migration_oracle_compatibility.md` | `migration_oracle` | `sql_reference`, `general_reference_1_datatypes_properties`, `spatial_nifi_tableau` | Migration Center, Adapter for Oracle, object/data conversion, PSM review, validation, Oracle-difference routing. | `GAP-J002-005`, `GAP-J002-017` |
| `16_dblink_external_connectors.md` | `dblink_hadoop_external_connectors` | `jdbc_java`, `technical_documents_support`, `third_party_guides`, `security_ssl_tls` | DB Link, Hadoop Connector, third-party connector procedures, Java runtime and linker checks. | `GAP-J002-012`, `GAP-J002-014` |
| `17_kubernetes_aku_cloud.md` | `kubernetes_aku`, `third_party_guides` | `release_notes_platform`, `utilities_datacompj`, `replication_manual`, `security_ssl_tls` | Kubernetes deployment, AKU samples, container operations, image/env fields, validation steps. | `GAP-J002-012`, `GAP-J002-018` |
| `18_security_ssl_tls.md` | `security_ssl_tls` | `replication_manual`, `jdbc_java`, `c_cli_odbc_precompiler`, `technical_documents_support` | Client/server TLS, certificate setup, JDBC/CLI/tool TLS placement, replication SSL separation and checks. | `GAP-J002-002`, `GAP-J002-012`, `GAP-J002-018` |
| `19_spatial_nifi_tableau_misc.md` | `spatial_nifi_tableau`, `third_party_guides` | `jdbc_java`, `isql_iloader`, `utilities_datacompj`, `migration_oracle` | Spatial SQL, `GEOMETRY`, altiShapeLoader, NiFi, Tableau, JDBC settings, validation outcomes. | `GAP-J002-017` |

## Later-Job Handoff

- J003 defines reusable item block schemas and extraction rules in
  `GPTs/reports/catalog_schema_extraction_rules.md`; later jobs should apply those
  rules to the source families and coverage shapes in this matrix.
- J004 created `GPTs/reports/property_inventory.md` and added a compact property-name
  availability index to `05_data_types_properties.md`; J005-J009 should use that
  baseline with `general_reference_1_datatypes_properties` and close or split
  property/data type gaps from `GAP-J002-001`, `GAP-J002-004`, `GAP-J002-005`, and
  `GAP-J004-001`.
- J010 created `GPTs/reports/sql_syntax_inventory.md` as the SQL statement-family
  inventory, BNF conversion contract, and J011-J016 queue. J011-J016 should use that
  report with `sql_reference`, `administrator_operations`, `migration_oracle`, and
  `spatial_nifi_tableau` to convert syntax diagrams and SQL families into compact
  BNF-like item blocks.
- J017-J021 should use `general_reference_2_dictionary_views`, `performance_tuning`,
  `monitoring_api_snmp`, and replication/security view sources to close view/API gaps.
- J022-J026 should use `error_message_reference` and related operational sources to
  expand exact-code troubleshooting and close error-block gaps.
- J027-J033 should use operations, replication, networking, and TLS source families to
  expand runbooks and keep unresolved compatibility limits explicit.
- J034-J039 should use development, tool, connector, migration, and third-party guide
  source families to expand API/tool/integration coverage.
- J040 should run final retrieval and multilingual checks and verify that every open
  register item is either closed, split into a later accepted work item, or documented
  as a selected-source limitation.
