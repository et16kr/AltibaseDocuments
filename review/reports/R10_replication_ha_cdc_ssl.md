# R10 Replication, HA, CDC, Log Analyzer, And Replication SSL

Date: 2026-05-15
Reviewer: Codex
Verdict: Review Required

## Scope

- Attachments:
  - `GPTs/attachments/09_replication_ha_cdc.md`
  - `GPTs/attachments/18_security_ssl_tls.md`
  - `GPTs/attachments/03_sql_ddl_generation.md`
- Supporting reports:
  - `GPTs/reports/source_inventory.md`
  - `GPTs/reports/8_1_verification.md`
  - `GPTs/reports/sql_generation_test_results.md`
  - `review/reports/R02_high_risk_traceability.md`
  - `review/reports/R03_ddl_tablespace_storage.md`
- Source manuals sampled:
  - `Manuals/Altibase_7.1/eng/Replication Manual.md`
  - `Manuals/Altibase_7.3/eng/Replication Manual.md`
  - `Manuals/Altibase_trunk/eng/Replication Manual.md`
  - `Manuals/Altibase_trunk/kor/Replication Manual.md`
  - `Manuals/Altibase_trunk/eng/Log Analyzer User's Manual.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`
  - `Technical Documents/kor/ReplicationCompatibility.md`
  - `Technical Documents/kor/Replication network check.md`

## Commands Run

```bash
sed -n '1,240p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,220p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,260p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
wc -l GPTs/attachments/09_replication_ha_cdc.md GPTs/attachments/18_security_ssl_tls.md GPTs/attachments/03_sql_ddl_generation.md Manuals/Altibase_7.1/eng/Replication\ Manual.md Manuals/Altibase_7.3/eng/Replication\ Manual.md Manuals/Altibase_trunk/eng/Replication\ Manual.md Technical\ Documents/kor/ReplicationCompatibility.md Technical\ Documents/kor/Replication\ network\ check.md
rg -n "^(#|##|###) " GPTs/attachments/09_replication_ha_cdc.md
rg -n "^(#|##|###) " GPTs/attachments/18_security_ssl_tls.md
rg -n "^(#|##|###) |REPLICATION|Replication|replication|CREATE REPLICATION|ALTER REPLICATION|DROP REPLICATION|START REPLICATION|STOP REPLICATION" GPTs/attachments/03_sql_ddl_generation.md
rg -n "SSL|TLS|replication SSL|Replication SSL|REPLICATION_SSL|SSL_" GPTs/attachments/09_replication_ha_cdc.md GPTs/attachments/18_security_ssl_tls.md GPTs/attachments/03_sql_ddl_generation.md
rg -n "XLog|xlog|CDC|Log Analyzer|log analyzer|analysis|analyzer" GPTs/attachments/09_replication_ha_cdc.md GPTs/attachments/18_security_ssl_tls.md GPTs/attachments/03_sql_ddl_generation.md
nl -ba GPTs/attachments/09_replication_ha_cdc.md | sed -n '1,1577p'
nl -ba GPTs/attachments/18_security_ssl_tls.md | sed -n '1,610p'
nl -ba GPTs/attachments/03_sql_ddl_generation.md | sed -n '560,650p'
nl -ba GPTs/attachments/03_sql_ddl_generation.md | sed -n '1819,1925p'
rg -n "USING SSL|REPLICATION_SSL_PORT_NO|SSL|IF NOT EXISTS|UNIX_DOMAIN|FOR ANALYSIS|FOR PROPAGABLE|PROPAGATION|OFFLINE|REPLICATION_DDL_SYNC|REPLICATION_SQL_APPLY_ENABLE|REPLICATION_DDL_ENABLE" Manuals/Altibase_trunk/eng/Replication\ Manual.md ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md Manuals/Altibase_7.1/eng/Replication\ Manual.md Manuals/Altibase_7.3/eng/Replication\ Manual.md
rg -n "USING SSL|REPLICATION_SSL_PORT_NO|replication|Replication SSL|SSL/TLS" ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md
nl -ba Manuals/Altibase_trunk/eng/Replication\ Manual.md | sed -n '3196,3314p'
nl -ba "Manuals/Altibase_trunk/eng/Log Analyzer User's Manual.md" | sed -n '1048,1170p'
nl -ba "Manuals/Altibase_trunk/eng/Log Analyzer User's Manual.md" | sed -n '1248,1335p'
nl -ba Technical\ Documents/kor/ReplicationCompatibility.md | sed -n '1,180p'
nl -ba Technical\ Documents/kor/Replication\ network\ check.md | sed -n '1,100p'
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name README.md | wc -l
rg -n "REPLICATION_DDL_SYNC|REPLICATION_SQL_APPLY_ENABLE|REPLICATION_SSL_PORT_NO|USING SSL|FOR ANALYSIS|UNIX_DOMAIN" GPTs/attachments/09_replication_ha_cdc.md GPTs/attachments/18_security_ssl_tls.md GPTs/attachments/03_sql_ddl_generation.md
rg -n "trunk|Manuals/|ReleaseNotes|Technical Documents|/home/|file://|C:/|ALTIBASE/Documents|github.com/ALTIBASE/Documents" GPTs/attachments/09_replication_ha_cdc.md GPTs/attachments/18_security_ssl_tls.md GPTs/attachments/03_sql_ddl_generation.md
```

