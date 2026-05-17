# Altibase GPT Answerability Failure Root-Cause Analysis

- Date: 2026-05-17
- Baseline before GPTs update: `runs/altibase_answerability_20260516_145452/`
- Baseline after GPTs upgrade: `runs/altibase_answerability_20260517_095919/`
- Main evidence used: `summary.txt`, `judge/aggregate_report.json`,
  `judge/judgments.jsonl`, `answers/answers.jsonl`, durable question JSONL files,
  `answer_runner.py`, and `judge_report.py`
- Scope: root-cause analysis before modifying `GPTs/attachments/`

## Executive Conclusion

The second benchmark result still blocks upload readiness, but the failures do not mean
the attachment set is simply empty or globally missing every expected source fact.

The dominant problem is that benchmark answers do not consistently extract and preserve
the exact source-backed facts and literal tokens that are already reachable from the
full attachment set. In the 2026-05-17 run, 352 critical expected fact items were missed
by answers. A rule-judge approximation found:

| Critical-fact miss class | Missed critical fact items | Share |
| --- | ---: | ---: |
| Answer synthesis / extraction gap: fact appears in selected context but answer omits or weakens it | 322 | 91.5% |
| Retrieval gap: fact appears in full attachments but not in selected lexical context | 26 | 7.4% |
| Attachment content gap or fact-wording mismatch: fact is not matchable in full attachments | 4 | 1.1% |

Token preservation tells a more balanced story. The second run missed 525 required
literal token items:

| Required-token miss class | Missed token items | Share |
| --- | ---: | ---: |
| Token appears in selected context but answer omits it | 310 | 59.0% |
| Token is absent from the full attachment set | 110 | 21.0% |
| Token appears in full attachments but not in selected lexical context | 105 | 20.0% |

So the remediation should not begin by blindly adding more prose. The first fix should
separate three work streams:

1. Make existing facts easier for GPT answers to extract as complete, literal reference
   answers.
2. Add missing item-level tokens and exact syntax blocks where the attachment set truly
   lacks them.
3. Improve or validate retrieval behavior, because lexical context is broad but still
   misses exact tokens and sometimes sends the model noisy, diluted context.

## Benchmark Status

| Metric | 1st test before GPTs update | 2nd test after GPTs upgrade | Change |
| --- | ---: | ---: | ---: |
| Readiness decision | `blocking_gaps` | `blocking_gaps` | unchanged |
| Passed / total | 24 / 270 | 27 / 270 | +3 |
| Pass rate | 8.9% | 10.0% | +1.1pp |
| Critical fact coverage | 68.3% | 68.7% | +0.4pp |
| Required token preservation | 73.4% | 74.6% | +1.2pp |
| Unsupported-claim rate | 0.0% | 0.4% | -0.4pp |
| Protected-topic blockers | 81 | 77 | -4 |

The second run improved slightly overall, but it is still far below the readiness
thresholds:

- overall pass rate threshold: 85.0%;
- per-domain pass-rate threshold: 80.0%;
- critical fact coverage threshold: 90.0%;
- required token preservation threshold: 95.0%;
- protected-topic blocker allowance: 0.

## Domain Pattern

| Domain | 2nd run pass rate | Passed / total | Main failure categories |
| --- | ---: | ---: | --- |
| `errors_troubleshooting` | 3.3% | 1 / 30 | critical fact misses, token misses |
| `operations_admin` | 8.6% | 3 / 35 | critical fact misses, token misses, version handling |
| `properties` | 12.0% | 6 / 50 | critical fact misses, token misses, protected property blockers |
| `replication_cdc_security_network` | 10.0% | 3 / 30 | critical fact misses, token misses, replication blockers |
| `sql_ddl_dml_datatypes` | 4.4% | 2 / 45 | SQL token misses, critical fact misses, one prohibited-claim hit |
| `tools_apis_connectors_migration` | 18.0% | 9 / 50 | token misses, critical fact misses, version handling |
| `views_performance_monitoring` | 10.0% | 3 / 30 | token misses, critical fact misses, version handling |

The worst zero-pass subdomains include:

| Subdomain | Questions | Pass rate | Max severity |
| --- | ---: | ---: | --- |
| `sql_property_errors` | 12 | 0.0% | blocker |
| `ddl_generation` | 10 | 0.0% | blocker |
| `dml_expressions_functions` | 9 | 0.0% | high |
| `optimizer_plan_tuning` | 8 | 0.0% | high |
| `accounts_tablespaces_admin` | 7 | 0.0% | blocker |
| `performance_views_check_sql` | 7 | 0.0% | blocker |
| `psm_external_procedures` | 7 | 0.0% | high |
| `replication_state_changes` | 6 | 0.0% | high |
| `syntax_restrictions_examples` | 6 | 0.0% | blocker |

