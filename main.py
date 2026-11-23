"""One-Line Laugh entry: write a single funny line to /output/entry.txt.

The gate requires the file to be UTF-8 text of 1 to 200 characters, not
only whitespace, and the entry must stand alone as a single sentence.
The line below is validated against those rules before it is written.
"""

import os

LINE = "My fitness tracker congratulated me on 10,000 steps, all of them pacing in front of the microwave."

MAX_CHARS = 200


def validate_entry(text):
    """Check the line against the competition gate."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d characters, over the 200 limit" % len(text))
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    text.encode("utf-8")
    return text


def output_path():
    """Return the path of the entry file for this run."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def write_entry(text, path):
    """Write the validated line to the entry file as UTF-8."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main():
    line = validate_entry(LINE)
    write_entry(line, output_path())


if __name__ == "__main__":
    main()
