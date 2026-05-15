#!/usr/bin/env python3
"""Run review/remediation_plan.md tasks one step at a time.

The remediation plan is the source of truth. This runner parses the plan table,
finds the active task according to the plan's resume rule, updates task state,
and runs the validation command attached to a task.
"""

from __future__ import annotations

import argparse
import os
import re
import shlex
import subprocess
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[2]
DEFAULT_PLAN = ROOT_DIR / "review" / "remediation_plan.md"
FAILURE_LOG = ROOT_DIR / "review" / "remediation_failure_log.md"
VALID_STATES = ("ToDo", "Progress", "Done", "Fail")
TERMINAL_STATES = ("Done", "Fail")
DEFAULT_REVIEW_RETRIES = int(os.environ.get("REMEDIATION_REVIEW_RETRIES", "2"))


@dataclass(frozen=True)
class Task:
    id: str
    state: str
    severity: str
    source_reports: str
    target_files: str
    required_change: str
    validation: str
    section: str
    line_no: int
    order: int


@dataclass(frozen=True)
class ReviewResult:
    verdict: str
    returncode: int
    output: str


def die(message: str, code: int = 1) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(code)


def relpath(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT_DIR))
    except ValueError:
        return str(path)


def one_line(value: str | None) -> str:
    text = (value or "").strip()
    if not text:
        return "No reason supplied by caller."
    return re.sub(r"\s+", " ", text)


def append_failure_log(plan_path: Path, task: Task, reason: str, *, source: str) -> None:
    if not FAILURE_LOG.exists():
        FAILURE_LOG.write_text(
            "# Remediation Failure Log\n\n"
            "This file records why remediation tasks enter `Fail` or why a finish gate fails.\n",
            encoding="utf-8",
        )

    timestamp = datetime.now().astimezone().isoformat(timespec="seconds")
    entry = "\n".join(
        [
            "",
            f"## {timestamp} - {task.id}",
            "",
            f"- Source: {source}",
            f"- State at failure: {task.state}",
            f"- Reason: {one_line(reason)}",
            f"- Plan: `{relpath(plan_path)}:{task.line_no}`",
            f"- Severity: {task.severity}",
            f"- Source reports: {task.source_reports}",
            f"- Target files: {task.target_files}",
            f"- Validation: {task.validation}",
            "",
        ]
    )
    with FAILURE_LOG.open("a", encoding="utf-8") as handle:
        handle.write(entry)
    print(f"failure reason recorded in {relpath(FAILURE_LOG)}")


def split_markdown_table_row(line: str) -> list[str]:
    """Split a markdown table row, ignoring pipes inside code spans.

    The validation column contains commands such as `rg -n "A|B" ...`, so a
    normal split('|') is not safe.
    """

    text = line.strip()
    if not text.startswith("|") or not text.endswith("|"):
        return []

    text = text[1:-1]
    cells: list[str] = []
    buf: list[str] = []
    in_code = False
    escaped = False

    for ch in text:
        if ch == "`" and not escaped:
            in_code = not in_code
            buf.append(ch)
        elif ch == "|" and not in_code and not escaped:
            cells.append("".join(buf).strip())
            buf = []
        else:
            buf.append(ch)

        if ch == "\\" and not escaped:
            escaped = True
        else:
            escaped = False

    cells.append("".join(buf).strip())
    return cells


