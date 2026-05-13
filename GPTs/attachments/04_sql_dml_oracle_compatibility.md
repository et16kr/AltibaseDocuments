# 04. SQL DML and Oracle Compatibility

## Applicable Versions

- 7.1: Based on Altibase 7.1 SQL Reference.
- 7.3: Based on Altibase 7.3 SQL Reference.
- 8.1: Based on Altibase 8.1 verified source SQL Reference.

## Questions This File Can Answer

- How much Oracle SQL can be used unchanged in Altibase?
- What cautions apply when writing `SELECT`, `INSERT`, `UPDATE`, and `DELETE`?
- What are the differences between Oracle functions and Altibase functions?
- How should 8.1 JSON functions be used?

## Source Documents

- 7.1: Altibase 7.1 SQL Reference.
- 7.3: Altibase 7.3 SQL Reference.
- 8.1: Altibase 8.1 verified source SQL Reference.

## Core Guidance

- Explain that ordinary DML is similar to Oracle, but always check Altibase data types, functions, and restrictions.
- Even when a SQL generation request only needs DML, confirm whether the table is memory or disk based and whether LOB or JSON is used.
- Treat JSON functions as 8.1 baseline features.

## Answer Guidelines

- Oracle-compatible areas: basic `SELECT`, `JOIN`, `INSERT`, `UPDATE`, `DELETE`, `GROUP BY`, and `ORDER BY`.
- Areas requiring Altibase checks: data type conversion, date and character functions, regular expressions, LOB, JSON, hints, hierarchical queries, and analytic functions.

## Version Differences

- 7.1: Treat ordinary DML as the stable baseline and verify functions or limits against the 7.1 SQL Reference.
- 7.3: Note 7.3 SQL improvements when they affect Oracle compatibility or function behavior.
- 8.1: Treat JSON functions and JSON data handling as Altibase 8.1 verified source features.

## Conversion TODO

- Compress syntax that is similar to Oracle into one-line guidance plus one example.
- Expand only Altibase-specific functions or functions with meaningful differences.
- Organize 8.1 JSON functions around `JSON_ARRAY`, `JSON_OBJECT`, `JSON_EXISTS`, `JSON_QUERY`, `JSON_VALUE`, and `JSON_VALID`.
