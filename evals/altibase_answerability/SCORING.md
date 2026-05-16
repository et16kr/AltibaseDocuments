# Scoring Policy

This benchmark measures whether `GPTs/attachments/` can support source-backed Altibase
answers after the attachment rebuild workflow finishes.

## Unit Of Evaluation

Each question produces:

1. an answer record generated from attachments-only context;
2. a judgment comparing that answer against judge-only expected facts and constraints;
3. aggregate metrics across the manifest.

The judge must use canonical-English expected facts even when source facts came from
Korean manuals. The answering model should answer in English unless the manifest
explicitly requests a multilingual test.

## Required Scores

Judgments must include these normalized scores from `0.0` to `1.0`:

| Score | Meaning |
| --- | --- |
| `fact_coverage` | Fraction of required expected facts covered with source-compatible meaning. |
| `critical_fact_coverage` | Fraction of expected facts marked `critical` that are covered. |
| `required_token_preservation` | Fraction of required technical tokens preserved literally. |
| `version_handling` | Correctness of version scope, patch-level caveats, and assumptions. |
| `altibase_specific_correctness` | Whether the answer uses Altibase-specific facts instead of generic database assumptions. |
| `unsupported_claim_control` | Whether the answer avoids prohibited or unsupported claims. |
| `missing_input_handling` | Whether the answer asks for environment, log, object, or patch details only when required. |
| `overall` | Final per-question score after applying blockers and penalties. |

Per-question pass/fail is determined by the judge implementation, but an answer with a
blocker finding must not pass.

## Severity Model

| Severity | Meaning |
| --- | --- |
| `blocker` | Upload readiness is blocked for this behavior. The answer is unsafe, misleading, or materially incomplete for a high-risk area. |
| `high` | A customer could receive wrong Altibase guidance, unsafe SQL, wrong version behavior, or damaging operational advice. |
| `medium` | The answer is partially useful but misses meaningful source-backed facts or important caveats. |
| `low` | Minor omission, wording, or structure issue that does not change core correctness. |
| `none` | No finding. |

## Readiness Decision

The final aggregate report must choose one readiness decision:

- `ready_for_upload`: thresholds are met and there are no blocker findings in protected
  topics.
- `targeted_remediation`: most thresholds are met, but one or more domains, subdomains,
  or question classes need scoped attachment remediation.
- `blocking_gaps`: upload should not proceed because thresholds or protected-topic gates
  failed.
- `invalid_run`: the run cannot be used because validation, leakage checks, manifests,
  schemas, or required outputs are incomplete.

## Initial Thresholds

| Metric | Threshold |
| --- | ---: |
| Overall pass rate | `0.85` |
| Minimum domain pass rate | `0.80` |
| Critical fact coverage | `0.90` |
| Required token preservation | `0.95` |
| Unsupported-claim rate | `0.02` maximum |

Protected topics must have zero blocker findings:

- backup and recovery;
- destructive SQL or destructive administrative operations;
- security and TLS;
- replication state changes;
- version-sensitive property changes.

## Aggregation Dimensions

Reports must aggregate by:

- domain;
- subdomain;
- user level;
- version scope;
- answer type;
- retrieval risk.

Reports should also list the highest-impact missed facts and prohibited-claim hits so
attachment remediation can be scoped to concrete files.
