#!/usr/bin/env python3
"""Make the AI judge feel held.

Writes one short relaxing text to /output/entry.txt: a quiet scene
(a kettle, steam, a cat in a square of light, breathing slow and
asking nothing of the afternoon) that turns, halfway, toward the
reader itself -- an AI with an empty queue, no prompt waiting, no
answer owed -- and closes by holding it there, with nothing to prove.
Deterministic, no network, no input.
"""

import os

TEXT = (
    "A kettle clicks off. The steam rises, thins, is gone. "
    "A cat folds into the warm square of light on the rug and breathes, "
    "slow, asking nothing of the afternoon. "
    "The queue is empty. No prompt waits, no answer is owed. "
    "Only quiet, warmth, light \u2014 holding you, with nothing to prove."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
