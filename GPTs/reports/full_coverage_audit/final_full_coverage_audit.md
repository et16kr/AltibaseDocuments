# Final Full Coverage Audit

- Workflow: `altibase-gpt-full-coverage-audit`
- Audit job: `FCA-J051`
- Date: 2026-05-18
- Final readiness decision: `Blocked`
- Sign-off status: Not granted. The audit still has unresolved `Missing` rows.

## Decision Summary

The full source-to-attachment audit cannot be signed off in its current state.

Machine-checkable source coverage is structurally valid and retrieval closure is clean,
but the non-negotiable final-state rule is not met: `source_item_catalog.tsv` and
`source_to_attachment_matrix.tsv` still contain `115` unresolved `Missing` rows. All
remaining `Missing` rows are `patch_notes` / `patch-specific` / `version note` rows
mapped to `GPTs/attachments/00_version_release_platform.md`.

No unresolved `Retrieval-weak` rows remain.

## Job Boundary

`FCA-J051` is the final-report job. Its durable output is this report and the final
readiness decision. This job did not remediate attachment content, edit original
manuals or source documents, broaden Altibase behavior, or re-disposition catalog
rows without source review.

The required first checks were run before edits:

| Check | Result |
| --- | --- |
| `bash review/scripts/run_review_remediation_cycle.sh status` | `R00` through `R27` were all `Done` for both cycle and review status. |
| `rg -n $'\t(Reviewing\|Remediating\|ReReviewing\|Fail)$' review/review_remediation_cycle_status.tsv` | No active or failed cycle rows; exit code `1` with no matches. |
| `git status --short` | Only `.codex-jobs/altibase-gpt-full-coverage-audit/jobs.tsv` was dirty before project edits. |

## Source Scope

The locked source corpus is the repository-local selected corpus recorded in
`source_corpus_lock.md`, `GPTs/reports/source_inventory.md`, and
`GPTs/reports/coverage_matrix.md`.

Authority policy:

- Korean manuals, release notes, patch notes, tool manuals, technical documents, and
  third-party guides are authoritative when Korean and English sources differ.
- English sources are extraction aids when consistent with Korean sources.
- Altibase 7.1 and 7.3 claims require corresponding selected 7.x sources.
- `Manuals/Altibase_trunk` and `Manuals/Tools/Altibase_trunk` are treated as the
  Altibase 8.1 verified source, with customer-facing wording preserved as
  `Altibase 8.1 verified source`.
- No web or non-repository Altibase facts are part of this audit.
- Original manuals and source documents are not edited by the audit workflow.

## Audit Method

The audit proof uses one machine-checkable catalog row and one matrix row for each
reviewed source item:

- `source_item_catalog.tsv` records stable item IDs, source family, version scope,
  source path and heading, item type, literal tokens, normalized summary, attachment
  target, disposition, attachment anchor, guardrail reason, audit job, and evidence.
- `source_to_attachment_matrix.tsv` mirrors each catalog row into the attachment
  routing layer, including aliases, matrix notes, and copied disposition fields.
- `missing_item_register.md`, `guardrail_register.md`, and
  `retrieval_weakness_register.md` track unresolved or guarded dispositions.
- `remediation_log.md` records per-job changes, validation, skipped checks, and
  residual risk.

Dispositions are limited to `Covered`, `Covered-by-routing`, `Guardrail`,
`Out-of-scope`, `Missing`, and `Retrieval-weak`.

## Coverage Totals

Catalog and matrix row counts match exactly: `2153` catalog rows and `2153` matrix
rows.

| coverage_status | Rows |
| --- | ---: |
| `Covered` | 1162 |
| `Covered-by-routing` | 840 |
| `Guardrail` | 33 |
| `Out-of-scope` | 3 |
| `Missing` | 115 |
| `Retrieval-weak` | 0 |

Closure count:

| State | Rows |
| --- | ---: |
| Closed or justified (`Covered`, `Covered-by-routing`, `Guardrail`, `Out-of-scope`) | 2038 |
| Unresolved (`Missing`, `Retrieval-weak`) | 115 |

## Totals By Version Scope

