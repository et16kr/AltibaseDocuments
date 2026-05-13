# 07. Error Messages and Troubleshooting

## Applicable Versions

- 7.1: Based on Altibase 7.1 Error Message Reference.
- 7.3: Based on Altibase 7.3 Error Message Reference.
- 8.1: Based on Altibase 8.1 verified source Error Message Reference.

## Questions This File Can Answer

- What are the cause and action for a specific Altibase error code?
- What should be checked when a SQL execution error occurs?
- How should JSON, LOB, replication, or regular expression errors be handled?

## Source Documents

- 7.1: Altibase 7.1 Error Message Reference.
- 7.3: Altibase 7.3 Error Message Reference.
- 8.1: Altibase 8.1 verified source Error Message Reference.

## Core Guidance

- Error answers should follow `Symptom -> Cause -> Action -> Check SQL or Command -> Related Document`.
- Mark 8.1 JSON-related errors as 8.1-specific.

## Version Differences

- 7.1: Use 7.1 error messages and actions when the customer reports a 7.1 system.
- 7.3: Check 7.3 error wording and actions before reusing 7.1 guidance.
- 8.1: Use Altibase 8.1 verified source for JSON, Temporary LOB, replication SSL, and other 8.1-specific errors.

## Conversion Format

```text
Error Code:
Symptom:
Primary Causes:
Action:
Check SQL or Command:
Version Cautions:
```

## Conversion TODO

- Reclassify error lists not only by code order but also by topic.
- Convert frequently asked SQL, DDL, replication, and connection errors first.
