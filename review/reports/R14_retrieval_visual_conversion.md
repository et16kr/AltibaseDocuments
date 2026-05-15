# R14 Retrieval Structure, Visual Conversion, and Answerability

Date: 2026-05-15
Reviewer: Codex
Verdict: Review Required

## Scope

- Attachments: `GPTs/attachments/*.md`; `GPTs/attachments/README.md`
- Supporting reports: `GPTs/reports/image_inventory.md`; `GPTs/reports/table_inventory.md`; `GPTs/reports/link_inventory.md`
- Source manuals sampled: None directly. This stage was a structural retrieval and conversion review using the attachment files and inventory reports.

## Commands Run

```bash
sed -n '1,220p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,220p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,260p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
find GPTs/attachments -maxdepth 1 -type f -name '[0-9][0-9]_*.md' | wc -l
rg -n "!\[|<img\b|\.(png|gif|jpe?g|svg)\b|media/|file://|C:/|C:\\|/Users/|Manuals/Altibase_trunk|\btrunk\b" GPTs/attachments
rg -n '^## ' GPTs/attachments/[0-9][0-9]_*.md
awk '/^## Questions This File Can Answer$/{insec=1; start=FNR; count=0; file=FILENAME; next} insec && /^## /{print file ":" start ": question_lines=" count; insec=0} insec && /^- /{count++}' GPTs/attachments/[0-9][0-9]_*.md
awk 'FNR==1{if(NR>1) print prev, h2, h3; prev=FILENAME; h2=0; h3=0} /^## /{h2++} /^### /{h3++} END{print prev, h2, h3}' GPTs/attachments/[0-9][0-9]_*.md
awk 'FNR==1{file=FILENAME} /^```mermaid/{inm=1; start=FNR; lines=0; edges=0; next} inm && /^```$/{print file ":" start ": mermaid_lines=" lines " edge_lines=" edges; inm=0; next} inm{lines++; if($0 ~ /-->|---|==>|-.->/) edges++}' GPTs/attachments/[0-9][0-9]_*.md
awk '/^\|.*\|[[:space:]]*$/{if(!inblock){inblock=1; start=FNR} rows++; next} {if(inblock){print FILENAME ":" start ": table_rows=" rows; inblock=0; rows=0}} END{if(inblock) print FILENAME ":" start ": table_rows=" rows}' GPTs/attachments/[0-9][0-9]_*.md
rg -n 'V\$STATNAME|V\$MEMSTAT|V\$SESSION|V\$INTERNAL_SESSION|V\$BUFFPOOL_STAT|V\$TRANSACTION|V\$ALLCOLUMN|V\$TABLE\b' GPTs/attachments/06_data_dictionary_performance_views.md
rg -n 'SQLSTATE|Data type|Conversion|CallableStatement|ResultSet|Supported|Exception|block' GPTs/attachments/11_java_jdbc_spring.md
rg -n 'Attachment Cross-References|Cross-reference|Cross-References|See `|related attachment|`[0-9][0-9]_' GPTs/attachments/[0-9][0-9]_*.md
```

