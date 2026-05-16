#!/usr/bin/env bash
set -Eeuo pipefail

# User-run script. Default mode continues through all jobs until completion or failure.
# Optional controls:
#   RUN_ONE=1 ./run-all.sh          # stop after one completed ToDo job
#   FAIL_ON_NONZERO=1 ./run-all.sh  # mark nonzero codex exits as terminal Fail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
JOBS_FILE="${JOBS_FILE:-$SCRIPT_DIR/jobs.tsv}"
PROMPT_DIR="${PROMPT_DIR:-$SCRIPT_DIR/prompts}"
LOG_DIR="${LOG_DIR:-$SCRIPT_DIR/logs}"
ROLLBACK_DIR="${ROLLBACK_DIR:-$SCRIPT_DIR/rollbacks}"
RUNTIME_DIR="${RUNTIME_DIR:-$SCRIPT_DIR/.runtime}"
REQUIREMENTS_FILE="${REQUIREMENTS_FILE:-$SCRIPT_DIR/requirements.md}"

CODEX_BIN="${CODEX_BIN:-codex}"
CODEX_SUBCOMMAND="${CODEX_SUBCOMMAND:-exec}"
AUTO_ROLLBACK="${AUTO_ROLLBACK:-1}"
RUN_ONE="${RUN_ONE:-0}"
FAIL_ON_NONZERO="${FAIL_ON_NONZERO:-0}"
REQUIRE_CLEAN_START="${REQUIRE_CLEAN_START:-1}"
REQUIRE_CLEAN_AFTER_JOB="${REQUIRE_CLEAN_AFTER_JOB:-1}"
REQUIRE_COMMIT_AFTER_JOB="${REQUIRE_COMMIT_AFTER_JOB:-1}"

mkdir -p "$LOG_DIR" "$ROLLBACK_DIR" "$RUNTIME_DIR"

die() {
  printf 'ERROR: %s\n' "$*" >&2
  exit 1
}

status_of() {
  awk -F '\t' -v id="$1" 'NR > 1 && $1 == id { print $2; found = 1; exit } END { if (!found) exit 1 }' "$JOBS_FILE"
}

title_of() {
  awk -F '\t' -v id="$1" 'NR > 1 && $1 == id { print $4; found = 1; exit } END { if (!found) exit 1 }' "$JOBS_FILE"
}

set_status() {
  local id="$1"
  local status="$2"
  local tmp
  tmp="$(mktemp)"
  awk -F '\t' -v OFS='\t' -v id="$id" -v status="$status" '
    NR == 1 { print; next }
    $1 == id { $2 = status }
    { print }
  ' "$JOBS_FILE" > "$tmp"
  mv "$tmp" "$JOBS_FILE"
}

first_job_with_status() {
  awk -F '\t' -v status="$1" 'NR > 1 && $2 == status { print $1; exit }' "$JOBS_FILE"
}

job_ids() {
  awk -F '\t' 'NR > 1 && $1 != "" { print $1 }' "$JOBS_FILE"
}

inside_git_repo() {
  git rev-parse --is-inside-work-tree >/dev/null 2>&1
}

git_repo_root() {
  git rev-parse --show-toplevel
}

