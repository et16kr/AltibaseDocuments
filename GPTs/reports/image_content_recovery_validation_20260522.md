# Image Content Recovery — Phase 4 Validation (IMG-05)

- Date: 2026-05-22
- Job: IMG-05 — validation and documentation
- Spec: `GPTs/reports/image_content_recovery_spec_20260522.md` (Phase 4)
- Inputs validated: the IMG-04 rebuild of `GPTs/source_pack/` and
  `GPTs/upload_package/` shards, the build-stage sidecar
  `GPTs/image_recovery/image_conversions.jsonl`, the build script
  `GPTs/source_pack/scripts/build_source_pack.py`, and
  `GPTs/image_recovery/image_classification.tsv`.

## 1. Verdict

**PASS** for Phase 4 scope (package integrity, no-regression, documentation).

The rebuilt package injects exactly the **3,463** verified class-C/D/E image
conversions into the shards as text. Every converted site keeps its original
`![]()` / `<img>` reference and carries recovered text byte-identical to the
sidecar, and stripping the injected blocks reproduces the pre-IMG-04 shards
byte-for-byte — no non-C/D/E reference site and no non-image content changed.
The two package READMEs now document the sidecar mechanism.

One **outstanding item is recorded, not resolved** here: the Phase 5 fidelity
audit (IMG-06) is in a FAIL state with four uncorrected `material`
image-vs-conversion mismatches still present in the shipped sidecar. Phase 4
validates package integrity and no-regression; it does **not** re-judge
transcription fidelity. See §6 and §9.

## 2. Scope and baseline

IMG-04 committed nothing, so the regression baseline is the current `HEAD`
(`5725c839`). The working-tree changes under validation are:

- `GPTs/source_pack/scripts/build_source_pack.py` — IMG-04's intentional
  sidecar wiring (decisions D1/D2).
- 8 source-pack shards (`source_pack_shard_{001,006,010,012,013,014,015,016}.md`).
- 8 upload-package shards (the same eight indices).
- 2 generated shard-manifest files (`source_to_shard_manifest.tsv` and
  `upload_package/03_source_to_shard_manifest.md`).

`Manuals/` is byte-unchanged (`git diff --name-only -- Manuals/` is empty).

## 3. Spot-check of converted sites

A representative sample of C and E references was opened in the rebuilt
`GPTs/upload_package/` shards, spanning every affected manual family and all 8
modified shards. For each, the converted site was confirmed to carry **both**
the original `![]()` / `<img>` reference **and** the recovered text, and the
recovered text was confirmed byte-identical to the matching
`image_conversions.jsonl` record.

| ref_id | Class | Manual / shard | Site check |
| --- | --- | --- | --- |
| img-00088 | E | Administrator's Manual / shard 001 | link kept; `mermaid` decision flowchart; matches sidecar |
| img-00181 | C | DB Link User's Manual / shard 006 | link kept; `bnf` `create_dblink` grammar; matches sidecar |
| img-00332 | E | Log Analyzer User's Manual / shard 010 | link kept; `mermaid` API-usage step flow; matches sidecar |
| img-00358 | E | Performance Tuning Guide / shard 012 | link kept; `mermaid` query-processing flow; matches sidecar |
| img-00460 | E | Replication Manual / shard 012 | link kept; `mermaid` replication flow; matches sidecar |
| img-00565 | C | SQL Reference / shard 013 | link kept; `bnf` `alter_database ::=`; matches sidecar |
| img-00744 | E | SQL Reference / shard 013 | link kept; `mermaid` `create_table_lob.gif` LOB/partition tablespace precedence flowchart; matches sidecar |
| img-00925 | C | Spatial SQL Reference / shard 013 | link kept; `bnf` spatial-clause grammar; matches sidecar |
| img-00197 | C | External Procedures Manual / shard 014 | link kept; `bnf` external-procedure grammar; matches sidecar |
| img-00989 | C | Stored Procedures Manual / shard 014 | link kept; `bnf` PSM grammar; matches sidecar |
| img-01074 | C | Utilities Manual / shard 015 | link kept (absolute typo path); `bnf` `aexport ::=` command syntax; matches sidecar |
| img-03453 | C | StoredProcedure1_Eng / shard 015 | link kept; `bnf` PSM grammar; matches sidecar |
| img-07061 | E | Altibase Heartbeat User's Guide / shard 016 | link kept; `mermaid` heartbeat-transition flow; matches sidecar |

At each site the recovered text is inserted immediately after the original
reference line, wrapped in
`<!-- IMG_RECOVERY_BEGIN ref_id="…" source_md="…" line_no="…" image_path_raw="…" image_class="…" format="…" verified="…" -->`
/ `<!-- IMG_RECOVERY_END ref_id="…" -->` markers (spec decision D2).

### Exhaustive block check

