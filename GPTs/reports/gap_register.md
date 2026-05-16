# Altibase GPT Gap Register

Job: `J002`
Status: Active primary register
Last updated: 2026-05-17

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

### GAP-J002-003: Tablespace restore/recovery syntax diagrams source-audited by J011

- Status: `Closed-trace`
- Source family and version scope: `administrator_operations`, `sql_reference`; 7.1,
  7.3, and 8.1.
- Missing item or behavior: Closed by J011. The image-only
  `restore_tablespace_clause` was source-audited for 7.1, 7.3, and the Altibase 8.1
  verified source, and customer-facing syntax now converts it only as
  `TABLESPACE tablespace_name [, tablespace_name ...]`.
- Affected attachments: `02_administration_operations.md`,
  `03_sql_ddl_generation.md`.
- Evidence: `review/reports/R12_admin_backup_recovery_tablespace.md`;
  `GPTs/reports/sql_syntax_inventory.md`; `GPTs/attachments/03_sql_ddl_generation.md`;
  `GPTs/attachments/02_administration_operations.md`.
- Required remediation shape: Completed for the scoped grammar. Keep this trace so later
  jobs preserve the guardrail: generate `ALTER DATABASE RESTORE TABLESPACE ...` only
  from the audited restore clause and do not invent `RECOVER TABLESPACE`.

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

### GAP-J002-005: JSON SQL and function option grammar source-audited by J015

- Status: `Closed-trace`
- Source family and version scope: `sql_reference`,
  `general_reference_1_datatypes_properties`, `migration_oracle`; Altibase 8.1 verified
  source, with 7.1/7.3 negative-scope cautions.
- Missing item or behavior: Closed by J015 for the selected-source SQL scope. The 8.1
  Korean SQL Reference JSON function grammar and General Reference 1 JSON type/path
  restrictions were converted to English-normalized item blocks, and Migration Center
  JSON mapping cautions were cross-referenced.
- Affected attachments: `03_sql_ddl_generation.md`,
  `04_sql_dml_oracle_compatibility.md`, `05_data_types_properties.md`,
  `15_migration_oracle_compatibility.md`.
- Evidence: `GPTs/reports/8_1_verification.md`;
  `GPTs/reports/eng_kor_parity.md`;
  `review/reports/R06_lob_json_datatype_ddl.md`;
  `review/reports/R07_dml_functions_oracle_overlap.md`;
  `review/reports/R08_oracle_migration_compatibility.md`.
- Required remediation shape: Completed for `JSON_ARRAY`, `JSON_OBJECT`,
  `JSON_EXISTS`, `JSON_QUERY`, `JSON_VALUE`, `JSON_VALID`, `IS JSON`, JSON path
  operand restrictions, JSON DML examples, migration mapping, and Temporary LOB/error
  cross-references. Keep this trace so later jobs preserve the guardrail: Oracle
  SQL/JSON constructs not listed in the selected Altibase SQL Reference, such as
  `JSON_TABLE`, require manual redesign or exact target-version proof.

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
- J017 update: `GPTs/reports/dictionary_view_inventory.md` now provides the
  source-backed dictionary/performance view name, version-availability, and grouping
  baseline, and `GPTs/attachments/06_data_dictionary_performance_views.md` includes a
  compact customer-facing inventory index. This gap remains open for exhaustive
  per-view column blocks and patch-sensitive column validation in J018-J021.
- J018 update: the storage/log/archive/backup/checkpoint slice now has richer
  customer-facing cookbook checks and object blocks for `V$DATABASE`, `V$TABLESPACES`,
  `V$DATAFILES`, `V$MEM_TABLESPACES`, `V$VOL_TABLESPACES`, checkpoint-path/stable-file
  views, `V$LOG`, `V$LFG`, `V$ARCHIVE`, `V$BACKUP_INFO`,
  `V$OBSOLETE_BACKUP_INFO`, `V$FILESTAT`, `V$SNAPSHOT`, `V$TRACELOG`, and
  `V$TEMPORARY_LOBS`. The gap remains open for J019-J021 view families and exhaustive
  per-view, patch-sensitive column proof beyond the J018 scope.
