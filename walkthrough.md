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

### A note on pronunciation

Lexor uses **self-segregating morphology**: word boundaries fall out of word shapes, so you don't have to pause between words. You can speak at a natural pace, like in English or Spanish.

The rule that makes this work: regular content words (verbs, nouns, adjectives) always start with a consonant and end with a vowel. So when you hear a vowel followed by a consonant in a sound stream, the consonant is starting a new word. When you hear two consonants meeting, the second one is the next word's onset.

The small set of "function words" (pronouns, connectors, markers) can be vowel-initial, but they're a short memorized list — your brain identifies them as a unit when they come up.

In practice, this means you can speak Lexor fluidly. A short pause between words is *recommended* for clarity, especially when speaking fast or in noisy places — but it's not grammatically required.

A separate point: some example sentences below use placeholder forms like `pluve` for "rain." These are not yet locked Lexor words. They follow Latin-style shapes that don't fit the language's strict consonant-vowel-consonant pattern. When the vocabulary for "rain" is chosen, the real form will replace `pluve`.

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

**What it means:** "She eats." Or "He eats." The pronoun `e` refers to *one* other person whose gender the speaker doesn't want to specify.

**What `e` does and doesn't say:**

The pronoun `e` is precise about three things and deliberately vague about one:

- **Precise:** it refers to a *person*, not an object. (For "it," the pronoun is `i`.)
- **Precise:** it refers to *one* person, not several. (For multiple people, the pronoun is `lo`.)
- **Precise:** it refers to a *third party* — not the speaker, not the listener. (For "I" use `y`; for "you" use `u`.)
- **Vague:** gender. The speaker is choosing not to commit to "he" or "she." That's the only thing `e` leaves open.

In modern English, the word "they" is sometimes used in the singular when the speaker doesn't know or want to specify gender ("someone left their bag — they came back for it"). That singular "they" is what `e` matches. The *plural* "they" (multiple people) is a different Lexor word: `lo`.

**How it's built:**
- `loma` is the verb you already know: "eat" with no specific time.
- `e` is the third-person singular pronoun, gender unspecified.

**What this level shows:**
- The subject (who is doing the verb) comes *after* the verb. There's no object yet, so the order is just verb then subject.
- Pronouns are very short — often one letter — because they're used so often.
- The language never forces you to commit to information you haven't decided on. Gender is one example of this principle.

**The full set of pronouns:**

| Lexor | Refers to | Number |
|---|---|---|
| `y` | the speaker ("I, me") | one |
| `u` | the listener ("you") | one |
| `e` | one other person ("he, she, singular they") | one |
| `i` | one object or concept ("it") | one |
| `le` | speaker + listener ("we, just us two") | two |
| `lu` | speaker + one other person ("me and her/him") | two |
| `ly` | multiple listeners ("you all") | plural |
| `lo` | multiple other people ("they") | plural |
| `li` | multiple objects ("they" for things) | plural |
| `la` | some unspecified group including the speaker | unspecified |
| `lc` | speaker + listener + others ("we, inclusive of everyone") | plural |

Notice that "we" splits into several distinct forms depending on who exactly is included. Lexor refuses to collapse these into one ambiguous "we" the way English does.

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
| `loma [apple] totu e` | she eats every apple |
| `loma [apple] kelu e` | she eats some apple |
| `loma [apple] nulu e` | she eats no apple |
| `loma [apple] solu re e` | she eats only three apples |

**The pieces:**

- `re` is the digit 3. The full digit list is `zo pa du re ko fi sa chi bo ne` for 0 through 9.
- `totu` means "all" or "every." (Logicians sometimes call this the *universal* quantifier and write it as ∀.)
- `kelu` means "some." (Logicians call this the *existential* quantifier and write it as ∃.)
- `nulu` means "none, zero of."
- `solu` means "only, restricted to."

**Choosing between "each" and "together":**

When three people share three apples, English can be ambiguous — does each person get one, or do all three eat the apples together? Lexor has two small markers to make this explicit:

- `loma [apple] re padu e` — three apples, each one separately (distributive)
- `loma [apple] re masu e` — three apples, all together as a group (collective)

If you don't add either marker, you're saying "three apples" without committing to which reading — that's allowed and means exactly that.

---

## L6 — Place, time, and how-it's-done (prepositions)

Lexor uses small connector words to attach extra information like *where*, *when*, or *how*. These come at the end of the sentence by default.

