#!/usr/bin/python3
"""Defines class Student."""


class Student:
    """Represent student."""

    def __init__(self, first_name, last_name, age):
        """
            Initialize a new Student.
            Args:
                first_name (str): First name of student.
                last_name (str): Last name of student.
                age (int): Age of student.
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

    def reload_from_json(self, json):
        """Replace all attributes of the Student.

        Args:
            json (dict): key/value pairs to replace attributes with.
        """
        for l, m in json.items():
            setattr(self, l, m)
