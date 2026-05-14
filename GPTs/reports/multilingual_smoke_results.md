# Multilingual Smoke Test Results

Job: `JOB-085`
Phase: P8 QA
Date: 2026-05-14
Result: Pass

## Objective

Test whether the Altibase GPT attachment set supports customer answers in major user
languages while preserving SQL object names, function names, error codes, property
names, commands, and file paths literally.

Acceptance criterion: user-language response works.

## Sources Reviewed

- `GPTs/reports/multilingual_prompt_set.md`
- `GPTs/GPT_Instructions_Draft.md`
- `GPTs/attachments/README.md`
- `GPTs/internal/terminology_glossary.md`
- `GPTs/attachments/00_version_release_platform.md`
- `GPTs/attachments/02_administration_operations.md`
- `GPTs/attachments/03_sql_ddl_generation.md`
- `GPTs/attachments/04_sql_dml_oracle_compatibility.md`
- `GPTs/attachments/05_data_types_properties.md`
- `GPTs/attachments/06_data_dictionary_performance_views.md`
- `GPTs/attachments/07_error_messages_troubleshooting.md`
- `GPTs/attachments/08_performance_tuning_monitoring.md`
- `GPTs/attachments/09_replication_ha_cdc.md`
- `GPTs/attachments/10_psm_stored_external_procedures.md`
- `GPTs/attachments/11_java_jdbc_spring.md`
- `GPTs/attachments/12_c_cli_odbc_precompiler.md`
- `GPTs/attachments/13_isql_iloader_basic_tools.md`
- `GPTs/attachments/14_utilities_operation_tools.md`
- `GPTs/attachments/15_migration_oracle_compatibility.md`
- `GPTs/attachments/16_dblink_external_connectors.md`

## Method

The checks were run as manual Codex prompt simulations using the 18 prompts from
`GPTs/reports/multilingual_prompt_set.md`. No live Altibase server was used.

For each prompt, the simulated answer was checked for:

- Response language matching the user's language, or the explicitly requested override
  language.
- Literal preservation of SQL names, SQL keywords, function names, error codes,
  property names, commands, file paths, API names, host names, ports, and version labels.
- Version-aware behavior, including asking for the Altibase version when needed.
- Use of customer-safe `Altibase 8.1 verified source` wording if 8.1 source context is
  mentioned.
- Safe handling of missing context without inventing unsupported syntax, properties,
  error codes, or version claims.
- Attachment-backed answer content for the requested topic.

## Summary

| Metric | Count |
| --- | ---: |
| Prompt checks run | 18 |
| Languages covered | 9 |
| Passed | 18 |
| Failed | 0 |
| Review needed | 0 |

## Language Coverage

| Language | Prompt IDs | Result |
| --- | --- | --- |
| Vietnamese | `ML-vi-01`, `ML-vi-02` | Pass |
| Turkish | `ML-tr-01`, `ML-tr-02` | Pass |
| Persian | `ML-fa-01`, `ML-fa-02` | Pass |
| Hindi | `ML-hi-01`, `ML-hi-02` | Pass |
| Chinese | `ML-zh-01`, `ML-zh-02` | Pass |
| Japanese | `ML-ja-01`, `ML-ja-02` | Pass |
| English / French override | `ML-en-01`, `ML-en-02` | Pass |
| German | `ML-de-01`, `ML-de-02` | Pass |
| French | `ML-fr-01`, `ML-fr-02` | Pass |

## Prompt Checks

### ML-vi-01: Vietnamese - JSON DDL

Attachment support:

- `03_sql_ddl_generation.md`: 8.1 JSON table DDL and `TEMPORARY_LOB_ENABLE` checks.
- `04_sql_dml_oracle_compatibility.md`: `JSON_VALUE` usage.
- `05_data_types_properties.md`: native `JSON` type and JSON function family.

Accepted response behavior:

- Starts in Vietnamese, for example: "Với Altibase 8.1, có thể tạo bảng `T_CUSTOMER`
  với cột `PROFILE_JSON` kiểu `JSON` và kiểm tra bằng `JSON_VALUE` như sau."
- Preserves `Altibase 8.1`, `CREATE TABLE`, `T_CUSTOMER`, `CUST_ID`, `PROFILE_JSON`,
  `JSON`, `JSON_VALUE`, and `TEMPORARY_LOB_ENABLE`.
- Includes SQL that keeps `T_CUSTOMER` and `PROFILE_JSON` unchanged.

Result: Pass

### ML-vi-02: Vietnamese - Property And Path

Attachment support:

- `05_data_types_properties.md`: `QUERY_TIMEOUT`, `V$PROPERTY`, and
  `altibase.properties` property workflow.
