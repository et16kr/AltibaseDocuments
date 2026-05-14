# R08 Troubleshooting and Error Response Quality

Date: 2026-05-14
Reviewer: Codex
Verdict: Review Required

## Scope

- Attachments:
  - `GPTs/attachments/07_error_messages_troubleshooting.md`
  - `GPTs/attachments/06_data_dictionary_performance_views.md`
  - `GPTs/attachments/08_performance_tuning_monitoring.md`
- Supporting reports:
  - `GPTs/reports/8_1_verification.md`
- Source manuals sampled:
  - `Manuals/Altibase_7.1/eng/Error Message Reference.md`
  - `Manuals/Altibase_7.3/eng/Error Message Reference.md`
  - `Manuals/Altibase_trunk/eng/Error Message Reference.md`
  - `Manuals/Altibase_trunk/kor/Error Message Reference.md`
  - `Manuals/Altibase_7.3/eng/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_trunk/eng/General Reference-2.The Data Dictionary.md`

## Commands Run

```bash
sed -n '1,240p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,220p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,260p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
wc -l GPTs/attachments/07_error_messages_troubleshooting.md GPTs/attachments/06_data_dictionary_performance_views.md GPTs/attachments/08_performance_tuning_monitoring.md
rg -n "^(#|##|###|####) " GPTs/attachments/07_error_messages_troubleshooting.md
rg -n "^(#|##|###|####) " GPTs/attachments/06_data_dictionary_performance_views.md
rg -n "^(#|##|###|####) " GPTs/attachments/08_performance_tuning_monitoring.md
nl -ba GPTs/attachments/07_error_messages_troubleshooting.md | sed -n '23,180p'
nl -ba GPTs/attachments/07_error_messages_troubleshooting.md | sed -n '1145,1495p'
nl -ba GPTs/attachments/06_data_dictionary_performance_views.md | sed -n '980,1124p;1209,1368p;1431,1518p;1777,1817p'
nl -ba GPTs/attachments/08_performance_tuning_monitoring.md | sed -n '26,75p;1632,1940p;2202,2245p'
rg -n "qpERR_ABORT_QDB_TEMPORARY_TABLE_DDL_DISABLE|smERR_ABORT_smcExceedLockTimeWait|smERR_ABORT_NOT_ENOUGH_SPACE|rpERR_ABORT_RP_READ_SOCKET|rpERR_ABORT_RP_SENDER_HANDSHAKE|cmERR_ABORT_UNSUPPORTED_OPENSSL_VERSION|idERR_FATAL_idc_SVC_INET_BIND_ERROR" Manuals/Altibase_7.1/eng/Error\ Message\ Reference.md Manuals/Altibase_7.3/eng/Error\ Message\ Reference.md Manuals/Altibase_trunk/eng/Error\ Message\ Reference.md
rg -n "0x61100|RPC_DUPLICATE_REPLICATION|Duplicate replication names" Manuals/Altibase_7.1/eng/Error\ Message\ Reference.md Manuals/Altibase_7.3/eng/Error\ Message\ Reference.md Manuals/Altibase_trunk/eng/Error\ Message\ Reference.md
rg -n "QCM_NOT_EXIST_COLUMN|QCM_NOT_EXISTS_INDEX|QCM_REPL_NOT_FOUND|Undefined replication name|Column not found|Index not found|Sequence not found" Manuals/Altibase_7.3/eng/Error\ Message\ Reference.md Manuals/Altibase_trunk/eng/Error\ Message\ Reference.md Manuals/Altibase_7.1/eng/Error\ Message\ Reference.md
rg -n "mtERR_ABORT_PCRE2_NOT_SUPPORTED_ENCODING|mtERR_ABORT_PCRE2_UNEXPECTED_ERROR|mtERR_ABORT_JSON_WITHOUT_TEMPLOB|qpERR_ABORT_JSON_" Manuals/Altibase_trunk/eng/Error\ Message\ Reference.md Manuals/Altibase_trunk/kor/Error\ Message\ Reference.md
awk 'NR>=328 { if(/^### Error Block:/){blocks++} if(/^Error Code:/){ec++} if(/^Reference Symbol:/){rs++} if(/^Module \/ Severity:/){ms++} if(/^Message:/){msg++} if(/^Applies To:/){app++} if(/^Symptom:/){sym++} if(/^Primary Causes:/){cause++} if(/^Immediate Action:/){act++} if(/^Check SQL or Command:/){chk++} if(/^Version Cautions:/){ver++} if(/^Related Document:/){doc++} } END{print "blocks=" blocks; print "Error Code=" ec; print "Reference Symbol=" rs; print "Module / Severity=" ms; print "Message=" msg; print "Applies To=" app; print "Symptom=" sym; print "Primary Causes=" cause; print "Immediate Action=" act; print "Check SQL or Command=" chk; print "Version Cautions=" ver; print "Related Document=" doc}' GPTs/attachments/07_error_messages_troubleshooting.md
rg -n "Symptom:|Primary Causes:|Immediate Action:|Check SQL or Command:|Escalat|contact support|Altibase.*Support" GPTs/attachments/07_error_messages_troubleshooting.md GPTs/attachments/06_data_dictionary_performance_views.md GPTs/attachments/08_performance_tuning_monitoring.md
git status --short -- GPTs/attachments review/reports/R08_troubleshooting_errors.md review
```

