# Linux Authentication Log Analysis

## 🎯 Objective

The objective of this lab is to learn how to analyze Linux authentication logs and identify failed SSH login attempts.

We will:

* Understand Linux authentication logs
* Identify failed SSH authentication attempts
* Extract source IP addresses
* Count failed attempts per source
* Identify potentially suspicious authentication activity
* Automate the analysis using Python

---

## 📚 Concepts

### Syslog

Syslog is a standard mechanism used by systems and applications to generate and store log messages.

On many Linux systems, authentication-related events can be found in:

```text
/var/log/auth.log
```

On some distributions, authentication events may instead be stored in:

```text
/var/log/secure
```

The exact location depends on the Linux distribution and logging configuration.

---

## 🔐 SSH Authentication Logs

SSH authentication events can provide useful information for a SOC analyst.

A failed SSH login may look similar to:

```text
Sep 03 10:15:32 server sshd[1234]: Failed password for invalid user admin from 203.0.113.45 port 45231 ssh2
```

Important fields include:

| Field       | Meaning                         |
| ----------- | ------------------------------- |
| Timestamp   | When the event occurred         |
| Hostname    | System that generated the event |
| Process     | `sshd`                          |
| Event       | Failed password                 |
| Username    | Account targeted                |
| Source IP   | Origin of the connection        |
| Source Port | Port used by the remote client  |
| Protocol    | SSH                             |

---

# 🔎 Investigation

## Step 1 — Locate the authentication log

On Debian/Ubuntu systems:

```bash
sudo ls -l /var/log/auth.log
```

On systems using `/var/log/secure`:

```bash
sudo ls -l /var/log/secure
```

---

## Step 2 — Find failed SSH authentication attempts

For `/var/log/auth.log`:

```bash
grep "Failed password" /var/log/auth.log
```

This filters the log for messages containing:

```text
Failed password
```

---

## Step 3 — Extract source IP addresses

A simple approach is:

```bash
grep "Failed password" /var/log/auth.log
```

Then inspect the `from` field.

Example:

```text
Failed password for invalid user admin from 203.0.113.45
```

The source IP is:

```text
203.0.113.45
```

---

## Step 4 — Count failed attempts per IP

A simple Linux pipeline can be used to count source IPs:

```bash
grep "Failed password" /var/log/auth.log \
| grep -oE 'from ([0-9]{1,3}\.){3}[0-9]{1,3}' \
| awk '{print $2}' \
| sort \
| uniq -c \
| sort -nr
```

This produces results similar to:

```text
200 203.0.113.45
87  198.51.100.27
43  192.0.2.18
```

The IP addresses above use documentation ranges and are examples only.

---

# 🐍 Python Analysis

The same investigation can be automated using Python.

The script is located at:

```text
failed_ssh.py
```

Run it with:

```bash
python3 failed_ssh.py sample-auth.log
```

Example output:

```text
Top 5 source IPs by failed SSH login attempts:

203.0.113.45   200
198.51.100.27    87
192.0.2.18       43
```

---

# 🚨 Analyst Interpretation

A large number of failed SSH authentication attempts from the same source IP may indicate:

* SSH brute-force activity
* Password spraying
* Automated scanning
* A misconfigured legitimate service
* A legitimate administrator repeatedly entering an incorrect password

A high number of failures alone does **not** prove that an attack occurred.

A SOC analyst should correlate the activity with additional evidence.

Useful information includes:

* Time range
* Targeted usernames
* Successful logins
* Source IP reputation
* Geographic location
* Other systems contacted by the source
* Authentication patterns
* Whether the source belongs to the organization
* Whether the account is a service account
* Commands executed after successful authentication

---

# 🔍 Example Investigation

Suppose an IP generates:

```text
200 failed SSH attempts
```

within:

```text
10 minutes
```

against a jump server.

This is highly suspicious and is consistent with brute-force activity.

The analyst should investigate:

```text
1. Which usernames were targeted?
2. Did any login succeed?
3. When did the successful login occur?
4. Was the source IP external?
5. Did the same IP attack other systems?
6. What happened after authentication?
7. Is the source IP known or expected?
```

---

# 🛡️ Detection Idea

A SIEM could generate an alert when multiple failed SSH authentications occur from the same source within a short time window.

Example detection logic:

```text
IF
    authentication = SSH
AND
    result = failure
AND
    count(source_ip) >= threshold
WITHIN
    10 minutes
THEN
    generate alert
```

The threshold should be tuned according to the environment.

For example:

```text
20 failures / 10 minutes
```

could be suspicious in one environment, while another environment may legitimately generate more failures.

---

# ⚠️ False Positives

Possible legitimate explanations include:

### Misconfigured service

A service may repeatedly attempt authentication using an outdated password.

### Administrator error

An administrator may accidentally enter the wrong password multiple times.

### Automated infrastructure

Monitoring or deployment systems may repeatedly authenticate to servers.

### Security testing

Authorized penetration testing or vulnerability scanning can generate authentication failures.

Therefore, context is critical.

---

# 🧩 MITRE ATT&CK

This type of activity can be associated with:

**MITRE ATT&CK T1110 — Brute Force**

Relevant sub-techniques may include:

* Password Guessing
* Password Spraying
* Credential Stuffing

Mapping should be based on the actual observed behavior rather than automatically labeling every failed login as an attack.

---

# 🎤 Interview Question

### Question

How would you distinguish a brute-force attack from a misconfigured service account in the logs?

### Investigation approach

I would compare several indicators rather than relying only on the number of failed logins.

I would investigate:

* Source IP
* Targeted username
* Authentication frequency
* Time pattern
* Whether the source is internal or external
* Whether the account is a known service account
* Whether the failures occur at regular intervals
* Whether successful authentication eventually occurs
* What process or system is generating the connections
* Whether similar activity is occurring against other systems

A misconfigured service account may produce predictable, repetitive authentication attempts from a known internal system, while brute-force activity may involve many usernames, high-frequency attempts, external sources, or attempts across multiple systems.

---

# 💡 What I Learned

* Linux authentication logs contain valuable security information.
* SSH failures can be detected through log patterns.
* Source IPs can be extracted and counted.
* A large number of failed logins can indicate brute-force activity.
* Authentication failures must be investigated in context.
* Automation can make repetitive log analysis much faster.
* Detection rules need thresholds and tuning to reduce false positives.

---

# 📌 Key Commands

```bash
# Search failed SSH logins
grep "Failed password" /var/log/auth.log

# Follow authentication logs in real time
sudo tail -f /var/log/auth.log

# Search successful SSH authentication
grep "Accepted" /var/log/auth.log

# Count source IPs
grep "Failed password" /var/log/auth.log \
| grep -oE 'from ([0-9]{1,3}\.){3}[0-9]{1,3}' \
| awk '{print $2}' \
| sort \
| uniq -c \
| sort -nr
```

---

# 📚 References

* Linux `syslog` documentation: https://man7.org/linux/man-pages/man3/syslog.3.html
* Microsoft Windows security auditing documentation: https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/basic-audit-logon-events
* MITRE ATT&CK: https://attack.mitre.org/techniques/T1110/

---

## 🔬 Next Steps

Possible extensions to this lab:

* Detect successful login after multiple failures
* Group failures by username
* Detect password spraying
* Analyze authentication activity by time
* Create a simple brute-force detector
* Send logs to a SIEM
* Create an alert based on authentication thresholds
