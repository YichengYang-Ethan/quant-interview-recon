# 01 · Source access dossier

Every template below was **empirically probed on 2026-09-12**, and every failure
recorded here is one that was actually observed. Templates marked ✗ are listed
precisely so nobody re-derives them and ships them.

Re-probe if this file is more than ~6 months old. Cloudflare rules, Next.js
build ids, and forum slugs all rot.

---

## Policy gates — read before fetching anything

Two constraints are non-negotiable. They are not technical limits; both sites
below serve the content fine. They are about what we're entitled to take.

### A. `robots.txt` disallows ClaudeBot on three of these sites

Observed, site-wide `User-agent: ClaudeBot → Disallow: /`:

| Site | Also disallows | Signal header |
|---|---|---|
| `quantnet.com` | — | `search=yes, ai-train=no, use=reference` |
| `teamblind.com` | `anthropic-ai`, GPTBot, CCBot, Google-Extended | — |
| `brainstellar.com` | — | `search=yes, ai-train=no, use=reference` |

**Do not run automated fetches against these three.** Blind in particular
*will* serve a WebFetch a full post body — the wall is policy, not technology,
and "it worked" is not permission.

What is still fine, and is what the skill does instead:

- **Search-engine results.** All three signal `search=yes`. Reading an indexed
  title or snippet, and citing the URL, is the use they permit.
- **Opening a page in the user's own browser** when a specific thread is worth
  reading. That is the user browsing, not us crawling. Keep it to a handful of
  targeted reads, never a sweep.

### B. Never extract PuzzledQuant premium solutions

The anonymous RSC endpoint returns full solution text for all 165 `isPremium:
true` problems — the paywall is enforced only in a client UI that never
renders. That is a paywall bug, not an API.

**Filter on `isPremium` and keep only `false`.** Free problems there are
plentiful and legitimate.

---

## Priority 1 — must hit

### 一亩三分地 · 1point3acres.com

The single best Chinese source. It is **two sites with opposite rules** under
one domain; getting this wrong is the most common way to conclude "blocked".

| Path | Access | Note |
|---|---|---|
| `/interview/*` | ✓ plain curl / WebFetch | **A plain UA works; a full Chrome UA gets 403.** Do not "helpfully" spoof a browser. |
| `/bbs/*` | Chrome MCP only | 403 to curl, Chrome-UA curl, and Googlebot alike |

**Mechanism A — cheap, run first, no browser.** JSON with no login:

```
https://www.1point3acres.com/interview/company/{slug}                        (130 KB HTML)
https://www.1point3acres.com/_next/data/{buildId}/interview/company/{slug}.json   (8.8 KB — prefer this)
```
Resolve `buildId` per run by grepping `"buildId":"..."` from any page — it
changes on redeploy (observed `KL6iNX1EmQhACwy4fxBx1`). Then parse
`pageProps.trpcState.json.queries[]` and take the query whose `state.data.data`
is a list.

Probed `total` values: `optiver` 421, `citadel` 923, `sig` 377, `imc` 307,
`twosigma` 355, `drw` 263, `janestreet` 158.

> **⚠ Silent no-op pagination — verified 2026-09-12.** `?page=N` is ignored.
> Fetching pages 1–4 for `janestreet` returned **80 rows containing 20 unique
> tids** — the same newest 20, four times — while still reporting
> `total: 158`. There is **no tRPC/REST route** for the rest (`/api/trpc/…`,
> `/trpc/…` all 404). Treat this endpoint as "newest 20 only"; the remaining
> threads need Chrome on `/bbs/tag/…`. Never report `total` as the number
> harvested.

Each row carries a facet block — the only machine-readable NG-vs-intern signal
on any platform probed:

```json
{"tid": 1188886, "subject": "Jane Street SWE Intern R1 面经",
 "enSubject": "...", "dateline": 1788933812, "replies": 0,
 "options": {"company":"janestreet","jobyear":16,"jobseason":3,
             "jobcategory":1,"jobtype":2,"fresh":1}}
```

`jobtype` decoded by correlating against title text over 20 Jane Street threads:
**`2` = 实习/intern** (9 rows, 8 of them titled Intern), **`1` = non-intern**
(11 rows). Filter on `jobtype == 1` for NG full-time. `jobcategory` /
`jobseason` codes were not resolvable from this sample — do not guess them.

