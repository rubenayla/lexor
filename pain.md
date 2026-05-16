# Pain — why current languages are shit

Short, concrete examples of things natural languages get wrong. The "why" behind Lexor.

## Ambiguity you can't fix without rephrasing

- **"This password shall only use the letters K and L at the start."**
  > "Wait, so I can't use K or L anywhere else?"
  - Yes, you can. But your password must start with either K or L.

- **"Determinar el empuje específico, el impulso específico y el rendimiento isentrópico del difusor."**
  > "I spent an hour computing the specific thrust of the diffuser. Turns out only the efficiency was about the diffuser."
  - Only "del difusor" attaches to the last item. Thrust and impulse are not about the diffuser.
  - MISSING COMMA?

- **"The 12 cities marked in red have the same population as NYC."**
  > "So each of those cities is the size of New York?? That can't be right."
  - The 12 *combined* have NYC's population. Each one is much smaller.

- **"I have 10 dollars."**
  > "I also have 10 dollars! Look, I even have 100 dollars."
  - The speaker meant *exactly* 10. The reply takes "have 10" as "have at least 10.". If you have 100, you also have 10.

- **"Returns a list of rotations between 001, the z axis in object frame, and the origin system."**
  Three entities? Or two, with "the z axis in object frame" being an apposition for 001? A comma can't carry that weight.

- **"Write a password with no spaces and |."**
  > "Why is `|` not allowed? It's a normal character."
  - `|` *is* allowed. It's the separator between the two rules: "no spaces" and the next field.

- **"I bet I can do between three and four hundred pushups."**
  > "Three to four hundred? Bro you can't even do 50."
  - He meant 3 to 400, not 300 to 400.

- **"Mean sea level."**
  Mean over what dimension? Most people assume spatial mean over the globe; it's actually a temporal mean at each point.

- **"Its tube ends were round."**
  > "Its tube ends [what]?"
  - Parse A (intended): `[its [tube ends]]` were round — `tube` is a noun-adjunct modifying `ends`; the *ends* are round.
  - Parse B (live in other contexts): `[its tube] ends [...]` — `ends` is a verb meaning *terminates*. Compare "its tube ends here." Only the verb agreement on `were` kills B here; with a different head verb, the ambiguity is decided by chance.
  - English lets nouns sit next to nouns and silently flip one into a modifier. Listener disambiguates by inferring which word is the verb.

## Negation scope

- **"not (a = b)"** collapses in English to "a is not equal to b" — but often the intended meaning is *"a doesn't have to equal b."* English can't distinguish:
  - `a ≠ b` (never equal)
  - `¬(always a = b)` (not necessarily equal)
  - `possibly a = b` (no reason to rule it out)

- **"The masses can be different"** vs **"the masses are different."** Physics problems with m1, m2: people read "different" and assume m1 ≠ m2, missing the valid case m1 = m2.

## Mandatory commitments you haven't made

- **Spanish gender** — you can't refer to a friend without picking *amigo* or *amiga*. If you don't know or don't care, tough.
- **English number** — "I saw a dog / dogs." You must commit to singular or plural even when the count is irrelevant or unknown.
- **Tense when uncertain** — something is happening, happened, or will happen, and you're not sure which. Every major language forces a tense anyway.

## Missing distinctions

- **"The electron is at position x."**
  > "No, it *can be* measured at x. It isn't *at* anywhere until you look."
  - English merges Spanish *ser* (essence) and *estar* (state/location) into one verb, so "is at" smuggles in a claim about location that the speaker didn't intend.

- **"The password is incorrect."**
  > "What's the password? Incorrect?"
  - The password *has the property* of being wrong, not the literal value "incorrect." Predication vs identity-with-string collapse.

- **"My name is very stupid."**
  > "Did your parents really name you that, or do you just dislike your name?"
  - Could be predication (name has property "very stupid") or literal content (name = the string "very stupid"). One copula, two meanings.

- **"A whale is a mammal."**
  > "So whales and mammals are the same thing?"
  - It's set membership (`whale ∈ mammals`), not identity. English "is" hides which relation is meant. Most people don't notice until you ask "is mammal-ness the same as whale-ness?"

- **"Mammals are animals."**
  > "I have 4 mammals. Therefore I have 4 animals. But also: I have 1 animal group, mammals, in my house."
  - Subset relation (`mammals ⊆ animals`) vs membership of the *group* in some classification. English collapses these.

- **"There is a god."**
  > "Where? Show me which god."
  - Existence claim, not identity. English "is" overloads the existential with predication.

- **"She is a doctor" vs "She is tired."**
  - Permanent property vs current state. Spanish marks this (ser/estar); English doesn't. Medical/hiring/character-judgment ambiguities follow: "the patient is depressed" — clinical or just today? "He is reliable" — permanent trait or recent behavior?

- **"Taper ratio: λ = c_tip / c_root."**
  > "A higher taper ratio means more taper, right?"
  - No — higher λ means *less* taper (a rectangular wing has λ = 1). The name implies the opposite of what it measures.

- **"Are we going to the party?"**
  > "Wait, am I included in that 'we', or are you just asking if you and your roommate are going?"
  - English "we" collapses three meanings: just-you-and-me / you-me-and-others / me-and-others-not-you.

- **Top ≠ Up, Bottom ≠ Down** — direction vs location, often the same word.

- **Length / width / height / depth / thickness** — all orientation-dependent. No clean way to say "longest dimension, second-longest, shortest" without picking an orientation.

- **Fat vs thin, hot vs cold** — no neutral noun for the axis. "Weight" and "temperature" exist; "fatness" and "hotness" carry a direction. Can't say "uncool the yogurt to room temp" without sounding wrong.

- **Source of information** — Cherokee marks whether you saw it yourself or were told. English makes you tack on "I heard that…" or "apparently…" optionally and inconsistently.

- **Direction sense along an axis** — English has no single word for Spanish *sentido* (front vs back along the same axis). "Direction" overloads both.

## Clunky workarounds for things that should be cheap

- **Probability words** — "somewhat likely", "very likely", "more or less likely". Why not just "90% likely it'll rain"? Sounds robotic in English; shouldn't.

- **Ranges and distributions** — "from 2 to 9, usually around 7, with a long tail." Easy concept, painful to say. Should be as cheap as `7 +2-5`.

- **Approximation marker** — "I get 4h of sunlight in 1h" sounds like a lie when it's just eyeballed. No compact way to flag "rough estimate" like `s` flags plural.

- **Eyeballed % / ratio** — `%` always implies ×100. No clean symbol for a bare ratio.

- **Pronoun-less statements** — "Se ha decidido hacer esto" / "It has been decided." Most languages make this awkward; should be default-easy when the agent is irrelevant.

- **Placeholders** — when you write `<path>` twice, is it the same value or two independent ones? No convention. Same for variable `X` repeated in a sentence.

- **Literal vs interpreted** — *"my name is very stupid"* vs *my name is "very stupid"*. Quotes work in writing, nothing works in speech.

- **Anti-adjective / inclusive marker** — "a lot or a little", "more or less aligned", "like it or not". Needs to be one short word.

## Writing / encoding costs

- **Accents** — double the character set on computers; break pen flow when handwriting.
- **He/she** — forced gender on every third-person reference. Default should be neutral; specify only when relevant.
- **"You" singular vs plural** — English lost the distinction. *Tú* ≠ *vosotros*.
