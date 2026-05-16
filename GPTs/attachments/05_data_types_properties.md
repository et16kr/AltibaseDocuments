# 05. Data Types and Properties

## Applicable Versions

- 7.1: Based on Altibase 7.1 General Reference 1.
- 7.3: Based on Altibase 7.3 General Reference 1.
- 8.1: Based on Altibase 8.1 verified source General Reference 1 and Altibase 8.1 Release Notes.

## Questions This File Can Answer

- Which Altibase data type should be used for character, numeric, date/time, binary, LOB, spatial, or JSON data?
- What are the practical differences between Altibase data types and familiar Oracle data types?
- How do `FIXED`, `VARIABLE`, and `IN ROW` affect column storage?
- What are the 8.1 `JSON` data type and Temporary LOB features?
- Which LOB, JSON, Temporary LOB, PSM default-precision, VARRAY, and object-size properties should be checked?
- Where are Altibase server properties checked, and how are static and dynamic property changes applied?
- Which SQL should be used to inspect a property, change a dynamic property, and verify the related system view?
- What do properties such as `LOG_FILE_SIZE`, `TEMPORARY_LOB_ENABLE`, `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`, and `REPLICATION_SSL_PORT_NO` mean?

## Source Documents

- 7.1: Altibase 7.1 General Reference 1.
- 7.3: Altibase 7.3 General Reference 1.
- 8.1: Altibase 8.1 verified source General Reference 1; Altibase 8.1 Release Notes.

## Core Guidance

- Answer in the user's language, but keep SQL object names, data type names, function names, error codes, property names, commands, and file paths literal.
- If the customer specifies a version, use that version's data types and property definitions. If no version is specified, use the 8.1 baseline and call out features that do not exist in 7.1 or 7.3.
- For data type questions, identify the data shape, maximum size, storage target, and whether Oracle compatibility matters.
- For property questions, answer with `Meaning`, `Default`, `Dynamic Change Support`, `Range`, and `Check SQL`.
- For property change questions, include pre-change SQL, the correct `ALTER SYSTEM` or `ALTER SESSION` form only when the property supports it, post-change SQL, and any restart or recreation requirement.
- Do not expose internal source labels. Refer to the 8.1 source family as `Altibase 8.1 verified source`.
- Do not keep large source tables as-is. Convert them into searchable data type or property item blocks.

## Version Differences

- 7.1 and 7.3: Core data types are character, numeric, `DATE`, binary, `BLOB`, `CLOB`, and `GEOMETRY`. Native `JSON` and Temporary LOB are not part of these baselines.
- 8.1: Adds native `JSON`, JSON path-expression support, JSON generation/search/validation functions, and Temporary LOB support.
- 8.1: Adds or documents new properties including `CHECKPOINT_SCALE_SINGLE_DW_BUFFER_SIZE`, `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`, `MEMORY_TEMPLOB_PIECE_SIZE`, `REPLICATION_SSL_PORT_NO`, `TEMPORARY_LOB_ENABLE`, `TRCLOG_EXPLAIN_TYPE`, and `TRCLOG_JSON_PLAN_INDENT_DEPTH`.
- Cross-version property caution: `PSM_CASE_SENSITIVE_MODE` and `REGEXP_MODE` are documented in Altibase 7.x and 8.1 source documents. Do not label them as 8.1-only unless the customer asks about a target build where the installed documentation proves a narrower scope.
- 8.1: Release notes record changed defaults or ranges for `CHECKPOINT_INTERVAL_IN_LOG`, `FAST_START_LOGFILE_TARGET`, `LOG_CREATE_METHOD`, `LOG_FILE_SIZE`, `MEMORY_INDEX_BUILD_RUN_SIZE`, `MEMORY_INDEX_BUILD_VALUE_LENGTH_THRESHOLD`, and `OPTIMIZER_FEATURE_ENABLE`.
- 8.1: Release notes list `INSPECTION_LARGE_HEAP_THRESHOLD` as removed.

## Data Type Selection Flow

```mermaid
flowchart TD
  A[Choose column type] --> B{Stores JSON document?}
  B -->|Yes, 8.1| C[Use JSON]
  B -->|Yes, 7.1 or 7.3| D[Use character or LOB design]
  B -->|No| E{Value family}
  E --> F[Large object]
  E --> G[Text]
  E --> H[Numeric]
  E --> I[Date, binary, bit, or spatial]
```

Selection details:

1. Use `JSON` for native JSON documents on 8.1 and enable Temporary LOB behavior when the JSON workflow requires it.
2. Use character or LOB design, not native `JSON`, for JSON-like data on 7.1 or 7.3.
3. Use `CLOB` or `BLOB` for large text or binary objects.
4. Use `CHAR`, `VARCHAR`, `NCHAR`, or `NVARCHAR` for ordinary text.
5. Use exact numeric types such as `NUMERIC`, `DECIMAL`, `NUMBER(p,s)`, `INTEGER`, `BIGINT`, or `SMALLINT` when exact scale matters.
6. Use approximate numeric types such as `FLOAT`, `DOUBLE`, `REAL`, or `NUMBER` without precision when approximate values are acceptable.
7. Use `DATE` for date/time values, `BYTE`, `VARBYTE`, `NIBBLE`, `BIT`, or `VARBIT` for binary or bit strings, and `GEOMETRY` for spatial values.

## Compact Data Type Syntax

These patterns are generation guides, not a replacement for the full SQL Reference grammar.

```text
character_type ::=
  CHAR[(size)] [FIXED | VARIABLE [IN ROW size]]
  | VARCHAR[(size)] [FIXED | VARIABLE [IN ROW size]]
  | NCHAR[(size)] [FIXED | VARIABLE [IN ROW size]]
  | NVARCHAR[(size)] [FIXED | VARIABLE [IN ROW size]]

numeric_type ::=
  BIGINT
  | INTEGER
  | SMALLINT
  | DOUBLE
  | REAL
  | FLOAT[(precision)]
  | NUMERIC[(precision[, scale])]
  | DECIMAL[(precision[, scale])]
  | NUMBER[(precision[, scale])]

date_type ::= DATE

binary_type ::=
  BYTE[(size)] [[FIXED |] VARIABLE (IN ROW size)]
  | VARBYTE[(size)] [[FIXED |] VARIABLE (IN ROW size)]
  | NIBBLE[(size)] [[FIXED |] VARIABLE (IN ROW size)]
  | BIT[(size)] [[FIXED |] VARIABLE (IN ROW size)]
  | VARBIT[(size)] [[FIXED |] VARIABLE (IN ROW size)]

lob_type ::=
  BLOB [IN ROW size]
  | CLOB [IN ROW size]

json_type_8_1 ::=
  JSON [IN ROW size]
```

## Storage Modifiers

### Modifier Item: `FIXED`

Purpose: keep the column data in the fixed area of a record when the table is in a memory tablespace.

Use when: the column is short and predictable, or when avoiding variable-area lookup is more important than saving memory.

Notes:

- For disk tables, user-specified `FIXED` or `VARIABLE` is ignored and columns are treated as fixed.
- LOB column data is treated as variable storage behavior, but do not write `VARIABLE` in `BLOB` or `CLOB` type syntax; control small LOB placement with `IN ROW`.

### Modifier Item: `VARIABLE`

Purpose: store column payload separately from the fixed part of a record, while the fixed part stores length and pointer information.

Use when: values vary widely or can be large.

Supported types: `CHAR`, `VARCHAR`, `NCHAR`, `NVARCHAR`, `BYTE`, `VARBYTE`, `NIBBLE`, `BIT`, and `VARBIT`.

### Modifier Item: `IN ROW`

Purpose: keep small variable or LOB values in the fixed area when their stored size is less than or equal to the `IN ROW` threshold.

Use when: many rows contain small values, but occasional rows contain larger values.

Default-related properties:

- `MEMORY_VARIABLE_COLUMN_IN_ROW_SIZE`: default threshold for non-LOB variable columns in memory tables.
- `MEMORY_LOB_COLUMN_IN_ROW_SIZE`: default threshold for LOB columns in memory tables.
- `DISK_LOB_COLUMN_IN_ROW_SIZE`: default threshold for LOB columns in disk tables.

## Data Type Item Blocks

### Type Item: `CHAR`

Purpose: fixed-length character data in the database character set.

Syntax:

```sql
CHAR[(size)] [FIXED | VARIABLE [IN ROW size]]
```

Limits and storage:

- Default size is `1` byte.
- Maximum size is `32000` bytes.
- Values shorter than the declared size are padded with blanks.

Use when: the value has a stable fixed length, such as fixed-format codes.

### Type Item: `VARCHAR`

Purpose: variable-length character data in the database character set.

Syntax:

```sql
VARCHAR[(size)] [FIXED | VARIABLE [IN ROW size]]
```

Limits and storage:

- Default size is `1` byte.
- Maximum size is `32000` bytes.
- Stores only the actual input length plus length metadata, unless fixed-area storage applies.

Use when: ordinary text length varies and does not require the national character set.

Oracle mapping note: Oracle `VARCHAR2` commonly maps to Altibase `VARCHAR`, after checking the 32000-byte limit and character set.

### Type Item: `NCHAR`

Purpose: fixed-length Unicode character data in the national character set.

Syntax:

```sql
NCHAR[(size)] [FIXED | VARIABLE [IN ROW size]]
```

Limits and storage:

- Maximum length is `16000` characters for UTF16 national character set.
- Maximum length is `10666` characters for UTF8 national character set.
- UTF16 uses 2 bytes per character; UTF8 varies from 1 to 3 bytes per character.

Use when: fixed-length national character data is required.

### Type Item: `NVARCHAR`

Purpose: variable-length Unicode character data in the national character set.

Syntax:

```sql
NVARCHAR[(size)] [FIXED | VARIABLE [IN ROW size]]
```

Limits and storage:

- Maximum length is `16000` characters for UTF16 national character set.
- Maximum length is `10666` characters for UTF8 national character set.
- Like `VARCHAR`, it stores the actual input length plus metadata unless fixed-area storage applies.

Use when: variable-length Unicode text is required.

Oracle mapping note: Oracle `NVARCHAR2` commonly maps to Altibase `NVARCHAR`.

### Type Item: `BIGINT`

Purpose: 8-byte integer.

Syntax:

```sql
BIGINT
```

Range: `-9223372036854775807` through `9223372036854775807`.

Use when: exact integer values exceed the `INTEGER` range.

### Type Item: `INTEGER`

Purpose: 4-byte integer.

Syntax:

```sql
INTEGER
```

Range: `-2147483647` through `2147483647`.

Use when: ordinary exact integer values fit in 4 bytes.

### Type Item: `SMALLINT`

Purpose: 2-byte integer.

Syntax:

```sql
SMALLINT
```

Range: `-32767` through `32767`.

Use when: compact small integer storage is sufficient.

### Type Item: `NUMERIC`

Purpose: exact fixed decimal.

Syntax:

```sql
NUMERIC[(precision[, scale])]
```

Limits and defaults:

- `precision`: `1` through `38`.
- `scale`: `-84` through `128`.
- If precision is omitted, default precision is `38`.
- If scale is omitted, default scale is `0`.

Use when: exact decimal semantics are required, such as financial values.

### Type Item: `DECIMAL`

Purpose: exact fixed decimal.

Syntax:

```sql
DECIMAL[(precision[, scale])]
```

Behavior: same as `NUMERIC`.

Use when: source DDL uses `DECIMAL` and exact fixed decimal semantics are required.

### Type Item: `NUMBER`

Purpose: Oracle-familiar numeric declaration with Altibase-specific behavior.

Syntax:

```sql
NUMBER[(precision[, scale])]
```

Behavior:

- `NUMBER(p,s)` behaves like exact fixed decimal `NUMERIC(p,s)`.
- `NUMBER` with no precision and scale behaves like `FLOAT`.

Migration caution: do not map Oracle `NUMBER` blindly. Decide whether the source column is exact integer, exact decimal, or approximate numeric.

### Type Item: `FLOAT`

Purpose: non-native floating-point numeric with decimal precision.

Syntax:

```sql
FLOAT[(precision)]
```

Limits and defaults:

- Precision is `1` through `38`.
- Default precision is `38`.
- Value range for 7.1, 7.3, and 8.1 is approximately `-1E-120` through `1E+120`.

Use when: approximate numeric behavior is acceptable.

### Type Item: `DOUBLE`

Purpose: 8-byte native floating-point value.

Syntax:

```sql
DOUBLE
```

Use when: C `double`-like approximate numeric storage is desired.

### Type Item: `REAL`

Purpose: 4-byte native floating-point value.

Syntax:

```sql
REAL
```

Use when: C `float`-like approximate numeric storage is sufficient.

### Type Item: `DATE`

Purpose: date and time information.

Syntax:

```sql
DATE
```

Limits and storage:

- Stored in 8 bytes.
- Typical supported date range is `0001/01/01` through `9999/12/31`, subject to system behavior.
- Display and input formatting are controlled by date format strings and `DEFAULT_DATE_FORMAT`.

Oracle mapping note: Oracle `DATE` maps naturally to Altibase `DATE` for date and time values, but confirm fractional-second and timezone requirements before migration.

### Type Item: `BYTE`

Purpose: fixed-length hexadecimal byte data.

Syntax:

```sql
BYTE[(size)] [[FIXED |] VARIABLE (IN ROW size)]
```

Limits and storage:

- Default size is `1` byte.
- Maximum size is `32000` bytes.
- Two hexadecimal characters represent one byte.
- Values shorter than the declared size are padded on the right with `0`.

Use when: fixed-length binary values are needed.

### Type Item: `VARBYTE`

Purpose: variable-length hexadecimal byte data.

Syntax:

```sql
VARBYTE[(size)] [[FIXED |] VARIABLE (IN ROW size)]
```

Limits and storage:

- Default size is `1` byte.
- Maximum size is `32000` bytes.
- Two hexadecimal characters represent one byte.

Use when: Oracle `RAW`-like values vary in length and fit the Altibase limit.

### Type Item: `NIBBLE`

Purpose: hexadecimal data where each character is one nibble.

Syntax:

```sql
NIBBLE[(size)] [[FIXED |] VARIABLE (IN ROW size)]
```

Limits and storage:

- Maximum size is `254` nibbles.
- Allowed characters are `0` through `9` and `A` through `F`; lower-case `a` through `f` are stored as upper-case.

Use when: nibble-level hexadecimal storage is required.

### Type Item: `BIT`

Purpose: fixed-length bit string.

Syntax:

```sql
BIT[(size)] [[FIXED |] VARIABLE (IN ROW size)]
```

Limits and storage:

- Default size is `1` bit.
- Maximum size is `64000` bits.
- Allowed characters are `0` and `1`.
- Values shorter than the declared size are padded on the right with `0`.

### Type Item: `VARBIT`

