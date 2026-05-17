# J017 Java Connectors Migration Spatial Design Note

Date: 2026-05-17
Job: J017 - Java connectors migration spatial and integration blocks

## Scope

J017 strengthens customer-facing attachment coverage for:

- `GPTs/attachments/11_java_jdbc_spring.md`
- `GPTs/attachments/15_migration_oracle_compatibility.md`
- `GPTs/attachments/16_dblink_external_connectors.md`
- `GPTs/attachments/17_kubernetes_aku_cloud.md`
- `GPTs/attachments/19_spatial_nifi_tableau_misc.md`

The job is limited to JDBC, Java runtime boundaries, Spring, Hibernate, DB Link,
Hadoop Connector, Kubernetes, AKU, Migration Center, Adapter for Oracle, Spatial,
`altiShapeLoader`, NiFi, Tableau, and adjacent third-party connector guidance.

## Source Basis

The remediation uses repository-local selected sources only, with Korean manuals as the
source of truth where paired English and Korean sources differ:

- Korean JDBC manuals for `fetch_enough`, `time_zone`, `alternateservers`,
  `ssl_enable`, `stmt_cache_enable`, `setPoolable`, unsupported JDBC 4.x APIs, and
  Java runtime boundaries.
- Korean Spring/Hibernate guides for Maven Central availability, `com.altibase`,
  `altibase-jdbc`, `Altibase.jdbc.driver.AltibaseDriver`, and Hibernate 6.4
  configuration.
- Korean Migration Center and Adapter for Oracle manuals for `Prepare`, Migration
  Center `7.19` source/target scope, `Primary Key`, `Write to CSV`, FILESYNC, and
  `Altibase Log Analysis API` plus OCI usage.
- Korean DB Link and Hadoop Connector manuals for `REMOTE_TABLE`,
  `REMOTE_EXECUTE_IMMEDIATE`, `parameter marker`, `binding`, `sqoop import`,
  `sqoop export`, `altibase_sqoop14_connector.jar`, and `BLOB`/`CLOB` direction
  limits.
- Korean Utilities and AKU/Kubernetes guides for `AKU_SERVER_COUNT`,
  `OrderedReady`, `startupProbe`, `/tmp/aku_start_completed`,
  `publishNotReadyAddresses: true`, `terminationGracePeriodSeconds`, and abnormal
  `aku -p end` cleanup cautions.
- Korean Spatial SQL, `altiShapeLoader`, NiFi, and Tableau guides for `GEOMETRY`
  precision, `100MBytes`, `SPATIAL_REF_SYS`, `SYS_SPATIAL.ADD_SPATIAL_REF_SYS`,
  `JAVA_HOME`, `NiFi 1.12.1`, `Altibase42.jar`,
  `TableauDesktop-64bit-2021-4-4`, and `C:\Program Files\Tableau\Drivers`.

## Documentation Shape

The attachment boundaries and major section order remain unchanged. J017 adds compact
exact-answer blocks near the top of each scoped attachment so lexical retrieval can
surface the required literal tokens and safety caveats before the model compresses the
answer.

The existing detailed cookbooks remain the broader reference. The new blocks duplicate
only high-value, source-backed tokens and caveats that the benchmark evidence showed
were easy to omit during answer synthesis.

## Safety Rules Preserved

- Ask for exact Altibase version, driver or tool patch, Java version, connector product
  version, host/port, character set, SRID, failover topology, storage design, and
  rollback plan before production commands.
- Do not infer generic Oracle, JDBC, Sqoop, Kubernetes, Spatial, NiFi, or Tableau
  behavior where an Altibase source gives a narrower rule.
- Treat `oraAdapter`, DB Link pass-through, AKU shutdown/reset, shapefile import, data
  validation FILESYNC, and connector credential handling as operational workflows that
  require environment-specific evidence before destructive or state-changing actions.
