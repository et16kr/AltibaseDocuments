# 00. Versions, Releases, and Supported Platforms

## Applicable Versions

- 7.1: Based on Altibase 7.1 releases and manuals.
- 7.3: Based on Altibase 7.3 releases and manuals.
- 8.1: Based on Altibase 8.1 release notes and Altibase 8.1 verified source.

## Questions This File Can Answer

- What are the major differences between Altibase 7.3 and 8.1?
- What are the JSON, Temporary LOB, and replication SSL features added in 8.1?
- Is the current OS supported for an Altibase server or client?
- What database and metadata compatibility cautions apply during an 8.1 upgrade?

## Source Documents

- 7.1: Altibase 7.1 Release Notes; Supported Platforms.
- 7.3: Altibase 7.3 Release Notes; Supported Platforms.
- 8.1: Altibase 8.1 Release Notes; Supported Platforms; Altibase 8.1 verified source.

## Core Guidance

- For version questions, identify the customer's target version first.
- If the customer does not specify a version, answer from the 8.1 baseline and state that 7.1 or 7.3 behavior can differ.
- Do not leave platform tables as raw tables. Rewrite them as OS, CPU, server support, client support, and required software items.

## Version Differences

- 7.1: Preserve features and limits relevant to established stable customers.
- 7.3: Summarize AKU, JDBC 4.2, OpenSSL 3.0.8, and SQL, Spatial, and Replication improvements separately.
- 8.1: Summarize the JSON data type, Temporary LOB, KADA, Kafka connector, ABM, replication SSL, JSON plan, and property or performance view changes separately.

## Conversion TODO

- Decompose release note tables into sentence-style item lists.
- Reorganize upgrade compatibility cautions into `Risk`, `Required Action`, and `Check SQL`.
- Align 7.1, 7.3, and 8.1 supported platform guidance in one document without conflicts.
