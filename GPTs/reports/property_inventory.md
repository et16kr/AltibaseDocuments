# Altibase GPT Property Inventory

Job: `J004`
Status: Active support artifact
Last updated: 2026-05-16

## Reconfirmed Requirement And Boundary

`J004` inventories property names and version availability from General Reference 1 sources for the supported Altibase 7.1, 7.3, and 8.1 scope. Korean General Reference 1 manuals are the authoritative source for this baseline; matching English General Reference 1 manuals are extraction aids only when they agree with the Korean source.

This is a documentation-scope baseline. It does not attempt to finish every per-property default, range, dynamic-change rule, restart requirement, or example SQL block; those expansions remain split across later property jobs. The target customer attachment `GPTs/attachments/05_data_types_properties.md` now carries a compact property-name availability index so property-name and version-scope questions do not depend only on this internal support report.

## Design Note

The inventory is generated from detailed property headings, not from the summary table alone. The summary tables are useful for category and alter-level orientation, but the detailed headings are more stable for exact property-name inventory because the selected sources include summary-table drift such as a 7.1 `ERVER_MSGLOG_FILE` typo where the detailed heading is `SERVER_MSGLOG_FILE`, summary-table `RESULT_CACHE_MEMORY_MAXIUM` spelling drift where detailed headings use `RESULT_CACHE_MEMORY_MAXIMUM`, and a 7.1 summary-table `PSM_CASE_SENSITIVE` entry where detailed headings use `PSM_CASE_SENSITIVE_MODE`.

Duplicate detailed headings are preserved in the evidence columns. `PARALLEL_QUERY_THREAD_MAX` and `PARALLEL_QUERY_QUEUE_SIZE` appear under both `P` and `E` categories in the selected Korean manuals; customer-facing answers should use the exact property name and target version first, then the most relevant operational category.

J005 expands the customer-facing initialization and storage property blocks in `GPTs/attachments/05_data_types_properties.md`. It keeps the J004 property-name inventory as the version-availability baseline, then adds source-backed defaults, ranges, dynamic-change methods, `V$PROPERTY` checks, and cautions for path, memory, disk, volatile, log, recycle-bin, datafile, tablespace extent, and temporary-page storage properties. Korean source precedence was applied for extraction drift found in the matching English 8.1 manual, including temporary tablespace extent defaults such as `SYS_TEMP_TBS_EXTENT_SIZE` and `USER_TEMP_TBS_EXTENT_SIZE`.

J006 expands the same customer-facing property catalog for LOB, JSON, Temporary LOB,
PSM, VARRAY, and object-size properties. It keeps the attachment boundary unchanged
and adds searchable blocks for `DISK_LOB_COLUMN_IN_ROW_SIZE`,
`MEMORY_LOB_COLUMN_IN_ROW_SIZE`, `MEMORY_VARIABLE_COLUMN_IN_ROW_SIZE`,
`LOB_OBJECT_BUFFER_SIZE`, `LOB_CACHE_THRESHOLD`, `ST_OBJECT_BUFFER_SIZE`,
`TEMPORARY_LOB_ENABLE`, `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`,
`MEMORY_TEMPLOB_PIECE_SIZE`, `PSM_CURSOR_OPEN_LIMIT`, `PSM_FILE_OPEN_LIMIT`,
`PSM_CASE_SENSITIVE_MODE`, `PSM_IGNORE_NO_DATA_FOUND_ERROR`,
`PSM_MAX_DDL_REFERENCE_DEPTH`, PSM character default-precision properties,
`LISTAGG_PRECISION`, and `VARRAY_MEMORY_MAXIMUM`. Korean source precedence was
applied for version-sensitive defaults such as 7.1 versus 7.3/8.1 PSM default
precision and for 8.1-only Temporary LOB property scope.

J006 also records a customer-facing caution for `PSM_CURSOR_OPEN_LIMIT` because the
detailed Korean property section says read-only while the property alter-level summary
lists `SYSTEM`; answers should verify the installed target version before generating a
dynamic change for that property.

J007 expands the customer-facing property catalog for buffer-pool, checkpoint,
optimizer, SQL plan cache, sort, hash, work-area, execution-memory, and parallel-query
properties. It keeps the attachment boundary unchanged and adds grouped searchable
blocks for `BUFFER_AREA_*`, buffer replacement/flusher thresholds, `CHECKPOINT_*`,
`FAST_START_*`, `HASH_AREA_SIZE`, `SORT_AREA_SIZE`, `TOTAL_WA_SIZE`,
`INIT_TOTAL_WA_SIZE`, `EXECUTE_STMT_MEMORY_MAXIMUM`,
`PREPARE_STMT_MEMORY_MAXIMUM`, `MATHEMATICS_TEMP_MEMORY_MAXIMUM`,
`HASH_JOIN_MEM_TEMP_*`, `SQL_PLAN_CACHE_*`, optimizer transformation controls, and
`PARALLEL_QUERY_*`. Korean source precedence was applied for version-sensitive defaults
such as 7.1 versus 7.3/8.1 `CHECKPOINT_INTERVAL_IN_LOG`,
`FAST_START_LOGFILE_TARGET`, and `EXECUTE_STMT_MEMORY_MAXIMUM`; Korean release notes
were used for the 8.1 `OPTIMIZER_FEATURE_ENABLE` default and
`CHECKPOINT_SCALE_SINGLE_DW_BUFFER_SIZE` introduction.

J007 also records customer-facing cautions for `EXECUTOR_FAST_SIMPLE_QUERY` and
`OUTER_JOIN_OPERATOR_TRANSFORM_ENABLE` because the detailed Korean property sections
and the alter-level summary do not align cleanly on dynamic-change support; answers
should verify the installed target server before generating an online change for either
property.

J008 expands the customer-facing property catalog for session, timeout, client
communication, NLS, network/security, SSL/TLS, SNMP, and replication properties. It
keeps the attachment boundary unchanged and adds grouped searchable blocks for
`CM_DISCONN_DETECT_TIME`, `CONCURRENT_EXEC_*`, IPC/IPCDA properties,
`MAX_STATEMENTS_PER_SESSION`, `NLS_*`, user-lock properties, timeout properties,
`SERVICE_THREAD_RECV_TIMEOUT`, ordinary/SSL/InfiniBand replication ports, replication
connection, heartbeat, DDL, conflict, sync, gap, recovery, and applier properties,
`IB_*`, `SNMP_*`, `TCP_ENABLE`, and `SSL_*` properties.

Korean source precedence was applied for J008 source drift and ambiguity:

- The Altibase 8.1 English extraction aid lists `IB_PORT_NO` with default `0`, while
  the Korean authority lists default `20300`; the attachment uses `20300`.
- The selected manuals' `SNMP_ENABLE` prose says set `1` to enable SNMP and default
  `0` disables SNMP, while the value bullets are contradictory; the attachment records
  the enable/disable caution and requires checking the SNMP Agent Guide and installed
  configuration before changing it.
- The Altibase 8.1 verified source summary table references
  `REPLICATION_UPDATE_REPLACE`, but the detailed property heading is absent in the
  selected 8.1 Korean General Reference text; the attachment treats the 7.1/7.3
  detailed property blocks as the source for default, range, and dynamic-change
  details until J009 property QA records the 8.1 source drift.

J009 validates property catalog coverage, dynamic-change wording, cross-references, and
remaining gaps without changing the attachment boundary. The QA pass confirmed that all
`484` property names in this inventory appear in the customer-facing property inventory
baseline in `GPTs/attachments/05_data_types_properties.md`; every decomposed property
section or group has an explicit dynamic-change, restart, recreation, or
installed-version verification cue; and all attachment filename cross-references from
the property attachment resolve to existing upload files. J009 also records the 8.1
source drift for `REPLICATION_UPDATE_REPLACE` and
`REPLICATION_META_ITEM_COUNT_DIFF_ENABLE`: `REPLICATION_UPDATE_REPLACE` has 8.1 Korean
Replication Manual behavior and an 8.1 Korean General Reference alter-level summary
entry, while the selected 8.1 Korean General Reference detailed property block is
absent; `REPLICATION_META_ITEM_COUNT_DIFF_ENABLE` appears in the 8.1 Replication Manual
environment-property list, while the selected 8.1 Korean General Reference detailed
property block is absent. Customer-facing answers must verify `V$PROPERTY` and the
exact installed 8.1 version before giving default, range, or change SQL for either
source-drift case.

## Scoped Sources

- Altibase 7.1 Korean authority: `Manuals/Altibase_7.1/kor/General Reference-1.Data Types & Altibase Properties.md`
- Altibase 7.1 English extraction aid: `Manuals/Altibase_7.1/eng/General Reference-1.Data Types & Altibase Properties.md`
- Altibase 7.3 Korean authority: `Manuals/Altibase_7.3/kor/General_Reference-1.Data Types & Altibase Properties.md`
- Altibase 7.3 English extraction aid: `Manuals/Altibase_7.3/eng/General Reference-1.Data Types & Altibase Properties.md`
- Altibase 8.1 verified source Korean authority: `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md`
- Altibase 8.1 verified source English extraction aid: `Manuals/Altibase_trunk/eng/General Reference-1.Data Types & Altibase Properties.md`

## Extraction Method

1. Locate `# 2.Altibase 프로퍼티` in each Korean General Reference 1 source.
2. Record the nearest Korean property-category heading for each detailed `#### <PROPERTY_NAME>` section.
3. Treat property names as literal technical tokens and preserve source capitalization.
4. Record presence by supported version family: 7.1, 7.3, and Altibase 8.1 verified source.
5. Do not infer default, range, or dynamic-change behavior from a property name or neighboring property. Use later property block expansion and `V$PROPERTY` checks for those details.

