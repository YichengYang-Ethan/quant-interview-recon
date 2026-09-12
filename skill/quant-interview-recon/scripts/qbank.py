#!/usr/bin/env python3
"""
qbank.py — the deterministic core of the quant-interview-recon skill.

Three jobs the model should NOT do by hand:
  1. normalize   — canonicalize raw scraped question records
  2. merge       — fuzzy-dedup across platforms, preserving every source URL
  3. report      — render a Markdown + PDF question bank (CJK-safe)

Everything is stdlib-only. No network. No API keys.

Usage
-----
  qbank.py init      <outdir> --company "Optiver" --role QT
  qbank.py add       <outdir> --file raw_batch.json          # append harvested records
  qbank.py merge     <outdir> [--threshold 0.82]             # dedup -> questions.json
  qbank.py report    <outdir> [--pdf] [--lang zh|en|bi]
  qbank.py stats     <outdir>

Record shape (see references/02-taxonomy.md for the full contract):
  {
    "question": "...",              # REQUIRED, verbatim as found
    "company": "Optiver",           # REQUIRED
    "role": "QT",                   # QT|QR|QD|QA|SWE|unknown
    "round": "OA",                  # OA|phone|superday|onsite|final|unknown
    "category": "probability/conditional",
    "difficulty": "medium",         # easy|medium|hard|unknown
    "year": 2026,
    "source_url": "https://...",    # REQUIRED
    "source_platform": "1point3acres",
    "source_date": "2026-08-14",
    "confidence": 4,                # 1-5, see rubric
    "answer": "sketch or full solution, optional",
    "tags": ["mental-math"],
    "lang": "zh",                   # zh|en
    "verbatim": true                # false if paraphrased/translated by the agent
  }
"""

from __future__ import annotations

import argparse
import datetime as _dt
import difflib
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

# --------------------------------------------------------------------------
# constants
# --------------------------------------------------------------------------

ROLES = {
    "QT": "Quant Trader",
    "QR": "Quant Researcher",
    "QD": "Quant Developer",
    "QA": "Quant Analyst",
    "SWE": "Software Engineer",
    "unknown": "Unspecified",
}

ROUND_ORDER = ["OA", "phone", "superday", "onsite", "final", "unknown"]
ROUND_LABEL = {
    "OA": "Online Assessment / 笔试",
    "phone": "Phone / Video Screen / 电面",
    "superday": "Superday / Final Round",
    "onsite": "Onsite",
    "final": "Final / Offer Stage",
    "unknown": "Round Unspecified",
}

DIFF_ORDER = {"easy": 0, "medium": 1, "hard": 2, "unknown": 3}

# Marketing / low-signal noise. A record whose question text matches any of
# these is quarantined into rejected.json rather than silently dropped.
SPAM_PATTERNS = [
    r"(加|添加)\s*(微信|VX|vx|wx)",
    r"(扫码|私信|咨询)(了解|详情|报名)",
    r"(内推|求职|辅导|培训)(群|班|课程|服务)",
    r"\b(DM|dm) me\b.*\b(for|to get)\b.*\b(prep|coaching|referral)\b",
    r"(包过|保offer|保 offer|100% offer)",
    r"^\s*(求米|求大米|接力|谢谢分享|mark|Mark|占位)\s*$",
    r"(PH求职|WST|直通硅谷|Offer帮|Rexpand|睿思班)",
]
SPAM_RE = [re.compile(p) for p in SPAM_PATTERNS]

# Content-free recollections: a "question" that describes structure but asks nothing.
CONTENTLESS_RE = re.compile(
    r"^\s*(总共|一共)?\s*\d+\s*(轮|rounds?)\s*(面试)?\s*[,.。，]?\s*$"
    r"|^\s*(挂了|过了|等消息|waiting|rejected|no update)\s*[.。!！]?\s*$",
    re.IGNORECASE,
)

MIN_QUESTION_CHARS = 12

# Curated question banks assign one entry per problem by construction, so two
# DIFFERENT entries from the same bank are two different problems however
# similar the wording. QuantGuide ships deliberate near-twins ("Find the most
# recent date..." vs "Find the next date...") that score 0.91 lexically and are
# not the same question. Forums are excluded: the same recollection genuinely
# does get posted twice there.
CURATED_PLATFORMS = {
    "quantguide", "puzzledquant", "openquant", "brainstellar", "quantquestions",
    "quantinterview",
}


CROSS_LANG_SLACK = 0.10


def _curated(platform: str) -> str | None:
    p = (platform or "").lower().replace(".io", "").replace(".co", "").replace(" ", "")
    return p if p in CURATED_PLATFORMS else None

CJK_FONT_CANDIDATES = ["PingFang SC", "Heiti SC", "Songti SC", "Noto Sans CJK SC", "Hiragino Sans GB"]
MAIN_FONT_CANDIDATES = ["Helvetica Neue", "Helvetica", "Arial", "DejaVu Sans"]
MONO_FONT_CANDIDATES = ["Menlo", "Monaco", "DejaVu Sans Mono", "Courier New"]


# --------------------------------------------------------------------------
# small helpers
# --------------------------------------------------------------------------

def _now() -> str:
    return _dt.datetime.now().strftime("%Y-%m-%d %H:%M")


def _today() -> str:
    return _dt.date.today().isoformat()


def _read_json(p: Path, default):
    if not p.exists():
        return default
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        die(f"{p} is not valid JSON: {e}")


def _write_json(p: Path, obj) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def die(msg: str, code: int = 1):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(code)


