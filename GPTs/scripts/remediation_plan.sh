#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/../.." && pwd)"

export PYTHONDONTWRITEBYTECODE=1
exec python3 "${ROOT_DIR}/GPTs/scripts/remediation_plan.py" "$@"
