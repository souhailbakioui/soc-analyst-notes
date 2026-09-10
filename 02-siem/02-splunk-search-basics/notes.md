# Notes

## Splunk

Splunk is used to search, analyze, and work with machine data.

For a SOC Analyst, this can include authentication logs, endpoint events, firewall logs, VPN activity, and other security-related data.

## SPL

SPL means **Search Processing Language**.

A basic search can start with:

```spl
index=main
```

This searches events in the `main` index.

To search for a specific event:

```spl
index=main "Failed password"
```

## The pipe

The `|` character passes the results of one command to the next.

Example:

```spl
index=main "Failed password"
| stats count
```

The search finds failed login events, then `stats count` counts them.

## Why aggregation is useful

Raw events can be difficult to read when there are thousands of results.

Grouping events can reveal patterns.

For example:

```spl
index=main "Failed password"
| stats count by src_ip
```

This can show which source IP addresses generated the most failed login attempts.

## Time changes the meaning

Ten failed logins over several months may be normal.

Ten failed logins in two minutes are much more interesting.

During an investigation, the number of events and the timeline should be considered together.

## Detection is only the first step

A query can identify suspicious behavior, but the analyst still needs context.

For authentication activity, I would check:

- Source IP
- Username
- Time of activity
- Number of attempts
- Successful authentication
- Related events after the login

## Main takeaway

Searching finds data. Investigation explains what the data means.