This is not isolated to one attachment file. The low pass rate is systemic across
properties, SQL generation, troubleshooting, operations, replication, and monitoring.

## Why The Result Is Still So Low

### 1. The benchmark asks for exact manual-style answers, not short FAQ answers

The benchmark is intentionally strict. It is designed to test whether the upload set can
answer manual-backed questions from selected Altibase sources. Many questions require:

- exact property defaults, ranges, mutability, and version boundaries;
- exact SQL grammar tokens and command forms;
- exact error codes, symbols, cause/action patterns, and diagnostic checks;
- exact operational cautions for backup/recovery, replication state changes, TLS, and
  destructive SQL;
- exact version-specific or patch-specific wording.

The 2nd run question mix is also hard:

| Dimension | Questions | Passed | Pass rate |
| --- | ---: | ---: | ---: |
| high retrieval risk | 176 | 15 | 8.5% |
| `sql_generation` answers | 29 | 1 | 3.4% |
| `troubleshooting` answers | 57 | 3 | 5.3% |
| expert user level | 51 | 3 | 5.9% |
| developer user level | 65 | 5 | 7.7% |

Therefore a concise but directionally correct answer often fails because it omits one
or more literal tokens, numeric bounds, version labels, or high-risk caveats.

### 2. Answers frequently omit facts that are already in selected context

The most important finding is the critical-fact classification. Of 352 missed critical
fact items, 322 were classed as answer synthesis / extraction gaps. This means the same
rule judge could match the expected fact in the selected lexical context, but not in
the final answer.

Representative examples:

- `PROP-101`: the answer discussed static and dynamic properties, but the rule judge
  still missed the explicit static-property fact and the read-only environment-variable
  restart fact. The answer was close, but not literal or complete enough for the
  expected facts.
- `PROP-103`: the answer stated `DB_NAME` default and non-dynamic behavior, but omitted
  the expected read-only, single-value, no-explicit-range classification.
- `PROP-107`: the answer gave the changed 8.1 maximum as `4294967295`, but did not
  preserve the full expected release-note comparison phrase
  `18446744073709551615 to 4294967295`.
- `ERR-116`: the answer gave `ERR-31010` style codes, while the required token block
  expected `0x31010` style codes. That is a token-form preservation failure, not an
  absence of the troubleshooting topic.

This indicates that the GPT-facing answer style is too summarizing and too willing to
compress exact reference data. More content alone will not fix this class unless the
content is reorganized into answer-ready, item-level blocks that are easy to quote
literally.

### 3. Literal token preservation is a major independent failure mode

The 2nd run had 201 questions with `missing_required_tokens` findings. Token misses
matter because Altibase answers often depend on exact SQL syntax, property names,
view names, command options, numeric limits, and error codes.

Token miss classes:

| Class | Count | Typical examples |
| --- | ---: | --- |
| Token in selected context, omitted by answer | 310 | `VALUE1`, `2^64`, `ALTER SYSTEM`, `environment variable` |
| Token absent from full attachments | 110 | `CREATE VOLATILE TABLESPACE`, `ALTER TABLE ADD PARTITION`, `10M`, `ULONG MAX`, `PERMIT`, `DENY` |
| Token present in full attachments, missed by retrieval | 105 | `STOREDCOUNT`, `VALUE8`, `2097152`, `V$ACCESS_LIST`, `ACCESS_LIST_FILE` |

This is the strongest evidence that two different remediation styles are needed:

- add missing exact tokens and syntax forms where the full attachment set lacks them;
- rewrite or index existing blocks so GPT answers preserve literal forms instead of
  paraphrasing them away.

### 4. Lexical retrieval is broad, noisy, and still not exact enough

The runner used `context_mode=lexical` with a 180,000-character context budget. The
reconstructed context profile is:

| Retrieval context statistic | Value |
| --- | ---: |
| Average selected context size | about 179,956 characters |
| Average selected chunks | 48.4 |
| Average selected attachment files | 12.7 |
| Minimum / maximum selected context size | 179,859 / 179,997 characters |

This means the prompt is nearly always filled to the maximum budget. It is not a small
context problem. It is a targeting and signal-density problem.

Highly frequent selected files:

| Attachment file | Selected in questions |
| --- | ---: |
| `00_version_release_platform.md` | 257 / 270 |
| `09_replication_ha_cdc.md` | 245 / 270 |
| `07_error_messages_troubleshooting.md` | 241 / 270 |
| `03_sql_ddl_generation.md` | 232 / 270 |
| `05_data_types_properties.md` | 231 / 270 |
| `11_java_jdbc_spring.md` | 231 / 270 |