**Lexor:** `loma e tepa dima` — she eats during the day
**Lexor:** `loma e loka bra [kitchen] keti` — she eats in the kitchen
**Lexor:** `kompo e moda ke martelo o` — she fixes it by hammering it

**The connector words used here:**

- `tepa` — "at" or "during" (for points in time). `tepa dima` = "during the day."
- `loka` — "at," "in," or "on" (for places). `loka bra [kitchen] keti` = "in the kitchen." The `bra … keti` is a pair of brackets you'll meet in Level 16; here they just group the place word.
- `moda` — "by," "by means of." `moda ke martelo o` = "by hammering it." The `ke` introduces a small sub-sentence as the way it was done.

**The full set of place connectors** (closed list — these are the only ones):

`loka` (at/in/on), `suba` (under), `sura` (over), `poka` (near), `lata` (beside), `dora` (behind), `fasa` (in front of), `inta` (between), `kira` (around), `dira` (toward), `oksa` (from), `tra` (through).

**The full set of time connectors:**

`tepa` (at), `pena` (during), `sina` (since), `lima` (until), `anta` (before), `posa` (after).

---

## L7 — Saying "not"

To negate a word, attach `no-` directly in front of it. The hyphen shows it's stuck to the next word, not a separate word.

| Lexor | Meaning |
|---|---|
| `no-loma e` | she doesn't eat (the whole action is negated) |
| `loma no-[apple] e` | she eats not-an-apple (only the *thing eaten* is negated — she eats, but not an apple) |
| `no-magu e [him]` | she is not greater than him (the comparison is negated) |

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
| `loma e tepa ka` | when does she eat? (`ka` after the time-connector `tepa`) |
| `loma e loka ka` | where does she eat? (`ka` after the place-connector `loka`) |
| `loma e moda ka` | how does she eat? |
| `loma e kawa ka` | why does she eat? (`kawa` is the cause-connector) |
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
| `golo e tepa ke pluvex` | she left when it was raining | a time word → time clause |
| `golo e kawa ke pluvo` | she left because it rained | a cause word → reason clause |

**What this level shows:**
- One word, `ke`, replaces English's "who, which, that, when, while, because, although…"
- Whatever sits *before* `ke` tells you what role the sub-sentence is playing: a noun gives you a relative clause, a verb gives a complement, a connector word gives an adverbial.

---

## L10 — "If…then" sentences (conditionals)

**Lexor:** `isi pluve, lomy e [inside]` — if it's raining, she would eat inside
**Lexor:** `isi no-pluve, goly e` — if it isn't raining, she would go

**How it's built:**
- `isi` means "if." It introduces the condition.
- The verb after the comma takes the vowel `y` (the conditional vowel from Level 2). So `lomy` is "would eat" and `goly` is "would go."

**What this level shows:**
- Causal "if" (the everyday kind, where one thing makes another happen) uses `isi`. There's also a separate word `impi` for formal logical implication (used in proofs and math). You'll see `impi` in Level 12.
- The conditional vowel `y` on the result-verb signals that this isn't an assertion — it's a hypothetical.

---

## L11 — Linking with "and" / "or"

Two simple connectors:

**Lexor:** `loma [apple] e kune bibe [water] e` — she eats an apple and drinks water
**Lexor:** `loma [apple] e vele loma [pear] e` — she eats an apple or a pear

**The words:**
- `kune` = "and" (from Latin *cum*, "with")
- `vele` = "or" (from Latin *vel*, "or")

**What this level shows:**
- You can chain any number of "and"s together, or any number of "or"s. Those are unambiguous.
- But you *can't* mix them in a flat sentence. "A and B or C" is not allowed by itself — you have to use the bracket pair `bra … keti` (Level 16) to show whether you mean "(A and B) or C" or "A and (B or C)."

---

## L12 — Reasoning step by step

For arguments and proofs, Lexor uses three little discourse words: `dati`, `ergi`, and `impi`.

**Lexor:** `dati pluvo. golo e kawa ke pluvo. ergi stao sus-s [floor]`
**Translation:** "Given that it rained. She left because it rained. Therefore the floor is wet."

**Lexor:** `dati pluvo impi stao sus-s [floor]. no-stao sus-s [floor]. ergi no-pluvo`
**Translation:** "Given that rain implies a wet floor. The floor is not wet. Therefore it didn't rain." (This is the logical step called *modus tollens*.)

