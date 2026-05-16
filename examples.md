# Examples

Worked sentence translations. Goal: validate the grammar by writing realistic sentences with the locked machinery and surface gaps before more vocabulary is committed.

## Conventions
- Content roots that haven't been formally locked yet are written in brackets: `[apple]`, `[house]`, `[man]`, `[water]`. Their exact CVC form will be picked during the vocabulary buildout; the sentences here exercise *structure*, not lexicon.
- Roots used as working assumptions but not yet in roots.md are noted at first use: `pluv` (rain, from Latin *pluere*), `bib` (drink, from Latin *bibere*), `dik` (say, from Latin *dicere*).
- VOS = verb, object, subject. Role-vowel suffixes (`-e` subject, `-o` object, `-u` recipient, `-i` instrument) are only attached when default position would be ambiguous.

## 1. Basic VOS and tense

1. `loma e` — "She eats." (atemporal — habit, general fact, no specific time)
2. `lome e` — "She is eating." / "She eats right now." (present)
3. `lomo e` — "She ate." (past)
4. `lomi e` — "She will eat." (future)
5. `lomex e` — "She is eating." (present continuous, aspect `x` on present)
6. `lomu` — "Eat!" (imperative; subject usually elided)
7. `lomy e` — "She would eat." (conditional)
8. `loma [apple] e` — "She eats an apple." (VOS: verb, object, subject)

## 2. Role vowels (when position alone is ambiguous)

9. `loma [apple]-o e-e` — same as #8, explicit roles. Use when object/subject swap would be plausible from context.
10. `dake [apple]-o e-e u-u` — "She gives an apple to you." (recipient `u` marked because three-argument verb)
11. `pere [door]-o e-e [key]-i` — "She opens the door with a key." (instrument `i`)

## 3. Negation

12. `no-loma e` — "She doesn't eat." (logical negation, scope = entire predicate)
13. `loma no-[apple] e` — "She eats not-an-apple." (scope = object only)
14. `no-mag e [him]` — "She is not greater than him."

## 4. Quantifiers

15. `loma [apple] re e` — "She eats three apples." (quantifier follows noun)
16. `loma [apple] re pad e` — "She eats three apples, each one (distributive)."
17. `loma [apple] re mas e` — "She eats three apples together (collective)."
18. `loma [apple] tot e` — "She eats every apple." (universal quantifier)
19. `loma [apple] kel e` — "She eats some apple." (existential)
20. `loma [apple] nul e` — "She eats no apple." (none)
21. `loma [apple] sol re e` — "She eats only three apples." (restriction + count)

## 5. Numbers and time

22. `loma [apple] re tep [yesterday]` — "She ate three apples yesterday." (composing: `ant pa dim` = yesterday literally, but commonly the unit-time expression)
23. `lome e kex dim` — "She eats every day." (frequency operator)
24. `loma [apple] pa fi pem du` — "She eats 1.5×10² = 150 apples." (digit stream + base + scale)
25. `loma [apple] re tom fi e` — "She eats between three and five apples." (range)
26. `pluvex tep nun` — "It is raining right now." (using time-root `nun` = now)

## 6. Questions

27. `ka loma e` — "Does she eat?" (yes/no question; `ka` sentence-initial)
28. `loma ka` — "What does she eat?" (`ka` in the object slot)
29. `loma [apple] ka` — "Who eats apples?" (`ka` in the subject slot)
30. `loma e tep ka` — "When does she eat?"
31. `loma e lok ka` — "Where does she eat?"
32. `loma e mod ka` — "How does she eat?"
33. `loma e kaw ka` — "Why does she eat?"
34. `ka loma [apple] vel loma [pear] e` — "Does she eat an apple or a pear?" (choice question)
35. `loma e, ka` — "She eats, right?" (bare tag)
36. `loma e, ka no-loma e` — "She eats, doesn't she?" (echo tag, explicit polarity)

## 7. Subordinate clauses

37. `[man] ke loma [apple]` — "the man who eats apples" (relative clause, gap = subject of `loma`)
38. `[apple] ke loma e` — "the apple that she eats" (relative, gap = object)
39. `dike e ke loma u` — "She says that you eat." (complement clause, `dike` = "says")
40. `golo e tep ke pluvex` — "She left when it was raining." (temporal clause)
41. `golo e lok ke [house]` — "She left where the house is." (spatial clause; reads as "at-WHERE house [is]")
42. `golo e kaw ke pluvo` — "She left because it rained." (causal clause)
43. `kompo e mod ke martelo o` — "She fixed it by hammering it." (manner clause)

## 8. Conditionals

44. `is pluve, lomy e [inside]` — "If it's raining, she would eat inside." (conditional `is` + consequent in conditional `y`)
45. `is no-pluve, goly e` — "If it isn't raining, she would go." (negated antecedent)

## 9. Coordination and depth

