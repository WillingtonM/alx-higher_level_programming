#!/usr/bin/python3
"""Module for append_after method."""


def append_after(filename="", search_string="", new_string=""):
    """Function for inserting text after search string"""
    r_lines = []
    with open(filename, "r", encoding="utf-8") as fo:
        r_lines = fo.readlines()
        x = 0
        while x < len(r_lines):
            if search_string in r_lines[x]:
                r_lines[x:x + 1] = [r_lines[x], new_string]
                x += 1
            x += 1
    with open(filename, "w", encoding="utf-8") as fo:
        fo.writelines(r_lines)
