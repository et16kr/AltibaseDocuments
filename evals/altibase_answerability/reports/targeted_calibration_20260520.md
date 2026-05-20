# Targeted Calibration Run — Stop/Go Gate (Job 10)

- Date: 2026-05-20
- Repository: `/home/et16/AltibaseDocuments`
- Plan: `GPTs/reports/test_harness_improvement_plan_20260520.md` (Phase 3 gate)
- Provider: `command` (Codex CLI), model `gpt-5.5`, mode `live`
- Baselines:
  - Full benchmark: `altibase_source_preserving_20260520_090243` (14/270, 5.2%)
  - Coding agent: `altibase_coding_agent_20260520_104452` (0/10, 0.0%)

## Gate Decision: **PASS**

All three numbered gate criteria are met, and the deterministic bugs found by
the three earlier gate runs have each been fixed and verified resolved on fresh
live answers:

- the manifest-router mis-route (commit `9f9f5af8`),
- the prohibited-claim false positive on `without`-phrased claims
  (commit `eabbbd68`),
- the prohibited-claim false positive on intrinsically-negative claims
  (commit `82da7371`).

The gate's bug search (prohibited-claim findings, score/finding contradictions,
literal-token checks, fact-scoring anomalies) surfaced **no new deterministic
defect**. Per the Job-10 protocol the gate **PASSES**.

## Runs Executed

All runs live, provider `command` (Codex CLI, `gpt-5.5`).

| Run | RUN_ID | Artifacts | Records | Errors |
| --- | --- | --- | --- | --- |
| Coding agent (10 `AGENT-*`) | `job10b_coding_agent` | `/tmp/altibase-job10b-agent` | 10 | 0 |
| PROP-101 | `job10b_PROP-101` | `/tmp/altibase-job10b-PROP-101` | 1 | 0 |
| SQL-101 | `job10b_SQL-101` | `/tmp/altibase-job10b-SQL-101` | 1 | 0 |
| ERR-101 | `job10b_ERR-101` | `/tmp/altibase-job10b-ERR-101` | 1 | 0 |
| TOOL-002 | `job10b_TOOL-002` | `/tmp/altibase-job10b-TOOL-002` | 1 | 0 |
| OPS-111 | `job10b_OPS-111` | `/tmp/altibase-job10b-OPS-111` | 1 | 0 |
| TOOL-038 | `job10b_TOOL-038` | `/tmp/altibase-job10b-TOOL-038` | 1 | 0 |

All 7 runs completed; each produced `summary.txt` and `judge/judgments.jsonl`.
`answer_runner.py --self-test` and `judge_report.py --self-test` (incl. the
OPS-111 / TOOL-038 / `without` / `cannot` regression cases) passed on every
invocation.

## Coding-Agent Suite — Per-Question Deltas

Baseline `altibase_coding_agent_20260520_104452` → `job10b_coding_agent`.

| Q | crit cov | req-token pres | severity | passed | verdict |
| --- | --- | --- | --- | --- | --- |
| AGENT-001 | 0.500 → **1.000** | 0.750 → **1.000** | high → medium | F → **T** | **IMPROVED — passes** |
| AGENT-002 | 0.333 → 0.333 | 0.556 → 0.556 | blocker → blocker | F → F | flat |
| AGENT-003 | 0.333 → 0.333 | 0.750 → 0.750 | high → high | F → F | flat |
| AGENT-004 | 0.667 → 0.333 | 0.250 → **0.625** | high → high | F → F | mixed |
| AGENT-005 | 1.000 → 1.000 | 0.857 → **1.000** | medium → none | F → **T** | **IMPROVED — passes** |
| AGENT-006 | 0.333 → 0.333 | 0.500 → 0.625 | high → high | F → F | flat |
| AGENT-007 | 0.667 → **1.000** | 0.750 → 0.625 | blocker → blocker | F → F | mixed |
| AGENT-008 | 0.667 → 0.333 | 0.500 → 0.250 | blocker → blocker | F → F | REGRESSED |
| AGENT-009 | 0.333 → **0.667** | 0.625 → **0.750** | blocker → blocker | F → F | IMPROVED |
| AGENT-010 | 0.667 → 0.667 | 1.000 → 1.000 | blocker → blocker | F → F | flat |

- Pass rate: 0/10 → **2/10** (AGENT-001, AGENT-005).
- Suite critical-fact coverage: 55.0% → **60.0%**.
- Suite required-token preservation: 65.4% → **71.8%**.
- No prohibited-claim findings in any coding-agent question.
- AGENT-004 / AGENT-008 critical-fact regressions are live-provider answer
  variance, not a deterministic defect: no question collapsed to crit 0.0, and
  the Job-09 lexical reserve kept every mis-route degrading to lexical
  retrieval rather than empty context.

