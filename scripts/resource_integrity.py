"""Validate the skill's resource integrity; does not certify that reading occurred."""
import argparse
import hashlib
import json
import re
from datetime import date
from pathlib import Path, PureWindowsPath
from urllib.parse import unquote, urlsplit

def nonempty_text(value):
    return isinstance(value, str) and bool(value.strip())


def canonical_doi(value):
    if not isinstance(value, str):
        return ""
    value = re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", "", value.strip(), flags=re.I)
    value = unquote(value).lower()
    return value if re.fullmatch(r"10\.\d{4,9}/\S+", value) else ""


def inside_root(path, root):
    try:
        path.resolve().relative_to(root)
        return True
    except (ValueError, OSError, RuntimeError):
        return False


def relative_file(base, value, root, label, errors, allow_directory=False):
    if not nonempty_text(value):
        errors.append(f"{label}: missing relative file path")
        return None
    windows_path = PureWindowsPath(value)
    if Path(value).is_absolute() or windows_path.drive or windows_path.root:
        errors.append(f"{label}: file path must be relative to its resource directory")
        return None
    candidate = base / value
    if not inside_root(candidate, root):
        errors.append(f"{label}: file path escapes the skill directory")
        return None
    try:
        if not (candidate.exists() if allow_directory else candidate.is_file()):
            errors.append(f"{label}: missing file {value}")
            return None
    except OSError as exc:
        errors.append(f"{label}: cannot inspect file: {exc}")
        return None
    return candidate


def read_text(path, root, label, errors):
    if not inside_root(path, root):
        errors.append(f"{label}: resource resolves outside the skill directory")
        return None
    try:
        return path.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as exc:
        errors.append(f"{label}: cannot read resource: {exc}")
        return None


def read_json(path, root, label, errors):
    content = read_text(path, root, label, errors)
    if content is not None:
        try:
            return json.loads(content)
        except ValueError as exc:
            errors.append(f"{label}: invalid JSON: {exc}")
    return None


def check_note(paper, directory, root, label, errors):
    path = relative_file(directory, paper.get("note"), root, f"{label} reading note", errors)
    if path:
        content = read_text(path, root, f"{label} reading note", errors)
        if content is not None and len(content.strip()) < 300:
            errors.append(f"{label}: individual reading note must contain at least 300 characters")


def check_read_record(paper, label, errors, cache_hashes, require_read=False):
    full = paper.get("full_text", {})
    if not isinstance(full, dict):
        errors.append(f"{label}: full_text must be an object")
        return False
    if "status" in full and not nonempty_text(full["status"]):
        errors.append(f"{label}: full_text status must be a nonempty string")
    if full.get("status") != "read":
        if require_read:
            errors.append(f"{label}: full-text reading is not marked complete")
        return False
    for field in ("url", "version", "format", "read_scope", "read_at"):
        if not nonempty_text(full.get(field)):
            errors.append(f"{label}: read record missing valid {field}")
    if isinstance(full.get("format"), str) and full["format"].lower() == "pdf":
        if type(full.get("pages")) is not int or full["pages"] < 1:
            errors.append(f"{label}: read PDF record needs a positive integer page count")
    if nonempty_text(full.get("url")):
        try:
            source = urlsplit(full["url"])
            if source.scheme not in {"http", "https"} or not source.netloc:
                raise ValueError("expected an HTTP(S) source URL")
        except ValueError:
            errors.append(f"{label}: invalid full-text source URL")
    if nonempty_text(full.get("read_at")):
        try:
            date.fromisoformat(full["read_at"])
        except ValueError:
            errors.append(f"{label}: read_at must be an ISO calendar date")
    scope = full.get("hash_scope")
    if scope is not None and (not isinstance(scope, str) or scope not in {"source_bytes", "source", "extracted_text"}):
        errors.append(f"{label}: unrecognized source hash scope")
    source_digest, extracted_digest = full.get("sha256"), full.get("extracted_text_sha256")
    if not source_digest and (not extracted_digest or scope != "extracted_text"):
        errors.append(f"{label}: missing source-byte hash requires an explicit extracted_text hash scope")
    if scope == "extracted_text" and not extracted_digest:
        errors.append(f"{label}: extracted_text hash scope requires extracted_text_sha256")
    for field, digest in (("sha256", source_digest), ("extracted_text_sha256", extracted_digest)):
        if digest is None or digest == "":
            continue
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            errors.append(f"{label}: invalid {field}")
    digest = source_digest or extracted_digest
    if isinstance(digest, str) and re.fullmatch(r"[0-9a-f]{64}", digest):
        if cache_hashes is not None and digest not in cache_hashes:
            errors.append(f"{label}: source SHA256 absent from supplied research cache")
    return True
