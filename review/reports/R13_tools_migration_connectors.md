# R13 Tools, Migration, Connectors Review

Date: 2026-05-15
Reviewer: Codex
Verdict: Pass

## Scope
- Attachments:
  - `GPTs/attachments/14_utilities_operation_tools.md`
  - `GPTs/attachments/15_migration_oracle_compatibility.md`
  - `GPTs/attachments/16_dblink_external_connectors.md`
  - `GPTs/attachments/17_kubernetes_aku_cloud.md`
  - `GPTs/attachments/19_spatial_nifi_tableau_misc.md`
- Supporting reports:
  - `GPTs/reports/source_inventory.md`
  - `GPTs/reports/image_inventory.md`
- Source manuals sampled:
  - `Manuals/Tools/Altibase_release/eng/Utilities Manual.md`
  - `Manuals/Tools/Altibase_release/eng/dataCompJ User's Manual.md`
  - `Manuals/Tools/Altibase_release/eng/Migration Center User's Manual.md`
  - `Manuals/Tools/Altibase_release/eng/altiShapeLoader User's Manual.md`
  - `Manuals/Altibase_7.1/eng/Adapter for Oracle User's Manual.md`
  - `Manuals/Altibase_7.1/eng/DB Link User's Manual.md`
  - `Manuals/Altibase_7.3/eng/DB Link User's Manual.md`
  - `Manuals/Altibase_trunk/eng/DB Link User's Manual.md`
  - `Manuals/Altibase_7.3/eng/Utilities Manual.md`
  - `Manuals/Altibase_trunk/eng/Utilities Manual.md`
  - `3rd Party Guide for Altibase/eng/Altibase Kubernetes Guide for Startups.md`
  - `3rd Party Guide for Altibase/eng/Altibase aku Sample Guide for Kubernetes.md`
  - `3rd Party Guide for Altibase/eng/Altibase Spring Data JDBC Guide.md`
  - `3rd Party Guide for Altibase/eng/Altibase with Apache NiFi User's Guide.md`
  - `3rd Party Guide for Altibase/eng/Altibase with Tableau User's Guide.md`
  - `ReleaseNotes/eng/Altibase_7_3_0_0_1_Release_Notes.md`
  - `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`
  - `ReleaseNotes/eng/Altibase_Migration_Center_7_19_Release_Notes.md`

## Commands Run
```bash
sed -n '1,240p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,220p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,260p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
wc -l GPTs/attachments/14_utilities_operation_tools.md GPTs/attachments/15_migration_oracle_compatibility.md GPTs/attachments/16_dblink_external_connectors.md GPTs/attachments/17_kubernetes_aku_cloud.md GPTs/attachments/19_spatial_nifi_tableau_misc.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' | sort
rg -n '^### (14|15|16|17|19)_' GPTs/reports/source_inventory.md
rg -n '(14_utilities|15_migration|16_dblink|17_kubernetes|19_spatial)' GPTs/reports/image_inventory.md
rg -n 'TODO|FIXME|image|screenshot|media/|\.png|\.gif|\.jpg|github.com|trunk|Altibase_trunk|/home/|file://|C:\\|Documents/raw|<img|!\[' GPTs/attachments/14_utilities_operation_tools.md GPTs/attachments/15_migration_oracle_compatibility.md GPTs/attachments/16_dblink_external_connectors.md GPTs/attachments/17_kubernetes_aku_cloud.md GPTs/attachments/19_spatial_nifi_tableau_misc.md
find '3rd Party Guide for Altibase/eng' 'Manuals/Tools/Altibase_release/eng' 'Manuals/Tools/Altibase_trunk/eng' -maxdepth 2 -type f | sort
rg -n 'GoldenGate|goldengate|Oracle GoldenGate' GPTs Manuals '3rd Party Guide for Altibase' ReleaseNotes 'Technical Documents' review
find Manuals -path '*Golden*' -o -path '*golden*'
rg -n 'CREATE DATABASE LINK|DROP DATABASE LINK|IF NOT EXISTS|IF EXISTS|REMOTE_TABLE_STORE|REMOTE_TABLE' Manuals/Altibase_7.1/eng/DB\ Link\ User\'s\ Manual.md Manuals/Altibase_7.3/eng/DB\ Link\ User\'s\ Manual.md Manuals/Altibase_trunk/eng/DB\ Link\ User\'s\ Manual.md
rg -n 'AKU_SERVER_COUNT|up to 4|up to 6|scalable replicas|multiple.*REPLICATIONS|encrypted password|altiEncrypt' ReleaseNotes/eng/Altibase_7_3_0_0_1_Release_Notes.md ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md Manuals/Altibase_7.3/eng/Utilities\ Manual.md Manuals/Altibase_trunk/eng/Utilities\ Manual.md '3rd Party Guide for Altibase/eng/Altibase aku Sample Guide for Kubernetes.md'
rg -n 'Oracle Database|10gR2|21c|Altibase 6.5.1|JSON|CLOB|global temporary|volatile|external table|hybrid partitioned|identity|empty string|ROWID|Build Table|private synonym|sequences|PSM' Manuals/Tools/Altibase_release/eng/Migration\ Center\ User\'s\ Manual.md Manuals/Tools/Altibase_trunk/eng/Migration\ Center\ User\'s\ Manual.md ReleaseNotes/eng/Altibase_Migration_Center_7_19_Release_Notes.md
rg -n 'force_clob_bind|CLOB|BLOB|Altibase42|DBCPConnectionPool|Database Driver Location|Altibase.jdbc.driver.AltibaseDriver|1.12.1|JDBC API' '3rd Party Guide for Altibase/eng/Altibase with Apache NiFi User'\''s Guide.md'
rg -n 'TIMESTAMP_TO_DATE|mysql_date_function|Other Databases|SQL92|Altibase42|Properties File|JDBC' '3rd Party Guide for Altibase/eng/Altibase with Tableau User'\''s Guide.md'
```

