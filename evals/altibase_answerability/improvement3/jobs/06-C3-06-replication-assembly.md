# Job 06 — C3-06 `replication_cdc_security_network` identifier-anchored assembly

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Master plan: `GPTs/reports/answerability_improvement_cycle3_plan_20260522.md` —
  item C3-06.
- Evidence: `evals/altibase_answerability/reports/full_rerun_analysis_cycle2_20260520.md`
  section **6, target 2** — `views_performance_monitoring` and
  `replication_cdc_security_network` are now the two worst domains (10.0% pass
  each). Replication had **no dedicated cycle-2 builder**; it never received the
  identifier-anchored named-definition treatment that cycle-2 jobs C2-06 and
  C2-07 applied to `properties` and to `errors`/`views`.
- Reference the C2-06/07 deep-dive reports for the pattern:
  `evals/altibase_answerability/reports/properties_deep_dive_cycle2_20260520.md`
  and `evals/altibase_answerability/reports/errors_views_deep_dive_cycle2_20260521.md`.
- The 30 replication questions are in
  `evals/altibase_answerability/questions/replication_cdc_security_network.jsonl`.

## Task

Apply the C2-06/07 named-definition admission pattern to replication objects.

1. **Investigate.** For the 30 `replication_cdc_security_network` questions, use
   the cycle-2 job-09 run
   (`altibase_source_preserving_20260521_220915_job09`), the retrieval-audit
   sidecar, and the `judge_report.py --retrieval-recall` diagnostic to determine,
   per question, whether each required token / critical fact is:
   - **(a) present in the routed source but not selected into context** — a
     retrieval/assembly defect this job must fix; or
   - **(b) genuinely absent from the source pack** — a source-content gap, OUT
     of harness scope, to be reported honestly, not papered over.
2. **Fix category (a)** in `answer_runner.py`'s `build_context()` by extending
   the C2-06/07 identifier-anchored named-definition admission to replication
   objects: replication clauses (e.g. `START`/`STOP`/`SYNC` and the
   `CREATE REPLICATION` clauses), `REPLICATION_*` properties, and the
   security/network meta-tables and dictionary views these questions ask about.
   The right definition block must be admitted whole.
3. **`build_context()` only; non-replication questions byte-identical.** The
   change must not alter the assembled context for any non-replication question —
   verify this explicitly.
4. **Report category (b) honestly** in a deep-dive report
   `evals/altibase_answerability/reports/replication_deep_dive_cycle3_20260522.md`:
   the (a)/(b) split, what was fixed, and the residual source-content gaps. Do
   NOT edit `GPTs/upload_package/` and do NOT weaken the question records.
5. Preserve determinism, `max_context_chars`, leakage checks, `--self-test`, and
   all retrieval-audit fields. Use only the question text and in-package
   manifests for routing.

## Constraints (non-negotiable)

- You MAY modify `evals/altibase_answerability/scripts/answer_runner.py`
  (`build_context()` and its helpers).
- Do NOT touch `GPTs/upload_package/` source bodies. Do NOT modify question
  records in `evals/altibase_answerability/questions/` — if a question looks
  wrong, record it in the report instead.
- Do not run `run-all.sh` or other jobs' files.

## Acceptance checks

```bash
python3 evals/altibase_answerability/scripts/answer_runner.py --self-test
test -f evals/altibase_answerability/reports/replication_deep_dive_cycle3_20260522.md
# Dry-run retrieval; the audit sidecar must still be produced:
MODE=dry_run LIMIT=20 RUN_ID=c3_06_repl RUN_ROOT=/tmp/altibase-c3-06 \
  ./run-test.sh source-preserving
test -s /tmp/altibase-c3-06/answers/retrieval_audit.jsonl
git diff --check
```

For PASS: required-token-in-context for the `replication_cdc_security_network`
questions, reconstructed the same way before and after, must **increase** versus
the cycle-2 baseline for the category-(a) questions, with non-replication
questions byte-identical, and the report must clearly separate the (a) fixes
from the (b) source-content gaps. If the failure is overwhelmingly category (b),
that is still a PASS provided the report documents it precisely — state that
plainly in the result.

## Completion protocol

As your final action:

- Ensure `evals/altibase_answerability/improvement3/state/` exists.
- If the acceptance checks passed and the deep-dive report is complete, write
  `evals/altibase_answerability/improvement3/state/06.result` with first line
  `PASS` and a short summary (the (a)/(b) split, before/after token-in-context
  for category (a), confirmation non-replication context is byte-identical).
- Otherwise write the same file with first line `FAIL: <one-line reason>`.
