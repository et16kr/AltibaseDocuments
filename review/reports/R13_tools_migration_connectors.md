# R13 Utilities, Migration, Connectors, Kubernetes, Spatial Review
Date: 2026-05-14
Reviewer: Codex
Verdict: Review Required

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
  - `Manuals/Altibase_7.1/eng/Utilities Manual.md`
  - `Manuals/Altibase_7.3/eng/Utilities Manual.md`
  - `Manuals/Altibase_trunk/eng/Utilities Manual.md`
  - `Manuals/Tools/Altibase_release/eng/dataCompJ User's Manual.md`
  - `Manuals/Tools/Altibase_trunk/eng/dataCompJ User's Manual.md`
  - `Manuals/Tools/Altibase_release/eng/Migration Center User's Manual.md`
  - `Manuals/Tools/Altibase_trunk/eng/Migration Center User's Manual.md`
  - `Manuals/Altibase_7.1/eng/Adapter for Oracle User's Manual.md`
  - `Manuals/Altibase_trunk/eng/Adapter for Oracle User's Manual.md`
  - `Manuals/Altibase_7.1/eng/DB Link User's Manual.md`
  - `Manuals/Altibase_trunk/eng/DB Link User's Manual.md`
  - `Manuals/Altibase_7.1/eng/Hadoop Connector User's Manual.md`
  - `Manuals/Altibase_trunk/eng/Hadoop Connector User's Manual.md`
  - `Manuals/Tools/Altibase_release/eng/Altibase 3rd Party Connector Guide.md`
  - `Manuals/Tools/Altibase_trunk/eng/Altibase 3rd Party Connector Guide.md`
  - `3rd Party Guide for Altibase/eng/Altibase aku Sample Guide for Kubernetes.md`
  - `3rd Party Guide for Altibase/eng/NiFi User's Guide for Altibase.md`
  - `3rd Party Guide for Altibase/eng/Tableau User's Guide for Altibase/Tableau User's Guide for Altibase.md`
  - `Manuals/Altibase_trunk/eng/Spatial SQL Reference.md`
  - `Manuals/Tools/Altibase_trunk/eng/altiShapeLoader User's Manual.md`

## Commands Run
```bash
sed -n '1,220p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,220p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,240p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
wc -l GPTs/attachments/14_utilities_operation_tools.md GPTs/attachments/15_migration_oracle_compatibility.md GPTs/attachments/16_dblink_external_connectors.md GPTs/attachments/17_kubernetes_aku_cloud.md GPTs/attachments/19_spatial_nifi_tableau_misc.md
sed -n '251,346p' GPTs/reports/source_inventory.md
rg -n '^##|^###|^Tool block|^Connector Block|^Step block|^Option block|^Pattern block|^Command block|^Function block|^Procedure block|^Metadata block|^DDL block|^Format block|^Property block|^Troubleshooting block' GPTs/attachments/14_utilities_operation_tools.md GPTs/attachments/15_migration_oracle_compatibility.md GPTs/attachments/16_dblink_external_connectors.md GPTs/attachments/17_kubernetes_aku_cloud.md GPTs/attachments/19_spatial_nifi_tableau_misc.md
nl -ba GPTs/attachments/14_utilities_operation_tools.md | sed -n '1,1305p'
nl -ba GPTs/attachments/15_migration_oracle_compatibility.md | sed -n '1,1265p'
nl -ba GPTs/attachments/16_dblink_external_connectors.md | sed -n '1,1505p'
nl -ba GPTs/attachments/17_kubernetes_aku_cloud.md | sed -n '1,660p'
nl -ba GPTs/attachments/19_spatial_nifi_tableau_misc.md | sed -n '1,1605p'
rg -n 'publishNotReady|publishNotReadyAddresses|publishNotReadyAddress' '3rd Party Guide for Altibase/eng/Altibase aku Sample Guide for Kubernetes.md' GPTs/attachments/14_utilities_operation_tools.md GPTs/attachments/17_kubernetes_aku_cloud.md
rg -n 'DROP USER ldap|CREATE USER ldap|CREATE USER|DROP USER' 'Manuals/Tools/Altibase_release/eng/Altibase 3rd Party Connector Guide.md' 'Manuals/Tools/Altibase_trunk/eng/Altibase 3rd Party Connector Guide.md' '3rd Party Guide for Altibase/eng' GPTs/attachments/16_dblink_external_connectors.md
rg -n -C 4 'boundary-query|--query|Free-form|Query|sqoop import' "Manuals/Altibase_7.1/eng/Hadoop Connector User's Manual.md" "Manuals/Altibase_7.3/eng/Hadoop Connector User's Manual.md" "Manuals/Altibase_trunk/eng/Hadoop Connector User's Manual.md"
rg -n -C 4 'CLOB|BLOB|force_clob_bind|DBCPConnectionPool|1\.12\.1|Altibase42|Database Driver Location|Database Connection URL' "3rd Party Guide for Altibase/eng/NiFi User's Guide for Altibase.md"
rg -n -C 4 'TIMESTAMP_TO_DATE|mysql_date_function|Properties File|Other Databases|SQL92|Altibase42|2021\.4\.4' "3rd Party Guide for Altibase/eng/Tableau User's Guide for Altibase/Tableau User's Guide for Altibase.md"
rg -n '!\[|<img|media/|\.png|\.jpg|\.jpeg|\.gif|file://|/Users|trunk|master/Manuals|Documents/raw' GPTs/attachments/14_utilities_operation_tools.md GPTs/attachments/15_migration_oracle_compatibility.md GPTs/attachments/16_dblink_external_connectors.md GPTs/attachments/17_kubernetes_aku_cloud.md GPTs/attachments/19_spatial_nifi_tableau_misc.md
rg -n 'TODO|TBD|FIXME|Conversion TODO|screenshot|image|see figure|below image|shown below|refer to the image|click.*image' GPTs/attachments/14_utilities_operation_tools.md GPTs/attachments/15_migration_oracle_compatibility.md GPTs/attachments/16_dblink_external_connectors.md GPTs/attachments/17_kubernetes_aku_cloud.md GPTs/attachments/19_spatial_nifi_tableau_misc.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name README.md | wc -l
```

