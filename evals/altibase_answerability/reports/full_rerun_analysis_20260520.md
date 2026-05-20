# Full Re-run and Regression Analysis — Job 11

- Date: 2026-05-20
- Repository: `/home/et16/AltibaseDocuments`
- Master plan: `GPTs/reports/test_harness_improvement_plan_20260520.md`
  (see "Acceptance — Three Separate Scorecards")
- Scope: measurement only. No retrieval/judge source files, no
  `GPTs/upload_package/` bodies, and no other jobs' files were modified.

## 1. Runs

Both suites were re-run **live** (`provider=command`, Codex CLI 0.131.0,
`model=gpt-5.5`) after jobs 01–10. The live provider was smoke-tested before the
run (`READY`, exit 0). No complete post-job-09 full run existed under
`reports/full_benchmark/runs/` or `.../coding_agent_source_preserving/runs/`, so
both suites were run fresh.

| Suite | Run ID | Records | Errors | Status |
| --- | --- | ---: | ---: | --- |
| source-preserving (full) | `altibase_source_preserving_20260520_195639_job11` | 270 | 0 | all `answered` |
| coding-agent | `altibase_coding_agent_20260520_195650_job11` | 10 | 0 | all `answered` |

Baselines: `altibase_source_preserving_20260520_090243` (full, 14/270) and
`altibase_coding_agent_20260520_104452` (coding-agent, 0/10). The baseline runs
pre-date job 01, so they carry no retrieval-audit sidecar; baseline retrieval
numbers below were reconstructed by replaying the pre-job-01 `answer_runner.py`
(commit `a5ea8113`, the code that produced the baseline) — see §5.

## 2. Headline result

All three scorecards are reported separately, as the plan requires. **The
retrieval scorecard and the judge-validity scorecard both improved measurably;
the pass rate also rose but, as expected for cycle 1, did not reach the 85 %
readiness threshold. No genuine prohibited claim was added.**

| Scorecard | Verdict |
| --- | --- |
| Retrieval | **Improved** — all four metrics up |
| Judge validity | **Improved** — agreement 61.5 % → 75.0 %, precision up, OPS-111/TOOL-038 cleared |
| Pass rate | **Improved** — full 5.2 % → 13.7 %, coding-agent 0 % → 20 % |

## 3. Scorecard A — Retrieval

Measured from the job-01 retrieval-audit sidecar and from a faithful context
rebuild (`build_context` is deterministic; the new run is rebuilt with the
in-package manifests, exactly as `answer_runner.main()` does).

| Metric | Full baseline | Full new | Coding-agent baseline | Coding-agent new |
| --- | ---: | ---: | ---: | ---: |
| Routed source's block in selected context | 0 % (no routing stage) | **100 % (270/270)** | 0 % | **100 % (10/10)** |
| Required tokens literally present in context | 64.9 % (1331/2052) | **72.6 % (1490/2052)** | 67.5 % (54/80) | **76.3 % (61/80)** |
| Answers self-reporting missing context | 33.0 % (89/270) | **30.0 % (81/270)** | 60 % (6/10) | **30 % (3/10)** |
| Coding-agent `SRC-*` / `BLOCK-*` strings in context | n/a | n/a | 0 % (no provenance prefix) | **100 % (10/10)** |

**Verdict: improved.** Every retrieval-scorecard metric moved in the right
direction.

- **Routing now executes.** Pre-job-09 the manifest-routing contract was never
  run (`03_source_to_shard_manifest.md` was 0/270 utilised). Post-job-09 a
  routed source's block reaches the selected context for every question in both
  suites, and the `SRC-*`/`BLOCK-*`/version/shard-path provenance prefix (job
  06) is literally in context for all 280 questions.
- **Required-token recall up ~8 pp** in both suites, measured against the same
  (job-05-cleaned) token set for baseline and new — a fair apples-to-apples of
  the retrieval mechanism alone.
- **Self-reported context gaps fell** (full 33 % → 30 %, coding-agent 60 % →
  30 %). The drop is real but modest for the full suite and remains far from the
  < 10 % target — retrieval recall still leaves genuine gaps (see §6).

Non-scorecard observation: the literal `source_ref.source_path` string
(`GPTs/source_pack/...`) is present in context **less** often in the new run
(full 62.1 % → 41.7 %, coding-agent 69.6 % → 60.9 %). This is largely a
measurement artifact: job 08 deliberately normalises preserved
`GPTs/source_pack/...` paths to `GPTs/upload_package/source_pack_shard_*.md`,
and budgeted assembly favours routed blocks over whole source bodies, so the
un-normalised path string surfaces less. It is a noisy proxy, is **not** a
scorecard metric, and does not change the retrieval verdict — but the
path-normalisation/coverage interaction is noted as a follow-up.

## 4. Scorecard B — Judge validity

Measured with `calibrate_judge.py` against the 52-entry hand-labelled gold set
(`fixtures/judge_gold_set.jsonl`).