## Findings

No Blocker findings were identified. The High issue below should be corrected before upload.

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| High | `GPTs/attachments/09_replication_ha_cdc.md` | 854 | The DDL synchronization procedure is incomplete. It sets `REPLICATION_DDL_SYNC` and `REPLICATION_SQL_APPLY_ENABLE`, but omits required `REPLICATION_DDL_ENABLE` and `REPLICATION_DDL_ENABLE_LEVEL` enable and reset steps on both local and remote servers. It also omits the local `ALTER SESSION SET REPLICATION = DEFAULT` step and says to flush before DDL on the local server only, while the source procedure requires flushing on both local and remote servers. This was also reported in `R03` and remains unresolved. | Replace the DDL synchronization procedure with the full source sequence: verify required conditions, set `REPLICATION_DDL_ENABLE` and `REPLICATION_DDL_ENABLE_LEVEL` on both servers, set local `REPLICATION_DDL_SYNC` with `ALTER SESSION`, set remote `REPLICATION_DDL_SYNC` and `REPLICATION_SQL_APPLY_ENABLE` with `ALTER SYSTEM`, run `ALTER SESSION SET REPLICATION = DEFAULT`, flush both sides, execute DDL once on the local server, then reset every changed property. Add `REPLICATION_DDL_SYNC` to the properties list. |
| Medium | `GPTs/attachments/03_sql_ddl_generation.md`<br>`GPTs/attachments/09_replication_ha_cdc.md` | 593<br>313 | The compact CDC XLog Sender syntax blocks omit the `WITH UNIX_DOMAIN` alternative. `09_replication_ha_cdc.md` later has a UNIX-domain example, but the top syntax block and central DDL-generation attachment can still steer answers toward TCP-only CDC syntax. | Add `WITH UNIX_DOMAIN` as an alternative in both compact syntax blocks, with the existing same-host UNIX/Linux and `$ALTIBASE_HOME` cautions. Keep `USING SSL` and `USING IB` excluded from `FOR ANALYSIS`. |
| Medium | `GPTs/attachments/09_replication_ha_cdc.md` | 1378 | The XLog Sender host-change caution says "Host changes are TCP-only when a UNIX domain connection is used", which is ambiguous. The source says `ADD HOST` is impossible when `UNIX_DOMAIN` was specified, and `ADD HOST`, `DROP HOST`, and `SET HOST` apply only to TCP/IP hosts. | Replace the caution with explicit rules: a UNIX-domain XLog Sender cannot add hosts; host add/drop/set operations are for TCP/IP XLog Collector endpoints only; `SET HOST` takes effect after restart. |
| Medium | `GPTs/attachments/03_sql_ddl_generation.md` | 349 | The table DDL rule says not to generate any `ALTER TABLE` that changes a replication target. That is safe as a default, but too broad for the documented Altibase procedures that allow DDL execution or DDL synchronization under strict properties, protocol, gap, and service-migration conditions. | Reword as "Do not generate ad hoc `ALTER TABLE` for replication targets." Then point to `09_replication_ha_cdc.md` for the standard remove/re-add procedure and the documented DDL synchronization procedure. |

## Source Checks

