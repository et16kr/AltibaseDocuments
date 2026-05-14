# R15 Multilingual Behavior and Final Upload Readiness

Date: 2026-05-14
Reviewer: Codex
Verdict: Fail

## Scope

- Attachments: `GPTs/GPT_Instructions_Draft.md`; `GPTs/attachments/README.md`; all 20 upload Markdown files under `GPTs/attachments/`; `GPTs/reports/multilingual_prompt_set.md`; `GPTs/reports/multilingual_smoke_results.md`.
- Supporting reports: `GPTs/reports/attachment_count_validation.md`; `GPTs/reports/english_consistency_validation.md`; `GPTs/reports/version_coverage_validation.md`; prior review reports `review/reports/R00_*.md` through `review/reports/R14_*.md`.
- Source manuals sampled: none directly in this final readiness stage. Source-backed risk assessment is inherited from the prior detailed review reports and checked against the current attachment text.

## Commands Run

```bash
sed -n '1,220p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,260p' GPTs/GPT_Instructions_Draft.md
sed -n '1,320p' GPTs/reports/multilingual_smoke_results.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' | sort | wc -l
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' | sort
rg -n "trunk|C:/|file://|JOB-[0-9]+|Conversion TODO" GPTs/attachments --glob '*.md' || true
rg -n "!\[[^\]]*\]\(|\.(png|jpg|jpeg|gif|svg|webp|bmp)\b|media/" GPTs/attachments --glob '*.md' || true
for f in GPTs/attachments/*.md; do [ "$(basename "$f")" = README.md ] && continue; printf '%s|' "$(basename "$f")"; for h in "Applicable Versions" "Questions This File Can Answer" "Source Documents"; do if rg -q "^## $h" "$f"; then printf ' %s:yes' "$(printf '%s' "$h" | tr ' ' '_')"; else printf ' %s:no' "$(printf '%s' "$h" | tr ' ' '_')"; fi; done; printf '\n'; done
rg -n '^\| (Blocker|High) \|' review/reports/R*.md
rg -n "JOB-042|Conversion TODO|sub-millisecond|built-in conflict|ShardManager|CREATE \[LAZY \| EAGER\] REPLICATION|FOR ANALYSIS|IF NOT EXISTS|IF EXISTS|VARIABLE \( IN ROW|PSM_CASE_SENSITIVE_MODE|REGEXP_MODE|checkpoint_scale|10000103|10000201|publishNotReadyAddress|DROP USER ldap CASCADE|SQLGetLob\(\)|SQLPutLob\(\)|fromPosition" GPTs/attachments/*.md
nl -ba GPTs/attachments/07_error_messages_troubleshooting.md | sed -n '740,790p;970,1005p;1240,1270p;1478,1492p'
nl -ba GPTs/attachments/09_replication_ha_cdc.md | sed -n '1,35p;292,315p;808,850p'
nl -ba GPTs/attachments/03_sql_ddl_generation.md | sed -n '24,38p;566,585p;1808,1835p'
nl -ba GPTs/attachments/12_c_cli_odbc_precompiler.md | sed -n '925,960p'
nl -ba GPTs/attachments/14_utilities_operation_tools.md | sed -n '565,580p'
nl -ba GPTs/attachments/16_dblink_external_connectors.md | sed -n '1408,1422p'
```

