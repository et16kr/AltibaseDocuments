# Korean-Aligned English Baseline: Performance And Source Index Routing

- Job: `S1R-J004`
- Scope: Performance Tuning Guide rows across 7.1, 7.3, and `Altibase 8.1
  verified source` scope, plus source-index rows that blocked Stage 2 routing.
- Source-pack gate: `GPTs/source_pack/source_pack_validation.md` records
  `Status: pass`, `Verdict: Pass`, no blockers, and exact source-pack block
  preservation for the selected Performance Tuning Guide and source-index
  rows.
- Authority rule: Korean manuals are authoritative. English manuals are
  extraction aids. README rows are routing indexes or evidence-only selectors,
  not customer-facing behavior sources. For 8.1 material, preserve the
  established `Altibase 8.1 verified source` boundary.
- Downstream boundary: this file is a working route for guarded first drafts.
  It does not replace exact source-pack extraction, full property conversion,
  complete performance-view column conversion, complete hint syntax
  transcription, plan-node output validation, installed-version checks, or
  customer runtime evidence.

## Design Note

`S1R-J004` adds a dedicated performance and source-index baseline file instead
of rewriting generated S1-J006 inventory rows. The original per-source rows
remain immutable generated evidence, while `KAE-BLOCK-000283` through
`KAE-BLOCK-000285` provide the downstream routes needed by Stage 2:
Performance Tuning Guide working baseline, README/index exact source-pack
routing, and 7.1 Sharding deprecated exact source-pack routing. README and
Sharding routes intentionally record routing disposition only; they do not
promote index text into unsupported customer-facing facts.

## Batch Source Coverage

| Route | Korean source IDs | English source IDs | Baseline manifest rows | Disposition |
| --- | --- | --- | --- | --- |
| Performance Tuning Guide | `SRC-000067`, `SRC-000129`, `SRC-000189` | `SRC-000035`, `SRC-000098`, `SRC-000159` | `KAE-BLOCK-000026`, `KAE-BLOCK-000160`, `KAE-BLOCK-000214`, plus `KAE-BLOCK-000283` | aligned baseline route |
| Manual and tool README indexes | `SRC-000069`, `SRC-000066`, `SRC-000131`, `SRC-000191`, `SRC-000224`, `SRC-000210` | `SRC-000037`, `SRC-000100`, `SRC-000217`, `SRC-000203` | `KAE-BLOCK-000031`, `KAE-BLOCK-000032`, `KAE-BLOCK-000164`, `KAE-BLOCK-000219`, `KAE-BLOCK-000220`, `KAE-BLOCK-000237`, plus `KAE-BLOCK-000284` | exact source-pack route for routing indexes and evidence-only source selectors |
| 7.1 Sharding deprecated source | `SRC-000073` | none selected | `KAE-BLOCK-000033`, plus `KAE-BLOCK-000285` | exact source-pack route; no English working baseline |

## KAE-BLOCK-000283: Performance Tuning Guide Routing

- Source IDs: `SRC-000067`, `SRC-000035`, `SRC-000129`, `SRC-000098`,
  `SRC-000189`, `SRC-000159`.
- Version scope: 7.1, 7.3, and `Altibase 8.1 verified source`.
- Source block refs: `SRC-000067/BLOCK-000812`, `SRC-000035/BLOCK-000811`,
  `SRC-000129/BLOCK-000814`, `SRC-000098/BLOCK-000813`,
  `SRC-000189/BLOCK-000816`, `SRC-000159/BLOCK-000815`.
- Alignment status: baseline generated from paired Korean authority and English
  extraction aids. Exact property values, performance-view columns, hint
  grammar, plan-node formats, statistics procedure details, and runtime tuning
  decisions still require source-pack, target-version, or environment recheck.

Baseline:

1. Route performance-tuning work to the target-version Korean Performance
   Tuning Guide first, using the paired English manual only as an extraction
   aid. Preserve the top-level route through performance tuning introduction,
   Altibase server tuning, query optimizer, explain plan, optimizer and
   statistics, SQL hints, SQL Plan Cache, and Result Cache.
2. For server tuning, route to the manual sections for log files,
   checkpointing, buffers, service threads, garbage collector, SQL Plan Cache,
   and CPU usage. Do not turn this baseline into a production configuration
   prescription without checking the exact property rows in the General
   Reference and the customer's workload evidence.
