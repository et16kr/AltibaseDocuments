# R21 Java, JDBC, Spring, and Hibernate

Date: 2026-05-16
Reviewer: Codex
Verdict: Pass

## Scope

- Attachments:
  - `GPTs/attachments/11_java_jdbc_spring.md`
  - `GPTs/attachments/16_dblink_external_connectors.md`
- Supporting reports:
  - `GPTs/reports/source_inventory.md`
  - `GPTs/reports/eng_kor_parity.md`
- Source manuals sampled:
  - `Manuals/Altibase_7.1/kor/JDBC User's Manual.md`
  - `Manuals/Altibase_7.3/kor/JDBC User's Manual.md`
  - `Manuals/Altibase_trunk/kor/JDBC User's Manual.md`
  - `Manuals/Altibase_7.1/kor/Adapter for JDBC User's Manual.md`
  - `Manuals/Altibase_7.3/kor/Adapter for JDBC User's Manual.md`
  - `Manuals/Altibase_trunk/kor/Adapter for JDBC User's Manual.md`
  - `Manuals/Altibase_7.1/kor/DB Link User's Manual.md`
  - `Manuals/Altibase_7.3/kor/DB Link User's Manual.md`
  - `Manuals/Altibase_trunk/kor/DB Link User's Manual.md`
  - `Manuals/Altibase_7.1/kor/Altibase SSL TLS User's Guide.md`
  - `Manuals/Altibase_7.3/kor/Altibase SSL TLS User's Guide.md`
  - `Manuals/Altibase_trunk/kor/Altibase SSL TLS User's Guide.md`
  - `Manuals/Altibase_7.1/kor/Hadoop Connector User's Manual.md`
  - `Manuals/Altibase_7.3/kor/Hadoop Connector User's Manual.md`
  - `Manuals/Altibase_trunk/kor/Hadoop Connector User's Manual.md`
  - `Manuals/Tools/Altibase_release/kor/Altibase 3rd Party Connector Guide.md`
  - `Manuals/Tools/Altibase_trunk/kor/Altibase 3rd Party Connector Guide.md`
  - `Technical Documents/kor/JavaCompatibility.md`
  - `3rd Party Guide for Altibase/kor/Spring Data JPA User's Guide for Altibase.md`
  - `3rd Party Guide for Altibase/kor/Spring Data JPA with Hibernate 6.4 User's Guide for Altibase.md`
  - `ReleaseNotes/kor/Altibase_7_3_0_0_1_Release_Notes.md`
  - `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`

## Commands Run

