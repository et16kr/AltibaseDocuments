# Job 11 — C3-11 Harness documentation update

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Master plan: `GPTs/reports/answerability_improvement_cycle3_plan_20260522.md` —
  item C3-11.
- Cycle 3 (jobs 01–10) changed the test harness:
  - the prohibited-claim guard now ignores negation tokens inside quoted
    code/example spans (the ERR-101 quoted-span fix);
  - the judge gold set expanded from 52 to ~150 entries, domain-balanced;
  - the coding-agent question suite was enlarged (≥ 30 questions);
  - `answer_runner.py` gained an optional N-sample answer mode and the scorecard
    gained a variance band;
  - `build_context()` gained identifier-anchored named-definition assembly for
    `replication_cdc_security_network`, additional `views_performance_monitoring`
    coverage, and a prose→identifier resolution step.
- The harness documentation still describes the cycle-2 behaviour.

## Task

Update the harness documentation so it matches the harness as it now exists.

1. Update `evals/altibase_answerability/scripts/README.md` to describe:
   - the quoted-span polarity guard in the prohibited-claim detector;
   - the multi-sample answer mode (the option name and env toggle, default N=1,
     that N=1 is byte-identical to before and is the self-test path) and the
     scorecard variance band;
   - the replication identifier-anchored assembly and the prose→identifier
     resolution step in `build_context()`.
2. Update `evals/altibase_answerability/README.md` and, if present,
   `evals/altibase_answerability/manifests/README.md` and
   `evals/altibase_answerability/questions/README.md` where they describe
   retrieval/judging behaviour, the gold set size, or the coding-agent suite
   size that has changed.
3. Keep edits accurate and concise. Describe only what the code actually does
   now — read the current `answer_runner.py`, `judge_report.py`, and
   `calibrate_judge.py` to confirm. Do not invent behaviour.
4. Do not modify any code, question records, manifests, policy, the gold set, or
   `GPTs/upload_package/`. This job is documentation only.

## Constraints (non-negotiable)

- Modify only Markdown documentation files under `evals/altibase_answerability/`.
- Do not change behaviour. Do not run `run-all.sh` or other jobs' files.

## Acceptance checks

```bash
# Documentation only — code/tests must remain valid and unchanged by this job.
python3 evals/altibase_answerability/scripts/answer_runner.py --self-test
python3 evals/altibase_answerability/scripts/judge_report.py --self-test
git diff --check
```

Self-judgement: review your own `git diff` for this job and confirm every file
you changed is a Markdown documentation file under
`evals/altibase_answerability/`. If you changed anything else, revert it before
finishing — earlier jobs' uncommitted changes are expected and are NOT yours to
revert; only undo edits this job made.

## Completion protocol

As your final action:

- Ensure `evals/altibase_answerability/improvement3/state/` exists.
- If every acceptance check passed, write
  `evals/altibase_answerability/improvement3/state/11.result` with first line
  `PASS` and a short summary.
- Otherwise write the same file with first line `FAIL: <one-line reason>`.
