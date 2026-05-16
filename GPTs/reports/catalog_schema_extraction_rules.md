# Altibase GPT Catalog Schema And Extraction Rules

Job: `J003`
Status: Active support artifact
Last updated: 2026-05-16

## Reconfirmed Requirement And Boundary

`J003` defines reusable item block schemas and Korean-first extraction rules for later
rebuild jobs. It is a documentation-scope job. It does not directly rewrite the 20
customer-facing upload attachments unless the schema work proves that an attachment
boundary or customer-facing source label must change.

No attachment boundary or source-label change was found in this job. Keep exactly the
existing 20 upload Markdown files under `GPTs/attachments/`, excluding `README.md`.

Target attachments affected by this job: none.

Support artifacts affected by this job:

- `GPTs/reports/catalog_schema_extraction_rules.md`: canonical schema and extraction
  rule report for later jobs.
- `GPTs/reports/source_inventory.md`: source-root inventory cross-reference.
- `GPTs/reports/coverage_matrix.md`: matrix cross-reference and J003 handoff update.
- `GPTs/reports/gap_register.md`: register rules cross-reference.

## Design Note

Later jobs should use this report as the common contract for converting selected
repository-local source material into searchable attachment blocks. The report separates
content shape from topic ownership:

- `GPTs/reports/coverage_matrix.md` says which source families and attachments own a
  topic.
- `GPTs/reports/gap_register.md` says which item-level gaps remain open, guarded, or
  verification-limited.
- This report says how to extract, normalize, structure, cross-reference, and validate
  the resulting item blocks.

Customer-facing attachments must stay canonical English, must preserve literal
technical tokens, and must use `Altibase 8.1 verified source` for 8.1 customer-facing
source labels. Internal source paths and internal source labels belong only in support
reports.

## Scoped Source Families

J003 applies to every source family in the J002 coverage matrix:

- `release_notes_platform`
- `patch_notes`
- `getting_started_installation`
- `administrator_operations`
- `sql_reference`
- `general_reference_1_datatypes_properties`
- `general_reference_2_dictionary_views`
- `error_message_reference`
- `performance_tuning`
- `monitoring_api_snmp`
- `replication_manual`
- `log_analyzer`
- `replication_manager`
- `security_ssl_tls`
- `stored_external_procedures`
- `jdbc_java`
- `c_cli_odbc_precompiler`
- `isql_iloader`
- `utilities_datacompj`
- `migration_oracle`
- `dblink_hadoop_external_connectors`
- `kubernetes_aku`
- `spatial_nifi_tableau`
- `technical_documents_support`
- `third_party_guides`

Authoritative source order:

1. Use the Korean source root for the relevant family and version when it exists.
2. Use the matching English source as extraction help only when it agrees with the
   Korean source.
3. Use Korean release notes, patch notes, technical documents, tool manuals, and
   third-party guides as authoritative when paired sources differ, when the Korean file
   is more specific, or when the relevant source is Korean-only.
4. Use English-only source claims only after recording the source limitation or after
   checking that no paired Korean source exists in the selected corpus.

Default customer answer scope remains Altibase 7.1, 7.3, and 8.1. Do not broaden a
claim to another version family unless the selected source and the customer-facing
version caution are recorded.

## Korean-First Extraction Workflow

Use this workflow for every later item expansion, whether the output is a property
block, syntax block, view block, error block, runbook, tool command, API block, or
integration procedure.

1. Pick the source family and target attachment from `coverage_matrix.md`.
2. Read the source paths and Korean authority/check paths from `source_inventory.md`.
3. Inspect the Korean source first for product behavior, syntax, defaults, ranges,
   examples, warnings, version labels, and diagram semantics.
4. Inspect the English source for extraction wording, but keep the Korean source as the
   technical basis when paired sources differ.
5. Check release notes or patch notes before stating version introduction, removal,
   changed defaults, platform support, compatibility, or patch-sensitive behavior.
6. Translate and normalize Korean-only detail into concise English. Do not paste Korean
   prose into customer-facing attachments.
7. Preserve literal tokens exactly: SQL keywords, object names, function names, property
   names, error codes, commands, options, file paths, package/class/method names,
   connector names, and version labels.
8. Convert screenshots and diagrams to the smallest searchable form that preserves the
   answerable behavior: BNF-like text, item blocks, procedural steps, field/value lists,
   or Mermaid only when relationships matter.
9. Add or update the target attachment block with version scope, examples or check SQL
   when source-backed, related blocks, and uncertainty handling.
