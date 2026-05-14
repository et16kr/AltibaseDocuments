# R11 Security and TLS Review

Date: 2026-05-14
Reviewer: Codex
Verdict: Review Required

## Scope

- Stage ID: R11
- Group: G3_Operations
- Attachments reviewed:
  - `GPTs/attachments/18_security_ssl_tls.md`
  - `GPTs/attachments/11_java_jdbc_spring.md`
  - `GPTs/attachments/16_dblink_external_connectors.md`
- Required project context reviewed:
  - `review/Altibase_GPT_Detailed_Review_Design.md`
  - `GPTs/Altibase_GPT_Document_Selection.md`
  - `GPTs/Altibase_GPT_Attachment_Build_Workplan.md`
  - `GPTs/attachments/README.md`
- Source manuals sampled:
  - `Manuals/Altibase_7.1/eng/Altibase SSL TLS User's Guide.md`
  - `Manuals/Altibase_7.3/eng/Altibase SSL TLS User's Guide.md`
  - `Manuals/Altibase_trunk/eng/Altibase SSL TLS User's Guide.md`
  - `Manuals/Altibase_7.1/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_7.3/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_trunk/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`
  - `Manuals/Altibase_trunk/kor/Replication Manual.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
- Supporting reports sampled:
  - `GPTs/reports/eng_kor_parity.md`
  - `GPTs/reports/8_1_verification.md`
  - `review/reports/R10_replication_ha_cdc_ssl.md`

## Commands Run

```bash
sed -n '1,220p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,220p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,260p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
nl -ba GPTs/attachments/18_security_ssl_tls.md | sed -n '1,660p'
nl -ba GPTs/attachments/11_java_jdbc_spring.md | sed -n '1,260p'
nl -ba GPTs/attachments/16_dblink_external_connectors.md | sed -n '1,320p'
rg -n "SSL|TLS|FIPS|certificate|cert|cipher|secure|keystore|truststore|verify|DBLINK|JDBC|jdbc|connection|Replication SSL|replication SSL" GPTs/attachments/18_security_ssl_tls.md GPTs/attachments/11_java_jdbc_spring.md GPTs/attachments/16_dblink_external_connectors.md
rg -n "TLS 1\.3|TLSv1\.3|TLS 1\.2|TLS 1\.0|OpenSSL|FIPS|SSL_CIPHER_SUITES|SSL_LOAD_CONFIG|ALTIBASE_SSL_LOAD_CONFIG|ALTIBASE_SSL_PORT_NO|SSL_VERIFY|ssl_protocols|verify_server_certificate|truststore_url|keystore_url" Manuals/Altibase_7.1/eng/Altibase\ SSL\ TLS\ User\'s\ Guide.md Manuals/Altibase_7.3/eng/Altibase\ SSL\ TLS\ User\'s\ Guide.md Manuals/Altibase_trunk/eng/Altibase\ SSL\ TLS\ User\'s\ Guide.md
rg -n "REPLICATION_SSL_PORT_NO|USING SSL|FOR ANALYSIS|SSL" Manuals/Altibase_trunk/kor/Replication\ Manual.md Manuals/Altibase_trunk/kor/General_Reference-1.Data\ Types\ \&\ Altibase\ Properties.md ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md
rg -n "trunk|Altibase_trunk|file://|/home/|C:\\\\|workstation|internal source|source-tree|media/|\\.png|\\.gif|\\.jpg|\\.jpeg" GPTs/attachments/18_security_ssl_tls.md GPTs/attachments/11_java_jdbc_spring.md GPTs/attachments/16_dblink_external_connectors.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' -print
wc -l GPTs/attachments/18_security_ssl_tls.md GPTs/attachments/11_java_jdbc_spring.md GPTs/attachments/16_dblink_external_connectors.md
```

## Findings

No Blocker or High issues were found.

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Medium | `GPTs/attachments/18_security_ssl_tls.md` | 328 | The FIPS checklist says to set `ALTIBASE_SSL_LOAD_CONFIG=1` on "clients that use OpenSSL." The sampled 7.3 and 8.1 SSL/TLS guides document `ALTIBASE_SSL_LOAD_CONFIG` specifically in the ODBC/CLI FIPS flow and the FIPS summary says to set the `ODBC/CLI` environment variable. The attachment later narrows this correctly in troubleshooting, but this earlier checklist over-broadens the supported client surface. | Change the checklist to say `ALTIBASE_SSL_LOAD_CONFIG=1` for ODBC/CLI clients. For ADO.NET or other OpenSSL-using clients, say to use only source-documented connection-string keys unless a matching guide explicitly documents FIPS loading. |
| Medium | `GPTs/attachments/16_dblink_external_connectors.md` | 34 | The response rule says to use this attachment for SSL/TLS connector property names, but the attachment contains no SSL/TLS property placement for DB Link `TARGETS/CONNECTION_URL`, Sqoop `--connect`, DBeaver, or Hibernate. Retrieval can therefore promise connector-specific SSL help without giving source-backed connector syntax or a clear cross-reference. | Either add a short source-backed connector SSL note for JDBC-based connectors, pointing users to `ssl_enable=true`, the SSL port, `verify_server_certificate`, `truststore_*`, `keystore_*`, `ciphersuite_list`, and `ssl_protocols` where a connector accepts an Altibase JDBC URL/properties, or revise line 34 to say this file does not define connector-specific TLS syntax and the GPT should use `11_java_jdbc_spring.md` and `18_security_ssl_tls.md` for JDBC SSL parameters. |
| Low | `GPTs/attachments/18_security_ssl_tls.md` | 386 | The ADO.NET example is copied from the manual and omits `ssl verify=true`, while the same guide documents `ssl verify` defaulting to `false`. The attachment has verification cautions elsewhere, but a standalone retrieved example could be copied as a production pattern without server certificate verification. | Add a one-sentence caution next to the ADO.NET example: the sample follows the manual, but production server certificate verification requires `ssl verify=true` plus `ssl ca` or `ssl capath`. |

## Source Checks

- Claims checked:
  - Server SSL/TLS properties: `SSL_ENABLE`, `SSL_PORT_NO`, `SSL_MAX_LISTEN`, `SSL_CIPHER_LIST`, `SSL_CIPHER_SUITES`, `SSL_LOAD_CONFIG`, `SSL_CLIENT_AUTHENTICATION`, `SSL_CERT`, `SSL_KEY`, `SSL_CA`, and `SSL_CAPATH`.
  - Client JDBC properties: `ssl_enable`, `port`, `ciphersuite_list`, `ssl_protocols`, `verify_server_certificate`, `keystore_url`, `keystore_type`, `keystore_password`, `truststore_url`, `truststore_type`, and `truststore_password`.
  - ODBC/CLI and ADO.NET properties: `SSL_CA`, `SSL_CAPATH`, `SSL_CERT`, `SSL_KEY`, `SSL_VERIFY`, `SSL_CIPHER`, `conn type=ssl`, `ssl ca`, `ssl capath`, `ssl cert`, `ssl key`, `ssl verify`, and `ssl cipher`.
  - Version differences: 7.1 TLS 1.0 and OpenSSL `0.9.4` through `1.0.2`; 7.3 and 8.1-era TLS 1.0/1.2/1.3, OpenSSL 3.0.8, Java TLS 1.3 cautions, `SSL_CIPHER_SUITES`, and `SSL_LOAD_CONFIG`.
  - Replication SSL separation: `USING SSL`, peer `REPLICATION_SSL_PORT_NO`, and Log Analyzer non-support for SSL/IB.
- Source coverage:
  - Ordinary server/client SSL/TLS is well covered by the 7.1, 7.3, and 8.1 verified-source SSL/TLS guides.
  - Server property defaults and ranges are backed by the General Reference property sections, including `SSL_PORT_NO`, `SSL_MAX_LISTEN`, `SSL_CLIENT_AUTHENTICATION`, `SSL_CIPHER_SUITES`, and `SSL_LOAD_CONFIG`.
  - 8.1 replication SSL is correctly treated as separate from ordinary `SSL_PORT_NO`. The English 8.1 release note confirms `USING SSL` and `REPLICATION_SSL_PORT_NO`; Korean fallback manuals provide the detailed examples and the Log Analyzer limitation.
- Source gaps:
  - The English 8.1 replication manual and SQL Reference sampled here do not carry the full replication SSL detail; the attachment is appropriately relying on release notes plus Korean fallback for that part.
  - The reviewed connector attachment does not yet make the placement of JDBC SSL parameters explicit for external connector workflows.

## Oracle-Overlap Decision

- Correctly compressed: ordinary Oracle-overlapping DML is not expanded in this stage.
- Too much generic Oracle material: none found.
- Missing Altibase-specific difference: connector-specific placement of Altibase JDBC SSL parameters is under-specified in `16_dblink_external_connectors.md`.

## Version Checks

- 7.1: The attachment correctly limits 7.1 to TLS 1.0-era SSL/TLS guidance, OpenSSL `0.9.4` through `1.0.2`, Java/JRE 1.6 recommendation with JRE 1.5 caveat, and no `SSL_CIPHER_SUITES`, `SSL_LOAD_CONFIG`, or replication SSL.
- 7.3: The attachment correctly captures TLS 1.0/1.2/1.3, OpenSSL 3.0.8, Java TLS 1.3 caveats, `SSL_CIPHER_SUITES`, `SSL_LOAD_CONFIG`, FIPS setup, and no replication SSL claim.
- 8.1: The attachment correctly labels ordinary SSL/TLS as Altibase 8.1 verified source and separates replication SSL from client/server SSL. The main residual risk is that replication SSL detail depends on release notes and Korean fallback rather than a complete English manual section.

## Retrieval And GPT Answer Quality

- Strengths:
  - `18_security_ssl_tls.md` is well structured for TLS questions and keeps client/server SSL separate from replication SSL.
  - JDBC connection keys in `11_java_jdbc_spring.md` match the SSL/TLS guide and are concise enough for retrieval.
  - Certificate terminology is generally careful, distinguishing server-only authentication, mutual authentication, truststore, keystore, CA file, CA directory, certificate, and private key.
- Risks:
  - A user asking about FIPS could retrieve the broad line 328 wording and apply `ALTIBASE_SSL_LOAD_CONFIG` beyond the ODBC/CLI surface documented by the guide.
  - A user asking about TLS in DB Link, Sqoop, DBeaver, or Hibernate may retrieve `16_dblink_external_connectors.md` line 34 but not receive connector-specific placement guidance.
  - ADO.NET examples may be copied without `ssl verify=true` unless the GPT also retrieves the verification caution.

## Required Follow-Up

1. Narrow the FIPS client wording in `18_security_ssl_tls.md` to ODBC/CLI, and avoid implying undocumented FIPS-loading behavior for ADO.NET or other OpenSSL clients.
2. Add or revise connector SSL/TLS wording in `16_dblink_external_connectors.md` so connector-specific property placement is source-backed and clear.
3. Add a caution near the ADO.NET SSL/TLS example in `18_security_ssl_tls.md` that production verification requires `ssl verify=true`.

## Residual Risks

- I did not modify the attachments or source manuals, per stage rules.
- I did not exhaustively validate every Java/Spring/connector property outside SSL/TLS scope.
- The 8.1 replication SSL detail remains partly dependent on release notes and Korean fallback sources because the sampled English 8.1 replication manuals lack the full `USING SSL` examples.
