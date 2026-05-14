# Upload Package Checklist

Job: `JOB-087`
Phase: P8 QA
Date: 2026-05-14
Result: Upload-ready

## Objective

Prepare the final upload package checklist for the Altibase GPT attachment set.

## Package Scope

Upload the 20 customer-facing Markdown files in `GPTs/attachments/`, excluding
`README.md`.

Do not upload the following as customer-facing knowledge attachments:

- `GPTs/attachments/README.md` - directory guide and maintenance policy.
- `GPTs/reports/` - QA and source traceability work reports.
- `GPTs/internal/` - internal terminology and work material.
- `GPTs/scripts/` - job automation.

`GPTs/GPT_Instructions_Draft.md` is the companion GPT instruction draft if the GPT
configuration needs instruction text, but it is not counted as one of the 20 upload
attachments.

## Upload Manifest

| # | Attachment file | Size | Primary coverage |
| ---: | --- | ---: | --- |
| 1 | `00_version_release_platform.md` | 27047 bytes | Versions, release features, platform support |
| 2 | `01_getting_started_installation.md` | 16956 bytes | Installation, environment setup, first checks |
| 3 | `02_administration_operations.md` | 58521 bytes | Startup, shutdown, storage, backup, recovery, operations |
| 4 | `03_sql_ddl_generation.md` | 77807 bytes | DDL generation, tablespaces, users, constraints, indexes |
| 5 | `04_sql_dml_oracle_compatibility.md` | 39232 bytes | DML, Oracle compatibility, JSON functions |
| 6 | `05_data_types_properties.md` | 48470 bytes | Data types, properties, JSON, Temporary LOB |
| 7 | `06_data_dictionary_performance_views.md` | 47901 bytes | Dictionary views, performance views, verification SQL |
| 8 | `07_error_messages_troubleshooting.md` | 50159 bytes | Error messages, troubleshooting workflows |
| 9 | `08_performance_tuning_monitoring.md` | 68575 bytes | Tuning, monitoring, execution plans, diagnostics |
| 10 | `09_replication_ha_cdc.md` | 61916 bytes | Replication, HA, CDC, protocol compatibility |
| 11 | `10_psm_stored_external_procedures.md` | 40179 bytes | PSM, stored procedures, external procedures |
| 12 | `11_java_jdbc_spring.md` | 36653 bytes | Java, JDBC, Spring, Hibernate |
| 13 | `12_c_cli_odbc_precompiler.md` | 62482 bytes | C, CLI, ODBC, ACI, precompiler |
| 14 | `13_isql_iloader_basic_tools.md` | 38387 bytes | iSQL, iLoader, basic command-line tools |
| 15 | `14_utilities_operation_tools.md` | 45965 bytes | Utilities, export, comparison, diagnostics |
| 16 | `15_migration_oracle_compatibility.md` | 48153 bytes | Migration, Oracle compatibility, Migration Center |
| 17 | `16_dblink_external_connectors.md` | 51975 bytes | DB Link, external connectors, third-party integration |
| 18 | `17_kubernetes_aku_cloud.md` | 26033 bytes | AKU, Kubernetes, cloud deployment notes |
| 19 | `18_security_ssl_tls.md` | 25361 bytes | SSL/TLS, FIPS-related settings, security operations |
| 20 | `19_spatial_nifi_tableau_misc.md` | 58306 bytes | Spatial, NiFi, Tableau, miscellaneous connectors |

## QA Gate Checklist

| Gate | Evidence | Result |
| --- | --- | --- |
| Attachment count | `GPTs/reports/attachment_count_validation.md`; final command output below | Pass |
| Forbidden customer-facing strings | `GPTs/reports/forbidden_strings_validation.md`; final command output below | Pass |
| Version coverage | `GPTs/reports/version_coverage_validation.md` confirms all 20 attachments cover Altibase 7.1, 7.3, and 8.1 | Pass |
| English canonical content | `GPTs/reports/english_consistency_validation.md` reports no Korean-script leakage and confirms customer-safe 8.1 wording in all 20 attachments | Pass |
| SQL generation readiness | `GPTs/reports/sql_generation_test_results.md` reports 20 prompt checks passed, 0 failed, 0 review needed | Pass |
| Multilingual behavior | `GPTs/reports/multilingual_smoke_results.md` reports 18 prompt checks across 9 language groups passed, 0 failed, 0 review needed | Pass |
| Source audit | `GPTs/reports/source_audit.md` reports high-risk claims trace to source manuals, release notes, or accepted source reports | Pass |

## Upload Rules

- Upload all 20 files listed in the manifest.
- Keep filenames unchanged so topic routing and source references remain stable.
- Keep attachment files as canonical English.
- Configure the GPT to answer in the user's language while preserving SQL object names,
  function names, error codes, property names, commands, file paths, API names, and
  version labels literally.
- Preserve customer-safe 8.1 wording such as `Altibase 8.1 verified source`.
- Do not expose repository branch names, local paths, workstation paths, or internal
  build labels in customer answers.
- When version-specific behavior matters and the user did not provide an Altibase
  version, the GPT should ask for the version before giving final SQL or operational
  instructions.

## Known Source Caveats

The source audit found no blocking upload issues. These narrow areas are source-backed
but should remain conservative in generated answers:

- Altibase 8.1 JSON details, Temporary LOB details, replication SSL details, JSON error
  blocks, and `SQLFreeLob2` guidance rely on the verified 8.1 source set where English
  manuals are incomplete.
- JSON-format execution plan support is release-note-backed; do not invent JSON plan
  field names, property values, or example output.
- Replication compatibility should remain patch-aware and version-specific.

## Final Validation Commands

```bash
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' | wc -l
```

Output:

```text
20
```

```bash
rg -n "trunk|C:/|file://" GPTs/attachments || true
```

Output:

```text
No matches.
```

## Conclusion

The package is upload-ready. The 20 attachment files are present, English canonical,
version-covered for Altibase 7.1, 7.3, and 8.1, free of the required forbidden strings,
and backed by the completed P8 QA reports.
