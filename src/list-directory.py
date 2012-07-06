#!/usr/bin/env python

import posix2  #FIXME after moving readdir to generic
pyreaddir = posix2
import sys
import json

def main(argv):
    paths = argv[1:]
    if len(paths) == 0:
        paths = ["."]

    for path in paths:
        dircontents = pyreaddir.readdir(path)
        for entry in dircontents:
            print entry.to_json()


if __name__ == "__main__":
    main(sys.argv)
