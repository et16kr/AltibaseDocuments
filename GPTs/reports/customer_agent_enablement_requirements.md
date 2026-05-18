# Altibase GPT Customer And Agent Enablement Requirements

- Created: 2026-05-18
- Repository: this repository
- Status: requirements baseline
- Related designs: source-preserving pack and Korean-aligned English baseline designs
  should be kept under `GPTs/reports/` before implementation
- Scope: requirements only; no implementation performed by this document

## 1. Purpose

Build an Altibase GPT knowledge system that lets first-time overseas customers,
customer-owned LLMs, and coding agents perform source-backed Altibase work and build
Altibase-backed services with minimal or no Altibase technical-support intervention
for topics covered by the selected repository-local source corpus and the adjacent
AID corpus at `~/AID`.

The system must support both:

1. **Knowledge completeness**: preserve selected source-manual information without
   silent loss.
2. **Actionability**: help humans, LLMs, and coding agents safely generate, configure,
   execute, validate, troubleshoot, and test Altibase work from source-backed
   documentation.

The desired end state is not merely a compact FAQ or summarized manual. It is a
source-backed customer and agent enablement package.

The system must also assume that many customers will not use a separate coding
agent. They may ask the GPTs directly to design, code, configure, validate, and
troubleshoot Altibase-backed application or operations work, then paste generated
artifacts into their own project or environment. GPTs answers therefore must support
practical service-development and operations artifact generation, not only
explanatory answers.

## 2. Stakeholder Goal

The primary stakeholder goal is:

> A customer who is new to Altibase should be able to use our GPTs, their own LLM, or
> a coding agent to design, implement, configure, operate, validate, and troubleshoot
> an Altibase-backed service for work covered by the original selected documents
> without needing our technical support, except where exact customer environment,
> runtime state, logs, object definitions, unsupported behavior, customer policy, or
> live validation are required.

The target users include application developers, DBAs, SI engineers, migration
engineers, and operations engineers who need to build or support services using
Altibase.

GPTs and coding agents must be able to use the documentation to perform or draft work
involving:

- Altibase-backed service design and implementation planning;
- application data-access code, connection setup, transaction handling, and test
  scaffolding where source-backed;
- Altibase DDL and DCL generation;
- SQL generation and validation;
- environment and property configuration;
- installation, startup, shutdown, and first checks;
- ODBC, CLI, C Interface, Precompiler, JDBC, and related connection setup;
- iSQL, iLoader, utilities, dataCompJ, dump tools, and operational tools;
- backup, recovery, archive log, tablespaces, and administrative operations;
- replication, CDC, Log Analyzer, Replication Manager, and replication SSL;
- security, TLS, certificates, network, and access-control checks;
- migration, DB Link, external connectors, Kubernetes/AKU, Spatial, NiFi, Tableau, and
  other selected integration topics;
- troubleshooting and error response.

For direct GPT use, GPTs must generate customer-usable first drafts for the same
classes of service-development, DBA, operations, SQL, configuration, command, code,
script, and test artifacts. When the generated artifact is intended for copy/paste
use, the answer must include the required user inputs, version or environment
assumptions, validation checks, and destructive-action warnings before presenting the
artifact as safe to run.

## 3. Core Requirement

The documentation system must contain enough source-backed detail for a customer,
LLM, or coding agent to answer this question:

> Given a selected-source-backed Altibase service-development, DBA, or operations
> task, what exact inputs, commands, SQL, code, configuration, files, APIs, checks,
> expected outputs, risks, and stop conditions are needed to proceed safely?

If the answer depends on customer-specific runtime state, the system must not invent a
definitive answer. It must ask for the missing input and give the safest
source-backed next check.

## 4. Required Architecture

The system must use three complementary knowledge layers, one source-derived English
working baseline, and one final upload packaging layer.

### Layer 1: Source-Preserving Knowledge Pack

Purpose:

- Preserve selected source Markdown content without silent omission.
- Provide the low-level evidence layer for exact manual/source details.
- Preserve low-frequency exact tokens, appendix sample details, patch notes, examples,
  file paths, and source-specific warnings that may be omitted by compact summaries.

Expected location:

```text
GPTs/source_pack/
```

Required behavior:

- Include all selected source Markdown files exactly once, or exclude them with a
  recorded reason.
- Preserve original Markdown content inside stable source boundary markers.
- Include source IDs, source path, source family, version scope, language, authority,
  checksum, byte count, line count, and estimated token count.
- Organize the combined selected source corpus, including repository-local sources and
  `~/AID`, into deterministic source-pack shards or blocks that can be referenced by
  playbooks, attachments, and the final upload package.
- Treat source-pack files as evidence artifacts unless they are explicitly selected or
  transformed into the final upload package.
- Count any source-pack file intended for GPT Knowledge upload against the global
  final-upload limit.
- Keep each upload-intended shard or final upload file under GPT Knowledge file and
  token limits with margin.
- Provide deterministic validation proving source inclusion and exact extraction.

### Source-Derived Working Layer: Korean-Aligned English Baseline

Purpose:

- Provide Korean-source-checked English working text for downstream generation.
- Reduce repeated Korean/English reconciliation during playbook, attachment, and final
  upload-package work.
