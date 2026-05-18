# Korean-Aligned English Baseline: Stored And External Procedures

- Job: `S1R-J002`
- Scope: stored procedures, stored functions, PSM blocks, packages, typesets,
  user-defined PSM types, dynamic SQL, exceptions, built-in PSM package
  routing, C/C++ external procedure registration, external library routing,
  and the two English-only stored-procedure media extraction rows.
- Source-pack gate: `GPTs/source_pack/source_pack_validation.md` records
  `Status: pass`, `Verdict: Pass`, no blockers, and exact source-pack block
  preservation for the selected stored/external procedure sources.
- Authority rule: Korean Stored Procedures Manuals and Korean External
  Procedures Manuals are authoritative. English product manuals are extraction
  aids. For 8.1 material, preserve the established `Altibase 8.1 verified
  source` boundary.
- Downstream boundary: this file is a working baseline for guarded first
  drafts. It does not replace exact source-pack extraction, item-level syntax
  conversion, installed-library checks, C/C++ compilation, deployed server
  validation, or customer runtime evidence.

## Design Note

`S1R-J002` adds a dedicated stored/external procedure baseline file instead of
rewriting the generated S1-J006 inventory rows. The original per-manual
inventory rows remain immutable generated evidence, while `KAE-BLOCK-000277`
through `KAE-BLOCK-000279` provide downstream-ready routing for this job:
stored procedure manuals, external procedure manuals, and English-only media
exclusion. This keeps Korean authority explicit and prevents the two
English-only media extraction rows from becoming customer-facing authority.

## Batch Source Coverage

| Route | Korean source IDs | English source IDs | Baseline manifest rows | Disposition |
| --- | --- | --- | --- | --- |
| Stored procedures and PSM | `SRC-000075`, `SRC-000136`, `SRC-000196` | `SRC-000042`, `SRC-000105`, `SRC-000165` | `KAE-BLOCK-000037`, `KAE-BLOCK-000168`, `KAE-BLOCK-000225`, plus `KAE-BLOCK-000277` | aligned baseline route |
| C/C++ external procedures | `SRC-000055`, `SRC-000119`, `SRC-000179` | `SRC-000024`, `SRC-000088`, `SRC-000149` | `KAE-BLOCK-000036`, `KAE-BLOCK-000167`, `KAE-BLOCK-000224`, plus `KAE-BLOCK-000278` | aligned baseline route |
| English-only stored-procedure media extraction rows | none selected | `SRC-000109`, `SRC-000169` | `KAE-BLOCK-000169`, `KAE-BLOCK-000226`, plus `KAE-BLOCK-000279` | nonblocking exclusion |

## KAE-BLOCK-000277: Stored Procedure And PSM Routing

- Source IDs: `SRC-000075`, `SRC-000042`, `SRC-000136`, `SRC-000105`,
  `SRC-000196`, `SRC-000165`.
- Version scope: 7.1, 7.3, and `Altibase 8.1 verified source`.
- Source block refs: `SRC-000075/BLOCK-000897`, `SRC-000042/BLOCK-000895`,
  `SRC-000136/BLOCK-000902`, `SRC-000105/BLOCK-000899`,
  `SRC-000196/BLOCK-000907`, `SRC-000165/BLOCK-000904`.
- Alignment status: baseline generated from paired Korean authority and English
  extraction aids. Exact grammar, all examples, all built-in package routines,
  and patch-specific behavior still require source-pack or installed-version
  recheck before production use.

Baseline:

1. Route stored procedure work to the target-version Korean Stored Procedures
   Manual first, using the paired English manual only as an extraction aid.
   Preserve Altibase tokens such as `CREATE PROCEDURE`, `ALTER PROCEDURE`,
   `DROP PROCEDURE`, `EXECUTE`, `CREATE FUNCTION`, `ALTER FUNCTION`,
   `DROP FUNCTION`, `CREATE TYPESET`, `DROP TYPESET`, `CREATE PACKAGE`,
   `CREATE PACKAGE BODY`, `ALTER PACKAGE`, and `DROP PACKAGE`.
2. Treat PSM as Altibase PSM, not generic PL/SQL. Do not infer Oracle-only
   syntax, package behavior, or generic database assumptions. Generate from
   the exact target-version route and check unsupported constructs before
   presenting a final customer artifact.
