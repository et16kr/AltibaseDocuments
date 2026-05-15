# R13 Troubleshooting and Error Response Quality

Date: 2026-05-16
Reviewer: Codex
Verdict: Pass

## Scope

- Attachments:
  - `GPTs/attachments/07_error_messages_troubleshooting.md`
  - `GPTs/attachments/06_data_dictionary_performance_views.md`
  - `GPTs/attachments/08_performance_tuning_monitoring.md`
- Supporting reports:
  - `GPTs/reports/eng_kor_parity.md`
- Source manuals sampled:
  - `Manuals/Altibase_7.1/kor/Error Message Reference.md`
  - `Manuals/Altibase_7.3/kor/Error Message Reference.md`
  - `Manuals/Altibase_trunk/kor/Error Message Reference.md`
  - `Manuals/Altibase_7.1/kor/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_7.1/kor/Performance Tuning Guide.md`
  - `Manuals/Altibase_7.3/kor/Performance Tuning Guide.md`
  - `Manuals/Altibase_trunk/kor/Performance Tuning Guide.md`
  - `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`

## Commands Run

```bash
bash review/scripts/run_review_remediation_cycle.sh status
rg -n $'\t(Reviewing|Remediating|ReReviewing|Fail)$' review/review_remediation_cycle_status.tsv
git status --short
git diff -- GPTs/attachments/07_error_messages_troubleshooting.md GPTs/attachments/08_performance_tuning_monitoring.md review/review_remediation_cycle_status.tsv review/review_stage_status.tsv
sed -n '1,240p' review/reports/R13_troubleshooting_errors.md
sed -n '1,260p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,260p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,300p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,240p' GPTs/attachments/README.md
wc -l GPTs/attachments/07_error_messages_troubleshooting.md GPTs/attachments/06_data_dictionary_performance_views.md GPTs/attachments/08_performance_tuning_monitoring.md
rg -n "^(#|##|###) " GPTs/attachments/07_error_messages_troubleshooting.md
rg -n "^(#|##|###) " GPTs/attachments/06_data_dictionary_performance_views.md
rg -n "^(#|##|###) " GPTs/attachments/08_performance_tuning_monitoring.md
rg -n "qpERR_ABORT_JSON_(INVALID_TYPE|NUMBER_OVERFLOW|EXCEEDED_OBJECT_MAX_DEPTH|EMPTY_RESULTS|WRAPPER_IS_NEEDED|DEFAULT_VALUE_TOO_LONG|INVALID_KEY_TYPE|OBJECT_INCOMPLETE|TEXT_OVERFLOW|INVALID_JSON_PATH|INVALID_JSON_DATA|INAPPROPRIATE_JSON_PATH_VALUE|MULTIPLE_RESULTS|FAILED_TO_CONVERT_NUMERIC|RETURNS_NON_SCALAR_VALUE)|0x314B[C-F]|0x314C[0-9A]" Manuals/Altibase_trunk/kor/Error\ Message\ Reference.md
rg -n "ulERR_ABORT_SSL_OPERATION_FAILURE|ulERR_ABORT_SSL_LIBRARY_ERROR|ulERR_ABORT_SSL_LINK_FAILURE|ulERR_ABORT_INVALID_ALTIBASE_SSL_PORT_NO|ulERR_ABORT_PORT_NO_ALTIBASE_SSL_PORT_NO_NOT_SET|0x5120C|0x5120D|0x5120E|0x5121D|0x5121E" Manuals/Altibase_7.1/kor/Error\ Message\ Reference.md Manuals/Altibase_7.3/kor/Error\ Message\ Reference.md Manuals/Altibase_trunk/kor/Error\ Message\ Reference.md
rg -n "cmERR_ABORT_INVALID_CERTIFICATE|cmERR_ABORT_INVALID_PRIVATE_KEY|cmERR_ABORT_PRIVATE_KEY_VERIFICATION|cmERR_ABORT_SSL_HANDSHAKE|cmERR_ABORT_SSL_READ|cmERR_ABORT_SSL_WRITE|cmERR_ABORT_SSL_SHUTDOWN|cmERR_ABORT_INVALID_VERIFY_LOCATION|cmERR_ABORT_INVALID_CA_LIST_FILE|cmERR_ABORT_SSL_CONNECT|cmERR_ABORT_VERIFY_PEER_CERITIFICATE|cmERR_ABORT_SSL_OPERATION|cmERR_ABORT_UNSUPPORTED_OPENSSL_VERSION|0x710A[0-9A-B]|0x710CB" Manuals/Altibase_7.1/kor/Error\ Message\ Reference.md Manuals/Altibase_7.3/kor/Error\ Message\ Reference.md Manuals/Altibase_trunk/kor/Error\ Message\ Reference.md
rg -n "MINMEMSCNINTXS|OLDESTTX|MEMORY_VIEW_SCN|V\$MEMGC|V\$TRANSACTION|V\$STATEMENT" Manuals/Altibase_7.1/kor/General\ Reference-2.The\ Data\ Dictionary.md Manuals/Altibase_7.3/kor/General_Reference-2.The\ Data\ Dictionary.md Manuals/Altibase_trunk/kor/General_Reference-2.The\ Data\ Dictionary.md
rg -n "SYS_INDICES_|SYS_INDEX_COLUMNS_|IS_UNIQUE|INDEX_COL_ORDER|SORT_ORDER|CONSTRAINT_TYPE" Manuals/Altibase_7.1/kor/General\ Reference-2.The\ Data\ Dictionary.md Manuals/Altibase_7.3/kor/General_Reference-2.The\ Data\ Dictionary.md Manuals/Altibase_trunk/kor/General_Reference-2.The\ Data\ Dictionary.md
rg -n "smERR_ABORT_smnUniqueViolation|0x11058|The row already exists in a unique index" Manuals/Altibase_7.1/kor/Error\ Message\ Reference.md Manuals/Altibase_7.3/kor/Error\ Message\ Reference.md Manuals/Altibase_trunk/kor/Error\ Message\ Reference.md
rg -n "0x314B4|qpERR_ABORT_QMX_LOB_AUTOCOMMIT_MODE|0x5112C|ulERR_ABORT_LOB_AUTOCOMMIT_MODE_ERR|0x91101|utERR_ABORT_LOB_AUTOCOMMIT_MODE_ERR|mtERR_ABORT_JSON_WITHOUT_TEMPLOB|0x2106D" Manuals/Altibase_7.1/kor/Error\ Message\ Reference.md Manuals/Altibase_7.3/kor/Error\ Message\ Reference.md Manuals/Altibase_trunk/kor/Error\ Message\ Reference.md
rg -n "V\$TEMPORARY_LOBS|TEMPORARY_LOB_ENABLE|MEMORY_TEMPLOB_MAX_ALLOC_SIZE|MEMORY_TEMPLOB_PIECE_SIZE|ALTER SESSION SET FREE TEMPORARY LOB" Manuals/Altibase_trunk/kor ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md GPTs/reports/eng_kor_parity.md
rg -n "^Error Code|^Error Codes|^Reference Symbol|Exact code map|0x[0-9A-F]{5}|ERR-[0-9A-F]{5}" GPTs/attachments/07_error_messages_troubleshooting.md
rg -n "Unknown from the supplied message|Do not infer|Escalation:|Immediate Action:|Version Cautions:|Altibase 8.1 verified source|trunk|file://|C:/" GPTs/attachments/07_error_messages_troubleshooting.md GPTs/attachments/06_data_dictionary_performance_views.md GPTs/attachments/08_performance_tuning_monitoring.md
nl -ba GPTs/attachments/07_error_messages_troubleshooting.md | sed -n '880,1245p'
nl -ba GPTs/attachments/07_error_messages_troubleshooting.md | sed -n '1387,1498p'
nl -ba GPTs/attachments/08_performance_tuning_monitoring.md | sed -n '1890,1940p'
nl -ba GPTs/attachments/06_data_dictionary_performance_views.md | sed -n '402,520p'
git diff --check -- review/reports/R13_troubleshooting_errors.md GPTs/attachments/07_error_messages_troubleshooting.md GPTs/attachments/06_data_dictionary_performance_views.md GPTs/attachments/08_performance_tuning_monitoring.md
rg -n "^Verdict:|^\| (Blocker|High|Medium|Low) \|" review/reports/R13_troubleshooting_errors.md
rg -n "trunk|file://|C:/|Manuals/|ReleaseNotes/|Altibase_trunk" GPTs/attachments/07_error_messages_troubleshooting.md GPTs/attachments/06_data_dictionary_performance_views.md GPTs/attachments/08_performance_tuning_monitoring.md
bash review/scripts/run_review_stage.sh validate
```

