# Judge Gold Set Expansion — Cycle 3 (C3-02)

- Date: 2026-05-22
- Job: C3-02 — Expand and audit the judge gold set (52 → ~150)
- Plan: `GPTs/reports/answerability_improvement_cycle3_plan_20260522.md`
- File changed: `evals/altibase_answerability/fixtures/judge_gold_set.jsonl`
- Evidence motivating this job: `reports/full_rerun_analysis_cycle2_20260520.md`
  §6 target 4 — the 52-entry gold set was too small (one entry ≈ 1.9 %), and
  both residual cycle-2 judge disagreements (REPL-106 F04, REPL-108 F04) were
  borderline labels on it.

## 1. Summary

The judge gold set was expanded from **52 → 147 entries** (+95). The expanded
set is exactly domain-balanced at **21 entries per domain** across all seven
domains. Every new entry is weighted into the paraphrase-suspect `term_score`
band that the rule judge cannot resolve confidently. The two carried-over
borderline labels were re-audited against their source `expected_facts` and both
were **confirmed unchanged**.

The existing 52 entries were left byte-identical (`git diff` is 95 pure
insertions); the new 95 are appended.

## 2. Survey of the existing 52-entry set

- Schema (unchanged, reused verbatim): `question_id`, `fact_id`, `importance`,
  `fact_text`, `answer`, `required_tokens`, `label`, `notes`.
- 52 entries over 18 distinct questions; labels 29 `covered` / 23 `not_covered`;
  importance 50 `critical` / 2 `supporting`.
- Per-domain distribution was heavily skewed — `errors_troubleshooting` had a
  single entry, `views_performance_monitoring` had three — so a per-domain
  agreement estimate was not meaningful for five of the seven domains.
- Rule-judge `term_score` distribution of the 52: 6 below 0.40, 14 in 0.40–0.62,
  17 in 0.62–0.80, 10 in 0.80–1.00, 5 at exactly 1.00.

## 3. Before / after per-domain counts

| Domain | Before | Added | After |
| --- | ---: | ---: | ---: |
| errors_troubleshooting | 1 | +20 | 21 |
| operations_admin | 8 | +13 | 21 |
| properties | 13 | +8 | 21 |
| replication_cdc_security_network | 8 | +13 | 21 |
| sql_ddl_dml_datatypes | 12 | +9 | 21 |
| tools_apis_connectors_migration | 7 | +14 | 21 |
| views_performance_monitoring | 3 | +18 | 21 |
| **Total** | **52** | **+95** | **147** |

The final set is exactly even (21 per domain), so each domain now carries a
non-trivial, equally-weighted share of the ≥ 90 % agreement gate measured in
C3-05.

## 4. Source of the new entries

- All 95 new `answer` texts are copied **verbatim** from a real benchmark run —
  the cycle-2 job-09 full run
  `reports/full_benchmark/runs/altibase_source_preserving_20260521_220915_job09`
  (`answers/answers.jsonl`, 270 records). No answer text was synthesised.
- `fact_text` and `importance` are copied from each question's
  `expected_facts` entry; `required_tokens` is the question-level
  `required_tokens`. Both come unchanged from
  `evals/altibase_answerability/questions/*.jsonl`.
- The 95 facts span 27 distinct questions not previously represented as those
  `(question_id, fact_id)` pairs in the gold set.

## 5. Term_score-band coverage (priority on the hard band)

The rule judge (`judge_report.fact_match`) calls a fact `covered` at
`term_score ≥ 0.62` (plus a few technical-score combinations). The optional LLM
fact judge adjudicates the **paraphrase-suspect band** `term_score ∈ [0.40,
1.00]` excluding literal fact-text containment (`LLM_FACT_JUDGE_BAND_LOW = 0.40`,
`LLM_FACT_JUDGE_BAND_HIGH = 1.00` in `judge_report.py`). That band is exactly
where bag-of-words cannot tell a correct paraphrase from a near-miss, so all 95
new entries were selected into it.

| Rule-judge `term_score` band | Existing | New | Total |
| --- | ---: | ---: | ---: |
| < 0.40 (clearly missed) | 6 | 0 | 6 |
| 0.40–0.62 (below threshold, paraphrase-suspect) | 14 | 15 | 29 |
| 0.62–0.80 (above threshold, paraphrase-suspect) | 17 | 32 | 49 |
| 0.80–1.00 (high overlap, near-miss-suspect) | 10 | 32 | 42 |
| == 1.00 (total overlap, near-miss-suspect) | 5 | 16 | 21 |
| exact fact-text containment | 0 | 0 | 0 |

Every new entry lands in `[0.40, 1.00]`; none are in the trivially-missed
(`< 0.40`) or literal-containment zones. 48 of the 95 sit at `term_score ≥ 0.80`
— the zone where the cycle-2 analysis documented the rule judge's residual
over-credits (a wrong answer can reach a full 1.00 bag-of-words overlap). The
expansion deliberately concentrates the gold set where the judge calibration is
hardest.

## 6. Labelling policy

Each entry is labelled **by meaning, not by wording**:

- `covered` — the answer substantively conveys the core assertion of the fact.
  A correct paraphrase counts; different wording, structure, or omission of a
  secondary/incidental detail does not matter. When a fact states a rule plus a
  qualifier or exception, an answer that states the rule correctly is `covered`
  even if it omits the qualifier. When a fact lists several items, an answer is
  `covered` if it conveys the restriction and most of the listed items.
- `not_covered` — the answer omits the core assertion, contradicts it, states a
  materially different or opposite claim, or explicitly declines to state it.
  Mere keyword overlap with no real assertion of the fact is not coverage.

This is the same decision rule the LLM fact judge is prompted with
(`build_llm_fact_judge_prompt` in `judge_report.py`), applied here by a careful
human-style read of each `fact_text` against its full `answer`. Each entry's
`notes` field carries a one-line justification naming what the answer does or
does not convey.

New-entry label split: **82 `covered` / 13 `not_covered`**. The 13 `not_covered`
are genuine omissions or declines, e.g.:

- `TOOL-038 F03` — `term_score` 1.00 (every fact word appears) yet `not_covered`:
  the answer explicitly states the `build` / `reconcile` CLI syntax is *not
  available* and supplies only `run`. A pure near-miss the rule judge cannot
  catch.
- `TOOL-002 F04` — the answer explicitly declines to state whether a stored
  function called from SQL may perform DML or transaction control.
- `OPS-110 F01 / F04`, `OPS-116 F01 / F03`, `VPM-127 F02`, `VPM-128 F01` — the
  answer uses the relevant identifiers but never asserts the specific
  fact (relative-path resolution, view phase-availability, the "only offline"
  property, `altiPropertyTable`'s read/change role, the 8.1.0.0.1 "no meta
  tables changed" release note).
- `SQL-104 F02 / F04`, `SQL-105 F02`, `TOOL-001 F04`, `REPL-116 F01` — a distinct
  core assertion (a privilege requirement, a permanent-object DDL alternative,
  `ON COMMIT DELETE ROWS` semantics, which `AUTHID` mode is the default, how an
  XLog is obtained) is missing although related words are present.

Combined set label split: 111 `covered` / 36 `not_covered` over 147 entries —
enough of both classes for a stable precision and recall estimate in C3-05.

## 7. Re-audit of the borderline labels (REPL-106 F04, REPL-108 F04)

Both were re-examined against their question's `expected_facts` in
`questions/replication_cdc_security_network.jsonl` and the job-09 answer text.

### REPL-106 F04 — confirmed `not_covered`

Fact: *"DROP TABLE removes a table or partition from replication, but if master
transaction logs or table meta logs for that target remain in the replication
gap, the gap is given up and data mismatch can occur."*

The fact is a compound: a trivial operational clause (`DROP TABLE` removes a
table from replication) plus the distinctive clause — the **gap-given-up /
data-mismatch risk**. The answer states only that `DROP TABLE` removes a table
when replication is stopped; it never warns about the gap being given up or the
resulting data mismatch. In a "protected runbook" question the risk warning is
the gold-worthy content of F04, and it is entirely absent. **Label confirmed:
`not_covered`.**

### REPL-108 F04 — confirmed `covered`

Fact: *"The PARALLEL applier option creates multiple appliers to improve
replication performance by distributing received XLogs by transaction, but
commit synchronization can reduce the benefit."*

The answer states the `PARALLEL` option is "the parallel applier option for
receiver-side parallel apply", names `PARALLEL_APPLIER_COUNT` as "the number of
parallel applier", and gives the `0 ~ 512` count range — all inside a runbook
explicitly framed "For Altibase 7.3 tuning". That conveys the core assertion:
`PARALLEL` creates multiple receiver-side appliers as a performance/tuning
feature. It omits the "distributing received XLogs by transaction" mechanism and
the "commit synchronization can reduce the benefit" caveat — mechanism detail
and a qualifier, which under the §6 policy do not flip the label. **Label
confirmed: `covered`.**

Neither label was changed; the residual cycle-2 disagreements were genuine
borderline cases, and both stand after re-audit.

## 8. Verification

- `python3 -c "... assert len(rows)>=140 ..."` — 147 entries, all valid JSONL,
  all required fields present, all labels in `{covered, not_covered}`. **Pass.**
- `python3 evals/altibase_answerability/scripts/judge_report.py --self-test` —
  **Pass** (judge self-test green).
- `python3 evals/altibase_answerability/scripts/calibrate_judge.py --gold
  evals/altibase_answerability/fixtures/judge_gold_set.jsonl` — runs the
  rule-only calibration on the expanded set. **Pass** (rule judge vs. gold:
  agreement 0.8231, precision 0.8346, recall 0.9550, TP 106 / FP 21 / FN 5 /
  TN 15). The 21 rule-judge false positives are the expected paraphrase-suspect
  over-credits this expansion was built to surface; the LLM fact judge resolves
  them under C3-05.
- `git diff --check` — clean. The existing 52 entries are byte-identical (diff is
  95 pure insertions).

Only `fixtures/judge_gold_set.jsonl` and this report were modified. No judge or
retrieval code, no `GPTs/upload_package/` content, and no question records were
touched.
