# R12 Development Interfaces Review

Date: 2026-05-14
Reviewer: Codex
Verdict: Review Required

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
  - `Manuals/Altibase_trunk/eng/JDBC User's Manual.md`
  - `Manuals/Altibase_7.1/eng/CLI User's Manual.md`
  - `Manuals/Altibase_trunk/eng/CLI User's Manual.md`
  - `Manuals/Altibase_7.1/eng/ODBC User's Manual.md`
  - `Manuals/Altibase_7.1/eng/Altibase C Interface Manual.md`
  - `Manuals/Altibase_7.3/kor/API User's Manual.md`
  - `Manuals/Altibase_trunk/kor/CLI User's Manual.md`
  - `Technical Documents/kor/JavaCompatibility.md`
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`

## Commands Run

```bash
sed -n '1,240p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,220p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,260p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
nl -ba GPTs/attachments/10_psm_stored_external_procedures.md | sed -n '1,1220p'
nl -ba GPTs/attachments/11_java_jdbc_spring.md | sed -n '1,1120p'
nl -ba GPTs/attachments/12_c_cli_odbc_precompiler.md | sed -n '1,1700p'
nl -ba GPTs/attachments/13_isql_iloader_basic_tools.md | sed -n '1,1320p'
rg -n "PING|/\\* PING \\*/ SELECT 1|poolPingQuery|validationQuery" Manuals/Altibase_7.1 GPTs/attachments/11_java_jdbc_spring.md
rg -n "jdbc:Altibase|alternateservers|connectionretrycount|sessionfailover|lob_null_select|stmt_cache|truststore|verify_server_certificate" "Manuals/Altibase_7.1/eng/JDBC User's Manual.md" GPTs/attachments/11_java_jdbc_spring.md
rg -n "SQLGetLob\\(|SQLPutLob\\(|fromPosition|SQLTrimLob\\(" GPTs/attachments/12_c_cli_odbc_precompiler.md "Manuals/Altibase_trunk/eng/CLI User's Manual.md" "Manuals/Altibase_7.1/eng/CLI User's Manual.md"
rg -n "SQLFreeLob2|stmt_cache_enable|stmt_cache_size|stmt_cache_sql_limit" Manuals/Altibase_trunk ReleaseNotes GPTs/attachments/11_java_jdbc_spring.md GPTs/attachments/12_c_cli_odbc_precompiler.md
rg -n "ALTIBASE_UT_FILE_PERMISSION|ISQL_FILE_PERMISSION|ILO_FILE_PERMISSION|ISQL_SECURE_LOGIN_MSG" Manuals/Altibase_7.1 Manuals/Altibase_7.3 Manuals/Altibase_trunk GPTs/attachments/13_isql_iloader_basic_tools.md
rg -n "trunk|/home/|file://|Manuals/Altibase_trunk|workstation|repository|internal source" GPTs/attachments/10_psm_stored_external_procedures.md GPTs/attachments/11_java_jdbc_spring.md GPTs/attachments/12_c_cli_odbc_precompiler.md GPTs/attachments/13_isql_iloader_basic_tools.md
rg -n "http://|https://|\\.png|\\.jpg|\\.gif|\\.svg|!\\[|media/|PDF/" GPTs/attachments/10_psm_stored_external_procedures.md GPTs/attachments/11_java_jdbc_spring.md GPTs/attachments/12_c_cli_odbc_precompiler.md GPTs/attachments/13_isql_iloader_basic_tools.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name README.md | wc -l
```

## Findings

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| High | `GPTs/attachments/12_c_cli_odbc_precompiler.md` | 936 | The `SQLGetLob()` `fromPosition` guidance does not preserve the formal manual rule that the start point begins at `1`. The 7.1 and 8.1-source CLI manuals document `SQLGetLob()` `fromPosition` as "It begins at 1", while the attachment only says the sample loop starts with offset `0`. This can produce off-by-one LOB reads in generated C examples. | State the formal rule explicitly: `SQLGetLob()` `fromPosition` is documented as 1-based. If retaining the manual sample convention that initializes the first loop offset to `0`, label it as a source-sample inconsistency and advise testing against the target client patch before generating partial-read code. |
| High | `GPTs/attachments/12_c_cli_odbc_precompiler.md` | 947 | The `SQLPutLob()` position rule omits the documented 1-based `fromPosition` definition and instead emphasizes `fromPosition=0` examples for new or whole-value patterns. `SQLTrimLob()` is correctly documented separately as 0-based at line 954, so the current wording risks mixing `SQLTrimLob()` semantics into `SQLPutLob()` partial update examples. | Split the LOB position rules by API: `SQLGetLob()` and `SQLPutLob()` are documented as beginning at `1`; `SQLTrimLob()` begins at `0`. If examples use `0` for full replacement or empty LOB cases, explain that separately and do not use a generic `position` placeholder without the base rule. |
| Medium | `GPTs/attachments/12_c_cli_odbc_precompiler.md` | 1687 | The "Additional API Interfaces" block says Altibase provides "full support" for PHP/PDO, ADO.NET, XA, CheckServer API, and iLoader API. The API User's Manual has important constraints, including unsupported PDO APIs, CheckServer local/single-process restrictions, ADO.NET unsupported interfaces, platform and version requirements, and package-specific limitations. This overstates support and is outside this attachment's stated source list. | Replace "full support" with a constrained cross-reference such as "additional API families exist; check the API User's Manual and version/platform limits before use." Add one-line cautions for PDO, ADO.NET, CheckServer API, and iLoader API, or remove the block from this attachment and leave the details to the API/tool-specific attachment. |

## Source Checks

- Claims checked:
  - JDBC driver class, `jdbc:Altibase://server_ip:server_port/dbname`, URL property syntax, IPv6 form, DataSource search order, failover attributes, SSL/TLS properties, `lob_null_select`, PING validation query, Java 8 time mappings, JDBC 4.2 unsupported NCLOB/LOB-creation APIs, statement caching, and Atomic Batch.
  - Java compatibility for Altibase 7.1 and 7.3 from the Java compatibility technical note, plus Altibase 8.1 JDK and JDBC statement-cache release-note coverage.
  - Spring Boot/Hibernate 6.4 and pre-6.4 dialect setup, including `hibernate-community-dialects` and `spring.jpa.properties.hibernate.jdbc.lob.non_contextual_creation=true`.
  - CLI/ODBC call order, `SQLDriverConnect()` connection strings, ODBC 3.51 support table, `LongDataCompat`, CLI LOB locator APIs, `SQLFreeLob2()` JSON cleanup, ACI function flow, APRE command/options/host-variable syntax, and iSQL/iLoader command examples.
