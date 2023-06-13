#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_tmp = my_list[:]
    ls_len = len(my_list)
    if 0 <= idx < ls_len:
        list_tmp[idx] = element
        return(list_tmp)
    return(my_list)