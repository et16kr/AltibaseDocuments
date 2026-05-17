# J007 Design Note: Security, Access, Replication, Network, And TLS Properties

## Scope

This job strengthens answer-ready documentation for account security, access-list,
SSL/TLS, replication transport, network port, and SQL Apply property questions. It
does not change benchmark thresholds, source documents, SQL expected answers, or
replication operation runbooks reserved for J013 and J014.

## Evidence Used

- `PROP-135` missed the `PORT_NO` contrast and full `REPLICATION_PORT_NO` semantics.
- `PROP-136` missed `V$PROPERTY` and the EAGER sender-thread order caution.
- `PROP-137` missed `NONE`, `V$PROPERTY`, and the Replication Manual requirement for
  DDL on replicated tables.
- `PROP-138` missed `Lazy`, `Handshaking`, `V$PROPERTY`, and SQL Apply metadata
  conditions.
- `PROP-139` through `PROP-142` missed exact security/access/TLS values, including
  `65535`, quoted password behavior, `PERMIT`, `DENY`, `V$ACCESS_LIST`,
  `ACCESS_LIST_FILE`, and `RELOAD ACCESS LIST` runtime scope.
- `REPL-110` through `REPL-124` needed stronger port separation, `WITH` host-list
  rules, `DROP HOST ALL`, `Unsigned Integer`, `single value`, `Intel Linux`,
  `ALTIBASE_SSL_LOAD_CONFIG`, `FIPS`, `$ALTIBASE_HOME/conf/altibase.properties`, and
  `COMM_NAME` preservation.

## Documentation Pattern

The remediation keeps the existing attachment structure and adds compact literal
blocks that an LLM can quote directly:

- version scope and 8.1-only replication SSL boundaries;
- exact default, range, data type, attribute, and dynamic-change support;
- port separation among `PORT_NO`, `SSL_PORT_NO`, `REPLICATION_PORT_NO`, and
  `REPLICATION_SSL_PORT_NO`;
- `V$PROPERTY` and `V$ACCESS_LIST` validation SQL;
- safe stop conditions for access control, privileged access, DDL replication, EAGER
  replication, SSL/TLS, and SQL Apply changes.

## Boundary

This job adds property-level and retrieval-facing exact-token remediation. Broader
replication topology/state remediation, CDC/Log Analyzer procedure expansion, and final
retrieval restructuring remain for later jobs.
