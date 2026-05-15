# R22 CLI, ODBC, C Interface, Precompiler, iSQL, and iLoader

Date: 2026-05-16
Reviewer: Codex
Verdict: Pass

## Scope

- Attachments:
  - `GPTs/attachments/12_c_cli_odbc_precompiler.md`
  - `GPTs/attachments/13_isql_iloader_basic_tools.md`
- Supporting reports:
  - `GPTs/reports/eng_kor_parity.md`
  - `GPTs/reports/source_inventory.md`
- Source manuals sampled:
  - `Manuals/Altibase_7.1/kor/CLI User's Manual.md`
  - `Manuals/Altibase_7.3/kor/CLI User's Manual.md`
  - `Manuals/Altibase_trunk/kor/CLI User's Manual.md`
  - `Manuals/Altibase_7.1/kor/ODBC User's Manual.md`
  - `Manuals/Altibase_7.3/kor/ODBC User's Manual.md`
  - `Manuals/Altibase_trunk/kor/ODBC User's Manual.md`
  - `Manuals/Altibase_7.1/kor/Altibase C Interface Manual.md`
  - `Manuals/Altibase_7.3/kor/Altibase C Interface Manual.md`
  - `Manuals/Altibase_trunk/kor/Altibase C Interface Manual.md`
  - `Manuals/Altibase_7.1/kor/Precompiler User's Manual.md`
  - `Manuals/Altibase_7.3/kor/Precompiler User's Manual.md`
  - `Manuals/Altibase_trunk/kor/Precompiler User's Manual.md`
  - `Manuals/Altibase_7.1/kor/iSQL User's Manual.md`
  - `Manuals/Altibase_7.3/kor/iSQL User's Manual.md`
  - `Manuals/Altibase_trunk/kor/iSQL User's Manual.md`
  - `Manuals/Altibase_7.1/kor/iLoader User's Manual.md`
  - `Manuals/Altibase_7.3/kor/iLoader User's Manual.md`
  - `Manuals/Altibase_trunk/kor/iLoader User's Manual.md`
  - `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`

## Commands Run

```bash
bash review/scripts/run_review_remediation_cycle.sh status
rg -n $'\t(Reviewing|Remediating|ReReviewing|Fail)$' review/review_remediation_cycle_status.tsv
git status --short
sed -n '1,240p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,220p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,240p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
git diff -- GPTs/attachments/12_c_cli_odbc_precompiler.md
git diff -- GPTs/attachments/13_isql_iloader_basic_tools.md
git diff -- GPTs/reports/source_inventory.md
nl -ba GPTs/attachments/12_c_cli_odbc_precompiler.md | sed -n '1,1880p'
nl -ba GPTs/attachments/13_isql_iloader_basic_tools.md | sed -n '1,1380p'
rg -n "trunk|Altibase_trunk|/home/|file://|!\[|media/|TODO|FIXME|C:/|Manuals/|ReleaseNotes/" GPTs/attachments/12_c_cli_odbc_precompiler.md GPTs/attachments/13_isql_iloader_basic_tools.md
rg -n "SQLExecDirect|SQLPrepare|SQLBindParameter|SQLPutLob|SQLFreeLob2|SQLEmptyLob|SQLGetLobLength2|KEEP_SYSDBA|STARTUP SERVICE|fromPosition|LOBOFFSET|LongDataCompat|altibase_stmt_send_long_data|unsafe_null" GPTs/attachments/12_c_cli_odbc_precompiler.md GPTs/attachments/13_isql_iloader_basic_tools.md
rg -n -C 5 "fromPosition|SQLGetLob\(|SQLPutLob\(|SQLTrimLob\(|SQLFreeLob2|SQLEmptyLob|SQLGetLobLength2" Manuals/Altibase_7.1/kor/CLI\ User\'s\ Manual.md Manuals/Altibase_7.3/kor/CLI\ User\'s\ Manual.md Manuals/Altibase_trunk/kor/CLI\ User\'s\ Manual.md
rg -n -C 3 "libaltibase_odbc|ALTIBASE_HDB_ODBC|SQLLEN|ODBC 3\.51|LongDataCompat|SQL_BLOB|SQL_CLOB|unixODBC|iODBC" Manuals/Altibase_7.1/kor/ODBC\ User\'s\ Manual.md Manuals/Altibase_7.3/kor/ODBC\ User\'s\ Manual.md Manuals/Altibase_trunk/kor/ODBC\ User\'s\ Manual.md
rg -n -C 4 "altibase_init\(|altibase_connect\(|altibase_set_charset\(|altibase_store_result\(|altibase_use_result\(|altibase_fetch_lengths\(|altibase_stmt_send_long_data\(|altibase_stmt_set_array_bind\(|altibase_stmt_bind_param\(" Manuals/Altibase_7.1/kor/Altibase\ C\ Interface\ Manual.md Manuals/Altibase_7.3/kor/Altibase\ C\ Interface\ Manual.md Manuals/Altibase_trunk/kor/Altibase\ C\ Interface\ Manual.md
rg -n -C 4 -- "-parse|-mt|-unsafe_null|EXEC SQL BEGIN DECLARE SECTION|INDICATOR|sqlca\.sqlerrd\[2\]|WHENEVER|BLOB_FILE|CLOB_FILE|APRE_FILE_READ|APRE_FILE_CREATE|SQLLEN|ulpLibInterface|libapre|libodbccli" Manuals/Altibase_7.1/kor/Precompiler\ User\'s\ Manual.md Manuals/Altibase_7.3/kor/Precompiler\ User\'s\ Manual.md Manuals/Altibase_trunk/kor/Precompiler\ User\'s\ Manual.md
rg -n -C 6 "KEEP_SYSDBA|SYSDBA|STARTUP SERVICE|원격|DBMS를 구동" Manuals/Altibase_7.1/kor/iSQL\ User\'s\ Manual.md Manuals/Altibase_7.3/kor/iSQL\ User\'s\ Manual.md Manuals/Altibase_trunk/kor/iSQL\ User\'s\ Manual.md
rg -n -C 4 "LOBOFFSET|LOBSIZE|SET QUERYLOGGING|PLANCOMMIT|V\$TAB|SELECT \* FROM TAB|SELECT \* FROM SEQ|SET TIMESCALE|VERTICAL" Manuals/Altibase_7.1/kor/iSQL\ User\'s\ Manual.md Manuals/Altibase_7.3/kor/iSQL\ User\'s\ Manual.md Manuals/Altibase_trunk/kor/iSQL\ User\'s\ Manual.md
rg -n -C 6 -- "-rule csv|prefetch_rows|async_prefetch|lightmode|stmt_prefix|extra_col_delimiter|direct|parallel|atomic|use_lob_file=yes|lob_file_size|lob_indicator" Manuals/Altibase_7.1/kor/iLoader\ User\'s\ Manual.md Manuals/Altibase_7.3/kor/iLoader\ User\'s\ Manual.md Manuals/Altibase_trunk/kor/iLoader\ User\'s\ Manual.md
nl -ba ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md | sed -n '160,205p'
git diff --check
bash review/scripts/run_review_stage.sh validate
rg -n "trunk|Altibase_trunk|/home/|file://|!\[|media/|TODO|FIXME|C:/|Manuals/|ReleaseNotes/" GPTs/attachments/12_c_cli_odbc_precompiler.md GPTs/attachments/13_isql_iloader_basic_tools.md
rg -n "^Verdict:|^\| (Blocker|High|Medium|Low) \|" review/reports/R22_c_cli_odbc_precompiler_isql_iloader.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name README.md | wc -l
git status --short
```

