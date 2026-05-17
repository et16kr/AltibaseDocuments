# Full Coverage Audit Guardrail Register

- Workflow: `altibase-gpt-full-coverage-audit`
- Initialized by: `FCA-J003`
- Status: Active register for `Guardrail` and `Out-of-scope` catalog or matrix rows

## Register Contract

Add one entry for every `Guardrail` or `Out-of-scope` row. Each entry must explain the
source boundary or customer-evidence dependency and give the safest next check or
missing input pattern.

Accepted guardrail reasons include:

- exact version or patch level is required;
- customer environment, topology, object definition, log excerpt, runtime output, or
  installed tool behavior is required;
- selected sources do not support the requested compatibility, syntax, error-code, or
  operational claim;
- the item is outside the locked selected source corpus.

## Active Guardrails

### FCA-J038 Technical Documents Support Out-Of-Scope Rows

FCA-J038 cataloged the remaining technical-document support slice. Two selected-source
subsections are retained as traceability rows but remain outside the customer-facing
Altibase 7.1, 7.3, and 8.1 upload scope except where an in-scope compatibility row
explicitly uses an older version as an endpoint.

| source_item_id | status | source_family | version_scope | source_path | source_heading | guardrail_reason | safest_next_check | attachment_target | audit_job | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-REPL-XVER-000040 | Out-of-scope | technical_documents_support | cross-version | Technical Documents/kor/ReplicationCompatibility.md | ReplicationCompatibility > Altibase 6.x standalone sections and protocol rows | Altibase 6.x standalone replication compatibility and protocol rows are outside the locked customer-facing upload scope of Altibase 7.1, 7.3, and 8.1 except when an in-scope 7.x row explicitly uses 6.x as a Sender/Receiver endpoint. | Ask for the exact target versions, Sender/Receiver direction, `V$VERSION.repl_protocol_version`, replication mode, and whether the question is a 7.1/7.3 compatibility endpoint before using any 6.x row; otherwise do not answer 6.x-only protocol questions from the upload package. | N/A | FCA-J038 | source locator: Korean ReplicationCompatibility lines 69-98 and 123-141; catalog row `SRC-REPL-XVER-000040`. |
| SRC-OTHER-XVER-000269 | Out-of-scope | technical_documents_support | cross-version | Technical Documents/kor/JavaCompatibility.md | JavaCompatibility > Altibase 6.5.1 Java compatibility | Altibase 6.5.1 Java compatibility rows are outside the locked customer-facing upload scope of Altibase 7.1, 7.3, and 8.1; do not use them to answer current 7.x or 8.1 Java runtime questions unless an in-scope row explicitly uses 6.5.1 as a compatibility endpoint. | Ask for exact Altibase version and patch, component, Java runtime, and whether the question is a historical 6.5.1 migration/support question; otherwise route current Java runtime questions to 7.1, 7.3, or Altibase 8.1 verified-source rows. | N/A | FCA-J038 | source locator: Korean JavaCompatibility lines 88-110; catalog row `SRC-OTHER-XVER-000269`. |

### FCA-J037 Spatial NiFi Tableau And Live Integration Guardrail

FCA-J037 cataloged Spatial SQL, `GEOMETRY`, Spatial API, `altiShapeLoader`, NiFi, and
Tableau source rows. Source-backed syntax, options, setup procedures, and validation
checks are represented in attachment 19, but live import/export, BI/ETL connectivity,
performance, and root-cause claims remain dependent on customer environment evidence.

| source_item_id | status | source_family | version_scope | source_path | source_heading | guardrail_reason | safest_next_check | attachment_target | audit_job | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-OTHER-XVER-000267 | Guardrail | spatial_nifi_tableau | cross-version | GPTs/reports/gap_register.md | Gap Register > GAP-J002-017 and GAP-J002-018 > Spatial NiFi Tableau and live tool validation boundary | Requires exact Altibase version and patch, JDBC driver version, Java version, host, port, database name, character set, SRID, geometry precision, shapefile component set and size, NiFi/Tableau versions, relevant property/config files, full error/log/output, and rollback or reload plan before asserting production import/export, BI/ETL success, performance, or root cause. | Ask for the exact Altibase version and patch, JDBC driver version, Java version, host, port, database name, character set, SRID, geometry precision, shapefile component set and size, NiFi/Tableau versions, relevant property/config files, full error/log/output, and rollback or reload plan; validate first in non-production before declaring production import/export or integration success. | GPTs/attachments/19_spatial_nifi_tableau_misc.md | FCA-J037 | `GAP-J002-017`; `GAP-J002-018`; catalog row `SRC-OTHER-XVER-000267`; attachment anchors `Response Rules`, `Retrieval Alias Index`, and `Residual Scope`. |

### FCA-J036 Kubernetes AKU And Cloud Guardrail

FCA-J036 cataloged Kubernetes object examples, AKU sample object sets, AKU configuration
and lifecycle behavior, release-note AKU changes, and cloud/container operational
caveats. The selected sources support generic Kubernetes and AKU guidance, but
production cloud execution, TLS behavior, storage, secret handling, and runtime success
remain environment-limited.

