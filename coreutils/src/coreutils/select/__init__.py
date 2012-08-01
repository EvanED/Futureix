import os
import sys
import support.json as json
import argparse
import stat

parser = argparse.ArgumentParser()

def read_json_objects(stream):
    return (json.loads(line) for line in stream)


def get_predicates(args):
    def random_pred(obj):
        import random
        return random.randint(0,1)
    return [random_pred]

def main(args):
    preds = get_predicates(args)
    for obj in read_json_objects(sys.stdin):
        if all(p(obj) for p in preds):
            print json.dumps(obj)

if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