def warn(msg: str):
    print(f"WARN: {msg}", file=sys.stderr)


def _font_available(name: str) -> bool:
    """True if fontconfig or the macOS font dirs know this family."""
    if shutil.which("fc-list"):
        try:
            out = subprocess.run(["fc-list", ":family"], capture_output=True, text=True, timeout=20)
            if name.lower() in out.stdout.lower():
                return True
        except Exception:
            pass
    for d in ("/System/Library/Fonts", "/Library/Fonts", os.path.expanduser("~/Library/Fonts")):
        try:
            stem = name.replace(" ", "").lower()
            for f in os.listdir(d):
                if stem[:8] and stem[:8] in f.replace(" ", "").lower():
                    return True
        except OSError:
            continue
    return False


def _pick_font(candidates: list[str], fallback: str) -> str:
    for c in candidates:
        if _font_available(c):
            return c
    return fallback


# --------------------------------------------------------------------------
# normalization + dedup
# --------------------------------------------------------------------------

_PUNCT_MAP = str.maketrans({
    "，": ",", "。": ".", "？": "?", "！": "!", "；": ";", "：": ":",
    "（": "(", "）": ")", "【": "[", "】": "]", "“": '"', "”": '"',
    "‘": "'", "’": "'", "—": "-", "–": "-", "～": "~", "、": ",",
})

# Words that carry no discriminating power when comparing two question texts.
_STOP = {
    "the", "a", "an", "of", "is", "are", "was", "were", "to", "in", "on", "at", "for",
    "and", "or", "you", "your", "we", "i", "it", "that", "this", "what", "how", "many",
    "there", "be", "with", "do", "does", "did", "if", "then", "given", "find", "compute",
    "问", "求", "的", "了", "是", "有", "个", "会", "我", "你", "他", "这", "那", "就",
}


_ZH_NUM = {"零": "0", "一": "1", "两": "2", "二": "2", "三": "3", "四": "4", "五": "5",
           "六": "6", "七": "7", "八": "8", "九": "9", "十": "10", "百": "100", "千": "1000"}

# Spelled-out numbers are the usual form in English question text ("two heads
# in a row"), so without this the numeric guard sees no numbers at all and
# silently falls back to pure lexical matching — exactly the case it exists
# to catch.
_EN_NUM = {
    "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
    "six": "6", "seven": "7", "eight": "8", "nine": "9", "ten": "10",
    "eleven": "11", "twelve": "12", "thirteen": "13", "fourteen": "14",
    "fifteen": "15", "sixteen": "16", "seventeen": "17", "eighteen": "18",
    "nineteen": "19", "twenty": "20", "thirty": "30", "forty": "40",
    "fifty": "50", "sixty": "60", "seventy": "70", "eighty": "80",
    "ninety": "90", "hundred": "100", "thousand": "1000", "million": "1000000",
    "half": "0.5", "twice": "2", "double": "2", "triple": "3",
}
_EN_NUM_RE = re.compile(r"\b(" + "|".join(_EN_NUM) + r")\b")


def numeric_slots(s: str) -> tuple:
    """Ordered multiset of the numbers a question depends on."""
    return tuple(sorted(re.findall(r"\d+(?:\.\d+)?", s or "")))


def numbers_compatible(a: str, b: str) -> bool:
    """
    Two questions whose numbers CONFLICT are different questions: "two heads in
    a row" (E=6) is not "three heads in a row" (E=14), and 10 dice is not 100.

    But one side merely having FEWER numbers is not a conflict — it is what a
    truncation or a paraphrase looks like. A 一亩三分地 post cut off by a points
    wall keeps "$1" and loses "100 turns"; it is still the same question as the
    full text. So the test is subset, not equality.
    """
    from collections import Counter
    ca, cb = Counter(numeric_slots(a)), Counter(numeric_slots(b))
    if not ca or not cb:
        return True
    small, large = (ca, cb) if sum(ca.values()) <= sum(cb.values()) else (cb, ca)
    return all(large[k] >= v for k, v in small.items())


def normalize_text(s: str) -> str:
    """Canonical form used for fuzzy comparison only — never shown to the user."""
    s = unicodedata.normalize("NFKC", s or "")
    s = s.translate(_PUNCT_MAP)
    s = s.lower()
    s = re.sub(r"https?://\S+", " ", s)
    # Chinese numerals must become Arabic before any numeric comparison, or
    # "连续两次正面" and "two heads in a row" carry different slots.
    for zh, ar in _ZH_NUM.items():
        s = s.replace(zh, ar)
    s = _EN_NUM_RE.sub(lambda m: _EN_NUM[m.group(1)], s)
    # Numbers are NOT masked. Masking them merges "two heads in a row" (E=6)
    # with "three heads in a row" (E=14) — measured at similarity 0.91 — and a
    # bank that folds those together teaches a wrong answer while claiming
    # corroboration for it. A duplicate entry is a far cheaper mistake.
    s = re.sub(r"[^\w一-鿿]+", " ", s)
    toks = [t for t in s.split() if t and t not in _STOP]
    return " ".join(toks)


def _shingles(norm: str, n: int = 3) -> set:
    """Char shingles for CJK (no spaces), word shingles for latin."""
    if re.search(r"[一-鿿]", norm):
        compact = norm.replace(" ", "")
        return {compact[i:i + n] for i in range(max(1, len(compact) - n + 1))}
    words = norm.split()
    if len(words) < n:
        return set(words)
    return {" ".join(words[i:i + n]) for i in range(len(words) - n + 1)}


