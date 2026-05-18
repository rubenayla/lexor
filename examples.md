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
14. `no-magu e [him]` — "She is not greater than him."

## 4. Quantifiers

15. `loma [apple] re e` — "She eats three apples." (quantifier follows noun)
16. `loma [apple] re padu e` — "She eats three apples, each one (distributive)."
17. `loma [apple] re masu e` — "She eats three apples together (collective)."
18. `loma [apple] totu e` — "She eats every apple." (universal quantifier)
19. `loma [apple] kelu e` — "She eats some apple." (existential)
20. `loma [apple] nulu e` — "She eats no apple." (none)
21. `loma [apple] solu re e` — "She eats only three apples." (restriction + count)

## 5. Numbers and time

22. `loma [apple] re tepa [yesterday]` — "She ate three apples yesterday." (composing: `anta pa dima` = yesterday literally, but commonly the unit-time expression)
23. `lome e kexu dima` — "She eats every day." (frequency operator)
24. `loma [apple] pa fi pemu du` — "She eats 1.5×10² = 150 apples." (digit stream + base + scale)
25. `loma [apple] re tomu fi e` — "She eats between three and five apples." (range)
26. `pluvex tepa nuna` — "It is raining right now." (using time-root `nuna` = now)

## 6. Questions

27. `ka loma e` — "Does she eat?" (yes/no question; `ka` sentence-initial)
28. `loma ka` — "What does she eat?" (`ka` in the object slot)
29. `loma [apple] ka` — "Who eats apples?" (`ka` in the subject slot)
30. `loma e tepa ka` — "When does she eat?"
31. `loma e loka ka` — "Where does she eat?"
32. `loma e moda ka` — "How does she eat?"
33. `loma e kawa ka` — "Why does she eat?"
34. `ka loma [apple] vele loma [pear] e` — "Does she eat an apple or a pear?" (choice question)
35. `loma e, ka` — "She eats, right?" (bare tag)
36. `loma e, ka no-loma e` — "She eats, doesn't she?" (echo tag, explicit polarity)

## 7. Subordinate clauses

37. `[man] ke loma [apple]` — "the man who eats apples" (relative clause, gap = subject of `loma`)
38. `[apple] ke loma e` — "the apple that she eats" (relative, gap = object)
39. `dike e ke loma u` — "She says that you eat." (complement clause, `dike` = "says")
40. `golo e tepa ke pluvex` — "She left when it was raining." (temporal clause)
41. `golo e loka ke [house]` — "She left where the house is." (spatial clause; reads as "at-WHERE house [is]")
42. `golo e kawa ke pluvo` — "She left because it rained." (causal clause)
43. `kompo e moda ke martelo o` — "She fixed it by hammering it." (manner clause)

## 8. Conditionals

44. `isi pluve, lomy e [inside]` — "If it's raining, she would eat inside." (conditional `isi` + consequent in conditional `y`)
45. `isi no-pluve, goly e` — "If it isn't raining, she would go." (negated antecedent)

## 9. Coordination and depth

46. `loma [apple] e kune bibe [water] e` — "She eats an apple and drinks water." (AND, same depth)
47. `loma [apple] e vele loma [pear] e` — "She eats an apple or a pear." (OR)
48. Mixed AND/OR uses sub-constituent brackets `bra … keti`:
    - `bra loma A e kune loma B e keti vele loma C e` — "(A and B) or C."
    - `loma A e kune bra loma B e vele loma C e keti` — "A and (B or C)."
    - The old `defi`-binding rewrite still works (`defi vari p loma A e kune loma B e. vari p vele loma C e`) but is reserved for naming a sub-expression for later reuse, not just disambiguation.

48a. Numerical-range disambiguation (the `bra … keti` motivating case):
    - `tomu bra re keti bra ko zo zo keti e` — "between 3 and 400 (pushups)." Without brackets, `tomu re ko zo zo` would fuse all four digits into `rekozozo` (= 3400) and `tomu` would be missing its second argument — ill-formed.
    - `tomu bra re zo zo keti bra ko zo zo keti e` — "between 300 and 400." Always bracket both arguments; never trust the digit-stream rule to split a multi-number expression on its own.

## 9b. Epistemic modality (kani / musi)

