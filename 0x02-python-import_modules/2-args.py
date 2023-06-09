#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arg_len = len(sys.argv) - 1
    if arg_len == 0:
        print("0 argument.")
    elif arg_len == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(arg_len))
    for index in range(arg_len):
        print("{:d}: {:s}".format(index + 1, sys.argv[index + 1]))