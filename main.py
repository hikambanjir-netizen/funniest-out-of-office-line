#!/usr/bin/env python3
"""Write the funniest out-of-office entry line (final pass 2).

The line is a single out-of-office auto-reply: a real person could set
it, and the twist lands in the second half -- the replacement staff
are circus clowns, and they are still an upgrade on the sender.
"""
import os

ENTRY = "Out until Monday \u2014 I ran away to join the circus, and the clowns reply to email faster than I ever did."

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    data = ENTRY.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    with open(os.path.join(HERE, "entry.txt"), "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
