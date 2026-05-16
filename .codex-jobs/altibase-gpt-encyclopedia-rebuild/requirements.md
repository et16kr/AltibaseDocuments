# Altibase GPT Encyclopedia Rebuild Requirements

## Purpose

Rebuild `GPTs/attachments/` into an encyclopedia-grade consolidated Altibase reference
for overseas customers who may have no prior Altibase knowledge. The 20 Markdown files
are GPT upload packaging units, not a high-frequency FAQ subset.

The final attachment set must preserve answerability for the selected Altibase manuals,
release notes, technical documents, tool manuals, third-party guides, and approved
supporting sources already present in this repository. A source-backed Altibase question
within the supported version scope must not be answered only as "not covered in the
attachments."

## Source And Language Policy

- Use Korean Altibase manuals as the authoritative source when Korean and English
  manuals differ.
- Write customer-facing attachments in canonical English.
- Do not copy Korean prose directly into attachments; translate and normalize it into
  concise English.
- The GPT will answer users in their language at runtime. Do not treat multilingual
  support as a fixed language list.
- Preserve SQL object names, SQL keywords, function names, property names, error codes,
  commands, paths, package/class/method/API names, connector names, and version labels
  literally in every answer language.
- Use `Altibase 8.1 verified source` for 8.1 customer-facing source labels. Do not expose
  internal source labels, branch names, local filesystem paths, workstation paths, or
  build labels.

## Required Coverage

The rebuild must make the attachments usable as a reference and as a source for
copy-ready operational answers.

- Product/version/platform differences for Altibase 7.1, 7.3, and 8.1.
- SQL, DDL, DCL, administrative SQL, replication SQL, property SQL, backup/recovery SQL,
  and check SQL that are specific to Altibase.
- All practical property reference material: meaning, version, default, range, dynamic
  change support, change method, check SQL, related views, and cautions where source
  material provides them.
- Data types, JSON, LOB, Temporary LOB, functions, expressions, and Oracle compatibility
  differences.
- Dictionary and performance views: purpose, important columns, when to query, and
  example check SQL.
- Error reference material: code, symbol, message, cause, action, version caution, and
  troubleshooting response pattern where source material provides it.
- Operations runbooks: installation, startup, shutdown, backup, recovery, archive log
  mode, tablespaces, replication, performance, security, migration, and troubleshooting.
- Development and tool references: PSM, external procedures, JDBC, Java, Spring,
  Hibernate, CLI, ODBC, C Interface, Precompiler, iSQL, iLoader, utilities, DB Link,
  connectors, Kubernetes/AKU, Migration Center, Spatial, NiFi, Tableau, and related
  tool manuals.

## Attachment Boundaries

- Keep exactly 20 upload Markdown files under `GPTs/attachments/`, excluding
  `README.md`.
- Keep the existing file names unless a job records and justifies a stronger alternative.
- Prefer searchable item blocks over large opaque tables.
- Convert syntax diagrams to compact BNF-like text.
- Convert operational flows, topology, state, and sequence diagrams to compact Mermaid
  only when the visual relationship improves retrieval.
- Replace UI screenshots with procedural text, field/value lists, and expected results.
- Keep cross-references between attachments when a user question naturally spans multiple
  files.

## Common Verification

Every job must run checks proportional to its scope. At minimum, use:

```bash
git diff --check
bash review/scripts/run_review_stage.sh validate
```

Use targeted `rg`/inspection checks for the specific source families and attachments
changed by the job. A successful job must review the final diff, create a focused commit,
and leave project files clean.

## Existing Dirty Worktree Note

Before the generated workflow can run, current project changes outside `.codex-jobs/`
must be committed, stashed, or otherwise resolved. The workflow intentionally stops when
project files are dirty so one job's output cannot leak into the next job.