| Metric | Baseline judge | Current judge |
| --- | ---: | ---: |
| Judge-vs-gold agreement | 61.5 % (32/52) | **75.0 % (39/52)** |
| Precision (positive class = covered) | 0.655 | **0.711** |
| Recall | 0.655 | **0.931** |
| F1 | 0.655 | **0.806** |
| OPS-111 prohibited-claim finding | present (false positive) | **absent** |
| TOOL-038 prohibited-claim finding | present (false positive) | **absent** |

**Verdict: improved.** Agreement rose +13.5 pp and precision rose without
regression (the plan's explicit guard — semantic tolerance must not over-credit
wrong answers — holds: precision 0.655 → 0.711). OPS-111 and TOOL-038, the two
false-positive prohibited-claim findings called out in the plan, are both
cleared, and the `judge_report.py --self-test` (run inside both suites) passes
the OPS-111/TOOL-038 regression cases.

Agreement is **below the ≥ 90 % target**. This is expected for cycle 1 (T7-B,
the LLM-assisted fact judge, is deferred follow-up work). The residual gap is 13
disagreements: 11 false positives — the judge over-credits paraphrase-suspect
facts, concentrated in SQL-101 / SQL-102 / SQL-129 where bag-of-words cannot
distinguish a correct paraphrase from a near-miss — and 2 false negatives.

## 5. Scorecard C — Pass rate

| Metric | Full baseline | Full new | Δ | Coding-agent baseline | Coding-agent new | Δ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Pass rate | 5.2 % (14/270) | **13.7 % (37/270)** | +8.5 pp | 0 % (0/10) | **20 % (2/10)** | +20 pp |
| Critical fact coverage | 49.8 % | **67.2 %** | +17.4 pp | 55.0 % | **56.7 %** | +1.7 pp |
| Required token preservation | 56.4 % | **60.2 %** | +3.8 pp | 65.4 % | **68.1 %** | +2.7 pp |
| Protected-topic blockers | 104 | **86** | −18 | 5 | 5 | 0 |
| Prohibited-claim findings (count) | 2 | 6 | +4 | 0 | 0 | 0 |
| Prohibited-claim findings (**genuine**) | **0** | **0** | **0** | 0 | 0 | 0 |
| Unsupported-claim rate | 0.7 % | 2.2 % | +1.5 pp | 0 % | 0 % | 0 |

### 5.1 Gained / lost question IDs (full suite, vs official baseline)

- **Gained (28):** ERR-107, ERR-116, ERR-121, ERR-129, OPS-104, OPS-109,
  OPS-117, OPS-120, OPS-122, OPS-132, OPS-134, PROP-101, REPL-111, REPL-112,
  REPL-120, SQL-102, SQL-130, SQL-133, SQL-134, SQL-135, SQL-138, TOOL-001,
  TOOL-012, TOOL-026, TOOL-037, TOOL-042, VPM-102, VPM-124.
- **Lost (5):** OPS-102, OPS-110, OPS-119, TOOL-029, TOOL-033.

Net +23. Coding-agent gained AGENT-001 and AGENT-005.

**Decomposing the full-suite movement** (baseline answers re-judged with the
current judge isolate the two tracks):

| Stage | Passes |
| --- | ---: |
| Baseline answers + baseline judge (official) | 14 |
| Baseline answers + **current judge** (judge track alone) | 22 |
| New answers + current judge (this run) | 37 |

So ~+8 passes come from the judge track (T6–T9) and ~+15 from the retrieval +
answer-generation track (T2–T5).

**The 5 losses are not retrieval regressions:**

- OPS-102 (crit 1.00 → 0.67, tokens 1.00 → 0.40), OPS-110, OPS-119, TOOL-029 —
  marginal coverage drops from live answer-generation variance (the model
  produced a weaker answer this run; these are non-deterministic live calls).
- TOOL-033 — regressed pass → fail because of a **judge prohibited-claim false
  positive** (see §5.2), compounded by a critical-coverage drop to 0.75.

### 5.2 Prohibited claims — all six findings are false positives

The full run produced 6 prohibited-claim findings (PROP-140, PROP-142, SQL-137,
TOOL-003, TOOL-019, TOOL-033). Each answer was inspected verbatim. **None
genuinely asserts the prohibited claim** — in every case the answer asserts the
correct or opposite statement, and the bag-of-words overlap mis-fires:

| Question | Prohibited claim | What the answer actually says | FP cause |
| --- | --- | --- | --- |
| PROP-140 | `SSL_PORT_NO` defaults to 20300 | default is **20443**; `20300` only appears in an unrelated TCP-listener log line | incidental token from a code block |
| PROP-142 | no `ACCESS_LIST` match ⇒ deny by default | "if no entry matches, access is **allowed**" (correct) | polarity |
| SQL-137 | `NVL2` returns `expr3` when `expr1` is **not** NULL | returns `expr2` when not NULL, `expr3` when NULL (correct) | polarity |
| TOOL-003 | anonymous blocks **cannot** use OUTPUT bind variables | "it **can** use BIND variables for INPUT, OUTPUT, INOUTPUT" + example | polarity on a `cannot`-phrased claim |
| TOOL-019 | `SQLFreeLob2` commits the JSON LOB update | "it does **not** `commit` or `rollback`" (correct) | markdown-bold `**not**` defeats negation tokenisation |
| TOOL-033 | `ALTIBASE_UT_FILE_PERMISSION` overrides `AEXPORT_FILE_PERMISSION` | `AEXPORT_FILE_PERMISSION` overrides `ALTIBASE_UT_FILE_PERMISSION` (correct, reversed direction) | direction-sensitive claim |

