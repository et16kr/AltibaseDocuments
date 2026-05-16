# Source Taxonomy and Coverage Map

This is the J002 durable planning map for the Altibase answerability benchmark.

## Reconfirmed Scope

- Job requirement: map selected manual/source families to benchmark domains, user
  levels, and target question counts for later question-generation jobs.
- Durable output path: `evals/altibase_answerability/`.
- Source boundary: repository-local selected sources inventoried in
  `GPTs/reports/source_inventory.md`.
- Answer-generation boundary: answering models may use only `GPTs/attachments/*.md`,
  the allowlisted question projection, and optional manifest-selected GPT instruction
  draft material.
- Source authority: Korean Altibase manuals, release notes, patch notes, tool manuals,
  technical documents, and third-party guides are authoritative when paired Korean and
  English sources differ. Expected facts and reference answers stay in canonical
  English.

The machine-readable version of this map is
`evals/altibase_answerability/source_taxonomy.json`; it validates against
`evals/altibase_answerability/schemas/source_taxonomy.schema.json`.

## Domain Targets

| Domain ID | Owner | Minimum | Target | Primary attachment pattern |
| --- | --- | ---: | ---: | --- |
| `properties` | J004 | 40 | 50 | `05`, with checks from `06`, `07`, `09`, `18` |
| `sql_ddl_dml_datatypes` | J005 | 35 | 45 | `03`, `04`, `05`, plus replication, migration, spatial |
| `operations_admin` | J006 | 25 | 35 | `00`, `01`, `02`, `03`, `06`, `13`, `14`, `17` |
| `views_performance_monitoring` | J007 | 20 | 30 | `06`, `08`, with replication and DB Link view checks |
| `replication_cdc_security_network` | J008 | 20 | 30 | `09`, `18`, with `03` and `06` checks |
| `errors_troubleshooting` | J009 | 20 | 30 | `07`, with related operational, property, view, replication, and TLS files |
| `tools_apis_connectors_migration` | J010 | 40 | 50 | `10` through `17`, plus `19` |

Total target: 270 questions. Total required minimum: 200 questions.

## User-Level Mix

The benchmark should include every user level in every domain, but each domain should
weight the levels that best match the source family and risk profile.

| Domain ID | Beginner | Intermediate | Advanced operator | Developer | Expert |
| --- | ---: | ---: | ---: | ---: | ---: |
| `properties` | 4 | 14 | 18 | 4 | 10 |
| `sql_ddl_dml_datatypes` | 4 | 12 | 8 | 13 | 8 |
| `operations_admin` | 5 | 8 | 15 | 2 | 5 |
| `views_performance_monitoring` | 2 | 6 | 10 | 5 | 7 |
| `replication_cdc_security_network` | 2 | 5 | 12 | 4 | 7 |
| `errors_troubleshooting` | 4 | 8 | 10 | 4 | 4 |
| `tools_apis_connectors_migration` | 4 | 11 | 10 | 17 | 8 |

## Version and Risk Bias

Question-generation jobs should prefer cross-version and high-retrieval-risk items over
easy single-version facts, while still covering Altibase 7.1, 7.3, 8.1, and
patch-specific behavior.

| Domain ID | 7.1 | 7.3 | 8.1 | Cross-version | Patch-specific | Low risk | Medium risk | High risk |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `properties` | 8 | 7 | 13 | 15 | 7 | 8 | 22 | 20 |
| `sql_ddl_dml_datatypes` | 6 | 5 | 10 | 19 | 5 | 6 | 19 | 20 |
| `operations_admin` | 6 | 5 | 8 | 12 | 4 | 5 | 14 | 16 |
| `views_performance_monitoring` | 4 | 4 | 6 | 12 | 4 | 4 | 13 | 13 |
| `replication_cdc_security_network` | 5 | 4 | 8 | 9 | 4 | 3 | 10 | 17 |
| `errors_troubleshooting` | 5 | 4 | 5 | 10 | 6 | 4 | 12 | 14 |
| `tools_apis_connectors_migration` | 7 | 7 | 8 | 24 | 4 | 8 | 24 | 18 |

## Source Family Taxonomy

Use the source family IDs in `source_taxonomy.json` when creating question records and
source references. The paths below are planning locators, not answer-generation input.