## Findings

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Note | `GPTs/attachments/07_error_messages_troubleshooting.md`; `GPTs/attachments/08_performance_tuning_monitoring.md`; `GPTs/attachments/06_data_dictionary_performance_views.md` | - | No actionable `Blocker`, `High`, `Medium`, or `Low` findings remain for R13. The previous JSON/SSL mapping, OpenSSL-version scoping, MVCC GC diagnostic, and standalone unique-index diagnostic issues are resolved in the current worktree. | No R13 remediation is required. Preserve the exact-code mapping tables and evidence-first response rules during later cleanup. |

## Source Checks

- Claims checked:
  - The uncovered-error response rule preserves user-supplied codes and blocks unsupported inference in `07_error_messages_troubleshooting.md:29`.
  - `0x11058` unique-index violation now includes both constraint checks and standalone `SYSTEM_.SYS_INDICES_` / `SYSTEM_.SYS_INDEX_COLUMNS_` checks in `07_error_messages_troubleshooting.md:881` through `:943`, consistent with dictionary support also exposed in `06_data_dictionary_performance_views.md:402` through `:455`.
  - LOB autocommit and JSON/Temporary LOB blocks were rechecked against Korean error and 8.1 Temporary LOB sources; the SQL-level `0x314B4` scope is limited to 7.3/8.1, and `0x2106D` is kept 8.1-sensitive in `07_error_messages_troubleshooting.md:1132` through `:1193`.
  - The JSON `0x314BC` through `0x314CA` block now maps each runtime/reference code to the Korean 8.1 verified source symbol and message in `07_error_messages_troubleshooting.md:1197` through `:1242`.
  - Client SSL `0x5120C`, `0x5120D`, `0x5120E`, `0x5121D`, and `0x5121E` now have exact map rows in `07_error_messages_troubleshooting.md:1387` through `:1422`.
  - Server SSL `0x710A0` through `0x710AB` and unsupported OpenSSL `0x710CB` were checked against Korean error sources; `0x710CB` remains scoped to 7.3 and Altibase 8.1 verified source in `07_error_messages_troubleshooting.md:1426` through `:1495`.
  - The MVCC garbage collector diagnostic now uses `V$MEMGC.OLDESTTX` instead of arbitrary `MINMEMSCNINTXS` matching, consistent with the Korean data dictionary definition that `OLDESTTX` owns `MINMEMSCNINTXS`; see `08_performance_tuning_monitoring.md:1891` through `:1937`.
