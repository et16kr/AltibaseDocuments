# Full Coverage Audit Retrieval Weakness Register

- Workflow: `altibase-gpt-full-coverage-audit`
- Initialized by: `FCA-J003`
- Status: Active register for unresolved `Retrieval-weak` catalog or matrix rows

## Register Contract

Add one entry for every item that is present in the attachment set but unlikely to be
found reliably by GPT retrieval. A `Retrieval-weak` row remains unresolved until a later
job adds routing aliases, indexes, cross-links, heading fixes, or other retrieval proof
and updates the row to `Covered-by-routing` or another justified disposition.

Each entry should record:

- `source_item_id`
- current attachment anchor
- missing or weak retrieval aliases
- expected routing target
- benchmark question IDs or grep evidence when applicable
- remediation owner job
- validation evidence

## Active Retrieval Weaknesses

### FCA-J046 Core Reference Attachments 00-09

`FCA-J046` found no active `Retrieval-weak` catalog or matrix rows for
`GPTs/attachments/00_version_release_platform.md` through
`GPTs/attachments/09_replication_ha_cdc.md` at job start. The scoped audit still
strengthened the core attachment routing layer because the latest locked benchmark
run records high retrieval risk across release/platform, installation, operations,
SQL, data type/property, dictionary/view, error, tuning, and replication domains.

Remediation applied by `FCA-J046`:

- Added focused routing-anchor bullets to the `Retrieval Alias Index` in attachments
  `00` through `09`.
- Repeated exact tokens needed for customer retrieval and answer preservation, such as
  `$ALTIBASE_HOME/conf/altibase.properties`, `ALTIBASE_property_name`, `V$TABLE`,
  `V$ALLCOLUMN`, `NAME`, `COLUMNCOUNT`, `TABLENAME`, `COLNAME`,
  `idERR_FATAL_idc_SVC_INET_BIND_ERROR`, `errno`, `Active-Active`, `Conflict`,
  `User-Oriented Scheme`, `Master-Slave Scheme`, and `Timestamp-based Scheme`.
- Linked broad customer wording to the already answer-ready section headings in each
  scoped attachment, including property configuration, performance-view availability,
  protected backup/recovery, DDL syntax, JSON/DML, exact error blocks, plan-node
  reference, and replication conflict/CDC/network sections.

Disposition note: no catalog or matrix rows required a `Retrieval-weak` to
`Covered-by-routing` status transition because the scoped unresolved-row count was
already zero. This entry records the routing-hardening proof and regression guard for
the core attachment group.

Validation evidence:

```bash
awk -F '\t' 'NR==1{for(i=1;i<=NF;i++) h[$i]=i; next} $h["coverage_status"]=="Retrieval-weak" && $h["attachment_target"] ~ /^GPTs\/attachments\/(0[0-9])_/ {print $h["source_item_id"]}' GPTs/reports/full_coverage_audit/source_to_attachment_matrix.tsv | wc -l
awk -F '\t' 'NR==1{for(i=1;i<=NF;i++) h[$i]=i; next} $h["coverage_status"]=="Retrieval-weak" && $h["attachment_target"] ~ /^GPTs\/attachments\/(0[0-9])_/ {print $h["source_item_id"]}' GPTs/reports/full_coverage_audit/source_item_catalog.tsv | wc -l
```

Both commands returned `0`.

### FCA-J047 Developer Tools And Integration Attachments 10-19

`FCA-J047` found no active `Retrieval-weak` catalog or matrix rows for
`GPTs/attachments/10_psm_stored_external_procedures.md` through
`GPTs/attachments/19_spatial_nifi_tableau_misc.md` at job start. The scoped audit
still strengthened the developer-tool and integration routing layer because the latest
locked benchmark run records high retrieval risk and exact-token misses in the
`tools_apis_connectors_migration` domain.

Remediation applied by `FCA-J047`:

- Added focused routing-anchor bullets to the `Retrieval Alias Index` in attachments
  `10` through `19`.
- Repeated exact tokens needed for customer retrieval and answer preservation, such as
  `RETURN data_type`, `CREATE LIBRARY`, `jdbc:Altibase://localhost:20300/mydb`,
  `jdbc:Altibase://127.0.0.1:20300/mydb?lob_null_select=off`,
  `SQLFreeLob2(stmt, locator)`, `employees.fmt`, `DBMS_METADATA`,
  `./migcenter.sh filesync project_path`, `altibase_sqoop14_connector.jar`,
  `publishNotReadyAddresses: true`, `truststore_url`, and
  `SELECT * FROM SPATIAL_REF_SYS`.
- Linked broad customer wording to already answer-ready section headings for PSM and
  external procedures, JDBC/Spring/Hibernate, C/CLI/ODBC/APRE, iSQL/iLoader, utilities,
  migration/Adapter for Oracle, DB Link/Hadoop connectors, Kubernetes/AKU, TLS, and
  Spatial/NiFi/Tableau.

