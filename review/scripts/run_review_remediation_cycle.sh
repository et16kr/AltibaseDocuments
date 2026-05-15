#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/../.." && pwd)"
STAGES_FILE="${STAGES_FILE:-${ROOT_DIR}/review/review_stages.tsv}"
REVIEW_RUNNER="${REVIEW_RUNNER:-${ROOT_DIR}/review/scripts/run_review_stage.sh}"
CYCLE_STATUS_FILE="${CYCLE_STATUS_FILE:-${ROOT_DIR}/review/review_remediation_cycle_status.tsv}"
REVIEW_STATUS_FILE="${REVIEW_STATUS_FILE:-${ROOT_DIR}/review/review_stage_status.tsv}"
FAILURE_LOG="${FAILURE_LOG:-${ROOT_DIR}/review/remediation_failure_log.md}"
CODEX_BIN="${CODEX_BIN:-codex}"
CODEX_SUBCOMMAND="${CODEX_SUBCOMMAND:-exec}"
MAX_RETRIES="${MAX_RETRIES:-2}"
DRY_RUN="${DRY_RUN:-0}"
FORCE="${FORCE:-0}"

VALID_STATUSES="ToDo Reviewing Remediating ReReviewing Done Fail"

usage() {
  cat <<'USAGE'
Usage:
  bash review/scripts/run_review_remediation_cycle.sh status
  bash review/scripts/run_review_remediation_cycle.sh run <R-ID>
  bash review/scripts/run_review_remediation_cycle.sh run-all [GROUP]
  bash review/scripts/run_review_remediation_cycle.sh reset [R-ID|GROUP|all]
  bash review/scripts/run_review_remediation_cycle.sh prompt <R-ID>

Environment:
  MAX_RETRIES=N      Remediation/re-review attempts per stage. Default: 2.
  DRY_RUN=1          Print planned actions without running Codex or changing status.
  FORCE=1            Allow rerunning Done/Fail stages explicitly.
  CODEX_BIN          Codex binary. Default: codex.
  CODEX_SUBCOMMAND   Codex subcommand. Default: exec.

The workflow is stage-granular:
review -> remediate if needed -> validate -> re-review -> commit -> next stage.
USAGE
}

die() {
  echo "error: $*" >&2
  exit 1
}

is_dry_run() {
  [[ "$DRY_RUN" == "1" ]]
}

require_files() {
  [[ -f "$STAGES_FILE" ]] || die "stage file not found: $STAGES_FILE"
  [[ -x "$REVIEW_RUNNER" || -f "$REVIEW_RUNNER" ]] || die "review runner not found: $REVIEW_RUNNER"
}

is_valid_status() {
  case " $VALID_STATUSES " in
    *" $1 "*) return 0 ;;
    *) return 1 ;;
  esac
}

stage_line() {
  local id="$1"
  require_files
  awk -F'\t' -v id="$id" '
    NR == 1 || $0 ~ /^#/ { next }
    $1 == id { print; found=1 }
    END { if (!found) exit 1 }
  ' "$STAGES_FILE"
}

stage_field() {
  local id="$1"
  local field_index="$2"
  stage_line "$id" | awk -F'\t' -v field_index="$field_index" '{ print $field_index }'
}

stage_ids() {
  local group_filter="${1:-}"
  require_files
  awk -F'\t' -v group_filter="$group_filter" '
    NR == 1 || $0 ~ /^#/ { next }
    group_filter == "" || $2 == group_filter { print $1 }
  ' "$STAGES_FILE"
}

stage_title() {
  stage_field "$1" 3
}

stage_group() {
  stage_field "$1" 2
}

stage_output_rel() {
  stage_field "$1" 6
}

