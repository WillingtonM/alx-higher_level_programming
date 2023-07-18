#!/usr/bin/python3
"""Defines a base model class of all other classes for this project"""
import json
import csv
import turtle

class Base:
    """
        Represent base model.

        Represents "Base" for all other classes*.

        Attributes:
            __nb_objects (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
            Initialize a new Base.

            Args:
                id (int): Identity of new Base.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Return JSON serialization of list of dicts.

            Args:
                list_dictionaries (list): List of dictionaries.
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Write JSON serialization of list of objects to file.

            Args:
                list_objs (list): List of inherited Base instances.
        """
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                ls_dicts = [lo.to_dictionary() for lo in list_objs]
                jsonfile.write(Base.to_json_string(ls_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
            Return deserialization of JSON string.

            Args:
                json_string (str): JSON str representation of list of dicts.
            Returns:
                If json_string is None or empty - empty list.
                Otherwise - Python list represented by json_string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            Return class instantied from dictionary of attributes.

            Args:
                **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                rect_new = cls(1, 1)
            else:
                rect_new = cls(1)
            rect_new.update(**dictionary)
            return rect_new

    @classmethod
    def load_from_file(cls):
        """
            Return list of classes instantiated from file of JSON strings.

            Reads from `<cls.__name__>.json`.
            Returns:
                If file does not exist - empty list.
                Otherwise - list of instantiated classes.
        """
        file_name = str(cls.__name__) + ".json"
        try:
            with open(file_name, "r") as jsonfile:
                ls_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in ls_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
            Write CSV serialization of list of objects to file.

            Args:
                list_objs (list): List of inherited Base instances.
        """
        file_name = cls.__name__ + ".csv"
        with open(file_name, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                wd = csv.DictWriter(csvfile, field_names=field_names)
                for obj in list_objs:
                    wd.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
            Return list of classes instantiated from CSV file.

            Reads from `<cls.__name__>.csv`.
            Returns:
                If file does not exist - empty list.
                Otherwise - list of instantiated classes.
        """
        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                ls_dicts = csv.DictReader(csvfile, field_names=field_names)
                ls_dicts = [dict([i, int(j)] for i, j in ld.items())
                              for ld in ls_dicts]
                return [cls.create(**ld) for ld in ls_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
            Draw Rectangles & Squares using turtle module.

            Args:
                list_rectangles (list): List of Rectangle objects to draw.
                list_squares (list): List of Square objects to draw.
        """
        trtl = turtle.Turtle()
        trtl.screen.bgcolor("#b7312c")
        trtl.pensize(3)
        trtl.shape("turtle")

        trtl.color("#ffffff")
        for rect in list_rectangles:
            trtl.showturtle()
            trtl.up()
            trtl.goto(rect.x, rect.y)
            trtl.down()
            for x in range(2):
                trtl.forward(rect.width)
                trtl.left(90)
                trtl.forward(rect.height)
                trtl.left(90)
            trtl.hideturtle()

        trtl.color("#b5e3d8")
        for sqr in list_squares:
            trtl.showturtle()
            trtl.up()
            trtl.goto(sqr.x, sqr.y)
            trtl.down()
            for x in range(2):
                trtl.forward(sqr.width)
                trtl.left(90)
                trtl.forward(sqr.height)
                trtl.left(90)
            trtl.hideturtle()

        turtle.exitonclick()
