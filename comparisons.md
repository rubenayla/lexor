# Comparisons — Lexor vs other constructed languages

Honest comparisons with prior projects that share design goals. The goal is to make differentiation explicit, learn from mature work, and answer the legitimate question: "has this already been done better?"

Current entries:
- [Lojban](#lojban) — the most direct predecessor by design goals.

(Esperanto, Toki Pona, Ithkuil, Sona, etc. can be added later if relevant.)

---

## Lojban

### What it is

Lojban (pronounced LOZH-bahn) is a constructed logical language. It descended from Loglan in 1987 after an IP dispute, and has been actively developed by the Logical Language Group for over 30 years. The official reference is the *Complete Lojban Language* (cll.lojban.org), commonly called CLL. It has a small but persistent community, a YACC grammar, dictionaries, and some literature.

Lojban was designed to be:
- **Syntactically unambiguous** — every well-formed sentence has exactly one parse tree. The grammar is given as a LALR(1) parser, so unambiguity is provable.
- **Culturally neutral** — vocabulary derived algorithmically from the six most-spoken natural languages (Mandarin, English, Hindi, Spanish, Russian, Arabic), weighted by speaker counts.
- **Based on predicate logic** — every verb-like word ("selbri") has a fixed set of numbered argument places.
- **Self-segregating in speech** — word shapes are constrained so word boundaries fall out of sound, with no need for pauses.
- **Free of mandatory grammatical categories** — no obligatory tense, number, gender, definiteness.

These are essentially Lexor's design goals too. Lojban hit many of them first, and more rigorously.

### Where Lexor and Lojban agree (shared design goals)

| Goal | Lojban | Lexor |
|---|---|---|
| Every sentence has one meaning | ✓ central design goal | ✓ "vague allowed, ambiguous forbidden" meta-principle |
| Self-segregating morphology | ✓ strict word-shape rules | ✓ consonant-initial content + closed-class lookup (2026-05-17) |
| No mandatory tense | ✓ tense is optional cmavo | ✓ atemporal vowel `a` is the default |
| No mandatory gender | ✓ neutral 3rd-person pronoun | ✓ `e` covers he/she/singular-they |
| No mandatory number | ✓ number is optional | ✓ no plural marker; quantity is optional |
| Subject droppable | ✓ pro-drop | ✓ VOS with optional subject |
| Closed-class structure words | ✓ "cmavo" | ✓ markers/prepositions/copulas as closed class |
| Sourced from natural languages | ✓ algorithmic blend of 6 | partial — Latin/English/Spanish, more Eurocentric |
| Compositional grammar | ✓ predicate logic | ✓ position + role vowels + markers |
| No tone | ✓ | ✓ |

So at the design-goal level, the overlap is large. If Lojban achieves all of these, the legitimate question is what differentiates Lexor.

### Feature-by-feature comparison

#### Word shapes

**Lojban** distinguishes word classes by phonotactic shape, which is what makes the morphology self-segregating without pauses:
- **gismu** (root words): exactly 5 letters, shape CVCCV or CCVCV. Examples: *klama* (come), *vecnu* (sell). Always two syllables.
- **cmavo** (structure words / closed class): 1–2 syllables, shapes like V, VV, CV, CVV. Many of them — hundreds, organized into selma'o classes.
- **lujvo** (compounds): glued from gismu fragments by rule.
- **fu'ivla** (loanwords): special category with its own shape constraints.

**Lexor** uses simpler, shorter shapes:
- **Content roots**: CVC (3 letters, 1 syllable), with grammatical vowels attached: `lome` (eats), `lomera` (current eater).
- **Closed-class**: ranges from V (pronouns like `y`, `e`) to CVCC (`erg`, `imp`) to CVC (most markers).

The trade-off: Lexor is shorter and more compact, easier to pronounce, but with less vocabulary headroom (CVC space is ~2000 roots) and more risk of collisions. Lojban's longer shapes give more vocabulary space and more morphological cushion, but every content word costs two syllables minimum.

#### Argument structure

**Lojban** uses fixed numbered argument places ("sumti slots") per predicate. *klama* (come) has 5 places:
1. x1 = the goer
2. x2 = the destination
3. x3 = the origin
4. x4 = the route
5. x5 = the means of transport

Each slot has a fixed semantic role. You can omit slots (they default to "unspecified") or reorder with explicit tagging cmavo.

**Lexor** uses VOS word order plus optional role vowels (subject `-e`, object `-o`, recipient `-u`, instrument `-i`). For three-argument verbs, role vowels disambiguate. For two-argument verbs, position is enough. There are no fixed numbered slots — the language is closer to natural-language case marking than to predicate logic.

The trade-off: Lojban's approach is more rigorous (every verb's slots are part of its lexical entry), more uniform, and unambiguous by construction. Lexor's approach feels more natural for human speakers and is less prescriptive about how a verb's "frame" should look.

