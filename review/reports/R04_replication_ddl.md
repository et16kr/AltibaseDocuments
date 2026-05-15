# R04 DDL generation: replication SQL and replication DDL boundaries

Date: 2026-05-16
Reviewer: Codex
Verdict: Pass

## Scope

- Attachments:
  - `GPTs/attachments/03_sql_ddl_generation.md`
  - `GPTs/attachments/09_replication_ha_cdc.md`
- Supporting reports:
  - `GPTs/reports/sql_generation_test_results.md`
  - `GPTs/reports/source_inventory.md`
- Source manuals sampled:
  - `Manuals/Altibase_7.1/kor/SQL Reference.md`
  - `Manuals/Altibase_7.3/kor/SQL Reference.md`
  - `Manuals/Altibase_trunk/kor/SQL Reference.md`
  - `Manuals/Altibase_7.1/kor/Replication Manual.md`
  - `Manuals/Altibase_7.3/kor/Replication Manual.md`
  - `Manuals/Altibase_trunk/kor/Replication Manual.md`
  - `Manuals/Altibase_7.1/kor/Log Analyzer User's Manual.md`
  - `Manuals/Altibase_7.3/kor/Log Analyzer User's Manual.md`
  - `Manuals/Altibase_trunk/kor/Log Analyzer User's Manual.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`
  - English Replication Manual sequence-replication sections were sampled only as secondary wording checks.

## Commands Run

```bash
bash review/scripts/run_review_remediation_cycle.sh status
rg -n $'\t(Reviewing|Remediating|ReReviewing|Fail)$' review/review_remediation_cycle_status.tsv
git status --short
git diff -- GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/09_replication_ha_cdc.md GPTs/reports/source_inventory.md review/review_remediation_cycle_status.tsv review/review_stage_status.tsv
sed -n '1,260p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,240p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,280p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,240p' GPTs/attachments/README.md
rg -n "replication|REPLICATION|USING SSL|IF EXISTS|IF NOT EXISTS|FOR ANALYSIS|FOR PROPAGATION|DDL synchronization|SYNC TABLE|DROP REPLICATION|CREATE REPLICATION|ALTER REPLICATION" GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/09_replication_ha_cdc.md
nl -ba GPTs/attachments/03_sql_ddl_generation.md | sed -n '540,690p'
nl -ba GPTs/attachments/03_sql_ddl_generation.md | sed -n '1800,1985p'
nl -ba GPTs/attachments/09_replication_ha_cdc.md | sed -n '240,660p'
nl -ba GPTs/attachments/09_replication_ha_cdc.md | sed -n '760,1045p'
nl -ba GPTs/attachments/09_replication_ha_cdc.md | sed -n '1300,1445p'
sed -n '1,460p' GPTs/reports/sql_generation_test_results.md
rg -n "CREATE( LAZY| EAGER)? REPLICATION|DROP REPLICATION|ALTER REPLICATION|IF NOT EXISTS|IF EXISTS|USING SSL|FOR ANALYSIS|FOR PROPAGATION|PROPAGABLE" Manuals/Altibase_*/kor/SQL\ Reference.md
rg -n "REPLICATION_DDL|REPLICATION_SQL_APPLY_ENABLE|DDL|RECEIVE_ONLY|PROPAGATION|RECOVERY|EAGER|ENABLE SYNC TABLE|DISABLE SYNC TABLE|sequence|SYNC TABLE" Manuals/Altibase_*/kor/Replication\ Manual.md
rg -n "XLog Collector|FOR ANALYSIS|WITH UNIX_DOMAIN|UNIX_DOMAIN|SSL|InfiniBand|AT SN" Manuals/Altibase_*/kor/Log\ Analyzer\ User\'s\ Manual.md
nl -ba 'Manuals/Altibase_trunk/kor/SQL Reference.md' | sed -n '3114,3338p'
nl -ba 'Manuals/Altibase_trunk/kor/SQL Reference.md' | sed -n '6796,7005p'
nl -ba 'Manuals/Altibase_trunk/kor/SQL Reference.md' | sed -n '10503,10545p'
nl -ba 'Manuals/Altibase_trunk/kor/Replication Manual.md' | sed -n '1060,1155p'
nl -ba 'Manuals/Altibase_trunk/kor/Replication Manual.md' | sed -n '1937,2018p'
nl -ba 'Manuals/Altibase_trunk/kor/Replication Manual.md' | sed -n '2319,2575p'
nl -ba 'Manuals/Altibase_trunk/kor/Replication Manual.md' | sed -n '3580,3705p'
nl -ba 'Manuals/Altibase_trunk/kor/Replication Manual.md' | sed -n '5290,5335p'
nl -ba "Manuals/Altibase_trunk/kor/Log Analyzer User's Manual.md" | sed -n '1124,1238p'
rg -n "SYS_REPLICATIONS_|SYS_REPL_HOSTS_|SYS_REPL_ITEMS_|V\\$REPSENDER|V\\$REPRECEIVER|V\\$REPGAP|SQL_APPLY_TABLE_COUNT|REPLICATION_SSL_PORT_NO|REPLICATION_PORT_NO" Manuals/Altibase_trunk/kor/General_Reference-*.md
rg -n 'xlog_sender_host|xlog_sender_port|DROP REPLICATION replication_name;|DDL on replication objects with `RECOVERY`|DDL on EAGER-mode' GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/09_replication_ha_cdc.md
rg -n "DROP REPLICATION \\[IF EXISTS\\]|IF EXISTS.*DROP REPLICATION|xlog_collector_host|XLog Collector must already be listening|DISABLE SYNC TABLE|DDL synchronization procedure" GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/09_replication_ha_cdc.md
rg -n "trunk|C:/|file://" GPTs/attachments/03_sql_ddl_generation.md GPTs/attachments/09_replication_ha_cdc.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' | wc -l
git diff --check
bash review/scripts/run_review_stage.sh validate
rg -n "^Verdict:|^\| (Blocker|High|Medium|Low) \|" review/reports/R04_replication_ddl.md
git status --short
```

