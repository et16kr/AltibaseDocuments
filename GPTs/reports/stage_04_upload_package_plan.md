# Stage 4 Upload Package Composition Plan

- Job: `S4-J002`
- Date: 2026-05-19
- Scope: upload package composition plan, manifest schema, validation scaffold, and
  routing policy only
- Package directory: `GPTs/upload_package/` must remain absent in this job
- Assembly gate: `GPTs/reports/stage_04_preflight_status.md` still records
  `Verdict: Not ready for upload-package assembly`

## Boundary Reconfirmation

`S4-J002` defines the Stage 4 package architecture and deterministic validation
scaffold. It does not assemble broad upload content, create files under
`GPTs/upload_package/`, mark deferred playbooks complete, edit source manuals, or
modify `.codex-jobs/` workflow runtime files.

The current preflight report blocks upload-package assembly because the Stage 3
workflow ledger was not reconciled by the orchestrator. This scaffold is therefore
usable only as a pre-assembly contract until a later scoped job records a ready/pass
preflight or an operator reconciles that ledger mismatch.

## Design Note

This job changes Stage 4 documentation structure by replacing the blocked initial
plan with an explicit package file map, manifest schema, AID decision path, source and
playbook routing requirements, and a reusable validator. The validator supports a
pre-assembly scaffold mode so the repository can validate planned rows without
creating `GPTs/upload_package/`.


## S4-J003 Assembly Update

`S4-J003` starts progressive package assembly without changing the 20-file topic
architecture. It creates the first operational upload slice for version/release and
platform boundaries, installation/startup, and administration/backup/recovery. The
slice preserves full answer-ready attachment content under `Answer-Ready Reference`,
adds package-level source and playbook routing, and records source-pack,
Korean-aligned English, playbook, and attachment-to-upload crosswalk rows for the
assembled files.

The package is not final-upload ready after this slice. Remaining topic files, final
AID selection, retrieval checks, benchmark dry runs, and Stage 4 readiness remain
deferred to later scoped jobs. The validator now supports a progressive assembled
mode so assembled rows can pass while future rows remain planned.

## Package Shape Decision

The final package will use the existing 20 attachment topic filenames as the upload
file map unless a later Stage 4 review records a validator-backed need to merge or
replace files. No separate source-pack, playbook, or AID upload file set is allowed.

This decision keeps the global GPT Knowledge upload count at exactly 20 Markdown
files when assembly starts:

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

The source-preserving, playbook, and answer-ready layers are represented inside those
20 files as sections and routing notes, not as additional upload files:

| Layer | Upload-package representation | Outside-package evidence |
| --- | --- | --- |
| Source-preserving pack | Source route metadata and exact source-boundary references where needed. | `GPTs/source_pack/`, source manifests, source-to-upload crosswalks. |
| Korean-aligned English baseline | English-normalized wording and authority labels. `KAE-BLOCK-*` IDs stay outside upload Markdown. | Baseline manifest and baseline-to-upload crosswalk. |
| Agent playbooks | Task routing, missing-input prompts, generated-artifact boundaries, validation checks, stop conditions, and rollback or cleanup notes. | Playbook manifest and playbook-to-upload crosswalk. |
| Answer-ready attachments | Primary customer-facing reference blocks and retrieval aliases. | Attachment files and attachment-to-upload crosswalk. |

## Required Upload Markdown Sections

Every upload Markdown file must include these top-level sections after assembly:

1. `## Package Role`
2. `## Applicable Versions And Authority`
3. `## Questions This File Can Answer`
4. `## Retrieval Alias Index`
5. `## Source Routes`
6. `## Task And Playbook Routing`
7. `## Answer-Ready Reference`
8. `## Required Inputs And Stop Conditions`
9. `## Validation And Rollback Checks`
10. `## Cross-References`
11. `## Residual Scope And Limitations`

The `Answer-Ready Reference` section should carry the relevant Stage 3 attachment
content, normalized only as needed for source-boundary metadata, agent routing, and
upload-boundary hygiene.