def similarity(a: str, b: str) -> float:
    """Jaccard on shingles, floored by SequenceMatcher. 0..1."""
    if not a or not b:
        return 0.0
    if a == b:
        return 1.0
    sa, sb = _shingles(a), _shingles(b)
    jac = len(sa & sb) / len(sa | sb) if (sa | sb) else 0.0
    seq = difflib.SequenceMatcher(None, a, b).ratio()
    return max(jac, seq * 0.95)


def dedup_text(rec: dict) -> str:
    """
    The string used for fuzzy matching.

    Lexical similarity cannot see that "一枚均匀硬币抛 100 次，恰好 3 次正面" and
    "a fair coin flipped 10 times, exactly 3 heads" are the same problem — the
    shingle overlap across scripts is zero. So the harvesting agent is required
    to attach an English gloss (`question_en`) to every non-English record, and
    that gloss is what we match on. Falls back to the raw text when absent.
    """
    return rec.get("question_en") or rec.get("question", "")


def qid(rec: dict) -> str:
    return hashlib.sha1(normalize_text(dedup_text(rec)).encode("utf-8")).hexdigest()[:12]


def classify_junk(rec: dict) -> str | None:
    """Return a rejection reason, or None if the record is usable."""
    q = (rec.get("question") or "").strip()
    if len(q) < MIN_QUESTION_CHARS:
        return f"too short ({len(q)} chars)"
    if CONTENTLESS_RE.search(q):
        return "content-free recollection (describes structure, asks nothing)"
    for pat in SPAM_RE:
        if pat.search(q):
            return f"marketing/spam pattern: {pat.pattern}"
    if not rec.get("source_url"):
        return "no source_url (unsourced questions are not admissible)"
    return None


def _coerce(rec: dict, run: dict) -> dict:
    """Fill defaults and coerce types so downstream code can assume shape."""
    out = dict(rec)
    out["question"] = (out.get("question") or "").strip()
    out["company"] = (out.get("company") or run.get("company") or "unknown").strip()
    out["role"] = (out.get("role") or run.get("role") or "unknown").strip()
    r = out.get("round") or "unknown"
    out["round"] = r if r in ROUND_ORDER else "unknown"
    d = (out.get("difficulty") or "unknown").lower()
    out["difficulty"] = d if d in DIFF_ORDER else "unknown"
    out["category"] = (out.get("category") or "uncategorized").strip()
    try:
        out["confidence"] = max(1, min(5, int(out.get("confidence", 3))))
    except (TypeError, ValueError):
        out["confidence"] = 3
    try:
        out["year"] = int(out["year"]) if out.get("year") else None
    except (TypeError, ValueError):
        out["year"] = None
    out["tags"] = list(out.get("tags") or [])
    out["lang"] = out.get("lang") or ("zh" if re.search(r"[一-鿿]", out["question"]) else "en")
    out["verbatim"] = bool(out.get("verbatim", True))
    out["source_platform"] = out.get("source_platform") or "unknown"
    out["question_en"] = (out.get("question_en") or "").strip() or None
    out["canonical_key"] = (out.get("canonical_key") or "").strip().lower() or None
    # A non-English record with no gloss can never cross-language-dedup. That is
    # a silent recall failure, so it is surfaced rather than swallowed.
    if out["lang"] != "en" and not out["question_en"]:
        out["_warn"] = "no question_en gloss — will not dedup against English sources"
    return out


def merge_pair(keep: dict, drop: dict) -> dict:
    """Fold `drop` into `keep`, losing nothing that matters."""
    m = dict(keep)
    srcs = m.setdefault("sources", [])

    def _src(r):
        return {
            "url": r.get("source_url"),
            "platform": r.get("source_platform"),
            "date": r.get("source_date"),
            "year": r.get("year"),
            "lang": r.get("lang"),
        }

    if not srcs:
        srcs.append(_src(keep))
    if not any(s.get("url") == drop.get("source_url") for s in srcs):
        srcs.append(_src(drop))

    # Prefer the longer verbatim text — truncated forum posts lose the tail.
    if drop.get("verbatim") and len(drop["question"]) > len(m["question"]) * 1.15:
        m["variant_text"] = m["question"]
        m["question"] = drop["question"]

    # Most recent attestation wins for recency fields.
    if (drop.get("year") or 0) > (m.get("year") or 0):
        m["year"] = drop.get("year")
        if drop.get("round") != "unknown":
            m["round"] = drop["round"]

    # An answer is strictly additive.
    if drop.get("answer") and not m.get("answer"):
        m["answer"] = drop["answer"]
    elif drop.get("answer") and m.get("answer") and drop["answer"] not in m["answer"]:
        m["alt_answers"] = m.get("alt_answers", []) + [drop["answer"]]

    for f in ("category", "difficulty"):
        if m.get(f) in ("uncategorized", "unknown") and drop.get(f) not in ("uncategorized", "unknown"):
            m[f] = drop[f]

    m["tags"] = sorted(set(m.get("tags", [])) | set(drop.get("tags", [])))
    m["corroboration"] = len({s.get("url") for s in srcs if s.get("url")})
    # Independent corroboration is the strongest confidence signal there is.
    m["confidence"] = min(5, max(m.get("confidence", 3), drop.get("confidence", 3)) + (1 if m["corroboration"] >= 2 else 0))
    return m


