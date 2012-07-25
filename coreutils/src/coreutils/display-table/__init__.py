import sys
import support.json as json
import argparse

parser = argparse.ArgumentParser()

def main(args):
    for line in sys.stdin:
        obj = json.loads(line)
        print obj

if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
