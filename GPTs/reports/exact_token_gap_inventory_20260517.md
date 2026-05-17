# Altibase Exact Token Gap Inventory

- Job: `J003`
- Status: complete source-check inventory; no attachment remediation in this job
- Date: 2026-05-17
- Evidence run: `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_095919/`
- Primary inputs: `judgments.jsonl`, `answers.jsonl`, `aggregate_report.json`, `summary.txt`, `evals/altibase_answerability/questions/*.jsonl`, and the selected source paths listed in each question record

## Reconfirmed Requirement And Boundary

J003 source-checks required literal tokens that the 2026-05-17 benchmark classed as absent from the attachment set or weakly retrievable, then records a prioritized inventory before any `GPTs/attachments/` edits.

This job is limited to evidence and report work:

- Added: `GPTs/reports/exact_token_gap_inventory_20260517.md`
- Read-only evidence: benchmark run artifacts, durable question JSONL files, selected local sources, and current `GPTs/attachments/*.md`
- Not changed: `GPTs/attachments/*.md`, original manuals/source documents, benchmark thresholds, or benchmark expected questions

## Design Note

This report changes documentation structure only by adding a durable J003 inventory. It does not add or broaden any Altibase product behavior. Later remediation jobs must still open the listed selected source files before editing customer-facing attachments, especially where this inventory marks a token as a source-normalization candidate rather than an exact source-string hit.

The inventory keeps the four fix classes from J001/J002:

- `content gap`: token was missed by the answer and was not matchable in the full current attachment set.
- `retrieval gap`: token exists in full attachments but was not selected into the reproduced lexical context for that question.
- `answer synthesis gap`: token was present in selected context but the answer omitted it.
- `judge calibration candidate`: no confirmed judge-only issue here; only source-normalization candidates are listed for later calibration after source text and answer path are checked.

## Method

- Replayed `answer_runner.py` lexical retrieval with `max_context_chars=180000` and `chunk_chars=8000`; context digest mismatches: `0`.
- Classified each missed required token with the same `literal_token_present` matcher used by `judge_report.py`.
- Source-checked content and retrieval tokens against each question record's `source_refs[].source_path`; exact source hits use the same literal matcher.
- Treated a token with no exact source-string hit as a source-normalization candidate, not as unsupported. These candidates need manual wording checks in their later domain jobs.

## Evidence Snapshot

| Metric | Value |
| --- | ---: |
| Passed / total | `27 / 270` |
| Required-token preservation | `74.6%` |
| Missed required-token instances | `525` |
| Content-gap token instances | `110` |
| Retrieval-gap token instances | `105` |
| Answer-synthesis token instances | `310` |
| Unique content-gap tokens | `109` |
| Unique retrieval-gap tokens | `97` |
| Unique answer-synthesis tokens | `252` |

## Source-Check Summary

| Class | Missed instances | Unique tokens | Exact hits in selected source refs | Read |
| --- | ---: | ---: | ---: | --- |
| `content gap` | `110` | `109` | `98` | add or strengthen source-backed attachment blocks |
| `retrieval gap` | `105` | `97` | `98` | add aliases/headings/indexes/cross-links |
| `answer synthesis gap` | `310` | `252` | `273` | preserve exact tokens in answer-ready item blocks and GPT instructions |

For the J003 scope, the direct source-check focus is the `content gap` plus `retrieval gap` set: `215` missed token instances. `196` of those instances have exact source-string hits in the question-selected sources. The remaining `19` are not safe to treat as unsupported; most are English-normalized phrases, escaped Markdown/path forms, compact placeholders, or numeric notation variants that need manual wording checks in their later domain jobs.

## Domain Distribution

| Domain | Content | Retrieval | Synthesis | Next remediation jobs | Main target attachments |
| --- | ---: | ---: | ---: | --- | --- |
| `errors_troubleshooting` | `8` | `15` | `29` | `J010` | `07_error_messages_troubleshooting.md`, `13_isql_iloader_basic_tools.md`, `14_utilities_operation_tools.md` |
| `operations_admin` | `15` | `14` | `45` | `J011-J012` | `01_getting_started_installation.md`, `02_administration_operations.md`, `03_sql_ddl_generation.md`, `07_error_messages_troubleshooting.md`, `13_isql_iloader_basic_tools.md` |
| `properties` | `9` | `23` | `56` | `J004-J007` | `05_data_types_properties.md`, related `00`, `02`, `06`, `08`, `09`, `18` |
| `replication_cdc_security_network` | `20` | `10` | `42` | `J013-J014` | `09_replication_ha_cdc.md`, `03_sql_ddl_generation.md`, `06_data_dictionary_performance_views.md`, `16_dblink_external_connectors.md`, `18_security_ssl_tls.md` |
| `sql_ddl_dml_datatypes` | `24` | `18` | `56` | `J008-J009` | `03_sql_ddl_generation.md`, `04_sql_dml_oracle_compatibility.md`, `05_data_types_properties.md`, `15_migration_oracle_compatibility.md` |
| `tools_apis_connectors_migration` | `15` | `12` | `35` | `J016-J017` | `10_psm_stored_external_procedures.md`, `11_java_jdbc_spring.md`, `12_c_cli_odbc_precompiler.md`, `13_isql_iloader_basic_tools.md`, `14_utilities_operation_tools.md`, `15_migration_oracle_compatibility.md`, `16_dblink_external_connectors.md`, `17_kubernetes_aku_cloud.md`, `19_spatial_nifi_tableau_misc.md` |
| `views_performance_monitoring` | `19` | `13` | `47` | `J015` | `06_data_dictionary_performance_views.md`, `08_performance_tuning_monitoring.md` |

## Priority Rules

- `P0`: exact source-backed content gap in a blocker, protected-topic, or zero-pass subdomain path. Add an answer-ready source-backed block in the owning later job.
- `P1`: exact source-backed content gap without protected/blocker amplification, or retrieval gap in a blocker/protected/zero-pass path. Add the missing item block or retrieval alias/index.
- `P2`: lower-risk retrieval gap or answer-synthesis gap. Preserve exact tokens through compact item blocks, answer contract, and later retrieval cleanup.
- `P3`: source-normalization or calibration candidate. Do not edit attachments from the benchmark token alone; inspect the selected source wording first.

## Highest Priority Syntax And Command Tokens

These are syntax-shaped tokens from the content/retrieval set that later attachment jobs should check first because they affect generated SQL, operational commands, or exact command examples.

