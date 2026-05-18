# Security And TLS Playbook

- Playbook ID: `APB-000008`
- Owning job: `S2-J005`
- Validation status: `pass`
- Supported versions: Altibase 7.1, Altibase 7.3, and `Altibase 8.1 verified source`
- Protected topic: yes

## Source Routes

| Route | Source IDs | Source-pack block refs | Baseline blocks |
| --- | --- | --- | --- |
| TLS server setup, certificate paths, OpenSSL checks, protected security properties, security-sensitive administration, and client TLS handoff | `SRC-000051`, `SRC-000020`, `SRC-000115`, `SRC-000084`, `SRC-000175`, `SRC-000145`, `SRC-000049`, `SRC-000018`, `SRC-000113`, `SRC-000082`, `SRC-000173`, `SRC-000143`, `SRC-000056`, `SRC-000025`, `SRC-000120`, `SRC-000089`, `SRC-000180`, `SRC-000150`, `AID-SRC-000428` | `SRC-000051/BLOCK-000851`, `SRC-000020/BLOCK-000850`, `SRC-000115/BLOCK-000853`, `SRC-000084/BLOCK-000852`, `SRC-000175/BLOCK-000855`, `SRC-000145/BLOCK-000854`, `SRC-000049/BLOCK-000002`, `SRC-000018/BLOCK-000001`, `SRC-000113/BLOCK-000004`, `SRC-000082/BLOCK-000003`, `SRC-000173/BLOCK-000006`, `SRC-000143/BLOCK-000005`, `SRC-000056/BLOCK-000515`, `SRC-000025/BLOCK-000514`, `SRC-000120/BLOCK-000517`, `SRC-000089/BLOCK-000516`, `SRC-000180/BLOCK-000519`, `SRC-000150/BLOCK-000518`, `BLOCK-000438` | `KAE-BLOCK-000272`, `KAE-BLOCK-000274`, `KAE-BLOCK-000276` |

Guardrails: `CONF-000004`, `CONF-000006`, and `CONF-000007` remain open. This
playbook can draft guarded TLS and security-sensitive administration plans, but
exact certificate commands, client connection strings, API calls, cipher tables,
FIPS behavior, and production security policy require exact source recheck,
client/tool evidence, and customer security approval.

Forbidden assumption note: do not mix TLS requirements across Altibase 7.1,
7.3, and `Altibase 8.1 verified source`; do not infer OpenSSL, Java, ODBC, or
JDBC behavior from generic TLS guidance.

## Required Customer Inputs

Missing input prompts to collect before generating a TLS or security artifact:

- Target Altibase version and patch level.
- Server platform, OpenSSL toolkit version, OpenSSL library path, and
  `openssl version` output.
- TLS goal: server-only TLS, mutual authentication, JDBC TLS, ODBC/CLI TLS,
  iSQL TLS, replication SSL, certificate rotation, cipher restriction, or
  protected security property change.
- Server certificate path, server private-key path, CA file or CA directory,
  truststore path, keystore path, passwords handling policy, and file ownership.
- `SSL_ENABLE`, `SSL_PORT_NO`, `SSL_MAX_LISTEN`, `SSL_CIPHER_LIST`,
  `SSL_CLIENT_AUTHENTICATION`, `SSL_CERT`, `SSL_KEY`, `SSL_CA`, `SSL_CAPATH`,
  `SSL_CIPHERS_SUITES`, and `SSL_LOAD_CONFIG` target values where applicable.
- Client type, Java/JRE version for JDBC, DSN or URL policy, server-name
  verification policy, and whether `SSL_VERIFY=0` is being requested.
- Network path, existing TCP port, proposed SSL port, firewall policy,
  maintenance window, validation plan, and rollback plan.
- AID labels when AID security guidance is used.

## Generated Artifacts

This playbook may draft:

- TLS evidence request and certificate inventory.
- Protected `altibase.properties` change plan.
- Non-destructive OpenSSL and file-permission checks.
- Server startup validation checklist.
- Client TLS handoff notes for the JDBC and ODBC/C client playbooks.
- Security exception request for disabling certificate verification.
- Rollback notes for reverting TLS properties or certificate paths.

## Procedure

1. Confirm the version route before any TLS recommendation. The 7.1 SSL/TLS
   source supports OpenSSL 0.9.4 through 1.0.2 and warns to verify Heartbleed
   exposure. The 7.3 and 8.1-verified SSL/TLS sources require OpenSSL toolkit
   3.0.8 and state that 7.3 no longer supports OpenSSL 1.0.x.