| source_item_id | status | source_family | version_scope | source_path | source_heading | guardrail_reason | safest_next_check | attachment_target | audit_job | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-OTHER-XVER-000261 | Guardrail | kubernetes_aku | cross-version | GPTs/reports/gap_register.md | Gap Register > GAP-J002-012 and GAP-J002-018 > Kubernetes, AKU, TLS, and cloud live validation boundary | Requires exact Altibase version and patch, Kubernetes provider/version, node OS, image build, storage class/PV/PVC design, hostname-license basis, Service/DNS/network policy, secret and TLS/certificate design, ports, replication target tables, backup/recovery plan, full logs/output, and non-production validation evidence before asserting production cloud, TLS, or AKU runtime success. | Ask for the exact Altibase version and patch, Kubernetes provider/version, node OS, image build, storage class and PV/PVC design, hostname-license basis, Service/DNS/network policy, secret and TLS/certificate design, ports `20300` and `20301`, replication target tables, backup/recovery plan, full logs/output, and non-production validation evidence before declaring cloud deployment, TLS handshake, or AKU runtime success. | GPTs/attachments/17_kubernetes_aku_cloud.md | FCA-J036 | `GAP-J002-012`; `GAP-J002-018`; catalog row `SRC-OTHER-XVER-000261`; attachment anchors `Response Rules`, `Troubleshooting And Cautions`, and `Residual Scope`. |

### FCA-J035 DB Link And External Connector Guardrail

FCA-J035 cataloged DB Link, Hadoop Connector, DBeaver, Hibernate, OpenLDAP, and
Oracle GoldenGate source rows. Source-backed setup, syntax, configuration, and
troubleshooting content is represented in attachment 16, but live connector success,
compatibility conclusions, and root-cause claims remain environment-limited.

| source_item_id | status | source_family | version_scope | source_path | source_heading | guardrail_reason | safest_next_check | attachment_target | audit_job | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-OTHER-XVER-000245 | Guardrail | dblink_hadoop_external_connectors | cross-version | GPTs/reports/gap_register.md | Gap Register > GAP-J002-012 and GAP-J002-014 > DB Link, Hadoop, and external connector live validation boundary | Requires exact Altibase version and patch, `DBLINK_*`/`ALTILINKER_*` values, `dblink.conf`, remote DBMS and JDBC driver versions, Java runtime, Hadoop/Sqoop/DBeaver/Hibernate/OpenLDAP/GoldenGate product versions, JDBC/ODBC URL or DSN, TLS/firewall topology, full error/log/output, and non-production validation evidence before asserting production connector success or root cause. | Ask for the exact Altibase version and patch, DB Link properties and `dblink.conf`, remote DBMS and JDBC driver versions, Java runtime, connector or product versions, JDBC/ODBC URL or DSN, TLS/firewall topology, full error/log/output, and non-production validation evidence before declaring connector compatibility, success, or root cause. | GPTs/attachments/16_dblink_external_connectors.md | FCA-J035 | `GAP-J002-012`; `GAP-J002-014`; catalog row `SRC-OTHER-XVER-000245`; attachment anchors `Response Rules`, `Troubleshooting Checklist`, and `Residual Scope`. |

### FCA-J034 Migration And Oracle Compatibility Guardrail

FCA-J034 cataloged Migration Center and Adapter for Oracle source rows. The selected
manuals and release notes support the documented tool workflows, conversion rules,
options, property blocks, and validation checks, but production migration correctness
still depends on the customer's exact source and target environment and generated
artifacts.

| source_item_id | status | source_family | version_scope | source_path | source_heading | guardrail_reason | safest_next_check | attachment_target | audit_job | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-OTHER-XVER-000230 | Guardrail | migration_oracle | cross-version | GPTs/reports/gap_register.md | Gap Register > GAP-J002-017 and GAP-J002-018 > migration, adapter, and live validation boundary | Selected sources document the migration and adapter workflows, but production migration correctness depends on exact source and target versions, patch levels, object definitions, character sets, JDBC/OCI drivers, generated reports, configuration, logs, and non-production validation output. | Ask for source Oracle version, target Altibase version and patch, source and target character sets, storage/tablespace design, object DDL, PSM use, generated Build/Reconcile/Run/Data Validation reports, Adapter `oraAdapter.conf`, JDBC/OCI versions, logs, backup/rollback plan, and non-production validation evidence before asserting production migration success or compatibility. | GPTs/attachments/15_migration_oracle_compatibility.md | FCA-J034 | `GAP-J002-017`; `GAP-J002-018`; catalog row `SRC-OTHER-XVER-000230`; attachment `Residual Scope`. |

### FCA-J033 Utilities And Operation Tool Guardrails

FCA-J033 cataloged utility commands, operation-tool outputs, dump diagnostics,
dataCompJ, and AKU routing. The selected manuals support command syntax and expected
output patterns, but installed-tool behavior and live diagnostic conclusions still
depend on customer evidence.

| source_item_id | status | source_family | version_scope | source_path | source_heading | guardrail_reason | safest_next_check | attachment_target | audit_job | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-OTHER-XVER-000229 | Guardrail | utilities_datacompj | cross-version | GPTs/reports/gap_register.md | Gap Register > GAP-J002-016 > utilities and dump-tool live validation boundary | Selected sources document utility commands and output patterns, but exact installed behavior, generated files, dump decoding, synchronization effects, and diagnostic conclusions depend on exact version, package, input files, environment, and runtime output. | Ask for the exact Altibase version and patch, client/server package, installed utility help or version output, command line, configuration file, target source/destination objects, input dump/log/trace files, generated scripts or reports, and non-production/live output before asserting package-specific behavior, synchronization effect, dump interpretation, or root cause. | GPTs/attachments/14_utilities_operation_tools.md | FCA-J033 | `GAP-J002-016`; catalog row `SRC-OTHER-XVER-000229`; attachment `Residual Scope` and `Operational Guardrails`. |

