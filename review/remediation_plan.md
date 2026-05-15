# Altibase GPT Attachment Remediation Plan

Date: 2026-05-15
Owner: Codex / maintainer
Scope: `GPTs/attachments/*.md`, selected `GPTs/reports/*.md`, and `review/reports/*.md`

## State Rules

Use exactly one of these values in the `State` column:

- `ToDo`: not started.
- `Progress`: currently being edited or verified.
- `Done`: fix applied and focused validation passed.
- `Fail`: attempted, but blocked or validation failed.

Resume rule:

1. First search this file for `| Progress |`.
2. If found, continue that task before starting another task.
3. If none is in progress, start the first `ToDo` task in priority order.
4. Before editing a task, change its state from `ToDo` to `Progress`.
5. After editing, run the listed validation and change state to `Done` or `Fail`.
6. Do not mark R15 final readiness tasks `Done` until all referenced prerequisite tasks are `Done` or explicitly accepted as residual risk.
7. When marking a task `Fail`, record the cause in `review/remediation_failure_log.md`. The remediation runner appends this automatically for `mark`, `finish`, and `run-all`; pass `--reason` whenever the failure is operator-triggered.

Useful status commands:

```bash
rg -n "\| Progress \||\| Fail \||\| ToDo \|" review/remediation_plan.md
rg -n "^Verdict:|^\| (High|Medium|Low) \|" review/reports/R*.md
git status --short -- GPTs/attachments GPTs/reports review/reports review/remediation_plan.md
```

## Priority Model

- P0: tracking and workspace hygiene.
- P1: High severity correctness, safety, and source-traceability fixes.
- P2: Medium severity correctness and source-policy fixes.
- P3: retrieval-quality, cross-reference, and Low severity cleanup.
- P4: validation, report re-review, and final readiness.

R15 is a meta gate. Treat its High row as unresolved until the underlying `Review Required` reports are fixed or accepted.

## P0 Tracking And Hygiene

| ID | State | Severity | Source Reports | Target Files | Required Change | Validation |
| --- | --- | --- | --- | --- | --- | --- |
| P0-01 | Done | Hygiene | local workspace | `review/reports/Codex`, `review/reports/스크린샷` | Confirm whether the two empty untracked files are intentional. If not needed, remove them with approval or record them as ignored residual workspace files. | `find review/reports -maxdepth 1 -type f -empty -printf '%p\n'` |
| P0-02 | Done | Hygiene | local workspace | `review/reports/archive/` | Confirm whether the untracked archive directory should be committed, ignored, or left local-only. | `git status --short -- review/reports/archive` |
| P0-03 | Done | Process | all reports | this file | Keep task states current while editing. Only one task should be `Progress` at a time unless edits are truly independent. | `rg -n "\| Progress \|" review/remediation_plan.md` |

## P1 High Severity Fixes

