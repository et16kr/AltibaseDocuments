# SQL And Data Types Playbook

- Playbook ID: `APB-000003`
- Owning job: `S2-J003`
- Validation status: `pass`
- Supported versions: Altibase 7.1, Altibase 7.3, and `Altibase 8.1 verified source`
- Protected topic: yes

## Source Routes

| Route | Source IDs | Source-pack block refs | Baseline blocks |
| --- | --- | --- | --- |
| SQL, DML, functions, expressions, data types, LOB, JSON, and type validation | `SRC-000056`, `SRC-000025`, `SRC-000120`, `SRC-000089`, `SRC-000180`, `SRC-000150`, `SRC-000072`, `SRC-000040`, `SRC-000134`, `SRC-000103`, `SRC-000194`, `SRC-000163` | `SRC-000056/BLOCK-000515`, `SRC-000025/BLOCK-000514`, `SRC-000120/BLOCK-000517`, `SRC-000089/BLOCK-000516`, `SRC-000180/BLOCK-000519`, `SRC-000150/BLOCK-000518`, `SRC-000072/BLOCK-000884`, `SRC-000040/BLOCK-000883`, `SRC-000134/BLOCK-000886`, `SRC-000103/BLOCK-000885`, `SRC-000194/BLOCK-000888`, `SRC-000163/BLOCK-000887` | `KAE-BLOCK-000273` |

Guardrail: `CONF-000005` remains open. The playbook can draft SQL and data
type artifacts, but exact syntax diagrams, full function lists, full type
conversion matrices, full property rows, full view columns, and exact error
maps require the exact target-version source block.

Forbidden assumption note: do not complete Altibase SQL by analogy with
Oracle, MySQL, PostgreSQL, or ANSI SQL. Preserve only Altibase-source-backed
syntax and restrictions.

## Required Customer Inputs

Collect these before generating SQL, DML, or data type artifacts:

- Target Altibase version and patch level.
- Existing table DDL, column data types, constraints, indexes, triggers,
  partitions, replication membership, and LOB or JSON columns.
- Statement goal: read query, write DML, type selection, function conversion,
  expression generation, test case, or validation query.
- Input data types, expected return type, sample data, expected rows,
  transaction boundaries, autocommit state, and rollback need.
- Predicate, join condition, `MERGE` `ON` condition, source rows, uniqueness
  expectation, and expected affected row count for write DML.
- Whether the request depends on JSON, Temporary LOB, regular expressions,
  Oracle-overlap syntax, or other version-sensitive behavior.

## Generated Artifacts

This playbook may draft:

- `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `MOVE`, `MERGE`, `ENQUEUE`, and
  `DEQUEUE` first drafts.
- Read-only validation queries for dictionary and performance views.
- Data type decision notes for character, numeric, datetime, binary, LOB, and
  `Altibase 8.1 verified source` `JSON` data.
- LOB and JSON checks, including table and tablespace suitability checks.
- Test SQL with setup, expected results, negative cases, and cleanup notes.

Do not generate DML against dictionary tables or performance views unless a
source-backed writable object route exists. Use `SELECT` for dictionary and
performance views.

## Procedure

1. Confirm target version and source route. For 7.1 or 7.3, do not generate
   native `JSON`, `TEMPORARY_LOB_ENABLE`,
   `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`, `MEMORY_TEMPLOB_PIECE_SIZE`, or
   `V$TEMPORARY_LOBS` unless exact installed-version proof is supplied.
2. Classify the artifact as read SQL, write DML, data type selection, function
   expression, or validation test.
3. Preserve Altibase statement tokens: `SELECT`, `INSERT`, `UPDATE`,
   `DELETE`, `MOVE`, `MERGE`, `ENQUEUE`, `DEQUEUE`, `COMMIT`, `ROLLBACK`,
   `SAVEPOINT`, and `SET TRANSACTION`.
4. For write DML, require an expected affected-row count, predicate, rollback
   plan, and validation query before producing a runnable statement.
5. For functions and expressions, preserve source tokens such as `CAST`,
   `LIKE`, `BETWEEN`, `IN`, `EXISTS`, `IS NULL`, `IS JSON`,
   `REGEXP_LIKE`, `REGEXP_REPLACE`, `REGEXP_SUBSTR`, `GROUP_CONCAT`,
   `LISTAGG`, `DECODE`, `NVL2`, `CURRVAL`, `NEXTVAL`, and `ROWNUM`.
6. For Oracle-overlap syntax, map only source-backed Altibase behavior. The
   source route includes both `LEFT OUTER JOIN`, `RIGHT OUTER JOIN`,
   `FULL OUTER JOIN`, and `(+)` where applicable, but it does not authorize
   broad Oracle behavior.
7. Attach validation SQL and cleanup notes to every generated artifact.

## Data Type Route

Preserve exact source tokens when choosing data types:

- Character: `CHAR`, `VARCHAR`, `NCHAR`, `NVARCHAR`.
- Numeric: `BIGINT`, `DECIMAL`, `DOUBLE`, `FLOAT`, `INTEGER`, `NUMBER`,
  `NUMERIC`, `REAL`, `SMALLINT`.
- Date/time: `DATE`.
- Binary and bit: `BYTE`, `VARBYTE`, `NIBBLE`, `BIT`, `VARBIT`.
- LOB: `BLOB`, `CLOB`, `IN ROW size`, `DISK_LOB_COLUMN_IN_ROW_SIZE`,
  `MEMORY_LOB_COLUMN_IN_ROW_SIZE`, `LOB_OBJECT_BUFFER_SIZE`,
  `LOB_CACHE_THRESHOLD`.
- JSON: `JSON` only inside `Altibase 8.1 verified source` scope unless exact
  installed-version evidence proves availability.

Important boundaries:

- `BIGINT` ranges from `-9223372036854775807` to `9223372036854775807`.
- `FLOAT` precision ranges from `1` to `38`; omitted precision defaults to
  `38`.
- `NUMBER` and `NUMERIC` omit precision as `38` and omit scale as `0`.
- One LOB column can store up to `4GB-1byte`.
- LOB columns cannot be index keys, partition keys, or cursor columns, and
  cannot be used in volatile tablespaces or disk temporary tablespaces.
- `JSON` has maximum depth `256`, maximum size `2GB (2,147,483,648 bytes)`,
  and cannot be used in `SELECT FOR UPDATE` in this baseline route.

## Artifact Templates

```sql
-- 00_sql_precheck.sql
SELECT * FROM V$VERSION;