## Findings

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Note | N/A | N/A | No actionable `Blocker`, `High`, `Medium`, or `Low` findings remain for this stage. The previous R22 API-order issue in the CLI LOB examples is resolved: the examples now use `<literal_id>` with `SQLExecDirect()` rather than an unbound `?` parameter marker. | No scoped attachment remediation is required for R22. |

## Source Checks

- Claims checked:
  - CLI handle and execution order; parameterized statement guidance; diagnostics; ODBC 3.51 positioning; ODBC driver manager and `SQLLEN` variants; `LongDataCompat`; LOB locator C types and transaction lifetime; `SQLGetLob()`, `SQLPutLob()`, `SQLTrimLob()`, `SQLFreeLob()`, `SQLFreeLob2()`; 8.1 Empty LOB interface names; ACI direct and prepared call ordering; ACI result cleanup and length-sensitive fetch; unsupported `altibase_stmt_send_long_data()`; APRE options, host variables, indicators, diagnostics, and file LOB syntax; iSQL connection, startup, script, output, LOB display, security, and file-permission commands; iLoader syntax, mode behavior, CSV cautions, delimiter rules, LOB handling, performance options, Direct-Path restrictions, error handling, and 8.1 Empty LOB behavior.
- Source coverage:
  - Korean CLI manuals for 7.1, 7.3, and 8.1-source define `SQLGetLob()` and `SQLPutLob()` `fromPosition` as byte-based and 0-based. The attachment follows this rule and explicitly treats conflicting English 1-based wording as drift.
  - Korean 8.1-source CLI manual documents `SQLFreeLob2(stmt, locator)` for JSON LOB locator cleanup after `SQLPutLob()` and states that it does not commit or roll back. The attachment preserves both facts.
  - Korean 8.1 release notes list `SQLEmptyLob()` and `SQLGetLobLength2` as Empty LOB CLI additions, and state that iLoader Empty LOB improvement applies only with `-lob` and `use_lob_file=yes`. The attachments preserve these literals with an appropriate compile-ready-code caution.
  - Korean iSQL manuals for 7.1, 7.3, and 8.1-source list `[-SYSDBA] [-KEEP_SYSDBA]`, state that only one `SYSDBA` connection is allowed, and state that remote `SYSDBA` can connect but cannot start the DBMS. The attachment now preserves these startup boundaries.
  - Korean ODBC manuals back ODBC 3.51 conformance, ODBC-on-CLI positioning, `libaltibase_odbc-64bit-ul32.so` and `libaltibase_odbc-64bit-ul64.so`, unixODBC/iODBC driver manager notes, `ALTIBASE_HDB_ODBC_64bit`, and `LongDataCompat=ON` for LOB compatibility.
  - Korean ACI manuals back `altibase_init()`/`altibase_connect()` setup, `altibase_set_charset()` precedence, result-set cleanup, `altibase_fetch_lengths()` for binary or length-sensitive data, array-bind ordering, and the unsupported status of `altibase_stmt_send_long_data()`.
  - Korean Precompiler manuals back APRE `-parse`, `-mt`, `-unsafe_null`, host declaration sections, `INDICATOR`, `SQLLEN`, `sqlca.sqlerrd[2]`, `WHENEVER`, `BLOB_FILE`, `CLOB_FILE`, `APRE_FILE_CREATE`, `APRE_FILE_OVERWRITE`, `APRE_FILE_APPEND`, and `APRE_FILE_READ`.
  - Korean iLoader manuals back the standard `formout` -> `out` -> `in` workflow, `APPEND`/`REPLACE`/`TRUNCATE`, `-rule csv` caution with `-f`, `-t`, `-r`, and `-e`, `-extra_col_delimiter`, LOB option behavior, LOB-column performance restrictions, `-direct` restrictions, `-parallel` connection counts, `-prefetch_rows`, `-async_prefetch`, `-lightmode`, `-bad`, `-log`, `-verbose`, and result codes.