- Preserve traceability from enriched English content back to Korean authority and the
  original English source where useful.

Expected location:

```text
GPTs/korean_aligned_english/
```

Required behavior:

- Derive only from selected repository-local paired Korean/English sources and approved
  source IDs.
- Treat the original English source as the base English material and the paired Korean
  source as authoritative for conflicts, missing details, and current behavior.
- Record source IDs, source paths, version scope, authority labels, source-line or
  source-block references, and alignment status for each enriched block.
- Preserve unresolved Korean/English differences, weak evidence, suspected source drift,
  or unsupported gaps in the conflict or recheck register.
- For AID, reuse classified Korean-source-updated English evidence instead of deriving
  a duplicate baseline unless a recorded gap, conflict, recheck item, or unsupported
  coverage requires additional normalization.
- Use the baseline as the primary downstream working input for agent playbooks,
  answer-ready attachments, and final upload-package content when it exists for the
  relevant source scope.
- Do not use the baseline to replace source-pack exact extraction or Korean-authority
  checks. The source-preserving pack remains the exact-original evidence layer.
- Do not include Korean prose in customer-facing output unless the file explicitly
  requires it; translate and normalize into clear English while preserving literal
  technical tokens.

### Layer 2: Task-Oriented Agent Playbooks

Purpose:

- Convert source-backed manual content into actionable procedures for customers, LLMs,
  and coding agents.
- Provide task workflows that can generate safe first drafts of SQL, configuration,
  scripts, commands, code, and test cases.

Expected location:

```text
GPTs/agent_playbooks/
```

Required behavior:

- Use the Korean-aligned English baseline as the primary working input where it exists,
  while keeping the source-preserving pack and selected source corpus as evidence.
- Do not summarize away required tokens or operational cautions.
- Provide task-specific inputs, generated outputs, validation checks, expected result
  tokens, stop conditions, and cleanup or rollback notes.
- Distinguish safe draft generation from production execution.
- Ask for missing customer evidence when required.

### Layer 3: Answer-Ready Customer Attachments

Purpose:

- Provide concise, English-normalized, retrieval-friendly customer answer blocks.
- Remain the first layer for ordinary Q&A and support-style responses.

Expected location:

```text
GPTs/attachments/
```

Required behavior:

- Continue to be improved through the staged source-pack, playbook, attachment
  follow-up, upload-package, and readiness workflows defined in this requirements
  document.
- Use the Korean-aligned English baseline as the primary working input where it exists.
- Preserve exact technical tokens.
- Support direct GPT answer generation of source-backed application code snippets,
  connection examples, SQL, DDL, DCL, configuration snippets, tool commands, scripts,
  runbooks, and tests for customer copy/paste workflows.
- Route to source pack source IDs when exact detail or source verification is needed.
- Keep guardrails and source authority policy visible.

### Final GPT Knowledge Upload Package

Purpose:

- Package the source-preserving, Korean-aligned English, playbook, and answer-ready
  layers into the actual GPT Knowledge upload set.
- Keep the upload set within the final file-count, size, and token limits while
  preserving source-backed answerability and service-development usefulness.

Expected location:

```text
GPTs/upload_package/
```

Required behavior:

- Contain every Markdown file intended for GPT Knowledge upload.
- Contain 20 or fewer Markdown files total, including any selected or transformed
  repository-local source content, AID-derived content, source-pack material,
  Korean-aligned English material, playbook material, and answer-ready customer
  reference material.
- Treat the 20-file limit as a global final-upload limit, not as 20 files for
  repository-local manuals plus additional files for AID.
- Integrate or route to the three knowledge layers and the source-derived working
  baseline: source-preserving evidence, Korean-aligned English working text,
  task-oriented playbooks, and answer-ready customer references.
- Do not upload separate 20-file sets for `GPTs/source_pack/`,
  `GPTs/korean_aligned_english/`, `GPTs/agent_playbooks/`, and `GPTs/attachments/`.
- Keep manifests, reports, scripts, validation logs, and evidence matrices outside the
  upload package unless they are intentionally converted into customer-facing upload
  content and counted in the 20 files.
- Provide an upload order and final package manifest that lists every uploaded file,
  source families covered, AID tier coverage, estimated tokens, byte size, and
  evidence references.

## 5. Source Scope

The requirements apply to selected repository-local source materials already used by
the Altibase GPT workflows, plus the adjacent AID source corpus at `~/AID`.

Default source families:

- Altibase 7.1 product manuals;
- Altibase 7.3 product manuals;
- Altibase 8.1 verified source manuals under trunk source trees;
- release notes;
- 7.1 and 7.3 patch notes;
- tool manuals;
- technical documents;
- third-party guides;
- approved support reports and audit artifacts listed in the source manifest;
- AID Korean-source-updated English documentation and LLM reference artifacts.

Default include roots:

```text
Manuals/
ReleaseNotes/
PatchNotes/
Technical Documents/
3rd Party Guide for Altibase/
~/AID/
```

Support reports under `GPTs/reports/` are included only when the source manifest lists
them as approved support evidence. They are traceability and validation evidence; they
do not override selected product sources.