Disposition note: no catalog or matrix rows required a `Retrieval-weak` to
`Covered-by-routing` status transition because the scoped unresolved-row count was
already zero. This entry records the routing-hardening proof and regression guard for
the developer-tools and integration attachment group.

Validation evidence:

```bash
awk -F '\t' 'NR==1{for(i=1;i<=NF;i++) h[$i]=i; next} $h["coverage_status"]=="Retrieval-weak" && $h["attachment_target"] ~ /^GPTs\/attachments\/(1[0-9])_/ {print $h["source_item_id"]}' GPTs/reports/full_coverage_audit/source_to_attachment_matrix.tsv | wc -l
awk -F '\t' 'NR==1{for(i=1;i<=NF;i++) h[$i]=i; next} $h["coverage_status"]=="Retrieval-weak" && $h["attachment_target"] ~ /^GPTs\/attachments\/(1[0-9])_/ {print $h["source_item_id"]}' GPTs/reports/full_coverage_audit/source_item_catalog.tsv | wc -l
```

Both commands returned `0`.

### FCA-J029 PSM System Package Retrieval Weaknesses

Resolved by `FCA-J044`. `SRC-API-XVER-000038` through `SRC-API-XVER-000044` are no
longer active `Retrieval-weak` rows; the active catalog and matrix rows now point to
`10_psm_stored_external_procedures.md` > `System Package Routine Reference`.

| source_item_id | current_attachment_anchor | weak_retrieval_aliases | expected_routing_target | benchmark_or_grep_evidence | remediation_owner_job | validation_evidence |
| --- | --- | --- | --- | --- | --- | --- |

### FCA-J024 Performance Plan Node Retrieval Weaknesses

Resolved by `FCA-J043`. `SRC-OTHER-XVER-000149`, `SRC-OTHER-XVER-000150`, and
`SRC-OTHER-XVER-000168` now have dedicated `Plan Node Reference` blocks in
`08_performance_tuning_monitoring.md` and the active catalog/matrix rows are
`Covered` with `audit_job=FCA-J043`.

## Resolved Retrieval Weaknesses

### FCA-J046 Retrieval Remediation Core Reference Attachments

- Scope: attachments `00` through `09`.
- Active row result: no active scoped `Retrieval-weak` catalog or matrix rows existed
  at job start, so no source item IDs changed disposition in the TSV artifacts.
- Routing remediation: the job strengthened `Retrieval Alias Index` blocks with
  focused section routes, exact-token anchors, and cross-file routing cues for the
  high-risk core-reference domains evidenced by
  `altibase_answerability_20260517_205641`.
- Evidence: attachment grep checks and the zero scoped unresolved-row checks are
  recorded in `remediation_log.md`.

### FCA-J047 Retrieval Remediation Developer Tools And Integrations

- Scope: attachments `10` through `19`.
- Active row result: no active scoped `Retrieval-weak` catalog or matrix rows existed
  at job start, so no source item IDs changed disposition in the TSV artifacts.
- Routing remediation: the job strengthened `Retrieval Alias Index` blocks with
  focused section routes, exact-token anchors, and cross-file routing cues for the
  high-risk developer-tool and integration topics evidenced by
  `altibase_answerability_20260517_205641`.
- Evidence: attachment grep checks and the zero scoped unresolved-row checks are
  recorded in `remediation_log.md`.

### FCA-J044 Content Remediation Tools APIs Clients And Connectors

- Resolved 7 scoped PSM system-package `Retrieval-weak` rows by adding a dedicated
  `System Package Routine Reference` to `10_psm_stored_external_procedures.md`.
- Updated `source_item_catalog.tsv` and `source_to_attachment_matrix.tsv` to
  `Covered` with `audit_job=FCA-J044` and routine-reference attachment anchors.
- Evidence: attachment exact-token checks and source locators are recorded in the
  catalog and matrix rows.

Resolved source item IDs:

- `SRC-API-XVER-000038`
- `SRC-API-XVER-000039`
- `SRC-API-XVER-000040`
- `SRC-API-XVER-000041`
- `SRC-API-XVER-000042`
- `SRC-API-XVER-000043`
- `SRC-API-XVER-000044`

### FCA-J043 Views Performance Replication And Security

- Resolved 3 scoped `Retrieval-weak` plan-node rows by adding dedicated
  `GROUP-CUBE`, `GROUP-ROLLUP`, and `WINDOW SORT` plan-node blocks and strengthening
  the retrieval alias index in `08_performance_tuning_monitoring.md`.
- Updated `source_item_catalog.tsv` and `source_to_attachment_matrix.tsv` to
  `Covered` with `audit_job=FCA-J043` and attachment anchors for the same rows.
- Evidence: attachment exact-token checks and source locators are recorded in the
  catalog and matrix rows.

Resolved source item IDs:

- `SRC-OTHER-XVER-000149`
- `SRC-OTHER-XVER-000150`
- `SRC-OTHER-XVER-000168`
