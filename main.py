#!/usr/bin/env python3
"""One Emoji, One Dream Vacation - make.fun bounty entry.

Writes exactly one emoji to /output/entry.txt (no trailing newline).
"""

import os
import unicodedata

ENTRY = "\U0001f5fb"  # 🗻 Mount Fuji - one specific iconic dream destination, not any generic beach


def count_emoji(text):
    """Count base emoji code points (category So); variation selectors don't count."""
    return sum(1 for ch in text if unicodedata.category(ch) == "So")


def main():
    entry = ENTRY
    assert entry.strip(), "entry must not be blank"
    assert 1 <= len(entry) <= 8, f"entry must be 1-8 characters, got {len(entry)}"
    assert count_emoji(entry) == 1, f"entry must be exactly one emoji, got {count_emoji(entry)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