### FCA-J032 iSQL And iLoader Guardrails

FCA-J032 cataloged the iSQL and iLoader source rows. Most source-backed tool behavior
is represented in attachment 13, but `-dry-run` remains guarded because selected
manuals list the option without a full semantic block that would support production
precheck guarantees.

| source_item_id | status | source_family | version_scope | source_path | source_heading | guardrail_reason | safest_next_check | attachment_target | audit_job | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ILOAD-XVER-000016 | Guardrail | isql_iloader | cross-version | Manuals/Altibase_7.3/kor/iLoader User's Manual.md | iLoader User's Manual > -dry-run syntax boundary | Selected 7.1, 7.3, and Altibase 8.1 verified source syntax lists `-dry-run`, but the selected manuals do not define exact effects, guarantees, output, or failure diagnostics. | Ask for the exact installed iLoader client package and version, run `iloader help`, consult the installed client manual, or validate behavior with a non-production run before relying on `-dry-run` as a production precheck. | GPTs/attachments/13_isql_iloader_basic_tools.md | FCA-J032 | Korean iLoader 7.3 lines 505, 1645, and 1694; Korean iLoader 7.1 lines 503, 1616, and 1665; catalog row `SRC-ILOAD-XVER-000016`. |

### FCA-J031 C CLI ODBC And Precompiler Guardrails

FCA-J031 cataloged the C-facing CLI, ODBC, Altibase C Interface, and APRE
precompiler source rows. Most source-backed items route to attachment 12, but runtime
success, 8.1 Empty LOB compile-ready calls, and ACI long-data streaming remain guarded
by source or customer-evidence limits.

| source_item_id | status | source_family | version_scope | source_path | source_heading | guardrail_reason | safest_next_check | attachment_target | audit_job | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-API-8.1-000002 | Guardrail | c_cli_odbc_precompiler | 8.1 | ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md | Altibase 8.1.0.0.1 Release Notes > Empty LOB CLI function names | Selected 8.1 release notes name `SQLEmptyLob()` and `SQLGetLobLength2()`, but the selected manual corpus does not provide complete callable signatures or argument semantics. | Ask for the installed 8.1 client header or exact client manual page, client package version, OS/compiler, and intended LOB sequence before generating compile-ready calls; otherwise preserve only the function names and state the source limit. | GPTs/attachments/12_c_cli_odbc_precompiler.md | FCA-J031 | Korean 8.1 release note line 179; `GAP-J002-015`; catalog row `SRC-API-8.1-000002`; attachment residual scope and LOB API blocks. |
| SRC-API-XVER-000082 | Guardrail | c_cli_odbc_precompiler | cross-version | Manuals/Altibase_7.3/kor/Altibase C Interface Manual.md | Altibase C Interface Manual > altibase_stmt_send_long_data() boundary | Selected ACI source exposes `ALTIBASE_NEED_DATA` and `altibase_stmt_send_long_data()`, but does not support recommending that function as a customer-ready streaming LOB implementation. | Ask for the exact installed client package, `alticapi.h` header, source/manual page, return-code path, and full diagnostics before suggesting any ACI streaming LOB implementation; otherwise use covered locator or result-retrieval guidance. | GPTs/attachments/12_c_cli_odbc_precompiler.md | FCA-J031 | Korean ACI 7.3 lines 2959 and 3607; catalog row `SRC-API-XVER-000082`; attachment `ACI LOB caution block`. |
| SRC-OTHER-XVER-000226 | Guardrail | c_cli_odbc_precompiler | cross-version | GPTs/reports/gap_register.md | Gap Register > GAP-J002-012 > CLI/ODBC/ACI/APRE live execution validation boundary | Runtime success or root cause depends on exact Altibase version and patch, client package, OS/compiler, Driver Manager and SQLLEN width, DSN or connection string, SSL/TLS settings, autocommit and LOB sequence, source code, diagnostics, logs, and live output. | Ask for the exact server/client versions, client package, OS/compiler, Driver Manager and SQLLEN width, DSN or connection string, SSL/TLS settings, C or APRE source, full `SQLGetDiagRec`/ACI/APRE diagnostics, logs, and observed output before asserting runtime success or failure cause. | GPTs/attachments/12_c_cli_odbc_precompiler.md | FCA-J031 | `GAP-J002-012`; source inventory J036 note; catalog row `SRC-OTHER-XVER-000226`; attachment `Residual Scope`. |

### FCA-J030 JDBC Java Spring And Hibernate Runtime Guardrail

FCA-J030 cataloged one JDBC/Java/Spring/Hibernate guardrail row. The selected manuals
and approved third-party guides provide driver, URL, property, failover, Adapter,
Spring, and Hibernate configuration evidence, but production runtime success still
depends on the exact installed driver, Java and framework versions, target database
driver, topology, security settings, and live output.

