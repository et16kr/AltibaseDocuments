# R18 Replication SSL, Network Checks, and TLS Separation

Date: 2026-05-16
Reviewer: Codex
Verdict: Pass

## Scope

- Attachments: `GPTs/attachments/09_replication_ha_cdc.md`; `GPTs/attachments/18_security_ssl_tls.md`
- Supporting reports: `GPTs/reports/8_1_verification.md`; `GPTs/reports/eng_kor_parity.md`
- Source manuals sampled: `Manuals/Altibase_trunk/kor/Replication Manual.md`; `Manuals/Altibase_trunk/kor/SQL Reference.md`; `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`; `Technical Documents/kor/Replication network check.md`; 8.1 release notes for replication SSL confirmation

## Commands Run

```bash
bash review/scripts/run_review_remediation_cycle.sh status
rg -n $'\t(Reviewing|Remediating|ReReviewing|Fail)$' review/review_remediation_cycle_status.tsv
git status --short
sed -n '1,240p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,220p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,260p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
rg -n "SSL|TLS|replication|REPLICATION|network|certificate|REPLICATION_SSL|SSL_ENABLE|PORT|REMOTE|PEER|Receiver|Sender|replication network|handshake" GPTs/attachments/09_replication_ha_cdc.md
rg -n "SSL|TLS|replication|REPLICATION|network|certificate|property|SERVER|CLIENT|Replicated|TLS separation|REPLICATION_SSL|SSL_ENABLE" GPTs/attachments/18_security_ssl_tls.md
rg -n "Altibase 8\.1 verified source|8\.1 verified|trunk|file://|C:/|Altibase_trunk" GPTs/attachments/09_replication_ha_cdc.md GPTs/attachments/18_security_ssl_tls.md
rg -n "USING SSL|REPLICATION_SSL_PORT_NO|SSL_PORT_NO|SSL_ENABLE|REPLICATION_PORT_NO|FOR ANALYSIS|InfiniBand|인피니밴드|SSL|TLS" "Manuals/Altibase_trunk/kor/Replication Manual.md"
rg -n "REPLICATION_SSL_PORT_NO|SSL_PORT_NO|SSL_ENABLE|SSL_CIPHER|SSL_CIPHER_SUITES|SSL_LOAD_CONFIG|REPLICATION_PORT_NO" "Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md"
rg -n "CREATE REPLICATION|USING SSL|FOR ANALYSIS|REPLICATION|SSL" "Manuals/Altibase_trunk/kor/SQL Reference.md"
rg -n "replication SSL|Replication SSL|REPLICATION_SSL_PORT_NO|USING SSL|SSL.*replication|network|REPLICATION_HBT_DETECT_TIME|pstack|tcpdump|V\$REPRECEIVER|8\.1" GPTs/reports/8_1_verification.md GPTs/reports/eng_kor_parity.md "Technical Documents/kor/Replication network check.md"
rg -n "REPLICATION_SSL_PORT_NO|USING SSL" Manuals/Altibase_7.1 Manuals/Altibase_7.3
rg -n "REPLICATION_SSL_PORT_NO|USING SSL" Manuals/Altibase_trunk/eng
rg -n "SSL/TLS|USING SSL|REPLICATION_SSL_PORT_NO|이중화.*SSL|SSL.*이중화" ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md
```

## Findings

No Blocker, High, Medium, or Low findings were found.

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |

## Source Checks

- Claims checked:
  - Altibase 8.1 release notes confirm replication SSL/TLS support, `USING SSL`, and `REPLICATION_SSL_PORT_NO` (`ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md:125`-`:129`; English counterpart `:133`-`:138`).
  - Korean Replication Manual maps SSL replication to the peer `REPLICATION_SSL_PORT_NO`, states omitted `USING` defaults to TCP, and requires prior SSL setup on each replication target server (`Manuals/Altibase_trunk/kor/Replication Manual.md:1106`-`:1123`).
  - Korean Replication Manual examples match the attachment examples for `CREATE REPLICATION ... WITH 'peer', port USING SSL` (`Manuals/Altibase_trunk/kor/Replication Manual.md:1180`-`:1202`).
  - Korean SQL Reference repeats the same port mapping and SSL setup requirement (`Manuals/Altibase_trunk/kor/SQL Reference.md:6872`-`:6890`).
  - Korean General Reference documents `REPLICATION_SSL_PORT_NO` as unsigned integer, default `0`, range `[0, 65535]`, read-only/single-value, with `0` meaning SSL replication cannot connect and SSL setup must already be complete (`Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md:12373`-`:12393`).
  - Korean Replication Manual and SQL Reference state Log Analyzer does not support SSL or InfiniBand communication (`Manuals/Altibase_trunk/kor/Replication Manual.md:1092`-`:1095`; `Manuals/Altibase_trunk/kor/SQL Reference.md:6841`-`:6845`).
  - The network check document supports the attachment playbook checks for `V$REPRECEIVER.INSERT_SUCCESS_COUNT`, `pstack`, `netstat`, binary packet capture from both Sender and Receiver hosts, `REPLICATION_HBT_DETECT_TIME`, and Wireshark packet-loss symptoms (`Technical Documents/kor/Replication network check.md:3`-`:21`, `:38`-`:42`).
