import os

def parse_subprocess_memory_usage():
    list_dir = os.listdir()
    all_memory_usage = []
    for elem in list_dir:
        if ".log" in elem:
            with open(elem, 'r') as f:
                for line in f:
                    line = line.strip('\n')
                    if len(line) > 0:
                        if "Maximum resident set size (kbytes)" in line:
                            splitted_line = line.split()
                            all_memory_usage.append(int(splitted_line[-1]))


    print("The maximum memory usage between subprocesses: {0} MB".format(max(all_memory_usage)/1024))




if __name__ == '__main__':
    parse_subprocess_memory_usage()
