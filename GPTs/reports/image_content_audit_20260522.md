# Image Content Audit — Phase 1 (IMG-02)

- Date: 2026-05-22
- Job: IMG-02 — image classification and audit
- Spec: `GPTs/reports/image_content_recovery_spec_20260522.md` (Phase 1, §4)
- Input: `GPTs/image_recovery/image_inventory.tsv` (7,411 references, from IMG-01)
- Output: `GPTs/image_recovery/image_classification.tsv` (7,411 rows + header)

## 1. Result summary

Every one of the 7,411 inventoried image references in the `Manuals/` tree was
classified into exactly one class A–E (spec §4).

| Class | Refs | Distinct basenames | Distinct file copies | Action | Convert? |
| --- | ---: | ---: | ---: | --- | --- |
| A — syntax diagram redundant with adjacent text `Syntax` block | 185 | 37 | 136 | skip | no |
| B — conceptual diagram / screenshot redundant with prose | 3,769 | 500 | 2,959 | skip | no |
| C — railroad/syntax diagram, **only** source of the grammar | 3,405 | 598 | 3,161 | convert → BNF/EBNF | **yes** |
| D — tabular data rendered as an image | 0 | 0 | 0 | convert → Markdown table | — |
| E — process/decision flowchart | 52 | 13 | 52 | convert → Mermaid `flowchart` | **yes** |
| **Total** | **7,411** | | | | |

**Convertible (C + D + E): 3,457 references** — this is **not** negligible; see
the stop/go assessment in §6.

`distinct file copies` counts unique `image_path_resolved` values; the same
diagram is shipped once per manual/language/version, so the count of *distinct
diagrams* is closer to the `distinct basenames` column (e.g. the 52 class-E
references are only ~11 distinct flowcharts).

## 2. Method

Classification followed the spec's three-stage approach. The classifier is
`GPTs/image_recovery/classify_images.py`; it writes resumably (rows already in
the output TSV are kept, so an interrupted run resumes rather than restarts).

### 2.1 Rule pass

Deterministic rules over the inventory `context` column, in priority order.
Counts are `decided_by` tallies from the output TSV:

| Rule | Class | Refs | Decides on |
| --- | --- | ---: | --- |
| `rule-cover` | B | 200 | image path under `media/common/` (cover-page logo) |
| `rule-table-cell` | B | 1,412 | image sits inside a Markdown table cell (legend symbol / UI icon) |
| `vision` | E | 52 | curated vision-verified flowchart set (see §2.2) |
| `rule-hint` | C | 450 | heading chain contains `Hint List` / `힌트 목록` |
| `rule-syntax-textblock` | A | 185 | image immediately followed by a `Syntax`/`구문` heading + fenced code block |
| `rule-railroad-bnf` | C | 2,289 | image preceded by a `<symbol> ::=` BNF label |
| `rule-railroad-synhead` | C | 568 | image is the first element under a `Syntax`/`구문` heading |
| `rule-railroad-synsection` | C | 98 | reference's leaf heading is `Syntax` / `구문` |
| `rule-residual-conceptual` | B | 2,157 | residual — conceptual diagram / screenshot / illustration |

### 2.2 Sampled validation

~95 distinct rasters were opened with the image-reading tool to confirm the
rules and to hunt for D and E. Findings that changed the rules:

- **Hint images are class C, not B.** `media/SQL/full scan.gif`, `append.gif`,
  `8aeb39dd…png` (DELAY) etc. are railroad diagrams (`FULL → SCAN → ( →
  tbl_name → )`); the hint prose never gives the grammar. Added `rule-hint`.
