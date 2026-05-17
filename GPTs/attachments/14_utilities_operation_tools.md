# 14. Operations Utilities

## Applicable Versions

- 7.1: Based on Altibase 7.1 Utilities Manual and applicable tool manuals.
- 7.3: Based on Altibase 7.3 Utilities Manual, dataCompJ User's Manual, and dataCompJ release notes.
- 8.1: Based on Altibase 8.1 verified source Utilities Manual and tool manuals.

## Questions This File Can Answer

- Which Altibase utility should I use for logical migration, comparison, monitoring, or diagnostic work?
- How do I run `aexport`, and which generated scripts should I execute during a logical migration?
- How do I compare or synchronize replicated Altibase tables with `altiComp`?
- When should I use `dataCompJ` instead of `altiComp`?
- How should I interpret `altiComp`, `dataCompJ`, and dump-family output files?
- How do I operate `aku` for Altibase in a Kubernetes StatefulSet?
- What are `altiAudit`, `altiMon`, `altierr`, `altiProfile`, dump-family tools, `checkServer`, and `server` used for?
- Where is Replication Manager GUI workflow guidance covered?

## Retrieval Alias Index

Use this compact index before scanning utility command blocks. It is intentionally redundant with later headings so lexical retrieval can land on the exact migration, comparison, synchronization, monitoring, diagnostic, or dump-family block.

- Aliases and customer wording: utility, aexport, logical migration, altiComp, data comparison, data synchronization, dataCompJ, XML configuration, dumptrc, dumpla, dumpddf, altierr, altimon, altiMon, altiAudit, altiProfile, checkServer, server command, AKU utility.
- Exact-token anchors: `aexport`, `altiComp`, `dataCompJ`, `SYNC`, `SU`, `SI`, `MI`, `SD`, `Connections`, `Options`, `TablePairs`, `Materialized View`, `altierr`, `dumptrc`, `dumpla`, `dumpddf`, `checkServer`, `server`, `aku -p start`, `aku -p end`, `aku -p clean`, `ERR-00015`, `ERR-91144`.
- Answer route: use this file for utilities and diagnostics; use `13_isql_iloader_basic_tools.md` for iSQL and iLoader; use `17_kubernetes_aku_cloud.md` for Kubernetes AKU lifecycle; use `09_replication_ha_cdc.md` for Replication Manager topology and operation context.
- Stop condition: before `SYNC`, `aku -p clean`, generated import scripts, or corrective utility commands, require version, target host, port, database role, backup status, replication status, downtime window, and rollback plan.

## Source Documents

- 7.1: Altibase 7.1 Utilities Manual; dataCompJ User's Manual where applicable.
- 7.3: Altibase 7.3 Utilities Manual; dataCompJ User's Manual; dataCompJ 7.2 Release Notes.
- 8.1: Altibase 8.1 verified source Utilities Manual; dataCompJ User's Manual.

## Response Rules

- Answer explanatory text in the user's language.
- Keep utility names, command options, XML element names, SQL object names, property names, file names, paths, and error codes literal.
- If the customer does not specify a version, answer from the Altibase 8.1 verified source baseline and mention that exact option availability can differ on 7.1 and 7.3 clients.
- Do not expose internal source labels, repository paths, workstation paths, or original manual image paths in customer answers.
- Treat example credentials such as `sys/manager` as placeholders and advise the user to use environment-specific accounts and secure secret handling.
- For destructive or corrective utilities (`aexport` import scripts, `altiComp` `SYNC`, `dataCompJ` `SYNC`, `aku -p clean`, `server kill`), ask for version, target host, port, database role, recent backup status, replication status, downtime window, and rollback plan before giving a production-ready command.
- Prefer procedural text over screenshots. SQL syntax diagrams are represented as compact command syntax.

## Exact Utility Answer Blocks

Use these compact blocks when a customer asks for logical migration, comparison,
synchronization, error lookup, or dump-family diagnostics. Preserve the literal tool
names, policy codes, XML element names, file names, and error codes shown here.

Exact block: `aexport` purpose and object families

- Version scope: Altibase 8.1 verified source; selected 7.1 and 7.3 Utilities sources use the same logical-migration role with version-specific option lists.
- `aexport` supports automated logical migration between Altibase databases by saving logical structure and data as text, then generating scripts for reload into a new Altibase database.
- It can extract `users`, `privileges`, tables, `tablespaces`, constraints, indexes, views, `Materialized View`, `stored procedures`, `sequences`, and `replication objects` as documented.
- Because output is SQL scripts and text data, it is useful for movement between different Altibase versions and platforms.
- Run it when the Altibase server is running but not serving application workload or client connections.

Exact block: `DBMS_METADATA` prerequisite for `aexport`

- Version scope: Altibase 8.1 verified source and selected 7.3 Utilities source.
- `DBMS_METADATA` extracts object-creation DDL or `GRANT` statements from the data dictionary.
- `aexport` depends on the `DBMS_METADATA` package; install the package in Altibase before running `aexport`.
- If the package is not installed, `aexport` can fail with `ERR-91144 : DBMS_METADATA package does not exist`.
- Verify this prerequisite before export rather than diagnosing it only after script generation fails.

Exact block: `aexport` generated script order

- Version scope: Altibase 8.1 verified source.
- Run `aexport` first to generate migration scripts from the source database.
- Run `run_il_out.sh` to download source table data and verify `.fmt`, `.dat`, `.log`, and `.bad` files.
- Copy generated SQL, shell, `.fmt`, `.log`, `.dat`, and `.bad` files to the target host when source and target are on different systems.
- Run `run_is.sh` on the target to create the logical structure.
- Run `run_il_in.sh` to load data, inspect nonempty `.bad` files and related log files, then run generated post-load scripts such as `run_is_refresh_mview.sh`, `run_is_index.sh`, `run_is_fk.sh`, `run_is_alt_tbl.sh`, or `run_is_con.sh`.

Exact block: `aexport` generated-file permissions

- Version scope: Altibase 8.1 verified source.
- `ALTIBASE_UT_FILE_PERMISSION` is the common permission variable for files generated by `aexport`, `iLoader`, and `iSQL`.
- `AEXPORT_FILE_PERMISSION` controls files generated by `aexport`.
- `AEXPORT_FILE_PERMISSION` takes priority over `ALTIBASE_UT_FILE_PERMISSION`.
- If `AEXPORT_FILE_PERMISSION` is not set, the documented default for `aexport`-generated files is `666`.
- Use `AEXPORT_FILE_PERMISSION=600` for owner-read/write-only output.

Exact block: `altiComp` `DIFF`, `SYNC`, and policy codes

- Version scope: Altibase 8.1 verified source.
- `altiComp` compares Altibase tables between two Altibase databases and is primarily used for replication inconsistency handling.
- `DIFF` identifies inconsistent records and writes result files; it does not synchronize data by itself.
- `SYNC` identifies inconsistent records and applies reconciliation according to configured synchronization policies.
- Difference classes: `MOSO` means same primary key exists on both sides but non-key values differ; `MOSX` means the row exists only in Master; `MXSO` means the row exists only in Slave.
- Policy codes: `SU` updates Slave from Master for `MOSO`; `SI` inserts Master-only rows into Slave for `MOSX`; `MI` inserts Slave-only rows into Master for `MXSO`; `SD` deletes Slave-only rows from Slave for `MXSO`.
- `MI` and `SD` are mutually exclusive and must not be configured together.

Exact block: `dataCompJ` fit, configuration, and artifacts

- Version scope: cross-version dataCompJ tool guidance; validate tool package compatibility with the target estate.
- Use `dataCompJ` when checking or resolving consistency in data replicated from Altibase to heterogeneous databases through `Adapter for Oracle` or `Adapter for JDBC`.
- Use `altiComp` for Altibase-to-Altibase comparison and synchronization.
- `dataCompJ` is a pure Java client application and depends on the Java Runtime Environment more than hardware or OS.
- Supply the configuration file with the required `-f dataCompJ_env_file_path` option.
- Required configuration sections include `Connections`, `Options`, and `TablePairs`.
- `DIFF` writes inconsistent records to CSV output; `SYNC` resolves inconsistencies according to configured policy.
- Build-stage failures for target-table validity or supported-data-type constraints are reported in `dataCompJ_report.txt`, and the tool does not proceed to the Run stage.
- Check `dataCompJ_report.txt`, `dataCompJ.log`, and `dataCompJ_data.log`; enable detailed data tracing carefully because `dataCompJ_data.log` can become large.