## Findings

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| High | `GPTs/attachments/07_error_messages_troubleshooting.md` | 1255 | The duplicate replication block uses runtime views `V$REPSENDER` and `V$REPGAP` as the diagnostic query for `rpERR_ABORT_RPC_DUPLICATE_REPLICATION`. The 7.3 and 8.1 source action explicitly says to consult meta tables to find replications using the same name, IP address, and port. Runtime views may miss stopped or not-yet-started definitions and can produce a false negative for a DDL creation error. | Change this block to use `SYSTEM_.SYS_REPLICATIONS_` and `SYSTEM_.SYS_REPL_HOSTS_` as the primary checks, reusing the query pattern in `06_data_dictionary_performance_views.md` lines 1211-1245. Keep `V$REPSENDER`/`V$REPGAP` only as secondary runtime checks after a definition is known to exist. |
| High | `GPTs/attachments/07_error_messages_troubleshooting.md` | 759 | The "User, Table, Column, Sequence, Index, or Replication Not Found" block merges six error families but its check SQL only verifies `SYSTEM_.SYS_USERS_` and `SYSTEM_.SYS_TABLES_`. Source actions for `Column not found`, `Index not found`, and replication-not-found errors require `DESC`/column checks, index meta checks, or replication meta checks. | Split this into subcases or add branch-specific diagnostics: `SYSTEM_.SYS_COLUMNS_` for columns, `SYSTEM_.SYS_INDICES_` and `SYSTEM_.SYS_INDEX_COLUMNS_` for indexes, `SYSTEM_.SYS_REPLICATIONS_` and `SYSTEM_.SYS_REPL_HOSTS_` for replication, and the existing `SYS_TABLES_`/`V$SEQ` pattern for sequences. |
| High | `GPTs/attachments/07_error_messages_troubleshooting.md` | 983 | The regular expression block combines `mtERR_ABORT_PCRE2_NOT_SUPPORTED_ENCODING` and `mtERR_ABORT_PCRE2_UNEXPECTED_ERROR`, but the action only covers the unsupported-character-set path. The source for `mtERR_ABORT_PCRE2_UNEXPECTED_ERROR` says to check the detailed error message and contact Altibase Support, so the current block can under-escalate unexpected PCRE2 failures. | Separate the two codes or add a clear branch: for `0x2106B`, check PCRE2-supported character sets, `REGEXP_MODE`, and server character set; for `0x2106C`, collect the PCRE2 detail, version, SQL, `REGEXP_MODE`, character set, and trace context before escalation to support. |
| Medium | `GPTs/attachments/07_error_messages_troubleshooting.md` | 34 | The standard response format includes symptom, cause, action, check SQL/command, and version cautions, but no explicit `Escalation` or `Escalate When` field even though this stage requires escalation quality. The file has a general support-collection rule at line 31, but individual blocks do not tell the GPT when to stop and escalate. | Add an `Escalation:` field to the standard format and high-risk blocks. Use it for `FATAL` errors, source actions that say to contact support, repeated replication/socket failures after network checks, SSL certificate/private-key ambiguity, DB Link global transaction failures, and any case where trace-log error numbers are required. |
| Medium | `GPTs/attachments/07_error_messages_troubleshooting.md` | 1029 | For `qpERR_ABORT_QDB_TEMPORARY_TABLE_DDL_DISABLE`, the source action is to truncate all temporary tables based on the table and retry. The attachment adds "end the session or transaction" and the check SQL only shows whether the named table is temporary; it does not identify the temporary tables based on the target table. | Keep the source action as the primary action. If session termination is retained, label it as an operational fallback requiring owner/session confirmation and impact review. Add a diagnostic note telling the GPT not to invent a session-kill query unless a source-backed way to identify the temporary table/session is available. |
| Medium | `GPTs/attachments/07_error_messages_troubleshooting.md` | 1304 | The SSL client block says 7.3 and 8.1 sources include SSL client errors, but the 7.1 Error Message Reference also includes `ulERR_ABORT_SSL_OPERATION_FAILURE`, `ulERR_ABORT_SSL_LIBRARY_ERROR`, `ulERR_ABORT_SSL_LINK_FAILURE`, `ulERR_ABORT_INVALID_ALTIBASE_SSL_PORT_NO`, and `ulERR_ABORT_PORT_NO_ALTIBASE_SSL_PORT_NO_NOT_SET`. | Update the version caution to include 7.1, 7.3, and 8.1, while still advising confirmation of exact client library and server version. |
| Low | `GPTs/attachments/08_performance_tuning_monitoring.md` | 1800 | The server issue blocks are useful symptom/check/action summaries, but they are less complete than the error blocks: several lack explicit cause, rollback/verification, or escalation criteria for production property changes. | For the issue blocks most likely to drive operational changes, add compact `Cause`, `Verification`, and `Escalate when` bullets. Keep property-change recommendations conditional on before/after metric snapshots. |

