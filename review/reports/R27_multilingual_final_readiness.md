# R27 Multilingual Behavior and Final Upload Readiness

Date: 2026-05-16
Reviewer: Codex
Verdict: Pass

## Scope

- Attachments: `GPTs/GPT_Instructions_Draft.md`; `GPTs/attachments/*.md`; `GPTs/reports/multilingual_prompt_set.md`; `GPTs/reports/multilingual_smoke_results.md`
- Supporting reports: `GPTs/reports/attachment_count_validation.md`; `GPTs/reports/english_consistency_validation.md`; `GPTs/reports/version_coverage_validation.md`; `GPTs/reports/source_inventory.md`; `GPTs/reports/eng_kor_parity.md`; `GPTs/reports/8_1_verification.md`; prior review reports `R00` through `R26`
- Source manuals sampled: No new line-by-line manual source audit was performed in R27. This final readiness review checked the Korean-source precedence policy through `GPTs/GPT_Instructions_Draft.md`, the attachment README, the source inventory, the English/Korean parity report, the 8.1 verification report, and prior source-audit review reports.

## Commands Run

```bash
bash review/scripts/run_review_remediation_cycle.sh status
rg -n $'\t(Reviewing|Remediating|ReReviewing|Fail)$' review/review_remediation_cycle_status.tsv
git status --short
ls -l review/reports/R27_multilingual_final_readiness.md
git diff -- review/review_remediation_cycle_status.tsv
git diff -- review/review_stage_status.tsv
sed -n '1,240p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,260p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,280p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
sed -n '1,260p' GPTs/GPT_Instructions_Draft.md
sed -n '1,260p' GPTs/reports/multilingual_prompt_set.md
sed -n '1,300p' GPTs/reports/multilingual_smoke_results.md
sed -n '1,220p' GPTs/reports/attachment_count_validation.md
sed -n '1,260p' GPTs/reports/english_consistency_validation.md
sed -n '1,320p' GPTs/reports/version_coverage_validation.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' | sort
rg -n "Korean|English|source authority|source of truth|authoritative|translated|multilingual|literal|untranslated|Altibase 8\.1 verified source|trunk|C:/|file://" GPTs/attachments GPTs/GPT_Instructions_Draft.md GPTs/reports/multilingual_prompt_set.md GPTs/reports/multilingual_smoke_results.md
rg -n -P "[\p{Hangul}\p{Han}\p{Hiragana}\p{Katakana}\p{Arabic}\p{Devanagari}]" GPTs/attachments --glob '*.md'
rg -n "TODO|FIXME|TBD|Residual Scope Notes|unsupported|missing|not covered|source gap|Review Required|Fail" GPTs/attachments GPTs/GPT_Instructions_Draft.md GPTs/reports/multilingual_smoke_results.md
rg -n "local filesystem|workstation|repository|branch|internal|source labels|build labels|customer-safe|verified source" GPTs/attachments GPTs/GPT_Instructions_Draft.md
nl -ba GPTs/attachments/README.md | sed -n '1,145p'
nl -ba GPTs/GPT_Instructions_Draft.md | sed -n '1,95p'
nl -ba GPTs/reports/multilingual_prompt_set.md | sed -n '1,335p'
nl -ba GPTs/reports/multilingual_smoke_results.md | sed -n '1,450p'
nl -ba GPTs/Altibase_GPT_Document_Selection.md | sed -n '1,155p'
nl -ba GPTs/Altibase_GPT_Attachment_Build_Workplan.md | sed -n '1,240p'
nl -ba GPTs/reports/attachment_count_validation.md | sed -n '1,90p'
nl -ba GPTs/reports/version_coverage_validation.md | sed -n '1,150p'
rg -n "^Verdict:|^\| (Blocker|High|Medium|Low) \|" review/reports/R*.md
find review/reports -maxdepth 1 -type f -name 'R*.md' | sort
bash review/scripts/run_review_stage.sh validate
sed -n '1,220p' review/reports/R26_retrieval_visual_conversion.md
sed -n '1,180p' review/reports/R02_high_risk_traceability.md
sed -n '1,180p' review/reports/R01_strategy_source_policy.md
sed -n '1,180p' review/reports/R00_upload_boundary.md
nl -ba GPTs/reports/eng_kor_parity.md | sed -n '1,125p'
nl -ba GPTs/reports/8_1_verification.md | sed -n '1,120p'
nl -ba GPTs/reports/source_inventory.md | sed -n '1,95p'
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' | wc -l
rg -n "trunk|C:/|file://|/home/et16|Manuals/Altibase|ReleaseNotes/|Technical Documents/|3rd Party Guide for Altibase" GPTs/attachments || true
rg -n -P "[\p{Hangul}\p{Han}\p{Hiragana}\p{Katakana}]" GPTs/attachments --glob '*.md' || true
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' -exec rg --files-without-match "Altibase 8\.1 verified source" {} + || true
for f in GPTs/attachments/[0-9][0-9]_*.md; do for h in '## Applicable Versions' '## Source Documents' '## Questions This File Can Answer'; do rg -q "^$h$" "$f" || printf '%s missing %s\n' "$f" "$h"; done; done
rg -n "^Verdict: (Review Required|Fail)|^\| (Blocker|High|Medium|Low) \|" review/reports/R*.md
rg -n 'Answer in the user.s language|Keep .*literal|Do not expose internal source labels|For 8\.1-specific statements, say `Altibase 8\.1 verified source`|Use the wording `Altibase 8\.1 verified source`' GPTs/attachments/[0-9][0-9]_*.md
```

