#!/usr/bin/python3
def weight_average(my_list=[]):
    avg = 0
    size = 0
    if my_list and len(my_list):
        for x in my_list:
            avg += (x[0] * x[1])
            size += (x[1])
        return (avg/size)
    return 0