import sys, md5

if (len(sys.argv) == 2):
    sums_file = open(sys.argv[1])
    summer = md5.new()
