# Walkthrough — Lexor by progressive complexity

Read this top-to-bottom to learn the language. Each level introduces one new piece of grammar, and later levels assume you've seen the earlier ones.

Examples use bracketed placeholders like `[apple]` for content words whose Lexor forms haven't been chosen yet. The grammar is the focus here, not the vocabulary.

---

## What you need to know before Level 0

A few terms you'll see throughout. Don't worry about memorizing them — they'll make sense after a few examples.

### Word shapes

Lexor words follow predictable shapes built from two kinds of sounds:

- A **vowel** — `a e i o u y c`. (The letter `c` represents one of the vowel sounds, written that way for keyboard convenience.)
- A **consonant** — everything else: `b d f g h j k l m n p r s t v z x` plus the digraph `ch`.

The two main shapes you'll meet are:

- **CV** ("consonant-vowel") — a single consonant followed by a single vowel. Two letters, one syllable. Used for very common words like pronouns and digits: `e` (he/she), `pa` (the digit 1), `ka` (question particle).
- **CVC** ("consonant-vowel-consonant") — consonant, vowel, consonant. Three letters, one syllable. Used for all content roots like verbs, nouns, and adjectives: `lom` (eat), `pot` (make), `vis` (see).

Words built on a CVC root usually grow vowels on the end to mark tense or role, so you'll often see longer forms like `lome`, `loma e`, `lomera`. The starting consonant-vowel-consonant is the *root*, and the rest is grammatical information attached to it.

### Sentence order

Lexor sentences put the verb first. The order is:

> **verb · object · subject** — what is happening, what it happens to, who does it.

Some textbooks abbreviate this as **VOS** ("verb-object-subject"). This abbreviation will come up later. Most other modifiers (counts, place markers, time markers) come after the noun they refer to.

---

## L0 — The bare verb

**Lexor:** `loma`

**What it means:** "eat (in general)."

**How it's built:**
- `lom` is the root for the concept of eating.
- `a` is a vowel added to the root. This particular vowel means "no specific time" — the speaker isn't saying when the eating happens. It's the default choice when time doesn't matter.

So `loma` is the eat-root plus the no-time vowel, and the whole word means "to eat" or "eats in general."

**What this level shows:**
- Lexor words are made by combining a root with one or more vowels.
- The vowel right after the root tells you when the action happens. Other vowels would say "past," "future," "right now," and so on — you'll see those in Level 2.
- You can have a complete verb with no subject. The listener can fill in "who" from context if it matters.

---

## L1 — Adding a subject

**Lexor:** `loma e`

