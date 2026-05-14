# R01 Attachment Selection, Oracle-Overlap Strategy, And Source Policy

Date: 2026-05-14
Reviewer: Codex
Verdict: Fail

## Scope

- Attachments: `GPTs/Altibase_GPT_Document_Selection.md`; `GPTs/Altibase_GPT_Attachment_Build_Workplan.md`; `GPTs/attachments/README.md`; `GPTs/attachments/[0-9][0-9]_*.md`.
- Supporting reports: `GPTs/reports/source_inventory.md`; `GPTs/reports/eng_kor_parity.md`; `GPTs/reports/8_1_verification.md`.
- Source manuals sampled: `Manuals/Altibase_7.1/eng/Replication Manual.md`; `Manuals/Altibase_7.3/eng/Replication Manual.md`; `Manuals/Altibase_trunk/eng/Replication Manual.md`; `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`.

## Commands Run

```bash
sed -n '1,240p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,240p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,260p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
sed -n '1,560p' GPTs/reports/source_inventory.md
sed -n '1,260p' GPTs/reports/eng_kor_parity.md
sed -n '1,260p' GPTs/reports/8_1_verification.md
find GPTs/attachments -maxdepth 1 -type f -name '[0-9][0-9]_*.md' | wc -l
comm -3 <(printf '%s\n' 00_version_release_platform.md 01_getting_started_installation.md 02_administration_operations.md 03_sql_ddl_generation.md 04_sql_dml_oracle_compatibility.md 05_data_types_properties.md 06_data_dictionary_performance_views.md 07_error_messages_troubleshooting.md 08_performance_tuning_monitoring.md 09_replication_ha_cdc.md 10_psm_stored_external_procedures.md 11_java_jdbc_spring.md 12_c_cli_odbc_precompiler.md 13_isql_iloader_basic_tools.md 14_utilities_operation_tools.md 15_migration_oracle_compatibility.md 16_dblink_external_connectors.md 17_kubernetes_aku_cloud.md 18_security_ssl_tls.md 19_spatial_nifi_tableau_misc.md | sort) <(find GPTs/attachments -maxdepth 1 -type f -name '[0-9][0-9]_*.md' -printf '%f\n' | sort)
wc -l GPTs/attachments/*.md
rg -n "^#{1,3} " GPTs/attachments/*.md
rg -n "Conversion TODO|JOB-[0-9]+|trunk|file://|Manuals/|ReleaseNotes/|AltibaseDocuments|/home/|/Users/" GPTs/attachments/[0-9][0-9]_*.md GPTs/attachments/README.md
rg -n "Altibase 8\\.1 verified source|Altibase 8\\.1 Release Notes|8\\.1 verified" GPTs/attachments/*.md
rg -n "KADA|Kafka|ABM|abm|MindsDB|node-odbc-altibase|\\.NET 8|EF Core|Source Connector|Sink Connector" GPTs/attachments/[0-9][0-9]_*.md
rg -n -i "shard|ShardManager|scale-out" GPTs/attachments/[0-9][0-9]_*.md GPTs/reports/source_inventory.md GPTs/reports/eng_kor_parity.md
rg -n "sub-millisecond|guarantees|built-in conflict resolution|ShardManager|scale-out" GPTs/attachments/09_replication_ha_cdc.md "Manuals/Altibase_7.1/eng/Replication Manual.md" "Manuals/Altibase_7.3/eng/Replication Manual.md" "Manuals/Altibase_trunk/eng/Replication Manual.md"
rg -n -i "cannot guarantee data consistency|different update operations.*same record|data may be mismatched|Deferred Replication does not offer a perfect solution|The transaction corresponding to this XSN is not guaranteed" "Manuals/Altibase_7.1/eng/Replication Manual.md" "Manuals/Altibase_7.3/eng/Replication Manual.md" "Manuals/Altibase_trunk/eng/Replication Manual.md"
nl -ba GPTs/attachments/09_replication_ha_cdc.md | sed -n '1,70p'
nl -ba GPTs/attachments/00_version_release_platform.md | sed -n '88,116p'
nl -ba GPTs/attachments/04_sql_dml_oracle_compatibility.md | sed -n '62,138p'
nl -ba GPTs/attachments/04_sql_dml_oracle_compatibility.md | sed -n '667,826p'
```

