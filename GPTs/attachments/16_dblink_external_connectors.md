# 16. DB Link and External Connectors

## Applicable Versions

- 7.1: Based on Altibase 7.1 DB Link and Altibase Hadoop Connector guidance.
- 7.3: Based on Altibase 7.3 DB Link, Altibase Hadoop Connector, and third-party connector guidance.
- 8.1: Based on Altibase 8.1 verified source DB Link, Altibase Hadoop Connector, and third-party connector guidance.

## Questions This File Can Answer

- How should `DB Link` be enabled, configured, monitored, and used?
- Which `DB Link` SQL syntax, properties, performance views, and remote access methods matter?
- Which JDBC and Altibase data types are supported through `DB Link`?
- How is the Altibase Hadoop Connector installed and used with Sqoop?
- Which Altibase data types can the Hadoop Connector import or export?
- How should DBeaver connect to Altibase, and how are common DBeaver issues handled?
- How should Hibernate use `AltibaseDialect` and the Altibase JDBC driver?
- How does OpenLDAP `back-sql` connect to Altibase through ODBC metadata mapping?

## Source Documents

- 7.1: Altibase 7.1 DB Link User's Manual; Hadoop Connector User's Manual.
- 7.3: Altibase 7.3 DB Link User's Manual; Hadoop Connector User's Manual; Altibase 3rd Party Connector Guide.
- 8.1: Altibase 8.1 verified source DB Link User's Manual; Hadoop Connector User's Manual; Altibase 3rd Party Connector Guide.

## Response Rules

- Answer explanatory text in the user's language.
- Keep SQL object names, SQL syntax, connector names, class names, property names, command options, file names, paths, and error codes literal.
- For 8.1-specific statements, say `Altibase 8.1 verified source`.
- Do not expose internal source labels, repository paths, workstation paths, or source-image names in customer answers.
- Ask for Altibase version, remote DBMS, JDBC driver version, Java version, target host and port, transaction level, connector version, and network/firewall context before giving production-ready integration commands.
- Treat sample accounts such as `SYS` and `MANAGER` as placeholders. Advise users to use least-privilege accounts and protected secret handling.
- For SSL/TLS, truststores, certificate verification, and ciphers, use `11_java_jdbc_spring.md` and `18_security_ssl_tls.md` for Altibase JDBC/SSL parameter names. This attachment gives connector workflow context and should not invent connector-specific TLS placement unless the connector accepts the documented Altibase JDBC URL or properties.
- For generic JDBC URL attributes, Spring Boot, and Hibernate application code, cross-reference the Java/JDBC/Spring attachment.

## Fast Decision Map

```mermaid
flowchart TD
  A[Integration question] --> B{Connector}
  B -- SQL across databases --> C[DB Link]
  B -- Hadoop or Sqoop --> D[Altibase Hadoop Connector]
  B -- GUI SQL client --> E[DBeaver]
  B -- ORM --> F[Hibernate]
  B -- LDAP directory backed by RDBMS --> G[OpenLDAP back-sql]
  C --> H{Remote access style}
  H -- SELECT pushdown --> I[REMOTE_TABLE]
  H -- DML DDL DCL pass-through --> J[REMOTE_EXECUTE_IMMEDIATE]
  H -- Bind variables or batch --> K[REMOTE_* functions in PSM]
  H -- Compatibility only --> L[location descriptor @]
  D --> M{Direction}
  M -- Altibase to HDFS/Hive --> N[sqoop import]
  M -- HDFS to Altibase --> O[sqoop export]
```

## Version Differences

Version block: 7.1

- `DB Link` and Altibase Hadoop Connector behavior is materially the same as the 7.3 source except for documentation wording.
- `DB Link` requires `DBLINK_ENABLE=1` in `altibase.properties` and `ALTILINKER_ENABLE=1` in `dblink.conf` for heterogeneous links.
- `CREATE DATABASE LINK IF NOT EXISTS` and `DROP DATABASE LINK IF EXISTS` are not documented in the 7.1 DB Link source.
- Hadoop Connector requirements are `JRE` or `JDK` 1.6 or later, Hadoop 1.0, Sqoop 1.4.4 or later, and Altibase 5.0 or later.
- For DBeaver, the third-party connector guide states compatibility with Altibase Server 7.1.0 and later.
- For Hibernate 6.4 Spring guidance, the dedicated Spring guide uses Altibase server 7.1.0.9.3 or later and Altibase JDBC driver 7.1.0.9.0 or later. With the 7.1 JDBC driver, add `lob_null_select=off` when Hibernate LOB features are used.

Version block: 7.3

- `DB Link` and Hadoop Connector behavior is stable from 7.1 for the covered procedures.
- Third-party connector guidance covers DBeaver and OpenLDAP; the 8.1 verified source adds a concise Hibernate connector chapter.
- For Hibernate 6.4 Spring guidance, the Altibase JDBC driver is available from Maven Central starting with Altibase 7.3.0.0.2, and `lob_null_select` defaults to `off`.

Version block: 8.1

- Use the wording `Altibase 8.1 verified source` for 8.1-specific DB Link and connector statements.
- `CREATE DATABASE LINK` supports `IF NOT EXISTS` in the Altibase 8.1 verified source.
- `DROP DATABASE LINK` supports `IF EXISTS` in the Altibase 8.1 verified source.
- The Altibase 8.1 verified source keeps the same DB Link architecture, AltiLinker configuration model, Hadoop Connector command model, and DBeaver/OpenLDAP connector guidance unless otherwise stated.
- The Altibase 8.1 verified source third-party connector guide includes Hibernate connector guidance for `AltibaseDialect`.

## Connector Block Format

Each connector block uses these fields:

- Purpose: what the connector does.
- When to Use: the practical integration scenario.
- Required Pieces: software, drivers, services, properties, or accounts.
- Setup: concise procedure or syntax.
- Cautions: support limits, version sensitivity, or common mistakes.
- Verification: how to confirm the connector is working.

## Connector Block: `DB Link`

Purpose: `DB Link` lets an Altibase local server execute SQL against a remote Altibase or heterogeneous database server through a database link object.

When to Use:

- Query remote tables or views from Altibase SQL.
- Push a whole `SELECT` to a remote server with `REMOTE_TABLE`.
- Execute remote DML, DDL, or DCL with `REMOTE_EXECUTE_IMMEDIATE`.
- Use PSM `REMOTE_*` functions when bind variables or batch execution are required.

Required Pieces:

- Local Altibase server.
- Remote database server reachable from the local server host.
- `AltiLinker` process for heterogeneous links.
- Remote DBMS JDBC driver installed on the same host where `AltiLinker` runs.
- `JRE` compatible with `AltiLinker` and the remote JDBC driver.
- `altibase.properties` and `dblink.conf` configured.
- `CREATE DATABASE LINK` privilege for link creation; `DROP DATABASE LINK` privilege for link deletion.

DB Link architecture:

```mermaid
flowchart LR
  U[Client SQL] --> L[Local Altibase server]
  L --> DK[DB Link module]
  DK <-- ADLP over TCP --> AL[AltiLinker]
  AL <-- JDBC --> R[Remote DBMS]
  R --> AL --> DK --> L --> U
```

Core process:

1. The user submits SQL to the local Altibase server.
2. The local query processor parses the SQL and prepares remote work.
3. The DB Link module sends remote requests to `AltiLinker` through ADLP over TCP.
4. `AltiLinker` executes the request against the remote DBMS through JDBC.
5. The remote DBMS returns results to `AltiLinker`.
6. `AltiLinker` returns results to the local server, and the local server converts and uses the data.

