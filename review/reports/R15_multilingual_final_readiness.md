# R15 Multilingual Behavior and Final Upload Readiness

Date: 2026-05-16
Reviewer: Codex
Verdict: Pass

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
bash GPTs/scripts/remediation_plan.sh status
rg -n '\| (H|M|L|V0)[0-9]+ \| (ToDo|Progress|Fail) \|' review/remediation_plan.md || true
git status --short
```

## Findings

No multilingual-policy Blocker or High issue was found in the instruction draft, README, prompt set, or smoke results. The final-readiness gate is closed for report-blocking findings: H01-H16, M01-M22, L01-L10, V01, and V02 are `Done` in `review/remediation_plan.md`, and the referenced review reports no longer carry `Fail`, `Review Required`, Blocker, or High rows. V03 is this active closure row; V04 remains only a conditional residual-risk record task for any issue intentionally left unfixed by design.

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Resolved High | `review/reports/R01_strategy_source_policy.md`; `review/reports/R03_ddl_tablespace_storage.md`; `review/reports/R05_dml_oracle_compatibility.md`; `review/reports/R07_operations_admin_recovery.md`; `review/reports/R08_troubleshooting_errors.md`; `review/reports/R09_performance_monitoring.md`; `review/reports/R10_replication_ha_cdc_ssl.md`; `review/reports/R11_security_tls.md`; `review/reports/R12_development_interfaces.md`; `review/reports/R14_retrieval_visual_conversion.md` | 5 | The original gate finding was that detailed review reports still carried unresolved High rows. H01-H15 covered those High findings, and H16 closed the R15 High meta-gate after those prerequisites were `Done`. | No unresolved High task requires residual-risk acceptance. The final validation scan has no `Fail`, `Review Required`, Blocker, or High report findings. |
| Resolved Medium/Low | `review/remediation_plan.md` | 73 | The previous R15 version still described R06 Medium/Low follow-ups as remaining. Current plan evidence shows M01-M22 and L01-L10 are `Done`; V01 and V02 are also `Done`. | Treat the Medium/Low remediation debt as closed for this final-readiness pass. No attachment edit or residual-risk acceptance is required for a task left unfixed by design. |
| Note | `GPTs/reports/multilingual_smoke_results.md` | 16 | The multilingual smoke evidence is policy-sufficient but not exhaustive as a live-upload test. The source-reviewed list covers `00` and `02` through `16`; `17` is cited later in the Chinese startup prompt support, while `01`, `18`, and `19` are not listed in the report's reviewed-source list. | Optional post-upload prompts may still be run for installation, SSL/TLS, and Spatial/NiFi/Tableau topics before announcing production use. No attachment edits are required for this stage. |

## Source Checks

- Claims checked: final upload count; attachment list alignment; multilingual policy; literal token preservation; customer-safe 8.1 label use; unsafe source-label and local-path leakage; image-link leakage; required structural headings; prior QA pass evidence; current remediation-plan state; current review-report verdicts and report-blocking findings.
- Source coverage: the document selection maps all 20 final upload units to expected customer question areas (`GPTs/Altibase_GPT_Document_Selection.md:40`). The README repeats the 20-file upload list (`GPTs/attachments/README.md:40`) and pre-upload checks (`GPTs/attachments/README.md:122`).
- Source gaps: no source manuals were rechecked in this stage. The multilingual smoke test was a manual simulation, not a live GPT upload test (`GPTs/reports/multilingual_smoke_results.md:39`). No unresolved High, Medium, or Low task currently requires residual-risk acceptance for this gate.

## Oracle-Overlap Decision

- Correctly compressed: the final instruction draft tells the GPT to keep generic Oracle-compatible SQL brief and focus on Altibase-specific restrictions, storage choices, properties, and verification queries (`GPTs/GPT_Instructions_Draft.md:56`). The selection document assigns ordinary `SELECT`, `INSERT`, `UPDATE`, `DELETE`, basic joins, and basic predicates to compressed Oracle-compatible treatment while preserving detail for Altibase-specific DDL and operations (`GPTs/Altibase_GPT_Document_Selection.md:73`).
- Too much generic Oracle material: none found in this stage.
- Missing Altibase-specific difference: not re-audited in this stage; prior High, Medium, and Low remediation findings are closed through their own plan tasks.

## Version Checks

- 7.1: prior validation found 7.1 markers in all 20 attachments (`GPTs/reports/version_coverage_validation.md:43`).
- 7.3: prior validation found 7.3 markers in all 20 attachments (`GPTs/reports/version_coverage_validation.md:43`).
- 8.1: prior validation found 8.1 markers in all 20 attachments (`GPTs/reports/version_coverage_validation.md:43`), and this stage rechecked that all 20 upload attachments contain `Altibase 8.1 verified source`.
- Readiness caveat: marker coverage is not the same as source re-audit. This stage relies on the completed remediation plan and review-report closure evidence rather than rechecking every manual citation.

## Retrieval And GPT Answer Quality

- Strengths: the global instruction draft requires same-language answers, explicit response-language override handling, exact preservation of technical tokens, and no translation or localization of SQL object names, SQL syntax, functions, error codes, properties, commands, paths, APIs, connectors, or version labels (`GPTs/GPT_Instructions_Draft.md:22`). The attachment README repeats the multilingual literal-token policy (`GPTs/attachments/README.md:21`).
- Strengths: the multilingual prompt set has 18 prompts across Vietnamese, Turkish, Persian, Hindi, Chinese, Japanese, English/French override, German, and French (`GPTs/reports/multilingual_prompt_set.md:5`, `GPTs/reports/multilingual_prompt_set.md:288`). The smoke result reports 18 pass, 0 fail, 0 review-needed (`GPTs/reports/multilingual_smoke_results.md:57`) and spot-checks preserved tokens including `V$PROPERTY`, `REPLICATION_SSL_PORT_NO`, `TEMPORARY_LOB_ENABLE`, `$ALTIBASE_HOME/trc`, `PreparedStatement`, `SQLConnect`, `VARCHAR2`, `NUMBER`, and `SYSDATE` (`GPTs/reports/multilingual_smoke_results.md:403`).
- Strengths: the final upload boundary is clean. Prior QA and this stage both found exactly 20 upload Markdown files excluding `README.md`, and prior QA found no `trunk`, `C:/`, or `file://` leakage (`GPTs/reports/attachment_count_validation.md:14`).
- Risks: multilingual behavior still depends on GPT runtime adherence to the instruction draft after upload. The remaining risk is runtime/live-upload behavior, not an open remediation-plan finding.

## Required Follow-Up

- If any attachment or instruction file changes after this report, re-run the lightweight final checks: attachment count, unsafe-label scan, image-link scan, required heading scan, 8.1 label scan, multilingual smoke or live prompts, and review-report verdict scan.
- Use V04 only if maintainers intentionally leave a remediation task unfixed by design and need an explicit residual-risk record.
- Optional post-upload validation: run one live GPT prompt each for installation/package naming, SSL/TLS client/server vs replication SSL separation, and Spatial/NiFi/Tableau literal-token preservation.