## Findings

No actionable Blocker, High, Medium, or Low findings remain for this stage.

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Note | `GPTs/attachments/03_sql_ddl_generation.md`; `GPTs/attachments/09_replication_ha_cdc.md` | 597, 637, 841, 1012 | The current scoped attachment edits close the previously reported R04 issues: Log Analyzer TCP syntax now points to the XLog Collector endpoint, `DROP REPLICATION [IF EXISTS]` is marked 8.1-only, DDL synchronization exclusions are explicit, and sequence sync-table teardown removes the replication target before `DISABLE SYNC TABLE`. | No R04 remediation required. Preserve the current version boundaries and Korean-source basis during later replication stages. |

## Source Checks

- Claims checked:
  - `CREATE REPLICATION`, `ALTER REPLICATION`, `DROP REPLICATION`, `CREATE REPLICATION IF NOT EXISTS`, `DROP REPLICATION IF EXISTS`, ordinary TCP endpoints, 8.1 SSL endpoints, InfiniBand endpoints, multi-IP host lists, `AS MASTER` and `AS SLAVE`, `SYNC`, `SYNC ONLY`, `START`, `QUICKSTART`, `RESET`, `ADD TABLE`, `DROP TABLE`, `FLUSH`, XLog Sender `START AT SN`, sequence replication, and replication-target DDL handling.
