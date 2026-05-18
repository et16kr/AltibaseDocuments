# ODBC And C Clients Playbook

- Playbook ID: `APB-000009`
- Owning job: `S2-J004`
- Validation status: `pass`
- Supported versions: Altibase 7.1, Altibase 7.3, and `Altibase 8.1 verified source`
- Protected topic: no

## Source Routes

Use this playbook for source-backed ODBC, CLI, ACI, Precompiler/APRE,
connection configuration, compile/link/runtime checks, DSN diagnostics, and
common connection diagnostics. It can draft guarded code and build files, but
compile-ready production code still requires installed headers, installed
libraries, compiler output, and customer runtime evidence.

| Route | Source IDs | Source-pack block refs | Baseline blocks |
| --- | --- | --- | --- |
| API, ACI, CLI, ODBC, and Precompiler/APRE manuals | `SRC-000046`, `SRC-000015`, `SRC-000050`, `SRC-000019`, `SRC-000052`, `SRC-000021`, `SRC-000065`, `SRC-000034`, `SRC-000068`, `SRC-000036`, `SRC-000110`, `SRC-000079`, `SRC-000114`, `SRC-000083`, `SRC-000116`, `SRC-000085`, `SRC-000128`, `SRC-000097`, `SRC-000130`, `SRC-000099`, `SRC-000170`, `SRC-000140`, `SRC-000174`, `SRC-000144`, `SRC-000176`, `SRC-000146`, `SRC-000188`, `SRC-000158`, `SRC-000190`, `SRC-000160` | `SRC-000046/BLOCK-000467`, `SRC-000015/BLOCK-000462`, `SRC-000050/BLOCK-000468`, `SRC-000019/BLOCK-000463`, `SRC-000052/BLOCK-000469`, `SRC-000021/BLOCK-000464`, `SRC-000065/BLOCK-000470`, `SRC-000034/BLOCK-000465`, `SRC-000068/BLOCK-000471`, `SRC-000036/BLOCK-000466`, `SRC-000110/BLOCK-000477`, `SRC-000079/BLOCK-000472`, `SRC-000114/BLOCK-000478`, `SRC-000083/BLOCK-000473`, `SRC-000116/BLOCK-000479`, `SRC-000085/BLOCK-000474`, `SRC-000128/BLOCK-000480`, `SRC-000097/BLOCK-000475`, `SRC-000130/BLOCK-000481`, `SRC-000099/BLOCK-000476`, `SRC-000170/BLOCK-000487`, `SRC-000140/BLOCK-000482`, `SRC-000174/BLOCK-000488`, `SRC-000144/BLOCK-000483`, `SRC-000176/BLOCK-000489`, `SRC-000146/BLOCK-000484`, `SRC-000188/BLOCK-000490`, `SRC-000158/BLOCK-000485`, `SRC-000190/BLOCK-000491`, `SRC-000160/BLOCK-000486` | `KAE-BLOCK-000002`, `KAE-BLOCK-000003`, `KAE-BLOCK-000004`, `KAE-BLOCK-000005`, `KAE-BLOCK-000006`, `KAE-BLOCK-000137`, `KAE-BLOCK-000138`, `KAE-BLOCK-000139`, `KAE-BLOCK-000140`, `KAE-BLOCK-000141`, `KAE-BLOCK-000192`, `KAE-BLOCK-000193`, `KAE-BLOCK-000194`, `KAE-BLOCK-000195`, `KAE-BLOCK-000196`, `KAE-BLOCK-000274` |
| AID source-backed development and client API reference route | `AID-SRC-000434` | `BLOCK-000444` | `KAE-BLOCK-000276` |

Guardrails: `CONF-000006` and `CONF-000007` remain open. Use this playbook
for guarded first drafts. Recheck exact source-pack blocks, installed headers,
installed libraries, `odbc.ini`, driver-manager output, compiler/linker
output, SQLSTATE, and application logs before treating a generated artifact as
complete or production-ready.

Forbidden assumption note: do not import generic ODBC, generic Unix, generic
Oracle Precompiler, or generic C client behavior into Altibase artifacts. Use
the exact Altibase CLI, ODBC, ACI, APRE, and API source routes above.