- Source coverage:
  - Korean Error Message Reference sources support the sampled common SQL, LOB, JSON, replication, client SSL, CM SSL, and OpenSSL code families.
  - Korean General Reference data dictionary sources support the sampled metadata and performance view columns used by the diagnostic SQL.
  - `eng_kor_parity.md` still supports using Korean source detail for 8.1 JSON errors, Temporary LOB, and replication SSL while keeping attachment prose in English.
- Korean/English source conflicts:
  - No new Korean/English conflict was found in this stage.
  - Existing parity notes remain relevant for 8.1 JSON errors and Temporary LOB detail.
- Source gaps:
  - This stage sampled high-risk troubleshooting and diagnostic paths; it did not exhaustively verify every grouped non-sensitive error-code block.
  - Future added error blocks should continue to use exact per-code rows when several codes share one troubleshooting topic.

## Oracle-Overlap Decision

- Correctly compressed:
  - Ordinary SQL syntax, object-not-found, privileges, conversion, date parsing, and constraint troubleshooting stay brief and direct the GPT to Altibase dictionary checks rather than generic Oracle-style diagnosis.
- Too much generic Oracle material:
  - None found in the scoped attachments.
- Missing Altibase-specific difference:
  - None actionable remains. The prior unique-index blind spot is now covered with Altibase `SYSTEM_.SYS_INDICES_` and `SYSTEM_.SYS_INDEX_COLUMNS_`.

## Version Checks

- 7.1:
  - Common SQL, storage, replication, client SSL, CM SSL, CLI/utility LOB autocommit, index metadata, and MVCC diagnostic columns sampled as present.
  - The attachment does not map a generic 7.1 SSL symptom to `0x710CB`; it requires the target runtime to show that exact code.
- 7.3:
  - JSON is not broadened into 7.3. SSL, `0x710CB`, SQL-level LOB autocommit, client LOB, utility LOB, replication, index metadata, and MVCC diagnostics are scoped consistently with sampled Korean sources.
- 8.1:
  - JSON errors, `TEMPORARY_LOB_ENABLE`, Temporary LOB properties, `V$TEMPORARY_LOBS`, replication SSL cautions, SSL errors, and JSON plan residual cautions remain version-aware and source-limited.

## Retrieval And GPT Answer Quality

- Strengths:
  - `07_error_messages_troubleshooting.md` gives a consistent symptom/cause/action/check/version/escalation structure and an explicit rule for uncovered error codes.
  - High-risk JSON and SSL questions no longer require list-order inference because exact code maps are present.
  - Diagnostic SQL for uniqueness and MVCC GC now has enough Altibase-specific metadata to avoid common false diagnoses.
  - Escalation wording emphasizes evidence collection before destructive or support-level actions.
- Risks:
  - The attachment intentionally covers representative/common errors, not the full Error Message Reference. The uncovered-error rule is therefore still important.
  - Some grouped non-sensitive blocks rely on ordered code/symbol/message lists rather than full exact-code tables; sampled high-risk blocks are acceptable, but future remediation should prefer exact maps when users commonly ask by code.
  - Diagnostic SQL still depends on target-version view and column availability; the attachments correctly tell the GPT to verify availability before relying on version-sensitive views.

## Required Follow-Up

- No R13 remediation is required.
- Keep future troubleshooting additions source-backed, version-scoped, and exact-code mapped when a topic contains multiple actionable error codes.