SELECT NAME, SLOTSIZE, COLUMNCOUNT
FROM V$TABLE
WHERE NAME IN ('<TARGET_TABLE>', 'V$PROPERTY', 'V$ALLCOLUMN')
ORDER BY NAME;

SELECT TABLENAME, COLNAME
FROM V$ALLCOLUMN
WHERE TABLENAME = '<TARGET_TABLE>'
ORDER BY COLNAME;
```

```sql
-- 10_read_query_first_draft.sql
-- Confirm columns with V$ALLCOLUMN before running.
SELECT <column_list>
FROM <schema_name>.<table_name>
WHERE <source_backed_predicate>
ORDER BY <stable_sort_column>;
```

```sql
-- 20_write_dml_first_draft.sql
-- Non-production first draft. Confirm candidate row count before write DML.
SELECT COUNT(*) AS candidate_rows
FROM <schema_name>.<table_name>
WHERE <required_predicate>;

SAVEPOINT <before_change_savepoint>;

UPDATE <schema_name>.<table_name>
SET <column_name> = <source_backed_value_expression>
WHERE <required_predicate>;

SELECT COUNT(*) AS changed_rows
FROM <schema_name>.<table_name>
WHERE <post_change_predicate>;

-- Commit or rollback only after customer approval and validation.
-- COMMIT;
-- ROLLBACK;
```

```sql
-- 30_merge_first_draft.sql
MERGE INTO <target_schema>.<target_table> t
USING <source_query_or_table> s
ON (<source_backed_match_condition>)
WHEN MATCHED THEN
  UPDATE SET <target_column> = <source_expression>
WHEN NOT MATCHED THEN
  INSERT (<column_list>)
  VALUES (<value_expression_list>);
```

## Guardrails

- Write DML must include a predicate, candidate row count, expected affected
  row count, transaction plan, and validation query. Stop if the statement
  would affect all rows without explicit confirmation.
- Do not combine source-restricted `multiple_delete` or `multiple_update`
  forms with `limit_clause` or `returning_clause`; do not use dictionary
  tables or `full outer join` in those forms.
- For the DML `returning_clause`, preserve restrictions from the source route:
  table only, no aggregate functions in `expr`, no LOB type return, no aliases
  or subqueries in `expr`, no sequences in `expr`, and matching host or PSM
  variable counts and types.
- Do not promise rollback of DDL or truncation behavior from this playbook.
  Route DDL and truncation to `APB-000002`.
- For regular expressions, ask for `REGEXP_MODE`, exact input data, expected
  match behavior, and target version.
- For JSON functions, stay inside `Altibase 8.1 verified source` unless
  customer evidence proves availability in the installed version.

## Validation Checks

Attach the relevant checks:

- Version and feature check: `V$VERSION`, `V$PROPERTY`.
- Table and column check: `V$TABLE`, `V$ALLCOLUMN`.
- Type-sensitive check: sample input rows, expected output rows, and explicit
  casts or return types.
- DML safety check: pre-change count, post-change count, transaction decision,
  and cleanup.
- LOB or JSON check: table type, tablespace type, in-row size, memory limit,
  and client API behavior supplied by the customer.

## Stop Conditions

Stop and ask for more input if:

- Target version, table DDL, data types, expected result, predicate, or row
  count is missing.
- The request needs exact function syntax, complete conversion matrices, or
  exhaustive SQL grammar from this playbook alone.
- The target is 7.1 or 7.3 and the request depends on native `JSON`,
  Temporary LOB, or `V$TEMPORARY_LOBS`.
- The requested DML targets dictionary tables or performance views without a
  source-backed writable object route.
- The answer depends on live data volume, runtime errors, patch behavior,
  client binding behavior, or logs that the customer has not supplied.
