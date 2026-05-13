# 15. Migration and Oracle Compatibility

## Applicable Versions

- 7.1: Based on Altibase 7.1 migration-related documents.
- 7.3: Based on Altibase 7.3 Migration Center and Oracle Adapter guidance.
- 8.1: Based on Altibase 8.1 verified source and the latest Migration Center release guidance.

## Questions This File Can Answer

- How should DDL be changed when moving from Oracle to Altibase?
- What is the Migration Center usage procedure?
- When is Oracle Adapter used?
- How should pre-migration and post-migration verification be performed?

## Source Documents

- 7.1: Altibase 7.1 Adapter for Oracle User's Manual.
- 7.3: Migration Center User's Manual; Altibase 7.3 Adapter for Oracle User's Manual.
- 8.1: Altibase 8.1 verified source Migration Center User's Manual; Adapter for Oracle User's Manual; Migration Center Release Notes.

## Core Guidance

- Answer Oracle compatibility by separating `Can Use As-Is`, `Needs Modification`, and `Needs Alternative Design`.
- For DDL conversion, refer first to `03_sql_ddl_generation.md`.

## Version Differences

- 7.1: Use 7.1 Adapter for Oracle guidance when the source or target environment includes 7.1.
- 7.3: Use 7.3 Migration Center and Adapter for Oracle guidance for 7.3 migrations.
- 8.1: Use Altibase 8.1 verified source and current Migration Center guidance for 8.1 migration answers.

## Conversion TODO

- Organize Migration Center procedures as ordered steps.
- Link Oracle data type and DDL differences to the SQL generation document.
- Treat 7.x version mentions in tool release notes as tool versions only.