### AID Source Corpus

The `~/AID` workspace is in scope for customer and agent enablement. It contains an
English documentation set that has already been updated from Korean source material,
plus semantic coverage and LLM reference evidence.

Important AID inputs include:

```text
~/AID/DOCK/Home/
~/AID/faq/Home/
~/AID/arch/Home/
~/AID/FAQE/Home/
~/AID/llm-reference/
~/AID/KO_EN_SEMANTIC_COVERAGE_REPORT.md
~/AID/KO_EN_DOC_REVIEW_REPORT.md
~/AID/PASS2_KO_EN_DOC_REVIEW_REPORT.md
~/AID/source-stabilization/
~/AID/semantic-coverage/
~/AID/manifest.json
```

The important AID inputs must be classified by upload role before packaging:

| AID tier | Default treatment |
| --- | --- |
| Upload-content candidates | Stabilized English files under `~/AID/arch/Home/`, `~/AID/FAQE/Home/`, and source-backed `~/AID/llm-reference/` files may be included in source-preserving, Korean-aligned English baseline, playbook, attachment, or final upload content when their evidence classification supports use. |
| Evidence-only authority | Korean source files under `~/AID/DOCK/Home/` and `~/AID/faq/Home/`, semantic-coverage matrices, source-stabilization notes, review reports, and `manifest.json` are traceability and authority evidence by default, not customer upload content. |
| Accepted limitation | Rows or files classified as `source_limitation`, legacy unavailable attachment, export artifact limitation, or intentionally excluded low-information content must be recorded as limitations and must not be expanded into unsupported customer-facing content. |
| Conflict or recheck input | Any AID content that conflicts with the selected Altibase manual corpus, lacks required classification evidence, or fails spot checks must go to a conflict or recheck register before it can become upload content. |

The AID corpus must be treated as a Korean-source-updated English working source, not
as an unrelated raw English corpus. Its own reports state that Korean documents under
`DOCK/Home` and `faq/Home` were authoritative for source cleanup decisions, while the
stabilized English source files under `arch/Home` and `FAQE/Home` and the consolidated
`llm-reference/` package are intended for LLM reference use.

AID current-state assumption:

- AID English content has already been updated from the Korean source set before this
  project-level packaging work begins.
- Current known AID evidence records `KO_EN_SEMANTIC_COVERAGE_REPORT.md` as
  `COMPLETE`, with no unresolved `missing`, `unverified`, or `recheck_required`
  coverage rows; it also records accepted `source_limitation` rows that must remain
  limitations rather than inferred content.
- Current known AID inventory evidence records 588 kept Markdown page entries and 53
  excluded low-information pages.
- Current known AID second-pass evidence says the checked English source set is ready
  for LLM reference consolidation if later work preserves classification boundaries
  and remaining risks.
- AID is therefore not a raw translation backlog. Do not schedule a blanket
  Korean-to-English rewrite pass for AID unless an AID validation report, source
  classification, source limitation, conflict record, or spot check identifies a
  specific unresolved gap.
- This assumption may skip or narrow translation-normalization tasks for AID, but it
  does not skip AID source inventory, source preservation, checksum validation,
  classification preservation, conflict checks, 20-file packaging, retrieval testing,
  playbook integration, or final readiness validation.
- If a workflow step would normally translate or reconcile English manuals from Korean
  originals, it must first check whether the relevant AID file is already
  Korean-source-verified or link-validated Korean-source-verified, then either reuse
  that evidence or record why additional work is still required.
- AID translation-normalization work may be skipped only when the relevant AID file or
  source group has evidence showing `COMPLETE`, `covered`, `added`, `not_applicable`,
  or accepted `source_limitation` status with no unresolved `missing`, `unverified`,
  or `recheck_required` rows.

Requirements for AID integration:

- preserve AID source classifications such as Korean-source-verified,
  link-validated Korean-source-verified, English-only source, and source limitation;
- include AID upload-content candidates in the source-preserving pack,
  Korean-aligned English baseline, playbooks, attachments, or final upload package when
  their classification supports that use, or record a justified exclusion;
- keep AID evidence-only authority files outside the customer upload package by
  default while preserving their source IDs and evidence links;
- use AID `llm-reference/` as a high-value input for Korean-aligned English baseline
  work, replacement docs, agent playbooks, attachments, or final upload content when
  its evidence classification permits that use;
- keep AID validation reports as traceability evidence;
- do not silently merge AID English-only auxiliary content with Korean-source-verified
  content;
- maintain an AID tier manifest that records upload-content, evidence-only, accepted
  limitation, conflict, and recheck decisions;
- if AID conflicts with the selected Altibase manual corpus, record the conflict and
  resolve it using the active source authority policy.

## 6. Source Authority Requirements

The system must preserve the existing Altibase source policy.

- Korean manuals, release notes, patch notes, tool manuals, technical documents, and
  third-party guides are authoritative when paired Korean and English sources differ.
- English sources are extraction aids when consistent with Korean sources.
- Altibase 7.1 and 7.3 claims require corresponding selected 7.x source evidence.
- `Manuals/Altibase_trunk` and `Manuals/Tools/Altibase_trunk` are the selected
  Altibase 8.1 verified source.
