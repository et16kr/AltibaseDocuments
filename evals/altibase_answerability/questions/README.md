# Questions

Question files are JSONL files, preferably one file per benchmark domain.

Each line must validate against `../schemas/question.schema.json`. Question-generation
jobs must use the selected repository-local source corpus, prefer Korean manuals where
paired Korean and English manuals exist, and write expected facts in canonical English.
Use `../source_taxonomy.json` and `../SOURCE_COVERAGE_MAP.md` for the durable mapping
from domains to selected source families, target counts, user-level mix, version-scope
mix, answer type mix, retrieval risk, and exclusion notes.

Suggested future files:

- `properties.jsonl`
- `sql_ddl_dml_datatypes.jsonl`
- `operations_admin.jsonl`
- `views_performance_monitoring.jsonl`
- `replication_cdc_security_network.jsonl`
- `errors_troubleshooting.jsonl`
- `tools_apis_connectors_migration.jsonl`

Production manifests should select the domain files above, not the fixture seed file.
The validator's default `full` profile enforces the 200-question total and per-domain
minimums from `../policy.json`. Use `--profile fixture` only for small offline
calibration manifests such as `../manifests/fixture_seed.json`.