- Claims checked:
  - 8.1 replication SSL is source-backed by `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md:133`-`138` and `:326`, Korean replication syntax at `Manuals/Altibase_trunk/kor/Replication Manual.md:1106`-`1123` and `:1180`-`1202`, and `REPLICATION_SSL_PORT_NO` property detail at `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md:12373`-`12393`.
  - DDL synchronization requirements are source-backed by `Manuals/Altibase_trunk/eng/Replication Manual.md:3214`-`3218`, `:3257`-`:3273`, `:3276`-`:3290`, and `:3296`-`:3312`.
  - Cross-version compatibility claims match `Technical Documents/kor/ReplicationCompatibility.md:21`-`28`, `:33`-`:45`, `:53`-`:63`, and protocol rows `:104`-`:121`.
  - Network troubleshooting guidance matches `Technical Documents/kor/Replication network check.md:3`-`:21` and `:32`-`:42`.
  - Log Analyzer limitations, API workflow, UNIX-domain syntax, and host restrictions match `Manuals/Altibase_trunk/eng/Log Analyzer User's Manual.md:409`-`:427`, `:650`-`:675`, `:1049`-`:1077`, `:1124`-`:1153`, and `:1248`-`:1335`.
- Source coverage:
  - `09_replication_ha_cdc.md` has strong coverage of topology, modes, HA, compatibility, network checks, DDL restrictions, offline replication, Log Analyzer, and CDC.
  - `18_security_ssl_tls.md` correctly separates ordinary client/server SSL/TLS from 8.1 replication SSL.
  - `03_sql_ddl_generation.md` includes replication DDL examples and version-scoped SSL replication syntax.
- Source gaps:
  - English 8.1 manuals do not carry the full replication SSL detail; the existing 8.1 verification report documents release-note plus Korean fallback use.
  - This review did not validate every replication performance view column against every version's data dictionary. It sampled the views used in the stage attachments.

## Oracle-Overlap Decision

- Correctly compressed:
  - Ordinary DML is not expanded in this stage. The attachments focus on Altibase-specific replication, DDL, CDC, operations, and SSL behavior.
- Too much generic Oracle material:
  - None found in the reviewed stage files.
- Missing Altibase-specific difference:
  - The allowed-but-controlled DDL synchronization path needs to be represented more accurately, instead of only a broad "do not alter replication targets" rule in the DDL generation file.

## Version Checks

- 7.1:
  - Replication, Log Analyzer, compatibility, and non-SSL TCP guidance are represented. Replication SSL is not presented as a 7.1 feature.
- 7.3:
  - Replication compatibility and Log Analyzer guidance are represented. Replication SSL is not presented as a 7.3 feature.
- 8.1:
  - Replication SSL is correctly scoped to Altibase 8.1 verified source, uses `USING SSL`, and uses peer `REPLICATION_SSL_PORT_NO`.
  - General TLS is not confused with replication SSL; `SSL_PORT_NO` and `REPLICATION_SSL_PORT_NO` are repeatedly separated.

## Retrieval And GPT Answer Quality

- Strengths:
  - The SSL material is easy to retrieve and consistently separates application TLS from replication SSL.
  - The replication attachment has customer-answer templates, topology diagrams, operational check SQL, compatibility guidance, network troubleshooting, and Log Analyzer API blocks.
  - Literal tokens such as `CREATE REPLICATION`, `USING SSL`, `REPLICATION_SSL_PORT_NO`, `FOR ANALYSIS`, `ALA_Handshake`, and `V$REPSENDER` are preserved.
- Risks:
  - A GPT could generate an incomplete DDL synchronization procedure because the high-risk property sequence is missing.
  - A GPT could miss or mishandle UNIX-domain Log Analyzer CDC if it retrieves the compact syntax block instead of the later example.
  - A GPT could over-reject replication-target `ALTER TABLE` requests instead of routing them to the documented Altibase procedure.

## Required Follow-Up

- Fix the DDL synchronization procedure in `09_replication_ha_cdc.md`.
- Add `WITH UNIX_DOMAIN` to the compact CDC syntax in `03_sql_ddl_generation.md` and `09_replication_ha_cdc.md`.
- Clarify XLog Sender host-change rules for `UNIX_DOMAIN` versus TCP/IP endpoints in `09_replication_ha_cdc.md`.
- Reword the broad replication-target `ALTER TABLE` prohibition in `03_sql_ddl_generation.md` to point to the documented procedures in `09_replication_ha_cdc.md`.
