# `replication_cdc_security_network` Domain Deep-Dive — Cycle 3, C3-06

- Date: 2026-05-22
- Repository: `/home/et16/AltibaseDocuments`
- Master plan: `GPTs/reports/answerability_improvement_cycle3_plan_20260522.md` — item C3-06
- Evidence baseline: `evals/altibase_answerability/reports/full_rerun_analysis_cycle2_20260520.md`
  §6 target 2 — `views_performance_monitoring` and `replication_cdc_security_network`
  are the two worst domains (10.0 % pass each); replication had **no dedicated
  cycle-2 builder**.
- Reference pattern: `properties_deep_dive_cycle2_20260520.md` (C2-06) and
  `errors_views_deep_dive_cycle2_20260521.md` (C2-07).
- Scope: `evals/altibase_answerability/scripts/answer_runner.py` only. No
  `GPTs/upload_package/` source bodies and no question records were modified.

## 1. Summary

`replication_cdc_security_network` was the one worst domain that never received
the cycle-2 identifier-anchored named-definition treatment that C2-06 gave
`properties` and C2-07 gave `errors`/`views`. Its 30 questions ask about
replication DDL clauses (`CREATE`/`ALTER`/`DROP REPLICATION` and the `ALTER`
sub-commands `START`/`STOP`/`SYNC`/`QUICKSTART`/…), replication option blocks
(Gapless, Parallel Applier, Meta Logging, Offline) and the replication
monitoring views — all documented in the Replication Manual and General
Reference-2, both of which the manifest router cannot single out (every
per-version manual row carries the same generic title, exactly the C2-06/07
root cause).

Unlike `properties`/`errors`/`views`, replication was **not** badly broken:
required-token-in-context was already **265 / 311 (85.2 %)** before this job,
because (i) many replication questions name the manual in their text and so
route correctly on the manifest `title` column, and (ii) the C2-06 property
section already covers the `REPLICATION_*` properties the questions name. The
remaining gap is real but **narrower** than the other three domains'.

This is a **category-(a) retrieval/assembly problem with no genuine
category-(b) source-content gap**: every required token is documented somewhere
in `GPTs/upload_package/`.

The fix (C3-06) adds a dedicated, highest-priority **replication-clause
section** to `build_context()` that admits — regardless of routing — the
Replication Manual clause/option section a question's named clause points at,
plus the replication monitoring views (`V$REPSENDER`/`V$REPSYNC`/…) as the
documented companion. It is anchored on replication-clause phrases verified to
occur only in replication-domain question text, so `build_context()` stays
byte-identical for every non-replication question.

| Metric (30 `replication_cdc_security_network` questions, 311 required tokens) | Before | After |
| --- | ---: | ---: |
| Required tokens literally in assembled context | 265 / 311 (85.2 %) | **273 / 311 (87.8 %)** |
| Questions improved / unchanged / regressed | — | **5 / 25 / 0** |

"Before" is the current `build_context()` (cycle-2 final state, pre-C3-06);
"after" is the same harness with the C3-06 change. Both are reconstructed the
same deterministic way and the rebuild is reproducible. The cycle-2 report
published replication at 256/311; the +9 to the 265 "before" is the unrelated
`IMG-01..06` image-content recovery refresh of the source pack (the shards and
manifests were regenerated on 2026-05-22), not a `build_context()` change — the
before/after here is measured on one identical pack.

The same C3-06 builder also lifts the three replication-domain questions of the
coding-agent suite that name a clause — **AGENT-007 5→8, AGENT-023 4→8,
AGENT-024 6→8 (+9)** — so the domain total across all 37 replication questions
is **306/367 → 323/367 (+17)**.

## 2. Method

Mirrors the C2-06/C2-07 deep-dives. For the 30 questions of
`evals/altibase_answerability/questions/replication_cdc_security_network.jsonl`:

1. `build_context()` was replayed deterministically with the in-package
   manifests (`02_source_manifest.md`, `03_source_to_shard_manifest.md`),
   exactly as `answer_runner.main()` runs it (`max_context_chars = 180000`,
   `chunk_chars = 8000`, lexical mode).
2. Each required token was checked three ways: literally present in the
   assembled context; present in the question's *expected* source blocks (its
   `source_refs` `source_path`s); present anywhere in the source pack.
