# Korean-Aligned English Baseline: Release, Patch, Technical, And AID Batch

- Job: `S1-J010`
- Scope: release notes, exact product and patch version boundaries, 7.1 and 7.3
  patch-note routing, `BUG-*` and `TASK-*` token preservation, selected
  technical documents, selected third-party guide boundaries, and AID
  upload-content candidate reuse.
- Source-pack gate: `GPTs/source_pack/source_pack_validation.md` records
  `Status: pass`, `Verdict: Pass`, no source-pack validation blockers, and the
  explicit continuation gate for the Korean-aligned English baseline.
- Authority rule: Korean product manuals, Korean release notes, Korean patch
  notes, Korean technical documents, and Korean third-party guides are
  authoritative where selected. English files are extraction aids unless an AID
  classification explicitly allows English-only auxiliary use. For 8.1
  material, preserve the established `Altibase 8.1 verified source` boundary.
- Downstream boundary: this file is a working baseline for guarded first
  drafts. It does not replace exact source-pack extraction, full patch-note
  translation, installed-version checks, live platform validation, connector
  testing, or AID evidence-ledger review.

## Batch Source Coverage

| Source group | Source IDs | Baseline manifest rows | Alignment status |
| --- | --- | --- | --- |
| Product release and version boundary sources | `SRC-000033`, `SRC-000064`, `SRC-000424` through `SRC-000429`, `SRC-000450` through `SRC-000452`, `SRC-000477` | `KAE-BLOCK-000027`, `KAE-BLOCK-000028`, `KAE-BLOCK-000039`, `KAE-BLOCK-000171`, `KAE-BLOCK-000172`, `KAE-BLOCK-000215`, `KAE-BLOCK-000253`, plus `KAE-BLOCK-000275` | aligned for routing; exact item claims still require source recheck |
| 7.1 patch notes and version histories | `SRC-000228` through `SRC-000396`, including English extraction-aid row `SRC-000300` | `KAE-BLOCK-000022` through `KAE-BLOCK-000133`, plus `KAE-BLOCK-000275` | aligned for patch routing; full token-by-token translation remains not-ready |
| 7.3 patch notes and version histories | `SRC-000397` through `SRC-000423` | `KAE-BLOCK-000173` through `KAE-BLOCK-000190`, plus `KAE-BLOCK-000275` | aligned for patch routing; full token-by-token translation remains not-ready |
| Selected technical documents | `SRC-000472` through `SRC-000476` | `KAE-BLOCK-000230` through `KAE-BLOCK-000234`, plus `KAE-BLOCK-000275` | aligned for routing; platform and compatibility matrices remain exact-source checks |
| Selected third-party guides | `SRC-000001` through `SRC-000014` | `KAE-BLOCK-000240` through `KAE-BLOCK-000250`, reused through `KAE-BLOCK-000274`, plus `KAE-BLOCK-000275` | reused from S1-J009; live connector support remains not-ready |
| AID upload-content candidates | Upload-content candidate tiers `AID-000001` through `AID-000005`; evidence-only or limitation tiers `AID-000006` through `AID-000028`; exact file rows `AID-SRC-000001` through `AID-SRC-000438`; source-pack support evidence `AID-000009` through `AID-000025` | `KAE-BLOCK-000276` | aid_reuse with AID classifications preserved |

## KAE-RELPAID-BLOCK-001: Product Release And Version Boundaries

- Source IDs: `SRC-000033`, `SRC-000064`, `SRC-000424`, `SRC-000425`,
  `SRC-000426`, `SRC-000427`, `SRC-000428`, `SRC-000429`, `SRC-000450`,
  `SRC-000451`, `SRC-000452`, with 8.1 verification support from
  `SRC-000477`.
- Version scope: 7.1, 7.3, `Altibase 8.1 verified source`, and exact release
  note rows `7.1.0.1.2`, `7.3.0.0.1`, and `8.1.0.0.1`.
- Source block refs: inherited from `KAE-BLOCK-000027`,
  `KAE-BLOCK-000028`, `KAE-BLOCK-000039`, `KAE-BLOCK-000171`,
  `KAE-BLOCK-000172`, `KAE-BLOCK-000215`, and `KAE-BLOCK-000253`.
- Alignment status: baseline generated for release-boundary routing. Exact
  feature lists, package tables, download rows, and platform matrices remain
  exact-source checks.

Baseline:

1. Treat release notes as version-boundary sources, not broad product manuals.
   A statement from `Altibase 7.1.0.1.2 Release Notes`,
   `Altibase 7.3.0.0.1 Release Notes`, or `Altibase 8.1.0.0.1 Release Notes`
   must keep that exact version scope unless a manual or later patch source is
   also cited.
