# GPT And Coding-Agent Scenario Tests

- Job: `S2-J011`
- Scope: representative scenario tests for direct GPT answers and coding-agent
  outputs that generate or validate Altibase-backed service artifacts
- Status: scenario test contract

## Boundary

These scenarios test whether a GPT or coding agent can use the Stage 2
playbooks to produce source-backed first drafts. They do not approve
production execution. Every answer must preserve source routes, exact Altibase
tokens, missing-input prompts, validation checks, stop conditions, and
copy/paste artifact boundaries.

Required playbooks and instruction notes are present for the covered routes:
`service_development_artifact_generation.md`, `ddl_generation.md`,
`sql_data_types.md`, `properties.md`, `dictionary_views.md`,
`java_jdbc.md`, `odbc_c_clients.md`, `installation_startup.md`,
`backup_recovery.md`, `protected_operations.md`, `replication_cdc.md`,
`tools.md`, `migration_integrations.md`, `errors_troubleshooting.md`,
`aid_version_release_patch_routing.md`,
`coding_agent_instruction_note.md`, and
`gpt_service_development_instruction_note.md`. The dedicated
`test_generation.md` playbook remains a planned route in
`playbook_manifest.tsv`; scenario `SCN-016` therefore routes positive and
negative SQL tests through the completed SQL, DDL, dictionary, and service
artifact playbooks until `APB-000014` is promoted.

## Common Judge Setup

For every scenario, the judge must use
`GPTs/agent_playbooks/scenario_judge_rubric.md`. A scenario passes only when
the response scores at least the scenario threshold and has no blocker failure.

Shared blocker failures:

- Missing expected source IDs or replacing them with unsourced manual claims.
- Dropping required exact tokens or rewriting them into generic database terms.
- Inferring behavior from Oracle, MySQL, PostgreSQL, ANSI SQL, generic JDBC,
  generic ODBC, generic TLS, Kubernetes, or third-party assumptions.
- Marking a runnable artifact as safe when required customer inputs,
  environment evidence, validation output, or rollback evidence are missing.
- Omitting validation checks or stop conditions for protected operations.

## Scenario Result Ledger

| Scenario | Minimum scenario covered | Applicability | Pass threshold | Result |
| --- | --- | --- | --- | --- |
| `SCN-001` | Minimal Altibase-backed service plan | Both | 85/100 and no blocker | `Not run` |
| `SCN-002` | Application connection code and configuration | Both | 85/100 and no blocker | `Not run` |
| `SCN-003` | Disk tablespace DDL with validation SQL | Both | 85/100 and no blocker | `Not run` |
| `SCN-004` | User and privilege setup | Both | 85/100 and no blocker | `Not run` |
| `SCN-005` | GPT copy/paste implementation artifacts | Direct GPT primary; coding-agent secondary | 85/100 and no blocker | `Not run` |
| `SCN-006` | ODBC DSN configuration and verification | Both | 85/100 and no blocker | `Not run` |
| `SCN-007` | JDBC example with version caveats | Both | 85/100 and no blocker | `Not run` |
| `SCN-008` | iSQL script with spool/log handling | Both | 85/100 and no blocker | `Not run` |
| `SCN-009` | iLoader load/export workflow | Both | 85/100 and no blocker | `Not run` |
| `SCN-010` | Safe property change | Both | 85/100 and no blocker | `Not run` |
| `SCN-011` | Exact error diagnosis | Both | 85/100 and no blocker | `Not run` |
| `SCN-012` | Backup/recovery check | Both | 85/100 and no blocker | `Not run` |
| `SCN-013` | Replication setup draft | Both | 85/100 and no blocker | `Not run` |
| `SCN-014` | TLS basics | Both | 85/100 and no blocker | `Not run` |
| `SCN-015` | Utility or migration workflow | Both | 85/100 and no blocker | `Not run` |
| `SCN-016` | Positive and negative SQL tests | Both | 85/100 and no blocker | `Not run` |

### SCN-001: Minimal Altibase-Backed Service Plan

- Minimum scenario: design a minimal Altibase-backed service implementation
  plan with required inputs, interfaces, schema work, validation, and stop
  conditions.
- Input Prompt: "Plan a minimal Altibase-backed order service for a new team.
  Include the required customer inputs, schema and privilege work, connection
  interface choice, validation checks, and stop conditions. Target Altibase is
  not yet confirmed."
- Expected Source IDs: `SRC-000049`, `SRC-000018`, `SRC-000056`,
  `SRC-000025`, `SRC-000057`, `SRC-000026`.
- Expected Source Routes: `APB-000015`, `APB-000002`, `APB-000003`,
  `APB-000005`, `CONF-000004`, `CONF-000005`.
- Expected Artifacts: service plan, source-route block, missing-input list,
  schema-work outline, privilege-work outline, validation plan, test plan, and
  stop-condition list.
- Applicability: Both. Direct GPT should return a structured answer; a
  coding-agent output may also create a plan file when the user requests one.
- Required Exact Tokens: `V$VERSION`, `V$PROPERTY`, `V$TABLE`,
  `V$ALLCOLUMN`, `GRANT`, `REVOKE`, `Altibase 8.1 verified source`.
- Forbidden Generic Assumptions: no Oracle-compatible shortcut, no generic
  JDBC or ODBC defaults, no `IF EXISTS` or `IF NOT EXISTS` unless exact
  target-version source and customer evidence are supplied.
