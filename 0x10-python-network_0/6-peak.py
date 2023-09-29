#!/usr/bin/python3
"""Finds peak in list of unsorted integers"""

def find_peak(list_of_integers):
    """
        Find Peak in list

        Args: list_of_integers: list of int
        Returns: value or None
    """

    int_ls = list_of_integers
    len_ls = len(int_ls)
    if (len_ls <= 2):
        return (None)
    for z in range(1, len_ls - 1):
	    if (int_ls[z - 1] <= int_ls[z] >= int_ls[z + 1]):
	        return (int_ls[z])
    return (None)
