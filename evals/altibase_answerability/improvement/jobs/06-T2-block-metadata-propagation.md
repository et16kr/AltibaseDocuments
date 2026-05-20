# Job 06 — T2 Source-block metadata propagation

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Master plan: `GPTs/reports/test_harness_improvement_plan_20260520.md` — read
  section **T2**.
- Problem: in `evals/altibase_answerability/scripts/answer_runner.py` the shard
  files wrap each copied source body in
  `<!-- SOURCE_BLOCK_BEGIN source_id="..." block_id="..." ... -->` /
  `<!-- SOURCE_BLOCK_END -->` HTML comments. `split_markdown_chunks()` only
  breaks on Markdown headings, so block provenance is never attached to chunks
  and `SRC-*` / `BLOCK-*` tokens never reach the model context. This is the
  structural cause of coding-agent provenance-token failures.
- Job 01 already added a retrieval audit sidecar (`retrieval_audit.jsonl`) with
  per-chunk records.

## Task

In `evals/altibase_answerability/scripts/answer_runner.py`:

1. Parse `SOURCE_BLOCK_BEGIN` / `SOURCE_BLOCK_END` comments while chunking.
   Extract the attributes: `source_id`, `block_id`, `source_path`,
   `source_family`, `version_scope`, `language`, `authority_label`, plus the
   shard file path.
2. Add a `block_meta` field to the `ContextChunk` dataclass (and update
   `make_context_chunk()` / `split_markdown_chunks()` accordingly). Each chunk
   carved from inside a source block carries that block's metadata; chunks
   outside any block carry empty/none metadata.
3. When a chunk with block metadata is emitted into the context text, prefix the
   context header with compact provenance, for example:
   `===== source_id=SRC-000018 block_id=BLOCK-000001 version=7.1 lang=en :: <heading> =====`
   so `SRC-*` / `BLOCK-*` / version / shard-path strings are literally present
   in the model context.
4. **Extend the job-01 retrieval audit**: every entry in a question's
   `selected_chunks` audit list must now also include the chunk's `block_meta`
   (`source_id`, `block_id`, `source_path`, `source_family`, `version_scope`,
   `language`, `authority_label`). This keeps the audit a faithful record of
   provenance and is required by jobs 08, 10, and 11.
5. Preserve all existing behaviour: deterministic ordering, `max_context_chars`
   handling, leakage checks, the `--self-test`, and the retrieval audit sidecar
   (now extended).

## Constraints (non-negotiable)

- Modify only `evals/altibase_answerability/scripts/answer_runner.py`.
- Do not touch `GPTs/upload_package/` source bodies. You only parse them.
- Use only allowlisted question input + package context — no judge-only fields.
- Keep behaviour deterministic.
- Do not run `run-all.sh` or other jobs' files.

## Acceptance checks

```bash
python3 evals/altibase_answerability/scripts/answer_runner.py --self-test
MODE=dry_run RUN_ROOT=/tmp/altibase-job06-agent ./run-test.sh coding-agent
# AGENT-001's audit (with block_meta) must contain SRC-* / BLOCK-* provenance.
python3 -c "
import json
rows=[json.loads(l) for l in open('/tmp/altibase-job06-agent/answers/retrieval_audit.jsonl')]
a=[r for r in rows if r['question_id']=='AGENT-001'][0]
blob=json.dumps(a)
assert 'SRC-' in blob and 'BLOCK-' in blob, 'no provenance tokens in AGENT-001 audit'
assert any('block_meta' in c for c in a.get('selected_chunks',[])), 'block_meta missing from audit chunks'
print('AGENT-001 provenance present; audit carries block_meta')
"
MODE=dry_run LIMIT=3 RUN_ROOT=/tmp/altibase-job06-sp ./run-test.sh source-preserving
git diff --check
```

## Completion protocol

As your final action:

- Ensure `evals/altibase_answerability/improvement/state/` exists.
- If every acceptance check passed, write
  `evals/altibase_answerability/improvement/state/06.result` with first line
  `PASS` and a short summary.
- Otherwise write the same file with first line `FAIL: <one-line reason>`.
