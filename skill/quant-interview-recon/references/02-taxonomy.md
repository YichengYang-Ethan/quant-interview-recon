# 02 · Taxonomy, scoring and dedup

## 1. Category tree (controlled vocabulary)

`category` is the string `"l1/l2"`. **Never invent an L1 or L2 name** — the report groups by `category.split("/")[0]`, so a typo'd L1 becomes its own silent bucket and breaks the distribution table that the whole drill plan is built on. If nothing fits, use the closest L2 and put the nuance in `tags[]`. L3 archetypes are open vocabulary and live in `tags[]` only.

`mental_math` — Optiver 80-in-8 and Jane Street ~60q/8min screens.
- `mental_math/arithmetic_speed` — multiplication, division, decimals, fraction comparison. *Observed:* `47 × 8`.
- `mental_math/percentages_ratios` — % change, ratio scaling, European `5:2` = 5÷2 notation.
- `mental_math/sequences_patterns` — numeric sequence completion (Optiver: "26 sequences in 25 minutes").
- `mental_math/approximation` — sig-fig estimation, error bounding.
- `mental_math/fermi_estimation` — "how many X in NYC", market-sizing.
- `mental_math/mental_ev` — EV of a small game computed under time pressure.

`probability` — largest bucket at every site sampled (QuantQuestions: 180+; QuantGuide lists it first).
- `probability/discrete_basics` — coins, dice, cards, urns.
- `probability/conditional_bayes` — two-children problem, Monty Hall, medical-test base rates.
- `probability/expected_value` — a headline topic in its own right at QuantQuestions (90+).
- `probability/continuous_distributions` — uniform/normal/exponential, order statistics.
- `probability/order_statistics_extremes` — expected max/min, expected position of first ace.
- `probability/geometric_probability` — *observed archetype:* "semicircle point placement"; broken-stick; Buffon.
- `probability/recursion_first_step` — first-step analysis, gambler's ruin. *Observed:* "expected number of flips until two heads in a row".
- `probability/inequalities_bounds` — Markov, Chebyshev, Jensen, Cauchy-Schwarz.
- `probability/paradoxes` — inspection paradox, Simpson's, St. Petersburg.

`combinatorics`
- `combinatorics/counting_basics` — permutations, combinations, multiset.
- `combinatorics/inclusion_exclusion`
- `combinatorics/pigeonhole_extremal`
- `combinatorics/generating_functions`
- `combinatorics/graph_lattice_paths` — Catalan, ballot problem.

`statistics`
- `statistics/estimation` — MLE, MoM, bias/variance, sufficiency.
- `statistics/hypothesis_testing` — t/z, p-values, power, multiple comparisons.
- `statistics/confidence_intervals`
- `statistics/regression_theory` — OLS derivation, Gauss-Markov, R².
- `statistics/regression_diagnostics` — multicollinearity, heteroskedasticity, reading OLS output (explicitly named in QR guides).
- `statistics/bayesian_inference` — priors, conjugacy, posterior updating.
- `statistics/resampling` — bootstrap, permutation tests, cross-validation.
- `statistics/experiment_design` — A/B tests, sample sizing.

`stochastic_processes`
- `stochastic_processes/markov_chains` — *observed archetype* at Jane Street superday.
- `stochastic_processes/random_walks` — hitting times, reflection principle.
- `stochastic_processes/martingales_stopping` — optional stopping, Wald.
- `stochastic_processes/poisson_queueing`
- `stochastic_processes/brownian_motion` — hitting times, BM properties.
- `stochastic_processes/ito_sde` — Itô's lemma, Girsanov. (QuantQuestions: "Stochastic Calculus 35+".)

`market_making` — repeatedly described as the highest-weight round at JS / Optiver / SIG / Akuna / IMC / Citadel Securities.
- `market_making/make_me_a_market` — quote two-sided on an unknown quantity; spread widens/narrows as info is revealed.
- `market_making/spread_and_edge` — sizing spread to uncertainty; "too wide nobody trades, too narrow you get picked off".
- `market_making/adverse_selection` — informed-counterparty risk.
- `market_making/inventory_risk` — position management across rounds, break-even, P&L attribution.
- `market_making/information_updating` — Bayesian revision of fair value mid-game.
- `market_making/auction_bidding` — winner's curse, common-value auctions.
- `market_making/game_theory` — Nash, iterated dominance, Colonel Blotto, JS "resource-division game".