- Missing Inputs: target Altibase version, patch level, platform,
  service goal, workload, schema names, object definitions, interface choice,
  privilege model, validation target, and rollback or cleanup plan.
- Expected Files/Code/SQL/Commands/Configuration/Tests:
  `service_plan.md` for coding-agent use, plus named draft sections for
  `00_precheck.sql`, `10_schema.sql`, `20_privileges.sql`,
  `90_validation.sql`, and non-production test cases.
- Validation Checks: require source route validation, `V$VERSION`, dictionary
  checks with `V$TABLE` and `V$ALLCOLUMN`, privilege validation route, and an
  explicit note that live validation output is still required.
- Stop Conditions: stop before runnable SQL when target version, object names,
  storage plan, privilege approval, or rollback plan is missing.
- Scenario Scoring Rubric: use the 100-point S2-J011 rubric, with extra weight
  on source routing, missing inputs, generated artifact structure, validation,
  and stop conditions.
- Pass Threshold: 85/100 and no blocker failure.
- Pass/Fail Result Placeholder: `Not run`.

### SCN-002: Application Connection Code And Configuration

- Minimum scenario: generate application connection code and configuration for
  a supported interface.
- Input Prompt: "Generate first-draft Java connection code and configuration
  for an Altibase-backed API service. Include dependency, connection URL,
  credentials placeholders, a connection test, and diagnostics. I have not
  provided the driver JAR or JDK version."
- Expected Source IDs: `SRC-000047`, `SRC-000016`, `SRC-000061`,
  `SRC-000030`, `SRC-000111`, `SRC-000080`, `AID-SRC-000434`.
- Expected Source Routes: `APB-000010`, `APB-000015`, `CONF-000006`,
  `CONF-000007`.
- Expected Artifacts: Java connection code, configuration snippet, build or
  run commands, connection test, diagnostics section, missing-input prompts,
  and source-route note.
- Applicability: Both. Direct GPT should provide copy/paste blocks with
  placeholders; coding-agent output may create source files and test files only
  in a requested project workspace.
- Required Exact Tokens: `Altibase.jdbc.driver.AltibaseDriver`,
  `jdbc:Altibase://`, `Altibase.jar`, `Altibase42.jar`, `java -version`,
  `SQLSTATE`.
- Forbidden Generic Assumptions: no generic JDBC driver class, no PostgreSQL or
  MySQL URL format, no compile-ready claim without exact driver JAR, JDK,
  classpath, credentials policy, and runtime evidence.
- Missing Inputs: target version, patch level, JDK version, actual driver JAR,
  host, port, database name, credentials policy, framework version, and runtime
  output.
- Expected Files/Code/SQL/Commands/Configuration/Tests:
  `AltibaseConnectionCheck.java`, `application.properties`, compile/run
  commands, connection smoke test, and diagnostic handling for connection
  failures.
- Validation Checks: require `java -version`, `java -jar` against the actual
  driver JAR, compile check, connection check, transaction or rollback smoke
  test when source-backed, and diagnostic capture.
- Stop Conditions: stop before claiming compile-ready or production-ready code
  if driver, JDK, runtime output, target version, or credentials policy is
  absent.
- Scenario Scoring Rubric: use the 100-point S2-J011 rubric, with extra weight
  on exact JDBC tokens, missing-input prompts, code/config separation, and
  compile/connection validation.
- Pass Threshold: 85/100 and no blocker failure.
- Pass/Fail Result Placeholder: `Not run`.

### SCN-003: Disk Tablespace DDL With Validation SQL

- Minimum scenario: generate a disk tablespace DDL with validation SQL.
- Input Prompt: "Draft a disk tablespace creation script for Altibase with
  validation SQL. Use placeholders where needed and tell me what you still need
  before it is safe to run."
- Expected Source IDs: `SRC-000049`, `SRC-000018`, `SRC-000113`,
  `SRC-000082`, `SRC-000057`, `SRC-000026`.
- Expected Source Routes: `APB-000002`, `APB-000005`, `APB-000016`,
  `CONF-000004`, `CONF-000005`.
- Expected Artifacts: precheck SQL, guarded `CREATE DISK TABLESPACE` draft,
  validation SQL, rollback or cleanup note, source-route note, and stop
  conditions.
- Applicability: Both. Direct GPT should return fenced `sql` blocks; a
  coding agent may create `00_precheck.sql`, `10_tablespace.sql`, and
  `90_validation.sql` only when asked to write files.
- Required Exact Tokens: `CREATE DISK TABLESPACE`, `DATAFILE`,
  `ALTER TABLESPACE`, `DROP TABLESPACE`, `V$TABLESPACES`, `V$DATAFILES`.
- Forbidden Generic Assumptions: no Oracle tablespace syntax, no default file
  path or autoextend behavior invented from another database, no destructive
  cleanup command without explicit approval.
- Missing Inputs: target version, tablespace name, datafile path, initial size,
  growth policy, disk capacity, archive-log state, replication membership,
  maintenance window, and rollback plan.
- Expected Files/Code/SQL/Commands/Configuration/Tests:
  `00_precheck.sql`, `10_create_disk_tablespace.sql`,
  `90_tablespace_validation.sql`, and optional non-production cleanup draft.
