# Trials — language design test suite

Each entry exercises one capability or trap. The suite is both a regression set (each known natural-language ambiguity has a trial demonstrating Lexor disarms it) and a stretch set (ambitious cases that probe whether the design holds up).

## Tags
- `[trap]` — known ambiguity / failure from natural languages
- `[feature]` — required language capability
- `[stretch]` — ambitious case to validate the design holds up
- `[stress, open]` — edge case probing an open design question

## Statuses
- `passes` — Lexor renders this unambiguously; mechanism locked in decisions.md
- `open` — concept understood, no mechanism locked yet (see tasks.md)
- `parked` — deliberately deferred

Grep examples: `grep '\[trap, open\]' trials.md` for traps without a fix yet.

---

## A. Ambiguity disarmed by morphology and word order

### A1. Tube ends [trap, passes]
**English:** "Its tube ends were round."
**Trap:** Noun-noun-verb POS ambiguity. `[its tube ends]` (tube modifying ends) vs `[its tube] ends [...]` (ends as verb).
**Lexor:** `sta rons dita-tubas i-e` — "are-state round, the tube-ish ends, of-it."
**How:** Adjective suffix `-s` on `tube` is morphological — `tubas` cannot be a verb. Outer role-vowel on `dita` (patient noun from `dit`/end) marks it as a noun. POS is explicit.
**Related:** decisions.md derivation consonants (`-s` adjective), AGENTS.md roots-are-concept-level.

### A2. Password K and L [trap, passes]
**English:** "This password shall only use the letters K and L at the start."
**Trap:** Scope of `only` — applies to the letters (K and L nowhere else) or to the position (at-start is K-or-L exclusively).
**Lexor:** `sol` (only) attaches positionally to its immediately adjacent argument; three positions = three meanings. `sol` before the letter set vs `sol` before the position prepositional phrase yields distinct sentences.
**How:** decisions.md "operator scope: scopes over the immediately adjacent argument."
**Related:** decisions.md `sol` quantifier.

### A3. Diffuser-and-the-others [trap, passes]
**Spanish:** "Determinar el empuje específico, el impulso específico y el rendimiento isentrópico **del difusor**."
**Trap:** Does "del difusor" attach to the last item, or distribute over all three?
**Lexor:** `bra … ket` brackets pin the scope: `[empuje, impulso, rendimiento] del difusor` vs `empuje, impulso, [rendimiento del difusor]`. Modifier attaches to the immediately adjacent bracketed unit.
**How:** decisions.md sub-constituent grouping markers (2026-05-16).

### A4. 12 cities = NYC [trap, passes]
**English:** "The 12 cities marked in red have the same population as NYC."
**Trap:** Distributive (each city = NYC) vs collective (sum = NYC).
**Lexor:** `pad` (distributive) vs `mas` (collective) is a required mark; the unmarked form means "speaker not committing." Three forms, three meanings.
**How:** decisions.md distributive vs collective.

### A5. "I have 10 dollars" — exactly vs at-least [trap, passes]
**English:** "I have 10 dollars." — total = 10? Or possess ≥ 10?
**Lexor:** `sam` (equals) vs `mag` (greater) vs unmarked range. `hav pa zo dolar e` is "I have ten dollars" with quantifier `sam pa zo` (exactly 10) or `mag pa zo` (at least 10).
**How:** decisions.md comparison-operator quantifiers.

### A6. "Rotations between 001, z axis, origin" — apposition vs list [trap, passes]
**English:** "Returns a list of rotations between 001, the z axis in object frame, and the origin system."
**Trap:** Three entities or two-with-apposition.
**Lexor:** `def var z 001. lis rot int var z kun origin` — naming the apposed thing breaks the list/apposition collision. Or: `bra 001 sam [z axis in object frame] ket` brackets the apposition explicitly.
**How:** decisions.md `def`-binding, `bra/ket` grouping, `sam` identity copula.

### A7. "Password with no spaces and |" — coordinator vs conjunction [trap, passes]
**English:** "Write a password with no spaces and |."
**Trap:** Is `|` allowed (and = "separator between rules") or forbidden (and = "AND no |")?
**Lexor:** `kun` (AND) only coordinates same-depth predications; doesn't sit inside a `no-` scope without explicit re-application. To forbid both: `no-spas kun no-pipe`. To present as separator: clause break + sentence boundary.
**How:** decisions.md coordinators `kun`/`vel`, depth rule.