**What it means:** "She eats." (or "He eats," or "They eat" — the speaker isn't committing to a gender.)

**How it's built:**
- `loma` is the verb you already know: "eat" with no specific time.
- `e` is a one-letter pronoun meaning "he, she, or they (one person)." Lexor doesn't force the speaker to commit to a gender.

**What this level shows:**
- The subject (who is doing the verb) comes *after* the verb. There's no object yet, so the order is just verb then subject.
- Pronouns are very short — usually one letter — because they're used so often.
- The language never forces you to commit to information you haven't decided on. Gender is one example.

**Other pronouns you can use in the same slot:**

| Lexor | Meaning |
|---|---|
| `y` | I, me (the speaker) |
| `u` | you (one listener) |
| `e` | he / she / they (one other person) |
| `i` | it (one object or concept) |
| `le` | we (you and me, just us two) |
| `lo` | they (multiple other people) |
| `ly` | you (multiple listeners) |
| `la` | we (some group including the speaker, members unspecified) |

---

## L2 — When the action happens (tense)

The vowel at the end of the root tells you when the action takes place. Swap the vowel, get a different time.

| Lexor | Meaning |
|---|---|
| `loma e` | she eats (general / no specific time) |
| `lome e` | she is eating (right now) |
| `lomo e` | she ate (in the past) |
| `lomi e` | she will eat (in the future) |
| `lomex e` | she is eating (ongoing right now — the `x` adds "is in the middle of") |
| `lomy e` | she would eat (hypothetical / if-then condition) |
| `lomu` | eat! (a command — the subject is usually left out) |

**The full set of these vowels:**

| Vowel | Meaning |
|---|---|
| `a` | no specific time (general truth, default) |
| `e` | present (right now) |
| `o` | past |
| `i` | future |
| `u` | imperative (a command) |
| `y` | conditional (hypothetical, "would") |
| `c` | perfect (completed action — sounds like "æ") |

The extra letter `x` after one of these adds "in the middle of" (ongoing). So `lomex` is "is right now in the middle of eating."

**What this level shows:**
- One vowel does the work of English's whole tense system (eat / ate / will eat / would eat / etc.).
- If you don't know or don't care about when, use `a`. Lexor doesn't force you to pick a tense.
- Same vowels work later on nouns derived from verbs — for example, a "current eater" vs a "past eater" uses the same vowel system.

---

## L3 — Adding an object

**Lexor:** `loma [apple] e`

**What it means:** "She eats an apple."

**How it's built:**
- `loma` — eat (general).
- `[apple]` — the thing being eaten. (We're using brackets because the real Lexor word for apple hasn't been picked yet.)
- `e` — she.

**What this level shows:**
- With an object in the sentence, the order is verb, then object, then subject. The object sits between the verb and the subject.
- There's no word for "a" or "the." If you don't care whether it's "an apple" or "the apple" or just "apples in general," you don't say it.
- There's no plural mark either. "An apple," "apples," and "the apples" all surface as `[apple]` unless you specifically want to add a number or a definiteness marker.

---

## L4 — Marking roles when position alone isn't enough

For sentences with two arguments (eater and food), the order is enough — verb, object, subject. But for verbs that take three arguments (like "give X to Y") or where the order could be ambiguous, you can stick a small vowel on the end of each noun to mark its role.

**Lexor:** `loma [apple]-o e-e` — she eats an apple, with explicit roles
**Lexor:** `dake [apple]-o e-e u-u` — she gives an apple to you
**Lexor:** `apre [door]-o e-e [key]-i` — she opens the door with a key

**The role vowels:**

| Vowel | Role | English equivalent |
|---|---|---|
| `-e` | subject (the doer) | she |
| `-o` | object (the thing acted on) | the apple |
| `-u` | recipient | to you |
| `-i` | instrument | with a key |

You only need these when the default order doesn't make the meaning clear. For ordinary two-argument sentences, just rely on word order.

When a pronoun already ends in `e` and you add `-e`, you get a doubled vowel like `e-e`. Pronounce that as one longer vowel.

---

## L5 — Counting and quantifying

To say how many of something, put a number or quantity word *after* the noun.

| Lexor | Meaning |
|---|---|
| `loma [apple] re e` | she eats three apples |
| `loma [apple] tot e` | she eats every apple |
| `loma [apple] kel e` | she eats some apple |
| `loma [apple] nul e` | she eats no apple |
| `loma [apple] sol re e` | she eats only three apples |

**The pieces:**

- `re` is the digit 3. The full digit list is `zo pa du re ko fi sa chi bo ne` for 0 through 9.
- `tot` means "all" or "every." (Logicians sometimes call this the *universal* quantifier and write it as ∀.)
- `kel` means "some." (Logicians call this the *existential* quantifier and write it as ∃.)
- `nul` means "none, zero of."
- `sol` means "only, restricted to."

**Choosing between "each" and "together":**

When three people share three apples, English can be ambiguous — does each person get one, or do all three eat the apples together? Lexor has two small markers to make this explicit:

- `loma [apple] re pad e` — three apples, each one separately (distributive)
- `loma [apple] re mas e` — three apples, all together as a group (collective)

If you don't add either marker, you're saying "three apples" without committing to which reading — that's allowed and means exactly that.

---

## L6 — Place, time, and how-it's-done (prepositions)

Lexor uses small connector words to attach extra information like *where*, *when*, or *how*. These come at the end of the sentence by default.

**Lexor:** `loma e tep dim` — she eats during the day
**Lexor:** `loma e lok bra [kitchen] ket` — she eats in the kitchen
**Lexor:** `kompo e mod ke martelo o` — she fixes it by hammering it

**The connector words used here:**

- `tep` — "at" or "during" (for points in time). `tep dim` = "during the day."
- `lok` — "at," "in," or "on" (for places). `lok bra [kitchen] ket` = "in the kitchen." The `bra … ket` is a pair of brackets you'll meet in Level 16; here they just group the place word.
- `mod` — "by," "by means of." `mod ke martelo o` = "by hammering it." The `ke` introduces a small sub-sentence as the way it was done.

**The full set of place connectors** (closed list — these are the only ones):

`lok` (at/in/on), `sub` (under), `sur` (over), `pok` (near), `lat` (beside), `dor` (behind), `fas` (in front of), `int` (between), `kir` (around), `dir` (toward), `oks` (from), `tra` (through).

**The full set of time connectors:**

`tep` (at), `pen` (during), `sin` (since), `lim` (until), `ant` (before), `pos` (after).

---

## L7 — Saying "not"

To negate a word, attach `no-` directly in front of it. The hyphen shows it's stuck to the next word, not a separate word.

| Lexor | Meaning |
|---|---|
| `no-loma e` | she doesn't eat (the whole action is negated) |
| `loma no-[apple] e` | she eats not-an-apple (only the *thing eaten* is negated — she eats, but not an apple) |
| `no-mag e [him]` | she is not greater than him (the comparison is negated) |

**What this level shows:**
- `no-` always scopes over the *one* word it's attached to. To negate a different part of the sentence, move `no-` to a different word. Three positions, three meanings.
- Lexor doesn't have separate negation prefixes like English "un-," "non-," "anti-." There's just `no-` for everything.
- Lexor has no built-in opposite marker either. "Love" and "hate" get their own separate roots (`am` and `od`). `no-am` means "doesn't love," which is not the same as "hates."

---

## L8 — Asking questions

All questions in Lexor use the same little word: `ka`. Where you put `ka` determines what kind of question you're asking.

| Lexor | Meaning |
|---|---|
| `ka loma e` | does she eat? (yes/no — `ka` at the start) |
| `loma ka` | what does she eat? (`ka` in the object slot) |
| `loma [apple] ka` | who eats apples? (`ka` in the subject slot) |
| `loma e tep ka` | when does she eat? (`ka` after the time-connector `tep`) |
| `loma e lok ka` | where does she eat? (`ka` after the place-connector `lok`) |
| `loma e mod ka` | how does she eat? |
| `loma e kaw ka` | why does she eat? (`kaw` is the cause-connector) |
| `loma e, ka` | she eats, right? (tag question — comma plus `ka` at the end) |

**What this level shows:**
- One word, `ka`, replaces all of English's "who, what, when, where, why, how, does, is, are…"
- The position of `ka` tells you which slot is being asked about. No memorizing a separate word for each question type.

---

## L9 — Building bigger sentences (subordinate clauses)

To put a small sentence inside a bigger one — like "the man who eats apples" or "she says that you eat" — Lexor uses one word: `ke`. What `ke` means depends on what comes right before it.

| Lexor | Meaning | What's before `ke` |
|---|---|---|
| `[man] ke loma [apple]` | the man who eats apples | a noun → relative clause |
| `[apple] ke loma e` | the apple that she eats | a noun (object) → relative clause |
| `dike e ke loma u` | she says that you eat | a speech verb → complement clause |
| `golo e tep ke pluvex` | she left when it was raining | a time word → time clause |
| `golo e kaw ke pluvo` | she left because it rained | a cause word → reason clause |

**What this level shows:**
- One word, `ke`, replaces English's "who, which, that, when, while, because, although…"
- Whatever sits *before* `ke` tells you what role the sub-sentence is playing: a noun gives you a relative clause, a verb gives a complement, a connector word gives an adverbial.

---

## L10 — "If…then" sentences (conditionals)

**Lexor:** `is pluve, lomy e [inside]` — if it's raining, she would eat inside
**Lexor:** `is no-pluve, goly e` — if it isn't raining, she would go

**How it's built:**
- `is` means "if." It introduces the condition.
- The verb after the comma takes the vowel `y` (the conditional vowel from Level 2). So `lomy` is "would eat" and `goly` is "would go."

**What this level shows:**
- Causal "if" (the everyday kind, where one thing makes another happen) uses `is`. There's also a separate word `imp` for formal logical implication (used in proofs and math). You'll see `imp` in Level 12.
- The conditional vowel `y` on the result-verb signals that this isn't an assertion — it's a hypothetical.

---

## L11 — Linking with "and" / "or"

Two simple connectors:

**Lexor:** `loma [apple] e kun bibe [water] e` — she eats an apple and drinks water
**Lexor:** `loma [apple] e vel loma [pear] e` — she eats an apple or a pear

**The words:**
- `kun` = "and" (from Latin *cum*, "with")
- `vel` = "or" (from Latin *vel*, "or")

**What this level shows:**
- You can chain any number of "and"s together, or any number of "or"s. Those are unambiguous.
- But you *can't* mix them in a flat sentence. "A and B or C" is not allowed by itself — you have to use the bracket pair `bra … ket` (Level 16) to show whether you mean "(A and B) or C" or "A and (B or C)."

---

## L12 — Reasoning step by step

For arguments and proofs, Lexor uses three little discourse words: `dat`, `erg`, and `imp`.

**Lexor:** `dat pluvo. golo e kaw ke pluvo. erg sta sus-s [floor]`
**Translation:** "Given that it rained. She left because it rained. Therefore the floor is wet."

**Lexor:** `dat pluvo imp sta sus-s [floor]. no-sta sus-s [floor]. erg no-pluvo`
**Translation:** "Given that rain implies a wet floor. The floor is not wet. Therefore it didn't rain." (This is the logical step called *modus tollens*.)

**The three words:**
- `dat` — "given that," "let us assume." Marks a starting point.
- `erg` — "therefore." Marks a conclusion.
- `imp` — "formally implies." Used for strict logical implication, separate from the everyday "if…then" (`is`) of Level 10.

**What this level shows:**
- Reasoning chains are built from separate sentences, each one a step. Lexor doesn't nest conditionals inside conditionals.
- These three words together let you write proofs, arguments, and structured explanations cleanly.

---

## L13 — "Might" and "must" (modal operators)

To say something might be true, or must be true, use one of two markers at the start of the sentence.

**Lexor:** `kan pluve` — it might rain
**Lexor:** `mus pluve` — it must be raining
**Lexor:** `no- mus sam a b` — a doesn't have to equal b (it's not necessarily true that a equals b)
**Lexor:** `kan no- sam m1 m2` — m1 and m2 might be different (it's possible that they aren't equal)

