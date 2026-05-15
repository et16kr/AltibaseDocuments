# R12 Development Interfaces Review
Date: 2026-05-15
Reviewer: Codex
Verdict: Pass With Follow-Up

## Scope
- Attachments:
  - `GPTs/attachments/10_psm_stored_external_procedures.md`
  - `GPTs/attachments/11_java_jdbc_spring.md`
  - `GPTs/attachments/12_c_cli_odbc_precompiler.md`
  - `GPTs/attachments/13_isql_iloader_basic_tools.md`
- Supporting reports:
  - `review/Altibase_GPT_Detailed_Review_Design.md`
  - `GPTs/Altibase_GPT_Document_Selection.md`
  - `GPTs/Altibase_GPT_Attachment_Build_Workplan.md`
  - `GPTs/attachments/README.md`
- Source manuals sampled:
  - `Manuals/Altibase_7.1/eng/JDBC User's Manual.md`
  - `Manuals/Altibase_7.3/eng/JDBC User's Manual.md`
  - `Technical Documents/kor/JavaCompatibility.md`
  - `Manuals/Altibase_7.1/eng/CLI User's Manual.md`
  - `Manuals/Altibase_7.3/eng/CLI User's Manual.md`
  - `Manuals/Altibase_trunk/kor/CLI User's Manual.md`
  - `Manuals/Altibase_7.1/eng/ODBC User's Manual.md`
  - `Manuals/Altibase_7.3/eng/ODBC User's Manual.md`
  - `Manuals/Altibase_7.1/eng/iSQL User's Manual.md`
  - `Manuals/Altibase_7.3/eng/iSQL User's Manual.md`
  - `Manuals/Altibase_7.1/eng/iLoader User's Manual.md`
  - `Manuals/Altibase_7.3/eng/iLoader User's Manual.md`
  - `Manuals/Altibase_trunk/eng/iLoader User's Manual.md`
  - `Manuals/Altibase_7.1/eng/Altibase C Interface Manual.md`
  - `Manuals/Altibase_7.3/eng/Altibase C Interface Manual.md`
  - `Manuals/Altibase_trunk/eng/Precompiler User's Manual.md`
  - `Manuals/Altibase_7.3/eng/Precompiler User's Manual.md`
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`

## Commands Run
```bash
wc -l GPTs/attachments/10_psm_stored_external_procedures.md GPTs/attachments/11_java_jdbc_spring.md GPTs/attachments/12_c_cli_odbc_precompiler.md GPTs/attachments/13_isql_iloader_basic_tools.md
rg -n "jdbc:|Altibase.jdbc|AltibaseConnection|LOB|Temporary LOB|Spring|Hibernate|SQLAlloc|SQLConnect|SQLDriverConnect|SQLFree|SQLBind|SQLFetch|isql|iloader|precompiler|APRE|CLI|ODBC|DSN|URL|Driver|JDK|Java" GPTs/attachments/10_psm_stored_external_procedures.md GPTs/attachments/11_java_jdbc_spring.md GPTs/attachments/12_c_cli_odbc_precompiler.md GPTs/attachments/13_isql_iloader_basic_tools.md
rg -n "AltibaseFailoverCallback|failoverCallback|Event\\.BEGIN|Result\\.GO|/\\* PING \\*/ SELECT 1|lob_null_select|hibernate-community-dialects" "Manuals/Altibase_7.1/eng/JDBC User's Manual.md" "Manuals/Altibase_7.3/eng/JDBC User's Manual.md" GPTs/attachments/11_java_jdbc_spring.md
rg -n "SQLGetLob\\(|SQLPutLob|SQLTrimLob|SQLFreeLob2|SQLEmptyLob|SQLGetLobLength2|CONNTYPE|LongDataCompat" Manuals/Altibase_7.1/eng Manuals/Altibase_7.3/eng Manuals/Altibase_trunk/kor GPTs/attachments/12_c_cli_odbc_precompiler.md -g '*CLI*' -g '*ODBC*' -g '*.md'
rg -n -- "-dry-run|-lightmode|-stmt_prefix|-extra_col_delimiter|use_lob_file|Empty LOB|LOB data of size 0|rule csv" "Manuals/Altibase_7.1/eng/iLoader User's Manual.md" "Manuals/Altibase_7.3/eng/iLoader User's Manual.md" "Manuals/Altibase_trunk/eng/iLoader User's Manual.md" ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md GPTs/attachments/13_isql_iloader_basic_tools.md
rg -n "trunk|/home/|file://|Manuals/Altibase_trunk|github.com/ALTIBASE/Documents|media/|\\.png|\\.gif|TODO|TBD|FIXME" GPTs/attachments/10_psm_stored_external_procedures.md GPTs/attachments/11_java_jdbc_spring.md GPTs/attachments/12_c_cli_odbc_precompiler.md GPTs/attachments/13_isql_iloader_basic_tools.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name README.md | wc -l
git status --short -- GPTs/attachments review/reports/R12_development_interfaces.md
```

## Findings
| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Resolved High | `GPTs/attachments/12_c_cli_odbc_precompiler.md`; `GPTs/attachments/11_java_jdbc_spring.md`; `GPTs/attachments/13_isql_iloader_basic_tools.md` | 98; 81; 70 | Altibase 8.1 Empty LOB interface changes are not captured. The 8.1 release notes add CLI `SQLEmptyLob()` and `SQLGetLobLength2()`, improved iLoader Empty LOB support only with `-lob -use_lob_file=yes`, and improved JDBC Empty LOB support. The current attachments cover ordinary LOBs, Temporary LOBs, and `SQLFreeLob2()`, but do not distinguish this 8.1 Empty LOB behavior from older 7.1/7.3 guidance where zero-length LOB data is documented as handled like `NULL`. | Resolved by H11. The 8.1 Empty LOB interface gap is no longer an open High gate item; remaining rows in this report are Medium/Low follow-ups. |
| Resolved High | `GPTs/attachments/13_isql_iloader_basic_tools.md` | 727 | The CSV cookbook examples use `-rule csv` together with `-f target_table.fmt`, but the 7.1 and 7.3 iLoader manuals state that `-rule csv` cannot be used with delimiter-related options including `-f`, `-t`, `-r`, and `-e`; the caution at line 733 omits `-f`. This makes the user-facing example potentially not version-safe. | Resolved by H12. The iLoader `-rule csv` copy-ready example risk is no longer an open High gate item; remaining rows in this report are Medium/Low follow-ups. |
| Medium | `GPTs/attachments/13_isql_iloader_basic_tools.md` | 527 | The compact iLoader syntax omits documented literal options that are likely retrieval targets: `-dry-run`, `-lightmode`, and 7.1-documented `-stmt_prefix` and `-extra_col_delimiter`. The version block mentions `-lightmode`, but the command syntax and option blocks do not preserve these literals in the main iLoader section. | Add the omitted options with version scope, or label the compact syntax as intentionally partial and add small option blocks for `-dry-run`, `-lightmode`, `-stmt_prefix`, and `-extra_col_delimiter`. |
| Low | `GPTs/attachments/11_java_jdbc_spring.md` | 144 | The SSL/TLS JDBC URL example enables `verify_server_certificate=true` but does not show the truststore attributes needed for private CA deployments. The truststore properties are listed later, so the issue is example completeness rather than a missing literal. | Add an inline note under the SSL/TLS URL example that server verification requires a configured default truststore or explicit `truststore_url` and `truststore_password`, and keep detailed certificate procedure in the SSL/TLS attachment. |

## Source Checks
- Claims checked:
  - JDBC URL shape, `Altibase.jdbc.driver.AltibaseDriver`, `AltibaseConnection`, `/* PING */ SELECT 1`, failover callback constants, statement cache properties, Maven Central availability, Hibernate dialect setup, `lob_null_select`, and Java compatibility were checked against 7.1/7.3 JDBC manuals and the Java compatibility technical document.
  - CLI and ODBC connection strings, handle allocation order, diagnostics, `LongDataCompat`, ODBC support tables, LOB locator functions, `SQLGetLob()` and `SQLPutLob()` position cautions, `SQLTrimLob()`, `SQLFreeLob()`, and 8.1 `SQLFreeLob2()` guidance were checked against CLI/ODBC manuals and 8.1 release notes.
  - iSQL and iLoader command forms, generated file permissions, `ALTIBASE_UT_FILE_PERMISSION`, `ISQL_FILE_PERMISSION`, `ISQL_SECURE_LOGIN_MSG`, iLoader CSV, LOB, bad/log, and performance options were checked against iSQL/iLoader manuals.
  - APRE command options, build/link requirements, host variable rules, indicator variables, multi-connection syntax, LOB file modes, and SQLDA names were sampled against precompiler manuals.
  - Temporary LOB coverage in the PSM attachment was checked against 8.1 release notes and verified-source data dictionary references for `V$TEMPORARY_LOBS`.
- Source coverage:
  - Strong for JDBC, CLI, ODBC, iSQL, iLoader, APRE option names, and common command examples for Altibase 7.1 and 7.3.
  - Adequate for 8.1 interface deltas where release notes and verified trunk sources expose the relevant literals.
- Source gaps:
  - 8.1 full English interface manuals are not available in the sampled set, so some 8.1 interface details rely on release notes and verified-source/trunk material.
  - The iLoader `-rule csv` source language appears internally surprising because it names `-f` as incompatible even though format files are central to many iLoader examples. This needs a targeted maintainer or runtime check before upload.
  - C Interface and APRE were sampled for API/order/literal preservation, not exhaustively line-by-line.

## Oracle-Overlap Decision
- Correctly compressed:
  - Generic SQL and Oracle-overlapping DML are brief. The reviewed attachments focus mostly on Altibase-specific drivers, tools, API names, LOB locators, iSQL/iLoader behavior, APRE, and connection properties.
- Too much generic Oracle material:
  - No significant issue found in this stage.
- Missing Altibase-specific difference:
  - 8.1 Empty LOB interface behavior is missing from the development-interface attachments.
  - The iLoader CSV option compatibility needs Altibase-specific correction before examples are copy-ready.

## Version Checks
- 7.1:
  - JDBC, CLI, ODBC, APRE, iSQL, and iLoader literals are mostly preserved.
  - Older LOB handling around zero-length LOBs should be protected from being applied to 8.1 Empty LOB answers.
- 7.3:
  - Java compatibility, Maven availability, Hibernate LOB defaults, `socket_immediate_close`, iSQL permissions, and iLoader option families are mostly represented.
  - `-lightmode` is mentioned but not included in the iLoader syntax block.
- 8.1:
  - Temporary LOB and `SQLFreeLob2()` are represented.
  - Empty LOB interface changes are not represented for JDBC, CLI, or iLoader and should be added before pass.

## Retrieval And GPT Answer Quality
- Strengths:
  - Attachments 11 and 12 preserve many exact driver, property, API, callback, and LOB locator literals.
  - Attachment 13 gives practical iSQL/iLoader workflows with command templates and troubleshooting paths.
  - Attachment 10 gives clear Temporary LOB and external procedure guidance without overloading ordinary PSM material.
- Risks:
  - Closed by H11: 8.1 Empty LOB answers no longer need to inherit 7.1/7.3 zero-length LOB guidance.
  - Closed by H12: iLoader CSV commands are no longer presented in conflict with manual-stated `-rule csv` option restrictions.
  - Less common iLoader options may be hard to retrieve because some literals are absent from the compact syntax and option blocks.

## Required Follow-Up
- Closed by H11: 8.1 Empty LOB guidance in `11_java_jdbc_spring.md`, `12_c_cli_odbc_precompiler.md`, and `13_isql_iloader_basic_tools.md`.
- Closed by H12: `-rule csv` cookbook commands in `13_isql_iloader_basic_tools.md`.
- Add version-scoped iLoader option literals for `-dry-run`, `-lightmode`, `-stmt_prefix`, and `-extra_col_delimiter`, or clearly mark the compact syntax as partial.
- Optionally clarify the JDBC SSL URL example with truststore requirements while keeping the full SSL/TLS procedure in the dedicated security attachment.
