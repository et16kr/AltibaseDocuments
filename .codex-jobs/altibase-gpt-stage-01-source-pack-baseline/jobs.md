# Altibase GPT Stage 1: Source Pack And Korean-Aligned English Baseline

- Kind: `mixed`
- Status values: `ToDo`, `Progress`, `Done`, `Fail`
- User-run command: `./run-all.sh` from this directory
- Codex workdir: repository root by default, override with `CODEX_WORKDIR=/path`
- Default behavior: continue through all jobs until completion or failure
- Optional single-job mode: `RUN_ONE=1 ./run-all.sh`
- Handoff gate: uncommitted project files stop the workflow before the next job starts
- Commit gate: each successful job must pass review and create a focused commit
- Stage order: source manifest and exact source-pack validation must complete before
  Korean-aligned English baseline generation starts for the same source scope.
- Baseline gate: if source-pack validation is missing or not ready, baseline jobs must
  record blockers instead of generating baseline blocks.
- Source authority: Korean sources are authoritative when paired Korean/English sources
  differ; English sources are extraction aids unless already Korean-source-verified
  AID evidence supports reuse.
- Upload limit: Stage 1 may prepare evidence and working layers outside
  `GPTs/upload_package/`; only files intentionally selected or transformed into
  `GPTs/upload_package/` count toward the final 20 Markdown upload limit.

## Jobs

| ID | Status | Title | Goal |
| --- | --- | --- | --- |
| `S1-J001` | `ToDo` | Stage preflight and schema design | Confirm Stage 1 scope, inspect requirements and durable evidence, define schemas and design notes for source manifest, source pack, AID tiering, and Korean-aligned English baseline. |
| `S1-J002` | `ToDo` | Repository source manifest | Inventory selected repository-local sources, approved support evidence, exclusions, and source IDs into deterministic manifests without treating all GPTs/reports files as source by default. |
| `S1-J003` | `ToDo` | AID tier manifest | Classify AID source groups into upload-content, evidence-only, accepted limitation, conflict, recheck, or excluded tiers while preserving AID evidence classifications. |
| `S1-J004` | `ToDo` | Source pack scripts and shards | Implement or update deterministic source-pack scripts, generate source-preserving shards with source boundaries, and create source-to-shard mapping. |
| `S1-J005` | `ToDo` | Source pack validation and notes | Validate exact source extraction, checksums, token/byte estimates, upload-order guidance, and source-pack GPT instruction notes. |
| `S1-J006` | `ToDo` | Korean English pairing inventory | Inventory repository-local paired Korean and English sources, define baseline block schema, and create the Korean-aligned English baseline manifest. |
| `S1-J007` | `ToDo` | Admin operations baseline batch | Generate Korean-aligned English baseline blocks for installation, administration, storage, backup/recovery, operations, and protected-topic product manual sources, or record scoped not-ready gaps. |
| `S1-J008` | `ToDo` | SQL reference baseline batch | Generate Korean-aligned English baseline blocks for SQL, DDL, DCL, DML, data types, properties, dictionary/performance views, errors, and troubleshooting product manual sources, or record scoped not-ready gaps. |
| `S1-J009` | `ToDo` | Client tool integration baseline batch | Generate Korean-aligned English baseline blocks for client interfaces, APIs, tools, utilities, migration, DB Link, connectors, Spatial, NiFi, Tableau, Kubernetes/AKU, and integration sources, or record scoped not-ready gaps. |
| `S1-J010` | `ToDo` | Release patch technical AID baseline batch | Generate or reuse Korean-aligned English baseline blocks for release notes, patch notes, technical documents, third-party guides, and AID upload candidates, or record scoped not-ready gaps. |
| `S1-J011` | `ToDo` | Baseline validation and conflict register | Validate baseline traceability, alignment status, unresolved Korean/English conflicts, AID reuse decisions, and conflict/recheck records. |
| `S1-J012` | `ToDo` | Stage 1 integration cross-check | Check source-pack to baseline coverage, AID tier coverage, downstream routing readiness, and remaining not-ready gaps before final readiness review. |
| `S1-J013` | `ToDo` | Stage 1 readiness review | Run Stage 1 validation, review all source-pack and baseline deliverables, write readiness or not-ready report, and commit final Stage 1 readiness evidence. |

## Resume Rules

- `Fail`: stop before starting later jobs.
- Dirty project files: stop before starting or advancing to another job.
- `Progress`: preserve interruption evidence, set the job back to `ToDo`, then rerun only when project files are clean.
- `Done`: skip.
- Nonzero `codex exec` exits leave the job as `Progress` by default; the next manual run stops if project files are dirty, or resets runtime state and retries when clean.

## Acceptance Checklist

- Each job has a matching prompt in `prompts/`.
- Each job has concrete acceptance criteria.
- Each successful job leaves project files clean and advances HEAD with a commit.
- `bash -n run-all.sh` passes.

## Stage 1 Completion Outcome

Stage 1 is complete only when the source-preserving pack and Korean-aligned English
baseline are both either complete with validation evidence or explicitly blocked by a
not-ready report. A not-ready report is not a pass; it is a readiness blocker that must
identify the missing source, weak evidence, conflict, validation failure, or scope
decision needed before downstream stages continue.
