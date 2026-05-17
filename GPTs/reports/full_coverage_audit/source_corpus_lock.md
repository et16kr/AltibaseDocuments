# Full Coverage Audit Source Corpus Lock

- Workflow: `altibase-gpt-full-coverage-audit`
- Audit jobs: `FCA-J001`, `FCA-J002`
- Job title: Preflight, benchmark evidence, and source corpus lock
- Status: Latest benchmark baseline and selected source corpus are locked; item-level
  catalog extraction remains assigned to later FCA jobs
- Date: 2026-05-18

## FCA-J001 Scope

`FCA-J001` confirms that the staged review/remediation cycle is complete, that no
project files outside workflow runtime/status files were dirty before this job edited
the repository, and that the latest full benchmark run is locked as failure evidence
for the stricter full coverage audit.

This job does not catalog source items, remediate attachment content, broaden source
scope, edit original manuals, or change customer-facing GPT instructions. Later jobs
must still prove item-level source-to-attachment coverage from repository-local
selected sources.

## FCA-J002 Scope

`FCA-J002` freezes the selected repository-local source roots, source family IDs,
authority order, extraction-aid role, exclusions, and customer-facing scope boundaries
for the full coverage audit.

This job does not catalog individual source items, add source-to-attachment matrix rows,
remediate attachments, edit GPT instructions, edit original manuals, rerun the live
benchmark, or change the 20-file upload package. Later FCA catalog jobs must still
create row-level dispositions in `source_item_catalog.tsv` and later matrix/register
jobs must prove each row as `Covered`, `Covered-by-routing`, `Guardrail`,
`Out-of-scope`, `Missing`, or `Retrieval-weak`.

## Job Boundary Evidence

The job boundary was reconfirmed from:

- `.codex-jobs/altibase-gpt-full-coverage-audit/jobs.tsv`: `FCA-J001` was the only
  `Progress` job, with goal "Confirm the current review/remediation cycle is complete,
  the worktree is clean, previous jobs are committed, and the latest full benchmark run
  is locked as audit evidence."
- `.codex-jobs/altibase-gpt-full-coverage-audit/jobs.md`: `FCA-J001` targets current
  workflow status, latest benchmark, and existing reports, with expected durable output
  "Preflight evidence section and locked latest-run baseline."
- `.codex-jobs/altibase-gpt-full-coverage-audit/requirements.md`: the latest run below
  is failure evidence only, not the full audit scope.

For `FCA-J002`, the boundary was reconfirmed from:

- `.codex-jobs/altibase-gpt-full-coverage-audit/jobs.tsv`: `FCA-J002` was the
  `Progress` job, with title "Source corpus lock" and goal "Freeze the exact selected
  source roots, source families, authoritative Korean sources, extraction aids,
  exclusions, and customer-facing scope boundaries."
- `.codex-jobs/altibase-gpt-full-coverage-audit/jobs.md`: `FCA-J002` targets
  `source_inventory.md`, `coverage_matrix.md`, and selected source roots, with expected
  durable output `source_corpus_lock.md`.
- `.codex-jobs/altibase-gpt-full-coverage-audit/requirements.md`: the full coverage
  audit must use selected repository-local sources only, with Korean-source precedence
  and no unresolved final `Missing` or `Retrieval-weak` dispositions.

## Repository Preflight Evidence

Required first checks from `AGENTS.md` were run before project edits:

| Check | Evidence | Result |
| --- | --- | --- |
| Review/remediation cycle status | `bash review/scripts/run_review_remediation_cycle.sh status` | `R00` through `R27` were all `Done` for both cycle and review status. |
| Active or failed stages | `rg -n $'\t(Reviewing\|Remediating\|ReReviewing\|Fail)$' review/review_remediation_cycle_status.tsv` | No matches; command exited `1`, which means no active or failed cycle rows were present. |
| Worktree status before project edits | `git status --short` | Only `.codex-jobs/altibase-gpt-full-coverage-audit/jobs.tsv` was modified. No project files outside workflow status/runtime files were dirty. |
| Recent committed workflow base | `git log --oneline -5` | `8808d1e2 Harden full coverage audit runner cwd handling` was HEAD before this project edit; prior workflow setup commits were already present. |