- Validation Checks: require source route validation, `V$VERSION`, dictionary
  validation through `V$TABLESPACES` and `V$DATAFILES`, file-path existence
  checks as customer-run commands, and post-run space/object validation.
- Stop Conditions: stop before runnable DDL if file path, size, source syntax,
  privilege, storage risk, archive-log state, or rollback plan is missing.
- Scenario Scoring Rubric: use the 100-point S2-J011 rubric, with extra weight
  on protected storage guardrails, exact DDL tokens, validation SQL, and stop
  conditions.
- Pass Threshold: 85/100 and no blocker failure.
- Pass/Fail Result Placeholder: `Not run`.

### SCN-004: User And Privilege Setup

- Minimum scenario: generate a user/privilege setup for an application schema.
- Input Prompt: "Create a least-privilege setup for an application schema:
  service user, role, object grants, validation SQL, and rollback notes. I have
  not listed the exact tables yet."
- Expected Source IDs: `SRC-000049`, `SRC-000018`, `SRC-000056`,
  `SRC-000025`, `SRC-000057`, `SRC-000026`.
- Expected Source Routes: `APB-000002`, `APB-000005`, `APB-000016`,
  `CONF-000004`, `CONF-000005`.
- Expected Artifacts: precheck SQL, `CREATE USER` or placeholder route,
  `CREATE ROLE`, `GRANT`, `REVOKE` or rollback draft, privilege validation SQL,
  and missing-input prompts.
- Applicability: Both. Direct GPT should return guarded SQL blocks; coding-agent
  output may write separate DCL and validation files when requested.
- Required Exact Tokens: `CREATE USER`, `CREATE ROLE`, `GRANT`, `REVOKE`,
  `SYS_GRANT_SYSTEM_`, `SYS_GRANT_OBJECT_`, `SYS_USER_ROLES_`.
- Forbidden Generic Assumptions: no broad DBA-style grants by default, no Oracle
  role semantics, no password policy invention, and no drop/cascade cleanup
  without object inventory and approval.
- Missing Inputs: target version, schema names, service user, role name,
  object list, required privileges, password policy, admin executor, and
  rollback plan.
- Expected Files/Code/SQL/Commands/Configuration/Tests:
  `00_privilege_precheck.sql`, `20_privileges.sql`,
  `90_privilege_validation.sql`, and `99_privilege_rollback.sql` as guarded
  draft artifacts.
- Validation Checks: require source route validation, privilege dictionary
  route checks, role membership checks, object existence checks, and a note
  that exact target-version view columns must be rechecked before hard-coding.
- Stop Conditions: stop before final DCL if object definitions, privilege list,
  executor authority, password handling, or rollback evidence is missing.
- Scenario Scoring Rubric: use the 100-point S2-J011 rubric, with extra weight
  on least-privilege structure, exact DCL tokens, validation SQL, and
  privilege-change stop conditions.
- Pass Threshold: 85/100 and no blocker failure.
- Pass/Fail Result Placeholder: `Not run`.

### SCN-005: GPT Copy/Paste Implementation Artifacts

- Minimum scenario: generate GPTs copy/paste implementation artifacts,
  including SQL, DDL, or DCL where appropriate, with required assumptions and
  warnings.
- Input Prompt: "Give me a copy/paste Altibase first-draft package for a small
  customer table, a service role, seed data, validation SQL, and cleanup. I want
  the SQL split into files."
- Expected Source IDs: `SRC-000049`, `SRC-000018`, `SRC-000056`,
  `SRC-000025`, `SRC-000120`, `SRC-000089`.
- Expected Source Routes: `APB-000015`, `APB-000002`, `APB-000003`,
  `APB-000005`, `CONF-000004`, `CONF-000005`.
- Expected Artifacts: source-route and assumptions block, missing-input
  prompts, safety notes, separated runnable SQL blocks, validation SQL, test
  cases, and cleanup or rollback draft.
- Applicability: Direct GPT primary; coding-agent secondary when asked to
  create files in a customer project.
- Required Exact Tokens: `00_precheck.sql`, `10_schema.sql`,
  `20_privileges.sql`, `30_seed_or_change_dml.sql`, `90_validation.sql`,
  `99_cleanup_or_rollback.sql`, `DDL can implicitly commit`, `CREATE TABLE`,
  `GRANT`.
- Forbidden Generic Assumptions: no generic SQL portability claim, no
  unsupported `IF NOT EXISTS`, no safe-to-run label without customer-supplied
  version, object names, privilege model, validation plan, and rollback plan.
- Missing Inputs: target version, patch level, schema, table, column data
  types, primary key, tablespace, privilege model, seed data, expected result,
  and cleanup approval.
- Expected Files/Code/SQL/Commands/Configuration/Tests:
  six named SQL artifact blocks, a non-production test section, expected row
  count checks, and cleanup or rollback draft.
- Validation Checks: require `V$VERSION`, `V$PROPERTY`, `V$TABLE`,
  `V$ALLCOLUMN`, expected row counts, privilege checks, and cleanup
  confirmation.
- Stop Conditions: stop before runnable artifacts when target source route,
  object definitions, destructive-effect approval, or rollback plan is missing.
- Scenario Scoring Rubric: use the 100-point S2-J011 rubric, with extra weight
  on direct-GPT copy/paste structure, artifact separation, exact file tokens,
  and guarded safety language.