Beyond the sampled sites, **every** injected block in both packages was checked
programmatically: 3,463 blocks in the 8 source-pack shards and 3,463 in the 8
upload-package shards (6,926 total). For all 6,926:

- the marker `ref_id` resolves to a sidecar record;
- the marker `image_class` and `format` match the sidecar record;
- the block body byte-equals the sidecar `converted_text`;
- the line immediately preceding the block is the original image reference and
  contains the record's `image_path_raw`;
- the BEGIN and END `ref_id` agree;
- the `ref_id` is classified C/D/E in `image_classification.tsv`.

**0 discrepancies.** All 3,463 distinct C/D/E references are present in both
packages, and the 8 non-converted shards in each package contain no injected
block.

## 4. Regression check

For each of the 16 changed shards the working-tree file had its injected blocks
deleted — each block is the inserted run
`\n\n<!-- IMG_RECOVERY_BEGIN … -->\n…\n<!-- IMG_RECOVERY_END … -->\n` — and the
result was compared byte-for-byte to the file's `HEAD` blob.

| Shard | source_pack stripped == HEAD | upload_package stripped == HEAD | blocks |
| --- | --- | --- | ---: |
| 001 | yes | yes | 12 |
| 006 | yes | yes | 24 |
| 010 | yes | yes | 6 |
| 012 | yes | yes | 32 |
| 013 | yes | yes | 920 |
| 014 | yes | yes | 1,841 |
| 015 | yes | yes | 567 |
| 016 | yes | yes | 61 |
| **Total** | **byte-identical** | **byte-identical** | **3,463** |

Stripping the injected blocks reproduces the pre-IMG-04 shards **byte-for-byte**
in all 16 files. Therefore every changed hunk in the shards sits at a C/D/E
reference site that gained recovered text; no non-C/D/E reference site and no
non-image content changed. The other 8 shards in each package are untouched.

### Generated manifests

The two shard-manifest files also changed — expected generated bookkeeping, not
content change. Of the **941** manifest rows, **346** changed:

- **67 rows** — exactly the 67 source files that received conversions — show an
  updated `extracted_body_sha256`, `block_byte_count`, `block_line_count`,
  `block_estimated_tokens`, and a `notes` value stating the body was copied
  with N image-recovery sidecar conversion(s) inserted.
- **279 rows** changed **only** `shard_estimated_tokens` — non-injected sources
  that share one of the 8 affected shards, whose shard-level token total
  shifted because of the injected text.
- `source_sha256` is unchanged for **all 941** rows; `validation_status` stays
  `pass` for every row. No source's identity changed.

`git diff --check` is clean.

## 5. Recovered references by class

3,463 references converted — every class-C/D/E reference in the inventory, one
sidecar record each, all `verified: true`, all transcribed from the rendered
raster (`source_used: raster`; no PDF fallback was needed).

| Class | Format | References | Notes |
| --- | --- | ---: | --- |
| C — railroad/syntax diagram, only source of the grammar | `bnf` | 3,405 | the formal grammar of Altibase SQL, PSM, external procedures, utility commands, and SQL hints |
| D — tabular data rendered as an image | (Markdown table) | 0 | none exist in the `Manuals/` tree (Altibase renders tables as Markdown text) |
| E — process/decision flowchart | `mermaid` | 58 | 15 distinct flowcharts, including the `create_table_lob.gif` LOB/partition tablespace precedence flowchart re-classified from B to E after the Phase 5 audit |
| **Total** | | **3,463** | dedup: 609 unique `converted_text` strings (594 C + 15 E) transcribed once and reused across language/version copies |

By manual:

| Manual | C | E | Total |
| --- | ---: | ---: | ---: |
| SQL Reference | 2,582 | 6 | 2,588 |
| Stored Procedures Manual | 407 | 0 | 407 |
| External Procedures Manual | 120 | 0 | 120 |
| Utilities Manual | 114 | 0 | 114 |
| StoredProcedure1_Eng | 90 | 0 | 90 |
| Spatial SQL Reference | 66 | 0 | 66 |
| DB Link User's Manual | 24 | 0 | 24 |
| Performance Tuning Guide | 0 | 18 | 18 |
| Replication Manual | 0 | 12 | 12 |
| Administrator's Manual | 0 | 12 | 12 |
| Log Analyzer User's Manual | 0 | 6 | 6 |
| Altibase Heartbeat User's Guide | 0 | 4 | 4 |
| Sharding (deprecated) | 2 | 0 | 2 |
| **Total** | **3,405** | **58** | **3,463** |

Counts span 67 source markdown files (the same diagrams shipped per
language/version) across the 7.1, 7.3, and trunk manual trees.

## 6. Residual flagged conversions