| ID | State | Severity | Source Reports | Target Files | Required Change | Validation |
| --- | --- | --- | --- | --- | --- | --- |
| H01 | Done | High | R01 | `GPTs/attachments/17_kubernetes_aku_cloud.md`, possibly `GPTs/reports/source_inventory.md` | Resolve 7.1 AKU traceability. Either add a verified 7.1 AKU/Utilities source to inventory and keep the claims, or remove/narrow 7.1 AKU utility and 4-replica claims. | `rg -n "7\.1|aku|AKU|replica|scale" GPTs/attachments/17_kubernetes_aku_cloud.md GPTs/reports/source_inventory.md` |
| H02 | Done | High | R03, R10 | `GPTs/attachments/09_replication_ha_cdc.md` | Replace incomplete DDL synchronization procedure with full local/remote property sequence. Include `REPLICATION_DDL_ENABLE`, `REPLICATION_DDL_ENABLE_LEVEL`, local `ALTER SESSION SET REPLICATION_DDL_SYNC`, remote `ALTER SYSTEM SET REPLICATION_DDL_SYNC`, `REPLICATION_SQL_APPLY_ENABLE`, `ALTER SESSION SET REPLICATION = DEFAULT`, flush both sides, execute DDL once, and reset every changed property. Add `REPLICATION_DDL_SYNC` to property list. | `rg -n "REPLICATION_DDL_ENABLE|REPLICATION_DDL_ENABLE_LEVEL|REPLICATION_DDL_SYNC|REPLICATION_SQL_APPLY_ENABLE|ALTER SESSION SET REPLICATION = DEFAULT|flush" GPTs/attachments/09_replication_ha_cdc.md` |
| H03 | Done | High | R05 | `GPTs/attachments/04_sql_dml_oracle_compatibility.md` | Split regex guidance into default Altibase regex mode and PCRE2-compatible mode. Include `REGEXP_MODE=1`, system/session setting examples, character-set requirement, and syntax-difference caution. Cross-reference properties and troubleshooting attachments. | `rg -n "REGEXP_LIKE|REGEXP_MODE|PCRE2|ALTER SYSTEM SET REGEXP_MODE|ALTER SESSION SET REGEXP_MODE|US7ASCII|UTF-8" GPTs/attachments/04_sql_dml_oracle_compatibility.md` |
| H04 | Done | High | R07 | `GPTs/attachments/02_administration_operations.md` | Fix disk datafile move runbook. Split planned service/offline and recovery/CONTROL flows if source policy allows both. Put OS copy/move before `RENAME DATAFILE`, include ownership/permission check, `V$DATAFILES` verification, and source-audit note for Admin Manual vs SQL Reference phase wording. | `rg -n "RENAME DATAFILE|STARTUP CONTROL|OFFLINE|ONLINE|V\$DATAFILES|ownership|permission|copy|move" GPTs/attachments/02_administration_operations.md` |
| H05 | ToDo | High | R07 | `GPTs/attachments/02_administration_operations.md` | Add complete incremental recovery runbooks: complete recovery, incomplete recovery by tag, and incomplete recovery by `UNTIL TIME` or `UNTIL CANCEL`. Include historical `loganchor*`, `backupInfo`, disabling invalid change tracking in PROCESS, tag matching, temporary-file recreation, `META RESETLOGS`, and required full backup afterward. | `rg -n "incremental|backupInfo|loganchor|CHANGE TRACKING|RESETLOGS|UNTIL TIME|UNTIL CANCEL|tag|temporary" GPTs/attachments/02_administration_operations.md` |
| H06 | ToDo | High | R08 | `GPTs/attachments/07_error_messages_troubleshooting.md` | Add explicit uncovered-error-code behavior. Preserve supplied code/message, say exact cause/action is not covered, ask for version/full error/SQL/log excerpt, and avoid inferred cause/action beyond unknown. Narrow broad question bullet to covered/common codes unless full coverage is added. | `rg -n "uncovered|not covered|Unknown from the supplied message|covered/common|specific Altibase error code" GPTs/attachments/07_error_messages_troubleshooting.md` |
| H07 | ToDo | High | R09 | `GPTs/attachments/08_performance_tuning_monitoring.md` | Fix SQL plan cache join alias. `CHILD_PCO_COUNT` must come from `V$SQL_PLAN_CACHE_SQLTEXT` alias, not `V$SQL_PLAN_CACHE_PCO`. Keep `hit_count` and `rebuild_count` on PCO alias. | `rg -n "child_pco_count|V\$SQL_PLAN_CACHE_SQLTEXT|V\$SQL_PLAN_CACHE_PCO|hit_count|rebuild_count" GPTs/attachments/08_performance_tuning_monitoring.md` |
| H08 | ToDo | High | R09 | `GPTs/attachments/08_performance_tuning_monitoring.md` | Correct `DBMS_SQL_PLAN_CACHE.KEEP_PLAN` and `UNKEEP_PLAN` version guidance. State that sampled 7.1, 7.3, and 8.1 sources document the package while still requiring target-server verification of plan-cache keep columns. | `rg -n "DBMS_SQL_PLAN_CACHE|KEEP_PLAN|UNKEEP_PLAN|PLAN_CACHE_KEEP|7\.1|7\.3|8\.1" GPTs/attachments/08_performance_tuning_monitoring.md` |
| H09 | ToDo | High | R11 | `GPTs/attachments/18_security_ssl_tls.md` | Add 7.1 OpenSSL/Heartbleed caution. Mention verifying installed OpenSSL is not vulnerable before enabling SSL/TLS and include `OPENSSL_NO_HEARTBEATS` as the source-provided check. | `rg -n "Heartbleed|OPENSSL_NO_HEARTBEATS|OpenSSL|7\.1|TLS 1\.0" GPTs/attachments/18_security_ssl_tls.md` |
| H10 | ToDo | High | R11 | `GPTs/attachments/18_security_ssl_tls.md` | Add platform support caveat for SSL/TLS JDBC and ODBC guidance. Before production SSL/TLS recommendations, require target version/platform verification and state the SSL/TLS guide's Intel-Linux scope for JDBC/ODBC SSL connections. | `rg -n "Intel-Linux|platform|JDBC|ODBC|SSL/TLS|supported" GPTs/attachments/18_security_ssl_tls.md` |
| H11 | ToDo | High | R12 | `GPTs/attachments/11_java_jdbc_spring.md`, `GPTs/attachments/12_c_cli_odbc_precompiler.md`, `GPTs/attachments/13_isql_iloader_basic_tools.md` | Add Altibase 8.1 Empty LOB interface notes. Preserve `SQLEmptyLob()`, `SQLGetLobLength2()`, `-lob`, `use_lob_file=yes`, and state that older 7.1/7.3 zero-length LOB guidance should not be assumed for 8.1 Empty LOB behavior. | `rg -n "Empty LOB|SQLEmptyLob|SQLGetLobLength2|use_lob_file|SQLFreeLob2|zero-length" GPTs/attachments/11_java_jdbc_spring.md GPTs/attachments/12_c_cli_odbc_precompiler.md GPTs/attachments/13_isql_iloader_basic_tools.md` |
| H12 | ToDo | High | R12 | `GPTs/attachments/13_isql_iloader_basic_tools.md` | Rework `-rule csv` cookbook examples. Do not present `-rule csv` with `-f target_table.fmt` as copy-ready if source says `-f`, `-t`, `-r`, and `-e` are incompatible. Update caution to include all incompatible options and provide a verified alternative or explicit source conflict note. | `rg -n -- "-rule csv|-f|-t|-r|-e|target_table\.fmt|CSV|incompatible" GPTs/attachments/13_isql_iloader_basic_tools.md` |
| H13 | ToDo | High | R14 | `GPTs/attachments/06_data_dictionary_performance_views.md` | Add compact searchable object/column blocks for missing high-priority performance view families: `V$STATNAME`, `V$MEMSTAT`, `V$BUFFPOOL_STAT`, `V$INTERNAL_SESSION`, plus large-view column blocks where useful. Include purpose, key columns, when to query, and representative SQL. | `rg -n "V\$STATNAME|V\$MEMSTAT|V\$BUFFPOOL_STAT|V\$INTERNAL_SESSION|Searchable Object Blocks" GPTs/attachments/06_data_dictionary_performance_views.md` |
| H14 | ToDo | High | R14 | `GPTs/attachments/11_java_jdbc_spring.md` | Expand JDBC matrix material into searchable blocks by important Java/JDBC type mapping and method family. Cover `ResultSet`, `CallableStatement`, `PreparedStatement`, and LOB method families with support status, exception behavior, and version notes. | `rg -n "ResultSet|CallableStatement|PreparedStatement|LOB|type mapping|SQLSTATE|JDBC 4\.2" GPTs/attachments/11_java_jdbc_spring.md` |
| H15 | ToDo | High | R14 | `GPTs/attachments/11_java_jdbc_spring.md` | Expand SQLSTATE section into class/subclass blocks for retained JDBC table entries so code-level troubleshooting questions can be answered without guessing. | `rg -n "SQLSTATE|SQL state|080|220|HY|class|subclass" GPTs/attachments/11_java_jdbc_spring.md` |
| H16 | ToDo | High | R15 | `review/reports/*.md`, optional residual-risk record | Resolve R15 meta gate by making underlying High tasks `Done`, or create an explicit residual-risk acceptance record for any unresolved High task. Do not do this before H01-H15 are handled. | `rg -n "Verdict: (Fail|Review Required)|^\| (Blocker|High) \|" review/reports/R*.md` |