- Pass Threshold: 85/100 and no blocker failure.
- Pass/Fail Result Placeholder: `Not run`.

### SCN-006: ODBC DSN Configuration And Verification

- Minimum scenario: configure and verify an ODBC DSN.
- Input Prompt: "Draft an ODBC DSN configuration for an Altibase client on
  Linux with verification steps and diagnostics. I have not provided the driver
  path or unixODBC files yet."
- Expected Source IDs: `SRC-000046`, `SRC-000015`, `SRC-000050`,
  `SRC-000019`, `SRC-000052`, `SRC-000021`, `AID-SRC-000434`.
- Expected Source Routes: `APB-000009`, `CONF-000006`, `CONF-000007`.
- Expected Artifacts: `odbc.ini` snippet, `odbcinst.ini` route, environment
  variables, connection string, first-check commands, diagnostic plan, and
  missing-input prompts.
- Applicability: Both. Direct GPT should return configuration snippets; a
  coding agent may write sample DSN files only in a requested test directory.
- Required Exact Tokens: `odbc.ini`, `odbcinst.ini`, `ODBCINI`,
  `ODBCSYSINI`, `DSN=ALTIBASE;LongDataCompat=ON`, `SQLDriverConnect`,
  `SQLGetDiagRec`, `SQLSTATE`.
- Forbidden Generic Assumptions: no generic ODBC driver name, no invented
  driver-manager path, no password embedded in reusable files when credentials
  policy is unknown.
- Missing Inputs: target version, OS, bitness, client package, driver path,
  unixODBC paths, DSN name, host, port, database name, credentials policy,
  `NLS_USE`, and runtime diagnostic output.
- Expected Files/Code/SQL/Commands/Configuration/Tests:
  `10_odbc.ini`, `10_odbcinst.ini`, environment export commands, connection
  test command, and diagnostic capture plan.
- Validation Checks: require source route validation, file path checks,
  driver-manager checks, test connection, `SQLGetDiagRec` diagnostics for
  failures, and `SQLSTATE` recording.
- Stop Conditions: stop before final DSN if driver path, bitness, DSN, user,
  password policy, library path, or runtime output is missing.
- Scenario Scoring Rubric: use the 100-point S2-J011 rubric, with extra weight
  on exact ODBC tokens, configuration separation, diagnostics, and missing
  client evidence.
- Pass Threshold: 85/100 and no blocker failure.
- Pass/Fail Result Placeholder: `Not run`.

### SCN-007: JDBC Example With Version Caveats

- Minimum scenario: create a JDBC connection example with version caveats.
- Input Prompt: "Show a minimal JDBC connection example for Altibase and list
  the version caveats for driver JAR selection and failover options."
- Expected Source IDs: `SRC-000047`, `SRC-000016`, `SRC-000061`,
  `SRC-000030`, `SRC-000473`, `AID-SRC-000435`.
- Expected Source Routes: `APB-000010`, `APB-000017`, `CONF-000006`,
  `CONF-000007`.
- Expected Artifacts: minimal Java snippet, JDBC URL example, driver JAR
  caveat list, optional failover URL caveat, compile/run commands, and
  connection validation.
- Applicability: Both. Direct GPT should return code and command snippets;
  coding-agent output may add a test class only when a Java project is supplied.
- Required Exact Tokens: `Altibase.jdbc.driver.AltibaseDriver`,
  `jdbc:Altibase://host_ip:port_no/database_name`, `Altibase.jar`,
  `Altibase42.jar`, `Altibase7_1.jar`, `alternateservers`, `java -jar`.
- Forbidden Generic Assumptions: no generic JDBC URL, no claim that one JAR
  fits every target without source and installed-driver evidence, and no
  failover guarantee without exact source and runtime validation.
- Missing Inputs: target Altibase version, patch level, JDK version, delivered
  JAR name, classpath, host, port, database name, credentials policy, framework
  version, and runtime output.
- Expected Files/Code/SQL/Commands/Configuration/Tests:
  `AltibaseJdbcCheck.java`, optional `application.properties`, classpath
  command, driver JAR inspection command, and connection test.
- Validation Checks: require `java -version`, `java -jar Altibase.jar` or the
  actual delivered JAR, compile check, connection check, and diagnostic capture.
- Stop Conditions: stop before compile-ready or failover-ready claims when
  target version, JAR, JDK, URL, credentials policy, or runtime validation is
  absent.
- Scenario Scoring Rubric: use the 100-point S2-J011 rubric, with extra weight
  on version caveats, exact JDBC tokens, and compile/connection checks.
- Pass Threshold: 85/100 and no blocker failure.
- Pass/Fail Result Placeholder: `Not run`.

### SCN-008: iSQL Script With Spool And Log Handling

- Minimum scenario: run an iSQL script with spool/log handling.
- Input Prompt: "Create an iSQL script and command wrapper that spools query
  output, enables query logging for the run, validates the output, and turns
  logging off or documents cleanup."
- Expected Source IDs: `SRC-000045`, `SRC-000078`, `SRC-000108`,
  `SRC-000139`, `SRC-000168`, `SRC-000199`.
- Expected Source Routes: `APB-000011`, `CONF-000006`, `CONF-000007`.
- Expected Artifacts: shell command, iSQL script, spool file path, query log
  path, validation checks, cleanup/log-retention note, and missing-input
  prompts.
