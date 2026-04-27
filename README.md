Daily Reflection Tree — Deterministic End-of-Day Tool

This repository contains a deterministic reflection tool designed as a decision tree.
The tree guides an employee through a structured end-of-day reflection across three psychological axes:

Axis 1 — Locus: Victim ↔ Victor (Agency)
Axis 2 — Orientation: Entitlement ↔ Contribution
Axis 3 — Radius: Self-centrism ↔ Altrocentrism

The tool does not use any LLM at runtime.
All intelligence is encoded directly into the tree structure.

📁 Tree File

/tree/reflection-tree.tsv

This file is the product.
The agent (optional Part B) simply walks this data.

🧱 TSV Columns Explained
Column	Meaning
id	Unique node identifier
parentId	Parent node (forms the tree structure)
type	Node behavior: start, question, decision, reflection, bridge, summary, end
text	What the employee sees. Supports interpolation like {A1_OPEN.answer}
options	Fixed choices (pipe `
target	Explicit jump to another node (used by bridges)
signal	Records state like axis1:internal for tallying patterns
🔄 How the Tree Flows

The conversation always moves in this sequence:

Start → Axis 1 → Bridge → Axis 2 → Bridge → Axis 3 → Summary → End

Question nodes wait for user input
Decision nodes route automatically based on earlier answers
Reflection nodes provide insight based on the path taken
Bridge nodes transition between axes
Summary node synthesizes the entire session using the employee’s own answers

Given the same answers, the same path is always followed.

🧠 What Are Signals?

Signals are simple tags that accumulate state during the session.

Examples:

axis1:internal
axis2:contribution
axis3:altro

These are tallied like:

state.axis1.internal += 1

They allow reflections and the summary to respond to the pattern of answers, not a single choice.

🧾 How the Summary Is Formed

The summary does not generate text.

It uses interpolation from earlier answers:

{A1_OPEN.answer} — how the employee described their day
{A2_OPEN.answer} — how they behaved in interactions
{A3_OPEN.answer} — who they were thinking about

This makes the reflection feel personal while remaining fully deterministic.

✅ Design Principles Followed
No free-text input
No AI classification
No runtime API calls
Fixed options only
Deterministic branching
Psychological grounding in Locus of Control, Organizational Citizenship, and Self-Transcendence

This tree encodes psychological insight into a predictable, auditable structure that guides honest self-reflection at the end of each workday.