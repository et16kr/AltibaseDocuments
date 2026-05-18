# Altibase GPT Post-Workflow Follow-Up Plan

- Date: 2026-05-18
- Repository: `/home/et16/AltibaseDocuments`
- Status: Draft for review
- Purpose: define the next work after the full coverage audit workflow and the latest full answerability benchmark.

This document is self-contained. It supersedes any temporary planning notes outside
this repository for deciding the next work sequence.

## Current Evidence Snapshot

First checks at planning time:

| Check | Current result |
| --- | --- |
| `bash review/scripts/run_review_remediation_cycle.sh status` | `R00` through `R27` are `Done` for both cycle and review status. |
| Active or failed cycle rows | No `Reviewing`, `Remediating`, `ReReviewing`, or `Fail` rows. |
| `git status --short` | Clean worktree before this draft was added. |

Full coverage audit state:

| Item | Current result |
| --- | --- |
| Final audit report | `GPTs/reports/full_coverage_audit/final_full_coverage_audit.md` |
| Final readiness decision | `Blocked` |
| Catalog rows | `2153` |
| Matrix rows | `2153` |
| `Covered` | `1162` |
| `Covered-by-routing` | `840` |
| `Guardrail` | `33` |
| `Out-of-scope` | `3` |
| `Missing` | `115` |
| `Retrieval-weak` | `0` |

The `115` active `Missing` rows are all:

| Field | Value |
| --- | --- |
| Source item range | `SRC-PATCH-PATCH-000001` through `SRC-PATCH-PATCH-000115` |
| Source family | `patch_notes` |
| Version scope | `patch-specific` |
| Item type | `version note` |
| Attachment target | `GPTs/attachments/00_version_release_platform.md` |
| Source split | `96` Altibase 7.1 patch-note files and `19` Altibase 7.3 patch-note files |

Latest full answerability benchmark:

| Item | Current result |
| --- | --- |
| Run ID | `altibase_answerability_20260518_091947` |
| Manifest | `full_benchmark` |
| Mode | `live` |
| Provider/model | `command` / `codex-exec` |
| Context mode | `lexical` |
| Readiness decision | `blocking_gaps` |
| Passed / total | `98 / 270` |
| Failed | `172` |
| Pass rate | `36.3%` |
| Critical fact coverage | `82.5%` |
| Required token preservation | `89.2%` |
| Unsupported-claim rate | `1.1%` |
| Worst domain | `views_performance_monitoring` at `10.0%` |
| Protected-topic blockers | `36` |

Latest benchmark artifacts:

- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260518_091947/summary.txt`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260518_091947/judge/report.md`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260518_091947/judge/aggregate_report.json`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260518_091947/judge/judgments.jsonl`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260518_091947/answers/answers.jsonl`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260518_091947/answers/run.json`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260518_091947/run-test.log`

Protected-topic blockers in the latest benchmark:

| Topic | Count | Question IDs |
| --- | ---: | --- |
| `backup_recovery` | `7` | `ERR-110`, `OPS-103`, `OPS-114`, `OPS-118`, `OPS-133`, `PROP-130`, `VPM-114` |
| `destructive_sql` | `3` | `ERR-120`, `ERR-128`, `SQL-105` |
| `replication_state_changes` | `8` | `ERR-127`, `PROP-136`, `REPL-113`, `REPL-116`, `REPL-118`, `SQL-114`, `SQL-141`, `VPM-125` |
| `security_tls` | `2` | `PROP-140`, `PROP-141` |
| `version_sensitive_property_changes` | `16` | `PROP-109`, `PROP-110`, `PROP-112`, `PROP-115`, `PROP-117`, `PROP-121`, `PROP-122`, `PROP-124`, `PROP-127`, `PROP-128`, `PROP-131`, `PROP-144`, `PROP-146`, `PROP-147`, `PROP-148`, `PROP-149` |

## Planning Decision

The next work should not start with another broad full benchmark rerun.

The current blocking order is:

1. Close the full coverage audit gate by resolving the `115` active patch-note
   `Missing` rows.
2. Re-run source-to-attachment structural validation.
3. Then address the `36` protected-topic blockers from the latest benchmark.
4. Then classify and remediate remaining benchmark failures by primary cause.
5. Run targeted validation after each remediation wave.
6. Run the full 270-question live benchmark only after the coverage gate is closed and
   high-risk targeted checks no longer show protected blockers.

Reasoning:

- The final audit report is still `Blocked`; unresolved source-backed `Missing` rows
  prevent source-exhaustive sign-off.
- `Retrieval-weak` is already `0`, so the first audit blocker is not routing; it is
  patch-note coverage closure.
- The latest benchmark still has protected-topic blockers, so readiness cannot pass
  even if overall pass rate improves.
- The latest failures are still dominated by missing facts and missing exact tokens,
  so fixes must remain evidence-driven instead of only changing GPT instructions.

## Replacement-Grade Policy Direction

The attachment set is no longer treated as a compact FAQ or customer-answer-only
summary. The target is a replacement-grade LLM reference for:

- overseas customer Q&A;
- GPT/LLM retrieval and synthesis;
- coding agents building services that use Altibase;
- Altibase-oriented test-case generation and validation planning.

This does not mean every original word must be copied. It means a source-backed
question, implementation task, or test-design task should be answerable from the
attachment set without consulting the original manual, except where the answer depends
on customer-specific runtime state, exact patch level, unsupported behavior, logs,
object definitions, or an accepted guardrail.

The workflow must therefore preserve more than high-level meaning. For every source
family, replacement-grade coverage should include the following when present in the
selected sources:

| Coverage class | Required attachment behavior |
| --- | --- |
| Exact commands and syntax | Preserve command names, option names, statement grammar, abbreviations, examples, and required command ordering. |
| Options, properties, and environment variables | Preserve defaults, ranges, units, precedence, mutability, restart/recreate requirements, version scope, and error behavior. |
| API and connector contracts | Preserve class/function names, connection properties, compile/link requirements, callback/handle lifecycles, and version-specific caveats. |
| Runnable examples and sample inventories | Preserve enough code, file paths, generated file names, sample class names, table names, and setup assumptions for a coding agent to adapt safely. |
| Test-generation anchors | Preserve positive and negative cases, validation SQL, expected result tokens, failure codes, boundary values, setup/teardown needs, and stop conditions. |
| Operational runbooks | Preserve prerequisites, missing inputs, exact checks, safe order, destructive effects, rollback or recovery notes, and escalation evidence. |
| Troubleshooting | Preserve error code, symbol, message, immediate action, primary causes, required customer input, and next checks. |
| Version and patch boundaries | Preserve the version/patch where behavior exists, changes, or is unsupported; do not generalize 7.1, 7.3, and 8.1 behavior without source evidence. |
| Guardrails and accepted omissions | Record why a detail is excluded, unsafe, customer-specific, unsupported, or better answered by asking for missing input. |

The two source-replacement samples below are examples that exposed the policy need.
They are not the whole standard. `PWF-J002A` must turn this direction into a standalone
policy document, and `PWF-J016A` must apply it across all source families.

## Korean Source Replacement Samples

This plan includes concrete source-replacement sample audits so the next workflow does
not rely only on aggregate metrics.

### Sample 1: SSL/TLS Guide

Selected source:

- `Manuals/Altibase_7.1/kor/Altibase SSL TLS User's Guide.md`

Primary attachment checked:

- `GPTs/attachments/18_security_ssl_tls.md`

Related attachment routes checked:

- `GPTs/attachments/11_java_jdbc_spring.md`
- `GPTs/attachments/12_c_cli_odbc_precompiler.md`
- `GPTs/attachments/13_isql_iloader_basic_tools.md`
- `GPTs/attachments/06_data_dictionary_performance_views.md`

Why this source was selected:

- It is small enough for a manual section-by-section audit.
- It is high risk because TLS/security is a protected topic in the benchmark.
- It has clear customer-answer surfaces: server properties, JDBC, ODBC/CLI, ADO.NET,
  TCP restriction, SSL session monitoring, and sample files.

Coverage result:

| Source area | Current attachment answerability | Judgment |
| --- | --- | --- |
| Manual front matter, target audience, conventions, feedback | Not preserved in attachments. | Acceptable omission for GPT customer answering. |
| SSL/TLS concept, certificates, server-only vs mutual authentication | Covered in `18_security_ssl_tls.md` under `Core Concepts` and client/server setup. | Answerable. |
| Altibase SSL behavior: TLS 1.0, separate SSL listener port, Intel Linux scope, JSSE/JDBC/ODBC support | Covered in `Applicable Versions`, `Core Concepts`, and `Version Differences`. | Answerable. |
| 7.1 software requirements: OpenSSL `0.9.4` through `1.0.2`, Altibase `6.5.1` or later, Heartbleed, `OPENSSL_NO_HEARTBEATS`, JRE 1.6 recommendation and JRE 1.5 caveat | Mostly covered in `18_security_ssl_tls.md`; JRE 1.5 nuance is compressed. | Answerable for ordinary customer questions. |
| Server setup: `SSL_ENABLE`, `SSL_PORT_NO`, `SSL_MAX_LISTEN`, `SSL_CIPHER_LIST`, `SSL_CLIENT_AUTHENTICATION`, `SSL_CERT`, `SSL_KEY`, `SSL_CA`, `SSL_CAPATH`, startup SSL listener evidence | Covered in `Server SSL/TLS`. | Answerable. |
| JDBC setup: truststore/keystore import, PKCS #12, JVM properties, `System.setProperty`, JDBC properties, `ssl_enable`, `port`, `ciphersuite_list`, `verify_server_certificate`, store types | Covered in `Client SSL/TLS` and routed to `11_java_jdbc_spring.md`. | Answerable for setup and troubleshooting. |
| ODBC/CLI setup: OpenSSL library check, PEM client certificate, `SSL_CA`, `SSL_CAPATH`, `SSL_CERT`, `SSL_KEY`, `SSL_VERIFY`, `SSL_CIPHER`, server-vs-client property comparison | Covered in `Client SSL/TLS` and routed to `12_c_cli_odbc_precompiler.md`. | Answerable. |
| ADO.NET setup: `conn type=ssl`, `port`, `ssl ca`, `ssl capath`, `ssl cert`, `ssl key`, `ssl verify`, `ssl cipher` | Covered with checklist and example. | Answerable. |
| TCP restriction: `CREATE USER ... DISABLE TCP`, `ALTER USER ... ENABLE TCP`, `SYSTEM_.SYS_USERS_`, `DISABLE_TCP` | Covered in `Managing SSL/TLS Access`; cross-file data dictionary routes also contain `disable_tcp`. | Answerable. |
| SSL monitoring and session close: `V$SESSION`, `COMM_NAME LIKE 'SSL%'`, `SYSDBA`, `ALTER DATABASE database_name SESSION CLOSE session_number` | Covered in `Server SSL/TLS` and `Managing SSL/TLS Access`. | Answerable. |
| Appendix sample file locations: `$ALTIBASE_HOME/sample/cert`, `$ALTIBASE_HOME/sample/SQLCLI/SSL` | Catalog marks this area as `Covered-by-routing`, but `18_security_ssl_tls.md` does not clearly preserve both sample paths. | Weak; can fail sample-location questions. |
| Appendix full JDBC sample: `SslSimpleSQL`, `RuntimeEnvironmentVariables`, `Altibase.jdbc.driver.AltibaseDriver`, `$ALTIBASE_HOME/sample/CERT/truststore`, `$ALTIBASE_HOME/sample/CERT/keystore.jks`, `ssl_port`, `TEST_EMP_TBL` | The attachment set preserves general JDBC connection patterns and the driver class elsewhere, but not this exact appendix sample. | Not source-replacement complete. |
| Appendix ADO.NET short sample | A compact equivalent appears in `18_security_ssl_tls.md`. | Answerable. |

Sample audit conclusion:

- `18_security_ssl_tls.md` is strong enough to answer most practical customer
  questions from the selected Korean SSL/TLS guide.
- It is not a full replacement for the selected Korean source if the customer asks for
  appendix sample-file locations or the exact JDBC sample program.
