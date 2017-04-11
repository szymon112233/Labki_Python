import sys, hashlib

if (len(sys.argv) == 2):
    sums_file = open(sys.argv[1])
    summer_lines = sums_file.readlines()
    files = {}
    for line in summer_lines:
        splitted_line = line.split()
        files[splitted_line[1]] = splitted_line[0]
    for filename in files:
        file = open(filename)
        sum = hashlib.md5(file.read()).hexdigest()
        if (files[filename] == sum):
            print filename + ": Suma poprawna"
        else:
            print filename + ": Suma niepoprawna"

