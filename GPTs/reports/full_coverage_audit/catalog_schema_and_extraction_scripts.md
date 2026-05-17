# Full Coverage Audit Catalog Schema And Extraction Scripts

- Workflow: `altibase-gpt-full-coverage-audit`
- Audit job: `FCA-J003`
- Status: Active schema and tooling baseline for later FCA jobs
- Date: 2026-05-18

## Job Boundary

`FCA-J003` defines the source-item catalog schema, source-to-attachment matrix schema,
controlled vocabularies, stable ID rules, and reusable extraction/check scripts for the
full coverage audit.

This job does not catalog product items from source manuals, change customer-facing
attachments, edit GPT instructions, edit original manuals, or decide final coverage.
Later catalog jobs must append or update only their scoped rows and must preserve rows
created by other jobs.

## Inputs Inspected

The schema was derived from these repository-local artifacts:

- `AGENTS.md`
- `.codex-jobs/altibase-gpt-full-coverage-audit/jobs.tsv`
- `.codex-jobs/altibase-gpt-full-coverage-audit/jobs.md`
- `GPTs/attachments/README.md`
- `GPTs/GPT_Instructions_Draft.md`
- `GPTs/reports/source_inventory.md`
- `GPTs/reports/coverage_matrix.md`
- `GPTs/reports/gap_register.md`
- `GPTs/reports/catalog_schema_extraction_rules.md`
- `GPTs/reports/full_coverage_audit/source_corpus_lock.md`
- `evals/altibase_answerability/reports/full_benchmark/failure_root_cause_analysis_20260517.md`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_205641/summary.txt`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_205641/judge/report.md`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_205641/judge/aggregate_report.json`

Benchmark evidence reinforces the need for exact token preservation, item-level blocks,
and retrieval-routing proof, but the benchmark questions are not the audit scope.

## Catalog TSV Schema

Canonical file:

`GPTs/reports/full_coverage_audit/source_item_catalog.tsv`

Required columns, in order:

| Column | Required content |
| --- | --- |
| `source_item_id` | Stable ID following the rules below. |
| `source_family` | One frozen source family from `source_corpus_lock.md`. |
| `version_scope` | `7.1`, `7.3`, `8.1`, `cross-version`, or `patch-specific`. |
| `source_path` | Repository-relative selected source path. |
| `source_heading` | Heading path or nearest stable anchor in the source. |
| `item_type` | Controlled item type from this report. |
| `literal_tokens` | Exact tokens that must survive into customer answers. Separate multiple tokens with `; `. |
| `source_summary` | Short normalized English summary of the source-backed item. |
| `attachment_target` | Expected owner in `GPTs/attachments/*.md`, or `N/A` only for `Out-of-scope`. |
| `coverage_status` | One disposition value from this report. |
| `attachment_anchor` | Attachment heading or line evidence when represented; blank is allowed for unresolved `Missing`. |
| `guardrail_reason` | Required for `Guardrail` and `Out-of-scope`; otherwise blank unless useful. |
| `audit_job` | FCA job ID that created or last reviewed the row. |
| `evidence` | Command, grep, source locator, script output, or review evidence. |

Catalog rows must be source-backed. Do not create a row from generic Altibase memory,
Oracle behavior, or a benchmark expected answer unless the selected repository-local
source item is also located.

## Matrix TSV Schema

Canonical file:

`GPTs/reports/full_coverage_audit/source_to_attachment_matrix.tsv`

Required columns, in order:

| Column | Required content |
| --- | --- |
| `source_item_id` | Existing catalog ID. |
| `source_family` | Source family copied from or checked against the catalog. |
| `version_scope` | Version scope copied from or checked against the catalog. |
| `source_path` | Repository-relative selected source path. |
| `source_heading` | Source heading path or stable anchor. |
| `item_type` | Controlled item type. |
| `attachment_target` | Attachment owner or `N/A` for `Out-of-scope`. |
| `coverage_status` | Current disposition for this mapping. |
| `attachment_anchor` | Exact attachment heading, line locator, or routing anchor. |
| `routing_aliases` | Retrieval aliases or index terms when coverage depends on routing. |
| `matrix_notes` | Short coverage note, including answer-readiness gaps when present. |
| `guardrail_reason` | Required for `Guardrail` and `Out-of-scope`. |
| `audit_job` | FCA job ID that created or last reviewed the row. |
| `evidence` | Matrix check command, grep, source/attachment locator, or review evidence. |

The matrix may later contain multiple rows for one `source_item_id` when a source item
is intentionally represented across more than one attachment. Duplicate
`source_item_id` plus `attachment_target` pairs are not allowed.

## Controlled Vocabularies

### Source Families

Use only these family IDs unless a later committed support-report update explicitly
extends the corpus:

- `release_notes_platform`
- `patch_notes`
- `getting_started_installation`
- `administrator_operations`
- `sql_reference`
- `general_reference_1_datatypes_properties`
- `general_reference_2_dictionary_views`
- `error_message_reference`
- `performance_tuning`
- `monitoring_api_snmp`
- `replication_manual`
- `log_analyzer`
- `replication_manager`
- `security_ssl_tls`
- `stored_external_procedures`
- `jdbc_java`
- `c_cli_odbc_precompiler`
- `isql_iloader`
- `utilities_datacompj`
- `migration_oracle`
- `dblink_hadoop_external_connectors`
- `kubernetes_aku`
- `spatial_nifi_tableau`
- `technical_documents_support`
- `third_party_guides`

### Version Scopes

- `7.1`: source item applies to Altibase 7.1.
- `7.3`: source item applies to Altibase 7.3.
- `8.1`: source item applies to the Altibase 8.1 verified source.
- `cross-version`: source item is common across multiple supported versions and the row
  evidence lists the checked versions.
- `patch-specific`: source item is tied to an exact patch note, release note, or other
  patch/version boundary.

### Coverage Statuses

- `Covered`: represented in `GPTs/attachments/` as an answer-ready block.
- `Covered-by-routing`: represented through a clearly linked section plus retrieval
  alias, index, or routing entry.
- `Guardrail`: selected sources do not support a definitive customer answer, or the
  answer depends on exact version, patch level, environment, object definition, log
  excerpt, runtime output, installed tool behavior, or live integration state.
- `Out-of-scope`: outside the selected upload source corpus, with a recorded reason.
- `Missing`: source-backed and in scope but not answerable from the attachments.
- `Retrieval-weak`: present but unlikely to be found by GPT retrieval.

The final audit cannot retain unresolved `Missing` or unresolved `Retrieval-weak` rows.

### Item Types

- `property`
- `SQL syntax`
- `command option`
- `view`
- `column`
- `error code`
- `API`
- `runbook step`
- `compatibility rule`
- `version note`
- `warning`
- `example`
- `data type`
- `function`
- `tool command`
- `connector setting`
- `release note`
- `platform rule`
- `other documented category`

Use the most specific type that controls the answer-ready standard. For example, a
documented iLoader flag is `command option`, while a whole iLoader execution workflow is
`runbook step`.

## Stable ID Rules

Stable IDs use this format:

```text
SRC-<KIND>-<VERSION_CODE>-<NNNNNN>
```

Rules:

- `SRC` is literal.
- `<KIND>` is an uppercase compact class code, such as `PROP`, `SQL`, `VIEW`, `ERR`,
  `TOOL`, `API`, `REPL`, `SEC`, `MIGR`, `SPAT`, `REL`, or `OTHER`.
- `<VERSION_CODE>` is `7.1`, `7.3`, `8.1`, `XVER` for `cross-version`, or `PATCH` for
  `patch-specific`.
- `<NNNNNN>` is a six-digit sequence within the `<KIND>-<VERSION_CODE>` namespace.
- IDs are never reused after a row is deleted or merged. Deprecate the row in notes or
  leave a trace in the relevant register instead.
- When one documented item has separate version-specific behavior, prefer separate
  version rows. Use `cross-version` only when the checked source evidence is materially
  the same across supported versions.
- When a heading contains many answerable subitems, create one row per customer-answer
  unit rather than one broad chapter row.

Example:

```text
SRC-PROP-7.3-000123
SRC-SQL-XVER-000042
SRC-ERR-PATCH-000007
```

## Extraction Workflow For Later Jobs

1. Reconfirm the job boundary from `jobs.tsv` and `jobs.md`.
2. Use `source_corpus_lock.md` and `coverage_matrix.md` to select the source family,
   authority source, extraction aid, and attachment owner.
3. Inspect Korean source first when a paired Korean source exists.
4. Use English source only as an extraction aid unless no paired Korean source exists.
5. Extract one row per answerable item, preserving literal tokens and source anchors.
6. Set `coverage_status` conservatively:
   - use `Missing` when source-backed content is absent from attachments;
   - use `Retrieval-weak` when present but hard to find;
   - use `Guardrail` only for explicit source or customer-evidence limitations;
   - use `Out-of-scope` only when the item is outside the locked selected corpus.
7. Update the register that matches every unresolved or guarded disposition.
8. Run the TSV checker plus standard repository validation before committing.

## Reusable Scripts

Script:

`GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py`

The script uses only the Python standard library. It does not write canonical catalog
rows; `build-matrix` is the explicit exception for initializing
`source_to_attachment_matrix.tsv` from already reviewed catalog rows.

Validate initialized or populated TSVs:

```bash
python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers
```

Run stricter catalog consolidation QA before matrix mapping:

```bash
python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py catalog-qa
```

Initialize the source-to-attachment matrix from the validated catalog:

```bash
python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py build-matrix \
  --audit-job FCA-J040
```

Validate that every catalog row has a matrix mapping and that copied fields still match:

```bash
python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py matrix-qa
```

Generate a source heading outline as extraction aid:

```bash
python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py outline \
  --source-family sql_reference \
  Manuals/Altibase_7.3/kor/SQL\ Reference.md
```

Get the next stable ID in a namespace:

```bash
python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py next-id \
  --kind-code SQL \
  --version-code 7.3
```

The checker enforces:

- required catalog and matrix columns;
- duplicate `source_item_id` detection in the catalog;
- duplicate `source_item_id` plus `attachment_target` pairs in the matrix;
- valid `source_family`, `version_scope`, `coverage_status`, and `item_type` values;
- repository-relative `source_path` values;
- valid attachment targets for non-`Out-of-scope` rows;
- non-empty `source_path`, `source_summary`, `audit_job`, and `evidence` in catalog rows;
- non-empty `source_path`, `audit_job`, and `evidence` in matrix rows;
- required `guardrail_reason` for `Guardrail` and `Out-of-scope` rows;
- presence of the initialized register/report files when `--require-registers` is used.

The `matrix-qa` command also checks:

- canonical catalog and matrix column order;
- at least one matrix row for every catalog `source_item_id`;
- the initial catalog `source_item_id` plus `attachment_target` mapping is present;
- copied matrix fields match the catalog for source family, version scope, source path,
  source heading, item type, coverage status, attachment anchor, and guardrail reason;
- non-empty `routing_aliases`, `matrix_notes`, `audit_job`, and `evidence` fields.

The stricter `catalog-qa` command also checks:

- canonical catalog and matrix column order;
- `source_item_id` version-code consistency with `version_scope`;
- non-empty `source_heading`, `literal_tokens`, and `source_summary`;
- existing repository-relative `source_path` files;
- non-empty `attachment_anchor` for represented `Covered`, `Covered-by-routing`,
  `Guardrail`, and `Retrieval-weak` rows;
- all controlled source families have at least one catalog row;
- ID namespace sequence-gap count for stable-ID review; sequence gaps are not fatal
  because retired IDs must not be reused;
- every unresolved `Missing`, `Guardrail`, `Out-of-scope`, and `Retrieval-weak`
  catalog row is mentioned in the matching register.

## Register Update Rules

- `missing_item_register.md`: every unresolved `Missing` row must appear here until it
  becomes `Covered`, `Covered-by-routing`, `Guardrail`, or `Out-of-scope`.
- `retrieval_weakness_register.md`: every unresolved `Retrieval-weak` row must appear
  here until retrieval routing is fixed or the row receives another justified
  disposition.
- `guardrail_register.md`: every `Guardrail` or `Out-of-scope` row must appear here
  with the missing input or source-boundary reason and safest next check.
- `remediation_log.md`: every later attachment, instruction, support-report, or matrix
  remediation should record changed files, source rows, validation, and residual risk.
- `final_full_coverage_audit.md`: remains a non-final placeholder until FCA-J051.

## FCA-J003 Verification Plan

Required checks for this job and later schema users:

```bash
python3 GPTs/reports/full_coverage_audit/scripts/fca_catalog_tools.py check --require-registers
git diff --check
bash review/scripts/run_review_stage.sh validate
rg -n "^Verdict:|^\| (Blocker|High|Medium|Low) \|" review/reports/R*.md
```

Later catalog jobs should also run a scoped `outline` or source-location command and
record it in the `evidence` field for every row they add or update.
