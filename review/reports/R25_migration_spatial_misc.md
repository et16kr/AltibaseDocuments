# R25 Migration Tools, Spatial, NiFi, Tableau, and Miscellaneous Integrations

Date: 2026-05-16
Reviewer: Codex
Verdict: Pass

## Scope

- Attachments:
  - `GPTs/attachments/15_migration_oracle_compatibility.md`
  - `GPTs/attachments/19_spatial_nifi_tableau_misc.md`
- Supporting reports:
  - `GPTs/reports/source_inventory.md`
  - `GPTs/reports/image_inventory.md`
- Source manuals sampled:
  - `Manuals/Tools/Altibase_release/kor/Migration Center User's Manual.md`
  - `Manuals/Tools/Altibase_trunk/kor/Migration Center User's Manual.md`
  - `ReleaseNotes/kor/Altibase_Migration_Center_7_19_Release_Notes.md`
  - `Manuals/Altibase_7.1/kor/Spatial SQL Reference.md`
  - `Manuals/Altibase_7.3/kor/Spatial SQL Reference.md`
  - `Manuals/Altibase_trunk/kor/Spatial SQL Reference.md`
  - `Manuals/Tools/Altibase_release/kor/altiShapeLoader User's Manual.md`
  - `Manuals/Tools/Altibase_trunk/kor/altiShapeLoader User's Manual.md`
  - `ReleaseNotes/kor/Altibase_altiShapeLoader_1_0_Release_Notes.md`
  - `3rd Party Guide for Altibase/kor/NiFi User's Guide for Altibase.md`
  - `3rd Party Guide for Altibase/kor/Tableau User's Guide for Altibase/Tableau User's Guide for Altibase.md`
  - `Manuals/Altibase_7.1/kor/Adapter for Oracle User's Manual.md`
  - `Manuals/Altibase_7.3/kor/Adapter for Oracle User's Manual.md`
  - `Manuals/Altibase_trunk/kor/Adapter for Oracle User's Manual.md`

## Commands Run

