# Altibase GPT Encyclopedia Rebuild

- Kind: `docs`
- Status values: `ToDo`, `Progress`, `Done`, `Fail`
- User-run command: `./run-all.sh` from this directory
- Default behavior: continue through all jobs until completion or failure
- Optional single-job mode: `RUN_ONE=1 ./run-all.sh`
- Handoff gate: uncommitted project files stop the workflow before the next job starts
- Commit gate: each successful job must pass review and create a focused commit

## Workflow Requirements

`run-all.sh` prepends `requirements.md` to every job prompt at runtime. Treat that file
as the shared contract for source policy, English attachment output, multilingual
runtime behavior, coverage expectations, attachment boundaries, and verification.

## Partitioning Model

The workflow is split into 40 focused jobs so broad manual areas are not collapsed into
one oversized remediation pass. The partitioning is:

- J001-J003: requirements, source scope, coverage matrix, and extraction schemas.
- J004-J009: full property reference inventory, expansion, and QA.
- J010-J016: Altibase-specific SQL syntax and SQL generation coverage.
- J017-J021: dictionary, performance, replication, CDC, security, and monitoring views.
- J022-J026: error reference inventory, troubleshooting blocks, and unresolved gaps.
- J027-J033: installation, backup, recovery, administration, replication, and network runbooks.
- J034-J039: PSM, APIs, utilities, connectors, migration, Spatial, and integrations.
- J040: retrieval structure, multilingual validation, final gap review, and upload readiness.

## Jobs