#### Tense and aspect

**Lojban** has many tense and aspect cmavo (~20+ for fine distinctions: past, future, near-past, distant-past, completive, inceptive, continuative, etc.). They compose freely.

**Lexor** has 7 tense vowels (atemporal, present, past, future, imperative, conditional, perfect) attached to verb roots, plus continuous aspect `x`. Coarser-grained.

Trade-off: Lojban can express precise temporal distinctions; Lexor optimizes for compactness with the most common distinctions covered.

#### Logical connectives

**Lojban** has a rich set of logical connectives (jeks, joiks, gi'iks) with explicit scope. Mixed AND/OR, conditionals, and other operators all have well-defined scope rules.

**Lexor** has `kun` (AND) and `vel` (OR) plus `bra/ket` brackets for grouping. Mixed AND/OR in flat form is grammatically forbidden — speakers must bracket.

Trade-off: Lojban handles logical complexity by having more vocabulary; Lexor by having a single grouping mechanism plus a small operator set.

#### Modality

**Lojban** has cmavo for possibility, necessity, attitudinal indicators, evidentiality (source of information). Quite rich — Lojban can express "I assert that this happened, I learned it from a third party, and I'm uncertain about it" as a single sentence with stacked attitudinal markers.

**Lexor** has `kan` (possibility ◇), `mus` (necessity □), `chan` (graded probability with explicit number). Evidentiality is parked (trial H4). Attitudinal markers haven't been designed yet.

Trade-off: Lojban is more developed here; Lexor has the modal infrastructure but hasn't built up to attitudinal/evidential yet.

#### Numbers

Both languages support arbitrary bases, exact counts, ranges, approximation. Both use compositional digit streams. Lojban has dedicated cmavo for many numeric concepts (Lexor uses `tom`, `pir`, `mag`, `min`, `pem`).

Trade-off: roughly equivalent. Lexor's first-class dozenal support is a stronger commitment than Lojban's (Lojban has multi-base support but doesn't privilege dozenal).

#### Pronouns and reference

**Lojban** has personal pronouns (mi = I, do = you, etc.), demonstratives, anaphora (referring back to earlier mentions). The system is rich but learners often struggle.

**Lexor** has 11 pronouns covering all six combinations of speaker/listener/other × singular/plural × person/object, plus the distinction between "we generic" and "we specific subgroups." Smaller and more systematic.

Trade-off: Lexor's pronoun system is one of its cleanest design wins — arguably more elegant than Lojban's, and certainly more compact.

#### Self-segregating morphology

This is the rule that lets you talk without pausing between words.

**Lojban** achieves it through strict phonotactic rules on each word class. Gismu's CVCCV/CCVCV shape can't accidentally match a cmavo + cmavo concatenation or any other valid run. The rules are proven to give unique segmentation.

**Lexor** achieves it (as of 2026-05-17) through: content roots are consonant-initial and vowel-final; closed-class is a finite memorizable list. The reasoning is more informal than Lojban's but the structural guarantee is the same.

Trade-off: Lojban's morphology has been formally verified by decades of usage. Lexor's is freshly locked and needs empirical stress-testing as vocabulary grows.

### Where Lojban is currently more mature than Lexor

Honest assessment:
- **Vocabulary:** Lojban has ~1300+ gismu and thousands of lujvo and cmavo. Lexor has 137 entries.
- **Documentation:** Lojban has the CLL (a book), several dictionaries, online learning resources, a YACC grammar. Lexor has a handful of markdown files.
- **Speakers/community:** Lojban has a small but real community with conversational ability. Lexor is a personal design project.
- **Formal grammar:** Lojban's grammar is given as LALR(1) and parseable by machine. Lexor's grammar is informally specified across decisions.md.
- **Literature:** Lojban has translated stories, songs, and original works. Lexor has 60+ example sentences.
- **Modal/evidential system:** Lojban's is rich; Lexor's is starting.

If maturity is what matters, Lojban wins decisively. Lexor is a young project covering similar ground.

### Where Lexor's choices differ — design points it could win on

Three legitimate differentiators:

1. **Simplicity of word shapes.** CVC is shorter than CVCCV. A Lexor verb plus its tense vowel is two syllables; a Lojban gismu is two syllables before any grammatical material attaches. For everyday speech, Lexor is more compact.

2. **Natural-language feel.** Lexor preserves Latinate roots and ordinary-sounding words (`lom` from "comer/eat," `vis` from "see/visus"). Lojban's algorithm-blended roots feel alien to most speakers. This makes Lexor more learnable for speakers of European languages — at the cost of being less culturally neutral.

3. **Smaller closed class.** Lexor's closed class is in the tens of items; Lojban's is in the hundreds. Less to memorize for a beginner.

These are aesthetic and ergonomic differences, not technical ones. Lojban achieves more (precision, neutrality, formal verification) at the cost of being notoriously hard to learn. Lexor is betting on a different point in the trade-off space — closer to natural-language ergonomics, with less formal rigor but less learning curve.

Whether that's "better" depends on what you want.

### What Lexor can learn from Lojban

- **Formal grammar specification.** Lexor's grammar lives across decisions.md, examples.md, and trials.md in prose. Eventually a formal grammar (PEG, EBNF, or similar) would let parsing be tested mechanically. Lojban's LALR(1) is a model.
- **Attitudinal and evidential markers.** Lojban's UI/evidential system is a solved problem; Lexor could borrow the architecture (closed-class markers stacking after the predicate) when those land.
- **Compound word formation.** Lojban's lujvo system gives rules for combining gismu into compounds without losing the underlying meanings. Lexor's compound vocabulary is parked; Lojban's approach is worth studying when this round comes.
- **Self-segregation as proof.** Lojban can prove its segmentation is unique. Lexor's argument (2026-05-17) is informal; tightening it into a verifiable claim is worth doing.

### Should Lexor continue?

This is a fair question. Honest answer:

If the goal is "build a precise, unambiguous language from first principles," Lojban already exists, has 30 years of development, and is more rigorous than Lexor is likely to become in any reasonable timeframe. Investing in learning Lojban would yield more communicative power than continuing to build Lexor.

If the goal is something more like "design a language that's *also* learnable and natural-feeling for speakers of European languages, optimizing for short common words and a small closed class," Lexor occupies a different point in the design space. Lojban is famously hard to learn; Lexor is betting that simpler shapes plus Latinate roots plus a tighter closed class give a better learnability/precision trade-off.

If the goal is "enjoy designing a language and learning from the design process," then comparison-to-existing-projects is informative but not decisive. Lexor is still worth doing.

The strongest argument for continuing: Lexor is making concrete design choices that Lojban explicitly didn't (privileging dozenal, prioritizing learnability over neutrality, simpler word shapes). Those choices have value even if Lojban exists.

The strongest argument against: there's a real risk of building a less-good Lojban. Worth being honest about which design choices are genuinely better and which are just different.

### Sources

This comparison draws on general knowledge of Lojban. The canonical source is the *Complete Lojban Language* (cll.lojban.org). The Wikipedia article (https://en.wikipedia.org/wiki/Lojban) is a good entry point. Specific feature claims in this document have not been verified against the current CLL — corrections welcome.
