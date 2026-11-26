"""Rejected Olympic Sports (make.fun bounty u-motasimfuad-rejected-olympic-sports-9d83e7da).

Writes one funny single-line sport the Olympics rejected to /output/entry.txt.
Gate: UTF-8, 1-200 characters, one line, not only whitespace, no trailing newline.
"""

ENTRY = "Synchronized apologizing: two Canadians say sorry in perfect unison until one of them actually means it."


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
