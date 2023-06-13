#!/usr/bin/python3
def element_at(my_list, idx):
    ls_len = len(my_list)
    return(my_list[idx] if 0 <= idx < ls_len else "None")