3. Preserve performance-related property tokens as source routes, including
   `AGER_WAIT_MAXIMUM`, `AGER_WAIT_MINIMUM`,
   `BUFFER_VICTIM_SEARCH_INTERVAL`, `BUFFER_VICTIM_SEARCH_PCT`,
   `BULKIO_PAGE_COUNT_FOR_DIRECT_PATH_INSERT`,
   `CHECKPOINT_BULK_SYNC_PAGE_COUNT`, `CHECKPOINT_BULK_WRITE_PAGE_COUNT`,
   `CHECKPOINT_FLUSH_COUNT`, `DATABASE_IO_TYPE`,
   `DB_FILE_MULTIPAGE_READ_COUNT`, `DEDICATED_THREAD_MODE`,
   `DIRECT_IO_ENABLED`, `EXECUTE_STMT_MEMORY_MAXIMUM`,
   `EXECUTOR_FAST_SIMPLE_QUERY`, `FAST_START_IO_TARGET`,
   `FAST_START_LOGFILE_TARGET`, `HASH_AREA_SIZE`, `LOB_CACHE_THRESHOLD`,
   `LOG_IO_TYPE`, `MAX_THREAD_COUNT`, `NORMALFORM_MAXIMUM`,
   `OPTIMIZER_FEATURE_ENABLE`, `OPTIMIZER_MODE`,
   `OUTER_JOIN_OPERATOR_TRANSFORM_ENABLE`, `PARALLEL_QUERY_THREAD_MAX`,
   `PREPARE_STMT_MEMORY_MAXIMUM`, `QUERY_REWRITE_ENABLE`,
   `SECONDARY_BUFFER_ENABLE`, `SORT_AREA_SIZE`, `SQL_PLAN_CACHE_SIZE`,
   `TABLE_LOCK_ENABLE`, `TIMED_STATISTICS`, `TIMER_RUNNING_LEVEL`,
   `TOTAL_WA_SIZE`, `INIT_TOTAL_WA_SIZE`, and `TRX_UPDATE_MAX_LOGSIZE`.
   Exact defaults, ranges, mutability, and version differences stay in the
   target-version General Reference route.
4. Route performance statistics and monitoring checks through the documented
   performance-view route before drafting SQL. Preserve view tokens such as
   `V$SESSION_EVENT`, `V$SESSION_WAIT`, `V$SESSION_WAIT_CLASS`,
   `V$SYSTEM_EVENT`, `V$SYSTEM_WAIT_CLASS`, `V$BUFFPAGEINFO`,
   `V$BUFFPOOL_STAT`, `V$DBMS_STATS`, `V$FLUSHER`, `V$FLUSHINFO`,
   `V$LATCH`, `V$LOCK_WAIT`, `V$MEMSTAT`, `V$SERVICE_THREAD`,
   `V$SESSTAT`, `V$SYSSTAT`, and `V$UNDO_BUFF_STAT`. Recheck the General
   Reference before generating full column lists or production diagnostics.
5. Route optimizer work through query conversion, logical execution plan
   generation, physical execution plan generation, cost estimation, access
   methods, join order, join method, and optimizer-related properties.
   Preserve conversion names such as Common Subexpression Elimination,
   Constant Filter Precedence, View Merging, Subquery Unnesting, Predicate
   Pushdown, Transitive Predicate Generation, and View Materialization.
6. Route explain-plan work through `ALTER SESSION SET EXPLAIN PLAN = ON`,
   `ONLY`, or `OFF`; `ALTER SYSTEM SET TRCLOG_DETAIL_PREDICATE = 1`; and the
   exact plan-node sections before interpreting output. Preserve plan-node
   tokens such as `AGGREGATION`, `ANTI-OUTER-JOIN`, `BAG-UNION`,
   `CONCATENATION`, `CONNECT BY`, `COUNT`, `DISTINCT`, `FILTER`,
   `FULL-OUTER-JOIN`, `GROUP-AGGREGATION`, `GROUPING`, `HASH`, `JOIN`,
   `LEFT-OUTER-JOIN`, `LIMIT-SORT`, `MATERIALIZATION`, `MERGE-JOIN`,
   `PARALLEL-QUEUE`, `PARALLEL-SCAN-COORDINATOR`,
   `PARTITION-COORDINATOR`, `PROJECT`, `SCAN`, `VIEW`, `VIEW-SCAN`,
   `SET-DIFFERENCE`, `SET-INTERSECT`, `SORT`, and `STORE`. The Korean source
   also exposes `GROUP-CUBE`, `GROUP-ROLLUP`, and `WINDOW SORT` plan-node
   headings; use exact target-version source text before drafting node-level
   explanations.
