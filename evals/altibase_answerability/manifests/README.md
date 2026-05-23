# Manifests

Run manifests select question files, define run metadata, and configure optional
answer-generation behavior. A manifest must validate against
`../schemas/manifest.schema.json`.

Manifests may include GPT instruction draft material only by explicit path selection.
They must not expose source references, expected facts, required tokens, prohibited
claims, canonical reference answers, source-language basis, difficulty, or retrieval
risk to the answering model.

## Seed Manifest

`fixture_seed.json` is a small offline manifest for J003 schema and leakage-boundary
checks. It selects `../fixtures/seed_questions.jsonl`, uses only
`GPTs/attachments/*.md` as the attachment source boundary, and lists exactly the
question fields that the answer runner may project:

- `id`
- `question`
- `version_scope`
- `user_level`
- `answer_type`
- `answer_language`
- `requested_language`

`requested_language` is an allowed optional projection field. If a manifest does not
set `answer_generation.requested_language`, the answer runner should omit it and default
to English answers.

## Full Benchmark Manifest

`full_benchmark.json` selects all seven durable domain question files and is the
manifest to use for production answer generation and readiness reporting. It preserves
the same answer-generation boundary as the fixture manifests: only
`GPTs/attachments/*.md`, the allowlisted question projection, and no judge-only fields.

`full_benchmark_source_preserving_package.json` selects the same seven durable domain
question files without changing question records or expected answers, but routes
answer-generation context to `GPTs/upload_package/*.md`. It keeps the
same answer-input allowlist, judge configuration, and reporting dimensions, and adds an
explicit `context_root` so package dry-runs cannot escape the source-preserving upload
package.

Because the context root is the upload package, the runner's manifest-aware retrieval
also reads the package's `02_source_manifest.md` and `03_source_to_shard_manifest.md`
to route each question to its documented source blocks. These two files are part of
the selected context, not a separate input; routing degrades cleanly to plain lexical
ranking when they are absent. See `../scripts/README.md` for the context-selection and
retrieval-audit details.

Manifest fields cover what the runner does per question; live-run knobs that
multiply the per-question record count, such as the `ANSWER_SAMPLES`
environment variable for multi-sample answer generation, sit outside the
manifest. `ANSWER_SAMPLES=1` (the default) leaves every artifact byte-for-byte
identical to a pre-multi-sample run; see `../scripts/README.md` for details.

## Coding-Agent Manifest

`coding_agent_source_preserving_package.json` is a separate benchmark for practical
Codex, customer-owned LLM, and RAG-agent use of the source-preserving package. It
selects only `../questions/coding_agent_source_preserving.jsonl`, uses
`GPTs/upload_package/*.md` as answer context, and is not part of the
locked 270-question `full_benchmark` baseline.

Validate it with the dedicated small-profile gate:

```bash
python3 evals/altibase_answerability/scripts/validate_benchmark.py \
  --manifest evals/altibase_answerability/manifests/coding_agent_source_preserving_package.json \
  --profile coding_agent
```
