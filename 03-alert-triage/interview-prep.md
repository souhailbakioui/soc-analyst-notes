# Interview Prep: Alert Triage Scenarios

## Question: You have 40 open alerts and 30 minutes left in your shift. How do you decide what to work first?

**Junior SOC Analyst Answer:**
When time is tight and the queue is backed up, I can't look at everything, so I have to prioritize based on risk and potential impact rather than just order or age. 

First, I would quickly scan the queue to filter out low-severity or known noisy alerts. Then, I would focus my remaining time on high-priority assets—like domain controllers, payment servers, or executive workstations—looking specifically for high-severity indicators like potential malware execution, credential dumping, or active C2 beaconing. 

If I spot an alert that looks critical and time-sensitive, I'll dive into that one. For the remaining alerts, I'll document my shift handover clearly, noting what was left unworked and flagging any high-risk items so the incoming shift analyst can pick them up right away.

---

## Follow-up Questions & Answers

### Q: Why not just work alerts oldest first?
- **Answer:** Working strictly oldest-first can cause analysts to waste precious time on stale false positives while a critical, active intrusion sits at the bottom of a newer queue. Risk and asset criticality matter more than timestamp order.

### Q: High severity alert on a decommissioned test server — what happens to priority?
- **Answer:** The business priority drops significantly. Even though the technical signature (severity) looks bad, a decommissioned server with no data or network connectivity poses minimal risk to the organization.

### Q: What is the minimum information needed before escalating an alert?
- **Answer:** I need enough context so Tier 2 doesn't have to start from scratch: the source and target identifiers, a clear timeline of events, the user or service account involved, and the specific evidence or logs that convinced me the alert is valid.

### Q: Why is triage important for a SOC?
- **Answer:** Triage is the frontline filter of the SOC. Without it, analysts would drown in noise and false positives, increasing response times and letting real attackers move undetected through the network.
