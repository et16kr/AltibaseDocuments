# Patch Note Closure Design

- Job id: `PWF-J002`
- Date: 2026-05-18
- Status: Design only. This job does not edit `GPTs/attachments/` or close catalog
  rows.
- Target scope: active patch-note `Missing` rows in
  `GPTs/reports/full_coverage_audit/source_item_catalog.tsv` and
  `GPTs/reports/full_coverage_audit/source_to_attachment_matrix.tsv`.

## Worktree And Cycle Gate

Required first checks were run before this report was created.

| Check | Result |
| --- | --- |
| `bash review/scripts/run_review_remediation_cycle.sh status` | All stages `Done`. |
| `rg -n $'\t(Reviewing\|Remediating\|ReReviewing\|Fail)$' review/review_remediation_cycle_status.tsv` | No active `Reviewing`, `Remediating`, `ReReviewing`, or `Fail` stages. |
| `git status --short` | Existing modification only under `.codex-jobs/altibase-gpt-post-workflow-followup/jobs.tsv`; no project-file edits outside orchestrator state before this report. |

## Active Missing Row Confirmation

The active `Missing` set is still exactly the patch-note range requested by this job.

| Evidence | Result |
| --- | --- |
| Catalog `Missing` rows | `115` |
| Matrix `Missing` rows | `115` |
| Active range | `SRC-PATCH-PATCH-000001` through `SRC-PATCH-PATCH-000115` |
| Range continuity | No gaps |
| Source family | `patch_notes` |
| Version scope | `patch-specific` |
| Attachment target | `GPTs/attachments/00_version_release_platform.md` |
| Altibase 7.1 rows | `96` |
| Altibase 7.3 rows | `19` |
| Non-patch `Missing` rows | `0` in catalog and matrix |
| Current `TASK-*` literals | `0`; the closure rules below still require preserving `TASK-*` if a later source split discovers one. |

Confirmation commands used:

```bash
awk -F '\t' 'NR==1 {next}
  $1 ~ /^SRC-PATCH-PATCH-/ && $8 == "Missing" {
    n++; if (first=="") first=$1; last=$1;
    split($1,a,"-"); num=a[4]+0;
    if (n==1) prev=num-1;
    if (num != prev+1) gaps=gaps prev ":" num ";";
    prev=num;
    if ($4 ~ /Altibase_7\.1/) v71++;
    if ($4 ~ /Altibase_7\.3/) v73++;
  }
  END {
    printf("count=%d\nfirst=%s\nlast=%s\ngaps=%s\n7.1=%d\n7.3=%d\n",
      n, first, last, (gaps==""?"none":gaps), v71, v73)
  }' GPTs/reports/full_coverage_audit/source_to_attachment_matrix.tsv

awk -F '\t' 'NR==1 {next}
  $10 == "Missing" && $1 !~ /^SRC-PATCH-PATCH-/ {n++}
  END {print "catalog_non_patch_missing=" n+0}' \
  GPTs/reports/full_coverage_audit/source_item_catalog.tsv

awk -F '\t' 'NR==1 {next}
  $8 == "Missing" && $1 !~ /^SRC-PATCH-PATCH-/ {n++}
  END {print "matrix_non_patch_missing=" n+0}' \
  GPTs/reports/full_coverage_audit/source_to_attachment_matrix.tsv
```

## Representative Source Shape

Sampled patch-note files show the same closure-relevant structure: patch heading,
`New Features`, `Fixed Bugs`, `Changes`, `Version Info`, compatibility notes,
property notes, and performance-view notes.

| Sample | Source row | File | Observed structure |
| --- | --- | --- | --- |
| Early 7.1 | `SRC-PATCH-PATCH-000001` | `PatchNotes/Altibase_7.1/kor/Altibase_7_1_0_1_3_Patch_Notes.md` | `New Features` at line 51, `Fixed Bugs` at line 504, `Changes` at line 1246, `Version Info` at line 1249, plus property and performance-view sections. |
| Late 7.1 | `SRC-PATCH-PATCH-000096` | `PatchNotes/Altibase_7.1/kor/Altibase_7_1_0_10_8_Patch_Notes.md` | `New Features` at line 47, `Fixed Bugs` at line 162, `Changes` at line 1042, `Version Info` at line 1045, plus explicit no-change property and performance-view sections. |
| 7.3 | `SRC-PATCH-PATCH-000107` | `PatchNotes/Altibase_7.3/kor/Altibase_7_3_0_1_2_Patch_Notes.md` | `New Features` at line 40, `Fixed Bugs` at line 242, `Changes` at line 859, `Version Info` at line 862, plus explicit no-change property and performance-view sections. |

