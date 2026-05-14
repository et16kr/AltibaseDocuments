# Altibase GPTs Attachment Job List

## Purpose

This document tracks every job required to turn the current Altibase GPTs attachment skeletons into upload-ready, English canonical, multilingual-service-ready GPTs knowledge files.

The attachments must support customers using Altibase 7.1, 7.3, and 8.1. The internal 8.1 source may use the current verified source set, but customer-facing attachment files must not expose internal source labels.

## Status Values

| Status | Meaning |
| --- | --- |
| ToDo | Not started. |
| InProgress | A Codex CLI job is currently working on it. |
| Review | Work is done but requires human or second-pass review. |
| Done | Accepted and complete. |
| Fail | Attempted and failed. Add notes before retrying. |
| Blocked | Cannot proceed until another job or missing information is resolved. |
| Skip | Intentionally skipped. |

## How To Run Jobs

Use the runner script from the repository root.

```bash
bash GPTs/scripts/attachment_jobs.sh list
bash GPTs/scripts/attachment_jobs.sh ready
bash GPTs/scripts/attachment_jobs.sh blocked
bash GPTs/scripts/attachment_jobs.sh next
bash GPTs/scripts/attachment_jobs.sh deps JOB-030
bash GPTs/scripts/attachment_jobs.sh prompt JOB-030
bash GPTs/scripts/attachment_jobs.sh start JOB-030
bash GPTs/scripts/attachment_jobs.sh run JOB-030
bash GPTs/scripts/attachment_jobs.sh run-all
bash GPTs/scripts/attachment_jobs.sh run-all "P1 Inventory"
bash GPTs/scripts/attachment_jobs.sh finish JOB-030 Review "DDL guide expanded"
bash GPTs/scripts/attachment_jobs.sh finish JOB-030 Done "Reviewed and accepted"
bash GPTs/scripts/attachment_jobs.sh finish JOB-030 Fail "Source section missing"
bash GPTs/scripts/attachment_jobs.sh history JOB-030
bash GPTs/scripts/attachment_jobs.sh validate
```

By default, `run` calls `codex exec "<prompt>"`. Override if needed:

```bash
CODEX_BIN=codex CODEX_SUBCOMMAND=exec bash GPTs/scripts/attachment_jobs.sh run JOB-030
```

To run from the first available job through the remaining dependency graph:

```bash
bash GPTs/scripts/attachment_jobs.sh run-all
```

Useful controls:

```bash
MAX_JOBS=3 bash GPTs/scripts/attachment_jobs.sh run-all
STOP_ON_FAIL=1 bash GPTs/scripts/attachment_jobs.sh run-all
AUTO_ACCEPT_REVIEW=1 bash GPTs/scripts/attachment_jobs.sh run-all
DRY_RUN=1 bash GPTs/scripts/attachment_jobs.sh run-all
ALLOW_FAILURES=1 bash GPTs/scripts/attachment_jobs.sh run-all
ALLOW_INCOMPLETE=1 bash GPTs/scripts/attachment_jobs.sh run-all
bash GPTs/scripts/attachment_jobs.sh run-all "P3 SQL Core"
```

Commit behavior:

- `start JOB-ID` changes the job to `InProgress` and immediately commits the status change.
- `run JOB-ID` automatically performs `start JOB-ID` first when the job is still `ToDo`.
- `run-all [PHASE]` repeatedly runs ready `ToDo` jobs whose dependencies are `Done`. If a job fails, it is closed as `Fail` when possible, and unrelated ready jobs continue unless `STOP_ON_FAIL=1` is set.
- `AUTO_ACCEPT_REVIEW=1 run-all` promotes a successful `Review` job to `Done` so dependent jobs can continue without a manual review gate.
- `DRY_RUN=1` previews job actions without changing statuses, running Codex, staging, or committing.
- `run-all` returns nonzero when any job fails unless `ALLOW_FAILURES=1` is set.
- `finish JOB-ID Review|Done|Fail|Blocked|Skip "message"` changes the final status and immediately commits all changes under `GPTs/`.
- `commit JOB-ID "message"` can be used for an extra checkpoint during a long job.
- `history JOB-ID` shows the Git commits for that specific job.
- Commits are intentionally scoped to `GPTs/` so unrelated source manual edits are not included.
- `start` and `run` refuse to begin when `GPTs/` already has uncommitted changes, because those changes would be swept into the next job commit. Use `ALLOW_DIRTY_COMMIT_SCOPE=1` only for manual recovery.
- Use `mark` only for manual recovery when a commit is not desired; normal work should use `start` and `finish`.

