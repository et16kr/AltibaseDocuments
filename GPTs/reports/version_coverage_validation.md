# Version Coverage QA Report

Job: `JOB-082`
Phase: P8 QA
Date: 2026-05-14
Result: Pass

## Objective

Validate that every customer-facing attachment in `GPTs/attachments/`, excluding `README.md`, contains guidance for Altibase 7.1, 7.3, and 8.1.

## Validation Criteria

An attachment passes when it has all of the following:

- `Applicable Versions` coverage for 7.1, 7.3, and 8.1.
- `Source Documents` or equivalent source coverage for 7.1, 7.3, and 8.1.
- Version-specific operational, SQL, compatibility, or feature guidance in the body.
- Customer-safe 8.1 wording such as `Altibase 8.1 verified source`.

## Automated Marker Check

Command:

```bash
for f in GPTs/attachments/*.md; do
  [ "$(basename "$f")" = README.md ] && continue
  b=$(basename "$f")
  printf '%s|' "$b"
  for v in "7.1" "7.3" "8.1"; do
    if rg -q "^- $v:|^\| $v |^Version block: $v|^$v:|^### Altibase $v|^### $v| $v:" "$f"; then
      printf ' %s:yes' "$v"
    else
      printf ' %s:no' "$v"
    fi
  done
  printf '\n'
done
```

Output:

```text
00_version_release_platform.md| 7.1:yes 7.3:yes 8.1:yes
01_getting_started_installation.md| 7.1:yes 7.3:yes 8.1:yes
02_administration_operations.md| 7.1:yes 7.3:yes 8.1:yes
03_sql_ddl_generation.md| 7.1:yes 7.3:yes 8.1:yes
04_sql_dml_oracle_compatibility.md| 7.1:yes 7.3:yes 8.1:yes
05_data_types_properties.md| 7.1:yes 7.3:yes 8.1:yes
06_data_dictionary_performance_views.md| 7.1:yes 7.3:yes 8.1:yes
07_error_messages_troubleshooting.md| 7.1:yes 7.3:yes 8.1:yes
08_performance_tuning_monitoring.md| 7.1:yes 7.3:yes 8.1:yes
09_replication_ha_cdc.md| 7.1:yes 7.3:yes 8.1:yes
10_psm_stored_external_procedures.md| 7.1:yes 7.3:yes 8.1:yes
11_java_jdbc_spring.md| 7.1:yes 7.3:yes 8.1:yes
12_c_cli_odbc_precompiler.md| 7.1:yes 7.3:yes 8.1:yes
13_isql_iloader_basic_tools.md| 7.1:yes 7.3:yes 8.1:yes
14_utilities_operation_tools.md| 7.1:yes 7.3:yes 8.1:yes
15_migration_oracle_compatibility.md| 7.1:yes 7.3:yes 8.1:yes
16_dblink_external_connectors.md| 7.1:yes 7.3:yes 8.1:yes
17_kubernetes_aku_cloud.md| 7.1:yes 7.3:yes 8.1:yes
18_security_ssl_tls.md| 7.1:yes 7.3:yes 8.1:yes
19_spatial_nifi_tableau_misc.md| 7.1:yes 7.3:yes 8.1:yes
```

## Attachment Review Matrix

