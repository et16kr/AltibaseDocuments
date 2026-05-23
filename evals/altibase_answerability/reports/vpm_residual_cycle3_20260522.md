# `views_performance_monitoring` Residual Coverage — Cycle 3, C3-07

- Date: 2026-05-22
- Repository: `/home/et16/AltibaseDocuments`
- Master plan: `GPTs/reports/answerability_improvement_cycle3_plan_20260522.md` — item C3-07
- Evidence baseline: `evals/altibase_answerability/reports/full_rerun_analysis_cycle2_20260520.md`
  §6 target 2 — `views_performance_monitoring` (VPM) is tied for the worst domain
  at 10.0 % pass.
- C2-07 deep-dive resolved: `evals/altibase_answerability/reports/errors_views_deep_dive_cycle2_20260521.md`
- Reference pattern: `properties_deep_dive_cycle2_20260520.md` (C2-06),
  `errors_views_deep_dive_cycle2_20260521.md` (C2-07),
  `replication_deep_dive_cycle3_20260522.md` (C3-06).
- Scope: this job MAY modify `evals/altibase_answerability/scripts/answer_runner.py`
  only. No `GPTs/upload_package/` source bodies and no question records were
  modified.

## 1. Summary

C3-07 resolves the `views_performance_monitoring` residuals left by cycle-2 job
C2-07. The task is to classify every surviving VPM residual into:

- **(a) retrieval/assembly defect** — facts are in a routed source but not
  selected into context; fixable in `answer_runner.py`;
- **(b) out-of-mechanism-scope source gap** — facts live in a manual family the
  C2-07/C3-06 anchored-admission mechanism deliberately does not cover; out of
  this job's scope, reported here;
- **(c) question-phrasing residual** — the question is answerable but its
  wording does not route/anchor cleanly; the proper fix is C3-08
  (prose→identifier resolution), deferred there.

**Finding: there is no category-(a) residual left to fix.** The C2-07 dedicated
dictionary-view section (`build_dict_view_section`) already admits the whole
documented section of every `V$`/`X$`/`SYS_..._` identifier a VPM question names
in its text, regardless of the manifest routing decision. Re-verified
question-by-question on the **current** source pack: all seven view-naming VPM
questions have their named view's section admitted intact (see §4.1). No
performance-view definition block is split by chunking or starved by the
budget. **No `answer_runner.py` change is made by this job** — a speculative
retrieval/scoring change here would risk regression for no category-(a) gain,
which the job's "conservatively and deterministically" constraint forbids.

The 76 residual required-token misses (VPM is **204 / 280** required-tokens-in-
context on the current pack) therefore split entirely into **(b)** and **(c)**:

| Category | VPM questions | Missing tokens | Disposition |
| --- | ---: | ---: | --- |
| (a) retrieval/assembly defect | 0 | 0 | none — C2-07 mechanism verified complete |
| (b) out-of-mechanism-scope | 8 | 41 | reported §4.2; out of C3-07 scope |
| (c) question-phrasing residual | 6 | 32 | **handed to C3-08** §4.3 |
| question-record token-form artifact | 3 | 3 | reported §4.4; not a retrieval residual, not weakenable |
| **VPM total residual** | **17** | **76** | 204 / 280 in context |

