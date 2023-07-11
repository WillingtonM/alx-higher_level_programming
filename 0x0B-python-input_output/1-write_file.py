#!/usr/bin/python3
"""Defines file-writing method."""


def write_file(filename="", text=""):
    """
        Write string to UTF8 text file.
        Args:
            filename (str): Name of the file to write.
            text (str): Text to write to file.
        Returns:
            Number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as fo:
        return fo.write(text)
