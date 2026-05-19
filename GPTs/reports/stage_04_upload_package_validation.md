# Stage 4 Upload Package Validation

- Job: `S4-J009`
- Date: 2026-05-19
- Scope: deterministic upload-package manifest, crosswalk, boundary, and leakage
  validation after assembly
- Verdict: Pass for deterministic package validation; final live benchmark readiness
  is not claimed

## Boundary Reconfirmation

`S4-J009` validates the assembled Stage 4 upload package and its route evidence. It
does not add upload Markdown files, broaden customer-facing Altibase behavior, edit
source manuals, mark `APB-000014` complete, or claim final live benchmark readiness.

The final upload-package boundary remains exactly the 20 Markdown files under
`GPTs/upload_package/`. Manifests, crosswalks, validation reports, scripts, source
pack shards, Korean-aligned English baselines, playbooks, attachments, AID evidence
ledgers, and benchmark reports remain outside the upload package unless transformed
into one of those 20 files and listed in the manifest.

## Design Note

This job changes deterministic validation behavior, not customer-facing product
content. `GPTs/reports/scripts/validate_upload_package.py` now validates not only
manifest shape and Markdown leakage, but also route-row integrity for the
source-pack, Korean-aligned English, playbook, and attachment upload crosswalks.

New checks verify upload file ID/path consistency, crosswalk status values,
source-pack source/block resolution, one attachment route per package file,
`APB-000014` deferral rows, baseline/playbook ID non-exposure policy, stale assembly
placeholder text, balanced fenced code blocks, and preservation of the `Altibase 8.1
verified source` wording where 8.1 appears.

Historical note: `S4-J002` added the original validation scaffold and scaffold mode;
later package assembly jobs used progressive and assembled modes. This report now
records the current assembled-package validation state for `S4-J009`.

## S4-J008 Final AID Decision

`S4-J008` records the final AID upload-content routing decision without increasing the
20-file upload package. AID-derived material remains inside the existing topical
package architecture only when an exact source route and source label support the
claim. No separate AID Markdown upload file is added.

Design note: this job changes the Stage 4 documentation state from deferred AID
selection to final routing. It does not add a new upload-package file, broaden AID
authority, convert accepted limitations into facts, or change customer-facing
Altibase behavior.

| AID row | Final Stage 4 disposition |
| --- | --- |
| `AID-000001` | Selected as labeled source-route evidence and exact-source support for future topic-level use; no independent AID prose was added to upload Markdown in this job. Preserve Korean-source-verified and link-validated labels. |
| `AID-000002` | Selected as labeled Korean-core FAQE evidence and exact-source support for future topic-level use; no independent AID prose was added to upload Markdown in this job. Preserve per-file verification labels. |
| `AID-000003` | Deferred to labeled auxiliary use only. English-only auxiliary material must keep the `English-only source` or `english_only_auxiliary` label and must not be presented as Korean-source-verified. |
| `AID-000004` | Selected as the primary AID `llm-reference/` working source for routing and recheck support, with Korean-source-verified, link-validated, English-only, and source-limitation labels preserved. |
| `AID-000005` | Explicitly excluded as a separate upload file because it would inflate the global 20 Markdown file limit. It may be used only as consolidation review evidence outside the upload package. |

Accepted AID limitations remain limitations, not upload facts. `CONF-000001` carries
legacy attachment, unavailable diagram, non-document-format, source variation, and
accepted English-only auxiliary limitations. `CONF-000002` carries English-only
auxiliary residual risk. `CONF-000004` through `CONF-000007` remain open guardrails
for exact operational, SQL/reference, client/tool, release/patch, AID, and live
environment claims. `CONF-000008` remains resolved only as a Stage 1 routing blocker;
item-level upload-package claims still require exact source routes and recheck
handling. `CONF-000009` remains a nonblocking exclusion, so `SRC-000109` and
`SRC-000169` stay out of authoritative upload-package content.

