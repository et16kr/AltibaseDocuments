# J011 Installation Administration and Tablespace Runbook Design Note

Date: 2026-05-17

## Scope

J011 strengthens customer-facing runbook content in:

- `GPTs/attachments/01_getting_started_installation.md`
- `GPTs/attachments/02_administration_operations.md`
- `GPTs/attachments/13_isql_iloader_basic_tools.md`

The job does not change original manuals, benchmark thresholds, question wording, or
unsupported Altibase behavior.

## Design

The main structure change is a pair of compact answer-anchor sections near the top of
the installation and administration attachments. Existing detailed runbooks remain in
place; the anchors are retrieval and synthesis aids for exact operational tokens that
were easy to omit in answers.

`01_getting_started_installation.md` now anchors the post-install sequence,
startup/shutdown phases, creation-time path properties, 7.3 platform boundaries,
client-only environment handling, and APatch rollback/meta-downgrade checks.

`02_administration_operations.md` now anchors built-in accounts, `CREATE USER`,
system tablespaces, tablespace states, memory checkpoint paths, destructive
tablespace DDL, undo pressure, verification views, datafile recovery, log anchors,
backup completion markers, and protected administration stop points.

`13_isql_iloader_basic_tools.md` adds a concise iLoader table-level backup anchor
with `t1.fmt` and `t1.dat` so logical backup answers do not blur iLoader with
physical database backup.

## Source Basis

The edited facts were checked against repository-local selected sources, especially:

- Altibase 7.1 and 7.3 Korean Installation Guides for `post_install.sh dbcreate`,
  `server create`, `catproc.sql`, client environment variables, supported-platform
  notes, pre-install Linux checks, APatch rollback files, and `server downgrade`.
- Altibase 7.1, 7.3, and Altibase 8.1 verified source Administrator's Manuals for
  startup phases, shutdown modes, system tablespaces, tablespace state transitions,
  undo tablespace operations, checkpoint paths, log anchors, backup/recovery, and
  datafile recovery behavior.
- Altibase 8.1 verified source SQL Reference for `CREATE USER`, password behavior,
  tablespace assignment, `ACCESS`, automatic grants, and destructive tablespace DDL.
- Altibase iLoader manuals and Administrator's Manual logical-backup examples for
  `formout`, `out`, `in`, FORM files, and table-level backup limits.

## Safety Rules Preserved

- Ask for exact version, patch, startup phase, database mode, paths, object scope,
  backup evidence, and business approval before destructive or recovery operations.
- Keep customer-facing content in English while preserving literal Altibase tokens.
- Prefer current log anchors for ordinary complete media recovery; use historical
  log anchors only when source-backed recovery scenarios require them.
- Do not treat iLoader exports as physical database backups.