`trading_games` — kept separate from `market_making` because these are *interactive multi-round exercises*, not single questions. One record per game, with the mechanics in `answer` and the round structure in `tags[]`.
- `trading_games/dice_game` — JS phone-round dice game; dice games with stopping rules.
- `trading_games/sports_betting_game` — JS phone round.
- `trading_games/card_game`
- `trading_games/multi_round_auction`
- `trading_games/portfolio_allocation_game`
- `trading_games/live_market_sim` — order-book simulation vs interviewer/bot.
- `trading_games/neuro_assessment` — Optiver "Neuro-assessment games… risk aversion, numerical ability, logical reasoning"; Talent Central Verify G+.

`brainteasers`
- `brainteasers/logic_deduction` — hats, prisoners, islanders.
- `brainteasers/weighing_measuring` — coins-and-balance, jug pouring.
- `brainteasers/lateral_thinking`
- `brainteasers/invariants_parity` — chessboard/domino tiling.
- `brainteasers/optimal_strategy` — pirates-and-gold, adversarial splitting.
- `brainteasers/river_crossing_scheduling`

`coding`
- `coding/data_structures` — hash maps, heaps, trees, tries.
- `coding/algorithms` — DP, greedy, graph, two-pointer.
- `coding/simulation` — Monte Carlo, game simulation (named in the JS coding round).
- `coding/order_book` — order-book implementation (named explicitly).
- `coding/time_series_ops` — moving averages, rolling windows, resampling.
- `coding/data_parsing` — file/log/tick parsing.
- `coding/numerical_methods` — root finding, integration, linear solvers.
- `coding/pandas_numpy` — data-manipulation round.
- `coding/complexity_analysis`

`cpp_systems` — the single most common failure source at HRT / Jump / Citadel Securities per the C++ guides.
- `cpp_systems/language_core` — value categories, RAII, move semantics, virtual dispatch, ODR.
- `cpp_systems/memory_model` — happens-before, atomics, memory_order, undefined behavior.
- `cpp_systems/templates_metaprogramming` — CRTP, SFINAE/concepts, type traits.
- `cpp_systems/stl_internals` — runtime behavior of standard containers, allocator/iterator invalidation.
- `cpp_systems/concurrency` — mutexes, condition variables, lock-free structures.
- `cpp_systems/performance_microarch` — false sharing, branch prediction, cache lines, NUMA.
- `cpp_systems/os_internals` — scheduling, syscalls, page cache, virtual memory.
- `cpp_systems/networking` — TCP/UDP, kernel-bypass (DPDK/ef_vi/Solarflare), multicast.
- `cpp_systems/latency_measurement` — profiling, percentiles, jitter, tick-to-trade.
- `cpp_systems/system_design_lowlat` — feed handler, matching engine, risk gateway. *Optiver runs a standalone technology-fundamentals interview with no live coding (memory model, concurrency primitives, networking stack, OS internals) — tag it `tech_fundamentals`.*

`ml_regression`
- `ml_regression/linear_models` — OLS/ridge/lasso, GLMs, logistic.
- `ml_regression/tree_ensembles` — when XGBoost beats a linear model (non-linearities + interactions, >10k obs, rich features).
- `ml_regression/bias_variance_regularization`
- `ml_regression/validation_leakage` — purged & embargoed CV, time-series split vs random CV, label-horizon leakage. The highest-signal QR discriminator observed.
- `ml_regression/feature_engineering` — factor construction, normalization, winsorization.
- `ml_regression/time_series` — stationarity, ARIMA/GARCH, autocorrelation.
- `ml_regression/unsupervised` — PCA, clustering.
- `ml_regression/model_evaluation` — report model performance (R², RMSE, IC caveats), out-of-sample decay.
- `ml_regression/deep_learning` — rare at NG level; kept for completeness.

