# Java And JDBC Playbook

- Playbook ID: `APB-000010`
- Owning job: `S2-J004`
- Validation status: `pass`
- Supported versions: Altibase 7.1, Altibase 7.3, and `Altibase 8.1 verified source`
- Protected topic: no

## Source Routes

Use this playbook for source-backed Java application connectivity, JDBC URLs,
JDBC driver selection, Spring, Hibernate, Adapter for JDBC routes, connection
configuration, connection checks, and first diagnostics. It can draft guarded
customer artifacts, but it does not replace exact source-pack checks,
installed JAR inspection, framework documentation, or live connection tests.

| Route | Source IDs | Source-pack block refs | Baseline blocks |
| --- | --- | --- | --- |
| JDBC and Adapter for JDBC manuals | `SRC-000047`, `SRC-000016`, `SRC-000061`, `SRC-000030`, `SRC-000111`, `SRC-000080`, `SRC-000125`, `SRC-000094`, `SRC-000171`, `SRC-000141`, `SRC-000185`, `SRC-000155` | `SRC-000047/BLOCK-000552`, `SRC-000016/BLOCK-000550`, `SRC-000061/BLOCK-000553`, `SRC-000030/BLOCK-000551`, `SRC-000111/BLOCK-000556`, `SRC-000080/BLOCK-000554`, `SRC-000125/BLOCK-000557`, `SRC-000094/BLOCK-000555`, `SRC-000171/BLOCK-000560`, `SRC-000141/BLOCK-000558`, `SRC-000185/BLOCK-000561`, `SRC-000155/BLOCK-000559` | `KAE-BLOCK-000016`, `KAE-BLOCK-000017`, `KAE-BLOCK-000151`, `KAE-BLOCK-000152`, `KAE-BLOCK-000207`, `KAE-BLOCK-000208`, `KAE-BLOCK-000274` |
| Java compatibility, Spring Data JPA, and Hibernate 6.4 guides | `SRC-000473`, `SRC-000012`, `SRC-000005`, `SRC-000013`, `SRC-000006` | `SRC-000473/BLOCK-000562`, `SRC-000012/BLOCK-000923`, `SRC-000005/BLOCK-000916`, `SRC-000013/BLOCK-000924`, `SRC-000006/BLOCK-000917` | `KAE-BLOCK-000231`, `KAE-BLOCK-000247`, `KAE-BLOCK-000248`, `KAE-BLOCK-000274` |
| AID source-backed development and framework reference routes | `AID-SRC-000434`, `AID-SRC-000435` | `BLOCK-000444`, `BLOCK-000445` | `KAE-BLOCK-000276` |

Guardrails: `CONF-000006` and `CONF-000007` remain open. Use this playbook
for guarded first drafts. Recheck exact source-pack blocks, delivered JARs,
Java compatibility tables, framework versions, JDBC trace behavior, failover
topology, TLS material, and live runtime output before treating an artifact as
complete or production-ready.

Forbidden assumption note: do not infer JDBC URL properties, Spring pool
properties, Hibernate dialect behavior, TLS behavior, failover semantics, or
Java support from generic Java, Oracle, PostgreSQL, MySQL, or framework
defaults. Preserve Altibase tokens exactly.

## Required Customer Inputs

Collect these inputs before drafting a customer-usable JDBC artifact:

- Target Altibase version and patch level, including whether the target is
  7.1, 7.3, or `Altibase 8.1 verified source`.
- Server host, `PORT_NO`, DB name, user, password handling policy, TLS policy,
  and whether the connection is direct JDBC, pooled JDBC, Spring, Hibernate,
  Adapter for JDBC, XA, failover, or tracing work.
- JDK vendor and version, application server or framework version, pool
  library, build system, expected runtime classpath, selected driver JAR path,
  and whether the driver comes from `$ALTIBASE_HOME/lib` or Maven coordinates.
- For Spring and Hibernate, the exact framework version, dialect requirement,
  LOB usage, transaction policy, connection-test query, and whether
  `lob_null_select=off` is required by the target version and driver.
- For TLS, the truststore and keystore paths, passwords, store types,
  certificate policy, and server-certificate verification policy.
