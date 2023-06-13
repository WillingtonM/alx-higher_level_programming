#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list[:]
    for count, item in enumerate(my_list):
        if item % 2 == 0:
            new_list[count] = True
        else:
            new_list[count] = False
    return(new_list)
