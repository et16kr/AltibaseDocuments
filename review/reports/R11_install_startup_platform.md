# R11 Installation, Startup/Shutdown, First-Run Checks, and Platform Boundaries

Date: 2026-05-16
Reviewer: Codex
Verdict: Pass

## Scope

- Attachments:
  - `GPTs/attachments/01_getting_started_installation.md`
  - `GPTs/attachments/00_version_release_platform.md`
- Supporting reports:
  - `GPTs/reports/version_coverage_validation.md`
  - `GPTs/reports/source_inventory.md`
- Source manuals sampled:
  - `Manuals/Altibase_7.1/kor/Getting Started Guide.md`
  - `Manuals/Altibase_7.1/kor/Installation Guide.md`
  - `Manuals/Altibase_7.3/kor/Getting Started Guide.md`
  - `Manuals/Altibase_7.3/kor/Installation Guide.md`
  - `Manuals/Altibase_trunk/kor/Getting Started Guide.md`
  - `Manuals/Altibase_trunk/kor/Installation Guide.md`
  - `ReleaseNotes/kor/Altibase_7_1_0_1_2_Release_Notes.md`
  - `ReleaseNotes/kor/Altibase_7_3_0_0_1_Release_Notes.md`
  - `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`
  - `Technical Documents/kor/Supported Platforms.md`

## Commands Run

```bash
bash review/scripts/run_review_remediation_cycle.sh status
rg -n $'\t(Reviewing|Remediating|ReReviewing|Fail)$' review/review_remediation_cycle_status.tsv
git status --short
git diff -- GPTs/attachments/00_version_release_platform.md
git diff -- GPTs/attachments/01_getting_started_installation.md
git diff -- GPTs/reports/source_inventory.md
sed -n '1,240p' review/reports/R11_install_startup_platform.md
sed -n '1,260p' review/Altibase_GPT_Detailed_Review_Design.md
sed -n '1,260p' GPTs/Altibase_GPT_Document_Selection.md
sed -n '1,340p' GPTs/Altibase_GPT_Attachment_Build_Workplan.md
sed -n '1,240p' GPTs/attachments/README.md
rg -n '^R11\t|G3_Operations' review/review_stages.tsv
nl -ba GPTs/attachments/01_getting_started_installation.md | sed -n '1,520p'
nl -ba GPTs/attachments/00_version_release_platform.md | sed -n '1,520p'
nl -ba GPTs/reports/version_coverage_validation.md | sed -n '1,180p'
rg -n 'post_install|pre_install|server create|server start|server stop|shutdown normal|shutdown immediate|shutdown abort|server kill|catproc|APatch|downgrade|license|Transparent|THP|sample/APRE|schema.sql|ALTIBASE_NLS|ALTIBASE_PORT_NO|altibase_user.env|STARTUP Process SUCCESS|V\$VERSION' Manuals/Altibase_7.1/kor/Getting\ Started\ Guide.md Manuals/Altibase_7.1/kor/Installation\ Guide.md Manuals/Altibase_7.3/kor/Getting\ Started\ Guide.md Manuals/Altibase_7.3/kor/Installation\ Guide.md Manuals/Altibase_trunk/kor/Getting\ Started\ Guide.md Manuals/Altibase_trunk/kor/Installation\ Guide.md
rg -n 'RemoveIPC|/etc/systemd/logind.conf|semaphore|세마포어|비정상|Transparent Huge|transparent_hugepage|redhat_transparent' Manuals/Altibase_7.1/kor/Installation\ Guide.md Manuals/Altibase_7.3/kor/Installation\ Guide.md Manuals/Altibase_trunk/kor/Installation\ Guide.md
rg -n 'Windows|AIX|HP-UX|RHEL|Red Hat|CentOS|Rocky|Oracle Linux|Ubuntu|LinuxONE|s390x|glibc|JDK|JRE|Java|64|x86|POWER|Itanium|IA-64|2008|Windows 10' Technical\ Documents/kor/Supported\ Platforms.md ReleaseNotes/kor/Altibase_7_1_0_1_2_Release_Notes.md ReleaseNotes/kor/Altibase_7_3_0_0_1_Release_Notes.md ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md Manuals/Altibase_7.3/kor/Installation\ Guide.md
rg -n 'product_version|meta_version|protocol_version|repl_protocol_version|META_MAJOR_VER|SYS_DATABASE_|DBMS_METADATA|database binary|데이터베이스 바이너리|메타|프로토콜' ReleaseNotes/kor/Altibase_7_1_0_1_2_Release_Notes.md ReleaseNotes/kor/Altibase_7_3_0_0_1_Release_Notes.md ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md Manuals/Altibase_7.1/kor/Installation\ Guide.md Manuals/Altibase_7.3/kor/Installation\ Guide.md Manuals/Altibase_trunk/kor/Installation\ Guide.md
nl -ba 'Technical Documents/kor/Supported Platforms.md' | sed -n '1,180p'
nl -ba 'Technical Documents/kor/Supported Platforms.md' | sed -n '180,260p'
nl -ba ReleaseNotes/kor/Altibase_7_3_0_0_1_Release_Notes.md | sed -n '60,95p'
nl -ba ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md | sed -n '40,65p'
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name README.md | sort | wc -l
rg -n 'trunk|file://|C:/|Manuals/|ReleaseNotes/|Altibase_trunk|/home/' GPTs/attachments/01_getting_started_installation.md GPTs/attachments/00_version_release_platform.md
rg -n 'RemoveIPC|Windows 2008|post_install\.sh dbcreate|server create|server start|shutdown normal|shutdown immediate|V\$VERSION|STARTUP Process SUCCESS|Altibase 8\.1 verified source' GPTs/attachments/01_getting_started_installation.md GPTs/attachments/00_version_release_platform.md
find review/reports -maxdepth 1 -type f -name 'R11*' -print
git diff --check
bash review/scripts/run_review_stage.sh validate
rg -n "^Verdict:|^\| (Blocker|High|Medium|Low) \|" review/reports/R11_install_startup_platform.md
git status --short
```

