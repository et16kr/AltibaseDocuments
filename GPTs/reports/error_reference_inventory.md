# Altibase GPT Error Reference Inventory

Job: `J022`
Status: Active support artifact
Last updated: 2026-05-17

## Reconfirmed Requirement And Boundary

`J022` inventories Altibase error-code families and defines the error block and
troubleshooting response schema that later error jobs must use. It is a
documentation-scope baseline for J023-J026. It does not try to convert every Error
Message Reference entry into a customer-facing block.

The target customer attachment affected by this job is:

- `GPTs/attachments/07_error_messages_troubleshooting.md`

Support artifacts affected by this job are:

- `GPTs/reports/error_reference_inventory.md`
- `GPTs/reports/catalog_schema_extraction_rules.md`
- `GPTs/reports/source_inventory.md`
- `GPTs/reports/coverage_matrix.md`
- `GPTs/reports/gap_register.md`

## Design Note

This report is the error-reference counterpart to the property, SQL syntax, and
dictionary-view inventory baselines. It separates the shared error-family inventory and
response schema from later item-level expansion:

- `07_error_messages_troubleshooting.md` carries customer-facing response rules,
  common check SQL, representative blocks, and a compact family baseline.
- This report records source-family counts, source drift, schema requirements, and the
  J023-J026 work queue.
- `gap_register.md` remains the primary register for unresolved manual/source-backed
  gaps.

Later jobs must not infer cause, action, severity, `SQLSTATE`, or exact version support
from an error prefix alone. Use the exact source entry first, keep the customer's
literal runtime code and message, then add version-scoped cause/action and diagnostics.
When a grouped troubleshooting topic contains several codes, use an exact-code map
rather than relying on list order.

## Scoped Source Families

Primary source family:

- `error_message_reference`: exact error code, decimal code, reference symbol, message,
  severity heading, cause, and action.

Supporting source families for diagnostics and safe checks:

- `sql_reference`: corrected SQL, DDL/DCL, replication SQL, and syntax-sensitive action.
- `general_reference_1_datatypes_properties`: properties that control error behavior.
- `general_reference_2_dictionary_views`: dictionary and performance views used in
  check SQL.
- `replication_manual`: replication-state and topology checks for `rpERR_*`.
- `security_ssl_tls`: SSL/TLS certificate, port, and OpenSSL diagnostics.
- `isql_iloader`, `utilities_datacompj`, `c_cli_odbc_precompiler`,
  `dblink_hadoop_external_connectors`, and `log_analyzer`: tool and client contexts
  for utility, CLI/ODBC, DB Link, and Log Analyzer errors.

Korean source paths checked first:

- `Manuals/Altibase_7.1/kor/Error Message Reference.md`
- `Manuals/Altibase_7.3/kor/Error Message Reference.md`
- `Manuals/Altibase_trunk/kor/Error Message Reference.md`

English extraction paths checked second:

- `Manuals/Altibase_7.1/eng/Error Message Reference.md`
- `Manuals/Altibase_7.3/eng/Error Message Reference.md`
- `Manuals/Altibase_trunk/eng/Error Message Reference.md`

Known related reports:

- `GPTs/reports/eng_kor_parity.md`: keeps Korean source precedence for 8.1 JSON error
  detail and other known drift.
- `GPTs/reports/8_1_verification.md`: verifies 8.1 release-note features such as
  JSON, Temporary LOB, replication SSL, and JSON plan boundaries.
- `review/reports/R13_troubleshooting_errors.md`: records the prior troubleshooting
  quality review and sampled exact-code checks.

## Extraction Method

1. Use Korean Error Message Reference family chapters as the authoritative inventory
   source for 7.1, 7.3, and Altibase 8.1 verified source.
2. Count exact entries from source lines shaped like
   `0x... (decimal) <symbol> <message>` under a current family and severity heading.
3. Treat `FATAL`, `ABORT`, `IGNORE`, and `RETRY` as source severity headings for answer
   risk, not as complete operational severity levels.
4. Treat the Regular Expression Error Code chapter as an explanatory appendix unless it
   provides a separate exact `0x...` entry. In the checked sources, the exact PCRE2
   codes are represented in the `MT Error Code` family as `0x2106B` and `0x2106C`.
