# Tasks

Open design questions parked here so we can address them one at a time.

## Inbox
(empty — VOS question addressed; see history.md 2026-05-15)

## Design decisions to resolve
- [x] **Part-of-speech marking** — resolved: suffix, vowel-initial, universal word shape `CVC + V[C]`. Derivation consonants: `r` agent, `n` act, `t` patient, `s` adjective. See decisions.md and history.md 2026-05-15.
- [x] **Plural rule** — resolved: no plural inflection. Number is unspecified by default; quantity is a separate optional modifier system. See history.md 2026-05-15.
- [x] **Quantifier / quantity system framework** — resolved: digit-stream numbers, base markers `dem`/`doz` for decimal/dozenal first-class compatibility, scale via `pem` scientific notation, comparison operators `min`/`mag`/`sam`/`tom`/`pir` as CVC closed class. Quantifier follows noun. See decisions.md / history.md 2026-05-15. Sub-questions still open:
    - [x] **12 digit roots** — resolved: `zo pa du re ko fi sa chi bo ne` (0–9) plus `ja gi` (A, B for dozenal). See decisions.md / history.md 2026-05-15.
    - [x] **Prosodic disambiguation rule** for CV-vs-CVC overlap — resolved: obligatory brief acoustic break (~50–100 ms / light glottal) at every word boundary; digit streams concatenate as one prosodic unit. See phonetics.md "Prosody" section, decisions.md / history.md 2026-05-16.
    - [ ] **Distribution-shape roots** (gaussian, uniform, bimodal, etc.) for richer probabilistic quantifiers.
    - [ ] **Arbitrary-base spoken notation** (user's written `9_12.5` syntax — base-N representation of numbers).
    - [x] **Vague quantifiers** — partially resolved: `sol`/`tot`/`nul`/`kel` cover only/all/none/some. "Many"/"few" still open as fuzzy magnitude quantifiers.
    - [ ] "Many" / "few" / "most" — fuzzy magnitude quantifiers, distinct from the precise `tot`/`kel`.
- [x] **Trailing vowel for non-verb forms** — resolved: all words end in vowels (`CVCV(CV)`). Inner vowel reuses tense system; outer vowel is the role/case slot. See decisions.md and history.md 2026-05-15. Sub-questions still open:
    - [x] Which specific vowel = "atemporal / temporal-frame unspecified"? Resolved: `a`. Other tense vowels reassigned around it (see history.md 2026-05-15).
    - [x] Specific role-vowel assignments for outer slot — resolved: `a` default, `e` subject, `o` object, `u` recipient, `i` instrument. See decisions.md / history.md 2026-05-15.
    - [x] Pronoun behavior with role vowels — resolved: suffix role vowel, doubled-vowel collisions pronounced as long vowels. See decisions.md / history.md 2026-05-15.
    - [x] Temporal-modifier system framework — resolved: numeric calendar, time-relation prepositions (`tep`/`pen`/`sin`/`lim`/`ant`/`pos`), frequency operator `kex`, reference frame defaults to now (root `nun`), relative time by composition. See decisions.md / history.md 2026-05-15. Sub-questions still open:
        - [ ] 12-hour vs 24-hour clock convention.
        - [ ] Dedicated roots vs compositions for noon / midnight / dawn / dusk.
        - [ ] Time zone representation.
        - [x] Event-relative time ("when X happens") — unblocked. Use `tep ke [clause]` ("at WHEN she arrives"). See subordinate-clause framework 2026-05-15.
        - [ ] Weak placeholder roots `xor` (hour), `vet` (year) flagged for possible replacement.
- [x] **Verb shape** — confirmed: CVC root + V (tense vowel). Infinitive = bare CVC. Continuous-aspect `x` after tense vowel. Stale TODO in roots.md cleared. See decisions.md / history.md 2026-05-16.
- [x] **Negation** — resolved: prefix `no-`, phonologically bound to its host. See decisions.md and history.md 2026-05-15. Related sub-questions parked:
    - [x] Lexical opposite marker (`love` → `hate`) — resolved: rejected. Antonyms get separate roots; `no-` is the only "not" operator. See decisions.md / history.md 2026-05-16.
    - [ ] Canonical stacking order for multiple prefixes (negation + interrogative + intensity, etc.) when more prefixes get added.
    - [ ] Reserve the prefix phonological inventory (which CV shapes are prefixes vs root onsets) so future prefixes don't collide.
- [x] **Literal marker** — resolved: `lit … fin` paired quotation markers. See decisions.md 2026-05-16. Sub-question still open:
    - [x] **Variable / placeholder marker** — resolved: `var` prefix, single-word scope. Covers both template-slot and bound-variable cases. Pairs with `def` for bindings. See decisions.md / history.md 2026-05-16.
- [x] **"is" overload** — resolved: split into `sam` (identity), `est` (essential predication / ser), `sta` (state predication / estar), `mem` (membership), `tot+mem` (subset, composed), `kel` (existence, composed), `lit/fin` (paired quotation markers). Universal quantifier family also locked: `sol`/`tot`/`nul`/`kel`. See decisions.md and history.md 2026-05-16.
- [ ] **Synonym/equivalence grouping** — comma-like marker for "scalar-first, wxyz, Hamilton convention" being three names for one thing (TODO.md:9).
- [ ] **Rotation names** — names for X/Y/Z rotations (decisions.md:23-25).
- [ ] **Multi-level sentence punctuation** — beyond comma, for nested clauses (decisions.md:26).
- [x] **Subordinate clauses** — resolved: single universal complementizer `ke`, function determined by what precedes it. Conditional uses dedicated particle `is`. See decisions.md / history.md 2026-05-15. Sub-questions still open:
    - [x] Causation particle for "because/since" — resolved: `kaw` (also serves "why?" question). See decisions.md / history.md 2026-05-16.
    - [x] Embedded-question marker — resolved: `ka` inside a `ke`-clause does the work. See history.md 2026-05-15.
    - [x] Nested-clause disambiguation — resolved: strict adjacency for ~2 levels; named binding (`def`) for deeper or for clause-closure-back-to-main. No terminator words. See history.md 2026-05-15.
    - [x] Comma/pause prosodic conventions between main and subordinate clauses — resolved: clause boundary = ~200–300 ms pause + slight pitch reset; sentence = ~500+ ms + complete reset. See phonetics.md "Prosody", decisions.md / history.md 2026-05-16.
- [x] **Precision-by-default meta-principle** — locked: every sentence has exactly one meaning. Vague allowed, ambiguous forbidden. See AGENTS.md, decisions.md, history.md 2026-05-15.
- [x] **Reasoning-particle set** — locked: `dat` (premise), `erg` (therefore), `imp` (logical implication, distinct from `is` causal conditional). Multi-step reasoning uses staged sentences, not nested conditionals. See decisions.md / history.md 2026-05-15. Sub-questions still open:
    - [ ] Scope-of-premise: when does a `dat`-asserted premise expire?
    - [ ] Other proof-structuring particles ("suppose for contradiction", QED-marker, case-splitting).
    - [ ] Sibling implication operators (necessary vs sufficient, biconditional).
- [x] **Named binding for compositional clarity** — locked as concept (`def`-style construction for long expressions). Sub-questions still open:
    - [x] Specific `def`-construction syntax — resolved: `def var <name> <expression>`. Bare `def` is the binding op; explicit retraction `nul def var <name>`; shadowing on re-`def`. See decisions.md / history.md 2026-05-16.
    - [x] Scope of named bindings — resolved (default): discourse-local. Sentence-local and explicit-block scopes parked; revisit only if examples.md exposes a need.
- [x] **Coordinators kun (AND) / vel (OR)** and **depth rule** — locked. See decisions.md / history.md 2026-05-15.
- [x] **Question system** — locked: universal `ka`, position determines yes/no vs wh vs role-question vs embedded. Spatial preposition `lok` added. See decisions.md / history.md 2026-05-15. Sub-questions still open:
    - [x] Manner preposition for "how?" questions — resolved: `mod`. See decisions.md / history.md 2026-05-16.
    - [x] Causation preposition for "why?" questions — resolved: `kaw` (same root serves as "because/since" subordinator). See decisions.md / history.md 2026-05-16.
    - [ ] Person vs object disambiguation marker on `ka` for rare context-failure cases.
    - [x] Tag questions sanity check — resolved: compose from existing parts. Bare `ka?` tag is the default; echo form `ka no-[verb] [subj]?` is available when explicit polarity is wanted. No new particle. See decisions.md / history.md 2026-05-16.
    - [ ] Full spatial-preposition family (under, over, near, beside, etc.).

## Vocabulary buildout (after decisions above)
- [ ] Fill empty categories in roots.md: prepositions, conjunctions, adverbs, demonstratives, relatives, interrogatives, indefinites, nouns, modifiers, logical operators, probabilistic operators, directions, states, emotions.
- [ ] Build a reservation map of CVC space (which roots are taken vs free) to prevent collisions.
- [ ] Populate dictionary.md from roots.md (currently empty).

## Validation
- [x] Write `examples.md` with 20–50 worked translations covering questions, conditionals, negation, plurals, nested clauses. Resolved: 66 worked examples committed (see examples.md). Surfaced gaps documented in the "Observations" section of that file. Next pass after vocabulary buildout.

## Repo restructuring
- [ ] Split the root tables out of roots.md (prose stays; data moves to dictionary.md or a roots/ folder by category).
- [ ] Disambiguate TODO.md vs checklist.md vs decisions.md: TODO = open questions, checklist = features the language must support, decisions = settled. Items currently drift between them.
- [ ] Eventually: machine-readable form (YAML/JSON) for roots so collisions can be scripted and the dictionary auto-generated.
