<!-- consult-selectively — grep for the relevant failure; entries are chronological. -->
# Error log

## 2026-09-24 — English paraphrases substituted for Lexor grammar design (GPT-6 Astra)

**Error:** Asked to investigate the attachment ambiguity in "alquiler de camiones sin conductor," the assistant recommended explicit English paraphrases, then repeated them when Rubén said the proposal was unclear. That did not answer how Lexor should make the construction unambiguous.

**Cause:** The assistant treated meaning descriptions as a language-design solution and let a secondary distinction (driver absence versus autonomous capability) displace the primary problem (which constituent a modifier targets).

**Correction:** Reopened the analysis at the grammar level. Trial A11 now proposes testing the existing spoken grouping markers with a precise constituent/head attachment rule. Structural templates are labelled as proposals, and incomplete lexical material is identified rather than invented as settled Lexor.

**Prevention:** For a Lexor design question, state the parsing rule, demonstrate contrasting structures, and identify what the current grammar leaves unspecified. Use English glosses to explain those structures, not as the solution itself.

**Attribution:** The current session's latest `turn_context` reports model `gpt-6-astra`; inspected on 2026-09-24.