The context is broad enough to contain many answerable facts, but broad context can
dilute the exact block the model needs. Lexical scoring uses only the allowed question
input, not judge-only required tokens or expected facts. That is correct for leakage
control, but it means exact source blocks for numeric bounds or syntax variants can be
missed unless the public question text includes the same terms.

### 5. Some answers incorrectly say the attachment context is insufficient

Several failed answers explicitly say the attachment context does not contain a fact
that the full attachment set can match. Examples include:

- `PROP-105` on `LOGANCHOR_DIR`: the answer says the context does not provide default,
  maximum count, or dynamic-change rules, but the full-attachment approximation matched
  the expected facts.
- `PROP-108`, `PROP-109`, `PROP-112`, `PROP-120`, and `PROP-124`: answers fell back to
  `V$PROPERTY` checks instead of providing expected property details.

This is a useful safety behavior for real customer support when the context is truly
insufficient, but in this benchmark it becomes a failure when the relevant source-backed
fact is present but not selected or not recognized.

### 6. The answer runner did not include the GPT instruction draft

The production manifest has:

```json
"include_gpt_instruction_draft": false
```

So the benchmark did not test the final GPT instruction draft as part of the prompt. It
tested a generic attachment-only benchmark prompt plus lexical attachment context.

This is useful for isolating attachment answerability, but it also means the run may
understate the value of GPT instructions that force:

- complete reference answers;
- exact literal token preservation;
- version-scope statements;
- refusal to generalize from Oracle behavior;
- structured property and SQL answer formats.

Before changing large amounts of attachment content, a controlled calibration run with
the instruction draft enabled, or an equivalent prompt profile, should be considered.

### 7. The rule judge is strict and partly lexical

The judge is intentionally conservative. It does not call a semantic model. It matches
expected facts using normalized term overlap plus technical-term overlap, and it checks
required tokens literally.

This produces some false-negative risk where an answer is semantically acceptable but
not phrased in the expected terms. However, the result should not be dismissed as only
a judge artifact:

- 201 questions missed literal required tokens;
- 183 questions missed critical facts;
- 77 questions still had protected-topic blockers;
- many failed answers genuinely omitted numeric bounds, exact syntax, exact code forms,
  or version-sensitive caveats.

The judge is strict, but it is exposing real answerability weaknesses for a manual-style
Altibase GPT.

## Protected Topic Risk

Protected-topic blockers fell from 81 to 77, but readiness still blocks because the
allowed count is zero.

| Protected topic | 1st run | 2nd run | Change |
| --- | ---: | ---: | ---: |
| backup/recovery | 22 | 22 | 0 |
| destructive SQL | 5 | 7 | +2 |
| replication state changes | 12 | 14 | +2 |
| security/TLS | 11 | 9 | -2 |
| version-sensitive property changes | 31 | 25 | -6 |

The blocker profile shows that the GPTs are not ready for high-risk operational
answers. This does not necessarily require more total volume, but it does require more
deterministic answer paths for:

- backup and recovery sequences;
- destructive DDL/DCL/administrative operations;
- replication start/stop/reset/rebuild and gap handling;
- SSL/TLS and replication TLS separation;
- dynamic versus static property changes.

## Domain-Specific Root Causes

### Properties

Properties improved from 6.0% to 12.0%, but still fail 44 of 50 questions. It has the
largest critical-fact miss count in the 2nd run.

Key failure pattern:

- many property-specific defaults, ranges, units, mutability flags, and side effects are
  not emitted even when the property name is found;
- property answers often fall back to generic `V$PROPERTY` checks instead of providing
  the expected manual-backed item detail;
- some required tokens are absent from the full attachment set, especially exact
  values or terms such as `10M`, `ULONG MAX`, `NNF`, `PERMIT`, and `DENY`.

Interpretation: this domain needs dense item-level property blocks and answer templates
that require default/range/unit/mutability/dynamic-change/version fields.

### SQL, DDL, DML, Data Types

SQL pass rate regressed from 8.9% to 4.4%. It is the weakest domain after
`errors_troubleshooting`.

Key failure pattern:

- SQL generation answers omit exact grammar tokens;
- some syntax tokens are absent from the full attachment set, for example
  `CREATE VOLATILE TABLESPACE`, `CREATE DISK TABLESPACE`, `ALTER TABLE ADD PARTITION`,
  `table_compression_clause`, `LOB(column_name)`, and `multiple_update`;
