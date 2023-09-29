#!/usr/bin/python3
"""Finds peak in list of unsorted integers"""


def find_peak(list_of_integers):
    """Find Peak in list

    Args:
        list_of_integers: list of int
    Returns:
        value or None
    """

    if list_of_integers is None or list_of_integers == []:
        return None
    low_key     = 0
    high_key    = len(list_of_integers)
    mid_key     = ((high_key - lo) // 2) + lo
    mid_key     = int(mid_key)
    if high_key == 1:
        return list_of_integers[0]
    if high_key == 2:
        return max(list_of_integers)
    if list_of_integers[mid_key] >= list_of_integers[mid_key - 1] and\
            list_of_integers[mid_key] >= list_of_integers[mid_key + 1]:
        return list_of_integers[mid_key]
    if mid_key > 0 and list_of_integers[mid_key] < list_of_integers[mid_key + 1]:
        return find_peak(list_of_integers[mid_key:])
    if mid_key > 0 and list_of_integers[mid_key] < list_of_integers[mid_key - 1]:
        return find_peak(list_of_integers[:mid_key])
