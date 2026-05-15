# R15 Multilingual Behavior and Final Upload Readiness

Date: 2026-05-15
Reviewer: Codex
Verdict: Review Required

## Scope

- Attachments: `GPTs/GPT_Instructions_Draft.md`; `GPTs/attachments/README.md`; all 20 upload Markdown attachments under `GPTs/attachments/`, excluding `README.md`; `GPTs/reports/multilingual_prompt_set.md`; `GPTs/reports/multilingual_smoke_results.md`.
- Supporting reports: `GPTs/reports/attachment_count_validation.md`; `GPTs/reports/english_consistency_validation.md`; `GPTs/reports/version_coverage_validation.md`.
- Source manuals sampled: none. This stage checked final package behavior and prior validation evidence, not source-manual fidelity.

## Commands Run

```bash
sed -n '1,240p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,220p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,240p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
sed -n '1,260p' GPTs/GPT_Instructions_Draft.md
sed -n '1,260p' GPTs/reports/multilingual_prompt_set.md
sed -n '260,560p' GPTs/reports/multilingual_prompt_set.md
sed -n '1,280p' GPTs/reports/multilingual_smoke_results.md
sed -n '280,620p' GPTs/reports/multilingual_smoke_results.md
sed -n '1,220p' GPTs/reports/attachment_count_validation.md
sed -n '1,240p' GPTs/reports/english_consistency_validation.md
sed -n '1,260p' GPTs/reports/version_coverage_validation.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' | sort | wc -l
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' | sort
rg -n 'trunk|file://|C:/|C:\\|/home/et16|/Users/|Manuals/Altibase|ReleaseNotes/kor|Altibase_trunk' GPTs/attachments GPTs/GPT_Instructions_Draft.md || true
rg -n '!\[[^]]*\]\([^)]*\.(png|jpg|jpeg|gif|svg|webp)\)|<img|https?://[^ )]+\.(png|jpg|jpeg|gif|svg|webp)|[^[:space:]]+\.(png|jpg|jpeg|gif|svg|webp)' GPTs/attachments/*.md GPTs/GPT_Instructions_Draft.md || true
rg -n "TODO|TBD|FIXME|Conversion TODO|Review needed|placeholder|unresolved|unknown" GPTs/attachments/*.md GPTs/GPT_Instructions_Draft.md || true
for h in "Applicable Versions" "Questions This File Can Answer" "Source Documents"; do printf '%s\n' "$h"; find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' -exec rg --files-without-match "^## $h$" {} + || true; done
rg -n -P "[\p{Hangul}\p{Han}\p{Hiragana}\p{Katakana}\p{Arabic}\p{Devanagari}]" GPTs/attachments/*.md GPTs/GPT_Instructions_Draft.md || true
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' -exec rg -l "Altibase 8\.1 verified source" {} + | sort | wc -l
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' -exec rg --files-without-match "Altibase 8\.1 verified source" {} + || true
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' -exec rg --files-without-match "Keep .*literal|keep .*literal|Preserve .*literal|preserving .*literally|Do not translate" {} + || true
rg -n 'Attachment support:|GPTs/attachments/[0-9][0-9]_' GPTs/reports/multilingual_smoke_results.md
rg -n 'Verdict: (Fail|Review Required)|^\| (Blocker|High) \|' review/reports/R*.md || true
rg -n '^Verdict:' review/reports/R*.md || true
git status --short
```

## Findings

No multilingual-policy Blocker or High issue was found in the instruction draft, README, prompt set, or smoke results. The final upload gate is still Review Required because current review reports contain unresolved High findings and no acceptance record was found.

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| High | `review/reports/R01_strategy_source_policy.md`; `review/reports/R03_ddl_tablespace_storage.md`; `review/reports/R05_dml_oracle_compatibility.md`; `review/reports/R07_operations_admin_recovery.md`; `review/reports/R08_troubleshooting_errors.md`; `review/reports/R09_performance_monitoring.md`; `review/reports/R10_replication_ha_cdc_ssl.md`; `review/reports/R11_security_tls.md`; `review/reports/R12_development_interfaces.md`; `review/reports/R14_retrieval_visual_conversion.md` | 5 | Current review artifacts still have `Verdict: Review Required` and unresolved High rows. Gate 5 requires remaining review reports to be resolved or explicitly accepted as residual risk before final upload readiness can pass. | Do not upload as final-ready until each High finding in those reports is fixed and re-reviewed, or explicitly accepted in a final residual-risk record. Keep the multilingual policy artifacts as-is unless a follow-up live test shows a language-specific issue. |
| Medium | `review/reports/R06_properties_dictionary_checks.md` | 5 | `R06` also remains `Review Required` with Medium/Low findings around LOB autocommit version scope and customer-facing "sampled source" wording. These are not multilingual failures, but they remain unresolved package-readiness items. | Resolve the two R06 follow-ups or explicitly accept them as residual risk before upload sign-off. |
| Note | `GPTs/reports/multilingual_smoke_results.md` | 16 | The multilingual smoke evidence is policy-sufficient but not exhaustive as a live-upload test. The source-reviewed list covers `00` and `02` through `16`; `17` is cited later in the Chinese startup prompt support, while `01`, `18`, and `19` are not listed in the report's reviewed-source list. | Accept as residual risk for upload readiness, or run optional post-upload prompts for installation, SSL/TLS, and Spatial/NiFi/Tableau topics before announcing production use. No attachment edits are required for this stage. |

