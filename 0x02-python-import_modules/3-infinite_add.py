#!/usr/bin/python3
if __name__ == "__main__":
    """Print addition of arguments."""
    import sys

    sum = 0
    size = len(sys.argv) - 1
    for index in range(size):
        sum += int(sys.argv[index + 1])
    print("{}".format(sum))
