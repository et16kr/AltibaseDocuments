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

### FCA-J029 PSM System Package Retrieval Weaknesses

FCA-J029 cataloged package-level PSM coverage. The current attachment preserves the
system-defined package inventory and routes users to PSM/package context, but several
package families are still weak for routine-level retrieval because the attachment does
not expose complete subprogram signatures, parameter rules, and examples as dedicated
answer-ready blocks.

| source_item_id | current_attachment_anchor | weak_retrieval_aliases | expected_routing_target | benchmark_or_grep_evidence | remediation_owner_job | validation_evidence |
| --- | --- | --- | --- | --- | --- | --- |
| SRC-API-XVER-000038 | `10_psm_stored_external_procedures.md` > `Built-In PSM Facilities` > `System-Defined Packages` | `DBMS_APPLICATION_INFO`, `READ_CLIENT_INFO`, `READ_MODULE`, `SET_ACTION`, `SET_CLIENT_INFO`, `SET_MODULE`, `CLIENT_INFO` | `10_psm_stored_external_procedures.md` > `System Package Routine Reference` | Korean Stored Procedures Manual 7.3 documents `DBMS_APPLICATION_INFO`; `rg -n 'DBMS_APPLICATION_INFO|SET_ACTION|SET_MODULE|CLIENT_INFO' GPTs/attachments/10_psm_stored_external_procedures.md` shows package-level routing only. | FCA-J044 or FCA-J047 | FCA-J029 catalog check and standard validation passed. |
| SRC-API-XVER-000039 | `10_psm_stored_external_procedures.md` > `Built-In PSM Facilities` > `System-Defined Packages` | `DBMS_ALERT`, `REGISTER`, `REMOVE`, `REMOVEALL`, `SET_DEFAULTS`, `SIGNAL`, `WAITANY`, `WAITONE`, `POLLANY`, `POLLONE` | `10_psm_stored_external_procedures.md` > `System Package Routine Reference` | Korean Stored Procedures Manual 7.3 documents `DBMS_ALERT`; `rg -n 'DBMS_ALERT|WAITANY|WAITONE|SIGNAL|POLLANY' GPTs/attachments/10_psm_stored_external_procedures.md` shows package-level routing only. | FCA-J044 or FCA-J047 | FCA-J029 catalog check and standard validation passed. |
| SRC-API-XVER-000040 | `10_psm_stored_external_procedures.md` > `Built-In PSM Facilities` > `System-Defined Packages` | `DBMS_CONCURRENT_EXEC`, concurrent procedure execution, parallel procedure, job wait | `10_psm_stored_external_procedures.md` > `System Package Routine Reference` | Korean Stored Procedures Manual 7.3 documents `DBMS_CONCURRENT_EXEC`; `rg -n 'DBMS_CONCURRENT_EXEC|concurrent' GPTs/attachments/10_psm_stored_external_procedures.md` shows package-level routing only. | FCA-J044 or FCA-J047 | FCA-J029 catalog check and standard validation passed. |
| SRC-API-XVER-000041 | `10_psm_stored_external_procedures.md` > `Built-In PSM Facilities` > `System-Defined Packages`; `Dynamic SQL` | `DBMS_SQL`, `OPEN_CURSOR`, `PARSE`, `BIND_VARIABLE`, `EXECUTE`, `FETCH_ROWS`, `COLUMN_VALUE`, `CLOSE_CURSOR` | `10_psm_stored_external_procedures.md` > `System Package Routine Reference` and `Dynamic SQL` | Korean Stored Procedures Manual 7.3 documents `DBMS_SQL`; `rg -n 'DBMS_SQL|OPEN_CURSOR|PARSE|BIND_VARIABLE|FETCH_ROWS|COLUMN_VALUE' GPTs/attachments/10_psm_stored_external_procedures.md` shows incomplete routine-level retrieval. | FCA-J044 or FCA-J047 | FCA-J029 catalog check and standard validation passed. |
| SRC-API-XVER-000042 | `10_psm_stored_external_procedures.md` > `Built-In PSM Facilities` > `System-Defined Packages` | `DBMS_STATS`, `GATHER_DATABASE_STATS`, `GATHER_SCHEMA_STATS`, `GATHER_TABLE_STATS`, `DELETE_TABLE_STATS`, `SET_TABLE_STATS`, `SHOW_STAT` | `10_psm_stored_external_procedures.md` > `System Package Routine Reference`; `08_performance_tuning_monitoring.md` statistics routes | Korean Stored Procedures Manual 7.3 documents `DBMS_STATS`; `rg -n 'DBMS_STATS|GATHER_DATABASE_STATS|GATHER_TABLE_STATS|SHOW_STAT' GPTs/attachments/10_psm_stored_external_procedures.md` shows package-level routing only. | FCA-J044 or FCA-J046 | FCA-J029 catalog check and standard validation passed. |
| SRC-API-XVER-000043 | `10_psm_stored_external_procedures.md` > `Built-In PSM Facilities` > `System-Defined Packages` | `UTL_RAW`, `CAST_TO_RAW`, `CAST_TO_VARCHAR`, `UTL_SMTP`, `MAIL`, `RCPT`, `DATA`, `QUIT`, `UTL_TCP`, `READ_LINE`, `WRITE_LINE` | `10_psm_stored_external_procedures.md` > `System Package Routine Reference` | Korean Stored Procedures Manual 7.3 documents `UTL_RAW`, `UTL_SMTP`, and `UTL_TCP`; attachment preserves package names but not complete routine contracts. | FCA-J044 or FCA-J047 | FCA-J029 catalog check and standard validation passed. |
| SRC-API-XVER-000044 | `10_psm_stored_external_procedures.md` > `Built-In PSM Facilities` > `System-Defined Packages`; `File Control` | `DBMS_LOCK`, `DBMS_METADATA`, `DBMS_OUTPUT`, `DBMS_RANDOM`, `DBMS_RECYCLEBIN`, `DBMS_SQL_PLAN_CACHE`, `DBMS_STANDARD`, `DBMS_UTILITY`, `STANDARD`, `SYS_SPATIAL`, `UTL_COPYSWAP`, `UTL_FILE` | `10_psm_stored_external_procedures.md` > `System Package Routine Reference`; `File Control` | Korean Stored Procedures Manual 7.3 documents the remaining package sections; `rg -n 'DBMS_LOCK|DBMS_METADATA|DBMS_OUTPUT|DBMS_RANDOM|UTL_FILE|SYS_SPATIAL' GPTs/attachments/10_psm_stored_external_procedures.md` shows broad package routing only. | FCA-J044 or FCA-J047 | FCA-J029 catalog check and standard validation passed. |

