# R02 High-risk Source Traceability Audit

Date: 2026-05-16
Reviewer: Codex
Verdict: Pass

## Scope

- Attachments: `GPTs/attachments/00_version_release_platform.md`; `GPTs/attachments/03_sql_ddl_generation.md`; `GPTs/attachments/05_data_types_properties.md`; `GPTs/attachments/06_data_dictionary_performance_views.md`; `GPTs/attachments/09_replication_ha_cdc.md`; `GPTs/attachments/18_security_ssl_tls.md`.
- Supporting reports: `GPTs/reports/source_inventory.md`; `GPTs/reports/8_1_verification.md`; `GPTs/reports/eng_kor_parity.md`; prior R02 findings in this report's previous version.
- Source manuals sampled: `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`; `ReleaseNotes/kor/Altibase_7_1_0_1_2_Release_Notes.md`; `ReleaseNotes/kor/Altibase_7_3_0_0_1_Release_Notes.md`; `Technical Documents/kor/Supported Platforms.md`; `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`; `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`; `Manuals/Altibase_trunk/kor/SQL Reference.md`; `Manuals/Altibase_trunk/kor/Replication Manual.md`.

## Commands Run

```bash
bash review/scripts/run_review_remediation_cycle.sh status
rg -n $'\t(Reviewing|Remediating|ReReviewing|Fail)$' review/review_remediation_cycle_status.tsv
git status --short
git diff --stat
git diff -- GPTs/attachments/03_sql_ddl_generation.md
git diff -- GPTs/attachments/09_replication_ha_cdc.md
sed -n '1,240p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,240p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,260p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
sed -n '1,260p' GPTs/reports/source_inventory.md
sed -n '1,220p' GPTs/reports/8_1_verification.md
sed -n '1,240p' GPTs/reports/eng_kor_parity.md
wc -l GPTs/attachments/00_version_release_platform.md GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/05_data_types_properties.md GPTs/attachments/06_data_dictionary_performance_views.md GPTs/attachments/09_replication_ha_cdc.md GPTs/attachments/18_security_ssl_tls.md
rg -n "JSON|Temporary LOB|TEMPORARY_LOB|MEMORY_TEMPLOB|V\$TEMPORARY_LOBS|REPLICATION_SSL_PORT_NO|USING SSL|TRCLOG_EXPLAIN_TYPE|TRCLOG_JSON_PLAN_INDENT_DEPTH|V\$LOCK_TABLE_STATS|V\$MEM_STABLE|platform|supported|Linux|AIX|Windows|8\.1|7\.3|7\.1" GPTs/attachments/00_version_release_platform.md GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/05_data_types_properties.md GPTs/attachments/06_data_dictionary_performance_views.md GPTs/attachments/09_replication_ha_cdc.md GPTs/attachments/18_security_ssl_tls.md
rg -n "customer confirms|provides version-specific confirmation|confirms support|customer verifies support|unless the customer" GPTs/attachments/00_version_release_platform.md GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/05_data_types_properties.md GPTs/attachments/06_data_dictionary_performance_views.md GPTs/attachments/09_replication_ha_cdc.md GPTs/attachments/18_security_ssl_tls.md
rg -n "FOR PROPAGABLE LOGGING|FOR PROPAGATION|FOR ANALYSIS PROPAGATION|FOR ANALYSIS|USING SSL|USING IB" GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/09_replication_ha_cdc.md GPTs/attachments/18_security_ssl_tls.md
rg -n "trunk|Altibase_trunk|Manuals/Altibase|ReleaseNotes/|Technical Documents/|file://|C:/" GPTs/attachments/00_version_release_platform.md GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/05_data_types_properties.md GPTs/attachments/06_data_dictionary_performance_views.md GPTs/attachments/09_replication_ha_cdc.md GPTs/attachments/18_security_ssl_tls.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name README.md | sort | wc -l
rg -n "V\$TEMPORARY_LOBS|V\$LOCK_TABLE_STATS|V\$MEM_STABLE|TEMPORARY_LOB|LOCK_TABLE_STATS|MEM_STABLE" "Manuals/Altibase_7.1/kor/General Reference-2.The Data Dictionary.md" "Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md" "Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md" ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md
rg -n "Altibase 8\.1|8\.1\.0\.0\.1|AIX 7\.2|Red Hat Enterprise Linux 9|Microsoft Windows 2008|Microsoft Windows 10|HP-UX|LinuxONE|Ubuntu|Debian|Altibase 7\.3|7\.3\.0\.0\.9|Altibase 7\.1|7\.1\.0\.10\.0|Oracle Linux 9|Rocky Linux 9" "Technical Documents/kor/Supported Platforms.md" ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md ReleaseNotes/kor/Altibase_7_3_0_0_1_Release_Notes.md ReleaseNotes/kor/Altibase_7_1_0_1_2_Release_Notes.md
nl -ba ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md | sed -n '1,60p'
nl -ba ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md | sed -n '55,145p'
nl -ba ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md | sed -n '220,335p'
nl -ba ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md | sed -n '340,366p'
nl -ba "Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md" | sed -n '2588,2785p'
nl -ba "Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md" | sed -n '12360,12388p'
nl -ba "Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md" | sed -n '15998,16045p'
nl -ba "Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md" | sed -n '16542,16564p'
nl -ba "Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md" | sed -n '6936,6978p'
nl -ba "Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md" | sed -n '7508,7545p'
nl -ba "Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md" | sed -n '11655,11682p'
nl -ba "Manuals/Altibase_trunk/kor/SQL Reference.md" | sed -n '16165,16210p'
nl -ba "Manuals/Altibase_trunk/kor/SQL Reference.md" | sed -n '23596,23625p'
nl -ba "Manuals/Altibase_trunk/kor/SQL Reference.md" | sed -n '26490,26508p'
nl -ba "Manuals/Altibase_trunk/kor/Replication Manual.md" | sed -n '1058,1120p'
nl -ba "Manuals/Altibase_trunk/kor/Replication Manual.md" | sed -n '1180,1205p'
git diff --check
```

