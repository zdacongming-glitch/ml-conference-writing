"""Check conference corpus identity and evidence records; not a reading certification."""
import argparse
import hashlib
import json
import re
from datetime import date
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlsplit, urlunsplit

from resource_integrity import (canonical_doi, check_note, check_read_record, inside_root,
                                nonempty_text, read_json, read_text, relative_file)

CONFERENCES = ("icml", "iclr", "neurips")
CONTRIBUTION_TYPES = {"methods", "theory", "empirical-study", "negative-results",
                      "datasets-benchmarks", "systems", "position"}
TRACKS = {"main", "position", "datasets-benchmarks", "workshop", "other"}


def canonical_url(value):
    if not nonempty_text(value):
        return ""
    try:
        url = urlsplit(value.strip())
        if url.scheme not in {"https", "http"} or not url.netloc:
            return ""
        return urlunsplit(("https", url.netloc.lower(), unquote(url.path).rstrip("/"), url.query, ""))
    except ValueError:
        return ""


def identity_keys(paper):
    """Identity aliases connect versions; DOI is optional for ML proceedings."""
    keys = set()
    if nonempty_text(paper.get("work_id")):
        keys.add("work:" + paper["work_id"].strip())
    publication = canonical_url(paper.get("publication_url"))
    if publication:
        keys.add("publication:" + publication)
    identifiers = paper.get("identifiers", {})
    if not isinstance(identifiers, dict):
        return keys
    doi = canonical_doi(identifiers.get("doi"))
    if doi:
        keys.add("doi:" + doi)
    arxiv = identifiers.get("arxiv")
    if nonempty_text(arxiv):
        arxiv = re.sub(r"^https?://(?:www\.)?arxiv\.org/(?:abs|pdf)/|^arxiv:\s*", "", arxiv.strip(), flags=re.I)
        arxiv = re.sub(r"v\d+$", "", arxiv.removesuffix(".pdf"))
        keys.add("arxiv:" + arxiv.lower())
    forum = identifiers.get("openreview")
    if nonempty_text(forum):
        if forum.startswith(("https://", "http://")):
            try:
                forum = parse_qs(urlsplit(forum).query).get("id", [forum])[0]
            except ValueError:
                forum = ""
        if forum:
            keys.add("openreview:" + forum.strip())
    proceedings = canonical_url(identifiers.get("proceedings_url"))
    if proceedings:
        keys.add("publication:" + proceedings)
    return keys


def check_markdown(root, errors):
    for path in root.rglob("*.md"):
        if any(part in {".git", "__pycache__"} for part in path.relative_to(root).parts):
            continue
        label = path.relative_to(root).as_posix()
        text = read_text(path, root, label, errors)
        if text is None:
            continue
        prose = re.sub(r"```[^\n]*\n.*?```", "", text, flags=re.S)
        prose = re.sub(r"`[^`\n]*`", "", prose)
        if re.search(r"\\[()\[\]]", prose):
            errors.append(f"{label}: disallowed Markdown math delimiter")
        delimiters = [line for line in prose.splitlines() if "$$" in line]
        if any(line.strip() != "$$" for line in delimiters) or len(delimiters) % 2:
            errors.append(f"{label}: display math needs paired delimiters on separate lines")
        if re.search(r"(?:[A-Za-z]:[\\/]Users[\\/]|/Users/|/home/)[^\s]+", prose):
            errors.append(f"{label}: personal absolute path in shared prose")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if re.match(r"^(?:https?://|mailto:|#)", target, flags=re.I):
                continue
            destination = unquote(target.split("#", 1)[0].strip("<>"))
            if destination:
                relative_file(path.parent, destination, root, f"{label} link", errors, allow_directory=True)


def paper_types(paper):
    values = paper.get("contribution_types", [paper.get("contribution_type")])
    return set(values) if isinstance(values, list) and all(isinstance(v, str) for v in values) else set()


