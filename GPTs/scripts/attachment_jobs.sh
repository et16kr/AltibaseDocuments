#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/../.." && pwd)"
JOBS_DOC="${JOBS_DOC:-${ROOT_DIR}/GPTs/Altibase_GPT_Attachment_Job_List.md}"
ATTACH_DIR="${ATTACH_DIR:-${ROOT_DIR}/GPTs/attachments}"
CODEX_BIN="${CODEX_BIN:-codex}"
CODEX_SUBCOMMAND="${CODEX_SUBCOMMAND:-exec}"
GIT_BIN="${GIT_BIN:-git}"
COMMIT_PATHSPEC="${COMMIT_PATHSPEC:-GPTs}"

usage() {
  cat <<'USAGE'
Usage:
  bash GPTs/scripts/attachment_jobs.sh list
  bash GPTs/scripts/attachment_jobs.sh phase <PHASE>
  bash GPTs/scripts/attachment_jobs.sh ready
  bash GPTs/scripts/attachment_jobs.sh blocked
  bash GPTs/scripts/attachment_jobs.sh next
  bash GPTs/scripts/attachment_jobs.sh show <JOB-ID>
  bash GPTs/scripts/attachment_jobs.sh deps <JOB-ID>
  bash GPTs/scripts/attachment_jobs.sh prompt <JOB-ID>
  bash GPTs/scripts/attachment_jobs.sh start <JOB-ID>
  bash GPTs/scripts/attachment_jobs.sh run <JOB-ID>
  bash GPTs/scripts/attachment_jobs.sh run-all [PHASE]
  bash GPTs/scripts/attachment_jobs.sh finish <JOB-ID> <Review|Done|Fail|Blocked|Skip> [commit message]
  bash GPTs/scripts/attachment_jobs.sh commit <JOB-ID> [commit message]
  bash GPTs/scripts/attachment_jobs.sh history <JOB-ID>
  bash GPTs/scripts/attachment_jobs.sh mark <JOB-ID> <ToDo|InProgress|Review|Done|Fail|Blocked|Skip>
  bash GPTs/scripts/attachment_jobs.sh validate

Environment:
  JOBS_DOC         Override job list path.
  ATTACH_DIR      Override attachments directory.
  CODEX_BIN       Codex binary. Default: codex
  CODEX_SUBCOMMAND Codex subcommand. Default: exec
  GIT_BIN          Git binary. Default: git
  COMMIT_PATHSPEC  Commit scope. Default: GPTs
  FORCE=1          Bypass dependency/status readiness checks for recovery.
  DRY_RUN=1        Preview without changing status, running Codex, staging, or committing.
  MAX_JOBS=N       Stop run-all after N jobs. Default: 0 means no limit.
  STOP_ON_FAIL=1   Stop run-all immediately when a job command fails.
  AUTO_ACCEPT_REVIEW=1
                   Promote Review to Done after a successful run-all job.
  ALLOW_FAILURES=1 Return success from run-all even if one or more jobs failed.
  ALLOW_INCOMPLETE=1
                   Return success when run-all stops with blocked ToDo jobs.
  ALLOW_DIRTY_COMMIT_SCOPE=1
                   Allow start/run to begin when COMMIT_PATHSPEC already has changes.
USAGE
}

die() {
  echo "error: $*" >&2
  exit 1
}

trim_awk='function trim(s){gsub(/^[ \t]+|[ \t]+$/, "", s); return s}'

require_jobs_doc() {
  [[ -f "$JOBS_DOC" ]] || die "job list not found: $JOBS_DOC"
}

is_dry_run() {
  [[ "${DRY_RUN:-0}" == "1" ]]
}

require_git_repo() {
  command -v "$GIT_BIN" >/dev/null 2>&1 || die "git binary not found: $GIT_BIN"
  "$GIT_BIN" -C "$ROOT_DIR" rev-parse --is-inside-work-tree >/dev/null 2>&1 || die "not inside a git work tree: $ROOT_DIR"
}

