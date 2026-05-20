# Job 10 — C2-10 Harness documentation update

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Cycle 2 (jobs 01–09) changed the test harness: a round-2 prohibited-claim fix
  (polarity-, direction-, and markdown-emphasis-aware), an optional
  LLM-assisted fact judge, a `--retrieval-recall` manifest fix, and retrieval
  scoring/coverage tuning for under-specified questions and the `properties` /
  `errors_troubleshooting` / `views_performance_monitoring` domains.
- The harness documentation still describes the cycle-1 behaviour.

## Task

Update the harness documentation so it matches the harness as it now exists.

1. Update `evals/altibase_answerability/scripts/README.md` to describe:
   - the optional LLM-assisted fact judge — the `--llm-fact-judge` flag, that it
     is off by default, that it adjudicates only the paraphrase-suspect band,
     caches verdicts, and falls back to the deterministic rule judge;
   - the round-2 prohibited-claim detection (polarity-, direction-, and
     markdown-emphasis-aware);
   - the manifest-aware `--retrieval-recall` diagnostic;
   - any new router-scoring behaviour the retrieval jobs introduced.
2. Update `evals/altibase_answerability/README.md` and, if present,
   `evals/altibase_answerability/manifests/README.md` where they describe
   retrieval or judging behaviour that has changed.
3. Keep edits accurate and concise. Describe only what the code actually does
   now — read the current `answer_runner.py`, `judge_report.py`, and
   `calibrate_judge.py` to confirm. Do not invent behaviour.
4. Do not modify any code, question records, manifests, policy, or
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

- Ensure `evals/altibase_answerability/improvement2/state/` exists.
- If every acceptance check passed, write
  `evals/altibase_answerability/improvement2/state/10.result` with first line
  `PASS` and a short summary.
- Otherwise write the same file with first line `FAIL: <one-line reason>`.
