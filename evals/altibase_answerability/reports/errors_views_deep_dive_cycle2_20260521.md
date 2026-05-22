# `errors_troubleshooting` / `views_performance_monitoring` Deep-Dive — Cycle 2, C2-07

- Date: 2026-05-21
- Repository: `/home/et16/AltibaseDocuments`
- Master plan: `GPTs/reports/answerability_improvement_cycle2_plan_20260520.md` — item C2-07
- Evidence baseline: `evals/altibase_answerability/reports/full_rerun_analysis_20260520.md`
  §5.3 and §6 target 5 — after `properties`, the two weakest domains are
  `errors_troubleshooting` and `views_performance_monitoring`.
- Scope: `evals/altibase_answerability/scripts/answer_runner.py` only. No
  `GPTs/upload_package/` source bodies and no question records were modified.

## 1. Summary

`errors_troubleshooting` and `views_performance_monitoring` are weak for the
same structural reason `properties` was (C2-06): the manifest router cannot
single out the manual that documents the fact, the mis-route then floods the
saturated 180 000-char budget with the wrong manual's blocks, and the one
block the question actually needs never reaches context.

- For `errors_troubleshooting` the needed block is a **per-error entry** in the
  Error Message Reference (`error_message_reference` family) — the
  `0x... (decimal) symbol message` line plus its Cause/Action.
- For `views_performance_monitoring` the needed block is a **per-view /
  per-meta-table section** in General Reference-2
  (`general_reference_2_dictionary_views` family).

This is overwhelmingly a **category-(a) retrieval/scoring defect**. There is
**no genuine category-(b) source-content gap**: every error code, symbol,
message, view, and column the 60 questions ask about is documented in
`GPTs/upload_package/`.

The fix (C2-07) extends `build_context()` with a dedicated, highest-priority
**reference section** — the same treatment C2-06 gave `properties` — that
admits the named error's entry chunk and the named view's documented section
regardless of the manifest routing decision.

| Metric | `errors_troubleshooting` | `views_performance_monitoring` |
| --- | ---: | ---: |
| Required tokens (30 questions) | 198 | 280 |
| Required-token-in-context — cycle-1 baseline | 113 / 198 (57.1 %) | 179 / 280 (63.9 %) |
| Required-token-in-context — after C2-07 | **166 / 198 (83.8 %)** | **211 / 280 (75.4 %)** |
| Δ vs cycle-1 baseline | **+53 (+26.7 pp)** | **+32 (+11.5 pp)** |

"Before" is the cycle-1 job-11 retrieval code (`HEAD`); "after" is the same
`build_context()` harness with the cycle-2 changes through C2-07. Both are
reconstructed the same deterministic way — see §2 — and the rebuild is
reproducible (verified: every one of the 270 questions byte-stable across two
rebuilds).

## 2. Method

Mirrors the C2-06 properties deep-dive. For the 30 questions of each domain
(`evals/altibase_answerability/questions/errors_troubleshooting.jsonl`,
`.../views_performance_monitoring.jsonl`):

1. `build_context()` is replayed deterministically with the in-package
   manifests (`02_source_manifest.md`, `03_source_to_shard_manifest.md`),
   exactly as `answer_runner.main()` runs it (`max_context_chars = 180000`,
   `chunk_chars = 8000`, lexical mode) — the manifest-aware rebuild the
   cycle-1 `--retrieval-recall` tooling note calls for.
2. Each required token is checked for literal presence in the assembled
   context, and for presence anywhere in the source pack.
3. The cycle-1 job-11 retrieval-audit sidecar
   (`reports/full_benchmark/runs/altibase_source_preserving_20260520_195639_job11/answers/retrieval_audit.jsonl`)
   gave the per-question routed `source_id`s used in the diagnosis.

The reconstruction reproduces the published cycle-1 `properties` number
(168/278) exactly, confirming the harness is faithful.

## 3. Root cause — why these questions fail

### 3.1 The router cannot single out the reference manual (category a)

