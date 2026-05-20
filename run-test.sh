#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_ROOT"

usage() {
  cat <<'USAGE'
Usage:
  ./run-test.sh [attachments|source-preserving|coding-agent]

Default:
  ./run-test.sh
    Runs the original attachment-based 270-question full benchmark.
    Live command-provider runs use gpt-5.5 via the Codex CLI unless overridden.

Suites:
  attachments        GPTs/attachments full benchmark (default)
  source-preserving  GPTs/upload_package full benchmark
  coding-agent       Source-preserving coding-agent benchmark

Common examples:
  MODE=dry_run ./run-test.sh source-preserving
  ./run-test.sh source-preserving
  ./run-test.sh coding-agent

Environment overrides:
  MANIFEST, PROFILE, RUN_ID, MODE/ALTIBASE_TEST_MODE, PROVIDER/ALTIBASE_TEST_PROVIDER,
  ALTIBASE_TEST_MODEL, CODEX_EXEC_MODEL, DEFAULT_CODEX_MODEL, LIMIT, QUESTION_ID, RUN_ROOT
USAGE
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

SUITE_RAW="${1:-${ALTIBASE_TEST_SUITE:-${TEST_SUITE:-attachments}}}"
case "$SUITE_RAW" in
  attachments|attachment|full|default)
    TEST_SUITE="attachments"
    DEFAULT_MANIFEST="evals/altibase_answerability/manifests/full_benchmark.json"
    DEFAULT_PROFILE="full"
    ;;
  source-preserving|source_preserving|source|sp)
    TEST_SUITE="source-preserving"
    DEFAULT_MANIFEST="evals/altibase_answerability/manifests/full_benchmark_source_preserving_package.json"
    DEFAULT_PROFILE="full"
    ;;
  coding-agent|coding_agent|agent)
    TEST_SUITE="coding-agent"
    DEFAULT_MANIFEST="evals/altibase_answerability/manifests/coding_agent_source_preserving_package.json"
    DEFAULT_PROFILE="coding_agent"
    ;;
  *)
    printf 'ERROR: unknown test suite: %s\n\n' "$SUITE_RAW" >&2
    usage >&2
    exit 2
    ;;
esac

MANIFEST="${MANIFEST:-$DEFAULT_MANIFEST}"
PROFILE="${PROFILE:-${VALIDATION_PROFILE:-$DEFAULT_PROFILE}}"
POLICY="${POLICY:-evals/altibase_answerability/policy.json}"
SUITE_ID="${TEST_SUITE//-/_}"
RUN_ID="${RUN_ID:-altibase_${SUITE_ID}_$(date +%Y%m%d_%H%M%S)}"
MODE="${ALTIBASE_TEST_MODE:-${MODE:-live}}"
PROVIDER="${ALTIBASE_TEST_PROVIDER:-${PROVIDER:-command}}"
DEFAULT_CODEX_MODEL="${DEFAULT_CODEX_MODEL:-gpt-5.5}"
case "$PROVIDER" in
  command)
    MODEL="${ALTIBASE_TEST_MODEL:-${CODEX_EXEC_MODEL:-${MODEL_NAME:-$DEFAULT_CODEX_MODEL}}}"
    if [[ -n "${ALTIBASE_TEST_MODEL:-}" && -n "${CODEX_EXEC_MODEL:-}" && "$ALTIBASE_TEST_MODEL" != "$CODEX_EXEC_MODEL" ]]; then
      printf 'ERROR: ALTIBASE_TEST_MODEL (%s) and CODEX_EXEC_MODEL (%s) disagree for provider=command.\n' "$ALTIBASE_TEST_MODEL" "$CODEX_EXEC_MODEL" >&2
      printf 'Set only one of them, or set both to the same model.\n' >&2
      exit 2
    fi
    export CODEX_EXEC_MODEL="$MODEL"
    ;;
  openai|openai_responses)
    MODEL="${ALTIBASE_TEST_MODEL:-${OPENAI_MODEL:-${MODEL_NAME:-}}}"
    ;;
  *)
    MODEL="${ALTIBASE_TEST_MODEL:-${MODEL_NAME:-}}"
    ;;
esac
PROVIDER_COMMAND="${PROVIDER_COMMAND:-evals/altibase_answerability/scripts/codex_exec_provider.sh}"
CONTEXT_MODE="${CONTEXT_MODE:-lexical}"
MAX_CONTEXT_CHARS="${MAX_CONTEXT_CHARS:-180000}"
PROVIDER_TIMEOUT_SECONDS="${PROVIDER_TIMEOUT_SECONDS:-600}"

DEFAULT_RUN_ROOT="$(python3 - "$MANIFEST" "$RUN_ID" <<'PY'
import json
import sys
from pathlib import Path

