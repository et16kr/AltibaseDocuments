# J006 Design Note: Optimizer, Session, Locale, Lock, Timeout, And Safety Properties

## Scope

This job strengthens answer-ready documentation for Altibase optimizer,
normalization, LOB client cache, lock-escalation, timeout, autocommit, session locale,
plan/result cache, Temporary LOB, and DDL-safety property questions. It does not
change benchmark thresholds, original source documents, or unrelated security,
replication, network, SQL-generation, or backup/recovery runbooks reserved for later
jobs.

## Evidence Used

- `PROP-120` missed `NORMALFORM_MAXIMUM`, `CNF`, `DNF`, `NNF`, `2048`, and
  `[1, 2^32 - 1]` behavior.
- `PROP-122` missed `LOCK_ESCALATION_MEMORY_SIZE`, `100M`, `1000MB`, `inplace
  update`, lock-mode, and `ALTER SYSTEM` cautions.
- `PROP-124` missed `NLS_TERRITORY`, `NLS_NUMERIC_CHARACTERS='.,'`, first-two-character
  interpretation, forbidden leading characters, and session-only change behavior.
- `PROP-125` through `PROP-129` missed timeout rollback/disconnect differences,
  `DDL_LOCK_TIMEOUT` special values, and exact `ALTER SESSION SET AUTOCOMMIT = FALSE`.
- `PROP-115`, `PROP-116`, `PROP-143`, and `PROP-150` needed stronger answer-ready
  plan-cache, result-cache, Temporary LOB, and `EXEC_DDL_DISABLE` blocks.

## Documentation Pattern

The remediation keeps the existing attachment structure and adds compact literal
blocks that an LLM can quote directly:

- exact default, range, value meanings, and units;
- dynamic scope: `ALTER SYSTEM`, `ALTER SESSION`, both, read-only, or verify-installed;
- runtime effect and stop condition when changing the value can affect locking,
  rollback, memory growth, plan choice, DDL availability, or JSON/Temporary LOB use;
- check SQL using `V$PROPERTY`, `V$SESSION`, `V$SQL_PLAN_CACHE`, `V$TIME_ZONE_NAMES`,
  or `V$TEMPORARY_LOBS` as applicable.

## Boundary

Archive-log failure policy, checkpoint scheduling, restart-recovery tuning, security,
replication, and network properties are left for their owning jobs unless they appear
only as related performance-property checks.
