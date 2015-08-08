import os,sys,re

sys.path.append(os.path.dirname(__file__))

def format_one_line(name, plugin, flags):
    first_part = "        [%s," % name
    return '%s %s, %s],\n' % (first_part.ljust(28), plugin, flags)

def main(argv):
    src_file = argv[1]
    dest_file = argv[2]
    plugin_list = []

    # open need write file
    try:
        dest_handle = open(dest_file, "w")
    except Exception, details:
        print "Exception: %s" % details
        return -1
    
    # extend regular express: ^[ ]*(?P<name>\"[ ]*[0-9A-Za-z]+[ ]*\")[ ]*:[ ]*\([ ]*(?P<plugin>\"[ ]*[0-9A-Za-z]+[ ]*\")[ ]*[ ]*,[ ]*(?P<flags>\"[ ]*-l[0-9A-Za-z\-_.]+[ ]*-l[0-9A-Za-z\-_. ]+\")\)[ ]*,[ ]*$
    #                         = ^[ ]*(?P<name>\"[ ]*[\w]+[ ]*\")[ ]*:[ ]*\([ ]*(?P<plugin>\"[ ]*[\w]+[ ]*\")[ ]*[ ]*,[ ]*(?P<flags>\"[ ]*-l[\w\-.]+[ ]*-l[\w\-. ]+\")\)[ ]*,[ ]*$
    good_pattern   = re.compile(r'^[ ]*(?P<name>\"[ ]*[\w]+[ ]*\")[ ]*:[ ]*\([ ]*(?P<plugin>\"[ ]*[\w]+[ ]*\")[ ]*,[ ]*(?P<flags>\"[ ]*-l[\w\-.]+[ ]*\")[ ]*\)[ ]*,[ ]*$')
    extend_pattern = re.compile(r'^[ ]*(?P<name>\"[ ]*[\w]+[ ]*\")[ ]*:[ ]*\([ ]*(?P<plugin>\"[ ]*[\w]+[ ]*\")[ ]*[ ]*,[ ]*(?P<flags>\"[ ]*-l[\w\-.]+[ ]*-l[\w\-. ]+\")\)[ ]*,[ ]*$')
    line_list = []
    for origin_line in open(src_file, "r"):
        extend_group = extend_pattern.search(origin_line)
        if extend_group:
            full_info = format_one_line(extend_group.group("name"), extend_group.group("plugin"), extend_group.group("flags"))
            line_list.append(full_info)
            continue
        good_group = good_pattern.search(origin_line)
        if good_group:
            full_info = format_one_line(good_group.group("name"), good_group.group("plugin"), good_group.group("flags"))
            line_list.append(full_info)
            continue
        #others
        line_list.append(origin_line)
    dest_handle.writelines(line_list)
    dest_handle.close()
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
