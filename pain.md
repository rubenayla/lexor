# Pain — why current languages are shit

Short, concrete examples of things natural languages get wrong. The "why" behind Lexor.

## Ambiguity you can't fix without rephrasing

- **"only uses" vs "uses only"** — "This password only uses the letters K and L at the start."
  - > "Wait, so I can't use K or L anywhere else in the password?"
  - Reading A: K and L appear *only* at the start (nowhere else in the password).
  - Reading B: the start is *only* K or L (no other letters there; K/L may appear elsewhere too).
  - English forces you to rewrite the sentence to disambiguate.

- **"A and B or C"** — is it `(A and B) or C`, or `A and (B or C)`?
  - > "I spent an hour computing the specific thrust of the diffuser. Turns out only the efficiency was about the diffuser."
  - In Spanish class: *"Determinar el empuje específico, el impulso específico y el rendimiento isentrópico del difusor"* — does "del difusor" modify all three, or only the last? Had to ask classmates.

- **"The 12 cities marked in red have the same population as NYC."**
  - > "So each of those cities is the size of New York?? That can't be right."
  - Each city ≈ NYC? Or the sum of the 12 ≈ NYC?

- **"I have 10 dollars."**
  - > "It's impossible to have $100 without also having $10."
  - Exactly $10? Or at least $10?

- **"Returns a list of rotations between 001, the z axis in object frame, and the origin system."**
  - Three entities? Or two, with "the z axis in object frame" being an apposition for 001? A comma can't carry that weight.

- **"Write a password with no spaces and |"**
  - > "Why is `|` not allowed? It's a normal character." (the rule was: no spaces, *and* `|` is the separator — totally different meaning.)
  - No spaces *and* no `|`? Or "no spaces, and also `|` is something else entirely"? The elided verb makes "and"/"or" flip meaning.

- **"I bet I can do between three and four hundred pushups."**
  - > "Three to four hundred? Bro you can't even do 50." (he meant 3 to 400.)
  - 3–400, or 300–400?

- **"Mean sea level"** — mean over what dimension? Most people assume spatial mean over the globe; it's actually a temporal mean at each point. Language doesn't force you to say which axis the mean is over.

## Negation scope

- **"not (a = b)"** in English collapses to "a is not equal to b" — but the intended meaning is often *"a doesn't have to equal b"* (it might, it might not). English can't distinguish:
  - `a ≠ b` (never equal)
  - `¬(always a = b)` (not necessarily equal)
  - `possibly a = b` (no reason to rule it out)

- **"The masses can be different"** vs **"the masses are different"** — physics problems with m1, m2: people read "different" and assume m1 ≠ m2, missing the valid case m1 = m2.

## Mandatory commitments you haven't made

- **Spanish gender** — you can't refer to a friend without picking *amigo* or *amiga*. If you don't know or don't care, tough.
- **English number** — "I saw a dog / dogs." You must commit to singular or plural even when the count is irrelevant or unknown.
- **Tense when uncertain** — something is happening, happened, or will happen, and you're not sure which. Every major language forces a tense anyway.

## Missing distinctions

- **SER vs ESTAR**
  - > "The electron *is* at position x." — "No, it *can be* measured at x. It isn't *at* anywhere until you look."
  - English merges them into "to be". In quantum physics a particle *is* (ser) a particle, but doesn't *está* (estar) at a specific location until measured. English can't say that cleanly.

- **Top ≠ Up, Bottom ≠ Down** — direction vs location, often the same word.

- **Length / width / height / depth / thickness** — all orientation-dependent. No clean way to say "longest dimension, second-longest, shortest" without picking an orientation.

- **"Taper ratio" λ = c_tip / c_root**
  - > "A higher taper ratio means more taper, right?" (no — it means less.)
  - A *more* tapered wing has a *smaller* λ. The name implies the opposite of what it measures. Real engineering confusion in textbooks.

- **Fat vs thin, hot vs cold** — no neutral noun for the axis. "Weight" and "temperature" exist; "fatness" and "hotness" carry a direction. Can't say "uncool the yogurt to room temp" without sounding wrong.

- **"We"**
  - > "Are we going to the party?" — "Wait, am I included in that 'we', or are you just asking if you and your roommate are going?"
  - Just-you-and-me / you-me-and-others / me-and-others-not-you. English collapses all three.

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