Exact block: `altierr` lookup forms

- Version scope: Altibase 8.1 verified source.
- `altierr` prints detailed explanations for Altibase server error codes and can search by error number or message keyword pattern.
- Altibase server logs errors in `ERR-{error number}` form, where the error number is hexadecimal.
- For `ERR-00015`, examples include `altierr 0x00015`, `altierr -w 00015`, and `altierr 21`.
- For SQLCODE or ODBC-return-code style negative integers, examples include `altierr -266286`, `altierr 266286`, and `altierr 0x4102E`.
- Keyword search uses `altierr -w keyword_pattern`, such as `altierr -w connect`.

Exact block: dump-family diagnostic dispatch

- Version scope: Altibase 8.1 verified source; use the installed utility version for binary format compatibility.
- Use `dumpbi` for backup information, `dumpct` for change tracking files, `dumpdb` for database files, `dumpddf` for disk datafile headers, `dumpla` for log anchor files, `dumplf` for log files, and `dumptrc` for trace-file conversion.
- Dump-family tools are offline diagnostic aids. Do not use their output alone to authorize recovery, deletion, `REUSE`, or file replacement without current version, log-anchor, datafile, backup, and archive-log evidence.

## Fast Decision Map

```mermaid
flowchart TD
  A[User request] --> B{Main task}
  B -- Logical Altibase migration --> C[aexport]
  B -- Altibase to Altibase consistency check --> D[altiComp DIFF]
  B -- Altibase to Altibase corrective sync --> E[altiComp SYNC]
  B -- Altibase to Oracle or MariaDB replicated data check --> F[dataCompJ DIFF]
  B -- Heterogeneous corrective sync --> G[dataCompJ SYNC]
  B -- Kubernetes StatefulSet pod lifecycle --> H[aku]
  B -- Server process control --> I[server or iSQL SYSDBA]
  B -- Monitoring daemon --> J[altiMon]
  B -- Audit log conversion --> K[altiAudit]
  B -- Error lookup --> L[altierr]
  B -- Profile analysis --> M[altiProfile]
  B -- Binary file or trace inspection --> N[dump-family tools]
  B -- Replication GUI management --> O[Replication Manager in 09_replication_ha_cdc.md]
```

## Version Differences

Version block: 7.1

- Core utility names and operational roles are stable for the utility families in this attachment.
- `aexport`, `altiComp`, `aku`, and the other Utilities Manual tools are documented in the Altibase 7.1 Utilities Manual.
- The 7.1 `aexport` section documents logical migration, generated scripts, SSL options, and `aexport.properties`; use the installed 7.1 client option list when a local binary differs from the examples here.
- `dataCompJ` is documented as a separate tool release and supports an Altibase master database at supported versions; validate tool package compatibility before using it in a 7.1 estate.

Version block: 7.3

- The 7.3 Utilities Manual explicitly documents the `DBMS_METADATA` package prerequisite for `aexport`.
- The 7.3 `aku` section includes StatefulSet operation, `aku.conf`, `AKU_*` properties, and pod start/end/clean behavior.
- The dataCompJ 7.2 release notes record Java runtime requirements, database compatibility, and bug fixes including clearer unsupported-DB JDBC URL handling and Log4j 2.17.1.

Version block: 8.1

- Use the wording `Altibase 8.1 verified source` for 8.1-specific statements.
- The 8.1 verified source keeps the same practical utility model: `aexport` for logical migration, `altiComp` for Altibase-to-Altibase comparison and synchronization, `aku` for Kubernetes StatefulSet lifecycle assistance, and dump-family tools for offline diagnostics.
- For exact behavior of less common options, prefer the installed 8.1 client help output and the Altibase 8.1 verified source.

## Standard Tool Block Format

Each utility block below uses the same fields:

- Purpose: what the utility does.
- When to Use: the operational scenario.
- Representative Command: compact syntax or a typical command.
- Key Inputs: files, properties, or configuration values the user must prepare.
- Cautions: high-risk behavior, version sensitivity, or common mistakes.
- Verification Method: how to confirm that the command worked or produced usable evidence.

## Tool Block: `aexport`

Purpose: `aexport` performs logical Altibase-to-Altibase migration. It extracts logical structures and data as text files and generates SQL and shell scripts that use iSQL and iLoader to recreate schema and load data on a destination database.

When to Use:

- Move data between Altibase versions or platforms.
- Recreate users, privileges, tablespaces, tables, constraints, indexes, views, materialized views, stored procedures, sequences, database links, replication objects, statistics, and related objects as supported by the source version.
- Build a script-driven logical migration when the source database can be running but should not be actively serving application workload.

Representative Command:

```bash
aexport -s source-host -port 20300 -u sys -p source_password \
  -tserver target-host -tport 21300 -nls_use UTF8
```

Compact syntax:

```text
aexport
  [-h]
  [-s server_name]
  [-u user_id]
  [-p password]
  [-port port_no]
  [-object owner.object]
  [-tserver target_server_name]
  [-tport target_port_no]
  [-nls_use charset]
  [-prefer_ipv6]
  [-ssl_ca CA_file_path | -ssl_capath CA_dir_path]
  [-ssl_cert certificate_file_path]
  [-ssl_key key_file_path]
  [-ssl_verify]
  [-ssl_cipher cipher_list]
```

Key Inputs:

- `ALTIBASE_HOME`: installation directory for the server or client package.
- `ALTIBASE_PORT_NO`: source server port, unless `-port` is supplied.
- `ALTIBASE_NLS_USE` or `-nls_use`: character set used for export/import text data.
- `$ALTIBASE_HOME/conf/aexport.properties`: required property file. Create it from `aexport.properties.sample` if it does not exist.
- `DBMS_METADATA` package: required by the Altibase 7.3 Utilities Manual and Altibase 8.1 verified source for DDL extraction.
- Source connection information: `-s`, `-port`, `-u`, `-p`.
- Destination connection information written into generated scripts: `-tserver`, `-tport`.
- `AEXPORT_FILE_PERMISSION`: set before generation when output files must be restricted, for example `export AEXPORT_FILE_PERMISSION=600`.

Cautions:

- Full DB mode is only available for `SYS`.
- A non-`SYS` user exports only that user's schema and needs `CREATE TABLE` privilege because `aexport` creates temporary tables for dependency analysis.
- Do not run multiple `aexport` processes concurrently against the same database; temporary table use can make results unpredictable.
- `run_is.sh` can drop existing users and objects on the destination depending on generated scripts and properties. Never run generated import scripts against the source database.
- If `-tserver` and `-tport` are omitted, generated scripts use the source server and port as the destination values.
- Set `NLS_USE` explicitly in non-`US7ASCII` environments to reduce character conversion and data-loss risk.
- `AEXPORT_FILE_PERMISSION` overrides `ALTIBASE_UT_FILE_PERMISSION` for `aexport` output. If neither is set, generated files can default to `666` permissions.
- Double-quote user or object names that contain lowercase letters, spaces, or special characters.
- `aexport` does not guarantee creation order for all stored procedures or materialized views. Some failed objects may need manual ordering and recreation.
- Sequence metadata is limited for non-`SYS` accounts; manually validate sequence attributes on the destination.

Verification Method:

- Before export: confirm `aexport.properties` exists and `DBMS_METADATA` is installed where required.
- After `aexport`: confirm expected SQL and shell scripts exist.
- After `run_il_out.sh`: confirm `.fmt`, `.dat`, `.log`, and `.bad` files were generated; inspect any nonempty `.bad` files.
- After `run_is.sh`: connect with iSQL and inspect users, tablespaces, objects, invalid objects, and errors from the script output.
- After `run_il_in.sh`: compare table row counts and inspect iLoader log and bad files.
- After final constraint/index/materialized-view scripts: validate indexes, foreign keys, triggers, materialized views, replication objects, and application smoke tests.

## `aexport` Modes And Generated Scripts

Tool block: Full DB mode

- Purpose: export the entire database logical structure and data.
- When to Use: version/platform migration or full logical rebuild.
- Representative Command: `aexport -s source-host -port 20300 -u sys -p source_password`.
- Key Inputs: `SYS` account, source/destination host and port, `aexport.properties`.
- Cautions: generated scripts can affect all users and objects on the destination.
- Verification Method: compare object counts by user, tablespace definitions, row counts, and invalid object lists.

Tool block: User mode

