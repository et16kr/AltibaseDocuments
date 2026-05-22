# Image Content Recovery — Conversion Comparison Audit (Phase 5 / IMG-06)

- Date: 2026-05-22
- Repository: `/home/et16/AltibaseDocuments`
- Spec: `GPTs/reports/image_content_recovery_spec_20260522.md` — Phase 5
- Ledger: `GPTs/image_recovery/image_comparison_audit.tsv`
- Verdict: **PASS** — zero `material` mismatches, zero `uncertain` cases.

## 1. Scope and method

This is the independent conversion-fidelity check: each converted graph is
compared, by visual inspection of the original raster, against its
`converted_text` in `image_conversions.jsonl` (joined to `image_classification.tsv`
and `image_inventory.tsv` by `ref_id`).

- Class **D** (tables): there are **0** class-D images in the corpus — the
  classifier produced no D rows, so D coverage is vacuously 100%.
- Class **E** (flowcharts): **100%** — all 58 conversions audited.
- Class **C** (syntax/railroad diagrams): stratified sample of **930 / 3,405**
  conversions (**27.3%**, ≥ 25% and ≥ 40), spread across all three manual sets.
- Class **A/B** (classified redundant, never converted): stratified sample of
  **511 / 3,948** references (**12.9%**, ≥ 10% and ≥ 30) — confirming each is
  genuinely redundant and not a misclassified C/D/E.
- Every IMG-03 record is `verified:true` (0 `verified:false`), so no extra
  forced-audit set applies.

Rasters were read directly with the image tool (`.gif` / `.png` / `.jpg`); no
raster was unreadable, so no PDF fallback was needed and no case is `uncertain`.

### Re-run note

This is a **re-run** of IMG-06. The prior IMG-06 ledger recorded 36 `material`
findings; the recovery cycle then re-ran IMG-03 → IMG-05. This run independently
re-audited every one of those 36 references against the current sidecar by
opening the source rasters:

- **M5 / M6 — `create_table_lob.gif` (eng + kor), 6 refs.** Genuine prior
  defect: the image is a YES/NO decision tree wrongly classified **B** and never
  converted. The IMG-03 re-run reclassified it **E** and added a Mermaid
  conversion. Re-audit of the new conversion against the raster: faithful →
  `match`.
- **M1–M4 — `ddl_clause`, `close_database_link`, `aexport`, the data-type
  conversion-path graph, 30 refs.** Genuine prior defects. The recovery cycle
  corrected all 30 sidecar records before this re-run: M1 reversed the
  `<0+E+L>` edge to `DOUBLE → REAL` (the narrowing conversion); M2 changed
  `DDL [ by_clause ]` to `DDL by_clause { by_clause }` (the diagram's
  repetition loop); M3 removed the spurious `|` so `ALTER SESSION CLOSE
  DATABASE LINK …` reads as the one wrapped sequence it is; M4 changed the
  option-group wrapper from `[ … ]` to `{ … }` (the diagram's repetition
  loop). Re-audit of the corrected conversions against the rasters: faithful
  → `match`.

The other 1,463 ledger rows cover sidecar records not affected by the
recovery-cycle corrections; their verdicts were spot-validated this run (14
class-C and 8 class-A/B independent re-checks, all confirming) and retained.

## 2. Per-verdict counts

| Verdict | Count |
| --- | --- |
| `match` | 1,449 |
| `minor` | 50 |
| `material` | 0 |
| `uncertain` | 0 |
| **Total audited** | **1,499** |

## 3. Audit coverage per class

| Class | In corpus | Audited | Coverage | Requirement | Met |
| --- | --- | --- | --- | --- | --- |
| D (tables) | 0 | 0 | 100% (vacuous) | 100% | yes |
| E (flowcharts) | 58 | 58 | 100% | 100% | yes |
| C (syntax diagrams) | 3,405 | 930 | 27.3% | >= 25% and >= 40 | yes |
| A/B (redundant) | 3,948 | 511 | 12.9% | >= 10% and >= 30 | yes |

Manual spread of the audited sample:

| Class | Altibase_7.1 | Altibase_7.3 | Altibase_trunk | Tools |
| --- | --- | --- | --- | --- |
| E | 18 | 18 | 18 | 4 |
| C | 284 | 325 | 321 | 0 |
| A | 61 | 61 | 63 | 0 |
| B | 175 | 62 | 59 | 30 |

All audited C conversions span the three manual versions; A/B spans the manual
versions plus the Tools manuals.

## 4. Material mismatches

**None.** Zero `material` verdicts.

The prior run's 36 `material` findings were all resolved (see the re-run note in
§1): 6 by the IMG-03 reclassification + conversion of `create_table_lob.gif`,
and 30 by correcting the four faulty C/E conversions in the sidecar
(`data_type_conversion_path_kor.gif`, `audit_ddl_clause.gif`,
`alter_session.gif`, the aexport diagram) so they now match their rasters.

## 5. Uncertain cases

**None.** Every audited raster was readable; no PDF fallback was required.

## 6. Minor differences (logged, non-failing)

50 `minor` verdicts, all class C — cosmetic or notation nuances with no grammar
element lost. They fall into five recurring patterns:

- `column_definition` (12) — trailing list written `[ {',' column_constraint} ]`
  vs the diagram idiom `column_constraint {',' column_constraint}`;
  separator-placement only.
- `call_spec` (10) — `NAME func_name` / `LIBRARY lib_name` linearised to a fixed
  sequence where the diagram stacks them; no token lost.
- `execute_procedure_statement` (8) — qualifier brackets nested
  `[ user_name '.' [ package_name '.' ] ]` vs two independent optionals;
  bracket-scope imprecision.
- `parameter_notation` (7) — comma-repetition factored out to the call sites
  rather than redrawn per image.
- `Point_clause` (6) and `altimon` (7) — metavariable legend lines not
  transcribed / `{}` vs optional-marker imprecision.

These are logged for awareness only and do not affect the verdict.

## 7. Result

D and E audited 100% (D vacuous, E 58/58); the class-C sample is 27.3%
(>= 25%, >= 40) spread across all manual sets; the class-A/B sample is 12.9%
(>= 10%, >= 30). The audit finds **zero `material` mismatches** and **zero
`uncertain` cases**.

**PASS.**