## Findings

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Blocker | `GPTs/attachments/07_error_messages_troubleshooting.md` | 1484 | The attachment still contains `## Conversion TODO` and line 1486 exposes the internal workflow label `JOB-042`. This violates the customer-facing source policy and means the set is not upload-ready even before strategy issues are considered. | Remove this section or rewrite it as customer-safe residual scope text with no job IDs, internal workflow language, or future job references. Re-run the customer-safe string scan afterward. |
| High | `GPTs/attachments/09_replication_ha_cdc.md` | 20 | The overview claims Active-Active replication "guarantees sub-millisecond latency and built-in conflict resolution." The sampled replication manuals instead state that the committed XSN is not guaranteed to be committed remotely, that replication cannot guarantee data consistency against conflicts, that deferred replication does not offer a perfect solution to conflicts, and that different updates to the same record in Active-Active can mismatch data. This can produce unsafe HA guidance. | Replace the claim with source-backed wording: replication is log replay through Sender/Receiver/XLog, LAZY/EAGER have different commit behavior, Active-Standby is the usual HA recommendation, Active-Active needs write ownership and conflict planning, and no fixed latency or conflict-free guarantee should be stated. |
| High | `GPTs/attachments/09_replication_ha_cdc.md` | 21 | The file introduces "Sharding (ShardManager)" and tells the GPT to refer scaling-out users to sharding capabilities, but the selected source family for attachment 09 is replication, Log Analyzer, Replication Manager, and release notes. The parity report explicitly notes that the Korean-only `Sharding(deprecated).md` is not in the current attachment source inventory. This is a source-policy mismatch and can make the GPT over-answer an area not covered by the selected knowledge set. | Remove the sharding overview from attachment 09, or add a narrow source-scoped warning that sharding details are outside the selected attachment set except for error-code triage. Do not generate shard configuration guidance without a dedicated source audit and selected source family. |
| High | `GPTs/attachments/00_version_release_platform.md` | 104 | Several significant Altibase 8.1 feature families are release-summarized but not represented with usable answer depth in the task attachments: `KADA`, Kafka Source/Sink connectors, `abm`/ABM, MindsDB handler, `.NET 8`/EF Core, and `node-odbc-altibase`. A live search found these only in the version/platform file, while the 20-file selection table assigns related tool and connector coverage to files 11, 12, 14, and 16 without those source families. This leaves major 8.1 tool/connector areas underrepresented. | Either explicitly scope these as release-note-only in `00_version_release_platform.md` and instruct the GPT not to provide procedures, or add concise, source-backed blocks to the relevant existing attachments: `11` or `12` for API/client interfaces, `14` for `abm`, and `16` for Kafka/MindsDB/node connector coverage. |
| Medium | `GPTs/attachments/04_sql_dml_oracle_compatibility.md` | 62 | The DML attachment expands into broad SELECT subclause grammar and general condition/function syntax blocks at lines 62-138 and 667-826. This is useful reference material, but it weakens the intended Oracle-overlap compression strategy, which says ordinary `SELECT`, `INSERT`, `UPDATE`, `DELETE`, basic joins, predicates, and Oracle-equivalent functions should keep only key Altibase differences or limits. | Trim or demote generic grammar into short compatibility summaries. Preserve Altibase-specific material such as row limiting, `LIMIT`, `TOP`, `INLIST`, multi-table `DELETE`, `MOVE`, DML `RETURN`, JSON functions, queue DML, restrictions, and cautions. |
| Note | `GPTs/attachments/[0-9][0-9]_*.md` | N/A | The attachment count and file names match the final 20-file selection exactly. The exact-list `comm` check returned no differences, and the live count returned 20 numbered Markdown files. | No attachment selection rename or count change is needed. Fix the content/source-policy issues above within the existing 20-file structure unless the project explicitly reopens the selection list. |

## Source Checks

