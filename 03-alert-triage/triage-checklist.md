# Day 4 — Alert Triage & Severity Prioritization

This module covers the core workflow of a Tier 1 SOC Analyst: **Alert Triage and Severity Prioritization**. When a SIEM fires dozens or hundreds of alerts a day, knowing how to quickly separate the noise from real threats is critical.

## What I Learned
- The difference between **Technical Severity** and **Business Priority**.
- How to perform systematic alert triage using context (Source, Target, Timeline, User, Asset).
- What a Tier 1 analyst needs to gather before escalating an incident to Tier 2.
- Handling false positives and managing alert fatigue.

## Module Structure
- [Notes](./notes.md) - Detailed learning notes and core concepts.
- [Triage Checklist](./triage-checklist.md) - Step-by-step checklist I use when analyzing alerts.
- [Lab](./lab.md) - Practical triage practice with 10 mixed alerts.
- [Flashcards](./flashcards.md) - Quick review cards for key terms and concepts.
- [Interview Prep](./interview-prep.md) - Common interview questions and practical answers on shift prioritization.

## Basic Triage Flow
```
[ Alert Fires ] ---> [ Gather Context (Source, Target, Timeline) ] ---> [ Validate: True/False Positive? ]
                                                                             │
                      ┌──────────────────────────────────────────────────────┴──────────────────────────────────────┐
                      ▼                                                      ▼                                      ▼
            [ Close as Benign/FP ]                               [ Investigate Further ]                    [ Escalate to Tier 2 ]
```
