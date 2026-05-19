# Agent Playbook Gap Register

- Created: 2026-05-18
- Updated: 2026-05-19
- Current job: `S3-J017`
- Status: Stage 2/3 playbook validation and attachment-route gap register

## Reconfirmed Requirement And Boundary

`S2-J012` validates Stage 2 playbook source routes, baseline routes, crosswalks, and
remaining gaps. It does not edit original sources, `GPTs/attachments/`, or
`GPTs/upload_package/`, and it does not create missing domain playbooks outside the
crosswalk and validation-report scope.

This register extends the Stage 1 `S1-J012` / `S1R-J006` gap record. Stage 1 remains
ready/pass for guarded Stage 2 routing. `CONF-000008` stays closed only as a Stage 1
routing blocker, and `CONF-000009` stays a nonblocking exclusion guardrail.
No open Stage 2 blockers remain for `CONF-000008` or `CONF-000009`.
CONF-000009 remains a nonblocking exclusion guardrail.

`S3-J017` updates only the Stage 3 attachment-routing disposition. It does not run
scenario tests, does not create a source-ID-backed test-generation playbook, and does
not assemble `GPTs/upload_package/` content.

## Current Validation Snapshot

Evidence sources:

- `GPTs/agent_playbooks/playbook_manifest.tsv`
- `GPTs/reports/source_pack_to_playbook_crosswalk.tsv`
- `GPTs/reports/korean_aligned_english_to_playbook_crosswalk.tsv`
- `GPTs/source_pack/source_manifest.tsv`
- `GPTs/source_pack/source_to_shard_manifest.tsv`
- `GPTs/korean_aligned_english/baseline_manifest.tsv`
- `GPTs/reports/aid_tier_manifest.tsv`

| Check | Result |
| --- | --- |
| Manifest rows | 17 |
| Manifest rows at `validation_status=pass` | 16 |
| Manifest rows at `validation_status=planned` | 1 |
| Required domains with a manifest route or recorded gap | 14 of 14 |
| Source-to-playbook crosswalk rows | 444 |
| Unique source-pack source IDs in source-to-playbook crosswalk | 265 |
| Korean-aligned English-to-playbook crosswalk rows | 127 |
| Unique baseline block IDs in baseline-to-playbook crosswalk | 86 |
| AID tier route IDs recorded separately from source-pack source IDs | 12 |

Rows marked with residual risks are usable only for guarded first drafts. They do
not authorize exhaustive, production-ready, patch-definitive, live-environment, or
final-upload claims.

## Not-Ready Blockers

| Gap ID | Status | Severity | Scope | Evidence | Required handling |
| --- | --- | --- | --- | --- | --- |
| APG-S2-J012-001 | Open | Medium | `APB-000014` / Test generation | `playbook_manifest.tsv` keeps `APB-000014` at `validation_status=planned`; it has baseline block routes but no source IDs, no source-pack block IDs, and no `GPTs/agent_playbooks/test_generation.md` playbook file. The scenario-test suite exists in `test_scenarios.md`, but that is not a source-backed generated-test playbook. `S3-J017` rechecked this condition and did not close it. | Before declaring complete Stage 2 playbook readiness, create a source-ID-backed test-generation playbook or record an explicit readiness decision that test generation remains deferred. Until then, use the existing scenario tests only as validation scenarios, not as a customer-facing test-generation playbook. |

## Accepted Limitations

| Gap ID | Status | Severity | Scope | Evidence | Required handling |
| --- | --- | --- | --- | --- | --- |
| APG-S2-J012-002 | Accepted limitation | Low | AID source limitations, untranslated extraction-aid snippets, and English-only stored-procedure media exclusions | Carries forward `CONF-000001`, `CONF-000003`, and `CONF-000009`. `CONF-000009` keeps `SRC-000109` and `SRC-000169` excluded from authoritative customer-facing playbook, attachment, and upload-package text. | Preserve source-limitation labels, avoid copying Korean prose from extraction aids into customer-facing playbooks, and keep excluded English-only media rows out of authoritative generated artifacts unless a later source-authority decision changes the route. |

