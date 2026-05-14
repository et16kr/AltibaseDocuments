# Review Remediation Application Report

Date: 2026-05-14
Source: `review/reports/R00_*.md` through `review/reports/R15_multilingual_final_readiness.md`
Scope: customer-facing upload attachments under `GPTs/attachments/`.

## Applied Fixes

| Status | Fix |
| --- | --- |
| `already_applied` | R01/R15: mark 8.1 feature families as release-note-only unless sourced elsewhere |
| `already_applied` | R07/R15: add AIX 7.2 to 8.1 pre-install platform baseline |
| `already_applied` | R07/R15: add AIX 7.2 to 8.1 version differences |
| `already_applied` | R07/R15: remove 8.1-only CHECKPOINT_SCALE from common V$LOG query |
| `already_applied` | R04: make idempotent DDL exception 8.1-only |
| `already_applied` | R03/R10/R15: split ordinary replication syntax from Log Analyzer CDC syntax in attachment 03 |
| `already_applied` | R03: add EAGER restrictions for FOR ANALYSIS and RETRY in attachment 03 notes |
| `already_applied` | R10/R15: move non-SSL replication SYNC after both peer objects exist |
| `already_applied` | R10/R15: move SSL replication SYNC after both peer objects exist |
| `already_applied` | R04: split LOB IN ROW syntax by version in core type grammar |
| `already_applied` | R06/R15: remove PSM_CASE_SENSITIVE_MODE from 8.1-new property list |
| `already_applied` | R04: add 8.1 LOB syntax note to BLOB item |
| `already_applied` | R04: add 8.1 LOB syntax note to CLOB item |
| `already_applied` | R06/R15: reclassify PSM_CASE_SENSITIVE_MODE as cross-version |
| `already_applied` | R06/R15: reclassify REGEXP_MODE as cross-version |
| `already_applied` | R08/R15: add branch-specific not-found diagnostics |
| `already_applied` | R08/R15: split PCRE2 unsupported character set and unexpected error handling |
| `already_applied` | R08/R15: use replication meta tables before runtime views for duplicate replication |
| `already_applied` | R00/R01/R15: remove internal Conversion TODO/JOB label from troubleshooting attachment |
| `already_applied` | R09: add DBMS_SQL_PLAN_CACHE coverage for 7.3/8.1 |
| `already_applied` | R09: replace Monitoring API default credentials with placeholders |
| `already_applied` | R09: replace SNMP default community strings with placeholders |
| `already_applied` | R09/R15: caveat SNMP continuous session failure trap code |
| `already_applied` | R01/R02/R03/R10/R15: replace unsafe Active-Active and sharding overview |
| `already_applied` | R03/R10/R15: split CREATE REPLICATION syntax in attachment 09 |
| `already_applied` | R03/R10/R15: add LAZY-only FOR ANALYSIS note in attachment 09 |
| `already_applied` | R03: add EAGER restriction for START RETRY in attachment 09 |
| `already_applied` | R10/R15: replace mixed replication DDL procedure with separate standard and sync procedures |
| `already_applied` | R12/R15: state SQLGetLob 1-based fromPosition rule |
| `already_applied` | R12/R15: state SQLPutLob 1-based fromPosition rule |
| `already_applied` | R13/R15: correct AKU Kubernetes service field spelling |
| `already_applied` | R11: avoid promising connector-specific TLS property placement from attachment 16 |
| `already_applied` | R13/R15: remove destructive OpenLDAP DROP USER reset |
| `already_applied` | R11: narrow FIPS ALTIBASE_SSL_LOAD_CONFIG wording to ODBC/CLI |
| `already_applied` | R11: add certificate verification caution to ADO.NET example |

## Validation

Result: Pass

- Script validation found no remaining targeted Blocker/High review patterns.
- Re-run the detailed review reports or final readiness review before upload.
