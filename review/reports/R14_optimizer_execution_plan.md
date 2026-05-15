# R14 Performance Tuning, Optimizer, and Execution Plans

Date: 2026-05-16
Reviewer: Codex
Verdict: Pass

## Scope

- Attachments:
  - `GPTs/attachments/08_performance_tuning_monitoring.md`
  - `GPTs/attachments/03_sql_ddl_generation.md`
- Supporting reports:
  - `GPTs/reports/sql_generation_test_results.md`
- Source manuals sampled:
  - `Manuals/Altibase_7.1/kor/Performance Tuning Guide.md`
  - `Manuals/Altibase_7.3/kor/Performance Tuning Guide.md`
  - `Manuals/Altibase_trunk/kor/Performance Tuning Guide.md`
  - `Manuals/Altibase_7.1/kor/SQL Reference.md`
  - `Manuals/Altibase_7.3/kor/SQL Reference.md`
  - `Manuals/Altibase_trunk/kor/SQL Reference.md`
  - `Manuals/Altibase_7.1/kor/iSQL User's Manual.md`
  - `Manuals/Altibase_7.3/kor/iSQL User's Manual.md`
  - `Manuals/Altibase_trunk/kor/iSQL User's Manual.md`
  - `Manuals/Altibase_7.1/kor/Administrator's Manual.md`
  - `Manuals/Altibase_7.3/kor/Administrator's Manual.md`
  - `Manuals/Altibase_trunk/kor/Administrator's Manual.md`
  - `Manuals/Altibase_7.1/kor/General Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md`
  - `Manuals/Altibase_7.1/kor/Stored Procedures Manual.md`
  - `Manuals/Altibase_7.3/kor/Stored Procedures Manual.md`
  - `Manuals/Altibase_trunk/kor/Stored Procedures Manual.md`
  - `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`

## Commands Run