- Purpose: export objects owned by one user.
- When to Use: migrate or clone one schema.
- Representative Command: `aexport -s source-host -port 20300 -u app_user -p app_password`.
- Key Inputs: the owner account, or `SYS` exporting that owner.
- Cautions: role extraction is full DB mode only; tablespace creation in user mode depends on `CRT_TBS_USER_MODE`.
- Verification Method: compare schema objects, row counts, grants, constraints, indexes, and invalid objects for that user.

Tool block: Object mode

- Purpose: export a specific object or set of objects.
- When to Use: move or recreate one table, materialized view, view, or stored module.
- Representative Command: `aexport -s source-host -port 20300 -u sys -p source_password -object "APP"."T1"`.
- Key Inputs: fully qualified object names.
- Cautions: all specified objects must belong to the same user unless exporting as `SYS`; `DROP` statements are not generated in object mode.
- Verification Method: validate the specific object DDL, dependent objects, row counts if table data was included, and object validity.

Generated script block:

- `run_il_out.sh`: uses iLoader to export table data from the source database.
- `run_il_in.sh`: uses iLoader to import table data into the destination database.
- `run_is.sh`: creates schema on the destination database.
- `run_is_con.sh`: creates constraints and related objects when `TWO_PHASE_SCRIPT=ON`.
- `run_is_index.sh`: creates indexes when generated separately.
- `run_is_fk.sh`: creates foreign keys and triggers when generated separately.
- `run_is_repl.sh`: creates replication objects when generated separately.
- `run_is_refresh_mview.sh`: refreshes materialized views when generated.
- `run_is_alt_tbl.sh`: switches table and partition data access mode when generated.

Standard migration cookbook:

```bash
# 1. Generate export/import scripts from the source database.
aexport -s source-host -port 20300 -u sys -p source_password \
  -tserver target-host -tport 21300 -nls_use UTF8

# 2. Export table data from the source database.
sh run_il_out.sh

# 3. Copy generated SQL, shell, .fmt, .dat, .log, and .bad files to the target host if needed.

# 4. Create schema on the destination database.
sh run_is.sh

# 5. Load data into the destination database.
sh run_il_in.sh

# 6. Finish post-load objects.
sh run_is_refresh_mview.sh
sh run_is_index.sh
sh run_is_fk.sh
# If replication objects are in scope and endpoint/topology review is complete:
sh run_is_repl.sh
sh run_is_alt_tbl.sh
```

If `TWO_PHASE_SCRIPT=OFF`, run `run_is_repl.sh` only when replication objects are in scope and the target host, port, and replication topology have been reviewed; otherwise record that replication DDL was intentionally skipped. If `TWO_PHASE_SCRIPT=ON`, run `run_is_con.sh` instead of the separate post-load scripts because it includes the indexes, foreign keys, triggers, and replication object creation bundle. Verify replication endpoints before executing generated replication DDL.

## `aexport.properties` Searchable Blocks

Property block: `OPERATION`

- Values: `IN`, `OUT`.
- Use `OUT` to generate schema and data export scripts. Use `IN` to execute previously generated schema/data loading scripts.

Property block: `EXECUTE`

- Values: `ON`, `OFF`.
- `ON` runs the generated scripts automatically for the selected `OPERATION`. `OFF` generates scripts without running them.

Property block: `INVALID_SCRIPT`

- Values: `ON`, `OFF`.
- Controls whether invalid object creation scripts are grouped into `INVALID.sql`.

Property block: `TWO_PHASE_SCRIPT`

- Values: `ON`, `OFF`.
- `ON` groups object creation into two SQL scripts and creates `run_is.sh` and `run_is_con.sh`.

Property block: `CRT_TBS_USER_MODE`

- Values: `ON`, `OFF`.
- Controls whether user-mode exports include statements for tablespaces related to the exported user.

Property block: `INDEX`

- Values: `ON`, `OFF`.
- Controls separate index creation when `TWO_PHASE_SCRIPT=OFF`.

Property block: `USER_PASSWORD`

- Value: password to use when exported users are created on the destination.
- If omitted, `aexport` prompts for each user password.

Property block: `VIEW_FORCE`

- Values: `ON`, `OFF`.
- Allows views to be created even when underlying objects do not yet exist.

Property block: `DROP`

- Values: `ON`, `OFF`.
- Adds `DROP` statements for existing destination objects when supported. Use with caution.

Property block: generated script file names

- `ILOADER_OUT`: default-style output script such as `run_il_out.sh`.
- `ILOADER_IN`: import script such as `run_il_in.sh`.
- `ISQL`: schema creation script such as `run_is.sh`.
- `ISQL_CON`: constraint script such as `run_is_con.sh`.
- `ISQL_INDEX`: index script such as `run_is_index.sh`.
- `ISQL_FOREIGN_KEY`: foreign key script such as `run_is_fk.sh`.
- `ISQL_REPL`: replication script such as `run_is_repl.sh`.
- `ISQL_REFERSH_MVIEW`: materialized-view refresh script name as documented by the utility property.
- `ISQL_ALT_TBL`: table data-access-mode switch script such as `run_is_alt_tbl.sh`.

Property block: iLoader behavior

- `ILOADER_FIELD_TERM`: field delimiter for generated iLoader commands.
- `ILOADER_ROW_TERM`: row delimiter for generated iLoader commands.
- `ILOADER_PARTITION`: controls partition-specific iLoader scripts.
- `ILOADER_ERRORS`: maximum allowed load errors.
- `ILOADER_ARRAY`: rows processed at once.
- `ILOADER_COMMIT`: rows per commit during upload.
- `ILOADER_PARALLEL`: iLoader parallelism.
- `ILOADER_ASYNC_PREFETCH`: `OFF`, `ON`, or `AUTO` asynchronous prefetch behavior during export.

Property block: `COLLECT_DBMS_STATS`

- Values: `ON`, `OFF`.
- Controls export of table, column, and index statistics.

Property block: SSL destination settings

- `SSL_ENABLE`: enables SSL-related options in generated iSQL and iLoader scripts.
- Related properties include `SSL_CA`, `SSL_CAPATH`, `SSL_CERT`, `SSL_KEY`, `SSL_CIPHER`, and `SSL_VERIFY`.

## Tool Block: `altiComp`

Purpose: `altiComp` compares data between two Altibase databases and can synchronize inconsistent records according to configured policies. It is commonly used to validate and repair data consistency in Altibase replication environments.

When to Use:

- Compare replicated Altibase tables after replication lag, outage, failover, or maintenance.
- Produce difference logs for table-by-table investigation.
- Correct differences between two Altibase databases when the master/slave direction and policies are explicitly approved.

Representative Command:

```bash
altiComp -f sample.cfg
```

Key Inputs:

- An altiComp environment file such as `sample.cfg`.
- `DB_MASTER`: reference database connection string.
- `DB_SLAVE`: database to compare and, depending on policies, correct.
- `OPERATION`: `DIFF` or `SYNC`.
- Synchronization policy properties: `INSERT_TO_SLAVE`, `INSERT_TO_MASTER`, `DELETE_IN_SLAVE`, `UPDATE_TO_SLAVE`.
- Workload properties: `MAX_THREAD`, `CHECK_INTERVAL`, `COUNT_TO_COMMIT`, `FILE_MODE_MAX_ARRAY`.
- One or more table groups with `TABLE`, `SCHEMA`, `WHERE`, and `EXCLUDE`.

Cautions:

- `DB_MASTER` is the reference database for most sync policies. Confirm which system is authoritative before `SYNC`.
- `INSERT_TO_MASTER` and `DELETE_IN_SLAVE` are mutually exclusive.
- `WHERE` filters and `EXCLUDE` columns change the meaning of equality; document them in the run record.
- LOB column values are not printed in result files.
- `FILE_MODE_MAX_ARRAY` is only for Altibase-to-Altibase use and may not improve performance when many LOB columns exist.
- Run `DIFF` first, review results, then run `SYNC` only with an approved policy.

Verification Method:

- For `DIFF`, inspect `script_file_name.log` and each table result file.
- For `SYNC`, inspect try/fail counts, error details, and rerun `DIFF` to confirm `MOSO`, `MOSX`, and `MXSO` differences are zero or expected.
- Compare row counts and representative checksums where feasible.

## `altiComp` Inconsistency And Policy Map

```mermaid
flowchart TD
  A[Compare rows by primary key] --> B{Difference type}
  B -- Same PK exists on both sides, non-PK values differ --> C[MOSO]
  B -- Row exists only in Master DB --> D[MOSX]
  B -- Row exists only in Slave DB --> E[MXSO]
  C --> F[UPDATE_TO_SLAVE = SU policy]
  D --> G[INSERT_TO_SLAVE = SI policy]
  E --> H[INSERT_TO_MASTER = MI policy]
  E --> I[DELETE_IN_SLAVE = SD policy]
  H -. mutually exclusive .- I
```

