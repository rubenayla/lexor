<!-- consult selectively — grep, never read in full -->

# History

Append-only log of decisions, reflections, and findings. Newest at the bottom.

## 2026-05-15 — Root sourcing rule
Decided: when choosing a root, prefer the language whose everyday word for the concept matches. Don't pull a Latin root if the word people actually use is Germanic (or vice-versa). Goal is recognizability for real speakers, not etymological neatness. Added to `decisions.md`.

## 2026-05-15 — Roots are concept-level, shared across parts of speech
Decided: a root like `lom` represents the concept ("the eating-thing"), not specifically the verb. Verb / noun / adjective forms are produced by markers on top of the same root. Rationale: nouns frequently become verbs and vice-versa in natural use, and a concept-level root is more compact and learnable than reserving separate roots per part of speech.

Implication: the part-of-speech / derivation marker system must do real work — it's the only thing distinguishing *eat* from *eating* from *food* from *eater* from *edible*.

## 2026-05-15 — Derivation slots to systematize
Working set of derivations the marker system should cover systematically:
1. Verb — "to eat"
2. Act/event noun — "eating" (the act, as a referrable thing)
3. Agent noun — "eater" (the doer)
4. Patient noun — "food" (the thing acted on)
5. Adjective (capable/prone) — "edible", "voracious"

Slots considered but left out of the systematic set (handle via compounds or separate roots):
- Instrument — "fork/utensil"
- Location — "dining room"
- Result — "meal"

Rationale: 1–5 are the productive derivations English/Latin lean on heavily; covering them systematically makes Lexor more learnable than English on this axis. 6–8 are less productive and cost marker inventory we may want for other things.

Still open: the actual marker scheme (prefix vs suffix vs internal-vowel vs reserved-consonant-slot). See `tasks.md`.

## 2026-05-15 — Marker is a suffix, not a prefix
Decided: derivation/POS markers attach as suffixes. Rationale: word recognition is incremental — keeping the root at the onset lets listeners identify the concept first, then refine with the suffix. Matches the cross-linguistic suffixing preference (~70%+ of world languages). Prefixes would force listeners to hold the modifier in memory before binding it to a root not yet heard.

Counter considered: prefixes give category-first parsing (consistent with VOS at the sentence level). Rejected because at the word level the concept carries the meaning, and the suffixing preference is strong empirical evidence.

## 2026-05-15 — Universal word shape: CVC-root + V[C]
Decided: every word is CVC root followed by a vowel-initial suffix. This guarantees no consonant clusters across the root↔suffix boundary, eliminating buffer-vowel irregularity at its source.

- Verb: CVC + V (tense vowel). The "bare" case — no suffix consonant.
- Other derivations: CVC + V + C, where C identifies the derivation slot (agent / patient / act / adjective) and the V carries inflection (number / definiteness, parallel to tense for verbs).

Tradeoff accepted: derived words are one syllable longer than the bare root. Worth it for the structural symmetry and zero special cases.

Still open: which consonant maps to which derivation slot, and how the trailing vowel encodes noun inflection. See `tasks.md`.

## 2026-05-15 — No mandatory grammatical marking (meta-principle)
Decided: Lexor never forces a speaker to commit to information they haven't actually decided on. Examples of what this rules out: Spanish-style obligatory gender, English-style obligatory number on nouns, languages that force evidentiality marking on every verb. Every grammatical category is opt-in, attached only when the speaker has and cares about that info.

Rationale (from user): "in Spanish you HAVE to specify lots of things that maybe are not specified yet, which makes you decide things you haven't decided yet just to be able to talk." This is a known cognitive cost of mandatory marking, and Lexor's precision-and-efficiency goal is better served by deferring commitments until the speaker has them.

This is a meta-principle that should govern every future grammatical decision (gender, definiteness, tense obligation, etc.), not just plurals.

## 2026-05-15 — Plural is not a noun inflection
Decided: number is dropped from the word shape entirely. Nouns are number-unspecified by default. When quantity matters, speakers reach for a separate optional quantifier system that can express exact counts, ranges (2–8), and distributions (gaussian μ=15 σ=5), not just singular/plural.

Consequence: `s` is free for the adjective derivation slot — no conflict between adjective marking and plural marking.

Connects to checklist.md:97 (ranges/distributions) and :120 (numeric probability). The quantifier system design is parked in tasks.md.

## 2026-05-15 — Derivation consonants assigned
Decided:
- `r` — agent ("eater"). English `-er`, Latin `-or`.
- `n` — act/event noun ("eating"). English `-tion`/`-ing`, Spanish `-ción`.
- `t` — patient ("food", thing acted on). English past participle `-ed`. Picked unvoiced over `d` for cleaner clusters across all root-final consonants.
- `s` — adjective ("edible"). English `-ous`/`-ish`, Latin `-osus`.

Worked example with `lom` (eat-concept):
- `loma` — eats (verb, present)
- `loman` — eating (the act)
- `lomer` — eater
- `lomet` — food
- `lomes` — edible

All four chosen for mnemonic strength: English/Latin speakers recognize the suffix function from their existing intuitions.

## 2026-05-15 — Why negation needs a different position than derivations
Question raised: babies famously ignore the "no" in "don't touch the stove" and act on the verb. Do adults still suffer this? Should negation really be a particle/affix in the usual position?

