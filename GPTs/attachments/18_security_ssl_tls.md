# 18. Security and SSL/TLS

## Applicable Versions

- 7.1: Based on Altibase 7.1 SSL/TLS guidance.
- 7.3: Based on Altibase 7.3 SSL/TLS guidance and release notes for OpenSSL 3.0.8, TLS 1.3, and FIPS configuration.
- 8.1: Based on Altibase 8.1 verified source SSL/TLS guidance, release notes, and replication SSL guidance.

## Questions This File Can Answer

- How should an Altibase server be configured to accept SSL/TLS connections?
- How should JDBC, ODBC/CLI, ADO.NET, iSQL, and utilities connect over SSL/TLS?
- Which server and client properties control certificates, ciphers, verification, ports, and FIPS loading?
- What changed between 7.1, 7.3, and 8.1?
- How is Altibase 8.1 replication SSL configured with `USING SSL` and `REPLICATION_SSL_PORT_NO`?
- How can SSL/TLS sessions be verified, restricted, monitored, or closed?

## Source Documents

- 7.1: Altibase 7.1 SSL/TLS User's Guide; General Reference; iSQL and utility guidance where SSL ports are relevant.
- 7.3: Altibase 7.3 SSL/TLS User's Guide; General Reference; iSQL and utility guidance; Altibase 7.3 release notes.
- 8.1: Altibase 8.1 verified source SSL/TLS User's Guide; Altibase 8.1 verified source Replication Manual; Altibase 8.1 verified source General Reference where available; Altibase 8.1 release notes.

## Response Rules

- Answer explanatory text in the user's language.
- Keep SQL object names, function names, error codes, property names, commands, file paths, environment variables, connection-string keys, and view names literal.
- Separate ordinary client/server SSL/TLS from replication SSL. Do not answer them as one configuration surface.
- For 8.1-specific statements, say `Altibase 8.1 verified source`.
- Do not expose internal source labels or local source-tree paths in customer answers.
- For production SSL/TLS changes, ask for the exact Altibase version, client interface, authentication mode, certificate type, server and client OS, OpenSSL version, and target ports before giving a final procedure.

## Fast Decision Map

```mermaid
flowchart TD
  A[SSL/TLS question] --> B{Connection type}
  B -- Application to Altibase server --> C[Server SSL/TLS plus client SSL/TLS]
  B -- Altibase replication between nodes --> D[Replication SSL/TLS]
  B -- Utility or iSQL connection --> E[Client SSL/TLS for tools]
  C --> F{Client interface}
  F -- JDBC --> G[JDBC truststore keystore properties]
  F -- ODBC or CLI --> H[OpenSSL PEM files and SSL_* connection properties]
  F -- ADO.NET --> I[ADO.NET SSL connection-string keys]
  D --> J{Version}
  J -- 8.1 --> K[USING SSL plus peer REPLICATION_SSL_PORT_NO]
  J -- 7.1 or 7.3 --> L[Use ordinary TCP replication unless a supported source says otherwise]
```

## Core Concepts

Altibase SSL/TLS protects network communication by encrypting data, authenticating the server, and optionally authenticating the client. Altibase uses an additional SSL/TLS listening port rather than switching an existing TCP connection from non-secure to secure.

Authentication modes:

- `Server-only authentication`: the server presents its certificate and the client verifies the server.
- `Mutual authentication`: the server presents its certificate, and the server also requests a client certificate during the SSL/TLS handshake.

Connection surfaces:

- `Server SSL/TLS`: controlled mainly by `SSL_ENABLE`, `SSL_PORT_NO`, certificate properties, cipher properties, and `SSL_CLIENT_AUTHENTICATION`.
- `Client SSL/TLS`: controlled by interface-specific settings such as JDBC properties, ODBC/CLI `SSL_*` properties, ADO.NET connection-string keys, and `ALTIBASE_SSL_PORT_NO`.
- `Replication SSL/TLS`: an Altibase 8.1 replication feature using `CREATE REPLICATION ... USING SSL` and `REPLICATION_SSL_PORT_NO`.