| Priority | Class | Token | Questions | Next jobs | Source check |
| --- | --- | --- | --- | --- | --- |
| `P0` | `content gap` | `ALTER DATABASE db_name META RESETLOGS` | `OPS-117` | `J011-J012` | exact source hit 1/1 |
| `P0` | `content gap` | `ALTER DATABASE dbname SERVICE` | `OPS-125` | `J011-J012` | exact source hit 1/1 |
| `P0` | `content gap` | `ALTER SESSION SET AUTOCOMMIT = FALSE` | `PROP-129` | `J004-J007` | exact source hit 1/1 |
| `P0` | `content gap` | `ALTER TABLE ADD PARTITION` | `SQL-108` | `J008-J009` | exact source hit 1/1 |
| `P0` | `content gap` | `arg1` | `SQL-136` | `J008-J009` | exact source hit 1/1 |
| `P0` | `content gap` | `CREATE DISK TABLESPACE` | `SQL-104` | `J008-J009` | exact source hit 1/1 |
| `P0` | `content gap` | `CREATE VOLATILE TABLESPACE` | `SQL-103` | `J008-J009` | exact source hit 1/1 |
| `P0` | `content gap` | `Database-Level Backup Completed [SUCCESS]` | `OPS-127` | `J011-J012` | exact source hit 1/1 |
| `P0` | `content gap` | `full table scan` | `VPM-116` | `J015` | exact source hit 1/1 |
| `P0` | `content gap` | `inplace update` | `PROP-122` | `J004-J007` | exact source hit 1/1 |
| `P0` | `content gap` | `multiple_update` | `SQL-121` | `J008-J009` | exact source hit 1/1 |
| `P0` | `content gap` | `NON-AUTOCOMMIT` | `SQL-124` | `J008-J009` | exact source hit 1/1 |
| `P0` | `content gap` | `occurrence` | `SQL-138` | `J008-J009` | exact source hit 1/1 |
| `P0` | `content gap` | `POSIX Basic Regular Expression` | `SQL-138` | `J008-J009` | exact source hit 1/1 |
| `P0` | `content gap` | `replace_string` | `SQL-138` | `J008-J009` | exact source hit 1/1 |
| `P0` | `content gap` | `replication_host_ip` | `SQL-141` | `J008-J009` | exact source hit 1/1 |
| `P0` | `content gap` | `replication_host_port_no` | `SQL-141` | `J008-J009` | exact source hit 1/1 |
| `P0` | `content gap` | `table_compression_clause` | `SQL-110` | `J008-J009` | exact source hit 1/1 |
| `P1` | `content gap` | `0-9` | `SQL-142` | `J008-J009` | exact source hit 1/1 |
| `P1` | `content gap` | `2,147,483,648` | `SQL-130` | `J008-J009` | exact source hit 1/1 |
| `P1` | `content gap` | `A-Z` | `SQL-142` | `J008-J009` | exact source hit 1/1 |
| `P1` | `content gap` | `a-z` | `SQL-142` | `J008-J009` | exact source hit 1/1 |
| `P1` | `content gap` | `Anti Join` | `SQL-143` | `J008-J009` | exact source hit 1/1 |
| `P1` | `content gap` | `D$` | `SQL-142` | `J008-J009` | exact source hit 1/1 |
| `P1` | `content gap` | `ISO/IEC 19075-6(2021)` | `SQL-130` | `J008-J009` | exact source hit 1/1 |
| `P1` | `content gap` | `no_rows_insert_clause` | `SQL-123` | `J008-J009` | exact source hit 1/1 |
| `P1` | `content gap` | `Oracle Database 10gR2` | `TOOL-037` | `J016-J017` | exact source hit 1/1 |
| `P1` | `content gap` | `Semi Join` | `SQL-143` | `J008-J009` | exact source hit 1/1 |
| `P1` | `content gap` | `That had return update result` | `VPM-130` | `J015` | exact source hit 1/1 |
| `P1` | `content gap` | `X$` | `SQL-142` | `J008-J009` | exact source hit 1/1 |
| `P3` | `content gap` | `/*+ hint */` | `VPM-120` | `J015` | no exact source-string hit; inspect source wording |
| `P3` | `content gap` | `40 bytes` | `SQL-142` | `J008-J009` | no exact source-string hit; inspect source wording |
| `P3` | `content gap` | `CREATE USER system privilege` | `OPS-108` | `J011-J012` | no exact source-string hit; inspect source wording |
| `P3` | `content gap` | `hybrid database` | `OPS-119` | `J011-J012` | no exact source-string hit; inspect source wording |
| `P3` | `content gap` | `LOB(column_name)` | `SQL-111` | `J008-J009` | no exact source-string hit; inspect source wording |
| `P3` | `content gap` | `rollback-p<patch_version>` | `OPS-129` | `J011-J012` | no exact source-string hit; inspect source wording |
| `P1` | `retrieval gap` | `CREATE FUNCTION` | `TOOL-002`, `TOOL-007` | `J016-J017` | exact source hit 2/2 |
| `P1` | `retrieval gap` | `8-byte` | `SQL-106` | `J008-J009` | no exact source-string hit; inspect source wording |
| `P1` | `retrieval gap` | `alias` | `SQL-110` | `J008-J009` | exact source hit 1/1 |
| `P1` | `retrieval gap` | `CREATE INDEX` | `SQL-105` | `J008-J009` | exact source hit 1/1 |
| `P1` | `retrieval gap` | `CREATE PROCEDURE` | `TOOL-002` | `J016-J017` | exact source hit 1/1 |
| `P1` | `retrieval gap` | `CREATE SEQUENCE` | `SQL-114` | `J008-J009` | exact source hit 1/1 |
| `P1` | `retrieval gap` | `expr1` | `SQL-136` | `J008-J009` | exact source hit 1/1 |
| `P1` | `retrieval gap` | `full outer join` | `SQL-121` | `J008-J009` | exact source hit 1/1 |
| `P1` | `retrieval gap` | `join condition` | `SQL-129` | `J008-J009` | exact source hit 1/1 |

## Content Gap Token Inventory

All tokens in this section were missed by the answer and were not matchable in the full current attachment set. Later jobs should add them only after opening the selected sources named by the question records.

