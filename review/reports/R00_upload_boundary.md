# R00 Upload Boundary, Image Independence, And Customer-Safe Strings

Date: 2026-05-14
Reviewer: Codex
Verdict: Fail

## Scope

- Attachments: `GPTs/attachments/*.md`; `GPTs/attachments/README.md`.
- Supporting reports: `GPTs/reports/attachment_count_validation.md`; `GPTs/reports/forbidden_strings_validation.md`; `GPTs/reports/image_inventory.md`.
- Source manuals sampled: None. R00 checked the upload boundary, residual image dependencies, customer-safe labels, and conversion presence. It did not audit source-claim fidelity.

## Commands Run

```bash
sed -n '1,240p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,220p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,260p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
sed -n '1,240p' GPTs/reports/attachment_count_validation.md
sed -n '1,260p' GPTs/reports/forbidden_strings_validation.md
sed -n '1,320p' GPTs/reports/image_inventory.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' -printf '%f\n' | sort
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' | wc -l
find GPTs/attachments -maxdepth 1 -type f -printf '%f\n' | sort
find GPTs/attachments -maxdepth 1 -type f ! -name '*.md' -printf '%f\n'
find GPTs/attachments -maxdepth 2 -type f \( -iname '*.png' -o -iname '*.jpg' -o -iname '*.jpeg' -o -iname '*.gif' -o -iname '*.svg' -o -iname '*.webp' -o -iname '*.bmp' \) -printf '%p\n' | sort
rg -n "!\[[^\]]*\]\(|<img\b|\b(src|href)=['\"][^'\"]*\.(png|jpe?g|gif|svg|webp|bmp)|\.(png|jpe?g|gif|svg|webp|bmp)\b|media/|images/|image[0-9]*\.(gif|png|jpe?g)" GPTs/attachments/*.md
rg -n '(?i:\btrunk\b|file://|AltibaseDocuments|/home/|/Users/|Manuals/|ReleaseNotes/|source_inventory|JOB-[0-9]+|IMG-[0-9]+)|(^|[^A-Za-z])[A-Za-z]:[\\/]' GPTs/attachments/*.md GPTs/attachments/README.md
rg -n '(?i:\btrunk\b|file://|AltibaseDocuments|source_inventory|JOB-[0-9]+|IMG-[0-9]+|Manuals/|ReleaseNotes/)' GPTs/attachments/*.md GPTs/attachments/README.md
rg -n '(^|[^A-Za-z])[A-Za-z]:[\\/]|/home/|/Users/' GPTs/attachments/*.md GPTs/attachments/README.md
rg -n '(^|[^[:alnum:]_])(JOB-[0-9]+|IMG-[0-9]+)([^[:alnum:]_]|$)' GPTs/attachments/*.md
rg -n 'Conversion TODO' GPTs/attachments/*.md
rg -n '/home/|/Users/|/tmp/|/var/folders|AltibaseDocuments|GPTs/|Manuals/|ReleaseNotes/' GPTs/attachments/*.md
rg -n '^```mermaid|BNF|syntax notation|screenshot|wizard|diagram|flowchart|stateDiagram|sequenceDiagram' GPTs/attachments/*.md
rg -n '```mermaid' GPTs/attachments/*.md | cut -d: -f1 | sort | uniq -c
rg -c '^```mermaid$' GPTs/attachments/[0-9][0-9]_*.md
awk 'FNR==1{if(NR>1 && open) print prev ": unmatched code fence"; open=0; prev=FILENAME} /^```/{open=!open} END{if(open) print prev ": unmatched code fence"}' GPTs/attachments/[0-9][0-9]_*.md
nl -ba GPTs/attachments/07_error_messages_troubleshooting.md | sed -n '1480,1490p'
sed -n '1428,1452p' GPTs/attachments/19_spatial_nifi_tableau_misc.md
sed -n '20,115p' GPTs/attachments/01_getting_started_installation.md
sed -n '30,95p' GPTs/attachments/02_administration_operations.md
sed -n '650,710p' GPTs/attachments/03_sql_ddl_generation.md
sed -n '292,322p' GPTs/attachments/09_replication_ha_cdc.md
```

## Findings

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Blocker | `GPTs/attachments/07_error_messages_troubleshooting.md` | 1486 | The customer-facing attachment still exposes an internal build label: `JOB-042`. The same section is headed `## Conversion TODO` at line 1484 and refers to future deep-dive jobs, which is internal workflow language rather than upload-ready knowledge content. Gate 0 requires no internal labels or customer-facing forbidden strings before upload. | Remove the `Conversion TODO` section before upload, or rewrite it as customer-safe residual risk text with no job IDs, future job references, or internal workflow labels. |
| Note | `GPTs/attachments/*.md` | N/A | Upload file count passes. The directory contains exactly 20 numbered Markdown upload files plus `README.md`, and no non-Markdown files at max depth 1. | No count or directory-boundary change is needed for this stage. |
| Note | `GPTs/attachments/*.md` | N/A | Image independence passes at the upload-boundary level. Scans found no Markdown image links, HTML image tags, common image-extension references, `media/`, or `images/` references in attachments, and no image files under `GPTs/attachments/` to depth 2. | No separate image files are required for GPTs upload. Keep semantic checking of converted visuals in later stages. |
| Note | `GPTs/attachments/*.md` | N/A | Mermaid and text conversion markers are present. The live scan found 77 Mermaid blocks across diagram-heavy attachments, BNF-like syntax replacements in SQL/replication areas, procedural UI text in installation and NiFi areas, and no unmatched Markdown code fences. | Treat full source-image semantic fidelity as residual risk. R00 verified upload independence and conversion presence, not every relationship in the 3,513-image inventory. |

## Source Checks

- Claims checked: There should be exactly 20 upload Markdown attachments, no upload-required image files, no residual image references, no internal source labels or local source paths, and sufficient Mermaid/text conversion presence for GPTs upload.
- Source coverage: `attachment_count_validation.md` and the live `find` count both show 20 upload files. `forbidden_strings_validation.md` passed its targeted scan for `trunk`, `C:/`, and `file://`; this R00 scan broadened coverage to job/image IDs, source paths, repository labels, and absolute path candidates. `image_inventory.md` documents 3,513 source image references and the intended conversion classes; live scans found no remaining image dependency in upload attachments.
- Source gaps: This stage did not compare every Mermaid diagram, BNF block, procedural UI conversion, or text summary against the original source images. Later visual-fidelity review should sample or audit the highest-load files from `image_inventory.md`.

## Oracle-Overlap Decision

- Correctly compressed: Not evaluated in depth for R00.
- Too much generic Oracle material: Not evaluated in this stage.
- Missing Altibase-specific difference: Not evaluated in this stage.

## Version Checks

- 7.1: No 7.1-specific upload-boundary issue found.
- 7.3: No 7.3-specific upload-boundary issue found.
- 8.1: Direct scans found no customer-facing `trunk`, `Altibase_trunk`, `Manuals/Altibase`, or `ReleaseNotes/` source-path labels. The permitted customer-safe wording `Altibase 8.1 verified source` remains present.

## Retrieval And GPT Answer Quality

- Strengths: The attachment set has the expected 20-file upload boundary, no image-file dependency, no residual source-image links, and broad Mermaid/BNF/procedural conversion coverage.
- Risks: The `JOB-042` and `Future deep-dive jobs` text can leak internal workflow state into customer answers. The `/home/altibase/NiFi/nifi-1.12.1/lib` hits in `19_spatial_nifi_tableau_misc.md` are documented NiFi example values rather than workstation/source-tree paths, but later content review can decide whether placeholders would be clearer.

## Required Follow-Up

- Remove or customer-safely rewrite `GPTs/attachments/07_error_messages_troubleshooting.md:1484` through `GPTs/attachments/07_error_messages_troubleshooting.md:1486` before upload.
- Re-run a customer-safe string scan after cleanup that includes `JOB-[0-9]+`, `IMG-[0-9]+`, `Conversion TODO`, source-tree labels, local source paths, `trunk`, drive paths, and `file://`.
- Carry the residual visual-fidelity risk into later stages for diagram-heavy files, especially `02_administration_operations.md`, `08_performance_tuning_monitoring.md`, `09_replication_ha_cdc.md`, `16_dblink_external_connectors.md`, and `17_kubernetes_aku_cloud.md`.
