# 10. PSM, Stored Procedures, and External Procedures
## Package Role
- Provides guarded PSM, stored procedure, stored function, anonymous block, package, trigger, TYPESET, collection, cursor, dynamic SQL, exception, pragma, and external procedure routes.
- Use it when a customer wants source-backed stored logic or native external-procedure first drafts, including compile/deploy preconditions and iSQL execution shape.
- Route SQL inside PSM to `04_sql_dml_oracle_compatibility.md`, DDL shell syntax to `03_sql_ddl_generation.md`, C client API work to `12_c_cli_odbc_precompiler.md`, and exact errors to `07_error_messages_troubleshooting.md`.
## Applicable Versions And Authority
- 7.1: Based on Korean authoritative Stored Procedures and External Procedures routes, with English extraction aids used only as support.
- 7.3: Based on Korean authoritative Stored Procedures and External Procedures routes plus release-note routes for version-gated PSM features.
- 8.1: Based on Altibase 8.1 verified source Stored Procedures, External Procedures, SQL Reference, General Reference, and release-note routes.
- Production PSM and external procedure claims require exact target version, patch level, object definition, compile or runtime output, native library path, OS, compiler, ABI, parameter types, privileges, and validation evidence.
## Questions This File Can Answer
- How should Altibase PSM procedures, functions, packages, triggers, anonymous blocks, cursors, collections, and exceptions be drafted and verified?
- Which inputs are required before writing external procedure or external function registration and deployment steps?
- How should Oracle PL/SQL-like patterns be adapted without treating Altibase as fully Oracle-compatible?
- When must the answer stop until compile output, library path, platform, privilege, object definition, or installed tool evidence is supplied?
## Retrieval Alias Index
- Aliases and customer wording: PSM, stored procedure, stored function, anonymous block, package, trigger, TYPESET, REF CURSOR, dynamic SQL, exception, pragma, external procedure, external library.
- Exact-token anchors: `CREATE PROCEDURE`, `CREATE FUNCTION`, `CREATE PACKAGE`, `CREATE PACKAGE BODY`, `CREATE LIBRARY`, `LANGUAGE C`, `EXTERNAL NAME`, `PARAMETERS`, `AUTHID`, `NOCOPY`, `VARRAY`, `TYPESET`, `OPEN FOR`, `PRAGMA AUTONOMOUS_TRANSACTION`, `DBMS_OUTPUT`, `END;`, `/`.
- Route native compilation, shared-library deployment, and runtime loader failures through the C/client package and troubleshooting package when the question leaves stored-object syntax.
## Source Routes
Use these source-boundary routes for source-backed synthesis. They identify the source ID and source-pack block that must be rechecked before item-level production claims.

- 7.1 Stored Procedures route: `SRC-000075/BLOCK-000897`.
- 7.1 External Procedures route: `SRC-000055/BLOCK-000896`.
- 7.3 Stored Procedures route: `SRC-000136/BLOCK-000902`.
- 7.3 External Procedures route: `SRC-000119/BLOCK-000901`.
- 8.1 Stored Procedures route: `SRC-000196/BLOCK-000907`.
- 8.1 External Procedures route: `SRC-000179/BLOCK-000906`.
- 8.1 SQL syntax and object-validation route: `SRC-000194/BLOCK-000888`.
- 8.1 data type and property route for PSM feature boundaries: `SRC-000180/BLOCK-000519`.
- 7.3 release-note route for PSM feature boundary: `SRC-000451/BLOCK-000824`.
- 8.1 release-note route for Temporary LOB and feature boundary: `SRC-000452/BLOCK-000826`.
- Exact compiler output, installed client library or driver files, DSN entries, classpath, utility help output, generated artifacts, runtime logs, patch levels, and protected-operation claims must be rechecked against the target-version source route and customer evidence.
- AID-derived support is not a separate upload file; preserve Korean-source-verified, link-validated, English-only, and source-limitation labels whenever exact AID evidence is used.
- Internal baseline, playbook, guardrail, job, and local-path identifiers stay outside this upload Markdown.
## Task And Playbook Routing
- Stored logic generation routing: require target version, patch level, schema, object names, parameter modes, data types, referenced tables, privileges, transaction expectations, SQL side effects, and compile plan before copy-ready PSM.
- External procedure routing: require OS, compiler, bitness, ABI, client/server installation, library path, source code, exported symbol, parameter mapping, deployment privilege, restart or reload requirement, runtime log path, and rollback plan before production instructions.
- Migration routing: treat Oracle PL/SQL compatibility as a conversion task; verify each package, pragma, type, exception, autonomous transaction, and side-effect rule against Altibase sources before claiming compatibility.
- Generated-test coverage remains deferred; include compile checks, validation SQL, and cleanup notes but do not claim a complete source-backed test-generation route.
## Answer-Ready Reference
The reference below preserves the validated answer-ready content for this topic. Section headings are nested so the package-level routing sections above remain the top-level retrieval contract.
### Applicable Versions

- 7.1: Based on Altibase 7.1 Stored Procedures Manual, External Procedures Manual, SQL Reference, and General Reference.
- 7.3: Based on Altibase 7.3 Stored Procedures Manual, External Procedures Manual, SQL Reference, General Reference, and release-note coverage for VARRAY.
- 8.1: Based on Altibase 8.1 verified source Stored Procedures Manual, External Procedures Manual, SQL Reference, General Reference, and release-note coverage for Temporary LOB.

### Questions This File Can Answer

- How should Altibase PSM procedures, functions, anonymous blocks, and packages be written?
- Which Oracle PL/SQL constructs are similar, and where must code be changed?
- How are `%TYPE`, `%ROWTYPE`, `RECORD`, `ASSOCIATIVE ARRAY`, `VARRAY`, `REF CURSOR`, and `TYPESET` used?
- How are cursors, dynamic SQL, exceptions, pragmas, and package initialization handled?
- How are DML triggers written, enabled, disabled, compiled, and verified?
- How should C/C++ external procedures and external functions be registered and called?
- How should external libraries be deployed, validated, and troubleshot?
- How do 8.1 Temporary LOB rules affect PSM variables and collections?

### Retrieval Alias Index

Use this compact index before scanning PSM, package, trigger, type, and external procedure sections. It is intentionally redundant with later headings so lexical retrieval can land on the exact procedure, function, anonymous block, type, pragma, or external library block.

- Aliases and customer wording: stored procedure, stored function, PSM, anonymous block, trigger body, package, package body, user-defined type, associative array, varray, cursor, ref cursor, dynamic SQL, exception, pragma, external procedure, external library, C external function.
- Exact-token anchors: `CREATE PROCEDURE`, `CREATE FUNCTION`, `CREATE PACKAGE`, `CREATE PACKAGE BODY`, `RETURN`, `DETERMINISTIC`, `AUTHID`, `NOCOPY`, `ASSOCIATIVE ARRAY`, `VARRAY`, `TYPESET`, `OPEN FOR`, `END;`, `CREATE LIBRARY`, `LANGUAGE C`, `EXTERNAL NAME`, `PRAGMA AUTONOMOUS_TRANSACTION`, `PRAGMA EXCEPTION_INIT`, `DBMS_OUTPUT`, `DBMS_APPLICATION_INFO`, `DBMS_ALERT`, `DBMS_CONCURRENT_EXEC`, `DBMS_SQL`, `DBMS_STATS`, `UTL_RAW`, `UTL_SMTP`, `UTL_TCP`.
- Focused routing anchors: stored function side-effect questions route to `Exact block: stored function return and side effects` and must keep `RETURN data_type`, `RETURN expression`, `SELECT`, `INSERT`, `UPDATE`, and `DELETE`; external native-code questions route to `Exact block: external procedure and function registration` and must keep `CREATE LIBRARY`, `CREATE PROCEDURE`, `CREATE FUNCTION`, `LANGUAGE C`, `PARAMETERS`, `EXTERNAL`, and `INTERNAL`.
- Answer route: use this file for PSM generation and external procedure deployment; use `04_sql_dml_oracle_compatibility.md` for SQL inside PSM; use `05_data_types_properties.md` for type limits; use `12_c_cli_odbc_precompiler.md` for C interface details outside the external procedure contract.
- Safety route: external procedure answers must ask for target OS, Altibase version, compiler/runtime ABI, library path, parameter types, and deployment privileges before production commands.

### Source Documents

- 7.1: Altibase 7.1 Stored Procedures Manual; External Procedures Manual; SQL Reference; General Reference.
- 7.3: Altibase 7.3 Stored Procedures Manual; External Procedures Manual; SQL Reference; General Reference; Altibase 7.3 Release Notes for VARRAY.
- 8.1: Altibase 8.1 verified source Stored Procedures Manual; External Procedures Manual; SQL Reference; General Reference; Altibase 8.1 Release Notes.

### Response Rules

- Answer in the user's language, but keep SQL object names, function names, error codes, property names, commands, and file paths literal.
- Treat Altibase PSM as PL/SQL-like, not fully Oracle PL/SQL compatible. Confirm syntax, data types, package availability, and side effects.
- If no version is specified, use the 8.1 baseline and call out older-version checks for `IF EXISTS`, `IF NOT EXISTS`, VARRAY, Temporary LOB, and PSM case-sensitivity behavior.
- For broad 7.1 and 7.3 compatibility, avoid `IF EXISTS` and `IF NOT EXISTS` in PSM DDL unless the target version is 8.1 verified source.
- For trigger DDL generation, use this file for PSM body rules and `03_sql_ddl_generation.md` for surrounding schema-object DDL context.
- Do not generate external procedures unless the user accepts native code deployment into `$ALTIBASE_HOME/lib` and the operational risk of the selected external procedure mode.
- Prefer examples that compile in iSQL: end PSM object creation with `END;` and then `/` on the next line.

### Exact PSM Answer Blocks

Use these compact blocks when a customer asks for syntax generation or version-sensitive
stored logic behavior. Preserve the literal tokens shown here in answers.

Exact block: stored procedure parameters and iSQL execution

- Version scope: Altibase 8.1 verified source for `IF NOT EXISTS`; core parameter rules also apply to the selected 7.1 and 7.3 PSM sources unless an installed patch proves otherwise.
- Parameter modes: `IN`, `OUT`, and `IN OUT`; `IN` is the default.
- Default-value rule: `OUT` and `IN OUT` parameters cannot have `DEFAULT` or `:=` default values.
- `NOCOPY`: supported for `ASSOCIATIVE ARRAY` parameter cases and for collection subarray access patterns. Use it deliberately because the effect is pass-by-reference-style behavior, not a generic scalar speed switch.
- Privilege model: `AUTHID DEFINER` is the default; `AUTHID CURRENT_USER` uses the invoking user's privileges and object resolution.
- iSQL execution rule: after a PSM object body, enter `/` on the line after `END;`.

```sql
CREATE OR REPLACE PROCEDURE p_demo(
  p_id IN INTEGER,
  p_out OUT INTEGER,
  p_arr IN NOCOPY arr_types.arr_type
)
AUTHID DEFINER
AS
BEGIN
  p_out := p_id;
END;
/
```

Exact block: stored function return and side effects