## Findings

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Blocker | `GPTs/attachments/07_error_messages_troubleshooting.md` | 1484 | The customer-facing upload attachment still contains `## Conversion TODO` and exposes the internal workflow label `JOB-042`. This violates the source-safety and upload-boundary policy and was already reported as a Blocker in R00/R01. | Remove the `Conversion TODO` section from the upload attachment, or rewrite it as customer-safe residual scope text with no job IDs, future job references, or internal workflow labels. Re-run the forbidden/internal label scan before upload. |
| High | `review/reports/R00_upload_boundary.md`; `review/reports/R01_strategy_source_policy.md`; `review/reports/R03_ddl_tablespace_storage.md`; `review/reports/R04_table_index_constraint_ddl.md`; `review/reports/R06_properties_dictionary_checks.md`; `review/reports/R07_operations_admin_recovery.md`; `review/reports/R08_troubleshooting_errors.md`; `review/reports/R09_performance_monitoring.md`; `review/reports/R10_replication_ha_cdc_ssl.md`; `review/reports/R12_development_interfaces.md`; `review/reports/R13_tools_migration_connectors.md` | mixed | Gate 5 requires remaining review reports to be resolved or explicitly accepted as residual risk. The current review set still includes `Fail` and `Review Required` verdicts with unresolved Blocker/High findings, and no acceptance record was found. | Do not upload until each Blocker/High finding is fixed, re-reviewed, or formally accepted as residual risk in a final readiness note. |
| High | `GPTs/attachments/09_replication_ha_cdc.md` | 20 | The Active-Active overview still claims replication "guarantees sub-millisecond latency and built-in conflict resolution." Prior source-backed reports found this unsupported and unsafe for HA guidance. | Replace with conservative wording: Altibase supports replication modes/topologies, but latency depends on workload and network, and Active-Active requires explicit conflict avoidance, ownership, and monitoring. |
| High | `GPTs/attachments/09_replication_ha_cdc.md` | 21 | Sharding/ShardManager scale-out guidance remains in the replication attachment even though prior review found it outside the selected source family for this file. Retrieval can over-answer sharding setup questions without source support. | Remove the sharding overview from this attachment, or restrict it to a customer-safe note that sharding setup requires a separate selected source audit. |
| High | `GPTs/attachments/03_sql_ddl_generation.md`; `GPTs/attachments/09_replication_ha_cdc.md` | 577; 303 | The compact replication grammar still combines `[LAZY | EAGER]` with `FOR ANALYSIS`, which prior source checks found can lead to invalid Log Analyzer SQL such as `CREATE EAGER REPLICATION ... FOR ANALYSIS`. | Split ordinary table replication syntax from Log Analyzer CDC syntax. State near the grammar that `FOR ANALYSIS` is not an EAGER table-replication form. |
| High | `GPTs/attachments/09_replication_ha_cdc.md` | 819 | The "Standard DDL procedure" still mixes property-based SQL apply guidance with a simplified "execute same DDL on both nodes" flow and omits the safer no-special-property procedure noted in R10. | Split standard DDL and DDL synchronization procedures, including service/admin prerequisites, `REP_GAP=0` verification, stopping replication, target drop/add, property sequence, restrictions, and restoration steps. |
| High | `GPTs/attachments/03_sql_ddl_generation.md` | 1819 | The two-node replication example still runs `ALTER REPLICATION ... SYNC` inside each node's setup block before showing both peer objects created. This can be copied into an invalid or unsafe initialization sequence. | Move `SYNC`/`START` after both matching `CREATE REPLICATION` statements and state that sync direction depends on Active-Standby versus Active-Active ownership and existing data. |
| High | `GPTs/attachments/01_getting_started_installation.md` | 60, 380 | The 8.1 platform baseline still omits AIX 7.2 server/client support, while the version/platform attachment and prior review cite it for 8.1. | Add AIX 7.2 to both 8.1 installation/platform statements or explicitly scope this file to a Linux quick path and route platform decisions to file 00. |
| High | `GPTs/attachments/02_administration_operations.md` | 162 | A common DBA query still selects `checkpoint_scale` from `V$LOG`, even though prior review found it is 8.1-only in the sampled dictionaries. A 7.1/7.3 answer can generate a failing query. | Remove `checkpoint_scale` from the common query and add a separate 8.1-only query guarded by version wording or a `V$ALLCOLUMN` column check. |
| High | `GPTs/attachments/07_error_messages_troubleshooting.md` | 759, 983, 1255 | Previously reported troubleshooting gaps remain: the "not found" block lacks branch-specific column/index/replication checks, the PCRE2 block under-escalates unexpected PCRE2 failures, and duplicate-replication diagnostics still use runtime views as primary checks. | Add branch-specific dictionary checks, split or branch PCRE2 errors, and use replication meta tables as the primary duplicate-replication diagnostic. |
| High | `GPTs/attachments/05_data_types_properties.md` | 39, 1978 | `PSM_CASE_SENSITIVE_MODE` and `REGEXP_MODE` are still represented as 8.1-new or 8.1-only even though prior review found 7.x source evidence. This can make multilingual answers preserve the token but give the wrong version scope. | Reclassify these as cross-version or source-audit-required properties and add version-specific caveats instead of implying 8.1-only availability. |
| High | `GPTs/attachments/12_c_cli_odbc_precompiler.md` | 936, 947 | `SQLGetLob()` and `SQLPutLob()` `fromPosition` guidance still omits the formal 1-based rule reported in R12 and emphasizes `0` examples, risking off-by-one generated C code. | State the formal API position base by function: `SQLGetLob()` and `SQLPutLob()` begin at `1`; `SQLTrimLob()` begins at `0`. Isolate any sample-specific `0` convention as a tested exception. |
| High | `GPTs/attachments/08_performance_tuning_monitoring.md` | 2147 | The SNMP trap block still asserts `10000103` for continuous session failure despite prior source conflict between `10000201` and example output. | Do not assert one code until confirmed; state the ambiguity and require target-version validation with actual `snmptrapd` output before alert-rule configuration. |
| High | `GPTs/attachments/14_utilities_operation_tools.md`; `GPTs/attachments/16_dblink_external_connectors.md` | 574; 1416 | The current package still has the AKU/Kubernetes field typo `publishNotReadyAddress` and an OpenLDAP example containing `DROP USER ldap CASCADE;` without a clear test-only gate. These remain upload risks for tool behavior and destructive SQL. | Correct the Kubernetes field to `publishNotReadyAddresses: true`. Remove the destructive OpenLDAP reset or isolate it as an explicit lab-only reset with impact warning. |
| Medium | `GPTs/attachments/00_version_release_platform.md` | 104-110 | Several 8.1 feature families are release-summarized (`KADA`, Kafka connectors, `abm`, MindsDB, `.NET 8`/EF Core, `node-odbc-altibase`) but prior review found limited procedural depth elsewhere. Retrieval can mention these but may not support implementation answers. | Either scope these as release-note-only topics that require product documentation for procedures, or add concise source-backed blocks to the relevant API/tool/connector attachments. |