```
https://www.1point3acres.com/interview/problems/company/{slug}
```
✓ Question **titles are free** (61 catalogued for Optiver: 18 coding, 1 system
design, 1 behavioral, 32 OJ). Bodies are gated.

> **⚠ The UA rule is inverted here — re-verified 2026-09-12.** On `/interview/*`
> a plain `curl/8.4.0` UA returns **200** and `Googlebot/2.1` returns **200**,
> but a full desktop Chrome UA string returns **403**. Spoofing a browser to
> "be polite" is exactly what breaks this endpoint. Send a plain UA.
> (`/bbs/*` is the opposite: 403 to curl, Chrome-UA curl *and* Googlebot alike.)

**Mechanism B — Chrome, for the 面经 threads.**

```
https://www.1point3acres.com/bbs/tag/{slug}-{TAG_ID}-{page}.html
```
✓ `optiver-8331-1` → 505 主题 / 438 面经 / 26 pages. `janestreet-2069-1` → 280
主题 / 215 面经. `Quant-9652-4` → 233 主题 / 12 pages. The trailing digit is the
page and does paginate. Find `TAG_ID` via `WebSearch site:1point3acres.com
{company} 面经`.

> **⚠ The slug is cosmetic — only `TAG_ID` selects the tag.**
> `/bbs/tag/optiver-1-1.html` returns **HTTP 200 serving tag id 1**, which is
> 「录取汇报：研究生」 (157k grad-admission threads) — not Optiver. A wrong id
> fails **silently, with plausible-looking content**. Always confirm the
> rendered page header names the company you asked for.

```
https://www.1point3acres.com/bbs/thread-{tid}-1-1.html
```
✓ renders, but many threads show **需要積分 105–188**.

**The gate leaks, and that is the highest-yield trick on this platform.**
Three things stay readable on a gated thread:

1. **Head and tail of the body.** The `[hide]` span is withheld but the text
   around it is not. Observed on tid 1185510 as a guest:
   *"You are playing a one-player game with two opaque boxes. At each turn, you
   can choose to either 'place' or '"* `[GATE]` *"cumulative sum of your rolls
   at any time but lose everything if you hit a square number 1, 4, 9, 16, ..."*
2. **Every reply.** Replies are never points-gated and routinely reconstruct
   the hidden question. On a gated Jane Street QR thread the replies gave
   `play for 5-20 for first round, and at most 4 times re-play`, `从最大数字的机器
   开始一个个turn on？`, `贝叶斯概率问题。` — enough to identify it as a Bayesian
   optimal-stopping machine-selection game.
3. **The structured metadata line** (年度 / 类别 / 全职-实习).

So: on a gated thread, harvest the teaser, the metadata line, and all replies.
Tag the record `gated-body` and **cap `confidence` at 3** — and if you had to
reconstruct the question rather than read it, set `verbatim: false`. A
reconstruction must never be citable later as a verbatim sighting.

✗ `/bbs/search.php?...` — guests get 「您所在的用户组(游客)无法进行此操作」. Dead.
✗ `/interview/thread/{tid}` — guest gets title + a one-line AI abstract; the
body is rendered to a `<canvas>` with zero DOM text, so there is nothing to
scrape even in Chrome.

> **大米 rule.** Points-gated threads cost a balance the user earned. **Do not
> unlock them.** Report thread + cost and let the user choose. (`06-chrome.md`)

---

## Priority 2 — should hit

### Glassdoor

Hard-walled to every server-side fetch (403 Cloudflare, all mirrors incl.
`.co.uk`). But it has the best NG-vs-intern role separation of any platform,
and there is a clean way in.

**The trick: the question is in the page title.** Individual question pages
title themselves `<Company> Interview Question: <FULL QUESTION TEXT> | Glassdoor`,
and that title is what search engines index. So:

```
WebSearch  allowed_domains:["glassdoor.com"]   query: {company} {role} interview question
```
Parse the **titles**. Zero fetches, no wall, full question text. This is the
primary mechanism.

Real yield from the probe: *"You have 100 dice, every time you roll the dice,
you remove the one have points larger than 3… What is average points you have
on the dice finally"* (Optiver QR, dated 2026-09-04).

