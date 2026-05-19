# Altibase GPT Source-Preserving Package Finalization

- Kind: `mixed`
- Status values: `ToDo`, `Progress`, `Done`, `Fail`
- User-run command: `./run-all.sh` from this directory
- Codex workdir: repository root by default, override with `CODEX_WORKDIR=/path`
- Default behavior: continue through all jobs until completion or failure
- Optional single-job mode: `RUN_ONE=1 ./run-all.sh`
- Handoff gate: uncommitted project files stop the workflow before the next job starts
- Commit gate: each successful job must pass review and create a focused commit
  containing both job output and `jobs.tsv`/`jobs.md` `Done` state
- Purpose: finalize `GPTs/upload_package_source_preserving/` as the primary
  source-preserving Altibase encyclopedia package for GPTs, Codex, and LLM/RAG
  systems.
- Scope boundary: this workflow may edit `GPTs/upload_package_source_preserving/`,
  add source-preserving validation scripts and reports under `GPTs/reports/`,
  and update `evals/altibase_answerability/` benchmark manifests, scripts,
  questions, schemas, and reports needed for package-aware dry-run validation.
  It must not edit original manual/source documents or alter existing 270
  benchmark question/expected-answer records.
- Integrity boundary: source bodies inside `SOURCE_BLOCK_BEGIN` /
  `SOURCE_BLOCK_END` must remain byte-preserved. Wrapper/header wording and
  retrieval metadata may change only outside source blocks.
- Live benchmark boundary: do not run a live 270-question benchmark unless
  explicit operator approval and the output path are recorded before execution.
  Dry-runs, schema validation, self-tests, and deterministic package validation
  are allowed.
- Reference plan:
  `GPTs/reports/source_preserving_upload_package_finalization_plan.md`.

## Jobs

| ID | Status | Title | Goal |
| --- | --- | --- | --- |
| `SPF-J001` | `Done` | Preflight and package boundary gate | Verify the source-preserving package baseline, clean handoff rules, finalization plan, and unresolved live-benchmark approval boundary before any package edits. |
| `SPF-J002` | `Done` | Source-preserving package validator | Create and document a validator dedicated to GPTs/upload_package_source_preserving with count, size, token, SHA, block-boundary, and final-wording checks before package wording edits. |
| `SPF-J003` | `Done` | Final-upload wording normalization | Normalize wrapper and header wording in the source-preserving upload package using the source-preserving validator while preserving source block bodies byte-for-byte. |
| `SPF-J004` | `Done` | GPT Codex retrieval instructions | Add final GPT/Codex/LLM usage instructions that define the package as the primary source corpus and enforce source-grounded answer behavior. |
| `SPF-J005` | `Done` | Shard retrieval metadata | Add non-source-body shard retrieval metadata to improve semantic search while preserving all source block bytes. |
| `SPF-J006` | `Done` | Package-aware benchmark harness | Retarget benchmark tooling or manifests so the existing 270-question benchmark can dry-run against GPTs/upload_package_source_preserving without changing questions or expected answers. |
| `SPF-J007` | `Done` | Coding-agent benchmark extension | Add a separate coding-agent question set, manifest, and rubric that tests repository work, SQL/iSQL generation, APIs, diagnostics, safety checks, and citation behavior against the source-preserving package. |
| `SPF-J008` | `Done` | Final validation and readiness review | Run final deterministic validation, benchmark dry-runs, and write a readiness report with explicit remaining live-benchmark routing and no unsupported pass claims. |

## Resume Rules

- `Fail`: stop before starting later jobs.
- Dirty project files: stop before starting or advancing to another job.
- `Progress`: preserve interruption evidence, set the job back to `ToDo`, then rerun only when project files are clean.
- `Done`: skip.
- Nonzero `codex exec` exits leave the job as uncommitted `Progress` by default. A repository reset to the last successful job commit returns that job to `ToDo`; otherwise the next manual run stops if project files are dirty, or resets runtime state and retries when clean.

## Acceptance Checklist

- Each job has a matching prompt in `prompts/`.
- Each job has concrete acceptance criteria.
- Each successful job leaves project files clean and advances HEAD with a commit containing both job output and workflow state.
- `bash -n run-all.sh` passes.
- `run-all.sh` invokes `codex exec --cd "$exec_root"` by default, with
  `$exec_root` resolving to the repository root unless `CODEX_WORKDIR` is set.
- `SPF-J001` writes or updates the preflight report before package edits.
- `SPF-J002` adds a validator dedicated to
  `GPTs/upload_package_source_preserving/`.
- `SPF-J006` preserves the existing 270-question baseline while adding a
  package-aware dry-run route.
- `SPF-J007` adds coding-agent benchmark coverage as a separate question set and
  manifest, not by mutating the existing 270-question baseline.
- `SPF-J008` writes the final readiness report and makes no live benchmark pass
  claim unless a live run actually occurred with prior approval.