## P2 Medium Severity Fixes

| ID | State | Severity | Source Reports | Target Files | Required Change | Validation |
| --- | --- | --- | --- | --- | --- | --- |
| M01 | ToDo | Medium | R01 | `GPTs/attachments/11_java_jdbc_spring.md` | Align 7.1 source labels and version claims for Spring Data JPA, Hibernate, Maven, and Java compatibility with source inventory. If source basis is not verified for 7.1, phrase as driver-patch examples requiring target-driver verification. | `rg -n "7\.1|Spring|Hibernate|Maven|Java compatibility|source" GPTs/attachments/11_java_jdbc_spring.md GPTs/reports/source_inventory.md` |
| M02 | ToDo | Medium | R01, R06 | `GPTs/attachments/05_data_types_properties.md` | Replace customer-facing process wording such as "sampled 7.3 Korean source" and "sampled 7.x" for `LISTAGG_PRECISION` and `VARRAY_MEMORY_MAXIMUM` with customer-safe source labels. | `rg -n "sampled|Korean source|LISTAGG_PRECISION|VARRAY_MEMORY_MAXIMUM|supplemental source" GPTs/attachments/05_data_types_properties.md` |
| M03 | ToDo | Medium | R01, R07 | `GPTs/attachments/02_administration_operations.md` | Rewrite promotional architecture wording into source-neutral hybrid storage guidance. Avoid latency guarantees and "no external caching layer" unless source/workload scoped. | `rg -n "uniquely combines|microsecond|external caching|memory, disk|volatile tablespaces|storage choice" GPTs/attachments/02_administration_operations.md` |
| M04 | ToDo | Medium | R03 | `GPTs/attachments/02_administration_operations.md` | Add version-aware `DROP TABLESPACE IF EXISTS` guidance for 8.1 only. State 7.1/7.3 must omit `IF EXISTS` and use metadata pre-checks for idempotent scripts. | `rg -n "DROP TABLESPACE|IF EXISTS|metadata pre-check|7\.1|7\.3|8\.1" GPTs/attachments/02_administration_operations.md` |
| M05 | ToDo | Medium | R03 | `GPTs/attachments/02_administration_operations.md` | Add type-specific drop tablespace rules. Disk and memory may use `INCLUDING CONTENTS AND DATAFILES`; volatile must omit `AND DATAFILES`; keep temporary/system caveats separate. | `rg -n "AND DATAFILES|volatile|temporary|system|INCLUDING CONTENTS" GPTs/attachments/02_administration_operations.md` |
| M06 | ToDo | Medium | R05 | `GPTs/attachments/04_sql_dml_oracle_compatibility.md` | Add DML-side JSON column cautions: native `JSON` is 8.1 only, JSON uses Temporary LOB processing, `TEMPORARY_LOB_ENABLE` should be checked, JSON columns are LOB-like for restrictions, and `SELECT FOR UPDATE` should not target JSON columns. | `rg -n "JSON|TEMPORARY_LOB_ENABLE|SELECT FOR UPDATE|LOB-like|8\.1" GPTs/attachments/04_sql_dml_oracle_compatibility.md` |
| M07 | ToDo | Medium | R06 | `GPTs/attachments/07_error_messages_troubleshooting.md` | Split LOB autocommit version caution by code: `0x5112C` and `0x91101` present in sampled 7.1/7.3/8.1; `0x314B4` treated as 7.3/8.1 unless target 7.1 build confirms it. | `rg -n "0x5112C|0x91101|0x314B4|LOB_AUTOCOMMIT|autocommit|7\.1|7\.3|8\.1" GPTs/attachments/07_error_messages_troubleshooting.md` |
| M08 | ToDo | Medium | R07 | `GPTs/attachments/02_administration_operations.md` | Add `$ALTIBASE_HOME/conf/altibase.properties` to offline physical backup manifest and add post-`server stop` verification before copying backup files. | `rg -n "offline physical backup|altibase.properties|server stop|backup manifest|log anchor|checkpoint" GPTs/attachments/02_administration_operations.md` |
| M09 | ToDo | Medium | R07 | `GPTs/attachments/02_administration_operations.md` | Convert archive log mode change block into a full service-impact runbook: current mode check, downtime planning, archive destination capacity, clean stop, SYSDBA, `STARTUP CONTROL`, alter mode, verify, `STARTUP SERVICE`, and follow-up backup guidance. | `rg -n "ARCHIVELOG|NOARCHIVELOG|STARTUP CONTROL|STARTUP SERVICE|V\$LOG|V\$ARCHIVE|downtime|capacity" GPTs/attachments/02_administration_operations.md` |
| M10 | ToDo | Medium | R07 | `GPTs/attachments/01_getting_started_installation.md` | Add post-downgrade APatch rollback/delete-patch step after `server downgrade`. Make order explicit: backup, stop, downgrade when needed, delete/uninstall patch, verify binary and meta versions. | `rg -n "downgrade|rollback|APatch|delete|uninstall|meta|server stop|version" GPTs/attachments/01_getting_started_installation.md` |
| M11 | ToDo | Medium | R08 | `GPTs/attachments/07_error_messages_troubleshooting.md` | Add `Escalation:` coverage to every error block or add a clear module/severity default inherited by all blocks. Include evidence to collect and when to stop corrective actions. | `rg -n "Escalation:|Error block|Evidence|stop" GPTs/attachments/07_error_messages_troubleshooting.md` |
| M12 | ToDo | Medium | R08 | `GPTs/attachments/08_performance_tuning_monitoring.md` | Normalize server issue blocks to fields: `Symptom`, `Primary Causes`, `Check SQL or Command`, `Immediate Action`, `Verification`, `Version Cautions`, and `Escalation`. | `rg -n "Server issue block|Symptom|Primary Causes|Verification|Version Cautions|Escalation" GPTs/attachments/08_performance_tuning_monitoring.md` |
| M13 | ToDo | Medium | R08 | `GPTs/attachments/08_performance_tuning_monitoring.md` | Correct `VICTIM_SEARCH_WARP` interpretation to replacement-buffer search pressure. Pair it with `VICTIM_FAILS`, `PREPARE_AGAIN_VICTIMS`, `READ_PAGES`, and time-window snapshots before recommending property changes. | `rg -n "VICTIM_SEARCH_WARP|VICTIM_FAILS|PREPARE_AGAIN_VICTIMS|READ_PAGES|BUFFER_AREA_SIZE" GPTs/attachments/08_performance_tuning_monitoring.md` |
| M14 | ToDo | Medium | R08 | `GPTs/attachments/08_performance_tuning_monitoring.md` | Refine service-thread overload diagnostic. Count `TYPE` and `RUN_MODE`, inspect `READY_TASK_COUNT`, and compare only multiplexing/shared load with `MULTIPLEXING_THREAD_COUNT`. | `rg -n "V\$SERVICE_THREAD|READY_TASK_COUNT|MULTIPLEXING_THREAD_COUNT|SOCKET|RUN_MODE|TYPE" GPTs/attachments/08_performance_tuning_monitoring.md` |
| M15 | ToDo | Medium | R09 | `GPTs/attachments/08_performance_tuning_monitoring.md` | Avoid hard-coding only `CREATED_BY_CACHE_MISS`. Prefer data dictionary spellings or interpret actual `CREATE_REASON` values returned by the target server. | `rg -n "CREATE_REASON|CREATED_BY_CACHE_MISS|CREATE_BY_CACHE_MISS|CREATE_BY_PLAN" GPTs/attachments/08_performance_tuning_monitoring.md` |
| M16 | ToDo | Medium | R10 | `GPTs/attachments/03_sql_ddl_generation.md`, `GPTs/attachments/09_replication_ha_cdc.md` | Add `WITH UNIX_DOMAIN` alternative to compact CDC XLog Sender syntax blocks with same-host UNIX/Linux and `$ALTIBASE_HOME` cautions. Keep `USING SSL` and `USING IB` excluded from `FOR ANALYSIS`. | `rg -n "FOR ANALYSIS|WITH UNIX_DOMAIN|USING SSL|USING IB|ALTIBASE_HOME" GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/09_replication_ha_cdc.md` |
| M17 | ToDo | Medium | R10 | `GPTs/attachments/09_replication_ha_cdc.md` | Clarify XLog Sender host-change rules: UNIX-domain XLog Sender cannot add hosts; host add/drop/set applies only to TCP/IP XLog Collector endpoints; `SET HOST` takes effect after restart. | `rg -n "ADD HOST|DROP HOST|SET HOST|UNIX_DOMAIN|TCP/IP|restart" GPTs/attachments/09_replication_ha_cdc.md` |
| M18 | ToDo | Medium | R10 | `GPTs/attachments/03_sql_ddl_generation.md` | Reword replication-target DDL rule to "Do not generate ad hoc `ALTER TABLE` for replication targets." Point to standard remove/re-add and documented DDL synchronization procedure in `09_replication_ha_cdc.md`. | `rg -n "ALTER TABLE|replication target|ad hoc|DDL synchronization|remove/re-add" GPTs/attachments/03_sql_ddl_generation.md` |
| M19 | ToDo | Medium | R11 | `GPTs/attachments/11_java_jdbc_spring.md` | Version-scope JDBC `ssl_protocols` as 7.3 and 8.1 verified-source guidance. For 7.1, keep SSL guidance to `ssl_enable`, `port`, `ciphersuite_list`, truststore/keystore properties, and limitations in security attachment. | `rg -n "ssl_protocols|ssl_enable|ciphersuite_list|truststore|keystore|7\.1|7\.3|8\.1" GPTs/attachments/11_java_jdbc_spring.md` |
| M20 | ToDo | Medium | R12 | `GPTs/attachments/13_isql_iloader_basic_tools.md` | Add version-scoped iLoader option literals or mark compact syntax as partial. Preserve `-dry-run`, `-lightmode`, `-stmt_prefix`, and `-extra_col_delimiter`. | `rg -n -- "-dry-run|-lightmode|-stmt_prefix|-extra_col_delimiter|compact syntax|partial" GPTs/attachments/13_isql_iloader_basic_tools.md` |
| M21 | ToDo | Medium | R14 | multiple attachments | Split or simplify oversized Mermaid diagrams listed by R14, or move linear procedure detail into ordered text blocks. | `rg -n "^```mermaid|-->|->>|participant|sequenceDiagram|flowchart" GPTs/attachments/*.md` |
| M22 | ToDo | Medium | R14 | `GPTs/attachments/02_administration_operations.md`, `03_sql_ddl_generation.md`, `05_data_types_properties.md`, `06_data_dictionary_performance_views.md`, `07_error_messages_troubleshooting.md`, `08_performance_tuning_monitoring.md`, `09_replication_ha_cdc.md`, `12_c_cli_odbc_precompiler.md`, `14_utilities_operation_tools.md`, `18_security_ssl_tls.md` | Add short `Attachment Cross-References` sections to high-overlap files. Keep each to 3-6 links with concrete reason to use the related attachment. | `rg -n "Attachment Cross-References" GPTs/attachments/02_administration_operations.md GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/05_data_types_properties.md GPTs/attachments/06_data_dictionary_performance_views.md GPTs/attachments/07_error_messages_troubleshooting.md GPTs/attachments/08_performance_tuning_monitoring.md GPTs/attachments/09_replication_ha_cdc.md GPTs/attachments/12_c_cli_odbc_precompiler.md GPTs/attachments/14_utilities_operation_tools.md GPTs/attachments/18_security_ssl_tls.md` |

