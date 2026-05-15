# R24 DB Link, External Connectors, Kubernetes, and AKU Review

Date: 2026-05-16
Reviewer: Codex
Verdict: Pass

## Scope

- Attachments:
  - `GPTs/attachments/16_dblink_external_connectors.md`
  - `GPTs/attachments/17_kubernetes_aku_cloud.md`
- Supporting reports:
  - `GPTs/reports/source_inventory.md`
  - `GPTs/reports/image_inventory.md`
- Source manuals sampled:
  - `Manuals/Altibase_7.1/kor/DB Link User's Manual.md`
  - `Manuals/Altibase_7.3/kor/DB Link User's Manual.md`
  - `Manuals/Altibase_trunk/kor/DB Link User's Manual.md`
  - `Manuals/Altibase_7.1/kor/Hadoop Connector User's Manual.md`
  - `Manuals/Altibase_7.3/kor/Hadoop Connector User's Manual.md`
  - `Manuals/Altibase_trunk/kor/Hadoop Connector User's Manual.md`
  - `Manuals/Tools/Altibase_release/kor/Altibase 3rd Party Connector Guide.md`
  - `Manuals/Tools/Altibase_trunk/kor/Altibase 3rd Party Connector Guide.md`
  - `3rd Party Guide for Altibase/kor/Spring Data JPA with Hibernate 6.4 User's Guide for Altibase.md`
  - `3rd Party Guide for Altibase/kor/Kubernetes User's Guide for Altibase.md`
  - `3rd Party Guide for Altibase/kor/Altibase aku Sample Guide for Kubernetes.md`
  - `Manuals/Altibase_7.1/kor/Utilities Manual.md`
  - `Manuals/Altibase_7.3/kor/Utilities Manual.md`
  - `Manuals/Altibase_trunk/kor/Utilities Manual.md`
  - `ReleaseNotes/kor/Altibase_7_3_0_0_1_Release_Notes.md`
  - `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`

## Commands Run

