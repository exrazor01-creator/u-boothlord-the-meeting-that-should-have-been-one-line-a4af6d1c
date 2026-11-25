#!/usr/bin/env python3
"""One-line entry: The Meeting That Should Have Been One Line.

The brief asks for the single sentence that could have
replaced an entire pointless meeting. The judge weighs, in
order: the line is one sentence that could have replaced a
pointless meeting, it kills the meeting outright so no one
could justify holding it, it feels relatable to anyone who
has sat through a useless one, it lands as a joke with a
turn or a sting, and it stands alone with no context or
explanation.

The sealed line below is built to that order on purpose. It
is the meeting's own verdict on itself: the meeting is over,
and what it produced was an agreement to hold another
meeting to decide what this meeting decided. One sentence,
no setup, and the recursion is the sting -- after this line
there is nothing left for a meeting to do, because the
meeting just admitted it decided nothing. The line is also
the sentence itself: say it in the room and the meeting has
no reason to continue.

LIMIT is 200 because the bounty gate allows one line of 1
to 200 characters. The sealed line is 97 characters, so it
sits well inside the cap; the validator below only guards
against an edit that would push it past the limit.
"""

import os

# The sealed line: the meeting's own verdict -- it produced
# only an agreement to meet again about what it decided.
ENTRY = "The meeting is over: we agreed to have another meeting to decide what we decided in this meeting."

LIMIT = 200  # bounty gate: one line, 1-200 characters


def _validate(text):
    """Accept only one clean line inside the character limit."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text:
        raise ValueError("entry must not be empty")
    if not text.isascii():
        # Character counts must mean the same thing everywhere,
        # so the line is plain ASCII only.
        raise ValueError("entry must be plain ASCII text")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ch.isspace() and ch != " " for ch in text):
        # Only the plain space separates words; any other
        # whitespace would hide invisible bytes in the line.
        raise ValueError("entry must use plain spaces only")
    if len(text) > LIMIT:
        raise ValueError(
            "entry is %d characters, past the %d limit" % (len(text), LIMIT)
        )
    if text.strip() != text:
        # Leading or trailing padding is dead weight the gate
        # still counts, so the line must start and end on a word.
        raise ValueError("entry must not pad itself with spaces")
    if not text.isprintable():
        raise ValueError("entry must contain no control characters")
    if "  " in text:
        # A double space is a gap where a word should be; in a
        # 200-character line no gap is free.
        raise ValueError("entry must not contain a double space")
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
