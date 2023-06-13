#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    ls_len = len(my_list)
    if idx < 0 or idx >= ls_len:
        return (my_list)

    new_list[idx] = element
    return (new_list)