49a. `kani pluve` — "It might rain." / "Possibly it rains." (◇)
49b. `musi pluve` — "It must be raining." / "Necessarily." (□)
49c. `no- musi samo m1 m2` — "Not necessarily m1 = m2." (English's elusive "doesn't have to equal" reading)
49d. `kani no- samo m1 m2` — "Possibly m1 ≠ m2." (the "can be different" reading without claiming they actually are)
49e. `kani loka-x i kune kani loka-y i kune no- mesa` — "Possibly at-x AND possibly at-y AND no measurement." (quantum superposition without smuggling in a definite location)
49f. `dik e ke kani pluve` — "She says that it might rain." (modal inside a complement clause)

## 9c. Axis system (aksi / tipi / mezi)

49g. `aksi fasa` — "the X axis (forward-back axis, agent-frame)."
49h. `aksi sura magu` — "upward direction" (Z axis, + polarity).
49i. `aksi sura minu` — "downward direction" (Z axis, − polarity).
49j. `gol aksi fasa magu e` — "She goes forward." (motion verb + direction)
49k. `tipi aksi sura magu bra box keti` — "the top of the box" (extreme point at +Z end of the box).
49l. `stao sus tipi aksi sura magu bra box keti` — "the top of the box is dirty."
49m. Contrast: `sura box` (relational: somewhere above the box) vs `tipi aksi sura magu bra box keti` (intrinsic: the top extreme of the box itself).
49n. `mezi aksi sura bra box keti` — "the height of the box" (magnitude along Z axis).
49o. `samo re metr mezi aksi pa bra box keti` — "the longest dimension of the box equals 3 meters." (Object-frame, orientation-free.)
49p. `aksi fasa magu bra trafik keti` — "the (forward) direction of the traffic flow" (sentido, polarized).
49q. Object-frame ranks: `mezi aksi pa` (longest dimension), `mezi aksi du` (middle), `mezi aksi re` (shortest). Doesn't presume orientation.

## 9d. Angles (fractions of a revolution)

49r. `rot zo dozu re aksi sura e` — "She turns 90° left." (Rotate by 1/4 = `zo dozu re` = 0.25 around Z, positive direction.)
49s. `rot zo dozu sa aksi sura e` — "She turns around (180°)." (1/2 revolution around Z.)
49t. `rot zo dozu pa aksi lata e` — "She tilts forward 30°." (1/12 revolution around Y, the lateral axis.)
49u. `rot minu zo dozu re aksi sura e` — "She turns 90° right." (Negative quarter rev around Z.)
49v. `samo zo dozu sa rota bra his approach keti aksi sura` — "His angle of approach is 180° around Z." (Noun form via `rota`.)
49w. Cardinal vs angular reference points around Z, starting from forward (+X = "12 o'clock"):
   - 12 o'clock (forward): `aksi fasa magu` (cardinal) or `rota zo aksi sura` (angle 0).
   - 9 o'clock (left): `aksi lata magu` (cardinal) or `rota zo dozu re aksi sura` (angle 1/4 = 0.25 dec = 0.3 doz).
   - 6 o'clock (back): `aksi fasa minu` (cardinal) or `rota zo dozu sa aksi sura` (angle 1/2).
   - 3 o'clock (right): `aksi lata minu` (cardinal) or `rota minu zo dozu re aksi sura` (angle −1/4).
49x. Non-cardinal "1:30 o'clock" (45° clockwise from 12) = `rota minu zo dozu pa sa aksi sura` ≈ "rotation of −1/8 around Z."

## 9e. Graded probability (chani)

49y. `chani zo demu ne zo pluve` — "It will rain with probability 0.90." (90% likely)
49z. `chani zo demu fi samo a b` — "a equals b with probability 0.5." (Coin-flip uncertainty.)
49aa. `chani zo demu pa pluve` — "It'll rain with probability 0.1." (Unlikely.)
49bb. Equivalences:
    - `chani zo X` ≡ `no- kani X` — P = 0 = impossible.
    - `chani pa X` ≡ `musi X` — P = 1 = certain.
    - `kani X` ≈ `chani <unspecified positive> X` — speaker not committing to a specific value.
49cc. Probability ranges (compose with comparison operators):
    - `chani magu zo demu fi pluve` — "P(rain) > 0.5" (more likely than not)
    - `chani minu zo demu du fi pluve` — "P(rain) < 0.25"
    - `chani tomu zo demu du fi zo demu chi fi pluve` — "P(rain) is between 0.25 and 0.75"
49dd. Probability comparison: `magu chani pluve chani ne` — "rain is more likely than snow" (chance-of-rain > chance-of-snow).
49ee. Conditional probability: `chani zo demu ne zo pluve dati stao nub-s [sky]` — "P(rain | sky is cloudy) = 0.9" (conditional via `dati`).
49ff. `kani samo re metr mezi aksi pa bra box keti. chani zo demu chi fi samo re metr. no-vis y i` — "The longest dimension of the box might be 3 meters. It's probably 3 meters (P = 0.75). I haven't seen it." (Hedging with mixed modals.)
49gg. Distinction from amount-precision:
    - `hav piru pa zo [apple] e` — "She has approximately 10 apples." (`piru` on the amount.)
    - `chani zo demu chi fi hav pa zo [apple] e` — "She probably has 10 apples." (`chani` on the proposition.)
    - These are different claims. `piru` says the amount is uncertain; `chani` says the whole statement is uncertain.

## 10. Reasoning chain

49. `dati pluvo` — "Given that it rained." (premise)
50. `dati pluvo. golo e kawa ke pluvo. ergi [floor wet]` — "Given it rained. She left because it rained. Therefore the floor is wet."
51. Modus tollens: `dati pluvo impi [floor wet]. no-[floor wet]. ergi no-pluvo` — "Given rain implies wet floor. The floor is not wet. Therefore it did not rain."

## 11. Copulas (the "is"-overload split)

52. `[Mark Twain] samo [Samuel Clemens]` — "Mark Twain is Samuel Clemens." (identity)
53. `esto [blue] [sky]` — "The sky is blue." (essential predication)
54. `stao [tired] e` — "She is tired." (state predication, transient)
55. `memo [mammal] [whale]` — "A whale is a mammal." (set membership)
56. `totu [mammal] memo [animal]` — "Every mammal is an animal." (subset by composition)
57. `kelu [problem]` — "There is a problem." (existence by composition)
58. `samo liti incorrect fini [password]` — "The password is (literally) 'incorrect'."
59. `stao [incorrect-property] [password]` — "The password is incorrect (= wrong)."

## 12. Literal and variable markers

60. `dike e liti thank you fini` — "She says, 'thank you'." (raw string content)
61. `samo liti Lexor fini [name-language]` — "The language's name is 'Lexor'."
62. `golo u tepa vari path. legu u vari path` — "Go to var-path. Read var-path." (template; both occurrences = same slot)
63. `defi vari x samo [biggest prime anta pa zo zo]. magu vari x fi zo` — "Let x = the biggest prime before 100. x > 50."
64. `defi vari f [function-expression]. kompe y vari f moda vari x` — "Let f = [function]. I apply f to x."
65. `nulu defi vari x` — "x is no longer bound." (explicit retraction)

## 13. Composed bindings inside reasoning

66. `defi vari p [totu [whale] memo [mammal]]. dati vari p. dati memo [whale] [moby]. ergi memo [mammal] [moby]` — "Let p = 'every whale is a mammal'. Given p. Given Moby is a whale. Therefore Moby is a mammal."

---

## Observations and surfaced gaps

Working through these exposed the following:

1. **"Yesterday" / "tomorrow" composition feels clunky.** `tepa anta pa dima` ("at one-day-before") is correct but mouthy compared to `tepa [yesterday]`. May want a dedicated unit-shift composition convention or a small set of relative-time roots after all. Decision deferred.
2. **No locked roots for many high-frequency content words** — drink, water, door, key, apple, person, house, fix, hammer, read, function. Examples here rely on placeholder brackets. This is the next major work item (vocabulary arc, Session N+3+).
3. **VOS placement of full clauses** (e.g., `dike e ke loma u`) reads naturally: verb, subject, complement-clause. The complement is the object slot, but expressed as a `ke`-clause it sits after the subject — consistent with "subordinate clause follows its host."
4. **Embedded literal inside identity** (`samo liti incorrect fini [password]`) works but is heavy. For everyday quoted speech, the order `verb subject liti content fini` (as in #60, `dike e liti thank you fini`) is lighter because no copula is involved.
5. **`defi`-binding inside reasoning chains** (#66) is the most powerful demonstration so far. Long premises become single tokens (`vari p`); the chain stays readable.
6. **No problems found with prosody assumptions.** All examples parse uniquely under the brief-break / clause-break / sentence-break model.
7. **`kompo` / `kompe`** ("fix/repair") used as working root; needs vocab assignment.
8. **`pere` / `legu`** (open / read-imperative) — `pere` updated 2026-05-16 (root renamed `apr → per`). `legu` still using working-form spelling.

## Next examples to add (after vocabulary buildout)

- Full spatial-prepositions paragraph (under/over/near/beside) once that family is locked.
- Negative reasoning with multiple `dati` premises and case-splitting (need the parked proof-structuring particles first).
- Nested `defi`s in a formal proof (need scope rules locked).
- Long natural-text paragraph (3–5 sentences) demonstrating discourse flow.