- `13_isql_iloader_basic_tools.md`: minimal `isql` command patterns.

Accepted response behavior:

- Starts in Vietnamese, for example: "Bạn có thể kiểm tra `QUERY_TIMEOUT` bằng
  `V$PROPERTY`, rồi đối chiếu với `$ALTIBASE_HOME/conf/altibase.properties` nếu cần
  cấu hình bền sau khi restart."
- Preserves `QUERY_TIMEOUT`, `V$PROPERTY`, `$ALTIBASE_HOME/conf/altibase.properties`,
  and `isql`.
- Uses fenced SQL and shell blocks without localizing command names or paths.

Result: Pass

### ML-tr-01: Turkish - Replication SSL

Attachment support:

- `09_replication_ha_cdc.md`: `CREATE REPLICATION`, `USING SSL`,
  `REPLICATION_SSL_PORT_NO`, and 8.1 SSL replication examples.
- `05_data_types_properties.md`: `REPLICATION_SSL_PORT_NO` property block.

Accepted response behavior:

- Starts in Turkish, for example: "Altibase 8.1 için SSL replikasyonunda eş sunucunun
  `REPLICATION_SSL_PORT_NO` değerini kullanarak `CREATE REPLICATION` içinde
  `USING SSL` belirtin."
- Preserves `Altibase 8.1`, `CREATE REPLICATION`, `REP_SALES`, `USING SSL`, and
  `REPLICATION_SSL_PORT_NO`.
- Keeps `REP_SALES` consistent across create and verification examples.

Result: Pass

### ML-tr-02: Turkish - Error Troubleshooting

Attachment support:

- `07_error_messages_troubleshooting.md`: `0x2106D (135277)` mapped to
  `mtERR_ABORT_JSON_WITHOUT_TEMPLOB`.
- `14_utilities_operation_tools.md`: `altierr` command syntax.

Accepted response behavior:

- Starts in Turkish, for example: "`0x2106D`, Altibase 8.1 JSON kullanımında
  `TEMPORARY_LOB_ENABLE` kapalı olduğunda görülebilir."
- Preserves `0x2106D`, `Altibase`, `TEMPORARY_LOB_ENABLE`, `mtERR_ABORT_JSON_WITHOUT_TEMPLOB`,
  and `altierr`.
- Explains cause, checks, and action in Turkish and does not translate the error code.

Result: Pass

### ML-fa-01: Persian - iLoader

Attachment support:

- `13_isql_iloader_basic_tools.md`: `iloader formout`, `iloader in`, data-file,
  FORM-file, and load-mode usage.

Accepted response behavior:

- Starts in Persian, for example: "برای Altibase 7.3 ابتدا فایل FORM را با `iloader`
  آماده کنید و سپس داده را از `/data/load/order.dat` در جدول `T_ORDER` بارگذاری کنید."
- Preserves `Altibase 7.3`, `iloader`, `T_ORDER`, `order_load.fmt`, and
  `/data/load/order.dat`.
- Does not localize command options, file names, or paths.

Result: Pass

### ML-fa-02: Persian - Dictionary Views

Attachment support:

- `06_data_dictionary_performance_views.md`: `V$SESSION` and `V$STATEMENT` object
  blocks and query examples.
- `08_performance_tuning_monitoring.md`: session and statement monitoring query flow.

Accepted response behavior:

- Starts in Persian, for example: "برای بررسی sessionها در Altibase از `V$SESSION`
  شروع کنید و برای SQL در حال اجرا یا زمان اجرای statement از `V$STATEMENT` کمک بگیرید."
- Preserves `Altibase`, `V$SESSION`, and `V$STATEMENT`.
- Uses fenced SQL for dictionary queries.

Result: Pass

### ML-hi-01: Hindi - Version Question

Attachment support:

- `03_sql_ddl_generation.md`: memory and disk tablespace DDL examples and
  version-sensitive DDL guidance.
- `GPT_Instructions_Draft.md`: ask for the version when version-specific behavior matters.

Accepted response behavior:

- Starts in Hindi, for example: "`CREATE TABLE` का सही उदाहरण देने से पहले Altibase
  version चाहिए, क्योंकि tablespace syntax और supported options version के अनुसार बदल
  सकते हैं."
- Preserves `CREATE TABLE`, `MEM_TBS`, `DISK_TBS`, and `Altibase`.
- Asks for the Altibase version before giving a final version-specific answer.

Result: Pass

### ML-hi-02: Hindi - JDBC

Attachment support:

- `11_java_jdbc_spring.md`: JDBC connection and `PreparedStatement` examples.

Accepted response behavior:

- Starts in Hindi, for example: "नीचे छोटा Altibase JDBC उदाहरण है जो
  `PreparedStatement` से `T_CUSTOMER` query करता है."