- Source coverage:
  - Strong for JDBC, Spring/Hibernate, CLI, ODBC, ACI, APRE, iSQL, and iLoader ordinary workflows.
  - Strong for 8.1 statement caching and JSON LOB cleanup, with release-note and verified-source support.
  - The stage attachments preserve most literal API names, options, commands, properties, and paths.
- Source gaps:
  - No live Altibase client/server was available, so examples were source-reviewed but not executed.
  - The CLI manuals themselves contain an apparent inconsistency: `SQLGetLob()`/`SQLPutLob()` argument tables say `fromPosition` begins at `1`, while some examples pass `0`. The attachment should expose that nuance rather than smoothing it away.
  - The "Additional API Interfaces" block needs a source audit or reduced wording because it summarizes API families with known limitations.

## Oracle-Overlap Decision

- Correctly compressed:
  - Generic Java/JDBC, ODBC, embedded SQL, and iSQL/iLoader workflows are kept practical and focused on Altibase-specific tokens and behavior.
- Too much generic Oracle material:
  - None significant in this stage.
- Missing Altibase-specific difference:
  - The LOB position-base distinction for `SQLGetLob()`, `SQLPutLob()`, and `SQLTrimLob()` needs to be explicit because general ODBC knowledge will not recover it.

## Version Checks

- 7.1:
  - JDBC URL, PING query, `lob_null_select=off` Hibernate caution, CLI/ODBC LOB APIs, ODBC support table, ACI, APRE, and iSQL/iLoader core command examples were source-supported.
  - LOB offset wording needs correction for 7.1 as noted above.
- 7.3:
  - Java compatibility, Maven dependency example, Hibernate 6.4 guidance, iSQL generated-file permissions, and iLoader package-specific option cautions were source-supported.
- 8.1:
  - Statement caching, native JSON caution, Temporary LOB caution, `SQLFreeLob2()`, and 8.1-safe source labeling were generally supported.
  - No internal `trunk` labels were found in the reviewed attachment text.

## Retrieval And GPT Answer Quality

- Strengths:
  - The attachments are highly searchable, with literal driver classes, URLs, connection properties, commands, API names, SQLSTATE values, and version blocks.
  - JDBC/Spring, CLI/ODBC/ACI/APRE, and iSQL/iLoader answer templates should retrieve well for common customer questions.
  - Utility examples include operational cautions for credentials, file permissions, LOB imports, Direct-Path INSERT, and replication impact.
- Risks:
  - LOB partial read/update answers could be wrong by one byte/character position if the `fromPosition` base is not clarified.
  - The "full support" phrasing for additional APIs may cause broad, unsupported answers for PHP/PDO or ADO.NET instead of version- and API-specific guidance.
  - Source-reviewed utility commands were not executed against installed Altibase clients.

## Required Follow-Up

- Correct `GPTs/attachments/12_c_cli_odbc_precompiler.md` LOB position guidance for `SQLGetLob()`, `SQLPutLob()`, and `SQLTrimLob()`.
- Constrain or remove the "Additional API Interfaces" block in `GPTs/attachments/12_c_cli_odbc_precompiler.md`.
- After fixes, rerun targeted `rg` checks for `fromPosition`, `SQLGetLob`, `SQLPutLob`, `SQLTrimLob`, `SQLFreeLob2`, `PHP`, `PDO`, `ADO.NET`, `CheckServer`, and `iLoader API`.