- Version scope: Altibase 8.1 verified source.
- Syntax tokens to preserve: `CREATE FUNCTION`, `RETURN data_type`, `RETURN expression`, `DETERMINISTIC`, `SELECT`, `INSERT`, `UPDATE`, `DELETE`.
- A function declaration specifies `RETURN data_type`; the body must return a value with `RETURN expression`.
- A stored procedure errors if its `RETURN` statement specifies a value; a stored function must specify a value.
- Use `DETERMINISTIC` only for a function whose same input always gives the same result, especially when check constraints or function-based indexes depend on it.
- A function called from a `SELECT` statement cannot execute `INSERT`, `UPDATE`, `DELETE`, or transaction-control statements.
- A function called from `INSERT`, `UPDATE`, or `DELETE` cannot execute transaction-control statements.

Exact block: anonymous block and bind variables

- Version scope: 7.3 release-note wording and 8.1 PSM baseline.
- Anonymous block shape: `DECLARE ... BEGIN ... END;`.
- It does not create or store a PSM database object.
- It does not return a value through a `RETURN` clause.
- Unlike a stored procedure, it can use iSQL bind variables for `INPUT`, `OUTPUT`, and `INOUTPUT` use.

Exact block: `VARRAY`, `VARRAY_MEMORY_MAXIMUM`, and `NOCOPY`

- Version scope: Altibase 7.3 release notes add PSM `VARRAY`; do not backport `VARRAY` to a 7.1 baseline without exact patch evidence.
- `VARRAY` is a user-defined array type for storing consecutive values of the same data type.
- `VARRAY_MEMORY_MAXIMUM` is the property tied to the 7.3+ `VARRAY` feature area.
- `NOCOPY` is relevant when accessing lower arrays in `ASSOCIATIVE ARRAY` or `VARRAY` structures.
- For a generated answer, keep the tokens `VARRAY`, `VARRAY_MEMORY_MAXIMUM`, `NOCOPY`, `ASSOCIATIVE ARRAY`, `7.3`, and `7.1` together.

Exact block: `REF CURSOR` return-through-parameter pattern

- Version scope: Altibase 8.1 verified source.
- Use `OPEN FOR` to open the cursor variable and execute the query before returning it through an `OUT` or `IN OUT` procedure parameter.
- Cursor variables can be passed only as `OUT` or `IN OUT` parameters of stored procedures.
- A cursor variable cannot be returned from a stored function with a `RETURN` statement.
- Generation rule: expose a cursor to callers through a procedure parameter, not an Oracle-style function return.

```sql
CREATE TYPESET emp_types AS
  TYPE emp_cur IS REF CURSOR;
END;
/

CREATE OR REPLACE PROCEDURE open_emps(
  p_result OUT emp_types.emp_cur
)
AS
BEGIN
  OPEN p_result FOR SELECT eno, e_lastname FROM employees;
END;
/
```

Exact block: external procedure and function registration

- Version scope: Altibase 8.1 verified source.
- Deployment sequence: build a shared library, place it where the server-side external procedure facility can load it, create the `CREATE LIBRARY` object, then create the external `CREATE PROCEDURE` or `CREATE FUNCTION`.
- External declarations use `LANGUAGE C` and name the user function, library object, and `PARAMETERS` mapping.
- The call spec can choose `EXTERNAL` or `INTERNAL`; if neither is specified, the documented behavior is `EXTERNAL` mode.
- For an external function, `RETURN` in the `PARAMETERS` list identifies the parameter that receives the external function return value.
- `RETURN` must appear after all function argument parameters, at the end of the parameter list.
- If no attribute parameter follows `RETURN`, specifying `RETURN` alone is equivalent to omitting `RETURN`.

Exact block: PSM client-tool durable checklist

- Before generating stored logic, choose the object form deliberately: `CREATE PROCEDURE` for no scalar return, `CREATE FUNCTION` with `RETURN data_type` and `RETURN expression` for a scalar result, or an anonymous `BEGIN ... END;` block for one-time execution.
- In iSQL scripts, end `CREATE PROCEDURE`, `CREATE FUNCTION`, `CREATE TYPESET`, package, and anonymous-block bodies with `END;`, then submit the block with `/` on the next line; successful compilation is reported as `Create success.`.
- Parameter handling: `IN` is the default, `OUT` and `IN OUT` cannot have default values, and `NOCOPY` should be used only for source-supported collection cases such as `ASSOCIATIVE ARRAY` or `VARRAY` subarray access.
- For cursor-return procedures, define a `REF CURSOR` type in a typeset or package, declare the procedure parameter as `OUT` or `IN OUT`, and open it with `OPEN cursor_variable FOR select_statement`.
- External native-code sequence: compile the shared object, place the file under `$ALTIBASE_HOME/lib`, run `CREATE LIBRARY`, then run external `CREATE PROCEDURE` or `CREATE FUNCTION` with `LANGUAGE C`, the user function name, `PARAMETERS`, and `EXTERNAL` or `INTERNAL` mode.
- Verification packet: preserve the exact DDL, library file path, iSQL output, object status, call SQL, external-procedure mode, and any external-procedure agent or server trace before diagnosing load, symbol, type-mapping, or execution errors.

### Version Differences

| Area | 7.1 | 7.3 | 8.1 verified source |
| --- | --- | --- | --- |
| Core PSM | Procedures, functions, anonymous blocks, cursors, exceptions, packages, typesets, dynamic SQL, and external procedures are covered. Anonymous block support is documented from 7.1.0.2.3. | Same core PSM model. | Same core model plus verified 8.1 property and Temporary LOB guidance. |
| Idempotent DDL | Do not assume `IF EXISTS` or `IF NOT EXISTS` for PSM objects. | Do not assume `IF EXISTS` or `IF NOT EXISTS` for PSM objects. | PSM object DDL includes `IF NOT EXISTS` for `CREATE PROCEDURE`, `CREATE FUNCTION`, `CREATE TYPESET`, `CREATE PACKAGE`, and `CREATE PACKAGE BODY`; `IF EXISTS` for related `DROP` statements where documented. External library DDL includes `CREATE LIBRARY IF NOT EXISTS` and `DROP LIBRARY IF EXISTS`. |
| Trigger DDL | DML triggers, `ALTER TRIGGER`, and `DROP TRIGGER` are supported; do not assume trigger `IF EXISTS` or `IF NOT EXISTS`. | Same baseline trigger model as 7.1; do not assume trigger `IF EXISTS` or `IF NOT EXISTS`. | `CREATE TRIGGER IF NOT EXISTS` and `DROP TRIGGER IF EXISTS` are Altibase 8.1 verified source syntax. |
| VARRAY | Not part of the 7.1 baseline. | Release notes add PSM `VARRAY` as a user-defined type and `VARRAY_MEMORY_MAXIMUM`. | Treat VARRAY as supported in the Altibase 8.1 verified source; use the 7.3+ VARRAY rules below. |
| External procedure mode | `call_spec` supports `LANGUAGE [EXTERNAL | INTERNAL] C`; `EXTERNAL` or omission uses external mode, and `INTERNAL` uses internal mode. | Same explicit mode guidance as 7.1. | Same explicit mode guidance as 7.1. |
| Temporary LOB | Not part of the 7.1 baseline. | Not part of the 7.3 baseline. | Temporary LOB is supported. PSM LOB variables and LOB collections can create transaction or session Temporary LOBs. |
| PSM case sensitivity | `PSM_CASE_SENSITIVE_MODE` default is `0`. `0` is case-insensitive and `1` is case-sensitive for `RECORD` and `%ROWTYPE` field names and label names. | `PSM_CASE_SENSITIVE_MODE` default is `1`; use the same `0`/`1` behavior. | `PSM_CASE_SENSITIVE_MODE` default is `1`; use the same `0`/`1` behavior. |
| Open cursor with rollback | `COMMIT` and `ROLLBACK` can execute while a cursor is open. | `COMMIT` and `ROLLBACK` can execute while a cursor is open. | `COMMIT` and `ROLLBACK` can execute while a cursor is open. |

### PSM Generation Flow

```mermaid
flowchart TD
  A[User asks for stored logic] --> B{Version specified?}
  B -->|No| C[Use 8.1 baseline]
  B -->|Yes| D[Use requested version]
  C --> E{Needs persisted object?}
  D --> E
  E -->|No| F[Generate anonymous block]
  E -->|Yes| G{Returns scalar value?}
  G -->|Yes| H[Generate CREATE FUNCTION]
  G -->|No| I[Generate CREATE PROCEDURE]
  H --> J{Shared API or state needed?}
  I --> J
  J -->|Yes| K[Use package specification and body]
  J -->|No| L[Keep standalone object]
  K --> M[Add grants, compile, execute, verify]
  L --> M
  F --> M
```

### External Procedure Flow

```mermaid
flowchart TD
  A[Write C/C++ user functions] --> B[Write entryfunction]
  B --> C[Build shared library]
  C --> D[Move .so to $ALTIBASE_HOME/lib]
  D --> E[CREATE LIBRARY object]
  E --> F[CREATE external PROCEDURE or FUNCTION]
  F --> G{Mode}
  G -->|EXTERNAL or omitted| H[Agent Process loads library]
  G -->|INTERNAL| I[Server process loads library]
  H --> J[Call from SQL, PSM, or client]
  I --> J
```

### Compact PSM Syntax Patterns

These patterns are generation guides converted from source syntax diagrams. They are not a replacement for the full grammar.

#### Procedure

```text
create_procedure ::=
  CREATE [OR REPLACE] PROCEDURE [IF NOT EXISTS] [user_name.]procedure_name
  [(parameter_declaration [, ...])]
  [AUTHID {CURRENT_USER | DEFINER}]
  {AS | IS}
  [declaration_section]
  BEGIN
    statement...
  [EXCEPTION
    exception_handler...]
  END [procedure_name];

parameter_declaration ::=
  parameter_name [IN | OUT | IN OUT] [NOCOPY] data_type
  [{DEFAULT | :=} expression]
```

Generation notes:

- `IN` is the default parameter mode.
- `IN` parameters are constants inside the procedure and cannot be assigned to or used as `SELECT ... INTO` targets.
- `OUT` and `IN OUT` parameters cannot have default values.
- `NOCOPY` is for supported collection cases; use it deliberately because it passes by reference-like behavior.
- `AUTHID DEFINER` executes using the creator's privileges; `AUTHID CURRENT_USER` resolves referenced objects using the invoking user.
- A procedure has no return value and cannot be used as an expression in SQL.

#### Function

```text
create_function ::=
  CREATE [OR REPLACE] FUNCTION [IF NOT EXISTS] [user_name.]function_name
  [(parameter_declaration [, ...])]
  RETURN data_type
  [DETERMINISTIC]
  [AUTHID {CURRENT_USER | DEFINER}]
  {AS | IS}
  [declaration_section]
  BEGIN
    statement...
  [EXCEPTION
    exception_handler...]
  END [function_name];
```

Generation notes:

- A function must return one value using `RETURN expression`.
- Use `DETERMINISTIC` only when identical input always returns identical output. This matters for function-based indexes and check constraints.
- A stored function called from a `SELECT` statement cannot contain `INSERT`, `UPDATE`, or `DELETE`.
- A stored function called from `SELECT`, `INSERT`, `UPDATE`, or `DELETE` cannot contain transaction control statements.
- Do not redefine a function used in constraints or function-based indexes as if that were harmless; dependent DML can fail if invoked functions change or disappear.