```bash
bash review/scripts/run_review_remediation_cycle.sh status
rg -n $'\t(Reviewing|Remediating|ReReviewing|Fail)$' review/review_remediation_cycle_status.tsv
git status --short
sed -n '1,220p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,220p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,240p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
git diff -- GPTs/attachments/16_dblink_external_connectors.md GPTs/attachments/17_kubernetes_aku_cloud.md GPTs/reports/source_inventory.md review/review_remediation_cycle_status.tsv review/review_stage_status.tsv
wc -l GPTs/attachments/16_dblink_external_connectors.md GPTs/attachments/17_kubernetes_aku_cloud.md GPTs/reports/source_inventory.md GPTs/reports/image_inventory.md review/review_stages.tsv
nl -ba GPTs/attachments/16_dblink_external_connectors.md
nl -ba GPTs/attachments/17_kubernetes_aku_cloud.md
nl -ba GPTs/reports/source_inventory.md | sed -n '420,485p'
rg -n "R24|DB Link|DBeaver|GoldenGate|Hadoop|Kubernetes|AKU|aku|connector|external|16_dblink|17_kubernetes" GPTs/reports/source_inventory.md GPTs/reports/image_inventory.md review/review_stages.tsv
rg -n "trunk|Manuals/|ReleaseNotes/|3rd Party Guide|GPTs/|media/|/home/|file://|Altibase_trunk|source-image|local source|\.png|\.jpg|\.jpeg|\.gif|\.svg" GPTs/attachments/16_dblink_external_connectors.md GPTs/attachments/17_kubernetes_aku_cloud.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name README.md | sort | wc -l
rg -n "NLS_BYTE_PER_CHAR|REMOTE_TABLE_STORE|REMOTE_TABLE\(|CREATE .*DATABASE LINK|DROP .*DATABASE LINK|DBLINK_ENABLE|ALTILINKER_ENABLE|ALTILINKER_PORT_NO|DBLINK_GLOBAL_TRANSACTION_LEVEL|Homogeneous|Heterogeneous|IF NOT EXISTS|IF EXISTS|java\.sql\.Types|JRE|JDK" "Manuals/Altibase_7.1/kor/DB Link User's Manual.md" "Manuals/Altibase_7.3/kor/DB Link User's Manual.md" "Manuals/Altibase_trunk/kor/DB Link User's Manual.md"
rg -n "sqoop|AltibaseManager|altibase_sqoop14_connector|Hadoop 1\.0|Sqoop 1\.4\.4|JRE|JDK|--batch|allowinsert|BLOB|CLOB|MERGE|records.per.statement|list-tables|list-databases|--as-avrodatafile|--as-sequencefile|--hive-import" "Manuals/Altibase_7.1/kor/Hadoop Connector User's Manual.md" "Manuals/Altibase_7.3/kor/Hadoop Connector User's Manual.md" "Manuals/Altibase_trunk/kor/Hadoop Connector User's Manual.md"
rg -n "DBeaver|23\.3\.3|Altibase Server 7\.1\.0|Auto-Commit|Manual Commit|DBMS_METADATA|SYSTEM_|Show system objects|EXPLAIN_PLAN|PRINTLN|Microseconds|CHAR|Binary|OpenLDAP|back-sql|GoldenGate|JDBC Handler|AltibaseDialect|hibernate-community-dialects|lob_null_select|NClob|7\.3\.0\.0\.2|7\.1\.0\.9\.2" "Manuals/Tools/Altibase_release/kor/Altibase 3rd Party Connector Guide.md" "Manuals/Tools/Altibase_trunk/kor/Altibase 3rd Party Connector Guide.md" "3rd Party Guide for Altibase/kor/Spring Data JPA with Hibernate 6.4 User's Guide for Altibase.md"
rg -n "AKU_SERVER_COUNT|REPLICATIONS|SYNC_PARALLEL_COUNT|AKU_STS_NAME|AKU_SVC_NAME|AKU_SYS_PASSWORD|AKU_REPLICATION_RESET_AT_END|AKU_FLUSH_AT_START|AKU_FLUSH_AT_END|AKU_QUERY|aku -p|--pod|start_completed|StatefulSet|OrderedReady|publishNotReadyAddresses|ADMIN_MODE|REMOTE_SYSDBA_ENABLE|altiEncrypt" "Manuals/Altibase_7.1/kor/Utilities Manual.md" "Manuals/Altibase_7.3/kor/Utilities Manual.md" "Manuals/Altibase_trunk/kor/Utilities Manual.md" "3rd Party Guide for Altibase/kor/Kubernetes User's Guide for Altibase.md" "3rd Party Guide for Altibase/kor/Altibase aku Sample Guide for Kubernetes.md" "ReleaseNotes/kor/Altibase_7_3_0_0_1_Release_Notes.md" "ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md"
```

## Findings

No actionable `Blocker`, `High`, `Medium`, or `Low` findings remain for this stage.

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Note | N/A | N/A | R24 re-review passed after checking the current DB Link, external connector, Kubernetes, AKU, and source-inventory text against the sampled Korean sources. | No R24 remediation required. |

## Source Checks

- Claims checked:
  - DB Link architecture, `AltiLinker` placement, `DBLINK_ENABLE`, `ALTILINKER_ENABLE`, `TARGETS`, `CREATE DATABASE LINK`, `DROP DATABASE LINK`, transaction levels, remote object access, `REMOTE_TABLE`, `REMOTE_TABLE_STORE`, `REMOTE_EXECUTE_IMMEDIATE`, PSM `REMOTE_*` functions, monitoring views, and JDBC type mapping.
  - Hadoop Connector requirements, Sqoop command shapes, batch/export behavior, list commands, and import/export type support.
  - DBeaver version baseline, JDBC driver setup, LOB manual-commit behavior, `SYSTEM_` visibility, `DBMS_METADATA`, plan viewing, `EXPLAIN_PLAN`, `PRINTLN` output, DATE microsecond display, binary/bit-type caveats, and auto-commit setup.
  - Hibernate 6.4 `AltibaseDialect`, `hibernate-community-dialects`, Maven JDBC examples, `lob_null_select`, and `NClob` handling.
  - OpenLDAP `back-sql` Altibase ODBC mapping and Oracle GoldenGate for Big Data JDBC Handler boundary.
  - Kubernetes `Pod`, `Deployment`, `Service`, PV/PVC, StatefulSet, AKU command syntax, `aku.conf`, lifecycle flows, `AKU_SERVER_COUNT`, multiple `REPLICATIONS`, and recovery cautions.
