"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one small good thing from this morning: a neighbour's
# cat steals the toast, claims the lap, and purrs like it pays rent.
import os

TEXT = (
    "This morning the neighbour's cat stole my toast, climbed onto my "
    "lap, and purred like it paid rent \u2014 I have never felt so "
    "chosen by a small criminal."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# One line, 149 characters: warm, surprising, and concrete enough to smile at.
