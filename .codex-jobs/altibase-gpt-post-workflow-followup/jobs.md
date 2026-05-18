# Altibase GPT Post-Workflow Follow-Up

- Kind: `docs`
- Status values: `ToDo`, `Progress`, `Done`, `Fail`
- User-run command: `./run-all.sh` from this directory
- Codex workdir: repository root by default, override with `CODEX_WORKDIR=/path`
- Default behavior: continue through all jobs until completion or failure
- Optional single-job mode: `RUN_ONE=1 ./run-all.sh`
- Handoff gate: uncommitted project files stop the workflow before the next job starts
- Commit gate: each successful job must pass review and create a focused commit
- Workflow runtime state under `.codex-jobs/` is not part of per-job commits

## Jobs

| ID | Status | Title | Goal |
| --- | --- | --- | --- |
| `PWF-J001` | `ToDo` | Benchmark evidence lock | Record the latest full benchmark run as the official post-workflow evidence baseline without remediation. |
| `PWF-J002` | `ToDo` | Patch-note closure design | Design the closure approach for active patch-note Missing rows before attachment edits. |
| `PWF-J002A` | `ToDo` | Replacement-grade reference policy | Define the cross-document policy for source replacement, LLM use, coding agents, and test-case generation. |
| `PWF-J003` | `ToDo` | Patch-note closure 7.1 001-010 | Close or justify `SRC-PATCH-PATCH-000001` through `SRC-PATCH-PATCH-000010`. |
| `PWF-J004` | `ToDo` | Patch-note closure 7.1 011-020 | Close or justify `SRC-PATCH-PATCH-000011` through `SRC-PATCH-PATCH-000020`. |
| `PWF-J005` | `ToDo` | Patch-note closure 7.1 021-030 | Close or justify `SRC-PATCH-PATCH-000021` through `SRC-PATCH-PATCH-000030`. |
| `PWF-J006` | `ToDo` | Patch-note closure 7.1 031-040 | Close or justify `SRC-PATCH-PATCH-000031` through `SRC-PATCH-PATCH-000040`. |
| `PWF-J007` | `ToDo` | Patch-note closure 7.1 041-050 | Close or justify `SRC-PATCH-PATCH-000041` through `SRC-PATCH-PATCH-000050`. |
| `PWF-J008` | `ToDo` | Patch-note closure 7.1 051-060 | Close or justify `SRC-PATCH-PATCH-000051` through `SRC-PATCH-PATCH-000060`. |
| `PWF-J009` | `ToDo` | Patch-note closure 7.1 061-070 | Close or justify `SRC-PATCH-PATCH-000061` through `SRC-PATCH-PATCH-000070`. |
| `PWF-J010` | `ToDo` | Patch-note closure 7.1 071-080 | Close or justify `SRC-PATCH-PATCH-000071` through `SRC-PATCH-PATCH-000080`. |
| `PWF-J011` | `ToDo` | Patch-note closure 7.1 081-088 | Close or justify `SRC-PATCH-PATCH-000081` through `SRC-PATCH-PATCH-000088`. |
| `PWF-J012` | `ToDo` | Patch-note closure 7.1 089-096 | Close or justify `SRC-PATCH-PATCH-000089` through `SRC-PATCH-PATCH-000096`. |
| `PWF-J013` | `ToDo` | Patch-note closure 7.3 097-105 | Close or justify `SRC-PATCH-PATCH-000097` through `SRC-PATCH-PATCH-000105`. |
| `PWF-J014` | `ToDo` | Patch-note closure 7.3 106-115 | Close or justify `SRC-PATCH-PATCH-000106` through `SRC-PATCH-PATCH-000115`. |
| `PWF-J015` | `ToDo` | SSL sample replacement gap remediation | Remediate or explicitly justify the sampled SSL/TLS appendix replacement gap before final coverage validation. |
| `PWF-J016` | `ToDo` | Coverage closure validation | Validate source-to-attachment closure and update final audit readiness only when `Missing` and `Retrieval-weak` gates are closed. |
| `PWF-J016A` | `ToDo` | Replacement-grade gap register | Apply the replacement-grade policy across source families and assign cross-document gaps to owner jobs. |
| `PWF-J016B` | `ToDo` | Replacement remediation version release platform | Remediate replacement-grade version, release-note, platform, and patch-note gaps assigned by the gap register. |
| `PWF-J017` | `ToDo` | Protected-topic blocker classification | Classify protected-topic blockers from the latest full benchmark by primary cause. |
| `PWF-J018` | `ToDo` | Protected remediation version-sensitive properties | Fix or justify version-sensitive property-change protected blockers with targeted validation. |
| `PWF-J019` | `ToDo` | Protected remediation security TLS | Fix or justify security/TLS protected blockers with targeted validation. |
| `PWF-J020` | `ToDo` | Protected remediation backup recovery | Fix or justify backup/recovery protected blockers with targeted validation. |
| `PWF-J021` | `ToDo` | Protected remediation destructive SQL | Fix or justify destructive SQL protected blockers with targeted validation. |
| `PWF-J022` | `ToDo` | Protected remediation replication state | Fix or justify replication-state-change protected blockers with targeted validation. |
| `PWF-J023` | `ToDo` | Protected-topic targeted validation | Run or record targeted validation for all protected-topic remediations. |
| `PWF-J024` | `ToDo` | Residual failure classification and domain plan | Classify remaining non-protected failures and define bounded domain remediation waves. |
| `PWF-J025` | `ToDo` | Domain remediation views performance | Remediate classified views/performance/monitoring failures with targeted validation. |
| `PWF-J026` | `ToDo` | Domain remediation SQL data types | Remediate classified SQL/DDL/DML/data type failures with targeted validation. |
| `PWF-J027` | `ToDo` | Domain remediation properties | Remediate classified non-protected property failures with targeted validation. |
| `PWF-J028` | `ToDo` | Domain remediation replication security network | Remediate classified replication/CDC/security/network failures with targeted validation. |
| `PWF-J029` | `ToDo` | Domain remediation errors operations | Remediate classified errors/troubleshooting and operations/admin failures with targeted validation. |
| `PWF-J030` | `ToDo` | Domain remediation tools APIs connectors | Remediate classified tools/APIs/connectors/migration failures with targeted validation. |
| `PWF-J031` | `ToDo` | Answer contract and instruction check | Use instruction-aware targeted checks to separate answer synthesis gaps from attachment gaps. |
| `PWF-J031A` | `ToDo` | LLM developer and test readiness | Validate that the attachment set supports coding-agent implementation work and Altibase test-case generation. |
| `PWF-J032` | `ToDo` | Final readiness gate and rerun | Run final validation and the full live benchmark only after closure and protected-topic gates are clean. |