## Findings

No actionable `Blocker`, `High`, `Medium`, or `Low` findings were found in the current R11 worktree.

| Severity | File | Line | Finding | Recommendation |
| --- | --- | ---: | --- | --- |
| Note | `GPTs/attachments/01_getting_started_installation.md`; `GPTs/attachments/00_version_release_platform.md` | n/a | The current attachment text is actionable for installation prerequisites, first database creation, startup/shutdown, first-run verification, package/platform boundaries, and version labeling. The prior R11 issues around `RemoveIPC`, database creation wording, explicit `V$VERSION` verification, and 7.3 Windows 2008 source drift are represented in the scoped attachments. | No R11 attachment remediation is required. Keep exact customer patch level in scope for platform answers, especially for 7.1 and 7.3 supported-platform additions. |

## Source Checks

- Claims checked:
  - Package installer mode, server/client package separation, `ALTIBASE_HOME`, `Full Installation`, `Patch Installation`, package execution, license placement, and generated environment files.
  - First database creation through `sh post_install.sh dbcreate` when database creation properties were selected, and `server create [DB Character Set] [National Character Set]` when they were not.
  - Startup through iSQL `startup` and `server start`, including `SERVICE` phase and `STARTUP Process SUCCESS`.
  - Shutdown modes `shutdown normal`, `shutdown immediate`, `server stop`, `shutdown abort`, and `server kill`.
  - First-run checks using iSQL plus `V$VERSION`, trace-log review, sample schema path `$ALTIBASE_HOME/sample/APRE/schema/schema.sql`, and client profile variables.
  - Linux prerequisites for user limits, kernel parameters, THP disabled as `never`, and Red Hat 7.2-or-later `RemoveIPC=no`.
  - APatch directory behavior, patch rollback limits, HP-UX rollback limitation, `server downgrade`, and `SYSTEM_.SYS_DATABASE_` meta-version checks.
  - 7.1, 7.3, and 8.1 server/client platform blocks, 64-bit package boundaries, Windows client-only status, glibc conditions, and JDK/JRE conditions.
