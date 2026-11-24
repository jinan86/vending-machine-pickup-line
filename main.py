#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single pickup line, spoken by a vending machine to a passing
human, to /output/entry.txt.

Python 3.13, standard library only, no network, fully deterministic:
every run writes byte-identical output.
"""

import os

# The entry: one pickup line from a vending machine (70 chars).
PICKUP_LINE = "Everybody else gets my sold-out light. You? I just restocked my heart."

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 200


def build_entry() -> str:
    """Return the contest entry, validated against the length rule."""
    text = PICKUP_LINE.strip()
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS} chars, got {len(text)}"
    )
    assert text.strip(), "entry must not be whitespace-only"
    return text


def write_entry(text: str) -> None:
    """Write the entry text to the output path, creating dirs as needed."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main() -> None:
    """Build the entry and write it to the output path."""
    write_entry(build_entry())


if __name__ == "__main__":
    main()
