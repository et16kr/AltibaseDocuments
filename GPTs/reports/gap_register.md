# Altibase GPT Gap Register

Job: `J002`
Status: Active primary register
Last updated: 2026-05-16

## Register Rules

This is the primary tracking artifact for item-level gaps after J002. A gap entry is not
always an attachment defect. Some entries are selected-source limitations or verification
limits that must remain visible so later jobs do not invent unsupported detail.

Statuses:

- `Open`: selected sources or prior reviews show item-level coverage work that later
  jobs should resolve or split.
- `Guardrail`: selected sources do not currently support a definitive claim; attachments
  must keep narrow wording and ask for missing input.
- `Verification-limited`: source-backed text exists, but runtime execution, compile, or
  live integration validation was not performed.
- `Closed-trace`: prior gap was remediated before J002; the entry remains as a traceable
  source-policy reminder.

Every later job that touches a listed area should either close the entry, narrow it,
split it into more specific entries, or record why the source limitation remains.
Use `GPTs/reports/catalog_schema_extraction_rules.md` for the required item block,
BNF-like syntax, runbook, example, cross-reference, and validation-note shapes when
recording or remediating gaps.

## Gaps

### GAP-J002-001: JSON execution plan schema and examples

- Status: `Guardrail`
- Source family and version scope: `release_notes_platform`, `performance_tuning`,
  `general_reference_1_datatypes_properties`; Altibase 8.1 verified source.
- Missing item or behavior: Detailed JSON execution-plan schema, property value
  enumerations, and example JSON output for the release-note feature tied to
  `TRCLOG_EXPLAIN_TYPE` and `TRCLOG_JSON_PLAN_INDENT_DEPTH`.
- Affected attachments: `00_version_release_platform.md`,
  `05_data_types_properties.md`, `08_performance_tuning_monitoring.md`.
- Evidence: `GPTs/reports/8_1_verification.md` Source Gap Register;
  `review/reports/R02_high_risk_traceability.md`;
  `review/reports/R09_properties_datatypes.md`;
  `review/reports/R14_optimizer_execution_plan.md`;
  `review/reports/R27_multilingual_final_readiness.md`.
- Required remediation shape: Keep only release-note-backed feature and property names
  unless a later source is found. If a later source is found, add a compact item block
  with version, enabling property, allowed values/defaults, sample invocation, sample
  output fields, and verification SQL.

### GAP-J002-002: 8.1-to-older replication and replication SSL compatibility matrix

- Status: `Guardrail`
- Source family and version scope: `replication_manual`, `security_ssl_tls`,
  `technical_documents_support`; cross-version 7.1/7.3/8.1 replication.
- Missing item or behavior: A selected source-backed compatibility matrix for 8.1
  replication, especially 8.1 SSL replication with older peers.
- Affected attachments: `09_replication_ha_cdc.md`, `18_security_ssl_tls.md`.
- Evidence: `review/reports/R16_replication_topology_state.md`;
  `review/reports/R18_replication_ssl_network.md`.
- Required remediation shape: Add a version-pair compatibility item block only when a
  selected compatibility matrix, release note, or approved vendor/source confirmation is
  available. Until then, answers must request exact versions/builds, topology, transport,
  and vendor/source confirmation.

### GAP-J002-003: Tablespace restore/recovery syntax diagrams still need source audit

- Status: `Open`
- Source family and version scope: `administrator_operations`, `sql_reference`; 7.1,
  7.3, and 8.1.
- Missing item or behavior: Full source-audited BNF-like conversion for image-only
  tablespace restore/recovery grammar such as `restore_tablespace_clause` before any
  future generated `RESTORE TABLESPACE` or `RECOVER TABLESPACE` syntax expansion.
- Affected attachments: `02_administration_operations.md`,
  `03_sql_ddl_generation.md`.
- Evidence: `review/reports/R12_admin_backup_recovery_tablespace.md`.
- Required remediation shape: Per-version BNF-like syntax block, prerequisites, example
  SQL or command sequence, expected recovery mode, and validation/check SQL. Do not add
  syntax generated from diagrams until the original source diagram is audited.

