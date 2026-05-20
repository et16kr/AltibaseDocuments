# Job 04 — T7a Semantic-tolerant fact matching

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Master plan: `GPTs/reports/test_harness_improvement_plan_20260520.md` — read
  section **T7**, phase A only (deterministic; the LLM judge in phase B is a
  separate follow-up and is NOT in scope here).
- Evidence: `GPTs/reports/source_preserving_test_analysis_and_plan_review_20260520.md`
  section 4 — the rule judge fails paraphrased-correct answers because it
  requires exact word forms (`restarting` != `restarted`). PROP-101 gives a
  substantively correct answer scored `term_score=0.50` on fact F01. All 270
  questions are Korean-sourced, so retrieval cannot close this English lexical
  gap — the judge must.
- Jobs 02 and 03 already ran: the gold set
  `evals/altibase_answerability/fixtures/judge_gold_set.jsonl` and
  `evals/altibase_answerability/scripts/calibrate_judge.py` exist, and the judge
  may already contain the job-03 prohibited-claim fix.

## Task

Make fact coverage tolerant of word-form variation, deterministically, in
`evals/altibase_answerability/scripts/judge_report.py`.

1. FIRST, record the current baseline: run
   `python3 evals/altibase_answerability/scripts/calibrate_judge.py
   --gold evals/altibase_answerability/fixtures/judge_gold_set.jsonl`
   and note the current agreement % and precision. This is your "before" number.
2. In `term_present()` / `fact_match()` add light stemming/lemmatization so
   word-form variants match (`restarting` ~ `restarted` ~ `restart`;
   `changed` ~ `change`; `files` ~ `file`). A small deterministic suffix
   normalizer is fine — do not add heavy third-party dependencies.
3. Add a small, curated equivalence map for recurring Altibase phrasings, e.g.
   `restart` <-> `reboot`, `reflected` <-> `applied` / `take effect`. Keep it
   conservative and documented inline.
4. Keep the `fact_match(fact_text, answer, required_tokens) -> FactMatch`
   signature and its `.covered` attribute STABLE — `calibrate_judge.py` depends
   on that interface. If you genuinely must change the signature, also update
   `calibrate_judge.py` to match.
5. Do not weaken literal **required-token** preservation: `literal_token_present`
   must stay exact. Only fact-term coverage becomes form-tolerant.

## Constraints (non-negotiable)

- Modify `evals/altibase_answerability/scripts/judge_report.py`. You MAY also
  modify `evals/altibase_answerability/scripts/calibrate_judge.py`, but only if
  step 4 forced a `fact_match` interface change — otherwise leave it untouched.
- Keep the judge deterministic. Do not touch `GPTs/upload_package/`.
- Precision must not regress: semantic tolerance must not credit answers that
  are actually wrong. Verify against the gold set.
- Do not run `run-all.sh` or other jobs' files.

## Acceptance checks

```bash
python3 evals/altibase_answerability/scripts/judge_report.py --self-test
# Re-judge the existing run; PROP-101 fact F01 must now be covered:
python3 evals/altibase_answerability/scripts/judge_report.py \
  --manifest evals/altibase_answerability/manifests/full_benchmark_source_preserving_package.json \
  --policy evals/altibase_answerability/policy.json \
  --answers evals/altibase_answerability/reports/full_benchmark/runs/altibase_source_preserving_20260520_090243/answers/answers.jsonl \
  --output-dir /tmp/altibase-job04-judge
python3 -c "import json; js={j['question_id']:j for j in (json.loads(l) for l in open('/tmp/altibase-job04-judge/judgments.jsonl'))}; f01=[fr for fr in js['PROP-101']['fact_results'] if fr['fact_id']=='F01'][0]; print('PROP-101 F01 covered:', f01['covered']); assert f01['covered'], f01"
# "after" calibration — compare against the "before" number from Task step 1:
python3 evals/altibase_answerability/scripts/calibrate_judge.py \
  --gold evals/altibase_answerability/fixtures/judge_gold_set.jsonl
git diff --check
```

The "after" agreement must be **>= the "before" agreement** recorded in Task
step 1, and precision must not drop. If it does, tune the stemmer and the
equivalence map until both conditions hold, then re-verify.

## Completion protocol

As your final action:

- Ensure `evals/altibase_answerability/improvement/state/` exists.
- If every acceptance check passed AND the after-agreement/precision condition
  holds, write `evals/altibase_answerability/improvement/state/04.result` with
  first line `PASS` and a short summary including the before and after
  agreement %.
- Otherwise write the same file with first line `FAIL: <one-line reason>`.
