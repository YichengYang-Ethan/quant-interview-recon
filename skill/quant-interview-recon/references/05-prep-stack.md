# 05 · Prep resources by category

Read the category mix in the bank this run produced, then hand the user drills per category from §6. Every price, URL and status below was verified 2026-09-12; anything unverified is marked, and the marking must survive into whatever you tell the user.

## 0 · Dead — never recommend these

All three appear in most "quant prep resources" listicles and r/quant megathreads. All three were tested 2026-09-12.

| Resource | Status | Symptom |
|---|---|---|
| **TraderTest.org** | DEAD ≥ Jan 2022 (4.5+ yrs) | HTTPS refused (443 closed). Over HTTP: *"After 8 years reality finally caught up with the server this site was running on and killed it."* `test.php` → 500, `tests.php` → 404. Same notice in Wayback captures 2022-01-22, 2023-02-01, 2023-12-12, 2024-02-22, 2024-12-03, 2025-01-15. |
| **RankYourBrain** | DEAD | Cert mismatch (`CN=dhm104.savviihq.com`); over HTTP a Plesk default page — *"You see this page because there is no Web site at this address."* `/mental-math` 404 in Wayback since 2025-01-20, again 2026-01-21. |
| **thequantguide.com** (the $3,500 course) | DEAD, 404 | Webflow 404 on `https://`, `https://www.`, `http://`. DNS still resolves (198.202.211.1). Last Wayback 200: 2024-05-06. |

