#!/usr/bin/python3

def safe_print_integer(value):
    '''
    Safely prints an integer
    '''
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        return False