The source prose is Korean. Customer-facing closure in attachments must normalize it
to English while preserving exact product versions, literal object names, and
`BUG-*` or `TASK-*` tokens.

## Closure Shape

The default closure should add compact patch-note blocks to attachment `00`, not full
translated patch notes. The blocks should be dense enough for exact-token retrieval and
customer answers, while routing implementation details to owner attachments.

Recommended attachment placement for later remediation jobs:

- Add a section near `Minor Patch & Release Notes Caveats`, for example
  `## Patch Note Compact Change Blocks`.
- Keep one subsection per exact patch version unless row splitting is required.
- Keep the existing release, platform, and upgrade sections as the high-level entry
  points. Patch blocks are the exact-token closure layer under those entry points.

Per-patch block template:

```markdown
### Altibase <exact patch version> Patch Notes

Source row: `<SRC-PATCH-PATCH-000000>`.
Source file: `<repository-relative patch note path>`.
Version info: database binary `<value>`, meta `<value>`, communication protocol
`<value>`, replication protocol `<value>`.

Customer-answerable change tokens:
- New features: `BUG-xxxxx` - <short English normalized change>; route: <owner>.
- Fixed bugs: `BUG-xxxxx` - <short English normalized fix>; route: <owner>.
- Tasks: `TASK-xxxxx` - <short English normalized change>; route: <owner>.

Patch compatibility notes:
- Database binary version: <changed/not changed and migration implication when source says it>.
- Meta version: <changed/not changed and rollback or metadata implication when source says it>.
- Communication protocol: <changed/not changed>.
- Replication protocol: <changed/not changed>.
- Properties: <added, changed, deleted, or no changes>.
- Performance views: <added, changed, deleted, or no changes>.

Guardrail:
- Use the customer's exact installed patch, platform, object definitions, logs, and
  runtime output before asserting root cause, applicability, or production safety.

Owner routing:
- <attachment owner> owns implementation details for the listed feature, utility,
  connector, property, view, SQL, replication, security, or operational behavior.
```

Closure quality requirements:

- Preserve the exact patch version from `source_path`; never collapse a row to only
  `7.1` or `7.3`.
- Preserve every customer-answerable `BUG-*` and `TASK-*` literal from the source row.
- Preserve exact property names, view names, utility names, error tokens, SQL feature
  names, protocol names, package names, and environment variables when present.
- Translate or normalize Korean source prose into concise English; do not paste large
  Korean paragraphs into attachments.
- Include the `Version Info` values when present because upgrade and rollback answers
  depend on database binary, meta, communication protocol, and replication protocol
  values.
- Record whether property and performance-view sections say no changes, additions,
  changes, or deletions.
- Avoid inventing operational procedures from patch notes. Route procedures to owner
  attachments when they already have source-backed coverage.

## Owner Routing

Patch blocks in `00_version_release_platform.md` should be the version-aware index.
Detailed behavior belongs to the existing owner attachments.

| Source cue in patch note | Owner route |
| --- | --- |
| Install, package, startup, shutdown, rollback, meta downgrade | `01_getting_started_installation.md` |
| Backup, recovery, tablespaces, accounts, privileges, operational runbooks | `02_administration_operations.md` |
| DDL, DCL, tables, indexes, partitions, constraints, queue DDL | `03_sql_ddl_generation.md` |
| DML, expressions, functions, predicates, Oracle compatibility | `04_sql_dml_oracle_compatibility.md` |
| Properties, data types, LOB, JSON, locale, character set | `05_data_types_properties.md` |
| Dictionary views, performance views, metadata checks | `06_data_dictionary_performance_views.md` |
| Error codes, diagnostic messages, troubleshooting symptoms | `07_error_messages_troubleshooting.md` |
| Optimizer, statistics, execution plans, performance tuning, monitoring APIs | `08_performance_tuning_monitoring.md` |
| Replication, SQL apply, CDC, Log Analyzer, Replication Manager, protocol risk | `09_replication_ha_cdc.md` |
| PSM, packages, procedures, triggers, external procedures | `10_psm_stored_external_procedures.md` |
| JDBC, Java, Spring, Hibernate, JDBC Adapter | `11_java_jdbc_spring.md` |
| CLI, ODBC, C Interface, APRE/precompiler | `12_c_cli_odbc_precompiler.md` |
| iSQL and iLoader | `13_isql_iloader_basic_tools.md` |
| Utilities, `aexport`, `altiComp`, `altiMon`, `awrite`, `altiEncrypt` when used as a utility | `14_utilities_operation_tools.md` |
| Migration Center, Oracle migration, Adapter for Oracle | `15_migration_oracle_compatibility.md` |
| DB Link, AltiLinker, Hadoop and external connectors | `16_dblink_external_connectors.md` |
| AKU and Kubernetes | `17_kubernetes_aku_cloud.md` |
| SSL, TLS, FIPS, encrypted-password security boundaries | `18_security_ssl_tls.md` |
| Spatial, NiFi, Tableau, miscellaneous integrations | `19_spatial_nifi_tableau_misc.md` |