Cognitive science (Kaup, Lüdtke, Zwaan; Wegner's ironic process theory):
- Adults do still suffer the leak, just less dramatically than toddlers.
- Standard propositional negation ("the door is not open") is processed in two steps: simulate the affirmative state, then invert. Step 1 fully activates the affirmative concept. Measurable: negated sentences take longer to process than affirmative ones, and the affirmative meaning leaks into downstream tasks.
- **Bound negation escapes the leak via lexicalization.** When negation is morphologically fused to the verb (e.g., English "dislike", Turkish `-me` suffix, "unhappy"), the negated form acts as its own lexical entry — one retrieval, one stored concept (e.g., "aversion" for "dislike"), no inversion step. The affirmative is never independently activated.
- For lexicalization to actually work, the bound form must be (a) phonologically integrated (one word, no pause), (b) productive and uniform across all verbs, (c) frequent enough that listeners chunk it as a stored pattern rather than computing it compositionally each time.
- Within bound negation, **prefixes chunk faster than suffixes.** A prefix delivers the negation cue *before* the stem, so stem activation happens already in negated context. A suffix delivers the stem first, allowing affirmative activation before the negator arrives at the end and forces a retroactive inversion. For scope operators, modifier-first beats root-first.

This created tension with the earlier "suffixes are universally better" decision: that argument was about *concept recognition*, where the root carries meaning and should come first. Negation is doing different work — *scope priming* — and the cognitive logic flips.

## 2026-05-15 — Hybrid morphology: prefixes for scope, suffixes for derivation
Decided: Lexor uses a hybrid morphology.
- **Suffixes = derivational/inflectional.** They change what the root is (agent, patient, act, adjective) or refine it (tense). Productive, open-ended. Root stays at the word's onset.
- **Prefixes = scope/operator.** A small closed class (negation, and others as needed: maybe interrogative, intensity, evidentiality). Modifier arrives first so the listener processes the rest in the modified frame.

Not an inconsistency — it's the principled answer to "different cognitive jobs deserve different positions." Cross-linguistically attested in Bantu, Quechua, and others.

Constraints on the prefix system:
- Closed class, kept small.
- Each prefix is phonologically bound to its host (one stress group, no pause between prefix and root) so listeners don't lose track of word boundaries.
- Phonological shape must not collide with pronoun space (`y`, `u`, `e`, `i`, `l-` series) or be mistakeable for a root onset.
- A canonical stacking order will need to be defined if multiple prefixes ever combine (parked).

## 2026-05-15 — Negation prefix: `no`
Decided: negation is prefixed `no`. Matches Spanish, English (`no`), Italian, French (`non`), Latin (`non`), German (`nein`) — maximum cross-language recognizability. `n` is already the act-noun derivation suffix consonant, but slot differs (suffix vs prefix) so there's no actual ambiguity.

Worked examples with `lom`:
- `loma` — eats
- `noloma` — does not eat
- `lomer` — eater
- `nolomer` — non-eater (one who doesn't eat)
- `lomes` — edible
- `nolomes` — inedible

Note: this is *logical negation* (the event didn't happen / the property doesn't hold). A separate question — whether Lexor also wants a distinct *lexical opposite* marker (e.g., `love` → `hate`, not just `not love`) — is parked. The two are cognitively different and most languages conflate them.

## 2026-05-15 — Speech speed concern: CVCV pattern, sticking with it
Concern raised: the regular CVC-root + V[C] pattern may make Lexor slow to speak compared to languages with denser syllables (English `strengths` = 1 syllable / 8 phonemes vs Lexor's 2-syllable words for similar concepts).

What the literature says (Pellegrino et al. 2011, *Language*): across languages, information rate converges to ~39 bits/sec. Languages with simple syllables (Japanese, Spanish) compensate with higher syllables/sec; languages with complex syllables (English) compensate with lower syllables/sec but more info per syllable. The product is roughly constant. Lexor's CVC+V[C] is moderate complexity, so by this prediction speakers will naturally adjust syllable rate.

Real costs accepted:
- Per-syllable density lower than English. 1-syllable English verbs ("eat") become 2-syllable Lexor (`loma`).
- Strict phonotactics resist the vowel-reduction tricks fast English uses (`gonna`, `prolly`).
- Highly regular shape risks Japanese-style "machine-gun" perception (aesthetic, not speed).

Real compensations from other decisions:
- No mandatory plural / gender / article / tense → fewer wasted morphemes per utterance than Spanish or English.
- Concept-level roots → one root spawns the whole derivation family, fewer separate words to retrieve.
- VOS → action arrives in syllable 1–2; no auxiliary/copula buildup.
- Optional precision → speakers only pay for info they actually intend to transmit.

Decision: stick with the approach. Per-meaning rate is plausibly neutral or favorable; per-syllable rate is worse than English but better than Japanese. Real verdict requires actual spoken usage. Premature redesign is a bigger risk than the speed cost.

If speed becomes a real problem later, cheap retrofits exist:
- Sub-CVC shapes for high-frequency closed-class words (already done for pronouns: `y`, `u`, `e`).
- Optional vowel reduction in unstressed syllables for fluent speakers.
- Contractions for very common verb+pronoun combinations.

None of these break the structural design; they layer on top of it.

## 2026-05-15 — All words end in vowels; inner vowel reuses tense
Two design changes locked in together:

**Change 1: every content word ends in a vowel.** Old derived shapes (`lomer`, `lomet`, `loman`, `lomes`) ended in consonants. New universal shape `(prefix-)CVCV(CV)` means derived non-verbs become `lomera`, `lometa`, etc.

Rationale (user-raised): word-final consonants are often weakly articulated and missed by listeners; vowel-final words are more audible and "stack like Lego" — they concatenate cleanly with consonant-initial next words, eliminating boundary clusters and the need for sandhi rules. Cross-linguistically the open-syllable languages (Japanese, Italian, Hawaiian, Polynesian) tend to be described as easy to follow.

Cost: derived nouns/adjectives grow from 2 syllables to 3. Accepted — consistent with the earlier speech-speed decision (per-meaning rate matters, not per-syllable; Lexor compensates via no-mandatory-marking and concept-level roots).

**Change 2: the inner vowel of derived non-verbs reuses the tense vowel system.** That vowel sits in the same structural slot as a verb's tense vowel, so reuse is natural and free.

Examples:
- `lomara` — current eater (`a` = present)
- `lomera` — former eater (`e` = past)
- `lomira` — future eater (`i` = future)
- `lomesa` — currently edible
- `lomese` — was edible (not anymore)

English needs extra words ("former", "would-be", "currently") for this; Lexor encodes it natively.

Meta-principle conflict resolved: a vowel will be reserved as "atemporal / temporal frame unspecified" (specific vowel TBD — `y` is a candidate but currently assigned to "perfect/completed"). When the speaker doesn't want to commit to a frame, that vowel slots in. Avoids forcing temporal commitment.

Limitation accepted: 6-vowel tense system is coarse. Real temporal precision ("yesterday", "since 2020", "every Tuesday", "during the war") will need a separate temporal-modifier system. Parked — but the inner vowel handles the frame cheaply and the precision system layers on top, same way the quantifier system layers on top of nouns without forcing number.

Vowel-echo phenomenon noted: mono-temporal sentences with explicit inner vowels on every noun produce repeated vowels (`loma lomata lomara` for "the current eater eats current food"). Not a bug — when present, it carries real cross-word temporal-alignment info, and speakers can suppress it via the atemporal default. Mixed-temporal sentences naturally produce distinct vowels marking the contrast.

**The outer vowel** of derived forms is reserved as the optional role/case slot (subject / object / other), addressing the VOS subject-marking question from decisions.md. Specific vowel assignments parked.

## 2026-05-15 — Tense-vowel reassignment
Question raised: which vowel should mean "atemporal / temporal-frame unspecified"?

Analysis: the most-versatile vowel cross-linguistically is /a/ — most sonorous, most universal (in nearly every language), most articulatorily independent of preceding consonants, maximum acoustic distance from neighbors. By the principle "most frequent slot gets the easiest vowel," /a/ should serve whatever role is most common.

Frequency: in real speech, content nouns outnumber finite verbs ~1.5–2× per sentence, and most nouns most of the time don't carry temporal frame. So *atemporal* is plausibly more frequent than *present-tense*. The old assignment gave `a` to present; the new one gives it to atemporal.

Other vowels reassigned to add a mnemonic: front vowel `i` = future (forward in time), back vowel `o` = past (behind in time). The old `e`=past, `i`=future swap had no logic; new pairing is teachable.

New table:
- `a` = atemporal / unspecified (most universal vowel, most frequent slot)
- `e` = present (neutral mid front, second-most-common)
- `i` = future (front = forward)
- `o` = past (back = behind)
- `u` = imperative (deep, strong)
- `y` = conditional (marked vowel for less frequent meaning)
- `c` /æ/ = perfect/completed (marked vowel for aspect distinction)
- `x` = continuous (consonant aspect combiner)
- ∅ = infinitive (verbs only)

Cost: disturbs the earlier tense table in roots.md. Acceptable — no vocabulary is locked in yet, the rationale is now documented, and retrofitting later (after vocab exists) would be much more expensive.

This decision validates the meta-principle "no mandatory marking" in a concrete case: even temporal frame is optional — `a` is *unspecified*, not just *unmarked-present*. A speaker can convey an action or property without committing to when it happens.

## 2026-05-15 — Role-vowel assignments (outer slot)
Decided: outer vowel of derived non-verbs carries optional role/case marking. Shape 2 chosen — core argument roles get vowels, everything else is prepositional.

Reasoning for scope (Shape 2 vs minimal vs full):
- Minimal (subject + object only) — tempting but recipient ("I gave it *to him*") is the third-most-common role and falling back to a preposition felt arbitrary.
- Full thematic role inventory — over-commits the vowel inventory. Location/time/source/goal genuinely benefit from prepositions because they take *expressions* (e.g. "under the table", "since 2020"), not single nouns.
- Shape 2 hits the sweet spot.

Assignments:
- `a` = default (position carries role). Most universal vowel for most common case, consistent with the atemporal-default principle in the inner slot.
- `e` = subject / agent. Front vowel = active.
- `o` = object / patient. Back vowel = passive, receives.
- `u` = recipient / dative. Deeper back = directed inward, "to whom."
- `i` = instrument (optional, 4th slot). Front high = "by means of."
- `y`, `c` /æ/ = reserved.

The same letter at the inner vs outer slot means different things (e.g. `a` = atemporal inner, default-role outer), and the positionally-fixed slot disambiguates. Pronounceable two-`e` words like `lomere` (`lom` + `e` present + `r` agent + `e` subject = "present eater [SUBJ]") are expected; should be monitored as vocab grows for any real confusion.

Worked examples (verb `lom` eat, root-based nouns):
- Canonical VOS: `lome lometa lomera` — "the (current) eater eats (current) food." Default outer vowels, position carries roles.
- Topicalized object: `lome lometo lomere` — "FOOD the eater eats." Explicit markers override broken order.
- With recipient: `supe libra-u y-e lomera` — "give book-to-RECIPIENT I-SUBJ the eater" → "I give the book to the eater." (`sup` = supply/give; `lib` as stand-in for "book".)

Doesn't lock pronoun behavior — open question whether pronouns also take role vowels (likely yes for consistency: `y-e` "I-subj", `y-o` "me-obj").

## 2026-05-15 — Quantifier system framework
Question opened: how does Lexor express quantity, given that we dropped plural as a mandatory noun inflection?

User constraints raised this round:
- Must be compatible with both decimal AND dozenal. Lexor doesn't pick a side; both bases are first-class. (User is a dozenal advocate; ~/vault/ideas/dozenal/ + ~/vault/standards.md formalize their dozenal notation conventions: `;` as dozenal radix point, `[base]_[number]` for arbitrary bases.)
- Numbers are digit-streams ("two-four-three"), not place-value words ("two hundred forty-three"). Faster, fully regular, no irregular teens.
- Big numbers via scientific-notation-style scale expression, not a "million/billion/trillion" word ladder.
- Quantifier follows the noun (`apple 3`, not `3 apple`) — consistent with Lexor's "thing first, modifiers after" pattern at every other level (VOS sentence order, concept-root first in words, tense/role vowels at the end). Also gives smaller working-memory load: listener builds the noun referent before refining its quantity.

System designed (specific roots picked by me with delegation from user):

**Base markers** (CVC, sit at the written radix-point position):
- `dem` — decimal (mnemonic: DECimal)
- `doz` — dozenal (mnemonic: DOZenal)

Both required by grammar. No default — every number expression carries an explicit base marker. Can be elided pragmatically when context sets the base for a run of numbers, but grammar always allows explicit marking. Achieves the "both first-class" goal cleanly.

**Scale marker** (CVC):
- `pem` — "times-base-to-the-power-of" (mnemonic: Power/Exponent of Mantissa)
- Form: `[mantissa] pem [exponent] [base-marker]`. Mantissa and exponent share the base.

**Comparison/bounds operators** (CVC closed class):
- `min` — < (minimum)
- `mag` — > (Latin magnus, max)
- `sam` — = (same)
- `tom` — range "to" (from English "to")
- `pir` — ≈ (approximately, no strong cross-language mnemonic, picked for distinctness)

Negation by existing `no` prefix:
- `nosam` = ≠, `nomin` = ≥, `nomag` = ≤

Plus-or-minus, ranges, distributions are *compositions* of these. No special syntax. Examples sketched (specific digit-roots TBD):
- "around 15" → `pir pi fi`
- "between 2 and 8" → uses `tom` between the two numbers
- "≥ 10" → `nomin` + the number
- gaussian/uniform/bimodal distributions → eventually need distribution-shape roots; parked.

Deliberately deferred:
- The 12 digit-roots themselves (10 used in decimal mode). They need careful acoustic-distinctness work and mnemonic tuning. Frequent enough to deserve dedicated design.
- Distribution-shape roots.
- Arbitrary-base notation in spoken form (user's written `9_12.5` syntax).
- Whether pronoun-like quantifiers ("some", "all", "none", "many", "few") are part of this system or a separate operator class.

## 2026-05-15 — 12 digit roots assigned
Same 10 roots serve decimal (0–9); dozenal adds 2 more (A=10, B=11). All single CV, all initial-consonant unique across the set.

Design priority: maximum acoustic distinctness between *adjacent* digits, because confusing 3↔4 is far worse than confusing 3↔9. Every adjacent pair differs in both consonant and vowel.

| Value | Root | Mnemonic |
|---|---|---|
| 0 | `zo` | English **z**ero |
| 1 | `pa` | distinctness-driven; no strong cross-language match |
| 2 | `du` | Latin/Italian **du**o, Spanish **do**s |
| 3 | `re` | Spanish t**re**s (/r/ carries it) |
| 4 | `ko` | Latin **q**uattuor / Spanish **c**uatro |
| 5 | `fi` | English **fi**ve |
| 6 | `sa` | English **s**ix, Spanish **s**eis |
| 7 | `chi` | Mandarin **qī** /tɕʰ/ → `ch` |
| 8 | `bo` | Spanish o**ch**o (vowel /o/, /b/ for distinctness from 7) |
| 9 | `ne` | English **n**ine, Spanish **n**ueve |
| A (10) | `ja` | dozenal only; arbitrary, picked for distinctness |
| B (11) | `gi` | dozenal only; arbitrary, /g/ otherwise unused |

Worked examples:
- decimal 243 → `du ko re dem`
- decimal 12.5 → `pa du dem fi`
- dozenal 14;6 (= decimal 16.5) → `pa ko doz sa`
- dozenal "A0B" (= decimal 1451) → `ja zo gi doz`
- 3 × 10⁹ → `re pem ne dem`
- approximately 15 → `pir pa fi dem`

Risk flagged: digit 6 `sa` is a substring of operator `sam` (equal); digit 4 `ko` is a substring of verb root `kom`. CV digits will sometimes overlap with CVC roots they're contained in. Resolution: needs a prosodic convention (likely "CVC carries final-consonant stress; CV doesn't") to disambiguate in running speech. Parked as a parsing/prosody question, not a reason to redesign digits.

## 2026-05-15 — Precise temporal-modifier system framework
Question opened: how does Lexor express precise time, given that inner-vowel tense only covers coarse frames (present/past/future/etc.)?

Parallel to the quantifier system in structure: coarse handling is built into word morphology (inner vowel for tense, dropped plural for quantity); precise handling is a *separate composable layer* invoked only when needed. Same architectural pattern, different domain.

Three opportunities to do better than English/Spanish were identified:
1. **Named days/months are pure overhead.** Memorizing 7+12 arbitrary names is rote work that buys nothing — numeric calendar works (Mandarin: 星期一 = week-day-1 = Monday) and is culturally universal.
2. **Irregular plural for frequency.** English "every 3 days" vs "every day" use different morphology; Lexor doesn't need this if frequency is a dedicated operator.
3. **Redundant relative-time roots.** Languages have separate words for yesterday/today/tomorrow when those are trivially derivable from "day" + "before/after now."

Decisions locked:

1. **Numeric calendar.** Day-of-week = `[day] 1..7`, month = `[month] 1..12`. No named-day roots.

2. **Time-relation prepositions** (closed class, CVC, parallel to quantifier operators):
   - `tep` — at / in / on (point in time)
   - `pen` — during (within a span)
   - `sin` — since (start point)
   - `lim` — until (end point)
   - `ant` — before
   - `pos` — after
   - `pir` reused — approximately (in time)

3. **Frequency operator: `kex`** ("every / each"). Attaches to any duration uniformly. `kex dim` = every day, `kex re dim` = every 3 days, `kex sem` = every week.

4. **Reference frame defaults to time-of-utterance.** Now = root `nun` (Latin nunc, German nun, obvious mnemonic). Yesterday and tomorrow are compositions:
   - yesterday = `ant pa dim` (before 1 day)
   - tomorrow = `pos pa dim` (after 1 day)
   - last week = `ant pa sem`
   - in 3 hours = `pos re xor`

5. **Tense vowel and time modifier must semantically agree.** Saying "I will-eat yesterday" is a semantic error (matching English/Spanish behavior). Inner vowel = coarse frame, time modifier = precision; consistency required.

6. **Position**: time modifier at sentence end by default, fronted for topicalization. Matches the general "thing first, modifiers after" Lexor pattern (verb first, role markers after the noun, etc.).

Time-unit roots (placeholders, may revise in vocab buildout):
- `mom` second, `mit` minute, `xor` hour, `dim` day, `sem` week, `mes` month, `vet` year
- Note: many obvious roots (`min`, `sek`, `hor`, `dur`) were already taken by operators or verbs or were phonetically illegal (`h`+vowel forbidden). `xor` and `vet` are weak mnemonics — flagged for possible revision.

Worked examples:
- "I ate yesterday" → `lomo y ant pa dim` (eat-past I before-1-day)
- "She will arrive in 3 hours" → `veni e pos re xor`
- "Since 2020" → `sin du zo du zo dem` (year as digit-stream, decimal-marked)
- "Around noon" → `pir tep [noon-expression]` — noon is "hour 12 in dozenal" or `xor pa du dem` (hour 12 decimal)

Parked sub-questions:
- 12-hour vs 24-hour clock convention (recommend 24-hour to match ISO and dozenal-friendliness)
- Dedicated roots vs compositions for noon / midnight / dawn / dusk
- Time zones
- Event-relative ("when X happens") — needs subordinate-clause construction first
- Whether the weakly-mnemonic time-unit roots (`xor`, `vet`) get replaced

## 2026-05-15 — Pronoun behavior with role vowels
Question: pronouns are sub-CVC (V or CV shape), so they don't fit the standard CVCV(CV) word shape where the outer vowel is the role marker. Do they take role vowels, and how?

Three options considered:
- **A. Suffix role vowel directly** (chosen). Add the role vowel after the pronoun. Simple, parallel to noun behavior.
- **B. Dedicated forms per pronoun×role.** Like English I/me/my. Rejected — 11 pronouns × 4 roles = 44 memorizations, way too much overhead for a slot meant to be optional.
- **C. No role marking on pronouns, position only.** Rejected — VOS sentences with two pronouns get ambiguous exactly when marking is most needed.

Mechanism locked:
- Bare pronoun = default role (position determined).
- Suffix `-e` subject, `-o` object, `-u` recipient, `-i` instrument when explicit.
- Collision case (pronoun-final-vowel = role-vowel): doubled vowel pronounced as long vowel (held twice). Phonetics.md permits 2 consecutive vowels and forbids only repeated *consonants*, so this is legal. Long vowels are a clear distinction in many languages (Japanese, Latin, Finnish), so listeners parse fine.

Worked table (selected):
- `y` (I) → `ye/yo/yu/yi` for subject/object/recipient/instrument
- `u` (you) → `ue/uo/uu(long)/ui`
- `e` (he/she) → `ee(long)/eo/eu/ei`
- `i` (it) → `ie/io/iu/ii(long)`
- `la` (we-generic) → `lae/lao/lau/lai` (default already ends in `a`, marker adds a second vowel)
- `lo` (they) → `loe/loo(long)/lou/loi`
- `li` (they-objects) → `lie/lio/liu/lii(long)`

Notes:
- `l-` series pronouns produce two-vowel endings (`lae`, `loe`, etc.). These are within the phonotactic limit and pronounceable as diphthong-like glides.
- The convention "bare pronoun = default role" mirrors "bare noun outer slot = `a` default" — same principle, different mechanism (vowel-final pronoun doesn't need an extra `a`).

Doesn't affect existing pronoun roots in roots.md (the table is preserved); just adds the role-marker layer on top.

## 2026-05-15 — Subordinate clauses: single universal complementizer `ke`
Foundational gap: precise temporal expressions need "when X happens" constructions; complex sentences need relative and complement clauses; conditionals need an "if" construction. English uses ~10 different subordinators (who/which/that/when/while/although/because/since/whereas/unless) — that's pure clutter.

Design principle: ONE universal clause-introducer particle, function determined by what *precedes* it. Avoids subordinator-memorization and matches Lexor's general "context selects meaning" preference (e.g. same vowel positions carry different info depending on word class).

Particle: **`ke`** — universal subordinating complementizer. Mnemonic: Spanish/French/Italian/Portuguese *que/che* converge here; very high cross-Romance recognition. Single CV.

Function depends on context:
- Noun + `ke` + clause → relative ("the X that…")
- Cognitive/speech verb + `ke` + clause → complement ("say/think/know that…")
- Time preposition (`tep`/`pen`/`ant`/`pos`) + `ke` + clause → temporal ("when/during/before/after…")
- Causation particle (TBD) + `ke` + clause → reason ("because/since…")

Conditional gets its own particle because the structure is genuinely different (paired antecedent/consequent, not a clause hanging off a single host):
- **`is`** — conditional "if" (mnemonic: English "if", Spanish "si"). Sub-CVC, like pronouns. Pairs with conditional inner-vowel `y` on the consequent verb for proper alignment.

Relative-clause gap mechanism: when `ke` opens a relative clause attached to a noun, the embedded clause has one missing argument slot. The modified noun fills that gap semantically. If the gap's role is non-default (subject when object position is empty, etc.), the role-vowel pattern signals it; otherwise position handles disambiguation.

Position: subordinate clause comes after its host (consistent with "thing first, modifiers after"). Main clause precedes the subordinate when both appear in a sentence.

Worked examples (using current root set):
- "the eater who eats apples" → `lomera ke lome [apple]a` — embedded clause `lome [apple]a` is missing its subject, which is filled semantically by `lomera`.
- "the apple that the eater eats" → `[apple]a ke lome lomera` — embedded clause missing its object.
- "I know that she left" → `vise y ke golo e`
- "Bring the book before she arrives" → `feru u libra, ant ke veni e`
- "When she arrives, I will leave" → `goli y, tep ke veni e`
- "If it rains, I'll stay home" → `[stay]y y, is [rain]e`

Parked sub-questions:
- Causation particle for "because/since"
- Embedded-question marker ("what she said") — needs the broader question system designed first
- Multiple nested clauses — does `ke` stack cleanly, or do we need parenthesis-equivalent disambiguators?
- Comma/pause prosodic conventions between main and subordinate

## 2026-05-15 — VOS reflection (kept, not changed)
User asked: was VOS the right choice?

Honest assessment recorded so the question is settled rather than recurring:

Facts:
- VOS is rare cross-linguistically (~1–3% of natural languages — Malagasy, Tzotzil, some Philippine languages).
- SOV ~45%, SVO ~42%, VSO ~9%. Most verb-initial languages are VSO, not VOS.

Coherent arguments *for* keeping VOS in Lexor:
- Predictable verb-object skeleton at the front means the subject is a clean optional tail. Drop the subject and nothing breaks — matches the no-mandatory-marking principle better than SVO would.
- Object adjacent to verb keeps the patient/affected next to the action that operates on it.
- Action-first matches "what happened?" priority in many situations.

Real friction VOS introduces:
- Heavy subject NPs bury the action at the far end.
- Two animate nouns force role-vowel marking more often than SVO would (SVO has positional disambiguation between the nouns).
- Runs against the L1 intuitions of ~87% of probable learners (SVO + SOV speakers).

Honest alternative considered: **VSO** (verb-subject-object).
- More common (~9%, well-attested: Welsh, Classical Arabic, Hawaiian, Tagalog, Biblical Hebrew).
- Preserves verb-first action-prominence.
- Matches natural agent→patient cognitive flow (the doer comes immediately after the verb; the patient lands at the end where heavy NPs typically prefer).
- The "processing space after the verb" — listener processes the action with only the subject as additional info, then the object arrives last — is the structural reason VSO works in practice.

Decision: **keep VOS, eyes open about the trade.** VSO is a low-cost retrofit if friction emerges in practice (only the relative position of subject vs object changes; role-vowel system handles either). This is not re-decided every time — see this entry instead.

## 2026-05-15 — Scope, ambiguity, and the precision-by-default principle
User raised the hardest design problem in the language: how do you eliminate ambiguity (multiple distinct meanings for the same sentence form) without making the language tedious? Bad laws and contract disputes are downstream of this failure across many natural languages.

First proposal (rejected by user): a four-layer system with default positional rules + grammatical prosody + explicit operators + named binding. Critique was sharp and correct: the layered system left layers 2–4 *optional*, so sloppy speakers stay in Layer 1 and produce ambiguous sentences. Listeners then do the "interpret the obvious meaning" dance — exactly the rot we're trying to eliminate. The structure permits failure; "obvious interpretation" claims the failures as features.

Revised principle (locked):

**Every well-formed Lexor sentence has exactly one meaning. Vagueness allowed (one meaning with unspecified parameters); ambiguity forbidden (multiple distinct meanings competing for the same form).**

Crucial distinction surfaced in clarification:
- *Vague* = single meaning, parameters unspecified. "Some people came." Speaker doesn't say how many. ONE claim, with a gap. Cheap and natural — no extra morphology required.
- *Ambiguous* = multiple distinct meanings. "The 12 cities have NYC's population." Could mean each-city or all-combined. The grammar must forbid this.

This corrects an earlier overreach where I proposed mandatory `pad`/`mas` markers on every plural predication. That would force speakers to commit when they may genuinely not know. The correct rule: unmarked = "speaker is explicitly not committing" (vague, valid, short). Marked = one specific reading. Three forms, three distinct meanings (one of which is vagueness-as-a-statement).

Listeners do not "interpret" — they take the grammar at face value. If the speaker said something vague, the listener knows it's vague. If the speaker wanted to commit, they would have marked. Misalignment is the speaker's responsibility for using wrong syntax, not the listener's burden to charitably guess intent.

Structural mechanisms that achieve this:

1. **Strict positional rules** pin scope:
   - Modifier attachment: only to immediately adjacent unit. Wide scope requires restructuring (front the modifier) or named binding.
   - Operator scope (`sol`, `no`, `tot`): scopes over its adjacent argument. Three positions = three distinct meanings.
   - Quantifier scope: linear order = logical scope. First mentioned has widest scope.
   - Mixed AND/OR is grammatically forbidden in flat form; named binding required for grouping.

2. **Optional disambiguation markers** for inherently positional-cue-free cases:
   - `pad` (distributive) / `mas` (collective).
   - "Is"-overload copula family (separate sub-question).
   - Future: modal-scope markers when modals are designed.
   - Unmarked = vagueness, single meaning.

3. **Prosody is for focus and parsing aid, not scope.** Demoted from scope-resolution. Grammar already pins meaning; prosody adds emphasis and tracks phrase boundaries in real-time speech.

4. **Named binding** for compositional clarity of long/complex expressions. Used in legal text, formal proofs, multi-level nesting. Not an escape hatch — those structures shouldn't exist; named binding helps when natural complexity overloads working memory.

What this does NOT solve (honest residuals):
- Reference resolution ("which man?" when context has multiple).
- Genericity ("dogs bark" — all dogs, typical dogs, this kind of dog?).
- Word-level vagueness ("tall" — how tall?). Numeric precision is available but speakers can't be forced to use it.
- Idiom/figuration — Lexor probably rejects idioms entirely (compositional only) plus a literal-vs-figurative marker for metaphor.

The "user-the-jerk" failure mode is structurally prevented. Sloppy speech becomes visibly imprecise (the marker would be there if precision were intended, and isn't) rather than disguising failure as natural ambiguity.

## 2026-05-15 — Nested clauses and the staged-reasoning particle set
Two related questions resolved together.

### Nested clauses
User asked for a definitive answer on how deep `ke` can stack.

Mechanism: each `ke` pairs with its immediately preceding host. Strict adjacency. The grammar permits arbitrary recursion in principle (no depth limit in the rules).

Style rule (not grammar): humans can track ~2 levels of nesting in real time. Beyond that, OR any time the relative clause needs to close and the outer clause continues, use named binding instead.

Example showing why named binding is needed:
- "The man who saw the dog [then] bit the cat" — man bit cat, not dog.
- Adjacency-only: `man ke vise dog ke bite cat` would put the biting on the dog. Wrong.
- Named binding: `def M = man ke vise dog. M bite cat.` Closes the relative clause by naming the result; fresh sentence claims the next predication.

No terminator words (Lojban-style closers feel programmer-y; named binding does the disambiguation work and is useful regardless). Prosody helps parsing in real time but isn't load-bearing.

### Reasoning-particle set (from the modus tollens test case)
User asked: how would Lexor express modus tollens `(A → B) ∧ ¬B ⊢ ¬A`?

English and Spanish both struggle: trying to fit it in one sentence creates 3-level nested logical structure that's awkward to parse. "If A implies B and B is not true, then A is not true" / "Si A implica B, y B no es cierto, entonces A no es cierto" — both stack an implication inside a conjunction inside a conditional. Listeners stumble.

Both languages can do better by *staging* — multiple sentences, each holding one piece of the argument. "Take it as given that A leads to B. Now: B did not happen. So A did not happen." This works, but the connectives ("take as given", "so") are lexical bandaids on top of an inadequate grammar.

User's insight: the cognitive structure of this proposition is *sequential*, not nested. Lexor should make staging the grammatically natural form, not nesting.

Locked: three new closed-class particles for multi-step reasoning, plus a causal/logical implication distinction.

- **`dat`** — premise marker. Asserts a sentence as a premise available for subsequent reasoning. Mnemonic: Latin *datum*, English *data*, Spanish *dado*. CVC.
- **`erg`** — inference marker / "therefore." Marks a sentence as derived from prior premises. Mnemonic: Latin *ergo*. CVC.
- **`imp`** — logical implication. Mnemonic: English *implies*. Distinct from `is` (causal/temporal conditional).

Modus tollens in Lexor:
```
dat A imp B.    ← Given: A logically implies B.
noB.           ← Not B.
erg noA.       ← Therefore, not A.
```

Three sentences, each with one meaning, each parseable independently. The logical relationship between them is explicit (premise / observation / conclusion) rather than encoded in nested structure.

Proof-by-cases extension:
```
dat A imp B.                ← Given: A → B.
is B, [unconstrained].       ← When B holds, A may or may not. (forward direction underconstrained)
is noB, noA.               ← When B doesn't hold, A doesn't either. (modus tollens)
```

Each case parallel, neither nested in the other.

The causal-vs-logical distinction is a real Lexor advantage:
- `is A, B` — causal/temporal: "if A happens, B happens." Everyday use.
- `A imp B` — logical: "A entails B." Formal/proof use, axiom-like.

English's "if" overloads both. Lexor splits them — speakers can now distinguish "if you press the button, the light turns on" (causal `is`) from "all even numbers imply divisibility by 2" (logical `imp`).

Parked sub-questions:
- Scope-of-premise: when does a `dat`-asserted premise expire? Until end of paragraph? Until explicit retraction? Probably until discourse turn ends, but needs design.
- Other proof-structuring particles: "suppose for contradiction," QED-marker, case-splitting marker. Defer until they arise.
- Whether `imp` needs siblings for necessary vs sufficient implication, biconditional, etc.

## 2026-05-15 — Coordinators (`kun`, `vel`) and the depth rule
User asked: how does a listener parse multiple predications at the same depth inside a subordinate clause? Would you repeat `ke`?

Repeating `ke` doesn't work — the adjacency rule says each `ke` attaches to its immediately preceding noun, so a second `ke` would descend further (relative clause on the previous noun), not stay at the current level.

Real cases for same-depth multi-predication:
- "The man who saw the dog and bit the cat" — both predications about the man.
- "The eater who eats food or drinks water" — disjunction at the same depth.

Solution: dedicated coordinators that signal "same depth, another predication."

Locked:
- **`kun`** — AND. Latin *cum* ("with, together"). CVC, free.
- **`vel`** — OR. Latin *vel*. CVC, free.

Mixed AND/OR remains forbidden in flat form (already decided); named binding required to group.

Worked example: "The man who saw the dog and bit the cat"
- `man ke vise dog kun bite cat`
- Parse: `man` outer noun, `ke` opens relative clause on man, `vise dog` first predication (gap=subject, object=dog) closes, `kun` says same-depth continuation, `bite cat` second predication (gap=subject, object=cat) closes, no more coordinators → ascend.

Contrast: "The man who saw the dog that bit the cat" — `man ke vise dog ke bite cat`. Second `ke` descends (attaches to `dog`). Different particle, different depth.

Depth rule made explicit:
- `ke` → +1 depth.
- `kun` / `vel` → same depth (continue current clause).
- Verb-argument completion + no following coordinator → automatic ascent.
- No terminator words; ascent is signaled by argument-counting, not by an explicit closer.

Closure rule made explicit: a clause introduced by `ke` is grammatically closed when all argument slots of its head verb are filled (the gap counts as one filled slot) AND no coordinator follows. Next word goes to next-outer open clause.

Edge case acknowledged: coordinated relative clauses where the gap fills different slots in each clause (e.g., "the man whom I see and who saw the dog" — gap is object of first verb, subject of second). Naive chaining loads role-vowel disambiguation onto the listener. Solution: named binding restructures into atomic sentences. Same pattern as deep nesting — when complexity threatens working memory, name and split.

## 2026-05-15 — Question system: universal particle `ka`, position determines type
Foundational gap: Lexor had no way to ask anything. Embedded questions ("what she said") were also blocked.

Design principle: same as every other Lexor operator — one particle, position determines meaning. Avoids the English/Spanish clutter of having ~6 wh-words (who/what/when/where/why/how / quién/qué/cuándo/dónde/por qué/cómo).

Locked: **`ka`** — universal question particle.
- Mnemonic: Japanese か (well-known interrogative). CV, distinct from existing operators and pronouns.
- Adjacent to digit `ko` (4) in /k/-initial space but different vowel and different syntactic position.

Position pins type:
- **Sentence-initial** → yes/no question over the whole proposition. `ka golo e` = "Did she leave?"
- **In an argument slot** → wh-question about that slot. `golo ka` = "Who left?" `lome ka e` = "What did she eat?"
- **After a preposition** → wh-question about that role. `tep ka` = "When?" `lok ka` = "Where?"
- **Inside a `ke`-clause** → embedded question. `[wonder] y ke dik ka e` = "I wonder what she said."

Choice questions compose from existing pieces: `ka X vel Y` — yes/no over a disjunction. "Coffee or tea?" needs no new mechanism.

Spatial preposition added in passing: **`lok`** — at/in (spatial location). Mnemonic: Latin *locus*. Pairs with `tep` (temporal "at") as the spatial counterpart. Needed because previously `tep` was time-only, so "where?" had no preposition to compose with `ka`. Full spatial-preposition family (under, over, near, beside, etc.) parked.

Person vs object distinction: `ka` is generic. Context (verb selectional preferences, slot position) usually disambiguates: `vise ka e` = "she sees what/whom?" is interpreted in context. Mandarin works similarly (`什么 shénme` covers both depending on construction). For rare cases where context fails, an explicit person-marker / thing-marker is needed; parked.

Worked examples:
- `ka golo e` → "Did she leave?"
- `ka lome lometa e` → "Did she eat the food?"
- `golo ka` → "Who left?"
- `lome ka e` → "What did she eat?"
- `golo e tep ka` → "When did she leave?"
- `golo e lok ka` → "Where did she go?"
- `ka coffee vel tea` → "Coffee or tea?"
- `[wonder] y ke dik ka e` → "I wonder what she said."
- `[tell-imperative] u y ke golo ka` → "Tell me who left."

Considered and rejected: dedicated wh-roots (who/what/when/where/why/how as separate words). Cost: 6+ memorizations, no compositional value. Benefit: minor brevity. Compositional `ka` is more Lexor-like and the verbose-ness (1-2 syllables longer) is a small price.

Parked sub-questions:
- Manner preposition for "how?" questions.
- Causation preposition for "why?" questions (tied to "because/since" gap).
- Person vs object disambiguation marker on `ka` when context fails.
- Tag questions ("she left, didn't she?") — likely composable from yes/no + negation.
- Rhetorical questions — register distinction, not grammar.
- Full spatial-preposition family (under, over, near, beside, etc.).

## 2026-05-16 — Survey of senses collapsed by English "is" / Spanish ser-estar
Before designing Lexor's replacement, mapping out what natural-language copulas actually do. Each is a distinct semantic relation; collapsing them all into one word creates the ambiguities catalogued in pain.md.

The nine senses of English "is":

1. **Identity / equation**: "Mark Twain is Samuel Clemens." X = Y (symmetric; refer to the same entity). Math: `=`.
2. **Property attribution**: "The sky is blue." X has-property P (asymmetric).
3. **Set membership**: "A whale is a mammal." X ∈ Y (X is one element of set Y).
4. **Set inclusion / subset**: "Mammals are animals." X ⊆ Y (all members of X are also members of Y). Different from membership: mammals-as-a-set aren't an element of animals.
5. **Existence**: "There is a problem." ∃X.
6. **Permanent vs temporary state**: "She is a doctor" vs "She is tired." Spanish marks (ser/estar); English collapses.
7. **Literal content / quotation**: "My name is 'John'". X's content is literally the string Y, not a property.
8. **Auxiliary in aspect**: "She is going." Continuous aspect. Already handled by Lexor's `x` aspect marker.
9. **Passive voice marker**: "She is loved." Not needed in Lexor because role-vowels make passive unnecessary.

Senses 1–7 are real distinctions Lexor needs to express separately. 8 and 9 are already handled or eliminated by prior design.

Decided: split into multiple distinct verbs / particles. One copula per relation. The user's intuition is that `password = 'incorrect'` (literal) is genuinely not the same as `password has-property incorrect` (predication), and the design should reflect that.

Minimal new inventory (proposed shape, specific roots TBD next round):
- **Identity** (sense 1): reuse `sam` (already the `=` comparison operator).
- **Predication** (sense 2): new copula verb. State/property distinction (sense 6) rides on the inner tense vowel — atemporal `a` for essential property, present `e` for current state. (Pending user confirmation on whether to split further into permanent/temporary as Spanish does.)
- **Membership** (sense 3): new particle, math `∈`.
- **Subset** (sense 4): either a new particle or composed from universal-quantifier + membership ("every X mem Y"). (Pending user choice.)
- **Existence** (sense 5): either composed from existential-quantifier ("some X exists") or a dedicated existence-verb. Likely the former.
- **Literal content** (sense 7): paired open/close quotation markers, mirroring how speakers say "quotes … quotes" in spoken English.

Three sub-questions to settle before locking specific roots:
- Sense 6 (permanent vs temporary): split via separate copulas (Spanish-style) or via the tense-vowel system on a single predication copula?
- Sense 4 (subset): dedicated particle or composition?
- Sense 7 (quotation): paired open/close (like spoken English "quotes...quotes") — yes per user.

## 2026-05-16 — "Is"-overload replacement set locked
User decisions on the three sub-questions:
1. Permanent vs temporary state: split via separate copulas, Spanish-style. (User intuition leaned Spanish.) The argument: real ambiguities in English ("the patient is depressed" — chronic or today? "he is reliable" — trait or recent behavior?) are eliminated by splitting.
2. Subset: composition, not dedicated particle. Matches Lexor's pattern of composing from primitives. `tot X mem Y` ("every X is-member-of Y") expresses ⊆.
3. Quotation: paired open/close markers, matching how spoken English uses "quotes…quotes" — but with distinct words for open vs close so nested quotations remain unambiguous.

Locked inventory:
- **`sam`** — identity (X = Y, symmetric, refer to the same entity). Reused from existing `=` comparison operator. Math: `=`.
- **`est`** — essential predication. Spanish *ser*. Latin *esse*. "X has essential property P" / "X is essentially Y." Permanent traits, classifications, definitions.
- **`sta`** — state predication. Spanish *estar*. Latin *stare*. "X is currently in state P." Temporary states, current situations, transient properties. Note: `sta` is CCV — valid per phonetics.md (2-consonant clusters allowed).
- **`mem`** — set membership (X ∈ Y). "X is one element of set Y."
- **Subset by composition**: `tot X mem Y` ("every X is member-of Y") expresses X ⊆ Y. No dedicated subset particle — the universal quantifier `tot` plus `mem` does the work.
- **Existence by composition**: `kel X` ("some X exists") expresses ∃X. No dedicated existence-verb — the existential quantifier `kel` plus context does the work.
- **`lit … fin`** — paired quotation markers. Open with `lit` (literal), close with `fin` (finish). Inside the pair, content is treated as raw string, not parsed as Lexor predications. Distinct open and close words ensure nested quotations remain unambiguous (which a same-word-both-times convention couldn't).

Worked examples:
- "Mark Twain is Samuel Clemens" → `[MarkTwain] sam [SamuelClemens]` (identity)
- "The sky is blue (essentially)" → `est sky blue` or `[blue-property] est sky` — predication of essential property
- "She is tired (right now)" → `sta she tired` — predication of current state
- "A whale is a mammal" → `[whale] mem [mammals]` — set membership
- "Mammals are animals" → `tot [mammal] mem [animal]` — every mammal is member of animals (subset)
- "There is a problem" → `kel [problem]` — some problem exists (existence)
- "The password is 'incorrect'" → `[password] sam lit incorrect fin` — identity with literal string content (sense 7 — literal not predication)
- "The password is incorrect" (it's wrong) → `sta [password] [incorrect-property]` — predication of a current-state error (sense 2 + 6, temporary)
- "My name is 'very stupid'" → `[name-mine] sam lit very stupid fin` — literal-content identity, not predication

The password example specifically motivated the `sam`+`lit/fin` vs `sta`+adjective split. Two completely different facts about the password; two completely different sentence forms.

Also locked the rest of the universal-quantifier operator family that had been informally proposed:
- `sol` — only / restriction (previously locked).
- `tot` — all / every (∀).
- `nul` — none.
- `kel` — some (∃).

Plus the previously-locked `pad` (distributive) and `mas` (collective).

Phonotactic note: `est` is V-C-C (vowel-initial, ends in 2-consonant cluster). `sta` is C-C-V (starts with 2-consonant cluster). Both legal per phonetics.md (2-consonant clusters allowed; only 3+ forbidden). These are unusual root shapes compared to the standard CVC, but the cross-language recognizability (English/Spanish/Italian/Latin all use est-/sta- roots for being) is worth the irregularity.

Parked sub-questions:
- A "variable" marker distinct from `lit` for cases where a name stands for something computed/derived (TODO.md "literal vs variable"). `lit/fin` handles the literal case; the variable case may need its own marker.
- Tag questions ("she left, didn't she?") — sanity check that they compose from yes/no + negation.
- Other copula-like senses: "X seems Y" (epistemic), "X becomes Y" (transition). Probably regular verbs, not copulas.

## 2026-05-16 — Manner preposition `mod`, causation preposition `kaw`, tag-question composition

Closed three linked items from the question-system parking lot (tasks.md). The question system was already locked around universal `ka` whose meaning is pinned by position, with `tep` (time) and `lok` (space) as the prepositions composing with `ka` for "when?" / "where?". Two slots were missing: **manner** ("how?", "by means of [doing X]") and **causation** ("why?", "because/since"). Closing both unblocks full use of the question system and unblocks the causation subordinator.

### Manner preposition: `mod`

Question opened: what preposition does `ka` compose with for "how?" and adverbially for manner ("by doing X", "in such-and-such way")?

Distinction first. The instrument role-vowel `-i` already covers "with [tool]" — "she opened it with a key" → `[key]-i` on the noun. Manner is the *non-tool* axis: "how did she fix it?" can be answered by "carefully" (manner adverb) or "by hammering" (manner-of-action), neither of which is a tool. So manner-preposition takes a manner expression (adjective, gerund clause, or full clause via `ke`), distinct from the instrument vowel.

Options considered:
- `mod` — Latin *modus* ("manner, way"). Survives in English mode, modal, modus operandi; Spanish modo; Italian modo; French mode. Cross-Romance recognizability is unusually strong for a 3-letter CVC. Clean phonotactically.
- `med` — Latin *medium* ("by means of"). Weaker because *medium* in modern usage is more "middle/medium" than "manner". Likely collides with a future "middle" or "average" root.
- `man` — surface form of English *manner*. Strong English mnemonic but the CV `ma-` and CVC `man` are likely needed for a future "hand" root (universal across Romance, also Germanic *hand*); reserving `man` for body-parts is better.
- `via` — Latin *via* ("by way of"). Phonotactically wrong: V-V-V (or C-V-V depending on analysis of /j/), doesn't fit the CVC closed-class shape used by other prepositions (`tep`, `lok`, `ant`, etc.).

Picked **`mod`**. Tradeoffs accepted: minor risk of confusion with future "mode" (in the statistical sense — most frequent value) or "modal" (in the modal-logic sense), both of which can compose from `mod` plus other markers rather than need their own root.

Compositions enabled:
- `mod ka` — "how?" / "in what manner?" (question)
- `mod [manner]` — "in [such-and-such] manner" (adverbial)
- `mod ke [clause]` — "by [doing X]" (manner clause: "by hammering it" = `mod ke [hammer-verb] o`)

Worked examples:
- `kompo e mod ka` → "How did she fix it?" — VOS with `e` marking subject, manner-question at the end.
- `kompo e mod ke martelo o` → "She fixed it by hammering it." — Literally: fixed[past] she manner that hammer[past] it.
- `koma e mod [careful-adjective]` → "She eats carefully." — manner-adverbial with no clause.
- `koma e [chopstick]-i mod [careful-adjective]` → "She eats with chopsticks carefully." — instrument-vowel and manner-preposition co-occur cleanly without collision.

### Causation preposition: `kaw`

Question opened: what preposition does `ka` compose with for "why?", and is the "because/since" subordinator the same root?

Decision: one root does both. `kaw ka` = "why?" (question), `kaw ke [clause]` = "because [clause]" (causal subordinator). Matches the established pattern: time gets `tep` (with `tep ka` = "when?", `tep ke X` = "when X happens"); space gets `lok` (with `lok ka` = "where?", `lok ke X` = "where X is"). Causation should not be a special case.

This also keeps the *epistemic* "why" (purpose / motivation) and the *physical* "why" (cause) under one root, which the user may later split if a real ambiguity surfaces. For now, vagueness on the cause-vs-purpose axis is allowed (per the precision-by-default meta-principle); only structural ambiguity is forbidden, and there is none here.

Options considered:
- `kaw` — surface form of English *cause*. Spelled with `w` to avoid the V-V-V shape that `kau` would have. Phonotactically clean CVC. Strong English mnemonic.
- `kos` — from Latin *causa* / Spanish *porque*. Risk of collision with a future "thing" (Spanish *cosa*) root.
- `kuz` — from English colloquial *'cuz*. Vivid but informal-feeling; weaker for the formal-reasoning use case where `kaw` will appear alongside `dat`/`erg`/`imp`.
- `kar` — irregular sourcing. Weak mnemonic.

Picked **`kaw`**. Tradeoffs accepted: only English-leaning of the candidates; Romance speakers won't immediately recognize it. But Lexor already has Romance-heavy roots elsewhere (`ant`, `pos`, `sin`, `lim`, `mod`), so picking up an English-leaning one for causation balances the lexicon slightly. The phonotactic cleanness (clear CVC, distinct from any existing root) is the bigger win.

Relationship to existing reasoning particles:
- `kaw` — preposition for *real-world* causation. "She left because it was raining."
- `imp` — logical implication. Formal-proof use. "Rain entails wet ground."
- `is` — causal/temporal conditional. "If it rains, the ground gets wet." Pairs with conditional inner-vowel `y`.
- `dat` — premise marker. "Given that it was raining."
- `erg` — conclusion marker. "Therefore the ground got wet."

These five cover the real-world / formal / hypothetical / premise-stating / conclusion-stating axes without overlap. `kaw` slots in cleanly: it's the everyday "because" that doesn't claim formal entailment.

Worked examples:
- `golo e kaw ka` → "Why did she leave?"
- `golo e kaw ke pluvex` → "She left because it was raining." — Literally: left[past] she cause that rain[present-continuous].
- `dat pluvox. golo e kaw ke pluvox. erg [floor-wet-state]` → A staged reasoning chain: given that it rained; she left because it rained; therefore the floor is wet. Mixed `kaw` (causation in the world) and `dat`/`erg` (reasoning structure) coexist without conflict.

### Tag questions (sanity check)

Question opened: do tag questions ("she left, didn't she?", "you're coming, right?") need a dedicated particle, or do they compose from already-locked parts?

The English/Spanish tag pattern is "make an assertion, then briefly request confirmation." Lexor already has:
- Assertion: normal VOS sentence, no marker needed.
- Yes/no question: sentence-initial `ka` covers the whole proposition.

Two compositional options give a tag without a new particle:
1. **Bare `ka?` tag**: assertion, comma, `ka?`. "She left, right?" → `golo e, ka?`. The bare `ka` after a comma reads as "yes/no question about the just-asserted proposition" — confirmation-seeking. Short, ergonomic.
2. **Echo question**: assertion, comma, mini yes/no question echoing the verb. "She left, didn't she leave?" → `golo e, ka nogolo e?`. Verbose but maximally explicit.

Locked: both are grammatical. The bare `ka?` form (option 1) is the default; the echo form (option 2) is available when extra emphasis is wanted ("you didn't *actually* leave, did you?"). No new particle introduced.

Polarity note: English/Spanish tag-question polarity matches the speaker's expectation (positive assertion → negative tag if expecting "yes": "she left, didn't she?"). Lexor's bare `ka?` is polarity-neutral — it just requests confirmation, leaving the speaker's expectation unstated. This is consistent with the no-mandatory-marking meta-principle: speakers who *want* to convey expectation can use the echo form with explicit `no`.

Worked examples:
- `golo e, ka?` → "She left, right?"
- `golo e, ka nogolo e?` → "She left, didn't she?" (with explicit negative-polarity tag conveying speaker expects "yes")
- `pluvex, ka?` → "It's raining, right?"

### What this unblocks
- Full "how/why" question coverage — the question system is now feature-complete for the standard wh-set (who/what/when/where/why/how) without any dedicated wh-roots.
- Causation subordinator — closes one of the remaining gaps in the subordinate-clause system (`ke`-clauses on `kaw` now work the same way as on `tep`, `lok`).
- Tag questions don't need a Session N+2 round of their own.

### Parked
- Cause-vs-purpose split on `kaw` — only if real ambiguity surfaces during examples.md validation.
- "Mode" in the statistical sense, "modal" in the modal-logic sense — compose from `mod` + qualifiers rather than dedicate new roots, unless examples.md forces a split.

## 2026-05-16 — Variable marker `var`, no lexical opposite, `def` syntax locked

Closed the second sub-batch of Session N+1: the variable/placeholder marker (item 4 in the plan), the lexical-opposite question (item 11), and the exact form of named-binding `def` (item 6). These three were grouped because they touch the same conceptual region (markers that flag a word as something other than a plain content reference) and decisions on one constrain the others.

### Variable/placeholder marker: `var`

Question opened: how does Lexor flag a word as a placeholder or bound variable, distinct from a regular noun and distinct from a literal string?

Already-locked context: `lit … fin` is paired open/close quotation for *literal* content — the inside is raw string, not a parsed predication. The remaining case is the *variable* one: "go to `<path>` and read `<path>`" (template slot, both occurrences refer to the same unfilled position) or "let X = ..., then X..." (bound name standing for a computed expression). Neither is literal — the slot/name *will be* substituted with real content.

Two cases — but they collapse to one marker. In both, the function is: "treat the marked word as a slot-or-name, not as its regular meaning." Whether that slot is filled later by context (template) or by an explicit binding (formal expression) is a separate question handled by `def` (below).

Options considered:
- `var` — transparent English/Latin (*variabilis*). Clean CVC. Immediately recognizable to anyone with programming or math exposure.
- `nom` — Latin *nomen* "name". Too generic; "name" as a regular noun is already needed in everyday vocabulary, will collide.
- `pla` — from "placeholder". Weak mnemonic outside English; "place" is also a likely future root.
- A vowel-prefix like `i-` or `a-` — too short, collides with role vowels and conditional-prefix slots.

Picked **`var`**. Single-word scope (the immediately following word). Composable: `var path` is a slot/name named "path". Two occurrences of `var path` in the same discourse refer to the same slot. Distinct from regular `path`, which means the actual noun.

Worked examples:
- `golo u tep var path. kompo u var path` → "Go to var-path. Fix var-path." Both `var path` refer to the same slot; the listener understands they get filled with the same value.
- `def var x sam [biggest prime ant 100]. mag var x 50` → "Let var-x be the biggest prime before 100. Var-x is greater than 50." (See `def` below for the binding syntax.)
- `koma var [food-item] e` → "She eats var-food-item." A template where var-food-item is unfilled, awaiting context.

Interaction with other markers:
- `var` + `lit/fin`: distinct, no overlap. `lit incorrect fin` is the literal string "incorrect"; `var x` is a placeholder named x.
- `var` + `no`: composes. `novar x` = "not var-x" (logical negation of the bound value).
- `var` + role vowels: composes. `var x-e` = subject-marked slot.

### Lexical opposite marker: rejected

Question opened: should Lexor have a productive prefix like Esperanto's `mal-` that derives a lexical opposite of an adjective/state (love → hate, hot → cold), distinct from logical negation `no`?

The real distinction this would capture: English "I don't love her" (logical neg, neutral about positive/negative feeling) vs "I hate her" (specific positive antipathy). Spanish makes the same distinction. A productive opposite-marker on `am` (love) would give `mal-am` = hate, saving the root.

Options considered:
- Adopt `kon` (Latin *contra* / English *contra-, counter-*) — neutral connotation, recognizable.
- Adopt `mal` (Esperanto-style) — proven cross-linguistic but connotation-loaded (mal = "bad" in Romance, biases the marker).
- Reject the marker entirely. Use separate roots for each antonym.

Picked **reject**. Rationale:

1. "Opposite" is sharply defined only for binary/scalar concepts. For "red" the additive opposite is cyan, the subtractive is green — vague. For "house", "run", "sleep" — undefined. A productive marker with a fuzzy domain creates fake words.

2. Per the precision-by-default meta-principle, every productive operator should have one canonical meaning. Lexical-opposite doesn't pass this bar. The "vague is allowed" half of the principle says speakers can underspecify — but here the *operator itself* would be underspecified, not the speaker's choice. That's different. Vagueness should be a speaker move, not baked into grammar.

3. Lexor's root-sourcing rule already lets each antonym pull from its natural language source (`am` love / Latin *amare*; `od` hate / Latin *odisse*). Separate roots are cheap given the 2000+ CVC slot space; root-saving is not a priority.

4. The English/Spanish distinction (don't-love vs hate) is preserved compositionally: `noam` (logical negation, neutral) vs `od` (separate root, specific antipathy). The semantic difference is real and Lexor expresses it — just without a productive opposite-marker.

Tradeoffs accepted: 20-50 additional roots in the scalar-adjective vocabulary buildout. Worth it for the conceptual cleanness.

This decision is reversible: if examples.md validation reveals frequent cases where speakers reach for a missing opposite-marker, the question reopens. For now, no.

### Named-binding `def` syntax

Question opened: what is the exact form of "Let X = ..." in Lexor, given that `var` now flags the variable name?

Options considered:
- A: `def var x sam [expression]` — explicit equality via `sam`. Verbose but transparent (reads as "define var-x equal [expr]").
- B: `def var x [expression]` — `def` itself is the binding operator. Shorter.
- C: `var x def [expression]` — infix. Reads more like math (`x := ...`) but breaks Lexor's pattern of leading operators.

Picked **B**: `def var x [expression]`. The bare `def` introduces the binding; no `sam` is needed because `def` already says "this name takes this value." Saves a word per binding and matches Lexor's prefix-operator pattern (negation, quantifiers, premise markers all lead their scope).

Syntax:
- **Introduce**: `def var <name> <expression>` — binds `var <name>` to the expression's value.
- **Reference**: `var <name>` — anywhere in scope, refers to the bound value.
- **Retract**: `nul def var <name>` — explicitly ends the binding. Composes from existing `nul` (none/no) + `def` + the variable.

Worked examples:
- `def var x sam [biggest-prime ant 100]. mag var x 50` — "Let x = biggest prime before 100. x > 50." (Here `sam` is the identity copula inside the bound expression, not part of the `def` syntax itself.)
- `def var path lit /home/user/data fin. golo y tep var path` — "Let path = '/home/user/data'. I go to path." Binding to a literal string.
- `def var f [function-expression]. kompe y var f mod var x` — "Let f = [function]. I apply f to x." Functional binding.
- `nul def var x` — "x is no longer bound."

Scope (default and minimum spec for now):
- **Discourse-local**: a binding persists from the `def` statement until either explicit retraction (`nul def var <name>`) or end-of-discourse (speaker stops or changes topic).
- Sentence-local and explicit-block-scoped variants are parked. The discourse default is enough for everyday and most formal use; tighter scoping rules can be designed later if they turn out to be needed (likely for nested `def`s in formal proofs).
- Shadowing: a second `def` on the same `var <name>` replaces the prior binding. Listeners should hear the new binding as the live one.

Interaction with already-locked machinery:
- `def` + `ke`-clauses: a `def` statement can appear before a complex sentence to make the sentence shorter. The bound name is used inside the sentence's clauses. This is exactly the use case named-binding was introduced for (decisions.md: "compositional clarity of long expressions").
- `def` + reasoning particles: `def var p [some-premise]. dat var p. ...` — premise-marking on a bound name works the same as on any other proposition.
- `def` + quantifiers: `def var s [tot X mem Y]. erg var s imp [conclusion]` — bind a complex quantified statement, then reason about it.

### What this unblocks
- Formal expressions and proofs: `def` is the missing piece for clean expression of named entities in long arguments.
- Templates / examples: `var` lets us write instructions with unfilled slots.
- The variable-vs-literal distinction (`var x` vs `lit x fin`) is now fully expressible, closing the TODO.md "literal vs variable" question.
- examples.md validation no longer blocked on these — every sentence type previously requiring named-binding can now be written.

### Parked
- Sentence-local vs discourse-local scope for `def`. Currently discourse-local by default. May need formal scoping rules for nested proofs; revisit only if examples.md exposes a need.
- Multi-name binding: "Let X = ..., Y = ..." — can either chain `def`s or use a coordinator. Specifics not locked.
- `def` interaction with `kun`/`vel` (binding inside a coordinated chain) — defer until concrete examples surface a problem.

## 2026-05-16 — Prosody rules, verb shape confirmed

Session N+2 housekeeping. Closed three small items.

### Prosody (tasks.md items 7, 8)

Question opened: how does the listener disambiguate CV-vs-CVC overlap in connected speech? E.g. digit `sa` (6) followed by a consonant-initial word vs operator `sam` (=) followed by a vowel-initial word.

Three approaches considered:
- (a) Vowel-length distinction (CV digits long, CVC short). Phonetically tone-adjacent, conflicts with Lexor's non-tonal commitment.
- (b) Mandatory acoustic break at word boundaries. Simple, additive, matches what fluent speakers of any language already do.
- (c) Stress-and-timing convention with no explicit break. Risks under-specification.

Picked **(b)**. Every word is its own prosodic unit; word boundaries are obligatorily marked by a brief acoustic break (≈50–100 ms pause or light glottal closure). Inside a digit stream, digits concatenate without internal breaks — the stream is one prosodic unit. The break is the *single* disambiguator: a speaker who runs words together creates parse failures, and the listener can ask for repetition.

Three-level prosodic hierarchy locked:
- **Word boundary** — brief break (≈50–100 ms), no pitch reset.
- **Clause boundary** (written comma) — longer pause (≈200–300 ms) + slight pitch reset. Separates main from subordinate, hosts from tag-questions, and clauses joined by `kun`/`vel`.
- **Sentence boundary** (written period) — full pause (≈500+ ms) + complete pitch reset.

Stress is fixed on the first syllable of each word; non-lexical (never distinguishes minimal pairs); available as a focus overlay (heavier primary stress) without changing meaning. Focus is pragmatic, not scope-resolving — scope is pinned by positional rules per the precision-by-default principle.

Tradeoffs accepted: speakers must respect word boundaries audibly. Rapid colloquial speech that elides boundaries is technically ill-formed (similar to dropping word-spaces in writing). Lexor prioritizes parsing reliability over speed.

Rules written to phonetics.md "Prosody" section.

### Verb shape (tasks.md item 19, roots.md:40)

Question opened: confirm the CVC-root + V-tense shape that has been used throughout decisions but was still flagged TODO in roots.md.

Locked: verb = CVC root + V (tense vowel). Infinitive is the bare CVC root with no trailing vowel. Continuous-aspect consonant `x` attaches after the tense vowel. All seven tense-vowel assignments (`a` atemporal, `e` present, `i` future, `o` past, `u` imperative, `y` conditional, `c` perfect) are already locked in decisions.md.

This wasn't a new decision, just a long-overdue cleanup of a stale TODO that had been resolved by prior rounds. roots.md updated to remove the TODO and inline the shape rule.

### What this unblocks
- examples.md can now be written without prosody being ambiguous.
- No remaining structural cleanups before validation.

### Parked
- Rhythmic-meter conventions for poetry/song (the stress-fixed-on-first-syllable rule makes Lexor naturally trochaic in feel; whether to make this rule explicit for verse is a separate design question).
- Whispered or fully-silent prosody (sign-language analog) — not in scope.

## 2026-05-16 — examples.md first pass (66 sentences)

Wrote the first validation pass: 66 worked translations grouped by feature (basic VOS, tense, role vowels, negation, quantifiers, numbers/time, questions, subordinate clauses, conditionals, coordination, reasoning, copula split, markers, bindings). Content roots not yet locked are written as bracket-placeholders so the exercise tests structure, not lexicon. Working-assumption roots (`pluv`, `bib`, `dik`, `kompo`, `apre`, `legu`) flagged.

The exercise is its own argument: the grammar held up. No structural rule broke; the precision-by-default principle was visibly load-bearing several times (every example has exactly one parse).

Gaps surfaced and recorded in examples.md "Observations" section:
1. `tep ant pa dim` ("yesterday") is correct but heavy. May reopen the relative-time-root question during vocab buildout.
2. Major content vocabulary (drink, water, door, key, apple, person, house, fix, hammer, read, function) is missing. Next major work item.
3. Complement-clause placement (`dike e ke loma u`) reads naturally.
4. `lit … fin` is heavy when embedded inside an identity copula; quoted speech with a speech-verb is lighter.
5. `def`-bindings inside reasoning chains (example 66) demonstrate the most powerful use of named binding: long premises become single tokens.
6. Prosody rules parse every example uniquely. No collisions.

These observations are *findings*, not new design decisions. They feed the vocabulary arc (Session N+3+) and may reopen one or two parked questions if the load becomes annoying in practice.

### What this unblocks
- Vocabulary buildout: the structural framework is validated, so root assignment can proceed without fear of structural re-design.
- Concrete examples now exist for the README / future tutorial.
- Future design rounds can quote example numbers when discussing edge cases.

### Parked / followups
- Second pass of examples.md after the first wave of vocabulary lands (spatial prepositions, common nouns).
- A long-paragraph example (3–5 connected sentences) demonstrating discourse flow.
- Examples for proof-structuring particles ("suppose for contradiction", QED) once those are designed.

## 2026-05-16 — Spatial-preposition family, rotation names

Session N+3 first wave. Two related items locked: the full spatial-preposition closed class (extending the previously-locked `lok`) and the names of X/Y/Z rotations (resolved compositionally, no new roots beyond a verb `rot`).

### Spatial prepositions (twelve-root closed class)

Question opened: what is the full spatial-preposition family that complements `lok` (at/in/on)? Needed for examples like "under the table", "behind the door", "between two trees". Previously parked.

Approach: pick a small primitive set (~10–12) covering the canonical spatial relations; let everything else compose. Same strategy as the time prepositions (`tep`, `pen`, `sin`, `lim`, `ant`, `pos`).

Locked roots and rationale:

- **`sub`** — under / below. Latin *sub*. Cross-linguistic transparency (Spanish, English compounds like subway, subterranean).
- **`sur`** — over / above. French/Latin *super* / *sur*. Strong recognizability. Note: `sup` was already taken (supply/give verb), so `sur` is the spatial choice. Acceptable: the etymological family is the same and the surface is cleaner.
- **`pok`** — near / close-to. From Latin *proximus*. CVC; the alternatives `prok` (CCVC) and `pro` (CV, conflicts with prefix slot) were rejected on phonotactic grounds.
- **`lat`** — beside / at-the-side. Latin *latus* (side). Survives in English lateral, bilateral.
- **`dor`** — behind / at-the-back. Latin *dorsum* (back). Survives in English dorsal. Chosen over `pos` (time-only, locked) and `ter` (risks collision with future "earth/terra"). Mnemonic is a slight stretch for non-anatomy speakers but the alternatives were worse.
- **`fas`** — in-front-of. Latin *facies* (face). Survives in English face, façade. The X axis (forward direction) is conceptually the same direction; the spatial preposition and the axis-name share the root (see rotation-names section below).
- **`int`** — between. Latin *inter*. Binary by default ("between A and B"); for n-way "among", compose with quantifier (`int tot X` = "among all X"). Phonotactically VCC; legal per the established exceptions (`est`, `sta` are also unusual shapes).
- **`kir`** — around / surrounding. Greek *kyklos* / Latin *circa*. Mnemonic: English circle, cycle.
- **`dir`** — toward (goal direction). Latin *directio*. Distinct from `tep` (point in time at goal) and `lok` (point in space). `dir` is the *motion-toward* preposition.
- **`oks`** — from / out-of (source direction). Latin *ex*. Phonotactically CVC; `eks` (VCC) was the alternative but `oks` reads cleaner and avoids a vowel-initial shape collision with role vowels.
- **`tra`** — through. Latin *trans*. Phonotactically CCV — legal but unusual; chosen because the cross-linguistic recognition is too strong to pass up.
- **`lok`** — at/in/on (previously locked, 2026-05-15).

Compositions handle the rest:
- **inside / interior**: `lok int` ("at-the-inside") or just `lok` when interior is contextually obvious.
- **outside**: `oks` ("from-outside", in motion sense) or `nolok int` (negation, in stative sense).
- **across**: `tra` reused, or compose with `lat` for the lateral sense ("across the road" = `tra` + road).
- **against (touching)**: compose `pok` + contact context, or rely on a future "touch" verb root.
- **along**: compose `tra` + path axis, or rely on a future "path/line" root.
- **away from**: `oks` covers this in motion contexts; for stative "far from" use `nopok`.

Tradeoffs accepted:
- Some prepositions take CCV / VCC shapes (`tra`, `int`, `oks`). Lexor already has these exceptions; the closed-class slot can tolerate non-CVC shapes when the root has high cross-linguistic recognizability.
- "in front of" and "before (time)" don't share a root (`fas` vs `ant`); same for "behind" vs "after" (`dor` vs `pos`). English/Spanish overload these (front/before, behind/after) but the spatial-vs-temporal distinction is real and worth marking — eliminates the "before the door" ambiguity (= in space, in front of) vs "before the meeting" (= in time, prior to).

Examples (added compositionally to examples.md if useful in a future pass):
- `loma sub [tree] e` — "She eats under the tree."
- `golo dor [door] e` — "She went behind the door."
- `viv int [montañas] lo` — "They live between the mountains."
- `kompo [auto] e dir [city]` — "She drove the car toward the city." (Note: `kompo` is a working-assumption verb; will refine.)
- `ven oks [house] e` — "She came from the house."
- `gol tra [forest] e` — "She went through the forest."

### Rotation names (X/Y/Z) — compositional, no new roots

Question opened: how to name the X, Y, Z rotations (decisions.md item from 2026-05-15 marked TODO three times). The user's framing: names must be obvious, no need to actively memorize (unlike yaw/pitch/roll/aft/starboard/port/camber/caster/toe).

Coordinate frame already locked: X forward, Y left, Z up; right-handed; positive horizontal rotation toward the left.

Approach: name rotations by the spatial-preposition root for the axis they rotate about. Composes with a generic rotation verb `rot`.

Locked:
- **`rot`** — verb root, "rotate". Latin *rotare*. CVC. No collision with existing roots.
- **`rot fas`** — rotation about the X (forward) axis. English equivalent: roll.
- **`rot lat`** — rotation about the Y (lateral / left) axis. English equivalent: pitch.
- **`rot sur`** — rotation about the Z (vertical / up) axis. English equivalent: yaw.

Rationale for compositional vs dedicated roots:
- Dedicated roots (`rol`, `pit`, `yaw` or analogous) would save one syllable per use but require three new memorizations and aren't transparent to anyone without aerospace/animation background.
- Compositional form (`rot` + axis-direction) is self-explanatory the moment you know the spatial-preposition family and the coordinate frame. Speakers don't need to memorize three additional mappings.
- Matches Lexor's pattern: no dedicated roots when composition works (subset, existence, "what/who/when/where/why/how" are all compositional).

Sign convention (positive rotation):
- `rot sur` positive = turning left (matches user's "positive horizontal rotation toward the left").
- `rot lat` positive = ... TBD on convention; defer to physics arc.
- `rot fas` positive = ... TBD on convention; defer to physics arc.

The exact sign convention for pitch and roll is parked — it's a separate question from the *naming* one and depends on whether Lexor wants to standardize physics conventions universally or allow context (aerospace vs robotics vs animation use different signs).

### What this unblocks
- Spatial sentences for examples.md (second pass).
- The "where/when" distinction can now be fully expressed for all spatial relations, not just `lok` (at).
- Rotation terminology no longer needs a placeholder; existing vocabulary suffices.

### Parked
- Pitch/roll sign conventions.
- "Inside / outside" potentially needing dedicated roots if the `lok int` / `oks` compositions feel heavy in practice — defer until examples surface a problem.
- "Along", "against (contact)", "across (perpendicular sense)" — defer to vocabulary buildout when their use-cases concretize.
- Diagonal / oblique spatial relations — out of scope for the core 12.

---

## 2026-05-16 — Machine-readable lexicon and collision-checker

### What was decided
- `lexicon.yaml` becomes the source of truth for all locked roots. Schema is self-documenting (header comment in the file). All 130 currently-locked roots seeded: 11 pronouns, 12 digits, 11 markers, 2 coordinators, 15 quantifiers (incl. comparison/base/scale operators), 3 non-identity copulas, 20 prepositions, 8 time-unit roots, 48 verb roots.
- `scripts/check_collisions.py` runs over the YAML. Detects duplicate root forms (whitelisting only `sam`, which is one concept used in two syntactic contexts) and shape violations. Shape rule enforced strictly only on open-class kinds (`verb`, `noun`, `adj`); closed-class kinds (markers, prepositions, etc.) are allowed to keep their hand-chosen non-CVC forms (`est`, `ant`, `imp`, `is`, etc.) because those were deliberately picked for source-language recognizability and are locked in decisions.md.

### Tree-structure decision
The user suggested encoding the whole vocabulary as a tree. Considered:
- (a) Full WordNet-style semantic ontology upfront — rejected. Pre-designing every internal node is a classic conlang deathtrap; months of taxonomy work before any vocabulary lands.
- (b) Lightweight emergent tree — accepted. Each entry carries an optional `semantic_parent` field with a gloss; internal nodes only get created when at least one leaf points to them. Traversal still works (find all entries with `semantic_parent: motion`, etc.). Cost is bounded; the tree grows organically with the vocabulary.
- (c) Phonological tree (index by CVC slot) — folded into the collision-checker, no separate file needed.
- (d) Etymological / derivational trees — derivable on demand from existing fields.

### Why YAML, why at the repo root
- YAML over JSON for human edit-ability (comments allowed, less ceremony).
- Repo root (not `data/`) for visibility — there are only a handful of top-level files; nesting it would just hide it.
- Single file (not one-per-category) because the total stays well under 10K entries even at full buildout, and a single file is grep-friendly and atomic to read.

### Collision-checker finding: verb-root phoneme conformance
Running the checker surfaced 7 inherited verb roots that violate the strict CVC verb-shape rule:
- `cad`, `cri`, `cur`, `cla`, `duc` — use `c` as if it were /k/, but per phonetics.md `c` is exclusively the vowel /æ/. So `cad` is phonetically /kæd/? No — it's /æad/, which has 3 consecutive vowels including the implicit "a" — illegal.
- `apr`, `aud` — start with a vowel, shape VCC or VVC, not CVC.

These were inherited from a draft of roots.md that predates the strict CVC + phoneme-table locks. Two fix paths (parked as a `tasks.md` item, not resolved here):
1. Rename to fit CVC + the phoneme table: `cad→kad`, `cri→kri`, `cur→kur`, `cla→kla`, `duc→duk` (but `k`-final is forbidden by phonetics.md rule 1, so `duc→tir` or similar), `apr→pri` or rename, `aud→` rename to a sense-of-hearing CVC.
2. Grant an explicit exception clause in decisions.md allowing inherited verb roots to keep non-conformant shapes. Discouraged — would weaken the rule that should drive future vocabulary.

Path 1 is preferred but each rename is its own micro-decision and should run through the standard "lay out options, pick, log rationale" flow. Parked.

### What this unblocks
- Bulk vocabulary adds: every new root gets entered in `lexicon.yaml` and `python3 scripts/check_collisions.py` is run before committing. Collisions are caught structurally instead of through manual search.
- Frequency-list driven assignment: once `frequencies.yaml` is built, the assignment loop is "take next-highest-frequency concept, propose CVC root, run checker, commit on green."
- Auto-generated `dictionary.md` from the YAML — straightforward script, parked under repo-restructuring tasks.

### Parked
- Frequency-list construction (`frequencies.yaml`): merged top-N from English (SUBTLEX-US), Spanish (SUBTLEX-ESP), Latin (Diederich's basic Latin list), deduped by concept. To be built next.
- Verb-root rename audit (the 7 findings above).
- `dictionary.md` auto-generation script.

---

## 2026-05-16 — Verb-root rename pass: phoneme conformance

### What was decided
Resolved the 7 verb-shape warnings surfaced by the collision-checker. All renames preserve source-language recognizability where possible; switched source language only when the original cluster wouldn't fit CVC:

| Old  | New  | Source                                    | Notes |
|------|------|-------------------------------------------|-------|
| `cad`| `kad`| Latin *cadere*                            | Direct phoneme rewrite. |
| `cur`| `kur`| Latin *currere*                           | Direct phoneme rewrite. Now overlaps with `ked` (run); split sense: `kur` = continuous flow, `ked` = locomotive. |
| `cri`| `lor`| Spanish *llorar* / Latin *plorare*        | Cluster reduction (drop initial /pl/ or /j/). Sense narrowed to tearful crying; loud-shouting/scream sense parked for a future root. |
| `cla`| `xut`| English *shut* (x=/ʃ/)                    | Switched source language because Latin *claudere*'s /kl/ cluster can't fit CVC. |
| `duc`| `tir`| Spanish/Italian *tirar*/*tirare*          | Latin *ducere* failed two ways: `duc` has `c`=vowel; `duk` violates /k/-final rule. Romance "tir-" is widely cognate (Spanish, Italian, also French *tirer*). |
| `apr`| `per`| Latin *a-PER-ire* stem                    | Dropped leading vowel; PER stem preserved. |
| `aud`| `lis`| English *listen*                          | Latin *audire* (VVC) doesn't fit CVC. Candidate `her` (English hear) blocked by phonetics rule 6 (h+vowel forbidden). |

### Alternatives considered and rejected
- **`cad → kad` vs preserving `cad` with an exception clause.** Rejected the exception: would weaken the strict-CVC rule that should drive all future open-class roots, and the rewrite costs nothing.
- **`cri → lam` (Latin *clamare* cluster-reduced) vs `lor`.** Picked `lor` because *llorar* is the everyday Spanish word for crying, while *clamare* is closer to "exclaim/proclaim" — slightly different sense. Reserved `lam` for a potential future "shout/proclaim" root.
- **`cla → klu`/`klud`** rejected for CC cluster; **`cla → ser`** rejected (collides with verb `ser` = serve). **`cla → ker`** rejected because of weak mnemonic and to keep `k`+vowel for the `kad`/`kur` pair.
- **`duc → dut` or `dug`** rejected for arbitrary phoneme swap with no mnemonic; **`tir`** chosen for cross-Romance recognizability.
- **`apr → bri`** (Spanish *abrir* cluster-reduced) rejected because `per` traces back to a more widely-cognate Latin stem (*aperire* → English *aperture*, French *ouvrir* from *operire*).
- **`aud → her`** (English *hear*) rejected at the phonetics check — rule 6.
- **`aud → kut`** (Latin *auscultare* middle syllable) rejected for weak mnemonic.

### Propagation
Updated everywhere `cad/cri/cur/cla/duc/apr/aud` appeared:
- `lexicon.yaml` — 7 entries renamed, original spelling preserved in `notes`.
- `roots.md` — verb table updated.
- `examples.md` — `apre` → `pere` (only inflected form in use).
- `frequencies.yaml` — `assigned_root` fields for "hear" and "fall" updated.
- `tasks.md` — audit task ticked.

### Sense-split surfaced as a side effect
- **`kur` vs `ked`** — both glossed "run" before, but now `kur` (from *currere*, primary sense = continuous flow) and `ked` (already in lexicon as "run", working English-stem mnemonic) overlap. Decided to split: `kur` = liquid/continuous flow, `ked` = locomotive running. Logged in both `notes` fields. May need a third root if "running of an engine / running of an event" gets crowded; defer.
- **`lor` vs the parked future "shout/proclaim" root** — `lor` covers tearful crying; loud emotional shouting is a separate concept and gets its own root later (candidate slot: `lam` reserved).

### Parked
- Future root for "shout/proclaim" (candidate slot `lam` from *clamare*).
- Possible third "run" root if `kur`/`ked` split feels insufficient under more examples.

---

## 2026-05-16 — Sub-constituent grouping markers `bra … ket`

### Problem
Working through the "I bet I can do between three and four hundred pushups" example surfaced a gap: Lexor's locked prosody (word / clause / sentence boundaries) only structures clause-level and above. There was no general mechanism for sub-clause constituent grouping inside a single clause. The digit-stream auto-fuse rule actively fights such cases: `tom re ko zo zo` parses as `tom rekozozo` (one fused number = 3400), so `tom`'s second argument is missing entirely — ill-formed, but the speaker had no good shape to produce. Mixed AND/OR (examples.md #48) hits the same family of gap; the current answer is `def`-binding, which is heavy for short phrases.

### Options considered
- (A) Paired grouping brackets (parenthesis-style closed-class markers). Two short words: one opens, one closes. Parser treats the bracketed span as a single argument unit.
- (B) Fourth prosodic level (~150 ms sub-constituent pause, between word-break and clause-break).
- (C) Single closed-class separator word, no closer.

### Why (A) won
- **General.** Handles numerical ranges, mixed AND/OR, future nested operators of any shape. (B) and (C) only address some.
- **No prosodic load.** (B) would push the prosodic-distinction count to 4 levels, near the perceptual reliability limit per Lehiste 1973 / Price et al. 1991. Listeners under noise/fatigue/cross-dialect would lose distinctions.
- **Consistent with the locked "scope by explicit markers, not by prosody" rule.** (B) directly contradicts it.
- **Composable with `lit … fin`.** Lexor already has one paired-marker pattern; reusing the shape is familiar.
- **Nesting comes free.** Each `ket` matches the nearest unmatched `bra`, like every paren-based language.
- (C) collapses into (A) as soon as nesting is needed — you still need a closer. So (A) generalizes (C).

### Tonality side-question
User asked: could tonality make the brackets unnecessary in speech? Honest answer documented in the response: prosody *can* cue grouping (every natural language uses intonational phrasing for it), but formally licensing prosody as a substitute breaks two locked invariants: (1) "scope is pinned by positional rules, not prosody"; (2) precision-by-default fails under noise/speed/cross-dialect. Resolution: brackets are mandatory; prosody is a secondary cue that aligns with them. Keeping the brackets short (one syllable each) makes the cost of saying them low enough that "trusting prosody instead" doesn't save much.

### Surface forms
- `bra` (CCV, closed-class shape exception fine per the established rule for non-CVC closed-class entries).
- `ket` (CVC).
- Mnemonic: English "bracket" split. `bra` opens, `ket` closes.
- Checked against lexicon: no collisions. `ket` distinct from `ke` (universal complementizer) and `kex` (frequency operator) under the obligatory ~50–100 ms word-boundary break.

### Alternatives rejected
- `kop / kof` — abstract phonological mirror, no mnemonic.
- `bok / kob` — clean CVC but weak mnemonic.
- `pa / ap` — `pa` collides with digit 1.
- `gru / urg` — weak mnemonic, two cluster shapes.
- `tag / gat` — weak mnemonic.

### What this unblocks
- `tom`-range expressions on heterogeneous-digit numbers: `tom bra re ket bra ko zo zo ket` cleanly = "between 3 and 400."
- Mixed AND/OR without `def`: `bra A kun B ket vel C` = "(A and B) or C." `def`-binding goes back to its real job (naming an expression for reuse), no longer load-bearing for disambiguation.
- Future operators that take 2+ arguments where digit-stream or constituent-fuse rules would otherwise eat the boundary.
- Cleaner factoring: examples.md #48 updated; the principle that `def` is for naming, brackets are for grouping, is now visible at the syntax level.

### Parked
- Whether to add a third prosodic-level reinforcement (a ~150 ms tighter phrase inside brackets) as a *style* recommendation, not a grammatical requirement. Probably yes, but document later under "spoken-style guide" rather than `phonetics.md` proper.
- Multi-character/Unicode written form for the brackets (parentheses `( )`, square `[ ]`, angle `⟨ ⟩`). Defer until a written-form section is written.

---

## 2026-05-16 — `trials.md` consolidates checklist + pain into a test suite

### What was decided
`checklist.md` removed. Its content (and the pain.md trap inventory) restructured into `trials.md` as a tagged test suite. Each entry has the shape:
- `### Name [tag, status]`
- one-line setup (English problem or capability target)
- Lexor rendering when one exists
- `How:` pointer to the decision that disarms it (for `passes`) or `Status:` pointer to tasks.md (for `open`)

Tags: `[trap]` (known natural-language ambiguity), `[feature]` (required capability), `[stretch]` (ambitious case), `[stress]` (open-question probe). Status: `passes` / `open` / `parked`. Grep `\[.*, open\]` returns every unmet design goal.

### Why one file, not two
Original sketch had a separate `regressions.md` paired with pain.md. User pushed back ("regressions.md is too specific... I want more ambitious tests"), then observed that `checklist.md` is already half-trial: half of its entries were concrete English sentences ("password K and L," "taper ratio," "1080p vs 1km"). The right move was merge, not multiply. One file is now both the wishlist (what should be possible) and the validation (each case worked or marked open). Drift between feature spec and trial coverage is structurally eliminated because they're the same artifact.

### Initial inventory
61 entries seeded:
- 18 [trap, passes] — natural-language ambiguities Lexor has formally disarmed.
- 15 [feature, passes] — required capabilities the design meets.
- 12 [feature, open] — capabilities still needing decisions (anti-adjective, evidentiality, direction-sense, neutral axis names, % bare ratio, eyeballed marker, probability operator, distribution shapes, unspecified-addressee, taper-ratio neutralization, direction-vs-location).
- 6 [stretch, open] — ambitious cases waiting on vocabulary or modal operators.
- 3 [trap, open] — traps with no mechanism yet (mean-sea-level modifier attachment, not(a=b) modal, masses-can-be-different modal).
- 4 [stress, open] — probes of open design questions (deep nesting, long digit streams, mixed bases, ambiguity-by-omission).
- 2 [stretch, passes] — pronoun-less paragraph, long mathematical statement (mechanism passes, full text not yet written).
- 1 [stretch, partly-passes] — quantum superposition (waits on modal operators).

### What this unblocks
- Auditing the language design empirically: `grep '\[.*, open\]' trials.md` lists every design gap with a concrete trial that motivates closing it.
- Each new decision can be linked back to the trial(s) it closes — the trial is the regression test, the decision is the fix.
- Future trap discoveries get tagged `[trap, open]` immediately, becoming a queue for design rounds.

### Parked
- TODO.md vs tasks.md merge (separate concern from checklist removal).
- A script that auto-checks every `[*, passes]` trial against the decision/lexicon it cites (catches drift if a decision changes).

---

## 2026-05-16 — Epistemic modal operators `kan` / `mus`

### Why this round
User handed design autonomy. Highest-leverage open trial cluster on the inventory: modal modality, with 3 open trials (B1 "not(a=b)", B2 "masses can be different", I2 quantum superposition) and one open feature (D6 plug-in probability) all blocked on the same missing infrastructure. One decision round closes three trials and clears the path for the fourth.

Alternative clusters considered:
- **Direction family** (G3/G4/G5: sentido, direction vs location, neutral axis names) — 3 trials, but interlocking; needs ~2-3 design rounds to settle.
- **Evidentiality** (H4) — 1 trial, would add a new suffix-level system; bigger structural commitment.
- **Probability/distribution** (D5/D6) — downstream of modals; can't lock cleanly without them.
- **Bulk vocab from frequencies.yaml** — broad but flat. Doesn't unlock any structurally-new sentence.

Modals win clearly: deepest hole, three trials closed at once, foundation for the probability work that comes next.

### What was decided
Two closed-class markers:
- `kan` — epistemic possibility (◇). "X may be / can be / is possibly the case."
- `mus` — epistemic necessity (□). "X must be / is necessarily the case."

Both sentence-initial, scoping over the remainder of the clause. Inside a `ke`-clause: `ke kan pluve` = "that it might rain."

Compose with `no` for the four corner readings:
- `kan X` = ◇X (possible X)
- `mus X` = □X (necessary X)
- `no mus X` = ¬□X (not necessarily X) — the "doesn't have to" reading
- `no kan X` = ¬◇X (impossible X) — same as `mus no X` (always-not-X), with which it is logically equivalent.

### Alternatives considered and rejected
- **Only one primitive + composition** (lock only `kan`, derive `mus` as `no kan no`). Rejected: forces "not possibly not" every time someone wants "must." Cognitive friction, same anti-pattern as English's mandatory tense. Cost is one extra closed-class root — trivial.
- **Modal-as-quantifier** (treat possibility as ∃ over possible-worlds, necessity as ∀). Linguistically valid (standard Kripke semantics) but would require explicit "world" arguments. Reject for surface simplicity — keep the modal as a marker that scopes over a proposition.
- **Modal-as-suffix** on the verb (like tense vowels). Rejected: modal scope is the whole proposition, not just the verb's temporal frame. Marker shape is correct.
- **Epistemic + deontic both in this round** (e.g., `kan` epistemic + `let` deontic-permission + `mus` epistemic-necessity + `obg` deontic-obligation). Rejected: no current trial requires deontic; YAGNI. Park.
- **Alethic vs epistemic split** (logical necessity vs known necessity, e.g., `2+2=4` is alethically necessary, while "the sun will rise tomorrow" is epistemically near-certain). Real philosophical distinction. Rejected for now — locks the unified epistemic flavor first; refine if a trial exposes a case that needs alethic-specifically.

### Surface-form alternatives considered
- `kan` vs `pos` for possibility — `pos` is taken (after-in-time preposition).
- `kan` vs `pot` — `pot` is taken (verb: create/make). Also semantically weaker mnemonic for possibility.
- `mus` vs `dev` (from Spanish *deber*) for necessity — `dev` would carry an obligation flavor (deontic) more than necessity (epistemic); chose `mus` to keep the marker firmly in the epistemic territory.
- `mus` vs `nec` — `c` is the vowel /æ/ per phonetics.md; `nec` would be VCC and shape-violate; `nek` doesn't have the same Latin mnemonic strength.
- Both `kan` and `mus` checked against lexicon: no collisions.

### Position rule rationale
Sentence-initial position chosen for consistency with the existing sentence-level operator family: `is` (conditional), `dat` (premise), `erg` (therefore). All scope-over-clause operators sit at the head. This is the operator-family invariant.

Alternative considered: modal-as-trailing-suffix on the verb (like Turkish/Japanese). Rejected because (a) inconsistent with the rest of the operator family, (b) puts the scope-defining word at the *end* of the proposition, requiring listeners to revise their parse retroactively — exactly the "negation processing leak" failure mode that motivated negation-as-prefix.

### Trials closed
- B1 "not(a=b) vs a≠b" — passes via `no mus sam a b` / `kan no sam a b`.
- B2 "masses can be different" — passes via `kan no sam m1 m2`.
- I2 quantum superposition — passes via `kan lok-x i kun kan lok-y i kun no mes`.

### Trials clarified but not closed
- D6 plug-in numerical probability — path is now `kan pir [number]` or `[number] dem kan X`, but the specific shape is parked for a follow-up round. The infrastructure exists; the API is pending.

### Parked
- **Deontic modality**: `let` (permission) / `obg` (obligation) — surface forms tentative; lock when a trial requires them.
- **Alethic modality**: split from epistemic if a logical/metaphysical trial exposes the need.
- **Probability operator surface form**: D6 stays open; the modal infrastructure is necessary but not sufficient. Needs a separate round to pick the syntax.
- **Counterfactual conditionals**: "If she had eaten, she would not be hungry now" — distinct from the locked `is` (real conditional) and `imp` (formal implication). Parked, no trial yet.

---

## 2026-05-16 — Axis system (G3/G4/G5 closures)

### Why this round
User handed design autonomy again after the modal-operators round. Direction family was the highest-leverage remaining cluster on the trials inventory: G3 (sentido), G4 (direction vs location), G5 (neutral axis names) all blocked on the same missing structural concept — a way to talk about *axes themselves* (as abstract directed lines) independent of relational location.

### Conceptual factoring
English collapses these four distinct concepts:
1. **An axis** — a 1D directed line through space (Z axis, longest axis).
2. **A direction** — axis + polarity ("upward," "leftward").
3. **An endpoint / extremum** — the extreme point at one end of an axis ("top of the box").
4. **A magnitude** — the length of an object along an axis ("height").

"Up" in English drifts between (2) and (3). "Top" hides (3) and a relational reading. "Height" is (4) but assumes vertical-orientation. Lexor needs distinct surface shapes for all four.

### What was decided
Three closed-class composable roots:
- `aks` — axis. Composes with spatial preposition for agent-frame axis (`aks fas` X, `aks lat` Y, `aks sur` Z) or with digit for object-frame rank (`aks pa` longest, `aks du` middle, `aks re` shortest).
- `tip` — endpoint / extremum. `tip aks <ax> <pol>` gives the extreme point in that direction along an axis.
- `mez` — dimensional magnitude. `mez aks <ax>` gives the length-along-that-axis as a number.

Polarity reuses the existing comparison operators `mag` (+) / `min` (−). No new polarity root needed.

Agent-frame axes reuse spatial prepositions `fas`/`lat`/`sur` — same as the locked rotation names `rot fas/lat/sur` (2026-05-16). No new axis roots needed; the structural cue ("preposition after `aks`") generalizes the existing pattern.

### Surface forms
- `aks` — VCC. Closed-class shape OK. Mnemonic: English/Latin *axis*.
- `tip` — CVC. Mnemonic: English *tip* (end of anything).
- `mez` — CVC. Mnemonic: Spanish/Latin *medir/metiri* (to measure).

Initial proposal had `pek` for endpoint, but caught by the phonetics check: `pek` ends in /k/, which phonetics.md rule 1 forbids. Swapped to `tip` — better mnemonic anyway (general "endpoint" rather than vertical-biased "peak").

All three checked against lexicon: no collisions.

### Alternatives considered and rejected
- **Single direction roots, no `aks`** (use `fas mag` for forward, `sur min` for downward, etc.) — rejected: collides with the relational reading of spatial prepositions. `sur X` already means "above X"; adding `sur mag` as a separate noun-phrase reading creates ambiguity.
- **Vowel-encoded polarity on the preposition** (`fas-e` forward, `fas-o` backward) — rejected: clashes with the existing role-vowel suffix system.
- **Compose with `dir` (toward)** to derive directions (`dir fas` forward, `dir sub` downward) — rejected because the lateral (Y) axis lacks paired left/right prepositions; the system would have a gap.
- **Drop `mez`, let `aks` carry magnitude by metonymy** (like English "length" doubles as direction + magnitude) — rejected: violates precision-by-default. An axis (geometric) and its length (numeric) are different types; the type-coercion would be ambiguous in unobvious cases.
- **Drop `aks`, just use `tip` and `mez` over prepositions directly** — rejected: same relational-vs-axis ambiguity as the first alternative.
- **Use `lon`/`med`/`kor` (long/middle/short) for object-frame ranks** — rejected in favor of digit reuse. `aks pa/du/re` falls out of the existing digit system, no new roots, and matches the "longest is rank 1" convention.
- **`pek` for endpoint** — rejected at phonetics check (/k/-final). Replaced by `tip`.

### Closes
- **G3 sentido** — `aks fas mag` (forward) vs `aks fas min` (backward). Same axis root, polarity distinguishes.
- **G4 direction vs location** — `aks sur mag` (direction) vs `tip aks sur mag bra X ket` (location at X's top) vs `sur X` (relational, somewhere above). Three structurally distinct shapes.
- **G5 neutral axis names** — `aks pa/du/re` for object-frame ranks; `mez aks pa` for "longest dimension." Orientation-free.

### What this unblocks
- Coordinate-system expressions for navigation and physics.
- "Height of an object lying on its side" without contradiction.
- "Sentido del tráfico" cleanly expressible (`aks fas mag/min` over the traffic compound).
- Geometric / engineering vocabulary that needs axis-talk: vectors, gradients, slopes.

### Parked
- **Compass directions** (N, S, E, W) — need dedicated roots or compositional from an Earth-frame system. Punt.
- **Gravity-as-axis vs Z-axis** — sometimes "up" means "against gravity" (frame-of-reference matters in vehicles, spacecraft). Defer until a trial exposes the need.
- **Direction from `dir` (toward)** as a verb — current `dir` is a preposition (toward); could derive a verbal "head toward" form, but parked.
- **"Width" specifically** as opposed to "the Y dimension" — English has cultural overlay on width (often shorter horizontal). Not modeled; speakers use object-rank or agent-Y as appropriate.
- **Negative magnitudes** — `mez` produces a non-negative number. Signed magnitudes (like in physics displacement) compose with `mag`/`min` on top. Convention parked.

---

## 2026-05-16 — Angle convention

### What was decided
Angles expressed as fractions of a full revolution; no dedicated angle unit, no new roots. Sign by right-handed convention around the named axis. Reference direction (for starting "where") = agent's +X (forward), per the locked coord system (X forward, Y left, Z up). Verb form `rot <amount> aks <ax>`; noun form `rota <amount> aks <ax>` using the atemporal derivation.

### Why no new roots
The existing infrastructure carries the load:
- `rot` (verb root: rotate) — derivation gives `rota` for the noun "rotation/angle."
- `aks <ax>` — names the rotation axis.
- digit-stream + `dem`/`doz` — gives any numeric magnitude in any base.
- `min`/`mag` — sign on the magnitude.

Adding a unit root (like `rev` or `tur`) was considered and rejected: the number IS the unit count, by convention. Same principle as Lexor not having "second/minute/hour" suffixed to numbers — the type-context tells you what the number measures.

### Why fractions of a revolution (not degrees, not radians)
- Degrees (1/360) are arbitrary (Babylonian sexagesimal artifact) and 360 is awkward in dozenal.
- Radians are mathematically nice but require π for any cardinal angle — speakers can't say "quarter turn" without invoking π/2.
- Revolutions are universal, intuitive, base-agnostic, and dozenal-friendly: 1/12 = `zo doz pa`, 1/4 = `zo doz re`, 1/2 = `zo doz sa`. Every cardinal angle has a finite expansion in dozenal.

### Sign convention rationale
Right-handed rotation around the named axis is the physics/math standard and matches the locked coord system. For everyday rotations around Z (looking down at a horizontal plane), positive = counterclockwise = "turning left" for an agent facing +X. The user's "9 o'clock = 0.25 revolutions" check passes: 9 o'clock (left side of a viewer-facing clock) = +Y = quarter turn counterclockwise from +X = +0.25 around +Z. ✓

The "3 o'clock" = right side is `-0.25` (or `+0.75`). The clock analogy is *flipped* relative to physics convention; speakers used to clocks will need to remember this. Documented; accepted.

### Reference direction
Locked: when the angle is given without a "from where" specifier, the implicit reference is the agent's +X (forward). This handles the "12 o'clock = 0" case naturally. Speakers wanting a different reference (e.g., compass north) must state it explicitly.

### Closes
- trials.md **G6 compact angle expression** [feature, passes].

### Parked
- Compass / geographic directions (N/S/E/W) — still need a separate convention if Earth-frame is ever required. Not blocking; defer.
- Solid angles (steradians) — 3D angular measure, parked. Same fraction-of-sphere convention would extend naturally.
- Spherical coordinates (longitude + latitude for a direction in 3D) — composable from two angle expressions, but the ergonomic shorthand is parked.
- Angular velocity / acceleration — composable from `rot` + temporal derivatives, but no specific syntax locked.

---

## 2026-05-16 — Graded probability `chan`

### Why this round
User: "be able to sprinkle probability markers on what we say easily ... for facts not amounts, we would still need the probability markers, which is different from a precision one in an amount." That's trial D6. The modal-operator round (`kan`/`mus`) handled binary modality; the missing piece was *graded* probability — attaching a specific number to a proposition's truth.

### What was decided
One new closed-class marker:
- `chan` — graded epistemic probability. Form: `chan <number> <proposition>`. Number in [0, 1].
- Sentence-initial, matching the position rule of other modal/discourse operators (`kan`, `mus`, `is`, `dat`, `erg`).

Mnemonic: English/French/Spanish *chance* (`ch` = /tʃ/ in Lexor phonetics). The word "chance" carries the probability meaning across Romance and Germanic, making it broadly recognizable.

### Why a new marker, not an extension of `kan`
Considered overloading `kan` to take an optional numeric argument: bare `kan X` = "possibly X (unspecified)"; `kan <num> X` = "X with probability <num>." Rejected because the parser disambiguation between "number-as-probability" and "proposition-starting-with-number" would require contextual interpretation — exactly the precision-by-default failure mode. With a dedicated marker, the grammar is clean: `chan` *requires* a numeric expression before the proposition; `kan`/`mus` *forbid* one.

### Why fraction in [0, 1], not percent / odds
- Percent (×100) carries cultural overhead and a built-in scale factor that's awkward in dozenal.
- Odds (X:Y form) need additional syntax for the ratio.
- Probability as a bare fraction is universal, base-agnostic, and composes with the existing digit-stream + base-marker system without anything new. `zo dem ne zo` = 0.90 decimal. `zo doz ne` = 0;9 dozenal = 9/12 ≈ 0.75 decimal.

### Why number-first, proposition-after
Matches the existing pattern of other operators that take a quantitative argument: `tom <a> <b>`, `sam <a> <b>`, `pir <num>`, `mag <num>`, `min <num>`. The argument comes before the operand. Reverse order (`chan <prop> <num>`) was considered for English-ergonomics ("the probability of rain is 0.9") but rejected for inconsistency.

### Why no fuzzy probability words ("likely", "unlikely", "very likely")
Rejected adding `lik` (likely), `lim` (unlikely — also collides with `lim` for "until"), or similar fuzzy magnitude words. Reasons:
- Violates precision-by-default. The whole point of `chan` is to make probability *explicit* and numeric.
- Speakers who want fuzziness can compose: `chan zo dem ne zo` ("0.9") = very likely; `chan zo dem pa` ("0.1") = unlikely; `chan mag zo dem fi` (">0.5") = more likely than not.
- Or fall back on the binary modals: `kan X` for "possible" (any positive probability), `mus X` for "certain."

### Surface form alternatives considered
- `chan` (chosen) — English/French/Spanish *chance*; pan-Romance and Germanic recognizability; clean CVC where `ch` is the /tʃ/ digraph.
- `prob` — Latin/English *probable*. CCVC shape (closed-class allows). Slightly longer; mnemonic OK but slightly more abstract.
- `pos` — taken (after-in-time preposition).
- `cer` — `c` is the vowel /æ/; `cer` would be VVC shape and weak mnemonic.
- `lik` — `k`-final forbidden by phonetics rule 1.

`chan` checked against lexicon: no collision. Distinct from `chi` (digit 7) by the prosodic word-boundary break.

### Closes
- trials.md **D6 plug-in probability** [feature, passes].

### What this unblocks
- Probabilistic reasoning chains: combining `dat`, `erg`, `imp`, `kan`, `mus`, `chan` in a single discourse for proof-grade hedged arguments.
- Conditional probability cleanly via `chan X dat Y` ("P(X|Y) = …").
- Bayes-style updates by stating prior, likelihood, and posterior as sequential `chan` sentences.
- Decision-theoretic talk: "expected value is X with probability Y" composes naturally.

### Parked
- **Probability distribution roots** (gaussian, uniform, bimodal, beta, etc.) — trial D5 still open. `chan` handles point-probabilities; distributions over a domain need more machinery. Defer until a trial concretizes the need.
- **Continuous probability densities** — same as above.
- **Fuzzy probability words** — rejected on principle; if a use case emerges that the composed forms can't handle, revisit.
- **Probabilistic versions of `dat`/`erg`** — for "given that with probability P" / "therefore with probability P." Composable but not formalized.
- **Frequentist vs Bayesian flavors** — Lexor's `chan` is interpretation-neutral; if a trial requires distinguishing "P(X) in the long run" from "my degree of belief in X," add then.

---

## 2026-05-16 — walkthrough.md readability pass

### Issues raised by the user (and observed)
The first draft of `walkthrough.md` had three concrete problems:

1. **Acronyms used without explanation on first use.** VOS, CVC, logic symbols (◇ □ ∀ ∃), 1D, coordinate notation (+Y / −Z), and P(X) / P(X|Y) all appeared without being defined. A learner reading top-to-bottom hits these and has to either guess or leave the document to look them up.

2. **General tone too terse / jargon-heavy.** The doc was structurally a walkthrough but read like reference material in places.

3. **Stacked-adjective phrases were genuinely hard to parse.** The user flagged "atemporal-frame inner vowel" as the canonical example: three words modifying "vowel," with "atemporal-frame" ambiguously parseable as either a hyphenated unit or "atemporal frame" (where frame is the noun), and "inner" feeling tacked on. The reader has to do parsing work that the writer should have done.

### Fix
Rewrote the entire file (411 → 549 lines, structure preserved). Specific changes:

- **Added a "What you need to know before Level 0" preface** that introduces word shapes (CV, CVC) and sentence order (VOS) once, with examples, before they're used. Every later reference can rely on this.
- **Replaced math/logic symbols with words** where they appeared in prose: ◇/□ → "might / must," ∀/∃ → "all / some" with parenthetical notes for readers who know the symbols. Where the symbol is genuinely useful (rare), it's introduced alongside the word.
- **Broke stacked adjectives into clear sentences.** "Atemporal-frame inner vowel" became "The vowel `a` ... means 'no specific time' — the default when a speaker doesn't want to commit to a time." Each level's gloss now uses short declarative sentences instead of noun-stack phrases.
- **Friendlier overall voice.** Each level starts with what the example means (the meaning, not the parts) before breaking down the structure. Lists use tables where comparison is easier. Removed implicit linguistics-trained-reader assumptions.
- **Coordinate notation written out.** "+Y direction" became "the positive Y direction" with a reminder that Y points to the speaker's left.
- **Probability notation (P(X), P(X|Y)) gone from the prose** in L13b; the math notation appears only in the related-files comment in `decisions.md`.

### Rule added (consider promoting to AGENTS.md)
**When writing learner-facing material in this repo, define every abbreviation on its first use, prefer plain words over symbols, and avoid stacking more than one adjective in front of a noun. If you find yourself writing "X-Y Z noun," refactor into a sentence: "the noun, which is Y and X, …" or similar.**

This rule deserves to be permanent — it'll come up again in the README, any future tutorial chapters, and any user-facing explanation. Will offer to add it to AGENTS.md next.

### What the fix doesn't address
- The user said "i have a few issues to fix" — plural. They named two issues explicitly (acronyms, friendliness) plus the stacked-adjective example. The rewrite addresses these three. If there are more issues they spot on a re-read, they're invited to flag.

---

## 2026-05-16 — walkthrough.md second pass + writing-style rule

### Issues raised on the rewrite
After my first readability pass, the user flagged three more issues on re-read:

1. **Visual consonant clusters between words look hard to pronounce.** Examples like `chan zo dem ne zo pluve` look stuck together — `n` at the end of `chan` next to `z` at the start of `zo`, `m` next to `n` between `dem` and `ne`, etc. A reader unfamiliar with Lexor's prosody can't tell that the space between words is a real short pause (~50–100 ms), which keeps adjacent consonants out of being a real cluster. The walkthrough never said this.

2. **The L1 explanation of pronoun `e` was misleading.** I wrote that `e` means "he, she, or they (one person)," which conflated the modern English singular *they* (one person, gender unknown) with plural *they* (multiple people). Plural "they" is a separate Lexor pronoun: `lo`. The user pushed back: "they is very different from he/she/it. it's plural. it's really undefined? then what does e even mean?" The point was sharp: by listing three English glosses without specifying which scope they each cover, I made `e` sound vague rather than precise. `e` is in fact precise about person/number/third-person and only vague about gender — that's the one and only thing it leaves open.

3. **The "X-Y Z noun" example in the proposed AGENTS.md rule was awkward.** Lifted out of context, the symbolic example didn't communicate what kind of construction the rule was forbidding.

### Fix
1. **walkthrough.md preface** — added a "A note on pronunciation" subsection. States explicitly that the space between words is a real pause, that adjacent consonants across spaces are not a cluster, that single Lexor words have stricter rules (max 2 consonants in a row, a few combinations forbidden) so no real Lexor word is hard to pronounce. Also flagged that placeholder forms like `pluve` are not yet locked.

2. **walkthrough.md L1** — rewrote the pronoun explanation. Split what `e` is precise about (person, singular, third-person) from what it deliberately leaves open (gender). Made the English mapping explicit: `e` covers the modern singular *they*, not the plural. Added a fuller pronoun table including `lc` (we inclusive of everyone) and a note that "we" splits into several distinct forms in Lexor.

3. **AGENTS.md** — added the writing-style rule under working conventions, without the symbolic example. Four bullets: define abbreviations on first use; prefer words over symbols; avoid stacked adjectives; be precise about what a feature commits to vs leaves open. The last bullet is new and comes directly from the pronoun-`e` mistake.

### Lesson worth keeping
When explaining a feature that *deliberately leaves something open* (gender on `e`, time on `a`, definiteness on bare nouns), be explicit about the asymmetry: "this commits to X and Y but deliberately not to Z." Just listing the multiple English translations side-by-side ("he, she, or they") makes the feature read as vague-overall, when it's actually vague-on-exactly-one-axis. The reader needs to see the axis named.

This is a writing-rule, captured in AGENTS.md's new fourth bullet.

---

## 2026-05-17 — Self-segregating morphology replaces mandatory pause

### What changed
The 2026-05-16 prosody decision required an obligatory ~50–100 ms acoustic break between every pair of content words to disambiguate the CV-vs-CVC overlap. User objected: "i dont like requiring waits AT ALL." Asked how natural languages solve the same problem.

### What natural languages actually do
- English: relies on stress patterns, phonotactic constraints, vocabulary sparsity. No obligatory pause.
- Spanish: actively dissolves word boundaries via resyllabification (`los amigos` → [lo-sa-migos]) and sinalefa (vowel merging). Famously rapid, continuous speech.
- Lojban: uses self-segregating morphology — word shapes are mathematically constrained so no concatenation of valid words equals another valid word. No pause needed.

The mandatory-pause rule was an over-engineering of a problem that has a structural solution.

### Why Lexor was almost there already
- All locked verb roots are consonant-initial.
- All content words already end in a vowel (locked).
- Closed-class items are a finite list (markers, prepositions, copulas, pronouns, digits, coordinators, quantifiers).

We only needed to formalize one new rule: **open-class content roots must start with a consonant**. This is already de-facto true.

### The new parsing argument
Given the rules:
1. Content roots start with a consonant, end with a vowel.
2. Closed-class items are a finite, memorizable list (some are vowel-initial).

Then:
- After a vowel-final word, the next sound is either:
  - A consonant → must be the onset of a new word (boundary clear).
  - A vowel → must be a closed-class vowel-initial item; lookup decides.
- After a consonant-final word (must be closed-class), the next sound is either:
  - A consonant → boundary clear.
  - A vowel → again, lookup against the closed-class list.

Worked through the canonical "ambiguous" pairs from the original prosody decision:
- `sa magas` (digit + content) vs `sam agas` (operator + ???) — `agas` is vowel-initial, not closed-class, so `sam agas` doesn't parse. Unique reading: `sa magas`.
- `ko mago` vs `kom ago` — same analysis. Unique reading: `ko mago`.

The pause was never grammatically needed. It was a workaround for a problem that doesn't actually exist under the stricter morphology.

### What changed in the files
- `decisions.md` — locked the new rule and explicitly superseded the 2026-05-16 mandatory-pause decision.
- `phonetics.md` — rewrote the "Word boundary" subsection. Pause is now recommended for clarity, not required. Three-rule mechanism explained.
- `walkthrough.md` preface — rewrote the "A note on pronunciation" subsection to match. Speakers can talk at natural pace.
- `trials.md` — added new trial J5 [stress, passes] confirming run-together speech parses uniquely.

### What this changes downstream
- The clause and sentence boundary rules (~200–300 ms and ~500+ ms) are unchanged. Those carry pitch and meaning information that morphology can't supply.
- The digit-stream rule (digits concatenate as one prosodic unit) is unchanged — it was already not about pauses but about the absence of structure.
- Stress is unchanged (first syllable, non-lexical).
- The recommended-pause-for-clarity convention is a courtesy, not a rule.

### Lesson worth keeping
Before locking a phonological constraint, check whether morphological structure already does the work. Mandatory speaker effort is a tax on the language's everyday use; structural constraints are paid once at design time.

### Parked
- Empirical test: write a paragraph of locked-vocabulary Lexor and confirm no part of it admits an alternate parse when spoken run-together. Trial J5 will be exercised when more vocabulary lands.

---

## 2026-05-17 — comparisons.md expanded to include natural languages

### Why
User asked: "ah, that compare with others like English and Spanish too?" The original comparisons.md framed itself as "Lexor vs other *constructed* languages," but most of `pain.md` engages with English and Spanish and Lexor borrows several decisions from Spanish. Confining the comparison file to conlangs left an obvious gap.

### What was added
Two new sections in `comparisons.md`, alongside the existing Lojban section. Each follows the same four-axis structure:
- **What [language] does well that Lexor sacrifices** — honest about the costs of leaving an established language.
- **What Lexor fixes** — concrete list, mostly drawn from pain.md and trials.md trap entries.
- **What Lexor borrowed from [language]** — explicit credit for design moves taken from natural languages.
- **What Lexor explicitly rejected** — design patterns the language deliberately avoids.

Plus a "trade-off, stated honestly" paragraph closing each section.

### Reframe of comparisons.md
Top of file rewritten: title changed from "Lexor vs other constructed languages" to "Lexor vs other languages." Added note that constructed-language comparisons are about technical differentiation while natural-language comparisons are about trade-offs.

Listed in the table-of-contents: Lojban, English, Spanish. Future entries (Mandarin, Latin, Esperanto, Toki Pona, Ithkuil, Sona) noted as possible later additions.

### Specific honest acknowledgments worth keeping
- **Lexor sacrifices English's redundancy.** Compact CVC roots are less forgiving of mishearing than English's morphologically rich words.
- **Lexor sacrifices Spanish's subjunctive expressiveness.** The composable modal markers (chan/kan/mus + conditional vowel) are technically equivalent but lose some of the subjunctive's compactness for hopes/doubts/desires.
- **Lexor's pronoun system loses Spanish's gender-based disambiguation cheapness.** In a paragraph with two women, Spanish writers use "la otra" — Lexor needs names or def-bindings. Real cost.
- **Beating English at being English is not the goal.** English wasn't designed for precision; it survived for social cohesion. The bet is that for tasks where precision matters more than ergonomics (technical writing, legal text, scientific argument, multi-step reasoning), Lexor will be measurably better. For casual conversation, English likely wins on social comfort.

### What this doesn't yet cover
- **Mandarin** — would be interesting because it tonally distinguishes words and has classifier systems Lexor could learn from.
- **Latin** — interesting because Lexor sources many roots from it; comparison would clarify what Lexor took vs left.
- **Toki Pona** — minimalist constructed language with ~120 words; very different design philosophy.
- **Ithkuil** — extreme-precision constructed language; comparison would expose Lexor's commitments to readability vs theoretical maximum precision.

Parked unless a use case surfaces.

---

## 2026-05-18 — Closed-class subclass-vowel suffix (C-2)

### Why
The self-segregating-morphology fix (2026-05-17) solved word-boundary *parsing* but not *pronounceability*. Closed-class CVCs like `aks`, `sur`, `kun`, `sam` end in consonants, and they stack frequently (especially in technical sentences like the axis system, modal operators, prepositional chains). Stacked CVCs produce uncomfortable boundary clusters: `aks sur` → doubled /s/, `aks fas` → three-consonant cluster /ksf/, `imp tra` → four-consonant pile-up /mptr/.

User pushed back: "you sure that's comfortable? it feel awkward to me." Honest answer: no, it wasn't. The hand-waved "speakers accommodate naturally" was inadequate.

### Options considered
- **Accept rough spots.** Speakers cope. User found it awkward.
- **Buffer-vowel sandhi.** Insert /a/ unconsciously between consonant clusters. Adds a phonological rule; speakers have to learn it.
- **Add a meaningless `-a` to all closed-class items** (`aksa`, `kuna`). User: "no adding meaningless V at the end."
- **Redesign closed-class to CV (one syllable, vowel-final).** Loses Latinate mnemonics. Bigger change.
- **Subclass-vowel suffix** (chosen). Each closed-class subclass gets a specific ending vowel that *signals* the subclass. The vowel does real work, not ornament.

User asked: "would it be possible to use a vowel for nouns, another vowel for adjectives etc, so the roots stay CVC?" That's exactly Esperanto's system. Confirmed: word class for *content* roots already lives in the derivation consonant (r/n/t/s), so no vowel exhaustion. Word class for *closed-class* items can use the suffix vowel slot freely.

### What was decided
| Subclass | Suffix | Examples |
|---|---|---|
| Prepositions | `-a` | `tepa`, `loka`, `sura`, `dora`, `fasa`, `moda`, `kawa`, `anta`, `posa`, `inta`, `oksa`, `kira`, `dira`, `suba`, `poka`, `lata`, `sina`, `lima`, `pena` |
| Coordinators | `-e` | `kune`, `vele` |
| Markers | `-i` | `isi`, `dati`, `ergi`, `impi`, `liti`, `fini`, `vari`, `defi`, `keti`, `kani`, `musi`, `chani`, `aksi`, `tipi`, `mezi` |
| Copulas | `-o` | `samo` (identity, also numerical equality), `esto`, `stao`, `memo` |
| Quantifiers / operators | `-u` | `solu`, `totu`, `nulu`, `kelu`, `padu`, `masu`, `minu`, `magu`, `tomu`, `piru`, `demu`, `dozu`, `pemu`, `kexu` |
| Time-unit content roots | `-a` (default) | `nuna`, `moma`, `mita`, `xora`, `dima`, `sema`, `mesa`, `veta` |

**Exceptions (kept as-is because they're already vowel-final or special):**
- `no` (negation prefix, phonologically bound to its host).
- `ka` (universal question particle, high-frequency, vowel-final).
- `ke` (universal complementizer, high-frequency, vowel-final).
- `bra` (group-open, paired with `keti`, already vowel-final).
- `tra` (preposition "through," already ends in -a matching the subclass vowel).

**`sam` → `samo`:** treated as copula, single form covering both identity (`samo a b` = a is b) and numerical equality (`samo re ko` = 3 = 4? false). No separate form for the quantifier sense.

### The win
Every word in spoken Lexor now ends in a vowel. Every word boundary is either:
- vowel + consonant (smooth, no cluster), or
- vowel + vowel (allowed glide).

Zero consonant clusters at boundaries, ever. Speakers can talk at natural pace without thinking about consonant accommodation.

The suffix vowel earns its keep: it signals the subclass of closed-class word, so a listener hearing a word end in `-u` knows it's a quantifier or operator before recognizing the specific root. Esperanto-style class signaling.

### Sweep applied (2026-05-18)
- `lexicon.yaml` — ~50 root entries renamed; cross-references in `notes` fields updated.
- `roots.md` — markers, prepositions, coordinators, copulas, and quantifier tables updated.
- `examples.md` — all closed-class references swept.
- `walkthrough.md` — all levels and the preface updated.
- `trials.md` — all trial entries swept.
- `phonetics.md` — Prosody section's worked examples updated.
- `comparisons.md` — Lexor references in the English/Spanish/Lojban sections swept.
- `frequencies.yaml` — `assigned_root` values updated.

Etymology references in `source:` fields preserved (e.g., "English can / German kann / Dutch kan" stays — those are natural-language origins, not Lexor forms). Done via a context-aware script (`/tmp/rename_lexor.py`) that only touches text inside backticks or markdown code blocks plus the `root:` and `assigned_root:` yaml fields.

History.md and decisions.md historical entries are unchanged — they document the language's evolution and reference the old forms accurately for their time.

### Parked
- **C-1 vs C-2 trade-off review.** C-1 (uniform `-a`) was rejected for being ornamental. If the subclass-signal turns out to be hard to learn (users mis-remembering which subclass gets which vowel), revisit.
- **Compound and derivation morphology** at the closed-class level. Lujvo-style closed-class compounds aren't yet designed.
- **`bra` exception** is a little inconsistent (markers should end in `-i`, but `bra` doesn't). Tolerable for now; revisit if it bites.
- **Stale example text** that uses bare verb roots (like `dik e` instead of `dike e`). Not a C-2 issue; pre-existing. Clean up in a future pass.

---

## 2026-05-18 — Vocab batch 1: 47 content roots

### What was added
First substantive vocabulary buildout, post-C-2. Forty-seven content roots covering universal high-frequency concepts:

- **20 verbs** — preference (`vol` want, `dev` need, `gus` like, `lov` love, `nem` hate), cognition (`sav` know-fact, `kon` know-person, `kog` think), action (`tul` use, `lab` work), biological state (`som` sleep, `vig` wake), communication (`ker` ask, `res` answer), transaction (`kop` buy, `vez` sell), recreation (`lud` play, `son` sing, `bal` dance), motion (`nat` swim).
- **10 environment nouns** — `vat` water, `fog` fire, `ter` earth, `sun` sun, `lun` moon, `tel` star, `lig` tree, `lap` stone, `kas` house, `vej` road.
- **9 people / body nouns** — `gen` person, `vir` man, `fem` woman, `nin` child, `kor` body, `kab` head, `kar` heart, `man` hand, `ped` foot.
- **8 adjectives** — `bon` good, `mal` bad, `big` big, `tin` small, `nov` new, `mat` old, `kal` hot, `kol` cold.

### Sources
Mostly Latin and Spanish (≈70%) where the everyday Romance word fits CVC cleanly. English (≈25%) where the Germanic form is more recognizable (`big`, `tin`, `lov`, `kol`, `sun`, `vej`, `vat`, `tul`). Greek (≈5%) for `nem` (hate).

### Phonetic constraints honored
- All CVC.
- None /k/-final.
- None h+vowel start (this killed obvious candidates `hom` for person and `hat` for hate — switched to `gen` and `nem`).
- No doubled consonants, no 3+ clusters within a root.

### Collision avoidance
The closed-class underlying roots (now suffixed as e.g. `aksi`, `kani`, `samo`) were treated as off-limits at the root level even though their bare CVC form isn't in lexicon.yaml — reusing them would confuse learners who recognize the closed-class word.

### Coverage
`frequencies.yaml` now has 76 `assigned_root` entries (was 29 before this batch). Concepts still needing roots at the top of the priority queue: time, eye, mouth, air, sky, morning, night, find, get/obtain, speak/talk specifically (currently composes with `dik`), fly, first, last.

### What this unblocks
- Real example sentences with vocabulary instead of `[bracketed]` placeholders. The walkthrough's L18 paragraphs can now be rewritten using actual roots.
- Validation that the C-2 system is comfortable in practice with real content words flowing through.
- Frequency-driven assignment continues — next batch could target body parts that need more design effort (eye, ear, mouth) plus closure of the most-cited gaps in trials.

### Parked
- **Demonstratives** (this, that, these, those). Composable with `ka` + `ke` or new root family. Defer to its own design round.
- **Number nouns** (one-thing, two-thing concepts vs digit). Currently the digits suffice; no dedicated "first / last / unique" roots yet. `first` (`pa-na`?) and `last` (`xut-na`?) compose from existing.
- **Function words: what, who.** These compose with `ka` (universal question particle); no dedicated roots needed.
- **Eye, ear, mouth.** Vowel-initial source words across all candidate languages make these hard to fit into consonant-initial CVC. Need a thoughtful design pass.

---

## 2026-05-18 — Vocab batch 2: 26 more content roots + L18 rewrite

### What was added
Second vocabulary batch (after C-2 stabilization). Twenty-six more content roots:

- **10 verbs** — perception/communication (`mir` look, `chal` talk), motion (`kam` walk, `vor` fly, `sed` sit), action (`bib` drink, `lan` throw, `gid` drive, `pin` paint, `gan` find/gain).
- **10 nouns** — body (`vid` eye, `bos` mouth), environment (`luv` rain), units (`met` meter, `kub` box), language/abstract (`nom` name, `lin` language, `lex` word, `num` number, `mon` money).
- **6 adjectives** — speed (`rap` fast, `tar` slow), length (`lon` long), moisture (`mol` wet), aesthetic (`bel` beautiful), emotion (`dol` sad).

Total lexicon: 185 → 211 entries.

### Notable design moves
- **`vor` for fly** (from Latin *volare*) — couldn't use `vol` because batch 1 took it for "want." Shifted to `vor`, accepted the slight mnemonic stretch.
- **`vid` for eye** (vision-organ) — distinct from `vis` (see-action). Mnemonic from *videre*; the eye is the see-organ, vis- the verb.
- **`bos` for mouth** (from Spanish *boca*) — couldn't use `bok` because /k/-final is forbidden by phonetics rule 1. Swapped k→s.
- **`luv` for rain** (Spanish *lluvia* / Latin *pluvia*) — dropped the consonant cluster to fit CVC. Now `luve` (rains-present), `luvex` (is-raining), `luvo` (rained), etc.
- **`chal` for talk/chat** — distinct from `dik` (say). Spanish *charlar*. Conversational vs propositional speech.
- **`mir` for look-at** — distinct from `vis` (see-passively). Spanish *mirar*. Intentional vs incidental perception.

### Sweep of active docs
Replaced `[metr]` → `met` and `[box]` → `kub` everywhere in `walkthrough.md`, `examples.md`, `trials.md`. Replaced `pluv-` placeholder roots → `luv-` (so `pluve` → `luve`, etc.). Updated the convention note in `examples.md` to reflect that `bib`/`dik` are now locked roots, and the walkthrough preface to note that most placeholders are now real words.

### L18 rewrite (committed as 1c4f31a, earlier today)
Replaced the contrived original example sentences (she-might-come-pet-her, pushup-bet) with six worked scenes using real vocabulary from batch 1: morning routine, trade, modal+complement clause, navigation order, hedging measurement, reasoning chain. The new examples flow with locked vocabulary instead of placeholders, demonstrating real-world fluency of the language.

### Frequencies coverage
`frequencies.yaml` now has 102 `assigned_root` entries (was 76 before batch 2). Batch 2 added 22 new entries to the file for concepts not previously tracked.

### Still missing (next batches)
- **ear** — vowel-initial source words in all candidates; needs design thought.
- **time** (the abstract concept) — `tem` taken (fear), `tep` is now `tepa` (preposition). Park.
- **first / last / unique** — could compose with digits + ordinal marker (no marker yet) or get dedicated roots.
- **morning / night** — composition or dedicated roots.
- **Many specialized vocab** — colors (red/blue/green), animals (dog/cat), common foods, body parts beyond face. Tackleable in subsequent batches.

### Parked
- **Demonstratives** (this/that). Still parked from batch 1.
- **Compound noun formation**. Lojban-style lujvo rules haven't been studied yet.
- **Time-as-noun root**. Hard because of root collisions.

## 2026-06-07 — Scalar degree / amount-modifier system (postposed, not bound)

Started from a material-science question: brittleness = lack of stored plastic energy, but a springy-but-shattering material (lots of elastic energy, ~0 plastic) is *also* brittle — so "brittle" conflates an energy *magnitude* with a failure *mode*. Working out how Lexor should name material properties surfaced the general question of how scalar opposites and degrees work, and whether the amount machinery belongs inside the word or beside it.

### The material-property example (the motivating case)
English splits the area under the stress–strain curve unevenly: **resilience** (elastic energy, area to yield), **toughness** (total energy to fracture), and a *nameless* plastic-only integral. Separately, **ductile ↔ brittle** is a different axis entirely (does it yield before breaking), not an energy magnitude. The "we need ~6 words" feeling comes from English minting separate lexemes for points on what are really **two scalar axes**: (A) energy absorbed per unit volume, region-scoped to elastic/plastic/total; (B) plastic-fraction at failure (ductile = high, brittle = low). On axes, "opposite" is just the low end — `minu` — not a separate root. This is the concrete H2 case (neutral magnitude term).

### Three operations English collapses
Clarified that there are **three** distinct operations, and natural languages mark all three (English: *not* / *un-,dis-* / *-less*):
- **Complement** (≠, the set-complement): "not happy" includes sad *and* neutral *and* asleep — anywhere but the positive value. This is Lexor's `no` (proposition-level, bound prefix, already locked).
- **Contrary** (× −1, opposite pole): `unhappy` = sad, `dislike` = aversion. NOT logical negation — these lexicalize to the far pole.
- **Privative** (× 0, absence): `-less` = careless, colorless. Zero of the quantity.

Key correction during the discussion: `dislike`/`unhappy` *feel* like negation but are actually **contrary** (× −1), which is exactly why overloading Lexor's strict-logical `no` with the opposite-job would reintroduce ambiguity (`nopretty` = "≤ norm" vs "ugly"). The intuitiveness the user liked comes from the form being **bound into the word**, not from it being the `no` sound.

### Why postposed separate words, not bound affixes
The user wanted to integrate this with amount-quantifiers (× −1, × 0, × 2, "stronger"). That reframe is what settled the position question: as an *antonym affix*, × −1 sits in a prefix-biased category; as *the −1 coefficient in a degree system*, it rides with quantities — and Lexor already postposes those (number-after-noun, `magu`/`minu` polarity after the axis). Decisive practical point: the amount class is **open** (any number, ranges via `tomu`, ≈ via `piru`, scale via `pemu`). Binding it would force a bound duplicate of the whole numeral system — precisely the mistake Lexor refused when it kept numbers as separate words instead of a plural suffix. Rule reaffirmed: **bind only small closed classes (tense, role, `no`); keep open/productive systems as separate words.**

Empirical check on "do inverters have to be prefixes": suffixal **negation** (Turkish `-me`, Japanese `-nai`) and suffixal **privative** (English `-less`, Finnish abessive `-tta`, Hungarian `-tlan`) are well-attested; it is specifically **contrary/opposite-pole** derivation that resists suffixing cross-linguistically (prefers prefixes un-/dis-/mal- or suppletion). So × 0 suffixes freely, × −1 is the holdout — but the coefficient reframe moves × −1 out of the "antonym affix" reference class entirely, so the prefix bias no longer binds.

### Reference-point convention (also closes the parked signed-magnitude item)
A scalar comparison needs a reference. **Bipolar** axes use the natural origin `zo` (`minu zo`/`magu zo`/`samo zo` = negative/positive/neutral side). **Unipolar/ratio** axes (no negatives) use a contextual norm (`minu` = below typical); `samo zo` = absence. This is the convention left open under "signed magnitudes compose `magu`/`minu` on top of `mezi`."

### Alternatives considered and rejected
- **Overload `no` for opposites** — rejected: creates one-form/two-meanings ambiguity (complement vs contrary).
- **Mint a productive opposite-marker now** (reopening the 2026-05-16 rejection) — partially reconsidered. The 2026-05-16 reasons (opposite is fuzzy for `house`/`run`; root-saving not a priority) are defeated *for scalars* by scoping to gradable roots and by the new **chunking** argument (a bound opposite is one stored retrieval). So a bound shorthand for the two poles is approved *in principle* — but **parked**, because a bound pole-marker needs a reserved prefix/suffix slot, and the prefix-inventory + prefix-stacking-order questions are still open (tasks.md). Lock the compositional system now; add the sugar once the slot system is built.
- **A dedicated contrary suffix** (floated mid-discussion) — superseded: with the coefficient reframe, contrary is just `minu` on a named axis, so no dedicated affix is needed; the cost shifts to naming the axis (H2), which is the better problem to have.

### What this leaves open
Exact multiplicative coefficient (general × N beyond `pemu`'s × 10ⁿ); absolute intensifiers ("very"/"slightly") vs the relative `magu`/`minu`; and axis-naming for everyday adjectives (H2), which the whole scalar-opposite story now depends on. The compositional layer added no new roots — it reuses the `-u` operator class. The bound layer (next section) added two prefixes.

## 2026-06-07 (same session) — Bound polarity prefixes `mi` / `ze` locked (un-parking the actual task)

The previous section parked the bound shorthand for the two poles "pending the prefix-inventory / stacking decisions." That was wrong: designing the −1 and 0 operators *was* the task, and parking it deferred the deliverable. The prerequisite questions (which CV shapes are prefixes; stacking order) are not really prerequisites — locking these two prefixes is what *answers* them. So the bound forms are now designed and locked.

### Decision
Two bound prefixes join `no` as one polarity family, restricted to gradable/scalar roots:
- `no` — complement ("not", ≠) — existing.
- `mi` — contrary (× −1, opposite pole). Source *minus*; deliberately echoes `minu`. Bipolar scales only.
- `ze` — privative (× 0, absence). Source *zero*; deliberately echoes `zo`. Any scalar.

### Prefix, not suffix — and why this overrides the default
Lexor's standing rule is prefix = scope (proposition-level), suffix = derivation (value-level), which by itself would make contrary/privative *suffixes* (they produce another value on the same axis). Overridden deliberately, for three reasons:
1. **Family coherence.** These three are the negation/polarity operators. Keeping them one prefix series ({`no`, `mi`, `ze`}) is more learnable than splitting negation-as-prefix from opposite/absence-as-suffix. English itself is inconsistent here (un-/dis- prefix, -less suffix); Lexor unifies.
2. **Frame-first helps.** Knowing "opposite-of" or "without" *before* the root lets the listener process the root already in the modified frame — the same modifier-first logic that put `no` in front. The affirmative-leak hazard that is specific to *negation* doesn't apply, but the framing benefit still does.
3. **The user's throughline.** The whole reason the bound form exists is the `unhappy`/`dislike` chunk intuition, and those are prefixes. Matching that intuition is the point.

### Morpheme sourcing
`mi` from *minus* and `ze` from *zero* tie the two prefixes directly to the user's own "× −1 / × 0" framing, and each echoes an existing word with the same polarity (`minu` low/less; `zo` zero) so the meaning is transparent without creating a collision (the prefixes are bound, the echoed words are free). Both are CV, vowel-final, attaching to consonant-initial roots — smooth under the self-segregating-morphology rule, and exempt from the subclass-vowel scheme exactly as `no` is.

### Scope, stacking, redundancy
- **Scope by scale type:** `ze` (× 0) on any scalar; `mi` (× −1) only on *bipolar* scales (real opposite exists). On unipolar scales ("tough", "tall") there is no × −1 — "less tough" is the postposed `minu`, not `mitough`. This is why `mi` and the reference-point convention agree.
- **Stacking:** `no` outermost (`nomi[pretty]` = "not ugly"); `mi`/`ze` mutually exclusive on one root. First concrete prefix-stacking rule; fixes the prefix inventory at three.
- **Redundancy is intended:** `mi`/`ze` are the lexicalized everyday shorthand; `samo minu pa` / `samo zo` / postposed `minu` stay for exact/numeric work. Two forms, one meaning = paraphrase.

### Alternatives reconsidered
- **Suffixes** (architecture default): rejected for family coherence + frame-first, above. Noted that privative-as-suffix (`-less`) is the cross-linguistic norm, but consistency with `no` won.
- **`an-` (anti-) for contrary:** rejected — shares an onset with the time preposition `anta` (before), a needless near-collision. `mi` is cleaner and ties to `minu`.
- **`zo-` (the digit itself) for privative:** rejected — would overload the digit root `zo`; `ze` keeps the zero mnemonic without the overload.

## 2026-06-07 (same session) — H2 closed: gradable roots = neutral axis, adjective defaults positive

The scalar-opposite/degree machinery (`magu`/`minu`, `mi`/`ze`, `mezi`) all assumed a *named scalar dimension* but never said how a gradable concept's root names it. H2 was the keystone. Resolved.

### Decision
A gradable-concept root denotes the **quality/dimension itself**, direction-free. This is the natural reading of two standing principles: "roots are concept-level" (the root is the concept, not a POS or a pole) and "no implied direction." Everything directional derives from it:
- **Magnitude noun:** `mezi [Q] X` = "the degree of [Q] of X." `mezi` is generalized from geometric length to any abstract scalar quality — that *is* the H2 neutral magnitude term.
- **Adjective:** the bare `-s` adjective (`[Q]asa`) **defaults to the positive pole** ("beautiful"). Markedness — the common high case is unmarked.
- **Direction/degree:** `minu` (low / less), `mi` (opposite, bipolar only), `ze` (absence), all already locked.

### Why default-positive, and how vagueness survives
User chose default-positive over strict-neutral. Strict-neutral (bare adjective = "has Q, direction unstated") is more principled but taxes the common case — you'd pay `magu` every time you call something beautiful. Default-positive matches how natural languages mark gradables (unmarked = positive pole: "how *tall*", "how *old*"). The "no mandatory marking / vague allowed" meta-principle is *not* violated, because the direction-free form still exists — it's the magnitude noun `mezi [Q]` ("the degree of Q"), not the bare adjective. So vagueness moved to the magnitude route; the bare adjective took on the high-frequency positive job.

### Bipolar vs unipolar (kept consistent)
Bipolar qualities (beauty, warmth) get both a low end (`minu`) and an opposite-quality (`mi`). Unipolar/ratio qualities (height, mass, toughness) get only a low end (`minu`); `mi` is undefined there — "less tough," not "anti-tough." Same split as the reference-point convention (bipolar → origin `zo`; unipolar → contextual norm).

### Worked back to the material-property example that started all this
Toughness is unipolar: `mezi [tough] X` = degree of toughness; brittle = low on a *different* axis (plastic-fraction), `mezi [ductile] X` with `minu`. Resilience = `mezi [tough] X` scoped to the elastic region. The "we need 6 words" problem dissolves into two named quality-roots + the degree operators — no antonym roots, no conflation of energy-magnitude with failure-mode.

### What's still open
Exact ×N coefficient; absolute intensifiers ("very"/"slightly"). (The material-property roots that follow were the immediate next step.)

## 2026-06-07 (same session) — Material-property vocabulary, by decomposition

The thread opened with a material-science complaint: English names *resilience* (elastic energy) and *toughness* (total energy) but has **no one-word term for plastic-only energy**, and it conflates *brittle* (a failure mode) with *low toughness* (an energy magnitude). The instruction for Lexor was explicit: don't copy that incomplete system — "ours must be good."

### Decision: decompose, don't borrow
Named engineering properties are **compositions** over a few base quantities, not separate borrowed roots. Six base roots added: `tes` stress (Latin tensio), `dis` strain (distortion), `ner` energy (Greek energeia), `las` deformation-recoverability (Greek elastikos), `dus` hardness (Latin durus), `rup` fracture (Latin rumpere). (`dur` and `lon`, the first picks for hardness/strain, were already taken — endure/long — so re-sourced to `dus`/`dis`.)

The key move is **regime-scoping of energy by the recoverability adjective `las`**:
- elastic regime = `lasasa` (recoverable), plastic regime = `zelasasa` (non-recoverable, ×0 recovery).
- resilience = `mezi ner lasasa <X>`; plastic energy = `mezi ner zelasasa <X>`; toughness = `mezi ner <X>` (total). Identity: toughness = resilience + plastic energy.

That is the completeness win: **plastic energy, which English cannot say in one word, is a regular phrase here**, and it sits in an explicit additive relationship with the other two. No region-scoping *mechanism* had to be invented — `lasasa`/`zelasasa` is just an adjective modifying the quantity head (`ner`), ordinary modifier-after-head.

Other properties fall out the same way: strength = stress at fracture (`mezi tes tepa rup <X>`); stiffness/modulus = stress per strain (`mezi tes kexu dis <X>`, reusing `kexu` "per" exactly as the H3 pixels-per-mm trial does); ductility = non-recoverable strain (`mezi dis zelasasa <X>`), brittle = that with `minu`; hardness = `mezi dus <X>`.

### Why this beats English structurally
The brittle/low-toughness conflation is *impossible* to make here, because toughness is built on `ner` (energy) and ductility/brittleness on `dis` (strain) — different roots. English collapses them because it lexicalized points on two different curves into adjacent-sounding words; Lexor keeps the curves (energy vs strain) as separate base quantities and derives the rest.

### Side decisions
- **`kal`/`kol` refactored to H2.** The pre-H2 hot/cold antonym pair became one neutral root `kal` = temperature (hot = `kalasa`, cold = `mikalasa`, temperature = `mezi kal X`); `kol` removed. Only the lexicon referenced them, so the sweep was clean. Flags the general pattern: legacy antonym pairs get folded into single H2 axes as they surface.
- **Units = metric/SI by default** (energy density J·m⁻³, stress Pa). Only the default system is fixed; the unit-*expression* mechanism stays parked.

### Still open
Unit-expression mechanism; elastic/plastic as standalone regime *nouns* if ever needed (currently only the adjective forms are used); the broader physical-property vocabulary (density, mass, conductivity, …) as future batches; exact ×N coefficient and absolute intensifiers. Lexicon now 218 entries, collision-clean.

## 2026-06-07 (same session) — Orthography: no dashes

Up to now prefixes were written with a teaching dash (`no-loma`, `mi-kalasa`). User's call: drop it — "I don't want dashes in our language. We got spaces. That should be enough."

Rationale: the dash never carried information. Negation/polarity prefixes were already decided to be *phonologically bound* (one stress group, no pause), so in speech there is no separator at all. In writing, self-segregating morphology (content roots consonant-initial, prefixes vowel-final) plus the closed three-prefix inventory {no, mi, ze} make the boundary recoverable from the letters: `noloma` can only be `no`+`loma` (a root `nol` would leave the invalid vowel-initial `omes`). So the dash was redundant clarity, and redundant marking is exactly what Lexor sheds.

Decision: **spaces are the only word separator; bound prefixes attach with no space and no dash.** `noloma`, `mikalasa`, `zelas`, stacked `nomikalasa`. Swept all docs + lexicon root fields (`"no-"`→`"no"`, etc.), preserving English-prose hyphenated compounds (`no-mandatory`, `no-lexical`, `no-time`, the `mono-temporal` substring) since those are English, not Lexor. Collision-clean at 218 entries (the bare `no`/`mi`/`ze` forms are unique against digits, pronouns, and CVC roots).

Recorded as the first writing-system rule in decisions.md; a dedicated orthography section can grow from it. Left untouched (out of scope, flagged): a few examples.md cases write negation as a *spaced* separate word before an operator — whether negation binds to a following operator with no space, like it does to a root, is resolved in the next entry.

## 2026-06-08 — Negation scope = attachment point; no bracket symbols

Two finalizations from the same thread.

### Negation: one operator, attachment = scope
The spaced `no musi` / `no samo` in the docs looked like a *second* kind of negation (sentential, separate word) alongside the bound prefix. It isn't. The examples already showed the real rule unstated: `noloma e` (`no` on the verb = predicate negation) vs `loma no[apple] e` (`no` on the argument = constituent negation) vs `nosamo` (`no` on the operator = "≠"). The attachment point already carries the scope.

So there is exactly **one** negation — the bound prefix `no` — and *where you attach it is what it scopes*. The spaced forms were legacy inconsistency, now swept to attached (`nomusi`, `nosamo`, `nokani`, `nomesa`).

Multi-word scope: an operator-headed proposition is negated by attaching to the head (`nomusi P` = ¬□P, the modal scopes the rest). A multi-word scope with no single operator head is wrapped in the existing brackets, attaching to `bra`: `nobra … keti`.

Rejected alternative: a separate spaced word for sentential negation (Lojban `na` style). It would double the negation mechanism for no gain — `nobra…keti` already expresses sentential negation with existing parts — and reintroduce the spaced-vs-bound split just eliminated. Minimalism wins.

### No bracket symbols
User's reasoning: if `bra`/`keti` already behave like brackets, no bracket *symbols* are needed. Correct. `bra` and `keti` are spoken words; a `(`/`[` symbol would be one you'd still pronounce "bra," i.e. a writing-only shorthand that diverges from speech — forbidden by "written like talked." Grouping is therefore lexical, not punctuational, and identical in speech and writing. This is also the answer to the worry "does Lexor lean on written punctuation that fails when spoken?" — no: every disambiguator (grouping, scope, roles) is an audible recoverable word; punctuation is limited to comma/period (pauses) and the radix point (number position). Closes the parked "written form for the brackets" item: no symbol form.

### Still-present dash remnants (flagged, not swept here)
Independent of negation: role-vowel notation around placeholders (`[apple]-o`, `e-e` → should be `[apple]o`, `ee` per the doubled-vowel rule) and labelled-variable forms (`loka-x`, `loka-y`) still carry dashes and violate the 2026-06-07 no-dash rule. Left for a focused follow-up because `loka-x` needs a small decision on how to write a labelled variable (`loka vari x`?).
