#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        avr = sum(list(map(lambda x: x[0]*x[1], my_list)))
        sze = sum(list(map(lambda x: x[1], my_list)))
        return (avg/size)
    return 0
