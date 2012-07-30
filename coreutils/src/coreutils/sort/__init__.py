import sys
import support.json as json
import argparse

parser = argparse.ArgumentParser()

def read_json_objects(stream):
    return (json.loads(line) for line in stream)

def main(args):
    objs = list(read_json_objects(sys.stdin))
    for obj in objs:
        print json.dumps(obj)

if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
