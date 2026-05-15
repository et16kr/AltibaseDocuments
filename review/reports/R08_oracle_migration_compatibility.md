# R08 Oracle Migration Compatibility and Conversion-Risk Framing

Date: 2026-05-16
Reviewer: Codex
Verdict: Pass

## Scope

- Attachments:
  - `GPTs/attachments/15_migration_oracle_compatibility.md`
  - `GPTs/attachments/04_sql_dml_oracle_compatibility.md`
- Supporting reports:
  - `GPTs/reports/source_inventory.md`
  - `GPTs/reports/8_1_verification.md`
  - `GPTs/reports/eng_kor_parity.md`
- Source manuals sampled:
  - `Manuals/Tools/Altibase_trunk/kor/Migration Center User's Manual.md`
  - `Manuals/Tools/Altibase_release/kor/Migration Center User's Manual.md`
  - `Manuals/Altibase_7.1/kor/Adapter for Oracle User's Manual.md`
  - `Manuals/Altibase_7.3/kor/Adapter for Oracle User's Manual.md`
  - `Manuals/Altibase_trunk/kor/Adapter for Oracle User's Manual.md`
  - `ReleaseNotes/kor/Altibase_Migration_Center_7_19_Release_Notes.md`
  - `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`

## Commands Run

```bash
bash review/scripts/run_review_remediation_cycle.sh status
rg -n $'\t(Reviewing|Remediating|ReReviewing|Fail)$' review/review_remediation_cycle_status.tsv
git status --short
sed -n '1,240p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,220p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,240p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
git diff -- GPTs/attachments/15_migration_oracle_compatibility.md GPTs/attachments/04_sql_dml_oracle_compatibility.md GPTs/reports/source_inventory.md review/review_remediation_cycle_status.tsv review/review_stage_status.tsv
rg -n "^#|Option block|Object support|Data type|Default|Adapter|oraAdapter|PSM|Migration Center|Oracle|JSON|Invisible|Foreign Key|Keep Partition|FORCE|Validation|Reconcile|RunReport|sqlconv|LOB|5\.5\.1|6\.5\.1|7\.1\.0\.7\.0" GPTs/attachments/15_migration_oracle_compatibility.md
rg -n "^#|Oracle|migration|compatibility|difference|RETURN|MERGE|LOB|JSON|ROWNUM|LIMIT|sequence|function|SYSDATE|NVL|DECODE|REGEXP|manual review|unsupported|Altibase-specific" GPTs/attachments/04_sql_dml_oracle_compatibility.md
rg -n "R08|Oracle migration|Migration Center|Adapter for Oracle" review/review_stages.tsv review/review_stage_status.tsv review/review_remediation_cycle_status.tsv
rg --files Manuals/Altibase_7.1/kor Manuals/Altibase_7.3/kor Manuals/Altibase_trunk/kor Manuals/Tools/Altibase_release/kor Manuals/Tools/Altibase_trunk/kor ReleaseNotes/kor | rg "(Adapter for Oracle User's Manual|Migration Center User's Manual|Migration Center|Release_Notes)"
rg -n "Oracle|오라클|Migration Center|마이그레이션|oraAdapter|JSON|PSM|Data Validation|DIFF|FILESYNC|Adapter for Oracle" GPTs/reports/source_inventory.md GPTs/reports/8_1_verification.md GPTs/reports/eng_kor_parity.md
nl -ba GPTs/attachments/15_migration_oracle_compatibility.md | sed -n '223,380p'
nl -ba GPTs/attachments/15_migration_oracle_compatibility.md | sed -n '397,610p'
nl -ba GPTs/attachments/15_migration_oracle_compatibility.md | sed -n '728,1090p'
nl -ba GPTs/attachments/04_sql_dml_oracle_compatibility.md | sed -n '23,42p'
nl -ba GPTs/attachments/04_sql_dml_oracle_compatibility.md | sed -n '1070,1124p'
rg -n "Foreign Key Migration|PSM Migration|Drop Existing Objects|Keep Partition Table|Use Double-quoted Identifier|Remove FORCE|Invisible Column|Postfix|Batch Execution|Batch Size|Batch LOB|Convert Oversized|Correction Factor|Data Validation|Include LOB|Data Sampling" "Manuals/Tools/Altibase_trunk/kor/Migration Center User's Manual.md"
rg -n "Build User|Build Table|Table|Primary Key|Unique|Check|Foreign Key|Index|Sequence|Synonym|Procedure|Function|Package|View|Materialized View|Trigger|IS JSON|Invisible|scalable|global temporary|external|hybrid|blockchain|immutable" "Manuals/Tools/Altibase_trunk/kor/Migration Center User's Manual.md"
rg -n "JSON|CLOB|IS JSON|NCLOB|ROWID|DEFAULT ON NULL|DBTIMEZONE|SYS_GUID|UID|USER|BINARY DOUBLE|TIMESTAMP|VARCHAR2|Convert Oversized String|Replace Default Empty String|EMPTY_STRING|NOT NULL|LOB" "Manuals/Tools/Altibase_trunk/kor/Migration Center User's Manual.md"
rg -n "Altibase.*5\.5\.1|Altibase.*6\.5\.1|Oracle.*10g|LOB|7\.1\.0\.7\.0|ADAPTER_LOB_TYPE_SUPPORT|ORACLE_ERROR_RETRY_COUNT|ORACLE_SKIP_ERROR|ORACLE_ARRAY_DML_MAX_SIZE|SELECT FOR UPDATE|REPLICATION_MAX_COUNT|DDL|FOR ANALYSIS|primary key|기본키" "Manuals/Altibase_7.1/kor/Adapter for Oracle User's Manual.md" "Manuals/Altibase_7.3/kor/Adapter for Oracle User's Manual.md" "Manuals/Altibase_trunk/kor/Adapter for Oracle User's Manual.md"
rg -n "10gR2|21c|6\.5\.1|7\.8|JDBC|JSON|IS JSON|Invisible|External|Hybrid|Blockchain|Immutable|LOB|Data Validation|FILESYNC|DIFF" ReleaseNotes/kor/Altibase_Migration_Center_7_19_Release_Notes.md ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md
nl -ba "Manuals/Tools/Altibase_trunk/kor/Migration Center User's Manual.md" | sed -n '930,1016p'
nl -ba "Manuals/Tools/Altibase_trunk/kor/Migration Center User's Manual.md" | sed -n '1068,1088p'
nl -ba "Manuals/Tools/Altibase_trunk/kor/Migration Center User's Manual.md" | sed -n '1208,1230p'
nl -ba "Manuals/Tools/Altibase_trunk/kor/Migration Center User's Manual.md" | sed -n '2056,2071p'
nl -ba "Manuals/Tools/Altibase_trunk/kor/Migration Center User's Manual.md" | sed -n '2160,2243p'
rg -n "^Verdict:|^\| (Blocker|High|Medium|Low) \|" review/reports/R08_oracle_migration_compatibility.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name README.md | wc -l
rg -n "trunk|file://|C:/|/home/|media/" GPTs/attachments/15_migration_oracle_compatibility.md GPTs/attachments/04_sql_dml_oracle_compatibility.md
git diff --check
git status --short
```