46. `loma [apple] e kun bibe [water] e` — "She eats an apple and drinks water." (AND, same depth)
47. `loma [apple] e vel loma [pear] e` — "She eats an apple or a pear." (OR)
48. Mixed AND/OR uses sub-constituent brackets `bra … ket`:
    - `bra loma A e kun loma B e ket vel loma C e` — "(A and B) or C."
    - `loma A e kun bra loma B e vel loma C e ket` — "A and (B or C)."
    - The old `def`-binding rewrite still works (`def var p loma A e kun loma B e. var p vel loma C e`) but is reserved for naming a sub-expression for later reuse, not just disambiguation.

48a. Numerical-range disambiguation (the `bra … ket` motivating case):
    - `tom bra re ket bra ko zo zo ket e` — "between 3 and 400 (pushups)." Without brackets, `tom re ko zo zo` would fuse all four digits into `rekozozo` (= 3400) and `tom` would be missing its second argument — ill-formed.
    - `tom bra re zo zo ket bra ko zo zo ket e` — "between 300 and 400." Always bracket both arguments; never trust the digit-stream rule to split a multi-number expression on its own.

## 9b. Epistemic modality (kan / mus)

49a. `kan pluve` — "It might rain." / "Possibly it rains." (◇)
49b. `mus pluve` — "It must be raining." / "Necessarily." (□)
49c. `no- mus sam m1 m2` — "Not necessarily m1 = m2." (English's elusive "doesn't have to equal" reading)
49d. `kan no- sam m1 m2` — "Possibly m1 ≠ m2." (the "can be different" reading without claiming they actually are)
49e. `kan lok-x i kun kan lok-y i kun no- mes` — "Possibly at-x AND possibly at-y AND no measurement." (quantum superposition without smuggling in a definite location)
49f. `dik e ke kan pluve` — "She says that it might rain." (modal inside a complement clause)

## 9c. Axis system (aks / tip / mez)

49g. `aks fas` — "the X axis (forward-back axis, agent-frame)."
49h. `aks sur mag` — "upward direction" (Z axis, + polarity).
49i. `aks sur min` — "downward direction" (Z axis, − polarity).
49j. `gol aks fas mag e` — "She goes forward." (motion verb + direction)
49k. `tip aks sur mag bra box ket` — "the top of the box" (extreme point at +Z end of the box).
49l. `sta sus tip aks sur mag bra box ket` — "the top of the box is dirty."
49m. Contrast: `sur box` (relational: somewhere above the box) vs `tip aks sur mag bra box ket` (intrinsic: the top extreme of the box itself).
49n. `mez aks sur bra box ket` — "the height of the box" (magnitude along Z axis).
49o. `sam re metr mez aks pa bra box ket` — "the longest dimension of the box equals 3 meters." (Object-frame, orientation-free.)
49p. `aks fas mag bra trafik ket` — "the (forward) direction of the traffic flow" (sentido, polarized).
49q. Object-frame ranks: `mez aks pa` (longest dimension), `mez aks du` (middle), `mez aks re` (shortest). Doesn't presume orientation.

## 9d. Angles (fractions of a revolution)

49r. `rot zo doz re aks sur e` — "She turns 90° left." (Rotate by 1/4 = `zo doz re` = 0.25 around Z, positive direction.)
49s. `rot zo doz sa aks sur e` — "She turns around (180°)." (1/2 revolution around Z.)
49t. `rot zo doz pa aks lat e` — "She tilts forward 30°." (1/12 revolution around Y, the lateral axis.)
49u. `rot min zo doz re aks sur e` — "She turns 90° right." (Negative quarter rev around Z.)
49v. `sam zo doz sa rota bra his approach ket aks sur` — "His angle of approach is 180° around Z." (Noun form via `rota`.)
49w. Cardinal vs angular reference points around Z, starting from forward (+X = "12 o'clock"):
   - 12 o'clock (forward): `aks fas mag` (cardinal) or `rota zo aks sur` (angle 0).
   - 9 o'clock (left): `aks lat mag` (cardinal) or `rota zo doz re aks sur` (angle 1/4 = 0.25 dec = 0.3 doz).
   - 6 o'clock (back): `aks fas min` (cardinal) or `rota zo doz sa aks sur` (angle 1/2).
   - 3 o'clock (right): `aks lat min` (cardinal) or `rota min zo doz re aks sur` (angle −1/4).
49x. Non-cardinal "1:30 o'clock" (45° clockwise from 12) = `rota min zo doz pa sa aks sur` ≈ "rotation of −1/8 around Z."

## 9e. Graded probability (chan)

49y. `chan zo dem ne zo pluve` — "It will rain with probability 0.90." (90% likely)
49z. `chan zo dem fi sam a b` — "a equals b with probability 0.5." (Coin-flip uncertainty.)
49aa. `chan zo dem pa pluve` — "It'll rain with probability 0.1." (Unlikely.)
49bb. Equivalences:
    - `chan zo X` ≡ `no- kan X` — P = 0 = impossible.
    - `chan pa X` ≡ `mus X` — P = 1 = certain.
    - `kan X` ≈ `chan <unspecified positive> X` — speaker not committing to a specific value.
49cc. Probability ranges (compose with comparison operators):
    - `chan mag zo dem fi pluve` — "P(rain) > 0.5" (more likely than not)
    - `chan min zo dem du fi pluve` — "P(rain) < 0.25"
    - `chan tom zo dem du fi zo dem chi fi pluve` — "P(rain) is between 0.25 and 0.75"
49dd. Probability comparison: `mag chan pluve chan ne` — "rain is more likely than snow" (chance-of-rain > chance-of-snow).
49ee. Conditional probability: `chan zo dem ne zo pluve dat sta nub-s [sky]` — "P(rain | sky is cloudy) = 0.9" (conditional via `dat`).
49ff. `kan sam re metr mez aks pa bra box ket. chan zo dem chi fi sam re metr. no-vis y i` — "The longest dimension of the box might be 3 meters. It's probably 3 meters (P = 0.75). I haven't seen it." (Hedging with mixed modals.)
49gg. Distinction from amount-precision:
    - `hav pir pa zo [apple] e` — "She has approximately 10 apples." (`pir` on the amount.)
    - `chan zo dem chi fi hav pa zo [apple] e` — "She probably has 10 apples." (`chan` on the proposition.)
    - These are different claims. `pir` says the amount is uncertain; `chan` says the whole statement is uncertain.

## 10. Reasoning chain

49. `dat pluvo` — "Given that it rained." (premise)
50. `dat pluvo. golo e kaw ke pluvo. erg [floor wet]` — "Given it rained. She left because it rained. Therefore the floor is wet."
51. Modus tollens: `dat pluvo imp [floor wet]. no-[floor wet]. erg no-pluvo` — "Given rain implies wet floor. The floor is not wet. Therefore it did not rain."

## 11. Copulas (the "is"-overload split)

52. `[Mark Twain] sam [Samuel Clemens]` — "Mark Twain is Samuel Clemens." (identity)
53. `est [blue] [sky]` — "The sky is blue." (essential predication)
54. `sta [tired] e` — "She is tired." (state predication, transient)
55. `mem [mammal] [whale]` — "A whale is a mammal." (set membership)
56. `tot [mammal] mem [animal]` — "Every mammal is an animal." (subset by composition)
57. `kel [problem]` — "There is a problem." (existence by composition)
58. `sam lit incorrect fin [password]` — "The password is (literally) 'incorrect'."
59. `sta [incorrect-property] [password]` — "The password is incorrect (= wrong)."

## 12. Literal and variable markers

60. `dike e lit thank you fin` — "She says, 'thank you'." (raw string content)
61. `sam lit Lexor fin [name-language]` — "The language's name is 'Lexor'."
62. `golo u tep var path. legu u var path` — "Go to var-path. Read var-path." (template; both occurrences = same slot)
63. `def var x sam [biggest prime ant pa zo zo]. mag var x fi zo` — "Let x = the biggest prime before 100. x > 50."
64. `def var f [function-expression]. kompe y var f mod var x` — "Let f = [function]. I apply f to x."
65. `nul def var x` — "x is no longer bound." (explicit retraction)

## 13. Composed bindings inside reasoning

66. `def var p [tot [whale] mem [mammal]]. dat var p. dat mem [whale] [moby]. erg mem [mammal] [moby]` — "Let p = 'every whale is a mammal'. Given p. Given Moby is a whale. Therefore Moby is a mammal."

---

## Observations and surfaced gaps

Working through these exposed the following:

1. **"Yesterday" / "tomorrow" composition feels clunky.** `tep ant pa dim` ("at one-day-before") is correct but mouthy compared to `tep [yesterday]`. May want a dedicated unit-shift composition convention or a small set of relative-time roots after all. Decision deferred.
2. **No locked roots for many high-frequency content words** — drink, water, door, key, apple, person, house, fix, hammer, read, function. Examples here rely on placeholder brackets. This is the next major work item (vocabulary arc, Session N+3+).
3. **VOS placement of full clauses** (e.g., `dike e ke loma u`) reads naturally: verb, subject, complement-clause. The complement is the object slot, but expressed as a `ke`-clause it sits after the subject — consistent with "subordinate clause follows its host."
4. **Embedded literal inside identity** (`sam lit incorrect fin [password]`) works but is heavy. For everyday quoted speech, the order `verb subject lit content fin` (as in #60, `dike e lit thank you fin`) is lighter because no copula is involved.
5. **`def`-binding inside reasoning chains** (#66) is the most powerful demonstration so far. Long premises become single tokens (`var p`); the chain stays readable.
6. **No problems found with prosody assumptions.** All examples parse uniquely under the brief-break / clause-break / sentence-break model.
7. **`kompo` / `kompe`** ("fix/repair") used as working root; needs vocab assignment.
8. **`pere` / `legu`** (open / read-imperative) — `pere` updated 2026-05-16 (root renamed `apr → per`). `legu` still using working-form spelling.

## Next examples to add (after vocabulary buildout)

- Full spatial-prepositions paragraph (under/over/near/beside) once that family is locked.
- Negative reasoning with multiple `dat` premises and case-splitting (need the parked proof-structuring particles first).
- Nested `def`s in a formal proof (need scope rules locked).
- Long natural-text paragraph (3–5 sentences) demonstrating discourse flow.