## Findings
| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| High | `GPTs/attachments/14_utilities_operation_tools.md` | 574 | The AKU/Kubernetes utility guidance names the Service field as `publishNotReadyAddress`. The sampled AKU source guide and the Kubernetes attachment use the Kubernetes field `publishNotReadyAddresses` with the trailing `es`. A GPT answer that repeats the singular field can produce invalid or ineffective Service YAML for AKU startup and peer DNS discovery. | Change the field to `publishNotReadyAddresses: true` and keep that exact spelling consistent across the utility and Kubernetes guidance. |
| High | `GPTs/attachments/16_dblink_external_connectors.md` | 1416 | The OpenLDAP setup example includes `DROP USER ldap CASCADE;` before creating the `ldap` user. This destructive reset was not found in the sampled third-party connector source guide, and it appears in task guidance without an immediate test-only warning, backup requirement, or confirmation gate. | Remove the destructive statement from the upload attachment, or isolate it as an explicit test-lab reset only. Prefer a non-destructive create/verify/grant sequence, and cross-reference user/privilege guidance for production-safe setup. |

## Source Checks
- Claims checked:
  - Utility behavior for `aexport`, `altiComp`, `dataCompJ`, `aku`, `altiAudit`, `altibase`, `altiMon`, `altierr`, `altipasswd`, `altiProfile`, `altiwrap`, `awrite`, `checkServer`, `killCheckServer`, `server`, and dump utilities.
  - Migration Center flow, CLI options, Adapter for Oracle properties, DDL ordering, offline mode, object support, type differences, empty-string behavior, JSON handling, LOB handling, and PSM review cautions.
  - DB Link object setup, link types, transaction levels, supported data types, Hadoop Connector Sqoop examples, DBeaver setup, Hibernate dialect behavior, and OpenLDAP connector setup.
  - Kubernetes and AKU workflows for headless Service, StatefulSet, PVCs, `AKU_SERVER_COUNT`, `REPLICATIONS`, `AKU_FLUSH_AT_START`, `AKU_REPLICATION_RESET_AT_END`, startup scripts, and online log cautions.
  - Spatial DDL, geometry metadata, SRID, R-Tree, Spatial SQL functions, `altiShapeLoader`, NiFi CLOB/BLOB limits, NiFi DBCP setup, Tableau JDBC setup, `TIMESTAMP_TO_DATE`, and `mysql_date_function.sql`.