Link types:

- Homogeneous Link: remote server is an Altibase server using the same protocol version. It does not pass through `AltiLinker` and is faster for frequent remote access. Altibase 6.5.1 does not support Homogeneous Links.
- Heterogeneous Link: remote server is a heterogeneous DBMS, or an Altibase server whose version differs from the local server. It uses `AltiLinker` and JDBC.

Setup:

1. Install a compatible `JRE` on the local server host.
2. Install the remote DBMS JDBC driver on the local server host where `AltiLinker` runs.
3. Set Java environment variables, for example:

```sh
export JAVA_HOME=<jre_home>
export CLASSPATH=${JAVA_HOME}/lib:${CLASSPATH}
export PATH=${JAVA_HOME}/bin:${PATH}
```

4. In `altibase.properties`, set:

```properties
DBLINK_ENABLE = 1
```

5. In `$ALTIBASE_HOME/conf/dblink.conf`, set `ALTILINKER_ENABLE`, `ALTILINKER_PORT_NO`, and at least one `TARGETS` entry:

```properties
ALTILINKER_ENABLE = 1
ALTILINKER_PORT_NO = 23238

TARGETS = (
  (
    NAME = "alti_remote"
    JDBC_DRIVER = "$ALTIBASE_HOME/lib/Altibase.jar"
    CONNECTION_URL = "jdbc:Altibase://remote-host:20300/mydb"
    USER = "remote_user"
    PASSWORD = "remote_password"
    XADATASOURCE_CLASS_NAME = "Altibase.jdbc.driver.AltibaseXADataSource"
    XADATASOURCE_URL_SETTER_NAME = "setURL"
  )
)
```

6. Restart the Altibase server, or start `AltiLinker` in `SYSDBA` mode:

```sql
ALTER DATABASE LINKER START;
```

7. Create a database link object:

```sql
CREATE PRIVATE DATABASE LINK link1
CONNECT TO remote_user IDENTIFIED BY remote_password
USING alti_remote;
```

Cautions:

- `AltiLinker` runs on the same server as the local Altibase server.
- The remote JDBC driver is mandatory for heterogeneous links.
- `JDBC_DRIVER` and `CONNECTION_URL` are mandatory in each `TARGETS` entry.
- `USER` and `PASSWORD` in `CREATE DATABASE LINK` take priority over `USER` and `PASSWORD` in `dblink.conf`.
- If user names or passwords are case-sensitive or contain special characters, quote them in `CREATE DATABASE LINK`.
- A database link object targets exactly one remote server.
- `PRIVATE` links are usable by the creator and `SYS`; `PUBLIC` links are usable by all users, but only the creator or `SYS` can drop them.

Verification:

```sql
SELECT * FROM V$DBLINK_ALTILINKER_STATUS;
SELECT * FROM V$DBLINK_DATABASE_LINK_INFO;
SELECT * FROM REMOTE_TABLE(link1, 'select 1 from dual');
```

## DB Link Syntax

Compact syntax for 7.1 and 7.3:

```text
CREATE [PUBLIC | PRIVATE] DATABASE LINK dblink_name
  CONNECT TO user_id IDENTIFIED BY password
  USING target_name;

DROP [PUBLIC | PRIVATE] DATABASE LINK dblink_name;
```

Compact syntax for Altibase 8.1 verified source:

```text
CREATE [PUBLIC | PRIVATE] DATABASE LINK [IF NOT EXISTS] dblink_name
  CONNECT TO user_id IDENTIFIED BY password
  USING target_name;

DROP [PUBLIC | PRIVATE] DATABASE LINK [IF EXISTS] dblink_name;
```

Common DB Link control syntax:

```text
ALTER DATABASE LINKER { START | STOP | STOP FORCE | DUMP };

ALTER SESSION CLOSE DATABASE LINK { ALL | dblink_name };

COMMIT FORCE DATABASE LINK;

ROLLBACK FORCE DATABASE LINK;
```

`ALTER DATABASE LINKER` notes:

- `START`: starts `AltiLinker` when no `AltiLinker` process is running.
- `STOP`: stops `AltiLinker` only when no transaction is using DB Link.
- `STOP FORCE`: stops `AltiLinker` even if a transaction is using DB Link.
- `DUMP`: writes current `AltiLinker` thread operations to `$ALTIBASE_HOME/trc/altibase_lk_dump.log`.
- Only `SYS` in `SYSDBA` mode can run `ALTER DATABASE LINKER`.

`ALTER SESSION CLOSE DATABASE LINK` notes:

- `ALL`: closes all linker sessions for the current Altibase server.
- `dblink_name`: closes linker sessions associated with that database link.
- All users can execute this statement.

## DB Link Remote Access Methods

Method block: `REMOTE_TABLE`

- Purpose: execute a remote `SELECT` as pass-through SQL.
- Use in: `FROM` clause of a local `SELECT`.
- Syntax:

```text
REMOTE_TABLE (
  dblink_name    IN VARCHAR,
  statement_text IN VARCHAR
)
```

- Example:

```sql
SELECT *
FROM REMOTE_TABLE(link1, 'select c1, c2 from t1 where c1 = 10');
```

- Cautions: `REMOTE_TABLE` accepts only `SELECT`; it does not bind parameter markers. For repeated access to remote query results, use `REMOTE_TABLE_STORE` behavior where appropriate.

Method block: location descriptor `@`

- Purpose: compatibility style for remote table or view access.
- Example:

```sql
SELECT * FROM t1@link1;
```

- Cautions: only tables and views are accessible with `@`; only `SELECT` is executable. Queries using `@` can retrieve all remote records to the local server before filtering, which can add network, CPU, memory, and temporary I/O cost. Prefer `REMOTE_TABLE` for remote predicate pushdown.

Method block: `REMOTE_EXECUTE_IMMEDIATE`

- Purpose: execute remote DML, DDL, or DCL except `SELECT`.
- Syntax:

```text
REMOTE_EXECUTE_IMMEDIATE (
  dblink_name    IN VARCHAR,
  statement_text IN VARCHAR
);
```

- Example:

```sql
EXEC REMOTE_EXECUTE_IMMEDIATE('link1', 'create table remote_t(c1 integer)');
EXEC REMOTE_EXECUTE_IMMEDIATE('link1', 'insert into remote_t values (10)');
```

- Cautions: `SELECT` is excluded. Parameter markers cannot be bound with this procedure.

Method block: `REMOTE_*` functions with bind variables

- Purpose: execute remote SQL with parameter markers in stored procedures or stored functions.
- SELECT call order:

```text
REMOTE_ALLOC_STATEMENT
REMOTE_BIND_VARIABLE
REMOTE_EXECUTE_STATEMENT
REMOTE_NEXT_ROW
REMOTE_GET_COLUMN_VALUE_type
REMOTE_FREE_STATEMENT
```

- DML, DDL, or DCL call order:

```text
REMOTE_ALLOC_STATEMENT
REMOTE_BIND_VARIABLE
REMOTE_EXECUTE_STATEMENT
REMOTE_FREE_STATEMENT
```

- Result access functions:

```text
REMOTE_GET_COLUMN_VALUE_CHAR
REMOTE_GET_COLUMN_VALUE_VARCHAR
REMOTE_GET_COLUMN_VALUE_FLOAT
REMOTE_GET_COLUMN_VALUE_SMALLINT
REMOTE_GET_COLUMN_VALUE_INTEGER
REMOTE_GET_COLUMN_VALUE_BIGINT
REMOTE_GET_COLUMN_VALUE_REAL
REMOTE_GET_COLUMN_VALUE_DOUBLE
REMOTE_GET_COLUMN_VALUE_DATE
```