`finance_derivatives`
- `finance_derivatives/options_basics` — payoffs, put-call parity, moneyness.
- `finance_derivatives/black_scholes` — derivation, assumptions, limitations of vanilla BS.
- `finance_derivatives/greeks` — delta/gamma/vega/theta, hedging.
- `finance_derivatives/vol_surface` — skew/smile, local vol (Dupire), stochastic vol (Heston, SABR), jump-diffusion (Merton).
- `finance_derivatives/pricing_methods` — binomial/trinomial trees for American, Monte Carlo for path-dependent.
- `finance_derivatives/risk_neutral_pricing` — risk-neutral vs real-world measure, no-arbitrage.
- `finance_derivatives/fixed_income` — duration, convexity, curve building.
- `finance_derivatives/market_microstructure` — order types, queue position, spread decomposition.
- `finance_derivatives/portfolio_theory` — Kelly, Sharpe, mean-variance.
- `finance_derivatives/model_validation` — backtesting against historical prices, sensitivity analysis on vol/rates, stress testing. Primarily a bank Quant Analyst bucket.

`behavioral`
- `behavioral/motivation_fit` — "why trading", "why this firm".
- `behavioral/firm_culture` — SIG reads competitive-gaming background; Jane Street reads collaboration + curiosity. Put the firm-specific angle in `tags[]`.
- `behavioral/project_deep_dive` — resume/research defense; paper discussion is a named QR round.
- `behavioral/failure_learning`
- `behavioral/risk_attitude` — biggest bet ever placed, poker/games background.
- `behavioral/ethics_compliance`

## 2. Role → L1 weighting (gap detection)

Run this against the L1 histogram in `qbank.py stats`. An L1 marked ●●● for the target role with **zero or one** harvested question is a coverage gap: go back and search that L1 specifically before reporting. An L1 marked ○ that dominates the bank means the harvest drifted off-role.

| L1 | QT | QR | QD | Quant Analyst |
|---|---|---|---|---|
| mental_math | ●●● | ● | ○ | ● |
| probability | ●●● | ●●● | ●● | ●● |
| combinatorics | ●● | ●● | ● | ● |
| statistics | ● | ●●● | ● | ●● |
| stochastic_processes | ● | ●● | ○ | ●●● |
| market_making | ●●● | ● | ○ | ○ |
| trading_games | ●●● | ● | ○ | ○ |
| brainteasers | ●● | ●● | ● | ● |
| coding | ●● | ●● | ●●● | ●● |
| cpp_systems | ○ | ○ | ●●● | ● |
| ml_regression | ● | ●●● | ● | ● |
| finance_derivatives | ● | ● | ● | ●●● |
| behavioral | ●● | ●● | ●● | ●● |

## 3. Record schema — the flat shape the code actually reads

One JSON object per **sighting**, appended to `raw/records.json` via `qbank.py add --file <batch>.json`. `scripts/qbank.py` reads exactly these keys; anything else is carried along untouched but never rendered, never scored, never merged.

```json
{
  "question": "I flip a fair coin repeatedly until I get two heads in a row. How many flips on average?",
  "question_en": null,
  "canonical_key": "hh_run_expected_flips",
  "company": "Jane Street",
  "role": "QT",
  "round": "phone",
  "category": "probability/recursion_first_step",
  "difficulty": "medium",
  "year": 2026,
  "source_url": "https://www.techinterview.org/companies/jane-street/",
  "source_platform": "techinterview",
  "source_date": "2026-07-21",
  "confidence": 3,
  "answer": "First-step analysis on states {start, one-H, done}: E = 6.",
  "tags": ["coin_flip", "first_step_analysis", "green_book", "verbatim_excerpt"],
  "lang": "en",
  "verbatim": true
}
```