```bash
bash review/scripts/run_review_remediation_cycle.sh status
rg -n $'\t(Reviewing|Remediating|ReReviewing|Fail)$' review/review_remediation_cycle_status.tsv
git status --short
sed -n '1,240p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,220p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,220p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
git diff -- GPTs/attachments/11_java_jdbc_spring.md GPTs/attachments/16_dblink_external_connectors.md GPTs/reports/source_inventory.md GPTs/reports/eng_kor_parity.md review/review_remediation_cycle_status.tsv review/review_stage_status.tsv
rg -n "^(#|##|###|####) " GPTs/attachments/11_java_jdbc_spring.md GPTs/attachments/16_dblink_external_connectors.md
nl -ba GPTs/attachments/11_java_jdbc_spring.md | sed -n '1,1450p'
nl -ba GPTs/attachments/16_dblink_external_connectors.md | sed -n '1,1605p'
rg -n "alternateservers|connectionretrycount|connectionretrydelay|sessionfailover|jdbc:Altibase://datasource_name|sys=user|lob_null_select|socket_immediate_close|stmt_cache|Altibase42|createBlob|createClob|createNClob" "Manuals/Altibase_7.1/kor/JDBC User's Manual.md" "Manuals/Altibase_7.3/kor/JDBC User's Manual.md" "Manuals/Altibase_trunk/kor/JDBC User's Manual.md"
rg -n "ADAPTER_LOB_TYPE_SUPPORT|7\.1\.0\.6\.9|7\.1\.0\.7\.0|OTHER_DATABASE_BATCH_DML_MAX_SIZE|JDBC_ADAPTER_HOME|6\.3\.1|DDL|RESET OFFLINE META" "Manuals/Altibase_7.1/kor/Adapter for JDBC User's Manual.md" "Manuals/Altibase_7.3/kor/Adapter for JDBC User's Manual.md" "Manuals/Altibase_trunk/kor/Adapter for JDBC User's Manual.md"
rg -n "Homogeneous|Heterogeneous|6\.5\.1|ALTILINKER_ENABLE|DBLINK_ENABLE|CREATE DATABASE LINK|DROP DATABASE LINK|IF NOT EXISTS|IF EXISTS|JRE|Java|1\.8|REMOTE_TABLE|REMOTE_EXECUTE_IMMEDIATE|DBLINK_GLOBAL_TRANSACTION_LEVEL" "Manuals/Altibase_7.1/kor/DB Link User's Manual.md" "Manuals/Altibase_7.3/kor/DB Link User's Manual.md" "Manuals/Altibase_trunk/kor/DB Link User's Manual.md"
rg -n "Altibase\.jar|Altibase42\.jar|Adapter for JDBC|DB Link|Java 5|Java 8|Java 9|Java 11|17|21|7\.1\.0\.2\.5|7\.1\.0\.2\.6|7\.3" "Technical Documents/kor/JavaCompatibility.md"
rg -n "Spring Boot|Hibernate|6\.4|7\.3\.0\.0\.2|7\.1\.0\.9\.2|7\.1\.0\.9\.3|lob_null_select|hibernate-community-dialects|AltibaseDialect|createNClob|non_contextual_creation|JDBC" "3rd Party Guide for Altibase/kor/Spring Data JPA User's Guide for Altibase.md" "3rd Party Guide for Altibase/kor/Spring Data JPA with Hibernate 6.4 User's Guide for Altibase.md"
rg -n "ssl_protocols|TLSv|TLS" "Manuals/Altibase_7.1/kor/Altibase SSL TLS User's Guide.md" "Manuals/Altibase_7.3/kor/Altibase SSL TLS User's Guide.md" "Manuals/Altibase_trunk/kor/Altibase SSL TLS User's Guide.md"
rg -n "DBeaver|23\.3\.3|DBMS_METADATA|GoldenGate|12\.3|OpenLDAP|Hibernate" "Manuals/Tools/Altibase_release/kor/Altibase 3rd Party Connector Guide.md" "Manuals/Tools/Altibase_trunk/kor/Altibase 3rd Party Connector Guide.md"
rg -n "Hadoop|Sqoop|1\.4\.4|JDK|JRE|BLOB|CLOB|allowinsert|AltibaseManager|sqoop export" "Manuals/Altibase_7.1/kor/Hadoop Connector User's Manual.md" "Manuals/Altibase_7.3/kor/Hadoop Connector User's Manual.md" "Manuals/Altibase_trunk/kor/Hadoop Connector User's Manual.md"
rg -n "jdbc:Altibase://datasource_name|7\.1\.0\.6\.9|7\.1\.0\.7\.0|Altibase version 6\.5\.1|Homogeneous Link|IF NOT EXISTS|IF EXISTS" "Manuals/Altibase_7.1/eng/JDBC User's Manual.md" "Manuals/Altibase_7.3/eng/JDBC User's Manual.md" "Manuals/Altibase_trunk/eng/JDBC User's Manual.md" "Manuals/Altibase_7.1/eng/Adapter for JDBC User's Manual.md" "Manuals/Altibase_7.3/eng/Adapter for JDBC User's Manual.md" "Manuals/Altibase_trunk/eng/Adapter for JDBC User's Manual.md" "Manuals/Altibase_7.1/eng/DB Link User's Manual.md" "Manuals/Altibase_7.3/eng/DB Link User's Manual.md" "Manuals/Altibase_trunk/eng/DB Link User's Manual.md"
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name README.md | sort | wc -l
git diff --check
rg -n "trunk|/home/|file://|!\[|media/|TODO|FIXME" GPTs/attachments/11_java_jdbc_spring.md GPTs/attachments/16_dblink_external_connectors.md
rg -n "^Verdict:|^\| (Blocker|High|Medium|Low) \|" review/reports/R21_java_jdbc_spring.md
git status --short
```