**The three words:**
- `dati` — "given that," "let us assume." Marks a starting point.
- `ergi` — "therefore." Marks a conclusion.
- `impi` — "formally implies." Used for strict logical implication, separate from the everyday "if…then" (`isi`) of Level 10.

**What this level shows:**
- Reasoning chains are built from separate sentences, each one a step. Lexor doesn't nest conditionals inside conditionals.
- These three words together let you write proofs, arguments, and structured explanations cleanly.

---

## L13 — "Might" and "must" (modal operators)

To say something might be true, or must be true, use one of two markers at the start of the sentence.

**Lexor:** `kani pluve` — it might rain
**Lexor:** `musi pluve` — it must be raining
**Lexor:** `no- musi samo a b` — a doesn't have to equal b (it's not necessarily true that a equals b)
**Lexor:** `kani no- samo m1 m2` — m1 and m2 might be different (it's possible that they aren't equal)

**The words:**
- `kani` = "might," "may," "is possibly." Mnemonic: English/German *can* / *kann*.
- `musi` = "must," "is necessarily." Mnemonic: English/German *must* / *muss*.

Both go at the very start of a sentence. Both can be combined with `no-` from Level 7 to give four readings: "might be the case," "might not be," "must be," "doesn't have to be."

**What this level shows:**
- The distinctions English collapses into "is" / "could be" / "might be" / "doesn't have to be" are clearly separate in Lexor.
- This is *epistemic* modality — about what the speaker thinks is possible or necessary. Permission and obligation ("you may smoke here," "you must wear a helmet") are a separate kind of modality that hasn't been added yet.

---

## L13b — Numerical probability

Sometimes you want to attach a specific probability to a claim, like "90% likely." Lexor uses `chani` for this.

**Lexor:** `chani zo demu ne zo pluve` — it will rain with probability 0.90
**Lexor:** `chani zo demu fi samo a b` — a equals b with probability 0.5
**Lexor:** `chani magu zo demu fi pluve` — the probability of rain is greater than 0.5

**How it works:**
- `chani` goes at the start of the sentence, like `kani` and `musi`.
- After `chani` comes a number, then the rest of the sentence.
- The number is a fraction between 0 and 1, where 0 means "impossible" and 1 means "certain."
- Mnemonic: English/French *chance*.

The number itself is built from digits: `zo demu ne zo` is "zero point nine zero" = 0.90 in decimal. (The `demu` is the decimal point.)

**Relating `chani` to the earlier `kani` and `musi`:**
- `chani zo X` = "X has probability 0" = impossible. Same as `no- kani X`.
- `chani pa X` = "X has probability 1" = certain. Same as `musi X`.
- `kani X` (without a number) is "X is possible to some unspecified degree."

**Conditional probability** uses `dati` from Level 12: `chani zo demu ne zo X dati Y` reads as "X has probability 0.9 given Y." That's the probability of X assuming Y.

**What this level shows:**
- You can attach a specific numeric probability to any sentence without awkward "it's 90% likely that…" wrappers.
- `chani` is different from the amount-precision markers (`piru` for "approximately," `tomu` for "between"). Those attach to a single number; `chani` attaches to a whole sentence.

---

## L14 — Talking about axes, directions, and dimensions

For directions ("upward"), locations ("the top"), and dimensions ("the height"), Lexor uses a small system based on three new words plus the place-connectors you already know.

**Lexor:** `gol aksi fasa magu e` — she goes forward
**Lexor:** `aksi lata magu` — left direction (the positive Y direction)
**Lexor:** `aksi sura minu` — down direction (the negative Z direction)
**Lexor:** `tipi aksi sura magu bra [box] keti` — the top of the box (the extreme point at the upper end)
**Lexor:** `mezi aksi pa bra [box] keti` — the longest dimension of the box
**Lexor:** `mezi aksi sura bra [box] keti` — the height of the box (the size along the up-down axis)

**The pieces:**
- `aksi` means "axis" — a line that goes through space in one direction.
- `tipi` means "the extreme point" or "the end of an axis."
- `mezi` means "size along an axis" (a length, a width, a height, etc.).
- `magu` and `minu` mark which end of an axis: `magu` = the positive end, `minu` = the negative end. (You've seen them before as "greater than" and "less than" — Lexor reuses them.)

**Two ways to identify an axis:**

*By the body's reference frame* (an observer's forward-backward, left-right, up-down):
- `aksi fasa` = the front-back axis (= the X axis)
- `aksi lata` = the left-right axis (= the Y axis)
- `aksi sura` = the up-down axis (= the Z axis)