### FCA-J024 Performance Plan Node Retrieval Weaknesses

FCA-J024 cataloged three documented plan-node items that are present only as token-level
or result-cache list coverage in `08_performance_tuning_monitoring.md`. Later retrieval
remediation should add aliases or dedicated plan-node blocks and then update the catalog
rows to `Covered-by-routing` or `Covered`.

| source_item_id | current_attachment_anchor | weak_retrieval_aliases | expected_routing_target | benchmark_or_grep_evidence | remediation_owner_job | validation_evidence |
| --- | --- | --- | --- | --- | --- | --- |
| SRC-OTHER-XVER-000149 | `08_performance_tuning_monitoring.md` > `Result Cache` | `GROUP-CUBE`, `GROUP BY CUBE`, plan node, cube aggregation | `08_performance_tuning_monitoring.md` > `Plan Node Reference` | Korean Performance Tuning Guide 7.3 lines 3959-4009 document `GROUP-CUBE`; `rg -n 'GROUP-CUBE\|GROUP BY CUBE' GPTs/attachments/08_performance_tuning_monitoring.md` shows token-level result-cache coverage only. | FCA-J046 or FCA-J043 | FCA-J024 catalog check and standard validation passed. |
| SRC-OTHER-XVER-000150 | `08_performance_tuning_monitoring.md` > `Result Cache` | `GROUP-ROLLUP`, `GROUP BY ROLLUP`, plan node, rollup aggregation | `08_performance_tuning_monitoring.md` > `Plan Node Reference` | Korean Performance Tuning Guide 7.3 lines 4009-4053 document `GROUP-ROLLUP`; `rg -n 'GROUP-ROLLUP\|GROUP BY ROLLUP' GPTs/attachments/08_performance_tuning_monitoring.md` shows token-level result-cache coverage only. | FCA-J046 or FCA-J043 | FCA-J024 catalog check and standard validation passed. |
| SRC-OTHER-XVER-000168 | `08_performance_tuning_monitoring.md` > `Result Cache` | `WINDOW  SORT`, `WINDOW-SORT`, `OVER` clause, analytic plan node | `08_performance_tuning_monitoring.md` > `Plan Node Reference` | Korean Performance Tuning Guide 7.3 lines 5432-5481 document `WINDOW  SORT`; `rg -n 'WINDOW\|WINDOW-SORT\|WINDOW  SORT' GPTs/attachments/08_performance_tuning_monitoring.md` shows token-level result-cache coverage only. | FCA-J046 or FCA-J043 | FCA-J024 catalog check and standard validation passed. |
