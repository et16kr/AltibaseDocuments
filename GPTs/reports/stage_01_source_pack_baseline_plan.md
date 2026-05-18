# Stage 1 Source Pack And Korean-Aligned English Baseline Plan

Job: `S1-J001`
Status: design and schema contract
Created: 2026-05-18
Scope: Stage 1 source-pack and baseline contract only

## Reconfirmed Requirement And Boundary

`S1-J001` defines the Stage 1 contracts for source selection, exact source-pack
extraction, AID tiering, conflict recording, and the Korean-aligned English working
baseline. This job does not generate the full source pack, does not create baseline
content, does not edit customer-facing attachments, and does not assemble the final
upload package.

The Stage 1 subphase order is:

```text
source selection -> exact source-pack extraction -> source-pack validation -> Korean-aligned English baseline -> alignment validation
```

Later Stage 1 jobs must use repository-relative paths when writing repository files.
`~/AID` paths must be recorded as `~/AID/...` or `AID:<relative path>` in manifest
fields so the package remains portable across local checkouts.

## Design Note

The repository is moving from answer-ready attachments alone to a layered knowledge
system. Stage 1 provides the durable evidence contracts for that system:

- `GPTs/source_pack/` preserves selected source Markdown exactly, including
  repository-local sources and approved AID sources.
- `GPTs/reports/` records support evidence, decisions, AID tiering, validation, and
  conflict or recheck records.
- `GPTs/korean_aligned_english/` holds derived English working text aligned to Korean
  authority, or reused AID Korean-source-updated English when classification permits.

GPTs/reports/ files are support evidence only when explicitly listed in the source manifest.
Support reports may guide source selection, validation, and conflict resolution, but
they do not override selected product manuals, release notes, patch notes, technical
documents, tool manuals, third-party guides, or approved AID source records.

Source-pack exact extraction cannot be replaced by the English baseline. The source
pack remains the exact-original evidence layer, while the Korean-aligned English
baseline is a derived working layer for downstream playbooks, attachments, and final
upload-package drafting.

AID Korean-source-updated English may be reused only with preserved classification evidence.
AID evidence-only authority files, accepted limitations, English-only
auxiliary rows, legacy attachment labels, and recheck or conflict rows must keep their
classification boundaries in all downstream manifests.

## Durable Inputs Read For This Contract

- `AGENTS.md`
- `GPTs/reports/customer_agent_enablement_requirements.md`
- `GPTs/reports/source_inventory.md`
- `evals/altibase_answerability/README.md`
- `GPTs/reports/catalog_schema_extraction_rules.md`
- `~/AID/source-stabilization/source-classification.tsv`
- `~/AID/source-stabilization/validation-report.md`
- `~/AID/llm-reference/00-source-classification.md`
- `~/AID/llm-reference/coverage/source-inventory.tsv`
- `~/AID/llm-reference/coverage/omissions-and-risks.tsv`

## Stage 1 Outputs

Later jobs in Stage 1 should create or update these files according to the schemas
below:

- `GPTs/source_pack/source_manifest.tsv`
- `GPTs/source_pack/source_exclusion_register.tsv`
- `GPTs/source_pack/source_to_shard_manifest.tsv`
- `GPTs/reports/aid_tier_manifest.tsv`
- `GPTs/korean_aligned_english/baseline_manifest.tsv`
- `GPTs/reports/source_conflict_register.md`

This plan is the controlling design note for those files until a later committed
design explicitly supersedes it.

## Source Selection Contract

Source selection must produce a deterministic selected-source set before extraction.
The selected set must include all source files needed for the top-level customer and
agent enablement requirement, or record an explicit exclusion or limitation.

Default repository-local candidate roots:

- `Manuals/`
- `ReleaseNotes/`
- `PatchNotes/`
- `Technical Documents/`
- `3rd Party Guide for Altibase/`
- approved support reports under `GPTs/reports/` only when selected as support
  evidence in `GPTs/source_pack/source_manifest.tsv`

