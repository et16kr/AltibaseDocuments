# 12. C, CLI, ODBC, Precompiler

## Applicable Versions

- 7.1: Based on Altibase 7.1 C, CLI, ODBC, and Precompiler manuals.
- 7.3: Based on Altibase 7.3 C, CLI, ODBC, and Precompiler manuals.
- 8.1: Based on Altibase 8.1 verified source C, CLI, ODBC, and Precompiler manuals.

## Questions This File Can Answer

- What is the basic CLI API call order?
- How is an ODBC connection string written?
- What is the difference between C Interface and Precompiler?
- What cautions apply when using CLI functions related to LOB or JSON?

## Source Documents

- 7.1: Altibase 7.1 CLI User's Manual; ODBC User's Manual; Altibase C Interface Manual; Precompiler User's Manual.
- 7.3: Altibase 7.3 CLI User's Manual; ODBC User's Manual; Altibase C Interface Manual; Precompiler User's Manual.
- 8.1: Altibase 8.1 verified source CLI User's Manual; ODBC User's Manual; Altibase C Interface Manual; Precompiler User's Manual.

## Core Guidance

- Decompose API tables into per-function explanation blocks.
- Build cookbook entries for connection strings, handle allocation and release, transaction handling, and LOB handling order.

## Version Differences

- 7.1: Use 7.1 C, CLI, ODBC, and Precompiler APIs for 7.1 answers.
- 7.3: Capture 7.3 API, connection, or precompiler changes separately.
- 8.1: Use Altibase 8.1 verified source for JSON and LOB-related CLI guidance.

## Conversion TODO

- Reclassify CLI API lists into `Connection`, `Execution`, `Fetch`, `LOB`, and `Error Handling`.
- Add details for 8.1 JSON-related LOB locator functions.
