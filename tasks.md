# Tasks

Open design questions parked here so we can address them one at a time.

## Inbox
- you agree VOS was the right choice?

## Design decisions to resolve
- [x] **Part-of-speech marking** — resolved: suffix, vowel-initial, universal word shape `CVC + V[C]`. Derivation consonants: `r` agent, `n` act, `t` patient, `s` adjective. See decisions.md and history.md 2026-05-15.
- [x] **Plural rule** — resolved: no plural inflection. Number is unspecified by default; quantity is a separate optional modifier system. See history.md 2026-05-15.
- [x] **Quantifier / quantity system framework** — resolved: digit-stream numbers, base markers `dem`/`doz` for decimal/dozenal first-class compatibility, scale via `pem` scientific notation, comparison operators `min`/`mag`/`sam`/`tom`/`pir` as CVC closed class. Quantifier follows noun. See decisions.md / history.md 2026-05-15. Sub-questions still open:
    - [x] **12 digit roots** — resolved: `zo pa du re ko fi sa chi bo ne` (0–9) plus `ja gi` (A, B for dozenal). See decisions.md / history.md 2026-05-15.
    - [ ] **Prosodic disambiguation rule** for CV-vs-CVC overlap (e.g., digit `sa` 6 vs operator `sam` equal, digit `ko` 4 vs verb `kom` move). Likely a stress-and-timing convention.
    - [ ] **Distribution-shape roots** (gaussian, uniform, bimodal, etc.) for richer probabilistic quantifiers.
    - [ ] **Arbitrary-base spoken notation** (user's written `9_12.5` syntax — base-N representation of numbers).
    - [ ] **Vague quantifiers** ("some", "all", "none", "many", "few"): part of this system or a separate operator class?
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
- [ ] **Verb shape** — confirm CVC-root + vowel-for-tense (roots.md:40 currently marked TODO).
- [x] **Negation** — resolved: prefix `no-`, phonologically bound to its host. See decisions.md and history.md 2026-05-15. Related sub-questions parked:
    - [ ] Lexical opposite marker (`love` → `hate`) — distinct from logical negation. Decide whether Lexor wants one and how it differs from `no-`.
    - [ ] Canonical stacking order for multiple prefixes (negation + interrogative + intensity, etc.) when more prefixes get added.
    - [ ] Reserve the prefix phonological inventory (which CV shapes are prefixes vs root onsets) so future prefixes don't collide.
- [ ] **Literal vs variable marker** — "my name is very stupid" vs my name is `"very stupid"` (TODO.md:7).
- [ ] **"is" overload** — distinguish "the password is [the string] incorrect" vs "the password has property incorrect" (TODO.md:13).
- [ ] **Synonym/equivalence grouping** — comma-like marker for "scalar-first, wxyz, Hamilton convention" being three names for one thing (TODO.md:9).
- [ ] **Rotation names** — names for X/Y/Z rotations (decisions.md:23-25).
- [ ] **Multi-level sentence punctuation** — beyond comma, for nested clauses (decisions.md:26).
- [x] **Subordinate clauses** — resolved: single universal complementizer `ke`, function determined by what precedes it. Conditional uses dedicated particle `is`. See decisions.md / history.md 2026-05-15. Sub-questions still open:
    - [ ] Causation particle for "because/since".
    - [ ] Embedded-question marker — needs broader question system first.
    - [ ] Nested-clause disambiguation — does `ke` stack cleanly or need parentheses?
    - [ ] Comma/pause prosodic conventions between main and subordinate clauses.

## Vocabulary buildout (after decisions above)
- [ ] Fill empty categories in roots.md: prepositions, conjunctions, adverbs, demonstratives, relatives, interrogatives, indefinites, nouns, modifiers, logical operators, probabilistic operators, directions, states, emotions.
- [ ] Build a reservation map of CVC space (which roots are taken vs free) to prevent collisions.
- [ ] Populate dictionary.md from roots.md (currently empty).

## Validation
- [ ] Write `examples.md` with 20–50 worked translations covering questions, conditionals, negation, plurals, nested clauses. Use it to expose gaps before committing more roots.

## Repo restructuring
- [ ] Split the root tables out of roots.md (prose stays; data moves to dictionary.md or a roots/ folder by category).
- [ ] Disambiguate TODO.md vs checklist.md vs decisions.md: TODO = open questions, checklist = features the language must support, decisions = settled. Items currently drift between them.
- [ ] Eventually: machine-readable form (YAML/JSON) for roots so collisions can be scripted and the dictionary auto-generated.