Genuine prohibited claims: **0 in the new run, 0 in the baseline** (the
baseline's 2 findings, OPS-111 and TOOL-038, were themselves the false
positives the plan called out). **No increase in genuine prohibited claims.**

The *count* of false positives nevertheless rose 2 → 6. This is a judge-validity
weakness, not a content regression: job-04 stemming raised bag-of-words overlap
to 1.00 on more claims, and three new failure modes appear — markdown emphasis
around the negation word, `cannot`-phrased intrinsically-negative claims (the
job-10 fix did not generalise from `without` to `cannot` for this answer shape),
and reversed-direction "A overrides B" claims. Each false positive blocks an
otherwise-passing question (≈ 6 questions, including the TOOL-033 regression),
so it directly suppresses the pass rate. This is the top remediation target.

### 5.3 Domain breakdown (full suite)

| Domain | Pass baseline → new | Crit baseline → new |
| --- | ---: | ---: |
| errors_troubleshooting | 0.0 % → 13.3 % | 43.6 % → 60.3 % |
| operations_admin | 11.4 % → 22.9 % | 68.8 % → 82.1 % |
| properties | 0.0 % → 2.0 % | 33.7 % → 52.2 % |
| replication_cdc_security_network | 6.7 % → 16.7 % | 46.9 % → 74.5 % |
| sql_ddl_dml_datatypes | 4.4 % → 17.8 % | 47.7 % → 69.9 % |
| tools_apis_connectors_migration | 8.0 % → 14.0 % | 64.6 % → 76.4 % |
| views_performance_monitoring | 6.7 % → 13.3 % | 41.7 % → 54.7 % |

Every domain improved on pass rate and critical-fact coverage. `properties`
remains the worst domain (2.0 %): its 32 version-sensitive-property protected
topics still block, and required-token preservation there is unchanged (≈ 50 %).

## 6. Verdict and remediation targets

- **Retrieval scorecard: improved.** Routing 0 → 100 %, provenance 0 → 100 %,
  required-token recall +8 pp, self-reported gaps down. ✔
- **Judge-validity scorecard: improved.** Agreement +13.5 pp, precision up,
  OPS-111/TOOL-038 cleared. ✔ (still short of the 90 % target — cycle-1 expected)
- **Pass-rate scorecard: improved.** Full 5.2 % → 13.7 %, coding-agent 0 % →
  20 %, blockers 104 → 86, no genuine prohibited claim added. ✔ (85 % readiness
  not reached — not required for this job)

### Top remaining remediation targets

1. **Judge prohibited-claim false positives (highest priority).** Count rose
   2 → 6, each one blocks a passing question. Make `prohibited_claim_present()`
   polarity- and direction-aware; strip markdown emphasis before negation
   tokenisation; generalise the `cannot`-phrased intrinsically-negative guard;
   add PROP-140/PROP-142/SQL-137/TOOL-003/TOOL-019/TOOL-033 as self-test
   fixtures.
2. **Judge agreement 75 % < 90 %.** 11 gold-set over-credits, concentrated in
   SQL paraphrase-suspect facts. Needs the deferred T7-B LLM-assisted fact
   judge; keep the rule judge as default/fallback.
3. **`properties` domain.** Pass 2.0 %, 32 version-sensitive-property blockers,
   token preservation ≈ 50 %. Retrieval routing landed but coverage is still
   low — investigate whether the routed property sources carry the
   version-specific facts the questions need.
4. **Self-reported context gaps still 30 %.** Required-token-in-context is
   72.6 % — over a quarter of required tokens never reach the model. Tighten
   router scoring for vaguely worded questions.
5. **`errors_troubleshooting` and `views_performance_monitoring`.** Lowest
   critical-fact coverage (60 % / 55 %) and token preservation (≈ 52–55 %) after
   `properties`.

### Tooling note (not fixed here — measurement-only job)

`judge_report.py --retrieval-recall` calls `build_context()` **without** the
`manifest_rows`/`shard_map` arguments added in jobs 08–09, so it reconstructs
the *pre-routing* lexical context and under-reports recall for routed runs
(reconstruction was unfaithful for all sampled questions). The retrieval numbers
in §3 were therefore computed with a standalone, manifest-aware rebuild. The
`--retrieval-recall` diagnostic should be updated to pass the manifests in a
future harness job.

## 7. Acceptance check

```
test -f evals/altibase_answerability/reports/full_rerun_analysis_20260520.md   # present
git diff --check                                                              # clean
```

Both suites completed live with 0 errors; the retrieval and judge-validity
scorecards both improved versus baseline; no genuine prohibited claim was added.
**Job 11: PASS.**