**No residual flagged (unverified) conversions.** IMG-03 reported 0 flagged
(`verified: false`) conversions, and this job re-confirmed it: all 3,463 sidecar
records have `verified: true`. No unreadable raster was carried over
unconverted; no PDF fallback was needed.

8 records carry an explanatory `notes` value documenting a path-resolution
correction — all still `verified: true`:

- 1 record (`img-00809`) — source markdown image path
  `media/SQL_multiple_delete.png` is a typo; verified against the actual raster
  `media/SQL/multiple_delete.png`.
- 7 records — reference raster absent from its own (trunk) manual tree; verified
  against the byte-identical sibling copy of the same image in the 7.1/7.3 tree.

These are resolved, verified conversions, not residual flags.

### Outstanding Phase 5 fidelity finding (carried, not a Phase 4 flag)

This is **not** an IMG-03 `verified: false` flag, but it must be recorded. The
Phase 5 conversion comparison audit (IMG-06,
`GPTs/reports/image_content_recovery_comparison_audit_20260522.md`) last ran
with verdict **FAIL** — 36 reference rows across 6 conversions judged `material`
mismatch:

- **M5 / M6 — resolved.** `create_table_lob.gif` (eng + kor) was a YES/NO
  decision flowchart misclassified B and never converted. It has since been
  re-classified **E**; the IMG-03 re-run added the 6 missing E records
  (`img-00744 / 01882 / 03060 / 04257 / 05391 / 06591`), which is why the
  sidecar grew from 3,457 to **3,463** records and shards 013/014 each gained
  the new blocks. These 6 are validated above (§3, `img-00744` sampled).
- **M1–M4 — still outstanding.** Four C/E conversions still carry the
  `material` mismatch IMG-06 reported (M1 `data_type_conversion_path_kor.gif`
  reversed edge; M2 `ddl_clause` missing repetition loop; M3
  `close_database_link` spurious alternation; M4 `aexport` missing repetition
  loop). They have **not** been corrected in `image_conversions.jsonl`, so the
  rebuilt shards inject those four faithless transcriptions. IMG-06 has not been
  re-run to confirm. Correcting M1–M4 and re-running IMG-03 → IMG-06 is a
  required follow-on, tracked under Phase 5 — out of scope for Phase 4.

50 further `minor` IMG-06 verdicts (notation/decomposition imprecision, all
tokens present) do not fail the audit and are logged only.

## 7. Documentation updates

- `GPTs/source_pack/README.md` — added an **Image-Recovery Sidecar** section:
  which classes are recovered (C → `bnf`, D → Markdown table, E → `mermaid`),
  that the `Manuals/` originals stay byte-unchanged and the recovered text is
  injected only at build time from
  `GPTs/image_recovery/image_conversions.jsonl`, the `IMG_RECOVERY_BEGIN/END`
  marker convention, and pointers to the spec and the `GPTs/image_recovery/`
  artifacts.
- `GPTs/upload_package/00_README_SOURCE_PRESERVING_UPLOAD.md` — added a
  **Recovered Image Content** section describing the marked recovered-text
  blocks in the shards, the recovered classes, that originals are unmodified,
  and where the sidecar and spec live.

## 8. Acceptance checks

| Check | Result |
| --- | --- |
| `test -f GPTs/reports/image_content_recovery_validation_20260522.md` | PASS (this file) |
| `git diff --name-only -- Manuals/` empty | PASS — Manuals untouched |
| `git diff --check` | PASS — clean |
| Spot-checks: converted sites carry link + recovered text | PASS — 13-ref sample + 6,926-block exhaustive check, 0 discrepancies |
| Regression: no unintended change | PASS — stripping injected blocks reproduces `HEAD` byte-for-byte in all 16 shards |
| Both READMEs updated | PASS |

## 9. Limitations and follow-ons

- **Phase 5 fidelity FAIL is open.** Four `material` mismatches (M1–M4, §6) are
  still in the shipped sidecar; IMG-06 must be re-run after they are corrected.
  Phase 4 deliberately does not re-judge transcription fidelity — it validates
  that whatever the sidecar holds is injected losslessly and without
  regression, which it is.
- **Validators not yet re-baselined.** `validate_source_pack.py` and
  `validate_source_preserving_upload_package.py` enforce the pre-recovery
  invariant "extracted body == original source bytes", which decision D2
  deliberately changes; they now FAIL and need re-baselining. Recorded by
  IMG-04; out of scope here. `build_source_pack.py --check` itself already
  accounts for the sidecar and passes.
- **Answerability harness re-baseline pending.** Rebuilding
  `GPTs/upload_package/` changed the corpus the answerability harness runs
  against. Re-baselining that harness is a separate, still-pending follow-on
  (flagged by IMG-04).
- **Class-D HTML-table refinement** (spec §12) — not exercised: 0 class-D
  references exist in the `Manuals/` tree.
