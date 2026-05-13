# Altibase GPTs Link Inventory

Job: `JOB-015`
Phase: P1 Inventory
Status: Complete

Objective: detect Windows absolute paths and broken image links in the selected source documents, and list cleanup targets for later attachment build jobs.

## Scope and Method

- Source list: `GPTs/reports/source_inventory.md`
- Selected Markdown source documents scanned: 114
- Missing selected source documents: 0
- Image references parsed: 3513
- Broken local image references found: 16
- Windows absolute or `file://` source lines found: 12
- Image patterns: Markdown image links and quoted HTML `<img src="...">` references.
- Broken-image rule: local image targets are resolved relative to the source Markdown file. External `http`, `https`, `mailto`, `data`, and fragment-only targets are not counted as broken local images.
- Windows-path rule: drive-root paths such as `C:\...`, `C:/...`, and `file://` links are listed for cleanup review. JDBC URLs such as `jdbc:Altibase://...` are intentionally excluded.

This is a work report, so source paths are retained for traceability. Customer-facing attachments should use customer-safe labels such as "Altibase 8.1 verified source" and must not copy internal source labels or source-local absolute paths.

## Summary Counts

| Category | Count | Cleanup expectation |
| --- | ---: | --- |
| Broken local image references | 16 | Convert to BNF/text/Mermaid/procedure text, or use the nearby corrected local image only for inspection. |
| Windows absolute or `file://` source lines | 12 | Replace user-machine paths with placeholders when copied; keep genuine product paths only when needed and documented as examples. |
| Missing selected source documents | 0 | No source availability cleanup needed for this job. |

### By Source Family

| Source family | Broken image refs | Windows/path lines |
| --- | ---: | ---: |
| Altibase 7.1 | 2 | 3 |
| Altibase 7.3 | 6 | 3 |
| Altibase 8.1 verified source | 8 | 4 |
| Third-party guide | 0 | 1 |
| Tool release source | 0 | 1 |

### By Target Attachment

| Target attachment | Broken image refs from mapped sources | Windows/path lines from mapped sources |
| --- | ---: | ---: |
| `03_sql_ddl_generation.md` | 5 | 0 |
| `04_sql_dml_oracle_compatibility.md` | 5 | 0 |
| `10_psm_stored_external_procedures.md` | 2 | 0 |
| `12_c_cli_odbc_precompiler.md` | 0 | 6 |
| `14_utilities_operation_tools.md` | 9 | 5 |
| `19_spatial_nifi_tableau_misc.md` | 0 | 1 |

## Cleanup Targets: Broken Image References