stage_output_abs() {
  local output
  output="$(stage_output_rel "$1")"
  if [[ "$output" == /* ]]; then
    printf '%s\n' "$output"
  else
    printf '%s/%s\n' "$ROOT_DIR" "$output"
  fi
}

cycle_status() {
  local id="$1"
  local status=""
  if [[ -f "$CYCLE_STATUS_FILE" ]]; then
    status="$(awk -F'\t' -v id="$id" '
      NR == 1 && $1 == "id" { next }
      $1 == id { print $2; found=1; exit }
    ' "$CYCLE_STATUS_FILE")"
  fi
  if [[ -z "$status" ]]; then
    status="ToDo"
  fi
  is_valid_status "$status" || die "invalid cycle status for $id: $status"
  printf '%s\n' "$status"
}

set_cycle_status() {
  local id="$1"
  local status="$2"
  local temp sid current previous
  stage_line "$id" >/dev/null || die "unknown stage: $id"
  is_valid_status "$status" || die "invalid cycle status: $status"
  previous="$(cycle_status "$id")"
  if is_dry_run; then
    echo "[dry-run] $id: $previous -> $status"
    return 0
  fi
  mkdir -p "$(dirname "$CYCLE_STATUS_FILE")"
  temp="$(mktemp "${CYCLE_STATUS_FILE}.tmp.XXXXXX")"
  {
    printf 'id\tstatus\n'
    while IFS= read -r sid; do
      [[ -z "$sid" ]] && continue
      if [[ "$sid" == "$id" ]]; then
        current="$status"
      else
        current="$(cycle_status "$sid")"
      fi
      printf '%s\t%s\n' "$sid" "$current"
    done < <(stage_ids)
  } > "$temp"
  mv "$temp" "$CYCLE_STATUS_FILE"
  if [[ "$previous" != "$status" ]]; then
    echo "$id: $previous -> $status"
  else
    echo "$id: $status"
  fi
}

reset_cycle_status() {
  local target="${1:-all}"
  local id group
  if [[ "$target" == "all" ]]; then
    while IFS= read -r id; do
      set_cycle_status "$id" ToDo
    done < <(stage_ids)
    return 0
  fi
  if stage_line "$target" >/dev/null 2>&1; then
    set_cycle_status "$target" ToDo
    return 0
  fi
  group="$target"
  while IFS= read -r id; do
    [[ -z "$id" ]] && continue
    set_cycle_status "$id" ToDo
  done < <(stage_ids "$group")
}

review_status() {
  local id="$1"
  if [[ -f "$REVIEW_STATUS_FILE" ]]; then
    awk -F'\t' -v id="$id" '
      NR == 1 && $1 == "id" { next }
      $1 == id { print $2; found=1; exit }
      END { if (!found) print "ToDo" }
    ' "$REVIEW_STATUS_FILE"
  else
    printf 'ToDo\n'
  fi
}

list_status() {
  local id group title cycle review
  require_files
  printf "%-4s %-16s %-12s %-8s %s\n" "ID" "Group" "Cycle" "Review" "Title"
  while IFS= read -r id; do
    group="$(stage_group "$id")"
    title="$(stage_title "$id")"
    cycle="$(cycle_status "$id")"
    review="$(review_status "$id")"
    printf "%-4s %-16s %-12s %-8s %s\n" "$id" "$group" "$cycle" "$review" "$title"
  done < <(stage_ids)
}

project_status_short() {
  git -C "$ROOT_DIR" status --short -- . \
    ":(exclude)$(realpath --relative-to="$ROOT_DIR" "$CYCLE_STATUS_FILE")" \
    ":(exclude)$(realpath --relative-to="$ROOT_DIR" "$REVIEW_STATUS_FILE")"
}

full_status_short() {
  git -C "$ROOT_DIR" status --short
}

require_clean_project_handoff() {
  local status
  if is_dry_run; then
    echo "[dry-run] clean project handoff check skipped"
    return 0
  fi
  status="$(project_status_short)"
  if [[ -n "$status" ]]; then
    echo "error: refusing to start; uncommitted project files are present." >&2
    echo "$status" >&2
    echo "Commit, inspect, or roll back these files before resuming the cycle." >&2
    return 1
  fi
  return 0
}

fail_if_any_stage_failed() {
  local id
  while IFS= read -r id; do
    [[ -z "$id" ]] && continue
    if [[ "$(cycle_status "$id")" == "Fail" ]]; then
      die "$id is Fail; resolve or reset it before continuing"
    fi
  done < <(stage_ids)
}

append_failure() {
  local id="$1"
  local reason="$2"
  if is_dry_run; then
    echo "[dry-run] would append failure: $id - $reason"
    return 0
  fi
  {
    echo
    echo "## $(date '+%Y-%m-%d %H:%M:%S %z') - review remediation cycle"
    echo
    echo "- Stage: \`$id\`"
    echo "- Reason: $reason"
  } >> "$FAILURE_LOG"
}

report_verdict() {
  local report="$1"
  awk -F':' '/^Verdict:/ { gsub(/^[ \t]+|[ \t]+$/, "", $2); print $2; exit }' "$report"
}

report_has_actionable_findings() {
  local report="$1"
  rg -q '^\|[[:space:]]*(Blocker|High|Medium|Low)[[:space:]]*\|' "$report"
}

stage_needs_remediation() {
  local id="$1"
  local report verdict
  report="$(stage_output_abs "$id")"
  [[ -s "$report" ]] || return 0
  verdict="$(report_verdict "$report")"
  if [[ "$verdict" != "Pass" ]]; then
    return 0
  fi
  if report_has_actionable_findings "$report"; then
    return 0
  fi
  return 1
}

run_review() {
  local id="$1"
  if is_dry_run; then
    echo "[dry-run] would run review stage $id"
    return 0
  fi
  bash "$REVIEW_RUNNER" run "$id"
}

build_remediation_prompt() {
  local id="$1"
  local group title attachments sources output focus acceptance report
  group="$(stage_group "$id")"
  title="$(stage_title "$id")"
  attachments="$(stage_field "$id" 4)"
  sources="$(stage_field "$id" 5)"
  output="$(stage_output_rel "$id")"
  focus="$(stage_field "$id" 7)"
  acceptance="$(stage_field "$id" 8)"
  report="$(stage_output_rel "$id")"

  cat <<EOF
You are Codex working in ${ROOT_DIR}.

Remediate exactly one Altibase GPT attachment review stage.

Stage:
- ID: ${id}
- Group: ${group}
- Title: ${title}
- Report: ${report}
- Attachments: ${attachments}
- Source/report hints: ${sources}
- Review focus: ${focus}
- Acceptance: ${acceptance}

Rules:
- Read the stage report first.
- Address actionable \`Blocker\`, \`High\`, \`Medium\`, and \`Low\` findings for this stage only.
- If the report has no actionable finding, make no content changes and exit successfully.
- Keep edits scoped to the listed attachments and directly required supporting reports such as \`GPTs/reports/source_inventory.md\`.
- Do not edit source manuals.
- Korean Altibase manuals, Korean release notes, and Korean technical documents are authoritative when they exist. Use English sources only as secondary extraction/reference material or when no Korean counterpart exists.
- Keep customer-facing files under \`GPTs/attachments/\` in clear English. Do not expose local paths, internal source labels, review job labels, or source inventory mechanics there.
- Preserve literal SQL object names, SQL keywords, function names, error codes, property names, commands, paths, API names, connector names, and version labels.
- Do not commit. The parent runner will re-review and commit the stage after validation passes.

Required work:
1. Inspect \`${report}\`, the listed attachment files, and relevant source hints.
2. Verify each actionable finding against Korean authoritative sources where applicable.
3. Apply the smallest safe fix for the stage.
4. Update source traceability reports only when the fix changes source basis.
5. Run focused validation:
   - \`git diff --check\`
   - \`bash review/scripts/run_review_stage.sh validate\`
   - targeted \`rg\` or \`find\` checks relevant to the changed finding(s)
6. Review the final diff and fix any obvious issue before exiting.

Final response: summarize changed files and validation commands run. Do not ask for approval unless blocked.
EOF
}

run_remediation() {
  local id="$1"
  local prompt
  prompt="$(build_remediation_prompt "$id")"
  if is_dry_run; then
    echo "$prompt"
    echo "[dry-run] would run: $CODEX_BIN $CODEX_SUBCOMMAND <remediation-prompt>"
    return 0
  fi
  command -v "$CODEX_BIN" >/dev/null 2>&1 || die "codex binary not found: $CODEX_BIN"
  (cd "$ROOT_DIR" && "$CODEX_BIN" "$CODEX_SUBCOMMAND" "$prompt" </dev/null)
}

run_common_validation() {
  if is_dry_run; then
    echo "[dry-run] would run common validation"
    return 0
  fi
  (cd "$ROOT_DIR" && git diff --check)
  (cd "$ROOT_DIR" && bash review/scripts/run_review_stage.sh validate)
}

commit_stage() {
  local id="$1"
  local title status subject body
  status="$(full_status_short)"
  if [[ -z "$status" ]]; then
    echo "==> $id produced no changes to commit."
    return 0
  fi
  title="$(stage_title "$id")"
  subject="Review/remediate ${id}: ${title}"
  if [[ "${#subject}" -gt 72 ]]; then
    subject="${subject:0:69}..."
  fi
  body="$(cat <<EOF
Stage: ${id}
Report: $(stage_output_rel "$id")
Verdict: Pass
Validation:
- git diff --check
- bash review/scripts/run_review_stage.sh validate
EOF
)"
  if is_dry_run; then
    echo "[dry-run] would commit:"
    echo "$subject"
    echo "$status"
    return 0
  fi
  (cd "$ROOT_DIR" && git add --all && git diff --cached --check && git commit -m "$subject" -m "$body")
}

complete_stage() {
  local id="$1"
  set_cycle_status "$id" Done
  if ! commit_stage "$id"; then
    set_cycle_status "$id" Fail
    append_failure "$id" "commit failed after stage reached Pass"
    return 1
  fi
}

handle_interrupted_status() {
  local id="$1"
  local status="$2"
  case "$status" in
    Reviewing|Remediating|ReReviewing)
      if [[ "$FORCE" == "1" ]]; then
        set_cycle_status "$id" ToDo
        return 0
      fi
      require_clean_project_handoff || return 1
      echo "==> $id was $status with clean project handoff; resetting to ToDo for retry."
      set_cycle_status "$id" ToDo
      ;;
  esac
}

run_stage_cycle() {
  local id="$1"
  local status attempt
  stage_line "$id" >/dev/null || die "unknown stage: $id"

  status="$(cycle_status "$id")"
  if [[ "$status" == "Done" && "$FORCE" != "1" ]]; then
    echo "==> $id is already Done; skipping."
    return 0
  fi
  if [[ "$status" == "Fail" && "$FORCE" != "1" ]]; then
    die "$id is Fail; inspect it or rerun with FORCE=1"
  fi
  handle_interrupted_status "$id" "$status"
  require_clean_project_handoff

  echo "==> reviewing $id: $(stage_title "$id")"
  set_cycle_status "$id" Reviewing
  if ! run_review "$id"; then
    set_cycle_status "$id" Fail
    append_failure "$id" "initial review command failed"
    return 1
  fi
  if is_dry_run; then
    echo "[dry-run] would inspect $(stage_output_rel "$id") for verdict and actionable findings"
    echo "[dry-run] would remediate, re-review, and commit only if the report requires it"
    return 0
  fi

  if ! stage_needs_remediation "$id"; then
    complete_stage "$id"
    return 0
  fi

  attempt=1
  while [[ "$attempt" -le "$MAX_RETRIES" ]]; do
    echo "==> remediating $id (attempt $attempt/$MAX_RETRIES)"
    set_cycle_status "$id" Remediating
    if ! run_remediation "$id"; then
      set_cycle_status "$id" Fail
      append_failure "$id" "remediation command exited nonzero on attempt $attempt"
      echo "==> $id remediation exited nonzero; marked status as Fail."
      return 1
    fi

    if ! run_common_validation; then
      set_cycle_status "$id" Fail
      append_failure "$id" "common validation failed after remediation attempt $attempt"
      return 1
    fi

    echo "==> re-reviewing $id"
    set_cycle_status "$id" ReReviewing
    if ! run_review "$id"; then
      set_cycle_status "$id" Fail
      append_failure "$id" "re-review command failed on attempt $attempt"
      return 1
    fi

    if ! stage_needs_remediation "$id"; then
      complete_stage "$id"
      return 0
    fi

    attempt=$((attempt + 1))
  done

  set_cycle_status "$id" Fail
  append_failure "$id" "stage still has actionable findings after $MAX_RETRIES remediation attempt(s)"
  return 1
}

next_stage_id() {
  local group_filter="${1:-}"
  local id status
  while IFS= read -r id; do
    [[ -z "$id" ]] && continue
    status="$(cycle_status "$id")"
    if [[ "$status" != "Done" ]]; then
      printf '%s\n' "$id"
      return 0
    fi
  done < <(stage_ids "$group_filter")
  return 1
}

run_all() {
  local group_filter="${1:-}"
  local id
  fail_if_any_stage_failed
  if is_dry_run; then
    while IFS= read -r id; do
      [[ -z "$id" ]] && continue
      if [[ "$(cycle_status "$id")" == "Done" ]]; then
        echo "==> $id is already Done; skipping."
        continue
      fi
      run_stage_cycle "$id"
    done < <(stage_ids "$group_filter")
    echo "[dry-run] completed one planned pass."
    return 0
  fi
  while id="$(next_stage_id "$group_filter")"; do
    run_stage_cycle "$id"
  done
  echo "No remaining stages."
}

main() {
  local command="${1:-}"
  case "$command" in
    status|list)
      list_status
      ;;
    run)
      [[ $# -eq 2 ]] || die "run requires a stage id"
      run_stage_cycle "$2"
      ;;
    run-all)
      [[ $# -le 2 ]] || die "run-all accepts at most one group"
      run_all "${2:-}"
      ;;
    reset)
      [[ $# -le 2 ]] || die "reset accepts at most one target"
      reset_cycle_status "${2:-all}"
      ;;
    prompt)
      [[ $# -eq 2 ]] || die "prompt requires a stage id"
      build_remediation_prompt "$2"
      ;;
    -h|--help|help|"")
      usage
      ;;
    *)
      usage
      die "unknown command: $command"
      ;;
  esac
}

main "$@"