## Residual Risks

| Gap ID | Status | Severity | Scope | Evidence | Required handling |
| --- | --- | --- | --- | --- | --- |
| APG-S2-J012-003 | Open guardrail | Medium | Exact item-level admin, SQL/reference, client/tool, release/patch/AID, and `CONF-000008` remediation-scope claims | Carries forward `CONF-000002`, `CONF-000004`, `CONF-000005`, `CONF-000006`, `CONF-000007`, and the Stage 1 routing-closed but item-level guarded `CONF-000008`. These guardrails appear in the playbook manifest and both crosswalks. | Use playbooks only for guarded first drafts unless exact source blocks, target version, patch level, installed tool output, runtime state, logs, object definitions, validation evidence, and rollback or cleanup evidence are available for the requested artifact. |

## Downstream Stage 3/4 Work

| Gap ID | Status | Severity | Scope | Evidence | Required handling |
| --- | --- | --- | --- | --- | --- |
| APG-S2-J012-004 | Partially closed; open downstream work | Low | Answer-ready attachment integration, scenario execution, AID upload composition, and final upload package assembly | Stage 3 domain attachment integration rows are `done`, and `S3-J017` generated source-pack, Korean-aligned English, and playbook-to-attachment crosswalks plus attachment validation evidence. The final GPT Knowledge package still must be assembled later under the global 20 Markdown file limit. Scenario rows are defined with `Not run` placeholders. AID upload-content candidates remain governed by `CONF-000007`. | Treat Stage 3 attachment crosswalk integration as closed for this gap. Stage 3/4 still must run or judge scenario coverage where required, preserve AID labels, choose final upload files, and revalidate the final package before upload readiness. |

## Carry-Forward Stage 1 Gap Closure

| Gap ID | Status | Severity | Source IDs | Baseline IDs | Conflict ID | Stage 2 handling |
| --- | --- | --- | --- | --- | --- | --- |
| APG-S1-J012-001 | Closed | Info | `GPTs/reports/stage_01_readiness_remediation_scope.tsv` rows for `CONF-000008` | `KAE-BLOCK-000277` through `KAE-BLOCK-000286`; `KAE-BLOCK-000287` for Replication Manager release-note boundaries | `CONF-000008` | Stage 2 may route through these baselines only with exact source IDs, source-pack blocks, missing-input prompts, customer evidence, and recheck guardrails. |
| APG-S1-J012-002 | Nonblocking | Low | `SRC-000109`; `SRC-000169` | `KAE-BLOCK-000279` | `CONF-000009` | Keep these rows excluded from authoritative customer-facing playbooks, attachments, and upload-package text unless later Korean authority or approved auxiliary use is recorded. |

## AID Downstream Disposition Check

| AID tier row | Disposition |
| --- | --- |
| `AID-000001` | Upload-content candidate after file-level source-manifest selection; preserve Korean-source-verified or link-validated labels. |
| `AID-000002` | Upload-content candidate after file-level source-manifest selection; preserve Korean-core FAQE verification labels. |
| `AID-000003` | English-only auxiliary upload-content candidate; preserve `CONF-000002` and source-confidence labels. |
| `AID-000004` | Primary AID `llm-reference/` working source with preserved labels. |
| `AID-000005` | AID GPT upload-package candidate for later review; counts against the global 20 Markdown file limit if selected. |

## Self-Review Notes

- Not-ready blockers: `APB-000014` is the only planned, source-pack-unitemized
  playbook row found by `S2-J012`.
- Accepted limitations: `CONF-000009` remains visible and nonblocking; no playbook
  row uses `SRC-000109` or `SRC-000169` as a source route.
- Residual risks: open guardrails are intentionally preserved in the manifest and
  crosswalks instead of being downgraded to readiness claims.
- Downstream work: final attachment/upload-package integration and scenario execution
  remain outside this job.
