#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arg_num = len(sys.argv) - 1
    if arg_num == 0:
        print("{:d} argument.".format(arg_num))
    elif arg_num == 1:
        print("{:d} argument:".format(arg_num))
    else:
        print("{:d} arguments.".format(arg_num))
    
    i = 1
    while i <= arg_num:
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