| Field | Type | Required | Contract enforced by `_coerce()` / `classify_junk()` |
|---|---|---|---|
| `question` | string | **yes** | Verbatim as found, in the source language. `< 12` chars → rejected to `rejected.json`. Do not clean numbers out of it. |
| `question_en` | string \| null | **yes when `lang != "en"`** | English gloss. `dedup_text()` matches on `question_en or question`, so a Chinese record without a gloss **can never dedup against an English source** — `_coerce()` stamps `_warn` on it and the recall failure is silent otherwise. |
| `canonical_key` | string \| null | no | Lowercased slug for a known named problem (`hh_run_expected_flips`). Asserted by you, trusted over any lexical score at merge — but still gated by the numeric check. |
| `company` | string | **yes** | Defaults to `run.json`'s company. Keep `citadel` and `citadel_securities` distinct — different entities, different role mix; merging them corrupts the weighting table. Normalize nicknames before writing: `简街→Jane Street`, `城堡→Citadel`, `傲博→Optiver`, `苏斯克→SIG`, `哈德逊河→HRT`. |
| `role` | enum | **yes** | `QT` \| `QR` \| `QD` \| `QA` \| `SWE` \| `unknown`. Anything else is not coerced — it passes through and breaks the role label. Note the code uses `QA`, not `Quant Analyst`. |
| `round` | enum | **yes** | `OA` \| `phone` \| `superday` \| `onsite` \| `final` \| `unknown`. **Any other value is silently rewritten to `unknown`.** The report's top-level sections are these six. Finer round names go in `tags[]`: `mental_math_test`, `tech_fundamentals`, `recruiter_screen`, `coding_round`, `trading_game_round`, `behavioral_round`, `take_home`. |
| `category` | string | **yes** | `"l1/l2"` from §1. Not validated by the code — a bad path becomes a bogus L1 bucket in the distribution table. Default if omitted: `uncategorized`. |
| `difficulty` | enum | no | `easy` \| `medium` \| `hard` \| `unknown` (lowercased). Anything else → `unknown`. If the source carries its own label (QuantGuide Easy/Medium/Hard, 1p3a 难度 facet), use it and tag `difficulty_from_source`; otherwise it is your judgment. |
| `year` | int \| null | strongly wanted | Interview year, not post year, when they differ and the post says so. Non-int → `null`. Drives the recency component and the "近两年" headline stat. |
| `source_url` | string | **yes** | **Missing `source_url` → rejected.** Never mint a URL you did not fetch. |
| `source_platform` | string | **yes** | Free string, defaults `unknown`, but the curated-bank rule (§5) matches on exact lowercase membership in `{quantguide, puzzledquant, openquant, brainstellar, quantquestions, quantinterview}` after stripping `.io`/`.co`/spaces. Spell those exactly. |
| `source_date` | string | no | `YYYY-MM-DD`. Carried into the source ledger. |
| `confidence` | int 1–5 | **yes** | §4. Clamped to 1–5; non-int → 3. Emit the **pre-merge** score; `merge_pair()` adds the corroboration bonus itself. |
| `answer` | string | no | Sketch or full solution. Additive at merge — a second distinct answer lands in `alt_answers[]` and renders as 另一解法. |
| `tags` | string[] | no | Union'd at merge, first 8 rendered. This is the only place L3 archetypes, gated-body markers and round refinements survive. |
| `lang` | `zh` \| `en` | no | Auto-detected from CJK presence if omitted. Drives the cross-language threshold slack. |
| `verbatim` | bool | no | Default `true`. Set `false` for anything you paraphrased, translated or reconstructed — it prints *非原文（转述/翻译）* and blocks the record from overwriting a verbatim sibling's text at merge. |

**Markers the flat schema carries in `tags[]`.** The richer design has no home here, so encode them as tags and say so in `answer` when it matters:
- `gated_body` — 1p3a body hidden behind a points wall; the text is reconstructed from teaser + replies. **Always pair with `verbatim: false`.** That pairing is the only thing stopping a reconstruction from later being quoted as a verbatim sighting.
- `reply_leak` — substance recovered from the un-gated reply tree rather than the post.
- `snippet_only` — only a WebSearch snippet was ever seen; caps confidence at 2 (§4.3).
- `mirror` — text is ≥95% identical to an existing Glassdoor-origin record on a non-glassdoor domain. Do not add it as a second source; it inflates `corroboration` without adding evidence.
- `textbook_only` — Green Book / Heard on the Street / Joshi with no firm sighting. Set `company` to the book, never to the firm you were searching for.
- `difficulty_from_source`, `tech_fundamentals`, `mental_math_test`, and the L3 archetype tags.