## Findings
No Blocker, High, or Medium issues were found. The reviewed attachments are task-oriented, convert UI-heavy source material into executable procedures, and avoid screenshot-dependent guidance.

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Low | `GPTs/attachments/16_dblink_external_connectors.md` | 9 | The document selection scope mentions GoldenGate as part of the external connector set, but the attachment has no GoldenGate section and local source searches did not find source material for it. This is a coverage risk only if GoldenGate was intended to be answerable. | Either confirm GoldenGate is out of scope for this attachment set, or add a small source-backed GoldenGate section once an approved source is available. Do not synthesize connector guidance without a source. |
| Low | `GPTs/attachments/19_spatial_nifi_tableau_misc.md` | 1436 | The NiFi setup uses `/home/altibase/NiFi/nifi-1.12.1/lib` as an example driver path. It is source-derived and labeled as a setup path, but validation flags it as a Unix home path that could be misread as environment-specific. | Consider rewriting the example as `$NIFI_HOME/lib` with the source path kept only as an example value, so GPT answers generalize the procedure while preserving the literal source example where needed. |

## Source Checks
- Claims checked:
  - `14_utilities_operation_tools.md` was checked against Utilities Manual and dataCompJ sources for `aexport`, `altiComp`, `dataCompJ`, `DB_MASTER`, `DB_SLAVE`, `MOSO`, `MOSX`, `MXSO`, policy behavior, generated scripts, and sync cautions.
  - `15_migration_oracle_compatibility.md` was checked against Migration Center, Adapter for Oracle, release notes, and data dictionary sources for Oracle version support, Altibase target support, object conversion limits, data type conversion, empty string behavior, `ROWID`, `DBMS_METADATA`, and `oraAdapter` version matching.
  - `16_dblink_external_connectors.md` was checked against DB Link manuals and third-party connector guide material for `CREATE DATABASE LINK`, `DROP DATABASE LINK`, 8.1-only `IF NOT EXISTS` and `IF EXISTS`, `REMOTE_TABLE`, `REMOTE_TABLE_STORE`, DBeaver caveats, Spring JDBC caveats, and Hadoop connector positioning.
  - `17_kubernetes_aku_cloud.md` was checked against Kubernetes/AKU guides, Utilities manuals, and release notes for `AKU_SERVER_COUNT`, 7.1 four-node and 7.3/8.1 six-node scaling, `REPLICATIONS`, `aku.conf`, `aku -p start`, `aku -p end`, `aku -p clean`, password encryption, StatefulSet behavior, startup probes, and ordered startup.
  - `19_spatial_nifi_tableau_misc.md` was checked against Spatial SQL Reference, altiShapeLoader, NiFi, and Tableau sources for geometry types, WKT/WKB/EWKT/EWKB, SRID behavior, spatial predicate outputs, R-tree/index guidance, `altiShapeLoader` import/export flow, NiFi JDBC settings, `force_clob_bind`, CLOB/BLOB limitations, Tableau `Altibase42`, `TIMESTAMP_TO_DATE`, and `mysql_date_function`.
