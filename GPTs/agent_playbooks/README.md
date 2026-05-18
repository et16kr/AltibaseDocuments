# Stage 2 Agent Playbooks

- Job: `S2-J002`
- Scope: schema, manifest placeholders, validation scaffolding, and source-routing
  plan only
- Status: scaffolded before domain playbooks are drafted

## Boundary

`GPTs/agent_playbooks/` is the Stage 2 task-playbook layer. Stage 2 playbooks must
route customer and coding-agent work through the validated Stage 1 source pack,
Korean-aligned English baseline, AID classifications, and conflict guardrails.

This scaffold does not create domain playbook content. Domain rows in
`playbook_manifest.tsv` start as `planned` placeholders so later Stage 2 jobs can
fill exact source IDs, source-pack block IDs, Korean-aligned baseline block IDs, AID
routes, generated artifact types, missing-input prompts, and validation status.

Stage 2 must not edit `GPTs/attachments/` or create `GPTs/upload_package/` content.
The validator fails when those forbidden paths have uncommitted changes.

## Manifest Schema

`playbook_manifest.tsv` uses one row per planned or completed playbook route.
Columns are strict and tab-separated:

| Column | Purpose |
| --- | --- |
| `playbook_id` | Stable `APB-000000` style playbook identifier. |
| `path` | Repository-relative Markdown path under `GPTs/agent_playbooks/`. |
| `title` | Customer-facing playbook title. |
| `domain` | Required playbook domain from the requirements, or a later approved extra domain. |
| `supported_versions` | Semicolon-separated version scope such as `7.1;7.3;8.1_verified`. |
| `source_ids` | Semicolon-separated `SRC-*`, `AID-*`, or `AID-SRC-*` IDs when routed. |
| `source_pack_block_ids` | Semicolon-separated `BLOCK-*` or `SRC-*/BLOCK-*` source-pack references when itemized. |
| `korean_aligned_baseline_block_ids` | Semicolon-separated `KAE-BLOCK-*` IDs when routed. |
| `aid_route_or_tier` | AID tier, route, or `not_used_yet`. |
| `guardrail_ids` | Semicolon-separated `CONF-*` conflict or recheck guardrails. |
| `generated_artifact_types` | Semicolon-separated artifact classes the playbook may draft. |
| `protected_topic` | `yes` when generated work may be destructive, privileged, storage-changing, replication-changing, security-sensitive, or environment-dependent; otherwise `no`. |
| `required_missing_input_prompts` | Semicolon-separated input prompts that must be preserved before final artifacts. |
| `validation_status` | `planned`, `draft`, `pass`, `fail`, or `blocked`. |
| `owning_stage2_job` | Stage 2 job responsible for filling or validating the row. |
| `notes` | Short routing or limitation note. |

Rows with `validation_status=planned` are coverage placeholders. They may have
baseline or guardrail routes but are not ready playbooks, and they do not need their
future Markdown file to exist yet. Any row promoted beyond `planned` must point to an
existing Markdown file and must carry source-backed routes.

## Validation

Run:

```bash
python3 GPTs/agent_playbooks/scripts/validate_playbooks.py
```

The validator checks manifest schema, duplicate playbook IDs, path boundaries,
required domain placeholders, ID and block-reference formats, known source and
baseline references when populated, forbidden `GPTs/attachments/` or
`GPTs/upload_package/` edits, and file existence for non-planned playbook rows.