10. If a source-backed item is missing but not fixed in the same job, update
    `gap_register.md` with source family, version scope, missing behavior, affected
    attachment, evidence path, and required remediation shape.

When the source does not establish an exact patch level, environment behavior, log
interpretation, object definition, or unsupported compatibility claim, the attachment
block must ask for that missing input and give the safest source-backed next check.

## Common Item Block Contract

Use searchable item blocks rather than large opaque tables for reference material.
Every item block should answer these questions when the source provides the detail:

- What is the item?
- Which Altibase versions or patch levels does it apply to?
- When should the customer use or inspect it?
- What literal syntax, property, view, error code, command, API, or field names matter?
- What example or check step can the customer run?
- What source-backed caution prevents an unsafe overclaim?
- Which attachment or block should be consulted next?

Preferred generic block shape:

```text
### <item kind>: `<literal name>`

- Version scope: <7.1, 7.3, Altibase 8.1 verified source, exact patch, or guardrail>
- Source basis: <customer-safe product/manual/version topic; use the
  coverage_matrix.md source family ID only in support reports>
- Purpose: <one or two concise sentences>
- Use when: <customer task or diagnostic trigger>
- Required inputs: <version, object name, property, log excerpt, environment, if needed>
- Syntax or command: <compact BNF, SQL, command, API signature, or "not applicable">
- Example: <source-backed minimal example or "record gap if missing">
- Check or validation: <SQL, command, output field, view, or procedure>
- Related items: <attachments or literal related tokens>
- Cautions: <version, restart, privilege, compatibility, destructive action, source limit>
```

Do not force every field into every block. Keep the block short when the source only
supports a short note, but preserve version scope, literal tokens, and uncertainty
handling.

## Property Block Schema

Use for server, session, replication, storage, optimizer, logging, network, security,
tool, and feature-control properties.

Required fields when source-backed:

- Name: literal property name.
- Version scope: 7.1, 7.3, Altibase 8.1 verified source, exact patch, or negative scope.
- Meaning: operational behavior controlled by the property.
- Default: source default and changed-default version note if applicable.
- Allowed values or range: units, minimum, maximum, enumerations, and invalid values.
- Dynamic change support: static, dynamic, session-level, system-level, or unknown.
- Change method: `ALTER SYSTEM`, `ALTER SESSION`, property file edit, restart, recreate,
  or installed-tool configuration.
- Check SQL: usually `V$PROPERTY`, a related performance view, or documented metadata.
- Related views/properties: direct dependencies and diagnostic views.
- Cautions: restart requirement, storage allocation impact, replication/security impact,
  version conflict, patch sensitivity, or source limitation.

Preferred shape:

```text
Property block: `<PROPERTY_NAME>`

- Version scope:
- Meaning:
- Default:
- Range or values:
- Dynamic change support:
- Change method:
- Check SQL:
- Related views/properties:
- Cautions:
```

If Korean and English manuals differ for default, range, dynamic-change support, or
version scope, use the Korean value and record the English-source drift in a support
report or the gap register when it affects later work.

## Data Type, Function, And Expression Block Schema

Use for data types, JSON, LOB, Temporary LOB, built-in functions, predicates,
expressions, Oracle-difference notes, and Spatial functions/operators.

Required fields when source-backed:

- Name: literal type, function, predicate, operator, or expression family.
- Version scope: include 8.1-only, 7.x negative scope, or patch-level caveat.
- Purpose and data shape: what data or expression form it supports.
- Syntax: compact BNF-like text for type/function arguments and options.
- Argument or option rules: data type, path expression, length, scale, unit, or null
  handling.
- Return or storage behavior: return type, storage placement, locator behavior, or
  compatibility note.
- Example: minimal SQL preserving literal tokens.
- Related errors/properties/views: for troubleshooting and validation.
- Oracle compatibility: only when Altibase behavior differs or migration risk is high.

For JSON and Temporary LOB material, keep 8.1 source scope explicit and do not project
the feature onto 7.1 or 7.3 unless a later selected source proves equivalent support.

## SQL Syntax And DDL Block Schema

Use for SQL statements, DDL/DCL, administrative SQL, replication SQL, Log Analyzer SQL,
PSM grammar, and generated SQL templates.

Required fields when source-backed:

- Statement or clause name.
- Version scope, including 8.1-only clauses such as `IF EXISTS` or `IF NOT EXISTS`.
- Privilege or server-state prerequisites.
- Compact BNF-like syntax.
- Parameter notes for Altibase-specific clauses.
- Runnable example with safe placeholder names.
- Verification SQL using dictionary/performance views when possible.
- Rollback, cleanup, or destructive-operation caution when relevant.
- Cross-reference to operation, property, error, replication, or migration attachment.