- concise answers often provide a safe pattern but miss required caveats such as
  destructive `REUSE`, default `AUTOEXTEND` behavior, object-name rules, or non-autocommit
  restrictions.

Interpretation: this domain needs exact syntax mini-reference blocks and generated-SQL
checklists, not just explanatory prose.

### Errors And Troubleshooting

This domain regressed from 16.7% to 3.3%.

Key failure pattern:

- answers often describe the right troubleshooting direction but miss literal error
  code forms, reference symbols, or exact cause/action families;
- some answers use alternate code notation such as `ERR-31010` instead of required
  hexadecimal codes such as `0x31010`;
- high-risk operational errors still need safer evidence-gathering sequences.

Interpretation: error blocks must preserve the exact code, symbol, message, cause,
action, and first-check sequence in a compact answer-ready format.

### Operations And Administration

Operations improved from 2.9% to 8.6%, but still has many blocker findings.

Key failure pattern:

- startup, install, tablespace, backup/recovery, and log-file operations require exact
  command sequences and path tokens;
- answers omit required path names, command names, or post-operation safety checks;
- backup/recovery protected blockers remain flat at 22.

Interpretation: operations content should be structured as deterministic runbooks with
preconditions, commands, validation SQL, and stop conditions.

### Replication, CDC, Security, Network

Replication improved from 3.3% to 10.0%, but protected replication blockers increased.

Key failure pattern:

- answers explain concepts but miss exact state-change restrictions, protocol/version
  checks, compatibility details, and command boundaries;
- token misses include both omitted and absent items;
- replication state changes require stronger caution and verification gates.

Interpretation: replication needs state-machine style runbooks and exact DDL/control SQL
boundaries.

### Views, Performance, Monitoring

This domain improved from 6.7% to 10.0%.

Key failure pattern:

- answers often know to check `V$TABLE` or `V$ALLCOLUMN` but omit exact columns or
  view names;
- optimizer and plan-tuning subdomains have zero-pass clusters because answer detail is
  too compressed;
- monitoring answers need literal API/SNMP/view tokens.

Interpretation: monitoring and performance content needs query-ready view blocks and
example answer formats that preserve columns and caveats.

### Tools, APIs, Connectors, Migration

This is the best domain at 18.0%, but still far below the threshold.

Key failure pattern:

- PSM, utilities, APIs, connectors, and migration answers miss exact option names,
  syntax markers, command names, or version-specific connector caveats;
- some answers provide useful high-level guidance but not the full expected reference
  answer.

Interpretation: this domain likely benefits from exact command/API tables and concise
compatibility matrices.

## Should This Analysis Be Split Into Jobs?

The root-cause analysis itself did not need to be split. The aggregate and per-question
artifacts were structured enough to analyze in one pass.

However, remediation should be split. A single broad "improve GPTs" pass is likely to
repeat the current failure mode: adding prose without making the answer path more
deterministic.

Recommended remediation work packages:

| Work package | Purpose |
| --- | --- |
| RCA-R1 | Validate all `token_absent_from_attachments` items against source manuals and add only source-backed missing tokens/syntax blocks. |
| RCA-R2 | Build answer-ready property blocks for high-failure property questions: default, range, unit, mutability, dynamic-change support, version, caution. |
| RCA-R3 | Build SQL-generation syntax/caveat blocks for DDL/DML/data-type questions with literal grammar tokens. |
| RCA-R4 | Build high-risk runbook blocks for backup/recovery, destructive SQL, replication state changes, and TLS. |
| RCA-R5 | Calibrate retrieval by rerunning representative failures with full context, lexical context, and instruction-draft-enabled context. |
| RCA-R6 | Tune the answer format/prompt expectations so generated answers preserve required tokens and do not over-compress reference data. |
| RCA-R7 | Review rule-judge false negatives only after R1-R6, because current failures include many real omissions. |

## Immediate Recommendation

Before adding large amounts of new content, run a calibration cycle on a small but
representative subset:

- 10 property failures with token omissions;
- 10 SQL-generation failures with absent or omitted syntax tokens;
- 10 troubleshooting failures with exact error-code expectations;
- 10 protected-topic blockers across backup/recovery, replication, TLS, and destructive
  operations.

For each subset, compare:

1. current lexical context;
2. full attachment context;
3. lexical context plus GPT instruction draft;
4. updated answer-ready blocks.

This will tell whether each failure is best fixed by attachment content, retrieval
structure, or answer-generation instructions. The current evidence says all three
matter, but answer synthesis and literal-token preservation are the largest immediate
failure modes.