| Priority | Token | Instances | Questions | Domain/subdomain | Next jobs | Source check |
| --- | --- | ---: | --- | --- | --- | --- |
| `P0` | `0x31010` | `1` | `ERR-116` | `sql_property_errors` | `J010` | exact source hit 1/1 |
| `P0` | `0x31011` | `1` | `ERR-116` | `sql_property_errors` | `J010` | exact source hit 1/1 |
| `P0` | `0x31012` | `1` | `ERR-116` | `sql_property_errors` | `J010` | exact source hit 1/1 |
| `P0` | `0x31013` | `1` | `ERR-116` | `sql_property_errors` | `J010` | exact source hit 1/1 |
| `P0` | `0x31014` | `1` | `ERR-116` | `sql_property_errors` | `J010` | exact source hit 1/1 |
| `P0` | `0x31017` | `1` | `ERR-116` | `sql_property_errors` | `J010` | exact source hit 1/1 |
| `P0` | `1000MB` | `1` | `PROP-122` | `locking_and_update_behavior` | `J004-J007` | exact source hit 1/1 |
| `P0` | `10M` | `1` | `PROP-117` | `result_cache` | `J004-J007` | exact source hit 1/1 |
| `P0` | `ACT_REPL_MODE` | `1` | `REPL-102` | `replication_topology_states` | `J013-J014` | exact source hit 1/1 |
| `P0` | `ALA_FAILURE` | `1` | `REPL-115` | `cdc_log_analyzer_repmgr` | `J013-J014` | exact source hit 1/1 |
| `P0` | `ALTER DATABASE db_name META RESETLOGS` | `1` | `OPS-117` | `backup_restore_recovery` | `J011-J012` | exact source hit 1/1 |
| `P0` | `ALTER DATABASE dbname SERVICE` | `1` | `OPS-125` | `datafile_log_operations` | `J011-J012` | exact source hit 1/1 |
| `P0` | `ALTER SESSION SET AUTOCOMMIT = FALSE` | `1` | `PROP-129` | `transactions` | `J004-J007` | exact source hit 1/1 |
| `P0` | `ALTER TABLE ADD PARTITION` | `1` | `SQL-108` | `ddl_generation` | `J008-J009` | exact source hit 1/1 |
| `P0` | `arg1` | `1` | `SQL-136` | `dml_expressions_functions` | `J008-J009` | exact source hit 1/1 |
| `P0` | `August 31, 2023` | `1` | `REPL-128` | `version_patch_replication_caveats` | `J013-J014` | exact source hit 1/1 |
| `P0` | `BUG-45946` | `1` | `REPL-126` | `version_patch_replication_caveats` | `J013-J014` | exact source hit 1/1 |
| `P0` | `BUG-50573` | `1` | `REPL-128` | `version_patch_replication_caveats` | `J013-J014` | exact source hit 1/1 |
| `P0` | `CREATE DISK TABLESPACE` | `1` | `SQL-104` | `ddl_generation` | `J008-J009` | exact source hit 1/1 |
| `P0` | `CREATE VOLATILE TABLESPACE` | `1` | `SQL-103` | `ddl_generation` | `J008-J009` | exact source hit 1/1 |
| `P0` | `Database-Level Backup Completed [SUCCESS]` | `1` | `OPS-127` | `datafile_log_operations` | `J011-J012` | exact source hit 1/1 |
| `P0` | `DENY` | `1` | `PROP-142` | `access_control` | `J004-J007` | exact source hit 1/1 |
| `P0` | `Different replication protocols` | `1` | `REPL-127` | `version_patch_replication_caveats` | `J013-J014` | exact source hit 1/1 |
| `P0` | `ERR-61186` | `1` | `REPL-127` | `version_patch_replication_caveats` | `J013-J014` | exact source hit 1/1 |
| `P0` | `FIXED KEY RANGE` | `1` | `VPM-118` | `optimizer_plan_tuning` | `J015` | exact source hit 1/1 |
| `P0` | `full table scan` | `1` | `VPM-116` | `optimizer_plan_tuning` | `J015` | exact source hit 1/1 |
| `P0` | `GC_ALREADY_SYNC_COUNT` | `1` | `VPM-112` | `performance_views_check_sql` | `J015` | exact source hit 1/1 |
| `P0` | `Handshaking` | `1` | `PROP-138` | `replication_sql_apply` | `J004-J007` | exact source hit 1/1 |
| `P0` | `inplace update` | `1` | `PROP-122` | `locking_and_update_behavior` | `J004-J007` | exact source hit 1/1 |
| `P0` | `Master-Slave Scheme` | `1` | `REPL-103` | `replication_topology_states` | `J013-J014` | exact source hit 1/1 |
| `P0` | `multiple_update` | `1` | `SQL-121` | `dml_expressions_functions` | `J008-J009` | exact source hit 1/1 |
| `P0` | `NNF` | `1` | `PROP-120` | `optimizer_normalization` | `J004-J007` | exact source hit 1/1 |
| `P0` | `NON-AUTOCOMMIT` | `1` | `SQL-124` | `syntax_restrictions_examples` | `J008-J009` | exact source hit 1/1 |
| `P0` | `occurrence` | `1` | `SQL-138` | `dml_expressions_functions` | `J008-J009` | exact source hit 1/1 |
| `P0` | `PERMIT` | `1` | `PROP-142` | `access_control` | `J004-J007` | exact source hit 1/1 |
| `P0` | `POSIX Basic Regular Expression` | `1` | `SQL-138` | `dml_expressions_functions` | `J008-J009` | exact source hit 1/1 |
| `P0` | `PRE-PROCESS` | `1` | `OPS-103` | `installation_startup_shutdown` | `J011-J012` | exact source hit 1/1 |
| `P0` | `PRE_PROCESS` | `1` | `OPS-103` | `installation_startup_shutdown` | `J011-J012` | exact source hit 1/1 |
| `P0` | `recvq` | `1` | `REPL-118` | `compatibility_network_diagnostics` | `J013-J014` | exact source hit 1/1 |
| `P0` | `replace_string` | `1` | `SQL-138` | `dml_expressions_functions` | `J008-J009` | exact source hit 1/1 |
| `P0` | `replication_host_ip` | `1` | `SQL-141` | `replication_admin_sql` | `J008-J009` | exact source hit 1/1 |
| `P0` | `replication_host_port_no` | `1` | `SQL-141` | `replication_admin_sql` | `J008-J009` | exact source hit 1/1 |
| `P0` | `ReplicationManager_1.4.0-linux.gtk.x86.zip` | `1` | `REPL-128` | `version_patch_replication_caveats` | `J013-J014` | exact source hit 1/1 |
| `P0` | `ReplicationManager_1.4.0-win32.win32.x86.zip` | `1` | `REPL-128` | `version_patch_replication_caveats` | `J013-J014` | exact source hit 1/1 |
| `P0` | `restartXSN` | `1` | `REPL-129` | `version_patch_replication_caveats` | `J013-J014` | exact source hit 1/1 |
| `P0` | `sendq` | `1` | `REPL-118` | `compatibility_network_diagnostics` | `J013-J014` | exact source hit 1/1 |
| `P0` | `SERVER SHUTDOWN` | `1` | `VPM-114` | `performance_views_check_sql` | `J015` | exact source hit 1/1 |
| `P0` | `SERVER STARTED` | `1` | `VPM-114` | `performance_views_check_sql` | `J015` | exact source hit 1/1 |
| `P0` | `START_FLAG` | `1` | `REPL-106` | `replication_state_changes` | `J013-J014` | exact source hit 1/1 |
| `P0` | `t1.dat` | `1` | `OPS-114` | `backup_restore_recovery` | `J011-J012` | exact source hit 1/1 |
| `P0` | `t1.fmt` | `1` | `OPS-114` | `backup_restore_recovery` | `J011-J012` | exact source hit 1/1 |
| `P0` | `table_compression_clause` | `1` | `SQL-110` | `syntax_restrictions_examples` | `J008-J009` | exact source hit 1/1 |
| `P0` | `TCP Dup ACK` | `1` | `REPL-118` | `compatibility_network_diagnostics` | `J013-J014` | exact source hit 1/1 |
| `P0` | `ULONG MAX` | `1` | `PROP-117` | `result_cache` | `J004-J007` | exact source hit 1/1 |
| `P0` | `UPDATE_TX_COUNT` | `1` | `VPM-112` | `performance_views_check_sql` | `J015` | exact source hit 1/1 |
| `P0` | `User-Oriented Scheme` | `1` | `REPL-103` | `replication_topology_states` | `J013-J014` | exact source hit 1/1 |
| `P0` | `v$repreceiver` | `1` | `REPL-118` | `compatibility_network_diagnostics` | `J013-J014` | exact source hit 1/1 |
| `P0` | `VARIABLE KEY RANGE` | `1` | `VPM-118` | `optimizer_plan_tuning` | `J015` | exact source hit 1/1 |
| `P0` | `wireshark` | `1` | `REPL-118` | `compatibility_network_diagnostics` | `J013-J014` | exact source hit 1/1 |
| `P1` | `0x4102E` | `2` | `ERR-101`, `TOOL-036` | `tool_driver_errors`, `utilities_datacompj` | `J010`, `J016-J017` | exact source hit 2/2 |
| `P1` | `(database1:20300, database2:20300)` | `1` | `TOOL-010` | `jdbc_java_spring_hibernate` | `J016-J017` | exact source hit 1/1 |
| `P1` | `0-9` | `1` | `SQL-142` | `oracle_differences` | `J008-J009` | exact source hit 1/1 |
| `P1` | `100MBytes` | `1` | `TOOL-047` | `spatial_nifi_tableau` | `J016-J017` | exact source hit 1/1 |
| `P1` | `2,147,483,648` | `1` | `SQL-130` | `datatypes_json_lob` | `J008-J009` | exact source hit 1/1 |
| `P1` | `7.1.0.7.9` | `1` | `VPM-130` | `version_sensitive_view_availability` | `J015` | exact source hit 1/1 |
| `P1` | `A-Z` | `1` | `SQL-142` | `oracle_differences` | `J008-J009` | exact source hit 1/1 |
| `P1` | `a-z` | `1` | `SQL-142` | `oracle_differences` | `J008-J009` | exact source hit 1/1 |
| `P1` | `Altibase 5.5.1` | `1` | `VPM-123` | `monitoring_api_snmp` | `J015` | exact source hit 1/1 |
| `P1` | `Anti Join` | `1` | `SQL-143` | `oracle_differences` | `J008-J009` | exact source hit 1/1 |
| `P1` | `B-TREE` | `1` | `VPM-104` | `dictionary_meta_tables` | `J015` | exact source hit 1/1 |
| `P1` | `D$` | `1` | `SQL-142` | `oracle_differences` | `J008-J009` | exact source hit 1/1 |
| `P1` | `DOWNGRADE` | `1` | `OPS-130` | `platform_upgrade_cautions` | `J011-J012` | exact source hit 1/1 |
| `P1` | `ERR-00015` | `1` | `TOOL-036` | `utilities_datacompj` | `J016-J017` | exact source hit 1/1 |
| `P1` | `GNU glibc 2.12 ~ 2.33` | `1` | `OPS-128` | `platform_upgrade_cautions` | `J011-J012` | exact source hit 1/1 |
| `P1` | `ISO/IEC 19075-6(2021)` | `1` | `SQL-130` | `datatypes_json_lob` | `J008-J009` | exact source hit 1/1 |
| `P1` | `jdbc:Altibase://localhost:20300/mydb?fetch_enough=0&time_zone=DB_TZ` | `1` | `TOOL-009` | `jdbc_java_spring_hibernate` | `J016-J017` | exact source hit 1/1 |
| `P1` | `long-term lock` | `1` | `ERR-109` | `symptom_log_collection` | `J010` | exact source hit 1/1 |
| `P1` | `no_rows_insert_clause` | `1` | `SQL-123` | `oracle_differences` | `J008-J009` | exact source hit 1/1 |
| `P1` | `Oracle Database 10gR2` | `1` | `TOOL-037` | `migration_oracle_adapter` | `J016-J017` | exact source hit 1/1 |
| `P1` | `PARTITION_MAX_VALUE` | `1` | `VPM-106` | `dictionary_meta_tables` | `J015` | exact source hit 1/1 |
| `P1` | `PARTITION_MIN_VALUE` | `1` | `VPM-106` | `dictionary_meta_tables` | `J015` | exact source hit 1/1 |
| `P1` | `PARTITION_ORDER` | `1` | `VPM-106` | `dictionary_meta_tables` | `J015` | exact source hit 1/1 |
| `P1` | `PARTITION_USABLE` | `1` | `VPM-106` | `dictionary_meta_tables` | `J015` | exact source hit 1/1 |
| `P1` | `R-TREE` | `1` | `VPM-104` | `dictionary_meta_tables` | `J015` | exact source hit 1/1 |
| `P1` | `Semi Join` | `1` | `SQL-143` | `oracle_differences` | `J008-J009` | exact source hit 1/1 |
| `P1` | `setPoolable` | `1` | `TOOL-013` | `jdbc_java_spring_hibernate` | `J016-J017` | exact source hit 1/1 |
| `P1` | `SPOOL filename` | `1` | `TOOL-025` | `isql_iloader` | `J016-J017` | exact source hit 1/1 |
| `P1` | `sqlerrm.sqlerrmc` | `1` | `TOOL-022` | `c_cli_odbc_precompiler` | `J016-J017` | exact source hit 1/1 |
| `P1` | `sqlerrm.sqlerrml` | `1` | `TOOL-022` | `c_cli_odbc_precompiler` | `J016-J017` | exact source hit 1/1 |
| `P1` | `sqlwarn` | `1` | `TOOL-022` | `c_cli_odbc_precompiler` | `J016-J017` | exact source hit 1/1 |
| `P1` | `TableauDesktop-64bit-2021-4-4` | `1` | `TOOL-050` | `spatial_nifi_tableau` | `J016-J017` | exact source hit 1/1 |
| `P1` | `test.bad` | `1` | `TOOL-028` | `isql_iloader` | `J016-J017` | exact source hit 1/1 |
| `P1` | `test.log` | `1` | `TOOL-028` | `isql_iloader` | `J016-J017` | exact source hit 1/1 |
| `P1` | `That had return update result` | `1` | `VPM-130` | `version_sensitive_view_availability` | `J015` | exact source hit 1/1 |
| `P1` | `Unix Domain Socket` | `1` | `VPM-123` | `monitoring_api_snmp` | `J015` | exact source hit 1/1 |
| `P1` | `Unsigned Integer` | `1` | `REPL-112` | `security_tls_replication_ssl` | `J013-J014` | exact source hit 1/1 |
| `P1` | `X$` | `1` | `SQL-142` | `oracle_differences` | `J008-J009` | exact source hit 1/1 |
| `P3` | `$ALTIBASE_HOME/trc/altibase_qp.log` | `1` | `OPS-130` | `platform_upgrade_cautions` | `J011-J012` | no exact source-string hit; inspect source wording |
| `P3` | `/*+ hint */` | `1` | `VPM-120` | `optimizer_plan_tuning` | `J015` | no exact source-string hit; inspect source wording |
| `P3` | `40 bytes` | `1` | `SQL-142` | `oracle_differences` | `J008-J009` | no exact source-string hit; inspect source wording |
| `P3` | `backup-time metadata` | `1` | `OPS-134` | `admin_runbook_safety` | `J011-J012` | no exact source-string hit; inspect source wording |
| `P3` | `C:\Program Files\Tableau\Drivers` | `1` | `TOOL-050` | `spatial_nifi_tableau` | `J016-J017` | no exact source-string hit; inspect source wording |
| `P3` | `CREATE USER system privilege` | `1` | `OPS-108` | `accounts_tablespaces_admin` | `J011-J012` | no exact source-string hit; inspect source wording |
| `P3` | `current loganchor` | `1` | `OPS-118` | `backup_restore_recovery` | `J011-J012` | no exact source-string hit; inspect source wording |
| `P3` | `hybrid database` | `1` | `OPS-119` | `backup_restore_recovery` | `J011-J012` | no exact source-string hit; inspect source wording |
| `P3` | `Intel Linux` | `1` | `REPL-123` | `security_tls_replication_ssl` | `J013-J014` | no exact source-string hit; inspect source wording |
| `P3` | `LOB(column_name)` | `1` | `SQL-111` | `datatypes_json_lob` | `J008-J009` | no exact source-string hit; inspect source wording |
| `P3` | `optimizer-related properties` | `1` | `VPM-115` | `optimizer_plan_tuning` | `J015` | no exact source-string hit; inspect source wording |
| `P3` | `rollback-p<patch_version>` | `1` | `OPS-129` | `platform_upgrade_cautions` | `J011-J012` | no exact source-string hit; inspect source wording |

