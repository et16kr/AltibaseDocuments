# Replacement-Grade Reference Policy

- Job id: `PWF-J002A`
- Date: 2026-05-18
- Status: Policy baseline for post-workflow remediation
- Scope: all selected source families in the full coverage audit

## Purpose

This policy defines the standard for treating `GPTs/attachments/` as a
replacement-grade Altibase reference for:

- overseas customer Q&A;
- GPT/LLM retrieval and synthesis;
- coding-agent implementation work that uses Altibase;
- Altibase-oriented test-case generation and validation planning.

Replacement-grade does not mean copying every word from every selected source. It
means a source-backed question, implementation task, or test-design task should be
answerable from the attachment set without consulting the original manual, except
when the answer depends on customer-specific runtime state, exact patch level, object
definition, log excerpt, unsupported behavior, or a recorded guardrail.

This policy is stricter than a FAQ-summary standard and does not relax the existing
Altibase source policy.

## Evidence Basis

This policy is based on repository-local audit artifacts and selected source-policy
documents, especially:

- `GPTs/reports/full_coverage_audit/source_corpus_lock.md`;
- `GPTs/reports/full_coverage_audit/catalog_schema_and_extraction_scripts.md`;
- `GPTs/reports/full_coverage_audit/catalog_consolidation_qa.md`;
- `GPTs/reports/full_coverage_audit/final_full_coverage_audit.md`;
- `GPTs/reports/full_coverage_audit/patch_note_closure_design_20260518.md`;
- `GPTs/reports/full_coverage_audit/post_workflow_followup_plan_20260518.md`;
- the sampled Korean source-replacement audits for the SSL/TLS guide and iSQL manual
  recorded in the follow-up plan.

The two sample audits are examples that exposed the need for this policy. They are not
the whole standard.

## Source Authority

All replacement-grade work must preserve the active source policy:

- Use selected repository-local sources only.
- Korean manuals, release notes, patch notes, tool manuals, technical documents, and
  third-party guides are authoritative when paired Korean and English sources differ.
- English sources are extraction aids when consistent with Korean sources.
- Altibase 7.1 and 7.3 claims require corresponding selected 7.x source evidence.
- `Manuals/Altibase_trunk` and `Manuals/Tools/Altibase_trunk` are the selected
  Altibase 8.1 verified source; customer-facing text must keep the established
  `Altibase 8.1 verified source` wording where the attachment set uses it.
- Patch-specific claims must keep exact patch boundaries and exact `BUG-*` or `TASK-*`
  tokens from selected patch or release sources.
- Internal support reports are traceability and validation evidence. They do not
  override selected product sources.
- Do not use web browsing, generic Oracle behavior, generic database assumptions, or
  non-repository memory to fill Altibase behavior.

## Replacement-Grade Definition

A source item is replacement-grade only when the attachment set supports all four use
cases below, unless a recorded guardrail explains why the item cannot safely support
one of them.

| Use case | Required behavior |
| --- | --- |
| Customer answerability | Give the customer the exact source-backed command, syntax, option, property, API, view, error, or runbook step needed to act safely, or ask for the missing exact input before answering. |
| LLM retrieval and synthesis | Preserve the exact tokens and retrieval aliases needed for lexical and semantic search, and provide owner headings or route anchors that make the item findable. |
| Coding-agent implementation | Preserve enough concrete syntax, setup, dependency, lifecycle, generated-file, sample-code, and validation detail for an implementation agent to adapt the source-backed behavior safely. |
| Test-case generation | Preserve positive cases, negative cases, boundary values, expected tokens, setup and teardown needs, validation SQL or command output, and stop conditions needed to design tests. |

`Covered` and `Covered-by-routing` dispositions must satisfy this standard. A vague
summary, broad cross-reference, or source-family mention is not enough.

## Universal Requirements

The requirements in this section apply to every source family when the selected source
contains the relevant evidence.