## Source Metadata Policy

All 20 upload Markdown files may contain limited source-boundary metadata in the
`Source Routes` section:

- allowed: `SRC-*`, `AID-SRC-*`, source-pack `BLOCK-*` IDs, authority labels,
  version scope labels, and exact source titles when they help source-backed
  synthesis;
- allowed only as customer-readable labels: `Korean-source-verified`,
  `Link-validated Korean-source-verified`, `English-only source`,
  `source_limitation`, and `Altibase 8.1 verified source`;
- not allowed in upload Markdown: `KAE-BLOCK-*`, `APB-*`, `CONF-*`,
  `S3-SCOPE-*`, job IDs, local workspace paths, `.codex-jobs/`, report paths,
  crosswalk filenames, temporary run directories, branch names, or validator
  implementation details.

The package text should explain guardrails in customer-readable language. Internal
IDs remain in the manifest, crosswalks, validation reports, and registers outside the
package.

## AID Selection Decision Path

AID-derived content counts against the same 20-file global limit. The final package
therefore integrates selected AID material into the existing topical files instead of
adding a dedicated AID Markdown file.

| Candidate | Stage 4 handling |
| --- | --- |
| `AID-000001` | Select topic-level stabilized English content only when it maps to a package topic and has file-level source routes. Preserve Korean-source-verified or link-validated labels. |
| `AID-000002` | Select Korean-core FAQE verified content only when it strengthens a package topic and preserves per-file link-validation labels. |
| `AID-000003` | Use only as English-only auxiliary material with explicit source-confidence wording; do not present it as Korean-source-verified. |
| `AID-000004` | Use as the primary AID `llm-reference/` working source for selected topics, preserving English-only and source-limitation labels. |
| `AID-000005` | Treat as a review input and consolidation candidate, not a separate upload file. If reused, integrate selected content into the 20 topical files and count no new file. |

Evidence-only AID rows, accepted limitations, coverage ledgers, audit reports, and
source-stabilization reports stay outside upload content unless a later scoped job
intentionally converts a small portion into customer-facing text and records the route.

## Guardrail Carry-Forward

The upload package must carry these guardrails through text, manifest fields, and
crosswalk evidence:

- `APB-000014` remains deferred. Stage 4 may include source-backed validation and test
  checklist guidance already present in other playbooks, but it must not claim a
  complete customer-facing test-generation playbook until a later job creates one or
  records final exclusion.
- `CONF-000004` keeps exact admin, backup/recovery, platform, property, and protected
  operation claims gated by exact source routes and customer evidence.
- `CONF-000005` keeps exact SQL, property, view, function, data type, and error maps
  gated by exact source routes.
- `CONF-000006` keeps client, API, tool, connector, third-party, installed-file, and
  runtime claims gated by source routes and live customer evidence.
- `CONF-000007` keeps release, patch, AID composition, and final upload readiness as
  downstream decisions with exact source and validation evidence.
- `CONF-000008` is closed only as a Stage 1 routing blocker; item-level claims still
  require exact source IDs, source-pack blocks, and recheck handling.
- `CONF-000009` remains a nonblocking exclusion. `SRC-000109` and `SRC-000169` must
  not be used as authoritative upload-package content unless a later source-authority
  decision permits it.

## Manifest Schema

`GPTs/reports/stage_04_upload_package_manifest.tsv` is the planned upload file map.
Rows may reference future paths under `GPTs/upload_package/`, but this scaffold job
must not create those paths.

Required columns:

| Column | Meaning |
| --- | --- |
| `upload_file_id` | Stable package row ID, `UPKG-000` through `UPKG-019`. |
| `upload_path` | Future repository-relative upload Markdown path. |
| `source_attachment_path` | Stage 3 attachment file used as the starting answer-ready source. |
| `upload_title` | Customer-facing title. |
| `package_role` | Topic responsibility for the file. |
| `owning_stage4_job` | First Stage 4 assembly job expected to populate the file. |
| `assembly_status` | Current state; this job uses `planned_not_assembled`. |
| `counts_against_20` | Whether the row counts toward the global upload limit. |
| `merge_policy` | Whether the file preserves the attachment filename or replaces/merges it. |
| `required_sections` | Required top-level section names for the future upload Markdown. |
| `source_route_expectation` | Source-pack route expectations for item-level claims. |
| `baseline_route_expectation` | Korean-aligned English route expectations and hidden IDs. |
| `playbook_route_expectation` | Playbook route expectations and deferred test-generation handling. |
| `attachment_route_expectation` | Attachment-to-upload relationship. |
| `aid_candidate_routes` | AID candidate rows that may feed the topic. |
| `aid_integration_policy` | How AID content is selected, integrated, or deferred. |
| `allowed_source_metadata` | Source metadata allowed inside upload Markdown. |
| `internal_ids_excluded_from_upload` | Internal IDs that must stay outside upload Markdown. |
| `guardrail_ids_carried` | Guardrails preserved by manifest, crosswalks, or package text. |
| `apb_000014_disposition` | Test-generation disposition for the row. |
| `excluded_source_ids` | Explicitly excluded source IDs. |
| `validation_status` | Scaffold or assembly validation state. |
| `notes` | Deterministic assembly notes. |

## Crosswalk Expectations

Later Stage 4 jobs should create these crosswalks after upload files exist:

- `GPTs/reports/source_pack_to_upload_package_crosswalk.tsv`
- `GPTs/reports/korean_aligned_english_to_upload_package_crosswalk.tsv`
- `GPTs/reports/playbook_to_upload_package_crosswalk.tsv`
- `GPTs/reports/attachment_to_upload_package_crosswalk.tsv`

The source-pack crosswalk must resolve every exposed `SRC-*`, `AID-SRC-*`, and
`BLOCK-*` route to `GPTs/source_pack/source_manifest.tsv` and
`GPTs/source_pack/source_to_shard_manifest.tsv`. The baseline crosswalk must resolve
all `KAE-BLOCK-*` working routes while keeping those IDs outside upload Markdown. The
playbook crosswalk must resolve all task routes, carry `APB-000014` as deferred, and
preserve protected-operation guardrails. The attachment crosswalk must show which
Stage 3 file and sections feed each upload file.

## Deterministic Validation Approach

`GPTs/reports/scripts/validate_upload_package.py` validates the scaffold now and the
assembled package later.

Scaffold-mode checks:

- manifest columns, row count, row IDs, unique future upload paths, and exact 20-file
  policy;
- source attachment existence and filename preservation;
- required section policy recorded for every row;
- AID candidate coverage for `AID-000001` through `AID-000005`;
- carry-forward of `APB-000014`, `CONF-000004` through `CONF-000009`, and excluded
  `SRC-000109` and `SRC-000169`;
- no assembled `GPTs/upload_package/*.md` files in this scaffold job.

Assembled-mode checks should additionally validate:

- Markdown file count is 20 or fewer and every file is listed in the manifest;
- required sections are present;
- source IDs and block IDs used in upload files resolve through crosswalks;
- forbidden internal IDs, report paths, local paths, `.codex-jobs/`, and temporary
  run paths do not leak into upload Markdown;
- CJK prose does not appear in English upload files, except exact technical tokens if
  explicitly allowed by a later source-backed note;
- Markdown links between upload files resolve and no local filesystem links are used;
- excluded source IDs are absent from authoritative upload content;
- AID labels and limitations are preserved;
- source, baseline, playbook, and attachment crosswalks match the manifest.

## Current Deferrals

- The first operational upload Markdown slice is assembled by `S4-J003`; remaining topic files are deferred to later Stage 4 assembly jobs.
- Final AID content selection is deferred to `S4-J008` after topical package files
  exist.
- Crosswalk generation to actual upload files is deferred to `S4-J009`.
- Retrieval and answerability dry-run gates remain deferred to `S4-J010`.
- Stage 4 readiness remains deferred to `S4-J011`.