`route_sources()` scores `02_source_manifest.md` rows by question-token overlap
on `title`, `source_family`, `source_path`, `version_scope`, `language`. The
Error Message Reference and the General Reference-2 data-dictionary manual carry
the **same generic per-version title** (`Altibase 7.3`, `Trunk`) as every other
manual of that version, and the discriminating token — the error symbol, the
hex code, the `V$`/`SYS_` identifier — appears in **no** `02_source_manifest.md`
column. So routing cannot distinguish them and falls back to `source_id` order,
usually selecting the wrong manual.

Worked examples from the cycle-1 job-11 audit:

- **ERR-112** ("…fails with `qpERR_ABORT_QDT_NOT_EXIST_TBS` or the message
  `Tablespace not found`") routed `AID-SRC-000158/000108/000135/000160/000173`
  — none is the 7.3 Error Message Reference (`SRC-000087` en / `SRC-000118`
  ko). Required-token-in-context: **1/5**.
- **ERR-104** routes the iSQL/iLoader manuals because the token `isql`
  word-boundary-matches the `isql_iloader` `source_family`.
- **VPM-112** ("which `V$LFG` columns…") routed
  `SRC-000126/000095/000402/000413/000422` — not the 7.3 General Reference-2
  (`SRC-000121`). Required-token-in-context: **1/8**.

### 3.2 The mis-route then saturates the budget (category a)

`score_chunk()` adds `ROUTED_SOURCE_BONUS = 100 000` to every chunk of a routed
source. The mis-routed manuals fill the routed ceiling (70 % of 180 000 chars)
with the wrong content, and the correct entry / view chunk — carrying only a
plain lexical score — never reaches context.

### 3.3 The facts are in the pack — there is no category (b)

Of the 101 required-token occurrences still missing after C2-07, **0 are a
genuine source-content gap**: every one is literally present somewhere in
`GPTs/upload_package/` except two descriptive-phrase / placeholder strings
(VPM-115 `optimizer-related properties`, VPM-120 `/*+ hint */`) whose
underlying facts the manuals do document, only not under that verbatim
phrasing. So for every question the failure is **category (a)** — the fact is
in the pack but retrieval/scoring does not bring it into context — never
**category (b)**.

## 4. The fix (category a)

`build_context()` gains a dedicated **reference section** (C2-07), assembled at
the same highest priority as the C2-06 property-definition section — after the
routing metadata and *before* the routed section — so a generic-titled
mis-route can no longer starve a named error's or view's documented block. New
code, all in `answer_runner.py`:

- `extract_error_identifiers()` — pulls the error identifiers a question names
  from the **question text only**: error symbols (`qpERR_ABORT_...`,
  `idERR_FATAL_idc_SVC_INET_BIND_ERROR`), hex reference codes (`0x311D6`), and
  the `ERR-<hex>` runtime form, expanded to its `0x<hex>` reference form (the
  form the manual indexes by). An all-zero runtime code (`ERR-00000`) is not
  expanded — it is a runtime status, not a reference code.
- `build_error_reference_section()` — admits, from the
  `error_message_reference` family and version-filtered, the chunk(s) whose
  **body** carries a named error's entry. The match is on the body because the
  manual documents each error as bold text under a generic
  `FATAL`/`ABORT`/`IGNORE`/`RETRY` heading, not a per-error heading.
- `extract_dict_view_names()` — pulls the `V$`/`X$`/`SYS_..._` identifiers a
  question names from the question text.
- `build_dict_view_section()` — admits, from the
  `general_reference_2_dictionary_views` family and version-filtered, the whole
  documented section of each named view: the view's description chunk **and**
  every following column-detail chunk. Heading-token matching alone is
  insufficient — the manual breaks a view's column list under a generic
  `Column Information` / `칼럼 정보` sub-heading, so the column chunks do not
  carry the view-name heading. The section therefore walks `context_chunks` in
  document order and tracks the most recent view-name heading; headings are
  matched with backslashes stripped so the escaped `V\$STATEMENT` /
  `SYS_TABLES\_` headings still match.

Design points (the same discipline as C2-06):

- **Naturally domain-scoped.** The error-identifier patterns and the
  `V$`/`SYS_` patterns occur **only** in `errors_troubleshooting` and
  `views_performance_monitoring` question text — verified across all seven
  full-suite domains. For every question of the other five domains both
  builders return an empty list, so `reference_section` is empty and
  `build_context()` is **byte-identical to before** there. No explicit `domain`
  guard is used (and `domain` is not on the answer-generation allowlist).
- **Anchored on the question's own text.** Only the allowlisted question
  projection and the in-package manifests/blocks are used — never judge-only
  fields. A question that names no error or view fires nothing.
- **Routing untouched.** `route_sources()` is not changed. The discriminating
  signal is absent from every manifest column, so manifest-only routing
  genuinely cannot be fixed; cycle-2 job-05 also found router re-ranking
  regression-prone under the saturated 180 k budget. C2-07 makes context
  *assembly* resilient to the unavoidable routing miss instead.
- **Determinism, leakage checks, `--self-test`, and every retrieval-audit
  field are preserved.** The reference section shares the routed ceiling, so
  the 30 % lexical reserve is untouched, and it is re-offered in the dedup
  refill pass in cycle-1 priority order.

## 5. Result and the (a)/(b) split

### 5.1 Category (a) — retrieval defect, fixed

C2-07's reference section is non-empty for **24** of the 60 questions (17
errors, 7 views — the questions that name an error or view identifier in their
text). Isolating C2-07's own contribution (the other five domains are
byte-identical before and after, so this is exact):