`APB-000014` remains finally deferred for Stage 4: upload Markdown may include
validation checks, negative-case cautions, smoke checks, and cleanup notes, but it must
not claim a complete customer-facing source-backed test-generation playbook.

## Scaffold Mode

Default validator mode checks:

- `stage_04_upload_package_plan.md`, `stage_04_upload_package_manifest.tsv`, and this
  validation note exist;
- the manifest has exactly 20 planned rows and no row outside the global 20-file
  limit;
- every planned upload path is under `GPTs/upload_package/`, ends in `.md`, and maps
  one-to-one to an existing Stage 3 attachment filename;
- every row records the required upload sections;
- every row records source-pack, baseline, playbook, attachment, AID, guardrail,
  excluded-source, and `APB-000014` disposition fields;
- the union of AID candidate routes covers `AID-000001` through `AID-000005`;
- the union of guardrail routes covers `CONF-000004` through `CONF-000009`;
- `SRC-000109` and `SRC-000169` are recorded as excluded source IDs;
- `GPTs/upload_package/` is absent or contains no Markdown files.

Historical `S4-J002` result: pass in scaffold mode, with all manifest rows reported as
`planned_not_assembled`. Current `S4-J008` validation uses assembled mode because the
20 upload Markdown files now exist.


## Progressive Assembly Mode

During topic-by-topic Stage 4 assembly, run:

```bash
python3 GPTs/reports/scripts/validate_upload_package.py --assembled --allow-partial
```

Progressive mode validates the assembled slice while allowing future manifest rows to
remain `planned_not_assembled`. It still enforces the global 20-file limit, required
sections, forbidden internal ID and local-path scans, source ID and block ID
resolution, and source-pack, Korean-aligned English, playbook, and attachment
crosswalk rows for every assembled upload file.

## Assembled Mode

After `S4-J003` through `S4-J008` create or update all package files, run:

```bash
python3 GPTs/reports/scripts/validate_upload_package.py --assembled
```

Assembled mode should require:

- 20 or fewer Markdown files under `GPTs/upload_package/`;
- every assembled upload Markdown file listed in the manifest;
- every manifest row at an assembled or intentionally deferred status;
- all required top-level sections present;
- upload Markdown source IDs and block IDs resolving through the source-pack
  manifest and source-pack-to-upload crosswalk;
- no forbidden local path, report path, `.codex-jobs/`, branch, temporary run,
  `KAE-BLOCK-*`, `APB-*`, `CONF-*`, `S3-SCOPE-*`, or job ID leakage;
- no CJK prose leakage in English upload files, except any later explicitly
  source-backed technical-token exception;
- no local filesystem links or broken relative links between upload files;
- no authoritative use of `SRC-000109` or `SRC-000169`;
- AID labels and limitations preserved where selected;
- attachment, source-pack, Korean-aligned English, and playbook crosswalks matching
  the assembled files.

## Deterministic Check Matrix

| Check | Scaffold mode | Assembled mode | Failure handling |
| --- | --- | --- | --- |
| File count | Validate 20 planned manifest rows and no assembled files. | Validate 20 or fewer assembled Markdown files and manifest coverage; progressive mode allows future rows to remain planned. | Do not add files beyond the limit; merge or defer content. |
| Required sections | Validate section list in manifest. | Validate actual Markdown headings. | Add missing headings before readiness. |
| Source routes | Validate source-route expectation fields. | Resolve exposed `SRC-*`, `AID-SRC-*`, and `BLOCK-*` routes through crosswalks. | Add route, remove unsupported claim, or defer. |
| Internal ID leakage | Validate policy fields. | Scan upload Markdown for disallowed IDs and paths. | Move IDs to reports/crosswalks or rewrite as customer-readable guardrails. |
| CJK leakage | Not applicable before assembly. | Scan upload Markdown for CJK ranges. | Translate or remove unsupported prose while preserving exact tokens. |
| Broken upload links | Not applicable before assembly. | Resolve relative `.md` links inside `GPTs/upload_package/`. | Fix link target or remove the link. |
| Excluded sources | Validate manifest records exclusions. | Scan upload Markdown for authoritative excluded-source references. | Remove content or record approved source-authority decision. |
| Upload boundary hygiene | Require no upload Markdown in this scaffold job. | Require all upload files live only under `GPTs/upload_package/`. | Move non-upload artifacts outside the package. |
| AID selection | Validate candidate decision path. | Verify selected AID labels and limitations. | Preserve label, defer row, or exclude content. |