- Korean/English source conflicts:
  - English CLI manuals sampled by earlier R22 work describe `SQLGetLob()`/`SQLPutLob()` `fromPosition` as beginning at 1, while Korean manuals say it starts at 0. The attachment correctly follows Korean source.
  - English iSQL manuals sampled by earlier R22 work omit `-KEEP_SYSDBA`, while Korean manuals include it. The attachment correctly follows Korean source.
  - The Korean iLoader manual itself contains a confusing `-rule csv` restriction that includes `-f` among delimiter-related options. The attachment treats this as a source conflict/caution and avoids copy-ready commands that combine `-rule csv` with `-f target_table.fmt`.
- Source gaps:
  - Detailed compile-ready signatures for `SQLEmptyLob()` and `SQLGetLobLength2()` were not found in the sampled 8.1-source CLI manual. The attachment mitigates this by preserving the literal function names and instructing users to check exact 8.1 headers or manuals before generating compile-ready C code.
  - Less common iLoader options can vary by client package and patch level. The attachment keeps the compact syntax intentionally partial and tells users to verify uncommon switches with the target client manual or runtime help.

## Oracle-Overlap Decision

- Correctly compressed:
  - Ordinary SQL and Oracle-overlapping DML remain brief. The reviewed files focus on Altibase-specific client interface behavior, LOB locator handling, JSON LOB cleanup, APRE behavior, iSQL operational commands, and iLoader data movement.
- Too much generic Oracle material:
  - None found in the scoped files.
- Missing Altibase-specific difference:
  - None requiring remediation. The previously missing Korean-source `fromPosition` and `-KEEP_SYSDBA` details are now present.

## Version Checks

- 7.1:
  - CLI LOB position rules, ODBC LOB compatibility, ACI call order, APRE build/indicator guidance, iSQL `SYSDBA` boundaries, and iLoader standard workflows are source-aligned for the sampled topics.
- 7.3:
  - The 7.3 client/tool behavior remains aligned with the attachment guidance for CLI, ODBC, ACI, APRE, iSQL, and iLoader. 7.3-specific iLoader performance options are framed as client-version-sensitive where appropriate.
- 8.1:
  - `Altibase 8.1 verified source` wording is used correctly for Empty LOB CLI/iLoader behavior and JSON LOB cleanup. The attachments avoid applying older 7.1/7.3 zero-length LOB guidance to 8.1 Empty LOB behavior.

## Retrieval And GPT Answer Quality

- Strengths:
  - `12_c_cli_odbc_precompiler.md` is searchable by interface, call flow, connection string, ODBC support, LOB locator rule, JSON cleanup, Empty LOB, diagnostics, ACI, APRE, and answer templates.
  - `13_isql_iloader_basic_tools.md` is task-oriented and preserves important command literals including `-SYSDBA`, `-KEEP_SYSDBA`, `/NOLOG`, `STARTUP SERVICE`, `SPOOL`, `START`, `AUTOCOMMIT`, `PLANCOMMIT`, `formout`, `out`, `in`, `-rule csv`, `-mode`, `-lob`, `use_lob_file=yes`, `-direct`, `-atomic`, `-parallel`, `-bad`, and `-log`.
- Risks:
  - Less common iLoader switches and patch-specific client behavior remain intentionally condensed. Production answers should continue to ask for exact Altibase/client version and use runtime help or target manuals for uncommon options.
  - Empty LOB CLI function names are preserved from the release notes, but compile-ready 8.1 C examples should still be checked against target headers.

## Required Follow-Up

- None for R22. No scoped attachment remediation is required before marking this stage done.
