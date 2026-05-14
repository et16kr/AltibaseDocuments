# English Consistency QA Report

Job: `JOB-083`
Phase: P8 QA
Date: 2026-05-14
Result: Pass

## Objective

Validate that customer-facing attachment Markdown files are English canonical and do not contain Korean text except where needed for examples or source names.

## Scope

- Directory: `GPTs/attachments/`
- Files counted: Markdown attachment files at max depth 1, excluding `README.md`
- Acceptance focus: English canonical prose, literal preservation of SQL/object/command names, customer-safe 8.1 labels, and no Korean-script leakage.

## Required Validation Commands

```bash
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' | wc -l
```

Output:

```text
20
```

```bash
rg -n "trunk|C:/|file://" GPTs/attachments || true
```

Output:

```text
No matches.
```

## Korean-Script Scan

Command:

```bash
rg -n -P "\p{Hangul}" GPTs/attachments --glob '*.md' || true
```

Output:

```text
No matches.
```

Supplemental broad CJK command:

```bash
rg -n -P "[\p{Hangul}\p{Han}\p{Hiragana}\p{Katakana}]" GPTs/attachments --glob '*.md' || true
```

Output:

```text
No matches.
```

## Per-File Korean-Script Counts

Command:

```bash
for f in GPTs/attachments/*.md; do
  [ "$(basename "$f")" = README.md ] && continue
  printf '%s|' "$(basename "$f")"
  rg -n -P "\p{Hangul}" "$f" | wc -l
done
```

Output:

```text
00_version_release_platform.md|0
01_getting_started_installation.md|0
02_administration_operations.md|0
03_sql_ddl_generation.md|0
04_sql_dml_oracle_compatibility.md|0
05_data_types_properties.md|0
06_data_dictionary_performance_views.md|0
07_error_messages_troubleshooting.md|0
08_performance_tuning_monitoring.md|0
09_replication_ha_cdc.md|0
10_psm_stored_external_procedures.md|0
11_java_jdbc_spring.md|0
12_c_cli_odbc_precompiler.md|0
13_isql_iloader_basic_tools.md|0
14_utilities_operation_tools.md|0
15_migration_oracle_compatibility.md|0
16_dblink_external_connectors.md|0
17_kubernetes_aku_cloud.md|0
18_security_ssl_tls.md|0
19_spatial_nifi_tableau_misc.md|0
```

## Customer-Safe 8.1 Label Check

Command:

```bash
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' -exec rg -l "Altibase 8\.1 verified source" {} + | wc -l
```

Output:

```text
20
```

Command:

```bash
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' -exec rg --files-without-match "Altibase 8\.1 verified source" {} + || true
```

Output:

```text
No matches.
```

## Review Notes

- All 20 upload attachments are written in English canonical prose.
- Korean script does not appear in any customer-facing attachment file, so no example/source-name exception is needed.
- Literal SQL names, function names, error codes, property names, commands, and file paths are preserved as technical tokens.
- All 20 upload attachments use customer-safe 8.1 wording through `Altibase 8.1 verified source`.
- The forbidden-string scan found no `trunk`, `C:/`, or `file://` leakage in `GPTs/attachments/`.

## Conclusion

`JOB-083` acceptance criteria are satisfied. No attachment content changes were required for this QA pass.
