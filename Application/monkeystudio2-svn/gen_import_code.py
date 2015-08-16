import os,sys

def main(argv):
    if len(argv) < 6:
        print "need more params."
        return -1

    src_file = argv[1]
    src_file_1 = argv[2]
    dest_file = argv[3]
    map_file = argv[4]
    script_f = argv[5]
    try:
        s_handle = open(src_file, "r")
        s_buff = s_handle.readlines()
        s_handle.close()
    except Exception, detail:
        print "Exception: {0}".format(detail)
        return -1
    try:
        s_1_handle = open(src_file_1, "r")
        cmp_buff = s_1_handle.readlines()
        s_1_handle.close()
    except Exception, detail:
        print "Exception: {0}".format(detail)
        return -1
    try:
        d_handle = open(dest_file, "w")
        m_handle = open(map_file, "w")
        sc_handle = open(script_f, "w")
        d_handle.write("#pragma GCC visibility push(default)\n");
        d_handle.write("#define DLL_PUBLIC __attribute__ ((visibility (\"default\")))\n");
        sc_handle.write("{ \n global: ")
        result_buff = []
        for line in s_buff:
            if line in cmp_buff:
                continue
            oneline = line[:-1]
            if oneline in result_buff:
                continue
            if oneline[:2] != '_Z':
                continue
            result_buff.append(oneline)
            sc_handle.write(" %s; \n" % oneline)
            m_handle.write("%s \n" % oneline)
            d_handle.write("extern void DLL_PUBLIC %s () ;\n" % oneline)
        d_handle.write("#pragma GCC visibility pop\n");
        m_handle.write("__monkeystudio_import_functions \n")
        sc_handle.write(" local: *; \n};\n")
        sc_handle.close()
        m_handle.close()
        d_handle.write("\nvoid __monkeystudio_import_functions ()\n{\n")
        result_buff = []
        for line in s_buff:
            if line in cmp_buff:
                continue
            oneline = line[:-1]
            if oneline in result_buff:
                continue
            if oneline[:2] != '_Z':
                continue
            result_buff.append(oneline)
            d_handle.write("    %s ();\n" % oneline)
        d_handle.write("}\n\n")
        d_handle.close()
    except Exception, detail:
        print "Exception: {0}".format(detail)
        return -1
    return 0
     
if __name__ == '__main__':
    sys.exit(main(sys.argv))
