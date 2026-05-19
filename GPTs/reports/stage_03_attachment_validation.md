# Stage 3 Attachment Validation

- Job: `S3-J017`
- Date: 2026-05-19
- Scope: retrieval aliases, cross-links, source/playbook-to-attachment crosswalks,
  gap-register disposition, and attachment validation evidence
- Verdict: Pass after final clean-worktree validation

## Requirement And Boundary

`S3-J017` consolidates Stage 3 attachment follow-up after the domain remediation
jobs. It updates only Stage 3 routing evidence, targeted attachment retrieval
anchors, validation checks, and gap-register dispositions.

This job does not edit original sources, does not run scenario tests, does not
assemble or modify `GPTs/upload_package/`, and does not close `APB-000014`.
`APB-000014` remains a planned/deferred test-generation playbook route because no
committed source-ID-backed `GPTs/agent_playbooks/test_generation.md` playbook exists.

## Design Note

This job changes validation behavior and documentation structure by adding three
Stage 3 attachment crosswalks and making the attachment validator require those
routes for completed Stage 3 target attachments:

- `GPTs/reports/source_pack_to_attachment_crosswalk.tsv`
- `GPTs/reports/korean_aligned_english_to_attachment_crosswalk.tsv`
- `GPTs/reports/playbook_to_attachment_crosswalk.tsv`

Attachment content architecture is unchanged. The only customer-facing edits are
targeted retrieval-alias and cross-reference anchors for Java/JDBC, DB Link,
utilities/AKU, Kubernetes/AKU, and Spatial/NiFi/Tableau handoffs.

## Domain Job Disposition

All domain remediation rows in
`GPTs/reports/stage_03_attachment_followup_scope.tsv` are complete:

| Area | Result |
| --- | --- |
| Scope rows | `14` rows, `S3-SCOPE-001` through `S3-SCOPE-014` |
| Current status | all `done` |
| Expected disposition | all `attachment_update` |
| Owning domain jobs | `S3-J003` through `S3-J016` |
| Attachment route coverage | all `20` customer-facing attachments have source-pack, Korean-aligned English, and playbook crosswalk routes |

## Crosswalk Summary

| Crosswalk | Rows | Attachment coverage | Scope coverage |
| --- | ---: | ---: | ---: |
| `source_pack_to_attachment_crosswalk.tsv` | 383 | 20 attachments | 14 scope rows |
| `korean_aligned_english_to_attachment_crosswalk.tsv` | 541 | 20 attachments | 14 scope rows |
| `playbook_to_attachment_crosswalk.tsv` | 157 | 20 attachments | 14 scope rows |

The crosswalks are generated from the completed Stage 3 scope ledger and the
validated Stage 1/2 manifests. They are route evidence, not permission to skip exact
source checks for item-level production commands, SQL, code, APIs, patch behavior,
or live-environment claims.

## Gap Register Disposition

`GPTs/reports/agent_playbook_gap_register.md` now records:

- `APG-S2-J012-001` remains open for `APB-000014` test generation.
- `APG-S2-J012-004` is partially closed for Stage 3 attachment integration and
  crosswalk routing, while scenario execution, AID upload composition, and final
  upload-package assembly remain downstream work.

Scenario files remain validation scenarios with `Not run` placeholders. This job did
not run, judge, or report scenario-test outcomes.

## Verification Results

| Command or check | Result |
| --- | --- |
| `python3 GPTs/attachments/scripts/validate_attachments.py` | Pass; attachment count, required sections, customer-facing path/internal-label scan, 8.1 wording, upload-package boundary, scope TSV, exact-token checks, and Stage 3 crosswalk routes passed. |
| `python3 GPTs/agent_playbooks/scripts/validate_playbooks.py` | Pass after the final clean-worktree rerun. A pre-commit run failed only because the Stage 2 validator intentionally rejects uncommitted attachment changes. |
| Edited attachment source/playbook route check | Pass; all 20 Stage 3-edited customer-facing attachments have source and playbook routes in the Stage 3 crosswalks. |
| Customer-facing attachment local-path/internal-label scan | Pass; no repository-local path, source ID, source-pack block ID, shard ID, Korean-aligned block ID, or local workspace path was found in customer-facing attachments. |
| `git diff --name-only 5538c9a8 -- GPTs/upload_package` | Pass; no Stage 3 upload-package paths changed. |
| `git diff --check -- GPTs/attachments GPTs/reports GPTs/agent_playbooks` | Pass. |

## Self-Review

- Overbroad readiness claims: avoided. This report validates Stage 3 attachment
  routing only, not final upload readiness.
- Source-policy drift: avoided. Crosswalks preserve source, baseline, playbook,
  guardrail, and protected-topic routes; exact item-level claims still require
  source rechecks and missing-input prompts.
- `APB-000014` handling: preserved as deferred and not counted as complete.
- Scenario handling: no scenario tests are declared as run.
- Upload-package boundary: preserved; no `GPTs/upload_package/` changes were made.
