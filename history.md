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
