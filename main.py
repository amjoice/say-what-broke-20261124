#!/usr/bin/env python3
"""Say What Actually Broke — one line of honest error copy.

Writes a single line of software error copy (at most 200 characters) to
/output/entry.txt. The line names the real failure (a full disk), tells the
user exactly what to do about it, and does it with a twist worth repeating.

Standard library only. Deterministic: the same bytes on every run.
"""

import os

ENTRY = (
    "Disk full. Your file is safe in memory, but memory forgets. "
    "Free 100 MB or this work dies with the tab."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