Configuration skeleton:

```text
DB_MASTER = "altibase://sys:master_password@DSN=master-host;PORT_NO=20300;NLS_USE=UTF8"
DB_SLAVE  = "altibase://sys:slave_password@DSN=slave-host;PORT_NO=20300;NLS_USE=UTF8"
OPERATION = DIFF
MAX_THREAD = -1

DELETE_IN_SLAVE = OFF
INSERT_TO_SLAVE = ON
INSERT_TO_MASTER = OFF
UPDATE_TO_SLAVE = ON

LOG_DIR = "./"
LOG_FILE = "sample.log"

[EMP]
TABLE = EMP
SCHEMA = SYS
WHERE = {ENO >= 1 and ENO <= 1000}
EXCLUDE = {UPDATED_AT}
```

Cookbook: run a non-corrective comparison

```bash
altiComp -f sample.cfg
```

Use when: the user needs to see whether replicated tables differ.

Verification:

- `sample.log` contains fetched row counts and `MOSO`, `MOSX`, `MXSO` counts.
- Per-table logs contain detailed difference records.

Cookbook: run corrective synchronization

```text
OPERATION = SYNC
INSERT_TO_SLAVE = ON
UPDATE_TO_SLAVE = ON
INSERT_TO_MASTER = OFF
DELETE_IN_SLAVE = OFF
```

```bash
altiComp -f sample.cfg
```

Use when: Master DB is confirmed authoritative and slave rows should be inserted or updated from the master.

Verification:

- `Try` and `Fail` counts in the sync log are reviewed.
- A follow-up `DIFF` run shows no unexpected differences.

## `altiComp` Output Evidence Blocks

Output block: DIFF summary log

- File pattern: `script_file_name.log`.
- Contains the executed environment-file content and one summary for each `TABLES` group.
- High-value fields:
  - `Fetch Rec In Master`: fetched row count from the master database.
  - `Fetch Rec In Slave`: fetched row count from the slave database.
  - `MOSX = DF, Count`: rows found only in the master database.
  - `MXSO = DF, Count`: rows found only in the slave database.
  - `MOSO = DF, Count`: rows with the same primary key but different compared values.
  - `MOSO = EQ, Count`: rows with the same primary key and matching compared values.
  - `SCAN TPS` and `Time`: scan throughput and elapsed time for the comparison.

Output block: DIFF per-table result file

- File pattern: `master_table-user_name.slave_table.log`.
- Record format:

```text
DF[m,n]-> COL_N (Vn_M, Vn_S):PK->{ PCOL_V }
```

- `DF`: difference class, such as `MOSX`, `MOSO`, or `MXSO`.
- `m`: master-side record order in the comparison stream.
- `n`: slave-side record order in the comparison stream.
- `COL_N`: first compared column that differs.
- `Vn_M`: master-side value for the differing column.
- `Vn_S`: slave-side value for the differing column.
- `PCOL_V`: primary-key value used to identify the record.
- Caution: LOB column values are not recorded in the result file.

Output block: SYNC summary log

- File pattern: `script_file_name.log`.
- Contains the executed environment-file content, synchronization policy summary, and one summary for each `TABLES` group.
- Policy values include `SI` for insert-to-slave, `SU` for update-to-slave, and disabled policy markers where no corrective action is configured.
- High-value fields:
  - `Operation`: corrective action such as `INSERT`, `UPDATE`, or `DELETE`.
  - `Try`: number of corrective attempts.
  - `Fail`: number of failed corrective attempts.
  - `OOP TPS`: out-of-place operation throughput for corrective work.
  - `SCAN TPS`: comparison scan throughput.
- If failures exist, preserve the error log and failed record detail, then rerun `DIFF` after fixing the root cause.

## Tool Block: `dataCompJ`

Purpose: `dataCompJ` is a Java CLI tool for comparing Altibase data with a heterogeneous slave database and optionally synchronizing the slave database according to configured policies.

When to Use:

- Validate data replicated from Altibase to Oracle or MariaDB through Altibase Adapter for Oracle or Adapter for JDBC.
- Compare data table-by-table when JDBC drivers are available for both databases.
- Synchronize slave-side differences back to the Altibase master baseline when the configured policy allows it.

Representative Command:

```bash
dataCompJCli.sh -f dataCompJ.xml
```

Key Inputs:

- Java Runtime Environment 8 or higher and `JAVA_HOME` pointing to the installed Java path.
- `dataCompJ.xml` or another XML configuration file.
- JDBC URL, JDBC driver path, user ID, password, `FetchSize`, and `BatchSize` for `<MasterDB>` and `<SlaveDB>`.
- `<Operation>`: `DIFF` or `SYNC`.
- `<FileEncoding>`: encoding for generated files.
- `<Diff><DirPath>`: output directory for DIFF CSV files.
- `<Sync>` policy elements: `<MOSO UPDATE_TO_SLAVE="true"/>`, `<MOSX INSERT_TO_SLAVE="true"/>`, `<MXSO DELETE_FROM_SLAVE="true"/>`.
- `<Log><DirPath>` and `<TraceInconsistentRecord>`.
- `<MaxThread>`: `0` uses the CPU core count.
- `<TablePairs>`: one or more `<TablePair>` entries or `<TableNameFilePath>`.

Cautions:

- The master database is Altibase. The documented slave databases are Oracle and MariaDB.
- Documented compatibility bounds are Master DB Altibase 5.3.3 or later, Slave DB Oracle 9i or later, and Slave DB MariaDB 5.5.x or later.
- Target tables must have compatible column names, column order, data types, and primary keys.
- At least one comparable non-primary-key column must remain after unsupported data types and `<Exclude>` columns are removed.
- Unsupported binary and LOB-type columns are excluded or cause build-phase errors depending on whether both sides are unsupported and compatible.
- If a data type pair is technically comparable but not equivalent, all rows can appear inconsistent at run time.
- `<TraceInconsistentRecord>true</TraceInconsistentRecord>` can create a very large `dataCompJ_data.log` and degrade performance.
- `SYNC` applies changes to the slave database. Run `DIFF` first and review the report before using `SYNC`.

Verification Method:

- Build phase completes with zero problematic tables in `dataCompJ_report.txt`.
- Run phase report shows expected fetched row counts and `MOSO`, `MOSX`, `MXSO` counts.
- For DIFF, inspect generated CSV files in `<Diff><DirPath>`.
- For SYNC, rerun DIFF and confirm differences are resolved.
- Inspect `dataCompJ.log` for program events and `dataCompJ_data.log` only when detailed inconsistent-record tracing is enabled.

Configuration skeleton:

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<dataCompJ>
  <Connections>
    <MasterDB>
      <JdbcUrl>jdbc:Altibase://master-host:20300/mydb</JdbcUrl>
      <JdbcFilePath>./jdbc/Altibase.jar</JdbcFilePath>
      <UserId>sys</UserId>
      <Password>master_password</Password>
      <FetchSize>1000</FetchSize>
      <BatchSize>1000</BatchSize>
    </MasterDB>
    <SlaveDB>
      <JdbcUrl>jdbc:oracle:thin:@//slave-host:1521/service_name</JdbcUrl>
      <JdbcFilePath>./jdbc/ojdbc.jar</JdbcFilePath>
      <UserId>app_user</UserId>
      <Password>slave_password</Password>
      <FetchSize>1000</FetchSize>
      <BatchSize>1000</BatchSize>
    </SlaveDB>
  </Connections>
  <Options>
    <Operation>DIFF</Operation>
    <FileEncoding>UTF-8</FileEncoding>
    <Diff>
      <DirPath>./diff/</DirPath>
    </Diff>
    <Sync>
      <MOSO UPDATE_TO_SLAVE="true"/>
      <MOSX INSERT_TO_SLAVE="true"/>
      <MXSO DELETE_FROM_SLAVE="true"/>
    </Sync>
    <Log>
      <DirPath>./</DirPath>
      <TraceInconsistentRecord>false</TraceInconsistentRecord>
    </Log>
    <MaxThread>0</MaxThread>
  </Options>
  <TablePairs>
    <TablePair>
      <MasterTable>SYS.EX1</MasterTable>
      <SlaveTable>APP.EX1</SlaveTable>
      <Exclude>UPDATED_AT</Exclude>
      <Where>C1 &gt; 5</Where>
    </TablePair>
  </TablePairs>