**The words:**
- `kan` = "might," "may," "is possibly." Mnemonic: English/German *can* / *kann*.
- `mus` = "must," "is necessarily." Mnemonic: English/German *must* / *muss*.

Both go at the very start of a sentence. Both can be combined with `no-` from Level 7 to give four readings: "might be the case," "might not be," "must be," "doesn't have to be."

**What this level shows:**
- The distinctions English collapses into "is" / "could be" / "might be" / "doesn't have to be" are clearly separate in Lexor.
- This is *epistemic* modality — about what the speaker thinks is possible or necessary. Permission and obligation ("you may smoke here," "you must wear a helmet") are a separate kind of modality that hasn't been added yet.

---

## L13b — Numerical probability

Sometimes you want to attach a specific probability to a claim, like "90% likely." Lexor uses `chan` for this.

**Lexor:** `chan zo dem ne zo pluve` — it will rain with probability 0.90
**Lexor:** `chan zo dem fi sam a b` — a equals b with probability 0.5
**Lexor:** `chan mag zo dem fi pluve` — the probability of rain is greater than 0.5

**How it works:**
- `chan` goes at the start of the sentence, like `kan` and `mus`.
- After `chan` comes a number, then the rest of the sentence.
- The number is a fraction between 0 and 1, where 0 means "impossible" and 1 means "certain."
- Mnemonic: English/French *chance*.