| Requirement | Attachment standard |
| --- | --- |
| Exact-token preservation | Preserve exact SQL keywords, object names, property names, view and column names, error codes, symbols, command options, API names, class names, file paths, environment variables, patch versions, `BUG-*` tokens, `TASK-*` tokens, and numeric values. Do not normalize away case, punctuation, prefixes, or abbreviations when those tokens are customer-answerable. |
| Customer-safe English | Translate or normalize Korean source prose into clear English. Do not paste large Korean prose blocks into customer-facing attachments. Preserve Korean terms only when they are literal product tokens or source names. |
| Executable syntax | Preserve enough grammar, command shape, required order, prerequisites, privileges, and example context for a reader or coding agent to issue the command safely in the right environment. |
| Options, defaults, ranges, and units | Preserve option names, defaults, valid values, ranges, units, mutability, precedence, scope, restart or recreate requirements, and error behavior. If a source omits a default or range, do not invent it. |
| Version and patch boundaries | Preserve whether the item is 7.1, 7.3, cross-version, 8.1 verified-source, or patch-specific. Keep patch versions and compatibility boundaries visible in customer-facing text. |
| Source-specific caveats | Preserve restrictions, unsupported cases, destructive behavior, implicit commits, replication or protocol risks, platform limits, privilege limits, and performance cautions. |
| Runnable examples | Preserve runnable examples when they are short and central to customer behavior. For long examples, preserve a compact skeleton plus a source-backed sample inventory unless full code is required for answerability. |
| Sample-code inventory | Preserve sample file paths, class names, method names, generated table names, connection properties, environment-variable assumptions, build commands, input files, output files, and expected result tokens. If full code is omitted, record the limitation or guardrail. |
| Generated-file semantics | Preserve file names, directories, generation commands, generated object scope, ownership, permissions, overwrite behavior, execution order, post-edit requirements, and replay or rollback cautions for generated SQL, scripts, config, logs, reports, or sample files. |
| Failure modes | Preserve error codes, symbols, messages, symptoms, likely source-backed causes, immediate actions, next checks, and evidence to request from the customer. |
| Guardrails | Ask for exact version, patch level, topology, object definition, logs, runtime output, installed package state, compiler/runtime version, or tool output when needed. Provide only the safest selected-source-backed next check. |
| Accepted omissions | Omit front matter, feedback instructions, audience boilerplate, decorative images, repetitive prose, generic overview text, and long verbatim code only when no customer answer, retrieval token, coding-agent step, test anchor, or guardrail depends on them. |

## Evidence And Disposition Rules

Use the catalog and matrix semantics from
`catalog_schema_and_extraction_scripts.md` without weakening them.

- `Covered` means the item is directly represented as an answer-ready block in the
  attachment set.
- `Covered-by-routing` means the item is represented through a specific owner heading,
  route anchor, alias, or index entry that contains the exact customer-answerable
  tokens or points to a concrete owner block. It cannot mean "generally related
  material exists somewhere."
- `Missing` means a selected source-backed item is absent or not answerable from the
  attachments. Treat this as remediation work.
- `Retrieval-weak` means the item exists but is unlikely to be found by GPT retrieval.
  Treat this as a routing or heading problem until fixed.
- `Guardrail` means selected sources do not support a definitive answer, or the answer
  depends on exact customer evidence. The guardrail must include the missing input and
  safest next check.
- `Out-of-scope` means the item is outside the locked selected corpus or upload
  package boundary and has a recorded reason.

Every row or remediation claim must be backed by source locators, exact-token checks,
attachment anchors, or validation commands. Benchmark questions can guide priority,
but they are not source authority by themselves.

## LLM Retrieval Requirements

Every replacement-grade item must be findable by both exact-token and practical
customer phrasing.

- Add headings, aliases, route entries, or compact owner inventories for low-frequency
  exact tokens.
- Keep one obvious owner attachment for each item; cross-references may exist, but the
  owner route must be clear.
- Do not rely on another attachment to answer an item when the route lacks the exact
  token or owner heading.
- Preserve synonyms and abbreviations from source syntax, such as full and abbreviated
  command forms, when they are documented.