</dataCompJ>
```

DIFF output files:

- `SchemaName.TableName_MASTER_diff.csv`: master-side rows for `MOSO` differences.
- `SchemaName.TableName_SLAVE_diff.csv`: slave-side rows for `MOSO` differences.
- `SchemaName.TableName_MASTER_only.csv`: rows present only in the master table (`MOSX`).
- `SchemaName.TableName_SLAVE_only.csv`: rows present only in the slave table (`MXSO`).

## `dataCompJ` Report Interpretation Blocks

Output block: generated files

- `dataCompJ_report.txt`: text report summarizing build and run results.
- `dataCompJ.log`: program event log for detailed execution history.
- `dataCompJ_data.log`: run-phase data-event log written when `<TraceInconsistentRecord>true</TraceInconsistentRecord>` is configured.
- Caution: `dataCompJ_data.log` can become very large and slow the tool when many inconsistent records exist.

Output block: Build section in `dataCompJ_report.txt`

- `Started`, `Finished`, `Elapsed`: build-phase timing.
- `[ User input information ]`: effective user-provided configuration summary.
- `[ Problematic table(s): n ]`: table pairs rejected during build validation.
- `[ Candidate table(s) for data comparison: n ]`: table pairs accepted for the run phase.
- Per-candidate details:
  - `SELECT SQL`: query generated for the master table comparison stream.
  - `Excluded columns`: columns excluded by configuration or unsupported comparison.
  - `Where condition`: selection predicate applied to both sides.
  - `N/A data type columns`: columns excluded because the data type is not supported for comparison, for example `CLOB`.

Output block: DIFF Run section in `dataCompJ_report.txt`

- `Fetched record count from MASTER`: master-side row count read for the table pair.
- `Fetched record count from SLAVE`: slave-side row count read for the table pair.
- `MOSO Matched`: rows with matching primary key and matching compared values.
- `MOSO Diff`: rows with matching primary key and different compared values.
- `MOSX Master only`: rows present only in the master table.
- `MXSO Slave only`: rows present only in the slave table.
- For `MOSO` differences, compare `SchemaName.TableName_MASTER_diff.csv` and `SchemaName.TableName_SLAVE_diff.csv`; the files store corresponding records in the same order.

Output block: SYNC Run section in `dataCompJ_report.txt`

- `Type`: difference class, such as `MOSO`, `MOSX`, or `MXSO`.
- `Resolution`: configured corrective action such as `UPDATE TO SLAVE`, `INSERT TO SLAVE`, or `DELETE FROM SLAVE`.
- `Try`: number of attempted corrective operations.
- `Fail`: number of failed corrective operations.
- Verification: after `SYNC`, rerun `DIFF` on the same `TablePair` and confirm `MOSO Diff`, `MOSX Master only`, and `MXSO Slave only` are zero or match the approved residual list.

Data type compatibility summary:

- Altibase to Oracle: common numeric types map to `NUMBER`; `FLOAT` maps to `FLOAT`; `DATE` maps to `DATE` or `TIMESTAMP`; `CHAR`, `VARCHAR`, `NCHAR`, and `NVARCHAR` map to Oracle character equivalents.
- Altibase to MariaDB: common integer and decimal types map to corresponding MariaDB numeric types; `REAL` maps to `FLOAT`; `DOUBLE` maps to `DOUBLE`; Altibase `FLOAT` has no direct documented MariaDB equivalent; `DATE` maps to `DATE`, `DATETIME`, or `TIMESTAMP`; character types map to MariaDB character/text equivalents.

## Tool Block: `aku`

Purpose: `aku` is the Altibase Kubernetes Utility. It helps coordinate Altibase data synchronization and replication metadata during Kubernetes StatefulSet pod start and termination.

When to Use:

- Start a new pod with the same data as an existing Altibase pod in a StatefulSet.
- Terminate a pod cleanly and reset replication information.
- Inspect or clean replication objects created by `aku`.

Representative Commands:

```bash
aku -i
aku -p start
aku -p end
aku -p clean
```

Compact syntax:

```text
aku
  [-h | --help]
  [-v | --version]
  [-i | --info]
  [-p start | -p end | -p clean]
  [--pod start | --pod end | --pod clean]
```

Key Inputs:

- `$ALTIBASE_HOME` and `$ALTIBASE_HOME/bin` in `PATH`.
- `$ALTIBASE_HOME/conf/aku.conf`, created from `aku.conf.sample`.
- Kubernetes values: `AKU_STS_NAME`, `AKU_SVC_NAME`, `AKU_SERVER_COUNT`.
- Database values: `AKU_SYS_PASSWORD`, `AKU_PORT_NO`, `AKU_REPLICATION_PORT_NO`.
- Startup/end behavior: `AKU_ADDRESS_CHECK_COUNT`, `AKU_FLUSH_AT_START`, `AKU_FLUSH_TIMEOUT_AT_START`, `AKU_DELAY_START_COMPLETE_TIME`, `AKU_FLUSH_AT_END`, `AKU_REPLICATION_RESET_AT_END`.
- Replication target groups under `REPLICATIONS`, including `REPLICATION_NAME_PREFIX`, `SYNC_PARALLEL_COUNT`, and table or partition targets.

Cautions:

- `aku` supports replication among pods. It does not provide Altibase data scale-out.
- Use only with Kubernetes StatefulSets and the `OrderedReady` pod management policy.
- The documented maximum number of scalable replicas is 6.
- `Altibase Server` and `aku` must run in the same container.
- Use the same `aku` version and identical `aku.conf` values across pods.
- Set Altibase properties `ADMIN_MODE=1` and `REMOTE_SYSDBA_ENABLE=1` as required by the utility procedure.
- Run `aku -p start` only after the Altibase server has started successfully.
- Configure a Kubernetes Startup Probe so multiple pods do not run `aku -p start` simultaneously. The `/tmp/aku_start_completed` file can be used as the completion indicator.
- Set `publishNotReadyAddresses: true` for the Kubernetes service.
- Run `aku -p end` before stopping the Altibase server, and set `terminationGracePeriodSeconds` high enough for `aku -p end` to finish.
- Do not manually create, drop, or modify replication objects created by `aku`.
- `aku -p clean` deletes all Altibase replication objects created by `aku` and removes `/tmp/aku_start_completed`; use it only when synchronization is no longer required.

Verification Method:

- `aku -i` shows the configured server, replication objects, and replication targets.
- Successful `aku -p start` output ends with `AKU run successfully.` and creates `/tmp/aku_start_completed`.
- Successful `aku -p end` flushes/stops/resets replication as configured and deletes `/tmp/aku_start_completed`.
- Query `SYSTEM_.SYS_REPLICATIONS_` to check replication names and `XSN` state when troubleshooting.

## `aku` Lifecycle Flow

```mermaid
flowchart TD
  A[Pod starts Altibase] --> B[Run aku -p start]
  B --> C{Pod number}
  C -- pod-0 --> D[Initialize master-side replication]
  C -- pod-1..N --> E[Join and synchronize slave Pod]
  D --> F[Mark AKU start completed]
  E --> F
  F --> G[Pod serves workload]
  G --> H[Run aku -p end before termination]
  H --> I[Flush, stop, reset, and clean up as configured]
  I --> J[Stop Altibase and terminate pod]
