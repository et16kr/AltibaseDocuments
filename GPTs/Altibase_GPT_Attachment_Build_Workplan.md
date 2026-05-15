# Altibase GPTs Attachment Build Workplan

## Purpose

This is the working standard for building the 20 Markdown files that will be uploaded
to GPTs. The final attachment set must let customers get version-aware answers for
SQL, DDL, configuration, operation, replication, and troubleshooting whether they use
Altibase 7.1, 7.3, or 8.1.

## Execution Management

The initial attachment build jobs are complete. Current pre-upload verification is
managed by the staged review/remediation cycle.

Current review-cycle files:

- Stage definitions: `review/review_stages.tsv`
- Cycle runner: `review/scripts/run_review_remediation_cycle.sh`
- Review stage runner: `review/scripts/run_review_stage.sh`
- Cycle status: `review/review_remediation_cycle_status.tsv`
- Review status: `review/review_stage_status.tsv`
- Stage reports: `review/reports/R*.md`

Automated execution:

- `bash review/scripts/run_review_remediation_cycle.sh run-all` runs remaining review
  stages in stage order.
- Each stage follows: review, remediate if needed, validate, re-review, commit, then
  move to the next stage.
- `DRY_RUN=1 bash review/scripts/run_review_remediation_cycle.sh run-all` previews the
  planned stage sequence without changing status or running Codex.
- Optional group execution uses `bash review/scripts/run_review_remediation_cycle.sh run-all GROUP`.

Review-cycle source reports under `GPTs/reports/` are retained only where they are
referenced by `review/review_stages.tsv` or the detailed review design.

## Source Version Mapping

| Answer baseline version | Internal source path | Customer-facing label |
| --- | --- | --- |
| 7.1 | `Manuals/Altibase_7.1` | Altibase 7.1 |
| 7.3 | `Manuals/Altibase_7.3` | Altibase 7.3 |
| 8.1 | `Manuals/Altibase_trunk` + `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md` | Altibase 8.1 verified source |

Review rules:

- Do not use internal source labels such as `trunk` in customer-facing attachment files.
- Work documents and the selection document may keep internal source paths for concise
  traceability.
- Check the 8.1 source against the 8.1 release notes for new feature coverage before using
  it as the 8.1 baseline.

## Outputs

- `GPTs/Altibase_GPT_Document_Selection.md`
- `GPTs/Altibase_GPT_Attachment_Build_Workplan.md`
- `GPTs/attachments/README.md`
- `GPTs/attachments/00_version_release_platform.md`
- `GPTs/attachments/01_getting_started_installation.md`
- `GPTs/attachments/02_administration_operations.md`
- `GPTs/attachments/03_sql_ddl_generation.md`
- `GPTs/attachments/04_sql_dml_oracle_compatibility.md`
- `GPTs/attachments/05_data_types_properties.md`
- `GPTs/attachments/06_data_dictionary_performance_views.md`
- `GPTs/attachments/07_error_messages_troubleshooting.md`
- `GPTs/attachments/08_performance_tuning_monitoring.md`
- `GPTs/attachments/09_replication_ha_cdc.md`
- `GPTs/attachments/10_psm_stored_external_procedures.md`
- `GPTs/attachments/11_java_jdbc_spring.md`
- `GPTs/attachments/12_c_cli_odbc_precompiler.md`
- `GPTs/attachments/13_isql_iloader_basic_tools.md`
- `GPTs/attachments/14_utilities_operation_tools.md`
- `GPTs/attachments/15_migration_oracle_compatibility.md`
- `GPTs/attachments/16_dblink_external_connectors.md`
- `GPTs/attachments/17_kubernetes_aku_cloud.md`
- `GPTs/attachments/18_security_ssl_tls.md`
- `GPTs/attachments/19_spatial_nifi_tableau_misc.md`

## Work Stages

### Stage 1: SQL/DDL Generation Core

Targets:

- `03_sql_ddl_generation.md`
- `04_sql_dml_oracle_compatibility.md`
- `05_data_types_properties.md`
- `06_data_dictionary_performance_views.md`

Work:

- Compress general SQL that overlaps with Oracle.
- Organize Altibase DDL, tablespaces, memory/disk tables, indexes, sequences, users and
  privileges, replication SQL, and property check SQL around executable examples.
