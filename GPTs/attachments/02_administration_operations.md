# 02. Administration and Operations

## Applicable Versions

- 7.1: Based on Altibase 7.1 Administrator's Manual.
- 7.3: Based on Altibase 7.3 Administrator's Manual.
- 8.1: Based on Altibase 8.1 verified source Administrator's Manual.

## Questions This File Can Answer

- How are accounts and privileges managed?
- How are tablespaces, datafiles, and log files managed?
- What are the basic backup and recovery procedures?
- What operational differences exist between memory and disk tablespaces?

## Source Documents

- 7.1: Altibase 7.1 Administrator's Manual.
- 7.3: Altibase 7.3 Administrator's Manual.
- 8.1: Altibase 8.1 verified source Administrator's Manual.

## Core Guidance

- Operational answers should follow `Check current state -> Change SQL or command -> Verify after applying`.
- Operational changes should mention backup, privileges, service impact, and rollback feasibility.
- Tablespace and datafile guidance should cover not only SQL syntax but also filesystem free space and recovery impact.

## Operations Checklist Format

1. Identify the current version and target object.
2. Query related properties and meta or performance views.
3. Confirm backup status or impact scope before the change.
4. Execute the DDL or operational command.
5. Verify with meta or performance views after the change.

## Version Differences

- 7.1: Use 7.1 Administrator's Manual behavior for account, tablespace, backup, and recovery guidance.
- 7.3: Add 7.3 operational changes when a command, property, or view differs from 7.1.
- 8.1: Use Altibase 8.1 verified source for 8.1 operations and mark 8.1-only behavior explicitly.

## Conversion TODO

- Decompose backup and recovery procedures into before, during, and after checklists.
- Convert tablespace tables into per-type explanation blocks.
- Convert operations images and architecture figures to Mermaid flowcharts.