### GAP-J002-004: Direct key supported-type matrix is summarized

- Status: `Open`
- Source family and version scope: `sql_reference`,
  `general_reference_1_datatypes_properties`; 7.1, 7.3, and 8.1.
- Missing item or behavior: Exhaustive direct-key supported/unsupported type matrix and
  full-key versus partial-key behavior.
- Affected attachments: `03_sql_ddl_generation.md`,
  `05_data_types_properties.md`.
- Evidence: `review/reports/R05_table_partition_index_constraint.md`.
- Required remediation shape: Searchable item block by key type with supported data
  types, unsupported combinations, version scope, DDL example, and validation query.

### GAP-J002-005: JSON SQL and function option grammar needs full itemization

- Status: `Open`
- Source family and version scope: `sql_reference`,
  `general_reference_1_datatypes_properties`, `migration_oracle`; Altibase 8.1 verified
  source, with 7.1/7.3 negative-scope cautions.
- Missing item or behavior: Full JSON function option grammar and deeper JSON DML
  behavior beyond the sampled family/path restrictions.
- Affected attachments: `03_sql_ddl_generation.md`,
  `04_sql_dml_oracle_compatibility.md`, `05_data_types_properties.md`,
  `15_migration_oracle_compatibility.md`.
- Evidence: `GPTs/reports/8_1_verification.md`;
  `GPTs/reports/eng_kor_parity.md`;
  `review/reports/R06_lob_json_datatype_ddl.md`;
  `review/reports/R07_dml_functions_oracle_overlap.md`;
  `review/reports/R08_oracle_migration_compatibility.md`.
- Required remediation shape: BNF-like syntax and function blocks for `JSON`,
  `JSON_ARRAY`, `JSON_OBJECT`, `JSON_EXISTS`, `JSON_QUERY`, `JSON_VALUE`,
  `JSON_VALID`, and `IS JSON`; include path operand restrictions, migration mapping,
  examples, and cross-references to error and property blocks.

### GAP-J002-006: Dictionary and performance view columns are not exhaustively proven

- Status: `Open`
- Source family and version scope: `general_reference_2_dictionary_views`,
  `performance_tuning`, `replication_manual`; 7.1, 7.3, and 8.1.
- Missing item or behavior: Exhaustive per-view column coverage across all large
  dictionary/performance views and patch levels.
- Affected attachments: `06_data_dictionary_performance_views.md`,
  `08_performance_tuning_monitoring.md`.
- Evidence: `review/reports/R10_dictionary_check_sql.md`.
- Required remediation shape: View item blocks with purpose, version availability, key
  columns, safe query timing, example check SQL, and a portable layout check using
  `V$TABLE`, `V$ALLCOLUMN`, `SYSTEM_.SYS_TABLES_`, and `SYSTEM_.SYS_COLUMNS_`.

### GAP-J002-007: Platform and patch support needs exact-version guardrails

- Status: `Guardrail`
- Source family and version scope: `release_notes_platform`, `patch_notes`,
  `technical_documents_support`; 7.1, 7.3, and 8.1.
- Missing item or behavior: Exhaustive inspection of every minor 7.1/7.3 patch release
  note for platform and support-boundary changes.
- Affected attachments: `00_version_release_platform.md`,
  `01_getting_started_installation.md`.
- Evidence: `review/reports/R11_install_startup_platform.md`;
  `GPTs/reports/version_coverage_validation.md`.
- Required remediation shape: Patch-level platform notes where selected sources support
  them; otherwise require exact version, patch, OS, CPU architecture, glibc/libc, Java,
  and client package before final support guidance.

### GAP-J002-008: Error reference expansion remains item-level work

- Status: `Open`
- Source family and version scope: `error_message_reference` plus related SQL,
  property, replication, and TLS sources; 7.1, 7.3, and 8.1.
- Missing item or behavior: Exhaustive exact-code blocks for grouped or low-frequency
  error codes, especially when multiple codes share one troubleshooting topic.
- Affected attachments: `07_error_messages_troubleshooting.md`.
- Evidence: `review/reports/R13_troubleshooting_errors.md`;
  `GPTs/reports/eng_kor_parity.md` for known 8.1 JSON error detail.
