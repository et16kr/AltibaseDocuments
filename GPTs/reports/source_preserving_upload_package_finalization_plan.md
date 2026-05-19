# Source-Preserving Upload Package Finalization Plan

- Date: 2026-05-19
- Repository: `/home/et16/AltibaseDocuments`
- Current baseline commit: `5af19e71 Add source-preserving GPT upload package`
- Primary package: `GPTs/upload_package/`
- Current verdict: correct source-preserving corpus; final upload polish and
  package-aware benchmark routing are still pending.

## Purpose

`GPTs/upload_package/` is the correct package boundary when the
goal is an Altibase encyclopedia for GPTs, Codex, or other LLM/RAG systems that
must retain the selected original source content.

The earlier `GPTs/upload_package/` directory is a compact topic/routing package.
It is useful as a secondary answer guide, but it is not a complete
source-preserving encyclopedia because it mostly routes to evidence instead of
containing the original selected manual/source bodies.

## Current Package State

The source-preserving package currently contains 20 files:

- `00_README_SOURCE_PRESERVING_UPLOAD.md`
- `01_upload_order.md`
- `02_source_manifest.md`
- `03_source_to_shard_manifest.md`
- `source_pack_shard_001.md` through `source_pack_shard_016.md`

The package was verified before commit:

| Check | Result |
| --- | --- |
| File count | `20` files |
| Package size | about `57M` |
| Shard integrity | all 16 shard files byte-match `GPTs/source_pack/` originals |
| Selected source baseline | `941` selected sources, `16` shards, `8,767` recorded exclusions |

This makes the package suitable as a primary source corpus for GPT Knowledge,
Codex, and RAG-style LLM systems. It is more useful for agents than the raw
manual tree because the content is already split into deterministic shards with
`source_id`, `source_path`, `source_family`, `version_scope`, `language`,
`authority_label`, `sha256`, and `SOURCE_BLOCK_BEGIN` / `SOURCE_BLOCK_END`
boundaries.

## Remaining Finalization Work

Execution note: the job workflow creates the source-preserving validator before
normalizing final-upload wording, so shard-wrapper edits are guarded by a
source-body integrity check.

### 1. Normalize Final-Upload Wording

The source body must stay byte-preserved, but wrapper/header text should be made
unambiguous for final upload use.

Required changes:

- remove or replace `Upload intended: no` in copied shard headers;
- remove or replace `not a final GPT Knowledge upload manifest` in upload-order
  guidance;
- preserve source-body bytes inside `SOURCE_BLOCK_BEGIN` / `SOURCE_BLOCK_END`;
- keep a clear distinction between primary source corpus and secondary topic
  routing documents.

### 2. Add A Source-Preserving Package Validator

Create a validator dedicated to `GPTs/upload_package/`. The
existing `validate_upload_package.py` validates the compact topic package and is
not sufficient for this package.

The new validator must enforce:

- exactly 20 final upload files;
- each file below GPT file-size and token safety limits;
- source block bodies remain byte-preserved against their recorded
  `source_sha256` values even when final-upload wrapper/header wording changes;
- all 16 shard files remain represented and their wrapper changes are recorded
  separately from source-body integrity;
- all selected sources remain represented;
- every `SOURCE_BLOCK_BEGIN` has a matching `SOURCE_BLOCK_END`;
- no final package wrapper contains reverse-routing language such as
  `Upload intended: no` or `not final upload`;
- manifest wrapper files remain readable by GPT/Codex/RAG tools.

### 3. Add GPT/Codex Retrieval Instructions

Add final usage instructions for custom GPTs, Codex, and other LLM systems.

The instructions should say:

- treat `GPTs/upload_package/` as the primary source corpus;
- use `02_source_manifest.md` to identify source documents;
- use `03_source_to_shard_manifest.md` to map source/block IDs to shard files;
- answer from shard source text when exact product behavior matters;
- cite or preserve `source_id`, `source_path`, `version_scope`, and language
  when practical;
- ask for an exact Altibase version before giving version-sensitive SQL,
  configuration, replication, backup/recovery, or destructive-operation advice;
- avoid unsupported behavior claims when the source block does not support them.

### 4. Improve Shard-Level Retrieval Metadata

For better semantic retrieval, add non-source-body metadata near the top of each
shard.

Recommended additions:

- shard topic summary;
- major manuals and source families in the shard;
- important keywords, SQL objects, utilities, error areas, and version ranges;
- pointers to representative `SRC-*` and `BLOCK-*` ranges.

The metadata must not alter source bodies inside source block boundaries.

### 5. Run Package-Aware Answerability Validation

After the final upload wording and validator are ready, run a package-aware
answerability validation. A deterministic dry run is not enough to claim live
answer quality.

The validation must preserve:

- unchanged benchmark questions;
- unchanged expected answers and judge policy;
- answer-input allowlisting;
- judge-only leakage protection;
- durable output paths under
  `evals/altibase_answerability/reports/full_benchmark/runs/`.

### 6. Retarget The 270-Question Benchmark To This Source-Preserving Package

Final follow-up task: update the existing 270-question validation benchmark so
that it uses this source-preserving upload package and this finalization document
as the package-routing authority. Extend the benchmark with coding-agent-focused
questions after the existing 270 records are preserved, so the package is tested
both as a GPT answer source and as a practical Codex/LLM agent reference.

Current limitation:

- `evals/altibase_answerability/manifests/full_benchmark.json` points answer
  generation at `GPTs/attachments/*.md`;
- `evals/altibase_answerability/scripts/answer_runner.py` currently enforces the
  `GPTs/attachments/` context boundary;
- `GPTs/reports/stage_04_retrieval_dry_run.md` records that the existing runner
  cannot benchmark `GPTs/upload_package/` or
  `GPTs/upload_package/` without a scoped harness change.

Required work:

- add a package-aware benchmark manifest or manifest option for
  `GPTs/upload_package/*.md`;
- include this document,
  `GPTs/reports/source_preserving_upload_package_finalization_plan.md`, as the
  benchmark routing policy reference;
- preserve all 270 existing question records without changing expected answers;
- add a separate coding-agent question set that tests source-grounded repository
  work, SQL/iSQL script generation, driver/API usage, error diagnosis, property
  and version checks, replication/backup safety checks, and required manual
  citation behavior;
- keep coding-agent questions distinct from the existing answerability questions
  with their own manifest, domain labels, expected artifacts, and judge rubric,
  so the original 270-question baseline remains comparable;
- keep leakage protections and judge-only fields unchanged;
- run schema validation, answer-runner self-test, judge self-test, and a dry run;
- only run a live 270-question benchmark after explicit operator approval and a
  pre-recorded output path;
- compare the package-aware result against the locked full benchmark evidence.

This task must be the final gate before claiming that the source-preserving
package is not only structurally valid, but also empirically usable as the
Altibase encyclopedia for GPTs, Codex, and LLM/RAG systems.