```bash
bash review/scripts/run_review_remediation_cycle.sh status
rg -n $'\t(Reviewing|Remediating|ReReviewing|Fail)$' review/review_remediation_cycle_status.tsv
git status --short
git diff --stat
git diff -- GPTs/attachments/08_performance_tuning_monitoring.md
git diff -- review/review_remediation_cycle_status.tsv review/review_stage_status.tsv
test -f review/reports/R14_optimizer_execution_plan.md && nl -ba review/reports/R14_optimizer_execution_plan.md || true
sed -n '1,260p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,240p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,300p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,240p' GPTs/attachments/README.md
rg -n "optimizer|Optimizer|optimization|execution plan|Execution Plan|plan|PLAN|index|Index|INDEX|hint|HINT|statistics|JSON|EXPLAIN|SET AUTOTRACE|AUTOTRACE|iSQL|JOIN|join|TRCLOG|PLAN_CACHE|RESULT_CACHE" GPTs/attachments/08_performance_tuning_monitoring.md GPTs/attachments/03_sql_ddl_generation.md
rg -n "optimizer|Optimizer|execution plan|Execution Plan|plan|PLAN|index|Index|INDEX|hint|HINT|statistics|JSON|EXPLAIN|SET AUTOTRACE|AUTOTRACE|iSQL|JOIN|join|TRCLOG|PLAN_CACHE|RESULT_CACHE" GPTs/reports/sql_generation_test_results.md
wc -l GPTs/attachments/08_performance_tuning_monitoring.md GPTs/attachments/03_sql_ddl_generation.md GPTs/reports/sql_generation_test_results.md Manuals/Altibase_7.1/kor/Performance\ Tuning\ Guide.md Manuals/Altibase_7.3/kor/Performance\ Tuning\ Guide.md Manuals/Altibase_trunk/kor/Performance\ Tuning\ Guide.md Manuals/Altibase_7.1/kor/SQL\ Reference.md Manuals/Altibase_7.3/kor/SQL\ Reference.md Manuals/Altibase_trunk/kor/SQL\ Reference.md
rg -n "^#{1,4} " GPTs/attachments/08_performance_tuning_monitoring.md
rg -n "^#{1,4} " GPTs/attachments/03_sql_ddl_generation.md
rg -n "^#{1,4} " Manuals/Altibase_trunk/kor/Performance\ Tuning\ Guide.md
rg -n "^#{1,4} " Manuals/Altibase_trunk/kor/SQL\ Reference.md | rg -n "INDEX|CREATE INDEX|DROP INDEX|ALTER INDEX|JSON|힌트|Hint|PLAN|EXPLAIN"
nl -ba GPTs/attachments/08_performance_tuning_monitoring.md | sed -n '193,380p'
nl -ba GPTs/attachments/08_performance_tuning_monitoring.md | sed -n '863,1045p'
nl -ba GPTs/attachments/08_performance_tuning_monitoring.md | sed -n '1046,1305p'
nl -ba GPTs/attachments/08_performance_tuning_monitoring.md | sed -n '1306,1670p'
nl -ba GPTs/attachments/08_performance_tuning_monitoring.md | sed -n '1670,1812p'
nl -ba GPTs/attachments/08_performance_tuning_monitoring.md | sed -n '2226,2326p'
nl -ba GPTs/attachments/03_sql_ddl_generation.md | sed -n '433,493p'
nl -ba GPTs/attachments/03_sql_ddl_generation.md | sed -n '1674,1840p'
nl -ba GPTs/reports/sql_generation_test_results.md | sed -n '1,80p'
nl -ba GPTs/reports/sql_generation_test_results.md | sed -n '190,286p'
nl -ba GPTs/reports/sql_generation_test_results.md | sed -n '315,333p'
nl -ba Manuals/Altibase_trunk/kor/Performance\ Tuning\ Guide.md | sed -n '546,610p'
nl -ba Manuals/Altibase_trunk/kor/Performance\ Tuning\ Guide.md | sed -n '624,790p'
nl -ba Manuals/Altibase_trunk/kor/Performance\ Tuning\ Guide.md | sed -n '990,1045p'
nl -ba Manuals/Altibase_trunk/kor/Performance\ Tuning\ Guide.md | sed -n '1365,1555p'
nl -ba Manuals/Altibase_trunk/kor/Performance\ Tuning\ Guide.md | sed -n '2300,2765p'
nl -ba Manuals/Altibase_trunk/kor/Performance\ Tuning\ Guide.md | sed -n '3108,3335p'
nl -ba Manuals/Altibase_trunk/kor/Performance\ Tuning\ Guide.md | sed -n '5481,5910p'
nl -ba Manuals/Altibase_trunk/kor/iSQL\ User\'s\ Manual.md | sed -n '2762,2864p'
nl -ba Manuals/Altibase_trunk/kor/SQL\ Reference.md | sed -n '2795,2865p'
nl -ba Manuals/Altibase_trunk/kor/SQL\ Reference.md | sed -n '5894,6065p'
nl -ba Manuals/Altibase_trunk/kor/SQL\ Reference.md | sed -n '6066,6275p'
nl -ba Manuals/Altibase_trunk/kor/SQL\ Reference.md | sed -n '10398,10465p'
nl -ba ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md | sed -n '200,225p'
nl -ba ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md | sed -n '300,316p'
rg -n "SELECT, INSERT, UPDATE, DELETE 등의 SQL DML문|INSERT문의 경우|DELETE 문, UPDATE 문, 및 MOVE 문" Manuals/Altibase_7.1/kor/Performance\ Tuning\ Guide.md Manuals/Altibase_7.3/kor/Performance\ Tuning\ Guide.md Manuals/Altibase_trunk/kor/Performance\ Tuning\ Guide.md
rg -n "SQL.*실행 계획은 SELECT, INSERT, UPDATE, DELETE|ALTER SESSION SET EXPLAIN PLAN|ONLY인 경우 질의 실행 없이|TRCLOG_DETAIL_PREDICATE" Manuals/Altibase_7.1/kor/iSQL\ User\'s\ Manual.md Manuals/Altibase_7.3/kor/iSQL\ User\'s\ Manual.md Manuals/Altibase_trunk/kor/iSQL\ User\'s\ Manual.md
rg -n "JSON.*실행 계획|TRCLOG_EXPLAIN_TYPE|TRCLOG_JSON_PLAN_INDENT_DEPTH|JSON.*plan|execution plan" ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md Manuals/Altibase_trunk/kor/Performance\ Tuning\ Guide.md Manuals/Altibase_trunk/kor/SQL\ Reference.md
rg -n "DBMS_SQL_PLAN_CACHE|KEEP_PLAN\(|UNKEEP_PLAN|PLAN_CACHE_KEEP|SQL_PLAN_CACHE_SQLTEXT|SQL_PLAN_CACHE_PCO" Manuals/Altibase_7.1/kor Manuals/Altibase_7.3/kor Manuals/Altibase_trunk/kor | head -n 80
rg -n "IF NOT EXISTS|IF EXISTS" Manuals/Altibase_7.1/kor/SQL\ Reference.md Manuals/Altibase_7.3/kor/SQL\ Reference.md Manuals/Altibase_trunk/kor/SQL\ Reference.md
rg -n "LOCALUNIQUE|글로벌 파티션드 인덱스|논파티션드 인덱스|메모리.*인덱스|GLOBAL.*인덱스|파티션드 메모리" Manuals/Altibase_7.1/kor/SQL\ Reference.md Manuals/Altibase_7.3/kor/SQL\ Reference.md Manuals/Altibase_trunk/kor/SQL\ Reference.md
rg -n "QUERY_REWRITE_ENABLE|DETERMINISTIC|LOB 데이터를 사용할 수 없다|부질의\(subquery\)|시퀀스|의사 칼럼|Direct Key|디스크 인덱스에는 Direct Key" Manuals/Altibase_7.1/kor/SQL\ Reference.md Manuals/Altibase_7.3/kor/SQL\ Reference.md Manuals/Altibase_trunk/kor/SQL\ Reference.md
rg -n "NOLOGGING|PARALLEL integer|INDEX_BUILD_THREAD_COUNT|AGING|REORGANIZATION|is_consistent|V\$DISK_BTREE_HEADER" Manuals/Altibase_7.1/kor/SQL\ Reference.md Manuals/Altibase_7.3/kor/SQL\ Reference.md Manuals/Altibase_trunk/kor/SQL\ Reference.md Manuals/Altibase_7.1/kor/General\ Reference-2.The\ Data\ Dictionary.md Manuals/Altibase_7.3/kor/General_Reference-2.The\ Data\ Dictionary.md Manuals/Altibase_trunk/kor/General_Reference-2.The\ Data\ Dictionary.md
rg -n "글로벌|global|Global|GLOBAL|논파티션드|파티션드 인덱스|메모리.*파티션드" Manuals/Altibase_trunk/kor/SQL\ Reference.md | head -n 120
rg -n "global partitioned|global non-partitioned|Global partitioned|GLOBAL PARTITION|global.*index|global.*Index|글로벌 파티션드 인덱스|글로벌.*인덱스" Manuals GPTs/reports review/reports | head -n 200
rg -n "글로벌|GLOBAL|global|non-partitioned|논파티션드|로컬 인덱스|LOCAL" Manuals/Altibase_trunk/kor/Administrator\'s\ Manual.md Manuals/Altibase_7.3/kor/Administrator\'s\ Manual.md Manuals/Altibase_7.1/kor/Administrator\'s\ Manual.md
rg -n "trunk|C:/|file://|Altibase_trunk" GPTs/attachments/08_performance_tuning_monitoring.md GPTs/attachments/03_sql_ddl_generation.md
git diff --check
bash review/scripts/run_review_stage.sh validate
rg -n "^Verdict:|^\| (Blocker|High|Medium|Low) \|" review/reports/R14_optimizer_execution_plan.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' | wc -l
git status --short
git diff --name-only
rg -n "^# R14|^Verdict:|No actionable|^\| (Blocker|High|Medium|Low) \||^## Required Follow-Up|No R14 remediation" review/reports/R14_optimizer_execution_plan.md
wc -l review/reports/R14_optimizer_execution_plan.md
```