- For patch-note and release-note items, keep the patch version and token in
  `00_version_release_platform.md` even when implementation detail is routed elsewhere.

## Coding-Agent Requirements

When a selected source supports implementation work, attachments must include enough
detail for a coding agent to produce a defensible first draft.

Required evidence includes, when source-backed:

- connection strings, DSN keys, properties, and environment variables;
- package, class, method, function, callback, handle, and constant names;
- compile, link, runtime, driver, library, JVM, or client prerequisites;
- object definitions, sample table names, seed data, and cleanup steps;
- transaction, autocommit, cursor, LOB, charset, and error-handling boundaries;
- generated scripts, output files, config files, permissions, and replay order;
- warnings that require customer confirmation before production execution.

Coding agents must not infer missing Altibase behavior from Oracle, JDBC, ODBC, SQL
standard, or generic database conventions.

## Test-Case Generation Requirements

When a selected source supports testing, attachments must provide enough anchors to
design both positive and negative tests.

Required evidence includes, when source-backed:

- setup prerequisites, privileges, object definitions, data, and environment variables;
- command or SQL input, option combinations, and boundary values;
- expected result rows, output tokens, error codes, messages, or state transitions;
- validation SQL, dictionary or performance-view checks, tool output checks, and log
  checks;
- cleanup, rollback, server restart, replication reset, certificate cleanup, or file
  removal needs;
- stop conditions for destructive SQL, backup/recovery, replication state changes,
  security/TLS, and version-sensitive properties.

Tests that require a live server, compiler, third-party product, network topology,
certificate set, or customer data remain guardrailed unless selected sources provide a
safe self-contained test environment.

## Generated-File Semantics

Generated files are answerable product behavior, not incidental examples, when selected
sources describe them.

Preserve the following when source-backed:

- generator command and required options;
- generated file path, naming pattern, extension, and directory;
- generated SQL or config execution order;
- object ownership, user/schema assumptions, privileges, and connection target;
- permissions controlled by variables such as tool-specific file-permission settings;
- overwrite, append, spool, log, backup, or temporary-file behavior;
- manual edits required before replay;
- tokens that prove generation succeeded or failed;
- cleanup and safety cautions for running generated scripts.

If generated content depends on installed metadata or runtime output, state the exact
input required and give a safe inspection command rather than inventing the file.

## Per-Domain Evidence Rules

| Domain | Required evidence for replacement-grade coverage |
| --- | --- |
| SQL | Statement grammar, mandatory and optional clauses, abbreviations, examples, object and privilege prerequisites, implicit commits, destructive effects, Oracle-compatibility differences, version boundaries, expected errors, and validation SQL. |
| PSM | Procedure, function, package, trigger, variable, cursor, exception, dynamic SQL, external procedure, privilege, compile, execute, and error-handling syntax; include runnable blocks or compact skeletons when source-backed. |
| Properties | Exact property name, default, valid values, range, unit, dynamic/static scope, restart or recreate requirement, dependency, precedence, version/patch boundary, side effect, related view or query, and source-backed error behavior. |
| Views | Exact view name, column names, meanings, units, join keys, sample checks, privilege or SYS access requirement, version availability, English/Korean list drift, and installed-metadata guardrail when source evidence is not enough. |
| Utilities | Command name, subcommands, options, option ordering, environment variables, input and output files, generated files, permissions, stdout/stderr tokens, exit or error behavior, examples, and safe production cautions. |
| Connectors and APIs | Driver or library name, version boundary, connection properties, DSN keys, class/function/method names, callbacks, handles, lifecycle order, compile/link/runtime requirements, charset/NLS behavior, transaction behavior, sample code, and validation checks. |
| Replication | DDL and administrative SQL, topology prerequisites, protocol and patch compatibility, replication states, queue/log behavior, conflict and recovery handling, restrictions, SSL/TLS separation, failover or switchover cautions, destructive steps, and validation views or commands. |
| Backup and recovery | Backup type, archive/log prerequisites, command sequence, tablespace or database scope, offline/online boundary, recovery target, media and incremental behavior, destructive warnings, rollback limits, validation queries, and required customer evidence before production recovery. |
| Security and TLS | Server and client properties, certificate and key files, CA/CAPATH behavior, cipher/protocol limits, FIPS or OpenSSL/JRE boundaries, listener ports, mutual authentication, TCP restriction, sample paths, session monitoring, and exact missing evidence for certificate or runtime failures. |
| Installation | Supported platforms, package names, kernel/user limits, environment variables, install/APatch/upgrade/uninstall commands, generated config files, startup/shutdown checks, first-run SQL, version labels, and unsupported-platform guardrails. |
| Migration | Source and target version boundaries, Oracle and Altibase compatibility limits, data type and DDL conversion rules, Migration Center or adapter options, generated files, validation queries, unsupported objects, character-set issues, and rollback or non-production test cautions. |
| Errors | Exact error code, symbol, message, family, source version, cause, action, related property/SQL/tool/view, ambiguity or source drift, next checks, and customer evidence required for root-cause claims. |
| Third-party guides | Third-party product version or scope, Altibase-specific setup, connector or plugin settings, authentication, generated files, sample paths, compatibility caveats, external-product guardrails, and clear separation between selected Altibase guidance and unverified vendor behavior. |

