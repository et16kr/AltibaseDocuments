# Tools Playbook

- Playbook ID: `APB-000011`
- Owning job: `S2-J007`
- Status: `pass`
- Version scope: Altibase `7.1`, `7.3`, and `8.1_verified` tool routes, plus guarded multi-version release-note and AID routes
- Protected topic: yes

## Source Routes

Use this playbook to draft iSQL, iLoader, utility, `dataCompJ`, dump-tool, `altiComp`, and `aexport` workflows. Keep exact command names, options, file names, environment variables, expected output tokens, and source-version boundaries.

Primary source routes:

| Route | Source IDs | Source-pack blocks | KAE blocks |
| --- | --- | --- | --- |
| iLoader manuals | `SRC-000044`;`SRC-000077`;`SRC-000107`;`SRC-000138`;`SRC-000167`;`SRC-000198` | `SRC-000044/BLOCK-000538`;`SRC-000077/BLOCK-000540`;`SRC-000107/BLOCK-000542`;`SRC-000138/BLOCK-000544`;`SRC-000167/BLOCK-000546`;`SRC-000198/BLOCK-000548` | `KAE-BLOCK-000014`;`KAE-BLOCK-000149`;`KAE-BLOCK-000205` |
| iSQL manuals | `SRC-000045`;`SRC-000078`;`SRC-000108`;`SRC-000139`;`SRC-000168`;`SRC-000199` | `SRC-000045/BLOCK-000539`;`SRC-000078/BLOCK-000541`;`SRC-000108/BLOCK-000543`;`SRC-000139/BLOCK-000545`;`SRC-000168/BLOCK-000547`;`SRC-000199/BLOCK-000549` | `KAE-BLOCK-000015`;`KAE-BLOCK-000150`;`KAE-BLOCK-000206` |
| Utilities, aexport, altiComp, dump tools, AKU, dataCompJ | `SRC-000043`;`SRC-000076`;`SRC-000106`;`SRC-000137`;`SRC-000166`;`SRC-000197`;`SRC-000206`;`SRC-000213`;`SRC-000220`;`SRC-000227`;`SRC-000449`;`SRC-000471` | `SRC-000043/BLOCK-000926`;`SRC-000076/BLOCK-000927`;`SRC-000106/BLOCK-000928`;`SRC-000137/BLOCK-000929`;`SRC-000166/BLOCK-000930`;`SRC-000197/BLOCK-000931`;`SRC-000206/BLOCK-000939`;`SRC-000213/BLOCK-000941`;`SRC-000220/BLOCK-000933`;`SRC-000227/BLOCK-000935`;`SRC-000449/BLOCK-000936`;`SRC-000471/BLOCK-000937` | `KAE-BLOCK-000038`;`KAE-BLOCK-000170`;`KAE-BLOCK-000227`;`KAE-BLOCK-000229`;`KAE-BLOCK-000252`;`KAE-BLOCK-000271` |
| AID utility and migration extracts | `AID-SRC-000043`;`AID-SRC-000044`;`AID-SRC-000045`;`AID-SRC-000046`;`AID-SRC-000047`;`AID-SRC-000110` | `AID-SRC-000043/BLOCK-000090`;`AID-SRC-000044/BLOCK-000091`;`AID-SRC-000045/BLOCK-000092`;`AID-SRC-000046/BLOCK-000093`;`AID-SRC-000047/BLOCK-000094`;`AID-SRC-000110/BLOCK-000409` | `KAE-BLOCK-000276` |

Cross-route baselines: `KAE-BLOCK-000274` for client/tool/integration alignment, `KAE-BLOCK-000275` for release-note and platform-sensitive rechecks, and `KAE-BLOCK-000276` for classified AID reuse.

Guardrail routes: `CONF-000004` for protected administration effects, `CONF-000006` for tool/client exact-option recheck, and `CONF-000007` for AID reuse limits.

## Required Customer Inputs

Collect these inputs before producing runnable tool commands:

- Target Altibase version, exact patch level when available, platform, shell, and installed tool version.
- `$ALTIBASE_HOME`, `$ALTIBASE_PORT_NO`, `$ALTIBASE_SSL_PORT_NO`, `$ALTIBASE_NLS_USE`, connection type, NLS/character-set policy, and credential-handling policy.
- Whether SSL/TLS is required, including `-ssl_ca`, `-ssl_capath`, `-ssl_cert`, `-ssl_key`, `-ssl_verify`, and `-ssl_cipher` paths when used.
- For iSQL: login mode, script file, spool/log file, formatting requirements, host variables, prompt/echo policy, and expected result rows.
- For iLoader: table name, FORM file, data files, delimiter or CSV rule, first/last rows, `-mode`, `-commit`, `-array`, `-parallel`, `-bad`, `-log`, LOB handling, partition handling, and rollback/reload plan.
- For `aexport`: source and target server names or IPs, ports, users, `aexport.properties`, `DBMS_METADATA` availability, `OPERATION`, `EXECUTE`, `TWO_PHASE_SCRIPT`, generated script names, and destination-drop policy.
- For `dataCompJ` and `altiComp`: master/slave connection strings, operation (`DIFF` or `SYNC`), table pairs, keys, exclusions, thread and commit settings, output log location, and post-sync verification plan.
- For dump tools: exact input file such as `backupInfo`, `changeTracking`, checkpoint image, incremental backup file, datafile, or loganchor file, plus whether the output can expose sensitive metadata.

