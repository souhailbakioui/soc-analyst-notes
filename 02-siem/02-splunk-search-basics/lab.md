# Lab: Investigating Suspicious Login Activity

## Objective

Practice a simple SOC investigation using authentication events in Splunk.

The idea is to look for repeated failed login attempts and determine whether they are followed by a successful authentication.

## Scenario

A source IP appears to be generating many failed login attempts.

I want to answer:

1. How many failures occurred?
2. Did they happen in a short period?
3. Which source generated them?
4. Did authentication eventually succeed?

## Step 1 — Find failed logins

```spl
index=main "Failed password"
```

First, I would inspect the raw events and identify the useful fields.

## Step 2 — Group by source

```spl
index=main "Failed password"
| stats count by src_ip
```

This helps identify sources generating a high number of failures.

## Step 3 — Apply a simple threshold

```spl
index=main "Failed password"
| stats count by src_ip
| where count >= 10
```

This does not prove an attack. It simply identifies activity worth investigating.

## Step 4 — Add time

```spl
index=main "Failed password"
| bin _time span=5m
| stats count by src_ip, _time
| where count >= 10
```

Now the detection is more specific: 10 or more failures from the same source within 5 minutes.

## Step 5 — Check for successful authentication

```spl
index=main "Accepted password"
```

If a successful login follows repeated failures, I would compare:

- Source IP
- Username
- Timestamp
- Destination system

## Investigation mindset

Repeated failures can have several explanations:

### Possible benign causes

- User entered the wrong password
- Application or service misconfiguration
- VPN authentication problems

### Suspicious indicators

- Unknown external source
- Many attempts in a short period
- Multiple targeted accounts
- Successful login after repeated failures

### What I would check next

If the login succeeded, I would continue looking for:

- Privilege changes
- New accounts
- Suspicious processes
- Unusual network connections
- Other activity from the same user or source

## Conclusion

The detection gives me a starting point.

The final decision depends on the surrounding evidence and context.