## Required Customer Inputs

Collect these inputs before drafting C, C++, APRE, ODBC, CLI, or ACI work:

- Target Altibase version and patch level, package type, OS, bitness,
  compiler, driver manager, and whether the target API is ODBC, CLI, ACI,
  Precompiler/APRE, or XA through the API manual route.
- `ALTIBASE_HOME`, include directory, library directory, runtime library path,
  installed header names, installed library names, and whether static or
  shared linking is required.
- DSN name, server host, port, DB name, user, password policy, `NLS_USE`,
  `LongDataCompat`, `DEFER_PREPARES`, transaction mode, and LOB, GEOMETRY, or
  JSON use.
- For unixODBC, `ODBCINI`, `ODBCSYSINI`, `odbc.ini`, `odbcinst.ini`,
  `odbcinst -j` output, driver-manager bitness, Altibase ODBC driver ELF
  bitness, `SQLLEN`, `SQLULEN`, and `dltest` output.
- For APRE, `.sc` path, output language, `apre` options, host-variable style,
  `SQLCA` usage, transaction policy, sample program target, and expected
  generated `.c` or `.cpp` file.
- For ACI, result-set size, LOB or GEOMETRY use, and whether
  `altibase_store_result()` or `altibase_use_result()` is appropriate.
- Expected runtime checks: connection success, SQL execution result,
  `SQLGetDiagRec` output, SQLSTATE, Altibase error code, connection loss
  symptoms, commit/rollback result, and cleanup evidence.

If any input is missing, ask for it and provide the safest source-backed next
check instead of inventing compiler options, DSN values, or API calls.

## Generated Artifacts

This playbook may draft:

- ODBC and CLI DSN configuration snippets for `odbc.ini`, connection strings,
  and first checks using exact tokens such as `DSN=ALTIBASE;LongDataCompat=ON`
  and
  `DRIVER=ALTIBASE_HDB_ODBC_64bit;User=SYS;Password=<password>;Server=127.0.0.1;PORT=20300;NLS_USE=US7ASCII;LongDataCompat=ON`.
- CLI C code skeletons using `SQLAllocHandle`, `SQLDriverConnect`,
  `SQLConnect`, `SQLGetDiagRec`, `SQLEndTran`, diagnostics, cleanup paths, and
  explicit transaction handling.
- ACI C build and result-handling notes using `alticapi.h`,
  `libalticapi.a`, `-lalticapi`, `altibase_store_result()`,
  `altibase_use_result()`, `altibase_free_result()`, `altibase_sqlstate()`,
  and `altibase_errno()`.
- Precompiler/APRE build snippets using `APRE`, `apre`, `.sc`, `.c`,
  `.cpp`, `-t c`, `-t cpp`, `-I`, `-D`, `-parse none`,
  `-parse partial`, `-parse full`, `libapre.a`, `-lapre`,
  `libodbccli.a`, and `-lodbccli`.
- Runtime prerequisites and checks for `$ALTIBASE_HOME/include/sqlcli.h`,
  `$ALTIBASE_HOME/lib/libodbccli.a`, `$ALTIBASE_HOME/include/alticapi.h`,
  `$ALTIBASE_HOME/lib/libalticapi.a`, `LD_LIBRARY_PATH`,
  `LD_LIBRARY_PATH_64`, `LIBPATH`, `SHLIB_PATH`, `ODBCINI`, and
  `ODBCSYSINI`.
- Diagnostics artifacts for SQLSTATE, `HY000`, `HY001`, `08001`, `08002`,
  `08003`, `08S01`, `SQL_SUCCESS_WITH_INFO`, `SQL_NO_DATA`,
  connection-disconnect symptoms, and first checks.
- Statement cleanup snippets using `SQLFreeStmt`, `SQL_CLOSE`, `SQL_DROP`,
  `SQL_UNBIND`, and `SQL_RESET_PARAMS` only when the source route and handle
  reuse intent match.

## Procedure

1. Classify the requested route as ODBC DSN, direct CLI code, ACI code,
   Precompiler/APRE embedded SQL, unixODBC integration, Windows ODBC, or XA.