manifest = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
run_id = sys.argv[2]
base = manifest.get("reporting", {}).get("output_dir", "evals/altibase_answerability/reports")
print(f"{base}/runs/{run_id}")
PY
)"
RUN_ROOT="${RUN_ROOT:-$DEFAULT_RUN_ROOT}"
ANSWERS_DIR="${RUN_ROOT}/answers"
JUDGE_DIR="${RUN_ROOT}/judge"
SUMMARY_FILE="${RUN_ROOT}/summary.txt"
LOG_FILE="${RUN_ROOT}/run-test.log"

mkdir -p "$ANSWERS_DIR" "$JUDGE_DIR"

log() {
  printf '%s\n' "$*" | tee -a "$LOG_FILE"
}

run_logged() {
  log "$*"
  "$@" 2>&1 | tee -a "$LOG_FILE"
}

require_live_provider_config() {
  if [[ "$MODE" != "live" ]]; then
    return
  fi

  case "$PROVIDER" in
    openai|openai_responses)
      if [[ -z "${OPENAI_API_KEY:-}" ]]; then
        log "ERROR: OPENAI_API_KEY is required for live OpenAI runs."
        log "Example: OPENAI_API_KEY=... OPENAI_MODEL=... ./run-test.sh"
        exit 2
      fi
      if [[ -z "$MODEL" ]]; then
        log "ERROR: OPENAI_MODEL, MODEL_NAME, or ALTIBASE_TEST_MODEL is required."
        log "Example: OPENAI_MODEL=... ./run-test.sh"
        exit 2
      fi
      python3 - <<'PY' 2>&1 | tee -a "$LOG_FILE"
try:
    import openai  # noqa: F401
except ImportError:
    raise SystemExit("ERROR: Python package 'openai' is required. Install it in this environment first.")
PY
      ;;
    command)
      if [[ -z "${PROVIDER_COMMAND:-}" ]]; then
        log "ERROR: PROVIDER_COMMAND is required when PROVIDER=command."
        exit 2
      fi
      if [[ ! -x "$PROVIDER_COMMAND" ]]; then
        log "ERROR: PROVIDER_COMMAND is not executable: ${PROVIDER_COMMAND}"
        exit 2
      fi
      ;;
    *)
      log "ERROR: unsupported live provider: ${PROVIDER}"
      log "Supported live providers: openai, openai_responses, command"
      exit 2
      ;;
  esac
}

build_optional_args() {
  OPTIONAL_ARGS=()
  if [[ -n "${LIMIT:-}" ]]; then
    OPTIONAL_ARGS+=(--limit "$LIMIT")
  fi
  if [[ -n "${QUESTION_ID:-}" ]]; then
    OPTIONAL_ARGS+=(--question-id "$QUESTION_ID")
  fi
}

write_summary() {
  local aggregate_json="$1"
  local runner_status="${2:-ok}"
  local answer_status="${3:-0}"
  python3 - "$aggregate_json" "$SUMMARY_FILE" "$runner_status" "$answer_status" <<'PY'
import json
import sys
from pathlib import Path

aggregate_path = Path(sys.argv[1])
summary_path = Path(sys.argv[2])
runner_status = sys.argv[3]
answer_status = sys.argv[4]
report = json.loads(aggregate_path.read_text(encoding="utf-8"))
metrics = report["overall_metrics"]
domains = report["aggregates"]["domain"]
worst_domain = min(domains, key=lambda item: item["metrics"]["pass_rate"]) if domains else None
decision = "invalid_run" if runner_status != "ok" else report["readiness_decision"]

def pct(value: float) -> str:
    return f"{value * 100:.1f}%"

lines = [
    "Altibase answerability test summary",
    f"Run ID: {report['run_id']}",
    f"Decision: {decision}",
    f"Judge decision: {report['readiness_decision']}",
    f"Answer runner status: {runner_status}",
    f"Answer runner exit code: {answer_status}",
    (
        "Totals: "
        f"{report['totals']['passed']}/{report['totals']['questions']} passed, "
        f"{report['totals']['failed']} failed"
    ),
    f"Pass rate: {pct(metrics['pass_rate'])}",
    f"Critical fact coverage: {pct(metrics['critical_fact_coverage'])}",
    f"Required token preservation: {pct(metrics['required_token_preservation'])}",
    f"Unsupported-claim rate: {pct(metrics['unsupported_claim_rate'])}",
    (
        "Worst domain: "
        + (
            f"{worst_domain['key']} ({pct(worst_domain['metrics']['pass_rate'])})"
            if worst_domain
            else "n/a"
        )
    ),
    f"Protected-topic blockers: {sum(item['count'] for item in report['protected_topic_blockers'])}",
    f"Report: {report['artifacts']['markdown_report_path']}",
    f"Aggregate JSON: {aggregate_path.as_posix()}",
    f"Answers: {report['artifacts']['answers_path']}",
    f"Judgments: {report['artifacts']['judgments_path']}",
]
summary_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(
    "RESULT "
    f"decision={decision} "
    f"pass_rate={pct(metrics['pass_rate'])} "
    f"critical={pct(metrics['critical_fact_coverage'])} "
    f"tokens={pct(metrics['required_token_preservation'])} "
    f"report={report['artifacts']['markdown_report_path']}"
)
PY
}

