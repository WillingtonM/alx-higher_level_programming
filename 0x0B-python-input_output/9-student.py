#!/usr/bin/python3
"""Module defines class Student"""


class Student:
    """Represent student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student
        """
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self):
        """Gets dictionary representation of Student"""
        return self.__dict__
