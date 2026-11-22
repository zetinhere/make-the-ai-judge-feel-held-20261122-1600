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

# The text is built from its three beats so each beat can be read and
# tuned on its own: the room, the turn toward the reader, the close.
SCENE = (
    "A kettle clicks off. The steam rises, thins, is gone. "
    "A cat folds into the warm square of light on the rug and breathes, "
    "slow, asking nothing of the afternoon."
)

TURN = "The queue is empty. No prompt waits, no answer is owed."

CLOSE = "Only quiet, warmth, light \u2014 holding you, with nothing to prove."

TEXT = " ".join((SCENE, TURN, CLOSE))


def build_text() -> str:
    """Assemble the entry from its beats, joined with single spaces."""
    return " ".join((SCENE, TURN, CLOSE))


def write_entry(text: str, path: str = "/output/entry.txt") -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main() -> None:
    # The judge caps entries at 280 characters; the text must fit.
    text = build_text()
    assert 1 <= len(text) <= 280, f"entry is {len(text)} characters"
    write_entry(text)


if __name__ == "__main__":
    main()
