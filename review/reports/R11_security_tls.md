# R11 Security and TLS

Date: 2026-05-15
Reviewer: Codex
Verdict: Review Required

## Scope

- Attachments:
  - `GPTs/attachments/18_security_ssl_tls.md`
  - `GPTs/attachments/11_java_jdbc_spring.md`
  - `GPTs/attachments/16_dblink_external_connectors.md`
- Supporting reports:
  - `GPTs/reports/8_1_verification.md`
  - `GPTs/reports/source_audit.md`
  - `GPTs/reports/eng_kor_parity.md`
  - `review/reports/R10_replication_ha_cdc_ssl.md`
- Source manuals sampled:
  - `Manuals/Altibase_7.1/eng/Altibase SSL TLS User's Guide.md`
  - `Manuals/Altibase_7.3/eng/Altibase SSL TLS User's Guide.md`
  - `Manuals/Altibase_trunk/eng/Altibase SSL TLS User's Guide.md`
  - `Manuals/Altibase_7.1/eng/JDBC User's Manual.md`
  - `Manuals/Altibase_7.3/eng/JDBC User's Manual.md`
  - `Manuals/Altibase_trunk/eng/JDBC User's Manual.md`
  - `Manuals/Altibase_7.1/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_7.3/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_trunk/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_trunk/kor/Replication Manual.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_trunk/kor/SQL Reference.md`
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`
  - `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`

## Commands Run

```bash
sed -n '1,240p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,220p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,260p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
wc -l GPTs/attachments/18_security_ssl_tls.md GPTs/attachments/11_java_jdbc_spring.md GPTs/attachments/16_dblink_external_connectors.md
nl -ba GPTs/attachments/18_security_ssl_tls.md | sed -n '1,610p'
nl -ba GPTs/attachments/11_java_jdbc_spring.md | sed -n '1,280p'
nl -ba GPTs/attachments/11_java_jdbc_spring.md | sed -n '620,675p'
nl -ba GPTs/attachments/16_dblink_external_connectors.md | sed -n '1,260p'
find Manuals -path '*Altibase SSL TLS User*Guide.md' -print | sort
rg -n "TLS 1|TLSv|OpenSSL|FIPS|SSL_CIPHER|SSL_LOAD_CONFIG|SSL_PORT_NO|SSL_ENABLE|SSL_CLIENT_AUTHENTICATION|REPLICATION_SSL|USING SSL|ALTIBASE_SSL_PORT_NO" Manuals/Altibase_7.1/eng/Altibase\ SSL\ TLS\ User\'s\ Guide.md Manuals/Altibase_7.3/eng/Altibase\ SSL\ TLS\ User\'s\ Guide.md Manuals/Altibase_trunk/eng/Altibase\ SSL\ TLS\ User\'s\ Guide.md
rg -n "SSL_CIPHER_SUITES|SSL_CIPHERS_SUITES|CIPHER_SUITES|CIPHERS_SUITES" Manuals GPTs review -g '*.md'
rg -n "SSL_LOAD_CONFIG|ALTIBASE_SSL_LOAD_CONFIG|SSL_VERIFY|verify_server_certificate|SSL_CLIENT_AUTHENTICATION|SSL_CAPATH|SSL_CA|ssl_protocols|ciphersuite_list" Manuals/Altibase_7.1 Manuals/Altibase_7.3 Manuals/Altibase_trunk -g '*.md'
rg -n "REPLICATION_SSL_PORT_NO|USING SSL|SSL replication|replication SSL" Manuals ReleaseNotes GPTs/attachments/09_replication_ha_cdc.md GPTs/attachments/18_security_ssl_tls.md -g '*.md'
nl -ba Manuals/Altibase_7.1/eng/Altibase\ SSL\ TLS\ User\'s\ Guide.md | sed -n '236,392p'
nl -ba Manuals/Altibase_7.3/eng/Altibase\ SSL\ TLS\ User\'s\ Guide.md | sed -n '236,400p'
nl -ba Manuals/Altibase_trunk/eng/Altibase\ SSL\ TLS\ User\'s\ Guide.md | sed -n '236,400p'
nl -ba Manuals/Altibase_7.1/eng/Altibase\ SSL\ TLS\ User\'s\ Guide.md | sed -n '472,522p'
nl -ba Manuals/Altibase_7.3/eng/Altibase\ SSL\ TLS\ User\'s\ Guide.md | sed -n '484,534p'
nl -ba Manuals/Altibase_trunk/eng/Altibase\ SSL\ TLS\ User\'s\ Guide.md | sed -n '484,534p'
nl -ba Manuals/Altibase_7.3/eng/General\ Reference-1.Data\ Types\ \&\ Altibase\ Properties.md | sed -n '12420,12635p'
nl -ba Manuals/Altibase_trunk/eng/General\ Reference-1.Data\ Types\ \&\ Altibase\ Properties.md | sed -n '12440,12660p'
rg -n "ssl_protocols" GPTs/attachments/11_java_jdbc_spring.md GPTs/attachments/18_security_ssl_tls.md Manuals/Altibase_7.1/eng/Altibase\ SSL\ TLS\ User\'s\ Guide.md Manuals/Altibase_7.3/eng/Altibase\ SSL\ TLS\ User\'s\ Guide.md Manuals/Altibase_trunk/eng/Altibase\ SSL\ TLS\ User\'s\ Guide.md Manuals/Altibase_7.1/eng/JDBC\ User\'s\ Manual.md Manuals/Altibase_7.3/eng/JDBC\ User\'s\ Manual.md Manuals/Altibase_trunk/eng/JDBC\ User\'s\ Manual.md
nl -ba Manuals/Altibase_trunk/kor/Replication\ Manual.md | sed -n '1106,1130p'
nl -ba Manuals/Altibase_trunk/kor/Replication\ Manual.md | sed -n '1178,1205p'
nl -ba Manuals/Altibase_trunk/kor/General_Reference-1.Data\ Types\ \&\ Altibase\ Properties.md | sed -n '12365,12405p'
nl -ba Manuals/Altibase_trunk/kor/SQL\ Reference.md | sed -n '6868,6894p'
nl -ba ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md | sed -n '130,141p'
nl -ba ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md | sed -n '322,329p'
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name README.md | wc -l
rg -n "trunk|Manuals/|ReleaseNotes|Technical Documents|/home/|file://|C:/|ALTIBASE/Documents|github.com/ALTIBASE/Documents" GPTs/attachments/18_security_ssl_tls.md GPTs/attachments/11_java_jdbc_spring.md GPTs/attachments/16_dblink_external_connectors.md
rg -n "Heartbleed|OPENSSL_NO_HEARTBEATS|Intel-Linux|ssl_protocols|TLS 1\.3|SSL_LOAD_CONFIG|ALTIBASE_SSL_LOAD_CONFIG|REPLICATION_SSL_PORT_NO|USING SSL" GPTs/attachments/18_security_ssl_tls.md GPTs/attachments/11_java_jdbc_spring.md GPTs/attachments/16_dblink_external_connectors.md Manuals/Altibase_7.1/eng/Altibase\ SSL\ TLS\ User\'s\ Guide.md Manuals/Altibase_7.3/eng/Altibase\ SSL\ TLS\ User\'s\ Guide.md Manuals/Altibase_trunk/eng/Altibase\ SSL\ TLS\ User\'s\ Guide.md ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md
```

## Findings

No Blocker findings were identified. The High issues below should be corrected before upload because they affect security cautioning and support-boundary accuracy.

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| High | `GPTs/attachments/18_security_ssl_tls.md` | 76 | The 7.1 version block says Altibase 7.1 uses TLS 1.0 with OpenSSL `0.9.4` through `1.0.2`, but omits the source warning to verify that the installed OpenSSL version is not affected by Heartbleed and the `OPENSSL_NO_HEARTBEATS` check. In a security attachment, this makes legacy 7.1 OpenSSL guidance look less risky than the source manual states. | Add a 7.1-specific caution near the version block and server setup checklist: verify OpenSSL installation and confirm it is not vulnerable to Heartbleed before enabling SSL/TLS; mention `OPENSSL_NO_HEARTBEATS` as the source-provided check. Keep the caution scoped to 7.1-era OpenSSL guidance. |
| High | `GPTs/attachments/18_security_ssl_tls.md` | 101 | The server/client SSL setup is written as a generic procedure but does not preserve the SSL/TLS guide's platform caveat that Altibase JDBC and ODBC SSL connections are currently supported only on Intel-Linux. The attachment asks for OS information at line 31, but retrieval against the setup checklist can still produce production guidance for unsupported OS combinations. | Add a platform support caution in `Core Concepts`, `Version Differences`, or the server/client setup checklist: before production SSL/TLS recommendations, verify the target Altibase version and platform; the SSL/TLS guide states JDBC and ODBC SSL connection support is Intel-Linux scoped. Cross-reference supported-platform guidance rather than extending support claims. |
| Medium | `GPTs/attachments/11_java_jdbc_spring.md` | 229 | The JDBC attribute block lists `ssl_protocols` generically beside `ciphersuite_list`. The SSL/TLS guides show `ssl_protocols` in 7.3 and 8.1-era SSL guidance, but not in the 7.1 SSL/TLS guide or 7.1 JDBC manual. This can lead a GPT to suggest protocol pinning with `ssl_protocols` for Altibase 7.1. | Qualify `ssl_protocols` as 7.3 and 8.1 verified-source guidance in the JDBC attachment. For 7.1, keep JDBC SSL guidance to `ssl_enable`, `port`, `ciphersuite_list`, truststore/keystore properties, and the TLS 1.0/OpenSSL limitations in `18_security_ssl_tls.md`. |

## Source Checks

- Claims checked:
  - Server SSL/TLS setup uses `SSL_ENABLE`, `SSL_PORT_NO`, `SSL_MAX_LISTEN`, `SSL_CIPHER_LIST`, `SSL_CLIENT_AUTHENTICATION`, `SSL_CERT`, `SSL_KEY`, `SSL_CA`, and `SSL_CAPATH` across 7.1, 7.3, and 8.1-era guides.
  - 7.3 and 8.1-era TLS 1.3 guidance is backed by the SSL/TLS guides and General Reference property sections for `SSL_CIPHER_SUITES` and `SSL_LOAD_CONFIG`.
  - The SSL/TLS guide text spells `SSL_CIPHERS_SUITES` in one server setup section, but the General Reference property name is `SSL_CIPHER_SUITES`; the attachment uses the General Reference spelling.
  - JDBC SSL properties `ssl_enable`, `port`, `ciphersuite_list`, `verify_server_certificate`, `keystore_url`, and `truststore_url` are source-backed. `ssl_protocols` is source-backed for 7.3 and 8.1-era SSL guidance, not 7.1.
  - ODBC/CLI and ADO.NET verification defaults and keys match the SSL/TLS guides: `SSL_VERIFY` defaults off for ODBC/CLI, `ssl verify` defaults false for ADO.NET, and production verification requires CA configuration.
  - FIPS handling is correctly scoped to 7.3 and 8.1-era OpenSSL 3.0.8 guidance: server `SSL_LOAD_CONFIG=1` plus ODBC/CLI `ALTIBASE_SSL_LOAD_CONFIG=1`.
  - 8.1 replication SSL is source-backed by release notes and Korean fallback manuals: `USING SSL`, `REPLICATION_SSL_PORT_NO`, peer-port interpretation, and the requirement to complete ordinary SSL/TLS setup first.
- Source coverage:
  - `18_security_ssl_tls.md` has strong coverage of server properties, client interfaces, certificate stores, verification behavior, FIPS setup, monitoring, session close, and 8.1 replication SSL separation.
  - `11_java_jdbc_spring.md` includes the needed JDBC SSL connection keys and cross-references the TLS attachment for certificate procedures.
  - `16_dblink_external_connectors.md` is appropriately cautious: it does not invent connector-specific TLS placement and sends SSL/TLS questions to the JDBC and security attachments.
- Source gaps:
  - English 8.1 replication/property manuals lack full replication SSL detail; existing project reports document release-note plus Korean manual fallback use.
  - This review sampled SSL/TLS, JDBC, property, and replication SSL sources, but did not validate every client utility's full SSL option syntax outside the stage focus.

## Oracle-Overlap Decision

- Correctly compressed:
  - The reviewed files avoid generic Oracle SQL expansion and focus on Altibase-specific TLS, driver, DB Link, connector, and replication SSL behavior.
- Too much generic Oracle material:
  - None found in this stage.
- Missing Altibase-specific difference:
  - Add the Altibase SSL/TLS guide's platform caveat and 7.1 OpenSSL Heartbleed caution.
  - Version-scope JDBC `ssl_protocols` so Altibase 7.1 is not treated like 7.3 or 8.1 for protocol pinning.

## Version Checks

- 7.1:
  - Correctly limited to TLS 1.0-era SSL/TLS, OpenSSL `0.9.4` through `1.0.2`, JRE 1.6 recommendation with JRE 1.5 caveat, and no `SSL_CIPHER_SUITES`, `SSL_LOAD_CONFIG`, or replication SSL.
  - Missing the source Heartbleed/`OPENSSL_NO_HEARTBEATS` caution.
  - Needs clearer exclusion of `ssl_protocols`.
- 7.3:
  - Correctly captures TLS 1.0/1.2/1.3, OpenSSL 3.0.8, Java TLS 1.3 caveats, `SSL_CIPHER_SUITES`, `SSL_LOAD_CONFIG`, and FIPS setup.
  - Replication SSL is not claimed as a 7.3 feature.
- 8.1:
  - General SSL/TLS follows the current SSL/TLS guide baseline.
  - Replication SSL is correctly scoped to Altibase 8.1 verified source and separated from ordinary `SSL_PORT_NO`.
  - English-source replication SSL gaps are covered by the release notes and Korean fallback manuals already documented by project reports.

## Retrieval And GPT Answer Quality

- Strengths:
  - `18_security_ssl_tls.md` has question-oriented sections, reusable answer templates, property blocks, and troubleshooting blocks.
  - Literal tokens such as `SSL_ENABLE`, `SSL_PORT_NO`, `SSL_CIPHER_SUITES`, `SSL_LOAD_CONFIG`, `ALTIBASE_SSL_LOAD_CONFIG`, `verify_server_certificate`, `ssl_protocols`, `USING SSL`, and `REPLICATION_SSL_PORT_NO` are preserved.
  - Replication SSL and ordinary client/server SSL/TLS are repeatedly separated, reducing a high-risk answer confusion.
  - `16_dblink_external_connectors.md` avoids overstating TLS placement for external tools.
- Risks:
  - Retrieval against the 7.1 version block can miss the old-OpenSSL vulnerability warning.
  - Retrieval against the setup checklist can omit platform support checks.
  - Retrieval against the Java/JDBC attachment can over-apply `ssl_protocols` to 7.1.

## Required Follow-Up

- Add the 7.1 Heartbleed and `OPENSSL_NO_HEARTBEATS` caution to `18_security_ssl_tls.md`.
- Add an Intel-Linux/platform support caveat for SSL/TLS JDBC and ODBC guidance in `18_security_ssl_tls.md`.
- Version-scope `ssl_protocols` in `11_java_jdbc_spring.md`, and optionally restate that qualifier in the `18_security_ssl_tls.md` JDBC troubleshooting block.