## P3 Low Severity And Optional Cleanup

| ID | State | Severity | Source Reports | Target Files | Required Change | Validation |
| --- | --- | --- | --- | --- | --- | --- |
| L01 | ToDo | Low | R01 | `GPTs/attachments/00_version_release_platform.md` | Replace backticked `ReleaseNotes` wording with customer-safe "release notes" or "Altibase release notes". | `rg -n "ReleaseNotes|release notes|Altibase release notes" GPTs/attachments/00_version_release_platform.md` |
| L02 | ToDo | Low | R03 | `GPTs/attachments/02_administration_operations.md` | Split memory vs volatile tablespace sizing note. Memory can mention `SPLIT EACH`; volatile should not. | `rg -n "SPLIT EACH|volatile|memory tablespace|AUTOEXTEND NEXT" GPTs/attachments/02_administration_operations.md` |
| L03 | ToDo | Low | R03 | `GPTs/attachments/03_sql_ddl_generation.md` | Add password uppercasing note near `CREATE USER` examples: unquoted lowercase passwords are uppercased by default; case-sensitive passwords require `CASE_SENSITIVE_PASSWORD = 1` and quoted password. | `rg -n "CREATE USER|CASE_SENSITIVE_PASSWORD|password|uppercase|quoted" GPTs/attachments/03_sql_ddl_generation.md` |
| L04 | ToDo | Low | R07 | `GPTs/attachments/02_administration_operations.md` | Add SYSDBA password safety note near examples using `isql -u sys -p manager -sysdba`: `manager` is an example and production passwords should not be embedded in reusable scripts. | `rg -n "isql -u sys -p manager -sysdba|production passwords|SYS password" GPTs/attachments/02_administration_operations.md` |
| L05 | ToDo | Low | R08 | `GPTs/attachments/06_data_dictionary_performance_views.md` | Add final step to runtime/replication troubleshooting templates: map observed condition to relevant 07 or 08 response block before recommending an action. | `rg -n "troubleshooting template|07_error_messages|08_performance|map observed" GPTs/attachments/06_data_dictionary_performance_views.md` |
| L06 | ToDo | Low | R09 | `GPTs/attachments/08_performance_tuning_monitoring.md` | Replace SNMP example `-c private` with placeholder such as `-c <community>` while keeping ACL/default-community warning. | `rg -n -- "-c private|-c <community>|community|SNMP" GPTs/attachments/08_performance_tuning_monitoring.md` |
| L07 | ToDo | Low | R12 | `GPTs/attachments/11_java_jdbc_spring.md` | Add inline note under SSL/TLS JDBC URL example that server verification requires configured default truststore or explicit `truststore_url` and `truststore_password`. | `rg -n "verify_server_certificate|truststore_url|truststore_password|SSL/TLS JDBC URL" GPTs/attachments/11_java_jdbc_spring.md` |
| L08 | ToDo | Low | R13 | `GPTs/attachments/16_dblink_external_connectors.md` | Confirm GoldenGate is out of scope, or add a small source-backed section if an approved source exists. Do not synthesize connector guidance. | `rg -n "GoldenGate|scope|connector" GPTs/attachments/16_dblink_external_connectors.md GPTs/Altibase_GPT_Document_Selection.md` |
| L09 | ToDo | Low | R13 | `GPTs/attachments/19_spatial_nifi_tableau_misc.md` | Consider rewriting `/home/altibase/NiFi/nifi-1.12.1/lib` as `$NIFI_HOME/lib`, preserving source path only as an example value if needed. | `rg -n "/home/altibase/NiFi|NIFI_HOME|nifi-1\.12\.1/lib" GPTs/attachments/19_spatial_nifi_tableau_misc.md` |
| L10 | ToDo | Low | R14 | multiple attachments | Normalize only retrieval-critical top-level headings and add residual-scope notes where coverage is intentionally partial or condensed. | `rg -n "^## Residual Scope|^## Applicable Versions|^## Questions This File Can Answer|^## Source Documents" GPTs/attachments/*.md` |

