# Stage 4 Upload Package Plan

- Job: `S4-J001`
- Date: 2026-05-19
- Status: Blocked by preflight
- Package directory: `GPTs/upload_package/` is absent and must remain unassembled
  until the Stage 3 workflow-ledger blocker is cleared.

## Design Note

This initial plan records Stage 4 composition constraints and the first routing
decision points. It does not create an upload manifest, upload-package Markdown, or
crosswalk files because `stage_04_preflight_status.md` is not ready/pass.

## Current Blocker

Stage 4 package assembly is blocked because
`.codex-jobs/altibase-gpt-stage-03-attachments-followup/jobs.tsv` records all
`S3-J001` through `S3-J018` rows as `ToDo`. The Stage 3 readiness report says Stage 3
is ready/pass for guarded Stage 4 routing, but this plan cannot proceed until the
workflow ledger is reconciled by the orchestrator/operator.

## Composition Principles After Blocker Clearance

| Area | Required handling |
| --- | --- |
| Global file limit | Keep the final GPT Knowledge upload package at `20` Markdown files or fewer, including any AID-derived content. |
| Upload boundary | Treat only Markdown files intentionally placed under `GPTs/upload_package/` and listed in the final Stage 4 manifest as upload files. |
| Source-preserving layer | Use `GPTs/source_pack/` as exact source-route evidence; do not upload raw source-pack shards directly unless a later job intentionally transforms and counts them. |
| Korean-aligned baseline | Preserve Korean-authoritative policy, `Altibase 8.1 verified source` wording, AID labels, and conflict/recheck handling. |
| Playbook layer | Route customer and coding-agent tasks through the validated playbooks, while keeping `APB-000014` deferred unless a later job creates a source-ID-backed test-generation playbook or records final exclusion. |
| Attachment layer | Use the 20 validated Stage 3 attachment files as the starting answer-ready structure only if later composition confirms source-preserving, playbook, and AID routing can fit without exceeding the global limit. |
| AID candidates | Decide whether to integrate `AID-000001` through `AID-000005` into existing upload files or exclude/defer them with recorded labels; no separate AID file set is allowed beyond the same global `20` file limit. |
| Guardrails | Carry `CONF-000004` through `CONF-000007`, item-level `CONF-000008`, and `CONF-000009` exclusions into package text, manifest notes, or crosswalk evidence as appropriate. |

## Initial Package Shape Hypothesis

The conservative starting hypothesis is to preserve the current 20 attachment-topic
filenames as package-topic candidates and enrich them with source-route and playbook
routing notes during scoped Stage 4 assembly. This is only a hypothesis, not approval
to assemble files:

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

If AID upload-content candidates require separate customer-facing Markdown, a later
Stage 4 composition job must merge, replace, or reduce the package shape so the final
package remains at `20` Markdown files or fewer.

## Required Next Stage 4 Steps After Blocker Clearance

1. Re-run the `S4-J001` preflight and require a ready/pass verdict.
2. Create `GPTs/upload_package/` and deterministic package-generation or copy rules
   only in a scoped Stage 4 assembly job.
3. Build `stage_04_upload_package_manifest.tsv` with every upload file, source
   families, AID tier coverage, byte size, estimated tokens, and evidence references.
4. Build source-pack, Korean-aligned English, playbook, and attachment crosswalks to
   the upload package.
5. Validate global file count, package boundary, exact-token preservation, source
   labels, guardrail text, internal-label exposure, local path leakage, Markdown
   structure, and upload manifest completeness.
6. Keep final upload readiness and live benchmark readiness out of scope until the
   Stage 4 package and Stage 5 readiness checks pass.

## Non-Goals For This Blocked Plan

- Do not create upload-package Markdown files.
- Do not mark `APB-000014` complete.
- Do not convert AID evidence-only rows or accepted limitations into customer upload
  content.
- Do not use `SRC-000109` or `SRC-000169` as authoritative upload-package content.
- Do not claim final upload readiness, live benchmark readiness, or production
  operational certainty.