- Required remediation shape: Error item block with code, symbol, message, cause,
  action, affected versions, related property/view/check SQL, and missing-log or
  missing-object-definition prompt.

### GAP-J002-009: Monitoring API and SNMP behavior was source-reviewed, not live-tested

- Status: `Verification-limited`
- Source family and version scope: `monitoring_api_snmp`, `performance_tuning`; 7.1,
  7.3, and 8.1.
- Missing item or behavior: Runtime confirmation of sample SQL, Monitoring API calls,
  SNMP counters, traps, and ports against live Altibase environments.
- Affected attachments: `08_performance_tuning_monitoring.md`,
  `06_data_dictionary_performance_views.md`.
- Evidence: `review/reports/R15_monitoring_snmp_api.md`.
- Required remediation shape: Preserve source-backed API/SNMP blocks. If live validation
  becomes available, add tested command/call examples, expected return values, and
  version/environment notes.

### GAP-J002-010: 7.1 receive-only replication option is patch/meta-version sensitive

- Status: `Open`
- Source family and version scope: `replication_manual`, `patch_notes`,
  `general_reference_2_dictionary_views`; Altibase 7.1 patch scope and cross-version
  replication checks.
- Missing item or behavior: A concise patch-sensitive item block reconciling the 7.1
  General Reference option list with the SQL Reference and 7.1.0.8.5 patch-note
  `RECEIVE_ONLY` evidence.
- Affected attachments: `09_replication_ha_cdc.md`,
  `06_data_dictionary_performance_views.md`.
- Evidence: `review/reports/R16_replication_topology_state.md`.
- Required remediation shape: Item block with exact patch/source evidence, option value,
  check SQL, and answer pattern requiring exact patch or metadata check before stating
  receive-only availability.

### GAP-J002-011: Replication Manager package contents are installed-tool checks

- Status: `Guardrail`
- Source family and version scope: `replication_manager`, `utilities_datacompj`;
  supported tool releases used with 7.1, 7.3, and 8.1 servers.
- Missing item or behavior: Stable source-backed package contents for all Replication
  Manager distributions.
- Affected attachments: `09_replication_ha_cdc.md`,
  `14_utilities_operation_tools.md`.
- Evidence: `review/reports/R17_cdc_loganalyzer_repmgr.md`.
- Required remediation shape: Keep package contents as an installed-tool or release
  package verification step. If a stable manifest source is later selected, add an item
  block with release, files, driver placement, and startup validation.

### GAP-J002-012: TLS and connector live integration behavior is not validated

- Status: `Verification-limited`
- Source family and version scope: `security_ssl_tls`, `jdbc_java`,
  `c_cli_odbc_precompiler`, `third_party_guides`; 7.1, 7.3, and 8.1.
- Missing item or behavior: Live handshake or connector execution validation for JDBC,
  ODBC/CLI, ADO.NET, iSQL, utilities, Kubernetes, and third-party connectors.
- Affected attachments: `11_java_jdbc_spring.md`,
  `12_c_cli_odbc_precompiler.md`, `16_dblink_external_connectors.md`,
  `17_kubernetes_aku_cloud.md`, `18_security_ssl_tls.md`,
  `19_spatial_nifi_tableau_misc.md`.
- Evidence: `review/reports/R19_security_tls.md`;
  `review/reports/R24_dblink_connectors_kubernetes.md`.
- Required remediation shape: Preserve source-backed settings and ask for exact
  Altibase version, client interface, OS/platform, Java/OpenSSL version, certificate
  mode, trust model, and target ports. Add live-tested examples only with environment
  and source notes.

### GAP-J002-013: PSM and external procedure examples lack compile/runtime validation

- Status: `Verification-limited`
- Source family and version scope: `stored_external_procedures`, `sql_reference`; 7.1,
  7.3, and 8.1.
- Missing item or behavior: Live compilation/execution of PSM and external C/C++
  examples; exhaustive conversion of every PSM grammar image.