- The current matrix row `SRC-SEC-XVER-000010` is marked `Covered-by-routing`, but the
  sampled attachment evidence is weaker than that status implies because the exact
  sample paths and sample-code identifiers are not all present in the attachment text.

Potential unanswerable or weak questions from the selected Korean source:

- Where does Altibase install SSL sample certificates and client sample programs?
- What is the exact sample path for SQLCLI SSL samples?
- What Java class and Altibase JDBC driver class does the SSL JDBC sample use?
- Which sample truststore and keystore paths does the SSL JDBC sample construct from
  `ALTIBASE_HOME`?
- Why does the appendix sample use `ssl_port`, while the property table and current
  attachment guidance emphasize `port`?
- What table, columns, and inserts does the JDBC SSL sample use to prove the
  connection?

Planned response if this kind of gap appears in other one-document replacement audits:

1. Treat the gap as `content gap` if the source-backed token, path, sample, property,
   or command is absent from all attachments.
2. Treat it as `retrieval gap` only if the exact item is present but not routed by
   aliases, headings, or cross-references.
3. Treat it as `answer synthesis gap` only if the exact item appears in selected
   context but the generated answer omits it.
4. Do not leave a row as `Covered-by-routing` unless the route contains the exact
   customer-answerable tokens or a concrete owner block.
5. For appendix code, decide whether to preserve the full code, a compact code
   skeleton, or a source-backed sample inventory. If full code is not preserved, record
   the limitation as `Guardrail` or as an accepted residual with a safe answer pattern.

Specific remediation plan for this sample:

1. Re-open `SRC-SEC-XVER-000010` and verify whether the sample appendix should remain
   `Covered-by-routing` or become a small content-remediation item.
2. If preserving sample answerability, add a compact `SSL/TLS Sample File Inventory`
   block to `18_security_ssl_tls.md` with:
   - `$ALTIBASE_HOME/sample/cert`;
   - `$ALTIBASE_HOME/sample/SQLCLI/SSL`;
   - `$ALTIBASE_HOME/sample/CERT/truststore`;
   - `$ALTIBASE_HOME/sample/CERT/keystore.jks`;
   - `SslSimpleSQL`;
   - `Altibase.jdbc.driver.AltibaseDriver`;
   - `RuntimeEnvironmentVariables.getVariable("ALTIBASE_HOME")`;
   - appendix sample note for `ssl_port`, with a caution to verify the exact driver
     property against the target JDBC manual before generating production code.
3. Add a short route in `11_java_jdbc_spring.md` only if the JDBC attachment is expected
   to answer sample-code questions directly.
4. Update `source_item_catalog.tsv`, `source_to_attachment_matrix.tsv`, and
   `remediation_log.md` if the disposition or evidence for `SRC-SEC-XVER-000010`
   changes.
5. Add one targeted regression question for the SSL/TLS appendix sample inventory.
6. Re-run source-to-attachment validation and a targeted answerability check before
   claiming this source is replacement-complete.

### Sample 2: iSQL User's Manual

This second sample deliberately uses a different source family from the SSL/TLS guide.
It checks whether the tool attachment can replace a Korean utility manual for ordinary
customer command generation and low-frequency troubleshooting.

Selected source:

- `Manuals/Altibase_7.1/kor/iSQL User's Manual.md`

Primary attachment checked:

- `GPTs/attachments/13_isql_iloader_basic_tools.md`

Related attachment routes checked:

- `GPTs/attachments/01_getting_started_installation.md`
- `GPTs/attachments/07_error_messages_troubleshooting.md`
- `GPTs/attachments/18_security_ssl_tls.md`

Why this source was selected:

- It is a practical customer-facing tool manual, not a protected-topic security guide.
- It has many exact command, option, environment-variable, and session-setting tokens
  that lexical retrieval must preserve.
- It tests whether the attachment can replace a manual for both common commands and
  low-frequency operational details.

Coverage result:

| Source area | Current attachment answerability | Judgment |
| --- | --- | --- |
| iSQL overview and ordinary connect/script/object-inspection workflows | Covered in `13_isql_iloader_basic_tools.md` with command-line syntax, connection cookbook, script/spool blocks, object inspection, transactions, and history/editing. | Answerable. |
| Core command-line options: `-S`, `-PORT`, `-U`, `-P`, `/NOLOG`, `-SYSDBA`, `-KEEP_SYSDBA`, `-F`, `-O`, `-NLS_USE`, `-NLS_NCHAR_LITERAL_REPLACE`, `-prefer_ipv6`, `-TIME_ZONE`, SSL options | Compact syntax is preserved in `13_isql_iloader_basic_tools.md`; common behavior for prompts, IPv6, `-PORT`, `/NOLOG`, `-SYSDBA`, `-KEEP_SYSDBA`, `-F`, and `-O` is covered. | Mostly answerable. |
| Local IPC/IPCDA/UNIX socket path behavior: `-UNIXDOMAIN-FILEPATH`, `-IPC-FILEPATH`, `-IPCDA-FILEPATH`, `ALTIBASE_IPC_FILEPATH`, `IPCDA_FILEPATH` | The three command-line options appear in syntax, but the attachment does not explain the `ALTIBASE_HOME` mismatch scenario or the matching environment-variable fallback paths. | Weak; can fail local IPC troubleshooting questions. |
| iSQL environment variables: `ALTIBASE_HOME`, `ALTIBASE_PORT_NO`, `ALTIBASE_SSL_PORT_NO`, `ALTIBASE_NLS_USE`, `ALTIBASE_NLS_NCHAR_LITERAL_REPLACE`, `ISQL_CONNECTION`, `ISQL_BUFFER_SIZE`, `ISQL_EDITOR`, `ALTIBASE_DATE_FORMAT`, `ALTIBASE_TIME_ZONE`, generated-file permissions, secure login message | Common install/client variables are covered by `01`; SSL port precedence is covered by `18`; `ISQL_BUFFER_SIZE` is only routed through error troubleshooting; `ALTIBASE_DATE_FORMAT`, `ALTIBASE_TIME_ZONE`, and local IPC path variables are not clearly owned by `13`. | Not replacement-complete as one iSQL source. |
| Login files and generated-file permissions: `$ALTIBASE_HOME/conf/glogin.sql`, `login.sql`, ignored `CONNECT`, `ALTIBASE_UT_FILE_PERMISSION`, `ISQL_FILE_PERMISSION`, `ISQL_SECURE_LOGIN_MSG` | Covered directly in `13`. | Answerable. |
| Output formatting and inspection controls: `SET LINESIZE`, `PAGESIZE`, `HEADING`, `FEEDBACK`, `COLSIZE`, `NUMWIDTH`, `NUMFORMAT`, `LOBSIZE`, `LOBOFFSET`, `TIMING`, `TIMESCALE`, `VERTICAL`, `CHKCONSTRAINTS`, `FOREIGNKEYS`, `PARTITIONS`, `SHOW ALL`, `COLUMN`, `CLEAR COLUMNS` | Major controls are covered. `SET CHKCONSTRAINTS`, `SET FOREIGNKEYS`, `SET PARTITIONS`, `CLEAR COLUMNS`, and `SHOW ALL` are present, though compact. | Answerable for ordinary formatting questions. |
| Script display and substitution controls: `SET TERM`, `SET ECHO`, `SET DEFINE`, `SET VERIFY`, `&1`, `&2`, `START`, `@`, `@@` | Script execution, parameters, `DEFINE`, `VERIFY`, and `TERM` are covered. `SET ECHO` is weak or absent as a named control. | Weak for exact script-display questions. |
| Prompt customization and help: `SET SQLP[ROMPT]`, `_CONNECT_IDENTIFIER`, `_DATE`, `_PRIVILEGE`, `_USER`, `HELP INDEX`, `HELP EXIT` | History, shell, editor, and help are covered generally, but prompt runtime variables and `HELP INDEX`/`HELP EXIT` are not preserved as an answer-ready block. | Not replacement-complete. |
| Host variables and prepared SQL: `VAR[IABLE]`, `INPUT`, `OUTPUT`, `INOUTPUT`, `EXEC[UTE]`, `PRINT VAR[IABLE]`, `PREPARE`, scalar types | Covered in `13` with examples and cautions. | Answerable. |
| NCHAR literal handling: `ALTIBASE_NLS_NCHAR_LITERAL_REPLACE`, `NCHAR`, `NVARCHAR`, `N`, values `0` and `1`, cost caution | Covered in `13` after prior remediation. | Answerable. |

