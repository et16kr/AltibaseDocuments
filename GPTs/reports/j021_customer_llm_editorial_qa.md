# J021 Customer LLM Editorial QA

- Job: `J021`
- Date: 2026-05-17
- Scope: `GPTs/attachments/*.md`, `GPTs/reports/`
- Boundary: editorial structure, customer answer usability, and unsafe-answer
  resistance only; no original manuals, benchmark thresholds, or expected questions
  changed

## Reconfirmed Requirement And Boundary

J021 reviews the updated attachment set as a customer-facing LLM corpus for first-time
Altibase users and veteran operators or developers. The review checks clarity, dense
exact-token reference value, source-boundary discipline, and protected-topic safety.

The pass remains documentation-scoped:

- Use repository-local selected sources and support reports only.
- Keep customer-facing attachment content in English.
- Do not add product facts unless the current selected sources already support them.
- Do not lower benchmark thresholds or rewrite benchmark expectations.
- Treat exact patch level, environment, object definition, log excerpt, topology,
  installed tool behavior, or unsupported compatibility claims as missing inputs.

## Design Note

This job changes documentation structure but not Altibase product behavior.

The upload attachments already had source-backed domain content from J004-J020 and the
J018 retrieval alias layer. J021 found one cross-file editorial inconsistency: several
upload files used `Core Guidance` or `Answering Rules` for the same customer-answer
policy block that most files call `Response Rules`. The headings are now normalized to
`Response Rules`, and `GPTs/attachments/README.md` now describes the current upload
structure and editorial QA checklist.

Fix classification:

| Fix | Classification | Rationale |
| --- | --- | --- |
| Normalize customer-answer policy headings to `Response Rules` | retrieval gap / answer synthesis gap | Makes the top-of-file answer guidance lexically consistent across all 20 upload files without changing product claims. |
| Refresh README attachment structure and QA checklist | answer synthesis gap | Documents the expected first-time and expert-user answer shape and protected-topic behavior for future edits. |

## Evidence Used

- `evals/altibase_answerability/reports/full_benchmark/failure_root_cause_analysis_20260517.md`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_095919/summary.txt`
- `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260517_095919/judge/aggregate_report.json`
- `evals/altibase_answerability/reports/targeted_calibration_j019_20260517.md`
- `GPTs/reports/customer_answer_contract.md`
- `GPTs/reports/coverage_matrix.md`
- `GPTs/reports/j020_residual_gap_remediation_design.md`

Evidence snapshot from the 2026-05-17 full benchmark:

| Metric | Value |
| --- | ---: |
| Passed / total | 27 / 270 |
| Critical fact coverage | 68.7% |
| Required token preservation | 74.6% |
| Unsupported-claim rate | 0.4% |
| Protected-topic blockers | 77 |

The dominant residual risk is not broad source absence. J019 found that 11 of 12
representative failures had all missed items in current lexical context, so the
editorial QA priority is answer-ready structure, literal-token preservation, and
guardrails against over-compression or unsafe action.

## Editorial Audit Results

| Area | Result | Notes |
| --- | --- | --- |
| Upload file boundary | Pass | Exactly 20 upload Markdown files under `GPTs/attachments/`, excluding `README.md`. |
| Required top-level routing sections | Pass after edit | Every upload file has `Applicable Versions`, `Questions This File Can Answer`, `Retrieval Alias Index`, `Source Documents`, `Response Rules`, `Attachment Cross-References`, and `Residual Scope`. |
| Source labels | Pass | Every upload file preserves `Altibase 8.1 verified source` wording for 8.1 coverage. |
| Customer-safe labels | Pass | No internal repository paths, local workstation paths, Windows drive paths, or original source-directory labels were found in upload attachments or GPT instructions. |
| English canonical content | Pass | No Korean, Chinese, Japanese, or other CJK prose was found in upload attachments. |
| Markdown fence integrity | Pass | Code fence counts are balanced in upload attachments. |
| Unsafe-answer resistance | Pass with residual benchmark risk | Attachments and GPT instructions require missing inputs and first checks for protected topics. The old benchmark still had protected-topic blockers, so J022 should plan post-upload or targeted rerun evidence. |

## Self-Review

- Source-backing: the changes are structural and do not add product behavior, syntax,
  defaults, ranges, or version claims.
- Exact tokens: headings and README guidance now reinforce literal preservation of SQL,
  property, view, error-code, command, path, option, API, class, numeric, unit, and
  version tokens.
- Customer clarity: the README now separates upload structure from the editorial QA
  checklist and removes stale "until final cleanup" wording.
- Beginner and veteran usability: the checklist explicitly requires both task purpose
  and expert-grade exact detail.
- Unsafe-answer resistance: protected-topic guidance remains aligned with
  `GPTs/GPT_Instructions_Draft.md` and the current attachment runbooks.

## Verification

Run during J021:

```bash
python3 - <<'PY'
from pathlib import Path
files = sorted(p for p in Path('GPTs/attachments').glob('*.md') if p.name != 'README.md')
required = [
    '## Applicable Versions',
    '## Questions This File Can Answer',
    '## Retrieval Alias Index',
    '## Source Documents',
    '## Response Rules',
    '## Attachment Cross-References',
    '## Residual Scope',
]
assert len(files) == 20
for path in files:
    text = path.read_text()
    missing = [section for section in required if section not in text]
    assert not missing, (path, missing)
    assert 'Altibase 8.1 verified source' in text, path
    assert text.count('```') % 2 == 0, path
PY
```

Additional required checks run during J021:

- `git diff --check`
- `bash review/scripts/run_review_stage.sh validate`
- `rg -n "^Verdict:|^\\| (Blocker|High|Medium|Low) \\|" review/reports/R*.md`

Result: pass. The review report scan returned only `Verdict: Pass` lines and no
actionable `Blocker`, `High`, `Medium`, or `Low` finding rows.

No full 270-question live benchmark was run in J021. This job made editorial structure
changes, not benchmark-question-specific content changes. Full live rerun planning is
owned by J022.
