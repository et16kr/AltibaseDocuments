# Test-Harness Improvement — Job Runner

Staged, resumable execution of the Altibase answerability **test harness**
improvement plan. Each job is run by the Claude CLI (`opus`, `xhigh` effort) as
one autonomous step.

- Plan: `GPTs/reports/test_harness_improvement_plan_20260520.md`
- Analysis basis: `GPTs/reports/source_preserving_test_analysis_and_plan_review_20260520.md`
- Scope: changes are limited to `evals/altibase_answerability/`. No edits to
  `GPTs/upload_package/` source bodies.

## Usage

```bash
cd evals/altibase_answerability/improvement
./run-all.sh            # run from the first non-Done job to the last
./run-all.sh status     # show the job status table
./run-all.sh reset 03   # send job 03 back to ToDo
./run-all.sh reset all  # send every job back to ToDo
```

## How it works

- `jobs.tsv` lists the jobs in execution order.
- `jobs/NN-*.md` is the prompt fed to the Claude CLI for job `NN`.
- Each job's status lives in `state/NN.status`: `ToDo | Progress | Done | Fail`.
- A job is marked `Done` only when its Claude run writes `state/NN.result`
  whose first line is `PASS`. Otherwise the job is `Fail` and the runner stops.
- `run-all.sh` skips `Done` jobs and runs the first non-`Done` job. It stops on
  the first job that does not reach `Done`.

## Resuming after an interruption

Re-running `./run-all.sh` is always safe:

- `Done` jobs are skipped.
- A job left in `Progress` (script killed) or `Fail` (token/usage limit, crash,
  failed check) is re-run from scratch. Job prompts are written declaratively
  ("bring the code to this target state"), so re-running a partially-finished
  job converges correctly.

If a job stops because of a token/usage limit, just run `./run-all.sh` again
when capacity is back — it resumes at that job.

## Env overrides

| Variable | Default | Purpose |
| --- | --- | --- |
| `CLAUDE_MODEL` | `opus` | model passed to `claude --model` |
| `CLAUDE_EFFORT` | `xhigh` | reasoning effort passed to `claude --effort` |
| `CLAUDE_PERMISSION_MODE` | `bypassPermissions` | `claude --permission-mode` |
| `MAX_BUDGET_USD` | (unset) | optional per-job spend cap |
| `SKIP_PREFLIGHT` | `0` | set `1` to skip the harness self-test preflight |
| `COMMIT_EACH_JOB` | `0` | set `1` to git-commit a checkpoint after each Done job |

Before the loop, `run-all.sh` runs a preflight (`answer_runner.py` and
`judge_report.py` self-tests) and aborts if the harness is already broken.
`COMMIT_EACH_JOB=1` is recommended for long runs: it creates a clean rollback
point after every completed job.

## Jobs

| # | Item | Phase | Notes |
| --- | --- | --- | --- |
| 01 | T1 retrieval audit instrumentation | 0 | additive sidecar |
| 02 | T9 judge calibration gold set | 1 | builds the yardstick |
| 03 | T6 prohibited-claim false-positive fix | 1 | judge |
| 04 | T7a semantic-tolerant fact matching | 1 | judge |
| 05 | T8 pass-logic / threshold consistency | 1 | judge + policy |
| 06 | T2 source-block metadata propagation | 2 | retrieval |
| 07 | T3 query tokenization fix | 2 | retrieval |
| 08 | T4 manifest-aware routing | 2 | retrieval |
| 09 | T5 budgeted context assembly | 2 | retrieval |
| 10 | targeted calibration run | 3 | **LIVE**, stop/go gate |
| 11 | full re-run and regression analysis | 3 | **LIVE**, long-running |
| 12 | harness documentation update | 4 | docs only |

Jobs 10–11 perform live provider runs and can take a long time. Job 10 is a
stop/go gate: if the targeted calibration does not improve, it fails on purpose
so the retrieval jobs can be revised before spending a full 270-question run.

Work item **T7-B** (LLM-assisted judge mode) is intentionally left out of this
runner; the plan keeps it as a follow-up after T7-A calibration is stable.