Purpose: variable-length bit string.

Syntax:

```sql
VARBIT[(size)] [[FIXED |] VARIABLE (IN ROW size)]
```

Limits and storage:

- Default size is `1` bit.
- Maximum size is `64000` bits.
- Allowed characters are `0` and `1`.

### Type Item: `BLOB`

Purpose: large binary object.

Syntax:

```sql
BLOB [IN ROW size]
```

Limits and storage:

- Maximum size is `4GB - 1 byte`.
- Disk table LOB data can be stored in a separate disk LOB tablespace.
- Memory table LOB data stays in the same tablespace as the table.
- Small LOB values can use `IN ROW` behavior.

Restrictions:

- LOB columns cannot be used in volatile tables or disk temporary tablespaces.
- LOB columns cannot be used in cursors.
- LOB columns cannot be partition key columns.
- Indexes cannot be created on LOB columns.
- Avoid `NOT NULL` on LOB columns unless the application and driver behavior are tested.

Related properties and checks:

- `DISK_LOB_COLUMN_IN_ROW_SIZE`: default disk-table LOB `IN ROW` threshold.
- `MEMORY_LOB_COLUMN_IN_ROW_SIZE`: default memory-table LOB `IN ROW` threshold.
- `LOB_OBJECT_BUFFER_SIZE`: maximum LOB object buffer used for LOB parameters, variables, or return values in PSM and triggers.
- `LOB_CACHE_THRESHOLD`: maximum client LOB cache size for small LOB values.
- Check `SYSTEM_.SYS_COLUMNS_` for column storage metadata and `V$PROPERTY` for property values before changing DDL or LOB client behavior.

### Type Item: `CLOB`

Purpose: large character object.

Syntax:

```sql
CLOB [IN ROW size]
```

Limits, storage, and restrictions: same general LOB rules as `BLOB`.

Use when: text can exceed ordinary `VARCHAR` or `NVARCHAR` limits.

### Type Item: Temporary LOB

Version: Altibase 8.1 verified source feature. It is not part of the selected 7.1 or 7.3 baselines.

Purpose: transient LOB created in memory at execution time for large text or binary processing.

Enablement:

- `TEMPORARY_LOB_ENABLE=1` enables Temporary LOB.
- Temporary LOB information is exposed through `V$TEMPORARY_LOBS`.

Lifecycle types:

- Transaction Temporary LOB: exists for a transaction and is removed when the transaction ends.
- Session Temporary LOB: exists for a session and is removed when the session ends, or when `ALTER SESSION SET FREE TEMPORARY LOB` is executed.

Common creation cases:

- `TO_CLOB`.
- `TO_BLOB`.
- `SUBSTR` with a `CLOB` argument.
- `CONCAT` with a `CLOB` argument.
- LOB-type PSM variables.
- PSM `ASSOCIATIVE ARRAY`, `VARRAY`, and package variables that use LOB types can be session Temporary LOB cases.

Memory controls:

- `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`: total memory allocation limit for Temporary LOB.
- `MEMORY_TEMPLOB_PIECE_SIZE`: memory piece size used to split and store Temporary LOB data.
- Temporary LOB memory is separate from `MEM_MAX_DB_SIZE`.
- JSON processing uses Temporary LOB, so JSON failures or memory reviews should include these properties.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name IN (
  'TEMPORARY_LOB_ENABLE',
  'MEMORY_TEMPLOB_MAX_ALLOC_SIZE',
  'MEMORY_TEMPLOB_PIECE_SIZE'
)
ORDER BY name;

SELECT type, id, alloced_size, open_count
FROM V$TEMPORARY_LOBS;
```

Cleanup SQL for session Temporary LOB:

```sql
ALTER SESSION SET FREE TEMPORARY LOB;
```

### Type Item: `GEOMETRY`

Purpose: spatial data type supported by Altibase SQL.

Supported subtypes:

- `Point`
- `LineString`
- `Polygon`
- `GeomCollection`
- `MultiPolygon`
- `MultiLineString`
- `MultiPoint`

Limits and storage:

- Length range is `8` through `104857600`.
- Stored size is length plus geometry header overhead.

Use the spatial attachment for spatial functions, indexes, and geometry operators.

### Type Item: `JSON`

Version: Altibase 8.1 verified source feature. It is not part of the selected 7.1 or 7.3 baselines.

Purpose: store and retrieve JSON documents natively.

Syntax:

```sql
JSON [IN ROW size]
```

Limits and standards:

- Maximum JSON document size is `2GB`.
- JSON definition follows RFC 8259.
- JSON path expressions and JSON functions follow ISO/IEC 19075-6:2021.
- Maximum JSON document depth is `256`.

Restrictions and prerequisites:

- JSON columns follow the same broad restrictions as LOB columns.
- JSON processing uses Temporary LOB, so `TEMPORARY_LOB_ENABLE` must be `1`.
- `JSON` cannot be used with `SELECT FOR UPDATE`.
- Before generating dynamic JSON path-expression SQL, verify the path operand form in the target 8.1 SQL Reference. If the exact grammar is not confirmed, use literal JSON path expressions in examples and avoid claiming support for bind variables, table columns, SQL functions, or user-defined functions as JSON path operands.

JSON function family:

- JSON generation: `JSON_ARRAY`, `JSON_OBJECT`.
- JSON search: `JSON_EXISTS`, `JSON_QUERY`, `JSON_VALUE`.
- JSON validation: `JSON_VALID`.
- JSON condition: `IS JSON`, `IS NOT JSON`.

JSON path elements:

- `$`: root node.
- `@`: current node.
- `.`: object key access.
- `[]`: array element access.
- `*`: wildcard.
- `?(logical-expr)`: filter expression.

Example:

```sql
CREATE TABLE app_event (
  event_id BIGINT,
  payload JSON
);

SELECT JSON_VALUE(payload, '$.customer.id') AS customer_id
FROM app_event
WHERE JSON_EXISTS(payload, '$.customer');
```

Property and view checks:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name IN (
  'TEMPORARY_LOB_ENABLE',
  'MEMORY_TEMPLOB_MAX_ALLOC_SIZE',
  'MEMORY_TEMPLOB_PIECE_SIZE'
)
ORDER BY name;

SELECT type, id, alloced_size, open_count
FROM V$TEMPORARY_LOBS;
```

Version caution: do not use native `JSON`, JSON functions, `IS JSON`, or `V$TEMPORARY_LOBS` in generated 7.1 or 7.3 answers unless the customer provides a target-version source proving equivalent support.

## Oracle Data Type Conversion Guidance

- Oracle `VARCHAR2` -> Altibase `VARCHAR`, after checking byte length and character set.
- Oracle `CHAR` -> Altibase `CHAR`, after checking blank-padding behavior.
- Oracle `NCHAR` -> Altibase `NCHAR`; Oracle `NVARCHAR2` -> Altibase `NVARCHAR`.
- Oracle `NUMBER(p,s)` -> Altibase `NUMBER(p,s)` or `NUMERIC(p,s)` when exact decimal behavior is required.
- Oracle unconstrained `NUMBER` -> choose Altibase `NUMBER`, `FLOAT`, `BIGINT`, `INTEGER`, or `NUMERIC` based on actual data semantics.
- Oracle `DATE` -> Altibase `DATE` for date/time values.
- Oracle `BLOB` -> Altibase `BLOB`; Oracle `CLOB` -> Altibase `CLOB`.
- Oracle `RAW` -> Altibase `BYTE` or `VARBYTE`.
- Oracle JSON features -> Altibase native `JSON` only for 8.1. For 7.1 or 7.3, design around `VARCHAR`, `CLOB`, application validation, or upgrade planning.

## Property Configuration Model

Altibase properties are stored in `altibase.properties` under the server configuration directory.

Property setting methods:

- Static file setting: edit `altibase.properties`; restart is required.
- Dynamic server setting: use `ALTER SYSTEM` when the property supports server-level dynamic changes.
- Dynamic session setting: use `ALTER SESSION` when the property supports session-level dynamic changes.
- Environment variable setting: set `ALTIBASE_property_name`; restart is required.

Precedence:

1. Environment variable.
2. `altibase.properties`.
3. Default system value.

Attribute interpretation:

- `Read-Only`: treat as static unless the manual explicitly says otherwise. Many require restart or database recreation.
- `Read-Write`: can be changed dynamically with `ALTER SYSTEM`, `ALTER SESSION`, or both, depending on the property.
- `Single Value`: one configured value.
- `Multiple Values`: multiple configured values are accepted.

Alter level interpretation:

- `SESSION`: use `ALTER SESSION` for the current session only.
- `SYSTEM`: use `ALTER SYSTEM` for the running server.
- `BOTH`: either `ALTER SESSION` or `ALTER SYSTEM` is valid; choose scope deliberately.
- `NONE`: do not generate dynamic SQL. Use `altibase.properties`, an `ALTIBASE_property_name` environment variable, restart, or database recreation as documented for that property.

Do not infer alter level from the `V$PROPERTY.ATTR` number alone. Use the property's documented dynamic-change support and verify the installed version.

## Property Change Decision Flow

```mermaid
flowchart TD
  A[Need property guidance] --> B[Check version and current value in V$PROPERTY]
  B --> C{Dynamic change supported?}
  C -->|No| D[Use altibase.properties or ALTIBASE_property_name and plan restart or recreation]
  C -->|Yes| E{Scope required?}
  E -->|Current session only| F[ALTER SESSION SET property = value]
  E -->|All sessions or server default| G[ALTER SYSTEM SET property = value]
  E -->|Either| H[Choose SESSION for test, SYSTEM for server-wide change]
  F --> I[Verify V$PROPERTY in same session and related performance view]
  G --> I
  D --> J[Verify after restart or recreation with V$PROPERTY and related view]
```

## Compact Property SQL Syntax

These patterns replace SQL syntax diagrams for property operations.

```text
property_profile_query ::=
  SELECT name, storedcount, attr, min, max, value1, ..., value8
  FROM V$PROPERTY
  WHERE name {= property_name | IN (property_name [, ...])}

alter_system_property ::=
  ALTER SYSTEM SET property_name = property_value

alter_session_property ::=
  ALTER SESSION SET property_name = property_value

free_session_temporary_lob_8_1 ::=
  ALTER SESSION SET FREE TEMPORARY LOB
```

Property SQL rules:

- Use exact property names, for example `QUERY_TIMEOUT`, not a translated property label.
- Quote string values such as date formats and time zone names.
- Keep numeric values explicit. If the property unit is seconds or bytes, state that unit.
- For `ALTER SYSTEM`, the user must be `SYS` or have `ALTER SYSTEM` privilege.
- For `ALTER SESSION`, the change affects only the current session.
- For persistent operations policy, also maintain `altibase.properties` when the site requires restart-stable configuration; do not assume a dynamic statement replaces file configuration unless the target version documentation confirms it.

## Property Check SQL

Use exact property names in `V$PROPERTY`. `V$PROPERTY` exposes `NAME`, `STOREDCOUNT`, `ATTR`, `MIN`, `MAX`, and `VALUE1` through `VALUE8`; multi-value properties use multiple `VALUE` columns.

```sql
SELECT name,
       storedcount,
       attr,
       min,
       max,
       value1,
       value2,
       value3,
       value4,
       value5,
       value6,
       value7,
       value8
FROM V$PROPERTY
WHERE name = '<PROPERTY_NAME>';

SELECT name, storedcount, value1, value2, value3, value4, value5, value6, value7, value8
FROM V$PROPERTY
WHERE name IN ('MEM_DB_DIR', 'LOGANCHOR_DIR')
ORDER BY name;

SELECT name, value1
FROM V$PROPERTY
WHERE name = 'LOG_FILE_SIZE';

SELECT name, value1
FROM V$PROPERTY
WHERE name IN (
  'TEMPORARY_LOB_ENABLE',
  'MEMORY_TEMPLOB_MAX_ALLOC_SIZE',
  'MEMORY_TEMPLOB_PIECE_SIZE'
);

SELECT name, value1
FROM V$PROPERTY
WHERE name LIKE 'REPLICATION%PORT%';

SELECT name, storedcount,
       value1, value2, value3, value4,
       value5, value6, value7, value8
FROM V$PROPERTY
WHERE name IN (
  'DEFAULT_DISK_DB_DIR',
  'MEM_DB_DIR',
  'LOG_DIR',
  'LOGANCHOR_DIR',
  'DOUBLE_WRITE_DIRECTORY'
)
ORDER BY name;

SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name IN (
  'DEFAULT_MEM_DB_FILE_SIZE',
  'SYS_DATA_FILE_INIT_SIZE',
  'SYS_DATA_FILE_MAX_SIZE',
  'SYS_DATA_FILE_NEXT_SIZE',
  'USER_DATA_FILE_INIT_SIZE',
  'USER_DATA_FILE_MAX_SIZE',
  'USER_DATA_FILE_NEXT_SIZE',
  'MEM_MAX_DB_SIZE',
  'DISK_MAX_DB_SIZE',
  'VOLATILE_MAX_DB_SIZE'
)
ORDER BY name;
```

Use property-specific performance views when available:

```sql
SELECT *
FROM V$TEMPORARY_LOBS;

SELECT max_cache_size
FROM V$SQL_PLAN_CACHE;

SELECT name, utc_offset
FROM V$TIME_ZONE_NAMES
WHERE name = 'Asia/Seoul';
```

## Property Change Examples

System-level timeout change:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name = 'QUERY_TIMEOUT';

ALTER SYSTEM SET QUERY_TIMEOUT = 300;

SELECT name, value1
FROM V$PROPERTY
WHERE name = 'QUERY_TIMEOUT';

SELECT query_time_limit
FROM V$SESSION
WHERE id = SESSION_ID();
```

Session-level timeout test:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name = 'QUERY_TIMEOUT';

ALTER SESSION SET QUERY_TIMEOUT = 120;

SELECT name, value1
FROM V$PROPERTY
WHERE name = 'QUERY_TIMEOUT';
```

Session time zone change with value validation:

```sql
SELECT name, utc_offset
FROM V$TIME_ZONE_NAMES
WHERE name = 'Asia/Seoul';

ALTER SESSION SET TIME_ZONE = 'Asia/Seoul';

SELECT name, value1
FROM V$PROPERTY
WHERE name = 'TIME_ZONE';

SELECT time_zone
FROM V$SESSION
WHERE id = SESSION_ID();
```

SQL plan cache size change and related system view check:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name = 'SQL_PLAN_CACHE_SIZE';

SELECT max_cache_size,
       current_cache_size,
       current_cache_obj_count,
       cache_hit_count,
       cache_miss_count
FROM V$SQL_PLAN_CACHE;

ALTER SYSTEM SET SQL_PLAN_CACHE_SIZE = 134217728;