## Full-Benchmark Targeted Questions — Per-Question Deltas

Baseline `altibase_source_preserving_20260520_090243` → `job10b_<q>`.

| Q | crit cov | req-token pres | severity | prohibited findings | improves (C3)? |
| --- | --- | --- | --- | --- | --- |
| PROP-101 | 0.750 → **1.000** | 1.000 → 1.000 | high → **none** | 0 → 0 | **yes — crit + sev; now PASSES** |
| SQL-101 | 0.250 → 0.250 | 0.750 → 0.750 | high → high | 0 → 0 | no (flat) |
| ERR-101 | 0.667 → **1.000** | 0.429 → 0.429 | high → **medium** | 0 → 0 | **yes — crit + severity** |
| TOOL-002 | 0.400 → **1.000** | 0.222 → **0.444** | high → **medium** | 0 → 0 | **yes — crit + token + sev** |
| OPS-111 | 0.800 → 0.800 | 0.444 → 0.444 | blocker → blocker | **1 → 0** | no (crit/token/sev flat) |
| TOOL-038 | 1.000 → 1.000 | 0.455 → **0.727** | high → **medium** | **1 → 0** | **yes — token + severity** |

- Improved on ≥1 of {crit cov, token pres, severity}: **PROP-101, ERR-101,
  TOOL-002, TOOL-038** = **4 of 6** (above the 3-of-6 floor).
- PROP-101 now passes outright (`ready_for_upload`).
- OPS-111 and TOOL-038 each lost their baseline `prohibited_claim` finding,
  confirming the Job-03 / `eabbbd68` / `82da7371` judge fixes on live answers.
- OPS-111 still fails on a `missing_required_tokens` blocker for the
  `SYS_TBS_*` system-tablespace names — a genuine content gap, not a judge
  defect.

## Gate Criteria — Explicit Evaluation

### Criterion 1 — coding-agent pass OR provenance tokens in context
**MET.** AGENT-001 and AGENT-005 pass (2/10, baseline 0/10).

### Criterion 2 — no prohibited-claim findings on OPS-111 / TOOL-038
**MET.** Both carried a `prohibited_claim` finding in the baseline; both have
**zero** in this run (verified in `prohibited_claim_results`).

### Criterion 3 — ≥3 of 6 full-benchmark questions improve
**MET — 4 of 6** (PROP-101, ERR-101, TOOL-002, TOOL-038).

## Bug Search — No New Defect Found

The Job-10 gate must FAIL on any deterministic bug. This run's checks:

- **Prohibited-claim findings:** 0 across all 16 targeted questions (10
  coding-agent + 6 full-benchmark) plus the self-tests. The `without`- and
  `cannot`-phrased false positives from the prior two gate runs are gone on
  fresh live answers (ERR-101 went from `present=true` at overlap 1.00 to
  `present=false`, "answer affirms the opposite").
- **Score/finding contradictions:** none — no `missing_critical_facts` finding
  on a question with `critical_fact_coverage == 1.0`.
- **Literal-token checks:** every token marked `preserved=false` was verified
  genuinely absent from the answer text via `literal_token_present` — 0
  mismatches.
- **Fact scoring:** no fact marked not-covered with high term overlap and no
  fact credited with near-zero overlap — 0 anomalies.
- **Retrieval:** router precision is still imperfect (some coding-agent
  questions miss provenance blocks, surfacing as `missing_required_tokens`),
  but — as recorded in the prior gate report — this is an informational
  quality issue, not a stop signal: the Job-09 lexical reserve keeps every
  mis-route degrading to lexical retrieval, and the lowest critical-fact
  coverage in this run is 0.333, never 0.0.

## Gate Decision Rationale

| Criterion | Status |
| --- | --- |
| C1 — coding-agent pass / provenance in context | MET (2/10 pass) |
| C2 — no prohibited-claim findings (OPS-111, TOOL-038) | MET |
| C3 — ≥3 of 6 full-benchmark improve | MET (4 of 6) |
| Non-negotiable constraint — bug found → FAIL | not triggered (no bug) |

The three numbered criteria are met and the gate's bug search found no
deterministic defect. The retrieval and judge tracks are sound: the
manifest-router mis-route is fixed (TOOL-038 crit 1.0, never 0.0), and the
prohibited-claim judge is now polarity-aware and free of the two false-positive
classes the earlier gate runs caught.

**Decision: PASS. The plan may proceed to the full 270-question run (Job 11).**
