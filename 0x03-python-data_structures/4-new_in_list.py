#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    ls_len = len(my_list)
    if idx < 0 or idx > my_list - 1):
        return (my_list)

    copy = my_list[:]
    copy[idx] = element
    return (copy)