3. For procedures, preserve `IN`, `OUT`, `IN OUT`, `NOCOPY`, and `AUTHID
   CURRENT_USER` or `AUTHID DEFINER`. `IN` is the default parameter mode.
   `AUTHID DEFINER` is the default authority model. `OUT` and `IN OUT`
   parameters must not receive default values.
4. For functions, preserve `RETURN data_type`, `RETURN expression`, and
   `DETERMINISTIC`. A stored function must return a value. A stored procedure
   must not return a value through a `RETURN` statement. Use `DETERMINISTIC`
   only when the same input always returns the same result.
5. Use `IF NOT EXISTS` and `IF EXISTS` only where the target-version source
   exposes them. The 8.1 verified source includes idempotent forms for stored
   procedure, stored function, typeset, package, and package body routes; do
   not backport those clauses to 7.1 or 7.3 without exact source evidence.
6. Route PSM blocks, variables, `SELECT ... INTO`, `BULK COLLECT`, `RETURNING
   INTO`, assignments, labels, `PRINT`, control flow, cursors, `REF CURSOR`,
   user-defined `RECORD`, `ASSOCIATIVE ARRAY`, `VARRAY`, dynamic SQL,
   exceptions, pragmas, packages, and built-in package questions back to this
   block and then to the exact source-pack row for item-level syntax.
7. Preserve the version boundary for `VARRAY`: the 7.3 and 8.1 verified Korean
   sources include `VARRAY`, `VARRAY_MEMORY_MAXIMUM`, constructor
   initialization, `EXTEND`, `TRIM`, and type-name compatibility guidance.
   The 7.1 stored procedure route uses `ASSOCIATIVE ARRAY` and `REF CURSOR`
   coverage, but does not establish the 7.3+ `VARRAY` baseline.
8. For result sets returned to clients, prefer a `REF CURSOR` exposed through
   an `OUT` or `IN OUT` procedure parameter. Do not return a cursor variable
   from a function `RETURN` clause unless exact source evidence for the target
   version is provided.

Safe first checks:

- Ask for target Altibase version and patch, object owner, object names,
  required privileges, dependent tables, desired parameter modes, expected row
  counts, transaction expectations, and whether the routine will be called from
  SQL, PSM, JDBC, ODBC, or another client.
- Check existing routine status and dependencies before replacing or dropping
  objects. Use source-backed metadata routes such as `SYS_PROCEDURES_`,
  `SYS_PROC_PARAS_`, `SYS_PROC_PARSE_`, and `SYS_PROC_RELATED_` when exact
  object state matters.
- Compile in a non-production schema first and execute a minimal call path
  before moving generated PSM into production.

Stop conditions:

- Stop if the requested answer depends on live object definitions, runtime
  errors, patch level, privileges, data volume, transaction side effects, or
  client binding behavior that the customer has not supplied.
- Stop if a request asks for exhaustive built-in package routine coverage,
  complete syntax diagrams, or every example from the manuals from this
  baseline alone. Route to the exact source-pack block.
- Stop if an Oracle PL/SQL pattern conflicts with the Altibase source route.

## KAE-BLOCK-000278: External C/C++ Procedure Routing

- Source IDs: `SRC-000055`, `SRC-000024`, `SRC-000119`, `SRC-000088`,
  `SRC-000179`, `SRC-000149`.
- Version scope: 7.1, 7.3, and `Altibase 8.1 verified source`.
- Source block refs: `SRC-000055/BLOCK-000896`, `SRC-000024/BLOCK-000894`,
  `SRC-000119/BLOCK-000901`, `SRC-000088/BLOCK-000898`,
  `SRC-000179/BLOCK-000906`, `SRC-000149/BLOCK-000903`.
- Alignment status: baseline generated from paired Korean authority and English
  extraction aids. C/C++ ABI, shared-library loading, external-agent behavior,
  and deployed runtime outcomes remain validation-required.

Baseline:

1. Route external procedure work to the target-version Korean External
   Procedures Manual first. Preserve source tokens such as `CREATE LIBRARY`,
   `ALTER LIBRARY`, `DROP LIBRARY`, `CREATE PROCEDURE`, `DROP PROCEDURE`,
   `CREATE FUNCTION`, `DROP FUNCTION`, `EXECUTE`, `LANGUAGE C`, `LIBRARY`,
   `NAME`, `PARAMETERS`, `EXTERNAL`, and `INTERNAL`.