- Source coverage:
  - Korean SQL Reference sources support the ordinary replication SQL in 7.1 and 7.3, and the 8.1-only additions for `IF NOT EXISTS`, `IF EXISTS`, and `USING SSL`.
  - Korean Replication Manual sources support same-name replication objects, table-to-table and partition-to-partition boundaries, primary-key prerequisites, multi-IP host lists without commas between host pairs, DDL execution properties, DDL synchronization conditions, unsupported DDL synchronization cases, and sequence replication teardown boundaries.
  - Korean Log Analyzer manuals support `CREATE REPLICATION ... FOR ANALYSIS`, the XLog Collector endpoint in TCP examples, `WITH UNIX_DOMAIN`, collector readiness before start, and `START AT SN` for XLog Sender operation.
  - Korean General Reference sources support sampled replication metadata tables, runtime views, `SQL_APPLY_TABLE_COUNT`, `REPLICATION_PORT_NO`, and `REPLICATION_SSL_PORT_NO`.
- Korean/English source conflicts:
  - No attachment-changing Korean/English conflict was found. The English sequence-replication wording mirrors the Korean section's ambiguous parenthetical around excluding the sync table; the report judged the attachment against the Korean context plus the source-backed `ALTER REPLICATION ... DROP TABLE` syntax.
- Source gaps:
  - No R04 blocking source gap found. Later replication stages should still re-check deeper topology, compatibility, CDC API, SSL/TLS, and network-diagnostic details in their dedicated scopes.

## Oracle-Overlap Decision

- Correctly compressed:
  - Ordinary Oracle-overlapping DDL remains secondary. Replication is handled as Altibase-specific SQL, not mapped to Oracle replication syntax.
- Too much generic Oracle material:
  - None found in the scoped replication DDL sections.
- Missing Altibase-specific difference:
  - None actionable for R04. The attachment set now preserves the key Altibase-specific differences for replication DDL boundaries: version-scoped idempotent syntax, peer replication ports, `USING SSL` only for 8.1 verified source, Log Analyzer endpoint semantics, DDL synchronization limits, and sequence sync-table teardown.

## Version Checks

- 7.1:
  - Use ordinary `CREATE REPLICATION`, `ALTER REPLICATION`, and `DROP REPLICATION` syntax without `IF NOT EXISTS`, `IF EXISTS`, or `USING SSL`.
  - Log Analyzer `FOR ANALYSIS`, ordinary TCP or UNIX-domain CDC, sequence replication, multi-IP host lists, and replication-target DDL procedures are represented with Korean-source boundaries.
- 7.3:
  - Same idempotent-syntax and SSL exclusions as 7.1.
  - 7.3 Korean manuals support the ordinary and multi-IP replication SQL patterns sampled in the attachments.
- 8.1:
  - `CREATE REPLICATION IF NOT EXISTS`, `DROP REPLICATION IF EXISTS`, `USING SSL`, and `REPLICATION_SSL_PORT_NO` are represented as Altibase 8.1 verified source guidance.
  - Log Analyzer remains separated from SSL and InfiniBand, matching the Korean source note that Log Analyzer does not support those communication methods.

## Retrieval And GPT Answer Quality

- Strengths:
  - `03_sql_ddl_generation.md` gives a compact SQL-generation block for replication and explicitly routes replication-target DDL, sequence replication, and CDC questions to `09_replication_ha_cdc.md`.
  - `09_replication_ha_cdc.md` now has executable-looking generation patterns for ordinary TCP replication, 8.1 SSL replication, `ALTER REPLICATION` operations, `DROP REPLICATION`, DDL synchronization, sequence replication, and XLog Sender SQL.
  - High-retrieval syntax blocks preserve literal SQL keywords, object names, property names, and version labels.
- Risks:
  - XLog Sender `START AT SN`, offline replication, and DDL synchronization are operationally sensitive. The current text is source-backed, but answer generation should still ask for exact version, topology, mode, replication gap, and service impact before emitting production steps.
  - Sequence replication source wording contains a likely manual typo around "excluding a table from the replication target"; the attachment uses the valid `ALTER REPLICATION ... DROP TABLE` operation and should not be weakened back to the ambiguous parenthetical.

## Required Follow-Up

- None for R04.
- Leave broader replication topology, compatibility, CDC API, replication SSL, and network troubleshooting checks to their later dedicated stages.
