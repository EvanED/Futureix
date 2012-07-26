import sys
import support.json as json
import argparse

parser = argparse.ArgumentParser()

def read_json_objects(stream):
    return (json.loads(line) for line in stream)

def get_column_specs(objects):
    """A colum spec is a tuple (name, size)"""
    col_specs = {}
    for obj in objects:
        for (k,v) in obj.iteritems():
            v = str(v)
            spec = col_specs.get(k, (k, len(k)))
            if len(v) > spec[1]:
                spec = (k, len(v))
            col_specs[k] = spec
    return list(col_specs.itervalues())


def print_object(obj, cols):
    def col_contribution(name, size):
        try:
            field = str(obj[name])
        except KeyError:
            field = "--"
        return ("{: <%s}" % str(size)).format(field)
    print "  ".join(col_contribution(name, size) for (name, size) in cols)

def print_header(cols):
    names = {name:name for (name, _) in cols}
    seps = {name:("-"*size) for (name, size) in cols}
    print_object(names, cols)
    print_object(seps, cols)


def main(args):
    objs = list(read_json_objects(sys.stdin))
    cols = get_column_specs(objs)
    print_header(cols)
    for obj in objs:
        print_object(obj, cols)

if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