def check_paper(paper, directory, root, conference, errors, cache_hashes,
                require_read=False, minimum_year=2000, require_main=False):
    if not isinstance(paper, dict):
        errors.append(f"{conference}: paper record must be an object")
        return False
    ident = paper.get("id", "?")
    label = str(ident)
    for field in ("id", "work_id", "title", "selection_reason", "publication_url"):
        if not nonempty_text(paper.get(field)):
            errors.append(f"{label}: missing nonempty {field}")
    if not canonical_url(paper.get("publication_url")):
        errors.append(f"{label}: publication_url must identify a public HTTP(S) record")
    authors = paper.get("authors")
    if not isinstance(authors, list) or not authors or any(not nonempty_text(a) for a in authors):
        errors.append(f"{label}: authors must be a nonempty list of names")
    if paper.get("conference_id") != conference:
        errors.append(f"{label}: conference_id does not match the corpus")
    year = paper.get("year")
    if type(year) is not int or not minimum_year <= year <= date.today().year:
        errors.append(f"{label}: formal publication year outside supported range")
    if not isinstance(paper.get("track"), str) or paper["track"] not in TRACKS:
        errors.append(f"{label}: track must use a supported stable ID")
    if require_main and paper.get("track") != "main":
        errors.append(f"{label}: initial core/calibration corpus requires verified main-track papers")
    types = paper_types(paper)
    if (not types or not types <= CONTRIBUTION_TYPES or not isinstance(paper.get("contribution_type"), str)
            or paper["contribution_type"] not in types):
        errors.append(f"{label}: unsupported contribution type or type labels")
    if not isinstance(paper.get("topics"), list) or not paper["topics"] or any(not nonempty_text(t) for t in paper["topics"]):
        errors.append(f"{label}: topics must contain descriptive labels")
    identifiers = paper.get("identifiers")
    if not isinstance(identifiers, dict):
        errors.append(f"{label}: identifiers must be an object; DOI may be absent")
    else:
        for key, value in identifiers.items():
            if value is not None and not nonempty_text(value):
                errors.append(f"{label}: identity alias {key} must be a nonempty string or null")
        if identifiers.get("doi") and not canonical_doi(identifiers["doi"]):
            errors.append(f"{label}: invalid DOI alias")
    evidence = paper.get("recognition_evidence")
    if not isinstance(evidence, list) or not evidence:
        errors.append(f"{label}: selection needs recorded recognition/evidence sources")
    else:
        for item in evidence:
            if not isinstance(item, dict) or not canonical_url(item.get("url")) or not nonempty_text(item.get("note")):
                errors.append(f"{label}: recognition evidence needs a source URL and accurate note")
    check_note(paper, directory, root, label, errors)
    return check_read_record(paper, label, errors, cache_hashes, require_read)