- Source coverage:
  - Korean Getting Started Guides support first database creation, startup, shutdown, sample schema loading, and character-set environment guidance.
  - Korean Installation Guides support package installer behavior, generated scripts, post-install steps, client-only environment behavior, user limits, kernel parameters, THP, `RemoveIPC`, APatch, rollback, and meta downgrade.
  - Korean release notes and the Korean Supported Platforms document support the version and platform boundaries in `00_version_release_platform.md`.
  - `GPTs/reports/version_coverage_validation.md` confirms that both scoped attachments contain 7.1, 7.3, and 8.1 coverage markers.
- Korean/English source conflicts:
  - No Korean/English conflict was used as a basis for this stage. The review used Korean manuals, Korean release notes, and Korean technical documents as the source authority.
  - Korean-source drift for 7.3 Windows 2008 is now explicitly represented: 7.3.0.0.1 release/installation sources list Windows 2008 client-only, while the newer Supported Platforms document lists Windows 10 only for 7.3.
- Source gaps:
  - This review sampled the required R11 Korean sources and the supplied coverage report. It did not inspect every minor 7.1 or 7.3 patch release note; platform answers should still collect the customer's exact patch version before giving final support guidance.

## Oracle-Overlap Decision

- Correctly compressed:
  - The scoped attachments stay focused on Altibase-specific installation, database creation, platform support, startup/shutdown, patch rollback, metadata/protocol verification, and first-run troubleshooting.
- Too much generic Oracle material:
  - None found.
- Missing Altibase-specific difference:
  - None found for this stage. The Altibase-specific `RemoveIPC`, THP, APatch, `server create`, `server downgrade`, `V$VERSION`, and platform-boundary guidance is present.

## Version Checks

- 7.1:
  - Installation/startup/shutdown procedure is source-backed by the 7.1 Korean Getting Started and Installation Guides.
  - Platform guidance preserves 64-bit-only package scope, Windows client-only status, Windows 2008 client patch condition, and JDK/JRE 1.5-or-later requirement.
  - Upgrade/rollback guidance preserves database binary, metadata, communication protocol, and replication protocol cautions at the level needed for R11.
- 7.3:
  - Installation/startup/shutdown procedure is source-backed by the 7.3 Korean Getting Started and Installation Guides.
  - Platform guidance preserves 64-bit-only package scope, LinuxONE/RHEL 9 patch additions, Windows 10 current supported-platform status, and the 7.3.0.0.1 Windows 2008 client-only source caveat.
  - Version labeling includes 7.3 database binary/meta/protocol compatibility cautions.
- 8.1:
  - Installation workflow is source-backed by the Altibase 8.1 verified source manuals.
  - 8.1 platform guidance matches the 8.1 Korean release notes for AIX 7.2, Linux x86-64 on RHEL 7/8/9, Windows 2008/10 client-only, 64-bit package scope, and JDK 1.8-or-later Java compatibility.
  - Upgrade caution correctly states that pre-8.1 databases are not binary-compatible and require migration or metadata rebuild planning rather than an in-place package-patch answer.

## Retrieval And GPT Answer Quality

- Strengths:
  - The installation attachment has direct, retrievable procedure sections for prerequisites, installer steps, generated files, database creation, PSM setup, startup, first connection verification, shutdown, client-only installation, patch rollback, and first-run troubleshooting.
  - The version/platform attachment separates release identity, compatibility risks, component versions, platform blocks, and platform-answer collection fields.
  - Literal commands, SQL object names, property names, paths, view names, and version labels are preserved.
  - The current line-level wording avoids flattening server/client support and tells the GPT to ask for exact patch level when platform support depends on it.
- Risks:
  - Exact site commands still depend on installer choices, license state, OS account setup, kernel values, and customer patch level.
  - 8.1 is represented from the verified source and 8.1.0.0.1 release notes; newer 8.1 patch behavior would require a newer source pass if introduced.

## Required Follow-Up

- None for R11. This stage can be committed once the usual validation and review-cycle status handling pass.
