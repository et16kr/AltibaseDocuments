# J013 Replication Topology State SQL Design Note

Date: 2026-05-17
Job: J013 - Replication topology state and SQL blocks

## Scope

J013 strengthens customer-facing replication reference blocks for topology, state transitions, DDL/control SQL, replication gap handling, compatibility checks, and unsafe-operation guardrails.

Primary attachment targets:

- `GPTs/attachments/09_replication_ha_cdc.md`
- `GPTs/attachments/03_sql_ddl_generation.md`
- `GPTs/attachments/06_data_dictionary_performance_views.md`

J014 remains responsible for deeper CDC, Log Analyzer, Replication Manager, TLS, certificate, port, and network diagnostic remediation. J013 may mention these topics only where they are needed to keep replication SQL, state, or compatibility answers safe.

## Source Basis

The edits are source-backed by repository-local selected sources:

- Korean Altibase 7.3 and 8.1 verified source SQL Reference sections for `CREATE REPLICATION`, `ALTER REPLICATION`, `ALTER SESSION SET REPLICATION`, and `DROP REPLICATION`.
- Korean Altibase 7.3 and 8.1 verified source Replication Manual sections for terminology, conflict schemes, `SYNC`, `SYNC ONLY`, `START`, `QUICKSTART`, `RESET`, `DROP HOST ALL`, `GAPLESS`, `PARALLEL`, `META_LOGGING`, and offline replication.
- Korean General Reference data dictionary sections for `SYSTEM_.SYS_REPLICATIONS_`, `SYSTEM_.SYS_REPL_HOSTS_`, `SYSTEM_.SYS_REPL_ITEMS_`, `V$REPSENDER`, `V$REPSYNC`, and offline status.
- Korean release and patch notes for DDL replication compatibility, 7.1 patch protocol transitions, `BUG-49398`, and `BUG-46940`.
- `Technical Documents/kor/ReplicationCompatibility.md` for 7.1/7.3 LAZY compatibility and protocol-version boundaries.

## Documentation Shape

The job keeps the existing attachment organization and adds retrieval-dense blocks rather than large prose rewrites:

- `03_sql_ddl_generation.md`: exact SQL-generation tokens for `replication_host_ip`, `replication_host_port_no`, `SYS`, `AS MASTER`, `AS SLAVE`, `FOR ANALYSIS`, `DROP HOST ALL`, and offline forms.
- `06_data_dictionary_performance_views.md`: compact metadata/runtime decode blocks so answers preserve exact view and column tokens such as `CONFLICT_RESOLUTION`, `REMOTE_FAULT_DETECT_TIME`, `START_FLAG`, `NET_ERROR_FLAG`, `STATUS`, `REPL_MODE`, `ACT_REPL_MODE`, `SYNC_RECORD_COUNT`, and `V$REPOFFLINE_STATUS`.
- `09_replication_ha_cdc.md`: exact-answer blocks for topology terms, LAZY/EAGER state, Active-Active conflicts, control SQL, `SYNC`/`SYNC ONLY`, `GAPLESS`, `PARALLEL`, offline replication, host-list failover, DDL replication guardrails, compatibility, and patch-specific rebuild/protocol cases.

## Safety Rules Preserved

- Ask for exact version, patch, topology, role, object names, and current gap before state-changing replication guidance.
- Do not use `QUICKSTART`, `RESET`, `DROP TABLE`, `DROP REPLICATION`, offline replication, DDL replication, or receive-only conversion as generic fixes.
- Do not infer 8.1-to-older compatibility from protocol prefixes alone.
- Keep customer-facing content in English while preserving exact Altibase tokens from the Korean authoritative sources.
