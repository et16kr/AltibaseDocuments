# R03 DDL Tablespace Storage Review

Date: 2026-05-14
Reviewer: Codex
Verdict: Review Required

## Scope

- Attachments:
  - `GPTs/attachments/03_sql_ddl_generation.md`
  - `GPTs/attachments/02_administration_operations.md`
  - `GPTs/attachments/09_replication_ha_cdc.md`
- Supporting reports:
  - `GPTs/reports/sql_generation_test_results.md`
- Source manuals sampled:
  - `Manuals/Altibase_7.1/eng/SQL Reference.md`
  - `Manuals/Altibase_7.3/eng/SQL Reference.md`
  - `Manuals/Altibase_trunk/eng/SQL Reference.md`
  - Altibase 7.3 and 8.1 source Administrator's Manual sections for tablespace storage clauses
  - Altibase 7.3 and 8.1 source Replication Manual sections for replication DDL synchronization
  - Altibase 8.1 source General Reference sections for dictionary views and replication properties

## Commands Run

```bash
wc -l GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/02_administration_operations.md GPTs/attachments/09_replication_ha_cdc.md GPTs/reports/sql_generation_test_results.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' | sort | wc -l
rg -n 'IF NOT EXISTS|IF EXISTS|DROP TABLESPACE|AND DATAFILES|REPLICATION_DDL_(ENABLE|ENABLE_LEVEL|SYNC)|REPLICATION_SQL_APPLY_ENABLE|SPLIT EACH' GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/02_administration_operations.md GPTs/attachments/09_replication_ha_cdc.md
rg -n 'IF NOT EXISTS|IF EXISTS|AND DATAFILES|REPLICATION_DDL_(ENABLE|ENABLE_LEVEL|SYNC)|REPLICATION_SQL_APPLY_ENABLE|SPLIT EACH' "Manuals/Altibase_trunk/eng/SQL Reference.md" "Manuals/Altibase_trunk/eng/Replication Manual.md" "Manuals/Altibase_7.3/eng/Replication Manual.md"
nl -ba GPTs/attachments/09_replication_ha_cdc.md | sed -n '790,880p'
nl -ba GPTs/attachments/02_administration_operations.md | sed -n '650,760p'
nl -ba GPTs/attachments/02_administration_operations.md | sed -n '960,1008p'
nl -ba GPTs/attachments/03_sql_ddl_generation.md | sed -n '1060,1098p'
```

## Findings

No Blocker findings were identified. High and Medium issues below should be corrected before the attachments are uploaded.

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| High | `GPTs/attachments/09_replication_ha_cdc.md` | 854 | The SQL apply DDL synchronization procedure is incomplete. It sets `REPLICATION_DDL_SYNC` and `REPLICATION_SQL_APPLY_ENABLE`, but it omits the required `REPLICATION_DDL_ENABLE` and `REPLICATION_DDL_ENABLE_LEVEL` enable and reset steps on the local and remote servers. The properties list also omits `REPLICATION_DDL_SYNC`, even though the procedure uses it. The source Replication Manual procedure requires local `ALTER SYSTEM SET REPLICATION_DDL_ENABLE = 1`, `ALTER SYSTEM SET REPLICATION_DDL_ENABLE_LEVEL = 1`, and `ALTER SESSION SET REPLICATION_DDL_SYNC = 1`; remote `ALTER SYSTEM SET REPLICATION_DDL_ENABLE = 1`, `ALTER SYSTEM SET REPLICATION_DDL_ENABLE_LEVEL = 1`, `ALTER SYSTEM SET REPLICATION_DDL_SYNC = 1`, and `ALTER SYSTEM SET REPLICATION_SQL_APPLY_ENABLE = 1`; then matching resets after completion. | Replace the SQL apply DDL synchronization example with the full local and remote property sequence from the source manual. Add `REPLICATION_DDL_SYNC` to the property list. Include the reset sequence for all changed properties, and keep the local `ALTER SESSION` versus remote `ALTER SYSTEM` distinction explicit. |
| Medium | `GPTs/attachments/02_administration_operations.md` | 990 | The drop tablespace runbook says `AND DATAFILES` removes disk data files or memory checkpoint image files, but it does not warn that `AND DATAFILES` cannot be used when dropping a volatile tablespace. The nearby generic examples can be copied into a volatile-tablespace answer and produce invalid SQL. | Add type-specific drop rules and examples: disk and memory drops may use `INCLUDING CONTENTS AND DATAFILES`; volatile drops must omit `AND DATAFILES`; temporary/system tablespace caveats should remain separate. |
| Medium | `GPTs/attachments/02_administration_operations.md` | 665 | The tablespace drop syntax omits 8.1 `DROP TABLESPACE IF EXISTS`, while `03_sql_ddl_generation.md` only provides a broad version note that 8.1 supports `IF EXISTS` in supported `DROP` statements. For this stage, tablespace drop syntax should be directly version-aware. | Add `[IF EXISTS]` to the 8.1-only `DROP TABLESPACE` syntax and examples, and state that 7.1 and 7.3 must omit it and use metadata pre-checks for idempotent scripts. |
| Low | `GPTs/attachments/02_administration_operations.md` | 755 | The preflight note groups memory and volatile tablespaces together and tells the user to choose `SIZE`, `NEXT`, and `SPLIT EACH` values. `SPLIT EACH` applies to memory checkpoint image splitting, not volatile tablespaces. | Split the note: memory tablespaces should size `SIZE`, `AUTOEXTEND NEXT`, and `SPLIT EACH`; volatile tablespaces should size only `SIZE` and `AUTOEXTEND NEXT` against the same allocation-unit rule. |
| Low | `GPTs/attachments/03_sql_ddl_generation.md` | 1072 | User creation examples use lowercase placeholder passwords without noting Altibase's default password uppercasing behavior. The source SQL Reference says lowercase passwords are converted to uppercase by default unless `CASE_SENSITIVE_PASSWORD = 1` and the password is quoted. This can surprise users testing generated `CREATE USER` SQL. | Add a short note near `CREATE USER` examples: unquoted lowercase passwords are uppercased by default; for case-sensitive passwords, confirm `CASE_SENSITIVE_PASSWORD = 1` and quote the password. |

