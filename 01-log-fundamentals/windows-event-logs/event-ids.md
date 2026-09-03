# Windows Security Event IDs

A quick-reference guide for Windows Security events commonly encountered by SOC analysts.

---

# Event ID 4625

## Failed Logon

**Event ID:** `4625`

### Description

A logon attempt failed.

### Why it matters

Repeated failed logons can indicate:

* Brute-force activity
* Password spraying
* Incorrect credentials
* Misconfigured services
* Expired passwords
* Automated applications repeatedly using invalid credentials

### Important fields

Look for:

```text
Account Name
Account Domain
Logon Type
Failure Reason
Source Network Address
Workstation Name
Timestamp
```

### Investigation questions

```text
Who was targeted?

Where did the attempt originate?

How many failures occurred?

How quickly did they occur?

Were multiple accounts targeted?

Did a successful logon occur afterward?

Is the source expected?
```

---

# Event ID 4688

## New Process Created

**Event ID:** `4688`

### Description

A new process was created.

### Why it matters

Process creation events can help an analyst determine what executed on a Windows system.

### Important fields

Depending on audit configuration, investigate:

```text
New Process Name
Process ID
Parent Process
Creator Account
Command Line
Timestamp
```

### Investigation questions

```text
What process was created?

Who created it?

What was the parent process?

What command line was used?

Where was the executable located?

Was the process expected?

Did it occur shortly after a suspicious logon?
```

---

# 🔎 Event Correlation

Individual events rarely provide the complete story.

A SOC analyst should correlate related events.

Example:

```text
10:00
4625 - Failed logon

10:01
4625 - Failed logon

10:02
4625 - Failed logon

10:03
4624 - Successful logon

10:04
4688 - New process created
```

This sequence deserves investigation because it connects authentication activity with subsequent process execution.

---

# 📊 Quick Reference

| Event ID | Description      | SOC Relevance                  |
| -------- | ---------------- | ------------------------------ |
| 4625     | Failed logon     | Authentication investigation   |
| 4688     | Process creation | Endpoint/process investigation |

> Note: Windows generates many other security-relevant Event IDs. This file currently focuses on the events covered in this learning module.

---

# 🧠 Analyst Principle

Do not automatically classify every Event ID 4625 as an attack or every Event ID 4688 as malicious.

The analyst should consider:

* Frequency
* Timing
* Source
* User
* Process
* Parent process
* Command line
* Baseline behavior
* Related events

**Context turns individual events into an investigation.**