def merge_records(records: list[dict], threshold: float = 0.82) -> tuple[list[dict], list[dict]]:
    """Bucket by (normalized-prefix-ish) then O(n^2) within bucket."""
    merged: list[dict] = []
    norms: list[str] = []
    trail: list[dict] = []
    by_canon: dict[str, int] = {}

    # Deterministic order: highest confidence and longest text first, so the
    # best-attested phrasing becomes the survivor.
    ordered = sorted(records, key=lambda r: (-r.get("confidence", 3), -len(r.get("question", ""))))

    for rec in ordered:
        n = normalize_text(dedup_text(rec))
        canon = (rec.get("canonical_key") or "").strip().lower()

        # An explicit canonical_key is an assertion by the harvester that this
        # is a known named problem. Trust it over any lexical score.
        if canon and canon in by_canon and numbers_compatible(n, norms[by_canon[canon]]):
            i = by_canon[canon]
            trail.append({
                "action": "merged",
                "basis": f"canonical_key={canon}",
                "similarity": 1.0,
                "into": merged[i]["question"][:90],
                "from": rec["question"][:90],
                "from_url": rec.get("source_url"),
            })
            merged[i] = merge_pair(merged[i], rec)
            continue

        cur = _curated(rec.get("source_platform", ""))
        best_i, best_s, best_thr = -1, 0.0, threshold
        for i, existing in enumerate(norms):
            # Same curated bank, different entry -> different problem. Skip.
            if cur and any(
                _curated(sr.get("platform", "")) == cur
                and sr.get("url") != rec.get("source_url")
                for sr in (merged[i].get("sources") or [])
            ):
                continue
            if not numbers_compatible(n, existing):
                continue
            s = similarity(n, existing)
            # A cross-language match is being made through a translated gloss,
            # which is a paraphrase by nature. Holding it to the same lexical
            # bar as two English posts is the wrong test: measured on a real
            # pair, an accurate gloss scored 0.799 against the original.
            thr = threshold
            if rec.get("lang") != merged[i].get("lang"):
                thr = threshold - CROSS_LANG_SLACK
            if s > best_s:
                best_i, best_s, best_thr = i, s, thr
        if best_s >= best_thr and best_i >= 0:
            trail.append({
                "action": "merged",
                "basis": "lexical",
                "similarity": round(best_s, 3),
                "into": merged[best_i]["question"][:90],
                "from": rec["question"][:90],
                "from_url": rec.get("source_url"),
            })
            merged[best_i] = merge_pair(merged[best_i], rec)
            if canon:
                by_canon.setdefault(canon, best_i)
        else:
            rec = dict(rec)
            rec.setdefault("sources", [{
                "url": rec.get("source_url"),
                "platform": rec.get("source_platform"),
                "date": rec.get("source_date"),
                "year": rec.get("year"),
                "lang": rec.get("lang"),
            }])
            rec["corroboration"] = 1
            merged.append(rec)
            norms.append(n)
            if canon:
                by_canon.setdefault(canon, len(merged) - 1)

    for m in merged:
        m["id"] = qid(m)
    return merged, trail


# --------------------------------------------------------------------------
# markdown rendering
# --------------------------------------------------------------------------

# Measured against PingFang SC + Helvetica Neue under xelatex: every glyph on
# the left is missing from at least one weight, and renders as a tofu box.
# Scraped questions do contain them, so they are folded here rather than only
# being kept out of our own templates.
_GLYPH_FALLBACK = str.maketrans({
    "\u2192": "->", "\u2190": "<-", "\u21d2": "=>", "\u2194": "<->",
    "\u25cf": "\u2022", "\u25cb": "o", "\u25a0": "\u2022", "\u25a1": "[ ]",
    "\u25aa": "\u2022", "\u2587": "\u2022", "\u25b0": "\u2022", "\u25b1": "\u2022",
    "\u25c6": "\u2022", "\u2605": "*", "\u2606": "*", "\u2588": "\u2022",
    # Symbols that carry meaning, so they get a spelled equivalent rather than
    # being dropped: a warning marker that silently vanishes is worse than an
    # ugly one.
    "\u26a0": "!", "\u2b50": "*", "\u2714": "v", "\u2713": "v", "\u2717": "x",
    "\u2718": "x", "\u2705": "v", "\u274c": "x", "\u27a1": "->", "\u2b05": "<-",
})

# Emoji and pictographs. Neither PingFang nor Helvetica has them, and forum
# text (and our own authored sections) is full of them. Anything still
# unmapped after _GLYPH_FALLBACK gets dropped rather than left to tofu.
_EMOJI_RE = re.compile(
    "[" 
    "\U0001F000-\U0001FAFF"   # emoji blocks
    "\U00002600-\U000027BF"   # misc symbols & dingbats
    "\U0001F1E6-\U0001F1FF"   # regional indicators
    "\U00002190-\U000021FF"   # arrows not already mapped
    "\U0000FE00-\U0000FE0F"   # variation selectors
    "\U0000200D"               # zero-width joiner
    "\U00002B00-\U00002BFF"   # misc symbols and arrows
    "]+"
)


