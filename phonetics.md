## Phoneme-to-Character Mapping
| **Phoneme** | **IPA Symbol** | **Proposed Character** | **Type**    | **Articulation/Description**          | **Origin/Notes**        |
|-------------|----------------|-------------------------|-------------|----------------------------------------|--------------------------|
| a           | /a/            | `a`                   | Vowel       | Open front unrounded vowel             | Standard vowel           |
| e           | /e/            | `e`                   | Vowel       | Close-mid front unrounded vowel        | Standard vowel           |
| i           | /i/            | `i`                   | Vowel       | Close front unrounded vowel            | Standard vowel           |
| o           | /o/            | `o`                   | Vowel       | Close-mid back rounded vowel           | Standard vowel           |
| u           | /u/            | `u`                   | Vowel       | Close back rounded vowel               | Standard vowel           |
| æ           | /æ/            | `c`                   | Vowel       | Near-open front unrounded vowel        | Distinct vowel sound     |
| y           | y              | `y`                   | Vowel       | Open-mid back unrounded vowel          | Open-mid back unrounded vowel. |
| x           | /ʃ/            | `x`                   | Consonant   | Voiceless postalveolar fricative (sh)  | Chosen for the `sh` sound |
| ch          | /t͡ʃ/          | ch                    | affricate   | Voiceless postalveolar affricate (ch)  | As in Spanish "chico"    |
| p           | /p/            | `p`                   | Consonant   | Voiceless bilabial plosive             | Plosive                  |
| t           | /t/            | `t`                   | Consonant   | Voiceless alveolar plosive             | Plosive                  |
| k           | /k/            | `k`                   | Consonant   | Voiceless velar plosive                | Plosive                  |
| b           | /b/            | `b`                   | Consonant   | Voiced bilabial plosive                | Plosive                  |
| d           | /d/            | `d`                   | Consonant   | Voiced alveolar plosive                | Plosive                  |
| g           | /g/            | `g`                   | Consonant   | Voiced velar plosive                   | Plosive                  |
| j           | /x/            | `j`                   | Consonant   | Voiceless velar fricative (Spanish j)  | As in Spanish "j" / German "Bach" |
| f           | /f/            | `f`                   | Consonant   | Voiceless labiodental fricative        | Fricative                |
| s           | /s/            | `s`                   | Consonant   | Voiceless alveolar fricative           | Fricative                |
| v           | /v/            | `v`                   | Consonant   | Voiced labiodental fricative           | Fricative                |
| z           | /z/            | `z`                   | Consonant   | Voiced alveolar fricative              | Fricative                |
| l           | /l/            | `l`                   | Consonant   | Alveolar lateral approximant           | Lateral                  |
| m           | /m/            | `m`                   | Consonant   | Bilabial nasal                         | Nasal                    |
| n           | /n/            | `n`                   | Consonant   | Alveolar nasal                         | Nasal                    |
| r           | /ɾ/            | `r`                   | Consonant   | Alveolar tap (Spanish single r)        | Rhotic                   |
| h           | /h/            | `h`                   | Consonant   | Voiceless glottal fricative            | Aspirate                 |

- So 24 characters in total. 7 vowels and 17 consonants.
- This means we can generate 17*7*17*7=14161 words in the format of CVCV. That's >50% of the active vocabulary of an average adult English speaker.
- By adding an extra syllable, we can generate $(17*7)^3 = 1\ 685\ 159$ words, which is more than we will ever need.
- Now the work is to make the language consistent. All these words will be easy to pronounce. All connectors and basic common words will be single-syllable words. The most common will be 2-syllable words. Then verbs will be in 'CVC' root + 'V' for conjugation. We have $2023$ possible verbs in this way. People usually use 200 verbs in a daily basis, and recognize about 2000.

### Unused Characters
q, w

### Unused Common Phonemes
- `/ə/` (schwa): as in sofa – Useful for unstressed syllables.
- `/ŋ/` (as in "song") → Velar nasal.
- `/ʒ/` (as in "measure") → Voiced postalveolar fricative.
- `/θ/` (as in "think") → Voiceless dental fricative.
- `/ð/` (as in "this") → Voiced dental fricative.
- `/tʃ/` (as in "chat") → Voiceless postalveolar affricate.
- `/dʒ/` (as in "judge") → Voiced postalveolar affricate.
- `/w/` (as in "we") → Voiced labial-velar glide.
- `/j/` (as in "yes") → Voiced palatal glide.

### Forbidden Phonetics
To ensure clarity and ease of articulation, the following phonetic rules are forbidden:

1. **Words ending with the `k` sound**:
    - Avoid ending words with `k` to reduce abrupt stops in flow.
    - Example: `pak` → Invalid, `pax` → Valid.

2. **Repeated identical consonants**:
    - Avoid sequences like `kk`, `ss`, or `tt`.
    - Example: `katto` → Invalid, `kato` → Valid.

3. **More than two consecutive vowels**:
    - To avoid ambiguity or pronunciation difficulty.
    - Example: `aai` → Invalid, `ai` → Valid.

4. **Combination of `ʃ` (`x`) and `z`**:
    - This creates acoustic overlap; avoid sequences like `xzi`.

5. **Clusters of more than two consonants**:
    - Restrict consonant clusters to a maximum of two consecutive consonants.
    - Example: Valid → `plu`, Invalid → `pltra`.

