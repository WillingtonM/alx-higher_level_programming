#!/usr/bin/python3
"""Defines Prints a text with 2 new lines after each, cof these characters: . ? and :
Attributes:
    text_indentation: Prints a text with specific conditions
"""

def text_indentation(text):
    """Prints text with 2 new lines after .?: characters.

    Args:
        text: String to be examined.

    Raises:
        TypeError: If text is not type str.
    """
    err_1 = "text must be a string"
    if not isinstance(text, str):
        raise TypeError(err_1)

    for delimeter in ".:?":
        text = (delimeter + "\n\n").join([l.strip(" ") for l in text.split(delimeter)])

    print(text, end="")
