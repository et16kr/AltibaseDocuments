# Altibase English/Korean Source Parity Report

Job: `JOB-012`
Phase: P1 Inventory
Status: Complete

Objective: compare English and Korean source quality for core manuals and document source precedence for GPT attachment construction.

## Source Precedence Decision

Korean Altibase manuals are the authoritative latest manual source. The local manual trees have broad English/Korean parity for the manuals required by `GPTs/reports/source_inventory.md`, but if a Korean manual and English manual differ, later jobs should treat the Korean manual as the source of truth and record the English-source drift as a source issue.

English remains the canonical attachment language for customer-facing GPT attachment files. Korean-source content must be translated and normalized into concise English attachment text, with source traceability kept in work reports and without exposing internal source labels in `GPTs/attachments/`.

For Altibase 8.1, customer-facing attachments must label the source family as "Altibase 8.1 verified source" or equivalent wording. Internal paths under `Manuals/Altibase_trunk/...` may appear in this work report only.

## Scope

Compared top-level Markdown manuals under these source roots:

- `Manuals/Altibase_7.1/eng` and `Manuals/Altibase_7.1/kor`
- `Manuals/Altibase_7.3/eng` and `Manuals/Altibase_7.3/kor`
- `Manuals/Altibase_trunk/eng` and `Manuals/Altibase_trunk/kor`
- `Manuals/Tools/Altibase_release/eng` and `Manuals/Tools/Altibase_release/kor`
- `Manuals/Tools/Altibase_trunk/eng` and `Manuals/Tools/Altibase_trunk/kor`

`README.md`, PDF folders, media folders, and Markdown media sidecars were excluded from the parity counts. Filename matching normalized smart apostrophes and the `General_Reference` versus `General Reference` spelling difference.

## Coverage Summary

| Source tree | Paired manuals | English-only manuals | Korean-only manuals | Source authority decision |
| --- | ---: | ---: | ---: | --- |
| Altibase 7.1 manuals | 30 | 0 | 1 | Korean authoritative when paired or conflicting. Korean-only `Sharding(deprecated).md` is not in the current attachment source inventory. |
| Altibase 7.3 manuals | 29 | 0 | 0 | Korean authoritative when paired or conflicting. |
| Altibase 8.1 verified source manuals | 29 | 0 | 0 | Korean authoritative when paired or conflicting, with known Korean-source detail cases listed below. |
| Tool manuals, release source | 6 | 0 | 0 | Korean authoritative when paired or conflicting. |
| Tool manuals, Altibase 8.1 verified source | 6 | 0 | 0 | Korean authoritative when paired or conflicting. |
| Total | 100 | 0 | 1 | Korean manual source authority is accepted; English remains the normalized attachment language. |

## Source Quality Findings

- English manual coverage is complete for the core manual set used by the 20 planned attachments, but English is not authoritative when a paired Korean manual differs.
- Known conflict decision: Korean 7.1, 7.3, and Altibase 8.1 verified source General Reference manuals list the `FLOAT` range as `-1E-120` through `1E+120`, while English extraction had used `-1E+120` as the lower bound. Attachment `05_data_types_properties.md` should use the Korean-source lower bound for the covered versions.
- Korean manuals generally pair with the same document families and are often slightly longer. Korean manual authority comes from the project source policy, not from line count alone.
- Checked English manual roots had no `C:/` or `file://` matches.
- Korean source roots contain absolute Windows or `file://` links in these files and should not be copied directly into attachments:
  - `Manuals/Altibase_7.1/kor/SQL Reference.md:11995`
  - `Manuals/Altibase_7.1/kor/SQL Reference.md:11999`
  - `Manuals/Altibase_7.1/kor/SQL Reference.md:12003`
  - `Manuals/Altibase_7.1/kor/Hadoop Connector User's Manual.md:320`
  - `Manuals/Altibase_7.3/kor/Hadoop Connector User's Manual.md:326`
  - `Manuals/Altibase_trunk/kor/SQL Reference.md:12218`
  - `Manuals/Altibase_trunk/kor/SQL Reference.md:12222`
  - `Manuals/Altibase_trunk/kor/SQL Reference.md:12226`
  - `Manuals/Altibase_trunk/kor/Hadoop Connector User's Manual.md:325`
- Both English and Korean SQL manuals rely heavily on syntax diagram images. Later SQL jobs should convert the needed syntax diagrams into compact BNF-like text or Mermaid instead of preserving image dependencies.

## 8.1 Korean Source Detail Register

These are known cases where English should remain the attachment language, but Korean source should be used as the source of technical detail after translation and normalization. The same Korean-source precedence applies to any later-discovered Korean/English conflict.

