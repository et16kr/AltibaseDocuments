# Test-Harness Improvement — Job Runner, Cycle 2

Staged, resumable execution of the Altibase answerability **test harness**
improvement plan, cycle 2. Each job is run by the Claude CLI (`opus`, `xhigh`
effort) as one autonomous step.

- Plan: `GPTs/reports/answerability_improvement_cycle2_plan_20260520.md`
- Cycle-1 outcome: `evals/altibase_answerability/reports/full_rerun_analysis_20260520.md`
- Cycle-1 runner: `evals/altibase_answerability/improvement/`
- Scope: changes are limited to `evals/altibase_answerability/`. No edits to
  `GPTs/upload_package/` source bodies.
- Baselines (cycle-2 "before"): `altibase_source_preserving_20260520_195639_job11`
  (full, 37/270) and `altibase_coding_agent_20260520_195650_job11`
  (coding-agent, 2/10).

## Usage

```bash
cd evals/altibase_answerability/improvement2
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
| 01 | C2-01 prohibited-claim false-positive fix round 2 | 1 | judge |
| 02 | C2-02 LLM-assisted fact judge (T7-B) | 1 | judge; uses live provider |
| 03 | C2-03 `--retrieval-recall` manifest fix | 1 | tooling |
| 04 | C2-04 judge re-calibration gate | 1 | **LIVE**; **gate: ≥90% agreement** |
| 05 | C2-05 router scoring tuning | 2 | retrieval |
| 06 | C2-06 `properties` domain deep-dive | 2 | retrieval |
| 07 | C2-07 errors / views coverage | 2 | retrieval |
| 08 | C2-08 targeted calibration run | 3 | **LIVE**, stop/go gate |
| 09 | C2-09 full re-run and regression analysis | 3 | **LIVE**, long-running |
| 10 | C2-10 harness documentation update | 4 | docs only |

Job 04 is a hard gate: Phase 2 does not start until judge-vs-gold agreement
reaches ≥ 90%. Jobs 08–09 perform live provider runs and can take a long time;
job 08 is a stop/go gate so the retrieval jobs can be revised before spending a
full 270-question run.

The live command provider (Codex CLI) is needed earlier than Phase 3: job 02
exercises the LLM fact judge (and degrades to the rule judge if the provider is
absent), and job 04 **requires** it to evaluate the calibration gate. The LLM
fact judge is enabled for benchmark runs with `JUDGE_LLM_FACT=1` in the
environment — `run-test.sh` does not take a judge flag.