- Customer-facing text should preserve the established `Altibase 8.1 verified source`
  wording where applicable.
- Patch-specific claims must preserve exact patch versions and exact `BUG-*` or
  `TASK-*` tokens.
- AID Korean-source-updated English documents may be used as a primary English working
  input for baseline work, replacement docs, playbooks, attachments, and final upload
  content, but their classification and validation evidence must be preserved.
- Do not use generic Oracle, generic database, driver, ODBC, JDBC, Kubernetes, or
  third-party assumptions to fill missing Altibase behavior.

### Korean-Aligned English Working Baseline

For repository-local paired Korean and English source documents, the workflow must
explicitly create or maintain a Korean-aligned English working baseline before
generating downstream replacement docs, playbooks, attachments, or final upload
package content from those sources.

Required behavior:

- Treat the paired Korean source as authoritative and the original English source as
  the base English material.
- Compare the original English source against the Korean source for the selected
  corpus, then strengthen the English baseline with Korean-source-backed missing
  details, current wording, version or patch distinctions, SQL syntax, DDL and DCL
  patterns, commands, examples, properties, restrictions, warnings, expected outputs,
  validation checks, cleanup or rollback notes, and stop conditions.
- Preserve traceability from each enriched English source block to the Korean source
  IDs and, where useful, the original English source IDs.
- Record unresolved Korean/English differences, weak evidence, or suspected source
  drift in a conflict or recheck register instead of silently choosing the English
  text or inventing unsupported content.
- Use the Korean-aligned English working baseline as the primary downstream working
  input for agent playbooks, answer-ready attachments, and the final upload package
  when that baseline exists for the relevant source scope.
- Treat this baseline as a verified derived working source, not as a replacement for
  the Korean authoritative source. Exact version-sensitive, conflicting, destructive,
  security-sensitive, or high-risk claims still require a Korean source recheck.
- Do not duplicate AID's completed Korean-source-verification work as a blanket
  rewrite pass. Reuse AID's Korean-source-updated English files when their evidence
  classification permits it, and perform additional normalization only for recorded
  gaps, conflicts, recheck items, or unsupported coverage.

## 7. User Personas

### First-Time Overseas Customer

Needs:

- plain English explanation;
- prerequisite checks;
- exact commands and SQL;
- safe order of operations;
- validation steps;
- stop conditions and escalation inputs.

Must not receive:

- unsupported compatibility claims;
- destructive commands without preconditions;
- vague "not in attachments" answers when selected sources cover the topic;
- Korean prose copied directly as the final answer.

### Experienced DBA Or Operator

Needs:

- exact syntax;
- version and patch boundaries;
- property defaults/ranges/dynamic-change behavior;
- dictionary/performance view checks;
- replication, backup, recovery, and troubleshooting guardrails.

### Developer Or Coding Agent

Needs:

- connection strings;
- driver, DSN, property, class, method, API, callback, handle, compile, and link
  details;
- SQL/DDL generation patterns;
- code or command skeletons;
- validation queries;
- expected output tokens;
- common error handling.

### Test Designer Or Validation Agent

Needs:

- positive cases;
- negative cases;
- boundary values;
- setup and teardown;
- expected errors or output tokens;
- validation SQL;
- cleanup and rollback requirements.

## 8. Functional Requirements

### FR-001: Lossless Source Preservation

All selected source Markdown files must be preserved in the source pack without silent
omission.

Acceptance:

- every selected source file has a manifest row;
- every included source appears in exactly one shard;
- every excluded source has a reason;
- extracted source block checksums match the originals.

### FR-002: Exact Token Preservation

The system must preserve exact source-backed technical tokens.

Token classes include:

- SQL keywords, grammar tokens, and examples;
- object names and schema names;
- property names, values, defaults, ranges, units, and mutability terms;
- view and column names;
- error codes, symbols, and messages;
- command options and environment variables;
- API, class, method, callback, handle, library, and package names;
- file paths, generated file names, sample names, and output tokens;
- patch versions, `BUG-*`, `TASK-*`, protocol labels, and version info values.

### FR-003: Task Playbook Coverage

For each major supported work area, the system must provide task-oriented playbooks.

Each playbook must include:

- task purpose;
- supported versions;
- required customer inputs;
- source-backed assumptions;
- prerequisites;
- generated artifacts;
- commands, SQL, configuration, or code templates;
- step-by-step procedure;
- validation checks;
- expected result tokens;
- common errors and first checks;
- stop conditions;
- cleanup, rollback, or non-production test guidance;
- source IDs or source pack references.

### FR-004: Service Development And Artifact Generation Support

Coding agents and GPTs must be able to help customers build Altibase-backed services
by drafting source-backed implementation and operations artifacts, including:

- service architecture notes that identify Altibase-specific constraints, connection
  choices, transaction behavior, storage choices, and operational dependencies;
- application connection examples and data-access code for supported interfaces;
- project configuration snippets, environment variables, library paths, driver
  settings, DSN entries, build flags, and runtime prerequisites;