2. Run non-destructive OpenSSL and file checks before property edits.
3. Classify the TLS goal. Server listener setup belongs here; connector-specific
   JDBC, ODBC/CLI, iSQL, or replication SSL connection strings should be routed
   to the more specific playbook after server TLS prerequisites are confirmed.
4. Prepare a protected property plan for `SSL_ENABLE`, `SSL_PORT_NO`,
   `SSL_MAX_LISTEN`, `SSL_CIPHER_LIST`, `SSL_CLIENT_AUTHENTICATION`,
   `SSL_CERT`, `SSL_KEY`, `SSL_CA`, `SSL_CAPATH`, `SSL_CIPHERS_SUITES`, and
   `SSL_LOAD_CONFIG` only after target-version source checks.
5. Verify server certificate, private key, and CA files are readable by the
   Altibase process account and are not world-readable when customer policy
   forbids that.
6. Restart or startup is required when the exact source route says the TLS
   property path is static or server-start dependent. Do not claim online
   activation unless the exact property source says so.
7. Validate startup output for both TCP and SSL listener evidence when TLS is
   enabled.

## Artifact Templates

```sh
# 00_tls_first_checks.sh
openssl version
openssl ciphers
test -r "<server_certificate_path>" && ls -l "<server_certificate_path>"
test -r "<server_private_key_path>" && ls -l "<server_private_key_path>"
test -r "<ca_file_or_directory>" && ls -ld "<ca_file_or_directory>"
```

```text
# 10_altibase_properties_tls_plan.txt
# Use only after exact target-version property checks and customer approval.
# Record original values, desired values, restart requirement, validation,
# and rollback plan before editing $ALTIBASE_HOME/conf/altibase.properties.

SSL_ENABLE = <0_or_1>
SSL_PORT_NO = <ssl_port>
SSL_MAX_LISTEN = <max_listen>
SSL_CIPHER_LIST = <cipher_list>
SSL_CLIENT_AUTHENTICATION = <0_or_1>
SSL_CERT = <server_certificate_path>
SSL_KEY = <server_private_key_path>
SSL_CA = <ca_file>
SSL_CAPATH = <ca_directory>
SSL_CIPHERS_SUITES = <tls13_cipher_suites>
SSL_LOAD_CONFIG = <0_or_1>
```

```sql
-- 90_tls_property_validation.sql
SELECT NAME, VALUE1, VALUE2
FROM V$PROPERTY
WHERE NAME IN ('SSL_ENABLE',
               'SSL_PORT_NO',
               'SSL_MAX_LISTEN',
               'SSL_CIPHER_LIST',
               'SSL_CLIENT_AUTHENTICATION',
               'SSL_CERT',
               'SSL_KEY',
               'SSL_CA',
               'SSL_CAPATH',
               'SSL_CIPHERS_SUITES',
               'SSL_LOAD_CONFIG')
ORDER BY NAME;
```

## Guardrails

- Stop if the OpenSSL version does not match the exact Altibase version source.
- Stop if private keys, certificates, CA files, truststores, or keystores are
  missing, unreadable by the intended process, or not approved by customer
  security policy.
- Stop before setting `SSL_VERIFY=0` without an explicit customer security
  exception and compensating validation.
- Stop before mixing 7.1 TLS requirements with 7.3 or 8.1-verified TLS
  requirements.
- Stop before presenting connector-specific TLS snippets as ready when the
  exact connector playbook, client version, and runtime output have not been
  checked.

## Validation Checks

Every TLS or security-sensitive administration artifact must include:

- Exact source route, target version, patch level, and OpenSSL version evidence.
- Non-destructive file readability and ownership checks for certificates,
  private keys, CA paths, truststores, and keystores.
- Property before/after plan, restart requirement, validation query, and
  rollback note for `altibase.properties`.
- Listener validation after startup, including expected TCP and SSL listener
  evidence when SSL is enabled.
- Client handoff route when JDBC, ODBC/CLI, iSQL, or replication SSL details
  are needed.
- Customer approval for disabling certificate verification or weakening cipher
  policy.

## Stop Conditions

Stop and ask for missing input if:

- The target version, OpenSSL output, certificate paths, private-key path, CA
  evidence, authentication mode, client type, network path, validation plan, or
  rollback plan is missing.
- The request depends on production security policy, certificate rotation,
  disabled verification, FIPS behavior, connector-specific TLS, or live startup
  output that the customer has not supplied.
- The requested TLS change could make the database unreachable and no tested
  rollback path or maintenance window has been supplied.
