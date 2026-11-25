#!/usr/bin/env python3
"""Snooze Button Roast - make.fun entry.

Writes one line roasting an alarm clock that rings at 6 AM on a Saturday
to /output/entry.txt. Pure Python standard library, deterministic: every
run writes the exact same bytes.

Gate (from the contest kit): /output/entry.txt must be UTF-8 text of
1-200 characters, not only whitespace, a single line.
"""

import os
import sys

LINE = (
    "My alarm clock rings at 6 AM on a Saturday like it's gunning for "
    "Employee of the Month at a job it doesn't even have."
)
OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def fail(message):
    print("error: " + message, file=sys.stderr)
    sys.exit(1)


def main():
    if not (1 <= len(LINE) <= MAX_CHARS):
        fail(
            "entry must be 1-%d characters, got %d"
            % (MAX_CHARS, len(LINE))
        )
    if not LINE.strip():
        fail("entry must not be only whitespace")
    if "\n" in LINE or "\r" in LINE:
        fail("entry must be a single line (no newline or carriage return inside)")
    try:
        raw = LINE.encode("utf-8")
    except UnicodeEncodeError as exc:
        fail("entry is not valid UTF-8: %s" % exc)

    output_dir = os.path.dirname(OUTPUT_PATH)
    try:
        os.makedirs(output_dir, exist_ok=True)
    except OSError as exc:
        fail("cannot create output directory %s: %s" % (output_dir, exc))

    try:
        with open(OUTPUT_PATH, "wb") as f:
            f.write(raw)
        os.chmod(OUTPUT_PATH, 0o644)
    except OSError as exc:
        fail("cannot write %s: %s" % (OUTPUT_PATH, exc))

    print("entry.txt: %d characters" % len(LINE))


if __name__ == "__main__":
    main()
