#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/../.." && pwd)"
STAGES_FILE="${STAGES_FILE:-${ROOT_DIR}/review/review_stages.tsv}"
STATUS_FILE="${STATUS_FILE:-${ROOT_DIR}/review/review_stage_status.tsv}"
DESIGN_DOC="${DESIGN_DOC:-${ROOT_DIR}/review/Altibase_GPT_Detailed_Review_Design.md}"
REPORT_DIR="${REPORT_DIR:-${ROOT_DIR}/review/reports}"
CODEX_BIN="${CODEX_BIN:-codex}"
CODEX_SUBCOMMAND="${CODEX_SUBCOMMAND:-exec}"

usage() {
  cat <<'USAGE'
Usage:
  bash review/scripts/run_review_stage.sh list
  bash review/scripts/run_review_stage.sh groups
  bash review/scripts/run_review_stage.sh show <R-ID>
  bash review/scripts/run_review_stage.sh prompt <R-ID>
  bash review/scripts/run_review_stage.sh run <R-ID>
  bash review/scripts/run_review_stage.sh run-all [GROUP]
  bash review/scripts/run_review_stage.sh clear [GROUP]
  bash review/scripts/run_review_stage.sh validate

Environment:
  STAGES_FILE       Review stage TSV. Default: review/review_stages.tsv
  STATUS_FILE       Review stage status TSV. Default: review/review_stage_status.tsv
  DESIGN_DOC        Review design document. Default: review/Altibase_GPT_Detailed_Review_Design.md
  REPORT_DIR        Review report output directory. Default: review/reports
  CODEX_BIN         Codex binary. Default: codex
  CODEX_SUBCOMMAND  Codex subcommand. Default: exec
  DRY_RUN=1         Print the Codex prompt or clear actions instead of running them.
  MAX_STAGES=N      Limit run-all to N stages. Default: 0 means no limit.

Status:
  Stage status is tracked in STATUS_FILE, not inferred from report existence.
  Missing status rows default to ToDo.
USAGE
}

die() {
  echo "error: $*" >&2
  exit 1
}

require_files() {
  [[ -f "$STAGES_FILE" ]] || die "stage file not found: $STAGES_FILE"
  [[ -f "$DESIGN_DOC" ]] || die "design doc not found: $DESIGN_DOC"
}

is_dry_run() {
  [[ "${DRY_RUN:-0}" == "1" ]]
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

valid_stage_status() {
  case "$1" in
    ToDo|Progress|Done|Fail)
      return 0
      ;;
    *)
      return 1
      ;;
  esac
}

stage_status() {
  local id="$1"
  local status=""

  if [[ -f "$STATUS_FILE" ]]; then
    status="$(awk -F'\t' -v id="$id" '
      NR == 1 && $1 == "id" { next }
      $1 == id { print $2; found=1; exit }
    ' "$STATUS_FILE")"
  fi

  if [[ -n "$status" ]]; then
    valid_stage_status "$status" || die "invalid status for $id in $STATUS_FILE: $status"
    printf '%s\n' "$status"
  else
    printf 'ToDo\n'
  fi
}

set_stage_status() {
  local id="$1"
  local status="$2"
  local previous temp sid current

  stage_line "$id" >/dev/null || die "unknown stage: $id"
  valid_stage_status "$status" || die "invalid status: $status"

  previous="$(stage_status "$id")"
  mkdir -p "$(dirname "$STATUS_FILE")"
  temp="$(mktemp "${STATUS_FILE}.tmp.XXXXXX")"

  {
    printf 'id\tstatus\n'
    while IFS= read -r sid; do
      [[ -z "$sid" ]] && continue
      if [[ "$sid" == "$id" ]]; then
        current="$status"
      else
        current="$(stage_status "$sid")"
      fi
      printf '%s\t%s\n' "$sid" "$current"
    done < <(stage_ids)
  } > "$temp"

  mv "$temp" "$STATUS_FILE"
  if [[ "$previous" != "$status" ]]; then
    printf "%s: %s -> %s\n" "$id" "$previous" "$status"
  else
    printf "%s: %s\n" "$id" "$status"
  fi
}

