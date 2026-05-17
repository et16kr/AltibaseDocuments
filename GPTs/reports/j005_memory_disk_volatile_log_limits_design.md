# J005 Design Note: Memory, Disk, Volatile, Log, And Cache Limits

## Scope

This job strengthens answer-ready documentation for Altibase memory, disk, volatile,
log-size, log-creation, plan-cache, result-cache, and related capacity-limit
properties. It does not change benchmark thresholds, source documents, or unrelated
property families reserved for later jobs.

## Evidence Used

- `PROP-106` and `PROP-107` missed exact `LOG_FILE_SIZE` defaults, ranges, release-note
  maximum changes, read-only change path, and offline replication caution.
- `PROP-108`, `PROP-109`, and `PROP-110` missed capacity-limit defaults, 32-bit and
  64-bit ranges, `2G` wording, read-only status, and exceeded-limit behavior.
- `PROP-115`, `PROP-116`, and `PROP-117` missed SQL plan cache and result cache
  details such as `MAX_CACHE_SIZE`, `ALTER SYSTEM`, `10M`, `4096`, and `ULONG MAX`.
- `PROP-134` missed `LOG_CREATE_METHOD` OS-specific defaults and `write()` versus
  `fallocate()` behavior after the 8.1 default-change note.

## Documentation Pattern

The remediation keeps the existing attachment structure and adds compact, literal
blocks that an LLM can quote directly:

- source version scope and release-note boundaries;
- default, range, unit, data type where material, and read-only/read-write status;
- exact dynamic-change method or explicit database-recreation/static-change cautions;
- exceeded-limit behavior for memory, disk, volatile, Temporary LOB, and result cache;
- `V$PROPERTY` and subsystem-view checks with literal column and property names.

## Boundary

Optimizer mode, session locale, account/security, network, and replication properties
remain for J006 and J007 unless they are mentioned only as related checks for the
capacity and cache blocks.
