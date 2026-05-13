# Altibase 8.1 Source Verification

Job: `JOB-011`
Phase: P1 Inventory
Status: Complete

Objective: verify Altibase 8.1 source content against the 8.1 release notes for the required feature set: JSON, Temporary LOB, replication SSL, and JSON plan.

## Scope

- Release notes checked: `ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md`
- English 8.1 verified source manuals checked: `Manuals/Altibase_trunk/eng`
- Korean 8.1 source fallback checked where English coverage was missing: `Manuals/Altibase_trunk/kor`
- Prior inventory dependency: `GPTs/reports/source_inventory.md`

The report is an internal work document. Customer-facing attachments should cite this source family as "Altibase 8.1 verified source" and should not expose the internal directory label.

## Summary

| Feature | Release notes claim | English 8.1 manual coverage | Korean fallback coverage | Verification result |
| --- | --- | --- | --- | --- |
| JSON data type and JSON functions | Present at release notes lines 68-81; functions listed as `JSON_ARRAY`, `JSON_OBJECT`, `JSON_EXISTS`, `JSON_QUERY`, `JSON_VALUE`, `JSON_VALID` | Not found in English 8.1 manuals by targeted search, except unrelated `.json` text and generic SSL lines | Present in Korean General Reference and SQL Reference | Release-note claim verified; English canonical manual gap documented |
| Temporary LOB | Present at release notes lines 83-96; properties and `V$TEMPORARY_LOBS` listed at lines 324-328 and 374 | Not found in English 8.1 manuals by targeted search | Present in Korean General Reference, SQL Reference, and Data Dictionary | Release-note claim verified; English canonical manual gap documented |
| Replication SSL | Present at release notes lines 133-138; `REPLICATION_SSL_PORT_NO` listed at line 326 | English SSL guide covers client/server SSL, but English replication/property manuals do not show `USING SSL` or `REPLICATION_SSL_PORT_NO` replication detail | Present in Korean Replication Manual, SQL Reference, and General Reference | Release-note claim verified; English canonical manual gap documented |
| JSON-formatted execution plan | Present at release notes lines 231-233; `TRCLOG_EXPLAIN_TYPE` and `TRCLOG_JSON_PLAN_INDENT_DEPTH` listed at lines 329-330 | Not found in English 8.1 manuals by targeted search | Not found in Korean 8.1 manuals by targeted search | Release-note-only; do not invent JSON plan schema from manuals |

## Detailed Findings

### JSON

Release notes confirm that Altibase 8.1 adds a native `JSON` data type, supports JSON path expressions, and lists `JSON_ARRAY`, `JSON_OBJECT`, `JSON_EXISTS`, `JSON_QUERY`, `JSON_VALUE`, and `JSON_VALID` (`ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md:68`, `:70`, `:72`, `:74`-`:79`).

Targeted searches over `Manuals/Altibase_trunk/eng` did not find substantive English manual coverage for `JSON`, `JSON_ARRAY`, `JSON_OBJECT`, `JSON_EXISTS`, `JSON_QUERY`, `JSON_VALUE`, `JSON_VALID`, or `IS JSON`. The only English hits were unrelated `.json` package output and generic SSL content.

Korean source contains the missing detail:

- `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md:2741` starts the JSON data type section.
- `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md:2745` states the `JSON` maximum size as 2 GB.
- `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md:2749`-`:2751` cites RFC 8259 and ISO/IEC 19075-6.
- `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md:2766` shows compact syntax: `JSON [ IN ROW size ]`.
- `Manuals/Altibase_trunk/kor/SQL Reference.md:23604`-`:23616` lists JSON function categories and function names.
- `Manuals/Altibase_trunk/kor/SQL Reference.md:26496` documents `IS JSON`.

Attachment impact: use the English release notes for canonical high-level JSON claims. If later jobs need full syntax/function behavior, translate and normalize the Korean source into English canonical attachment text with source traceability retained only in work docs.

### Temporary LOB

Release notes confirm Temporary LOB support, session and transaction Temporary LOB categories, common creation cases such as `TO_CLOB`, `TO_BLOB`, `SUBSTR`, and `CONCAT`, and `V$TEMPORARY_LOBS` for inspection (`ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md:83`-`:96`). The release notes also list `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`, `MEMORY_TEMPLOB_PIECE_SIZE`, `TEMPORARY_LOB_ENABLE`, and `V$TEMPORARY_LOBS` (`:324`-`:328`, `:374`).

Targeted searches over `Manuals/Altibase_trunk/eng` did not find substantive English manual coverage for `Temporary LOB`, `TEMPORARY_LOB_ENABLE`, `MEMORY_TEMPLOB_*`, or `V$TEMPORARY_LOBS`.

Korean source contains the missing detail:

- `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md:2617` starts the Temporary LOB section.
- `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md:2619` links Temporary LOB usage to `TEMPORARY_LOB_ENABLE` and `V$TEMPORARY_LOBS`.
- `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md:2634`-`:2638` compares transaction and session Temporary LOB behavior.
- `Manuals/Altibase_trunk/kor/SQL Reference.md:16174`-`:16206` documents `ALTER SESSION SET FREE TEMPORARY LOB`.
- `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md:11665`-`:11674` documents `V$TEMPORARY_LOBS` columns.
- `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md:16014`, `:16038`, and `:16549` document `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`, `MEMORY_TEMPLOB_PIECE_SIZE`, and `TEMPORARY_LOB_ENABLE`.

