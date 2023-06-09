#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arg_len = len(sys.argv) - 1
    if arg_len == 0:
        print("0 arguments.")
    elif arg_len == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_len))
    for index in range(arg_len):
        print("{}: {}".format(index + 1, sys.argv[index + 1]))