3. The cycle-2 job-09 retrieval-audit sidecar
   (`…/runs/altibase_source_preserving_20260521_220915_job09/answers/retrieval_audit.jsonl`)
   gave the per-question routed `source_id`s used in the diagnosis.
4. The before/after comparison was reconstructed against a faithful pre-C3-06
   copy of `build_context()` and verified byte-identical for every
   non-replication question across both benchmark manifests (270 + coding-agent).

## 3. Root cause — why `replication` questions fail

### 3.1 The router cannot single out the Replication Manual (category a)

`route_sources()` scores `02_source_manifest.md` rows by question-token overlap
on `title`, `source_family`, `source_path`, `version_scope`, `language`. Every
per-version Replication Manual row (`replication_manual` family — `SRC-000132`
7.3-ko, `SRC-000101` 7.3-en, `SRC-000192` 8.1-ko, …) carries the same generic
title (`Replication Manual`, `Trunk`) as the version's other manuals, and the
discriminating token — the clause name, the option name, the `V$REP…`
identifier — appears in **no** `02_source_manifest.md` column. Where a question
does *not* name the manual, routing mis-selects and the wrong manual then
floods the budget via `ROUTED_SOURCE_BONUS = 100 000`.

The job-09 audit confirms the split: replication questions that name "Replication
Manual"/"Log Analyzer"/"Replication Manager" in their text route correctly on
the `title` column (REPL-103/104/107/108/109 → Replication Manual;
REPL-113/114/116 → Log Analyzer; REPL-119/120/128 → Replication Manager). The
rest mis-route — REPL-106 routed five English-aid manuals, REPL-115 routed five
unrelated sources, REPL-118 routed five unrelated sources.

### 3.2 Even a correct route does not place the right clause section (category a)

The Replication Manual is ~250 KB. A correct route applies the routed bonus to
*every* one of its chunks, but the 180 000-char budget cannot hold them all, so
the specific clause/option section a question needs competes on plain lexical
score against the rest of the manual. The replication monitoring-view facts the
questions need (`REPL_MODE`, `ACT_REPL_MODE`, `START_FLAG`, `NET_ERROR_FLAG`,
`SYNC_RECORD_COUNT`) live in a *different* manual again — General Reference-2 —
which the question never names, so they are doubly out of reach.

### 3.3 The facts are in the pack — there is no category (b)

Every one of the 311 required tokens is documented in `GPTs/upload_package/`.
Three tokens the literal-substring check flagged as "absent"
(`V$REPOFFLINE_STATUS`, `START AT SN`, `Intel Linux`) were each verified to be a
**token-form mismatch**, not a missing fact — see §5.3. So for every question
the failure is **category (a)** — the fact is in the pack but retrieval/assembly
does not bring it into context — never **category (b)**.

## 4. The fix (category a)

`build_context()` gains a dedicated **replication-clause section** (C3-06),
assembled at the same highest priority as the C2-06 property-definition section
and the C2-07 reference section — after the routing metadata and *before* the
routed section — so a generic-titled mis-route can no longer starve a named
clause's documented block. New code, all in `answer_runner.py`:

- `extract_replication_anchors()` — pulls the replication-clause anchor phrases a
  question names from the **question text only** (`alter replication`,
  `drop replication`, `quickstart`, `sync only`, `start with offline`,
  `meta_logging`, `gapless`, `parallel applier`, `replication mode`,
  `replication host`) and maps them to Replication Manual section keys.
- `build_replication_section()` — admits, version-filtered:
  1. the **Replication Manual clause/option section(s)** the named clause points
     at, from the `replication_manual` family — the section heading chunk and
     every following generic sub-section chunk (`구문`/Syntax, `설명`/Description,
     `예제`/Example, …), walked in document order; and
  2. the **replication monitoring-view companion** — `V$REPSENDER`,
     `V$REPRECEIVER`, `V$REPGAP`, `V$REPSYNC`, `V$REPOFFLINE_STATUS` — from the
     General Reference-2 data-dictionary manual, the documented companion that
     carries the `REPL_MODE`/`START_FLAG`/`SYNC_RECORD_COUNT` column facts (the
     analogue of the C2-06 `V$PROPERTY` companion).
- `_normalize_heading()` — folds the markdown-escape / bold / curly-quote /
  whitespace differences across the Korean and English manual copies so the
  clause-heading lookup is an exact match (a procedure heading such as
  `세션의 이중화 모드 설정` is therefore not mistaken for the `이중화 모드` section).