## Source Checks

- Claims checked:
  - `CREATE DISK DATA TABLESPACE`, `CREATE MEMORY DATA TABLESPACE`, `CREATE VOLATILE DATA TABLESPACE`, and `CREATE TEMPORARY TABLESPACE` examples and their 8.1 `IF NOT EXISTS` version gating.
  - `DROP TABLESPACE`, `INCLUDING CONTENTS`, `AND DATAFILES`, `CASCADE CONSTRAINTS`, and 8.1 `IF EXISTS` behavior.
  - Memory checkpoint path and `SPLIT EACH` behavior, including the fact that volatile tablespaces do not support checkpoint path splitting.
  - User DDL, default/temporary tablespace assignment, tablespace `ACCESS`, password notes, system privileges, object privileges, and role reconnect behavior.
  - `CREATE REPLICATION`, `ALTER REPLICATION`, multi-IP host syntax, SSL replication syntax, replication metadata queries, and DDL synchronization properties.
  - Verification query targets including `V$TABLESPACES`, `V$DATAFILES`, `V$MEM_TABLESPACES`, `V$VOL_TABLESPACES`, `V$MEM_TABLESPACE_CHECKPOINT_PATHS`, `SYSTEM_.SYS_REPLICATIONS_`, `SYSTEM_.SYS_REPL_HOSTS_`, and `V$REPGAP`.
- Source coverage:
  - 7.1 and 7.3 SQL Reference manuals were sampled for compatibility and absence of 8.1-only `IF NOT EXISTS` and `IF EXISTS` clauses.
  - 8.1 verified source SQL Reference was sampled for 8.1 idempotent DDL clauses, `DROP TABLESPACE IF EXISTS`, user DDL, and replication DDL.
  - Administrator's Manual sections were sampled for memory/volatile storage behavior and tablespace operation rules.
  - Replication Manual sections were sampled for SQL apply mode, DDL synchronization, and required replication properties.
- Source gaps:
  - No SQL was executed against a live Altibase server.
  - 8.1 checks rely on the project-defined Altibase trunk source policy, not a separate installed 8.1 server.
  - The review sampled source sections relevant to this stage; it did not perform a full manual-to-attachment diff.

## Oracle-Overlap Decision

- Correctly compressed:
  - Generic DML is mostly absent from the reviewed sections, and the DDL material emphasizes Altibase-specific storage, user access, dictionary verification, and replication behavior.
- Too much generic Oracle material:
  - None significant in this stage.
- Missing Altibase-specific difference:
  - Volatile tablespace drop behavior with `AND DATAFILES`.
  - Altibase password uppercasing behavior in `CREATE USER`.
  - Direct 8.1 tablespace `DROP ... IF EXISTS` syntax in the tablespace operation section.

## Version Checks

- 7.1:
  - The reviewed create examples generally avoid 8.1-only `IF NOT EXISTS` for 7.1. Tablespace drop idempotency should continue to use metadata pre-checks rather than `IF EXISTS`.
- 7.3:
  - The reviewed create examples generally avoid 8.1-only `IF NOT EXISTS` for 7.3. The DDL synchronization issue also applies to 7.3 because the 7.3 Replication Manual includes the same required property family.
- 8.1:
  - `IF NOT EXISTS` for tablespace creation, user creation, and replication creation is represented.
  - `DROP TABLESPACE IF EXISTS` is supported in the 8.1 verified source but not represented directly in the tablespace drop syntax or examples.
  - SSL replication syntax is represented, but DDL synchronization with SQL apply mode is missing required property steps.

## Retrieval And GPT Answer Quality

- Strengths:
  - The reviewed attachments have strong Altibase-specific headings and examples for memory, disk, volatile, temporary storage, users, privileges, replication creation, and verification queries.
  - The examples usually preserve literal object names, properties, views, and version labels.
  - The SQL generation QA report shows broad prompt coverage, but it also confirms that no SQL was executed against a live Altibase server.
- Risks:
  - The High replication issue could cause the GPT to generate an incomplete operational procedure for DDL synchronization.
  - The volatile tablespace drop gap could produce invalid `DROP TABLESPACE ... AND DATAFILES` SQL.
  - The missing 8.1 `DROP TABLESPACE IF EXISTS` syntax reduces version-aware completeness for tablespace DDL generation.
  - The password case note is small but relevant for examples that users may copy directly.

## Required Follow-Up

- Fix the replication DDL synchronization property sequence in `GPTs/attachments/09_replication_ha_cdc.md` before upload.
- Add volatile-specific `DROP TABLESPACE` guidance and 8.1 `DROP TABLESPACE IF EXISTS` syntax in the relevant tablespace sections of `GPTs/attachments/02_administration_operations.md` and, if appropriate, `GPTs/attachments/03_sql_ddl_generation.md`.
- Correct the memory/volatile preflight wording around `SPLIT EACH`.
- Add a concise `CREATE USER` password case-sensitivity note.
- Re-run targeted `rg` checks and prompt simulations for tablespace drop and replication DDL synchronization after edits.
