# J009 DML, Functions, Data Types, And Oracle-Difference Design Note

## Scope

J009 strengthens customer-facing retrieval blocks for DML, expressions, functions,
JSON, LOB, core data types, object-name rules, and Oracle migration differences.
The primary attachment targets are:

- `GPTs/attachments/04_sql_dml_oracle_compatibility.md`
- `GPTs/attachments/05_data_types_properties.md`
- `GPTs/attachments/15_migration_oracle_compatibility.md`

This job does not edit original manuals, benchmark questions, or benchmark thresholds.

## Evidence Used

- `evals/altibase_answerability/reports/full_benchmark/failure_root_cause_analysis_20260517.md`
- `GPTs/reports/answerability_failure_remediation_inventory_20260517.md`
- `GPTs/reports/exact_token_gap_inventory_20260517.md`
- `evals/altibase_answerability/questions/sql_ddl_dml_datatypes.jsonl`
- Korean Altibase 7.3 and 8.1 SQL Reference sections for `UPDATE`, `DELETE`,
  `MERGE`, `GROUP_CONCAT`, `DECODE`, `NVL2`, `REGEXP_REPLACE`,
  `REGEXP_SUBSTR`, `REGEXP_LIKE`, `ROWNUM`, object-name rules, outer joins,
  and `CREATE REPLICATION`
- Korean Altibase 8.1 General Reference and release notes for native `JSON`,
  JSON path restrictions, Temporary LOB, and LOB restrictions
- Altibase 8.1 Adapter for Oracle source sections already summarized in
  `15_migration_oracle_compatibility.md`

## Documentation Structure Decision

The evidence showed many answer failures where the right topic existed but exact
grammar tokens or conversion cautions were easy to omit. J009 therefore adds dense
item-level anchors near existing sections instead of adding broad prose:

- DML anchors preserve `multiple_update`, `multiple_delete`, `RETURNING`,
  `INSERT SELECT`, `FOR UPDATE`, `WAIT`, `SEC`, `MSEC`, `USEC`, `NOWAIT`,
  set-operator, hierarchical-query, and LATERAL/APPLY restrictions.
- Function anchors preserve literal argument forms for `GROUP_CONCAT`,
  `LISTAGG`, `DECODE`, `NVL2`, `REGEXP_REPLACE`, `REGEXP_SUBSTR`,
  `REGEXP_LIKE`, `CURRVAL`, `NEXTVAL`, and `ROWNUM`.
- JSON anchors preserve 8.1-only scope, `2GB (2,147,483,648 bytes)`,
  `ISO/IEC 19075-6(2021)`, `256`, path literal restrictions, and
  `JSON_QUERY` / `JSON_VALUE` return/default behavior.
- Migration anchors preserve Altibase object-name rules and Oracle outer join
  rewrite tokens such as `A-Z`, `a-z`, `0-9`, `_`, `$`, `#`, `V$`, `X$`,
  `D$`, `LEFT OUTER JOIN`, `RIGHT OUTER JOIN`, `FULL OUTER JOIN`, `(+)`,
  `Semi Join`, and `Anti Join`.

## Source-Safety Notes

Native `JSON` remains scoped to Altibase 8.1 verified source. For 7.1 and 7.3,
answers must not generate native JSON SQL unless the customer supplies exact
target-version proof.

The `CREATE REPLICATION` anchor is included only as a literal SQL-generation
guardrail because J009 evidence contained `replication_host_ip` and
`replication_host_port_no` token misses. Deeper replication state, DDL
replication, gap, CDC, and TLS runbooks remain owned by later replication jobs.

Oracle compatibility guidance remains conservative: common Oracle-style syntax is
listed only where Altibase manuals show support or Migration Center / Adapter for
Oracle sources document a conversion rule. Unsupported Oracle SQL/JSON, PL/SQL,
package, hint, and object semantics still require manual redesign or exact
target-version proof.
