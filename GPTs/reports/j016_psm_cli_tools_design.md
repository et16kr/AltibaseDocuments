# J016 PSM CLI Tools Remediation Design Note

Date: 2026-05-17
Job: J016 - PSM CLI ODBC C precompiler iSQL iLoader utility blocks

## Scope

J016 strengthens customer-facing attachment coverage for:

- `GPTs/attachments/10_psm_stored_external_procedures.md`
- `GPTs/attachments/12_c_cli_odbc_precompiler.md`
- `GPTs/attachments/13_isql_iloader_basic_tools.md`
- `GPTs/attachments/14_utilities_operation_tools.md`

The job is limited to PSM, external procedures, CLI, ODBC, Altibase C Interface, APRE,
iSQL, iLoader, utilities, dataCompJ, dump-family tools, and LOB/API token coverage.

## Source Basis

The remediation uses repository-local selected sources only, with Korean manuals as the
source of truth where paired English and Korean sources differ:

- Altibase 8.1 verified source Korean Stored Procedures Manual and External Procedures
  Manual for `NOCOPY`, `AUTHID`, iSQL `/`, `REF CURSOR`, `OPEN FOR`, external
  `LANGUAGE C`, `EXTERNAL`, `INTERNAL`, `PARAMETERS`, and external `RETURN`.
- Altibase 7.3 Korean release notes for anonymous block and `VARRAY` boundaries.
- Altibase 8.1 verified source Korean CLI, ODBC, Altibase C Interface, and
  Precompiler manuals for `DEFER_PREPARES`, `LongDataCompat`, `SQLFreeLob2`,
  `altibase_store_result()`, `altibase_use_result()`, APRE build tokens, and `SQLCA`
  or `WHENEVER` caveats.
- Altibase 8.1 verified source Korean iSQL and iLoader manuals for command-line
  options, `SYSDBA` restrictions, `SPOOL`, generated-file permissions, iLoader FORM
  flows, error files, and load modes.
- Altibase 8.1 verified source Korean Utilities Manual for `aexport`,
  `DBMS_METADATA`, `altiComp`, `altierr`, and dump-family dispatch, plus the Korean
  dataCompJ User's Manual for `dataCompJ` configuration and report artifacts.

## Documentation Shape

The attachment structure remains intact. The change adds retrieval-dense exact-answer
blocks near the top of each scoped file, while leaving the existing detailed sections as
the broader reference.

These blocks are intended to reduce synthesis omissions by clustering exact tokens,
version scope, and safety rules in one searchable place. They duplicate only high-value
source-backed items already represented by the detailed sections or selected manuals.

## Safety Rules Preserved

- Ask for exact Altibase version, client package, OS, compiler, driver manager, LOB
  size, connection method, object names, and operational window before production C/API,
  external procedure, bulk load, synchronization, or recovery-adjacent commands.
- Do not invent generic Oracle or ODBC behavior when Altibase-specific sources define a
  narrower rule.
- Treat `altiComp SYNC`, `dataCompJ SYNC`, `iLoader REPLACE`, `iLoader TRUNCATE`,
  generated `aexport` import scripts, and dump-family recovery interpretation as
  high-risk until backup, role, replication, and rollback inputs are known.
