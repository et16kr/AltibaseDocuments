# R01 Attachment Selection, Oracle-Overlap Strategy, and Source Policy

Date: 2026-05-14
Reviewer: Codex
Verdict: Pass

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

No Blocker findings were found. V02 re-review confirms that all previously listed High, Medium, and Low findings are closed by the remediation tasks named in the recommendation column.

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Resolved High | `GPTs/attachments/17_kubernetes_aku_cloud.md` | 5 | The 7.1 metadata and body assert `aku` utility guidance and a 7.1 AKU scale limit of 4 replicas, repeated at lines 58 and 392, but the source inventory for this attachment lists only 7.1 Installation, Administrator, and Replication manuals for 7.1 (`GPTs/reports/source_inventory.md:302`). That leaves an operational version claim without traceability to the selected 7.1 source set. | Resolved by H01. The AKU traceability issue is no longer an open High gate item. |
| Resolved Medium | `GPTs/attachments/11_java_jdbc_spring.md` | 5 | The 7.1 metadata listed Spring Data JPA, Hibernate, and Java compatibility as 7.1 sources, while the source inventory only listed 7.1 JDBC and Adapter for JDBC manuals for this attachment. | Resolved by M01. The attachment now treats the 7.1 Spring/Hibernate and Java compatibility material as driver-patch examples requiring target-driver verification rather than broad 7.1 source coverage. |
| Resolved Medium | `GPTs/attachments/05_data_types_properties.md` | 1989 | Customer-facing text cited "sampled 7.3 Korean source" for `LISTAGG_PRECISION`, with the same pattern for `VARRAY_MEMORY_MAXIMUM` at line 2034. | Resolved by M02. The attachment now uses customer-safe supplemental-source wording and keeps target-build verification cautions. |
| Resolved Medium | `GPTs/attachments/02_administration_operations.md` | 18 | The architecture section used broad marketing-style claims including "uniquely combines", "extreme high-performance (microsecond latency)", and "requires no external caching layer." | Resolved by M03. The section now uses source-neutral hybrid storage guidance without latency or cache-layer guarantees. |
| Resolved Low | `GPTs/attachments/00_version_release_platform.md` | 442 | The caveat used backticked `ReleaseNotes`, which read like an internal directory label rather than the customer-safe source label used elsewhere. | Resolved by L01. The wording now uses customer-safe "release notes" phrasing. |

## Source Checks

- Claims checked: exact 20-file attachment boundary; selected attachment names versus the recommendation; top-level source labels; presence of question-oriented sections; source policy strings; 8.1 JSON, Temporary LOB, replication SSL, JSON plan, and `SQLFreeLob2` coverage.
- Source coverage: the 20-file topic set matches the selection table. All numbered attachments include `Applicable Versions`, `Questions This File Can Answer`, and `Source Documents`. The 8.1 special-source topics from the verification reports are represented in the expected files: `00`, `03`, `04`, `05`, `06`, `07`, `08`, `09`, `10`, `12`, and `18`.
- Source gaps: no raw `trunk`, `Manuals/`, `ReleaseNotes/`, `C:/`, or `file://` strings were found in numbered attachments. The prior source-traceability and customer-facing provenance gaps are closed by H01, M01, M02, M03, and L01.

## Oracle-Overlap Decision

- Correctly compressed: `04_sql_dml_oracle_compatibility.md` explicitly says to compress generic Oracle SQL and expand only Altibase differences (`GPTs/attachments/04_sql_dml_oracle_compatibility.md:26`). Its classifier keeps ordinary DML brief while focusing on row limiting, DML `RETURN`, `MERGE WHEN NO ROWS`, JSON, queue DML, restrictions, hints, and function differences.
- Too much generic Oracle material: none found at this strategy stage. The DML file is long, but the length is mostly Altibase syntax boundaries, restrictions, and examples rather than generic Oracle tutorial material.
- Missing Altibase-specific difference: no major missing Oracle-overlap difference found at this stage. Detailed SQL correctness should remain in later SQL-focused stages.

## Version Checks

- 7.1: Covered across the 20 files. The prior AKU and Java/Spring source-traceability findings are closed by H01 and M01.
- 7.3: Covered across the 20 files. The prior customer-facing "sampled 7.3 Korean source" wording is closed by M02.
- 8.1: The attachment set consistently uses `Altibase 8.1 verified source` wording. JSON, Temporary LOB, replication SSL, JSON plan property names, and `SQLFreeLob2` are present and generally scoped conservatively.

## Retrieval And GPT Answer Quality

- Strengths: the set is organized by customer question topic, with deep coverage concentrated in Altibase-specific DDL, storage, properties, data dictionary, administration, troubleshooting, performance, replication, security, tooling, migration, and connectors. The numbered files are searchable, sectioned, and mostly use literal technical tokens correctly.
- Risks: the prior source-inventory drift and customer-facing provenance risks are closed. Release-note-only 8.1 feature families such as KADA, Kafka connectors, ABM, MindsDB, `.NET 8`, EF Core, and `node-odbc-altibase` remain intentionally summarized rather than implementation-ready.

## V02 Closure

- Closed by H01, M01, M02, M03, and L01.
- No open R01 finding remains after V02 re-review of the changed sections.
