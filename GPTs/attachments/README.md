# Altibase GPTs Attachments

This directory contains customer-facing Markdown knowledge files for Altibase GPTs.
The files consolidate the selected Altibase manuals, release notes, technical documents,
tool manuals, third-party guides, and approved supporting sources into the canonical
English source used by the GPT to answer customer questions about Altibase 7.1, 7.3,
and 8.1.

The target GPT is an encyclopedia-grade Altibase assistant for overseas customers who
may have no prior Altibase knowledge. The 20 files are upload packaging units, not a
high-frequency FAQ subset.

## Core Rules

- Keep exactly 20 attachment Markdown files, excluding this `README.md`.
- Write every attachment in canonical English.
- Treat canonical English as the source language for the knowledge files. The GPT may
  translate explanations at answer time, but the attachment text itself should stay English.
- Support Altibase 7.1, 7.3, and 8.1 answers.
- Treat the 20 attachment files as the consolidated answer source for the selected
  source documents. Do not answer only that a product/manual detail is absent from the
  attachments when the question is within the selected source-backed Altibase corpus;
  answer from the closest relevant consolidated source blocks and ask only for missing
  version, environment, log, or object details needed for a safe answer.
- Preserve source-backed answerability for manual-style questions about properties,
  SQL syntax, data types, dictionary/performance views, error codes, utilities, tools,
  drivers, connectors, backup/recovery, replication, security, migration, and operations.
- Label Altibase 8.1 material as based on the `Altibase 8.1 verified source`.
- Prioritize Altibase-specific DDL, configuration, operation, compatibility, and troubleshooting behavior.
- Keep common SQL behavior that overlaps with Oracle brief unless Altibase differs.
- Convert tables and images into searchable Markdown text whenever possible.
- Keep customer-facing source references concise and safe: use product, manual, version, and topic names only.
- Do not expose internal repository names, branch names, workstation paths, or local build labels.

## Multilingual Answer Policy

The GPT should answer in the user's language whenever possible. Keep the following items
literal and untranslated in every language:

- SQL object names
- SQL keywords when used as syntax
- Function names
- Error codes
- Property names
- Commands and command options
- File and directory paths
- Package, class, method, API, and connector names
- Altibase version numbers and edition names

When translating explanatory text, preserve the exact spelling and casing of literal
technical tokens. If a translated sentence would make a command, property, or SQL
syntax ambiguous, keep that portion in English and explain it in the user's language.

## File List

1. `00_version_release_platform.md`
2. `01_getting_started_installation.md`
3. `02_administration_operations.md`
4. `03_sql_ddl_generation.md`
5. `04_sql_dml_oracle_compatibility.md`
6. `05_data_types_properties.md`
7. `06_data_dictionary_performance_views.md`
8. `07_error_messages_troubleshooting.md`
9. `08_performance_tuning_monitoring.md`
10. `09_replication_ha_cdc.md`
11. `10_psm_stored_external_procedures.md`
12. `11_java_jdbc_spring.md`
13. `12_c_cli_odbc_precompiler.md`
14. `13_isql_iloader_basic_tools.md`
15. `14_utilities_operation_tools.md`
16. `15_migration_oracle_compatibility.md`
17. `16_dblink_external_connectors.md`
18. `17_kubernetes_aku_cloud.md`
19. `18_security_ssl_tls.md`
20. `19_spatial_nifi_tableau_misc.md`

## Attachment Structure

Each upload attachment should keep these customer-answer sections:

- `Applicable Versions`
- `Questions This File Can Answer`
- `Retrieval Alias Index`
- `Source Documents`
- `Response Rules`
- `Attachment Cross-References`
- `Residual Scope`

Use `Version Differences` when the attachment has version-specific behavior to
summarize. Keep file-specific answer blocks, runbooks, syntax patterns, inventories,
or tool blocks under descriptive headings after `Response Rules`.

Use compact, searchable item blocks for large reference tables. Use BNF-like text for
SQL syntax diagrams. Use Mermaid only when it helps explain graphs, flows, states,
architecture, topology, or sequences. Replace UI screenshots with procedural text and
clear input or value descriptions.