5. Use English manuals only for customer-facing wording when they agree with the
   Korean source. If English contains a family or entry absent from the paired Korean
   source, record source drift and avoid broad customer-facing version claims.
6. Do not convert decimal values, runtime `ERR-xxxxx` forms, or `SQLSTATE` values unless
   the source or customer-provided driver output supplies the mapping.

## Inventory Summary

Exact `0x...` entries counted from the checked Korean Error Message Reference files:

- 7.1 selected source: `2927` entries.
- 7.3 selected source: `2899` entries.
- Altibase 8.1 verified source: `2916` entries.

Severity notation below: `F` = `FATAL`, `A` = `ABORT`, `I` = `IGNORE`, `R` = `RETRY`.

| Error family | Typical symbols | Diagnosis lane | 7.1 Korean inventory | 7.3 Korean inventory | 8.1 Korean inventory | Later ownership |
| --- | --- | --- | --- | --- | --- | --- |
| ID Error Code | `idERR_*` | Infrastructure, OS calls, IPC, shared memory, semaphores, sockets, files, properties | 239 (`F71/A150/I18`) | 239 (`F71/A150/I18`) | 239 (`F71/A150/I18`) | J023/J025 by symptom; startup runbooks later |
| SM Error Code | `smERR_*` | Storage manager, transactions, locks, logs, data files, tablespaces, backup, recovery | 354 (`F49/A299/I2/R4`) | 357 (`F49/A302/I2/R4`) | 357 (`F49/A302/I2/R4`) | J023 |
| MT Error Code | `mtERR_*` | Data types, conversion, literals, date/time, regular expression, JSON type support | 107 (`F8/A95/I4`) | 107 (`F8/A95/I4`) | 108 (`F8/A96/I4`) | J024 |
| RP Error Code | `rpERR_*` | Replication definition, sender, receiver, sockets, handshake, sync, metadata | 358 (`F8/A338/I12`) | 390 (`F8/A369/I12/R1`) | 390 (`F8/A369/I12/R1`) | J025 |
| QP Error Code | `qpERR_*` | SQL parser, DDL, DML, metadata, objects, privileges, PSM, query execution | 851 (`F19/A827/R5`) | 857 (`F19/A833/R5`) | 873 (`F19/A849/R5`) | J023/J024 by topic |
| SD Error Code | `sdERR_*` | Sharding metadata, shard nodes, shard keys, shard SQL restrictions | 67 (`A67`) | Not listed | Not listed in the checked Korean source | J026 source-drift handling |
| ST Error Code | `stERR_*` | Spatial SQL and geometry operations | 78 (`F3/A74/I1`) | 79 (`F3/A75/I1`) | 79 (`F3/A75/I1`) | J026 residual or J039 spatial expansion |
| MM Error Code | `mmERR_*` | Main module, sessions, startup, shutdown, protocol, access mode | 155 (`F22/A124/I9`) | 156 (`F22/A125/I9`) | 156 (`F22/A125/I9`) | J025 and later operations runbooks |
| ODBC Error Code | `ulERR_*` | CLI/ODBC client connection, fetch, bind, LOB, SSL client settings | 152 (`F5/A135/I12`) | 142 (`F5/A125/I12`) | 142 (`F5/A125/I12`) | J025 and J036 |
| APRE Error Code | `ulpERR_*`, with related `ulERR_*` and `utERR_*` entries | Precompiler and embedded SQL diagnostics | 93 (`A93`) | 93 (`A93`) | 93 (`A93`) | J025 and J036 |
| Utilities Error Code | `utERR_*` | `isql`, `iloader`, utilities, display, file, communication, LOB utility behavior | 179 (`F6/A172/I1`) | 180 (`F6/A173/I1`) | 180 (`F6/A173/I1`) | J025 and J037 |
| CM Error Code | `cmERR_*` | Communication module, SSL/TLS context, certificates, socket I/O | 107 (`F6/A97/I2/R2`) | 112 (`F6/A102/I2/R2`) | 112 (`F6/A102/I2/R2`) | J025 |
| Database Link Error Code | `dkERR_*` | DB Link, AltiLinker, remote statements, global transactions, `dblink.conf` | 111 (`F2/A108/R1`) | 111 (`F2/A108/R1`) | 111 (`F2/A108/R1`) | J025 and J038 |
| Log Analyzer Error Code | `ulaERR_*` | Log Analyzer, CDC network/protocol, XLog processing | 76 (`F5/A37/I34`) | 76 (`F5/A37/I34`) | 76 (`F5/A37/I34`) | J025 and J032 |
| Regular Expression Error Code appendix | `ERR-2106C`, related `mtERR_*` PCRE2 entries | PCRE2 error-message pattern and regex syntax limitations | Appendix, no separate `0x...` entries counted | Appendix, no separate `0x...` entries counted | Appendix, no separate `0x...` entries counted | J024 |

