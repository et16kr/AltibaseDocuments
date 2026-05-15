# R23 Utilities, dataCompJ, and Operation Tools

Date: 2026-05-16
Reviewer: Codex
Verdict: Pass

## Scope

- Attachments:
  - `GPTs/attachments/14_utilities_operation_tools.md`
  - `GPTs/attachments/13_isql_iloader_basic_tools.md`
- Supporting reports:
  - `GPTs/reports/source_inventory.md`
  - `GPTs/reports/image_inventory.md`
- Source manuals sampled:
  - `Manuals/Altibase_7.1/kor/Utilities Manual.md`
  - `Manuals/Altibase_7.3/kor/Utilities Manual.md`
  - `Manuals/Altibase_trunk/kor/Utilities Manual.md`
  - `Manuals/Altibase_7.1/kor/iSQL User's Manual.md`
  - `Manuals/Altibase_7.3/kor/iSQL User's Manual.md`
  - `Manuals/Altibase_trunk/kor/iSQL User's Manual.md`
  - `Manuals/Altibase_7.1/kor/iLoader User's Manual.md`
  - `Manuals/Altibase_7.3/kor/iLoader User's Manual.md`
  - `Manuals/Altibase_trunk/kor/iLoader User's Manual.md`
  - `Manuals/Tools/Altibase_release/kor/dataCompJ User's Manual.md`
  - `Manuals/Tools/Altibase_trunk/kor/dataCompJ User's Manual.md`
  - `ReleaseNotes/kor/Altibase_dataCompJ_7_2_Release_Notes.md`

## Commands Run

```bash
bash review/scripts/run_review_remediation_cycle.sh status
rg -n $'\t(Reviewing|Remediating|ReReviewing|Fail)$' review/review_remediation_cycle_status.tsv
git status --short
git diff -- GPTs/attachments/14_utilities_operation_tools.md GPTs/reports/source_inventory.md review/review_remediation_cycle_status.tsv review/review_stage_status.tsv
sed -n '1,260p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,240p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,260p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,220p' GPTs/attachments/README.md
wc -l GPTs/attachments/14_utilities_operation_tools.md GPTs/attachments/13_isql_iloader_basic_tools.md GPTs/reports/source_inventory.md GPTs/reports/image_inventory.md
rg -n '^#{1,5} ' GPTs/attachments/14_utilities_operation_tools.md GPTs/attachments/13_isql_iloader_basic_tools.md
nl -ba GPTs/attachments/14_utilities_operation_tools.md | sed -n '1,1325p'
nl -ba GPTs/attachments/13_isql_iloader_basic_tools.md | sed -n '1,1320p'
sed -n '350,410p' GPTs/reports/source_inventory.md
rg -n '13_isql_iloader_basic_tools|14_utilities_operation_tools' GPTs/reports/image_inventory.md
rg -n 'AEXPORT_FILE_PERMISSION|ALTIBASE_UT_FILE_PERMISSION|TWO_PHASE_SCRIPT|run_is_repl|run_is_con|ISQL_REPL|ISQL_REFERSH_MVIEW|DBMS_METADATA' Manuals/Altibase_7.3/kor/Utilities\ Manual.md Manuals/Altibase_trunk/kor/Utilities\ Manual.md Manuals/Altibase_7.1/kor/Utilities\ Manual.md
rg -n 'JAVA_HOME|JRE|Java|Altibase 5\.3\.3|Oracle 9i|MariaDB 5\.5|MasterDB|SlaveDB|TraceInconsistentRecord|MaxThread|TablePair|TableNameFilePath|MOSO|MOSX|MXSO|dataCompJCli\.sh' Manuals/Tools/Altibase_release/kor/dataCompJ\ User\'s\ Manual.md Manuals/Tools/Altibase_trunk/kor/dataCompJ\ User\'s\ Manual.md ReleaseNotes/kor/Altibase_dataCompJ_7_2_Release_Notes.md
rg -n 'dumptrc|\[-x\]|버전.*다른|altibase.*버전|호출 스택|call stack' Manuals/Altibase_7.3/kor/Utilities\ Manual.md Manuals/Altibase_trunk/kor/Utilities\ Manual.md Manuals/Altibase_7.1/kor/Utilities\ Manual.md
rg -n 'aku|AKU_|OrderedReady|StatefulSet|/tmp/aku_start_completed|REMOTE_SYSDBA_ENABLE|ADMIN_MODE|publishNotReadyAddresses|XSN|RESET' Manuals/Altibase_7.3/kor/Utilities\ Manual.md Manuals/Altibase_trunk/kor/Utilities\ Manual.md
rg -n 'ALTIBASE_UT_FILE_PERMISSION|ISQL_FILE_PERMISSION|ILO_FILE_PERMISSION|ISQL_SECURE_LOGIN_MSG|Empty LOB|use_lob_file|Direct-Path|direct|lightmode|extra_col_delimiter|rule csv|dry-run' Manuals/Altibase_7.3/kor/iSQL\ User\'s\ Manual.md Manuals/Altibase_7.3/kor/iLoader\ User\'s\ Manual.md Manuals/Altibase_trunk/kor/iSQL\ User\'s\ Manual.md Manuals/Altibase_trunk/kor/iLoader\ User\'s\ Manual.md Manuals/Altibase_7.1/kor/iSQL\ User\'s\ Manual.md Manuals/Altibase_7.1/kor/iLoader\ User\'s\ Manual.md
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name README.md | wc -l
rg -n '!\[[^]]*\]\(|<img|media/|\.png|\.gif|\.jpg|file://|/home/|C:\\|trunk' GPTs/attachments/14_utilities_operation_tools.md GPTs/attachments/13_isql_iloader_basic_tools.md
rg -n 'AEXPORT_FILE_PERMISSION|run_is_repl\.sh|JAVA_HOME|Altibase 5\.3\.3|Oracle 9i|MariaDB 5\.5\.x|\[-x\]|Korean manuals and Korean release notes' GPTs/attachments/14_utilities_operation_tools.md GPTs/reports/source_inventory.md
git diff --check -- GPTs/attachments/14_utilities_operation_tools.md GPTs/reports/source_inventory.md review/reports/R23_utilities_datacompj.md
bash review/scripts/run_review_stage.sh validate
```