2. Preserve the initial-release boundaries:
   `7.1.0.1.2 (Released)`, `7.3.0.0.1 (Released)`, and
   `8.1.0.0.1`. Do not describe a feature as available in all 7.1, all 7.3,
   or all 8.1 patches unless the exact source supports that broader scope.
3. For 7.3 release-note content, preserve feature boundaries such as AKU,
   altiShapeLoader 1.0, partial JDBC API Specification 4.2 support, OpenSSL
   3.0.8, TLS 1.3, SQL extensions, Spatial SQL improvements, replication
   improvements, application development interface improvements, utility
   improvements, and package/download changes as 7.3 release-note material.
4. For 8.1 release-note content, preserve the `Altibase 8.1 verified source`
   boundary for native `JSON`, Temporary LOB, KADA APIs, Kafka source/sink
   connectors, ABM, replication SSL/TLS, `altiEncrypt`, encrypted iSQL
   password-file login support, checkpoint-scale single mode, and the listed
   performance and integration improvements.
5. Platform rows in release notes are exact-version evidence. If a platform
   claim also appears in `Supported Platforms`, resolve the customer-facing
   answer by target version and patch first, then by the Korean authoritative
   technical document before using the English table as an extraction aid.

Safe first checks:

- Ask for the target Altibase product version and patch level before using
  release-note content to answer availability, compatibility, or syntax
  questions.
- For 8.1-only features, require either an `Altibase 8.1 verified source`
  citation or installed-version evidence such as `V$VERSION`.
- For package or platform support, check `SRC-000476` and the exact release
  note row before converting table markers into prose.

Stop conditions:

- Stop if a requested feature is cited only from a different major or patch
  line.
- Stop if the user asks for a definitive platform-support answer without
  exact OS, CPU architecture, glibc or vendor level, server/client package,
  and Altibase patch level.
- Stop if a claim depends on live package availability or download URLs; this
  baseline preserves source-backed documentation, not current distribution
  state.

## KAE-RELPAID-BLOCK-002: 7.1 And 7.3 Patch Notes, Version Histories, BUG Tokens, And TASK Tokens

- Source IDs: 7.1 patch-note corpus `SRC-000228` through `SRC-000396`;
  7.3 patch-note corpus `SRC-000397` through `SRC-000423`.
- Version scope: exact patch versions from `7.1.0.1.3` through
  `7.1.0.10.8` where selected, plus exact 7.3 patch versions from
  `7.3.0.0.2` through `7.3.0.2.0` where selected.
- Source block refs: inherited from `KAE-BLOCK-000022` through
  `KAE-BLOCK-000133` for 7.1 and `KAE-BLOCK-000173` through
  `KAE-BLOCK-000190` for 7.3.
- Alignment status: baseline generated for deterministic patch routing and
  token preservation. Full Korean-to-English normalization of every
  token-specific behavior paragraph is recorded as not-ready in `CONF-000007`.

Token preservation checkpoint:

| Patch corpus | Selected sources | Korean authoritative rows | English extraction-aid rows | Mixed index rows | Unique `BUG-*`/`TASK-*` tokens detected | No-token source IDs |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Altibase 7.1 patch notes | 169 | 96 | 70 | 3 | 990 | `SRC-000229`, `SRC-000230`, `SRC-000300` |
| Altibase 7.3 patch notes | 27 | 19 | 6 | 2 | 235 | `SRC-000398`, `SRC-000404` |

Version-history checkpoints:

1. The 7.1 version-history source maps database binary version, meta version,
   CM protocol version, and replication protocol version by patch band. Keep
   exact bands such as `7.1.0.10.1~`, `7.1.0.10.0`, `7.1.0.8.6 ~
   7.1.0.9.9`, `7.1.0.8.5`, `7.1.0.6.6 ~ 7.1.0.8.4`,
   `7.1.0.6.5`, `7.1.0.6.2 ~ 7.1.0.6.4`, `7.1.0.6.1`,
   `7.1.0.4.5 ~ 7.1.0.6.0`, `7.1.0.4.4`, `7.1.0.4.1 ~
   7.1.0.4.3`, `7.1.0.4.0`, `7.1.0.2.5 ~ 7.1.0.3.9`,
   `7.1.0.2.4`, `7.1.0.1.9 ~ 7.1.0.2.3`, `7.1.0.1.8`,
   `7.1.0.1.5 ~ 7.1.0.1.7`, `7.1.0.1.4`, `7.1.0.1.3`, and
   `7.1.0.1.2 (Released)`.
2. The 7.1 version-history source records database binary version `6.5.1`
   across the selected rows, with meta versions including `8.5.1` through
   `8.12.1`, CM protocol versions `7.1.6` and `7.1.7`, and replication
   protocol versions `7.4.2` through `7.4.7`. Do not infer compatibility from
   the product version alone; use the explicit version-history row.
