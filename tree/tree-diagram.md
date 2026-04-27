```mermaid
flowchart TD

START --> A1_OPEN
A1_OPEN --> A1_D1

A1_D1 -->|Productive / Mixed| A1_Q_AGENCY_HIGH
A1_D1 -->|Tough / Frustrating| A1_Q_AGENCY_LOW

A1_Q_AGENCY_HIGH --> A1_R_INT
A1_Q_AGENCY_LOW --> A1_R_EXT

A1_R_INT --> BRIDGE_1_2
A1_R_EXT --> BRIDGE_1_2

BRIDGE_1_2 --> A2_OPEN
A2_OPEN --> A2_D1

A2_D1 -->|Helped / Extra| A2_Q_CONTRIB
A2_D1 -->|Recognition / Frustration| A2_Q_ENT

A2_Q_CONTRIB --> A2_R_CONTRIB
A2_Q_ENT --> A2_R_ENT

A2_R_CONTRIB --> BRIDGE_2_3
A2_R_ENT --> BRIDGE_2_3

BRIDGE_2_3 --> A3_OPEN
A3_OPEN --> A3_D1

A3_D1 -->|Self| A3_Q_SELF
A3_D1 -->|Team / Colleague / Customer| A3_Q_ALTRO

A3_Q_SELF --> A3_R_SELF
A3_Q_ALTRO --> A3_R_ALTRO

A3_R_SELF --> SUMMARY
A3_R_ALTRO --> SUMMARY

SUMMARY --> END