7. Route statistics work through the optimizer statistics section and
   `DBMS_STATS` stored-procedure route. Preserve statistics groups for table,
   column, index, and database system statistics, and procedure tokens such as
   `GATHER_SYSTEM_STATS`, `GATHER_DATABASE_STATS`, `GATHER_TABLE_STATS`,
   `GATHER_INDEX_STATS`, `SET_SYSTEM_STATS`, `SET_TABLE_STATS`,
   `SET_INDEX_STATS`, `SET_COLUMN_STATS`, `LOCK_TABLE_STATS`, and
   `UNLOCK_TABLE_STATS`. Recheck object definitions and current data-change
   patterns before recommending collection frequency.
8. Route hint work through the SQL Hints chapter and SQL Reference syntax.
   Preserve hint families for optimization strategy, normalization type, join
   order, joining method, intermediate result storage medium, hash bucket
   count, group processing, duplicate removal, view optimization, access
   method, query conversion, plan cache, Direct-Path INSERT, simple query
   execution, parallel query execution, arithmetic precision, and execution
   plan delay. Do not generate a final hinted SQL rewrite without checking
   indexes, statistics, table order, object definitions, and the resulting
   plan.
9. Route SQL Plan Cache work through the dedicated chapter and preserve
   `SQL_PLAN_CACHE_BUCKET_CNT`, `SQL_PLAN_CACHE_HOT_REGION_LRU_RATIO`,
   `SQL_PLAN_CACHE_PREPARED_EXECUTION_CONTEXT_CNT`,
   `SQL_PLAN_CACHE_SIZE`, `V$SQL_PLAN_CACHE_PCO`, and
   `V$SQL_PLAN_CACHE_SQLTEXT`. Preserve the source-backed distinction between
   literal SQL and parameterized SQL when explaining plan reuse.
10. Route Result Cache work through the Result Cache sections. Preserve
    `RESULT_CACHE`, `TOP_RESULT_CACHE`, `RESULT_CACHE_ENABLE`,
    `RESULT_CACHE_MEMORY_MAXIMUM`, and `TOP_RESULT_CACHE_MODE`, and recheck
    exact restrictions before suggesting cache use for functions, temporary
    or fixed tables, DB link remote tables, encrypted columns, LOB columns,
    partitioned disk table temporary-table use, or commit-mode behavior.

Safe first checks:

- Ask for target Altibase version and patch, workload goal, slow SQL text,
  execution plan output, table and index definitions, statistics state, object
  owners, row counts, bind/literal pattern, relevant property values, relevant
  performance-view samples, operating system resource symptoms, and the
  validation window before suggesting a tuning change.
- Compare the current plan and the candidate plan using source-backed explain
  plan routes. For property or hint changes, capture a rollback path and the
  expected validation metric before applying the change.
- For cross-manual details, route exact property values and performance-view
  column definitions to the target-version General Reference, stored
  procedures to the Stored Procedures Manual, and SQL syntax to the SQL
  Reference.

Stop conditions:

- Stop if the request depends on live workload behavior, logs, current object
  definitions, exact patch level, property defaults or ranges, performance-view
  columns, missing plan output, unsupported hint combinations, or customer
  environment details that have not been supplied.
- Stop if the request asks for exhaustive property lists, full plan-node
  formatting, complete hint syntax, all statistics procedure signatures, or
  production-ready tuning actions from this baseline alone. Route to the exact
  source-pack block and the paired target-version manual.
- Stop if a request bases Altibase performance behavior on Oracle patterns,
  generic database assumptions, or an unverified platform rule.

## KAE-BLOCK-000284: README Source-Index Routing

- Source IDs: `SRC-000069`, `SRC-000037`, `SRC-000066`, `SRC-000131`,
  `SRC-000100`, `SRC-000191`, `SRC-000224`, `SRC-000217`, `SRC-000210`,
  `SRC-000203`.
