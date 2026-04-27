Design Rationale — Daily Reflection Tree
Why These Three Axes?
This reflection tool is built around three psychological axes that, when experienced in sequence, naturally guide a person from reaction → contribution → meaning.
Axis 1 — Locus (Victim ↔ Victor)
Inspired by Julian Rotter’s Locus of Control and Carol Dweck’s Growth Mindset, this axis helps the employee notice whether they experienced the day as something that happened to them or something they actively navigated.
The goal is not to assign blame but to surface agency.
Most people end difficult days feeling powerless. Carefully designed questions help them recognize where they still made choices — even small ones.
This is the foundation. Without a sense of agency, reflection cannot progress meaningfully.

Axis 2 — Orientation (Entitlement ↔ Contribution)
Grounded in Organizational Citizenship Behavior (Organ, 1988) and research on Psychological Entitlement (Campbell et al., 2004), this axis shifts attention from:

“What did I receive today?”
to
“What did I give today?”

Entitlement is often invisible to the person experiencing it. Instead of accusing, the tree uses situational questions to make this pattern visible through the employee’s own selections.
Once a person sees their agency (Axis 1), they are more ready to examine how they contributed (Axis 2).

Axis 3 — Radius (Self-centrism ↔ Altrocentrism)
Inspired by Maslow’s later work on Self-Transcendence (1969) and Batson’s work on Perspective-Taking, this axis widens the frame of concern.
Most workplace stress feels larger because it is viewed only through a self-focused lens. When the employee considers team members, colleagues, or customers, problems are contextualized within something larger.
This axis introduces meaning — the realization that contributing beyond oneself reduces emotional friction and increases fulfillment.

Why These Specific Questions?
The questions were designed with the following principles:


Realistic at 7pm — A tired employee should still feel able to answer honestly without overthinking.


Non-leading options — Each option represents a believable, human reaction. There are no “obviously correct” choices.


Branch-worthy answers — Options are meaningfully different so that branching feels purposeful.


Self-recognition — Many questions reuse the employee’s earlier words through interpolation, making the reflection feel personal without any AI generation.


Progressive depth — Early questions are simple and descriptive; later ones become more reflective and perspective-driven.


Each axis contains:


At least two question nodes


A decision node to route based on patterns


A reflection node that reframes without moralizing


A bridge that prepares the mind for the next axis



How the Branching Was Designed
The tree uses two mechanisms:


Immediate decisions based on the last answer (e.g., productive vs frustrating day)


Accumulated signals (axis1:internal, axis2:contribution, etc.) to determine dominant patterns


This allows reflections to respond to patterns, not single answers.
Trade-offs made:


Avoided too many branches to keep the tree readable as data


Avoided overly complex routing so another developer can easily build an agent from the file


Chose clarity over cleverness — the structure should be auditable without running code



How This Tree Makes a Person Reflect
The tree does not ask the employee to “be better.”
Instead, it guides them to notice:


How they responded to events (agency)


What they focused on giving (contribution)


Who they were thinking about (radius)


By the time the employee reaches the summary, they see their own words quoted back to them across these three dimensions.
This creates a powerful moment of recognition:

“That is exactly how I showed up today.”

Because the tool is deterministic, this insight feels trustworthy.
Because it uses their own answers, it feels personal.
Because it avoids moralizing, it feels safe.

What I Would Improve With More Time


Add more nuanced branches for mixed patterns (e.g., internal locus but high entitlement)


Expand the tree to include optional micro-reflections within each axis


Build a visual interface for easier daily use


Conduct user testing to refine question wording for clarity and emotional impact



This tree encodes psychological insight into a structured, predictable conversation that helps employees end their day with clarity, ownership, and perspective.