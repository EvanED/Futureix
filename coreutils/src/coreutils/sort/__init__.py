import sys
import support.json as json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-k', '--key', help='Comma-separated list of sort keys (first item in the list is sorted first)')

def read_json_objects(stream):
    return (json.loads(line) for line in stream)

def main(args):
    assert args.key
    objs = sorted(read_json_objects(sys.stdin),
                  key=lambda o: o[args.key])
    for obj in objs:
        print json.dumps(obj)

if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
