#!/usr/bin/env python3
"""Write the 24 November 2026 world-news image to the output directory.

The repository holds the finished image (entry.png); this program copies
it to <output>/entry.png. Standard library only, no network, and the
output bytes are identical on every run because the source file is fixed.
"""
import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