## P4 Validation And Report Closure

| ID | State | Severity | Source Reports | Target Files | Required Change | Validation |
| --- | --- | --- | --- | --- | --- | --- |
| V01 | ToDo | Validation | all | `GPTs/attachments/` | Run upload-boundary checks after edits: exactly 20 upload Markdown files excluding README, no image dependency, no internal path/source labels, required headings present. | See command block below. |
| V02 | ToDo | Validation | changed report set | `review/reports/R01_*.md` through `R14_*.md` | Re-review changed sections only and update relevant reports from `Review Required` to `Pass` when all listed findings are fixed or accepted. Preserve old evidence in archive if needed. | `rg -n "^Verdict:|^\| (High|Medium|Low) \|" review/reports/R*.md` |
| V03 | ToDo | Validation | R15 | `review/reports/R15_multilingual_final_readiness.md` | Re-run final readiness after underlying report closure or residual-risk acceptance. R15 should remain `Review Required` until this point. | `rg -n "Verdict: (Fail|Review Required)|^\| (Blocker|High) \|" review/reports/R*.md` |
| V04 | ToDo | Validation | final | optional acceptance record | If any task is not fixed by design, create an explicit residual-risk record that names the task ID, reason, impact, and owner approval. | `rg -n "residual|accepted risk|H[0-9]+|M[0-9]+" review GPTs -g '*.md'` |