- J019 update: the session/statement/wait/lock/transaction/service-thread slice now has
  richer customer-facing cookbook checks and object blocks for `V$SESSION`,
  `V$SESSIONMGR`, `V$SERVICE_THREAD`, `V$SERVICE_THREAD_MGR`, `V$STATEMENT`,
  `V$SQLTEXT`, `V$EVENT_NAME`, `V$WAIT_CLASS_NAME`, `V$SESSION_WAIT`,
  `V$SESSION_EVENT`, `V$SESSION_WAIT_CLASS`, `V$SYSTEM_EVENT`,
  `V$SYSTEM_WAIT_CLASS`, `V$LATCH`, `V$MUTEX`, `V$TRANSACTION`,
  `V$TRANSACTION_MGR`, `V$LOCK_WAIT`, `V$LOCK`, and `V$LOCK_STATEMENT` in
  `GPTs/attachments/06_data_dictionary_performance_views.md`. The gap remains open
  for J020-J021 view families and exhaustive per-view, patch-sensitive column proof
  beyond the J019 scope.
- J020 update: the optimizer/statistics/plan-cache/buffer/flusher/memory/table and
  index, segment, undo, temp, and direct-path slice now has richer customer-facing cookbook checks
  and object blocks for `V$SQL_PLAN_CACHE`, `V$SQL_PLAN_CACHE_PCO`,
  `V$SQL_PLAN_CACHE_SQLTEXT`, `V$DBMS_STATS`, `V$LOCK_TABLE_STATS`,
  `V$STATNAME`, `V$SYSSTAT`, `V$SESSTAT`, `V$MEMSTAT`, `V$MEMGC`,
  `V$BUFFPAGEINFO`, `V$BUFFPOOL_STAT`, `V$UNDO_BUFF_STAT`, `V$SBUFFER_STAT`,
  `V$FLUSHER`, `V$FLUSHINFO`, `V$SFLUSHER`, `V$SFLUSHINFO`, `V$MEMTBL_INFO`,
  `V$DISKTBL_INFO`, `V$INDEX`, BTREE/RTREE index header and node-pool view families,
  `V$SEGMENT`, `V$USAGE`, `V$DB_FREEPAGELISTS`, `V$TSSEGS`, `V$TXSEGS`,
  `V$UDSEGS`, `V$DISK_UNDO_USAGE`, `V$DISK_TEMP_INFO`, `V$DISK_TEMP_STAT`, and
  `V$DIRECT_PATH_INSERT` in `GPTs/attachments/06_data_dictionary_performance_views.md`,
  with tuning interpretation updates in `GPTs/attachments/08_performance_tuning_monitoring.md`.
  The gap remains open for J021 view families and exhaustive per-view,
  patch-sensitive column proof beyond the J020 scope.
- J021 update: the replication/CDC/security/Monitoring API/SNMP slice now has richer
  customer-facing cookbook checks, object blocks, and mapping blocks for
  `SYSTEM_.SYS_AUDIT_`, `SYSTEM_.SYS_AUDIT_OPTS_`,
  `SYSTEM_.SYS_SECURITY_`, `SYSTEM_.SYS_ENCRYPTED_COLUMNS_`,
  `SYSTEM_.SYS_REPLICATIONS_`, `SYSTEM_.SYS_REPL_HOSTS_`,
  `SYSTEM_.SYS_REPL_ITEMS_`, replication Sender, Receiver, gap, sync, log-buffer,
  offline, statistics, transaction, and recovery view families, Monitoring API function-to-view
  mappings, and SNMP MIB-to-SQL cross-check mappings in
  `GPTs/attachments/06_data_dictionary_performance_views.md`, with cross-reference
  updates in `GPTs/attachments/08_performance_tuning_monitoring.md`,
  `GPTs/attachments/09_replication_ha_cdc.md`, and
  `GPTs/attachments/18_security_ssl_tls.md`. The gap remains open only for exhaustive
  per-view, patch-sensitive column proof outside the J018-J021 scoped slices.

### GAP-J017-001: Dictionary and performance view inventory source drift

- Status: `Guardrail`
- Source family and version scope: `general_reference_2_dictionary_views`,
  `release_notes_platform`; Altibase 7.1, Altibase 7.3, and Altibase 8.1 verified
  source.
- Missing item or behavior: Reconciled source explanation for list drift around
  `SYS_REPL_TABLE_OID_IN_USE_`, `V$QUEUE_DELETE_OFF`, `V$TEMPORARY_LOBS`, and
  `V$ST_ANGULAR_UNIT`/`V$ST_AREA_UNIT`/`V$ST_LINEAR_UNIT`.