## Retrieval Gap Token Inventory

All tokens in this section exist somewhere in full attachments but were not selected into the reproduced lexical context for the failed question. Later jobs should prefer searchable aliases, exact headings, compact indexes, and cross-links over duplicating long prose.

| Priority | Token | Instances | Questions | Domain/subdomain | Next jobs | Source check |
| --- | --- | ---: | --- | --- | --- | --- |
| `P1` | `2097152` | `3` | `PROP-108`, `PROP-109`, `PROP-110` | `disk_database_limits`, `memory_database_limits`, `volatile_database_limits` | `J004-J007` | exact source hit 3/3 |
| `P1` | `2^32 + 1` | `2` | `PROP-108`, `PROP-110` | `memory_database_limits`, `volatile_database_limits` | `J004-J007` | no exact source-string hit; inspect source wording |
| `P1` | `CREATE FUNCTION` | `2` | `TOOL-002`, `TOOL-007` | `psm_external_procedures` | `J016-J017` | exact source hit 2/2 |
| `P1` | `CREATE_LSN_FILENO` | `2` | `OPS-113`, `OPS-123` | `accounts_tablespaces_admin`, `datafile_log_operations` | `J011-J012` | exact source hit 2/2 |
| `P1` | `STOREDCOUNT` | `2` | `PROP-104`, `PROP-105` | `database_file_paths` | `J004-J007` | exact source hit 2/2 |
| `P1` | `SYS_TBS_DISK_TEMP` | `2` | `OPS-111`, `OPS-125` | `accounts_tablespaces_admin`, `datafile_log_operations` | `J011-J012` | exact source hit 2/2 |
| `P1` | `VALUE8` | `2` | `PROP-104`, `PROP-105` | `database_file_paths` | `J004-J007` | exact source hit 2/2 |
| `P1` | `$ALTIBASE_HOME/dbs1` | `1` | `OPS-110` | `accounts_tablespaces_admin` | `J011-J012` | exact source hit 1/1 |
| `P1` | `'.,'` | `1` | `PROP-124` | `session_locale` | `J004-J007` | exact source hit 1/1 |
| `P1` | `1000` | `1` | `PROP-112` | `connection_limits` | `J004-J007` | exact source hit 1/1 |
| `P1` | `135277` | `1` | `ERR-124` | `sql_property_errors` | `J010` | exact source hit 1/1 |
| `P1` | `16777216` | `1` | `PROP-144` | `temporary_lob_memory` | `J004-J007` | exact source hit 1/1 |
| `P1` | `2147483648` | `1` | `PROP-144` | `temporary_lob_memory` | `J004-J007` | exact source hit 1/1 |
| `P1` | `2^31` | `1` | `PROP-108` | `memory_database_limits` | `J004-J007` | no exact source-string hit; inspect source wording |
| `P1` | `4000` | `1` | `PROP-148` | `aggregate_function_limits` | `J004-J007` | exact source hit 1/1 |
| `P1` | `4096` | `1` | `PROP-117` | `result_cache` | `J004-J007` | exact source hit 1/1 |
| `P1` | `7.4.4` | `1` | `REPL-129` | `version_patch_replication_caveats` | `J013-J014` | exact source hit 1/1 |
| `P1` | `7.4.5` | `1` | `REPL-129` | `version_patch_replication_caveats` | `J013-J014` | exact source hit 1/1 |
| `P1` | `8-byte` | `1` | `SQL-106` | `ddl_generation` | `J008-J009` | no exact source-string hit; inspect source wording |
| `P1` | `ACCESS_LIST_FILE` | `1` | `PROP-142` | `access_control` | `J004-J007` | exact source hit 1/1 |
| `P1` | `alias` | `1` | `SQL-110` | `syntax_restrictions_examples` | `J008-J009` | exact source hit 1/1 |
| `P1` | `Autocommit` | `1` | `REPL-115` | `cdc_log_analyzer_repmgr` | `J013-J014` | exact source hit 1/1 |
| `P1` | `CHECKPOINT_INTERVAL_IN_LOG` | `1` | `PROP-131` | `checkpoint` | `J004-J007` | exact source hit 1/1 |
| `P1` | `CHECKPOINT_INTERVAL_IN_SEC` | `1` | `PROP-131` | `checkpoint` | `J004-J007` | exact source hit 1/1 |
| `P1` | `CREATE INDEX` | `1` | `SQL-105` | `ddl_generation` | `J008-J009` | exact source hit 1/1 |
| `P1` | `CREATE PROCEDURE` | `1` | `TOOL-002` | `psm_external_procedures` | `J016-J017` | exact source hit 1/1 |
| `P1` | `CREATE SEQUENCE` | `1` | `SQL-114` | `syntax_restrictions_examples` | `J008-J009` | exact source hit 1/1 |
| `P1` | `CURRSIZE` | `1` | `OPS-113` | `accounts_tablespaces_admin` | `J011-J012` | exact source hit 1/1 |
| `P1` | `END;` | `1` | `TOOL-003` | `psm_external_procedures` | `J016-J017` | exact source hit 1/1 |
| `P1` | `expr1` | `1` | `SQL-136` | `dml_expressions_functions` | `J008-J009` | exact source hit 1/1 |
| `P1` | `fallocate()` | `1` | `PROP-134` | `log_creation` | `J004-J007` | exact source hit 1/1 |
| `P1` | `full outer join` | `1` | `SQL-121` | `dml_expressions_functions` | `J008-J009` | exact source hit 1/1 |
| `P1` | `join condition` | `1` | `SQL-129` | `datatypes_json_lob` | `J008-J009` | exact source hit 1/1 |
| `P1` | `Logical Plan Generator` | `1` | `VPM-115` | `optimizer_plan_tuning` | `J015` | exact source hit 1/1 |
| `P1` | `NET_ERROR_FLAG` | `1` | `REPL-106` | `replication_state_changes` | `J013-J014` | exact source hit 1/1 |
| `P1` | `NLS_TERRITORY` | `1` | `PROP-124` | `session_locale` | `J004-J007` | exact source hit 1/1 |
| `P1` | `OPENED` | `1` | `OPS-113` | `accounts_tablespaces_admin` | `J011-J012` | exact source hit 1/1 |
| `P1` | `Physical Plan Generator` | `1` | `VPM-115` | `optimizer_plan_tuning` | `J015` | exact source hit 1/1 |
| `P1` | `Propagation` | `1` | `REPL-126` | `version_patch_replication_caveats` | `J013-J014` | exact source hit 1/1 |
| `P1` | `QUERY` | `1` | `VPM-108` | `performance_views_check_sql` | `J015` | exact source hit 1/1 |
| `P1` | `Query Rewriter` | `1` | `VPM-115` | `optimizer_plan_tuning` | `J015` | exact source hit 1/1 |
| `P1` | `Replication Gap` | `1` | `REPL-102` | `replication_topology_states` | `J013-J014` | exact source hit 1/1 |
| `P1` | `SID` | `1` | `VPM-108` | `performance_views_check_sql` | `J015` | exact source hit 1/1 |
| `P1` | `SQL hints` | `1` | `VPM-115` | `optimizer_plan_tuning` | `J015` | no exact source-string hit; inspect source wording |
| `P1` | `STATUS` | `1` | `REPL-106` | `replication_state_changes` | `J013-J014` | exact source hit 1/1 |
| `P1` | `SYS_TBS_DISK_DATA` | `1` | `OPS-111` | `accounts_tablespaces_admin` | `J011-J012` | exact source hit 1/1 |
| `P1` | `SYS_TBS_MEM_DATA` | `1` | `OPS-111` | `accounts_tablespaces_admin` | `J011-J012` | exact source hit 1/1 |
| `P1` | `tcpdump` | `1` | `REPL-118` | `compatibility_network_diagnostics` | `J013-J014` | exact source hit 1/1 |
| `P1` | `TRANS_ID` | `1` | `VPM-108` | `performance_views_check_sql` | `J015` | exact source hit 1/1 |
| `P1` | `TX_ID` | `1` | `VPM-108` | `performance_views_check_sql` | `J015` | exact source hit 1/1 |
| `P1` | `V$ACCESS_LIST` | `1` | `PROP-142` | `access_control` | `J004-J007` | exact source hit 1/1 |
| `P1` | `WAIT_CLASS` | `1` | `VPM-108` | `performance_views_check_sql` | `J015` | exact source hit 1/1 |
| `P1` | `WAIT_FOR_TRANS_ID` | `1` | `VPM-108` | `performance_views_check_sql` | `J015` | exact source hit 1/1 |
| `P1` | `write()` | `1` | `PROP-134` | `log_creation` | `J004-J007` | exact source hit 1/1 |
| `P1` | `XSN` | `1` | `REPL-129` | `version_patch_replication_caveats` | `J013-J014` | exact source hit 1/1 |
| `P2` | `0x0001F` | `1` | `ERR-106` | `high_risk_operations_errors` | `J010` | exact source hit 1/1 |
| `P2` | `0x311B1` | `1` | `ERR-117` | `high_risk_operations_errors` | `J010` | exact source hit 1/1 |
| `P2` | `0x31293` | `1` | `ERR-117` | `high_risk_operations_errors` | `J010` | exact source hit 1/1 |
| `P2` | `0x4107C` | `1` | `ERR-117` | `high_risk_operations_errors` | `J010` | exact source hit 1/1 |
| `P2` | `21` | `1` | `TOOL-036` | `utilities_datacompj` | `J016-J017` | exact source hit 1/1 |
| `P2` | `69697` | `1` | `ERR-108` | `error_code_cause_action` | `J010` | exact source hit 1/1 |
| `P2` | `altiShapeLoader.properties` | `1` | `TOOL-048` | `spatial_nifi_tableau` | `J016-J017` | exact source hit 1/1 |
| `P2` | `BIGINT` | `1` | `SQL-134` | `datatypes_json_lob` | `J008-J009` | exact source hit 1/1 |
| `P2` | `DB_NAME` | `1` | `OPS-105` | `installation_startup_shutdown` | `J011-J012` | exact source hit 1/1 |
| `P2` | `deadlock` | `1` | `ERR-108` | `error_code_cause_action` | `J010` | exact source hit 1/1 |
| `P2` | `DECIMAL` | `1` | `SQL-134` | `datatypes_json_lob` | `J008-J009` | exact source hit 1/1 |
| `P2` | `DOUBLE` | `1` | `SQL-134` | `datatypes_json_lob` | `J008-J009` | exact source hit 1/1 |
| `P2` | `employees.dat` | `1` | `TOOL-027` | `isql_iloader` | `J016-J017` | exact source hit 1/1 |
| `P2` | `employees.fmt` | `1` | `TOOL-027` | `isql_iloader` | `J016-J017` | exact source hit 1/1 |
| `P2` | `ERR-91144` | `1` | `TOOL-031` | `utilities_datacompj` | `J016-J017` | exact source hit 1/1 |
| `P2` | `FLOAT` | `1` | `SQL-134` | `datatypes_json_lob` | `J008-J009` | exact source hit 1/1 |
| `P2` | `GRANT` | `1` | `TOOL-031` | `utilities_datacompj` | `J016-J017` | exact source hit 1/1 |
| `P2` | `INET` | `1` | `ERR-106` | `high_risk_operations_errors` | `J010` | exact source hit 1/1 |
| `P2` | `INT` | `1` | `SQL-134` | `datatypes_json_lob` | `J008-J009` | exact source hit 1/1 |
| `P2` | `libodbccli.a` | `1` | `VPM-124` | `monitoring_api_snmp` | `J015` | exact source hit 1/1 |
| `P2` | `LOG_DIR` | `1` | `OPS-105` | `installation_startup_shutdown` | `J011-J012` | exact source hit 1/1 |
| `P2` | `LOGANCHOR_DIR` | `1` | `OPS-105` | `installation_startup_shutdown` | `J011-J012` | exact source hit 1/1 |
| `P2` | `MANAGER` | `1` | `OPS-101` | `installation_startup_shutdown` | `J011-J012` | exact source hit 1/1 |
| `P2` | `mmERR_ABORT_INSUFFICIENT_PRIV` | `1` | `ERR-117` | `high_risk_operations_errors` | `J010` | exact source hit 1/1 |
| `P2` | `NULL ON EMPTY` | `1` | `SQL-134` | `datatypes_json_lob` | `J008-J009` | exact source hit 1/1 |
| `P2` | `NULL ON ERROR` | `1` | `SQL-134` | `datatypes_json_lob` | `J008-J009` | exact source hit 1/1 |
| `P2` | `NUMBER` | `1` | `SQL-134` | `datatypes_json_lob` | `J008-J009` | exact source hit 1/1 |
| `P2` | `NUMERIC` | `1` | `SQL-134` | `datatypes_json_lob` | `J008-J009` | exact source hit 1/1 |
| `P2` | `OPTIMIZER_PERFORMANCE_VIEW` | `1` | `VPM-130` | `version_sensitive_view_availability` | `J015` | exact source hit 1/1 |
| `P2` | `Primary Key` | `1` | `TOOL-039` | `migration_oracle_adapter` | `J016-J017` | exact source hit 1/1 |
| `P2` | `qpERR_ABORT_QCI_NotPermittedUser` | `1` | `ERR-117` | `high_risk_operations_errors` | `J010` | exact source hit 1/1 |
| `P2` | `qpERR_ABORT_QDP_INSUFFICIENT_PRIVILEGES` | `1` | `ERR-117` | `high_risk_operations_errors` | `J010` | exact source hit 1/1 |
| `P2` | `re-execute` | `1` | `ERR-108` | `error_code_cause_action` | `J010` | exact source hit 1/1 |
| `P2` | `ROLLBACK` | `1` | `ERR-123` | `tool_driver_errors` | `J010` | exact source hit 1/1 |
| `P2` | `rolled back` | `1` | `ERR-108` | `error_code_cause_action` | `J010` | exact source hit 1/1 |
| `P2` | `SERVER_MSGLOG_DIR` | `1` | `OPS-105` | `installation_startup_shutdown` | `J011-J012` | exact source hit 1/1 |
| `P2` | `Shapefile` | `1` | `TOOL-048` | `spatial_nifi_tableau` | `J016-J017` | exact source hit 1/1 |
| `P2` | `single value` | `1` | `REPL-112` | `security_tls_replication_ssl` | `J013-J014` | no exact source-string hit; inspect source wording |
| `P2` | `SMALLINT` | `1` | `SQL-134` | `datatypes_json_lob` | `J008-J009` | exact source hit 1/1 |
| `P2` | `Unable to bind the INET socket` | `1` | `ERR-106` | `high_risk_operations_errors` | `J010` | exact source hit 1/1 |
| `P2` | `uppercase` | `1` | `SQL-142` | `oracle_differences` | `J008-J009` | no exact source-string hit; inspect source wording |
| `P2` | `W` | `1` | `VPM-102` | `dictionary_meta_tables` | `J015` | exact source hit 1/1 |

