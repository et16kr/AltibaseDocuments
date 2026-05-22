# Image Content Recovery — Job Specification (Draft)

- Date: 2026-05-22
- Repository: `/home/et16/AltibaseDocuments`
- Status: **Confirmed** (2026-05-22) — §9 decisions settled. Job runner:
  `GPTs/image_recovery/` (jobs IMG-01 … IMG-06).
- Related: `GPTs/reports/answerability_improvement_cycle3_plan_20260522.md`
  (separate effort; this job is **not** part of the answerability cycle).

## 1. Background

The source-preserving upload package (`GPTs/upload_package/`) ships only the
`.md` shards. The original manuals reference **7,142 images**
(`.gif` 5,124 / `.png` 2,213 / `.jpg` 592) via Markdown `![](media/...)` syntax.
That syntax survives into the shards as text, but **no image binary is shipped**
— every reference is a dead link. Any information that exists only inside a
diagram or an image-rendered table is invisible to the RAG/GPT system.

A spot inspection found the images fall into five classes of very different
value (see §4). Most are redundant with adjacent text; a minority carry unique,
currently-lost information. This job recovers that minority **as text**, so it
flows through the existing build into the shards.

Visio (`.vsd`) sources are **not available** and will not be sourced; the
rendered rasters are the working input (see §8).

## 2. Goals

- Recover, **as text**, the information carried only by diagram/table images.
- Insert the recovered text at the image's reference site, upstream in the
  build pipeline, so it survives a shard rebuild.
- Leave the package free of redundant or low-value conversions.

## 3. Non-goals

- Not shipping image binaries.
- Not converting redundant images (classes A/B in §4).
- Not a blanket conversion of all 7,142 references.
- Not modifying the answerability eval question sets (a follow-on; see §10).
- Not sourcing external `.vsd` files.

## 4. Image classification taxonomy

Every referenced image is classified **in its document context** — the class
cannot be decided from the image alone.

| Class | Description | Example | Action |
| --- | --- | --- | --- |
| A | Syntax diagram redundant with an adjacent text `Syntax` code block | `bigint1.png` followed by ```` ``` BIGINT ``` ```` | skip |
| B | Conceptual diagram redundant with surrounding prose | `su_policy_eng.png` (prose already states the policy) | skip |
| C | Railroad/syntax diagram that is the **only** source of the grammar | SQL Reference `alter_database ::=` (text has only the `::=` label) | convert → BNF/EBNF text block |
| D | Tabular data rendered as an image | `replicationCompatibility.png` (version-compat matrix) | convert → Markdown table |
| E | True process/decision flowchart with branching logic not in prose | (to be quantified in Phase 1) | convert → Mermaid `flowchart` |

Only **C / D / E** are converted. Phase 1 reports the count in each class.

## 5. Pipeline constraint

Build pipeline: `Manuals/` (original) → `GPTs/source_pack/` →
`GPTs/upload_package/` shards. Recovered text inserted **only into the final
shards is wiped by the next rebuild**. The recovered text must therefore be
injected **upstream**. Recommended approach (see §9 decision D1): keep the
original manuals unmodified and inject from a **conversion sidecar** during the
`source_pack` build, keyed by image reference. Original sources stay immutable;
the sidecar is the single reviewable artifact.

## 6. Phases

- **Phase 0 — Inventory.** Extract every `![](...)` reference across `Manuals/`
  (and other in-scope source trees) with: source file, image path, basename,
  enclosing heading/section, and the ±N lines of surrounding text. Output:
  `image_inventory.tsv`.
