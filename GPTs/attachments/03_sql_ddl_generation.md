# 03. SQL DDL Generation

## Applicable Versions

- 7.1: Based on Altibase 7.1 SQL Reference.
- 7.3: Based on Altibase 7.3 SQL Reference.
- 8.1: Based on Altibase 8.1 verified source SQL Reference and Altibase 8.1 Release Notes.

## Questions This File Can Answer

- Generate memory or disk tablespace DDL and table DDL.
- Convert Oracle DDL to Altibase DDL.
- Generate SQL to create users, privileges, sequences, and indexes.
- Generate SQL to create and start replication objects.
- Generate SQL to check property values or performance views.

## Source Documents

- 7.1: Altibase 7.1 SQL Reference; General Reference 1.
- 7.3: Altibase 7.3 SQL Reference; General Reference 1.
- 8.1: Altibase 8.1 verified source SQL Reference; General Reference 1; Altibase 8.1 Release Notes.

## Core Guidance

- If the customer specifies a version, generate SQL for that version.
- If the customer does not specify a version, generate SQL from the 8.1 baseline and state that some features, such as JSON, Temporary LOB, and replication SSL, might not exist in 7.1 or 7.3.
- Do not over-explain DML or basic `SELECT` syntax that is identical or nearly identical to Oracle.
- Prioritize Altibase-specific DDL, tablespaces, memory and disk storage structure, replication, and property check SQL.

## Oracle Compatibility Baseline

- Basic `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `JOIN`, `WHERE`, `GROUP BY`, and `ORDER BY` are generally Oracle-compatible areas.
- For `CREATE TABLE`, `TABLESPACE`, `MAXROWS`, `QUEUE`, `REPLICATION`, memory or disk tablespaces, and LOB storage location, prioritize Altibase syntax because Altibase differences matter.
- For Oracle DDL conversion requests, do not claim that the Oracle syntax can be run unchanged.

## DDL Writing Patterns

### Tablespaces

Example Questions:

- Create a disk tablespace and then create a table on it.
- Create a memory tablespace with auto extension.

Oracle Compatibility:

- Oracle's tablespace concept and purpose are similar, but Altibase requires attention to memory, disk, volatile, and temporary tablespace distinctions.

Example:

```sql
CREATE DISK TABLESPACE disk_tbs_01
DATAFILE '/data/altibase/disk_tbs_01.dbf';

CREATE MEMORY TABLESPACE mem_tbs_01
SIZE 32M
AUTOEXTEND ON;

ALTER TABLESPACE mem_tbs_01
ALTER AUTOEXTEND ON NEXT 256M MAXSIZE 1G;
```

Check SQL:

```sql
SELECT * FROM V$TABLESPACES;
SELECT * FROM V$MEM_TABLESPACES;
```

### Tables

Example Questions:

- Generate DDL for a memory table.
- Generate a disk table with a LOB column.

Oracle Compatibility:

- Column definitions, constraints, and basic DDL structure are similar to Oracle.
- Storage location, memory or disk tablespaces, LOB storage location, and clauses such as `MAXROWS` must be checked against Altibase syntax.

Example:

```sql
CREATE TABLE app_user (
    user_id     INTEGER NOT NULL,
    user_name   VARCHAR(80) NOT NULL,
    created_at  DATE DEFAULT SYSDATE,
    CONSTRAINT pk_app_user PRIMARY KEY (user_id)
) TABLESPACE mem_tbs_01;

CREATE TABLE app_document (
    doc_id      INTEGER NOT NULL,
    title       VARCHAR(200),
    body        CLOB,
    CONSTRAINT pk_app_document PRIMARY KEY (doc_id)
) TABLESPACE disk_tbs_01;
```

8.1 JSON Example:

```sql
CREATE TABLE app_event (
    event_id    INTEGER NOT NULL,
    payload     JSON,
    created_at  DATE DEFAULT SYSDATE,
    CONSTRAINT pk_app_event PRIMARY KEY (event_id)
) TABLESPACE disk_tbs_01;
```

### Indexes

Example Questions:

- Add an index to a specific column.
- Specify an index tablespace.

Example:

```sql
CREATE INDEX idx_app_user_name
ON app_user (user_name)
TABLESPACE mem_tbs_01;
```

Check SQL:

```sql
SELECT * FROM SYSTEM_.SYS_INDICES_;
```

### Users and Privileges

Example Questions:

- Create an application user and assign a default tablespace.
- Grant query and insert privileges on a specific table.

Example:

```sql
CREATE USER app IDENTIFIED BY app_password
DEFAULT TABLESPACE mem_tbs_01;

GRANT CREATE SESSION TO app;
GRANT SELECT, INSERT, UPDATE, DELETE ON sys.app_user TO app;
```

Cautions:

- In production, apply password policy and least privilege.
- Adjust object owners and schema names for the customer's environment.

### Sequences

Example Question:

- Create a sequence for a primary key.

Example:

```sql
CREATE SEQUENCE seq_app_user
START WITH 1
INCREMENT BY 1;
```

### Replication

Example Questions:

- Generate SQL for table replication between two servers.
- Generate an SSL replication example for 8.1.

General Example:

```sql
CREATE REPLICATION rep_app
WITH '192.168.10.12', 35524
FROM app.app_user TO app.app_user;

ALTER REPLICATION rep_app START;
```

8.1 SSL Example:

```sql
CREATE REPLICATION rep_app_ssl
WITH '192.168.10.12', 45524 USING SSL
FROM app.app_user TO app.app_user;
```

Cautions:

- For bidirectional or Active-Standby configurations, create the corresponding replication object on the peer server as well.
- Treat SSL replication as an 8.1 baseline feature, and tell 7.1 or 7.3 customers to verify availability for their version.

### Properties and Check SQL

Example Questions:

- Show SQL to check current property values.
- Show SQL to check session and performance status.

Example:

```sql
SELECT * FROM V$PROPERTY
WHERE NAME IN ('LOG_FILE_SIZE', 'REPLICATION_SSL_PORT_NO');

SELECT * FROM V$SESSION;
SELECT * FROM V$STATEMENT;
```

Cautions:

- Performance view names and columns can differ by version.
- Use `06_data_dictionary_performance_views.md` for exact column descriptions.

## Version Differences

- 7.1: Generate syntax that exists in the 7.1 SQL Reference and avoid 8.1-only JSON, Temporary LOB, and replication SSL features.
- 7.3: Use 7.3 SQL Reference behavior when the customer names 7.3, including 7.3-specific SQL, Spatial, or Replication improvements.
- 8.1: Use Altibase 8.1 verified source for JSON, Temporary LOB, replication SSL, and JSON plan related DDL or checks.

## Conversion TODO

- Reorganize all SQL Reference `CREATE`, `ALTER`, and `DROP` families in this format.
- Fill in item-level differences across 7.1, 7.3, and 8.1.
- Convert syntax images or diagrams to BNF-like text or Mermaid.
- Review example SQL with a 20-question representative sample.