#### Object Management

```text
alter_procedure ::= ALTER PROCEDURE [user_name.]procedure_name COMPILE;
alter_function  ::= ALTER FUNCTION  [user_name.]function_name  COMPILE;
drop_procedure  ::= DROP PROCEDURE [IF EXISTS] [user_name.]procedure_name;
drop_function   ::= DROP FUNCTION  [IF EXISTS] [user_name.]function_name;

execute_procedure ::=
  EXEC[UTE] [[user_name.]package_name.]procedure_name
  [(parameter_notation [, ...])];

execute_function ::=
  EXEC[UTE] variable := [[user_name.]package_name.]function_name
  [(parameter_notation [, ...])];

parameter_notation ::=
  expression
  | parameter_name => expression
```

Generation notes:

- Positional parameters can be mixed with named parameters only when all positional parameters come first.
- `ALTER ... COMPILE` explicitly recompiles invalid objects after referenced objects change.
- Dropping a referenced procedure or function can succeed, but later callers fail when they attempt to execute missing code.

Validation SQL:

```sql
SELECT u.user_name,
       p.proc_name,
       p.object_type,
       p.status,
       p.authid,
       p.para_num,
       p.created,
       p.last_ddl_time
FROM SYSTEM_.SYS_PROCEDURES_ p,
     SYSTEM_.SYS_USERS_ u
WHERE p.user_id = u.user_id
  AND u.user_name = '<OWNER_NAME>'
  AND p.proc_name = '<PROC_NAME>';
```

`OBJECT_TYPE` values include `0` procedure, `1` function, and `3` type set. `STATUS` values are `0` valid and `1` invalid. Use `SYS_PROC_PARAS_`, `SYS_PROC_PARSE_`, and `SYS_PROC_RELATED_` when the answer needs parameter, source-text, or dependency detail.

#### Anonymous Block

```text
anonymous_block ::=
  [<<label_name>>]
  [DECLARE declaration_section]
  BEGIN
    statement...
  [EXCEPTION
    exception_handler...]
  END [label_name];
```

Generation notes:

- Anonymous blocks do not create stored database objects.
- Anonymous blocks do not return a `RETURN` value.
- Anonymous blocks can use iSQL bind variables for `INPUT`, `OUTPUT`, and `INOUTPUT`.

#### Block and Variable Declarations

```text
block ::=
  [<<label_name>>]
  [DECLARE declaration_section]
  BEGIN statement... [EXCEPTION exception_handler...] END [label_name];

variable_declaration ::=
  variable_name [CONSTANT] data_type [NOCOPY] [{DEFAULT | :=} expression];

type_reference ::=
  scalar_sql_type
  | BOOLEAN
  | FILE_TYPE
  | table_or_cursor_name%ROWTYPE
  | table_or_column_or_variable%TYPE
  | user_defined_type
```

Generation notes:

- `DECLARE`, `BEGIN`, and `EXCEPTION` do not take semicolons; `END` and normal statements do.
- If a PSM variable and a table column have the same name inside SQL, Altibase resolves the name as the column. Use a block label such as `block_label.variable_name` to remove ambiguity.
- `BOOLEAN` is a PSM-only type with `TRUE`, `FALSE`, or `NULL`. It cannot be stored in a table column, fetched from a table column, returned by a SQL-callable function in a SQL statement, or passed to output procedures such as `PRINT`.

#### PSM Data Type Limits

| Type | SQL statement maximum | PSM maximum |
| --- | --- | --- |
| `CHAR(M)` | `32000` | `65534` |
| `VARCHAR(M)` | `32000` | `65534` |
| `NCHAR(M)` | `16000` for UTF-16, `10666` for UTF-8 | `32766` for UTF-16, `21843` for UTF-8 |
| `NVARCHAR(M)` | `16000` for UTF-16, `10666` for UTF-8 | `32766` for UTF-16, `21843` for UTF-8 |
| `BLOB` | `2GB - 1` | `100MB`, controlled by `LOB_OBJECT_BUFFER_SIZE` |
| `CLOB` | `2GB - 1` | `100MB`, controlled by `LOB_OBJECT_BUFFER_SIZE` |

Default precision properties for PSM character parameters and return values include `PSM_CHAR_DEFAULT_PRECISION`, `PSM_VARCHAR_DEFAULT_PRECISION`, `PSM_NCHAR_UTF8_DEFAULT_PRECISION`, `PSM_NCHAR_UTF16_DEFAULT_PRECISION`, `PSM_NVARCHAR_UTF8_DEFAULT_PRECISION`, and `PSM_NVARCHAR_UTF16_DEFAULT_PRECISION`.

#### SQL Inside PSM

```text
select_into ::=
  SELECT select_list
  INTO {variable_name [, ...] | record_name}
  rest_of_select_statement;

bulk_collect ::=
  SELECT select_list
  BULK COLLECT INTO {array_variable [, ...] | array_record}
  rest_of_select_statement;

returning_into ::=
  {INSERT | UPDATE | DELETE} ...
  RETURNING expr [, ...]
  INTO {variable_name [, ...] | record_name | BULK COLLECT INTO array_target};

assignment ::=
  variable_name := expression;
  | SET variable_name = expression;
```

Generation notes:

- A `SELECT` in PSM must use `INTO`.
- Ordinary `SELECT ... INTO` must return exactly one row. `NO_DATA_FOUND` is raised for zero rows and `TOO_MANY_ROWS` is raised for more than one row.
- `BULK COLLECT` returns all rows into associative array or VARRAY targets and is preferred over row-by-row loops when the result size is appropriate.
- `RETURNING INTO` stores values affected by `INSERT`, `UPDATE`, or `DELETE`.
- PSM has record extensions for `INSERT INTO table VALUES record_variable` and `UPDATE table SET ROW = record_variable` style operations. Column count and compatible order must match the target table.

### Control Flow

```text
if_statement ::=
  IF condition THEN statement...
  [ELSIF condition THEN statement...]...
  [ELSE statement...]
  END IF;

case_statement ::=
  CASE
    WHEN condition THEN statement...
    ...
    [ELSE statement...]
  END CASE;
  | CASE case_variable
      WHEN value THEN statement...
      ...
      [ELSE statement...]
    END CASE;

loop_statement ::=
  LOOP statement... END LOOP [label_name];
  | WHILE condition LOOP statement... END LOOP [label_name];
  | FOR counter IN [REVERSE] lower_bound .. upper_bound [STEP step_size]
      LOOP statement... END LOOP [label_name];

loop_control ::=
  EXIT [label_name] [WHEN condition];
  | CONTINUE [WHEN condition];
  | GOTO label_name;
  | NULL;
```

Generation notes:

- `IF` and `CASE` conditions can use SQL-style conditions, but subqueries in conditions are restricted except `EXISTS (subquery)` and `NOT EXISTS (subquery)`.
- `FOR` loop bounds are evaluated once before loop entry. A non-integer bound is rounded to the nearest integer.
- `STEP` must be at least `1`.
- `EXIT` can target a labeled outer loop when the label is placed immediately before that loop.
- `GOTO` cannot transfer into an inner block, between alternative branches of `IF` or `CASE`, or from an exception handler to another location in the same block.

### Cursors and Result Sets

```text
cursor_declaration ::=
  CURSOR cursor_name [(cursor_parameter [, ...])] IS select_statement;

open_cursor ::= OPEN cursor_name [(argument [, ...])];
fetch_cursor ::= FETCH cursor_name INTO {variable [, ...] | record_name};
fetch_bulk ::= FETCH cursor_name BULK COLLECT INTO array_target [LIMIT integer];
close_cursor ::= CLOSE cursor_name;

cursor_for_loop ::=
  FOR record_name IN cursor_name [(argument [, ...])] LOOP
    statement...
  END LOOP;

ref_cursor_type ::= TYPE type_name IS REF CURSOR;
open_for ::= OPEN cursor_variable FOR {select_statement | dynamic_select_string} [USING bind_value [, ...]];
```

Generation notes:

- Cursor parameters can be used only inside the cursor's `SELECT`.
- Cursor parameters cannot be `OUT` or `IN OUT`; `%ROWTYPE` is not supported for cursor parameters.
- `FETCH` into a `RECORD` target must use a single record variable that matches all selected columns.
- `CLOSE` frees cursor resources. If a cursor declared in a block is not explicitly closed, it is closed when the block exits, but explicit close is preferred.
- Cursor attributes are `%FOUND`, `%NOTFOUND`, `%ISOPEN`, and `%ROWCOUNT`. Use `SQL%FOUND`, `SQL%NOTFOUND`, and `SQL%ROWCOUNT` for implicit cursors from DML or single-row `SELECT INTO`.
- `REF CURSOR` can be passed as `OUT` or `IN OUT` procedure parameters and can be returned to ODBC or JDBC clients. It cannot be returned by a function `RETURN` clause.
- When returning a `REF CURSOR` to a client, the cursor must still be open.

### User-Defined Types

```text
type_definition ::=
  TYPE type_name IS record_type_spec;
  | TYPE type_name IS associative_array_type_spec;
  | TYPE type_name IS ref_cursor_type_spec;
  | TYPE type_name IS varray_type_spec;

record_type_spec ::=
  RECORD (column_name data_type [, column_name data_type ...])

associative_array_type_spec ::=
  TABLE OF data_type [INDEX BY {INTEGER | VARCHAR(size)}]

ref_cursor_type_spec ::=
  REF CURSOR

varray_type_spec ::=
  VARRAY(size) OF data_type
```

#### Type Item: `RECORD`

Purpose: groups heterogeneous fields into one local logical row type.

Usage notes:

- A `RECORD` type defined inside a block is local to that block.
- `%ROWTYPE` variables behave like record variables whose fields match a table or cursor row.
- Assignment between two named `RECORD` types requires the same type name. Identical internal structure alone is not enough.
- Assignment between `RECORD` and `%ROWTYPE` is compatible when field count and data types match.

#### Type Item: `ASSOCIATIVE ARRAY`

Purpose: key-value collection indexed by `INTEGER` or `VARCHAR`.

Access patterns:

```text
array_variable[index]
array_variable(index)
```

Methods:

- `COUNT()` returns the number of elements.
- `DELETE()`, `DELETE(n)`, and `DELETE(m, n)` remove all, one, or a range of elements.
- `EXISTS(n)` returns `TRUE` when the element exists.
- `FIRST()` and `LAST()` return the lowest and highest index or key.
- `NEXT(n)` and `PRIOR(n)` return adjacent indexes or keys.

#### Type Item: `VARRAY`

Version: 7.3 and later guidance; not part of the 7.1 baseline.

Purpose: ordered collection of elements of the same type with an integer index starting at `1`.

Syntax:

```text
TYPE type_name IS VARRAY(size) OF data_type;
variable_name type_name;
variable_name := type_name();
variable_name := type_name(initial_value1, initial_value2, ...);
```

Usage notes:

- `size` is the maximum number of elements. The documented upper limit is `2,147,483,647`, subject to memory limits.
- A VARRAY variable must normally be initialized with its constructor before use.
- Extend it before assigning new positions, for example `ret := variable_name.EXTEND();`.
- In `BULK COLLECT`, VARRAY targets can be populated without manual initialization and extension.
- Middle elements cannot be removed individually. Use `TRIM` from the end or `DELETE()` to remove all elements.
- Memory per VARRAY variable is limited by `VARRAY_MEMORY_MAXIMUM`.
- Values of user-defined `RECORD`, `ASSOCIATIVE ARRAY`, and `VARRAY` types can be passed between stored procedures and functions, but source manuals do not present them as ordinary client-returnable values. Use `REF CURSOR` for result sets returned to ODBC or JDBC clients.
- Assignment compatibility is type-name based for VARRAY values. Two VARRAY types with identical structure are not interchangeable unless they are the same named type.
- Use `NOCOPY` deliberately for supported associative-array or VARRAY subarray access patterns; do not add it to scalar parameters as a generic performance hint.

Methods:

- `COUNT()` returns current element count.
- `DELETE()` removes all elements.
- `LIMIT()` returns the maximum element count declared by the type.
- `EXTEND()`, `EXTEND(n)`, and `EXTEND(m, n)` extend by one, by `n`, or by copying the `n`th element while extending by `m`.
- `TRIM()` and `TRIM(n)` remove elements from the end.
- `EXISTS(n)`, `FIRST()`, `LAST()`, `NEXT(n)`, and `PRIOR(n)` inspect element presence and position.

VARRAY sizing check:

```sql
SELECT name, value1, min, max
FROM V$PROPERTY
WHERE name = 'VARRAY_MEMORY_MAXIMUM';
```

#### Type Item: `TYPESET`

```text
create_typeset ::=
  CREATE [OR REPLACE] TYPESET [IF NOT EXISTS] [user_name.]typeset_name
  {AS | IS}
    type_declaration...
  END;

drop_typeset ::=
  DROP TYPESET [IF EXISTS] [user_name.]typeset_name;
```

Purpose: database object that stores user-defined types for reuse across procedures and functions.

Usage notes:

- Types from a typeset can be used as procedure parameters and function return values.
- A result set can be passed to a client through a `REF CURSOR` type defined in a typeset.
- Dropping a typeset invalidates procedures or functions that depend on it.

### Dynamic SQL

```text
execute_immediate ::=
  EXECUTE IMMEDIATE dynamic_string
  [INTO variable [, ...] | BULK COLLECT INTO array_target]
  [USING bind_value [, ...]];

open_for_dynamic ::=
  OPEN ref_cursor_variable FOR dynamic_select_string
  [USING bind_value [, ...]];
```

Generation notes:

- `EXECUTE IMMEDIATE` can dynamically execute supported DDL, DCL, DML, and a `SELECT` returning one row.
- The dynamic SQL string uses `?` placeholders, bound in order by the `USING` clause.
- Supported dynamic SQL includes `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `MOVE`, `MERGE`, `LOCK TABLE`, `ENQUEUE`, `DEQUEUE`, `CREATE`, `ALTER`, `DROP`, `ALTER SYSTEM`, `ALTER SESSION`, `COMMIT`, and `ROLLBACK`.
- iSQL-only commands such as `DESC`, `SET TIMING`, `SET AUTOCOMMIT`, `CONNECT`, and `DISCONNECT` are not dynamic SQL targets.
- Use `OPEN ... FOR` when the dynamic query returns multiple rows through a `REF CURSOR`.

Example:

```sql
CREATE OR REPLACE PROCEDURE fire_emp(v_emp_id INTEGER) AS
BEGIN
  EXECUTE IMMEDIATE
    'DELETE FROM employees WHERE eno = ?'
    USING v_emp_id;
END;
/
```

### Exceptions and Error Handling

```text
exception_declaration ::= exception_name EXCEPTION;

raise_statement ::=
  RAISE [exception_name];

raise_application_error ::=
  RAISE_APPLICATION_ERROR(errcode INTEGER, errmsg VARCHAR(2047));

exception_handler ::=
  WHEN exception_name [OR exception_name ...] THEN statement...
  | WHEN OTHERS THEN statement...
```

System-defined exception item blocks:

- `CURSOR_ALREADY_OPEN`: raised when opening an already open cursor.
- `DUP_VAL_ON_INDEX`: raised on duplicate value for a unique index.
- `INVALID_CURSOR`: raised when cursor state is invalid for the requested operation.
- `NO_DATA_FOUND`: raised when a single-row `SELECT INTO` returns no row.
- `TOO_MANY_ROWS`: raised when a single-row `SELECT INTO` returns multiple rows.

File-control exception item blocks:

- `INVALID_PATH`
- `INVALID_MODE`
- `INVALID_FILEHANDLE`
- `INVALID_OPERATION`
- `READ_ERROR`
- `WRITE_ERROR`
- `ACCESS_DENIED`
- `DELETE_FAILED`
- `RENAME_FAILED`

Generation notes:

- User-defined exceptions must be declared in the declaration section.
- A user-defined exception with the same name as a system-defined exception takes precedence in its scope.
- `RAISE` without an exception name is allowed only inside an exception handler; it reraises the current exception.
- `RAISE_APPLICATION_ERROR` supports user-defined error codes from `990000` through `991000`.
- `SQLCODE` and `SQLERRM` are used in exception handlers to inspect the current Altibase error number and message. Assign them to variables before using their values in SQL statements.
- If no handler is found through the current block and outer blocks, execution stops with an unhandled exception.

Common error codes:

| Exception | Decimal code | Hex code |
| --- | --- | --- |
| User-defined exception | `201232` | `31210` |
| `CURSOR_ALREADY_OPEN` | `201062` | `31166` |
| `DUP_VAL_ON_INDEX` | `201063` | `31167` |
| `INVALID_CURSOR` | `201064` | `31168` |
| `NO_DATA_FOUND` | `201066` | `3116A` |
| `TOO_MANY_ROWS` | `201070` | `3116E` |
| `VALUE_ERROR` example | `201071` | version-specific display can use the mapped `ERR-` form |

Example:

```sql
CREATE OR REPLACE PROCEDURE raise_if_empty AS
  v_count INTEGER;
BEGIN
  SELECT COUNT(*) INTO v_count FROM employees;
  IF v_count = 0 THEN
    RAISE_APPLICATION_ERROR(990000, 'employees is empty');
  END IF;
EXCEPTION
  WHEN OTHERS THEN
    PRINTLN('SQLCODE: ' || SQLCODE);
    PRINTLN('SQLERRM: ' || SQLERRM);
    RAISE;
END;
/
```

### Pragmas

```text
pragma_declaration ::=
  PRAGMA AUTONOMOUS_TRANSACTION;
  | PRAGMA EXCEPTION_INIT(exception_name, error_code);
```

#### Pragma Item: `AUTONOMOUS_TRANSACTION`

Purpose: makes the top-level PSM object or trigger body execute with an independent transaction.

Allowed locations:

- Top-level stored procedures.
- Top-level stored functions.
- Top-level package subprograms.
- Trigger `psm_body`.

Operational notes:

- The autonomous transaction does not share locks, savepoints, commit dependency, or rollback dependency with the caller.
- If the caller rolls back, committed work from the autonomous transaction is not rolled back.
- A deadlock can occur if the autonomous transaction accesses objects already referenced by the main transaction.
- Explicitly `COMMIT` or `ROLLBACK` inside autonomous routines.

#### Pragma Item: `EXCEPTION_INIT`

Purpose: maps a user-declared exception variable to an Altibase error code.

Allowed locations:

- Declaration section of a procedure.
- Declaration section of a function.
- Declaration section of a package.
- Declaration section of a package subprogram.

Example:

```sql
CREATE OR REPLACE PROCEDURE catch_many_rows AS
  e_many_rows EXCEPTION;
  PRAGMA EXCEPTION_INIT(e_many_rows, 201070);
BEGIN
  NULL;
EXCEPTION
  WHEN e_many_rows THEN
    PRINTLN('Too many rows');
END;
/
```

### Trigger PSM Bodies

Trigger DDL is schema-object SQL, but the `psm_body` uses Altibase PSM block rules. Use this section with `03_sql_ddl_generation.md` when generating complete trigger statements.

```text
create_trigger ::=
  CREATE [OR REPLACE] TRIGGER [IF NOT EXISTS] [user_name.]trigger_name
  {simple_dml_trigger | instead_of_dml_trigger};

simple_dml_trigger ::=
  {BEFORE | AFTER} trigger_event ON [user_name.]table_name
  [referencing_clause]
  trigger_action;

trigger_action ::=
  FOR EACH ROW [{ENABLE | DISABLE}] [WHEN (search_condition)] psm_body
  | [FOR EACH STATEMENT] [{ENABLE | DISABLE}] psm_body;

instead_of_dml_trigger ::=
  INSTEAD OF {INSERT | DELETE | UPDATE} ON [user_name.]view_name
  [referencing_clause]
  FOR EACH ROW
  [{ENABLE | DISABLE}]
  psm_body;

trigger_event ::=
  INSERT | DELETE | UPDATE [OF column_name [, ...]]
  [OR trigger_event ...];

referencing_clause ::=
  REFERENCING {OLD [ROW] [AS] alias_name | NEW [ROW] [AS] alias_name}
              [, {OLD [ROW] [AS] alias_name | NEW [ROW] [AS] alias_name} ...];

alter_trigger ::=
  ALTER TRIGGER [user_name.]trigger_name {ENABLE | DISABLE | COMPILE};

drop_trigger ::=
  DROP TRIGGER [IF EXISTS] [user_name.]trigger_name;
```

Version and DDL notes:

- `IF NOT EXISTS` and `IF EXISTS` in trigger DDL are Altibase 8.1 verified source syntax. Omit them for 7.1 and 7.3 unless exact target-version documentation proves support.
- Ordinary table triggers can be `BEFORE` or `AFTER`. `INSTEAD OF` triggers are for views.
- `FOR EACH STATEMENT` is the default trigger granularity when the source statement omits the row/statement choice.
- `REFERENCING` and `WHEN` require `FOR EACH ROW`.
- `ENABLE` is the default trigger state; `DISABLE` prevents firing until `ALTER TRIGGER ... ENABLE`.

Trigger body restrictions:

- The trigger `psm_body` follows normal PSM block syntax, including local declarations, control flow, cursors, and exception handlers where allowed.
- Do not use `COMMIT`, `ROLLBACK`, session-control statements such as `CONNECT`, schema DDL such as `CREATE TABLE`, stored procedure calls, or recursive trigger-event operations inside a trigger body.
- Replication receiver-applied table changes do not fire triggers. Do not use triggers as a receiver-side replication business-rule mechanism.
- Multiple triggers on one table have no guaranteed firing order. If order matters, consolidate the logic into one trigger.
- If a trigger fails, the DML statement that fired it also fails.
- When the trigger source table is dropped, its triggers are dropped. If a table referenced inside the trigger body changes or disappears, the trigger can remain but the firing DML can fail.
- The source permits creating `BEFORE INSERT ... FOR EACH ROW` or `BEFORE UPDATE ... FOR EACH ROW` triggers on tables with LOB columns, but the DML that fires those triggers can error. Avoid that design unless the customer has target-version proof and a rollback plan.
- `OLD` row aliases are `NULL` for `INSERT` events. `NEW` row aliases are `NULL` for `DELETE` events; changing `NEW` values in a delete trigger does not affect the delete. In `BEFORE` row triggers, `NEW` values can be changed by the trigger body.

Trigger validation SQL:

```sql
SELECT tr.user_name,
       t.table_name,
       tr.trigger_name,
       tr.is_enable,
       tr.event_time,
       tr.event_type,
       tr.granularity,
       tr.update_column_cnt,
       tr.created,
       tr.last_ddl_time