SELECT name, value1
FROM V$PROPERTY
WHERE name = 'SQL_PLAN_CACHE_SIZE';

SELECT max_cache_size,
       current_cache_size,
       current_cache_obj_count
FROM V$SQL_PLAN_CACHE;
```

Static or read-only property answer pattern:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name IN ('LOG_FILE_SIZE', 'PORT_NO', 'MAX_CLIENT');
```

Do not generate `ALTER SYSTEM` or `ALTER SESSION` for these examples unless the target version documentation explicitly says the property is dynamically changeable. Explain the required restart or database recreation path instead.

## Property Categories

### Property Category: Database Initialization

Use for database identity, file locations, tablespace defaults, memory/disk/volatile database size limits, log file size, and default `IN ROW` behavior.

Representative properties:

- `DB_NAME`
- `DEFAULT_DISK_DB_DIR`
- `DEFAULT_MEM_DB_FILE_SIZE`
- `MEM_DB_DIR`
- `LOG_DIR`
- `LOGANCHOR_DIR`
- `DOUBLE_WRITE_DIRECTORY`
- `DOUBLE_WRITE_DIRECTORY_COUNT`
- `LOG_FILE_SIZE`
- `MEM_MAX_DB_SIZE`
- `DISK_MAX_DB_SIZE`
- `VOLATILE_MAX_DB_SIZE`
- `SYS_DATA_FILE_INIT_SIZE`
- `SYS_DATA_FILE_MAX_SIZE`
- `SYS_DATA_FILE_NEXT_SIZE`
- `SYS_TEMP_FILE_INIT_SIZE`
- `SYS_TEMP_FILE_MAX_SIZE`
- `SYS_TEMP_FILE_NEXT_SIZE`
- `SYS_UNDO_FILE_INIT_SIZE`
- `SYS_UNDO_FILE_MAX_SIZE`
- `SYS_UNDO_FILE_NEXT_SIZE`
- `USER_DATA_FILE_INIT_SIZE`
- `USER_DATA_FILE_MAX_SIZE`
- `USER_DATA_FILE_NEXT_SIZE`
- `DISK_LOB_COLUMN_IN_ROW_SIZE`
- `MEMORY_LOB_COLUMN_IN_ROW_SIZE`
- `MEMORY_VARIABLE_COLUMN_IN_ROW_SIZE`

### Property Category: Performance

Use for sort/hash memory, checkpoint behavior, optimizer behavior, SQL plan cache, result cache, locking behavior, and execution memory limits.

Representative properties:

- `HASH_AREA_SIZE`
- `SORT_AREA_SIZE`
- `EXECUTE_STMT_MEMORY_MAXIMUM`
- `PREPARE_STMT_MEMORY_MAXIMUM`
- `SQL_PLAN_CACHE_SIZE`
- `OPTIMIZER_FEATURE_ENABLE`
- `OPTIMIZER_MODE`
- `RESULT_CACHE_ENABLE`
- `CHECKPOINT_INTERVAL_IN_LOG`
- `FAST_START_LOGFILE_TARGET`
- `CHECKPOINT_SCALE_SINGLE_DW_BUFFER_SIZE`

### Property Category: Session and Timeout

Use for client session defaults, locale behavior, date formatting, transaction mode, statement limits, and timeout behavior.

Representative properties:

- `AUTO_COMMIT`
- `ISOLATION_LEVEL`
- `DEFAULT_DATE_FORMAT`
- `TIME_ZONE`
- `NLS_NUMERIC_CHARACTERS`
- `MAX_STATEMENTS_PER_SESSION`
- `QUERY_TIMEOUT`
- `FETCH_TIMEOUT`
- `IDLE_TIMEOUT`
- `LOGIN_TIMEOUT`
- `DDL_TIMEOUT`
- `DDL_LOCK_TIMEOUT`
- `UTRANS_TIMEOUT`

### Property Category: Replication, Network, and Security

Use for ordinary client ports, replication ports, SSL/TLS ports, SSL certificate paths, and replication connection behavior.

Representative properties:

- `PORT_NO`
- `MAX_CLIENT`
- `REPLICATION_PORT_NO`
- `REPLICATION_SSL_PORT_NO`
- `REPLICATION_CONNECT_TIMEOUT`
- `REPLICATION_RECEIVE_TIMEOUT`
- `SSL_ENABLE`
- `SSL_PORT_NO`
- `SSL_CA`
- `SSL_CERT`
- `SSL_KEY`
- `SSL_CIPHER_LIST`
- `TCP_ENABLE`

### Property Category: 8.1 JSON and Temporary LOB

Use for native JSON processing, Temporary LOB memory management, and JSON-formatted execution-plan output.

Representative properties and views:

- `TEMPORARY_LOB_ENABLE`
- `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`
- `MEMORY_TEMPLOB_PIECE_SIZE`
- `TRCLOG_EXPLAIN_TYPE`
- `TRCLOG_JSON_PLAN_INDENT_DEPTH`
- `V$TEMPORARY_LOBS`

## Property Inventory Baseline

Scope: Korean General Reference 1 detailed property headings were inventoried for Altibase 7.1, Altibase 7.3, and Altibase 8.1 verified source. A property name listed here is a source-backed name/availability entry, not a complete default, range, or dynamic-change block.

Inventory counts:

- `484` distinct property names are documented across the selected General Reference 1 sources.
- `444` names are documented in 7.1, 7.3, and Altibase 8.1 verified source.
- `5` names are documented only in the selected 7.1 source.
- `2` names are documented in 7.1 and 7.3 but not in Altibase 8.1 verified source.
- `28` names are documented in 7.3 and Altibase 8.1 verified source but not in 7.1.
- `5` names are documented only in Altibase 8.1 verified source.

Interpretation rules:

- Name availability does not prove identical defaults, ranges, units, or dynamic-change behavior across versions.
- Before generating `ALTER SYSTEM` or `ALTER SESSION`, use a decomposed property block below or verify the target version manual and `V$PROPERTY`.
- If a customer asks about a property name listed here but not decomposed below, state the source-backed version availability, ask for the exact installed version when runtime behavior matters, and give `V$PROPERTY` as the safest next check.
- `PARALLEL_QUERY_THREAD_MAX` and `PARALLEL_QUERY_QUEUE_SIZE` are documented in more than one source category; use the exact property name and target version first, then route to performance or other-operation context as needed.

### Property Inventory: Version Deltas

7.1 only in selected General Reference 1 sources:

- `LOCK_MGR_DETECTDEADLOCK_INTERVAL`, `LOCK_MGR_MAX_SLEEP`, `LOCK_MGR_MIN_SLEEP`, `LOCK_MGR_SPIN_COUNT`, `LOCK_MGR_TYPE`

7.1 and 7.3 only in selected General Reference 1 sources:

- `REPLICATION_META_ITEM_COUNT_DIFF_ENABLE`, `REPLICATION_UPDATE_REPLACE`

7.3 and Altibase 8.1 verified source, not 7.1:

- `CM_MSGLOG_COUNT`, `CM_MSGLOG_FILE`, `CM_MSGLOG_FLAG`, `CM_MSGLOG_SIZE`, `DISK_INDEX_BUILD_SORT_AREA_SIZE`, `DK_MSGLOG_RESERVE_SIZE`
- `DUMP_MSGLOG_RESERVE_SIZE`, `ERROR_MSGLOG_RESERVE_SIZE`, `MM_MSGLOG_FLAG`, `MM_MSGLOG_RESERVE_SIZE`, `NETWORK_ERROR_LOG_FILE`, `PSM_MAX_DDL_REFERENCE_DEPTH`
- `QP_MSGLOG_RESERVE_SIZE`, `REPLICATION_RECEIVER_APPLIER_YIELD_COUNT`, `RP_CONFLICT_MSGLOG_RESERVE_SIZE`, `RP_MSGLOG_RESERVE_SIZE`, `SERVER_MSGLOG_RESERVE_SIZE`, `SERVICE_THREAD_RECV_TIMEOUT`
- `SM_MSGLOG_RESERVE_SIZE`, `SSL_CIPHER_SUITES`, `SSL_LOAD_CONFIG`, `ST_MSGLOG_COUNT`, `ST_MSGLOG_FILE`, `ST_MSGLOG_FLAG`
- `ST_MSGLOG_SIZE`, `TRC_MSGLOG_RESERVE_SIZE`, `VARRAY_MEMORY_MAXIMUM`, `XA_MSGLOG_RESERVE_SIZE`

Altibase 8.1 verified source only:

- `CHECKPOINT_SCALE_SINGLE_DW_BUFFER_SIZE`, `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`, `MEMORY_TEMPLOB_PIECE_SIZE`, `REPLICATION_SSL_PORT_NO`, `TEMPORARY_LOB_ENABLE`

### Property Inventory: Common 7.1, 7.3, And 8.1 Names

#### `D` Database initialization

- `BUFFER_AREA_CHUNK_SIZE`, `BUFFER_AREA_SIZE`, `BUFFER_CHECKPOINT_LIST_CNT`, `BUFFER_FLUSHER_CNT`, `BUFFER_FLUSH_LIST_CNT`, `BUFFER_HASH_BUCKET_DENSITY`, `BUFFER_HASH_CHAIN_LATCH_DENSITY`
- `BUFFER_LRU_LIST_CNT`, `BUFFER_PREPARE_LIST_CNT`, `BULKIO_PAGE_COUNT_FOR_DIRECT_PATH_INSERT`, `COMPRESSION_RESOURCE_GC_SECOND`, `DB_NAME`, `DDL_SUPPLEMENTAL_LOG_ENABLE`, `DEFAULT_DISK_DB_DIR`
- `DEFAULT_MEM_DB_FILE_SIZE`, `DEFAULT_SEGMENT_MANAGEMENT_TYPE`, `DEFAULT_SEGMENT_STORAGE_INITEXTENTS`, `DEFAULT_SEGMENT_STORAGE_MAXEXTENTS`, `DEFAULT_SEGMENT_STORAGE_MINEXTENTS`, `DEFAULT_SEGMENT_STORAGE_NEXTEXTENTS`, `DIRECT_PATH_BUFFER_PAGE_COUNT`
- `DISK_INDEX_UNBALANCED_SPLIT_RATE`, `DISK_LOB_COLUMN_IN_ROW_SIZE`, `DISK_MAX_DB_SIZE`, `DOUBLE_WRITE_DIRECTORY`, `DOUBLE_WRITE_DIRECTORY_COUNT`, `DRDB_FD_MAX_COUNT_PER_DATAFILE`, `EXPAND_CHUNK_PAGE_COUNT`
- `LOB_OBJECT_BUFFER_SIZE`, `LOCK_MGR_CACHE_NODE`, `LOCK_NODE_CACHE_COUNT`, `LOGANCHOR_DIR`, `LOG_DIR`, `LOG_FILE_SIZE`, `MAX_CLIENT`
- `MEMORY_INDEX_BUILD_RUN_SIZE`, `MEMORY_INDEX_BUILD_VALUE_LENGTH_THRESHOLD`, `MEMORY_INDEX_UNBALANCED_SPLIT_RATE`, `MEMORY_LOB_COLUMN_IN_ROW_SIZE`, `MEMORY_VARIABLE_COLUMN_IN_ROW_SIZE`, `MEM_DB_DIR`, `MEM_MAX_DB_SIZE`
- `MEM_SIZE_CLASS_COUNT`, `MIN_COMPRESSION_RESOURCE_COUNT`, `MIN_LOG_RECORD_SIZE_FOR_COMPRESS`, `MIN_PAGES_ON_DB_FREE_LIST`, `MIN_PAGES_ON_TABLE_FREE_LIST`, `MIN_TASK_COUNT_FOR_THREAD_LIVE`, `PCTFREE`
- `PCTUSED`, `QP_MEMORY_CHUNK_SIZE`, `RECYCLEBIN_DISK_MAX_SIZE`, `RECYCLEBIN_ENABLE`, `RECYCLEBIN_MEM_MAX_SIZE`, `REDUCE_TEMP_MEMORY_ENABLE`, `SECURITY_ECC_POLICY_NAME`
- `SECURITY_MODULE_LIBRARY`, `SECURITY_MODULE_NAME`, `SERVICE_THREAD_INITIAL_LIFESPAN`, `SMALL_TABLE_THRESHOLD`, `ST_OBJECT_BUFFER_SIZE`, `SYS_DATA_FILE_INIT_SIZE`, `SYS_DATA_FILE_MAX_SIZE`
- `SYS_DATA_FILE_NEXT_SIZE`, `SYS_DATA_TBS_EXTENT_SIZE`, `SYS_TEMP_FILE_INIT_SIZE`, `SYS_TEMP_FILE_MAX_SIZE`, `SYS_TEMP_FILE_NEXT_SIZE`, `SYS_TEMP_TBS_EXTENT_SIZE`, `SYS_UNDO_FILE_INIT_SIZE`
- `SYS_UNDO_FILE_MAX_SIZE`, `SYS_UNDO_FILE_NEXT_SIZE`, `SYS_UNDO_TBS_EXTENT_SIZE`, `TABLE_BACKUP_FILE_BUFFER_SIZE`, `TABLE_COMPACT_AT_SHUTDOWN`, `TEMP_HASH_BUCKET_DENSITY`, `TEMP_PAGE_CHUNK_COUNT`
- `USER_DATA_FILE_INIT_SIZE`, `USER_DATA_FILE_MAX_SIZE`, `USER_DATA_FILE_NEXT_SIZE`, `USER_DATA_TBS_EXTENT_SIZE`, `USER_TEMP_FILE_INIT_SIZE`, `USER_TEMP_FILE_MAX_SIZE`, `USER_TEMP_FILE_NEXT_SIZE`
- `USER_TEMP_TBS_EXTENT_SIZE`, `VOLATILE_MAX_DB_SIZE`

#### `P` Performance

