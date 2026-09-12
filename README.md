# quant-interview-recon

A Claude Code skill that collects a **company-specific quant interview question
bank** and ships it as a folder of structured data plus a printable PDF.

You point it at a firm you're about to interview with:

```
/quant-interview-recon Optiver QT
```

and it fans out across every platform that actually carries US new-grad quant
interview material — Chinese and English, forums and question banks, public
and login-walled — extracts the questions, merges duplicates across languages,
scores how well-attested each one is, and writes:

```
~/Desktop/面试题库/Optiver_QT_2026-09-12/
├── Optiver_QT_面试题库.pdf     ← the deliverable
├── Optiver_QT_面试题库.md
├── questions.json              ← structured, one record per question
├── sources.json                ← what was searched, what was found, what was walled
├── rejected.json               ← quarantined spam, reviewable
├── merge-log.json              ← why each duplicate was folded
└── raw/                        ← unprocessed harvest
```

---

## Why this exists

Quant interview material is scattered across a dozen platforms in two
languages, half of it behind logins, much of it marketing spam from paid
bootcamps, and most of it about **internships** when you need **new-grad
full-time**. Searching it by hand for each firm you apply to is hours of work
that goes stale in a season.

The design follows three rules that most "interview question" scrapers break:

**Every question keeps its source.** No question enters the bank without a URL.
The PDF prints them. You can always go read the original thread.

**Gaps are labelled, not hidden.** When a platform is walled or returns
nothing, that becomes a visible row in the source ledger. A bank that
silently skipped 一亩三分地 looks identical to one that found nothing there —
so the ledger makes the difference explicit.

**Corroboration beats volume.** The same question recalled independently on
Glassdoor and 一亩三分地 is worth far more than ten questions from one post.
Cross-language dedup merges them and prints the source count.

---

## Install

```bash
git clone https://github.com/YichengYang-Ethan/quant-interview-recon.git
cd quant-interview-recon
./install.sh
```

`install.sh` symlinks the skill into `~/.claude/skills/`, so `git pull` updates
it in place. Use `./install.sh --copy` if you'd rather not have a symlink.

**Requirements**

| | | |
|---|---|---|
| `python3` | required | stdlib only, no pip installs |
| `pandoc` | for PDF | `brew install pandoc` |
| `xelatex` | for PDF | `brew install --cask mactex-no-gui` (or `brew install tectonic`) |
| Claude in Chrome | for walled sources | optional — the skill degrades to public sources without it and says so |

CJK rendering is handled automatically: the builder detects PingFang SC / Heiti
SC / Noto Sans CJK and picks what your machine has.

---

## Usage

```
/quant-interview-recon <Company> [QT|QR|QD|QA] [--deep] [--no-chrome]
```

```
/quant-interview-recon "Jane Street" QT
/quant-interview-recon Citadel Securities QR --deep
/quant-interview-recon SIG --no-chrome
```

- `--deep` runs extra gap-filling rounds until new questions stop appearing.
- `--no-chrome` skips every login-walled source; useful if your Chrome isn't
  connected or you'd rather not have it driven.

---

## The scripts, standalone

The Python does the parts that shouldn't be left to a language model's
judgement. Both run on their own:

```bash
# dedup + merge a pile of harvested records
python3 skill/quant-interview-recon/scripts/qbank.py merge ./myrun

# rebuild the PDF after hand-editing questions.json
python3 skill/quant-interview-recon/scripts/qbank.py report ./myrun --pdf

# pull candidate posts from any open Discourse forum
python3 skill/quant-interview-recon/scripts/harvest.py discourse \
    --base https://www.uscardforum.com --query "Optiver 面经" --out raw.json
```

`qbank.py` is stdlib-only and does no network I/O at all — you can read all of
it in one sitting.

---

## What it will not do

- **It will not log in as you, spend your 一亩三分地 大米, or post anything.**
  Points-gated threads are reported with their cost so you can decide.
- **It will not invent questions.** Every record needs a source URL or it is
  rejected. Thin coverage is reported as thin coverage.
- **It will not scrape paywalled question banks.** Paid sites are used only for
  what they publish openly.

---

## Honest limitations

- **New-grad full-time material is genuinely scarce.** Top prop shops convert
  most trader headcount from interns, so for several firms the honest answer is
  "the public record is mostly intern loops." The bank labels which is which.
- **NDAs distort what's posted.** Numbers get changed, onsite rounds go
  undescribed. Expect good OA/phone coverage and thin final-round coverage —
  that skew is in the sources, not in the tool.
- **Everything decays.** OA vendors and formats change yearly. The bank
  timestamps every question and flags anything over ~18 months old.
- **Confidence scores are heuristics**, not measurements. Treat the bank as a
  map of where to aim your prep, not as an answer key.

---

## Layout

```
skill/quant-interview-recon/
├── SKILL.md                 orchestration: lanes, gap loop, output contract
├── references/
│   ├── 01-sources.md        per-platform access dossier — tested URL templates
│   ├── 02-taxonomy.md       categories, record schema, confidence rubric, dedup
│   ├── 03-companies.md      firm roster, EN/中文 aliases, 2026-cycle timeline
│   ├── 04-pipelines.md      per-firm interview format, by stage
│   ├── 05-prep-stack.md     books, mental-math trainers, category→resource map
│   └── 06-chrome.md         driving logged-in Chrome, and the limits on it
└── scripts/
    ├── qbank.py             normalize · merge · render (stdlib, offline)
    └── harvest.py           headless harvesters for sources that allow it
```

The access dossier in `01-sources.md` is empirically probed, not assumed —
each URL template records whether it was tested and what came back, including
the ones that failed.

---

MIT. Not affiliated with any firm named in it. Collects only publicly posted
material; respect the NDAs you sign.
