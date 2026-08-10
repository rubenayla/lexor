<!-- reference — read only when you need the history of a shipped item -->
# Done archive — completed work items

Closed items moved out of the root `tasks.md` on 2026-08-10, following the same
convention as the partle and kart-medulla repos. Nothing here is actionable: the root
board carries only live work, while the reasoning behind resolved design questions
stays findable.

The board is `tasks.md` at the repo root — the only task board in this repo.

A top-level bullet only moves here once it AND every sub-question nested under it are
closed. A resolved top-level item that still has an open sub-question (e.g. a design
round that closed the framework but left a follow-up parked) stays on the board whole,
closed children included, so the open child keeps the context for what was already
settled.

## Closed design decisions

- [x] **Part-of-speech marking** — resolved: suffix, vowel-initial, universal word shape `CVC + V[C]`. Derivation consonants: `r` agent, `n` act, `t` patient, `s` adjective. See decisions.md and history.md 2026-05-15.

- [x] **Plural rule** — resolved: no plural inflection. Number is unspecified by default; quantity is a separate optional modifier system. See history.md 2026-05-15.

- [x] **Verb shape** — confirmed: CVC root + V (tense vowel). Infinitive = bare CVC. Continuous-aspect `x` after tense vowel. Stale TODO in roots.md cleared. See decisions.md / history.md 2026-05-16.

- [x] **Literal marker** — resolved: `liti … fini` paired quotation markers. See decisions.md 2026-05-16. Sub-question still open:
    - [x] **Variable / placeholder marker** — resolved: `vari` prefix, single-word scope. Covers both template-slot and bound-variable cases. Pairs with `defi` for bindings. See decisions.md / history.md 2026-05-16.

- [x] **"is" overload** — resolved: split into `samo` (identity), `esto` (essential predication / ser), `stao` (state predication / estar), `memo` (membership), `totu+memo` (subset, composed), `kelu` (existence, composed), `liti/fini` (paired quotation markers). Universal quantifier family also locked: `solu`/`totu`/`nulu`/`kelu`. See decisions.md and history.md 2026-05-16.

- [x] **Rotation names** — resolved compositionally: `rot fasa` (roll), `rot lata` (pitch), `rot sura` (yaw). No new roots beyond the verb `rot`. See decisions.md / history.md 2026-05-16.

- [x] **Sub-constituent grouping** — resolved 2026-05-16: paired markers `bra … keti`. Handles numerical ranges, mixed AND/OR, nested operators. `defi`-binding freed for its original naming role. See decisions.md / history.md 2026-05-16.

- [x] **Subordinate clauses** — resolved: single universal complementizer `ke`, function determined by what precedes it. Conditional uses dedicated particle `isi`. See decisions.md / history.md 2026-05-15. Sub-questions still open:
    - [x] Causation particle for "because/since" — resolved: `kawa` (also serves "why?" question). See decisions.md / history.md 2026-05-16.
    - [x] Embedded-question marker — resolved: `ka` inside a `ke`-clause does the work. See history.md 2026-05-15.
    - [x] Nested-clause disambiguation — resolved: strict adjacency for ~2 levels; named binding (`defi`) for deeper or for clause-closure-back-to-main. No terminator words. See history.md 2026-05-15.
    - [x] Comma/pause prosodic conventions between main and subordinate clauses — resolved: clause boundary = ~200–300 ms pause + slight pitch reset; sentence = ~500+ ms + complete reset. See phonetics.md "Prosody", decisions.md / history.md 2026-05-16.

- [x] **Precision-by-default meta-principle** — locked: every sentence has exactly one meaning. Vague allowed, ambiguous forbidden. See AGENTS.md, decisions.md, history.md 2026-05-15.

- [x] **Closed-class subclass-vowel suffix (C-2)** — resolved 2026-05-18. All closed-class items end in a subclass-marking vowel: prepositions `-a`, coordinators `-e`, markers `-i`, copulas `-o`, quantifiers `-u`, time-units `-a`. Every word in spoken Lexor now ends in a vowel; zero consonant clusters at word boundaries. ~50 lexicon entries renamed, ~10 active docs swept. See decisions.md / history.md 2026-05-18.

- [x] **Named binding for compositional clarity** — locked as concept (`defi`-style construction for long expressions). Sub-questions still open:
    - [x] Specific `defi`-construction syntax — resolved: `defi vari <name> <expression>`. Bare `defi` is the binding op; explicit retraction `nulu defi vari <name>`; shadowing on re-`defi`. See decisions.md / history.md 2026-05-16.
    - [x] Scope of named bindings — resolved (default): discourse-local. Sentence-local and explicit-block scopes parked; revisit only if examples.md exposes a need.

- [x] **Coordinators kun (AND) / vel (OR)** and **depth rule** — locked. See decisions.md / history.md 2026-05-15.

- [x] Build a reservation map of CVC space (which roots are taken vs free) to prevent collisions. Resolved: `lexicon.yaml` is the source of truth, `scripts/check_collisions.py` is the conflict-checker. 130 entries seeded from existing locked roots.

- [x] **Audit verb roots for phoneme conformance.** Resolved 2026-05-16: all 7 renamed to CVC. `cad→kad`, `cur→kur`, `cri→lor`, `cla→xut`, `duc→tir`, `apr→per`, `aud→lis`. See decisions.md / history.md for per-root rationale. Spawned: future root for "shout/proclaim" (parked).

- [x] Write `examples.md` with 20–50 worked translations covering questions, conditionals, negation, plurals, nested clauses. Resolved: 66 worked examples committed (see examples.md). Surfaced gaps documented in the "Observations" section of that file. Next pass after vocabulary buildout.

- [x] Disambiguate TODO.md vs checklist.md vs decisions.md — partly resolved 2026-05-16: `checklist.md` removed; its content restructured into `trials.md` (a test-suite of trap/feature/stretch/stress entries with passes/open/parked status). `decisions.md` remains the settled-decisions log. TODO.md vs tasks.md merge still pending.

- [x] Machine-readable form for roots — resolved: `lexicon.yaml` at repo root. Schema documented in-file. Collision-checker at `scripts/check_collisions.py`. See AGENTS.md.
