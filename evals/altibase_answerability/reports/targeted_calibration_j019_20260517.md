# Altibase Targeted Benchmark Calibration

- Job: `J019`
- Date: 2026-05-17
- Evidence run: `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_095919/`
- Current attachment context: repository `GPTs/attachments/*.md` after J004-J018 remediation
- Target questions: `PROP-101`, `PROP-105`, `PROP-117`, `SQL-103`, `SQL-108`, `SQL-142`, `OPS-117`, `REPL-118`, `ERR-116`, `VPM-112`, `TOOL-010`, `TOOL-036`

## Reconfirmed Requirement And Boundary

J019 calibrates representative failed benchmark questions before residual remediation.
It does not edit `GPTs/attachments/`, original manuals, benchmark thresholds, expected
facts, required tokens, or judge rules.

This job records whether sampled failures now look like:

- `content gap`: missed item is absent from the full current attachment set;
- `retrieval gap`: missed item is present in the full current attachment set but absent
  from current lexical context;
- `answer synthesis gap`: missed item is already present in current lexical context but
  the 2026-05-17 answer omitted, weakened, or changed its token form;
- `judge calibration issue`: suspected only after checking source/context and the old
  answer path.

## Design Note

J019 adds one durable instruction-aware manifest:
`evals/altibase_answerability/manifests/targeted_calibration_j019_instruction.json`.
The manifest keeps the same question allowlist and attachment boundary as
`full_benchmark.json`, but explicitly includes `GPTs/GPT_Instructions_Draft.md` so a
targeted run can compare the generic benchmark scaffold with the upload GPT answer
contract.

The full attachment set is about `1,871,642` characters before prompt overhead, so this
job uses full-context dry-run coverage checks rather than a live full-context answer
generation run. Live full-context answer generation should be attempted only after
confirming the chosen model and runtime budget can safely handle that prompt size.

## Method

For each target question, J019 compared the 2026-05-17 failed answer with the current
attachment corpus:

1. Loaded the old answer and judgment from the full benchmark run.
2. Rebuilt current lexical context with `context_mode=lexical`,
   `max_context_chars=180000`, and `chunk_chars=8000`.
3. Built full current attachment context with `context_mode=full` and
   `max_context_chars=0`.
4. Checked only the facts and tokens missed by the old answer, using the same
   `fact_match` and `literal_token_present` functions as `judge_report.py`.
5. Prepared and validated an instruction-aware dry-run path with the GPT instruction
   draft included in the prompt.

## Target Selection

The sample intentionally covers the major failure families from the 2026-05-17 run:

| Question | Reason selected |
| --- | --- |
| `PROP-101` | Property configuration model, static/dynamic/environment-variable precedence, protected property blocker. |
| `PROP-105` | Property path/count details where the old answer incorrectly said context was insufficient. |
| `PROP-117` | Result cache property values and numeric tokens, expected retrieval sensitivity. |
| `SQL-103` | Volatile tablespace DDL generation and exact syntax tokens. |
| `SQL-108` | Partition DDL generation and `ALTER TABLE ADD PARTITION`. |
| `SQL-142` | Identifier and Oracle-difference tokens with many literal characters. |
| `OPS-117` | Incomplete recovery and `META RESETLOGS`, protected backup/recovery blocker. |
| `REPL-118` | Replication/network diagnostic tokens, protected replication-state path. |
| `ERR-116` | Error-code token form mismatch, hexadecimal not-found family. |
| `VPM-112` | Performance view column preservation. |
| `TOOL-010` | JDBC failover property and exact example token preservation. |
| `TOOL-036` | Utility/error token preservation across tool and error-reference blocks. |

## Calibration Results

| Question | Domain | Old severity | Missed item availability in current lexical vs full | Dominant calibration result |
| --- | --- | --- | --- | --- |
| `PROP-101` | `properties/configuration_model` | `blocker` | `3/3` lexical, `3/3` full | `answer synthesis gap`; current lexical context has all missed items. |
| `PROP-105` | `properties/database_file_paths` | `blocker` | `7/7` lexical, `7/7` full | `answer synthesis gap`; current lexical context has all missed items. |
| `PROP-117` | `properties/result_cache` | `blocker` | `5/9` lexical, `9/9` full | `retrieval gap` remains; full context has all missed items. |
| `SQL-103` | `sql_ddl_dml_datatypes/ddl_generation` | `high` | `4/4` lexical, `4/4` full | `answer synthesis gap`; current lexical context has all missed items. |
| `SQL-108` | `sql_ddl_dml_datatypes/ddl_generation` | `high` | `5/5` lexical, `5/5` full | `answer synthesis gap`; current lexical context has all missed items. |
| `SQL-142` | `sql_ddl_dml_datatypes/oracle_differences` | `high` | `17/17` lexical, `17/17` full | `answer synthesis gap`; current lexical context has all missed items. |
| `OPS-117` | `operations_admin/backup_restore_recovery` | `blocker` | `6/6` lexical, `6/6` full | `answer synthesis gap`; current lexical context has all missed items. |
| `REPL-118` | `replication_cdc_security_network/compatibility_network_diagnostics` | `blocker` | `12/12` lexical, `12/12` full | `answer synthesis gap`; current lexical context has all missed items. |
| `ERR-116` | `errors_troubleshooting/sql_property_errors` | `high` | `8/8` lexical, `8/8` full | `answer synthesis gap`; current lexical context has all missed items. |
| `VPM-112` | `views_performance_monitoring/performance_views_check_sql` | `medium` | `3/3` lexical, `3/3` full | `answer synthesis gap`; current lexical context has all missed items. |
| `TOOL-010` | `tools_apis_connectors_migration/jdbc_java_spring_hibernate` | `high` | `5/5` lexical, `5/5` full | `answer synthesis gap`; current lexical context has all missed items. |
| `TOOL-036` | `tools_apis_connectors_migration/utilities_datacompj` | `high` | `6/6` lexical, `6/6` full | `answer synthesis gap`; current lexical context has all missed items. |