```mermaid
flowchart LR
  Client[JDBC, ODBC/CLI, ADO.NET, iSQL, utility] -->|SSL/TLS to SSL_PORT_NO| DB1[Altibase server]
  DB1 -->|Sender using SSL to peer REPLICATION_SSL_PORT_NO| DB2[Altibase peer]
  DB2 -->|Sender using SSL to peer REPLICATION_SSL_PORT_NO| DB1
```

## Version Differences

Version block: 7.1

- TLS support: Altibase 7.1 SSL/TLS guidance describes TLS 1.0 through the OpenSSL library.
- OpenSSL requirement: OpenSSL toolkit `0.9.4` through `1.0.2` according to the 7.1 SSL/TLS guide.
- Java guidance: JRE 1.6 or later is recommended for convenient SSL client setup; JRE 1.5 can be used but is not recommended.
- Server properties: use `SSL_ENABLE`, `SSL_PORT_NO`, `SSL_MAX_LISTEN`, `SSL_CIPHER_LIST`, `SSL_CLIENT_AUTHENTICATION`, `SSL_CERT`, `SSL_KEY`, `SSL_CA`, and `SSL_CAPATH`.
- 7.1 sources do not define `SSL_CIPHER_SUITES`, `SSL_LOAD_CONFIG`, or replication SSL.

Version block: 7.3

- TLS support: Altibase 7.3 supports TLS 1.0, TLS 1.2, and TLS 1.3 through OpenSSL.
- OpenSSL requirement: OpenSSL 3.0.8 is supported; OpenSSL 1.0.x is no longer supported.
- Java guidance: Java 1.8.0_351 or later is recommended for TLS 1.3 cipher use without extra settings. Java 1.8.0_261 or later supports TLS 1.3 when the client starts with `-Djdk.tls.client.protocols="TLSv1.3"` where needed.
- Newer SSL properties: `SSL_CIPHER_SUITES` configures TLS 1.3 cipher suites; `SSL_LOAD_CONFIG` loads the OpenSSL configuration file and is used for FIPS module configuration.
- Replication SSL is not documented as a 7.3 feature in the customer-facing sources for this attachment.

Version block: 8.1

- General SSL/TLS: use Altibase 8.1 verified source. The ordinary server and client setup follows the current SSL/TLS guide baseline.
- Replication SSL: Altibase 8.1 release notes add SSL/TLS support for replication communication.
- Replication syntax: use `CREATE REPLICATION ... WITH 'peer_host', peer_ssl_replication_port USING SSL`.
- Replication property: `REPLICATION_SSL_PORT_NO` configures the local SSL replication Receiver port. If this property is `0`, SSL replication is disabled for that node.

## Server SSL/TLS

Use this section for application-to-server SSL/TLS, not replication SSL.

Server setup checklist:

1. Confirm that the Altibase version and OpenSSL version match the target version guidance.
2. Prepare the server certificate, server private key, and CA certificate or CA directory.
3. Set SSL/TLS server properties in `altibase.properties`.
4. Decide whether the server will use server-only authentication or mutual authentication.
5. Start the server and verify that the SSL listener is created.
6. Test one client connection over the SSL/TLS port.
7. Monitor `V$SESSION` to confirm that the session `COMM_NAME` starts with `SSL`.

Representative server property file:

```properties
SSL_ENABLE = 1
SSL_PORT_NO = 20443
SSL_MAX_LISTEN = 128
SSL_CLIENT_AUTHENTICATION = 0
SSL_CERT = ?/cert/server-cert.pem
SSL_KEY = ?/cert/server-key.pem
SSL_CA = ?/cert/ca-cert.pem
# SSL_CAPATH = /etc/ssl/certs
# SSL_CIPHER_LIST = HIGH:!aNULL
# SSL_CIPHER_SUITES = TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256
# SSL_LOAD_CONFIG = 1
```

Server property block: `SSL_ENABLE`

- Purpose: enables or disables SSL/TLS on the Altibase server.
- Values: `0` disables SSL/TLS; `1` enables SSL/TLS.
- Default: `0`.
- Use when: the server must listen for SSL/TLS client connections.