- `AGER_WAIT_MAXIMUM`, `AGER_WAIT_MINIMUM`, `BUFFER_VICTIM_SEARCH_INTERVAL`, `BUFFER_VICTIM_SEARCH_PCT`, `CHECKPOINT_BULK_SYNC_PAGE_COUNT`, `CHECKPOINT_BULK_WRITE_PAGE_COUNT`, `CHECKPOINT_BULK_WRITE_SLEEP_SEC`
- `CHECKPOINT_BULK_WRITE_SLEEP_USEC`, `CHECKPOINT_FLUSH_COUNT`, `CHECKPOINT_FLUSH_MAX_GAP`, `CHECKPOINT_FLUSH_MAX_WAIT_SEC`, `CM_BUFFER_MAX_PENDING_LIST`, `CM_DISPATCHER_SOCK_POLL_TYPE`, `DATABASE_IO_TYPE`
- `DATAFILE_WRITE_UNIT_SIZE`, `DB_FILE_MULTIPAGE_READ_COUNT`, `DEDICATED_THREAD_CHECK_INTERVAL`, `DEDICATED_THREAD_INIT_COUNT`, `DEDICATED_THREAD_MAX_COUNT`, `DEDICATED_THREAD_MODE`, `DEFAULT_FLUSHER_WAIT_SEC`
- `DELAYED_FLUSH_LIST_PCT`, `DELAYED_FLUSH_PROTECTION_TIME_MSEC`, `DIRECT_IO_ENABLED`, `DISK_INDEX_BUILD_MERGE_PAGE_COUNT`, `EXECUTE_STMT_MEMORY_MAXIMUM`, `EXECUTOR_FAST_SIMPLE_QUERY`, `FAST_START_IO_TARGET`
- `FAST_START_LOGFILE_TARGET`, `FAST_UNLOCK_LOG_ALLOC_MUTEX`, `HASH_AREA_SIZE`, `HASH_JOIN_MEM_TEMP_AUTO_BUCKET_COUNT_DISABLE`, `HASH_JOIN_MEM_TEMP_PARTITIONING_DISABLE`, `HIGH_FLUSH_PCT`, `HOT_LIST_PCT`
- `HOT_TOUCH_CNT`, `INDEX_BUILD_THREAD_COUNT`, `INDEX_INITRANS`, `INDEX_MAXTRANS`, `INIT_TOTAL_WA_SIZE`, `LFG_GROUP_COMMIT_INTERVAL_USEC`, `LFG_GROUP_COMMIT_RETRY_USEC`
- `LFG_GROUP_COMMIT_UPDATE_TX_COUNT`, `LOB_CACHE_THRESHOLD`, `LOCK_ESCALATION_MEMORY_SIZE`, `LOG_CREATE_METHOD`, `LOG_IO_TYPE`, `LOW_FLUSH_PCT`, `LOW_PREPARE_PCT`
- `MATHEMATICS_TEMP_MEMORY_MAXIMUM`, `MAX_FLUSHER_WAIT_SEC`, `MEM_INDEX_KEY_REDISTRIBUTION`, `MEM_INDEX_KEY_REDISTRIBUTION_STANDARD_RATE`, `MULTIPLEXING_CHECK_INTERVAL`, `MULTIPLEXING_MAX_THREAD_COUNT`, `MULTIPLEXING_THREAD_COUNT`
- `NORMALFORM_MAXIMUM`, `OPTIMIZER_AUTO_STATS`, `OPTIMIZER_DELAYED_EXECUTION`, `OPTIMIZER_FEATURE_ENABLE`, `OPTIMIZER_MODE`, `OPTIMIZER_PERFORMANCE_VIEW`, `OPTIMIZER_UNNEST_AGGREGATION_SUBQUERY`
- `OPTIMIZER_UNNEST_COMPLEX_SUBQUERY`, `OPTIMIZER_UNNEST_SUBQUERY`, `OUTER_JOIN_OPERATOR_TRANSFORM_ENABLE`, `PARALLEL_LOAD_FACTOR`, `PARALLEL_QUERY_QUEUE_SIZE`, `PARALLEL_QUERY_THREAD_MAX`, `PREPARE_STMT_MEMORY_MAXIMUM`
- `QUERY_REWRITE_ENABLE`, `REFINE_PAGE_COUNT`, `RESULT_CACHE_ENABLE`, `RESULT_CACHE_MEMORY_MAXIMUM`, `SECONDARY_BUFFER_ENABLE`, `SECONDARY_BUFFER_FILE_DIRECTORY`, `SECONDARY_BUFFER_FLUSHER_CNT`
- `SECONDARY_BUFFER_SIZE`, `SECONDARY_BUFFER_TYPE`, `SERIAL_EXECUTE_MODE`, `SORT_AREA_SIZE`, `SQL_PLAN_CACHE_BUCKET_CNT`, `SQL_PLAN_CACHE_HOT_REGION_LRU_RATIO`, `SQL_PLAN_CACHE_PREPARED_EXECUTION_CONTEXT_CNT`
- `SQL_PLAN_CACHE_SIZE`, `STATEMENT_LIST_PARTIAL_SCAN_COUNT`, `TABLESPACE_LOCK_ENABLE`, `TABLE_INITRANS`, `TABLE_LOCK_ENABLE`, `TABLE_LOCK_MODE`, `TABLE_MAXTRANS`
- `TEMP_STATS_WATCH_TIME`, `THREAD_CPU_AFFINITY`, `THREAD_REUSE_ENABLE`, `TIMED_STATISTICS`, `TIMER_RUNNING_LEVEL`, `TIMER_THREAD_RESOLUTION`, `TOP_RESULT_CACHE_MODE`
- `TOTAL_WA_SIZE`, `TOUCH_TIME_INTERVAL`, `TRANSACTION_SEGMENT_COUNT`, `TRX_UPDATE_MAX_LOGSIZE`

#### `S` Session

- `CM_DISCONN_DETECT_TIME`, `CONCURRENT_EXEC_DEGREE_DEFAULT`, `CONCURRENT_EXEC_DEGREE_MAX`, `CONCURRENT_EXEC_WAIT_INTERVAL`, `DEFAULT_THREAD_STACK_SIZE`, `IPCDA_CHANNEL_COUNT`, `IPCDA_DATABLOCK_SIZE`
- `IPCDA_FILEPATH`, `IPCDA_SEM_KEY`, `IPCDA_SHM_KEY`, `IPC_CHANNEL_COUNT`, `IPC_FILEPATH`, `IPC_SEM_KEY`, `IPC_SHM_KEY`
- `MAX_LISTEN`, `MAX_STATEMENTS_PER_SESSION`, `NET_CONN_IP_STACK`, `NLS_COMP`, `NLS_CURRENCY`, `NLS_ISO_CURRENCY`, `NLS_NCHAR_CONV_EXCP`
- `NLS_NCHAR_LITERAL_REPLACE`, `NLS_NUMERIC_CHARACTERS`, `NLS_TERRITORY`, `PORT_NO`, `PSM_CURSOR_OPEN_LIMIT`, `PSM_FILE_OPEN_LIMIT`, `TIME_ZONE`
- `UNIXDOMAIN_FILEPATH`, `USER_LOCK_POOL_INIT_SIZE`, `USER_LOCK_REQUEST_CHECK_INTERVAL`, `USER_LOCK_REQUEST_LIMIT`, `USER_LOCK_REQUEST_TIMEOUT`, `USE_MEMORY_POOL`, `XA_HEURISTIC_COMPLETE`

#### `TO` Time-out

- `BLOCK_ALL_TX_TIME_OUT`, `DDL_LOCK_TIMEOUT`, `DDL_TIMEOUT`, `FETCH_TIMEOUT`, `IDLE_TIMEOUT`, `LOGIN_TIMEOUT`, `MULTIPLEXING_POLL_TIMEOUT`
- `QUERY_TIMEOUT`, `SHUTDOWN_IMMEDIATE_TIMEOUT`, `UTRANS_TIMEOUT`, `XA_INDOUBT_TX_TIMEOUT`

#### `T` Transaction

- `AUTO_COMMIT`, `ISOLATION_LEVEL`, `TRANSACTION_TABLE_SIZE`

#### `B` Backup and recovery

- `ARCHIVE_DIR`, `ARCHIVE_FULL_ACTION`, `ARCHIVE_MULTIPLEX_COUNT`, `ARCHIVE_MULTIPLEX_DIR`, `ARCHIVE_THREAD_AUTOSTART`, `CHECKPOINT_ENABLED`, `CHECKPOINT_INTERVAL_IN_LOG`
- `CHECKPOINT_INTERVAL_IN_SEC`, `COMMIT_WRITE_WAIT_MODE`, `INCREMENTAL_BACKUP_CHUNK_SIZE`, `INCREMENTAL_BACKUP_INFO_RETENTION_PERIOD`, `LOG_BUFFER_TYPE`, `LOG_MULTIPLEX_COUNT`, `LOG_MULTIPLEX_DIR`
- `PREPARE_LOG_FILE_COUNT`, `SNAPSHOT_DISK_UNDO_THRESHOLD`, `SNAPSHOT_MEM_THRESHOLD`

#### `R` Replication

- `REPLICATION_ACK_XLOG_COUNT`, `REPLICATION_ALLOW_DUPLICATE_HOSTS`, `REPLICATION_BEFORE_IMAGE_LOG_ENABLE`, `REPLICATION_COMMIT_WRITE_WAIT_MODE`, `REPLICATION_CONNECT_RECEIVE_TIMEOUT`, `REPLICATION_CONNECT_TIMEOUT`, `REPLICATION_DDL_ENABLE`
- `REPLICATION_DDL_ENABLE_LEVEL`, `REPLICATION_DDL_SYNC`, `REPLICATION_DDL_SYNC_TIMEOUT`, `REPLICATION_EAGER_PARALLEL_FACTOR`, `REPLICATION_EAGER_RECEIVER_MAX_ERROR_COUNT`, `REPLICATION_FAILBACK_INCREMENTAL_SYNC`, `REPLICATION_GAPLESS_ALLOW_TIME`
- `REPLICATION_GAPLESS_MAX_WAIT_TIME`, `REPLICATION_GAP_UNIT`, `REPLICATION_GROUPING_AHEAD_READ_NEXT_LOG_FILE`, `REPLICATION_GROUPING_TRANSACTION_MAX_COUNT`, `REPLICATION_HBT_DETECT_HIGHWATER_MARK`, `REPLICATION_HBT_DETECT_TIME`, `REPLICATION_IB_LATENCY`
- `REPLICATION_IB_PORT_NO`, `REPLICATION_INSERT_REPLACE`, `REPLICATION_KEEP_ALIVE_CNT`, `REPLICATION_LOCK_TIMEOUT`, `REPLICATION_LOG_BUFFER_SIZE`, `REPLICATION_MAX_COUNT`, `REPLICATION_MAX_LISTEN`
- `REPLICATION_MAX_LOGFILE`, `REPLICATION_POOL_ELEMENT_COUNT`, `REPLICATION_POOL_ELEMENT_SIZE`, `REPLICATION_PORT_NO`, `REPLICATION_PREFETCH_LOGFILE_COUNT`, `REPLICATION_RECEIVER_APPLIER_ASSIGN_MODE`, `REPLICATION_RECEIVER_APPLIER_QUEUE_SIZE`
- `REPLICATION_RECEIVE_TIMEOUT`, `REPLICATION_RECOVERY_MAX_LOGFILE`, `REPLICATION_RECOVERY_MAX_TIME`, `REPLICATION_SENDER_AUTO_START`, `REPLICATION_SENDER_COMPRESS_XLOG`, `REPLICATION_SENDER_ENCRYPT_XLOG`, `REPLICATION_SENDER_IP`
- `REPLICATION_SENDER_SEND_TIMEOUT`, `REPLICATION_SENDER_SLEEP_TIME`, `REPLICATION_SENDER_SLEEP_TIMEOUT`, `REPLICATION_SENDER_START_AFTER_GIVING_UP`, `REPLICATION_SERVER_FAILBACK_MAX_TIME`, `REPLICATION_SQL_APPLY_ENABLE`, `REPLICATION_SYNC_APPLY_METHOD`
- `REPLICATION_SYNC_LOCK_TIMEOUT`, `REPLICATION_SYNC_LOG`, `REPLICATION_SYNC_TUPLE_COUNT`, `REPLICATION_TIMESTAMP_RESOLUTION`, `REPLICATION_TRANSACTION_POOL_SIZE`

#### `NM` Network and security

- `IB_CONCHKSPIN`, `IB_ENABLE`, `IB_LATENCY`, `IB_LISTENER_DISABLE`, `IB_MAX_LISTEN`, `IB_PORT_NO`, `SNMP_ALARM_FETCH_TIMEOUT`
- `SNMP_ALARM_QUERY_TIMEOUT`, `SNMP_ALARM_SESSION_FAILURE_COUNT`, `SNMP_ALARM_UTRANS_TIMEOUT`, `SNMP_ENABLE`, `SNMP_MSGLOG_FLAG`, `SNMP_PORT_NO`, `SNMP_RECV_TIMEOUT`
- `SNMP_SEND_TIMEOUT`, `SNMP_TRAP_PORT_NO`, `SSL_CA`, `SSL_CAPATH`, `SSL_CERT`, `SSL_CIPHER_LIST`, `SSL_CLIENT_AUTHENTICATION`
- `SSL_ENABLE`, `SSL_KEY`, `SSL_MAX_LISTEN`, `SSL_PORT_NO`, `TCP_ENABLE`

#### `M` Message logging

- `ALL_MSGLOG_FLUSH`, `COLLECT_DUMP_INFO`, `DK_MSGLOG_COUNT`, `DK_MSGLOG_FILE`, `DK_MSGLOG_FLAG`, `DK_MSGLOG_SIZE`, `DUMP_MSGLOG_COUNT`
- `DUMP_MSGLOG_FILE`, `DUMP_MSGLOG_SIZE`, `ERROR_MSGLOG_COUNT`, `ERROR_MSGLOG_FILE`, `ERROR_MSGLOG_SIZE`, `JOB_MSGLOG_COUNT`, `JOB_MSGLOG_FILE`
- `JOB_MSGLOG_FLAG`, `JOB_MSGLOG_SIZE`, `LB_MSGLOG_COUNT`, `LB_MSGLOG_FILE`, `LB_MSGLOG_FLAG`, `LB_MSGLOG_SIZE`, `MM_MSGLOG_COUNT`
- `MM_MSGLOG_FILE`, `MM_MSGLOG_SIZE`, `MM_SESSION_LOGGING`, `NETWORK_ERROR_LOG`, `QP_MSGLOG_COUNT`, `QP_MSGLOG_FILE`, `QP_MSGLOG_FLAG`
- `QP_MSGLOG_SIZE`, `QUERY_PROF_FLAG`, `QUERY_PROF_LOG_DIR`, `RP_CONFLICT_MSGLOG_COUNT`, `RP_CONFLICT_MSGLOG_DIR`, `RP_CONFLICT_MSGLOG_ENABLE`, `RP_CONFLICT_MSGLOG_FILE`
- `RP_CONFLICT_MSGLOG_FLAG`, `RP_CONFLICT_MSGLOG_SIZE`, `RP_MSGLOG_COUNT`, `RP_MSGLOG_FILE`, `RP_MSGLOG_FLAG`, `RP_MSGLOG_SIZE`, `SERVER_MSGLOG_COUNT`
- `SERVER_MSGLOG_DIR`, `SERVER_MSGLOG_FILE`, `SERVER_MSGLOG_FLAG`, `SERVER_MSGLOG_SIZE`, `SM_MSGLOG_COUNT`, `SM_MSGLOG_FILE`, `SM_MSGLOG_FLAG`
- `SM_MSGLOG_SIZE`, `TRCLOG_DETAIL_PREDICATE`, `XA_MSGLOG_COUNT`, `XA_MSGLOG_FILE`, `XA_MSGLOG_FLAG`, `XA_MSGLOG_SIZE`

