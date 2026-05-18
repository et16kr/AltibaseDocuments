# Installation And Startup Playbook

- Playbook ID: `APB-000001`
- Owning job: `S2-J005`
- Validation status: `pass`
- Supported versions: Altibase 7.1, Altibase 7.3, and `Altibase 8.1 verified source`
- Protected topic: yes

## Source Routes

| Route | Source IDs | Source-pack block refs | Baseline blocks |
| --- | --- | --- | --- |
| Installation prerequisites, environment setup, package flow, license, database creation, startup phases, shutdown modes, and first checks | `SRC-000060`, `SRC-000029`, `SRC-000124`, `SRC-000093`, `SRC-000184`, `SRC-000154`, `SRC-000058`, `SRC-000027`, `SRC-000122`, `SRC-000091`, `SRC-000182`, `SRC-000152`, `SRC-000049`, `SRC-000018`, `SRC-000113`, `SRC-000082`, `SRC-000173`, `SRC-000143`, `AID-SRC-000426`, `AID-SRC-000428` | `SRC-000060/BLOCK-000529`, `SRC-000029/BLOCK-000527`, `SRC-000124/BLOCK-000533`, `SRC-000093/BLOCK-000531`, `SRC-000184/BLOCK-000537`, `SRC-000154/BLOCK-000535`, `SRC-000058/BLOCK-000528`, `SRC-000027/BLOCK-000526`, `SRC-000122/BLOCK-000532`, `SRC-000091/BLOCK-000530`, `SRC-000182/BLOCK-000536`, `SRC-000152/BLOCK-000534`, `SRC-000049/BLOCK-000002`, `SRC-000018/BLOCK-000001`, `SRC-000113/BLOCK-000004`, `SRC-000082/BLOCK-000003`, `SRC-000173/BLOCK-000006`, `SRC-000143/BLOCK-000005`, `BLOCK-000436`, `BLOCK-000438` | `KAE-BLOCK-000272`, `KAE-BLOCK-000276` |

Guardrails: `CONF-000004` and `CONF-000007` remain open. This playbook can
draft guarded installation and startup artifacts, but exact operating-system
support, package names, patch requirements, kernel parameters, resource sizing,
license behavior, and production startup automation require the exact
target-version source route and customer environment evidence.

Forbidden assumption note: do not infer platform support, startup commands,
shutdown safety, database character sets, or installer behavior from generic
Unix, Linux, Windows, Oracle, or other database practices.

## Required Customer Inputs

Missing input prompts to collect before generating a runnable artifact:

- Target Altibase version and patch level.
- Server or client package, operating system, CPU architecture, glibc or library
  level where relevant, and package download or installer evidence.
- Installation account, intended `ALTIBASE_HOME`, profile file to source, and
  whether `$ALTIBASE_HOME/conf/altibase_user.env` exists.
- License-file status and path under `$ALTIBASE_HOME/conf/license`.
- Database name, service port, archive-log choice, database character set,
  national character set, memory size, buffer size, and storage directories.
- Current startup phase, connected user, SYSDBA access, and whether the command
  is for new installation, database creation, restart, or shutdown.
- Maintenance window, current sessions, backup point, service impact tolerance,
  validation plan, and rollback or recovery expectation.
- AID labels when AID operational notes are used: preserve Korean-source-verified,
  link-validated, English-only auxiliary, and source-limitation classifications.

## Generated Artifacts

This playbook may draft:

- Installation prerequisite checklist.
- Environment setup and verification commands.
- Database-creation preparation notes and guarded `CREATE DATABASE` template.
- Startup phase and shutdown-mode runbooks.
- First-check SQL and command bundles.
- Rollback or recovery notes for failed installation, failed database creation,
  interrupted startup, or forceful shutdown.

## Procedure

1. Confirm the target-version route. Korean manuals remain authoritative, English
   manuals are extraction aids, and 8.1 material must retain the
   `Altibase 8.1 verified source` boundary.
2. Check the package and host before installation. Use source-backed platform
   rows, not generic operating-system assumptions.
3. Confirm the installation account, `ALTIBASE_HOME`, filesystem layout, and
   profile sourcing. The normal environment variables to verify are
   `ALTIBASE_HOME`, `PATH`, `LD_LIBRARY_PATH`, and `CLASSPATH`.
4. Confirm the license file before startup. A missing or expired license is a
   startup blocker.
5. Review installer-generated pre-install and post-install scripts before
   running any root-level or database-creation action.
6. Before `CREATE DATABASE`, confirm storage-directory properties, log-anchor
   locations, archive-log choice, character sets, and memory-related sizing.
