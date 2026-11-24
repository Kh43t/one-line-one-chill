#!/usr/bin/env python3
"""One Line, One Chill — make.fun entry.

The program writes a single sentence of horror to /output/entry.txt:
one breath, one scare, under 200 characters. The line itself is fixed
text; the program's whole job is to deliver it exactly, as UTF-8,
with no trailing newline games and no extra output.
"""

import os
from pathlib import Path

LINE = (
    "Biscuit has barked at the empty corner of the nursery "
    "every night for six years; tonight he stopped \u2014 and "
    "started wagging his tail."
)

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")
    if text != text.strip() or not text:
        raise SystemExit("entry must not be blank or padded")
    if "\n" in text or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence on one line")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    target = OUTPUT_DIR / "entry.txt"
    target.write_text(text, encoding="utf-8")
    os.chmod(target, 0o644)
    print(f"wrote {len(text)} characters to {target}")


if __name__ == "__main__":
    main()
