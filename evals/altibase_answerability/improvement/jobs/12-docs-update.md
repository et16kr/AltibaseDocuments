# Job 12 — Harness documentation update

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Jobs 01–11 changed the test harness: a retrieval audit sidecar, source-block
  metadata propagation, manifest-aware routing, budgeted context assembly, a
  prohibited-claim fix, semantic-tolerant fact matching, a pass-logic change,
  the `calibrate_judge.py` tool, and a judge calibration gold set.
- The harness documentation still describes the old behaviour.

## Task

Update the harness documentation so it matches the harness as it now exists.

1. Update `evals/altibase_answerability/scripts/README.md` to describe:
   - the `retrieval_audit.jsonl` sidecar and what it records;
   - manifest-aware, source-block-aware context selection in `answer_runner.py`;
   - the new judge behaviour (semantic-tolerant fact matching, the fixed
     prohibited-claim detection, the pass-logic change);
   - the new `calibrate_judge.py` tool and the gold set under `fixtures/`.
2. Update `evals/altibase_answerability/README.md` and, if present,
   `evals/altibase_answerability/manifests/README.md` where they describe
   retrieval or judging behaviour that has changed.
3. Keep edits accurate and concise. Describe only what the code actually does
   now — read the current `answer_runner.py` and `judge_report.py` to confirm.
   Do not invent behaviour.
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
finishing — earlier jobs' uncommitted code changes are expected and are NOT
yours to revert; only undo edits this job made.

## Completion protocol

As your final action:

- Ensure `evals/altibase_answerability/improvement/state/` exists.
- If every acceptance check passed, write
  `evals/altibase_answerability/improvement/state/12.result` with first line
  `PASS` and a short summary.
- Otherwise write the same file with first line `FAIL: <one-line reason>`.