Dependency behavior:

- `next` returns the first `ToDo` job whose dependencies are all `Done`.
- `ready` lists all runnable `ToDo` jobs.
- `blocked` lists `ToDo` jobs waiting on unfinished, failed, blocked, or missing dependencies.
- `run JOB-ID` refuses to run when dependencies are not `Done`.
- If a job fails, unrelated ready jobs can continue. Dependent jobs stay blocked until the failed dependency is retried and marked `Done`, or the dependency graph is intentionally revised.
- Use `FORCE=1 ... run JOB-ID` only for manual recovery.

## Global Rules For Every Job

- Do not modify original source manuals unless a job explicitly says so.
- Prefer editing files under `GPTs/`.
- Final attachment files under `GPTs/attachments/` are English canonical documents.
- Final attachment files must support answers in the user's language.
- SQL object names, function names, error codes, property names, and commands must not be translated.
- Attachment files must not contain internal source labels such as `trunk`.
- Graph, flow, state, architecture, and sequence images should become Mermaid where useful.
- SQL syntax diagrams should become compact BNF-like text or simple Mermaid.
- UI screenshots should become procedural text, not Mermaid.
- Large tables should be decomposed into searchable item blocks.
- Each attachment must keep sections for applicable versions, source documents, answerable questions, core guidance, version differences, and remaining TODOs until final cleanup.
- Do not run conversion jobs for documents whose required source inventory or prerequisite document jobs failed.
- Mermaid conversion jobs must only run after image inventory and the relevant attachment conversion jobs are `Done`.
- QA jobs must only run after the content jobs they validate are `Done`.
- Every executable job should have at least a start commit and a finish commit.
- If a job fails, finish it with `Fail` and include the reason in the commit message. Dependent jobs remain blocked, while unrelated ready jobs may continue.

## Job Table

