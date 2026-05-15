# R16 Replication topology, states, restrictions, and compatibility checks

Date: 2026-05-16
Reviewer: Codex
Verdict: Pass

## Scope

- Attachments:
  - `GPTs/attachments/09_replication_ha_cdc.md`
  - `GPTs/attachments/03_sql_ddl_generation.md`
  - `GPTs/attachments/06_data_dictionary_performance_views.md`
- Supporting reports:
  - `GPTs/reports/source_inventory.md`
  - `GPTs/reports/8_1_verification.md`
  - `GPTs/reports/eng_kor_parity.md`
  - `GPTs/reports/version_coverage_validation.md`
  - `review/reports/R04_replication_ddl.md`
- Source manuals sampled:
  - `Manuals/Altibase_7.1/kor/Replication Manual.md`
  - `Manuals/Altibase_7.3/kor/Replication Manual.md`
  - `Manuals/Altibase_trunk/kor/Replication Manual.md`
  - `Manuals/Altibase_7.1/kor/SQL Reference.md`
  - `Manuals/Altibase_7.1/kor/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`
  - `PatchNotes/Altibase_7.1/kor/Altibase_7_1_0_8_5_Patch_Notes.md`
  - `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`
  - `Technical Documents/kor/ReplicationCompatibility.md`

## Commands Run

```bash
bash review/scripts/run_review_remediation_cycle.sh status
rg -n $'\t(Reviewing|Remediating|ReReviewing|Fail)$' review/review_remediation_cycle_status.tsv
git status --short
git diff -- GPTs/attachments/09_replication_ha_cdc.md GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/06_data_dictionary_performance_views.md GPTs/reports/source_inventory.md review/review_remediation_cycle_status.tsv review/review_stage_status.tsv
sed -n '1,240p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,220p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,260p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
rg -n "^#|^##|^###|^Mode block|^Option block|^Operation block|^Compatibility block|^Health query block|^Template:" GPTs/attachments/09_replication_ha_cdc.md
rg -n "Replication|CREATE REPLICATION|ALTER REPLICATION|DROP REPLICATION|SYS_REPL|V\$REP|V\$REPSYNC|RECEIVE_ONLY|replication" GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/06_data_dictionary_performance_views.md
rg -n "RECEIVE_ONLY|DROP HOST ALL|SET RECEIVE_ONLY|V\$REPSYNC|SYNC ONLY|V\$REPRECEIVER_COLUMN|REPLICATION_SQL_APPLY_ENABLE|encrypted|8\.1-to-older|protocol prefix|EAGER mode is not recommended for three|three or more nodes|USING SSL|REPLICATION_SSL_PORT_NO" GPTs/attachments/09_replication_ha_cdc.md GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/06_data_dictionary_performance_views.md
rg -n "trunk|file://|C:/|Manuals/|PatchNotes/|ReleaseNotes/|Technical Documents/" GPTs/attachments/09_replication_ha_cdc.md GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/06_data_dictionary_performance_views.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name README.md | sort | wc -l
git diff --check -- GPTs/attachments/09_replication_ha_cdc.md GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/06_data_dictionary_performance_views.md review/reports/R16_replication_topology_state.md
```

## Findings

No actionable `Blocker`, `High`, `Medium`, or `Low` findings remain for this stage.

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Note | `GPTs/attachments/06_data_dictionary_performance_views.md` | 85 | The top-level Fast Object Map's `Replication runtime` row does not list `V$REPSYNC`, although the detailed cookbook and object block now include `V$REPSYNC` at lines 1391 and 2108. This is not blocking because the required synchronization-progress query is present and source-backed. | Optional retrieval polish: add `V$REPSYNC` to the Fast Object Map row during a later cleanup pass. No R16 remediation is required. |

## Source Checks

- Claims checked:
  - Replication topology and state guidance for `CREATE REPLICATION`, `SYNC`, `SYNC ONLY`, `START`, `QUICKSTART`, `STOP`, `RESET`, `DROP REPLICATION`, `FLUSH`, multi-IP host lists, LAZY/EAGER modes, receive-only replication, and failover validation.
  - Restrictions for primary keys, primary-key updates, table-to-table versus partition-to-partition mapping, EAGER mode, DDL execution and DDL replication, SQL apply mode, encrypted columns, receive-only operation, offline replication, and propagation roles.
  - Compatibility matrices and protocol guidance for 7.1 and 7.3 LAZY replication, plus the explicit 8.1 compatibility source boundary.
  - Verification queries for `SYSTEM_.SYS_REPLICATIONS_`, `SYSTEM_.SYS_REPL_HOSTS_`, `SYSTEM_.SYS_REPL_ITEMS_`, `V$REPGAP`, `V$REPGAP_PARALLEL`, `V$REPSYNC`, `V$REPSENDER`, `V$REPRECEIVER`, and `V$REPRECEIVER_COLUMN`.
