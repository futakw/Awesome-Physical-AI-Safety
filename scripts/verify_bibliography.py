#!/usr/bin/env python3
"""Verify catalog bibliographic fields against the linked primary source.

The catalog remains hand-curated, but title and first-author surname are always
checked against the paper URL before publication. `year` is checked against it
too, except when `paper_url` is an arXiv/OpenReview preprint and `venue`
already names a different, confirmed venue — that preprint's own year can
legitimately differ from its eventual venue year, so `year` stays
curator-verified against the venue's own listing instead (see
docs/reference/metadata-schema.md#venue-and-year). When the source itself is the venue
record (DOI/Crossref, ACL Anthology, CVF proceedings, etc.), `year` is always
checked against it. Network failures are fatal: an unavailable source is not
evidence that metadata is correct.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import subprocess
import unicodedata
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "papers.json"
USER_AGENT = "Awesome-Physical-AI-Safety bibliography verifier/1.0"


class VerificationError(RuntimeError):
    pass


@dataclass(frozen=True)
class SourceMetadata:
    title: str
    first_author: str | None
    year: int | None
    source_url: str
    first_submission_date: str | None = None


def fetch(url: str, *, accept: str = "text/html,application/xhtml+xml,application/xml") -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": accept})
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return response.read()
    except Exception as exc:  # noqa: BLE001 - preserve source as a blocker
        raise VerificationError(f"could not fetch {url}: {exc}") from exc


def normalize_title(value: str) -> str:
    value = html.unescape(value)
    value = unicodedata.normalize("NFKC", value)
    value = value.replace("–", "-").replace("—", "-").replace("‑", "-")
    value = re.sub(r"\s+", " ", value).strip()
    return value.rstrip(" .;:").casefold()


def surname(value: str) -> str:
    value = html.unescape(value)
    value = re.sub(r"\s+et\s+al\.?\s*$", "", value, flags=re.IGNORECASE).strip()
    value = re.sub(r"\s+", " ", value)
    if "," in value:
        return value.split(",", 1)[0].strip()
    return value.split()[-1].strip(".,") if value else ""


def parse_arxiv_v1_date(text: str) -> str | None:
    """Read the original submission, never the revised date or citation year."""
    block = re.search(r'<div class="submission-history">(.*?)</div>', text, re.S)
    if not block:
        return None
    plain = html.unescape(re.sub(r'<[^>]*>', ' ', block.group(1)))
    match = re.search(r'\[v1\]\s*(?:\w+,\s*)?(\d{1,2}\s+\w+\s+\d{4})\s+\d{2}:\d{2}:\d{2}\s+UTC', plain)
    if not match:
        return None
    try:
        return datetime.strptime(match.group(1), "%d %b %Y").date().isoformat()
    except ValueError:
        return None


def parse_arxiv(url: str) -> SourceMetadata:
    match = re.search(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})(?:v\d+)?", url)
    if not match:
        raise VerificationError(f"unsupported arXiv URL: {url}")
    arxiv_id = match.group(1)
    abs_url = f"https://arxiv.org/abs/{arxiv_id}"
    data = fetch(abs_url)
    text = data.decode("utf-8", errors="replace")
    title_match = re.search(r'<meta name="citation_title" content="([^"]+)"', text)
    authors = re.findall(r'<meta name="citation_author" content="([^"]+)"', text)
    date_match = re.search(r'<meta name="citation_date" content="(\d{4})', text)
    if not title_match:
        raise VerificationError(f"arXiv title not found at {abs_url}")
    return SourceMetadata(
        title=html.unescape(title_match.group(1)),
        first_author=authors[0] if authors else None,
        year=int(date_match.group(1)) if date_match else None,
        source_url=abs_url,
        first_submission_date=parse_arxiv_v1_date(text),
    )


def parse_openreview(url: str) -> SourceMetadata:
    parsed = urllib.parse.urlparse(url)
    query = urllib.parse.parse_qs(parsed.query)
    forum_id = query.get("id", [None])[0]
    if not forum_id:
        raise VerificationError(f"OpenReview URL has no forum id: {url}")
    api_url = "https://api2.openreview.net/notes?id=" + urllib.parse.quote(forum_id)
    try:
        payload = json.loads(fetch(api_url, accept="application/json").decode("utf-8"))
        note = payload["notes"][0]
        content = note.get("content", {})
        title = content.get("title")
        authors = content.get("authors") or []
        if not title:
            raise KeyError("content.title")
        year = None
        for candidate in (content.get("year"), note.get("cdate")):
            if candidate:
                year = int(str(candidate)[:4])
                break
        return SourceMetadata(title, authors[0] if authors else None, year, url)
    except VerificationError:
        raise
    except Exception as exc:  # noqa: BLE001
        raise VerificationError(f"could not parse OpenReview metadata at {api_url}: {exc}") from exc


def meta_content(text: str, name: str) -> list[str]:
    pattern = rf'<meta[^>]+(?:name|property)=["\']{re.escape(name)}["\'][^>]+content=["\']([^"\']+)' \
        rf'|<meta[^>]+content=["\']([^"\']+)["\'][^>]+(?:name|property)=["\']{re.escape(name)}["\']'
    return [html.unescape(a or b) for a, b in re.findall(pattern, text, flags=re.IGNORECASE)]


def proceedings_url_year(url: str) -> int | None:
    """Some proceedings sites stamp pages with a page-publish date rather than
    the conference edition (e.g. a NeurIPS 2025 paper's citation_publication_date
    can read 2026-04-23, the day its camera-ready page went live) — the same
    drift this script otherwise guards against for arXiv. Their URL path
    encodes the actual edition reliably, so prefer that over page metadata."""
    host = urllib.parse.urlparse(url).netloc.casefold()
    if host.endswith("proceedings.neurips.cc"):
        match = re.search(r"/paper(?:_files)?/paper/(\d{4})/", url)
        return int(match.group(1)) if match else None
    if host.endswith("openaccess.thecvf.com"):
        match = re.search(r"/content/[A-Za-z]+(\d{4})/", url)
        return int(match.group(1)) if match else None
    return None


def parse_html_source(url: str) -> SourceMetadata:
    text = fetch(url).decode("utf-8", errors="replace")
    titles = meta_content(text, "citation_title") or meta_content(text, "og:title")
    authors = meta_content(text, "citation_author")
    if not titles:
        raise VerificationError(f"canonical title metadata not found at {url}")
    url_year = proceedings_url_year(url)
    if url_year is not None:
        return SourceMetadata(titles[0], authors[0] if authors else None, url_year, url)
    dates = meta_content(text, "citation_publication_date") or meta_content(text, "citation_date")
    year_match = re.search(r"(20\d{2})", dates[0]) if dates else None
    return SourceMetadata(titles[0], authors[0] if authors else None, int(year_match.group(1)) if year_match else None, url)


def source_metadata(url: str) -> SourceMetadata:
    host = urllib.parse.urlparse(url).netloc.casefold()
    if host.endswith("arxiv.org"):
        return parse_arxiv(url)
    if host.endswith("openreview.net"):
        return parse_openreview(url)
    if host == "doi.org" or host.endswith(".doi.org"):
        doi = urllib.parse.urlparse(url).path.lstrip("/")
        api_url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="/")
        try:
            message = json.loads(fetch(api_url, accept="application/json").decode("utf-8"))["message"]
            title = (message.get("title") or [None])[0]
            authors = message.get("author") or []
            year_parts = (message.get("published-print") or message.get("published-online") or {}).get("date-parts")
            if not title:
                raise KeyError("title")
            return SourceMetadata(title, authors[0].get("family") if authors else None, year_parts[0][0] if year_parts else None, url)
        except Exception as exc:  # noqa: BLE001
            raise VerificationError(f"could not parse Crossref metadata for {url}: {exc}") from exc
    return parse_html_source(url)


def verify_record(record: dict[str, Any]) -> list[str]:
    label = record.get("id", "record")
    source = source_metadata(record["paper_url"])
    errors: list[str] = []
    if normalize_title(record["title"]) != normalize_title(source.title):
        errors.append(f"{label}: title mismatch\n  catalog: {record['title']}\n  source:  {source.title}\n  source_url: {source.source_url}")
    catalog_author = surname(record.get("first_author", ""))
    source_author = surname(source.first_author or "")
    if catalog_author and source_author and catalog_author.casefold() != source_author.casefold():
        errors.append(f"{label}: first_author mismatch\n  catalog: {record['first_author']}\n  source:  {source.first_author}\n  source_url: {source.source_url}")
    # A preprint host's own posted year can legitimately differ from a later
    # conference/journal acceptance year (see
    # docs/reference/metadata-schema.md#venue-and-year). Skip the automated year check
    # only when `paper_url` points at that preprint AND the catalog already
    # names a different, confirmed venue — the venue's own proceedings year
    # is curator-verified instead, not machine-checked against the preprint.
    # When the source itself is the venue record (Crossref/DOI, ACL
    # Anthology, CVF proceedings, etc.), it remains authoritative and year is
    # always checked against it.
    source_host = urllib.parse.urlparse(source.source_url).netloc.casefold()
    is_preprint_source = source_host.endswith(("arxiv.org", "openreview.net"))
    skip_year_check = is_preprint_source and record.get("venue") not in ("arXiv", "OpenReview")
    if not skip_year_check and source.year is not None and record.get("year") != source.year:
        errors.append(f"{label}: year mismatch\n  catalog: {record['year']}\n  source:  {source.year}\n  source_url: {source.source_url}")
    expected_date = record.get("first_submission_date")
    if expected_date is not None:
        date_url = record.get("first_submission_source")
        date_source = source if date_url == source.source_url or date_url == record["paper_url"] else source_metadata(date_url)
        if date_source.first_submission_date != expected_date:
            errors.append(f"{label}: first_submission_date mismatch or unavailable\n  catalog: {expected_date}\n  source:  {date_source.first_submission_date}\n  source_url: {date_url}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--id", action="append", dest="ids", help="verify only this record id (repeatable)")
    parser.add_argument(
        "--changed",
        action="store_true",
        help="verify records whose metadata differs from the committed HEAD version",
    )
    args = parser.parse_args()
    records = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    requested_ids = set(args.ids or [])
    if args.changed and args.ids:
        parser.error("--changed and --id cannot be used together")
    if args.changed:
        try:
            previous = json.loads(
                subprocess.check_output(
                    ["git", "show", "HEAD:data/papers.json"], cwd=ROOT, text=True
                )
            )
        except (subprocess.CalledProcessError, json.JSONDecodeError) as exc:
            print(f"Could not read committed catalog for --changed: {exc}", file=sys.stderr)
            return 1
        previous_by_id = {record.get("id"): record for record in previous}
        changed_ids = {
            record.get("id")
            for record in records
            if record.get("id") not in previous_by_id or record != previous_by_id[record.get("id")]
        }
        selected = [record for record in records if record.get("id") in changed_ids]
        if not selected:
            print("No changed catalog records; bibliography verification skipped")
            return 0
    else:
        selected = [record for record in records if not requested_ids or record.get("id") in requested_ids]
    if requested_ids and len(selected) != len(requested_ids):
        missing = sorted(requested_ids - {record.get("id") for record in selected})
        print(f"Unknown record id(s): {', '.join(missing)}", file=sys.stderr)
        return 1
    errors: list[str] = []
    for index, record in enumerate(selected, 1):
        try:
            errors.extend(verify_record(record))
        except VerificationError as exc:
            errors.append(f"{record.get('id', 'record')}: {exc}")
        print(f"Verified {index}/{len(selected)}: {record.get('id', 'record')}")
    if errors:
        print("\nBibliography verification failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        print("\nPublish blocked: fix metadata or resolve the source blocker.", file=sys.stderr)
        return 1
    print(f"Bibliography verified for {len(selected)} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
