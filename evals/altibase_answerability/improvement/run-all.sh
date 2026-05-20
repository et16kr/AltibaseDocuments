#!/usr/bin/env bash
# =============================================================================
# run-all.sh — Orchestrator for the Altibase answerability test-harness
#              improvement jobs.
#
# Each job is executed by the Claude CLI (opus, xhigh effort) as one autonomous
# step. Jobs run in the order listed in jobs.tsv, first to last.
#
#   ./run-all.sh            run from the first non-Done job to the last
#   ./run-all.sh status     print the job status table and exit
#   ./run-all.sh reset ID   reset one job (e.g. 03) back to ToDo
#   ./run-all.sh reset all  reset every job back to ToDo
#
# Behaviour:
#   - Each job has a status: ToDo | Progress | Done | Fail.
#   - A job is Done only when its Claude run writes a PASS result file.
#   - On the first non-Done job that does not reach Done, the script STOPS
#     with a non-zero exit code.
#   - Re-running the script skips Done jobs and retries the first non-Done job,
#     so it is safe to re-run after any interruption (token limit, crash, etc.).
#
# Env overrides:
#   CLAUDE_MODEL           default: opus
#   CLAUDE_EFFORT          default: xhigh
#   CLAUDE_PERMISSION_MODE default: bypassPermissions
#   MAX_BUDGET_USD         optional per-job spend cap (passed to --max-budget-usd)
#   SKIP_PREFLIGHT         set to 1 to skip the harness self-test preflight
#   COMMIT_EACH_JOB        set to 1 to git-commit a checkpoint after each Done job
# =============================================================================
set -uo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$HERE/../../.." && pwd)"
JOBS_TSV="$HERE/jobs.tsv"
JOBS_DIR="$HERE/jobs"
STATE_DIR="$HERE/state"
LOG_DIR="$HERE/logs"
LOCK="$STATE_DIR/.lock"

CLAUDE_MODEL="${CLAUDE_MODEL:-opus}"
CLAUDE_EFFORT="${CLAUDE_EFFORT:-xhigh}"
CLAUDE_PERMISSION_MODE="${CLAUDE_PERMISSION_MODE:-bypassPermissions}"

mkdir -p "$STATE_DIR" "$LOG_DIR"

# ---- helpers ---------------------------------------------------------------

status_of() {  # $1 = job id
  local f="$STATE_DIR/$1.status"
  if [[ -f "$f" ]]; then cat "$f"; else echo "ToDo"; fi
}

set_status() {  # $1 = job id, $2 = status word
  printf '%s\n' "$2" > "$STATE_DIR/$1.status"
}

