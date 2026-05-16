# Walkthrough — Lexor by progressive complexity

Read top-to-bottom to learn the language. Each level introduces one new piece of grammar; later levels assume the earlier ones. Examples use bracketed placeholders like `[apple]` for content words whose roots haven't been formally assigned yet — the grammar is the focus, not the vocabulary.

**Conventions used below:**
- `lexicon entry` for locked roots (lowercase, no markup).
- `[bracketed]` for unlocked placeholders.
- Verb root + tense vowel: `lom` (eat-concept) + `a` (atemporal) = `loma`.
- VOS sentence order: verb, object, subject — but most modifiers (quantifiers, prepositional phrases) follow the noun they modify.

For dense reference, see `examples.md`. For the test suite by capability, see `trials.md`.

---

## L0 — The bare verb

**Lexor:** `loma`

**Gloss:**
- `lom` — eat-concept (root)
- `a` — atemporal-frame inner vowel (the default, meaning "no specific time")

**English:** "(to) eat" / "eats (in general)"

**What this demonstrates:**
- Every content word is a CVC root plus a vowel.
- The inner vowel is the temporal frame. `a` is the universal default — speaker not committing to any specific time.
- A bare verb with no subject is a statement of the action in the abstract. The listener fills in the subject from context if needed.

**What's missing yet:**
- No "who's doing it" yet — that's the next level.

---

## L1 — Adding a subject

**Lexor:** `loma e`

**Gloss:**
- `loma` — eat (atemporal)
- `e` — third-person singular pronoun (he/she/they, gender-neutral)

**English:** "She eats." / "He eats." / "They eat (one person)." — the pronoun doesn't commit to gender.

**What this demonstrates:**
- VOS order: with no object, the subject follows the verb.
- Pronouns are CV or V shape (shorter than content roots) — `e` is one of 11 pronouns.
- No mandatory gender. The language never forces a commitment the speaker hasn't made.

**Other pronouns in this slot:**
- `y` (I), `u` (you-singular), `e` (he/she/they-person), `i` (it)
- Plurals: `le` (you+me), `lo` (they-people), `ly` (you-plural), `la` (we, generic)

---

## L2 — Tense

**Lexor:** `lomo e` — she ate
**Lexor:** `lome e` — she eats right now
**Lexor:** `lomi e` — she will eat
**Lexor:** `lomex e` — she is eating (present continuous)
**Lexor:** `lomy e` — she would eat (conditional)
**Lexor:** `lomu` — eat! (imperative, subject often elided)

**Gloss:**
- The inner vowel of the verb encodes tense.
- `a` atemporal, `e` present, `o` past, `i` future, `u` imperative, `y` conditional, `c` perfect.
- `x` after a tense vowel = continuous aspect.

**What this demonstrates:**
- Tense lives in one vowel, not in conjugation tables. Same vowel works on derived non-verbs too (a "current eater" vs a "former eater").
- Tense is opt-out, not opt-in: `a` means "I'm not committing to a time."

**What's missing yet:**
- What if you don't know the tense? Use `a` — atemporal is the principled choice when uncertain.

---

## L3 — Adding an object

**Lexor:** `loma [apple] e`

