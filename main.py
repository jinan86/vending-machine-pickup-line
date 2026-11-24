#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single pickup line, spoken by a vending machine to a passing
human, to /output/entry.txt.

Python 3.13, standard library only, no network, fully deterministic:
every run writes byte-identical output.
"""

import os

LINE = "Everybody else gets my sold-out light. You? I just restocked my heart."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip(), "entry must not be whitespace-only"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