- State 7.1/7.3/8.1 differences when they exist.

### Stage 2: Operations, Performance, and Replication

Targets:

- `01_getting_started_installation.md`
- `02_administration_operations.md`
- `07_error_messages_troubleshooting.md`
- `08_performance_tuning_monitoring.md`
- `09_replication_ha_cdc.md`
- `18_security_ssl_tls.md`

Work:

- Convert operational procedures into checklists.
- Decompose tables into item-level explanations.
- Convert flow images to Mermaid or procedural text.

### Stage 3: Development Interfaces

Targets:

- `10_psm_stored_external_procedures.md`
- `11_java_jdbc_spring.md`
- `12_c_cli_odbc_precompiler.md`
- `13_isql_iloader_basic_tools.md`

Work:

- Convert connection strings, drivers, API order of use, LOB handling, and error handling
  into FAQ-style guidance.
- Decompose API tables by function into role, arguments, return value, and cautions.

### Stage 4: Tools, Migration, and External Integration

Targets:

- `00_version_release_platform.md`
- `14_utilities_operation_tools.md`
- `15_migration_oracle_compatibility.md`
- `16_dblink_external_connectors.md`
- `17_kubernetes_aku_cloud.md`
- `19_spatial_nifi_tableau_misc.md`

Work:

- Reorganize release notes around version differences and upgrade cautions.
- Replace screenshot-heavy material with meaningful procedure text.
- Separate tool-specific restrictions from troubleshooting items.

## Common Attachment Template

Each attachment should follow this structure until final cleanup.

```markdown
# Document Title

## Applicable Versions

- 7.1:
- 7.3:
- 8.1:

## Questions This File Can Answer

- ...

## Source Documents

- 7.1:
- 7.3:
- 8.1 verified source:

## Core Guidance

## Version Differences

## Conversion TODO
```

## Attachment Writing Policy

- Write final attachment files in canonical English.
- Use Korean manuals as the source of truth for technical behavior when paired Korean
  and English manuals differ; keep final attachment language English.
- The GPT should answer in the user's language whenever possible, but literal technical
  tokens must stay unchanged in every answer language.
- Keep SQL object names, function names, error codes, property names, commands, file paths,
  package names, class names, method names, API names, connector names, and version numbers
  literal.
- Keep customer-facing source references concise and safe: use only product, manual,
  version, and topic names.
- Do not expose internal repository names, branch names, local filesystem paths, or local
  build labels in customer-facing attachment files.
- Label 8.1 customer-facing material as `Altibase 8.1 verified source` or equivalent
  customer-safe wording.
- Use compact, searchable item blocks for large reference tables.
- Use compact BNF-like text for SQL syntax diagrams. Use Mermaid only when it makes SQL
  syntax clearer than text.
- Use Mermaid for graph, flow, state, architecture, topology, and sequence diagrams when
  the diagram improves retrieval or explanation.
- Replace UI screenshots with procedural text and clear input/value descriptions.

## Mermaid And Visual Conversion Policy

Use Mermaid only when the visual relationship carries information that searchable prose
would otherwise lose. Each converted diagram must help a GPT answer user questions without
seeing the original image.

General conversion rules:

- Keep every diagram in a fenced `mermaid` code block with exactly one diagram per block.
- Put a short lead-in sentence before the diagram that states its purpose.
- Use concise English node labels, but keep SQL object names, SQL keywords, commands,
  property names, error codes, file paths, product names, and API names literal.
- Prefer stable, searchable labels over decorative labels. Do not reproduce colors,
  icons, shadows, screenshots, logos, or visual styling that does not change the meaning.
- Preserve version scope near the diagram when behavior differs for Altibase 7.1, 7.3,
  or 8.1.
- Do not copy internal source labels into customer-facing attachments. Use
  `Altibase 8.1 verified source` or another customer-safe label for 8.1 source material.
- If an image contains too much detail for one readable diagram, split it into smaller
  diagrams or replace nonessential parts with item blocks.
- If the original figure is ambiguous, write the source-backed facts in text and leave a
  conversion TODO instead of inventing relationships.

Diagram type rules:

| Source image type | Preferred conversion | Rule |
| --- | --- | --- |
| Architecture, component, storage, network, cluster, or topology diagram | `flowchart LR` or `flowchart TB` | Use nodes for hosts, processes, databases, files, listeners, clients, and services. Use labeled edges for data flow, control flow, replication, or dependency direction. Use `subgraph` only when grouping makes ownership or deployment boundaries clearer. |
| Operational workflow, backup/recovery flow, startup/shutdown flow, installation flow, failover procedure, or decision tree | `flowchart TD` | Represent actions as steps, decisions as branch nodes, and outcomes as terminal nodes. Keep procedure details in surrounding text when a node would become too long. |
| Lifecycle, replication state, server state, checkpoint state, failure state, or mode transition | `stateDiagram-v2` | Use state names from the manual when available. Show only meaningful transitions and label transition triggers, commands, or conditions. |
| Client/server exchange, handshake, replication sender/receiver exchange, JDBC or CLI call order, and ordered protocol interaction | `sequenceDiagram` | Use participants for roles or processes and messages for calls, responses, acknowledgements, and errors. Use it only when ordering matters more than topology. |
| Query execution plan tree or optimizer example | Indented text by default; small `flowchart TD` only when parent-child relationships are the point | Keep operator names, access methods, and object names literal. Avoid large Mermaid plan trees that are harder to search than text. |
| SQL, PSM, command, data type, or utility syntax railroad diagram | Compact BNF-like text by default; simple `flowchart LR` only for short branching syntax | Preserve literal keywords and placeholders. Use Mermaid only when alternatives or optional branches are clearer visually than a one-screen grammar block. |
| UI screenshot, wizard screen, dialog, console screenshot, or web form | Procedural text, field/value list, or expected-output block | Do not convert UI screenshots to Mermaid. Record menu paths, buttons, input fields, selected values, and resulting state. |
| Visual table, compatibility matrix, mapping chart, option list, or screen-captured result table | Searchable item blocks or Markdown table | Decompose large tables into per-item blocks with name, scope, value, default, version, caution, or example fields as applicable. |
| Conceptual reference figure | Short text summary, or Mermaid only if relationships matter | Summarize the point of the figure in one or two source-backed sentences when the layout itself is not needed. |
| Syntax legend icon, repeated boilerplate, logo, cover image, or decorative figure | Omit, or document once as shared notation | Do not repeat boilerplate image conversions in every attachment. |

Mermaid readability rules:

- Keep diagrams small enough to scan in a GPT attachment. As a rule of thumb, split a
  diagram when it exceeds about 12 nodes, 16 edges, or four decision branches.
- Use left-to-right layout for topology and architecture, top-down layout for procedures
  and cause/effect flow.
- Edge labels should explain the relationship, not restate adjacent node names.
- Prefer one noun phrase per node. Put commands, SQL examples, and long cautions outside
  the diagram in code blocks or item blocks.
- When a diagram depends on a preceding or following procedure, keep the procedure as the
  authoritative text and use Mermaid as a navigational aid.

## Review Checklist

- Confirm that `GPTs/attachments/*.md` contains exactly 20 files excluding
  `GPTs/attachments/README.md`.
- Confirm that attachment files are English canonical and ready for multilingual answers,
  while Korean manuals remain the default source authority for technical conflicts.
- Confirm that customer-facing attachment files do not contain `trunk`.
- Confirm that every attachment has applicable versions, source documents, answerable
  questions, and conversion TODOs until final cleanup removes those scaffolding sections.
- Confirm that no `C:/`, `file://`, broken image links, or screenshot-only references remain.
- Sample SQL generation documents with at least 20 representative questions.

## Representative SQL Generation Review Questions

1. Create a table DDL with a JSON column for Altibase 8.1.
2. Create a disk tablespace and a table on it for Altibase 7.3.
3. Create a memory tablespace and enable auto extension.
4. Add an index to a specific table and show how to verify it.
5. Create a user and set a default tablespace.
6. Grant and revoke privileges.
7. Create a sequence.
8. Move a table to another tablespace.
9. Create a table with a LOB column.
10. Create a partitioned table example.
11. Create a replication object.
12. Create an SSL replication example for Altibase 8.1.
13. Start and stop replication.
14. Check a property value.
15. Check session status from a performance view.
16. Explain how to check an execution plan.
17. Create an iLoader data-load command example.
18. Create a JDBC connection string.
19. Explain cautions when converting Oracle DDL to Altibase DDL.
20. Explain causes and actions for a specific error code.
