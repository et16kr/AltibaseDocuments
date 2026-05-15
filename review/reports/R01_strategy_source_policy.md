# R01 Attachment Selection, Oracle-Overlap Strategy, and Source Policy

Date: 2026-05-16
Reviewer: Codex
Verdict: Pass

## Scope

- Attachments: `GPTs/Altibase_GPT_Document_Selection.md`; `GPTs/Altibase_GPT_Attachment_Build_Workplan.md`; `GPTs/attachments/README.md`; `GPTs/attachments/*.md`.
- Supporting reports: `GPTs/reports/source_inventory.md`; `GPTs/reports/eng_kor_parity.md`; `GPTs/reports/8_1_verification.md`.
- Source manuals sampled: `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`; `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`; `Manuals/Altibase_trunk/kor/SQL Reference.md`; `Manuals/Altibase_trunk/kor/Replication Manual.md`; `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`.

## Commands Run

```bash
bash review/scripts/run_review_remediation_cycle.sh status
rg -n $'\t(Reviewing|Remediating|ReReviewing|Fail)$' review/review_remediation_cycle_status.tsv
git status --short

git diff -- review/review_remediation_cycle_status.tsv
git diff -- review/review_stage_status.tsv
ls -l review/reports/R01_strategy_source_policy.md
rg -n '^R01\b|^ID\b' review/review_remediation_cycle_status.tsv review/review_stage_status.tsv

sed -n '1,240p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,260p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,280p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' -printf '%f\n' | sort

sed -n '1,260p' GPTs/reports/source_inventory.md
sed -n '1,260p' GPTs/reports/eng_kor_parity.md
sed -n '1,280p' GPTs/reports/8_1_verification.md
sed -n '1,120p' review/review_stages.tsv

wc -l GPTs/attachments/*.md
rg -n '^# |^## (Applicable Versions|Source Documents|Questions This File Can Answer|Core Guidance|Version Differences|Residual Scope Notes)' GPTs/attachments/*.md
rg -n '^## |^### |^# ' GPTs/attachments/*.md
rg -n 'Oracle|DML|SELECT|INSERT|UPDATE|DELETE|MERGE|JOIN|Altibase-specific|Similar to Oracle|Different in Altibase' GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/04_sql_dml_oracle_compatibility.md GPTs/attachments/15_migration_oracle_compatibility.md
rg -n 'trunk|Manuals/|ReleaseNotes/|Technical Documents/|/home/|C:/|file://|Altibase_8|internal source|local build|workstation' GPTs/attachments/*.md
rg -n 'Korean|source of truth|authoritative|English|Altibase 8\.1 verified source' GPTs/attachments/*.md GPTs/Altibase_GPT_Document_Selection.md GPTs/Altibase_GPT_Attachment_Build_Workplan.md GPTs/attachments/README.md
rg -n 'JSON|Temporary LOB|TEMPORARY_LOB|V\$TEMPORARY_LOBS|MEMORY_TEMPLOB|USING SSL|REPLICATION_SSL_PORT_NO|TRCLOG_EXPLAIN_TYPE|TRCLOG_JSON_PLAN_INDENT_DEPTH|SQLFreeLob2|IS JSON' GPTs/attachments/*.md

find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' -printf '%f\n' | sort | wc -l
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' -printf '%f\n' | sort
for f in GPTs/attachments/*.md; do case "$f" in */README.md) continue;; esac; for h in '## Applicable Versions' '## Questions This File Can Answer' '## Source Documents'; do rg -q "^$h$" "$f" || printf '%s missing %s\n' "$f" "$h"; done; done
rg -n '^## (Applicable Versions|Questions This File Can Answer|Source Documents)' GPTs/attachments/*.md | wc -l
rg -n '8\.1|7\.1|7\.3' GPTs/attachments/*.md | wc -l

rg -n 'JSON \[ IN ROW|JSON_ARRAY|JSON_OBJECT|JSON_EXISTS|JSON_QUERY|JSON_VALUE|JSON_VALID|IS JSON' 'Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md' 'Manuals/Altibase_trunk/kor/SQL Reference.md'
rg -n 'Temporary LOB|TEMPORARY_LOB_ENABLE|MEMORY_TEMPLOB|V\$TEMPORARY_LOBS|ALTER SESSION SET FREE TEMPORARY LOB' 'Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md' 'Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md' 'Manuals/Altibase_trunk/kor/SQL Reference.md'
rg -n 'USING SSL|REPLICATION_SSL_PORT_NO' 'Manuals/Altibase_trunk/kor/Replication Manual.md' 'Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md' 'Manuals/Altibase_trunk/kor/SQL Reference.md'
rg -n 'JSON|Temporary LOB|REPLICATION_SSL_PORT_NO|USING SSL|TRCLOG_EXPLAIN_TYPE|TRCLOG_JSON_PLAN_INDENT_DEPTH' 'ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md'

git diff --check
rg -n '^Verdict:|^\| (Blocker|High|Medium|Low) \|' review/reports/R01_strategy_source_policy.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' -printf '%f\n' | sort | wc -l
git status --short
```

## Findings

