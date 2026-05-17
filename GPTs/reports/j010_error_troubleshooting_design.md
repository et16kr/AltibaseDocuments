# J010 Error Troubleshooting Remediation Design Note

Date: 2026-05-17

## Scope

J010 strengthens customer-facing error and troubleshooting content in:

- `GPTs/attachments/07_error_messages_troubleshooting.md`
- `GPTs/attachments/13_isql_iloader_basic_tools.md`
- `GPTs/attachments/14_utilities_operation_tools.md`

The job does not change original manuals, benchmark thresholds, question wording, or
unsupported Altibase behavior.

## Design

The main structure change is a compact answer-ready index near the top of
`07_error_messages_troubleshooting.md`. The index duplicates high-risk exact tokens
already supported by detailed blocks so lexical retrieval can surface the literal code,
symbol, message, cause/action focus, and first check in one place.

The detailed blocks remain the authoritative local attachment sections for full SQL,
commands, version cautions, and escalation inputs. The index is a routing and answer
synthesis aid, not a replacement for those sections.

## Source Basis

The edited facts were checked against repository-local selected sources, especially:

- Altibase 7.3 Korean and English Utilities Manual: `altierr`, `dumptrc`, and iLoader
  diagnostic options.
- Altibase 7.3 Korean and English Error Message Reference: `0x0001F`, `0x31010` family,
  `0x31363`, `0x6100D`, `0x61010`, `0x6102D`, `0x710A0`, and `0x710A3`.
- Altibase 8.1 verified source Error Message Reference: JSON and OpenSSL-related
  error blocks where 8.1 scope is stated.

## Safety Rules Preserved

- Preserve runtime and reference forms together when known, for example `ERR-31363`
  and `0x31363 (201571)`.
- Ask for version, patch level, exact SQL or command, object definitions, trace logs,
  and tool/client versions before recommending destructive, recovery, replication, or
  TLS changes.
- Keep JSON-specific error blocks scoped to Altibase 8.1 verified source unless the
  customer supplies exact installed-version evidence.
