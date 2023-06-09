#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    arg_num = len(argv)
    i = 1
    if arg_num == 0:
        print("0 arguments.")
    elif arg_num == 1:
        print("1 argument:")
    else:
        print("{:d} arguments.".format(arg_num))
        while i < arg_num:
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
