import support
import argparse
import readdir
import os
import sys
import json

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory', help='List entry for directories on the command line instead of their contents')
parser.add_argument('-r', '--recursive', help='List directory contents recursively')
parser.add_argument('paths', metavar='PATH', nargs='*', help='Files and directories to display information about')

typeinfo = {
    "type name":               "file info",
    "default display columns": ["name", "path", "kind"]
}


def output_listing(path):
    # If it's a file, we just list it. If it's a directory, we have to
    # print out the contents.
    if os.path.isdir(path):
        dircontents = readdir.readdir(path)
        for entry in dircontents:
            print entry.to_json(extras = {"-meta type": typeinfo})
    elif os.path.lexists(path):
        print path
    else:
        msg = "%s: cannot access %s: No such file or directory"
        sys.stderr.write(msg % (sys.argv[0], path))

def main(arguments):
    if len(arguments.paths) == 0:
        arguments.paths = ['.']
        
    for path in arguments.paths:
        output_listing(path)


def ls(directory, pattern, recursive, follow_links):
    """Emits JSON entries for files matching the criteria.
    
    directory - the name of the directory to search
    pattern   - a globbing pattern to search for
    recursive - boolean indicating whether to do a
                recursive search
    """
    
    pass

#futureix_options = 

if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