#### `L` Database link

- `DBLINK_ALTILINKER_CONNECT_TIMEOUT`, `DBLINK_DATA_BUFFER_ALLOC_RATIO`, `DBLINK_DATA_BUFFER_BLOCK_COUNT`, `DBLINK_DATA_BUFFER_BLOCK_SIZE`, `DBLINK_ENABLE`, `DBLINK_GLOBAL_TRANSACTION_LEVEL`, `DBLINK_RECOVERY_MAX_LOGFILE`
- `DBLINK_REMOTE_STATEMENT_AUTOCOMMIT`, `DBLINK_REMOTE_TABLE_BUFFER_SIZE`

#### `U` Auditing

- `AUDIT_FILE_SIZE`, `AUDIT_LOG_DIR`, `AUDIT_OUTPUT_METHOD`, `AUDIT_TAG_NAME_IN_SYSLOG`

#### `A` C/C++ external procedure agent

- `EXTPROC_AGENT_CALL_RETRY_COUNT`, `EXTPROC_AGENT_CONNECT_TIMEOUT`, `EXTPROC_AGENT_IDLE_TIMEOUT`, `EXTPROC_AGENT_SOCKET_FILEPATH`

#### `AS` Account security

- `CASE_SENSITIVE_PASSWORD`, `FAILED_LOGIN_ATTEMPTS`, `PASSWORD_GRACE_TIME`, `PASSWORD_LIFE_TIME`, `PASSWORD_LOCK_TIME`, `PASSWORD_REUSE_MAX`, `PASSWORD_REUSE_TIME`
- `PASSWORD_VERIFY_FUNCTION`

#### `E` Other

- `ACCESS_LIST`, `ACCESS_LIST_FILE`, `ADMIN_MODE`, `ARITHMETIC_OPERATION_MODE`, `CHECK_MUTEX_DURATION_TIME_ENABLE`, `COERCE_HOST_VAR_IN_SELECT_LIST_TO_VARCHAR`, `DEFAULT_DATE_FORMAT`
- `EXEC_DDL_DISABLE`, `GROUP_CONCAT_PRECISION`, `JOB_SCHEDULER_ENABLE`, `JOB_THREAD_COUNT`, `JOB_THREAD_QUEUE_SIZE`, `LISTAGG_PRECISION`, `MSG_QUEUE_PERMISSION`
- `PSM_CASE_SENSITIVE_MODE`, `PSM_CHAR_DEFAULT_PRECISION`, `PSM_IGNORE_NO_DATA_FOUND_ERROR`, `PSM_NCHAR_UTF16_DEFAULT_PRECISION`, `PSM_NCHAR_UTF8_DEFAULT_PRECISION`, `PSM_NVARCHAR_UTF16_DEFAULT_PRECISION`, `PSM_NVARCHAR_UTF8_DEFAULT_PRECISION`
- `PSM_PARAM_AND_RETURN_WITHOUT_PRECISION_ENABLE`, `PSM_VARCHAR_DEFAULT_PRECISION`, `QUERY_STACK_SIZE`, `RECURSION_LEVEL_MAXIMUM`, `REGEXP_MODE`, `REMOTE_SYSDBA_ENABLE`, `SELECT_HEADER_DISPLAY`
- `SYS_CONNECT_BY_PATH_PRECISION`, `TRC_ACCESS_PERMISSION`

## Decomposed Property Blocks

Unless a property block states a narrower scope, the block is documented for Altibase 7.1, Altibase 7.3, and Altibase 8.1 verified source. Version-specific General Reference sources are the basis for defaults, ranges, attributes, and change methods. For static initialization and storage properties, prefer `V$PROPERTY` checks plus restart or database-creation planning over generated `ALTER SYSTEM` SQL.

### Property Item: `DB_NAME`

Meaning: database name used when creating the database.

Default: `mydb`.

Dynamic Change Support: read-only. Create a new database to change it.

Range: no explicit range.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'DB_NAME';
```

### Property Item: `DDL_SUPPLEMENTAL_LOG_ENABLE`

Meaning: controls whether DDL operations write supplemental log records.

Default: `0`.

Dynamic Change Support: read-write; can be changed with `ALTER SYSTEM`.

Range: `[0, 1]`.

Values:

- `0`: disabled; do not write supplemental DDL logs.
- `1`: enabled; write supplemental DDL logs.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'DDL_SUPPLEMENTAL_LOG_ENABLE';
```

### Property Item: `DEFAULT_DISK_DB_DIR`

Meaning: default directory for disk database files.

Default: `$ALTIBASE_HOME/dbs`.

Dynamic Change Support: read-only; restart and file-layout planning are required.

Range: directory path.

Important note: this path must be configured even when disk database features are not used.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'DEFAULT_DISK_DB_DIR';
```

### Property Item: `DEFAULT_MEM_DB_FILE_SIZE`

Meaning: default size, in bytes, of checkpoint image files for memory tablespaces.

Default: `1073741824` bytes (`1G`).

Dynamic Change Support: read-only; set before database creation or recreate/replan the database file layout.

Range: `[4194304, 2^64 - 1]`.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name = 'DEFAULT_MEM_DB_FILE_SIZE';
```

### Property Item: `DEFAULT_SEGMENT_MANAGEMENT_TYPE`

Meaning: default segment space-management method when a disk tablespace is created.

Default: `1`.

Dynamic Change Support: read-only default for new disk tablespace creation.

Values:

- `0`: `MANUAL`; create segments that manage free space with freelists.
- `1`: `AUTO`; create segments that manage free space with bitmap index based management.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'DEFAULT_SEGMENT_MANAGEMENT_TYPE';
```

### Property Item Group: `DEFAULT_SEGMENT_STORAGE_*`

Meaning: default extent-count values used when a segment is created without explicit storage extent clauses.

Dynamic Change Support: read-only defaults; use explicit storage clauses in DDL when a specific object needs different values.

Properties:

- `DEFAULT_SEGMENT_STORAGE_INITEXTENTS`: initial extent count; default `1`; range `[1, 2^32 - 1]`.
- `DEFAULT_SEGMENT_STORAGE_MINEXTENTS`: minimum extent count; default `1`; range `[1, 2^32 - 1]`.
- `DEFAULT_SEGMENT_STORAGE_MAXEXTENTS`: maximum extent count; default `2^32 - 1`; range `[1, 2^32 - 1]`.
- `DEFAULT_SEGMENT_STORAGE_NEXTEXTENTS`: next extension extent count; default `1`; range `[1, 2^32 - 1]`.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name IN (
  'DEFAULT_SEGMENT_STORAGE_INITEXTENTS',
  'DEFAULT_SEGMENT_STORAGE_MINEXTENTS',
  'DEFAULT_SEGMENT_STORAGE_MAXEXTENTS',
  'DEFAULT_SEGMENT_STORAGE_NEXTEXTENTS'
)
ORDER BY name;
```

### Property Item: `MEM_DB_DIR`

Meaning: directory paths for memory database files.

Default: `$ALTIBASE_HOME/dbs`.

Dynamic Change Support: read-only; restart and storage planning are required.

Range: one to eight actual paths.

Behavior: when more than one path is configured, memory database files are distributed across the paths. The documented default path count is two, and both default entries use `$ALTIBASE_HOME/dbs`.

Check SQL:

```sql
SELECT name, storedcount,
       value1, value2, value3, value4,
       value5, value6, value7, value8
FROM V$PROPERTY
WHERE name = 'MEM_DB_DIR';
```

### Property Item: `LOG_DIR`

Meaning: path for log files.

Default: `$ALTIBASE_HOME/logs`.

Dynamic Change Support: read-only.

Range: path value; multiple values can be configured where supported.

Check SQL:

```sql
SELECT name, storedcount,
       value1, value2, value3, value4,
       value5, value6, value7, value8
FROM V$PROPERTY
WHERE name = 'LOG_DIR';
```

### Property Item: `LOGANCHOR_DIR`

Meaning: pathnames for log anchor files.

Default: `$ALTIBASE_HOME/logs`.

Dynamic Change Support: read-only.

Range: three log anchor file paths are required.

Check SQL:

```sql
SELECT name, storedcount,
       value1, value2, value3, value4,
       value5, value6, value7, value8
FROM V$PROPERTY
WHERE name = 'LOGANCHOR_DIR';
```

### Property Item: `LOG_FILE_SIZE`

Meaning: size in bytes of each log file. When an active log file fills, writing continues in a new log file.

Default: 7.1 uses `10 * 1024 * 1024`; 7.3 and the 8.1 baseline use `100 * 1024 * 1024`. The 8.1 release notes record this default as changed from `10485760` to `104857600`.

Dynamic Change Support: read-only. Set only at database creation; create a new database to change it.

Range: 7.1 `[1024 * 1024, 2^64 - 1]`; 7.3 and the 8.1 baseline `[64 * 1024, 2^32 - 1]`. The 8.1 release notes record the maximum as changed to `4294967295`.

Important note: for offline replication, set this property identically on local and remote servers.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'LOG_FILE_SIZE';
```

### Property Item Group: Log compression storage properties

Meaning: configure the minimum compression resource pool and the log-record size threshold for log compression.

Properties:

- `MIN_COMPRESSION_RESOURCE_COUNT`: minimum number of buffer chunks used by the log manager for log compression; default `16`; range `[1, 16384]`; read-only. One compression buffer chunk is about `16KB`.
- `MIN_LOG_RECORD_SIZE_FOR_COMPRESS`: log size threshold for compression; default `512` bytes; range `[0, 2^32 - 1]`; read-write with `ALTER SYSTEM`. `0` disables log compression, and records larger than the configured value are compressed.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name IN (
  'MIN_COMPRESSION_RESOURCE_COUNT',
  'MIN_LOG_RECORD_SIZE_FOR_COMPRESS'
)
ORDER BY name;
```

### Property Item: `MEM_MAX_DB_SIZE`

Meaning: maximum memory database size in bytes.

Default: `2^31` bytes.

Dynamic Change Support: read-only.

Range: `32-bit [2097152, 2^32 + 1]`; `64-bit [2097152, 2^64]`.

Behavior: if the memory database expands beyond this value, the offending transaction errors, and later non-`SELECT` SQL also errors until the condition is resolved.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'MEM_MAX_DB_SIZE';
```

### Property Item: `EXPAND_CHUNK_PAGE_COUNT`

Meaning: number of pages in one expand chunk, the allocation unit used when the memory database expands.

Default: `128`.

Dynamic Change Support: read-only. Set during database creation; recreate the database to change the page count.

Range: `[64, 2^32 - 1]`.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name = 'EXPAND_CHUNK_PAGE_COUNT';
```

### Property Item: `MEM_SIZE_CLASS_COUNT`

Meaning: number of free-space classes used to classify memory pages.

Default: `4`.

Dynamic Change Support: read-only.

Range: `[1, 4]`.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name = 'MEM_SIZE_CLASS_COUNT';
```

### Property Item: `DISK_MAX_DB_SIZE`

Meaning: maximum disk database size in bytes.

Default: `2^64 - 1`.

Dynamic Change Support: read-only.

Range: 64-bit `[2097152, 2^64]`.

Behavior: when the disk database exceeds the limit, the executing transaction fails and later non-`SELECT` SQL can fail.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'DISK_MAX_DB_SIZE';
```

### Property Item Group: `DOUBLE_WRITE_DIRECTORY` and `DOUBLE_WRITE_DIRECTORY_COUNT`

Meaning: configure where double write files are stored and how many double write directories are used.

Defaults:

- `DOUBLE_WRITE_DIRECTORY`: none.
- `DOUBLE_WRITE_DIRECTORY_COUNT`: `2`.

Dynamic Change Support: read-only; plan directory placement before startup and database storage rollout.

Range or values:

- `DOUBLE_WRITE_DIRECTORY`: directory path values; multiple values can be specified according to `DOUBLE_WRITE_DIRECTORY_COUNT`.
- `DOUBLE_WRITE_DIRECTORY_COUNT`: `[1, 16]`.

Behavior: double write files can be placed on different disks. Because each flusher uses a separate double write file, distributing directories across disks can improve flush performance.

Check SQL:

```sql
SELECT name, storedcount,
       value1, value2, value3, value4,
       value5, value6, value7, value8
FROM V$PROPERTY
WHERE name IN ('DOUBLE_WRITE_DIRECTORY', 'DOUBLE_WRITE_DIRECTORY_COUNT')
ORDER BY name;
```

### Property Item: `DRDB_FD_MAX_COUNT_PER_DATAFILE`

Meaning: maximum number of file descriptors that can be opened for I/O on one disk data file.

Default: `8`.

Dynamic Change Support: read-write; can be changed with `ALTER SYSTEM`.

Range: `[1, 1024]`.

Behavior: if file descriptors for a data file are already open up to this limit, later I/O waits until another I/O completes.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name = 'DRDB_FD_MAX_COUNT_PER_DATAFILE';
```

### Property Item: `VOLATILE_MAX_DB_SIZE`

Meaning: maximum total size of all volatile tablespaces.

Default: `2^32 + 1`.

Dynamic Change Support: read-only.

Range: `32-bit [2097152, 2^32 + 1]`; `64-bit [2097152, 2^64]`.

Caution: the configured volatile tablespace total cannot exceed memory capacity available from the operating system.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'VOLATILE_MAX_DB_SIZE';
```

### Property Item: `DISK_LOB_COLUMN_IN_ROW_SIZE`

Version: documented in 7.1, 7.3, and Altibase 8.1 verified source.

Meaning: default `IN ROW` threshold, in bytes, for LOB data stored directly in disk table segments.

Default: `4000`.

Dynamic Change Support: read-only; do not change with `ALTER SYSTEM` or `ALTER SESSION`.

Change method: treat as a database-initialization property. Verify the target database value before relying on default LOB placement.

Range: `[0, 4000]`.

Behavior: if the LOB data length is less than or equal to this value, the disk-table LOB value is saved in the table segment; otherwise it is saved in a LOB segment.

Related items: `BLOB`, `CLOB`, `LOB (...) STORE AS`, `MEMORY_LOB_COLUMN_IN_ROW_SIZE`, and `03_sql_ddl_generation.md` for disk LOB tablespace clauses.

