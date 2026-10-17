#!/usr/bin/env python3
"""Local cache for primary-source paper documents (PDF/HTML).

Cache-first: `get()` never makes a network request -- it only looks at what
is already on disk under .cache/papers/<paper_id>/. Fetching a document and
checking whether a newer arXiv version exists are separate, explicit
operations that must be invoked deliberately; neither runs implicitly from
`get()`. A new version is written to its own vN/ directory and never
overwrites an earlier one, so an audit log entry can record exactly which
version its evidence came from.

.cache/ is git-ignored. PDFs are never committed or redistributed; they are
a private local aid to avoid repeated network fetches while curating.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE_DIR = ROOT / ".cache" / "papers"
USER_AGENT = "Mozilla/5.0 (compatible; awesome-physical-ai-safety-curation/1.0)"


def arxiv_id_from_url(url: str | None) -> str | None:
    m = re.search(r"arxiv\.org/(?:abs|pdf|html)/([0-9]{4}\.[0-9]{4,5})", url or "")
    return m.group(1) if m else None


def paper_dir(paper_id: str) -> Path:
    return CACHE_DIR / paper_id


def list_versions(paper_id: str) -> list[str]:
    d = paper_dir(paper_id)
    if not d.exists():
        return []
    versions = [p.name for p in d.iterdir() if p.is_dir() and re.match(r"^v\d+$", p.name)]
    return sorted(versions, key=lambda v: int(v[1:]))


def get(paper_id: str, require_verified: bool = True) -> tuple[Path, dict] | None:
    """Cache-first lookup only. No network access. Returns the newest cached
    version's (source_path, meta) or None if nothing is cached yet.

    By default refuses to return a version whose title/identifier has not
    been checked against the catalog record (verification.status is
    "unverified" or "mismatch") -- a cache entry must be explicitly
    verified via `verify` before an audit may use it as evidence. Pass
    require_verified=False only for diagnostics, never for audit evidence."""
    versions = list_versions(paper_id)
    if not versions:
        return None
    vdir = paper_dir(paper_id) / versions[-1]
    meta_path = vdir / "meta.json"
    if not meta_path.exists():
        return None
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    if meta.get("status") != "ok":
        return None
    if require_verified and meta.get("verification", {}).get("status") != "verified":
        return None
    source = vdir / meta["filename"]
    return source, meta


def verify(paper_id: str, match: bool, observed_title: str | None = None, note: str | None = None) -> dict:
    """Record a title/identifier verification result against the newest
    cached version. This is a deliberate step -- the script cannot read PDF
    text itself, so the caller (a human or an agent that has actually read
    the cached document) performs the title comparison and reports the
    outcome here. A version stays "unverified" (and therefore unusable by
    `get()`) until this is called with match=True."""
    versions = list_versions(paper_id)
    if not versions:
        raise SystemExit(f"no cached version for {paper_id}")
    vdir = paper_dir(paper_id) / versions[-1]
    meta_path = vdir / "meta.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    meta["verification"] = {
        "status": "verified" if match else "mismatch",
        "observed_title": observed_title,
        "note": note,
        "verified_at": datetime.now(timezone.utc).isoformat(),
    }
    meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    return meta


def fetch(paper_id: str, url: str) -> tuple[Path | None, dict]:
    """Explicit network fetch. Tries the arXiv PDF first, falls back to the
    given URL as HTML. Always writes a new vN/ directory; never overwrites
    an existing cached version."""
    aid = arxiv_id_from_url(url)
    next_n = len(list_versions(paper_id)) + 1
    vdir = paper_dir(paper_id) / f"v{next_n}"

    data = None
    resolved_url = None
    content_type = None
    arxiv_version = None
    status = "inaccessible"

    if aid:
        try:
            req = urllib.request.Request(f"https://arxiv.org/pdf/{aid}", headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = resp.read()
                resolved_url = resp.geturl()
                content_type = "pdf"
                status = "ok"
            # The /pdf/<id> redirect doesn't always carry the version in its
            # URL, so resolve it from the abs page instead (same lookup
            # check_update uses) rather than trusting the PDF response URL.
            try:
                abs_req = urllib.request.Request(f"https://arxiv.org/abs/{aid}", headers={"User-Agent": USER_AGENT})
                with urllib.request.urlopen(abs_req, timeout=15) as abs_resp:
                    abs_html = abs_resp.read().decode("utf-8", errors="ignore")
                m = re.search(r"\[v(\d+)\]", abs_html)
                arxiv_version = f"v{m.group(1)}" if m else None
            except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError):
                arxiv_version = None
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError):
            data = None

    if data is None and url:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = resp.read()
                resolved_url = resp.geturl()
                content_type = "html"
                status = "ok"
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError):
            status = "inaccessible"

    fetched_at = datetime.now(timezone.utc).isoformat()
    if data is None:
        meta = {
            "paper_id": paper_id, "source_url": url, "resolved_url": None,
            "arxiv_version": None, "content_type": None, "filename": None,
            "sha256": None, "status": status, "fetched_at": fetched_at,
        }
        return None, meta

    vdir.mkdir(parents=True, exist_ok=True)
    filename = "source.pdf" if content_type == "pdf" else "source.html"
    (vdir / filename).write_bytes(data)
    meta = {
        "paper_id": paper_id, "source_url": url, "resolved_url": resolved_url,
        "arxiv_version": arxiv_version, "content_type": content_type,
        "filename": filename, "sha256": hashlib.sha256(data).hexdigest(),
        "status": status, "fetched_at": fetched_at,
        "verification": {"status": "unverified", "observed_title": None, "note": None, "verified_at": None},
    }
    (vdir / "meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    return vdir / filename, meta


def check_update(paper_id: str, url: str) -> dict:
    """Explicit version check against arXiv. Does not fetch the paper body
    and does not touch the cache; only reports whether a newer version
    exists than what is currently cached."""
    aid = arxiv_id_from_url(url)
    if not aid:
        return {"checked": False, "reason": "not an arXiv URL"}
    try:
        req = urllib.request.Request(f"https://arxiv.org/abs/{aid}", headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
        return {"checked": False, "reason": str(exc)}
    m = re.search(r"\[v(\d+)\]", html)
    latest_remote = f"v{m.group(1)}" if m else None
    cached_arxiv_versions = []
    for v in list_versions(paper_id):
        meta_path = paper_dir(paper_id) / v / "meta.json"
        if meta_path.exists():
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
            if meta.get("arxiv_version"):
                cached_arxiv_versions.append(meta["arxiv_version"])
    return {
        "checked": True, "latest_remote": latest_remote,
        "cached_arxiv_versions": cached_arxiv_versions,
        "has_newer": bool(latest_remote and latest_remote not in cached_arxiv_versions),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_get = sub.add_parser("get", help="cache-first lookup, no network access")
    p_get.add_argument("paper_id")
    p_get.add_argument("--allow-unverified", action="store_true", help="diagnostics only -- never use for audit evidence")

    p_fetch = sub.add_parser("fetch", help="explicit network fetch, writes a new version (unverified until `verify` is called)")
    p_fetch.add_argument("paper_id")
    p_fetch.add_argument("url")

    p_update = sub.add_parser("check-update", help="explicit arXiv version check, no fetch")
    p_update.add_argument("paper_id")
    p_update.add_argument("url")

    p_verify = sub.add_parser("verify", help="record a title/identifier match result for the newest cached version")
    p_verify.add_argument("paper_id")
    p_verify.add_argument("--match", choices=["true", "false"], required=True)
    p_verify.add_argument("--observed-title", default=None)
    p_verify.add_argument("--note", default=None)

    args = parser.parse_args()

    if args.cmd == "get":
        result = get(args.paper_id, require_verified=not args.allow_unverified)
        print(json.dumps({"cached": False} if result is None else {"cached": True, "path": str(result[0]), "meta": result[1]}, indent=2, ensure_ascii=False))
    elif args.cmd == "fetch":
        path, meta = fetch(args.paper_id, args.url)
        print(json.dumps({"path": str(path) if path else None, "meta": meta}, indent=2, ensure_ascii=False))
    elif args.cmd == "check-update":
        print(json.dumps(check_update(args.paper_id, args.url), indent=2, ensure_ascii=False))
    elif args.cmd == "verify":
        meta = verify(args.paper_id, args.match == "true", args.observed_title, args.note)
        print(json.dumps(meta, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
