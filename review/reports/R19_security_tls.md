# R19 Security and TLS

Date: 2026-05-16
Reviewer: Codex
Verdict: Pass

## Scope

- Attachments:
  - `GPTs/attachments/18_security_ssl_tls.md`
  - `GPTs/attachments/11_java_jdbc_spring.md`
  - `GPTs/attachments/16_dblink_external_connectors.md`
- Supporting reports:
  - `GPTs/reports/eng_kor_parity.md`
- Source manuals sampled:
  - `Manuals/Altibase_7.1/kor/Altibase SSL TLS User's Guide.md`
  - `Manuals/Altibase_7.3/kor/Altibase SSL TLS User's Guide.md`
  - `Manuals/Altibase_trunk/kor/Altibase SSL TLS User's Guide.md`
  - `Manuals/Altibase_trunk/kor/Replication Manual.md`
  - `Manuals/Altibase_7.1/kor/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_7.3/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_7.1/kor/iSQL User's Manual.md`
  - `Manuals/Altibase_7.3/kor/iSQL User's Manual.md`
  - `Manuals/Altibase_trunk/kor/iSQL User's Manual.md`

## Commands Run

```bash
bash review/scripts/run_review_remediation_cycle.sh status
rg -n $'\t(Reviewing|Remediating|ReReviewing|Fail)$' review/review_remediation_cycle_status.tsv
git status --short
ls -l review/reports/R19_security_tls.md
rg -n "^R19\t|R19|Security and TLS" review/review_remediation_cycle_status.tsv review/review_stage_status.tsv review/review_stages.tsv
sed -n '1,240p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,220p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,220p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
wc -l GPTs/attachments/18_security_ssl_tls.md GPTs/attachments/11_java_jdbc_spring.md GPTs/attachments/16_dblink_external_connectors.md "Manuals/Altibase_7.1/kor/Altibase SSL TLS User's Guide.md" "Manuals/Altibase_7.3/kor/Altibase SSL TLS User's Guide.md" "Manuals/Altibase_trunk/kor/Altibase SSL TLS User's Guide.md" "Manuals/Altibase_trunk/kor/Replication Manual.md" GPTs/reports/eng_kor_parity.md
nl -ba GPTs/attachments/18_security_ssl_tls.md
nl -ba GPTs/attachments/11_java_jdbc_spring.md
nl -ba GPTs/attachments/16_dblink_external_connectors.md
rg -n "SSL|TLS|certificate|cert|CA|private|key|wallet|trust|cipher|FIPS|VERIFY|SSL_|jdbc|URL|DBLINK|LINK|External|Replication" GPTs/attachments/18_security_ssl_tls.md GPTs/attachments/11_java_jdbc_spring.md GPTs/attachments/16_dblink_external_connectors.md
rg -n "SSL_ENABLE|SSL_PORT_NO|SSL_MAX_LISTEN|SSL_CLIENT_AUTHENTICATION|SSL_CIPHER_LIST|SSL_CIPHER_SUITES|SSL_LOAD_CONFIG|SSL_CERT|SSL_KEY|SSL_CA|SSL_CAPATH|ALTIBASE_SSL_LOAD_CONFIG|ALTIBASE_SSL_PORT_NO|verify_server_certificate|ssl_enable|ssl_protocols|ciphersuite_list|keystore|truststore|FIPS|TLS|OpenSSL|JDBC|ODBC|인텔|Linux|Intel|리눅스|Heartbleed|OPENSSL_NO_HEARTBEATS" "Manuals/Altibase_7.1/kor/Altibase SSL TLS User's Guide.md" "Manuals/Altibase_7.3/kor/Altibase SSL TLS User's Guide.md" "Manuals/Altibase_trunk/kor/Altibase SSL TLS User's Guide.md"
rg -n "REPLICATION_SSL_PORT_NO|USING SSL|FOR ANALYSIS|SSL|InfiniBand|IB|REPLICATION_PORT_NO|REPLICATION_IB_PORT_NO|replication.*SSL|SSL.*replication" "Manuals/Altibase_trunk/kor/Replication Manual.md"
rg -n "SSL_CIPHER_SUITES|SSL_CIPHERS_SUITES|REPLICATION_SSL_PORT_NO|SSL_LOAD_CONFIG|SSL_MAX_LISTEN|SSL_CLIENT_AUTHENTICATION|SSL_VERIFY" Manuals/Altibase_7.3/kor Manuals/Altibase_trunk/kor GPTs/attachments/05_data_types_properties.md GPTs/attachments/06_data_dictionary_performance_views.md GPTs/attachments/09_replication_ha_cdc.md GPTs/attachments/12_c_cli_odbc_precompiler.md
sed -n '318,506p' "Manuals/Altibase_7.1/kor/Altibase SSL TLS User's Guide.md"
sed -n '318,506p' "Manuals/Altibase_7.3/kor/Altibase SSL TLS User's Guide.md"
sed -n '318,506p' "Manuals/Altibase_trunk/kor/Altibase SSL TLS User's Guide.md"
sed -n '522,676p' "Manuals/Altibase_7.1/kor/Altibase SSL TLS User's Guide.md"
sed -n '520,676p' "Manuals/Altibase_trunk/kor/Altibase SSL TLS User's Guide.md"
sed -n '12780,12940p' "Manuals/Altibase_7.3/kor/General_Reference-1.Data Types & Altibase Properties.md"
sed -n '13040,13200p' "Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md"
sed -n '12360,12420p' "Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md"
rg -n "ALTIBASE_SSL_PORT_NO|-PORT|SSL_ENABLE|SSL_CA|SSL_CAPATH|SSL_CERT|SSL_KEY|SSL_CIPHER|SSL_VERIFY|CONNTYPE|ssl" Manuals/Altibase_trunk/kor/iSQL\ User\'s\ Manual.md Manuals/Altibase_7.3/kor/iSQL\ User\'s\ Manual.md Manuals/Altibase_7.1/kor/iSQL\ User\'s\ Manual.md
date +%F
git diff --check -- review/reports/R19_security_tls.md
git status --short
rg -n "^Verdict:|^\| (Blocker|High|Medium|Low) \|" review/reports/R19_security_tls.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name README.md | wc -l
git diff --name-only
git diff --no-index --check /dev/null review/reports/R19_security_tls.md
sed -n '1,260p' review/reports/R19_security_tls.md
rg -n "GPTs/attachments/|Manuals/Altibase" review/reports/R19_security_tls.md
```

