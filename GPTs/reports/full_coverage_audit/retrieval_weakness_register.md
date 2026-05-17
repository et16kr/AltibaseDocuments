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

No full coverage audit `Retrieval-weak` rows have been cataloged yet. The locked latest
benchmark run remains priority evidence for later retrieval jobs, especially high-risk
properties, SQL, view, error, replication, operation, and tool/API tokens.
