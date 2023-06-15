#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)
    avr = sum(list(map(lambda x: x[0]*x[1], my_list)))
    sze = sum(list(map(lambda x: x[1], my_list)))
    return (avr / sze)