def tex_safe(s: str) -> str:
    """
    Make text survive pandoc -> xelatex.

    The only genuinely dangerous character is `$`: pandoc reads it as a math
    delimiter. Quant questions legitimately contain both money ("$300k base")
    and math ("$P(X>1)$"). Heuristic: if the count of unescaped `$` is odd the
    author meant money, so escape them all; if even, assume intentional math
    and leave it alone.
    """
    if not s:
        return ""
    s = s.replace("\r\n", "\n").replace("\r", "\n")
    # Arrows/dashes that PingFang+Helvetica render as tofu boxes.
    s = s.translate(_GLYPH_FALLBACK)
    s = _EMOJI_RE.sub("", s)
    # JSON escape leakage from scraped payloads: a literal backslash-n that is
    # not the start of a real command (\nu, \neq). LaTeX reads it as an
    # undefined control sequence and aborts the whole document.
    # Real commands beginning \n \t \r are all lowercase (\nu, \neq, \nabla,
    # \times, \theta, \rho, \right), so "not followed by a lowercase letter"
    # cleanly separates leakage ("\nEach", "\n\n", "\t ") from real math.
    s = re.sub(r"\\([ntr])(?![a-z])", " ", s)
    # Double-unescaping upstream turns "\%" into "\\%". In LaTeX "\\" is a line
    # break, so "\\%" is invalid wherever it lands and kills the build. A real
    # "\\" is always followed by whitespace or "[", never by these specials.
    s = re.sub(r"\\{2,}(?=[%$&#_{}~^])", "\\\\", s)

    # Scraped payloads use LaTeX-native \( \) and \[ \] delimiters, but pandoc
    # markdown only understands $ and $$. Passing them through unconverted
    # makes pandoc emit them into a text context, where LaTeX rejects them as
    # a "Bad math environment delimiter" and the whole build dies.
    s = re.sub(r"\\\[(.+?)\\\]", r"$$\1$$", s, flags=re.S)
    s = re.sub(r"\\\((.+?)\\\)", r"$\1$", s, flags=re.S)

    bare = len(re.findall(r"(?<!\\)\$", s))
    if bare % 2 == 1:
        s = re.sub(r"(?<!\\)\$", r"\\$", s)
    # A lone backslash that isn't starting a known escape breaks LaTeX.
    # \( \) \[ \] are legitimate math delimiters and scraped quant questions
    # are full of them, so they must survive rather than be escaped into noise.
    s = re.sub(r"\\(?![\\$&%#_{}^~()\[\]a-zA-Z])", r"\\textbackslash{}", s)
    return s


# Glyph budget, measured against PingFang SC + Helvetica Neue with xelatex:
# ● ○ ■ □ ▪ ▇ ▰ ▱ ◆ ★ ☆ are all missing from Helvetica Neue in at least one
# weight (● survives roman and bold but NOT italic, which is exactly where a
# meta line puts it). Only • and · render in every weight. So the report uses
# a number for confidence and • for bars — no decorative glyph is worth a
# page full of tofu boxes on someone else's machine.
def _stars(n: int) -> str:
    return f"{max(1, min(5, int(n or 3)))}/5"


def _conf_note(n: int, corroboration: int = 1) -> str:
    """
    The label must not claim corroboration the sources do not support — a
    harvester can hand us confidence=5 off a single post, and printing
    "多源互证" there would be a lie the reader cannot check.
    """
    n = max(1, min(5, int(n or 3)))
    if n >= 5 and corroboration >= 2:
        return "多源互证 · 一手"
    if n >= 5:
        return "单一来源 · 强可信"
    return {4: "可信来源 · 近期", 3: "单一来源 · 合理",
            2: "弱来源 / 较旧", 1: "存疑 · 待验证"}.get(n, "")


def _short_host(url: str) -> str:
    m = re.match(r"https?://([^/]+)", url or "")
    return (m.group(1).replace("www.", "") if m else (url or "?"))[:38]


def _section_safe(md: str) -> str:
    """
    Sanitize an authored markdown block without destroying its formatting.

    tex_safe() is built for scraped question text and would mangle deliberate
    markdown. Here only the two things that actually abort a LaTeX build are
    touched: JSON-escape leakage and tofu glyphs.
    """
    md = md.translate(_GLYPH_FALLBACK)
    md = _EMOJI_RE.sub("", md)
    md = re.sub(r"\\([ntr])(?![a-z])", " ", md)
    md = re.sub(r"\\{2,}(?=[%$&#_{}~^])", "\\\\", md)
    return md