No actionable Blocker, High, Medium, or Low findings were found for R01. The attachment strategy matches the selection criteria, keeps generic Oracle-overlap material constrained, and does not leave a major Altibase-specific area underrepresented at the strategy level.

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Note | `GPTs/Altibase_GPT_Document_Selection.md` | 40 | The selection document defines the required 20 upload units, and the live attachment directory contains the same 20 files excluding `README.md`. | Keep the exact-file-count check in later validation and avoid splitting or merging files without updating the selection document. |
| Note | `GPTs/attachments/README.md` | 15 | The README states the intended bias toward Altibase-specific DDL, configuration, operation, compatibility, and troubleshooting behavior. The current file map gives dedicated coverage to those areas through files `02`, `03`, `05`, `06`, `07`, `08`, `09`, `14`, `18`, and related tool/interface files. | Continue topic-specific source audits in R02 and later stages, but no R01 selection remediation is required. |
| Note | `GPTs/attachments/04_sql_dml_oracle_compatibility.md` | 23 | The DML attachment explicitly instructs answers to compress generic Oracle SQL and expand only Altibase differences, restrictions, JSON behavior, LOB behavior, and compatibility boundaries. | Keep R07 focused on whether this compression preserves exact Altibase DML differences; the strategy itself is appropriate. |
| Note | `GPTs/reports/eng_kor_parity.md` | 63 | The supporting parity report records the expected Korean-source detail cases for 8.1 JSON, Temporary LOB, replication SSL, and JSON-plan caution, and the sampled Korean sources contain matching technical anchors. | Treat these areas as high-priority source-fidelity checks in R02, R06, R09, R10, R18, and R22. |

## Source Checks

- Claims checked: 20-file selection against the live attachment directory; presence of `Applicable Versions`, `Questions This File Can Answer`, and `Source Documents` in every upload attachment; source policy alignment with Korean-source precedence; sampled 8.1 Korean-source anchors for JSON, Temporary LOB, replication SSL, and release-note-only JSON plan.
- Source coverage: `GPTs/reports/source_inventory.md:25-29` reports 20 inventoried attachments, 20 with 7.1 source paths, 20 with 7.3 source paths, 20 with Altibase 8.1 verified source paths, and no missing blocking source paths. The heading validation command produced no missing-heading output.
- Korean/English source conflicts: no unhandled R01-level conflict was found. Known English-source gaps are already recorded for JSON, Temporary LOB, replication SSL, and JSON plan in `GPTs/reports/eng_kor_parity.md:63-69` and `GPTs/reports/8_1_verification.md:22-25`. Sampled Korean sources include JSON syntax/functions at `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md:2766` and `Manuals/Altibase_trunk/kor/SQL Reference.md:23609`; Temporary LOB and `V$TEMPORARY_LOBS` at `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md:2617` and `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md:11665`; replication SSL at `Manuals/Altibase_trunk/kor/Replication Manual.md:1110`, `:1188`, and `:1198`.
- Source gaps: R01 did not fully audit every technical claim in the attachments against Korean manuals. JSON plan remains intentionally release-note-only: `GPTs/reports/8_1_verification.md:25` and `:85-87` state that neither English nor Korean manuals provided detailed JSON plan schema coverage.

## Oracle-Overlap Decision

- Correctly compressed: `GPTs/Altibase_GPT_Document_Selection.md:68` defines ordinary `SELECT`, `INSERT`, `UPDATE`, `DELETE`, basic joins, predicates, and general functions as Oracle-overlap material to keep brief. The DML attachment applies that policy with an Oracle compatibility classifier at `GPTs/attachments/04_sql_dml_oracle_compatibility.md:32` and a residual-scope warning at `GPTs/attachments/04_sql_dml_oracle_compatibility.md:1120`.
- Too much generic Oracle material: none found at the strategy level. The longest Oracle-heavy file is `15_migration_oracle_compatibility.md`, but its scope is migration risk, conversion mapping, and `oraAdapter` behavior rather than generic Oracle SQL teaching.
- Missing Altibase-specific difference: none found at the strategy level. Altibase-specific DDL, tablespaces, memory/disk/volatile storage, properties, data dictionary, troubleshooting, performance, replication/HA/CDC, SSL/TLS, PSM, client APIs, tools, migration, DB Link, Kubernetes/AKU, and miscellaneous integrations all have an explicit attachment home.

## Version Checks

- 7.1: Every upload attachment has an `Applicable Versions` section and 7.1 source coverage is present in the inventory. The content strategy keeps 7.1 in scope for SQL, operations, tools, client interfaces, and source-backed compatibility.
- 7.3: Every upload attachment has an `Applicable Versions` section and 7.3 source coverage is present in the inventory. The strategy explicitly separates 7.3 from 7.1 and 8.1 where features differ.
- 8.1: Customer-facing wording consistently uses `Altibase 8.1 verified source` rather than internal source-tree labels. The high-risk 8.1 additions, including native `JSON`, Temporary LOB, `V$TEMPORARY_LOBS`, replication SSL, and JSON-plan property names, have dedicated attachment locations and source-report tracking.

## Retrieval And GPT Answer Quality

- Strengths: the 20-file set is topic-oriented and answer-oriented rather than manual-shaped. High-frequency customer paths are covered by dedicated files for version/platform, installation, administration, DDL generation, DML compatibility, data types/properties, dictionary/performance views, troubleshooting, performance, replication/CDC, PSM, Java/JDBC/Spring, C/CLI/ODBC/precompiler, iSQL/iLoader, utilities, migration, DB Link/connectors, Kubernetes/AKU, security/TLS, and spatial/miscellaneous integrations. All upload attachments have the three required top sections checked in this stage.
- Risks: this stage validates strategy and coverage shape, not every claim. Later stages still need to source-audit high-risk syntax, operational procedures, error actions, system-view columns, property semantics, API call order, and version-specific feature boundaries against the Korean authoritative manuals.

## Required Follow-Up

- No R01 remediation is required.
- Continue with R02 for high-risk source traceability, especially 8.1 JSON, Temporary LOB, replication SSL, `V$TEMPORARY_LOBS`, JSON plan properties, and supported-platform/version-boundary claims.
- Preserve R27 as the final readiness gate after upstream source-fidelity, retrieval, and multilingual-token preservation checks are complete.
