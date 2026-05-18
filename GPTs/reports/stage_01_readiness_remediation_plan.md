# Stage 1 Readiness Remediation Plan

- Job: `S1R-J001`
- Date: 2026-05-18
- Scope: Stage 1 readiness blocker preflight for `CONF-000008` and `CONF-000009`
- Boundary: planning and row-level scope freeze only

## Reconfirmed Boundary

This job freezes the current blocker scope and writes the remediation plan for the
remaining Stage 1 readiness blockers. It does not create `GPTs/agent_playbooks/`, edit
`GPTs/attachments/`, assemble `GPTs/upload_package/`, or modify orchestrator-managed
`.codex-jobs/` runtime files.

The row-level scope is recorded in
`GPTs/reports/stage_01_readiness_remediation_scope.tsv`.

## Design Note

The remediation scope uses
`GPTs/reports/source_pack_to_korean_aligned_english_crosswalk.tsv` as the row-level
source of truth. `source_conflict_register.md` preserves the human-readable blocker
summary, but the crosswalk controls the exact source rows, source-pack shard/block
IDs, baseline block IDs, current routing state, and downstream job assignment.

This avoids broadening compact prose ranges into unrelated baseline rows. For example,
the `CONF-000008` conflict-register summary mentions `KAE-BLOCK-000031` through
`KAE-BLOCK-000037`, but the actual blocked crosswalk rows only include
`KAE-BLOCK-000031`, `KAE-BLOCK-000032`, `KAE-BLOCK-000033`, `KAE-BLOCK-000036`, and
`KAE-BLOCK-000037` from that range. `KAE-BLOCK-000034` and `KAE-BLOCK-000035` remain
outside the frozen `CONF-000008`/`CONF-000009` row scope.

## Frozen Scope

| Check | Result |
| --- | --- |
| `CONF-000008` source-pack rows | 51 |
| `CONF-000009` source-pack rows | 2 |
| Total scoped source-pack rows | 53 |
| Scoped source IDs present in `GPTs/source_pack/source_manifest.tsv` | 53 of 53 |
| Scoped source IDs present in `GPTs/source_pack/source_to_shard_manifest.tsv` | 53 of 53 |
| Unique scoped baseline block IDs | 29 |
| Scoped baseline block IDs present in `GPTs/korean_aligned_english/baseline_manifest.tsv` | 29 of 29 |

The current routing states are:

| Conflict | Current routing status | Rows |
| --- | --- | --- |
| `CONF-000008` | `blocked_pending_baseline_alignment` | 51 |
| `CONF-000009` | `excluded_until_source_authority_or_auxiliary_label` | 2 |

## Remediation Sequence

| Job | Scope | Intended disposition |
| --- | --- | --- |
| `S1R-J002` | Stored/external procedure manuals and two English-only stored-procedure media rows | Create aligned baseline routing for paired manual rows; keep English-only media as `nonblocking_exclusion` unless Korean authority or approved auxiliary use is recorded. |
| `S1R-J003` | Monitoring API, SNMP Agent, and Log Analyzer rows | Create aligned baseline routing, or preserve explicit exact source-pack routing if full baseline alignment cannot be completed safely. |
| `S1R-J004` | Performance Tuning and source-index/Sharding rows | Create aligned baseline routing for performance rows; route source-index rows to exact source-pack blocks unless a row is explicitly promoted to an aligned baseline by source-backed work. |
| `S1R-J005` | Replication Manager manual rows | Create aligned baseline routing or explicit exact source-pack routing with version and production-use guardrails. |
| `S1R-J006` | Manifest/crosswalk closure | Update baseline manifest, crosswalk, conflict register, and gap register so `CONF-000008` and `CONF-000009` are resolved or explicitly downgraded with nonblocking guardrails. |
| `S1R-J007` | Stage 1 revalidation | Rerun Stage 1 validation and update readiness with a ready/pass or remaining-blocker verdict. |

## Completion Rules For Later Jobs

- A row may move to `aligned_baseline` only when the baseline manifest and Markdown
  block provide a parseable aligned working route for the source scope.
- A row may move to `exact_source_pack_route` only when the downstream note names the
  exact source-pack shard/block and keeps any version, patch, runtime, or source
  recheck guardrails explicit.
- A row may move to `nonblocking_exclusion` only when the source is not needed for
  Stage 2 playbook readiness or an authority/auxiliary decision justifies exclusion.
- A row remains `remaining_blocker` if it still lacks aligned baseline, exact
  source-pack routing, or defensible nonblocking exclusion after its assigned job.

## Verification Commands For This Preflight

The preflight must pass:

```bash
python3 - <<'PY'
import csv
from collections import Counter

with open('GPTs/reports/stage_01_readiness_remediation_scope.tsv', newline='') as f:
    rows = list(csv.DictReader(f, delimiter='\t'))

counts = Counter(row['conflict_id'] for row in rows)
assert counts['CONF-000008'] == 51, counts
assert counts['CONF-000009'] == 2, counts
assert len(rows) == 53, len(rows)
PY
```

```bash
python3 - <<'PY'
import csv

with open('GPTs/reports/stage_01_readiness_remediation_scope.tsv', newline='') as f:
    scope_ids = {row['source_id'] for row in csv.DictReader(f, delimiter='\t')}

with open('GPTs/source_pack/source_manifest.tsv', newline='') as f:
    manifest_ids = {row['source_id'] for row in csv.DictReader(f, delimiter='\t')}

with open('GPTs/source_pack/source_to_shard_manifest.tsv', newline='') as f:
    shard_ids = {row['source_id'] for row in csv.DictReader(f, delimiter='\t')}

assert not (scope_ids - manifest_ids), sorted(scope_ids - manifest_ids)
assert not (scope_ids - shard_ids), sorted(scope_ids - shard_ids)
PY
```

```bash
python3 - <<'PY'
import csv

with open('GPTs/reports/stage_01_readiness_remediation_scope.tsv', newline='') as f:
    baseline_ids = {
        row['baseline_block_id'] for row in csv.DictReader(f, delimiter='\t')
    }

with open('GPTs/korean_aligned_english/baseline_manifest.tsv', newline='') as f:
    manifest_ids = {
        row['baseline_block_id'] for row in csv.DictReader(f, delimiter='\t')
    }

assert not (baseline_ids - manifest_ids), sorted(baseline_ids - manifest_ids)
PY
```

```bash
git diff --check -- GPTs/reports/stage_01_readiness_remediation_plan.md GPTs/reports/stage_01_readiness_remediation_scope.tsv
```