7. Use SYSDBA for startup, shutdown, `CREATE DATABASE`, recovery, and resetlogs
   paths. Confirm the current startup phase before issuing phase-restricted
   commands.
8. Treat `SHUTDOWN ABORT`, `DROP DATABASE`, incomplete recovery, and resetlogs
   as protected operations that require a maintenance window, backup point, and
   recovery plan.

## Artifact Templates

```sh
# 00_installation_first_checks.sh
uname -a
id
test -n "$ALTIBASE_HOME" && printf 'ALTIBASE_HOME=%s\n' "$ALTIBASE_HOME"
test -r "$ALTIBASE_HOME/conf/altibase_user.env" && . "$ALTIBASE_HOME/conf/altibase_user.env"
test -r "$ALTIBASE_HOME/conf/license" && ls -l "$ALTIBASE_HOME/conf/license"
test -r "$ALTIBASE_HOME/conf/altibase.properties" && ls -l "$ALTIBASE_HOME/conf/altibase.properties"
test -r "$ALTIBASE_HOME/install/pre_install.sh" && ls -l "$ALTIBASE_HOME/install/pre_install.sh"
test -r "$ALTIBASE_HOME/install/post_install.sh" && ls -l "$ALTIBASE_HOME/install/post_install.sh"
```

```sql
-- 10_database_creation_guarded_template.sql
-- Use only after the exact target-version source confirms character sets,
-- archive-log choice, storage directories, and initialization properties.
-- Administration session shell command:
-- isql -u sys -p <SYS_PASSWORD> -sysdba

STARTUP PROCESS;

CREATE DATABASE <database_name> INITSIZE=<memory_size>
<ARCHIVELOG_OR_NOARCHIVELOG>
CHARACTER SET <database_character_set>
NATIONAL CHARACTER SET <national_character_set>;
```

```sql
-- 20_startup_shutdown_phase_template.sql
-- Confirm the current phase and maintenance window before use.
STARTUP PROCESS;
STARTUP CONTROL;
STARTUP META;
STARTUP SERVICE;

SHUTDOWN NORMAL;
SHUTDOWN IMMEDIATE;
-- SHUTDOWN ABORT is forceful; use only with an accepted recovery plan.
SHUTDOWN ABORT;
```

```sql
-- 90_startup_validation.sql
SELECT * FROM V$VERSION;

SELECT NAME, VALUE1, VALUE2
FROM V$PROPERTY
WHERE NAME IN ('DB_NAME',
               'SERVICE_PORT_NO',
               'LOGANCHOR_DIR',
               'ARCHIVE_DIR',
               'MEM_MAX_DB_SIZE')
ORDER BY NAME;
```

## Guardrails

- Stop before installation if the operating system, CPU architecture, package
  type, library level, or patch support is not confirmed by the exact source.
- Stop before editing kernel/resource settings or profile files when the
  executing account, required privilege, or customer change-control approval is
  missing.
- Stop before `CREATE DATABASE` when character sets, archive-log mode, storage
  paths, log-anchor paths, memory settings, or license state are unknown.
- Stop before `SHUTDOWN ABORT`, `DROP DATABASE`, incomplete recovery, resetlogs,
  or startup automation without a maintenance window, backup point, validation
  plan, and rollback or recovery notes.
- Do not present a generated installation or startup procedure as production
  ready when exact package output, installed patch level, or live startup logs
  have not been supplied.

## Validation Checks

Every generated installation or startup artifact must include:

- Exact source route, target version, patch level, host platform, and package
  evidence.
- File checks for `ALTIBASE_HOME`, `altibase_user.env`, `altibase.properties`,
  `license`, and installer scripts when applicable.
- Non-destructive first checks before commands that change system settings,
  database state, or storage.
- Startup phase confirmation before phase-specific SQL.
- Post-start `V$VERSION` and `V$PROPERTY` checks when the database reaches a
  queryable phase.
- A rollback note for file/profile edits and a recovery note for failed
  database creation, abnormal shutdown, or restart recovery.

## Stop Conditions

Stop and ask for missing input if:

- The target version, patch, host platform, package, `ALTIBASE_HOME`, license,
  startup phase, or SYSDBA path is missing.
- The request depends on platform support, patch-specific installer behavior,
  exact kernel settings, production sizing, customer storage layout, or live
  startup logs that have not been supplied.
- The customer asks for copy/paste `CREATE DATABASE`, shutdown, resetlogs, or
  startup automation without approving service impact, validation, and rollback
  or recovery expectations.
