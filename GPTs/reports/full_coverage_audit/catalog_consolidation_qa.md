# Full Coverage Audit Catalog Consolidation QA

- Workflow: `altibase-gpt-full-coverage-audit`
- Audit job: `FCA-J039`
- Status: Catalog QA passed; source-to-attachment matrix mapping remains assigned to `FCA-J040`
- Date: 2026-05-18

## Job Boundary

`FCA-J039` validates the existing `source_item_catalog.tsv` before matrix mapping. This
job does not add source items, change catalog dispositions, remediate customer-facing
attachments, edit original source documents, or populate `source_to_attachment_matrix.tsv`.

The durable output for this job is this QA report, stricter reusable catalog QA tooling,
and a remediation-log entry. The canonical catalog rows from `FCA-J004` through
`FCA-J038` were preserved.

## Inputs Inspected

The job-relevant portions of these repository-local artifacts were inspected:

- `AGENTS.md`
- `.codex-jobs/altibase-gpt-full-coverage-audit/jobs.tsv`
- `.codex-jobs/altibase-gpt-full-coverage-audit/jobs.md`
- `.codex-jobs/altibase-gpt-full-coverage-audit/prompts/FCA-J039.md`
- `GPTs/attachments/README.md`
- `GPTs/GPT_Instructions_Draft.md`
- `GPTs/reports/source_inventory.md`
- `GPTs/reports/coverage_matrix.md`
- `GPTs/reports/gap_register.md`
- `GPTs/reports/final_upload_readiness.md`
- `GPTs/reports/answerability_failure_remediation_inventory_20260517.md`
- `GPTs/reports/full_coverage_audit/catalog_schema_and_extraction_scripts.md`
- `GPTs/reports/full_coverage_audit/source_corpus_lock.md`
- `GPTs/reports/full_coverage_audit/source_item_catalog.tsv`
- `GPTs/reports/full_coverage_audit/source_to_attachment_matrix.tsv`
- `GPTs/reports/full_coverage_audit/missing_item_register.md`
- `GPTs/reports/full_coverage_audit/guardrail_register.md`
- `GPTs/reports/full_coverage_audit/retrieval_weakness_register.md`
- `GPTs/reports/full_coverage_audit/remediation_log.md`
- `evals/altibase_answerability/reports/full_benchmark/failure_root_cause_analysis_20260517.md`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_205641/summary.txt`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_205641/judge/report.md`

## First-Check Evidence

Required first checks from `AGENTS.md` were run before project edits:

| Check | Evidence | Result |
| --- | --- | --- |
| Review/remediation cycle status | `bash review/scripts/run_review_remediation_cycle.sh status` | `R00` through `R27` were all `Done` for both cycle and review status. |
| Active or failed cycle stages | `rg -n $'\t(Reviewing\|Remediating\|ReReviewing\|Fail)$' review/review_remediation_cycle_status.tsv` | No matches; exit code `1` means no active or failed cycle rows were present. |
| Worktree status before edits | `git status --short` | Only `.codex-jobs/altibase-gpt-full-coverage-audit/jobs.tsv` was modified. No project files outside workflow status/runtime files were dirty. |

## QA Tooling Added

`fca_catalog_tools.py` now has a stricter QA command:

```bash
python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py catalog-qa
```

This command supplements the existing `check --require-registers` validation with:

- canonical catalog and matrix column order checks;
- `source_item_id` version-code consistency with `version_scope`;
- non-empty `source_heading`, `literal_tokens`, and `source_summary`;
- existing repository-relative `source_path` files;
- non-empty `attachment_anchor` for represented `Covered`, `Covered-by-routing`,
  `Guardrail`, and `Retrieval-weak` rows;
- all controlled source families present in the catalog;
- ID namespace sequence-gap count for stable-ID review; sequence gaps are not fatal
  because retired IDs must not be reused;
- register reconciliation for unresolved `Missing`, `Guardrail`, `Out-of-scope`, and
  `Retrieval-weak` rows.

## Catalog QA Result

Command:

```bash
python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py catalog-qa
```

Result: `OK: catalog QA passed`

Catalog status:

| Check area | Result |
| --- | --- |
| Catalog rows | `2153` |
| Matrix rows | `0`; expected before `FCA-J040` matrix build |
| Catalog header | Canonical 14-column order matches the schema |
| Matrix header | Canonical 14-column order matches the schema |
| Duplicate `source_item_id` values | `0` |
| Invalid ID formats | `0` |
| ID/version-scope mismatches | `0` |
| ID namespace sequence gaps | `0` observed in this QA pass; future gaps should preserve retired IDs rather than reusing them |
| Invalid controlled vocabulary values | `0` |
| Missing repository-relative `source_path` files | `0` |
| Empty `literal_tokens`, `source_summary`, `audit_job`, or `evidence` fields | `0` |
| Missing represented anchors | `0`; unresolved `Missing` and `Out-of-scope` rows may keep `attachment_anchor` blank |
| Unregistered unresolved dispositions | `0` |

## Disposition Totals