print_table() {
  echo "------------------------------------------------------------------"
  echo " Altibase test-harness improvement jobs"
  echo "------------------------------------------------------------------"
  while IFS=$'\t' read -r id title prompt || [[ -n "$id" ]]; do
    [[ -z "$id" || "$id" == \#* ]] && continue
    printf '  [ %-8s ]  %s  %s\n' "$(status_of "$id")" "$id" "$title"
  done < "$JOBS_TSV"
  echo "------------------------------------------------------------------"
}

acquire_lock() {
  if [[ -f "$LOCK" ]]; then
    local pid; pid="$(cat "$LOCK" 2>/dev/null || true)"
    if [[ -n "$pid" ]] && kill -0 "$pid" 2>/dev/null; then
      echo "ERROR: run-all.sh is already running (pid $pid)." >&2
      exit 1
    fi
    echo "(clearing stale lock from pid ${pid:-unknown})"
  fi
  echo $$ > "$LOCK"
  trap 'rm -f "$LOCK"' EXIT INT TERM
}

preflight() {
  # Verify the harness is not already broken before running / resuming jobs.
  echo "Preflight: harness self-tests ..."
  ( cd "$REPO_ROOT" && python3 evals/altibase_answerability/scripts/answer_runner.py --self-test ) || return 1
  ( cd "$REPO_ROOT" && python3 evals/altibase_answerability/scripts/judge_report.py --self-test ) || return 1
  echo "Preflight: OK"
  return 0
}

# ---- subcommands -----------------------------------------------------------

case "${1:-run}" in
  status)
    print_table
    exit 0
    ;;
  reset)
    target="${2:-}"
    if [[ "$target" == "all" ]]; then
      rm -f "$STATE_DIR"/*.status "$STATE_DIR"/*.result
      echo "All jobs reset to ToDo."
    elif [[ -n "$target" ]]; then
      rm -f "$STATE_DIR/$target.status" "$STATE_DIR/$target.result"
      echo "Job $target reset to ToDo."
    else
      echo "usage: ./run-all.sh reset <job-id|all>" >&2
      exit 1
    fi
    exit 0
    ;;
  run)
    ;;
  *)
    echo "usage: ./run-all.sh [run|status|reset <job-id|all>]" >&2
    exit 1
    ;;
esac

# ---- preflight -------------------------------------------------------------

if ! command -v claude >/dev/null 2>&1; then
  echo "ERROR: 'claude' CLI not found on PATH." >&2
  exit 1
fi
if [[ ! -f "$JOBS_TSV" ]]; then
  echo "ERROR: jobs manifest not found: $JOBS_TSV" >&2
  exit 1
fi

acquire_lock

if [[ "${SKIP_PREFLIGHT:-0}" != "1" ]]; then
  if ! preflight; then
    echo >&2
    echo "ERROR: preflight self-tests failed — the harness is in a broken state." >&2
    echo "Fix the cause (a previous job may have left it broken), then re-run." >&2
    echo "Set SKIP_PREFLIGHT=1 to bypass this check." >&2
    exit 1
  fi
fi

echo
echo "Model=$CLAUDE_MODEL  Effort=$CLAUDE_EFFORT  Permission=$CLAUDE_PERMISSION_MODE"
print_table
echo

# ---- main loop -------------------------------------------------------------

while IFS=$'\t' read -r id title prompt || [[ -n "$id" ]]; do
  [[ -z "$id" || "$id" == \#* ]] && continue

  st="$(status_of "$id")"
  if [[ "$st" == "Done" ]]; then
    echo ">> $id  $title  :  Done (skip)"
    continue
  fi

  prompt_file="$JOBS_DIR/$prompt"
  if [[ ! -f "$prompt_file" ]]; then
    echo "ERROR: missing prompt file for $id: $prompt_file" >&2
    set_status "$id" Fail
    exit 1
  fi

  result_file="$STATE_DIR/$id.result"
  log_file="$LOG_DIR/$id.$(date +%Y%m%d_%H%M%S).log"
  rm -f "$result_file"
  set_status "$id" Progress

  echo
  echo "=================================================================="
  echo ">> RUN  $id  $title   (was: $st)"
  echo "   prompt: $prompt_file"
  echo "   log:    $log_file"
  echo "   started: $(date '+%Y-%m-%d %H:%M:%S')"
  echo "=================================================================="

  budget_args=()
  if [[ -n "${MAX_BUDGET_USD:-}" ]]; then
    budget_args+=(--max-budget-usd "$MAX_BUDGET_USD")
  fi

  cd "$REPO_ROOT"
  claude -p \
    --model "$CLAUDE_MODEL" \
    --effort "$CLAUDE_EFFORT" \
    --permission-mode "$CLAUDE_PERMISSION_MODE" \
    "${budget_args[@]}" \
    < "$prompt_file" 2>&1 | tee "$log_file"
  rc=${PIPESTATUS[0]}
  cd "$HERE"

  echo
  echo "   finished: $(date '+%Y-%m-%d %H:%M:%S')   (claude exit code: $rc)"

  if [[ -f "$result_file" ]] && head -n1 "$result_file" | grep -q '^PASS'; then
    set_status "$id" Done
    echo ">> $id  :  Done"
    if [[ "${COMMIT_EACH_JOB:-0}" == "1" ]]; then
      if ( cd "$REPO_ROOT" && git add -A \
             && git commit -q -m "test-harness improvement: job $id ($title)" \
                  -m "Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>" ); then
        echo "   checkpoint committed for $id"
      else
        echo "   (no changes to commit for $id)"
      fi
    fi
  else
    set_status "$id" Fail
    echo
    echo "!! $id  :  FAILED"
    if [[ -f "$result_file" ]]; then
      echo "   reason: $(head -n1 "$result_file")"
    elif [[ $rc -ne 0 ]]; then
      echo "   reason: claude exited with code $rc and wrote no PASS result"
      echo "           (possible token/usage limit or crash — safe to re-run)"
    else
      echo "   reason: job produced no PASS result file"
    fi
    echo "   log:    $log_file"
    echo
    echo "   Fix the cause if needed, then re-run ./run-all.sh to retry from $id."
    echo
    print_table
    exit 1
  fi
done < "$JOBS_TSV"

echo
echo "=================================================================="
echo " ALL JOBS DONE"
echo "=================================================================="
print_table
