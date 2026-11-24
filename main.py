#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry program.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt (override with MAKEFUN_OUTPUT_DIR).

Gate (from the kit's competition.yaml): the file must be UTF-8 text of
1 to 400 characters, not only white space. The chosen rant is a single
line, well inside the cap, and this program verifies the gate itself
after writing, so a bad write can never slip through silently.
"""

import os
import sys

RANT = (
    "One person replied-all 'Thanks!' to the whole company. "
    "Four hundred people. "
    "Then seventeen more replied-all 'Thanks!' to thank the first one. "
    "Then someone replied-all asking to be removed from the thread, "
    "which emailed four hundred people. "
    "The thread is now 84 messages long and nobody remembers "
    "what it was about."
)

MAX_CHARS = 400


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(RANT + "\n")
    # Gate self-check: read back exactly what was written and verify.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    text = written.strip()
    if written != RANT + "\n":
        print("FAIL: file bytes differ from rant + newline", file=sys.stderr)
        return 1
    if not text:
        print("FAIL: entry is empty or only whitespace", file=sys.stderr)
        return 1
    if len(written.rstrip("\n")) > MAX_CHARS:
        print(
            f"FAIL: entry is {len(written.rstrip(chr(10)))} chars, "
            f"over the {MAX_CHARS} cap",
            file=sys.stderr,
        )
        return 1
    if text != RANT:
        print("FAIL: written text differs from the rant", file=sys.stderr)
        return 1
    print(f"Wrote {path}: {len(text)} chars")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
