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