2. Confirm target version, OS, compiler, and bitness. Do not mix 32-bit
   applications with 64-bit headers or libraries, and do not mix unixODBC
   manager bitness with a mismatched Altibase ODBC driver.
3. Confirm installed files before generating code: `$ALTIBASE_HOME/include`,
   `$ALTIBASE_HOME/lib`, `sqlcli.h`, `alticapi.h`, `libodbccli.a`,
   `libalticapi.a`, and `libapre.a`.
4. For ODBC, generate `odbc.ini` or a connection string only after confirming
   `ODBCINI`, driver path, DSN name, `NLS_USE`, `LongDataCompat`, and
   whether LOB data is involved.
5. For CLI code, allocate handles in source-backed order and add diagnostics
   for every failing call. Use `SQLEndTran()` only for local transaction
   commit or rollback; API/XA routes require the API manual's transaction
   manager sequence.
6. For statement cleanup, choose `SQLFreeStmt(stmt, SQL_CLOSE)` when all rows
   were not fetched and the statement handle should be reused, and
   `SQLFreeStmt(stmt, SQL_DROP)` only when the statement handle will not be
   reused.
7. For ACI, choose `altibase_store_result()` only when full client buffering is
   acceptable. Use `altibase_use_result()` for large result sets, LOBs, or
   GEOMETRY unless the customer explicitly wants buffering and has memory
   evidence.
8. For Precompiler/APRE, precompile `.sc` source with `apre` before compiling
   generated C or C++ source. Use `WHENEVER`, `SQLCA`, `SQLCODE`,
   `SQLSTATE`, `sqlerrm.sqlerrmc`, `sqlerrm.sqlerrml`, and `sqlerrd[2]`
   exactly as source-backed diagnostics.
9. For LOB and 8.1 routes, preserve `SQLPutLob`, `SQLFreeLob2(stmt, locator)`,
   and `SQLEndTran`. Treat `SQLEmptyLob()` and `SQLGetLobLength2()` as
   recheck items against installed headers or exact source blocks before
   generating compile-ready code.
10. For unixODBC, check `odbcinst -j`, `file $ALTIBASE_HOME/lib/libaltibase_odbc*`,
   and `dltest` before any application build. If `SQLLEN`/`SQLULEN` are 64-bit
   where the selected route expects 32-bit, stop and resolve the driver-manager
   build before debugging application code.

## Artifact Templates

Use placeholders until customer inputs and installed files are confirmed.

```ini
; 10_odbc.ini
[Altiodbc]
Driver = <absolute_path_to_altibase_odbc_driver>
UserName = <user>
Password = <password_from_secret_store>
Server = <host_ip>
User = <user>
Port = <port_no>
Database = <database_name>
NLS_USE = <character_set>
LongDataCompat = ON
TraceFile = <trace_file_path>
Trace = Yes
```

```text
# 20_odbc_connection_string.txt
DSN=ALTIBASE;LongDataCompat=ON

DRIVER=ALTIBASE_HDB_ODBC_64bit;User=SYS;Password=<password>;Server=127.0.0.1;PORT=20300;NLS_USE=US7ASCII;LongDataCompat=ON
```