def render_markdown(run: dict, questions: list[dict], sources: list[dict], lang: str = "bi") -> str:
    company = run.get("company", "Unknown")
    role = run.get("role", "unknown")
    role_full = ROLES.get(role, role)
    L: list[str] = []

    # ---- front matter (pandoc YAML) ----
    L.append("---")
    L.append(f'title: "{company} — Quant 面试题库"')
    L.append(f'subtitle: "{role_full} ({role}) · New Grad Full-Time · 生成于 {run.get("generated", _today())}"')
    L.append('author: "quant-interview-recon"')
    L.append("---")
    L.append("")

    # ---- how to read ----
    total = len(questions)
    by_round = Counter(q.get("round", "unknown") for q in questions)
    by_cat = Counter((q.get("category", "uncategorized").split("/")[0]) for q in questions)
    corrob = sum(1 for q in questions if q.get("corroboration", 1) >= 2)
    recent = sum(1 for q in questions if (q.get("year") or 0) >= _dt.date.today().year - 1)

    L.append("# 概览 / At a Glance")
    L.append("")
    L.append("| | |")
    L.append("|---|---|")
    L.append(f"| **公司 Company** | {tex_safe(company)} |")
    L.append(f"| **岗位 Role** | {role_full} (`{role}`) |")
    L.append(f"| **题目总数 Questions** | {total} |")
    L.append(f"| **多源互证 Corroborated (≥2 sources)** | {corrob} ({(100*corrob//total) if total else 0}%) |")
    L.append(f"| **近两年 Recent (≥{_dt.date.today().year - 1})** | {recent} ({(100*recent//total) if total else 0}%) |")
    L.append(f"| **检索平台 Platforms searched** | {len(sources)} |")
    L.append(f"| **生成时间 Generated** | {run.get('generated', _now())} |")
    L.append("")

    if run.get("caveat"):
        L.append(f"> **口径提醒**：{tex_safe(run['caveat'])}")
        L.append("")

    L.append("**可信度标记**：`5/5` = 多源互证的一手回忆；`2/5` = 单一来源或年代较久，面试前请再交叉验证。"
             " 题目按 **轮次 / 类别** 两级编排；同一道题若在多个平台出现，已合并并列出全部来源。")
    L.append("")

    # ---- pipeline ----
    if run.get("pipeline"):
        L.append("# 面试流程 / Interview Pipeline")
        L.append("")
        for i, step in enumerate(run["pipeline"], 1):
            L.append(f"**{i}. {tex_safe(step.get('stage',''))}** — {tex_safe(step.get('detail',''))}")
            if step.get("source"):
                L.append(f"  <!-- -->  \n  来源：<{step['source']}>")
            L.append("")

    # ---- distribution ----
    if by_cat:
        L.append("# 题型分布 / Category Distribution")
        L.append("")
        L.append("| 类别 Category | 题数 | 占比 | |")
        L.append("|---|---:|---:|---|")
        for cat, n in by_cat.most_common():
            pct = 100 * n // total if total else 0
            L.append(f"| {tex_safe(cat)} | {n} | {pct}% | {'•' * max(1, pct // 4)} |")
        L.append("")
        L.append("*备考时间应按这张表分配，而不是按你喜欢做哪类题。*")
        L.append("")

    # ---- the questions ----
    L.append("# 题目 / Questions")
    L.append("")

    idx = 0
    present_rounds = [r for r in ROUND_ORDER if by_round.get(r)]
    for rnd in present_rounds:
        rqs = [q for q in questions if q.get("round", "unknown") == rnd]
        L.append(f"## {ROUND_LABEL[rnd]}  ({len(rqs)} 题)")
        L.append("")
        grouped = defaultdict(list)
        for q in rqs:
            grouped[q.get("category", "uncategorized")].append(q)

        for cat in sorted(grouped, key=lambda c: (-len(grouped[c]), c)):
            L.append(f"### {tex_safe(cat)}")
            L.append("")
            cqs = sorted(grouped[cat], key=lambda q: (DIFF_ORDER.get(q.get("difficulty", "unknown"), 3),
                                                      -(q.get("corroboration") or 1)))
            for q in cqs:
                idx += 1
                conf = q.get("confidence", 3)
                meta_bits = [
                    f"难度 {q.get('difficulty','unknown')}",
                    f"可信度 {_stars(conf)} {_conf_note(conf, q.get('corroboration', 1))}",
                ]
                if q.get("year"):
                    meta_bits.append(f"{q['year']} 年")
                if (q.get("corroboration") or 1) > 1:
                    meta_bits.append(f"{q['corroboration']} 个独立来源")
                if not q.get("verbatim", True):
                    meta_bits.append("*非原文（转述/翻译）*")

                L.append(f"**Q{idx}.** {tex_safe(q['question'])}")
                L.append("")
                L.append(f"<!-- -->  \n*{' · '.join(meta_bits)}*")
                L.append("")

                if q.get("variant_text"):
                    L.append(f"> **另一种问法：** {tex_safe(q['variant_text'])}")
                    L.append("")
                if q.get("answer"):
                    L.append(f"> **解题思路：** {tex_safe(q['answer'])}")
                    L.append("")
                for alt in q.get("alt_answers", [])[:2]:
                    L.append(f"> **另一解法：** {tex_safe(alt)}")
                    L.append("")
                if q.get("tags"):
                    L.append(f"`{'` `'.join(tex_safe(t) for t in q['tags'][:8])}`")
                    L.append("")

                srcs = q.get("sources") or [{"url": q.get("source_url"), "platform": q.get("source_platform")}]
                links = ", ".join(
                    f"[{tex_safe(s.get('platform') or _short_host(s.get('url','')))}]({s.get('url')})"
                    for s in srcs if s.get("url")
                )
                if links:
                    L.append(f"<small>来源：{links}</small>")
                    L.append("")
                L.append("")

    # ---- free-form sections ----
    # For a sparse-coverage firm the question count is the least useful part of
    # the report: what wins the interview is firm intel, a pipeline guess, and
    # the candidate's own story. run.json can carry those as markdown blocks so
    # they land in the same PDF instead of a separate file the user loses.
    for sec in run.get("sections", []):
        title = sec.get("title", "").strip()
        body = sec.get("body", "").strip()
        if not (title or body):
            continue
        L.append(f"# {tex_safe(title)}")
        L.append("")
        # Section bodies are authored, not scraped: pass headings, tables and
        # links through, and only defuse the characters that break LaTeX.
        L.append(_section_safe(body))
        L.append("")

    # ---- appendix: source ledger ----
    L.append("# 附录 A · 检索台账 / Source Ledger")
    L.append("")
    L.append("这张表记录了**搜过什么、拿到什么、哪里被墙**。空手而归的平台同样记录在案 —— "
             "「这里没有」和「这里有」一样是信息。")
    L.append("")
    L.append("| 平台 | 访问方式 | 结果 | 产出题数 |")
    L.append("|---|---|---|---:|")
    for s in sources:
        L.append(
            f"| {tex_safe(s.get('platform','?'))} "
            f"| {tex_safe(s.get('access','?'))} "
            f"| {tex_safe(s.get('result','?'))} "
            f"| {s.get('yield', 0)} |"
        )
    L.append("")

    # ---- appendix: raw urls ----
    all_urls = []
    seen = set()
    for q in questions:
        for s in (q.get("sources") or []):
            u = s.get("url")
            if u and u not in seen:
                seen.add(u)
                all_urls.append((s.get("platform", "?"), u, s.get("date") or ""))
    if all_urls:
        L.append("# 附录 B · 全部原始来源 URL")
        L.append("")
        for plat, u, d in sorted(all_urls):
            L.append(f"- **{tex_safe(plat)}**{(' · ' + d) if d else ''} — <{u}>")
        L.append("")

    # ---- appendix: drill plan ----
    if by_cat:
        L.append("# 附录 C · 针对性刷题建议")
        L.append("")
        L.append("按上面的分布表，你在这家公司最该练的是：")
        L.append("")
        for cat, n in by_cat.most_common(5):
            L.append(f"- **{tex_safe(cat)}**（{n} 题，{100*n//total if total else 0}%）")
        L.append("")
        L.append("资源映射见 skill 的 `references/05-prep-stack.md`。")
        L.append("")

    L.append("---")
    L.append("")
    L.append(f"<small>本文档由 `quant-interview-recon` 于 {run.get('generated', _now())} 生成。"
             "所有题目均来自公开来源，已标注出处与可信度。面经存在时间衰减与 NDA 脱敏，"
             "**请把本文档当作命中率地图，而不是标准答案集。**</small>")
    L.append("")
    return "\n".join(L)


