# Questions

Question files are JSONL files, preferably one file per benchmark domain.

Each line must validate against `../schemas/question.schema.json`. Question-generation
jobs must use the selected repository-local source corpus, prefer Korean manuals where
paired Korean and English manuals exist, and write expected facts in canonical English.

Suggested future files:

- `properties.jsonl`
- `sql_ddl_dml_datatypes.jsonl`
- `operations_admin.jsonl`
- `views_performance_monitoring.jsonl`
- `replication_cdc_security_network.jsonl`
- `errors_troubleshooting.jsonl`
- `tools_apis_connectors_migration.jsonl`