## Required Checks For This Scaffold Job

Run these commands before committing `S4-J002`:

```bash
rg -n "Verdict:|Stage 3 workflow ledger|Blocker|Not ready|ready/pass" GPTs/reports/stage_04_preflight_status.md
python3 GPTs/attachments/scripts/validate_attachments.py
python3 GPTs/agent_playbooks/scripts/validate_playbooks.py
python3 GPTs/reports/scripts/validate_upload_package.py
git status --short -- GPTs/upload_package
git diff --check -- GPTs/reports/stage_04_upload_package_plan.md GPTs/reports/stage_04_upload_package_manifest.tsv GPTs/reports/stage_04_upload_package_validation.md GPTs/reports/scripts
```

The preflight scan is expected to show the existing assembly blocker until the
orchestrator reconciles the Stage 3 workflow ledger. That blocker prevents upload
assembly, not this scaffold-only contract.

## Required Checks For S4-J008

`S4-J008` must run the package validator in assembled mode plus the AID guardrail
checks required by the job:

```bash
python3 GPTs/korean_aligned_english/scripts/validate_alignment.py
python3 GPTs/agent_playbooks/scripts/validate_playbooks.py --skip-forbidden-git-edits
python3 GPTs/reports/scripts/validate_upload_package.py --assembled
rg -n "[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uac00-\ud7af]" GPTs/upload_package/*.md
git diff --check -- GPTs/upload_package GPTs/reports/stage_04_upload_package_manifest.tsv GPTs/reports/korean_aligned_english_to_upload_package_crosswalk.tsv GPTs/reports/stage_04_upload_package_validation.md GPTs/reports/agent_playbook_gap_register.md GPTs/reports/source_conflict_register.md
```

Expected result: the first three commands pass, the Korean-prose scan returns no
matches, and `git diff --check` returns no whitespace errors.

## S4-J008 Verification Result

Result on 2026-05-19: pass.

| Check | Result |
| --- | --- |
| `python3 GPTs/korean_aligned_english/scripts/validate_alignment.py` | Pass |
| `python3 GPTs/agent_playbooks/scripts/validate_playbooks.py --skip-forbidden-git-edits` | Pass |
| `python3 GPTs/reports/scripts/validate_upload_package.py --assembled` | Pass; 20 manifest rows and 20 upload Markdown files validated. |
| CJK leakage scan over `GPTs/upload_package/*.md` | Pass; no CJK leakage found. |
| Scoped `git diff --check` | Pass |

## S4-J009 Current Crosswalk Summary

`S4-J009` keeps the assembled package at exactly 20 upload Markdown files and
validates the current route evidence outside the package:

| Artifact | Current count | Validation handling |
| --- | ---: | --- |
| `GPTs/upload_package/*.md` | 20 | Counted upload files; all are listed in the manifest and have required sections. |
| `stage_04_upload_package_manifest.tsv` | 20 rows | All rows are `assembled`, count against the global 20-file limit, carry final AID policy tokens, carry `APB-000014` deferral, and list `SRC-000109` plus `SRC-000169` as excluded. |
| `source_pack_to_upload_package_crosswalk.tsv` | 262 rows | Every row matches a manifest ID/path, has `route_status=pass`, resolves its `SRC-*` and `BLOCK-*` route, and does not route excluded sources. |
| `korean_aligned_english_to_upload_package_crosswalk.tsv` | 28 rows | Every row matches a manifest ID/path, remains crosswalk-only, and keeps baseline IDs out of upload Markdown. |
| `playbook_to_upload_package_crosswalk.tsv` | 109 rows | Every row matches a manifest ID/path; non-deferred playbook routes are `pass`/`routed`, and each package file keeps `APB-000014` as `planned`, `deferred_not_uploaded`, and `deferred_guardrail`. |
| `attachment_to_upload_package_crosswalk.tsv` | 20 rows | Exactly one attachment route exists per package file and matches the manifest source attachment path. |