## Findings

No actionable Blocker, High, Medium, or Low findings were found in this R21 re-review.

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Note | `GPTs/attachments/11_java_jdbc_spring.md`; `GPTs/attachments/16_dblink_external_connectors.md` | N/A | The prior R21 issues appear remediated in the current local attachment revisions: DB Link Homogeneous Link is now marked unsupported for 7.1/7.3/8.1 target guidance, Adapter LOB support is split by source version, `alternateservers` no longer states an unsupported two-server limit, the DSN URL literal is preserved, and DB Link Java compatibility is surfaced. | No R21 remediation is required. Preserve the current source-backed version cautions during later cleanup. |

## Source Checks

- Claims checked:
  - JDBC driver class and URL forms, URL attribute precedence, failover properties, DSN URL literals, SSL/TLS JDBC keys, statement cache keys, LOB and JDBC 4.2 method support, SQLSTATE blocks, Maven examples, Spring Boot/Hibernate 6.4 setup, Adapter for JDBC properties and LOB handling, DB Link architecture and syntax, DB Link Java runtime requirements, Hadoop Connector requirements, DBeaver cautions, Hibernate connector notes, OpenLDAP ODBC setup, and Oracle GoldenGate for Big Data JDBC Handler scope.
- Source coverage:
  - `alternateservers` in `GPTs/attachments/11_java_jdbc_spring.md:297-301` matches the repeated-list grammar in the Korean JDBC manuals (`7.1:589`, `7.3:530`, `8.1-source:530`).
  - The DSN URL example in `GPTs/attachments/11_java_jdbc_spring.md:358-366` preserves the source literal `jdbc:Altibase://datasource_name:20301?sys=user&password=pwd` from the Korean JDBC manuals (`7.1:1690-1692`, `7.3:1629-1631`, `8.1-source:1656-1658`).
  - `lob_null_select` defaults and Hibernate LOB guidance in `GPTs/attachments/11_java_jdbc_spring.md:220-225` and `536-545` match the 7.1 default `on` and 7.3/8.1-source default `off` in the Korean JDBC manuals and Spring/Hibernate guide.
  - Adapter LOB version lines in `GPTs/attachments/11_java_jdbc_spring.md:1364-1369` follow the Korean source split: `7.1.0.6.9` in the 7.1 Adapter manual and `7.1.0.7.0` in the 7.3 and 8.1-source Adapter manuals.
  - DB Link Homogeneous/Heterogeneous wording in `GPTs/attachments/16_dblink_external_connectors.md:144-147` follows the Korean DB Link manuals, which say Altibase `6.5.1` or later does not support Homogeneous Link.
  - DB Link Java runtime guidance in `GPTs/attachments/16_dblink_external_connectors.md:118-122` is backed by `Technical Documents/kor/JavaCompatibility.md` and the DB Link manuals' `AltiLinker` JRE setup sections.
  - Spring Boot/Hibernate 6.4 content in `GPTs/attachments/11_java_jdbc_spring.md:438-545` and `GPTs/attachments/16_dblink_external_connectors.md:1226-1299` is backed by the Korean Spring Data JPA guides for `hibernate-community-dialects`, Maven examples, `AltibaseDialect`, `spring.jpa.properties.hibernate.jdbc.lob.non_contextual_creation=true`, and `lob_null_select=off` on 7.1.
- Korean/English source conflicts:
  - DB Link Homogeneous Link has an English-source drift: English manuals say `Altibase 6.5.1 does not support Homogeneous Links`, while Korean manuals say Altibase `6.5.1` or later does not support Homogeneous Link. The attachment now follows the Korean authority.
  - Adapter for JDBC LOB support has source drift across Korean manual versions: the 7.1 Korean manual says `7.1.0.6.9`, while 7.3 and 8.1-source Korean manuals say `7.1.0.7.0`. The attachment now splits the guidance by source version.