```c
/* 30_cli_connect_skeleton.c */
#include <stdio.h>
#include <sqlcli.h>

static void print_diag(SQLSMALLINT handle_type, SQLHANDLE handle) {
    SQLCHAR sqlstate[6];
    SQLINTEGER native_error;
    SQLCHAR message[1024];
    SQLSMALLINT message_len;
    SQLSMALLINT rec = 1;

    while (SQLGetDiagRec(handle_type, handle, rec, sqlstate,
                         &native_error, message, sizeof(message),
                         &message_len) == SQL_SUCCESS) {
        printf("SQLSTATE=%s NativeError=%d Message=%s\n",
               sqlstate, native_error, message);
        rec++;
    }
}

int main(void) {
    SQLHENV env = SQL_NULL_HENV;
    SQLHDBC dbc = SQL_NULL_HDBC;
    SQLHSTMT stmt = SQL_NULL_HSTMT;
    SQLRETURN rc;

    rc = SQLAllocHandle(SQL_HANDLE_ENV, SQL_NULL_HANDLE, &env);
    if (rc != SQL_SUCCESS && rc != SQL_SUCCESS_WITH_INFO) return 1;

    rc = SQLAllocHandle(SQL_HANDLE_DBC, env, &dbc);
    if (rc != SQL_SUCCESS && rc != SQL_SUCCESS_WITH_INFO) {
        print_diag(SQL_HANDLE_ENV, env);
        return 1;
    }

    rc = SQLDriverConnect(dbc, NULL,
        (SQLCHAR *)"DSN=ALTIBASE;LongDataCompat=ON",
        SQL_NTS, NULL, 0, NULL, SQL_DRIVER_NOPROMPT);
    if (rc != SQL_SUCCESS && rc != SQL_SUCCESS_WITH_INFO) {
        print_diag(SQL_HANDLE_DBC, dbc);
        return 1;
    }

    rc = SQLAllocHandle(SQL_HANDLE_STMT, dbc, &stmt);
    if (rc == SQL_SUCCESS || rc == SQL_SUCCESS_WITH_INFO) {
        /* Add SQLExecDirect, fetch, diagnostics, and cleanup after validation. */
        SQLFreeHandle(SQL_HANDLE_STMT, stmt);
    }

    SQLEndTran(SQL_HANDLE_DBC, dbc, SQL_COMMIT);
    SQLDisconnect(dbc);
    SQLFreeHandle(SQL_HANDLE_DBC, dbc);
    SQLFreeHandle(SQL_HANDLE_ENV, env);
    return 0;
}
```

```makefile
# 40_cli_aci_apre_build.mk
ALTIBASE_HOME ?= /opt/altibase
ALTI_INCLUDE = $(ALTIBASE_HOME)/include
ALTI_LIBRARY = $(ALTIBASE_HOME)/lib

CPPFLAGS += -I$(ALTI_INCLUDE)
LDFLAGS += -L$(ALTI_LIBRARY)

# CLI
CLI_LIBS = -lodbccli

# ACI
ACI_LIBS = -lalticapi -lodbccli

# Precompiler/APRE
APRE_LIBS = -lapre -lodbccli

connect1.c: connect1.sc
	apre -t c connect1.sc

connect1_cpp.cpp: connect1.sc
	apre -mt -t cpp connect1.sc
```

```bash
# 50_runtime_and_driver_manager_checks.sh
test -f "$ALTIBASE_HOME/include/sqlcli.h"
test -f "$ALTIBASE_HOME/include/alticapi.h"
test -f "$ALTIBASE_HOME/lib/libodbccli.a"
test -f "$ALTIBASE_HOME/lib/libalticapi.a"
test -f "$ALTIBASE_HOME/lib/libapre.a"

file "$ALTIBASE_HOME"/lib/libaltibase_odbc*
odbcinst -j

# If using a custom unixODBC prefix:
/home/unixODBC/bin/dltest "$ALTIBASE_HOME/lib/libaltibase_odbc-64bit-ul32.so"
/home/unixODBC/bin/isql Altiodbc
```

```sql
-- 60_apre_embedded_sql_tokens.sc
EXEC SQL WHENEVER SQLERROR DO error_handler();
EXEC SQL CONNECT :usr IDENTIFIED BY :pwd USING :opt;
EXEC SQL COMMIT;
EXEC SQL ROLLBACK;
EXEC SQL DISCONNECT;
```

```c
/* 70_statement_cleanup_tokens.c */
SQLFreeStmt(stmt, SQL_CLOSE);
SQLFreeStmt(stmt, SQL_UNBIND);
SQLFreeStmt(stmt, SQL_RESET_PARAMS);
SQLFreeStmt(stmt, SQL_DROP);
```

## Guardrails

- Source authority: Korean product manuals and classified AID development
  references remain the authority routes. English manuals are extraction aids.
- Compile-ready code: do not promise compile success without the customer's
  compiler, bitness, installed header excerpts, installed library list, and
  exact linker output.