Method block: batch `REMOTE_*` functions

- Purpose: execute remote batch operations from PSM.
- Recommended call order:

```text
REMOTE_ALLOC_STATEMENT_BATCH
REMOTE_BIND_VARIABLE_BATCH
REMOTE_ADD_BATCH
REMOTE_EXECUTE_BATCH
REMOTE_GET_RESULT_COUNT_BATCH
REMOTE_GET_RESULT_BATCH
REMOTE_FREE_STATEMENT_BATCH
```

- Helper functions: `IS_ARRAY_BOUND`, `IS_FIRST_ARRAY_BOUND`, `IS_LAST_ARRAY_BOUND`.

## DB Link Remote Object Support

Remote object block: table

- `@` support: yes.
- `REMOTE_*` support: yes.
- Typical access: `REMOTE_TABLE` for `SELECT`; `REMOTE_EXECUTE_IMMEDIATE` or binding functions for DML and DDL.

Remote object block: view

- `@` support: yes.
- `REMOTE_*` support: yes.
- Typical access: `SELECT * FROM REMOTE_TABLE(link1, 'select * from v1')`.

Remote object block: index

- `@` support: no.
- `REMOTE_*` support: yes.
- Typical access: create or drop with `REMOTE_EXECUTE_IMMEDIATE`.

Remote object block: stored procedure

- `@` support: no.
- `REMOTE_*` support: yes.
- Typical access: create or call remote procedures with pass-through SQL.
- Restriction: a local stored procedure cannot declare `ROWTYPE` variables or cursors dependent on a remote server table.

Remote object block: sequence

- `@` support: no.
- `REMOTE_*` support: yes.
- Typical access: use `REMOTE_TABLE` for sequence values in `SELECT`, or `REMOTE_EXECUTE_IMMEDIATE` when a remote DML statement references the sequence.

Remote object block: queue

- `@` support: no.
- `REMOTE_*` support: yes.
- Typical access: `REMOTE_TABLE` for queue reads and `REMOTE_EXECUTE_IMMEDIATE` for enqueue statements.

Remote object block: trigger

- `@` support: no.
- `REMOTE_*` support: yes.
- Typical access: create or drop remote triggers with pass-through DDL.

Remote object block: synonym

- `@` support: no.
- `REMOTE_*` support: yes.
- Typical access: query or modify the underlying object through pass-through SQL.

Remote object block: constraint

- `@` support: no.
- `REMOTE_*` support: yes.
- Typical access: add, drop, or set constraints with pass-through SQL.

## DB Link Transaction Levels

```mermaid
flowchart TD
  A[DBLINK_GLOBAL_TRANSACTION_LEVEL] --> B{Level}
  B -- Remote statement execution --> C[Remote and local work are separate transactions]
  B -- Simple transaction commit --> D[Atomicity check without full 2PC prepare exchange]
  B -- Two-phase commit --> E[Prepare phase then commit phase]
  D --> F[Remote DBMS must support autocommit OFF]
  E --> G[Use COMMIT FORCE DATABASE LINK or ROLLBACK FORCE DATABASE LINK for failure recovery cases]
```

Level block: Remote Statement Execution

- Guarantees statement execution on the remote node, not global transaction consistency.
- Local and remote statements inside one global transaction are processed as separate transactions.
- `AltiLinker` connects to the remote server with autocommit `ON` by default for this level.

Level block: Simple Transaction Commit

- Enforces atomicity between Altibase and a heterogeneous DBMS with a simpler mechanism than full 2PC.
- Requires the remote DBMS to support autocommit `OFF`.
- `AltiLinker` connects to the remote server with autocommit `OFF` by default for this level.

Level block: Two-Phase Commit

- Set `DBLINK_GLOBAL_TRANSACTION_LEVEL` to `2`.
- Prepare phase: Altibase writes a prepare log and asks `AltiLinker` to prepare participants.
- Commit phase: Altibase writes a commit log and asks `AltiLinker` to commit participants.
- Failure before prepare log: remote transactions without log trace are canceled.
- Failure after prepare log and before commit log: Altibase recovers remote transactions toward rollback.
- Failure after commit log and before end log: Altibase keeps trying to complete commit or rollback and writes the end log after completion.

## DB Link Property Blocks

Property group: `altibase.properties`

- `AUTO_REMOTE_EXEC`: DB Link-related remote execution property.
- `DBLINK_ENABLE`: must be `1` to use DB Link.
- `DBLINK_GLOBAL_TRANSACTION_LEVEL`: controls remote statement, simple commit, or two-phase commit behavior.
- `DBLINK_RECOVERY_MAX_LOGFILE`: DB Link recovery log file control.
- `DBLINK_REMOTE_STATEMENT_AUTOCOMMIT`: remote statement autocommit behavior.
- `DBLINK_REMOTE_TABLE_BUFFER_SIZE`: remote table buffer size.
- `DBLINK_DATA_BUFFER_BLOCK_SIZE`: DB Link data buffer block size.
- `DBLINK_DATA_BUFFER_BLOCK_COUNT`: DB Link data buffer block count.
- `DBLINK_DATA_BUFFER_ALLOC_RATIO`: DB Link buffer allocation ratio.
- `DBLINK_ALTILINKER_CONNECT_TIMEOUT`: local server wait time for connection to `AltiLinker`.

Property group: `dblink.conf`

- `ALTILINKER_ENABLE`: `1` starts `AltiLinker`; `0` disables it.
- `ALTILINKER_PORT_NO`: TCP port where `AltiLinker` listens; valid port range is `1024` through `65535`.
- `ALTILINKER_RECEIVE_TIMEOUT`: maximum wait when Altibase exchanges data with `AltiLinker`.
- `ALTILINKER_REMOTE_NODE_RECEIVE_TIMEOUT`: maximum wait for remote prepare, DCL, and autocommit-setting operations.
- `ALTILINKER_QUERY_TIMEOUT`: maximum remote `SELECT` execution time.
- `ALTILINKER_NON_QUERY_TIMEOUT`: maximum remote non-`SELECT` execution time.
- `ALTILINKER_THREAD_COUNT`: number of `AltiLinker` threads for remote SQL execution.
- `ALTILINKER_THREAD_SLEEP_TIME`: idle wait for `AltiLinker` worker threads.
- `ALTILINKER_REMOTE_NODE_SESSION_COUNT`: maximum sessions for remote server connections; one is used as the linker control session.
- `ALTILINKER_TRACE_LOG_DIR`: trace log directory; default is `$ALTIBASE_HOME/trc`.
- `ALTILINKER_TRACE_LOG_FILE_SIZE`: maximum trace log file size.
- `ALTILINKER_TRACE_LOG_FILE_COUNT`: maximum trace log file count.
- `ALTILINKER_TRACE_LOGGING_LEVEL`: `0` none, `1` FATAL, `2` ERROR, `3` WARNING, `4` INFO, `5` DEBUG, `6` TRACE.
- `ALTILINKER_JVM_BIT_DATA_MODEL_VALUE`: `0` for 32-bit JVM, `1` for 64-bit JVM.
- `ALTILINKER_JVM_MEMORY_POOL_INIT_SIZE`: initial JVM memory pool for `AltiLinker`.
- `ALTILINKER_JVM_MEMORY_POOL_MAX_SIZE`: maximum JVM memory pool for `AltiLinker`.

