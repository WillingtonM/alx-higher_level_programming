#!/usr/bin/python3
"""MyList module"""

class MyList(list):
    """MyList class - Inherits from list
    """
    def print_sorted(self):
        """Prints list in ascending order"""
        print(sorted(self))
