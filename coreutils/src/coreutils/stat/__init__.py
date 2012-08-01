import os
import sys
import support.json as json
import argparse
import stat

parser = argparse.ArgumentParser()

def read_json_objects(stream):
    return (json.loads(line) for line in stream)

def fstat_translate(obj):
    path = None
    try:
        path = os.path.join(obj["in-directory"], obj["name"])
    except AttributeError:
        path = obj["path"]

    st = os.stat(path)
    out = {}
    #if "kind" not in obj:
    #    out["kind"] = to_kind(st.st_mode)
    out["permissions"] = stat.S_IMODE(st.st_mode)
    out["inode"] = st.st_ino
    out["device"] = st.st_dev
    out["number-hard-links"] = st.st_nlink
    out["owner-uid"] = st.st_uid
    out["owner-gid"] = st.st_gid
    out["size"] = st.st_size
    out["access-time"] = st.st_atime
    out["modification-time"] = st.st_mtime
    out["ctime"] = st.st_ctime

    def set_if_present(out, out_field, st, st_field):
        try:
            out[out_field] = st.__getattribute__(st_field)
        except AttributeError:
            pass

    # "On some Unix systems (such as Linux), the following attributes
    # may also be available"
    set_if_present(out, "number-blocks", st, "st_blocks")
    set_if_present(out, "filesystem-blocksize", st, "st_blksize")
    set_if_present(out, "device-type", st, "st_rdev")
    set_if_present(out, "user-flags", st, "st_flags")

    # "On other Unix systems (such as FreeBSD), the following
    # attributes may be available (but may be only filled out if root
    # tries to use them)"
    set_if_present(out, "inode-generation", st, "st_gen")
    set_if_present(out, "creation-time", st, "st_birthtime")

    # "On Mac OS systems, the following attributes may also be
    # available"
    set_if_present(out, "rsize", st, "st_rsize")
    set_if_present(out, "creator", st, "st_creator")
    set_if_present(out, "type", st, "st_type")

    # "On RISCOS systems, the following attributes are also available"
    set_if_present(out, "ftype", st, "st_ftype")
    set_if_present(out, "attrs", st, "st_attrs")
    set_if_present(out, "obtype", st, "st_obtype")

    return out

def accumulate_objs(dest, source, prefer=None):
    if prefer is None:
        prefer = dest
    for (k,v) in source.iteritems():
        if k in dest and prefer == dest:
            pass
        else:
            dest[k] = v


def main(args):
    for obj in read_json_objects(sys.stdin):
        stat = fstat_translate(obj)
        accumulate_objs(obj, stat)
        print json.dumps(obj)

if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