BNF-like notation:

```text
statement_name ::=
  LITERAL_KEYWORD [optional_clause]
  { alternative_a | alternative_b }
  repeated_item [, repeated_item ...]
```

Notation rules:

- Uppercase SQL keywords are literal syntax.
- Backticked names in prose are literal tokens.
- Lowercase names such as `table_name`, `expr`, and `file_path` are placeholders.
- `[ ... ]` means optional.
- `{ A | B }` means choose one alternative.
- `item [, item ...]` means one or more comma-separated items.
- Repeat complete alternatives explicitly when omission could change semantics.
- Do not infer omitted defaults from a diagram if manuals disagree; record the source
  drift and choose the safer generated form.

J010 SQL-specific rules:

- Use `GPTs/reports/sql_syntax_inventory.md` to choose the statement family, target
  attachment, and later-job ownership before converting a SQL Reference syntax diagram.
- Convert a complex diagram into a root statement production plus named clause
  productions; do not collapse backup/recovery, replication, partition, hint, or JSON
  option trees into one opaque line.
- Keep privileges, server state, archive-log mode, replication topology, file-system
  preparation, destructive-operation cautions, and implicit-commit behavior outside the
  BNF block as searchable notes.
- Treat 8.1-only syntax such as `IF EXISTS`, `IF NOT EXISTS`, and Korean-source JSON
  function options as 8.1-only unless the corresponding 7.1 or 7.3 Korean source proves
  the same clause.
- For generation-oriented statements, pair BNF with a minimal example, verification SQL,
  and a missing-input prompt for exact patch level, object definition, environment, log,
  or unsupported compatibility claims.

## Dictionary And Performance View Block Schema

Use for meta tables, dictionary views, performance views, monitoring views, replication
views, and storage/security diagnostic views.

Required fields when source-backed:

- View or table name.
- Version scope and patch sensitivity.
- Purpose: what question the view answers.
- Query timing: normal operation, post-DDL validation, incident triage, replication
  state check, or startup/shutdown check.
- Key columns: only columns confirmed by source or portable metadata inspection.
- Example check SQL.
- Related properties, errors, SQL statements, and attachments.
- Cautions: high-frequency polling, privilege, state dependency, column availability,
  live validation limit.

Portable metadata checks should use source-backed system objects such as `V$TABLE`,
`V$ALLCOLUMN`, `SYSTEM_.SYS_TABLES_`, and `SYSTEM_.SYS_COLUMNS_` when a column layout
is not fully proven across versions.

## Error And Troubleshooting Block Schema

Use for exact error codes, symbols, grouped error topics, log-message patterns, and
diagnostic response templates.

Required fields when source-backed:

- Code: literal error code such as `0x...`.
- Symbol: literal error symbol.
- Message: concise source-normalized message.
- Version scope: including 8.1-only, 7.x, patch, or exact-code guardrail.
- Cause: source-backed cause, not a generic database assumption.
- Action: safe next action in operational order.
- Required customer input: exact version, patch, full error, log excerpt, SQL text,
  object definition, property values, topology, certificate, or client environment.
- Related properties/views/check SQL.
- Related attachments and gap-register anchor when partial.

For grouped errors, keep exact codes searchable inside the block. Do not map a symptom
to an error code unless the user provides that exact code or the selected source proves
the mapping.

## Runbook Block Schema

Use for installation, startup, shutdown, backup, recovery, archive log mode, tablespace
operations, replication, performance, security, migration, Kubernetes/AKU, and tool
workflows.

Required fields when source-backed:

- Goal and version scope.
- Required inputs: exact version/patch, OS/platform, `ALTIBASE_HOME`, server mode,
  object names, topology, ports, certificates, log paths, or tool version.
- Preconditions: privileges, server state, archive mode, replication state, package
  installation, backup availability, or environment variables.
- Steps: numbered, ordered, and copy-ready where source-backed.
- Validation: SQL, command, expected output field, trace/log check, or UI result.
- Stop/rollback conditions: destructive action, restore/recovery boundary, replication
  state risk, TLS mismatch, missing backup, unsupported platform, or unverified source.
- Cross-references: property, view, error, SQL, or tool blocks.

Do not claim a runbook was live-tested unless a validation report records the tested
environment, command, and result.

## Tool, API, Connector, And Integration Block Schema

Use for JDBC, Java, Spring, Hibernate, CLI, ODBC, C Interface, Precompiler, iSQL,
iLoader, utilities, dataCompJ, DB Link, Hadoop Connector, Kubernetes/AKU, Migration
Center, Adapter for Oracle/JDBC, Spatial tooling, NiFi, Tableau, Monitoring API, and
SNMP.