- Affected attachments: `06_data_dictionary_performance_views.md`,
  `09_replication_ha_cdc.md`, `19_spatial_nifi_tableau_misc.md`.
- Evidence: `GPTs/reports/dictionary_view_inventory.md`;
  `Manuals/Altibase_7.1/kor/General Reference-2.The Data Dictionary.md`;
  `Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md`;
  `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`;
  `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`.
- Required remediation shape: Keep Korean-source precedence in customer-facing
  attachments. For `SYS_REPL_TABLE_OID_IN_USE_`, require an installed-version metadata
  check before relying on 8.1 availability. For `V$QUEUE_DELETE_OFF` and
  `V$TEMPORARY_LOBS`, keep the Korean-source-backed names despite English list
  omissions. For the reserved `V$ST_*` spatial unit views, treat them as 7.1
  Korean-source-only unless a later selected Korean source proves wider availability.

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
- J022 update: `GPTs/reports/error_reference_inventory.md` now provides the
  source-backed error-family inventory, severity-count baseline, exact-code/grouped
  response schema, and J023-J026 error expansion queue. This gap remains `Open` for
  item-level exact-code expansion, but later jobs should use the J022 inventory rather
  than rediscovering family boundaries.
- J023 update: `GPTs/attachments/07_error_messages_troubleshooting.md` now contains
  grouped exact-code maps for storage, datafile, file-system, backup, recovery, log,
  checkpoint, incremental-backup, and tablespace errors from the selected Korean 7.1,
  7.3, and Altibase 8.1 verified source Error Message References, with supporting
  checks and stop conditions. This gap remains `Open` for the J024-J026 error slices
  and for exhaustive exact-code coverage outside the J023 grouped blocks.
- J024 update: `GPTs/attachments/07_error_messages_troubleshooting.md` now contains
  grouped exact-code maps for SQL parser, DDL, table/column/data type, constraint,
  conversion, date, regular-expression, JSON, Temporary LOB, ordinary LOB, client/API
  LOB, Precompiler LOB, and utility LOB errors from the selected Korean 7.1, 7.3, and
  Altibase 8.1 verified source Error Message References, with supporting checks and
  version cautions. This gap remains `Open` for the J025-J026 error slices and for
  exhaustive exact-code coverage outside the J023-J024 grouped blocks.
- J025 update: `GPTs/attachments/07_error_messages_troubleshooting.md` now contains
  grouped exact-code maps for client session/protocol and alternate-server connection
  errors, replication startup/object-eligibility and metadata/conflict/log-buffer
  errors, SSL/TLS client and server certificate errors, DB Link/`AltiLinker` network
  and transaction errors, iSQL/iLoader/utility option and file errors, APRE
  source/connection/cursor errors, and Log Analyzer network/protocol/metadata/XLog-pool
  errors from the selected Korean 7.1, 7.3, and Altibase 8.1 verified source Error
  Message References, with component-specific evidence prompts and cross-references.
  This gap remains `Open` for J026 QA and for exhaustive exact-code coverage outside
  the J023-J025 grouped blocks.
- J026 update: `GPTs/attachments/07_error_messages_troubleshooting.md` now includes a
  QA gate for exact-code answers, aligns the response format with `Required Customer
  Input`, tightens uncovered-code and prefix-safety wording, and routes remaining
  Spatial `ST Error Code` exact-code work into `GAP-J026-001`. This gap remains
  `Open` only for exhaustive exact-code coverage outside the J023-J025 grouped blocks
  and the explicitly split spatial/sharding follow-up gaps.

### GAP-J022-001: `SD Error Code` source drift needs exact installed-version evidence

- Status: `Open`
- Source family and version scope: `error_message_reference`; Altibase 7.1, Altibase
  7.3, and Altibase 8.1 verified source, with English extraction-aid drift.
- Missing item or behavior: The 7.1 Korean Error Message Reference lists `SD Error
  Code` / `sdERR_*` entries. The checked 7.3 and Altibase 8.1 verified Korean Error
  Message Reference files do not list an `SD Error Code` chapter, while the checked
  8.1 English extraction aid does list `SD Error Code` entries. The attachment must
  not claim verified 7.3 or 8.1 `sdERR_*` coverage without exact installed-version
  evidence.