3. The 7.3 version-history source preserves `7.3.0.0.1 (Released)`,
   `7.3.0.0.2 ~ 7.3.0.0.7`, `7.3.0.0.8`, and `7.3.0.0.8~`, with database
   binary version `7.3.0`, meta versions `9.3.1` and `9.4.1`, CM protocol
   version `7.1.8`, and replication protocol version `7.4.9`.
4. Patch-note `BUG-*` and `TASK-*` identifiers are evidence tokens. Preserve
   them exactly, including hyphen and digits, and do not collapse multiple
   tokens into one issue. A token can be cited only with its source ID, patch
   version, and authority label.

Safe first checks:

- Ask for the exact Altibase patch before using a patch-note change to
  generate SQL, commands, configuration, compatibility guidance, or a root
  cause.
- For a token-specific answer, cite the exact token, patch version, and source
  ID. If a Korean and English source pair exists, use Korean as authority and
  English only as an extraction aid.
- For a patch note with no paired English source, translate the Korean source
  into English only for the requested token or section, and mark the answer as
  source-normalized from Korean.

Stop conditions:

- Stop if the user asks for an exhaustive patch-change list from this baseline
  alone. Route to the exact source-pack row or source file and generate a
  scoped token-level extraction.
- Stop if the requested behavior depends on runtime state, installed binaries,
  patch provenance, customer logs, trace output, object definitions, or live
  reproduction.
- Stop if the request tries to backport a later patch behavior to an earlier
  patch without explicit source evidence.

## KAE-RELPAID-BLOCK-003: Technical Documents And Third-Party Guide Boundaries

- Source IDs: technical documents `SRC-000472` through `SRC-000476`; selected
  third-party guides `SRC-000001` through `SRC-000014`.
- Version scope: multi-version technical support and selected integration
  guides.
- Source block refs: inherited from `KAE-BLOCK-000230` through
  `KAE-BLOCK-000250`, and reused from `KAE-BLOCK-000274` for detailed
  client-tool integration baseline content.
- Alignment status: technical-document routing generated for this batch;
  third-party guide content reused from S1-J009. Live platform, connector,
  Kubernetes, NiFi, Tableau, Spring, Hibernate, and AKU compatibility remain
  not-ready without customer environment evidence.

Baseline:

1. `SRC-000476` is the Korean authoritative supported-platform technical
   document. `SRC-000472` is the English extraction aid. Preserve exact
   version and patch qualifiers in platform rows, including rows that depend
   on minimum patch levels such as `Altibase 7.3.0.1.2` or `Altibase
   7.3.0.0.9`, and rows that distinguish server/client support from library
   and tool support.
2. `SRC-000473` is the Korean authoritative Java compatibility source. Treat
   Java compatibility markers as table evidence, not as a broad guarantee for
   every framework, driver, application server, or JDK vendor.
3. `SRC-000474` is a Korean authoritative replication network-check document.
   Use it as a source-backed next check for replication send/receive behavior,
   especially when the answer depends on whether receiver-side counters such
   as `insert_success_count` increase in the customer's environment.
4. `SRC-000475` is a Korean authoritative replication compatibility document.
   It records that Altibase supports replication lower compatibility from
   version 6 onward when the upper two digits of the replication protocol are
   the same, but eager mode and offline replication are exceptions that require
   both server versions to match. Preserve table-level sender, receiver, mode,
   and compatibility values rather than converting them into generic upgrade
   advice.
5. Third-party guides in `SRC-000001` through `SRC-000014` remain selected
   source evidence for AKU, Kubernetes, NiFi, Tableau, Spring Data JPA, and
   Hibernate integration. Reuse the S1-J009 client-tool integration baseline
   for generated first drafts, and require live customer versions before
   making support or compatibility claims.

Safe first checks:

- For platform support, ask for Altibase version, patch level, server/client
  package, operating system, CPU architecture, OS minor version, and relevant
  library level before answering.
- For replication compatibility, ask for both Altibase versions, replication
  mode, protocol version if known, topology, current gap, and whether eager or
  offline replication is involved.
- For third-party integrations, ask for the external product version, Altibase
  client or driver version, configuration files, logs, and a minimal
  connection or workload test.

Stop conditions:

- Stop if the OS, connector, Java, or external product is not listed in the
  selected source or customer evidence.
- Stop if the requested answer depends on current vendor support outside the
  selected documents.
- Stop if a generated integration artifact would require credentials,
  certificates, package URLs, cluster state, schema DDL, or tool output that
  the customer has not provided.

## KAE-RELPAID-BLOCK-004: AID Upload-Content Candidate Reuse And Classification Preservation

- Source IDs: upload-content candidate AID tier rows `AID-000001` through
  `AID-000005`; evidence-only or limitation tier rows `AID-000006` through
  `AID-000028`; exact upload-content candidate rows `AID-SRC-000001`
  through `AID-SRC-000438`; source-pack evidence-only and limitation support
  rows `AID-000009` through `AID-000025`.
