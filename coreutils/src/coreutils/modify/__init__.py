import os
import sys
import support.json as json
import argparse
import stat

parser = argparse.ArgumentParser()
parser.add_argument('--remove-key', help='Comma-separated list of keys to remove')
parser.add_argument('--select-key', help='Comma-separated list of keys to select')

def read_json_objects(stream):
    return (json.loads(line) for line in stream)

def get_transforms(args):
    def make_remover(key):
        def remover(obj):
            try:
                del obj[key]
            except KeyError:
                pass
        return remover

    if args.remove_key:
        return [make_remover(key) for key in args.remove_key.split(",")]

    if args.select_key:
        print args.select_key
        sys.exit(1)

    return [lambda x: x]

def apply_transformations(obj, xforms):
    for xform in xforms:
        xform(obj)

def main(args):
    xforms = get_transforms(args)
    for obj in read_json_objects(sys.stdin):
        apply_transformations(obj, xforms)
        print json.dumps(obj)

if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
