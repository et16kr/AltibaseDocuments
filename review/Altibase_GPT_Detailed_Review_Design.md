# Altibase GPTs Detailed Review Design

## Purpose

This review process verifies whether the 20 Altibase GPTs attachment files are ready
to be uploaded as GPTs knowledge files.

The target GPT should act as an encyclopedia-grade Altibase assistant for overseas
customers who may have no prior Altibase knowledge. It should answer source-backed
manual-style questions and generate Altibase-specific SQL, commands, configuration
steps, operational runbooks, troubleshooting guidance, and compatibility explanations
for Altibase 7.1, 7.3, and 8.1.

The 20 Markdown files are an upload packaging boundary, not a high-frequency FAQ
subset. Review should verify that the selected manuals, release notes, technical
documents, tool manuals, third-party guides, and approved supporting sources remain
answerable through searchable consolidated Markdown.

## Review Strategy

Review in small, independent stages. Each stage should be small enough for one Codex
CLI run to inspect carefully, produce a useful report, and stop without editing the
attachment files.

The review bias is:

- Keep ordinary DML SQL brief when it behaves like Oracle SQL.
- Review DML only for Altibase differences, limitations, functions, JSON behavior,
  compatibility boundaries, and migration cautions.
- Spend more review depth on Altibase-specific DDL, tablespaces, storage behavior,
  properties, data dictionary views, operation, troubleshooting, replication, HA,
  performance, security, and tool behavior; this depth requirement does not make
  missing catalog coverage acceptable.
- Treat missing source-backed property, SQL syntax, data type, view, error, utility,
  connector, tool, or runbook coverage as an actionable gap when it prevents
  encyclopedia-style answers.
- Treat Korean Altibase manuals as the authoritative latest manual source. If an
  English manual and its Korean counterpart differ, review against the Korean manual
  and call out any English-source drift as a source issue.
- Check that Altibase 8.1 material is based on the verified source policy and that
  customer-facing attachments do not expose internal source labels.
- Confirm that images and screenshots have been converted into searchable Markdown,
  Mermaid, BNF-like syntax, or procedural text instead of requiring separate image
  uploads.

## Review Artifacts

Primary files:

- `GPTs/Altibase_GPT_Document_Selection.md`
- `GPTs/Altibase_GPT_Attachment_Build_Workplan.md`
- `GPTs/GPT_Instructions_Draft.md`
- `GPTs/attachments/README.md`
- `GPTs/attachments/*.md`

Existing reports to use as context:

- `GPTs/reports/source_inventory.md`
- `GPTs/reports/8_1_verification.md`
- `GPTs/reports/eng_kor_parity.md`
- `GPTs/reports/image_inventory.md`
- `GPTs/reports/table_inventory.md`
- `GPTs/reports/link_inventory.md`
- `GPTs/reports/attachment_count_validation.md`
- `GPTs/reports/forbidden_strings_validation.md`
- `GPTs/reports/version_coverage_validation.md`
- `GPTs/reports/english_consistency_validation.md`
- `GPTs/reports/sql_generation_test_results.md`
- `GPTs/reports/multilingual_prompt_set.md`
- `GPTs/reports/multilingual_smoke_results.md` when available

Review outputs:

- One report per review stage under `review/reports/`.
- Reports should contain findings and recommended fixes only.
- Review runs should not edit `GPTs/attachments/` directly.

## Severity Model

Use these severities in every review report:

| Severity | Meaning |
| --- | --- |
| Blocker | Upload should not proceed. The attachment set is incomplete, unsafe, misleading, or structurally unusable. |
| High | A customer could receive wrong Altibase guidance, wrong SQL, wrong version behavior, or unsafe operational advice. |
| Medium | The content is probably usable but has meaningful gaps, weak source support, confusing structure, or retrieval problems. |
| Low | Small wording, organization, consistency, or polish issue. |
| Note | Non-blocking observation or optional improvement. |

## Report Format

Each stage report should use this structure:

````markdown
# Rxx Review Title

Date:
Reviewer:
Verdict: Pass | Review Required | Fail

## Scope

- Attachments:
- Supporting reports:
- Source manuals sampled:

## Commands Run

```bash
...
```

## Findings

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |

## Source Checks

- Claims checked:
- Source coverage:
- Korean/English source conflicts:
- Source gaps:

## Oracle-Overlap Decision

- Correctly compressed:
- Too much generic Oracle material:
- Missing Altibase-specific difference:

## Version Checks

- 7.1:
- 7.3:
- 8.1:

## Retrieval And GPT Answer Quality

- Strengths:
- Risks:

## Required Follow-Up

- ...
````

If there are no issues, state that clearly and list any residual risk or unverified
area. Do not invent missing source support; mark the issue as requiring source audit.

## Review Gates

### Gate 0: Upload Boundary And Safety

