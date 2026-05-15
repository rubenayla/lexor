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

## 2026-05-15 — Negation prefix: `no-`
Decided: negation is prefixed `no-`. Matches Spanish, English (`no`), Italian, French (`non`), Latin (`non`), German (`nein`) — maximum cross-language recognizability. `n` is already the act-noun derivation suffix consonant, but slot differs (suffix vs prefix) so there's no actual ambiguity.

Worked examples with `lom`:
- `loma` — eats
- `no-loma` — does not eat
- `lomer` — eater
- `no-lomer` — non-eater (one who doesn't eat)
- `lomes` — edible
- `no-lomes` — inedible

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

Negation by existing `no-` prefix:
- `no-sam` = ≠, `no-min` = ≥, `no-mag` = ≤

Plus-or-minus, ranges, distributions are *compositions* of these. No special syntax. Examples sketched (specific digit-roots TBD):
- "around 15" → `pir pi fi`
- "between 2 and 8" → uses `tom` between the two numbers
- "≥ 10" → `no-min` + the number
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
   - Operator scope (`sol`, `no-`, `tot`): scopes over its adjacent argument. Three positions = three distinct meanings.
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
no-B.           ← Not B.
erg no-A.       ← Therefore, not A.
```

Three sentences, each with one meaning, each parseable independently. The logical relationship between them is explicit (premise / observation / conclusion) rather than encoded in nested structure.

Proof-by-cases extension:
```
dat A imp B.                ← Given: A → B.
is B, [unconstrained].       ← When B holds, A may or may not. (forward direction underconstrained)
is no-B, no-A.               ← When B doesn't hold, A doesn't either. (modus tollens)
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