| ID | Status | Title | Goal |
| --- | --- | --- | --- |
| `J001` | `Done` | Requirements and source scope | Finalize encyclopedia-grade requirements, source corpus scope, and success criteria. |
| `J002` | `Done` | Coverage matrix and gap register | Map selected source families to the 20 attachments and record item-level gaps. |
| `J003` | `Done` | Catalog schema and extraction rules | Define reusable item block schemas and Korean-first extraction rules for later jobs. |
| `J004` | `Done` | Property inventory baseline | Inventory property names and version availability from General Reference 1 sources. |
| `J005` | `Done` | Initialization and storage properties | Expand initialization, path, memory, disk, volatile, log, and storage property blocks. |
| `J006` | `Done` | LOB JSON and temporary object properties | Expand LOB, JSON, Temporary LOB, PSM, VARRAY, and object-size property blocks. |
| `J007` | `Done` | Performance and optimizer properties | Expand buffer, checkpoint, optimizer, plan cache, sort, hash, and execution memory properties. |
| `J008` | `Done` | Session network security and replication properties | Expand timeout, NLS, client, network, SSL/TLS, and replication property blocks. |
| `J009` | `ToDo` | Property catalog QA and cross references | Validate property coverage, dynamic-change wording, cross-references, and remaining gaps. |
| `J010` | `ToDo` | SQL syntax inventory and BNF rules | Inventory SQL statement families and define BNF conversion rules for SQL syntax diagrams. |
| `J011` | `ToDo` | Database tablespace and datafile SQL | Expand database, tablespace, datafile, archive, backup, restore, and recovery SQL coverage. |
| `J012` | `ToDo` | Table column constraint partition and queue DDL | Expand table, column, constraint, partition, LOB storage, and queue DDL coverage. |
| `J013` | `ToDo` | Index statistics hint and plan SQL | Expand index, statistics, hint, execution plan, and tuning-related SQL coverage. |
| `J014` | `ToDo` | Users privileges roles and schema object SQL | Expand user, privilege, role, sequence, synonym, view, and schema-object SQL coverage. |
| `J015` | `ToDo` | DML functions expressions and JSON SQL | Expand DML, predicates, functions, expressions, JSON SQL, and Oracle-difference coverage. |
| `J016` | `ToDo` | Replication and administrative SQL generation | Expand replication DDL, Log Analyzer SQL, property SQL, and administrative SQL generation. |
| `J017` | `ToDo` | Dictionary view inventory baseline | Inventory dictionary and performance view names, version availability, and grouping. |
| `J018` | `ToDo` | Storage log archive backup and tablespace views | Expand storage, datafile, log, archive, backup, checkpoint, and tablespace view blocks. |
| `J019` | `ToDo` | Session statement wait lock and transaction views | Expand session, statement, SQL text, wait, lock, transaction, and service-thread views. |
| `J020` | `ToDo` | Optimizer plan cache statistics and buffer views | Expand optimizer, plan cache, statistics, buffer pool, checkpoint, and performance views. |
| `J021` | `ToDo` | Replication CDC security monitoring and SNMP views | Expand replication, CDC, security, Monitoring API, and SNMP view/API mappings. |
| `J022` | `ToDo` | Error reference inventory and response schema | Inventory error code families and define error block and troubleshooting response schema. |
| `J023` | `ToDo` | Storage backup recovery and tablespace errors | Expand storage, backup, recovery, datafile, log, and tablespace error coverage. |
| `J024` | `Done` | SQL DDL data type JSON and LOB errors | Expand SQL, DDL, data type, constraint, JSON, LOB, and Temporary LOB error coverage. |
| `J025` | `ToDo` | Client network security replication and tool errors | Expand client, network, SSL/TLS, replication, utility, and tool error coverage. |
| `J026` | `Done` | Troubleshooting QA and unresolved error gaps | Validate troubleshooting structure, exact-code handling, escalation wording, and gaps. |
| `J027` | `ToDo` | Installation platform startup and shutdown runbooks | Expand installation, platform, database creation, startup, shutdown, and first-run runbooks. |
| `J028` | `ToDo` | Backup archive and incremental backup runbooks | Expand logical, offline, online, archive log, loganchor, and incremental backup runbooks. |
| `J029` | `ToDo` | Restore recovery and media failure runbooks | Expand complete, incomplete, incremental, tablespace, datafile, temp file, and media recovery runbooks. |
| `J030` | `ToDo` | Administration tablespace user and privilege runbooks | Expand admin, account, privilege, storage, tablespace lifecycle, and operational safety runbooks. |
| `J031` | `ToDo` | Replication topology state and compatibility | Expand replication topology, object restrictions, states, modes, and compatibility checks. |
| `J032` | `ToDo` | Replication operations CDC Log Analyzer and RepMgr | Expand replication operations, synchronization, CDC, Log Analyzer, and Replication Manager workflows. |
| `J033` | `ToDo` | Network checks SSL TLS and replication SSL | Expand network diagnostics, ordinary TLS, certificate handling, and replication SSL separation. |
| `J034` | `ToDo` | PSM stored and external procedures | Expand PSM, packages, triggers, VARRAY, external procedure, and library reference coverage. |
| `J035` | `ToDo` | Java JDBC Spring Hibernate and adapters | Expand JDBC, Java compatibility, Spring, Hibernate, Adapter for JDBC, and Java-facing examples. |
| `J036` | `ToDo` | CLI ODBC C Interface Precompiler and LOB APIs | Expand CLI, ODBC, Altibase C Interface, Precompiler, LOB, JSON LOB, and API diagnostics. |
| `J037` | `ToDo` | iSQL iLoader utilities dataCompJ and dump tools | Expand iSQL, iLoader, utilities, dataCompJ, dump tools, and operational tool workflows. |
| `J038` | `ToDo` | DB Link connectors Kubernetes and AKU | Expand DB Link, Hadoop, third-party connectors, Kubernetes, AKU, and cloud/container workflows. |
| `J039` | `ToDo` | Migration Oracle compatibility Spatial NiFi and Tableau | Expand Migration Center, Adapter for Oracle, Spatial, altiShapeLoader, NiFi, and Tableau coverage. |
| `J040` | `ToDo` | Retrieval multilingual validation and final readiness | Finalize retrieval structure, multilingual policy, validation reports, final gap review, and upload readiness. |

## Resume Rules

- `Fail`: stop before starting later jobs.
- Dirty project files: stop before starting or advancing to another job.
- `Progress`: preserve interruption evidence first, stop if project files are dirty, or set the job back to `ToDo` and rerun only when project files are clean.
- `Done`: skip.
- Nonzero `codex exec` exits leave the job as `Progress` by default; the next manual run preserves status/diff evidence, then stops if project files are dirty or resets runtime state and retries when clean.

## Acceptance Checklist

- Each job has a matching prompt in `prompts/`.
- Each job has concrete acceptance criteria.
- Each successful job leaves project files clean and advances HEAD with a commit.
- `bash -n run-all.sh` passes.