valid_status() {
  case "$1" in
    ToDo|InProgress|Review|Done|Fail|Blocked|Skip) return 0 ;;
    *) return 1 ;;
  esac
}

job_line() {
  local id="$1"
  require_jobs_doc
  awk -F'|' -v id="$id" "$trim_awk"'
    $0 ~ /^\| JOB-/ {
      job=trim($2)
      if (job == id) {
        print $0
        found=1
      }
    }
    END { if (!found) exit 1 }
  ' "$JOBS_DOC"
}

job_cells() {
  local line="$1"
  printf '%s\n' "$line" | awk -F'|' "$trim_awk"'
    {
      for (i = 2; i < NF; i++) {
        print trim($i)
      }
    }
  '
}

job_status() {
  local id="$1"
  local line
  line="$(job_line "$id")" || return 1
  mapfile -t cells < <(job_cells "$line")
  printf '%s\n' "${cells[2]}"
}

job_deps() {
  local id="$1"
  local line
  line="$(job_line "$id")" || return 1
  mapfile -t cells < <(job_cells "$line")
  printf '%s\n' "${cells[3]}"
}

split_deps() {
  local deps="$1"
  [[ "$deps" == "-" || -z "$deps" ]] && return 0
  printf '%s\n' "$deps" | tr ',' '\n' | awk "$trim_awk"'{ dep=trim($0); if (dep != "") print dep }'
}

deps_satisfied() {
  local id="$1"
  local dep status
  while IFS= read -r dep; do
    [[ -z "$dep" ]] && continue
    status="$(job_status "$dep" 2>/dev/null || true)"
    [[ "$status" == "Done" ]] || return 1
  done < <(split_deps "$(job_deps "$id")")
  return 0
}

job_field() {
  local id="$1"
  local index="$2"
  local line
  line="$(job_line "$id")" || return 1
  mapfile -t cells < <(job_cells "$line")
  printf '%s\n' "${cells[$index]}"
}

deps_summary() {
  local id="$1"
  local deps dep status out
  deps="$(job_deps "$id")"
  if [[ "$deps" == "-" || -z "$deps" ]]; then
    printf '%s\n' "-"
    return 0
  fi
  out=""
  while IFS= read -r dep; do
    [[ -z "$dep" ]] && continue
    status="$(job_status "$dep" 2>/dev/null || printf 'Missing')"
    if [[ -n "$out" ]]; then
      out+=", "
    fi
    out+="${dep}(${status})"
  done < <(split_deps "$deps")
  printf '%s\n' "$out"
}

is_ready() {
  local id="$1"
  [[ "$(job_status "$id")" == "ToDo" ]] || return 1
  deps_satisfied "$id"
}

list_jobs() {
  require_jobs_doc
  awk -F'|' "$trim_awk"'
    $0 ~ /^\| JOB-/ {
      printf "%-8s %-14s %-11s %-30s %s\n", trim($2), trim($3), trim($4), trim($5), trim($6)
    }
  ' "$JOBS_DOC"
}

list_phase() {
  local phase="$1"
  require_jobs_doc
  awk -F'|' -v phase="$phase" "$trim_awk"'
    $0 ~ /^\| JOB-/ {
      if (trim($3) == phase) {
        printf "%-8s %-14s %-11s %-30s %s\n", trim($2), trim($3), trim($4), trim($5), trim($6)
      }
    }
  ' "$JOBS_DOC"
}

ready_jobs() {
  require_jobs_doc
  local id line
  while IFS= read -r line; do
    id="$(printf '%s\n' "$line" | awk -F'|' "$trim_awk"'{ print trim($2) }')"
    if is_ready "$id"; then
      mapfile -t cells < <(job_cells "$line")
      printf "%-8s %-14s %-11s %-30s %s\n" "${cells[0]}" "${cells[1]}" "${cells[2]}" "${cells[3]}" "${cells[4]}"
    fi
  done < <(awk '/^\| JOB-/' "$JOBS_DOC")
}

