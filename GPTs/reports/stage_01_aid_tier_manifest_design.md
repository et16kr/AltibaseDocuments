# Stage 1 AID Tier Manifest Design Note

Job: `S1-J003`
Status: tier classification baseline
Created: 2026-05-18
Scope: AID tier manifest, AID evidence selection, and initial limitation register only

## Reconfirmed Requirement And Boundary

`S1-J003` classifies the adjacent AID corpus for Stage 1 use. The job does not
rewrite AID content, does not edit `GPTs/attachments/`, does not assemble the final
upload package, and does not run a blanket Korean-to-English rewrite.

No blanket Korean-to-English rewrite is scheduled for AID. AID evidence records Phase
1 semantic coverage as `COMPLETE`, Phase 2 source stabilization as
`READY_FOR_LLM_CONSOLIDATION`, and the LLM reference package as
`COMPLETE_REFERENCE_PACKAGE`.

## Design

`GPTs/reports/aid_tier_manifest.tsv` uses source-group rows for large AID trees and
evidence-file rows for the AID files that justify those decisions.

The manifest preserves these AID classification boundaries:

- stabilized `~/AID/arch/Home/` and Korean-source-verified `~/AID/FAQE/Home/` content
  are upload-content candidates after file-level source-pack selection;
- `~/AID/FAQE/Home/` English-only auxiliary content is an upload-content candidate
  only with explicit `English-only source` or `english_only_auxiliary` labels;
- source-backed `~/AID/llm-reference/` topic and GPTs upload bundle files are
  upload-content candidates, but still count against the global 20 Markdown upload
  file limit only if copied or transformed into `GPTs/upload_package/`;
- Korean source trees, manifests, coverage matrices, stabilization evidence, and
  review reports are evidence-only authority by default;
- source limitations, legacy attachment labels without downloadable URLs, unavailable
  diagrams, non-document-format artifacts, and accepted English-only auxiliary
  limitations remain limitations and must not be expanded into invented facts.

`GPTs/source_pack/source_manifest.tsv` is updated only with AID support-evidence rows
in this job. Exact file-level `include_exact` rows for `~/AID/arch/Home/`,
`~/AID/FAQE/Home/`, and selected `~/AID/llm-reference/` upload-content candidates are
deferred to a later source-pack extraction job because the Stage 1 exact extraction
contract requires one selected source file per row, stable checksums, and deterministic
shard placement.

## Validation Contract

The targeted validator for this job checks that:

- every AID tier row uses a known tier and has evidence;
- every upload-content candidate has classification evidence or is blocked as
  conflict/recheck;
- every source ID referenced by the tier manifest exists in the source manifest;
- conflict or recheck rows have a conflict-register ID;
- the design note records that no blanket AID Korean-to-English rewrite is scheduled.