Caution: this property applies to disk-table LOB storage. Memory tables use `MEMORY_LOB_COLUMN_IN_ROW_SIZE` instead.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name = 'DISK_LOB_COLUMN_IN_ROW_SIZE';
```

### Property Item: `MEMORY_LOB_COLUMN_IN_ROW_SIZE`

Version: documented in 7.1, 7.3, and Altibase 8.1 verified source.

Meaning: default `IN ROW` threshold, in bytes, for LOB data stored directly in memory table rows.

Default: `64`.

Dynamic Change Support: read-only; do not change with `ALTER SYSTEM` or `ALTER SESSION`.

Change method: treat as a database-initialization property. Verify the target database value before relying on default memory LOB placement.

Range: `[0, 4000]`.

Behavior: if the LOB data length is less than or equal to this value, it is saved in the fixed area; otherwise it is saved in the variable area.

Related items: `BLOB`, `CLOB`, `DISK_LOB_COLUMN_IN_ROW_SIZE`, and `MEMORY_VARIABLE_COLUMN_IN_ROW_SIZE`.

Caution: this property applies to memory-table LOB storage. Disk tables use `DISK_LOB_COLUMN_IN_ROW_SIZE` instead.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name = 'MEMORY_LOB_COLUMN_IN_ROW_SIZE';
```

### Property Item: `MEMORY_VARIABLE_COLUMN_IN_ROW_SIZE`

Version: documented in 7.1, 7.3, and Altibase 8.1 verified source.

Meaning: default `IN ROW` threshold, in bytes, for non-LOB variable columns in memory tables.

Default: `32`.

Dynamic Change Support: read-only; do not change with `ALTER SYSTEM` or `ALTER SESSION`.

Change method: treat as a database-initialization property. Verify the target database value before relying on default variable-column placement.

Range: `[0, 4000]`.

Behavior: variable column data at or below the threshold is stored in the fixed area; larger data is stored in the variable area.

Related items: `CHAR`, `VARCHAR`, `NCHAR`, `NVARCHAR`, `BYTE`, `VARBYTE`, `NIBBLE`, `BIT`, `VARBIT`, and `MEMORY_LOB_COLUMN_IN_ROW_SIZE`.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name = 'MEMORY_VARIABLE_COLUMN_IN_ROW_SIZE';
```

### Property Item: `LOB_OBJECT_BUFFER_SIZE`

Version: documented in 7.1, 7.3, and Altibase 8.1 verified source.

Meaning: maximum internal LOB data size, in bytes, used by the server while executing stored procedures, stored functions, or triggers whose parameters, internal variables, or return values are declared as LOB types.

Default: `32000`.

Dynamic Change Support: read-only; do not change with `ALTER SYSTEM` or `ALTER SESSION`.

Change method: configure statically before startup when the target version and workload require it, then verify with `V$PROPERTY`.

Range: `[32000, 104857600]`.

Related items: `BLOB`, `CLOB`, PSM LOB variables, trigger LOB variables, `TEMPORARY_LOB_ENABLE`, and `10_psm_stored_external_procedures.md`.

Caution: this property limits server-side PSM or trigger LOB processing. It does not change ordinary table LOB column maximum size or client LOB API limits.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name = 'LOB_OBJECT_BUFFER_SIZE';
```

### Property Item: `LOB_CACHE_THRESHOLD`

Version: documented in 7.1, 7.3, and Altibase 8.1 verified source.

Meaning: maximum LOB data size, in bytes, that can be stored in the client LOB cache.

Default: `8192`.

Dynamic Change Support: read-write; can be changed with `ALTER SYSTEM` or `ALTER SESSION`.

Change method: use `ALTER SESSION` for a session-level bulk-select test, or `ALTER SYSTEM` for a server-level default after testing the memory and fetch impact.

Range: `[0, 524288]`.

Values:

- `0`: do not temporarily store LOB data in the client LOB cache.
- Positive value: LOB data at or below the threshold can be cached on the client side.

Behavior: raising the threshold can improve bulk-select speed when many fetched LOB values fit under the cache limit.

Related items: client LOB fetch behavior, `V$SESSION.LOB_CACHE_THRESHOLD`, `12_c_cli_odbc_precompiler.md`, and `11_java_jdbc_spring.md`.

Caution: tune from measured LOB fetch workload and client memory behavior; do not raise the value only because table LOB columns are large.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name = 'LOB_CACHE_THRESHOLD';

SELECT id, lob_cache_threshold
FROM V$SESSION
WHERE id = SESSION_ID();
```

### Property Item: `ST_OBJECT_BUFFER_SIZE`

Version: documented in 7.1, 7.3, and Altibase 8.1 verified source.

Meaning: maximum size, in bytes, of a single spatial `Geometry Object`.

Default: `32000` (`32KByte`).

Dynamic Change Support: read-write; can be changed with `ALTER SYSTEM`.

Change method: change only after confirming spatial object size requirements and memory impact.

Range: `[32000, 104857600]`.

Related items: `GEOMETRY`, spatial functions, `19_spatial_nifi_tableau_misc.md`.

Caution: this property is an object-size limit for spatial geometry, not a LOB or JSON property. Include it when a customer asks about object-size limits across `LOB_OBJECT_BUFFER_SIZE`, `ST_OBJECT_BUFFER_SIZE`, or spatial data.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name = 'ST_OBJECT_BUFFER_SIZE';
```

### Property Item Group: Free-page and memory-allocation thresholds

Meaning: configure storage-manager thresholds used when memory pages, table free lists, and query-processor memory chunks are allocated.

Properties:

- `MIN_PAGES_ON_DB_FREE_LIST`: minimum free pages to retain on each database free-page list when pages are distributed; default `16`; range `[1, 2^32 - 1]`; read-only.
- `MIN_PAGES_ON_TABLE_FREE_LIST`: minimum free pages retained for each table free-list operation; default `1`; range `[1, 2^32 - 1]`; read-write with `ALTER SYSTEM`.
- `QP_MEMORY_CHUNK_SIZE`: memory allocation extension unit for the query processor; default `65536` bytes; range `[1024, 2^64 - 1]`; read-only.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name IN (
  'MIN_PAGES_ON_DB_FREE_LIST',
  'MIN_PAGES_ON_TABLE_FREE_LIST',
  'QP_MEMORY_CHUNK_SIZE'
)
ORDER BY name;
```

### Property Item Group: `RECYCLEBIN_*`

Meaning: configure whether dropped tables are moved to the recycle bin and how much disk or memory table data the recycle bin can hold.

Properties:

- `RECYCLEBIN_ENABLE`: default `0`; range `[0, 1]`; read-write; the documented change method is `ALTER SESSION`. `0` drops tables directly from the database system; `1` moves dropped tables to the recycle bin.
- `RECYCLEBIN_DISK_MAX_SIZE`: disk-table recycle bin size in bytes; default `2^64 - 1`; range `[0, 2^64 - 1]`; read-write with `ALTER SYSTEM`.
- `RECYCLEBIN_MEM_MAX_SIZE`: memory-table recycle bin size in bytes; default `4GB`; range `[0, 2^64 - 1]`; read-write with `ALTER SYSTEM`.

Behavior: tables in the recycle bin are renamed and marked as type `R`; DDL and `INSERT`/`UPDATE`/`DELETE` are not allowed on them, but `SELECT`, `FLASHBACK`, and `PURGE` handling remain possible. If the recycle bin already contains tables, changing `RECYCLEBIN_ENABLE` to `0` does not prevent querying, recovering, or purging those existing recycle-bin tables.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name IN (
  'RECYCLEBIN_ENABLE',
  'RECYCLEBIN_DISK_MAX_SIZE',
  'RECYCLEBIN_MEM_MAX_SIZE'
)
ORDER BY name;
```

### Property Item: `REDUCE_TEMP_MEMORY_ENABLE`

Meaning: controls whether variable-length column data temporarily stored in a memory tablespace uses the defined column length or only the actual data length.

Default: `0`.

Dynamic Change Support: read-write; can be changed with `ALTER SYSTEM`.

Range: `[0, 1]`.

Values:

- `0`: use temporary storage according to the defined variable-column length.
- `1`: use temporary storage according to the actual variable-column data length.

Caution: setting `1` can reduce memory use for temporary intermediate results in memory tablespaces, but query processing can become slower. Disk temporary tablespace remains the default intermediate-result location for disk tables or views unless a supported memory temporary tablespace hint is used.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name = 'REDUCE_TEMP_MEMORY_ENABLE';
```

### Property Item Group: System disk data tablespace file defaults

Meaning: defaults used when `SYS_TBS_DISK_DATA` is created and when data files are added without explicit size clauses.

Properties:

- `SYS_DATA_FILE_INIT_SIZE`: initial size of `system001.dbf` and default initial size for later added data files; default `100 * 1024 * 1024`; range `[8 * 8KB, 32GB]`; read-only.
- `SYS_DATA_FILE_MAX_SIZE`: maximum size of the allocated data file; default `2 * 1024 * 1024 * 1024`; range `[8 * 8KB, 32GB]`; read-only; must be at least `SYS_DATA_FILE_INIT_SIZE`, with documented minimum `64KB`.
- `SYS_DATA_FILE_NEXT_SIZE`: autoextend increment when `SYS_TBS_DISK_DATA` data files need more space; default `1 * 1024 * 1024`; range `[8 * 8KB, 32GB]`; read-only.
- `SYS_DATA_TBS_EXTENT_SIZE`: extent size when `SYS_TBS_DISK_DATA` is created; default `512 * 1024`; range `[40KB, 32GB]`; read-only.

Caution: if a data file reaches `SYS_DATA_FILE_MAX_SIZE` and other data files do not have at least `SYS_DATA_FILE_NEXT_SIZE` of available space, a tablespace-space error can occur. Extent size is decided at creation and cannot be changed afterward.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name IN (
  'SYS_DATA_FILE_INIT_SIZE',
  'SYS_DATA_FILE_MAX_SIZE',
  'SYS_DATA_FILE_NEXT_SIZE',
  'SYS_DATA_TBS_EXTENT_SIZE'
)
ORDER BY name;
```

### Property Item Group: System disk temporary tablespace file defaults

Meaning: defaults used when `SYS_TBS_DISK_TEMP` is created and when temporary data files are added without explicit size clauses.

Properties:

- `SYS_TEMP_FILE_INIT_SIZE`: initial size of `temp001.dbf` and default initial size for later added temporary data files; default `100 * 1024 * 1024`; range `[8 * 8KB, 32GB]`; read-only.
- `SYS_TEMP_FILE_MAX_SIZE`: maximum size of `temp001.dbf` or later temporary data files when no maximum is specified; default `2 * 1024 * 1024 * 1024`; range `[8 * 8KB, 32GB]`; read-only; must be at least `SYS_TEMP_FILE_INIT_SIZE`, with documented minimum `64KB`.
- `SYS_TEMP_FILE_NEXT_SIZE`: increment used when a `SYS_TBS_DISK_TEMP` data file lacks space; default `1 * 1024 * 1024`; range `[8 * 8KB, 32GB]`; read-only.
- `SYS_TEMP_TBS_EXTENT_SIZE`: extent size when `SYS_TBS_DISK_TEMP` is created; default `512 * 1024` in the authoritative source; range `[40KB, 32GB]`; read-only.

Caution: use the installed server's `V$PROPERTY` when a customer environment or extraction aid shows a different `SYS_TEMP_TBS_EXTENT_SIZE` default.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name IN (
  'SYS_TEMP_FILE_INIT_SIZE',
  'SYS_TEMP_FILE_MAX_SIZE',
  'SYS_TEMP_FILE_NEXT_SIZE',
  'SYS_TEMP_TBS_EXTENT_SIZE'
)
ORDER BY name;
```

### Property Item Group: System disk undo tablespace file defaults

Meaning: defaults used when `SYS_TBS_DISK_UNDO` is created and when undo data files are added without explicit size clauses.

Properties:

- `SYS_UNDO_FILE_INIT_SIZE`: initial size of `undo001.dbf` and default initial size for later added undo data files; default `100 * 1024 * 1024`; range `[32 * 8KB, 32GB]`; read-only.
- `SYS_UNDO_FILE_MAX_SIZE`: maximum size of `undo001.dbf` or later undo data files when no maximum is specified; default `2 * 1024 * 1024 * 1024`; range `[32 * 8KB, 32GB]`; read-only; must be at least `SYS_UNDO_FILE_INIT_SIZE`, with documented minimum `256KB`.
- `SYS_UNDO_FILE_NEXT_SIZE`: increment used when a `SYS_TBS_DISK_UNDO` data file lacks space; default `1 * 1024 * 1024`; range `[8 * 8KB, 32GB]`; read-only.
- `SYS_UNDO_TBS_EXTENT_SIZE`: extent size when `SYS_TBS_DISK_UNDO` is created; default `256 * 1024`; range `[40KB, 32GB]`; read-only.

Caution: `SYS_TBS_DISK_UNDO` is the single system disk undo tablespace used only for undo information. Users cannot create or delete tables, indexes, or other objects in this tablespace.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name IN (
  'SYS_UNDO_FILE_INIT_SIZE',
  'SYS_UNDO_FILE_MAX_SIZE',
  'SYS_UNDO_FILE_NEXT_SIZE',
  'SYS_UNDO_TBS_EXTENT_SIZE'
)
ORDER BY name;
```

### Property Item Group: User disk data tablespace file defaults

Meaning: defaults used when user disk data tablespace files are created or added without explicit size or extent clauses.

Properties:

- `USER_DATA_FILE_INIT_SIZE`: initial size of a user-defined data file; default `100 * 1024 * 1024`; range `[8 * 8KB, 32GB]`; read-only.
- `USER_DATA_FILE_MAX_SIZE`: maximum size of a user-defined data file when no maximum is specified; default `2 * 1024 * 1024 * 1024`; range `[8 * 8KB, 32GB]`; read-only; must be at least `USER_DATA_FILE_INIT_SIZE`, with documented minimum `64KB`.
- `USER_DATA_FILE_NEXT_SIZE`: increment used when a user disk data tablespace data file lacks space; default `1 * 1024 * 1024`; range `[8 * 8KB, 32GB]`; read-only.
- `USER_DATA_TBS_EXTENT_SIZE`: extent size when a user disk data tablespace is created; default `512 * 1024`; range `[2 * 8KB, 2^64 - 1]`; read-only.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name IN (
  'USER_DATA_FILE_INIT_SIZE',
  'USER_DATA_FILE_MAX_SIZE',
  'USER_DATA_FILE_NEXT_SIZE',
  'USER_DATA_TBS_EXTENT_SIZE'
)
ORDER BY name;
```

### Property Item Group: User temporary tablespace file defaults

Meaning: defaults used when user temporary tablespace files are created or added without explicit size or extent clauses.

Properties:

- `USER_TEMP_FILE_INIT_SIZE`: initial size of a user-defined temporary data file; default `100 * 1024 * 1024`; range `[8 * 8KB, 32GB]`; read-only.
- `USER_TEMP_FILE_MAX_SIZE`: maximum size of a user-defined temporary data file when no maximum is specified; default `2 * 1024 * 1024 * 1024`; range `[8 * 8KB, 32GB]`; read-only; selected sources state that it must be at least `USER_DATA_FILE_INIT_SIZE`, with documented minimum `64KB`.
- `USER_TEMP_FILE_NEXT_SIZE`: increment used when a user temporary data file lacks space; default `1 * 1024 * 1024`; range `[8 * 8KB, 32GB]`; read-only.
- `USER_TEMP_TBS_EXTENT_SIZE`: extent size when a user temporary tablespace is created; default `512 * 1024` in the authoritative source; range `[5 * 8KB, 2^64 - 1]`; read-only.

Caution: selected sources state a minimum of two pages for `USER_TEMP_TBS_EXTENT_SIZE` in the description while the value range is `[5 * 8KB, 2^64 - 1]`; ask for the exact installed version and check `V$PROPERTY` before resolving a boundary-size dispute.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name IN (
  'USER_TEMP_FILE_INIT_SIZE',
  'USER_TEMP_FILE_MAX_SIZE',
  'USER_TEMP_FILE_NEXT_SIZE',
  'USER_TEMP_TBS_EXTENT_SIZE'
)
ORDER BY name;
```

