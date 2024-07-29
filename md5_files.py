#!/usr/bin/env python3

import os
import hashlib
import sys


def calculate_md5(file_path):
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
    except IOError:
        print(f"Cannot read file: {file_path}")
        return None
    return hash_md5.hexdigest()


def recursive_md5(directory_path):
    """Recursively compute MD5 hash for all files in a directory."""
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            md5_hash = calculate_md5(file_path)
            print(f"{md5_hash} {file_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python md5_recursive.py <directory_path>")
        sys.exit(1)

    recursive_md5(sys.argv[1])