def validate(root, require_complete=False, cache_root=None):
    root = Path(root).resolve()
    errors, summaries, topics = [], [], []
    cache_hashes = None
    if cache_root:
        try:
            cache_hashes = {hashlib.sha256(p.read_bytes()).hexdigest() for p in Path(cache_root).rglob("*")
                            if p.is_file() and p.suffix.lower() in {".pdf", ".txt", ".html", ".htm", ".xml"}}
        except OSError as exc:
            errors.append(f"research cache: {exc}")
    check_markdown(root, errors)
    papers, locations, identity_owner = {}, {}, {}

    def register(paper, conference, label, allow_reuse=False):
        if not isinstance(paper, dict) or not nonempty_text(paper.get("id")):
            return
        ident = paper["id"]
        previous = papers.get(ident)
        if previous:
            if not allow_reuse or previous.get("work_id") != paper.get("work_id") or locations[ident] != conference:
                errors.append(f"{label}: duplicate/conflicting paper ID {ident}")
        else:
            papers[ident], locations[ident] = paper, conference
        for key in identity_keys(paper):
            if key in identity_owner and identity_owner[key] != ident:
                errors.append(f"{label}: duplicate work/version alias {key}; reuse {identity_owner[key]}")
            identity_owner[key] = ident

    base = root / "references" / "conferences"
    for conference in CONFERENCES:
        directory = base / conference
        summary = {"conference_id": conference, "papers": 0, "read": 0, "calibration_papers": 0, "calibration_read": 0}
        for kind, count in (("core", 35), ("calibration", 2)):
            path = directory / f"{kind}-corpus.json"
            if not path.exists():
                if require_complete:
                    errors.append(f"{conference}: missing {kind} corpus")
                continue
            corpus = read_json(path, root, f"{conference} {kind} corpus", errors)
            if not isinstance(corpus, dict) or not isinstance(corpus.get("papers"), list):
                errors.append(f"{conference} {kind}: expected an object with papers list")
                continue
            if corpus.get("conference_id") != conference:
                errors.append(f"{conference} {kind}: conference_id mismatch")
            if type(corpus.get("schema_version")) is not int or corpus["schema_version"] != 1:
                errors.append(f"{conference} {kind}: unsupported schema_version")
            records = corpus["papers"]
            if require_complete and (len(records) != count if kind == "core" else len(records) < count):
                errors.append(f"{conference}: expected {count} {kind} papers, found {len(records)}")
            relative_file(directory, "guide.md", root, f"{conference} guide", errors)
            read = 0
            for paper in records:
                read += int(check_paper(paper, directory, root, conference, errors, cache_hashes,
                                       require_complete, 2023 if kind == "calibration" else 2013 if conference == "iclr" else 2000,
                                       require_main=True))
                register(paper, conference, f"{conference} {kind}")
            summary["papers" if kind == "core" else "calibration_papers"] = len(records)
            summary["read" if kind == "core" else "calibration_read"] = read
        summaries.append(summary)

    topic_records = []
    for directory in sorted(base.glob("*/topics/*")):
        label = directory.relative_to(root).as_posix()
        if not directory.is_dir() or not inside_root(directory, root):
            errors.append(f"{label}: invalid topic directory")
            continue
        conference = directory.parents[1].name
        for name in ("profile.md", "corpus.json", "terms.json"):
            relative_file(directory, name, root, f"{label} {name}", errors)
        terms = read_json(directory / "terms.json", root, f"{label} terms", errors)
        if not isinstance(terms, (dict, list)):
            errors.append(f"{label}: terms must be a JSON object or array")
        topic = read_json(directory / "corpus.json", root, f"{label} corpus", errors)
        if not isinstance(topic, dict):
            errors.append(f"{label}: corpus must be a JSON object")
            continue
        topic_records.append((directory, conference, label, topic))
        extra = topic.get("additional_papers", [])
        if not isinstance(extra, list):
            errors.append(f"{label}: additional_papers must be a list")
            continue
        local_ids = set()
        for paper in extra:
            actual_conference = paper.get("conference_id") if isinstance(paper, dict) else None
            if not nonempty_text(actual_conference):
                errors.append(f"{label}: additional paper needs its actual conference_id")
                actual_conference = conference
            check_paper(paper, directory, root, actual_conference, errors, cache_hashes, minimum_year=1)
            if isinstance(paper, dict) and nonempty_text(paper.get("id")):
                if paper["id"] in local_ids:
                    errors.append(f"{label}: repeated additional paper ID")
                local_ids.add(paper["id"])
            register(paper, actual_conference, label, allow_reuse=True)

    for directory, conference, label, topic in topic_records:
        if type(topic.get("schema_version")) is not int or topic["schema_version"] != 1:
            errors.append(f"{label}: unsupported schema_version")
        if conference not in CONFERENCES or topic.get("conference_id", conference) != conference:
            errors.append(f"{label}: target conference mismatch")
        status, target_type, track = topic.get("status"), topic.get("contribution_type"), topic.get("track")
        if status not in ("provisional", "complete"):
            errors.append(f"{label}: status must be provisional or complete")
        if not isinstance(target_type, str) or target_type not in CONTRIBUTION_TYPES:
            errors.append(f"{label}: unsupported target contribution_type")
        if not isinstance(track, str) or track not in TRACKS:
            errors.append(f"{label}: target track must be explicit")
        evidence = topic.get("type_evidence", {})
        if not isinstance(evidence, dict):
            errors.append(f"{label}: type_evidence must be an object")
            evidence = {}
        primary = topic.get("paper_ids", [])
        supplementary = topic.get("supplementary_paper_ids", [])
        for name, ids in (("paper_ids", primary), ("supplementary_paper_ids", supplementary)):
            if not isinstance(ids, list) or any(not nonempty_text(i) for i in ids):
                errors.append(f"{label}: {name} must be a list of IDs")
            elif len(ids) != len(set(ids)):
                errors.append(f"{label}: duplicate IDs in {name}")
        if not isinstance(primary, list) or not isinstance(supplementary, list) or any(not nonempty_text(i) for i in primary + supplementary):
            continue
        if set(primary) & set(supplementary):
            errors.append(f"{label}: primary and supplementary lists overlap")
        read_works = set()
        for ident in primary + supplementary:
            paper = papers.get(ident)
            if not paper:
                errors.append(f"{label}: unknown paper ID {ident}")
                continue
            if ident in supplementary:
                continue
            match = evidence.get(ident, {})
            if not isinstance(match, dict) or not nonempty_text(match.get("basis")) or match.get("contribution_type") != target_type:
                if status == "complete":
                    errors.append(f"{label} {ident}: complete profile needs matching contribution-type evidence")
                continue
            if locations[ident] != conference or paper.get("track") != track or target_type not in paper_types(paper):
                if status == "complete":
                    errors.append(f"{label} {ident}: conference, track or contribution type does not match")
                continue
            full = paper.get("full_text", {})
            if isinstance(full, dict) and full.get("status") == "read" and nonempty_text(paper.get("work_id")):
                read_works.add(paper["work_id"])
        if status == "complete" and len(read_works) < 10:
            errors.append(f"{label}: complete profile requires ten distinct read works matching conference, topic, track and contribution type")
        topics.append({"path": label, "status": status, "matching_read_papers": len(read_works)})
    return {"ok": not errors, "conferences": summaries, "topics": topics, "errors": errors,
            "limitation": "Integrity checks cannot establish actual full-text reading, semantic topic relevance, accurate track/type judgments, or sound writing rules. Review the cited evidence."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--require-complete", action="store_true")
    parser.add_argument("--cache-root", type=Path)
    args = parser.parse_args()
    result = validate(args.root, args.require_complete, args.cache_root)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["ok"] else 1)


if __name__ == "__main__":
    main()
