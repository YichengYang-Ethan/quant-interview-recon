#!/usr/bin/env python3
"""
Regression tests for qbank's dedup and LaTeX escaping.

Every case here is one the pipeline got WRONG at some point against real
scraped data. Run before shipping a change to normalize/merge/tex_safe:

    python3 test_qbank.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from qbank import (  # noqa: E402
    classify_junk, merge_records, normalize_text, numbers_compatible,
    numeric_slots, similarity, tex_safe,
)

FAILED = []


def check(name, got, want):
    ok = got == want
    print(f"  {'ok  ' if ok else 'FAIL'} {name}")
    if not ok:
        print(f"        got:  {got!r}\n        want: {want!r}")
        FAILED.append(name)


def rec(q, url, plat, **kw):
    d = {"question": q, "company": "X", "role": "QT", "source_url": url,
         "source_platform": plat, "lang": "en", "confidence": 3}
    d.update(kw)
    return d


def merged_count(records, **kw):
    m, _ = merge_records([_coerce(r) for r in records], **kw)
    return len(m)


def _coerce(r):
    r.setdefault("round", "unknown")
    r.setdefault("difficulty", "unknown")
    r.setdefault("category", "uncategorized")
    r.setdefault("tags", [])
    r.setdefault("verbatim", True)
    return r


print("numbers are load-bearing")
# E=6 vs E=14. Merging these teaches a wrong answer AND claims corroboration.
check("two vs three heads in a row stay separate", merged_count([
    rec("I flip a fair coin until I get two heads in a row. Expected number of flips?", "u1", "Glassdoor"),
    rec("I flip a fair coin until I get three heads in a row. Expected number of flips?", "u2", "Reddit"),
]), 2)
check("10 vs 100 dice stay separate", merged_count([
    rec("You roll 10 dice. What is the expected number of sixes?", "u3", "WSO"),
    rec("You roll 100 dice. What is the expected number of sixes?", "u4", "Blind"),
]), 2)
check("spelled-out numbers become slots", numeric_slots(normalize_text("two heads in a row")), ("2",))
check("chinese numerals become slots", numeric_slots(normalize_text("连续两次正面")), ("2",))
# A points-walled 一亩三分地 post keeps "$1" and loses "100 turns"; it is still
# the same question as the full QuantGuide text. Subset, not equality.
check("a truncated quote still merges with the full text", merged_count([
    rec("You are playing a one-player game with two opaque boxes. At each turn, you can choose to "
        'either "place" or "take". "Place" places $1 from a third party into one box randomly. '
        '"Take" empties out one box randomly and that money is yours. This game consists of 100 '
        "turns where you must either place or take. Assuming optimal play, what is the expected "
        "payoff of this game?",
        "https://quantguide.io/questions/place-or-take", "QuantGuide", canonical_key="pot"),
    rec('You are playing a one-player game with two opaque boxes. At each turn you can choose to either '
        '"place" or "take". "Place" places $1 from a third pa',
        "https://1point3acres.com/bbs/thread-1185510-1-1.html", "1point3acres", canonical_key="pot"),
]), 1)
check("but conflicting numbers still block a canonical_key merge", merged_count([
    rec("Roll 10 dice, expected number of sixes?", "x1", "QuantGuide", canonical_key="dice"),
    rec("Roll 100 dice, expected number of sixes?", "x2", "Glassdoor", canonical_key="dice"),
]), 2)
check("missing numbers on one side is tolerated",
      numbers_compatible("expect flip coin consecutive head", "expect flip coin 2 consecutive head"), True)

print("\ncross-language merging")
# An accurate English gloss measured 0.799 against its original — under the
# 0.82 bar — so cross-language pairs get slack.
zh = rec("求最近的一个日期，使得写成 MM/DD/YYYY 形式时所有数字互不相同。", "u5", "1point3acres",
         lang="zh", question_en="Find the most recent date where all digits in MM/DD/YYYY are distinct.")
en = rec("Find the most recent date where all of the digits, when expressed in the form MM/DD/YYYY, are distinct.",
         "u6", "Glassdoor")
check("zh + en same question merge", merged_count([zh, en]), 1)
check("zh without a gloss cannot merge", merged_count([
    rec("求最近的一个日期，使得所有数字互不相同。", "u7", "1point3acres", lang="zh"), en,
]), 2)

print("\ncurated banks never self-merge")
# QuantGuide ships deliberate near-twins that score 0.91 lexically.
check("two entries in one curated bank stay separate", merged_count([
    rec("Find the most recent date where all of the digits in MM/DD/YYYY are distinct.",
        "https://quantguide.io/questions/a", "QuantGuide"),
    rec("Find the next date where all of the digits in MM/DD/YYYY are distinct.",
        "https://quantguide.io/questions/b", "QuantGuide"),
]), 2)
check("but a forum can corroborate a curated entry", merged_count([
    rec("Find the most recent date where all of the digits in MM/DD/YYYY are distinct.",
        "https://quantguide.io/questions/a", "QuantGuide"),
    rec("Find the most recent date where all of the digits in MM/DD/YYYY are distinct.",
        "https://glassdoor.com/q", "Glassdoor"),
]), 1)

print("\njunk filtering")
check("spam is rejected", classify_junk(rec("加微信 vx123 领取内推题库包过", "u8", "WeChat")) is not None, True)
check("content-free recollection is rejected",
      classify_junk(rec("总共 4 轮面试", "u9", "Blind")) is not None, True)
check("unsourced question is rejected",
      classify_junk({"question": "A fair coin is flipped ten times, how many heads?"}) is not None, True)
check("a real question survives",
      classify_junk(rec("What is the probability of a sum of 10 on three dice?", "u10", "Glassdoor")), None)

print("\nlatex escaping (all four killed a real build)")
check("json \\n leakage is stripped", "\\n" in tex_safe("first line.\\nEach player then..."), False)
check("real commands survive", "\\nu" in tex_safe("let $\\nu$ be the rate"), True)
check("double-escaped percent is collapsed", "\\\\%" in tex_safe("gas with $10\\\\%$ probability"), False)
check("latex delimiters become pandoc math", tex_safe(r"a \(6-\)sided die"), "a $6-$sided die")
check("unbalanced money dollar is escaped", tex_safe("base salary is $150,000 a year"),
      "base salary is \\$150,000 a year")
check("balanced math is left alone", tex_safe("$P(X>1)$ is what?"), "$P(X>1)$ is what?")

print("\nglyphs (PingFang+Helvetica lack these; ● dies in italic)")
for bad in "●○■□▪▇▰▱◆★☆":
    if bad in tex_safe(f"confidence {bad} here"):
        FAILED.append(f"unsafe glyph {bad} reaches output")
print(f"  {'ok  ' if not any('unsafe glyph' in f for f in FAILED) else 'FAIL'} "
      f"no unsafe glyph is introduced by tex_safe")

print("\nemoji and symbols (authored sections and forum text both carry them)")
check("warning sign keeps a visible marker", tex_safe("\u26a0 careful"), "! careful")
check("star becomes asterisk", tex_safe("\u2b50 top pick"), "* top pick")
check("emoji are dropped, not left to tofu", tex_safe("nice \U0001F642 ok"), "nice  ok")
check("variation selector is dropped", tex_safe("\u26a0\ufe0f x"), "! x")
check("CJK is untouched", tex_safe("\u6982\u7387\u9898"), "\u6982\u7387\u9898")

print()
if FAILED:
    print(f"{len(FAILED)} FAILED: {FAILED}")
    sys.exit(1)
print("all passed")