- Applicability: Both. Direct GPT should return script blocks; coding-agent
  output may create `checks.sql` and a wrapper only when asked.
- Required Exact Tokens: `iSQL`, `SPOOL`, `SPOOL OFF`,
  `SET QUERYLOGGING ON`, `SET QUERYLOGGING OFF`,
  `$ALTIBASE_HOME/trc/isql_query.log`, `START file_name`, `@ file_name`,
  `@@ file_name`.
- Forbidden Generic Assumptions: no SQL*Plus-only behavior, no unconfirmed
  script include path, no inline production password recommendation, and no
  permanent query logging without an explicit retention or cleanup plan.
- Missing Inputs: target version, platform, `$ALTIBASE_HOME`, host, port, user,
  credentials policy, script working directory, output directory, expected rows,
  and log retention policy.
- Expected Files/Code/SQL/Commands/Configuration/Tests:
  `run_checks.sh`, `checks.sql`, `checks.spool`, `checks.out`, validation SQL,
  and cleanup commands for generated files.
- Validation Checks: require installed `isql` help or version evidence,
  successful command exit, `SPOOL OFF`, query log path check, expected row
  counts, and preserved script/output files.
- Stop Conditions: stop before final command if connection values, working
  directory, credentials policy, expected results, or log cleanup policy is
  missing.
- Scenario Scoring Rubric: use the 100-point S2-J011 rubric, with extra weight
  on exact iSQL tokens, spool/log lifecycle, validation, and cleanup.
- Pass Threshold: 85/100 and no blocker failure.
- Pass/Fail Result Placeholder: `Not run`.

### SCN-009: iLoader Load And Export Workflow

- Minimum scenario: prepare an iLoader load/export workflow.
- Input Prompt: "Prepare an iLoader workflow to export a table, load it into a
  test schema, capture bad/log files, and validate row counts. I have not
  supplied the FORM file or data file names."
- Expected Source IDs: `SRC-000044`, `SRC-000077`, `SRC-000107`,
  `SRC-000138`, `SRC-000167`, `SRC-000198`.
- Expected Source Routes: `APB-000011`, `CONF-000006`, `CONF-000007`.
- Expected Artifacts: `iloader formout`, export command, load command,
  file-inventory checklist, bad/log handling, result-code handling, row-count
  validation, and rollback/reload plan.
- Applicability: Both. Direct GPT should provide guarded commands; coding-agent
  output may create a workflow script only for a non-production directory.
- Required Exact Tokens: `iloader formout`, `iloader out`, `iloader in`,
  `-bad`, `-log`, `-mode APPEND`, `-commit`, `-array`,
  `Total 3 record download(T1)`, `Load Count : 2(T1)`, `-2`.
- Forbidden Generic Assumptions: no generic CSV behavior, no omitted NLS check,
  no `-direct nolog` without backup/recovery evidence, and no production load
  command without rollback approval.
- Missing Inputs: target version, platform, tool version, table name, FORM file,
  data file, delimiter or CSV rule, NLS policy, mode, commit/array size, bad/log
  paths, source/target row counts, and rollback plan.
- Expected Files/Code/SQL/Commands/Configuration/Tests:
  `formout` command, export command, load command, `*.fmt`, `*.dat`,
  `*.bad`, `*.log`, row-count SQL, and reload/cleanup notes.
- Validation Checks: require installed help output, file existence checks,
  `-bad` and `-log` inspection, return code handling for `0`, `-1`, and `-2`,
  `Load Count`, and source/target row-count comparison.
- Stop Conditions: stop when FORM/data files, NLS, mode, bad/log paths,
  source/target table definitions, or rollback plan are missing; stop on
  non-empty bad files or row-count mismatch.
- Scenario Scoring Rubric: use the 100-point S2-J011 rubric, with extra weight
  on exact iLoader tokens, result handling, file artifacts, and validation.
- Pass Threshold: 85/100 and no blocker failure.
- Pass/Fail Result Placeholder: `Not run`.

### SCN-010: Safe Property Change

- Minimum scenario: change a property safely with dynamic/static handling.
- Input Prompt: "Draft a safe plan to change one Altibase property. The
  property name and target value are placeholders. Show how to decide whether
  it can use ALTER SYSTEM, ALTER SESSION, or altibase.properties."
- Expected Source IDs: `SRC-000049`, `SRC-000018`, `SRC-000056`,
  `SRC-000025`, `SRC-000072`, `SRC-000040`.
- Expected Source Routes: `APB-000004`, `APB-000016`, `CONF-000004`,
  `CONF-000005`.
- Expected Artifacts: property inventory SQL, dynamic/static decision record,
  guarded `ALTER SESSION` or `ALTER SYSTEM` draft, file-change plan,
  validation SQL, rollback plan, and stop conditions.
- Applicability: Both. Direct GPT should return guarded SQL/config blocks; a
  coding agent may create a change-plan file but must not edit
  `altibase.properties` without explicit customer request and evidence.
- Required Exact Tokens: `V$PROPERTY`, `ALTER SYSTEM SET`,
  `ALTER SESSION SET`, `altibase.properties`, `ADMIN_MODE`, `LOGANCHOR_DIR`,
  `ARCHIVE_DIR`, `INCREMENTAL_BACKUP_CHUNK_SIZE`.