### Property Item: `TABLE_BACKUP_FILE_BUFFER_SIZE`

Meaning: I/O buffer size, in bytes, for table backup files used when adding or dropping columns in memory tables.

Default: `1024`.

Dynamic Change Support: read-only.

Range: `[0, 1048576]`.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name = 'TABLE_BACKUP_FILE_BUFFER_SIZE';
```

### Property Item: `TABLE_COMPACT_AT_SHUTDOWN`

Meaning: controls whether tables are compacted when the database shuts down.

Default: `1`.

Dynamic Change Support: read-write; can be changed with `ALTER SYSTEM`.

Range: `[0, 1]`.

Caution: the manuals recommend `1` to reduce memory waste for tables after database restart.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name = 'TABLE_COMPACT_AT_SHUTDOWN';
```

### Property Item Group: Temporary page storage defaults

Meaning: configure hash bucket density and allocation chunk size for temporary data pages.

Properties:

- `TEMP_HASH_BUCKET_DENSITY`: percentage controlling how many temporary table page frames one hash bucket manages; default `1`; range `[1, 100]` in the authoritative sources; read-only. Larger values reduce the number of buckets and memory use, but increase per-bucket operation cost.
- `TEMP_PAGE_CHUNK_COUNT`: number of temporary data pages allocated at one time; default `128`; range `[1, 2^32 - 1]`; read-only.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name IN ('TEMP_HASH_BUCKET_DENSITY', 'TEMP_PAGE_CHUNK_COUNT')
ORDER BY name;
```

### Property Item: `TEMPORARY_LOB_ENABLE`

Version: Altibase 8.1 verified source property. It is not part of the selected 7.1 or 7.3 baselines.

Meaning: enables or disables Temporary LOB use. Native `JSON` processing requires Temporary LOB support.

Default: `1`.

Dynamic Change Support: read-only; do not change with `ALTER SYSTEM` or `ALTER SESSION`.

Change method: configure statically before startup if the site has a verified reason to disable Temporary LOB; verify the installed 8.1 server before changing a JSON workload.

Range: `[0, 1]`.

Values:

- `0`: do not use Temporary LOB.
- `1`: use Temporary LOB.

Related items: `JSON`, `V$TEMPORARY_LOBS`, `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`, `MEMORY_TEMPLOB_PIECE_SIZE`, and `ALTER SESSION SET FREE TEMPORARY LOB`.

Caution: `JSON` type processing uses Temporary LOB, so disabling this property can make native JSON workflows fail.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name = 'TEMPORARY_LOB_ENABLE';

SELECT type, id, alloced_size, open_count
FROM V$TEMPORARY_LOBS;
```

### Property Item: `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`

Version: Altibase 8.1 verified source property. It is not part of the selected 7.1 or 7.3 baselines.

Meaning: maximum total memory, in bytes, that Temporary LOB can allocate.

Default: `2147483648` (`2G`).

Dynamic Change Support: read-write; can be changed with `ALTER SYSTEM`.

Change method: use `ALTER SYSTEM` only after estimating Temporary LOB and JSON workload memory. Keep a rollback value and verify runtime use with `V$TEMPORARY_LOBS`.

Range: `[16777216, 2^64]`.

Behavior: if a Temporary LOB allocation request exceeds this limit, memory allocation fails and the transaction is treated as an error.

Important note: Temporary LOB uses memory separate from `MEM_MAX_DB_SIZE`; size both limits deliberately.

Related items: `TEMPORARY_LOB_ENABLE`, `MEMORY_TEMPLOB_PIECE_SIZE`, `V$TEMPORARY_LOBS`, `JSON`, PSM LOB variables, and `10_psm_stored_external_procedures.md`.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name = 'MEMORY_TEMPLOB_MAX_ALLOC_SIZE';

SELECT type, id, alloced_size, open_count
FROM V$TEMPORARY_LOBS
ORDER BY type, id;
```

### Property Item: `MEMORY_TEMPLOB_PIECE_SIZE`

Version: Altibase 8.1 verified source property. It is not part of the selected 7.1 or 7.3 baselines.

Meaning: memory piece size, in bytes, used to split and store Temporary LOB data.

Default: `1048576` (`1M`).

Dynamic Change Support: read-only; do not change with `ALTER SYSTEM` or `ALTER SESSION`.

Change method: configure statically before startup when the Temporary LOB workload requires a different piece size.

Range: `[32768, 1048576]`.

Tuning note: larger values can improve large Temporary LOB processing speed but can waste memory for many small Temporary LOB values. Smaller values can improve memory efficiency for many small Temporary LOB values.

Related items: `TEMPORARY_LOB_ENABLE`, `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`, `V$TEMPORARY_LOBS`, `JSON`, and PSM LOB variables.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name = 'MEMORY_TEMPLOB_PIECE_SIZE';
```

### Property Item: `PCTFREE`

Meaning: minimum percentage of page space reserved for future updates when disk tables are created without an explicit `PCTFREE`.

Default: `10`.

Dynamic Change Support: read-only property default.

Range: `[0, 99]`.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'PCTFREE';
```

### Property Item: `PCTUSED`

Meaning: threshold percentage below which a disk page can return from update-only state to insert-eligible state.

Default: `40`.

Dynamic Change Support: read-only property default.

Range: `[0, 99]`.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'PCTUSED';
```

### Property Item: `HASH_AREA_SIZE`

Meaning: memory size, in bytes, of each temporary table used for hash operations.

Default: `4MB`.

Dynamic Change Support: read-write; can be changed with `ALTER SYSTEM`.

Range: `[3M, 2^64 - 1]`.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'HASH_AREA_SIZE';
```

### Property Item: `SORT_AREA_SIZE`

Meaning: memory size, in bytes, of each temporary table used for sort operations.

Default: `1048576`.

Dynamic Change Support: read-write; can be changed with `ALTER SYSTEM`.

Range: `[512, 2^64 - 1]`.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'SORT_AREA_SIZE';
```

### Property Item: `EXECUTE_STMT_MEMORY_MAXIMUM`

Meaning: maximum memory, in bytes, available to execute a single query statement.

Default: 7.1 `1073741824` (`1G`); 7.3 and 8.1 `2147483648` (`2G`).

Dynamic Change Support: read-write; can be changed with `ALTER SYSTEM`.

Range: `[1024 * 1024, 2^64 - 1]`.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'EXECUTE_STMT_MEMORY_MAXIMUM';
```

### Property Item: `PREPARE_STMT_MEMORY_MAXIMUM`

Meaning: maximum memory, in bytes, available to prepare a query statement.

Default: `200M`.

Dynamic Change Support: read-write; can be changed with `ALTER SYSTEM`.

Range: `[1024 * 1024, 2^64 - 1]`.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'PREPARE_STMT_MEMORY_MAXIMUM';
```

### Property Item: `SQL_PLAN_CACHE_SIZE`

Meaning: maximum SQL plan cache size in bytes.

Default: `64M`.

Dynamic Change Support: read-write; can be changed with `ALTER SYSTEM`.

Range: `[0, 2^64 - 1]`.

Behavior: `0` disables SQL plan cache.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'SQL_PLAN_CACHE_SIZE';

SELECT max_cache_size
FROM V$SQL_PLAN_CACHE;
```

### Property Item: `OPTIMIZER_FEATURE_ENABLE`

Meaning: controls a set of optimizer-related behavior using a version-like compatibility value.

Default: Altibase server version. In 8.1, release notes record the default as changed to `8.1.0.0.1`.

Dynamic Change Support: read-write for supported values with `ALTER SYSTEM`.

Range: supported optimizer compatibility values vary by version; check the installed `V$PROPERTY` value and the version-specific manual.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'OPTIMIZER_FEATURE_ENABLE';
```

### Property Item: `CHECKPOINT_INTERVAL_IN_LOG`

Meaning: checkpoint request interval based on the number of log file replacements.

Default: `10` in the 8.1 baseline. The 8.1 release notes record this default as changed from `100` to `10`.

Dynamic Change Support: read-write; can be changed with `ALTER SYSTEM`.

Range: `[1, 2^32 - 1]`.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'CHECKPOINT_INTERVAL_IN_LOG';
```

### Property Item: `FAST_START_LOGFILE_TARGET`

Meaning: target number of log files read during recovery after restart; lower values can reduce recovery time at the cost of more page flushing during runtime.

Default: `10` in the 8.1 baseline. The 8.1 release notes record this default as changed from `100` to `10`.

Dynamic Change Support: read-write; can be changed with `ALTER SYSTEM`.

Range: `[1, 2^32 - 1]`.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'FAST_START_LOGFILE_TARGET';
```

### Property Item: `LOG_CREATE_METHOD`

Meaning: system call method used to create log files.

Default: `1` on Linux in the 8.1 baseline; release notes record the default as changed from `0` to `1`.

Dynamic Change Support: read-only.

Range: `[0, 1]`.

Values:

- `0`: `write()` system call.
- `1`: `fallocate()` system call on Linux.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'LOG_CREATE_METHOD';
```

### Property Item: `CHECKPOINT_SCALE_SINGLE_DW_BUFFER_SIZE`

Version: 8.1 baseline property.

Meaning: size of the double write buffer and image file used when checkpoint scale is `SINGLE`.

Default: `524288000` (`500M`).

Dynamic Change Support: read-write.

Range: `[1M, 2G]`.

Tuning note: set to half the largest checkpoint image file size.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'CHECKPOINT_SCALE_SINGLE_DW_BUFFER_SIZE';
```

### Property Item: `TRCLOG_EXPLAIN_TYPE`

Version: 8.1 release-note property.

Meaning: related to JSON-formatted execution plan output in trace logging.

Default: verify on the installed server with `V$PROPERTY`; the verified manual source does not provide a value definition.

Dynamic Change Support: verify on the installed server and version-specific property output; do not infer values.

Range: verify on the installed server; do not invent values from the release-note-only entry.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'TRCLOG_EXPLAIN_TYPE';
```

### Property Item: `TRCLOG_JSON_PLAN_INDENT_DEPTH`

Version: 8.1 release-note property.

Meaning: related to indentation depth for JSON-formatted execution plan output.

Default: verify on the installed server with `V$PROPERTY`; the verified manual source does not provide a value definition.

Dynamic Change Support: verify on the installed server and version-specific property output; do not infer values.

Range: verify on the installed server; do not invent values from the release-note-only entry.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'TRCLOG_JSON_PLAN_INDENT_DEPTH';
```

### Property Item: `AUTO_COMMIT`

Meaning: controls whether each SQL statement is handled as a separate transaction and committed automatically.

Default: `1`.

Dynamic Change Support: read-write; can be changed with `ALTER SYSTEM`, and sessions can set autocommit behavior.

Range: `[0, 1]`.

Values:

- `0`: non-autocommit mode.
- `1`: autocommit mode.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'AUTO_COMMIT';
```

### Property Item: `ISOLATION_LEVEL`

Meaning: default transaction isolation level.

Default: `0`.

Dynamic Change Support: read-only property default.

Range: `[0, 2]`.

Values:

- `0`: committed read.
- `1`: repeatable read.
- `2`: no phantom.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'ISOLATION_LEVEL';
```

### Property Item: `DEFAULT_DATE_FORMAT`

Meaning: default input and output format for `DATE` values.

Default: `DD-MON-RRRR`.

Dynamic Change Support: read-only property default.

Range: date format string.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'DEFAULT_DATE_FORMAT';
```

### Property Item: `TIME_ZONE`

Meaning: session time zone. Region names, abbreviations, or UTC offset strings such as `+09:00` can be used.

Default: `OS_TZ`.

Dynamic Change Support: read-write; can be changed with `ALTER SESSION`.

Range: values listed in `V$TIME_ZONE_NAMES`, or accepted UTC offset strings.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'TIME_ZONE';

SELECT name, utc_offset
FROM V$TIME_ZONE_NAMES
WHERE name = 'Asia/Seoul';

SELECT time_zone
FROM V$SESSION
WHERE id = SESSION_ID();
```

### Property Item: `NLS_NUMERIC_CHARACTERS`

Meaning: decimal character and group separator for numeric display and parsing.

Default: determined by `NLS_TERRITORY`.

Dynamic Change Support: read-write; can be changed with `ALTER SESSION`.

Range: first two characters of the configured string are used as decimal character and group separator.

Example:

```sql
ALTER SESSION SET NLS_NUMERIC_CHARACTERS='.,';
```

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'NLS_NUMERIC_CHARACTERS';
```

### Property Item: `QUERY_TIMEOUT`

Meaning: maximum query execution time in seconds before the transaction is partially rolled back.

Default: `600`.

Dynamic Change Support: read-write; can be changed with `ALTER SYSTEM` or `ALTER SESSION`.

Range: `[0, 2^32 - 1]`.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'QUERY_TIMEOUT';
```

### Property Item: `FETCH_TIMEOUT`

Meaning: timeout in seconds for excessive fetch duration by client `SELECT` processing. On timeout, the session is disconnected and the transaction rolls back.

Default: `60`.

Dynamic Change Support: read-write; can be changed with `ALTER SYSTEM` or `ALTER SESSION`.

Range: `[0, 2^32 - 1]`.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'FETCH_TIMEOUT';
```

### Property Item: `IDLE_TIMEOUT`

Meaning: maximum idle session time in seconds before session disconnect and transaction rollback.

Default: `0`.

Dynamic Change Support: read-write; can be changed with `ALTER SYSTEM` or `ALTER SESSION`.

Range: `[0, 2^32 - 1]`.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'IDLE_TIMEOUT';
```

### Property Item: `LOGIN_TIMEOUT`

Meaning: permitted time in seconds for authorization to complete after connecting to an Altibase port.

Default: `0`.

