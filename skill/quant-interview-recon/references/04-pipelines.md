# 04 · Interview pipelines by firm

Two uses. (1) Fill the report's `pipeline` field from the per-firm section below — copy the stage list and the tag on each claim, never launder a CROWDSOURCED or UNVERIFIED claim into plain prose. (2) Gap detection: after the bank is collected, look up the firm in the final table and check the bank actually contains questions in the 2–3 categories that firm's pipeline demands. Zero mental-math questions for Optiver is a hole; zero C++ questions for IMC is a hole. Go fill it before writing the PDF.

Research date of everything below: **2026-09-12**. Re-verify anything older than one cycle.

| Tag | Meaning |
|---|---|
| **OFFICIAL** | Read off a company-controlled domain. Quote it; it is the strongest claim available. |
| **CROWDSOURCED** | Named candidate/employee post read directly (Reddit/Blind). Dated, anecdotal, unaudited. Always print the year. |
| **SEO-VENDOR** | Interview-prep businesses selling practice for the exact test they describe. **Treat as unverified marketing.** They contradict each other and primary sources. |
| **UNVERIFIED** | Widely repeated, no primary source reachable. Say so in the report rather than passing it on. |

Four firms publish **nothing at all** about process: **SIG, Jump, Akuna, Five Rings**. For those, every stage claim in the report must carry a visible unverified marker.

---

## Jane Street