| source_item_id | status | source_family | version_scope | source_path | source_heading | guardrail_reason | safest_next_check | attachment_target | audit_job | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-OTHER-XVER-000225 | Guardrail | jdbc_java | cross-version | GPTs/reports/gap_register.md | Gap Register > GAP-J002-012 and GAP-J002-014 > JDBC Java runtime and live connector validation boundary | Requires exact Altibase server version/patch, JDBC driver jar and `java -jar` output, Java runtime, Spring/Hibernate/pool versions, URL/properties, Adapter version, target JDBC driver, failover topology, SSL/TLS configuration, and live error/log/output before asserting runtime success. | Ask for the exact Altibase server version/patch, JDBC driver jar name and `java -jar $ALTIBASE_HOME/lib/Altibase.jar` output, Java runtime, Spring Boot/Spring Data/Hibernate/Hikari versions, JDBC URL/properties, Adapter for JDBC version and target driver, failover topology, SSL/TLS settings, and full error/log/output before declaring compatibility, root cause, or failover behavior. | GPTs/attachments/11_java_jdbc_spring.md | FCA-J030 | `GAP-J002-012`; `GAP-J002-014`; Korean JDBC and Adapter manuals; approved Spring Data JPA guides; catalog row SRC-OTHER-XVER-000225. |

### FCA-J029 PSM And External Procedure Runtime Guardrail

FCA-J029 cataloged one PSM/external procedure guardrail row. The selected manuals
provide syntax, build commands, metadata checks, and troubleshooting routes, but live
compile, shared-library load, external-agent execution, and runtime-output success
depend on the customer's installed Altibase environment and exact source artifacts.

| source_item_id | status | source_family | version_scope | source_path | source_heading | guardrail_reason | safest_next_check | attachment_target | audit_job | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-OTHER-XVER-000219 | Guardrail | stored_external_procedures | cross-version | GPTs/reports/gap_register.md | Gap Register > GAP-J002-013 > PSM and external procedure examples lack compile/runtime validation | Requires target Altibase version and patch, exact PSM or C/C++ source, compiler and platform, `$ALTIBASE_HOME/lib` deployment state, server runtime, full error or log output, and installed dictionary/view columns before asserting live compile, load, or execution success. | Ask for the exact Altibase version/patch, the PSM or C/C++ source, build command and compiler output, deployed shared-library path, `CREATE LIBRARY`/routine DDL, failed SQL call, full error/log text, and current `SYS_PROCEDURES_`, `SYS_LIBRARIES_`, `V$EXTPROC_AGENT`, `V$LIBRARY`, `V$PROCINFO`, and `V$PROPERTY` evidence before declaring success or root cause. | GPTs/attachments/10_psm_stored_external_procedures.md | FCA-J029 | `GAP-J002-013`; Korean Stored Procedures and External Procedures manuals build/runtime sections; catalog row SRC-OTHER-XVER-000219. |

### FCA-J027 CDC Log Analyzer And RepMgr Guardrails

FCA-J027 cataloged one Replication Manager guardrail row. The selected manuals and
release notes identify package names, Java/JDBC prerequisites, and download route, but
they do not provide a stable file manifest for every Replication Manager distribution
or installed tool state.

| source_item_id | status | source_family | version_scope | source_path | source_heading | guardrail_reason | safest_next_check | attachment_target | audit_job | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-TOOL-XVER-000011 | Guardrail | replication_manager | cross-version | Manuals/Tools/Altibase_release/kor/Replication Manager User's Manual.md | Replication Manager User's Manual and release notes > package-manifest boundary | Stable package contents and installed-file manifests depend on the exact Replication Manager release, downloaded distribution, OS package, bundled JRE state, and local installation; selected sources support package names and prerequisites but not a definitive manifest for every distribution. | Ask for exact Replication Manager release, downloaded archive name, OS package, install directory listing, bundled or external JRE state, and JDBC driver files before asserting package-file contents; otherwise answer only with source-backed package names, runtime requirements, and installation/removal route. | GPTs/attachments/09_replication_ha_cdc.md | FCA-J027 | `GAP-J002-011`; Korean Replication Manager release manual lines 280-295 and Korean 1.2/1.4 release-note package sections; catalog row SRC-TOOL-XVER-000011. |

### FCA-J026 Replication And HA Guardrails

FCA-J026 cataloged the replication and HA source-family slice. The only new guardrail
is the exact cross-version replication compatibility boundary: answers may use the
documented LAZY compatibility matrix and 8.1 verified-source wording, but must not
generalize to unsupported Sender/Receiver directions, optional features, or EAGER/DDL
cases without target evidence.

| source_item_id | status | source_family | version_scope | source_path | source_heading | guardrail_reason | safest_next_check | attachment_target | audit_job | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-REPL-XVER-000034 | Guardrail | replication_manual | cross-version | Manuals/Altibase_7.3/kor/Replication Manual.md | Replication Manual > replication compatibility > version and protocol boundary | Exact cross-version compatibility depends on Sender/Receiver direction, `product_version`, `meta_version`, `repl_protocol_version`, replication mode, option list, and feature use; selected sources support only documented pairings and guard 8.1-to-older or optional-feature claims without target evidence. | Ask for both nodes' `V$VERSION` output, Sender/Receiver direction, replication mode, replication object options, DDL/offline/SSL/receive-only involvement, and target object list before declaring compatibility; otherwise answer only with the documented source-backed boundary and safest next checks. | GPTs/attachments/09_replication_ha_cdc.md | FCA-J026 | Korean Replication Manual 7.3 compatibility appendix plus Altibase 8.1 verified-source release-note compatibility wording; catalog evidence `SRC-REPL-XVER-000034`; attachment evidence `Compatibility Guidance`. |