Attachment impact: do not rely on older English LOB sections as if they covered Temporary LOB. Use release notes for canonical English claims, and use Korean fallback only after translating and normalizing to English.

### Replication SSL

Release notes confirm SSL/TLS support for replication communication, the `USING SSL` clause for replication creation, and the `REPLICATION_SSL_PORT_NO` property (`ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md:133`-`:138`, `:326`).

English source status:

- `Manuals/Altibase_trunk/eng/Altibase SSL TLS User's Guide.md` covers general SSL client/server configuration.
- Targeted searches did not find `USING SSL` or `REPLICATION_SSL_PORT_NO` in English `Replication Manual.md`, `SQL Reference.md`, or `General Reference-1.Data Types & Altibase Properties.md`.

Korean source contains the missing replication-specific detail:

- `Manuals/Altibase_trunk/kor/Replication Manual.md:1110` maps SSL replication communication to `REPLICATION_SSL_PORT_NO`.
- `Manuals/Altibase_trunk/kor/Replication Manual.md:1188` and `:1198` show `CREATE REPLICATION ... USING SSL` examples.
- `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md:12373` documents `REPLICATION_SSL_PORT_NO`.
- `Manuals/Altibase_trunk/kor/SQL Reference.md:6877` also maps SSL communication to `REPLICATION_SSL_PORT_NO`.

Attachment impact: when building replication and SSL/TLS attachments, separate ordinary client/server SSL from replication SSL. For replication SSL commands, the release notes plus Korean fallback are the current source basis.

### JSON Plan

Release notes confirm support for outputting execution plans in JSON format (`ReleaseNotes/eng/Altibase_8_1_0_0_1_Release_Notes.md:231`-`:233`). The release notes list `TRCLOG_EXPLAIN_TYPE` and `TRCLOG_JSON_PLAN_INDENT_DEPTH` as new properties (`:329`-`:330`).

Targeted searches over both English and Korean 8.1 manual trees did not find substantive manual coverage for `TRCLOG_EXPLAIN_TYPE`, `TRCLOG_JSON_PLAN_INDENT_DEPTH`, "JSON plan", or execution plans in JSON format.

Attachment impact: future performance attachment work may state that 8.1 release notes add JSON-formatted execution plan output and the two property names above. It should not describe JSON object schema, property values, or output examples unless a later source is located.

## Source Gap Register

| Gap | Risk | Suggested follow-up job impact |
| --- | --- | --- |
| English 8.1 manuals lack JSON and Temporary LOB details found in Korean manuals | English-only extraction would omit 8.1 data type features | JOB-012 should flag these as Korean-source-backed English canonicalization candidates; JOB-038 should include translated, normalized JSON and Temporary LOB content |
| English 8.1 replication/property manuals lack replication SSL detail found in Korean manuals | Attachments could confuse general SSL with replication SSL | JOB-044 and JOB-045 should use release notes plus Korean fallback for `USING SSL` and `REPLICATION_SSL_PORT_NO` |
| JSON plan is release-note-only in both English and Korean manual trees | Risk of over-specifying unsupported details | JOB-043 should keep JSON plan wording narrow unless additional source appears |

## Verification Commands

Representative commands used:

```bash
rg -n -i "json|json_array|json_object|json_exists|json_query|json_value|json_valid|is json|temporary lob|temporary_lob|templob|V\\$TEMPORARY_LOBS|MEMORY_TEMPLOB|TRCLOG_EXPLAIN_TYPE|TRCLOG_JSON_PLAN_INDENT_DEPTH|USING SSL|REPLICATION_SSL_PORT_NO" Manuals/Altibase_trunk/eng
rg -n -i "json|temporary lob|temporary_lob|templob|V\\$TEMPORARY_LOBS|MEMORY_TEMPLOB|TRCLOG_EXPLAIN_TYPE|TRCLOG_JSON_PLAN_INDENT_DEPTH|USING SSL|REPLICATION_SSL_PORT_NO" Manuals/Altibase_trunk/kor
git grep -n -i -E "TRCLOG_EXPLAIN_TYPE|TRCLOG_JSON_PLAN_INDENT_DEPTH|json plan|json-formatted execution|json format|execution.*json|plan.*json" HEAD -- Manuals/Altibase_trunk/eng Manuals/Altibase_trunk/kor
git grep -n -i -E "json|json_array|json_object|json_exists|json_query|json_value|json_valid|is json|temporary lob|temporary_lob|templob|V\\$TEMPORARY_LOBS|MEMORY_TEMPLOB|TRCLOG_EXPLAIN_TYPE|TRCLOG_JSON_PLAN_INDENT_DEPTH|USING SSL|REPLICATION_SSL_PORT_NO" HEAD -- Manuals/Altibase_trunk/eng
```

The committed `HEAD` check produced the same English-manual gap pattern as the working tree check, so the pre-existing local edit in the English Performance Tuning Guide did not affect the JSON plan result.