**Not implemented — do not emit.** The code ignores these entirely, and shipping them creates a bank that looks richer than it is: `attestations[]`, `text_original` / `original_language`, `is_multipart` / `parts[]`, `secondary_paths[]`, `game_spec`, `source_type`, `source_access`, `fetch_method`, `gated_body` as a boolean field, `recollection_markers[]`, `distinct_platform_count`, `difficulty.source`, `answer.verified_by` / `answer_confidence`, `canonical.locator_verified`, `dedup.simhash64` / `embedding_model`, `quality.spam_score` / `review_state`, `provenance.*`, `schema_version`. Fields the code *writes for you* at merge and that you must not pre-populate: `id`, `sources[]`, `corroboration`, `variant_text`, `alt_answers[]`.

**Process records are not question records.** Round structures, timelines, test formats, "一共三轮", comp figures — most of what a 1p3a or Glassdoor page contains — belong in `run.json`'s `pipeline[]` and `sources.json`, not in `raw/records.json`. Forcing process text into the question table is the main way these banks rot.

## 4. Confidence rubric (1–5)

### 4.1 Five components, 0–3 each → raw total 0–15

**A. Source quality (0–3)**

| Pts | Criterion |
|---|---|
| 3 | First-person primary recollection on a tier-A platform (1p3a 面经 with facet metadata, Reddit megathread comment, Blind), **or** a first-party firm statement about its own process |
| 2 | Tier-B forum recollection (WSO, QuantNet, everythingquant), **or** a tier-C curated bank that tags per-question company + year |
| 1 | Aggregator guide with blanket attribution; Glassdoor entry with no round/date |
| 0 | Bootcamp marketing, SEO listicle, textbook-only with no firm attribution |

**B. Recency (0–3)** — relative to today, on the interview year

| Pts | Window |
|---|---|
| 3 | 2026 (current cycle) |
| 2 | 2025 |
| 1 | 2023–2024 |
| 0 | ≤2022, **or no date at all** |

*Carve-out:* a canonical textbook problem (`canonical_key` set) floors B at **1** — the Green Book's HH-run problem does not become false because the sighting is old. It **cannot exceed 1** without a fresh attestation; the study plan must not be driven by 2019 posts.

**C. Corroboration (0–3)** — keyed on distinct *platforms*, not raw post count

| Pts | Criterion |
|---|---|
| 3 | ≥3 distinct platforms, and at least two different kinds of source (forum + curated bank, say) |
| 2 | 2 distinct platforms |
| 1 | 1 platform, ≥2 independent posts (different authors / thread ids) |
| 0 | Single sighting |

Score C on what *you* found across the whole harvest, before submitting. `merge_pair()` then adds its own `+1` (capped at 5) once two distinct URLs actually land on one record — so do not pre-bump C for a merge you are expecting.

**D. Recollection authenticity (0–3)** — does this read like someone who was actually there?

| Pts | Criterion |
|---|---|
| 3 | ≥3 markers: first-person narrative, named interviewer count/role, timeline, stated outcome, admitted struggle, follow-ups described, self-deprecation |
| 2 | 2 markers |
| 1 | 1 marker |
| 0 | No markers; polished third-person exposition |

Marker vocabulary — pattern-match these literal strings:

`zh:` `挂经` `过经` `凉经` `求米` `裸考` `磕磕绊绊` `第二天收到拒信` `一共三个session` `时间还挺紧张的` `我只截到了第二道`

`en:` `I interviewed` · `they asked me` · `I blanked` · `got the rejection` · `my interviewer` · `I couldn't finish`

**E. Specificity (0–3)**

| Pts | Criterion |
|---|---|
| 3 | Verbatim question text + company + role + round + year |
| 2 | Verbatim text + company + (role or round), year inferable |
| 1 | Paraphrased topic only ("they asked a Markov chain question") |
| 0 | Category name with no question ("probability and brainteasers") |

### 4.2 Raw total → score

| Raw | `confidence` | Label | Use |
|---|---|---|---|
| 13–15 | **5** | confirmed | Drill first; safe to cite to a human |
| 10–12 | **4** | strong | Core study set |
| 7–9 | **3** | likely_real | Study, flag as unconfirmed |
| 4–6 | **2** | weak | Practice value only; never say "X asked this" |
| 0–3 | **1** | unreliable | Exclude from the study plan |