FROM SYSTEM_.SYS_TRIGGERS_ tr,
     SYSTEM_.SYS_TABLES_ t
WHERE tr.table_id = t.table_id
  AND tr.user_name = '<OWNER_NAME>'
  AND t.table_name = '<TABLE_NAME>'
ORDER BY tr.trigger_name;
```

`IS_ENABLE` values are `0` disabled and `1` enabled. `EVENT_TIME` values include `1` before, `2` after, and `3` instead of. `EVENT_TYPE` values include `1` insert, `2` delete, and `4` update. `GRANULARITY` values include `1` for each row and `2` for each statement. Use `SYS_TRIGGER_STRINGS_`, `SYS_TRIGGER_DML_TABLES_`, and `SYS_TRIGGER_UPDATE_COLUMNS_` when the answer needs source fragments, referenced DML tables, or `UPDATE OF` columns.

Example:

```sql
CREATE OR REPLACE TRIGGER default_score
BEFORE INSERT ON scores
REFERENCING NEW ROW new_row
FOR EACH ROW
WHEN (new_row.score IS NULL)
BEGIN
  new_row.score := 0;
END;
/
```

### Packages

```text
create_package ::=
  CREATE [OR REPLACE] PACKAGE [IF NOT EXISTS] [user_name.]package_name
  [AUTHID {CURRENT_USER | DEFINER}]
  {AS | IS}
    declare_section
  END [package_name];

create_package_body ::=
  CREATE [OR REPLACE] PACKAGE BODY [IF NOT EXISTS] [user_name.]package_name
  {AS | IS}
    declare_section
    [BEGIN initialize_statement... [EXCEPTION exception_handler...]]
  END [package_name];

alter_package ::=
  ALTER PACKAGE [user_name.]package_name COMPILE [SPECIFICATION | BODY | PACKAGE];

drop_package ::=
  DROP PACKAGE [BODY] [IF EXISTS] [user_name.]package_name;
```

Generation notes:

- A package has a specification and, when needed, a body.
- For 7.1 and 7.3, do not generate package `IF EXISTS`; use `DROP PACKAGE [BODY] [user_name.]package_name`. For 8.1, when dropping a package body idempotently, place `BODY` before `IF EXISTS`, for example `DROP PACKAGE BODY IF EXISTS pkg1`.
- The specification is the public API: types, variables, constants, cursors, exceptions, procedures, and functions declared there can be referenced from outside.
- The body defines package cursors and subprograms and can include private declarations.
- Package body initialization runs once per session on first package use. Package state is loaded per session and remains until the session ends.
- Package subprograms can be overloaded by parameter signature.
- The package body cannot be created before the package specification.
- Every subprogram declared in the package specification must be defined in the package body.
- A cursor defined inside a package remains open while subprograms execute and is implicitly closed when subprogram execution completes.
- When overloaded calls could match more than one subprogram, cast values explicitly with functions such as `CAST` or `TO_DATE` so Altibase chooses the intended parameter signature.

Example:

```sql
CREATE OR REPLACE PACKAGE emp_api AS
  PROCEDURE set_salary(p_eno IN INTEGER, p_salary IN NUMBER);
  FUNCTION get_salary(p_eno IN INTEGER) RETURN NUMBER;
END emp_api;
/

CREATE OR REPLACE PACKAGE BODY emp_api AS
  PROCEDURE set_salary(p_eno IN INTEGER, p_salary IN NUMBER) AS
  BEGIN
    UPDATE employees SET salary = p_salary WHERE eno = p_eno;
  END;

  FUNCTION get_salary(p_eno IN INTEGER) RETURN NUMBER AS
    v_salary NUMBER;
  BEGIN
    SELECT salary INTO v_salary FROM employees WHERE eno = p_eno;
    RETURN v_salary;
  END;
END emp_api;
/
```

Package validation SQL:

```sql
SELECT u.user_name,
       p.package_name,
       p.package_type,
       p.status,
       p.authid,
       p.created,
       p.last_ddl_time
FROM SYSTEM_.SYS_PACKAGES_ p,
     SYSTEM_.SYS_USERS_ u
WHERE p.user_id = u.user_id
  AND u.user_name = '<OWNER_NAME>'
  AND p.package_name = '<PACKAGE_NAME>'
ORDER BY p.package_type;
```

`PACKAGE_TYPE` values are `6` package specification and `7` package body. `AUTHID` values are `0` definer rights and `1` current-user rights. `STATUS` values are `0` valid and `1` invalid.

Package parameter and source checks:

```sql
SELECT pp.object_name,
       pp.sub_id,
       pp.sub_tpye,
       pp.para_name,
       pp.para_order,
       pp.inout_type,
       pp.data_type,
       pp.size,
       pp.precision,
       pp.scale,
       pp.default_val
FROM SYSTEM_.SYS_PACKAGE_PARAS_ pp,
     SYSTEM_.SYS_PACKAGES_ pkg,
     SYSTEM_.SYS_USERS_ u
WHERE pp.user_id = pkg.user_id
  AND pp.package_oid = pkg.package_oid
  AND pkg.user_id = u.user_id
  AND u.user_name = '<OWNER_NAME>'
  AND pkg.package_name = '<PACKAGE_NAME>'
ORDER BY pp.object_name, pp.sub_id, pp.para_order;

SELECT ps.seq_no,
       ps.parse
FROM SYSTEM_.SYS_PACKAGE_PARSE_ ps,
     SYSTEM_.SYS_PACKAGES_ pkg,
     SYSTEM_.SYS_USERS_ u
WHERE ps.user_id = pkg.user_id
  AND ps.package_oid = pkg.package_oid
  AND pkg.user_id = u.user_id
  AND u.user_name = '<OWNER_NAME>'
  AND pkg.package_name = '<PACKAGE_NAME>'