- Claims checked: 20-file selection match; customer-safe source labels; 8.1 verified-source policy; Oracle-overlap compression; replication HA claims; sharding source scope; 8.1 release-feature coverage.
- Source coverage: The 20 numbered attachment files match the selection document. Each attachment declares 7.1, 7.3, and 8.1 sources using customer-safe labels. The supporting inventory says all 20 attachments have source paths for 7.1, 7.3, and Altibase 8.1 verified source. The 8.1 JSON, Temporary LOB, replication SSL, and JSON plan policy is mostly reflected in files 03, 04, 05, 06, 08, 09, 12, and 18.
- Source gaps: The replication overview contains unsourced or contradicted HA guarantees. Sharding is introduced in attachment 09 without being part of the selected replication source family. Several 8.1 release-note feature families are not backed by procedural or troubleshooting depth in the task attachments.

## Oracle-Overlap Decision

- Correctly compressed: `03_sql_ddl_generation.md` gives depth to Altibase-specific DDL, storage, properties, tablespaces, queues, JSON, replication SQL, and verification queries. `04_sql_dml_oracle_compatibility.md` has a good classifier and answer templates that tell the GPT not to claim full Oracle compatibility.
- Too much generic Oracle material: `04_sql_dml_oracle_compatibility.md` still reads partly like a compact SQL Reference for SELECT subclauses, conditions, and analytic function grammar. This can make generic SQL grammar compete with Altibase-specific differences during retrieval.
- Missing Altibase-specific difference: No broad DML-specific omission was found in this stage. The larger missing-difference risk is in 8.1 non-SQL feature families where the set says they exist but does not give task-level guidance.

## Version Checks

- 7.1: 7.1 coverage is present across the selected attachment set. The replication overclaim affects 7.1 because the sampled 7.1 manual explicitly warns that conflict consistency is not guaranteed and that Active-Active updates to the same row can mismatch data.
- 7.3: 7.3 coverage is present and the set correctly highlights JDBC 4.2, OpenSSL/TLS changes, AKU, replication DDL synchronization, and migration requirements. The same replication overclaim affects 7.3.
- 8.1: The verified-source label policy is mostly followed, and JSON, Temporary LOB, replication SSL, JSON plan caution, and new property names are covered. However, `KADA`, Kafka connectors, ABM, MindsDB, `.NET 8`/EF Core, and `node-odbc-altibase` are only release-summarized, so the GPT should either be constrained to existence-level answers for these or receive source-backed coverage.

## Retrieval And GPT Answer Quality

- Strengths: The selected 20-file structure broadly matches the intended Altibase GPT purpose. DDL, storage, properties, data dictionary, operations, troubleshooting, performance, replication, security, tools, migration, and integration all have dedicated retrieval targets. Most files start with useful question scopes, source labels, response rules, and version boundaries.
- Risks: The remaining internal `JOB-042` label can leak into answers. The replication overview could cause confident but wrong HA claims. The sharding line invites out-of-scope answer generation. 8.1 release-feature summaries may trigger hallucinated how-to answers for KADA, Kafka connectors, ABM, MindsDB, .NET/EF Core, and Node.js because no detailed attachment covers them.

## Required Follow-Up

- Remove or customer-safely rewrite `GPTs/attachments/07_error_messages_troubleshooting.md:1484` through `GPTs/attachments/07_error_messages_troubleshooting.md:1486`.
- Rewrite `GPTs/attachments/09_replication_ha_cdc.md:19` through `GPTs/attachments/09_replication_ha_cdc.md:21` so HA, Active-Active, conflict handling, and sharding are source-backed and scoped.
- Decide the 8.1 release-feature strategy for KADA, Kafka connectors, ABM, MindsDB, `.NET 8`/EF Core, and `node-odbc-altibase`: either add scoped source-backed blocks to existing attachments or mark them release-note-only so the GPT does not invent procedures.
- Tighten `GPTs/attachments/04_sql_dml_oracle_compatibility.md` by reducing generic SQL grammar and keeping Altibase-specific differences, limits, and JSON behavior prominent.
- Re-run the count, forbidden-string/source-label, sharding-scope, and 8.1 feature coverage searches after the content fixes.
