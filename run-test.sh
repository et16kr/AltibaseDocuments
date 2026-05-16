#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_ROOT"

MANIFEST="${MANIFEST:-evals/altibase_answerability/manifests/full_benchmark.json}"
POLICY="${POLICY:-evals/altibase_answerability/policy.json}"
RUN_ID="${RUN_ID:-altibase_answerability_$(date +%Y%m%d_%H%M%S)}"
MODE="${ALTIBASE_TEST_MODE:-${MODE:-live}}"
PROVIDER="${ALTIBASE_TEST_PROVIDER:-${PROVIDER:-command}}"
MODEL="${ALTIBASE_TEST_MODEL:-${OPENAI_MODEL:-${MODEL_NAME:-codex-exec}}}"
PROVIDER_COMMAND="${PROVIDER_COMMAND:-evals/altibase_answerability/scripts/codex_exec_provider.sh}"
CONTEXT_MODE="${CONTEXT_MODE:-lexical}"
MAX_CONTEXT_CHARS="${MAX_CONTEXT_CHARS:-180000}"
PROVIDER_TIMEOUT_SECONDS="${PROVIDER_TIMEOUT_SECONDS:-600}"

RUN_ROOT="evals/altibase_answerability/reports/full_benchmark/runs/${RUN_ID}"
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
      if [[ -z "$MODEL" ]]; then
        MODEL="command-provider"
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

require_live_provider_config
build_optional_args

log "Altibase answerability test"
log "run_id=${RUN_ID}"
log "mode=${MODE} provider=${PROVIDER} model=${MODEL:-fixture} context=${CONTEXT_MODE}"
if [[ "$PROVIDER" == "command" ]]; then
  log "provider_command=${PROVIDER_COMMAND}"
fi
log "artifacts=${RUN_ROOT}"

run_logged python3 evals/altibase_answerability/scripts/validate_benchmark.py \
  --manifest "$MANIFEST"

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
