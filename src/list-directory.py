#!/usr/bin/env python

import posix2  #FIXME after moving readdir to generic
pyreaddir = posix2
import sys


def main(argv):
    paths = argv[1:]
    if len(paths) == 0:
        paths = ["."]

    for path in paths:
        dircontents = pyreaddir.readdir(path)
        for entry in dircontents:
            if entry.is_directory():
                dirmarker = "/"
            else:
                dirmarker = ""
            print "%s%s" % (entry.name, dirmarker)


if __name__ == "__main__":
    main(sys.argv)