## Source Checks

- Claims checked:
  - Error block structure and required fields in `07_error_messages_troubleshooting.md`.
  - Source cause/action text for socket bind, idle instance, lock timeout, tablespace free space, autoextend off, temporary-table DDL block, LOB autocommit, PCRE2 errors, replication socket/handshake, duplicate replication, SSL client/server/OpenSSL errors, DB Link errors, and JSON/Temporary LOB 8.1 errors.
  - Diagnostic view names and columns for `V$TABLE`, `V$LOCK_WAIT`, `V$LOCK_STATEMENT`, `V$REPSENDER`, `V$REPRECEIVER`, `V$REPGAP`, `V$DATAFILES`, `V$TEMPORARY_LOBS`, `V$SYSTEM_EVENT`, `V$BUFFPOOL_STAT`, `V$LFG`, `V$SERVICE_THREAD`, and `V$MEMGC`.
- Source coverage:
  - `07_error_messages_troubleshooting.md` has 32 searchable error blocks. From line 328 onward, every block has `Error Code`, `Reference Symbol`, `Module / Severity`, `Message`, `Applies To`, `Symptom`, `Primary Causes`, `Immediate Action`, `Check SQL or Command`, `Version Cautions`, and `Related Document`.
  - `06_data_dictionary_performance_views.md` provides strong supporting diagnostics for object metadata, locks, statements, replication, backup/archive state, and 8.1 Temporary LOB checks.
  - `08_performance_tuning_monitoring.md` provides symptom-first tuning workflows and monitoring checks that reduce hallucinated tuning recommendations.
- Source gaps:
  - Some `07` blocks collapse multiple source actions into one action path. The highest-risk cases are replication duplicate/not-found diagnostics and PCRE2 unexpected error escalation.
  - JSON and Temporary LOB error details are 8.1 verified-source material from Korean fallback sources and release-note verification, not the English 8.1 Error Message Reference.

## Oracle-Overlap Decision

- Correctly compressed:
  - Ordinary SQL syntax, object existence, constraint, conversion, and date-format errors are brief and focused on Altibase diagnostics rather than generic Oracle behavior.
- Too much generic Oracle material:
  - None found in the reviewed stage files.
- Missing Altibase-specific difference:
  - Some Altibase-specific replication metadata checks are missing from `07` even though `06` contains them.
  - The SSL client version note incorrectly omits 7.1 source coverage.

## Version Checks

- 7.1:
  - Error source sampling confirmed key common entries for socket bind, tablespace space, lock timeout, replication socket/handshake, temporary-table DDL block, and SSL client errors.
  - Finding: SSL client version caution should include 7.1.
- 7.3:
  - Source sampling confirmed lock timeout, tablespace free space, autoextend off, temporary-table DDL block, LOB autocommit, duplicate replication, not-found replication, PCRE2, SSL client, and unsupported OpenSSL entries.
- 8.1:
  - English source sampling confirmed common inherited entries for replication, SSL, SQL, storage, and DB Link errors.
  - JSON and Temporary LOB checks are based on Altibase 8.1 verified source, including Korean Error Message Reference and release-note-backed feature verification.

## Retrieval And GPT Answer Quality

- Strengths:
  - `07` gives a strong universal response format and preserves literal error codes, symbols, properties, commands, and paths.
  - The triage workflow and evidence checklist make it less likely that the GPT will jump directly to destructive operational steps.
  - `06` gives practical diagnostic SQL for sessions, locks, statements, replication, dictionary metadata, backup/archive state, and Temporary LOB.
  - `08` explicitly prevents unsupported tuning advice by requiring plan, statistics, storage type, and bottleneck evidence before index, hint, or property recommendations.
- Risks:
  - A query routed only to the `07` duplicate-replication or not-found blocks may receive insufficient or wrong diagnostic SQL because the richer metadata queries are in `06` but not surfaced in the error block.
  - The standard format does not require escalation output, so source actions that require support contact can be lost unless the GPT retrieves the general rule at line 31.
  - Some performance issue blocks may suggest property changes without enough local rollback or verification framing.

## Required Follow-Up

- Fix the two replication-related diagnostic gaps in `07`: duplicate replication must use replication meta tables, and not-found replication/index/column errors need branch-specific metadata checks.
- Split or branch the PCRE2 regular expression block so `0x2106C` preserves the source escalation path.
- Add an explicit `Escalation` field to the standard error response format and high-risk blocks.
- Correct the SSL client version caution to include 7.1.
- Tighten the temporary-table DDL block to avoid unsourced session-ending advice.