Required fields when source-backed:

- Tool/API/connector name and version scope.
- Runtime prerequisites: driver, shared library, Java/OpenSSL version, DSN, package,
  environment variables, classpath, port, certificate, or server property.
- Command, URL, API signature, configuration key, or field/value list.
- Input and output artifacts: files, reports, dump files, logs, tables, queues, or
  expected UI result.
- Example or minimal procedure.
- Validation step: command output, SQL check, connection test, generated report, or log.
- Cautions: client/server version compatibility, patch sensitivity, platform support,
  live validation limit, security setting, and unsupported connector behavior.

For screenshot-heavy tools, replace the screenshot with menu path, field labels, values,
selected options, button names, and expected result. Keep UI text in English when
customer-facing attachments are updated.

## Compatibility And Migration Block Schema

Use for release/platform differences, patch notes, Java compatibility, replication
compatibility, Oracle migration, cross-version behavior, and unsupported features.

Required fields when source-backed:

- Comparison subject and version pair or source/target.
- Source basis and evidence; keep repository paths and source-family IDs in support
  reports, not customer-facing attachments.
- Supported/unsupported status.
- Exact patch, platform, client, driver, or tool boundary.
- Required customer input before final guidance.
- Safe next check: source-backed SQL, command, release-note check, package check, or
  vendor/source confirmation.
- Customer-facing caution: concise and version-specific.

Do not convert a guardrail into a definitive compatibility matrix unless selected
sources provide that matrix.

## Visual And Table Conversion Rules

Use these rules when a source table, syntax diagram, operational diagram, topology
figure, state diagram, UI screenshot, or console screenshot is the source evidence.

- Large reference table: convert to searchable item blocks or short local lookup tables.
- SQL/PSM/command syntax diagram: convert to BNF-like text; preserve literals and
  option grouping.
- Operational flow: convert to numbered runbook steps; add Mermaid only when branch
  relationships are useful.
- Topology, state, or sequence diagram: use compact Mermaid only when relationships or
  ordering improve retrieval.
- UI screenshot: convert to menu path, fields, selected options, values, and expected
  result.
- Console screenshot: convert to command, expected key output, and validation note.
- Decorative logo/icon: omit unless the source text around it carries answer value.

If a high-risk visual cannot be audited in the job, record the gap with the source path,
version scope, affected attachment, and required conversion type.

## Gap Register Update Rules

Update `GPTs/reports/gap_register.md` when a later job discovers, splits, closes, or
accepts a gap. Required fields:

- Gap ID and concise title.
- Status: `Open`, `Guardrail`, `Verification-limited`, or `Closed-trace`.
- Source family and version scope.
- Missing item or behavior.
- Affected attachment files.
- Evidence paths or review reports.
- Required remediation shape.

Close or split a gap only when the attachment update or support-report decision is
specific enough for a later reviewer to verify. Do not delete closed trace entries when
they carry source-policy risk that later jobs must not reintroduce.

## Customer-Facing Text Rules

When a later job updates `GPTs/attachments/`:

- Keep prose canonical English.
- Answer-language translation is a GPT runtime behavior, not a reason to add multilingual
  attachment sections.
- Preserve literal tokens in every language.
- Use `Altibase 8.1 verified source` for 8.1 source labels.
- Do not expose repository-local paths, branch names, workstation paths, internal build
  labels, or internal source-family IDs.
- Prefer direct, task-oriented blocks over broad narrative.
- Keep common Oracle-overlapping behavior brief unless Altibase differs.
- Cross-reference another attachment when the natural answer spans SQL, properties,
  views, errors, tools, operations, and migration.

## Self-Review Checklist For Later Jobs

Before a later job finishes, check:

- The source family and version scope are explicit.
- Korean source precedence was applied where paired sources exist.
- English source text was not used to override Korean technical detail.
- Customer-facing text is English-normalized and preserves literal tokens.
- Version, patch, platform, and compatibility claims are source-backed.
- Required missing input is requested instead of guessed.
- BNF-like syntax preserves optionality, alternatives, and repeat semantics.
- Examples and check SQL are source-backed and do not imply untested live validation.
- Known gaps are closed, split, or updated in `gap_register.md`.
- Internal paths and internal labels are absent from customer-facing attachments.

## J003 Gap Assessment

No new manual/source-backed coverage gap was discovered during J003. Existing gaps from
`GPTs/reports/gap_register.md` remain active and should be handled by their assigned
later jobs using the schemas in this report.