Goal: confirm the final upload unit remains exactly 20 Markdown attachments and does
not depend on extra image files.

Checks:

- Exactly 20 files under `GPTs/attachments/`, excluding `README.md`.
- No image links or raw image file references remain in upload attachments.
- No `trunk`, Windows absolute path, `file://`, or internal source labels remain in
  customer-facing attachments.
- Mermaid and text replacements are present where image inventory required conversion.

### Gate 1: Strategy And Source Fidelity

Goal: confirm the attachment set follows the intended content strategy.

Checks:

- The attachment set matches the selection document.
- The attachment set is a consolidated encyclopedia-grade reference, not merely a
  high-frequency FAQ or support-summary set.
- English is the canonical attachment language, but Korean manuals are the authoritative
  source when paired Korean and English manuals differ.
- Korean-source content must be translated and normalized into English attachment prose
  without exposing internal source labels.
- Claims that matter for customer correctness are traceable to selected sources.
- Oracle-overlapping DML is intentionally compressed; Altibase-specific behavior is not
  lost.

### Gate 2: Altibase SQL, DDL, Storage, And System Metadata

Goal: verify the highest-risk SQL generation and system-behavior files.

Checks:

- DDL examples are version-aware and executable after placeholder replacement.
- Tablespace, memory/disk/volatile/temporary storage, LOB, JSON, partition, index,
  constraint, user, privilege, and replication DDL are correct for the stated version.
- System views and data dictionary queries use the correct object names and support
  operational checks.
- DML remains compact and focused on differences from Oracle.

### Gate 3: Operation, Troubleshooting, Performance, Replication, And Security

Goal: verify operational guidance that could affect production support.

Checks:

- Installation, startup/shutdown, backup/recovery, and tablespace operations are stated
  as safe procedures with prerequisites and verification steps.
- Error and troubleshooting content uses symptom, likely cause, check command/query, and
  action.
- Performance guidance avoids overclaiming optimizer behavior and preserves execution
  plan terminology.
- Replication, HA, CDC, and replication SSL behavior is version-aware.
- TLS/SSL guidance separates client/server SSL from replication SSL.

### Gate 4: Development Interfaces, Tools, Migration, And External Integrations

Goal: verify customer workflows around drivers, APIs, migration, utilities, and external
connectors.

Checks:

- JDBC, Spring, CLI, ODBC, C Interface, Precompiler, LOB, and JSON/Temporary LOB guidance
  is literal and version-aware.
- Utilities and third-party tools are organized by task and troubleshooting scenario.
- Migration and Oracle compatibility files focus on Altibase differences and conversion
  risks rather than generic Oracle usage.
- UI screenshots are replaced with procedural text that preserves field names, selected
  values, and expected outcomes.

### Gate 5: Retrieval, Multilingual Answers, And Final Upload Readiness

Goal: confirm the attachment set works as GPTs knowledge.

Checks:

- Each file has useful headings, question-oriented sections, compact item blocks, and
  source-safe wording.
- The final upload checklist maps source-backed manual-style question areas and
  reference catalogs to one or more attachments.
- Literal technical tokens remain unchanged in multilingual answer scenarios.
- Korean manuals remain the default source authority for the final repeated review; any
  Korean/English manual conflict is recorded and judged from the Korean manual.
- The final upload checklist maps every source-backed customer question area to one or
  more attachments.
- Remaining review reports are resolved or explicitly accepted as residual risk.

## Review Stages

The executable stage definitions are in `review/review_stages.tsv`. Use the runner:

```bash
bash review/scripts/run_review_stage.sh list
bash review/scripts/run_review_stage.sh prompt R03
DRY_RUN=1 bash review/scripts/run_review_stage.sh run R03
bash review/scripts/run_review_stage.sh run R03
bash review/scripts/run_review_stage.sh run-all G2_CoreSQL
```

Do not run these review stages while an attachment-building `run-all` is still writing
`GPTs/` unless the review is intentionally read-only and its reports are kept under
`review/`.

## Acceptance For The Whole Review Process

The attachment set is ready for upload when:

- Gate 0 has no blockers.
- All high-risk source and SQL claims reviewed in Gate 1 and Gate 2 are either supported
  or corrected.
- Operational, replication, troubleshooting, and security review has no Blocker or High
  findings.
- Development and tool review has no unresolved correctness finding that would mislead a
  customer.
- Multilingual and retrieval review confirms that answer language can change while SQL
  tokens, property names, commands, paths, error codes, and object names remain literal.
- Retrieval review confirms that manual-style questions over the selected source corpus
  can be answered from the consolidated attachment set, or are recorded as remediation
  gaps.
- The final repeated review explicitly uses Korean manuals as the default source
  authority when Korean and English manuals differ.
- The final upload checklist references exactly the 20 attachment Markdown files.
