#!/usr/bin/env python

import posix_wrapper  #FIXME after moving readdir to generic
pyreaddir = posix_wrapper
import os
import sys
import json

def output_for_path(path):
    # If it's a file, we just list it. If it's a directory, we have to
    # print out the contents.
    if os.path.isdir(path):
        dircontents = pyreaddir.readdir(path)
        for entry in dircontents:
            print entry.to_json()
    elif os.path.lexists(path):
        print path
    else:
        msg = "%s: cannot access %s: No such file or directory"
        sys.stderr.write(msg % (sys.argv[0], path))


def main(argv):
    paths = argv[1:]
    if len(paths) == 0:
        paths = ["."]

    for path in paths:
        output_for_path(path)

if __name__ == "__main__":
    main(sys.argv)