- Affected attachments: `10_psm_stored_external_procedures.md`,
  `04_sql_dml_oracle_compatibility.md`.
- Evidence: `review/reports/R20_psm_external_procedures.md`.
- Required remediation shape: Add or refine BNF-like syntax and compile/runbook blocks
  from source diagrams. Add live-tested compile/load/run notes only when a test
  environment is available.

### GAP-J002-014: Java compatibility and alternate-server behavior are patch sensitive

- Status: `Open`
- Source family and version scope: `jdbc_java`, `technical_documents_support`,
  `dblink_hadoop_external_connectors`; especially 7.1 patch/client driver scope.
- Missing item or behavior: Patch-sensitive Java runtime/JDBC 4.2 boundary and exact
  alternate-server grammar beyond examples.
- Affected attachments: `11_java_jdbc_spring.md`,
  `16_dblink_external_connectors.md`.
- Evidence: `review/reports/R21_java_jdbc_spring.md`.
- Required remediation shape: Item blocks for JDBC URL repeated-list grammar, Java
  compatibility by server/client patch, Adapter version boundaries, and production
  prompt asking for exact driver or Adapter patch.

### GAP-J002-015: Compile-ready CLI LOB signatures need exact header/manual source

- Status: `Open`
- Source family and version scope: `c_cli_odbc_precompiler`,
  `general_reference_1_datatypes_properties`; Altibase 8.1 verified source and
  7.x client manuals where applicable.
- Missing item or behavior: Detailed compile-ready signatures for less common CLI LOB
  functions such as `SQLEmptyLob()` and `SQLGetLobLength2()`.
- Affected attachments: `12_c_cli_odbc_precompiler.md`.
- Evidence: `review/reports/R22_c_cli_odbc_precompiler_isql_iloader.md`.
- Required remediation shape: Verify exact headers or manuals, then add function item
  blocks with signature, arguments, return/diagnostic handling, LOB/JSON LOB context,
  version scope, and compile cautions.

### GAP-J002-016: Low-frequency utility and iLoader options are intentionally partial

- Status: `Open`
- Source family and version scope: `isql_iloader`, `utilities_datacompj`; 7.1, 7.3,
  and 8.1 client package scope.
- Missing item or behavior: Exhaustive low-frequency options and output fields for
  iSQL, iLoader, utilities, `dataCompJ`, and dump tools.
- Affected attachments: `13_isql_iloader_basic_tools.md`,
  `14_utilities_operation_tools.md`.
- Evidence: `review/reports/R22_c_cli_odbc_precompiler_isql_iloader.md`;
  `review/reports/R23_utilities_datacompj.md`.
- Required remediation shape: Tool option item blocks prioritized by operational risk,
  with command syntax, input files, outputs, patch/client-help caveat, and validation
  steps.

### GAP-J002-017: Spatial, migration, NiFi, and Tableau examples need deeper itemization

- Status: `Open`
- Source family and version scope: `spatial_nifi_tableau`, `migration_oracle`,
  `jdbc_java`, `isql_iloader`, `utilities_datacompj`; 7.1, 7.3, and 8.1.
- Missing item or behavior: Exhaustive Spatial function examples, Adapter for Oracle
  property values, and Altibase-to-Altibase spatial WKB/EWKB migration cautions in the
  best target attachments.
- Affected attachments: `19_spatial_nifi_tableau_misc.md`,
  `15_migration_oracle_compatibility.md`,
  `13_isql_iloader_basic_tools.md`, `14_utilities_operation_tools.md`.
- Evidence: `review/reports/R25_migration_spatial_misc.md`.
- Required remediation shape: Function and tool item blocks with source-backed syntax,
  property/option values, example SQL or command, expected result, and cross-reference
  between Spatial, iLoader/aexport, and migration attachments.

### GAP-J002-018: High-risk converted visual/procedure coverage needs final source audit

- Status: `Open`
- Source family and version scope: All source families with syntax diagrams, topology
  diagrams, workflow figures, or UI screenshots; 7.1, 7.3, and 8.1.