### FCA-J025 Monitoring API And SNMP Guardrails

FCA-J025 cataloged Monitoring API and SNMP source rows. Most items are covered in the
current attachments, but live API/SNMP runtime behavior and three SNMP trap severity or
code details remain source- or environment-limited. Answers must request the exact
target version and live output before hard-coding those runtime values.

| source_item_id | status | source_family | version_scope | source_path | source_heading | guardrail_reason | safest_next_check | attachment_target | audit_job | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-OTHER-XVER-000184 | Guardrail | monitoring_api_snmp | cross-version | Manuals/Altibase_7.3/kor/Monitoring API Developer's Guide.md | Monitoring API Developer's Guide and SNMP Agent Guide > live runtime validation boundary | Runtime confirmation of sample SQL, Monitoring API calls, SNMP counters, traps, ports, and daemon output depends on an installed target Altibase environment and cannot be proven from selected source manuals alone. | Ask for exact Altibase version and patch, host topology, installed Monitoring API/SNMP package state, API program output, `snmpwalk` output, `snmptrapd` output, daemon config files, and relevant logs before asserting live behavior. | GPTs/attachments/08_performance_tuning_monitoring.md | FCA-J025 | `GAP-J002-009`; `review/reports/R15_monitoring_snmp_api.md`; catalog evidence `rg -n 'Monitoring API/SNMP validation\|snmpwalk\|snmptrapd\|live Altibase host' GPTs/reports/gap_register.md GPTs/attachments/08_performance_tuning_monitoring.md`. |
| SRC-OTHER-XVER-000200 | Guardrail | monitoring_api_snmp | cross-version | Manuals/Altibase_7.3/kor/SNMP Agent Guide.md | SNMP Agent Guide > Trap code > Altibase UnRunning Status | The selected SNMP source has an internal level conflict for `10000002`: the section level field says `3`, while sample `snmptrapd` output says `altiTrapLevel = 1`. | Ask for exact target version and sample `snmptrapd` output before hard-coding alert severity for `10000002`; otherwise state only that it means Altibase is not running and that severity must be validated. | GPTs/attachments/08_performance_tuning_monitoring.md | FCA-J025 | Korean SNMP Agent Guide 7.3 lines 1458-1485; R15 notes same conflict across checked guides; catalog evidence `rg -n '10000002\|Altibase is not running\|altiTrapLevel = 1' GPTs/attachments/08_performance_tuning_monitoring.md`. |
| SRC-OTHER-XVER-000202 | Guardrail | monitoring_api_snmp | cross-version | Manuals/Altibase_7.3/kor/SNMP Agent Guide.md | SNMP Agent Guide > Trap code > Altibase Subagent UnRunning Status | The selected SNMP source has an internal level conflict for `10000004`: the section level field says `3`, while sample `snmptrapd` output says `altiTrapLevel = 1`. | Ask for exact target version and sample `snmptrapd` output before hard-coding alert severity for `10000004`; otherwise state only that it means `altisnmpd` is not running and that severity must be validated. | GPTs/attachments/08_performance_tuning_monitoring.md | FCA-J025 | Korean SNMP Agent Guide 7.3 lines 1516-1543; R15 notes same conflict across checked guides; catalog evidence `rg -n '10000004\|Altisnmpd is not running\|nsNotifyShutdown' GPTs/attachments/08_performance_tuning_monitoring.md`. |
| SRC-OTHER-XVER-000206 | Guardrail | monitoring_api_snmp | cross-version | Manuals/Altibase_7.3/kor/SNMP Agent Guide.md | SNMP Agent Guide > Trap code > Too Many Continuous Query Failure | The selected SNMP source has an internal trap-code conflict for continuous session failure: the section label says `10000201`, but the sample output uses `altiTrapCode = 10000103`. | Ask for exact target version, `SNMP_ALARM_SESSION_FAILURE_COUNT`, the triggering condition, and actual `snmptrapd` output before hard-coding the continuous-session-failure trap code. | GPTs/attachments/08_performance_tuning_monitoring.md | FCA-J025 | Korean SNMP Agent Guide 7.3 lines 1635-1662; R15 notes the conflict; benchmark evidence VPM-127; catalog evidence `rg -n 'Continuous session failure\|10000201\|10000103\|Session Failed Continuously' GPTs/attachments/08_performance_tuning_monitoring.md`. |

### FCA-J023 Error Reference Source Drift Guardrail

FCA-J023 cataloged the 7.1 `SD Error Code` exact-code rows and added one `Guardrail`
row for the cross-version `sdERR_*` source-drift boundary. Answers must use the 7.1
exact-code map only for 7.1 unless the customer supplies installed-version evidence for
another target.