- schema, privilege, object, and data-management SQL;
- DBA and operations commands, tool scripts, migration scripts, backup/recovery
  runbooks, replication drafts, monitoring queries, and troubleshooting workflows;
- positive and negative test cases, validation SQL, expected output tokens, and
  failure-handling checks.

SQL, DDL, and DCL generation is one required artifact class within this broader
service-development objective. Coding agents and GPTs must be able to draft
source-backed SQL, DDL, and DCL for:

- database and tablespace operations;
- datafiles and archive/log operations;
- users, roles, privileges, synonyms, views, sequences, directories, triggers, jobs;
- tables, constraints, indexes, partitions, LOB storage, queues;
- replication DDL and administrative SQL;
- DML, functions, expressions, JSON, LOB, Temporary LOB;
- property SQL and check SQL.

Generated artifacts must include validation queries or checks and cautions for
destructive effects, implicit commits, version restrictions, required privileges,
security exposure, operational risk, and unsupported assumptions.

When a customer asks GPTs to generate implementation artifacts for copy/paste use,
the answer must:

- state the assumed Altibase version, object names, schema names, privileges, and
  environment inputs, or ask for them if they are required;
- generate Altibase-specific syntax from source-backed documentation, not generic
  Oracle, MySQL, PostgreSQL, or ANSI assumptions;
- preserve exact identifiers, clauses, function names, data types, view names, property
  names, and utility command tokens from the source corpus;
- separate runnable code, SQL, commands, and configuration from explanatory text using
  clear fenced code blocks;
- include validation SQL, command checks, compile checks, connection checks, or test
  cases when the source supports them;
- call out destructive, irreversible, privilege-changing, storage-changing,
  replication-changing, or security-sensitive effects before the artifact;
- provide placeholders only when a value is customer-specific, and explain each
  placeholder immediately near the generated artifact;
- avoid presenting production execution, deployment, or service integration as safe
  when live environment checks, object definitions, logs, patch level, source-backed
  interface details, or customer policy are missing.

### FR-005: Environment And Property Configuration Support

The system must support source-backed property and environment configuration.

Required fields when source-backed:

- property name;
- purpose;
- version scope;
- default;
- valid values;
- range;
- unit;
- dynamic/static behavior;
- restart or recreate requirement;
- dependency and precedence;
- check SQL or file location;
- related views or errors;
- risks and stop conditions.

### FR-006: Client, ODBC, API, And Tool Support

GPTs and coding agents must be able to use documentation to draft and validate:

- ODBC DSN configuration;
- CLI connection and diagnostics;
- Altibase C Interface usage;
- Precompiler/APRE build and embedded SQL flows;
- JDBC connection strings, driver classes, properties, failover, LOB behavior;
- iSQL connection, script, host variable, and formatting workflows;
- iLoader load/export workflows;
- utilities, dataCompJ, dump tools, altiComp, aexport, and related operations.

Each tool/API playbook must preserve command names, options, environment variables,
input files, output files, sample paths, expected output, and common error handling.

### FR-007: Operations And Protected-Topic Support

The system must safely support high-risk operations:

- backup and recovery;
- archive log mode;
- loganchor and datafile operations;
- destructive SQL and DDL;
- replication state changes;
- security/TLS and certificate changes;
- version-sensitive property changes.

For protected topics, the system must provide:

- required preconditions;
- missing inputs to ask for;
- non-destructive first checks;
- exact command or SQL only when safe;
- stop conditions;
- validation steps;
- rollback or recovery notes when source-backed.

### FR-008: Troubleshooting And Error Response

The system must support source-backed troubleshooting from exact errors and symptoms.

Each error block or troubleshooting playbook must include:

- exact error code;
- symbol;
- message;
- source version scope;
- likely source-backed causes;
- immediate action;
- required customer evidence;
- related properties, views, logs, commands, tools, or SQL;
- escalation stop point.

### FR-009: Version And Patch Boundary Support

The system must preserve version and patch boundaries.

Required:

- exact Altibase 7.1, 7.3, and 8.1 verified-source labels;
- exact patch versions;
- `BUG-*` and `TASK-*` tokens;
- protocol, database binary, meta, communication, and replication version info when
  present;
- property and performance-view additions, changes, or removals;
- compatibility caveats and guardrails.

### FR-010: Retrieval And Routing

The system must be findable by both exact tokens and practical customer phrasing.

Required:

- source IDs;
- shard table of contents;
- source family index;
- version index;
- task playbook index;
- exact-token aliases;
- cross-links between source pack, playbooks, and attachments;
- clear owner routes for topics.

## 9. Agent Playbook Required Domains

The following playbook domains are required.

