# Tasks

Open design questions parked here so we can address them one at a time.

## Inbox — next session candidates (queued 2026-05-19)

Ready to pick up, ranked roughly by visible impact:

- [ ] **Vocab batch 3** — second-tier high-frequency concepts. Likely additions:
    - Colors: red, blue, green, yellow, black, white, gray.
    - Animals: dog, cat, bird, fish, horse, cow.
    - More body parts: ear (needs design — vowel-initial sources in all candidate languages), face, leg, arm, finger, hair, tooth, neck, back.
    - Hard parked ones from batch 2: `ear`, `time` (abstract concept; `tem` and `tep` taken).
    - Common verbs still missing: hear (locked `lis` already), feel (locked `sen`), believe, hope, dream, remember, forget, learn, teach, help, lose, leave-place.
    - Common adjectives still missing: dry (counterpart to `mol` wet), strong/weak, full/empty, easy/hard, true/false, right/correct, wrong, dead/alive (already `viv`/`mor` for verbs), young (counterpart to `mat` old; `nin` is child-noun not adjective).
    - Likely target: 30–50 roots.
- [ ] **Compound noun formation rules** (Lojban-style lujvo). Unblocks derivatives like "doctor" = treat-agent, "kitchen" = cook-place, "teacher" = teach-agent, etc., without needing dedicated roots for each. Would let the lexicon spend less effort on compound concepts and more on atomic ones. Design round.
- [ ] **H1 + H2 paired design round** — anti-adjective marker (for "more or less," "a lot or a little") plus neutral magnitude axis (for "weight" instead of "fatness/thinness," "temperature" instead of "hotness/coldness"). Closes trials H1 and H2 in one round.
- [ ] **Stale-content cleanup in examples.md** — pre-existing bare-verb-root bugs like `dik e` instead of `dike e`. One careful pass to fix all instances. Low risk, visible-correctness win.
- [ ] **Demonstrative system** (this / that / these / those). Parked since batch 1. Small new closed-class family (probably 2–4 markers under a `-i` subclass vowel, e.g., `ti` / `ta` / similar). Closes a gap that comes up constantly in real sentences.
- [ ] **Ordinal markers** — "first," "second," "last." Compose with digit + ordinal suffix? Or new roots? Worth one round.
- [ ] **Time-as-noun** — the abstract concept of "time" (not a specific unit like day/hour). `tem` and `tep` are taken; needs a creative root choice. Park as a vocab item but flag the design pressure.