## Findings

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Note | `GPTs/attachments/03_sql_ddl_generation.md`; `GPTs/attachments/09_replication_ha_cdc.md`; `GPTs/attachments/18_security_ssl_tls.md` | 352 | No actionable `Blocker`, `High`, `Medium`, or `Low` findings remain in the sampled high-risk traceability paths. The prior R02 High issues are resolved: 7.1/7.3 exceptions for native `JSON`, Temporary LOB checks, `IF EXISTS`/`IF NOT EXISTS`, and `USING SSL` replication now require exact later Altibase source support, and `FOR ANALYSIS`/`FOR ANALYSIS PROPAGATION` are separated from `FOR PROPAGABLE LOGGING`/`FOR PROPAGATION`. | No remediation required for R02. Preserve the exact-source wording in `03_sql_ddl_generation.md:352`, `:864`, `:1331`, `:1961`-`:1963`, and the separated replication syntax in `03_sql_ddl_generation.md:593`-`:655`, `09_replication_ha_cdc.md:313`-`:347`, and `18_security_ssl_tls.md:436`-`:479`. |

## Source Checks

- Claims checked: 8.1 native `JSON` feature existence, `JSON [ IN ROW size ]`, JSON function names, `IS JSON`, JSON restrictions, Temporary LOB lifecycle, Temporary LOB creation cases, `ALTER SESSION SET FREE TEMPORARY LOB`, `V$TEMPORARY_LOBS`, Temporary LOB properties, replication SSL syntax, `REPLICATION_SSL_PORT_NO`, Log Analyzer SSL/IB exclusion scope, propagation role syntax, JSON-plan property names, 8.1 performance views, component-version boundaries, and platform support blocks.
- Source coverage: `00_version_release_platform.md:97`-`:103` and `05_data_types_properties.md:507`-`:597` are backed by Korean 8.1 release notes and Korean 8.1 General Reference/SQL Reference. `06_data_dictionary_performance_views.md:37`-`:39`, `:689`-`:702`, `:1204`-`:1218`, and `:2067`-`:2079` are backed by Korean 8.1 release notes plus Korean General Reference 2, with `V$LOCK_TABLE_STATS` also present in sampled 7.1/7.3 Korean manuals. `09_replication_ha_cdc.md:313`-`:347`, `:406`-`:474`, and `18_security_ssl_tls.md:405`-`:479` are backed by Korean 8.1 release notes and Korean Replication/General Reference detail.
- Korean/English source conflicts: no new Korean/English contradiction was found. The known English-source gaps for 8.1 JSON, Temporary LOB, replication SSL, and JSON-plan detail remain documented in `GPTs/reports/8_1_verification.md` and `GPTs/reports/eng_kor_parity.md`; the attachments use Korean-source-backed English prose where details are needed.
- Source gaps: JSON-formatted execution plan remains release-note-only. The scoped wording is appropriately narrow in `00_version_release_platform.md:127` and `05_data_types_properties.md:1503`-`:1533`; it does not invent JSON plan schema, values, or examples.

## Oracle-Overlap Decision

- Correctly compressed: ordinary Oracle-overlapping DML and generic SQL are not expanded in this stage's sampled high-risk paths. `03_sql_ddl_generation.md:1948`-`:1957` focuses Oracle conversion warnings on Altibase-specific DDL, JSON, LOB, partitioning, storage, queue, user, sequence, and replication differences.
- Too much generic Oracle material: none found in the sampled high-risk traceability paths.
- Missing Altibase-specific difference: none found for R02 after remediation. The JSON 7.1/7.3 fallback at `03_sql_ddl_generation.md:1949` correctly directs older-version answers to `VARCHAR` or `CLOB` plus application validation or upgrade planning.

## Version Checks

- 7.1: Platform claims in `00_version_release_platform.md:261`-`:287` match sampled Korean supported-platform and 7.1 release-note evidence. Native `JSON`, Temporary LOB checks, `IF EXISTS`/`IF NOT EXISTS`, and replication SSL are not presented as 7.1 baseline features.
- 7.3: Platform claims in `00_version_release_platform.md:289`-`:315` match sampled Korean supported-platform and 7.3 release-note evidence. Native `JSON`, Temporary LOB, and replication SSL are not presented as 7.3 baseline features.
- 8.1: JSON, Temporary LOB, `V$TEMPORARY_LOBS`, `V$MEM_STABLE`, `V$LOCK_TABLE_STATS`, `REPLICATION_SSL_PORT_NO`, `USING SSL`, component version boundaries, and platform boundaries are supported by sampled Korean authoritative sources or 8.1 release notes. JSON-plan property names are release-note-backed only and are labeled narrowly.

## Retrieval And GPT Answer Quality

- Strengths: the scoped attachments now align on the high-risk 8.1 boundaries, preserve literal token names, keep customer-facing source labels safe, separate ordinary client/server SSL from replication SSL, and provide check SQL for runtime verification.
- Risks: future retrieval could still over-answer JSON plan detail if another stage adds examples without locating a later source. Platform support can also change by patch, so answers should continue collecting exact version, patch, OS, CPU, and glibc details before giving support guidance.

## Required Follow-Up

- None required for R02.
- Carry forward the residual JSON-plan source gap to later performance/retrieval review stages: state only release-note-backed feature and property names unless a later source provides schema, values, or examples.
- In later SQL/DDL stages, consider replacing any remaining non-critical "customer verified support" phrasing with exact source/version wording when the statement affects executable SQL generation.