If any input is missing, ask for it and provide a read-only next check such as installed help output, file existence checks, or dictionary queries rather than inventing a final command.

## Generated Artifacts

Allowed artifacts are first drafts of command lines, shell scripts, SQL snippets, configuration fragments, validation checks, and troubleshooting bundles. Preserve source command names and case.

### iSQL workflow draft

```bash
export ALTIBASE_HOME=/opt/altibase
export ALTIBASE_NLS_USE=UTF8

isql -s 127.0.0.1 -u sys -p manager -port 20300 -F ./checks.sql -O ./checks.out
```

```sql
SPOOL ./checks.spool
SET LINESIZE 160;
SET PAGESIZE 50;
SET FEEDBACK ON;
SET QUERYLOGGING ON;
VAR p1 INTEGER;
EXECUTE :p1 := 100;
PRINT p1;
SELECT * FROM V$TAB;
SPOOL OFF;
```

Use `START file_name`, `@ file_name`, or `@@ file_name` only when the script path and working directory are confirmed. For command logging, preserve the documented `$ALTIBASE_HOME/trc/isql_query.log` route when `SET QUERYLOGGING ON` is used.

### iLoader load and export draft

```bash
iloader formout -s 127.0.0.1 -u sys -p manager -port 20300 -T T1 -f T1.fmt
iloader out -s 127.0.0.1 -u sys -p manager -f T1.fmt -d T1.dat -log T1.out.log -bad T1.out.bad
iloader in -s 127.0.0.1 -u sys -p manager -f T1.fmt -d T1.dat -mode APPEND -F 1 -commit 1000 -array 1000 -log T1.in.log -bad T1.in.bad
```

For CSV mode, keep the documented incompatibility boundary: do not combine `-rule csv` with delimiter/enclosing options such as `-f`, `-t`, `-r`, or `-e` unless the exact target-version source explicitly allows the combination. Preserve `DATA_NLS_USE=US7ASCII` and `NCHAR_UTF16=YES` in FORM-file examples when they come from source output.

Expected iLoader result tokens to preserve in validation notes include `Total 3 record download(T1)`, `DOWNLOAD :`, `UPLOAD :`, and `Load Count : 2(T1)`. Interpret result code `-2` as upload completed with one or more row errors, then inspect `-bad` and `-log`.

### aexport migration script route

```bash
cd "$ALTIBASE_HOME"
aexport -s 127.0.0.1 -port 20300 -u sys -p manager
sh run_il_out.sh
sh run_is.sh
sh run_il_in.sh
sh run_is_refresh_mview.sh
sh run_is_index.sh
sh run_is_fk.sh
sh run_is_alt_tbl.sh
```

When `TWO_PHASE_SCRIPT=ON`, route constraint creation through `sh run_is_con.sh`. Before drafting a destination run, warn that `run_is.sh` deletes destination users and objects according to source guidance, check `*.bad` files, and inspect generated logs.

`aexport.properties` drafts may include these exact source keys only after customer confirmation: `OPERATION`, `EXECUTE`, `INVALID_SCRIPT`, `TWO_PHASE_SCRIPT`, `CRT_TBS_USER_MODE`, `INDEX`, `USER_PASSWORD`, `VIEW_FORCE`, `DROP`, `ILOADER_OUT`, `ILOADER_IN`, `ISQL`, `ISQL_CON`, `ISQL_INDEX`, `ISQL_FOREIGN_KEY`, `ISQL_REPL`, `ISQL_REFERSH_MVIEW`, `ISQL_ALT_TBL`, `ILOADER_FIELD_TERM`, `ILOADER_ROW_TERM`, `ILOADER_PARTITION`, `ILOADER_ERRORS`, `ILOADER_ARRAY`, `ILOADER_COMMIT`, `ILOADER_PARALLEL`, `ILOADER_ASYNC_PREFETCH`, and `SSL_ENABLE`.

### dataCompJ and altiComp comparison route

```bash
dataCompJCli.sh -f ./dataCompJ.xml
altiComp -f ./sample.cfg
```

`dataCompJ` drafts must keep `Connections`, `Options`, `TablePairs`, `MasterDB`, `SlaveDB`, `Operation`, `Diff`, `Sync`, `Log`, `MaxThread`, `Projection`, and `Selection` in XML source terminology. Record `dataCompJ_report.txt`, `dataCompJ.log`, and `dataCompJ_data.log` as output files; warn that tracing inconsistent records in `dataCompJ_data.log` can be large and can affect performance.

