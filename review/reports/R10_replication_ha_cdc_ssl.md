# R10 Replication, HA, CDC, Log Analyzer, and Replication SSL Review

Date: 2026-05-14
Reviewer: Codex
Verdict: Review Required

## Scope

- Stage ID: R10
- Group: G3_Operations
- Attachments reviewed:
  - `GPTs/attachments/09_replication_ha_cdc.md`
  - `GPTs/attachments/18_security_ssl_tls.md`
  - `GPTs/attachments/03_sql_ddl_generation.md`
- Required project context reviewed:
  - `review/Altibase_GPT_Detailed_Review_Design.md`
  - `GPTs/Altibase_GPT_Document_Selection.md`
  - `GPTs/Altibase_GPT_Attachment_Build_Workplan.md`
  - `GPTs/attachments/README.md`
- Source materials sampled:
  - `Manuals/Altibase_7.1/eng/Replication Manual.md`
  - `Manuals/Altibase_7.3/eng/Replication Manual.md`
  - `Manuals/Altibase_trunk/eng/Replication Manual.md`
  - `Manuals/Altibase_7.1/eng/Log Analyzer User's Manual.md`
  - `Manuals/Altibase_7.3/eng/Log Analyzer User's Manual.md`
  - `Manuals/Altibase_trunk/eng/Log Analyzer User's Manual.md`
  - `Manuals/Altibase_7.1/eng/Altibase SSL TLS User's Guide.md`
  - `Manuals/Altibase_7.3/eng/Altibase SSL TLS User's Guide.md`
  - `Manuals/Altibase_trunk/eng/Altibase SSL TLS User's Guide.md`
  - `Technical Documents/kor/ReplicationCompatibility.md`
  - `Technical Documents/kor/Replication network check.md`
  - `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`

## Findings

| Severity | File | Line | Finding | Recommendation |
|---|---|---:|---|---|
| High | `GPTs/attachments/09_replication_ha_cdc.md` | 20 | The Active-Active overview says it "guarantees sub-millisecond latency and built-in conflict resolution." This is not supported by the replication manuals and is risky for GPT retrieval. The source describes LAZY replication as potentially delayed with lower consistency, states that replication cannot guarantee consistency when conflicts occur, and warns that different updates to the same row in Active-Active can leave different values. | Replace the claim with conservative guidance: Active-Active is possible, but requires explicit write ownership, conflict avoidance, and monitoring. Do not promise sub-millisecond latency or guaranteed conflict resolution. Mention that conflict handling schemes exist but do not guarantee global consistency. |
| High | `GPTs/attachments/09_replication_ha_cdc.md` | 819 | The DDL section is labeled as a standard procedure but mixes property-based DDL/SQL apply guidance with a simplified "execute same DDL on both nodes" flow. It omits the documented standard procedure steps such as service stop or `ADMIN_MODE`, `REP_GAP=0` verification, stopping replication, dropping and re-adding replication targets, and the DDL sync-specific local/remote property sequence. | Split this into two clearly named procedures. First, document the standard no-special-property procedure from Appendix B: stop service or enter admin flow, flush and verify `REP_GAP=0`, stop replication, drop targets from all replication objects, run DDL on all nodes, add targets, and restart. Second, document DDL synchronization separately: local `ALTER SESSION SET REPLICATION_DDL_SYNC = 1`, remote `ALTER SYSTEM SET REPLICATION_DDL_SYNC = 1` and `REPLICATION_SQL_APPLY_ENABLE = 1`, flush both sides, execute DDL on the local server only, then restore properties. Include the documented restrictions for EAGER and recovery options. |
| High | `GPTs/attachments/03_sql_ddl_generation.md` | 1819 | Several replication DDL examples run `ALTER REPLICATION ... SYNC` inside each node's setup block. If followed sequentially, the first `SYNC` can occur before the peer replication object exists, which conflicts with the manual requirement to create matching replication objects on both servers before starting replication. Running `SYNC` from both directions also risks being copied as a default Active-Active initialization pattern. | Move `SYNC` and `START` commands after both peer `CREATE REPLICATION` statements. Add a short note that the initial alignment/start direction must be chosen based on Active-Standby versus Active-Active ownership and existing data. Mirror the safer ordering already used in `09_replication_ha_cdc.md`. |
| Medium | `GPTs/attachments/09_replication_ha_cdc.md` | 19 | The file opens with a sharding overview and mentions `ShardManager`, but this stage attachment is for replication, HA, CDC, and Log Analyzer behavior. The sampled replication sources do not support this as part of the stage topic, and it can pollute retrieval for replication/HA questions. | Remove the sharding overview from this attachment or replace it with a minimal cross-reference to a sharding attachment if that content is source-backed elsewhere. Keep this file focused on replication, HA, CDC, Log Analyzer, and replication SSL. |

## Source Checks