Because the only pre-existing dirty path was workflow status under `.codex-jobs/`, this
job was safe to proceed under the orchestrator contract.

`FCA-J002` re-ran the required first checks before editing project files:

| Check | Evidence | Result |
| --- | --- | --- |
| Review/remediation cycle status | `bash review/scripts/run_review_remediation_cycle.sh status` | `R00` through `R27` were all `Done` for both cycle and review status. |
| Active or failed stages | `rg -n $'\t(Reviewing\|Remediating\|ReReviewing\|Fail)$' review/review_remediation_cycle_status.tsv` | No matches; command exited `1`, which means no active or failed cycle rows were present. |
| Worktree status before project edits | `git status --short` | Only `.codex-jobs/altibase-gpt-full-coverage-audit/jobs.tsv` was modified. No project files outside workflow status/runtime files were dirty. |
| Baseline HEAD before this project edit | `git rev-parse --short HEAD` | `2423a61a` (`Mark FCA-J001 done`). |

## Source And Support Reports Inspected

The job-relevant portions of these repository-local artifacts were inspected:

- `AGENTS.md`
- `GPTs/attachments/README.md`
- `GPTs/GPT_Instructions_Draft.md`
- `GPTs/reports/source_inventory.md`
- `GPTs/reports/coverage_matrix.md`
- `GPTs/reports/gap_register.md`
- `GPTs/reports/final_upload_readiness.md`
- `GPTs/reports/answerability_failure_remediation_inventory_20260517.md`
- `evals/altibase_answerability/reports/full_benchmark/failure_root_cause_analysis_20260517.md`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_205641/summary.txt`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_205641/judge/report.md`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_205641/judge/aggregate_report.json`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_205641/judge/judgments.jsonl`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_205641/answers/answers.jsonl`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_205641/answers/run.json`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_205641/run-test.log`

Confirmed boundary facts:

- The upload package remains exactly the 20 Markdown files listed in
  `GPTs/attachments/README.md`, excluding that README.
- `GPTs/GPT_Instructions_Draft.md` is the customer answer contract and instruction
  basis, but the locked benchmark run below used attachment lexical context and did
  not include the instruction draft in the answer prompt.
- `GPTs/reports/source_inventory.md` remains the source-root and attachment-to-source
  path inventory.
- `GPTs/reports/coverage_matrix.md` remains the source family ownership and attachment
  routing map.
- `GPTs/reports/gap_register.md` remains the active guardrail, verification-limited,
  and closed-trace register until the new full coverage audit matrix/registers replace
  or refine those rows.
- Korean source precedence, selected repository-local sources only, and the customer
  label `Altibase 8.1 verified source` remain active policy.

## Locked Latest Benchmark Baseline

The latest full benchmark run locked for this audit is:

`evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_205641/`

Run metadata:

| Field | Value |
| --- | --- |
| Run ID | `altibase_answerability_20260517_205641` |
| Generated at | `2026-05-17T13:42:05Z` |
| Manifest | `full_benchmark` |
| Mode | `live` |
| Provider | `command` |
| Model | `codex-exec` |
| Context mode | `lexical` |
| Answer runner status | `ok` |
| Answer runner exit code | `0` |
| Answer records | `270` |
| Judgment records | `270` |
| Readiness decision | `blocking_gaps` |

Overall metrics:

| Metric | Locked value | Readiness threshold |
| --- | ---: | ---: |
| Passed / total | 101 / 270 | Overall pass rate >= 85.0% |
| Failed | 169 | 0 blocking failures expected before upload readiness |
| Pass rate | 37.4% | 85.0% |
| Critical fact coverage | 85.1% | 90.0% |
| Required token preservation | 90.1% | 95.0% |
| Unsupported-claim rate | 1.1% | <= 2.0% |
| Protected-topic blockers | 32 | 0 |

Domain results from `judge/report.md`:

| Domain | Questions | Passed | Failed | Pass rate | Max severity |
| --- | ---: | ---: | ---: | ---: | --- |
| `errors_troubleshooting` | 30 | 10 | 20 | 33.3% | blocker |
| `operations_admin` | 35 | 17 | 18 | 48.6% | blocker |
| `properties` | 50 | 18 | 32 | 36.0% | blocker |
| `replication_cdc_security_network` | 30 | 9 | 21 | 30.0% | blocker |
| `sql_ddl_dml_datatypes` | 45 | 15 | 30 | 33.3% | blocker |
| `tools_apis_connectors_migration` | 50 | 26 | 24 | 52.0% | high |
| `views_performance_monitoring` | 30 | 6 | 24 | 20.0% | blocker |

Protected-topic blockers:

| Topic | Count | Question IDs |
| --- | ---: | --- |
| `backup_recovery` | 6 | `ERR-110`, `ERR-113`, `OPS-114`, `OPS-116`, `PROP-130`, `VPM-114` |
| `destructive_sql` | 3 | `ERR-120`, `ERR-122`, `SQL-129` |
| `replication_state_changes` | 8 | `ERR-127`, `PROP-136`, `PROP-137`, `REPL-113`, `REPL-116`, `SQL-114`, `SQL-141`, `VPM-125` |
| `security_tls` | 3 | `PROP-140`, `REPL-103`, `REPL-121` |
| `version_sensitive_property_changes` | 12 | `PROP-112`, `PROP-115`, `PROP-117`, `PROP-122`, `PROP-123`, `PROP-127`, `PROP-128`, `PROP-129`, `PROP-131`, `PROP-132`, `PROP-144`, `PROP-148` |

Priority signals:

- The readiness decision is `blocking_gaps`.
- `views_performance_monitoring` is the worst domain by pass rate at `20.0%`.
- `113` of the `169` failed questions are in the high retrieval-risk bucket according
  to `judge/aggregate_report.json`.
- The top remediation target categories in `judge/report.md` are missing critical
  facts and missing required tokens, led by `properties`,
  `sql_ddl_dml_datatypes`, `views_performance_monitoring`,
  `errors_troubleshooting`, `replication_cdc_security_network`, and
  `operations_admin`.

Trend context from earlier full runs:

| Run | Passed / total | Failed | Pass rate | Critical fact coverage | Required token preservation | Protected-topic blockers | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `altibase_answerability_20260516_145452` | 24 / 270 | 246 | 8.9% | 68.3% | 73.4% | 81 | `blocking_gaps` |
| `altibase_answerability_20260517_095919` | 27 / 270 | 243 | 10.0% | 68.7% | 74.6% | 77 | `blocking_gaps` |
| `altibase_answerability_20260517_205641` | 101 / 270 | 169 | 37.4% | 85.1% | 90.1% | 32 | `blocking_gaps` |

## Locked Artifact Checksums

The following SHA-256 checksums lock the latest benchmark evidence files reviewed by
`FCA-J001`:

| Artifact | SHA-256 |
| --- | --- |
| `summary.txt` | `b4d16997f67c7bd31a618fa62cf25dcd20ea6616df3eb4dbf121944af5c9ea78` |
| `judge/report.md` | `a21110b13d67508966dc9305ec724b21a03fe8596cd3a2756537d6f592bddf7d` |
| `judge/aggregate_report.json` | `79cebf2a72b0961a9661e760b329ae25553e6359dcf7a7be0f35bd3367948d7a` |
| `judge/judgments.jsonl` | `be7c5e187d4e63c1a9766705a4cb8e8093278ec77c42332eabaf73abd3a6c3d3` |
| `answers/answers.jsonl` | `2899a671158d4b9f05c17f8de273984282de22ebb16261d781b2611c0ae7cca1` |
| `answers/run.json` | `970a94ff9eb3bd8225653fad45d76587d32a69911b7ff40168eaee21dac2dff7` |
| `run-test.log` | `184a11f0e17a41d2056d47c63729708184d2a6fe8d016e9406156e768cd14630` |

## Audit Use Rules

- Treat this locked benchmark as failure evidence for priority, targeted answerability,
  retrieval weakness, exact-token preservation, and protected-topic triage.
- Do not treat the 270 benchmark questions as the full audit scope. The full coverage
  audit scope is the selected repository-local source corpus recorded through
  `GPTs/reports/source_inventory.md`, `GPTs/reports/coverage_matrix.md`, and later
  `GPTs/reports/full_coverage_audit/source_item_catalog.tsv`.
- Do not lower benchmark thresholds, edit question expectations, or use non-repository
  Altibase facts to improve scores.
- Later catalog and matrix jobs must preserve exact literal token forms from selected
  sources and questions where those tokens are used as benchmark evidence.
- Remaining `Missing` and `Retrieval-weak` dispositions in the new full coverage audit
  artifacts are unresolved until remediated, routed, or converted to a justified
  `Guardrail` or `Out-of-scope` disposition.

## FCA-J002 Locked Source Corpus

The selected source corpus is the repository-local Markdown source material under the
root directories below, interpreted through the source family ownership in
`GPTs/reports/coverage_matrix.md` and the attachment-to-source inventory in
`GPTs/reports/source_inventory.md`.

The lock is a source boundary. It does not certify that every item is already covered in
the attachments. Item-level proof starts with `source_item_catalog.tsv` in later jobs.

### Authority Order

Apply this order when a catalog or remediation job finds overlapping source material:

1. Korean manuals, Korean release notes, Korean patch notes, Korean tool manuals,
   Korean technical documents, and Korean third-party guides are authoritative when
   Korean and English sources differ.
2. English manuals, release notes, patch notes, tool manuals, technical documents, and
   third-party guides are extraction aids when consistent with Korean sources.
3. Altibase 7.1 and 7.3 claims require the corresponding selected 7.x source family
   before broadening.
4. `Manuals/Altibase_trunk` and `Manuals/Tools/Altibase_trunk` are the selected
   Altibase 8.1 verified source. Customer-facing attachment wording must continue to
   use `Altibase 8.1 verified source`, not internal repository labels.
5. Patch-specific claims must keep exact patch boundaries and must come from selected
   7.1 or 7.3 patch notes, selected release notes, or a later row-specific source
   disposition.
6. Support reports under `GPTs/reports/` are internal traceability and validation
   evidence. They are not customer-facing source labels and do not override selected
   product sources.

### Locked Source Roots

The selected root set is frozen for this audit as follows. Counts and hashes are
path-list checks over Markdown files in each root at `FCA-J002` lock time; they are
audit aids, not item counts.

| Root | Role | Version or scope | Markdown paths | Path-list SHA-256 |
| --- | --- | --- | ---: | --- |
| `Manuals/Altibase_7.1/kor` | Authoritative manuals | Altibase 7.1 | 33 | `aa0d25e64baafe7af141d237cac2652d3b6d020a4e6130a14f30ec76c5d117b8` |
| `Manuals/Altibase_7.1/eng` | English extraction aid | Altibase 7.1 | 31 | `8db6908083faaa8ca21c09b13a0fd9af633345de054fd27593a3cee31a5e11f2` |
| `Manuals/Altibase_7.3/kor` | Authoritative manuals | Altibase 7.3 | 30 | `dca4fa6b3ecfeaf2a5d30e9e3a914aa6d447408749cab89b868b93c21a3a6a93` |
| `Manuals/Altibase_7.3/eng` | English extraction aid | Altibase 7.3 | 31 | `940b2d1d5fb61032a068857961153bd7ae2570e6716be5f78fccbd2c1fcfb31f` |
| `Manuals/Altibase_trunk/kor` | Authoritative manuals | Altibase 8.1 verified source | 30 | `15e4ef8a14387b00a4d711f963cc87414a5f02c92022cb84930e5276b911b73f` |
| `Manuals/Altibase_trunk/eng` | English extraction aid | Altibase 8.1 verified source | 30 | `2b75ada27704b652cb29a2e4aa39124bb9ff8436c3b7a95474dc5b812a83b6e9` |
| `ReleaseNotes/kor` | Authoritative release notes when content differs | 7.1, 7.3, 8.1, tool releases | 22 | `a18013ab93e01f03f20368261770938a4eb736f960200cbf40fcf83a792361bb` |
| `ReleaseNotes/eng` | English extraction aid | 7.1, 7.3, 8.1, tool releases | 23 | `97cfa36c149a333e7d3e04d429073fe560454cdd62703dd57b231b3bda837948` |
| `PatchNotes/Altibase_7.1/kor` | Authoritative patch notes | Altibase 7.1 patch-specific behavior | 96 | `4de6f4d91dfcaa042531a48bb1d1ba79e16662f0d4631feb9181138de1e592fe` |
| `PatchNotes/Altibase_7.1/eng` | English extraction aid | Altibase 7.1 patch-specific behavior | 70 | `ec5adf841584f10d39b5d85100f431cc66936ae47eda0f562e01be526c3ba264` |
| `PatchNotes/Altibase_7.3/kor` | Authoritative patch notes | Altibase 7.3 patch-specific behavior | 19 | `ec42a5fdf89ec67d718f33f16a012cea182f35aedf6d6ae0feda68a7257e6e9a` |
| `PatchNotes/Altibase_7.3/eng` | English extraction aid | Altibase 7.3 patch-specific behavior | 6 | `5ccd544fb091d913fd33a92ca75aeb3e6e125b85e21083bba5bdaab6ad4d5a0f` |
| `Manuals/Tools/Altibase_release/kor` | Authoritative tool manuals | 7.x release tool source | 7 | `2af5fb7775a5b5781ae9c3d40b9fc7d0cfaf74dc65cbfb92269eacb249af4d82` |
| `Manuals/Tools/Altibase_release/eng` | English extraction aid | 7.x release tool source | 7 | `d38f4afc575ddcf93c52fc70cca711dbe1c1b3ccd15c6267a9df2df10571d07c` |
| `Manuals/Tools/Altibase_trunk/kor` | Authoritative tool manuals | Altibase 8.1 verified tool source | 7 | `2664b02fb7bd4e5c546c108a38bb574b98783be5ddef0a03c32044439e7e0240` |
| `Manuals/Tools/Altibase_trunk/eng` | English extraction aid | Altibase 8.1 verified tool source | 7 | `4c0fd3140f373d547c3faed28e6c72465f3b12525281b7c373ad53995cd4fc45` |
| `Technical Documents/kor` | Authoritative when paired, Korean-only, or more specific | Cross-family support documents | 4 | `2245e3fa7ec30008c6f2319498a4d0ff75b2a85da74dbd1b3c28998c1b8cd856` |
| `Technical Documents/eng` | English extraction aid | Cross-family support documents | 2 | `9511e113600c67ea550653b74d5efe73e168fd2387dacf4e28779f5b70984618` |
| `3rd Party Guide for Altibase/kor` | Authoritative when paired or more specific | Third-party integration guides | 8 | `a46eac577bc8af24fe9d31ada4565996f0e26df1df6d70b34c7d758567a3d7e8` |
| `3rd Party Guide for Altibase/eng` | English extraction aid | Third-party integration guides | 7 | `34bd096456ed649785c403959bdf455c7de91572a1c79a19b9fd175611885d61` |

Combined selected Markdown path snapshot:

| Snapshot | Value |
| --- | --- |
| Selected Markdown paths | 470 |
| Combined path-list SHA-256 | `64b4c40b149953403e5bf440a6aabedcdfc732e7132b59cb0af05e891170fb0b` |
| Combined content-manifest SHA-256 | `6502e30d6248791bca1af3be3d282fcb5df466139509daad2cb321b1e3a9c996` |
| Evidence commands | `find <locked roots> -type f -name '*.md' \| sort`; `find <locked roots> -type f -name '*.md' -print0 \| sort -z \| xargs -0 sha256sum \| sha256sum` |

### Locked Source Families

The following source family IDs are frozen from
`GPTs/reports/coverage_matrix.md`. Catalog jobs must use these IDs in
`source_item_catalog.tsv` unless a later explicit workflow job updates the coverage
matrix and records the reason.

| Source family ID | Authority basis | Extraction basis | Primary attachment owners |
| --- | --- | --- | --- |
| `release_notes_platform` | Korean release notes and `Technical Documents/kor/Supported Platforms.md` | English release notes and supported-platform documents | `00` |
| `patch_notes` | `PatchNotes/Altibase_7.1/kor`, `PatchNotes/Altibase_7.3/kor` | Matching 7.x English patch notes when present | `00`, `05`, `06`, `09` |
| `getting_started_installation` | Korean Getting Started and Installation manuals | Matching English manuals | `01` |
| `administrator_operations` | Korean Administrator manuals plus SQL Reference where administrative SQL is needed | Matching English manuals | `02`, `03` |
| `sql_reference` | Korean SQL Reference manuals | Matching English SQL Reference manuals | `03`, `04`, `10`, `19` |
| `general_reference_1_datatypes_properties` | Korean General Reference 1 manuals | Matching English General Reference 1 manuals | `05`, `03`, `04` |
| `general_reference_2_dictionary_views` | Korean General Reference 2 manuals | Matching English General Reference 2 manuals | `06`, `08`, `09` |
| `error_message_reference` | Korean Error Message Reference manuals | Matching English Error Message Reference manuals | `07` |
| `performance_tuning` | Korean Performance Tuning Guides | Matching English Performance Tuning Guides | `08`, `06` |
| `monitoring_api_snmp` | Korean Monitoring API Developer's Guide and SNMP Agent Guide | Matching English manuals | `08`, `06` |
| `replication_manual` | Korean Replication Manual and SQL Reference | Matching English manuals | `09`, `03`, `06`, `18` |
| `log_analyzer` | Korean Log Analyzer User's Manual | Matching English manual | `09` |
| `replication_manager` | Korean Replication Manager manuals and release notes | Matching English manuals and release notes | `09`, `14` |
| `security_ssl_tls` | Korean SSL/TLS guide, Korean Replication Manual, and 8.1 Korean release notes | Matching English SSL/TLS guide and release notes | `18`, `09`, `11`, `12`, `13`, `14`, `16` |
| `stored_external_procedures` | Korean Stored Procedures and External Procedures manuals | Matching English manuals | `10`, `04` |
| `jdbc_java` | Korean JDBC and Adapter for JDBC manuals plus `Technical Documents/kor/JavaCompatibility.md` | English manuals and approved third-party guides | `11`, `16`, `17`, `19` |
| `c_cli_odbc_precompiler` | Korean CLI, ODBC, C Interface, and Precompiler manuals | Matching English manuals | `12`, `13` |
| `isql_iloader` | Korean iSQL and iLoader manuals | Matching English manuals | `13`, `14`, `19` |
| `utilities_datacompj` | Korean Utilities and dataCompJ manuals plus Korean utility release notes | Matching English manuals and release notes | `14`, `13`, `17` |
| `migration_oracle` | Korean Migration Center and Adapter for Oracle manuals plus Korean release notes | Matching English manuals and release notes | `15`, `04`, `19` |
| `dblink_hadoop_external_connectors` | Korean DB Link and Hadoop Connector manuals plus Korean third-party connector guide | Matching English manuals and connector guide | `16`, `03`, `06`, `11` |
| `kubernetes_aku` | Korean Kubernetes and AKU guides plus Korean release notes where present | Matching English guides and release notes | `17`, `14`, `09`, `18` |
| `spatial_nifi_tableau` | Korean Spatial SQL and altiShapeLoader manuals plus Korean NiFi/Tableau guides when present | Matching English manuals and guides | `19`, `13`, `14`, `15` |
| `technical_documents_support` | `Technical Documents/kor` where paired, Korean-only, or more specific | `Technical Documents/eng` | `00`, `09`, `11`, `16`, `18` |
| `third_party_guides` | `3rd Party Guide for Altibase/kor` when paired or more specific | `3rd Party Guide for Altibase/eng` | `11`, `16`, `17`, `19` |

### Customer-Facing Scope Boundary

The customer-facing upload package remains exactly the 20 Markdown files under
`GPTs/attachments/`, excluding `GPTs/attachments/README.md`:

1. `00_version_release_platform.md`
2. `01_getting_started_installation.md`
3. `02_administration_operations.md`
4. `03_sql_ddl_generation.md`
5. `04_sql_dml_oracle_compatibility.md`
6. `05_data_types_properties.md`
7. `06_data_dictionary_performance_views.md`
8. `07_error_messages_troubleshooting.md`
9. `08_performance_tuning_monitoring.md`
10. `09_replication_ha_cdc.md`
11. `10_psm_stored_external_procedures.md`
12. `11_java_jdbc_spring.md`
13. `12_c_cli_odbc_precompiler.md`
14. `13_isql_iloader_basic_tools.md`
15. `14_utilities_operation_tools.md`
16. `15_migration_oracle_compatibility.md`
17. `16_dblink_external_connectors.md`
18. `17_kubernetes_aku_cloud.md`
19. `18_security_ssl_tls.md`
20. `19_spatial_nifi_tableau_misc.md`

`GPTs/GPT_Instructions_Draft.md` remains the customer answer contract and instruction
basis. It is not a source root and must not be used to invent product behavior.

Customer-facing attachments must:

- stay in clear English;
- preserve exact SQL, property, command, API, view, error, version, option, file-path,
  class, method, and numeric tokens from selected sources;
- keep internal repository paths, branch names, workstation paths, and local build labels
  out of customer-facing text;
- ask for missing exact version, patch level, environment, object definition, topology,
  log excerpt, runtime output, installed tool behavior, or live integration state when
  selected sources do not support a definitive answer;
- use `Altibase 8.1 verified source` for customer-facing 8.1-only material where the
  attachment set uses that wording.

### Exclusions And Guardrail Boundaries

The following are outside the selected source corpus unless a later job creates an
explicit row-level `Out-of-scope` or `Guardrail` disposition with evidence:

- Web browsing, vendor pages outside this repository, generic Oracle/database memory,
  and non-repository Altibase claims.
- Original source documents outside the locked root list above.
- Older 6.x patch-note trees such as `PatchNotes/Altibase_6.1.1`,
  `PatchNotes/Altibase_6.3.1`, and `PatchNotes/Altibase_6.5.1`, except if a later job
  records a source-backed migration or historical reason.
- Non-Markdown binaries, PDFs, images, screenshots, decorative media, and boilerplate
  README content unless a selected Markdown source or later catalog row uses them as
  necessary evidence for an answer-ready item.
- Runtime behavior that requires a live Altibase server, installed client, compiler,
  Java runtime, Kubernetes cluster, network capture, TLS certificate set, third-party
  product instance, or customer data. These remain `Guardrail` or
  `Verification-limited` until customer evidence or selected source evidence is
  available.
- The 270 benchmark questions as a substitute for the full audit scope. Benchmark
  artifacts are priority and validation evidence only.

### FCA-J002 Handoff Rules

- Catalog jobs must use repository-relative paths from the locked roots.
- Every catalog row must use one frozen source family ID from the table above unless a
  later committed support-report update records a new family.
- A source-backed item absent from the attachments must start as `Missing`, not as an
  accepted absence.
- A source-backed item present but hard to retrieve must start as `Retrieval-weak`, not
  as fully covered.
- A row may use `Guardrail` only when selected sources are insufficient for a definitive
  customer answer or when the answer depends on exact version, patch, environment,
  object definition, log excerpt, runtime output, installed tool behavior, or live
  integration state.
- A row may use `Out-of-scope` only with a specific reason tied to this lock.
- Later remediation must not edit original manuals or source documents.

## FCA-J001 Verification

Verification run for this job:

| Check | Result |
| --- | --- |
| `LC_ALL=C rg -n '[^ -~\t]' GPTs/reports/full_coverage_audit/source_corpus_lock.md` | No matches; the new audit lock is ASCII-only. |
| `git diff --check` | Pass. |
| `bash review/scripts/run_review_stage.sh validate` | Pass; validation reported 20 upload attachments excluding `README.md` and completed without errors. |
| Review-report verdict/severity scan | `rg` returned `Verdict: Pass` lines for `R00` through `R27` and no actionable severity rows. |

## FCA-J001 Residual Risk And Handoff

- `FCA-J001` did not run a new 270-question live benchmark. It locked the existing
  latest run because the job scope is preflight and evidence locking.
- `FCA-J001` did not perform item-level source extraction. `FCA-J002` now freezes the
  selected source corpus in this file before catalog jobs add rows.
- Existing guardrail and verification-limited entries in `GPTs/reports/gap_register.md`
  remain active until new audit registers supersede them with traceable dispositions.
- The pre-existing `.codex-jobs/altibase-gpt-full-coverage-audit/jobs.tsv` status
  modification is workflow state owned by the orchestrator; this project commit should
  include only scoped repository audit artifacts.

## FCA-J002 Verification

Verification run for this job:

| Check | Result |
| --- | --- |
| Source root path snapshot | 470 selected Markdown paths under the locked roots; combined path-list SHA-256 `64b4c40b149953403e5bf440a6aabedcdfc732e7132b59cb0af05e891170fb0b`. |
| Source content manifest snapshot | Combined selected-source content-manifest SHA-256 `6502e30d6248791bca1af3be3d282fcb5df466139509daad2cb321b1e3a9c996`. |
| Scope self-review | No customer-facing attachment or GPT instruction was edited; original manuals and source documents were not edited; source family IDs match `GPTs/reports/coverage_matrix.md`; source roots match `GPTs/reports/source_inventory.md`; exclusions are explicit. |
| `LC_ALL=C rg -n '[^ -~\t]' GPTs/reports/full_coverage_audit/source_corpus_lock.md` | No matches; the updated audit lock is ASCII-only. |
| `git diff --check` | Pass. |
| `bash review/scripts/run_review_stage.sh validate` | Pass; validation reported 20 upload attachments excluding `README.md` and completed without errors. |
| Review-report verdict/severity scan | `rg` returned `Verdict: Pass` lines for `R00` through `R27` and no actionable severity rows. |

## FCA-J002 Residual Risk And Handoff

- `FCA-J002` locks source roots and family ownership only. It does not assert item-level
  coverage and does not close any `Missing` or `Retrieval-weak` disposition.
- The selected roots contain some README/media-style Markdown files. Later catalog jobs
  must mark non-product boilerplate as `Out-of-scope` when it does not carry
  answer-ready Altibase behavior.
- Remaining guardrail and verification-limited entries in `GPTs/reports/gap_register.md`
  stay active until new full coverage audit registers supersede them row by row.
- The pre-existing `.codex-jobs/altibase-gpt-full-coverage-audit/jobs.tsv` status
  modification is workflow state owned by the orchestrator; this project commit should
  include only scoped repository audit artifacts.