| coverage_status | Rows |
| --- | ---: |
| `Covered` | 1035 |
| `Covered-by-routing` | 840 |
| `Guardrail` | 33 |
| `Missing` | 232 |
| `Out-of-scope` | 3 |
| `Retrieval-weak` | 10 |

Register reconciliation:

| Disposition set | Catalog rows | Register check |
| --- | ---: | --- |
| `Missing` | 232 | Every row ID appears in `missing_item_register.md`. |
| `Guardrail` plus `Out-of-scope` | 36 | Every row ID appears in `guardrail_register.md`. |
| `Retrieval-weak` | 10 | Every row ID appears in `retrieval_weakness_register.md`. |

The unresolved `Missing` and `Retrieval-weak` totals remain intentional handoff work for
later remediation and routing jobs. They are not closed by this QA job.

## Version Scope Totals

| version_scope | Rows |
| --- | ---: |
| `7.1` | 96 |
| `7.3` | 15 |
| `8.1` | 65 |
| `cross-version` | 1838 |
| `patch-specific` | 139 |

## Source Family Completeness

All 25 controlled source families from `coverage_matrix.md` and the catalog schema have
at least one row, and no catalog row uses an out-of-vocabulary source family.

| source_family | Rows |
| --- | ---: |
| `administrator_operations` | 49 |
| `c_cli_odbc_precompiler` | 34 |
| `dblink_hadoop_external_connectors` | 35 |
| `error_message_reference` | 644 |
| `general_reference_1_datatypes_properties` | 380 |
| `general_reference_2_dictionary_views` | 226 |
| `getting_started_installation` | 40 |
| `isql_iloader` | 31 |
| `jdbc_java` | 38 |
| `kubernetes_aku` | 20 |
| `log_analyzer` | 19 |
| `migration_oracle` | 30 |
| `monitoring_api_snmp` | 53 |
| `patch_notes` | 115 |
| `performance_tuning` | 81 |
| `release_notes_platform` | 50 |
| `replication_manager` | 9 |
| `replication_manual` | 33 |
| `security_ssl_tls` | 16 |
| `spatial_nifi_tableau` | 26 |
| `sql_reference` | 105 |
| `stored_external_procedures` | 46 |
| `technical_documents_support` | 22 |
| `third_party_guides` | 11 |
| `utilities_datacompj` | 40 |

## Audit Job Coverage

Every catalog extraction job from `FCA-J004` through `FCA-J038` owns at least one row.
`FCA-J039` created no catalog rows and did not change existing row ownership.

| audit_job | Rows |
| --- | ---: |
| `FCA-J004` | 165 |
| `FCA-J005` | 40 |
| `FCA-J006` | 34 |
| `FCA-J007` | 29 |
| `FCA-J008` | 27 |
| `FCA-J009` | 21 |
| `FCA-J010` | 37 |
| `FCA-J011` | 15 |
| `FCA-J012` | 34 |
| `FCA-J013` | 41 |
| `FCA-J014` | 87 |
| `FCA-J015` | 94 |
| `FCA-J016` | 121 |
| `FCA-J017` | 73 |
| `FCA-J018` | 132 |
| `FCA-J019` | 21 |
| `FCA-J020` | 193 |
| `FCA-J021` | 155 |
| `FCA-J022` | 148 |
| `FCA-J023` | 148 |
| `FCA-J024` | 81 |
| `FCA-J025` | 53 |
| `FCA-J026` | 30 |
| `FCA-J027` | 25 |
| `FCA-J028` | 21 |
| `FCA-J029` | 46 |
| `FCA-J030` | 38 |
| `FCA-J031` | 34 |
| `FCA-J032` | 31 |
| `FCA-J033` | 40 |
| `FCA-J034` | 30 |
| `FCA-J035` | 42 |
| `FCA-J036` | 20 |
| `FCA-J037` | 30 |
| `FCA-J038` | 17 |

Narrative-log completeness note: catalog rows exist for `FCA-J013`, `FCA-J014`,
`FCA-J025`, `FCA-J029`, `FCA-J031`, and `FCA-J036`, but `remediation_log.md` did not
contain individual `###` sections for those jobs at the start of this QA pass. This job
records the issue in the `FCA-J039` remediation-log entry. The missing historical
headings are not a catalog or register blocker because the catalog rows, evidence
fields, and relevant registers passed QA.

## Matrix Handoff

`source_to_attachment_matrix.tsv` currently contains only the canonical header. That is
valid for `FCA-J039` because source-to-attachment row mapping is assigned to `FCA-J040`.

`FCA-J040` should start from this validated catalog and preserve the same
`source_item_id` values, source families, version scopes, source locators, item types,
attachment targets, current dispositions, guardrail reasons, audit jobs, and evidence
unless it has source-backed reason to update a row.

## Residual Risk

- `232` `Missing` rows and `10` `Retrieval-weak` rows remain unresolved by design and
  must be closed or re-dispositioned by later matrix, remediation, and routing jobs.
- `33` `Guardrail` rows and `3` `Out-of-scope` rows remain active and must keep their
  missing-input or source-boundary reasons during later mapping.
- This job did not perform customer-facing answer remediation, targeted answerability
  reruns, or full benchmark execution.