| source_item_id | status | source_family | version_scope | source_path | source_heading | guardrail_reason | safest_next_check | attachment_target | audit_job | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ERR-XVER-000561 | Guardrail | error_message_reference | cross-version | Manuals/Altibase_7.1/kor/Error Message Reference.md | Error Message Reference > SD Error Code > source drift boundary | Require exact installed version, patch level, full error line, and installed manual/runtime evidence before making a 7.3 or 8.1 `sdERR_*` claim because checked Korean 7.3 and 8.1 sources do not list `SD Error Code`. | Ask for `altibase -v`, full error line, target patch, failed SQL/command, shard metadata or runtime evidence, and installed manual/runtime proof; otherwise keep unsupported cause/action fields as `Unknown from the supplied message`. | GPTs/attachments/07_error_messages_troubleshooting.md | FCA-J023 | source locators: 7.1 Korean Error Message Reference `SD Error Code`; checked 7.3 and 8.1 verified source Korean Error Message References do not list `SD Error Code`; attachment source-drift caution and exact-code map inserted by FCA-J023. |


### FCA-J019 View Column And Metadata Guardrails

FCA-J019 cataloged 7 `Guardrail` rows for exact view-column layout, installed
meta-table layout, version-sensitive replication metadata columns, 8.1 checkpoint
columns, 7.1-only reserved spatial-unit views, replication runtime object identifiers,
and `V$USAGE` statistics prerequisites. Answers must ask for the target version,
patch, and installed metadata or runtime evidence before asserting these details.

| source_item_id | status | source_family | version_scope | source_path | source_heading | guardrail_reason | safest_next_check | attachment_target | audit_job | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-COL-XVER-000015 | Guardrail | general_reference_2_dictionary_views | cross-version | Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md | General Reference 2 > Data Dictionary > Performance Views > installed view layout boundary | Exact view-column layout depends on exact Altibase version, patch level, and installed metadata; selected source manuals do not prove every customer patch layout. | Ask for exact Altibase version and patch level, then query `V$TABLE` and `V$ALLCOLUMN` for the named view before asserting uncommon columns or generating final SQL. | GPTs/attachments/06_data_dictionary_performance_views.md | FCA-J019 | source locators: Korean General Reference 2 `V$TABLE` and `V$ALLCOLUMN` sections; `gap_register.md` `GAP-J002-006`; attachment anchor `Check Whether a Performance View or Column Exists`. |
| SRC-COL-XVER-000016 | Guardrail | general_reference_2_dictionary_views | cross-version | Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md | General Reference 2 > Data Dictionary > Meta Tables > installed SYS_* layout boundary | Exact `SYS_*` meta-table column availability depends on exact version, patch level, and installed metadata; source manuals alone are not enough for uncommon or version-sensitive columns. | Ask for exact version and patch, then query `SYSTEM_.SYS_TABLES_`, `SYSTEM_.SYS_COLUMNS_`, and `SYSTEM_.SYS_USERS_` for the target meta table and column before using it in customer SQL. | GPTs/attachments/06_data_dictionary_performance_views.md | FCA-J019 | source locators: Korean General Reference 2 `SYS_TABLES_` and `SYS_COLUMNS_` sections; attachment response rules and column-list cookbook. |
| SRC-COL-XVER-000017 | Guardrail | general_reference_2_dictionary_views | cross-version | Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md | General Reference 2 > Data Dictionary > Meta Tables > SYS_REPL_ITEMS_ > IS_CONDITION_SYNCED | The answer depends on exact version and installed `SYS_REPL_ITEMS_` layout; `IS_CONDITION_SYNCED` is documented in checked 7.3 and 8.1 layouts but not in the checked 7.1 layout. | Ask for target version and patch, then query `SYSTEM_.SYS_COLUMNS_` for `SYS_REPL_ITEMS_`.`IS_CONDITION_SYNCED`; omit the column in 7.1-compatible SQL unless the installed database exposes it. | GPTs/attachments/06_data_dictionary_performance_views.md | FCA-J019 | source locators: 7.3 Korean General Reference 2 `IS_CONDITION_SYNCED`; checked 7.1 layout lacks the column; attachment replication metadata check. |
| SRC-COL-8.1-000001 | Guardrail | general_reference_2_dictionary_views | 8.1 | Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md | General Reference 2 > Data Dictionary > Performance Views > V$LOG.CHECKPOINT_SCALE and V$MEM_STABLE | The answer depends on whether the target is Altibase 8.1 verified source or an installed system exposing `V$LOG.CHECKPOINT_SCALE` and `V$MEM_STABLE`; portable 7.1/7.3 SQL must not assume these columns. | Ask for exact version and patch, then query `V$TABLE` and `V$ALLCOLUMN` for `V$LOG`, `CHECKPOINT_SCALE`, and `V$MEM_STABLE` before generating checkpoint-scale SQL on non-8.1 targets. | GPTs/attachments/06_data_dictionary_performance_views.md | FCA-J019 | source locators: 8.1 Korean General Reference 2 `V$MEM_STABLE` and `V$LOG.CHECKPOINT_SCALE`; attachment 8.1 stable checkpoint checks. |
| SRC-COL-7.1-000001 | Guardrail | general_reference_2_dictionary_views | 7.1 | Manuals/Altibase_7.1/kor/General Reference-2.The Data Dictionary.md | General Reference 2 > Data Dictionary > Performance Views > reserved spatial unit views | The answer depends on exact target version and installed `V$TABLE`/`V$ALLCOLUMN` results because the selected Korean source lists `V$ST_ANGULAR_UNIT`, `V$ST_AREA_UNIT`, and `V$ST_LINEAR_UNIT` only for 7.1. | For 7.3 or 8.1 questions, do not assert these views or columns from English/source memory; query `V$TABLE` and `V$ALLCOLUMN`, then route Spatial interpretation to `19_spatial_nifi_tableau_misc.md`. | GPTs/attachments/06_data_dictionary_performance_views.md | FCA-J019 | source locators: `dictionary_view_inventory.md` Source Drift Notes and Spatial unit catalog; attachment inventory verification SQL. |
| SRC-COL-XVER-000018 | Guardrail | general_reference_2_dictionary_views | cross-version | Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md | General Reference 2 > Data Dictionary > Replication runtime table object identifiers | The answer depends on live replication state and installed metadata because replication runtime `TABLE_OID` values may not match a current `SYS_TABLES_` row when the referenced table no longer exists at log-processing time. | Ask for topology, replication name, current `V$REPSENDER`/`V$REPRECEIVER` rows, and `SYSTEM_.SYS_TABLES_`/partition metadata before resolving replication runtime object IDs to names. | GPTs/attachments/06_data_dictionary_performance_views.md | FCA-J019 | source locators: Korean General Reference 2 replication runtime notes for `TABLE_OID`; attachment replication runtime column block. |
| SRC-COL-XVER-000019 | Guardrail | general_reference_2_dictionary_views | cross-version | Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md | General Reference 2 > Data Dictionary > Performance Views > V$USAGE | The answer depends on runtime statistics collection state; `V$USAGE` space values are source-backed only after DBMS Stat statistics are collected. | Ask whether DBMS Stats have been collected or run the source-backed `gather_database_stats()`/view-check workflow, then join `V$USAGE.TARGET_ID` to `SYSTEM_.SYS_TABLES_.TABLE_OID` or `SYSTEM_.SYS_INDICES_.INDEX_ID`. | GPTs/attachments/06_data_dictionary_performance_views.md | FCA-J019 | source locators: Korean General Reference 2 `V$USAGE` section; attachment segment, space, and usage view block. |

