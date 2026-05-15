# R01 Attachment Selection, Oracle-Overlap Strategy, and Source Policy

Date: 2026-05-14
Reviewer: Codex
Verdict: Pass With Follow-Up

## Scope

- Attachments: `GPTs/Altibase_GPT_Document_Selection.md`; `GPTs/Altibase_GPT_Attachment_Build_Workplan.md`; `GPTs/attachments/README.md`; all 20 numbered files under `GPTs/attachments/`
- Supporting reports: `GPTs/reports/source_inventory.md`; `GPTs/reports/eng_kor_parity.md`; `GPTs/reports/8_1_verification.md`
- Source manuals sampled: none directly; this stage checked attachment strategy and source policy against the selection documents and existing source reports.

## Commands Run

```bash
pwd
wc -l review/Altibase_GPT_Detailed_Review_Design.md GPTs/Altibase_GPT_Document_Selection.md GPTs/Altibase_GPT_Attachment_Build_Workplan.md GPTs/attachments/README.md
rg --files GPTs/attachments
nl -ba review/Altibase_GPT_Detailed_Review_Design.md
nl -ba GPTs/Altibase_GPT_Document_Selection.md
nl -ba GPTs/Altibase_GPT_Attachment_Build_Workplan.md
nl -ba GPTs/attachments/README.md
wc -l GPTs/attachments/*.md
nl -ba GPTs/reports/source_inventory.md
nl -ba GPTs/reports/eng_kor_parity.md
nl -ba GPTs/reports/8_1_verification.md
rg -n "^(#|##|###) " GPTs/attachments/*.md
find GPTs/attachments -maxdepth 1 -type f -name '[0-9][0-9]_*.md' | sort
find GPTs/attachments -maxdepth 1 -type f -name '[0-9][0-9]_*.md' | wc -l
rg -n "trunk|Altibase_trunk|Manuals/|ReleaseNotes/|Technical Documents/|3rd Party Guide|C:/|file://" GPTs/attachments/[0-9][0-9]_*.md
rg -n "!\[[^\]]*\]\(|\.png|\.jpg|\.jpeg|\.gif|\.svg|\.webp" GPTs/attachments/[0-9][0-9]_*.md
rg -n "JSON|Temporary LOB|TEMPORARY_LOB_ENABLE|V\$TEMPORARY_LOBS|SQLFreeLob2|USING SSL|REPLICATION_SSL_PORT_NO|TRCLOG_EXPLAIN_TYPE|TRCLOG_JSON_PLAN_INDENT_DEPTH" GPTs/attachments/[0-9][0-9]_*.md
rg -n "sampled 7\.3 Korean source|sampled 7\.x|sampled SNMP sources|ReleaseNotes" GPTs/attachments/[0-9][0-9]_*.md
git status --short
```

## Findings

No Blocker findings were found. High and Medium findings are listed first.

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Resolved High | `GPTs/attachments/17_kubernetes_aku_cloud.md` | 5 | The 7.1 metadata and body assert `aku` utility guidance and a 7.1 AKU scale limit of 4 replicas, repeated at lines 58 and 392, but the source inventory for this attachment lists only 7.1 Installation, Administrator, and Replication manuals for 7.1 (`GPTs/reports/source_inventory.md:302`). That leaves an operational version claim without traceability to the selected 7.1 source set. | Resolved by H01. The AKU traceability issue is no longer an open High gate item; remaining rows in this report are Medium/Low follow-ups. |
| Medium | `GPTs/attachments/11_java_jdbc_spring.md` | 5 | The 7.1 metadata lists Spring Data JPA, Hibernate, and Java compatibility as 7.1 sources, and the body gives 7.1 Maven/Java compatibility details at lines 60 and 63. The source inventory lists only 7.1 JDBC and Adapter for JDBC manuals for this attachment; Spring guides are listed under 7.3 and 8.1, and Java compatibility is Korean-only supplemental (`GPTs/reports/source_inventory.md:201`). | Align the 7.1 source metadata and claims with the source inventory. If the Spring/Hibernate and Java compatibility notes are valid for 7.1, document that source basis safely; otherwise phrase them as driver-patch examples requiring target driver verification. |
| Medium | `GPTs/attachments/05_data_types_properties.md` | 1989 | Customer-facing text cites "sampled 7.3 Korean source" for `LISTAGG_PRECISION`, with the same pattern for `VARRAY_MEMORY_MAXIMUM` at line 2034. The approved Korean fallback register is for specific 8.1 gaps and supplemental technical docs, not customer-visible 7.3 source labels. | Move Korean/source-sampling traceability out of the attachment text. Use customer-safe version labels, and source-audit exact 7.1/7.3/8.1 availability for these properties before keeping cross-version claims. |
| Medium | `GPTs/attachments/02_administration_operations.md` | 18 | The architecture section uses broad marketing-style claims: "uniquely combines", "extreme high-performance (microsecond latency)", and "requires no external caching layer." This is not framed as a source-backed operational fact and could cause overconfident performance answers. | Rewrite as source-backed hybrid-storage guidance: Altibase supports memory and disk tables in one engine, and storage choice affects performance and capacity. Avoid latency guarantees unless a cited source and workload scope are added. |
| Low | `GPTs/attachments/00_version_release_platform.md` | 442 | The caveat uses backticked `ReleaseNotes`, which reads like an internal directory label rather than the customer-safe source label used elsewhere. | Replace with plain "release notes" or "Altibase release notes" in customer-facing text. |

