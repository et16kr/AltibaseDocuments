#!/usr/bin/env python3
"""Run allowlisted-context answer generation for the Altibase benchmark.

The runner projects each question record to the answer-generation allowlist,
builds retrieval context only from an explicitly allowlisted Markdown context
root, checks for metadata leakage before any provider call, and writes answer
records as JSONL.
"""

from __future__ import annotations

import argparse
import datetime as dt
import glob
import hashlib
import json
import os
import re
import shlex
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


BENCHMARK_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_DIR = BENCHMARK_ROOT / "schemas"
REQUIRED_PROJECTION_KEYS = {
    "id",
    "question",
    "version_scope",
    "user_level",
    "answer_type",
    "answer_language",
}
STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "be",
    "can",
    "do",
    "does",
    "for",
    "from",
    "how",
    "i",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "should",
    "the",
    "to",
    "what",
    "when",
    "where",
    "which",
    "with",
}
ALLOWED_CONTEXT_ROOTS = {
    "GPTs/attachments/*.md": "GPTs/attachments",
    "GPTs/upload_package/*.md": "GPTs/upload_package",
}


@dataclass(frozen=True)
class AttachmentDocument:
    path: Path
    rel_path: str
    text: str


@dataclass(frozen=True)
class ContextBundle:
    text: str
    files: list[str]
    digest: str
    mode: str
    char_count: int
    chunk_count: int
    context_source_glob: str
    context_root: str


@dataclass(frozen=True)
class ContextChunk:
    rel_path: str
    heading: str
    text: str
    search_text: str
    rel_path_lower: str
    heading_lower: str


@dataclass(frozen=True)
class ProviderResult:
    status: str
    answer: str
    usage: dict[str, int | float | str | None]
    error: str | None = None


class RunnerError(Exception):
    """Raised for configuration and boundary failures."""


