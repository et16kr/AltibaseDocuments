# 05. Data Types and Properties

## Applicable Versions

- 7.1: Based on Altibase 7.1 General Reference 1.
- 7.3: Based on Altibase 7.3 General Reference 1.
- 8.1: Based on Altibase 8.1 verified source General Reference 1 and Altibase 8.1 Release Notes.

## Questions This File Can Answer

- What are the differences between Altibase data types and Oracle data types?
- Where are server properties checked and how are they configured?
- What are the 8.1 JSON data type and Temporary LOB?
- What do properties such as `LOG_FILE_SIZE` and `REPLICATION_SSL_PORT_NO` mean?

## Source Documents

- 7.1: Altibase 7.1 General Reference 1.
- 7.3: Altibase 7.3 General Reference 1.
- 8.1: Altibase 8.1 verified source General Reference 1; Altibase 8.1 Release Notes.

## Core Guidance

- For data type answers, first identify the version, storage target, and SQL generation purpose.
- Explain 8.1 separately as the baseline where the native JSON data type and JSON functions were added.
- Decompose properties into `Meaning`, `Default`, `Dynamic Change Support`, and `Related Performance View or Check SQL`.

## Version Differences

- 7.1: Use 7.1 data type and property definitions when the customer targets 7.1.
- 7.3: Capture 7.3 property or data type changes separately from the 7.1 baseline.
- 8.1: Use Altibase 8.1 verified source for native JSON, Temporary LOB, and new, changed, or removed properties.

## Conversion TODO

- Decompose data type tables into per-type explanation blocks.
- Decompose property tables into per-property explanation blocks.
- Cross-check 8.1 new, changed, and removed properties against the release notes.