*By size rank* (orientation doesn't matter):
- `aksi pa` = the longest dimension (rank 1)
- `aksi du` = the middle dimension (rank 2)
- `aksi re` = the shortest dimension (rank 3)

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
| `rot zo dozu re aksi sura e` | she turns 90° to the left (1/4 of a full turn around the Z axis) |
| `rot zo dozu sa aksi sura e` | she turns around (180°, 1/2 of a full turn) |
| `rot minu zo dozu re aksi sura e` | she turns 90° to the right (negative 1/4 turn) |
| `rot zo dozu pa aksi lata e` | she tilts forward 30° (1/12 of a turn around the Y axis) |

**How the numbers work:**

The number is just the fraction. So 1/4 of a turn = 0.25 in decimal = 0.3 in dozenal (base 12).

In dozenal — Lexor's natural base for angles, because 12 divides evenly into many useful angles:
- `zo dozu pa` = 1/12 = 30° (the `dozu` is the dozenal decimal point)
- `zo dozu du` = 2/12 = 60°
- `zo dozu re` = 3/12 = 90°
- `zo dozu sa` = 6/12 = 180°
- `zo dozu pa sa` = roughly 1/8 = 45°

**Direction of positive turn:**

A positive turn (no minus sign) means *right-handed* rotation around the named axis. For `aksi sura` (the Z axis, pointing up), that's counterclockwise when you look down from above — which is *leftward* for someone facing forward.

If you're used to a clock face, this is flipped: clock hands go clockwise (which is *negative* in Lexor for rotation around Z), and 9 o'clock (the left side of a clock face) corresponds to a positive 1/4 turn (0.25). It's consistent with physics convention; takes a moment to get used to.

**What this level shows:**
- Any angle around any axis can be expressed compactly with no new vocabulary — just the rotation verb, a number, and the axis name.
- Compass-like directions are reachable: forward = 0, left = +1/4, back = +1/2, right = +3/4 (or −1/4).

---

## L16 — Grouping inside a sentence (brackets)

When a sentence has multiple parts that could group different ways, Lexor uses a pair of bracket-words: `bra` (opens a group) and `keti` (closes a group). Mnemonic: English "bracket" split into bra-ket.

**Lexor:** `tomu bra re keti bra ko zo zo keti e` — "I can do between 3 and 400 (pushups)"
**Lexor:** `bra loma A e kune loma B e keti vele loma C e` — "(she eats A and she eats B) or she eats C"
**Lexor:** `loma A e kune bra loma B e vele loma C e keti` — "she eats A and (she eats B or she eats C)"

**When you need them:**
- When a number-operator like `tomu` (between) takes two numeric arguments. Without brackets, "tom 3 400" would all get read as one big number because Lexor concatenates adjacent digits.
- When you want to mix "and" and "or" in the same sentence. Flat mixed forms are not allowed; brackets make the grouping unambiguous.
- Anywhere else you'd want grouping for clarity.

**Nesting:**

If you have brackets inside brackets, each `keti` closes the most recent unclosed `bra` — same rule as math parentheses.

---

## L17 — Naming a piece of sentence for reuse

When you want to use the same phrase several times without retyping it, give it a name with `defi`.

**Lexor:** `defi vari p loma A e kune loma B e. vari p vele loma C e`
**Translation:** "Let p be 'she eats A and she eats B'. (p) or she eats C."

**Lexor:** `defi vari x samo [biggest prime anta pa zo zo]. magu vari x fi zo`
**Translation:** "Let x be the biggest prime before 100. x is greater than 50."

**Lexor:** `nulu defi vari x`
**Translation:** "x is no longer defined." (Explicit erasure of a name you had bound.)

**The pieces:**
- `defi` introduces a name-binding.
- `vari <name>` references a name you've defined. The first time, it's the name being introduced; later times, it stands in for the expression.
- `nulu defi vari <name>` removes the binding. Defining the same name again replaces the old binding.

**What this level shows:**
- Use `defi` to name long expressions so a later sentence can refer back to them compactly.
- The name stays defined as long as the conversation continues (until you erase it or define it differently).
- Note that `defi` is for *naming for reuse*. For just splitting up a confusing sentence so groupings are clear, use the brackets from Level 16 instead.

---

## L18 — Composing several features

A small collection of worked examples. With vocab batch 1 (2026-05-18), most everyday concepts are now real Lexor words. Only specialized vocabulary (like "meter" and "box") still appears as `[bracketed]` placeholders.

### Example 1: Morning scene

```
vige fema. some nina. kere vat fema. labe e.
```

Word-by-word:
- `vige fema` — wakes-up, the-woman.
- `some nina` — sleeps, the-child.
- `kere vat fema` — asks-for, water, the-woman.
- `labe e` — works, she.

Translation: "The woman wakes up. The child sleeps. The woman asks for water. She works."

What this demonstrates: simple verb-object-subject (VOS) sentences using content nouns. Conjugated verbs (`vige` wakes, `some` sleeps, `kere` asks-for, `labe` works). Pronoun continuity — `e` in the last sentence refers back to `fema` from earlier.

### Example 2: Trade

```
kope kasa vira. vezo lapa fema.
```

Word-by-word:
- `kope kasa vira` — buys, house, man.
- `vezo lapa fema` — sold, stone, woman.

Translation: "The man buys the house. The woman sold the stone."

What this demonstrates: noun subjects (not pronouns), and adjacent sentences in different tenses — present (`kope` = buys) and past (`vezo` = sold).

### Example 3: She might come home

```
dike e ke kani veni kasu.
```

Word-by-word:
- `dike e` — says, she.
- `ke` — that.
- `kani veni kasu` — might come-future to-house.

Translation: "She says she might come home."

What this demonstrates: a complement clause introduced by `ke`, with a modal (`kani`) inside the embedded clause, and recipient role on a noun (`kasu` = `kas` + `-u` recipient-role vowel = "to the house").

### Example 4: Navigation order

```
golu aksi fasa magu pa zo [metr]. rotu zo dozu re aksi sura. golu aksi fasa magu fi [metr].
```

Translation: "Go forward 10 meters. Turn 90° left. Go forward 5 meters."

Three imperatives in a row, chaining motion and rotation. The axis system plus the angle convention give a compact, unambiguous navigation language — useful for driving instructions, robotics, game commands, or military communications.

`golu` and `rotu` are imperative forms (root + `-u`). Subject is dropped in imperatives. `[metr]` is a placeholder; "meter" doesn't have an assigned root yet.

### Example 5: Hedging a measurement

```
kani samo re [metr] mezi aksi pa bra [box] keti. kani minu. no-visc y i.
```

Translation: "The longest dimension of the box might be 3 meters. It might be less. I haven't seen it."

What this demonstrates: how `kani` lets a speaker hedge cleanly. Compare to English "it's 3 meters… maybe? I don't know" which needs three separate clauses to do the same job. `[box]` and `[metr]` are placeholders. `no-visc y i` is the perfect tense ("have not seen") + "I" + "it."

### Example 6: A small reasoning chain

```
dati labe vira. dati some nina. ergi no-vige nina kawa ke labe vira.
```

Word-by-word:
- `dati labe vira` — given, works, man.
- `dati some nina` — given, sleeps, child.
- `ergi no-vige nina kawa ke labe vira` — therefore, not-wakes-up, child, because that works man.

Translation: "Given that the man works. Given that the child sleeps. Therefore the child does not wake up, because the man works."

What this demonstrates: reasoning particles (`dati` premise, `ergi` therefore), causal subordinator (`kawa ke` because-that), negation on a verb (`no-vige`), and real content nouns and verbs throughout — no placeholders at all.

---

## Closing notes

This walkthrough covers most of the locked grammar. The remaining details are in `decisions.md` (the log of settled choices) and `examples.md` (a denser reference with many more example sentences).

Open design questions are tracked in `tasks.md`. Unmet design goals are in `trials.md` — `grep` for `[.*, open]` to see them all.

The vocabulary is being built out incrementally. As of vocab batch 1 (2026-05-18), the lexicon has 185 entries covering common verbs, nouns, and adjectives — enough for most everyday topics. Specialized vocabulary (units of measurement, less common objects) still appears as bracketed placeholders. The priority list for filling those in is in `frequencies.yaml`.

If a sentence shape here parses two ways in your head, that's either a bug in the walkthrough or a real ambiguity worth filing as a `[trap]` entry in `trials.md`. Both are useful to flag.