```bash
bash review/scripts/run_review_remediation_cycle.sh status
rg -n $'\t(Reviewing|Remediating|ReReviewing|Fail)$' review/review_remediation_cycle_status.tsv
git status --short
git diff -- review/review_remediation_cycle_status.tsv
git diff -- review/review_stage_status.tsv
sed -n '1,260p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,260p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,260p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,240p' GPTs/attachments/README.md
rg -n '^R25\b|G4_DevTools|Migration tools|Spatial|NiFi|Tableau' review/review_stages.tsv review/Altibase_GPT_Detailed_Review_Design.md GPTs/Altibase_GPT_Attachment_Build_Workplan.md GPTs/Altibase_GPT_Document_Selection.md GPTs/attachments/README.md
nl -ba GPTs/attachments/15_migration_oracle_compatibility.md
nl -ba GPTs/attachments/19_spatial_nifi_tableau_misc.md
rg -n "Migration Center|altiShapeLoader|Spatial SQL|NiFi|Tableau|shape|WKT|WKB|GEOMETRY" GPTs/reports/source_inventory.md GPTs/reports/image_inventory.md
find Manuals/Tools/Altibase_release/kor Manuals/Tools/Altibase_trunk/kor Manuals/Altibase_7.1/kor Manuals/Altibase_7.3/kor Manuals/Altibase_trunk/kor '3rd Party Guide for Altibase/kor' ReleaseNotes/kor -maxdepth 3 \( -name "Migration Center User's Manual.md" -o -name "Spatial SQL Reference.md" -o -name "altiShapeLoader User's Manual.md" -o -name "NiFi User's Guide for Altibase.md" -o -name "Tableau User's Guide for Altibase.md" -o -name "Altibase_Migration_Center_7_19_Release_Notes.md" -o -name "Altibase_altiShapeLoader_1_0_Release_Notes.md" \) -print
rg -n "trunk|file://|C:|!\[|\.png|\.jpg|screenshot|Screenshot|image|figure|Figure|Altibase 8.1 verified source" GPTs/attachments/15_migration_oracle_compatibility.md GPTs/attachments/19_spatial_nifi_tableau_misc.md
rg -n "register|build|reconcile|run|diff|filesync|Approximate|Exact|Data Validation|primary key|LOB|Object Options|Replace Default Empty String|Batch LOB|Convert Oversized|Invisible Column|Oracle Database|21c|Java 8|GUI|CLI|Graphic" "Manuals/Tools/Altibase_release/kor/Migration Center User's Manual.md" "Manuals/Tools/Altibase_trunk/kor/Migration Center User's Manual.md" "ReleaseNotes/kor/Altibase_Migration_Center_7_19_Release_Notes.md"
rg -n "GEOMETRY|SRID|RTREE|R-Tree|SPATIAL_REF_SYS|ADD_SPATIAL_REF_SYS|DELETE_SPATIAL_REF_SYS|GEOMETRY_COLUMNS|SYS_GEOMETRY_COLUMNS|USER_SRS|NULL|EMPTY|Trigger|stored|procedure|ST_TRANSFORM|GEOMETRYCOLLECTION" "Manuals/Altibase_7.1/kor/Spatial SQL Reference.md" "Manuals/Altibase_7.3/kor/Spatial SQL Reference.md" "Manuals/Altibase_trunk/kor/Spatial SQL Reference.md"
rg -n "altiShapeLoader|CREATE_TABLE|GEO_COL_SIZE|103809024|DBF_CHAR|ATOMIC_BATCH|CREATE_BAD|SPATIAL_REF_SYS|ADD_SPATIAL_REF_SYS|epsg.properties|\.prj|2GB|255|NCHAR|NVARCHAR|BOOLEAN|FID|SEQ_|Altibase 7.1|Java" "Manuals/Tools/Altibase_release/kor/altiShapeLoader User's Manual.md" "Manuals/Tools/Altibase_trunk/kor/altiShapeLoader User's Manual.md" "ReleaseNotes/kor/Altibase_altiShapeLoader_1_0_Release_Notes.md"
rg -n "Altibase42|Altibase\.jar|AltibaseDriver|force_clob_bind|CLOB|BLOB|DBCPConnectionPool|GenerateTableFetch|Database Connection URL|Database Driver Location|1\.12\.1|7\.1\.0\.5\.6|7\.1\.0\.6\.7|Tableau|Properties File|SQL92|TIMESTAMP_TO_DATE|mysql_date_function|Other Databases|JDK|2021\.4\.4" "3rd Party Guide for Altibase/kor/NiFi User's Guide for Altibase.md" "3rd Party Guide for Altibase/kor/Tableau User's Guide for Altibase/Tableau User's Guide for Altibase.md"
rg -n "Adapter for Oracle|oraAdapter|NLS_LANG|ALA_SENDER|ORACLE_ASYNCHRONOUS|CREATE REPLICATION.*FOR ANALYSIS|ADAPTER_LOB|XLog|OCI|6\.5\.1|5\.5\.1" Manuals ReleaseNotes GPTs/reports/source_inventory.md
rg -n "ILOADER_GEOM|-geom|EWKB|WKB|spatial data|공간 데이터" GPTs/attachments Manuals/Altibase_7.1/kor/Spatial\ SQL\ Reference.md Manuals/Altibase_7.3/kor/Spatial\ SQL\ Reference.md Manuals/Altibase_trunk/kor/Spatial\ SQL\ Reference.md
```

## Findings

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Note | `GPTs/attachments/15_migration_oracle_compatibility.md`; `GPTs/attachments/19_spatial_nifi_tableau_misc.md` | 1 | No actionable Blocker, High, Medium, or Low findings were found in the R25 scope. | No remediation required for this stage. |

## Source Checks

