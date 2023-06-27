#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    ''' Safely executes function '''
    try:
        f_res = fct(*args)
        return f_res
    except Exception as err:
        sys.stdout.write("Exception: " + str(err) + "\n")
        return
