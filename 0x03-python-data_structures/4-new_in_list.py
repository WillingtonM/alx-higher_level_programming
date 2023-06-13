#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    if my_list:
        new_list = my_list.copy()
        ls_len = len(my_list)
        if idx < 0 or idx >= ls_len:
            return (my_list)
        else:
            new_list[idx] = element
            return (new_list)