## Findings

No actionable `Blocker`, `High`, `Medium`, or `Low` findings remain for R08.

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Note | `GPTs/attachments/15_migration_oracle_compatibility.md` | 241 | Previously reported R08 issues were remediated: `PSM Migration` now states the DB-to-DB and DB-to-File defaults as `Yes`, keeps semantic review cautions, splits `oraAdapter` Altibase prerequisites between 7.1 and 7.3/8.1, and adds the Adapter `7.1.0.7.0` LOB support boundary. | No further attachment change is required for this stage. Keep the manual-review cautions in future edits. |

## Source Checks

- Claims checked:
  - Migration Center 7.19 source/target scope: Oracle Database `10gR2` through `21c`; target Altibase `6.5.1` or later.
  - Migration Center flow: Prepare, Build, Reconcile, Run, Data Validation; GUI Reconcile versus CLI default behavior.
  - Migration options: `Foreign Key Migration`, `PSM Migration`, `Drop Existing Objects`, `Keep Partition Table`, `Use Double-quoted Identifier`, `Remove FORCE from View DDL`, `Invisible Column Migration`, `Batch Execution`, `Batch Size`, `Batch LOB type`, oversized `VARCHAR` conversion, character correction factor, and Data Validation options.
  - Oracle object migration matrix: tables, constraints, indexes, sequences, private synonyms, procedures, functions, packages, views, materialized views, triggers, and Oracle-specific table/index/JSON caveats.
  - Oracle-to-Altibase type/default conversion: `CHAR`, `NCHAR`, `VARCHAR2`, `NVARCHAR2`, `LONG`, `NUMBER`, `BINARY DOUBLE`, `TIMESTAMP`, `RAW`, `LONG RAW`, `BLOB`, `CLOB`, `NCLOB`, `ROWID`, `JSON`, empty strings, `DBTIMEZONE`, `SYS_GUID()`, `UID`, `USER`, identity defaults, and `DEFAULT ON NULL`.
  - `oraAdapter` purpose, prerequisites, properties, DDL behavior, offline behavior, LOB constraints, and data type mapping.