- Source coverage:
  - `TARGETS/NLS_BYTE_PER_CHAR` is now present in the DB Link sample, cautions, and property list, matching the Korean DB Link manuals.
  - `REMOTE_TABLE_STORE` is now defined as a separate remote-access method, matching the Korean DB Link manuals.
  - Multiple `REPLICATIONS` blocks are now version-framed across 7.1, 7.3, and Altibase 8.1 verified source, while replica-count limits remain separate.
  - `GPTs/reports/source_inventory.md` now lists Korean Hadoop, Kubernetes/AKU, Utilities, and Spring Hibernate 6.4 sources for the scoped attachments.
- Korean/English source conflicts:
  - No unresolved Korean/English conflict was found in the sampled DB Link, Hadoop, third-party connector, Kubernetes, or AKU material.
  - The prior AKU source tension is resolved in the attachment by distinguishing 8.1 release-note emphasis from Utilities Manual examples that document comma-separated `REPLICATIONS` blocks in 7.1 and 7.3 as well.
- Source gaps:
  - None requiring R24 remediation. Live connector execution, cluster deployment, and third-party product installation were not tested; the attachments appropriately limit themselves to source-backed Altibase-facing behavior and delegate third-party product details.

## Oracle-Overlap Decision

- Correctly compressed:
  - Generic SQL, generic JDBC setup, generic Kubernetes platform design, and generic Oracle GoldenGate product administration are kept brief or delegated to the relevant product manuals.
  - The material focuses on Altibase-specific DB Link behavior, connector parameters, metadata mapping, AKU lifecycle, replication reset behavior, and version-sensitive constraints.
- Too much generic Oracle material:
  - None found.
- Missing Altibase-specific difference:
  - None requiring R24 remediation. DB Link character-length conversion and AKU multiple-`REPLICATIONS` behavior are now represented.

## Version Checks

- 7.1:
  - DB Link excludes 8.1-only `IF EXISTS` / `IF NOT EXISTS` syntax.
  - Hadoop Connector requirements and commands are stable against the 7.1 Korean source.
  - AKU `AKU_SERVER_COUNT` is stated as 1 to 4, and multiple `REPLICATIONS` blocks are no longer incorrectly treated as 8.1-only.
- 7.3:
  - DB Link, Hadoop Connector, DBeaver, OpenLDAP, and GoldenGate guidance is stable against sampled 7.3/release Korean sources.
  - AKU `AKU_SERVER_COUNT` is stated as 1 to 6, and multiple `REPLICATIONS` blocks are included for 7.3.
  - Hibernate guidance correctly distinguishes 7.3 Maven/JDBC and `lob_null_select` behavior from 7.1.
- 8.1:
  - Customer-facing wording uses `Altibase 8.1 verified source` rather than internal source labels.
  - `CREATE DATABASE LINK IF NOT EXISTS`, `DROP DATABASE LINK IF EXISTS`, DB Link JRE 1.8 basis, AKU 1-to-6 replica count, `altiEncrypt` availability for AKU configuration, multi-thread AKU improvements, and 128-byte replication target-name behavior are represented where relevant.

## Retrieval And GPT Answer Quality

- Strengths:
  - Both attachments have question-oriented sections, version blocks, compact syntax examples, decision maps, operational procedures, and troubleshooting checklists.
  - Literal names such as `REMOTE_TABLE`, `TARGETS/NLS_BYTE_PER_CHAR`, `Altibase.jdbc.driver.AltibaseDriver`, `com.altibase.sqoop.manager.AltibaseManager`, `AKU_SERVER_COUNT`, `REPLICATIONS`, `aku -p start`, `aku -p end`, and `SYSTEM_.SYS_REPLICATIONS_` are preserved.
  - Screenshot-heavy source material is represented as procedure text, YAML, SQL, command blocks, item blocks, or compact Mermaid flows; the target attachments contain no raw image references.
  - Forbidden source-path leakage checks found only the attachments' own "do not expose" policy statements, not actual leaked repository paths or internal 8.1 source labels.
- Risks:
  - Static review cannot verify live DB Link connectivity, remote JDBC driver compatibility, GoldenGate behavior, OpenLDAP runtime behavior, Kubernetes object behavior, persistent volume performance, or AKU recovery in a real cluster.
  - Third-party products can change independently of the Altibase source set; the attachments correctly avoid broad compatibility promises.

## Required Follow-Up

- None for R24.
