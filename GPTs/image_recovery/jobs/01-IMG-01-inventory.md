# Job 01 — IMG-01 Image inventory

You are an autonomous coding agent executing ONE job of a multi-job plan. Do the
work end to end, verify it, and report the result exactly as specified.

## Context

- Working directory is the repository root (`/home/et16/AltibaseDocuments`).
- Spec: `GPTs/reports/image_content_recovery_spec_20260522.md` — Phase 0.
- Scope decision D3: this job covers the **`Manuals/`** tree only.

## Task

Build a complete inventory of every Markdown image reference in `Manuals/`.

1. Find every image reference — both `![alt](path)` Markdown syntax and
   `<img src="path">` HTML syntax — in every `.md` file under `Manuals/`.
2. Write `GPTs/image_recovery/image_inventory.tsv`, one row per reference, with
   a header line and these tab-separated columns:
   - `ref_id` — a stable unique id (e.g. zero-padded sequence).
   - `source_md` — repo-relative path of the Markdown file.
   - `line_no` — line number of the reference.
   - `image_path_raw` — the path exactly as written in the reference.
   - `image_path_resolved` — repo-relative path of the image file the
     reference resolves to (resolve `media/...` against the `.md` file's
     directory); empty if the file does not exist.
   - `basename` — image file basename.
   - `heading_chain` — the chain of enclosing Markdown headings, ` > `-joined.
   - `context` — the surrounding text needed to classify the image later: at
     least 12 lines before and 12 lines after the reference, with newlines
     escaped as `\n` so the row stays single-line.
3. Do not convert, classify, or modify anything — this job only inventories.

## Constraints (non-negotiable)

- Read-only on `Manuals/`. Do NOT modify any original document.
- Do NOT modify `GPTs/source_pack/`, `GPTs/upload_package/`, or build scripts.
- Do not run `run-all.sh` or other jobs' files.

## Acceptance checks

```bash
test -s GPTs/image_recovery/image_inventory.tsv
# The crude grep below is a LOWER BOUND on image references in Manuals/:
refs=$(grep -rhoE '!\[[^]]*\]\([^)]*\)|<img [^>]*src=' Manuals --include='*.md' | wc -l)
rows=$(( $(grep -c . GPTs/image_recovery/image_inventory.tsv) - 1 ))
echo "refs=$refs rows=$rows"   # rows must be >= refs
git diff --check
```

For PASS: the inventory covers 100% of image references in `Manuals/`, every
row has all columns populated (`image_path_resolved` may be empty only when the
image file genuinely does not exist), and the TSV is well-formed. The grep above
is only a lower bound — reference-style (`![alt][id]`) or multi-line forms may
add rows — so `rows` must be **>= `refs`**, and you must additionally confirm
every grep match is represented in the inventory.

## Completion protocol

As your final action:

- Ensure `GPTs/image_recovery/state/` exists.
- If the acceptance checks passed, write `GPTs/image_recovery/state/01.result`
  with first line `PASS` and a short summary (total references, distinct image
  files, count of references whose image file is missing).
- Otherwise write the same file with first line `FAIL: <one-line reason>`.
