# Altibase GPT Customer LLM Remediation

- Kind: `docs`
- Status values: `ToDo`, `Progress`, `Done`, `Fail`
- User-run command: `./run-all.sh` from this directory
- Codex workdir: repository root by default, override with `CODEX_WORKDIR=/path`
- Default behavior: continue through all jobs until completion or failure
- Optional single-job mode: `RUN_ONE=1 ./run-all.sh`
- Handoff gate: uncommitted project files stop the workflow before the next job starts
- Commit gate: each successful job must pass review and create a focused commit

## Job Count Decision

The earlier root-cause analysis proposed 7 broad remediation work packages. That count
is useful for strategy but too small for execution. This workflow uses 22 jobs because
the desired output is a customer-usable LLM corpus for both first-time and veteran
Altibase users. The work must separate source-backed gap inventory, GPT answer
instructions, exact-token coverage, domain-specific attachment remediation, retrieval
structure, calibration, editorial QA, and final readiness.

The original 20-job draft under-partitioned properties. Properties had the largest
critical-fact miss count in the 2026-05-17 benchmark, so this workflow splits property
remediation into four bounded jobs: core/path/storage, capacity/log limits,
optimizer/session/locale, and security/replication/network. More jobs may be useful
later if one domain remains difficult, but 22 is the initial balance between coverage
and operational overhead.

## Workflow Requirements

`run-all.sh` prepends `requirements.md` to every job prompt at runtime. Treat that file
as the shared contract for source policy, customer LLM quality, beginner/veteran
usability, benchmark evidence, verification, and commit handoff.

## Partitioning Model

- J001-J003: evidence inventory, answer contract, and exact-token gap mapping before
  attachment edits.
- J004-J007: property remediation split by source-backed property families and
  benchmark failure density.
- J008-J009: SQL generation, DDL/DML, functions, data types, and Oracle-difference
  remediation.
- J010-J012: troubleshooting and high-risk operations, including protected backup,
  recovery, and destructive-operation guidance.
- J013-J014: replication, CDC, TLS, network, and replication-tool remediation.
- J015-J017: views, performance, monitoring, APIs, tools, connectors, migration, and
  integration remediation.
- J018-J020: retrieval structure, targeted benchmark calibration, and residual gap
  remediation.
- J021-J022: customer-facing editorial QA, final validation, readiness reporting, and
  rerun planning.

## Job Scope Matrix

