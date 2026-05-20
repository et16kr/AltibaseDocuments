# Judge Pass-Logic and Threshold Consistency Decision (T8)

- Date: 2026-05-20
- Scope: `evals/altibase_answerability/scripts/judge_report.py` per-question
  `passed` decision; degenerate `required_tokens` in
  `evals/altibase_answerability/questions/*.jsonl`.
- Plan item: `GPTs/reports/test_harness_improvement_plan_20260520.md` section T8.
- Evidence:
  `GPTs/reports/source_preserving_test_analysis_and_plan_review_20260520.md`
  section 4.3.

## 1. What the pass logic was

`judge_answer()` decided a per-question pass with:

```python
passed = (
    severity in {"none", "low"}
    and overall >= 0.80
    and critical_fact_coverage >= 0.80
    and required_token_preservation >= 0.80
    and unsupported_claim_control == 1.0
)
```

This was internally inconsistent in two ways:

1. **The severity clause silently overrode the numeric thresholds.** Any missed
   critical fact emits a `high` finding; any missed required token emits a
   `medium` finding; no code path ever emits a `low` finding. So
   `severity in {"none", "low"}` collapsed in practice to "zero findings" — the
   bar was *lexically perfect reproduction*, not the policy bar. A question
   whose `critical_fact_coverage` / `required_token_preservation` were inside the
   ranges `policy.json` calls acceptable still auto-failed on a single
   near-miss finding.
2. **Every other clause was dead code.** Once `severity == "none"`, the answer
   already had full critical-fact coverage, full token preservation and no
   prohibited claim, so `overall >= 0.80`, `critical_fact_coverage >= 0.80` and
   `required_token_preservation >= 0.80` could never bind. The hardcoded `0.80`
   bars did not even match the policy values (`critical_fact_coverage_minimum`
   `= 0.90`, `required_token_preservation_minimum = 0.95`).

## 2. What the pass logic is now

The decision is made directly against `policy.json` `readiness_thresholds`
(the thresholds dict is now passed into `judge_answer()` from `run_judge()`):

```python
has_blocker_finding = any(item["severity"] == "blocker" for item in findings)
passed = (
    not has_blocker_finding
    and critical_fact_coverage >= thresholds["critical_fact_coverage_minimum"]
    and required_token_preservation >= thresholds["required_token_preservation_minimum"]
    and unsupported_claim_control == 1.0
)
```

A question passes when:

- **No `blocker` finding is present** — an unjudgeable answer (bad `status` or a
  failed leakage check) or a protected-topic blocker. This is the per-question
  form of `protected_topic_blockers_allowed == 0` plus the run-validity gate.
- **`critical_fact_coverage` meets `critical_fact_coverage_minimum`** (0.90).
- **`required_token_preservation` meets `required_token_preservation_minimum`**
  (0.95).
- **No prohibited claim is present** (`unsupported_claim_control == 1.0`) — the
  per-question form of `unsupported_claim_rate_maximum`.

`high`/`medium` near-miss findings still appear in each judgment's `findings`
list and still drive `max_severity`, the remediation targets and the markdown
report — they are remediation signal, but they no longer override a numeric
score that the policy says is acceptable.

## 3. Why this option

This is the recommended T8 option (reconcile the pass test with the stated
policy thresholds). No concrete blocker required choosing an alternative.

- **No dead code.** Each clause is independently load-bearing: clause 1 alone
  catches `status`/leakage blockers that no numeric score reflects; clauses 2–4
  each fail a non-protected-topic answer the others would pass (a missed
  critical fact, a missed token, and a prohibited claim are `high`/`high`/`high`
  or `medium` findings — not blockers — so only their own clause rejects them).
- **One source of truth.** Per-question pass thresholds and the aggregate
  `readiness_decision` now both read `policy.json`; changing a threshold there
  changes both. The previously hardcoded `0.80` constants are gone.
- **No silent override.** A near-miss finding inside the policy ranges no longer
  auto-fails the question. Per the evidence (§4.3), 25 questions failed *only*
  on `severity` while clearing every numeric threshold — exactly the silent
  override removed here.
- **`overall` is intentionally not a pass gate.** `policy.json` defines no
  per-question `overall` threshold (`overall_pass_rate_minimum` is the aggregate
  *pass rate*, already enforced in `readiness_decision`). Keeping a per-question
  `overall` bar would re-introduce a non-policy constant. `overall` remains
  computed and reported for ranking and diagnostics.
- **`version_handling` / `missing_input_handling` stay tracked-only**, exactly
  as `readiness_decision` already treats them (and as the markdown report labels
  them "Tracked"). They no longer gate a per-question pass via `severity`.