| Domain | Required playbook coverage |
| --- | --- |
| Installation and startup | install prerequisites, environment setup, database creation, startup phases, shutdown modes, first checks |
| DDL generation | tablespaces, users, roles, privileges, tables, indexes, partitions, constraints, queues, LOB storage |
| SQL and data types | DML, functions, predicates, expressions, JSON, LOB, Temporary LOB, Oracle differences |
| Properties | property changes, validation, dynamic/static behavior, restart rules |
| Dictionary and views | object lookup, performance checks, metadata checks, view-column guardrails |
| Backup and recovery | logical/offline/online backup, archive logs, recovery, media failure, incremental backup |
| Replication and CDC | topology, DDL, states, sync, conflicts, CDC, Log Analyzer, RepMgr |
| Security and TLS | certificates, server/client TLS, ODBC/JDBC/iSQL TLS, access controls, replication SSL separation |
| ODBC and C clients | ODBC, CLI, ACI, Precompiler, diagnostics, compile/link/runtime checks |
| Java and JDBC | JDBC URL, driver, properties, Java compatibility, Spring, Hibernate, Adapter for JDBC |
| Tools | iSQL, iLoader, utilities, dataCompJ, dump tools, altiComp, aexport |
| Migration and integrations | Migration Center, Adapter for Oracle, DB Link, Hadoop, Kubernetes/AKU, Spatial, NiFi, Tableau |
| Errors and troubleshooting | exact error handling, logs, symptoms, next checks, escalation |
| Test generation | positive/negative cases, expected outputs, cleanup, stop conditions |

## 10. Non-Functional Requirements

### NFR-001: Source Safety

The system must not modify original source files.

### NFR-002: Deterministic Build

Source pack and playbook generation should be reproducible from scripts or recorded
commands.

### NFR-003: Auditability

Every generated source shard and playbook must be traceable to source IDs and source
paths.

### NFR-004: Upload Readiness

Upload files must respect current GPT Knowledge file count, size, and token limits.
Limits must be rechecked before final upload because product limits can change.

### NFR-005: Customer-Safe English

Customer-facing playbooks and attachments must be in clear English while preserving
literal product tokens.

### NFR-006: No Unsupported Inference

The system must not infer Altibase behavior from Oracle, generic SQL, generic ODBC,
generic JDBC, Kubernetes, or third-party product assumptions.

### NFR-007: Guardrail Preservation

The system must preserve missing-input prompts and safe next checks for environment-
specific, runtime-specific, unsupported, or destructive operations.

## 11. Deliverables

### Source Pack Deliverables

```text
GPTs/source_pack/*.md
GPTs/source_pack/source_to_shard_manifest.tsv
GPTs/source_pack/source_pack_validation.md
GPTs/source_pack/upload_order.md
GPTs/source_pack/source_pack_gpt_instruction_note.md
GPTs/source_pack/scripts/
```

### Korean-Aligned English Baseline Deliverables

```text
GPTs/korean_aligned_english/*.md
GPTs/korean_aligned_english/baseline_manifest.tsv
GPTs/korean_aligned_english/alignment_validation.md
GPTs/korean_aligned_english/scripts/
```

### Agent Playbook Deliverables

```text
GPTs/agent_playbooks/*.md
GPTs/agent_playbooks/playbook_manifest.tsv
GPTs/agent_playbooks/playbook_validation.md
GPTs/agent_playbooks/test_scenarios.md
GPTs/agent_playbooks/scenario_judge_rubric.md
GPTs/agent_playbooks/coding_agent_instruction_note.md
GPTs/agent_playbooks/gpt_service_development_instruction_note.md
```

### Final Upload Package Deliverables

```text
GPTs/upload_package/*.md
GPTs/upload_package/final_upload_manifest.tsv
GPTs/upload_package/upload_order.md
GPTs/upload_package/final_upload_validation.md
```

### Integration Deliverables

```text
GPTs/reports/customer_agent_enablement_readiness.md
GPTs/reports/source_pack_to_attachment_crosswalk.tsv
GPTs/reports/source_pack_to_playbook_crosswalk.tsv
GPTs/reports/source_pack_to_upload_package_crosswalk.tsv
GPTs/reports/korean_aligned_english_to_playbook_crosswalk.tsv
GPTs/reports/korean_aligned_english_to_attachment_crosswalk.tsv
GPTs/reports/korean_aligned_english_to_upload_package_crosswalk.tsv
GPTs/reports/agent_playbook_gap_register.md
GPTs/reports/aid_tier_manifest.tsv
GPTs/reports/source_conflict_register.md
```

### Stage Workflow Deliverables

Each operator-requested stage must be prepared as a runnable Codex job workflow before
the user executes it.

Expected workflow locations:

```text
.codex-jobs/altibase-gpt-stage-01-source-pack-baseline/
.codex-jobs/altibase-gpt-stage-02-agent-playbooks/
.codex-jobs/altibase-gpt-stage-03-attachments-followup/
.codex-jobs/altibase-gpt-stage-04-upload-package/
.codex-jobs/altibase-gpt-stage-05-final-readiness/
```

Each stage workflow must contain:

```text
jobs.tsv
jobs.md
prompts/
run-all.sh
logs/
rollbacks/
```

The assistant prepares and validates these workflow files, including `bash -n
run-all.sh`, but does not execute `run-all.sh` during the preparation request. The
user executes `run-all.sh` manually.

Stage 1 must be internally ordered: source manifest, source selection, exact source-pack
extraction, and source-pack validation must complete before Korean-aligned English
baseline generation begins for the same source scope. Baseline jobs may then use the
validated source IDs, source boundaries, authority labels, and AID tier decisions from
the source-pack subphase.

