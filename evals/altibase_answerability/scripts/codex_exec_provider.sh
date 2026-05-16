#!/usr/bin/env bash
set -euo pipefail

if ! command -v codex >/dev/null 2>&1; then
  printf 'ERROR: codex CLI was not found in PATH.\n' >&2
  exit 127
fi

TMP_DIR="$(mktemp -d "${TMPDIR:-/tmp}/altibase-codex-provider.XXXXXX")"
cleanup() {
  rm -rf "$TMP_DIR"
}
trap cleanup EXIT

PROMPT_FILE="${TMP_DIR}/prompt.txt"
ANSWER_FILE="${TMP_DIR}/answer.txt"
LOG_FILE="${TMP_DIR}/codex.log"

cat >"$PROMPT_FILE"

CODEX_GLOBAL_ARGS=(
  --ask-for-approval never
)

CODEX_ARGS=(
  exec
  --cd "$TMP_DIR"
  --skip-git-repo-check
  --ephemeral
  --ignore-rules
  --sandbox read-only
  --color never
  --output-last-message "$ANSWER_FILE"
)

if [[ -n "${CODEX_EXEC_MODEL:-}" ]]; then
  CODEX_ARGS+=(--model "$CODEX_EXEC_MODEL")
fi

if [[ -n "${CODEX_EXEC_PROFILE:-}" ]]; then
  CODEX_ARGS+=(--profile "$CODEX_EXEC_PROFILE")
fi

if ! (cd "$TMP_DIR" && codex "${CODEX_GLOBAL_ARGS[@]}" "${CODEX_ARGS[@]}" - <"$PROMPT_FILE" >"$LOG_FILE" 2>&1); then
  printf 'ERROR: codex exec provider failed.\n' >&2
  sed -n '1,200p' "$LOG_FILE" >&2
  exit 1
fi

if [[ ! -s "$ANSWER_FILE" ]]; then
  printf 'ERROR: codex exec provider produced no final answer.\n' >&2
  sed -n '1,200p' "$LOG_FILE" >&2
  exit 1
fi

cat "$ANSWER_FILE"
