# Tasks

Open design questions parked here so we can address them one at a time.

## Design decisions to resolve
- [x] **Part-of-speech marking** — resolved: suffix, vowel-initial, universal word shape `CVC + V[C]`. Derivation consonants: `r` agent, `n` act, `t` patient, `s` adjective. See decisions.md and history.md 2026-05-15.
- [x] **Plural rule** — resolved: no plural inflection. Number is unspecified by default; quantity is a separate optional modifier system. See history.md 2026-05-15.
- [ ] **Quantifier / quantity system design** — separate module covering exact counts, ranges (2–8), and distributions (gaussian μ=15 σ=5), per the no-mandatory-marking principle. Connects to checklist.md:97, :120.
- [x] **Trailing vowel for non-verb forms** — resolved: all words end in vowels (`CVCV(CV)`). Inner vowel reuses tense system; outer vowel is the role/case slot. See decisions.md and history.md 2026-05-15. Sub-questions still open:
    - [ ] Which specific vowel = "atemporal / temporal-frame unspecified" for the inner slot? (`y` is candidate but currently means "perfect/completed".)
    - [ ] Specific role-vowel assignments for outer slot (subject, object, indirect, "role unspecified" default).
    - [ ] Temporal-modifier system for precise time ("yesterday", "since 2020", "every Tuesday"). Parallels the quantifier system — both layer optional precision on top of coarse word-internal marking.
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
