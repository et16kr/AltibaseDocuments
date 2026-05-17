# J014 CDC, RepMgr, TLS, And Network Design Note

- Job: `J014`
- Scope: `GPTs/attachments/09_replication_ha_cdc.md`, `GPTs/attachments/16_dblink_external_connectors.md`, and `GPTs/attachments/18_security_ssl_tls.md`
- Evidence: `GPTs/reports/answerability_failure_remediation_inventory_20260517.md` J014 rows and `evals/altibase_answerability/questions/replication_cdc_security_network.jsonl`

## Boundary

This job is a retrieval and answer-synthesis remediation pass, not a rewrite of the replication or TLS chapters. The durable structure remains the same: replication, CDC, Log Analyzer, Replication Manager, and network diagnostics stay in `09_replication_ha_cdc.md`; ordinary client/server SSL/TLS and 8.1 replication SSL stay in `18_security_ssl_tls.md`; external connector TLS and CDC boundary notes stay in `16_dblink_external_connectors.md`.

## Source-Backed Fix Classes

- Content gaps: add literal customer-answer tokens that were absent or too hard to retrieve, including `ALA_FAILURE`, `sendq`, `recvq`, lowercase `v$repreceiver`, lowercase `wireshark`, `TCP Dup ACK`, Replication Manager 1.4 package names, `August 31, 2023`, and `BUG-50573`.
- Retrieval gaps: add compact exact-token blocks near the relevant operational sections so lexical retrieval can find CDC, TLS, RepMgr, and network diagnostic answers without pulling unrelated replication state material.
- Answer synthesis gaps: add short templates and stop conditions that force answers to preserve component boundaries: ordinary client/server SSL/TLS versus replication SSL, Log Analyzer CDC versus ordinary table replication, RepMgr GUI convenience versus SQL/runtime verification, and network packet evidence versus replication metadata evidence.

## Safety Rules

- Do not broaden replication SSL beyond Altibase 8.1 verified source.
- Do not combine `FOR ANALYSIS` or `FOR ANALYSIS PROPAGATION` Log Analyzer objects with `USING SSL` or `USING IB`.
- Do not treat `SSL_PORT_NO`, JDBC `port`, ODBC/CLI `PORT`, or `ALTIBASE_SSL_PORT_NO` as replication Receiver ports.
- Do not use `Quick Start` or `QUICKSTART` as a generic network or gap fix; require an explicit decision to skip unsent XLogs.
- Do not request private keys as evidence. Ask for sanitized paths, ownership, permission, certificate subject/issuer/validity, logs, port values, and exact Altibase versions.

## Source Families Used

- Korean Replication Manual 7.3 and Altibase 8.1 verified source for `CREATE REPLICATION`, `USING SSL`, `REPLICATION_SSL_PORT_NO`, multi-host behavior, and Log Analyzer SSL/IB exclusion.
- Korean Log Analyzer User's Manual 7.3 for `ALA_FAILURE`, `ALA_ErrorMgr`, `ALA_GetErrorCode`, `ALA_GetErrorLevel`, `ALA_GetErrorMessage`, `ALA_ERROR_FATAL`, `ALA_ERROR_ABORT`, `ALA_ERROR_INFO`, `Autocommit`, and XLog Sender SQL.
- Korean Replication network check technical document for `v$repreceiver.insert_success_count`, `pstack`, `recvXlog`, `sendCmBlock`, `netstat -nrv`, `sendq`, `recvq`, `tcpdump`, `wireshark`, `REPLICATION_HBT_DETECT_TIME`, and `TCP Dup ACK`.
- Korean Replication Manager 1.4 release notes and tool manual for `August 31, 2023`, `BUG-50573`, package names, JDK/JRE requirements, Altibase 4.3.9 or later compatibility, and version-matched JDBC driver guidance.
- Korean SSL/TLS manuals for 7.1 and Altibase 8.1 verified source for OpenSSL/Heartbleed checks, ODBC/CLI SSL properties, certificate verification behavior, FIPS `ALTIBASE_SSL_LOAD_CONFIG`, and server SSL monitoring.