- Affected attachments: `07_error_messages_troubleshooting.md`; later sharding/tool
  coverage may also affect `09_replication_ha_cdc.md`, `16_dblink_external_connectors.md`,
  and `19_spatial_nifi_tableau_misc.md` if a later job accepts sharding-specific
  source scope.
- Evidence: `GPTs/reports/error_reference_inventory.md`;
  `Manuals/Altibase_7.1/kor/Error Message Reference.md`;
  `Manuals/Altibase_7.3/kor/Error Message Reference.md`;
  `Manuals/Altibase_trunk/kor/Error Message Reference.md`;
  `Manuals/Altibase_trunk/eng/Error Message Reference.md`.
- Required remediation shape: Until a later source-backed sharding job resolves the
  drift, preserve the customer-supplied exact `sdERR_*` or `0x...` code, ask for the
  exact product version, patch level, full error line, and installed manual/runtime
  evidence, and avoid broad 7.3 or 8.1 `sdERR_*` claims. If later accepted sharding
  sources are added, create exact-code maps with version scope, cause/action, and
  metadata/topology checks.

### GAP-J026-001: Spatial `ST Error Code` exact-code blocks need itemization

- Status: `Open`
- Source family and version scope: `error_message_reference` plus
  `spatial_nifi_tableau` and related dictionary metadata; Altibase 7.1, Altibase 7.3,
  and Altibase 8.1 verified source, with Korean Error Message Reference and Spatial
  SQL Reference manuals as the authority.
- Missing item or behavior: The selected Korean Error Message Reference manuals list
  `ST Error Code` / `stERR_*` chapters for Spatial SQL and geometry processing, but
  the customer-facing error attachment does not yet provide exact-code maps for
  Spatial errors such as WKT/WKB parsing, incompatible geometry types, SRID-sensitive
  operations, invalid buffer distance, object integrity, ring/line/polygon validation,
  and Spatial conversion failures.
- Affected attachments: `07_error_messages_troubleshooting.md` for exact-code
  troubleshooting blocks; `19_spatial_nifi_tableau_misc.md` for Spatial SQL,
  `GEOMETRY`, SRID, `GEOMETRY_COLUMNS`, `SPATIAL_REF_SYS`, R-Tree, and
  `altiShapeLoader` cross-references.
- Evidence: `GPTs/reports/error_reference_inventory.md`;
  `Manuals/Altibase_7.1/kor/Error Message Reference.md`;
  `Manuals/Altibase_7.3/kor/Error Message Reference.md`;
  `Manuals/Altibase_trunk/kor/Error Message Reference.md`;
  `Manuals/Altibase_7.1/kor/Spatial SQL Reference.md`;
  `Manuals/Altibase_7.3/kor/Spatial SQL Reference.md`;
  `Manuals/Altibase_trunk/kor/Spatial SQL Reference.md`.
