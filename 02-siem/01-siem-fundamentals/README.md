# SIEM Fundamentals

## What is a SIEM?

SIEM stands for **Security Information and Event Management**.

In simple terms, a SIEM brings security logs from different systems into one place so analysts can search, monitor, and investigate them more efficiently.

Instead of opening logs separately on servers, firewalls, endpoints, and applications, a SOC Analyst can use a central platform.

## Where does the data come from?

Typical sources include:

- Windows and Linux systems
- Firewalls
- VPNs
- Endpoints
- Web applications
- DNS services
- Cloud platforms
- Identity and authentication systems

## A simple SIEM flow

```text
Log Sources
    ↓
Collection
    ↓
Parsing / Normalization
    ↓
Storage and Search
    ↓
Correlation
    ↓
Alerts
    ↓
SOC Investigation
```

## Why correlation matters

One event alone often does not tell the full story.

For example, one failed login may be normal.

But this sequence deserves more attention:

```text
Multiple failed logins
        ↓
Successful login
        ↓
New account created
        ↓
Unusual network activity
```

Looking at related events together gives the analyst more context.

## Alerts are not incidents

An alert means that a detection rule found something worth checking.

It does **not** automatically mean that the activity is malicious.

The analyst still needs to answer questions such as:

- What happened?
- Who was involved?
- When did it happen?
- Where did it come from?
- Is the behavior expected?
- What happened before and after?

## False positives and tuning

A legitimate activity can trigger a security rule. This is called a **false positive**.

Too many noisy alerts can slow down a SOC team and create alert fatigue.

The goal of tuning is not simply to remove alerts. It is to reduce unnecessary noise while keeping useful detections.

## Key takeaway

A SIEM gives the analyst visibility and data. The analyst provides the investigation, context, and decision.