ready_job_ids() {
  local phase_filter="${1:-}"
  require_jobs_doc
  local id line
  while IFS= read -r line; do
    mapfile -t cells < <(job_cells "$line")
    id="${cells[0]}"
    if [[ -n "$phase_filter" && "${cells[1]}" != "$phase_filter" ]]; then
      continue
    fi
    if is_ready "$id"; then
      printf '%s\n' "$id"
    fi
  done < <(awk '/^\| JOB-/' "$JOBS_DOC")
}

blocked_jobs() {
  require_jobs_doc
  local id line
  while IFS= read -r line; do
    id="$(printf '%s\n' "$line" | awk -F'|' "$trim_awk"'{ print trim($2) }')"
    [[ "$(job_status "$id")" == "ToDo" ]] || continue
    if ! deps_satisfied "$id"; then
      mapfile -t cells < <(job_cells "$line")
      printf "%-8s %-14s %-11s %-70s %s\n" "${cells[0]}" "${cells[1]}" "${cells[2]}" "$(deps_summary "$id")" "${cells[4]}"
    fi
  done < <(awk '/^\| JOB-/' "$JOBS_DOC")
}

todo_count() {
  local phase_filter="${1:-}"
  require_jobs_doc
  awk -F'|' -v phase_filter="$phase_filter" "$trim_awk"'
    $0 ~ /^\| JOB-/ {
      phase=trim($3)
      status=trim($4)
      if (status == "ToDo" && (phase_filter == "" || phase == phase_filter)) {
        count++
      }
    }
    END { print count + 0 }
  ' "$JOBS_DOC"
}

next_job() {
  require_jobs_doc
  local first
  first="$(ready_jobs | head -1 || true)"
  [[ -n "$first" ]] || die "no ready ToDo jobs found"
  printf '%s\n' "$first"
}

show_job() {
  local id="$1"
  local line
  line="$(job_line "$id")" || die "unknown job: $id"
  mapfile -t cells < <(job_cells "$line")
  cat <<EOF
Job ID:      ${cells[0]}
Phase:       ${cells[1]}
Status:      ${cells[2]}
Depends on:  ${cells[3]}
Dep status:  $(deps_summary "${cells[0]}")
Target:      ${cells[4]}
Objective:   ${cells[5]}
Inputs:      ${cells[6]}
Outputs:     ${cells[7]}
Acceptance:  ${cells[8]}
EOF
}

show_deps() {
  local id="$1"
  job_line "$id" >/dev/null || die "unknown job: $id"
  printf '%s\n' "$(deps_summary "$id")"
  if deps_satisfied "$id"; then
    echo "Ready: yes"
  else
    echo "Ready: no"
  fi
}