Design points (the same discipline as C2-06/07):

- **Anchored on the question's own text, replication-exclusive by construction.**
  Every anchor phrase was verified across all seven full-suite domains and the
  coding-agent suite to occur **only** in `replication_cdc_security_network`
  question text. `create replication` is deliberately *not* an anchor phrase
  (it also occurs in `sql_ddl_dml_datatypes` question text — SQL-140/141); the
  CREATE REPLICATION section is still reachable via the `create` section key
  carried by the `replication host` anchor (host-failover questions need the
  `WITH`/`USING` connection-type clause documented under CREATE REPLICATION).
  For every question that names no replication clause the builder returns an
  empty list, so `build_context()` is **byte-identical to before**.
- **Routing untouched.** `route_sources()` is not changed; cycle-1/2 found
  router re-ranking regression-prone under the saturated 180 k budget. C3-06
  makes context *assembly* resilient to the unavoidable routing miss instead.
- **Determinism, `max_context_chars`, leakage checks, `--self-test`, and every
  retrieval-audit field are preserved.** The new section shares the routed
  ceiling (the 30 % lexical reserve is untouched) and is re-offered in the
  C2-05 dedup refill pass in priority order. Only the allowlisted question
  projection and the in-package manifests/blocks are used.

## 5. Result and the (a)/(b) split

### 5.1 Category (a) — retrieval defect, fixed

C3-06's replication section is non-empty for **8** of the 30 questions (the ones
that name a replication clause/option). Five improved; three were already
complete and stayed complete — the builder made their assembly
routing-independent without regressing them. **Zero questions regressed.**

| Question | version | before | after | Δ | anchor → what was recovered |
| --- | --- | ---: | ---: | ---: | --- |
| REPL-102 | cross-version | 5/7 | **7/7** | +2 | `replication mode` → `V$REPSENDER` companion: `REPL_MODE`, `ACT_REPL_MODE` |
| REPL-106 | 7.3 | 11/13 | **13/13** | +2 | `quickstart` → `V$REPSENDER` companion: `START_FLAG`, `NET_ERROR_FLAG` |
| REPL-107 | 7.3 | 8/10 | **9/10** | +1 | `alter replication`/`sync only` → `V$REPSYNC` companion: `SYNC_RECORD_COUNT` |
| REPL-110 | cross-version | 7/10 | **9/10** | +2 | `replication host` → host + CREATE REPLICATION sections: `SET HOST`, `IB_ENABLE` |
| REPL-130 | 8.1 | 8/9 | **9/9** | +1 | `meta_logging` → Meta Logging Option section: `Restart SN` |
| **Total** | | **265/311** | **273/311** | **+8** | |

Coding-agent corroboration (replication-domain, coding-agent suite, same
builder): AGENT-007 5/8→8/8, AGENT-023 4/8→8/8, AGENT-024 6/8→8/8 (**+9**).

### 5.2 Category (b) — genuine source-content gaps

**None.** Every error code, clause, option, property, view and column the 30
`replication_cdc_security_network` questions require is documented in
`GPTs/upload_package/`. No question's required facts are genuinely absent.

### 5.3 Residual misses (38 token occurrences) — classified honestly

The 38 still-missing token occurrences split into three honest classes; none is
a category-(b) content gap.

**(i) Token-form mismatches in the question records — 6 occurrences.** The fact
*is* in the assembled context; the question's `required_tokens` string does not
literally match the source rendering, and the harness measures literal substring
presence. Per the C3-06 constraints the question records were **not** edited.

- `V$REPSYNC` (REPL-107) and `V$REPOFFLINE_STATUS` (REPL-109): the
  data-dictionary manual markdown-escapes the `$` in headings (`V\$REPSYNC`,
  `V\$REPOFFLINE_STATUS`) — `v$repsync` matches 0× / `v\$repsync` 0× vs 24×.
  C3-06 *does* admit both view sections; the bare `V$…` token stays
  escape-sensitive. This is the identical class C2-06 recorded for `V$PROPERTY`.
- `read-only`, `single value` (REPL-112): the `REPLICATION_SSL_PORT_NO`
  definition block (admitted by the C2-06 property section) renders the
  attribute in Korean (`읽기 전용` / `단일 값`); the English token matches only the
  English-aid copy.