Server property block: `SSL_PORT_NO`

- Purpose: SSL/TLS listener port for client connections.
- Range: `1024` through `65535`.
- Default: `20443`.
- Caution: the SSL/TLS port must be distinct from the ordinary TCP service port.

Server property block: `SSL_MAX_LISTEN`

- Purpose: maximum listen queue size for concurrent SSL/TLS connections.
- Default: `128`.
- Range: `0` through `16384`.
- Caution: larger listen capacity can require more memory.

Server property block: `SSL_CLIENT_AUTHENTICATION`

- Purpose: controls whether the server requests a client certificate.
- Values: `0` means server-only authentication; `1` means mutual authentication.
- Default: `0`.
- Use `1` only when client certificates are prepared and distributed.

Server property block: `SSL_CERT`

- Purpose: server certificate path.
- Example: `?/cert/server-cert.pem`.
- Caution: the certificate must match the private key configured by `SSL_KEY`.

Server property block: `SSL_KEY`

- Purpose: server private key path.
- Example: `?/cert/server-key.pem`.
- Caution: protect this file with OS permissions and do not share it with clients.

Server property block: `SSL_CA`

- Purpose: file path for CA certificates used to verify received certificates.
- Example: `?/cert/ca-cert.pem`.
- Use with: public CA certificates or private CA certificates.

Server property block: `SSL_CAPATH`

- Purpose: CA directory path in X.509 directory format.
- Example: `/etc/ssl/certs`.
- Use when: CA certificates are managed as a directory instead of a single CA file.

Server property block: `SSL_CIPHER_LIST`

- Purpose: cipher candidate list for negotiated SSL/TLS communication before TLS 1.3 handling.
- Format: OpenSSL cipher names separated by colons.
- Verification command:

```sh
openssl ciphers
```

Server property block: `SSL_CIPHER_SUITES`

- Version: 7.3 and 8.1 verified source.
- Purpose: TLS 1.3 cipher suite candidates.
- Format: TLS 1.3 cipher suite names separated by colons.
- Default behavior: when unset, OpenSSL allows available TLS 1.3 cipher candidates.

Server property block: `SSL_LOAD_CONFIG`

- Version: 7.3 and 8.1 verified source.
- Purpose: loads `openssl.cnf`.
- Values: `0` does not load the file; `1` loads the file.
- Use when: enabling the OpenSSL FIPS module or another OpenSSL configuration that must be loaded by Altibase.

Server start verification:

```sh
server start
```

Expected listener evidence:

```text
[CM] Listener started : TCP on port 20300 [IPV4]
[CM] Listener started : SSL on port 20443 [IPV4]
```

## Client SSL/TLS

Use this section for client-to-server SSL/TLS. This includes applications and tools. It does not configure replication SSL.

Client certificate decision matrix:

- Private CA plus server-only authentication: import the server CA certificate into the client truststore or configure the client CA file.
- Private CA plus mutual authentication: import the server CA certificate into the truststore or client CA configuration, and configure the client certificate plus private key.
- Public CA plus server-only authentication: no private CA import is normally needed if the client runtime already trusts the issuing CA.
- Public CA plus mutual authentication: configure the client certificate plus private key.

JDBC setup checklist:

1. For private CA server certificates, import the server CA certificate into a truststore.
2. For mutual authentication, prepare a PKCS #12 file containing the client certificate and private key, then import it into a Java keystore.
3. Configure Java SSL properties either as JVM options, `System.setProperty(...)`, or JDBC connection properties.
4. Set `ssl_enable=true`.
5. Set `port` to the server `SSL_PORT_NO`, or set `ALTIBASE_SSL_PORT_NO` for tools and clients that use it.
6. For TLS 1.3 on 7.3 or 8.1, use a Java version that supports TLS 1.3 and set `ssl_protocols` when protocol pinning is needed.

JDBC truststore import:

```sh
keytool -import -alias alias_name -file server_certificate_file.pem -keystore truststore -storepass password
```

JDBC PKCS #12 preparation and import for mutual authentication:

```sh
openssl pkcs12 -export -in client_certificate.pem -inkey client_secretkey_file.pem > pkcs_file.p12
keytool -importkeystore -srckeystore pkcs_file.p12 -destkeystore keystore.jks -srcstoretype pkcs12
```

JDBC JVM properties:

```text
-Djavax.net.ssl.keyStore=path_to_keystore
-Djavax.net.ssl.keyStorePassword=password
-Djavax.net.ssl.trustStore=path_to_truststore
-Djavax.net.ssl.trustStorePassword=password
```

JDBC `System.setProperty(...)` form:

```java
System.setProperty("javax.net.ssl.keyStore", "path_to_keystore");
System.setProperty("javax.net.ssl.keyStorePassword", "password");
System.setProperty("javax.net.ssl.trustStore", "path_to_truststore");
System.setProperty("javax.net.ssl.trustStorePassword", "password");
```

JDBC connection property form:

```java
Properties props = new Properties();
props.put("ssl_enable", "true");
props.put("port", "20443");
props.put("keystore_url", "path_to_keystore");
props.put("keystore_password", "password");
props.put("truststore_url", "path_to_truststore");
props.put("truststore_password", "password");
```

JDBC property block: `ssl_enable`

- Purpose: chooses SSL/TLS or ordinary TCP for a JDBC connection.
- Values: `true` uses SSL/TLS; `false` uses ordinary TCP.
- Default: `false`.

JDBC property block: `port`

- Purpose: target server port.
- For SSL/TLS: set it to the server `SSL_PORT_NO`.
- Caution: do not rely on implicit defaults in production. Set `port` or `ALTIBASE_SSL_PORT_NO` explicitly.

JDBC property block: `ciphersuite_list`

- Purpose: Java cipher suite candidate list.
- Format: cipher suite names separated by colons.
- Caution: if the JRE does not support a named suite, the client can raise an `Unsupported ciphersuite` error.

JDBC property block: `ssl_protocols`

- Version: 7.3 and 8.1 verified source.
- Purpose: protocol list for SSL/TLS communication.
- Format: comma-separated values such as `TLSv1.2,TLSv1.3`.

JDBC property block: `verify_server_certificate`

- Purpose: controls server certificate verification.
- Values: `true` verifies the server certificate; `false` skips server CA verification.
- Default: `true`.
- Caution: use `false` only for controlled troubleshooting or explicitly accepted exception cases.

JDBC property block: `keystore_url`, `keystore_type`, `keystore_password`

- Purpose: client private-key and certificate container for mutual authentication.
- Common types: `JKS`, `JCEKS`, `PKCS12`.
- Default type: `JKS`.

JDBC property block: `truststore_url`, `truststore_type`, `truststore_password`

- Purpose: certificate store used to trust the server certificate issuer.
- Common types: `JKS`, `JCEKS`, `PKCS12`.

ODBC/CLI setup checklist:

1. Verify that OpenSSL libraries and the `openssl` utility are installed on the client host.
2. For mutual authentication, prepare the client certificate and private key in PEM format.
3. Configure `SSL_CA` or `SSL_CAPATH` when server certificate verification is required.
4. Configure `SSL_CERT` and `SSL_KEY` when mutual authentication is enabled.
5. Connect with SSL/TLS by selecting SSL connection type and using the server `SSL_PORT_NO`.
6. For FIPS on 7.3 or 8.1 verified source, set `ALTIBASE_SSL_LOAD_CONFIG=1` for ODBC/CLI clients and set `SSL_LOAD_CONFIG=1` on the server. For ADO.NET or other clients, use only source-documented SSL connection keys unless a matching guide explicitly documents FIPS config loading.

ODBC/CLI verification commands:

```sh
ls -al /usr/lib/libssl*
ls -al /usr/lib/libcrypto*
openssl version
```

ODBC/CLI property block: `SSL_CA`

- Purpose: CA certificate file for verifying received certificates.
- Example: `SSL_CA=/cert/ca-cert.pem`.

ODBC/CLI property block: `SSL_CAPATH`

- Purpose: CA certificate directory.
- Example: `SSL_CAPATH=/etc/ssl/certs`.