- Replication SSL separation was checked against `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md:125` and `:308`. The attachments correctly distinguish 8.1 replication SSL (`REPLICATION_SSL_PORT_NO`, `USING SSL`) from ordinary client/server SSL (`SSL_PORT_NO`) and do not claim replication SSL support for 7.1 or 7.3.
- General SSL/TLS guidance in `18_security_ssl_tls.md` matches the SSL/TLS user guides at a high level: 7.1 is older TLS/OpenSSL guidance, while 7.3 and 8.1-era documentation include TLS 1.0/1.2/1.3, OpenSSL 3.0.8, `SSL_CIPHER_SUITES`, `SSL_LOAD_CONFIG`, and FIPS-related handling. No confusion with replication SSL was found.
- Active-Active claims were checked against `Manuals/Altibase_trunk/eng/Replication Manual.md:470`, `:657`, and `:1018`. The attachment overstates latency and conflict behavior.
- Replication DDL guidance was checked against `Manuals/Altibase_trunk/eng/Replication Manual.md:1966`, `:3222`, `:3253`, `:3286`, and `:5108`. The current attachment DDL procedure is too compressed and blends distinct documented procedures.
- Replication object creation and start ordering were checked against `Manuals/Altibase_trunk/eng/Replication Manual.md:548` and `:1023`, plus the corresponding 7.3 replication syntax area. The manual requires matching objects on both servers before replication starts.
- Compatibility guidance in `09_replication_ha_cdc.md` broadly aligns with `Technical Documents/kor/ReplicationCompatibility.md`, especially the emphasis on exact version and replication protocol checks before 8.1-to-older-node replication.
- Network troubleshooting guidance was checked against `Technical Documents/kor/Replication network check.md`; the attachment covers directional checks, `netstat`, `tcpdump`, and heartbeat-related troubleshooting.
- Log Analyzer / CDC guidance was checked against the Log Analyzer manuals. The attachment preserves the key constraints: SYS execution, analyzed table primary key requirement, DDL limitation, sender limit, matching protocol version, TCP/UNIX socket transport, LAZY-only behavior, and `START AT SN` prerequisites.

## Oracle-Overlap Decision

- Correctly compressed: ordinary Oracle-overlapping DML is not expanded in this stage.
- Too generic: no major generic Oracle content issue was found.
- Missing or risky Altibase-specific detail: the DDL procedure and replication initialization examples need source-accurate Altibase ordering and restrictions.

## Version Checks

- 7.1: Replication and Log Analyzer coverage is generally version-aware; no replication SSL support is implied.
- 7.3: Replication and SSL/TLS coverage is generally version-aware; no replication SSL support is implied.
- 8.1: Replication SSL is separated from general TLS correctly. The main 8.1-era risk is not SSL confusion, but the unsafe replication DDL procedure and the overconfident Active-Active statement.

## Retrieval Quality

- Strengths: `09_replication_ha_cdc.md` has useful task-oriented sections for compatibility checks, network troubleshooting, Log Analyzer, and 8.1 replication SSL. `18_security_ssl_tls.md` clearly keeps general SSL/TLS separate from replication SSL.
- Risks: the unsupported Active-Active sentence appears near the top of `09_replication_ha_cdc.md` and is likely to be retrieved as authoritative. The DDL procedure block and `03_sql_ddl_generation.md` examples are likely to be copied as operational runbooks, so they need precise ordering and restrictions.

## Validation Commands

Lightweight read-only validation and review commands run during this stage included:

```bash
sed -n '1,240p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,220p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,260p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
wc -l GPTs/attachments/09_replication_ha_cdc.md GPTs/attachments/18_security_ssl_tls.md GPTs/attachments/03_sql_ddl_generation.md
rg -n "REPLICATION_SSL_PORT_NO|USING SSL|SSL_PORT_NO|FOR ANALYSIS|Log Analyzer|REPLICATION_DDL|REPLICATION_DDL_SYNC|Active-Active|sub-millisecond" GPTs/attachments Manuals ReleaseNotes "Technical Documents"
rg -n "trunk|file://|/home/|C:\\\\|Altibase_trunk|internal" GPTs/attachments/09_replication_ha_cdc.md GPTs/attachments/18_security_ssl_tls.md GPTs/attachments/03_sql_ddl_generation.md
nl -ba GPTs/attachments/09_replication_ha_cdc.md | sed -n '1,220p'
nl -ba GPTs/attachments/09_replication_ha_cdc.md | sed -n '760,860p'
nl -ba GPTs/attachments/03_sql_ddl_generation.md | sed -n '1800,1865p'
nl -ba GPTs/attachments/18_security_ssl_tls.md | sed -n '395,485p'
nl -ba Manuals/Altibase_trunk/eng/Replication\ Manual.md | sed -n '620,720p'
nl -ba Manuals/Altibase_trunk/eng/Replication\ Manual.md | sed -n '3220,3410p'
nl -ba Manuals/Altibase_trunk/eng/Replication\ Manual.md | sed -n '5106,5488p'
nl -ba ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md | sed -n '120,135p'
```

## Required Follow-Up

1. Replace the unsupported Active-Active latency/conflict guarantee in `09_replication_ha_cdc.md`.
2. Rewrite the replication DDL guidance in `09_replication_ha_cdc.md` as separate standard and DDL sync procedures.
3. Reorder the replication examples in `03_sql_ddl_generation.md` so both peer replication objects are created before any `SYNC` or `START`.
4. Remove or relocate the sharding overview from `09_replication_ha_cdc.md`.

## Residual Risks

- I did not modify the attachments or source manuals, per stage rules.
- I did not exhaustively validate every replication SQL example in the full 1,546-line replication attachment; the review concentrated on the requested topology, compatibility, network, DDL, CDC/log analysis, and replication SSL areas.
- The 8.1 replication SSL source appears in release notes rather than a full English replication manual section in the sampled tree, so the report treats release notes as the authoritative source for `USING SSL` and `REPLICATION_SSL_PORT_NO`.