Property group: `TARGETS`

- `TARGETS/NAME`: logical remote target name referenced by `CREATE DATABASE LINK ... USING target_name`.
- `TARGETS/JDBC_DRIVER`: path to the remote DBMS JDBC driver.
- `TARGETS/JDBC_DRIVER_CLASS_NAME`: JDBC driver class name; optional when the driver implements `java.sql.Driver` and can be loaded automatically.
- `TARGETS/CONNECTION_URL`: JDBC URL for the remote database.
- `TARGETS/USER`: remote database user.
- `TARGETS/PASSWORD`: remote database password.
- `TARGETS/XADATASOURCE_CLASS_NAME`: XADataSource class name for two-phase commit support.
- `TARGETS/XADATASOURCE_URL_SETTER_NAME`: setter method for the XADataSource URL, commonly `setURL`.

Monitoring views:

- `V$DBLINK_ALTILINKER_STATUS`: `AltiLinker` process and JVM memory status.
- `V$DBLINK_DATABASE_LINK_INFO`: database link object information.
- `V$DBLINK_GLOBAL_TRANSACTION_INFO`: global transaction information.
- `V$DBLINK_LINKER_CONTROL_SESSION_INFO`: linker control session information.
- `V$DBLINK_LINKER_DATA_SESSION_INFO`: linker data session information.
- `V$DBLINK_LINKER_SESSION_INFO`: linker session information.
- `V$DBLINK_NOTIFIER_TRANSACTION_INFO`: notifier transaction information.
- `V$DBLINK_REMOTE_STATEMENT_INFO`: remote statement information.
- `V$DBLINK_REMOTE_TRANSACTION_INFO`: remote transaction information.
- `SYS_DATABASE_LINKS_`: DB Link metadata table.

## DB Link Data Type Support Blocks

DB Link type block: `java.sql.Types.CHAR`

- Altibase SQL type: `CHAR`.
- Standard SQL type: `CHAR`.
- Support: yes.
- Notes: supported through JDBC v3.0 mapping.

DB Link type block: `java.sql.Types.VARCHAR`

- Altibase SQL type: `VARCHAR`.
- Standard SQL type: `VARCHAR`.
- Support: yes.
- Notes: supported through JDBC v3.0 mapping.

DB Link type block: `java.sql.Types.LONGVARCHAR`

- Altibase SQL type: none.
- Standard SQL type: `LONGVARCHAR`.
- Support: no.
- Notes: use a supported character type where possible.

DB Link type block: `java.sql.Types.NCHAR`

- Altibase SQL type: `NCHAR`.
- Standard SQL type: `NCHAR`.
- Support: no.
- Notes: JDBC v4.0 type, not supported by DB Link data type mapping.

DB Link type block: `java.sql.Types.NVARCHAR`

- Altibase SQL type: `NVARCHAR`.
- Standard SQL type: `NVARCHAR`.
- Support: no.
- Notes: JDBC v4.0 type, not supported by DB Link data type mapping.

DB Link type block: `java.sql.Types.LONGNVARCHAR`

- Altibase SQL type: none.
- Standard SQL type: `LONGNVARCHAR`.
- Support: no.
- Notes: JDBC v4.0 type, not supported by DB Link data type mapping.

DB Link type block: `java.sql.Types.NUMERIC`

- Altibase SQL type: `NUMERIC`.
- Standard SQL type: `NUMERIC`.
- Support: yes.
- Notes: supported through JDBC v3.0 mapping.

DB Link type block: `java.sql.Types.DECIMAL`

- Altibase SQL type: `DECIMAL`.
- Standard SQL type: `DECIMAL`.
- Support: yes.
- Notes: supported through JDBC v3.0 mapping.

DB Link type block: `java.sql.Types.BIT`

- Altibase SQL type: `SMALLINT`.
- Standard SQL type: `BIT`.
- Support: yes.
- Notes: standard `BIT` is mapped to `SMALLINT` because Altibase `BIT` stores a bit set rather than only one bit.

DB Link type block: Altibase `BIT` bitset

- Altibase SQL type: `BIT`.
- Standard SQL type: none.
- Support: no.
- Notes: Altibase bitset-style `BIT` is not supported through DB Link mapping.

DB Link type block: `java.sql.Types.BOOLEAN`

- Altibase SQL type: `SMALLINT`.
- Standard SQL type: `BOOLEAN`.
- Support: yes.
- Notes: Altibase does not provide a `BOOLEAN` SQL type, so DB Link maps it to `SMALLINT`. If the remote server is Altibase, `INSERT` is not possible for this type.

DB Link type block: `java.sql.Types.TINYINT`

- Altibase SQL type: `SMALLINT`.
- Standard SQL type: `TINYINT`.
- Support: yes.
- Notes: Altibase does not provide `TINYINT`, so DB Link maps it to `SMALLINT`.

DB Link type block: `java.sql.Types.SMALLINT`

- Altibase SQL type: `SMALLINT`.
- Standard SQL type: `SMALLINT`.
- Support: yes.
- Notes: supported through JDBC v3.0 mapping.

DB Link type block: `java.sql.Types.INTEGER`

- Altibase SQL type: `INTEGER`.
- Standard SQL type: `INTEGER`.
- Support: yes.
- Notes: supported through JDBC v3.0 mapping.

DB Link type block: `java.sql.Types.BIGINT`

- Altibase SQL type: `BIGINT`.
- Standard SQL type: `BIGINT`.
- Support: yes.
- Notes: supported through JDBC v3.0 mapping.

DB Link type block: `java.sql.Types.REAL`

- Altibase SQL type: `REAL`.
- Standard SQL type: `REAL`.
- Support: yes.
- Notes: supported through JDBC v3.0 mapping.

DB Link type block: `java.sql.Types.FLOAT`

- Altibase SQL type: `FLOAT`.
- Standard SQL type: `FLOAT`.
- Support: yes.
- Notes: supported through JDBC v3.0 mapping.

DB Link type block: `java.sql.Types.DOUBLE`

- Altibase SQL type: `DOUBLE`.
- Standard SQL type: `DOUBLE`.
- Support: yes.
- Notes: supported through JDBC v3.0 mapping.

DB Link type block: `java.sql.Types.BINARY`

- Altibase SQL type: `BINARY`.
- Standard SQL type: `BINARY`.
- Support: no.
- Notes: if the remote server is Altibase, `INSERT` is not possible for this type.

DB Link type block: `java.sql.Types.VARBINARY`

- Altibase SQL type: none.
- Standard SQL type: `VARBINARY`.
- Support: no.
- Notes: not supported by DB Link data type mapping.

DB Link type block: `java.sql.Types.LONGVARBINARY`

- Altibase SQL type: none.
- Standard SQL type: `LONGVARBINARY`.
- Support: no.
- Notes: not supported by DB Link data type mapping.

DB Link type block: `java.sql.Types.DATE`

- Altibase SQL type: `DATE`.
- Standard SQL type: `DATE`.
- Support: yes.
- Notes: if the year value is B.C., Altibase processes it as `0`.

DB Link type block: `java.sql.Types.TIME`

- Altibase SQL type: `DATE`.
- Standard SQL type: `TIME`.
- Support: yes.
- Notes: remote timestamp precision finer than microseconds is converted to Altibase microsecond precision.

DB Link type block: `java.sql.Types.TIMESTAMP`

- Altibase SQL type: `DATE`.
- Standard SQL type: `TIMESTAMP`.
- Support: yes.
- Notes: remote timestamp precision finer than microseconds is converted to Altibase microsecond precision. If the year value is B.C., Altibase processes it as `0`.

