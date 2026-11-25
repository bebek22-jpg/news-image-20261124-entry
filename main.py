#!/usr/bin/env python3
"""Write the 24 November 2026 world-news image to the output directory.

The repository holds the finished image (entry.png); this program copies
it to <output>/entry.png. Standard library only, no network, and the
output bytes are identical on every run because the source file is fixed.

The copy is verified before the program exits: the destination must be
byte-identical to the source (size and SHA-256), and the image must pass
the competition's gate limits (a PNG, at most 1 MiB and at most 1024 by
1024 pixels). A failed check exits non-zero with a clear message instead
of silently writing a broken or invalid entry.
"""
import hashlib
import os
import shutil
import struct
import sys

MAX_BYTES = 1_048_576
MAX_DIMENSION = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def check_png(path):
    """Check the file is a PNG within the competition's gate limits."""
    with open(path, "rb") as handle:
        header = handle.read(33)
    if len(header) < 33 or header[:8] != PNG_MAGIC:
        fail(f"{path} is not a PNG file")
    if header[12:16] != b"IHDR":
        fail(f"{path} has no PNG IHDR chunk")
    width, height = struct.unpack(">II", header[16:24])
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        fail(f"{path} is {width}x{height}, over the 1024x1024 limit")
    size = os.path.getsize(path)
    if size > MAX_BYTES:
        fail(f"{path} is {size} bytes, over the 1 MiB limit")


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if not os.path.isfile(src):
        fail(f"source image missing: {src}")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    if os.path.getsize(dst) != os.path.getsize(src) or sha256_of(dst) != sha256_of(src):
        os.remove(dst)
        fail(f"copy to {dst} is not byte-identical to {src}")
    check_png(dst)


if __name__ == "__main__":
    main()
