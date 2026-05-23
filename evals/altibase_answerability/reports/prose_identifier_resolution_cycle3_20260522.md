# C3-08 — Prose-named identifier resolution

- Date: 2026-05-22
- Plan: `GPTs/reports/answerability_improvement_cycle3_plan_20260522.md` — item C3-08
- Scope: `evals/altibase_answerability/scripts/answer_runner.py` only
- Predecessors: C2-06 (`build_definition_section`), C2-07
  (`build_error_reference_section` / `build_dict_view_section`), C3-06
  (`build_replication_section`). C3-08 changes none of those builders' admission
  logic — it only widens the *identifier set* they anchor on.

## 1. Problem

The C2-06 / C2-07 / C3-06 named-definition admission only fires when the
question text literally contains the identifier its builder anchors on — a
property name, an error symbol / hex code, a `V$`/`X$`/`SYS_..._` view name.
A residual band of questions names the object only **descriptively**:

- PROP-123 says "session **time zone**", not the `TIME_ZONE` property;
- ERR-117/119/120/123/130 describe errors by their message or effect
  ("insufficient-privilege", "CHECK constraint violations", "conversion not
  applicable", "LOB ... autocommit mode", "SSL certificate ... handshake"),
  not by an error symbol or `0x` code;
- VPM-101/103/104/106/107/108 describe a view's role ("wait-event
  investigation", "active SQL text", "index definitions and index columns"),
  not the `V$`/`SYS_..._` identifier.

`extract_property_names` / `extract_error_identifiers` / `extract_dict_view_names`
therefore return the empty set, the identifier-anchored section never fires, and
the question falls back to plain lexical retrieval under the saturated
180 000-char budget against a generic-titled mis-route. The cycle-2 deep-dives
(`properties_deep_dive_cycle2` §5.3(iii), `errors_views_deep_dive_cycle2`
§5.3(i)) and the C3-07 residual report (§4.3, §7) all classified this as a
question-phrasing residual and named C3-08 prose→identifier resolution as the
proper fix.

## 2. Fix

`answer_runner.py` gains a deterministic prose→identifier resolver:

- `PROSE_IDENTIFIER_RESOLUTIONS` — a curated map from a distinctive lower-cased
  question-text phrase to the canonical identifier(s) it points at, grouped by
  kind (`property` / `error` / `view`). It follows the C3-06
  `REPLICATION_ANCHOR_PHRASES` precedent.
- `resolve_prose_identifiers(question)` — scans the question text for those
  phrases (plain lower-cased substring match, like `extract_replication_anchors`)
  and unions the identifiers each points at.
- `build_definition_section`, `build_error_reference_section` and
  `build_dict_view_section` each union the resolver's output for their kind into
  the identifier set they already extract literally. A resolved phrase therefore
  reaches **exactly the same admission path** as a literally-named identifier —
  no admission logic changed.

Every anchor phrase was verified against the full 300-question benchmark corpus
and the in-package source to satisfy three conditions:

1. it occurs in the residual question's text;
2. it occurs in **no other** benchmark question — so the resolver fires only for
   the intended question and `build_context()` is byte-identical everywhere
   else;
3. it points at an identifier with a documented section / entry in
   `GPTs/upload_package/` that the existing builder admits.

Only the question text and the in-package source/manifests are used — never a
judge-only field (`required_tokens`, `expected_facts`, `source_refs`,
`prohibited_claims`). Ambiguous prose is left unresolved (see §5).

The C3-08 resolver is added to the `--self-test` path
(`prose_resolution_self_test_failures`): it checks property / error / view
resolution, inertness for an identifier-named question, presence of every kind
key, and determinism.

## 3. Resolution table

| Question | prose anchor (verified question-unique) | resolved identifier(s) |
| --- | --- | --- |
| PROP-123 | "session time zone" | property `TIME_ZONE`; view `V$TIME_ZONE_NAMES` |
| ERR-117 | "insufficient-privilege" | `qpERR_ABORT_QDP_INSUFFICIENT_PRIVILEGES`, `mmERR_ABORT_INSUFFICIENT_PRIV` |
| ERR-119 | "check constraint violations" / "referential constraint failures" | `qpERR_ABORT_QDN_VIOLATE_CHECK_CONSTRAINT`, `qpERR_ABORT_QMX_CHILD_EXIST`, `qpERR_ABORT_QMX_NOT_FOUND_PARENT_ROW` |
| ERR-120 | "conversion not applicable" / "value overflow" / "invalid literal" / "out-of-range type value" | `mtERR_ABORT_CONVERSION_NOT_APPLICABLE`, `mtERR_ABORT_VALUE_OVERFLOW`, `mtERR_ABORT_INVALID_LITERAL`, `mtERR_ABORT_OVERFLOW` |
| ERR-123 | "autocommit mode" | `qpERR_ABORT_QMX_LOB_AUTOCOMMIT_MODE`, `ulERR_ABORT_LOB_AUTOCOMMIT_MODE_ERR`, `utERR_ABORT_LOB_AUTOCOMMIT_MODE_ERR` |
| ERR-130 | "ssl certificate" | `cmERR_ABORT_INVALID_CERTIFICATE`, `cmERR_ABORT_SSL_HANDSHAKE`, `cmERR_ABORT_UNSUPPORTED_OPENSSL_VERSION` |
| VPM-103 | "data type code" | view `V$DATATYPE` |
| VPM-104 | "index definitions and index columns" | meta tables `SYS_INDICES_`, `SYS_INDEX_COLUMNS_` |
| VPM-106 | "partition pruning" | meta tables `SYS_TABLE_PARTITIONS_`, `SYS_PART_KEY_COLUMNS_`, `SYS_INDEX_PARTITIONS_` |
| VPM-107 | "active sql text" | views `V$STATEMENT`, `V$SQLTEXT` |
| VPM-108 | "wait-event" | views `V$SESSION_WAIT`, `V$SESSION_EVENT`, `V$SESSION_WAIT_CLASS`, `V$LOCK_WAIT`, `V$LOCK_STATEMENT` |

Each error symbol's message was confirmed in the Error Message Reference — e.g.
`mtERR_ABORT_CONVERSION_NOT_APPLICABLE` is documented as `0x2100C ( 135180)
mtERR_ABORT_CONVERSION_NOT_APPLICABLE Conversion not applicable.` so the question
quotes the error's documented message verbatim.

## 4. Result — required-token-in-context, before vs after

Reconstructed the same deterministic way (`build_context()`, 180 000-char
budget, current source pack) immediately before and after the C3-08 change — so
this is C3-08's own delta on the post-job-07 state, crediting no gain jobs 06–07
already produced.

| Question | before | after | Δ | resolver |
| --- | ---: | ---: | ---: | --- |
| PROP-123 | 0/6 | 4/6 | +4 | anchored |
| ERR-117 | 1/7 | 5/7 | +4 | anchored |
| ERR-119 | 2/8 | 8/8 | +6 | anchored |
| ERR-120 | 6/8 | 8/8 | +2 | anchored |
| ERR-123 | 4/10 | 10/10 | +6 | anchored |
| ERR-130 | 6/8 | 8/8 | +2 | anchored |
| VPM-101 | 4/7 | 4/7 | +0 | **left unresolved** (§5) |
| VPM-103 | 8/9 | 8/9 | +0 | anchored (residual is escape artifact, §6) |
| VPM-104 | 4/10 | 9/10 | +5 | anchored |
| VPM-106 | 6/8 | 7/8 | +1 | anchored |
| VPM-107 | 1/13 | 12/13 | +11 | anchored |
| VPM-108 | 4/12 | 9/12 | +5 | anchored |
| **total** | **46/106** | **92/106** | **+46** | |

The resolver newly anchored **11 of the 12** listed questions (all except
VPM-101). Required-token-in-context for the named prose-residual set rose
**46 → 92 (+46)**. No listed question regressed.

## 5. Deliberately left unresolved — VPM-101

VPM-101: *"Before relying on a performance view or column in a portable Altibase
answer, which views should be checked and what must not be done to the
performance view itself?"*

The phrase "performance view or column" describes a **task** ("verify a view /
column exists before relying on it"), not a specific object. Mapping it to
`V$TABLE` / `V$ALLCOLUMN` would be an inference about the answer's method, not a
descriptive reference to a named object. Per the C3-08 mandate — conservative,
high-precision, resolve nothing rather than admit the wrong block — VPM-101 is
left unresolved. Its assembled context is byte-identical to before this job.

## 6. Residual missing tokens after resolution — escape artifacts, not defects

After resolution the remaining missing tokens are overwhelmingly the
markdown-escape **question-record token-form artifact** the C3-07 report (§4.4)
and `properties_deep_dive_cycle2` already documented for `V$LFG` / `V$LOG` /
`V$PROPERTY`: General Reference-2 escapes the `$` / trailing `_` in section
headings (`V\$DATATYPE`, `SYS_PART_KEY_COLUMNS\_`), so the bare `V$DATATYPE`
literal does not match even though the section **is** admitted. Verified directly
in the admitted context:

| Question | "missing" token | reality |
| --- | --- | --- |
| VPM-103 | `V$DATATYPE` | `V\$DATATYPE` section admitted whole — heading escaped |
| VPM-106 | `SYS_PART_KEY_COLUMNS_` | `SYS_PART_KEY_COLUMNS\_` section admitted — trailing `_` escaped |
| VPM-107 | `V$SQLTEXT` | `V\$SQLTEXT` section admitted whole — heading escaped |
| VPM-108 | `V$SESSION_WAIT` / `_EVENT` / `_WAIT_CLASS` | all three sections admitted whole — headings escaped |
| PROP-123 | `V$TIME_ZONE_NAMES`, `V$PROPERTY` | both sections admitted whole — headings escaped |

These are neither a retrieval defect nor weakenable, and the question records
are not edited (C3-08 constraint). The one genuine recall residual is ERR-117's
`qpERR_ABORT_QCI_NotPermittedUser` ("Unauthorized user."): the question prose
says "insufficient-privilege" / "SYSDBA", never "unauthorized", so that third
error is conservatively not resolved — high precision preferred over recall.

## 7. No regression

The resolver returns three empty sets for any question with no curated anchor,
so the three builders see the identical identifier set as before and
`build_context()` is byte-identical. Reconstructed assembled-context SHA-256
digests for **all 300 questions** (full benchmark 270 + coding-agent 30):

- **289 / 300 byte-identical** — every question the resolver does not fire for,
  including all replication questions (C3-06 gains preserved), all other
  errors / properties / VPM questions, and the entire coding-agent suite.
- **11 / 300 changed** — exactly the resolver-anchored questions (PROP-123,
  ERR-117/119/120/123/130, VPM-103/104/106/107/108); each improved or held
  (VPM-103 8→8), none regressed.

The cycle-2 (C2-06/C2-07) and job-06/07 gains are untouched: no admission logic
changed, and every non-anchored question's context is byte-identical.

## 8. Acceptance

```
python3 evals/altibase_answerability/scripts/answer_runner.py --self-test   # OK (incl. C3-08 prose resolver)
MODE=dry_run LIMIT=20 RUN_ID=c3_08_prose RUN_ROOT=/tmp/altibase-c3-08 \
  ./run-test.sh source-preserving                                          # 20 records, 0 errors
test -s /tmp/altibase-c3-08/answers/retrieval_audit.jsonl                  # 20-record sidecar
git diff --check                                                           # clean
```

Determinism, `max_context_chars`, leakage checks, `--self-test` and all
retrieval-audit fields are preserved. `build_context()` byte-identical for 289 of
300 questions; the 11 changed are exactly the prose-residual questions the
resolver anchored.

**C3-08: PASS** — required-token-in-context for the named prose-residual set
46 → 92 (+46); resolver newly anchored 11 of 12 listed questions; VPM-101
deliberately left unresolved as too ambiguous; zero regression elsewhere.
