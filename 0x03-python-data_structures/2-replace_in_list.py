#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    ls_len = len(my_list)
    if 0 <= idx < ls_len:
        my_list[idx] = element
    return(my_list)
