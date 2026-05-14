# R14 Retrieval Structure, Visual Conversion, and Answerability

Date: 2026-05-14
Reviewer: Codex
Verdict: Review Required

## Scope

- Attachments: `GPTs/attachments/*.md`, `GPTs/attachments/README.md`
- Supporting reports: `GPTs/reports/image_inventory.md`, `GPTs/reports/table_inventory.md`, `GPTs/reports/link_inventory.md`
- Source manuals sampled: None directly; this stage checked retrieval structure and conversion readiness against the attachment files and existing inventory reports.

## Commands Run

```bash
sed -n '1,240p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,220p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,260p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' | sort
wc -l GPTs/attachments/*.md
rg -n "!\[|<img|\.png|\.jpg|\.jpeg|\.gif|\.svg|file://|trunk|Manuals/|ReleaseNotes/|/home/|C:\\|TODO|Conversion TODO|TBD|FIXME" GPTs/attachments
rg -n "^## (Applicable Versions|Source Documents|Questions This File Can Answer|Core Guidance|Version Differences|Conversion TODO)" GPTs/attachments/*.md
awk '/^```mermaid/ {inb=1; start=FNR; lines=0; next} inb && /^```/ {if(lines>18) print FILENAME ":" start ":" lines " mermaid content lines"; inb=0; next} inb {lines++}' GPTs/attachments/*.md
awk '/^\|/ { if(!inblock){inblock=1; start=FNR; rows=0; file=FILENAME} rows++; next } { if(inblock){ if(rows>=12) print file ":" start ":" rows " table rows"; inblock=0; rows=0 } } END{if(inblock && rows>=12) print file ":" start ":" rows " table rows"}' GPTs/attachments/*.md
awk '/^```text/ {inb=1; start=FNR; lines=0; next} inb && /^```/ {if(lines>80) print FILENAME ":" start ":" lines " text fence lines"; inb=0; next} inb {lines++}' GPTs/attachments/*.md
rg -n 'attachment [0-9]|Attachment [0-9]|`[0-9][0-9]_[^`]+\.md`|Cross-References|cross-reference the .* attachment|Use attachment|see attachment' GPTs/attachments/*.md
```

## Findings

No Blocker or High issues were found.

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Medium | `GPTs/attachments/03_sql_ddl_generation.md` | 225 | The `Table Syntax` fenced text block is 89 content lines and combines `CREATE TABLE`, column definitions, constraints, `DROP TABLE`, core `ALTER TABLE`, and partition grammar. This is converted out of image form, but it is still a large syntax chunk rather than a compact retrieval block keyed to likely questions. | Split into smaller subsections or item blocks such as `CREATE TABLE`, column definition, constraint definition, `ALTER TABLE`, and partition maintenance. Keep the 7.1/7.3 versus 8.1 `IF EXISTS` notes beside the exact statements they qualify. |
| Medium | `GPTs/attachments/03_sql_ddl_generation.md` | 660 | The `Additional SQL Reference DDL and DCL Syntax` fenced text block is 167 content lines and mixes `ALTER DATABASE`, directory, synonym, view, materialized view, trigger, job, maintenance, session/system control, and audit syntax. Retrieval for a specific statement can land in the middle of a broad opaque grammar block. | Break this into statement-level compact blocks with short lead-in questions and examples. Prioritize `ALTER DATABASE`, `CREATE VIEW`, materialized view, trigger, audit, and job syntax as separate searchable units. |
| Medium | `GPTs/attachments/12_c_cli_odbc_precompiler.md` | 107 | The CLI API sequence diagram is 31 content lines and exceeds the README guidance to split Mermaid diagrams when they become large. Similar oversized Mermaid blocks appear in operational triage and lifecycle flows, including `02_administration_operations.md:1628`, `09_replication_ha_cdc.md:1239`, and `17_kubernetes_aku_cloud.md:294`. | Split long diagrams into smaller phase diagrams or replace parts with checklist/item blocks. For CLI, separate allocation/connect, prepare/execute/fetch, transaction, and cleanup phases. |
| Low | `GPTs/attachments/07_error_messages_troubleshooting.md` | 1484 | The customer-facing attachment still contains a `Conversion TODO` section and an internal build reference, `JOB-042`. Even though it says no TODO remains, the heading and job label are build-process noise that may be retrieved in customer answers. | Remove the `Conversion TODO` section or convert it to a customer-safe residual note outside the upload attachment. |
| Low | `GPTs/attachments/03_sql_ddl_generation.md` | 835 | Cross-references are useful but inconsistent. This file uses `attachment 10`, `attachment 02`, and `attachment 18` instead of literal filenames; `16_dblink_external_connectors.md:35` similarly says "Java/JDBC/Spring attachment." Only `15_migration_oracle_compatibility.md` has a dedicated literal `Attachment Cross-References` section. | Use literal filenames in cross-reference text, for example `10_psm_stored_external_procedures.md`, `02_administration_operations.md`, and `18_security_ssl_tls.md`. Add small cross-reference sections to high-traffic files where another attachment is the better answer source. |
| Low | `GPTs/attachments/04_sql_dml_oracle_compatibility.md` | 36 | A few small tables have very long cells containing many distinct searchable tokens, especially the Oracle compatibility classifier and the version-difference table in `10_psm_stored_external_procedures.md:35`. They are not large source tables, but they are less scannable than item blocks. | Convert dense classifier/version rows into short bullet item blocks if these files are revised. Keep the table only when column comparison is essential. |

## Source Checks

- Claims checked: upload boundary count, presence of question sections, residual image links, residual source/internal labels, broad table blocks, long Mermaid blocks, long syntax fences, and explicit cross-reference patterns.
- Source coverage: all 20 attachment files plus `README.md` were scanned; image, table, and link inventory reports were read for expected conversion load.
- Source gaps: no primary manual line-by-line source validation was performed in this stage. SQL/DDL correctness findings should be handled by the SQL and source-fidelity review stages.

## Oracle-Overlap Decision

- Correctly compressed: `04_sql_dml_oracle_compatibility.md` keeps ordinary `SELECT`, `INSERT`, `UPDATE`, `DELETE`, joins, predicates, and common functions brief and emphasizes Altibase-specific differences.
- Too much generic Oracle material: no broad generic Oracle expansion was found in this retrieval pass.
- Missing Altibase-specific difference: none proven by this stage; the residual risk is that the long DDL grammar blocks in `03_sql_ddl_generation.md` may bury Altibase-specific version notes.

## Version Checks

- 7.1: attachment headers and version-difference sections consistently include 7.1 coverage.
- 7.3: attachment headers and version-difference sections consistently include 7.3 coverage.
- 8.1: customer-safe `Altibase 8.1 verified source` wording is present; no `trunk` label was found in attachments. The remaining `JOB-042` build reference in `07_error_messages_troubleshooting.md` should be removed before upload.

## Retrieval And GPT Answer Quality

- Strengths: every upload attachment has `Questions This File Can Answer` near the top; no raw image links remain; large source-table inventory targets appear mostly converted into item blocks; SQL syntax diagrams are generally represented as fenced text rather than external visuals; operational, replication, tool, and connector files use many task-oriented headings.
- Risks: the central DDL file still has two large grammar fences that are less answerable than statement-level blocks; several Mermaid diagrams are readable but exceed compactness guidance; cross-file routing is not consistently literal; one attachment still contains build-process language.

## Required Follow-Up

- Split the two long syntax fences in `03_sql_ddl_generation.md` into smaller searchable blocks.
- Reduce or split oversized Mermaid diagrams, starting with `12_c_cli_odbc_precompiler.md:107`, then the representative operational and lifecycle diagrams listed above.
- Remove the `Conversion TODO`/`JOB-042` text from `07_error_messages_troubleshooting.md`.
- Normalize cross-references to literal attachment filenames in high-traffic files.
- Optional: convert the remaining dense classifier/version tables to item blocks during final polish.