**Gloss:**
- `loma` — eat
- `[apple]` — the thing eaten (placeholder; the apple-root isn't locked yet)
- `e` — she

**English:** "She eats an apple."

**What this demonstrates:**
- VOS order: verb, then object, then subject. The object sits between the verb and the subject by default — no preposition needed.
- No article (`a`/`the`). Definiteness is opt-in; bare nouns are unspecified by default.
- No plural. "An apple" / "apples" / "the apple" all surface as `[apple]` unless number or definiteness matters.

---

## L4 — Role vowels (when position alone is ambiguous)

**Lexor:** `loma [apple]-o e-e` — same meaning, explicit roles
**Lexor:** `dake [apple]-o e-e u-u` — she gives an apple to you (three arguments)
**Lexor:** `apre [door]-o e-e [key]-i` — she opens the door with a key (instrument)

**Gloss:**
- Outer vowel on a noun marks its role.
- `-e` subject, `-o` object, `-u` recipient (dative), `-i` instrument.
- Attached only when default position doesn't fully pin the roles.

**What this demonstrates:**
- Lexor's grammar pins roles by position *or* by morphology. Position works for two-argument verbs; explicit role-vowels handle three-or-more.
- Doubled vowels (like `e-e` where the pronoun already ends in `e`) are pronounced as a long vowel.

---

## L5 — Quantifiers and counts

**Lexor:** `loma [apple] re e` — she eats three apples
**Lexor:** `loma [apple] tot e` — she eats every apple
**Lexor:** `loma [apple] kel e` — she eats some apple
**Lexor:** `loma [apple] nul e` — she eats no apple
**Lexor:** `loma [apple] sol re e` — she eats only three apples

**Gloss:**
- `re` digit 3 (digits: `zo pa du re ko fi sa chi bo ne` = 0–9)
- `tot` universal (∀), `kel` existential (∃), `nul` none, `sol` only
- Quantifier follows the noun.

**What this demonstrates:**
- Number is a separate optional modifier system, not a noun inflection.
- Quantifier order is locked: it follows the noun, like all modifiers.
- "Every" / "some" / "none" / "only" are single CVC roots, not multi-word.

**Distributive vs collective:**
- `loma [apple] re pad e` — three apples, each individually (distributive)
- `loma [apple] re mas e` — three apples, together as a group (collective)
- Unmarked = speaker not committing to either reading.

---

## L6 — Prepositions (time, place, manner)

**Lexor:** `loma e tep dim` — she eats during the day
**Lexor:** `loma e lok bra [kitchen] ket` — she eats in the kitchen
**Lexor:** `kompo e mod ke martelo o` — she fixes it by hammering it

**Gloss:**
- `tep` at/in (point in time), `lok` at/in/on (spatial)
- `mod` manner / by means of
- The preposition takes its argument as a noun phrase or clause.

**What this demonstrates:**
- Prepositions are closed-class CVC roots.
- Time / place / manner modifiers sit at the end of the sentence by default (after verb, object, subject).
- For complex arguments, group with `bra … ket` (Level 16).

**Full spatial set:** `lok sub sur pok lat dor fas int kir dir oks tra` — 12 closed-class spatial relations covering under/over/near/beside/behind/front/between/around/toward/from/through.

**Full temporal set:** `tep pen sin lim ant pos` — at/during/since/until/before/after.

---

## L7 — Negation

**Lexor:** `no-loma e` — she doesn't eat (whole-predicate negation)
**Lexor:** `loma no-[apple] e` — she eats not-an-apple (object-scoped negation)
**Lexor:** `no-mag e [him]` — she is not greater than him

**Gloss:**
- `no-` is a prefix, phonologically bound to its host.
- Scopes over the immediately adjacent unit. Three positions = three meanings.

**What this demonstrates:**
- Negation is positionally explicit. No ambiguity between "she doesn't eat apples" and "she eats non-apples."
- One operator, not many. Lexor has no separate "anti-" / "non-" / "un-" — just `no-`.

**No lexical antonyms:**
- Lexor doesn't have an "opposite" marker. Antonyms like love/hate get distinct roots (`am` / `od`); `no-am` means "doesn't love," which is not the same as "hates."

---

## L8 — Questions

**Lexor:** `ka loma e` — does she eat? (yes/no)
**Lexor:** `loma ka` — what does she eat? (`ka` in the object slot)
**Lexor:** `loma [apple] ka` — who eats apples?
**Lexor:** `loma e tep ka` — when does she eat?
**Lexor:** `loma e lok ka` — where does she eat?
**Lexor:** `loma e mod ka` — how does she eat?
**Lexor:** `loma e kaw ka` — why does she eat?
**Lexor:** `loma e, ka` — she eats, right? (tag question)

**Gloss:**
- `ka` is the universal question particle.
- Position determines question type: initial = yes/no, in-slot = wh, after-preposition = role-question.

**What this demonstrates:**
- One particle covers all interrogatives — no `who`/`what`/`when`/`where`/`why`/`how` lexical sprawl.
- Tag questions just append `, ka` to an assertion.

---

## L9 — Subordinate clauses

**Lexor:** `[man] ke loma [apple]` — the man who eats apples (relative clause)
**Lexor:** `[apple] ke loma e` — the apple that she eats (relative, gap = object)
**Lexor:** `dike e ke loma u` — she says that you eat (complement clause)
**Lexor:** `golo e tep ke pluvex` — she left when it was raining (temporal clause)
**Lexor:** `golo e kaw ke pluvo` — she left because it rained (causal clause)

**Gloss:**
- `ke` is the universal complementizer.
- Function determined by what *precedes* `ke`: a noun → relative clause; a speech verb → complement; a preposition → adverbial.

**What this demonstrates:**
- One subordinator covers what English uses 8+ words for (who/which/that/when/while/whereas/because/although).
- Relative-clause "gap" (the missing role in the embedded clause) is the modified noun. Role-vowel marks the gap when it's non-default.

---

## L10 — Conditionals

**Lexor:** `is pluve, lomy e [inside]` — if it's raining, she would eat inside
**Lexor:** `is no-pluve, goly e` — if it isn't raining, she would go

**Gloss:**
- `is` is the conditional particle (causal/temporal "if").
- The consequent verb takes the conditional vowel `y`.

**What this demonstrates:**
- Causal conditional (`is`) is a different beast from logical implication (`imp`, see L12) — English's "if" overloads both; Lexor splits them.

---

## L11 — Coordination

**Lexor:** `loma [apple] e kun bibe [water] e` — she eats an apple and drinks water
**Lexor:** `loma [apple] e vel loma [pear] e` — she eats an apple or a pear

**Gloss:**
- `kun` AND, `vel` OR (Latin *cum* / *vel*).
- Coordinators keep clause depth constant — they continue the current clause with another predication.

**What this demonstrates:**
- Pure-AND and pure-OR sequences are flat and unambiguous.
- Mixed AND/OR (`A and B or C`) is **forbidden in flat form** — speakers must group with `bra … ket` (Level 16) to disambiguate.

---

## L12 — Reasoning chains

**Lexor:** `dat pluvo. golo e kaw ke pluvo. erg sta sus-s [floor]` — Given it rained. She left because it rained. Therefore the floor is wet.
**Lexor:** `dat pluvo imp sta sus-s [floor]. no-sta sus-s [floor]. erg no-pluvo` — Modus tollens: given rain implies wet-floor; the floor is not wet; therefore it didn't rain.

**Gloss:**
- `dat` premise / given that
- `erg` therefore / inference
- `imp` formal logical implication (distinct from `is` causal conditional)

**What this demonstrates:**
- Multi-step reasoning uses *staged sentences* — each premise / observation / conclusion is its own sentence. No nested conditionals.
- The three reasoning markers (`dat`, `erg`, `imp`) are discourse-level — they're how Lexor does proofs, arguments, and structured thought.

---

## L13 — Modal operators (possibility, necessity)

**Lexor:** `kan pluve` — it might rain (possibility, ◇)
**Lexor:** `mus pluve` — it must be raining (necessity, □)
**Lexor:** `no- mus sam a b` — "not necessarily a = b" (the elusive English reading)
**Lexor:** `kan no- sam m1 m2` — "possibly m1 ≠ m2" (= "the masses can be different")

**Gloss:**
- `kan` epistemic possibility — English/German *can*/*kann*.
- `mus` epistemic necessity — English/German *must*/*muss*.
- Both sentence-initial. Both compose with `no-` for the four corners.

**What this demonstrates:**
- The "can be different" / "doesn't have to equal" / "may or may not be" readings that English collapses are all distinct surface shapes in Lexor.
- Epistemic flavor only — deontic permission/obligation are separate concepts not yet locked.

---

## L13b — Graded probability

**Lexor:** `chan zo dem ne zo pluve` — it will rain with probability 0.90
**Lexor:** `chan zo dem fi sam a b` — a equals b with probability 0.5
**Lexor:** `chan mag zo dem fi pluve` — probability of rain is greater than 0.5
**Lexor:** `chan zo dem ne zo X dat Y` — P(X | Y) = 0.9 (conditional probability via `dat`)

**Gloss:**
- `chan` — graded probability marker, sentence-initial.
- Form: `chan <number> <proposition>`. Number in [0, 1] = the probability.
- Scalar version of `kan` (◇) and `mus` (□): `chan zo` ≡ `no- kan` (impossible), `chan pa` ≡ `mus` (certain).
- Mnemonic: English/French *chance*.

**What this demonstrates:**
- Probability "sprinkles" onto any proposition. The infrastructure handles point probabilities, ranges (compose with `mag`/`min`/`tom`), and conditional probabilities (compose with `dat`).
- Distinct from amount-precision markers (`pir`/`tom`/`pem`) which scope over a *single magnitude*. `chan` scopes over the *whole proposition*. Different positions, no overload.
- No fuzzy probability words ("likely," "unlikely"). Speakers compose with explicit numbers or fall back on the binary modals.

---

## L14 — Axis system (direction, location, dimension)

**Lexor:** `gol aks fas mag e` — she goes forward
**Lexor:** `aks lat mag` — left (the +Y direction)
**Lexor:** `aks sur min` — down (the −Z direction)
**Lexor:** `tip aks sur mag bra [box] ket` — the top of the box (extreme point of +Z axis of box)
**Lexor:** `mez aks pa bra [box] ket` — the longest dimension of the box (object-frame, orientation-free)
**Lexor:** `mez aks sur bra [box] ket` — the height of the box (Z-axis magnitude, agent-frame)

**Gloss:**
- `aks` — axis (1D directed line). Combines with spatial preposition for agent-frame (`aks fas` = X), or with digit for object-rank (`aks pa` = longest).
- `tip` — endpoint / extremum along an axis.
- `mez` — dimensional magnitude (length along an axis).
- `mag`/`min` — polarity (positive / negative end of an axis).

**Coord system (locked):** X forward, Y left, Z up, right-handed.

**What this demonstrates:**
- "Up" the direction vs "top" the location vs "height" the magnitude are three structurally distinct shapes. No overload.
- Object-intrinsic dimensions (`aks pa/du/re`) don't presume orientation — works for a box lying on its side.

---

## L15 — Angles

**Lexor:** `rot zo doz re aks sur e` — she turns 90° left (1/4 revolution around Z)
**Lexor:** `rot zo doz sa aks sur e` — she turns around (180°)
**Lexor:** `rot min zo doz re aks sur e` — she turns 90° right (negative 1/4)
**Lexor:** `rot zo doz pa aks lat e` — she tilts forward 30° (1/12 around Y)
**Lexor:** `sam zo doz sa rota bra his approach ket aks sur` — his angle of approach is 180° around Z

**Gloss:**
- Angles are *fractions of a full revolution*. No degrees, no radians, no unit suffix — the number IS the count.
- Dozenal is the natural base: `zo doz pa` = 1/12 (30°), `zo doz re` = 1/4 (90°), `zo doz sa` = 1/2 (180°), `zo doz pa sa` = 0.16 doz = 1/8 (45°).
- Sign: positive = right-handed around the named axis. For `aks sur` (Z), positive = counterclockwise from above = leftward turn (the clock analogy is flipped).

**What this demonstrates:**
- "12 o'clock = 0 revs, 9 o'clock = +0.25, 6 o'clock = +0.5, 3 o'clock = −0.25" — compositionally, no new vocabulary.
- The verb form (`rot <amount> aks <ax>`) and noun form (`rota <amount> aks <ax>`) share the same skeleton.

---

## L16 — Sub-constituent brackets

**Lexor:** `tom bra re ket bra ko zo zo ket e` — I can do between 3 and 400 (pushups)
**Lexor:** `bra loma A e kun loma B e ket vel loma C e` — (she eats A and eats B) or she eats C
**Lexor:** `loma A e kun bra loma B e vel loma C e ket` — she eats A and (eats B or eats C)

**Gloss:**
- `bra` opens a sub-constituent group, `ket` closes it.
- Each `ket` matches the nearest unmatched `bra` (standard nesting).

**What this demonstrates:**
- Brackets are required for mixed AND/OR — flat form is grammatically ill-formed.
- Brackets break the digit-stream auto-fuse rule, so `tom bra re ket bra ko zo zo ket` cleanly gives `tom` two distinct number arguments.
- Mnemonic: English "bracket" split into `bra` + `ket`.

---

## L17 — Named binding (`def`)

**Lexor:** `def var p loma A e kun loma B e. var p vel loma C e` — Let p = "she eats A and B." (p) or she eats C.
**Lexor:** `def var x sam [biggest prime ant pa zo zo]. mag var x fi zo` — Let x = the biggest prime before 100. x > 50.
**Lexor:** `nul def var x` — x is no longer bound (explicit retraction)

**Gloss:**
- `def var <name> <expression>` introduces a named binding.
- `var <name>` references it later.
- `nul def var <name>` retracts it; re-`def`ing the same name shadows.

**What this demonstrates:**
- For long expressions that would clutter the sentence, name them once and reuse.
- Scope is discourse-local (current conversation), not sentence-local.
- `def`'s real job is *naming for reuse*, not disambiguation (that's `bra/ket`'s job).

---

## L18 — Composing several features

A small worked text. Each sentence uses multiple earlier features.

### Scene: she might come, but won't eat unless we ask

```
kan vene e. is no-kan mus pet e ke loma, no-lomy e.
```

**Gloss line 1:** `kan` possibility · `vene` come-present · `e` she — "She might come."

**Gloss line 2:** `is` if · `no-kan` not-possible · `mus` necessary · `pet` ask · `e ke` she-that · `loma` eat · `,` · `no-lomy` not-eat-conditional · `e` — "If we can't necessarily ask her to eat, she would not eat."

(Stilted, but legal Lexor. Demonstrates modal + conditional + clause embedding composing without conflict.)

### Scene: pushup bet with bracketed range

```
dat dike e ke kan domi e bra rot bra re ket bra ko zo zo ket ket pushupn. erg lori e kaw ke no-kan.
```

**Translation:** "Given that she says she can do (between 3 and 400) pushups: therefore (she will cry) because (it is impossible)." — silly but exercises `dat`/`erg` reasoning, modal `kan`, sub-constituent brackets around a numerical range, and embedded clauses.

### Scene: navigation order

```
gol aks fas mag pa zo metr e. rot zo doz re aks sur e. gol aks fas mag fi metr e.
```

**Translation:** "Go forward 10 meters. Turn 90° left. Go forward 5 meters."

This is three crisp imperatives chaining motion, rotation, and motion. The axis system + angle convention gives a compact, unambiguous navigation language — useful in any context (driving instructions, robotics, game directions, military comms).

### Scene: epistemic hedge with measurement

```
kan sam re metr mez aks pa bra box ket. kan min. no-vis y i.
```

**Translation:** "The longest dimension of the box might be 3 meters. It might be less. I haven't seen it."

Demonstrates how modal `kan` lets a speaker hedge without lying. Compare to English "it's 3 meters... maybe? I don't know" which requires three separate clauses to convey the same hedging.

---

## Closing notes

- This walkthrough covers ~80% of the locked grammar. The remaining 20% is in `decisions.md` (settled choices) and `examples.md` (dense reference).
- Open design questions are tracked in `tasks.md`; unmet design goals are in `trials.md` (grep `\[.*, open\]`).
- The vocabulary is still mostly unwritten — every bracketed `[word]` above is a placeholder. The `frequencies.yaml` priority list drives the next vocab pass.

If a sentence-shape here parses two ways in your head, that's either a bug in the walkthrough or a real ambiguity worth filing as a `[trap]` trial in `trials.md`. Both are useful to flag.
