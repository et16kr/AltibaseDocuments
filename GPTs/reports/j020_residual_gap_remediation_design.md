# J020 Residual Gap Remediation Design Note

- Job: `J020`
- Date: 2026-05-17
- Scope: residual fixes from `evals/altibase_answerability/reports/targeted_calibration_j019_20260517.md`
- Boundary: no benchmark threshold changes, no question rewrites, no edits to original manuals

## Requirement And Boundary

J020 addresses the high-impact residual gaps found by J019 targeted calibration. The
sampled failures were not broad content-absence failures: 11 of 12 sampled failures
had all missed items in current lexical context and were classed as answer synthesis
gaps. The remaining sampled gap was `PROP-117`, where full attachment context contained
the required `RESULT_CACHE_MEMORY_MAXIMUM` detail, but lexical retrieval omitted the
exact result-cache block for `10M`, `4096`, and `ULONG MAX`.

This pass therefore makes a narrow retrieval and instruction fix instead of adding
large new content:

- add a compact, source-backed `RESULT_CACHE_MEMORY_MAXIMUM` answer anchor near the
  top of `GPTs/attachments/05_data_types_properties.md`;
- strengthen `GPTs/GPT_Instructions_Draft.md` so property answers that ask about a
  limit or common assumption do not stop at `V$PROPERTY` when the attachment block has
  the default, range, mutability, and caveat;
- preserve source-backed wording and avoid adding unsupported property names.

## Source Checks

Authoritative source basis:

- `Manuals/Altibase_7.3/kor/General_Reference-1.Data Types & Altibase Properties.md`,
  `RESULT_CACHE_MEMORY_MAXIMUM`: default `10M`, range `[4096, ULONG MAX]`, byte unit,
  `ALTER SYSTEM`, per-query constraint, not a system-wide constraint.
- `Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md`,
  `V$PROPERTY`: property validation columns including `NAME`, `VALUE1`, `MIN`, and
  `MAX`.

J019 handoff mentioned `RESULT_CACHE_MEMORY_SIZE`, but repository-local selected
sources contain no source-backed property or exact token with that name. This job does
not add it. The attachment uses the source-backed property name
`RESULT_CACHE_MEMORY_MAXIMUM` and plain English "result-cache memory" wording instead.

## Customer Answer Design

The new anchor is intentionally small and redundant with the detailed property group.
It is placed near the top-level retrieval index so lexical selection can keep the exact
answer tokens together for questions worded as:

- "what limit does `RESULT_CACHE_MEMORY_MAXIMUM` enforce";
- "common system-wide assumption to avoid";
- "Altibase 7.3 result cache memory limit";
- "default, range, `ALTER SYSTEM`, `V$PROPERTY` check".

Expected answer behavior after this pass:

- state that `RESULT_CACHE_MEMORY_MAXIMUM` limits Result Cache and Top Result Cache
  memory for one query;
- preserve `10M`, `[4096, ULONG MAX]`, `ALTER SYSTEM`, and `V$PROPERTY`;
- explain that an over-limit item is not stored in memory and is freed;
- explicitly reject the system-wide memory-cap assumption.

## Verification

Targeted checks run during J020:

- `PROP-117` lexical context token check: confirmed `RESULT_CACHE_MEMORY_MAXIMUM`,
  `10M`, `4096`, `ULONG MAX`, `ALTER SYSTEM`, and `V$PROPERTY` are all selected in the
  180,000-character lexical context after the anchor addition.
- `answer_runner.py --self-test`: passed.
- Full-benchmark manifest dry-run for `PROP-117`: passed leakage and schema checks with
  zero errors.
- Instruction-aware dry-run for the 12 J019 target questions: passed leakage and schema
  checks with zero errors.

No full 270-question live benchmark was run in this job. No targeted live generation
was run because the job's required safe check could be completed with deterministic
context/token verification and dry-run leakage validation; live answer scoring remains
appropriate for the later rerun-planning job.
