# Source Pack Baseline

Job: `S1-J004`
Status: repository and AID source-pack baseline

## Boundary

This directory records the deterministic Stage 1 source selection and exact
source-pack baseline. The manifest builder considers these repository source roots:

- `Manuals/`
- `ReleaseNotes/`
- `PatchNotes/`
- `Technical Documents/`
- `3rd Party Guide for Altibase/`

The manifest builder also materializes file-level AID upload-content candidates from
the approved AID tiering evidence. The AID corpus is a separate Git repository
checked out at `~/AID`; its repository, branch (`combine`), and pinned commit are
recorded in `GPTs/AID_DEPENDENCY.md`, which is required for a reproducible rebuild.
It does not treat every file under `GPTs/reports/`
as source. Reports are included only when the builder lists them as approved support
evidence with a concrete reason in `source_manifest.tsv`. Requirements, readiness
drafts, transient review notes, and generated validation logs remain outside the
source candidate universe unless a later job explicitly promotes them with an
evidence reason.

## Selection Rule

Supported Markdown sources under the repository source roots are selected with
`selection_decision=include_exact`. Altibase 6.x patch-note Markdown is excluded
because the active answer scope is Altibase 7.1, 7.3, and 8.1 unless a later
historical or migration job selects it. Binary/media/PDF sidecars and other
non-Markdown files are recorded in the exclusion register because Stage 1 exact
source-pack extraction is Markdown-first. Non-Markdown files that may contain useful
operational evidence, such as Tableau SQL sidecars, keep explicit exclusion notes so a
later text-sidecar or media pass can select them intentionally.

## Image-Recovery Sidecar

The original manuals reference thousands of diagram images that ship only as
dead `![](media/...)` links — any information carried only inside a diagram is
otherwise invisible to the RAG/GPT system. The image-content-recovery effort
recovers that information **as text**.

- **What is recovered.** Only diagram classes whose image is the *sole* source
  of the information: class **C** railroad/syntax diagrams (recovered as a
  `bnf` grammar block), class **D** tabular data rendered as an image
  (recovered as a Markdown table; none currently exist in `Manuals/`), and
  class **E** process/decision flowcharts (recovered as a `mermaid`
  flowchart). Redundant classes A and B are intentionally skipped.
- **Originals are unmodified.** The `Manuals/` source files stay byte-unchanged.
  Recovered text is injected only at build time from a conversion sidecar
  (decision D1) — it is not written back into the manuals.
- **How it is injected.** `build_source_pack.py` reads the sidecar
  `GPTs/image_recovery/image_conversions.jsonl` and, at each image reference
  that has a verified record, keeps the original `![]()` / `<img>` reference and
  inserts the recovered text immediately after it (decision D2), wrapped in
  `<!-- IMG_RECOVERY_BEGIN … -->` / `<!-- IMG_RECOVERY_END … -->` marker
  comments. References with no sidecar record are untouched. The sidecar is
  optional: with the file absent the build reproduces the byte-exact source
  pack.
- **Where it lives.** Sidecar and supporting artifacts (inventory,
  classification, conversions, comparison audit) are under
  `GPTs/image_recovery/`; the job specification and reports are under
  `GPTs/reports/` (`image_content_recovery_spec_20260522.md` and the audit /
  validation reports).

Stripping the `IMG_RECOVERY` blocks from a rebuilt shard reproduces the
pre-recovery shard byte-for-byte, so the recovery is additive only.

## Deterministic Command

Regenerate and validate the manifests from the repository root:

```bash
python3 GPTs/source_pack/scripts/build_source_manifest.py --write
```

Check that committed manifests match the deterministic builder output:

```bash
python3 GPTs/source_pack/scripts/build_source_manifest.py --check
```

Generate the exact source-pack shards and source-to-shard mapping:

```bash
python3 GPTs/source_pack/scripts/build_source_pack.py --write
```

Check that committed source-pack shards and mapping are current:

```bash
python3 GPTs/source_pack/scripts/build_source_pack.py --check
```

Validate the committed source pack, exact extracted source blocks, size/token gates,
and generated Stage 1 notes:

```bash
python3 GPTs/source_pack/scripts/validate_source_pack.py --check
```