For `altiComp`, preserve `DB_MASTER`, `DB_SLAVE`, `OPERATION=DIFF|SYNC`, `INSERT_TO_SLAVE`, `INSERT_TO_MASTER`, `DELETE_IN_SLAVE`, `UPDATE_TO_SLAVE`, `CHECK_INTERVAL`, `MAX_THREAD`, `COUNT_TO_COMMIT`, `FILE_MODE_MAX_ARRAY`, `TABLES`, `WHERE`, `EXCLUDE`, `TABLE`, and `SCHEMA`. Do not generate a config with both `INSERT_TO_MASTER` and `DELETE_IN_SLAVE` set to `ON`.

### Dump and utility diagnostics route

```bash
dumpbi backupInfo
dumpct changeTracking
dumpdb -j 1
dumpdb -j 7 -f SYS_TBS_MEM_DATA-0-0_TAG_MONDAY.ibak
dumpddf -f SYS_TBS_DISK_DATA-0-0.dwf -m
dumpla loganchor0
altierr -w replication
altiAudit audit.log
altiProfile -stat query profile_name
```

Use dump tools only against explicitly supplied files. For `dumpdb`, `dumpddf`, `dumpbi`, `dumpct`, `dumpla`, `dumplf`, and `dumptrc`, prefer read-only diagnostic output and ask for the source section or installed help before adding options not present in the local source route.

## Guardrails

- Treat iSQL, iLoader, `aexport`, `altiComp`, `dataCompJ`, dump tools, and utilities as version-sensitive. Recheck the matching source block before finalizing command options.
- Keep credentials out of reusable scripts when the customer policy forbids inline passwords. If a source example uses `-p manager`, label it as a source sample, not a recommended production secret pattern.
- Preserve NLS warnings. For iLoader, do not omit the character-set check because source notes warn that an omitted or wrong NLS can corrupt data.
- Do not run `aexport` against an active production service without a maintenance and rollback plan. Do not generate `DROP=ON` or a destination `run_is.sh` run without explicit approval.
- Do not treat `aexport` as a physical backup. It exports logical structure and data through generated scripts and iLoader routes.
- For `iLoader -direct nolog`, require an explicit backup/recovery plan because source guidance warns recovery is impossible if a no-logging direct path fails.
- For `dataCompJ` or `altiComp SYNC`, require primary keys, data-type compatibility, table-pair confirmation, a validation `DIFF`, and a rollback plan.
- For `ALTIBASE_UT_FILE_PERMISSION`, `ISQL_FILE_PERMISSION`, and patch-note-sensitive tool behavior, state that final behavior depends on the exact patch level and installed build.

## Validation Checks

Run validation in layers:

1. Check executable and version evidence with installed help, for example `isql -H`, `iloader -h`, `aexport -h`, `dataCompJCli.sh -f sample.xml` only when a sample config exists, or `altiComp -f sample.cfg` only in a test environment.
2. Check file prerequisites: `aexport.properties`, FORM file, data files, bad/log files, XML config, `sample.cfg`, source dump files, output directories, and permissions.
3. For iSQL scripts, verify `SPOOL OFF`, `SET QUERYLOGGING OFF` when needed, expected SQL row counts, and `$ALTIBASE_HOME/trc/isql_query.log`.
4. For iLoader, verify `-bad` files, `-log` files, return code `0`, `-1`, or `-2`, `Load Count`, and source/target row counts.
5. For `aexport`, inspect generated scripts, generated logs, `*.bad` file sizes, and destination object counts before and after `run_is.sh` or `run_is_con.sh`.
6. For `dataCompJ`, require a successful Build phase, no unsupported-table findings in `dataCompJ_report.txt`, and a post-`SYNC` `DIFF` that reports all records identical.
7. For `altiComp`, inspect `script_file_name.log`, per-table difference logs, and commit/error summaries.
8. For dump-tool diagnostics, preserve the exact command, input file, output file, and timestamp so the diagnostic can be reproduced.

## Stop Conditions

Stop and ask for missing evidence when:

- The customer has not supplied target version, patch level, platform, source/target objects, input files, or a rollback plan for state-changing operations.
- Source and installed help disagree on a command option, or an option appears only in release notes for a specific patch.
- `aexport` would delete destination users or objects, `DROP=ON` is requested, or `run_is.sh` would target an unconfirmed database.
- iLoader reports `-1` or `-2`, creates non-empty `*.bad` files, or row counts differ.
- `dataCompJ` Build reports unsupported LOB or incompatible data types, missing comparable non-PK columns, or mismatched primary-key definitions.
- `altiComp` table-pair rules would synchronize in the wrong direction or conflict with the documented `INSERT_TO_MASTER` and `DELETE_IN_SLAVE` restriction.
- Dump-tool input files are missing, live production files would be read unsafely, or output could expose sensitive metadata without approval.

## Cleanup And Rollback

Preserve cleanup commands as drafts until the customer confirms the run directory and database role. Typical cleanup includes archiving `*.log`, `*.bad`, `dataCompJ_report.txt`, `dataCompJ.log`, `dataCompJ_data.log`, `script_file_name.log`, generated `run_*.sh` scripts, dump outputs, and temporary FORM/data files. For load/sync workflows, rollback must be source-specific: restore from backup, reload from verified exports, run reverse `SYNC` only when source-backed and approved, or drop/recreate generated objects only after object names and dependencies are confirmed.