## Source Drift Notes

- `SD Error Code`: the 7.1 Korean Error Message Reference lists `sdERR_*` entries. The
  checked 7.3 and Altibase 8.1 verified Korean Error Message Reference files do not
  list an `SD Error Code` chapter. The checked 8.1 English extraction aid does list
  `SD Error Code` entries. Because Korean source has precedence, customer-facing 7.3
  or 8.1 answers must not treat `sdERR_*` as verified for those versions without exact
  installed-version evidence. This is tracked as `GAP-J022-001`.
- APRE chapter prefix mix: the APRE chapter contains `91` `ulpERR_*` entries plus one
  `ulERR_*` and one `utERR_*` entry in each checked Korean source. Route by exact
  source entry and runtime context, not by prefix alone.
- Regular expression appendix: the appendix explains PCRE2 error categories and the
  `ERR-2106C` message pattern. The exact reference entries remain `0x2106B` and
  `0x2106C` under `MT Error Code`.
- 8.1 JSON errors: 8.1 JSON and Temporary LOB error entries such as `0x2106D` and
  `0x314BC` through `0x314CA` are backed by the 8.1 Korean Error Message Reference
  and prior parity notes. Keep these as Altibase 8.1 verified source material.

## Error Block Schema

Use this schema for every exact-code or grouped error block added by J023-J026. Keep
the block compact, but do not drop fields needed for safe diagnosis.

Required fields:

- Heading: human-searchable topic name and the most important literal code or symbol.
- Error Code: runtime form when known, reference `0x... (decimal)` form when known, and
  every exact code in a grouped block.
- Reference Symbol: exact symbol from the selected source.
- Module / Severity: source family and severity heading from the exact entry.
- Message: source-normalized message with placeholders preserved.
- Applies To: version scope, component, client/server/tool context, and feature scope.
- Symptom: customer-observable failure shape.
- Primary Causes: source-backed causes only.
- Immediate Action: ordered next action, with unsafe changes gated by evidence.
- Check SQL or Command: dictionary/view/property/log/utility check when source-backed.
- Required Customer Input: exact version, patch level, full error line, SQL or command,
  object definition, topology, certificate paths, OS error number, or log excerpt.
- Version Cautions: 7.1, 7.3, Altibase 8.1 verified source, exact patch, or
  verification-limited note.
- Escalation: evidence to collect before support escalation or destructive action.
- Related Document: attachment cross-reference or later-job owner.

Grouped blocks must include an exact-code map before generalized cause/action prose:

```text
| Runtime form | Reference code | Symbol | Message | Version scope | First check |
| --- | --- | --- | --- | --- | --- |
| `ERR-xxxxx` | `0x... (decimal)` | `...ERR_...` | `...` | `7.1`, `7.3`, or `Altibase 8.1 verified source` | `...` |
```

Do not infer missing map cells. Use `Unknown from the supplied message` when the source
or customer evidence does not provide a value.

## Troubleshooting Response Schema

Use this response order for customer answers:

1. Restate the exact error code, message, and context provided by the user.
2. Normalize the runtime form to the reference form only when the mapping is source
   backed.
3. Identify module and severity from the exact source entry. If the entry is not in the
   consolidated attachment blocks, say what is unknown instead of inventing it.
4. Give source-backed cause and action for the exact version scope.
5. Ask for missing inputs that affect diagnosis: version, patch, full error line, SQL
   or command, object definition, topology, properties, logs, OS error, or client/tool
   environment.
6. Provide the safest check SQL, command, or log inspection available from selected
   sources.
7. State stop conditions before restart, recovery, data movement, object drop,
   replication rebuild, certificate change, or property change.