generate_prompt() {
  local id="$1"
  local line
  line="$(job_line "$id")" || die "unknown job: $id"
  mapfile -t cells < <(job_cells "$line")
  cat <<EOF
You are Codex working in /home/et16/AltibaseDocuments.

Execute this Altibase GPTs attachment job end to end.

Job ID: ${cells[0]}
Phase: ${cells[1]}
Current status: ${cells[2]}
Dependencies: ${cells[3]}
Dependency status: $(deps_summary "${cells[0]}")
Target: ${cells[4]}
Objective: ${cells[5]}
Inputs: ${cells[6]}
Expected outputs: ${cells[7]}
Acceptance criteria: ${cells[8]}

Project rules:
- Prefer editing only files under GPTs/.
- Do not modify original source manuals unless this job explicitly requires it.
- Final files under GPTs/attachments/ must be English canonical and suitable for multilingual GPT answers.
- The GPT should answer in the user's language, but SQL object names, function names, error codes, property names, commands, and file paths must stay literal.
- Customer-facing attachment files must not contain internal source labels such as "trunk".
- For 8.1, use the verified 8.1 source set internally and label it as "Altibase 8.1 verified source" or equivalent customer-safe wording.
- Convert graph, flow, state, architecture, topology, and sequence images to Mermaid when useful.
- Convert SQL syntax diagrams to compact BNF-like text or simple Mermaid.
- Replace UI screenshots with procedural text and input/value descriptions.
- Decompose large tables into searchable item blocks.
- Preserve concise source traceability in work docs, but keep customer-facing attachments clean.

Before finishing:
- Run: find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' | wc -l
- Run: rg -n "trunk|C:/|file://" GPTs/attachments || true
- Summarize changed files, then finish the job through the runner so status and output are committed.
- Use Done when the acceptance criteria are satisfied; use Review only when a human or second-pass review is genuinely needed:
  bash GPTs/scripts/attachment_jobs.sh finish ${cells[0]} Done "short summary"
  bash GPTs/scripts/attachment_jobs.sh finish ${cells[0]} Review "short summary"

If the job cannot be completed, mark it Fail or Blocked with a brief note in your final response.
Use finish for that too, for example:
  bash GPTs/scripts/attachment_jobs.sh finish ${cells[0]} Fail "reason the job could not complete"
EOF
}

commit_message_default() {
  local id="$1"
  local status target
  status="$(job_status "$id")"
  target="$(job_field "$id" 4)"
  target="${target//\`/}"
  printf 'GPTs %s: %s [%s]\n' "$id" "$target" "$status"
}

commit_body() {
  local id="$1"
  local line
  line="$(job_line "$id")" || die "unknown job: $id"
  mapfile -t cells < <(job_cells "$line")
  cat <<EOF
Job ID: ${cells[0]}
Phase: ${cells[1]}
Status: ${cells[2]}
Depends on: ${cells[3]}
Target: ${cells[4]}
Objective: ${cells[5]}
Acceptance: ${cells[8]}

Committed by GPTs/scripts/attachment_jobs.sh.
Scope: ${COMMIT_PATHSPEC}
EOF
}

commit_job() {
  local id="$1"
  shift || true
  job_line "$id" >/dev/null || die "unknown job: $id"

  local message
  if [[ $# -gt 0 ]]; then
    if [[ "$*" == GPTs\ "$id":* ]]; then
      message="$*"
    else
      message="GPTs ${id}: $*"
    fi
  else
    message="$(commit_message_default "$id")"
  fi

  if [[ "${DRY_RUN:-0}" == "1" ]]; then
    echo "[dry-run] ${GIT_BIN} -C ${ROOT_DIR} add -- ${COMMIT_PATHSPEC}"
    echo "[dry-run] ${GIT_BIN} -C ${ROOT_DIR} commit -m ${message@Q} -- ${COMMIT_PATHSPEC}"
    return 0
  fi

  require_git_repo
  "$GIT_BIN" -C "$ROOT_DIR" add -- "$COMMIT_PATHSPEC"

  if "$GIT_BIN" -C "$ROOT_DIR" diff --cached --quiet -- "$COMMIT_PATHSPEC"; then
    echo "No staged changes under ${COMMIT_PATHSPEC}; no commit created for ${id}."
    return 0
  fi

  "$GIT_BIN" -C "$ROOT_DIR" commit -m "$message" -m "$(commit_body "$id")" -- "$COMMIT_PATHSPEC"
}

ensure_clean_commit_scope_before_start() {
  is_dry_run && return 0
  [[ "${FORCE:-0}" == "1" ]] && return 0
  [[ "${ALLOW_DIRTY_COMMIT_SCOPE:-0}" == "1" ]] && return 0

  require_git_repo
  local dirty
  dirty="$("$GIT_BIN" -C "$ROOT_DIR" status --porcelain -- "$COMMIT_PATHSPEC")"
  if [[ -n "$dirty" ]]; then
    printf '%s\n' "$dirty" >&2
    die "uncommitted changes exist under ${COMMIT_PATHSPEC}; finish or commit current work before starting another job. Use ALLOW_DIRTY_COMMIT_SCOPE=1 only for manual recovery."
  fi
}

ensure_startable() {
  local id="$1"
  local status
  status="$(job_status "$id")"

  if [[ "${FORCE:-0}" == "1" ]]; then
    return 0
  fi

  case "$status" in
    ToDo)
      deps_satisfied "$id" && return 0
      show_deps "$id" >&2 || true
      die "job is not ready; dependencies must be Done before starting. Use FORCE=1 only for manual recovery."
      ;;
    InProgress)
      deps_satisfied "$id" && return 0
      show_deps "$id" >&2 || true
      die "job is in progress but dependencies are not Done. Use FORCE=1 only for manual recovery."
      ;;
    *)
      die "start/run requires ToDo or InProgress status; current status is ${status}. Use FORCE=1 only for manual recovery."
      ;;
  esac
}

