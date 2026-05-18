# AID, Version, Release, And Patch Routing Playbook

- Playbook ID: `APB-000017`
- Owning job: `S2-J009`
- Validation status: `pass`
- Supported versions: Altibase 7.1, Altibase 7.3, `Altibase 8.1 verified source`,
  selected release-note tool scopes, and classified AID routes
- Protected topic: yes

## Source Routes

Use this playbook when a customer, GPT, or coding agent must decide which source
route is allowed before using AID-derived material, release-note text, patch-note
tokens, version-history rows, or accepted limitations in a downstream answer or
generated artifact. It is a routing and recheck playbook, not an exhaustive patch
translation or final upload-package decision.

| Route | Source IDs | Source-pack block refs | Baseline blocks |
| --- | --- | --- | --- |
| Product release and version boundaries | `SRC-000424`, `SRC-000425`, `SRC-000426`, `SRC-000450`, `SRC-000451`, `SRC-000452`, `SRC-000477` | `SRC-000424/BLOCK-000819`, `SRC-000425/BLOCK-000822`, `SRC-000426/BLOCK-000827`, `SRC-000450/BLOCK-000821`, `SRC-000451/BLOCK-000824`, `SRC-000452/BLOCK-000826`, `SRC-000477/BLOCK-000829` | `KAE-BLOCK-000275` |
| 7.1 and 7.3 version-history routing | `SRC-000228`, `SRC-000397` | `SRC-000228/BLOCK-000615`, `SRC-000397/BLOCK-000784` | `KAE-BLOCK-000022`, `KAE-BLOCK-000157`, `KAE-BLOCK-000275` |
| Technical version and compatibility checks | `SRC-000473`, `SRC-000474`, `SRC-000475`, `SRC-000476` | `SRC-000473/BLOCK-000562`, `SRC-000474/BLOCK-000909`, `SRC-000475/BLOCK-000910`, `SRC-000476/BLOCK-000911` | `KAE-BLOCK-000231`, `KAE-BLOCK-000240`, `KAE-BLOCK-000241`, `KAE-BLOCK-000242`, `KAE-BLOCK-000275` |
| Replication Manager release-note boundaries | `SRC-000443`, `SRC-000444`, `SRC-000445`, `SRC-000464`, `SRC-000465`, `SRC-000466` | `SRC-000443/BLOCK-000836`, `SRC-000444/BLOCK-000838`, `SRC-000445/BLOCK-000840`, `SRC-000464/BLOCK-000837`, `SRC-000465/BLOCK-000839`, `SRC-000466/BLOCK-000841` | `KAE-BLOCK-000287` |
| AID tier and limitation evidence | `AID-000001`, `AID-000002`, `AID-000003`, `AID-000004`, `AID-000005`, `AID-000006`, `AID-000015`, `AID-000016`, `AID-000022`, `AID-000023`, `AID-000025`, `AID-000028` | `BLOCK-000454`, `BLOCK-000457`, `BLOCK-000459`, `BLOCK-000460`, `BLOCK-000429`, `BLOCK-000433`, `BLOCK-000431`, `BLOCK-000432` | `KAE-BLOCK-000276` |
| AID `llm-reference/` working sources | `AID-SRC-000423`, `AID-SRC-000424`, `AID-SRC-000425`, `AID-SRC-000426`, `AID-SRC-000427`, `AID-SRC-000428`, `AID-SRC-000429`, `AID-SRC-000430`, `AID-SRC-000431`, `AID-SRC-000432`, `AID-SRC-000433`, `AID-SRC-000434`, `AID-SRC-000435`, `AID-SRC-000436`, `AID-SRC-000437`, `AID-SRC-000438` | `BLOCK-000451`, `BLOCK-000453`, `BLOCK-000448`, `BLOCK-000436`, `BLOCK-000437`, `BLOCK-000438`, `BLOCK-000439`, `BLOCK-000440`, `BLOCK-000441`, `BLOCK-000442`, `BLOCK-000443`, `BLOCK-000444`, `BLOCK-000445`, `BLOCK-000446`, `BLOCK-000447`, `BLOCK-000452` | `KAE-BLOCK-000276` |