## Answer Synthesis Gap Clusters

These tokens were already present in selected lexical context but the generated answer omitted them. They are not attachment-absence evidence by themselves, but later jobs should preserve them in answer-ready blocks and avoid compressing them away.

| Instances | Domain | Subdomain | Representative omitted tokens |
| ---: | --- | --- | --- |
| `15` | `errors_troubleshooting` | `high_risk_operations_errors` | `31`, `errno`, `0x311DD`, `201181`, `The tablespace has objects`, `0x6100D`, `0x61010`, `0x6102D` |
| `14` | `views_performance_monitoring` | `optimizer_plan_tuning` | `EXPLAIN PLAN`, `TEMP_TBS_MEMORY`, `TEMP_TBS_DISK`, `set operator`, `USE_HASH`, `USE_SORT`, `NO_USE_HASH`, `NO_INDEX` |
| `13` | `views_performance_monitoring` | `performance_views_check_sql` | `TX_ID`, `SESSION_ID`, `ADD_OID_CNT`, `GC_OID_CNT`, `EXECUTE_FLAG`, `NO_PLAN_CACHE`, `POOL_SIZE`, `PAGE_SIZE` |
| `13` | `sql_ddl_dml_datatypes` | `datatypes_json_lob` | `FIXED`, `VARIABLE`, `IN ROW`, `cursor`, `256`, `ISO/IEC 19075-6`, `CHAR`, `VARCHAR` |
| `13` | `errors_troubleshooting` | `sql_property_errors` | `SQL syntax error`, `Unsupported syntax`, `69720`, `0x2100C`, `0x21010`, `0x21011`, `0x21048`, `0x31363` |
| `10` | `sql_ddl_dml_datatypes` | `syntax_restrictions_examples` | `CREATE TABLE AS SELECT`, `PRIMARY KEY`, `UNIQUE`, `TIMESTAMP`, `CREATE INDEX`, `CREATE TABLESPACE`, `UNION`, `INTERSECT` |
| `10` | `sql_ddl_dml_datatypes` | `oracle_differences` | `USING`, `DELETE`, `double quotes`, `_`, `$`, `#`, `V$`, `NULL` |
| `10` | `sql_ddl_dml_datatypes` | `dml_expressions_functions` | `RETURNING`, `IGNORE LOOP`, `INSERT SELECT`, `sequence`, `LIMIT`, `multiple_delete`, `default`, `start` |
| `10` | `sql_ddl_dml_datatypes` | `ddl_generation` | `UNLIMITED`, `ALTER TABLE`, `DROP TABLE`, `INSERT`, `1024`, `1000`, `PARALLEL`, `INDEX_BUILD_THREAD_COUNT` |
| `10` | `replication_cdc_security_network` | `version_patch_replication_caveats` | `REPLICATION_DDL_SYNC_TIMEOUT`, `ALTER SYSTEM`, `ALTER SESSION`, `REPLICATION_DDL_SYNC`, `REPLICATION_DDL_ENABLE`, `7.4.6`, `Receiver`, `DROP REPLICATION` |
| `10` | `operations_admin` | `backup_restore_recovery` | `CREATE DATABASE`, `iLoader`, `restart recovery`, `ALTER DATABASE RECOVER DATABASE`, `online logs`, `full database backup`, `SYS_TBS_MEM_DIC`, `DROP TABLESPACE` |
| `10` | `operations_admin` | `accounts_tablespaces_admin` | `SYS`, `SYS_TBS_DISK_UNDO`, `DROP DATAFILE`, `BEGIN BACKUP`, `END BACKUP`, `NAME`, `TYPE`, `STATE` |
| `9` | `views_performance_monitoring` | `dictionary_meta_tables` | `USER_ID`, `TABLE_NAME`, `T`, `S`, `V`, `R`, `A`, `INDEX_COL_ORDER` |
| `9` | `replication_cdc_security_network` | `replication_topology_states` | `Applier`, `XSN`, `V$REPSENDER`, `REPL_MODE`, `Conflict`, `Timestamp-based Scheme`, `LOB`, `CONFLICT_RESOLUTION` |
| `8` | `tools_apis_connectors_migration` | `utilities_datacompj` | `Materialized View`, `SU`, `SI`, `MI`, `SD`, `Connections`, `Options`, `TablePairs` |
| `8` | `operations_admin` | `installation_startup_shutdown` | `$ALTIBASE_HOME/install/pre_install.sh`, `isql`, `catproc.sql`, `SERVICE`, `rollback`, `CREATE DATABASE`, `$ALTIBASE_HOME/dbs`, `100M` |
| `7` | `views_performance_monitoring` | `version_sensitive_view_availability` | `NAME`, `COLUMNCOUNT`, `TABLENAME`, `COLNAME`, `V$PROPERTY`, `Altibase 6.5.1`, `ALTER SYSTEM` |
| `7` | `tools_apis_connectors_migration` | `psm_external_procedures` | `ASSOCIATIVE ARRAY`, `NOCOPY`, `OPEN FOR`, `CREATE LIBRARY`, `CREATE PROCEDURE`, `LANGUAGE C` |
| `7` | `tools_apis_connectors_migration` | `c_cli_odbc_precompiler` | `BLOB`, `CLOB`, `DSN=ALTIBASE;LongDataCompat=ON`, `ALTIBASE_HDB_ODBC_64bit`, `NULL`, `GEOMETRY`, `SQLCA` |
| `7` | `properties` | `timeouts` | `2^32 - 1`, `ALTER SYSTEM`, `ALTER SESSION`, `V$PROPERTY` |
| `7` | `operations_admin` | `platform_upgrade_cautions` | `Red Hat Enterprise Linux 6`, `Red Hat Enterprise Linux 7`, `uninstall-base`, `PROCESS`, `CONTROL`, `META`, `$ALTIBASE_HOME/trc/altibase_boot.log` |
| `6` | `replication_cdc_security_network` | `replication_state_changes` | `FOR ANALYSIS`, `ALTER REPLICATION ... START`, `SYNC_RECORD_COUNT`, `OPTIONS OFFLINE`, `SQL apply mode`, `Restart SN` |
| `6` | `replication_cdc_security_network` | `compatibility_network_diagnostics` | `WITH`, `DROP HOST ALL`, `TCP`, `replication protocol version`, `7.1.0.6.5`, `netstat -nrv` |
| `6` | `replication_cdc_security_network` | `cdc_log_analyzer_repmgr` | `Handshake`, `PROPAGATION`, `QUICKSTART`, `archive log mode`, `XLOG_TYPE_LOB_CURSOR_OPEN`, `XLOG_TYPE_LOB_CURSOR_CLOSE` |
| `6` | `operations_admin` | `datafile_log_operations` | `dumpla`, `ARCHIVE_DIR`, `LOG_DIR`, `ALTER TABLESPACE`, `absolute path`, `altibase_sm.log` |
| `5` | `replication_cdc_security_network` | `security_tls_replication_ssl` | `REPLICATION_PORT_NO`, `ALTIBASE_SSL_LOAD_CONFIG`, `FIPS`, `$ALTIBASE_HOME/conf/altibase.properties`, `COMM_NAME` |
| `4` | `views_performance_monitoring` | `monitoring_api_snmp` | `10000001`, `10000003`, `10000101`, `10000102` |
| `4` | `tools_apis_connectors_migration` | `migration_oracle_adapter` | `Altibase 6.5.1`, `Prepare`, `Write to CSV`, `Altibase Log Analysis API` |
| `4` | `operations_admin` | `admin_runbook_safety` | `meta table`, `DML`, `database backup`, `0` |
| `3` | `tools_apis_connectors_migration` | `isql_iloader` | `-KEEP_SYSDBA`, `CONNECT`, `Unix` |
| `3` | `tools_apis_connectors_migration` | `dblink_kubernetes_connectors` | `binding`, `sqoop import`, `sqoop export` |
| `3` | `sql_ddl_dml_datatypes` | `replication_admin_sql` | `SYS`, `Replication Manual`, `propagation` |
| `3` | `properties` | `replication_ddl` | `NONE`, `V$PROPERTY`, `Replication Manual` |
| `3` | `properties` | `ddl_safety` | `0`, `DML`, `ALTER SYSTEM` |
| `3` | `properties` | `database_file_paths` | `VALUE1`, `$ALTIBASE_HOME/logs` |

