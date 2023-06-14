#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_elem = [x for x in set_1 for y in set_2 if x == y]
    return common_elem
