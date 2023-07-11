#!/usr/bin/python3
"""Standard input and computes metrics"""


def print_stats(size, status_codes):
    """
        Accumulated metrics.
        Args:
            size (int): Accumulated read file size.
            status_codes (dict): Accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for k in sorted(status_codes):
        print("{}: {}".format(k, status_codes[k]))

if __name__ == "__main__":
    import sys

    status_codes = {}
    v_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    size = 0
    counter = 0

    try:
        for l in sys.stdin:
            if counter == 10:
                print_stats(size, status_codes)
                counter = 1
            else:
                counter += 1

            l = l.split()

            try:
                size += int(l[-1])
            except (IndexError, ValueError):
                pass

            try:
                if l[-2] in v_codes:
                    if status_codes.get(l[-2], -1) == -1:
                        status_codes[l[-2]] = 1
                    else:
                        status_codes[l[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
