# SPL Queries

> These examples are for learning. Index names, field names, and event text can change depending on the dataset.

## Search all events

```spl
index=main
```

## Search failed logins

```spl
index=main "Failed password"
```

## Search successful logins

```spl
index=main "Accepted password"
```

## Count failed logins

```spl
index=main "Failed password"
| stats count
```

## Count failed logins by source IP

```spl
index=main "Failed password"
| stats count by src_ip
```

## Find sources with 10 or more failures

```spl
index=main "Failed password"
| stats count by src_ip
| where count >= 10
```

## Look for repeated failures in a 5-minute window

```spl
index=main "Failed password"
| bin _time span=5m
| stats count by src_ip, _time
| where count >= 10
```

## Search both failed and successful authentication events

```spl
index=main ("Failed password" OR "Accepted password")
```

## Before using a query

Check the actual dataset first:

- What is the correct index?
- Which sourcetype contains the logs?
- What fields are available?
- How is the source IP named?
- What exact message represents a failed login?

A query that works in one dataset may need changes in another.