- For failover, primary host, alternate hosts, retry count and delay,
  `SessionFailOver`, `LoadBalance`, callback needs, transaction retry policy,
  and non-production test plan.
- For Adapter for JDBC, source Altibase system, target database, Log Analysis
  API prerequisites, `jdbcAdapter` properties, `oaUtility` usage, XLog sender
  handling, LOB requirement, and shutdown plan.
- Expected validation output: `java -version`, `java -jar <driver_jar>`,
  `altibase -v`, basic SELECT result, connection-pool validation result,
  framework startup logs, `jdbc.trc` behavior, and exception text if failing.

If any input is missing, ask for it and provide the safest source-backed next
check instead of inventing a final connection string or build file.

## Generated Artifacts

This playbook may draft:

- JDBC connection snippets using `Altibase.jdbc.driver.AltibaseDriver`,
  `DriverManager.getConnection`, `java.util.Properties`, and
  `jdbc:Altibase://host_ip:port_no/database_name`.
- Driver and build snippets for `Altibase.jar`, `Altibase42.jar`,
  `Altibase7_1.jar`, `Altibase42_7_1.jar`, `Altibase_t.jar`,
  `com.altibase`, `altibase-jdbc`, and
  `org.hibernate.orm:hibernate-community-dialects`.
- Spring configuration for `spring.datasource.driver-class-name`,
  `spring.datasource.url`, `spring.datasource.username`,
  `spring.datasource.password`,
  `spring.datasource.hikari.connection-test-query`, and pool-specific
  properties only when the source route supports them.
- JDBC datasource and XA class guidance using exact tokens such as
  `Altibase.jdbc.driver.AltibaseConnectionPoolDataSource`,
  `Altibase.jdbc.driver.AltibaseXADataSource`, `ABPoolingDataSource`,
  `ABXADataSource`, `AltibaseXAResource`, and `ABXAResource` only after the
  target driver/version route is confirmed.
- Hibernate configuration using `org.hibernate.dialect.AltibaseDialect`,
  `spring.jpa.properties.hibernate.jdbc.lob.non_contextual_creation`, and
  the guarded `lob_null_select=off` route for Altibase 7.1 LOB behavior.
- Failover and TLS connection-property templates using exact source tokens:
  `alternateservers`, `loadbalance`, `connectionretrycount`,
  `connectionretrydelay`, `sessionfailover`,
  `AltibaseFailoverCallback`, `ssl_enable`,
  `verify_server_certificate`, `truststore_url`, `truststore_type`,
  `truststore_password`, `keystore_url`, `keystore_type`, and
  `keystore_password`.
- Adapter for JDBC runbook drafts for `jdbcAdapter`, `oaUtility`, adapter
  properties, environment checks, XLog sender checks, LOB support checks, and
  stop or status commands.
- Connection and diagnostics checklists covering `CMP`, `cm protocol version`,
  `jdbc.trc`, `ALTIBASE_JDBC_TRCLOG_DISABLE`, SQLSTATE, and exception text.

## Procedure

1. Classify the request as direct JDBC, Spring, Hibernate, application-server
   datasource, failover, TLS, Java compatibility, Adapter for JDBC, or
   diagnostics. Route application-server specifics beyond Spring and
   Hibernate to the AID framework reference with `CONF-000007`.
2. Confirm target version and driver source. Check `$ALTIBASE_HOME/lib` before
   selecting `Altibase.jar`, `Altibase42.jar`, `Altibase7_1.jar`,
   `Altibase42_7_1.jar`, or `Altibase_t.jar`; use Maven coordinates only
   when the target patch source supports them.
3. Confirm Java compatibility before generating build files. Preserve
   `Oracle OpenJDK`, `Oracle JDK`, `IBM SDK`, `x`, `-`, and filled-circle
   compatibility-table values as source labels rather than broad support
   claims.
4. Start with a basic JDBC connection and SELECT check. Add Spring,
   Hibernate, TLS, failover, statement cache, or Adapter for JDBC only after
   the basic connection result is captured.
5. For 8.1 statement-cache material, preserve `stmt_cache_enable`,
   `stmt_cache_size`, `stmt_cache_sql_limit`, and
   `Statement.setPoolable(false/true)`. Do not combine driver-side statement
   cache with a duplicate pool cache unless the customer provides pool
   settings and asks for that design.
