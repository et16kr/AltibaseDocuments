# 06. Data Dictionary and Performance Views

## Applicable Versions

- 7.1: Based on Altibase 7.1 General Reference 2.
- 7.3: Based on Altibase 7.3 General Reference 2.
- 8.1: Based on Altibase 8.1 verified source General Reference 2 and Altibase 8.1 Release Notes.

## Questions This File Can Answer

- Show SQL for querying table, index, user, and privilege information.
- How can session, statement, and replication status be checked in performance views?
- What SQL checks a specific property or metadata item?
- Which performance views were added in 8.1?

## Source Documents

- 7.1: Altibase 7.1 General Reference 2.
- 7.3: Altibase 7.3 General Reference 2.
- 8.1: Altibase 8.1 verified source General Reference 2; Altibase 8.1 Release Notes.

## Core Guidance

- Do not keep large tables as-is. For each object, provide `Purpose`, `Key Columns`, and `Representative Query SQL`.
- If the customer gives an object name, also generate SQL to query metadata or performance views for that object.

## Version Differences

- 7.1: Use 7.1 dictionary and performance view names and columns for 7.1 answers.
- 7.3: Record 7.3 view or column changes where they affect check SQL.
- 8.1: Use Altibase 8.1 verified source and release notes for new or changed performance views.

## Representative Check SQL Patterns

```sql
SELECT * FROM SYSTEM_.SYS_TABLES_;
SELECT * FROM SYSTEM_.SYS_INDICES_;
SELECT * FROM V$SESSION;
SELECT * FROM V$STATEMENT;
SELECT * FROM V$PROPERTY;
```

## Conversion TODO

- Reclassify meta tables and performance views by topic.
- Cross-check new 8.1 performance views against the release notes.
- Build a cookbook of frequently used check SQL.