- Required remediation shape: Add grouped exact-code maps with code, decimal value,
  symbol, message, source-backed cause/action, affected version scope, and first
  checks. Required customer-input prompts should request the failed Spatial SQL
  function or operator, `GEOMETRY` column definition, WKT/WKB/EWKT/EWKB input when
  safe to share, SRID value, `GEOMETRY_COLUMNS` and `SPATIAL_REF_SYS` evidence,
  `altiShapeLoader` command/source file when relevant, exact version and patch level,
  and trace or utility output. Cross-reference `19_spatial_nifi_tableau_misc.md` for
  Spatial syntax and metadata procedures.

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
- J021 update: `GPTs/attachments/06_data_dictionary_performance_views.md` now maps
  Monitoring API functions to performance views/properties and maps SNMP MIB families
  to SQL-side cross-checks. This gap remains `Verification-limited` because the
  repository still has no live Altibase host, Monitoring API program output,
  `snmpwalk`, or `snmptrapd` run output for target environments.

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
- Progress notes:
  - J005 expanded initialization/path/memory/disk/volatile/log/storage property blocks
    in `GPTs/attachments/05_data_types_properties.md`, including `DEFAULT_MEM_DB_FILE_SIZE`,
    `DEFAULT_SEGMENT_STORAGE_*`, `DOUBLE_WRITE_DIRECTORY`, `DRDB_FD_MAX_COUNT_PER_DATAFILE`,
    log compression thresholds, recycle-bin sizing, system/user datafile defaults,
    tablespace extent defaults, and temporary page storage defaults. This gap remains
    `Open` for J006-J009 non-J005 property families and final catalog QA.
  - J006 expanded LOB, JSON, Temporary LOB, PSM, VARRAY, and object-size property
    blocks in `GPTs/attachments/05_data_types_properties.md`, including
    `LOB_CACHE_THRESHOLD`, `ST_OBJECT_BUFFER_SIZE`, 8.1-only Temporary LOB properties,
    PSM cursor/file/default-precision behavior, `PSM_MAX_DDL_REFERENCE_DEPTH`,
    `LISTAGG_PRECISION`, and `VARRAY_MEMORY_MAXIMUM`. This gap remains `Open` for
    J007-J009 performance/optimizer, network/security/replication, and final property
    catalog QA.
  - J007 expanded performance and optimizer property blocks in
    `GPTs/attachments/05_data_types_properties.md`, including buffer-pool sizing,
    buffer replacement and flusher thresholds, checkpoint intervals and bulk flush,
    `CHECKPOINT_SCALE_SINGLE_DW_BUFFER_SIZE`, sort/hash/work-area memory,
    execution/prepare statement memory, SQL plan cache sizing, optimizer behavior and
    query transformation controls, and parallel query controls. This gap remains
    `Open` for J008-J009 session, network/security/replication, and final property
    catalog QA.
  - J008 expanded session, timeout, client communication, NLS, network/security,
    SSL/TLS, SNMP, and replication property blocks in
    `GPTs/attachments/05_data_types_properties.md`, including IPC/IPCDA properties,
    user-lock waits, `SERVICE_THREAD_RECV_TIMEOUT`, ordinary/SSL/InfiniBand
    replication ports, replication connection/heartbeat/DDL/conflict/sync/recovery
    properties, `IB_*`, `SNMP_*`, `TCP_ENABLE`, and `SSL_*` properties. This gap
    remains `Open` for J009 final property catalog QA, source-drift cleanup, and
    remaining low-retrieval property families.
  - J009 completed final property catalog QA in
    `GPTs/attachments/05_data_types_properties.md` and
    `GPTs/reports/property_inventory.md`. It confirmed that all `484` inventoried
    property names appear in the attachment inventory baseline, every decomposed
    property section or group has a dynamic-change/restart/recreate/verify cue, and
    the attachment's cross-reference filenames resolve. It also recorded 8.1
    source-drift guardrails for `REPLICATION_UPDATE_REPLACE` and
    `REPLICATION_META_ITEM_COUNT_DIFF_ENABLE` because selected 8.1 Korean detailed
    General Reference property blocks are absent even though related 8.1 replication
    sources mention the properties. This gap remains `Open` after J009 for remaining
    low-retrieval property families that are inventoried by name but still lack full
    per-property default, range, dynamic-change, related-view, and caution blocks in
    the customer-facing attachment; later jobs should split or close those details
    only when their source-family scope requires them.

### GAP-J010-001: SQL Reference syntax diagram conversion queue remains open

- Status: `Open`
- Source family and version scope: `sql_reference` with supporting
  `administrator_operations`, `replication_manual`, `log_analyzer`,
  `performance_tuning`, `migration_oracle`, `dblink_hadoop_external_connectors`,
  `spatial_nifi_tableau`, and `stored_external_procedures`; Altibase 7.1, Altibase 7.3,
  and Altibase 8.1 verified source.
- Missing item or behavior: J010 inventories the SQL statement families and BNF-like
  conversion rules, but customer-facing attachments still need source-audited item
  blocks for the full SQL Reference syntax diagram queue. Existing compact BNF in the
  attachments is partial and must be verified or expanded by statement family.
- Affected attachments: `02_administration_operations.md`,
  `03_sql_ddl_generation.md`,
  `04_sql_dml_oracle_compatibility.md`, `05_data_types_properties.md`,
  `08_performance_tuning_monitoring.md`, `09_replication_ha_cdc.md`,
  `10_psm_stored_external_procedures.md`, `15_migration_oracle_compatibility.md`,
  `16_dblink_external_connectors.md`, `18_security_ssl_tls.md`, and
  `19_spatial_nifi_tableau_misc.md`.