- Version scope: 7.1, 7.3, `Altibase 8.1 verified source`, and multi-version
  tool manuals.
- Source block refs: `SRC-000069/BLOCK-000858`, `SRC-000037/BLOCK-000856`,
  `SRC-000066/BLOCK-000857`, `SRC-000131/BLOCK-000861`,
  `SRC-000100/BLOCK-000860`, `SRC-000191/BLOCK-000862`,
  `SRC-000224/BLOCK-000864`, `SRC-000217/BLOCK-000863`,
  `SRC-000210/BLOCK-000866`, `SRC-000203/BLOCK-000865`.
- Alignment status: exact source-pack routing generated for README/source-index
  rows. These rows are routing indexes or evidence-only source selectors, not
  customer-facing behavioral baselines.

Baseline:

1. Treat manual README rows as routing indexes. They identify selected manual
   families, version trees, language trees, and source paths. They do not
   establish item-level Altibase behavior, syntax, defaults, restrictions, or
   support matrices by themselves.
2. Treat tool README rows as evidence-only source selectors for selected tool
   manuals. Route customer-facing tool behavior to the exact tool manual,
   release-note, technical-document, or AID route selected for the target
   version and tool package.
3. For 7.1 and 7.3 paired README rows, use the Korean README as the
   authoritative index and the English README as an extraction aid. For the
   7.1 Korean PDF README row, keep the route as Korean-only PDF index evidence.
4. For `Altibase 8.1 verified source` README rows, preserve the verified-source
   boundary. The trunk Korean product README and trunk tool README rows route
   to exact source-pack blocks; do not backport trunk index membership to 7.1
   or 7.3 without exact selected-source evidence.
5. If a question asks whether a specific manual, tool manual, or source family
   is selected, this block can route to the exact README source-pack block and
   then to the selected target manual. If a question asks how a feature works,
   skip README text and use the target manual route.

Safe first checks:

- Ask for target Altibase version, language/source preference, manual family,
  tool package, and whether the user needs source selection or behavior.
- Confirm the README row is being used only to choose the next source, not to
  answer behavior, syntax, configuration, or support questions.

Stop conditions:

- Stop if an answer would convert README index membership into an unsupported
  customer-facing fact about feature behavior, defaults, restrictions,
  compatibility, platform support, or production operation.
- Stop if the requested answer depends on a manual body section that has not
  been routed from the README to the exact source-pack block.

## KAE-BLOCK-000285: Sharding Deprecated Exact Source-Pack Routing

- Source IDs: `SRC-000073`.
- Version scope: 7.1 Korean source.
- Source block refs: `SRC-000073/BLOCK-000859`.
- Alignment status: exact source-pack routing generated for the Korean-only
  7.1 Sharding deprecated source. This is not an English working baseline and
  does not authorize unsupported customer-facing Sharding facts.

Baseline:

1. Route any use of `Manuals/Altibase_7.1/kor/Sharding(deprecated).md` to the
   exact source-pack block `SRC-000073/BLOCK-000859`. Preserve its Korean
   authority label and deprecated-source boundary.
2. Use this block as a source selector and stop gate. It records that Stage 2
   has an exact route for the source, not that the selected source has been
   normalized into an answer-ready English baseline.
3. Do not merge this deprecated 7.1 Sharding route into current 7.3 or
   `Altibase 8.1 verified source` behavior without explicit selected-source
   evidence for the target version.
4. Do not generate Sharding configuration, metadata, package, shardLoader,
   Shard Manager, SQL, migration, resharding, or operational instructions from
   this route alone. Use the exact block and a scoped translation/recheck step
   before drafting any customer-facing artifact.

Safe first checks:

- Ask whether the user needs source selection, legacy 7.1 evidence, or a
  customer-facing Sharding procedure.
- For customer-facing work, ask for target version, patch, selected manual
  section, current Sharding topology, object definitions, tool package,
  validation evidence, and rollback requirements before drafting.

Stop conditions:

- Stop if the request would promote a Korean-only deprecated source into
  current customer guidance without an explicit translation, target-version
  check, and exact source-section route.
- Stop if the request depends on live topology, object definitions, package
  state, tool output, logs, compatibility, or migration behavior that the
  customer has not supplied.
