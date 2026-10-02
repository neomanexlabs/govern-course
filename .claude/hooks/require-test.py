#!/usr/bin/env python3
"""Block a commit that changes billing/ code without changing a test."""
import json
import subprocess
import sys

event = json.load(sys.stdin)
command = event.get("tool_input", {}).get("command", "")
if "git commit" not in command:
    sys.exit(0)

# Compare against HEAD, staged or not: the agent often runs `git add … && git commit` as one
# command, and this hook runs before it, when nothing is staged yet.
changed = subprocess.run(
    ["git", "diff", "HEAD", "--name-only"], capture_output=True, text=True
).stdout.split()
if any(p.startswith("billing/") for p in changed) and not any(p.startswith("tests/") for p in changed):
    print("Blocked: this commit changes billing/ with no test. Add a test that fails without the fix (standards/testing.md).", file=sys.stderr)
    sys.exit(2)
sys.exit(0)