# --------------------------------------------------------------------------
# pdf
# --------------------------------------------------------------------------

def build_pdf(md_path: Path, pdf_path: Path) -> bool:
    if not shutil.which("pandoc"):
        warn("pandoc not found — skipping PDF. Install with: brew install pandoc")
        return False

    cjk = _pick_font(CJK_FONT_CANDIDATES, "PingFang SC")
    main = _pick_font(MAIN_FONT_CANDIDATES, "Helvetica")
    mono = _pick_font(MONO_FONT_CANDIDATES, "Menlo")

    header = md_path.parent / ".pdf-header.tex"
    header.write_text(r"""
\usepackage{fancyhdr}
\usepackage{xcolor}
\definecolor{acc}{HTML}{1F4E79}
\definecolor{soft}{HTML}{5A6470}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\color{soft}\leftmark}
\fancyfoot[C]{\small\color{soft}\thepage}
\renewcommand{\headrulewidth}{0.3pt}
\usepackage{titlesec}
\titleformat{\section}{\Large\bfseries\color{acc}}{\thesection}{1em}{}
\titleformat{\subsection}{\large\bfseries\color{acc}}{\thesubsection}{1em}{}
\usepackage{enumitem}
\setlist{itemsep=2pt,parsep=0pt}
\usepackage{longtable}
\setlength{\emergencystretch}{3em}
""".strip() + "\n", encoding="utf-8")

    engines = ["xelatex", "lualatex"]
    last_err = ""
    for eng in engines:
        if not shutil.which(eng) and not (eng == "xelatex" and shutil.which("tectonic")):
            continue
        cmd = [
            "pandoc", str(md_path), "-o", str(pdf_path),
            f"--pdf-engine={eng}",
            "--toc", "--toc-depth=3",
            "-V", f"CJKmainfont={cjk}",
            "-V", f"mainfont={main}",
            "-V", f"monofont={mono}",
            "-V", "geometry:margin=2.2cm",
            "-V", "fontsize=10pt",
            "-V", "linkcolor=blue",
            "-V", "urlcolor=blue",
            "-V", "colorlinks=true",
            "--highlight-style=tango",
            f"--include-in-header={header}",
        ]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode == 0 and pdf_path.exists():
            header.unlink(missing_ok=True)
            return True
        if not last_err:
            last_err = f"[{eng}] " + (r.stderr or "")[-1500:]

    # Retry once with everything fancy stripped — a broken LaTeX package should
    # never cost the user their PDF.
    r = subprocess.run(
        ["pandoc", str(md_path), "-o", str(pdf_path), "--pdf-engine=xelatex",
         "--toc", "-V", f"CJKmainfont={cjk}", "-V", "geometry:margin=2.2cm"],
        capture_output=True, text=True,
    )
    header.unlink(missing_ok=True)
    if r.returncode == 0 and pdf_path.exists():
        warn("PDF built in fallback (plain) mode.")
        return True

    warn(f"PDF build failed.\n{last_err or r.stderr[-1500:]}")
    html = pdf_path.with_suffix(".html")
    subprocess.run(["pandoc", str(md_path), "-o", str(html), "--standalone", "--toc",
                    "--metadata", "title=Quant Interview Bank"], capture_output=True)
    if html.exists():
        warn(f"Wrote HTML fallback instead: {html}")
    return False


# --------------------------------------------------------------------------
# commands
# --------------------------------------------------------------------------

def cmd_init(a):
    out = Path(a.outdir).expanduser()
    (out / "raw").mkdir(parents=True, exist_ok=True)
    run = {
        "company": a.company,
        "role": a.role,
        "generated": _now(),
        "created": _today(),
        "cycle": a.cycle,
        "pipeline": [],
        "caveat": "",
    }
    _write_json(out / "run.json", run)
    if not (out / "raw" / "records.json").exists():
        _write_json(out / "raw" / "records.json", [])
    if not (out / "sources.json").exists():
        _write_json(out / "sources.json", [])
    print(f"initialized {out}")
    print(f"  company={a.company} role={a.role}")
    print(f"  next: append harvested records to {out/'raw'/'records.json'} (or `qbank.py add --file ...`)")