| Area | English status | Korean source with detail | Attachment impact |
| --- | --- | --- | --- |
| JSON data type | 8.1 English release notes confirm the feature, but targeted checks found no substantive English manual section for the type. | `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md:2741` and following. | JOB-038 should use English release notes for the high-level claim and Korean General Reference for normalized data type details. |
| JSON functions and `IS JSON` | 8.1 English SQL Reference does not contain the JSON function sections found in Korean. | `Manuals/Altibase_trunk/kor/SQL Reference.md:23604`, `:23618`, `:23681`, `:23758`, `:23839`, `:23969`, `:23999`, `:26496`. | JOB-037 and JOB-038 should translate and compress syntax/function behavior into English attachment text. |
| Temporary LOB | 8.1 English manuals do not contain `Temporary LOB`, `TEMPORARY_LOB_ENABLE`, `MEMORY_TEMPLOB_*`, or `V$TEMPORARY_LOBS` detail. | `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md:2617`, `:16014`, `:16038`, `:16549`; `Manuals/Altibase_trunk/kor/General_Reference-2.The Data Dictionary.md:11665`; `Manuals/Altibase_trunk/kor/SQL Reference.md:16174`. | JOB-038 and JOB-039 should translate the Temporary LOB behavior, properties, and view block. |
| Replication SSL | English SSL guide covers client/server SSL, but English replication/property manuals lack the replication-specific `USING SSL` and `REPLICATION_SSL_PORT_NO` detail. | `Manuals/Altibase_trunk/kor/Replication Manual.md:1110`, `:1188`, `:1198`; `Manuals/Altibase_trunk/kor/General_Reference-1.Data Types & Altibase Properties.md:12373`; `Manuals/Altibase_trunk/kor/SQL Reference.md:6877`. | JOB-035, JOB-044, and JOB-045 should separate general SSL/TLS from replication SSL and translate Korean source details. |
| JSON error messages | 8.1 English Error Message Reference did not match targeted JSON error symbols. | `Manuals/Altibase_trunk/kor/Error Message Reference.md:5109`, `:14893` through `:14977`. | JOB-042 should add JSON error blocks from Korean source detail if JSON troubleshooting is included. |
| CLI JSON LOB cleanup | 8.1 English CLI manual did not match `SQLFreeLob2`. | `Manuals/Altibase_trunk/kor/CLI User's Manual.md:8169` through `:8202`. | JOB-052 should include `SQLFreeLob2` only after translating and tying it to JSON/LOB update guidance. |
| JSON-formatted execution plan | 8.1 English release notes confirm JSON plan output and property names, but neither English nor Korean manuals had substantive manual coverage in JOB-011 checks. | No detailed manual source found. | JOB-043 should keep JSON plan wording narrow and avoid inventing output schema or examples. |

## Attachment-Level Extraction Notes

This table records convenient English extraction paths. Korean manual precedence overrides these notes when paired Korean and English manuals conflict.

| Attachment | Primary extraction notes | Korean source authority action |
| --- | --- | --- |
| `00_version_release_platform.md` | English release notes and English supported-platform sources. | Check Korean release notes when release-note content differs. |
| `01_getting_started_installation.md` | English Getting Started and Installation guides for 7.1, 7.3, and Altibase 8.1 verified source. | Use Korean manuals as conflict authority. |
| `02_administration_operations.md` | English Administrator manuals. | Use Korean manuals as conflict authority. |
| `03_sql_ddl_generation.md` | English SQL Reference, General Reference, and Replication Manual. | Use Korean source detail for 8.1 JSON type, Temporary LOB-related SQL, and replication SSL clauses, and for any later conflict. |
| `04_sql_dml_oracle_compatibility.md` | English SQL Reference. | Use Korean source detail for 8.1 JSON function and `IS JSON` sections, and for any later conflict. |
| `05_data_types_properties.md` | English General Reference and English release notes. | Use Korean source detail for 8.1 JSON, Temporary LOB, and related properties, and for any later conflict. |
| `06_data_dictionary_performance_views.md` | English Data Dictionary. | Use Korean source detail for `V$TEMPORARY_LOBS`, and for any later conflict. |
| `07_error_messages_troubleshooting.md` | English Error Message Reference. | Use Korean source detail for 8.1 JSON-related error messages if included, and for any later conflict. |
| `08_performance_tuning_monitoring.md` | English Performance Tuning, Monitoring API, and SNMP manuals. | No detailed Korean manual source was found for JSON plan; rely only on release-note-level claims unless later Korean source is found. |
| `09_replication_ha_cdc.md` | English Replication Manual, Log Analyzer, and Replication Manager manuals. | Use Korean source detail for 8.1 replication SSL. Korean-only technical documents from JOB-010 remain supplemental. |
| `10_psm_stored_external_procedures.md` | English Stored Procedures and External Procedures manuals. | Use Korean manuals as conflict authority. |
| `11_java_jdbc_spring.md` | English JDBC and Adapter for JDBC manuals, plus English third-party guides. | Use Korean JDBC and Adapter manuals as authority for literal URL grammar and Adapter patch-version drift. Korean-only Java compatibility technical document from JOB-010 remains supplemental outside the manual parity scope. |
| `12_c_cli_odbc_precompiler.md` | English CLI, ODBC, Altibase C Interface, and Precompiler manuals. | Use Korean source detail for `SQLFreeLob2` if JSON LOB update guidance is required, and for any later conflict. |
| `13_isql_iloader_basic_tools.md` | English iSQL and iLoader manuals. | Use Korean manuals as conflict authority. |
| `14_utilities_operation_tools.md` | English Utilities and English tool manuals. | Use Korean manuals as conflict authority. |
| `15_migration_oracle_compatibility.md` | English Adapter for Oracle and Migration Center manuals. | Use Korean manuals as conflict authority; `TODO` text in Migration Center examples is a product rule label, not a work-item marker. |
| `16_dblink_external_connectors.md` | English DB Link, Hadoop Connector, and third-party connector manuals. | Use Korean DB Link manuals as authority for Homogeneous Link support and `AltiLinker` JRE details. Use the Korean Java compatibility note and 8.1 release note for DB Link Java runtime guidance. Do not copy Korean Hadoop `file://` link text directly. |
| `17_kubernetes_aku_cloud.md` | English Kubernetes/AKU guides and English release notes from JOB-010. | Use Korean manuals as conflict authority where paired manuals exist. |
| `18_security_ssl_tls.md` | English SSL/TLS guide and English release notes. | Use Korean source detail for replication SSL, not for ordinary client/server SSL unless a Korean/English conflict is found. |
| `19_spatial_nifi_tableau_misc.md` | English Spatial SQL Reference, altiShapeLoader, NiFi, and Tableau sources. | Use Korean manuals as conflict authority. |

