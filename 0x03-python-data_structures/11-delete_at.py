#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    ls_len = len(my_list)
    if 0 <= idx < ls_len:
        del(my_list[idx])
    return(my_list)
