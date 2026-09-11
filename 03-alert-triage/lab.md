# Lab: Triage Practice (10 Mixed Alerts)

### Alert 1: Vulnerability Scanner Activity
- **Type:** Port Scanning / Vulnerability Assessment
- **Source:** 192.168.10.50 (Internal IP)
- **Target:** Internal Subnet 192.168.20.0/24
- **Context:** Security scanner tool running scheduled weekly vulnerability assessment against internal servers. Checked change management: approved task.
- **Decision:** Close as benign
- **Reason:** Verified as authorized internal vulnerability scanning activity matching scheduled maintenance windows.

### Alert 2: Repeated Failed Logins Followed by Success
- **Type:** Brute Force / Successful Authentication
- **Source:** 203.0.113.45 (External IP - Unknown)
- **Target:** Remote Desktop Gateway (rdp.company.com)
- **Context:** 15 failed password attempts for user `jsmith`, followed immediately by a successful login from the same external IP. User confirms they were not traveling or logging in at that time.
- **Decision:** Escalate
- **Reason:** High probability of credential stuffing or brute force leading to unauthorized account compromise.

### Alert 3: Suspicious PowerShell Execution
- **Type:** Execution / Living off the Land
- **Source:** Workstation WS-042 (User: mross)
- **Target:** Local PowerShell Process
- **Context:** PowerShell executed with `-enc` (encoded command) downloading a script from an external paste site. EDR blocked the network connection attempt.
- **Decision:** Investigate further / Escalate
- **Reason:** Encoded PowerShell pulling remote payloads is a strong indicator of malicious execution, even though EDR blocked the download.

### Alert 4: High Severity Alert on Decommissioned Server
- **Type:** Malware Detection
- **Source:** Internal Workstation
- **Target:** SRV-TEST-01 (Decommissioned test server with no data)
- **Context:** Antivirus triggered a high-severity malware signature alert, but the target server was powered down and decommissioned last month.
- **Decision:** Close as benign
- **Reason:** Asset is offline and decommissioned; technical severity is high, but real-world business priority and impact are zero.

### Alert 5: Privileged Account Login from Unusual Location
- **Type:** Impossible Travel / Privilege Abuse
- **Source:** IP from country X, followed 1 hour later by login from country Y for domain admin account.
- **Target:** Active Directory Domain Controller
- **Context:** Domain admin account logged in from two geographically impossible locations within an hour. User is currently sitting at their desk in the local office.
- **Decision:** Escalate
- **Reason:** Classic sign of session hijacking or compromised domain admin credentials requiring immediate containment.

### Alert 6: Standard User Accessing Shared HR Folder
- **Type:** Unauthorized File Access Attempt
- **Source:** Workstation WS-105 (User: ParkETING)
- **Target:** File Server - HR Confiential Share
- **Context:** Marketing intern attempted to open a restricted folder. Access was denied by Windows NTFS permissions. User was looking for company holiday party photos.
- **Decision:** Close as benign
- **Reason:** Access was denied by permissions, and user intent appears accidental/harmless based on follow-up context.

### Alert 7: Outbound Connection to Known C2 IP
- **Type:** Command and Control (C2) Communication
- **Source:** Workstation WS-012 (Finance Department)
- **Target:** 198.51.100.22 (Threat Intel match: known Cobalt Strike C2 server)
- **Context:** Firewall logs show regular beaconing intervals (every 60 seconds) outbound to an IP flagged on multiple threat intelligence feeds.
- **Decision:** Escalate
- **Reason:** High-fidelity threat intelligence match with beaconing behavior indicates active malware infection.

### Alert 8: Mass File Renaming (Simulated Ransomware)
- **Type:** Ransomware Behavior
- **Source:** Workstation WS-089 (User: jdoe)
- **Target:** Network Share (Home directory)
- **Context:** EDR triggered an alert for rapid renaming of files with a `.locked` extension. Investigation revealed it was a developer testing a local backup script gone wrong.
- **Decision:** Investigate further (False Positive verification)
- **Reason:** While behavior matches ransomware, developer context and lack of ransom note require quick verification before closing or escalating.

### Alert 9: DNS Tunneling Query Spike
- **Type:** Data Exfiltration / Tunneling
- **Source:** Workstation WS-033
- **Target:** External DNS Server
- **Context:** Unusually long DNS queries containing base64-encoded strings directed to a suspicious external resolver over port 53.
- **Decision:** Investigate further
- **Reason:** Long random subdomains querying external servers strongly suggest data exfiltration or C2 tunneling over DNS.

### Alert 10: Local Administrator Account Created
- **Type:** Account Manipulation
- **Source:** Workstation WS-015
- **Target:** Local SAM Database
- **Context:** New local user `support_temp` added to the local Administrators group. Checked IT ticketing system: approved IT support ticket for temporary troubleshooting.
- **Decision:** Close as benign
- **Reason:** Authorized administrative action verified against active change request ticket.