## Rules For Later Jobs

- Check Korean manuals for version-sensitive claims, especially when an English claim is surprising, incomplete, or contradicted by another source.
- If English and Korean manuals conflict, prefer the Korean manual for 7.1, 7.3, and Altibase 8.1 verified source.
- Use English release notes for release-note-only feature existence when no Korean release-note conflict is known, but use Korean manuals for detailed manual behavior when available.
- Do not place Korean prose directly into final attachment files. Translate and normalize it into concise English source blocks.
- Keep SQL object names, function names, error codes, properties, commands, and file paths literal.
- Do not copy absolute Windows paths, `file://` links, or internal source labels into `GPTs/attachments/`.

## Verification Commands

Representative commands used:

```bash
find Manuals -path '*/eng/*.md' -o -path '*/kor/*.md'
find Manuals -path '*/eng/*.md' -o -path '*/kor/*.md' | while IFS= read -r f; do lines=$(wc -l < "$f"); imgs=$(rg -n '!\[[^]]*\]\(' "$f" | wc -l); paths=$(rg -n 'C:/|file://' "$f" | wc -l); printf '%s\t%s\t%s\t%s\n' "$lines" "$imgs" "$paths" "$f"; done
rg -n "C:/|file://" Manuals/Altibase_7.1/eng Manuals/Altibase_7.3/eng Manuals/Altibase_trunk/eng Manuals/Tools/Altibase_release/eng Manuals/Tools/Altibase_trunk/eng || true
rg -n "C:/|file://" Manuals/Altibase_7.1/kor Manuals/Altibase_7.3/kor Manuals/Altibase_trunk/kor Manuals/Tools/Altibase_release/kor Manuals/Tools/Altibase_trunk/kor
rg -n -i "json|temporary lob|temporary_lob|templob|V\$TEMPORARY_LOBS|MEMORY_TEMPLOB|USING SSL|REPLICATION_SSL_PORT_NO|TRCLOG_EXPLAIN_TYPE|TRCLOG_JSON_PLAN_INDENT_DEPTH" Manuals/Altibase_trunk/eng Manuals/Altibase_trunk/kor
rg -n "SQLFreeLob2|JSON data|LOB Locator" "Manuals/Altibase_trunk/eng/CLI User's Manual.md" "Manuals/Altibase_trunk/kor/CLI User's Manual.md"
rg -n "qpERR_ABORT_JSON|mtERR_ABORT_JSON|JSON_WITHOUT_TEMPLOB|JSON_INVALID" "Manuals/Altibase_trunk/eng/Error Message Reference.md" "Manuals/Altibase_trunk/kor/Error Message Reference.md"
```

## Conclusion

`JOB-012` acceptance criteria are updated for the current source policy. Korean manuals are the default source authority when paired Korean and English manuals differ, while English remains the normalized attachment language.