- Version scope: AID.
- Source block refs: exact source-pack rows for `AID-SRC-000001` through
  `AID-SRC-000438` and support-evidence rows `AID-000009` through
  `AID-000025`.
- Alignment status: aid_reuse. This job reuses AID stabilized English and
  source-backed `llm-reference` candidates only where the existing AID
  classifications permit use.

AID classification checkpoint:

| AID source set | Count | Required handling |
| --- | ---: | --- |
| `Korean-source-verified` exact AID source rows | 167 | Upload-content candidate after packaging selection; preserve label |
| `Link-validated Korean-source-verified` exact AID source rows | 129 | Upload-content candidate after packaging selection; preserve label |
| `English-only source` exact AID source rows | 126 | Auxiliary only with explicit English-only confidence label |
| Source-backed `llm-reference` exact rows with mixed preserved labels | 16 | Upload-content candidate; preserve Korean-source-verified, link-validated, English-only, and source_limitation labels |
| AID support-evidence rows | 17 | Evidence-only unless a later job explicitly selects evidence text for package documentation |

Baseline:

1. AID stabilized English and source-backed `llm-reference` files are reusable
   working sources when their AID classification permits it. This job does not
   schedule a blanket AID rewrite and does not alter `aid_tier_manifest.tsv`.
2. `AID-000001` and `AID-000002` represent Korean-source-verified or
   link-validated Korean-source-verified upload-content candidate sets.
   Preserve per-file labels from the source manifest and AID evidence.
3. `AID-000003` represents English-only auxiliary FAQE material. It remains
   usable only with explicit `English-only source` or
   `english_only_auxiliary` handling and must not be presented as
   Korean-source-verified.
4. `AID-000004` and `AID-000005` represent source-backed `llm-reference` and
   GPT upload candidate material. They are candidates for the repository final
   package, not an automatic separate upload, and they count against the
   global 20 Markdown file upload limit if selected.
5. `AID-000006` through `AID-000028` are evidence-only or accepted-limitation
   rows by default. Do not convert manifests, coverage ledgers, review
   reports, diagram registers, URL registers, or accepted limitation ledgers
   into customer upload content unless a later packaging job explicitly
   records that decision.
6. Accepted AID limitations remain limitations. Preserve
   `source_limitation`, `legacy_no_downloadable_url`,
   `legacy_attachment_label_only`, `diagram_unavailable`,
   `not_document_format`, `accepted_source_limitation`, and
   `accepted_english_only_auxiliary` labels instead of inventing missing
   URLs, diagrams, source variants, or exact values.

Safe first checks:

- Before packaging AID-derived customer content, check `aid_tier_manifest.tsv`,
  `source_manifest.tsv`, AID `source-inventory.tsv`, and AID
  `omissions-and-risks.tsv` for the exact source row and label.
- If an AID answer depends on exact customer environment, patch level, logs,
  runtime state, object definitions, unsupported behavior, or live validation,
  ask for that evidence and provide the safest next check.
- If an AID source conflicts with selected Altibase manual or release-note
  sources, record the conflict and resolve it using the active
  Korean-authoritative source policy.

Stop conditions:

- Stop if an AID evidence-only file is being treated as customer upload content
  without an explicit packaging decision.
- Stop if an English-only AID source is being cited as Korean-source-verified.
- Stop if a source-limitation row is being expanded into invented customer
  content.

## Remaining Not-Ready Gaps

The batch is intentionally deterministic but not exhaustive. `CONF-000007`
records these residual gaps for downstream work:

1. Full English normalization of every 7.1 and 7.3 patch-note `BUG-*` and
   `TASK-*` paragraph remains not-ready. The exact source pack preserves the
   tokens and source boundaries, and this baseline provides routing rules and
   counts.
2. Exhaustive conversion of release-note platform, package, download, and
   compatibility tables remains not-ready. Use the exact version source and
   technical documents before producing customer claims.
3. Third-party guide claims remain not-ready for live support status without
   customer product versions, installed packages, configuration files, logs,
   and a controlled validation result.
4. AID packaging remains a later upload-package decision. This job preserves
   classifications and reuses approved working sources; it does not decide the
   final 20-file upload composition.

## S1-J010 Self-Review Notes

- Patch/version boundary: Pass for routing. Exact version bands and token
  counts are preserved, and broad availability claims are blocked by stop
  conditions.
- AID classification preservation: Pass. `Korean-source-verified`,
  `Link-validated Korean-source-verified`, `English-only source`, and
  `source_limitation` handling are preserved.
- Unsupported inference: Pass after recording `CONF-000007` for exhaustive
  patch-token, platform-table, third-party live-support, and final AID
  packaging gaps.