| Target attachment(s) | Source trace | Image target | Issue | Cleanup action |
| --- | --- | --- | --- | --- |
| `03_sql_ddl_generation.md`, `04_sql_dml_oracle_compatibility.md` | `Manuals/Altibase_7.1/eng/SQL Reference.md:10589` | `media/SQL_multiple_delete.png` | Missing local image file | Use `media/SQL/multiple_delete.png` as the local source if the diagram is inspected, then convert the `multiple_delete` syntax to compact BNF-like text. |
| `14_utilities_operation_tools.md` | `Manuals/Altibase_7.1/eng/Utilities Manual.md:488` | `/Users/richardnahm/Desktop/Documents/Manuals/Altibase_7.1/kor/media/Utilities/83e5d3722e9a7c575270c6a6bb5206c2.gif` | Missing local image file | Replace the user-machine absolute path with `media/Utilities/83e5d3722e9a7c575270c6a6bb5206c2.gif` for inspection, then convert the `aexport` syntax diagram to BNF-like text. |
| `03_sql_ddl_generation.md`, `04_sql_dml_oracle_compatibility.md` | `Manuals/Altibase_7.3/eng/SQL Reference.md:1858` | `Manuals/Altibase_trunk/eng/media/SQL/hash bucket count.gif` | Missing local image file | Treat as a repository-root path pasted into a relative link. Use `media/SQL/hash bucket count.gif` only for inspection, then convert the hint syntax diagram to BNF-like text. |
| `10_psm_stored_external_procedures.md` | `Manuals/Altibase_7.3/eng/Stored Procedures Manual.md:452` | `media/StoredProcedure/storedprocedure_structure_eng.png` | Missing local image file | Use the nearby `media/StoredProcedure/storedProcedure_structure.gif` only for inspection; replace the procedure block diagram with a concise text structure description. |
| `14_utilities_operation_tools.md` | `Manuals/Altibase_7.3/eng/Utilities Manual.md:1111` | `media/Utilities/su_policy_eng.png` | Missing local image file | Actual file is `media/su_policy_eng.png` in these source trees. Prefer the adjacent bullet definitions as text and omit the policy image in attachments. |
| `14_utilities_operation_tools.md` | `Manuals/Altibase_7.3/eng/Utilities Manual.md:1113` | `media/Utilities/si_policy_eng.png` | Missing local image file | Actual file is `media/si_policy_eng.png` in these source trees. Prefer the adjacent bullet definitions as text and omit the policy image in attachments. |
| `14_utilities_operation_tools.md` | `Manuals/Altibase_7.3/eng/Utilities Manual.md:1115` | `media/Utilities/mi_policy_eng.png` | Missing local image file | Actual file is `media/mi_policy_eng.png` in these source trees. Prefer the adjacent bullet definitions as text and omit the policy image in attachments. |
| `14_utilities_operation_tools.md` | `Manuals/Altibase_7.3/eng/Utilities Manual.md:1118` | `media/Utilities/sd_policy_eng.png` | Missing local image file | Actual file is `media/sd_policy_eng.png` in these source trees. Prefer the adjacent bullet definitions as text and omit the policy image in attachments. |
| `03_sql_ddl_generation.md`, `04_sql_dml_oracle_compatibility.md` | `Manuals/Altibase_trunk/eng/SQL Reference.md:1827` | `Manuals/Altibase_trunk/eng/media/SQL/full scan.gif` | Missing local image file | Treat as a repository-root path pasted into a relative link. Use `media/SQL/full scan.gif` only for inspection, then convert the hint syntax diagram to BNF-like text. |
| `03_sql_ddl_generation.md`, `04_sql_dml_oracle_compatibility.md` | `Manuals/Altibase_trunk/eng/SQL Reference.md:1833` | `Manuals/Altibase_trunk/eng/media/SQL/group bucket count.gif` | Missing local image file | Treat as a repository-root path pasted into a relative link. Use `media/SQL/group bucket count.gif` only for inspection, then convert the hint syntax diagram to BNF-like text. |
| `03_sql_ddl_generation.md`, `04_sql_dml_oracle_compatibility.md` | `Manuals/Altibase_trunk/eng/SQL Reference.md:1857` | `Manuals/Altibase_trunk/eng/media/SQL/hash bucket count.gif` | Missing local image file | Treat as a repository-root path pasted into a relative link. Use `media/SQL/hash bucket count.gif` only for inspection, then convert the hint syntax diagram to BNF-like text. |
| `10_psm_stored_external_procedures.md` | `Manuals/Altibase_trunk/eng/Stored Procedures Manual.md:452` | `media/StoredProcedure/storedprocedure_structure_eng.png` | Missing local image file | Use the nearby `media/StoredProcedure/storedProcedure_structure.gif` only for inspection; replace the procedure block diagram with a concise text structure description. |
| `14_utilities_operation_tools.md` | `Manuals/Altibase_trunk/eng/Utilities Manual.md:1107` | `media/Utilities/su_policy_eng.png` | Missing local image file | Actual file is `media/su_policy_eng.png` in these source trees. Prefer the adjacent bullet definitions as text and omit the policy image in attachments. |
| `14_utilities_operation_tools.md` | `Manuals/Altibase_trunk/eng/Utilities Manual.md:1109` | `media/Utilities/si_policy_eng.png` | Missing local image file | Actual file is `media/si_policy_eng.png` in these source trees. Prefer the adjacent bullet definitions as text and omit the policy image in attachments. |
| `14_utilities_operation_tools.md` | `Manuals/Altibase_trunk/eng/Utilities Manual.md:1111` | `media/Utilities/mi_policy_eng.png` | Missing local image file | Actual file is `media/mi_policy_eng.png` in these source trees. Prefer the adjacent bullet definitions as text and omit the policy image in attachments. |
| `14_utilities_operation_tools.md` | `Manuals/Altibase_trunk/eng/Utilities Manual.md:1114` | `media/Utilities/sd_policy_eng.png` | Missing local image file | Actual file is `media/sd_policy_eng.png` in these source trees. Prefer the adjacent bullet definitions as text and omit the policy image in attachments. |

## Cleanup Targets: Windows Absolute Paths and File URIs