## Findings

No actionable Blocker, High, Medium, or Low findings were found. The multilingual policy, Korean-source precedence policy, and final package behavior are upload-ready for the 20 Markdown attachment set.

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |

## Source Checks

- Claims checked: multilingual answer policy; literal preservation for SQL object names, SQL keywords, function names, error codes, property names, commands, paths, API names, connector names, and version labels; Korean-source precedence when Korean and English manuals differ; customer-safe 8.1 source labels; final attachment count and upload package readiness.
- Source coverage: `GPTs/GPT_Instructions_Draft.md:19`-`:23` tells the GPT to use Korean manuals as the source authority when Korean and English manuals differ, explain the Korean-manual basis if asked, and avoid unsafe answers when attachments lack enough information. `GPTs/reports/source_inventory.md:7`-`:22` records Korean roots as authoritative across 7.1, 7.3, 8.1, release notes, tool manuals, technical documents, and third-party guides.
- Korean/English source conflicts: The English/Korean parity report explicitly keeps Korean manuals authoritative and final attachments English-normalized (`GPTs/reports/eng_kor_parity.md:9`-`:15`). Known 8.1 Korean-source detail cases are registered for JSON, Temporary LOB, replication SSL, JSON errors, CLI JSON LOB cleanup, and JSON plan limits (`GPTs/reports/eng_kor_parity.md:58`-`:70`), and prior R02 source audit reports them handled without remaining actionable findings.
- Source gaps: JSON-formatted execution plan remains release-note-only. The gap is already explicit in `GPTs/reports/8_1_verification.md:81`-`:87`, and prior review carried it forward as a residual risk to avoid inventing JSON plan schema, values, or examples.

## Oracle-Overlap Decision

- Correctly compressed: The selection document keeps generic Oracle-overlapping SQL brief and reserves detail for Altibase-specific DDL, storage, properties, operations, troubleshooting, replication, HA, performance, security, and tool behavior (`GPTs/Altibase_GPT_Document_Selection.md:8`-`:11`, `:68`-`:82`).
- Too much generic Oracle material: No final-readiness issue was found. Prior R00-R26 reports are `Verdict: Pass`, and the R27 unresolved-finding scan found no `Review Required`, `Fail`, `Blocker`, `High`, `Medium`, or `Low` rows.
- Missing Altibase-specific difference: No new R27 gap was identified. The final file map covers all expected customer question areas through the 20-file selection matrix (`GPTs/Altibase_GPT_Document_Selection.md:40`-`:66`).

## Version Checks

- 7.1: Version coverage validation passed for all 20 attachments, and the automated marker check found 7.1 coverage in every file (`GPTs/reports/version_coverage_validation.md:43`-`:64`).
- 7.3: Version coverage validation passed for all 20 attachments, and the automated marker check found 7.3 coverage in every file (`GPTs/reports/version_coverage_validation.md:43`-`:64`).
- 8.1: Version coverage validation passed for all 20 attachments, customer-facing 8.1 wording uses `Altibase 8.1 verified source`, and the R27 scan found no attachment missing that customer-safe label. The attachment count remains exactly 20 excluding `README.md`.

## Retrieval And GPT Answer Quality

- Strengths: `GPTs/attachments/README.md:21`-`:38` defines the multilingual answer policy and literal token preservation rule. `GPTs/GPT_Instructions_Draft.md:25`-`:41` repeats the answer-language rule and enumerates literal tokens, while `:43`-`:57` preserves user-provided SQL object names and documented dictionary/performance object names exactly. The multilingual prompt set covers 18 prompts across nine language/override categories and requires token preservation, version clarification, customer-safe 8.1 labels, and unsupported-claim avoidance (`GPTs/reports/multilingual_prompt_set.md:17`-`:32`, `:288`-`:300`). The multilingual smoke test passed all 18 prompts with zero failures (`GPTs/reports/multilingual_smoke_results.md:57`-`:65`) and spot-checked preservation of representative SQL, property, command, path, API, connector, and version tokens (`GPTs/reports/multilingual_smoke_results.md:403`-`:417`).
- Risks: Multilingual smoke results were manual Codex prompt simulations, not a live test against an uploaded GPT (`GPTs/reports/multilingual_smoke_results.md:39`-`:42`). The prompt set covers major customer languages but does not exhaust every locale or code-switching case. These are accepted residual risks because the GPT instructions, README policy, per-attachment literal-token reminders, and smoke results all align, and no actionable final package defect was found.

## Required Follow-Up

- No R27 remediation is required.
- Before actual GPT upload, run the normal final operational checklist outside the attachment files: upload exactly the 20 Markdown files listed in `GPTs/attachments/README.md:40`-`:61`, apply the current `GPTs/GPT_Instructions_Draft.md` as the GPT instruction basis, and do one live multilingual smoke check after upload to confirm platform retrieval behavior matches the staged simulations.
