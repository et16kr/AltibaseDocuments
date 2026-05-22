# AID Corpus Dependency

This repository's source pack, upload package, and answerability eval embed
content **extracted from the adjacent AID corpus**. The AID corpus is a separate
Git repository and is *not* vendored into this repository. This file pins the
exact AID source so the build is reproducible.

## Canonical AID source

| Field | Value |
| --- | --- |
| Repository | `git@github.com:et16kr/AID.git` |
| **Branch** | **`combine`** |
| Pinned commit | `64c0ef35b8015ad7ed9706bc39b495c45dffe28a` (2026-05-17 18:23:47 +0900, "Add GPTs readiness validation report") |
| Local checkout path | `~/AID` (absolute — see "Path coupling" below) |

### Why branch `combine`, not `master`

`combine` is the authoritative AID branch: it carries the **fully-updated
English documentation set** and supersedes `master`. The AID `master` branch is
only a single `init` commit and must **not** be used. Always check out
`combine`.

## Setup in a fresh environment

```bash
git clone git@github.com:et16kr/AID.git ~/AID
cd ~/AID
git checkout combine
git rev-parse HEAD          # expect 64c0ef35b8015ad7ed9706bc39b495c45dffe28a
```

The source-pack and AID-tier tooling reads `~/AID` directly:

- `GPTs/source_pack/scripts/build_source_manifest.py`
- `GPTs/source_pack/scripts/build_source_pack.py`
- `GPTs/source_pack/scripts/validate_aid_tier_manifest.py`

The AID tiering decisions are recorded in `GPTs/reports/aid_tier_manifest.tsv`.

## Path coupling (known limitation)

Over 455 committed references in this repository — `~/AID/...` `source_path`
attributes in the `GPTs/upload_package/` shards, plus `GPTs/source_pack/` and
`GPTs/reports/` manifests and scripts — hardcode the **absolute** path `~/AID`.
The AID checkout must therefore live at exactly `~/AID`. Making these paths
relative (so AID could be a submodule or a configurable location) is a separate
refactor; it is not done here.

## Update protocol

When the AID `combine` branch advances and this repository should pick up the
newer AID content:

1. `git -C ~/AID checkout combine && git -C ~/AID pull`
2. Update the pinned commit in this file.
3. Rebuild and re-validate the source pack
   (`GPTs/source_pack/scripts/build_source_pack.py --write`, then `--check`).
4. Commit the regenerated manifests, shards, and this file together.