### A8. Between 3 and 400 pushups [trap, passes]
**English:** "I bet I can do between three and four hundred pushups." — 3 to 400, or 300 to 400?
**Lexor:** `tom bra re ket bra ko zo zo ket` — brackets pin each numeric argument. Without them, the digit-stream auto-fuse rule would merge `re ko zo zo` into one number.
**How:** decisions.md sub-constituent grouping markers, digit-stream rule.

### A9. Mean sea level [trap, open]
**English:** "Mean sea level."
**Trap:** Mean over which dimension? Default reading is spatial; actual definition is temporal-at-each-point.
**Lexor goal:** Make "mean over X" require explicit X. Either via preposition-on-mean (`med tep` = temporal mean, `med lok` = spatial mean) or via a more general modifier-attachment rule.
**Status:** No "mean" root locked yet; the preposition-on-aggregator pattern is consistent with existing decisions but not formalized.
**Related:** tasks.md modifier-attachment for aggregators.

---

## B. Negation, modality, possibility — distinguishing what English collapses

### B1. not(a = b) vs a ≠ b [trap, passes]
**English:** "a is not equal to b" — never equal, or "doesn't have to equal"?
**Lexor:**
- Assertion of inequality: `no- sam a b` (a ≠ b, claimed).
- "a doesn't necessarily equal b": `no- mus sam a b` (¬□ a=b).
- "a may or may not equal b": `kan no- sam a b` (◇ a≠b).
**How:** decisions.md modal operators `kan`/`mus` (2026-05-16).

### B2. "Masses can be different" [trap, passes]
**English:** "The masses can be different" — speaker is not committing on whether they actually are.
**Lexor:** `kan no- sam m1 m2` — "possibly m1 ≠ m2." Speaker explicitly does not commit to the inequality holding.
**How:** decisions.md modal operators (2026-05-16).

### B3. Tense when uncertain [trap, passes]
**English:** Speaker isn't sure if it happened, is happening, or will happen, but must commit to a tense.
**Lexor:** Atemporal vowel `a` is the default — speaker is explicitly not committing to a temporal frame. `loma e` = "she eats" with no time commitment.
**How:** decisions.md atemporal default `a` (2026-05-15).

---

## C. Copula and "is"-overload — splitting what English collapses

### C1. "The electron is at position x" [trap, passes]
**English:** "Is at" — claims a definite location, but in quantum contexts location is observation-dependent.
**Lexor:** `sta lok-x i` (state at-location-x) vs `est lok-x i` (essence at-location-x). Pre-measurement particles are in superposition — neither holds definitively. Use `kel` (possibility) over the state predicate.
**How:** decisions.md "is"-overload split (sam/est/sta/mem/lit-fin).

### C2. "The password is incorrect" [trap, passes]
**English:** Predication ("has property wrong") vs literal-string-identity ("password = the word 'incorrect'").
**Lexor:** `sta no-korek-s [password]` (state-of-being-incorrect) vs `sam lit incorrect fin [password]` (identity with the literal string).
**How:** decisions.md `lit … fin` paired literal markers.

### C3. "My name is very stupid" [trap, passes]
Same shape as C2.
**Lexor:** `est stupid-s [name]-y` (my name is essentially stupid) vs `sam lit very stupid fin [name]-y` (my name literally is the string).
**How:** As C2.

### C4. "A whale is a mammal" [trap, passes]
**English:** Identity? Membership? Subset?
**Lexor:** `mem mamal whal` (whale ∈ mammals). Not `sam`. Not `est`.
**How:** decisions.md "is"-overload, `mem` membership.

### C5. "Mammals are animals" [trap, passes]
**English:** Subset (mammals ⊆ animals) vs membership-of-the-class.
**Lexor:** `tot mamal mem animal` (every mammal is-member-of animals). Composed from `tot` + `mem`; no dedicated subset particle.
**How:** decisions.md subset by composition.

### C6. "There is a god" [trap, passes]
**English:** "Is" overloads existence and predication.
**Lexor:** `kel dios` (some/exists god). No copula needed.
**How:** decisions.md existence by composition with `kel`.