### 4.3 Hard caps, applied after the sum

| Condition | Cap |
|---|---|
| Only ever seen as a WebSearch snippet (`snippet_only`) | **2** |
| Question text never seen — reconstructed from category labels alone | **2** |
| Only source is bootcamp marketing | **1** |
| Gated body **and** no reply leakage | **2** — and it is a process record, not a question |
| Textbook only, no firm sighting | **3**, and `company` must be the book, not the firm you searched for |

### 4.4 The 1p3a gating case, worked

Jane Street QR thread, body gated at 105 points, but the metadata line, the teaser and every reply were readable. A = 3 (tier-A 面经 with facets), B = 2 (posted 2024-10-23, `找工年度 2025`), C = 0 (single sighting), D = 3 (`裸考`, `磕磕绊绊`, `第二天收到拒信`), E = 1 (text hidden; topic reconstructed from replies as a Bayesian / optimal-stopping machine-selection EV game). Raw = 9 → `confidence: 3`. The gated-body cap of 2 does **not** apply because the replies leaked substance:

> `play for 5-20 for first round, and at most 4 times re-play, say for 18.19.20`
> `3号和之后的机器的期望收益都大于1，所以应该都玩一次？`
> `贝叶斯概率问题。`

Write the reconstruction into `question`, set `verbatim: false`, tag `gated_body` + `reply_leak`, and put the reply quotes in `answer` so a reader can check your reconstruction.

## 5. Dedup — what the merger does, and what you must do for it

Mechanics live in `merge_records()` / `merge_pair()`. Default threshold 0.82 on a Jaccard-over-shingles score floored by `SequenceMatcher × 0.95`; records are processed highest-confidence-and-longest-first so the best-attested phrasing survives. Your job is to feed it the three things it cannot recover on its own.

**Numbers are load-bearing.** `numbers_compatible()` blocks any merge where both sides have numbers and the multisets differ. "Two heads in a row" (E=6) and "three heads in a row" (E=14) measure 0.91 lexically and are **different questions**; a bank that folds them teaches a wrong answer while claiming corroboration for it. So: never round, never normalize, never drop a numeral when transcribing. Spelled-out numbers are converted too (`two→2`, `half→0.5`, `两→2`, `三→3`), so "two heads" and "2 heads" do match. The one tolerated asymmetry is a paraphrase that lost its numbers entirely — then only lexical similarity decides, which is exactly why paraphrases are worth less.

**A non-English question needs an English gloss.** `question_en` is the match key. Without it a Chinese record shares zero shingles with its English twin and both survive as separate entries. Cross-language pairs get 0.10 of threshold slack (0.82 → 0.72) because a gloss is a paraphrase by nature — a measured accurate gloss scored 0.799 against its original — so the gloss should be a faithful restatement, not a tidy rewrite.

**Curated banks never self-merge.** Two *different* entries from `quantguide`, `puzzledquant`, `openquant`, `brainstellar`, `quantquestions` or `quantinterview` are never merged with each other, however similar, because those banks list each problem exactly once. QuantGuide ships deliberate near-twins ("Find the most recent date…" vs "Find the next date…") that score 0.91 and are not the same question. Forums are excluded from this rule — the same recollection genuinely does get posted twice there. Consequence: spell curated platform names exactly as listed, and never assign two of that bank's entries the same `canonical_key`.

**`canonical_key` overrides the lexical score** (still subject to the numeric guard). Use it when you are confident two differently-worded sightings are the same named problem — a Chinese 面经 and a Glassdoor post of the HH-run problem. Do not use it as a category label; it is an identity assertion.

