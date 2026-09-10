# Splunk Search Basics

This module is my introduction to using Splunk for basic security investigations.

The focus is on **SPL (Search Processing Language)** and using authentication events to investigate suspicious login activity.

## Scenario

A common pattern to investigate is:

```text
Repeated failed logins
        ↓
Same source
        ↓
Short time period
        ↓
Successful login
```

This can be a sign of password guessing or brute-force activity, but the pattern still needs context before calling it an incident.

## Module files

- [Notes](notes.md)
- [SPL Queries](spl-queries.md)
- [Lab](lab.md)
- [Flashcards](flashcards.md)
- [Interview Preparation](interview-prep.md)

## What I practiced

- Basic Splunk searches
- Filtering authentication events
- Using pipes
- Counting events with `stats`
- Grouping activity by source
- Looking at events over time
- Building a simple brute-force detection idea

> Field names and event messages depend on the dataset. A query should always be adapted to the actual data available.
