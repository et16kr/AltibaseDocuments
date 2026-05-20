# Job 02 — C2-02 LLM-assisted fact judge (T7-B)

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Master plan: `GPTs/reports/test_harness_improvement_plan_20260520.md` —
  read section **T7, phase B** (the LLM-assisted judge), and
  `GPTs/reports/answerability_improvement_cycle2_plan_20260520.md` item C2-02.
- Evidence: `evals/altibase_answerability/reports/full_rerun_analysis_20260520.md`
  section **4** — the rule judge reaches only 75.0% judge-vs-gold agreement; the
  residual gap is 11 over-credits concentrated in SQL paraphrase-suspect facts
  (SQL-101 / SQL-102 / SQL-129) where bag-of-words cannot distinguish a correct
  paraphrase from a near-miss.
- Cycle 1 deferred this work; cycle 2 includes it. The deterministic rule judge
  stays the default and the fallback — the LLM judge only adjudicates the
  paraphrase-suspect band.

## Task

Add an optional LLM-assisted fact judge to
`evals/altibase_answerability/scripts/judge_report.py`.

1. **Opt-in, off by default.** Add an `--llm-fact-judge` flag (and/or a
   `JUDGE_LLM_FACT` env toggle). When OFF, behaviour is byte-for-byte the
   current deterministic rule judge. `--self-test` must run with it OFF so the
   self-test stays hermetic and deterministic.
2. **Adjudicate only the uncertain band.** The LLM judge is consulted only for
   facts whose rule-judge `term_score` falls in a paraphrase-suspect band
   (about 0.40–0.75 — confirm against the gold set notes). Facts the rule judge
   scores clearly covered or clearly missed are not sent to the LLM.
3. **Provider.** Reuse the existing command-provider plumbing the harness
   already uses for answer generation (Codex CLI; see
   `evals/altibase_answerability/scripts/codex_exec_provider.sh` and how
   `answer_runner.py` shells out). The LLM is asked a single, tightly scoped
   question: does this answer substantively convey this expected fact —
   `covered` or `not_covered` — judged by meaning, not wording.
4. **Caching + determinism.** Cache LLM verdicts keyed by a hash of
   `(fact_text, answer)` so re-runs are stable and cheap. On any error, timeout,
   or unavailable provider, **fall back to the rule-judge verdict** and record
   that the fallback was used. The judge must never hang or crash when the
   provider is missing.
5. **Stable interface.** Keep
   `fact_match(fact_text, answer, required_tokens) -> FactMatch` and its
   `.covered` attribute STABLE. The LLM verdict overrides `.covered` for
   in-band facts; everything `calibrate_judge.py` depends on stays the same.
6. **Literal tokens untouched.** Do not let the LLM judge affect
   `literal_token_present` / required-token preservation — that stays exact and
   deterministic. Only fact-term coverage may use the LLM verdict.
7. **calibrate_judge.py wiring.** Add a matching opt-in flag to
   `evals/altibase_answerability/scripts/calibrate_judge.py` (e.g.
   `--llm-fact-judge`) so job C2-04 can measure agreement with the LLM judge
   enabled. With the flag off, `calibrate_judge.py` behaves exactly as today.

## Constraints (non-negotiable)

- Modify only `judge_report.py` and `calibrate_judge.py` under
  `evals/altibase_answerability/scripts/`.
- Do not touch `GPTs/upload_package/`. Do not change answer generation.
- Do not run `run-all.sh` or other jobs' files.
- Precision must not regress: the LLM judge must not credit answers that are
  actually wrong.

## Acceptance checks

```bash
# Self-test stays deterministic with the LLM judge OFF:
python3 evals/altibase_answerability/scripts/judge_report.py --self-test
# Rule-only calibration still runs (baseline, LLM off):
python3 evals/altibase_answerability/scripts/calibrate_judge.py \
  --gold evals/altibase_answerability/fixtures/judge_gold_set.jsonl
# LLM-judge calibration runs and falls back cleanly if the provider is absent
# (must not hang or crash; record the agreement % either way):
python3 evals/altibase_answerability/scripts/calibrate_judge.py \
  --gold evals/altibase_answerability/fixtures/judge_gold_set.jsonl --llm-fact-judge
git diff --check
```

If the live provider is available, the `--llm-fact-judge` agreement must be
**>= the rule-only agreement** and precision must not drop. If the provider is
unavailable in this environment, the `--llm-fact-judge` run must still complete
via fallback (equal to rule-only) — record that clearly in the result; the gate
itself is job C2-04.

## Completion protocol

As your final action:

- Ensure `evals/altibase_answerability/improvement2/state/` exists.
- If every acceptance check passed, write
  `evals/altibase_answerability/improvement2/state/02.result` with first line
  `PASS` and a short summary: rule-only agreement %, LLM-judge agreement %
  (or "provider unavailable — fell back to rule judge"), and precision for both.
- Otherwise write the same file with first line `FAIL: <one-line reason>`.
