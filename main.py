#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second.

One job: write a single-sentence startup pitch (at most 200 characters)
to the output file the make.fun program/v1 harness grades.

The pitch sells a stranger who says "no" for you: $5 a call to your boss,
your mother-in-law, or your landlord, because people-pleasers will pay to
outsource the one word they cannot say.

Run:  MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

PITCH = (
    "For $5 a call, a trained stranger says no to your boss, "
    "your mother-in-law, or your landlord, because people-pleasers "
    "pay to outsource the one word they can't say."
)


def main() -> None:
    # The gate rejects anything outside 1-200 characters, so fail loudly
    # here instead of writing an entry that can never be judged.
    if not 1 <= len(PITCH) <= 200:
        raise ValueError(f"pitch is {len(PITCH)} characters, must be 1-200")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(PITCH)
    print(PITCH)


if __name__ == "__main__":
    main()