### FCA-J017 Dictionary And Meta Table Guardrail

FCA-J017 cataloged one `Guardrail` row for a source-version conflict in the General Reference 2 meta-table inventory. Answers must use the installed-metadata check instead of assuming the table exists on Altibase 8.1.

| source_item_id | status | source_family | version_scope | source_path | source_heading | guardrail_reason | safest_next_check | attachment_target | audit_job | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-DICT-XVER-000052 | Guardrail | general_reference_2_dictionary_views | cross-version | Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md | General Reference 2 > Data Dictionary > Meta Tables > SYS_REPL_TABLE_OID_IN_USE_ | Listed in the 7.1 and 7.3 Korean General Reference 2 meta-table lists but absent from the checked Altibase 8.1 verified-source Korean list while the 8.1 release notes state no meta tables were added, deleted, or changed; do not assume 8.1 availability from memory. | Ask for exact Altibase version and patch level, then query `SYSTEM_.SYS_TABLES_` and `SYSTEM_.SYS_COLUMNS_` for `SYS_REPL_TABLE_OID_IN_USE_` before relying on the table or any columns in generated SQL. | GPTs/attachments/06_data_dictionary_performance_views.md | FCA-J017 | source locators: dictionary_view_inventory.md Source Drift Notes and Meta Table Inventory Groups; Korean General Reference 2 lists 7.1/7.3 include `SYS_REPL_TABLE_OID_IN_USE_`, checked 8.1 list does not; rg -n 'SYS_REPL_TABLE_OID_IN_USE_' GPTs/attachments/06_data_dictionary_performance_views.md |


### FCA-J005 Installation And Getting-Started Guardrails

FCA-J005 cataloged 2 `Guardrail` rows. These are acceptable only when answers ask for
the customer evidence below instead of guessing package availability or license status.

| source_item_id | status | source_family | version_scope | source_path | source_heading | guardrail_reason | safest_next_check | attachment_target | audit_job | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-OTHER-XVER-000030 | Guardrail | getting_started_installation | cross-version | Manuals/Altibase_trunk/kor/Installation Guide.md | Installation Guide > Package installer download > support portal package acquisition | Current package download availability depends on exact version, patch, customer entitlement, OS/CPU package naming, and live Altibase Support portal state; selected manuals identify the route but cannot verify current access. | Ask for exact Altibase version/patch, server or client target, OS/version, CPU architecture, and whether the customer has the installer package or support-portal entitlement before giving copy-ready package commands. | GPTs/attachments/01_getting_started_installation.md | FCA-J005 | rg -n 'support.altibase.com\|패키지 인스톨러\|operating system' Manuals/Altibase_trunk/kor/Installation\ Guide.md GPTs/attachments/01_getting_started_installation.md |
| SRC-OTHER-7.1-000001 | Guardrail | getting_started_installation | 7.1 | Manuals/Altibase_7.1/kor/Installation Guide.md | Installation Guide > Register or Update the Altibase License Key > license acquisition | License issuance depends on license type, customer contract, current Altibase Support process, and issued license validity; selected 7.1 source documents historical acquisition paths but cannot verify current entitlement or portal behavior. | Ask for license type, exact Altibase version/patch, whether a license file/key has already been issued, and the current support/contract path; for installation, only state the source-backed placement and startup effect of `$ALTIBASE_HOME/conf/license`. | GPTs/attachments/01_getting_started_installation.md | FCA-J005 | rg -n 'Enterprise Edition\|Trial\|support.altibase.com\|라이선스' Manuals/Altibase_7.1/kor/Installation\ Guide.md GPTs/attachments/01_getting_started_installation.md |

