<!-- read in full — kept under 150 lines -->

# Lexor — Agent Guide

Lexor is a constructed language designed from first principles to maximize precision and efficiency. Under active development.

## Repo layout
- `README.md` — public-facing intro.
- `decisions.md` — settled design decisions. Append here once something is locked in.
- `trials.md` — language design test suite. Each entry is a `[trap]` (known ambiguity from natural languages) or `[feature]`/`[stretch]`/`[stress]` (capability target). Tagged with `passes`/`open`/`parked` status. Grep `[.*, open]` to find every unmet design goal. Replaces the older `checklist.md`. Append a trial when a new capability target or trap surfaces; close one by changing its status when a decision lands.
- `walkthrough.md` — pedagogical progression. ~18 levels of increasing complexity from bare verb to full paragraph, each level introduces one grammar feature. Audience: learners and evaluators. Different from `examples.md` (dense feature-organized reference) and `trials.md` (capability test suite).
- `comparisons.md` — honest comparisons with prior constructed languages that share design goals. Currently covers Lojban; can grow to cover Esperanto, Toki Pona, Ithkuil, etc. Used to answer "has this been done better?" and to track what Lexor can learn from mature projects.
- `pain.md` — concrete examples of what current languages get wrong. The "why" behind Lexor.
- `TODO.md` — older open-questions list. Being merged into `tasks.md` over time.
- `tasks.md` — current open design questions and work items, parked for later.
- `history.md` — append-only log of decisions, reflections, findings. Grep, don't read in full.
- `lexicon.yaml` — **source of truth for all locked roots.** Machine-readable. Every new root is added here first. Schema documented in the file header. Tree structure emerges from `semantic_parent` links — internal taxonomy nodes only get created when needed.
- `roots.md` — root inventory rationale + tables. Tables are legacy / human-readable views; `lexicon.yaml` is authoritative if they disagree.
- `dictionary.md` — word list (currently near-empty; will be auto-generated from `lexicon.yaml`).
- `frequencies.yaml` — merged frequency rankings from English / Spanish / Latin, used to prioritize root assignment. (Planned; not yet built.)
- `phonetics.md` — phoneme inventory and rules.
- `grammar.md` — grammar notes.
- `stuff.md` — misc.
- `scripts/check_collisions.py` — runs over `lexicon.yaml`; flags duplicate root forms and (for open-class verbs/nouns/adj) shape violations against the locked CVC rule. Run before committing any new root.

## Working conventions
- **Plan before building.** For non-trivial design decisions, debate one question at a time. Don't try to settle everything in one pass.
- **Every decision logs its rationale to `history.md`.** Not just *what* was decided — *why*, what alternatives were considered, what tradeoffs were accepted. `decisions.md` records the call; `history.md` records the reasoning. Future sessions and future-you need the rationale to evaluate edge cases and to know whether a past decision is still load-bearing when circumstances change. This is non-negotiable — if a round of work produced a decision, the rationale must be in `history.md` before the work is "done."
- **Park open questions in `tasks.md`.** Don't let unresolved sub-questions clutter the active discussion. Tick boxes when resolved; add sub-questions when a decision spawns new ones.
- **Update this file when you notice a missing rule.** If you find yourself repeatedly doing something that isn't documented here — re-explaining a convention, re-deriving a principle from prior decisions, or correcting yourself for forgetting a habit — that's a signal the rule belongs in `AGENTS.md`. Add it. The user shouldn't have to remind you twice.
- **Root sourcing rule.** When picking a root, prefer the language whose everyday word for the concept matches the target meaning. Don't pull a Latin root if real speakers use a Germanic word (and vice-versa).
- **Roots are concept-level.** A root represents the underlying concept, not a specific part of speech. Verb/noun/adjective forms come from markers on top.
- **Meta-principle: no mandatory grammatical marking.** Lexor never forces a speaker to commit to information they haven't decided on. Every grammatical category (number, gender, tense, definiteness, role) is opt-in. When designing any new feature, default to *optional with a neutral-default option* unless there's a strong reason otherwise.
- **Meta-principle: vague is allowed, ambiguous is forbidden.** Every well-formed sentence has exactly one meaning. Vagueness (one meaning with unspecified parameters) is welcome and cheap; ambiguity (two distinct meanings competing for the same syntactic form) is structurally eliminated. Listeners don't interpret; they take the grammar at face value. If two readings would exist, the unmarked form has *one* canonical meaning (often "speaker not committing on that axis") and the other reading requires explicit marking or restructuring. When designing any feature, the test is: "can two distinct meanings fit into the same surface form?" If yes, the design is wrong — either pin one by structure or require a marker for one.
- **Writing style for learner-facing material.** When writing any document a learner or evaluator reads (the walkthrough, README, future tutorials, onboarding pages), follow these rules:
    - Define every abbreviation the first time you use it. CVC, VOS, modal-logic symbols, and so on must be introduced before they appear in glosses.
    - Prefer plain words over math or logic symbols in prose. "Possibly" beats ◇; "all" beats ∀. The symbol can appear alongside the word for readers who know it, but the word carries the meaning.
    - Avoid stacking multiple adjectives in front of a noun. If you're writing two or more modifiers before a noun and the result requires the reader to parse which modifies which, refactor into a sentence.
    - Be precise about what a feature commits to *and* what it deliberately leaves open. "Doesn't say what gender" is different from "is undefined."

## How to make progress
When resolving an open question:
1. Read `history.md` for prior reasoning on adjacent decisions.
2. Lay out 2–4 concrete options with tradeoffs.
3. Pick one. Append the decision to `decisions.md` and the full rationale (alternatives considered, tradeoffs accepted, links to related decisions) to `history.md`.
4. Tick the corresponding box in `tasks.md`. Add any new sub-questions the decision spawned.
5. Commit. Then either pause or pick another `tasks.md` item.

The biggest current gaps are in vocabulary buildout (most root categories in `roots.md` are still empty headers) and in the precise temporal-modifier system (parallel to the quantifier system, also parked). See `tasks.md` for the full list.
