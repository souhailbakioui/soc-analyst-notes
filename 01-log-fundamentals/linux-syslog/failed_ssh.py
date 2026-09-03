#!/usr/bin/env python3

"""
Failed SSH Login Analyzer

Purpose:
Parse a Linux authentication log and identify the top 5
source IP addresses associated with failed SSH login attempts.

Usage:
python3 failed_ssh.py <log_file>

Example:
python3 failed_ssh.py sample-auth.log
"""

import re
import sys
from collections import Counter

# Pattern used to identify failed SSH password authentication.

FAILED_SSH_PATTERN = re.compile(
    r"Failed password for .* from "
    r"(?P<ip>\d{1,3}(?:.\d{1,3}){3})"
    )

def analyze_log(filename):
    """
    Read the authentication log and count failed SSH
    authentication attempts by source IP.
    """

    
    failed_attempts = Counter()

    try:
        with open(filename, "r", errors="ignore") as logfile:

            for line in logfile:

                match = FAILED_SSH_PATTERN.search(line)

                if match:
                    source_ip = match.group("ip")
                    failed_attempts[source_ip] += 1

    except FileNotFoundError:
        print(f"[!] Error: File not found: {filename}")
        sys.exit(1)

    except PermissionError:
        print(f"[!] Error: Permission denied: {filename}")
        sys.exit(1)

    return failed_attempts
        

def main():

    
    if len(sys.argv) != 2:
        print("Usage: python3 failed_ssh.py <log_file>")
        sys.exit(1)

    log_file = sys.argv[1]

    results = analyze_log(log_file)

    print("\nTop 5 source IPs by failed SSH login attempts:")
    print("-" * 50)

    if not results:
        print("No failed SSH login attempts found.")
        return

    for ip, count in results.most_common(5):
        print(f"{ip:15} {count}")
        

if __name__ == "__main__":
    main()