- Source coverage:
  - Korean replication manuals support the state, mode, DDL, SQL apply, offline, multi-IP, propagation, and receive-only restrictions now present in `09_replication_ha_cdc.md`.
  - Korean General Reference sources support the sampled replication metadata and runtime queries, including the corrected `V$REPRECEIVER_COLUMN` layout and `V$REPSYNC`.
  - `Technical Documents/kor/ReplicationCompatibility.md` supports the 7.1 and 7.3 LAZY compatibility blocks and protocol-version table.
  - Korean 8.1 release notes and the 8.1 verified source support `USING SSL` and `REPLICATION_SSL_PORT_NO` as replication SSL transport features, not generic HA compatibility guarantees.
  - 7.1 SQL Reference plus the 7.1.0.8.5 patch note support treating `RECEIVE_ONLY` as patch-level 7.1 material.
- Korean/English source conflicts:
  - No English-over-Korean drift was found in the sampled R16 scope.
- Source gaps:
  - No selected source provides an 8.1-to-older replication compatibility matrix; the attachment correctly requires an 8.1 matrix or vendor confirmation before declaring cross-version 8.1 compatibility.
  - The sampled 7.1 General Reference options list does not show `512` for receive-only, while 7.1 SQL Reference and the 7.1.0.8.5 patch note document `RECEIVE_ONLY`; the attachment correctly makes 7.1 receive-only answers patch/meta-version-sensitive.

## Oracle-Overlap Decision

- Correctly compressed:
  - Replication remains Altibase-specific and is not described through Oracle replication assumptions.
- Too much generic Oracle material:
  - None found in the scoped replication topology, state, DDL restriction, compatibility, or verification-query content.
- Missing Altibase-specific difference:
  - None actionable. Receive-only replication, `SYNC ONLY`, `V$REPSYNC`, EAGER restrictions, DDL synchronization boundaries, SQL apply restrictions, and 8.1 replication SSL separation are now represented.

## Version Checks

- 7.1:
  - Core ordinary replication syntax, state behavior, `SYNC ONLY`, EAGER restrictions, DDL guidance, and runtime checks are source-backed.
  - `RECEIVE_ONLY` is correctly framed as 7.1.0.8.5 patch-level material that requires exact patch/meta-version confirmation.
- 7.3:
  - Korean 7.3 sources support `RECEIVE_ONLY`, DDL synchronization, LAZY compatibility rows, protocol `7.4.9`, and the replication metadata/runtime queries sampled.
- 8.1:
  - The 8.1 verified source supports the same sampled topology/state details plus replication SSL through `USING SSL` and `REPLICATION_SSL_PORT_NO`.
  - The attachment correctly avoids claiming 8.1-to-older replication compatibility without an 8.1 compatibility matrix or vendor confirmation.

## Retrieval And GPT Answer Quality

- Strengths:
  - `09_replication_ha_cdc.md` is organized around operational decision blocks, state diagrams, option blocks, compatibility guidance, and health queries.
  - `03_sql_ddl_generation.md` keeps replication SQL Altibase-specific, separates ordinary TCP from 8.1 SSL examples, and routes detailed operational behavior to `09_replication_ha_cdc.md`.
  - `06_data_dictionary_performance_views.md` now includes receive-only option decoding and `V$REPSYNC` synchronization-progress checks.
- Risks:
  - The Fast Object Map in `06_data_dictionary_performance_views.md` is less complete than the detailed replication sections for `V$REPSYNC`, but the detailed query and cross-reference coverage are sufficient for R16 pass.
  - 8.1 cross-version replication compatibility remains an accepted source gap, not an attachment defect, because no selected compatibility matrix covers it.

## Required Follow-Up

- No required R16 follow-up.
- Optional cleanup: add `V$REPSYNC` to the `Replication runtime` row in the Fast Object Map of `GPTs/attachments/06_data_dictionary_performance_views.md`.