`Retrieval Alias Index` is a compact lexical-routing block near the top of each upload
attachment. It should repeat customer wording, exact literal tokens, owning answer
routes, cross-file routes, and missing-input triggers without adding new product
behavior. Keep these blocks short; the goal is to point retrieval to the precise
answer section, not to duplicate the full reference content.

## Customer LLM Editorial QA Checklist

- A first-time user should be able to find the task purpose, prerequisites, safe
  defaults, and first checks before any risky command or SQL.
- A veteran user should be able to extract exact property names, SQL syntax, view and
  column names, error codes, command options, defaults, ranges, units, version labels,
  and operational caveats without relying on generic database assumptions.
- Protected topics such as backup/recovery, destructive SQL, replication state changes,
  TLS/security changes, and version-sensitive property changes should ask for missing
  patch, environment, topology, log, object-definition, or current-state inputs before
  giving state-changing guidance.
- If a source-backed answer path exists in the attachment set, the answer should use
  the closest consolidated block instead of saying only that the detail is absent.
- If selected sources do not establish the claim, the answer should say what input or
  installed evidence is missing and give the safest source-backed next check.

## Mermaid And Visual Conversion Policy

Use Mermaid when a diagram's relationships are important for answering customer questions.
Use searchable text when the image is mainly syntax, UI detail, table data, or decoration.

General rules:

- Use a fenced `mermaid` code block with one diagram per block.
- Add a short lead-in sentence explaining what the diagram represents.
- Keep labels concise and English, while preserving literal technical tokens such as
  SQL keywords, object names, error codes, property names, commands, paths, and API names.
- Keep version scope explicit when the diagram differs across Altibase 7.1, 7.3, and 8.1.
- Use customer-safe source labels, including `Altibase 8.1 verified source` for 8.1
  material.
- Do not reproduce decorative styling, icons, logos, colors, or screenshots.
- Split large visuals into smaller diagrams or searchable item blocks.

Diagram type rules:

| Source image type | Preferred conversion |
| --- | --- |
| Architecture, component, storage, network, cluster, or topology diagram | Mermaid `flowchart LR` or `flowchart TB` with labeled edges and `subgraph` groups only when useful |
| Operational workflow, installation flow, backup/recovery flow, startup/shutdown flow, failover flow, or decision tree | Mermaid `flowchart TD` with actions, decisions, and outcomes |
| Lifecycle, replication state, server state, checkpoint state, failure state, or mode transition | Mermaid `stateDiagram-v2` with meaningful transition labels |
| Client/server exchange, handshake, replication sender/receiver exchange, JDBC or CLI call order, or ordered protocol interaction | Mermaid `sequenceDiagram` when message ordering matters |
| Query execution plan tree or optimizer example | Indented text by default; Mermaid `flowchart TD` only for small parent-child examples |
| SQL, PSM, command, data type, or utility syntax railroad diagram | Compact BNF-like text by default; simple Mermaid only for short branching syntax |
| UI screenshot, wizard, dialog, console screenshot, or web form | Procedural text with menu path, field names, input values, selected options, and expected result |
| Visual table, compatibility matrix, mapping chart, option list, or screen-captured result table | Markdown table or searchable item blocks |
| Conceptual reference figure | Short source-backed text summary, or Mermaid only if relationships matter |
| Syntax legend icon, boilerplate, logo, cover image, or decorative figure | Omit, or document once as shared notation |

Keep Mermaid diagrams compact. Split or replace a diagram with text when it grows beyond
roughly 12 nodes, 16 edges, or four decision branches. Put long commands, SQL examples,
and cautions outside the diagram in code blocks or item blocks.

## Source Traceability Policy

Customer-facing attachments may cite source material only with safe labels such as
Altibase version, manual family, release note, or topic. Keep internal paths and branch
names in work documents only. For Altibase 8.1, use `Altibase 8.1 verified source` or
equivalent wording instead of any internal source-set name.

## Pre-Upload Checks

- Confirm that exactly 20 Markdown attachment files exist, excluding `README.md`.
- Confirm that each attachment is English canonical and ready for multilingual answers.
- Confirm that version coverage and version differences are explicit.
- Confirm that customer-facing source references are safe and concise.
- Confirm that no internal repository labels, local paths, or non-customer source names remain.
