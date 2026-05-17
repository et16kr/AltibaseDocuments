# Altibase GPT Customer Answer Contract

Job: `J002`
Status: Complete
Date: 2026-05-17

## Reconfirmed Requirement And Boundary

J002 updates the GPT answer contract so customer-facing answers preserve complete
source-backed Altibase detail for both first-time users and veteran operators or
developers.

This job is limited to the answer contract and GPT instruction layer:

- Updated: `GPTs/GPT_Instructions_Draft.md`
- Added: `GPTs/reports/customer_answer_contract.md`
- Not changed: `GPTs/attachments/*.md`, original manuals, benchmark thresholds, or
  benchmark question expectations

## Design Note

This job changes documentation behavior by making the GPT instruction draft more
deterministic. It does not add new Altibase product facts. Later attachment remediation
jobs still must source-check missing tokens and item-level content before changing
customer-facing attachment files.

The contract is evidence-driven:

- `answer synthesis gap`: primary J002 fix class. The 2026-05-17 root-cause analysis
  found 322 of 352 missed critical facts and 310 missed literal tokens already appeared
  in selected context but were omitted or weakened by answers.
- `retrieval gap`: acknowledged but assigned mainly to later retrieval and attachment
  structure jobs. J002 tells the GPT not to over-compress when the relevant block is
  found.
- `content gap`: not remediated by this job. Missing source-backed tokens remain for
  later source-checking jobs.
- `judge calibration issue`: not claimed by this job. Calibration is reserved for later
  instruction-aware and targeted benchmark work after source and answer paths are
  checked.

## Evidence Used

- `evals/altibase_answerability/reports/full_benchmark/failure_root_cause_analysis_20260517.md`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_095919/summary.txt`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_095919/judge/report.md`
- `GPTs/reports/answerability_failure_remediation_inventory_20260517.md`

Evidence snapshot:

| Metric | 2026-05-17 run |
| --- | ---: |
| Passed / total | 27 / 270 |
| Critical fact coverage | 68.7% |
| Required token preservation | 74.6% |
| Protected-topic blockers | 77 |
| Missed critical facts classed as answer synthesis gaps | 322 |
| Missed required tokens classed as answer synthesis gaps | 310 |

## Contract Changes

The instruction draft now requires:

- direct answers with explicit version scope or assumptions;
- beginner context plus veteran-grade exact tokens in the same answer when relevant;
- literal preservation of SQL, DDL, property, view, error, command, path, option, API,
  class, numeric, unit, and version tokens;
- domain-specific answer shapes for properties, SQL generation, views, errors,
  operations, replication, security, tools, APIs, connectors, and migration;
- protected-topic guardrails for backup/recovery, destructive SQL, replication state
  changes, security/TLS, and version-sensitive property changes;
- safe missing-input prompts for patch level, environment, object definition, topology,
  log excerpt, installed tool evidence, or unsupported compatibility claims.

## Later-Job Handoff

Later remediation jobs should treat this contract as the answer-generation layer only.
It can reduce omission and over-compression when the attachment context is already
source-backed, but it cannot replace item-level source remediation.

Use the following split:

- Content gaps: source-check the listed manuals, release notes, tool manuals, guides, or
  approved support files, then add answer-ready attachment blocks only when supported.
- Retrieval gaps: add headings, aliases, compact indexes, or cross-links so exact blocks
  are selected without flooding context.
- Answer synthesis gaps: preserve the contract's exact-token and domain-shape rules in
  attachment blocks and future calibration prompts.
- Calibration candidates: reserve for J019/J020 after source coverage and answer paths
  have been verified.

## Self-Review

- Source boundary preserved: the instruction draft still limits answers to attached
  curated knowledge and does not authorize outside manuals or generic Oracle behavior.
- Exact-token preservation strengthened: the draft now calls out code forms, numeric
  ranges, units, grammar nonterminals, view names, paths, properties, commands, APIs,
  classes, and version labels.
- Version handling strengthened: cross-version answers must label 7.1, 7.3, 8.1,
  patch-specific, or verified-source boundaries.
- Customer safety strengthened: protected topics now require preconditions, missing
  inputs, non-destructive first checks, and stop conditions before risky actions.
- Beginner/veteran usability strengthened: answers must explain prerequisites briefly
  while retaining expert-level exact details.