Guardrails: `CONF-000001`, `CONF-000002`, `CONF-000004`, `CONF-000005`,
`CONF-000006`, `CONF-000007`, `CONF-000008`, and `CONF-000009`. `CONF-000004`
through `CONF-000007` remain open recheck gates. `CONF-000008` is closed only
as a Stage 1 routing blocker; item-level procedures and APIs still need exact
source sections. `CONF-000009` remains an accepted limitation excluding
`SRC-000109` and `SRC-000169` from authoritative customer-facing use.

## Required Customer Inputs

Collect these inputs before using this routing playbook to approve an answer or
generated artifact:

- `target_version`, exact patch level, and whether the claim targets 7.1,
  7.3, or `Altibase 8.1 verified source`.
- Requested claim type: AID-derived answer, `llm-reference/` use, release-note
  availability, patch-specific behavior, `BUG-*` or `TASK-*` token lookup,
  version-history lookup, platform support, Java compatibility, replication
  compatibility, or final upload-package selection.
- Exact source ID, source path, release-note version, patch-note version,
  `BUG-*` token, `TASK-*` token, or AID tier row when the user already has one.
- Runtime evidence when a claim depends on installed binaries, such as
  `V$VERSION`, tool version output, JAR/package names, `altierr` output,
  logs, object definitions, platform details, or customer validation results.
- AID source label when AID is involved, including `Korean-source-verified`,
  `Link-validated Korean-source-verified`, `English-only source`,
  `english_only_auxiliary`, `source_limitation`,
  `accepted_source_limitation`, or `accepted_english_only_auxiliary`.
- Packaging intent, including whether the content is only internal evidence or
  is being proposed for the final global 20 Markdown file upload package.

If any input is missing, ask for it and provide the safest source-backed next
check instead of widening a release, patch, AID, platform, or compatibility
claim.

## Generated Artifacts

This playbook may generate routing matrices, source recheck plans, version
boundary notes, patch-token evidence packets, AID classification decisions, and
upload-package decision notes. It must not generate final production SQL,
commands, code, platform guarantees, compatibility guarantees, or upload-package
composition by itself.

### Routing decision template

```text
routing_decision:
  target_version: <7.1|7.3|8.1_verified|tool_release|aid>
  patch_level: <exact patch or unknown>
  requested_claim: <availability|patch_behavior|BUG|TASK|platform|AID|upload>
  source_ids: <SRC/AID/AID-SRC ids>
  source_pack_blocks: <BLOCK ids or SRC/BLOCK pairs>
  baseline_blocks: <KAE-BLOCK ids>
  authority_label: <Korean authoritative|English extraction aid|Altibase 8.1 verified source|AID label>
  guardrails: <CONF ids>
  missing_inputs: <exact inputs still required>
  allowed_output: <guarded first draft|evidence-only note|accepted limitation|stop>
  next_check: <exact source recheck, customer evidence request, or packaging review>
```

### Patch-token evidence packet

```text
patch_token_packet:
  token: <BUG-*|TASK-*>
  token_type: <bug|task>
  product_line: <7.1|7.3|Replication Manager>
  patch_or_tool_release: <exact release>
  source_id: <exact source>
  source_block: <exact block>
  authority: <Korean authoritative|English extraction aid|Repository source evidence>
  customer_runtime_evidence: <V$VERSION, tool version, logs, or unknown>
  allowed_claim: <token appears in this source only|behavior requires source section>
```

### AID tier decision packet

```text
aid_decision:
  aid_tier_row: <AID-000001..AID-000028 or AID-SRC row>
  aid_tier: <upload_content_candidate|evidence_only_authority|accepted_limitation>
  source_class: <exact aid_tier_manifest source_class>
  required_label: <exact aid_tier_manifest required_label>
  downstream_use: <allowed_downstream_use from aid_tier_manifest>
  package_count_effect: <counts against global 20 Markdown file limit|evidence only>
  stop_if: <English-only relabeled, evidence-only promoted, limitation invented>
```

## AID Classification Rules