- **A "bare fenced block after the image" is not class A.** An early rule
  guessed A when a ``` ``` ``` ```` block followed the image; the sample showed
  these are screenshots/illustrations next to *code examples* (e.g. Spatial SQL
  geometry plots), not syntax. Rule dropped; those rows fall to the residual.
- **`::=` labels also appear as `:: =` and as bold `**label**` with no `::=`.**
  The BNF rule normalises whitespace; the `Syntax`-section rules
  (`rule-railroad-synhead`, `rule-railroad-synsection`) catch the bold-label
  railroad diagrams (e.g. SQL `CASE WHEN`).
- **The residual is overwhelmingly class B.** Every sampled residual raster was
  a conceptual diagram, GUI screenshot, architecture/class diagram, geometry
  plot or annotated-example illustration — redundant with the surrounding prose
  — except for the process flowcharts promoted to E.

### 2.3 Residual / vision pass

The residual (`rule-residual-conceptual`, 2,157 refs) is the validated default:
non-syntax, non-table-cell, non-cover images in a documentation context are
conceptual/illustrative and redundant with prose → B. Class-E flowcharts were
identified by a vision sweep of the conceptual-diagram manuals (Tuning Guide,
Administrator's Manual, Replication Manual, Log Analyzer, Heartbeat); each
verified flowchart's every reference (all languages/versions) is in the
`vision`/E set. No genuine class-D image was found in the sample.

## 3. Recoverable-information estimate

**Currently lost (C + D + E): 3,457 references.** The upload-package shards
carry only the Markdown `![]()` text and a dead link — no image binary — so all
information that lives only inside these graphics is invisible to the RAG/GPT
system today.

- **Class C — 3,405 references (~598 distinct railroad diagrams). This is the
  bulk of the recoverable payload.** It is the complete formal **grammar** of
  Altibase: SQL statements (SQL Reference — 2,582 refs), the stored-procedure
  language (Stored Procedures Manual — 407, `StoredProcedure1_Eng` — 90),
  external-procedure statements (120), utility command-line syntax (Utilities
  Manual — 114), Spatial SQL (66), DB-Link statements (24) and the 450 SQL
  optimizer **hints**. In the shards each of these sites currently shows only a
  `name ::=` label (or a bare `Syntax` heading) followed by a dead link — the
  production itself is **100% lost**. Recovering C as BNF/EBNF text restores
  machine-answerable syntax for essentially every Altibase statement.
- **Class E — 52 references (~11 distinct flowcharts).** Small but genuine
  process/decision logic: query-processing and optimizer pipelines, the
  index-type decision tree, replication fail-over (with a failure branch and a
  retry loop), the Log Analyzer API usage loop, the troubleshooting procedure,
  the data-type conversion graph, and the heartbeat state machine. Prose
  mentions these topics but not the branching/sequencing the diagrams encode.
- **Class D — 0 references.** No tabular-data-as-image was found. Altibase
  manuals render reference tables as Markdown tables; image-embedded tables seen
  in the sample (e.g. the Migration Center data-type-mapping dialog) are GUI
  screenshots classified B, not standalone data tables. **IMG-03's class-D
  conversion step will have nothing to do.**

Skipped as redundant: **A — 185** (data-type syntax diagrams that sit directly
above an identical text `Syntax` block, e.g. `bigint1.png`) and **B — 3,769**
(conceptual diagrams, architecture/class diagrams, GUI screenshots, geometry
plots, syntax-diagram legend symbols, cover-page logos).

## 4. Worked examples

### Class A — syntax diagram redundant with adjacent text block (skip)

- `img-00231` `media/GeneralReference/bigint1.png` — under `BIGINT > Syntax
  Diagram`; the very next heading is `Syntax` with a fenced block containing
  `BIGINT`. The railroad image carries nothing the text block does not.
- `img-01365` `bigint1.png` (Korean) — same page, `흐름도` heading followed by a
  `구문` fenced block — the Korean mirror of the above.
- `img-00227` `media/GeneralReference/242f2c3edb0f197d371a4ec74f665ba8.jpg` —
  a data-type `Syntax Diagram` figure immediately above its text `Syntax` block.

### Class B — conceptual diagram / screenshot redundant with prose (skip)

- `img-00001` `media/common/e5cfb376…png` — the cover-page logo (`<img>` inside
  PDF-margin comments); no recoverable text.
- `img-01075` `media/Utilities/su_policy_eng.png` — a Master-DB→Slave-DB box
  diagram; the surrounding prose already states the synchronization policy.
- `img-00099` `media/Admin/7-20.png` — partition `SPLIT` illustration; the prose
  narrates it step by step ("① a new partition part_4 is created, ② records are
  moved …").
- `img-04999` `media/Admin/image012.gif` — a `SELECT` box, one legend symbol in
  the "Syntax Diagram Conventions" table; its meaning is the adjacent cell.

### Class C — railroad diagram, only source of the grammar (convert)

- `img-00999` `media/StoredProcedure/invoker_rights_clause.gif` — preceded by
  the label `invoker_rights_clause::=`; the railroad is the **only** definition
  of that production. Text around it has just the `::=` label.
- `img-00499` `media/SQL/full scan.gif` — under `Hint List > FULL SCAN`; the
  raster is the railroad `FULL → SCAN → ( → tbl_name → )`. The prose only says
  "this hint specifies that the full table scan will be performed" — the
  grammar `FULL SCAN(tbl_name)` exists nowhere as text.
- `img-00565` `media/SQL/97f0082b…png` — `ALTER DATABASE` under `Syntax`, label
  `alter_database :: =`; the statement grammar is image-only.

### Class D — tabular data rendered as an image (convert)

**None.** No class-D reference exists in the `Manuals/` tree (see §3).

### Class E — process/decision flowchart (convert)

- `img-00088` `media/Admin/cdba9650…png` ("Types of Indexes") — a textbook
  **decision flowchart**: YES/No decision diamonds (`Index Partitioning
  Status`, `index_part_key == table_part_key`, `index_part_key == index_key`)
  branching to five index-type outcomes. The branching logic is not in prose.
- `img-00460` `media/Replication/Replication_eng.1.22.1.jpg` ("Fail-Over
  Process") — a normal-vs-abnormal connection flowchart with a failure branch
  ("Failure occurs. Use Fail-Over." → connect to DB B → check sync) and a retry
  loop.
- `img-00332` `media/LogAnalyzer/basic_use_eng.png` ("Basic Usage") — a
  five-step process flowchart with a back-edge ("Repeat until Xlog Sender
  ends"); the prose explicitly says "the following diagram illustrates the
  steps".
- `img-00358` `media/TuningGuide/BASIC_STEPS_IN_QUERY_PROCESSING.gif` — the
  client/server query-processing pipeline (Parsing → Validation → Optimization
  → Binding → Execution).

## 5. Raster readability

| Flag | Count | Handling |
| --- | ---: | --- |
| `yes` | 7,299 | raster file resolves and is a readable `.gif`/`.png`/`.jpg` |
| `low_res` | 0 | none encountered in the sampled rasters |
| `missing` | 112 | `image_path_resolved` is empty — the binary does not exist |

The 112 `missing` rasters were classified from document context alone (no
guessing from a non-existent image): 92 fall in class C and 20 in class B. The
**92 missing class-C rasters are the priority flag for IMG-03** — their grammar
cannot be transcribed from the (absent) raster and must come from the PDF
fallback (spec §8) or be flagged unconverted. No raster was readable-but-too-
low-resolution in the sample; if IMG-03 hits one it should set `low_res` and
use the PDF fallback rather than guess.

## 6. Stop/go assessment

**Go — continue the runner.** C + D + E = **3,457** references is far from
negligible. Class C alone (3,405 refs / ~598 distinct railroad diagrams) is the
entire formal grammar of Altibase SQL, PSM, external procedures, utility
commands and hints, and it is **100% lost** in the current shards. IMG-03/04
would therefore recover a large, high-value body of text. Class E adds ~11
genuine process/decision flowcharts. Only class D is empty, so IMG-03's
table-conversion path will simply find nothing to do — that is expected and not
a failure.

## 7. Risks and limitations

- **Class-E completeness is best-effort.** E is rare and scattered; it was
  found by a vision sweep of the conceptual-diagram manuals, not an exhaustive
  read of all ~3,000 distinct B/E rasters. A small number of flowcharts may
  remain mislabelled B. Per spec §11 this is the classification false-negative
  risk; Phase 5's stratified re-check of A/B classifications is the safety net.
- **A/B boundary is low-stakes.** Both A and B are skipped, so an A↔B mistake
  changes nothing downstream; effort was therefore spent on the C and E
  boundaries instead.
- **Rule pass favours C.** Where the residual rules were uncertain the row was
  pushed toward C, not A/B (e.g. a `Syntax`-section image with no detected text
  block → C). A wrong C only wastes a conversion; a wrong A/B silently drops
  unique grammar.
- **92 missing class-C rasters** require the PDF fallback in IMG-03; they cannot
  be transcribed from the inventory alone.
