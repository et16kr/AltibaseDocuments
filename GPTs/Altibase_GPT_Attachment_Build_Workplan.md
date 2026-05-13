# Altibase GPTs Attachment Build Workplan

## Purpose

This is the working standard for building the 20 Markdown files that will be uploaded
to GPTs. The final attachment set must let customers get version-aware answers for
SQL, DDL, configuration, operation, replication, and troubleshooting whether they use
Altibase 7.1, 7.3, or 8.1.

## Execution Management

Long work is split into jobs.

- Job list: `GPTs/Altibase_GPT_Attachment_Job_List.md`
- Runner script: `GPTs/scripts/attachment_jobs.sh`

Each job has one status: `ToDo`, `InProgress`, `Review`, `Done`, `Fail`, `Blocked`, or
`Skip`. Each step is designed so the runner can pass an independent job prompt to the
Codex CLI.

Commit and recovery rules:

- Each job should leave a Git commit at the start and at the finish.
- Start a job with `bash GPTs/scripts/attachment_jobs.sh start JOB-ID`. This changes
  the job status to `InProgress` and commits only changes under `GPTs/`.
- `run JOB-ID` automatically starts a `ToDo` job before running the Codex CLI.
- Finish a job with `bash GPTs/scripts/attachment_jobs.sh finish JOB-ID Done "summary"`,
  or use `Review`, `Fail`, `Blocked`, or `Skip` when appropriate. The finish command
  commits the status change and outputs together.
- For long jobs, use `bash GPTs/scripts/attachment_jobs.sh commit JOB-ID "intermediate summary"`
  when an intermediate save point is useful.
- If token exhaustion, session closure, or CLI failure interrupts a job, use
  `bash GPTs/scripts/attachment_jobs.sh history JOB-ID` to find job commits and resume.
- The runner commit scope is `GPTs/` by default. Source manuals and other directories
  are not included in job commits.
- Close failed jobs with `finish JOB-ID Fail "failure reason"` so the reason is captured
  in the commit message. Other ready jobs that do not depend on the failed job may continue.
- `start` and `run` check for uncommitted changes under `GPTs/` before starting, because
  those changes could otherwise mix with the next job commit.
- Use `ALLOW_DIRTY_COMMIT_SCOPE=1` only for manual recovery when a dirty `GPTs/` scope is
  intentional.
- `DRY_RUN=1` previews status changes, Codex execution, staging, and commits without
  making changes.

Automated execution:

- `bash GPTs/scripts/attachment_jobs.sh run-all` runs ready `ToDo` jobs whose dependencies
  are all `Done`.
- `bash GPTs/scripts/attachment_jobs.sh run-all "P3 SQL Core"` runs ready jobs only for
  that phase.
- `MAX_JOBS=3` limits a long run to three jobs.
- `STOP_ON_FAIL=1` stops the run immediately after a job fails. By default, failed jobs
  are marked `Fail` and unrelated ready jobs continue.
- `AUTO_ACCEPT_REVIEW=1` promotes jobs that finish as `Review` to `Done` during `run-all`.
- `ALLOW_FAILURES=1` allows `run-all` to exit successfully even when failures occurred.
- `ALLOW_INCOMPLETE=1` allows `run-all` to exit successfully when no more jobs are ready
  but blocked `ToDo` jobs remain.

Dependency rules:

- `next` and `run` only target jobs whose dependencies are all `Done`.
- If a job becomes `Fail` or `Blocked`, unrelated `ToDo` jobs may still continue.
- Document conversion jobs run only after the required source inventory, language policy,
  header conversion, and label cleanup jobs have succeeded.
- Mermaid conversion jobs run only after image inventory and related attachment conversion
  jobs have succeeded.
- QA jobs run only after the conversion jobs they check have succeeded.

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

## Review Checklist

- Confirm that `GPTs/attachments/*.md` contains exactly 20 files excluding
  `GPTs/attachments/README.md`.
- Confirm that attachment files are English canonical and ready for multilingual answers.
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