## Findings

No actionable `Blocker`, `High`, `Medium`, or `Low` findings remain in the R14 scope.

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Note | `GPTs/attachments/08_performance_tuning_monitoring.md` | 297 | The prior R14 `EXPLAIN PLAN` DML-scope issue is resolved in the current worktree. The attachment now states that iSQL plan checking covers `SELECT`, `INSERT`, `UPDATE`, and `DELETE`, that `DELETE`/`UPDATE`/`MOVE` use the same optimization process as `SELECT`, and that `INSERT` visibility is limited to the `SELECT` part of `INSERT INTO SELECT`. This matches the sampled Korean Performance Tuning Guide and iSQL User's Manual wording. | No further R14 remediation is required. Keep the option-block wording below it scoped to the source examples for `SELECT`, `ON`, `ONLY`, runtime `ACCESS`, and `??`. |

## Source Checks

- Claims checked:
  - Query processing order: parsing, validation, optimization, binding, execution.
  - Optimizer components: `Query Rewriter`, `Logical Plan Generator`, `Physical Plan Generator`.
  - Memory-table and disk-table tuning differences, including CPU-vs-disk cost priority, buffer effects, one-pass/two-pass join behavior, and disk-table index selectivity caution.
  - `EXPLAIN PLAN = ON | ONLY | OFF`, DML plan-check scope, `TRCLOG_DETAIL_PREDICATE`, plan indentation, `ACCESS`, `COST`, `DISK_PAGE_COUNT`, and `TID` semantics.
  - Access methods: `FULL SCAN`, `INDEX RANGE SCAN`, `INDEX FULL SCAN`, filter/key-range behavior, composite-index ordering, and data-type conversion impact on index use.
  - Join-order, join-method, join-symbol, plan-node, statistics, hint, SQL Plan Cache, plan pinning, and Result Cache terminology.
  - Index DDL/tuning bridge in `03_sql_ddl_generation.md`: local/global index boundary, function-based index restrictions, `QUERY_REWRITE_ENABLE`, direct key limitations, `NOLOGGING`, `PARALLEL`, and 8.1-only `IF NOT EXISTS`/`IF EXISTS` index syntax.
  - 8.1 JSON-format execution-plan claim and property-name boundary.