2. Use this source-backed deployment order for first drafts: write the C/C++
   user function, write the required `entryfunction`, build a shared library,
   place the library where Altibase can load it, create or replace the library
   object, create the external procedure or function object, then call and
   validate it.
3. Preserve the documented entry point shape:
   `extern "C" void entryfunction(char* func_name, int arg_count, void ** args,
   void ** returnArg);`. Do not change the entry function name or parameter
   types in generated examples without exact source or installed-code evidence.
4. Preserve external mode boundaries. `EXTERNAL` mode or omission uses the
   external agent process. `INTERNAL` mode loads and executes the dynamic
   library directly in the Altibase server process. Treat `INTERNAL` as a
   higher operational risk and require explicit approval and test evidence.
5. Preserve external function `RETURN` handling in the `PARAMETERS` list.
   `RETURN` identifies the parameter that receives the external function
   return value, must appear after all function argument parameters, and if no
   attribute parameter follows `RETURN`, `RETURN` alone is equivalent to
   omitting it.
6. Route diagnostics to the source-backed metadata and performance-view paths:
   `SYS_LIBRARIES_`, `SYS_PROCEDURES_`, `V$EXTPROC_AGENT`, and `V$LIBRARY`.
   Route external-agent configuration to
   `EXTPROC_AGENT_CONNECT_TIMEOUT`, `EXTPROC_AGENT_CALL_RETRY_COUNT`,
   `EXTPROC_AGENT_IDLE_TIMEOUT`, and `EXTPROC_AGENT_SOCKET_FILEPATH`.
7. Do not use the external procedure manuals as general C Interface, ODBC,
   or Precompiler documentation. Client-side C and ODBC work stays in the
   client/tool integration route; this block covers server-side native
   library registration and invocation.

Safe first checks:

- Ask for target Altibase version and patch, operating system, compiler,
  bitness, shared-library extension, `ALTIBASE_HOME`, library path, source
  code, exported function names, parameter mapping, desired external mode, and
  rollback plan before generating a deployable artifact.
- Build and test the shared library outside production first. Confirm the
  library object compiles, the external routine compiles, and `V$LIBRARY` or
  `V$EXTPROC_AGENT` shows the expected state before customer traffic uses it.
- For property changes, check the exact General Reference source and current
  runtime configuration before changing external-agent settings.

Stop conditions:

- Stop if the customer cannot confirm compiler/runtime ABI, library path,
  deployment account, external mode, parameter types, or source code.
- Stop if the requested artifact would load unreviewed native code into the
  server process or external agent.
- Stop if the answer depends on deployed shared-library behavior, server logs,
  trace files, object status, or live failure output that has not been
  provided.

## KAE-BLOCK-000279: English-Only Stored Procedure Media Exclusion

- Source IDs: `SRC-000109`, `SRC-000169`.
- Version scope: 7.3 and `Altibase 8.1 verified source`.
- Source block refs: `SRC-000109/BLOCK-000900`, `SRC-000169/BLOCK-000905`.
- Alignment status: nonblocking exclusion. These rows remain in the exact
  source pack as English extraction evidence, but they are not Korean-aligned
  authority and are not a downstream customer-facing baseline source.

Baseline:

1. Do not copy `SRC-000109` or `SRC-000169` into customer-facing baseline,
   playbook, attachment, or upload-package text as authoritative Altibase
   behavior.
2. If a stored procedure answer needs manual authority, route to
   `KAE-BLOCK-000277` and the paired Korean/English Stored Procedures Manual
   sources for the target version.
3. If an external procedure answer needs manual authority, route to
   `KAE-BLOCK-000278` and the paired Korean/English External Procedures Manual
   sources for the target version.
4. If a later job wants to promote these media rows, require paired Korean
   authority or an explicit approved auxiliary disposition first. Until then,
   they are retained only as exact source-pack evidence with an English-only
   extraction-aid label.

Safe first checks:

- Check whether the requested example exists in the paired Korean manual route
  before using these media rows.
- Check the source label before citing either media row; the label must remain
  visible if the row is discussed as evidence.

Stop conditions:

- Stop if an answer would depend solely on `SRC-000109` or `SRC-000169`.
- Stop if the requested use would silently upgrade English-only media into
  Korean-authoritative customer guidance.