## Findings

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| High | `GPTs/attachments/06_data_dictionary_performance_views.md` | 1526 | The file has a `Searchable Object Blocks` section, but it does not decompose several top-priority dictionary/performance table families identified in `table_inventory.md`, including `V$STATNAME`, `V$MEMSTAT`, `V$BUFFPOOL_STAT`, `V$INTERNAL_SESSION`, and detailed column-level blocks for large views. `rg` found no `V$STATNAME` or `V$MEMSTAT` occurrences in the attachments. This weakens answerability for statistic identifiers, memory modules, buffer pool counters, and exact view-column questions. | Add compact object/column blocks for the missing high-priority performance view families. Key each block by view/statistic/module/column name, include purpose, key columns, when to query it, and a representative SQL check. |
| High | `GPTs/attachments/11_java_jdbc_spring.md` | 542 | The JDBC type/API material is reduced to "Basic data type mapping blocks" and "JDBC 4.2 API support highlights" instead of the method-level and type-level decompositions expected for the P0/P1 JDBC matrices. Specific `ResultSet` and `CallableStatement` support details are only highlighted around lines 573-578. | Add searchable blocks for the high-risk JDBC matrices: one block per important Java/JDBC type mapping and one block per relevant `ResultSet`, `CallableStatement`, `PreparedStatement`, and LOB method family with support status, exception behavior, and version notes. |
| High | `GPTs/attachments/11_java_jdbc_spring.md` | 630 | The source inventory flags the JDBC SQL state table as P0, but the attachment condenses it into a small set of SQLSTATE class blocks. This is useful for common cases, but not enough for direct lookup of many specific SQLSTATE values. | Expand the SQLSTATE section into searchable blocks by class and subclass for the retained JDBC table entries. Keep the current class summaries, but add enough specific code blocks to answer code-level troubleshooting questions without guessing. |
| Medium | Multiple attachments | 65 | Several Mermaid blocks exceed the project's compact diagram guideline of roughly 12 nodes or 16 edges. Examples include `02_administration_operations.md:65` with 18 edge lines, `02_administration_operations.md:1670` with 22 edge lines, `12_c_cli_odbc_precompiler.md:107` with a 31-line sequence, `12_c_cli_odbc_precompiler.md:1249` with 19 edge lines, `14_utilities_operation_tools.md:588` with 17 edge lines, and `17_kubernetes_aku_cloud.md:294` with 18 edge lines. They are readable, but less retrieval-friendly than smaller diagrams plus item blocks. | Split the largest diagrams into phase-specific diagrams or replace linear portions with ordered item blocks. Keep diagrams for relationships and put long procedure/detail text outside Mermaid. |
| Medium | Multiple attachments | 1246 | Cross-reference coverage is uneven. `15_migration_oracle_compatibility.md:1246` has a useful `Attachment Cross-References` section, and a few inline references exist in `03` and `16`, but most high-overlap files do not provide a local cross-reference block. This reduces retrieval help for questions that span DDL, properties, performance views, troubleshooting, replication, SSL/TLS, and tools. | Add short `Attachment Cross-References` sections to high-overlap files, especially `02`, `03`, `05`, `06`, `07`, `08`, `09`, `12`, `14`, and `18`. Keep each section to 3-6 links with the concrete reason to use the related attachment. |
| Low | Multiple attachments | 3 | All 20 attachments have `Applicable Versions`, `Questions This File Can Answer`, and `Source Documents`, but section naming is not fully uniform. Many files use `Response Rules`, `Version Notes`, or topic-specific headings instead of the common template, and only `07_error_messages_troubleshooting.md:1532` has a `Residual Scope` section. | Before upload, normalize only the retrieval-critical top-level headings that help GPT routing. At minimum, add a short residual-scope note where source coverage is intentionally partial or condensed. |

## Source Checks

- Claims checked: upload file count, image/link cleanup, internal-label cleanup, required question sections, heading density, Mermaid block size, remaining table blocks, BNF-like syntax presence, and selected high-risk table-decomposition targets.
- Source coverage: The review used the selection/build design documents plus image, table, and link inventories. It did not re-audit primary manual claims line by line.
- Source gaps: The missing or condensed P0/P1 table-family items in `06_data_dictionary_performance_views.md` and `11_java_jdbc_spring.md` should be checked against the source manuals before being filled in.

## Oracle-Overlap Decision

- Correctly compressed: `04_sql_dml_oracle_compatibility.md` keeps generic Oracle-overlapping DML brief and focuses on Altibase-specific syntax, row limiting, DML `RETURN`, `MERGE`, hints, conditions, queue DML, and 8.1 JSON behavior.
- Too much generic Oracle material: No broad blocker found. The remaining generic content generally supports Altibase-specific differences or examples.
- Missing Altibase-specific difference: No single Oracle-overlap blocker found in this stage, but missing cross-reference blocks make it easier for retrieval to miss related Altibase-specific material in `03`, `05`, `06`, `09`, and `18`.

## Version Checks

- 7.1: All attachments include 7.1 applicability/source lines near the beginning.
- 7.3: All attachments include 7.3 applicability/source lines near the beginning.
- 8.1: Attachments use customer-safe `Altibase 8.1 verified source` wording. The validation search found no remaining `Manuals/Altibase_trunk`, bare `trunk`, `file://`, image references, or source-local absolute paths in the attachment set.

## Retrieval And GPT Answer Quality

- Strengths: The attachment set has the expected 20 upload files; every file has a question-oriented section with 5-8 bullets; headings are generally dense and topic-specific; raw image dependencies are absent; large source tables have mostly been converted into item blocks or small lookup tables; BNF-like syntax is present for SQL, PSM, replication, data type, spatial, and command syntax.
- Risks: A few high-priority table inventories appear under-decomposed rather than merely compressed; several diagrams are near or beyond the compactness policy; cross-file retrieval cues are inconsistent; residual scope is rarely stated, which makes intentional omissions harder to distinguish from accidental gaps.

## Required Follow-Up

- Expand the missing high-priority dictionary/performance view blocks in `06_data_dictionary_performance_views.md`.
- Expand JDBC SQLSTATE, method-support, and type-conversion blocks in `11_java_jdbc_spring.md`.
- Split or simplify the largest Mermaid diagrams listed in the findings.
- Add concise cross-reference blocks to the high-overlap attachments.
- Add residual-scope notes where content is intentionally partial, sampled, or condensed.