ORDER BY ps.package_type, ps.seq_no;
```

The catalog column is spelled `SUB_TPYE` in the selected General Reference. Use that literal name when querying `SYSTEM_.SYS_PACKAGE_PARAS_`. Concatenate `PARSE` values in `SEQ_NO` order when reconstructing package source text.

### Built-In PSM Facilities

#### Output

- `PRINT(value)` outputs text without appending a newline.
- `PRINTLN(value)` outputs text and appends a newline.
- Both are owned by `SYSTEM_`; public synonyms allow calls such as `PRINTLN('ok')`.

#### File Control

File control uses `FILE_TYPE` and directory objects. The physical directory must exist in the operating system and have suitable permissions; `CREATE DIRECTORY` records a database object and does not create the physical directory.

Procedure and function item blocks:

- `FOPEN(location, filename, open_mode)`: opens a file and returns `FILE_TYPE`; `open_mode` is `r`, `w`, or `a`.
- `FCLOSE(file)`: closes one file handle.
- `FCLOSE_ALL`: closes all file handles opened in the current session.
- `FCOPY(location, filename, dest_dir, dest_file, start_line, end_line)`: copies file lines.
- `FFLUSH(file)`: flushes buffered output.
- `FREMOVE(location, filename)`: deletes a file.
- `FRENAME(location, filename, dest_dir, dest_file, overwrite)`: renames or moves a file.
- `GET_LINE(file, buffer, len)`: reads one line.
- `IS_OPEN(file)`: returns `BOOLEAN`.
- `NEW_LINE(file, lines)`: writes newline sequences.
- `PUT(file, buffer)`: writes a string.
- `PUT_LINE(file, buffer, autoflush)`: writes a line and newline sequence.

Important file-control limits:

- Directory object names passed to file procedures should be uppercase.
- One text line cannot exceed `32767` bytes.
- `FILE_TYPE` values cannot be read or modified directly by users.

#### System-Defined Packages

Common package item blocks:

- `STANDARD`: defines basic PSM types usable without extra declarations.
- `DBMS_STANDARD`: provides default subprograms.
- `DBMS_OUTPUT`: prints buffered character strings to the client.
- `DBMS_SQL`: dynamic SQL cursor API, including `OPEN_CURSOR`, `PARSE`, `BIND_VARIABLE`, `EXECUTE_CURSOR`, `DEFINE_COLUMN`, `FETCH_ROWS`, `COLUMN_VALUE`, `CLOSE_CURSOR`, and `LAST_ERROR_POSITION`.
- `DBMS_APPLICATION_INFO`: sets or reads client application information in `V$SESSION`.
- `DBMS_ALERT`: notifies users of database events.
- `DBMS_CONCURRENT_EXEC`: executes procedures concurrently.
- `DBMS_LOCK`: user lock and unlock interface.
- `DBMS_METADATA`: extracts object DDL or grant DDL from the dictionary.
- `DBMS_RANDOM`: generates random values.
- `DBMS_RECYCLEBIN`: purges objects managed in the recycle bin.
- `DBMS_SQL_PLAN_CACHE`: keeps or removes execution plans in the SQL plan cache.
- `DBMS_STATS`: reads and changes optimizer statistics.
- `DBMS_UTILITY`: utility subprograms.
- `SYS_SPATIAL`: GEOMETRY-related subprograms.
- `UTL_FILE`: reads and writes operating-system text files.
- `UTL_RAW`: converts or manipulates RAW/VARBYTE data.
- `UTL_SMTP`: sends email through SMTP.
- `UTL_TCP`: controls TCP access in PSM.

Do not assume Oracle package parity. Match requested Oracle packages to the Altibase package list and verify procedure signatures.

#### System Package Routine Reference

Use this reference when a customer asks for an Altibase system-defined package routine, a PL/SQL package equivalent, or an exact subprogram name. Version scope is selected 7.1, 7.3, and Altibase 8.1 verified source Stored Procedures manuals unless a customer provides an installed package definition that proves a patch-specific difference.

Routine block: `DBMS_APPLICATION_INFO`

- Purpose: sets or reads application information stored in session metadata such as `V$SESSION` `MODULE`, `ACTION`, and `CLIENT_INFO`.
- Routines and signatures:
  - `DBMS_APPLICATION_INFO.READ_CLIENT_INFO(client_info OUT VARCHAR(128));`
  - `DBMS_APPLICATION_INFO.READ_MODULE(module_name OUT VARCHAR(128), action_name OUT VARCHAR(128));`
  - `DBMS_APPLICATION_INFO.SET_ACTION(action_name VARCHAR(128));`
  - `DBMS_APPLICATION_INFO.SET_CLIENT_INFO(client_info VARCHAR(128));`
  - `DBMS_APPLICATION_INFO.SET_MODULE(module_name VARCHAR(128), action_name VARCHAR(128));`
- Example:

```sql
EXEC DBMS_APPLICATION_INFO.SET_MODULE('altibase_module', 'running');
EXEC DBMS_APPLICATION_INFO.SET_ACTION('stop');
EXEC DBMS_APPLICATION_INFO.SET_CLIENT_INFO('test_application');
```

Routine block: `DBMS_ALERT`

- Purpose: registers named database alerts, sends alert messages, waits for alerts, and removes alert registrations.
- Selected-source routine set: `REGISTER`, `REMOVE_EVENT`, `REMOVEALL`, `SET_DEFAULTS`, `SIGNAL`, `WAITANY`, and `WAITONE`. The selected 7.1, 7.3, and 8.1 source manuals do not list `POLLANY` or `POLLONE`; ask for the exact installed package definition before promising those names.
- Routines and signatures:
  - `DBMS_ALERT.REGISTER(name);`
  - `DBMS_ALERT.REMOVE_EVENT(name);`
  - `DBMS_ALERT.REMOVEALL();`
  - `DBMS_ALERT.SET_DEFAULTS(poll_interval);`
  - `DBMS_ALERT.SIGNAL(name, message);`
  - `DBMS_ALERT.WAITANY(name, message, status, timeout);`
  - `DBMS_ALERT.WAITONE(name, message, status, timeout);`
- Parameter notes: alert `name` is `VARCHAR2(30)`, `message` is `VARCHAR2(1800)`, `status` is `INTEGER` where documented success is `0` and failure is `1`, and `timeout`/`poll_interval` are seconds.
- Example:

```sql
EXEC DBMS_ALERT.REGISTER('S1');
EXEC DBMS_ALERT.SIGNAL('S1', 'MESSAGE 001');
EXEC DBMS_ALERT.WAITONE(:NAME, :MESSAGE, :STATUS, 5);
```

Routine block: `DBMS_CONCURRENT_EXEC`

- Purpose: requests concurrent execution of procedures that do not return result values.
- Related properties: `CONCURRENT_EXEC_DEGREE_MAX`, `CONCURRENT_EXEC_DEGREE_DEFAULT`, and `CONCURRENT_EXEC_WAIT_INTERVAL`.
- Restrictions: it cannot execute functions, cannot execute procedures whose parameter mode is `OUT`, cannot be called recursively, cannot be used in parallel query, and `PRINT`/`PRINTLN` output from procedures run through the package is written to `$ALTIBASE_HOME/trc/altibase_qp.log`.
- Routines and signatures:
  - `DBMS_CONCURRENT_EXEC.INITIALIZE(in_degree INTEGER DEFAULT NULL)` returns the configured degree or `0` if resources cannot be allocated.
  - `DBMS_CONCURRENT_EXEC.REQUEST(text VARCHAR(8192))` returns a Request ID, or `-1` when the request itself fails.
  - `DBMS_CONCURRENT_EXEC.WAIT_ALL()` waits for all requested procedures and returns `1` or `-1`.
  - `DBMS_CONCURRENT_EXEC.WAIT_REQ(req_id INTEGER)` waits for one Request ID and returns `1` or `-1`.
  - `DBMS_CONCURRENT_EXEC.GET_ERROR_COUNT()` returns the count of errors after `WAIT_ALL`.
  - `DBMS_CONCURRENT_EXEC.GET_ERROR(req_id IN INTEGER, text OUT VARCHAR(8192), err_code OUT INTEGER, err_msg OUT VARCHAR(8192))` returns the Request ID or `-1`.
  - `DBMS_CONCURRENT_EXEC.PRINT_ERROR(req_id IN INTEGER)` prints the requested error detail.
  - `DBMS_CONCURRENT_EXEC.GET_LAST_REQ_ID()` returns the last successful Request ID.
  - `DBMS_CONCURRENT_EXEC.GET_REQ_TEXT(req_id IN INTEGER)` returns the requested procedure text or `NULL`.
  - `DBMS_CONCURRENT_EXEC.FINALIZE()` releases package resources and returns `1` on success.
- Example call order: `INITIALIZE`, one or more `REQUEST` calls, `WAIT_ALL` or `WAIT_REQ`, `GET_ERROR_COUNT`/`GET_ERROR` or `PRINT_ERROR`, then `FINALIZE`.

```sql
VARIABLE OUT_DEGREE INTEGER;
VARIABLE REQ_ID1 INTEGER;
VARIABLE RC INTEGER;
EXEC :OUT_DEGREE := DBMS_CONCURRENT_EXEC.INITIALIZE(4);
EXEC :REQ_ID1 := DBMS_CONCURRENT_EXEC.REQUEST('PROC1');
EXEC :RC := DBMS_CONCURRENT_EXEC.WAIT_REQ(:REQ_ID1);
EXEC :RC := DBMS_CONCURRENT_EXEC.FINALIZE();
```

Routine block: `DBMS_SQL`

- Purpose: dynamic SQL cursor API for open, parse, bind, execute, fetch, extract, and close operations.
- Related property: `PSM_CURSOR_OPEN_LIMIT`; the selected source states the default open-cursor limit as `32`.
- Dynamic SQL call order: `OPEN_CURSOR`, `PARSE`, optional `BIND_VARIABLE`, `EXECUTE_CURSOR`, for `SELECT` use `DEFINE_COLUMN`, loop `FETCH_ROWS`, use `COLUMN_VALUE`, then `CLOSE_CURSOR`. Use `LAST_ERROR_POSITION` immediately after a `PARSE` error.
- Routines and signatures:
  - `INTEGER variable := DBMS_SQL.OPEN_CURSOR;`
  - `BOOLEAN variable := DBMS_SQL.IS_OPEN(c);`
  - `DBMS_SQL.PARSE(c, sql, language_flag);`
  - `DBMS_SQL.BIND_VARIABLE(c, name, value);`
  - `BIGINT variable := DBMS_SQL.EXECUTE_CURSOR(c);`
  - `DBMS_SQL.DEFINE_COLUMN(c, position, column_value);`
  - `INTEGER variable := DBMS_SQL.FETCH_ROWS(c);`
  - `DBMS_SQL.COLUMN_VALUE(c, position, column_value);`
  - `DBMS_SQL.CLOSE_CURSOR(c);`
  - `DBMS_SQL.LAST_ERROR_POSITION;`
- Supported bind/column value families in the selected source include `VARCHAR2(32000)`, `CHAR(32000)`, `INTEGER`, `BIGINT`, `SMALLINT`, `DOUBLE`, `REAL`, `NUMERIC(38)`, and `DATE`; column positions start at `1`.
- Example:

```sql
c := DBMS_SQL.OPEN_CURSOR;
DBMS_SQL.PARSE(c, 'select i1 from t1 where i1 = :b1', DBMS_SQL.NATIVE);
DBMS_SQL.BIND_VARIABLE(c, ':b1', b1);
rc := DBMS_SQL.EXECUTE_CURSOR(c);
DBMS_SQL.DEFINE_COLUMN(c, 1, c1);
LOOP
  EXIT WHEN DBMS_SQL.FETCH_ROWS(c) = 0;
  DBMS_SQL.COLUMN_VALUE(c, 1, c1);