URL shapes, for citation and for targeted Chrome reads:

```
✓ /Interview/{Company-Dashed}-Interview-Questions-E{id}.htm
✓ /Interview/{Company-Dashed}-Interview-Questions-E{id}_P{n}.htm          (5 per page)
✓ /Interview/{Company-Dashed}-Interview-Questions-E{id}.htm?filter.jobTitleExact={Role+Encoded}
✓ /Interview/{...}-QTN_{qid}.htm                                          (title carries the question)
```
Employer ids probed: Optiver `243355`, Jane Street `255549`.
The `EI_IE{id}.0,{C}_KO{C+1},{C+1+R}` role form works, where `C` = company slug
length and `R` = role slug length — but `filter.jobTitleExact` is easier and
does the same job.

✗ Never WebFetch glassdoor.com. Guaranteed 403. Do not retry, do not UA-spoof.

### Wall Street Oasis

Cloudflare 403 to every fetch → **Chrome MCP mandatory**, no login needed.

```
✓ https://www.wallstreetoasis.com/company/{slug}/interview
✓ https://www.wallstreetoasis.com/company/{slug}/interview?page={N}
✓ https://www.wallstreetoasis.com/company/{slug}/interview/{entry-slug}
```

> **Silent-failure trap.** A wrong slug returns **HTTP 200 with "0 Entries"**,
> not a 404. `jane-street` → 0. `jane-street-capital` → **353**. Optiver → 260.
> Always resolve the slug with `WebSearch site:wallstreetoasis.com {company}
> interview` first, and **assert the entry count is > 0** before believing an
> empty result.

Entries state the role verbatim ("QUANTITATIVE TRADER INTERVIEW — PROP TRADING"
vs "QUANT TRADING INTERN INTERVIEW"), so NG/intern is separable without guessing.

### LeetCode — GraphQL only

HTML is Cloudflare-403. The **unauthenticated GraphQL API works**:

```
POST https://leetcode.com/graphql
```