- Claims checked:
  - Migration Center scope, Java/Swing/CLI requirements, source/target version scope, five-stage workflow, CLI `register/build/reconcile/run/diff/filesync`, CLI Reconcile default-value limitation, Data Validation primary-key and LOB restrictions, empty-string object/data options, Oracle JSON mapping, LOB `NOT NULL` removal, and troubleshooting examples.
  - Adapter for Oracle `oraAdapter`/`oaUtility` architecture, ALA startup pattern, DDL handling, LOB support property, offline option, and DDL-gap cautions.
  - Spatial `GEOMETRY` subtypes, WKT/WKB/EWKT/EWKB, column precision/SRID syntax, R-Tree index behavior, `SPATIAL_REF_SYS`/`GEOMETRY_COLUMNS`, SRID change rules, `NULL`/`EMPTY` index-count caveat, function/operator syntax, and Spatial API sample path.
  - altiShapeLoader system requirements, package setup, option precedence, required and optional switches, default values such as `CREATE_TABLE=T`, `DBF_CHAR=EUC-KR`, `PARALLEL=4`, `COMMIT=1000`, `GEO_COL_SIZE=103809024`, SRID/.prj/`epsg.properties` behavior, import/export expected files, and shapefile/data-type constraints.
  - NiFi and Tableau JDBC requirements, driver file names, `force_clob_bind=true`, CLOB/BLOB caveats, `TIMESTAMP_TO_DATE = 1`, `mysql_date_function.sql`, UI menu paths, fields, and expected validation outcomes.
- Source coverage:
  - The sampled high-risk claims are backed by Korean manuals or Korean third-party guides where those exist.
  - English-image inventory items for Migration Center, Spatial SQL, NiFi, and Tableau are represented in the attachments as procedural text, BNF-like syntax, tables, or compact item blocks.
- Korean/English source conflicts:
  - None found in sampled claims.
- Source gaps:
  - I did not exhaustively verify every individual Spatial function example or every Adapter for Oracle property value. The sampled sections covered syntax families and high-risk operational constraints.

## Oracle-Overlap Decision

- Correctly compressed:
  - Attachment 15 keeps ordinary Oracle-compatible SQL brief and centers on Migration Center stages, conversion differences, options, generated reports, PSM review, data validation, and `oraAdapter` behavior.
  - Attachment 19 keeps generic JDBC/BI/ETL material limited to the fields and checks needed to connect Altibase through NiFi/Tableau.
- Too much generic Oracle material:
  - None found in the scoped files.
- Missing Altibase-specific difference:
  - No actionable gap for this stage. A residual area for later retrieval review is that Altibase-to-Altibase spatial WKB/EWKB migration caveats are covered more directly in the iLoader/aexport attachments than in attachment 19.

## Version Checks

- 7.1:
  - Spatial SQL syntax, `Altibase42.jar` third-party integration guidance, altiShapeLoader support floor, and Adapter for Oracle constraints are represented and source-backed.
- 7.3:
  - Migration Center 7.19 release-note scope, Spatial SQL, altiShapeLoader, NiFi, Tableau, and Adapter for Oracle guidance are represented without treating tool release `7.19` as an Altibase server version.
- 8.1:
  - Customer-facing text uses `Altibase 8.1 verified source` rather than internal source labels. JSON migration behavior and Spatial SQL/tool baselines are source-backed against trunk/Korean sources plus release notes where applicable.

## Retrieval And GPT Answer Quality

- Strengths:
  - Both attachments have question-oriented headings, decision maps, task cookbooks, option blocks, troubleshooting blocks, and literal command/property/function tokens.
  - UI screenshots from Migration Center, NiFi, and Tableau are replaced with procedural text and field/value lists, so answers do not depend on unavailable screenshots.
  - High-risk conversion behavior such as empty strings, JSON, LOB `NOT NULL`, data validation limits, SRID handling, R-Tree `NULL`/`EMPTY`, and third-party driver caveats is prominent and searchable.
- Risks:
  - Attachment 19 is intentionally broad. For obscure GIS semantics, individual Spatial API functions, or patch-specific third-party UI changes, the GPT should still ask for target versions and verify against the relevant manuals.
  - Some spatial product-to-product migration detail is distributed across attachment 13/14 rather than fully repeated in attachment 19, so final retrieval testing should include cross-file questions about `GEOMETRY`, `WKB`, `EWKB`, `-geom WKB`, and `ILOADER_GEOM`.

## Required Follow-Up

- None for R25.
