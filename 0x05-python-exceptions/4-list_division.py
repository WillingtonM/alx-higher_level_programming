#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    '''
    Divides elements of 2 lists with the same list index
    '''
    list_res = []
    for i in range(list_length):
        div = 0
        try:
            a, b = (my_list_1[i], my_list_2[i])
            div = a / b
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            list_res.append(div)
    return list_res