6. Preserve source-backed datasource property names such as `portNumber`,
   `databaseName`, `user`, `password`, `serverName`, `connType`, `url`,
   `maxPoolSize`, `minPoolSize`, `initialPoolSize`, `maxIdleTime`, and
   `propertyCycle`. Do not rename them to framework-preferred forms unless
   the exact Spring or application-server route uses that form.
7. For Hibernate LOB work, keep the source boundary: Altibase 7.1 requires
   `lob_null_select=off` for the referenced Hibernate path; 7.3 and 8.1
   sources state that the default is off. Do not broaden this into every JDBC
   use case without exact source checking.
8. For failover, produce non-production test steps. Do not claim transaction
   failover. The AID route says CTF applies during connection, STF applies
   after service-time failure, and application logic must retry work.
9. For TLS, do not present `ssl_enable=true` as complete security. Require
   truststore, keystore, password, verification policy, and customer security
   policy inputs.
10. For Adapter for JDBC, require Altibase and the target database to be
   running, adapter properties and environment variables to be configured,
   and a controlled shutdown plan because forcefully terminating the adapter
   can leave the Altibase XLog sender attempting to connect.

## Artifact Templates

Use placeholders until customer inputs and target source routes are confirmed.

```bash
# 00_jdbc_environment_checks.sh
java -version

# Select the actual JAR after checking the delivered package.
ls -1 "$ALTIBASE_HOME/lib"/Altibase*.jar

java -jar "$ALTIBASE_HOME/lib/Altibase.jar"
altibase -v
```

```java
// 10_basic_jdbc_check.java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Properties;

public class AltibaseJdbcCheck {
    public static void main(String[] args) throws Exception {
        Class.forName("Altibase.jdbc.driver.AltibaseDriver");

        String url = "jdbc:Altibase://<host_ip>:<port_no>/<database_name>";
        Properties props = new Properties();
        props.put("user", "<user>");
        props.put("password", "<password_from_secret_store>");

        try (Connection conn = DriverManager.getConnection(url, props);
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery("select 1 from dual")) {
            while (rs.next()) {
                System.out.println(rs.getInt(1));
            }
        }
    }
}
```

```properties
# 20_spring_application.properties
spring.datasource.driver-class-name=Altibase.jdbc.driver.AltibaseDriver
spring.datasource.url=jdbc:Altibase://<host_ip>:<port_no>/<database_name>
spring.datasource.username=<user>
spring.datasource.password=<password_from_secret_store>
spring.datasource.hikari.connection-test-query=select 1 from dual

# Hibernate route. Use only when the target framework and version require it.
spring.jpa.properties.hibernate.jdbc.lob.non_contextual_creation=true
spring.jpa.database-platform=org.hibernate.dialect.AltibaseDialect
```

```xml
<!-- 30_maven_dependencies.xml -->
<dependency>
    <groupId>org.hibernate.orm</groupId>
    <artifactId>hibernate-community-dialects</artifactId>
    <version>6.4.1.Final</version>
</dependency>

<!-- Use only after confirming the target Altibase patch supports Maven Central. -->
<dependency>
    <groupId>com.altibase</groupId>
    <artifactId>altibase-jdbc</artifactId>
    <version><target_altibase_jdbc_version></version>
</dependency>
```

```text
# 40_failover_url_template.txt
jdbc:Altibase://<primary_host>:<port_no>/<database_name>?alternateservers=(<alternate1>:<port_no>,<alternate2>:<port_no>)&connectionretrycount=<count>&connectionretrydelay=<seconds>&sessionfailover=off&loadbalance=off
```

```text
# 50_tls_property_tokens.txt
ssl_enable=true
verify_server_certificate=<true_or_false_from_policy>
truststore_url=<path>
truststore_type=<type>
truststore_password=<secret>
keystore_url=<path_if_client_auth_is_used>
keystore_type=<type_if_client_auth_is_used>
keystore_password=<secret_if_client_auth_is_used>
```

```bash
# 60_jdbc_trace_checks.sh
find "${ALTIBASE_HOME:-.}" -name 'jdbc.trc*' -print

# Use only when the source-supported target version allows disabling trace output.
java -DALTIBASE_JDBC_TRCLOG_DISABLE=true -cp "$ALTIBASE_HOME/lib/Altibase.jar:." AltibaseJdbcCheck
```

