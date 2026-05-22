# `properties` Domain Deep-Dive — Cycle 2, C2-06

- Date: 2026-05-20
- Repository: `/home/et16/AltibaseDocuments`
- Master plan: `GPTs/reports/answerability_improvement_cycle2_plan_20260520.md` — item C2-06
- Evidence baseline: `evals/altibase_answerability/reports/full_rerun_analysis_20260520.md`
  §5.3 and §6 target 3 — `properties` is the worst domain (pass 2.0 %, required-token
  preservation ≈ 50 %).
- Scope: `evals/altibase_answerability/scripts/answer_runner.py` only. No
  `GPTs/upload_package/` source bodies and no question records were modified.

## 1. Summary

`properties` is the worst domain not because the version-specific property facts
are missing from the source pack — **they are almost all present** — but because
the manifest router cannot tell the General Reference-1 property manual apart
from the other manuals of the same Altibase version, and the mis-route then
floods the 180 000-char context budget with the wrong manual's blocks.

This is overwhelmingly a **category-(a) retrieval/scoring defect**. There are
**no genuine category-(b) source-content gaps**: every property fact the 50
questions ask about is documented in `GPTs/upload_package/`.

The fix (C2-06) adds a dedicated, highest-priority **property-definition
section** to `build_context()` that admits the named property's own
documented section — and the `V$PROPERTY` data-dictionary companion —
regardless of the manifest routing decision.

| Metric (50 `properties` questions, 278 required tokens) | Before | After |
| --- | ---: | ---: |
| Required tokens literally in assembled context | 168 / 278 (60.4 %) | **223 / 278 (80.2 %)** |
| Questions improved / unchanged / regressed | — | **24 / 26 / 0** |

"Before" is the cycle-1 baseline reconstruction (the job-11 retrieval code at
`HEAD`); "after" is the same `build_context()` harness with the C2-06 change.
Both are reconstructed the same way — `build_context()` is deterministic — and
the run is reproducible (verified: two reconstructions byte-identical).

## 2. Method

For each of the 50 `properties` questions
(`evals/altibase_answerability/questions/properties.jsonl`):

1. The cycle-1 job-11 retrieval-audit sidecar
   (`reports/full_benchmark/runs/altibase_source_preserving_20260520_195639_job11/answers/retrieval_audit.jsonl`)
   gave the actual routed `source_id`s per question.
2. `build_context()` was replayed deterministically with the in-package
   manifests (`02_source_manifest.md`, `03_source_to_shard_manifest.md`),
   exactly as `answer_runner.main()` runs it (`max_context_chars = 180000`,
   `chunk_chars = 8000`, lexical mode) — the manifest-aware rebuild the
   `--retrieval-recall` tooling note in §6 of the cycle-1 analysis calls for.
3. Each required token was checked three ways: literally present in the
   assembled context; present in the question's *expected* source blocks (the
   `source_refs`); present anywhere in the source pack.

## 3. Root cause — why `properties` questions fail

### 3.1 The router cannot distinguish the property manual (category a)

`route_sources()` scores `02_source_manifest.md` rows by question-token overlap
on `title`, `source_family`, `source_path`, `version_scope`, `language`. Every
per-version product manual row carries the **same generic title** — `Altibase
7.3`, `Altibase 7.1` — and the **same `version_scope`**. The property manual
(`general_reference_1_datatypes_properties` family, e.g. `SRC-000120` for 7.3)
is therefore indistinguishable from the same version's JDBC, migration, or
administration manual.