## Findings

No actionable `Blocker`, `High`, `Medium`, or `Low` findings remain for this stage.

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Note | `GPTs/attachments/14_utilities_operation_tools.md` and `GPTs/attachments/13_isql_iloader_basic_tools.md` | N/A | The scoped attachments are task-oriented, version-aware at the attachment level, and no longer depend on screenshots or raw image references. The previously reported R23 issues for `run_is_repl.sh`, `AEXPORT_FILE_PERMISSION`, Korean-source inventory, `dataCompJ` runtime/compatibility bounds, and `dumptrc -x` are represented in the current workspace. | No R23 remediation required. Preserve the existing residual-scope wording that less common or patch-specific utility switches should be verified against the installed utility help or target manual. |

## Source Checks

- Claims checked:
  - `aexport` purpose, `DBMS_METADATA` prerequisite, generated script names, `TWO_PHASE_SCRIPT`, `run_is_repl.sh`, `run_is_con.sh`, generated import flow, and output-file permission variables.
  - `altiComp` `DIFF`/`SYNC`, `DB_MASTER`, `DB_SLAVE`, `MOSO`, `MOSX`, `MXSO`, `INSERT_TO_SLAVE`, `INSERT_TO_MASTER`, `DELETE_IN_SLAVE`, `UPDATE_TO_SLAVE`, `WHERE`, `EXCLUDE`, `MAX_THREAD`, and `FILE_MODE_MAX_ARRAY`.
  - `dataCompJ` Java 8+ runtime, `JAVA_HOME`, Master DB and Slave DB version bounds, `dataCompJCli.sh -f`, build/run phases, XML sections, `TraceInconsistentRecord`, `MaxThread`, `TablePair`, `TableNameFilePath`, DIFF files, and SYNC policy elements.
  - `aku` `aku.conf`, `AKU_*` properties, StatefulSet/OrderedReady constraints, `ADMIN_MODE`, `REMOTE_SYSDBA_ENABLE`, `/tmp/aku_start_completed`, `aku -p start`, `aku -p end`, `aku -p clean`, and `XSN` reset checks.
  - `altiAudit`, `altibase`, `altiMon`, `altierr`, `altipasswd`, `altiProfile`, `altiwrap`, `awrite`, `checkServer`, `killCheckServer`, `server`, and dump-family diagnostic utilities including `dumptrc -x`.
  - Companion iSQL/iLoader guidance for generated-file permissions, secure login messages, iLoader CSV conflict handling, LOB handling, Direct-Path INSERT, `-lightmode`, `-extra_col_delimiter`, and production bad/log file handling.