Uncovered exact-code pattern:

```text
I do not have a consolidated block for `<customer_code>` in these attachments. Keep the
exact code and message as supplied. Cause and action beyond the supplied message are
`Unknown from the supplied message`. Please provide the Altibase version, patch level,
full error line, SQL or command, and relevant trace log excerpt; the safest next check
is <source-backed check>.
```

Log-only or symptom-only pattern:

```text
This symptom is not enough to choose an Altibase error entry. Please provide the exact
`ERR-xxxxx` or `0x...` line, Altibase version, failed SQL or command, and trace log
excerpt around the timestamp. Meanwhile, check <non-destructive source-backed command
or view>.
```

## Later-Job Handoff

| Job | Error slice | Required remediation shape |
| --- | --- | --- |
| J023 | Storage, backup, recovery, datafile, log, lock, and tablespace errors from `SM`, relevant `QP`, and relevant `ID` entries | Exact-code blocks with tablespace/datafile/log check SQL, backup/recovery stop conditions, and escalation evidence |
| J024 | SQL, DDL, data type, constraint, JSON, Temporary LOB, LOB, and regular expression errors from `QP`, `MT`, and related client/utility LOB entries | Exact-code maps for grouped topics, corrected SQL or object checks, JSON/Temporary LOB 8.1 scope, and non-invented conversion actions |
| J025 | Client, network, SSL/TLS, replication, utility, DB Link, Log Analyzer, APRE, and CLI/ODBC errors from `RP`, `MM`, `ODBC`, `APRE`, `Utilities`, `CM`, `DK`, and `ULA` | Component-specific evidence prompts, property/log checks, certificate and topology guardrails, and tool command checks |
| J026 | Error QA and unresolved gaps | Verify exact-code coverage, unresolved source drift, uncovered-code response quality, cross-links, and absence of unsafe prefix inference |

`GAP-J002-008` remains open after J022 for item-level exact-code expansion. J022 narrows
the gap by adding the family inventory and response schema. `GAP-J022-001` records the
`SD Error Code` source drift discovered during this baseline.

## J023 Completion Addendum

J023 used the `error_message_reference` source family for Altibase 7.1, Altibase 7.3,
and the Altibase 8.1 verified source, with Korean Error Message Reference manuals
checked first and matching English manuals used for customer-facing extraction. The
supporting diagnostic sources were `administrator_operations`, `sql_reference`,
`general_reference_1_datatypes_properties`, and `general_reference_2_dictionary_views`.

Design note: J023 keeps the attachment boundary unchanged and expands
`GPTs/attachments/07_error_messages_troubleshooting.md` in place. It does not move
backup/recovery runbooks, generated DDL, or view definitions into the error attachment;
instead, it adds grouped exact-code maps for the storage/error slice and links each
block back to `02_administration_operations.md`, `03_sql_ddl_generation.md`,
`05_data_types_properties.md`, and `06_data_dictionary_performance_views.md` for
copy-ready corrective SQL, property context, and validation queries.

J023 added customer-facing grouped blocks for:

- datafile and file-system storage errors from relevant `ID` and `SM` entries;
- backup, recovery, log, log-anchor, archive-mode, and `RESETLOGS` errors from `SM`;
- checkpoint-path, checkpoint-image, change-tracking, `backupInfo`, incremental-backup,
  and multiplex-directory errors from `SM`;
- tablespace state, type, capacity, lock, and DDL errors from `SM` and relevant `QP`
  entries.

No new source-drift gap was found in the scoped slice: the listed grouped-block codes
are present in the checked Korean 7.1, 7.3, and Altibase 8.1 verified source Error
Message References. `GAP-J002-008` remains open for the later J024-J026 error slices
and for exhaustive exact-code coverage outside the J023 grouped blocks.

## J024 Completion Addendum

J024 used the `error_message_reference` source family for Altibase 7.1, Altibase 7.3,
and the Altibase 8.1 verified source, with Korean Error Message Reference manuals
checked first and matching English manuals used only for customer-facing extraction
when consistent. Supporting source families for diagnostics and guardrails were
`sql_reference`, `general_reference_1_datatypes_properties`,
`general_reference_2_dictionary_views`, `c_cli_odbc_precompiler`,
`isql_iloader`, and `utilities_datacompj`.