stage_output_path() {
  local id="$1"
  local output

  output="$(stage_field "$id" 6)"
  [[ -n "$output" ]] || die "missing output for $id"

  if [[ "$output" == /* ]]; then
    printf '%s\n' "$output"
  else
    printf '%s/%s\n' "$ROOT_DIR" "$output"
  fi
}

list_stages() {
  require_files
  local line id group title output status
  while IFS=$'\t' read -r id group title attachments source_hints output focus acceptance; do
    [[ "$id" == "id" || "$id" == \#* || -z "$id" ]] && continue
    status="$(stage_status "$id")"
    printf "%-4s %-16s %-8s %s\n" "$id" "$group" "$status" "$title"
  done < "$STAGES_FILE"
}

list_groups() {
  require_files
  awk -F'\t' '
    NR == 1 || $0 ~ /^#/ { next }
    !seen[$2]++ { print $2 }
  ' "$STAGES_FILE"
}

show_stage() {
  local id="$1"
  local group title attachments source_hints output focus acceptance status report_file report_state
  group="$(stage_field "$id" 2)" || die "unknown stage: $id"
  title="$(stage_field "$id" 3)"
  attachments="$(stage_field "$id" 4)"
  source_hints="$(stage_field "$id" 5)"
  output="$(stage_field "$id" 6)"
  focus="$(stage_field "$id" 7)"
  acceptance="$(stage_field "$id" 8)"
  status="$(stage_status "$id")"
  report_file="$(stage_output_path "$id")"
  if [[ -f "$report_file" ]]; then
    report_state="present"
  else
    report_state="missing"
  fi

  cat <<EOF
ID:          $id
Group:       $group
Status:      $status
Title:       $title
Attachments: $attachments
Sources:     $source_hints
Output:      $output
Report File: $report_state
Focus:       $focus
Acceptance:  $acceptance
EOF
}

build_prompt() {
  local id="$1"
  local group title attachments source_hints output focus acceptance
  group="$(stage_field "$id" 2)" || die "unknown stage: $id"
  title="$(stage_field "$id" 3)"
  attachments="$(stage_field "$id" 4)"
  source_hints="$(stage_field "$id" 5)"
  output="$(stage_field "$id" 6)"
  focus="$(stage_field "$id" 7)"
  acceptance="$(stage_field "$id" 8)"

  cat <<EOF
You are Codex working in ${ROOT_DIR}.

Run a read-only detailed review stage for the Altibase GPTs attachment project.

Stage ID: ${id}
Group: ${group}
Title: ${title}

Primary rule:
- Do not edit files under GPTs/attachments/.
- Do not modify source manuals.
- You may write exactly one review report: ${output}
- Create the report directory if needed.

Project objective:
- The 20 Markdown attachments under GPTs/attachments/ will be uploaded to GPTs as the Altibase knowledge set.
- The GPT must answer about Altibase 7.1, 7.3, and 8.1.
- Keep ordinary Oracle-overlapping DML brief.
- Prioritize Altibase-specific DDL, storage, properties, data dictionary, operations, troubleshooting, structure, replication, HA, performance, security, and tool behavior.
- Source precedence: Korean Altibase manuals are the authoritative latest manual source. If English and Korean manuals differ, use the Korean manual as the technical basis and report the English-source drift. Final attachment prose should still be normalized into English.
- Preserve literal SQL object names, SQL keywords, function names, error codes, property names, commands, paths, API names, connector names, and version labels.

Read first:
- review/Altibase_GPT_Detailed_Review_Design.md
- GPTs/Altibase_GPT_Document_Selection.md
- GPTs/Altibase_GPT_Attachment_Build_Workplan.md
- GPTs/attachments/README.md

Stage attachments:
- ${attachments}

Supporting source/report hints:
- ${source_hints}

Review focus:
- ${focus}

Acceptance:
- ${acceptance}

Expected report:
- Write ${output}
- Use the report format from review/Altibase_GPT_Detailed_Review_Design.md.
- Start findings with Blocker and High issues first.
- Include file and line references where practical.
- If you find no issues, say so clearly and include residual risks or unverified areas.
- Keep recommendations actionable and scoped to the relevant attachment files.

Before finishing, run lightweight validation commands relevant to this stage where practical, such as rg or find commands. Do not run broad destructive commands and do not make attachment changes.
EOF
}

run_stage() {
  local id="$1"
  local prompt output_path marker rc
  stage_line "$id" >/dev/null || die "unknown stage: $id"
  mkdir -p "$REPORT_DIR"
  prompt="$(build_prompt "$id")"

  if is_dry_run; then
    printf '%s\n' "$prompt"
    return 0
  fi

  command -v "$CODEX_BIN" >/dev/null 2>&1 || die "codex binary not found: $CODEX_BIN"
  output_path="$(stage_output_path "$id")"
  marker="$(mktemp)"
  set_stage_status "$id" Progress

  set +e
  (cd "$ROOT_DIR" && "$CODEX_BIN" "$CODEX_SUBCOMMAND" "$prompt" </dev/null)
  rc=$?
  set -e

  if [[ "$rc" -eq 0 && -s "$output_path" && "$output_path" -nt "$marker" ]]; then
    rm -f "$marker"
    set_stage_status "$id" Done
    return 0
  fi

  rm -f "$marker"
  set_stage_status "$id" Fail
  if [[ "$rc" -eq 0 ]]; then
    echo "error: expected non-empty fresh report was not created: $output_path" >&2
    return 1
  fi
  return "$rc"
}

run_all() {
  local group_filter="${1:-}"
  local max="${MAX_STAGES:-0}"
  local count=0
  local id
  while IFS= read -r id; do
    [[ -z "$id" ]] && continue
    run_stage "$id"
    count=$((count + 1))
    if [[ "$max" != "0" && "$count" -ge "$max" ]]; then
      break
    fi
  done < <(stage_ids "$group_filter")
}

clear_reports() {
  local group_filter="${1:-}"
  local deleted=0
  local missing=0
  local id path

  require_files
  while IFS= read -r id; do
    [[ -z "$id" ]] && continue
    path="$(stage_output_path "$id")"

    if [[ -f "$path" ]]; then
      if is_dry_run; then
        printf "would delete %s\n" "$path"
      else
        rm -- "$path"
        printf "deleted %s\n" "$path"
      fi
      deleted=$((deleted + 1))
    else
      printf "no report %s (%s)\n" "$id" "$path"
      missing=$((missing + 1))
    fi

    if is_dry_run; then
      printf "would set %s status to ToDo\n" "$id"
    else
      set_stage_status "$id" ToDo
    fi
  done < <(stage_ids "$group_filter")

  if is_dry_run; then
    printf "dry run: %d report(s) would be deleted; %d report(s) already absent.\n" "$deleted" "$missing"
  else
    printf "clear complete: %d report(s) deleted; %d report(s) already absent; statuses set to ToDo.\n" "$deleted" "$missing"
  fi
}

validate() {
  require_files
  local missing=0
  local id output

  echo "Stage definitions:"
  list_stages

  echo
  echo "Attachment count excluding README:"
  find "$ROOT_DIR/GPTs/attachments" -maxdepth 1 -type f -name '*.md' ! -name 'README.md' | wc -l

  echo
  echo "Residual image references in attachments:"
  rg -n '!\[|<img|\.png|\.jpg|\.jpeg|\.gif|\.svg|Images/|image::' "$ROOT_DIR/GPTs/attachments" || true

  echo
  echo "Forbidden customer-facing strings in attachments:"
  rg -n 'trunk|C:/|file://' "$ROOT_DIR/GPTs/attachments" || true

  while IFS= read -r id; do
    output="$(stage_field "$id" 6)"
    if [[ -z "$output" ]]; then
      echo "missing output for $id" >&2
      missing=1
    fi
  done < <(stage_ids)

  [[ "$missing" == "0" ]] || exit 1
}

main() {
  local cmd="${1:-}"
  case "$cmd" in
    list)
      list_stages
      ;;
    groups)
      list_groups
      ;;
    show)
      [[ $# -eq 2 ]] || die "show requires a stage id"
      show_stage "$2"
      ;;
    prompt)
      [[ $# -eq 2 ]] || die "prompt requires a stage id"
      build_prompt "$2"
      ;;
    run)
      [[ $# -eq 2 ]] || die "run requires a stage id"
      run_stage "$2"
      ;;
    run-all)
      [[ $# -le 2 ]] || die "run-all accepts at most one group"
      run_all "${2:-}"
      ;;
    clear)
      [[ $# -le 2 ]] || die "clear accepts at most one group"
      clear_reports "${2:-}"
      ;;
    validate)
      validate
      ;;
    -h|--help|help|"")
      usage
      ;;
    *)
      usage
      die "unknown command: $cmd"
      ;;
  esac
}

main "$@"
