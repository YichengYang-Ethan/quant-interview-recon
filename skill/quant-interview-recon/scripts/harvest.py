#!/usr/bin/env python3
"""
harvest.py — headless harvesters for the sources that genuinely allow it.

Deliberately small. Most quant-interview sources are login-walled or
bot-blocked, and pretending otherwise produces a skill that silently returns
nothing. This file covers ONLY the sources empirically confirmed to serve
content to an unauthenticated script; everything else is handled by the agent
through WebSearch / WebFetch / logged-in Chrome, which is the skill's job.

Confirmed working (probed 2026-09-12):
  * discourse  — any Discourse forum's open JSON API (uscardforum.com et al.)
  * generic    — plain HTML fetch + text extraction, for sites that allow it

Confirmed NOT working headlessly (do not add adapters for these):
  * reddit.com — 403 Blocked for every User-Agent tried, incl. browser UAs and
                 api.reddit.com. Use WebFetch or logged-in Chrome instead.
  * zhihu, 1point3acres, Blind, Glassdoor — login / anti-bot walls.

Usage
-----
  harvest.py discourse --base https://www.uscardforum.com \
      --query "Optiver 面经" --max-topics 15 --out raw.json

  harvest.py generic --url https://example.com/thread --out raw.json

Output is a JSON list of *candidate* records: source-attributed text blocks
for the agent to read and turn into proper question records. This script
never invents a question — extraction of the actual questions is a judgement
call and stays with the model.
"""

from __future__ import annotations

import argparse
import html as _html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

UA = "quant-interview-recon/1.0 (personal interview prep; +https://github.com/YichengYang-Ethan/quant-interview-recon)"
TIMEOUT = 25
SLEEP = 1.2  # be a polite citizen of someone else's forum


def fetch(url: str, accept: str = "application/json") -> tuple[int | None, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": accept})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.status, r.read(2_000_000).decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, f"HTTPError {e.code}: {e.reason}"
    except Exception as e:  # noqa: BLE001 — any transport failure is reportable
        return None, f"{type(e).__name__}: {e}"


def strip_html(s: str) -> str:
    s = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", s or "")
    s = re.sub(r"(?i)<br\s*/?>", "\n", s)
    s = re.sub(r"(?i)</(p|div|li|h[1-6]|tr)>", "\n", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = _html.unescape(s)
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


# --------------------------------------------------------------------------
# discourse
# --------------------------------------------------------------------------

def harvest_discourse(base: str, query: str, max_topics: int, verbose: bool = True) -> list[dict]:
    """
    Discourse exposes /search.json and /t/<id>.json without auth on most public
    installs. Confirmed on uscardforum.com: search returns `topics`, topic JSON
    returns `post_stream.posts[].cooked` (HTML body).
    """
    base = base.rstrip("/")
    out: list[dict] = []

    surl = f"{base}/search.json?q={urllib.parse.quote(query)}"
    st, body = fetch(surl)
    if st != 200:
        print(f"  search failed [{st}]: {body[:160]}", file=sys.stderr)
        return out
    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        print("  search returned non-JSON (anti-bot page?)", file=sys.stderr)
        return out

    topics = data.get("topics") or []
    # Discourse returns post hits separately; keep their topic ids too.
    for p in (data.get("posts") or []):
        tid = p.get("topic_id")
        if tid and not any(t.get("id") == tid for t in topics):
            topics.append({"id": tid, "title": f"(post hit in topic {tid})"})

    if verbose:
        print(f"  search '{query}' -> {len(topics)} topics", file=sys.stderr)

    for t in topics[:max_topics]:
        tid = t.get("id")
        if not tid:
            continue
        time.sleep(SLEEP)
        st, tbody = fetch(f"{base}/t/{tid}.json")
        if st != 200:
            if verbose:
                print(f"    topic {tid} failed [{st}]", file=sys.stderr)
            continue
        try:
            tj = json.loads(tbody)
        except json.JSONDecodeError:
            continue
        title = tj.get("title") or t.get("title") or ""
        slug = tj.get("slug") or ""
        posts = (tj.get("post_stream") or {}).get("posts") or []
        for i, p in enumerate(posts):
            text = strip_html(p.get("cooked", ""))
            if len(text) < 40:
                continue
            out.append({
                "source_platform": _platform_name(base),
                "source_url": f"{base}/t/{slug}/{tid}/{p.get('post_number', i+1)}",
                "source_date": (p.get("created_at") or "")[:10],
                "thread_title": title,
                "author": p.get("username"),
                "post_index": p.get("post_number", i + 1),
                "text": text[:12000],
            })
        if verbose:
            print(f"    topic {tid}: {title[:60]} -> {len(posts)} posts", file=sys.stderr)
    return out


def _platform_name(base: str) -> str:
    host = urllib.parse.urlparse(base).netloc.replace("www.", "")
    return {"uscardforum.com": "美卡论坛"}.get(host, host)


# --------------------------------------------------------------------------
# generic
# --------------------------------------------------------------------------

def harvest_generic(url: str) -> list[dict]:
    st, body = fetch(url, accept="text/html,application/xhtml+xml")
    if st != 200:
        print(f"  [{st}] {body[:200]}", file=sys.stderr)
        return []
    text = strip_html(body)
    if len(text) < 200:
        print("  page returned almost no text — likely JS-rendered or walled", file=sys.stderr)
        return []
    return [{
        "source_platform": urllib.parse.urlparse(url).netloc.replace("www.", ""),
        "source_url": url,
        "thread_title": (re.search(r"(?is)<title[^>]*>(.*?)</title>", body) or [None, ""])[1].strip()[:200]
        if re.search(r"(?is)<title", body) else "",
        "text": text[:30000],
    }]


# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    d = sub.add_parser("discourse", help="harvest a Discourse forum's open JSON API")
    d.add_argument("--base", default="https://www.uscardforum.com")
    d.add_argument("--query", required=True, help='e.g. "Optiver 面经"')
    d.add_argument("--max-topics", type=int, default=15)
    d.add_argument("--out", required=True)

    g = sub.add_parser("generic", help="plain HTML fetch + text extraction")
    g.add_argument("--url", required=True)
    g.add_argument("--out", required=True)

    a = ap.parse_args()
    if a.cmd == "discourse":
        recs = harvest_discourse(a.base, a.query, a.max_topics)
    else:
        recs = harvest_generic(a.url)

    p = Path(a.out).expanduser()
    p.parent.mkdir(parents=True, exist_ok=True)
    existing = []
    if p.exists():
        try:
            existing = json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            existing = []
    seen = {r.get("source_url") for r in existing}
    fresh = [r for r in recs if r.get("source_url") not in seen]
    p.write_text(json.dumps(existing + fresh, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{len(fresh)} new blocks -> {p} (total {len(existing)+len(fresh)})")
    if not fresh:
        print("NOTE: nothing new. That is a result, not an error — record it in sources.json.", file=sys.stderr)


if __name__ == "__main__":
    main()
