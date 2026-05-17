# Full Coverage Audit Guardrail Register

- Workflow: `altibase-gpt-full-coverage-audit`
- Initialized by: `FCA-J003`
- Status: Active register for `Guardrail` and `Out-of-scope` catalog or matrix rows

## Register Contract

Add one entry for every `Guardrail` or `Out-of-scope` row. Each entry must explain the
source boundary or customer-evidence dependency and give the safest next check or
missing input pattern.

Accepted guardrail reasons include:

- exact version or patch level is required;
- customer environment, topology, object definition, log excerpt, runtime output, or
  installed tool behavior is required;
- selected sources do not support the requested compatibility, syntax, error-code, or
  operational claim;
- the item is outside the locked selected source corpus.

## Active Guardrails

### FCA-J005 Installation And Getting-Started Guardrails

FCA-J005 cataloged 2 `Guardrail` rows. These are acceptable only when answers ask for
the customer evidence below instead of guessing package availability or license status.

| source_item_id | status | source_family | version_scope | source_path | source_heading | guardrail_reason | safest_next_check | attachment_target | audit_job | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-OTHER-XVER-000030 | Guardrail | getting_started_installation | cross-version | Manuals/Altibase_trunk/kor/Installation Guide.md | Installation Guide > Package installer download > support portal package acquisition | Current package download availability depends on exact version, patch, customer entitlement, OS/CPU package naming, and live Altibase Support portal state; selected manuals identify the route but cannot verify current access. | Ask for exact Altibase version/patch, server or client target, OS/version, CPU architecture, and whether the customer has the installer package or support-portal entitlement before giving copy-ready package commands. | GPTs/attachments/01_getting_started_installation.md | FCA-J005 | rg -n 'support.altibase.com\|패키지 인스톨러\|operating system' Manuals/Altibase_trunk/kor/Installation\ Guide.md GPTs/attachments/01_getting_started_installation.md |
| SRC-OTHER-7.1-000001 | Guardrail | getting_started_installation | 7.1 | Manuals/Altibase_7.1/kor/Installation Guide.md | Installation Guide > Register or Update the Altibase License Key > license acquisition | License issuance depends on license type, customer contract, current Altibase Support process, and issued license validity; selected 7.1 source documents historical acquisition paths but cannot verify current entitlement or portal behavior. | Ask for license type, exact Altibase version/patch, whether a license file/key has already been issued, and the current support/contract path; for installation, only state the source-backed placement and startup effect of `$ALTIBASE_HOME/conf/license`. | GPTs/attachments/01_getting_started_installation.md | FCA-J005 | rg -n 'Enterprise Edition\|Trial\|support.altibase.com\|라이선스' Manuals/Altibase_7.1/kor/Installation\ Guide.md GPTs/attachments/01_getting_started_installation.md |

### FCA-J004 Release, Platform, And Scope Guardrails

FCA-J004 cataloged 6 `Guardrail` or `Out-of-scope` rows. These rows remain acceptable only with the missing-input or source-boundary pattern below.