## Category Key

- `D`: Database initialization
- `P`: Performance
- `S`: Session
- `TO`: Time-out
- `T`: Transaction
- `B`: Backup and recovery
- `R`: Replication
- `NM`: Network and security
- `M`: Message logging
- `L`: Database link
- `U`: Auditing
- `A`: C/C++ external procedure agent
- `AS`: Account security
- `E`: Other

## Version Availability Summary

- Distinct property names inventoried: `484`.
- Documented in 7.1, 7.3, and Altibase 8.1 verified source: `444`.
- Documented only in 7.1 selected source: `5`.
- Documented in 7.1 and 7.3 selected sources, but not in Altibase 8.1 verified source: `2`.
- Documented in 7.3 and Altibase 8.1 verified source, but not in 7.1 selected source: `28`.
- Documented only in Altibase 8.1 verified source: `5`.

### 7.1-Only Property Names

- `LOCK_MGR_DETECTDEADLOCK_INTERVAL`, `LOCK_MGR_MAX_SLEEP`, `LOCK_MGR_MIN_SLEEP`, `LOCK_MGR_SPIN_COUNT`, `LOCK_MGR_TYPE`

### 7.1 And 7.3 Property Names Not Found In 8.1 Verified Source

- `REPLICATION_META_ITEM_COUNT_DIFF_ENABLE`, `REPLICATION_UPDATE_REPLACE`

### 7.3 And 8.1 Property Names Not Found In 7.1

- `CM_MSGLOG_COUNT`, `CM_MSGLOG_FILE`, `CM_MSGLOG_FLAG`, `CM_MSGLOG_SIZE`, `DISK_INDEX_BUILD_SORT_AREA_SIZE`, `DK_MSGLOG_RESERVE_SIZE`
- `DUMP_MSGLOG_RESERVE_SIZE`, `ERROR_MSGLOG_RESERVE_SIZE`, `MM_MSGLOG_FLAG`, `MM_MSGLOG_RESERVE_SIZE`, `NETWORK_ERROR_LOG_FILE`, `PSM_MAX_DDL_REFERENCE_DEPTH`
- `QP_MSGLOG_RESERVE_SIZE`, `REPLICATION_RECEIVER_APPLIER_YIELD_COUNT`, `RP_CONFLICT_MSGLOG_RESERVE_SIZE`, `RP_MSGLOG_RESERVE_SIZE`, `SERVER_MSGLOG_RESERVE_SIZE`, `SERVICE_THREAD_RECV_TIMEOUT`
- `SM_MSGLOG_RESERVE_SIZE`, `SSL_CIPHER_SUITES`, `SSL_LOAD_CONFIG`, `ST_MSGLOG_COUNT`, `ST_MSGLOG_FILE`, `ST_MSGLOG_FLAG`
- `ST_MSGLOG_SIZE`, `TRC_MSGLOG_RESERVE_SIZE`, `VARRAY_MEMORY_MAXIMUM`, `XA_MSGLOG_RESERVE_SIZE`

### 8.1-Only Property Names

- `CHECKPOINT_SCALE_SINGLE_DW_BUFFER_SIZE`, `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`, `MEMORY_TEMPLOB_PIECE_SIZE`, `REPLICATION_SSL_PORT_NO`, `TEMPORARY_LOB_ENABLE`

## Inventory Table

