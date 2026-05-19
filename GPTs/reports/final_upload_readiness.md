# Altibase GPT Final Upload Readiness

- Updated: 2026-05-19
- Current source of truth:
  `GPTs/reports/customer_agent_enablement_stage_04_readiness.md`
- Supersedes: the 2026-05-17 `J022` attachment-only final-readiness handoff
- Status: ready/pass for live benchmark rerun only; not final GPT Knowledge upload
  readiness

## Current Decision

The current Stage 4 package is deterministically valid and ready for controlled live
benchmark rerun routing. It is not certified for final GPT Knowledge upload because no
Stage 4 package-context live benchmark pass exists.

The older `J022` report described the upload boundary as `GPTs/attachments/`. Stage 4
supersedes that boundary: final upload-intended Markdown now lives only under
`GPTs/upload_package/` and is listed in
`GPTs/reports/stage_04_upload_package_manifest.tsv`.

## Upload Package Boundary

| Check | Current result |
| --- | --- |
| Upload package directory | `GPTs/upload_package/` |
| Upload Markdown count | `20` files |
| Manifest rows | `20` rows |
| Assembly status | all rows `assembled` |
| Global file limit | all `20` rows count against the same final-upload limit |
| AID separate file | none; selected AID routes are integrated into topical files or deferred/excluded |

Support reports, manifests, crosswalks, source-pack shards, Korean-aligned English
baselines, playbooks, attachments, AID evidence ledgers, and benchmark artifacts are
not final upload files unless a later scoped job transforms them into
`GPTs/upload_package/` and lists them in the manifest.

## Validation Snapshot

Stage 4 readiness validation on 2026-05-19 passed the deterministic gates:

| Check | Result |
| --- | --- |
| Upload-package validator | Pass: `20` manifest rows and `20` upload Markdown files validated. |
| Attachment validator with upload-package gate skipped | Pass: `20` customer-facing attachments and Stage 3 routes validated. |
| Playbook validator with forbidden-git-edits gate skipped | Pass: `17` rows, `14/14` required domains route-or-gap, `13/14` pass rows, `1` planned placeholder. |
| Source-pack validator | Pass: `941` selected sources, `16` shards, `8,767` exclusions. |
| Korean-aligned English validator | Pass: `287` baseline rows plus AID classification, conflict/recheck, leakage, and unsupported-inference checks. |
| Review-stage validator | Pass: `R00` through `R27` are `Done`. |
| Scoped whitespace check | Pass for the Stage 4 upload package and readiness-report paths. |

Route evidence is current: `262` source-pack-to-upload rows pass, `28`
Korean-aligned English-to-upload rows are routed, `109` playbook-to-upload rows are
present with `20` deferred `APB-000014` guardrail rows, and `20` attachment-to-upload
rows are assembled.

## Guardrails

`APB-000014` remains deferred and is not a completed customer-facing test-generation
playbook. Scenario files remain validation scenarios with `Not run` placeholders.

`CONF-000004` through `CONF-000007` remain open guardrails for exact operational,
SQL/reference, client/tool, release/patch, AID, third-party, and live-environment
claims. `CONF-000008` is resolved only as a Stage 1 routing blocker and still requires
item-level source rechecks. `CONF-000009` remains an accepted limitation: `SRC-000109`
and `SRC-000169` are excluded from authoritative upload-package content.

## Live Benchmark Gate

No Stage 4 live benchmark was run. The latest recorded full live benchmark remains
`altibase_answerability_20260517_095919`, with `blocking_gaps`, `27/270` passed,
`10.0%` pass rate, `68.7%` critical fact coverage, `74.6%` required-token
preservation, `0.4%` unsupported-claim rate, and `77` protected-topic blockers.

`S4-J010` passed benchmark schema validation, runner self-tests, judge/report
self-tests, and the supported lexical dry-run with `270` answer records, `errors=0`,
and `0` leakage-check failures. That dry-run does not prove answer quality or
package-context behavior.

The current benchmark runner is attachment-bound. A package-context live result
requires a package-aware runner or a documented operator-approved harness that
preserves the existing leakage and allowlist controls.

## Required Next Gate

Run a controlled live benchmark rerun before any final GPT Knowledge upload claim.
Final upload readiness requires a fresh passing benchmark result under the configured
policy gates, including overall and per-domain pass rates, critical fact coverage,
required-token preservation, unsupported-claim limit, and zero protected-topic
blockers.

If the rerun fails, triage failures as content gap, retrieval gap, answer synthesis
gap, benchmark harness limitation, or judge calibration issue using repository-local
sources and the current Stage 4 package evidence. Do not lower thresholds, rewrite
expected answers, or broaden source authority to make the benchmark pass.