### FCA-J004 Release, Platform, And Scope Guardrails

FCA-J004 cataloged 6 `Guardrail` or `Out-of-scope` rows. These rows remain acceptable only with the missing-input or source-boundary pattern below.

| source_item_id | status | source_family | version_scope | source_path | source_heading | guardrail_reason | safest_next_check | attachment_target | audit_job | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-REL-8.1-000006 | Guardrail | release_notes_platform | 8.1 | ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md | Altibase 8.1.0.0.1 Release Notes > release-note-only feature procedure boundary | Selected release notes confirm availability, but implementation procedures depend on exact feature family, installed package/API, and a dedicated source-backed manual or tool bl... | Ask for exact version/patch, component, OS/CPU/glibc or installed tool/API state as applicable; use only selected source rows or run a dedicated source-backed audit before givin... | GPTs/attachments/00_version_release_platform.md | FCA-J004 | rg -n 'KADA/Kafka/ABM/MindsDB/\.NET 8/node-odbc-altibase/Release-note-only feature scope/Residual Scope' ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md GPTs/attachments/00... |
| SRC-PLAT-XVER-000002 | Guardrail | release_notes_platform | cross-version | Technical Documents/kor/Supported Platforms.md | Supported Platforms > overview > unlisted OS support | The supported-platform source explicitly sends unlisted OS compatibility to Altibase Support; ask for exact Altibase version/patch, component, OS/version, CPU architecture, glib... | Ask for exact version/patch, component, OS/CPU/glibc or installed tool/API state as applicable; use only selected source rows or run a dedicated source-backed audit before givin... | GPTs/attachments/00_version_release_platform.md | FCA-J004 | source locator: Technical Documents/kor/Supported Platforms.md lines 29-34; rg -n 'Altibase Support/Platform Answer Checklist/direct the customer to Altibase Support' GPTs/attac... |
| SRC-PLAT-XVER-000003 | Out-of-scope | release_notes_platform | cross-version | Technical Documents/kor/Supported Platforms.md | Supported Platforms > Altibase 6.5.1 | Altibase 6.5.1 platform support is outside the locked customer-facing upload scope of Altibase 7.1, 7.3, and 8.1; do not use 6.5.1 platform rows to answer 7.x or 8.1 support que... | Ask for exact version/patch, component, OS/CPU/glibc or installed tool/API state as applicable; use only selected source rows or run a dedicated source-backed audit before givin... | N/A | FCA-J004 | source locator: Technical Documents/kor/Supported Platforms.md lines 167-254; rg -n 'Altibase 6.5.1/Do not use 6.5.1 platform support' GPTs/attachments/00_version_release_platfo... |
| SRC-REL-PATCH-000015 | Guardrail | release_notes_platform | patch-specific | ReleaseNotes/kor/Altibase_ShardManager_v.3.2_Release_Notes.md | Altibase Shard Manager Release Notes > release-note document boundary | The locked release-note root contains this product/tool release note, but the 20-file attachment/source-family map has no dedicated answer-ready owner for ShardManager/Sharding/... | Ask for exact version/patch, component, OS/CPU/glibc or installed tool/API state as applicable; use only selected source rows or run a dedicated source-backed audit before givin... | GPTs/attachments/00_version_release_platform.md | FCA-J004 | rg -n 'Release Notes/BUG-' ReleaseNotes/kor/Altibase_ShardManager_v.3.2_Release_Notes.md |
| SRC-REL-PATCH-000016 | Guardrail | release_notes_platform | patch-specific | ReleaseNotes/kor/Altibase_Sharding3_3_2_0_0_1_Release_Notes.md | Altibase Sharding 3 Release Notes > release-note document boundary | The locked release-note root contains this product/tool release note, but the 20-file attachment/source-family map has no dedicated answer-ready owner for ShardManager/Sharding/... | Ask for exact version/patch, component, OS/CPU/glibc or installed tool/API state as applicable; use only selected source rows or run a dedicated source-backed audit before givin... | GPTs/attachments/00_version_release_platform.md | FCA-J004 | rg -n 'Release Notes/BUG-' ReleaseNotes/kor/Altibase_Sharding3_3_2_0_0_1_Release_Notes.md |
| SRC-REL-PATCH-000017 | Guardrail | release_notes_platform | patch-specific | ReleaseNotes/kor/Altibase_Windows2026_2_6_0_0_1_Release_Notes.md | Altibase Windows 2026 Release Notes > release-note document boundary | The locked release-note root contains this product/tool release note, but the 20-file attachment/source-family map has no dedicated answer-ready owner for ShardManager/Sharding/... | Ask for exact version/patch, component, OS/CPU/glibc or installed tool/API state as applicable; use only selected source rows or run a dedicated source-backed audit before givin... | GPTs/attachments/00_version_release_platform.md | FCA-J004 | rg -n 'Release Notes/BUG-' ReleaseNotes/kor/Altibase_Windows2026_2_6_0_0_1_Release_Notes.md |
