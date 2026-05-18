# Stage 2 Playbook Validation

- Job: `S2-J012`
- Date: 2026-05-19
- Scope: playbook source-route validation, crosswalk evidence, and gap-register
  update
- Verdict: Pass with recorded gaps; `APB-000014` remains a not-ready blocker for a
  dedicated test-generation playbook

## Boundary Reconfirmation

`S2-J012` validates Stage 2 playbook coverage and traceability. It writes the
source-to-playbook and Korean-aligned English-to-playbook crosswalks, updates the
playbook gap register, and extends the playbook validator for the new contracts. It
does not edit original source files, `GPTs/attachments/`, or `GPTs/upload_package/`.

Prior Stage 2 jobs are accounted for: `S2-J001` through `S2-J011` are marked `Done`
in the job ledger and are committed in the current Git history before this job.

## Design Note

This job changes Stage 2 documentation structure by adding deterministic crosswalk
evidence and making that evidence part of `validate_playbooks.py`. The source
crosswalk treats `SRC-*` and `AID-SRC-*` values as source-pack source IDs that must
resolve in `GPTs/source_pack/source_manifest.tsv`; `AID-000*` values are preserved
as AID tier route IDs and validated against `GPTs/reports/aid_tier_manifest.tsv`.

The validator now checks:

- every required domain has a manifest route or a recorded gap;
- every playbook Markdown file has a `playbook_manifest.tsv` row;
- every manifest source-pack source ID resolves to `source_manifest.tsv` and
  `source_to_shard_manifest.tsv`;
- every AID tier route ID resolves to `aid_tier_manifest.tsv`;
- every Korean-aligned baseline block resolves to `baseline_manifest.tsv`;
- both crosswalk files match the current manifest routes;
- planned or source-less playbook rows are recorded in the gap register.

## Evidence Summary

| Evidence item | Result |
| --- | --- |
| Manifest rows | 17 |
| Pass rows | 16 |
| Planned rows | 1 |
| Required domains with route or recorded gap | 14 of 14 |
| Required domains with pass rows | 13 of 14 |
| Source-To-Playbook Crosswalk rows | 444 |
| Unique source-pack source IDs in source crosswalk | 265 |
| Korean-Aligned English-To-Playbook Crosswalk rows | 127 |
| Unique baseline block IDs in baseline crosswalk | 86 |
| Protected-topic manifest rows | 13 |
| AID tier route IDs preserved separately | 12 |

## Source-To-Playbook Crosswalk

`GPTs/reports/source_pack_to_playbook_crosswalk.tsv` maps each non-AID-tier
manifest source route to a playbook, source-pack shard, source-pack block, generated
artifact classes, protected-topic flag, guardrails, AID route, baseline routes, and
remaining gap classification.

Every `SRC-*` and `AID-SRC-*` route in `playbook_manifest.tsv` is represented in
the crosswalk and resolves to both `source_manifest.tsv` and
`source_to_shard_manifest.tsv`. AID tier IDs such as `AID-000001` are not source-pack
source IDs; they are carried in the `aid_tier_ids` column and validated against
`aid_tier_manifest.tsv`.

## Korean-Aligned English-To-Playbook Crosswalk

`GPTs/reports/korean_aligned_english_to_playbook_crosswalk.tsv` maps each manifest
baseline route to a playbook, source block references, baseline source type,
planned downstream use, alignment status, generated artifact classes,
protected-topic flag, guardrails, AID route, and remaining gap classification.

Every `KAE-BLOCK-*` route in `playbook_manifest.tsv` is represented in the
crosswalk and resolves to `GPTs/korean_aligned_english/baseline_manifest.tsv`.

## Required Domains

| Required domain | Manifest route | Status | Gap handling |
| --- | --- | --- | --- |
| Installation and startup | `APB-000001` | Pass | Residual exact-source and downstream upload guardrails only. |
| DDL generation | `APB-000002` | Pass | Residual exact SQL/admin source guardrails only. |
| SQL and data types | `APB-000003` | Pass | Residual exact SQL/reference source guardrails only. |
| Properties | `APB-000004` | Pass | Residual exact property/admin source guardrails only. |
| Dictionary and views | `APB-000005` | Pass | Residual exact dictionary/performance-view source guardrails only. |
| Backup and recovery | `APB-000006` | Pass | Residual exact protected-operation and AID-route guardrails only. |
| Replication and CDC | `APB-000007` | Pass | Residual topology, runtime-state, exact-source, and `CONF-000008` guardrails only. |
| Security and TLS | `APB-000008` | Pass | Residual exact TLS/security/client source guardrails only. |
| ODBC and C clients | `APB-000009` | Pass | Residual installed-client, compiler, runtime, and exact API guardrails only. |
| Java and JDBC | `APB-000010` | Pass | Residual driver, framework, runtime, and exact source guardrails only. |
| Tools | `APB-000011` | Pass | Residual installed-tool help, file, option, and AID-route guardrails only. |
| Migration and integrations | `APB-000012` | Pass | Residual third-party, tool-version, AID, and `CONF-000009` guardrails only. |
| Errors and troubleshooting | `APB-000013` | Pass | Residual log, runtime-state, exact error, and escalation guardrails only. |
| Test generation | `APB-000014` | Planned | `APG-S2-J012-001` records a not-ready blocker for a dedicated source-backed test-generation playbook. |

Additional pass playbooks provide cross-cutting routes for service-development
artifact generation (`APB-000015`), protected administration operations
(`APB-000016`), and AID/version/release/patch routing (`APB-000017`).

## Gap Register

`GPTs/reports/agent_playbook_gap_register.md` now distinguishes:

- not-ready blocker: `APG-S2-J012-001` for `APB-000014` test generation;
- accepted limitation: `APG-S2-J012-002` for carried-forward source limitations and
  `CONF-000009` exclusions;
- residual risk: `APG-S2-J012-003` for exact-source, production, patch, client/tool,
  runtime-state, and `CONF-000008` item-level guardrails;
- downstream Stage 3/4 work: `APG-S2-J012-004` for attachment/upload integration,
  scenario execution, AID upload composition, and final package readiness.

## Verification Results

| Command or check | Result |
| --- | --- |
| `python3 GPTs/agent_playbooks/scripts/validate_playbooks.py` | Pass |
| Required-domain route or gap check | Pass; 14 of 14 required domains have a manifest route or recorded gap. |
| Playbook-file manifest-row check | Pass; every playbook Markdown file has a manifest row. |
| Manifest source ID resolution | Pass; all `SRC-*` and `AID-SRC-*` routes resolve to `source_manifest.tsv`; AID tier route IDs resolve to `aid_tier_manifest.tsv`. |
| Baseline block ID resolution | Pass; all `KAE-BLOCK-*` routes resolve to `baseline_manifest.tsv`. |
| `git diff --check -- GPTs/agent_playbooks GPTs/reports/source_pack_to_playbook_crosswalk.tsv GPTs/reports/korean_aligned_english_to_playbook_crosswalk.tsv GPTs/reports/agent_playbook_gap_register.md` | Pass |

## Self-Review

- Coverage: every required domain has a route or recorded gap; `APB-000014` is the
  only planned placeholder.
- Traceability: the crosswalks resolve all source-pack and baseline IDs used by the
  manifest.
- AID handling: AID tier route IDs are not treated as source-pack block IDs; they
  remain route labels with preserved classification requirements.
- Guardrails: open guardrails remain visible as residual risks and do not become
  exhaustive or production-ready claims.
- Scope: no original sources, attachments, upload-package files, or unrelated
  workflow files were edited.