**What merging preserves.** Every distinct `source_url` is appended to `sources[]` — no URL is ever overwritten. A longer *verbatim* text (>1.15× the incumbent) replaces the shorter one and the loser moves to `variant_text`; a non-verbatim record never replaces text. Recency fields take the max year (and that record's round, if known); `category`/`difficulty` are backfilled only when the survivor says `uncategorized`/`unknown`; `tags` union; `corroboration` = count of distinct URLs. Because text and metadata move independently, a 2021 verbatim Glassdoor quote keeps its wording while a 2026 paraphrase contributes its year.

**Audit it.** `merge-log.json` records every fold with basis (`lexical` or `canonical_key=…`), similarity, both texts and the incoming URL. Read it after `qbank.py merge`. Two symptoms to look for: a fold at similarity 0.83–0.86 between questions with different setups (threshold too low for that batch — rerun with `--threshold 0.86`), and obvious twins that did *not* fold (usually a missing `question_en`).

## 6. Spam / junk filter

The code rejects on four binary rules in `classify_junk()`, writing losers to `rejected.json` with a reason — quarantined, reviewable, never deleted:

1. `question` shorter than 12 characters.
2. Content-free recollection: matches `^(总共|一共)?\s*\d+\s*(轮|rounds?)\s*(面试)?[,.。，]?$` or a bare `挂了` / `过了` / `等消息` / `waiting` / `rejected` / `no update`.
3. Marketing patterns: `加/添加 微信|VX|wx` · `扫码/私信/咨询 了解/详情/报名` · `内推/求职/辅导/培训 群/班/课程/服务` · `DM me … for … prep/coaching/referral` · `包过|保offer|100% offer` · a post whose entire body is `求米|求大米|接力|谢谢分享|mark|占位` · the vendor names `PH求职|WST|直通硅谷|Offer帮|Rexpand|睿思班`.
4. No `source_url`.

Everything past that is your judgment, before you write the record:

**Blanket attribution (the strongest single signal).** One sentence names many firms for a whole page and no individual question carries its own company/year/round. Archetype, observed verbatim on quantt.co.uk: *"This guide collects 25 worked examples from recent SIG, Optiver, IMC, Akuna, Citadel Securities, Jane Street and Hudson River Trading trader interviews."* Harvest at most as `confidence: 1–2` with the guide as the company-less source; never attribute those questions to a named firm.

**Other marketing tells:** `free cheatsheet` / `enter your email` / `subscribe for`; `Sign in for a free lesson` / `start your free trial`; `/#pricing`, `$X/month`, `Enroll now`, `Book a call`, `limited seats`; title matching `/(\d+)\s+(Real\s+)?(Examples?|Questions?)\s+20\d\d/` on a non-forum domain; ">N real questions" with N ≥ 50 and no per-item source; uniform paragraph lengths with zero first-person markers and a tidy 3-bullet "why they ask this" after every question.

**Injected ads inside forum streams** — strip before reading, they are not the poster's words: `使用独家折扣码 1p3acre 立享额外9折优惠！`, `使用折扣码 1p3acre 立减10%`, `Coderust: Hacking the Coding Interview`, `Grokking the Coding Interview`, `System Design Interview热销书在线版独家折扣`. On 1p3a also strip the `相关帖子`, `论坛导航`, `精品网课` and sponsored-footer zones — a naive `get_page_text` ingests all of it and inflates both junk scores and dedup noise.

**Route, don't reject:**
- *Process-only* ("I had 3 rounds", "OA then phone then superday", `一共三轮`) → `run.json` `pipeline[]`.
- *Status queries* (`现在五点了还没回复，什么情况`, "anyone heard back?", `求问timeline`, `同问`) → drop.
- *Pure compensation* (base/RSU only) → out of scope for the bank.
- *Gated with no leakage* → process record only. Never fabricate the hidden questions.

The Optiver OA thread is the worked counter-example: heavily gated, full of `求米`, yet the surviving teaser — *"一共三个session…第一个部分8分钟80道mental math，第二部分是一些probability和找规律的题。第三部分是两道game题"* — is a legitimate **process** record carrying category signal (`mental_math/arithmetic_speed`, `mental_math/sequences_patterns`, `probability/*`, `trading_games/*`). It is not 80 question records, and you must not invent them.

**Glassdoor-specific:** the same text syndicated across SEO mirrors must not become `corroboration: 10` — tag the copies `mirror` and do not add them as sources. Glassdoor also dumps whole OA descriptions into the "question" field; one observed entry contained *"80in8, 80 questions in 8 minutes of simple calculations… Numerical sequences, 26 sequences in 25 minutes. HR interview… Neuro-assessment games… Talent Central Verify G+ test… Technical interv[iew]"* — five round descriptions in one field. Split those into pipeline steps; never store as one question.