Common validation commands:

```bash
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' | sort | wc -l
rg -n 'trunk|Altibase_trunk|file://|C:/|C:\\|/home/et16|/Users/|Manuals/Altibase|ReleaseNotes/kor|JOB-[0-9]+|IMG-[0-9]+|Conversion TODO' GPTs/attachments/*.md GPTs/attachments/README.md || true
rg -n '!\[[^]]*\]\([^)]*\.(png|jpg|jpeg|gif|svg|webp)\)|<img|https?://[^ )]+\.(png|jpg|jpeg|gif|svg|webp)|[^[:space:]]+\.(png|jpg|jpeg|gif|svg|webp)' GPTs/attachments/*.md GPTs/attachments/README.md || true
for h in "Applicable Versions" "Questions This File Can Answer" "Source Documents"; do
  printf '%s\n' "$h"
  find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' -exec rg --files-without-match "^## $h$" {} + || true
done
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' -exec rg --files-without-match "Altibase 8\.1 verified source" {} + || true
rg -n "Verdict: (Fail|Review Required)|^\| (Blocker|High) \|" review/reports/R*.md || true
```

## Current Gate Summary

Known pass reports:

- R00 upload boundary
- R02 high-risk source traceability
- R04 table/index/constraint DDL
- R13 tools/migration/connectors, with Low notes

Known review-required reports:

- R01 source policy
- R03 DDL/tablespace/storage
- R05 DML/Oracle compatibility
- R06 properties/dictionary checks
- R07 operations/admin/recovery
- R08 troubleshooting/errors
- R09 performance/monitoring
- R10 replication/HA/CDC/SSL
- R11 security/TLS
- R12 development interfaces
- R14 retrieval/visual conversion
- R15 final readiness