When a token spans several domains, keep the patch version and token in attachment
`00`, then route each detail to the most specific owner. Do not duplicate long
procedure text in attachment `00`.

## Batch Assignment

`PWF-J003` through `PWF-J014` should close or justify the 115 rows in 8-10 row
batches. The split keeps the 7.1 and 7.3 boundary clean and avoids mixed-version
recovery work.

| Job | Rows | Count | Version span | Source split | Token preservation check |
| --- | --- | ---: | --- | --- | --- |
| `PWF-J003` | `SRC-PATCH-PATCH-000001`-`SRC-PATCH-PATCH-000010` | 10 | `7.1.0.1.3` to `7.1.0.2.2` | 7.1 | 186 `BUG-*`, 0 `TASK-*` catalog literals |
| `PWF-J004` | `SRC-PATCH-PATCH-000011`-`SRC-PATCH-PATCH-000020` | 10 | `7.1.0.2.3` to `7.1.0.3.2` | 7.1 | 93 `BUG-*`, 0 `TASK-*` catalog literals |
| `PWF-J005` | `SRC-PATCH-PATCH-000021`-`SRC-PATCH-PATCH-000030` | 10 | `7.1.0.3.3` to `7.1.0.4.2` | 7.1 | 104 `BUG-*`, 0 `TASK-*` catalog literals |
| `PWF-J006` | `SRC-PATCH-PATCH-000031`-`SRC-PATCH-PATCH-000040` | 10 | `7.1.0.4.3` to `7.1.0.5.2` | 7.1 | 79 `BUG-*`, 0 `TASK-*` catalog literals |
| `PWF-J007` | `SRC-PATCH-PATCH-000041`-`SRC-PATCH-PATCH-000050` | 10 | `7.1.0.5.3` to `7.1.0.6.2` | 7.1 | 69 `BUG-*`, 0 `TASK-*` catalog literals |
| `PWF-J008` | `SRC-PATCH-PATCH-000051`-`SRC-PATCH-PATCH-000060` | 10 | `7.1.0.6.3` to `7.1.0.7.2` | 7.1 | 73 `BUG-*`, 0 `TASK-*` catalog literals |
| `PWF-J009` | `SRC-PATCH-PATCH-000061`-`SRC-PATCH-PATCH-000069` | 9 | `7.1.0.7.3` to `7.1.0.8.1` | 7.1 | 83 `BUG-*`, 0 `TASK-*` catalog literals |
| `PWF-J010` | `SRC-PATCH-PATCH-000070`-`SRC-PATCH-PATCH-000078` | 9 | `7.1.0.8.2` to `7.1.0.9.0` | 7.1 | 134 `BUG-*`, 0 `TASK-*` catalog literals |
| `PWF-J011` | `SRC-PATCH-PATCH-000079`-`SRC-PATCH-PATCH-000087` | 9 | `7.1.0.9.1` to `7.1.0.9.9` | 7.1 | 64 `BUG-*`, 0 `TASK-*` catalog literals |
| `PWF-J012` | `SRC-PATCH-PATCH-000088`-`SRC-PATCH-PATCH-000096` | 9 | `7.1.0.10.0` to `7.1.0.10.8` | 7.1 | 111 `BUG-*`, 0 `TASK-*` catalog literals |
| `PWF-J013` | `SRC-PATCH-PATCH-000097`-`SRC-PATCH-PATCH-000106` | 10 | `7.3.0.0.2` to `7.3.0.1.1` | 7.3 | 148 `BUG-*`, 0 `TASK-*` catalog literals |
| `PWF-J014` | `SRC-PATCH-PATCH-000107`-`SRC-PATCH-PATCH-000115` | 9 | `7.3.0.1.2` to `7.3.0.2.0` | 7.3 | 90 `BUG-*`, 0 `TASK-*` catalog literals |

