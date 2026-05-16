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
