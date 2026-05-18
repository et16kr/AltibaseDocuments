# Stage 2 Agent Playbooks

- Job: `S2-J002` scaffold, extended by `S2-J003`
- Scope: manifest schema, validation scaffolding, source-routing plan,
  service-development SQL generation playbooks, and application connectivity
  playbooks
- Status: scaffolded with completed `S2-J003` and `S2-J004` playbook routes

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

## S2-J003 Design Note

`S2-J003` promotes the service-development, DDL/DCL, SQL/data type, properties, and
dictionary/view routes from placeholders to source-backed playbooks. SQL, DDL, DCL,
and DML generation are documented as generated artifact classes inside a broader
Altibase-backed service-development workflow, not as the entire boundary.

The manifest now includes `APB-000015` as the service-development and direct GPT
copy/paste artifact hub, while `APB-000002` through `APB-000005` provide focused
artifact-generation routes. Later Stage 2 jobs may extend adjacent operational,
connectivity, troubleshooting, and testing content, but this job establishes the
shared guardrails for destructive effects, implicit DDL commits, privilege changes,
storage changes, version restrictions, required customer inputs, validation SQL, and
stop conditions.

The validator now checks non-planned playbook files for their playbook ID, title,
required sections, manifest source IDs, source-pack block refs, Korean-aligned
baseline block IDs, guardrail IDs, and fenced generated-artifact examples.

## S2-J004 Design Note

`S2-J004` promotes the Java/JDBC and ODBC/C-client routes from placeholders to
source-backed connectivity playbooks. The playbooks preserve the route split
created by `S2-J002`: `java_jdbc.md` owns JDBC URLs, driver selection, Java
compatibility, Spring, Hibernate, Adapter for JDBC, TLS, failover, tracing, and
connection checks; `odbc_c_clients.md` owns ODBC DSNs, CLI, ACI,
Precompiler/APRE, compile/link/runtime checks, unixODBC, SQLSTATE diagnostics,
and C/C++ build snippets.

The manifest now cites exact repository source IDs plus classified AID
`llm-reference` routes for development/API and framework diagnostics. Because
`CONF-000006` and `CONF-000007` remain open, both playbooks produce guarded
first drafts only; compile-ready code, exhaustive option tables, patch-specific
behavior, live connector compatibility, and production diagnostics still
require exact source-block or customer runtime evidence.

The validator now includes domain-token checks for the completed connectivity
playbooks so required tokens such as `JDBC`, `ODBC`, `CLI`, `ACI`, and
`Precompiler` cannot be silently dropped from the files.

## Validation

Run:

```bash
python3 GPTs/agent_playbooks/scripts/validate_playbooks.py
```

The validator checks manifest schema, duplicate playbook IDs, path boundaries,
required domain placeholders, ID and block-reference formats, known source and
baseline references when populated, forbidden `GPTs/attachments/` or
`GPTs/upload_package/` edits, and file existence for non-planned playbook rows.
