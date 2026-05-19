# S4-J010 Package-Context Rerun Note

- Date: 2026-05-19
- Scope: package-specific answerability routing note for the assembled Stage 4 upload
  package
- Decision: no package-context live benchmark was started, and no live benchmark pass
  is claimed

## Current Limitation

The current full-benchmark runner is intentionally attachment-bound. The full
benchmark manifest sets `answer_generation.attachment_glob` to
`GPTs/attachments/*.md`, and `answer_runner.py` validates both that glob and the
`GPTs/attachments/` path boundary before constructing context.

Because of that boundary, the benchmark cannot target `GPTs/upload_package/` without a
scoped code or manifest-policy change. This note does not change benchmark questions,
expected answers, judge rules, or readiness thresholds.

## S4-J010 Dry-Run Evidence

The safest supported dry-run path was the existing lexical attachment-context runner:

```bash
python3 evals/altibase_answerability/scripts/answer_runner.py \
  --manifest evals/altibase_answerability/manifests/full_benchmark.json \
  --run-id s4_j010_full_lexical_dry_run_20260519 \
  --mode dry_run \
  --context-mode lexical \
  --validate-output \
  --output-dir /tmp/s4_j010_full_lexical_dry_run
```

Result: pass for dry-run mechanics; 270 answer records were written with `errors=0`.
The run validates projection, lexical context construction, answer-record schema, and
leakage checks. It does not validate live answer quality and does not prove package
context behavior.

## Package-Specific Live Routing

Before any future package-specific live run, record operator approval and the output
path, then use a scoped package-aware runner or documented harness that preserves:

- unchanged benchmark questions and expected answers;
- answer-input allowlisting and judge-only leakage protection;
- package context rooted only at `GPTs/upload_package/`;
- the existing readiness policy thresholds;
- durable outputs under `evals/altibase_answerability/reports/full_benchmark/runs/`
  or another approved path recorded before generation.

Until that package-aware route exists and is judged, the latest live comparison result
remains the previously recorded full-benchmark run, not a Stage 4 package-context
readiness claim.
