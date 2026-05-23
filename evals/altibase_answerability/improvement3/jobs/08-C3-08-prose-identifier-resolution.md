# Job 08 — C3-08 Prose-named identifier resolution

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Master plan: `GPTs/reports/answerability_improvement_cycle3_plan_20260522.md` —
  item C3-08.
- Evidence: `evals/altibase_answerability/reports/full_rerun_analysis_cycle2_20260520.md`
  section **6** and the cycle-2 deep-dive reports. The C2-06/07 (and the job 06
  / job 07) identifier-anchored named-definition admission only fires when the
  question text contains the **identifier** the builders anchor on (a property
  name, an `ERR-xxxxx` code, a `V$`/`SYS_*` view name). Many residuals name the
  property/error/view in **prose** instead — e.g. PROP-123,
  ERR-117/119/120/123/130, VPM-101/103/104/106/107/108 describe the object by
  its function or message rather than by its identifier, so the named-definition
  section never fires.

## Task

Add a prose→identifier resolution step so the named-definition admission can
still fire when the question names the object descriptively.

1. **Diagnose.** For the residual questions listed above (and any equivalent
   ones job 06 / job 07 hand to C3-08), confirm via the retrieval-audit sidecar
   that the question does not contain the literal identifier the named-definition
   builder anchors on, and identify how the question *does* refer to the object
   (a paraphrased property purpose, an error message string, a view's described
   role).
2. **Build a deterministic prose→identifier resolver** in `answer_runner.py`:
   before the named-definition admission runs, map descriptive references in the
   question text to the canonical identifier(s) — property name, error code,
   view name — using only the in-package manifests and source material (e.g. an
   error-message string maps to its `ERR-xxxxx` code; a described property maps
   to its `*_PROPERTY` name). The resolver must be deterministic, conservative,
   and high-precision: when the prose is ambiguous, resolve nothing rather than
   admit the wrong block.
3. **Feed the resolved identifiers into the named-definition admission** so the
   right definition block is admitted even when the question only named the
   object in prose.
4. **No-op where nothing resolves.** For any question where no prose identifier
   is confidently resolvable, the assembled context must be byte-identical to
   before this job. Verify that explicitly.
5. **Do not regress** the cycle-2 gains or jobs 06–07. Use only the question
   text and in-package manifests/source — never judge-only question fields
   (`expected_facts`, `required_tokens`, `source_refs`, `prohibited_claims`).
6. Preserve determinism, `max_context_chars`, leakage checks, `--self-test`, and
   all retrieval-audit fields.

## Constraints (non-negotiable)

- You MAY modify `evals/altibase_answerability/scripts/answer_runner.py`.
- Do NOT touch `GPTs/upload_package/` source bodies. Do NOT modify question
  records.
- Do not run `run-all.sh` or other jobs' files.

## Acceptance checks

```bash
python3 evals/altibase_answerability/scripts/answer_runner.py --self-test
MODE=dry_run LIMIT=20 RUN_ID=c3_08_prose RUN_ROOT=/tmp/altibase-c3-08 \
  ./run-test.sh source-preserving
test -s /tmp/altibase-c3-08/answers/retrieval_audit.jsonl
git diff --check
```

For PASS: required-token-in-context for the named prose-residual questions
(PROP-123, ERR-117/119/120/123/130, VPM-101/103/104/106/107/108 and any handed
over by jobs 06–07), reconstructed the same way **immediately before and after
this job** (i.e. measure job 08's own delta, on the post-job-07 state — do not
credit gains that jobs 06–07 already produced), must **increase**, and the
resolver must newly anchor **at least some** of the listed questions. Questions
where no prose identifier resolves must keep byte-identical assembled context.
Record which questions the resolver newly anchored, and document any prose
reference that was deliberately left unresolved because it was too ambiguous. If
the resolver cannot safely anchor any listed question, that is a stop signal —
FAIL and record why (the plan's prose-residual premise needs review).

## Completion protocol

As your final action:

- Ensure `evals/altibase_answerability/improvement3/state/` exists.
- If every acceptance check passed AND the prose-residual questions improved
  with no regression elsewhere, write
  `evals/altibase_answerability/improvement3/state/08.result` with first line
  `PASS` and a short summary (which questions were newly anchored, before/after
  token-in-context).
- Otherwise write the same file with first line `FAIL: <one-line reason>`.