- Source gaps:
  - No source was found for a two-alternate-server limit; the attachment now uses the manual repeated-list grammar and treats two servers as an example only.
  - JDBC 4.2 and Java compatibility remain patch-sensitive for 7.1. The attachment consistently tells users to verify the exact target driver or Adapter patch before production Java runtime guidance.

## Oracle-Overlap Decision

- Correctly compressed:
  - Generic Java, Spring, and connector boilerplate is compressed. The attachments emphasize Altibase-specific driver class names, URL parameters, LOB behavior, JDBC 4.2 boundaries, `AltibaseDialect`, Adapter for JDBC properties, DB Link `AltiLinker`, remote access methods, and connector cautions.
- Too much generic Oracle material:
  - No broad Oracle-overlap expansion was found in the sampled Java/JDBC/Spring/DB Link sections.
- Missing Altibase-specific difference:
  - No actionable omission found. The most important Altibase-specific differences for this stage are present: `lob_null_select`, unsupported `NCLOB`, `AltibaseDialect`, Adapter LOB/DDL cautions, DB Link Homogeneous Link unsupported status for target versions, `REMOTE_TABLE` versus `@`, DB Link data type limits, and connector-specific troubleshooting.

## Version Checks

- 7.1:
  - JDBC URL and DSN examples preserve literal source parameters.
  - `lob_null_select=off` is correctly required for Hibernate LOB behavior.
  - Maven and Java compatibility examples are framed as driver-patch-sensitive rather than universal 7.1 guarantees.
  - Adapter LOB support now reflects the 7.1 Korean Adapter manual's `7.1.0.6.9` start version.
  - DB Link Homogeneous Link is not presented as usable for 7.1 target guidance.
- 7.3:
  - Maven Central `com.altibase:altibase-jdbc:7.3.0.0.2`, Hibernate 6.4 guidance, `lob_null_select` default `off`, `socket_immediate_close` driver-patch limit, Java compatibility, Adapter LOB start version, and DB Link syntax are source-backed in sampled material.
  - `CREATE DATABASE LINK IF NOT EXISTS` and `DROP DATABASE LINK IF EXISTS` are not applied to 7.3.
- 8.1:
  - Altibase 8.1 verified source wording is used for JDBC, Adapter, and DB Link guidance.
  - Statement caching, JSON/Temporary LOB caution, Empty LOB caution, `CREATE DATABASE LINK IF NOT EXISTS`, and `DROP DATABASE LINK IF EXISTS` are source-backed in sampled material.
  - DB Link runtime guidance follows the 8.1-source `JRE 1.8` baseline plus the 8.1 release-note JDK 1.8-or-later compatibility statement.

## Retrieval And GPT Answer Quality

- Strengths:
  - `11_java_jdbc_spring.md` has searchable blocks for direct JDBC, failover, DataSource, Spring/Hibernate, JDBC data types and API families, SQLSTATE troubleshooting, and Adapter for JDBC.
  - `16_dblink_external_connectors.md` has task-oriented blocks for DB Link architecture, syntax, remote access methods, properties, data type support, and connector troubleshooting.
  - Literal tokens such as `jdbc:Altibase://...`, `Altibase.jdbc.driver.AltibaseDriver`, `AltibaseDialect`, `lob_null_select`, `ADAPTER_LOB_TYPE_SUPPORT`, `REMOTE_TABLE`, and `REMOTE_EXECUTE_IMMEDIATE` are preserved.
- Risks:
  - Java compatibility for 7.1 remains patch-sensitive; later answer generation should keep asking for exact driver or Adapter patch when users target newer Java runtimes.
  - JSON/JDBC binding details for Altibase 8.1 remain intentionally conservative because sampled JDBC manuals do not expand native JSON binding behavior.

## Required Follow-Up

- None for R21.