## Source Checks

- Claims checked: multilingual answer policy wording, literal-token preservation policy, final upload count, attachment structure markers, image/reference cleanup, internal label leakage, prior Blocker/High review status, and current attachment text for representative unresolved risks.
- Source coverage: multilingual behavior is supported by `GPTs/attachments/README.md` lines 21-38, `GPTs/GPT_Instructions_Draft.md` lines 22-38, the 18-prompt prompt set, and the smoke test summary showing 18 passes across 9 language cases.
- Source gaps: no live GPT run, no live Altibase server, and no new direct source manual audit were performed in R15. The correctness risks above rely on prior source-backed detailed review reports and current attachment confirmation.

## Oracle-Overlap Decision

- Correctly compressed: ordinary DML/Oracle-overlap handling remains supported by the prior R05 Pass and the instruction policy to keep generic Oracle-compatible SQL brief.
- Too much generic Oracle material: none newly identified by this stage.
- Missing Altibase-specific difference: final upload readiness is blocked by unresolved Altibase-specific differences in replication, properties, views, platform support, LOB APIs, SNMP traps, and tool behavior.

## Version Checks

- 7.1: Version marker coverage exists in all 20 attachments, but unresolved risks can produce wrong 7.1 answers for `IF EXISTS`/`IF NOT EXISTS`, common `V$LOG` checks, `REGEXP_MODE`, and LOB API positions.
- 7.3: Version marker coverage exists in all 20 attachments, but the same unresolved risks apply to 7.3 operational and API answers.
- 8.1: Version marker coverage exists and multilingual token policy preserves `Altibase 8.1 verified source`, but unresolved 8.1 risks remain for platform support, JSON/LOB property scope, replication SSL/DDL guidance, and release-note-only feature depth.

## Retrieval And GPT Answer Quality

- Strengths: the answer-language policy is explicit; the prompt set covers Vietnamese, Turkish, Persian, Hindi, Chinese, Japanese, English/French override, German, and French; the smoke result reports 18/18 pass with literal preservation of SQL names, properties, paths, commands, APIs, error codes, and version labels. The current attachment package has exactly 20 upload files, no image references were found, and all 20 files have `Applicable Versions`, `Questions This File Can Answer`, and `Source Documents` headings.
- Risks: final upload is not ready because retrieval can still surface the internal `JOB-042` note and multiple high-impact incorrect operational, replication, property, API, and tool statements. These issues affect multilingual answers because token preservation does not prevent the GPT from giving wrong source-backed behavior around the preserved tokens.

## Required Follow-Up

- Remove or rewrite the `Conversion TODO` / `JOB-042` section in `07_error_messages_troubleshooting.md`.
- Resolve or formally accept every remaining Blocker/High finding from R00-R14 before upload.
- Fix the current high-risk attachment content confirmed in R15: replication guarantees/sharding, replication grammar and DDL procedures, 8.1 platform baseline, common `V$LOG` query, troubleshooting diagnostics, property version scope, LOB API positions, SNMP trap ambiguity, AKU field typo, and destructive OpenLDAP reset.
- Re-run the lightweight final checks: attachment count, internal-label scan, image-reference scan, section-marker scan, multilingual prompt smoke, and high/blocker review-status scan.