## Source-Normalization And Calibration Candidates

No confirmed judge calibration issue is claimed by J003. The following tokens are candidates for later source-normalization or calibration review because the benchmark required token did not appear as an exact string in the selected source files even though the question record and nearby source wording support the topic. Do not edit attachments from these tokens alone; inspect the listed source area first.

| Class | Token | Questions | Next jobs | Source wording note |
| --- | --- | --- | --- | --- |
| `content gap` | `$ALTIBASE_HOME/trc/altibase_qp.log` | `OPS-130` | `J011-J012` | Installation source contains `$ALTIBASE_HOME/trc` and `altibase_qp.log`; Markdown escaping prevents exact token match. |
| `content gap` | `/*+ hint */` | `VPM-120` | `J015` | Performance source includes an escaped Markdown heading for the hint form and concrete `/*+ ... */` examples. |
| `content gap` | `40 bytes` | `SQL-142` | `J008-J009` | Korean SQL source has Korean 40-byte wording; the English token is normalized. |
| `content gap` | `backup-time metadata` | `OPS-134` | `J011-J012` | Administrator source supports backupInfo/loganchor recovery metadata, not this exact English phrase. |
| `content gap` | `C:\Program Files\Tableau\Drivers` | `TOOL-050` | `J016-J017` | Tableau guide source has the Windows path, but source matching needs backslash-escape inspection before editing. |
| `content gap` | `CREATE USER system privilege` | `OPS-108` | `J011-J012` | Korean source has `CREATE USER` and `CREATE USER ... system privilege` wording, not this exact English phrase. |
| `content gap` | `current loganchor` | `OPS-118` | `J011-J012` | Administrator source discusses current/recent loganchor recovery inputs, but not the exact English phrase. |
| `content gap` | `hybrid database` | `OPS-119` | `J011-J012` | Korean source uses translated hybrid-database wording. |
| `content gap` | `Intel Linux` | `REPL-123` | `J013-J014` | Selected SSL/TLS source did not expose this exact platform phrase in local text search. |
| `content gap` | `LOB(column_name)` | `SQL-111` | `J008-J009` | SQL source uses LOB grammar/examples with spacing or concrete column names, not this exact compact placeholder. |
| `content gap` | `optimizer-related properties` | `VPM-115` | `J015` | Korean performance source has optimizer-property heading text, not this exact English phrase. |
| `content gap` | `rollback-p<patch_version>` | `OPS-129` | `J011-J012` | Installation source examples use concrete directories such as `rollback-p0_0_0_10`; placeholder form is benchmark-normalized. |
| `retrieval gap` | `2^32 + 1` | `PROP-108`, `PROP-110` | `J004-J007` | Selected property/release-note sources expose decimal limits and Korean max-value text; exponent form is normalized. |
| `retrieval gap` | `2^31` | `PROP-108` | `J004-J007` | Selected property/release-note sources expose decimal limits and Korean max-value text; exponent form is normalized. |
| `retrieval gap` | `8-byte` | `SQL-106` | `J008-J009` | SQL source uses Korean 8-byte wording. |
| `retrieval gap` | `SQL hints` | `VPM-115` | `J015` | Source uses `hints ::=`, concrete hints, and Korean hint sections; exact English plural phrase is normalized. |
| `retrieval gap` | `single value` | `REPL-112` | `J013-J014` | Korean property source uses single-value wording in Korean; English phrase is normalized. |
| `retrieval gap` | `uppercase` | `SQL-142` | `J008-J009` | SQL source states unquoted names are internally converted to uppercase in Korean; English token is normalized. |