- Source coverage:
  - The stage attachments are generally task-oriented and avoid screenshot-dependent instructions.
  - The `source_inventory.md` entries matched the expected source families for utilities, migration, DB Link, Hadoop, Kubernetes/AKU, Spatial, NiFi, Tableau, and third-party connectors.
  - `image_inventory.md` shows heavy screenshot and syntax-image source load for this stage, but attachment-level scans found no remaining image embeds or direct image dependencies in the reviewed files.
- Source gaps:
  - No live Altibase, Kubernetes, Hadoop/Sqoop, NiFi, Tableau, DBeaver, or OpenLDAP execution was performed.
  - The OpenLDAP `DROP USER ldap CASCADE;` sample was not located in the sampled connector source manuals.
  - This review sampled the relevant source manuals and scanned the attachments, but did not individually reconcile every source image reference from the image inventory.

## Oracle-Overlap Decision
- Correctly compressed:
  - `GPTs/attachments/15_migration_oracle_compatibility.md` keeps generic Oracle-overlapping SQL brief and focuses on Altibase migration differences, tool flow, Adapter for Oracle behavior, object compatibility, type handling, and operational risk.
  - The reviewed tool and connector attachments emphasize Altibase-specific commands, properties, connector names, version caveats, and execution checks rather than generic DML.
- Too much generic Oracle material:
  - No major over-expansion found.
- Missing Altibase-specific difference:
  - The OpenLDAP setup block needs production-safe Altibase user/privilege framing instead of an unguarded destructive reset.
  - The AKU utility block needs the exact Kubernetes field spelling used by AKU source examples.

## Version Checks
- 7.1:
  - Utility, DB Link, Hadoop Connector, Spatial, and connector claims were sampled against 7.1 manuals where available.
  - `AKU_SERVER_COUNT` differs from later versions: sampled 7.1 utilities source supports 1 to 4 servers.
- 7.3:
  - Utility and AKU checks align with the later 1 to 6 server count.
  - Migration Center and dataCompJ release/source notes were included in the source set for 7.3-era tool behavior.
- 8.1:
  - Trunk-source manuals were sampled as the source family for 8.1 claims.
  - The reviewed attachments did not expose internal `trunk` labels in the stage files.
  - DB Link DDL, AKU properties, Migration Center JSON support, and connector procedures were spot-checked against current source families.

## Retrieval And GPT Answer Quality
- Strengths:
  - The files are broken into task-oriented blocks with explicit commands, setup steps, verification checks, restrictions, and troubleshooting cues.
  - Screenshots and UI flows were generally converted into procedural text, especially in DB Link connectors, Migration Center, NiFi, Tableau, and AKU sections.
  - Literal names for commands, properties, connectors, package names, SQL object types, and version labels are preserved well overall.
- Risks:
  - The singular `publishNotReadyAddress` typo can propagate into Kubernetes YAML advice and break AKU workflow guidance.
  - The OpenLDAP destructive reset example can lead to data loss if repeated outside a disposable test schema.
  - Some connector examples include source-derived absolute sample paths, such as NiFi installation paths, which are acceptable as examples but should remain clearly framed as replaceable environment paths.

## Required Follow-Up
- Correct `publishNotReadyAddress` to `publishNotReadyAddresses` in `GPTs/attachments/14_utilities_operation_tools.md`.
- Remove or strictly guard `DROP USER ldap CASCADE;` in `GPTs/attachments/16_dblink_external_connectors.md`.
- After fixes, run targeted validation:
```bash
rg -n 'publishNotReadyAddress\b|publishNotReadyAddresses' GPTs/attachments/14_utilities_operation_tools.md GPTs/attachments/17_kubernetes_aku_cloud.md
rg -n 'DROP USER ldap|CREATE USER ldap' GPTs/attachments/16_dblink_external_connectors.md
rg -n '!\[|<img|media/|\.png|\.jpg|\.jpeg|\.gif|file://|trunk|master/Manuals|Documents/raw' GPTs/attachments/14_utilities_operation_tools.md GPTs/attachments/15_migration_oracle_compatibility.md GPTs/attachments/16_dblink_external_connectors.md GPTs/attachments/17_kubernetes_aku_cloud.md GPTs/attachments/19_spatial_nifi_tableau_misc.md
```