Technical documents support the domain they describe. They do not create a weaker
standard or override the authority order.

## Failure Modes And Guardrails

The attachment set must prefer a safe source-backed partial answer over an unsupported
complete answer.

Use a guardrail when a definitive answer requires:

- exact Altibase version or patch level;
- platform, package, or installed tool state;
- database object definition, metadata, or customer data;
- replication topology, state, logs, or peer version;
- backup media, archive log state, or recovery target;
- TLS certificate files, cipher configuration, or runtime handshake logs;
- compiler, driver, JVM, third-party product, or Kubernetes cluster state;
- live command output or error logs not present in selected sources.

Guardrail answers must name the missing input and provide a safest next check, such as
querying `V$VERSION`, `V$TABLE`, `V$ALLCOLUMN`, `V$PROPERTY`, or relevant replication
views, running installed tool help or version output, checking generated files, or
validating in non-production.

## Accepted Omissions

The following can be omitted from customer-facing attachments when they do not carry
answerable product behavior, retrieval tokens, implementation details, test anchors, or
guardrail evidence:

- manual front matter, target audience text, copyright notices, feedback channels, and
  document conventions;
- repeated prose that does not change command, option, API, property, error, version,
  or operational behavior;
- screenshots, decorative images, and PDF/image-only material unless a selected
  Markdown source depends on them for an answerable item;
- full long sample programs when a compact code skeleton and sample-code inventory
  preserve the customer-answerable identifiers and behavior;
- third-party product behavior beyond selected Altibase guide scope;
- runtime-success claims that require an installed environment.

An omission is not accepted merely because an item is low-frequency. Low-frequency
source-backed tokens still require coverage, routing, or a recorded guardrail.

## Validation Expectations

Before a remediation job claims replacement-grade closure, it should run the relevant
source-to-attachment checks and inspect the diff. Standard checks include:

```bash
python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers
python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py catalog-qa
python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py matrix-qa
python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py guardrail-audit
git diff --check
bash review/scripts/run_review_stage.sh validate
rg -n "^Verdict:|^\| (Blocker|High|Medium|Low) \|" review/reports/R*.md
```

Additional targeted checks should be added for scoped exact tokens, sample-code
inventories, generated-file tokens, option defaults/ranges, patch versions, protected
topics, coding-agent scenarios, and test-case generation scenarios.

## Workflow Handoff

`PWF-J016A` must apply this policy across all source families and produce the
cross-document replacement-grade gap handoff before broad domain remediation scales
out. Later jobs must not treat the SSL/TLS and iSQL samples as the only standard. They
are examples of the audit method; the policy above applies to every selected source
family and every attachment owner.