- Evidence: `GPTs/reports/sql_syntax_inventory.md`;
  `GPTs/reports/image_inventory.md`; `GPTs/reports/coverage_matrix.md`;
  `Manuals/Altibase_7.1/kor/SQL Reference.md`;
  `Manuals/Altibase_7.3/kor/SQL Reference.md`;
  `Manuals/Altibase_trunk/kor/SQL Reference.md`;
  `Manuals/Altibase_7.1/kor/Replication Manual.md`;
  `Manuals/Altibase_7.3/kor/Replication Manual.md`;
  `Manuals/Altibase_trunk/kor/Replication Manual.md`;
  `Manuals/Altibase_7.1/kor/Log Analyzer User's Manual.md`;
  `Manuals/Altibase_7.3/kor/Log Analyzer User's Manual.md`;
  `Manuals/Altibase_trunk/kor/Log Analyzer User's Manual.md`.
- Required remediation shape: J011-J016 have completed their assigned SQL-generation
  families. J034 and J039 should apply the same notation rules to PSM, external
  procedure, Spatial, and tool-adjacent SQL, adding compact BNF roots and named clause
  productions, version scope, prerequisites, examples, validation SQL,
  destructive-operation and implicit-commit cautions, and cross-references. Keep Korean
  source precedence and customer-facing English normalization throughout.
- J011 update: The database, tablespace, datafile, archive, backup, restore, and
  recovery SQL family is source-audited and expanded in
  `GPTs/attachments/03_sql_ddl_generation.md`, with the operational
  `RESTORE TABLESPACE` guardrail cross-referenced in
  `GPTs/attachments/02_administration_operations.md`. This queue remains open for
  J013-J016 and later specialized SQL families.
- J012 update: The table, column, constraint, partition, LOB storage, queue, and
  table-maintenance SQL family is source-audited and expanded in
  `GPTs/attachments/03_sql_ddl_generation.md`, with queue DML wait semantics in
  `GPTs/attachments/04_sql_dml_oracle_compatibility.md` and LOB storage cross-reference
  guidance in `GPTs/attachments/05_data_types_properties.md`. The shared syntax queue
  remains open for J013-J016 and later specialized SQL families.
- J013 update: The index, optimizer statistics, hint, execution-plan, and
  tuning-related SQL family is source-audited and expanded in
  `GPTs/attachments/08_performance_tuning_monitoring.md`, with supporting
  `V$DBMS_STATS` and `V$LOCK_TABLE_STATS` object blocks in
  `GPTs/attachments/06_data_dictionary_performance_views.md` and additional
  index-generation cautions in `GPTs/attachments/03_sql_ddl_generation.md`. No direct
  J013 change was required in `GPTs/attachments/04_sql_dml_oracle_compatibility.md`
  because DML hint placement is covered in the tuning attachment. The shared syntax
  queue remains open for J014-J016 and later specialized SQL families.
- J014 update: The user, privilege, role, sequence, synonym, view, materialized view,
  directory, trigger, and job SQL family is source-audited and expanded in
  `GPTs/attachments/03_sql_ddl_generation.md`, with supporting metadata checks and
  object blocks in `GPTs/attachments/06_data_dictionary_performance_views.md`. The
  shared syntax queue remains open for J015-J016 and later specialized SQL families.
- J015 update: The DML, query expression, function, condition, operator, and 8.1 JSON
  SQL family is source-audited and expanded in
  `GPTs/attachments/04_sql_dml_oracle_compatibility.md`, with JSON data type
  cross-reference support in `GPTs/attachments/05_data_types_properties.md` and
  migration rewrite cautions in
  `GPTs/attachments/15_migration_oracle_compatibility.md`. The shared syntax queue
  remains open for later specialized SQL families.
- J016 update: The replication, Log Analyzer, property/session, transaction, and
  administrative control SQL family is source-audited and expanded in
  `GPTs/attachments/03_sql_ddl_generation.md`, with matching replication option syntax
  in `GPTs/attachments/09_replication_ha_cdc.md` and a completion note in
  `GPTs/reports/sql_syntax_inventory.md`. The update keeps 8.1 `IF EXISTS` and
  `IF NOT EXISTS` boundaries, separates ordinary replication, SSL replication, and Log
  Analyzer forms, adds receive-only and offline replication SQL generation guardrails,
  and corrects `ALTER SESSION SET REPLICATION` to `{DEFAULT | NONE}` only.