| Job ID | Phase | Status | Depends On | Target | Objective | Inputs | Outputs | Acceptance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| JOB-001 | P0 Governance | Done | - | Selection | Establish 7.1, 7.3, 8.1 version policy | Existing selection notes | `GPTs/Altibase_GPT_Document_Selection.md` | Version policy exists |
| JOB-002 | P0 Governance | Done | JOB-001 | Workplan | Create build workplan | User plan | `GPTs/Altibase_GPT_Attachment_Build_Workplan.md` | Workplan exists |
| JOB-003 | P0 Governance | Done | JOB-001, JOB-002 | Attachment skeletons | Create 20 attachment skeletons | Planned attachment list | `GPTs/attachments/*.md` | 20 files excluding README |
| JOB-004 | P0 Governance | Done | JOB-003 | README | Convert attachment README to English canonical instructions | `GPTs/attachments/README.md` | Updated README | Multilingual answer policy included |
| JOB-005 | P0 Governance | Done | - | Job operations | Keep this job list current and mark completed setup jobs | This file | Updated statuses | Statuses reflect actual state |
| JOB-006 | P0 Governance | Done | JOB-004 | Upload policy | Add GPT Instructions draft for user-language answers | Workplan, README | `GPTs/GPT_Instructions_Draft.md` | Includes answer-language and SQL naming policy |
| JOB-010 | P1 Inventory | Done | JOB-003 | Source inventory | Inventory 7.1, 7.3, 8.1 source availability for all 20 attachments | Manuals, ReleaseNotes, Technical Documents | `GPTs/reports/source_inventory.md` | Every attachment has source paths |
| JOB-011 | P1 Inventory | Done | JOB-010 | 8.1 verification | Verify 8.1 source content against 8.1 release notes | 8.1 release notes, 8.1 source set | `GPTs/reports/8_1_verification.md` | JSON, Temporary LOB, replication SSL, JSON plan checked |
| JOB-012 | P1 Inventory | Done | JOB-010 | English/Korean parity | Compare English and Korean source quality for core docs | `Manuals/*/eng`, `Manuals/*/kor` | `GPTs/reports/eng_kor_parity.md` | English canonical source choice documented |
| JOB-013 | P1 Inventory | Done | JOB-010 | Image inventory | List candidate images for Mermaid or text conversion | Selected source docs | `GPTs/reports/image_inventory.md` | Each image classified |
| JOB-014 | P1 Inventory | Done | JOB-010 | Table inventory | List large tables that require decomposition | Selected source docs | `GPTs/reports/table_inventory.md` | Top priority tables identified |
| JOB-015 | P1 Inventory | Done | JOB-010 | Bad links | Detect Windows absolute paths and broken image links in selected sources | Selected source docs | `GPTs/reports/link_inventory.md` | Cleanup targets listed |
| JOB-020 | P2 Language | Done | JOB-004, JOB-006 | Canonical language | Convert attachment writing policy to English canonical | Workplan, attachments README | Selection, README, Workplan | English canonical policy clear |
| JOB-021 | P2 Language | Done | JOB-010, JOB-012 | Terminology glossary | Build Altibase terminology glossary for multilingual answers | Source manuals | `GPTs/internal/terminology_glossary.md` | Terms not to translate listed |
| JOB-022 | P2 Language | Done | JOB-020, JOB-021 | Header conversion | Convert all attachment headers and common sections to English | 20 attachments | 20 updated attachments | Common structure is English |
| JOB-023 | P2 Language | Done | JOB-022 | Source label cleanup | Replace customer-facing internal labels in attachments | 20 attachments | 20 updated attachments | No internal source labels in attachments |
| JOB-024 | P2 Language | Done | JOB-006, JOB-021 | Multilingual policy tests | Draft sample prompts in Vietnamese, Turkish, Persian, Hindi, Chinese, Japanese, English, German, French | README, instructions draft | `GPTs/reports/multilingual_prompt_set.md` | At least 10 language prompts |
| JOB-030 | P3 SQL Core | Done | JOB-010, JOB-011, JOB-012, JOB-022, JOB-023 | `03_sql_ddl_generation.md` | Expand DDL generation guide from source manuals | SQL Reference, General Reference | Updated attachment 03 | DDL examples cover tablespace, table, index, user, sequence, replication |
| JOB-031 | P3 SQL Core | Done | JOB-030, JOB-041 | Tablespace DDL | Deepen memory, disk, volatile, temporary tablespace DDL | SQL Reference, Admin | Attachment 03 and 02 | Version-aware DDL and check SQL |
| JOB-032 | P3 SQL Core | Done | JOB-030, JOB-038 | Table DDL | Deepen table DDL for memory, disk, LOB, JSON, partition, queue | SQL Reference | Attachment 03 | Oracle differences stated |
| JOB-033 | P3 SQL Core | Done | JOB-030, JOB-043 | Index and constraints | Deepen indexes, constraints, PK, FK, unique, partitioned indexes | SQL Reference, Tuning | Attachment 03 and 08 | Examples plus verification SQL |
| JOB-034 | P3 SQL Core | Done | JOB-030, JOB-041 | Users and privileges | Deepen CREATE USER, ALTER USER, GRANT, REVOKE, roles | SQL Reference, Admin | Attachment 03 and 02 | Least-privilege notes included |
| JOB-035 | P3 SQL Core | Done | JOB-030, JOB-044 | Replication SQL | Deepen CREATE/ALTER REPLICATION and 8.1 SSL examples | SQL Reference, Replication | Attachment 03 and 09 | Non-SSL and SSL cases separated |
| JOB-036 | P3 SQL Core | Done | JOB-030, JOB-038, JOB-039 | Property SQL | Deepen property query/change guidance and system views | General Reference | Attachment 03, 05, 06 | Query examples verified |
| JOB-037 | P3 SQL Core | Done | JOB-010, JOB-012, JOB-022, JOB-023 | `04_sql_dml_oracle_compatibility.md` | Build Oracle-compatible DML summary and Altibase differences | SQL Reference | Updated attachment 04 | Generic Oracle SQL compressed |
| JOB-038 | P3 SQL Core | Done | JOB-010, JOB-011, JOB-012, JOB-022, JOB-023 | `05_data_types_properties.md` | Build data type and property guide including 8.1 JSON and Temporary LOB | General Reference, Release Notes | Updated attachment 05 | Properties decomposed |
| JOB-039 | P3 SQL Core | Done | JOB-010, JOB-011, JOB-012, JOB-022, JOB-023 | `06_data_dictionary_performance_views.md` | Build dictionary and performance view query cookbook | General Reference 2 | Updated attachment 06 | Common checks grouped by task |
| JOB-040 | P4 Operations | Done | JOB-010, JOB-012, JOB-022, JOB-023 | `01_getting_started_installation.md` | Build installation and first-run guide | Getting Started, Installation | Updated attachment 01 | Flowchart Mermaid included |
| JOB-041 | P4 Operations | Done | JOB-010, JOB-012, JOB-022, JOB-023 | `02_administration_operations.md` | Build admin operations guide | Administrator | Updated attachment 02 | Backup, recovery, tablespace operations covered |
| JOB-042 | P4 Operations | Done | JOB-010, JOB-012, JOB-022, JOB-023 | `07_error_messages_troubleshooting.md` | Build troubleshooting and error response guide | Error Message Reference | Updated attachment 07 | Error format standardized |
| JOB-043 | P4 Operations | Done | JOB-010, JOB-012, JOB-022, JOB-023 | `08_performance_tuning_monitoring.md` | Build performance tuning and monitoring guide | Performance Tuning, Monitoring API, SNMP | Updated attachment 08 | Plan trees transformed |
| JOB-044 | P4 Operations | Done | JOB-010, JOB-011, JOB-012, JOB-022, JOB-023 | `09_replication_ha_cdc.md` | Build replication, HA, CDC guide | Replication, Log Analyzer, Compatibility docs | Updated attachment 09 | State diagram Mermaid included |
| JOB-045 | P4 Operations | Done | JOB-010, JOB-011, JOB-012, JOB-022, JOB-023 | `18_security_ssl_tls.md` | Build SSL/TLS guide including replication SSL | SSL/TLS Guide, Release Notes | Updated attachment 18 | Server, client, replication cases separated |
| JOB-050 | P5 Development | Done | JOB-010, JOB-012, JOB-022, JOB-023 | `10_psm_stored_external_procedures.md` | Build PSM and external procedure guide | Stored Procedures, External Procedures | Updated attachment 10 | Oracle PL/SQL compatibility notes |
| JOB-051 | P5 Development | Done | JOB-010, JOB-012, JOB-021, JOB-022, JOB-023 | `11_java_jdbc_spring.md` | Build Java, JDBC, Spring, Hibernate guide | JDBC, Adapter, JavaCompatibility, Spring guides | Updated attachment 11 | URL and config cookbook |
| JOB-052 | P5 Development | Done | JOB-010, JOB-012, JOB-022, JOB-023 | `12_c_cli_odbc_precompiler.md` | Build C, CLI, ODBC, Precompiler guide | CLI, ODBC, C Interface, Precompiler | Updated attachment 12 | API flow and LOB guidance |
| JOB-053 | P5 Development | Done | JOB-010, JOB-012, JOB-022, JOB-023 | `13_isql_iloader_basic_tools.md` | Build iSQL and iLoader guide | iSQL, iLoader | Updated attachment 13 | Export/import cookbook |
| JOB-060 | P6 Tools | Done | JOB-010, JOB-011, JOB-012, JOB-022, JOB-023 | `00_version_release_platform.md` | Build version, release, platform guide | Release Notes, Supported Platforms | Updated attachment 00 | 7.1/7.3/8.1 differences clear |
| JOB-061 | P6 Tools | Done | JOB-010, JOB-012, JOB-022, JOB-023 | `14_utilities_operation_tools.md` | Build utilities guide | Utilities, dataCompJ | Updated attachment 14 | Tool blocks standardized |
| JOB-062 | P6 Tools | Done | JOB-010, JOB-012, JOB-022, JOB-023 | `15_migration_oracle_compatibility.md` | Build migration and Oracle compatibility guide | Migration Center, Adapter for Oracle | Updated attachment 15 | Migration steps and DDL differences |
| JOB-063 | P6 Tools | Done | JOB-010, JOB-012, JOB-022, JOB-023 | `16_dblink_external_connectors.md` | Build DB Link and external connector guide | DB Link, Hadoop, 3rd Party Connector | Updated attachment 16 | Connector-by-connector guidance |
| JOB-064 | P6 Tools | Done | JOB-010, JOB-012, JOB-022, JOB-023 | `17_kubernetes_aku_cloud.md` | Build Kubernetes and AKU guide | Kubernetes guide, AKU guide, release notes | Updated attachment 17 | Pod lifecycle flow included |
| JOB-065 | P6 Tools | Done | JOB-010, JOB-012, JOB-022, JOB-023 | `19_spatial_nifi_tableau_misc.md` | Build Spatial, altiShapeLoader, NiFi, Tableau guide | Spatial, altiShapeLoader, NiFi, Tableau | Updated attachment 19 | UI screenshots converted to procedure text |
| JOB-070 | P7 Mermaid | Done | JOB-013, JOB-020 | Mermaid policy | Add detailed Mermaid conversion policy to workplan and README | Workplan, README | Updated docs | Diagram type rules included |
| JOB-071 | P7 Mermaid | Done | JOB-013, JOB-040, JOB-041, JOB-070 | Admin diagrams | Convert admin and installation flow images to Mermaid | Image inventory, Admin, Installation | Attachments 01, 02 | No image-only flow remains |
| JOB-072 | P7 Mermaid | Done | JOB-013, JOB-030, JOB-037, JOB-070 | SQL syntax diagrams | Convert SQL syntax diagrams to BNF or Mermaid | SQL Reference | Attachments 03, 04 | Syntax readable without images |
| JOB-073 | P7 Mermaid | Done | JOB-013, JOB-043, JOB-070 | Performance diagrams | Convert plan tree and tuning images | Performance Tuning | Attachment 08 | Plan structures searchable |
| JOB-074 | P7 Mermaid | InProgress | JOB-013, JOB-044, JOB-070 | Replication diagrams | Convert replication topology and state diagrams | Replication | Attachment 09 | Mermaid topology/state diagrams |
| JOB-075 | P7 Mermaid | ToDo | JOB-013, JOB-063, JOB-064, JOB-065, JOB-070 | UI screenshots | Replace UI screenshots with procedural text | 3rd party guides | Attachments 16, 17, 19 | No screenshot dependency |
| JOB-080 | P8 QA | Done | JOB-003 | Count validation | Validate exactly 20 upload attachments excluding README | Attachments | QA report | Count equals 20 |
| JOB-081 | P8 QA | Done | JOB-023 | Forbidden strings | Validate no internal source labels, Windows paths, file URLs in attachments | Attachments | QA report | No matches |
| JOB-082 | P8 QA | ToDo | JOB-030, JOB-037, JOB-038, JOB-039, JOB-040, JOB-041, JOB-042, JOB-043, JOB-044, JOB-045, JOB-050, JOB-051, JOB-052, JOB-053, JOB-060, JOB-061, JOB-062, JOB-063, JOB-064, JOB-065 | Version coverage | Validate each attachment has 7.1, 7.3, 8.1 guidance | Attachments | QA report | Coverage complete or exception documented |
| JOB-083 | P8 QA | ToDo | JOB-022, JOB-023, JOB-030, JOB-037, JOB-038, JOB-039, JOB-040, JOB-041, JOB-042, JOB-043, JOB-044, JOB-045, JOB-050, JOB-051, JOB-052, JOB-053, JOB-060, JOB-061, JOB-062, JOB-063, JOB-064, JOB-065 | English consistency | Validate attachment files are English canonical | Attachments | QA report | Korean only appears in examples or source names if needed |
| JOB-084 | P8 QA | ToDo | JOB-030, JOB-031, JOB-032, JOB-033, JOB-034, JOB-035, JOB-036, JOB-037, JOB-038, JOB-039 | SQL generation tests | Run 20 representative SQL generation prompt checks manually or with Codex | Attachment 03 plus related docs | `GPTs/reports/sql_generation_test_results.md` | Each prompt has acceptable answer |
| JOB-085 | P8 QA | ToDo | JOB-006, JOB-024, JOB-083 | Multilingual smoke tests | Test answers in major customer languages | Prompt set, attachments | `GPTs/reports/multilingual_smoke_results.md` | User language response works |
| JOB-086 | P8 QA | ToDo | JOB-010, JOB-011, JOB-012, JOB-082, JOB-083 | Source audit | Verify major claims trace to source manuals or release notes | Attachments, source reports | `GPTs/reports/source_audit.md` | High-risk claims sourced |
| JOB-087 | P8 QA | ToDo | JOB-080, JOB-081, JOB-082, JOB-083, JOB-084, JOB-085, JOB-086 | Packaging | Prepare final upload package checklist | Attachments | `GPTs/reports/upload_checklist.md` | Upload-ready list produced |
| JOB-088 | P8 QA | ToDo | JOB-087 | Final review | Final human review pass and status closure | All GPTs files | Updated job list | All required jobs Done or documented |