The number itself is built from digits: `zo dem ne zo` is "zero point nine zero" = 0.90 in decimal. (The `dem` is the decimal point.)

**Relating `chan` to the earlier `kan` and `mus`:**
- `chan zo X` = "X has probability 0" = impossible. Same as `no- kan X`.
- `chan pa X` = "X has probability 1" = certain. Same as `mus X`.
- `kan X` (without a number) is "X is possible to some unspecified degree."

**Conditional probability** uses `dat` from Level 12: `chan zo dem ne zo X dat Y` reads as "X has probability 0.9 given Y." That's the probability of X assuming Y.

**What this level shows:**
- You can attach a specific numeric probability to any sentence without awkward "it's 90% likely that…" wrappers.
- `chan` is different from the amount-precision markers (`pir` for "approximately," `tom` for "between"). Those attach to a single number; `chan` attaches to a whole sentence.

---

## L14 — Talking about axes, directions, and dimensions

For directions ("upward"), locations ("the top"), and dimensions ("the height"), Lexor uses a small system based on three new words plus the place-connectors you already know.

**Lexor:** `gol aks fas mag e` — she goes forward
**Lexor:** `aks lat mag` — left direction (the positive Y direction)
**Lexor:** `aks sur min` — down direction (the negative Z direction)
**Lexor:** `tip aks sur mag bra [box] ket` — the top of the box (the extreme point at the upper end)
**Lexor:** `mez aks pa bra [box] ket` — the longest dimension of the box
**Lexor:** `mez aks sur bra [box] ket` — the height of the box (the size along the up-down axis)