END LOOP;
DBMS_SQL.CLOSE_CURSOR(c);
```

Routine block: `DBMS_STATS`

- Purpose: collects, deletes, reads, sets, locks, and unlocks optimizer statistics for database, system, table, index, column, primary-key, unique-key, and partition cases.
- Routine inventory: `COPY_TABLE_STATS`, `DELETE_COLUMN_STATS`, `DELETE_DATABASE_STATS`, `DELETE_INDEX_STATS`, `DELETE_TABLE_STATS`, `DELETE_SYSTEM_STATS`, `GATHER_DATABASE_STATS`, `GATHER_INDEX_STATS`, `GATHER_SYSTEM_STATS`, `GATHER_TABLE_STATS`, `GET_COLUMN_STATS`, `GET_INDEX_STATS`, `GET_SYSTEM_STATS`, `GET_TABLE_STATS`, `LOCK_TABLE_STATS`, `SET_COLUMN_STATS`, `SET_INDEX_STATS`, `SET_PRIMARY_KEY_STATS`, `SET_SYSTEM_STATS`, `SET_TABLE_STATS`, `SET_UNIQUE_KEY_STATS`, and `UNLOCK_TABLE_STATS`.
- Exact signatures expanded in the selected source include:
  - `DBMS_STATS.SET_PRIMARY_KEY_STATS(ownname VARCHAR(128), tabname VARCHAR(128), keycount BIGINT DEFAULT NULL, numpage BIGINT DEFAULT NULL, numdist BIGINT DEFAULT NULL, clusteringfactor BIGINT DEFAULT NULL, indexheight BIGINT DEFAULT NULL, avgslotcnt BIGINT DEFAULT NULL, no_invalidate BOOLEAN DEFAULT FALSE);`
  - `DBMS_STATS.SET_UNIQUE_KEY_STATS(ownname VARCHAR(128), tabname VARCHAR(128), colnamelist VARCHAR(32000), keycount BIGINT DEFAULT NULL, numpage BIGINT DEFAULT NULL, numdist BIGINT DEFAULT NULL, clusteringfactor BIGINT DEFAULT NULL, indexheight BIGINT DEFAULT NULL, avgslotcnt BIGINT DEFAULT NULL, no_invalidate BOOLEAN DEFAULT FALSE);`
  - `DBMS_STATS.LOCK_TABLE_STATS(ownname VARCHAR(128), tabname VARCHAR(128));`
  - `DBMS_STATS.UNLOCK_TABLE_STATS(ownname VARCHAR(128), tabname VARCHAR(128));`
- `no_invalidate` default is `FALSE`; use `TRUE` when the intent is not to rebuild related execution plans after stats changes.
- Example:

```sql
EXEC DBMS_STATS.LOCK_TABLE_STATS('SYS', 'T1');
EXEC DBMS_STATS.UNLOCK_TABLE_STATS('SYS', 'T1');
```

Routine block: raw, SMTP, TCP, lock, metadata, output, random, recycle bin, plan cache, and file packages

- `UTL_RAW`: conversion/manipulation routines include `CAST_FROM_BINARY_INTEGER`, `CAST_FROM_NUMBER`, `CAST_TO_BINARY_INTEGER`, `CAST_TO_NUMBER`, `CAST_TO_RAW`, `CAST_TO_VARCHAR2`, `CONCAT`, `LENGTH`, and `SUBSTR`. Key signatures include `UTL_RAW.CAST_TO_RAW(c IN VARCHAR(32767))`, `UTL_RAW.CAST_TO_VARCHAR2(c IN RAW(32767))`, and `UTL_RAW.CONCAT(r1...r12 IN RAW(32767))`.
- `UTL_SMTP`: SMTP call order is `OPEN_CONNECTION`, `HELO`, `MAIL`, `RCPT`, `OPEN_DATA`, `WRITE_DATA` or `WRITE_RAW_DATA`, `CLOSE_DATA`, then `QUIT`. The selected source lists `CONNECT_TYPE` handles, `VARCHAR(64)` host/domain fields, `VARCHAR(256)` sender/recipient fields, and `VARCHAR(65534)` or `RAW(65534)` data payloads.
- `UTL_TCP`: TCP routines include `CLOSE_ALL_CONNECTIONS`, `CLOSE_CONNECTION(c IN CONNECT_TYPE)`, `IS_CONNECT(c IN CONNECT_TYPE)`, `OPEN_CONNECTION(...)`, and `WRITE_RAW(...)`. Use `IS_CONNECT` before assuming a handle is still valid.
- `DBMS_LOCK`: user-lock routines are `REQUEST`, `RELEASE`, `SLEEP`, and `SLEEP2`; lock ID range is `0` through `1073741823`, and `SLEEP2` accepts microseconds up to `999999`.
- `DBMS_METADATA`: DDL extraction routines are `GET_DDL`, `GET_DEPENDENT_DDL`, `GET_GRANTED_DDL`, `SET_TRANSFORM_PARAM`, and `SHOW_TRANSFORM_PARAMS`; common transform parameters include `SQLTERMINATOR`, `SEGMENT_ATTRIBUTES`, `STORAGE`, `TABLESPACE`, `CONSTRAINTS`, and `REF_CONSTRAINTS`.
- `DBMS_OUTPUT`: output routines are `NEW_LINE`, `PUT(str IN VARCHAR(65534))`, and `PUT_LINE(str IN VARCHAR(65533))`.
- `DBMS_RANDOM`: random routines include `INITIALIZE`, `SEED`, `STRING`, `VALUE`, and `RANDOM`.
- `DBMS_RECYCLEBIN`: purge routines include `PURGE_USER_RECYCLEBIN`, `PURGE_ALL_RECYCLEBIN`, `PURGE_TABLESPACE`, and `PURGE_ORIGINAL_NAME`.
- `DBMS_SQL_PLAN_CACHE`: plan cache routines are `KEEP_PLAN(sql_text_id)` and `UNKEEP_PLAN(sql_text_id)` where `sql_text_id` is `VARCHAR(64)`.
- `DBMS_STANDARD`: trigger-context routines include `DELETING`, `INSERTING`, and `UPDATING`, including `UPDATING(COLNAME IN VARCHAR(128))`.
- `DBMS_UTILITY`: diagnostic routines include `FORMAT_CALL_STACK` and `FORMAT_ERROR_BACKTRACE`.
- `STANDARD`: defines PSM base types usable without extra package qualification.
- `SYS_SPATIAL`: provides `GEOMETRY`-related subprograms; use `19_spatial_nifi_tableau_misc.md` for Spatial SQL and API details.
- `UTL_COPYSWAP`: online-DDL copy-and-swap routines include `CHECK_PRECONDITION`, `COPY_TABLE_SCHEMA`, `REPLICATE_TABLE`, `SWAP_TABLE`, `SWAP_TABLE_PARTITION`, and `FINISH`; ask for replication name, source/target table names, foreign-key/encryption state, and rollback plan before using it in production.
- `UTL_FILE`: file routines are covered in the `File Control` block above; preserve `FILE_TYPE`, `FOPEN`, `FCLOSE`, `FCLOSE_ALL`, `FCOPY`, `FFLUSH`, `FREMOVE`, `FRENAME`, `GET_LINE`, `IS_OPEN`, `NEW_LINE`, `PUT`, and `PUT_LINE`.

### 8.1 Temporary LOB in PSM

Temporary LOB is an 8.1 feature for transient `CLOB` and `BLOB` values created in memory at execution time.

Temporary LOB categories:

- Transaction Temporary LOB: exists for a transaction and is removed when the transaction ends.
- Session Temporary LOB: exists for a session and is removed when the session ends or when `ALTER SESSION SET FREE TEMPORARY LOB` is executed.

PSM cases:

- `TO_CLOB`, `TO_BLOB`, `SUBSTR` with a `CLOB` argument, and `CONCAT` with a `CLOB` argument can create transaction Temporary LOBs.
- LOB-type variables in PSM execution can create transaction Temporary LOBs unless they fall into a session Temporary LOB case.
- LOB values used as `ASSOCIATIVE ARRAY`, `VARRAY`, or package variables are session Temporary LOB cases.

Required checks:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name IN (
  'TEMPORARY_LOB_ENABLE',
  'MEMORY_TEMPLOB_MAX_ALLOC_SIZE',
  'MEMORY_TEMPLOB_PIECE_SIZE'
);

SELECT type, id, alloced_size, open_count
FROM V$TEMPORARY_LOBS;
```

Cleanup SQL:

```sql
ALTER SESSION SET FREE TEMPORARY LOB;
```

Operational notes:

- `TEMPORARY_LOB_ENABLE=1` enables Temporary LOB.
- `MEMORY_TEMPLOB_MAX_ALLOC_SIZE` limits total Temporary LOB memory allocation; requests beyond the limit fail and the transaction is treated as an error.
- Temporary LOB memory is separate from `MEM_MAX_DB_SIZE`; size both deliberately.
- `MEMORY_TEMPLOB_PIECE_SIZE` controls the memory piece size used for splitting and storing Temporary LOB data.

### External Procedures and Functions

External procedures expose C/C++ functions through Altibase procedure or function objects.

Use external mode unless there is a specific, tested reason to use internal mode:

- `EXTERNAL` mode starts an Agent Process. The Agent Process loads the dynamic library and calls the user function. Native-code failure is isolated from the Altibase server process.
- `INTERNAL` mode loads and calls the dynamic library directly in the Altibase server process. Defective native code can crash the server or leak memory in the server process.

#### External Library

```text
create_library ::=
  CREATE [OR REPLACE] LIBRARY [IF NOT EXISTS] [user_name.]library_name
  {AS | IS} 'file_name';

alter_library ::=
  ALTER LIBRARY [user_name.]library_name COMPILE;

drop_library ::=
  DROP LIBRARY [IF EXISTS] [user_name.]library_name;
```

Generation notes:

- The shared library file must be located in `$ALTIBASE_HOME/lib`.
- `CREATE LIBRARY` can succeed even if the file does not exist. File existence is checked when the external procedure executes; the object can become `INVALID`.
- `DROP LIBRARY` drops only the database library object. It does not delete the operating-system file.
- `ALTER LIBRARY ... COMPILE` is reserved for future language support and has no server-side effect for C/C++.
- `IF NOT EXISTS` and `IF EXISTS` for external library DDL are Altibase 8.1 verified source syntax. Omit them for 7.1 and 7.3 unless the customer provides exact target-version source proof.
- A library object can be dropped even when an external procedure contained in that library is running; the operating-system library file remains in place.

#### External Procedure and Function

```text
external_procedure ::=
  CREATE [OR REPLACE] PROCEDURE [user_name.]procedure_name
  [(argument_declaration [, ...])]
  AS call_spec;

external_function ::=
  CREATE [OR REPLACE] FUNCTION [user_name.]function_name
  [(argument_declaration [, ...])]
  RETURN return_type
  AS call_spec;

argument_declaration ::=
  argument_name [IN | OUT | IN OUT] data_type

call_spec ::=
  LANGUAGE [EXTERNAL | INTERNAL] C
  {NAME "func_name" | LIBRARY library_name}...
  [PARAMETERS(parameter_declaration [, ...])]

parameter_declaration ::=
  parameter_name [INDICATOR | LENGTH | MAXLEN]
  | RETURN [INDICATOR | LENGTH | MAXLEN]
```

Generation notes:

- In 7.1, 7.3, and 8.1 syntax, `call_spec` supports `EXTERNAL` and `INTERNAL`; `EXTERNAL` or omission defaults to external mode.
- `NAME` and `LIBRARY` can appear in any order, but each should appear only once.
- `PARAMETERS` maps SQL arguments and argument properties to the C/C++ function arguments.
- For external functions, `RETURN` in the `PARAMETERS` list must be last. Omitting return property parameters is equivalent to not specifying `RETURN` in that list.
- Dropping an external procedure or function that is currently executing raises an error instead of dropping it.

Example:

```sql
CREATE OR REPLACE LIBRARY lib1 AS 'shlib.so';

CREATE OR REPLACE PROCEDURE str_uppercase_proc(
  a1 IN CHAR(30),
  a2 OUT CHAR(30)
)
AS
LANGUAGE C
LIBRARY lib1
NAME "str_uppercase"
PARAMETERS(a1, a1 LENGTH, a2);
/
```

The mapped C prototype is:

```cpp
extern "C" void str_uppercase(char* str1, long long str1_len, char* str2);
```

#### Entry Function Contract

Every dynamic library must include the standard entry function:

```cpp
extern "C" void entryfunction(
    char* func_name,
    int arg_count,
    void** args,
    void** returnArg);
```

Entry function notes:

- Do not change the entry function name or argument types.
- The entry function dispatches by `func_name` and calls the appropriate user-defined C/C++ function.
- `args` must be interpreted in the same order as the external procedure `PARAMETERS` clause.
- `returnArg` is `NULL` for external procedures with no return value.
- For external functions, check `returnArg` before assigning the return value and cast according to return type.
- Use `extern "C"` for user-defined functions and `entryfunction` to avoid C++ name mangling.

#### External Parameter Properties

| Property | IN C type | OUT, IN OUT, or RETURN C type | Meaning |
| --- | --- | --- | --- |
| `INDICATOR` | `short` | `short *` | NULL indicator: `ALTIBASE_EXTPROC_IND_NULL` or `ALTIBASE_EXTPROC_IND_NOTNULL`. |
| `LENGTH` | `long long` | `long long *` | Value length in bytes. For strings, this is byte length, not character count. |
| `MAXLEN` | not allowed | `long long` | Buffer size for OUT, IN OUT, or RETURN values. |

#### External Data Type Mapping

| PSM type | IN C/C++ type | OUT or IN OUT C/C++ type | RETURN C/C++ type | Notes |
| --- | --- | --- | --- | --- |
| `BIGINT` | `long long` | `long long *` | `long long` |  |
| `BOOLEAN` | `char` | `char *` | `char` | `0` is `FALSE`; `1` is `TRUE`. |
| `SMALLINT`, `INTEGER` | `int` | `int *` | `int` |  |
| `REAL` | `float` | `float *` | `float` |  |
| `DOUBLE` | `double` | `double *` | `double` |  |
| `CHAR`, `VARCHAR`, `NCHAR`, `NVARCHAR`, `BYTE`, `VARBYTE` | `char *` | `char *` | `char *` | Add `LENGTH` and `MAXLEN` parameters where needed for string or binary buffers. |
| `NUMERIC`, `DECIMAL`, `NUMBER`, `FLOAT` | `double` | `double *` | `double` | Precision can be lost when high-precision values are converted to `double`. |
| `DATE`, `INTERVAL` | `SQL_TIMESTAMP_STRUCT` | `SQL_TIMESTAMP_STRUCT *` | `SQL_TIMESTAMP_STRUCT` |  |

#### External Build Checklist

1. Write user-defined C/C++ functions with `extern "C"`.
2. Write `entryfunction` and dispatch by `func_name`.
3. Compile with position-independent shared library options, for example:

```sh
g++ -g -fPIC -shared -o shlib.so extproc.cpp
```

4. Move the shared library to `$ALTIBASE_HOME/lib`.
5. Create or replace the Altibase library object.
6. Create or replace the external procedure or external function.
7. Call it through `EXEC`, SQL, PSM, or a client program.
8. Inspect `SYS_LIBRARIES_`, `V$EXTPROC_AGENT`, `V$LIBRARY`, and `V$PROCINFO` when troubleshooting.