## Findings

No actionable Blocker, High, Medium, or Low findings were found.

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Note | `GPTs/attachments/18_security_ssl_tls.md` | N/A | No remediation required. The attachment separates ordinary client/server SSL/TLS from Altibase 8.1 verified-source replication SSL, uses literal property and connection key names, and keeps unsupported combinations cautious. | Keep the current separation and source-safe wording. For future edits, continue to check Korean manuals first and avoid extending SSL/TLS support to unverified platforms or connector-specific property names. |

## Source Checks

- Claims checked:
  - 7.1 TLS scope, OpenSSL `0.9.4` through `1.0.2`, Heartbleed/`OPENSSL_NO_HEARTBEATS` caution, and absence of `SSL_CIPHER_SUITES`, `SSL_LOAD_CONFIG`, and replication SSL in the 7.1 source.
  - 7.3 and Altibase 8.1 verified-source TLS 1.0/1.2/1.3 wording, OpenSSL 3.0.8 requirement, Java TLS 1.3 runtime cautions, `SSL_CIPHER_SUITES`, and `SSL_LOAD_CONFIG`.
  - Server property names and defaults for `SSL_ENABLE`, `SSL_PORT_NO`, `SSL_MAX_LISTEN`, `SSL_CLIENT_AUTHENTICATION`, `SSL_CERT`, `SSL_KEY`, `SSL_CA`, `SSL_CAPATH`, `SSL_CIPHER_LIST`, `SSL_CIPHER_SUITES`, and `SSL_LOAD_CONFIG`.
  - JDBC SSL keys `ssl_enable`, `port`, `ciphersuite_list`, `ssl_protocols`, `verify_server_certificate`, `keystore_*`, and `truststore_*`.
  - ODBC/CLI and ADO.NET SSL keys, including `SSL_VERIFY` / `ssl verify`, and FIPS-specific `ALTIBASE_SSL_LOAD_CONFIG`.
  - Altibase 8.1 verified-source replication SSL syntax, `REPLICATION_SSL_PORT_NO`, `USING SSL`, peer-port interpretation, and `FOR ANALYSIS` exclusion from SSL/IB communication.
  - iSQL SSL port precedence and SSL certificate flags for cross-reference consistency.
