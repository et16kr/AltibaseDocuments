# 11. Java, JDBC, and Spring

## Applicable Versions

- 7.1: Based on Altibase 7.1 JDBC guidance.
- 7.3: Based on Altibase 7.3 JDBC guidance and JDBC 4.2 improvements.
- 8.1: Based on Altibase 8.1 verified source JDBC guidance and Java compatibility.

## Questions This File Can Answer

- Generate a JDBC connection string.
- What is the Java version compatibility?
- How is Altibase connected from Spring Data JPA or Hibernate?
- What cautions apply to JDBC LOB or JSON handling?

## Source Documents

- 7.1: Altibase 7.1 JDBC User's Manual; Adapter for JDBC User's Manual.
- 7.3: Altibase 7.3 JDBC User's Manual; Adapter for JDBC User's Manual.
- 8.1: Altibase 8.1 verified source JDBC User's Manual; Adapter for JDBC User's Manual; Java Compatibility.
- Common external guides: Spring Data JPA User's Guide for Altibase; Spring Data JPA with Hibernate 6.4 User's Guide for Altibase.

## Core Guidance

- Java answers should cover the driver file, JDBC URL, account and privileges, charset, and failover options together.
- For Spring or Hibernate questions, prioritize dialect, datasource, and transaction settings.

## Version Differences

- 7.1: Use 7.1 JDBC driver and Java compatibility guidance for 7.1 applications.
- 7.3: Include 7.3 JDBC 4.2 and driver behavior when it affects application setup.
- 8.1: Use Altibase 8.1 verified source for JDBC, Java compatibility, JSON, and LOB guidance.

## Conversion TODO

- Organize connection string and Spring configuration examples by version.
- Convert Java Compatibility material from a version matrix into explanatory lists.
- Add details for 8.1 JSON and LOB JDBC cautions.
