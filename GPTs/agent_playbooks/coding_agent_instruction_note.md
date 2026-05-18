# Coding-Agent Instruction Note

- Job: `S2-J010`
- Scope: repository-local coding agents that generate, edit, validate, or review
  Altibase-backed service artifacts from the Stage 2 playbooks
- Status: instruction note

## Boundary

Use this note when a coding agent is asked to produce or modify Altibase-backed
service work. The goal is source-backed first drafts for practical artifacts, not
unverified production execution.

SQL, DDL, and DCL are required generated artifact classes, but they are only one
part of the broader service-development objective. The same routing discipline
also applies to generated code, commands, configuration, scripts, validation SQL,
test cases, troubleshooting packets, and stop condition records.

Do not edit `GPTs/attachments/`, `GPTs/upload_package/`, original source files,
or unrelated project files while using this note for Stage 2 work.

## Source Routing

1. Classify the user request before drafting artifacts. Start with
   `GPTs/agent_playbooks/service_development_artifact_generation.md` for broad
   service packages, then route to the focused domain playbook:
   `ddl_generation.md`, `sql_data_types.md`, `properties.md`,
   `dictionary_views.md`, `java_jdbc.md`, `odbc_c_clients.md`,
   `installation_startup.md`, `backup_recovery.md`, `protected_operations.md`,
   `replication_cdc.md`, `tools.md`, `migration_integrations.md`,
   `errors_troubleshooting.md`, or `aid_version_release_patch_routing.md`.
2. Read the relevant row in `GPTs/agent_playbooks/playbook_manifest.tsv`.
   Copy the exact `source ID`, source-pack block reference, Korean-aligned
   baseline block ID, AID route or tier, guardrail ID, generated artifact type,
   protected-topic flag, and required missing input prompt into the work plan.
3. Use `GPTs/korean_aligned_english/` as the working English route when a
   relevant baseline block exists. Use `GPTs/source_pack/` when exact syntax,
   command options, property rows, view columns, error text, API tokens,
   release-note tokens, or patch-specific behavior must be checked.
4. Route AID-derived material through
   `GPTs/agent_playbooks/aid_version_release_patch_routing.md` and preserve the
   recorded AID label. Evidence-only and accepted-limitation rows stay evidence
   or limitations unless a later packaging decision records a different use.
5. Treat Korean Altibase manuals, Korean release notes, Korean patch notes,
   Korean technical documents, and Korean third-party guides as authoritative
   where selected. English manuals and English-only auxiliary sources are
   extraction aids unless their classification explicitly permits guarded use.

## Missing Input Prompts

Ask for missing input before producing a runnable artifact when the answer
depends on customer-specific evidence. The prompt must name the exact missing
item and provide the safest source-backed next check.

Common missing input prompts:

- Target Altibase version and patch level.
- Platform, package, client driver, JDK, compiler, third-party connector, or
  installed tool version.
- Object definitions, schema names, table types, tablespace names, privilege
  model, property names, and current `V$PROPERTY` or dictionary evidence.
- Logs, exact error code, `SQLSTATE`, error message, runtime state,
  replication state, source/target topology, and validation output.
- Backup point, rollback plan, maintenance window, production approval, and
  cleanup target for destructive, privilege-changing, storage-changing,
  replication-changing, or security-sensitive work.

If the missing input affects safety or correctness, stop at a non-runnable
draft, evidence checklist, or read-only first check.

## Artifact Structure

Separate explanation from runnable artifacts. Do not bury operational steps in
prose when the customer needs copy/paste material.

Use this structure for coding-agent output or repository documentation:

```text
source_route:
  playbooks:
  source_ids:
  source_pack_blocks:
  baseline_blocks:
  aid_route_or_tier:
  guardrails:

customer_inputs_used:
  target_version:
  patch_level:
  runtime_evidence:
  rollback_or_cleanup_plan:

generated_artifacts:
  explanation:
  runnable_files:
  validation:
  test_plan:
  stop_conditions:
```

Runnable artifacts must be in fenced code blocks or repository files with clear
filenames. Keep each class separate:

- SQL, DDL, DCL, and DML: separate precheck SQL, schema SQL, privilege SQL,
  data-change SQL, validation SQL, and cleanup SQL.
- Code: separate application code, connection code, error handling, transaction
  handling, and test scaffolding from explanation.
- Commands and scripts: separate shell commands, iSQL/iLoader/tool commands,
  compile/link commands, migration scripts, and diagnostics scripts.
- Configuration: separate `altibase.properties`, JDBC URL, ODBC DSN, TLS,
  replication, Kubernetes/AKU, and third-party configuration snippets.
- Test cases: include setup, positive case, negative case, expected output
  token, validation query or command, and cleanup.

## Validation

Every generated artifact package must include validation before it is considered
customer-usable:

- Source validation: record the playbook path, `source ID`, source-pack block,
  baseline block, AID label when used, and guardrail ID.
- Syntax or token validation: preserve Altibase tokens exactly and recheck the
  target source block for SQL, DDL, DCL, command options, property names, view
  columns, API names, error codes, `BUG-*`, and `TASK-*`.
- Runtime validation: provide read-only checks first, such as `V$VERSION`,
  `V$PROPERTY`, dictionary/performance views, client version output, tool help,
  logs, and compile or connection checks.
- Result validation: state expected output tokens, row counts, error tokens,
  connection success criteria, file outputs, or rollback confirmation.
- Documentation validation: run the relevant local checker when the repository
  contract is updated, including
  `python3 GPTs/agent_playbooks/scripts/validate_playbooks.py` for Stage 2
  playbook and instruction-note changes.

## Stop Conditions

Stop and ask for missing input instead of generating final runnable artifacts
when:

- The target version, patch level, platform, package, driver, or tool version
  is missing for version-sensitive behavior.
- The request depends on object definitions, logs, runtime output, installed
  tool output, source/target topology, third-party compatibility, or live
  validation that has not been supplied.
- A requested behavior is only supported by `Altibase 8.1 verified source` and
  the target is 7.1 or 7.3 without exact installed-version evidence.
- The work may drop, truncate, overwrite, load, synchronize, replicate, change
  privileges, change persistent properties, change storage, alter TLS, or alter
  recovery state without explicit approval and rollback or recovery evidence.
- The available route is evidence-only, accepted limitation, English-only
  auxiliary, or guarded candidate and the customer asks for definitive
  production behavior.

## Forbidden Generic Assumptions

Avoid unsupported generic database assumptions.

Do not fill gaps from Oracle, MySQL, PostgreSQL, ANSI SQL, generic JDBC,
generic ODBC, generic Kubernetes, or generic third-party connector behavior.
Do not invent Altibase syntax, `IF EXISTS` or `IF NOT EXISTS` support, JSON or
temporary LOB behavior, property defaults, view columns, error causes, command
options, platform support, API signatures, TLS compatibility, replication
semantics, or patch behavior without the exact source route and customer
evidence required by the relevant playbook.

## Self-Review Checklist

Before handing off:

- The response or patch names the selected playbook and source route.
- Every runnable block is separated from explanation.
- SQL, DDL, DCL, code, commands, configuration, scripts, validation SQL, and
  test material each have required inputs and validation where used.
- Missing input prompts are explicit and do not ask for unnecessary unrelated
  evidence.
- Stop condition text is visible for unsafe, unsupported, or runtime-dependent
  work.
- No unsupported generic database assumption was used to complete an Altibase
  detail.