workflow_rel_path() {
  local root="$1"
  case "$SCRIPT_DIR/" in
    "$root"/*) printf '%s\n' "${SCRIPT_DIR#$root/}" ;;
    *) return 1 ;;
  esac
}

git_head() {
  git rev-parse --verify HEAD 2>/dev/null || printf '%s\n' "__NO_HEAD__"
}

git_dirty_blocking() {
  inside_git_repo || return 1

  local root rel status
  root="$(git_repo_root)"
  rel="$(workflow_rel_path "$root" || true)"
  if [[ "$rel" == ".codex-jobs" || "$rel" == ".codex-jobs/"* ]]; then
    rel=".codex-jobs"
  fi

  if [[ -n "$rel" ]]; then
    status="$(git -C "$root" status --porcelain --untracked-files=all -- . ":(exclude)$rel" ":(exclude)$rel/**")"
  else
    status="$(git -C "$root" status --porcelain --untracked-files=all)"
  fi

  [[ -n "$status" ]]
}

preserve_and_clear_progress() {
  local id="$1"
  local timestamp
  timestamp="$(date +%Y%m%d-%H%M%S)"
  local dir="$ROLLBACK_DIR/$id-$timestamp"
  mkdir -p "$dir"

  if [[ "$AUTO_ROLLBACK" != "1" ]]; then
    die "Job $id is Progress. AUTO_ROLLBACK=0, so resolve it manually and set status to ToDo or Done."
  fi

  if ! inside_git_repo; then
    die "Job $id is Progress, but this is not a git repository. Rollback manually, then set status to ToDo."
  fi

  git status --porcelain > "$dir/status.txt" || true
  git diff > "$dir/unstaged.diff" || true
  git diff --staged > "$dir/staged.diff" || true
  git ls-files -o --exclude-standard > "$dir/untracked.txt" || true

  if git_dirty_blocking; then
    die "Job $id is Progress and uncommitted project files exist. Commit, stash, or inspect them manually before retrying."
  else
    printf 'No uncommitted project files to preserve. Workflow runtime state was left in place.\n' > "$dir/resume.txt"
  fi

  set_status "$id" "ToDo"
  printf 'Reset interrupted job %s to ToDo. Preserved details in %s\n' "$id" "$dir"
}

ensure_clean_before_job() {
  local id="$1"
  if [[ "$REQUIRE_COMMIT_AFTER_JOB" == "1" ]] && ! inside_git_repo; then
    die "Job $id cannot start because this is not a git repository and successful jobs must commit."
  fi
  if [[ "$REQUIRE_CLEAN_START" == "1" ]] && git_dirty_blocking; then
    die "Uncommitted project files exist before starting $id. Commit or stash them before running jobs."
  fi
}

ensure_clean_after_job() {
  local id="$1"
  if [[ "$REQUIRE_CLEAN_AFTER_JOB" == "1" ]] && git_dirty_blocking; then
    set_status "$id" "Fail"
    die "Job $id finished but left uncommitted project files. Commit or clean them, then rerun."
  fi
}

ensure_commit_after_job() {
  local id="$1"
  local before_head="$2"

  if [[ "$REQUIRE_COMMIT_AFTER_JOB" != "1" ]]; then
    return 0
  fi

  if ! inside_git_repo; then
    set_status "$id" "Fail"
    die "Job $id cannot be accepted because this is not a git repository and successful jobs must commit."
  fi

  local after_head
  after_head="$(git_head)"
  if [[ "$after_head" == "$before_head" ]]; then
    set_status "$id" "Fail"
    die "Job $id finished without creating a commit. A successful reviewed job must commit its result."
  fi
}

build_runtime_prompt() {
  local id="$1"
  local prompt_file="$PROMPT_DIR/$id.md"
  local runtime_prompt="$RUNTIME_DIR/$id.prompt.md"

  [[ -f "$prompt_file" ]] || die "Missing prompt file: $prompt_file"

  {
    if [[ -f "$REQUIREMENTS_FILE" ]]; then
      printf '## Workflow Requirements\n\n'
      cat "$REQUIREMENTS_FILE"
      printf '\n\n'
    fi
    cat "$prompt_file"
    printf '\n## Orchestrator Contract\n\n'
    printf -- '- This job id is `%s`.\n' "$id"
    printf -- '- Complete only this job and preserve unrelated user changes.\n'
    printf -- '- Before editing, stop if uncommitted project files exist outside the `.codex-jobs/altibase-gpt-encyclopedia-rebuild/` workflow directory. Status, log, rollback, and runtime files inside that workflow directory are expected orchestration state.\n'
    printf -- '- If the job cannot be completed safely, stop with a clear failure.\n'
    printf -- '- After review and verification pass, create a focused git commit for this job.\n'
    printf -- '- A successful job must leave project files clean and must advance HEAD with a commit.\n'
  } > "$runtime_prompt"

  printf '%s\n' "$runtime_prompt"
}

run_job() {
  local id="$1"
  local title
  title="$(title_of "$id")"
  local runtime_prompt
  runtime_prompt="$(build_runtime_prompt "$id")"
  local log_file="$LOG_DIR/$id.log"

  printf '\n==> %s: %s\n' "$id" "$title"
  ensure_clean_before_job "$id"
  local before_head
  before_head="$(git_head)"
  set_status "$id" "Progress"

  set +e
  "$CODEX_BIN" "$CODEX_SUBCOMMAND" "$(cat "$runtime_prompt")" > "$log_file" 2>&1
  local rc=$?
  set -e

  cat "$log_file"

  if [[ "$rc" -ne 0 ]]; then
    if [[ "$FAIL_ON_NONZERO" == "1" ]]; then
      set_status "$id" "Fail"
      die "Job $id failed. See $log_file"
    fi
    die "Job $id stopped with exit code $rc and remains Progress. Next run preserves interruption evidence, then stops if project files are dirty or resets runtime state and retries when clean. See $log_file"
  fi

  ensure_clean_after_job "$id"
  ensure_commit_after_job "$id" "$before_head"
  set_status "$id" "Done"
  printf 'Done: %s\n' "$id"
}

[[ -f "$JOBS_FILE" ]] || die "Missing jobs file: $JOBS_FILE"

failed_job="$(first_job_with_status Fail || true)"
if [[ -n "$failed_job" ]]; then
  die "Job $failed_job is Fail. Fix it or reset its status before continuing."
fi

while true; do
  progress_job="$(first_job_with_status Progress || true)"
  [[ -n "$progress_job" ]] || break
  preserve_and_clear_progress "$progress_job"
done

if [[ "$REQUIRE_CLEAN_START" == "1" ]] && git_dirty_blocking; then
  die "Uncommitted project files exist. Commit or stash them before running jobs."
fi

for id in $(job_ids); do
  status="$(status_of "$id")"
  case "$status" in
    Done)
      printf 'Skip Done: %s\n' "$id"
      ;;
    ToDo)
      run_job "$id"
      if [[ "$RUN_ONE" == "1" ]]; then
        printf 'RUN_ONE=1, stopping after one completed job.\n'
        exit 0
      fi
      ;;
    Progress)
      die "Unexpected Progress state after rollback handling: $id"
      ;;
    Fail)
      die "Job $id is Fail. Stop."
      ;;
    *)
      die "Unknown status for $id: $status"
      ;;
  esac
done

printf '\nAll jobs completed.\n'