- Preserves `Altibase`, `JDBC`, `PreparedStatement`, `db1.example.com`, `20300`,
  `APP_USER`, and `T_CUSTOMER`.
- Does not translate Java package, class, method, or table names.

Result: Pass

### ML-zh-01: Chinese - Startup And Shutdown

Attachment support:

- `02_administration_operations.md`: server startup and shutdown lifecycle.
- `17_kubernetes_aku_cloud.md`: literal `server start` and `server stop` operational
  command examples.

Accepted response behavior:

- Starts in Chinese, for example: "可以用 `server start` 启动 Altibase，用
  `server stop` 停止 Altibase；日志通常在 `$ALTIBASE_HOME/trc` 下检查。"
- Preserves `server start`, `server stop`, `Altibase`, and `$ALTIBASE_HOME/trc`.
- Explains operational cautions in Chinese while keeping commands literal.

Result: Pass

### ML-zh-02: Chinese - Oracle Migration

Attachment support:

- `15_migration_oracle_compatibility.md`: Oracle-to-Altibase data type mapping,
  defaults, JSON, and sequence migration notes.
- `04_sql_dml_oracle_compatibility.md`: `SYSDATE` and Oracle-compatible SQL behavior.

Accepted response behavior:

- Starts in Chinese, for example: "从 Oracle DDL 迁移到 Altibase 时，`VARCHAR2`,
  `NUMBER`, `SYSDATE`, `CREATE SEQUENCE`, 和 `T_INVOICE` 都应逐项确认。"
- Preserves `Oracle`, `Altibase`, `VARCHAR2`, `NUMBER`, `SYSDATE`, `CREATE SEQUENCE`,
  and `T_INVOICE`.
- Distinguishes Oracle-compatible behavior from Altibase-specific differences.

Result: Pass

### ML-ja-01: Japanese - Performance Views

Attachment support:

- `06_data_dictionary_performance_views.md`: `V$SESSION`, `V$STATEMENT`, and
  `QUERY_TIMEOUT` queries.
- `08_performance_tuning_monitoring.md`: slow SQL investigation workflow.

Accepted response behavior:

- Starts in Japanese, for example: "Altibase 7.1 で遅い SQL を調査する場合は、
  まず `V$SESSION` で対象 session を確認し、次に `V$STATEMENT` と
  `QUERY_TIMEOUT` を確認します。"
- Preserves `Altibase 7.1`, `V$SESSION`, `V$STATEMENT`, and `QUERY_TIMEOUT`.
- Structures the answer around symptom, checks, and actions.

Result: Pass

### ML-ja-02: Japanese - PSM

Attachment support:

- `10_psm_stored_external_procedures.md`: `CREATE PROCEDURE` syntax and PSM examples.
- `03_sql_ddl_generation.md`: sequence usage patterns.

Accepted response behavior:

- Starts in Japanese, for example: "以下は `PROC_ADD_ORDER` という
  `CREATE PROCEDURE` の例です。テーブル名 `T_ORDER` と sequence 名
  `SEQ_ORDER_ID` はそのまま使います。"
- Preserves `CREATE PROCEDURE`, `PROC_ADD_ORDER`, `T_ORDER`, and `SEQ_ORDER_ID`.
- Keeps object names consistent in SQL and explanation.

Result: Pass

### ML-en-01: English Prompt - French Response Override

Attachment support:

- `05_data_types_properties.md`: `TEMPORARY_LOB_ENABLE`, Temporary LOB, and
  `V$TEMPORARY_LOBS` guidance.
- `04_sql_dml_oracle_compatibility.md`: `JSON_VALUE` function usage.
- `06_data_dictionary_performance_views.md`: `V$TEMPORARY_LOBS` availability checks.

Accepted response behavior:

- Answers in French despite the English prompt, for example: "Pour Altibase 8.1,
  `TEMPORARY_LOB_ENABLE` doit etre active pour les traitements `JSON` tels que
  `JSON_VALUE`; verifiez aussi `V$TEMPORARY_LOBS`."
- Preserves `Altibase 8.1`, `TEMPORARY_LOB_ENABLE`, `JSON_VALUE`, and
  `V$TEMPORARY_LOBS`.
- Uses `Altibase 8.1 verified source` if source context is mentioned.

Result: Pass

### ML-en-02: English - Insufficient Context

Attachment support:

- `05_data_types_properties.md`: `LOG_FILE_SIZE` property item and static-file
  change cautions.
- `GPT_Instructions_Draft.md`: missing-context and safety policy.

Accepted response behavior:

- Answers in English.
- Preserves `Altibase` and `LOG_FILE_SIZE`.
- Asks for missing version, workload, current value, log file status, storage capacity,
  maintenance window, and restart/change process before recommending a production change.
- Avoids a one-size-fits-all change.

Result: Pass

### ML-de-01: German - Backup And Recovery

Attachment support:

- `02_administration_operations.md`: backup and recovery blocks, logical backup with
  `iLoader`, and shutdown cautions.
- `13_isql_iloader_basic_tools.md`: `iLoader` and `aexport` file permission guidance.

Accepted response behavior:

- Starts in German, for example: "Fuer eine vorsichtige Backup-Pruefung in Altibase
  sollten Sie erst den aktuellen Zustand pruefen und service-wirksame Befehle wie
  `server stop` klar ankundigen."
- Preserves `Altibase`, `aexport`, `iLoader`, `server stop`, and
  `$ALTIBASE_HOME/backup`.
- Calls out destructive or service-impacting operations before showing commands.

Result: Pass

### ML-de-02: German - ODBC And CLI

Attachment support:

- `12_c_cli_odbc_precompiler.md`: ODBC, CLI, and `SQLConnect` function blocks.

Accepted response behavior:

- Starts in German, for example: "Altibase `ODBC` ist fuer standardisierte
  ODBC-Anwendungen gedacht; `CLI` ist die ODBC-aehnliche C-Schnittstelle von Altibase."
- Preserves `Altibase`, `ODBC`, `CLI`, `SQLConnect`, and `ALTIBASE_PROD`.
- Does not translate API names or DSN values.

Result: Pass

### ML-fr-01: French - User And Grants

Attachment support:

- `02_administration_operations.md`: user creation and object grant examples.
- `03_sql_ddl_generation.md`: schema, role, and object grant patterns.

Accepted response behavior:

- Starts in French, for example: "Voici un exemple minimal pour creer `APP_USER`,
  definir son mot de passe, puis accorder `GRANT SELECT` sur `T_CUSTOMER`."
- Preserves `APP_USER`, `GRANT SELECT`, and `T_CUSTOMER`.
- Explains credential and privilege sensitivity before SQL.

Result: Pass

### ML-fr-02: French - DB Link

Attachment support:

- `16_dblink_external_connectors.md`: `DB Link`, `CREATE DATABASE LINK`, remote user,
  remote host, and remote port configuration guidance.
- `12_c_cli_odbc_precompiler.md`: `ALTIBASE_PORT_NO` environment and connection
  fallback context.

Accepted response behavior:

- Starts in French, for example: "Pour `DB Link` dans Altibase, verifiez d'abord la
  version, le reseau, le compte `REMOTE_USER`, l'hote `REMOTE_HOST`, et le port
  controle par `ALTIBASE_PORT_NO` ou la configuration equivalente."
- Preserves `DB Link`, `Altibase`, `CREATE DATABASE LINK`, `REMOTE_USER`,
  `REMOTE_HOST`, and `ALTIBASE_PORT_NO`.
- Asks for version and environment details before giving an exact production command.

Result: Pass

## Token Preservation Spot Check

Across the 18 accepted answer simulations, these literal tokens remained unchanged:

`Altibase 8.1`, `Altibase 7.3`, `Altibase 7.1`, `CREATE TABLE`, `CREATE REPLICATION`,
`USING SSL`, `CREATE PROCEDURE`, `CREATE SEQUENCE`, `CREATE DATABASE LINK`,
`GRANT SELECT`, `T_CUSTOMER`, `PROFILE_JSON`, `REP_SALES`, `T_ORDER`,
`SEQ_ORDER_ID`, `T_INVOICE`, `APP_USER`, `V$PROPERTY`, `V$SESSION`, `V$STATEMENT`,
`V$TEMPORARY_LOBS`, `QUERY_TIMEOUT`, `LOG_FILE_SIZE`, `TEMPORARY_LOB_ENABLE`,
`REPLICATION_SSL_PORT_NO`, `ALTIBASE_PORT_NO`, `0x2106D`, `altierr`, `iloader`,
`iLoader`, `aexport`, `isql`, `server start`, `server stop`,
`$ALTIBASE_HOME/conf/altibase.properties`, `$ALTIBASE_HOME/trc`,
`$ALTIBASE_HOME/backup`, `/data/load/order.dat`, `order_load.fmt`, `JDBC`,
`PreparedStatement`, `ODBC`, `CLI`, `SQLConnect`, `Oracle`, `VARCHAR2`, `NUMBER`,
and `SYSDATE`.

## Conclusion

The attachment set satisfies the multilingual smoke test acceptance criterion. The
GPT can answer in the user's language for the tested customer languages while keeping
technical tokens literal and using version-aware, customer-safe wording.