The residuals are overwhelmingly **(b)/(c)**. Per the C3-07 acceptance criteria
("If the residuals are overwhelmingly (b)/(c), that is still a PASS provided the
report documents it precisely"), this is the documented outcome.

### 1.1 The cycle-2 → cycle-3 source-pack refresh

C2-07 (2026-05-21) reported VPM at **211 / 280** required-tokens-in-context.
The current pack measures **204 / 280**. The −7 is **not** a code regression: it
is the `IMG-01..06` image-content-recovery refresh of the source pack (shards
and `03_source_to_shard_manifest.md` regenerated, commit `1dc54cb6`,
2026-05-22 15:18 — before the cycle-3 job runner started 15:23). The same
refresh is documented in `replication_deep_dive_cycle3_20260522.md` §1, where it
*raised* replication by +9; for VPM it lowered three un-anchored questions
(VPM-106 7→6, VPM-107 4→1, VPM-108 7→4) because a larger pack tightens the
already-saturated 180 000-char budget and those three questions have no anchor
and depend on lexical fallback (they are all category (c) — see §4.3). The
`answer_runner.py` retrieval path (`build_context`, `score_chunk`,
`build_dict_view_section`) is byte-identical between the cycle-2 commit and the
current tree, confirmed by diff. C3-07's before/after is measured on **one
identical (current) pack**, the same discipline C3-06 used.

## 2. Method

Mirrors the C2-06/C2-07/C3-06 deep-dives.

1. `build_context()` was replayed deterministically with the in-package
   manifests (`02_source_manifest.md`, `03_source_to_shard_manifest.md`),
   exactly as `answer_runner.main()` runs it (`max_context_chars = 180000`,
   `chunk_chars = 8000`, lexical mode).
2. Each required token was checked for literal presence in the assembled
   context with `judge_report.literal_token_present` (the exact function the
   `--retrieval-recall` diagnostic and the rule judge use), and for presence
   anywhere in the source pack (both as-is and with markdown backslash escapes
   stripped).
3. Cross-validated with `judge_report.py --retrieval-recall` over a full
   270-question source-preserving dry-run: **270 / 270 faithful
   reconstructions**, VPM **204 / 280** — identical to the standalone replay,
   so the reconstruction is faithful to a real run's recorded audit.
   Artifact: `/tmp/altibase-c3-07-full/judge/retrieval_recall.json` (the dry-run
   is reproducible; the in-repo equivalent is regenerated by the C3-07
   acceptance dry-run).
4. The cycle-2 job-09 run
   `reports/full_benchmark/runs/altibase_source_preserving_20260521_220915_job09/`
   provided the routed-`source_id` audit for the diagnosis. (That run predates
   the `IMG-01..06` pack refresh, so its absolute numbers are the pre-refresh
   211/280 baseline; the routing decisions it records are unchanged.)

Full-suite required-token-in-context, current pack (for the §6 no-regression
check): ERR 166/198, OPS 205/251, PROP 221/278, REPL 265/311, SQL 289/360,
TOOL 322/374, VPM 204/280 — total **1672 / 2052 (81.5 %)**.

## 3. The C2-07 residual list

C2-07 (`errors_views_deep_dive_cycle2_20260521.md` §5.3, §6) enumerated the VPM
residuals after its fix as three classes: (i) question-phrasing residuals
(VPM-101, 103, 104, 106, 107, 108), (ii) question-record token-form mismatches
(VPM-112 `V$LFG`, VPM-114 `V$LOG`, VPM-120 `/*+ hint */`), and (iii)
out-of-mechanism-scope manuals (VPM-115, 118, 119, 121, 122 Performance Tuning
Guide; VPM-125 Monitoring API Developer's Guide; VPM-129, 130 release/patch
notes). C2-07 also recorded (§3.3, §5.2) that **no VPM residual is a genuine
category-(b) source-content gap** — every fact is documented somewhere in
`GPTs/upload_package/`.

C3-07 re-verified every one of those residuals independently on the current
pack. The C2-07 classification holds; the mapping onto the C3-07 (a)/(b)/(c)
scheme is below.

## 4. Classification — (a) / (b) / (c)

### 4.1 Category (a) — retrieval/assembly defect — 0 residuals

The C2-07 `build_dict_view_section` admits, regardless of routing, the whole
documented General Reference-2 section (description chunk + every following
column-detail chunk) of each `V$`/`X$`/`SYS_..._` identifier the question names
in its **text**. Seven VPM questions name such an identifier; all seven have the
named section admitted intact on the current pack:

| Question | named identifier(s) | in-context | section admitted whole? |
| --- | --- | ---: | --- |
| VPM-102 | `SYS_TABLES_` | 6 / 6 | yes |
| VPM-109 | `V$MEMGC` `V$TRANSACTION` `V$STATEMENT` | 9 / 9 | yes |
| VPM-111 | `V$BUFFPOOL_STAT` | 11 / 11 | yes |
| VPM-112 | `V$LFG` | 7 / 8 | yes — all 7 column tokens present; see §4.4 |
| VPM-113 | `V$LOCK_TABLE_STATS` | 8 / 8 | yes |
| VPM-114 | `V$LOG` | 8 / 9 | yes — all 8 column tokens present; see §4.4 |
| VPM-128 | `V$TEMPORARY_LOBS` | 9 / 9 | yes |

No named-view section is partially admitted, split by chunking, or starved by
the budget. The `D$` identifier form the C3-07 task names was checked: **no VPM
question text names a `D$` identifier and no `D$` object exists anywhere in
`GPTs/upload_package/`** (Altibase exposes performance views as `V$` and fixed
tables as `X$`; there is no `D$` namespace). Adding `D$` to the
`extract_dict_view_names` pattern would therefore be inert dead code, so it is
not added.

There is no category-(a) defect for a conservative `answer_runner.py` change to
close. C2-07's identifier-anchored section already did that work; C3-07 confirms
it.

### 4.2 Category (b) — out-of-mechanism-scope source gap — 8 residuals, 41 tokens

These questions need a manual **family** that the manifest router cannot single
out (every per-version manual row in `02_source_manifest.md` carries the same
generic title — the C2-06/07/C3-06 root cause) **and** that the C2-07/C3-06
identifier-anchored mechanism deliberately does not cover. The mechanism is
scoped to the Error Message Reference, the General Reference-2 dictionary-view
manual, and the Replication Manual; it does not cover the Performance Tuning
Guide, the Monitoring API Developer's Guide, or the release/patch-note families.
The facts **are** in the pack (these are not source-content gaps — see §3); the
gap is mechanism coverage.

| Question | in-context | manual family needed | missing tokens |
| --- | ---: | --- | --- |
| VPM-115 | 1 / 7 | `performance_tuning` (optimizer architecture) | `Query Rewriter`, `Logical Plan Generator`, `Physical Plan Generator`, `plan tree`, `SQL hints`; `optimizer-related properties` is a descriptive phrase not in the pack verbatim |
| VPM-118 | 6 / 7 | `performance_tuning` (predicate plan detail) | `VARIABLE KEY RANGE` |
| VPM-119 | 7 / 9 | `performance_tuning` (plan-tree reading) | `TEMP_TBS_MEMORY`, `TEMP_TBS_DISK` |
| VPM-121 | 3 / 9 | `performance_tuning` (join/access hints) | `ORDERED`, `USE_NL`, `USE_HASH`, `USE_SORT`, `NO_USE_HASH`, `FULL SCAN` |
| VPM-122 | 5 / 9 | `performance_tuning` (DBMS_STATS statistics) | `GATHER_SYSTEM_STATS`, `GATHER_TABLE_STATS`, `GATHER_INDEX_STATS`, `SET_SYSTEM_STATS` |
| VPM-125 | 0 / 13 | `monitoring_api_snmp` (Monitoring API Developer's Guide) | all 13 `ABIGet*` functions |
| VPM-129 | 2 / 6 | release notes — `8.1.0.0.1` JSON execution plan | `JSON`, `TRCLOG_EXPLAIN_TYPE`, `TRCLOG_JSON_PLAN_INDENT_DEPTH`, `V$PROPERTY` |
| VPM-130 | 3 / 8 | `patch_notes` — `7.1` JDBC view-query workaround | `x$`, `v$`, `That had return update result`, `OPTIMIZER_PERFORMANCE_VIEW`, `7.1.0.7.9` |

**Out-of-scope statement.** Resolving (b) means a *new* anchored-admission
builder for the Performance Tuning Guide, the Monitoring API Developer's Guide,
and the release/patch-note families — a separate retrieval job, larger than the
`V$`/`SYS_*`/`D$` dictionary-view scope the C3-07 task defines. C2-07 §5.3(iii)
already flagged this as "a worthwhile follow-up, left out of this job to keep
the change scoped … and regression-safe"; C3-07 keeps the same boundary and
recommends a dedicated follow-on job. These 41 tokens are **not** handed to
C3-08 unless C3-08's prose→identifier resolver is also extended to map prose
("optimizer", "Monitoring API functions", "statistics gathering") to a manual
family — that is a C3-08 design decision, noted but not assumed here.

### 4.3 Category (c) — question-phrasing residual — 6 residuals, 32 tokens — handed to C3-08

These questions are answerable from the General Reference-2 dictionary-view
manual that the C2-07 mechanism already admits whole **when the view is named**.
Their wording names the *facts* (column names, behaviours) but **not the
`V$`/`SYS_..._` identifier**, so `extract_dict_view_names` returns an empty set,
the identifier-anchored section does not fire, and the question falls back to
lexical retrieval under the saturated 180 000-char budget. They are not
category-(a) defects (no identifier to anchor on) and not category-(b) gaps (the
facts are in a family the mechanism *does* cover). The proper fix is **C3-08
prose→identifier resolution**: resolving the question's prose to the
`V$`/`SYS_..._` identifier lets the existing C2-07 section fire and admit the
section whole — and makes the question immune to the budget-pressure
sensitivity that the `IMG-01..06` pack refresh exposed (§1.1).

| Question | in-context | prose that must resolve to an identifier (C3-08) |
| --- | ---: | --- |
| VPM-101 | 4 / 7 | "performance view or column … which views should be checked" → `V$TABLE`, `V$ALLCOLUMN` |
| VPM-103 | 8 / 9 | "data type code" → `V$DATATYPE` (the `SYS_COLUMNS_` companion view) |
| VPM-104 | 4 / 10 | "meta tables … index definitions and index columns" → `SYS_INDICES_`, `SYS_INDEX_COLUMNS_` |
| VPM-106 | 6 / 8 | "meta tables … partition pruning, partition access, local index partition" → `SYS_TABLE_PARTITIONS_`, `SYS_PART_KEY_COLUMNS_`, `SYS_INDEX_PARTITIONS_` |
| VPM-107 | 1 / 13 | "performance views … active SQL text, timing, plan-cache linkage" → `V$STATEMENT`, `V$SQLTEXT` |
| VPM-108 | 4 / 12 | "lock-wait or wait-event investigation, which views" → `V$SESSION_WAIT`, `V$SESSION_EVENT`, `V$SESSION_WAIT_CLASS`, `V$LOCK_WAIT`, `V$LOCK_STATEMENT` |

C3-07 deliberately does **not** implement prose→identifier resolution here: the
C3-07 task instruction is explicit that C3-08 is the proper fix and that this
work must not be duplicated. Anchoring on a judge-only field
(`required_tokens`) is also forbidden by the harness leakage policy and the
C2-06/07 design discipline, so there is no in-scope way to fire the section for
these six questions from C3-07.

### 4.4 Question-record token-form artifacts — 3 tokens — not a retrieval residual

Three "missing" tokens are not retrieval failures at all — the correct content
**is** in the assembled context; the question record's required-token string
just does not literally match the source rendering, and the harness measures
literal substring presence. Per the C3-07 constraint the question records are
**not** edited (and must not be weakened).

| Question | token | reality |
| --- | --- | --- |
| VPM-112 | `V$LFG` | The C2-07 section admits the whole `V$LFG` view section; all 7 *column* tokens are in context. The General Reference-2 manual escapes the heading as `V\$LFG`, so the bare `V$LFG` literal matches only where a body line leaves it unescaped. The unescaped form also occurs in the Performance Tuning Guide Group-Commit section, which is not admitted (family out of mechanism scope, §4.2). |
| VPM-114 | `V$LOG` | Same: the `V$LOG` section is admitted whole, all 8 column tokens present; heading escaped as `V\$LOG`. |
| VPM-120 | `/*+ hint */` | A placeholder string; the manuals show concrete hints, not the literal placeholder `/*+ hint */`. The hint *facts* are in context (6/7). |

These are recorded honestly here rather than papered over; they are neither a
retrieval defect nor weakenable, so no action is taken.

## 5. What was fixed

Nothing in `answer_runner.py`. The category-(a) retrieval/assembly fix for VPM
was completed by cycle-2 job C2-07 (`build_dict_view_section` /
`extract_dict_view_names`); C3-07's independent re-verification on the current
pack (§4.1) confirms it is complete and that every named-view section is
admitted whole. The remaining 76-token residual is entirely (b)
out-of-mechanism-scope (41) and (c) question-phrasing (32) plus 3 question-record
token-form artifacts — none of which a conservative, deterministic,
regression-safe change inside the C3-07 scope can close. Making no code change
is therefore the correct outcome, and it guarantees zero regression elsewhere.

## 6. No regression

`answer_runner.py` is byte-identical to the pre-C3-07 working tree, so
`build_context()` is byte-identical for every question of all seven domains and
the coding-agent suite. Required-token-in-context, before == after:

| Domain | required-token-in-context (before == after) |
| --- | ---: |
| errors_troubleshooting | 166 / 198 |
| operations_admin | 205 / 251 |
| properties | 221 / 278 |
| replication_cdc_security_network | 265 / 311 |
| sql_ddl_dml_datatypes | 289 / 360 |
| tools_apis_connectors_migration | 322 / 374 |
| **views_performance_monitoring** | **204 / 280** |
| **full suite** | **1672 / 2052 (81.5 %)** |

The cycle-2 gains from C2-06/C2-07 and the C3-06 replication gain are preserved
(no code path touched). For category (a) — the empty set — required-token-in-
context is unchanged (0 → 0), vacuously satisfying the acceptance criterion.

## 7. Handed to C3-08

The six category-(c) questions — **VPM-101, VPM-103, VPM-104, VPM-106, VPM-107,
VPM-108** (32 missing tokens) — are handed to C3-08 (prose-named identifier
resolution). C3-08's resolver should map each question's prose to the
`V$`/`SYS_..._` identifier listed in §4.3; the existing C2-07
`build_dict_view_section` then fires and admits the section whole, with no
further change to the assembly code. This also removes these questions'
sensitivity to source-pack growth (§1.1).

## 8. Recommended follow-on (not C3-07, not C3-08)

The eight category-(b) questions need a new anchored-admission builder for the
`performance_tuning`, `monitoring_api_snmp`, and release/patch-note families —
the follow-up C2-07 §5.3(iii) flagged. This is out of scope for both C3-07
(scoped to `V$`/`SYS_*`/`D$` dictionary-view blocks) and C3-08 (prose→identifier
resolution), and should be a separate retrieval job.

## 9. Acceptance

```
python3 evals/altibase_answerability/scripts/answer_runner.py --self-test          # OK
test -f evals/altibase_answerability/reports/vpm_residual_cycle3_20260522.md        # present
MODE=dry_run LIMIT=20 RUN_ID=c3_07_vpm RUN_ROOT=/tmp/altibase-c3-07 \
  ./run-test.sh source-preserving                                                  # 20 records, 0 errors
test -s /tmp/altibase-c3-07/answers/retrieval_audit.jsonl                          # 20-record sidecar
git diff --check                                                                   # clean
```

VPM required-token-in-context, reconstructed the same deterministic way before
and after, is **204 / 280** — unchanged, because no `answer_runner.py` change is
warranted: the category-(a) defect was already closed by C2-07 and is verified
complete here. The residuals are **overwhelmingly (b)/(c)** — 41 tokens
out-of-mechanism-scope (reported §4.2), 32 tokens question-phrasing handed to
C3-08 (§4.3, §7), 3 question-record token-form artifacts (§4.4) — with **zero
regression** in the other six domains.

**C3-07: PASS** (residuals overwhelmingly (b)/(c), documented precisely;
no category-(a) defect remains).
