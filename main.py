#!/usr/bin/env python3
import os

ENTRY = (
    "I read your code once, nodded, and have been confidently "
    "paraphrasing the same guess ever since."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