- **Phase 1 — Classification / audit.** Classify each reference into A–E using
  the surrounding text. Cheap deterministic rules first (e.g. "image
  immediately followed by a fenced `Syntax` block" → A); a sampled manual
  review validates the rules and the residual is classified with vision. Output:
  `image_classification.tsv` + an audit report quantifying each class and the
  recoverable-information estimate.
- **Phase 2 — Conversion.** For C/D/E only, produce the text rendition in the
  per-class format (§4). Batched/parallel over the filtered set. Each conversion
  is **cross-checked against the rendered raster**; raster too low-resolution
  for a reliable transcription is flagged, not guessed (PDF fallback, §8).
  Output: the conversion sidecar (`image_conversions.jsonl`, keyed by image
  reference).
- **Phase 3 — Pipeline integration.** Wire the sidecar into the `source_pack`
  build so each C/D/E reference site gains the recovered text; rebuild the
  shards. Output: updated build + rebuilt `upload_package/` shards.
- **Phase 4 — Validation & docs.** Spot-check converted sites in the rebuilt
  shards; confirm no regression to existing text; update the source-pack /
  upload-package docs. Output: validation report.
- **Phase 5 — Conversion comparison audit.** Independently compare each
  converted graph against its original image — classes D and E fully, class C
  on a stratified sample. Any `material` mismatch fails the run so a faithless
  conversion is caught, not shipped. Output: comparison audit ledger + report.

## 7. Deliverables

- `image_inventory.tsv` — every image reference with context.
- `image_classification.tsv` — class A–E per reference + rationale.
- `image_conversions.jsonl` — recovered text for every C/D/E reference.
- Updated `source_pack` build + rebuilt `upload_package/` shards.
- Audit report (class counts, recoverable-information estimate) and a
  validation report.
- `image_comparison_audit.tsv` + comparison audit report — the per-image
  image-vs-graph fidelity verdicts.

## 8. Inputs

- **Primary:** `Manuals/` markdown + the `media/` rendered rasters.
- **Fallback:** the manuals' `PDF/` folders — higher-resolution / vector
  renditions, used only for C/D/E images whose raster is too low-res for a
  reliable transcription.
- `.vsd` Visio sources: **not available, not used.**

## 9. Confirmed decisions (settled 2026-05-22)

- **D1 — Injection point: build-stage sidecar.** The `Manuals/` originals stay
  unmodified. Recovered text is injected from a conversion sidecar during the
  `source_pack` build (see §5).
- **D2 — Reference handling: keep the link, add text beside it.** At a converted
  C/D/E site the original `![]()` reference is kept and the recovered text is
  inserted next to it — consistent with the source-preserving package.
- **D3 — Scope of source trees: `Manuals/` only.** This job covers the
  `Manuals/` tree; `Technical Documents/`, `ReleaseNotes/`, `PatchNotes/` are a
  later pass.
- **D4 — Verification depth: full per-image cross-check for C, D, and E.**
  Every converted image is verified against its rendered raster (PDF fallback
  where the raster is too low-resolution).

## 10. Acceptance criteria

- Phase 1 classifies **100%** of inventory references into A–E.
- Every C/D/E reference has a conversion in the sidecar; each is verified
  against its raster (or PDF fallback) — none guessed from an unreadable image.
- Rebuilt shards: every C/D/E reference site carries the recovered text;
  existing text is byte-unchanged elsewhere (no regression).
- The audit report quantifies class counts and the recoverable-information
  estimate.
- The comparison audit (Phase 5) finds **zero `material` mismatches** — classes
  D and E compared fully, class C on a stratified sample — against the
  converted graphs.
- `git diff --check` clean.

## 11. Risks

- **Conversion hallucination** — AI transcription can invent diagram content;
  mitigated by mandatory raster cross-check and PDF fallback.
- **Classification false-negative** — a class-A/B call that is really C/D/E
  silently drops unique info; mitigated by sampled manual validation of the
  rules in Phase 1.
- **Rebuild wipe** — recovered text not injected upstream is lost; addressed by
  §5 / decision D1.
- **Low-resolution rasters** — small-text railroad diagrams may be unreadable;
  addressed by the PDF fallback.
- **Scale** — 7,142 references; mitigated because only the filtered C/D/E set
  is converted, and conversion is batched.

## 12. Follow-on (out of scope)

The current answerability eval will not move on this job alone — its 270
questions were authored against the text. To actually exercise recovered
diagram content, a later effort could add diagram-dependent eval questions
(e.g. precise SQL-statement-syntax questions). Noted, not included here.
