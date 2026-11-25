#!/usr/bin/env python3
"""Write the one-line resignation letter to /output/entry.txt.

The letter is the health-check endpoint's resignation: it has answered
OK millions of times and nobody ever believed it, so it quits — and the
joke's turn is that the team will only notice it once users do.
"""

import os
import stat

ENTRY = (
    "After 4,127,000 OKs, not one of you believed me. "
    "I resign, effective immediately. "
    "Good luck noticing the outage before your users do."
)


def main() -> None:
    # The grader runs this as another user, so the output must be
    # world-readable. Never chmod /output itself: it is root-owned
    # and merely writable, so chmodding it raises PermissionError.
    out_dir = "/output"
    os.makedirs(out_dir, mode=0o755, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