| Attachment | Result | Version guidance found |
| --- | --- | --- |
| `00_version_release_platform.md` | Pass | Dedicated 7.1, 7.3, and 8.1 release summaries, platform blocks, compatibility matrix, and version-specific answer rules. |
| `01_getting_started_installation.md` | Pass | `Version Differences` covers package and platform guidance for 7.1, 7.3, and 8.1, including 8.1 upgrade cautions. |
| `02_administration_operations.md` | Pass | `Version Differences` covers 7.1 and 7.3 administrator behavior and 8.1 checkpoint-scale guidance. |
| `03_sql_ddl_generation.md` | Pass | `Version Differences` covers 7.1, 7.3, and 8.1 DDL boundaries, including 8.1 `IF EXISTS`, `IF NOT EXISTS`, `JSON`, Temporary LOB, and replication SSL. |
| `04_sql_dml_oracle_compatibility.md` | Pass | `Version Differences` table covers 7.1 and 7.3 DML baselines and 8.1 JSON function guidance. |
| `05_data_types_properties.md` | Pass | `Version Differences` covers 7.1 and 7.3 baseline data types and 8.1 `JSON`, Temporary LOB, and property changes. |
| `06_data_dictionary_performance_views.md` | Pass | `Version Notes` covers 7.1, 7.3, and 8.1 view availability, including 8.1 `V$MEM_STABLE` and `V$TEMPORARY_LOBS`. |
| `07_error_messages_troubleshooting.md` | Pass | `Version Differences` covers 7.1, 7.3, and 8.1 error-source selection and 8.1 JSON/Temporary LOB/replication SSL sensitivity. |
| `08_performance_tuning_monitoring.md` | Pass | `Version Notes` covers 7.1 and 7.3 tuning source usage and 8.1 JSON plan release-note limits. |
| `09_replication_ha_cdc.md` | Pass | `Compatibility Guidance` provides 7.1 and 7.3 replication compatibility blocks and an 8.1 block for replication SSL and exact protocol checks. |
| `10_psm_stored_external_procedures.md` | Pass | `Version Differences` table covers 7.1, 7.3, and 8.1 PSM, idempotent DDL, VARRAY, external mode, Temporary LOB, and case-sensitivity guidance. |
| `11_java_jdbc_spring.md` | Pass | `Version Differences` has separate 7.1, 7.3, and 8.1 blocks for driver files, Maven availability, LOB behavior, Java compatibility, statement cache, and JSON/Temporary LOB caveats. |
| `12_c_cli_odbc_precompiler.md` | Pass | `Version Differences` has separate 7.1, 7.3, and 8.1 blocks for CLI/ODBC/ACI/APRE, ordinary LOBs, and 8.1 JSON LOB cleanup. |
| `13_isql_iloader_basic_tools.md` | Pass | `Version Differences` has separate 7.1, 7.3, and 8.1 blocks for iSQL/iLoader workflows and option-availability caution. |
| `14_utilities_operation_tools.md` | Pass | `Version Differences` has separate 7.1, 7.3, and 8.1 blocks for utility roles, `aexport`, `aku`, `dataCompJ`, and installed-client option checks. |
| `15_migration_oracle_compatibility.md` | Pass | `Applicable Versions`, `Source Documents`, `Tool and Version Scope`, response rules, and JSON conversion blocks cover 7.1, 7.3, and 8.1. |
| `16_dblink_external_connectors.md` | Pass | `Version Differences` has separate 7.1, 7.3, and 8.1 blocks for DB Link, Hadoop Connector, DBeaver, Hibernate, and idempotent DB Link DDL. |
| `17_kubernetes_aku_cloud.md` | Pass | `Version Differences` has separate 7.1, 7.3, and 8.1 blocks for AKU replica limits, Kubernetes model, multiple replication configuration, and encrypted password support. |
| `18_security_ssl_tls.md` | Pass | `Version Differences` has separate 7.1, 7.3, and 8.1 blocks for TLS/OpenSSL support, FIPS-related properties, and 8.1 replication SSL. |
| `19_spatial_nifi_tableau_misc.md` | Pass | `Version Differences` has separate 7.1, 7.3, and 8.1 blocks for Spatial SQL, JDBC driver selection, altiShapeLoader, NiFi, and Tableau. |

## Exceptions

No blocking coverage gaps were found.

Structural exceptions documented:

- `09_replication_ha_cdc.md` uses `Compatibility Guidance` instead of a generic `Version Differences` heading because replication version behavior is protocol and mode compatibility driven.
- `15_migration_oracle_compatibility.md` uses `Tool and Version Scope` and migration-specific difference blocks instead of a standalone `Version Differences` heading because Migration Center `7.19` is a tool release and the target Altibase server coverage is expressed through source scope, response rules, and conversion behavior.

## Customer-Facing 8.1 Label Check

The attachments use customer-safe 8.1 wording such as `Altibase 8.1 verified source`. Internal source labels are not required to explain 8.1 guidance in customer-facing files.

## Conclusion

All 20 customer-facing attachment files contain 7.1, 7.3, and 8.1 guidance. The acceptance criteria for `JOB-082` are satisfied.
