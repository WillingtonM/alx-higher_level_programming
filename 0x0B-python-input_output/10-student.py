#!/usr/bin/python3
"""Module defines class Student"""


class Student:
    """Represent student."""

    def __init__(self, first_name, last_name, age):
        """Initializes new Student
        """
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        """Get dictionary representation of Student
        """
        if (type(attrs) == list and
                all(type(elmnt) == str for elmnt in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__