DB Link type block: `java.sql.Types.CLOB`

- Altibase SQL type: `CLOB`.
- Standard SQL type: `CLOB`.
- Support: no.
- Notes: not supported by DB Link data type mapping.

DB Link type block: `java.sql.Types.NCLOB`

- Altibase SQL type: none.
- Standard SQL type: `NCLOB`.
- Support: no.
- Notes: JDBC v4.0 type, not supported by DB Link data type mapping.

DB Link type block: `java.sql.Types.BLOB`

- Altibase SQL type: `BLOB`.
- Standard SQL type: `BLOB`.
- Support: no.
- Notes: not supported by DB Link data type mapping.

DB Link type block: `java.sql.Types.ARRAY`

- Altibase SQL type: none.
- Standard SQL type: none.
- Support: no.
- Notes: not supported by DB Link data type mapping.

DB Link type block: `java.sql.Types.DISTINCT`

- Altibase SQL type: none.
- Standard SQL type: none.
- Support: no.
- Notes: not supported by DB Link data type mapping.

DB Link type block: `java.sql.Types.STRUCT`

- Altibase SQL type: none.
- Standard SQL type: none.
- Support: no.
- Notes: not supported by DB Link data type mapping.

DB Link type block: `java.sql.Types.REF`

- Altibase SQL type: none.
- Standard SQL type: none.
- Support: no.
- Notes: not supported by DB Link data type mapping.

DB Link type block: `java.sql.Types.DATALINK`

- Altibase SQL type: none.
- Standard SQL type: none.
- Support: no.
- Notes: not supported by DB Link data type mapping.

DB Link type block: `java.sql.Types.JAVA_OBJECT`

- Altibase SQL type: none.
- Standard SQL type: none.
- Support: no.
- Notes: not supported by DB Link data type mapping.

DB Link type block: Altibase `NIBBLE`

- Altibase SQL type: `NIBBLE`.
- Standard SQL type: none.
- Support: no.
- Notes: not supported by DB Link data type mapping.

DB Link type block: Altibase `VARBIT`

- Altibase SQL type: `VARBIT`.
- Standard SQL type: none.
- Support: no.
- Notes: not supported by DB Link data type mapping.

DB Link type block: Altibase `INTERVAL`

- Altibase SQL type: `INTERVAL`.
- Standard SQL type: none.
- Support: no.
- Notes: not supported by DB Link data type mapping.

## Connector Block: Altibase Hadoop Connector

Purpose: Altibase Hadoop Connector transfers data between Altibase and Hadoop through Sqoop.

When to Use:

- Import Altibase table data into HDFS as text, sequence, or Avro files.
- Import Altibase table data into Hive.
- Export HDFS data into Altibase.
- List Altibase databases or tables from a Sqoop environment.

Required Pieces:

- `JRE` or `JDK` 1.6 or later.
- Hadoop 1.0 in the source manual baseline.
- Sqoop 1.4.4 or later.
- Altibase 5.0 or later.
- Altibase JDBC driver copied to `$SQOOP_HOME/lib`.
- Altibase Hadoop Connector JAR copied to `$SQOOP_HOME/lib`.

Setup:

```sh
cp $ALTIBASE_HOME/lib/Altibase.jar $SQOOP_HOME/lib
cp altibase_sqoop14_connector.jar $SQOOP_HOME/lib
```

Connection test:

```sh
sqoop list-tables \
  --connect jdbc:Altibase://127.0.0.1:20300/mydb \
  --driver Altibase.jdbc.driver.AltibaseDriver \
  --username SYS \
  --password MANAGER \
  --connection-manager com.altibase.sqoop.manager.AltibaseManager
```

Expected success signals include log messages similar to:

```text
manager.AltibaseManager: init default option autocommit false
manager.SqlManager: Using default fetchSize of 1000
manager.AltibaseManager: Altibase manager 1.0 connector create
```

Common command syntax:

```text
sqoop <command>
  --connect jdbc:Altibase://host:port/mydb
  --driver Altibase.jdbc.driver.AltibaseDriver
  --username user
  --password password
  --connection-manager com.altibase.sqoop.manager.AltibaseManager
```

Command option block:

- `<command>`: examples covered by the source are `import`, `export`, `list-databases`, and `list-tables`.
- `--connect`: Altibase JDBC URL, for example `jdbc:Altibase://host:20300/mydb`.
- `--driver`: `Altibase.jdbc.driver.AltibaseDriver`.
- `--username`: database user.
- `--password`: database password.
- `--connection-manager`: `com.altibase.sqoop.manager.AltibaseManager`.

Import block: HDFS text file

- Purpose: import an Altibase table into an HDFS directory as text.
- Representative command:

```sh
sqoop import \
  --connect jdbc:Altibase://host:20300/mydb \
  --driver Altibase.jdbc.driver.AltibaseDriver \
  --username app_user \
  --password app_password \
  --connection-manager com.altibase.sqoop.manager.AltibaseManager \
  --table table_name \
  --split-by split_column
```

- Text delimiter options: `--enclosed-by`, `--escaped-by`, `--fields-terminated-by`, `--lines-terminated-by`, `--mysql-delimiters`, `--optionally-enclosed-by`.
- Default field separator: comma.
- Default line separator: `\n`.
- Caution: if a line separator or field separator appears in field data, enclose the field. If a quotation mark appears in field data, prefix it with an escape character.

Import block: HDFS sequence file

```sh
sqoop import \
  --connect jdbc:Altibase://host:20300/mydb \
  --driver Altibase.jdbc.driver.AltibaseDriver \
  --username app_user \
  --password app_password \
  --connection-manager com.altibase.sqoop.manager.AltibaseManager \
  --table table_name \
  --split-by split_column \
  --as-sequencefile
```

Import block: HDFS Avro file

```sh
sqoop import \
  --connect jdbc:Altibase://host:20300/mydb \
  --driver Altibase.jdbc.driver.AltibaseDriver \
  --username app_user \
  --password app_password \
  --connection-manager com.altibase.sqoop.manager.AltibaseManager \
  --table table_name \
  --split-by split_column \
  --as-avrodatafile
```

Import block: query-based import

```sh
sqoop import \
  --connect jdbc:Altibase://host:20300/mydb \
  --driver Altibase.jdbc.driver.AltibaseDriver \
  --username app_user \
  --password app_password \
  --connection-manager com.altibase.sqoop.manager.AltibaseManager \
  --table table_name \
  --split-by split_column \
  --boundary-query query_text
```

Import block: Hive

```sh
sqoop import \
  --connect jdbc:Altibase://host:20300/mydb \
  --driver Altibase.jdbc.driver.AltibaseDriver \
  --username app_user \
  --password app_password \
  --connection-manager com.altibase.sqoop.manager.AltibaseManager \
  --table table_name \
  --split-by split_column \
  --hive-import
```

Export block: insert HDFS data into Altibase

```sh
sqoop export \
  -D sqoop.export.records.per.statement=100 \
  --connect jdbc:Altibase://host:20300/mydb \
  --driver Altibase.jdbc.driver.AltibaseDriver \
  --username app_user \
  --password app_password \
  --connection-manager com.altibase.sqoop.manager.AltibaseManager \
  --table table_name \
  --export-dir hdfs_dir
```

Export block: batch insert