- Source coverage:
  - Korean Performance Tuning Guides across 7.1, 7.3, and the 8.1 source set support the shared optimizer process, access methods, DML plan-checking nuance, plan-tree interpretation, join methods, statistics, hints, SQL Plan Cache, and Result Cache guidance sampled.
  - Korean iSQL User's Manuals across 7.1, 7.3, and the 8.1 source set support the `ALTER SESSION SET EXPLAIN PLAN` command, DML plan-checking scope, `ON`/`ONLY`/`OFF`, `TRCLOG_DETAIL_PREDICATE`, and `ACCESS: ??` behavior for `ONLY`.
  - Korean SQL Reference manuals support the index syntax and restrictions sampled for `CREATE INDEX`, `ALTER INDEX`, `DROP INDEX`, function-based indexes, direct key indexes, `NOLOGGING`, `PARALLEL`, and 8.1-only index idempotency.
  - Korean Administrator manuals support the index-family boundary used by both attachments: local partitioned indexes and global non-partitioned indexes are supported, global partitioned indexes are not, and partitioned memory tables cannot use global non-partitioned indexes.
  - Korean General Reference and Stored Procedures manuals support the sampled SQL plan cache and plan-pinning verification points, including `V$SQL_PLAN_CACHE_PCO`, `V$SQL_PLAN_CACHE_SQLTEXT`, `PLAN_CACHE_KEEP`, `DBMS_SQL_PLAN_CACHE.KEEP_PLAN(sql_text_id)`, and `DBMS_SQL_PLAN_CACHE.UNKEEP_PLAN(sql_text_id)`.
  - The 8.1 Korean release notes confirm JSON-format execution-plan support and list `TRCLOG_EXPLAIN_TYPE` and `TRCLOG_JSON_PLAN_INDENT_DEPTH`. The attachment correctly avoids inventing JSON field names, property values, or example output.