- Source coverage:
  - Coverage is good for the reviewed tool and connector topics. The attachments preserve literal commands, property names, SQL keywords, object names, connector names, and version labels.
  - UI and screenshot-heavy source guides were generally converted into menu paths, fields, settings, validation checks, and troubleshooting procedures.
  - Version-sensitive behavior is explicitly called out where sampled sources differ, especially for DB Link 8.1 syntax and AKU scaling.
- Source gaps:
  - GoldenGate appears in the document selection intent but not in the sampled source inventory or local source tree.
  - `GPTs/reports/source_inventory.md` underlists the 7.1 Utilities Manual for the AKU/Kubernetes attachment, although the attachment itself cites and uses the 7.1 AKU material and the source manual was sampled.
  - Altibase Heartbeat source manuals exist under tools manuals, but Heartbeat is not part of the selected R13 attachment scope and was not reviewed as covered content.

## Oracle-Overlap Decision
- Correctly compressed:
  - Ordinary DML and generic migration concepts are brief. The migration attachment emphasizes Altibase-specific object conversion, unsupported Oracle constructs, tool order, risk checks, and replication adapter behavior.
  - DB Link and connector sections avoid generic JDBC explanations unless needed to state Altibase-specific driver, dialect, type, or tool caveats.
- Too much generic Oracle material:
  - None found at a blocking or high level. Oracle material is mostly framed as migration risk, object compatibility, or Adapter for Oracle input behavior.
- Missing Altibase-specific difference:
  - No required Altibase-specific differences were missing in sampled areas. The GoldenGate source gap remains conditional on whether that connector is truly in scope.

## Version Checks
- 7.1:
  - Covered for utility behavior, Adapter for Oracle, DB Link syntax without `IF NOT EXISTS` or `IF EXISTS`, and AKU four-node scaling.
- 7.3:
  - Covered for Migration Center 7.19 positioning, DB Link baseline syntax, AKU six-node scaling, `altiEncrypt`, and Kubernetes/AKU operational changes.
- 8.1:
  - Covered for DB Link `IF NOT EXISTS` and `IF EXISTS`, AKU six-node scaling, multiple `REPLICATIONS`, JSON migration differences, and current trunk/manual behavior where 8.1 source material is represented by trunk manuals.

## Retrieval And GPT Answer Quality
- Strengths:
  - The attachments are strongly organized around answerable tasks: command recipes, setup checklists, verification queries, generated-file explanations, risk tables, and troubleshooting paths.
  - Literal names and syntax are preserved, including SQL object names, commands, properties, connector names, data dictionary views, and version labels.
  - Screenshot-dependent guides were converted into procedure steps with field names, expected values, and validation points.
  - The migration and connector sections are explicit about caveats rather than over-promising compatibility.
- Risks:
  - GoldenGate may be a retrieval miss if users ask for it because it appears in the selection intent but is not covered in the reviewed attachment.
  - Example paths such as the NiFi `/home/altibase/...` driver path may need answer-time framing as examples, not universal install paths.
  - Some third-party connector details are necessarily version-bound to the sampled guide versions, so future connector UI changes may require refresh.

## Required Follow-Up
- No attachment changes are required for pass.
- Decide whether GoldenGate is intentionally out of scope for the GPT attachment set. If it is in scope, add only source-backed guidance after an approved source is added.
- Optionally generalize the NiFi driver path example to `$NIFI_HOME/lib` while preserving the literal source path as an example.
