# Test-Harness Improvement — Job Runner, Cycle 3

Staged, resumable execution of the Altibase answerability **test harness**
improvement plan, cycle 3. Each job is run by the Claude CLI (`opus`, `xhigh`
effort) as one autonomous step.

- Plan: `GPTs/reports/answerability_improvement_cycle3_plan_20260522.md`
- Cycle-2 outcome: `evals/altibase_answerability/reports/full_rerun_analysis_cycle2_20260520.md`
- Cycle-2 runner: `evals/altibase_answerability/improvement2/`
- Scope: changes are limited to `evals/altibase_answerability/` (including the
  question sets under `evals/altibase_answerability/questions/`). No edits to
  `GPTs/upload_package/` source bodies.
- Baselines (cycle-3 "before"): `altibase_source_preserving_20260521_220915_job09`
  (full, 41/270 = 15.2%) and `altibase_coding_agent_20260521_220915_job09`
  (coding-agent, 2/10 = 20%).

## Usage

```bash
cd evals/altibase_answerability/improvement3
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
| 01 | C3-01 ERR-101 quoted-span prohibited-claim fix | 1 | judge |
| 02 | C3-02 expand and audit the judge gold set (52 → ~150) | 1 | judge fixtures |
| 03 | C3-03 enlarge the coding-agent question suite | 1 | question set |
| 04 | C3-04 multi-sample answer generation + variance band | 1 | tooling |
| 05 | C3-05 judge re-calibration gate | 1 | **LIVE**; **gate: ≥90% agreement** |
| 06 | C3-06 `replication_cdc_security_network` assembly | 2 | retrieval |
| 07 | C3-07 `views_performance_monitoring` residual coverage | 2 | retrieval |
| 08 | C3-08 prose-named identifier resolution | 2 | retrieval |
| 09 | C3-09 targeted calibration run | 3 | **LIVE**, stop/go gate |
| 10 | C3-10 full re-run and regression analysis | 3 | **LIVE**, long-running |
| 11 | C3-11 harness documentation update | 4 | docs only |

Job 05 is a hard gate: Phase 2 does not start until judge-vs-gold agreement
reaches ≥ 90% **on the expanded gold set** (mean of three runs ≥ 90%, lowest
≥ 88%). Jobs 09–10 perform live provider runs and can take a long time; job 09
is a stop/go gate so the retrieval jobs can be revised before spending a full
270-question multi-sample run.

The live command provider (Codex CLI) is needed from job 05 onward: job 05
**requires** it to evaluate the calibration gate on the expanded gold set, and
jobs 09–10 use it for the live benchmark runs. The LLM fact judge is enabled for
benchmark runs with `JUDGE_LLM_FACT=1` in the environment. Cycle-3 live runs use
multi-sample answer generation (N=3); single-sample (N=1) remains the default
and the deterministic self-test path.