## Source Checks

- Claims checked: exact 20-file attachment boundary; selected attachment names versus the recommendation; top-level source labels; presence of question-oriented sections; source policy strings; 8.1 JSON, Temporary LOB, replication SSL, JSON plan, and `SQLFreeLob2` coverage.
- Source coverage: the 20-file topic set matches the selection table. All numbered attachments include `Applicable Versions`, `Questions This File Can Answer`, and `Source Documents`. The 8.1 special-source topics from the verification reports are represented in the expected files: `00`, `03`, `04`, `05`, `06`, `07`, `08`, `09`, `10`, `12`, and `18`.
- Source gaps: no raw `trunk`, `Manuals/`, `ReleaseNotes/`, `C:/`, or `file://` strings were found in numbered attachments. The remaining gaps are source-traceability mismatches in `17` and `11`, plus customer-facing "sampled source" wording in `05`.

## Oracle-Overlap Decision

- Correctly compressed: `04_sql_dml_oracle_compatibility.md` explicitly says to compress generic Oracle SQL and expand only Altibase differences (`GPTs/attachments/04_sql_dml_oracle_compatibility.md:26`). Its classifier keeps ordinary DML brief while focusing on row limiting, DML `RETURN`, `MERGE WHEN NO ROWS`, JSON, queue DML, restrictions, hints, and function differences.
- Too much generic Oracle material: none found at this strategy stage. The DML file is long, but the length is mostly Altibase syntax boundaries, restrictions, and examples rather than generic Oracle tutorial material.
- Missing Altibase-specific difference: no major missing Oracle-overlap difference found at this stage. Detailed SQL correctness should remain in later SQL-focused stages.

## Version Checks

- 7.1: Covered across the 20 files, but `17_kubernetes_aku_cloud.md` and `11_java_jdbc_spring.md` need source-traceability cleanup for 7.1-specific AKU and Java/Spring claims.
- 7.3: Covered across the 20 files. `05_data_types_properties.md` should remove customer-facing "sampled 7.3 Korean source" wording or back those claims with customer-safe source labels.
- 8.1: The attachment set consistently uses `Altibase 8.1 verified source` wording. JSON, Temporary LOB, replication SSL, JSON plan property names, and `SQLFreeLob2` are present and generally scoped conservatively.

## Retrieval And GPT Answer Quality

- Strengths: the set is organized by customer question topic, with deep coverage concentrated in Altibase-specific DDL, storage, properties, data dictionary, administration, troubleshooting, performance, replication, security, tooling, migration, and connectors. The numbered files are searchable, sectioned, and mostly use literal technical tokens correctly.
- Risks: source-inventory drift in a few version-sensitive files could lead GPT answers to overstate 7.1 AKU or Java/Spring support. A few customer-facing phrases still read like work-report provenance rather than final attachment language. Release-note-only 8.1 feature families such as KADA, Kafka connectors, ABM, MindsDB, `.NET 8`, EF Core, and `node-odbc-altibase` are intentionally summarized but not implementation-ready.

## Required Follow-Up

- Source-audit and resolve the `17_kubernetes_aku_cloud.md` 7.1 AKU claims before upload.
- Align `11_java_jdbc_spring.md` 7.1 source labels and version claims with the source inventory.
- Clean customer-facing provenance wording in `05_data_types_properties.md` and the `ReleaseNotes` wording in `00_version_release_platform.md`.
- Reword the unsupported performance/architecture claim in `02_administration_operations.md`.
- After these source-policy fixes, rerun the same count, unsafe-label, image-link, and 8.1 feature-coverage validation commands.