6. **Vowel following `h`**:
    - Avoid starting a word with `h` directly followed by a vowel to reduce breathy or unclear transitions.
    - Example: `ha` → Invalid, `ha` prefixed with a consonant → Valid (`sha`, `pha`).

7. **Silent Letters**:
    - All characters must represent a distinct phoneme. Silent letters are disallowed to maintain 1-to-1 phoneme-to-character mapping.
    - Example: `knee` → Invalid; `ne` → Valid.

8. **Words starting with `z` and ending with `s` or `x`**:
    - This sequence is phonetically unstable and may cause slurring in rapid speech.
    - Example: `zis`, `zix` → Invalid.

## Prosody

### Word boundary

Word boundaries are inferable from morphology alone — Lexor uses **self-segregating morphology**. No mandatory pause is required between words; a speaker can talk at natural pace and the listener will still parse boundaries unambiguously.

The mechanism is built from three rules working together:

1. **Open-class content roots must start with a consonant.** Every verb, noun, and adjective root begins with a consonant. (See decisions.md 2026-05-17.)
2. **Content words end in a vowel.** Verbs are `CVC + V` (root + tense vowel); derived non-verbs are `CVCVCV`.
3. **Closed-class items are a finite, memorizable list.** Markers, prepositions, copulas, pronouns, and digits include some vowel-initial forms (`is`, `erg`, `imp`, `aks`, `est`, `int`, `oks`, `ant`, plus the V-shape pronouns `y u e i`). The listener identifies these by direct lookup.

How parsing works under these rules:

- After a vowel-final word, if the next sound is a consonant, the boundary is obvious — a new word is starting.
- After a vowel-final word, if the next sound is a vowel, the next word must be one of the finite closed-class vowel-initial items; lookup decides which.
- After a consonant-final closed-class word, if the next sound is a consonant, the boundary is obvious.
- After a consonant-final closed-class word, if the next sound is a vowel, the next word must again be from the closed-class vowel-initial list — content words can't start with a vowel.

Worked examples:

- `sa magas` (digit 6 + content `magas`) vs `sam agas` (operator + ???) — `agas` starts with a vowel, isn't a closed-class item, and content roots can't begin with vowels. So `sam agas` doesn't parse. The unique reading is `sa magas`.
- `ko mago` (digit 4 + content `mago`) vs `kom ago` (verb + ???) — `ago` starts with a vowel and isn't closed-class. So `kom ago` doesn't parse. Unique reading: `ko mago`.

### Recommended pause for clarity

A short acoustic break (~50–100 ms) between words is **recommended for clarity**, especially in noisy environments, at speed, or with non-native listeners. But it is **not required by the grammar**. A speaker who runs words together still produces parseable Lexor — the morphology guarantees uniqueness.

This matches how natural languages work. English and Spanish speakers don't pause between every word; listeners parse boundaries from stress, vowel quality, and word-shape expectations. Lexor's self-segregating morphology gives a similar effect through stricter word-shape rules.

### Numbers
Inside a digit stream (sequence of digit roots forming one number), the digits are **concatenated with no internal break**. The number forms a single prosodic unit. The unit closes when a non-digit word follows or when the base marker (`dem`/`doz`) or scale marker (`pem`) appears at its boundary position.

Examples:
- `sa pa du` (642 in some base) → one prosodic unit `sapadu`, no internal breaks.
- `sa pa du dem chi` (642.7 decimal) → `sapadu` [break] `dem` [break] `chi` — the radix marker `dem` is its own unit.
- `sa dim` (6 days) → `sa` [break] `dim` — `dim` is not a digit, so the digit stream closed before it.

### Pronouns
Pronouns are V or CV shape (`y`, `u`, `e`, `la`, etc.), shorter than the standard CVCV word. They still get their own prosodic unit and their own brief break before and after. Pronoun + role vowel (e.g. `y-e`, `u-o`) is one unit (the role vowel is a suffix, not a separate word); doubled vowels (`ee`, `uu`, `loo`) are pronounced as a single long vowel held about twice the duration of a short vowel.

### Clause boundary (comma in writing)
A clause boundary is marked by **a longer pause (≈200–300 ms) plus a slight pitch reset**. This is the spoken equivalent of the comma. It separates:
- Main clause from subordinate clause: `golo e [break-long] tep ke pluvex` — "she left, when it was raining."
- Coordinated clauses joined by `kun` / `vel`: `kome e [break-long] kun bibe e` — "she eats, and she drinks."
- Tag-question hosts from the tag: `golo e [break-long] ka` — "she left, right?"
- Reasoning-particle transitions: `dat A [break-long] erg B` — "given A, therefore B."

The comma boundary is acoustically distinguishable from the word boundary by **duration and pitch reset** combined. A word-break is a short flat micro-pause; a clause-break is a longer pause plus a fresh pitch starting point on the next clause.

### Sentence boundary
Sentence boundaries get **a full pause (≈500 ms or more) plus a complete pitch reset**. Spoken equivalent of the period. Longer than a clause boundary.

### Stress
Each word carries **primary stress on its first syllable** (the root onset). Derived non-verb forms (CVCVCV) have a secondary stress on the suffix. Numbers stress the first digit of the stream. Stress is not lexical — it never distinguishes minimal pairs — but it aids parsing by giving the listener a regular rhythm.

Stress is also used for **focus**: a word the speaker wants to emphasize can take heavier-than-default primary stress without changing meaning. Per the precision-by-default principle, focus is a pragmatic overlay, not a scope-resolution mechanism — scope is already pinned by the strict positional rules.