The token counts above are a planning check from catalog literals, not a substitute
for reading the source files during remediation. Each remediation job must inspect its
scoped patch-note files and preserve all exact tokens found in source headings and
body text.

## Row Splitting Rules

Default: close the existing patch-file row with a compact patch block when one block
can preserve the exact version, all `BUG-*` and `TASK-*` tokens, `Version Info`, and
routing.

Split a row before closure when any of these are true:

- The patch file contains too many independent customer-answerable changes for one
  compact block to remain reviewable.
- A single patch row mixes unrelated high-risk domains, for example upgrade protocol
  risk plus security behavior plus replication failure behavior.
- A `BUG-*` or `TASK-*` item needs a different disposition from the parent patch, such
  as `Guardrail` or `Out-of-scope`.
- The exact token needs an owner-specific attachment anchor outside attachment `00`
  before the parent row can be closed.

Safe split shape:

- Keep the existing parent `SRC-PATCH-PATCH-000001` through
  `SRC-PATCH-PATCH-000115` row. Do not delete it.
- Add child rows using the next available `SRC-PATCH-PATCH-000116+` IDs if a split is
  required.
- Set each child `source_heading` to the exact patch version, section, and `BUG-*` or
  `TASK-*` heading.
- Set each child `literal_tokens` to the exact version plus the exact `BUG-*` or
  `TASK-*` token and any customer-answerable object tokens.
- Close the parent as `Covered-by-routing` only after all child rows are closed or
  justified and the parent points to a compact patch index anchor.
- Record the split in `remediation_log.md` and keep register totals consistent.

Do not split only to avoid preserving tokens. Splitting is for reviewability,
different dispositions, or owner-specific coverage.

## Guardrail Disposition

`Guardrail` is allowed for a patch-note item only when the selected source supports a
version-aware warning but not a definitive customer answer without more input.

Valid `Guardrail` reasons include:

- The customer asks whether a patch is the root cause or fix for their live incident,
  but the answer requires their exact installed patch, platform, logs, SQL, object
  definitions, workload, or runtime output.
- The patch note lists a feature or fix, but production safety depends on environment
  validation or an owner manual procedure not present in the selected source.
- The patch note mentions protocol, binary, meta, or replication compatibility, but
  the customer's mixed-version topology is unknown.

Invalid `Guardrail` uses:

- Marking a source-backed patch row as closed merely because it is patch-specific.
- Dropping `BUG-*` or `TASK-*` tokens from attachment coverage.
- Replacing a source-backed change with generic database or Oracle assumptions.

A `Guardrail` row still needs an attachment anchor with a customer-safe response rule:
ask for the missing input, cite the exact patch boundary, and route the next check.

## Out-of-Scope Disposition

`Out-of-scope` should be rare for the active 115 rows because they were selected as
in-scope patch-note rows.

Use `Out-of-scope` only when the specific claim to be closed is outside the approved
upload corpus, for example:

- The source row depends on an external bug tracker, code repository, or document not
  selected for the attachment corpus.
- The requested claim concerns an unsupported version, platform, product, or
  third-party behavior not covered by the selected source inventory.
- The source text is only a pointer to non-selected material and does not state a
  customer-answerable Altibase behavior.

Do not use `Out-of-scope` for a normal patch-note feature, fixed bug, version-info
table, property list, performance-view list, or compatibility note in the selected
patch-note files.

## Downstream Closure Checklist

Each `PWF-J003` through `PWF-J014` remediation job should:

1. Re-run the required first checks and stop on uncommitted project files outside
   `.codex-jobs/`.
2. Inspect every scoped patch-note file, not just catalog summaries.
3. Add compact attachment blocks or owner routing, without editing original patch
   notes.
4. Update catalog and matrix rows from `Missing` to `Covered`, `Covered-by-routing`,
   `Guardrail`, or `Out-of-scope`.
5. Update `missing_item_register.md`, `guardrail_register.md`,
   `remediation_log.md`, and `final_full_coverage_audit.md` as required by the
   register state.
6. Run:

```bash
python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers
git diff --check
bash review/scripts/run_review_stage.sh validate
```

7. Review the scoped diff and commit only the job-owned project files with explicit
   path staging.

This design intentionally does not perform the broad patch-note remediation itself.
