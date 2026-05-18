# Properties Playbook

- Playbook ID: `APB-000004`
- Owning job: `S2-J003`
- Validation status: `pass`
- Supported versions: Altibase 7.1, Altibase 7.3, and `Altibase 8.1 verified source`
- Protected topic: yes

## Source Routes

| Route | Source IDs | Source-pack block refs | Baseline blocks |
| --- | --- | --- | --- |
| Property lookup, defaults, ranges, dynamic behavior, and change SQL | `SRC-000056`, `SRC-000025`, `SRC-000120`, `SRC-000089`, `SRC-000180`, `SRC-000150`, `SRC-000072`, `SRC-000040`, `SRC-000134`, `SRC-000103`, `SRC-000194`, `SRC-000163` | `SRC-000056/BLOCK-000515`, `SRC-000025/BLOCK-000514`, `SRC-000120/BLOCK-000517`, `SRC-000089/BLOCK-000516`, `SRC-000180/BLOCK-000519`, `SRC-000150/BLOCK-000518`, `SRC-000072/BLOCK-000884`, `SRC-000040/BLOCK-000883`, `SRC-000134/BLOCK-000886`, `SRC-000103/BLOCK-000885`, `SRC-000194/BLOCK-000888`, `SRC-000163/BLOCK-000887` | `KAE-BLOCK-000272`, `KAE-BLOCK-000273` |

Guardrails: `CONF-000004` and `CONF-000005` remain open. This playbook can
draft property lookup and change artifacts, but it cannot claim exhaustive
property coverage or exact property defaults, ranges, units, or online-change
support without the target-version property section.

Forbidden assumption note: do not infer an Altibase property default, range,
restart requirement, or dynamic-change level from Oracle, MySQL, PostgreSQL, or
ANSI SQL terminology.

## Required Customer Inputs

Before generating a property artifact, collect:

- Target Altibase version and patch level.
- Property name, current value, desired value, and why the change is needed.
- Current startup phase, connected user, and whether `SYS` or `ALTER SYSTEM`
  privilege is available.
- Exact target-version property section or source route for default value,
  attribute, value range, unit, dynamic-change level, related views, cautions,
  and version scope.
- Whether the change should use `ALTER SESSION`, `ALTER SYSTEM`,
  `altibase.properties`, database creation, startup-control operation, or a
  customer maintenance procedure.
- Restart window, service impact, replication state, archive-log or storage
  impact, backup point, validation query, and rollback plan.

## Generated Artifacts

This playbook may draft:

- Property inventory and evidence request.
- Runtime inspection SQL using `V$PROPERTY`.
- A proposed `ALTER SESSION` or `ALTER SYSTEM` statement when dynamic-change
  support is source-confirmed.
- An `altibase.properties` edit plan when the property is static or file-based.
- Validation and rollback notes for protected properties.

## Procedure

1. Identify the property in the exact target-version General Reference route.
   Preserve source fields: property name, default value, attribute, value
   range, unit, dynamic-change level, related views, cautions, and version
   scope.
2. Confirm the dynamic-change vocabulary:
   - `SESSION` maps to `ALTER SESSION`.
   - `SYSTEM` maps to `ALTER SYSTEM`.
   - `BOTH` can use either path when the source and customer intent allow it.
   - `NONE` is not dynamically changeable.
3. Treat `V$PROPERTY` as runtime evidence only. Current runtime value does not
   prove the default, range, unit, or dynamic-change level.
4. For protected properties, require maintenance and validation evidence before
   drafting a runnable command. Protected examples include `ADMIN_MODE`,
   `REPLICATION_DDL_ENABLE`, `REPLICATION_DDL_ENABLE_LEVEL`,
   `REPLICATION_SQL_APPLY_ENABLE`, `MEM_MAX_DB_SIZE`, `LOGANCHOR_DIR`,
   `ARCHIVE_DIR`, `TRANSACTION_SEGMENT_COUNT`,
   `INCREMENTAL_BACKUP_CHUNK_SIZE`, `TEMPORARY_LOB_ENABLE`,
   `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`, `MEMORY_TEMPLOB_PIECE_SIZE`,
   `SSL_ENABLE`, `SSL_PORT_NO`, and `SNMP_ENABLE`.
5. Preserve the source-drift caution for `REPLICATION_UPDATE_REPLACE` and
   `REPLICATION_META_ITEM_COUNT_DIFF_ENABLE`: require installed-version
   checks for 8.1 before using them in customer artifacts.

## Artifact Templates

```sql
-- 00_property_inventory.sql
SELECT NAME, VALUE1, VALUE2
FROM V$PROPERTY
WHERE NAME IN ('<PROPERTY_NAME>',
               'ADMIN_MODE',
               'REPLICATION_DDL_ENABLE',
               'REPLICATION_DDL_ENABLE_LEVEL',
               'REPLICATION_SQL_APPLY_ENABLE',
               'TEMPORARY_LOB_ENABLE',
               'MEMORY_TEMPLOB_MAX_ALLOC_SIZE',
               'MEMORY_TEMPLOB_PIECE_SIZE')
ORDER BY NAME;
```

```sql
-- 10_dynamic_property_change.sql
-- Use only when the exact target-version property section confirms SESSION.
ALTER SESSION SET <PROPERTY_NAME> = <VALUE>;

-- Use only when the exact target-version property section confirms SYSTEM.
ALTER SYSTEM SET <PROPERTY_NAME> = <VALUE>;
```

```text
# altibase.properties change plan
# Use only when the exact target-version source confirms file-based/static use.
# Record original value, desired value, restart requirement, and rollback.

<PROPERTY_NAME> = <VALUE>
```

```sql
-- 90_property_validation.sql
SELECT NAME, VALUE1, VALUE2
FROM V$PROPERTY
WHERE NAME = '<PROPERTY_NAME>';
```

## Guardrails

- Stop before changing a read-only property, a `NONE` dynamic-change property,
  a startup-only property, or a phase-restricted property through an online SQL
  path.
- Stop if the requested value is outside the source-defined range or if the
  unit is unknown.
- Stop before changing replication, archive-log, log-anchor, memory-size,
  incremental-backup, Temporary LOB, SSL/TLS, SNMP, or admin-mode properties
  without a maintenance window and validation plan.
- Do not use `ALTER SYSTEM` unless the connected user and source route permit
  it. `ALTER SYSTEM` can change system properties only when the property
  supports that mode.
- Do not present a property change as persistent or runtime-only unless the
  exact source route confirms persistence and activation behavior.

## Validation Checks

Every property artifact must include:

- Exact source route and target-version property section.
- Runtime before value from `V$PROPERTY` when available.
- Desired value, unit, range check, dynamic-change level, and user privilege
  check.
- Restart or phase-transition requirement when applicable.
- Post-change `V$PROPERTY` query.
- Rollback command or file rollback note.
- Customer confirmation for any service-impacting or replication-impacting
  property.

## Stop Conditions

Stop and ask for more evidence if:

- The property name, target version, current value, desired value, or exact
  source section is missing.
- The property detailed source block is absent, incomplete, or inconsistent for
  the target version.
- The change depends on live workload, logs, replication state, archive-log
  state, memory sizing, restart tolerance, or installed-version behavior that
  the customer has not supplied.
- The request asks for a full property table, all defaults, all ranges, or
  production-ready tuning recommendations from this playbook alone.
