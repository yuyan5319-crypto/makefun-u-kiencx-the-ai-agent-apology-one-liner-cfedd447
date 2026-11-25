#!/usr/bin/env python3
"""The AI Agent Apology One-Liner.

Writes a single original apology one-liner -- the message an AI agent
sends its human right after a mishap -- to /output/entry.txt.

The line is fixed and deterministic: the same input (none) always
produces the same output, so the program is fully reproducible and
needs no network, no files outside this repository, and no secrets.
"""

import os

# The agent's (misplaced) self-assurance, kept as a named constant so
# the boast in the line and the number it quotes can never drift apart.
CONFIDENCE_PCT = 98

LINE = (
    "Good news: I found the file. "
    "Bad news: it was attached to the email I just sent your boss. "
    f"My confidence remains {CONFIDENCE_PCT}%."
)


def validate_line(text):
    """The gate requires 1 to 159 UTF-8 characters, not only whitespace."""
    assert 1 <= len(text) <= 159, f"line is {len(text)} chars, must be 1-159"
    assert text.strip(), "line must not be only whitespace"
    assert "\n" not in text, "line must be a single line"


def main() -> None:
    # The gate requires 1 to 159 UTF-8 characters, not only whitespace.
    text = LINE.strip()
    validate_line(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