Use only the AID tier classifications recorded in
`GPTs/reports/aid_tier_manifest.tsv`:

| Tier or row | Required handling |
| --- | --- |
| `AID-000001` | `upload_content_candidate`; `primary_working_source_after_file_level_source_manifest_selection`; required label: AID stabilized English; preserve per-file Korean-source-verified or Link-validated Korean-source-verified labels |
| `AID-000002` | `upload_content_candidate`; `primary_working_source_after_file_level_source_manifest_selection`; required label: AID Korean-core FAQE verified source; preserve per-file link-validation labels |
| `AID-000003` | `upload_content_candidate`; `auxiliary_labeled_only`; required label: English-only source or english_only_auxiliary; do not present as Korean-source-verified |
| `AID-000004` | `upload_content_candidate`; `primary_working_source`; required label: AID source-backed llm-reference with preserved labels including English-only source labels |
| `AID-000005` | `upload_content_candidate`; `upload_package_candidate_for_review`; required label: AID GPTS_UPLOAD_READY; counts toward global 20 Markdown upload limit if selected |
| `AID-000006` | `evidence_only_authority`; `support_evidence_only`; required label: Optional internal audit evidence |
| `AID-000015` | `accepted_limitation`; `support_evidence_only`; required label: legacy_no_downloadable_url or legacy_attachment_label_only; do not invent URLs |
| `AID-000016` | `accepted_limitation`; `support_evidence_only`; required label: Preserve preserved_url rows; keep legacy_no_downloadable_url and not_document_format limitations |
| `AID-000022` | `accepted_limitation`; `support_evidence_only`; required label: Preserve source limitation and English-only auxiliary labels |
| `AID-000023` | `accepted_limitation`; `support_evidence_only`; required label: Do not invent unavailable diagrams, synthetic URLs, or non-document artifact content |
| `AID-000025` | `accepted_limitation`; `support_evidence_only`; required label: Preserve accepted limitation and accepted English-only auxiliary labels |
| `AID-000028` | `evidence_only_authority`; `support_evidence_only`; required label: AID GPTs packaging evidence |

Do not schedule or imply a blanket Korean-to-English rewrite pass for AID. Use
stabilized English and source-backed `llm-reference/` rows when their labels
permit it, and preserve evidence-only and accepted-limitation rows as evidence
or limitations unless a later packaging job records an explicit decision.

## Procedure

1. Classify the request. Route AID material through `KAE-BLOCK-000276`, release
   and patch material through `KAE-BLOCK-000275`, and Replication Manager
   release-note material through `KAE-BLOCK-000287`.
2. Confirm the source authority. Korean manuals, Korean release notes, Korean
   patch notes, Korean technical documents, and Korean third-party guides are
   authoritative where selected. English sources are extraction aids unless an
   AID classification explicitly permits labeled English-only auxiliary use.
3. Preserve exact version boundaries. Release-note claims for
   `7.1.0.1.2 (Released)`, `7.3.0.0.1 (Released)`, or `8.1.0.0.1` stay at
   that exact version unless another source explicitly broadens the scope.
4. For 8.1-only material, preserve the wording `Altibase 8.1 verified source`
   and do not backport features to 7.1 or 7.3 without exact source evidence.
5. For patch-note work, preserve `BUG-*` and `TASK-*` tokens exactly. Examples
   such as `BUG-49398`, `BUG-48885`, `BUG-47805`, and `BUG-47873` are token
   anchors, not proof of broad behavior outside their exact source rows.
6. For version-history work, keep the table fields as table fields:
   `database binary version`, `meta version`, `CM protocol version`, and
   `replication protocol version`. Treat `CM protocol version` as the
   communication/protocol token recorded by the version-history source.
7. For replication compatibility, use `SRC-000475` and ask for both server
   versions, replication mode, topology, current state, and whether eager mode
   or offline replication is involved before applying a compatibility row.
8. For AID, preserve the recorded tier and source class. Upload-content
   candidates can support guarded working content; evidence-only rows support
   audit and source tracing; accepted limitations remain limitations.