### C7. "She is a doctor" vs "she is tired" [trap, passes]
**English:** Permanent property vs current state.
**Lexor:** `est doktor e` (essence: doctor) vs `sta tem-s e` (state: tired).
**How:** decisions.md "is"-overload, ser/estar split.

---

## D. Quantifier, scope, and number expression

### D1. Single-syllable digits [feature, passes]
**Capability:** Every digit 0–B is one syllable. Numbers concatenate.
**Trial:** "1408" → `pa ko zo bo` (CV per digit, one prosodic unit).
**How:** decisions.md digit roots, prosody.

### D2. Numbers in any base [feature, passes]
**Capability:** Decimal and dozenal first-class. Other bases compositional.
**Trial:** 6.5₁₀ = `sa dem fi`; 6.5₁₂ (= 6.4166₁₀) = `sa doz fi`.
**How:** decisions.md `dem`/`doz` base markers.

### D3. Scientific notation [feature, passes]
**Capability:** Universal magnitude expression; no million/billion arms race.
**Trial:** 1.5 × 10² = `pa dem fi pem du`.
**How:** decisions.md `pem` scale marker.

### D4. Range and approximation [feature, passes]
**Capability:** Express "from A to B," "around X," "X ± Y" without special syntax.
**Trial:** "Around 7" = `pir chi`; "from 2 to 9" = `tom du ne`; "7 +2 -5" composes from these.
**How:** decisions.md comparison operators `min`/`mag`/`sam`/`tom`/`pir`.

### D5. Distribution shape [feature, open]
**Capability:** Probabilistic distributions (gaussian, uniform, bimodal) compositional.
**Status:** Parked. tasks.md distribution-shape roots.

### D6. Plug-in probability [feature, open]
**Capability:** "90% likely to rain" reads as cleanly as "5 cm."
**Status:** Path clearer after modal-operators land. Possible surface forms: `kan pir [number]` (possibly to approximate degree N) or `[number] dem kan X` (X with degree-N possibility). Specific shape parked for follow-up round.
**Related:** D5, modal operators 2026-05-16.

### D7. Exactly vs at-least [feature, passes]
See A5.

### D8. Every / each / all / some / none [feature, passes]
**Capability:** Universal/existential quantifiers, plus distributive/collective markers.
**Trial:** `tot` ∀, `kel` ∃, `nul` ∅, `sol` only, `pad` each, `mas` together.
**How:** decisions.md universal-quantifier family.

### D9. Bare ratio (not percent) [feature, open]
**Capability:** Symbol/word for "ratio of X to Y" that doesn't carry the ×100 of `%`.
**Status:** Open. Composable solution: `re tom pa zo` (3 out of 10) works but is verbose.

### D10. Approximation/eyeballed marker [feature, open]
**Capability:** A short mark that says "rough estimate."
**Trial goal:** "I got 4 h of sun in 1 h" without sounding like a lie.
**Status:** Open. `pir` (approximately) covers part of this but is a number-comparison operator, not a "this whole statement is eyeballed" marker.

---

## E. Coordination and reasoning

### E1. Mixed AND/OR grouping [feature, passes]
**Capability:** `(A and B) or C` distinguishable from `A and (B or C)`.
**Trial:** `bra loma A e kun loma B e ket vel loma C e` = "(A and B) or C".
**How:** decisions.md `bra/ket` brackets (2026-05-16); flat mixed form forbidden.

### E2. Formal logical implication vs causal conditional [feature, passes]
**Capability:** Distinguish "A entails B" (axiom-like) from "if A happens, B happens" (everyday).
**Trial:** `A imp B` (formal) vs `is A, B` (causal).
**How:** decisions.md causal-conditional vs logical-implication split.

### E3. Multi-step reasoning [feature, passes]
**Capability:** Premises → inference, chainable.
**Trial:** `dat A imp B. no-B. erg no-A.` (modus tollens, three crisp sentences).
**How:** decisions.md reasoning-particle set `dat`/`erg`/`imp`.

### E4. Proof structuring [feature, open]
**Capability:** "Suppose for contradiction," "QED," case-splitting.
**Status:** Parked. tasks.md proof-structuring particles.

---

## F. Pronouns and reference

### F1. "We" with explicit member set [feature, passes]
**Capability:** Distinguish just-you-and-me / you-me-and-others / me-and-others-not-you / generic-we.
**Trial:** `le` (you+me), `lc` (we inclusive of others), `lu` (me+third, no listener), `la` (generic).
**How:** roots.md pronouns.