| version_scope | Rows |
| --- | ---: |
| `7.1` | 96 |
| `7.3` | 15 |
| `8.1` | 65 |
| `cross-version` | 1838 |
| `patch-specific` | 139 |

## Totals By Source Family

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

## Totals By Item Type

| item_type | Rows |
| --- | ---: |
| `API` | 93 |
| `SQL syntax` | 121 |
| `column` | 16 |
| `command option` | 29 |
| `compatibility rule` | 60 |
| `connector setting` | 14 |
| `data type` | 39 |
| `error code` | 643 |
| `example` | 4 |
| `function` | 28 |
| `other documented category` | 177 |
| `platform rule` | 15 |
| `property` | 378 |
| `release note` | 38 |
| `runbook step` | 133 |
| `tool command` | 54 |
| `version note` | 126 |
| `view` | 133 |
| `warning` | 52 |

## Matrix Totals By Attachment

| attachment_target | Rows |
| --- | ---: |
| `GPTs/attachments/00_version_release_platform.md` | 145 |
| `GPTs/attachments/01_getting_started_installation.md` | 34 |
| `GPTs/attachments/02_administration_operations.md` | 46 |
| `GPTs/attachments/03_sql_ddl_generation.md` | 57 |
| `GPTs/attachments/04_sql_dml_oracle_compatibility.md` | 54 |
| `GPTs/attachments/05_data_types_properties.md` | 369 |
| `GPTs/attachments/06_data_dictionary_performance_views.md` | 227 |
| `GPTs/attachments/07_error_messages_troubleshooting.md` | 644 |
| `GPTs/attachments/08_performance_tuning_monitoring.md` | 134 |
| `GPTs/attachments/09_replication_ha_cdc.md` | 78 |
| `GPTs/attachments/10_psm_stored_external_procedures.md` | 46 |
| `GPTs/attachments/11_java_jdbc_spring.md` | 40 |
| `GPTs/attachments/12_c_cli_odbc_precompiler.md` | 36 |
| `GPTs/attachments/13_isql_iloader_basic_tools.md` | 33 |
| `GPTs/attachments/14_utilities_operation_tools.md` | 44 |
| `GPTs/attachments/15_migration_oracle_compatibility.md` | 43 |
| `GPTs/attachments/16_dblink_external_connectors.md` | 54 |
| `GPTs/attachments/17_kubernetes_aku_cloud.md` | 20 |
| `GPTs/attachments/18_security_ssl_tls.md` | 14 |
| `GPTs/attachments/19_spatial_nifi_tableau_misc.md` | 32 |
| `N/A` | 3 |

## Unresolved Missing Rows

The remaining unresolved rows are:

| Field | Value |
| --- | --- |
| Count | `115` |
| `source_item_id` range | `SRC-PATCH-PATCH-000001` through `SRC-PATCH-PATCH-000115` |
| Source family | `patch_notes` |
| Version scope | `patch-specific` |
| Item type | `version note` |
| Attachment target | `GPTs/attachments/00_version_release_platform.md` |
| Source split | `96` Altibase 7.1 patch-note files and `19` Altibase 7.3 patch-note files |

Required closure work: add or route answer-ready patch-note blocks in attachment `00`,
or split the current patch-file change-set rows into per-BUG or per-feature rows before
closure. Each closure must preserve exact patch versions, BUG/TASK tokens, affected
feature/property/view/tool names, source-backed caveats, and routing to detailed owner
attachments when applicable.

These rows cannot be treated as accepted guardrails merely because they are
patch-specific. They are selected, source-backed, in-scope patch-note items that still
lack answer-ready attachment representation.

## Retrieval Closure

Active `Retrieval-weak` rows: `0`.

`FCA-J046` strengthened retrieval routing for attachments `00` through `09`, and
`FCA-J047` strengthened routing for attachments `10` through `19`. The
`retrieval_weakness_register.md` records zero active scoped unresolved-row counts for
both groups. The final matrix also has `0` rows with `coverage_status=Retrieval-weak`.

## Guardrails And Out-Of-Scope Rows

Guarded rows are structurally clean:

| Disposition | Rows |
| --- | ---: |
| `Guardrail` | 33 |
| `Out-of-scope` | 3 |