## Required Inputs

- Follow-up plan: `GPTs/reports/full_coverage_audit/post_workflow_followup_plan_20260518.md`
- Final audit report: `GPTs/reports/full_coverage_audit/final_full_coverage_audit.md`
- Catalog: `GPTs/reports/full_coverage_audit/source_item_catalog.tsv`
- Matrix: `GPTs/reports/full_coverage_audit/source_to_attachment_matrix.tsv`
- Missing register: `GPTs/reports/full_coverage_audit/missing_item_register.md`
- Latest benchmark run: `evals/altibase_answerability/reports/full_benchmark/runs/altibase_answerability_20260518_091947/`

## Expected Workflow Outputs

- Replacement-grade policy: `GPTs/reports/full_coverage_audit/replacement_grade_reference_policy_20260518.md`
- Cross-document replacement gap register: `GPTs/reports/full_coverage_audit/replacement_grade_gap_register_20260518.md`
- Developer/test readiness report: `GPTs/reports/full_coverage_audit/llm_developer_test_readiness_20260518.md`

## Work Order Rationale

The full coverage audit is still blocked by `115` active patch-note `Missing` rows,
while `Retrieval-weak` is already `0`. Before remediation scales out, `PWF-J002A`
sets the replacement-grade policy for every source family: customer answerability,
LLM retrieval, coding-agent implementation, and test-case generation. Patch-note
closure is split into smaller 8-10-row batches to keep exact-token review and failure
recovery practical.

The sampled SSL/TLS replacement gap is remediated before final coverage validation so
the closure report is not immediately stale. `PWF-J016A` then applies the same
replacement-grade policy across all source families, not just the sampled manuals, and
assigns any cross-document gaps to owner jobs. `PWF-J016B` gives version,
release-note, platform, and patch-note gaps a direct remediation owner after the gap
register, so those gaps are not deferred into unrelated protected-topic or domain
jobs. Protected-topic remediation is split by topic because the benchmark reports
distinct blocker classes. Residual domain remediation jobs now exist before the final
rerun gate, and `PWF-J031A` adds a developer/test-generation readiness gate, so
`PWF-J032` should not be the first job that discovers replacement-grade work remains.

## Resume Rules

- `Fail`: stop before starting later jobs.
- Dirty project files: stop before starting or advancing to another job.
- `Progress`: preserve interruption evidence, set the job back to `ToDo`, then rerun only when project files are clean.
- `Done`: skip.
- Nonzero `codex exec` exits leave the job as `Progress` by default; the next manual run stops if project files are dirty, or resets runtime state and retries when clean.
- A job commit that includes `.codex-jobs/` workflow state is treated as `Fail`.

## Acceptance Checklist

- Each job has a matching prompt in `prompts/`.
- Each job has concrete acceptance criteria.
- Each successful job leaves project files clean and advances HEAD with a commit.
- Each job commit excludes `.codex-jobs/` workflow status, logs, runtime prompts, and rollback files.
- Protected-topic remediation jobs must run targeted validation or create an explicit blocker report.
- Domain remediation jobs must run targeted validation or create an explicit not-ready report for remaining failures.
- Replacement-grade gaps must be assigned to owner jobs or explicitly accepted as
  guardrails before final readiness.
- Developer and test-case generation scenarios must pass targeted checks or create an
  explicit not-ready report before final readiness.
- `bash -n run-all.sh` passes.