- Missing item or behavior: Final source audit for high-risk converted visuals where
  diagram semantics can change customer behavior, including DDL syntax, replication
  topology/state, backup/recovery workflows, execution plan trees, installer/tool UI
  procedures, and security/replication SSL flows.
- Affected attachments: `01_getting_started_installation.md`,
  `02_administration_operations.md`, `03_sql_ddl_generation.md`,
  `09_replication_ha_cdc.md`, `17_kubernetes_aku_cloud.md`,
  `18_security_ssl_tls.md`.
- Evidence: `review/reports/R00_upload_boundary.md`;
  `review/reports/R26_retrieval_visual_conversion.md`.
- Required remediation shape: For each high-risk figure or screenshot, record whether
  it is represented by BNF-like text, procedural text, Mermaid, or an explicit accepted
  omission. Include source path, version scope, and retrieval-friendly cross-reference.

### GAP-J002-019: 8.1 Korean-source-only feature details must stay English-normalized

- Status: `Closed-trace`
- Source family and version scope: `general_reference_1_datatypes_properties`,
  `sql_reference`, `general_reference_2_dictionary_views`, `error_message_reference`,
  `replication_manual`, `security_ssl_tls`, `c_cli_odbc_precompiler`; Altibase 8.1
  verified source.
- Missing item or behavior: Earlier English-only extraction missed 8.1 JSON, Temporary
  LOB, replication SSL, JSON error, and `SQLFreeLob2` details found in Korean sources.
- Affected attachments: `03_sql_ddl_generation.md`,
  `04_sql_dml_oracle_compatibility.md`, `05_data_types_properties.md`,
  `06_data_dictionary_performance_views.md`, `07_error_messages_troubleshooting.md`,
  `09_replication_ha_cdc.md`, `12_c_cli_odbc_precompiler.md`,
  `18_security_ssl_tls.md`.
- Evidence: `GPTs/reports/8_1_verification.md`;
  `GPTs/reports/eng_kor_parity.md`;
  `review/reports/R02_high_risk_traceability.md`;
  `review/reports/R06_lob_json_datatype_ddl.md`;
  `review/reports/R18_replication_ssl_network.md`;
  `review/reports/R22_c_cli_odbc_precompiler_isql_iloader.md`.
- Required remediation shape: Keep Korean-source detail translated and normalized into
  English, preserve literal tokens, and never expose internal source labels in
  customer-facing attachments. Reopen or split this entry if later jobs find missing
  item-level detail inside these 8.1 feature areas.

### GAP-J004-001: Full per-property detail blocks remain split across property jobs

- Status: `Open`
- Source family and version scope: `general_reference_1_datatypes_properties`; Altibase
  7.1, Altibase 7.3, and Altibase 8.1 verified source.
- Missing item or behavior: J004 inventories `484` source-backed property names and
  version availability, but `05_data_types_properties.md` still contains complete
  decomposed blocks only for high-retrieval properties. Most inventoried names still
  need source-backed defaults, ranges, units, dynamic-change support, change method,
  related views, cautions, and examples where the manuals provide them.
- Affected attachments: `05_data_types_properties.md`, with cross-references to
  `03_sql_ddl_generation.md`, `06_data_dictionary_performance_views.md`,
  `08_performance_tuning_monitoring.md`, `09_replication_ha_cdc.md`, and
  `18_security_ssl_tls.md` when a property affects SQL generation, diagnostics,
  tuning, replication, or security.
- Evidence: `GPTs/reports/property_inventory.md`;
  `Manuals/Altibase_7.1/kor/General Reference-1.Data Types & Altibase Properties.md`;
  `Manuals/Altibase_7.3/kor/General_Reference-1.Data Types & Altibase Properties.md`;
  `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`.
- Required remediation shape: Use the J003 property block schema for each later
  expansion: name, version scope, meaning, default, range or values, dynamic-change
  support, change method, `V$PROPERTY` check SQL, related views/properties, cautions,
  and exact-version or environment prompts where source material is incomplete. J005
  should start with initialization/storage properties, J006 with LOB/JSON/temporary
  object properties, J007 with performance/optimizer properties, J008 with session,
  network, security, and replication properties, and J009 with catalog QA and remaining
  property gaps.