ODBC/CLI property block: `SSL_CERT`

- Purpose: client certificate path.
- Example: `SSL_CERT=/cert/client-cert.pem`.

ODBC/CLI property block: `SSL_KEY`

- Purpose: client private key path.
- Example: `SSL_KEY=/cert/client-key.pem`.

ODBC/CLI property block: `SSL_VERIFY`

- Purpose: controls server certificate verification.
- Values: `0` or `OFF` does not verify the server certificate; `1` or `ON` verifies it.
- Default in SSL/TLS guide: `0`.
- Caution: production connections should normally verify the server certificate.

ODBC/CLI property block: `SSL_CIPHER`

- Purpose: client-side cipher candidate list.
- Format: OpenSSL cipher names separated by colons.

ODBC/CLI connection note:

- On the client side, `SSL_ENABLE` and `SSL_PORT_NO` are server properties. ODBC/CLI clients select SSL/TLS with the SSL connection type and connect to the SSL/TLS port, for example `PORT=20443` or the equivalent tool-specific `PORT_NO` key.
- If a specific tool documents a numeric connection type for SSL/TLS, use that tool's documented value. Otherwise keep answers at the named setting level, such as `CONNTYPE=SSL`.

ADO.NET setup checklist:

1. Verify OpenSSL the same way as ODBC/CLI.
2. Prepare PEM files for mutual authentication when needed.
3. Use `conn type=ssl`.
4. Set `Port` to the server `SSL_PORT_NO`.
5. Add `ssl ca`, `ssl capath`, `ssl cert`, `ssl key`, `ssl verify`, and `ssl cipher` as required by the authentication mode.

ADO.NET example:

```text
Server=127.0.0.1;Port=20443;User=user;Password=pwd;conn type=ssl;ssl ca=/altibase_home/sample/CERT/ca-cert.pem;ssl cert=/altibase_home/sample/CERT/client-cert.pem;ssl key=/altibase_home/sample/CERT/client-key.pem
```

Production server-certificate verification requires `ssl verify=true` plus `ssl ca` or `ssl capath`; do not copy the manual-style example as a complete production verification pattern without that setting.

iSQL and utility port guidance:

- `ALTIBASE_SSL_PORT_NO` specifies the server SSL/TLS port for SSL/TLS client connections.
- For iSQL and several utilities, the explicit `-PORT` option has highest priority, then `ALTIBASE_SSL_PORT_NO`, then the property file value. If no port is available, the tool can prompt for a port.
- Utility-specific SSL options may include `SSL_ENABLE`, `SSL_CA`, `SSL_CAPATH`, `SSL_CERT`, `SSL_KEY`, `SSL_CIPHER`, and `SSL_VERIFY`. Check the relevant utility attachment when answering tool-specific syntax.

## Replication SSL/TLS

Use this section only for Altibase-to-Altibase replication communication.

Scope:

- Replication SSL is an Altibase 8.1 feature in the Altibase 8.1 verified source.
- It is separate from the ordinary client/server `SSL_PORT_NO`.
- It uses `REPLICATION_SSL_PORT_NO` for the local replication Receiver SSL port.
- It uses `USING SSL` in `CREATE REPLICATION` to select SSL/TLS replication communication.

Replication SSL prerequisites:

1. Confirm both nodes are Altibase 8.1 when using the verified 8.1 replication SSL guidance.
2. Complete ordinary SSL/TLS setup on each replication target server before creating SSL replication.
3. Set `REPLICATION_SSL_PORT_NO` to a nonzero local port on each node.
4. Open firewall routes for each node's `REPLICATION_SSL_PORT_NO`.
5. Create the same replication object name on both nodes, with reversed peer host and peer SSL replication port.
6. Use `USING SSL` on both replication objects.
7. Do not combine `FOR ANALYSIS` Log Analyzer replication with SSL communication. The verified source notes that Log Analyzer does not support SSL or InfiniBand communication.

Replication property block: `REPLICATION_SSL_PORT_NO`