write_dry_run_summary() {
  local run_json="$1"
  python3 - "$run_json" "$SUMMARY_FILE" "$TEST_SUITE" <<'PY'
import json
import sys
from pathlib import Path

run_path = Path(sys.argv[1])
summary_path = Path(sys.argv[2])
suite = sys.argv[3]
run = json.loads(run_path.read_text(encoding="utf-8"))
lines = [
    "Altibase answerability dry-run summary",
    f"Suite: {suite}",
    f"Run ID: {run.get('run_id')}",
    f"Manifest: {run.get('manifest_id')}",
    f"Mode: {run.get('mode')}",
    f"Provider: {run.get('provider')}",
    f"Model: {run.get('model')}",
    f"Answer records: {run.get('answer_records')}",
    f"Errors: {run.get('errors')}",
    f"Context glob: {run.get('context_source_glob')}",
    f"Context root: {run.get('context_root')}",
    f"Run JSON: {run_path.as_posix()}",
    f"Answers: {(run_path.parent / 'answers.jsonl').as_posix()}",
]
summary_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(
    "RESULT "
    f"dry_run suite={suite} "
    f"records={run.get('answer_records')} "
    f"errors={run.get('errors')} "
    f"summary={summary_path.as_posix()}"
)
PY
}

require_live_provider_config
build_optional_args

log "Altibase answerability test"
log "suite=${TEST_SUITE}"
log "run_id=${RUN_ID}"
log "manifest=${MANIFEST}"
log "profile=${PROFILE}"
log "mode=${MODE} provider=${PROVIDER} model=${MODEL:-fixture} context=${CONTEXT_MODE}"
if [[ "$PROVIDER" == "command" ]]; then
  log "provider_command=${PROVIDER_COMMAND}"
  log "codex_exec_model=${CODEX_EXEC_MODEL:-}"
fi
log "artifacts=${RUN_ROOT}"

run_logged python3 evals/altibase_answerability/scripts/validate_benchmark.py \
  --manifest "$MANIFEST" \
  --profile "$PROFILE"

run_logged python3 evals/altibase_answerability/scripts/answer_runner.py --self-test
run_logged python3 evals/altibase_answerability/scripts/judge_report.py --self-test

PROVIDER_ARGS=()
if [[ "$PROVIDER" == "command" && -n "${PROVIDER_COMMAND:-}" ]]; then
  PROVIDER_ARGS+=(--provider-command "$PROVIDER_COMMAND")
fi

ANSWER_STATUS=0
python3 evals/altibase_answerability/scripts/answer_runner.py \
  --manifest "$MANIFEST" \
  --policy "$POLICY" \
  --run-id "$RUN_ID" \
  --mode "$MODE" \
  --provider "$PROVIDER" \
  --model "${MODEL:-fixture}" \
  --context-mode "$CONTEXT_MODE" \
  --max-context-chars "$MAX_CONTEXT_CHARS" \
  --provider-timeout-seconds "$PROVIDER_TIMEOUT_SECONDS" \
  --validate-output \
  --output-dir "$ANSWERS_DIR" \
  "${OPTIONAL_ARGS[@]}" \
  "${PROVIDER_ARGS[@]}" 2>&1 | tee -a "$LOG_FILE" || ANSWER_STATUS=$?

if [[ ! -s "${ANSWERS_DIR}/answers.jsonl" ]]; then
  log "ERROR: answer runner did not produce ${ANSWERS_DIR}/answers.jsonl"
  exit 1
fi

if [[ "$ANSWER_STATUS" -ne 0 ]]; then
  log "WARNING: answer runner reported errors; generating judge report from produced answer records."
fi

if [[ "$MODE" == "dry_run" && "${JUDGE_DRY_RUN:-0}" != "1" ]]; then
  write_dry_run_summary "${ANSWERS_DIR}/run.json" | tee -a "$LOG_FILE"
  log "SUMMARY ${SUMMARY_FILE}"
  exit "$ANSWER_STATUS"
fi

run_logged python3 evals/altibase_answerability/scripts/judge_report.py \
  --manifest "$MANIFEST" \
  --policy "$POLICY" \
  --answers "${ANSWERS_DIR}/answers.jsonl" \
  --validate-output \
  --output-dir "$JUDGE_DIR" \
  "${OPTIONAL_ARGS[@]}"

RUNNER_STATUS="ok"
if [[ "$ANSWER_STATUS" -ne 0 ]]; then
  RUNNER_STATUS="invalid_run"
fi

write_summary "${JUDGE_DIR}/aggregate_report.json" "$RUNNER_STATUS" "$ANSWER_STATUS" | tee -a "$LOG_FILE"
log "SUMMARY ${SUMMARY_FILE}"

if [[ "$ANSWER_STATUS" -ne 0 ]]; then
  exit "$ANSWER_STATUS"
fi