```sh
sqoop export \
  --connect jdbc:Altibase://host:20300/mydb \
  --driver Altibase.jdbc.driver.AltibaseDriver \
  --username app_user \
  --password app_password \
  --connection-manager com.altibase.sqoop.manager.AltibaseManager \
  --table table_name \
  --export-dir hdfs_dir \
  --batch
```

- Caution: the connector runs in batch mode and inserts 100 records by default per execute operation. To disable batch mode, set `-D sqoop.export.records.per.statement=1`.

Export block: update existing rows

```sh
sqoop export \
  --connect jdbc:Altibase://host:20300/mydb \
  --driver Altibase.jdbc.driver.AltibaseDriver \
  --username app_user \
  --password app_password \
  --connection-manager com.altibase.sqoop.manager.AltibaseManager \
  --table table_name \
  --export-dir hdfs_dir \
  --update-key key_column
```

Export block: update or insert

```sh
sqoop export \
  --connect jdbc:Altibase://host:20300/mydb \
  --driver Altibase.jdbc.driver.AltibaseDriver \
  --username app_user \
  --password app_password \
  --connection-manager com.altibase.sqoop.manager.AltibaseManager \
  --table table_name \
  --export-dir hdfs_dir \
  --update-key key_column \
  --update-mode allowinsert
```

- Caution: this uses the Altibase `MERGE` statement and requires Altibase 6.3.1 or later.

Export block: staging table

```sh
sqoop export \
  --connect jdbc:Altibase://host:20300/mydb \
  --driver Altibase.jdbc.driver.AltibaseDriver \
  --username app_user \
  --password app_password \
  --connection-manager com.altibase.sqoop.manager.AltibaseManager \
  --table table_name \
  --export-dir hdfs_dir \
  --update-key key_column \
  --staging-table staging_table_name
```

- Purpose: reduce partial-commit risk by first loading HDFS data into a staging table, then moving it to the target table.

List commands:

```sh
sqoop list-databases \
  --connect jdbc:Altibase://host:20300/mydb \
  --driver Altibase.jdbc.driver.AltibaseDriver \
  --username app_user \
  --password app_password \
  --connection-manager com.altibase.sqoop.manager.AltibaseManager

sqoop list-tables \
  --connect jdbc:Altibase://host:20300/mydb \
  --driver Altibase.jdbc.driver.AltibaseDriver \
  --username app_user \
  --password app_password \
  --connection-manager com.altibase.sqoop.manager.AltibaseManager
```

Hadoop Connector type block: `CHAR`

- Sqoop type: `String`.
- Import: yes.
- Export: yes.

Hadoop Connector type block: `VARCHAR`

- Sqoop type: `String`.
- Import: yes.
- Export: yes.

Hadoop Connector type block: `NCHAR`

- Sqoop type: `String`.
- Import: yes.
- Export: yes.

Hadoop Connector type block: `NVARCHAR`

- Sqoop type: `String`.
- Import: yes.
- Export: yes.

Hadoop Connector type block: `INTEGER`

- Sqoop type: `Integer`.
- Import: yes.
- Export: yes.

Hadoop Connector type block: `BIGINT`

- Sqoop type: `Long`.
- Import: yes.
- Export: yes.

Hadoop Connector type block: `SMALLINT`

- Sqoop type: `Integer`.
- Import: yes.
- Export: yes.

Hadoop Connector type block: `NUMBER`

- Sqoop type: `Double`.
- Import: yes.
- Export: yes.

Hadoop Connector type block: `NUMERIC`

- Sqoop type: `java.math.BigDecimal`.
- Import: yes.
- Export: yes.

Hadoop Connector type block: `DECIMAL`

- Sqoop type: `java.math.BigDecimal`.
- Import: yes.
- Export: yes.

Hadoop Connector type block: `FLOAT`

- Sqoop type: `Double`.
- Import: yes.
- Export: yes.

Hadoop Connector type block: `DOUBLE`

- Sqoop type: `Double`.
- Import: yes.
- Export: yes.

Hadoop Connector type block: `REAL`

- Sqoop type: `Float`.
- Import: yes.
- Export: yes.

Hadoop Connector type block: `DATE`

- Sqoop type: `java.sql.Timestamp`.
- Import: yes.
- Export: yes.

Hadoop Connector type block: `BLOB`

- Sqoop type: `com.cloudera.sqoop.lib.BlobRef`.
- Import: yes.
- Export: no.
- Notes: Sqoop supports `BLOB` only for import in the source baseline.

Hadoop Connector type block: `CLOB`

- Sqoop type: `com.cloudera.sqoop.lib.ClobRef`.
- Import: yes.
- Export: no.
- Notes: Sqoop supports `CLOB` only for import in the source baseline.

## Connector Block: DBeaver

Purpose: DBeaver is a GUI SQL client. The Altibase DBeaver package or DBeaver with the Altibase JDBC driver can connect to Altibase for SQL editing, object browsing, plan viewing, and data work.

When to Use:

- A user needs an interactive SQL client for Altibase.
- A user needs to browse Altibase objects, run SQL, view plans, inspect server output, or edit data from DBeaver.

Required Pieces:

- DBeaver 23.3.3 or later.
- Altibase Server 7.1.0 or later.
- Altibase JDBC driver.
- Driver class: `Altibase.jdbc.driver.AltibaseDriver`.
- JDBC URL: `jdbc:Altibase://host:port/database`.

Connection procedure:

1. Open `Database` > `New Database Connection`.
2. Select `Altibase` from `ALL` or `SQL`, then continue.
3. Enter connection fields:
   - `Host`: Altibase host name or IP address.
   - `Port`: Altibase service port, commonly `20300`.
   - `Database/Schema`: database name, commonly `mydb`.
   - `Username`: Altibase user.
   - `Password`: Altibase password.
4. If DBeaver can access the internet, let DBeaver download the Altibase JDBC driver in the driver settings window.
5. If offline or using a local driver, open `Driver Settings`, go to `Libraries`, choose `Add File`, select the Altibase JDBC driver, add it to the classpath, then apply the settings.
6. Finish the connection and double-click it in `Database Navigator`. A successful connection shows the connection as active.

DBeaver issue block: LOB data is not retrieved

- Cause: DBeaver uses `Auto-Commit` by default; Altibase LOB retrieval requires manual transaction handling.
- Fix for the current connection: use the transaction mode selector in the SQL toolbar and choose `Manual Commit`.
- Fix for a specific connection: open `Edit Connection` or press `F4`, go to `Connection settings` > `Initialization` > `Connection`, clear `Auto-commit`, save the connection, and reconnect.
- Fix for the global default: open `Window` > `Preferences` > `Connections` > `Connection Types`, clear `Auto-commit by default`, apply the setting, and reconnect.
- Caution: in `Manual Commit`, explicitly commit or roll back table modifications.

DBeaver issue block: `SYSTEM_` schema is not visible

- Cause: DBeaver does not show system objects by default.
- Fix: enable `Connection View` > `Show system objects`, then reconnect.

DBeaver issue block: DDL output is inaccurate

- Cause: DBeaver needs Altibase `DBMS_METADATA` support for accurate object DDL.
- Fix: connect as `SYS` and install the package scripts from `$ALTIBASE_HOME/packages`:

```sh
isql -f $ALTIBASE_HOME/packages/dbms_metadata.sql
isql -f $ALTIBASE_HOME/packages/dbms_metadata.plb
```

- Verification: reconnect in DBeaver and retrieve object DDL again.

DBeaver issue block: query execution plan location

- Procedure: open the connected database's `SQL Editor` > `New SQL script`, enter the query, and click `Explain Execution Plan`.
- Default: the Altibase DBeaver plugin uses `Explain Plan Only` by default.