- Source coverage:
  - Korean Utilities Manual 7.1, 7.3, and 8.1-source sampling supports the current utility workflows and cautions in `14_utilities_operation_tools.md`.
  - Korean dataCompJ manuals and Korean dataCompJ 7.2 release notes support the current runtime, compatibility, CLI, XML, DIFF, and SYNC guidance.
  - Korean iSQL and iLoader manual sampling supports the companion `13_isql_iloader_basic_tools.md` content relevant to this stage.
  - `GPTs/reports/source_inventory.md` now lists Korean manuals and Korean release notes as primary for attachment 14, with English sources kept as secondary extraction/parity references.
- Korean/English source conflicts:
  - No remaining conflict was found that changes the scoped attachment guidance. The earlier source-inventory drift was corrected in the current workspace.
- Source gaps:
  - The attachments intentionally do not reproduce every low-frequency utility option or every output field. The residual-scope sections correctly direct final runbook answers to verify patch-level option behavior against the installed client help or target manual.

## Oracle-Overlap Decision

- Correctly compressed:
  - Ordinary Oracle-overlapping SQL is not expanded. The scoped attachments focus on Altibase-specific utilities, generated scripts, iSQL/iLoader operational behavior, comparison/synchronization tools, Kubernetes utility behavior, and diagnostic commands.
- Too much generic Oracle material:
  - None found.
- Missing Altibase-specific difference:
  - None found for this stage after re-review. `dataCompJ` preserves the documented Altibase-to-Oracle/MariaDB scope and version bounds.

## Version Checks

- 7.1:
  - Stable utility behavior is covered for `aexport`, `altiComp`, iSQL/iLoader companion workflows, and dump-family tools. The attachment tells users to verify exact local utility options for less common switches.
- 7.3:
  - Korean 7.3 source supports the current `DBMS_METADATA`, `AEXPORT_FILE_PERMISSION`, `aku`, `altiComp`, iSQL/iLoader, and `dumptrc -x` guidance.
- 8.1:
  - The attachment uses customer-safe `Altibase 8.1 verified source` wording and does not expose internal source labels. The sampled 8.1-source Utilities, iSQL/iLoader, and dataCompJ manuals align with the current task-oriented guidance.

## Retrieval And GPT Answer Quality

- Strengths:
  - The utility attachment is organized by decision map and repeated tool blocks with purpose, use case, representative command, key inputs, cautions, and verification method.
  - High-risk workflows are procedure-oriented: `aexport` migration scripts, `altiComp` and `dataCompJ` DIFF/SYNC, `aku` pod lifecycle, server control, and dump-family diagnostics all include guardrails.
  - Screenshot and syntax-diagram content has been converted into searchable Markdown, compact command syntax, Mermaid where useful, or procedure text.
  - Companion iSQL/iLoader material supports generated-script workflows, data-load modes, bad/log file handling, file permissions, and character-set handling.
- Risks:
  - Less common utility switches and exact output fields remain summarized. This is acceptable for upload because the attachment explicitly scopes those areas to installed-client/manual verification before producing a final production runbook.

## Required Follow-Up

- None for R23.
