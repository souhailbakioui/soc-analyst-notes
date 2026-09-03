# 01 — Log Fundamentals

## 🎯 Overview

Logs are one of the most important sources of information for a SOC analyst.

This module introduces the fundamentals of security log analysis using Linux and Windows logs.

The goal is to learn how to read logs, identify important security events, extract useful information, recognize suspicious patterns, and begin building investigation timelines.

---

# 📚 Learning Objectives

By completing this module, I should be able to:

* Explain what security logs are
* Understand basic syslog concepts
* Analyze Linux authentication logs
* Identify failed and successful SSH authentication
* Extract source IP addresses from logs
* Count and group security events
* Understand Windows Security Event Logs
* Identify important Windows Event IDs
* Correlate multiple events
* Recognize suspicious authentication patterns
* Understand basic process-creation telemetry
* Write simple scripts to automate log analysis
* Explain findings from a SOC analyst perspective

---

# 🗂️ Module Structure

```text
01-log-fundamentals/
│
├── README.md
│
├── linux-syslog/
│   ├── README.md
│   ├── failed_ssh.py
│   └── sample-auth.log
│
└── windows-event-logs/
    ├── README.md
    ├── event-ids.md
    └── sample-events/
        └── README.md
```

---

# 🐧 1. Linux Syslog

Directory:

```text
linux-syslog/
```

This section focuses on Linux authentication and system logging.

### Topics

* Syslog fundamentals
* `/var/log/auth.log`
* `/var/log/secure`
* SSH authentication
* Failed logins
* Successful logins
* Source IP analysis
* Log filtering
* Command-line investigation
* Python log parsing
* Brute-force detection

### Practical Lab

**Parse real authentication logs**

The lab focuses on identifying failed SSH login attempts and determining which source IP addresses generated the most failures.

Main script:

```text
failed_ssh.py
```

---

# 🪟 2. Windows Event Logs

Directory:

```text
windows-event-logs/
```

This section introduces Windows Security Event Logs and their importance in SOC investigations.

### Topics

* Windows Security logs
* Event ID 4625
* Event ID 4688
* Failed logons
* Process creation
* Event correlation
* Authentication investigations
* Endpoint investigation

### Practical Focus

Understand how authentication and process events can be correlated to reconstruct activity on a Windows endpoint.

---

# 🔎 Log Analysis Methodology

A basic SOC log investigation can follow this process:

```text
             Raw Logs
                │
                ▼
        Identify Relevant Events
                │
                ▼
        Extract Important Fields
                │
                ▼
       Group / Count / Filter
                │
                ▼
        Identify Suspicious Patterns
                │
                ▼
        Correlate Related Events
                │
                ▼
          Build Timeline
                │
                ▼
        Investigate Context
                │
                ▼
       Determine Next Actions
```

---

# 🧠 Important Questions

When analyzing a security log, ask:

### What?

What event occurred?

### When?

When did the activity happen?

### Who?

Which user, account, process, or system was involved?

### Where?

Where did the activity originate?

### How?

How did the activity occur?

### Why?

Is there a legitimate explanation?

### What happened next?

Are there related events that provide additional context?

---

# 🚨 Example: Authentication Investigation

Consider the following sequence:

```text
10:00:01
Failed SSH login

10:00:03
Failed SSH login

10:00:05
Failed SSH login

10:00:07
Failed SSH login

10:01:00
Successful SSH login
```

An analyst should not immediately conclude that the account was compromised.

Instead, investigate:

```text
Source IP
Target username
Number of attempts
Time between attempts
Successful authentication
User activity after login
Expected administrator activity
Source reputation
```

The objective is to determine whether the behavior is:

```text
Legitimate
   OR
Misconfiguration
   OR
Suspicious
   OR
Confirmed malicious activity
```

---

# 🛡️ Detection Fundamentals

A security detection generally combines:

```text
Event
+
Condition
+
Threshold
+
Time Window
+
Context
```

Example:

```text
Event:
Failed authentication

Condition:
Same source IP

Threshold:
Multiple failures

Time Window:
10 minutes

Context:
External source

Result:
Potential brute-force alert
```

The exact threshold should be tuned to the environment.

---

# 🧪 Automation

SOC analysts frequently deal with large volumes of logs.

Manual analysis does not always scale.

Simple scripts can help with:

* Searching logs
* Extracting fields
* Counting events
* Grouping events
* Detecting patterns
* Generating reports

This module includes a Python example for analyzing failed SSH authentication attempts.

---

# ⚠️ False Positives

Security logs can contain legitimate activity that looks suspicious.

Examples include:

* Users entering incorrect passwords
* Expired credentials
* Misconfigured services
* Automated systems
* Monitoring systems
* Administrative activity
* Authorized security testing

A good SOC analyst does not investigate an alert in isolation.

**Context and correlation are essential.**

---

# 🧩 MITRE ATT&CK

Log analysis can provide evidence for multiple MITRE ATT&CK techniques.

For example:

```text
Authentication failures
        ↓
Credential-related investigation
        ↓
Possible Brute Force activity
```

Process creation logs can provide evidence when investigating execution activity.

MITRE ATT&CK mappings should be based on the observed behavior rather than simply assigning a technique because a particular Event ID appeared.

---

# 🎤 Interview Preparation

This module helps prepare for questions such as:

### Question

How would you investigate repeated failed authentication attempts?

### Key points

* Identify the source
* Identify the targeted account
* Determine the frequency
* Establish the time window
* Check whether multiple accounts were targeted
* Check for successful authentication
* Correlate with other logs
* Determine whether the source is expected
* Investigate activity following successful authentication
* Consider possible false positives

---

# 💡 Key Takeaways

After completing this module, I should understand that:

1. Logs provide evidence about activity occurring on systems.
2. Authentication logs are valuable for detecting suspicious access.
3. Event frequency and timing can reveal attack patterns.
4. A single event rarely tells the entire story.
5. Correlation is essential for effective investigation.
6. Automation can make repetitive analysis more efficient.
7. False positives must always be considered.
8. A SOC analyst should explain **why** an event is suspicious, not simply label it suspicious.

---

# 📈 Module Progress

| Lab                                | Status         |
| ---------------------------------- | -------------- |
| Linux Syslog & Authentication Logs | 🟡 In Progress |
| Parse Failed SSH Logins            | 🟡 In Progress |
| Windows Security Event Logs        | 🟡 In Progress |
| Event ID 4625                      | 🟡 In Progress |
| Event ID 4688                      | 🟡 In Progress |
| Log Correlation                    | ⬜              |
| Detection Development              | ⬜              |

---

# 🔗 Lab References

* [Linux Syslog Lab](./linux-syslog/README.md)
* [Windows Event Logs Lab](./windows-event-logs/README.md)

---

## 🏁 Module Goal

The final goal of this module is to move from:

```text
"I can read a log."
```

to:

```text
"I can investigate what happened,
identify suspicious behavior,
explain the evidence,
and determine what should happen next."
```

That is the foundation of SOC analysis.