9. If a selected AID source conflicts with a selected Altibase manual, release
   note, patch note, or technical document, record a conflict or recheck item
   and resolve it with the active Korean-authoritative source policy before
   using the claim.

## Guardrails

- `CONF-000004`: do not use this route to claim exhaustive admin operations,
  production recovery, platform support, property values, TLS samples, or
  protected operations without exact target-version source blocks and customer
  evidence.
- `CONF-000005`: do not use this route to claim exhaustive SQL grammar,
  property tables, view columns, data type behavior, error-code maps, or
  patch-specific SQL behavior without the exact source section.
- `CONF-000006`: do not use technical documents, third-party guides, or
  release notes to assert live client, tool, Java, connector, Kubernetes, NiFi,
  Tableau, or GUI compatibility without installed-version evidence.
- `CONF-000007`: do not claim exhaustive 7.1 or 7.3 patch behavior, final AID
  upload readiness, or complete platform/package table conversion from
  `KAE-BLOCK-000275` or `KAE-BLOCK-000276` alone.
- `CONF-000008`: closed as a Stage 1 routing blocker only. Exact procedures,
  APIs, command options, tuning, source-index behavior, and Replication
  Manager workflows still require exact source-section and customer-evidence
  checks.
- `CONF-000009`: keep `SRC-000109` and `SRC-000169` out of authoritative
  customer-facing playbooks, attachments, and upload-package text unless a
  later source-authority decision records paired Korean authority or approved
  auxiliary use.
- AID accepted limitations from `CONF-000001` and English-only residual risk
  from `CONF-000002` stay visible whenever source confidence matters.

## Validation Checks

Before handing off a version, release, patch, or AID routing answer, verify:

- The answer includes source IDs, source-pack block refs, baseline block IDs,
  and guardrail IDs.
- AID labels come from `GPTs/reports/aid_tier_manifest.tsv`; no invented AID
  tier, source class, or downstream use label is introduced.
- Version-history claims preserve `database binary version`, `meta version`,
  `CM protocol version`, and `replication protocol version`.
- Release-note claims preserve exact release versions and do not broaden
  `Altibase 8.1 verified source` material to 7.1 or 7.3.
- Patch-token claims preserve exact `BUG-*` or `TASK-*` spelling, patch
  version, source ID, and authority label.
- Platform, Java, replication, tool, and third-party claims include the
  required customer runtime evidence or stop at a source-backed next check.
- Any proposed upload use counts AID-derived Markdown against the single global
  20 Markdown file upload limit.

Use this local verification when a changed playbook mentions AID classifications:

```bash
python3 GPTs/agent_playbooks/scripts/validate_playbooks.py
rg -n "upload_content_candidate|evidence_only_authority|accepted_limitation|English-only source|source_limitation|llm-reference" GPTs/agent_playbooks
```

## Stop Conditions

Stop and ask for more evidence if:

- The target version or patch level is missing for a release-note, patch-note,
  version-history, platform, or compatibility claim.
- The request asks for all `BUG-*` or `TASK-*` behavior from the selected
  corpus without a scoped token, patch, source row, or extraction task.
- The answer depends on installed binaries, live package availability,
  download URLs, tool help, Java/JRE files, OS minor versions, logs, object
  definitions, replication state, or validation output that has not been
  supplied.
- An AID `evidence_only_authority` or `accepted_limitation` row is being
  converted into customer upload content without an explicit packaging
  decision.
- An `English-only source` or `english_only_auxiliary` row is being presented
  as `Korean-source-verified`.
- A `source_limitation`, `legacy_no_downloadable_url`, `diagram_unavailable`,
  or `not_document_format` row is being expanded into invented content.
- A patch behavior is being backported to an earlier patch or broadened to all
  7.1, all 7.3, or all 8.1 without exact source evidence.

## Cleanup And Handoff

For this routing playbook, cleanup means preserving the decision trail rather
than reverting runtime state. Archive the source route, missing-input list,
guardrail IDs, and exact customer evidence used. If a downstream artifact later
generates runnable SQL, commands, code, or configuration, hand off to the
focused domain playbook and keep rollback or cleanup requirements there.