### F2. "You" singular vs plural [feature, passes]
**Capability:** Tú ≠ vosotros.
**Trial:** `u` (sg) vs `ly` (pl).
**How:** roots.md pronouns.

### F3. Gender-neutral default [feature, passes]
**Capability:** Refer to a person without gender commitment.
**Trial:** `e` covers he/she/they regardless of gender. No mandatory gender marker exists in the grammar.
**How:** AGENTS.md no-mandatory-marking meta-principle.

### F4. Pronoun-less impersonal [feature, passes]
**Capability:** "It has been decided to do this" without dummy subjects.
**Trial:** Bare verb without subject argument: `decisu lit do this fin` ≈ "decided-perfect [literal: do this]". No `e`, no agent required.
**How:** decisions.md VOS with optional subject.

### F5. Unspecified-addressee [feature, open]
**Capability:** Calling out to someone unnamed (asking for help in a group).
**Status:** No dedicated vocative; could compose `ka u-i` ("hey you-instrumental"?) or designate a root. Parked.

---

## G. Spatial and directional

### G1. Full spatial-preposition family [feature, passes]
**Capability:** 12 closed-class spatial relations covering under/over/near/beside/behind/front/between/around/toward/from/through.
**How:** decisions.md spatial-preposition family (2026-05-16).

### G2. Rotation by axis [feature, passes]
**Capability:** Roll / pitch / yaw compositional from rotate-verb + axis preposition.
**Trial:** `rot fas` (roll), `rot lat` (pitch), `rot sur` (yaw).
**How:** decisions.md rotation names (2026-05-16).

### G3. Direction-sense ("sentido") [feature, open]
**Capability:** Two-direction-along-one-axis distinction without two separate words.
**Trial goal:** "Forward" and "backward" share a root; vowel distinguishes the sense.
**Status:** Open; no axis-with-polarity-marker root family yet.

### G4. Direction vs location [feature, open]
**Capability:** "Up" (direction) ≠ "top" (location), but possibly same root.
**Status:** Open. Probably composes from existing spatial preps + a direction-marker, but the marker isn't designed yet.

### G5. Neutral axis names (length / width / height) [feature, open]
**Capability:** Talk about "longest dimension," "shortest dimension" without picking an orientation.
**Trial goal:** "Longest-axis 3 m, shortest 1 m" works for any object regardless of how it's standing.
**Status:** Open. Needs an axis-by-rank-not-by-orientation root.

---

## H. Predication that English needs adverbs/circumlocutions for

### H1. Anti-adjective / inclusive marker [feature, open]
**English:** "A lot or a little," "more or less," "like it or not."
**Trial goal:** One short word that says "irrespective of magnitude/polarity."
**Status:** Open. Possibly composes from `tot` (universal) + the modifier axis.

### H2. Taper ratio / neutral magnitude term [feature, open]
**Capability:** A noun for the magnitude axis (e.g., "weight," "temperature") with no implied direction. Adjective specifies direction.
**Trial goal:** Talk about a 0–1 ratio where 0 = maximum tapering, without the value-meaning inversion.
**Status:** Open. Requires both an axis-noun policy and explicit direction-suffix.

### H3. Pixels-per-mm vs mm-per-pixel [trap, passes]
**English:** "Higher resolution" ambiguous: more pixels per area, or finer detail per pixel.
**Lexor:** Express the ratio explicitly with units: `pixel kex milimet` (pixels per mm) vs `milimet kex pixel`. No "resolution" as a monolithic term unless followed by the unit.
**How:** decisions.md frequency operator `kex` reused for "per."

### H4. Source of information / evidentiality [feature, open]
**English:** "I heard that..." optional and inconsistent.
**Trial goal:** Cherokee-style suffix on verbs marking saw-it / heard-it / inferred-it.
**Status:** Open. Could be a closed-class suffix CV; reserved-slot work parked.

### H5. Apposition / "and that one is..." [trap, passes]
See A6.

---

## I. Stretch goals

### I1. Express Lexor in Lexor [stretch, open]
**Goal:** Self-bootstrap. Write decisions.md, this file, examples.md in Lexor.
**Why:** Validates the language is expressive enough for its own meta-discourse.
**Status:** Parked in checklist; tracked in tasks.md.