## 12. Validation Requirements

Validation must include:

- source manifest completeness;
- checksum or exact-content extraction validation;
- approved support-report manifest validation;
- Korean-aligned English baseline manifest and alignment validation;
- Korean/English conflict and recheck register validation;
- AID tier manifest validation;
- AID translation-normalization skip-gate validation;
- global upload file-count validation proving that the final GPT Knowledge package is
  20 Markdown files or fewer including AID-derived content;
- final upload package manifest validation proving that every GPT Knowledge upload
  file is listed under `GPTs/upload_package/`;
- shard size and estimated token validation;
- exact-token spot checks;
- source authority label checks;
- playbook source-ID coverage checks;
- generated implementation artifact checks, including code, SQL, commands,
  configuration, scripts, and tests;
- direct GPT service-development artifact checks, including SQL/DDL/DCL as one
  artifact class;
- scenario judge-rubric checks for required source IDs, required exact tokens,
  forbidden generic assumptions, missing-input prompts, generated artifacts, and
  validation steps;
- protected-topic guardrail checks;
- targeted retrieval smoke tests;
- GPT and coding-agent service-development scenario tests;
- customer Q&A scenario tests;
- final readiness report.

## 13. GPT And Coding-Agent Scenario Tests

The project must define representative GPT and coding-agent scenario tests before
declaring readiness.

Minimum scenarios:

- design a minimal Altibase-backed service implementation plan with required inputs,
  interfaces, schema work, validation, and stop conditions;
- generate application connection code and configuration for a supported interface;
- generate a disk tablespace DDL with validation SQL;
- generate a user/privilege setup for an application schema;
- generate GPTs copy/paste implementation artifacts, including SQL, DDL, or DCL where
  appropriate, with required assumptions and warnings;
- configure and verify an ODBC DSN;
- create a JDBC connection example with version caveats;
- run an iSQL script with spool/log handling;
- prepare an iLoader load/export workflow;
- change a property safely with dynamic/static handling;
- diagnose an exact error code;
- plan a backup and recovery check without unsafe production commands;
- create a replication setup draft with topology and state guardrails;
- configure TLS client/server basics with certificate path checks;
- use a utility or migration tool with expected output and error handling;
- design positive and negative SQL tests from source-backed syntax.

Each scenario must record:

- input prompt;
- expected source IDs;
- expected generated artifacts;
- whether the expected artifact is a direct GPTs answer, coding-agent output, or both;
- required exact tokens;
- forbidden generic assumptions or unsafe statements that must not appear;
- missing inputs that the GPT or coding agent must ask for before generating or
  marking an artifact as safe;
- expected files, code blocks, SQL statements, commands, configuration snippets, or
  test cases;
- validation checks;
- compile, connection, execution, or dry-run checks where source-backed and practical;
- stop conditions;
- scoring rubric and required pass threshold;
- pass/fail result.

## 14. Acceptance Gates

The system is not ready unless all gates pass. If a gate cannot pass, the project must
produce an explicit not-ready report and treat readiness as blocked.

| Gate | Pass condition |
| --- | --- |
| Source preservation | all selected sources included once or excluded with reason |
| Source extraction | extracted source blocks match originals |
| Korean-aligned English baseline | repository-local paired Korean/English sources used downstream have a Korean-source-backed enriched English baseline with manifest and validation evidence, or a recorded exclusion, limitation, conflict, or recheck reason |
| Global upload count | final GPT Knowledge upload package is 20 Markdown files or fewer including AID-derived content |
| Final upload package definition | every upload-intended Markdown file is under `GPTs/upload_package/` and listed in the final upload manifest |
| AID tiering | every in-scope AID file or source group is classified as upload-content, evidence-only, accepted limitation, conflict, recheck, or excluded with reason |
| AID skip gate | translation-normalization work is skipped only for AID files or source groups with qualifying completion/classification evidence |
| Token preservation | required exact-token spot checks pass |
| Playbook coverage | required playbook domains exist with source IDs |
| GPT service-development generation | direct GPT outputs can support Altibase-backed service coding, DBA, and operations tasks with source-backed, copy/paste structured, and guarded artifacts |
| Protected topics | guardrail checks pass |
| GPT and coding-agent scenarios | representative GPT and coding-agent tests pass using a recorded judge rubric |
| Customer Q&A scenarios | representative first-time customer tests pass |
| Benchmark integration | existing answerability benchmark gates are not weakened |
| Upload readiness | file count, size, and token estimates are within current limits |

## 15. Relationship To Existing Workflows

### Superseded `.codex-jobs` Workflows

The earlier `.codex-jobs` workflows, including `altibase-gpt-post-workflow-followup`,
`altibase-gpt-full-coverage-audit`, `altibase-gpt-encyclopedia-rebuild`,
`altibase-gpt-customer-llm-remediation`, and `altibase-gpt-answerability-benchmark`,
are superseded by this staged customer and agent enablement workflow. They may be
deleted from the active workspace to prevent Codex or operators from resuming stale
or partially obsolete job queues.

