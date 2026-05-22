# Image Content Recovery — Job Runner

Staged, resumable execution of the image content recovery job. The original
manuals reference ~7,100 images; the upload package ships only the `.md` shards,
so any information carried only inside a diagram or an image-rendered table is
currently lost. This job recovers that information **as text** and feeds it
through the build into the shards.

- Spec: `GPTs/reports/image_content_recovery_spec_20260522.md`
- Scope: the `Manuals/` tree (decision D3).
- AID dependency: the source-pack build reads `~/AID`; see
  `GPTs/AID_DEPENDENCY.md`.

## Confirmed decisions

- **D1** — recovered text is injected from a build-stage **sidecar**; `Manuals/`
  originals stay unmodified.
- **D2** — at a converted site the original `![]()` link is **kept** and the
  recovered text is added beside it.
- **D3** — scope is the `Manuals/` tree only.
- **D4** — every converted image (C, D, E) is **fully** cross-checked against
  its rendered raster (PDF fallback where the raster is too low-resolution).

## Usage

```bash
cd GPTs/image_recovery
./run-all.sh            # run from the first non-Done job to the last
./run-all.sh status     # show the job status table
./run-all.sh reset 03   # send job 03 back to ToDo
./run-all.sh reset all  # send every job back to ToDo
```

## How it works

- `jobs.tsv` lists the jobs in execution order.
- `jobs/NN-*.md` is the prompt fed to the Claude CLI for job `NN`.
- Each job's status lives in `state/NN.status`: `ToDo | Progress | Done | Fail`.
- A job is `Done` only when its Claude run writes `state/NN.result` whose first
  line is `PASS`. Otherwise the job is `Fail` and the runner stops.
- `run-all.sh` skips `Done` jobs, runs the first non-`Done` job, and stops on
  the first job that does not reach `Done`. Re-running is always safe — `Done`
  jobs are skipped and an interrupted job is re-run from scratch.

Before the loop, `run-all.sh` runs a preflight: it checks that `~/AID` is
present and the source-pack build scripts exist, and aborts otherwise.

## Env overrides

| Variable | Default | Purpose |
| --- | --- | --- |
| `CLAUDE_MODEL` | `opus` | model passed to `claude --model` |
| `CLAUDE_EFFORT` | `xhigh` | reasoning effort passed to `claude --effort` |
| `CLAUDE_PERMISSION_MODE` | `bypassPermissions` | `claude --permission-mode` |
| `MAX_BUDGET_USD` | (unset) | optional per-job spend cap |
| `SKIP_PREFLIGHT` | `0` | set `1` to skip the dependency preflight |
| `COMMIT_EACH_JOB` | `0` | set `1` to git-commit a checkpoint after each Done job |

## Jobs

| # | Item | Phase | Output |
| --- | --- | --- | --- |
| 01 | IMG-01 image inventory | 0 | `image_inventory.tsv` |
| 02 | IMG-02 classification and audit | 1 | `image_classification.tsv`, audit report |
| 03 | IMG-03 convert C/D/E images | 2 | `image_conversions.jsonl` |
| 04 | IMG-04 build-sidecar integration and shard rebuild | 3 | updated build + rebuilt shards |
| 05 | IMG-05 validation and documentation | 4 | validation report, updated READMEs |
| 06 | IMG-06 conversion comparison audit | 5 | comparison audit report + ledger |

Job 02 is a soft stop/go: if classes C/D/E turn out negligible it still passes,
but its result says so plainly so the run can be reconsidered before IMG-03.
Job 04 rebuilds `GPTs/upload_package/`, which changes the corpus the
answerability harness runs against — re-baselining that harness is out of scope
and is flagged in the IMG-04 result.
Job 06 independently compares each converted graph against its original image
(D and E fully, C sampled); it fails on any `material` mismatch, so a faithless
conversion stops the run rather than shipping silently.

## Artifacts

`state/` and `logs/` are runtime-only and git-ignored. The deliverables —
`image_inventory.tsv`, `image_classification.tsv`, `image_conversions.jsonl`,
and the reports under `GPTs/reports/` — are committed.