def cmd_add(a):
    out = Path(a.outdir).expanduser()
    run = _read_json(out / "run.json", {})
    if not run:
        die(f"{out}/run.json missing — run `qbank.py init` first")
    incoming = _read_json(Path(a.file).expanduser(), None)
    if incoming is None:
        die(f"cannot read {a.file}")
    if isinstance(incoming, dict):
        incoming = incoming.get("questions") or incoming.get("records") or [incoming]
    if not isinstance(incoming, list):
        die("input must be a JSON list of records (or an object with .questions)")

    store = _read_json(out / "raw" / "records.json", [])
    rejected = _read_json(out / "rejected.json", [])
    kept = 0
    for rec in incoming:
        if not isinstance(rec, dict):
            continue
        rec = _coerce(rec, run)
        reason = classify_junk(rec)
        if reason:
            rejected.append({**rec, "_rejected": reason})
            continue
        store.append(rec)
        kept += 1

    _write_json(out / "raw" / "records.json", store)
    _write_json(out / "rejected.json", rejected)
    print(f"added {kept} records ({len(incoming) - kept} quarantined) — raw total {len(store)}")
    if len(incoming) - kept:
        print(f"  quarantined records are in {out/'rejected.json'} (reviewable, not deleted)")


def cmd_merge(a):
    out = Path(a.outdir).expanduser()
    raw = _read_json(out / "raw" / "records.json", [])
    if not raw:
        die("no raw records — nothing to merge")
    merged, trail = merge_records(raw, threshold=a.threshold)
    _write_json(out / "questions.json", merged)
    _write_json(out / "merge-log.json", trail)
    print(f"merged {len(raw)} raw -> {len(merged)} unique ({len(raw)-len(merged)} folded)")
    multi = sum(1 for m in merged if m.get("corroboration", 1) >= 2)
    print(f"  {multi} questions now have >=2 independent sources")
    print(f"  audit trail: {out/'merge-log.json'}")


def cmd_report(a):
    out = Path(a.outdir).expanduser()
    run = _read_json(out / "run.json", {})
    questions = _read_json(out / "questions.json", None)
    if questions is None:
        raw = _read_json(out / "raw" / "records.json", [])
        if not raw:
            die("no questions.json and no raw records — nothing to report")
        warn("questions.json missing; merging on the fly")
        questions, _ = merge_records(raw)
        _write_json(out / "questions.json", questions)
    sources = _read_json(out / "sources.json", [])

    run["generated"] = _now()
    _write_json(out / "run.json", run)

    company_slug = re.sub(r"[^\w一-鿿-]+", "_", run.get("company", "company"))
    stem = f"{company_slug}_{run.get('role','')}_面试题库"
    md_path = out / f"{stem}.md"
    md_path.write_text(render_markdown(run, questions, sources, lang=a.lang), encoding="utf-8")
    print(f"wrote {md_path}")

    if a.pdf:
        pdf_path = out / f"{stem}.pdf"
        if build_pdf(md_path, pdf_path):
            size = pdf_path.stat().st_size // 1024
            print(f"wrote {pdf_path} ({size} KB)")
        else:
            print("PDF not produced — see warnings above", file=sys.stderr)
            sys.exit(3)


def cmd_stats(a):
    out = Path(a.outdir).expanduser()
    qs = _read_json(out / "questions.json", [])
    raw = _read_json(out / "raw" / "records.json", [])
    rej = _read_json(out / "rejected.json", [])
    run = _read_json(out / "run.json", {})
    print(f"{run.get('company','?')} / {run.get('role','?')}")
    print(f"  raw harvested : {len(raw)}")
    print(f"  quarantined   : {len(rej)}")
    print(f"  unique        : {len(qs)}")
    if qs:
        print(f"  corroborated  : {sum(1 for q in qs if q.get('corroboration',1)>=2)}")
        print("  by round      : " + ", ".join(f"{k}={v}" for k, v in Counter(q.get('round') for q in qs).most_common()))
        print("  by category   : " + ", ".join(f"{k}={v}" for k, v in Counter(q.get('category','?').split('/')[0] for q in qs).most_common(8)))
        print("  by platform   : " + ", ".join(f"{k}={v}" for k, v in Counter(
            s.get('platform') for q in qs for s in (q.get('sources') or [])).most_common()))


def main():
    ap = argparse.ArgumentParser(description="quant interview question bank builder")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("init"); p.add_argument("outdir"); p.add_argument("--company", required=True)
    p.add_argument("--role", default="QT", choices=list(ROLES)); p.add_argument("--cycle", default="2026")
    p.set_defaults(func=cmd_init)

    p = sub.add_parser("add"); p.add_argument("outdir"); p.add_argument("--file", required=True)
    p.set_defaults(func=cmd_add)

    p = sub.add_parser("merge"); p.add_argument("outdir"); p.add_argument("--threshold", type=float, default=0.82)
    p.set_defaults(func=cmd_merge)

    p = sub.add_parser("report"); p.add_argument("outdir"); p.add_argument("--pdf", action="store_true")
    p.add_argument("--lang", default="bi", choices=["zh", "en", "bi"]); p.set_defaults(func=cmd_report)

    p = sub.add_parser("stats"); p.add_argument("outdir"); p.set_defaults(func=cmd_stats)

    a = ap.parse_args()
    a.func(a)


if __name__ == "__main__":
    main()
