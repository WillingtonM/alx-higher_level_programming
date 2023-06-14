#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_len = len(sys.argv) - 1
    if (arg_len == 0):
        print(arg_len, "arguments.")
    else:
        if (arg_len == 1):
            print(arg_len, "argument:".format(sys.argv[0]))
            print("1:", sys.argv[1])
        else:
            print(arg_len, "arguments:")

        for index in range(1, arg_len + 1):
                print("{}: {}".format(index, sys.argv[index]))