| source_item_id | status | source_family | version_scope | source_path | source_heading | guardrail_reason | safest_next_check | attachment_target | audit_job | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-REL-8.1-000006 | Guardrail | release_notes_platform | 8.1 | ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md | Altibase 8.1.0.0.1 Release Notes > release-note-only feature procedure boundary | Selected release notes confirm availability, but implementation procedures depend on exact feature family, installed package/API, and a dedicated source-backed manual or tool bl... | Ask for exact version/patch, component, OS/CPU/glibc or installed tool/API state as applicable; use only selected source rows or run a dedicated source-backed audit before givin... | GPTs/attachments/00_version_release_platform.md | FCA-J004 | rg -n 'KADA/Kafka/ABM/MindsDB/\.NET 8/node-odbc-altibase/Release-note-only feature scope/Residual Scope' ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md GPTs/attachments/00... |
| SRC-PLAT-XVER-000002 | Guardrail | release_notes_platform | cross-version | Technical Documents/kor/Supported Platforms.md | Supported Platforms > overview > unlisted OS support | The supported-platform source explicitly sends unlisted OS compatibility to Altibase Support; ask for exact Altibase version/patch, component, OS/version, CPU architecture, glib... | Ask for exact version/patch, component, OS/CPU/glibc or installed tool/API state as applicable; use only selected source rows or run a dedicated source-backed audit before givin... | GPTs/attachments/00_version_release_platform.md | FCA-J004 | source locator: Technical Documents/kor/Supported Platforms.md lines 29-34; rg -n 'Altibase Support/Platform Answer Checklist/direct the customer to Altibase Support' GPTs/attac... |
| SRC-PLAT-XVER-000003 | Out-of-scope | release_notes_platform | cross-version | Technical Documents/kor/Supported Platforms.md | Supported Platforms > Altibase 6.5.1 | Altibase 6.5.1 platform support is outside the locked customer-facing upload scope of Altibase 7.1, 7.3, and 8.1; do not use 6.5.1 platform rows to answer 7.x or 8.1 support que... | Ask for exact version/patch, component, OS/CPU/glibc or installed tool/API state as applicable; use only selected source rows or run a dedicated source-backed audit before givin... | N/A | FCA-J004 | source locator: Technical Documents/kor/Supported Platforms.md lines 167-254; rg -n 'Altibase 6.5.1/Do not use 6.5.1 platform support' GPTs/attachments/00_version_release_platfo... |
| SRC-REL-PATCH-000015 | Guardrail | release_notes_platform | patch-specific | ReleaseNotes/kor/Altibase_ShardManager_v.3.2_Release_Notes.md | Altibase Shard Manager Release Notes > release-note document boundary | The locked release-note root contains this product/tool release note, but the 20-file attachment/source-family map has no dedicated answer-ready owner for ShardManager/Sharding/... | Ask for exact version/patch, component, OS/CPU/glibc or installed tool/API state as applicable; use only selected source rows or run a dedicated source-backed audit before givin... | GPTs/attachments/00_version_release_platform.md | FCA-J004 | rg -n 'Release Notes/BUG-' ReleaseNotes/kor/Altibase_ShardManager_v.3.2_Release_Notes.md |
| SRC-REL-PATCH-000016 | Guardrail | release_notes_platform | patch-specific | ReleaseNotes/kor/Altibase_Sharding3_3_2_0_0_1_Release_Notes.md | Altibase Sharding 3 Release Notes > release-note document boundary | The locked release-note root contains this product/tool release note, but the 20-file attachment/source-family map has no dedicated answer-ready owner for ShardManager/Sharding/... | Ask for exact version/patch, component, OS/CPU/glibc or installed tool/API state as applicable; use only selected source rows or run a dedicated source-backed audit before givin... | GPTs/attachments/00_version_release_platform.md | FCA-J004 | rg -n 'Release Notes/BUG-' ReleaseNotes/kor/Altibase_Sharding3_3_2_0_0_1_Release_Notes.md |
| SRC-REL-PATCH-000017 | Guardrail | release_notes_platform | patch-specific | ReleaseNotes/kor/Altibase_Windows2026_2_6_0_0_1_Release_Notes.md | Altibase Windows 2026 Release Notes > release-note document boundary | The locked release-note root contains this product/tool release note, but the 20-file attachment/source-family map has no dedicated answer-ready owner for ShardManager/Sharding/... | Ask for exact version/patch, component, OS/CPU/glibc or installed tool/API state as applicable; use only selected source rows or run a dedicated source-backed audit before givin... | GPTs/attachments/00_version_release_platform.md | FCA-J004 | rg -n 'Release Notes/BUG-' ReleaseNotes/kor/Altibase_Windows2026_2_6_0_0_1_Release_Notes.md |
