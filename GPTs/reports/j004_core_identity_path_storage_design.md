# J004 Design Note: Core Identity, Path, And Storage Properties

## Scope

This job strengthens answer-ready documentation for core Altibase property families:
database identity, static path properties, memory database directories, log and log
anchor directories, disk database file defaults, and storage defaults. It does not
change benchmark thresholds or source documents.

## Evidence Used

- `PROP-103` missed the `DB_NAME` read-only, single-value, no-explicit-range fact.
- `PROP-104` and `PROP-105` missed or failed to preserve `STOREDCOUNT`, `VALUE1`,
  `VALUE8`, and `LOGANCHOR_DIR` default/count facts.
- The exact-token inventory classed these as content, retrieval, or answer synthesis
  gaps, not judge calibration issues.
- Source backing is from the selected Korean General Reference 1 property blocks and
  General Reference 2 `V$PROPERTY` column block for 7.1, 7.3, and Altibase 8.1
  verified source where applicable.

## Documentation Pattern

The remediation adds compact, item-level blocks that an LLM can quote directly:

- purpose and version scope;
- property default, count, unit, and range;
- read-only/read-write and single-value/multi-value status;
- startup, restart, or recreation guidance;
- `V$PROPERTY` checks using literal `NAME`, `STOREDCOUNT`, `ATTR`, `MIN`, `MAX`,
  `VALUE1`, and `VALUE8`;
- operational stop conditions for missing path, count, or customer-specific inputs.

## Boundary

Capacity-limit tuning, optimizer/session properties, security/network properties, and
replication properties remain for later jobs unless they are needed only as related
checks for these core path and storage blocks.