Dynamic Change Support: read-write property.

Range: `[0, 2^32 - 1]`.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'LOGIN_TIMEOUT';
```

### Property Item: `DDL_LOCK_TIMEOUT`

Meaning: wait time in seconds to obtain a lock for DDL when the target table is locked.

Default: `0`.

Dynamic Change Support: read-write; can be changed with `ALTER SYSTEM`.

Range: `[-1, 65535]`.

Values:

- `-1`: wait indefinitely.
- `0`: return an error immediately if the lock cannot be obtained.
- Positive value: wait that many seconds.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'DDL_LOCK_TIMEOUT';
```

### Property Item: `DDL_TIMEOUT`

Meaning: maximum DDL execution time in seconds.

Default: `0`, meaning wait indefinitely.

Dynamic Change Support: read-write; can be changed with `ALTER SYSTEM` or `ALTER SESSION`.

Range: `[0, 2^32 - 1]`.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'DDL_TIMEOUT';
```

### Property Item: `UTRANS_TIMEOUT`

Meaning: timeout in seconds for long write transactions, used to prevent abnormal log file growth.

Default: `3600`.

Dynamic Change Support: read-write; can be changed with `ALTER SYSTEM` or `ALTER SESSION`.

Range: `[0, 2^32 - 1]`.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'UTRANS_TIMEOUT';
```

### Property Item: `PORT_NO`

Meaning: TCP/IP client-server listener port.

Default: `20300`.

Dynamic Change Support: read-only.

Range: `[1024, 65535]`.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'PORT_NO';
```

### Property Item: `MAX_CLIENT`

Meaning: maximum number of client connections.

Default: `1000`.

Dynamic Change Support: read-only.

Range: `[0, 65535]`, with an effective upper bound reduced by `JOB_THREAD_COUNT` when job threads are configured.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'MAX_CLIENT';
```

### Property Item: `REPLICATION_PORT_NO`

Meaning: local ordinary replication port.

Default: `0`.

Dynamic Change Support: read-only.

Range: `[0, 65535]`.

Behavior: `0` disables ordinary replication listener use for this property.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'REPLICATION_PORT_NO';
```

### Property Item: `REPLICATION_SSL_PORT_NO`

Version: 8.1 baseline property.

Meaning: local SSL replication port used when replication connects with SSL.

Default: `0`.

Dynamic Change Support: read-only.

Range: `[0, 65535]`.

Behavior: `0` means SSL replication cannot be connected through this property. Before using SSL replication, complete SSL configuration on each replication target server.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'REPLICATION_SSL_PORT_NO';
```

### Property Item: `SSL_ENABLE`

Meaning: enables or disables SSL/TLS for Altibase client/server communication.

Default: `0`.

Dynamic Change Support: read-only.

Range: `[0, 1]`.

Values:

- `0`: disable SSL/TLS.
- `1`: enable SSL/TLS.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'SSL_ENABLE';
```

### Property Item: `SSL_PORT_NO`

Meaning: SSL/TLS listener port for client/server communication.

Default: `20443`.

Dynamic Change Support: read-write; can be changed with `ALTER SYSTEM`. After changing it, verify SSL/TLS listener and client connection behavior.

Range: `[1024, 65535]`.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'SSL_PORT_NO';
```

### Property Item: `SSL_CA`

Meaning: path to CA certificate file used to verify received certificates.

Default: none.

Dynamic Change Support: read-only.

Range: path value.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'SSL_CA';
```

### Property Item: `SSL_CERT`

Meaning: path to the Altibase server certificate.

Default: none.

Dynamic Change Support: read-only.

Range: path value.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'SSL_CERT';
```

### Property Item: `SSL_KEY`

Meaning: path to the server private key.

Default: none.

Dynamic Change Support: read-only.

Range: path value.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'SSL_KEY';
```

### Property Item: `PSM_CASE_SENSITIVE_MODE`

Version: documented in 7.1, 7.3, and Altibase 8.1 verified source.

Meaning: controls case sensitivity when PSM refers to `RECORD` and `ROWTYPE` column names or label names.

Default: 7.1 `0`; 7.3 and 8.1 `1`.

Dynamic Change Support: read-write; can be changed with `ALTER SYSTEM`.

Range: `[0, 1]`.

Values:

- `0`: case-insensitive behavior.
- `1`: case-sensitive behavior.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name = 'PSM_CASE_SENSITIVE_MODE';
```

### Property Item: `PSM_CURSOR_OPEN_LIMIT`

Version: documented in 7.1, 7.3, and Altibase 8.1 verified source.

Meaning: maximum number of cursors that one session can open by using the `DBMS_SQL` package.

Default: `32`.

Dynamic Change Support: source-sensitive. The detailed Korean property section says read-only, while the property alter-level summary lists `SYSTEM`; verify the installed target version before generating dynamic change SQL.

Range: `[1, 1024]`.

Related items: `DBMS_SQL`, dynamic SQL in PSM, `10_psm_stored_external_procedures.md`.

Caution: if the customer hits cursor-limit errors in PSM, ask for Altibase version, current `V$PROPERTY` output, package code pattern, and open-cursor cleanup before recommending a value change.

Check SQL:

```sql
SELECT name, attr, value1, min, max
FROM V$PROPERTY
WHERE name = 'PSM_CURSOR_OPEN_LIMIT';
```

### Property Item: `PSM_FILE_OPEN_LIMIT`

Version: documented in 7.1, 7.3, and Altibase 8.1 verified source.

Meaning: maximum number of stored-procedure file handles that can be open per session.

Default: `16`.

Dynamic Change Support: read-write; selected source summary lists `SYSTEM`.

Change method: use `ALTER SYSTEM` only after verifying the installed version and file-handle workload.

Range: `[0, 128]`.

Related items: PSM file operations and `10_psm_stored_external_procedures.md`.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name = 'PSM_FILE_OPEN_LIMIT';
```

### Property Item: `PSM_IGNORE_NO_DATA_FOUND_ERROR`

Version: documented in 7.1, 7.3, and Altibase 8.1 verified source.

Meaning: controls whether a stored function suppresses the system-defined `NO_DATA_FOUND` exception when a PSM `SELECT ... INTO` statement returns no row.

Default: `0`.

Dynamic Change Support: read-write; can be changed with `ALTER SYSTEM`.

Range: `[0, 1]`.

Values:

- `0`: raise `NO_DATA_FOUND` when the result set has no row.
- `1`: do not raise `NO_DATA_FOUND` for stored functions in that case.

Related items: PSM exception handlers, `SQLCODE`, `SQLERRM`, `10_psm_stored_external_procedures.md`.

Caution: do not use this property to hide unexpected missing-data bugs. Ask for the stored function body and expected result cardinality before recommending `1`.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name = 'PSM_IGNORE_NO_DATA_FOUND_ERROR';
```

### Property Item: `PSM_MAX_DDL_REFERENCE_DEPTH`

Version: documented in 7.3 and Altibase 8.1 verified source; not found in the selected 7.1 General Reference 1 inventory.

Meaning: limits the recursive call or reference depth used while compiling PSM. If the configured depth is exceeded, compilation fails with an error.

Default: `128`.

Dynamic Change Support: read-write property in the detailed source; verify the installed target version before changing.

Range: `[64, 2^32 - 1]`.

Related items: nested PSM dependencies, recursive PSM calls, package compile order, `10_psm_stored_external_procedures.md`.

Caution: when a compile error depends on object dependency depth, ask for Altibase version, full compile error, object dependency chain, and current property value before recommending a higher limit.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name = 'PSM_MAX_DDL_REFERENCE_DEPTH';
```

### Property Item Group: PSM character default-precision properties

Version: documented in 7.1, 7.3, and Altibase 8.1 verified source.

Meaning: controls the precision assigned when PSM procedure parameters, function parameters, or function return values use `CHAR`, `VARCHAR`, `NCHAR`, or `NVARCHAR` without an explicit size.

Properties:

- `PSM_PARAM_AND_RETURN_WITHOUT_PRECISION_ENABLE`: default `1`; range `[0, 1]`; read-only. `1` uses the default-precision properties below; `0` makes the omitted size `1`.
- `PSM_CHAR_DEFAULT_PRECISION`: read-only; range `[1, 65534]`; default 7.1 `32767`, 7.3 and 8.1 `32000`.
- `PSM_VARCHAR_DEFAULT_PRECISION`: read-only; range `[1, 65534]`; default 7.1 `32767`, 7.3 and 8.1 `32000`.
- `PSM_NCHAR_UTF16_DEFAULT_PRECISION`: read-only; range `[1, 32766]`; default 7.1 `16383`, 7.3 and 8.1 `16000`.
- `PSM_NCHAR_UTF8_DEFAULT_PRECISION`: read-only; range `[1, 21843]`; default 7.1 `10921`, 7.3 and 8.1 `10666`.
- `PSM_NVARCHAR_UTF16_DEFAULT_PRECISION`: read-only; range `[1, 32766]`; default 7.1 `16383`, 7.3 and 8.1 `16000`.
- `PSM_NVARCHAR_UTF8_DEFAULT_PRECISION`: read-only; range `[1, 21843]`; default 7.1 `10921`, 7.3 and 8.1 `10666`.

Use when: a PSM procedure or function declares character parameters or return values without precision and the customer asks why inferred size differs by version or character set.

Related items: `CHAR`, `VARCHAR`, `NCHAR`, `NVARCHAR`, PSM data type limits, and `10_psm_stored_external_procedures.md`.

Caution: prefer explicit sizes in generated PSM signatures. Do not rely on these defaults when migrating Oracle PL/SQL or when a function return value is consumed by client code.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name IN (
  'PSM_PARAM_AND_RETURN_WITHOUT_PRECISION_ENABLE',
  'PSM_CHAR_DEFAULT_PRECISION',
  'PSM_VARCHAR_DEFAULT_PRECISION',
  'PSM_NCHAR_UTF16_DEFAULT_PRECISION',
  'PSM_NCHAR_UTF8_DEFAULT_PRECISION',
  'PSM_NVARCHAR_UTF16_DEFAULT_PRECISION',
  'PSM_NVARCHAR_UTF8_DEFAULT_PRECISION'
)
ORDER BY name;
```

### Property Item: `LISTAGG_PRECISION`

Version: documented in 7.1, 7.3, and Altibase 8.1 verified source.

Meaning: size of the `VARCHAR` returned by `LISTAGG`.

Default: `4000`.

Dynamic Change Support: read-write; can be changed with `ALTER SYSTEM`.

Range: 7.1 `[0, 32000]`; 7.3 and 8.1 `[1, 32000]`.

Related items: `LISTAGG`, aggregate SQL, `04_sql_dml_oracle_compatibility.md`.

Caution: for 7.1, verify the installed version when `0` is proposed because 7.3 and 8.1 sources use `[1, 32000]`.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name = 'LISTAGG_PRECISION';
```

### Property Item: `REGEXP_MODE`

Version: 7.1, 7.3, and 8.1 documented property where PCRE2 regular expression processing is available; verify exact behavior against the installed build.

Meaning: selects regular expression syntax mode.

Default: `0`.

Dynamic Change Support: read-write.

Range: `[0, 1]`.

Values:

- `0`: Altibase regular expression mode with partial POSIX BRE and ERE support.
- `1`: PCRE2-compatible mode; available when the server character set is `US7ASCII` or `UTF-8`.

Check SQL:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name = 'REGEXP_MODE';
```

### Property Item: `VARRAY_MEMORY_MAXIMUM`

Version: documented in 7.3 and Altibase 8.1 verified source. It is not part of the selected 7.1 General Reference 1 inventory.

Meaning: maximum memory, in bytes, allowed for one `VARRAY` variable.

Default: `209715200` (`200M`).

Dynamic Change Support: read-write; can be changed with `ALTER SYSTEM`.

Range: `[1048576, 2^64 - 1]`.

Behavior: if a `VARRAY` expansion exceeds this limit, an error occurs.

Related items: PSM `VARRAY`, `BULK COLLECT`, `10_psm_stored_external_procedures.md`, and `MEMORY_TEMPLOB_MAX_ALLOC_SIZE` when the `VARRAY` stores LOB values in 8.1 Temporary LOB workflows.

Caution: for 7.1 answers, do not suggest PSM `VARRAY` or this property unless the customer provides a target build source proving support.

Check SQL:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name = 'VARRAY_MEMORY_MAXIMUM';
```

## Attachment Cross-References

- Use `03_sql_ddl_generation.md` when a type or property answer must become executable table, index, user, replication, or `ALTER SYSTEM` syntax.
- Use `04_sql_dml_oracle_compatibility.md` for DML, condition, function, and Oracle-conversion behavior affected by data type semantics.
- Use `06_data_dictionary_performance_views.md` for `V$PROPERTY`, object-column, Temporary LOB, and version-availability verification SQL.
- Use `08_performance_tuning_monitoring.md` when a property affects optimizer behavior, memory use, plan cache, result cache, statistics, or server tuning.
- Use `10_psm_stored_external_procedures.md` when PSM default precision, `DBMS_SQL`, `NO_DATA_FOUND`, `VARRAY`, or Temporary LOB behavior appears inside stored code.
- Use `12_c_cli_odbc_precompiler.md` for CLI, ODBC, Altibase C Interface, and APRE type conversion and LOB handling questions.
- Use `18_security_ssl_tls.md` for SSL/TLS property names, ports, certificate paths, and security-facing property checks.
- Use `19_spatial_nifi_tableau_misc.md` for `ST_OBJECT_BUFFER_SIZE`, `GEOMETRY`, and spatial object-size questions.

## Property Answer Checklist

- State the Altibase version used as the baseline.
- Use exact property name capitalization.
- State whether the property is read-only or read-write.
- State whether the change can use `ALTER SYSTEM`, `ALTER SESSION`, restart, or database recreation.
- Include `V$PROPERTY` check SQL.
- For 8.1 JSON or Temporary LOB issues, also include `V$TEMPORARY_LOBS`.
- For PSM signature-size questions, prefer explicit `CHAR`, `VARCHAR`, `NCHAR`, or `NVARCHAR` precision over relying on default-precision properties.
- For VARRAY questions, include the target version because `VARRAY_MEMORY_MAXIMUM` is documented in 7.3 and Altibase 8.1 verified source, not in the selected 7.1 inventory.
- For SSL replication, distinguish `REPLICATION_SSL_PORT_NO` from ordinary `REPLICATION_PORT_NO` and ordinary client `SSL_PORT_NO`.
- If the verified source does not define values, say to verify with `V$PROPERTY` instead of inventing defaults or ranges.

## Residual Scope

- Data type and property blocks focus on high-retrieval items and version-sensitive differences. When a property, default, range, or dynamic-change rule is not listed here, verify it with the installed target version and `V$PROPERTY` instead of extrapolating from adjacent properties.
