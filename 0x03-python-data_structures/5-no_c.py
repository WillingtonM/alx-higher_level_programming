#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for item in my_string:
        if item is not 'c' and item is not 'C':
            new_str += item
    return (new_str)