def strip_code_span(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value.startswith("`") and value.endswith("`"):
        return value[1:-1]
    return value


def load_text(plan_path: Path) -> str:
    if not plan_path.exists():
        die(f"plan file not found: {relpath(plan_path)}")
    return plan_path.read_text(encoding="utf-8")


def parse_tasks(plan_path: Path = DEFAULT_PLAN) -> list[Task]:
    text = load_text(plan_path)
    tasks: list[Task] = []
    section = ""

    for line_no, line in enumerate(text.splitlines(), start=1):
        heading = re.match(r"^##\s+(.+)$", line)
        if heading:
            section = heading.group(1).strip()
            continue

        cells = split_markdown_table_row(line)
        if len(cells) < 7:
            continue

        task_id, state = cells[0], cells[1]
        if task_id == "ID" or state == "State":
            continue
        if state not in VALID_STATES:
            continue

        tasks.append(
            Task(
                id=task_id,
                state=state,
                severity=cells[2],
                source_reports=cells[3],
                target_files=cells[4],
                required_change=cells[5],
                validation=cells[6],
                section=section,
                line_no=line_no,
                order=len(tasks),
            )
        )

    if not tasks:
        die(f"no remediation tasks found in {relpath(plan_path)}")
    return tasks


def task_by_id(tasks: list[Task], task_id: str) -> Task:
    for task in tasks:
        if task.id == task_id:
            return task
    die(f"unknown task id: {task_id}")


def progress_tasks(tasks: list[Task]) -> list[Task]:
    return [task for task in tasks if task.state == "Progress"]


def next_task(tasks: list[Task]) -> Task | None:
    in_progress = progress_tasks(tasks)
    if in_progress:
        return in_progress[0]

    for task in tasks:
        if task.state == "ToDo":
            return task
    return None


def update_task_state(plan_path: Path, task_id: str, new_state: str, *, force: bool = False) -> None:
    if new_state not in VALID_STATES:
        die(f"invalid state: {new_state}; expected one of {', '.join(VALID_STATES)}")

    tasks = parse_tasks(plan_path)
    task = task_by_id(tasks, task_id)

    if task.state == new_state:
        print(f"{task_id} is already {new_state}.")
        return

    if new_state == "Progress" and not force:
        active = [item for item in progress_tasks(tasks) if item.id != task_id]
        if active:
            ids = ", ".join(item.id for item in active)
            die(f"another task is already Progress: {ids}; finish it first or use --force")

    text = load_text(plan_path)
    lines = text.splitlines(keepends=True)
    idx = task.line_no - 1
    pattern = re.compile(
        rf"^(\|\s*{re.escape(task_id)}\s*\|\s*)"
        rf"(?:{'|'.join(VALID_STATES)})"
        rf"(\s*\|)"
    )
    updated = pattern.sub(rf"\g<1>{new_state}\g<2>", lines[idx], count=1)
    if updated == lines[idx]:
        die(f"failed to update state for {task_id} on line {task.line_no}")

    lines[idx] = updated
    plan_path.write_text("".join(lines), encoding="utf-8")
    print(f"{task_id}: {task.state} -> {new_state}")


def command_for_task(plan_path: Path, task: Task) -> str | None:
    validation = strip_code_span(task.validation)
    if validation == "See command block below.":
        return extract_common_validation_block(plan_path)
    if validation and validation != "-":
        return validation
    return None


def extract_common_validation_block(plan_path: Path) -> str | None:
    text = load_text(plan_path)
    marker = "Common validation commands:"
    start = text.find(marker)
    if start < 0:
        return None

    after = text[start + len(marker) :]
    match = re.search(r"```bash\n(?P<body>.*?)\n```", after, flags=re.S)
    if not match:
        return None
    return match.group("body").strip()


def run_shell(command: str, *, quiet: bool = False) -> int:
    if not quiet:
        print(f"$ {command}")
        sys.stdout.flush()
    completed = subprocess.run(
        ["/bin/bash", "-lc", command],
        cwd=ROOT_DIR,
        text=True,
    )
    if not quiet:
        print(f"exit: {completed.returncode}")
    return completed.returncode


def run_process(command: list[str], *, quiet: bool = False) -> int:
    if not quiet:
        print(f"$ {shlex.join(command)}")
        sys.stdout.flush()
    completed = subprocess.run(command, cwd=ROOT_DIR, text=True)
    if not quiet:
        print(f"exit: {completed.returncode}")
    return completed.returncode


def task_pathspecs(task: Task, plan_path: Path) -> list[str]:
    pathspecs: list[str] = []

    for token in re.findall(r"`([^`]+)`", task.target_files):
        token = token.strip()
        if token == "this file":
            pathspecs.append(relpath(plan_path))
            continue
        if token.startswith(("GPTs/", "review/")):
            pathspecs.append(token)

    if "this file" in task.target_files and relpath(plan_path) not in pathspecs:
        pathspecs.append(relpath(plan_path))

    unique: list[str] = []
    for pathspec in pathspecs:
        if pathspec not in unique:
            unique.append(pathspec)
    return unique


def source_report_paths(task: Task) -> list[str]:
    paths: list[str] = []
    for report_id in re.findall(r"\bR\d{2}\b", task.source_reports):
        paths.extend(str(path.relative_to(ROOT_DIR)) for path in sorted((ROOT_DIR / "review" / "reports").glob(f"{report_id}_*.md")))
    return paths


def common_review_command() -> str:
    return "\n".join(
        [
            "find GPTs/attachments -maxdepth 1 -type f -name '*.md' ! -name 'README.md' | sort | wc -l",
            "rg -n 'trunk|Altibase_trunk|file://|C:/|C:\\\\|/home/et16|/Users/|Manuals/Altibase|ReleaseNotes/kor|JOB-[0-9]+|IMG-[0-9]+|Conversion TODO' GPTs/attachments/*.md GPTs/attachments/README.md || true",
            "rg -n '!\\[[^]]*\\]\\([^)]*\\.(png|jpg|jpeg|gif|svg|webp)\\)|<img|https?://[^ )]+\\.(png|jpg|jpeg|gif|svg|webp)|[^[:space:]]+\\.(png|jpg|jpeg|gif|svg|webp)' GPTs/attachments/*.md GPTs/attachments/README.md || true",
        ]
    )


def run_review_checks(
    plan_path: Path,
    task: Task,
    *,
    strict_validation: bool = False,
    include_common: bool = True,
    quiet: bool = False,
) -> int:
    pathspecs = task_pathspecs(task, plan_path)
    report_paths = source_report_paths(task)
    validation = command_for_task(plan_path, task)
    hard_failures = 0

    if not quiet:
        print("Review scope:")
        print_task(task, plan_path)
        if pathspecs:
            print("\nTarget pathspecs:")
            for pathspec in pathspecs:
                print(f"- {pathspec}")
        else:
            print("\nTarget pathspecs: none parsed from plan; reviewing repository diff.")

    status_cmd = ["git", "status", "--short", "--", *(pathspecs or ["."])]
    diffstat_cmd = ["git", "diff", "--stat", "--", *(pathspecs or ["."])]
    diff_cmd = ["git", "diff", "--", *(pathspecs or ["."])]
    diff_check_cmd = ["git", "diff", "--check", "--", *(pathspecs or ["."])]

    print("\nChanged files:")
    run_process(status_cmd, quiet=quiet)
    print("\nDiff summary:")
    run_process(diffstat_cmd, quiet=quiet)
    print("\nDiff:")
    run_process(diff_cmd, quiet=quiet)
    print("\nWhitespace/conflict-marker check:")
    if run_process(diff_check_cmd, quiet=quiet) != 0:
        hard_failures += 1

    if report_paths:
        print("\nRelated review report excerpts:")
        run_process(
            [
                "rg",
                "-n",
                r"^Verdict:|^\| (Blocker|High|Medium|Low) \|",
                *report_paths,
            ],
            quiet=quiet,
        )
    else:
        print("\nRelated review report excerpts: none parsed from Source Reports.")

    if validation:
        print("\nTask validation command:")
        validation_rc = run_shell(validation, quiet=quiet)
        if strict_validation and validation_rc != 0:
            hard_failures += 1
    else:
        print("\nTask validation command: none.")
        if strict_validation:
            hard_failures += 1

    if include_common:
        print("\nCommon upload-boundary review checks:")
        run_shell(common_review_command(), quiet=quiet)

    print("\nManual review decision:")
    print("- Confirm the diff satisfies the Required Change exactly.")
    print("- Confirm related report findings are addressed without broad or unsupported claims.")
    print(f"- If the issue is small and scoped, fix it and run this review again. Retry budget: {DEFAULT_REVIEW_RETRIES}.")
    print("- If the issue remains unresolved after retry, mark the task Fail instead of Done.")
    sys.stdout.flush()

    return 1 if hard_failures else 0


def build_codex_review_prompt(plan_path: Path, task: Task) -> str:
    return f"""You are Codex acting as an independent reviewer for one remediation task.

Workspace: {ROOT_DIR}
Plan file: {relpath(plan_path)}

Do not edit files. Do not change task state. Review only.

Task:
ID: {task.id}
State: {task.state}
Severity: {task.severity}
Section: {task.section}
Source reports: {task.source_reports}
Target files: {task.target_files}
Required change: {task.required_change}
Validation: {task.validation}

Review procedure:
1. Run the local evidence command:
   bash GPTs/scripts/remediation_plan.sh --plan {shlex.quote(str(plan_path))} review {task.id} --local
2. Inspect the diff, the target files, and the related review report excerpts.
3. Decide whether the final document change satisfies the Required Change without adding unsupported claims, internal source labels, unrelated edits, or customer-facing risk.
4. Use `PASS` only when the required change is complete and no actionable issue remains.
5. Use `RETRY` when a small, scoped, source-backed correction is needed and can reasonably be fixed by the current task worker.
6. Use `FAIL` when the issue is blocked, source evidence is insufficient, the fix would broaden scope, or repeated review would not be productive.

Output format:
Start your final answer with exactly one line:
REMEDIATION_REVIEW_RESULT: PASS
or
REMEDIATION_REVIEW_RESULT: RETRY
or
REMEDIATION_REVIEW_RESULT: FAIL

Then add a concise reason. For RETRY or FAIL, include specific file/line references or exact missing evidence.
"""


def parse_review_verdict(output: str) -> str | None:
    match = re.search(r"^REMEDIATION_REVIEW_RESULT:\s*(PASS|RETRY|FAIL)\s*$", output, flags=re.M)
    if match:
        return match.group(1)
    return None


def run_codex_review(
    plan_path: Path,
    task: Task,
    *,
    codex_bin: str | None = None,
    codex_subcommand: str | None = None,
    quiet: bool = False,
) -> ReviewResult:
    codex_bin = codex_bin or os.environ.get("CODEX_BIN", "codex")
    codex_subcommand = codex_subcommand or os.environ.get("CODEX_SUBCOMMAND", "exec")
    prompt = build_codex_review_prompt(plan_path, task)
    command = [codex_bin, codex_subcommand, prompt]

    if not quiet:
        print(f"$ {shlex.join([codex_bin, codex_subcommand, '<review-prompt>'])}")
        sys.stdout.flush()

    completed = subprocess.run(
        command,
        cwd=ROOT_DIR,
        text=True,
        capture_output=True,
    )
    output = (completed.stdout or "") + (completed.stderr or "")
    if output and not quiet:
        print(output, end="" if output.endswith("\n") else "\n")
    if not quiet:
        print(f"exit: {completed.returncode}")

    verdict = parse_review_verdict(output)
    if completed.returncode != 0 and verdict is None:
        verdict = "FAIL"
    if verdict is None:
        verdict = "FAIL"
        if not quiet:
            print("REMEDIATION_REVIEW_RESULT: FAIL")
            print("Reason: Codex review output did not include a parseable REMEDIATION_REVIEW_RESULT line.")
    sys.stdout.flush()

    return ReviewResult(verdict=verdict, returncode=completed.returncode, output=output)


def print_task(task: Task, plan_path: Path = DEFAULT_PLAN) -> None:
    print(f"ID:              {task.id}")
    print(f"State:           {task.state}")
    print(f"Severity:        {task.severity}")
    print(f"Section:         {task.section}")
    print(f"Source Reports:  {task.source_reports}")
    print(f"Target Files:    {task.target_files}")
    print(f"Required Change: {task.required_change}")
    print(f"Validation:      {task.validation}")
    print(f"Plan Line:       {relpath(plan_path)}:{task.line_no}")


def task_summary_line(task: Task) -> str:
    target = task.target_files.replace("`", "")
    if len(target) > 56:
        target = target[:53] + "..."
    return f"{task.id:<6} {task.state:<8} {task.severity:<10} {task.source_reports:<12} {target}"


def cmd_status(args: argparse.Namespace) -> int:
    tasks = parse_tasks(args.plan)
    counts = Counter(task.state for task in tasks)
    print(f"Plan: {relpath(args.plan)}")
    print("State summary:")
    for state in VALID_STATES:
        print(f"  {state:<8} {counts[state]}")

    active = progress_tasks(tasks)
    if active:
        print("\nProgress task:")
        for task in active:
            print(task_summary_line(task))
    else:
        print("\nProgress task: none")

    candidate = next_task(tasks)
    if candidate:
        print("\nNext task:")
        print(task_summary_line(candidate))
    else:
        print("\nNext task: none")
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    tasks = parse_tasks(args.plan)
    print(f"{'ID':<6} {'State':<8} {'Severity':<10} {'Source':<12} Target")
    for task in tasks:
        if args.state and task.state != args.state:
            continue
        if args.severity and task.severity != args.severity:
            continue
        print(task_summary_line(task))
    return 0


def cmd_next(args: argparse.Namespace) -> int:
    task = next_task(parse_tasks(args.plan))
    if not task:
        print("No Progress or ToDo tasks remain.")
        return 1
    if args.id_only:
        print(task.id)
    else:
        print_task(task, args.plan)
    return 0


def cmd_show(args: argparse.Namespace) -> int:
    tasks = parse_tasks(args.plan)
    task = task_by_id(tasks, args.task_id) if args.task_id else next_task(tasks)
    if not task:
        print("No Progress or ToDo tasks remain.")
        return 1
    print_task(task, args.plan)
    return 0


def cmd_start(args: argparse.Namespace) -> int:
    tasks = parse_tasks(args.plan)
    if args.task_id:
        task = task_by_id(tasks, args.task_id)
        if task.state == "Progress":
            print(f"{task.id} is already Progress.")
            return 0
        if task.state != "ToDo" and not args.force:
            die(f"start requires ToDo; {task.id} is {task.state}. Use --force for recovery.")
    else:
        task = next_task(tasks)
        if not task:
            print("No Progress or ToDo tasks remain.")
            return 1
        if task.state == "Progress":
            print(f"{task.id} is already Progress.")
            return 0

    update_task_state(args.plan, task.id, "Progress", force=args.force)
    return 0


def cmd_mark(args: argparse.Namespace) -> int:
    task = task_by_id(parse_tasks(args.plan), args.task_id)
    update_task_state(args.plan, args.task_id, args.state, force=args.force)
    if args.state == "Fail":
        append_failure_log(args.plan, task, args.reason, source="mark")
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    tasks = parse_tasks(args.plan)
    task = task_by_id(tasks, args.task_id) if args.task_id else next_task(tasks)
    if not task:
        print("No Progress or ToDo tasks remain.")
        return 1

    command = command_for_task(args.plan, task)
    if not command:
        print(f"{task.id} has no runnable validation command.")
        return 2

    return run_shell(command, quiet=args.quiet)


def cmd_review(args: argparse.Namespace) -> int:
    tasks = parse_tasks(args.plan)
    task = task_by_id(tasks, args.task_id) if args.task_id else next_task(tasks)
    if not task:
        print("No Progress or ToDo tasks remain.")
        return 1

    if args.local:
        return run_review_checks(
            args.plan,
            task,
            strict_validation=args.strict,
            include_common=not args.no_common,
            quiet=args.quiet,
        )

    result = run_codex_review(
        args.plan,
        task,
        codex_bin=args.codex_bin,
        codex_subcommand=args.codex_subcommand,
        quiet=args.quiet,
    )
    if result.verdict == "PASS":
        return 0
    if result.verdict == "RETRY":
        return 2
    return 1


def cmd_finish(args: argparse.Namespace) -> int:
    if args.state not in TERMINAL_STATES:
        die(f"finish state must be one of {', '.join(TERMINAL_STATES)}")

    tasks = parse_tasks(args.plan)
    task = task_by_id(tasks, args.task_id)

    if task.state != "Progress" and not args.force:
        die(f"finish expects Progress; {task.id} is {task.state}. Use --force for recovery.")

    if args.state == "Done" and not args.no_review:
        if args.local_review:
            rc = run_review_checks(
                args.plan,
                task,
                strict_validation=args.strict_review,
                include_common=not args.no_common_review,
                quiet=False,
            )
            if rc != 0:
                append_failure_log(
                    args.plan,
                    task,
                    "local review checks found hard failures; task was not marked Done",
                    source="finish Done local-review",
                )
                die("local review checks found hard failures; task was not marked Done")
        else:
            result = run_codex_review(
                args.plan,
                task,
                codex_bin=args.codex_bin,
                codex_subcommand=args.codex_subcommand,
                quiet=False,
            )
            if result.verdict != "PASS":
                append_failure_log(
                    args.plan,
                    task,
                    f"Codex review returned {result.verdict}; task was not marked Done",
                    source="finish Done review",
                )
                die(f"Codex review returned {result.verdict}; task was not marked Done")
    elif args.state == "Done" and not args.no_validate:
        command = command_for_task(args.plan, task)
        if command:
            rc = run_shell(command, quiet=False)
            if rc != 0:
                print(
                    "warning: validation command returned non-zero. "
                    "The plan uses evidence commands as well as strict checks; inspect the output before accepting Done.",
                    file=sys.stderr,
                )
        else:
            print(f"warning: {task.id} has no runnable validation command.", file=sys.stderr)

    update_task_state(args.plan, args.task_id, args.state, force=args.force)
    if args.state == "Fail":
        append_failure_log(args.plan, task, args.reason, source="finish Fail")
    return 0


def build_prompt(plan_path: Path, task: Task) -> str:
    validation = command_for_task(plan_path, task) or task.validation
    return f"""You are Codex working in {ROOT_DIR}.

Execute exactly one remediation task from review/remediation_plan.md.

Follow the plan's state rules:
- If any task is already Progress, continue that task before starting another.
- Before editing a ToDo task, mark it Progress.
- After editing, run the listed validation.
- Run the remediation review command before marking Done. This invokes a separate Codex CLI reviewer.
- Mark the task Done only when the required change is applied, validation evidence is acceptable, and Codex review returns `REMEDIATION_REVIEW_RESULT: PASS`.
- Mark the task Fail if the task is blocked or validation shows the change is not complete. Include `--reason` so the failure log captures the cause.
- Do not mark R15 final readiness tasks Done until their prerequisite tasks are Done or explicitly accepted as residual risk.
- Review retry rule: after the first review, if a finding is small, scoped to this task, and source-backed, fix it and run review again. Retry at most {DEFAULT_REVIEW_RETRIES} time(s). If the same issue remains, required source evidence is unclear, or a fix would broaden scope, mark the task Fail and record the reason.
- If Codex review returns `RETRY`, fix only the reported scoped issue and rerun review. If Codex review returns `FAIL`, mark the task Fail.

Task:
ID: {task.id}
Current state: {task.state}
Severity: {task.severity}
Source reports: {task.source_reports}
Target files: {task.target_files}
Required change: {task.required_change}
Validation command:
{validation}

Use these commands for state transitions:
- Start: bash GPTs/scripts/remediation_plan.sh start {task.id}
- Validate: bash GPTs/scripts/remediation_plan.sh validate {task.id}
- Review: bash GPTs/scripts/remediation_plan.sh review {task.id}
- Finish Done: bash GPTs/scripts/remediation_plan.sh finish {task.id} Done
- Finish Fail: bash GPTs/scripts/remediation_plan.sh finish {task.id} Fail --force --reason "short failure reason"

Keep edits scoped to the target files and any directly required supporting report or source-inventory files. Do not change unrelated tasks.
Do not use `finish {task.id} Done` until Codex review has returned PASS after the final edit. The finish command runs a final Codex review gate as a safeguard.
"""


def cmd_prompt(args: argparse.Namespace) -> int:
    tasks = parse_tasks(args.plan)
    task = task_by_id(tasks, args.task_id) if args.task_id else next_task(tasks)
    if not task:
        print("No Progress or ToDo tasks remain.")
        return 1
    print(build_prompt(args.plan, task))
    return 0


def cmd_run(args: argparse.Namespace) -> int:
    tasks = parse_tasks(args.plan)
    task = task_by_id(tasks, args.task_id) if args.task_id else next_task(tasks)
    if not task:
        print("No Progress or ToDo tasks remain.")
        return 1

    if task.state == "ToDo" and not args.no_start:
        if args.dry_run:
            print(f"[dry-run] would mark {task.id} Progress")
        else:
            update_task_state(args.plan, task.id, "Progress", force=args.force)
            task = task_by_id(parse_tasks(args.plan), task.id)

    prompt = build_prompt(args.plan, task)

    codex_bin = args.codex_bin or os.environ.get("CODEX_BIN", "codex")
    codex_subcommand = args.codex_subcommand or os.environ.get("CODEX_SUBCOMMAND", "exec")

    if args.dry_run:
        print(prompt)
        print(f"[dry-run] would run: {codex_bin} {codex_subcommand} <prompt>")
        return 0

    return subprocess.run([codex_bin, codex_subcommand, prompt], cwd=ROOT_DIR).returncode


def cmd_run_all(args: argparse.Namespace) -> int:
    max_tasks = args.max_tasks
    if max_tasks < 1:
        die("--max-tasks must be at least 1")

    if args.dry_run:
        tasks = parse_tasks(args.plan)
        active = progress_tasks(tasks)
        candidates = active[:1] if active else [task for task in tasks if task.state == "ToDo"][:max_tasks]
        if not candidates:
            print("No Progress or ToDo tasks remain.")
            return 0
        for task in candidates:
            print(f"==> [dry-run] would run {task.id}: {task.required_change}")
        return 0

    ran = 0
    while ran < max_tasks:
        task = next_task(parse_tasks(args.plan))
        if not task:
            print("No Progress or ToDo tasks remain.")
            return 0

        print(f"==> running {task.id}: {task.required_change}")
        rc = cmd_run(
            argparse.Namespace(
                plan=args.plan,
                task_id=task.id,
                no_start=False,
                force=args.force,
                dry_run=args.dry_run,
                codex_bin=args.codex_bin,
                codex_subcommand=args.codex_subcommand,
            )
        )
        ran += 1
        if rc != 0:
            print(f"==> {task.id} command failed with exit code {rc}")
            append_failure_log(
                args.plan,
                task,
                f"Codex command failed during run-all with exit code {rc}",
                source="run-all",
            )
            return rc

        refreshed = task_by_id(parse_tasks(args.plan), task.id)
        if refreshed.state == "Progress":
            print(f"==> {task.id} is still Progress; stopping for review.")
            return 2
        if refreshed.state == "Fail" and args.stop_on_fail:
            print(f"==> {task.id} is Fail; stopping because --stop-on-fail was set.")
            return 1

    print(f"Stopped after {ran} task(s).")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, default=DEFAULT_PLAN, help="Path to remediation_plan.md.")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("status", help="Show state summary and next task.").set_defaults(func=cmd_status)

    list_parser = sub.add_parser("list", help="List remediation tasks.")
    list_parser.add_argument("--state", choices=VALID_STATES, help="Only show tasks in this state.")
    list_parser.add_argument("--severity", help="Only show tasks with this severity.")
    list_parser.set_defaults(func=cmd_list)

    next_parser = sub.add_parser("next", help="Show Progress task, otherwise first ToDo task.")
    next_parser.add_argument("--id-only", action="store_true", help="Print only the task id.")
    next_parser.set_defaults(func=cmd_next)

    show_parser = sub.add_parser("show", help="Show a task, or the next task when omitted.")
    show_parser.add_argument("task_id", nargs="?")
    show_parser.set_defaults(func=cmd_show)

    start_parser = sub.add_parser("start", help="Mark the next or selected ToDo task Progress.")
    start_parser.add_argument("task_id", nargs="?")
    start_parser.add_argument("--force", action="store_true", help="Bypass state and single-Progress checks.")
    start_parser.set_defaults(func=cmd_start)

    mark_parser = sub.add_parser("mark", help="Set a task state manually.")
    mark_parser.add_argument("task_id")
    mark_parser.add_argument("state", choices=VALID_STATES)
    mark_parser.add_argument("--force", action="store_true", help="Bypass single-Progress checks.")
    mark_parser.add_argument("--reason", help="Reason to record when setting Fail.")
    mark_parser.set_defaults(func=cmd_mark)

    validate_parser = sub.add_parser("validate", help="Run the task validation command.")
    validate_parser.add_argument("task_id", nargs="?")
    validate_parser.add_argument("--quiet", action="store_true", help="Suppress runner command/exit lines.")
    validate_parser.set_defaults(func=cmd_validate)

    review_parser = sub.add_parser("review", help="Run Codex CLI review for a task.")
    review_parser.add_argument("task_id", nargs="?")
    review_parser.add_argument("--local", action="store_true", help="Print local review evidence instead of invoking Codex CLI.")
    review_parser.add_argument("--strict", action="store_true", help="Return failure when the task validation command is non-zero.")
    review_parser.add_argument("--no-common", action="store_true", help="Skip common upload-boundary review checks.")
    review_parser.add_argument("--quiet", action="store_true", help="Suppress runner command/exit lines.")
    review_parser.add_argument("--codex-bin", help="Codex binary. Default: CODEX_BIN or codex.")
    review_parser.add_argument("--codex-subcommand", help="Codex subcommand. Default: CODEX_SUBCOMMAND or exec.")
    review_parser.set_defaults(func=cmd_review)

    finish_parser = sub.add_parser("finish", help="Run Codex review and mark a Progress task Done or Fail.")
    finish_parser.add_argument("task_id")
    finish_parser.add_argument("state", choices=TERMINAL_STATES)
    finish_parser.add_argument("--force", action="store_true", help="Allow finishing a non-Progress task.")
    finish_parser.add_argument("--no-review", action="store_true", help="Skip the review gate before Done.")
    finish_parser.add_argument("--reviewed", action="store_true", help="Deprecated no-op kept for older prompts.")
    finish_parser.add_argument("--local-review", action="store_true", help="Use local evidence checks instead of Codex CLI review.")
    finish_parser.add_argument("--strict-review", action="store_true", help="Fail Done when the task validation command is non-zero.")
    finish_parser.add_argument("--no-common-review", action="store_true", help="Skip common upload-boundary checks in the Done review gate.")
    finish_parser.add_argument("--no-validate", action="store_true", help="Skip validation before Done.")
    finish_parser.add_argument("--reason", help="Reason to record when setting Fail.")
    finish_parser.add_argument("--codex-bin", help="Codex binary. Default: CODEX_BIN or codex.")
    finish_parser.add_argument("--codex-subcommand", help="Codex subcommand. Default: CODEX_SUBCOMMAND or exec.")
    finish_parser.set_defaults(func=cmd_finish)

    prompt_parser = sub.add_parser("prompt", help="Print the Codex prompt for the next or selected task.")
    prompt_parser.add_argument("task_id", nargs="?")
    prompt_parser.set_defaults(func=cmd_prompt)

    run_parser = sub.add_parser("run", help="Start one task and run Codex on it.")
    run_parser.add_argument("task_id", nargs="?")
    run_parser.add_argument("--no-start", action="store_true", help="Do not mark ToDo as Progress before running.")
    run_parser.add_argument("--force", action="store_true", help="Bypass single-Progress checks.")
    run_parser.add_argument("--dry-run", action="store_true", help="Print prompt without running Codex.")
    run_parser.add_argument("--codex-bin", help="Codex binary. Default: CODEX_BIN or codex.")
    run_parser.add_argument("--codex-subcommand", help="Codex subcommand. Default: CODEX_SUBCOMMAND or exec.")
    run_parser.set_defaults(func=cmd_run)

    run_all_parser = sub.add_parser("run-all", help="Run tasks sequentially through Codex.")
    run_all_parser.add_argument("--max-tasks", type=int, default=int(os.environ.get("MAX_TASKS", "1")))
    run_all_parser.add_argument("--stop-on-fail", action="store_true")
    run_all_parser.add_argument("--force", action="store_true", help="Bypass single-Progress checks.")
    run_all_parser.add_argument("--dry-run", action="store_true", help="Print prompts without running Codex.")
    run_all_parser.add_argument("--codex-bin", help="Codex binary. Default: CODEX_BIN or codex.")
    run_all_parser.add_argument("--codex-subcommand", help="Codex subcommand. Default: CODEX_SUBCOMMAND or exec.")
    run_all_parser.set_defaults(func=cmd_run_all)

    return parser


def main(argv: list[str]) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not args.command:
        args.command = "status"
        args.func = cmd_status
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