- Version: Altibase 8.1 verified source.
- Purpose: local SSL replication Receiver port.
- Data type: unsigned integer.
- Default: `0`.
- Range: `0` through `65535`.
- Meaning of `0`: SSL replication cannot be connected on that node.
- Caution: this is not the ordinary client/server `SSL_PORT_NO`.

Replication SSL syntax:

```text
CREATE [LAZY | EAGER] REPLICATION replication_name
  [FOR PROPAGABLE LOGGING | FOR PROPAGATION]
  [AS MASTER | AS SLAVE]
  [OPTIONS option_name [option_name ...]]
  WITH 'remote_host_ip_or_name', remote_replication_ssl_port USING SSL
  FROM user_name.table_name [PARTITION partition_name]
  TO   user_name.table_name [PARTITION partition_name]
  [, FROM ... TO ...];
```

Replication SSL example:

```sql
-- Node A
CREATE REPLICATION rep1
WITH '192.168.1.12', 45524 USING SSL
FROM sys.employees TO sys.employees,
FROM sys.departments TO sys.departments;

-- Node B
CREATE REPLICATION rep1
WITH '192.168.1.60', 35524 USING SSL
FROM sys.employees TO sys.employees,
FROM sys.departments TO sys.departments;
```

Example interpretation:

- Node A connects to Node B at `45524`, which must be Node B's `REPLICATION_SSL_PORT_NO`.
- Node B connects to Node A at `35524`, which must be Node A's `REPLICATION_SSL_PORT_NO`.
- Both sides use the same `replication_name`, here `rep1`.
- Both sides include `USING SSL`.

Replication connection type guidance:

- Omitted `USING` clause: ordinary TCP replication.
- `USING SSL`: SSL/TLS replication, Altibase 8.1 verified source.
- `USING IB`: InfiniBand replication where supported.
- For TCP replication, the peer port is `REPLICATION_PORT_NO`.
- For SSL replication, the peer port is `REPLICATION_SSL_PORT_NO`.
- For InfiniBand replication, the peer port is `REPLICATION_IB_PORT_NO`.

## Managing SSL/TLS Access

Limit ordinary TCP access for a database user:

```sql
CREATE USER user_name IDENTIFIED BY password DISABLE TCP;
ALTER USER user_name DISABLE TCP;
ALTER USER user_name ENABLE TCP;
```

Check TCP access status:

```sql
SELECT user_name, disable_tcp
FROM SYSTEM_.SYS_USERS_
ORDER BY user_name;
```

Monitor SSL/TLS sessions:

```sql
SELECT id, db_username, comm_name
FROM V$SESSION
WHERE comm_name LIKE 'SSL%';
```

Close an unwanted session as `SYSDBA`:

```sql
ALTER DATABASE database_name SESSION CLOSE session_number;
```

Verify SSL/TLS and replication properties:

```sql
SELECT name, value1
FROM V$PROPERTY
WHERE name IN (
  'SSL_ENABLE',
  'SSL_PORT_NO',
  'SSL_MAX_LISTEN',
  'SSL_CLIENT_AUTHENTICATION',
  'SSL_CIPHER_LIST',
  'SSL_CIPHER_SUITES',
  'SSL_LOAD_CONFIG',
  'SSL_CERT',
  'SSL_KEY',
  'SSL_CA',
  'SSL_CAPATH',
  'REPLICATION_PORT_NO',
  'REPLICATION_SSL_PORT_NO'
)
ORDER BY name;
```

## Troubleshooting Blocks

Troubleshooting block: SSL listener is not shown at startup

- Check `SSL_ENABLE=1`.
- Check that `SSL_PORT_NO` is set to a free port.
- Check OpenSSL installation and version for the Altibase version.
- Check `SSL_CERT`, `SSL_KEY`, and CA configuration.
- Check server logs for certificate load or OpenSSL load failures.

Troubleshooting block: JDBC handshake fails

- Check `ssl_enable=true`.
- Set the SSL/TLS `port` explicitly.
- If a private CA is used, import the server CA certificate into the truststore.
- If mutual authentication is enabled, configure `keystore_url` and `keystore_password`.
- Check `verify_server_certificate`.
- Check `ssl_protocols` and `ciphersuite_list` for Java runtime compatibility.