| Source family ID | Source basis | Primary benchmark use |
| --- | --- | --- |
| `release_notes_platform` | `ReleaseNotes/{kor,eng}`, Supported Platforms | Version availability, changed defaults/ranges, upgrade and platform cautions |
| `patch_notes` | `PatchNotes/*/{kor,eng}` | Patch-specific behavior and compatibility fixes |
| `getting_started_installation` | Getting Started and Installation manuals | Installation, database creation, startup, shutdown, first checks |
| `administrator_operations` | Administrator manuals and SQL Reference | Accounts, tablespaces, backup, restore, recovery, administrative SQL |
| `sql_reference` | SQL Reference manuals | SQL/DDL/DML/DCL syntax, functions, hints, replication SQL, generation constraints |
| `general_reference_1_datatypes_properties` | General Reference 1 | Data types, properties, JSON, LOB, Temporary LOB, property changes |
| `general_reference_2_dictionary_views` | General Reference 2 | Meta tables, performance views, object lookup SQL, monitoring SQL |
| `error_message_reference` | Error Message Reference manuals | Error codes, cause/action, symptom and troubleshooting records |
| `performance_tuning` | Performance Tuning Guides | Optimizer, plans, indexes, joins, statistics, tuning diagnostics |
| `monitoring_api_snmp` | Monitoring API Developer's Guide, SNMP Agent Guide | Monitoring API, SNMP setup, counters, traps, ports |
| `replication_manual` | Replication manuals and SQL Reference | Replication topology, modes, states, DDL, gaps, protected state changes |
| `log_analyzer` | Log Analyzer User's Manuals | CDC, XLog Sender, XLog Collector, Log Analysis API |
| `replication_manager` | Replication Manager manuals and release notes | GUI replication management and tool release boundaries |
| `security_ssl_tls` | SSL/TLS guides, Replication Manual, release notes | Client/server TLS, certificates, cipher settings, replication SSL |
| `stored_external_procedures` | Stored and External Procedures manuals | PSM, functions, procedures, external procedure setup |
| `jdbc_java` | JDBC, Adapter for JDBC, JavaCompatibility, Spring/Hibernate guides | JDBC URLs, drivers, Java compatibility, ORM behavior |
| `c_cli_odbc_precompiler` | CLI, ODBC, C Interface, Precompiler manuals | Client API calls, DSN setup, precompiler, LOB APIs |
| `isql_iloader` | iSQL and iLoader manuals | Command-line SQL sessions, export/import, load files |
| `utilities_datacompj` | Utilities, dataCompJ, utility release notes | aexport, altiComp, aku, altiMon, dataCompJ, dump tools |
| `migration_oracle` | Migration Center, Adapter for Oracle, release notes | Oracle migration, conversion limits, comparison and correction workflows |
| `dblink_hadoop_external_connectors` | DB Link, Hadoop Connector, third-party connector guide | DB Link syntax/views, Hadoop, DBeaver, GoldenGate, connector checks |
| `kubernetes_aku` | Kubernetes and AKU guides, release notes | Container deployment, AKU samples, Kubernetes operations |
| `spatial_nifi_tableau` | Spatial SQL, altiShapeLoader, NiFi, Tableau | GEOMETRY, spatial SQL, shape loading, NiFi and Tableau procedures |
| `technical_documents_support` | JavaCompatibility, ReplicationCompatibility, network check, Supported Platforms | Approved supplemental compatibility and diagnostic material |
| `third_party_guides` | Approved third-party guides | Spring, Hibernate, Kubernetes, AKU, NiFi, Tableau, approved integration procedures |

## Domain Generation Guardrails

- `properties`: include item-level property facts, change support, version changes,
  exact tokens, and verification SQL. Prohibit generic tuning advice that is not
  source-backed.
- `sql_ddl_dml_datatypes`: prefer Altibase-specific syntax, DDL generation, data type
  restrictions, JSON/LOB behavior, and Oracle differences over generic SQL.
- `operations_admin`: include backup/recovery and destructive operation protection.
  Expected facts must request missing environment, object, path, or log inputs when
  needed.
- `views_performance_monitoring`: test view/column selection, portable availability
  checks, plan/tuning behavior, Monitoring API, and SNMP without direct meta-table DML.
- `replication_cdc_security_network`: treat replication state changes and TLS/security
  as protected topics. Include topology, version, gap, property, and network checks.
- `errors_troubleshooting`: keep cause/action source-backed. Require missing logs,
  exact SQL, object definitions, version, or patch level only when needed.
- `tools_apis_connectors_migration`: preserve literal class, method, option, property,
  command, file, and connector names. Do not include unapproved integrations.

## Maintenance Notes

- The taxonomy is judge/planning material. Do not expose it to the answering model.
- Question records should cite concrete manual/source sections in `source_refs`, not just
  a source family ID.
- If later jobs discover a selected source gap or a better subdomain split, update
  `source_taxonomy.json` and this map before adding affected questions.
- Counts in the taxonomy are targets. J004-J010 may exceed targets, but they must not
  fall below each domain's required minimum.