| Target attachment(s) | Source trace | Matched source text | Cleanup action |
| --- | --- | --- | --- |
| `19_spatial_nifi_tableau_misc.md` | `3rd Party Guide for Altibase/eng/Tableau User's Guide for Altibase/Tableau User's Guide for Altibase.md:61` | `3. Copy and paste Altibase JDBC driver in C:\\Program Files\\Tableau\\Drivers.` | Retain only as a Tableau Windows driver-directory instruction when needed; do not convert it to a `file://` link or internal local path. |
| `12_c_cli_odbc_precompiler.md` | `Manuals/Altibase_7.1/eng/ODBC User's Manual.md:593` | `FileStream fs = new FileStream("c:\\test.dat", FileMode.Open, FileAccess.Read);` | If the C# BLOB sample is retained, replace `c:\test.dat` with a neutral placeholder such as `<local-test-file>` or explain it as an example input/output file. |
| `12_c_cli_odbc_precompiler.md` | `Manuals/Altibase_7.1/eng/ODBC User's Manual.md:625` | `fs = new FileStream("c:\\test.dat", FileMode.CreateNew, FileAccess.Write);` | If the C# BLOB sample is retained, replace `c:\test.dat` with a neutral placeholder such as `<local-test-file>` or explain it as an example input/output file. |
| `14_utilities_operation_tools.md` | `Manuals/Altibase_7.1/eng/Utilities Manual.md:3937` | `Database File Path C:\altibase_home\dbs\system001.dbf]` | Normalize to an Altibase placeholder such as `$ALTIBASE_HOME/dbs/system001.dbf` if the dump output is summarized. |
| `12_c_cli_odbc_precompiler.md` | `Manuals/Altibase_7.3/eng/ODBC User's Manual.md:590` | `FileStream fs = new FileStream("c:\\test.dat", FileMode.Open, FileAccess.Read);` | If the C# BLOB sample is retained, replace `c:\test.dat` with a neutral placeholder such as `<local-test-file>` or explain it as an example input/output file. |
| `12_c_cli_odbc_precompiler.md` | `Manuals/Altibase_7.3/eng/ODBC User's Manual.md:622` | `fs = new FileStream("c:\\test.dat", FileMode.CreateNew, FileAccess.Write);` | If the C# BLOB sample is retained, replace `c:\test.dat` with a neutral placeholder such as `<local-test-file>` or explain it as an example input/output file. |
| `14_utilities_operation_tools.md` | `Manuals/Altibase_7.3/eng/Utilities Manual.md:3948` | `Database File Path C:\altibase_home\dbs\system001.dbf]` | Normalize to an Altibase placeholder such as `$ALTIBASE_HOME/dbs/system001.dbf` if the dump output is summarized. |
| `12_c_cli_odbc_precompiler.md` | `Manuals/Altibase_trunk/eng/ODBC User's Manual.md:590` | `FileStream fs = new FileStream("c:\\test.dat", FileMode.Open, FileAccess.Read);` | If the C# BLOB sample is retained, replace `c:\test.dat` with a neutral placeholder such as `<local-test-file>` or explain it as an example input/output file. |
| `12_c_cli_odbc_precompiler.md` | `Manuals/Altibase_trunk/eng/ODBC User's Manual.md:622` | `fs = new FileStream("c:\\test.dat", FileMode.CreateNew, FileAccess.Write);` | If the C# BLOB sample is retained, replace `c:\test.dat` with a neutral placeholder such as `<local-test-file>` or explain it as an example input/output file. |
| `14_utilities_operation_tools.md` | `Manuals/Altibase_trunk/eng/Utilities Manual.md:3944` | `Database File Path C:\altibase_home\dbs\system001.dbf]` | Normalize to an Altibase placeholder such as `$ALTIBASE_HOME/dbs/system001.dbf` if the dump output is summarized. |
| `14_utilities_operation_tools.md` | `Manuals/Tools/Altibase_release/eng/dataCompJ User's Manual.md:407` | `C:\dataCompJ> dataCompJ.bat -f dataCompJ_env_file_path` | Use a generic command prompt such as `<dataCompJ_home>` if the Windows batch example is retained. |
| `14_utilities_operation_tools.md` | `Manuals/Tools/Altibase_trunk/eng/dataCompJ User's Manual.md:409` | `C:\dataCompJ> dataCompJ.bat -f dataCompJ_env_file_path` | Use a generic command prompt such as `<dataCompJ_home>` if the Windows batch example is retained. |

## Build Guidance

- Do not carry broken image links into `GPTs/attachments/`. For syntax diagrams, use compact BNF-like text; for process or architecture diagrams, use Mermaid only when relationships matter; for UI screenshots, use procedural text and input/value descriptions.
- For the SQL Reference broken links, the local media files generally exist nearby. Use those files only to understand the diagram, then remove the image dependency in the attachment text.
- For the Utilities policy images, the source prose already names the four policies (`SU`, `SI`, `MI`, `SD`). Attachment text should keep the policy definitions as searchable bullets and omit the screenshots.
- Treat source-local absolute paths under `/Users/...`, `C:\...`, and `file://` as cleanup targets. Replace internal or user-machine paths with placeholders such as `$ALTIBASE_HOME`, `<dataCompJ_home>`, or `<local-test-file>` unless a documented Windows product directory is essential to the user task.
- Known Korean manual absolute-link issues documented in `GPTs/reports/eng_kor_parity.md` remain outside this selected-source scan unless a later fallback job opens those Korean manuals directly. If used, normalize them before customer-facing attachment text is written.

## Verification Commands

Representative commands used:

```bash
python3 - <<'PY'
# Parsed GPTs/reports/source_inventory.md, then scanned selected files for Markdown/HTML images, missing local targets, and drive-root/file URI path text.
PY
find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' | wc -l
rg -n "trunk|C:/|file://" GPTs/attachments || true
```

## Conclusion

`JOB-015` acceptance criteria are satisfied. Cleanup targets are listed for all broken image references and Windows/file-URI path text found in the selected source documents.
