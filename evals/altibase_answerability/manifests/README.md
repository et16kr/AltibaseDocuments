# Manifests

Run manifests select question files, define run metadata, and configure optional
answer-generation behavior. A manifest must validate against
`../schemas/manifest.schema.json`.

Manifests may include GPT instruction draft material only by explicit path selection.
They must not expose source references, expected facts, required tokens, prohibited
claims, canonical reference answers, source-language basis, difficulty, or retrieval
risk to the answering model.