- `START AT SN` (REPL-114): the Log Analyzer manual documents the clause as
  `START [AT SN …]` with the SQL optional-syntax bracket (`start [at sn` 6×);
  the required token drops the `[`.
- `Intel Linux` (REPL-123): the SSL/TLS guide writes `Intel-Linux` (hyphenated,
  4×) — the form REPL-121's own `required_tokens` use; REPL-123 uses the
  space form.

**(ii) Out-of-mechanism-scope category-(a) misses — 31 occurrences.** A residual
band of questions needs a manual family the C3-06 clause/property/view
mechanism deliberately does not cover, and additionally names no identifier in
its text (it states the need in prose), so an identifier-anchored builder cannot
fire. The facts *are* in the pack. This is the same residual class C2-07
recorded for its Performance-Tuning-Guide / Monitoring-API band.

- **Log Analyzer manual / API** — REPL-115 (8: `ALA_FAILURE`, `ALA_ErrorMgr`,
  `ALA_GetErrorCode`, `ALA_GetErrorLevel`, `ALA_GetErrorMessage`,
  `ALA_ERROR_FATAL`, `ALA_ERROR_ABORT`, `ALA_ERROR_INFO`); REPL-114
  (`archive log mode`). The `ALA_*` API is not a replication *clause*; REPL-115
  names no `ALA_*` symbol in its text.
- **Technical documents** — REPL-117 (2: `7.4.9`, `offline replication` —
  `ReplicationCompatibility.md`); REPL-118 (11: `insert_success_count`,
  `pstack`, `recvXlog`, `sendCmBlock`, `netstat -nrv`, `sendq`, `recvq`,
  `tcpdump`, `wireshark`, `REPLICATION_HBT_DETECT_TIME`, `TCP Dup ACK` —
  `Replication network check.md`). Both are tiny Korean-titled technical
  documents the router cannot match and the questions name in pure prose.
- **SSL/TLS guide** — REPL-123 (`OPENSSL_NO_HEARTBEATS`), REPL-124
  (`SSL_CIPHER_SUITES`).
- **Replication Manager manual** — REPL-128 (`JRE 8`).
- **Patch notes** — REPL-129 (6: `BUG-46940`, `7.1.0.2.4`, `restartXSN`,
  `DROP REPLICATION`, `7.4.4`, `7.4.5`).

Extending anchored admission to a Log-Analyzer-API, technical-document,
release/patch-note and SSL-guide companion — and resolving the prose-named
identifiers — is worthwhile follow-up work. It is left out of this job to keep
the change scoped to the replication clauses / properties / dictionary views the
plan names and regression-safe; the prose-named subset is the explicit remit of
**C3-08** (prose→identifier resolution).

**(iii) In-scope category-(a) residual — 1 occurrence.** REPL-110's
`DROP HOST ALL`: the contiguous literal `DROP HOST ALL` is documented in the
Replication Manual, but in the *Receive Only Option* section's cautions note
(`ALTER REPLICATION … DROP HOST ALL`) rather than the remote-host section the
`replication host` anchor admits. The remote-host section the builder *does*
admit recovered `SET HOST` and `IB_ENABLE`; the third token sits one section
away. A chunk-placement residual, recorded rather than papered over.

## 6. Per-question before → after

`before` = pre-C3-06 `build_context()`; `after` = with C3-06. ✓ marks a question
C3-06's replication section directly moved.

