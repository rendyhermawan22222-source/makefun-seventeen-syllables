#!/usr/bin/env python3
"""Seventeen Syllables of Debugging entry: one haiku, 5-7-5, about debugging.

The haiku is rubber-duck debugging at 3 a.m.: the duck listens while the
debugger blames the code, and the last line turns the blame around - the
code blames the debugger back. Concrete picture (the duck, the code),
self-referential loop, deadpan throughout; the turn lands in the last
five syllables.
"""
import os

HAIKU = (
    "three a.m., the duck\n"
    "listens while I blame the code\n"
    "the code blames me back\n"
)

# Syllable counts for the exact words used, so the 5-7-5 shape is verified
# at runtime rather than trusted ("a.m." is two syllables: ay-em).
SYLLABLES = {
    "three": 1, "a.m.,": 2, "the": 1, "duck": 1,
    "listens": 2, "while": 1, "i": 1, "blame": 1, "code": 1,
    "blames": 1, "me": 1, "back": 1,
}


def count_syllables(line):
    return sum(SYLLABLES[w] for w in line.lower().split())


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, "entry.txt")
    with open(out, "w", encoding="ascii") as f:
        f.write(HAIKU)
    # Read-back verification: what ships is exactly the haiku.
    with open(out, "r", encoding="ascii") as f:
        back = f.read()
    assert back == HAIKU, "read-back mismatch"
    lines = HAIKU.rstrip("\n").split("\n")
    assert len(lines) == 3, "haiku must be three lines"
    assert len(HAIKU) <= 200, "haiku exceeds 200 characters"
    counts = [count_syllables(line) for line in lines]
    assert counts == [5, 7, 5], f"not 5-7-5: {counts}"
    print(f"wrote {len(HAIKU)} chars, syllables {counts}, to {out}")


if __name__ == "__main__":
    main()