- Source coverage:
  - Main Migration Center conversion-risk guidance is supported by the Korean trunk Migration Center manual, with 7.19 tool-version scope confirmed by Korean release notes.
  - 8.1 JSON claims are supported by Korean 8.1 release notes and the Korean Migration Center manual's JSON conversion row.
  - `oraAdapter` prerequisite and LOB boundaries are supported by Korean Adapter manuals for 7.1, 7.3, and 8.1 verified source.
- Korean/English source conflicts:
  - No new Korean/English conflict was found in this R08 re-review. Existing `eng_kor_parity.md` still correctly records that this attachment should treat Korean Migration Center and Adapter manuals as conflict authority.
- Source gaps:
  - No blocking source gap found for this stage. The remaining risk is normal migration-tool condensation: the attachment does not reproduce every PSM converter rule, but it gives source-backed report files and manual-review triggers for customer answers.

## Oracle-Overlap Decision

- Correctly compressed:
  - `04_sql_dml_oracle_compatibility.md` keeps generic Oracle-like DML brief and moves risky behavior into classifier rows for Altibase syntax checks, semantic differences, and non-parity features.
  - `15_migration_oracle_compatibility.md` focuses on Migration Center, Oracle object support, data type/default conversion, validation, and `oraAdapter`, rather than generic Oracle usage.
- Too much generic Oracle material:
  - None found.
- Missing Altibase-specific difference:
  - None found after the current remediation. The attachment preserves the key Altibase-specific cautions for volatile tablespaces, disk allocation, JSON version behavior, LOB `NOT NULL`, empty-string handling, PSM converter limits, and `oraAdapter` DDL/LOB constraints.

## Version Checks

- 7.1:
  - Adapter for Oracle prerequisite now matches the 7.1 Korean manual: Altibase `5.5.1` or later.
  - Adapter LOB support boundary is present: Adapter for Oracle `7.1.0.7.0`.
  - DML attachment avoids 8.1 JSON functions for 7.1.
- 7.3:
  - Adapter for Oracle prerequisite now matches the 7.3 Korean manual: Altibase `6.5.1` or later.
  - Oracle `JSON` migration is correctly framed as `CLOB` for 7.3 and earlier targets.
  - DML attachment avoids 8.1 JSON functions for 7.3.
- 8.1:
  - Adapter for Oracle prerequisite now matches the 8.1 verified-source Korean manual: Altibase `6.5.1` or later.
  - Oracle `JSON` migration is correctly framed as `JSON` for 8.1 verified source and later JSON-capable targets.
  - DML attachment marks JSON functions and `IS JSON` as 8.1 verified-source features.

## Retrieval And GPT Answer Quality

- Strengths:
  - The attachment gives task-oriented headings for planning, options, object support, DDL differences, data type/default mappings, PSM review, validation, troubleshooting, and `oraAdapter`.
  - Conversion-risk language is explicit: it avoids full Oracle-compatibility claims and requires Reconcile, conversion-report review, validation, compile/runtime testing, and application checks.
  - Literal names such as `sqlconv.html`, `RunReport4Summary.html`, `ADAPTER_LOB_TYPE_SUPPORT`, `REPLICATION_MAX_COUNT`, `IS JSON`, and `DEFAULT ON NULL` are preserved for retrieval.
- Risks:
  - PSM converter rules are necessarily condensed. Customer answers should point users to generated `sqlconv_*` reports and attachment `10_psm_stored_external_procedures.md` when the exact PL/SQL construct matters.
  - Data Validation still has structural limits: primary-key-only comparison and LOB comparison exclusions require separate checks for some migrations.

## Required Follow-Up

- None for R08.
