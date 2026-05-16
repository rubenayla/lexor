# Comparisons — Lexor vs other languages

Honest comparisons with both natural languages (English, Spanish, …) and constructed ones (Lojban, …). Each comparison asks two questions:
- For constructed languages with overlapping design goals: "has this been done better?"
- For natural languages: "what does Lexor fix, and what does it sacrifice?"

The two kinds of comparison have different shapes. Constructed-language comparisons are about technical differentiation. Natural-language comparisons are about trade-offs — Lexor wins on precision but loses on familiarity, corpus, and depth.

Current entries:
- [Lojban](#lojban) — closest predecessor by design goals.
- [English](#english) — natural reference point for most readers; many trial cases come from English's failures.
- [Spanish](#spanish) — natural reference point with several Lexor decisions borrowed (ser/estar split, sentido, pronoun-drop) and several explicitly rejected (mandatory gender, accents, conjugation irregularity).

(Esperanto, Toki Pona, Ithkuil, Sona, Mandarin, Latin, etc. can be added later if relevant.)

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

## English

### Framing

English is the natural reference point for most Lexor readers, and many of the trial cases in `trials.md` and `pain.md` come from places where English fails. But English also does some things well that Lexor sacrifices. This section is the honest two-sided ledger.

### What English does well that Lexor sacrifices

- **A vast established vocabulary.** ~170,000 currently-used words; billions of hours of text and audio corpus; comprehensive dictionaries. Lexor has 138 entries.
- **A native speaker community of ~1.5 billion people** (~400M native, ~1.1B as a second language). Lexor has none.
- **Redundancy.** English packs the same meaning into multiple cues (word order, agreement, intonation, idiom). You can mishear half a sentence and still recover meaning. Lexor's compact CVC roots carry less redundancy — a single misheard consonant can change the meaning, especially since vocabulary will eventually be dense in CVC space.
- **Idiomatic compactness.** "Get over it," "make do," "look up to" — multi-word phrases that compress meaning that Lexor would have to spell out compositionally.
- **Pedagogical maturity.** Billions of dollars of teaching materials, immersion contexts, books for every skill level. A learner of Lexor reads markdown files.
- **Cultural depth.** Centuries of literature, scientific corpus, idiom, slang, register variation. Lexor has 60 example sentences.
- **Adapted to human cognition by evolution.** English's irregularities are largely the result of high-frequency words resisting regularization — the irregular forms are easier to access mentally. Lexor's regularity is uniform but doesn't pre-optimize for frequency.

### What Lexor fixes (vs English)

A condensed version of `pain.md` and `trials.md`, restated as comparison:

- **Mandatory number.** English forces "a dog" vs "dogs" even when count is irrelevant or unknown. Lexor: number is an optional modifier.
- **The "is"-overload.** English collapses identity (Mark Twain is Samuel Clemens), essential predication (the sky is blue), state predication (she is tired), set membership (a whale is a mammal), subset (mammals are animals), existence (there is a god), and literal identity (the password is "incorrect") into one verb. Lexor splits these: `sam` / `est` / `sta` / `mem` / `tot+mem` / `kel` / `lit…fin`.
- **Negation scope.** "Not a equals b" is ambiguous between "never equal" and "doesn't have to equal." Lexor: positional `no-` with explicit modal operators (`mus`, `kan`) for the necessity reading.
- **"Top" vs "up" vs "height" conflation.** English uses "up" for direction and "top" for both location and quasi-direction. Lexor: `aks sur mag` (direction), `tip aks sur mag bra X ket` (location), `mez aks sur bra X ket` (magnitude).
- **Tense/aspect tangle.** English perfect, continuous, modal forms don't compose cleanly ("I might have been going to have eaten"). Lexor: one vowel = tense, one consonant `x` = continuous aspect, modals separate at sentence-start.
- **Modal soup.** "Have to" / "must" / "may" / "might" / "could" / "should" each carry subtly different mixes of epistemic and deontic modality. Lexor: epistemic split (`kan`, `mus`, `chan`) with deontic explicitly parked, no conflation.
- **Lexical sprawl for question words.** Who/what/when/where/why/how — six different words. Lexor: one particle `ka`, position determines type.
- **Mixed AND/OR ambiguity.** "A and B or C" parses two ways. Lexor: forbidden in flat form; brackets required.
- **Compound-noun ambiguity.** "Its tube ends were round" — `tube` modifying `ends`, or `ends` as verb? Lexor: adjective suffix on modifier disambiguates morphologically.
- **Gendered third person.** English forces he/she on every reference (singular "they" is gaining ground but still controversial in formal writing). Lexor: `e` is gender-neutral by default.
- **Stress is unmarked in writing.** "I scream" vs "ice cream" — disambiguated only by spoken stress, not by spelling. Lexor: stress is non-lexical (always on first syllable).
- **Spelling irregularities.** English has hundreds of common words whose pronunciation can't be derived from spelling. Lexor: one-to-one phoneme-character mapping.
- **Number expression.** Million / billion / trillion / quadrillion — arms race with no end. Lexor: scientific notation `pem` handles arbitrary magnitudes.
- **Two clock conventions** (12-hour and 24-hour) with built-in ambiguity at noon/midnight. Lexor: digit stream + base marker, both bases first-class.

### What Lexor borrowed from English

- **Sub-constituent brackets `bra/ket`** — split from the English word "bracket."
- **Modal markers `kan` (can) and `mus` (must)** — direct phoneme rewrite of English/Germanic stems.
- **Probability marker `chan`** — English "chance."
- **Endpoint marker `tip`** — English "tip" (end of anything).
- **Several verb roots** when the English everyday word matched the concept: `xut` (shut, for close), `lis` (listen), `hav` (have), `lek` (read, via Latin but matches English "lecture" stem).
- **Stress as parsing aid** — English's reliance on first-syllable stress on content words shaped Lexor's first-syllable stress convention.
- **The basic concept of compositional negation** with a single morpheme (English "un-/not-" partially inspired the `no-` prefix).

### What Lexor explicitly rejected from English

- **Mandatory tense on every verb.** English forces past/present/future. Lexor: atemporal default.
- **Mandatory number on nouns.** English forces singular/plural. Lexor: number is optional.
- **Spelling-pronunciation mismatch.** English's irregular orthography is the explicit anti-pattern motivating Lexor's one-to-one phoneme-character rule.
- **Word-order-only role marking.** English's SVO ("subject-verb-object") is rigid and breaks down with pronoun fronting, passive, etc. Lexor: VOS plus optional role vowels handles the same cases more cleanly.
- **Gendered pronouns required.** English's he/she/it is rejected; gender is optional.
- **Single "you" for singular and plural.** Confusing in groups; Lexor splits `u` (singular) and `ly` (plural).
- **Multiple "we" forms collapsed.** English's "we" hides whether the listener is included; Lexor has five distinct forms.
- **Articles (a, the).** English forces definiteness commitment; Lexor: optional.
- **Lexical antonym families.** English's love/hate, hot/cold, etc. are independent roots in Lexor (`am`/`od` planned); no "opposite-of" morpheme.

### The trade-off, stated honestly

Lexor wins on precision; English wins on familiarity, redundancy, and corpus. Beating English at "being English" is not the goal — English wasn't designed for precision, it was selected for survival by hundreds of millions of speakers over a thousand years. Lexor accepts that it will never feel as natural as English for an English speaker. The bet is that for tasks where precision matters more than ergonomics (technical writing, legal text, scientific argument, multi-step reasoning), Lexor will be measurably better.

For everyday casual conversation, English will likely win on social comfort even if Lexor wins on technical accuracy.

---

## Spanish

### Framing

Spanish is the other natural reference point that shows up repeatedly in Lexor's design — both as a *source* (several decisions copied Spanish features) and as a *target of correction* (mandatory gender, accent marks, conjugation irregularities). The user grew up with Spanish, so several pain entries are Spanish examples ("Determinar el empuje... del difusor," ser/estar nuance, "yo voy el sábado" topic-fronting).

### What Spanish does well that Lexor sacrifices

- **Flowing rhythm with vowel-rich phonology.** Spanish's 5-vowel system and predictable stress give it a musical, easy-to-listen-to character. Lexor's vowel inventory is wider (7 vowels) but its rhythm is less established.
- **Native speaker community of ~500M.** Lexor has none.
- **Compact subjunctive mood for hypotheticals, desires, doubts.** "Espero que vengas" packs hope + uncertainty + future-orientation into the verb form. Lexor needs to compose this from `chan`, conditional vowel `y`, and a content verb for "hope."
- **Reflexive constructions for impersonal/passive ("se").** "Se ha decidido," "se vende" — compact ways to leave the agent unspecified. Lexor copies this in spirit (pronoun-droppable VOS).
- **Diminutives and augmentatives.** -ito / -ita / -ón / -ona attach to nouns to compactly express size, affection, or contempt ("perrito" = cute little dog; "casona" = imposing big house). Lexor would need separate adjectives.
- **Verb conjugations carry person + number + tense + mood** in one ending. Compact when you've memorized them, though irregular for high-frequency verbs.
- **Cultural depth.** Centuries of literature, regional variation (Castilian, Mexican, Rioplatense, Andean…), idiom and slang.
- **"Sentido"** — a precise word for direction-with-polarity along an axis. English has no clean equivalent. Lexor borrowed the concept (axis system, `aks <ax> <pol>`) but Spanish was here first.

### What Lexor fixes (vs Spanish)

- **Mandatory gender on every noun.** Spanish forces amigo/amiga, el/la, -o/-a. Lexor: no mandatory gender anywhere.
- **The ser/estar split is real but conjugation is irregular.** Spanish nailed the conceptual distinction (essence vs state), then drowned it in conjugation paradigms. Lexor: keeps the split (`est`/`sta`) with regular vowel-based tense, no irregularities.
- **Verb conjugation paradigms.** Spanish has 17+ regular tense/mood forms per verb × 6 person-number combinations, with multiple irregular families. A learner spends years memorizing. Lexor: one vowel encodes tense, pronouns are separate.
- **Mandatory subjunctive triggers.** Spanish's "que" clauses force subjunctive in unpredictable ways for non-native speakers. Lexor: no subjunctive; conditional vowel `y` and modal markers compose explicitly.
- **Number agreement across constituents.** "Los perros pequeños corren" forces agreement on article, noun, adjective, verb. Lexor: no agreement.
- **Accent marks.** Spanish uses ´ on stress when it's irregular, ñ for /ɲ/, ü occasionally. Lexor: no accents.
- **Letters that don't match phonemes one-to-one.** Spanish has c/qu/k overlap, gu/g, h silent, y/ll merger in many dialects. Lexor: one phoneme per character.
- **"Estamos a 14 de enero" / month-name memorization.** Spanish names the days and months. Lexor: numeric calendar (day-of-week 1–7, month 1–12).
- **Sí/no question intonation only.** Spanish lacks a dedicated question particle and signals questions purely by intonation (and inverted ¡? in writing). Lexor: explicit `ka`.
- **"Yo voy el sábado" ambiguity.** Whether "Saturday" is the day-of-going or a topic-fronting ("on Saturdays I do go," allowing other days) is unclear. Lexor: topic-fronting conventions are explicit (parked, but the infrastructure exists).
- **Lexical antonym pairs are sometimes morphological.** "Feliz / infeliz" is paired with the in- prefix, but "alegre / triste" is two unrelated roots. Inconsistent. Lexor: rejects opposite-prefixes; antonyms always get distinct roots.

### What Lexor borrowed from Spanish

- **The ser/estar distinction.** Possibly the single most impactful borrow. `est` (Spanish *ser*) / `sta` (Spanish *estar*) preserve the conceptual split.
- **"Sentido" as direction-with-polarity.** Built into the axis system (`aks fas mag` vs `aks fas min`).
- **Pronoun-droppable construction** ("se ha decidido").
- **Several content roots** where Spanish's everyday word matched the concept:
    - `lor` (cry/weep) from *llorar*
    - `tir` (pull/draw) from *tirar*
    - `mez` (measure) from *medir/metiri*
    - `mes` (month) from *mes*
    - `pag` (pay) from *pagar*
- **Awareness of resyllabification.** Spanish's word-boundary-dissolution informed Lexor's self-segregating morphology design — both languages avoid mandatory pauses, but Lexor handles it through stricter shape rules rather than predictable resyllabification.
- **Comma-based clause boundaries.** Spanish's heavy use of clause-internal commas matches Lexor's clause-boundary prosody.

### What Lexor explicitly rejected from Spanish

- **Mandatory gender.** The biggest rejection. Spanish-speaking Lexor learners will feel the absence of "el/la" cues most acutely.
- **Verb conjugation paradigms** (replaced by vowel inflection).
- **Mandatory articles** (el/la rejected).
- **Number agreement** rejected across constituents.
- **Pluralization morphemes** (-s/-es) rejected.
- **Accent marks** rejected; one phoneme per character means stress is non-lexical.
- **Subjunctive mood** rejected; replaced by `chan`/`kan`/`mus` + conditional vowel.
- **Two-letter digraphs** (ch, ll, rr) mostly rejected — Lexor keeps `ch` (one phoneme /tʃ/) and uses `x` for /ʃ/.
- **Ser/estar conjugation irregularity** — keeps the split, kills the irregularity.

### The trade-off, stated honestly

Spanish-speaking Lexor learners will gain precision and lose two things they're used to: the expressive subjunctive (compensated by composable modal markers), and the gender-based reference disambiguation (in a paragraph with two women, Spanish lets you say "la otra" to disambiguate; Lexor would need a name binding or contextual cue).

Lexor's pronoun system (no mandatory gender) is a clear win for many users, but in a multi-character narrative it costs disambiguation cheapness. A Spanish writer can write "ella le dijo a él que la quería" — gender alone disambiguates four references. Lexor would either use names, `def`-bindings, or accept the loss of disambiguation. This is a real cost.

The borrows are substantial enough that Spanish speakers should find Lexor more learnable than English speakers will — many of the conceptual moves (ser/estar, sentido, pronoun-drop) come from territory Spanish already navigates.