| Domain | before C2-07 (cycle-2 jobs 05–06) | after C2-07 | Δ from C2-07 |
| --- | ---: | ---: | ---: |
| errors_troubleshooting | 124 / 198 | **166 / 198** | **+42** |
| views_performance_monitoring | 190 / 280 | **211 / 280** | **+21** |

No question regressed; 19 improved. Largest recoveries: ERR-126 3→9,
ERR-106 2→6, ERR-113 2→6, ERR-112 1→5, ERR-115 0→4, VPM-111 5→11, VPM-112 1→7,
VPM-114 3→8.

### 5.2 Category (b) — genuine source-content gaps

**None.** Every error code, symbol, message, view, and column the 60 questions
require is documented in `GPTs/upload_package/`. No question's required facts
are genuinely absent from the pack.

### 5.3 Residual misses — classified honestly

The C2-07 reference section is anchored on the identifier the question states.
The residual misses are **not** category-(b) content gaps; they split into:

**(i) Question-phrasing residuals.** The question does not name the error /
view identifier in its text, so the identifier-anchored section cannot fire and
the question falls back to lexical retrieval under the saturated budget. The
facts *are* in the pack. Errors: ERR-117, ERR-119, ERR-120, ERR-123, ERR-130
name no error symbol or hex code (e.g. ERR-117 says "insufficient-privilege
errors" rather than `qpERR_ABORT_QDP_INSUFFICIENT_PRIVILEGES`). Views: VPM-101,
VPM-103, VPM-104, VPM-106, VPM-107, VPM-108 name no `V$`/`SYS_` identifier
(e.g. VPM-107 says "performance views and columns … active SQL text" rather
than `V$STATEMENT`). This is the same residual class C2-06 recorded for
PROP-123 — a question-record phrasing weakness, recorded here, not papered
over.

**(ii) Token-form mismatches in the question records.** The fact is in the
assembled context; the question's `required_tokens` string just does not
literally match the source rendering, and the harness measures literal
substring presence. Per the C2-07 constraints the question records were **not**
edited. Examples: `V$LFG` / `V$LOG` (the data-dictionary manual
markdown-escapes the `$` in headings as `V\$LFG`, so the bare token matches
only where a body line happens to leave it unescaped), `re-execute` (ERR-108),
`unique key` (ERR-118), `ERR-31363` (ERR-122 — the manual indexes the error by
its `0x31363` reference code, not the `ERR-` runtime form), `/*+ hint */`
(VPM-120 — the manual shows real hints, not the placeholder).

**(iii) Out-of-mechanism-scope manuals.** A residual band of questions needs a
manual family the C2-07 error-reference / dictionary-view mechanism
deliberately does not cover: tool manuals (ERR-102 `dumptrc` — Utilities
Manual), the Performance Tuning Guide (VPM-115, VPM-118, VPM-119, VPM-121,
VPM-122), the Monitoring API Developer's Guide (VPM-125), and patch / release
notes (VPM-129, VPM-130). Those facts are in the pack; extending the
anchored-admission mechanism to a tool-procedure and release-note companion is
a worthwhile follow-up, left out of this job to keep the change scoped to the
error-reference and `V$`/`SYS_` reference tables the plan names and
regression-safe.

## 6. Per-question before → after

`before` = cycle-1 job-11 baseline; `after` = cycle-2 through C2-07. ✓ marks a
question C2-07's reference section directly moved.

| Question | version_scope | before | after | Δ | note |
| --- | --- | ---: | ---: | ---: | --- |
| ERR-101 | 7.3 | 4/7 | 6/7 | +2 | altierr — tool manual (scope) |
| ERR-102 | 7.3 | 2/8 | 2/8 | +0 | dumptrc — tool manual (scope) |
| ERR-103 | 7.3 | 8/8 | 8/8 | +0 | — |
| ERR-104 | 7.3 | 6/6 | 6/6 | +0 | — |
| ERR-105 | 7.3 | 3/5 | 5/5 | +2 | ✓ |
| ERR-106 | 7.3 | 2/6 | 6/6 | +4 | ✓ |
| ERR-107 | 7.3 | 5/5 | 5/5 | +0 | ✓ |
| ERR-108 | 7.3 | 1/6 | 5/6 | +4 | ✓ — `re-execute` token-form |
| ERR-109 | 7.3 | 4/5 | 5/5 | +1 | ✓ |
| ERR-110 | 7.3 | 2/5 | 5/5 | +3 | ✓ |
| ERR-111 | 7.3 | 5/5 | 5/5 | +0 | ✓ |
| ERR-112 | 7.3 | 1/5 | 5/5 | +4 | ✓ |
| ERR-113 | 7.3 | 2/6 | 6/6 | +4 | ✓ |
| ERR-114 | 7.3 | 2/5 | 5/5 | +3 | ✓ |
| ERR-115 | 7.3 | 0/4 | 4/4 | +4 | ✓ |
| ERR-116 | 7.3 | 8/8 | 8/8 | +0 | — |
| ERR-117 | 7.3 | 1/7 | 1/7 | +0 | phrasing — names no symbol |
| ERR-118 | 7.3 | 0/5 | 4/5 | +4 | ✓ — `unique key` token-form |
| ERR-119 | 7.3 | 2/8 | 2/8 | +0 | phrasing — names no symbol |
| ERR-120 | 7.3 | 6/8 | 6/8 | +0 | phrasing — names messages not symbols |
| ERR-121 | 7.3 | 6/6 | 6/6 | +0 | — |
| ERR-122 | cross-version | 3/6 | 5/6 | +2 | ✓ — `ERR-31363` runtime token-form |
| ERR-123 | cross-version | 4/10 | 4/10 | +0 | phrasing — names no symbol |
| ERR-124 | 8.1 | 3/6 | 6/6 | +3 | ✓ |
| ERR-125 | 8.1 | 8/8 | 8/8 | +0 | — |
| ERR-126 | cross-version | 3/9 | 9/9 | +6 | ✓ |
| ERR-127 | 7.3 | 8/8 | 8/8 | +0 | — |
| ERR-128 | 7.3 | 5/7 | 7/7 | +2 | ✓ |
| ERR-129 | 7.3 | 8/8 | 8/8 | +0 | ✓ |
| ERR-130 | 7.3 | 1/8 | 6/8 | +5 | phrasing — names no symbol |
| **errors total** | | **113/198** | **166/198** | **+53** | |
| VPM-101 | cross-version | 4/7 | 4/7 | +0 | phrasing — names no view |
| VPM-102 | 7.3 | 6/6 | 6/6 | +0 | ✓ |
| VPM-103 | 7.3 | 8/9 | 8/9 | +0 | phrasing — `V$DATATYPE` not named |
| VPM-104 | 7.3 | 0/10 | 4/10 | +4 | phrasing — names no view |
| VPM-105 | 7.3 | 11/11 | 11/11 | +0 | — |
| VPM-106 | 7.3 | 7/8 | 7/8 | +0 | phrasing — meta tables not named |
| VPM-107 | 7.3 | 4/13 | 4/13 | +0 | phrasing — names no view |
| VPM-108 | cross-version | 7/12 | 7/12 | +0 | phrasing — names no view |
| VPM-109 | cross-version | 8/9 | 9/9 | +1 | ✓ |
| VPM-110 | 7.3 | 8/11 | 11/11 | +3 | — |
| VPM-111 | 8.1 | 5/11 | 11/11 | +6 | ✓ |
| VPM-112 | 7.3 | 1/8 | 7/8 | +6 | ✓ — `V$LFG` escaped-heading token-form |
| VPM-113 | patch-specific | 7/8 | 8/8 | +1 | ✓ |
| VPM-114 | 7.3 | 3/9 | 8/9 | +5 | ✓ — `V$LOG` escaped-heading token-form |
| VPM-115 | cross-version | 1/7 | 1/7 | +0 | Performance Tuning Guide (scope) |
| VPM-116 | cross-version | 7/7 | 7/7 | +0 | — |
| VPM-117 | cross-version | 8/8 | 8/8 | +0 | — |
| VPM-118 | cross-version | 6/7 | 6/7 | +0 | Performance Tuning Guide (scope) |
| VPM-119 | 7.3 | 7/9 | 7/9 | +0 | Performance Tuning Guide (scope) |
| VPM-120 | cross-version | 6/7 | 6/7 | +0 | `/*+ hint */` placeholder token-form |
| VPM-121 | 7.3 | 3/9 | 3/9 | +0 | Performance Tuning Guide (scope) |
| VPM-122 | cross-version | 5/9 | 5/9 | +0 | Performance Tuning Guide (scope) |
| VPM-123 | cross-version | 5/5 | 5/5 | +0 | — |
| VPM-124 | cross-version | 13/13 | 13/13 | +0 | — |
| VPM-125 | cross-version | 0/13 | 0/13 | +0 | Monitoring API Guide (scope) |
| VPM-126 | cross-version | 13/13 | 13/13 | +0 | — |
| VPM-127 | 7.3 | 18/18 | 18/18 | +0 | — |
| VPM-128 | patch-specific | 3/9 | 9/9 | +6 | ✓ |
| VPM-129 | patch-specific | 2/6 | 2/6 | +0 | 8.1.0.0.1 Release Notes (scope) |
| VPM-130 | patch-specific | 3/8 | 3/8 | +0 | 7.1 Patch Notes (scope) |
| **views total** | | **179/280** | **211/280** | **+32** | |

## 7. No regression elsewhere

The C2-07 error-identifier and `V$`/`SYS_` patterns occur only in the two
target domains' question text. For all 230 questions of the other five domains
both section builders return an empty list, so `build_context()` is
byte-identical to the cycle-2 jobs 05–06 working tree. Verified empirically —
required-token-in-context unchanged to the token:

| Domain | jobs 05–06 | after C2-07 |
| --- | ---: | ---: |
| operations_admin | 208/251 | 208/251 |
| properties | 223/278 | 223/278 |
| replication_cdc_security_network | 256/311 | 256/311 |
| sql_ddl_dml_datatypes | 293/360 | 293/360 |
| tools_apis_connectors_migration | 322/374 | 322/374 |

Full-suite required-token-in-context: cycle-1 baseline 1517/2052 (73.9 %) →
after C2-07 **1679/2052 (81.8 %)**.

## 8. Acceptance

```
python3 evals/altibase_answerability/scripts/answer_runner.py --self-test     # OK
MODE=dry_run LIMIT=20 RUN_ID=c2_07_dryrun RUN_ROOT=/tmp/altibase-c2-07 \
  ./run-test.sh source-preserving                                             # 20 records, 0 errors
test -s /tmp/altibase-c2-07/answers/retrieval_audit.jsonl                     # 20-record sidecar
git diff --check                                                              # clean
```

Required-token-in-context for `errors_troubleshooting` (113/198 → 166/198,
+53) and `views_performance_monitoring` (179/280 → 211/280, +32),
reconstructed the same deterministic way before and after, **increases** versus
the cycle-1 baseline, with **zero regression** in the other five domains. The
investigation found the failure is category (a) — retrieval/scoring — with
**no genuine category-(b) source-content gap**; the residual misses are
question-phrasing residuals, question-record token-form mismatches, and a
band of out-of-mechanism-scope manuals (tool/Performance-Tuning/Monitoring-API/
patch-note), each documented above rather than papered over.

**C2-07: PASS.**