## Guardrails

- Source authority: Korean product manuals, Korean third-party guides, the
  Java compatibility technical document, and classified AID source-backed
  references remain the authority routes. English manuals are extraction aids
  unless their classification says otherwise.
- Driver selection: do not select a driver JAR by filename alone. Check the
  installed client package, `java -jar <driver_jar>` output, target server
  version, and `cm protocol version`.
- URL properties: use only source-backed JDBC properties. Preserve case and
  spelling such as `fetch_enough`, `time_zone`, `lob_null_select`,
  `login_timeout`, `query_timeout`, `response_timeout`, `alternateservers`,
  `loadbalance`, `connectionretrycount`, and `sessionfailover`.
- Framework behavior: do not infer Spring, Hibernate, HikariCP, DBCP, Tomcat,
  JEUS, JBoss, WebLogic, or WebSphere behavior from generic framework
  defaults. Route those to the exact source or AID framework block.
- Hibernate LOB behavior: require target version and LOB use before adding
  `lob_null_select=off`. Do not remove it from a 7.1 Hibernate LOB route
  without evidence that the target driver does not need it.
- TLS: require truststore and keystore evidence. Do not expose plaintext
  passwords in committed build files, logs, or examples.
- Failover: require topology and a retry policy. Do not describe STF as
  automatic transaction replay.
- Adapter for JDBC: confirm `jdbcAdapter`, `oaUtility`, adapter properties,
  LOB property requirements such as `ADAPTER_LOB_TYPE_SUPPORT`, and shutdown
  behavior against the exact target source before making an operational
  runbook.

## Validation Checks

Include the relevant checks before handing off generated artifacts:

- Driver and Java: `java -version`, `java -jar Altibase.jar`,
  `java -jar Altibase42.jar`, or the actual delivered driver JAR.
- Server compatibility: `altibase -v`, expected `CMP` token in driver output,
  expected `cm protocol version` token in server output, and target patch.
- Basic connection: run a single SELECT such as `select 1 from dual` before
  adding pools, TLS, failover, Spring, Hibernate, or Adapter for JDBC.
- Spring/Hibernate: verify application startup, datasource initialization,
  validation query, `org.hibernate.dialect.AltibaseDialect`, and LOB behavior
  in a non-production environment.
- LOB methods: when generated code uses LOBs, verify explicit transaction
  handling with `setAutoCommit(false)` and source-backed behavior for
  `ResultSet.getBlob()`, `ResultSet.getClob()`, and
  `Connection.createNClob()`.
- JDBC tracing: locate `jdbc.trc`, `jdbc.trc.lck`, `jdbc.trc.1`, and related
  files when tracing is relevant; for lock errors, check write permission on
  `$ALTIBASE_HOME/trc` or the Java execution directory.
- Failover: capture `SQLException.getSQLState()`, failover callback logs,
  `V$SESSION.FAILOVER_SOURCE` when used by the source route, and application
  retry behavior.
- TLS: verify truststore and keystore file readability, store passwords,
  certificate chain, and the exact exception text, including source-backed
  tokens such as `Could not load keystore`, `Could not open keystore file`,
  and `Could not retreive key from keystore`.
- Adapter for JDBC: validate adapter process status, `oaUtility` status,
  target database connectivity, XLog sender state, LOB support setting, and
  controlled shutdown output.

## Stop Conditions

Stop and ask for evidence if:

- Target Altibase version, patch, JDK version, framework version, driver JAR,
  URL, credentials policy, or validation output is missing.
- The request needs exact Java compatibility, Maven Central availability,
  statement-cache behavior, TLS, failover, or Adapter for JDBC behavior that
  is not present in the cited source route or customer runtime evidence.
- A generated artifact would include a password, truststore password,
  keystore password, or callback class that the customer has not supplied
  through an approved secret-handling path.
- A requested framework, pool, application server, or Hibernate dialect
  version is not covered by the selected source or classified AID route.
- The customer wants production-ready connectivity, exhaustive property
  tables, or patch-specific behavior from this playbook alone.