Design note: J024 keeps the attachment boundary unchanged and expands
`GPTs/attachments/07_error_messages_troubleshooting.md` in place. Corrected SQL,
data type semantics, LOB API details, utility workflows, and JSON function syntax
remain routed to their owning attachments; the error attachment now carries grouped
exact-code maps, first checks, required customer input, and version cautions for the
J024 error slice.

J024 added customer-facing grouped blocks for:

- SQL parser, clause, and statement-shape errors from `QP/QCP`;
- table, column, data type, temporary-table, compression, and LOB DDL errors from
  `QP/QDB`;
- constraint definition, unique-index, check-constraint, and referential errors from
  `SM`, `QP/QDN`, `QP/QDB`, and `QP/QMX`;
- conversion, literal, numeric, date, and regular-expression errors from `MT`;
- ordinary LOB locator, SQL-shape, client/API, Precompiler, and utility LOB errors
  from `SM`, `QP`, `ODBC`, `APRE`, and `Utilities`;
- 8.1-scoped JSON and Temporary LOB errors from `MT` and `QP`.

No new source-drift gap was found in the scoped slice. The listed non-JSON grouped-block
codes are present in the checked Korean 7.1, 7.3, and Altibase 8.1 verified source
Error Message References except the explicitly noted SQL-level LOB autocommit code
`0x314B4`, which is checked in 7.3 and Altibase 8.1 verified source. JSON and Temporary
LOB codes remain Altibase 8.1 verified source material. `GAP-J002-008` remains open
for the later J025-J026 error slices and for exhaustive exact-code coverage outside the
J023-J024 grouped blocks.

## J025 Completion Addendum

J025 used the `error_message_reference` source family for Altibase 7.1, Altibase 7.3,
and the Altibase 8.1 verified source, with Korean Error Message Reference manuals
checked first and matching English manuals used only for customer-facing extraction
when consistent. Supporting source families for diagnostics and guardrails were
`replication_manual`, `security_ssl_tls`, `general_reference_2_dictionary_views`,
`isql_iloader`, `utilities_datacompj`, `c_cli_odbc_precompiler`,
`dblink_hadoop_external_connectors`, and `log_analyzer`.

Design note: J025 keeps the attachment boundary unchanged and expands
`GPTs/attachments/07_error_messages_troubleshooting.md` in place. Replication,
Log Analyzer, DB Link, CLI/ODBC, APRE, iSQL/iLoader, utility, and SSL/TLS procedures
remain routed to their owning attachments; the error attachment carries grouped
exact-code maps, first checks, required customer input, and version cautions for the
J025 error slice.

J025 expanded or confirmed customer-facing grouped coverage for:

- client session, protocol, NLS, task/session capacity, connection-string, and
  alternate-server errors from `MM`, `CM`, and `ODBC`;
- replication startup, disabled/denied/not-started state, self-replication, object
  eligibility, role/mode, metadata mismatch, conflict, timeout, and log-buffer errors
  from `RP`;
- client SSL and server/communication-module SSL certificate, private-key, CA,
  handshake, read/write, connect, OpenSSL library, and unsupported-version errors from
  `ODBC` and `CM`, including J025 evidence prompts and property checks;
- DB Link and `AltiLinker` configuration, network, ADLP protocol, buffer, and
  global-transaction errors from `DK`;
- iSQL, iLoader, and utility environment, syntax, option, file, NLS, CSV, data-parse,
  upload, and library-version errors from `Utilities`;
- APRE source file, declare-section, host-variable, indicator, option, connection,
  statement, and cursor errors from `APRE`;
- Log Analyzer metadata, network, protocol, link, table/column metadata, environment,
  and XLog-pool errors from `ULA`.

No new source-drift gap was found in the scoped slice. The listed grouped-block codes
are present in the checked Korean 7.1, 7.3, and Altibase 8.1 verified source Error
Message References, except that numeric `0x510xx` values are intentionally treated as
component-sensitive because ODBC/CLI, APRE, and Log Analyzer entries can share numeric
reference codes with different symbols and messages. `GAP-J002-008` remains open for
J026 QA and for exhaustive exact-code coverage outside the J023-J025 grouped blocks.