DBeaver issue block: use `EXPLAIN_PLAN = ON`

- Procedure: open connection properties or the SQL script panel preferences, go to `Altibase settings`, enable `Datasource settings`, then choose `Explain Plan = ON`.

DBeaver issue block: PSM `PRINTLN` server output

- Procedure: open connection properties, go to `Altibase settings`, enable `Datasource settings`, and check `Enable DBMS Output`.
- Then open the SQL script window and click `Show server output`. Output appears in the output tab after executing SQL.

DBeaver issue block: Altibase `DATE` microseconds are not visible

- Cause: DBeaver timestamp display commonly shows milliseconds, while Altibase `DATE` can represent microseconds.
- Fix option 1: `Window` > `Preferences` > `Editors` > `Data Editor` > `Data Formats` > `Datasource settings`; set the timestamp value format to include six fractional second digits, for example `yyyy-MM-dd HH:mm:ss.SSSSSS`.
- Fix option 2: in the same data format settings, enable `Disable date/time formatting`.

DBeaver issue block: `"Invalid data type length"` when modifying `CHAR`

- Cause: DBeaver Data Editor can issue `INSERT`-style changes; values longer than the column size fail.
- Fix: check the modified value length before saving, especially for fixed-length character columns.

DBeaver issue block: show binary data as Hex

- Procedure: open connection properties, go to `Editors` > `Data Editor` > `Binary data`, set the binary data formatter to `Hex`, apply, and refresh the table view.

DBeaver issue block: binary data cannot be modified in Data Editor

- Fix: enter the binary value in the Data Editor `Value` field. Editing directly in the grid cell can convert the value unexpectedly.

DBeaver issue block: `BIT`, `VARBIT`, and `NIBBLE`

- DBeaver processes binary data by byte. Since `BIT`, `VARBIT`, and `NIBBLE` can be smaller than a byte, DBeaver handles them as numeric or character types.

DBeaver issue block: reset DBeaver settings and reinstall

- Purpose: remove old DBeaver workspace data before reinstalling or rebuilding a connection profile.
- Procedure: exit DBeaver, uninstall or replace the application as needed, then remove the DBeaver workspace directory for the operating system.
- Common workspace locations:
  - Windows: `%APPDATA%\DBeaverData`.
  - macOS: `~/Library/DBeaverData/`.
  - Linux: `$XDG_DATA_HOME/DBeaverData/`, or `~/.local/share/DBeaverData/` when `$XDG_DATA_HOME` is not set.
- Verification: after reinstalling, start DBeaver and confirm that old connection profiles and driver settings are no longer present.

DBeaver issue block: set SQL Editor auto-commit off by default

- Procedure: right-click the connection and choose `Edit Connection`, or select the connection and press `F4`.
- In the connection configuration, go to `Connection settings` > `Initialization` > `Connection`.
- Clear `Auto-commit`, save the connection, and reconnect before opening a new SQL editor.
- Temporary alternative: use the SQL editor transaction mode selector to switch the active editor session from `Auto-Commit` to `Manual Commit`.
- Verification: the SQL editor opens in manual transaction mode for that connection, and table changes require an explicit commit or rollback.

## Connector Block: Hibernate

Purpose: Hibernate needs an Altibase JDBC driver and `AltibaseDialect` so that Hibernate can generate Altibase-compatible SQL.

When to Use:

- Java ORM applications use Hibernate directly.
- Spring Data JPA applications use Hibernate as the JPA provider.

Required Pieces:

- Altibase JDBC driver.
- Driver class: `Altibase.jdbc.driver.AltibaseDriver`.
- JDBC URL: `jdbc:Altibase://host:port/database`.
- `AltibaseDialect` configured in Hibernate.

Hibernate 6.4 and later:

- `AltibaseDialect` is included in `hibernate-community-dialects`.
- Add a dependency similar to:

```xml
<dependency>
  <groupId>org.hibernate.orm</groupId>
  <artifactId>hibernate-community-dialects</artifactId>
  <version>6.4.1.Final</version>
</dependency>
```

- Spring Boot property example:

```properties
spring.datasource.driver-class-name=Altibase.jdbc.driver.AltibaseDriver
spring.datasource.url=jdbc:Altibase://localhost:20300/mydb
spring.datasource.username=sys
spring.datasource.password=manager
spring.jpa.properties.hibernate.jdbc.lob.non_contextual_creation=true
```

Altibase JDBC Maven examples from the Spring Hibernate 6.4 guide:

```xml
<!-- Altibase 7.3 example -->
<dependency>
  <groupId>com.altibase</groupId>
  <artifactId>altibase-jdbc</artifactId>
  <version>7.3.0.0.2</version>
</dependency>

<!-- Altibase 7.1 example -->
<dependency>
  <groupId>com.altibase</groupId>
  <artifactId>altibase-jdbc</artifactId>
  <version>7.1.0.9.2</version>
</dependency>
```

Hibernate before 6.4:

- The official Hibernate library does not include `AltibaseDialect.class`.
- Compile and port `AltibaseDialect.java`; include `AltibaseLimitHandler.java` where the target Hibernate version requires it.
- Configure Hibernate to use the resulting `AltibaseDialect.class`.

LOB cautions:

- `spring.jpa.properties.hibernate.jdbc.lob.non_contextual_creation=true` suppresses `java.sql.SQLFeatureNotSupportedException` that can occur when Hibernate checks `Connection.createNClob()`. Altibase does not support `NClob`; the check can be safely avoided this way.
- With the Altibase 7.1 JDBC driver, add `lob_null_select=off` when Hibernate LOB features are used:

```text
jdbc:Altibase://127.0.0.1:20300/mydb?lob_null_select=off
```

- Starting with Altibase 7.3, `lob_null_select` defaults to `off`.

Verification:

- Confirm the application starts without Hibernate dialect resolution errors.
- Confirm Hibernate logs show the expected Hibernate ORM version.
- Execute a simple entity DDL or query and confirm generated SQL succeeds on Altibase.

## Connector Block: OpenLDAP `back-sql`

Purpose: OpenLDAP `back-sql` can use Altibase as an RDBMS backend repository through ODBC.

When to Use:

- LDAP entries should be backed by relational tables in Altibase.
- The integration uses OpenLDAP SQL Backend, also called `back-sql`.

Required Pieces:

- OpenLDAP built with SQL backend support.
- Altibase 6.5.1 or later is recommended by the source guide.
- Altibase ODBC driver.
- ODBC DSN configuration.
- Altibase metadata tables that map LDAP `objectClass` and `attributeType` definitions to SQL tables and columns.

OpenLDAP architecture:

```mermaid
flowchart LR
  C[LDAP client] --> S[OpenLDAP slapd]
  S --> B[back-sql]
  B --> O[ODBC DSN]
  O --> A[Altibase]
  A --> M[ldap_oc_mappings and related metadata]
  A --> D[Application data tables]
```

OpenLDAP build procedure:

```sh
tar xvfz openldap_package.tgz
./configure --prefix=<openldap_home> --enable-sql
make depend
make
make install
```

ODBC DSN example:

```ini
[ldap_altibase]
Description = ODBC for Altibase
Driver = $ALTIBASE_HOME/lib/libaltibase_odbc-64bit-ul64.so
server = 127.0.0.1
port = 20030
```

ODBC trace example:

```ini
[ODBC]
TraceFile = $ALTIBASE_HOME/trc/odbc.log
Trace = Yes
```

`slapd.conf` SQL backend essentials:

```text
database        sql
suffix          "dc=example,dc=com"
rootdn          "cn=Manager,dc=example,dc=com"
rootpw          secret
dbname          ldap_altibase
dbuser          ldap
dbpasswd        ldap
subtree_cond    "upper(ldap_entries.dn) LIKE CONCAT('%',upper(?))"
insentry_stmt   "insert into ldap_entries (id,dn,oc_map_id,parent,keyval) values (ldap_entry_ids.nextval,?,?,?,?)"
has_ldapinfo_dn_ru  no
upper_func      UPPER
```

Metadata table block: `ldap_oc_mappings`

- Purpose: maps LDAP structural `objectClass` values to Altibase tables.
- Key columns: `ID`, `NAME`, `KEYTBL`, `KEYCOL`, `CREATE_PROC`, `CREATE_KEYVAL`, `DELETE_PROC`, `EXPECT_RETURN`.
- `NAME` must match an `objectClass` loaded in the OpenLDAP schema.
- `KEYTBL` is the table mapped to the object class.
- `KEYCOL` is the primary key column of `KEYTBL`.
- `CREATE_PROC` and `DELETE_PROC` define SQL actions used when adding or deleting entries.
- If a procedure returns a value, the output binding parameter should be placed first.

Metadata table block: `ldap_attr_mappings`

- Purpose: maps LDAP `attributeType` values to SQL expressions, tables, joins, and procedures.
- Key columns: `ID`, `OC_MAP_ID`, `NAME`, `SEL_EXPR`, `FROM_TBLS`, `JOIN_WHERE`, `ADD_PROC`, `DELETE_PROC`, `PARAM_ORDER`, `EXPECT_RETURN`.
- `OC_MAP_ID` references `ldap_oc_mappings.ID`.
- `NAME` must match an `attributeType` loaded in the OpenLDAP schema.
- `SEL_EXPR`, `FROM_TBLS`, and `JOIN_WHERE` define how the attribute is selected.
- `ADD_PROC` and `DELETE_PROC` define how attribute values are inserted or deleted.
- `PARAM_ORDER` controls whether the mapped table key value appears before or after the attribute value in procedure parameters.

Metadata table block: `ldap_entries`

- Purpose: stores the LDAP distinguished name for each entry.
- Key columns: `ID`, `DN`, `OC_MAP_ID`, `PARENT`, `KEYVAL`.
- `OC_MAP_ID` references the object-class mapping.
- `PARENT` points to the parent entry; the suffix entry has `0`.
- `KEYVAL` stores the primary key value of the mapped data row.

Metadata table block: `ldap_entry_objclasses`

- Purpose: stores auxiliary object classes for an LDAP entry.
- Key columns: `ENTRY_ID`, `NAME`.
- `ENTRY_ID` references `ldap_entries.ID`.
- `NAME` must match an auxiliary `objectClass` loaded in the OpenLDAP schema.

OpenLDAP setup checklist:

1. Create an Altibase user for LDAP metadata and data.
2. Create the OpenLDAP metadata tables.
3. Create application tables for the LDAP object classes.
4. Insert rows into `ldap_oc_mappings`, `ldap_attr_mappings`, `ldap_entries`, and `ldap_entry_objclasses`.
5. Configure `.odbc.ini`, `.odbcinst.ini`, and `slapd.conf`.
6. Start OpenLDAP and test LDAP operations.

Example user creation:

```sql
CREATE USER ldap IDENTIFIED BY '<password>';
```

Do not include `DROP USER ... CASCADE` in production setup examples. If a lab reset is required, document the destructive impact, backup requirement, and explicit operator approval outside the copy-ready setup path.

Example data-build commands:

```sh
isql -s localhost -u ldap -p ldap -f backsql_create.sql
isql -s localhost -u ldap -p ldap -f testdb_create.sql
isql -s localhost -u ldap -p ldap -f testdb_metadata.sql
isql -s localhost -u ldap -p ldap -f testdb_data.sql
```

Cautions:

- OpenLDAP `back-sql` depends on the ODBC DSN, driver bitness, library path, and Altibase user privileges.
- `slapd.conf` should not be world-readable because it can include credentials.
- Mapping values must match OpenLDAP schema names exactly.
- Validate stored procedures used in mapping tables independently in Altibase before debugging LDAP operations.

Verification:

- Confirm the ODBC DSN connects to Altibase.
- Confirm the LDAP metadata tables contain mappings for the expected `objectClass` and `attributeType` values.
- Confirm `slapd` starts without SQL backend errors.
- Run LDAP search/add/delete operations and verify corresponding Altibase table rows change as expected.

## Troubleshooting Checklist

DB Link failures:

- Check `DBLINK_ENABLE=1` in `altibase.properties`.
- Check `ALTILINKER_ENABLE=1` and `ALTILINKER_PORT_NO` in `dblink.conf`.
- Confirm `AltiLinker` is running with `V$DBLINK_ALTILINKER_STATUS`.
- Confirm the remote JDBC driver exists and matches the remote DBMS and Java runtime.
- Confirm `TARGETS/NAME`, `TARGETS/JDBC_DRIVER`, `TARGETS/CONNECTION_URL`, `TARGETS/USER`, and `TARGETS/PASSWORD`.
- Confirm the database link object exists in `V$DBLINK_DATABASE_LINK_INFO`.
- Check `ALTILINKER_TRACE_LOG_DIR` and `ALTILINKER_TRACE_LOGGING_LEVEL` for trace output.
- For transaction issues, check `DBLINK_GLOBAL_TRANSACTION_LEVEL` and the remote DBMS autocommit/XA capability.

Hadoop Connector failures:

- Confirm `$ALTIBASE_HOME/lib/Altibase.jar` is in `$SQOOP_HOME/lib`.
- Confirm `altibase_sqoop14_connector.jar` is in `$SQOOP_HOME/lib`.
- Confirm the command includes `--connection-manager com.altibase.sqoop.manager.AltibaseManager`.
- Confirm the JDBC URL, driver class, user, and password.
- For export failures, verify target table structure, delimiter handling, batch settings, and whether the data type is export-supported.
- For `BLOB` and `CLOB`, remember that the source baseline supports import only.

DBeaver failures:

- Confirm DBeaver version is 23.3.3 or later.
- Confirm the driver class is `Altibase.jdbc.driver.AltibaseDriver`.
- Confirm the URL is `jdbc:Altibase://host:port/database`.
- For LOB retrieval, use `Manual Commit`.
- For hidden system objects, enable `Show system objects`.
- For inaccurate DDL, install `DBMS_METADATA`.
- For DATE microseconds, adjust data format settings.

Hibernate failures:

- Confirm `AltibaseDialect` is available through `hibernate-community-dialects` for Hibernate 6.4 or manually ported for older Hibernate.
- Confirm the Altibase JDBC driver dependency or local JAR matches the Altibase server version.
- For Altibase 7.1 LOB behavior, add `lob_null_select=off`.
- Add `spring.jpa.properties.hibernate.jdbc.lob.non_contextual_creation=true` when Hibernate checks unsupported `NClob` creation.

OpenLDAP failures:

- Confirm OpenLDAP was built with `--enable-sql`.
- Confirm the Altibase ODBC driver and DSN work before testing LDAP.
- Confirm `dbname` in `slapd.conf` matches the ODBC DSN.
- Confirm `dbuser` and `dbpasswd` are valid Altibase credentials.
- Confirm mapping metadata uses schema names loaded in OpenLDAP.
- Enable ODBC trace only while diagnosing; turn it off when done.