Related properties for external mode agent operation:

- `EXTPROC_AGENT_CONNECT_TIMEOUT`
- `EXTPROC_AGENT_CALL_RETRY_COUNT`
- `EXTPROC_AGENT_IDLE_TIMEOUT`
- `EXTPROC_AGENT_SOCKET_FILEPATH`

These properties do not affect internal mode, because internal mode does not create an Agent Process.

External procedure diagnostics:

```sql
SELECT *
FROM SYSTEM_.SYS_LIBRARIES_
WHERE library_name = '<LIBRARY_NAME>';

SELECT *
FROM V$EXTPROC_AGENT;

SELECT *
FROM V$LIBRARY;

SELECT *
FROM V$PROCINFO;

SELECT name, value1
FROM V$PROPERTY
WHERE name IN (
  'EXTPROC_AGENT_CONNECT_TIMEOUT',
  'EXTPROC_AGENT_CALL_RETRY_COUNT',
  'EXTPROC_AGENT_IDLE_TIMEOUT',
  'EXTPROC_AGENT_SOCKET_FILEPATH'
);
```

Use `SYS_LIBRARIES_` to confirm the database library object, `V$EXTPROC_AGENT` for currently created external-mode Agent Processes, `V$LIBRARY` for dynamic libraries loaded directly by the database, and `V$PROCINFO` to confirm external procedure mode. If exact columns differ by patch, query the installed dictionary layout before writing final diagnostic SQL.

### Oracle PL/SQL Compatibility Notes

#### Usually Similar

- `CREATE PROCEDURE`, `CREATE FUNCTION`, `CREATE PACKAGE`, and `CREATE PACKAGE BODY`.
- DML trigger timing concepts such as `BEFORE`, `AFTER`, `INSTEAD OF`, `REFERENCING`, row triggers, and statement triggers.
- `IN`, `OUT`, and `IN OUT` parameters.
- `AUTHID CURRENT_USER` and `AUTHID DEFINER`.
- `%TYPE` and `%ROWTYPE`.
- `IF`, `CASE`, `LOOP`, `WHILE`, `FOR`, `EXIT`, `CONTINUE`, `GOTO`, and `NULL`.
- Explicit cursors, cursor FOR loops, and cursor attributes.
- `RECORD`, associative-array-like collections, and `REF CURSOR`.
- `BULK COLLECT`, `RETURNING INTO`, and dynamic SQL through `EXECUTE IMMEDIATE`.
- Exception declarations, `RAISE`, `WHEN OTHERS`, `SQLCODE`, `SQLERRM`, `RAISE_APPLICATION_ERROR`, `PRAGMA AUTONOMOUS_TRANSACTION`, and `PRAGMA EXCEPTION_INIT`.

#### Needs Altibase-Specific Handling

- Dynamic SQL bind placeholders in `EXECUTE IMMEDIATE` use `?`, not Oracle-style named bind markers in the SQL string.
- `RAISE_APPLICATION_ERROR` uses Altibase user-defined error codes `990000` through `991000`, not Oracle's negative application-error range.
- `SQLCODE` and `SQLERRM` are used as PSM status values in handlers; do not assume Oracle function signatures.
- `BOOLEAN` is PSM-only and cannot be used as a SQL column type or SQL-callable function return in a SQL statement.
- Altibase stored functions called from SQL have DML and transaction-control restrictions.
- Altibase trigger bodies have strict transaction, session-control, schema-DDL, stored-procedure-call, recursion, LOB table, and replication-receiver boundaries.
- Oracle packages are not automatically available. Map to Altibase packages such as `DBMS_SQL`, `DBMS_OUTPUT`, `DBMS_STATS`, `UTL_FILE`, `UTL_RAW`, `UTL_SMTP`, and `UTL_TCP`, and verify signatures.
- Oracle collection code may need conversion to Altibase `ASSOCIATIVE ARRAY`, `VARRAY` in 7.3+, or `TYPESET`.
- PSM field and label case sensitivity depends on `PSM_CASE_SENSITIVE_MODE`: default `0` in 7.1, default `1` in 7.3 and 8.1.
- For external native code, Altibase requires `LANGUAGE C`, a library object, `entryfunction`, and deployment to `$ALTIBASE_HOME/lib`.

#### Needs Alternative Design or Explicit Review

- Oracle object types, nested tables, pipelined table functions, and Oracle-specific package APIs should not be assumed to exist.
- Oracle Java stored procedures are not equivalent to Altibase C/C++ external procedures.
- Oracle autonomous transaction code should be reviewed for Altibase lock and deadlock behavior.
- Oracle LOB code that stores large temporary values in PSM should be reviewed for 8.1 Temporary LOB memory properties or redesigned for 7.1/7.3.

### Minimal Examples

#### Procedure with Parameters

```sql
CREATE OR REPLACE PROCEDURE give_raise(
  p_eno IN INTEGER,
  p_amount IN NUMBER,
  p_new_salary OUT NUMBER
)
AS
BEGIN
  UPDATE employees
  SET salary = salary + p_amount
  WHERE eno = p_eno
  RETURNING salary INTO p_new_salary;
END;
/
```

#### Function

```sql
CREATE OR REPLACE FUNCTION get_salary(p_eno IN INTEGER)
RETURN NUMBER
AS
  v_salary NUMBER;
BEGIN
  SELECT salary INTO v_salary
  FROM employees
  WHERE eno = p_eno;

  RETURN v_salary;
END;
/
```

#### Cursor Loop

```sql
CREATE OR REPLACE PROCEDURE print_employee_names AS
  CURSOR c_emp IS
    SELECT eno, e_lastname
    FROM employees
    ORDER BY eno;
BEGIN
  FOR r IN c_emp LOOP
    PRINTLN(r.eno || ': ' || r.e_lastname);
  END LOOP;
END;
/
```

#### VARRAY in 7.3+

```sql
CREATE OR REPLACE PROCEDURE collect_names AS
  TYPE name_array IS VARRAY(20) OF VARCHAR(20);
  v_names name_array;
BEGIN
  SELECT e_lastname
  BULK COLLECT INTO v_names
  FROM employees
  WHERE eno BETWEEN 1 AND 20;

  FOR i IN v_names.FIRST() .. v_names.LAST() LOOP
    PRINTLN(v_names[i]);
  END LOOP;
END;
/
```

#### Ref Cursor Result Set

```sql
CREATE TYPESET emp_types AS
  TYPE emp_cur IS REF CURSOR;
END;
/

CREATE OR REPLACE PROCEDURE open_emps(
  p_job IN VARCHAR(20),
  p_result OUT emp_types.emp_cur
)
AS
BEGIN
  OPEN p_result FOR
    'SELECT eno, e_lastname, salary FROM employees WHERE emp_job = ?'
    USING p_job;
END;
/
```

### Troubleshooting Checklist

- Compilation error: check missing `/`, missing semicolon after `END`, parameter mode/default combinations, unsupported data type, ambiguous variable/column names, and package specification/body mismatch.
- Runtime `NO_DATA_FOUND` or `TOO_MANY_ROWS`: review each single-row `SELECT INTO`; use exception handling or `BULK COLLECT` where appropriate.
- Runtime cursor error: check open/close state and cursor attributes; avoid fetching from closed cursors.
- Function called from SQL fails: check for DML or transaction control inside the function.
- Dynamic SQL fails: check `?` placeholder count and `USING` order.
- Trigger fails: check `IS_ENABLE`, trigger granularity, `REFERENCING` aliases, `WHEN` restrictions, forbidden transaction/session/DDL/procedure calls, LOB table limitations, and referenced table changes.
- Package call surprises: remember package initialization runs once per session and package state persists in that session.
- External procedure fails: verify `.so` location under `$ALTIBASE_HOME/lib`, `CREATE LIBRARY`, `entryfunction`, `PARAMETERS` order, `LENGTH` and `MAXLEN`, external mode agent properties, and `V$EXTPROC_AGENT`.
- 8.1 Temporary LOB memory issue: check `TEMPORARY_LOB_ENABLE`, `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`, `MEMORY_TEMPLOB_PIECE_SIZE`, and `V$TEMPORARY_LOBS`.

### Attachment Cross-References

- Use `03_sql_ddl_generation.md` for surrounding object DDL, grants, synonyms, jobs, triggers, and table structures that stored logic depends on.
- Use `05_data_types_properties.md` for exact data type limits, property names, VARRAY memory, Temporary LOB behavior, and conversion constraints.
- Use `07_error_messages_troubleshooting.md` when a PSM, package, cursor, dynamic SQL, or external procedure answer starts from an Altibase error code.
- Use `12_c_cli_odbc_precompiler.md` when native C/C++ clients, CLI, ODBC, or precompiler code must call or complement stored logic.

### Residual Scope

- This attachment covers core PSM generation, trigger PSM body rules, package patterns, VARRAY behavior, and external procedure patterns. It is not a complete built-in package or PL/SQL compatibility catalog; use target-version PSM sources when an answer depends on an unlisted built-in, pragma, or external-procedure edge case.
- PSM and external C/C++ snippets in this attachment are source-audited patterns, not live-compiled artifacts. Ask for the target Altibase version, object DDL, compile error, shared-library build flags, and runtime log excerpt before giving a definitive compile or native-code diagnosis.
## Required Inputs And Stop Conditions
- Exact Altibase version and patch, object DDL, owner/schema, parameter list, data types, referenced objects, privileges, SQL side effects, transaction expectations, and target execution method such as iSQL.
- For external procedures, OS, compiler, bitness, ABI, library filename and path, exported symbol, source code, installed header/library evidence, deployment permissions, runtime logs, and restart or rollback plan.
- Stop before final executable stored logic or native deployment when compile output, runtime error text, object definitions, external library files, platform evidence, or validation plan is missing.
## Validation And Rollback Checks
- Compile PSM objects and check generated errors before treating an example as usable; use iSQL terminator rules literally when testing object creation.
- For external procedures, verify library existence, permissions, symbol export, parameter mapping, and runtime logs before and after registration.
- Rollback by dropping or replacing only the generated objects and restoring previous library files when a backed-up copy and maintenance plan exist.
## Cross-References
- `03_sql_ddl_generation.md` for surrounding object DDL and destructive DDL cautions.
- `04_sql_dml_oracle_compatibility.md` for SQL, functions, and Oracle-overlap behavior inside PSM.
- `05_data_types_properties.md` for data type and property boundaries.
- `12_c_cli_odbc_precompiler.md` for native C/client compile, link, and library details.
- `13_isql_iloader_basic_tools.md` for iSQL execution and script capture.
- `07_error_messages_troubleshooting.md` for compile, runtime, and loader error response.
## Residual Scope And Limitations
- This file supports guarded first drafts of PSM and external procedure work, not proof that native code is safe to load into a production server.
- Compiler, ABI, library path, symbol export, installed tool output, runtime logs, and object definitions are customer-environment facts and must not be invented.
- English-only stored-procedure media extraction rows remain excluded from authoritative upload content unless a later source-authority decision changes that route.