- DSN and connection strings: preserve `LongDataCompat=ON` only for source
  routes where LOB compatibility is required. Preserve `DEFER_PREPARES=ON` as
  an optional connection setting, not a default.
- unixODBC: check SQLLEN/SQLULEN separately from driver ELF bitness. The
  `ul32` and `ul64` tokens in Altibase ODBC driver filenames indicate SQLLEN
  size, not necessarily ELF bitness.
- ACI result buffering: avoid `altibase_store_result()` for large result sets,
  LOBs, or GEOMETRY unless the customer wants full buffering and provides a
  memory budget.
- Precompiler/APRE: do not generate Oracle-only `sqlwarn` handling. Do not use
  the precompiler library interface directly.
- LOB lifecycle: `SQLFreeLob2(stmt, locator)` releases the locator and is not a
  commit or rollback substitute. A transaction ending with `SQLEndTran()` can
  release LOB locators according to the source route.
- XA: if the API route is XA, replace ordinary local transaction assumptions
  with the API manual's transaction manager sequence; do not mix `SQLEndTran()`
  with global transaction completion without source-backed handling.

## Validation Checks

Before handing off generated C, C++, APRE, ODBC, CLI, or ACI artifacts,
include the relevant checks:

- Installed files: check `$ALTIBASE_HOME/include/sqlcli.h`,
  `$ALTIBASE_HOME/include/alticapi.h`, `$ALTIBASE_HOME/lib/libodbccli.a`,
  `$ALTIBASE_HOME/lib/libalticapi.a`, and `$ALTIBASE_HOME/lib/libapre.a`.
- Runtime library paths: verify `LD_LIBRARY_PATH`, `LD_LIBRARY_PATH_64`,
  `LIBPATH`, or `SHLIB_PATH` according to customer OS and compiler.
- unixODBC: run `odbcinst -j`, `file $ALTIBASE_HOME/lib/libaltibase_odbc*`,
  `dltest`, and a test `isql` connection to the DSN.
- CLI diagnostics: collect `SQLGetDiagRec` records on each failed handle,
  including SQLSTATE and native error. Prioritize connection SQLSTATE values
  such as `08001`, `08002`, `08003`, `08S01`, `HY000`, and `HY001`.
- APRE diagnostics: log `sqlca.sqlcode`, `SQLCODE`, `SQLSTATE`,
  `sqlca.sqlerrm.sqlerrmc`, `sqlca.sqlerrm.sqlerrml`, and `sqlerrd[2]` for
  DML row-count or fetch-array checks.
- ACI diagnostics: log `altibase_sqlstate()`, `altibase_errno()`,
  `altibase_error()`, `altibase_stmt_sqlstate()`, and
  `altibase_stmt_errno()` only after checking the exact source route and
  before another call resets the diagnostic state.
- Link checks: on Linux, unresolved POSIX thread, math, dynamic loader, or C++
  symbols can require system libraries such as `-lpthread`, `-lm`, `-ldl`,
  `-lcrypt`, `-lstdc++`, and `-lrt`; confirm against
  `$ALTIBASE_HOME/install/altibase_env.mk`, sample Makefiles, and linker
  errors.
- LOB checks: if ODBC LOB work is requested, run a small non-production LOB
  insert/select with `LongDataCompat=ON` and explicit transaction handling.

## Stop Conditions

Stop and ask for evidence if:

- Target version, OS, compiler, bitness, `ALTIBASE_HOME`, DSN, driver manager,
  SQLLEN/SQLULEN, or installed library paths are missing.
- A generated call uses an API function not present in the selected manual,
  installed header, or customer-provided header excerpt.
- The request asks for complete callable signatures for `SQLEmptyLob()` or
  `SQLGetLobLength2()` without installed header or exact source-block evidence.
- The customer asks for production-ready Makefiles, full option tables,
  platform-specific system libraries, or exhaustive SQLSTATE handling from
  this playbook alone.
- A connection string, DSN, source file, or Makefile would embed a password or
  secret that has not been routed through the customer's secret-handling
  policy.
- Oracle precompiler patterns, generic ODBC assumptions, or app-server
  defaults conflict with the Altibase CLI, ODBC, ACI, Precompiler/APRE, or API
  source route.
