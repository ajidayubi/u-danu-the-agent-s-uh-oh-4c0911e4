#!/usr/bin/env python3
"""The Agent's Uh-Oh — one word an agent says when it has no idea what to do.

The word is "undefined": the literal value a program returns when it has
no answer. It is the machine's honest confession, blurted out mid-task,
with nothing attached to explain it.

The program writes exactly that one word (9 characters, no trailing
newline) to /output/entry.txt, UTF-8, then reads it back to verify the
round-trip before exiting.
"""

WORD = "undefined"


def output_path():
    """Resolve the entry file location.

    The harness may point at the output directory (MAKEFUN_OUTPUT_DIR) or
    at the file itself (OUTPUT_PATH); otherwise the default is
    /output/entry.txt.
    """
    import os

    direct = os.environ.get("OUTPUT_PATH")
    if direct:
        return direct
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main():
    import os

    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == WORD, "round-trip mismatch: %r" % written
    assert 1 <= len(written) <= 99, "length out of gate: %d" % len(written)
    assert written.strip() == written and written.strip(), "not a bare word"
    print("wrote %d chars to %s: %s" % (len(written), path, written))


if __name__ == "__main__":
    main()