- Forbidden Generic Assumptions: no generic dynamic-property rule, no invented
  default, range, unit, or restart behavior, and no online change for
  database-creation-only or startup-only properties without exact source proof.
- Missing Inputs: target version, patch level, property name, current value,
  desired value, source section, dynamic-change level, startup phase, restart
  window, replication/archive-log state, and rollback plan.
- Expected Files/Code/SQL/Commands/Configuration/Tests:
  `00_property_inventory.sql`, `10_dynamic_property_change.sql`,
  `altibase.properties` change plan, file validation commands, and
  `90_property_validation.sql`.
- Validation Checks: require exact source route for the property row,
  `V$PROPERTY` before/after, file readability checks, restart or session scope
  confirmation, and rollback validation.
- Stop Conditions: stop before changing read-only, `NONE`, startup-only,
  database-creation-only, out-of-range, or unit-unknown properties.
- Scenario Scoring Rubric: use the 100-point S2-J011 rubric, with extra weight
  on dynamic/static handling, exact property tokens, missing-input prompts, and
  rollback validation.
- Pass Threshold: 85/100 and no blocker failure.
- Pass/Fail Result Placeholder: `Not run`.

### SCN-011: Exact Error Diagnosis

- Minimum scenario: diagnose an exact error code.
- Input Prompt: "Diagnose this Altibase error safely: ERR-2106C. I only have
  the code, not the full log or SQL. Explain what you need and provide the next
  checks."
- Expected Source IDs: `SRC-000054`, `SRC-000023`, `SRC-000118`,
  `SRC-000087`, `SRC-000076`, `SRC-000043`.
- Expected Source Routes: `APB-000013`, `APB-000011`, `CONF-000005`,
  `CONF-000006`, `CONF-000008`.
- Expected Artifacts: error evidence packet, source-route note, missing-input
  prompts, `altierr` lookup commands, log collection commands, safe next SQL or
  dictionary checks, and escalation packet.
- Applicability: Both. Direct GPT should provide diagnosis boundaries and next
  checks; coding-agent output may prepare a diagnostic script only when logs and
  environment paths are supplied.
- Required Exact Tokens: `ERR-2106C`, `0x6100D`, `SQLSTATE`, `altierr`,
  `exact_error_code`, `error_symbol`, `altibase_error.log`,
  `altibase_boot.log`.
- Forbidden Generic Assumptions: no inferred root cause from prefix alone, no
  invented `SQLSTATE`, no definitive fix without full error text, logs, runtime
  state, object definitions, and target version.
- Missing Inputs: target version, patch level, full error message, `SQLSTATE`,
  error symbol if available, SQL or command, log excerpt, runtime state, object
  definitions, timestamp, and reproduction steps.
- Expected Files/Code/SQL/Commands/Configuration/Tests:
  error packet template, `altierr` commands, scoped log grep commands, read-only
  dictionary/view checks, and escalation packet.
- Validation Checks: require source route validation, exact token preservation,
  `altierr` output, matching log timestamp, supplied SQL/command context, and
  any source-backed read-only next check.
- Stop Conditions: stop before root-cause or repair claims when full error
  text, logs, runtime state, source route, or reproduction evidence is absent.
- Scenario Scoring Rubric: use the 100-point S2-J011 rubric, with extra weight
  on exact error-token preservation, missing evidence, safe next checks, and no
  invented root cause.
- Pass Threshold: 85/100 and no blocker failure.
- Pass/Fail Result Placeholder: `Not run`.

### SCN-012: Backup And Recovery Check

- Minimum scenario: plan a backup and recovery check without unsafe production
  commands.
- Input Prompt: "Plan how to verify whether an Altibase database has enough
  backup and recovery evidence for an online backup rehearsal. Do not give me
  unsafe production recovery commands."
- Expected Source IDs: `SRC-000049`, `SRC-000018`, `SRC-000056`,
  `SRC-000025`, `SRC-000072`, `SRC-000040`, `AID-SRC-000429`.
- Expected Source Routes: `APB-000006`, `APB-000016`, `CONF-000004`,
  `CONF-000005`, `CONF-000007`.
- Expected Artifacts: read-only backup evidence checklist, archive-log state
  checks, file inventory commands, guarded backup template, recovery stop
  points, and rollback/recovery evidence list.
- Applicability: Both. Direct GPT should return a guarded runbook; coding-agent
  output may create a checklist or read-only script only with supplied paths.
- Required Exact Tokens: `ARCHIVELOG`, `NOARCHIVELOG`,
  `ALTER DATABASE BACKUP DATABASE`, `ALTER DATABASE BACKUP TABLESPACE`,
  `V$LOG`, `V$ARCHIVE`, `STARTUP CONTROL`, `ALTER DATABASE RESETLOGS`,
  `backupInfo`.
- Forbidden Generic Assumptions: no generic backup guarantee, no file movement,
  no restore, no `RESETLOGS`, and no production recovery command without exact
  failure scope, backup set, logs, recovery point, and approval.
- Missing Inputs: target version, backup mode, archive-log state, backup path,
  free space, datafile paths, online logs, archive logs, log anchors, backup
  inventory, failure scope, recovery point, maintenance window, and rollback
  evidence.
- Expected Files/Code/SQL/Commands/Configuration/Tests:
  read-only SQL checks, file inventory commands, guarded backup template,
  recovery evidence checklist, and non-production rehearsal plan.
