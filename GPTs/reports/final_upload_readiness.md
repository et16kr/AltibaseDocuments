# Altibase GPT Final Upload Readiness

Job: `J040`
Status: Pass
Date: 2026-05-17

## Reconfirmed Requirement And Boundary

J040 finalizes retrieval structure, multilingual policy, validation evidence, final gap
review, and upload readiness for the 20 customer-facing Markdown attachments in
`GPTs/attachments/`, excluding `README.md`.

This job is a documentation-scope finalization job. It does not add, remove, rename, or
rewrite customer-facing attachment files because the final structural and policy checks
passed and no attachment boundary or source-label defect was found.

## Scoped Source Families

J040 covers the full selected rebuild scope through the active support reports:

- Altibase 7.1, 7.3, and Altibase 8.1 verified source product manuals.
- Korean release notes and patch notes, with English notes used only as extraction aids
  when consistent.
- Tool manuals, technical documents, third-party guides, and approved support reports.
- Retrieval, visual conversion, source inventory, coverage matrix, gap register,
  multilingual prompt, and smoke-test reports.

Korean manuals and Korean release notes remain authoritative when paired Korean and
English sources differ. Customer-facing answers must remain English-normalized in the
attachments, preserve literal technical tokens, and use `Altibase 8.1 verified source`
for 8.1 customer-facing source labels.

## Design Note

J040 adds this final readiness report and updates the support reports that define the
final handoff:

- `GPTs/reports/final_upload_readiness.md`: final upload-readiness sign-off.
- `GPTs/reports/gap_register.md`: final disposition of previously open items.
- `GPTs/reports/coverage_matrix.md`: J040 completion handoff.
- `GPTs/reports/source_inventory.md`: final source-inventory addendum.
- `GPTs/reports/multilingual_prompt_set.md` and
  `GPTs/reports/multilingual_smoke_results.md`: final multilingual validation labels.

No customer-facing attachment text changed because the current attachment set already
contains the required multilingual policy, literal-token policy, version scope, safe
8.1 label, retrieval sections, and cross-file routing. Remaining uncertainty is tracked
as guardrails or verification limits, not unregistered work.

## Upload Package

The upload package is exactly these 20 Markdown files:

1. `00_version_release_platform.md`
2. `01_getting_started_installation.md`
3. `02_administration_operations.md`
4. `03_sql_ddl_generation.md`
5. `04_sql_dml_oracle_compatibility.md`
6. `05_data_types_properties.md`
7. `06_data_dictionary_performance_views.md`
8. `07_error_messages_troubleshooting.md`
9. `08_performance_tuning_monitoring.md`
10. `09_replication_ha_cdc.md`
11. `10_psm_stored_external_procedures.md`
12. `11_java_jdbc_spring.md`
13. `12_c_cli_odbc_precompiler.md`
14. `13_isql_iloader_basic_tools.md`
15. `14_utilities_operation_tools.md`
16. `15_migration_oracle_compatibility.md`
17. `16_dblink_external_connectors.md`
18. `17_kubernetes_aku_cloud.md`
19. `18_security_ssl_tls.md`
20. `19_spatial_nifi_tableau_misc.md`

`GPTs/attachments/README.md` remains a policy/readme file and is not counted as an
upload attachment.

## Retrieval Readiness

Current retrieval checks found:

- Exactly 20 upload Markdown files.
- No residual image references, source-local image paths, `file://` links, Windows drive
  paths, local workstation paths, or internal source path labels in customer-facing
  attachments.
- Every upload attachment has `Applicable Versions`, `Source Documents`, and
  `Questions This File Can Answer` sections.
- Every upload attachment uses `Altibase 8.1 verified source` somewhere in its 8.1
  coverage.
- No Korean, Chinese, Japanese, or other non-English prose appears in the canonical
  English attachment files.
- Long SQL/configuration examples that remain are headed and scoped as verification or
  runbook examples; R26 accepted them as retrieval-safe.

## Multilingual Readiness

The final multilingual policy is:

- Answer in the user's language whenever possible, or in the explicit language the user
  requests.
- Do not treat runtime multilingual support as a fixed language list.
- Preserve SQL object names, SQL keywords, function names, error codes, property names,
  commands, paths, package/class/method/API names, connector names, and version labels
  literally in every answer language.
- Ask for exact version, patch level, environment, log excerpt, object definition, or
  runtime evidence when those inputs determine a safe answer.

The multilingual smoke set covers 18 prompts across Vietnamese, Turkish, Persian,
Hindi, Chinese, Japanese, English/French override, German, and French. The staged smoke
simulation passed all 18 prompts with zero failures. This validates the policy pattern;
it is not a live post-upload GPT retrieval test.

## Final Gap Review

J040 reviewed the active gap register and removed unresolved `Open` status as a final
handoff state. Remaining entries are either:

- `Closed-trace`: resolved but retained for source-policy traceability.
- `Guardrail`: selected sources or attachment scope require exact version, installed
  header, object definition, runtime evidence, or source-backed confirmation before a
  definitive answer.
- `Verification-limited`: the documentation is source-backed, but live server, client,
  tool, compiler, Kubernetes, TLS, or third-party integration execution was not run.

Accepted final guardrails include direct-key type matrix details, exhaustive view-column
proof, uncovered exact error codes, `sdERR_*` source drift, Spatial `stERR_*` exact-code
itemization, `SQLEmptyLob()` / `SQLGetLobLength2()` compile-ready signatures,
low-retrieval per-property detail blocks, JSON execution-plan schema, cross-version
replication SSL compatibility, platform patch boundaries, Java compatibility drift, and
environment-specific tool/integration behavior.

These guardrails do not permit invented answers. They require the GPT to preserve the
customer's literal code or token, state the version/source limit, ask for the missing
input, and provide the safest source-backed next check.

## Verification Summary

Representative J040 checks:

```bash
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' | sort | wc -l
rg -n "trunk|C:/|file://|/home/et16|Manuals/Altibase|ReleaseNotes/|Technical Documents/|3rd Party Guide for Altibase|JOB-[0-9]+" GPTs/attachments GPTs/GPT_Instructions_Draft.md || true
rg -n -P "[\p{Hangul}\p{Han}\p{Hiragana}\p{Katakana}]" GPTs/attachments --glob '*.md' || true
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' -exec rg --files-without-match "Altibase 8\.1 verified source" {} + || true
rg -n "^Verdict: (Review Required|Fail)|^\| (Blocker|High|Medium|Low) \|" review/reports/R*.md || true
git diff --check
bash review/scripts/run_review_stage.sh validate
```

Result: pass after J040 report updates.

## Upload Readiness Decision

The attachment set is ready for upload as the staged Altibase GPT knowledge package,
subject to the normal operational step of uploading exactly the 20 Markdown files listed
above and applying `GPTs/GPT_Instructions_Draft.md` as the instruction basis.

After upload, run one live multilingual retrieval smoke check against the configured GPT
platform. That post-upload platform test is outside repository documentation scope.