Default AID candidate roots:

- `~/AID/arch/Home/`
- `~/AID/FAQE/Home/`
- `~/AID/llm-reference/`
- `~/AID/DOCK/Home/`
- `~/AID/faq/Home/`
- `~/AID/source-stabilization/`
- `~/AID/semantic-coverage/`
- `~/AID/KO_EN_SEMANTIC_COVERAGE_REPORT.md`
- `~/AID/KO_EN_DOC_REVIEW_REPORT.md`
- `~/AID/PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `~/AID/manifest.json`

A source candidate must be assigned exactly one of these Stage 1 decisions:

| Decision | Meaning | Required record |
| --- | --- | --- |
| `include_exact` | Include exact Markdown in the source pack. | `source_manifest.tsv` and `source_to_shard_manifest.tsv` |
| `include_support_evidence` | Include as support evidence, not customer-facing product source. | `source_manifest.tsv` with `source_role=support_evidence` |
| `exclude_duplicate` | Excluded because another selected source preserves the same material. | `source_exclusion_register.tsv` |
| `exclude_out_of_scope` | Excluded because it is outside the selected corpus or current version scope. | `source_exclusion_register.tsv` |
| `exclude_low_information` | Excluded because evidence records it as low-information or non-answerable. | `source_exclusion_register.tsv` |
| `accepted_limitation` | Not expanded because the source itself lacks downloadable, textual, or verifiable detail. | `source_exclusion_register.tsv` and, for AID, `aid_tier_manifest.tsv` |
| `conflict_or_recheck` | Blocked from upload-content use until conflict or evidence weakness is resolved. | `source_conflict_register.md` and, for AID, `aid_tier_manifest.tsv` |

## Exact Source-Pack Extraction Contract

Exact extraction must preserve the selected Markdown source bytes inside stable source
boundaries. Extraction may normalize only the wrapper, shard ordering metadata, and
manifest metadata. It must not silently omit headings, code fences, tables, notes,
warnings, SQL, commands, sample output, paths, comments, or low-frequency tokens inside
the selected source.

Recommended source block wrapper:

```text
<!-- SOURCE_BLOCK_BEGIN source_id="<source_id>" source_path="<path>" sha256="<sha256>" -->
<exact source Markdown bytes decoded as UTF-8 or recorded source encoding>
<!-- SOURCE_BLOCK_END source_id="<source_id>" -->
```

Checksum rules:

- `source_sha256` is calculated on the original file bytes.
- `extracted_body_sha256` is calculated on the exact source body inside the wrapper,
  after decoding and re-encoding rules are recorded.
- For normal UTF-8 Markdown, `extracted_body_sha256` must equal `source_sha256`.
- Wrapper markers are not part of `source_sha256`.
- If a source cannot be decoded safely as UTF-8, the extraction job must record the
  encoding decision and stop unless a reversible conversion rule is documented.

Shard rules:

- Every included source ID must appear in exactly one source-pack shard.
- Every shard must have deterministic ordering by source family, version scope,
  source origin, and source path unless a later extraction job records a stronger
  ordering rule.
- Upload-intended shards count against the final 20 Markdown file upload limit.
- Evidence-only shards remain outside `GPTs/upload_package/` unless intentionally
  transformed or copied into the final upload package and listed in its manifest.

## Korean-Aligned English Baseline Contract

The baseline is a derived English working layer. It must not weaken source authority.
Repository-local paired Korean and English sources use Korean authority for conflicts
and missing details, with English sources used as wording and extraction aids when
consistent.

Baseline entries may be created from:

- paired repository-local Korean and English manuals or documents;
- Korean-only repository-local sources translated and normalized into English with
  source references;
- AID Korean-source-updated English sources when the AID classification evidence
  supports reuse;
- English-only auxiliary sources only when explicitly labeled and bounded as auxiliary.

Baseline entries must not be created from:

- unresolved conflict records;
- AID `recheck_required` rows;
- accepted source limitations that do not provide the missing fact;
- support reports that are not explicitly selected in `source_manifest.tsv`;
- generic database, Oracle, connector, platform, or third-party assumptions.

## Source Manifest Schema

File: `GPTs/source_pack/source_manifest.tsv`

Purpose: canonical list of selected source files and approved support evidence.

Primary key: `source_id`

Required columns:

| Column | Required | Allowed values or format | Rule |
| --- | --- | --- | --- |
| `source_id` | yes | Stable ID such as `SRC-000001` or `AID-000001` | Never reuse after deletion; record replacements separately. |
| `source_origin` | yes | `repo`, `aid` | Identifies repository-local or `~/AID` source. |
| `source_path` | yes | Repository-relative path or `~/AID/...` | Do not store machine-specific absolute paths except `~/AID`. |
| `source_role` | yes | `product_source`, `release_note`, `patch_note`, `tool_manual`, `technical_document`, `third_party_guide`, `support_evidence`, `aid_source`, `aid_evidence` | `GPTs/reports/` entries must use `support_evidence`. |
| `source_family` | yes | Existing source-family ID or new documented ID | Must align with coverage and benchmark taxonomy where possible. |
| `title` | yes | Text | Human-readable source title. |
| `version_scope` | yes | `7.1`, `7.3`, `8.1_verified`, exact patch, `multi`, `aid`, or `unknown` | `unknown` requires a note and downstream guardrail. |
| `language` | yes | `ko`, `en`, `ko+en`, `mixed`, `n/a` | Customer-facing output still remains English unless explicitly required. |
| `authority_label` | yes | Text from source policy | Examples: `Korean authoritative`, `English extraction aid`, `Altibase 8.1 verified source`, `AID Korean-source-verified`. |
| `aid_classification` | conditional | AID class or blank | Required for `source_origin=aid`. |
| `classification_evidence` | conditional | Path list | Required for AID sources and support evidence. |
| `selection_decision` | yes | `include_exact`, `include_support_evidence` | Excluded candidates belong in the exclusion register. |
| `extraction_mode` | yes | `exact_markdown`, `support_evidence_only` | `support_evidence_only` cannot become customer source text by itself. |
| `source_sha256` | yes | SHA-256 hex | Calculated from original file bytes. |
| `byte_count` | yes | Integer | Original file byte count. |
| `line_count` | yes | Integer | Original file line count. |
| `estimated_tokens` | yes | Integer | Deterministic estimator chosen by extraction job. |
| `selected_by_job` | yes | Job ID | First job that selected the source. |
| `last_verified_job` | yes | Job ID | Latest job that verified the row. |
| `notes` | no | Text | Keep concise; use conflict register for disputes. |

Validation rules:

- Each included source has one and only one row.
- `source_path` values are unique unless one physical file is intentionally represented
  by multiple source IDs for separate version-scoped blocks; that exception requires a
  note and a shard manifest cross-reference.
- Every `GPTs/reports/` source row must state `source_role=support_evidence`.
- Every AID row must preserve `aid_classification` and `classification_evidence`.

## Source Exclusion Register Schema

File: `GPTs/source_pack/source_exclusion_register.tsv`

Purpose: auditable record for candidate sources not included as exact source-pack
content or approved support evidence.

Primary key: `exclusion_id`

Required columns:

| Column | Required | Allowed values or format | Rule |
| --- | --- | --- | --- |
| `exclusion_id` | yes | Stable ID such as `EXC-000001` | Never reuse. |
| `candidate_origin` | yes | `repo`, `aid` | Source location class. |
| `candidate_path` | yes | Repository-relative path or `~/AID/...` | Candidate file or directory. |
| `source_family` | yes | Source-family ID or `unknown` | `unknown` requires rationale. |
| `version_scope` | yes | Version, patch, `aid`, `multi`, or `unknown` | Preserve version uncertainty. |
| `language` | yes | `ko`, `en`, `mixed`, `n/a` | Use `n/a` only for non-text evidence. |
| `exclusion_type` | yes | `duplicate`, `out_of_scope`, `low_information`, `non_markdown`, `accepted_source_limitation`, `evidence_only`, `conflict_pending`, `recheck_required` | Drives downstream eligibility. |
| `exclusion_reason` | yes | Text | Must be specific enough for reviewer verification. |
| `evidence_ref` | yes | Path, source ID, or conflict ID | Points to the evidence justifying exclusion. |
| `replacement_source_id` | conditional | Source ID or blank | Required for duplicates. |
| `aid_tier` | conditional | AID tier or blank | Required for `candidate_origin=aid`. |
| `risk_label` | yes | `none`, `low`, `medium`, `high`, `blocker` | Conflicts or rechecks should not be `none`. |
| `selected_by_job` | yes | Job ID | Job that made the decision. |
| `review_status` | yes | `draft`, `accepted`, `superseded`, `recheck_required` | Only `accepted` rows are final exclusions. |
| `notes` | no | Text | Keep concise. |

Validation rules:

- An excluded candidate must not also appear as `include_exact` in
  `source_manifest.tsv` unless the exclusion row is `superseded`.
- `accepted_source_limitation` rows must not be used to infer missing facts.
- `conflict_pending` and `recheck_required` rows block final upload-content use until
  resolved.

## Source-To-Shard Manifest Schema

File: `GPTs/source_pack/source_to_shard_manifest.tsv`

Purpose: deterministic mapping from selected sources to source-pack shard files and
source boundary blocks.

Primary key: `source_id`

Required columns:

| Column | Required | Allowed values or format | Rule |
| --- | --- | --- | --- |
| `source_id` | yes | Existing source ID | Must exist in `source_manifest.tsv`. |
| `shard_id` | yes | Stable ID such as `SHARD-001` | Deterministic shard identifier. |
| `shard_path` | yes | `GPTs/source_pack/<file>.md` | Repository-relative path. |
| `block_id` | yes | Stable ID such as `BLOCK-000001` | Unique source block ID. |
| `order_in_shard` | yes | Integer | 1-based order in the shard. |
| `source_start_line` | yes | Integer | Usually `1` for whole-file exact extraction. |
| `source_end_line` | yes | Integer | Original source line count for whole-file extraction. |
| `source_sha256` | yes | SHA-256 hex | Must match `source_manifest.tsv`. |
| `extracted_body_sha256` | yes | SHA-256 hex | Must match source body after extraction rules. |
| `block_byte_count` | yes | Integer | Exact body byte count. |
| `block_line_count` | yes | Integer | Exact body line count. |
| `block_estimated_tokens` | yes | Integer | Deterministic token estimate. |
| `shard_estimated_tokens` | yes | Integer | Total shard token estimate. |
| `upload_intended` | yes | `yes`, `no`, `candidate` | `yes` and final `candidate` count toward upload planning. |
| `validation_status` | yes | `pending`, `pass`, `fail` | Final Stage 1 validation requires `pass`. |
| `notes` | no | Text | Use conflict register for disputes. |

Validation rules:

- Every `include_exact` source in `source_manifest.tsv` appears exactly once.
- No `source_id` maps to more than one shard row unless a later design adds explicit
  split-block support.
- Shard token and byte totals must leave margin below GPT Knowledge limits chosen by
  the upload-package stage.
- `upload_intended=yes` shard files must be counted against the global final upload
  package limit of 20 Markdown files if copied or transformed into
  `GPTs/upload_package/`.

## AID Tier Manifest Schema

File: `GPTs/reports/aid_tier_manifest.tsv`

Purpose: preserve AID upload role, classification evidence, and downstream eligibility.

Primary key: `aid_source_id`

Required columns:

| Column | Required | Allowed values or format | Rule |
| --- | --- | --- | --- |
| `aid_source_id` | yes | Stable ID such as `AID-000001` | May match `source_manifest.tsv` when included. |
| `aid_path` | yes | `~/AID/...` or AID-relative path | Must identify the AID file or evidence row. |
| `aid_tier` | yes | `upload_content_candidate`, `evidence_only_authority`, `accepted_limitation`, `conflict`, `recheck` | Controls downstream use. |
| `source_class` | yes | `Korean-source-verified`, `Link-validated Korean-source-verified`, `English-only source`, `english_only_auxiliary`, `source_limitation`, `legacy_attachment_label_only`, `diagram_unavailable`, `not_document_format`, `recheck_required`, or documented equivalent | Preserve exact AID evidence label when available. |
| `coverage_status` | yes | `covered`, `covered_with_risk`, `accepted_source_limitation`, `accepted_english_only_auxiliary`, `complete`, `missing`, `unverified`, `recheck_required`, or documented equivalent | Preserve AID coverage state. |
| `classification_evidence` | yes | Path list | Usually AID stabilization or llm-reference coverage files. |
| `allowed_downstream_use` | yes | Text or controlled phrase | Examples: `primary_working_source`, `support_evidence_only`, `auxiliary_labeled_only`, `blocked_until_recheck`. |
| `required_label` | yes | Text | Label that downstream content must carry. |
| `source_manifest_action` | yes | `include_exact`, `include_support_evidence`, `exclude_register`, `conflict_register`, `recheck_register` | Links AID tier to source selection. |
| `source_id` | conditional | Source ID or blank | Required when included in source manifest. |
| `exclusion_id` | conditional | Exclusion ID or blank | Required when excluded. |
| `conflict_id` | conditional | Conflict ID or blank | Required for `aid_tier=conflict` or `recheck`. |
| `last_verified_job` | yes | Job ID | Latest job that checked the row. |
| `notes` | no | Text | Keep concise. |

Validation rules:

- AID upload-content candidates must preserve source classification and evidence links.
- AID evidence-only authority files are not customer upload content by default.
- AID English-only auxiliary material must not be relabeled as Korean-source-verified.
- AID accepted limitations must remain limitations and must not be expanded into
  unsupported customer-facing content.
- AID conflict or recheck rows block baseline, playbook, attachment, and final upload
  use until resolved or explicitly accepted as residual risk.

## Korean-Aligned English Baseline Manifest Schema

File: `GPTs/korean_aligned_english/baseline_manifest.tsv`

Purpose: track Korean-aligned English baseline inventory blocks, downstream baseline
generation candidates, and their source authority.

S1-J006 implementation refinement: the first committed manifest is an inventory of
repository-local selected source groups, not derived baseline prose. It creates one
stable `baseline_block_id` for each normalized Korean/English source pair, Korean-only
source, English-only source, and selected no-language-tree source. Later baseline text
generation may extend this manifest or add a content manifest with `baseline_path`,
content checksums, and generated block line counts after the English baseline text
exists.

Primary key: `baseline_block_id`

Required columns:

| Column | Required | Allowed values or format | Rule |
| --- | --- | --- | --- |
| `baseline_block_id` | yes | Stable ID such as `KAE-BLOCK-000001` | One inventory block for a normalized pair, unpaired source, no-language-tree source, or not-ready gate row. |
| `korean_source_id` | conditional | Source ID list or blank | Required for repository-local Korean authority rows. |
| `korean_source_path` | conditional | Repository-relative path list or blank | Required when `korean_source_id` is present. |
| `english_source_id` | conditional | Source ID list or blank | Required when an English extraction-aid row exists. |
| `english_source_path` | conditional | Repository-relative path list or blank | Required when `english_source_id` is present. |
| `other_source_id` | conditional | Source ID list or blank | Records selected repository sources that have no `kor` or `eng` path segment. |
| `other_source_path` | conditional | Repository-relative path list or blank | Required when `other_source_id` is present. |
| `source_family` | yes | Source-family ID | Align with source manifest. |
| `version_scope` | yes | `7.1`, `7.3`, `8.1_verified`, exact patch, tool/release scope inherited from `source_manifest.tsv`, `multi`, `aid`, or `unknown` | `unknown` requires guardrail. |
| `authority_label` | yes | Source authority label list | Preserve Korean authoritative, English extraction-aid, and `Altibase 8.1 verified source` wording. |
| `baseline_source_type` | yes | `repo_paired_ko_en`, `repo_ko_only`, `repo_en_only`, `repo_no_language_tree`, `aid_reuse`, `hybrid`, `not_ready` | Describes inventory and derivation path. |
| `planned_downstream_use` | yes | Controlled phrase | Examples: `primary_working_source_after_alignment`, `translation_candidate_after_alignment`, `blocked_until_korean_authority_or_auxiliary_label`, `source_pack_only_not_korean_aligned`, `blocked_until_source_pack_validation_passes`. |
| `alignment_status` | yes | `pending`, `aligned`, `conflict`, `recheck`, `excluded`, `aid_reuse`, `not_ready` | Only aligned, aid-reuse, or explicitly approved pending rows may become downstream inputs after later validation. |
| `source_block_refs` | yes | Source ID plus source-pack block and line refs | Must be reviewable against `source_to_shard_manifest.tsv`. |
| `evidence_or_limitation_note` | yes | Text | Records pairing evidence, missing counterpart, exclusion reason, or validation blocker. |
| `last_verified_job` | yes | Job ID | Latest alignment validation job. |

Validation rules:

- A baseline inventory row must trace back to source manifest rows, source-pack block
  refs, AID tier rows, or a source-pack validation blocker row.
- Baseline text cannot serve as proof of exact source inclusion.
- Destructive, security-sensitive, version-sensitive, or conflict-prone claims require
  source references back to Korean authority or accepted AID classification evidence.
- `conflict`, `recheck`, `excluded`, and `not_ready` rows are not eligible for
  customer-facing downstream generation.
- Unpaired Korean-only and English-only selected sources must appear in the manifest
  and must not be silently dropped.

## Source Conflict Register Schema

File: `GPTs/reports/source_conflict_register.md`

Purpose: human-reviewable register for Korean/English source drift, AID/manual
conflicts, weak evidence, source limitations that affect answerability, and recheck
items.

The register should use one Markdown table per status group or a single table with
these required columns:

| Column | Required | Allowed values or format | Rule |
| --- | --- | --- | --- |
| `Conflict ID` | yes | Stable ID such as `CONF-000001` | Referenced by manifests. |
| `Status` | yes | `open`, `resolved`, `accepted_limitation`, `accepted_residual_risk`, `superseded` | Open conflicts block downstream use. |
| `Severity` | yes | `Blocker`, `High`, `Medium`, `Low`, `Info` | Use review severity language. |
| `Source IDs` | yes | Source ID list | Include AID source IDs when applicable. |
| `Paths` | yes | Path list | Repository-relative or `~/AID/...`. |
| `Version Scope` | yes | Version, patch, `aid`, `multi`, or `unknown` | Preserve version boundary. |
| `Conflict Type` | yes | `ko_en_drift`, `aid_manual_conflict`, `source_variation`, `weak_evidence`, `missing_source`, `source_limitation`, `recheck_required` | Choose the most specific type. |
| `Finding` | yes | Text | State the exact conflict or evidence weakness. |
| `Authority Policy` | yes | Text | State which source authority policy applies. |
| `Resolution Or Next Check` | yes | Text | Must be actionable. |
| `Downstream Guardrail` | yes | Text | How playbooks, attachments, or upload package must handle it. |
| `Owner Job` | yes | Job ID | Job responsible for resolution or acceptance. |
| `Last Reviewed` | yes | Date or job ID | Keep current. |

Validation rules:

- Every `conflict_or_recheck`, `conflict_pending`, `recheck_required`, S1-J006
  `conflict`, or S1-J006 `recheck` manifest row must have a conflict register entry.
- Resolved rows must state the source-backed resolution and downstream guardrail.
- Accepted limitations must preserve the limitation instead of inventing missing
  details.

## Validation Gates For Later Stage 1 Jobs

### Gate 1: Source Selection

- `source_manifest.tsv` exists and validates against the schema.
- `source_exclusion_register.tsv` exists and validates against the schema.
- Every selected source candidate is included, excluded, or blocked by conflict or
  recheck record.
- `GPTs/reports/` support evidence is selected only through `source_manifest.tsv`.
- AID tiering is complete before any AID content is packaged.

### Gate 2: Exact Source-Pack Extraction

- Every `include_exact` source appears in exactly one source-pack shard.
- Original source checksums match manifest rows.
- Extracted body checksums match original source content under the recorded extraction
  rule.
- Source boundary markers are present and well-formed.
- No baseline or summary output is accepted as a substitute for exact source-pack
  extraction.

### Gate 3: Source-Pack Validation

- `source_to_shard_manifest.tsv` validates inclusion, uniqueness, ordering, and
  checksum rules.
- Shard byte and token estimates are recorded.
- Upload-intended shard candidates are counted against the final 20-file upload limit.
- Evidence-only shards remain outside `GPTs/upload_package/` unless intentionally
  transformed or copied into that package and listed in the final upload manifest.

### Gate 4: Korean-Aligned English Baseline

- `baseline_manifest.tsv` exists before baseline content is used downstream.
- Every baseline block traces to selected source IDs, AID tier rows, or both.
- Korean authority is used for repository-local paired Korean/English conflicts.
- AID reuse preserves classification evidence and required labels.
- English-only auxiliary material stays explicitly labeled and bounded.

### Gate 5: Alignment Validation

- No downstream-eligible baseline row has unresolved conflict or recheck status.
- Conflict register entries exist for all unresolved source drift, weak evidence, or
  AID/manual conflicts.
- Destructive, security-sensitive, version-sensitive, and patch-sensitive generated
  material retains source references and missing-input guardrails.
- Validation output is recorded under `GPTs/reports/` as support evidence only when
  explicitly selected in the source manifest.

## Targeted Verification For S1-J006

`GPTs/korean_aligned_english/scripts/build_baseline_manifest.py --check` must verify
that `source_pack_validation.md` records `Status: pass`, `Verdict: Pass`, no source-pack
validation blockers, and the Korean-aligned English continuation gate before baseline
inventory rows are accepted. It must also verify normalized `kor`/`eng` pair detection,
distinguishable `7.1`, `7.3`, and `8.1_verified` rows, complete selected-source ID
coverage, and explicit rows for unpaired Korean-only and English-only sources.

Required targeted commands:

```bash
python3 GPTs/korean_aligned_english/scripts/build_baseline_manifest.py --check
python3 GPTs/source_pack/scripts/validate_source_pack.py --check
git diff --check -- GPTs/korean_aligned_english GPTs/reports/stage_01_source_pack_baseline_plan.md
```

## Targeted Verification For S1-J001

This design note is documentation-only. The required verification for this job is:

```bash
rg -n "GPTs/reports/ files are support evidence only when explicitly listed in the source manifest" GPTs/reports/stage_01_source_pack_baseline_plan.md
rg -n "Source-pack exact extraction cannot be replaced by the English baseline" GPTs/reports/stage_01_source_pack_baseline_plan.md
rg -n "AID Korean-source-updated English may be reused only with preserved classification evidence" GPTs/reports/stage_01_source_pack_baseline_plan.md
git diff --check -- GPTs/reports/stage_01_source_pack_baseline_plan.md
```

Later implementation jobs should add executable validators for the TSV and Markdown
schemas once those files are created.
