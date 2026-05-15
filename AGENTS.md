<!-- read in full — kept under 150 lines -->

# Lexor — Agent Guide

Lexor is a constructed language designed from first principles to maximize precision and efficiency. Under active development.

## Repo layout
- `README.md` — public-facing intro.
- `decisions.md` — settled design decisions. Append here once something is locked in.
- `checklist.md` — features the language must support (capability list, not tasks).
- `pain.md` — concrete examples of what current languages get wrong. The "why" behind Lexor.
- `TODO.md` — older open-questions list. Being merged into `tasks.md` over time.
- `tasks.md` — current open design questions and work items, parked for later.
- `history.md` — append-only log of decisions, reflections, findings. Grep, don't read in full.
- `roots.md` — root inventory: rationale + tables. Will eventually be split (data → `dictionary.md`).
- `dictionary.md` — word list (currently near-empty; to be populated).
- `phonetics.md` — phoneme inventory and rules.
- `grammar.md` — grammar notes.
- `stuff.md` — misc.

## Working conventions
- **Plan before building.** For non-trivial design decisions, debate one question at a time. Don't try to settle everything in one pass.
- **Every decision logs its rationale to `history.md`.** Not just *what* was decided — *why*, what alternatives were considered, what tradeoffs were accepted. `decisions.md` records the call; `history.md` records the reasoning. Future sessions and future-you need the rationale to evaluate edge cases and to know whether a past decision is still load-bearing when circumstances change. This is non-negotiable — if a round of work produced a decision, the rationale must be in `history.md` before the work is "done."
- **Park open questions in `tasks.md`.** Don't let unresolved sub-questions clutter the active discussion. Tick boxes when resolved; add sub-questions when a decision spawns new ones.
- **Update this file when you notice a missing rule.** If you find yourself repeatedly doing something that isn't documented here — re-explaining a convention, re-deriving a principle from prior decisions, or correcting yourself for forgetting a habit — that's a signal the rule belongs in `AGENTS.md`. Add it. The user shouldn't have to remind you twice.
- **Root sourcing rule.** When picking a root, prefer the language whose everyday word for the concept matches the target meaning. Don't pull a Latin root if real speakers use a Germanic word (and vice-versa).
- **Roots are concept-level.** A root represents the underlying concept, not a specific part of speech. Verb/noun/adjective forms come from markers on top.
- **Meta-principle: no mandatory grammatical marking.** Lexor never forces a speaker to commit to information they haven't decided on. Every grammatical category (number, gender, tense, definiteness, role) is opt-in. When designing any new feature, default to *optional with a neutral-default option* unless there's a strong reason otherwise.
- **Meta-principle: vague is allowed, ambiguous is forbidden.** Every well-formed sentence has exactly one meaning. Vagueness (one meaning with unspecified parameters) is welcome and cheap; ambiguity (two distinct meanings competing for the same syntactic form) is structurally eliminated. Listeners don't interpret; they take the grammar at face value. If two readings would exist, the unmarked form has *one* canonical meaning (often "speaker not committing on that axis") and the other reading requires explicit marking or restructuring. When designing any feature, the test is: "can two distinct meanings fit into the same surface form?" If yes, the design is wrong — either pin one by structure or require a marker for one.

## How to make progress
When resolving an open question:
1. Read `history.md` for prior reasoning on adjacent decisions.
2. Lay out 2–4 concrete options with tradeoffs.
3. Pick one. Append the decision to `decisions.md` and the full rationale (alternatives considered, tradeoffs accepted, links to related decisions) to `history.md`.
4. Tick the corresponding box in `tasks.md`. Add any new sub-questions the decision spawned.
5. Commit. Then either pause or pick another `tasks.md` item.

The biggest current gaps are in vocabulary buildout (most root categories in `roots.md` are still empty headers) and in the precise temporal-modifier system (parallel to the quantifier system, also parked). See `tasks.md` for the full list.