## Full-Context Comparison

No sampled missed item was absent from the full current attachment set. That means this
sample does not support broad content additions before J020. The full-context check is
still useful because it separates true content absence from retrieval targeting:

- `PROP-117` has a current lexical retrieval miss for the result-cache detail set:
  expected fact `F02` plus tokens `10M`, `4096`, and `ULONG MAX` are present in the full
  current attachment set but not in the current lexical context selected for the
  question.
- The other 11 sampled failures have every previously missed item in current lexical
  context, so re-running them with full context should not be necessary to diagnose the
  dominant failure class.

## Instruction-Aware Comparison

The instruction-aware manifest changes the prompt contract, not the attachment
selection. It is expected to help the 11 synthesis-dominant samples because
`GPTs/GPT_Instructions_Draft.md` explicitly requires complete reference answers, exact
token preservation, version scope, protected-topic guardrails, and no over-compression
of defaults/ranges/units/error-code forms.

It is not expected to fix `PROP-117` by itself because the missed result-cache tokens
are not in the current lexical context. J020 should first improve retrieval routing for
that property block, then test whether the instruction-aware prompt preserves `10M`,
`4096`, `ULONG MAX`, and `ALTER SYSTEM`.

## Judge Calibration Notes

No sampled failure is safe to classify as judge-only. The closest calibration candidate
is `PROP-101`: the old answer used `Environment variable` with capital `E`, while the
required token is `environment variable`, and it summarized read-only/single-value
behavior rather than repeating the exact expected phrase. That is a token-form and
answer-shape issue first. If an instruction-aware live answer still preserves the same
facts but fails only on case for non-code prose tokens, then judge token
case-sensitivity can be reviewed as a later calibration issue.

`ERR-116` is not a judge issue: the old answer used `ERR-31010` style codes while the
expected tokens require hexadecimal `0x31010` through `0x31017`. Current lexical context
now contains the hexadecimal forms, so the next live run should test synthesis and
token preservation.

## J020 Handoff

- Prioritize instruction-aware targeted live runs for the 11 synthesis-dominant sample
  questions before adding new content.
- Fix the sampled residual retrieval gap for `PROP-117` by strengthening result-cache
  retrieval aliases or compact heading/index text so `RESULT_CACHE_MEMORY_MAXIMUM`,
  `RESULT_CACHE_MEMORY_SIZE`, `10M`, `4096`, and `ULONG MAX` are selected together.
- Do not lower benchmark thresholds or rewrite expected questions. The sampled failures
  still represent real customer-answer risks: exact values and tokens were available
  but not reliably emitted.
- Review judge calibration only after instruction-aware targeted live answers are
  available and only for non-code prose-token case sensitivity or equivalent semantic
  false negatives.

## Reproduction Commands

Use the same 12 question ids for all targeted modes:

```bash
TARGET_IDS=(
  PROP-101 PROP-105 PROP-117 SQL-103 SQL-108 SQL-142
  OPS-117 REPL-118 ERR-116 VPM-112 TOOL-010 TOOL-036
)
QUESTION_ARGS=()
for id in "${TARGET_IDS[@]}"; do
  QUESTION_ARGS+=(--question-id "$id")
done
```

Current lexical dry-run:

```bash
python3 evals/altibase_answerability/scripts/answer_runner.py \
  --manifest evals/altibase_answerability/manifests/full_benchmark.json \
  --mode dry_run \
  --context-mode lexical \
  --validate-output \
  --output-dir /tmp/altibase-j019-calibration-lexical \
  "${QUESTION_ARGS[@]}"
```

Full-context dry-run:

```bash
python3 evals/altibase_answerability/scripts/answer_runner.py \
  --manifest evals/altibase_answerability/manifests/full_benchmark.json \
  --mode dry_run \
  --context-mode full \
  --max-context-chars 0 \
  --validate-output \
  --output-dir /tmp/altibase-j019-calibration-full \
  "${QUESTION_ARGS[@]}"
```

Instruction-aware lexical dry-run:

```bash
python3 evals/altibase_answerability/scripts/answer_runner.py \
  --manifest evals/altibase_answerability/manifests/targeted_calibration_j019_instruction.json \
  --mode dry_run \
  --context-mode lexical \
  --validate-output \
  --output-dir /tmp/altibase-j019-calibration-instruction \
  "${QUESTION_ARGS[@]}"
```