start_job() {
  local id="$1"
  ensure_startable "$id"

  local status
  status="$(job_status "$id")"
  if [[ "$status" == "InProgress" ]]; then
    echo "${id} is already InProgress."
    return 0
  fi

  if is_dry_run; then
    echo "[dry-run] would mark ${id} InProgress"
    commit_job "$id" "GPTs ${id}: start"
    return 0
  fi

  ensure_clean_commit_scope_before_start
  mark_job "$id" InProgress
  commit_job "$id" "GPTs ${id}: start"
}

run_job() {
  local id="$1"
  ensure_startable "$id"

  if [[ "$(job_status "$id")" == "ToDo" ]]; then
    start_job "$id"
  fi

  local prompt
  prompt="$(generate_prompt "$id")"

  if is_dry_run; then
    echo "[dry-run] would run: ${CODEX_BIN} ${CODEX_SUBCOMMAND} <generated prompt for ${id}>"
    return 0
  fi

  command -v "$CODEX_BIN" >/dev/null 2>&1 || die "Codex binary not found: $CODEX_BIN"
  "$CODEX_BIN" "$CODEX_SUBCOMMAND" "$prompt"
}

run_all_jobs() {
  local phase_filter="${1:-}"
  local max_jobs="${MAX_JOBS:-0}"
  [[ "$max_jobs" =~ ^[0-9]+$ ]] || die "MAX_JOBS must be a non-negative integer"

  local ran=0
  local failures=0
  local id status rc target

  echo "Starting run-all${phase_filter:+ for phase ${phase_filter}}."
  echo "MAX_JOBS=${max_jobs}, AUTO_ACCEPT_REVIEW=${AUTO_ACCEPT_REVIEW:-0}, STOP_ON_FAIL=${STOP_ON_FAIL:-0}, ALLOW_FAILURES=${ALLOW_FAILURES:-0}"

  if is_dry_run; then
    echo "Dry run: no statuses will change, Codex will not run, and no commits will be created."
    mapfile -t ids < <(ready_job_ids "$phase_filter")
    if [[ ${#ids[@]} -eq 0 ]]; then
      echo "No ready ToDo jobs."
      return 0
    fi
    for id in "${ids[@]}"; do
      target="$(job_field "$id" 4)"
      echo "[dry-run] would run ${id}: ${target}"
    done
    return 0
  fi

  while true; do
    mapfile -t ids < <(ready_job_ids "$phase_filter")
    [[ ${#ids[@]} -gt 0 ]] || break

    local progressed=0
    for id in "${ids[@]}"; do
      if [[ "$max_jobs" -gt 0 && "$ran" -ge "$max_jobs" ]]; then
        echo "MAX_JOBS reached after ${ran} job(s)."
        validate
        if [[ "$failures" -gt 0 && "${ALLOW_FAILURES:-0}" != "1" ]]; then
          echo
          echo "run-all observed ${failures} failed or blocked job(s). Set ALLOW_FAILURES=1 only when this is acceptable."
          return 1
        fi
        return 0
      fi

      if ! is_ready "$id"; then
        continue
      fi

      target="$(job_field "$id" 4)"
      echo
      echo "==> run-all starting ${id}: ${target}"

      if run_job "$id"; then
        status="$(job_status "$id")"

        if [[ "$status" == "Review" && "${AUTO_ACCEPT_REVIEW:-0}" == "1" ]]; then
          finish_job "$id" Done "Auto-accepted Review during run-all"
          status="$(job_status "$id")"
        fi

        case "$status" in
          Done|Skip)
            commit_job "$id" "Run-all checkpoint after ${status}"
            echo "==> ${id} finished as ${status}."
            ;;
          Review)
            commit_job "$id" "Run-all checkpoint after Review"
            echo "==> ${id} finished as Review. Dependent jobs will wait until it is marked Done."
            ;;
          Fail|Blocked)
            commit_job "$id" "Run-all checkpoint after ${status}"
            echo "==> ${id} finished as ${status}. Independent ready jobs may continue."
            failures=$((failures + 1))
            ;;
          InProgress|ToDo)
            echo "==> ${id} ended without a terminal status; marking Fail for recovery."
            finish_job "$id" Fail "Codex command ended without finish status during run-all"
            failures=$((failures + 1))
            ;;
          *)
            echo "==> ${id} ended with unexpected status ${status}; marking Fail for recovery."
            finish_job "$id" Fail "Unexpected job status during run-all: ${status}"
            failures=$((failures + 1))
            ;;
        esac
      else
        rc=$?
        echo "==> ${id} command failed with exit code ${rc}."
        status="$(job_status "$id" 2>/dev/null || printf 'Missing')"
        case "$status" in
          InProgress|ToDo)
            finish_job "$id" Fail "Codex command failed during run-all with exit code ${rc}"
            ;;
          Missing)
            echo "==> ${id} is missing from the job list; cannot mark Fail."
            ;;
          *)
            echo "==> ${id} already has status ${status}."
            commit_job "$id" "Run-all checkpoint after command failure [${status}]"
            ;;
        esac
        failures=$((failures + 1))
        if [[ "${STOP_ON_FAIL:-0}" == "1" ]]; then
          validate
          return "$rc"
        fi
      fi

      ran=$((ran + 1))
      progressed=1
    done

    [[ "$progressed" -eq 1 ]] || break
  done

  echo
  echo "run-all stopped after ${ran} job(s); failures observed: ${failures}."
  validate

  local exit_code=0
  if [[ "$failures" -gt 0 && "${ALLOW_FAILURES:-0}" != "1" ]]; then
    echo
    echo "run-all observed ${failures} failed or blocked job(s). Set ALLOW_FAILURES=1 only when this is acceptable."
    exit_code=1
  fi

  local remaining_todo
  remaining_todo="$(todo_count "$phase_filter")"
  if [[ "$remaining_todo" -gt 0 ]]; then
    echo
    echo "No more ready jobs; ${remaining_todo} ToDo job(s) remain blocked by dependencies or review states."
    if [[ "${ALLOW_INCOMPLETE:-0}" != "1" && "$exit_code" -eq 0 ]]; then
      exit_code=2
    fi
  fi
  return "$exit_code"
}