Sources: [/join-jane-street/interviewing/](https://www.janestreet.com/join-jane-street/interviewing/), [/trading-interviews/](https://www.janestreet.com/trading-interviews/), [/join-jane-street/sp/interviewing](https://www.janestreet.com/join-jane-street/sp/interviewing), [/preparing-for-a-software-engineering-interview/](https://www.janestreet.com/preparing-for-a-software-engineering-interview/)

**Quantitative Trading — OFFICIAL.** "phone interviews at the start, and then in-person interviews for the final stage." **No online assessment is mentioned for trading.** Final-round content, verbatim: "problem solving, probability and statistics, coding (in any language of your choice), data analysis, and general interests." "All of your interviews will be conducted by quantitative traders." Tone: "a lot more like a conversation than a quiz and won't require previous knowledge of finance or involve any complicated math." **Round count is not published** — high confidence on structure, none on count.

**Quantitative Research — OFFICIAL.** Described only as "a mix of the two"; candidates are pointed at both the trading and technology guides. No standalone QR pipeline exists.

**Software Engineering (QD-adjacent) — OFFICIAL.** Zoom technical interview(s) → **final round in person**, "mostly, if not exclusively, focused on collaborating on a series of coding problems." Real code, not pseudocode; any language, but "we strongly encourage you not to try OCaml for the first time during the interview." Explicitly excluded: "We don't ask software engineers to do mental math, or math olympiad questions, or to contemplate logic puzzles." The [2020 blog post](https://blog.janestreet.com/jane-street-interview-process-2020/) gives **1 technical phone + 2–4 onsite rounds**, but is dated **July 24, 2020** and covers SWE only ("interviews for roles in trading, research... will differ substantially").

**Strategy & Product — OFFICIAL, the only JS track with an OA.** Online assessment, multiple-choice + short answer, "typically takes an hour" → **1–2 video interviews** on "hypothetical business scenarios and logic puzzles... in real time" → "a day of in-office interviews."

**TDOE — OFFICIAL.** Take-home exercise ("assesses your attention to detail and how you adapt to an unfamiliar concept") → **two** Zoom interviews → onsite final.

**Intern vs NG full-time:** not differentiated anywhere on the site; the 2020 SWE post bundles intern/new grad/experienced.

**Do not repeat these:** "estimation / Fermi questions" appear on **zero** official JS pages — the official wording is "problem solving" plus "probability and statistics"; the estimation framing is folklore. A **Jane Street trading OA on HackerRank** is claimed by [techinterview.org](https://www.techinterview.org/companies/jane-street/) and [finalroundai](https://www.finalroundai.com/blog/jane-street-interview-process) with **no primary corroboration**; the same pages carry a fabricated "60-question, 8-minute mental math test" for JS, which is Optiver's format with the numbers filed off.

---

## Citadel Securities (and Citadel)

citadel.com and citadelsecurities.com publish **parallel, near-identical** guides; official framing is that interviewing means "talking with two firms at once: Citadel and Citadel Securities." Both domains **403 on WebFetch** — read via logged-in Chrome.

**Campus Quantitative Research — OFFICIAL**, page dated **Nov 9, 2024**. [citadelsecurities.com/.../our-quantitative-research-interview-process/](https://www.citadelsecurities.com/careers/career-perspectives/our-quantitative-research-interview-process/). **Four steps, ~4–5 weeks end to end.**
1. **First Round** — "45- to 60-minute remote interview," video. Focus: "programming skills, ability, data structures/algorithms and problem-solving." Core languages Python and C++, any accepted. **Vendor: CoderPad** — "Prior to the interviews, we'll send a CoderPad link." Also behavioral: technical interests, internships, projects, motivation.
2. **Second Round** — **onsite**, "usually consists of three to five 60-minute interviews," technical + behavioral. Next steps within two weeks.
3. **Final Review** — hiring managers determine team fit; multi-team interest resolved with the recruiter.
4. Offer.

**Internship & New Graduate Engineering — OFFICIAL**, page dated **July 24, 2024**. [.../internship-and-new-graduates-engineering-interview-process/](https://www.citadelsecurities.com/careers/career-perspectives/internship-and-new-graduates-engineering-interview-process/). **Four steps, ~8 weeks.** "you will not be interviewing for a position on a specific team until the end of the process."
1. **First Round** — **45-minute** remote video, **CoderPad**, DS&A + problem solving + behavioral.
2. **Second Round** — "usually consists of **three 45-minute** interviews."
3. **Leadership Interview** — "If a hiring manager expresses interest in your profile, you will interview with a senior engineer to be assessed for a specific team."
4. Offer.

This is the sharpest NG-vs-other split any firm publishes: NG/intern engineering = 45 min + 3×45 min; campus QR = 45–60 min + 3–5×60 min.

**Quantitative Trading — no official pipeline.** [Candidate FAQs: Markets & Trading](https://www.citadelsecurities.com/careers/career-perspectives/candidate-faqs-markets-trading/) contains exactly three questions — "What is the culture like for traders?", "What qualities make someone a successful trader?", "What types of complex mathematical or statistical problems do you solve?" — and **no process description whatsoever**.

**The OA gap.** Neither official guide mentions any OA; both start at "First Round." [interviewfox](https://interviewfox.ai/interview-questions/citadel-oa-hackerrank-questions/), [extrabrain](https://extrabrain.app/interview-questions/citadel-hackerrank-questions-extrabrain/) and [techinterview](https://www.techinterview.org/companies/citadel-securities/) uniformly claim a HackerRank/CodeSignal OA (2–3 problems / 60–90 min SWE; 3–5 problems / 90–120 min quant). **UNVERIFIED** — no primary source and no first-hand candidate post confirming it. Either Citadel omits the OA from its guides or these sites are wrong; the distinction was not resolvable. Same status for the **Correlation One Datathon** as an alternate recruiting channel: SEO-VENDOR only, not verified against Citadel's own site.

---

## Optiver

Source: [optiver.com/join-us/stories/optiver-us-campus-recruiting-qa/](https://www.optiver.com/join-us/stories/optiver-us-campus-recruiting-qa/) — page dated **September 22, 2025**, squarely this cycle. FAQ answers lazy-load on click; WebFetch returns headers only, so the accordions must be expanded in Chrome.

**OFFICIAL, verbatim.** "At a high-level, the interview process starts with an **online assessment** followed by **behavioral and technical interviews**. The final step is a **virtual interview with the hiring team**." — "**All final round interviews will be conducted virtually**." This directly refutes the widely repeated "Optiver Chicago onsite Superday"; most third-party guides are still wrong about it. OA content: "your ability to problem solve and use logic and reasoning **in different formats**... it may be helpful to practice activities that involve quick problem-solving skills, such as **mental math and strategy games**." "Final interviews do not require technical preparation." On mental math: "Being good at mental math is **necessary but insufficient** to thrive as a Trader at Optiver... you also need to be a quick decision-maker and stay cool under pressure." Reapplication is allowed once the next recruitment season begins.

**Optiver never names 80-in-8, never states a question count, time limit, scoring rule, or cutoff.** "In different formats" is the only official hint that the OA is multi-module. Their FAQ carries the verbatim question *"There's a lot of information out there about your interview process. How do I know what's true and what's not?"* — answer: "we highly encourage you to simply ask our recruiters!"

**Assessment platform — OFFICIAL (empirical).** [assessment-portal.optiver.com](https://assessment-portal.optiver.com/) resolves; title "Login - Optiver Assessment Portal"; auth is a **6-digit email code** into an OIDC/ASP.NET Identity flow (`/connect/authorize/callback`, PKCE). A vendor keyword scan of the live login page returned **zero hits** for zyvo, mettl, hackerrank, codesignal, codility, pymetrics, SHL; the only external assets are jQuery validation from `ajax.aspnetcdn.com`. The front door is **first-party Optiver infrastructure**; what sits behind the login is not observable without taking the test.

**CROWDSOURCED — origin of the "80-in-8 / 55" numbers.** [r/quant "Optiver 80 in 8 Assessment"](https://old.reddit.com/r/quant/comments/w3cbr9/optiver_80_in_8_assessment/), thread is **~4 years old (2022 cycle)**.
- OP: "invited to do the Graduate Quantitative Trader Assessment **by Zyvo**" — the vendor name comes from a candidate, not from Optiver.
- u/chizzmaster (10 pts): "You need like a score of **55+ i believe** (**+1 point for correct, −1 for incorrect or skip**)" — hedged, and it says **skipping is penalised**, which every prep site contradicts (they say skip = 0).
- u/hitori_ookami (21 pts), who passed, reached **question 72** of 80 and says "forums suggest around **65** would be passing." Describes **three** stages: (1) 80-in-8, "very similar to the expert level at rankyourbrain.com"; (2) "a bit taxing, taking **an hour**... remember the number, **flip the meat before it burns**, guess the pattern"; (3) "**26 questions on series** to solve in **25 min**... a score of **15+** should take you through."
- Content disputed between candidates: one reports no decimals and "fractions and stuff," another "2 decimal places... fractions+/−decimals." Multiple-choice is reported, not confirmed. No calculator, no paper.

**Vendor triangulation — this one holds.** [Zyvo](https://www.zyvo.nl/en/producten/neuro-assessments) is a real Utrecht HR assessment firm; its neuro-assessment product page names the games **"Balloon Pop, Grill Master, and Shopaholic"** plus a **"Zap-Q personality test"**. "Grill Master" matches the 2022 candidate's "flip the meat before it burns" almost exactly — independent corroboration that Optiver's gamified module is Zyvo's battery, at least as of 2022.

**SEO-VENDOR module list (unverified).** [quantvault](https://quantvault.org/optiver-online-assessment.html), [tradermaths](https://www.tradermaths.com/trading-firms-prep/optiver), [quantt](https://www.quantt.co.uk/tools/optiver-80-in-8), [aptitude-test-prep](https://aptitude-test-prep.com/employers/trading-assessments/optiver-assessment/), [jobtestprep](https://www.jobtestprep.com/optiver-test) claim: **Number Logic** (~15 *or* 26 Q / 25 min — they disagree), **Beat the Odds** (~30 Q / 45 min), **Zap-N** (games, 45–60 min), **Zap-Q** (personality); **+1 / −1 / 0-for-skip**; ~3 hours total; a 2026 "Likelihood Test" addition. Cutoff claims are mutually contradictory: "higher than 55, but you'll want ~70" / "cutoff is 55" / "70+ usually mentioned."

**Verdict on "80-in-8 = +1/−1 with a ~55 net pass line": cannot verify; partially refuted.** The **format** (80 questions / 8 minutes) is consistently reported first-hand and is real. The **+1/−1 rule** and the **55 line** trace to one hedged 2022 Reddit comment; a second candidate in the same thread says 65; prep vendors say 55 *or* 70 and contradict the Reddit comment on whether skipping is penalised. **No primary source exists.** Write it into the report with that verdict attached, never as a bare number.

One adjacent Blind data point, Optiver employee account u/CMEJesus via [teamblind](https://www.teamblind.com/post/how-does-optiver-grade-their-oa-sagvbp8e): "All optiver OAs need you to pass a threshold, time taken is not really considered," thresholds "generally close to a perfect score." **Context ambiguous** — that thread is about the SWE coding OA, not 80-in-8.

**Intern vs NG:** the Sept 2025 Q&A is a single "campus" process covering both; no differentiation published. **Do not rely on** "assessments can only be completed once every 8 months" — it surfaced in a search summary of optiver.com but was not present in the extracted page text.

---

## SIG (Susquehanna)

**OFFICIAL — nothing.** [sig.com/campus-programs/campus-recruiting/](https://sig.com/campus-programs/campus-recruiting/) is intern testimonials; [careers.sig.com/us-campus-recent-graduate-student](https://careers.sig.com/us-campus-recent-graduate-student) is navigation only; [careers.sig.com/us-campus/jobs](https://careers.sig.com/us-campus/jobs) is a job list; `sig.com/careers/interview-process/` **404s**. The only official-adjacent statements found via search: Discovery Programs give students "an early introduction to their interview process," and SIG "uses puzzles to emulate the trading environment."

**CROWDSOURCED (first-hand, read directly).** r/quant, "SIG: Trading Online Assessment for discovery day?" (~2022): "I just took the online assessment for SIG's trading (internship)... It was **14 questions in 20 minutes** and I had idiotically thought that no calculators were allowed" → **calculators appear to be allowed**. A separate r/quant post (~1 yr ago) from a PhD candidate who took "the **probability assessment** from SIG for a **quant research** role" confirms **role-specific OA variants**.

**SEO-VENDOR (unverified, mutually contradictory).** [tradermath](https://www.tradermath.org/knowledge-base/sig-interview-guide), [quantt](https://www.quantt.co.uk/resources/sig-interview), [jobtestprep](https://www.jobtestprep.com/sig-online-assessment), [aptitude-test-prep](https://aptitude-test-prep.com/employers/finance-and-investment-banking-assessments/sig-problem-solving-assessment/) claim the OA is the **"SIG Problem-Solving Assessment," published by Mercer | Mettl** — **could not verify**, no primary source and no first-hand post naming Mettl. Question counts claimed: **9** / **9–15** / **17** in ~60 min, against the candidate's **14 in 20 min**; all four disagree. Claimed pipeline: OA → 45-min HR call (3 probability/EV questions) → 1–2 technical rounds with a trader → (sometimes) 48-hour take-home trade-sequence project → Super Day, 4–6 back-to-back 30–45 min interviews plus a group card/dice/trading game.

**Two specific negatives.** **Poker is not evidenced as an interview round** — the one source addressing it directly (SEO-VENDOR) says poker is "culture and post-hire training for new traders — you do not need a poker background to get an offer"; no official confirmation either way. **Personality test: no evidence at all**, official or crowdsourced, that SIG administers one. Treat the claim as unsupported.

---

## IMC

**OFFICIAL — US page is thin.** [imc.com/us/careers/recruitment-process](https://www.imc.com/us/careers/recruitment-process) gives three generic stages: **Application** → **Assessment** ("For some roles, you may be invited to complete an assessment") → **Interviews** ("a series of interviews where we'll evaluate specific competencies"). No counts, no formats.

**OFFICIAL — APAC pages are far more specific** (structure likely mirrors US; region caveat applies). [How to prepare for an interview at IMC](https://www.imc.com/ap/articles/how-to-prepare-for-an-interview-at-imc) — four stages: (1) **Online assessment**, screens so "only suitable candidates are invited to interview," gated on working rights and grades; (2) **Behavioral interview**, "A friendly chat on the phone or over Zoom" with a campus recruiter; (3) **Technical interview**, "First round technical Interview with one of our traders or engineers, who you will work closely with to solve a specific problem"; (4) **Final Assessment Day**, in office, "a mix of technical and behavioural **stations**."

**OFFICIAL — best description of the OA, from an IMC engineer.** [A unique approach to hiring: Alex ten Brink](https://www.imc.com/in/articles/a-unique-approach-to-hiring-in-conversation-with-alex-ten-brink). Stage 1 verbatim: "We do a first round of **automated LeetCode questions, which are purely theoretical**, but this is just a **time-saving filter**, in order to ensure that only suitable candidates are invited to a second-stage interview." Stage 2 splits in two: "a discussion that emulates talking through a problem with an IMC colleague" **and** "a programming test, where the candidate works on **an approximation of our actual trading system** that enables traders to get the trades they want." Assessed: C++ proficiency, algorithms, communication, resilience — **process over correctness**, and **resilience is explicitly tested throughout**.

"Automated LeetCode questions" is descriptive, not a vendor name — **IMC never names HackerRank or CodeSignal.** Intern vs NG: APAC content references "graduates and interns" together and does not differentiate; both gated on "a minimum of a Distinction average."

---

## Two Sigma

Sources: [Interviewing at Two Sigma](https://www.twosigma.com/careers/interviewing-at-two-sigma/), [Interviewing for Quantitative Research & Modeling](https://www.twosigma.com/careers/interviewing-at-two-sigma/interviewing-for-quantitative-research-modeling/)

**OFFICIAL — logistics documented, structure not.** "Our interviews are conducted over video conferencing" — **Google Meet or Microsoft Teams**, link emailed "the evening prior." Log in **10 minutes early**; a **Candidate Experience Coordinator** handles troubleshooting and reviews the itinerary. "Your meeting link is the same for the interviews you are scheduled for on a given day, so interviewers will join at their scheduled time." A **prep call** with recruiting happens beforehand. QR & Modeling content assessed: "Data analysis/open-ended problem solving"; "Coding and algorithms"; "Statistics or your research domain for PhDs." Philosophy: "Our interviews are practical. We'll explore areas of your knowledge and experience through discussion and problem solving" — they weigh *how* you got there. An official **"Quantitative Research Interview Demo"** video is referenced on the QR page.

**Not published:** round count; any OA or take-home (can neither confirm nor deny); intern vs NG difference. The same-link-all-day detail strongly implies a **multi-interview final day**, but the count is genuinely unpublished — do not fill in a number.

---

## HRT (Hudson River Trading)

Sources: [How to Prepare for Your Software Engineer Interview at HRT](https://www.hudsonrivertrading.com/hrtbeat/interview-at-hrt/), [Answers to Questions I Often Get](https://www.hudsonrivertrading.com/hrtbeat/engineering-and-interviewing-at-hrt/)

**OFFICIAL — the most vendor-explicit firm here.** Pipeline: "a **coding test**, **1–2 technical phone screens**, and an **onsite multi-round final interview**." Coding test vendor named outright: **"Hackerrank or Codility."** Timed with a deadline; language restrictions depend on role; **you may consult external references**; corner-case testing matters. Technical discussion round: **45 minutes**, on one of **Knowledge of Systems / Data Structures / Problem Solving**. Programming round: C++ or Python for some roles, free choice for others. Onsite: full day, back-to-back — programming (idiomatic modern code, resource usage), systems-level knowledge (memory, I/O, process management), problem-solving method, collaboration, **teachability and response to feedback**, communication. Philosophy: HRT "does its best to stray away from 'burst of insight' leet-code style questions"; the ideal is that "a strong programmer from a competitive firm would ace their technical interview with no studying."

**Intern vs NG — OFFICIAL and explicit:** internship programs follow "**a slightly abridged process**" versus full-time; the specific differences are not detailed.

**Caveat:** both pages are framed around **Software Engineering**. HRT's Algo Developer (Quant Research & Trading) track is not separately documented; the page notes "interviews vary slightly between some roles" and that recruiter-provided detail supersedes the general guide.

---

## Jump Trading

**OFFICIAL — nothing, verified empirically.** [jumptrading.com/hr/students-new-grads](https://www.jumptrading.com/hr/students-new-grads) rendered main content (3,833 chars) contains **zero occurrences of "process", "interview", "assessment", or "round"** — it is a values blurb plus a live job list. `jumptrading.com/careers/...` job postings **403 on WebFetch**.

Useful and OFFICIAL from that page, directly relevant to a 2027-start candidate: "We're opening **2027 roles by region, starting with the US**. If you're waiting for opportunities elsewhere, they're on the way. Please hold off on applying to US positions if you're planning to apply to a role in another region." Campus contact: `campusrecruiting@jumptrading.com`.

**No first-hand candidate account of Jump's pipeline was found. Anything the bank contains about Jump's rounds is unverified — label it as such.**

---

## D. E. Shaw

Sources: [deshaw.com/careers/interviewing-guide](https://www.deshaw.com/careers/interviewing-guide), [careers/interviewing](https://www.deshaw.com/careers/interviewing), [candidate FAQ](https://www.deshaw.com/careers/faq). `deshaw.com/careers/interview-process` returns an empty body — that URL is not a content page.

**OFFICIAL, verbatim stages:** "The typical stages of a successful hiring process include the following: **application review, phone interview and virtual interviews, references, and finally an offer**." Plus: "You may also be asked to provide a **writing sample or code sample**, and to complete a **case study**. Depending on the role, your process may differ slightly." Question types are behavioral, situational, and **case studies** — "questions or prompts based on real-world situations... A case study may include discussion with an interviewer, a **written response**, or an exercise similar to work one might do in the role." What they value: "curious to see how you process new information and approach challenging problems, not simply whether you arrive at a 'correct' answer, know a particular mathematical technique, or are fluent in a specific programming language." Process "might take several weeks." No dress code.

**Not published:** round counts, any OA vendor (no HackerRank/CodeSignal reference anywhere), intern vs NG differentiation. D. E. Shaw is the only firm here that puts **reference checks inside the pipeline**.

---

## Akuna Capital

**OFFICIAL — no pipeline published.** [akunacapital.com/careers/](https://akunacapital.com/careers/) is value proposition only; [work-with-us/early-careers/](https://akunacapital.com/work-with-us/early-careers/) confirms full-time roles across Technology, Trading, Quant, Operations with "no prior industry experience required" but no process. `akunacapital.com/faq-items` **404s**; job posting `akunacapital.com/careers/job/7993921/` **404s** (listing closed since indexing).

**OFFICIAL-adjacent — Akuna's 2026 Virtual Quant Trading Challenge**, surfaced via search of akunacapital.com; the live posting 404'd before it could be read verbatim. Candidates **write market-making bots** that compete against Akuna's own models and each other **on a simulated exchange**; **~5–8 hours** to complete; most profitable submissions win swag and "**expedited recruitment processes**" for Chicago quant full-time and internship roles; entry reportedly requires a resume plus a **≤1-page / 500-word motivation letter**. **Confidence: medium** — mechanism and framing consistent across Akuna-domain search results, not read off a live page.

This is a **parallel fast-track, not the main pipeline.** Akuna's ordinary round structure is undocumented.

---

## Five Rings

**OFFICIAL — verified empty.** [fiverings.com/positions/](https://fiverings.com/positions/) describes training ("extensive," hands-on and classroom) and lists exactly **three** full-time tracks: **Software Developers, Quantitative Traders, Quantitative Researchers**. No interview process, no stages, no assessments. The domain is **fiverings.com**, not fiveringsllc.com (a domain-restricted search on the latter returns zero results).

**UNVERIFIED — everything else.** All process claims come from SEO-VENDOR sites ([quantt](https://www.quantt.co.uk/resources/five-rings-guide), [quantblueprint](https://www.quantblueprint.com/guides/how-to-get-a-job-at-five-rings)), a Medium post by a self-described ex-Five Rings recruiter, and login-walled Glassdoor/Blind. Commonly repeated and unsupported: 3–4 stages compressed into 4–8 weeks; a timed opening assessment of probability/combinatorics/logic "harder than most peers' first rounds"; 3–4 virtual rounds of math/probability/brainteasers, then **one round with the head of trading and one with a founder**; small NY-only class; NG TC $350k–$500k. Treat all of it as **rumor** — the "founder round" is distinctive enough to be either real or pure folklore.

---

## DRW

**Best-documented pipeline of any firm here, and OFFICIALLY identical for interns and new grads** — the [graduates](https://www.drw.com/work-at-drw/graduates) and [interns](https://www.drw.com/work-at-drw/interns) pages describe the same four stages. Also: [Preparing for our technical challenge](https://www.drw.com/updates/insights/gearing-up-for-the-technical-challenge), [You're almost there — final round](https://www.drw.com/updates/insights/youre-almost-there-preparing-for-drws-final-round-interviews).

1. **Application** — resume only. "We review applications on a **rolling basis** so we encourage you to apply early."
2. **Technical Challenge** — at home, **timed**, role-split, verbatim: "Depending on your role, this could be a **quantitative challenge focused on probability and logic skills** or a **coding challenge on fundamental computer science concepts**." **Vendor: Codility**, named explicitly for Software Developer roles. **Time limit is not published** — "we will provide you with the length of time the exercise will take in the introduction e-mail." Coding version has "questions at varying difficulty levels that will assess both **correctness and performance** of your code"; some tasks are function-writing, some simulate game scenarios. **Scoring methodology is not disclosed**; DRW warns "the questions are designed to be difficult."
3. **Phone / Zoom Interview** — "You'll talk to a fellow developer, quantitative trader or researcher," technical + behavioral. **~45 minutes** *(from a search summary of drw.com, not the extracted page text — medium confidence).*
4. **Final Round — two days, onsite.** "Day one starts in the **afternoon** with introductions followed by a **technical challenge**. **Day two is a full day of interviews** focusing on a range of topics, both technical and behavioral," plus casual team interaction; the prep article adds "Your final round may include **several back to back interviews**." Role-specific prep: developers review advanced CS, trading candidates stay current on markets, researchers must discuss their work in depth.

**Explicitly not confirmed:** search summaries attribute a **"Superday" label, a Python quantitative coding challenge, and a trading simulation** to DRW's pages. Neither the interns nor the graduates page mentions a trading simulation, Python specifically, or the word "Superday." Treat all three as **unverified**.

---

## G-Research

**Strongest primary source in this report: a dated official PDF** — [Assessment process for quantitative research and machine learning (uploaded 2025/07)](https://www.gresearch.com/wp-content/uploads/2025/07/Quantitative-research-and-machine-learning-interview-prep-assessment-process.pdf). WebFetch cannot parse it; download and run `pdftotext`. Also [QR interview questions career guide](https://www.gresearch.com/career-guides/quantitative-researcher-interview-questions/).

**OFFICIAL, verbatim from the 2025 PDF.** Online application — "We will ask you for your CV/resume and a few personal details... you will receive an update on the status of your application **within one week of applying**." **Stage one: online quant quiz** — "You will be asked to complete **one of two quant quizzes**; either a **general quantitative aptitude assessment**, or an **ML specific one**, depending on your background." **Stage two: technical interviews** — "**Typically, you will sit four interviews**, one of which will focus on **in-depth technical questions in mathematics**. **Each interview will last one hour.**" ML track: "If your profile is better suited to ML, you'll complete **two one-hour interviews**, which will focus on your ML knowledge, but do expect to answer questions on **mathematics, programming and stats** that are relevant to the ML space as well!" **Stage three: leadership interviews** — "you will meet some of our leaders."

**Quiz content (career guide, OFFICIAL, medium-high):** "The quiz assesses **basic skills, more so than advanced mathematics**." Topics: **probability, statistics (including OLS), linear algebra, calculus (especially differential equations), programming, and finance.** **No question count or time limit is published.**

**Version drift.** The older official PDF `Quantitative-Researcher-Assessment-process-guidance-v3.pdf` (2022) describes a **"triage interview"** between the quiz and the technical rounds. **The July 2025 PDF drops triage entirely** — if a guide tells you to expect a triage round, it is working from 2022 material.

**Intern vs NG:** search surfaced an official claim of "four stages in our quantitative research internship assessment process, typically one to two weeks to complete" — same shape, much faster. **Not directly verified.**

---

## Cross-firm quick reference

| Firm | OA? | Vendor (confidence) | Rounds after OA | Final round | NG = intern? |
|---|---|---|---|---|---|
| Jane Street | QT **no**; SP **yes** (1 hr MC+short answer) | none named | QT: phone(s) → onsite | **In person** | Not stated |
| Citadel Sec — QR | Not mentioned officially | **CoderPad** (OFFICIAL, interview tool) | 45–60 min R1 → **3–5 × 60 min onsite** → team match | **Onsite** | NG/intern eng is a separate, shorter published process |
| Citadel Sec — Eng NG | Not mentioned | **CoderPad** | 45 min R1 → **3 × 45 min** → leadership | ~8 wks total | Intern + NG share one guide |
| Optiver | **Yes**, multi-module | First-party portal; **Zyvo** games (2022 candidate + product-page match) | behavioral + technical | **Virtual** (OFFICIAL 2025) | One campus process |
| SIG | **Yes** (crowdsourced) | "Mercer\|Mettl" — **UNVERIFIED** | unpublished | unpublished | Unknown |
| IMC | **Yes** — "automated LeetCode questions" | none named | behavioral → technical (discussion + trading-system coding) | **Assessment Day, stations** | Not differentiated |
| Two Sigma | Not mentioned | Google Meet / MS Teams (logistics only) | **unpublished** | Multi-interview day, virtual | Not stated |
| HRT | **Yes** | **HackerRank or Codility** (OFFICIAL) | **1–2** phone screens (45 min tech discussion) | **Onsite, full day** | Intern "slightly abridged" (OFFICIAL) |
| Jump | Unknown | — | **Nothing published** | — | Unknown |
| D. E. Shaw | Not mentioned | none named | phone → virtual interviews → **references** | Virtual | Not stated |
| Akuna | Trading Challenge (5–8 hrs, bot vs sim exchange) | first-party sim | **Nothing published** | — | Challenge covers both |
| Five Rings | Unknown | — | **Nothing published** | — | Unknown |
| DRW | **Yes**, timed at home; quant *or* coding by role | **Codility** (SWE, OFFICIAL) | 1 phone/Zoom (~45 min) | **Two-day onsite** | **Identical** (OFFICIAL) |
| G-Research | **Yes** — quant quiz, general *or* ML | none named | **4 × 1 hr** (ML: 2 × 1 hr) | **Leadership interviews** | Internship = 4 stages, 1–2 wks (unverified) |

---

## Fetch failures to expect (don't rediscover them)

| Target | Symptom / workaround |
|---|---|
| `reddit.com`, `old.reddit.com` | WebFetch: "Claude Code is unable to fetch from old.reddit.com". WebSearch with `allowed_domains:["reddit.com"]`: API Error 400, "The following domains are not accessible to our user agent". **Use logged-in Chrome.** |
| `citadelsecurities.com/*`, `citadel.com/*` | **403** on every WebFetch. Read via Chrome. |
| `wallstreetoasis.com` | **403**. Holds 258 SIG and 353 Jane Street interview entries that stay unread. |
| `glassdoor.com` | Login wall; needs logged-in Chrome plus an account. |
| `jumptrading.com/careers/<id>` | **403**. The `/hr/` pages load fine. |
| `optiver.com` FAQ answers | Lazy-loaded on click; WebFetch and `textContent` both return headers only. Click each accordion in Chrome. |
| G-Research PDF | WebFetch returns unparsed binary; download and `pdftotext` locally. |
| Known-dead paths (404) | `janestreet.com/join-jane-street/interviewing-at-jane-street/` (correct: `/join-jane-street/interviewing/`), `optiver.com/working-at-optiver/hiring-process/`, `sig.com/careers/interview-process/`, `akunacapital.com/faq-items`, `akunacapital.com/careers/job/7993921/`. `careers.imc.com/ap/en/hiring-process` 308-redirects to `imc.com/ap`. |

**Domain blacklist — down-weight, never cite as primary:** techinterview.org, quantt.co.uk, tradermath.org / tradermaths.com, quantvault.org, quantblueprint.com, aptitudeprep.com / aptitude-test-prep.com, finalroundai.com, interviewfox.ai, extrabrain.app, linkjob.ai, getsmartresume.com, jobtestprep.com. They sell practice for the exact assessments they describe and **demonstrably fabricate** — the "Jane Street 60-question 8-minute mental math test" is Optiver's format transplanted onto Jane Street. They disagree with each other on every cross-checked number (SIG: 9 vs 9–15 vs 17 questions; Optiver cutoff: 55 vs 70; Optiver Number Logic: 15 vs 26 questions).

**Trust order:** firm's own careers/blog pages → dated official PDFs → first-hand Reddit/Blind posts *with the date printed* → everything else.

---

## Gap-detection table — categories each pipeline demands

L1 names from `02-taxonomy.md`. If the collected bank has **zero** questions in a row's categories, that is a gap: go collect more before rendering the PDF. "(unverified)" means the pipeline evidence driving the row is not OFFICIAL — still worth collecting, but do not assert the round exists.

| Firm / track | Demanded categories | Driven by |
|---|---|---|
| Jane Street — QT | `probability`, `statistics`, `coding` | OFFICIAL final-round wording |
| Jane Street — SWE/QD | `coding`, `behavioral` | OFFICIAL; mental_math and brainteasers **explicitly excluded** — their presence is a false positive, not a gap |
| Jane Street — SP | `brainteasers`, `behavioral` | OFFICIAL ("business scenarios and logic puzzles") |
| Citadel Sec — QR | `coding`, `probability`, `behavioral` | OFFICIAL (DS&A + problem solving + motivation) |
| Citadel Sec — Eng NG | `coding`, `behavioral` | OFFICIAL (45-min CoderPad DS&A) |
| Optiver | `mental_math`, `trading_games`, `probability` | OFFICIAL ("mental math and strategy games"); 80-in-8 + Zyvo games crowdsourced |
| SIG | `probability`, `brainteasers`, `trading_games` | CROWDSOURCED OA (14 Q / 20 min) + "puzzles to emulate the trading environment"; group card/dice game is SEO-VENDOR (unverified) |
| IMC | `coding`, `cpp_systems`, `behavioral` | OFFICIAL (LeetCode filter, C++ proficiency, trading-system coding, resilience) |
| Two Sigma | `statistics`, `ml_regression`, `coding` | OFFICIAL ("data analysis/open-ended problem solving", "coding and algorithms", "statistics or your research domain") |
| HRT | `coding`, `cpp_systems`, `behavioral` | OFFICIAL (HackerRank/Codility, systems round, teachability) |
| Jump | — no signal | Nothing published, no first-hand account; do not infer categories |
| D. E. Shaw | `behavioral`, `coding`, `statistics` | OFFICIAL (behavioral + situational + case study; code/writing sample) |
| Akuna | `market_making`, `coding`, `cpp_systems` | Trading Challenge = market-making bots on a simulated exchange (medium confidence); main pipeline undocumented |
| Five Rings | `probability`, `combinatorics`, `brainteasers` (unverified) | SEO-VENDOR only — collect, but mark every round claim as rumor |
| DRW | `probability`, `coding`, `brainteasers` | OFFICIAL ("quantitative challenge focused on probability and logic skills" *or* coding challenge) |
| G-Research | `probability`, `statistics`, `ml_regression` | OFFICIAL quiz topics (probability, stats incl. OLS, linear algebra, ODEs, programming, finance); ML track splits off |

Two cross-cutting checks. **`behavioral` is demanded by every firm that publishes a first round** (Citadel, IMC, DRW, HRT, D. E. Shaw, G-Research leadership stage) — a bank with zero behavioral questions is a gap almost everywhere. **`finance_derivatives` is demanded by almost none of these NG pipelines**; only G-Research names finance as a quiz topic, and Jane Street states outright that trading interviews "won't require previous knowledge of finance." Do not flag its absence as a gap.

When the bank is thin for a firm that publishes nothing (SIG, Jump, Akuna, Five Rings), the honest report action is to say so and point the candidate at the recruiter — Optiver's own FAQ tells candidates to "simply ask our recruiters," and recruiters at most of these firms will confirm format, length, and vendor on request.