| ID | Primary target areas | Expected durable output |
| --- | --- | --- |
| `J001` | `evals/altibase_answerability/reports/`, `GPTs/reports/` | A source-backed remediation inventory linking failed questions, tokens, source families, and attachment targets. |
| `J002` | `GPTs/GPT_Instructions_Draft.md`, `GPTs/reports/` | A customer answer contract that forces exact tokens, source boundaries, version handling, and beginner/veteran answer depth. |
| `J003` | `evals/altibase_answerability/questions/*.jsonl`, `GPTs/reports/` | A prioritized exact-token gap inventory separated into content, retrieval, synthesis, and judge-calibration candidates. |
| `J004` | `GPTs/attachments/05_data_types_properties.md`, related `00`, `01`, `02`, `06` references | Core identity, path, memory-directory, database-file, log-anchor, and storage property blocks. |
| `J005` | `GPTs/attachments/05_data_types_properties.md`, related `00`, `02`, `08` references | Memory, disk, volatile, log-size, plan-cache, result-cache, and capacity-limit property blocks. |
| `J006` | `GPTs/attachments/05_data_types_properties.md`, `08`, `06` | Optimizer, normalization, lock, timeout, autocommit, session, locale, and performance property blocks. |
| `J007` | `GPTs/attachments/05_data_types_properties.md`, `09`, `18` | Account, access-list, SSL/TLS, replication, network, port, and SQL-apply property blocks. |
| `J008` | `GPTs/attachments/03_sql_ddl_generation.md`, `02`, `05` | DDL and storage SQL generation blocks with exact syntax, privileges, destructive cautions, and validation SQL. |
| `J009` | `GPTs/attachments/04_sql_dml_oracle_compatibility.md`, `05`, `15` | DML/function/data-type/Oracle-difference blocks with literal grammar tokens and conversion-risk guidance. |
| `J010` | `GPTs/attachments/07_error_messages_troubleshooting.md`, `13`, `14` | Error and troubleshooting blocks preserving exact code forms, symbols, cause/action, and first checks. |
| `J011` | `GPTs/attachments/01_getting_started_installation.md`, `02`, `13` | Installation, startup, account, tablespace, datafile, and loganchor runbooks for first-time and veteran users. |
| `J012` | `GPTs/attachments/02_administration_operations.md`, `03`, `07` | Protected backup/recovery/destructive-operation runbooks with preconditions, stop points, and recovery checks. |
| `J013` | `GPTs/attachments/09_replication_ha_cdc.md`, `03`, `06` | Replication topology/state/SQL blocks with exact terms, compatibility checks, and unsafe-operation guardrails. |
| `J014` | `GPTs/attachments/09_replication_ha_cdc.md`, `16`, `18` | CDC, Log Analyzer, RepMgr, TLS, certificate, port, and network diagnostic blocks. |
| `J015` | `GPTs/attachments/06_data_dictionary_performance_views.md`, `08` | View, column, monitoring, SNMP, optimizer, plan, wait, lock, session, and check-SQL blocks. |
| `J016` | `GPTs/attachments/10_psm_stored_external_procedures.md`, `12`, `13`, `14` | PSM, CLI, ODBC, ACI, Precompiler, iSQL, iLoader, utility, and LOB/API token coverage. |
| `J017` | `GPTs/attachments/11_java_jdbc_spring.md`, `15`, `16`, `17`, `19` | Java, connector, migration, Kubernetes, Spatial, NiFi, Tableau, and integration reference blocks. |
| `J018` | All `GPTs/attachments/*.md`, `GPTs/reports/coverage_matrix.md` | Retrieval headings, aliases, cross-links, and compact index blocks that improve exact fact/token recall. |
| `J019` | `evals/altibase_answerability/reports/`, optional manifest/report notes | Targeted calibration report comparing lexical, full-context, and instruction-aware behavior for representative failures. |
| `J020` | `GPTs/attachments/*.md`, `GPTs/GPT_Instructions_Draft.md`, `GPTs/reports/` | Residual fixes from calibration without benchmark threshold reduction or unsupported claims. |
| `J021` | All `GPTs/attachments/*.md`, `GPTs/reports/` | Editorial QA report and fixes for customer clarity, expert density, unsafe-answer resistance, and source-backed consistency. |
| `J022` | Validation reports, `evals/altibase_answerability/reports/`, `GPTs/reports/final_upload_readiness.md` | Final validation results, readiness update, full-benchmark rerun plan, and residual-risk summary. |

## Jobs