- Korean/English source conflicts:
  - No English manual was used as the technical basis. Korean manuals and Korean 8.1 release notes were checked first.
  - One Korean SQL Reference function-based-index restriction still mentions "global partitioned indexes"; Korean Administrator manuals across the sampled versions explicitly state that Altibase supports only local and global non-partitioned indexes and does not support global partitioned indexes. The attachment follows the Administrator-manual support boundary, so no attachment issue remains.
- Source gaps:
  - No verified source sampled here provides JSON execution-plan field schema, property value enumerations, or example JSON output; the attachment correctly keeps that material out of scope.
  - No live Altibase server was available, so plan examples and generated SQL were checked against manuals and prior SQL-generation QA rather than runtime execution.

## Oracle-Overlap Decision

- Correctly compressed:
  - Generic Oracle-like SQL is not expanded into a SQL tutorial.
  - The scoped sections prioritize Altibase-specific optimizer process, plan trees, access methods, hints, statistics, memory/disk storage effects, SQL plan cache, Result Cache, index DDL boundaries, and operational retest workflow.
- Too much generic Oracle material:
  - None found in the sampled optimizer/index/plan sections.
- Missing Altibase-specific difference:
  - None actionable remains. The important `EXPLAIN PLAN` DML nuance is now visible in the attachment.

## Version Checks

- 7.1:
  - Korean 7.1 Performance Tuning Guide, iSQL User's Manual, SQL Reference, Administrator's Manual, General Reference, and Stored Procedures Manual support the shared optimizer, plan-tree, index, statistics, hint, and plan-cache guidance sampled.
  - 8.1-only syntax/features such as index `IF NOT EXISTS`, index `IF EXISTS`, native `JSON`, and JSON-format plan output are not applied to 7.1 in the scoped optimizer/index material.
- 7.3:
  - Korean 7.3 manuals remain consistent with the shared optimizer, DML plan-checking, index, hint, statistics, and SQL plan-cache guidance sampled.
  - 8.1-only syntax/features are not leaked into 7.3 guidance in the scoped material.
- 8.1:
  - `Altibase 8.1 verified source` wording is used in the attachment.
  - JSON-format execution-plan guidance is constrained to release-note-confirmed existence and property names only.

## Retrieval And GPT Answer Quality

- Strengths:
  - `08_performance_tuning_monitoring.md` has strong retrieval anchors for slow SQL workflow, optimizer model, `EXPLAIN PLAN`, access methods, index tuning, join methods, plan nodes, statistics, hints, SQL Plan Cache, Result Cache, and answer patterns.
  - `03_sql_ddl_generation.md` gives the GPT a source-backed bridge from tuning recommendations to index DDL, metadata checks, property checks, and version-scoped syntax.
  - The response rules and residual scope notes discourage unsupported index, hint, property, or JSON-plan recommendations without target-server evidence.
- Risks:
  - JSON execution-plan retrieval is intentionally sparse; future remediation should not add field names or example JSON unless a verified source is added.
  - Plan-node and hint lists are compact, not exhaustive. The attachment tells the GPT to verify target SQL, plan, metrics, and installed-version behavior before recommending production changes.
  - Runtime behavior can still vary by exact patch, schema state, object statistics, bind types, privileges, tablespace state, and workload; the stage did not execute SQL against a live server.

## Required Follow-Up

- No R14 remediation is required before moving to the next stage.
- Keep the current DML-scope `EXPLAIN PLAN` note, narrow 8.1 JSON-plan wording, and target-server verification cautions during later cleanup.