No relative Markdown links are present in the upload package, so there are no
non-upload support references to record. Future relative `.md` links must either
resolve inside `GPTs/upload_package/` or remain outside customer upload Markdown and
be recorded in support reports.

## Required Checks For S4-J009

`S4-J009` must run the upload-package validator plus the upstream layer validators
required by the job:

```bash
python3 GPTs/reports/scripts/validate_upload_package.py --assembled
python3 GPTs/attachments/scripts/validate_attachments.py --skip-upload-package-gate
python3 GPTs/agent_playbooks/scripts/validate_playbooks.py --skip-forbidden-git-edits
python3 GPTs/source_pack/scripts/validate_source_pack.py --check
python3 GPTs/korean_aligned_english/scripts/validate_alignment.py
git diff --check -- GPTs/upload_package GPTs/reports/stage_04_upload_package_manifest.tsv GPTs/reports/*_to_upload_package_crosswalk.tsv GPTs/reports/stage_04_upload_package_validation.md GPTs/reports/scripts
```

Because the required source-pack check found stale committed support-evidence
metadata for `SRC-000485`, this job refreshed the deterministic source-pack
manifest, shard mapping, shard 014, validation note, and upload-order note before
rerunning the required check. The refresh does not add upload files and does not make
the source pack upload-intended.

## S4-J009 Verification Result

Result on 2026-05-19: pass.

| Check | Result |
| --- | --- |
| `python3 GPTs/reports/scripts/validate_upload_package.py --assembled` | Pass; 20 manifest rows, 20 upload Markdown files, required sections, crosswalk route integrity, excluded-source handling, AID limitation labels, stale-placeholder scan, and CJK scan passed. |
| `python3 GPTs/attachments/scripts/validate_attachments.py --skip-upload-package-gate` | Pass; 20 customer-facing attachment files, required sections, internal-label scan, exact-token checks, and Stage 3 routes passed. Upload-package dirty-worktree gate was intentionally skipped for this Stage 4 job. |
| `python3 GPTs/agent_playbooks/scripts/validate_playbooks.py --skip-forbidden-git-edits` | Pass; 17 manifest rows, 14/14 required domains route-or-gap, 13/14 pass rows, and one planned placeholder for `APB-000014`. |
| `python3 GPTs/source_pack/scripts/validate_source_pack.py --check` | Pass after deterministic support-evidence refresh; 941 selected sources, 16 shards, and 8,767 exclusions validated. |
| `python3 GPTs/korean_aligned_english/scripts/validate_alignment.py` | Pass; baseline manifest, AID classification preservation, conflict/recheck coverage, Korean leakage, and unsupported-inference scans passed. |
| Scoped `git diff --check` from the job request | Pass |

## Self-Review Checklist

- The package uses the existing 20 topic filenames.
- No upload-package Markdown is created or rewritten by this job.
- AID content has no separate file allocation.
- `APB-000014` remains deferred.
- `CONF-000004` through `CONF-000009` remain visible in reports and manifest fields.
- `SRC-000109` and `SRC-000169` remain excluded.
- Internal IDs are allowed in the package only where this plan explicitly permits
  source IDs and source-pack block IDs as source-boundary metadata.
- The source-pack refresh is limited to deterministic support-evidence currentness
  required by `validate_source_pack.py --check`.
