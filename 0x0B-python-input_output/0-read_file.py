#!/usr/bin/python3
"""Module for read_file method."""


def read_file(filename=""):
    """Reads text file & prints to STDOUT"""

    with open(filename, "r", encoding="UTF-8") as fo:
        for f_line in fo:
            print(f_line, end="")
