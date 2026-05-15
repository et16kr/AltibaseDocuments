# R08 Troubleshooting and Error Response Quality

Date: 2026-05-15
Reviewer: Codex
Verdict: Review Required

## Scope

- Attachments:
  - `GPTs/attachments/07_error_messages_troubleshooting.md`
  - `GPTs/attachments/06_data_dictionary_performance_views.md`
  - `GPTs/attachments/08_performance_tuning_monitoring.md`
- Supporting reports:
  - None sampled for this stage.
- Source manuals sampled:
  - `Manuals/Altibase_7.1/eng/Error Message Reference.md`
  - `Manuals/Altibase_7.3/eng/Error Message Reference.md`
  - `Manuals/Altibase_trunk/eng/Error Message Reference.md`
  - `Manuals/Altibase_7.3/eng/General Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_7.3/eng/General Reference-2.The Data Dictionary.md`
  - `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`

## Commands Run

```bash
sed -n '1,220p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,220p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,220p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
rg -n '^(#{2,4}) ' GPTs/attachments/07_error_messages_troubleshooting.md
rg -n '^(#{2,4}) ' GPTs/attachments/06_data_dictionary_performance_views.md
rg -n '^(#{2,4}) ' GPTs/attachments/08_performance_tuning_monitoring.md
rg -n '^### Error Block:' GPTs/attachments/07_error_messages_troubleshooting.md
rg -c '^\*\*0x[0-9A-F]{5}' Manuals/Altibase_7.1/eng/Error\ Message\ Reference.md Manuals/Altibase_7.3/eng/Error\ Message\ Reference.md Manuals/Altibase_trunk/eng/Error\ Message\ Reference.md
rg -n 'If the user gives only an error code|If one field is unknown|If the reference action says to contact support|Add future error blocks' GPTs/attachments/07_error_messages_troubleshooting.md
rg -n 'VICTIM_SEARCH_WARP|V\$SERVICE_THREAD|TYPE .*service thread|READY_TASK_COUNT|MULTIPLEXING_THREAD_COUNT' 'Manuals/Altibase_7.3/eng/General Reference-2.The Data Dictionary.md' 'Manuals/Altibase_7.3/eng/General Reference-1.Data Types & Altibase Properties.md'
rg -n 'qpERR_ABORT_QDB_TEMPORARY_TABLE_DDL_DISABLE|rpERR_ABORT_RP_READ_SOCKET|rpERR_ABORT_RP_SENDER_HANDSHAKE|utERR_ABORT_Comm_Failure_Error|idERR_FATAL_idc_SVC_INET_BIND_ERROR' Manuals/Altibase_7.1/eng/Error\ Message\ Reference.md Manuals/Altibase_7.3/eng/Error\ Message\ Reference.md Manuals/Altibase_trunk/eng/Error\ Message\ Reference.md
```

## Findings

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| High | `GPTs/attachments/07_error_messages_troubleshooting.md` | 11 | The file says it can answer cause and action for a specific Altibase error code, but the attachment contains only 32 searchable error blocks while each sampled Error Message Reference has roughly 2,900-3,000 entries. The safety rules at lines 28 and 53 reduce hallucination risk, but there is no explicit "uncovered error code" answer path. A GPT could infer cause/action from prefix/module when the exact code is not in the attachment. | Add an explicit uncovered-code response block: preserve the supplied code/message, say the exact cause/action is not covered by the attachment, ask for full error line/version/SQL or command/log excerpt, and do not provide cause/action beyond `Unknown from the supplied message`. Narrow the question bullet to "covered/common error codes" unless broader sourced coverage is added. |
| Medium | `GPTs/attachments/07_error_messages_troubleshooting.md` | 34 | The standard response format requires `Escalation`, but most error blocks omit an explicit escalation line. Only the temporary-table DDL and client SSL blocks include concrete escalation text; production-sensitive blocks such as FATAL listener bind, replication socket/handshake, server SSL, and DB Link do not. | Add an `Escalation:` field to every error block, or add a module/severity default that every block inherits. Include exact evidence to collect and when to stop giving corrective actions. |
| Medium | `GPTs/attachments/08_performance_tuning_monitoring.md` | 1808 | Server tuning blocks are useful but not consistently organized as symptom, cause, diagnostic check, bounded action, verification, and escalation. Several actions involve operational property changes without rollback limits or a post-change verification query. | Rewrite each `Server issue block` with the same troubleshooting fields used in attachment 07: `Symptom`, `Primary Causes`, `Check SQL or Command`, `Immediate Action`, `Verification`, `Version Cautions`, and `Escalation`. |
| Medium | `GPTs/attachments/08_performance_tuning_monitoring.md` | 1839 | `VICTIM_SEARCH_WARP` is interpreted as page flushing being deprioritized, but the 7.3 source describes it as continued replacement-buffer searches after failing to find replacement targets. The current interpretation could lead to wrong buffer-pressure diagnosis. | Rephrase as replacement-buffer search pressure. Pair it with `VICTIM_FAILS`, `PREPARE_AGAIN_VICTIMS`, `READ_PAGES`, and time-window snapshots before recommending `BUFFER_AREA_SIZE` or SQL/index changes. |
| Medium | `GPTs/attachments/08_performance_tuning_monitoring.md` | 1858 | The service-thread action compares a generic `SOCKET` count with `MULTIPLEXING_THREAD_COUNT`, but `V$SERVICE_THREAD.TYPE` distinguishes `SOCKET (MULTIPLEXING)` and `SOCKET (DEDICATED)`, and `READY_TASK_COUNT` is the more direct queue signal. The current wording can over-recommend increasing `MULTIPLEXING_THREAD_COUNT`. | Count `TYPE` and `RUN_MODE` explicitly, inspect `READY_TASK_COUNT`, and compare only multiplexing/shared load with `MULTIPLEXING_THREAD_COUNT`. Include a verification query and version/property check before recommending a property change. |
| Low | `GPTs/attachments/06_data_dictionary_performance_views.md` | 1797 | The runtime and replication answer templates stop after listing diagnostic views. They do not point the GPT back to the error/performance files for action and escalation after the data is collected. | Add one final step to each troubleshooting template: map the observed condition to the relevant 07 or 08 response block before recommending an action. |

