import os,sys

def main(argv):
    if len(argv) < 3:
        print "need more params."
        return -1

    src_file = argv[1]
    dest_file = argv[2]
    try:
        s_handle = open(src_file, "r")
        s_buff = s_handle.readlines()
        s_handle.close()
    except Exception, detail:
        print "Exception: {0}".format(detail)
        return -1
    try:
        d_handle = open(dest_file, "w")
        for line in s_buff:
            d_handle.write("extern void %s ();\n" % line[:-1])
        d_handle.write("\nstatic void __gst_import_functions ()\n{\n")
        for line in s_buff:
            d_handle.write("    %s ();\n" % line[:-1])
        d_handle.write("}\n\n")
        d_handle.close()
    except Exception, detail:
        print "Exception: {0}".format(detail)
        return -1
    return 0
     
if __name__ == '__main__':
    sys.exit(main(sys.argv))