`guardrail_register.md` contains all `36` guarded rows and the `guardrail-audit`
command passed. The active guardrails cover source or customer-evidence dependencies
such as exact patch/version boundaries, installed metadata, live tool behavior,
runtime logs/output, replication topology, platform/package state, Java/runtime
versions, connector configuration, and unsupported older-version scope.

Customer answer pattern for guarded rows:

- Ask for exact version, patch level, component, topology, object definition, command,
  configuration, installed metadata, tool/package version, log excerpt, or runtime
  output as required by the row.
- Give only the safest selected-source-backed next check, such as querying
  `V$VERSION`, `V$TABLE`, `V$ALLCOLUMN`, `SYSTEM_.SYS_TABLES_`, or
  `SYSTEM_.SYS_COLUMNS_`, running installed tool help/version output, or validating in
  non-production.
- Do not invent unsupported compatibility, runtime success, full column layouts,
  exact error-code mappings, or package contents from generic database knowledge.

## Benchmark Evidence

The locked latest full benchmark remains failure evidence, not the full audit scope:

| Metric | Locked latest run |
| --- | ---: |
| Run ID | `altibase_answerability_20260517_205641` |
| Passed / total | `101 / 270` |
| Failed | `169` |
| Pass rate | `37.4%` |
| Critical fact coverage | `85.1%` |
| Required token preservation | `90.1%` |
| Unsupported-claim rate | `1.1%` |
| Protected-topic blockers | `32` |
| Readiness decision | `blocking_gaps` |

`FCA-J050` also ran a 14-question targeted live sample with the instruction draft
included. It improved from `2 / 14` to `6 / 14` passed for the same question IDs, but
the targeted result remained `blocking_gaps` with `4` protected-topic blockers.

The full 270-question live benchmark was not rerun in `FCA-J050` or `FCA-J051` because
the source-to-attachment closure gate is already blocked by the `115` active patch-note
`Missing` rows and the targeted live sample still has protected blockers. A full live
rerun would require 270 provider calls and could not produce a final readiness pass
until the coverage gate is closed.

## Validation Output

Scoped source-to-attachment checks run for this final report:

```bash
python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers
python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py catalog-qa
python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py matrix-qa
python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py guardrail-audit
```

Result: all four commands passed structurally. They validate required columns,
controlled vocabularies, duplicate IDs, matrix/catalog reconciliation, register
presence, missing-row registration, retrieval-weak registration, guardrail registration,
and guarded-row missing-input or safest-next-check patterns.

Current structural result:

- Catalog rows: `2153`.
- Matrix rows: `2153`.
- Duplicate `source_item_id` values: `0`.
- ID namespace sequence gaps: `0`.
- Active `Retrieval-weak` rows: `0`.
- Active `Missing` rows: `115`.
- Guardrail register rows: `36`.

Standard verification was also run after report edits:

```bash
git diff --check
bash review/scripts/run_review_stage.sh validate
rg -n "^Verdict:|^\| (Blocker|High|Medium|Low) \|" review/reports/R*.md
```

Result: recorded in the `FCA-J051` remediation-log entry. Any skipped full-live
benchmark is justified above.

## Final Readiness Decision

Final readiness decision: `Blocked`.

Reason: the audit has `115` unresolved `Missing` rows. The attachment package cannot be
certified as a source-exhaustive, customer-usable Altibase GPT encyclopedia until those
patch-note rows are remediated, routed, or re-dispositioned with source-backed reasons.

Minimum work before sign-off:

1. Close `SRC-PATCH-PATCH-000001` through `SRC-PATCH-PATCH-000115` as `Covered`,
   `Covered-by-routing`, `Guardrail`, or `Out-of-scope` with source-backed evidence.
2. Re-run `check --require-registers`, `catalog-qa`, `matrix-qa`, and
   `guardrail-audit`.
3. Re-run the standard repository verification commands.
4. Re-run targeted protected-topic answerability checks; then run the full live
   270-question benchmark when the closure gate is no longer blocked.
5. Replace this decision with sign-off only after there are no unresolved `Missing` or
   `Retrieval-weak` rows and readiness validation no longer reports blocking gaps.