def repo_rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def utc_now() -> str:
    return (
        dt.datetime.now(dt.timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def canonical_json(data: Any) -> str:
    return json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def digest_text(text: str) -> str:
    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except FileNotFoundError as exc:
        raise RunnerError(f"Missing JSON file: {repo_rel(path)}") from exc
    except json.JSONDecodeError as exc:
        raise RunnerError(f"Invalid JSON in {repo_rel(path)}:{exc.lineno}:{exc.colno}: {exc.msg}") from exc
    if not isinstance(data, dict):
        raise RunnerError(f"Expected JSON object: {repo_rel(path)}")
    return data


def resolve_repo_path(path_text: str, label: str) -> Path:
    path = Path(path_text)
    if path.is_absolute():
        raise RunnerError(f"{label} must be repository-relative: {path_text}")
    resolved = (REPO_ROOT / path).resolve()
    try:
        resolved.relative_to(REPO_ROOT)
    except ValueError as exc:
        raise RunnerError(f"{label} escapes repository root: {path_text}") from exc
    return resolved


def expand_question_files(manifest: dict[str, Any]) -> list[Path]:
    resolved_files: list[Path] = []
    for pattern in manifest.get("question_files", []):
        if any(char in pattern for char in "*?[]"):
            matches = sorted(Path(match).resolve() for match in glob.glob(str(REPO_ROOT / pattern)))
            if not matches:
                raise RunnerError(f"Question file glob matched no files: {pattern}")
            resolved_files.extend(matches)
        else:
            resolved_files.append(resolve_repo_path(pattern, "question_files"))

    seen: set[Path] = set()
    unique_files: list[Path] = []
    for path in resolved_files:
        if path in seen:
            raise RunnerError(f"Duplicate resolved question file: {repo_rel(path)}")
        seen.add(path)
        if path.suffix != ".jsonl":
            raise RunnerError(f"Question file must be JSONL: {repo_rel(path)}")
        if not path.exists():
            raise RunnerError(f"Question file does not exist: {repo_rel(path)}")
        unique_files.append(path)
    return unique_files


def load_questions(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    for question_file in expand_question_files(manifest):
        with question_file.open("r", encoding="utf-8") as handle:
            for line_no, line in enumerate(handle, start=1):
                stripped = line.strip()
                if not stripped:
                    continue
                try:
                    record = json.loads(stripped)
                except json.JSONDecodeError as exc:
                    raise RunnerError(
                        f"Invalid JSONL in {repo_rel(question_file)}:{line_no}:{exc.colno}: {exc.msg}"
                    ) from exc
                if not isinstance(record, dict):
                    raise RunnerError(f"{repo_rel(question_file)}:{line_no} must be a JSON object")
                question_id = record.get("id")
                if not isinstance(question_id, str) or not question_id:
                    raise RunnerError(f"{repo_rel(question_file)}:{line_no} has no question id")
                if question_id in seen_ids:
                    raise RunnerError(f"Duplicate question id selected by manifest: {question_id}")
                seen_ids.add(question_id)
                records.append(record)
    return records


def validate_runner_policy(manifest: dict[str, Any], policy: dict[str, Any]) -> str:
    answer_generation = manifest.get("answer_generation", {})
    attachment_glob = answer_generation.get("attachment_glob")
    if not isinstance(attachment_glob, str):
        raise RunnerError("answer_generation.attachment_glob must be a string")

    context_root = ALLOWED_CONTEXT_ROOTS.get(attachment_glob)
    if context_root is None:
        raise RunnerError(
            "answer_generation.attachment_glob has no runner context-root "
            f"allowlist entry: {attachment_glob}"
        )

    manifest_context_root = answer_generation.get("context_root")
    if manifest_context_root is not None and manifest_context_root != context_root:
        raise RunnerError(
            "answer_generation.context_root must match the runner allowlist for "
            f"{attachment_glob}: {context_root}"
        )

    manifest_allowlist = set(answer_generation.get("allowlisted_question_fields", []))
    policy_allowlist = set(policy.get("answer_input_allowlist", []))
    if manifest_allowlist != policy_allowlist:
        raise RunnerError("Manifest allowlisted question fields must match policy.json")

    overlap = sorted(manifest_allowlist & set(policy.get("judge_only_question_fields", [])))
    if overlap:
        raise RunnerError(f"Answer allowlist overlaps judge-only fields: {', '.join(overlap)}")

    if answer_generation.get("default_answer_language", "en") != "en":
        raise RunnerError("answer_generation.default_answer_language must be en")

    return context_root


def load_attachment_documents(
    attachment_glob: str,
    context_root_rel: str,
) -> list[AttachmentDocument]:
    paths = sorted(Path(match).resolve() for match in glob.glob(str(REPO_ROOT / attachment_glob)))
    if not paths:
        raise RunnerError(f"Context glob matched no files: {attachment_glob}")

    documents: list[AttachmentDocument] = []
    context_root = resolve_repo_path(context_root_rel, "context_root")
    for path in paths:
        if path.suffix != ".md":
            raise RunnerError(f"Context path is not Markdown: {repo_rel(path)}")
        try:
            path.relative_to(context_root)
        except ValueError as exc:
            raise RunnerError(
                f"Context path escapes allowlisted root {context_root_rel}: {repo_rel(path)}"
            ) from exc
        documents.append(
            AttachmentDocument(
                path=path,
                rel_path=repo_rel(path),
                text=path.read_text(encoding="utf-8"),
            )
        )
    return documents


def project_question(
    question: dict[str, Any],
    manifest: dict[str, Any],
    policy: dict[str, Any],
) -> dict[str, Any]:
    answer_generation = manifest.get("answer_generation", {})
    allowlist = set(answer_generation.get("allowlisted_question_fields", []))
    projection: dict[str, Any] = {}

    requested_language = answer_generation.get("requested_language")
    for key in answer_generation.get("allowlisted_question_fields", []):
        if key == "requested_language":
            if requested_language:
                projection[key] = requested_language
        elif key == "answer_language":
            if requested_language:
                projection[key] = question.get("answer_language") or answer_generation.get(
                    "default_answer_language", "en"
                )
            else:
                projection[key] = "en"
        elif key in question:
            projection[key] = question[key]

    missing = sorted(REQUIRED_PROJECTION_KEYS - set(projection))
    if missing:
        raise RunnerError(f"{question.get('id', '<unknown>')} projection missing: {', '.join(missing)}")

    judge_only = set(policy.get("judge_only_question_fields", []))
    leaked = sorted(set(projection) & judge_only)
    if leaked:
        raise RunnerError(f"{question['id']} projected judge-only fields: {', '.join(leaked)}")

    disallowed = sorted(set(projection) - allowlist)
    if disallowed:
        raise RunnerError(f"{question['id']} projected non-allowlisted fields: {', '.join(disallowed)}")

    return projection


def tokenize_query(projection: dict[str, Any]) -> list[str]:
    query = " ".join(
        str(projection.get(key, ""))
        for key in ("id", "question", "version_scope", "user_level", "answer_type")
    )
    tokens = re.findall(r"[A-Za-z0-9_$#./:+-]{2,}", query.lower())
    return [token for token in tokens if token not in STOPWORDS]


def make_context_chunk(rel_path: str, heading: str, text: str) -> ContextChunk:
    search_text = f"{rel_path}\n{heading}\n{text}".lower()
    return ContextChunk(
        rel_path=rel_path,
        heading=heading,
        text=text,
        search_text=search_text,
        rel_path_lower=rel_path.lower(),
        heading_lower=heading.lower(),
    )


def split_markdown_chunks(document: AttachmentDocument, chunk_chars: int) -> list[ContextChunk]:
    chunks: list[ContextChunk] = []
    current_heading = document.rel_path
    current_lines: list[str] = []
    current_size = 0

    def flush() -> None:
        nonlocal current_lines, current_size
        text = "".join(current_lines).strip()
        if text:
            chunks.append(make_context_chunk(document.rel_path, current_heading, text))
        current_lines = []
        current_size = 0

    for line in document.text.splitlines(keepends=True):
        heading = re.match(r"^(#{1,4})\s+(.+?)\s*$", line)
        if heading and current_lines:
            flush()
        if heading:
            current_heading = heading.group(2).strip()
        if current_size + len(line) > chunk_chars and current_lines:
            flush()
        current_lines.append(line)
        current_size += len(line)
    flush()
    return chunks


def collect_markdown_chunks(documents: list[AttachmentDocument], chunk_chars: int) -> list[ContextChunk]:
    chunks: list[ContextChunk] = []
    for document in documents:
        chunks.extend(split_markdown_chunks(document, chunk_chars))
    return chunks


def score_chunk(chunk: ContextChunk, query_tokens: list[str]) -> int:
    score = 0
    for token in query_tokens:
        occurrences = chunk.search_text.count(token)
        if occurrences:
            score += min(occurrences, 5)
        if token in chunk.rel_path_lower:
            score += 3
        if token in chunk.heading_lower:
            score += 5
    return score


def build_context(
    documents: list[AttachmentDocument],
    context_chunks: list[ContextChunk],
    projection: dict[str, Any],
    mode: str,
    max_context_chars: int,
    context_source_glob: str,
    context_root: str,
) -> ContextBundle:
    if max_context_chars < 0:
        raise RunnerError("--max-context-chars must be 0 or a positive integer")

    if mode == "full":
        parts = [
            f"\n\n===== {document.rel_path} =====\n{document.text.rstrip()}\n"
            for document in documents
        ]
        text = "".join(parts).strip()
        if max_context_chars and len(text) > max_context_chars:
            raise RunnerError(
                "Full attachment context exceeds --max-context-chars; "
                "increase the limit or use --context-mode lexical"
            )
        files = [document.rel_path for document in documents]
        return ContextBundle(
            text=text,
            files=files,
            digest=digest_text(text),
            mode=mode,
            char_count=len(text),
            chunk_count=len(documents),
            context_source_glob=context_source_glob,
            context_root=context_root,
        )

    if mode != "lexical":
        raise RunnerError(f"Unknown context mode: {mode}")

    query_tokens = tokenize_query(projection)
    scored_chunks: list[tuple[int, ContextChunk]] = []
    for chunk in context_chunks:
        scored_chunks.append((score_chunk(chunk, query_tokens), chunk))

    scored_chunks.sort(key=lambda item: (-item[0], item[1].rel_path, item[1].heading))
    selected: list[ContextChunk] = []
    selected_size = 0
    budget = max_context_chars or sum(len(item.text) for _, item in scored_chunks)
    for score, chunk in scored_chunks:
        if score <= 0 and selected:
            continue
        header = f"\n\n===== {chunk.rel_path} :: {chunk.heading} =====\n"
        candidate_size = len(header) + len(chunk.text) + 1
        if candidate_size > budget and not selected:
            remaining = max(budget - len(header) - 1, 0)
            selected.append(
                make_context_chunk(chunk.rel_path, chunk.heading, chunk.text[:remaining].rstrip())
            )
            selected_size = budget
            break
        if selected_size + candidate_size > budget:
            continue
        selected.append(make_context_chunk(chunk.rel_path, chunk.heading, chunk.text.rstrip()))
        selected_size += candidate_size
        if selected_size >= budget:
            break

    if not selected and scored_chunks:
        _, chunk = scored_chunks[0]
        selected.append(
            make_context_chunk(chunk.rel_path, chunk.heading, chunk.text[:budget].rstrip())
        )

    if not selected:
        raise RunnerError("No context chunks were selected")

    parts = [
        f"\n\n===== {chunk.rel_path} :: {chunk.heading} =====\n{chunk.text}\n"
        for chunk in selected
    ]
    text = "".join(parts).strip()
    files = sorted({chunk.rel_path for chunk in selected})
    return ContextBundle(
        text=text,
        files=files,
        digest=digest_text(text),
        mode=mode,
        char_count=len(text),
        chunk_count=len(selected),
        context_source_glob=context_source_glob,
        context_root=context_root,
    )


def load_instruction_draft(manifest: dict[str, Any]) -> tuple[str | None, str | None]:
    answer_generation = manifest.get("answer_generation", {})
    if not answer_generation.get("include_gpt_instruction_draft"):
        return None, None
    draft_path_text = answer_generation.get("gpt_instruction_draft_path")
    if not draft_path_text:
        raise RunnerError("GPT instruction draft is enabled but no path is configured")
    draft_path = resolve_repo_path(draft_path_text, "gpt_instruction_draft_path")
    if not draft_path.exists():
        raise RunnerError(f"GPT instruction draft path does not exist: {draft_path_text}")
    return repo_rel(draft_path), draft_path.read_text(encoding="utf-8")


def language_instruction(projection: dict[str, Any]) -> str:
    requested = projection.get("requested_language")
    if requested:
        return (
            f"Answer in the requested language '{requested}'. Preserve literal technical "
            "tokens exactly as written."
        )
    return "Answer in English. Preserve literal technical tokens exactly as written."


def build_prompt(
    projection: dict[str, Any],
    context: ContextBundle,
    draft_text: str | None,
) -> tuple[str, str]:
    instruction_parts = [
        "You are answering an Altibase benchmark question.",
        "Use only the benchmark context included in this request.",
        "Do not use outside knowledge or repository files not included in the context.",
        language_instruction(projection),
        (
            "Keep SQL object names, SQL keywords used as syntax, function names, "
            "property names, error codes, commands, paths, package/class/method/API "
            "names, connector names, and version labels literal."
        ),
        (
            "If the benchmark context is not enough for a safe answer, ask for the "
            "missing version, environment, log excerpt, patch level, or object "
            "definition needed, and give the safest next check supported by the "
            "benchmark context."
        ),
    ]
    if draft_text is not None:
        instruction_parts.append("Manifest-selected GPT instruction draft follows.")
        instruction_parts.append(draft_text)

    projected_json = json.dumps(projection, ensure_ascii=False, indent=2, sort_keys=True)
    scaffold = "\n\n".join(instruction_parts) + f"\n\nAllowed question input:\n{projected_json}"
    prompt = f"{scaffold}\n\nAttachment context:\n{context.text}"
    return prompt, scaffold


def recursive_payload_key_leaks(value: Any, judge_only: set[str], path: str = "$") -> list[str]:
    failures: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            if key in judge_only:
                failures.append(f"request payload contains judge-only key at {child_path}")
            failures.extend(recursive_payload_key_leaks(child, judge_only, child_path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            failures.extend(recursive_payload_key_leaks(child, judge_only, f"{path}[{index}]"))
    return failures


def quoted_key_leaks(text: str, judge_only: set[str], label: str) -> list[str]:
    failures: list[str] = []
    for key in sorted(judge_only):
        pattern = re.compile(rf"([\"']){re.escape(key)}\1\s*:")
        if pattern.search(text):
            failures.append(f"{label} contains JSON-like judge-only key {key}")
    return failures


def scaffold_label_leaks(scaffold: str, judge_only: set[str]) -> list[str]:
    failures: list[str] = []
    for key in sorted(judge_only):
        pattern = re.compile(rf"(?im)^\s*{re.escape(key)}\s*:")
        if pattern.search(scaffold):
            failures.append(f"prompt scaffold contains judge-only label {key}")
    return failures


def run_leakage_check(
    projection: dict[str, Any],
    request_payload: dict[str, Any],
    prompt_text: str,
    prompt_scaffold: str,
    policy: dict[str, Any],
) -> dict[str, Any]:
    judge_only = set(policy.get("judge_only_question_fields", []))
    failures: list[str] = []

    leaked_projection = sorted(set(projection) & judge_only)
    if leaked_projection:
        failures.append(f"projected input contains judge-only keys: {', '.join(leaked_projection)}")

    failures.extend(recursive_payload_key_leaks(request_payload, judge_only))
    # Source context is root-allowlisted and may legitimately contain JSON-like source text.
    failures.extend(quoted_key_leaks(prompt_scaffold, judge_only, "prompt scaffold"))
    failures.extend(scaffold_label_leaks(prompt_scaffold, judge_only))

    return {
        "passed": not failures,
        "judge_only_keys_checked": sorted(judge_only),
        "failures": failures,
    }


def build_request_payload(provider: str, model: str, mode: str, prompt_text: str) -> dict[str, Any]:
    if provider in {"openai", "openai_responses"}:
        return {
            "model": model,
            "input": prompt_text,
        }
    if provider == "command":
        return {
            "provider": "command",
            "model": model,
            "stdin": prompt_text,
            "mode": mode,
        }
    return {
        "provider": provider,
        "model": model,
        "input": prompt_text,
        "mode": mode,
    }


def offline_fixture_answer(
    projection: dict[str, Any],
    context: ContextBundle,
    max_preview_chars: int,
) -> ProviderResult:
    preview = context.text[:max_preview_chars].rstrip()
    answer = (
        f"Offline fixture answer for {projection['id']}. No live model call was made.\n\n"
        f"Question: {projection['question']}\n\n"
        "Allowlisted context was built and leakage checks passed. "
        f"Selected context files: {', '.join(context.files)}.\n\n"
        f"Context preview:\n{preview}"
    )
    return ProviderResult(
        status="answered",
        answer=answer,
        usage={
            "offline_fixture": "true",
            "context_mode": context.mode,
            "context_characters": context.char_count,
            "context_chunks": context.chunk_count,
            "attachment_file_count": len(context.files),
            "context_file_count": len(context.files),
        },
    )


def command_answer(command: str | None, prompt_text: str, timeout_seconds: int) -> ProviderResult:
    if not command:
        return ProviderResult(
            status="error",
            answer="",
            usage={},
            error="provider=command requires --provider-command",
        )
    try:
        completed = subprocess.run(
            shlex.split(command),
            input=prompt_text,
            text=True,
            capture_output=True,
            timeout=timeout_seconds,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return ProviderResult(status="error", answer="", usage={}, error=str(exc))

    usage = {"exit_code": completed.returncode}
    if completed.returncode != 0:
        error_text = completed.stderr.strip() or f"command exited with {completed.returncode}"
        return ProviderResult(status="error", answer=completed.stdout, usage=usage, error=error_text)
    return ProviderResult(status="answered", answer=completed.stdout, usage=usage)


def openai_answer(model: str, prompt_text: str) -> ProviderResult:
    try:
        from openai import OpenAI  # type: ignore[import-not-found]
    except ImportError:
        return ProviderResult(
            status="error",
            answer="",
            usage={},
            error="provider=openai requires the openai Python package",
        )
    if not os.environ.get("OPENAI_API_KEY"):
        return ProviderResult(
            status="error",
            answer="",
            usage={},
            error="provider=openai requires OPENAI_API_KEY",
        )

    try:
        client = OpenAI()
        response = client.responses.create(model=model, input=prompt_text)
    except Exception as exc:  # pragma: no cover - live provider path
        return ProviderResult(status="error", answer="", usage={}, error=str(exc))

    answer = getattr(response, "output_text", "")
    usage: dict[str, int | float | str | None] = {}
    raw_usage = getattr(response, "usage", None)
    if raw_usage is not None:
        if hasattr(raw_usage, "model_dump"):
            raw_usage = raw_usage.model_dump()
        if isinstance(raw_usage, dict):
            for key, value in raw_usage.items():
                if isinstance(value, (int, float, str)) or value is None:
                    usage[key] = value
    return ProviderResult(status="answered", answer=answer or "", usage=usage)


def run_provider(
    provider: str,
    model: str,
    mode: str,
    prompt_text: str,
    context: ContextBundle,
    projection: dict[str, Any],
    args: argparse.Namespace,
) -> ProviderResult:
    if mode == "dry_run":
        return ProviderResult(
            status="skipped",
            answer="Dry run: projection, allowlisted context, and leakage checks passed.",
            usage={
                "context_mode": context.mode,
                "context_characters": context.char_count,
                "context_chunks": context.chunk_count,
                "attachment_file_count": len(context.files),
                "context_file_count": len(context.files),
            },
        )
    if mode == "offline_fixture":
        return offline_fixture_answer(projection, context, args.offline_preview_chars)
    if mode != "live":
        return ProviderResult(status="error", answer="", usage={}, error=f"Unsupported mode: {mode}")

    if provider == "command":
        return command_answer(args.provider_command, prompt_text, args.provider_timeout_seconds)
    if provider in {"openai", "openai_responses"}:
        return openai_answer(model, prompt_text)
    return ProviderResult(
        status="error",
        answer="",
        usage={},
        error=f"Unsupported live provider: {provider}",
    )


def answer_record(
    run_id: str,
    manifest: dict[str, Any],
    projection: dict[str, Any],
    provider: str,
    model: str,
    mode: str,
    context: ContextBundle,
    draft_path: str | None,
    leakage_check: dict[str, Any],
    prompt_text: str,
    request_payload: dict[str, Any],
    result: ProviderResult,
) -> dict[str, Any]:
    attachment_context: dict[str, Any] = {
        "attachment_files": context.files,
        "context_digest": context.digest,
        "context_source_glob": context.context_source_glob,
        "context_root": context.context_root,
    }
    if draft_path:
        attachment_context["gpt_instruction_draft_path"] = draft_path

    record: dict[str, Any] = {
        "$schema": "../schemas/answer_record.schema.json",
        "run_id": run_id,
        "manifest_id": manifest["manifest_id"],
        "question_id": projection["id"],
        "generated_at": utc_now(),
        "provider": provider,
        "model": model,
        "mode": mode,
        "status": result.status,
        "answering_input": projection,
        "attachment_context": attachment_context,
        "leakage_check": leakage_check,
        "prompt_audit": {
            "prompt_digest": digest_text(prompt_text),
            "request_payload_digest": digest_text(canonical_json(request_payload)),
            "projected_input_digest": digest_text(canonical_json(projection)),
        },
        "answer": result.answer,
        "usage": result.usage,
    }
    if result.error:
        record["error"] = result.error
    return record


def load_answer_record_validator() -> Any | None:
    try:
        from jsonschema import Draft202012Validator, FormatChecker
    except ImportError:
        return None
    schema = load_json(SCHEMA_DIR / "answer_record.schema.json")
    return Draft202012Validator(schema, format_checker=FormatChecker())


def validate_answer_record(record: dict[str, Any], validator: Any | None) -> list[str]:
    if validator is None:
        return ["jsonschema is not installed; cannot validate answer record schema"]
    return [error.message for error in sorted(validator.iter_errors(record), key=lambda item: list(item.path))]


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def filter_questions(
    questions: list[dict[str, Any]],
    question_ids: list[str] | None,
    limit: int | None,
) -> list[dict[str, Any]]:
    selected = questions
    if question_ids:
        wanted = set(question_ids)
        selected = [record for record in selected if record.get("id") in wanted]
        missing = sorted(wanted - {record.get("id") for record in selected})
        if missing:
            raise RunnerError(f"Requested question id(s) not found: {', '.join(missing)}")
    if limit is not None:
        selected = selected[:limit]
    if not selected:
        raise RunnerError("No questions selected")
    return selected


def run_self_test(policy_path: Path) -> int:
    policy = load_json(policy_path)
    judge_only = set(policy.get("judge_only_question_fields", []))
    projection = {
        "id": "PROP-001",
        "question": "What does MEM_MAX_DB_SIZE control?",
        "version_scope": "7.3",
        "user_level": "advanced_operator",
        "answer_type": "reference",
        "answer_language": "en",
    }
    payload = build_request_payload("offline", "fixture", "offline_fixture", "Prompt")
    clean = run_leakage_check(projection, payload, "Allowed question input: {}", "Allowed question input: {}", policy)
    if not clean["passed"]:
        print(f"SELF-TEST FAILED: clean projection leaked: {clean['failures']}", file=sys.stderr)
        return 1

    dirty_payload = {"model": "fixture", "expected_facts": []}
    dirty_prompt = 'Allowed question input:\n{"expected_facts":[]}'
    dirty = run_leakage_check(projection, dirty_payload, dirty_prompt, dirty_prompt, policy)
    if dirty["passed"] or "expected_facts" not in " ".join(dirty["failures"]):
        print("SELF-TEST FAILED: leakage check did not catch expected_facts", file=sys.stderr)
        return 1

    missing = {"domain", "expected_facts", "required_tokens"} - judge_only
    if missing:
        print(f"SELF-TEST FAILED: policy missing expected judge-only keys: {missing}", file=sys.stderr)
        return 1

    print("OK: answer runner self-test passed")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, help="Benchmark manifest JSON path.")
    parser.add_argument(
        "--policy",
        type=Path,
        default=BENCHMARK_ROOT / "policy.json",
        help="Benchmark policy JSON path.",
    )
    parser.add_argument("--run-id", help="Stable run id. Defaults to timestamp plus manifest id.")
    parser.add_argument("--output-dir", type=Path, help="Directory for answers.jsonl and run.json.")
    parser.add_argument("--mode", choices=["dry_run", "offline_fixture", "live"], help="Override manifest mode.")
    parser.add_argument("--provider", help="Override manifest answer_generation.provider.")
    parser.add_argument("--model", help="Override manifest answer_generation.model.")
    parser.add_argument("--provider-command", help="Command used when provider=command and mode=live.")
    parser.add_argument("--provider-timeout-seconds", type=int, default=300)
    parser.add_argument("--question-id", action="append", help="Run one question id. May be repeated.")
    parser.add_argument("--limit", type=int, help="Limit selected questions after filtering.")
    parser.add_argument(
        "--context-mode",
        choices=["lexical", "full"],
        default="lexical",
        help="Use lexical attachment chunk selection or full attachment context.",
    )
    parser.add_argument(
        "--max-context-chars",
        type=int,
        default=180_000,
        help="Maximum attachment context characters. Use 0 for unlimited.",
    )
    parser.add_argument("--chunk-chars", type=int, default=8_000)
    parser.add_argument("--offline-preview-chars", type=int, default=2_000)
    parser.add_argument("--validate-output", action="store_true", help="Validate answer records against schema.")
    parser.add_argument("--self-test", action="store_true", help="Run leakage-check self-test and exit.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    policy_path = args.policy if args.policy.is_absolute() else (REPO_ROOT / args.policy)

    try:
        if args.self_test:
            return run_self_test(policy_path.resolve())

        if not args.manifest:
            raise RunnerError("--manifest is required unless --self-test is used")

        manifest_path = args.manifest if args.manifest.is_absolute() else (REPO_ROOT / args.manifest)
        policy = load_json(policy_path.resolve())
        manifest = load_json(manifest_path.resolve())
        context_root = validate_runner_policy(manifest, policy)

        answer_generation = manifest.get("answer_generation", {})
        mode = args.mode or answer_generation.get("mode") or "dry_run"
        provider = args.provider or answer_generation.get("provider") or "offline"
        model = args.model or answer_generation.get("model") or "fixture"
        run_id = args.run_id or f"{dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ')}_{manifest['manifest_id']}"

        if args.limit is not None and args.limit < 1:
            raise RunnerError("--limit must be a positive integer")
        if args.chunk_chars < 512:
            raise RunnerError("--chunk-chars must be at least 512")

        output_dir = args.output_dir
        if output_dir is None:
            output_dir = resolve_repo_path(
                manifest.get("reporting", {}).get("output_dir", "evals/altibase_answerability/reports")
                + f"/runs/{run_id}",
                "output_dir",
            )
        elif not output_dir.is_absolute():
            output_dir = (REPO_ROOT / output_dir).resolve()
        output_dir.mkdir(parents=True, exist_ok=True)

        questions = filter_questions(load_questions(manifest), args.question_id, args.limit)
        context_source_glob = answer_generation["attachment_glob"]
        documents = load_attachment_documents(context_source_glob, context_root)
        context_chunks = collect_markdown_chunks(documents, args.chunk_chars)
        draft_path, draft_text = load_instruction_draft(manifest)
        validator = load_answer_record_validator() if args.validate_output else None

        answer_path = output_dir / "answers.jsonl"
        records_written = 0
        error_count = 0
        with answer_path.open("w", encoding="utf-8") as answer_handle:
            for question in questions:
                projection = project_question(question, manifest, policy)
                context = build_context(
                    documents,
                    context_chunks,
                    projection,
                    args.context_mode,
                    args.max_context_chars,
                    context_source_glob,
                    context_root,
                )
                prompt_text, prompt_scaffold = build_prompt(projection, context, draft_text)
                request_payload = build_request_payload(provider, model, mode, prompt_text)
                leakage_check = run_leakage_check(
                    projection,
                    request_payload,
                    prompt_text,
                    prompt_scaffold,
                    policy,
                )
                if leakage_check["passed"]:
                    result = run_provider(provider, model, mode, prompt_text, context, projection, args)
                else:
                    result = ProviderResult(
                        status="error",
                        answer="",
                        usage={},
                        error="leakage check failed; no provider call was made",
                    )

                record = answer_record(
                    run_id,
                    manifest,
                    projection,
                    provider,
                    model,
                    mode,
                    context,
                    draft_path,
                    leakage_check,
                    prompt_text,
                    request_payload,
                    result,
                )
                if args.validate_output:
                    validation_errors = validate_answer_record(record, validator)
                    if validation_errors:
                        record["status"] = "error"
                        record["error"] = "answer record schema validation failed: " + "; ".join(
                            validation_errors
                        )
                        error_count += 1
                if result.status == "error" or not leakage_check["passed"]:
                    error_count += 1

                answer_handle.write(canonical_json(record) + "\n")
                records_written += 1

        run_summary = {
            "run_id": run_id,
            "manifest_id": manifest["manifest_id"],
            "generated_at": utc_now(),
            "mode": mode,
            "provider": provider,
            "model": model,
            "context_mode": args.context_mode,
            "answer_records": records_written,
            "errors": error_count,
            "answers_path": repo_rel(answer_path),
            "attachment_glob": answer_generation["attachment_glob"],
            "context_source_glob": context_source_glob,
            "context_root": context_root,
        }
        write_json(output_dir / "run.json", run_summary)

    except RunnerError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(
        f"OK: wrote {records_written} answer record(s) to {repo_rel(answer_path)} "
        f"(errors={error_count})"
    )
    return 1 if error_count else 0


if __name__ == "__main__":
    raise SystemExit(main())
