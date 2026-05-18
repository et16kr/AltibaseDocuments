# Source Pack Baseline

Job: `S1-J002`
Status: repository source manifest baseline

## Boundary

This directory records the deterministic Stage 1 repository-local source selection
baseline. The manifest builder considers these repository source roots:

- `Manuals/`
- `ReleaseNotes/`
- `PatchNotes/`
- `Technical Documents/`
- `3rd Party Guide for Altibase/`

The builder does not treat every file under `GPTs/reports/` as source. Reports are
included only when the builder lists them as approved support evidence with a concrete
reason in `source_manifest.tsv`. Requirements, readiness drafts, transient review
notes, and generated validation logs remain outside the source candidate universe
unless a later job explicitly promotes them with an evidence reason.

## Selection Rule

Supported Markdown sources under the repository source roots are selected with
`selection_decision=include_exact`. Altibase 6.x patch-note Markdown is excluded
because the active answer scope is Altibase 7.1, 7.3, and 8.1 unless a later
historical or migration job selects it. Binary/media/PDF sidecars and other
non-Markdown files are recorded in the exclusion register because Stage 1 exact
source-pack extraction is Markdown-first. Non-Markdown files that may contain useful
operational evidence, such as Tableau SQL sidecars, keep explicit exclusion notes so a
later text-sidecar or media pass can select them intentionally.

## Deterministic Command

Regenerate and validate the manifests from the repository root:

```bash
python3 GPTs/source_pack/scripts/build_source_manifest.py --write
```

Check that committed manifests match the deterministic builder output:

```bash
python3 GPTs/source_pack/scripts/build_source_manifest.py --check
```
