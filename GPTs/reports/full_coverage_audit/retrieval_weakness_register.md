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
