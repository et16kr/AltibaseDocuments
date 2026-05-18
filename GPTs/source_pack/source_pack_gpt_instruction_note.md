# Source Pack GPT Instruction Note

- Job: `S1-J005`
- Last verified: 2026-05-18
- Status: source-pack instruction note

## Use Policy

When source-pack content or source IDs are available to a GPT, LLM, or coding
agent, use these rules:

- Treat `GPTs/source_pack/` as exact evidence, not as the final customer-facing
  upload package unless a later upload manifest explicitly selects it.
- Prefer answer-ready attachments and playbooks for normal customer answers, then
  use source-pack source IDs to verify exact manual text, low-frequency tokens,
  examples, commands, SQL, configuration names, errors, and version boundaries.
- Preserve source IDs, source paths, version scope, language, authority label, and
  AID classification labels when citing or transforming source-pack evidence.
- For repository-local Korean/English conflicts, apply the active source policy:
  Korean Altibase manuals are authoritative, while English manuals may be
  extraction aids unless a stronger source label is recorded.
- For AID-derived material, preserve Korean-source-verified, link-validated,
  English-only auxiliary, evidence-only, and accepted-limitation boundaries.
- Do not infer Altibase behavior from Oracle, generic SQL, generic ODBC/JDBC,
  Kubernetes, or third-party assumptions when source-pack evidence is absent.
- If an answer depends on patch level, platform, installed output, object DDL,
  logs, runtime state, unsupported behavior, or customer environment, ask for
  that input and give the safest source-backed next check instead of inventing a
  definitive answer.
- Do not upload all source-pack shards alongside attachments. The final GPT
  Knowledge upload package must remain 20 Markdown files or fewer including
  AID-derived content.

## Validation Reference

The committed source pack currently validates 941 selected source rows across 16 shards with exact body checksums. Rerun this command after any source-pack change:

```bash
python3 GPTs/source_pack/scripts/validate_source_pack.py --check
```