Troubleshooting block: ODBC/CLI or ADO.NET handshake fails

- Verify OpenSSL libraries with `ls -al /usr/lib/libssl*` and `ls -al /usr/lib/libcrypto*`.
- Check `openssl version`.
- Check `SSL_CA` or `SSL_CAPATH` for server certificate verification.
- Check `SSL_CERT` and `SSL_KEY` for mutual authentication.
- Check `SSL_VERIFY` or `ssl verify`.
- Check cipher compatibility through `SSL_CIPHER`.

Troubleshooting block: TLS 1.3 cipher does not work

- For 7.3 and 8.1 verified source, configure server TLS 1.3 candidates with `SSL_CIPHER_SUITES`.
- For JDBC, use a Java runtime that supports TLS 1.3.
- On Java 1.8.0_261 or later where needed, start with `-Djdk.tls.client.protocols="TLSv1.3"`.
- On Java clients, set `ssl_protocols=TLSv1.3` only when the server and runtime both support it.

Troubleshooting block: FIPS configuration does not take effect

- Configure the OpenSSL FIPS module in `openssl.cnf`.
- Set server `SSL_LOAD_CONFIG=1`.
- Set client `ALTIBASE_SSL_LOAD_CONFIG=1` for ODBC/CLI clients that must load the OpenSSL configuration.
- Restart affected server and client processes after changing environment variables or property files.

Troubleshooting block: replication SSL does not connect

- Confirm the feature is being used on Altibase 8.1 verified source.
- Confirm ordinary SSL/TLS setup is complete on both replication target servers.
- Confirm each node's `REPLICATION_SSL_PORT_NO` is nonzero.
- In each `CREATE REPLICATION`, use the peer node's `REPLICATION_SSL_PORT_NO`.
- Include `USING SSL` on both replication objects.
- Check firewall rules for both SSL replication ports.
- Do not use `FOR ANALYSIS` Log Analyzer replication with `USING SSL`.

## Customer Answer Templates

Template: server SSL/TLS setup

```text
Configure server SSL/TLS in `altibase.properties`: set `SSL_ENABLE=1`, choose a unique `SSL_PORT_NO`, set `SSL_CERT`, `SSL_KEY`, and `SSL_CA` or `SSL_CAPATH`, then choose `SSL_CLIENT_AUTHENTICATION=0` for server-only authentication or `1` for mutual authentication. Restart the server and verify the startup output shows `Listener started : SSL on port ...`.
```

Template: JDBC SSL/TLS setup

```text
For JDBC, set `ssl_enable=true` and set `port` to the server `SSL_PORT_NO`. If the server certificate is issued by a private CA, import the CA certificate into a truststore and configure `truststore_url` and `truststore_password`. For mutual authentication, import the client certificate and private key into a keystore and configure `keystore_url` and `keystore_password`.
```

Template: ODBC/CLI SSL/TLS setup

```text
For ODBC/CLI, verify OpenSSL on the client host, connect with the SSL connection type, and use the server `SSL_PORT_NO`. Configure `SSL_CA` or `SSL_CAPATH` for server verification. For mutual authentication, also configure `SSL_CERT` and `SSL_KEY`. Use `SSL_VERIFY=1` when the server certificate must be verified.
```

Template: Altibase 8.1 replication SSL setup

```text
In Altibase 8.1 verified source, replication SSL is configured separately from ordinary client SSL. Set a nonzero `REPLICATION_SSL_PORT_NO` on each node, complete SSL/TLS setup on both replication target servers, then create matching replication objects with reversed peer endpoints and `USING SSL`. The port in `WITH 'peer_host', peer_port USING SSL` must be the peer node's `REPLICATION_SSL_PORT_NO`.
```

Template: monitoring SSL/TLS sessions

```text
Use `SELECT id, db_username, comm_name FROM V$SESSION WHERE comm_name LIKE 'SSL%';` to find current SSL/TLS sessions. If a session must be forcibly disconnected, connect as `SYSDBA` and run `ALTER DATABASE database_name SESSION CLOSE session_number;`.
```