- Source coverage:
  - `09_replication_ha_cdc.md` correctly scopes non-SSL TCP, SSL, and IB port selection (`:351`-`:365`), provides a separate Altibase 8.1 SSL example (`:424`-`:492`), records 8.1 SSL as a transport feature rather than a compatibility guarantee (`:1146`-`:1153`), and includes source-backed network triage (`:1279`-`:1320`).
  - `18_security_ssl_tls.md` explicitly separates server/client SSL/TLS from replication SSL (`:28`, `:60`-`:64`, `:101`-`:103`, `:220`-`:223`, `:405`-`:479`) and keeps the replication SSL procedure scoped to Altibase 8.1 verified source (`:411`-`:424`, `:578`-`:586`, `:617`-`:620`).
- Korean/English source conflicts:
  - No technical conflict was found in sampled content. Existing source reports already note that English 8.1 replication/property manuals lack the replication-specific `USING SSL` and `REPLICATION_SSL_PORT_NO` detail, so the attachments correctly use release notes plus Korean manual detail (`GPTs/reports/8_1_verification.md:63`-`:79`; `GPTs/reports/eng_kor_parity.md:67`, `:87`, `:96`).
- Source gaps:
  - No blocker gap for this stage. Mixed-version 8.1-to-older replication SSL compatibility remains unverified and is correctly not inferred by the attachment.

## Oracle-Overlap Decision

- Correctly compressed: Oracle-overlapping DML is not expanded in this stage. The reviewed content stays on Altibase-specific replication transport, properties, TLS setup, and network troubleshooting.
- Too much generic Oracle material: None found.
- Missing Altibase-specific difference: None found for the stage objective.

## Version Checks

- 7.1: `rg` found no `USING SSL` or `REPLICATION_SSL_PORT_NO` in the sampled 7.1/7.3 manual trees. `18_security_ssl_tls.md:84` and `:92` avoid presenting replication SSL as a 7.1 or 7.3 feature.
- 7.3: Correctly treated as ordinary TCP replication unless a supported source says otherwise (`18_security_ssl_tls.md:46`-`:49`, `:86`-`:92`).
- 8.1: Replication SSL is source-backed and labeled as Altibase 8.1 verified source, with syntax, peer-port usage, nonzero local `REPLICATION_SSL_PORT_NO`, prior SSL setup, firewall checks, and Log Analyzer exclusion preserved.

## Retrieval And GPT Answer Quality

- Strengths:
  - The decision map in `18_security_ssl_tls.md` routes replication questions away from ordinary client/server TLS and toward `USING SSL` plus peer `REPLICATION_SSL_PORT_NO`.
  - `09_replication_ha_cdc.md` gives direct SQL examples and operational checks, while `18_security_ssl_tls.md` gives the security-specific prerequisites and troubleshooting block.
  - The network playbook is compact and likely retrievable for symptoms such as replication not starting, replication gap growth, and suspected packet loss.
- Risks:
  - The property mutability detail for `REPLICATION_SSL_PORT_NO` is more explicit in `05_data_types_properties.md` than in the two stage attachments. This is acceptable for this stage because neither reviewed attachment gives a runtime `ALTER SYSTEM SET REPLICATION_SSL_PORT_NO` example, and `18_security_ssl_tls.md` cross-references property-focused content.
  - Production certificate policy, external PKI validation, and vendor confirmation for mixed-version 8.1 SSL replication remain outside the sampled sources.

## Required Follow-Up

- No remediation is required for `GPTs/attachments/09_replication_ha_cdc.md` or `GPTs/attachments/18_security_ssl_tls.md`.
- Keep the existing residual-risk posture: require exact Altibase version/build, topology, target ports, certificate setup, and vendor/source confirmation before advising mixed-version replication SSL deployments.