- Source coverage:
  - Korean SSL/TLS manuals support the attachment's version split: 7.1 TLS 1.0 and OpenSSL 0.9.4-1.0.2; 7.3 and Altibase 8.1 verified source TLS 1.0/1.2/1.3 and OpenSSL 3.0.8.
  - Korean General Reference property sections support the canonical property spelling `SSL_CIPHER_SUITES`, `SSL_LOAD_CONFIG`, `SSL_MAX_LISTEN`, `SSL_CLIENT_AUTHENTICATION`, and `REPLICATION_SSL_PORT_NO`.
  - Korean Replication Manual supports `CREATE REPLICATION ... USING SSL`, peer use of `REPLICATION_SSL_PORT_NO`, ordinary TCP default when `USING` is omitted, and the Log Analyzer `FOR ANALYSIS` SSL/IB restriction.
- Korean/English source conflicts:
  - No conflict requiring attachment remediation was found.
  - The SSL/TLS guide text contains a source typo spelling the TLS 1.3 property as `SSL_CIPHERS_SUITES` in one bullet, but Korean and English General Reference manuals list the canonical property as `SSL_CIPHER_SUITES`; the attachment uses the canonical spelling.
- Source gaps:
  - Live handshake behavior was not tested for JDBC, ODBC/CLI, ADO.NET, iSQL, or utilities.
  - Third-party connector-specific TLS placement remains intentionally out of scope unless the connector accepts the documented Altibase JDBC URL or properties.

## Oracle-Overlap Decision

- Correctly compressed:
  - The scoped attachments do not expand generic SQL or Oracle-overlapping DML. Security content stays focused on Altibase SSL/TLS properties, certificates, connection keys, and replication SSL.
- Too much generic Oracle material:
  - None found in the scoped TLS/security content.
- Missing Altibase-specific difference:
  - None found. The attachment preserves Altibase-specific ports, properties, client key names, FIPS handling, and replication SSL differences.

## Version Checks

- 7.1:
  - Correctly limits TLS guidance to the 7.1 SSL/TLS source baseline and excludes `SSL_CIPHER_SUITES`, `SSL_LOAD_CONFIG`, and replication SSL.
  - Correctly preserves OpenSSL 0.9.4-1.0.2 and Heartbleed/`OPENSSL_NO_HEARTBEATS` cautions.
- 7.3:
  - Correctly reflects TLS 1.0/1.2/1.3, OpenSSL 3.0.8, Java TLS 1.3 runtime cautions, `SSL_CIPHER_SUITES`, `ssl_protocols`, and FIPS `SSL_LOAD_CONFIG` / `ALTIBASE_SSL_LOAD_CONFIG`.
  - Correctly avoids presenting replication SSL as a documented 7.3 feature.
- 8.1:
  - Correctly labels 8.1 material as `Altibase 8.1 verified source`.
  - Correctly separates ordinary client/server SSL/TLS from 8.1 replication SSL using `REPLICATION_SSL_PORT_NO` and `USING SSL`.

## Retrieval And GPT Answer Quality

- Strengths:
  - `18_security_ssl_tls.md` is the correct primary retrieval target for SSL/TLS questions and includes a decision map, version blocks, property blocks, setup checklists, troubleshooting blocks, and answer templates.
  - `11_java_jdbc_spring.md` gives concise JDBC URL and property guidance, then defers certificate and server procedure details to the SSL/TLS attachment.
  - `16_dblink_external_connectors.md` explicitly avoids inventing connector-specific TLS placement and points users back to the JDBC and SSL/TLS attachments.
- Risks:
  - Runtime-specific Java, OpenSSL, platform, and connector behavior still needs target-environment verification before production recommendations.
  - The GPT should not infer that third-party tools support Altibase TLS properties unless the connector consumes the documented Altibase JDBC URL or client property set.

## Required Follow-Up

- No remediation is required for R19.
- Residual risk: before production deployment answers, ask for the exact Altibase version, client interface, OS/platform, Java/OpenSSL version, certificate mode, trust model, and target ports.
