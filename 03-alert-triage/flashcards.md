# Flashcards: Alert Triage & Severity

### Q: What is the main goal of Tier 1 alert triage?
A: To quickly review incoming alerts, filter out false positives, and identify genuine security incidents that require deeper investigation or escalation.

### Q: What is the difference between alert severity and business priority?
A: Severity is technical (how bad the activity looks on paper). Priority factors in severity plus business context—such as what asset is affected and the actual impact if the threat is real.

### Q: What is the minimum a Tier 1 analyst needs before escalating an incident?
A: Enough solid evidence so Tier 2 can act without restarting triage from scratch: source details, clear timeline, affected asset/user, and a summary of why it is believed to be real.

### Q: An alert is HIGH severity but hit a decommissioned test server with no data. How should priority differ?
A: Priority should be lower than severity because the real-world impact on business operations is minimal.

### Q: What is a False Positive (FP)?
A: Legitimate or safe activity that incorrectly triggers a security detection rule (e.g., vulnerability scanners or admin scripts).

### Q: What is alert fatigue?
A: Mental exhaustion and desensitization experienced by analysts due to an overwhelming volume of alerts, leading to slower response times or missed threats.

### Q: Why is collecting the "Timeline" crucial during triage?
A: It helps determine if an alert is a single isolated event or part of a broader multi-stage attack chain (e.g., initial access followed by execution and exfiltration).

### Q: What are the three primary outcomes of alert triage?
A: 1) Close as Benign/False Positive, 2) Investigate further, 3) Escalate to Tier 2.
