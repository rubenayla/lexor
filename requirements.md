# Requirements

Lexor's goals and constraints: what the language must achieve. [decisions.md](decisions.md) records the chosen mechanisms; [trials.md](trials.md) exercises them; [tasks.md](tasks.md) tracks open work. These requirements collect existing project commitments, rather than introducing new language features.

The requirements are active design targets, not a claim that the unfinished language already satisfies them. Individual trials retain their own pass/open status. Sources below identify the existing project statements from which each requirement was collected.

## R1. Unambiguous meaning, with vagueness allowed

**Vague is allowed, ambiguous is forbidden.** Every well-formed Lexor sentence has exactly one meaning. That meaning may include underspecified parameters — *vagueness* (one claim, some details unspecified) is a positive feature and is grammatically cheap (no extra marking). What's forbidden is *ambiguity* (two distinct meanings competing for the same syntactic form). When two readings would otherwise exist, structural rules force one or the speaker must mark / restructure to express the other; the unmarked form has *one* canonical meaning, which is often "speaker is not committing to that parameter." Listeners do not interpret — they take the structurally-given meaning at face value. Misalignment is the speaker's responsibility, not the listener's charity.

Multiple forms may express the same meaning. The forbidden case is one well-formed form with competing meanings, not synonymous forms.

**Source:** Moved from the "Meta-principle: vague is allowed, ambiguous is forbidden" entry in decisions.md; rationale in history.md, 2026-05-15, "Scope, ambiguity, and the precision-by-default principle." The allowance for synonymous forms is also stated in decisions.md under "Scalar degree / amount-modifier system" and "Bound polarity-prefix family" (2026-06-07).

**Check / status:** Use the ambiguity traps and omission/nesting stress tests in trials.md. Open cases, including A11, prevent a language-wide claim of completion.

## R2. No forced commitment to unspecified information

**No mandatory grammatical marking.** Lexor never forces speakers to commit to information they haven't decided on. Spanish gender, English number, etc. are anti-features. Every grammatical category is optional and only attached when the speaker actually has and cares about that info.

Optional information must still obey R1: an omitted category must have a defined neutral meaning rather than competing readings. This requirement does not make every structural cue optional.

**Source:** Moved from decisions.md's no-mandatory-marking principle; also stated in AGENTS.md.

**Check / status:** Check neutral forms against their explicitly marked counterparts. Trial F3 addresses gender; A4 addresses distributive versus collective readings; J4 tests ambiguity by omission. The general requirement remains under evaluation.

## R3. Efficient communication

Aim to maximize precision and efficiency, with clear and compact expression. Evaluate competing mechanisms against the same intended meaning; a shorter form that changes the claim does not meet the same goal.

**Source:** README.md's project purpose and AGENTS.md's introduction. This is an optimization goal; this reorganization introduces no numerical efficiency threshold.

**Check / status:** Compare the length and use of candidate constructions on the same trials. For A11, the spoken syllable cost of grouping is known, but the pitch alternative has not been tested for delivery speed or comprehension. Overall efficiency has not been established.

## R4. Clear spoken communication

Aim for understandable speech in complex situations, including competing speakers and noise.

**Source:** The rationale for the existing non-tonal choice in decisions.md, and its vowel-final-word rationale. This records the desired outcome separately from either proposed means of achieving it.

**Check / status:** The nesting-pitch discussion in history.md, 2026-09-24, identifies an unresolved comparison with explicit grouping. The cited design rationales do not establish that a particular encoding is reliable; this requirement is not marked satisfied by choosing a mechanism.

## R5. Recognizable vocabulary

Prefer roots that real speakers can recognize from everyday words for the intended concept, rather than choosing for etymological neatness.

**Source:** The root-sourcing rationale in decisions.md and AGENTS.md. The sourcing policy remains in decisions.md.

**Check / status:** Review each root's intended concept and recorded source in lexicon.yaml against the sourcing policy. This is an ongoing selection criterion, not a measured claim about learner recognition.

## Requirements versus decisions

Word order, word shapes, derivation markers, phoneme-to-character mapping, non-tonality, and spoken grouping words remain in decisions.md. They specify how Lexor is currently designed. Their wording may be mandatory for the current grammar without making them permanent project goals.

The pitch alternative in trial A11 is still a proposal. This reorganization neither adopts it nor removes the existing rules. Its evaluation must address R1, R3, and R4; any adopted change must update the affected decisions and their rationale.