**The pieces:**
- `aks` means "axis" — a line that goes through space in one direction.
- `tip` means "the extreme point" or "the end of an axis."
- `mez` means "size along an axis" (a length, a width, a height, etc.).
- `mag` and `min` mark which end of an axis: `mag` = the positive end, `min` = the negative end. (You've seen them before as "greater than" and "less than" — Lexor reuses them.)

**Two ways to identify an axis:**

*By the body's reference frame* (an observer's forward-backward, left-right, up-down):
- `aks fas` = the front-back axis (= the X axis)
- `aks lat` = the left-right axis (= the Y axis)
- `aks sur` = the up-down axis (= the Z axis)

*By size rank* (orientation doesn't matter):
- `aks pa` = the longest dimension (rank 1)
- `aks du` = the middle dimension (rank 2)
- `aks re` = the shortest dimension (rank 3)

**The coordinate system Lexor uses** (locked in `decisions.md`):
- X axis points forward (the direction the person is facing).
- Y axis points to their left.
- Z axis points up.
- "Right-handed" — if you curl the fingers of your right hand from X toward Y, your thumb points along Z.

**What this level shows:**
- English mixes up "up" the direction, "top" the location, and "height" the size. Lexor uses three different shapes for these so there's no ambiguity.
- For the dimensions of an object (longest / middle / shortest), Lexor uses the digit ranks. That way you don't have to know which way the object is sitting.

---

## L15 — Angles

Angles in Lexor are written as *fractions of a full turn*. There's no degrees, no radians — the number itself is how many full rotations.

| Lexor | Meaning |
|---|---|
| `rot zo doz re aks sur e` | she turns 90° to the left (1/4 of a full turn around the Z axis) |
| `rot zo doz sa aks sur e` | she turns around (180°, 1/2 of a full turn) |
| `rot min zo doz re aks sur e` | she turns 90° to the right (negative 1/4 turn) |
| `rot zo doz pa aks lat e` | she tilts forward 30° (1/12 of a turn around the Y axis) |

**How the numbers work:**

The number is just the fraction. So 1/4 of a turn = 0.25 in decimal = 0.3 in dozenal (base 12).

In dozenal — Lexor's natural base for angles, because 12 divides evenly into many useful angles:
- `zo doz pa` = 1/12 = 30° (the `doz` is the dozenal decimal point)
- `zo doz du` = 2/12 = 60°
- `zo doz re` = 3/12 = 90°
- `zo doz sa` = 6/12 = 180°
- `zo doz pa sa` = roughly 1/8 = 45°

**Direction of positive turn:**

A positive turn (no minus sign) means *right-handed* rotation around the named axis. For `aks sur` (the Z axis, pointing up), that's counterclockwise when you look down from above — which is *leftward* for someone facing forward.

If you're used to a clock face, this is flipped: clock hands go clockwise (which is *negative* in Lexor for rotation around Z), and 9 o'clock (the left side of a clock face) corresponds to a positive 1/4 turn (0.25). It's consistent with physics convention; takes a moment to get used to.

**What this level shows:**
- Any angle around any axis can be expressed compactly with no new vocabulary — just the rotation verb, a number, and the axis name.
- Compass-like directions are reachable: forward = 0, left = +1/4, back = +1/2, right = +3/4 (or −1/4).

---

## L16 — Grouping inside a sentence (brackets)

When a sentence has multiple parts that could group different ways, Lexor uses a pair of bracket-words: `bra` (opens a group) and `ket` (closes a group). Mnemonic: English "bracket" split into bra-ket.

**Lexor:** `tom bra re ket bra ko zo zo ket e` — "I can do between 3 and 400 (pushups)"
**Lexor:** `bra loma A e kun loma B e ket vel loma C e` — "(she eats A and she eats B) or she eats C"
**Lexor:** `loma A e kun bra loma B e vel loma C e ket` — "she eats A and (she eats B or she eats C)"

**When you need them:**
- When a number-operator like `tom` (between) takes two numeric arguments. Without brackets, "tom 3 400" would all get read as one big number because Lexor concatenates adjacent digits.
- When you want to mix "and" and "or" in the same sentence. Flat mixed forms are not allowed; brackets make the grouping unambiguous.
- Anywhere else you'd want grouping for clarity.

**Nesting:**

If you have brackets inside brackets, each `ket` closes the most recent unclosed `bra` — same rule as math parentheses.

---

## L17 — Naming a piece of sentence for reuse

When you want to use the same phrase several times without retyping it, give it a name with `def`.

**Lexor:** `def var p loma A e kun loma B e. var p vel loma C e`
**Translation:** "Let p be 'she eats A and she eats B'. (p) or she eats C."

**Lexor:** `def var x sam [biggest prime ant pa zo zo]. mag var x fi zo`
**Translation:** "Let x be the biggest prime before 100. x is greater than 50."

**Lexor:** `nul def var x`
**Translation:** "x is no longer defined." (Explicit erasure of a name you had bound.)

**The pieces:**
- `def` introduces a name-binding.
- `var <name>` references a name you've defined. The first time, it's the name being introduced; later times, it stands in for the expression.
- `nul def var <name>` removes the binding. Defining the same name again replaces the old binding.

**What this level shows:**
- Use `def` to name long expressions so a later sentence can refer back to them compactly.
- The name stays defined as long as the conversation continues (until you erase it or define it differently).
- Note that `def` is for *naming for reuse*. For just splitting up a confusing sentence so groupings are clear, use the brackets from Level 16 instead.

---

## L18 — Composing several features

A small collection of worked examples. Each one combines several earlier features in a way the language is designed to handle smoothly.

### Example 1: she might come, but won't eat unless we ask

```
kan vene e. is no-kan mus pet e ke loma, no-lomy e.
```

Sentence 1: `kan vene e` — "She might come." (`kan` = might, `vene` = come-present, `e` = she.)

Sentence 2: `is no-kan mus pet e ke loma, no-lomy e` — "If we can't necessarily ask her to eat, she would not eat." Stilted in English but legal Lexor; demonstrates a modal inside a conditional inside an embedded clause.

### Example 2: a pushup bet with a number range

```
dat dike e ke kan domi e bra rot bra re ket bra ko zo zo ket ket pushupn. erg lori e kaw ke no-kan.
```

Translation: "Given that she says she can do (between 3 and 400) pushups: therefore (she will cry) because (it is impossible)."

This silly example exercises: reasoning markers (`dat`, `erg`), a modal (`kan`), grouping brackets around a number range, and embedded clauses.

### Example 3: a navigation order

```
gol aks fas mag pa zo metr e. rot zo doz re aks sur e. gol aks fas mag fi metr e.
```

Translation: "Go forward 10 meters. Turn 90° left. Go forward 5 meters."

Three crisp imperatives in a row, chaining motion and rotation. The axis system plus the angle convention makes this kind of language compact and unambiguous — useful for driving instructions, robotics, game commands, military communications.

### Example 4: hedging a measurement

```
kan sam re metr mez aks pa bra box ket. kan min. no-vis y i.
```

Translation: "The longest dimension of the box might be 3 meters. It might be less. I haven't seen it."

Shows how `kan` lets a speaker hedge cleanly. Compare to English "it's 3 meters… maybe? I don't know" which needs three separate clauses to do the same job.

---

## Closing notes

This walkthrough covers most of the locked grammar. The remaining details are in `decisions.md` (the log of settled choices) and `examples.md` (a denser reference with many more example sentences).

Open design questions are tracked in `tasks.md`. Unmet design goals are in `trials.md` — `grep` for `[.*, open]` to see them all.

The vocabulary itself is still mostly unwritten. Every bracketed `[word]` above is a placeholder for a content root that hasn't been chosen yet. The priority list for filling those in is in `frequencies.yaml`.

If a sentence shape here parses two ways in your head, that's either a bug in the walkthrough or a real ambiguity worth filing as a `[trap]` entry in `trials.md`. Both are useful to flag.