Sample audit conclusion:

- `13_isql_iloader_basic_tools.md` is strong enough for ordinary iSQL connection,
  script execution, object inspection, formatting, host-variable, prepared SQL,
  login-file, and file-permission questions.
- It is not a full replacement for the selected Korean iSQL source when the customer
  asks about low-frequency iSQL environment variables, local IPC/IPCDA path fallback,
  prompt runtime variables, or exact script display controls.
- Some missing facts are present in related attachments or error blocks, but they are
  not yet grouped into an iSQL-owned answer block. That makes the current state more
  of a routed reference than a source-replacement reference.

Potential unanswerable or weak questions from the selected Korean source:

- How do I use `-IPC-FILEPATH` or `ALTIBASE_IPC_FILEPATH` when client and server
  `ALTIBASE_HOME` differ?
- What is the matching `IPCDA_FILEPATH` fallback for `-IPCDA-FILEPATH`?
- What is the precedence for the iSQL SSL port and where does `ALTIBASE_SSL_PORT_NO`
  fit when `ISQL_CONNECTION=SSL`?
- What does `ISQL_BUFFER_SIZE` control and when should it be increased?
- How do `ALTIBASE_DATE_FORMAT` and `ALTIBASE_TIME_ZONE` affect iSQL display/session
  behavior?
- How do I customize the iSQL prompt with `_CONNECT_IDENTIFIER`, `_DATE`,
  `_PRIVILEGE`, or `_USER`?
- What is the difference between `SET TERM` and `SET ECHO` for script execution output?
- How do `HELP INDEX` and `HELP EXIT` behave in iSQL?

Specific remediation plan for this sample:

1. Treat the iSQL findings as a `content gap` in the tools/APIs/connectors domain
   unless PWF-J024 proves each exact token already appears in selected retrieval
   context.
2. In `PWF-J030`, add or strengthen an `iSQL Environment and Session Controls`
   inventory in `13_isql_iloader_basic_tools.md` with:
   - `ALTIBASE_SSL_PORT_NO`;
   - `ISQL_BUFFER_SIZE`;
   - `ALTIBASE_DATE_FORMAT`;
   - `ALTIBASE_TIME_ZONE`;
   - `ALTIBASE_IPC_FILEPATH`;
   - `IPCDA_FILEPATH`;
   - the behavior of `-UNIXDOMAIN-FILEPATH`, `-IPC-FILEPATH`, and `-IPCDA-FILEPATH`;
   - `SET ECHO`;
   - `SET SQLPROMPT` / `SET SQLP`;
   - `_CONNECT_IDENTIFIER`, `_DATE`, `_PRIVILEGE`, `_USER`;
   - `HELP INDEX` and `HELP EXIT`.
3. Keep cross-references to `01_getting_started_installation.md` for installation
   environment setup, `18_security_ssl_tls.md` for SSL/TLS port semantics, and
   `07_error_messages_troubleshooting.md` for `ISQL_BUFFER_SIZE` error handling, but
   make `13` the owner route for iSQL command generation.
4. Re-check catalog/matrix rows `SRC-ISQL-XVER-000002`, `SRC-ISQL-XVER-000003`,
   `SRC-ISQL-XVER-000009`, and `SRC-ISQL-XVER-000011` after the content update; adjust
   anchors if they currently overstate direct coverage.
5. Add targeted regression questions for local IPC path fallback, prompt runtime
   variables, `SET ECHO` vs `SET TERM`, and `ISQL_BUFFER_SIZE`.
6. Re-run source-to-attachment validation and targeted answerability before claiming
   the 7.1 Korean iSQL source is replacement-complete.

## Execution Workflow

The executable workflow lives in:

- `.codex-jobs/altibase-gpt-post-workflow-followup/jobs.tsv`
- `.codex-jobs/altibase-gpt-post-workflow-followup/jobs.md`
- `.codex-jobs/altibase-gpt-post-workflow-followup/prompts/`
- `.codex-jobs/altibase-gpt-post-workflow-followup/run-all.sh`

The `.codex-jobs` directory contains workflow definitions and runtime state. Per-job
commits must include the scoped attachment/report changes only; the runner now fails a
job if its commit includes `.codex-jobs` status, log, runtime, or rollback files.

The workflow intentionally uses smaller jobs than the conceptual work packages above.
Patch-note closure is split into 8-10 row batches because the original 32-row batches
were too large for reliable exact-token review and recovery.

| Job range | Purpose |
| --- | --- |
| `PWF-J001` | Lock the latest benchmark evidence without remediation. |
| `PWF-J002` | Design patch-note closure before attachment edits. |
| `PWF-J002A` | Define the replacement-grade policy for customer Q&A, LLM retrieval, coding-agent implementation, and test-case generation across all source families. |
| `PWF-J003` through `PWF-J014` | Close or justify `SRC-PATCH-PATCH-000001` through `SRC-PATCH-PATCH-000115` in small batches. |
| `PWF-J015` | Remediate or justify the sampled SSL/TLS appendix replacement gap before final closure validation. |
| `PWF-J016` | Validate full source-to-attachment closure with `Missing=0` and `Retrieval-weak=0`. |
| `PWF-J016A` | Apply the replacement-grade policy across all source families and assign cross-document gaps to owner jobs. |
| `PWF-J016B` | Remediate replacement-grade version, release-note, platform, and patch-note gaps assigned by the gap register. |
| `PWF-J017` | Classify all protected-topic blockers by primary cause. |
| `PWF-J018` through `PWF-J022` | Remediate protected blockers by topic: version-sensitive properties, security/TLS, backup/recovery, destructive SQL, and replication state. |
| `PWF-J023` | Run or record targeted protected-topic validation. |
| `PWF-J024` | Classify remaining non-protected failures and assign domain waves. |
| `PWF-J025` through `PWF-J030` | Remediate domain waves: views/performance, SQL/data types, properties, replication/security/network, errors/operations, tools/APIs/connectors. |
| `PWF-J031` | Run instruction-aware synthesis checks and narrowly update instructions if evidence requires it. |
| `PWF-J031A` | Validate coding-agent implementation and Altibase test-generation readiness across representative scenarios. |
| `PWF-J032` | Run the final readiness gate and full live rerun only when preconditions are clean. |

`PWF-J016B` is the owner for any replacement-grade gap in
`00_version_release_platform.md`, release notes, platform support, install/upgrade
boundaries, and patch-note coverage that remains after the structural coverage gate.
If that job finds the work is too broad for one run, it must create an explicit
not-ready report and split the remaining work before protected-topic remediation.

Protected-topic remediation jobs must run targeted validation for their scoped question
IDs, or produce an explicit blocker report explaining why validation could not run.
The final full benchmark is not the first proof step; it is a final gate after coverage,
replacement-grade, protected-topic, domain remediation, and developer/test-readiness
evidence is clean.

Do not lower thresholds or rewrite benchmark questions to make the benchmark pass.

## Non-Goals

- Do not edit original manuals, release notes, patch notes, or source documents.
- Do not browse for new Altibase facts.
- Do not treat patch-specific source-backed items as closed merely because they are
  patch-specific.
- Do not make a full benchmark rerun the next action while the audit still has active
  `Missing` rows.
- Do not replace Altibase-specific behavior with generic Oracle or generic database
  assumptions.
- Do not classify a failure as judge-only unless selected context, full attachment
  context, answer text, source evidence, exact tokens, and expected facts have all been
  checked.

## Suggested Next Immediate Action

Create and execute the workflow from `PWF-J001` onward after this draft is committed.
The early part of the workflow now includes `PWF-J002A`, so the replacement-grade
policy is established before patch-note and domain remediation scale out.

Do not split off the later remediation waves until `PWF-J016A` has produced the
cross-document replacement-grade gap register. That register is the handoff that
prevents the workflow from only fixing the two sampled manuals.