```

Lifecycle phase details:

1. On pod 0, `aku -p start` creates AKU-managed replication objects and starts replication for connected Pods.
2. On pod 1 through pod N, `aku -p start` connects to existing Pods, creates or reuses replication objects, truncates replication target tables when needed, synchronizes from the master Pod, and starts replication.
3. A successful start sets `ADMIN_MODE` to allow access and creates `/tmp/aku_start_completed`.
4. Before termination, `aku -p end` flushes replication, stops and resets replication if configured, deletes `/tmp/aku_start_completed`, and then Altibase can stop.

Troubleshooting block: unreset replication information

- Symptom: a pod was force-terminated before `aku -p end` completed, or `AKU_REPLICATION_RESET_AT_END=0` left replication information initialized.
- Risk: online log files needed for replication to the terminated pod can accumulate and exhaust disk space.
- Check:

```sql
SELECT REPLICATION_NAME, XSN FROM SYSTEM_.SYS_REPLICATIONS_;
```

- If a replication object should be reset but `XSN` is not `-1`, stop and reset the replication object after confirming the target topology:

```sql
ALTER REPLICATION replication_name STOP;
ALTER REPLICATION replication_name RESET;
```

## Tool Block: `altiAudit`

Purpose: converts binary Altibase audit log files into readable text or CSV output.

When to Use: audit review, security investigation, or support evidence collection for audited SQL activity.

Representative Command:

```bash
altiAudit $ALTIBASE_HOME/trc/alti-1366989680-0.aud
altiAudit -s $ALTIBASE_HOME/trc/alti-1366989680-0.aud
```

Key Inputs:

- Audit log file from `$ALTIBASE_HOME/trc` or the directory configured by `AUDIT_LOG_DIR`.
- `-s` for CSV output.

Cautions:

- Output can include user names, client IPs, SQL text, execution result, timing, and row counts. Treat it as sensitive.
- Confirm the audit log belongs to the target server and time window.

Verification Method:

- Text output contains sections such as `Session Info`, `Query Info`, `Query Elapsed Time`, and `SQL`.
- CSV output is comma-separated and suitable for spreadsheet or log ingestion.

## Tool Block: `altibase`

Purpose: executable server binary for Altibase services.

When to Use:

- `altibase -v`: check installed binary version.
- `altibase -n`: run the server in the foreground for debugging.

Representative Command:

```bash
altibase -v
altibase -n
```

Key Inputs:

- Correct Altibase environment and binary path.

Cautions:

- Do not use `altibase -n` as a normal production startup method.
- For routine startup/shutdown, use iSQL in `SYSDBA` mode or the `server` script.

Verification Method:

- `altibase -v` prints installed version information without starting the server.
- Foreground execution should be used only in a controlled debug session.

## Tool Block: `altiMon`

Purpose: `altimon.sh` monitors the Altibase server process and host system and writes collected metrics and alerts to log files.

When to Use:

- Continuous monitoring of database and OS metrics.
- Alert action scripts based on thresholds.
- CSV group metrics for trend analysis.

Representative Command:

```bash
altimon.sh start
altimon.sh stop
```

Key Inputs:

- Java 8 or higher, with bitness compatible with the PICL C library.
- `$ALTIBASE_HOME/altiMon/conf/config.xml`.
- `$ALTIBASE_HOME/altiMon/conf/Metrics.xml`.
- `$ALTIBASE_HOME/altiMon/conf/GroupMetrics.xml`.
- Optional action scripts in `$ALTIBASE_HOME/altiMon/action_scripts`.

Cautions:

- If no compatible PICL library exists for OS metrics, configure `monitorOsMetric="false"`.
- The password element may be stored and then encrypted by altiMon; still protect configuration file permissions.
- Custom command metrics execute commands or scripts, so review them as operational code.

Verification Method:

- Check `$ALTIBASE_HOME/altiMon/logs/altimon.log` after `start`.
- Confirm metric logs such as `OsMetrics.log`, `[SQLMetric_Name].log`, `[GroupMetric_Name].csv`, `alert.log`, and `report.html`.
- Confirm archive and CSV backup behavior if metric definitions change.

## Tool Block: `altierr`

Purpose: searches Altibase error messages by code or keyword and prints the detailed description, cause, and action.

When to Use:

- Decode `ERR-xxxxx` values from logs.
- Search for errors by phrase.
- Translate application `SQLCODE` or ODBC negative error numbers into Altibase details.

Representative Command:

```bash
altierr 0x00015
altierr -266286
altierr 266286
altierr 0x4102E
altierr -n 0x4102E
altierr -w connect
```

Compact syntax:

```text
altierr {-w keyword_pattern | [-n] error_number}
Source syntax wording: altierr {-w keyword pattern | [-n] error number}
```

Key Inputs:

- Hexadecimal, positive decimal, or negative decimal error number.
- `-n` means search by error number; when searching by error number, `-n` can be omitted.
- Negative integer values can come from application `SQLCODE` variables or ODBC function return codes, for example `-266286`.
- Keyword pattern with `-w`.

Cautions:

- Keyword searches can return multiple records; ask for the exact error code when possible.
- Keep the error code literal in multilingual answers.
- Preserve equivalent forms together when known, for example `0x4102E (266286)` and application return code `-266286`.

Verification Method:

- Output includes the matching error code, message, cause, and action.

## Tool Block: `altipasswd`

Purpose: updates `$ALTIBASE_HOME/conf/syspassword`, which is used to verify the `SYS` user password for `SYSDBA` operations when the database is not in service.

When to Use:

- After changing `SYS` password with `ALTER USER`, update `syspassword` so `SYSDBA` startup/shutdown continues to work.

Representative Command:

```bash
altipasswd
```

Key Inputs:

- Previous `SYS` password.
- New `SYS` password.

Cautions:

- If the database `SYS` password and `syspassword` do not match, `SYSDBA` tasks such as startup and shutdown can fail.
- Protect shell history and terminal capture when changing privileged passwords.

Verification Method:

- Start iSQL as `SYSDBA` and confirm the expected administrative connection works.

## Tool Block: `altiProfile`

Purpose: converts Altibase profile files into readable form and can produce SQL statement statistics in text and CSV formats.

When to Use:

- Analyze query execution information from profile files.
- Rank SQL by `TOTAL`, `AVG`, `COUNT`, success, and failure statistics.
- Inspect profile sections such as `[STATEMENT]`, `[PLAN]`, `[BIND]`, `[SESSION STAT]`, `[SYSTEM STAT]`, and `[MEMORY STAT]`.

Representative Command:

```bash
altiProfile $ALTIBASE_HOME/trc/alti-1286503704-0.prof
altiProfile -stat query $ALTIBASE_HOME/trc/*.prof
altiProfile -stat session $ALTIBASE_HOME/trc/*.prof
```

Compact syntax:

```text
altiProfile [-h] [-stat query|session] profile_name [profile_name2 ...]
```

Key Inputs:

- Profile files in `$ALTIBASE_HOME/trc`.
- Server properties for profile generation:
  - `QUERY_PROF_FLAG`: enables selected profile sections.
  - `TIMED_STATISTICS=1`: required for proper elapsed time output.

Cautions:

- Profiling can grow files rapidly and fill disk. Enable only for a planned window.
- `QUERY_PROF_FLAG` values are additive: `1` statement, `2` bind, `4` plan, `8` session stat, `16` system stat, `32` memory stat.

Verification Method:

- Conversion output is readable text.
- `-stat query` or `-stat session` writes files like `alti-prof-stat-<time>.txt` and `alti-prof-stat-<time>.csv`.

## Tool Block: `altiwrap`

Purpose: encrypts persistent stored module source code so procedure, function, typeset, package, and package body code is not exposed as plain text.

When to Use:

- Distribute PSM code while hiding implementation details.

Representative Command:

```bash
altiwrap --iname sample1.sql --oname sample1.plb
```

Compact syntax:

```text
altiwrap {--iname input_file} [--oname output_file]
```

Key Inputs:

- Input SQL file. If the extension is omitted, `.sql` is assumed.
- Output wrapped file. If the extension is omitted, `.plb` is assumed.

Cautions:

- Wrapped code cannot be modified directly. Change the original source and wrap again.
- Triggers cannot be encrypted by `altiwrap`.
- Encrypted code cannot be checked for syntax and semantic errors before execution in the same way as plain source.

Verification Method:

- Run the wrapped `.plb` file in iSQL and confirm the object is created successfully.
- Execute a small procedure/function call when safe.

## Tool Block: `awrite`

Purpose: compares response time for system calls used to create or expand log files.

When to Use:

- Evaluate which log creation method may be appropriate for the `LOG_CREATE_METHOD` property.

Representative Command:

```bash
awrite
```

Key Inputs:

- Host filesystem where Altibase log files will be created.

Cautions:

- Run on the target storage class during a maintenance or test window because it writes test data.
- Do not infer database workload performance from this utility alone; it measures specific file expansion calls.

Verification Method:

- Output shows elapsed time for `fallocate` and `write` expansion methods.

## Tool Block: `checkServer`

Purpose: monitors the Altibase process and runs a user-specified script if Altibase terminates unexpectedly.

When to Use:

- Simple process watchdog behavior for restart automation.

Representative Command:

```bash
checkServer -f restart.sh &
checkServer -n -f restart.sh
```

Compact syntax:

```text
checkServer [-n] {-f server_restart_script_file}
```

Key Inputs:

- Restart script, commonly:

```bash
#!/bin/sh
${ALTIBASE_HOME}/bin/server start
```

Cautions:

- `checkServer` executes the restart script only when Altibase terminates without `server stop`.
- `checkServer.pid` and `checkServer.log` are created in `$ALTIBASE_HOME/trc`.
- If `checkServer` is killed abnormally, a stale `checkServer.pid` can block restart of `checkServer`.
- Use `killCheckServer` for normal termination.

Verification Method:

- Confirm `$ALTIBASE_HOME/trc/checkServer.log` records watchdog activity.
- Confirm no stale `$ALTIBASE_HOME/trc/checkServer.pid` remains after normal termination.

## Tool Block: `killCheckServer`

Purpose: terminates a running `checkServer` utility.

When to Use:

- Stop the watchdog before planned server stop or operational maintenance.

Representative Command:

```bash
killCheckServer
```

Key Inputs:

- Running `checkServer` process and its PID file.

Cautions:

- `server stop` and `server kill` may call this utility before terminating the Altibase instance.
- If run manually, results might not be recorded in `killCheckServer.log`.

Verification Method:

- `checkServer killed.` appears when the process is running.
- `ERROR CODE : -27` can appear when `checkServer` is not running.

## Tool Block: `server`

Purpose: shell script that wraps common Altibase create, startup, shutdown, restart, kill, status, and role-manager operations.

When to Use:

- Routine DBA server control from the operating system account that owns Altibase.

Representative Command:

```bash
server start
server restart
server stop
server status
server kill
server create UTF8 UTF16
server startRoleManager
server stopRoleManager
```

Compact syntax:

```text
server {start | stop | restart | kill | status | create db_charset national_charset | startRoleManager | stopRoleManager}
```

Key Inputs:

- Correct Altibase environment variables and owner account.
- Database and national character sets when using `server create`.

Cautions:

- Prefer graceful `server stop` or iSQL `SHUTDOWN NORMAL` for planned shutdowns.
- `server kill` is forceful and should be reserved for failure cases with an approved recovery plan.
- `server create` creates a database using the supplied character sets; confirm this is a new intended database operation.

Verification Method:

- `server status` confirms process state.
- iSQL connection and a simple query confirm service state after start.
- Review `$ALTIBASE_HOME/trc/altibase_boot.log` after startup or shutdown.

## Dump-Family Diagnostic Tools

The dump-family tools convert binary Altibase internal files into readable text for diagnostics. They are usually evidence-gathering tools, not normal data access tools. Keep outputs version-matched with the Altibase binary and share them with support when investigating recovery, storage, log, or crash issues.

## Dump-Family Output Evidence Map

Use this map when a customer pastes dump output and asks what fields matter. Do not treat dump output as current live state unless the file source, copy time, Altibase version, and server status are known.

Output block: `dumpbi`

- Sections: `[BACKUP INFO FILE HDR]`, `[BACKUP INFO SLOT]`.
- High-value fields:
  - `Backup info slot count`: number of stored backup slots.
  - `Last backup LSN`: most recent backup LSN and backupInfo validity clue.
  - `Database name`: database name recorded in the file.
  - `Begin backup time`, `End backup time`: backup window.
  - `Backup target`: `DATABASE` or `TABLESPACE`.
  - `Backup level`: `level 0` or `level 1`.
  - `Backup Type`: full, differential, or cumulative.
  - `Tablespace ID`, `File ID`, `Backup Tag`, `Backup file name`: identify the backed-up scope and artifact.

Output block: `dumpct`

- Sections: `[CHANGE TRACKING FILE HDR]`, `[CHANGE TRACKING FILE BODY]`.
- High-value fields:
  - `Change tracking body count`: number of body areas in the changeTracking file.
  - `Incremental backup chunk size`: `INCREMENTAL_BACKUP_CHUNK_SIZE` at creation time.
  - `Last flush LSN` or `Flush LSN`: LSN when changed memory data was flushed to the file.
  - `Database name`: database name recorded in the file.
  - `Datafile descriptor slot` and `Slot ID`: link change-tracking body detail to datafile descriptors.

Output block: `dumpdb`

- Use `dumpdb -j 7 -f file_name` for memory tablespace incremental-backup metadata.
- High-value fields for incremental backup output:
  - `Binary DB Version`: version of the data file.
  - `Redo LSN`: redo point for media recovery.
  - `Create LSN`: checkpoint image creation LSN.
  - `DataFileDescSlot ID`: changeTracking descriptor slot tied to the memory checkpoint image.

Output block: `dumpddf`

- Header fields:
  - `Binary DB Version`: datafile version.
  - `Redo LSN`: starting point for media recovery when loganchor redo is later than the datafile redo.
  - `Create LSN`: datafile creation LSN.
  - `MustRedo LSN`: redo target needed during media recovery.
  - `DataFileDescSlot ID`: changeTracking descriptor slot tied to the disk datafile.
- Incremental-backup header fields can include `Begin Backup Time`, `End Backup Time`, `IBChunk Count`, `Backup Target`, `Backup Level`, `Backup Type`, `TableSpace ID`, `File ID`, `Backup Tag Name`, and `Backup File Name`.

Output block: `dumpla`

- Sections: `[LOGANCHOR ATTRIBUTE SIZE]`, `[LOGANCHOR HEADER]`, `[TABLESPACE ATTRIBUTE]`, `[MEMORY CHECKPOINT PATH ATTRIBUTE]`, `[MEMORY CHECKPOINT IMAGE ATTRIBUTE]`, `[DISK DATABASE FILE ATTRIBUTE]`, `[Change Tracking ATTRIBUTE]`, and `[Backup Info ATTRIBUTE]`.
- High-value header fields:
  - `Binary DB Version`, `Archivelog Mode`, `Begin Checkpoint LSN`, `End Checkpoint LSN`, `Disk Redo LSN`, `LSN for Recovery from Replication`, `Server Status`, `End LSN`, `ResetLog LSN`, `Last Created Logfile Num`, and `Delete Logfile(s) Range`.
- `Server Status` caution: if startup sees a status indicating the previous server was started rather than cleanly shut down, restart recovery is required.
- Tablespace status values can include `OFFLINE`, `ONLINE`, `INCONSISTENT`, `CREATING`, `DROPPING`, `DROP_PENDING`, `DROPPED`, `DISCARDED`, `BACKUP`, `SWITCHING_TO_OFFLINE`, and `SWITCHING_TO_ONLINE`.
- Disk datafile status values can include `OFFLINE`, `ONLINE`, `CREATING`, `BACKUP_BEGIN`, `BACKUP_END`, `DROPPING`, `RESIZING`, and `DROPPED`.

Output block: `dumplf`

- Common record fields:
  - `LSN`: physical log position as file number and offset.
  - `COMP`: whether the log record is compressed.
  - `MAGIC`: validity value based on the log LSN.
  - `TID`: transaction identifier.
  - `BE`: begin-transaction flag.
  - `REP`: whether a replication Sender sends or references the log.
  - `ISVP` and `ISVP_DEPTH`: implicit savepoint flag and nesting depth.
  - `PLSN`: previous log LSN for the same transaction chain.
  - `LT`: log type.
  - `SZ`: log size in bytes.
- Frequently useful `LT` values include checkpoint, transaction commit/abort, savepoint, DDL, LOB-for-replication, memory update, NTA, compensation, file, disk redo/undo, and table metadata log types.
- `-S lsn [-F path] [-g]` output summarizes `INSERT`, `UPDATE`, `DELETE`, `COMMIT`, and `ROLLBACK` counts in memory database logs from an LSN; with `-g`, include table object ID statistics.

## Tool Block: `dumpbi`

Purpose: converts a `backupInfo` binary file to text.

When to Use:

- Inspect backup history stored in `backupInfo`.
- Validate backup slots, backup target, level, type, tag, and file names.

Representative Command:

```bash
dumpbi backupinfo
```

Compact syntax:

```text
dumpbi backupinfo_file_name
```

Key Inputs:

- `backupInfo` file from the target database environment.

Cautions:

- Use a copy for support collection if there is any risk of disturbing diagnostic evidence.

Verification Method:

- Output includes `[BACKUP INFO FILE HDR]` and `[BACKUP INFO SLOT]` sections.

## Tool Block: `dumpct`

Purpose: converts a `changeTracking` binary file to text.

When to Use:

- Diagnose incremental backup change tracking metadata.

Representative Command:

```bash
dumpct changeTracking
```

Compact syntax:

```text
dumpct changeTracking_file_name
```

Key Inputs:

- `changeTracking` file from the database environment.

Cautions:

- Interpret `Flush LSN`, tablespace type, page size, and bitmap list values with recovery context.

Verification Method:

- Output includes `[CHANGE TRACKING FILE HDR]` and `[CHANGE TRACKING FILE BODY]` sections.

## Tool Block: `dumpdb`

Purpose: inspects memory checkpoint image files and memory tablespace incremental backup files.

When to Use:

- Inspect memory tablespace metadata, tablespace free lists, table metadata, page contents, or incremental backup metadata.

Representative Command:

```bash
dumpdb -j 1
dumpdb -j 4 -d
dumpdb -j 6 -s 0 -p 4
dumpdb -j 7 -f SYS_TBS_MEM_DATA-0-0_TAG_MONDAY.ibak
```

Compact syntax:

```text
dumpdb {-j job_number} [-i pingpong_number] [-o object_id] [-f file_name] [-s tablespace_id] [-p page_id] [-d]
```

Key Inputs:

- `-j` job number:
  - `0`: `META`
  - `1`: `TABLESPACE`
  - `2`: `TABLESPACE-FLI`
  - `3`: `TABLESPACE-FREE-PAGE-LIST`
  - `4`: `TABLE`
  - `5`: `TABLE-ALLOC-PAGE-LIST`
  - `6`: `PAGE`
  - `7`: `INCREMENTAL_BACKUP_META`
- Optional tablespace, object, page, ping-pong, file, and detail arguments.

Cautions:

- `dumpdb` reads checkpoint image files on disk. If the server terminated abnormally after DDL and before the updated schema was written to disk, output might not show the latest in-memory state.

Verification Method:

- Output contains requested metadata, table, page, or backup information.

## Tool Block: `dumpddf`

Purpose: outputs header information for disk data files or specific pages in disk data files. It can also show incremental backup file header and backup information.

When to Use:

- Inspect disk tablespace datafile metadata for recovery or support analysis.

Representative Command:

```bash
dumpddf -f system001.dbf -m
dumpddf -f system001.dbf -p 100
dumpddf -m -f system001.dbf_TAG_MONDAY.ibak
```

Compact syntax:

```text
dumpddf {-f datafile_name} {-m | -p page_id}
```

Key Inputs:

- `-f`: datafile or incremental backup file.
- `-m`: header output.
- `-p`: page ID output.

Cautions:

- Ensure the file belongs to the target database and version.
- Avoid using stale copied datafile output as proof of current live state without timestamp context.

Verification Method:

- Header output includes `Binary DB Version`, `Redo LSN`, `Create LSN`, `MustRedo LSN`, and `DataFileDescSlot ID`.

## Tool Block: `dumpla`

Purpose: converts loganchor files to text. Loganchor files contain recovery metadata, tablespace attributes, checkpoint image paths, disk datafile attributes, change tracking metadata, and backup information.

When to Use:

- Diagnose startup recovery, tablespace state, checkpoint image state, datafile state, or backup metadata.

Representative Command:

```bash
dumpla loganchor0
```

Compact syntax:

```text
dumpla loganchor_file_name
```

Key Inputs:

- One of the loganchor files, typically named `loganchor0`, `loganchor1`, or `loganchor2`.

Cautions:

- Loganchor files are critical recovery metadata. Inspect copies when collecting evidence.
- `Server Status` can indicate whether restart recovery is required after abnormal shutdown.

Verification Method:

- Output includes sections such as `[LOGANCHOR HEADER]`, `[TABLESPACE ATTRIBUTE]`, `[MEMORY CHECKPOINT PATH ATTRIBUTE]`, `[DISK DATABASE FILE ATTRIBUTE]`, `[Change Tracking ATTRIBUTE]`, and `[Backup Info ATTRIBUTE]`.

## Tool Block: `dumplf`

Purpose: converts Altibase log files to text.

When to Use:

- Inspect transaction log headers, log types, transaction IDs, log sequence numbers, and update/commit/rollback activity.
- Count or summarize DML-related log activity in memory database logs.

Representative Command:

```bash
dumplf -f logfile0
dumplf -f logfile0 -t 6400
dumplf -f logfile0 -s
dumplf -f logfile0 -l
dumplf -S "0,0" -F $ALTIBASE_HOME/logs -g
```

Compact syntax:

```text
dumplf {-f log_file_name} [-t transaction_id] [-s] [-l] [-S lsn [-F path] [-g]]
```

Key Inputs:

- `-f`: log file name.
- `-t`: transaction ID filter.
- `-s`: output only log headers.
- `-l`: output log type and sub-logtype information.
- `-S`: output counts for `INSERT`, `UPDATE`, `DELETE`, `COMMIT`, and `ROLLBACK` in MMDB logs from an LSN.
- `-F`: log directory path for `-S`.
- `-g`: include table object ID statistics.

Cautions:

- Output is internal and version-sensitive. Use it as diagnostic evidence, not as a business-data extraction method.
- Keep LSN values literal when discussing recovery.

Verification Method:

- Output records include fields such as `LSN`, `COMP`, `MAGIC`, `TID`, `PLSN`, `LT`, and `SZ`.

## Tool Block: `dumptrc`

Purpose: converts and filters Altibase trace logs, including call stack information, into readable output for crash and abnormal termination analysis.

When to Use:

- Gather diagnostic evidence after abnormal shutdown.
- Convert process call stack addresses to function names.
- Print or follow selected trace logs from `$ALTIBASE_HOME/trc` or another trace directory.

Representative Command:

```bash
dumptrc -i server -i error
dumptrc -c -i error -i server -i sm -n 20
dumptrc -e error
dumptrc -p /path/to/altibase_home/trc -c -n 20
dumptrc -f
dumptrc -v
```

Compact syntax:

```text
dumptrc
  [-h]
  [-p file_path]
  [-c [-s]]
  [-a | -i file_name [-i file_name]... | -e file_name [-e file_name]...]
  [-n file_count]
  [-x]
  [-f]
  [-v]
```

Key Inputs:

- Trace directory, defaulting to `$ALTIBASE_HOME/trc`.
- Trace selectors such as `error`, `server`, `sm`, `rp`, `qp`, `dk`, `dr`, `xa`, `mm`, `rp_conflict`, `dump`, `trc`, `snmp`, `cm`, `misc`, and `sd`.
- `-c` to convert call stack addresses to function names.
- `-s` to show only the call stack without symbol conversion.
- `-x` to force call stack output when the `altibase` executable version and `dumptrc` version differ.

Cautions:

- The `dumptrc` version and Altibase executable version should match for normal call stack conversion.
- Use `dumptrc -x` only as a forced mismatch-mode diagnostic option for support use, not as the normal path.
- Trace logs can contain SQL text, host information, process IDs, and operational details. Treat output as sensitive.

Verification Method:

- Output shows selected logs and a summary such as number of logs printed.
- With `-c`, stack frames are annotated with function names when symbols are resolvable.

## Attachment Cross-References

- Use `02_administration_operations.md` when a utility recommendation affects startup, shutdown, backup, recovery, tablespaces, or service operations.
- Use `06_data_dictionary_performance_views.md` for SQL checks that verify utility output, object state, replication state, sessions, or file metadata.
- Use `07_error_messages_troubleshooting.md` with `altierr`, trace logs, dump-family output, and tool-reported Altibase error codes.
- Use `09_replication_ha_cdc.md` when tool output involves replication state, Replication Manager GUI actions, Log Analyzer CDC, XLog Sender, or replication log diagnostics.
- Use `13_isql_iloader_basic_tools.md` for iSQL and iLoader command-line workflows that complement `aexport`, migration, and data-load operations.
- Use `18_security_ssl_tls.md` for `altiAudit`, `altipasswd`, audit policy, password handling, and SSL/TLS-sensitive operational tooling.

## Operational Guardrails

- Prefer a read-only diagnostic utility first (`altierr`, `altiAudit`, `altiProfile`, dump-family tools, `altiComp DIFF`, `dataCompJ DIFF`) before recommending a corrective action.
- For data movement or synchronization, capture a pre-change baseline: row counts, replication status, relevant logs, and backup state.
- For generated scripts, inspect contents before execution and run on a staging system first when possible.
- For Kubernetes, keep `aku` lifecycle commands inside the pod lifecycle flow rather than running ad hoc from unrelated containers.
- For customer answers, translate the explanation but keep commands, options, properties, XML tags, file names, and SQL literal.

## Residual Scope

- Utility blocks cover the selected tools most likely to be used in customer answers. For unlisted options, utility output fields, or patch-specific command behavior, verify the installed utility manual or command help before producing a final runbook.
