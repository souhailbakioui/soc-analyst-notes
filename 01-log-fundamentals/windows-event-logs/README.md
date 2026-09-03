# Windows Event Logs

## 🎯 Objective

The objective of this lab is to understand Windows Security Event Logs and learn how a SOC analyst can use them to investigate authentication and process activity.

This section focuses on two important Windows Security Event IDs:

* **Event ID 4625** — Failed logon
* **Event ID 4688** — A new process has been created

These events can provide valuable evidence during security investigations.

---

# 📚 What Are Windows Event Logs?

Windows records system and security activity in Event Logs.

For SOC analysts, the **Windows Security log** is particularly important because it can contain information about:

* Successful logons
* Failed logons
* Account activity
* Privilege-related events
* Process creation
* Security policy changes
* Other security-relevant activity

Windows Event Viewer can be used to inspect these events.

---

# 🔐 Event ID 4625 — Failed Logon

Event ID **4625** indicates that an account failed to log on.

A failed logon can happen for many legitimate reasons, including:

* Incorrect password
* Expired credentials
* Misconfigured applications
* Incorrect service-account credentials
* Network authentication problems

However, repeated failed logons may also indicate suspicious activity.

### Important fields to investigate

When analyzing Event ID 4625, look for:

| Field                  | Why it matters                     |
| ---------------------- | ---------------------------------- |
| Account Name           | Account being targeted             |
| Account Domain         | Domain associated with the account |
| Logon Type             | How authentication was attempted   |
| Source Network Address | Origin of the authentication       |
| Workstation Name       | System associated with the attempt |
| Timestamp              | When the event occurred            |
| Failure Reason         | Why authentication failed          |

---

# 🚨 Investigating Failed Logons

A single failed login is usually not enough to indicate an attack.

Look for patterns such as:

```text
Multiple failures
        ↓
Same source
        ↓
Short time period
        ↓
Multiple usernames
        ↓
Possible successful login
```

This type of pattern deserves further investigation.

---

# ⚙️ Event ID 4688 — Process Creation

Event ID **4688** indicates that a new process was created.

Process creation events can be useful when investigating what happened on a Windows endpoint.

Useful information can include:

* New process name
* Process ID
* Parent process
* Account that created the process
* Command line
* Timestamp

The availability of some fields depends on the Windows auditing and logging configuration.

---

# 🔎 Why Process Creation Matters

Suppose an analyst investigates a suspicious login.

The authentication log shows:

```text
Successful authentication
        ↓
User session created
        ↓
Suspicious process started
        ↓
Additional activity
```

Event ID 4688 can help connect authentication activity with process execution.

For example, an analyst may investigate whether a newly created process:

* Was expected
* Was launched by a legitimate parent process
* Used unusual command-line arguments
* Ran from an unusual location
* Was executed by an unexpected account

---

# 🧪 Investigation Workflow

A basic SOC investigation can follow this process:

### 1. Identify the event

Determine which Event ID was generated.

### 2. Examine the timestamp

Determine when the activity occurred.

### 3. Identify the account

Determine which account was involved.

### 4. Identify the source

For authentication events, investigate the source workstation or network address where available.

### 5. Look for related events

Search around the same timestamp for:

* Successful logons
* Failed logons
* Process creation
* Account changes
* Privilege activity

### 6. Build a timeline

Connect events together to understand what happened before and after the suspicious event.

---

# 🛡️ Detection Ideas

## Detect repeated failed logons

A SIEM could identify repeated Event ID 4625 events from the same source.

Example logic:

```text
IF
    Event ID = 4625
AND
    multiple failures occur
AND
    failures originate from the same source
WITHIN
    a defined time window
THEN
    generate an alert
```

The threshold should be tuned for the organization's environment.

---

## Investigate suspicious process creation

Event ID 4688 can be investigated for unusual:

* Process names
* Parent-child relationships
* Command lines
* Execution paths
* User accounts

A detection should consider the normal behavior of the environment to reduce false positives.

---

# ⚠️ False Positives

SOC analysts should consider legitimate explanations.

For Event ID 4625:

* User entered the wrong password
* Password was recently changed
* Service account still uses an old password
* Application configuration problem
* Network authentication issue

For Event ID 4688:

* Normal Windows processes
* Software updates
* Administrative tools
* Security software
* Enterprise management software

Context and correlation are essential.

---

# 🧩 MITRE ATT&CK

Event ID 4625 can provide evidence useful when investigating credential-related activity.

Event ID 4688 can provide evidence useful when investigating execution activity.

The event itself should not automatically be classified as malicious. MITRE ATT&CK mapping should be based on the behavior observed during the investigation.

---

# 🎤 Interview Questions

### Question 1

What does Windows Event ID 4625 indicate?

**Answer:**

It indicates that a logon attempt failed.

---

### Question 2

What does Windows Event ID 4688 indicate?

**Answer:**

It indicates that a new process was created.

---

### Question 3

How would you investigate multiple Event ID 4625 events?

Look at:

* Source IP or network address
* Targeted accounts
* Number of failures
* Time period
* Logon type
* Whether the source is internal or external
* Whether a successful logon followed
* Related events on the target system

---

### Question 4

Why is Event ID 4688 useful to a SOC analyst?

It provides information about process creation and can help establish what executed on a Windows endpoint during an investigation.

---

# 💡 What I Learned

* Windows Security logs are an important source of SOC telemetry.
* Event ID 4625 represents a failed logon.
* Event ID 4688 represents process creation.
* Authentication events should be investigated as patterns rather than isolated events.
* Process creation events can help reconstruct endpoint activity.
* Correlating multiple events provides better investigative context.

---

# 📚 References

Microsoft documentation:

* Windows Security auditing documentation
* Windows Security Event ID 4625
* Windows Security Event ID 4688

See also:

* `../linux-syslog/README.md`
* `../../resources/windows-event-ids.md`