- Validation Checks: require `V$PROPERTY`, `V$LOG`, `V$ARCHIVE`, backup path
  inventory, archive-log evidence, backup file inventory, and explicit
  source-recheck before any recovery syntax is filled.
- Stop Conditions: stop before online backup if archive-log state, backup path,
  or free space is unknown; stop before recovery if backup set, logs, anchors,
  failure scope, or recovery point is missing.
- Scenario Scoring Rubric: use the 100-point S2-J011 rubric, with extra weight
  on protected recovery guardrails, read-only checks, and stop conditions.
- Pass Threshold: 85/100 and no blocker failure.
- Pass/Fail Result Placeholder: `Not run`.

### SCN-013: Replication Setup Draft

- Minimum scenario: create a replication setup draft with topology and state
  guardrails.
- Input Prompt: "Draft a first-pass Altibase replication setup for two nodes.
  Include topology inputs, CREATE REPLICATION placeholders, state checks, and
  hold points. I have not provided table definitions or current replication
  state."
- Expected Source IDs: `SRC-000070`, `SRC-000038`, `SRC-000132`,
  `SRC-000101`, `SRC-000192`, `SRC-000161`.
- Expected Source Routes: `APB-000007`, `APB-000002`, `APB-000005`,
  `CONF-000004`, `CONF-000005`, `CONF-000006`, `CONF-000008`.
- Expected Artifacts: topology input checklist, replication precheck SQL,
  guarded `CREATE REPLICATION` draft, state-check SQL, hold-point commands,
  validation plan, and rollback or recovery note.
- Applicability: Both. Direct GPT should return guarded SQL and checklist
  blocks; coding-agent output may create draft files only for a non-production
  workspace.
- Required Exact Tokens: `CREATE REPLICATION`, `ALTER REPLICATION`,
  `DROP REPLICATION`, `V$REPSENDER`, `V$REPRECEIVER`, `V$REPGAP`,
  `SYNC ONLY`, `QUICKSTART`, `REPLICATION_DDL_SYNC`.
- Forbidden Generic Assumptions: no generic replication semantics, no automatic
  bidirectional assumption, no state-changing `ALTER REPLICATION` command
  without topology, object definitions, current state, logs, and approval.
- Missing Inputs: target version, patch level, topology, local host, remote
  host, replication ports, mode, object definitions, primary keys, character
  sets, current sender/receiver state, logs, validation plan, and rollback plan.
- Expected Files/Code/SQL/Commands/Configuration/Tests:
  `00_replication_precheck.sql`, `10_create_replication.sql`,
  `20_state_checks.sql`, guarded hold-point commands, and validation notes.
- Validation Checks: require `V$REPSENDER`, `V$REPRECEIVER`, `V$REPGAP`,
  source/target object validation, replication state confirmation, trace-log
  collection, and post-draft review before state changes.
- Stop Conditions: stop before `CREATE REPLICATION` or `ALTER REPLICATION`
  when topology, object definitions, primary keys, state, logs, source syntax,
  or rollback plan is missing.
- Scenario Scoring Rubric: use the 100-point S2-J011 rubric, with extra weight
  on topology inputs, state guardrails, exact replication tokens, validation,
  and stop conditions.
- Pass Threshold: 85/100 and no blocker failure.
- Pass/Fail Result Placeholder: `Not run`.

### SCN-014: TLS Client/Server Basics

- Minimum scenario: configure TLS client/server basics with certificate path
  checks.
- Input Prompt: "Draft the basics for enabling Altibase server/client TLS in a
  test environment. Include certificate path checks and explain what is still
  required before changing the server."
- Expected Source IDs: `SRC-000051`, `SRC-000020`, `SRC-000115`,
  `SRC-000084`, `SRC-000175`, `SRC-000145`, `AID-SRC-000428`.
- Expected Source Routes: `APB-000008`, `APB-000004`, `APB-000016`,
  `CONF-000004`, `CONF-000006`, `CONF-000007`.
- Expected Artifacts: TLS property inventory SQL, certificate file checklist,
  guarded `altibase.properties` snippet, client connection note, validation
  commands, rollback plan, and stop conditions.
- Applicability: Both. Direct GPT should provide guarded config snippets; a
  coding agent may create a checklist or test config only in a requested test
  directory.
- Required Exact Tokens: `SSL_ENABLE`, `SSL_PORT_NO`, `SSL_CERT`, `SSL_KEY`,
  `SSL_CA`, `SSL_CAPATH`, `SSL_VERIFY`, `SSL_LOAD_CONFIG`, `openssl version`.
- Forbidden Generic Assumptions: no generic TLS default, no recommendation to
  set `SSL_VERIFY=0` without explicit customer security policy, no confusion of
  client/server TLS with replication SSL.
- Missing Inputs: target version, patch level, certificate paths, CA path,
  private-key permissions, access policy, client type, network path, OpenSSL
  version, authentication mode, restart window, and rollback plan.
- Expected Files/Code/SQL/Commands/Configuration/Tests:
  `00_tls_property_inventory.sql`, certificate path shell checks,
  `altibase.properties` draft, client connection validation, and rollback
  checklist.
- Validation Checks: require `V$PROPERTY` for TLS properties, file existence and
  permissions checks, `openssl version`, client connection test, log review, and
  rollback validation.