## Later-Job Handoff

- Start with `P0` content gaps in properties, operations, replication, SQL generation, troubleshooting, and performance views because they combine exact source-backed absence with blocker or protected-answer risk.
- For retrieval gaps, do not duplicate whole manual sections. Add exact-token headings, alias lines, local indexes, and cross-links near the existing source-backed blocks.
- For synthesis gaps, keep using `GPTs/reports/customer_answer_contract.md`: future attachment edits should use dense item blocks that make default/range/unit/mutability, exact SQL grammar, exact error code, and exact view-column tokens hard to omit.
- For `P3` source-normalization candidates, decide in the owning job whether the attachment should include the benchmark-normalized English token, a source-literal token, or a calibration note. Do not treat them as source-backed exact strings until that check is complete.

## Self-Review

- Source boundary: all checks used repository-local benchmark artifacts, current attachments, and question-selected source files only.
- Exact-token preservation: the report keeps literal token forms in code spans and separates absence, retrieval, and synthesis causes.
- Customer safety: protected-topic and blocker paths are promoted to `P0`/`P1` so later jobs handle risky backup/recovery, destructive SQL, replication, TLS, and version-sensitive properties first.
- Scope control: no `GPTs/attachments/` files, manuals, source documents, benchmark thresholds, or question expectations were changed.