Durable evidence and reusable outputs from those workflows must remain in their
project locations, such as `GPTs/reports/`, `evals/altibase_answerability/`,
`GPTs/attachments/`, and `review/`. Do not rely on deleted `.codex-jobs` prompts,
status files, logs, or rollback files as the active plan of record.

### New Stage Workflows

Create new stage workflows only when the operator requests a specific stage. The new
workflows must follow the five-stage sequence below and must incorporate the
Korean-aligned English working baseline requirement before downstream playbook,
attachment, or upload-package work uses paired Korean/English sources.

### Operator Request Model

The work must be controllable through five explicit operator stages. The operator can
ask the assistant to prepare one stage at a time by using short Korean requests such
as `1단계 준비해 주세요`, `2단계 준비해 주세요`, `3단계 준비해 주세요`,
`4단계 준비해 주세요`, or `5단계 준비해 주세요`.

For a stage preparation request, the assistant must:

- inspect the current repository status and any prior stage workflow status;
- generate or update the stage workflow under `.codex-jobs/`;
- write bounded jobs, prompts, acceptance checks, and rollback behavior;
- validate the generated `run-all.sh` with `bash -n`;
- provide the exact command the user should run;
- not execute `run-all.sh`.

The user owns stage execution by manually running the generated `run-all.sh`. After a
manual run, the operator may ask `N단계 실행 결과를 점검해 주세요`; the assistant
then inspects `jobs.tsv`, logs, validation artifacts, commits, and the worktree before
declaring the stage complete or blocked.

If the operator says only `N단계 실행해 주세요`, treat that as a request to prepare
or verify execution readiness, not as permission to run `run-all.sh`, unless the
operator explicitly changes the execution ownership rule in the same request.

### Five Stage Sequence

| Stage | Operator preparation request | Workflow directory | Purpose | Completion or blocked outcome |
| --- | --- | --- | --- | --- |
| 1 | `1단계 준비해 주세요` | `.codex-jobs/altibase-gpt-stage-01-source-pack-baseline/` | Prepare the source-preserving knowledge pack first, then the Korean-aligned English working baseline for repository-local sources and `~/AID`, using durable evidence under `GPTs/reports/` and `evals/altibase_answerability/` only as supporting context. | Source manifest, AID tier manifest, source shards, checksums, source IDs, source-pack validation, baseline manifest, alignment validation, and conflict/recheck records are complete or produce a not-ready report. |
| 2 | `2단계 준비해 주세요` | `.codex-jobs/altibase-gpt-stage-02-agent-playbooks/` | Prepare task-oriented playbook generation from the validated source pack and Korean-aligned English baseline, including coding-agent, GPT service-development, and test-generation playbooks. | Required playbook domains, source IDs, baseline links, generated artifact patterns, validation checks, stop conditions, test scenarios, and judge rubric are complete or produce a not-ready report. |
| 3 | `3단계 준비해 주세요` | `.codex-jobs/altibase-gpt-stage-03-attachments-followup/` | Re-plan and execute only the still-needed attachment follow-up work using the source pack, Korean-aligned English baseline, durable benchmark evidence, and playbooks as evidence. | Answer-ready attachments preserve required exact tokens, route to source IDs and playbooks, close scoped coverage gaps, and pass targeted validation. |
| 4 | `4단계 준비해 주세요` | `.codex-jobs/altibase-gpt-stage-04-upload-package/` | Prepare the final GPT Knowledge upload package from the source-preserving, Korean-aligned English, playbook, and answer-ready layers. | `GPTs/upload_package/` contains every upload-intended Markdown file, the package has 20 Markdown files or fewer including AID-derived content, and manifest/order/size/token validation passes. |
| 5 | `5단계 준비해 주세요` | `.codex-jobs/altibase-gpt-stage-05-final-readiness/` | Prepare final readiness validation, targeted scenario checks, protected-topic checks, customer Q&A checks, and the final benchmark gate. | Final readiness report records pass status or explicit blockers; benchmark and scenario gates are not weakened. |

Recommended order:

1. Prepare Stage 1 and have the user run its `run-all.sh`.
2. Inspect Stage 1 results and resolve blockers before preparing Stage 2.
3. Prepare Stage 2 and have the user run its `run-all.sh`.
4. Inspect Stage 2 results and resolve blockers before preparing Stage 3.
5. Prepare Stage 3 and have the user run its `run-all.sh`.
6. Inspect Stage 3 results and resolve blockers before preparing Stage 4.
7. Prepare Stage 4 and have the user run its `run-all.sh`.
8. Inspect Stage 4 results and resolve blockers before preparing Stage 5.
9. Prepare Stage 5 and have the user run its `run-all.sh`.
10. Inspect Stage 5 results and update final readiness.

## 16. Success Definition

The project succeeds when a first-time customer, customer LLM, or coding agent can use
the uploaded knowledge package to do source-backed Altibase work without technical
support for selected-source-covered topics, while the system reliably asks for missing
customer evidence or escalates when source-backed safety requires it.

Success is not measured by file count or document size alone. It is measured by:

- no silent source loss;
- actionable task playbooks;
- exact-token preservation;
- safe guarded behavior;
- coding-agent scenario success;
- customer Q&A scenario success;
- benchmark/readiness evidence.
