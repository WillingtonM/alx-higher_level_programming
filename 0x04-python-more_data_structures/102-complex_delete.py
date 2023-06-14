#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for x_key in list(a_dictionary):
        if a_dictionary[x_key] == value:
            del a_dictionary[x_key]
    return a_dictionary
