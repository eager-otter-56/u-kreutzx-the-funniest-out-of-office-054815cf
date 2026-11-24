"""Entry for 'The Funniest Out-of-Office': writes one line to entry.txt."""

import os

TEXT = "Out of office until Monday: I'm best man at my brother's wedding, in charge of the rings, the speech, and stopping Uncle Ray doing the worm."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