Worked example — PROP-113 ("What are HASH_AREA_SIZE's default, range, purpose,
and dynamic change support in Altibase 7.3?"):

- Query tokens that hit a manifest row: `altibase` (every Altibase row) and
  `7.3` (every 7.3 row). The discriminating token, the property name
  `hash_area_size`, appears in **no** `02_source_manifest.md` column.
- Every 7.3 product-manual row scores identically: `altibase` (title, 5) +
  `7.3` (title, technical ×4 = 20) + version-match bonus (4) = **29**, with
  **2 distinct token hits**. The General Reference-1 property manual
  `SRC-000120` ties with the JDBC, migration, administration, CLI, and
  dblink manuals.
- The tie is broken by ascending `source_id`, so routing returns
  `SRC-000080, SRC-000081, SRC-000082, SRC-000083, SRC-000086` — the JDBC,
  migration-Oracle, administration, CLI, and dblink manuals. The property
  manual is **not routed**.

Across the 50 `properties` questions the router selected a question's own
documented source for **only 1** (PROP-111). The other 49 mis-route.

### 3.2 The mis-route then saturates the budget (category a)

`score_chunk()` adds `ROUTED_SOURCE_BONUS = 100 000` to **every** chunk of a
routed source. The mis-routed manuals are large single blocks, so the routed
section fills the routed ceiling (70 % of 180 000 chars) with content from the
wrong manuals — for PROP-113 the assembled context was 75 chunks from
`SRC-000080/81/82/83/86` ("lib Directory", "Documentation Conventions", "Range
Partitioning" …). The correct `HASH_AREA_SIZE` section of `SRC-000120` ranked
#1221 with a lexical score of 35 and never reached context: PROP-113 went from
**0 / 6** required tokens in context.

### 3.3 The facts are in the pack — there is no category (b)

The property facts are present and correctly documented:

- required tokens literally in the pack: **270 / 278 (97.1 %)**;
- required tokens in the question's *expected* source blocks: **213 / 278**;
- the 8 tokens not literally in the pack are **token-form mismatches**, not
  missing content (see §5).

So for every question the failure is **(a): the fact is in the source pack but
retrieval/scoring does not bring it into context** — never **(b): genuinely
absent**.

## 4. The fix (category a)

`build_context()` gains a dedicated **property-definition section** (`C2-06`),
assembled at the highest priority after the routing-metadata section and
*before* the routed section, so a generic-titled mis-route can no longer starve
a named property's own documented section. New code, all in
`answer_runner.py`:

- `extract_property_names()` — pulls Altibase property identifiers
  (ALL-CAPS with an interior underscore: `HASH_AREA_SIZE`, `MEM_DB_DIR`) from
  the **question text only**.
- `version_scope_serves()` — matches the question `version_scope` to a source
  block's: `7.1`/`7.3` exact, `8.1` to any `8.1*`, `cross-version` /
  `patch-specific` to any tree.
- `build_definition_section()` — selects, from the deterministically scored
  chunk set:
  1. the **property's own definition block** — a chunk in the General
     Reference-1 property manual (`general_reference_1_datatypes_properties`)
     whose heading *is* a property identifier named in the question, version
     filtered;
  2. the **`V$PROPERTY` data-dictionary companion** — the General
     Reference-2 section that carries the `NAME` / `STOREDCOUNT` / `ATTR` /
     `MIN` / `MAX` / `VALUE1..VALUE8` columns — admitted when the question
     genuinely names a documented property or uses the word "property".

Design points:

- **Scoped to the properties domain.** Both passes are confined to the two
  property-manual `source_family` values. An error macro or SQL function with
  the same ALL-CAPS-underscore shape (`ERR_ABORT`, `JSON_VALUE`) has no section
  there, so `build_definition_section()` returns an empty list and
  `build_context()` is byte-identical to before for it. Across the other six
  domains the section is non-empty for only 14 / 230 questions, and every one
  of those 14 genuinely names an Altibase property — admitting its manual
  section is correct retrieval, not a regression.
- **Markdown-escape aware.** The manuals escape `$` in the data-dictionary
  heading (`V\$PROPERTY`); headings are tokenised with backslashes stripped so
  the companion still matches.
- **Routing untouched.** `route_sources()` is *not* changed. The discriminating
  signal — the property name — is absent from every `02_source_manifest.md`
  column, so manifest-only routing genuinely cannot distinguish the property
  manual; cycle-1 job-10 / cycle-2 job-05 also found router re-ranking
  regression-prone under the saturated 180 k budget. The C2-06 fix instead
  makes context *assembly* resilient to the unavoidable routing miss, anchored
  on the property identifier that the question states and the source body
  carries as a section heading.
- **Determinism, leakage checks, `--self-test`, and every retrieval-audit
  field are preserved.** The new section uses only the allowlisted question
  projection and the in-package manifests/blocks.

## 5. The (a)/(b) split and residual gaps

### 5.1 Category (a) — retrieval defect, fixed

55 required-token occurrences moved into context (168 → 223). No question
regressed; 24 improved, 26 were already complete or were limited only by the
residuals below. Largest recoveries: PROP-113 0→4, PROP-124 0→4, PROP-149 2→6,
PROP-104/120/121/122/131 +3 each.

### 5.2 Category (b) — genuine source-content gaps

**None.** Every fact the 50 `properties` questions require is documented in
`GPTs/upload_package/`. No question's required facts are genuinely missing from
the pack.

### 5.3 Residual misses (55 token occurrences) — classified honestly

The 55 still-missing token occurrences are **not** category-(b) content gaps.
They split into:

**(i) Token-form mismatches in the question records — 46 occurrences.** The
fact *is* in the assembled context; the question's `required_tokens` string
just does not literally match the source's markdown/HTML rendering, and the
harness measures literal substring presence. Per the C2-06 constraints, the
question records were **not** edited — recorded here instead:

- **`V$PROPERTY` — 25 occurrences** (PROP-105, 109, 110, 112, 113, 114, 116,
  117, 119, 122, 123, 124, 127, 128, 129, 130, 131, 135, 136, 137, 138, 141,
  148, 149, 150). The authoritative Korean manuals markdown-escape the `$`
  (`V\$PROPERTY`); the literal token `V$PROPERTY` matches only in the English
  AID copies. The C2-06 fix *does* admit the documented `V$PROPERTY` section
  (its `STOREDCOUNT` / `VALUE1..VALUE8` columns are now retrieved — see
  PROP-104/105), but the bare view-name token stays escape-sensitive.
- **Numeric / math notation — 21 occurrences.** The manuals render exponents
  with HTML superscript and escape `*`: the question token `2^32 - 1` is
  `2<sup>32</sup>-1` in the source (565 occurrences), `2^64`/`2^31` are
  `2<sup>64</sup>`/`2<sup>31</sup>`, `100 * 1024 * 1024` is
  `100 \* 1024 \* 1024`, `64M` is `67108864` / `64 \* 1024 \* 1024`. Affected:
  `2^32 - 1` ×7, `2^64 - 1` ×5, `2^64` ×4, `2^32 + 1` ×2, `2^31` ×1,
  `100 * 1024 * 1024` ×1, `64M` ×1.

**(ii) Residual category-(a) retrieval miss — 4 occurrences.** PROP-107
(`10485760`, `104857600`, `4294967295`) and PROP-118 (`7.3.0.0.1`) need the
8.1 release-note **"Changed server properties"** change record. Those integers
are plentiful in the pack and literally matchable, but the change record is a
release-note table, not a per-property manual heading, so the C2-06
definition-block mechanism does not reach it. Admitting the release-note
change-record section is a worthwhile follow-up (a release-note-aware
companion, analogous to the `V$PROPERTY` companion) but is left out of this
job to keep the change properties-scoped and regression-safe.

**(iii) Question-phrasing residual — PROP-123, 5 occurrences.** PROP-123 names
its property in prose ("session **time zone**") rather than as the `TIME_ZONE`
identifier, so the identifier-anchored definition section cannot fire and the
question falls back to lexical retrieval, which is insufficient under the
saturated budget against the mis-route. `TIME_ZONE`, `OS_TZ`,
`V$TIME_ZONE_NAMES`, `+09:00`, `ALTER SESSION` stay missing. The facts *are*
in the pack — this is a question-record phrasing weakness (the question could
state the `TIME_ZONE` property name), recorded here, not papered over.

## 6. Per-question before → after

| Question | version_scope | before | after | Δ | residual misses |
| --- | --- | ---: | ---: | ---: | --- |
| PROP-101 | cross-version | 5/5 | 5/5 | +0 | — |
| PROP-102 | cross-version | 6/8 | 8/8 | +2 | — |
| PROP-103 | 7.3 | 4/4 | 4/4 | +0 | — |
| PROP-104 | 7.3 | 3/6 | 6/6 | +3 | — |
| PROP-105 | 7.3 | 2/6 | 5/6 | +3 | `V$PROPERTY` (escape) |
| PROP-106 | 7.1 | 4/5 | 4/5 | +0 | `2^64 - 1` (notation) |
| PROP-107 | patch-specific | 1/6 | 1/6 | +0 | 3× release-note ints; `100 * 1024 * 1024`, `2^32 - 1` (notation) |
| PROP-108 | 7.3 | 3/7 | 4/7 | +1 | `2^31`, `2^32 + 1`, `2^64` (notation) |
| PROP-109 | 7.3 | 1/6 | 3/6 | +2 | `2^64 - 1`, `2^64` (notation); `V$PROPERTY` |
| PROP-110 | 7.3 | 1/5 | 2/5 | +1 | `2^32 + 1`, `2^64` (notation); `V$PROPERTY` |
| PROP-111 | 7.3 | 7/7 | 7/7 | +0 | — |
| PROP-112 | 7.3 | 4/5 | 4/5 | +0 | `V$PROPERTY` |
| PROP-113 | 7.3 | 0/6 | 4/6 | +4 | `2^64 - 1` (notation); `V$PROPERTY` |
| PROP-114 | 7.3 | 3/6 | 4/6 | +1 | `2^64 - 1` (notation); `V$PROPERTY` |
| PROP-115 | 7.3 | 4/6 | 4/6 | +0 | `64M`, `2^64 - 1` (notation) |
| PROP-116 | 7.3 | 1/4 | 3/4 | +2 | `V$PROPERTY` |
| PROP-117 | 7.3 | 3/6 | 5/6 | +2 | `V$PROPERTY` |
| PROP-118 | patch-specific | 4/5 | 4/5 | +0 | `7.3.0.0.1` (release-note) |
| PROP-119 | 7.3 | 1/4 | 3/4 | +2 | `V$PROPERTY` |
| PROP-120 | 7.3 | 2/6 | 5/6 | +3 | `2^32 - 1` (notation) |
| PROP-121 | 7.3 | 2/5 | 5/5 | +3 | — |
| PROP-122 | 7.3 | 2/6 | 5/6 | +3 | `V$PROPERTY` |
| PROP-123 | 7.3 | 0/6 | 0/6 | +0 | question-phrasing residual (5) + `V$PROPERTY` |
| PROP-124 | 7.3 | 0/5 | 4/5 | +4 | `V$PROPERTY` |
| PROP-125 | 7.1 | 5/7 | 6/7 | +1 | `2^32 - 1` (notation) |
| PROP-126 | 7.3 | 3/6 | 5/6 | +2 | `2^32 - 1` (notation) |
| PROP-127 | 7.3 | 1/5 | 3/5 | +2 | `2^32 - 1` (notation); `V$PROPERTY` |
| PROP-128 | 7.3 | 2/5 | 4/5 | +2 | `V$PROPERTY` |
| PROP-129 | 7.3 | 3/4 | 3/4 | +0 | `V$PROPERTY` |
| PROP-130 | 7.3 | 2/3 | 2/3 | +0 | `V$PROPERTY` |
| PROP-131 | 7.3 | 0/4 | 3/4 | +3 | `V$PROPERTY` |
| PROP-132 | patch-specific | 5/6 | 5/6 | +0 | `2^32 - 1` (notation) |
| PROP-133 | patch-specific | 5/6 | 5/6 | +0 | `2^32 - 1` (notation) |
| PROP-134 | patch-specific | 7/7 | 7/7 | +0 | — |
| PROP-135 | 7.3 | 4/5 | 4/5 | +0 | `V$PROPERTY` |
| PROP-136 | 7.3 | 1/4 | 3/4 | +2 | `V$PROPERTY` |
| PROP-137 | 7.3 | 5/6 | 5/6 | +0 | `V$PROPERTY` |
| PROP-138 | 7.3 | 5/6 | 5/6 | +0 | `V$PROPERTY` |
| PROP-139 | 8.1 | 6/6 | 6/6 | +0 | — |
| PROP-140 | 7.3 | 7/7 | 7/7 | +0 | — |
| PROP-141 | 7.3 | 1/3 | 2/3 | +1 | `V$PROPERTY` |
| PROP-142 | 7.3 | 7/7 | 7/7 | +0 | — |
| PROP-143 | 8.1 | 4/4 | 4/4 | +0 | — |
| PROP-144 | 8.1 | 6/7 | 6/7 | +0 | `2^64` (notation) |
| PROP-145 | 8.1 | 6/6 | 6/6 | +0 | — |
| PROP-146 | cross-version | 3/5 | 5/5 | +2 | — |
| PROP-147 | cross-version | 5/5 | 5/5 | +0 | — |
| PROP-148 | 7.3 | 6/7 | 6/7 | +0 | `V$PROPERTY` |
| PROP-149 | 7.3 | 2/7 | 6/7 | +4 | `V$PROPERTY` |
| PROP-150 | 7.3 | 4/5 | 4/5 | +0 | `V$PROPERTY` |
| **Total** | | **168/278** | **223/278** | **+55** | 46 token-form, 4 release-note, 5 phrasing |

## 7. Question-record observations (not modified — recorded per the constraints)

The 46 token-form mismatches in §5.3(i) and PROP-123's phrasing all point at the
question records, which were left untouched:

- `required_tokens` values such as `2^64 - 1`, `2^32 + 1`, `100 * 1024 * 1024`,
  `64M`, and `V$PROPERTY` use a plain-text rendering that the authoritative
  Korean manuals do not use verbatim (`2<sup>64</sup>-1`,
  `100 \* 1024 \* 1024`, `67108864`, `V\$PROPERTY`). A future cycle should
  either normalise these tokens in the question records or make the
  required-token check escape/markup-insensitive — a measurement change, out of
  scope for this retrieval job.
- PROP-123 would benefit from naming the `TIME_ZONE` property identifier in the
  question text the way the other 48 property questions name theirs.

## 8. Acceptance

```
python3 evals/altibase_answerability/scripts/answer_runner.py --self-test     # OK
test -f evals/altibase_answerability/reports/properties_deep_dive_cycle2_20260520.md  # present
MODE=dry_run LIMIT=20 RUN_ID=c2_06_props RUN_ROOT=/tmp/altibase-c2-06 \
  ./run-test.sh source-preserving                                             # 20 records, 0 errors
test -s /tmp/altibase-c2-06/answers/retrieval_audit.jsonl                     # 20-record sidecar
git diff --check                                                              # clean
```

Required-token-in-context for the `properties` questions, reconstructed the same
way before and after, **increases 60.4 % → 80.2 % (+55 tokens, +19.8 pp)** for
the category-(a) questions, with **zero regressions**. The investigation found
the failure is category (a) — retrieval/scoring — with **no genuine category-(b)
source-content gap**; the residual 55 token occurrences are 46 question-record
token-form mismatches, 4 release-note retrieval misses (follow-up noted), and
PROP-123's question-phrasing residual, each documented above rather than papered
over.

**C2-06: PASS.**