1. Resolve the tag: `ugcArticleSearchTags(keyword:"citadel")` → `[citadel, citadeloa]`.
   (`"jane"` → `jane-street`; `"susquehanna"` → SIG's slug; `"akuna"` → `akuna-capital`.)
2. List — **all four arguments are required; omitting any gives HTTP 400**
   (re-verified 2026-09-12):

   ```graphql
   query{ ugcArticleDiscussionArticles(
            keywords: [], tagSlugs: ["jane-street"],
            first: 30, skip: 0, orderBy: MOST_RECENT
          ){ totalNum edges { node { topicId title createdAt } } } }
   ```
   → `totalNum` 15 for `jane-street`, 32 for `optiver`.
3. Body: `ugcArticleDiscussionArticle(topicId:{id})`.
4. Replies: `topicComments(topicId:{id}, orderBy:"newest_to_oldest")`.

> **Silent-failure trap.** An invalid `tagSlug` does **not** error — it drops
> the filter and returns the entire Discuss corpus. Signature: `totalNum ==
> 3000`. Treat 3000 as "my tag was wrong", never as a jackpot.
> Also: `slug:"citadel-securities"` → `Tag not found`. Use `citadel`.

Best for **QD / SWE OA** at quant firms. Thin for QT/QR.

### Reddit — logged-in Chrome only

WebFetch is refused at tool level; plain HTTP is 403 "blocked by network
security" for every UA tried (I confirmed this independently). Inside the
user's Chrome, the JSON endpoints work:

```
✓ /r/{sub}/search.json?q={company}&restrict_sr=1&sort=new&t=year&limit=100
✓ /r/quant+quantfinance+FinancialCareers+csMajors/search.json?q={company}&...   (multireddit "+" works)
✓ {permalink}.json?limit=500&depth=8&sort=top        (returns a 2-element array; [1] is the comments)
✓ &after={t3_xxx}                                     (pagination; null = end)
```
Prefer `javascript_tool` running `fetch(url, {credentials:"include"})` inside
an open Reddit tab over navigating to the JSON URL — navigating dumps ~53 KB of
raw JSON into context per query.

> **⚠ Scrape the megathreads, not the post listing.** r/quant funnels interview
> talk into *"Weekly Megathread: Education, Early Career and Hiring/Interview
> Advice"*. A full year of `sort=new` search for "interview" returned only ~7
> standalone posts, two of which **were** megathreads. Post-level scraping of
> r/quant returns almost nothing; the content is in the megathread comment
> trees. Fetch those with `{permalink}.json?limit=500&depth=8`.

Heavily intern-skewed. Good for atmosphere, timelines, and TC; weak for verbatim questions.

### 知乎 zhihu.com

A JS/browser challenge, not an account wall — but operationally **Chrome only**.

```
✓ /search?type=content&q={company}+面经        ← navigate here first; it mints the __zse_ck cookie
✓ /api/v4/search_v3?t=general&q={q}&offset={0,20,40}&limit=20     (in-page fetch only; curl → 403)
✓ /api/v4/questions/{qid}/answers?...                              (in-page)
✓ /question/{qid}     ·  zhuanlan.zhihu.com/p/{article_id}
✗ /api/v4/articles/{id} — 403 code 10003 even from a good session
```

Richest source of **first-person full-loop narratives** (one Jane Street thread
yielded four verbatim questions). But see the spam warning: much of the 2026
quant 面经 in 专栏 is lead-gen for **interview-cheating services** — one probed
post was headlined 「vo-oa面试辅助指导」. Filter hard (`02-taxonomy.md`).

### QuantGuide.io — company-tagged drill bank

Fully open, no login, no Cloudflare.

```
✓ https://www.quantguide.io/questions           → one GET returns the WHOLE catalog
                                                   (1,204 unique questions, company-tagged)
✓ https://www.quantguide.io/questions/{slug}    → free question bodies
✗ /questions?company=Optiver                    → 200 but byte-identical; the filter is client-side
```
**Unescape it correctly — a naive `.replace('\\"', '"')` silently truncates
questions.** The payload is triple-escaped: it lives inside a JS string
literal, and question text contains its own quotes and `\$`. A blind replace
corrupts the escaping and the regex stops at the first inner quote — "Place or
Take" came back as 97 characters of its real 455, ending mid-sentence, with no
error. Let `json.loads` do exactly one level:

```python
flight = []
for m in re.finditer(r'self\.__next_f\.push\(\[\d+,\s*("(?:[^"\\]|\\.)*")\s*\]\)', html, re.S):
    try: flight.append(json.loads(m.group(1)))   # one correct level of unescaping
    except ValueError: pass
blob = "".join(flight)                            # ~637 KB, normal JSON escaping
for m in re.finditer(r'"prompt":"((?:[^"\\]|\\.)*)"', blob):
    text = json.loads('"' + m.group(1) + '"')
```

Question objects in `blob` look like:

```json
{"id":"pjSCKiq39SvESirmwFq4","title":"Place or Take","difficulty":"hard",
 "topic":"probability","isPremium":false,"companies":[{"company":"Jane Street"}],
 "tags":[{"tag":"Games"},{"tag":"Expected Value"}],"urlEnding":"place-or-take"}
```

Counts verified 2026-09-12: 948 unique questions in the catalog; Jane Street
tagged 133 (matching the site's own filter chip), of which 78 free / 55 premium.

> **⚠ KaTeX digit corruption — the worst trap in this file.** Via WebFetch,
> `$5$` renders as `555` and `$7$` as `777`. **Every numeric parameter would be
> silently wrong.** Use raw curl + the JSON `prompt` field. Never WebFetch this site.

Company tags are drill hints, not attestations that the firm asked it. Score
accordingly (`confidence` ≤ 3, `round: unknown`).

### PuzzledQuant

```
✓ https://www.puzzledquant.com/sitemap.xml                      → 618 locs (454 problems, 39 discussions)
✓ https://www.puzzledquant.com/problems/{id}   header: RSC: 1   → 411/454 full JSON
✓ https://www.puzzledquant.com/discussions/{id} header: RSC: 1  → e.g. "SIG | QR | Interview experience"
✗ /company/{x}, /companies/{x}, /tag/{x}  → all 404. No company namespace.
✗ /?company=Optiver → 200 but carries no problem data
```
163 of 454 problems carry company tags. **Keep only `isPremium: false`** (see
policy gate B). Content skews India-heavy; check applicability before including.

### quantquestions.io

100% JS-rendered CRA + Firestore. curl/WebFetch return a 2.7 KB shell for every
route; Firestore REST is 403 and anon auth is disabled. **Chrome only.**

```
✓ /playlist/{firm-slug}     → e.g. /playlist/optiver: 60 problems, 18 topics, first ~3 titles free
✓ /problems/{slug}          → stem free, solution paid
```
Take stems, leave solutions.

---

## Priority 3 — optional

### QuantNet
`robots.txt` disallows ClaudeBot; Cloudflare 403s everything anyway (HTML, RSS,
sitemap — only `/robots.txt` returns 200). **`WebSearch site:quantnet.com
{company} interview questions` is the only mechanism.** It works well: thread
URLs come back correctly shaped as `/threads/{slug}.{id}/`, and snippets carry
real questions (a Jane Street 100-sided-die reroll problem; the Optiver
"ZAP-N" / "Brain Circuit" screen names).

### 美卡论坛 uscardforum.com
Discourse JSON, no auth — but **only via `www.`** and **only the `/t/topic/`
form**:

```
✓ https://www.uscardforum.com/t/topic/{id}.json          ← curl works, no login
✓ https://www.uscardforum.com/t/topic/{id}.json?page={n} ← chunk_size 20
✗ https://uscardforum.com/...        (apex → 403)
✗ https://www.uscardforum.com/t/{id}.json   (canonical Discourse form → 403)
✗ /search.json?q=...  via curl → 403; works in Chrome
```
`scripts/harvest.py discourse` implements this. Small NG-quant yield — a 面经
search also returns green-card timelines — so filter by relevance. Topic 72833
(「Quant面经」) is the known good thread.

### Brainstellar
`robots.txt` disallows ClaudeBot → **search-index / user-directed reads only**,
despite the Gatsby `page-data` JSON being wide open. 101 puzzles, all with
worked solutions. Zero company attribution — a topic drill source, never
company intel.

### OpenQuant.co
`robots.txt`: `Allow: /`. Fully open, no rate limit.

```
✓ https://openquant.co/_next/data/{buildId}/questions.json            → 190 questions
✓ https://openquant.co/_next/data/{buildId}/questions/{slug}.json     → bodies + solutions
✓ https://openquant.co/sitemap-0.xml
✗ /companies/{x}, /company/{x}, /interview/{x}, /questions/{x}        → all 404
```
> **`buildId` rots on every redeploy — never hardcode it.** Resolve per run by
> grepping `"buildId":"..."` out of any page's `__NEXT_DATA__`. A stale one 404s.

**Zero company attribution** (verified by searching all 190 records). Topic drill only:
Probability 89, Brainteaser 49, Statistics 18.

### Official company pages
Highest-trust primary source for **process and format**, and never walled.
Jane Street puzzles archive, Optiver's own assessment description, G-Research's
recommended reading. Always run this lane; it's cheap and it anchors
`04-pipelines.md`.

---

## Quick reference

| Source | Mechanism | Priority | Best for |
|---|---|---|---|
| 一亩三分地 `/interview` | curl, **plain UA** | 1 | NG×FT×Quant facet, counts |
| 一亩三分地 `/bbs` | Chrome | 1 | 面经 threads (mind 大米) |
| Glassdoor | **WebSearch titles** | 2 | verbatim Qs, role split |
| WSO | Chrome | 2 | process, role-labelled entries |
| LeetCode | GraphQL POST | 2 | QD/SWE OA |
| Reddit | Chrome in-page fetch | 2 | atmosphere, timeline, TC |
| 知乎 | Chrome | 2 | full-loop narratives |
| QuantGuide | curl (**never WebFetch**) | 2 | company-tagged drills |
| PuzzledQuant | curl + `RSC: 1` | 2 | curated Qs (free only) |
| quantquestions.io | Chrome | 2 | firm playlists (stems) |
| QuantNet | WebSearch only | 3 | classic Qs, screen names |
| 美卡论坛 | curl `www` + `/t/topic/` | 3 | Chinese supplement |
| Brainstellar | search-index only | 3 | brainteaser drills |
| OpenQuant | curl + live buildId | 3 | topic drills |
| Company sites | WebFetch | 1 | process, official format |
