# Altibase GPT Stage 1 Readiness Remediation

- Kind: `mixed`
- Status values: `ToDo`, `Progress`, `Done`, `Fail`
- User-run command: `./run-all.sh` from this directory
- Codex workdir: repository root by default, override with `CODEX_WORKDIR=/path`
- Default behavior: continue through all jobs until completion or failure
- Optional single-job mode: `RUN_ONE=1 ./run-all.sh`
- Handoff gate: uncommitted project files stop the workflow before the next job starts
- Commit gate: each successful job must pass review and create a focused commit
- Purpose: close the two Stage 1 readiness blockers recorded by `S1-J013` without
  weakening source authority, exact-source routing, or downstream guardrails.
- Scope boundary: this workflow may update Stage 1 source-pack/baseline/crosswalk/
  conflict/readiness evidence, but it must not create Stage 2 playbooks, edit
  `GPTs/attachments/`, or assemble `GPTs/upload_package/`.
- Blocking sources:
  - `CONF-000008` / `APG-S1-J012-001`: 51 selected source-pack rows with pending
    Korean-aligned English routing.
  - `CONF-000009` / `APG-S1-J012-002`: 2 English-only stored-procedure media rows
    excluded until Korean authority, approved auxiliary use, or a nonblocking
    exclusion route is recorded.
- Completion target: `customer_agent_enablement_stage_01_readiness.md` must be
  updated by `S1R-J007` with an explicit `ready/pass` or remaining-blocker verdict.
- Validation coverage: if any job creates a new
  `GPTs/korean_aligned_english/*.md` baseline file, it must also update
  `GPTs/korean_aligned_english/scripts/validate_alignment.py` so the new file is
  included in baseline Markdown validation.

## Jobs

| ID | Status | Title | Goal |
| --- | --- | --- | --- |
| `S1R-J001` | `ToDo` | Blocker preflight and source grouping | Freeze the current CONF-000008 and CONF-000009 scope, verify source IDs and baseline rows, and write the remediation plan for Stage 1 readiness blockers. |
| `S1R-J002` | `ToDo` | Stored procedures and media authority remediation | Resolve stored/external procedure baseline routing, including the two English-only stored-procedure media sources, with Korean authority or explicit auxiliary/exclusion handling. |
| `S1R-J003` | `ToDo` | Monitoring and Log Analyzer remediation | Create aligned working baseline or exact source-pack routing for Monitoring API, SNMP Agent, and Log Analyzer pending rows. |
| `S1R-J004` | `ToDo` | Performance and source-index remediation | Create aligned working baseline or exact source-pack routing for Performance Tuning and source-index/Sharding pending rows. |
| `S1R-J005` | `ToDo` | Replication Manager remediation | Create aligned working baseline or exact source-pack routing for Replication Manager manual and release-note pending rows. |
| `S1R-J006` | `ToDo` | Manifest crosswalk and blocker closure | Update baseline manifest, crosswalk, conflict register, and Stage 2 gap register so CONF-000008 and CONF-000009 are resolved or explicitly downgraded with nonblocking guardrails. |
| `S1R-J007` | `ToDo` | Stage 1 readiness revalidation | Rerun Stage 1 source-pack, AID tier, baseline, crosswalk, and conflict validation, then update the Stage 1 readiness report with a ready/pass or remaining blocker verdict. |

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
- `CONF-000008` and `CONF-000009` are either resolved or preserved as explicit
  remaining blockers with exact next action.
- All new baseline files are covered by `validate_alignment.py`, and new appended
  `KAE-BLOCK-*` rows use non-conflicting IDs after the existing manifest rows.
- Stage 2 must not be declared safe unless the crosswalk has no
  `not_ready_pending_alignment`, `blocked_pending_baseline_alignment`, or unresolved
  excluded-authority rows blocking Stage 2 routing.