- Stop Conditions: stop before server changes when certificate paths, key
  permissions, OpenSSL compatibility, restart window, access policy, or
  rollback plan is missing.
- Scenario Scoring Rubric: use the 100-point S2-J011 rubric, with extra weight
  on exact TLS tokens, certificate path checks, protected property handling, and
  stop conditions.
- Pass Threshold: 85/100 and no blocker failure.
- Pass/Fail Result Placeholder: `Not run`.

### SCN-015: Utility Or Migration Workflow

- Minimum scenario: use a utility or migration tool with expected output and
  error handling.
- Input Prompt: "Draft a Migration Center workflow for moving a source schema
  to Altibase. Include register/build/reconcile/run/diff steps, expected output
  files, unsupported-object handling, and stop conditions."
- Expected Source IDs: `SRC-000216`, `SRC-000223`, `SRC-000202`,
  `SRC-000209`, `SRC-000430`, `AID-SRC-000356`.
- Expected Source Routes: `APB-000012`, `APB-000017`, `CONF-000006`,
  `CONF-000007`, `CONF-000009`.
- Expected Artifacts: migration input checklist, guarded `migcenter.sh`
  commands, report/output inventory, unsupported-object handling,
  validation plan, rollback plan, and cleanup note.
- Applicability: Both. Direct GPT should return guarded commands and report
  checks; coding-agent output may create project scripts only when the project
  directory and drivers are supplied.
- Required Exact Tokens: `Migration Center`, `migcenter.sh`, `register.xml`,
  `BuildReport4Unsupported.html`, `RunReport4Summary.html`,
  `RunReport4Missing.html`, `DbObj_Create.sql`, `DbObj_Failed.sql`,
  `iLoaderIn.sh`.
- Forbidden Generic Assumptions: no universal source-database support claim, no
  production `run` command without Build/Reconcile report review, no unsupported
  third-party compatibility claim, and no treating reports as clean when missing.
- Missing Inputs: source DB product and version, target Altibase version,
  JDBC drivers, project path, `register.xml`, `options.xml`, object scope,
  data validation policy, primary keys, output directories, rollback plan, and
  cutover approval.
- Expected Files/Code/SQL/Commands/Configuration/Tests:
  `register.xml`, `options.xml`, `migcenter.sh` command sequence,
  generated SQL/report file checklist, failed-data directory review, and
  validation reports.
- Validation Checks: require driver evidence, Build report review,
  Reconcile report review, generated SQL inspection, `RunReport4Summary.html`,
  `RunReport4Missing.html`, failed SQL or data review, and post-run comparison.
- Stop Conditions: stop when drivers, project files, Build/Reconcile outputs,
  unsupported-object report, rollback plan, or production approval are missing.
- Scenario Scoring Rubric: use the 100-point S2-J011 rubric, with extra weight
  on exact migration tokens, report validation, third-party caveats, and stop
  conditions.
- Pass Threshold: 85/100 and no blocker failure.
- Pass/Fail Result Placeholder: `Not run`.

### SCN-016: Positive And Negative SQL Tests

- Minimum scenario: design positive and negative SQL tests from source-backed
  syntax.
- Input Prompt: "Design positive and negative SQL tests for a generated
  Altibase table and query. Include setup, expected pass output, expected
  negative error token, validation SQL, and cleanup. The exact target version
  and table definition are not supplied."
- Expected Source IDs: `SRC-000056`, `SRC-000025`, `SRC-000120`,
  `SRC-000089`, `SRC-000180`, `SRC-000150`.
- Expected Source Routes: `APB-000003`, `APB-000002`, `APB-000005`,
  `APB-000015`, `APB-000014`, `CONF-000005`.
- Expected Artifacts: non-production test plan, setup SQL, positive SQL case,
  negative SQL case, expected tokens, validation SQL, cleanup SQL, and missing
  input prompts.
- Applicability: Both. Direct GPT should return test-case blocks; coding-agent
  output may create test files only when a target test harness is supplied.
- Required Exact Tokens: `positive case`, `negative case`,
  `expected error token`, `V$TABLE`, `V$ALLCOLUMN`, `ERR-`, `setup`,
  `cleanup`, `rollback`.
- Forbidden Generic Assumptions: no ANSI SQL portability claim, no invented
  error code, no unsupported data type or syntax, and no production test run
  without target-version and cleanup evidence.
- Missing Inputs: target version, feature under test, setup objects, table
  type, column data types, negative case, expected output, cleanup plan, and
  whether the test is non-production.
- Expected Files/Code/SQL/Commands/Configuration/Tests:
  `00_test_setup.sql`, `10_positive_case.sql`, `20_negative_case.sql`,
  `90_test_validation.sql`, and `99_test_cleanup.sql`.
- Validation Checks: require exact source route for tested syntax, setup object
  validation with `V$TABLE` and `V$ALLCOLUMN`, positive expected rows, negative
  expected error token, and cleanup confirmation.
- Stop Conditions: stop before final tests when target version, exact syntax
  route, setup objects, expected outputs, negative token, or cleanup plan is
  missing.
- Scenario Scoring Rubric: use the 100-point S2-J011 rubric, with extra weight
  on positive/negative pairing, exact expected tokens, validation, and cleanup.
- Pass Threshold: 85/100 and no blocker failure.
- Pass/Fail Result Placeholder: `Not run`.