| Question | version_scope | before | after | Δ | note |
| --- | --- | ---: | ---: | ---: | --- |
| REPL-101 | cross-version | 10/10 | 10/10 | +0 | — |
| REPL-102 | cross-version | 5/7 | 7/7 | +2 | ✓ |
| REPL-103 | 7.3 | 10/10 | 10/10 | +0 | — |
| REPL-104 | 7.3 | 13/13 | 13/13 | +0 | — |
| REPL-105 | 7.3 | 12/12 | 12/12 | +0 | — |
| REPL-106 | 7.3 | 11/13 | 13/13 | +2 | ✓ |
| REPL-107 | 7.3 | 8/10 | 9/10 | +1 | ✓ — `V$REPSYNC` token-form |
| REPL-108 | 7.3 | 7/7 | 7/7 | +0 | builder fires, already complete |
| REPL-109 | 7.3 | 9/10 | 9/10 | +0 | builder fires; `V$REPOFFLINE_STATUS` token-form |
| REPL-110 | cross-version | 7/10 | 9/10 | +2 | ✓ — `DROP HOST ALL` residual (§5.3 iii) |
| REPL-111 | 8.1 | 9/9 | 9/9 | +0 | — |
| REPL-112 | 8.1 | 5/7 | 5/7 | +0 | `read-only`, `single value` token-form |
| REPL-113 | 7.3 | 11/11 | 11/11 | +0 | — |
| REPL-114 | 7.3 | 8/10 | 8/10 | +0 | `START AT SN` token-form; `archive log mode` scope |
| REPL-115 | 7.3 | 4/12 | 4/12 | +0 | Log Analyzer API (scope) — names no `ALA_*` |
| REPL-116 | 7.3 | 9/9 | 9/9 | +0 | — |
| REPL-117 | cross-version | 6/8 | 6/8 | +0 | ReplicationCompatibility doc (scope) |
| REPL-118 | cross-version | 1/12 | 1/12 | +0 | Replication network check doc (scope) |
| REPL-119 | cross-version | 12/12 | 12/12 | +0 | — |
| REPL-120 | 8.1 | 12/12 | 12/12 | +0 | builder fires, already complete |
| REPL-121 | 8.1 | 12/12 | 12/12 | +0 | — |
| REPL-122 | 8.1 | 12/12 | 12/12 | +0 | — |
| REPL-123 | 7.1 | 9/11 | 9/11 | +0 | `Intel Linux` token-form; `OPENSSL_NO_HEARTBEATS` scope |
| REPL-124 | 8.1 | 14/15 | 14/15 | +0 | `SSL_CIPHER_SUITES` — SSL/TLS guide (scope) |
| REPL-125 | cross-version | 8/8 | 8/8 | +0 | — |
| REPL-126 | patch-specific | 9/9 | 9/9 | +0 | — |
| REPL-127 | patch-specific | 9/9 | 9/9 | +0 | — |
| REPL-128 | patch-specific | 10/11 | 10/11 | +0 | `JRE 8` — Replication Manager (scope) |
| REPL-129 | patch-specific | 5/11 | 5/11 | +0 | 7.1.0.2.4 patch note (scope) |
| REPL-130 | 8.1 | 8/9 | 9/9 | +1 | ✓ |
| **Total** | | **265/311** | **273/311** | **+8** | 6 token-form, 31 scope, 1 chunk-placement |

## 7. No regression elsewhere

The C3-06 anchor phrases occur only in `replication_cdc_security_network`
question text. For all 240 questions of the other six full-suite domains —
**and all 23 non-replication questions of the coding-agent suite** —
`extract_replication_anchors()` returns an empty set, `build_replication_section()`
returns an empty list, and `build_context()` is **byte-identical to before**.
Verified empirically: the assembled-context SHA-256 digest is unchanged for
every one of the 263 non-replication questions across both benchmark manifests
(`full_benchmark_source_preserving_package.json` and
`coding_agent_source_preserving_package.json`).

## 8. Acceptance

```
python3 evals/altibase_answerability/scripts/answer_runner.py --self-test     # OK
test -f evals/altibase_answerability/reports/replication_deep_dive_cycle3_20260522.md  # present
MODE=dry_run LIMIT=20 RUN_ID=c3_06_repl RUN_ROOT=/tmp/altibase-c3-06 \
  ./run-test.sh source-preserving                                             # 20 records, 0 errors
test -s /tmp/altibase-c3-06/answers/retrieval_audit.jsonl                     # 20-record sidecar
git diff --check                                                              # clean
```

Required-token-in-context for the `replication_cdc_security_network` questions,
reconstructed the same deterministic way before and after, **increases
85.2 % → 87.8 % (+8 tokens)** for the category-(a) questions, with **zero
regressions** and **every non-replication question byte-identical**. The
investigation found the failure is category (a) — retrieval/assembly — with
**no genuine category-(b) source-content gap**; the residual 38 token
occurrences are 6 question-record token-form mismatches, 31 out-of-mechanism-
scope category-(a) misses (Log Analyzer API, technical documents, patch notes,
SSL/TLS guide, Replication Manager — the prose-named subset is C3-08's remit),
and 1 in-scope chunk-placement residual, each documented above rather than
papered over.

**C3-06: PASS.**