| ID | Status | Title | Goal |
| --- | --- | --- | --- |
| `J001` | `ToDo` | Failure inventory and remediation map | Turn the 2026-05-17 root-cause analysis into a source-backed remediation inventory that maps failed benchmark questions to attachment files, missing tokens, and customer answer patterns. |
| `J002` | `ToDo` | Customer answer contract and GPT instructions | Update the GPT answer contract so beginner and veteran customers receive complete source-backed answers with exact tokens, version boundaries, and safe escalation behavior. |
| `J003` | `ToDo` | Exact token gap inventory | Source-check required tokens classed as absent or weakly retrievable, then write a prioritized token and syntax gap inventory before editing attachments. |
| `J004` | `ToDo` | Core identity path and storage properties | Strengthen core, identity, path, memory-directory, database-file, log-anchor, and storage property blocks for defaults, counts, mutability, and startup/restart behavior. |
| `J005` | `ToDo` | Memory disk volatile and log limit properties | Strengthen memory, disk, volatile, log-size, plan-cache, result-cache, and capacity-limit property blocks with exact defaults, ranges, units, and exceeded-limit behavior. |
| `J006` | `ToDo` | Optimizer performance session and locale properties | Strengthen optimizer, normalization, lock, timeout, autocommit, session, locale, and performance property blocks with exact values, SQL, and runtime cautions. |
| `J007` | `ToDo` | Security access replication and network properties | Strengthen account, access-list, SSL/TLS, replication, network, port, and SQL-apply property blocks with exact values, scope, reload behavior, and high-risk cautions. |
| `J008` | `ToDo` | DDL and storage SQL generation blocks | Strengthen tablespace, datafile, table, partition, index, constraint, LOB storage, and destructive-DDL generation blocks with exact syntax and caveats. |
| `J009` | `ToDo` | DML functions data types and Oracle-difference blocks | Strengthen DML, expressions, functions, JSON, LOB, data type, object-name, and Oracle migration difference blocks with literal grammar tokens and compatibility cautions. |
| `J010` | `ToDo` | Error code and troubleshooting blocks | Strengthen error-message, altierr, SQL/property error, tool/driver error, and first-check troubleshooting blocks with exact codes, symbols, cause/action, and escalation inputs. |
| `J011` | `ToDo` | Installation administration and tablespace runbooks | Strengthen beginner-to-veteran runbooks for installation, licensing, environment setup, startup/shutdown, accounts, privileges, tablespaces, datafiles, and log anchors. |
| `J012` | `ToDo` | Backup recovery and destructive-operation runbooks | Strengthen protected-topic runbooks for backup, archive log, restore, incomplete recovery, media failure, RESETLOGS, DROP/DISCARD/REUSE, and stop-condition handling. |
| `J013` | `ToDo` | Replication topology state and SQL blocks | Strengthen replication terminology, topology, state transitions, DDL/control SQL, gap handling, compatibility checks, and unsafe-operation guardrails. |
| `J014` | `ToDo` | CDC Log Analyzer RepMgr TLS and network blocks | Strengthen CDC, Log Analyzer, Replication Manager, replication SSL, ordinary TLS, certificate, port, and network diagnostic blocks. |
| `J015` | `ToDo` | Views performance monitoring and optimizer blocks | Strengthen data dictionary, performance view, monitoring API, SNMP, optimizer, execution plan, wait/lock/session, and check-SQL blocks with exact view and column tokens. |
| `J016` | `ToDo` | PSM CLI ODBC C precompiler iSQL iLoader utility blocks | Strengthen PSM, external procedures, CLI, ODBC, ACI, Precompiler, iSQL, iLoader, utilities, dataCompJ, dump tools, and LOB/API token coverage. |
| `J017` | `ToDo` | Java connectors migration spatial and integration blocks | Strengthen JDBC, Java, Spring, Hibernate, DB Link, adapters, Kubernetes, AKU, Migration Center, Spatial, NiFi, Tableau, and third-party connector coverage. |
| `J018` | `ToDo` | Retrieval structure and cross-link pass | Reorganize attachment headings, aliases, cross-references, and compact index blocks so lexical retrieval finds the exact customer-answer block without flooding context. |
| `J019` | `ToDo` | Targeted benchmark calibration | Run or prepare targeted calibration on representative failed questions using current lexical context, full context, and instruction-aware context; record whether remaining failures are content, retrieval, synthesis, or judge issues. |
| `J020` | `ToDo` | Residual gap remediation pass | Use the targeted calibration results to fix remaining high-impact attachment and instruction gaps without lowering benchmark expectations. |
| `J021` | `ToDo` | Customer LLM editorial QA | Review the updated attachment set as a customer-facing LLM corpus for both first-time and veteran Altibase users, including clarity, density, source-backing, and unsafe-answer resistance. |
| `J022` | `ToDo` | Final validation readiness and rerun plan | Run available validation checks, review diffs, update readiness reports, and prepare the final full-benchmark rerun instructions and residual-risk summary. |

## Resume Rules

- `Fail`: stop before starting later jobs.
- Dirty project files: stop before starting or advancing to another job.
- `Progress`: preserve interruption evidence, set the job back to `ToDo`, then rerun only when project files are clean.
- `Done`: skip.
- Nonzero `codex exec` exits leave the job as `Progress` by default; the next manual run stops if project files are dirty, or resets runtime state and retries when clean.

## Acceptance Checklist

- Each job has a matching prompt in `prompts/`.
- Each job has concrete acceptance criteria.
- Each successful job leaves project files clean and advances HEAD with a commit.
- `bash -n run-all.sh` passes.