### I2. Quantum superposition [stretch, passes]
**Goal:** Express "the particle's position is in superposition over X and Y" without smuggling in a definite location.
**Lexor:** `kan lok-x i kun kan lok-y i kun no- mes` = "possibly at x AND possibly at y AND no measurement." Each location is modal-possible, not asserted-state.
**How:** decisions.md modal operators (2026-05-16).

### I3. Pronoun-less paragraph [stretch, passes]
**Goal:** Three consecutive sentences with no explicit subject, no awkwardness.
**Trial draft:** Forming a paragraph that flows pronoun-free. Doable with VOS-optional-subject grammar; just needs example writing.
**Status:** Mechanism passes; specific paragraph not yet written.

### I4. Long mathematical statement [stretch, passes]
**Goal:** "For every prime p > 2, there exist integers a, b with p = a² + b² iff p ≡ 1 (mod 4)."
**Status:** Mechanism (quantifiers + def-binding + reasoning particles) exists. Full rendering parked until vocabulary covers "prime," "integer," "mod."

### I5. Multi-paragraph discourse with discourse-local def [stretch, open]
**Goal:** Long-form text where def-bindings introduced once are referenced across paragraphs.
**Status:** Scope rules for def-binding are discourse-local but the boundary isn't formally tested.

### I6. Composable comparator across adjectives [stretch, open]
**Goal:** "Less pretty" / "uglier" expressible without a separate antonym root.
**Status:** Open. Discussed and rejected in decisions.md (lexical-opposite marker), so this trial is *expected to fail* — the deliberate cost of the no-opposite-marker decision. Logged here to make that cost visible.

### I7. "Yo voy el sábado" — fronting and topicalization [stretch, open]
**Goal:** Distinguish "the day I'm going is Saturday" from "Saturday I'll go (possibly other days too)."
**Status:** Open. Topicalization conventions parked in tasks.md.

### I8. Place chaining ("Spain, Madrid, Fuenlabrada, URJC, Building B") [stretch, open]
**Goal:** Compact nested-location expression that isn't a list.
**Status:** Open. Probably composes from spatial prepositions but the convention isn't locked.

### I9. Variable position swap (evaluate_classifiers vs classifier_evaluator) [stretch, open]
**Goal:** Compact way to flip the head noun in a derived compound (the action vs the actor).
**Status:** Lexor's role-vowel and derivation-suffix system probably already handles this (`lekr` reader vs `lekn` reading vs `lekt` thing-read), but the test case hasn't been worked through.

---

## J. Stress tests (probing open questions)

### J1. Deeply nested clauses [stress, open]
**Goal:** Sentence with 4+ levels of `ke`-clause nesting; does it parse without `def`-binding?
**Status:** Style rule says use `def`-binding past ~2 levels. Stress test would push past it deliberately to confirm the rule's necessity.

### J2. Long digit stream [stress, open]
**Goal:** A 12-digit number — does prosodic concatenation hold up at length?
**Status:** Untested. Phonetics.md says no internal break in digit streams; long streams not yet tried.

### J3. Mixed bases in one sentence [stress, open]
**Goal:** "6.5 in dozenal equals 6.4166 in decimal" — both base markers in one breath.
**Status:** Should work compositionally; not yet exercised.

### J4. Ambiguity-by-omission [stress, open]
**Goal:** Construct a sentence where omitting an optional marker creates ambiguity, to confirm Lexor's rule "unmarked has one canonical meaning."
**Status:** Untested. The grammar promises this is impossible; a failed attempt to construct one would be the proof.

---

## How to use this file

1. **Adding a trial:** copy a template entry. Tag honestly. If the status is `open`, link to the relevant `tasks.md` item so the design gap is tracked.
2. **Closing a trial:** when a decision lands that disarms a trap or unlocks a feature, change the status to `passes` and add a `How:` line pointing to the decision.
3. **Trials and tests aren't sacred:** if a trial reveals the trial itself was wrong, edit or delete. The point is to keep the design auditable, not to preserve every entry.
4. **Auditing the design:** `grep '\[.*, open\]' trials.md` shows every unmet goal. `grep '\[trap, passes\]' trials.md` shows every natural-language ambiguity Lexor has formally answered.
