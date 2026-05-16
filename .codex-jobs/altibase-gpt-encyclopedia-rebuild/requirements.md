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

## J001 Boundary And Design Note

J001 finalizes the shared rebuild contract, source-corpus scope, and success criteria
used by later jobs. It is a documentation-scope job and does not directly rewrite the
20 customer-facing attachments unless the source-scope documents themselves prove that
an attachment boundary or source label must change.

The shared runtime contract is this file. `GPTs/reports/source_inventory.md` remains the
support report for source roots and attachment-to-source mapping until J002 creates the
coverage matrix and gap register. Later jobs must use these documents together: this
file defines policy and success criteria, while the source inventory and later coverage
matrix define the concrete source families and item-level work queue.

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
- If a user question depends on an exact patch level, customer environment, log excerpt,
  object definition, or unsupported/unverified claim, ask for that missing input and
  provide the safest source-backed next check instead of inventing a definitive answer.

## Source Corpus Scope

The rebuild uses only selected sources already present in this repository and approved
supporting reports. Source families are scoped as follows:

| Source family | Authoritative use | English extraction use |
| --- | --- | --- |
| Altibase 7.1 product manuals | `Manuals/Altibase_7.1/kor` for product behavior, syntax, runbooks, properties, views, APIs, and errors. | `Manuals/Altibase_7.1/eng` for convenient English extraction when it agrees with Korean source. |
| Altibase 7.3 product manuals | `Manuals/Altibase_7.3/kor` for product behavior, syntax, runbooks, properties, views, APIs, and errors. | `Manuals/Altibase_7.3/eng` for convenient English extraction when it agrees with Korean source. |
| Altibase 8.1 verified source manuals | `Manuals/Altibase_trunk/kor` for current 8.1 manual behavior, checked against 8.1 release notes before customer-facing use. | `Manuals/Altibase_trunk/eng` for convenient English extraction when it agrees with Korean source. |
| Release notes | `ReleaseNotes/kor` for release-note conflicts, version boundaries, feature introductions, and platform claims. | `ReleaseNotes/eng` for English extraction and cross-checking. |
| Patch notes | `PatchNotes/Altibase_7.1/kor` and `PatchNotes/Altibase_7.3/kor` for patch-level behavior in supported 7.x scope. | `PatchNotes/Altibase_7.1/eng` and `PatchNotes/Altibase_7.3/eng` when present and consistent. Older 6.x patch notes are out of default answer scope unless a later job records a source-backed migration or historical reason. |
| Tool manuals | `Manuals/Tools/Altibase_release/kor` and `Manuals/Tools/Altibase_trunk/kor` for tool behavior. | Matching `eng` trees for English extraction when consistent. |
| Technical documents | `Technical Documents/kor` when paired, Korean-only, or more specific; record any conflict before using an English-only statement. | `Technical Documents/eng` for English extraction and customer-facing terminology. |
| Third-party guides | `3rd Party Guide for Altibase/kor` when present, paired, or more specific. | `3rd Party Guide for Altibase/eng` for English extraction and UI/procedure wording when consistent. |
| Supporting reports | `GPTs/reports/*.md` for source inventory, parity decisions, validation findings, and approved source notes. | Reports are internal support artifacts; do not expose internal paths or branch names in customer-facing attachments. |

The default supported answer scope is Altibase 7.1, 7.3, and 8.1. Do not broaden a
claim to another version family unless a later job records the supporting source and the
customer-facing version caution. Treat Korean-only or release-note-only detail as usable
only after translating, normalizing, and narrowing it to the source-backed version scope.

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

## Gap Recording Policy

Missing item-level source-backed coverage is not acceptable as a final state. When a job
finds a manual/source-backed gap, it must record the gap with enough detail for a later
job to resolve it:

- Source family and version scope.
- Missing item or behavior.
- Affected attachment file.
- Source path, report path, or review report used as evidence.
- Required remediation shape, such as item block, runbook step, BNF-like syntax,
  example SQL, cross-reference, or validation note.

Before J002 creates the coverage matrix and gap register, record such gaps in the
relevant support report, `GPTs/reports/source_inventory.md`, or the changed attachment's
`Residual Scope Notes` section. After J002, use the coverage matrix or gap register as
the primary tracking artifact.

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

## Success Criteria

A completed rebuild job is successful only when all of the following are true:

- The job's source families and version scope are explicit.
- Affected attachments or support reports are updated, or a source-backed reason for no
  attachment change is recorded.
- Known gaps are registered in the correct tracking artifact with enough remediation
  detail for later jobs.
- Customer-facing attachment text, when changed, is searchable English and preserves
  literal technical tokens.
- Version-sensitive claims are backed by selected sources, with Korean source precedence
  applied when paired sources differ.
- Exact-version, environment, log, object-definition, and unsupported-claim uncertainty
  is handled by asking for the missing input and giving safe next checks.
- Required validation passes, or skipped checks are explicitly justified.
- The final diff is reviewed, the job is committed with a focused message, and project
  files outside expected orchestration state are clean.

## Existing Dirty Worktree Note

Before the generated workflow can run, current project changes outside `.codex-jobs/`
must be committed, stashed, or otherwise resolved. The workflow intentionally stops when
project files are dirty so one job's output cannot leak into the next job.