| Property | Availability | Primary category | 7.1 evidence | 7.3 evidence | 8.1 evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `BUFFER_AREA_CHUNK_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L4419 D | L4466 D | L4702 D | - |
| `BUFFER_AREA_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L4443 D | L4490 D | L4724 D | - |
| `BUFFER_CHECKPOINT_LIST_CNT` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L4465 D | L4512 D | L4746 D | - |
| `BUFFER_FLUSHER_CNT` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L4509 D | L4556 D | L4790 D | - |
| `BUFFER_FLUSH_LIST_CNT` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L4487 D | L4534 D | L4768 D | - |
| `BUFFER_HASH_BUCKET_DENSITY` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L4531 D | L4578 D | L4814 D | - |
| `BUFFER_HASH_CHAIN_LATCH_DENSITY` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L4553 D | L4600 D | L4836 D | - |
| `BUFFER_LRU_LIST_CNT` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L4577 D | L4624 D | L4860 D | - |
| `BUFFER_PREPARE_LIST_CNT` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L4599 D | L4646 D | L4882 D | - |
| `BULKIO_PAGE_COUNT_FOR_DIRECT_PATH_INSERT` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L4621 D | L4668 D | L4904 D | - |
| `COMPRESSION_RESOURCE_GC_SECOND` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L4645 D | L4692 D | L4928 D | - |
| `DB_NAME` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L4667 D | L4714 D | L4950 D | - |
| `DDL_SUPPLEMENTAL_LOG_ENABLE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L4689 D | L4736 D | L4972 D | - |
| `DEFAULT_DISK_DB_DIR` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L4717 D | L4764 D | L5000 D | - |
| `DEFAULT_MEM_DB_FILE_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L4739 D | L4786 D | L5022 D | - |
| `DEFAULT_SEGMENT_MANAGEMENT_TYPE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L4761 D | L4808 D | L5044 D | - |
| `DEFAULT_SEGMENT_STORAGE_INITEXTENTS` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L4787 D | L4834 D | L5070 D | - |
| `DEFAULT_SEGMENT_STORAGE_MAXEXTENTS` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L4809 D | L4856 D | L5092 D | - |
| `DEFAULT_SEGMENT_STORAGE_MINEXTENTS` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L4831 D | L4878 D | L5114 D | - |
| `DEFAULT_SEGMENT_STORAGE_NEXTEXTENTS` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L4853 D | L4900 D | L5136 D | - |
| `DIRECT_PATH_BUFFER_PAGE_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L4875 D | L4922 D | L5158 D | - |
| `DISK_INDEX_UNBALANCED_SPLIT_RATE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L4899 D | L4946 D | L5182 D | - |
| `DISK_LOB_COLUMN_IN_ROW_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L4923 D | L4970 D | L5206 D | - |
| `DISK_MAX_DB_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L4947 D | L4994 D | L5230 D | - |
| `DOUBLE_WRITE_DIRECTORY` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L4971 D | L5018 D | L5254 D | - |
| `DOUBLE_WRITE_DIRECTORY_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L4993 D | L5040 D | L5276 D | - |
| `DRDB_FD_MAX_COUNT_PER_DATAFILE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5015 D | L5062 D | L5298 D | - |
| `EXPAND_CHUNK_PAGE_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5037 D | L5084 D | L5320 D | - |
| `LOB_OBJECT_BUFFER_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5059 D | L5106 D | L5342 D | - |
| `LOCK_MGR_CACHE_NODE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5081 D | L5128 D | L5364 D | - |
| `LOCK_MGR_DETECTDEADLOCK_INTERVAL` | 7.1 | `D` Database initialization | L5111 D | - | - | - |
| `LOCK_MGR_MAX_SLEEP` | 7.1 | `D` Database initialization | L5135 D | - | - | - |
| `LOCK_MGR_MIN_SLEEP` | 7.1 | `D` Database initialization | L5159 D | - | - | - |
| `LOCK_MGR_SPIN_COUNT` | 7.1 | `D` Database initialization | L5183 D | - | - | - |
| `LOCK_MGR_TYPE` | 7.1 | `D` Database initialization | L5207 D | - | - | - |
| `LOCK_NODE_CACHE_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5235 D | L5158 D | L5394 D | - |
| `LOGANCHOR_DIR` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5257 D | L5182 D | L5418 D | - |
| `LOG_DIR` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5279 D | L5204 D | L5440 D | - |
| `LOG_FILE_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5301 D | L5226 D | L5462 D | - |
| `MAX_CLIENT` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5328 D | L5253 D | L5489 D | - |
| `MEMORY_INDEX_BUILD_RUN_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5402 D | L5327 D | L5563 D | - |
| `MEMORY_INDEX_BUILD_VALUE_LENGTH_THRESHOLD` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5426 D | L5351 D | L5587 D | - |
| `MEMORY_INDEX_UNBALANCED_SPLIT_RATE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5452 D | L5377 D | L5613 D | - |
| `MEMORY_LOB_COLUMN_IN_ROW_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5476 D | L5401 D | L5637 D | - |
| `MEMORY_VARIABLE_COLUMN_IN_ROW_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5500 D | L5425 D | L5661 D | - |
| `MEM_DB_DIR` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5352 D | L5277 D | L5513 D | - |
| `MEM_MAX_DB_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5376 D | L5301 D | L5537 D | - |
| `MEM_SIZE_CLASS_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5524 D | L5449 D | L5685 D | - |
| `MIN_COMPRESSION_RESOURCE_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5546 D | L5471 D | L5707 D | - |
| `MIN_LOG_RECORD_SIZE_FOR_COMPRESS` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5568 D | L5493 D | L5729 D | - |
| `MIN_PAGES_ON_DB_FREE_LIST` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5592 D | L5517 D | L5753 D | - |
| `MIN_PAGES_ON_TABLE_FREE_LIST` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5614 D | L5539 D | L5775 D | - |
| `MIN_TASK_COUNT_FOR_THREAD_LIVE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5636 D | L5561 D | L5797 D | - |
| `PCTFREE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5660 D | L5585 D | L5821 D | - |
| `PCTUSED` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5686 D | L5611 D | L5847 D | - |
| `QP_MEMORY_CHUNK_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5712 D | L5637 D | L5873 D | - |
| `RECYCLEBIN_DISK_MAX_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5734 D | L5659 D | L5895 D | - |
| `RECYCLEBIN_ENABLE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5758 D | L5683 D | L5919 D | - |
| `RECYCLEBIN_MEM_MAX_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5790 D | L5715 D | L5951 D | - |
| `REDUCE_TEMP_MEMORY_ENABLE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5814 D | L5739 D | L5975 D | - |
| `SECURITY_ECC_POLICY_NAME` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5846 D | L5771 D | L6007 D | - |
| `SECURITY_MODULE_LIBRARY` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5868 D | L5793 D | L6029 D | - |
| `SECURITY_MODULE_NAME` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5890 D | L5815 D | L6051 D | - |
| `SERVICE_THREAD_INITIAL_LIFESPAN` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5912 D | L5837 D | L6073 D | - |
| `SMALL_TABLE_THRESHOLD` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5938 D | L5863 D | L6099 D | - |
| `ST_OBJECT_BUFFER_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5964 D | L5889 D | L6125 D | - |
| `SYS_DATA_FILE_INIT_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L5986 D | L5911 D | L6147 D | - |
| `SYS_DATA_FILE_MAX_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L6008 D | L5933 D | L6169 D | - |
| `SYS_DATA_FILE_NEXT_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L6032 D | L5957 D | L6193 D | - |
| `SYS_DATA_TBS_EXTENT_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L6056 D | L5981 D | L6217 D | - |
| `SYS_TEMP_FILE_INIT_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L6082 D | L6007 D | L6243 D | - |
| `SYS_TEMP_FILE_MAX_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L6104 D | L6029 D | L6265 D | - |
| `SYS_TEMP_FILE_NEXT_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L6128 D | L6053 D | L6289 D | - |
| `SYS_TEMP_TBS_EXTENT_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L6150 D | L6075 D | L6311 D | - |
| `SYS_UNDO_FILE_INIT_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L6176 D | L6101 D | L6337 D | - |
| `SYS_UNDO_FILE_MAX_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L6198 D | L6123 D | L6359 D | - |
| `SYS_UNDO_FILE_NEXT_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L6220 D | L6145 D | L6381 D | - |
| `SYS_UNDO_TBS_EXTENT_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L6242 D | L6167 D | L6403 D | - |
| `TABLE_BACKUP_FILE_BUFFER_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L6266 D | L6191 D | L6427 D | - |
| `TABLE_COMPACT_AT_SHUTDOWN` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L6288 D | L6213 D | L6449 D | - |
| `TEMP_HASH_BUCKET_DENSITY` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L6310 D | L6235 D | L6471 D | - |
| `TEMP_PAGE_CHUNK_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L6334 D | L6259 D | L6495 D | - |
| `USER_DATA_FILE_INIT_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L6356 D | L6281 D | L6517 D | - |
| `USER_DATA_FILE_MAX_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L6378 D | L6303 D | L6539 D | - |
| `USER_DATA_FILE_NEXT_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L6402 D | L6327 D | L6563 D | - |
| `USER_DATA_TBS_EXTENT_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L6424 D | L6349 D | L6585 D | - |
| `USER_TEMP_FILE_INIT_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L6448 D | L6373 D | L6609 D | - |
| `USER_TEMP_FILE_MAX_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L6470 D | L6395 D | L6631 D | - |
| `USER_TEMP_FILE_NEXT_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L6494 D | L6419 D | L6655 D | - |
| `USER_TEMP_TBS_EXTENT_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L6516 D | L6441 D | L6677 D | - |
| `VOLATILE_MAX_DB_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `D` Database initialization | L6538 D | L6463 D | L6699 D | - |
| `AGER_WAIT_MAXIMUM` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L6564 P | L6489 P | L6725 P | - |
| `AGER_WAIT_MINIMUM` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L6586 P | L6511 P | L6747 P | - |
| `BUFFER_VICTIM_SEARCH_INTERVAL` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L6608 P | L6533 P | L6769 P | - |
| `BUFFER_VICTIM_SEARCH_PCT` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L6630 P | L6555 P | L6791 P | - |
| `CHECKPOINT_BULK_SYNC_PAGE_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L6652 P | L6577 P | L6813 P | - |
| `CHECKPOINT_BULK_WRITE_PAGE_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L6676 P | L6601 P | L6837 P | - |
| `CHECKPOINT_BULK_WRITE_SLEEP_SEC` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L6700 P | L6625 P | L6861 P | - |
| `CHECKPOINT_BULK_WRITE_SLEEP_USEC` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L6724 P | L6649 P | L6885 P | - |
| `CHECKPOINT_FLUSH_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L6748 P | L6673 P | L6909 P | - |
| `CHECKPOINT_FLUSH_MAX_GAP` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L6770 P | L6695 P | L6931 P | - |
| `CHECKPOINT_FLUSH_MAX_WAIT_SEC` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L6794 P | L6719 P | L6955 P | - |
| `CM_BUFFER_MAX_PENDING_LIST` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L6816 P | L6741 P | L6977 P | - |
| `CM_DISPATCHER_SOCK_POLL_TYPE` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L6838 P | L6763 P | L6999 P | - |
| `DATABASE_IO_TYPE` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L6864 P | L6789 P | L7025 P | - |
| `DATAFILE_WRITE_UNIT_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L6888 P | L6813 P | L7049 P | - |
| `DB_FILE_MULTIPAGE_READ_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L6912 P | L6837 P | L7073 P | - |
| `DEDICATED_THREAD_CHECK_INTERVAL` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L6940 P | L6865 P | L7101 P | - |
| `DEDICATED_THREAD_INIT_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L6964 P | L6891 P | L7127 P | - |
| `DEDICATED_THREAD_MAX_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L6988 P | L6915 P | L7151 P | - |
| `DEDICATED_THREAD_MODE` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7014 P | L6941 P | L7177 P | - |
| `DEFAULT_FLUSHER_WAIT_SEC` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7038 P | L6965 P | L7201 P | - |
| `DELAYED_FLUSH_LIST_PCT` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7060 P | L6987 P | L7223 P | - |
| `DELAYED_FLUSH_PROTECTION_TIME_MSEC` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7084 P | L7009 P | L7245 P | - |
| `DIRECT_IO_ENABLED` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7108 P | L7031 P | L7269 P | - |
| `DISK_INDEX_BUILD_MERGE_PAGE_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7134 P | L7057 P | L7295 P | - |
| `DISK_INDEX_BUILD_SORT_AREA_SIZE` | 7.3, Altibase 8.1 verified source | `P` Performance | - | L7085 P | L7323 P | - |
| `EXECUTE_STMT_MEMORY_MAXIMUM` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7158 P | L7113 P | L7351 P | - |
| `EXECUTOR_FAST_SIMPLE_QUERY` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7182 P | L7135 P | L7373 P | - |
| `FAST_START_IO_TARGET` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7210 P | L7163 P | L7401 P | - |
| `FAST_START_LOGFILE_TARGET` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7238 P | L7191 P | L7429 P | - |
| `FAST_UNLOCK_LOG_ALLOC_MUTEX` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7266 P | L7219 P | L7457 P | - |
| `HASH_AREA_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7292 P | L7245 P | L7483 P | - |
| `HASH_JOIN_MEM_TEMP_AUTO_BUCKET_COUNT_DISABLE` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7316 P | L7269 P | L7507 P | - |
| `HASH_JOIN_MEM_TEMP_PARTITIONING_DISABLE` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7348 P | L7301 P | L7539 P | - |
| `HIGH_FLUSH_PCT` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7378 P | L7331 P | L7569 P | - |
| `HOT_LIST_PCT` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7400 P | L7353 P | L7593 P | - |
| `HOT_TOUCH_CNT` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7422 P | L7375 P | L7617 P | - |
| `INDEX_BUILD_THREAD_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7444 P | L7397 P | L7639 P | - |
| `INDEX_INITRANS` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7468 P | L7421 P | L7663 P | - |
| `INDEX_MAXTRANS` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7490 P | L7443 P | L7685 P | - |
| `INIT_TOTAL_WA_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L9045 P | L9000 P | L9243 P | - |
| `LFG_GROUP_COMMIT_INTERVAL_USEC` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7512 P | L7465 P | L7707 P | - |
| `LFG_GROUP_COMMIT_RETRY_USEC` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7538 P | L7491 P | L7733 P | - |
| `LFG_GROUP_COMMIT_UPDATE_TX_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7562 P | L7515 P | L7757 P | - |
| `LOB_CACHE_THRESHOLD` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7586 P | L7539 P | L7781 P | - |
| `LOCK_ESCALATION_MEMORY_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7612 P | L7565 P | L7807 P | - |
| `LOG_CREATE_METHOD` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7666 P | L7619 P | L7861 P | - |
| `LOG_IO_TYPE` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7640 P | L7593 P | L7835 P | - |
| `LOW_FLUSH_PCT` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7692 P | L7646 P | L7888 P | - |
| `LOW_PREPARE_PCT` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7714 P | L7668 P | L7910 P | - |
| `MATHEMATICS_TEMP_MEMORY_MAXIMUM` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7736 P | L7690 P | L7932 P | - |
| `MAX_FLUSHER_WAIT_SEC` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7757 P | L7712 P | L7954 P | - |
| `MEM_INDEX_KEY_REDISTRIBUTION` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7779 P | L7734 P | L7976 P | - |
| `MEM_INDEX_KEY_REDISTRIBUTION_STANDARD_RATE` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7809 P | L7764 P | L8006 P | - |
| `MULTIPLEXING_CHECK_INTERVAL` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7835 P | L7790 P | L8032 P | - |
| `MULTIPLEXING_MAX_THREAD_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7859 P | L7814 P | L8056 P | - |
| `MULTIPLEXING_THREAD_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7885 P | L7840 P | L8082 P | - |
| `NORMALFORM_MAXIMUM` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7909 P | L7864 P | L8106 P | - |
| `OPTIMIZER_AUTO_STATS` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7943 P | L7898 P | L8140 P | - |
| `OPTIMIZER_DELAYED_EXECUTION` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L7981 P | L7936 P | L8178 P | - |
| `OPTIMIZER_FEATURE_ENABLE` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8011 P | L7966 P | L8208 P | - |
| `OPTIMIZER_MODE` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8052 P | L8007 P | L8249 P | - |
| `OPTIMIZER_PERFORMANCE_VIEW` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8076 P | L8031 P | L8273 P | - |
| `OPTIMIZER_UNNEST_AGGREGATION_SUBQUERY` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8102 P | L8057 P | L8299 P | - |
| `OPTIMIZER_UNNEST_COMPLEX_SUBQUERY` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8132 P | L8087 P | L8329 P | - |
| `OPTIMIZER_UNNEST_SUBQUERY` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8160 P | L8115 P | L8357 P | - |
| `OUTER_JOIN_OPERATOR_TRANSFORM_ENABLE` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8188 P | L8143 P | L8385 P | - |
| `PARALLEL_LOAD_FACTOR` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8218 P | L8173 P | L8415 P | - |
| `PARALLEL_QUERY_QUEUE_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8266 P<br>L15273 E | L8221 P<br>L15779 E | L8463 P<br>L16086 E | Multiple detailed categories: `P`, `E` |
| `PARALLEL_QUERY_THREAD_MAX` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8242 P<br>L15295 E | L8197 P<br>L15801 E | L8439 P<br>L16108 E | Multiple detailed categories: `P`, `E` |
| `PREPARE_STMT_MEMORY_MAXIMUM` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8290 P | L8245 P | L8487 P | - |
| `QUERY_REWRITE_ENABLE` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8314 P | L8269 P | L8511 P | - |
| `REFINE_PAGE_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8340 P | L8295 P | L8537 P | - |
| `RESULT_CACHE_ENABLE` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8364 P | L8319 P | L8561 P | - |
| `RESULT_CACHE_MEMORY_MAXIMUM` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8392 P | L8347 P | L8589 P | - |
| `SECONDARY_BUFFER_ENABLE` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8416 P | L8371 P | L8613 P | - |
| `SECONDARY_BUFFER_FILE_DIRECTORY` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8444 P | L8399 P | L8641 P | - |
| `SECONDARY_BUFFER_FLUSHER_CNT` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8468 P | L8423 P | L8665 P | - |
| `SECONDARY_BUFFER_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8492 P | L8447 P | L8689 P | - |
| `SECONDARY_BUFFER_TYPE` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8516 P | L8471 P | L8713 P | - |
| `SERIAL_EXECUTE_MODE` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L9147 P | L9102 P | L9345 P | - |
| `SORT_AREA_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8546 P | L8501 P | L8743 P | - |
| `SQL_PLAN_CACHE_BUCKET_CNT` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8570 P | L8525 P | L8767 P | - |
| `SQL_PLAN_CACHE_HOT_REGION_LRU_RATIO` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8592 P | L8547 P | L8789 P | - |
| `SQL_PLAN_CACHE_PREPARED_EXECUTION_CONTEXT_CNT` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8616 P | L8571 P | L8814 P | - |
| `SQL_PLAN_CACHE_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8642 P | L8597 P | L8840 P | - |
| `STATEMENT_LIST_PARTIAL_SCAN_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8666 P | L8621 P | L8864 P | - |
| `TABLESPACE_LOCK_ENABLE` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8794 P | L8749 P | L8992 P | - |
| `TABLE_INITRANS` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8690 P | L8645 P | L8888 P | - |
| `TABLE_LOCK_ENABLE` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8712 P | L8667 P | L8910 P | - |
| `TABLE_LOCK_MODE` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8746 P | L8701 P | L8944 P | - |
| `TABLE_MAXTRANS` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8772 P | L8727 P | L8970 P | - |
| `TEMP_STATS_WATCH_TIME` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8826 P | L8781 P | L9024 P | - |
| `THREAD_CPU_AFFINITY` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8850 P | L8805 P | L9048 P | - |
| `THREAD_REUSE_ENABLE` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8877 P | L8832 P | L9075 P | - |
| `TIMED_STATISTICS` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8905 P | L8860 P | L9103 P | - |
| `TIMER_RUNNING_LEVEL` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8931 P | L8886 P | L9129 P | - |
| `TIMER_THREAD_RESOLUTION` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8967 P | L8922 P | L9165 P | - |
| `TOP_RESULT_CACHE_MODE` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L8989 P | L8944 P | L9187 P | - |
| `TOTAL_WA_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L9021 P | L8976 P | L9219 P | - |
| `TOUCH_TIME_INTERVAL` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L9071 P | L9026 P | L9269 P | - |
| `TRANSACTION_SEGMENT_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L9095 P | L9050 P | L9293 P | - |
| `TRX_UPDATE_MAX_LOGSIZE` | 7.1, 7.3, Altibase 8.1 verified source | `P` Performance | L9119 P | L9074 P | L9317 P | - |
| `CM_DISCONN_DETECT_TIME` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L9177 S | L9132 S | L9375 S | - |
| `CONCURRENT_EXEC_DEGREE_DEFAULT` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L9205 S | L9160 S | L9403 S | - |
| `CONCURRENT_EXEC_DEGREE_MAX` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L9231 S | L9186 S | L9429 S | - |
| `CONCURRENT_EXEC_WAIT_INTERVAL` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L9257 S | L9212 S | L9455 S | - |
| `DEFAULT_THREAD_STACK_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L9283 S | L9238 S | L9481 S | - |
| `IPCDA_CHANNEL_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L9403 S | L9358 S | L9601 S | - |
| `IPCDA_DATABLOCK_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L9427 S | L9382 S | L9625 S | - |
| `IPCDA_FILEPATH` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L9451 S | L9406 S | L9649 S | - |
| `IPCDA_SEM_KEY` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L9475 S | L9430 S | L9673 S | - |
| `IPCDA_SHM_KEY` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L9501 S | L9456 S | L9699 S | - |
| `IPC_CHANNEL_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L9305 S | L9260 S | L9503 S | - |
| `IPC_FILEPATH` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L9327 S | L9282 S | L9525 S | - |
| `IPC_SEM_KEY` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L9351 S | L9306 S | L9549 S | - |
| `IPC_SHM_KEY` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L9377 S | L9332 S | L9575 S | - |
| `MAX_LISTEN` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L9527 S | L9482 S | L9725 S | - |
| `MAX_STATEMENTS_PER_SESSION` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L9549 S | L9504 S | L9747 S | - |
| `NET_CONN_IP_STACK` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L9573 S | L9528 S | L9771 S | - |
| `NLS_COMP` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L9601 S | L9556 S | L9799 S | - |
| `NLS_CURRENCY` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L9625 S | L9580 S | L9823 S | - |
| `NLS_ISO_CURRENCY` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L9655 S | L9610 S | L9853 S | - |
| `NLS_NCHAR_CONV_EXCP` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L9683 S | L9638 S | L9881 S | - |
| `NLS_NCHAR_LITERAL_REPLACE` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L9713 S | L9668 S | L9911 S | - |
| `NLS_NUMERIC_CHARACTERS` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L9745 S | L9700 S | L9943 S | - |
| `NLS_TERRITORY` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L9775 S | L9730 S | L9973 S | - |
| `PORT_NO` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L9805 S | L9760 S | L10003 S | - |
| `PSM_CURSOR_OPEN_LIMIT` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L9827 S | L9782 S | L10025 S | - |
| `PSM_FILE_OPEN_LIMIT` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L9849 S | L9804 S | L10047 S | - |
| `TIME_ZONE` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L9871 S | L9826 S | L10069 S | - |
| `UNIXDOMAIN_FILEPATH` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L9895 S | L9850 S | L10093 S | - |
| `USER_LOCK_POOL_INIT_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L9947 S | L9902 S | L10145 S | - |
| `USER_LOCK_REQUEST_CHECK_INTERVAL` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L9971 S | L9926 S | L10169 S | - |
| `USER_LOCK_REQUEST_LIMIT` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L9995 S | L9950 S | L10193 S | - |
| `USER_LOCK_REQUEST_TIMEOUT` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L10019 S | L9974 S | L10215 S | - |
| `USE_MEMORY_POOL` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L9919 S | L9874 S | L10117 S | - |
| `XA_HEURISTIC_COMPLETE` | 7.1, 7.3, Altibase 8.1 verified source | `S` Session | L10043 S | L9998 S | L10239 S | - |
| `BLOCK_ALL_TX_TIME_OUT` | 7.1, 7.3, Altibase 8.1 verified source | `TO` Time-out | L10075 TO | L10030 TO | L10271 TO | - |
| `DDL_LOCK_TIMEOUT` | 7.1, 7.3, Altibase 8.1 verified source | `TO` Time-out | L10099 TO | L10054 TO | L10295 TO | - |
| `DDL_TIMEOUT` | 7.1, 7.3, Altibase 8.1 verified source | `TO` Time-out | L10125 TO | L10080 TO | L10321 TO | - |
| `FETCH_TIMEOUT` | 7.1, 7.3, Altibase 8.1 verified source | `TO` Time-out | L10151 TO | L10106 TO | L10347 TO | - |
| `IDLE_TIMEOUT` | 7.1, 7.3, Altibase 8.1 verified source | `TO` Time-out | L10175 TO | L10130 TO | L10371 TO | - |
| `LOGIN_TIMEOUT` | 7.1, 7.3, Altibase 8.1 verified source | `TO` Time-out | L10201 TO | L10156 TO | L10397 TO | - |
| `MULTIPLEXING_POLL_TIMEOUT` | 7.1, 7.3, Altibase 8.1 verified source | `TO` Time-out | L10223 TO | L10178 TO | L10419 TO | - |
| `QUERY_TIMEOUT` | 7.1, 7.3, Altibase 8.1 verified source | `TO` Time-out | L10245 TO | L10200 TO | L10441 TO | - |
| `SERVICE_THREAD_RECV_TIMEOUT` | 7.3, Altibase 8.1 verified source | `TO` Time-out | - | L10224 TO | L10465 TO | - |
| `SHUTDOWN_IMMEDIATE_TIMEOUT` | 7.1, 7.3, Altibase 8.1 verified source | `TO` Time-out | L10269 TO | L10247 TO | L10488 TO | - |
| `UTRANS_TIMEOUT` | 7.1, 7.3, Altibase 8.1 verified source | `TO` Time-out | L10293 TO | L10271 TO | L10512 TO | - |
| `XA_INDOUBT_TX_TIMEOUT` | 7.1, 7.3, Altibase 8.1 verified source | `TO` Time-out | L10317 TO | L10295 TO | L10536 TO | - |
| `AUTO_COMMIT` | 7.1, 7.3, Altibase 8.1 verified source | `T` Transaction | L10341 T | L10319 T | L10560 T | - |
| `ISOLATION_LEVEL` | 7.1, 7.3, Altibase 8.1 verified source | `T` Transaction | L10367 T | L10345 T | L10586 T | - |
| `TRANSACTION_TABLE_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `T` Transaction | L10397 T | L10375 T | L10616 T | - |
| `ARCHIVE_DIR` | 7.1, 7.3, Altibase 8.1 verified source | `B` Backup and recovery | L10425 B | L10403 B | L10644 B | - |
| `ARCHIVE_FULL_ACTION` | 7.1, 7.3, Altibase 8.1 verified source | `B` Backup and recovery | L10449 B | L10427 B | L10668 B | - |
| `ARCHIVE_MULTIPLEX_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `B` Backup and recovery | L10479 B | L10457 B | L10698 B | - |
| `ARCHIVE_MULTIPLEX_DIR` | 7.1, 7.3, Altibase 8.1 verified source | `B` Backup and recovery | L10505 B | L10483 B | L10724 B | - |
| `ARCHIVE_THREAD_AUTOSTART` | 7.1, 7.3, Altibase 8.1 verified source | `B` Backup and recovery | L10527 B | L10505 B | L10746 B | - |
| `CHECKPOINT_ENABLED` | 7.1, 7.3, Altibase 8.1 verified source | `B` Backup and recovery | L10551 B | L10529 B | L10770 B | - |
| `CHECKPOINT_INTERVAL_IN_LOG` | 7.1, 7.3, Altibase 8.1 verified source | `B` Backup and recovery | L10579 B | L10557 B | L10798 B | - |
| `CHECKPOINT_INTERVAL_IN_SEC` | 7.1, 7.3, Altibase 8.1 verified source | `B` Backup and recovery | L10605 B | L10583 B | L10824 B | - |
| `CHECKPOINT_SCALE_SINGLE_DW_BUFFER_SIZE` | Altibase 8.1 verified source | `B` Backup and recovery | - | - | L10848 B | - |
| `COMMIT_WRITE_WAIT_MODE` | 7.1, 7.3, Altibase 8.1 verified source | `B` Backup and recovery | L10629 B | L10607 B | L10872 B | - |
| `INCREMENTAL_BACKUP_CHUNK_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `B` Backup and recovery | L10657 B | L10635 B | L10900 B | - |
| `INCREMENTAL_BACKUP_INFO_RETENTION_PERIOD` | 7.1, 7.3, Altibase 8.1 verified source | `B` Backup and recovery | L10685 B | L10663 B | L10928 B | - |
| `LOG_BUFFER_TYPE` | 7.1, 7.3, Altibase 8.1 verified source | `B` Backup and recovery | L10711 B | L10689 B | L10954 B | - |
| `LOG_MULTIPLEX_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `B` Backup and recovery | L10739 B | L10717 B | L10982 B | - |
| `LOG_MULTIPLEX_DIR` | 7.1, 7.3, Altibase 8.1 verified source | `B` Backup and recovery | L10765 B | L10743 B | L11008 B | - |
| `PREPARE_LOG_FILE_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `B` Backup and recovery | L10787 B | L10765 B | L11030 B | - |
| `SNAPSHOT_DISK_UNDO_THRESHOLD` | 7.1, 7.3, Altibase 8.1 verified source | `B` Backup and recovery | L10833 B | L10811 B | L11076 B | - |
| `SNAPSHOT_MEM_THRESHOLD` | 7.1, 7.3, Altibase 8.1 verified source | `B` Backup and recovery | L10809 B | L10787 B | L11052 B | - |
| `REPLICATION_ACK_XLOG_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L10861 R | L10839 R | L11104 R | - |
| `REPLICATION_ALLOW_DUPLICATE_HOSTS` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L10889 R | L10867 R | L11132 R | - |
| `REPLICATION_BEFORE_IMAGE_LOG_ENABLE` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L10915 R | L10893 R | L11158 R | - |
| `REPLICATION_COMMIT_WRITE_WAIT_MODE` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L10945 R | L10923 R | L11188 R | - |
| `REPLICATION_CONNECT_RECEIVE_TIMEOUT` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L10967 R | L10945 R | L11210 R | - |
| `REPLICATION_CONNECT_TIMEOUT` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L10991 R | L10969 R | L11234 R | - |
| `REPLICATION_DDL_ENABLE` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11015 R | L10993 R | L11258 R | - |
| `REPLICATION_DDL_ENABLE_LEVEL` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11041 R | L11019 R | L11284 R | - |
| `REPLICATION_DDL_SYNC` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11066 R | L11043 R | L11308 R | - |
| `REPLICATION_DDL_SYNC_TIMEOUT` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11094 R | L11071 R | L11336 R | - |
| `REPLICATION_EAGER_PARALLEL_FACTOR` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11126 R | L11099 R | L11364 R | - |
| `REPLICATION_EAGER_RECEIVER_MAX_ERROR_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11152 R | L11125 R | L11390 R | - |
| `REPLICATION_FAILBACK_INCREMENTAL_SYNC` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11180 R | L11153 R | L11418 R | - |
| `REPLICATION_GAPLESS_ALLOW_TIME` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11235 R | L11209 R | L11473 R | - |
| `REPLICATION_GAPLESS_MAX_WAIT_TIME` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11263 R | L11237 R | L11501 R | - |
| `REPLICATION_GAP_UNIT` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11207 R | L11181 R | L11445 R | - |
| `REPLICATION_GROUPING_AHEAD_READ_NEXT_LOG_FILE` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11289 R | L11263 R | L11527 R | - |
| `REPLICATION_GROUPING_TRANSACTION_MAX_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11313 R | L11287 R | L11551 R | - |
| `REPLICATION_HBT_DETECT_HIGHWATER_MARK` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11337 R | L11311 R | L11575 R | - |
| `REPLICATION_HBT_DETECT_TIME` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11363 R | L11337 R | L11601 R | - |
| `REPLICATION_IB_LATENCY` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11389 R | L11363 R | L11627 R | - |
| `REPLICATION_IB_PORT_NO` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11413 R | L11387 R | L11651 R | - |
| `REPLICATION_INSERT_REPLACE` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11437 R | L11411 R | L11675 R | - |
| `REPLICATION_KEEP_ALIVE_CNT` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11461 R | L11435 R | L11699 R | - |
| `REPLICATION_LOCK_TIMEOUT` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11483 R | L11457 R | L11721 R | - |
| `REPLICATION_LOG_BUFFER_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11507 R | L11481 R | L11745 R | - |
| `REPLICATION_MAX_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11537 R | L11511 R | L11775 R | - |
| `REPLICATION_MAX_LISTEN` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11561 R | L11535 R | L11799 R | - |
| `REPLICATION_MAX_LOGFILE` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11583 R | L11557 R | L11821 R | - |
| `REPLICATION_META_ITEM_COUNT_DIFF_ENABLE` | 7.1, 7.3 | `R` Replication | L12300 R | L12295 R | - | 8.1 Replication Manual lists the property in the replication-environment property set, but selected 8.1 Korean General Reference detailed property block is absent. |
| `REPLICATION_POOL_ELEMENT_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11611 R | L11585 R | L11849 R | - |
| `REPLICATION_POOL_ELEMENT_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11635 R | L11609 R | L11873 R | - |
| `REPLICATION_PORT_NO` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11659 R | L11633 R | L11897 R | - |
| `REPLICATION_PREFETCH_LOGFILE_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11681 R | L11655 R | L11919 R | - |
| `REPLICATION_RECEIVER_APPLIER_ASSIGN_MODE` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11731 R | L11705 R | L11969 R | - |
| `REPLICATION_RECEIVER_APPLIER_QUEUE_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11761 R | L11735 R | L11999 R | - |
| `REPLICATION_RECEIVER_APPLIER_YIELD_COUNT` | 7.3, Altibase 8.1 verified source | `R` Replication | - | L11761 R | L12025 R | - |
| `REPLICATION_RECEIVE_TIMEOUT` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11703 R | L11677 R | L11941 R | - |
| `REPLICATION_RECOVERY_MAX_LOGFILE` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11787 R | L11785 R | L12049 R | - |
| `REPLICATION_RECOVERY_MAX_TIME` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11817 R | L11815 R | L12079 R | - |
| `REPLICATION_SENDER_AUTO_START` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11843 R | L11841 R | L12105 R | - |
| `REPLICATION_SENDER_COMPRESS_XLOG` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11865 R | L11863 R | L12127 R | - |
| `REPLICATION_SENDER_ENCRYPT_XLOG` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11893 R | L11891 R | L12155 R | - |
| `REPLICATION_SENDER_IP` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11919 R | L11917 R | L12181 R | - |
| `REPLICATION_SENDER_SEND_TIMEOUT` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11954 R | L11952 R | L12216 R | - |
| `REPLICATION_SENDER_SLEEP_TIME` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L11980 R | L11978 R | L12242 R | - |
| `REPLICATION_SENDER_SLEEP_TIMEOUT` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L12002 R | L12000 R | L12264 R | - |
| `REPLICATION_SENDER_START_AFTER_GIVING_UP` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L12027 R | L12024 R | L12288 R | - |
| `REPLICATION_SERVER_FAILBACK_MAX_TIME` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L12053 R | L12050 R | L12314 R | - |
| `REPLICATION_SQL_APPLY_ENABLE` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L12075 R | L12072 R | L12336 R | - |
| `REPLICATION_SSL_PORT_NO` | Altibase 8.1 verified source | `R` Replication | - | - | L12373 R | - |
| `REPLICATION_SYNC_APPLY_METHOD` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L12111 R | L12108 R | L12395 R | - |
| `REPLICATION_SYNC_LOCK_TIMEOUT` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L12142 R | L12137 R | L12424 R | - |
| `REPLICATION_SYNC_LOG` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L12168 R | L12163 R | L12450 R | - |
| `REPLICATION_SYNC_TUPLE_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L12192 R | L12187 R | L12474 R | - |
| `REPLICATION_TIMESTAMP_RESOLUTION` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L12216 R | L12211 R | L12498 R | - |
| `REPLICATION_TRANSACTION_POOL_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `R` Replication | L12246 R | L12241 R | L12528 R | - |
| `REPLICATION_UPDATE_REPLACE` | 7.1, 7.3 | `R` Replication | L12276 R | L12271 R | - | 8.1 Korean Replication Manual describes behavior and 8.1 Korean General Reference summary lists `SYSTEM`, but selected 8.1 Korean General Reference detailed property block is absent. |
| `IB_CONCHKSPIN` | 7.1, 7.3, Altibase 8.1 verified source | `NM` Network and security | L12327 NM | L12321 NM | L12582 NM | - |
| `IB_ENABLE` | 7.1, 7.3, Altibase 8.1 verified source | `NM` Network and security | L12351 NM | L12345 NM | L12606 NM | - |
| `IB_LATENCY` | 7.1, 7.3, Altibase 8.1 verified source | `NM` Network and security | L12377 NM | L12371 NM | L12632 NM | - |
| `IB_LISTENER_DISABLE` | 7.1, 7.3, Altibase 8.1 verified source | `NM` Network and security | L12403 NM | L12397 NM | L12658 NM | - |
| `IB_MAX_LISTEN` | 7.1, 7.3, Altibase 8.1 verified source | `NM` Network and security | L12429 NM | L12423 NM | L12684 NM | - |
| `IB_PORT_NO` | 7.1, 7.3, Altibase 8.1 verified source | `NM` Network and security | L12451 NM | L12445 NM | L12706 NM | - |
| `SNMP_ALARM_FETCH_TIMEOUT` | 7.1, 7.3, Altibase 8.1 verified source | `NM` Network and security | L12495 NM | L12489 NM | L12750 NM | - |
| `SNMP_ALARM_QUERY_TIMEOUT` | 7.1, 7.3, Altibase 8.1 verified source | `NM` Network and security | L12473 NM | L12467 NM | L12728 NM | - |
| `SNMP_ALARM_SESSION_FAILURE_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `NM` Network and security | L12545 NM | L12540 NM | L12800 NM | - |
| `SNMP_ALARM_UTRANS_TIMEOUT` | 7.1, 7.3, Altibase 8.1 verified source | `NM` Network and security | L12517 NM | L12511 NM | L12772 NM | - |
| `SNMP_ENABLE` | 7.1, 7.3, Altibase 8.1 verified source | `NM` Network and security | L12567 NM | L12562 NM | L12822 NM | - |
| `SNMP_MSGLOG_FLAG` | 7.1, 7.3, Altibase 8.1 verified source | `NM` Network and security | L12593 NM | L12588 NM | L12848 NM | - |
| `SNMP_PORT_NO` | 7.1, 7.3, Altibase 8.1 verified source | `NM` Network and security | L12615 NM | L12610 NM | L12870 NM | - |
| `SNMP_RECV_TIMEOUT` | 7.1, 7.3, Altibase 8.1 verified source | `NM` Network and security | L12659 NM | L12654 NM | L12914 NM | - |
| `SNMP_SEND_TIMEOUT` | 7.1, 7.3, Altibase 8.1 verified source | `NM` Network and security | L12683 NM | L12678 NM | L12938 NM | - |
| `SNMP_TRAP_PORT_NO` | 7.1, 7.3, Altibase 8.1 verified source | `NM` Network and security | L12637 NM | L12632 NM | L12892 NM | - |
| `SSL_CA` | 7.1, 7.3, Altibase 8.1 verified source | `NM` Network and security | L12707 NM | L12702 NM | L12962 NM | - |
| `SSL_CAPATH` | 7.1, 7.3, Altibase 8.1 verified source | `NM` Network and security | L12729 NM | L12724 NM | L12984 NM | - |
| `SSL_CERT` | 7.1, 7.3, Altibase 8.1 verified source | `NM` Network and security | L12751 NM | L12746 NM | L13006 NM | - |
| `SSL_CIPHER_LIST` | 7.1, 7.3, Altibase 8.1 verified source | `NM` Network and security | L12773 NM | L12768 NM | L13028 NM | - |
| `SSL_CIPHER_SUITES` | 7.3, Altibase 8.1 verified source | `NM` Network and security | - | L12794 NM | L13054 NM | - |
| `SSL_CLIENT_AUTHENTICATION` | 7.1, 7.3, Altibase 8.1 verified source | `NM` Network and security | L12799 NM | L12816 NM | L13076 NM | - |
| `SSL_ENABLE` | 7.1, 7.3, Altibase 8.1 verified source | `NM` Network and security | L12825 NM | L12842 NM | L13102 NM | - |
| `SSL_KEY` | 7.1, 7.3, Altibase 8.1 verified source | `NM` Network and security | L12851 NM | L12868 NM | L13128 NM | - |
| `SSL_LOAD_CONFIG` | 7.3, Altibase 8.1 verified source | `NM` Network and security | - | L12892 NM | L13152 NM | - |
| `SSL_MAX_LISTEN` | 7.1, 7.3, Altibase 8.1 verified source | `NM` Network and security | L12875 NM | L12918 NM | L13178 NM | - |
| `SSL_PORT_NO` | 7.1, 7.3, Altibase 8.1 verified source | `NM` Network and security | L12897 NM | L12940 NM | L13200 NM | - |
| `TCP_ENABLE` | 7.1, 7.3, Altibase 8.1 verified source | `NM` Network and security | L12919 NM | L12962 NM | L13222 NM | - |
| `ALL_MSGLOG_FLUSH` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L12947 M | L12990 M | L13250 M | - |
| `CM_MSGLOG_COUNT` | 7.3, Altibase 8.1 verified source | `M` Message logging | - | L13038 M | L13298 M | - |
| `CM_MSGLOG_FILE` | 7.3, Altibase 8.1 verified source | `M` Message logging | - | L13060 M | L13320 M | - |
| `CM_MSGLOG_FLAG` | 7.3, Altibase 8.1 verified source | `M` Message logging | - | L13104 M | L13364 M | - |
| `CM_MSGLOG_SIZE` | 7.3, Altibase 8.1 verified source | `M` Message logging | - | L13082 M | L13342 M | - |
| `COLLECT_DUMP_INFO` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L12969 M | L13012 M | L13272 M | - |
| `DK_MSGLOG_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L12995 M | L13128 M | L13388 M | - |
| `DK_MSGLOG_FILE` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13017 M | L13150 M | L13410 M | - |
| `DK_MSGLOG_FLAG` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13039 M | L13172 M | L13432 M | - |
| `DK_MSGLOG_RESERVE_SIZE` | 7.3, Altibase 8.1 verified source | `M` Message logging | - | L13196 M | L13456 M | - |
| `DK_MSGLOG_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13063 M | L13218 M | L13478 M | - |
| `DUMP_MSGLOG_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13085 M | L13240 M | L13500 M | - |
| `DUMP_MSGLOG_FILE` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13107 M | L13262 M | L13522 M | - |
| `DUMP_MSGLOG_RESERVE_SIZE` | 7.3, Altibase 8.1 verified source | `M` Message logging | - | L13306 M | L13566 M | - |
| `DUMP_MSGLOG_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13129 M | L13284 M | L13544 M | - |
| `ERROR_MSGLOG_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13151 M | L13328 M | L13588 M | - |
| `ERROR_MSGLOG_FILE` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13173 M | L13350 M | L13610 M | - |
| `ERROR_MSGLOG_RESERVE_SIZE` | 7.3, Altibase 8.1 verified source | `M` Message logging | - | L13394 M | L13654 M | - |
| `ERROR_MSGLOG_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13195 M | L13372 M | L13632 M | - |
| `JOB_MSGLOG_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13576 M | L13416 M | L13676 M | - |
| `JOB_MSGLOG_FILE` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13598 M | L13438 M | L13698 M | - |
| `JOB_MSGLOG_FLAG` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13620 M | L13460 M | L13720 M | - |
| `JOB_MSGLOG_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13644 M | L13484 M | L13744 M | - |
| `LB_MSGLOG_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13218 M | L13506 M | L13766 M | - |
| `LB_MSGLOG_FILE` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13240 M | L13528 M | L13788 M | - |
| `LB_MSGLOG_FLAG` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13262 M | L13550 M | L13810 M | - |
| `LB_MSGLOG_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13292 M | L13580 M | L13840 M | - |
| `MM_MSGLOG_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13314 M | L13602 M | L13862 M | - |
| `MM_MSGLOG_FILE` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13336 M | L13624 M | L13884 M | - |
| `MM_MSGLOG_FLAG` | 7.3, Altibase 8.1 verified source | `M` Message logging | - | L13646 M | L13906 M | - |
| `MM_MSGLOG_RESERVE_SIZE` | 7.3, Altibase 8.1 verified source | `M` Message logging | - | L13670 M | L13930 M | - |
| `MM_MSGLOG_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13358 M | L13692 M | L13952 M | - |
| `MM_SESSION_LOGGING` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13380 M | L13714 M | L13974 M | - |
| `NETWORK_ERROR_LOG` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13402 M | L13736 M | L13996 M | - |
| `NETWORK_ERROR_LOG_FILE` | 7.3, Altibase 8.1 verified source | `M` Message logging | - | L13760 M | L14020 M | - |
| `QP_MSGLOG_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13426 M | L13782 M | L14042 M | - |
| `QP_MSGLOG_FILE` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13448 M | L13804 M | L14064 M | - |
| `QP_MSGLOG_FLAG` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13470 M | L13826 M | L14086 M | - |
| `QP_MSGLOG_RESERVE_SIZE` | 7.3, Altibase 8.1 verified source | `M` Message logging | - | L13850 M | L14110 M | - |
| `QP_MSGLOG_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13494 M | L13872 M | L14132 M | - |
| `QUERY_PROF_FLAG` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13516 M | L13894 M | L14154 M | - |
| `QUERY_PROF_LOG_DIR` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13552 M | L13930 M | L14190 M | - |
| `RP_CONFLICT_MSGLOG_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13666 M | L13954 M | L14214 M | - |
| `RP_CONFLICT_MSGLOG_DIR` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13688 M | L13976 M | L14236 M | - |
| `RP_CONFLICT_MSGLOG_ENABLE` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13711 M | L13998 M | L14258 M | - |
| `RP_CONFLICT_MSGLOG_FILE` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13733 M | L14020 M | L14280 M | - |
| `RP_CONFLICT_MSGLOG_FLAG` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13755 M | L14042 M | L14302 M | - |
| `RP_CONFLICT_MSGLOG_RESERVE_SIZE` | 7.3, Altibase 8.1 verified source | `M` Message logging | - | L14072 M | L14332 M | - |
| `RP_CONFLICT_MSGLOG_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13785 M | L14094 M | L14354 M | - |
| `RP_MSGLOG_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13807 M | L14116 M | L14376 M | - |
| `RP_MSGLOG_FILE` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13829 M | L14138 M | L14398 M | - |
| `RP_MSGLOG_FLAG` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13851 M | L14160 M | L14420 M | - |
| `RP_MSGLOG_RESERVE_SIZE` | 7.3, Altibase 8.1 verified source | `M` Message logging | - | L14184 M | L14444 M | - |
| `RP_MSGLOG_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13876 M | L14206 M | L14466 M | - |
| `SERVER_MSGLOG_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13898 M | L14228 M | L14488 M | - |
| `SERVER_MSGLOG_DIR` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13920 M | L14250 M | L14510 M | - |
| `SERVER_MSGLOG_FILE` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13944 M | L14274 M | L14535 M | - |
| `SERVER_MSGLOG_FLAG` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13968 M | L14298 M | L14559 M | - |
| `SERVER_MSGLOG_RESERVE_SIZE` | 7.3, Altibase 8.1 verified source | `M` Message logging | - | L14322 M | L14583 M | - |
| `SERVER_MSGLOG_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L13993 M | L14344 M | L14605 M | - |
| `SM_MSGLOG_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L14015 M | L14366 M | L14627 M | - |
| `SM_MSGLOG_FILE` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L14037 M | L14388 M | L14649 M | - |
| `SM_MSGLOG_FLAG` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L14059 M | L14410 M | L14671 M | - |
| `SM_MSGLOG_RESERVE_SIZE` | 7.3, Altibase 8.1 verified source | `M` Message logging | - | L14432 M | L14693 M | - |
| `SM_MSGLOG_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L14082 M | L14454 M | L14715 M | - |
| `ST_MSGLOG_COUNT` | 7.3, Altibase 8.1 verified source | `M` Message logging | - | L14502 M | L14763 M | - |
| `ST_MSGLOG_FILE` | 7.3, Altibase 8.1 verified source | `M` Message logging | - | L14524 M | L14785 M | - |
| `ST_MSGLOG_FLAG` | 7.3, Altibase 8.1 verified source | `M` Message logging | - | L14476 M | L14737 M | - |
| `ST_MSGLOG_SIZE` | 7.3, Altibase 8.1 verified source | `M` Message logging | - | L14546 M | L14807 M | - |
| `TRCLOG_DETAIL_PREDICATE` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L14104 M | L14590 M | L14851 M | - |
| `TRC_MSGLOG_RESERVE_SIZE` | 7.3, Altibase 8.1 verified source | `M` Message logging | - | L14568 M | L14829 M | - |
| `XA_MSGLOG_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L14128 M | L14614 M | L14875 M | - |
| `XA_MSGLOG_FILE` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L14150 M | L14636 M | L14897 M | - |
| `XA_MSGLOG_FLAG` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L14172 M | L14658 M | L14919 M | - |
| `XA_MSGLOG_RESERVE_SIZE` | 7.3, Altibase 8.1 verified source | `M` Message logging | - | L14688 M | L14949 M | - |
| `XA_MSGLOG_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `M` Message logging | L14202 M | L14710 M | L14971 M | - |
| `DBLINK_ALTILINKER_CONNECT_TIMEOUT` | 7.1, 7.3, Altibase 8.1 verified source | `L` Database link | L14226 L | L14734 L | L14995 L | - |
| `DBLINK_DATA_BUFFER_ALLOC_RATIO` | 7.1, 7.3, Altibase 8.1 verified source | `L` Database link | L14248 L | L14756 L | L15017 L | - |
| `DBLINK_DATA_BUFFER_BLOCK_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `L` Database link | L14270 L | L14778 L | L15039 L | - |
| `DBLINK_DATA_BUFFER_BLOCK_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `L` Database link | L14292 L | L14800 L | L15061 L | - |
| `DBLINK_ENABLE` | 7.1, 7.3, Altibase 8.1 verified source | `L` Database link | L14314 L | L14822 L | L15083 L | - |
| `DBLINK_GLOBAL_TRANSACTION_LEVEL` | 7.1, 7.3, Altibase 8.1 verified source | `L` Database link | L14336 L | L14844 L | L15105 L | - |
| `DBLINK_RECOVERY_MAX_LOGFILE` | 7.1, 7.3, Altibase 8.1 verified source | `L` Database link | L14364 L | L14872 L | L15133 L | - |
| `DBLINK_REMOTE_STATEMENT_AUTOCOMMIT` | 7.1, 7.3, Altibase 8.1 verified source | `L` Database link | L14388 L | L14896 L | L15157 L | - |
| `DBLINK_REMOTE_TABLE_BUFFER_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `L` Database link | L14416 L | L14924 L | L15185 L | - |
| `AUDIT_FILE_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `U` Auditing | L14442 U | L14950 U | L15211 U | - |
| `AUDIT_LOG_DIR` | 7.1, 7.3, Altibase 8.1 verified source | `U` Auditing | L14472 U | L14980 U | L15241 U | - |
| `AUDIT_OUTPUT_METHOD` | 7.1, 7.3, Altibase 8.1 verified source | `U` Auditing | L14502 U | L15010 U | L15271 U | - |
| `AUDIT_TAG_NAME_IN_SYSLOG` | 7.1, 7.3, Altibase 8.1 verified source | `U` Auditing | L14546 U | L15054 U | L15315 U | - |
| `EXTPROC_AGENT_CALL_RETRY_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `A` C/C++ external procedure agent | L14592 A | L15100 A | L15361 A | - |
| `EXTPROC_AGENT_CONNECT_TIMEOUT` | 7.1, 7.3, Altibase 8.1 verified source | `A` C/C++ external procedure agent | L14570 A | L15078 A | L15339 A | - |
| `EXTPROC_AGENT_IDLE_TIMEOUT` | 7.1, 7.3, Altibase 8.1 verified source | `A` C/C++ external procedure agent | L14618 A | L15126 A | L15387 A | - |
| `EXTPROC_AGENT_SOCKET_FILEPATH` | 7.1, 7.3, Altibase 8.1 verified source | `A` C/C++ external procedure agent | L14640 A | L15148 A | L15409 A | - |
| `CASE_SENSITIVE_PASSWORD` | 7.1, 7.3, Altibase 8.1 verified source | `AS` Account security | L14668 AS | L15176 AS | L15437 AS | - |
| `FAILED_LOGIN_ATTEMPTS` | 7.1, 7.3, Altibase 8.1 verified source | `AS` Account security | L14695 AS | L15203 AS | L15464 AS | - |
| `PASSWORD_GRACE_TIME` | 7.1, 7.3, Altibase 8.1 verified source | `AS` Account security | L14761 AS | L15269 AS | L15530 AS | - |
| `PASSWORD_LIFE_TIME` | 7.1, 7.3, Altibase 8.1 verified source | `AS` Account security | L14739 AS | L15247 AS | L15508 AS | - |
| `PASSWORD_LOCK_TIME` | 7.1, 7.3, Altibase 8.1 verified source | `AS` Account security | L14717 AS | L15225 AS | L15486 AS | - |
| `PASSWORD_REUSE_MAX` | 7.1, 7.3, Altibase 8.1 verified source | `AS` Account security | L14805 AS | L15313 AS | L15574 AS | - |
| `PASSWORD_REUSE_TIME` | 7.1, 7.3, Altibase 8.1 verified source | `AS` Account security | L14783 AS | L15291 AS | L15552 AS | - |
| `PASSWORD_VERIFY_FUNCTION` | 7.1, 7.3, Altibase 8.1 verified source | `AS` Account security | L14827 AS | L15335 AS | L15596 AS | - |
| `ACCESS_LIST` | 7.1, 7.3, Altibase 8.1 verified source | `E` Other | L14851 E | L15359 E | L15620 E | - |
| `ACCESS_LIST_FILE` | 7.1, 7.3, Altibase 8.1 verified source | `E` Other | L14938 E | L15444 E | L15705 E | - |
| `ADMIN_MODE` | 7.1, 7.3, Altibase 8.1 verified source | `E` Other | L14962 E | L15468 E | L15729 E | - |
| `ARITHMETIC_OPERATION_MODE` | 7.1, 7.3, Altibase 8.1 verified source | `E` Other | L14992 E | L15498 E | L15759 E | - |
| `CHECK_MUTEX_DURATION_TIME_ENABLE` | 7.1, 7.3, Altibase 8.1 verified source | `E` Other | L15018 E | L15524 E | L15785 E | - |
| `COERCE_HOST_VAR_IN_SELECT_LIST_TO_VARCHAR` | 7.1, 7.3, Altibase 8.1 verified source | `E` Other | L15046 E | L15552 E | L15813 E | - |
| `DEFAULT_DATE_FORMAT` | 7.1, 7.3, Altibase 8.1 verified source | `E` Other | L15072 E | L15578 E | L15839 E | - |
| `EXEC_DDL_DISABLE` | 7.1, 7.3, Altibase 8.1 verified source | `E` Other | L15103 E | L15609 E | L15870 E | - |
| `GROUP_CONCAT_PRECISION` | 7.1, 7.3, Altibase 8.1 verified source | `E` Other | L15129 E | L15635 E | L15896 E | - |
| `JOB_SCHEDULER_ENABLE` | 7.1, 7.3, Altibase 8.1 verified source | `E` Other | L15153 E | L15659 E | L15920 E | - |
| `JOB_THREAD_COUNT` | 7.1, 7.3, Altibase 8.1 verified source | `E` Other | L15181 E | L15687 E | L15948 E | - |
| `JOB_THREAD_QUEUE_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `E` Other | L15203 E | L15709 E | L15970 E | - |
| `LISTAGG_PRECISION` | 7.1, 7.3, Altibase 8.1 verified source | `E` Other | L15225 E | L15731 E | L15992 E | - |
| `MEMORY_TEMPLOB_MAX_ALLOC_SIZE` | Altibase 8.1 verified source | `E` Other | - | - | L16014 E | - |
| `MEMORY_TEMPLOB_PIECE_SIZE` | Altibase 8.1 verified source | `E` Other | - | - | L16038 E | - |
| `MSG_QUEUE_PERMISSION` | 7.1, 7.3, Altibase 8.1 verified source | `E` Other | L15247 E | L15753 E | L16060 E | - |
| `PSM_CASE_SENSITIVE_MODE` | 7.1, 7.3, Altibase 8.1 verified source | `E` Other | L15317 E | L15823 E | L16130 E | - |
| `PSM_CHAR_DEFAULT_PRECISION` | 7.1, 7.3, Altibase 8.1 verified source | `E` Other | L15340 E | L15846 E | L16153 E | - |
| `PSM_IGNORE_NO_DATA_FOUND_ERROR` | 7.1, 7.3, Altibase 8.1 verified source | `E` Other | L15366 E | L15871 E | L16179 E | - |
| `PSM_MAX_DDL_REFERENCE_DEPTH` | 7.3, Altibase 8.1 verified source | `E` Other | - | L15898 E | L16206 E | - |
| `PSM_NCHAR_UTF16_DEFAULT_PRECISION` | 7.1, 7.3, Altibase 8.1 verified source | `E` Other | L15393 E | L15920 E | L16228 E | - |
| `PSM_NCHAR_UTF8_DEFAULT_PRECISION` | 7.1, 7.3, Altibase 8.1 verified source | `E` Other | L15418 E | L15945 E | L16253 E | - |
| `PSM_NVARCHAR_UTF16_DEFAULT_PRECISION` | 7.1, 7.3, Altibase 8.1 verified source | `E` Other | L15443 E | L15970 E | L16278 E | - |
| `PSM_NVARCHAR_UTF8_DEFAULT_PRECISION` | 7.1, 7.3, Altibase 8.1 verified source | `E` Other | L15468 E | L15995 E | L16303 E | - |
| `PSM_PARAM_AND_RETURN_WITHOUT_PRECISION_ENABLE` | 7.1, 7.3, Altibase 8.1 verified source | `E` Other | L15493 E | L16020 E | L16328 E | - |
| `PSM_VARCHAR_DEFAULT_PRECISION` | 7.1, 7.3, Altibase 8.1 verified source | `E` Other | L15525 E | L16052 E | L16360 E | - |
| `QUERY_STACK_SIZE` | 7.1, 7.3, Altibase 8.1 verified source | `E` Other | L15550 E | L16077 E | L16385 E | - |
| `RECURSION_LEVEL_MAXIMUM` | 7.1, 7.3, Altibase 8.1 verified source | `E` Other | L15580 E | L16107 E | L16415 E | - |
| `REGEXP_MODE` | 7.1, 7.3, Altibase 8.1 verified source | `E` Other | L15604 E | L16131 E | L16439 E | - |
| `REMOTE_SYSDBA_ENABLE` | 7.1, 7.3, Altibase 8.1 verified source | `E` Other | L15640 E | L16167 E | L16475 E | - |
| `SELECT_HEADER_DISPLAY` | 7.1, 7.3, Altibase 8.1 verified source | `E` Other | L15666 E | L16193 E | L16501 E | - |
| `SYS_CONNECT_BY_PATH_PRECISION` | 7.1, 7.3, Altibase 8.1 verified source | `E` Other | L15690 E | L16217 E | L16525 E | - |
| `TEMPORARY_LOB_ENABLE` | Altibase 8.1 verified source | `E` Other | - | - | L16549 E | - |
| `TRC_ACCESS_PERMISSION` | 7.1, 7.3, Altibase 8.1 verified source | `E` Other | L15714 E | L16241 E | L16574 E | - |
| `VARRAY_MEMORY_MAXIMUM` | 7.3, Altibase 8.1 verified source | `E` Other | - | L16266 E | L16599 E | - |

## Later-Job Handoff

- Use this report as the canonical property-name/version baseline for J005-J009 property expansion and QA work.
- J005 has expanded the initialization/path/memory/disk/volatile/log/storage subset in `GPTs/attachments/05_data_types_properties.md`; later property jobs should avoid re-opening that subset unless exact-version source review finds a default, range, or alter-level drift.
- When adding a customer-facing property block, keep the version scope from this inventory, then source the default, range, dynamic-change support, change method, and cautions from the target version manual section and `V$PROPERTY` check patterns.
- If a later job finds a property name in a selected General Reference 1 source that is absent from this inventory, update this report and split or amend `GAP-J004-001` in `GPTs/reports/gap_register.md`.
- For properties listed here but not yet decomposed in `GPTs/attachments/05_data_types_properties.md`, answer with the property-name/version availability, ask for the exact installed version when defaults or runtime behavior matter, and verify details through `V$PROPERTY` and the target version manual instead of inventing values.
- After J009, unresolved property-detail work is not a missing-name problem: it is a
  lower-retrieval detail-block gap for inventoried names that still lack full
  source-backed defaults, ranges, dynamic-change methods, related views, and cautions
  in the customer-facing attachment. Track those remaining details through
  `GPTs/reports/gap_register.md`.
