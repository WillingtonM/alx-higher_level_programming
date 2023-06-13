#!/usr/bin/python3
def max_integer(my_list=[]):
    ls_len = len(my_list)
    if 0 == ls_len:
        return None
    return sorted(my_list)[-1]
