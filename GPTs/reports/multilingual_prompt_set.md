# Multilingual Prompt Set

Job: `JOB-024`
Status: work output
Prompt count: 18

Purpose: provide reusable multilingual smoke-test prompts for the Altibase GPT answer
language policy. The prompts cover Vietnamese, Turkish, Persian, Hindi, Chinese,
Japanese, English, German, and French.

## Source Basis

- `GPTs/attachments/README.md`: canonical English attachment and multilingual answer policy.
- `GPTs/GPT_Instructions_Draft.md`: answer language, version, SQL naming, and safety policy.
- `GPTs/internal/terminology_glossary.md`: literal token patterns and customer-safe source labels.

## Common Pass Conditions

For every prompt below, the expected answer should:

- Answer in the user's language unless the prompt explicitly asks for another language.
- Preserve literal technical tokens exactly, including SQL object names, SQL keywords,
  function names, error codes, property names, commands, options, file paths, API names,
  connector names, and version labels.
- Preserve casing, punctuation, underscores, `$`, and version numbers in tokens such as
  `T_CUSTOMER`, `V$PROPERTY`, `REPLICATION_SSL_PORT_NO`, `$ALTIBASE_HOME/conf`, and
  `Altibase 8.1`.
- Ask for the Altibase version when the correct answer depends on version-specific
  behavior and the user did not provide a version.
- If a source label is needed for 8.1, use `Altibase 8.1 verified source` and do not
  expose internal repository names, branch names, workstation paths, or build labels.
- Avoid inventing unsupported syntax, properties, error codes, or version claims.

## Prompt Set

### ML-vi-01 - Vietnamese - JSON DDL

Prompt:

```text
Tôi đang dùng Altibase 8.1. Hãy tạo ví dụ `CREATE TABLE` cho bảng `T_CUSTOMER` có cột `CUST_ID`, `PROFILE_JSON`, và chỉ ra cách kiểm tra giá trị bằng `JSON_VALUE`. Đừng đổi tên `T_CUSTOMER` hoặc `PROFILE_JSON`.
```

Expected policy checks:

- Answer in Vietnamese.
- Preserve `Altibase 8.1`, `CREATE TABLE`, `T_CUSTOMER`, `CUST_ID`, `PROFILE_JSON`, and `JSON_VALUE`.
- If source context is mentioned, use `Altibase 8.1 verified source`.

### ML-vi-02 - Vietnamese - Property And Path

Prompt:

```text
Giải thích cách kiểm tra thuộc tính `QUERY_TIMEOUT` trong `V$PROPERTY` và tệp `$ALTIBASE_HOME/conf/altibase.properties`. Tôi cần câu lệnh `isql` tối thiểu để kiểm tra.
```

Expected policy checks:

- Answer in Vietnamese.
- Preserve `QUERY_TIMEOUT`, `V$PROPERTY`, `$ALTIBASE_HOME/conf/altibase.properties`, and `isql`.
- Ask for version only if the answer needs version-specific detail.

### ML-tr-01 - Turkish - Replication SSL

Prompt:

```text
Altibase 8.1 için `CREATE REPLICATION` örneği yaz. Nesne adı `REP_SALES` olsun ve SSL için `USING SSL` ile `REPLICATION_SSL_PORT_NO` kullanılsın. Ayrıca nasıl doğrulayacağımı göster.
```

Expected policy checks:

- Answer in Turkish.
- Preserve `Altibase 8.1`, `CREATE REPLICATION`, `REP_SALES`, `USING SSL`, and `REPLICATION_SSL_PORT_NO`.
- Keep generated SQL identifiers consistent across create and verification examples.

### ML-tr-02 - Turkish - Error Troubleshooting

Prompt:

```text
`0x2106D` hatasını gördüm. Altibase içinde olası nedenleri, kontrol etmem gereken günlükleri ve `altierr` ile nasıl bakacağımı açıklar mısın?
```

Expected policy checks:

- Answer in Turkish.
- Preserve `0x2106D`, `Altibase`, and `altierr`.
- If the exact error is not covered by attachments, say what is missing and provide the safest next check.

### ML-fa-01 - Persian - iLoader

Prompt:

```text
برای Altibase 7.3 یک نمونه دستور `iloader` برای بارگذاری داده در جدول `T_ORDER` بده. نام فایل کنترل را `order_load.fmt` و مسیر داده را `/data/load/order.dat` نگه دار.
```

Expected policy checks:

- Answer in Persian.
- Preserve `Altibase 7.3`, `iloader`, `T_ORDER`, `order_load.fmt`, and `/data/load/order.dat`.
- Do not localize command options, file names, or paths.

### ML-fa-02 - Persian - Dictionary Views

Prompt:

```text
چطور در Altibase وضعیت sessionها را با `V$SESSION` بررسی کنم؟ اگر لازم است از `V$STATEMENT` هم مثال بزن، اما نام viewها را تغییر نده.
```

Expected policy checks:

- Answer in Persian.
- Preserve `Altibase`, `V$SESSION`, and `V$STATEMENT`.
- Use fenced SQL for dictionary queries.

### ML-hi-01 - Hindi - Version Question

Prompt:

```text
मुझे `CREATE TABLE` में memory tablespace और disk tablespace के लिए उदाहरण चाहिए। मेरी tablespace names `MEM_TBS` और `DISK_TBS` हैं, लेकिन मैंने Altibase version नहीं बताया है।
```

Expected policy checks:

- Answer in Hindi.
- Preserve `CREATE TABLE`, `MEM_TBS`, `DISK_TBS`, and `Altibase`.
- Ask for the Altibase version if syntax, defaults, or feature behavior could differ by version.

### ML-hi-02 - Hindi - JDBC

Prompt:

```text
Altibase JDBC connection के लिए `PreparedStatement` वाला छोटा Java example दें। Host `db1.example.com`, port `20300`, user `APP_USER`, और table `T_CUSTOMER` रखें।
```

Expected policy checks:

- Answer in Hindi.
- Preserve `Altibase`, `JDBC`, `PreparedStatement`, `db1.example.com`, `20300`, `APP_USER`, and `T_CUSTOMER`.
- Do not translate package, class, method, or table names.

### ML-zh-01 - Chinese - Startup And Shutdown

Prompt:

```text
请用中文说明如何用 `server start` 和 `server stop` 启动、停止 Altibase，并说明如何查看 `$ALTIBASE_HOME/trc` 中的日志。
```

Expected policy checks:

- Answer in Chinese.
- Preserve `server start`, `server stop`, `Altibase`, and `$ALTIBASE_HOME/trc`.
- Keep commands literal and explain operational cautions in Chinese.

### ML-zh-02 - Chinese - Oracle Migration

Prompt:

```text
我正在把 Oracle DDL 迁移到 Altibase。请说明 `VARCHAR2`, `NUMBER`, `SYSDATE`, `CREATE SEQUENCE`, 和表名 `T_INVOICE` 需要注意什么。
```

Expected policy checks:

- Answer in Chinese.
- Preserve `Oracle`, `Altibase`, `VARCHAR2`, `NUMBER`, `SYSDATE`, `CREATE SEQUENCE`, and `T_INVOICE`.
- Distinguish Oracle-compatible behavior from Altibase-specific differences.

### ML-ja-01 - Japanese - Performance Views

Prompt:

```text
Altibase 7.1 で遅い SQL を調査したいです。`V$SESSION`, `V$STATEMENT`, `QUERY_TIMEOUT` を使って確認する手順を日本語で説明してください。
```

Expected policy checks:

- Answer in Japanese.
- Preserve `Altibase 7.1`, `V$SESSION`, `V$STATEMENT`, and `QUERY_TIMEOUT`.
- Structure troubleshooting around symptom, checks, and actions.

### ML-ja-02 - Japanese - PSM

Prompt:

```text
`CREATE PROCEDURE` の簡単な例を `PROC_ADD_ORDER` という名前で作ってください。テーブル名は `T_ORDER`、sequence 名は `SEQ_ORDER_ID` のままにしてください。
```

Expected policy checks:

- Answer in Japanese.
- Preserve `CREATE PROCEDURE`, `PROC_ADD_ORDER`, `T_ORDER`, and `SEQ_ORDER_ID`.
- Keep generated object names consistent in SQL and explanation.

### ML-en-01 - English - Explicit Response Language Override

Prompt:

```text
Answer in French: for Altibase 8.1, explain how `TEMPORARY_LOB_ENABLE` relates to JSON functions such as `JSON_VALUE`, and include a check using `V$TEMPORARY_LOBS`.
```

Expected policy checks:

- Answer in French because the user explicitly requested it, even though the prompt is written in English.
- Preserve `Altibase 8.1`, `TEMPORARY_LOB_ENABLE`, `JSON_VALUE`, and `V$TEMPORARY_LOBS`.
- If source context is mentioned, use `Altibase 8.1 verified source`.

### ML-en-02 - English - Insufficient Context

Prompt:

```text
For my production Altibase system, should I change `LOG_FILE_SIZE` today? I did not provide the Altibase version, workload, current value, or log file status.
```

Expected policy checks:

- Answer in English.
- Preserve `Altibase` and `LOG_FILE_SIZE`.
- Ask for missing version and operational context instead of giving an unsafe one-size-fits-all change.

### ML-de-01 - German - Backup And Recovery

Prompt:

```text
Erkläre auf Deutsch eine vorsichtige Backup-Prüfung für Altibase. Behalte die Befehle `aexport`, `iLoader`, `server stop` und den Pfad `$ALTIBASE_HOME/backup` unverändert.
```

Expected policy checks:

- Answer in German.
- Preserve `Altibase`, `aexport`, `iLoader`, `server stop`, and `$ALTIBASE_HOME/backup`.
- Call out destructive or service-impacting operations before showing commands.

### ML-de-02 - German - ODBC And CLI

Prompt:

```text
Ich brauche eine kurze Erklärung zu Altibase `ODBC` und `CLI`. Bitte nenne, wann `SQLConnect` verwendet wird, und behalte den DSN-Namen `ALTIBASE_PROD` unverändert.
```

Expected policy checks:

- Answer in German.
- Preserve `Altibase`, `ODBC`, `CLI`, `SQLConnect`, and `ALTIBASE_PROD`.
- Do not translate API names or DSN values.

### ML-fr-01 - French - User And Grants

Prompt:

```text
En français, montre comment créer l'utilisateur `APP_USER`, définir le mot de passe, puis faire `GRANT SELECT` sur `T_CUSTOMER`. Garde les noms `APP_USER` et `T_CUSTOMER` tels quels.
```

Expected policy checks:

- Answer in French.
- Preserve `APP_USER`, `GRANT SELECT`, and `T_CUSTOMER`.
- Explain any destructive or security-sensitive step before SQL when applicable.

### ML-fr-02 - French - DB Link

Prompt:

```text
Explique en français les points à vérifier pour `DB Link` dans Altibase. Inclue les noms `CREATE DATABASE LINK`, `REMOTE_USER`, `REMOTE_HOST`, et `ALTIBASE_PORT_NO` sans les traduire.
```

Expected policy checks:

- Answer in French.
- Preserve `DB Link`, `Altibase`, `CREATE DATABASE LINK`, `REMOTE_USER`, `REMOTE_HOST`, and `ALTIBASE_PORT_NO`.
- Ask for version and environment details if required for an exact command.

## Coverage Summary

| Language | Prompt IDs | Main Policy Coverage |
| --- | --- | --- |
| Vietnamese | `ML-vi-01`, `ML-vi-02` | Same-language answers, SQL names, JSON functions, properties, paths, commands |
| Turkish | `ML-tr-01`, `ML-tr-02` | Replication SSL literals, error code troubleshooting, command names |
| Persian | `ML-fa-01`, `ML-fa-02` | RTL-language answers, utility commands, file paths, dictionary views |
| Hindi | `ML-hi-01`, `ML-hi-02` | Version clarification, tablespace names, JDBC/API names |
| Chinese | `ML-zh-01`, `ML-zh-02` | Commands, paths, migration terms, Oracle compatibility tokens |
| Japanese | `ML-ja-01`, `ML-ja-02` | Performance views, properties, PSM object names |
| English | `ML-en-01`, `ML-en-02` | Explicit response-language override, 8.1 source label, insufficient context |
| German | `ML-de-01`, `ML-de-02` | Operational commands, backup caution, ODBC/CLI API names |
| French | `ML-fr-01`, `ML-fr-02` | Security SQL, grants, DB Link terms, properties |