Two footnotes that still have value. TraderTest's surviving book list at `http://www.tradertest.org/media.php` is readable and still sane (Sticker *How to Calculate Quickly*, Natenberg, Hull). RankYourBrain's death is corroborated by r/quant [*"Where did rank your brain go?"*](https://old.reddit.com/r/quant/comments/192t17m/where_did_rank_your_brain_go/) — *"all the hyperlinks go to nowhere"* — where one commenter claims a revival at `rankyourbrain.net` and a reply one month ago says the link didn't work; **`.net` untested, unverified.**

Losing RankYourBrain matters operationally: it was *the* sequence trainer. §2 has the only verified free replacement.

## 1 · The four canonical books

| Book | Current ed. / ISBN | Published | Pages | Price 2026-09-12 |
|---|---|---|---|---|
| **Green Book** — Zhou, *A Practical Guide To Quantitative Finance Interviews* | No numbered new edition exists. Two live listings of the **same** book: 978-1438236667 (CreateSpace), 978-1735028804 (self-pub) | 2008-04-09 / 2020-05-05 | 209 both | $26.20 / $26.00 |
| **Heard on the Street** — Crack | 27th ed., 978-1067058340 | **2026-09-03** | 424 | $45.00 |
| ↳ prior edition | 978-1067058326 | 2025-08-25 | 422 | used from ~$10 |
| **Quant Job Interview Q&A** — Joshi, Denson, Downes | 2nd ed., 978-0987122827 (Pilot Whale). Joshi died 2017; no 3rd ed. exists | 2013-05-25 | 388 | $44.84–48.96 |
| **150 Most Frequently Asked Questions** — Stefanica, Radoičić, Wang | 3rd ed., 978-1734531244 (FE Press) | 2024-11 | 331 | $29.04 Amazon / $38.50 list ([fepress](https://www.fepress.org/150iqs-third-edition/)) |

Two facts that change what the user buys:

- **The Green Book has no "latest edition" to chase.** The 2020 ISBN is a re-release of the identical 209-page 2008 book. Buy whichever is cheaper; ignore any site claiming a newer edition.
- **Heard on the Street turned over nine days ago.** The 27th is full price; the 26th (Aug 2025) and 24th (Sept 2023) are ~$10 used. Crack self-publishes annually and adjacent-edition drift is small, so a one-year-old edition is the value buy. Crack's own listing warns against buying an old edition by mistake — the flip side is that the annual cadence is partly a business model.

### Green Book

Contents per the publisher description: brain teasers · calculus · linear algebra · probability · stochastic processes & stochastic calculus · finance · programming. 200+ problems.

- **QT** — the brainteaser and probability chapters are the highest-density-per-page material in the entire canon. This is the book r/quant reflexively names.
- **QR** — probability + stochastic processes/calculus + linear algebra.
- **QD** — the programming chapter is thin and dated. Skip it; use §5.

### 150 FAQ

Section structure from the [publisher's own 2nd-ed TOC PDF](https://www.fepress.org/wp-content/uploads/2019/12/150iqs-second_ed-table_of_contents.pdf): §2.1 math/calculus/ODEs · §2.2 covariance & correlation matrices, linear algebra · §2.3 financial instruments (options, bonds, swaps, forwards, futures) · §2.4 **C++ and data structures** · §2.5 Monte Carlo & numerical methods · §2.6 probability & stochastic calculus · §2.7 brainteasers. The 3rd ed. adds **statistics and machine learning for the first time**, plus more C++/data structures, finance, math and brainteasers; 200+ questions total.

- **QD** — §2.4 + §2.5 are the only real C++/data-structures coverage in the canon, and the reason to own this book.
- **QR** — §2.2 + §2.6 + the new stats/ML block, which is what justifies buying the 3rd ed. over a used 2nd.
- **QT** — §2.7 + §2.3, but the Green Book beats it here.
- Format is a pocket book with solutions in a separate back half: good for spaced self-testing, bad cover-to-cover.

### Joshi

Organised around *what the interviewer is testing*, not by topic. Strongest on option-pricing reasoning, "how would you price X", C++ questions, and — uniquely — a substantial chunk on how quant hiring actually works and what the roles are (r/quant's wiki still points at a summary derived from it).

- **QR/QD at banks and derivatives shops** — best of the four.
- **QT at prop/MM shops** — weakest of the four. It is a 2013 book written for a derivatives-desk world.
- **Weakness:** $45–49 for a 13-year-old book is the worst price-per-value of the set for a 2026 QT candidate. Buy only if QR/derivatives-targeted.

### Heard on the Street

Pure quant/logic · financial economics · derivatives · statistics, plus a large non-quantitative interview section (267 questions in recent editions).

- **QT** — the brainteaser/logic half, yes.
- **QR** — the statistics and financial-economics sections.
- **QD** — skip almost entirely.
- **Weakness:** it draws from *all* interview types (corporate finance, S&T, MBA-level), so it has the highest off-target fraction of the four for a prop-shop QT.

## 2 · Mental-math trainers

### Zetamac, exact default config

**`https://arithmetic.zetamac.com/game?key=a7220a92`**

The config JSON the page injects:

```
init({"add":true,"sub":true,"mul":true,"div":true,
      "add_left_min":2,"add_left_max":100,"add_right_min":2,"add_right_max":100,
      "mul_left_min":2,"mul_left_max":12,"mul_right_min":2,"mul_right_max":100});
```

This matches the homepage form defaults exactly — addition 2–100 + 2–100, multiplication 2–12 × 2–100, all four operations on. Duration is absent from the config and `app.js` has `const duration = options.duration || 120;`, so **the key resolves to the canonical 120-second game**. This is the URL people mean by "60 on Zetamac".

Two mechanics worth knowing:

- Zetamac POSTs a per-problem log (problem, answer, keystroke sequence, ms elapsed) to `/log`, and sets `entry: null` on a detected paste, non-numeric input, or over-long typing. It is instrumented against cheating.
- Appending `pink` to the URL only recolours the banner — which tells you `key` is an opaque 8-hex config handle, not a score token.

### Score targets — provenance matters more than the number

**No firm publishes a Zetamac threshold, and no reported number is independently verifiable.** Carry that caveat whenever you quote these.

| Reported claim | Who reported it | Weight |
|---|---|---|
| Practised to **40+ on default**, then cleared Optiver's mental-math stage and reached Optiver final round | [u/rzch_, r/quant](https://old.reddit.com/r/quant/comments/pxkf86/what_score_should_i_be_getting_on_the_mental/) | The single most useful point in the thread — it ties a score to a named outcome. Same user later: *"these days I consider 60+ to be a good score for me,"* but he became a QR, *"which didn't need super-fast mental maths skills to get through the door."* |
| Prepping at "consistent 60's with some 70's"; hitting 40s by day 2–3 | u/6MrStonks9, same thread | Self-reported, no outcome attached |
| "30–60 good… 60 being required for some jobs and elite for the general population" | u/Ok_Permit_3687, same thread | Opinion, no outcome |
| 45 first try → ~75 after a week | u/Training-Farmer7990, same thread | Trajectory, not a threshold |
| 20 → mid-40s after 1 week → **80s–90s after 3–4 weeks** | [u/mathememer, "Zetamax: Modern Zetamac", 130 pts](https://old.reddit.com/r/quant/comments/1gqckgl/zetamax_modern_zetamac/) | Best-documented improvement curve. His own conclusion: *"stop stressing about hitting specific scores."* |
| "120+ in 2m is borderline impossible" | u/MaterialOkra6645 | Useful ceiling |
| A successful mid-career HFT trader scoring **14** — *"my zetamac score this morning was like 14 lol"* | [r/quant thread neighbour, 182 pts](https://old.reddit.com/r/quant/comments/pxkf86/) | Best available evidence that the score does not measure trading ability |

Practical read: 40+ on the default config is the only score tied to evidence of clearing a real gate. 55–70 is where self-reported competitive candidates sit. Above ~75 the user is optimising a metric no employer sees, and the number is contaminated by typing speed and numpad use.

**The counterweight is first-party.** Jane Street's own prep PDF (§4) lists *"You have to be really good at mental math"* under **"Here are some common myths"**:

> "Numeracy certainly helps in our interviews… At the same time, we're not going to judge you harshly for not being able to mentally multiply double-digit numbers in 5 seconds."

### Optiver "80 in 8"

Widely described as 80 arithmetic questions in 8 minutes, **+1 correct / −1 wrong**, no skipping. Reported pass bars: *"forums suggest around 65 would be passing"* (from a candidate who reached Q72 and cleared) and *"You need like a score of 55+ I believe"* ([r/quant thread](https://old.reddit.com/r/quant/comments/w3cbr9/optiver_80_in_8_assessment/)). **All ~4 years old, anonymous, unverifiable.**

The 2026 caveat must be passed to the user: [Optiver's own Career Kickstarter – Trading 2026 posting](https://www.optiver.com/join-us/jobs/institutional-sales-and-trading/amsterdam/career-kickstarter-trading-2026/) describes only *"an online assessment… must be completed by 20 September"* plus a technical interview Sept–Oct. Optiver publishes nothing about the assessment's contents. Third-party claims that the 2026 OA is now sectioned as "NumberLogic / Beat the Odds / Zap-N / coding" come only from SEO content farms (quantvault.org, quantt.co.uk, techprep.app, quantblueprint.com) — **unconfirmed; treat 80-in-8 as possibly obsolete.** Whether pen and paper are allowed is also unresolved: Reddit candidates say *"No paper and mental math"* and no calculator; commercial prep sites say pen and paper are allowed.

### What is actually live

**OpenQuant Game Room — `https://openquant.co/math-game`** (free, verified live) is the practical successor. Eight modes, mapping unusually well onto real OAs:

- Arithmetic · Arithmetic Pro — Zetamac-equivalent
- **Sequence Game** — the category that died with RankYourBrain; sequences appear in Optiver/Flow OAs
- **"Optiver 80 in 8"** — a direct simulator of the named test
- Memory · Risk · Flexibility · Letter Speed — these mirror "Zap-N"-style reaction/dual-task mini-games

Provenance is good: built by u/AliBuilds and [announced on r/quant](https://old.reddit.com/r/quant/comments/si5ocb/aggregate_of_quant_interview_prep_resources/) as *"I rebuilt zetamac to have a leaderboard + a new game mode to practice sequence questions"*; r/quant's wiki credits the same author. **Caveat: the all-time leaderboard is contaminated** — top Arithmetic reads 1884, then 208, 183, 182. Use the "Today" board or personal history as the reference point.

**QuantGuide** includes a mental-math simulator in its free Basic tier — confirmed from the pricing page only. `/mental-math` and `/quentify` both 404 to an anonymous fetch (client-side routing/login), so the direct URL is **unverified**.

Community Zetamac clones surfaced on r/quant, **none tested**: `zetamonkey.com`, `monkeymac.vercel.app`, `zetamac-tui` (pip-installable, local SQLite), CalcAllen.

## 3 · Question banks, free vs paid

| Platform | Free tier | Paid | Verified detail |
|---|---|---|---|
| [**Brainstellar**](https://brainstellar.com/puzzles/) | Fully free, no account | — | ~109 puzzles: Easy 31 / Medium 40 / Hard 26 / **Deadly 4**, plus Discrete Maths, Probability, Strategy, General Tricks. Each puzzle is Hint → Answer → Solution (verified on "Drunk Passenger"). Best free-signal ratio of anything here. |
| [**OpenQuant**](https://openquant.co/questions) | **190 questions, free, no paywall** | — | "Roll the Dice" random practice plus a simulated **Online Assessment** mode; solutions on YouTube. Free [study guide](https://openquant.co/guide) split QR vs QT with real written content. The site's actual business is a job board. |
| [**QuantGuide**](https://www.quantguide.io/pricing) | Basic: non-premium questions, personalized analytics, mental-math simulator | **$20/mo billed annually ($240/yr)** or $35/mo monthly | 1,000+ questions. Premium unlocks the premium subset, **solutions and hints to every question**, and **company filters**. Company tags observed live: SIG 146, Jane Street 133, Citadel 84, Goldman 72, Five Rings 70, Akuna 64, WorldQuant 56, DRW 50, IMC 45, Virtu 43. Playlists "Quant Trader 75", "Top 50". |
| [**Quantable**](https://www.quantable.io/pricing) | 600+ questions, **no solutions, no hints** | $19.99/mo annual · $29.99/mo on a 4-month "Recruiting" plan · $34.99/mo monthly | Claims 1500+ premium questions in its comparison table but "over 850 premium questions" in its own FAQ — **internally inconsistent; flag it if you quote a count.** |

**Both major freemium banks paywall the solutions, not the questions.** QuantGuide Basic and Quantable free both hand over questions with no worked answers. That is exactly the gap a scraped bank plus generated solutions fills, and it is what the community recommends:

> "just do green book/brainstellar/50 challenging problems in probability/**quantguide free questions + use chatgpt thinking mode to generate solutions (no need to upgrade to premium)** and openquant"
> — [u/According-Jump-978](https://old.reddit.com/r/quant/comments/1sltsh5/sites_like_getcracked_io_are_pure_scam/), self-described incoming quant dev at a tier-1 firm

Pass on the caveat: LLM-generated solutions to probability brainteasers are wrong often enough that they must be checked against the Green Book / Mosteller / Brainstellar wherever problems overlap, and treated as drafts otherwise.

## 4 · Free first-party material

**Jane Street, *Probability & Markets* — `https://www.janestreet.com/static/pdfs/trading-interview.pdf`** (live, 1,108,302 bytes, 12 pages).

Sections: Introduction · Randomness · Counting · Probabilities · Independence · Random Variables · Expected Value · Confidence Intervals · Conditional Probability · **Making Markets** · **Adverse Selection** · Problem Solving Tools · **Interview Thoughts**.

It is the best free market-making resource in existence and it teaches the literal floor grammar a MM round expects you to produce:

> "If you want to try to buy 10 widgets for a price of $2 each, say 'I'm 2 bid for 10.'" … "it's much more common to say **'I'm 2 at 4, 10 up.'**" … someone trades against you by saying **"sold"** to hit your bid or **"take 'em"** to lift your offer.

And the heuristic market-making questions are actually testing:

> "Conditional on my order being filled, what do I think the expected value of the security is? Given this updated expected value, would I be happy to have done the trade?"

Its "Interview Thoughts" section debunks four myths: mental math, complicated math, wrong answers = failure, and "you should act confident". Note one unverified detail: the PDF sits under `/static/pdfs/` and no linking page could be found — `/join-jane-street/interview-process/` 404s — so its *official status* is unverified, though the content is unambiguously Jane Street's own.

Free QR-specific texts, from [a 308-point r/quant post by u/sudeepraja](https://old.reddit.com/r/quant/comments/1f621hf/3_small_books_that_helped_me_prep_for_quant/); the first two link-verified live (HTTP 200, `application/pdf`):

- Ipsen, *Numerical Matrix Analysis* — **free full book**, 1.38 MB — `https://ipsen.math.ncsu.edu/ps/OT113_Ipsen.pdf`
- Magnus, *Introduction to the Theory of Econometrics* — **free 52-page preview**, 7.1 MB — `https://janmagnus.nl/misc/magnus-preview.pdf`
- Schwarz, *40 Puzzles and Problems in Probability and Mathematical Statistics* — paywalled / university access

His framing is worth repeating: each is <150 pages and readable in a week, unlike the 500-page standards, and *"a bulk of my non-programming interviews consisted of these three topics."*

## 5 · QD coding prep

There is no canonical QD book the way the Green Book is canonical for QT. The loop decomposes in two halves.

**Half 1 — algorithms, ~60–70% of the loop: LeetCode.** Contested, but the contest resolves clearly:

> "he regularly claims that LeetCode is garbage and that you should not use it, whereas **60 to 70% of quant dev interviews still involve LeetCode style problems**… Ask any quant dev and they will tell you that LeetCode still forms a major part of quant dev interviews."
> — [u/According-Jump-978, r/quant](https://old.reddit.com/r/quant/comments/1sltsh5/sites_like_getcracked_io_are_pure_scam/)

**Half 2 — C++ / OS / concurrency / design patterns, ~30–40%: books and self-made cheatsheets, not drilled MCQs.**

> "topics such as C++ OS computer networks and design patterns are not like LeetCode where practicing questions is the way. They are theory intensive and the best way to cover them is through… books… along with creating short notes or cheatsheets so you can quickly revise before interviews."

Named by r/quant practitioners:

- **Alexandrescu, *Modern C++ Design*** — named by u/microstructureguy specifically "For C++ interviews"
- **C++ Core Guidelines** and the **Google C++ Style Guide** — "have a lot of wisdom" (same commenter); both free online
- **150 FAQ §2.4 (C++, data structures) and §2.5 (Monte Carlo, numerical methods)** — the only canonical-book coverage of this material
- r/quant wiki FAQ: *"Learn at least 1 of (C++, C#, Java) for efficient implementations and 1 of [Python, R] for statistics"*, and explicitly *"Do I need to know C++ to be a quant? A: **No.** Some/a lot of quant developer roles require C++ but there are many that don't."*
- For transitions into QD the wiki names the differentiator as *"Low level high performance or low latency programming experience. For such roles the bar for mathematical knowledge is a bit lower, but e.g. you should be able to implement a PDE solver."*

What to steer away from: MCQ-based "master C++/OS/concurrency" subscription platforms (§7). The structural criticism is specific:

> "that particular platform even has you read the textbooks to solve questions anyway, and boasts a 'structured' form of learning when all he does is slice topics from the same books extremely thinly to feign depth."
> — u/DearFig3394, same thread

## 6 · Category → resource map

One row per L1 category in `02-taxonomy.md`. Drill the categories the bank is actually dense in.

| L1 category | Primary | Secondary | Note |
|---|---|---|---|
| `mental_math` | Zetamac default — `arithmetic.zetamac.com/game?key=a7220a92` | OpenQuant Game Room → Arithmetic Pro; **Sequence Game** for number patterns | 40+ is the only score tied to a named outcome. Sequence Game is the only verified free replacement for the dead RankYourBrain. |
| `probability` | Green Book, probability chapter | Brainstellar (free, Hint→Answer→Solution); Mosteller, *Fifty Challenging Problems in Probability* | "Green Book + 50CP + Brainstellar" is the standard triad on r/quant |
| `combinatorics` | Green Book, brainteaser + probability chapters | Jane Street PDF, "Counting" section (free) | Counting is usually scored inside a probability answer rather than on its own |
| `statistics` | Magnus, *Intro to the Theory of Econometrics* preview (free, 52pp) | 150 FAQ **3rd ed.** statistics section; Heard on the Street statistics section | 150 FAQ 3rd ed. is the first edition to carry statistics at all |
| `stochastic_processes` | Green Book, stochastic processes & stochastic calculus chapter | 150 FAQ §2.6; Joshi | QR-weighted; rarely load-bearing for prop QT |
| `market_making` | **Jane Street *Probability & Markets* PDF** — "Making Markets" + "Adverse Selection" | Green Book probability chapter for the conditional-EV step | Nothing else teaches the bid/offer grammar from a firm's own mouth. Read before any MM round; it costs nothing. |
| `trading_games` | Jane Street PDF — Expected Value, Confidence Intervals, Adverse Selection | Figgie (Jane Street's card game); OpenQuant → Risk, Flexibility modes | JS explicitly flags that candidates give too-narrow 95% intervals — drill interval width, not point estimates |
| `brainteasers` | Green Book, brainteaser chapter | Brainstellar; Heard on the Street pure quant/logic half | Highest density per page in the canon for QT |
| `coding` | LeetCode | 150 FAQ §2.4; OpenQuant `/questions` → "Online Assessment" mode for timed reps | 60–70% of the QD loop per §5 |
| `cpp_systems` | Books + your own cheatsheets: Alexandrescu *Modern C++ Design*, C++ Core Guidelines, Google C++ Style Guide | 150 FAQ §2.4–2.5 | Explicitly **not** MCQ subscription platforms |
| `ml_regression` | 150 FAQ 3rd ed. (stats + ML section, new in this edition) | Magnus preview for regression theory; Ipsen for the linear-algebra underpinning | The main reason to buy 3rd ed. new rather than 2nd ed. used |
| `finance_derivatives` | Joshi — option-pricing reasoning, "how would you price X" | Natenberg, *Option Volatility & Pricing*; 150 FAQ §2.3; HOTS derivatives section | Natenberg was TraderTest's recommendation and is still standard |
| `behavioral` | Jane Street PDF, "Interview Thoughts" (four myths, incl. "you should act confident") | HOTS non-quantitative section (267 questions); Joshi's role/hiring chapters; r/quant wiki FAQ | Joshi is the only canonical book that explains how quant hiring works |

Cross-cutting rows — not L1 categories, but name them when the bank warrants it:

| Need | Resource | Note |
|---|---|---|
| Timed OA simulation | OpenQuant → "Optiver 80 in 8" mode; OpenQuant `/questions` → Online Assessment mode | The only free simulators of the named formats |
| Linear algebra (QR) | Ipsen, *Numerical Matrix Analysis* (free, full book) → 150 FAQ §2.2 | |
| Estimation / Fermi | Jane Street PDF, "Confidence Intervals" → Heard on the Street | JS explicitly warns candidates give too-narrow 95% intervals |
| Company-tagged targeting | QuantGuide Premium company filter ($20/mo annual) | The one genuinely hard-to-replicate paid feature; worth it only in the ~6 weeks before loops |

**Suggested spend.** Free gets ~90% of the way: Brainstellar + OpenQuant (190 Qs + 8 games) + Zetamac + Jane Street PDF + Ipsen + Magnus + LeetCode + the bank this run just produced. About **$70 of books** — Green Book $26 + 150 FAQ 3rd ed. $29 — covers the canon that matters across QT/QR/QD; add HOTS used (~$10–18) for volume. **$240/yr QuantGuide annual** is defensible for company-tagged filtering alone. Skip Joshi at $45 unless QR/derivatives-targeted. Skip every bootcamp.

## 7 · Paid coaching: reported complaints

Everything here is anonymous user opinion attributed to its source. State it as "X reported", never as established fact. The only goal is to stop the user wasting money.

**r/quant has a standing moderator policy** — pinned, locked, moderator-distinguished on the getcracked thread:

> **"Bootcamps and Courses.** It is r/quant's opinion that there are no good 'bootcamps' or other alternative education routes for entering this field. **They are a waste of money, and some are outright scams.** If you want to become a quant then you need to go to a good university, study the right things (see the FAQ in our wiki), and achieve excellent grades."
> — [u/quant-ModTeam](https://old.reddit.com/r/quant/comments/1sltsh5/sites_like_getcracked_io_are_pure_scam/)

That is the strongest single citation available, and it is standing policy rather than one person's opinion.

### "The Quant Guide" ($3,500) — heavily alleged scam, and the site now 404s

- *"As a quant, just wanted to say this website is a complete scam. Designed to scam SWEs with unrealistic dreams."* — **DRW** poster `.cpp`, 16 upvotes ([thread](https://www.teamblind.com/post/anybody-try-the-quant-guide-tv46ebyh))
- *"Am a quant… Quant Guide is a scam."* — same DRW poster ([thread](https://www.teamblind.com/post/has-anybody-tried-the-quant-guides-ultimate-quant-interview-preparation-course-t4txwrhp))
- *"It's a scam. Please check reddit"* — **Microsoft** poster ([thread](https://www.teamblind.com/post/thoughts-on-the-quant-guide-1dhuuyj5))
- The most substantive negative report, from a firsthand buyer — Blind user `QKWJ44`, 7 upvotes: *"**They scrapped Glassdoor for the questions. Some are not even properly spell checked. No solutions available. About 20% of the questions are duplicates** lol… When I complained about these, they were brazen enough to respond with 'these are real interview questions.'"*
- Alleged astroturfing on the promotional threads: *"Wow this exact fake shill post is back again with all the same fake comments lmfaooo. It's a scam."* (Meta poster, 5 upvotes); *"Same group of losers keep making these fake 'question' posts with fake answers to push their scam product. Beware!"* (ex-Microsoft poster, 4 upvotes). The glowing "SWE at LinkedIn → QT at CitSec, 225k → 550k TC" testimonials sit on threads Blind itself labels **Sponsored**.

Blind posters are employer-verified but anonymous, so the scam characterisation remains allegation. The product being gone is independently verified: 404 on every variant, last live Wayback capture 2024-05-06.

### getcracked.io — live, disputed, with a real caveat about the accuser

Priced today: **Trader $241/yr · Developer $330/yr · All Access $390/yr · Hardware Eng. $201/yr** (all marked 33–50% off), 3-day trial. Content by "CJ" (Coding Jesus). The critique lives in [the 180-point r/quant thread](https://old.reddit.com/r/quant/comments/1sltsh5/sites_like_getcracked_io_are_pure_scam/): the LeetCode-disparagement point (§5) and the "thin-slicing textbooks to feign depth" point.

Three things must be flagged alongside it:

1. A moderator removed the post for suspected bad faith — *"I have removed this post now because you were praising this same website only h[ours] before making this post and the behaviour is suspicious."* (u/lampishthing). OP said the earlier praise was ragebait; the post is visible again now.
2. Substantive dissent exists and is reasonable — *"Please use the word scam when the product is a ploy to defraud customers, not when it's simply not worth the price"* (u/Major-Peachi, 6 pts).
3. Its own marketing line *"For the cost of 0.01% of your future compensation"* implies $3.9M future comp at the $390 tier. Misleading framing, not fraud.

**Overpriced-for-what-it-is is well supported; "scam" is contested.**

### TheWallStreetQuants — no smoking gun, structural yellow flags

- Trustpilot **4.6/5 from only 23 reviews**, profile **claimed by the company** since April 2024, under Trustpilot's own banner *"We use technology to protect platform integrity, but we don't fact-check reviews."* Thin base, vendor-controlled profile.
- One Blind data point, far weaker than the Quant Guide evidence: *"As a quant, I can tell you this is an absolute SCAM. Trying to get your hopes high and charge a crazy amount of money for no return"* — **Citadel Securities** poster, Nov 2024 ([thread](https://www.teamblind.com/post/the-wall-street-quants-course-sy6po6yo)). Single comment, 2 upvotes.
- **Price is not published** — gated behind "Find Out If You Qualify / Speak with our quant career advisor today." A [2022 QuantNet thread](https://quantnet.com/threads/thewallstreetquants-bootcamp.52757/) cited ~$3,400 (→$1,400 with "scholarship"), but QuantNet is Cloudflare-blocked, so **that price is unverified**. An undisclosed price behind a sales call is a structural flag regardless of product quality.
- The site displays Citadel/Jane Street-class logos under the disclaimer *"No affiliation or endorsement implied."*

### Calibration on 1:1 coaching

Reported going rate, quoted derisively in-thread: *"for coach, yeah one should definitely pay **300-400 USD** [LOL] for a 1 hour session where they do a mock interview (again using the same questions lol) or review your resume."*

The strongest pro-course argument, from a Citadel Securities poster: *"From an EV perspective, the probability that it's a scam has to be really damn high for this not to be worth it… it really only has to help you .6% for it to be worth the investment."* That logic holds conditional on the product doing anything at all — which is precisely what the firsthand buyer report disputes.

**Adjacent, first-party:** Jump Trading's [Students & New Grads page](https://www.jumptrading.com/hr/students-new-grads) carries a **"Beware Of Scams"** notice — *"Emails from our team will always come from @jumptrading.com. We'll never ask for banking details or payment."* Recruiting-impersonation scams are a live problem this cycle, separate from the coaching-product question.

## 8 · Unverified as of 2026-09-12 — keep these marked

- Optiver's 2026 OA format — Optiver publishes nothing; the "NumberLogic / Beat the Odds / Zap-N" breakdown comes only from SEO content farms. 80-in-8 may be obsolete.
- Optiver 80-in-8 pass bars (54 / 55 / 65) — anonymous Reddit self-reports, all ~4 years old, no first-party confirmation.
- Whether pen and paper are allowed in Optiver's OA — Reddit candidates and commercial prep sites directly contradict each other.
- `rankyourbrain.net` revival — not tested.
- QuantGuide free-tier question count and the direct mental-math URL — not published; both paths 404 to anonymous fetch.
- Quantable's question count — vendor self-contradicts (1500+ vs "over 850").
- TheWallStreetQuants price (~$3,400 / $1,400) — QuantNet is Cloudflare-blocked.
- The Jane Street PDF's official linking status — content is unambiguously theirs, but no linking page exists and the interview-process page 404s.
- Every scam allegation in §7 — anonymous opinion, and the getcracked one is actively disputed.
- Wall Street Oasis (HTTP 403) and QuantNet (HTTP 403 + Cloudflare interstitial) could not be read at all, so nothing sourced from either appears anywhere above.