## Source Checks

- Claims checked: final upload count; attachment list alignment; multilingual policy; literal token preservation; customer-safe 8.1 label use; unsafe source-label and local-path leakage; image-link leakage; required structural headings; prior QA pass evidence; current review-report verdicts and High findings.
- Source coverage: the document selection maps all 20 final upload units to expected customer question areas (`GPTs/Altibase_GPT_Document_Selection.md:40`). The README repeats the 20-file upload list (`GPTs/attachments/README.md:40`) and pre-upload checks (`GPTs/attachments/README.md:122`).
- Source gaps: no source manuals were rechecked in this stage. The multilingual smoke test was a manual simulation, not a live GPT upload test (`GPTs/reports/multilingual_smoke_results.md:39`). No explicit acceptance record was found for the current `Review Required` reports.

## Oracle-Overlap Decision

- Correctly compressed: the final instruction draft tells the GPT to keep generic Oracle-compatible SQL brief and focus on Altibase-specific restrictions, storage choices, properties, and verification queries (`GPTs/GPT_Instructions_Draft.md:56`). The selection document assigns ordinary `SELECT`, `INSERT`, `UPDATE`, `DELETE`, basic joins, and basic predicates to compressed Oracle-compatible treatment while preserving detail for Altibase-specific DDL and operations (`GPTs/Altibase_GPT_Document_Selection.md:73`).
- Too much generic Oracle material: none found in this stage.
- Missing Altibase-specific difference: not re-audited in this stage; current review reports still list unresolved High differences that must be resolved or accepted before final upload sign-off.

## Version Checks

- 7.1: prior validation found 7.1 markers in all 20 attachments (`GPTs/reports/version_coverage_validation.md:43`).
- 7.3: prior validation found 7.3 markers in all 20 attachments (`GPTs/reports/version_coverage_validation.md:43`).
- 8.1: prior validation found 8.1 markers in all 20 attachments (`GPTs/reports/version_coverage_validation.md:43`), and this stage rechecked that all 20 upload attachments contain `Altibase 8.1 verified source`.
- Readiness caveat: marker coverage is not the same as issue closure. Current detailed review reports still contain unresolved High version/correctness findings.

## Retrieval And GPT Answer Quality

- Strengths: the global instruction draft requires same-language answers, explicit response-language override handling, exact preservation of technical tokens, and no translation or localization of SQL object names, SQL syntax, functions, error codes, properties, commands, paths, APIs, connectors, or version labels (`GPTs/GPT_Instructions_Draft.md:22`). The attachment README repeats the multilingual literal-token policy (`GPTs/attachments/README.md:21`).
- Strengths: the multilingual prompt set has 18 prompts across Vietnamese, Turkish, Persian, Hindi, Chinese, Japanese, English/French override, German, and French (`GPTs/reports/multilingual_prompt_set.md:5`, `GPTs/reports/multilingual_prompt_set.md:288`). The smoke result reports 18 pass, 0 fail, 0 review-needed (`GPTs/reports/multilingual_smoke_results.md:57`) and spot-checks preserved tokens including `V$PROPERTY`, `REPLICATION_SSL_PORT_NO`, `TEMPORARY_LOB_ENABLE`, `$ALTIBASE_HOME/trc`, `PreparedStatement`, `SQLConnect`, `VARCHAR2`, `NUMBER`, and `SYSDATE` (`GPTs/reports/multilingual_smoke_results.md:403`).
- Strengths: the final upload boundary is clean. Prior QA and this stage both found exactly 20 upload Markdown files excluding `README.md`, and prior QA found no `trunk`, `C:/`, or `file://` leakage (`GPTs/reports/attachment_count_validation.md:14`).
- Risks: multilingual behavior still depends on GPT runtime adherence to the instruction draft after upload. More importantly, final package upload readiness is not yet satisfied because unresolved High findings remain in current review reports.

## Required Follow-Up

- Resolve or explicitly accept all current `Review Required` reports, especially High findings in R01, R03, R05, R07, R08, R09, R10, R11, R12, and R14.
- Resolve or explicitly accept the Medium/Low R06 findings.
- After issue closure or acceptance, re-run the lightweight final checks: attachment count, unsafe-label scan, image-link scan, required heading scan, 8.1 label scan, multilingual smoke or live prompts, and review-report verdict scan.
- Optional post-upload validation: run one live GPT prompt each for installation/package naming, SSL/TLS client/server vs replication SSL separation, and Spatial/NiFi/Tableau literal-token preservation.
