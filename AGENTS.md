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
- **Record decisions immediately.** Once a design call is made, append it to `decisions.md` and `history.md` so the reasoning survives.
- **Park open questions in `tasks.md`.** Don't let unresolved questions clutter the active discussion.
- **Root sourcing rule.** When picking a root, prefer the language whose everyday word for the concept matches the target meaning. Don't pull a Latin root if real speakers use a Germanic word (and vice-versa).
- **Roots are concept-level.** A root represents the underlying concept, not a specific part of speech. Verb/noun/adjective forms come from markers on top. (See `history.md` 2026-05-15.)

## How to make progress
The biggest blocker right now is the **part-of-speech / derivation marker system** — without it, the empty categories in `roots.md` (prepositions, conjunctions, nouns, adjectives, etc.) can't be filled responsibly. See `tasks.md` for the full list of parked decisions.

When resolving an open question:
1. Read `history.md` for prior reasoning on adjacent decisions.
2. Lay out 2–4 concrete options with tradeoffs.
3. Pick one, append the decision + rationale to `decisions.md` and `history.md`.
4. Tick the corresponding box in `tasks.md`.