finish_job() {
  local id="$1"
  local status="$2"
  shift 2 || true
  case "$status" in
    Review|Done|Fail|Blocked|Skip) ;;
    *) die "finish status must be one of Review, Done, Fail, Blocked, Skip" ;;
  esac
  job_line "$id" >/dev/null || die "unknown job: $id"

  if is_dry_run; then
    echo "[dry-run] would mark ${id} ${status}"
    if [[ $# -gt 0 ]]; then
      commit_job "$id" "GPTs ${id}: $* [${status}]"
    else
      commit_job "$id"
    fi
    return 0
  fi

  mark_job "$id" "$status"

  if [[ $# -gt 0 ]]; then
    commit_job "$id" "GPTs ${id}: $* [${status}]"
  else
    commit_job "$id"
  fi
}

mark_job() {
  local id="$1"
  local status="$2"
  valid_status "$status" || die "invalid status: $status"
  job_line "$id" >/dev/null || die "unknown job: $id"
  JOB_ID="$id" JOB_STATUS="$status" perl -0pi -e '
    my $id = $ENV{"JOB_ID"};
    my $status = $ENV{"JOB_STATUS"};
    s/^(\|\s*\Q$id\E\s*\|\s*[^|]+\|\s*)[^|]+(\|)/$1$status $2/m;
  ' "$JOBS_DOC"
}

job_history() {
  local id="$1"
  job_line "$id" >/dev/null || die "unknown job: $id"
  command -v "$GIT_BIN" >/dev/null 2>&1 || die "git binary not found: $GIT_BIN"
  "$GIT_BIN" -C "$ROOT_DIR" log --oneline --decorate --grep="$id" -- "$COMMIT_PATHSPEC" || true
}

validate() {
  require_jobs_doc
  echo "Attachment count excluding README:"
  find "$ATTACH_DIR" -maxdepth 1 -type f -name '*.md' ! -name 'README.md' | wc -l
  echo
  echo "Forbidden customer-facing strings in attachments:"
  rg -n "trunk|C:/|file://" "$ATTACH_DIR" || true
  echo
  echo "Job status summary:"
  awk -F'|' "$trim_awk"'
    $0 ~ /^\| JOB-/ {
      count[trim($4)]++
    }
    END {
      for (status in count) {
        printf "%-11s %d\n", status, count[status]
      }
    }
  ' "$JOBS_DOC" | sort
  echo
  echo "Ready ToDo jobs:"
  ready_jobs | wc -l
  echo
  echo "Blocked ToDo jobs:"
  blocked_jobs | wc -l
}

cmd="${1:-}"
case "$cmd" in
  list)
    list_jobs
    ;;
  phase)
    [[ $# -eq 2 ]] || die "phase requires one argument"
    list_phase "$2"
    ;;
  ready)
    ready_jobs
    ;;
  blocked)
    blocked_jobs
    ;;
  next)
    next_job
    ;;
  show)
    [[ $# -eq 2 ]] || die "show requires JOB-ID"
    show_job "$2"
    ;;
  deps)
    [[ $# -eq 2 ]] || die "deps requires JOB-ID"
    show_deps "$2"
    ;;
  prompt)
    [[ $# -eq 2 ]] || die "prompt requires JOB-ID"
    generate_prompt "$2"
    ;;
  start)
    [[ $# -eq 2 ]] || die "start requires JOB-ID"
    start_job "$2"
    ;;
  run)
    [[ $# -eq 2 ]] || die "run requires JOB-ID"
    run_job "$2"
    ;;
  run-all)
    [[ $# -le 2 ]] || die "run-all accepts at most one optional PHASE argument"
    run_all_jobs "${2:-}"
    ;;
  finish)
    [[ $# -ge 3 ]] || die "finish requires JOB-ID and status"
    finish_job "$2" "$3" "${@:4}"
    ;;
  commit)
    [[ $# -ge 2 ]] || die "commit requires JOB-ID"
    commit_job "$2" "${@:3}"
    ;;
  history)
    [[ $# -eq 2 ]] || die "history requires JOB-ID"
    job_history "$2"
    ;;
  mark)
    [[ $# -eq 3 ]] || die "mark requires JOB-ID and status"
    JOB_ID="$2" JOB_STATUS="$3" mark_job "$2" "$3"
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