## Design decisions to resolve
- [x] **Part-of-speech marking** — resolved: suffix, vowel-initial, universal word shape `CVC + V[C]`. Derivation consonants: `r` agent, `n` act, `t` patient, `s` adjective. See decisions.md and history.md 2026-05-15.
- [x] **Plural rule** — resolved: no plural inflection. Number is unspecified by default; quantity is a separate optional modifier system. See history.md 2026-05-15.
- [x] **Quantifier / quantity system framework** — resolved: digit-stream numbers, base markers `demu`/`dozu` for decimal/dozenal first-class compatibility, scale via `pemu` scientific notation, comparison operators `minu`/`magu`/`samo`/`tomu`/`piru` as CVC closed class. Quantifier follows noun. See decisions.md / history.md 2026-05-15. Sub-questions still open:
    - [x] **12 digit roots** — resolved: `zo pa du re ko fi sa chi bo ne` (0–9) plus `ja gi` (A, B for dozenal). See decisions.md / history.md 2026-05-15.
    - [x] **Prosodic disambiguation rule** for CV-vs-CVC overlap — resolved: obligatory brief acoustic break (~50–100 ms / light glottal) at every word boundary; digit streams concatenate as one prosodic unit. See phonetics.md "Prosody" section, decisions.md / history.md 2026-05-16.
    - [ ] **Distribution-shape roots** (gaussian, uniform, bimodal, etc.) for richer probabilistic quantifiers.
    - [ ] **Arbitrary-base spoken notation** (user's written `9_12.5` syntax — base-N representation of numbers).
    - [x] **Vague quantifiers** — partially resolved: `solu`/`totu`/`nulu`/`kelu` cover only/all/none/some. "Many"/"few" still open as fuzzy magnitude quantifiers.
    - [ ] "Many" / "few" / "most" — fuzzy magnitude quantifiers, distinct from the precise `totu`/`kelu`.
- [x] **Trailing vowel for non-verb forms** — resolved: all words end in vowels (`CVCV(CV)`). Inner vowel reuses tense system; outer vowel is the role/case slot. See decisions.md and history.md 2026-05-15. Sub-questions still open:
    - [x] Which specific vowel = "atemporal / temporal-frame unspecified"? Resolved: `a`. Other tense vowels reassigned around it (see history.md 2026-05-15).
    - [x] Specific role-vowel assignments for outer slot — resolved: `a` default, `e` subject, `o` object, `u` recipient, `i` instrument. See decisions.md / history.md 2026-05-15.
    - [x] Pronoun behavior with role vowels — resolved: suffix role vowel, doubled-vowel collisions pronounced as long vowels. See decisions.md / history.md 2026-05-15.
    - [x] Temporal-modifier system framework — resolved: numeric calendar, time-relation prepositions (`tepa`/`pena`/`sina`/`lima`/`anta`/`posa`), frequency operator `kexu`, reference frame defaults to now (root `nuna`), relative time by composition. See decisions.md / history.md 2026-05-15. Sub-questions still open:
        - [ ] 12-hour vs 24-hour clock convention.
        - [ ] Dedicated roots vs compositions for noon / midnight / dawn / dusk.
        - [ ] Time zone representation.
        - [x] Event-relative time ("when X happens") — unblocked. Use `tepa ke [clause]` ("at WHEN she arrives"). See subordinate-clause framework 2026-05-15.
        - [ ] Weak placeholder roots `xora` (hour), `veta` (year) flagged for possible replacement.
- [x] **Verb shape** — confirmed: CVC root + V (tense vowel). Infinitive = bare CVC. Continuous-aspect `x` after tense vowel. Stale TODO in roots.md cleared. See decisions.md / history.md 2026-05-16.
- [x] **Negation** — resolved: prefix `no-`, phonologically bound to its host. See decisions.md and history.md 2026-05-15. Related sub-questions parked:
    - [x] Lexical opposite marker (`love` → `hate`) — resolved: rejected. Antonyms get separate roots; `no-` is the only "not" operator. See decisions.md / history.md 2026-05-16.
    - [ ] Canonical stacking order for multiple prefixes (negation + interrogative + intensity, etc.) when more prefixes get added.
    - [ ] Reserve the prefix phonological inventory (which CV shapes are prefixes vs root onsets) so future prefixes don't collide.
- [x] **Literal marker** — resolved: `liti … fini` paired quotation markers. See decisions.md 2026-05-16. Sub-question still open:
    - [x] **Variable / placeholder marker** — resolved: `vari` prefix, single-word scope. Covers both template-slot and bound-variable cases. Pairs with `defi` for bindings. See decisions.md / history.md 2026-05-16.
- [x] **"is" overload** — resolved: split into `samo` (identity), `esto` (essential predication / ser), `stao` (state predication / estar), `memo` (membership), `totu+memo` (subset, composed), `kelu` (existence, composed), `liti/fini` (paired quotation markers). Universal quantifier family also locked: `solu`/`totu`/`nulu`/`kelu`. See decisions.md and history.md 2026-05-16.
- [ ] **Synonym/equivalence grouping** — comma-like marker for "scalar-first, wxyz, Hamilton convention" being three names for one thing (TODO.md:9).
- [x] **Rotation names** — resolved compositionally: `rot fasa` (roll), `rot lata` (pitch), `rot sura` (yaw). No new roots beyond the verb `rot`. See decisions.md / history.md 2026-05-16.
- [x] **Sub-constituent grouping** — resolved 2026-05-16: paired markers `bra … keti`. Handles numerical ranges, mixed AND/OR, nested operators. `defi`-binding freed for its original naming role. See decisions.md / history.md 2026-05-16.
- [ ] **Multi-level sentence punctuation** — beyond comma, for nested clauses (decisions.md:26). Partly addressed by `bra/keti` for sub-clause grouping; full multi-level punctuation system still open.
- [x] **Subordinate clauses** — resolved: single universal complementizer `ke`, function determined by what precedes it. Conditional uses dedicated particle `isi`. See decisions.md / history.md 2026-05-15. Sub-questions still open:
    - [x] Causation particle for "because/since" — resolved: `kawa` (also serves "why?" question). See decisions.md / history.md 2026-05-16.
    - [x] Embedded-question marker — resolved: `ka` inside a `ke`-clause does the work. See history.md 2026-05-15.
    - [x] Nested-clause disambiguation — resolved: strict adjacency for ~2 levels; named binding (`defi`) for deeper or for clause-closure-back-to-main. No terminator words. See history.md 2026-05-15.
    - [x] Comma/pause prosodic conventions between main and subordinate clauses — resolved: clause boundary = ~200–300 ms pause + slight pitch reset; sentence = ~500+ ms + complete reset. See phonetics.md "Prosody", decisions.md / history.md 2026-05-16.
- [x] **Precision-by-default meta-principle** — locked: every sentence has exactly one meaning. Vague allowed, ambiguous forbidden. See AGENTS.md, decisions.md, history.md 2026-05-15.
- [x] **Reasoning-particle set** — locked: `dati` (premise), `ergi` (therefore), `impi` (logical implication, distinct from `isi` causal conditional). Multi-step reasoning uses staged sentences, not nested conditionals. See decisions.md / history.md 2026-05-15. Sub-questions still open:
    - [ ] Scope-of-premise: when does a `dati`-asserted premise expire?
    - [ ] Other proof-structuring particles ("suppose for contradiction", QED-marker, case-splitting).
    - [ ] Sibling implication operators (necessary vs sufficient, biconditional).
- [x] **Epistemic modal operators** — resolved 2026-05-16: `kani` (possibility ◇), `musi` (necessity □). Closed class, sentence-initial. Compose with `no-`. Closed trials B1/B2/I2. See decisions.md / history.md 2026-05-16. Sub-questions parked:
    - [ ] Deontic modality (permission / obligation) — split from epistemic when a trial requires it.
    - [ ] Alethic vs epistemic split — refine if a logical/metaphysical trial exposes the need.
    - [x] Probability operator surface form (trial D6) — resolved 2026-05-16: `chani <number> <proposition>` sentence-initial, scalar version of `kani`/`musi`. See decisions.md / history.md 2026-05-16.
    - [ ] Counterfactual conditionals ("if she had eaten...") — distinct from `isi`/`impi`. Parked.
- [x] **Closed-class subclass-vowel suffix (C-2)** — resolved 2026-05-18. All closed-class items end in a subclass-marking vowel: prepositions `-a`, coordinators `-e`, markers `-i`, copulas `-o`, quantifiers `-u`, time-units `-a`. Every word in spoken Lexor now ends in a vowel; zero consonant clusters at word boundaries. ~50 lexicon entries renamed, ~10 active docs swept. See decisions.md / history.md 2026-05-18.
- [x] **Axis system: aksi / tipi / mezi** — resolved 2026-05-16. Closed trials.md G3 (sentido), G4 (direction vs location), G5 (neutral axis names). Three new closed-class composable markers; agent-frame axes reuse spatial prepositions, object-frame ranks reuse digits, polarity reuses `magu`/`minu`. See decisions.md / history.md 2026-05-16. Sub-questions parked:
    - [ ] Compass directions (N/S/E/W) — need dedicated roots or compositional Earth-frame system.
    - [ ] Gravity-as-axis vs Z-axis distinction — defer until a trial exposes the need (vehicles, spacecraft).
    - [ ] Signed magnitudes (physics displacement, negative values) — compose `magu`/`minu` on top of `mezi`; convention not yet locked.
- [x] **Angle convention** — resolved 2026-05-16: angles as fractions of a revolution, right-handed sign around the named axis, reference +X. No new roots; reuses `rot`/`rota` + `aksi` + digit-stream. Closed trial G6. See decisions.md / history.md 2026-05-16. Sub-questions parked:
    - [ ] Solid angles (3D angular measure).
    - [ ] Spherical-coordinate shorthand for arbitrary 3D directions.
    - [ ] Angular velocity / acceleration syntax (composable but not formalized).
- [x] **Named binding for compositional clarity** — locked as concept (`defi`-style construction for long expressions). Sub-questions still open:
    - [x] Specific `defi`-construction syntax — resolved: `defi vari <name> <expression>`. Bare `defi` is the binding op; explicit retraction `nulu defi vari <name>`; shadowing on re-`defi`. See decisions.md / history.md 2026-05-16.
    - [x] Scope of named bindings — resolved (default): discourse-local. Sentence-local and explicit-block scopes parked; revisit only if examples.md exposes a need.
- [x] **Coordinators kun (AND) / vel (OR)** and **depth rule** — locked. See decisions.md / history.md 2026-05-15.
- [x] **Question system** — locked: universal `ka`, position determines yes/no vs wh vs role-question vs embedded. Spatial preposition `loka` added. See decisions.md / history.md 2026-05-15. Sub-questions still open:
    - [x] Manner preposition for "how?" questions — resolved: `moda`. See decisions.md / history.md 2026-05-16.
    - [x] Causation preposition for "why?" questions — resolved: `kawa` (same root serves as "because/since" subordinator). See decisions.md / history.md 2026-05-16.
    - [ ] Person vs object disambiguation marker on `ka` for rare context-failure cases.
    - [x] Tag questions sanity check — resolved: compose from existing parts. Bare `ka?` tag is the default; echo form `ka no-[verb] [subj]?` is available when explicit polarity is wanted. No new particle. See decisions.md / history.md 2026-05-16.
    - [x] Full spatial-preposition family — resolved: 12-root closed class (`loka` `suba` `sura` `poka` `lata` `dora` `fasa` `inta` `kira` `dira` `oksa` `tra`). See decisions.md / history.md 2026-05-16.

## Vocabulary buildout (after decisions above)
- [ ] Fill empty categories in roots.md: prepositions, conjunctions, adverbs, demonstratives, relatives, interrogatives, indefinites, nouns, modifiers, logical operators, probabilistic operators, directions, states, emotions.
- [x] Build a reservation map of CVC space (which roots are taken vs free) to prevent collisions. Resolved: `lexicon.yaml` is the source of truth, `scripts/check_collisions.py` is the conflict-checker. 130 entries seeded from existing locked roots.
- [x] **Audit verb roots for phoneme conformance.** Resolved 2026-05-16: all 7 renamed to CVC. `cad→kad`, `cur→kur`, `cri→lor`, `cla→xut`, `duc→tir`, `apr→per`, `aud→lis`. See decisions.md / history.md for per-root rationale. Spawned: future root for "shout/proclaim" (parked).
- [ ] **Build a parallel frequency list** (`frequencies.yaml`) merging top-N words from English (SUBTLEX-US), Spanish (SUBTLEX-ESP), Latin (Diederich). Drives frequency-first root assignment. Dedup by concept across languages.
- [ ] Populate dictionary.md from lexicon.yaml (auto-generation script).

## Validation
- [x] Write `examples.md` with 20–50 worked translations covering questions, conditionals, negation, plurals, nested clauses. Resolved: 66 worked examples committed (see examples.md). Surfaced gaps documented in the "Observations" section of that file. Next pass after vocabulary buildout.

## Repo restructuring
- [ ] Split the root tables out of roots.md (prose stays; data moves to `lexicon.yaml`, which now exists). Tables in roots.md become read-only views or get deleted entirely.
- [x] Disambiguate TODO.md vs checklist.md vs decisions.md — partly resolved 2026-05-16: `checklist.md` removed; its content restructured into `trials.md` (a test-suite of trap/feature/stretch/stress entries with passes/open/parked status). `decisions.md` remains the settled-decisions log. TODO.md vs tasks.md merge still pending.
- [x] Machine-readable form for roots — resolved: `lexicon.yaml` at repo root. Schema documented in-file. Collision-checker at `scripts/check_collisions.py`. See AGENTS.md.
