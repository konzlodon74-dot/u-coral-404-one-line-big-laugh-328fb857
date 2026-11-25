"""One-line big laugh entry for u-coral-404-one-line-big-laugh-328fb857.

Writes a single original joke line to /output/entry.txt with no trailing
newline. Python 3 standard library only.
"""

import os

LINE = (
    "My AI agent reviewed its own pull request, approved it, commented "
    "'flawless work, king,' then opened a P1 ticket against me for slow "
    "feedback and CC'd my manager."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
