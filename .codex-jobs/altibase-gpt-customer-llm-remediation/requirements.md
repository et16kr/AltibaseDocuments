# Workflow Requirements

## Purpose

Prepare and execute targeted remediation so `GPTs/attachments/` becomes a
customer-usable Altibase LLM corpus, not merely a benchmark-passing artifact.

The target users include:

- first-time Altibase users who need clear terms, prerequisites, safe defaults, and
  step-by-step checks;
- veteran Altibase operators and developers who need exact syntax, properties,
  version boundaries, numeric limits, error codes, views, and operational caveats.

## Non-Negotiable Source Policy

- Keep customer-facing attachment content in clear English.
- Use repository-local selected sources only: manuals, release notes, patch notes,
  technical documents, tool manuals, third-party guides, and approved support files.
- Prefer Korean Altibase manuals when Korean and English sources differ.
- Do not invent Altibase behavior from generic Oracle or generic database knowledge.
- Do not lower benchmark thresholds or rewrite expected questions to hide gaps.
- Treat exact patch level, environment, object definition, log excerpt, or unsupported
  claims as missing inputs that must be requested when needed.

## Customer LLM Quality Bar

Every edited attachment section must be usable as retrieval context for an LLM answer.
Prefer dense, item-level reference blocks over broad prose. Include both beginner and
expert affordances where relevant:

- short purpose and scope statement;
- version applicability: 7.1, 7.3, 8.1, cross-version, or patch-specific;
- exact SQL, command, property, view, error-code, API, path, option, and class names;
- defaults, ranges, units, mutability, dynamic-change support, restart requirements,
  privilege requirements, and destructive-operation cautions when source-backed;
- runnable or adaptable SQL/command examples where the source supports them;
- first checks, validation SQL, stop conditions, and escalation inputs for operations;
- explicit "ask for this missing input" guidance when an answer cannot be safe without
  customer-specific details.

## Benchmark Evidence To Use

Primary evidence:

- `evals/altibase_answerability/reports/full_benchmark/failure_root_cause_analysis_20260517.md`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_095919/summary.txt`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_095919/judge/aggregate_report.json`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_095919/judge/judgments.jsonl`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_095919/answers/answers.jsonl`
- `evals/altibase_answerability/questions/*.jsonl`

Before editing, read this workflow's `jobs.md` and use its job scope matrix to keep the
current job bounded.

Use the evidence to classify each fix as one of:

- content gap: the attachment set lacks the source-backed item or exact token;
- retrieval gap: the item exists but is hard to retrieve;
- answer synthesis gap: the item exists but the answer path encourages omission or
  over-compression;
- judge calibration issue: suspected only after source and answer path have been
  checked.

## Expected File Areas

Most remediation should remain inside:

- `GPTs/attachments/*.md`
- `GPTs/GPT_Instructions_Draft.md`
- `GPTs/reports/*.md`
- `evals/altibase_answerability/reports/*.md`

Do not edit original manuals or source documents unless explicitly instructed.

## Verification

Each job must run checks proportional to its scope. Prefer:

```bash
git diff --check
bash review/scripts/run_review_stage.sh validate
rg -n "^Verdict:|^\\| (Blocker|High|Medium|Low) \\|" review/reports/R*.md
```

When benchmark-specific changes are made, also run applicable dry-run, limited,
or targeted answerability checks if feasible. Do not start a full 270-question live
benchmark inside a job unless the job explicitly decides the environment and runtime
budget are suitable.

## Handoff

Each successful job must:

- update the scoped attachments or reports;
- self-review for source-backing, exact-token preservation, customer safety, and
  beginner/veteran usability;
- leave unrelated files untouched;
- commit a focused result;
- leave project files clean after the commit.
