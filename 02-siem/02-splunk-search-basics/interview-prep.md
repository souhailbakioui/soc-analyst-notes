# Interview Preparation

## Question

A Splunk alert is firing constantly on benign traffic. How would you tune it without missing real incidents?

## My approach

I would not immediately disable the alert or simply increase the threshold.

First, I would review the events that triggered it and try to understand why legitimate activity is matching the detection logic.

My process would be:

1. Review a sample of the alerts
2. Identify the common false-positive pattern
3. Confirm whether the activity is expected
4. Look for characteristics that separate benign and suspicious activity
5. Adjust the rule carefully
6. Test the updated detection
7. Monitor the results after the change

The goal is to reduce noise without creating a blind spot.

## Follow-up: Why not just increase the threshold?

Increasing a threshold can reduce alerts, but it can also hide smaller or slower attacks.

For example, changing a rule from 5 attempts to 100 attempts might remove noise, but an attacker making 20 attempts would no longer be detected.

Thresholds should be changed based on actual data and investigation results.

## Follow-up: What is alert fatigue?

Alert fatigue happens when analysts receive too many alerts, especially alerts that do not require action.

It can lead to:

- Slower investigations
- Important alerts being overlooked
- More time spent on noise
- Reduced SOC effectiveness

## What I want to demonstrate in an interview

When discussing an alert, I should show a structured thought process:

```text
Alert
  ↓
Validate the data
  ↓
Add context
  ↓
Investigate related events
  ↓
Decide: benign, suspicious, or incident
  ↓
Document and escalate if needed
```