- The judge stays deterministic and offline; `judge_mode` remains `rule`.
- `policy.json` was **not changed** — no threshold value needed to move.

The self-test still holds: PROP-001 passes, OPS-001 fails and still produces a
`backup_recovery` protected-topic blocker, and the OPS-111 / TOOL-038
prohibited-claim regression cases still pass.

## 4. Degenerate required tokens fixed

A required token is degenerate when it is a single character (or punctuation
only) and so cannot be matched literally in a meaningful way: `literal_token_present`
either matches it against unrelated text (a bare `0` matches any standalone `0`;
`$` matches `V$...`) or fails it for non-substantive reasons. Such tokens are
noise in `required_token_preservation`. `expected_facts` were **not** changed;
only `required_tokens` were edited. 34 questions were changed.

### 4a. Removed (31 questions)

The degenerate token's meaning is already carried by another required token in
the same list (the property/column name, or the full URL string) and by the
`expected_facts`, so the bare character was removed.

| Question(s) | Removed | Rationale |
| --- | --- | --- |
| OPS-134 | `0` | Value for `REPLICATION_SENDER_AUTO_START` (token kept). |
| PROP-115, 121, 127, 135, 139 | `0` | Property value / range bound; property name and multi-char bounds kept. |
| PROP-116, 119, 131, 134, 141, 147, 150 | `0`, `1` | Property values; property name kept. |
| PROP-128 | `0` | Range value; `-1` and `65535` kept. |
| PROP-129, 143 | `1`, `0` | Property values; property name kept. |
| PROP-130 | `0`, `1`, `2` | Property values; `ARCHIVE_FULL_ACTION` kept. |
| PROP-136 | `2` | Range lower bound; `512` kept. |
| PROP-146 | `0`, `1` | Property values; version tokens `7.1`/`7.3`/`8.1` kept. |
| PROP-149 | `1` | Range minimum; `4000`/`32000` kept. |
| REPL-112 | `0` | Default value; `REPLICATION_SSL_PORT_NO`/`65535` kept. |
| SQL-131 | `1` | Value for `TEMPORARY_LOB_ENABLE` (token kept). |
| TOOL-001 | `/` | iSQL slash terminator; `END;` kept. No distinctive literal form. |
| TOOL-009 | `?`, `&` | URL separators already present inside the full JDBC URL token. |
| TOOL-046 | `1`, `6` | `AKU_SERVER_COUNT` range bounds; property name kept. |
| TOOL-047 | `0` | `SRID` default; `SRID` token kept. |
| VPM-102 | `T`,`S`,`V`,`Q`,`R`,`W`,`A` | Single-letter `TABLE_TYPE`/`ACCESS` value codes; column names kept. |
| VPM-103 | `V`,`F`,`L` | Single-letter `STORE_TYPE` value codes; column name kept. |
| VPM-104 | `A`,`D` | Single-letter `SORT_ORDER` value codes; column name kept. |
| VPM-106 | `R`,`W`,`A` | Single-letter `PARTITION_ACCESS` value codes; column name kept. |
| VPM-116 | `M` | Bare cost-notation symbol; `T(R)`/`V(R.a)`/`B(R)` kept. |

### 4b. Replaced with the meaningful token (3 questions)

Where the degenerate character clearly stood for a distinctive, literally
matchable phrase named in the `expected_facts`, it was replaced rather than
removed.

| Question | Change | Source justification |
| --- | --- | --- |
| REPL-128 | `6` → `JRE 6`, `8` → `JRE 8` | F02 ("JRE 6 or later") and F04 ("updated the JRE … from 6 to 8"). |
| SQL-142 | `_` → `underscore`, `$` → `dollar sign`, `#` → `hash sign` | F04 lists the allowed unquoted-name characters as "underscore, dollar sign, and hash sign". |
| VPM-117 | `??` → `question marks` | F04: post-execution values "are displayed as question marks" under `EXPLAIN PLAN = ONLY`. |

### 4c. Considered but kept (not degenerate)

- `(+)` (SQL-143) — the three-character Oracle outer-join operator; distinctive
  and literally matchable, and the subject of the question.
- `'.,'` (PROP-124) — the quoted `NLS_NUMERIC_CHARACTERS` value; a distinctive
  four-character string that is meaningful when matched literally.

## 5. Acceptance

```
python3 evals/altibase_answerability/scripts/judge_report.py --self-test            # OK
python3 evals/altibase_answerability/scripts/validate_benchmark.py \
  --manifest .../full_benchmark_source_preserving_package.json --profile full       # OK, 270 questions
python3 evals/altibase_answerability/scripts/validate_benchmark.py \
  --manifest .../coding_agent_source_preserving_package.json --profile coding_agent # OK, 10 questions
git diff --check                                                                   # clean
```