## Source Checks

- Claims checked:
  - `ERR-31363` / `0x31363` maps to `qpERR_ABORT_QDB_TEMPORARY_TABLE_DDL_DISABLE`, with source action to truncate related temporary tables and retry.
  - `0x91015` maps to `utERR_ABORT_Comm_Failure_Error`, with source cause/action limited to network connection closed and checking the DBMS server.
  - `0x0001F` maps to `idERR_FATAL_idc_SVC_INET_BIND_ERROR`, with source action to verify whether another process uses the port.
  - `0x61003` and `0x6100D` replication socket/handshake entries support checking network, timeout context, definitions, and `altibase_rp.log`.
  - Sampled diagnostic columns for `V$LOCK_STATEMENT`, `V$SESSION`, `V$BUFFPOOL_STAT`, `V$SERVICE_THREAD`, `V$REPSENDER`, `V$REPRECEIVER`, and `V$REPGAP` exist in the sampled General Reference.
- Source coverage:
  - The sampled 07 error blocks are mostly source-backed and are organized around symptom, cause, action, and check SQL/commands.
  - The 8.1 JSON and Temporary LOB cautions are appropriately limited to 8.1 verified source and release-note-backed behavior.
- Source gaps:
  - Error coverage is curated, not comprehensive. The attachment needs an explicit unsupported/uncovered-code behavior to avoid inferred cause/action for thousands of unlisted codes.
  - Escalation guidance is not itemized for most individual error blocks.

## Oracle-Overlap Decision

- Correctly compressed:
  - Generic SQL execution errors are kept brief and routed to Altibase dictionary checks.
- Too much generic Oracle material:
  - None found in this stage.
- Missing Altibase-specific difference:
  - The main gap is not Oracle overlap; it is Altibase-specific operational escalation and uncovered error-code behavior.

## Version Checks

- 7.1:
  - Sampled error codes and dictionary objects are present in the 7.1 source.
- 7.3:
  - Sampled error codes, `V$SERVICE_THREAD`, `V$BUFFPOOL_STAT`, lock views, and replication views are present in the 7.3 source.
- 8.1:
  - JSON and Temporary LOB material is correctly treated as 8.1-sensitive. `V$TEMPORARY_LOBS` is backed by the 8.1 release notes, but exact 8.1 error-code coverage remains curated rather than comprehensive.

## Retrieval And GPT Answer Quality

- Strengths:
  - Attachment 07 has a strong response format, module/severity map, evidence checklist, and many common operational error blocks.
  - Attachment 06 provides useful operational SQL for sessions, locks, replication, tablespaces, backup/log state, and Temporary LOB checks.
  - Attachment 08 correctly warns against recommending indexes, hints, and property changes before evidence is collected.
- Risks:
  - Uncovered error codes are the main hallucination risk because the file promises broad code-specific cause/action coverage but only contains curated blocks.
  - Missing escalation fields make answers less consistent for production incidents.
  - A few performance troubleshooting actions need tighter source wording and verification steps before property changes.

## Required Follow-Up

- Add a source-safe "uncovered error code" response pattern to `07_error_messages_troubleshooting.md`.
- Add explicit `Escalation:` fields, or inherited escalation defaults, to the individual 07 error blocks.
- Normalize 08 server issue blocks to the symptom/cause/check/action/verification/escalation structure.
- Correct the `VICTIM_SEARCH_WARP` interpretation and refine the service-thread overload diagnostic before upload.
